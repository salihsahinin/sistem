# Seans Teslim — Araştırma Borçları Pipeline'ı (2026-08-21, paralel oturum s13)

*Salih emri: "sistemdeki araştırma borçlarını pipeline kur koş". Pipeline: `cc/pipeline-2026-08-21-arastirma-borclari.md` · Emir: `cc/gorev-2026-08-21-arastirma-borclari.md` · 7 scout raporu: `cc/rapor-2026-08-21-ab*.md`. Rejim [maliyet-öncelikli]; işçiler 6× Sonnet + 1× Haiku; H=7 halüsinasyon sözleşmesi, Kapı-Ö GEÇTİ. Bu oturum PARALEL: karar ALINMADI, ledger/kutu/defter/kapsül/pano'ya YAZILMADI — hükümler ve kayıt güncellemeleri §4 devir-notlarıyla ana oturuma/Salih'e.*

## 1. Durum bloğu (m.18)
- **Geçmiş:** açılışta sistem tarandı → 5 açık araştırma borcu envanterlendi (kutu 2 + ledger 2 + kayıtsız 1); UFUK üçlüsü, ölçüm-sınıfı işler (KB-17b, İB-10) ve BEKLET-tetikli KB-31 kapsam dışı bırakıldı (gerekçeler manifestte).
- **Şu an:** 7/7 scout raporu indi, tüm done-yüklemleri DRFR PASS; hakem sentezi (G-1) aşağıda; commit'ler atıldı; push YOK (m.9 Salih beyanı).
- **Sıradaki:** devir-notlarının ana oturumca işlenmesi (§4) + AB-1/AB-2 tasarım kararlarının Salih masasına gelmesi.

## 2. G-1 Sentez — borç başına hakem hükmü (maskeli hakemlik; hüküm ≠ karar, karar Salih'te)

### AB-1 skill-bakım sistemi (tez `ab1-tez` 9D+1K · antitez `ab1-antitez` 1D+6K+2X, 2 zayıflatıcı)
İki kol BAĞIMSIZ koşup AYNI noktaya yakınsadı: **saf takvimli bakım da, saf olay-tetikli bakım da tek başına eksik — dış pratik hibrit öneriyor** (sapma/koşum-tetikli birincil mekanizma + düşük-maliyetli takvim tabanı). Hayatta kalan somut parçalar:
- İB-07 description-eval planı Anthropic skill-creator `run_loop`'unun birebir karşılığı (20 sorgu · 3x · %60/40 split) — icat değil UYGULAMA işi; betik hazır [D].
- Mevcut mimari (v_skill_kosum + Karar 51 + m.43) dışarıda tanınan "baseline-karşı-güncel" deseni [D]; eksik tek katman: **takvimli canary alt-sınırı** (ör. "W penceresinde hiç koşum yoksa yine de 1 kontrol") — sessiz model güncellemesini olay-tetik yakalayamıyor [D-6/D-9].
- Emeklilik kriteri kanonda YOK; 4-aşamalı şablon (@deprecated → telemetri → tarihli uyarı → kaldırma) doğrudan devralınabilir [D].
- Eşik SAYILARIMIZIN (n≥10, N=5/W=90) literatür karşılığı yok — SoK taraması "açık problem" diyor [D]; sayılar kendi tasarım kararımız olarak savunulur, dış meşrulaştırma aranmaz.
- Antitezin MUTLAK biçimi ("periyodik gereksizdir") TUTMADI: kendi bulguları bile hibrite işaret ediyor; yön uyarısı geçerli — takvim katmanı eklenirse maliyet-fayda gerekçesi yazılmalı, "bakım tiyatrosu"na büyümemeli.
**Hüküm:** tasarım hammaddesi TAM, kanon-aday tasarım (hibrit bakım + emeklilik aşamaları) Salih masasına hazır. m.40b çift-kol koşulduğu için antitez borcu YOK.

### AB-2 idempotens sistematik entegrasyonu (İB-39; `ab2-idempotens` iç 7/7 D + dış 2D+3K)
- İç envanter 3 MEKANİK desen (id-dedup · tam-sil+yeniden-yükle · temp→rename+eşdeğerlik-kapısı) + 1 MUHAKEME-tabanlı (damıtma triyaj NOOP) buldu; **sistemin asıl boşluğu tek tek hatlar değil, TEK bir idempotens tanımı/testinin olmaması** (byte-özdeşlik standardı yalnız baglam-tablo.py'de, elle, tek-seferlik).
- Somut boşluklar G1-G5: gece-senkron uyarı dosyası FAIL'de sınırsız birikir/başarıda sıfırlanmaz · ambar-parquet metadata'sı byte-özdeşliği bozar · damıtma dedup'ı mekanik anahtar kontrolüne indirgenebilir (hash → LLM yalnız yeni/belirsizde) · ingest damgası dosya-düzeyinde (kayıt-düzeyi değil) · katman-hatti'de geçici/kalıcı hata ayrımı yok. Her birine eşleşen dış desen tabloda.
- 07-26'nın C7 boşluğu KAPANDI: IETF Idempotency-Key draft-07 bulundu ve okundu [D].
**Hüküm:** araştırma ayağı TAMAM; entegrasyon TASARIMI kanon-aday olacağı için **m.40b antitez borcu AÇIK KAYDEDİLDİ** (tek-şerit rapor kanonlaşmaz) — tasarım masaya gelmeden hedefli antitez turu gerekir.

### AB-3 usage-otomasyon yol seçimi (İB-08; `ab3-usage` 6D+1K+1X)
**m.40 araştırma-önce şartı KAPANDI.** Kıyas net: JSONL-parse SÜRDÜRÜLÜR (kurulu, zengin, KB-13(5)/KB-27 bağlı) ama kırılganlığı artık BELGELİ (format resmen "internal", 2.1.169 somut regresyon) → iki sertleştirme icra borcu olarak İB-08'de kalır: (1) parse script'lerine FAIL-LOUD şema freni, (2) `claude -p --output-format json` ile periyodik çapraz-doğrulama. OTLP resmî/sağlam ama collector bedeli tek-kullanıcıda kazanımı aşıyor (çoklu-oturum canlı izleme doğarsa aday); ccusage omurga olmaz (aynı JSONL'e bağımlı + üçüncü-parti yüzey), elle hızlı-sağlama aracı olarak serbest.

### AB-4 V59 token-verim okuyucu ön-katmanı (tez `ab4-tez` 5D · antitez `ab4-antitez` 4-6D+4K+1X)
07-22 adjudikasyonu (AUGMENT-only koşulu) + bugünün iki bağımsız kolu ÜÇÜNCÜ kez aynı sonuca yakınsadı — bulgu artık sağlam:
- **Kayıpsız format-temizleme ≠ özetleme:** ReaderLM-v2 sınıfı temizleyici ön-katman bilgi kaybı riski taşımaz, ingest için düşük-riskli aday [D].
- **Token-seviyesi sıkıştırma (LLMLingua sınıfı) bizim ölçekte gereksiz:** manşet 20×'e karşı uçtan-uca gerçek kazanç ~%18 [D]; m.20 yapısal pointer zaten "ne taşınacağını" seçiyor; yalnız gerçek pencere-aşımı dev-doküman işinde break-even hesaplı düşünülür.
- **Kademe eklemek koşulsuz kazanç DEĞİL:** sabit zincirler doğrudan yönlendirmenin altında kalıyor (SimpleQA: tam-zincir %1,3 vs router %26,7) [D]; zayıf ön-modelin yanlış kabul/red'i pahalı modele ek tur bindiriyor [D]; özet-katmanı "decontextualization" ile karar-çevirme oranını 2×+ artırabiliyor [D].
- **Sınır (antitezin kendi dürüstlük kaydı X1):** risk açık-uçlu/karmaşık okumada yoğun; yapılandırılmış/basit özetleme küçük modelde genelde sorunsuz. m.20'nin "özet+ADRES" biçimi (kaynağa dönüş yolu) bu riske kısmi zırh.
- Elle model-atama (kural-tabanlı, kosum_profili) survey taksonomisinde deterministik uca denk — mevcut ölçekte otomatik router yatırımı gerekçesiz [D].
**Hüküm:** V59 "kurulsun mu" kararı DEĞİL (Katman-1); bulgu seti: kurulacaksa yalnız kayıpsız-temizleyici ∨ özet+pointer-AUGMENT biçiminde, ablation+bilgi-koruma ölçümü şartıyla. Kutu satırı güncellemesi devirde.

### AB-5 cascade-failure kaynak doğrulama (`ab5-cascade` künye D)
Makale (arXiv 2605.17288) açıldı-okundu; künye ve ana iddia (kademeli LLM sistemleri hedefli düşmanca manipülasyona açık; performans + maliyet avantajı birlikte bozulabiliyor) Carvis çapraz-fetch'iyle de TEYİTLİ. 08-15 raporunun "girmez (bu hâliyle) — okunmalı" şartı karşılandı. **Hakem düzeltmesi:** ajan raporundaki "saldırı yüzeyini doğrusal olmayan biçimde artırır" ifadesi özette YOK → DAYANAKSIZ (rapor kullanılırken bu cümleye yaslanılmaz); geçerli hüküm: "kapı sayısı arttıkça saldırı yüzeyi artar" [K — yön destekli, nicel sınır verilmemiş]. Bedel-defteri kalemi devirde.

## 3. Tahmin ↔ gerçekleşen (KB-02; işleme ana-oturum/kapanış ritüeline devir)
| Rol | Tahmin (araç · süre) | Gerçek (araç · süre · toplam token) | Bant |
|---|---|---|---|
| S-1a | 15-30 · 4-8 dk | 18 · 4,5 dk · 68,3k | İÇİNDE |
| S-1b | 8-15 · 3-5 dk | 18 · 6,1 dk · 72,9k | **ÜSTÜNDE (araç+süre)** |
| S-2 | 20-35 · 5-10 dk | 18 · 5,3 dk · 98,3k | araç hafif ALTINDA, süre içinde |
| S-3 | 10-20 · 3-6 dk | 10 · 3,1 dk · 66,8k | İÇİNDE |
| S-4a | 15-30 · 5-9 dk | 15 · 5,9 dk · 75,1k | İÇİNDE |
| S-4b | 8-15 · 3-5 dk | 14 · 4,5 dk · 60,5k | İÇİNDE |
| S-5 | 4-8 · 1-3 dk | 3 · 1,0 dk · 32,9k | araç ALTINDA |
Kaynak: Agent usage blokları (subagent_tokens toplam kullanım; tahmin alanı çıktı-token'dı — birebir kıyas ambar işlemesinde). Revizyon dersi: **antitez rolleri tahminden pahalı** (analojik komşu-alan taraması daha çok arama istiyor) — sonraki antitez tahminlerinde araç bandı tez bandına eşitlenmeli [K — tek koşum, S-1b örneği].

## 4. DEVİR-NOTLARI (paralel fren gereği bu oturum YAZMADI — ana oturum/Salih işler)
1. **Ledger `veri/karar-borcu.jsonl`:** İB-39 araştırma ayağı koşuldu → kapanış-kanıtı adayı `cc/rapor-2026-08-21-ab2-idempotens.md` (entegrasyon tasarımı + antitez turu AÇIK kalır) · İB-08 araştırma-önce şartı koşuldu → kapanış-kanıtı adayı `cc/rapor-2026-08-21-ab3-usage.md` (icra ayağı: FAIL-LOUD freni + çapraz-doğrulama betiği KALIR).
2. **Fikir kutusu:** V59 satırı (kutu:79) bayat — "ARAŞTIRILACAK" hükmü 07-22 koşumu (rapor §111-146) + bugünkü çift kolla EskİDİ; skill-bakım satırı (kutu:101) → "araştırma KOŞTU 08-21, tasarım masaya" güncellemesi.
3. **Bedel-defteri kalemi (08-15 raporu D-6 şartı):** "kapı sayısı arttıkça saldırı yüzeyi artar [K, arXiv 2605.17288, okundu 08-21]" — artık eklenebilir; "doğrusal olmayan" nicelemesi OLMADAN.
4. **KURAL ADAYI (Salih'e):** koşum-önü manifest kapısının grep'i varyant-toleranslı olmalı (tire/boşluk/büyük-küçük; ör. `ATLAS[- ]?V59`) — vaka: bu pipeline AB-4'ü "hiç koşmamış" sanıp kısmen mükerrer koştu (tireli desen boşluklu başlığı ıskaladı). Hafifletici: S-4a eski raporu kendiliğinden bulup üstüne koydu; zarar sınırlı ama vaka-3 (518k) sınıfının küçük tekrarı.
5. **Masa gündem adayları:** (a) AB-1 hibrit bakım tasarımı — kanon-aday, çift-kol malzeme hazır (takvimli canary + emeklilik 4-aşaması + İB-07 icrası); (b) AB-2 entegrasyon tasarımı — ÖNCE antitez turu (m.40b borcu açık).
6. **Mini borç adayı (opsiyonel, S-5 deseni):** Agenta'nın aktardığı GPT-4 %84→%51 rakamının birincil kaynağı (muhtemelen Chen ve ark. 2023) açılmadı — K'da kalıyor; kullanılacaksa tekil doğrulama.
7. **Senkron-log bayatlığı:** son kayıt 08-04 FAIL-ff, 17 gün sessiz — kök-neden bu pipeline'ın kapsamı dışında, açılış brifinde beyan edildi.

## 5. Arıza/ders kaydı
- Kapı-Ö ilk koşumda BLOKE (kayit alanı eksik) → onarıldı, ikinci koşum GEÇTİ (mekanik kapı işledi).
- Manifest-kapısı grep ıskası (bkz. devir-notu 4) — `[ariza]` sınıfı değil (kayıt bozulmadı), süreç dersi.
- Halüsinasyon yakalama: 1 adet (S-5 "doğrusal olmayan" güçlendirmesi, V26 çapraz-denetimde düşürüldü) — H=7 sözleşmesi + hakem denetimi birlikte çalıştı.

## 6. Kaptan beyanı (T)
**Araştırma-borcu koşumu hazır ve sisteme gömülü** — 5 borcun 5'i koşuldu; AB-3/AB-5 şartları kapandı, AB-1/AB-4 çift-kollu bulgu setleri ve AB-2 envanter+boşluk haritası karar-hammaddesi olarak masada; kayıt güncellemeleri devir-notlarında.
