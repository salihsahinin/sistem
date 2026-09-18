#!/usr/bin/env bash
# BÜYÜK-HARF VURGU FRENİ — Stop hook (deneysel m.29; kurulum 2026-09-15, Salih yan-görevi 09-15:
# "caps lock açık bir şekilde kelime vurgusu görmek istemiyorum"; kök neden analizi
# raporlar/2026-09/buyuk-harf-vurgu-analizi-2026-09-15.md).
# Mekanizma: cevap bitince son asistan mesajı + son turun araç girdileri (widget/Write/Edit, v0.3) taranır; kısaltma/kod dışı ≥4 harfli tamamı-büyük
# sözcük varsa Claude durdurulmaz, "kalın harfe çevir" gerekçesiyle devam ettirilir (decision=block).
# Sınır: hook gösterilmiş çıktıyı GERİ ÇEKEMEZ; yalnız ekleme yaptırır. Bu yüzden düzeltme TEK SATIR
# (09-15 vakası: "cevabı yeniden yaz" talimatı aynı soruyu iki kez gösterdi → yan oturum transkripti
# 4ac5ca1c kayıt 449/453). Ölçüm: block sayısı 5 seans sonra (defter 09-15 Salih hükmü).
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
# v0.3 (09-17, Salih "büyük harf sorunu neden sürüyor" analizi): yalnız son metin değil, SON TURUN araç girdileri de taranır —
# mcp__visualize show_widget.widget_code (JS dizeleri dahil; HTML etiketleri/CSS düşer), Write.content, Edit.new_string,
# Artifact/Lavish için yazılan .html içerikleri. 09-17 vakası: caps sözcükler widget JS dizesindeydi, metin tarayıcısı görmedi.
ARAC_ALAN = {"mcp__visualize__show_widget": "widget_code", "Write": "content", "Edit": "new_string"}
arac_metin = []
if tp and pathlib.Path(tp).exists():
    tur = []   # son user mesajından sonraki asistan satırları
    for line in open(tp, errors="ignore"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("type") == "user":
            tur = []
        elif r.get("type") == "assistant":
            tur.append(r.get("message", {}))
    for m in tur:
        for c in m.get("content", []):
            if c.get("type") == "text" and c.get("text", "").strip() and not son:
                son = c["text"]
            if c.get("type") == "tool_use" and c.get("name") in ARAC_ALAN:
                v = (c.get("input") or {}).get(ARAC_ALAN[c["name"]], "")
                if isinstance(v, str) and v.strip():
                    v = re.sub(r"<style.*?</style>", " ", v, flags=re.S)       # CSS düşer
                    v = re.sub(r"<[^>]+>", " ", v)                                # etiketler düşer; JS/metin kalır
                    v = re.sub(r"&[a-z]+;|&#\d+;", " ", v)
                    arac_metin.append(v)
if not son and not arac_metin:
    sys.exit(0)
IZ = set("""AS-OF DAG MCP OWASP YAML JSON JSONL YML CSV HTML HTTP HTTPS PDF SVG PNG AXI GNHF OCR USD EUR IAM ASCII FTS BM25 RRF NLI XML
CI CD API SQL URL URI CLI GUI IDE SDK LLM RAG HITL ASR NDCG MAP MRR GSM8K SWE UK AISI AWS DEA GCP MIT OCW README HEAD MEMORY CLAUDE
JARVIS JARVİS FRIDAY CARVIS ATLAS OPUS SONNET HAIKU FABLE GPT KB MB GB TODO FIFO LIFO SHA UTC TR EN ID UID DNS TLS SSH OAUTH
NEMO NLP ML AI ETL ELT DBT SPARK MLOPS RAG LTR NDCG PR PRS CTR ROC AUC F1 REGEX BPE ROPE KV SFT RLHF CVE CVSS CWE OWASP UTF
İB KB-08 EK SKILL SCRIPTLER KILAVUZ MECE""".split())   # durum sözcükleri (DONE, KALAN, BAYAT…) artık `kod` biçiminde yazılır (Salih 09-15 "büyük harf = kod")
metin = re.sub(r"```.*?```", " ", (son or ""), flags=re.S)
metin = metin + " " + " ".join(arac_metin)   # v0.3: araç girdileri (widget/dosya) metinle birlikte
metin = re.sub(r"`[^`\n]*`", " ", metin)
metin = re.sub(r"aynen:\s*[\"“][^\"”]*[\"”]", " ", metin)
metin = re.sub(r"https?://\S+", " ", metin)
adaylar = re.findall(r"(?<![\w./-])[A-ZÇĞİÖŞÜ]{3,}(?![\w./-])", metin)   # ≥3 harf (Salih 09-15: "VAR", "SANA" da vurgu)
ihlal = sorted({w for w in adaylar if w not in IZ})
if not ihlal:
    sys.exit(0)
neden = ("Büyük-harf vurgu freni (Salih 09-15; v0.3 09-17 araç girdileri dahil): son turda (cevap ya da widget/dosya içeriği) tamamı büyük harfle yazılmış sözcük var: "
         + ", ".join(ihlal[:12]) + (" …" if len(ihlal) > 12 else "")
         + ". Vurguyu kalın harfle (**sözcük**) ya da cümle yapısıyla ver; büyük harf yalnız kısaltma/durum-sözcüğü. "
           "Cevabı YENİDEN YAZMA (09-15 arızası: tam yeniden yazım Salih'e aynı soruyu iki kez gösterdi); "
           "yalnız tek satır ekle: 'Düzeltme: <SÖZCÜK> → **sözcük**' ve dur.")
print(json.dumps({"decision": "block", "reason": neden}, ensure_ascii=False))
EOF
