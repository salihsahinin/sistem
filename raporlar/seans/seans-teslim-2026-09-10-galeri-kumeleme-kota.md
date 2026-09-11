# Seans Teslim — 2026-09-10 — Galeri şeridi: m=30 ret, galeri kümeleme v3 + Faz-1, kota taraması, ekip dokümanları (jarvis-dışı)

*Yüzey: Claude Code masaüstü, Mac, ana-sıra, Fable 5.1 (ajan adı Jarvis; Karar 93 bu seans sırasında paralel oturumda alındı). Hat: galeri şeridi (md.49; repo `~/Desktop/repo/data-company-vehicle-scoring`; iş dizini `kuyruk/galeri-siralama/veri3/` commit'lenmez). Oturum 09-10 09:46 açıldı ("seans başı"), 09-11 kapanış; kanona karar girmedi.*

## Bugün gerçekten ne değişti
- **m=30 varyantı (36-37):** üç fold; sıcak dilimde m=10'a göre +1,3/+1,6 ama M4b'nin 1,4-1,7 altında, fold yönü tutarsız → galeri kümesi (M6b) RET. M0/M4b sonuçları 34 ile birebir aynı (deterministik).
- **Trim kümesi v2 analizi görseli:** `raporlar/gorsel/gorsel-2026-09-10-trim-kume-v2-analiz.html` (8 bölüm: boru hattı, eksik özellik, k seçimi, 15 küme, dilim×fold, kolon önemi, küme×küme tablo gücü).
- **Galeri kümeleme v3 (40):** davranış vektörü 4 blok (B2B payları, ilan envanteri kümülatif as-of, ilan ölçeği, bölge+sayaç) + blok maskesi + bölge kümeleri (yalnız-bölge 5.947 galeri) + boyut kısıtı (büyük ≥50 / ince 5-20) + matris-çarpımlı maskeli atama. 27+7 küme, %88 kararlı. Salih kararları K0-A/K1-A/K2-A/K6-A; K4 veriyle "büyük".
- **Faz-1 küme sıralama modeli (41-42):** YetiRank, grup (ihale, trim kümesi), hedef hücre oranı → model = "küme genel oranı" (aktiflik); trim-özgü sıralama yok. **Teşhis (43):** gk ana etkisi %43-52, etkileşim ~%20 ama yarı-bölme Spearman 0,25-0,32. **Lift hedefi (46):** rastgeleden 0,01-0,03 üstte. **Hücre düşürme (47):** T=5'te tutarlılık 0,40, eşik 0,5 altı. **C seçeneği (50-51):** M7 küme aktifliği M4b altı; küme×ölçek soğuk kotası ≈ 0.
- **Kota taraması (52-54):** kural "en az k soğuk", k=0..20, üç fold; toplam k≤4 düz, k≥5 iniş; öneri **k=3** (soğuk +2,3 puan, toplam korunur). Görsel `raporlar/gorsel/gorsel-2026-09-10-kota-taramasi.html`. İlk taramadaki "sabit k" kuralı hatası düzeltildi (k=0 saf M4b'den kötüydü).
- **Dokümanlar (jarvis reposu, staj damgalı):** `raporlar/2026-09/galeri-siralama-kumeleme-denemeleri-2026-09-10.md` (7 negatif deneme tablosu + kota + nihai yöntem) · `raporlar/2026-09/galeri-siralama-ekip-yazisi-2026-09-10.md` (ekibe, terim açıklamalı) · `raporlar/gorsel/gorsel-2026-09-10-galeri-siralama-nihai-ekip.html` (baştan sona 10 görsel + sözlük) · `raporlar/gorsel/gorsel-2026-09-10-galeri-kume-v3-analiz.html`.
- **Dondurulmuş kopya:** `veri3/surum-v3-faz1-2026-09-10/` (26 dosya, README).
- Ortam notu: veri3 script'leri dış repo venv'iyle koşar (`~/Desktop/repo/data-company-vehicle-scoring/src/.venv/bin/python`); sistem python3'te duckdb yok (ilk koşum bu yüzden düştü).

## Hangi karar verildi (Salih; jarvis-dışı, masaya girmez)
- Galeri kümesi (üç katman / m=30 / v3 Faz-1 / lift / C) → modele GİRMEZ. Gerekçe: üç bağımsız ölçümde tercih sinyali tekrarlanmıyor; kök 33 ihale, galeri başına medyan 2 olay.
- Kota politikası uygulanacak; sayı eğriden → öneri 3 (4 üst sınır), Salih hükmü açık.
- Data ekibinden 12 aylık geçmiş isteği ALINMAYACAK.
- Doküman yalnız jarvis reposunda, staj damgalı (context karışmasın).
- Nihai yöntem harmanı: trim kümesi v2 + M4b üçlüsü + en az 3 soğuk kotası; her galeri özelliği as-of; ölçüm üç fold altı dilim.

## Hangi fikir aday kaldı (karar DEĞİL)
- Kaynak-kör galeri kümeleme (Yol 1) / kapasite kısıtlı atama (Yol 2): ölçülmedi, beklenti rastgele; veri büyürse.
- Canlı ölçüm: her ihale sonrası aynı Recall@30 + "kotayla giren soğuklardan kaçı teklif verdi" sayacı.
- Ekip yazısındaki "çift-oturum şüphesi data ekibine soruldu" şerhi teyit ister.

## Sonraki ilk iş (galeri şeridi)
1. Salih: kota sayısı hükmü (3 / 4) + ekip dokümanlarının gönderimi (sadece §5 şerh kontrolü).
2. Nihai yöntemi şirket reposunda uygulama: M4b eğitim + en_az kota kuralı üretim koduna (`src/`), `analiz/` dokümanına §9 (Salih onayıyla).
3. Wiki kuyruğu: "küme×etkileşim sinyali testi" (yarı-bölme tutarlılığı) genel ders.

## Neyi yeniden açmak için hangi koşul gerekir
- Galeri kümesi: 12 aylık dealer geçmişi (Salih: istek alınmayacak) ∨ ihale sayısı ~3× (≥100).
- Küme×trim tercihi: yarı-bölme tutarlılığı ≥ 0,5 (47 script'i ile ölçülür).

## Hasat
**Özütler:** (1) Küme kimliğini gören sıralayıcı düzgünleştirilmiş hücre tablosudur; girdi kısıtlamak sinyal yaratmaz, tekrarlanabilirlik verinin özelliğidir. (2) Modelleme öncesi ucuz test: yarı-bölme tutarlılığı (Spearman) + permütasyon; 10 dakika, model kurmadan konuyu kapatır. (3) "Tam k" kotası ile "en az k" kotası farklı politikadır; k=0 tanımı kıyas tabanını belirler, ilk tarama bu yüzden yanlıştı. (4) Soğuk galeriyi küme oranı değil modelin kendi 305 kolonu ayırıyor; küme bilgisi galeri düzeyi bilgiye ek değil. (5) Kümeleme başarısı ile modele katkı ayrı ölçülür: v3 kümeleme %88 kararlı ve yorumlanabilir, katkısı sıfır.
**Wiki-delta:** `wiki/README.md` kuyruğuna "etkilesim-sinyali-testi" satırı (yarı-bölme tutarlılığı + permütasyon tabanı; kaynak 43/47).
**Verilebilir miydi:** 19 script (36-54), ~15 CatBoost koşumu, 4 HTML görsel, 2 md doküman; işçi-ajan yok; 40'ın ilk sürümünde bellek çöküşü (yayın 1,3M×408×45) → matris çarpımı; ilk kota taraması kural hatası → ikinci tarama.
**Token×zaman (v_baglam_seyri, oturum 72eb3a58):** 218 tur · ilk 72,0k · max 428,1k · 128k üstü 171 · çıktı 527,6k · thinking 102,0k.

## Kapılar
- hareket kütüğü: 8319 çağrı (20 yeni) · silver 7162 · `raporlar/hareket/hareket-gunlugu-2026-09-11.md` · test PASS. Workflow koşumu yok.
- skill-eşik: 6 çift · yeni-pencere sapması 0.
- silver-sağlık: çıkış 0 · WARN 0 · YETİM aday 39 (eşik 351) · KAPANDI 105 · T-A ön-eleme 7476/500.
- bayat-çekim: kuyruk 0 · çekilen 0/3.
- test-kapısı: 121 test · FAIL 0 · skip 7.
- kural-sayacı 19/100.
- uzun-koşum: max bağlam 428k (171 tur üstte) — hasat kontrol: (1) kalıcı kural adayı yok (md.49; wiki satırı kuyrukta) · (2) açık pipeline yok · (3) ajan koşumu yok · (4) paralel oturum 09-10 sabah-öğle çalıştı ve kapandı (dd44cf4/b786059; kapsül FIFO ile GALERİ maddesi arşive inmişti) → `git add <yol>`, kapsüle yalnız GALERİ maddesi.
- araç-çıktısı aşımı: yok (büyük çıktılar dosyaya, tail/grep ile okundu).
- boyut-tetiği: defter 52,4/48 (önceki seanstan, bu seans dokunmadı) · CLAUDE.md 7,17/7 (önceki).
- Seans hedefi (m.29, sayaç 3/5): açılış hedefi "m=30 varyantı 3 fold → galeri kümesi kabul/ret" → TUTTU (ret); üstüne Salih yönlendirmesiyle v3 kümeleme + Faz-1 + kota + dokümanlar (hedef genişledi, sapma değil).
