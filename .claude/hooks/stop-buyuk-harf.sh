#!/usr/bin/env bash
# BÜYÜK-HARF VURGU FRENİ — Stop hook (deneysel m.29; kurulum 2026-09-15, Salih yan-görevi 09-15:
# "caps lock açık bir şekilde kelime vurgusu görmek istemiyorum"; kök neden analizi
# raporlar/2026-09/buyuk-harf-vurgu-analizi-2026-09-15.md).
# Mekanizma: cevap bitince son asistan mesajı taranır; kısaltma/kod dışı ≥4 harfli tamamı-büyük
# sözcük varsa Claude durdurulmaz, "kalın harfe çevir" gerekçesiyle devam ettirilir (decision=block).
# Sonsuz döngü freni: stop_hook_active=true ise (ikinci tur) fren pas geçer.
# Beyaz liste: teknik kısaltmalar + kanon durum sözcükleri (DONE/PASS/FAIL/AS-OF) + faz adları.
# Kod blokları (```…```) ve satır-içi kod (`…`) taranmaz; Salih beyanı alıntıları ("aynen: …") taranmaz.
input=$(cat)
PY=$(command -v python3 || command -v python)
GIRDI=$(mktemp); printf '%s' "$input" > "$GIRDI"; trap 'rm -f "$GIRDI"' EXIT
"${PY:-python3}" - "$GIRDI" <<'EOF'
import sys, json, re, pathlib
d = json.load(open(sys.argv[1]))
if d.get("stop_hook_active"):
    sys.exit(0)
son = d.get("last_assistant_message") or None   # resmî alan (hooks docs, AS-OF 2026-09-15); yoksa transkriptten
tp = d.get("transcript_path")
if not son and (not tp or not pathlib.Path(tp).exists()):
    sys.exit(0)
for line in (open(tp, errors="ignore") if not son else []):
    try:
        r = json.loads(line)
    except Exception:
        continue
    if r.get("type") == "assistant":
        m = r.get("message", {})
        txt = "".join(c.get("text", "") for c in m.get("content", []) if c.get("type") == "text")
        if txt.strip():
            son = txt
if not son:
    sys.exit(0)
IZ = set("""DONE PASS FAIL WARN ERROR AS-OF PROBE PLAN TEACH CLOSE DAG MCP OWASP YAML JSON YML CSV HTML HTTP HTTPS PDF SVG PNG
CI CD API SQL URL URI CLI GUI IDE SDK LLM RAG HITL ASR NDCG MAP MRR GSM8K SWE UK AISI AWS DEA GCP MIT OCW README HEAD MEMORY CLAUDE
JARVIS JARVİS FRIDAY CARVIS ATLAS OPUS SONNET HAIKU FABLE GPT KB MB GB TODO FIFO LIFO SHA UTC TR EN ID UID DNS TLS SSH OAUTH
NEMO NLP ML AI ETL ELT DBT SPARK MLOPS RAG LTR NDCG PR PRS CTR ROC AUC F1 REGEX BPE ROPE KV SFT RLHF CVE CVSS CWE OWASP UTF
İB KB-08 EK SKILL SCRIPTLER KILAVUZ""".split())
metin = re.sub(r"```.*?```", " ", son, flags=re.S)
metin = re.sub(r"`[^`\n]*`", " ", metin)
metin = re.sub(r"aynen:\s*[\"“][^\"”]*[\"”]", " ", metin)
metin = re.sub(r"https?://\S+", " ", metin)
adaylar = re.findall(r"(?<![\w./-])[A-ZÇĞİÖŞÜ]{4,}(?![\w./-])", metin)
ihlal = sorted({w for w in adaylar if w not in IZ})
if not ihlal:
    sys.exit(0)
neden = ("Büyük-harf vurgu freni (Salih 09-15): son cevapta tamamı büyük harfle yazılmış sözcük var: "
         + ", ".join(ihlal[:12]) + (" …" if len(ihlal) > 12 else "")
         + ". Vurguyu kalın harfle (**sözcük**) ya da cümle yapısıyla ver; büyük harf yalnız kısaltma/durum-sözcüğü. "
           "Cevabı bu sözcükler düzeltilmiş hâlde yeniden yaz (içerik aynı kalsın).")
print(json.dumps({"decision": "block", "reason": neden}, ensure_ascii=False))
EOF
