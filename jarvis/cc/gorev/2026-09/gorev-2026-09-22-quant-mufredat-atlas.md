# Görev emri — quant öğrenme müfredatı Atlas koşumu (2026-09-22)

`[tip: gorev | kaynak: jarvis-terminal 09-22 | tarih: 2026-09-22 | hedef: cc/rapor | sema: v2 | koken: jarvis/claude-fable-5-1/2026-09-22]`

**Tetik (Salih 09-22 aynen):** "quant alanına girmek ve öğrenmeye başlamak istiyorum,bunun için atlas araştırmasıyla önce uygun quant öğrenme sırasına ait müfredatı bul ve oluştur.mevcut müfredattan sıfırdan ilerleyebilmek için her bir konu başlığına dag oluşturacak şekilde quant öğrendiğim bir ajan oluştur."

**Soru:** Sıfırdan quantitative finance öğrenmek isteyen matematik mühendisliği son sınıf öğrencisi (İTÜ [?]; lineer cebir · olasılık · analiz · Python temel var; PortRisk küçük projesi var) için 2026'da sektörde kabul gören öğrenme sırası nedir; her konu başlığının ön-koşulu (DAG kenarı) ve kabul gören kaynağı (kitap/kurs/ders notu) nedir?

**Zaman-zemini (Karar 68):** bugün 2026-09-22; her iddia AS-OF damgalı; kaynağın yayım tarihi yazılır; "güncel" = 2024 sonrası doğrulanmış.

## Aileler (dik; her biri bağımsız tez ajanı, Sonnet)
- **A — Program müfredatları:** MFE/MSCF/quant yüksek lisans müfredatları (CMU MSCF · Baruch MFE + pre-MFE primer · NYU Courant MathFin · Columbia MSFE · Oxford MCF · Princeton MFin · ETH/EPFL) → zorunlu ders sırası, ön-koşul zinciri, hangi konu hangi dönemde.
- **B — Klasik kaynak sırası (stokastik hesap · türev fiyatlama · portföy/risk):** Hull · Shreve I-II · Wilmott · Björk · Joshi · Grinold-Kahn · Meucci · Jorion; QuantNet "Master Reading List", QuantStart yol haritası, Mark Joshi "On becoming a quant"; okuma sırası ve neden.
- **C — Veri tarafı (zaman serisi · ekonometri · ML/quant araştırma):** Tsay · Hamilton · Campbell-Lo-MacKinlay · López de Prado (AFML, ML for Asset Managers) · Chan · Isichenko · Paleologo; 2024-2026 sektör pratiği (ML'in quant araştırmadaki yeri, alternatif veri, LLM kullanımı).
- **D — Uygulama + kariyer:** backtest çerçeveleri (vectorbt · backtrader · zipline-reloaded · QuantConnect Lean) · veri kaynakları (yfinance · Polygon · WRDS/CRSP) · piyasa mikroyapısı (O'Hara · Harris · Bouchaud) · mülakat hazırlığı (Green Book, Heard on the Street, "150 Most Frequently Asked Questions") · 2026 iş ilanı beklentileri (quant researcher vs trader vs dev); Türkiye + küresel.

## Çıktı disiplini (atlas-kosum §3)
- URL zorunlu · rakam kaynaklı, kestirim `[?]` · uydurma yasak, "bulunamadı" meşru · 403/paywall bayraklanır · her iddia AS-OF damgalı · **≥2 birincil kaynak gerçekten açılır** (WebFetch), yalnız arama-özeti K'da kalır.
- Rapor şablonu: `.claude/skills/atlas-kosum/references/rapor-sablonu.md`; her iddia D/K/X + URL.
- Hedef dosya: `cc/rapor/2026-09/rapor-2026-09-22-quant-mufredat-tez-<A|B|C|D>.md` (≤ 12 KB).
- Son bölüm zorunlu: **"DAG önerisi"** — konu düğümleri (İngilizce sektör başlığıyla) + `önkoşul → konu` kenarları listesi + her düğüme 1 kaynak.

## Aşamalar
1. Tez A-D paralel (bu dosya) → 2. antitez (iddia listesi, gerekçesiz; CoVe-Factored) → 3. V26 sondaj tablosu → 4. hakem (`subagent_type: hakem`, beklenti maskesi: "ne bulunmalı" verilmez) → 5. sentez `raporlar/2026-09/2026-09-22-quant-mufredat-atlas.md` → 6. ajan doğumu (spec + `alan-ajani-dogur.py`) + DAG dosyası `<ajan>/ogrenme/quant/mufredat-dag.md`.

`kosum_profili:` tez 4 × Sonnet medium · antitez 4 × Sonnet medium · hakem Sonnet (eskalasyon b: `TUTMADI` ≥3 → Opus 5.5) · sentez Jarvis. Beklenen alt-ajan token ≈ 0,8-1,2 M `[?]` (Karar 102 koşumu 10 ajan 864k; bitirme-tezi 16 ajan 1,77 M).
