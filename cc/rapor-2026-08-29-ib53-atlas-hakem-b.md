# MASKELİ HAKEM RAPORU — IB-53 / Aile B (2B↔3B graf okunabilirliği)

## KÜNYE

| Alan | Değer |
|---|---|
| Rapor kodu | IB-53 / Aile B — Hakem (R3, maskeli) |
| Rol | Maskeli hakem; üretici koşumların devamı değil. İki rapor kimliğe değil İDDİA+KANIT içeriğine göre kıyaslandı |
| Tarih (AS-OF) | 2026-08-29 |
| Girdi 1 (tez) | `scratchpad/hakem-b/rapor-1.md` — 15 birincil deney, 28 iddia |
| Girdi 2 (antitez) | `scratchpad/hakem-b/rapor-2.md` — 14 iddiaya ¬T taraması; 6 ÇÜRÜDÜ / 5 DARALDI / 3 ÇÜRÜTEMEDİM beyanı |
| Bağımsız denetçi sondajı | R1: Ware&Franck katsayıları (1,6×/2,2×/3,0×), Yoghourdjian eşikleri (yoğun ≥50 / seyrek >100), tarama medyanı 49,5, Moscovich 27,2s→8,5s birebir DOĞRU. R2: Kwon 2016 (43,20s vs 75,77s) ve Schaffer 1996 birebir DOĞRU — ANCAK Kwon 2016'nın TÜM koşulları HMD (Oculus Rift DK2) içindedir, düz-ekran kolu YOKTUR. Huang/Pfister/Yang 2023'te düz-ekran 3B+fare kolu VARDIR |
| Yöntem | Web araması YAPILMADI; yalnız iki rapor + denetçi teyidi. Görünür çelişkiler önce KOŞUL EKSENİNDE (düz masaüstü ekran ↔ stereo/HMD/VR ↔ hareket/döndürme) ayrıştırıldı; ancak koşul ayrımıyla çözülemeyen kalemler ÇELİŞKİLİ sayıldı |
| Verdikt ölçeği | SAĞLAM (iki taramadan da sağ çıktı) · DARALDI (daraltılmış form AYNEN yazıldı — karar girdisi) · DÜŞTÜ · ÇELİŞKİLİ (uzlaşmaz) · KARARSIZ (mevcut erişimle hüküm verilemez) |

---

## KOŞUL-EKSENLİ VERDİKT TABLOSU

| # | Kalem | Görünür çelişki | Koşul-eksenli çözüm | Verdikt |
|---|---|---|---|---|
| K1 | ① Düz ekranda STATİK 3B ↔ 2B | R1: statik perspektif ≈ 2B (Ware&Franck) ↔ R2: Tavanti&Lind 2001 statik 3B üstün | Tavanti&Lind grafı değil HİYERARŞİYİ ölçer + yinelemesi (Cockburn&McKenzie 2004) farksız çıktı; graf alanında Huang 2023 R1'i DESTEKLER | **DARALDI** (graf görevlerinde sağlam) |
| K1' | ①-ek Düz ekranda DÖNDÜRMELİ 3B ↔ 2B | Ware&Franck Deney-2: yalnız-hareket hata %11,4 vs 2B %26 ↔ Huang 2023: 3B+fare ≈ 2B, üç görevde farksız | Aynı hücre (düz ekran + döndürme), iki farklı sonuç. Uzlaştırma adayları: Ware'in 2B kolu yapısal dezavantajlı (Z-silinmiş projeksiyon, 2B'ye özel yerleşim yok), görev/graf/donanım-kuşağı farkı — doğrulanamadı | **KARARSIZ** (kazanç kanıtlanmamış sayılır) |
| K2 | ② 3B süre-kazancı hangi koşulda | R1: "hiçbir çalışmada süre kazancı yok" ↔ R2: Kwon 2016 %43 hızlı, "ÇÜRÜDÜ" | KOŞUL FARKI: Kwon'un tüm kolları HMD içinde (denetçi teyidi) — düz-ekran iddiasına dokunmaz. Düz ekranda süre kazancı hâlâ sıfır | **DARALDI** (iki taraf da) |
| K3 | ③ Bellek/hatırlama görevlerinde yön | R1: Kotlarek'te 2B > 3B ↔ R2: Tavanti&Lind 3B > 2B, "ÇÜRÜDÜ" | ALAN FARKI: Kotlarek graf düğüm-konumu (masaüstü-2B vs VR-3B); Tavanti&Lind hiyerarşi + yineleme başarısız. Graf-içi tek ölçüm 2B lehine duruyor | **DARALDI** |
| K4a | ④ ~50/100 düğüm kırılma eşikleri | R1: yoğun ≥50 / seyrek >100 kırılır (denetçi teyitli) ↔ R2: Ghoniem'de 50 düğümde %93 doğru; Ware&Bobrow'da vurgusuz 32'de bile kırık, vurguyla 3200'de sağlam | Eşikler KOŞUL-ÖZGÜ ölçümdür (statik, etkileşimsiz, en-kısa-yol, small-world); evrensel sabit değildir — etkileşim eşiği iki yönde kaydırır | **DARALDI** |
| K4a' | ④-alt: Ghoniem 50-düğüm %93 ↔ Yoghourdjian ≥50 kırılması | Aynı nominal koşulda (statik düğüm-bağ, ~50 düğüm, yol görevi) zıt sonuç | Uzlaştırma adayları (Ghoniem'in yoğunluk tanımı d=√e/n farklı; görev formu farkı) mevcut erişimle DOĞRULANAMADI | **ÇELİŞKİLİ** — ~50 sabit tasarım eşiği olarak KULLANILAMAZ |
| K4b | ④ 585-düğüm tam-graf negatifi | R1: "bu ölçekte ölçüm yok" ↔ R2: bant iki yandan kuşatılmış | 500-600 bandında birebir deney yok; ama 258/332 (Okoe, tam metin), 320-333/1000 (Ware&Bobrow, Ware&Mitchell — abstract düzeyi), 900 (Okoe 2014, ikincil, >%50 hata) mevcut | **DARALDI** |
| K5a | ⑤ Odak-getirme (Bring&Go) kazancı | Çelişki yok; R2 sayıları doğruladı, kapsamı daralttı | Denetçi teyitli: 27,2s→8,5s (3,2×), yoğun grafta hata %25→%10; bağ-takipte 1,67× ve hata farkı anlamsız — kazanç görev-bağımlı | **SAĞLAM** (görev-sınırı notuyla) |
| K5b | ⑤ Bozunum-F+C / fisheye | R1: "kazanç yok ya da negatif" ↔ R2: Schaffer 1996 fisheye %37 hızlı (denetçi teyitli), Furnas 1986 lehine | TEKNİK+UYARAN FARKI: fisheye/hiyerarşik-ağ lehine 1 deney (confound bayraklı), rubber-sheet/ağaç aleyhine 1 deney (Nekrasovski); derleme "net kılavuz yok" der. R1'in mutlak negatifi düştü; sınıf-düzeyi hüküm verilemez | **DÜŞTÜ** (mutlak form) → sınıf hükmü: KARARSIZ |
| K5c | ⑤ Overview panelinin süre katkısı | R1: "katkı yok" ↔ R2: Beard&Walker 1990 lehine, "ÇÜRÜDÜ" | Karşı-kanıt zayıf-birincil (n=6, 1990, kelime ağacı, graf değil); graf/ağaç gezinme ölçümlerinde katkı yok bulgusu duruyor | **DARALDI** |
| K6 | ⑥ Not-grafı bağlamında deney yok | Çelişki yok; R2 5 bağımsız sorguyla ÇÜRÜTEMEDİ | Çift-taraflı arama negatifi; tek doğrulanmamış aday (Atlas 2025, dosya-sistemi) açık | **SAĞLAM** ("bu sorgularla bulunamadı" statüsünde) |

**Sayım: 2 SAĞLAM · 6 DARALDI · 1 DÜŞTÜ · 1 ÇELİŞKİLİ · 1 KARARSIZ.**

---

## DARALTILMIŞ FORMLAR (AYNEN — karar girdisi)

**K1:** Düz masaüstü ekranda, GRAF görevlerinde, statik-perspektif 3B'nin 2B'ye karşı ölçülmüş kazancı yoktur (Ware&Franck 1996: iki 2B koşulu — ortografik ve statik perspektif — birbirinden ayrışmaz; Huang/Pfister/Yang 2023: 2B+fare ↔ 3B+fare üç görevde de süre ve doğrulukta farksız). Bu hüküm graf-dışı hiyerarşik uzamsal-bellek görevine genellenemez (Tavanti&Lind 2001 statik 3B lehine; yinelemesi Cockburn&McKenzie 2004 farksız).

**K2:** 3B'nin ölçülmüş süre kazancı yalnız TÜM koşulların HMD içinde gösterildiği kıyasta vardır (Kwon 2016: 3B-düzen 43,20s vs 2B-düzen 75,77s; her iki kol da Oculus Rift DK2 içinde — denetçi teyidi, düz-ekran kolu yok). Düz masaüstü ekranda 3B'ye ait ölçülmüş süre kazancı hiçbir çalışmada yoktur: süre ya farksızdır (Huang 2023) ya 2B lehinedir (Greffard 2011 — abstract düzeyi; Kotlarek 2020'de masaüstü-2B, VR-3B'den her üç görevde hızlı).

**K3:** Graf düğüm-konumu bellek/hatırlama görevinde eldeki tek doğrudan ölçüm 2B lehinedir (Kotlarek 2020: doğruluk 0,951 vs 0,923, p=8,88·10⁻⁵; süre 31,92s vs 50,70s) — ancak kıyas masaüstü-2B ↔ VR-3B'dir ve tek çalışmadır; graf-dışı uzamsal-bellek bulgularına genellenemez.

**K4a:** Yoghourdjian 2020 eşikleri (yoğunluk 6'da ≥50 düğüm, yoğunluk 2'de >100 düğümde en-kısa-yol başarısı %50'nin altına düşer — denetçi teyitli) YALNIZ statik, etkileşimsiz, vurgusuz düğüm-bağ + en-kısa-yol görevi koşulunda geçerli ölçümlerdir; evrensel okunabilirlik sabiti değildir. Etkileşimli vurgulama eşiği iki yönde kaydırır (Ware&Bobrow 2005, abstract düzeyi: vurgusuz 32 düğümde bile yüksek hata; vurguyla 3200 düğümde hızlı-doğru sorgu).

**K4b:** Tam olarak 500-600 düğüm bandında tam-graf topoloji deneyi yoktur; ama bant iki yandan kuşatılmıştır (Okoe 2019: 258/332 düğüm, tam metin; Ware&Bobrow 320/1000 ve Ware&Mitchell 333/1000, abstract düzeyi; Okoe 2014: 900 düğümde >%50 hata, ikincil aktarım). "Bu ölçek hiç ölçülmemiştir" formu düşmüştür; "tam bu bantta birincil deney yok" formu ayakta.

**K5a (kapsam notu):** 1-sıçrama komşuluk görevinde odak-getirme (Bring&Go), pan&zoom'a karşı 27,2s→8,5s (3,2×) ve yoğun grafta hata %25→%10 kazandırır (1000 düğüm, n=12 — denetçi teyitli); kazanç görev-bağımlıdır — bağ-takip görevinde 1,67× ve hata farkı anlamsızdır; genel navigasyona genellenemez.

**K5c:** Overview panelinin görev süresine katkısı graf/ağaç gezinme ölçümlerinde bulunamamıştır (Nekrasovski 2006: F(1,36)=0,611, p>0,4; Hornbæk 2002 aktarımı) ve kullanıcı algısıyla ayrışır; mutlak "hiçbir bağlamda katkısı yoktur" formu düşmüştür (Beard&Walker 1990: n=6, kelime-ağacı, harita-penceresi lehine p<.005 — zayıf ama birincil karşı-örnek).

---

## HAYATTA KALAN ÇEKİRDEK (Jarvis masaüstü 2B/3B kararı için doğrudan kullanılabilir)

1. **Düz masaüstü ekranda 3B'nin 2B'ye ölçülmüş bir üstünlüğü gösterilememiştir:** statik 3B için kesin (iki bağımsız çalışma uyumlu), fare-döndürmeli 3B için kanıt bölünmüş ve en yeni ölçümde farksız; süre boyutunda hiçbir düz-ekran çalışmasında 3B kazancı yoktur. Jarvis'in masaüstü görüntüleme katmanı için 2B varsayılan seçimdir.
2. **3B'nin ölçülmüş tüm kazançları stereo/HMD/hareket-paralaks koşullarına aittir** (Ware&Franck stereo+kafa-izleme 3,0×; Kwon 2016 HMD-içi %43 süre; McGuffin VR-içi) ve bu koşullar Jarvis masaüstü kararına aktarılamaz — Kwon'un "3B daha hızlı" bulgusu dahi 2B'nin de HMD'de gösterildiği kıyastan gelir (denetçi teyidi).
3. **~585 düğümlük tam-graf statik görünümü ölçülmüş okunabilirlik aralığının dışındadır** ve en yakın ölçümler (yoğun ≥50 / seyrek >100 kırılması; 900 düğümde >%50 hata — ikincil) tam-graf "hairball"un topoloji görevlerinde kullanılamaz olduğuna işaret eder; >500 düğüm kullanan çalışmaların %83'ü zaten grafın parçasını çıkaran etkileşimi ölçer. Tam-graf açılış görünümüne yatırım kanıtla desteklenmez.
4. **Ölçülmüş en güçlü kazanç görüntüleme boyutunda değil ETKİLEŞİMDEDİR:** 1-sıçrama komşu-getirme 3,2× hız + hata yarıdan fazla azalma (denetçi teyitli); etkileşimli vurgulama 3200 düğüme kadar sorguları ayakta tutar (abstract düzeyi). Yatırım önceliği 3B değil, odak/komşuluk etkileşimidir.
5. **Bozunum-tabanlı fisheye/rubber-sheet ve overview paneli karar gerekçesi olarak KULLANILMAMALIDIR:** fisheye kanıtı teknik-ve-görev-bağımlı biçimde bölünmüştür (sınıf hükmü yok), overview'ün süre katkısı graf/ağaç ölçümlerinde bulunamamıştır (algılanan fayda ölçülen faydayla ayrışır).
6. **Not-grafı (Obsidian/Roam sınıfı) bağlamında kontrollü deney iki bağımsız taramada da bulunamadı;** yukarıdaki tüm çıkarımlar sentetik/bilimsel-sosyal ağlardan aktarımdır — karar bu aktarım belirsizliği damgasıyla alınmalıdır.

---

## DÜŞEN / DARALAN

**DÜŞEN mutlak formlar:**
1. R1: "3B'nin süre kazancı hiçbir kontrollü çalışmada ölçülmemiştir" → Kwon 2016 (HMD-içi, denetçi teyitli) karşısında düştü; yerine K2.
2. R1: "Modern (2015+) düz-ekran 3B↔2B kıyası yoktur" → Huang/Pfister/Yang 2023 karşısında düştü — sonucu R1'in ana tezini DESTEKLER (fark yok).
3. R1: "Bozunum-tabanlı F+C kazancı yok ya da negatif" → Schaffer 1996 (denetçi teyitli) + Furnas 1986 karşısında düştü; yerine K5b sınıf hükmü: KARARSIZ.
4. R1: "Overview'ün süreye ölçülmüş katkısı yoktur" (mutlak) → Beard&Walker 1990 (zayıf-birincil) karşısında düştü; yerine K5c.
5. R2: "İddia 2 ÇÜRÜDÜ" hükmünün MASAÜSTÜ kapsamına genellenmesi → düştü; Kwon'un düz-ekran kolu yoktur (denetçi teyidi), düz-ekran süre iddiası ayaktadır.
6. R2: "İddia 3 ÇÜRÜDÜ" hükmünün GRAF alanına taşınması → düştü; Tavanti&Lind graf değildir ve yinelemesi başarısızdır; graf-içi tek ölçüm (Kotlarek) 2B lehinedir.
7. R2: "İddia 5 ÇÜRÜDÜ (eşikler yanlış)" hükmünün Yoghourdjian SAYILARINA uzanması → düştü; sayılar denetçi-teyitlidir. Düşen şey eşiklerin evrensel-sabit okumasıdır (→ K4a); Ghoniem hücresi ÇELİŞKİLİ kalır.

**DARALAN formlar:** K1, K2, K3, K4a, K4b, K5a-kapsam, K5c — yukarıdaki "DARALTILMIŞ FORMLAR" bölümünde aynen; karar girdisi olarak yalnız o cümleler kullanılmalıdır.

**ÇELİŞKİLİ / KARARSIZ kalanlar:** Ghoniem-50-düğüm ↔ Yoghourdjian-eşiği (ÇELİŞKİLİ; ~50 sabit eşik olarak kullanılamaz) · düz-ekran döndürmeli-3B hücresi (KARARSIZ; kazanç kanıtlanmamış sayılır).

---

**Hakem raporu sonu — maskeli hakem B, AS-OF 2026-08-29.**
