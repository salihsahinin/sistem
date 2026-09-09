# Seans Teslim — 2026-08-29 · galeri-scoring korelasyon şeridi (paralel, jarvis-dışı iş)

*Oturum aralığı: 2026-08-26 16:0x → 2026-08-29 (aynı oturum devam ettirildi). Yüzey: Claude Code masaüstü, Fable, ana-sıra dışı YAN ŞERİT (iş danışmanlığı, m.15 sınıfı). md.49: şirket verisi repoya girmedi — tüm iş çıktıları `~/Downloads/galeri-scoring-korelasyon/` (repo DIŞI); bu rapor yalnız yöntem + karar düzeyi.*

## Beş soru

- **Bugün gerçekten ne değişti:** Salih'in işyeri galeri-skorlama projesi için CatBoost öncesi feature-temizlik altyapısı kuruldu. (1) 290 kolonluk veri sözlüğü xlsx'i TAMAMEN okundu (3 sayfa; Salih emri "tamamını oku" → ~34k token parçalı okuma). (2) Sözlükten deterministik SQL üreten script yazıldı → 3 Redshift sorgusu: dealer matrisi (86 feature) · trim-dealer + A-yayını (182 feature) · rapor katmanı p_* (10 bileşen). Yöntem: ortalama-rank + Pearson = Spearman; NULL dolgusuz pairwise (n_cift raporlanır); is_eligible + son process_ts filtresi gömülü; sqlglot Redshift parse PASS. (3) Lokal pandas koşucusu yazılıp sentetik veriyle test edildi (bilinen r'ler birebir; pandas 3.0 str-dtype hatası yakalanıp düzeltildi). (4) Salih emriyle klasör sadeleştirildi: yalnız 3 SQL kaldı (üretici + lokal koşucu + talimat md silindi; içerik konuşmada, istenirse yeniden üretilir). (5) Ekip liderine copy-paste koşum talimatı verildi (sıra: dealer → p_rapor aşısı → trim-dealer; sağlama taşları: has_bought↔never_bought=−1 · p_butce↔p_karsilanabilirlik≈1 · dealer_purchase_budget↔a_purchase_budget=1). (6) Gizlilik sorusu cevaplandı: çıktılar yalnız (feature adı, n_cift, r) — satır-düzeyi veri sızmaz.
- **Hangi karar verildi (kaynak + gerekçe + geri-açma):** Jarvis-kanon kararı YOK (Katman-1 dokunuşu yok). İş-yöntem kararları (Salih onaylı akışta): rapor CSV'sinden değil tam aday havuzundan ölçüm (top-50 seçim yanlı — sözlüğün kendi uyarısı) · Spearman-via-rank (p_* zaten rank; ham katmanda çarpıklığa dayanıklılık) · koşumlar ekip liderine devredildi (Salih'in Redshift erişimi yok). Geri-açma: sözlük değişirse SQL yeniden üretilir (üretici script konuşma kaydında).
- **Hangi fikir ADAY kaldı (karar değil):** V88 fikir-kutusuna eklendi — "sözlükten-üretim deseni" (veri sözlüğü tek kaynak → analiz kodu türetilir; jarvis'e genelleme adayı) + yan dersler (pandas 3.0 str dtype · Redshift'te CORR() yok).
- **Sonraki ilk iş (bu şerit):** ekip liderinden 3 matris CSV'si gelince → küme analizi + CatBoost feature-eleme önerisi (Salih tetiği). Ana-sıra "sonraki ilk iş" kapsülde, bu şerit ona dokunmaz.
- **Yeniden-açma koşulu:** 3 CSV'nin gelmesi ∨ ekip liderinin sağlama-taşı hatası bildirmesi (has_bought↔never_bought ≠ −1 vb. → hat şüpheli, yeniden bakılır) ∨ sözlük revizyonu (p_fiyat CUME_DIST düzeltmesi sonrası matris yeniden koşulmalı — önce/sonra doğrulaması zaten amaç).

## Hasat (damga: beyansız — m.33)

1. **Özütler:** (a) Veri sözlüğü birim sütunu, korelasyona girecek kolon seçimini deterministik yapmaya yetiyor (adet/gün/TL/oran/yok + evet-hayır girer; kimlik/metin/tarih/koşu-sabiti girmez). (b) Yapısal r=1 çiftleri (aynı değerin iki adla yayını) koşum sağlama-taşı olarak kullanılabilir — hat doğrulaması bedavaya çıkar. (c) pandas 3.0: CSV metinleri `object` değil `str` dtype — `is_object_dtype ∨ is_string_dtype` kontrolü şart (tuzak, V88 içinde). (d) Redshift'te `CORR()` yok — AVG/STDDEV_POP açık formülü taşınabilir. (e) Agregat-çıktı çerçevesi ("dışarı yalnız ad+sayım+katsayı iner") veri-hassasiyeti sorularına hazır cevap.
2. **Wiki-delta:** yok (dersler V88'de; wiki kuyruğu zaten dolu, tempo kuralı).
3. **Verilebilir miydi (V20):** kısmen — SQL-üretici scriptin yazımı işçi-ajana verilebilirdi; verilmedi çünkü sözlük okuma + Salih'le ardışık kapsam kararları (tüm featurelar → erişimsiz koşum → ekip-lideri devri) tek bağlamda daha ucuzdu. Eksik yetenek değil, bağlam-devir maliyeti.
4. **Token×zaman etiketi (V28):** seçim: orta token × uzun zaman (3 güne yayılan tek oturum). Gerçekleşen (`v_baglam_seyri` be4a4b92): 96 tur · ilk bağlam 70.569 · max 279.082 · 74 tur >128K · çıktı 258.463 token. Beklenti: kısmen (kapsam iki kez büyüdü: 10 p_* → tüm sözlük → erişimsiz koşum planı).

## Ritüel koşum özetleri (6b-6e)

- hareket-tablo: PASS (bronz 3718 çağrı · silver 3368 · günlük `raporlar/hareket-gunlugu-2026-08-29.md`).
- skill-esik: 6 çift · yeni sapma 0 · son 24 saat 0.
- silver-sağlık kapısı: **çıkış 0** (T-Ç hata yok) · ADAY kuyruğu: SUPERSEDED 3 · YETİM 229 · KAPANDI 73 · ÖNELEME 6467 (500 yazıldı) — Salih triyajı, karar değil.
- kural-sayacı: 19/100 OK.
- **uzun-koşum: max bağlam 279.082 (74 tur 128K üstünde)** → hasat kontrol listesi (KB-52): (1) kalıcı aday ingest'e girdi ✓ (V88) · (2) açık pipeline yok; koşumlar SAHADA (ekip lideri) damgalı ✓ · (3) Workflow/ajan koşumu yok → KB-02 kaydı doğmadı ✓ · (4) paralel-oturum kaydı: bu rapor + aşağıdaki çakışma notu ✓.
- **araç-çıktısı aşımı:** sözlük dökümü ~34k token (sistem dosyaya persist etti; Salih'in açık "tamamını oku" emriyle parçalı tam okuma yapıldı — KB-50 istisnası beyan edildi).
- **boyut-tetiği:** fikir-kutusu 28,9→~31/20 KB (V88 eklemesiyle; damıtma zaten Salih masasında, kapsül 08-26 kaydı) · defter 62,9/48 · KILAVUZ 20,5/16 · pano 13,2/12 (dördü 08-26'dan devreden DAMITMA tetiği — değişiklik yok).

## Paralel-oturum çakışma kaydı (H4)

Kapanış sırasında ana/GBM şeridinin oturumu CANLI çıktı: benim ritüel koşumlarım sırasında `cf4c7c5` kapanış commit'ini attı (08-29 uplift şeridi); kütük dosyalarının (bronz/silver/gold) benim koşum çıktılarım o commit'e karıştı — kütükler append-only ortak altyapı, zarar yok. Bu şeridin commit'i pathspec ile yalnız kendi dosyalarına atıldı (`git add <yol>` H4 + vaka-5 SOP); diğer şeridin working-tree kalıntılarına (graf/*, son-50-prompt) dokunulmadı. `kuyruk/galeri-siralama/` untracked klasörü GBM şeridinin CatBoost pratik kodu — kendi .gitignore'u var, bilinçli untracked görünüyor; commit kararı o şeridin/Salih'in.
