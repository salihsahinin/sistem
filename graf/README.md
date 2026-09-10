# graf/ — Jarvis POINTER SİSTEMİNİN GRAFI (D2) · v0 · görselin okunuş rehberi

*Bu dizin Jarvis'in pointer (işaretçi/anahtar) sisteminin GRAF olarak görünümüdür. Graf elle çizilmemiştir: `tools/pointer-graf.py` her koşumda silver veritabanından (`veri/baglam.sqlite`) yeniden türetir; aynı silver → aynı `.d2` → aynı `.svg` (5 pano × 5 render bayt-birebir, kayıt `pointer-sistemi-v0-uretim.json`). Ham kaynak silver/bronz'dur; graf türetilmiş görünümdür (world-model §8). Üretim: 2026-08-22, d2 v0.8.1, yerleşim ELK. Salih teyidi: 08-22 18:2x ("d2 tamam").*

## Dosyalar (ne, neden)
| Dosya | Ne | Kim okur |
|---|---|---|
| `pointer-sistemi-v0-genel.d2 / .svg` | **Pano 0 — genel bakış** (9 kutu): sistemin tamamı tek ekranda | insan (ilk bakış) |
| `pointer-sistemi-v0-silver.d2 / .svg` | **Pano 1 — silver tabloları**: 10 tablo, PK/FK bağları | insan (şema) |
| `pointer-sistemi-v0-pointer.d2 / .svg` | **Pano 2 — pointer türleri → hedefler**: 11 referans türü nereye çözülür | insan (pointer mekaniği) |
| `pointer-sistemi-v0-ilke.d2 / .svg` | **Pano 3 — ilke → mekanizma**: m.20/21/22/8 + adresli erişim hangi tabloyu nasıl şekillendirir | insan (kanon bağı) |
| `pointer-sistemi-v0-kronoloji.d2 / .svg` | **Pano 4 — kuruluş kronolojisi**: 07-11 → 08-22, 8 adım | insan (tarihçe) |
| `pointer-sistemi-v0-tam.d2 / .svg` | tek-pano TAM graf (7089×4419 px — okunmaz, arşiv/diff amaçlı) | makine/arşiv |
| `pointer-sistemi-v0-kenarlar.txt` | aynı grafın **kenar listesi** (düğüm + kenar satırları) — LLM'e verilen biçim; D2 kaynağı LLM'e verilmez | LLM |
| `pointer-sistemi-v0-uretim.json` | üretim kaydı: d2 sürümü · motor · her SVG'nin sha256 · N-koşum determinizm sonucu | denetim |
| `../veri/graf/pointer-sistemi-model.json` | graf MODELİ (58 düğüm / 56 kenar, tipli) — D2'nin türetildiği ara ürün | makine |

Yeniden üretim: `python3 tools/pointer-graf.py --d2 graf/pointer-sistemi-v0-tam.d2 --d2-dizin graf/ --kenar-listesi graf/pointer-sistemi-v0-kenarlar.txt --render 5`

## Renk ve biçim sözlüğü (tüm panolarda aynı)
- **Yeşil kutu + kalın yeşil ok** = VERİ HATTI (lineage): bronz → silver → gold türetmesi. Ok üstündeki yazı = türeten araç.
- **Mavi kutu** = POINTER'LAR (referans tablosu ve türleri). **Turuncu kutu** = ANAHTAR KAYDI (pointer'ların çözüldüğü kayıt). **Gri kutu** = tablo/dosya sınıfı. **Bulut** = repo dışı hedef (url, git sha, zaman, etiket).
- **Pembe altıgen** = pointer İLKESİ (tüzük maddesi — kanon sabiti). **Sayfa-köşeli kutu** = kronoloji adımı.
- **Düz gri ok** = FK (yabancı anahtar: bir tablonun sütunu başka tablonun PK'sına işaret eder). **Kırmızı kesikli ok** = KIRIK pointer içeren bağ. **Turuncu kesikli ok / halka** = SÜPERSEDE (yeni kayıt eskisinin yerine geçer; eski silinmez — m.8; PROV-O adı `prov:wasRevisionOf`). **Pembe kesikli ok** = "ilke uygular" (kural → mekanizma).
- Kutulardaki sayı = silver'daki satır/kayıt sayısı o anki üretimde (ör. `kayit · 48.957 satır`).

## Pano 0 — genel bakış: nasıl okunur (yukarıdan aşağı)
1. **KURULUŞ KRONOLOJİSİ (en üst)** → pembe kesikli ok "07-11 imza → 08-22 graf" → **POINTER İLKESİ** altıgeni: `m.20 özet+adres · m.21 dönüş yolu · m.22 arşiv · m.8 süpersede · adresli erişim`. Okunuşu: önce kural kondu (07-11 tüzük), kural zamanla mekanizmaya döndü.
2. Altıgenden pembe kesikli ok "uygular: kayit_id = ADRES · pointer→hedef · arşiv · SCD-2" → **VERİ HATTI** kutusu. Yani ilke, silver'ın tasarımına gömülüdür: kaydın PK'sı bir ADRESTİR (`yol#satır#sha8`), pointer'lar hedefe çözülür, bayat kayıt arşive iner, süpersede SCD-2 ile tutulur.
3. **VERİ HATTI içinde:** `BRONZ · git-izlenen md/json/jsonl · 571 dosya` → kalın yeşil ok `tools/katman-hatti.py — sıfırdan, idempotent` → `SİLVER · veri/baglam.sqlite · 10 tablo · 134.770 satır · PK = ADRES` → yeşil ok `v_* görünümler` → `GOLD · veri/gorunum · 20 CSV görünüm`. Okunuşu: ham dosyalar her koşumda sıfırdan tabloya dönüşür; tablolardan görünümler türetilir.
4. **SİLVER'dan üç gri ok aşağı:** `referans.kayit_id → kayit (FK)` → **POINTER'LAR (referans tablosu) · 11 tür · 63.062 referans · 1.107 KIRIK** (mavi) · `kayit.dosya_id → dosya (FK)` → **DOSYALAR · 571 · katman: ılık 81 · sıcak 35 · soğuk 406 · yapısal 49** (gri) · `koşum/tahmin olguları` → **AMBAR olgu tabloları · 7 tablo · 854 satır**.
5. **POINTER'LAR'dan üç ok:** gri `m.N · V-n · K-NNN · [[wiki]] · skill · terim → çözümleme` → **ANAHTAR KAYDI · 6 tür · 328 anahtar · süpersede zinciri** (turuncu; kendi üstüne turuncu kesikli halka `replaced_by = prov:wasRevisionOf`) · mavi `url · sha · tarih · etiket` → **REPO DIŞI HEDEFLER** (bulut) · **kırmızı kesikli** `dosya_pointer → yol (6.964 çözümlü / 1.107 KIRIK)` → DOSYALAR. Okunuşu: bir pointer ya repo içindeki bir anahtara (tüzük maddesi, V-numarası, kart, wiki sayfası, skill, terim) ya bir dosyaya ya da repo dışına çözülür; dosya pointer'larının 1.107'si bugün kırık (hedef dosya yok/taşınmış) — onarım borcu görünür hâle geldi.

## Pano 1 — silver tabloları (PK/FK)
10 tablo `sql_table` biçiminde: `kayit · 48.957` (PK `kayit_id`; FK `dosya_id`) · `dosya · 571` (PK `dosya_id`) · `referans · 63.062` (FK `kayit_id`, `hedef_yol`) · `anahtar · 328` (PK `anahtar_id`; FK `replaced_by` → kendine) · `karar_borcu · 97` (PK `borc_id`) · `karar_borcu_kaynak · 246` (FK `borc_id`, `dosya_id`, `kayit_id`) · `json_kayit · 18.795` (FK `dosya_id`) · `hareket · 2.356` · `prompt · 357` · `uretim · 1`. Oklar satır düzeyinde bağlanır (ör. `referans.kayit_id → kayit.kayit_id`): bir referans satırı hangi bloğa ait; `karar_borcu_kaynak` bir karar kalemini dosya+satır+blok adresine bağlar (246/246 çözümlü). Turuncu kesikli `anahtar.replaced_by → anahtar.anahtar_id` = süpersede zinciri. Yalnız şema-düzeyi sütunlar gösterilir (okunurluk); tam sütun listesi model JSON'da.

## Pano 2 — pointer türleri → hedefler
Sol mavi kutu: 11 referans türü ve sayıları — `anahtar_terim 29.247 · dosya_pointer 8.071 (6.964 çözümlü / 1.107 KIRIK) · tuzuk_madde 7.669 · etiket 5.408 · url 3.476 · v_no 3.099 · kart 2.025 · tarih 1.819 · skill_adi 1.456 · sha 628 · wiki_link 164`. Sağda üç hedef: **ANAHTAR KAYDI** (tuzuk_madde 137 · v_no 82 · wiki_sayfa 43 · anahtar_terim 27 · kart 23 · skill 16; turuncu halka = süpersede), **dosya tablosu · 571**, **REPO DIŞI** (etiket · git · url · zaman). Her ok "X → Y" etiketini taşır (ör. `m.N → tüzük maddesi (anahtar kaydı)`). Kırmızı kesikli tek ok = dosya_pointer → dosya (kırık içeren). Okunuşu: pointer'ın TÜRÜ, NEREYE çözüleceğini belirler; çözümleme anahtar kaydında ya da dosya tablosunda yapılır.

## Pano 3 — ilke → mekanizma
5 altıgen: `m.20 pointer ilkesi` (özet + ADRES) · `m.21 dönüş yolu` (özet kısalır, pointer düşmez) · `m.22 arşiv pointer` (bayat kayıt arşive iner, pointer güncellenir) · `m.8 silme yasağı → süpersede` · `adresli-erişim kuralı (08-18)`. Pembe kesikli oklar hangi tabloyu şekillendirdiğini söyler: m.20 → `kayit` ("kayit_id = ADRES") ve `referans` ("pointer → hedef") · m.21 → `referans` ("dönüş yolu") · m.22 → `dosya` ("arşiv yolu güncellenir") · m.8 → `anahtar` ("replaced_by / gecerli_bitis, SCD-2") · adresli erişim → `kayit` ("SEARCH USING INDEX"). Her altıgenin tooltip'inde kaynak dosya vardır.

## Pano 4 — kuruluş kronolojisi (yukarıdan aşağı)
`2026-07-11 tüzük m.20-22 imzalandı` → `07-12 PAT kararı: yalnız pointer izlendi (kanonik örnek)` → `07-18 pointerlar-arası iletişim raporu: typed-link Model A ÖNERİ` → `07-24 graf-mühendisliği raporu: %92,5 graf-yetim; elle index bayatlar` → `08-15 silver katmanı (kayit_id adres PK)` → `08-17 hafıza mimarisi Beyan 9` → `08-18 adresli-erişim kuralı (Karar 62-64)` → `08-22 pointer sisteminin grafı (D2), Karar 65`. Her adımın tooltip'inde kaynak dosya.

## Neyi GÖSTERMEZ (bilinçli)
Tek tek 48.957 kayıt ya da 63.062 referans çizilmez (okunmaz; B-YT6: pano ≤20-50 düğüm) — örnek-düzeyi odak panoları G1 kademesinde (`--odak <kayit_id ∨ KB-n>`). Tipli bağlar (destekler/çürütür/genişletir) henüz yok — G2 Katman-1 kararı (KB-60). Graf kaynak değil görünümdür; değişiklik silver/kanon'da yapılır, graf yeniden türetilir.

*Pointer: plan `raporlar/2026-08-22-graf-dili-uzun-vade-plani.md` · rapor `cc/rapor-2026-08-22-2.md` · pipeline `cc/pipeline-2026-08-22-pointer-graf-d2.md`.*

## G1 ekleri (İB-48, 08-22 19:1x) — odak panoları + kırık-pointer panosu + testler
- **Odak panoları** `graf/odak/odak-<X>.d2/.svg`: `python3 tools/pointer-graf.py --odak KB-59` (karar kalemi: bağımlılık / buna bağımlı / kaynak kayıt+dosya / kaynak kayıtların pointer türleri) · `--odak <yol#satır#sha8>` (bir kayıt: dosyası, çıkan pointer'ları, onu kaynak gösteren KB'ler) · `--odak cc/rapor-2026-08-22-2.md` (bir dosya: ona pointer veren kaynak dosyalar · bloklarının pointer türleri · kırık sayısı · onu kaynak gösteren KB'ler). 1-2 sıçrama, sınıf başına ≤18 düğüm (`--ust`), toplam ≤50; sıralama sayım DESC + ad ASC (deterministik). Turuncu = karar kalemi, gri = kayıt/dosya, mavi = pointer türü, kırmızı kesikli = kırık içerir, pembe kesikli = bağımlılık.
- **Kırık-pointer panosu** `pointer-sistemi-v0-kirik.d2/.svg` (`--kirik`): en çok kırık pointer VEREN kaynak dosyalar (sol) → VAR OLMAYAN hedef yol/adlar (sağ, bulut); kenar = sayı. Üst kutu toplam: 1.137 kırık referans · 461 ayrı hedef · 920 ayrı kayıt (08-22 silver). Okunuşu: hedeflerin çoğu çıplak ad (`MEMORY.md`, `derle.py`, `config.json`, `env-vars.md`) — raporlarda geçen, repoda bulunmayan/silinmiş dosya adları; onarım = ya hedef arşiv adresine güncelleme (m.22) ya da "dış ad" olarak damgalama.
- **Testler** (`--test`, FAIL-LOUD çıkış 5): T1 model determinizmi · T2 her panoda kenar uçları tanımlı mı · T3 pano düğüm tavanı · T4 kenar uçları modelde · T5 render sha (`--render N≥2`). İlk koşumda T2 gerçek hata yakaladı (D2 anahtarında Türkçe harf) → `slug()` ASCII'ye çevrildi.
- Hat entegrasyonu (3. parça, katman-hatti adımı): ~~seans-14 devri~~ **EKLENDİ 08-26 seans-17 (İB-48 3/3):** `("graf", [... "--kirik","--render","2","--d2","graf/pointer-sistemi-v0-tam.d2","--kenar-listesi","graf/pointer-sistemi-v0-kenarlar.txt"])` — uyarı kanalı; panolar + LLM/makine METİN türevleri (tam.d2 · kenarlar.txt) her hat koşumunda tazelenir. **tam.svg render'ı hatta girmez** (dev arşiv panosu, insan okumaz — Salih 08-26: "o dosya llm için, bir şeyini değiştirme"; ihtiyaçta elle: `d2 --layout=elk graf/pointer-sistemi-v0-tam.d2 graf/pointer-sistemi-v0-tam.svg`, ölçülen süre 2,2 s).

## Obsidian harita türevleri (Karar 72 EK, 08-27 — Salih seçimi A)
- **Ne:** `graf/obsidian-harita.md` (indeks) + `obsidian-harita-<küme>.md` (13 küme) — silver `referans` tablosundaki çözülmüş dosya-pointer kenarlarının md-link listeleri. Amaç: 3.666 backtick pointer'ın Obsidian graf görünümüne girmesi; kanon gövdeleri değişmez (m.8). Kenarlar grafikte harita-notu ÜZERİNDEN görünür (hub deseni; doğrudan A→B çizgisi ileri-dönük md-link kuralıyla zamanla gelir — KILAVUZ Obsidian-uyum satırı).
- **Üretim:** `tools/obsidian-harita.py`, katman-hatti `obsidian-harita` adımı (graf sonrası); GITIGNORE'LU TÜREV — commit'lenmez, elle düzenlenmez, her koşumda yeniden doğar. İlk koşum: 2.812 kenar · 527 düğüm.
- **Kanonik ağ hâlâ D2 panelleridir** (Karar 67); Obsidian grafiği gezinme yüzeyidir, kaynak değildir.

> **Ad eşitliği (Karar 93, 2026-09-10):** bu dizindeki tarihli dosyalarda geçen **Carvis = Jarvis** (Salih'le konuşan ajanın 09-10 öncesi adı); sistem/repo kastedilirken "depo"/"kanon". Halef-sözlük: `core/baglam-anahtar-kaydi.md` anahtar `carvis-rol-adi` → `jarvis-ajan-adi`.
