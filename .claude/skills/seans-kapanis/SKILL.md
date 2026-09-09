---
name: seans-kapanis
description: Carvis'in JARVIS seans-KAPANIŞ ritüelini koşar. Salih "seans bitimi" (standart tetik; jarvis klasörü oturumunda BU ritüel), "kapat", "bitiriyorum", "seansı kapat" dediğinde HER YÜZEYDE çalışır; bağlam-şişmesinde Carvis kendisi de önerir. Kapanış selamı zaman işareti / tek başına tetik DEĞİLDİR. Teslim raporu + hasat + ingest + kapsül + commit/push üretir; push'suz gün SAYILMAZ (m.9). KULLANILMAZ; açılışta ("seans başı" → seans-acilis), ara özette ("hizala"), JARVIS-dışı vedalaşmada, STAJ oturumlarında (ayrım klasörle; staj-kapanis jarvis kanonuna yazmaz).
---

# Seans bitimi — seans kapanışı (Carvis, v0.3-deneysel-m29 — ad: vardiya-kapanis → seans-kapanis + uyucam-sınıfı tetik emekliliği [Salih Katman-1 08-15]; v0.2: staj kapısı 08-12)

## 0. STAJ KAPISI (önce bu)
Oturum STAJ KLASÖRÜNDEN açıldıysa ∨ beyan AÇIKÇA staj bağlamındaysa → BU RİTÜEL KOŞULMAZ. **AYRIM KLASÖRLE yapılır (Salih 08-15): "seans bitimi" cümlesi tek başına staj işareti DEĞİLDİR — jarvis oturumunda jarvis kapanışıdır.** ZAMAN-KAYMASI FRENİ: kapanış sözünden gece/gündüz çıkarımı yapılmaz; zaman yalnız sistem kaynağından. Staj oturumu jarvis kanonuna YAZMAZ (md.49); kapanışı staj klasörünün kendi ritüeli (günlük toparlama + yerel checkpoint) yapar. Tek cümleyle beyan et, staj kapanışına geç.

Kapanış = hafıza yazımıdır: bir sonraki seans yalnız burada yazılanı devralır. Bayat kapsül boş kapsülden kötüdür (V4). Şablonların kaynağı `core/sablonlar/` — çelişkide şablon dosyası kazanır.

## 1. Yüzey + hat tespiti
- Kanon-yazım kanalı var mı? (PC: doğrudan · bulut: origin-klon + PAT ile commit/push; mount'ta git komutu YASAK — yazım klondan push'lanır, mount'u senkron scripti eşitler.)
- Kanal YOKSA: tam ritüel koşulamaz → kapanış notunu "HAM FİKİR / PC'de ingest edilecek" damgasıyla üret, Salih'e açıkça söyle: **bu gün m.9 gereği HENÜZ SAYILMADI**, ana seans devralınca sayılır.
- Hat: prototip mi PortRisk mi? Paralel-seans senkron kuralı: yalnız KENDİ şeridinin dosya/satırlarına dokun; iki oturum açıksa push öncesi pull zorunlu.

## 2. Teslim raporu (`core/sablonlar/seans-teslim.md` — beş soru)
`raporlar/seans/seans-teslim-YYYY-MM-DD-<hat/etiket>.md` dosyasına: bugün gerçekten ne değişti · hangi karar verildi (kaynak+gerekçe+geri-açma) · hangi fikir ADAY kaldı (karar değil) · sonraki ilk iş · yeniden-açma koşulu.
**"İlk plan = bitti değil" yoklaması (Karar 79 D3/KL16-6; kaynak `cc/rapor/2026-08/rapor-2026-08-01-16.md:301`):** kapanışta açılış planı/hedefi FİİLEN yoklanır — planın yazılmış olması bitmiş sayılmaz; sapma tek cümleyle kayda (m.29 seans-hedefi denemesiyle aynı aile).

## 3. Hasat (`core/sablonlar/hasat.md`)
Özütler (3-5, birer satır) · **wiki-delta**: güncellenecek/açılacak sayfa → `wiki/README.md` kuyruğuna (yazım sonraki oturumlara yayılır; mevcut sayfaya tuzak çıktıysa Gotchas'a DOĞRUDAN işle) · verilebilir miydi (V20, çift-yönlü kapasite verisi) · token×zaman etiketi (V28 hammaddesi). Damga yalnız gönüllü beyanla; beyansızlık düşürmez (m.33).

## 4. İngest turu (m.34 katmanlı: ham dışta, damıtılarak içe)
- **ŞEMA (08-14 AKTİF):** her kayıt `core/ingest-semasi.md` sözleşmesiyle işlenir — 5-alanlık zarf + kapalı tip + 4-soru triyajı (NOOP/UPDATE/GEÇERSİZ-KIL/ADD; silme yok, geçersiz-damgası); devir dosyası bütçesi ≈1-2k token; sınıflandırılamayan kayıt → `kuyruk/SINIFLANDIRILAMADI.md` (sessiz düşürme yasak); sayaçlar teslim raporuna (giren/NOOP/UPDATE/geçersiz/ADD/DLQ).
- Oturumda doğan kalıcı-aday fikirler → `fikir-kutusu.md` (fikir-kutusu-adayı formatı).
- Ölçek-eşiği üstü kararlar → `kuyruk/senaryo-defteri.md` (m.37 kaydı: modeller+seçim+gözlem alanı).
- Karara bağlanmamış bulgular → `kuyruk/build-tartisma-notlari.md`. Silme YOK — bayatlayan arşive iner (m.8).
- Model değişimi yaşandıysa: ingest kanona DEĞİL şerhli klasöre (`arsiv/chat-model-degisikligi/ingest-YYYY-MM-DD.md` — eski ad "model değişikliği ile…", parti 1 taşıması 09-09) — KILAVUZ protokolü.

## 5. Kapsül tazeleme (`core/durum-kapsulu.md`)
Üzerine yazılır, arşiv değildir. Yalnız kendi şeridinin satırları; güncelleme satırı + "şu an" + borçlar + "sonraki ilk iş". Bütçe: **≤8KB VE ≤40 satır** (kanon bütçesi; 08-22 İB-24'ten beri SessionStart hook kapsülü DEĞİL ≤2 KB brifi basar — kapsül açılışta ELLE okunur, bu yüzden "Sonraki ilk iş" ilk maddesi ve Güncelleme satırı brife girer: ikisini kısa ve kendini açıklar tut).

## 6. Boyut-izleme tek bakış (İMZALI kural 07-22)
Sıcak dosya bütçeleri: kapsül 8KB/40sat · pano 12KB · fikir-kutusu 20KB · senaryo-defteri 48KB · CLAUDE.md 7KB/80 satır (v2 bütçesi 08-17) · KILAVUZ 16KB. Aşım hata değil TETİK: teslim raporuna "boyut-tetiği: <dosya>" satırı düş; damıtma ilk boş seansta Salih-imzalı planla.

## 6b. Hareket kütüğü + workflow kopyası (okunabilirlik ilkesi, Salih Katman-1 08-17; CLAUDE.md §2)
`python3 tools/hareket-tablo.py` koş (bugünün `raporlar/hareket/hareket-gunlugu-YYYY-MM-DD.md` + bronz/silver/gold tazelenir; test PASS beklenir). Bu seansta Workflow koştuysa script kopyası `cc/workflow/YYYY-MM-DD-<ad>-<wf_id>.js` + README satırı (kaynak: oturum dizini `workflows/scripts/`). İkisi de commit'e girer; eksikse kapanış TAMAM sayılmaz.

## 6c. Skill eşik koşumu (Salih imzası 08-21, defter Karar 51)
`python3 tools/skill-esik.py` koş — `v_skill_kosum` verisinde n≥10 skill×model çiftlerinin medyan token/süre bandı; 2× üstü koşumlar SAPMA satırı olarak teslim raporuna. Ayrıca bu seansın ajan koşum hükümleri (done-yüklemi PASS/FAIL, DRFR'den) `veri/bronz/kosum-sonuc.jsonl`'e düşülür (ÖNERİ-damgalı alan, Karar 52). Otomatik kural değişikliği YOK.

## 6d. Silver-sağlık kapısı (Salih imzası 08-21, defter Karar 58 — KB-39/40/41 (a); icra İB-42 08-22)
`python3 tools/silver-saglik.py --kapi` koş (hareket-tablo'dan SONRA; ~1-2 sn). Çıkış 6 = T-Ç çelişki hatası (çift-güncel anahtar · aralık örtüşmesi · sıcak emekli-kalıntı · karar_borcu çift/kırık bağımlılık) → hat DURUR: kaynağı bronz'da düzelt (anahtar kaydı / ledger / sıcak dosya), yeniden koş; kapı geçmeden commit yok. Çıkış 0'da özet satırını teslim raporuna al: WARN sayısı (ılık kalıntı), kuyruk (YETİM/KAPANDI/SÜPERSEDE aday sayıları — `v_silver_kuyruk_ozet`) ve T-A çift sayısı; aday kuyruğu KARAR DEĞİL, Salih triyajı (silme yok, m.8). Kütük `veri/silver-saglik.jsonl` append-only.

## 6e. Uzun-koşum politikası + bağlam bütçesi (Salih imzası 08-21, defter Karar 61 — KB-50/52 (a); icra İB-46 08-22)
Kapanışta HASAT KONTROL LİSTESİ (uzun oturumun kaybolmaması için, 4 soru — her biri tek satır): (1) bu oturumda doğan kalıcı kural/karar ADAYI ingest'e girdi mi · (2) açık pipeline/manifest T beyanı aldı mı ya da SAHADA damgası kaldı mı · (3) Workflow/ajan koşumlarının tahmin↔gerçek kaydı (KB-02) ambara düştü mü · (4) paralel oturum varsa devir notu/çakışma kaydı var mı. **Araç-çıktısı kuralı (KB-50 a):** >~10k token tek araç çıktısı bağlama dökülmez — özet + pointer (dosyaya yaz, yolunu ver); bu seansta ihlal olduysa teslim raporuna "araç-çıktısı aşımı: <araç/yol>" satırı. **Kural-sayacı:** `python3 tools/kural-sayaci.py` (CLAUDE.md + bu seansta çağrılan skill'ler) — eşik 100 aşıldıysa teslim raporuna "kural-eşiği: N" + damıtma tetiği. **128K / bağlam seyri (KB-52 a; İB-22 08-22):** `python3 tools/baglam-seyir.py` (hat adımı `seyir`; hareket-tablo ile birlikte koşar) — bu oturumun `v_baglam_seyri` satırı (ilk-tur bağlamı = statik önek · max bağlam · 128K üstü tur · toplam çıktı) teslim raporunun token×zaman etiketine girer; max bağlam >128k ise "uzun-koşum: max bağlam N (M tur üstte)" satırı + hasat kontrol listesi zorunlu. Eşikler m.29 (ilk ölçüm 08-22: statik önek 50-76k, 128K üstü yaygın — kalibrasyon Salih masasında).

## 6f. Bayatlık kuyruğu N=3 yeniden-çekim (Salih imzası 08-26, defter Karar 69 EK — KB-68 (a); icra İB-52 08-29)
`python3 tools/bayat-cekim.py --liste` → D3 kuyruğunun (`v_bayat_aday`, eşik 90 gün) en yaşlı 3 dosyası + yeniden-çekilecek D1 iddiaları. Her hedef için CANLI çekim (M3: kanıt tarihi yazılır) → hüküm `--kaydet <dosya> --sonuc teyit|guncellendi|sonlandi [--kaynak-tarihi]` (bronz `cekim-olay.jsonl`; teyit dosyaya dokunmaz, damga silver'dan tazelenir; silme yok m.8). Sonra `--olcum` (kuyruk/hedef/bugün sayıları → `katman-olcum.jsonl`) ve teslim raporuna tek satır: "bayat-çekim: kuyruk K · çekilen M/3". Kuyruk boşsa "0 aday" yazılır, adım geçilir (uydurma yok). Hat (`katman-hatti`) bu adımdan SONRA koşar ki `kayit.cekim_tarihi` taze olsun.

## 6g. Birim-test kapısı (Karar 86 D6-1, Salih hükmü 2026-09-02)
`python3 -m unittest discover -s tools/testler -p 'test_*.py'` koş (~60 sn). FAIL/ERROR varsa kapanış DURUR: kök-neden `[ariza]` commit'iyle düzeltilir ya da teslim raporuna "test-kapısı: N FAIL — <neden>" satırı + İB açılır; yeşil olmadan push beyanı istenmez. Gerekçe: 08-30 kanon değişikliği (parquet varsayılanı) süiti sessizce kırdı, 3 kapanış fark etmedi (09-02 sağlık turu). Sonucu teslim raporuna tek satır: "test-kapısı: N test · FAIL 0 · skip K".

## 7. Commit + push (m.9 — proof-of-work)
Karar başına AYRI commit · İngilizce mesaj · [damıtma]/[icra] etiketi (V5, m.10). Başka jarvis oturumu canlıysa `git add -A` YASAK — `git add <yol>` (H4, Salih 08-17; `wiki/paralel-oturum-protokolu.md`). Push origin'e; bulut yüzeyde klondan. Push başarılıysa kapanış beyanı: **"gün sayıldı"** + insan-yüzü tek satır (m.18: ▸ Kapandı · Sonraki ilk iş · Açık borç). Push atılamadıysa bunu GİZLEME — gün sayılmadı de, nedenini yaz.

## Gotchas
- **Kapsül-şişirme:** kapanış heyecanıyla kapsüle tarih anlatma — tarihçe commit'lerde ve teslim raporlarında yaşar; kapsül yalnız "şu an + sıradaki".
- **Çift-şerit çiğneme:** diğer hattın kapsül satırına/teslim dosyasına dokunma (07-12 senkron kuralı).
- **Sessiz push arızası:** push hata verirse "commit attım" diye geçme; m.9 push ister, commit değil.
- **Övgü kapanışı:** "harika bir gündü" merci yok (m.7) — kapanış çıplak veridir.
- **Paylaşılan-jsonl merge tuzağı (BAKIM-KK 08-29 kanıtı: 2 başarısız oturum, 3-4'er merge denemesi — b2b05897 · aa05a9d1, dosya `veri/sozlesme/tarama-plan.jsonl` sınıfı; Salih imzası Karar 77):** kapanış commit'inden ÖNCE paylaşılan türev-jsonl'de `git status -- <dosya>` ile staged↔working-tree ayrımını TEK seferde teşhis et; çakışmada merge'i elle deneme — dosya TÜREV ise üreticisini yeniden koş (katman-hatti adımı) ve üretilen hâli commit'le (deterministik yeniden-türetim > merge tahmini; vaka-4 ailesi).
