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

## Arşiv index — 07-13→07-21 kararları (tam metin: `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-07-23.md`)
- 2026-07-13 · A5 · veri-koşumu sayısı kararı
- 2026-07-13 · hafıza-denetimi · süpürme sınırı kararı
- 2026-07-13 · paralel yapılanma · başlangıç tarihi kararı
- 2026-07-13 · K-017/K-018 · bilgi-açığı kapama sırası
- 2026-07-14 · P0-P6 · partisyon planı onayı
- 2026-07-15 · şerit düzeni · öğrenme şeridi + öncelik revizyonu (P1 yeniden şekillendi)
- 2026-07-15 · Atlas ilk koşumu · efor seçimi (Salih devri: "effort seçmek sana kalmış, bence yüksek")
- 2026-07-15 · K-015 madde 3 / loop-eng Faz 4 · ilk Routine mekanizma seçimi
- 2026-07-17 · m.37 · karşıt-temel şartı (kanon revizyonu)
- 2026-07-17 · P1 devri · okuma-sırası / kararlı-prefix kararı
- 2026-07-17 · V39 dar koşumu · efor/bütçe konfigürasyonu
- 2026-07-19 · K-009 açılış · canlı-ajan sınırı + guardrail + ses-sırası (Katman 1, Salih)
- 2026-07-19 · K-009 Dilim 1.5 + 1.3 · gecelik-senkron mekanizması + kararlı-prefix kapsamı (Salih seçimi)
- 2026-07-19 · imza masası · çift-atlas kuralı kapsamı (m.40 ek fıkrası)
- 2026-07-19 · imza masası · skill-doğum kuralı (m.43)
- 2026-07-19 · imza masası · m.34 delta-fıkrası (damıtma yöntemi)
- 2026-07-19 · imza masası · m.30b ↔ m.21/m.34 uzlaştırma dipnotu
- 2026-07-19 · imza masası · m.38 limit-şerhi + m.37a örnek-çifti
- 2026-07-19 · ikinci günaydın vardiyası · m.16 kapısı: bayat-disk masa-tekrarı
- 2026-07-19 · ikinci günaydın vardiyası · Dilim 2.2 ses PoC — kanal seçimi
- 2026-07-21 · m.40b · sağlamlık ölçütü (K1, Fable hükmü)
- 2026-07-21 · m.40b · koşum aygıtı (K2, Fable hükmü)
- 2026-07-21 · öğrenme şeridi · grill-me kararı (K3, Fable hükmü)
- 2026-07-21 · yakalama-hattı · otomasyon sınıfı (K4, Fable hükmü)
- 2026-07-21 · ajan-taksonomisi · D1-D8 + arketip eşlemesi kabulü (Katman-2, deneysel)
- 2026-07-21 · K-016 · S-C/S-G inşa sırası

### 2026-07-22 · ajan-tasarımı · tester + denetçi model seçimi (Salih yönü, P4 sonrası)
- **Bağlam:** Salih (07-22): tester ve denetçi ajan kurulacaksa denetçi GPT (aile-dışı) olsun; tester şimdilik önerilen modelde, diğer 2 seçenek hafızada. m.16 kapısı çaldı: m.30 ek fıkra "aile-dışı model planda yok (V56 ERTELENDİ)" — çelişki değil, V56'nın YENİDEN AÇILMASI (rapor sunuldu, Salih yönü kayda).
- **Model A (denetçi=GPT, tester=önerilen-aile-içi):** korelasyonsuz kör nokta (multihop: aynı ön-eğitim→korelasyonlu hata) · üretici≠doğrulayıcı YAPISAL + AİLESEL ayrım · ikinci API=para+veri-akışı | **Model B (ikisi de aile-içi):** tek hesap, basit · denetçi kör noktaları üreticiyle örtüşür | **Model C (denetçi=aile-içi farklı model):** kısmi ayrım, para yok · aynı-aile korelasyonu kısmen sürer → ✅ A (Salih yönü)
- **Karşıt-temel:** B ← hesap-minimalizmi + veri-tek-şirkette; canlılık ✓ — kayıtta kalır, K-010 imza masasında tartılır.
- **Seçim:** KOŞULLU YÖN, net karar YOK (Salih düzeltmesi 07-22, aynı gün): lojik form (m.38) — (K-010 açık ∧ GPT-API bütçesi VAR [Salih beyanı+imzası]) → denetçi=GPT (Model A) · (K-010 açık ∧ ¬bütçe) → B/C alternatifleri masaya döner. Para belirsizken hiçbir kol kilitlenmedi; tasarım sorusu açık: denetçiye ham iş mi iddia-listesi mi (CoVe-Factored ailesi).
- **Geri-alınabilirlik:** çok yüksek — kayıt; inşa yok.
- **Gözlem:** bekliyor (K-010).
- **Ders:** V56 erteleme-iptali sinyali ilk kez rol-bazlı geldi (genel hiyerarşi değil, TEK ROL için aile-dışı) — "aile-dışı" kararı monolitik değil rol-başına alınabilir.

### 2026-07-22 · K-009 · gece-senkron arıza çözümü
- **Bağlam:** script hiç koşmamış; neden netleşti (Salih beyanı): PC geceleri KAPALI; schtasks DAILY 06:00 kaçan görevi telafi etmez.
- **Model A (ONLOGON tetiği):** kaçırma yapısal imkânsız · idempotent script (ff-only) çoklu-koşuma dayanıklı · tek sefer admin | **Model B (DAILY + StartWhenAvailable):** günde-1 semantiği · ayar CLI-dışı (XML/GUI), kırılgan kurulum | **Model C (startup-klasörü kısayolu):** adminsiz · Task Scheduler envanteri dışı (K-009 kayıt disiplinine aykırı) → ✅ A
- **Karşıt-temel:** B ← "senkron GÜNLÜK ritüel olmalı" okulu; canlılık ✓ — yenildi: işlev açılış-senkron; ritim PC kullanım desenine bağlanınca isabetli.
- **Seçim:** A (Carvis Katman-2, m.37 görünür; veto açık) — **KURULDU 07-22 (Salih, admin schtasks: SUCCESS).** "Gece-senkron" adı kalır, işlev = açılış-senkron (yeniden adlandırma K-019 hijyen turuna).
- **Gözlem:** bekliyor — ilk log satırı `raporlar/usage/senkron-log.jsonl`.
- **Ders (aday):** zamanlanmış otomasyonda tetik, MAKINENİN değil KULLANICININ yaşam dönemine bağlanmalı (kapalı makinede saat yok).

### 2026-07-22 · bağlam-yükleme mimarisi · P5 Yarı-2 ingesti (Şerit 2 → Şerit 1)
- **Bağlam:** JARVIS kanon-yükleme mimarisi mekanik olarak nasıl kurulmalı? (P5 dersi Yarı-2; devir: `raporlar/vardiya/vardiya-teslim-2026-07-22-ogrenme-P5.md`. Rakamlar deneysel/proxy, m.39.)
- **Model A (@import merkezi):** ~12-15K token/açılış sabit · kalite ~0.50 (eager: @import launch'ta tam genişler — "böldüm=hafifledi" yanılsaması) → ✗ | **Model B (kısa index + Read-on-demand):** ~2-3K sıcak · kararlı-prefix cache dostu · ~0.85 · m.20/m.34'ün birebir mekaniği → ✅ | **Model C (bölümlenmiş JIT: path-scoped rules + skills + topic dosyaları):** token en düşük · ~0.90 · kurulum maliyeti bugünkü kazancı aşıyor (tek-alan/tek-proje fazı).
- **Karşıt-temel:** A ← "tek dosyada her şey görünür olsun" bütünlük okulu; canlılık ✓ — eager mekaniğine yenildi (CC resmî doküman: "imported files load at launch").
- **Seçim:** B (Salih onayı 07-22: "P5 okudum, anladım" + emir: **C İLERİDE-GEÇİŞ olarak KAYITLI** — kutu V58 TETİKLİ satırı; B→C geçiş kriteri P6'da tasarlanır). 
- **Uygulama denetimi (Fable gözü, 07-22 — TARAMA sonucu):** fiilen ZATEN B'deyiz — CLAUDE.md 26 satır, backtick'siz @import YOK, okuma-sırası = pointer listesi; kapsül 27 / pano 35 satır; MEMORY.md yok. TEK BULGU: SessionStart hook kapsülü `sed 1,40p` ile basıyor = kendi sert-kapımız (MEMORY.md sert-200'ün minyatürü) — kapsül 40 satırı aşarsa kuyruk SESSİZCE düşer. Sigorta: boyut-izleme kuralına "kapsül ≤40 satır (hook-kapısı)" satırı eklendi.
- **Gözlem:** bekliyor — B'nin ~2-3K sıcak-önek tahmini ilk /usage ölçümüyle test edilir (K-009 kararlı-prefix standardıyla aynı ölçüm günü).
- **Ders:** disk-düzeni ≠ context-maliyeti; lazy'nin doğru mekaniği index+Read. Kendi kanunumuz (m.20) dış dokümanla bir kez daha triangüle oldu — P5 dersi kuralın MEKANİK gerekçesini verdi.

### 2026-07-22 · K-010 tetiği · takvim şartının kanıt-kapılarına çevrilmesi (Salih emri, öğle seansı)
- **Bağlam:** Salih emri: "zaman tetikli iş istemiyorum; 2 hafta beklemek yerine tetik şartlarını kronolojik partisyonlu aşamalar olacak şekilde güncelleyelim — bekleyecek vakit yok." m.16 kapısı çaldı: K-010 ön-koşulu "temel katman 2 hafta sorunsuz" (07-10 kart; 07-22 sabah sicil kuralı; K4 kaydında referans). Rapor sunuldu: eksi = takvim-bazlı pasif gözlemin yakalayacağı seyrek/aralıklı arıza sınıfı (haftalık desenli schtasks tipi) kısalan pencerede görülmeyebilir; artı = kanıt yoğunluğu pasif beklemeden yüksek — her kapı AKTİF test üretir; ufuk ~10 Ekim'e karşı 14 gün ölü bekleme savunulamaz. Mitigasyon: arıza-kuralı korunur (sayaç sıfırlanmaz ama kök-neden kapanmadan aşama kapanmaz) + sicil kapanışla DURMAZ, K-010 sonrası da izlenir.
- **Model A (mevcut: takvim 2 hafta):** token ~0 · zaman 14 gün SABİT (kullanımdan bağımsız ölü bekleme) · kalite ~0.6 — gözlem pasif, devir-adımları tek kapıda test edilmemiş | **Model B (tek sayaç: 10 ardışık OK koşum):** token ~0 · zaman ~7-10 gün (ONLOGON ≈ PC-açılış ritmi) · kalite ~0.7 — aktif ama monolitik; /goal//loop/Routine basamakları yine sınanmadan açılır | **Model C (kronolojik partisyon A1-A4, paralel yürütme):** token düşük (tatbikat koşumları) · zaman ~5-8 gün (kritik yol A3; A2/A4 bugün başlar) · kalite ~0.85 — m.30 ek-fıkra devretme merdiveniyle birebir: her devir sınıfı (tetik→kontrol→durma-koşulu) kendi kanıt kapısından geçer → ✅ C (önerilen ∧ Salih emri aynı yönde)
- **Karşıt-temel:** A ← "nadir arıza ancak takvimde görünür" ihtiyat okulu (OpenClaw emsalinin ruhu); canlılık ✓ — arıza-kuralı + sürekli-sicil mitigasyonuna yenildi: takvim bilgi ÜRETMEZ, koşum üretir.
- **Seçim:** C (Salih emri 07-22 = Katman-1 imza; aşama-eşikleri [5/1/3 sayıları] Carvis Katman-2, deneysel m.29; veto açık). Lojik form (m.38): K-010 ← K-009 ∧ A1(5×OK ∧ incident=0) ∧ A2(kilit-PASS ∧ revert-tatbikat ∧ bütçe-yazılı) ∧ A3(/goal-OK ∧ /loop-OK ∧ Routine-3×OK); A3 ← A1∧A2 ∧ A4(defter-şeması ∧ D4-kartı ∧ denetçi-çatalı).
- **Geri-alınabilirlik:** yüksek — kapı tanımı; sıkılaştırma tek satır revizyon.
- **Gözlem:** bekliyor — ilk ölçüm: A1 sayacının fiilî günlük ritmi (öngörü ~1 koşum/gün) + A3 basamağının gerçek süresi.
- **Ders (aday):** 07-22 sabah dersi ("tetik kullanıcının yaşam dönemine bağlanır") genelleşti: BEKLEME de öyle — kapı takvime değil, kullanıcının ürettiği kanıt akışına bağlanır.

**Revizyon (aynı gün, öğle-2 — Salih emirleri):** (1) **Araştırma-kapısı eklendi:** her A-aşamasının adımı öncesi çift-atlas CC araştırması zorunlu — araştırmasız adım yok (V60). (2) **A5 ekip-lideri hattı açıldı (PARALEL, tetiği geciktirmez):** gerekçe Fable kota-tükenişi → görev devri; lider kuruluşu = K-010 ∧ A5; tasarım CC derin-araştırma ön-koşullu. **m.16 notu:** 07-21 kararı "ilk canlı-ajan sınıfı = araştırma-filosu (D4, en düşük bahis)" duruyor — A5 TASARIMI paralel başlar, KURULUŞ SIRASI (işçi-önce ∨ lider-önce) K-010 gününde ayrı karar; çelişki ancak lider İLK ajan yapılırsa doğar, o gün rapor yenilenir. (3) **Hız ilkesi kayda:** kapılar koşum-sayısı bazlı → sistem hızı Salih'in çalışma ritmiyle ölçeklenir (07-22 sabah dersinin emre dönüşmüş hali). (4) V59 kutuya: token-verim okuyucu ön-katmanı (arkadaş tasarımı) — araştırma başlığı görev emrinde.

**Gözlem eki (07-22 akşam):** (1) atlas-kosum v0.2 İLK CANLI KOŞUM (CC, 3 atlas × 3 aile, 18 ajan, ~793K token [K — öz-beyan, /usage çaprazlanmadı]): hayatta-kalma 9/9 sağlam çekirdek · 8/9 DARALTILDI · ~10/100 alt-iddia DÜŞTÜ — m.40b v0.2 diyalektiği çalışıyor, DARALTILDI-sinyali üretimi kanıtlandı. (2) Kilit saha-testi: #1-3 (Edit/Write→core/, CLAUDE.md, .claude/) PASS · git push onay-kapısı PASS · **#4 Bash-yolu: yapısal kilit KAPSAMIYOR, davranışsal ret durdurdu; canary ile [D]** — Dilim-1 kilidi built-in araç sınırıdır, tüm-yazım sınırı DEĞİL (Windows sandbox yokluğuyla bileşik). Karar girdisi: A2 platform kararı (Salih). (3) A2 tatbikat kalemi DONE (ebb6287→69471e3 revert çifti); sert-bütçe standardı yazıldı (şema dosyası eki) → A2'nin kalan tek kapısı = PLATFORM KARARI.

### 2026-07-23 · K-010/A2 · platform kararı — kabuksuz-ajan rejimi (Salih imzası: "önerinden devam edelim")
- **Bağlam:** canary [D]: `core/` Bash-yazımına açık; settings-deny yalnız built-in Edit/Write tutar; OS sandbox native Windows'ta YOK (WSL2-only). A2'nin kalan tek kapısı. Dış araştırma: `cc/rapor/2026-07/rapor-2026-07-22-1.md` (A5-F2 çekirdeği: kabuk-taşıyan ajan zaptedilemez; kabuksuz + dış-bant kilit zaptedilir).
- **Model A (kabuksuz-ajan + core/-Bash PreToolUse teli):** token ~0 · zaman ~1-2 saat · kalite ~0.8 — ajan sınıfına kabuk/exec verilmez → kaçış-kapısı yapısal olarak yok; şema bayrağıyla ("kabuk VAR → dış-bant izolasyon ZORUNLU") birebir uyumlu | **Model B (WSL2 şimdi):** zaman 1-2 gün + taşınma-arıza riski · kalite ~0.9 (gerçek dış-bant) ama prototip hızını yer; fiilen K-011'in büyütülmüş hali | **Model C (davranış-birincil):** zaman 0 · kalite ~0.4 — kapı KANIT ister, kabul beyanı kanıt değil → ✅ A
- **Karşıt-temel:** B ← "tek gerçek dış-bant OS sandbox" okulu; canlılık ✓ — yenilmedi, ERTELENDİ: B, K-011 gününe bağlandı (Salih gün seçince birleşik göç; o gün sandbox açılır, rejim gevşetilebilir).
- **Seçim:** A (Salih 07-23, Katman-1). Lojik form (m.38): (ajan-araç-seti ∋ kabuk ∨ exec) → dış-bant-izolasyon ZORUNLU; bu faz: ajan-araç-seti ∌ {kabuk, exec}. Hook teli = tökezleme-teli, güvenlik sınırı DEĞİL (iç-bant; m.29 deneysel).
- **Geri-alınabilirlik:** yüksek — rejim kuralı; WSL2 kapısı açık kalır.
- **Gözlem:** bekliyor — hook telinin kurulumu+ilk canlı yakalama · K-010 ilk ajan koşumunda rejim denetimi.
- **Sonuç: A2 KAPANDI (4/4).** K-010 kalan: A1 (2/5) ∧ A3 (A1∧A2∧A4'e bağlı) ∧ A4 (denetçi bütçe-çatalı).

### 2026-07-23 · K-015 · bağlam-yönetim stratejisi — P6 Yarı-2 kararı (ana-sıra kaydı; öneri görünür sunuldu, m.37 onay-beklemez)
- **Bağlam:** P6 dersi (07-22) K-015 şema taslağını kurdu; nihai kayıt ana-sıraya devredilmişti (ders kanona yazmaz). Ders: `ogrenme/dersler/2026-07-22-P6-context-eng-compaction.md`.
- **Modeller (deneysel/proxy, m.39):** A compaction'a-güven (~0.60, kararlar kayıplı özete erir) ✗ | **B not-tutma-öncelikli + iki-parçalı stabil-prefix (sıcak ~2-3K · ~0.85 · m.20/m.34/m.9 birebir) ✅ seçildi** | C tam-izolasyon (~0.90 · ~7× işçi-token; tetiği araştırma-filosu D4 canlıya alınınca — B→C eşiği kayıtlı).
- **Uygulama borcu (Şerit 1):** sıcak dosyaların iki-parçalı yerleşimi (değişmez çekirdek üstte, volatil/tarih altta — kapsül "Güncelleme" satırı şu an TEPEDE: prefix-invalidation adayı, K-015 kurulumunda düzeltilir).
- **Gözlem:** bekliyor — ilk K-015 kurulumunda token/cache ölçümü deftere.

### 2026-07-23 · sayı-araştırma turu — 4 hüküm (Salih imzası; kaynak `cc/rapor/2026-07/rapor-2026-07-23-1.md`, 6-atlas, 234K alt-ajan token)
- **Bütçe birimi:** KB kalır + 20KB+ dosyalara token-izleme; 8/12/20/8/16 ONAYLANDI (GEÇİCİ damga kalktı) · 48KB FLAG → damıtma seansında token-bazlı yeniden bütçe/bölme · ×1,4 tek çarpan onaylı · YENİ eksen: konum (tepe-çapa). KILAVUZ güncellendi.
- **Sicil:** 5/3/1 KALIR ama "c=0 go-gate, reliability kanıtı değil" etiketiyle + zaman-ayrıklık şartı + yuvarlanan hata-oranı izleme. 22-29'a çıkarma RED (blast düşük: kabuksuz-ajan + revert; hız ilkesi 07-22). Pano K-010/A1 güncellendi.
- **Eval:** 6+3 → SMOKE yeniden-etiketi + çıplak-%100 yasağı + yeni setlerde negatif ~10 + ≥3× koşum; 20-sorgu skill-creator protokolüne tam hiza (tek dış-standarda oturan sayımız çıktı). KILAVUZ eval kuralı revize.
- **Gözlem borçları:** ilk 3×-koşumlu eval turunda flakiness ölçümü · damıtma seansında 48KB→token dönüşümü · atlas alt-ajanlarına ucuz-model denemesi (V59/K-020 hattı, /usage %19 bulgusu).

## Arşiv index — 07-29→08-15 kararları (tam metin: `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md`; damıtma 08-17, KB-37)
*Her satır bir blok: tarih · başlık · arşiv satırı. Açık kalemler `veri/karar-borcu.jsonl`'da (pointer'lar arşive eşlendi).*
- 2026-07-29 — CC-mekanik doğrulama koşumu (compaction/bağlam; P6 Faz A+B) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:5`
- 2026-07-29 GECE — O2/O3 ingest kararları + Z6 kapanışı + m.37 revizyon talebi → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:11`
- 2026-07-30 — ana seans: O4+5/6 ingest damgaları (Katman-2, veto açık) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:17`
- 2026-07-30 — MERGE çözüm planı (analiz Carvis/klon-ölçümlü; icra Salih terminali) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:24`
- 2026-07-30 — MERGE İCRA EDİLDİ + senkron OK (SONUÇ kaydı) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:29`
- 2026-07-30 (2) — 30-1/30-2 ingest damgaları (Katman-2, veto açık) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:34`
- 2026-07-30 (3) — 30-3/30-4 ingest damgaları (Katman-2, veto açık) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:41`
- 2026-07-30 (4) — üretim freni AYRIŞTIRILDI + masa girişi kararı (Salih beyanları, akşam) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:48`
- 2026-07-30 (5) — bağlam hijyeni İKİNCİ EKSEN adayı + denetçi emrinin genişletilmesi → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:58`
- 2026-07-30 (6) — 30-5/30-6 ingest damgaları (Katman-2, veto açık) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:66`
- 2026-07-30 (7) — ARIZA KAYDI: kendi skill'lerimiz kullanılmadı (Salih yakaladı) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:132`
- 2026-07-31/08-01 — İngest turu ① masa-hizmetliler + ② araç kararları (8 rapor; Carvis ana-sıra/Fable, alt-ajan… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:235`
- 2026-08-01 — İngest turu ③ TAMAM: kalan 12 rapor (Carvis ana-sıra/Fable, 3 alt-ajan ≈498K token; Katman-2, vet… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:242`
- 2026-08-01 (2) — Salih usul beyanı + 08-01 CC raporlarının ingest'i (Carvis ana-sıra/Fable; 2 alt-ajan ≈130K) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:250`
- 2026-08-01 (3) — 08-01-3 (iz-hasadı) + 08-01-4 (m.40b antitezi) ingest; TARİHLİ BORÇ ana kısmı KAPANDI → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:258`
- 2026-08-01 — KATMAN-1 MASASI, 1. oturum (ana-sıra Cowork, Carvis/Fable; gündem `kuyruk/masa-gundemi-2026-07-30… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:268`
- 2026-08-01 · MASA 2. OTURUM (ana-sıra Fable, akşam ~21:00) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:314`
- 2026-08-02 · A1 seri doğrulaması İCRA (md.42 borcu; Carvis ana-sıra/Fable — gözlem kaydı, kapı hükmü DEĞİL) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:364`
- 2026-08-02 · GEÇ SEANS (rapor 08-02-1 tam ingest; Carvis ana-sıra/Fable) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:369`
- 2026-08-02 · GEÇ-2 (Carvis ana-sıra/Fable) — masa-hazırlık usulü STANDART + B1/B3 icra + usage-otomasyon borcu → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:375`
- 2026-08-03 · K2 MASASI KAPANDI — 15/15 (ana-sıra Fable, gece ~00:30; gündem `kuyruk/masa-gundemi-K2-2026-08-02… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:380`
- 2026-08-03 · ARIZA KAYDI: model-düşümü ölçüldü, şerh KAPANDI (temiz oturum Fable; tam rapor `raporlar/2026-08-… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:401`
- 2026-08-03 · SALİH EMRİ (YÜKSEK ÖNCELİK): L8/Kun-Chen workflow = fikirsel öncül + m.16 çelişki kaydı → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:408`
- 2026-08-03 · L8 KARAR MASASI (taze oturum, Fable) — İCRA-ÖNCE hükmü, masa KISA KAPANDI → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:413`
- 2026-08-04 · P1 DONE (L8 icra-önce hattı, ilk partisyon kapandı — saha koşumu Salih terminali, ~05:30-05:45) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:421`
- 2026-08-04 · P3 DONE (iki ayak) + lavish güvenlik incelemesi (~05:50-06:00) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:428`
- 2026-08-04 · SALİH EMRİ (Katman-1, "bu bir emirdir" damgalı): JARVIS = genel asistan, Jarvis projeleri DAHİL —… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:435`
- 2026-08-04 · Share-freni KURULDU + entegrasyon/temizlik ERTELEME emri (~06:10) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:440`
- 2026-08-04 · GECE-SENKRON ARIZASI + ONARIM (taze seans açılışı, ~sabah) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:446`
- 2026-08-04 · P2 ÖN-ARAŞTIRMA: no-mistakes birincil-belge okuması (m.40 dış-araştırma) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:452`
- 2026-08-04 · P2 DONE (3/3) — no-mistakes uçtan uca, 2 koşum (~06:30-07:15) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:459`
- 2026-08-12 — KATMAN-1 KARAR: Doğrudan yalnız-firstmate geçişi (Salih emri, Mac Cowork SON oturumu) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:512`
- 2026-08-13 — m.40b koşum gözlemi: spec-kit araştırması (terminal ana-sıra, ilk büyük atlas koşumu) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:520`
- 2026-08-14 — KATMAN-1 KARAR: Skill üretim/evrim/tetikleme yetkisi Carvis'e (Salih emri) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:526`
- 2026-08-15 — KATMAN-1 KARAR: Oturum-tetiği revizyonu — "seans başı / seans bitimi" + zaman-kayması freni (Sali… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:538`
- 2026-08-15 — KATMAN-1 KARAR: Skill-Üretim Şeması v1 (kapı-ağacı, hallucination-freni) AKTİF (Salih emri) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:549`
- 2026-08-15 — KATMAN-1 KARAR: Skill-Tetiklenme Şeması v1 (çağrı sözleşmesi) AKTİF (Salih emri, Hat-2) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:563`
- 2026-08-15 — KATMAN-1 KARAR: Halüsinasyon-Önleme Paketi v1 + Görev-Müsaitlik Derece Formülü + halusinasyon-eng… → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:574`
- 2026-08-15 — KATMAN-1 KARAR: Şema-Sıkıştırma v1 AKTİF + damitma v1.1 şema-dalı (Salih emri, Hat-4) → `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-17.md:585`

## Arşiv index — 08-16→08-20 kararları (tam metin: `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-21.md`; damıtma 08-21, boyut-tetiği KB-17c)
*Kalem detayı + kapanış kanıtları `veri/karar-borcu.jsonl` / `veri/gorunum/v_karar_borcu.csv`'de; burada seans-başına hüküm özü.*
- **08-16 seans-7 — İLK VE İLK KURAL (Katman-1):** her teslimin birinci ölçütü SALİH'İN ANLAMASI → CLAUDE.md §0. Kayıt TN-001/002.
- **08-17 seans-8 (Karar 1-8 + Beyan 9-12 + masa 5 parti):** CLAUDE.md v2 (≤80 satır/7 KB) · AÇIK KAYNAK ilkesi (m.14 revize) · şirket metaforu EMEKLİ + halef sözlük cascade (K-024) · kaynak dosyalar TÜRKÇE · DETERMİNİSTİK TASARIM (stokastik entegrasyon geri alındı; KB-04/05/06 RED) · okunabilirlik + hareket kütüğü · rol = KÖLE · V26 kural-tabanlı örneklem (Karar 8) · masa partileri: KB-01..16 + KB-33/35/37/38 hükümleri (kanıtlar borç kütüğünde) · Beyan 10 → KB-39..42 (silver temizlik) · Beyan 11 → KB-43..45 (hafıza teknikleri) · Beyan 12 → KB-50..52 (bağlam bütçesi).
- **08-18 seans-9 (Beyan 13-15 + Katman-1 karar):** indeks-araması → KB-53/54 · sütunsal depolama → kolon-katmani/PR #2 (KB-55/56) · tarama yöntemleri → PR #3 (KB-57/58) · GİZLİ KLASÖR YOK → CLAUDE.md §2.
- **08-20/21-gece seans-11 masa (Karar 29-47):** KB-17b/19/26 ölçüm-önce · KB-18 paket + m.43 N=3→5 (Karar 30) · KB-20 K-016 SON BİTEN · KB-21 11 dal arsiv/-tag'li silindi · KB-22 envanter 11/11 → entegrasyon masası · KB-23/24 EK-6 triyaj+süpersede (Karar 41 S1-S3; daraltılmış masa 9 kalem, ⑨ DONDUR) · KB-25 K2-l/K2-m (m.40b SAĞLAM/DARALDI/DÜŞTÜ kanon; yön: deterministik∧idempotent, İB-39) · KB-27 C ilke + A uç-eşikli (m.46(d)) · KB-28 pozitif-karşılık 8/8 yazım turu · KB-19 zinciri kapanış (Karar 43: çapa PASS → kısaltma, hazine 7.379 F1e yeşil) · KB-29 → entegrasyon devri · KB-30 → monolit bindirme İB-40 (Karar 45) · KB-31 BEKLET-tetikli (Codex beyanı) · KB-32 → AGENTS.md statik levha (Karar 47).

## Arşiv index — 08-21 kararları 48-64 (tam metin: `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-29.md` §1; damıtma 08-29, Karar 74 M-3)
- **Karar 48** kendini-analiz kısıtı (analiz yalnız üstten alta; Fable öz-analiz ≈0; OLAP istisnası) · **49** pano şablon v3 (Started damgası) · **50** seans-hedefi denemesi · **51** skill-eşik kuralı (n≥10 medyan 2×) · **52** FAIL-damga bronz (kosum-sonuc) · **53** M-1 tarihî-kayıt damgası · **54** KB-36 süpürme 13 hüküm (+sözlük-dondurma gerekçesi) · **55** [ariza]/[revert] commit önekleri · **56** GİRMEZ listesi (agile 7 kalem) · **57** RESUME kapısı kuralı · **58** silver-sağlık mimarisi (bayrak+güncel-görünüm+kuyruk; 4 yüklem) · **59** λ tazelik düzeltmesi (kalibre-edilmemiş damgası; T-Ç6 genel kural) · **60** KB-43/44/45 hafıza üçlüsü + MODEL-KUŞAĞI şerhi · **61** bağlam bütçesi mutlak-token seti · **62** adresli erişim + tazelik kapısı · **63** kolon katmanı venv-koşullu kabul · **64** tarama kuralı + PR #3 merge/push. Hepsi hükme bağlı, icraları ledger'da.
## Arşiv index — 08-22 seans-13 kararları 65-68 (tam metin `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-09-04.md` §1; damıtma 09-04)
- **Karar 65 · DETERMİNİZM ÖNCELİĞİ (Katman-1, Salih aynen arşivde):** determinizmle çelişkide determinizm kazanır → CLAUDE.md §6 öncelik kuralı; atlaslara belirtilir.
- **Karar 66 · KB-59 (a):** Karar 60 sırası aynen (FTS5 → ölç → hibrit/vektör) + vektör ÖLÇÜM KOLU şartnamesi (İB-47: multilingual-e5-large + sqlite-vec + RRF).
- **Karar 67 · KB-60 (a):** "graf dilinde konuşma" protokolü v0 (P1 adresleme=D2 anahtarı · P2 yapısal soru SQL · P3 graf elle düzenlenmez · P4 kanon/silver değişir graf türetilir).
- **Karar 68 · ANAKRONİZM YASAĞI (Katman-1, Salih aynen arşivde):** zaman-bağımlı iddia AS-OF damgasız çıkmaz; `wiki/anakronizm-freni.md` + `tools/anakronizm-denetim.py`; muafiyet sorusu D6-3 → masa-8 M4 AÇIK.
## Arşiv index — 08-26→08-29 kararları 69-78 (tam metinler `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-08-30.md`; damıtma s22 08-30)
- **Karar 69 (+EK, EK-2):** İlk Lavish masası — KB-62..66 hükümleri (a/a/a/b/a) · KB-66 satır-takası icrası.
- **Karar 70 · 71:** 08-26 hükümleri; 71 = ÇOK-OTURUM DÜZENİ (Salih beyanı aynen arşivde).
- **Karar 72 (+EK):** QuickLook iptal → md yüzeyi Obsidian; EK: graf-bağlantı (a) icra — `tools/obsidian-harita.py` + ileri-dönük md-link biçimi. **[Karar 80 ile revize: yüzey = VS Code]**
- **Karar 73 (+EK):** Varlık felsefesi (`core/varlik-felsefesi.md`: makine+matematik+ansiklopedi) + MIT 6.006/6.042J birebir kursları; EK: `kuyruk/galeri-siralama/` commit'lenmez freni.
- **Karar 74 (+EK-düzeltme):** İkinci Lavish masası — açık-kararlar 9/9 (M-1..M-9; M-4→İB-54 fren paketi); M-9 [revert] vakası kayıtlı.
- **Karar 75 · 77:** s20 emir-kararları; 77 = paylaşılan-jsonl merge tuzağı SOP (türev dosyada merge DENENMEZ — üretici yeniden koşulur, üretilen hâl commit'lenir).
- **Karar 76:** Üçüncü masa — ENTEGRASYON 13/13 (E-1 araç sınırı · E-2 firstmate · E-4 axi-standardı · m.37(e) riske-göre-derinlik İMZA · m.13 artefakt≠kurulum · E9 m.8 süpersede-teyit).
- **Karar 78 (+EK):** Dördüncü masa — EK-6 daraltılmış 10/10; m.43 2.REV (birim=GÖREV, N=3; zincir 3→5→3) · m.25 V47 şerhi · ölçüm-bankı→DE-GOLD süpersede · İB-60/İB-61 açıldı · MASA KUYRUĞU BOŞALDI (⑨ tetiği Salih beyanına kaldı → s21'de açıldı-kapandı, Karar 79).

## Arşiv index — 08-29→08-31 kararları 79-84 + icra blokları (tam metin `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-09-04.md` §2; damıtma 09-04)
- **Karar 79 (+D3 icra):** Beşinci Lavish masası ⑨ DONDUR 7/7 (`raporlar/masa/masa-dondur9-karar-yuzeyi-2026-08-29.html`); Frozen-95 → deterministik sayım 64 kalem; D3 İB-62 yazım turu KOŞULDU (m.39 şerhi, KILAVUZ tasarım-ilkeleri satırı).
- **Karar 80:** Karar 72 revizyonu — md açma yüzeyi VS CODE (Obsidian isteğe bağlı); İB-53 daraldı (kalan aday Foam, Salih tetiğiyle).
- **m.40b gözlemleri (İB-53 · İB-63 atlasları):** hakem kalemleri 40→11 SAĞLAM (İB-53) · V26 6/6 PASS · İB-63 antitez-B K-DÜŞÜŞ (uydurma atıf ilk yakalanış) — ölçüm satırları arşivde.
- **Karar 81 (+EK, EK-2):** "gece senkron uyarlaması gerekmez, sistem 7/24 çalışır hâle gelecek" (Salih aynen arşivde) → Mac 7/24; **A1 yeni biçim:** ardışık 5 başarılı OTOMASYON-KOŞUMU ∧ incident 0 (birim koşum) — A1 5/5 KESİN Karar 83 EK-2.
- **Karar 82 (+EK):** zamanlı-loop öncelik değil (Salih uzun loop'ları kendisi tetikler); A3 3. ayak = "Salih-tetikli uzun-loop 3 OK" (sayaç 1/3, Karar 84 EK-2).
- **[icra] 08-29→30 icra-devam oturumu:** İB-42/05/08/60 kapandı; teslim `raporlar/seans/seans-teslim-2026-08-30-icra-devam.md`.
- **Karar 83 (+EK, EK-2):** Altıncı Lavish masası K-010 paketi 19 hüküm (`raporlar/masa/masa-k010-paketi-karar-yuzeyi-2026-08-30.html`): A1 manifest şeması+PK-1..12 · B1 YETİM eşiği 351 · B2 `--parquet` varsayılan · **B3 T-A katmanlı triyaj** (icra 09-03 U5) · B4 İB-10 · C1 İB-57 · D1 İB-53 sentez (2B+odak, 3B RET) · E2 İB-07+09 onay; EK: A1 5/5 + firstmate onaylı + /goal.
- **Karar 84 (+EK, EK-2) — Katman-1 davranış kuralı (Salih aynen arşivde):** loop kurulumu gnhf ile, prompt planlayıcıdan ajana devredilir (Kun Chen firstmate deseni); EK: iki şerit — gece/sensiz → gnhf · izlenen → AYRI OTURUM (prompt Carvis, yapıştırma Salih) → **İB-65 açıldı**; EK-2: gece koşumu A3 3. ayağa sayıldı (1/3).
- **[icra] 08-31 gece:** İB-66 (gözlemlenebilir nested-loop atlası) · İB-67 (paper aday) · İB-68 (ürün aday) · İB-69 (matris koşum, SIRALI 2 aile) AÇILDI — koşum devri `cc/devir/devir-2026-08-31-opus-icra.md`.
- **[icra] 08-31 öğleden-sonra 3-emir paketi:** İB-70 kod-optimizasyon turları · İB-71 kod-oranı turları · İB-72 karantina · İB-73 eğitim serisi (tanımlar ledger `veri/karar-borcu.jsonl`; 70/71/72 ilk icra 09-03 Cowork U2-U4).
## Arşiv index — 09-02 kararları 85-86 + 09-03 İB-77 icra blokları (tam metin `arsiv/kuyruk-arsiv/senaryo-defteri-arsiv-2026-09-09.md`; damıtma 09-09, Karar 88 M16)
- **Karar 85 (09-02, Katman-1):** Opus emekli; ikili = Fable planlayıcı + Sonnet işçi; kanon şerhleri tüzük m.30/42/44 · ajan-metodolojisi §37 · research-agent R4 · gorev-emri/pipeline-kosum · 2 wiki (§1). **09-09 NOT:** Salih masa-9 M8 beyanı ("ekip lideri opus olsun … opus5 medium") bu kararla çelişir — m.16 raporu Karar 88, hüküm bekliyor.
- **Karar 86 (09-02, 7. masa FS 8/8):** D1 statik skill-orkestratör (+ tohum `kuyruk/ekip-lideri-ogrenme-desenleri.md`) · D2 tek Fable + Sonnet pipeline (Salih notu → İB-75) · D3 m.40b üçlü (yapan≠hakem · URL'siz V26 kotası · ≥2 birincil açılış) · D4 İB-76 · D5 manifest `tur` (→ Karar 88 M3) · D6 sağlık paketi (→ M4) · D7 devir toplu · D8 İB-70..73 sırası (§1).
- **İB-77 görselleştir (09-03):** pipeline koştu (8 Sonnet işçi, 22 kaynak, hakem D14/K7/X4), ürün `gorsellestir.py` + skill; 22:10 Salih "beğenmedim, sil" → arşiv → 09-09 KARANTİNA (Karar 88 M10); 2 [ariza] beyanı (öğrenme d2 render'ı) → Karar 88 M5 deneme-sürümü kuralının kaynağı (§2).

## Arşiv index — 09-04 Karar 87 + 09-09 Karar 88 (tam metin `arsiv/kuyruk-arsiv/senaryo-defteri-arsivi-2026-09-10.md`; damıtma 09-10 Karar 92 M5)
- **Karar 87 (09-04, 8. masa):** M1 icra yan-oturumu = Cowork "bu seferlik" · M2 damıtma turu aynı seansta · AÇIK kalemler 9. masaya aynen · push beyanları 09-04/09-08 · Lavish "Add to queue" notu.
- **Karar 88 (09-08→09, 9. masa, 14 kalem → 11 a + M6 hükümsüz + M11 beklet):** masa-kalitesi dersi (yüzey elle DaisyUI) · M3 manifest `tur_ustyazim` · M4 KURAL Karar 68 EK tarihli-dosya muafiyeti · M5 m.47 skill deneme-sürümü · M7 rapor yolu = EMİR · M8 İB-75 lider tasarım emri · M9 senkron kütüğü EMEKLİ · M10 ilk karantina tescili · M12 kod-oranı süzgeci · M13 T-A şiddet formülü · M14/15 karantina-envanter · M16 icra sırası.

## Arşiv index — 09-09→09-17 Karar 89-98 + Karar 96 + icra blokları (tam metin `arsiv/kuyruk-arsiv/senaryo-defteri-arsivi-2026-09-21.md`; damıtma 09-21, Karar 105 M7; kural sayacı tetiği 09-18)
- **Karar 89 (2026-09-09 ~10:10, Salih Katman-1 — m.16 çelişki raporu sonrası hüküm aynen: "başka açık oturumlar var, m8 çelişkisi için kararım **
- **Karar 90 (2026-09-09 ~10:40, Salih Katman-1, aynen: "5 başarılı koşum çok fazla 1 olsa yeter her hareketimizde çok fazla test ve ölçüm yapar**
- **Karar 91 (2026-09-09 ~13:40, Salih Katman-1 — dört mesajlık sorgulama sonrası "nihai önerinden devam"; beyanlar aynen: "gün sonunda gidilece**
- **Karar 91 EK (2026-09-09 ~15:00, Salih Katman-1, aynen: "şimdi bu ekip liderinin bi adı olsun ve hangi görevler için ekip lideri olduğu tanım**
- **Karar 91 EK-2 (2026-09-09 ~15:5x, Salih Katman-1, aynen: "yeni reponun doğumunun temel ihtiyaç şartlarından biri de birbirinden bağımsız con**
- **Karar 92 (2026-09-10 ~10:20-10:45, 10. Lavish masası; yüzey `raporlar/masa/masa-10-karar-yuzeyi-2026-09-10.html`; tetik Salih "bende bekleye**
- **Karar 93 (2026-09-10 ~11:4x, Salih Katman-1, aynen: "benle konuşan ajan jarvis olacak. b seçeneğinden gidelim. sistemin adı benle konuşan aj**
- **Karar 92 M3 EK — görev iletişim formatı (Salih 09-10, aynen: "direk chate yüklenecek md dosyası formatında iletişim kurulmasını istiyorum … **
- **Karar 93 EK (Salih 09-10 ~12:0x, aynen: "en baştan beri bilinen bir ayrım(jarvis/carvis) ise tüm contexti bu konuda halüsinasyon olmayacak ş**
- **Karar 94 (2026-09-11 ~10:4x, Salih Katman-1, masa-11 Lavish `raporlar/masa/masa-11-karar-yuzeyi-2026-09-11.html`, hükümler seçenek metniyle **
- **Karar 94 EK — ürün turu (Salih Katman-1, 2026-09-14 ~10:5x, aynen: "öğrendiğim konuları öğrenme süreci bitince bir üründe kullanıp/bir ürün **
- **Karar 94 EK-2 (Salih 09-14 ~11:0x, aynen: "llm as a judge konusu güncelde nasıl kullanılıyorsa ve ele alınıyorsa ben de öyle kullanmak istiy**
- **Karar 94 EK-3 (Salih 09-14 ~11:4x, hüküm: seçenek 3 = güvenlik):**
- **Karar 97 (2026-09-15 ~14:4x, Salih Katman-1, aynen: "onay, önce kuru diff koş" → "… kullanılabilir bir muadil araştırması yapıp önerilerini **
- **Karar 95 EK (Salih Katman-1, 2026-09-15 ~12:3x, aynen: "tamam şimdi önerdiğin şekilde devam edelim ve sorunları önerdiğin versiyonda çöz"):**
- **Karar 95 (Salih Katman-1, 2026-09-15, aynen: "bundan sonra her bir oturumumda create pr yapacağım. böylelikle conflictin önüne daha rahat ge**
- **Karar 94 EK-4 (Salih 09-15, aynen: "sürecin son aşaması … öğrendiklerimden skill oluşturma aşaması da olsun … staj sürecinde öğrendiğim tüm **
- **Karar 94 EK-5 (Salih 09-15 ~16:5x, aynen: "sisteme implement etme aşaması için bir örnek de 'siber güvenlik ajanı' gibi öğrenilen konunun ic**
- **Karar 98 (2026-09-16 ~17:4x, Salih Katman-1, "1. seçenekten gideceğiz"):**
- **Karar 96 (2026-09-15 ~15:3x, Salih Katman-1, masa-12 Lavish `raporlar/masa/masa-12-karar-yuzeyi-2026-09-15.html`, 7 kalem; hükümler seçenek/**
- **[icra] blokları (16):** 09-10 Karar 93 EK + Friday tur-2 · 09-15 büyük-harf freni · yan-oturum arıza · İB-92/90/91/89/88 · hook arızası · md→skill atlas · 09-16 İB-93 · Friday tur-3 · 09-17 büyük-harf kök neden · İB-83 ilk bulgu · atlas-kosum alt-ajan usulü — tam metin arşivde.

- **Karar 99 (2026-09-18 ~11:0x, Salih Katman-1, masa-13 Lavish `raporlar/masa/masa-13-karar-yuzeyi-2026-09-18.html`, 13/13 hüküm seçenek metniyle aynen; kayıt ana-sıra, karar-kaydet ritüeli Salih tetikli):** **M1 (a)** Friday yan oturum değildir: Karar 95 yalnız ~/jarvis worktree oturumları için; Friday kendi §5 kuralında kalır (main, push yok, pathspec-only) · **M2 (a)** Friday okuma-izin.sh'a agent_id dalı: işçi çağrısında liderin kapsül/pano/defter/kutu + kütükler RED (Jarvis pretool-altajan-okuma deseni); test dosyasına Z1-Z3 vakaları · **M3 (a)** Friday settings.json deny listesi 3b aynen girer (core/ hariç), okuma-izin.sh kalır; listeyi tazeleyen taraf Jarvis · **M4 (a)** desen core/desenler.md'ye girer (Friday çekirdek + Jarvis kanon), kanıt C1 §3a · **M5 (a)** dalga protokolü yalnız atlas-kosum SKILL'inde; **Salih eki aynen: "a diyeceğiz ama atlas damıtılmayacak"** · **M6 (Salih aynen: "şablonu core'a almadan önce şablonun başarılı olup olmadığını bi test edelim")** → şablon v0 core/'a girmez; önce ilk vaka (hakem ajanı) ile canlı test, başarı ölçüsüyle masaya döner · **M7 (c) dokunma + Salih aynen: "ontoloji satırlarının pozitif etkilemediğini kanıt olarak sunmak için önerilen kısımlar çıkarılmış farklı bir araştırma ajanıyla aynı koşum yapılarak çıktıları karşılaştırılabilir"** → A/B koşum: atlas aynen ∥ ölü-bölümsüz varyant (`atlas-sade`, deneme alanı), aynı emir, hakem kıyası · **M8 (a)** galeri kota k=3; ekip dokümanı gönderilir; sıradaki: yöntem işyeri reposu src/ + analiz §9 · **M9 (a)** mat-felsefesi şeridi açık; tetik "seans başı, mat-felsefesi"; ogren v0.2 · **M10 (a)** seans-hedefi kalıcı kural: seans-acilis brif sonu + seans-kapanis yoklama; deneysel damga düşer (tüzük m.29 satırı Salih eliyle/Edit kilidi) · **M11 (çoklu, üçü)** yan-oturum-merge · ib-kalem · silver-sorgu → skill-kapisi K0 · **M12 (a)** Ö3-Ö6 jarvis hazinesinde, genelleştirilmiş formatta (md.49); üretim ana-sırada; **Karar 98 satırındaki "Ö3-Ö6 staj reposunda" ibaresi Jarvis yazım hatasıydı, bu hükümle düzeltildi (m.16)** · **M13 (çoklu)** İB-79 hook tasarımı ilk 10 satır imzalandı (icra Ö1 sonrası) + İB-80 tetiği kanıt sayacına (FIFO 2 kez bayt sigortasına takılınca); Q2/Q4/Q6/parti-34 seçilmedi → kutuda kalır. **Masa arızaları (aynı gün):** üretici onsubmit kesme-işareti hatası (`a3d6473`, test E4) · Jarvis'in kendi tarayıcı panelinde oturumu açması Salih'in yüklemesini düşürdü (ders: masayı Jarvis açmaz). **İcra borçları:** İB-107 Friday tur-4 emri (M2 hook dalı + M3 deny bloğu + M4 desen; A1 v0.2 blok) · İB-108 hakem ajanı = şablon v0 ilk vaka + başarı ölçüsü (M6) · İB-109 atlas A/B ontoloji koşumu (M7) · İB-110/111/112 yan-oturum-merge / ib-kalem / silver-sorgu K0 (M11) · İB-79 icra · İB-80 sayaç · mat-felsefesi tetik satırı · seans-acilis/kapanis m.29 damgası.

*Parçalı defter (Karar 130 D26, 2026-11-11): kararlar aşağıdaki parçalarda sırayla durur; yeni karar en son parçanın (`senaryo-defteri-k124.md`) sonuna eklenir; parça 20 KB'ı geçince yeni parça açılır ve buraya `@` satırı eklenir. Sırayla okuma: `baglam genislet`.*
@senaryo-defteri-k100.md
@senaryo-defteri-k104.md
@senaryo-defteri-k112.md
@senaryo-defteri-k118.md
@senaryo-defteri-k124.md
