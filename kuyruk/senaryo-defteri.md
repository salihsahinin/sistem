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


## Arşiv index — 07-13→07-21 kararları (tam metin: `kuyruk/arsiv/senaryo-defteri-arsiv-2026-07-23.md`)
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
- **Bağlam:** JARVIS kanon-yükleme mimarisi mekanik olarak nasıl kurulmalı? (P5 dersi Yarı-2; devir: `raporlar/vardiya-teslim-2026-07-22-ogrenme-P5.md`. Rakamlar deneysel/proxy, m.39.)
- **Model A (@import merkezi):** ~12-15K token/açılış sabit · kalite ~0.50 (eager: @import launch'ta tam genişler — "böldüm=hafifledi" yanılsaması) → ✗ | **Model B (kısa index + Read-on-demand):** ~2-3K sıcak · kararlı-prefix cache dostu · ~0.85 · m.20/m.34'ün birebir mekaniği → ✅ | **Model C (bölümlenmiş JIT: path-scoped rules + skills + topic dosyaları):** token en düşük · ~0.90 · kurulum maliyeti bugünkü kazancı aşıyor (tek-alan/tek-proje fazı).
- **Karşıt-temel:** A ← "tek dosyada her şey görünür olsun" bütünlük okulu; canlılık ✓ — eager mekaniğine yenildi (CC resmî doküman: "imported files load at launch").
- **Seçim:** B (Salih onayı 07-22: "P5 okudum, anladım" + emir: **C İLERİDE-GEÇİŞ olarak KAYITLI** — kutu V58 TETİKLİ satırı; B→C geçiş kriteri P6'da tasarlanır). 
- **Uygulama denetimi (Fable gözü, 07-22 — TARAMA sonucu):** fiilen ZATEN B'deyiz — CLAUDE.md 26 satır, backtick'siz @import YOK, okuma-sırası = pointer listesi; kapsül 27 / pano 35 satır; MEMORY.md yok. TEK BULGU: SessionStart hook kapsülü `sed 1,40p` ile basıyor = kendi sert-kapımız (MEMORY.md sert-200'ün minyatürü) — kapsül 40 satırı aşarsa kuyruk SESSİZCE düşer. Sigorta: boyut-izleme kuralına "kapsül ≤40 satır (hook-kapısı)" satırı eklendi.
- **Gözlem:** bekliyor — B'nin ~2-3K sıcak-önek tahmini ilk /usage ölçümüyle test edilir (K-009 kararlı-prefix standardıyla aynı ölçüm günü).
- **Ders:** disk-düzeni ≠ context-maliyeti; lazy'nin doğru mekaniği index+Read. Kendi kanunumuz (m.20) dış dokümanla bir kez daha triangüle oldu — P5 dersi kuralın MEKANİK gerekçesini verdi.

### 2026-07-22 · K-010 tetiği · takvim şartının kanıt-kapılarına çevrilmesi (Salih emri, öğle vardiyası)
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
- **Bağlam:** canary [D]: `core/` Bash-yazımına açık; settings-deny yalnız built-in Edit/Write tutar; OS sandbox native Windows'ta YOK (WSL2-only). A2'nin kalan tek kapısı. Dış araştırma: `cc/rapor-2026-07-22-1.md` (A5-F2 çekirdeği: kabuk-taşıyan ajan zaptedilemez; kabuksuz + dış-bant kilit zaptedilir).
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

### 2026-07-23 · sayı-araştırma turu — 4 hüküm (Salih imzası; kaynak `cc/rapor-2026-07-23-1.md`, 6-atlas, 234K alt-ajan token)
- **Bütçe birimi:** KB kalır + 20KB+ dosyalara token-izleme; 8/12/20/8/16 ONAYLANDI (GEÇİCİ damga kalktı) · 48KB FLAG → damıtma vardiyasında token-bazlı yeniden bütçe/bölme · ×1,4 tek çarpan onaylı · YENİ eksen: konum (tepe-çapa). KILAVUZ güncellendi.
- **Sicil:** 5/3/1 KALIR ama "c=0 go-gate, reliability kanıtı değil" etiketiyle + zaman-ayrıklık şartı + yuvarlanan hata-oranı izleme. 22-29'a çıkarma RED (blast düşük: kabuksuz-ajan + revert; hız ilkesi 07-22). Pano K-010/A1 güncellendi.
- **Eval:** 6+3 → SMOKE yeniden-etiketi + çıplak-%100 yasağı + yeni setlerde negatif ~10 + ≥3× koşum; 20-sorgu skill-creator protokolüne tam hiza (tek dış-standarda oturan sayımız çıktı). KILAVUZ eval kuralı revize.
- **Gözlem borçları:** ilk 3×-koşumlu eval turunda flakiness ölçümü · damıtma vardiyasında 48KB→token dönüşümü · atlas alt-ajanlarına ucuz-model denemesi (V59/K-020 hattı, /usage %19 bulgusu).
