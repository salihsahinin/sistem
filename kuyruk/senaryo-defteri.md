# Senaryo Defteri

> m.37'nin operasyonel eki (açılış: 2026-07-13 günaydın, A1c). Ölçek-eşiği üstü her karar bir blok: karar bağlamı + 3 model tahmini + seçim + koşum-sonrası gözlem. Kayıt birimi ayrımı (V39 NİHAİ FORM): SEÇİM = kontrol edilen kısım; 4-tuple (model · token · zaman · kalite) = koşum-başına GÖZLEM satırı — iki bağlı çift: maliyet çifti (token↔zaman) + bilgi çifti (seçim↔gelişim-katkısı). Kalite türetilmiş — credit-assignment olgunlaşana dek boş/tahmini kalabilir (ŞERH 4). Format deneysel damgalı (m.29); görünürlük şerti: her blok Salih'e sunulduğu oturuma işaret eder.

## Kayıt şablonu
### [tarih] · [kart/iş] · karar adı
- **Bağlam:** tek satır.
- **Model A:** ~token · ~süre · beklenen kalite | **Model B:** ... | **Model C:** ... → ✅ öneri + tek satır gerekçe
- **Karşıt-temel (m.37 ek, 07-17):** Model X ← [karşıt varsayım/okul], önerilenin [varsayımına] zıt; canlılık şartı: bilimsel temelli + bugün savunulabilir
- **Seçim:** X (kim: Salih onayı / Carvis Katman-2) — görünürlük: hangi oturumda sunuldu
- **Gözlem (koşum sonrası):** token gerçek · süre gerçek · kalite [türetilmiş]
- **Ders:** tek satır (ingest hammaddesi)

---

## Sıfır-noktası — geriye dönük ilk kayıtlar (A1d, 07-13)

### 2026-07-13 · A5 · veri-koşumu sayısı kararı
- **Bağlam:** yeniden-inşa deneyinde koşum sayısı sabit mi, kurallı mı?
- **Model A (sabit 10):** öngörülebilir bütçe · veri-israfı riski (iyileşme durmuşsa boşa koşum) | **Model B (ardışık-deney: pilot 5 [1 referans + 4 tek-nokta değişimi] → 3'erli partiler → devam: son parti >%5 başarı-skoru iyileşmesi → tavan 15):** bütçe-duyarlı, durma kurallı · hafif karmaşıklık | **Model C (iyileşme sürene dek sınırsız):** maksimum veri · V28 bütçe koruması yok → ✅ B
- **Seçim:** B (Carvis, Katman 2 — Salih yetki devri 07-13) — görünürlük: 07-13 oturumu + bu kayıt; eşikler deneysel (m.29), A7 denetimine tabi
- **Gözlem:** henüz koşum yok (tetik: K-009/K-010)
- **Ders:** sabit sayı yerine durma-kuralı = Salih anti-overfit kalıbının (V42) sayısal karşılığı

### 2026-07-13 · hafıza-denetimi · süpürme sınırı kararı
- **Bağlam:** biyoloji-kökenli terimler hafızadan nasıl temizlenir?
- **Model A (tam süpürme + tek pointer):** yoğunluk sıfır · terminoloji çevirisi maliyeti tek seferlik | **Model B (iki-sınıf: teknik kalır, dekoratif gider):** literatür dili korunur · yoğunluk kısmen sürer, tekrar riski kapanmaz | **Model C (pointer'sız tam süpürme):** en temiz · dış-arama anahtarı kaybolur → ✅ A
- **Seçim:** A (Salih, 07-13 günaydın — ilk seçim yanlış-enter, ikinci turda bilinçli teyit)
- **Gözlem:** uygulandı (commit 884d900); kalite gözlemi = sonraki oturumlarda model-düşümü tekrarı olup olmadığı
- **Ders:** hipotez kaydı düştü — düşüm↔hafıza bağı doğrulanmadı; gözlem sütunu bunu ölçecek

### 2026-07-13 · paralel yapılanma · başlangıç tarihi kararı
- **Bağlam:** paralel şerit düzeni (JARVIS + PortRisk + chat) ne zaman başlar? (Salih yetki devri: "başlangıç tarihine karar vermek sana kalmış")
- **Model A (bugün):** erken veri · yarın sınav, bant genişliği bölünür | **Model B (15 Temmuz, sınav ertesi):** tam dikkat, talimat hazır · 2 gün gecikme | **Model C (loop-eng bitince):** olgun başlangıç · PortRisk keyfî gecikir (m.36c ihlal ruhu) → ✅ B
- **Seçim:** B (Carvis, Katman 2) — görünürlük: paralel plan raporu + bu kayıt; chat şeridi bugün, Cowork paralel denemesi 15 Temmuz
- **Gözlem:** bekliyor (15 Temmuz koşumu)
- **Ders:** —

### 2026-07-13 · K-017/K-018 · bilgi-açığı kapama sırası
- **Bağlam:** dispatch + remote control 07-13'te tesadüfen öğrenildi; sistematik yeni-özellik taraması yok — geri-dönüşü pahalı açık (Salih tespiti, 2. oturum).
- **Model A (tarama önce: K-017 CC koşumu → sonra Model-A paketi):** ~1 CC koşumu + 1 inceleme oturumu · kalite 8/10 — sonraki araç kararları tam bilgiyle | **Model B (araçları hemen kur, tarama sonra):** hızlı · körü körüne benimseme riski, dispatch↔K-009 çelişkisi çözümsüz | **Model C (hepsini 15 Tem sonrasına ertele):** sıfır maliyet · açık büyür → ✅ A
- **Seçim:** A (Salih, 07-13 2. oturum — "bu iş bitince model a da yapılacaklar listesinde") — görünürlük: aynı oturum + bu kayıt
- **Gözlem (koşum sonrası):** koşuldu 07-14 — 70 bulgu (58/12/0), ~2,4M token · ~8,5 dk · 78 ajan; **konfig: Fable ultraworkflow (en yüksek efor, Salih beyanı — ilk koşum bilinçli maksimum; token gözlemi efor-parametreli okunur)**; kalite [türetilmiş]: yüksek — 12 hata doğrulamada yakalandı, adaylar panoya dağıtıldı
- **Ders:** bilgi-açığı sınıfı karar = araştırma-önce (m.40b); tarama tek-seferlik değil tekrar eden ihtiyaç — periyodik tarama kararı K-017 inceleme oturumuna aday

### 2026-07-14 · P0-P6 · partisyon planı onayı
- **Bağlam:** 07-14 kapanışında sunulan kronolojik partisyon planı (P1=15 Tem paralel · P2=16-20 Tem K-015+K-018 · P3=otonomi kapısı ~Ağu başı · P4=ölçüm+deney Ağu · P5=Jarvis v1+demo ≤10 Eki · P6=K-004 Kas) karar masasında.
- **Seçenekler:** olduğu-gibi onay | onay + P5 minimum-demo sabitlemesi (kayma riskine karşılık) | revizyon | veto → ✅ onay + sabitleme
- **Seçim:** Salih (07-14 sabah, Katman 1 — yön kararı): "kronolojik partisyon" çerçevesi teyit + önerilen sabitleme kabul. Plan dosyası: `raporlar/partisyon-plani-P0-P6-2026-07-14.md` (ilk sunumda dosyaya inmemişti — kalıcılık dersi orada kayıtlı).
- **İlk tahminler (deneysel damga, m.39 — Brier için):** P1 DONE-tanımıyla kapanır: 0.80 · P2 20 Tem'e dek kapanır: 0.65 · P3 kapısı Ağu ilk haftasında açılır: 0.60 · P5 minimum demo ≤10 Eki: 0.60
- **Gözlem:** her partisyon kapanışında tahmin-vs-gerçek buraya.
- **Ders:** kritik sunum, sunulduğu vardiyada dosyaya iner (V43 ailesi — kapsül özeti tek başına kalıcılık değildir).

### 2026-07-15 · şerit düzeni · öğrenme şeridi + öncelik revizyonu (P1 yeniden şekillendi)
- **Bağlam:** Salih günaydın emri: öğrenme oturumları şeridi + PortRisk 3. öncelik + Atlas'la müfredat araştırması. m.16 çelişki raporu sunuldu (P1 B-kanadı boşa düşer + P4 ölçüm girdisi gecikir, kritik yolda tampon yok).
- **Seçenekler:** PortRisk bugün yine açılır (P1 aynen, ✅ Carvis önerisiydi) | B kanadı öğrenmeye devredilir | Carvis'e devir → Salih üçüncü yolu seçti: "birkaç gün odak sadece öğrenme + Jarvis; ölçüm bankı önemli olmaya başlayınca 3. oturum olarak tasarlanır."
- **Seçim:** Salih (Katman 1 — yön kararı; 07-15 günaydın oturumu). P1 revize: ilk paralel deneme JARVIS+öğrenme çiftiyle, tetik = müfredat DONE. Plan: `raporlar/paralel-yapilanma-plani-2026-07-15-v2.md`. Kabul edilen risk: P4 itilmesi (kayıtlı).
- **Gözlem:** bekliyor (ilk JARVIS+öğrenme paralel günü + P4 açılış tarihi).
- **Ders:** öneri reddi de veridir — Salih odak-bölünmesini P4 riskinden pahalı fiyatladı; Brier notu: P1 "DONE-tanımıyla kapanır: 0.80" tahmini eski DONE-tanımıyla ölçülemez, revize DONE ile ölçülecek.

### 2026-07-15 · Atlas ilk koşumu · efor seçimi (Salih devri: "effort seçmek sana kalmış, bence yüksek")
- **Bağlam:** müfredat araştırması Opus'la koşulacak (Salih beyanı: token maliyeti); efor kademesi Carvis'te.
- **Model A (orta):** ~400-700K token · ~4-5 dk · kalite 6/10 — müfredat iskeletde kalır, kaynak derinliği zayıf | **Model B (yüksek):** ~1-1,5M token · ~6-8 dk · kalite 8/10 — eksen genişletme (Wave) + örneklem-denetim rahat çalışır | **Model C (maks/ultraworkflow):** ~2M+ token · ~8-10 dk · kalite 8,5/10 — K-017'de marjinal getirisi doğrulama katmanındaydı, o da artık örneklemli → ✅ B (maliyet/kalite dizi; Salih sezgisiyle uyumlu)
- **Seçim:** B — yüksek (Carvis, Katman 2) — görünürlük: 07-15 günaydın oturumu + görev emri `cc/gorev-2026-07-15-1.md`.
- **Gözlem (07-15, koşum sonrası):** süre ~25 dk · 13 ajan (K-017'nin 78'ine karşı) · token toplamı raporlanmadı (/usage istenmedi — ders) · kalite [türetilmiş]: yüksek — 0 DOĞRULANAMADI, 9 KISMEN düzeltmesi yakalandı, 19-partisyon müfredat kullanılabilir çıktı; Model B tahmini (8/10) tutarlı görünüyor, token kolonu boş kaldığı için maliyet çifti doğrulanamadı.
- **Ders:** fan-out'u ucuz modele (sonnet), sentez/denetim kararını pahalıya (Opus) veren iç-routing CC tarafında kendiliğinden doğru kuruldu — m.28/V39 routing ilkesinin dış teyidi; görev emri şablonuna /usage-raporu satırı eklenecek.

### 2026-07-15 · K-015 madde 3 / loop-eng Faz 4 · ilk Routine mekanizma seçimi
- **Bağlam:** Faz 2+3 kapandı; Faz 4 = ilk Routine. Homebase emekli → eski hedef (transkript pipeline) bayat. m.40b dış araştırma YAPILDI (code.claude.com/docs/routines): Routine bulutta koşar (PC kapalıyken de), repoyu GitHub'dan klonlar → lokale yapısal olarak DOKUNAMAZ, push varsayılan yalnız `claude/`-önekli dallara — "mimari > talimat" hazır örneği.
- **Model A (kalıcı günlük sabah-brifingi Routine):** ~15-30K token/gün · kurulum ~15 dk · kalite orta (yalnız origin'i görür, V43 yakalayamaz) · RİSK orta (kalıcı gözetimsiz koşum K-009 sınırına komşu) | **Model B (lokal scheduled task — gerçek-ağaç V43 nöbetçisi):** ~10-20K/koşum · kalite yüksek · RİSK yüksek (gözetimsiz lokal yazma = K-009'un kendisi; bugün açılmaz, K-009 açılış adayı) | **Model C (öğrenme-amaçlı: kur → 1 otomatik koşu gözle → duraklat / tek-seferlik):** ~15-25K tek koşum · ~30 dk toplam · kalite: Faz 4 DONE tam karşılanır · RİSK en düşük (kalıcı otomasyon kurulmaz, K-009 bloke korunur) → ✅ C. **NOT: RİSK sütunu bu blokta İLK KEZ (Salih ajan-yetki formülasyonu, 07-15 — m.37 4. boyut adayı sahada denenmiş oldu).**
- **Seçim:** C (Salih, 07-15 ana-sıra oturumu: "model c'den devam edeceğiz"). Mimari sınırlar: connector'lar çıkarılır · yalnız jarvis reposu · rapor-only prompt (pozitif yetki listesi) · claude/ push kısıtı korunur.
- **Gözlem (TAMAMLANDI 07-17 — trigger kaydı + Salih'in yapıştırdığı koşum çıktısı):** ateşlenme 16 Tem 09:00:18 (GMT+3), tam zamanında; tek-seferlik kendini kapattı (`run_once_fired` — Model C sınırı mimaride tuttu). süre · token: RAPORLANMADI (rapor-only prompt'ta /usage yoktu; bulut Routine'de maliyet gözlemi yapısal zayıf — K-019/K-009 notu). kalite [türetilmiş]: YÜKSEK — 25-satır limitine uydu · tüm maddeler commit-gerçeğiyle uyumlu, halüsinasyon 0 · sınır disiplini tam (dosya değişikliği/commit/push yok, origin'de iz yok) · öz-referans doğru ("bu koşum ilk çalıştırmanın kendisi"). Tek kesinlik şerhi: "kapsam (1)-(4) DONE" ifadesi madde 3'ü erken kapatıyordu — raporun kendi (2)(a) satırı bunu düzeltti.
- **Ders:** pozitif-yetki-listesi + rapor-only prompt İLK gözetimsiz koşumda sınır ihlalsiz çalıştı; tek-seferliğin kendini kapatması "mimari > talimat"ın Routine-katmanı kanıtı. **FAZ 4 + K-015 madde 3 KAPANDI (07-17).** Açık ders: bulut-Routine sınıfında token kolonu yapısal boş kalıyor — maliyet-gözlem mekanizması K-009 tasarım girdisi.

### 2026-07-17 · m.37 · karşıt-temel şartı (kanon revizyonu)
- **Bağlam:** Tractatus oturumu §10 önerisi + Salih 07-17 netleştirmesi: "karşıt-görüş içselleştirilmiş" = önerilen modelin matematiksel felsefesine ZIT felsefeden kurulmuş en az 1 model.
- **Seçenekler:** karar-başına adversarial denetim paneli (ilk Carvis okuması; ~600K token sınıfı, m.37'nin varlık sebebini ihlal) | model-ÜRETİM kuralı: zıt-temelli en az 1 model (ucuz yapısal kısıt; §9.5 ortak-kurgu bulgusunu mekanizmaya çevirir) | statüko → ✅ üretim kuralı + ölçekli karşıtlık + canlılık şartı
- **Seçim:** Salih (Katman 1, 07-17 Cowork günaydın): iki Carvis düzeltmesi (ölçekli karşıtlık + aygıt şartı) ONAY + canlılık şartı eklendi (bilimsel temelsiz / kesin çürütülmüş pozisyon karşıt-kaynak olamaz). Tüzük m.37 ek fıkrası imzalandı; görünürlük: bu oturum + bu kayıt.
- **Gözlem:** ilk uygulama = sıradaki ölçek-eşiği üstü karar; izlenecek metrik = yakınsama-kalitesi (zıt temeller aynı eyleme çıkıyor mu → gerçek triangülasyon sayacı).
- **Ders:** denetim katmanı EKLEMEK yerine üretim kuralı DEĞİŞTİRİLDİ — ucuz-yapısal çözüm pahalı-denetimsel çözümü yendi; dünkü panelin kendi bulgusu (§9.5) kendi revizyonunu üretti (sistem kendi çıktısından öğrendi — m.35 tezinin küçük bir örneği).

### 2026-07-17 · P1 devri · okuma-sırası / kararlı-prefix kararı
- **Bağlam:** P1 öğrenme oturumu "kapsül-önce okuma cache'i çürütüyor, sırayı ters çevir" önerisiyle devretti (Model B, ~8× iddialı). m.40b dış araştırma: resmi prompt-caching dokümanı — TTL en fazla 1 saat (cache güne taşınmaz) + oturum-içi transkript append-only (okuma sırası oturum-içi cache'i bozmaz) → iddia interaktif sınıfta geçersiz, TTL-içi tekrar-koşum sınıfında (loop/Routine/ajan filosu) geçerli.
- **Model A (statüko):** 0 maliyet · ders uygulamasız kalır | **Model B (CLAUDE.md okuma sırası şimdi değişir):** ~30 dk + Katman-1 çekirdek değişimi · bugünkü kazanç ~0 · "kapsül İLK okunur" çapası bozulur (m.40c YÜKSEK sınıf) | **Model C (sınıf-ayrımı):** interaktifte statüko; kararlı-prefix/değişken-suffix OTOMASYON sınıfının tasarım standardı (K-009 gündemi) + ilk loop koşumunda /usage ölçümü → ✅ C
- **Karşıt-temel (m.37 ek — İLK saha kullanımı):** öneri beklenen-maliyet/amortisman zemininde; zıt zemin 1 = ampirist ölçüm-önce okul (aygıt: kontrollü /usage ölçümü — türetilmiş 8×'e de TTL analizine de ölçümsüz güvenme) · zıt zemin 2 = minimax/worst-case (çekirdek-bozulma maliyeti ≫ cache kaybı → B aleyhine). Her iki zıt temel C'de kesişti — gerçek triangülasyon; canlılık şartı sağlandı.
- **Seçim:** C (Salih, Katman 1 — 07-17 Cowork ana-sıra: "kalanına onay"). Görünürlük: bu oturum + bu kayıt.
- **Gözlem:** bekliyor (ilk gerçek loop/Routine koşumunda /usage açılış-maliyeti).
- **Ders:** yan-oturum türetilmiş rakamı ("8×") dış-doğrulamadan karara girmedi — m.41 + m.40b hattı çalıştı; ders (prefix-invalidation) yanlış değildi, uygulanma SINIFI yanlıştı.

### 2026-07-17 · V39 dar koşumu · efor/bütçe konfigürasyonu
- **Bağlam:** V39 kavram-sözlüğü dar koşumu Salih onayı aldı (07-17); konfig Carvis'te (Katman 2). Kapsam dar: ≈12 terim, hedef = dış-eşleşme haritası.
- **Model A (düşük, ~200-300K · 4 ajan · kalite ~6/10):** ucuz · atıf-hatası riski yüksek (Atlas koşumlarının ana hata sınıfı) | **Model B (orta-yüksek, ~400-600K · 6 alan-ailesi ajanı + Opus sentez + V26 örneklem doğrulama · kalite ~8/10):** dar kapsama uygun ölçek | **Model C (yüksek, ~1M+ · terim-başına ajan + tam doğrulama · kalite ~8,5/10):** marjinal kazanç dar kapsamda düşük (K-017 dersi: doğrulama katmanı marjinali örneklemle korunuyor) → ✅ B
- **Karşıt-temel (m.37 ek):** öneri maliyet/kalite-dengesi (beklenen-değer) zemininde; zıt zemin = worst-case bilgi-maliyeti (yanlış iç-terminoloji köklenirse ileride toplu yeniden-adlandırma + yanlış-yöntem ithali maliyeti → C'yi savunur). Kesişim: B + zorunlu V26 denetim + V54 etiketsizlik kuralı (zorlama-eşleştirme birincil aranan hata) — worst-case'in asıl korkusu yanlış-eşleşme, o da denetim şartıyla kapanıyor; canlılık şartı sağlandı.
- **Seçim:** B (Carvis, Katman 2) — görünürlük: 07-17 Cowork oturumu + görev emri `cc/gorev-2026-07-17-1.md`.
- **Gözlem (07-17, koşum sonrası):** $7.16 · 19,5 dk duvar (38 dk API) · /usage TAM raporlandı (ilk kez emirle) · kalite [türetilmiş]: yüksek — 12/12 satır, TAM=9/KISMİ=3/X=0, örneklem D2/K1/X0, tavan aşılmadı. Model B tahmini (~8/10) tutarlı; sapma: fan-out /usage'da haiku etiketli (emir sonnet dedi) — maliyeti DÜŞÜRDÜ, kaliteyi düşürmedi (örneklem temiz); denetim notu raporda.
- **Ders:** dar-kapsam + alan-ailesi-bazlı fan-out deseni doğrulandı (K-017 "eşleşmesiz" bulgusunu tersine çevirdi); ucuz-model fan-out + pahalı sentez/denetim routing'i yine kendiliğinden doğru kuruldu — m.28/V39 ikinci dış teyit.

### 2026-07-19 · K-009 açılış · canlı-ajan sınırı + guardrail + ses-sırası (Katman 1, Salih)
- Bağlam: K-009 açılış oturumu (Cowork ana-sıra/Fable, 07-17→19). Gündem madde 1 + rapor-1 (otomasyon-3model) soruları birleşik karara bağlandı; karar öncesi Salih'e merdiven + PreToolUse [S]-düzey anlatıldı (V55), hizalama sagası koşuldu.
- Karar 1 — SINIR (m.30 ek fıkrası olarak İMZALANDI): otomasyon (K-009) = tetik devrine kadar (RC · /goal · /loop · sabit-promptlu Routine); canlı ajan (K-010) = prompt + kalıcı kimlik devri (ajan işi kendisi seçer; Dispatch/Agent-SDK sınıfı). Gerekçe: hata-sınıfı sıçraması — önceden-denetlenebilirlik kaybı + defter yoluyla hata birikimi (OpenClaw emsali); Özgürlük(a) ≤ Toparlanabilirlik(hata(a)). Empirik ayak: /goal + /loop + Routine koşumları sınır içinde temiz (07-15/16); ajan-karar basamağı hiç koşulmadı.
- Karar 2 — GUARDRAIL: PreToolUse policy-as-code kilidi İLK gözetimsiz otomasyon dilimiyle BİRLİKTE kurulur (deterministik allowlist: core/ yazma DENY · push ASK · raporlar/ ALLOW sınıfı; rapor-1 Model-C aşısı; G4<G5).
- Karar 3 — SES SIRASI: önce L2 mobil-köprü protokolü (KILAVUZ 1 sayfa; rapor-1 Adım 0) → sonra tek ölçümlü ses PoC; kapsam niyet-yakalama/triyaj (rapor-10 antitez daraltması — "oyunda ciddi inşa" iddiası DÜŞTÜ).
- Model-hiyerarşi beyanı (Salih 07-19): JARVIS/ana-sıra = Fable (final karar en zeki katmanda; bütçe/hesap bağlamı) · ekip liderleri = Opus ya da bir-altı en yüksek model · m.30(c) ile uyumlu; aile-dışı model (Kimi) planda YOK — V56 ERTELENDİ.
- Rapor-1 mimari seçimi: B (ölçüm-önce omurga) fiilen seçildi — üç somut karar, B + A-kaldıraç-sırası + C-guardrail-aşısı bileşimini uyguluyor. Karşıt-temel: rapor-1 bloğu (Wald minimax/DRO ↔ beklenen-değer/VoI) — m.37 karşıt-temel şartı sahada.
- Geri-alınabilirlik: SINIR tanımı = iki-yönlü (tüzük revizyonuyla değişir, ucuz) · GUARDRAIL = iki-yönlü (hook dosyası silinir) · model-hiyerarşi = iki-yönlü (beyanla değişir).
- Gözlem: bekliyor (ilk K-009 dilimi: gecelik senkron adayı + PreToolUse kurulumu + /usage ölçümü).
- Ders: —

**Ek (aynı blok, 07-19):** m.42 ajan-yetki kanunu İMZALANDI (7 fıkra; içerik 07-15/07-17 kabul edilmiş formülasyonların tüzükleşmesi — yeni taahhüt yok). Karar-sunum kuralı güncellendi (Salih emri): her karar sorusunun yanında kısa 'bu ne / neden masada' özeti zorunlu.

### 2026-07-19 · K-009 Dilim 1.5 + 1.3 · gecelik-senkron mekanizması + kararlı-prefix kapsamı (Salih seçimi)
- Bağlam: ilk insansız otomasyonun mekanizma seçimi (m.37 + karşıt-temel; m.40b taraması taze — rapor 1, 07-17). Sunum yeni kuralla: karar sorularının yanında "bu ne" özeti.
- 3 model: **A** deterministik script/LLM'siz (token 0/gece · kurulum ~30dk · kalite 8 · RİSK DÜŞÜK) ✅ | **B** CC headless gece koşumu (~5-10K token/gece, /goal emsali 5.3K · kalite 8.5 · RİSK ORTA) | **C** minimax gece-dokunma + sabah-elle (kalite 7 · worst-case EN DÜŞÜK · sabah-sürtünme kalıcı).
- Karşıt-temel: C ← Wald minimax / robust karar teorisi; A-B'nin beklenen-fayda varsayımına zıt; aygıt = f(otonomi×geri-alınamazlık×blast); canlılık ✓ (+ iç kanıt: V43 sicili, 3 mount-bozulma vakası).
- Seçim: **A + C aşısı** (Salih, 07-19) — ff-only (ezme sınıfı yapısal kapalı) + başarısızlıkta dokunma-yok/sabah-uyarı; B KURULMAZ, onarım elle-tetik kalır. İcra: `tools/gece-senkron.ps1` + `raporlar/usage/` (Dilim 1.4 asgarisi aynı adımda açıldı; scriptin log satırı ilk müşteri). Görev-kaydı (schtasks, tek komut) Salih'te.
- Kararlı-prefix kapsamı (aynı oturum, Salih): sınıf = KOŞUM DESENİ — TTL-içi aynı-önek tekrarı olan HER koşum otomasyon-sınıfı (işçi/lider/Routine fark etmez); interaktif oturumlar kapsül-önce KALIR (Model C, 07-17). İlk /usage ölçümü ilk LLM'li loop koşumunda.
- Geri-alınabilirlik (m.37 ek): İKİ-YÖNLÜ · blast: dar · geri-alma: ucuz (script+görev silinir) · LRM: yok · Kapı: Katman-2 + Salih seçimi.
- Gözlem: bekliyor — ilk gece koşumu `raporlar/usage/senkron-log.jsonl`e düşecek.
- Ders: —
