# Dil Seçimi — Jarvis sistemi + "Jarvis gibi ürün" ekosistemi: hangi durumda hangi dil (Go · Rust · Python · TS · shell · CUE-sınıfı) — İNSAN-YÜZÜ TESLİM, 2026-08-26 (seans-16)

*Salih emri (00:0x, aynen): "jarvis bir sistem ve jarvis gibi ürünlerle bir ekosistem oluşturmak istiyorsam hangi durumlar için sistemde kodları hangi dilde (örneğin go, cue lang'de yazdığı gibi) yazmak en mantıklıdır bunu araştır atlasları koş pipeline kur, araştırma sonucu borçları karar masasına taşımak üzere borç olmayan değişiklikleri implement et."*
*Kaynak: `cc/rapor-2026-08-26-1.md` (m.40b çift-atlas, 3 aile × 12 işçi, wf_d8cf4f3a-1a8; §Sentez S1-S6) · emir `cc/gorev-2026-08-26-1.md` · manifest `cc/pipeline-2026-08-26-dil-secimi-ekosistem.md` · yerel ölçüm `veri/kod-envanter.jsonl`. Her rakam kaynaklı; D = birincil kaynak, K = teyide muhtaç; deneysel m.29.*

## 1. Tek cümle
**Tek "en mantıklı dil" yok; iş sınıfına göre 9 hücrelik bir matris var — ve 9 hücrenin 7'sinde cevap "olduğu gibi kal: Python-stdlib + bash (+ dayatma JS)".** Değişen iki şey: (a) yaslandığımız **sistem Python 3.9.6 ömrünü tamamlamış** (upstream EOL 2025-10-31) → sürüm pini kararı; (b) **ekosistem tetiği** (MCP sunucusu + dış makineye dağıtım) — Go/Rust/CUE ancak bu tetiklerde, ölçüm + kapı ile girer. CUE bugün girmez; eşiği tanımlı. Türkçe tanımlayıcı hiçbir dilde engel değil.

## 2. Matris — iş sınıfı → dil (kanıtla)
| İş sınıfı | Bugün Jarvis'te | Hüküm | Neden (kanıt) |
|---|---|---|---|
| Sıcak hook (PreToolUse/SessionStart) | bash 68 satır (+python) · 30,7 / 67,7 ms | **kal**; dil serbest | Claude Code hook sözleşmesi dil-bağımsız (D) · derlenmiş ikilinin tavan kazancı 14 ms/çağrı (yerel n=10) · yalnız EXEC-biçimli `command` hook deterministik |
| CLI araçları / veri hattı (`tools/*.py`) | 27 script · 7.484 satır · stdlib-only | **Python kal**; yorumlayıcıyı PİNLE | throughput kıyası literatürde yok → ölçülmeden değişmez · LLM en doğru yazdığı sınıf · **3.9.6 EOL (D)** |
| Ajan döngüsü / Workflow | JS 2.054 satır (dayatma) | Python ∨ TS | Agent SDK yalnız Py+TS (2026-08-26 doğrulandı, D) |
| MCP sunucusu = "Jarvis gibi ürün"ün arayüzü | yok | Tier-1: TS · Py · C# · **Go** · **Rust**; ilk sunucu Python | MCP resmî SDK 10 dil; Go v1.7.0, Rust rmcp v3.1.4 (D). 07-30'daki "Rust hiçbir sınıfta" **bu sınıfta daraldı** |
| Dağıtılabilir ikili (dış makine) | yok | **Go'nun tetiği burada** | gerekçe "küçük ikili" DEĞİL (ripgrep 1,8 MB ↔ gh 13,9 ↔ Codex 88; D) → "çalışma-zamanı kurdurmayan tek dosya + bit-bit tekrar-üretilebilir derleme" (Go 1.21+, D; Rust'ta belge yok) |
| Claude API istemcisi | yok | 7 SDK dili; Rust yok (D) | Jarvis Claude Code üzerinden çalışır → girmez |
| Konfig / şema / doğrulama | Python doğrulayıcı + JSON | **JSON Schema + Python yeter; CUE girmez (şimdilik)** | Jarvis yükünü CUE'nun geçtiği belgeli durum YOK (SAĞLAM) · CUE eşiği: çok-kaynaklı kısıt birleştirme · CUE Türkçe tanımlayıcı OK (D) ama 1.0-öncesi, Dagger bıraktı (D) |
| Politika (deny/allow) | bash regex/liste | **kal** (m.30 doğrulandı) | OPA/Cedar tek-kullanıcıda aşırı; Rego `http.send` yan-etkili |
| Kural/betik sandbox'ı (ufuk) | yok | Starlark ∨ Dhall | spec-düzeyi sonluluk/determinizm (D); Datalog ekseni taranmadı |

## 3. Üç yatay kural (öneri; kanon statüsü KB-64)
1. **Nadir-dil kapısı:** kodu LLM yazıyor → Python/TS/JSON dışı dilde üretim = istemde spec referansı + derleyici/vet/şema kapısı + parite testi. Ölçüm: nadir dilde pass@1 <%7, referansla +22..+46 puan (CangjieBench 2026-03, K); Multi-SWE-bench dil kırılımı Java 23,4 · Rust 15,9 · TS 11,6 · **Go 7,5** · JS 5,1 (2025-04; gösterge, D).
2. **İki-yol parite testi:** dil geçişinin kabulü = aynı girdide bayt-birebir aynı çıktı + N saat hatasız (Turborepo 72 saat, D). Geçiş tetiği: dış-makine dağıtımı ∨ yerel ölçülmüş sınır; tetik yoksa geçiş yok.
3. **Sürüm-pinli kanal:** derlenmiş ikili determinizm vermez, pin verir (DotSlash · Nix flake · npm pin · brew sha; D). `curl|sh`, `go install @latest` girmez. Envantere giren her araç için son release/commit/90-gün sayısı; >12 ay boşluk → sha-kilidi.

## 4. KARAR MASASINA taşınan borçlar (Katman-1, ÖNERİ damgalı; ledger `veri/karar-borcu.jsonl` KB-62..65)

**KB-62 · Python yorumlayıcı tabanı (3.9.6 EOL)**
- *Ne demek:* tüm `tools/*.py` macOS sistem Python'uyla koşuyor; upstream güvenlik yaması 2025-10-31'den beri yok; Apple geri-yaması bilinmiyor (D/?).
- *Seçenekler:* **(a) Homebrew `python@3.13` + shebang `#!/usr/bin/env python3` yolu** — ne yaparım: brew kurulumu, PATH doğrulaması, `kod-envanter.py`'ye sürüm kaydı; artı: Homebrew zaten kurulu (+0 yeni araç zinciri), stdlib-only projede kilitlenecek bağımlılık yok; eksi: brew yükseltmeleri sürüm atlatabilir (pin komutu gerekir) · (b) uv + `requires-python` + uv.lock — artı: en deterministik; eksi: +1 araç zinciri (m.42), stdlib projede kilit boş · (c) sistem Python'da kal — artı: 0 iş; eksi: yamasız yorumlayıcı riski.
- *Öneri:* **(a)** — gerekçe: hazırı temel al (Homebrew var), m.42 bedeli 0, determinizm `brew pin` ile.

**KB-63 · Ekosistem ilk ürün sınıfı + dili (E-4'ün dil boyutu)**
- *Ne demek:* "Jarvis gibi ürün" için ilk arayüzün ne olacağı ve hangi dilde yazılacağı.
- *Seçenekler:* **(a) Python MCP stdio sunucusu** (bugünkü tools'u araç olarak açar; dağıtım `uv tool`/pipx) — artı: SDK Tier-1, +0 zincir, LLM doğruluğu en yüksek, Salih okur; eksi: dış makinede Python ister · (b) Go tek-ikili — artı: çalışma-zamanı istemez, tekrar-üretilebilir derleme; eksi: +1 zincir, LLM Go doğruluğu en düşük ikinci → nadir-dil kapısı · (c) TS/npm — artı: Claude Code plugin yalnız npm/bun'ı otomatik kurar, node kurulu, Kun Chen axi kanalı; eksi: ikinci dil, Salih okumaz.
- *Öneri:* **(a) şimdi; (b) dış-makine tetiği (T1) çekilince parite testiyle.**

**KB-64 · Kural setinin kanon statüsü**
- *Seçenekler:* **(a) `wiki/dil-secimi.md` kural-kaynağı + KILAVUZ'a 1 satır pointer** — artı: yaşayan sayfa, süpersede zinciri; eksi: kanon değil · (b) tüzüğe madde · (c) kural yok, vaka-bazlı.
- *Öneri:* **(a)**.

**KB-65 · Hook biçimi (sigorta dosyası — Katman-1)**
- *Seçenekler:* (a) EXEC biçimi + tek-süreç Python (07-30 H4; ~15 ms; e) · **(b) olduğu gibi** · (c) yalnız EXEC biçimi.
- *Öneri:* **(b)** — 30,7 ms zaten düşük; fren dosyasına dokunma bedeli kazançtan büyük; hook sayısı/gecikme büyürse (a).

## 5. Bu seansta GÖMÜLEN borçsuz değişiklikler (Katman-2)
- `tools/kod-envanter.py` — dil × katman × dizin envanteri + stdlib-dışı import + araç-zinciri + başlangıç-gecikmesi (n=10 medyan); `--json` = axi çıktı deseni; bronz `veri/kod-envanter.jsonl` (62 olgu, append-only); kayıt `tools/SCRIPTLER.md` + `veri/README.md`.
- `wiki/dil-secimi.md` — kural seti (ÖNERİ) 6-blok + index + karşı-link turu.
- `cc/rapor-2026-08-26-1.md` (157 KB mekanik + sentez) · emir · manifest · workflow kopyası `cc/workflow/2026-08-26-dil-secimi-ekosistem-m40b-wf_d8cf4f3a.js` · bronz tahmin/koşum/halüsinasyon satırları · senaryo-defteri m.40b gözlemi · kapsül pointer.
- **Kurulmayan/yazılmayan:** yeni dil/araç zinciri (go/cue/uv) KURULMADI; hook DEĞİŞTİRİLMEDİ; kanon dosyalarına DOKUNULMADI (hepsi KB'de).

## 6. Koşum künyesi
12 işçi (tez/antitez Opus-medium · V26 Sonnet-low · hakem Fable-high) · 189 araç · 16,7 dk · alt-ajan usage 643.314 token · rapor tablosu çıktı-token Σ 46.874 (tahmin bandı 150-220k'nın ALTINDA — sayım yöntemi farkı: yapısal-çıktı aracı; sapma `kosum-sonuc`a not) · hayatta-kalma 8/22/0/0 · V26 45 denetim: 37 TUTUYOR / 4 TUTMUYOR / 4 ERİŞİLEMEDİ (A temiz; C tez tarafı ve B antitez tarafı K'ya düştü).

## 7. Kör noktalar (bir sonraki koşum adayları — karar değil)
Güncel-model (2026) dil-başına doğruluk kırılımı · Python↔Go↔Rust SQLite-ölçeği throughput · kişisel-ölçek sayısal geçiş eşiği · CUE/Go LLM-üretim ölçümü · Datalog/Alloy ile tüzük-lojiği · Claude Code marketplace dil dağılımı · Apple sistem-Python geri-yaması · Python paketleyici (PyApp/uv tool) ikili boyutu.
