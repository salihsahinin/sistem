# İB-69 Aile-1 (c) — İç emsaller: fiilen koşmuş matris/grid harness'leri

**Kapsam:** yalnız iç kaynak (Read/Grep/Bash-okuma), web yok. AS-OF 2026-08-31.

## 1. Emsal tablosu

| Emsal | Eksenler (kardinalite) | Hücre çıktı tipi | Kütük dosyası + satır şeması | Toplama yöntemi | Fiilen koştu mu |
|---|---|---|---|---|---|
| **İB-07 description-eval** | sorgu (20) × tekrar (3) × skill (14, altın-etiket olarak) — 3 boyutlu grid | etiket (`secilen_skill`: ad ∨ HİÇBİRİ) + boolean `isabet` | `veri/description-eval.jsonl` — alanlar: `kosum_id, ts, sorgu_id, tekrar, altin_etiket, secilen_skill, isabet, isci_model` (`cc/gorev-2026-08-30-ib07-description-eval.md:9-12`; kütük satırı `veri/description-eval.jsonl:1`) | LLM (işçi tek-alan döner) + deterministik karşılaştırma (harness `isabet` hesaplar; P/R script'le, dosya adı raporda `stats.py` — script kendisi repoda görülmedi, yalnız raporda anıldı: `raporlar/2026-08-30-ib07-description-eval.md` "script: `python3 stats.py`") | **KISMİ** — 45/60 satır; ajan-freni (`.claude/hooks/pretool-ajan-fren.sh`, sayaç 72) 60. çağrıya ulaşmadan kesti (`raporlar/2026-08-30-ib07-description-eval.md` Durum bloğu) |
| **İB-49 d2-mini-eval** | kol (a/b1/b2/c, 4) × işçi (N=5/kol) — düz grid, tek eksen tekrar (N) kol-başına | sayı (P/R/dogruluk) + etiket (derleme OK/HATA, tercih A/B) | `veri/d2-eval.jsonl` — alanlar (kol'a göre değişken şema): a-uretim → `ts, git_head, kol, kosum, dosya, derleme_kodu, derleme_hata, dugum_llm, dugum_model, kenar_llm, kenar_model, ortak, eksik, fazla, precision, recall, simetrik_fark, byte`; okuma/sql → `ts, git_head, kol, kosum, dosya, dogru, toplam, dogruluk, ayrinti`; hakem → `kol, a, b, tercih, hakem` (`tools/d2-eval.py:57-61` kaydet-uretim; `tools/d2-eval.py:96-98` kaydet-okuma) | **Deterministik** — LLM çağırmaz (harness stdlib+`d2` ikilisi + sqlite3); işçi çıktısı dosya olarak verilir, harness kıyaslar (`tools/d2-eval.py:1-4` docstring) | **TAM** — N=5×4 kol, "5/5 OK" vb. (`raporlar/2026-08-29-ib49-d2-mini-eval.md` §1 tablosu) |
| **İB-65/66 atlas beşlisi (aile×şerit matrisi)** | aile (A/B/C, m.40b tez) × şerit (antitez, V26, hakem) — sabit 5-6 rol matrisi, kaynak-sayısı değişken (İB-65: 10+ kaynak × 6 eksen E1-E6; İB-66: 12 araç × 5 kriter K1-K5 = 60 hücre) | etiket (D/K/X hakem hükmü; EVET/KISMİ/HAYIR/`[?]` kriter hücresi) | Kütük yok — rapor-gömülü tablo (`raporlar/2026-08-31-ib65-loop-pipeline-secim-atlas.md` §1, §1.3; `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md` §1); ham işçi raporları `cc/rapor-2026-08-31-ib65-{A,B,C,antitez,hakem}.md` / `cc/rapor-2026-08-31-ib66-{a1,a2,b,c,antitez,v26,hakem}.md` | **LLM** — tez (Sonnet) → CoVe-Factored antitez (Sonnet) → V26 kural-tabanlı örneklem → maskeli hakem (Opus); toplama insan-okur tablo, jsonl kütüğe İNMEDİ | **KISMİ her ikisi de** — İB-65: hakem+V26 tam koştu (9/9 dalga), 7. maskeli-hakem gerekmedi orada ama İB-66'da AÇILAMADI (ajan-freni sayaç 72/78); İB-66: 60 hücrenin 13'ü `[?]` kaldı, bağımsız hakem yerine lider-ajan kendi hükmünü verdi |

## 2. Alan adları — birebir dosya:satır referanslı

**`veri/description-eval.jsonl`** satır şeması (örnek satır 1, alan sırası): `kosum_id, ts, sorgu_id, tekrar, altin_etiket, secilen_skill, isabet, isci_model` — kaynak: `veri/description-eval.jsonl:1`. Emirde tanım: "kütüğe yazar (`veri/description-eval.jsonl`, append; koşum kimliği ts)" — `cc/gorev-2026-08-30-ib07-description-eval.md` madde 3.

**`tools/d2-eval.py`** kütük alanları (fonksiyon `kaydet`, `tools/d2-eval.py:49-54` genel zarf: `ts, git_head` + gövde):
- a-uretim gövdesi: `kol, kosum, dosya, derleme_kodu, derleme_hata, dugum_llm, dugum_model, kenar_llm, kenar_model, ortak, eksik, fazla, precision, recall, simetrik_fark, byte` — `tools/d2-eval.py:110-113`.
- okuma/sql gövdesi: `kol, kosum, dosya, dogru, toplam, dogruluk, ayrinti` — `tools/d2-eval.py:130-132`.
- hakem gövdesi (serbest): `kol, a, b, tercih, hakem` — kullanım örneği docstring `tools/d2-eval.py:16`.

**`tools/denetci-kalibrasyon.py`** kütük alanları (`veri/denetci-kalibrasyon.jsonl`, fonksiyon `--puanla`, `tools/denetci-kalibrasyon.py:74-78`): `ts, git_head, kosum, yakalama, hatali_n, yanlis_alarm, dogru_n, yakalama_orani, yanlis_alarm_orani, paketler` — `paketler` iç içe obje: `{paket_id: {etiket, hukum, ok, hata_sinifi}}`. Not: bu emsal İB-69 emrinde okunması istenen ama İB-69'un doğrudan konusu olan bir "matris" değil — 7 paket × 1 koşum (kolon değil satır ekseni: paket_id sabit 7, koşum tekrarlanabilir) — grid'i **koşum × paket** olarak genişletmeye uygun tasarım (her `--puanla` çağrısı 1 satır, 7 paketin hükmü satır içi gömülü).

## 3. Ortak harness iskeleti — önerilen ortak jsonl satır şeması

| alan | tip | zorunlu mu | kaynağı |
|---|---|---|---|
| `kosum_id` | string | evet | İB-07 (`kosum_id`) — İB-49/denetçi'de yok, `ts+kol+kosum` bileşimiyle örtük; ortak şemada AÇIKÇA istenmeli |
| `ts` | ISO8601 string | evet | üçünde de var (İB-07 `ts`; d2-eval `ts`; denetçi `ts`) |
| `git_head` | string (kısa sha) | evet | d2-eval + denetçi'de var (`tools/d2-eval.py:50`, `tools/denetci-kalibrasyon.py:76`); İB-07'de YOK — kaydın hangi koda ait olduğu yalnız raporun künye bloğunda (`raporlar/2026-08-30-ib07-description-eval.md` "HEAD `7509b65`"), satır düzeyinde eksik → önerilen düzeltme |
| `eksen_degerleri` | obje `{eksen_ad: deger}` | evet | genelleme — İB-07'de `sorgu_id, tekrar, altin_etiket` düz alanlar; d2-eval'de `kol, kosum, dosya`; ortak şemada tek obje altında toplanabilir ya da düz-alan bırakılıp yalnız eksen ADLARI manifestte tanımlanır (İB-66 matrisindeki gibi K1-K5 × araç) |
| `tekrar` | int | hayır (varsa) | yalnız İB-07'de var (3 tekrar); d2-eval'de N=5 işçi ayrı satır olarak zaten tekrar yerine geçiyor (örtük) |
| `sonuc` | obje (skorlar/etiket) | evet | İB-07 `secilen_skill+isabet`; d2-eval `precision/recall/dogruluk/derleme_kodu`; denetçi `yakalama/yanlis_alarm/...` — üçü de farklı iç şema, ortak şemada `sonuc: {tip, deger}` genellemesi gerekir |
| `model` | string | evet | İB-07 `isci_model`; d2-eval/denetçi'de YOK satır düzeyinde (yalnız rapor metninde "Sonnet, effort düşük") — eksik, ortak şemaya zorunlu eklenmeli |
| `toplama_yontemi` | enum {"llm","deterministik"} | evet | hiçbirinde satır alanı yok, yalnız docstring/rapor düzeyinde beyan ediliyor (`tools/d2-eval.py:1` "LLM çağırmaz") — ortak şemaya eklenmesi önerilir (harness kendini belgeler) |
| `kosum_durumu` | enum {"tam","kismi","planli"} | evet | manifest alanı `durum` üzerinden var (`veri/manifest/ib-07-description-eval.json:5` `"kismi-2026-08-31..."`) ama jsonl satırında YOK — İB-07'nin 45/60 kesintisi satır düzeyinde görünmüyor, yalnız harici raporda; ortak şemada satır başına `kosum_durumu` olması resume'u kolaylaştırır (bkz. §4) |

## 4. Kısmi-koşum dersi (İB-07, append-only + resume için şart alan)

İB-07'de 45/60 satır yazıldıktan sonra ajan-freni kesti (`raporlar/2026-08-30-ib07-description-eval.md` Durum bloğu: "45/60 satır"). Kütük zaten append-only olduğu için VERİ kaybı yok, ama **hangi (sorgu, tekrar) çiftlerinin eksik olduğunu bulmak için** ayrı bir hesap gerekti (rapor manuel "q06-q20 tekrar 3" diye çıkardı — kütükte bu doğrudan sorgulanabilir değildi çünkü eksen kombinasyonlarının TAM KÜMESİ (20×3=60) hiçbir yerde deklaratif olarak durmuyordu, yalnız emirde düz metin "20 sorgu × 3 tekrar × 14 skill" vardı).

**Somut cevap:** resume-edilebilirlik için şart alan = **eksen kombinasyonlarının tam kümesini tanımlayan bir manifest/plan dosyası** (örn. `veri/sozlesme/description-eval-sorgular.json` — emirde zaten öngörülmüş: "altın sorgu seti... dosyaya yazılır, deterministik yeniden-koşum için sabitlenir", `cc/gorev-2026-08-30-ib07-description-eval.md` madde "Girdi") + kütükte her satırın **birincil anahtarı** (`sorgu_id + tekrar`, ya da genelde `eksen_degerleri` birleşimi) olması, böylece "planlanan küme − kütükte mevcut anahtarlar = kalan iş" farkı BİR SORGUYLA çıkar. İB-07'de sorgu-seti dosyası vardı ama kütük satırında birincil-anahtar sorgusu için özel bir alan/script yoktu — devam işçisi elle 45 satırı okuyup q01-q05×tekrar3'ün var olduğunu çıkardı. Ortak şemada `kosum_id` + eksen alanları birlikte tekil anahtar oluşturmalı ve bir `--eksik` / `--resume` modu (d2-eval ve denetçi'de de yok) harness'e eklenmeli.

## 5. Ayak izi (PK-10) ve fren riski

**PK-10 tanımı** (`raporlar/2026-08-29-ib63-paralel-pipeline-atlas.md:50`): "iki loop ancak ayak izleri HER iterasyonda ayrıksa paralel; `iterasyon_ayak_izi:"buyuyen"` → her N iterasyonda kapı yeniden değerlendirir." `tools/paralel-kapi.py:113` bu kuralı `'SIRALI', 'PK-10 büyüyen iterasyon ayak-izi (v0: seri)'` olarak uyguluyor — yani ayak-izi "büyüyen" işaretli loop'lar VARSAYILAN SIRALI kabul edilir (v0 muhafazakâr).

**Matris koşumunda risk:** İB-69'un önerdiği matris-koşum (hücre × hücre fan-out) tam olarak İB-07'nin çarptığı duvarla aynı sınıf — **dosya çakışması değil, ajan-sayaç/tavan çakışması**: `.claude/hooks/pretool-ajan-fren.sh` (İB-54/Karar 39) TÜM oturumdaki Agent çağrılarını sayıyor, tek bir görev-emrine özel değil (İB-07 raporu: "sayaç bu oturumdaki TÜM Agent çağrılarını sayıyor... muhtemelen sayaç seans-genelinde kümülatif" — `raporlar/2026-08-30-ib07-description-eval.md`). Dosya-düzeyi çakışma (manifest `dislama_grubu`/`commit_kapsami`) İB-07 ve İB-69-a1 manifestlerinde AYRI (`veri/manifest/ib-07-description-eval.json` vs `veri/manifest/ib-69-a1.json`, `commit_kapsami` kesişmiyor) — asıl risk PK-9/ajan-tavanı sınıfında, PK-10 loop-ayak-izi sınıfında DEĞİL: İB-69-a1 kendisi "prototip İNŞASI/koşumu YASAK" diyerek (manifest `kapsam_beyani`) bu riski proaktif olarak dışlamış durumda.

## Özet (dönüş metni tekrarı için)

- **3 emsal:** İB-07 (3B grid, LLM+deterministik karışık, jsonl, KISMİ 45/60) · İB-49 (4 kol × N=5, tam deterministik harness+stdlib, jsonl, TAM koştu) · İB-65/66 (aile×şerit m.40b matrisi, rapor-gömülü tablo, kütüksüz, İB-66 KISMİ 13/60 hücre `[?]`).
- **Alan şemaları birebir çıkarıldı:** description-eval 8 alan (`veri/description-eval.jsonl:1`), d2-eval 2 farklı gövde şeması (`tools/d2-eval.py:110-113`, `:130-132`), denetçi-kalibrasyon tek gövde (`tools/denetci-kalibrasyon.py:74-78`).
- **Önerilen ortak şema:** `kosum_id, ts, git_head, eksen_degerleri, tekrar, sonuc, model, toplama_yontemi, kosum_durumu` — üçünden hiçbiri şu an `model` ve `toplama_yontemi`'ni satır düzeyinde taşımıyor; bunlar ortak şemaya EKLENMELİ.
- **Resume dersi:** eksen-kombinasyon planı ayrı dosyada sabitlenmeli + kütükte tekil-anahtar sorgusu (planlı küme − mevcut = eksik) desteklenmeli; İB-07'de bu elle yapıldı.
- **PK-10/ayak izi:** matris fan-out'unun asıl riski dosya çakışması değil, oturum-genelinde kümülatif ajan-sayaç tavanı (İB-54 hook) — İB-69-a1 manifest'i prototip koşumunu zaten yasaklayarak bunu proaktif dışlamış.
