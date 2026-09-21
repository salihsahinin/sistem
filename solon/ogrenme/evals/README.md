# LLM / Ajan Değerlendirme Mühendisliği (evals) — Sıfırdan Pratik Serisi (Karar 94 M2, 2026-09-11)

> **Salih kararı (masa-11 M2, 09-11 aynen seçenek metni):** "LLM/ajan değerlendirme mühendisliği (evals): eval seti + LLM-as-judge kalibrasyonu + trajektori/araç-çağrısı testi + CI regresyon; araçlar promptfoo/DeepEval/Inspect AI; kamu veri." Gerekçe (masa kanıt tablosu): staj rolü = agentic coding ekibinde **doğrulama katmanı** (K-022); dbt Labs 2026 anketi %72 AI-destekli kodlama ↔ yalnız %24 AI-destekli pipeline test/gözlemlenebilirlik (boşluk); evals iş-ilanı ve araç ekosistemi büyümesi (AS-OF 2026-09-11, ikincil rakamlar `[?]`); Jarvis müfredatı P18-P19 boş. Masa: `raporlar/masa/masa-11-karar-yuzeyi-2026-09-11.html`.

**Yüzey:** ayri sohbet (Salih beyanı 09-11: "farklı bir chat üzerinde"). Açılış tetiği: **"seans başı, evals"** (yüzeyi Salih adlandırır; "günaydın" kalıbı yok — 09-09). O sohbet bu README'yi + `ilerleme.md`'yi okur, sıradaki haftayı işler, ders kaydını `dersler/`e yazar; jarvis kapsülüne yalniz öğrenme satırı dokunur (ogrenme/README protokolü adım 4).

## Sınırlar
- **md.49:** şirket/staj verisi kullanilmaz; tüm pratik kamu veri ve kamu görev setleriyle (aşağıda adlandırılmış). Staj bağlantısı yalnız "hangi beceri" düzeyinde kalır.
- **Karar 73 matematik kuralı:** her derste ≥1 formül: tanım + sembol tablosu + elle işletilmiş sayısal örnek.
- **Karar 68 anakronizm:** araç sürümleri/pazar iddiaları AS-OF damgalı; ders içinde canlı doğrulanır (araç docs).
- **Öğretim biçimi (hafıza kuralları 08-17/09-08/09-09):** benzetme değil doğrudan tanım + mekanizma + somut örnek; görsel metinden önce ve atıflı; kutu içi tek cümle açıklama; cevap başına az konu; yeni konuda önce terim tabanı yoklanır (deneme skill'i `ogren`: `PROBE` → `PLAN` → `TEACH` → `CLOSE`, K4 ilk canlı koşum bu seriyle yapılabilir).
- **Hazırı temel al:** promptfoo / DeepEval / Inspect AI'ın kendi kavramları ve şemaları öğrenilir; benzeri sıfırdan yazılmaz. Kendi kodu yalnız "mekanizmayı elle görmek" için, ≤50 satır.

## Müfredat — 7 hafta (her hafta 1-2 oturum, oturum 1,5-2,5 sa; done yazılı)
| H | Konu | Sektör başlığı (EN; AS-OF ≤2026-01 model hafızası, ders içinde doğrulanır — Salih 09-14) | Tek-satır `DONE` (Salih yapar) | Formül (Karar 73) | Kamu veri / araç |
|---|---|---|---|---|---|
| H1 | **Eval nedir, neden test≠eval:** görev · vaka · metrik · yargıç; 3 katman (uçtan-uca → trajektori → bileşen); regresyon seti fikri | *LLM Evaluation (Evals)* · *Test vs Eval* | 20 vakalık kendi eval seti YAML'da (girdi · beklenen · metrik), promptfoo ile 1 koşum | doğruluk / pass@k tanımı: pass@k = 1 − C(n−c,k)/C(n,k) elle n=5,c=2,k=1 | promptfoo (docs canlı) · vaka kaynağı: GSM8K alt-kümesi 20 soru |
| H2 | **Deterministik kontroller:** exact/contains/regex/JSON-şema · araç adı + parametre doğrulaması · maliyet-gecikme metrikleri | *Code-based / Deterministic Assertions* · *Rule-based Evals* | 20 vakaya 3 deterministik assert türü; ilk "kırmızı" vakayı bilerek üret | precision/recall/F1 tanımı + 2×2 tablo elle | promptfoo assert türleri · DeepEval `GEval` dışı metrikler |
| H3 | **LLM-as-judge I:** rubrik yazımı · konum/uzunluk yanlılığı · çift-değerlendirme | *LLM-as-a-Judge* · *Judge Bias (position/verbosity)* | 10 vakaya rubrikli yargıç; kendi elle puanınla karşılaştır | Cohen κ = (p_o − p_e)/(1 − p_e), elle 10 vaka | DeepEval G-Eval · MT-Bench rubrik örneği (kamu) |
| H4 | **LLM-as-judge II — kalibrasyon:** yargıcı insan-yargısına ayarlama · eşik seçimi · Brier | *Judge Calibration* · *Human-Agreement (Cohen κ)* | κ ≥ 0,6 eşiğine ulaşan rubrik v2; Brier hesaplı | Brier = (1/N)Σ(p_i − o_i)², elle N=10 | aynı set; Jarvis m.37 kalibrasyon bağı ("⌥ Jarvis notu") |
| H5 | **Trajektori değerlendirme (ajan):** araç-çağrısı sırası · ara adım · takılma/döngü tespiti · trace okuma | *Agent Trajectory Evaluation* · *Trace-based Scoring* | 5 ajan görevinde trajektori assert'i (doğru araç ∧ ≤N adım) | adım-verimi = doğru_adım / toplam_adım; döngü tespiti: tekrar eden (araç, argüman) n-gram | Inspect AI (UK AISI) `solver`/`scorer` + inspect_evals'tan 1 küçük görev (ör. `gsm8k` ya da `swe_bench` lite alt-kümesi) |
| H6 | **CI regresyon:** her PR'da eval koşumu · eşik/geçiş kuralı · üretim hatası → regresyon seti · flaky vaka | *Evals in CI* · *Regression Testing for LLM Apps* | GitHub Actions'ta promptfoo/Inspect koşumu, eşik altı = kırmızı | küçük-N: bootstrap %95 GA, elle 20 vaka×1000 örnekleme (script) | GitHub Actions (kendi kamu repo'n) · promptfoo `--ci` |
| H7 | **Kapanış — sentez + ürün turu (ogrenme/README adım 5, Salih 09-14):** ne zaman eval yeter (durdurma kuralı) · maliyet-kalite eğrisi · aday listesi → 3-model (biri "hiçbiri") → metrik önce → Salih hükmü → ana-sırada icra. Bugünkü adaylar (09-14, ana-sıra tespiti): (1) hakem rubrik-kalibrasyonu — atlas hakem raporuna boyutlu puan + Salih çift-puanlama, κ ölçümü (H3 mekanizması; bugün κ ölçümü yok) · (2) regresyon seti kurumsallaşması — `evals/regresyon-seti.yaml` deseni → `cc/eval/` deposu, besleme karantina + hakem DARALDI/DÜŞTÜ + Salih "beğenmedim" (H2/H6) · (3) skill koşumlarına promptfoo CI kapısı (H6) | *Evaluation Strategy* · *Eval-driven Development* | 1 sayfalık "doğrulama katmanı el kitabı" + ürün turu hükmü (masa) | güç analizi: n ≥ (z_{α/2}+z_β)² · p(1−p)/δ², elle δ=0,1 | — |

## Ders kaydı biçimi
`dersler/YYYY-MM-DD-HN-konu.md` — blok: tanım → mekanizma → elle örnek → kontrol sorusu; ≤3 kavram/blok; `## Salih notu` serbest alan (ogren skill'i "yap" notu). "⌥ Jarvis notu" = Jarvis-bağı, saf içerikten ayrı.

## Ölçüm (m.29 deneysel; kapanışta yoklanır)
- Hafta DONE'u yazılı çıktı ile (dosya/koşum adresi), beyanla değil.
- Seri sonunda: eval seti ≥50 vaka · κ ≥ 0,6 · CI yeşil/kırmızı en az 1'er örnek · el kitabı. Sapma tek cümle `ilerleme.md`'ye.
