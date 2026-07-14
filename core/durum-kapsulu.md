# Durum Kapsülü

*Her oturumun İLK okuduğu dosya. Üzerine yazılır; arşiv değildir.*

**Güncelleme:** 2026-07-14 sabah vardiyası (Carvis) — P0-P6 ONAYLANDI (Salih; P5=minimum canlı demo sabitlendi) · K-014 KAPANDI (profil chat'te canlı doğrulandı) · 15 Tem PARALEL DENEME değişmedi

## Şu an
- **K-017 KAPANDI — kanalın ilk koşumu:** Cem'in research-agent'ı (V25 istisna damgalı, `.claude/agents/`) 7 eksende 70 kaynaklı bulgu üretti (58 D / 12 K / 0 X; 78 ajan, ~2,4M token — Fable ULTRAWORKFLOW/en-yüksek efor: ilk-koşum bilinçli maksimum, maliyet kıyasları bu parametreyle okunur). Rapor: `cc/rapor-2026-07-13-1.md` · defter ilk satırı yazıldı. Adaylar kartlara dağıtıldı: K-002 (yfinance sigortası) · K-009 gündemi (otonomi merdiveni + güvenlik emsalleri) · K-015 (envanter+/goal notu) · K-016 (eval/format ilhamları) · K-019/K-020 (yeni).
- **Yeni araç seti:** research-agent subagent + context7 MCP (`.mcp.json`, http, anahtarsız) + Orca bilgisi (CLI: `orca worktree create --agent claude-code --prompt` · `orca automations create` — makinede kurulu 07-09'dan).
- **Doktrin/desen:** V52 tetik-sahipliği araçsal, nihai misyon otomasyon (cc/README revize) · V53 LLM Council adayı (kural adaylarıyla) · V54 literatür-yokluğu simetrisi.
- **Operasyon:** pano BLOKE+SON BİTEN bölümü 07-13'ten beri KESİKMİŞ → git 8b281ec'ten onarıldı (V43 4. vaka; ders: bölüm-bütünlüğü de doğrulanır). Mount .git kilidi sürüyor → klon-push standart yol (bugün 6 commit böyle gitti).
- **Partisyon planı P0-P6 ONAYLI (Salih 07-14; P5 DONE = minimum canlı demo SABİT):** P0 ✅ (K-014) · P1=15 Tem paralel deneme · P2=16-20 Tem K-015 kuyruğu+K-018 · P3=K-009/K-010 otonomi kapısı (~Ağu başı) · P4=ölçüm+deney (Ağu) · P5=Jarvis v1+demo (≤10 Eki; PAT yenileme P5 DONE koşulu) · P6=K-004 (Kas). Kritik yol: Faz2+4→K-009→K-010→V39, tampon yok (kabul edildi). Plan dosyası: `raporlar/partisyon-plani-P0-P6-2026-07-14.md` · ilk tahminler senaryo-defterinde. Her partisyon kapanışında tahmin-vs-gerçek senaryo-defterine (Brier deseni).

## Açık borçlar
- **V39 kavram-sözlüğü dar koşumu:** gorev-2 adayı (7/10 terim dış-eşleşmesiz: tek-nokta değişimi=ablation ailesi · credit-assignment · transfer/hizalama · bağlı-çift=çok-amaçlı optimizasyon) — Salih kararı bekliyor; V26 örneklem-denetimli, ~400-600K token tahmini.
- K-019 ilk boş vardiyada · wiki borçları (tez #0 + çelişki kapısı sayfası) · KILAVUZ okuma (Salih) · tetikliler: K-011 (gün Salih'te) · K-004 (Kasım) · PAT ~10 Ekim ölür.

## Sonraki ilk iş
- **15 Temmuz: İLK PARALEL DENEME** (talimat: `PARALEL-VARDIYA-ILK-DENEME.md`) — DEĞİŞMEDİ:
  - Oturum A "günaydın" → `claude --version`+`doctor` envanteri (2 dk, K-015 icra notu) → loop-eng Faz 2 (/goal, ilk emir cc/ kanalından) + Faz 4 (Routine) + Karpathy revizyonu (eşlik: bbycroft.net/llm).
  - Oturum B "günaydın, PortRisk" → Sprint 1: yfinance + getiriler + **rate-limit sigortası BAŞTAN (K-002 eki)** + pytest + push (commit Salih'in; 