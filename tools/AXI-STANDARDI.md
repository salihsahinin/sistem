# AXI STANDARDI v0 — makine-okur, ajan-ergonomik araç arayüzü (İB-58; Karar 76 E-4; deneysel m.29, 2026-08-29)

*Ne bu:* `tools/*.py` deterministik çekirdekleri (Kun-Chen anatomisi: kod çekirdek + ince SKILL.md tetik katmanı) işçi-ajan EMİRLERİNE ARAÇ olarak verilebilir hale getiren yazım standardı. Emsal: `*-axi` CLI'ları (chrome-devtools-axi, gh-axi, lavish-axi — SessionStart brifleri `bin/description/help[n]` biçimi). Dil kararı E-4'ten ayrıldı (KB-63: Python MCP stdio; Go otomatik değil). Bu dosya Katman-2 (tools/ belgesi); kanon satırı gerekirse KILAVUZ araç-sınırı satırına pointer (Salih).

## Kurallar (A1-A8)
| # | Kural | Neden | Uyum sinyali |
|---|---|---|---|
| A1 | **İki kanal:** `--json` ile stdout = TEK makine-okur JSON nesnesi (sabit alanlar: `arac`, `surum`, `git_head`, `cikis`, iş alanları); insan satırları + ilerleme **stderr**. `--json`süz çağrıda insan çıktısı stdout'ta kalır (geri uyum) | ajan `stdout`u parse eder, ilerleme gürültüsü şemayı bozmaz | `"--json"` bayrağı + `insan = sys.stderr if a.json else sys.stdout` deseni |
| A2 | **Çıkış kodu sözlüğü (repo geneli):** 0 tamam · 1 hata/ihlal (hat düşer) · 2 girdi/kullanım hatası · 3 ihlal-UYARI (sayılır, hat düşmez — anakronizm) · 4 opsiyonel bağımlılık yok → ATLANDI (parquet/duckdb) · 6 ritüel kapısı (silver-saglik --kapi) | katman-hatti `adim_durumu` bu sözlüğü okur; ajan kodu görünce ne yapacağını bilir | docstring "Çıkış:" satırı |
| A3 | **Sabit bayrak adları:** `--repo` · `--sessiz` · `--json` · `--kuru` (yan-etkisiz prova) · `--bugun/--snapshot` (determinizm için zaman enjeksiyonu) | bir kez öğrenilen arayüz her araçta aynı | argparse add_argument adları |
| A4 | **Determinizm + idempotens damgası:** aynı girdi → bit-eşit çıktı (sha testi); kütükler APPEND-ONLY + tekil anahtar (yeniden koşum çift satır üretmez); `git_head`/`kod_sha` çıktıya yazılır | Karar 65; yeniden-koşum güvenliği (İB-39 kardeş) | test dosyasında `test_determinizm` |
| A5 | **Docstring = yardım:** Türkçe modül docstring'i argparse description'ı besler; "Ne bu / Grain / Modlar / Kullanım / Çıkış / Kayıt" blokları; alan adları tanımlı (alan adı talimattır, ajan-metodolojisi §1) | ajan emrine `python3 tools/X.py --help` yeter | `SCRIPTLER.md` satırı ↔ docstring birebir |
| A6 | **Yan-etki beyanı:** docstring'de salt-okur / eklemeli (append) / yıkıcı (üzerine yazar) sınıfı + dokunduğu dosyalar; yıkıcı sınıf `--kuru` zorunlu | skill-tetikleme-semasi "yan-etki damgası kayıt alanıdır" | docstring "Yazar:" satırı |
| A7 | **FAIL-LOUD:** bilinmeyen argüman/adım adı, eksik girdi, bozuk DB → stderr HATA + kod 2; sessiz atlama yok; traceback yerine tek satır teşhis | m.39; katman-hatti `--atla` bilinmeyen ad = 2 | test: bozuk girdi → 2 |
| A8 | **Bağlam bütçesi:** insan/ajan çıktısı ≤~2k token özet + dosya pointer (tam liste dosyaya: `veri/gorunum/*.csv`, kütük jsonl) | KB-50 a Karar 61 (alt-ajan dönüşü ≤2k) | `--sessiz` özet satırı tek |

## Ürünleşme eşiği (Salih sorusu: "her script değil — hangi kullanım sıklığında?") — ÖNERİ, karar masada
- Aday = `tools/*.py` ∧ (bir ajan emrinde/skill'de araç olarak geçiyor ∨ hareket kütüğünde k_W ≥ 3 oturum — `tools/loop-dedektor.py` görev imzası `py:<ad>` ile ölçülür) → A1-A8 uyumu istenir; aksi halde yalnız A2/A5/A7 (asgari hijyen).
- Dağıtım (npm/brew) yalnız dış kullanıcı hedeflenirse (E-4 b); bugün git-içi.

## Uyum envanteri (AS-OF 2026-08-29, ölçüm: `grep '"--json"' tools/*.py`)
- `tools/*.py` toplam **43** · `--json` olan **8** (anakronizm-denetim.py,katman-hatti.py,kod-envanter.py,kural-sayaci.py,pointer-graf.py,silver-saglik.py,wiki-baglanti.py,yuzey-parmak-izi.py) · `--sessiz` olan **30**.
- **İlk aday katman-hatti (08-29 UYGULANDI):** `python3 tools/katman-hatti.py --json` → tek satır JSON (`arac, surum, git_head, cikis, sure_s, adim_n, ok_n, uyari_n, adimlar[{adim, durum, sure_s, kod, uyari, stderr_son}]`); insan satırları stderr'e. Geri uyum: `--json`süz çıktı değişmedi (test_tarama_plan 13/13).
- Sonraki adaylar (kullanım sıklığına göre): `anahtar-denetim.py` — **kanon↔kod uyuşmazlığı:** `core/baglam-anahtar-kaydi.md` §5 `--json / --anahtar / --goster` bayraklarını vaat ediyor, kodda argparse YOK (08-29 ölçümü; Katman-1 metni düzeltilmez, kod kanona çekilir) · `hareket-tablo.py` · `loop-dedektor.py` · `erisim-fts.py --sorgu` (ajan aracı olmaya en yakın: sorgu → JSON sonuç). `silver-saglik.py` zaten `--json` + kapı kodu 6.

## Süpersede / bağlar
- 08-26 "E-4 ertelendi" → yerini aldı: 08-29 Karar 76 E-4 (a) erteleme kalktı, İB-58. · Dil: KB-63 (Python MCP stdio ilk arayüz). · Kardeşler: `core/ajan-metodolojisi.md` §1 (alan adı talimattır) · `core/skill-tetikleme-semasi.md` (yan-etki damgası) · Karar 65 (determinizm) · KB-50 (bağlam bütçesi) · İB-39 (idempotens).
