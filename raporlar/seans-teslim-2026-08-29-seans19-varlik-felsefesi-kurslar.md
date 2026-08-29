# Seans Teslimi — 2026-08-29 · Seans-19 (varlık felsefesi + birebir kurslar)

*Kapanış dipnotu (Salih): paralelde canlı jarvis koşumları var — bu kapanış YALNIZ s19 şeridini kapatır; ortak türevlere ve paralel oturumların alanına dokunulmadı (H4 + Karar 71).*

## 1. Bugün gerçekten ne değişti
- **Karar 73 (Salih Katman-1):** Jarvis varlık felsefesi kanonlaştı — yeni dosya `core/varlik-felsefesi.md`: (1) Jarvis özünde MAKİNE (dayanak: MIT 6.006 L1, Ku dk 9:40–10:21 "algoritma = sabit boyutlu makine, girdi→çıktı fonksiyonu" — Salih'in t=535s işaretli transkripti `Clippings/`te commit'li; Salih beyanı: Karpathy'nin videodaki söylediğiyle aynı çerçeve) · (2) matematik-temelli öğrenme: her desen formülizasyonlu (tanım+sembol+elle örnek), her derste ≥1 matematik içerik (ogrenme/README protokol satırı; ileri dönük m.8) · (3) Jarvis = Salih'in ansiklopedisi (bulunabilirlik ölçüsü) · (4) birincil kaynak sicili.
- **BK-1:** MIT OCW 6.006 S20 tam aynası (81 MB) → `ogrenme/kaynaklar/mit-6006-s20/` (gitignore'lu, künye commit'li), BİRİNCİL kaynak.
- **Karar 73 EK:** BK-2 = MIT OCW 6.042J F10 (77 MB, aynı düzen) — 6.006'nın resmî ön-koşulu; zincir 6.042J → 6.006. `kuyruk/galeri-siralama/` = Salih dosyası, COMMIT'LENMEZ freni deftere yazıldı.
- **İki birebir kurs açıldı:** `ogrenme/mit-6006/` (video-önce ritim; sadakat sözleşmesi + 14-haftalık resmi takvim) · `ogrenme/mit-6042j/` (ders-kaydı-önce "0'dan anlatım" + **"NEDEN" görevi**: her iddianın gerekçesi kursun kendi ispatından, ispatsızlar işaretli+⌥-blokta tamamlanır).
- **İki Ders-1 kaydı teslim:** `ogrenme/mit-6006/dersler/2026-08-29-L01-algoritma-ve-hesaplama.md` (8 blok + 6 kontrol; n(n−1)/2 ve ölçek tablosu elle) · `ogrenme/mit-6042j/dersler/2026-08-29-L01-giris-ve-ispatlar.md` (Kısım A ders akışı + Kısım B bölüm kalanı; 41·41 çarpanlaması, implikasyon NEDEN'i, ∃∀→∀∃ ispat + x>y karşı-model, SAT/P-vs-NP; Leighton'ın "1 asal" sürç-ü lisanı kitabın tanımıyla işaretli).
- **Mat-felsefesi serisi tasarımı v1:** `ogrenme/mat-felsefesi/README.md` — 17 partisyon / 4 blok, her partisyonda zorunlu elle-matematik öğesi (Cantor/Gödel/Turing köşegen üçlüsü omurga), S1-S3 karşılaştırma-matrisi.
- Push'lar Salih beyanıyla atıldı (4745df9..319f2dd + 4ff2fd6). Açılışta silver tazelendi (o anki HEAD'e; sonrası paralel oturumların hattında).

## 2. Kararlar (kaynak + gerekçe + geri-açma)
- **Karar 73 + EK** — kaynak: Salih beyanları aynen defterde. m.16 taraması: çelişki YOK (determinizm ilkesi, Karar 65, hazırı-temel-al ile aynı hiza). Geri-açma: Salih Katman-1.
- Katman-2 alt-kararlar (geri alınması ucuz): 81/77 MB ikili kütle gitignore + künye-commit (baglam.sqlite emsali) · CLAUDE.md'ye pointer YAZILMADI (bütçe 7162/7168 B) · 6.042J'de ders-kaydı-önce ritim (Salih "0'dan anlattığın" emrinin okuma hali).

## 3. ADAY kalan (karar değil)
- Karpathy videosunun KENDİ künyesi (link+an) sicile eklenebilir — Salih verirse; mevcut dayanak Salih'in işaretlediği L1 pasajı.
- Mat-felsefesi serisi tasarım ONAYI + ilk oturum (önerim MF-P1) — Salih tetiği.

## 4. Sonraki ilk iş (bu şerit)
Salih iki Ders-1'i okur → **bulanık blok numaraları** (6006: blok 1-8 · 6042J: A1-A4/B1-B7) → telafi turu; sonra 6.006 L2 videosu (Salih izler) ∨ 6.042J L2 ders kaydı (Carvis yazar — Ch.2+Ch.3, Leighton'ın söz verdiği sahte-PowerPoint-ispatı açılışıyla).

## 5. Yeniden-açma koşulu
Kurs sadakat sözleşmeleri Salih beyanıyla revize edilir; "NEDEN" görevi kapsam değişikliği (örn. dış kaynak serbestisi) Katman-1.

## Hasat
- Özüt-1: OCW aynası → künye + gitignore + birebir-kurs deseni artık TEKRARLANABİLİR kalıp (iki kursta aynı çekirdek sözleşme; üçüncü kurs ucuz).
- Özüt-2: "Neden" görevi ile sadakat çelişmez — çözüm ayrıştırma: kursun ispatı gövdede, kursun vermediği gerekçe ⌥-blokta.
- Özüt-3: iki kurs kendiliğinden zincirlendi (6.042J = 6.006 ön-koşulu) — müfredat sırası Salih'e seçenek: önce 6.042J bitirmek matematikçi için hızlı tekrar, 6.006'ya taban.
- Wiki-delta: yok (kanon gövdesi `core/varlik-felsefesi.md`'de; wiki kuyruğuna ekleme gerekmedi).
- Verilebilir miydi: evet — görev sınıfı okuma+yazım; işçi-ajan 0, Workflow 0 (maliyet tahmini alt-model kuralı gereği yazılmadı).
- Seans hedefi (m.29 yoklaması, KL16-6): "Karar 73 paketi + kurs açılışı + Ders 1" → **TUTTU + fazlası** (ikinci kurs EK göreviyle geldi; sapma yok).
- Hasat kontrol listesi (6e): (1) karar adayları ingest'te ✓ (defter Karar 73+EK) · (2) açık pipeline/manifest yok ✓ · (3) ajan koşumu yok ✓ · (4) paralel devir: bu rapor + kapsül s19 satırı ✓.
- Araç-çıktısı notu (KB-50): `chap01.pdf` 19 sayfa inline okundu (ders üretimi için zorunlu birincil okuma; VTT ise dosyaya indirilip okundu — kurala uygun).

## Kapanış işletim notu (paralel-scoped)
Hareket kütüğü koşuldu (bronz'a s19 satırları); **ortak türev dosyalar (veri/*, graf/*, günlükler) COMMIT'LENMEDİ** — canlı paralel oturumların kapanışları üreticiyi yeniden koşup commit'ler (Karar 77 deseni: deterministik yeniden-türetim > merge). Bu commit yalnız: teslim raporu + kapsül s19 satırı.
