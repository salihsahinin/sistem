# Seans Teslim — 2026-09-08/09 — Galeri şeridi: güncel extract, trim/galeri kümeleme, küme kolonlu model (jarvis-dışı repo)

*Yüzey: Claude Code masaüstü, Mac, ana-sıra, Fable 5.1. Hat: galeri şeridi (m.15/md.49; repo `~/Desktop/repo/data-company-vehicle-scoring`; çalışma dizini `kuyruk/galeri-siralama/veri3/` commit'lenmez, Karar 73 EK). Oturum 09-08 17:20 açıldı ("seans başı"), 09-09 akşam kapandı; bağlam max 610k, 457 tur 128k üstü.*

## Bugün gerçekten ne değişti
- **Güncel extract okundu:** `part_0000/0001_part_00` (09-08 12:17; 8,95 M satır, 33 ihale, 10.868 galeri × ihale trimleri tam çapraz ürün, 327 kolon) → DuckDB parquet (`veri3/guncel.parquet`). Eski 1.370'lik havuz güncel pozitiflerin %99,3'ünü taşıyor; tekrar satır 0; etiket 1 yok; ilk 3 ihalede etiket 2-3 eksik (eğitimden düşüldü).
- **Sızıntı denetimi:** eski gün-0 kalıbı kapanmış (days_since_last_bid_trim=0: %99 → %2; dealer çapası date_start−1). Şüphe: çift-oturum günlerinde sabah satırı akşamı %11-24 görüyor olabilir (extract dışı satış tipiyle ayırt edilemez, data ekibine soru). `signal_source` + 34 "kirli" kolon M0'da kaldı (dokümanın çıkarılanlar listesi); mutlak rakamlar bu yüzden şişkin olabilir, model kıyasları geçerli.
- **Trim kümeleme (Salih tasarım turu, 4 karar):** evren = ihale trimleri (506; katalog taraması iptal, arabam.com 1.936 düğüm indirilmiş kaldı, yalnız yakıt/vites boşluğu doldurmada kullanıldı) · 8 boyut (segment, kasa, hacim, yakıt, vites, ticari, fiyat dilimi 5, güç) · Ward k=15 · **"bilinmiyor" kategori değil: maskeli en-yakın-merkez atama** (yakıt+vites gizli → %70 aynı küme). Kartlar `veri3/trim_kume_v2_kartlar_k15.md`, merkezler `trim_kume_v2_merkez.json`.
- **Galeri kümeleme, üç deneme:** (a) ilan-profili → bölge kümeleri çıktı (marka payları her kümede aynı), küme×trim tutarlılığı 0,33; (b) ekip arkadaşının K-Means'i (6 boyut: yaş, hasar, devir, bütçe, HHI, aktiflik) → 5 boyutu extract kolonlarıyla r≈0,9 aynı bilgi, tek yeni parça hasar; etiketleri 3 Eyl itibarıyla → as-of değil; (c) **üç katmanlı as-of küme** (talep profili / ilan ölçeği / bölge) + shrinkage payı.
- **Model koşumları (CatBoost YetiRank, 200 iter, tam aday listesi, Recall@30, 3 fold 18/25 Ağu, 1 Eyl):** M4b (trim kümesi + galerinin araç-tipi payı + teklif sayısı) birleşik +0,9; sıcak×sıcak +1,7; sıcak×yeni trim +1,9 (2.524 pozitif, üç fold aynı yön). M6b (üç katman) birleşik −0,8; soğuk galeri×sıcak trim +2,7; 18 Ağu fold'unda sıcak −5,4 (kısa tarihçede gürültülü öncül). Özet `veri3/30_3fold_ozet.csv`, `35_3fold_ozet_m6b.csv`.
- **Üç sızıntı vakası yakalandı ve düzeltildi:** (1) galeri payları eğitim penceresinin tamamından → as-of (29→29b); (2) katman ataması pencere-bütünü → as-of (33→34); (3) ekip etiketi/boyutları 3 Eyl hesaplı → M5a/M5c sonuçları (genel +3,5) sızıntı şerhli. Ortak ders: her galeri özelliği ihale bazında as-of.
- **Yanlış teşhis kaydı:** fold-2 eğitimi "4 saat" göründü, swap sanılıp koşum durduruldu; PC uykudaymış (Salih).
- **Teslim (repo `analiz/`):** `guncel-extract-kumeleme-2026-09-08.md` (§0-7, bugünkü ek bulgular §8 olarak eklendi; commit Salih onayına).

## Hangi karar verildi (kaynak + gerekçe + geri-açma)
- **Trim evreni = ihale trimleri, katalog taraması yok (Salih 09-09).** Gerekçe: bağlam/iş yükü; katalog gelirse aynı 8-boyut vektörü + maskeli atama ile genişler.
- **Kümeleme ölçütü = soğuk başlangıç dış ölçüsü (Salih 09-09):** kümeler galeri–trim bilgisi yokken küme×küme ilişkisiyle tahmine hizmet eder; silhouette değil dilim Recall@30 seçer.
- **Yapı C mantığı (Salih):** küme = araç tipi; marka/seri kümenin içinde alt bölme.
- **Yalnız-sahibinden galerisi hedefe dahil (Salih):** küme numarasından skor yükselsin; bugünkü veriyle kararlı artı yok (tek kolon AUC ≤0,56; en iyi sinyal diğer satış tipi teklif sayacı 0,61 ve İç Anadolu).

## Hangi fikir aday kaldı (karar DEĞİL)
- Üç katmanlı galeri kümesi için öncül ağırlığı m=30 + öncülü yalnız yeterli olaylı kümelerde açmak (kısa tarihçe kararsızlığına karşı).
- Ekibin hasar skoru (ekspertiz panel) as-of kolon olarak; data ekibinden.
- Data ekibine: 12 aylık + tüm satış tipli as-of dealer kolonları (ekip verisi "soğuk" galerilerin %98'inin uzun geçmişi olduğunu gösterdi); çift-oturum kesim kuralı; ilk 3 ihale etiket 2-3; etiket 1 kaldırıldı mı; baseline 0,62 hangi havuzda.

## Sonraki ilk iş
1. m=30 öncül varyantı, 3 fold (~1 saat) → galeri kümesi kabul/ret.
2. Kabul edilen kolonlar (M4b üçlüsü) ve as-of sızıntı dersleri dokümana "B ailesi küme kademesi" olarak.
3. Keşif kanalı seçicisi: diğer-satış-tipi sayacı + ilan eşleşmesi; küme değil.

## Neyi yeniden açmak için hangi koşul gerekir
- Katalog geneli trim kümesi: data ekibi trim tablosu verirse (aynı script).
- Galeri ilan-profili kümesi: trim düzeyinde tüm ilan verisi gelirse (bugün 4.324 galerinin 1.500'ünde dolu).

## Hasat
**Özütler:** (1) Küme etiketi ranker'a ancak 305 kolonda olmayan bilgi taşıyorsa yardım eder; aktivite/bölge özetleri sıfır. (2) Küme×küme oranı tek başına sıralayamaz (aynı kümede aynı puan); galeri düzeyi puanla çarpılır ya da feature olur. (3) "Bilinmiyor" kümesi zararlı: modelde "asla teklif vermez" sinyaline dönüşür (M5b 0,006). (4) Pencere-bütününden hesaplanan her galeri özelliği eğitim satırının etiketini taşır; önem sırası 1'e fırlayan kolon = sızıntı imzası. (5) Aynı Recall@30, aynı model demek değil: fold 1 Eyl'de tahminler %74 örtüştü, pozitifler ilk 22'de sabit kaldı.
**Wiki-delta:** `hedef-sizintisi` sayfasına "as-of özellik" alt başlığı (üç vaka) → `wiki/README.md` kuyruğuna.
**Verilebilir miydi:** 35 script, ~12 CatBoost koşumu, 8 görsel, ekip xlsx analizi; işçi-ajan yok; arabam taraması (~2 saat) sonradan iptal edilen yol.
**Token×zaman:** oturum 75ecb346: 489 tur · ilk 71,9k · max 610k · 128k üstü 457 · çıktı 892k.

## Kapılar
- hareket kütüğü: 7909 çağrı (52 yeni) · silver 6855 · `raporlar/hareket/hareket-gunlugu-2026-09-09.md` · test PASS. Workflow koşumu yok.
- skill-eşik: 6 çift · SAPMA-YENİ 1: atlas-kosum × sonnet-5, agent ac56fcec 22.006 tok (medyan×2,3; başka oturum, 09-09 06:56).
- silver-sağlık: çıkış 0 · WARN 0 · YETİM aday 40 · KAPANDI 105 · T-A ön-eleme 7249/500.
- kural-sayacı 19/100 · bayat-çekim: kuyruk 0 · uzun-koşum: max bağlam 610k (457 tur üstte) — hasat kontrol: (1) kalıcı kural adayı yok (md.49; as-of dersi wiki kuyruğunda) · (2) açık pipeline yok · (3) ajan koşumu yok · (4) paralel oturum bugün çalıştı (Karar 88-91, Friday; 16:50 refresh) → `git add <yol>`.
- araç-çıktısı aşımı: `mcp__visualize__read_me` (81k → dosyaya düştü).
- test-kapısı: 121 test · FAIL 0 · skip 7.
- boyut-tetiği: kapsül 7,7/8 KB · fikir-kutusu 14,6/20 KB.
