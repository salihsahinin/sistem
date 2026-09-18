# Seans Teslim — 2026-09-08 — Galeri şeridi: kümeleme ders serisi + tasarım dokümanı incelemesi (jarvis-dışı repo)

*Yüzey: Claude Code masaüstü, Mac, ana-sıra, Fable 5.1. Hat: galeri şeridi (m.15/md.49; repo `~/Desktop/repo/data-company-vehicle-scoring`, `kuyruk/galeri-siralama/` commit'lenmez). Oturum 09-07 açıldı, 09-08 kapandı; seans-açılış ritüeli koşulmadı (Salih doğrudan konuya girdi), kapsül elle okundu.*

## Bugün gerçekten ne değişti
- **Üç plan üst üste iptal edildi (Salih):** (1) fiyat-bandı grain'i / hiyerarşik backoff önerisi → data-ekibi dokümanı yazıldı (`analiz/oneri-galeri-trim-cold-start-hiyerarsik-model.md`, duruyor, icra yok) · (2) iki vektör uzayı + ampirik-Bayes toplamsal model + kalibre birleştirme anlatımı → Salih "anlamadım", iptal · (3) **galeri kümeleme, seçenek A (küme etiketi = CatBoost feature)** → 7 derslik seri anlatıldı.
- **Kümeleme ders serisi (7 ders, hepsi gerçek `data.csv` 09-02 üzerinde, her derse mcp__visualize SVG):** vektör/z-skor/Öklid · Gower + kategorik baskınlık (a/b/c çözüm) · k-means adım adım (20 iterasyon merkez yolu) · hiyerarşik Ward + dendrogram + HDBSCAN (bu profilde çalışmadı) · dirsek/silhouette/bootstrap-ARI kararlılık (sıfırdan iki kez açıldı) · 50-boyutlu as-of galeri profili → Ward k=5, test-dönemi küme başına alım 0,05-0,30, eğitimde görülmemiş 104 galeri 2× alım · küme etiketinin CatBoost'a girişi (akış diyagramı).
- **Salih'in yüklediği `galeri_trim_tasarim.html` (2026-09-04, ekip lideri tasarım kararı, Redshift doğrulamalı) 12 derslik seriyle baştan anlatıldı:** problem/grain/etiket · hedef sızıntısı (gün-bazlı pencere, gün-0) · metrikler neden yanılttı (P@1 0,987 / AUC 0,99996 / GroupAUC 0,565) · zaman modeli (üç kesim kuralı, 3 saatlik epoch-UTC kayması) · sızıntısız baseline Recall@30 0,62 · talebin yapısı (trim %6, serie %17, make %16, segment %26, ilk-kez %28; 7-gün recency) · feature aileleri A-I (sönümlü affinity, hot-demand) · mimari (grup (ihale,trim), tek YetiRank + Logloss yan model) · rolling-origin + bootstrap + 7 kanarya · davet kanalları + segment kuralları · kümelemenin yeri (§7) · yol haritası + ekler.
- **Sızıntı bizim `data.csv` sürümünde doğrulandı:** etiket 2-4'te `days_since_last_bid_trim = 0` %99; etiket 4'te `days_since_last_purchase_trim = 0` %99; `signal_source` etiketle bire bir (4.835 pozitifin 4.802'si bid/both). Dokümanın 647k/29-ihale bulgusu 687k/27-ihale sürümünde aynen.
- **Hafta-günü Jaccard ölçümü (dokümanda yoktu):** 351 ihale çifti; 7 gün fark aynı gün 0,134 vs 6/8 gün farklı gün 0,105; 7-28 gün aynı gün 0,121 vs farklı 0,093. Zayıf, takvimle karışık (17/27 ihale Salı/Perşembe 10:00).
- **Teslim (repo `analiz/`):** `ek-bulgular-galeri-trim-tasarim-2026-09-08.md` — yalnız dokümanda olmayan 8 madde (§7 spesifikasyon boşluğu + ölçümler · §7 profili extract kolonlarından kurulursa sızıntılı · küme etiketi test-dönemi ayrışması + "görülmemiş galeri" seviyesi · soğuk-trim metriği ve trim-kümesi × galeri-kümesi affinity · Balanced yan model kalibrasyonu · davet listesi iki birleştirme kuralı · grupsuz AUC mekanizması · hafta-günü örtüşmesi). **Salih okuyacak, revize edilecek.**
- **Hafıza:** `feedback-gorsel-anlatim-atifli.md` (görsel önce, metin boyunca görsel parçalarına atıf, her derse görsel).

## Hangi karar verildi (kaynak + gerekçe + geri-açma)
- **Seçenek A: küme etiketi = feature, hedef değil (Salih 09-07).** Gerekçe: tek kolon, mevcut hat korunur, dört-dilim tabloyla ölçülür. Geri-açma: A soğuk-galeri diliminde kazanç vermezse B (küme = hedef) masaya.
- **Birincil kümeleme algoritması: hiyerarşik Ward + z-skor (Carvis önerisi, Salih itiraz etmedi).** Gerekçe: 1.375 galeri küçük, deterministik, ortalama-bağ ve HDBSCAN bu profilde ölçümle elendi. Geri-açma: profil 30+ boyuta çıkıp yoğunluk adaları oluşursa HDBSCAN yeniden.
- **Güncel `data.csv` bu oturumda okunmadı (Salih):** bağlam bütçesi; kümeleme+eğitim ayrı oturumda.
- **Yan oturum kapanış kuralı (Salih sorusu, Carvis cevabı):** "seans başı"sız soru-cevap oturumuna kapanış yazılmaz; taşınacak bir şey oluştuysa devir dosyası (m.41 GK-2), kapanış değil. Kanon değişikliği DEĞİL, mevcut kuralın uygulaması.

## Hangi fikir aday kaldı (karar DEĞİL)
- **Trim kümesi × galeri kümesi affinity:** dokümanın "araç kovası"nın veriden öğrenilmiş hâli; soğuk trim çözümü (fikir-kutusu V94).
- **Galeri × hafta-günü katılım feature'ı:** A ailesine düşük öncelikli aday; 3-4 puan çözünürlük altında kalırsa atılır (ek-bulgular madde 8).
- **İhale-bazlı as-of küme etiketi:** etiket eğitim boyunca sabit yerine her ihale için o güne kadarki profil (ders 7 açık nokta).
- Önceki oturumun fiyat-bandı/hiyerarşik-backoff dokümanı: iptal ama silinmedi; dokümanın §4.6 B ailesi aynı fikri "kademeli affinity" olarak zaten içeriyor.

## Sonraki ilk iş
1. Salih ek-bulgular dokümanını okur → revize.
2. **Ayrı oturum, güncel `data.csv`:** tekrar-satır kontrolü (%14,5 duplicate iddiası) · profil yalnız önceki-ihale etiketleri + `import_date < cutoff` ilanlarından (madde 2) · galeri + trim kümeleme (Ward, k dirsek+silhouette+ARI+dış) · `cluster_id` + "görülmemiş" seviyesi + `cluster_affinity` → CatBoost, rolling-origin, dört dilim.
3. Kapsül 0a'daki eski kalemler (features.py commit onayı · group_id çelişkisi) dokümanla büyük ölçüde yanıtlandı: group_id = (ihale, trim) dokümanın kararı; ETL market kolonları H ailesi olarak geri geliyor. Salih hükmüyle kapatılır.

## Neyi yeniden açmak için hangi koşul gerekir
- Seçenek B: soğuk-galeri diliminde A'nın GroupAUC/Recall kazancı çözünürlük altındaysa.
- Vektör-uzayı/FM kurgusu: veri 5-10× büyüyünce (doküman §5.1 aynı hükümde).
- Redshift'e bağlı doğrulamalar (kanarya 7'nin view/ilan damgaları, `status` sonradan değişimi): data ekibinden gelince.

## Hasat
**Özütler:**
1. Anlatım biçimi: Salih "5 karar" listesini anlamadı, terim tabanından başlayan seri anladı → yeni konuda önce vektör/uzaklık gibi temel terimler, her dersin sonunda kontrol sorusu, "kontrol sorularını sen cevapla" akışı işledi.
2. Görsel tek başına anlaşılmıyor: görsel ÖNCE, metin boyunca "A paneli / kutu 3 / kesikli çizgi" atıfları (hafızaya yazıldı).
3. Sızıntı kanıtı tek kolonla verilir: `P(f>0 | etiket≥2) − P(f>0 | etiket=0)`; bizim dosyada 1,0. Kanarya 1 bu farkı 0,5'e sınırlıyor.
4. Dokümandaki metrik uçurumu (0,99996 vs 0,565) iki ayrı hatanın toplamı: sızıntı + test etiket-şeması kayması; ikisi de "model iyi/kötü" demiyor.
5. Denetimli modelde kategorik feature ağırlığını etiket verir; Gower'daki kategorik baskınlık yalnız denetimsiz (kümeleme) sorunu — §7 uygulanırken geri gelir.

**Wiki-delta:** `hedef-sizintisi` (gün-0 pencere, kanarya formülü, metrik uçurumu; kaynak bu teslim + ek-bulgular) → `wiki/README.md` kuyruğuna. `korelasyon-kaliciligi` kuyrukta bekliyor (09-04).

**Verilebilir miydi:** 12+7 ders tek oturumda, 19 SVG; işçi-ajan koşumu yok. Ders başına ~1 hesap + 1 görsel + ~900 kelime metin; Salih'in "daha detaylı, daha sade, okuma fedakârlığı kabul" talebiyle uzunluk kasıtlı.

**Token×zaman:** `tools/baglam-seyir.py` satırı aşağıda (6e).

**"İlk plan = bitti değil" yoklaması:** açılış planı yoktu; oturum üç kez yön değiştirdi (Salih iptalleri), üçü de kayıtta. Kapsül 0a'nın 09-04 kalemleri (parity çıktısı · PairLogit denemesi · `16/17_yeni_trim`) bu seansta ELE ALINMADI; ikisi dokümanla anlamını yitirdi (yukarıda), `16/17_yeni_trim` hâlâ açık.

## Kapılar (6b-6g)
- hareket kütüğü: 7165 çağrı tarandı (77 yeni) · silver 6286 · `raporlar/hareket-gunlugu-2026-09-08.md`; testler PASS. Workflow koşumu yok.
- skill-eşik: 6 çift · yeni-pencere sapması 0 · ajan koşumu yok (kosum-sonuc.jsonl'e satır düşmedi).
- silver-sağlık: çıkış 0 · WARN 1 (YETİM aday 376 > eşik 351, Salih triyajı) · kuyruk: SÜPERSEDE 4 · KAPANDI 105 · T-A ön-eleme 7004/500.
- kural-sayacı: 19/100 OK. bayat-çekim: kuyruk 0 · çekilen 0/3. katman-hatti: PASS (WARN ajan araç çağrısı >54: 34, bilgi).
- **uzun-koşum: max bağlam 409k (153 tur 128k üstü)** · ilk-tur 73k · çıktı 444k (oturum f0312cc3, 09-04 açılış). Hasat kontrol listesi: (1) V94 + tartışma bloğu + wiki-delta ingest'e girdi · (2) açık pipeline yok · (3) ajan koşumu yok · (4) paralel oturum yok, git add <yol> ile commit.
- araç-çıktısı aşımı: `mcp__visualize__read_me` (81k karakter → dosyaya düştü, grep ile okundu; ihlal değil, ön-lem).
- test-kapısı: 102 test · FAIL 0 · skip 7.
- boyut-tetiği: `fikir-kutusu.md` 21,4/20 KB (09-04'ten beri aşımda; damıtma Salih planı) · kapsül 7.976 B / 26 satır · defter 45,9/48 · tartışma-notları 48 KB (bütçesiz, arşiv adayı).
