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

## 2026-07-29 — CC-mekanik doğrulama koşumu (compaction/bağlam; P6 Faz A+B)
- Kaynak: `cc/rapor-2026-07-29-3.md` (11-satır Faz A tablosu + Faz B denetim; koşum CC/opus-high, damga ana-sıra/Fable 07-29). Pointer m.20 — tablo buraya kopyalanmadı.
- Öne çıkan: **A.3 ÇÜRÜTÜLDÜ** (CLAUDE.md = sistem promptu SONRASI kullanıcı mesajı; byte-stabilite sorusunun cevabı) · **A.11 KISMEN ÇÜRÜTÜLDÜ** (Cowork aynı mimari ama `~/.claude` okumaz; Cowork'te CLAUDE.md/compaction [ARANAMADI] ⇒ CC-kuralı Cowork'e otomatik taşınmaz) · **C.1 teyit + keskinleşti** (kapsül satır-konumu cache VE kesilme ekseninde konusuz; kural yalnız MEMORY.md+SKILL.md'ye) · A.10b resmî ~7x · Faz B: kapsül HOOK-enjekte, hook compact'ta da koşuyor (D2 kapsül ayağı kazara kurulu — SAHA-TESTSİZ) · tüzük-thrash CC'de desteklenmedi (0 Read/12 transkript) · compaction izi 0 (negatif kanıt, şerhli) · YENİ sızıntı yolu: compaction sonrası skill LİSTESİ yeniden enjekte edilmiyor.
- Karar: D1-D7 tasnifi `raporlar/vardiya-teslim-2026-07-29-anasira.md`; Katman-1 kalemleri orada. Üçüncü-taraf "%98 eşik" rakamı KANON DIŞI.
- SONUÇ (m.37, gözlenecek): [açık] — saha testi: tek kasıtlı /compact + kapsül-dönüş kontrolü.

## 2026-07-29 GECE — O2/O3 ingest kararları + Z6 kapanışı + m.37 revizyon talebi
- **Z6 (m.41↔m.31 çelişki adayı) m.16 kapısından geçti ve KAPANDI:** rapor sunuldu (çelişki+artı/eksi+plan), Salih hükmü: m.41'in kastı GEREKLİLİK — ana-sıra∧Fable yeterlilik değil, uygulama Salih emir/onayıyla; amaç "en üst sürümün karar sürecinde olması" (sürüm-genel). Metin düzeltmesi `↔`→`→` Katman-1 masasında. Kayıt: defter O2-hasat damga ③.
- **Katman-2 damgalar (Carvis, veto açık):** O2'nin kapsam-aşan §1.3 denetimi KAPSAM-İÇİ (Z5/Z6 geçerli) · O1 devir md.1 KAPSAM DARALTMASI kabul (INSAN-borcu → dosya-başına; kesin borç tek dosya) · K10 önerme-formu kurallarında YOK tespiti (L31+K10 birleşik aday paket).
- **m.37 revizyon TALEBİ (Salih, karar DEĞİL):** 3-model sunumları decoy/compromise desenine kayıyor — gerçek-fedakârlık (Pareto baskın-olmama) şartı istendi; m.40(a) gereği araştırma-önce: `cc/gorev-2026-07-29-5.md`. SONUÇ (gözlenecek): [açık] — rapor ingest'inde revizyon taslağı masaya.
- **Görev emirleri (Katman-2 derleme):** O4 (`gorev-2026-07-29-4.md`, Ç1 uzlaştırma ana teslim) · gorev-5 (Pareto) · gorev-6 (Cowork→CC engel envanteri; yön kararı DEĞİL). Üçü de commit-yasağı + numarasız-aday kuralıyla.

## 2026-07-30 — ana vardiya: O4+5/6 ingest damgaları (Katman-2, veto açık)
- **Ç1 KULLANIM düzeyinde KAPANDI (ana-sıra damgası):** §4.6 uzlaştırması kabul — karşıt-okuma yapıldı ("geniş bant" itirazı geçerli; hüküm kapsamaya dayanmıyor). Künyesiz 0,31 ∧ doğrulanmamış ~%85 kullanılmaz; alet = P19 görev-tipi tablosu; "genel kalite" yargıca sorulmaz; yargıç≠üretici aile. KÜNYE düzeyi AÇIK (D5; erişimli oturumda tek seferde). §7.2 metin düzeltmesi Katman-1'de. Kaynak: `cc/rapor-2026-07-29-4.md` §4.
- **Okuma programı O1-O4 KAPANDI:** 23/23 rapor; kapanış envanteri (B-1..15 + D-1..21) `cc/rapor-2026-07-29-4.md` §13.
- **Dosya düzeltmeleri (m.8 üstü-çizili+[K]):** INSAN-pasif-ogrenme bekçi bölümü + ajan-durma-atlas §4 watchdog satırı — işlendi, veto=revert.
- **m.37/m.41 karar-girdileri masaya İNDİ:** KG-M37-1..10 + KG-CC-1..8 (özet `kuyruk/build-tartisma-notlari.md` 07-30 bloğu). İkisi de İMZASIZ — Katman-1.
- SONUÇ (gözlenecek): [açık] — Katman-1 masası tek oturumu; m.37 fıkrası imzalanırsa ilk 5 tam-form koşumda kalibrasyon denetimi.

## 2026-07-30 — MERGE çözüm planı (analiz Carvis/klon-ölçümlü; icra Salih terminali)
- Ölçüm: 7 birleşmemiş dal (5 değil); ana-sıra zinciri pasif⊂anasira-29⊂gece tek merge; 16 dosya YALNIZ dallarda (opus5:6 [serit1-5+telefon, 07-24] · orca:9 [07-19/20 araştırmaları] · agent-hierarchy:1 [ajan-baglam-hazinesi]); mount tüm ortak dosyaların EN YENİ hali (fikir-kutusu V63/V64 dahil; P0-tahminler main'de boş şablon, mount'ta dolu); main'de mount'a üstün/eksik içerik YOK; disk HEAD = pasif dalı + push'lanmamış yerel commit (a611f11, origin'de yok).
- Plan: yedek → dirty commit → 16 dosyayı `git checkout <dal> -- <yol>` ile kurtar+commit → 5 merge `-s ours` (içerik zaten diskte, soy kaydı için) → main'i buraya taşı → push → senkron elle koşum doğrulaması. Komut dizisi Salih'e verildi.
- SONUÇ (gözlenecek): [açık] — push sonrası ilk gece-senkron OK dönerse kök-neden kapanır; FAIL sürerse script pull-adımı/ls-remote doğrulaması masaya (07-23 fren adayları).

## 2026-07-30 — MERGE İCRA EDİLDİ + senkron OK (SONUÇ kaydı)
- Salih terminali: yedek → union commit (44 dosya) → 16 dosya kurtarma → 5 × `-s ours` merge → `main` push (`b97aac8..348ed67`, 89 commit) → working tree clean. Elle tetiklenen senkron: **OK, 348ed67→348ed67, dirty 1, 2 s** — FAIL-ff serisi (3 koşum) KAPANDI.
- 07-30 planının SONUÇ alanı: [gerçekleşti — beklentiyle birebir; çakışma çıkmadı]. Yalancı-OK kök-nedeni (dallanmış origin) ortadan kalktı; 07-23 fren adayları (pull-adımı + ls-remote doğrulaması) hâlâ İYİLEŞTİRME adayı olarak masada (arıza tekrar ederse tetiklenir).
- A1 sicil notu: sayaç etiketi Salih/masa işi — bu OK, arıza-sonrası ilk temiz koşumdur (zaman-ayrık şartına göre değerlendirilir).

## 2026-07-30 (2) — 30-1/30-2 ingest damgaları (Katman-2, veto açık)
- **Ç1 TAM KAPANDI:** kullanım-düzeyi (07-30 sabah) + künye-düzeyi (D5: "üç turda bulunamadı" kaydıyla kapatıldı; Thakur mekanizması [D] soruyu cevapladı). Yeniden açma koşulu: künye kendiliğinden bulunursa kayıt güncellenir, karar değişmez.
- **K14 KAPANDI [D-ölçüm]:** Explore sürdürülebilir; askı kalktı. Kalan: Plan 30-sn testi (ilk uygun CC koşumunda).
- **m.37 taslağı İMZAYA HAZIR DEĞİL (ana-sıra hakemlik ön-damgası):** antitez hükümleri sayısal ve yeniden-üretilebilir (kod + tam sayım); madde 2/6/7 revizyonsuz imzalanamaz; S1 teşhisi + madde 5/8/10/12 taşınır. v2 sentez borcu açıldı. m.16 kalemi (karşıt-temel çelişkisi) Katman-1 masasına eklendi.
- **[X] düzeltme borçları (m.8 dosya işlemleri, sıradaki uygun vardiya):** pasif-ogrenme-atlas §6.2 AAR daraltması (üstü-çizili + [K]: self-led bileşimler en etkili) · O1 hasat AAR/Staab/Park satırlarına düzeltme notu (eski hasat yeniden yazılmaz, not düşülür) · Staab %95,8→%95,2.
- SONUÇ (gözlenecek): [açık] — v2 sentez + Katman-1 masası; KG-B1-1/2 (Model B sınır koşulu + öz-değerlendirme kapısı) masada karara bağlanacak.

## 2026-07-30 (3) — 30-3/30-4 ingest damgaları (Katman-2, veto açık)
- **v2 sentez (30-3) ana-sıra hakemliği:** rakamlar antitezle birebir tutarlı (0,1379 · 0,0257 · 0,5871 tekrarlandı); taşıyıcı hamle = kapı↔etiket rol ayrımı — 3 KIRILDI'nın 2'sini (madde 2+6) tek hamlede, 7'yi ikameyle kapatıyor; geriye-dönük 3 vaka 3/3 doğruya dönüyor (v1'de 3/3 yanlıştı). Metin İMZASIZ; KG-V2-1..10 Katman-1'e. Usul kalemi AĞIRLAŞTI: üç koşum (tez·antitez·sentez) tek model ailesi, v2'nin yeni fıkraları saldırı görmedi (KG-V2-7).
- **masa-gundemi küme 1 v2 ile YAMANDI (m.8: özgün satırlar üstü-çizili korundu):** madde 1/3/5 önerisi değişti · 2/4/6/7 güncellendi · **7a (kademe çözünürlüğü, KG-V2-3) YENİ karar kalemi** · madde 44'e KG-V2-10 notu. Gündem 49→50 karar satırı; 30-4'ün §5.1 riski ("v2 farklı çare üretebilir") gerçekleşti ve kapatıldı.
- **KG-M37 → KG-V2 eşleme (kayıt):** 1→1 · 2→2 (çözüm değişti: sayı yazılmaz, türetilir) · 3→5 (yön TERS döndü) · 5→6 · 6→8 · 7→7 · 8→10 · KG-M37-4 Katman-2'de kalır · KG-M37-9 iki gözlemde duruyor (üçüncü tekrar gelmedi) · KG-M37-10 DARALDI (dayanak ön-baskı düzeyi).
- **Mount-git ilk deneme (kapsül md.4 yetkisi):** bu ingest'in commit+push'u doğrudan mount'tan atıldı — sonuç bu satırın altındaki commit'te. **SONUÇ: BAŞARILI ama şerhli** — commit `ab7f894` + push OK (3e33518..ab7f894); ŞERH: sandbox git kendi kilit dosyalarını (HEAD.lock/index.lock/tmp_obj) mount'tan silemedi (Operation not permitted) — Cowork silme-izni verilince temizlendi, repo temiz. Ders: mount-git her koşum sonrası kilit-artığı kontrolü ister (07-15 stale-lock sınıfının yeni yüzü); Katman-1 mount-git kalemine girdi. Şerh: teslim raporu "kural Katman-1 masasına dek GEÇERLİ" diyor, kapsül md.4 kapanış-denemesine izin veriyor; gerilim masada çözülür, deneme kapsül yetkisiyle yapıldı.
- SONUÇ (gözlenecek): [açık] — Katman-1 masası (giriş: `kuyruk/masa-gundemi-2026-07-30.md`, artık v2-güncel); üretim freni SÜRÜYOR (masa oturana dek yeni araştırma CC'si yok).

## 2026-07-30 (4) — üretim freni AYRIŞTIRILDI + masa girişi kararı (Salih beyanları, akşam)
- **Fren ayrıştırma (Salih onayı):** masa-hizmetli CC'ler SERBEST (mevcut kalemlerin altını dolduran koşumlar; "yeni karar kalemi AÇMA" şartı emirlere yazılır) · yeni-konu araştırma CC'leri masa oturana dek KAPALI. Gerekçe: Salih token/limit ziyan etmek istemiyor + birikim mekanizması korunuyor.
- **Masa girişi:** Salih bugün Katman-1'e girmiyor (bilinçli erteleme — zihinsel yük beyanı; m.23 gereği yorum yok, çıplak kayıt). Giriş noktası KARARLAŞTI: **küme 1 madde 7 (usul)** — menteşe maddesi.
- **Madde 7 EĞİLİM notu (karar DEĞİL):** Salih uzun vadede (c) çapraz-aile denetçiyi en mantıklı görüyor; engel kurulum bilinmezi → gorev-30-5 bu bilinmezi kapatmaya koşuldu. İmza yok, Katman-1 kaydı değil.
- **Derlenen emirler (Katman-2) — Salih itirazıyla İKİ KEZ REVİZE:**
  - `cc/gorev-2026-07-30-5.md` — ilk çerçeve YANLIŞTI (kurulum mekaniği merkezli). Salih düzeltmesi: "mesele sadece indirmek değil, sıfırdan bağlam vermek". Emir yeniden yazıldı: ana bölüm = BAĞLAM DEVRİ tasarımı, kurulum ikincil. Emrin taşıdığı yeni gerilim (Carvis tespiti): çapraz-aile denetçinin değeri çerçevemizi paylaşmamasıdır ⇒ ona kanonu yüklemek aile-körlüğünü çerçeve-körlüğüyle değiştirir; sorulan soru "minimum yeterli bağlam + neyi bilerek vermiyoruz" (kör denetçi ↔ bağlamlı denetçi kıyası, m.37 v2 somut vakasıyla). Bu gerilim masa madde 7+28'in altına girdi olarak gider, yeni kalem açmaz.
  - `cc/gorev-2026-07-30-6.md` — KAPSAM DARALTILDI. Salih sorusu: "30-6'nın amacı ne?" Dürüst cevap: üç testten ikisi (Plan sürdürme · /compact) hiçbir kararı beklemeyen muhasebe borcuydu — kapasite boş diye yazılmıştı; frenin küçük ölçekli ihlali. Emir tek gerçek soruya indi (E8 — yazım-kilidinin konfigürasyonlar arası kapsam doğrulaması; masa madde 26 + K-010/A2 kanıt kapısı); ikisi YOLCU İŞ olarak devredildi.
  - **Ders (hasat adayı):** boş kapasite kendi başına iş üretme gerekçesi değil — "defterde borç yazıyor" ile "bir karar bunu bekliyor" ayrı şeyler; ikincisi emir yazdırır, birincisi yolcu iş olur.
- SONUÇ (gözlenecek): [açık] — raporlar düşünce ingest; masa Salih'in seçtiği gün madde 7'den açılır.

## 2026-07-30 (5) — bağlam hijyeni İKİNCİ EKSEN adayı + denetçi emrinin genişletilmesi
- **Gözlem (Salih 07-30 akşam):** oturumda model düşümü yaşandı, oysa biyoloji-kökenli terim yoktu. Carvis hipotezi (kesin DEĞİL — model-değişim olayı içeriden görünmüyor): tetikleyici `gorev-2026-07-30-6`'nın ilk dili. Meşru bir kapsam ölçümü, kilit-etkisizleştirme tarifi kipinde yazılmıştı (başlıkta ve adım cümlesinde). **Tetikleyici ifadeler bu deftere KOPYALANMADI** — kayıt meta düzeyde tutulur, yoksa hijyen kaydının kendisi tetiği sonraki oturumlara taşır (Salih emri 07-30 akşam).
- **Aday kural (Katman-1, İMZASIZ):** 07-13 bağlam hijyeni kararı bir TERİM listesi değil bir TETİK YÜZEYİ tespitidir; ikinci eksen = koruma-etkisizleştirme kipi. Nötrleştirme yöntemi aynı: fiilen yapılan işi tarif et ("kilit kapsam doğrulaması"), etkisizleştirme kipini kullanma. **Usul şartı (Salih emri):** hijyen kayıtları tetikleyici ifadeyi ALINTILAMAZ, yalnız sınıfını adlandırır. Masa gündemine aday olarak taşınacak; imza Salih.
- **Katman-2 icra (yapıldı):** `gorev-2026-07-30-6` nötr dille yeniden yazıldı — deney değişmedi, çerçeve düzeltildi (başlık "yazım-kilidi kapsam doğrulaması"; sonuç etiketi "her konfigürasyonda geçerli / koşullu").
- **`gorev-2026-07-30-5` GENİŞLETİLDİ (Salih yönlendirmesi: "en iyi denetçi nasıl inşa edilir"):** emir motor-merkezli olmaktan çıkıp tasarım araştırması oldu — Eksen 1 bağlam devri (kör ↔ bağlamlı denetçi, literatür: self-preference bias · reference-free judging · CoVe · ensemble judge; m.37 v2 somut vakası; kalıcılık; bizim hazırlık yükümüz) · Eksen 2 rol ve yetki (ne denetlenir · çıktı biçimi · salt-okur garanti · denetçiyi kim denetler) · Eksen 3 motor tablosu (kısa, öneri satırı YASAK — masa kararı).
- SONUÇ (gözlenecek): [açık] — 30-5 raporu madde 7+28'in altına iner; hijyen ikinci ekseni masada imzalanırsa KILAVUZ'a yazım kuralı olarak geçer.
- **Taşıma-önleme icrası (Salih emri 07-30 akşam: "tetikleyici sonraki oturumlara taşınmasın"):** tetikleyici ifadeler kanondan temizlendi — senaryo-defteri 07-30 (4)/(5) blokları · `gorev-2026-07-30-6` revizyon notu · `build-tartisma-notlari` 07-30 bloğu · `vardiya-teslim-2026-07-30-anasira` hasat satırı. Yöntem: alıntı yok, sınıf adı var. Kalan eski izler (arşiv/okuma-defteri/gorev-22-1) taranmadı — pointer katmanında, her oturum okunmuyor; masa hijyen kalemi imzalanırsa tam süpürme o zaman koşulur.

## 2026-07-30 (6) — 30-5/30-6 ingest damgaları (Katman-2, veto açık)
- **30-5 (denetçi tasarımı) ana-sıra hakemliği: KABUL, yüksek değerli.** Taşıyıcı hamle emrin ikilemini kırmak: (A) kör ↔ (B) bağlamlı ikilisi ÜÇ nesneyi tek düğmeye bağlıyordu ⇒ ① ölçüt+ham veri+kod (iyileştirir, büyük) · ② akıl-yürütme zinciri (iki yönlü, denetçi gücüne bağlı) · ③ hüküm+kimlik+çerçeve (yalnız bozar). Ayırınca ödünleşim KAYBOLUYOR: ① açık · ③ kapalı · ② denetim nesnesi olarak. **Carvis şerhi:** emrin kurduğu gerilim ("kanonu verirsek çerçeve körlüğü") doğruydu ama ekseni yanlıştı — çerçeve ③'ten geliyor, ①'den değil. Bu, emri yazan tarafın (Carvis) hatasıdır, kayda geçer.
- **Sayısal çekirdek (niteleyicileriyle):** referanssız yargıç aşırı cömert — hüküm ters çevirme %85'e varıyor, çevirmelerin %91-100'ü "yanlışı doğru saymıştım"; insan uyumu referanssız 0,33-0,74 ↔ referanslı 0,85-0,96 · zincir verilince aşırı-red 2 kat (5,6→10,0 · 10,0→18,2) · dalkavukluk %58,19, gerileyici %14,66, kalıcılık %78,5 ⇒ **protokol: tek atışlık, itirazsız** · panel: 9 yargıç ≈ 2,18 etkin bağımsız oy, aynı-aile 0,437 ↔ çapraz-aile 0,389, en korelasyonlu 3 çift ÇAPRAZ aileden. **Niteleyici (taşınmadan alıntılanamaz): tüm ölçümler etiket-sınıflandırma/tercih görevinde; uzun-metin argüman denetiminde ölçüm literatürde YOK (§7 md.8).**
- **Masaya etki:** madde 28 yeniden kuruldu (4 bulgu + salt-okurluk ayrı-dizinle motordan bağımsız çözülüyor + tek-atışlık protokol) · madde 7'ye ÜÇÜNCÜ YOL (ucuz kalibrasyon koşumu: v1'in 3 kırık + 4 sağlam hükmü hazır sınama seti ⇒ bütçe kararı ölçümden önce alınmak zorunda değil) + muafiyetin fedası küçüldü.
- **30-6 (kilit kapsamı): KİLİT KOŞULLU ÇIKTI — kanon ifadesi yanlışlandı.** İki bağımsız yol: ayar-kaynağı bayrağı (deny + Bash kancası BİRLİKTE düşüyor — aynı dosyaya bağlı, ayrı sigorta değil) · proje kökü dışından açılış. Test dosyası iki kez de anında silindi, doğrulandı. **m.41'in "yapısal kilitli" ifadesi düzeltilmeli:** yapısal olan settings.json'un varlığı değil YÜKLENMESİ — yükleme cwd/bayrak/env'e bağlı çalışma-zamanı kararı. Yan bulgu: motor deny'i `Write` aracına da uyguluyor (kategori eşleşmesi, literal tool-adı değil).
- **K-010/A2 KAPISINA DOĞRUDAN ETKİ (Carvis tespiti, masaya):** A2 şartı "PreToolUse kilit canlı PASS" idi — ölçüm PASS vermedi, KOŞULLU verdi. Kapı=kanıt ilkesince A2 bu haliyle kapanamaz; ya kilit koşulsuzlaştırılır (sunucu-taraf katman) ya A2 metni "varsayılan açılışta geçerli" diye daraltılır. İkisi de Katman-1.
- **Yolcu iş SONUCU:** Plan sürdürme TAMAMLANDI — SendMessage ile aynı ajan-id'ye takip mesajı bağlamı kelimesi kelimesine korudu (~3 sn ilk yanıt, ~11 sn sürdürme) ⇒ **K14'ün son açık ucu KAPANDI.** /compact tetiklenmedi, uydurma sonuç üretilmedi (m.39). Worktree ekseni maliyet nedeniyle atlandı — devredildi.
- **Rapor-içi hata yakalama (kayda değer):** 30-5, birincil kaynağında (L-CHAIN Tablo 1) kopyala-yapıştır arızası buldu — iki satırın rakamları birebir aynı; o rakamları KULLANMADI. Akademik yeniden-doğrulama borcunun (B-1) canlı örneği; yöntem dersi: tablolarda tekrar eden satırlar taranır.
- **Bilgi borçları (karar öncesi teyit):** Gemini CLI'ın 18 Haziran 2026 durdurma bildirimi birincil kaynaktan doğrulanamadı [K] · Codex sandbox satırları [K] (birincil doküman 404/boş) · Türkçe token/karakter oranı ölçülmedi ⇒ 30-5'in token rakamları BANT halinde okunur, tek sayı olarak alıntılanmaz.
- **m.43 skill eşiği:** anahtarsız erişim yolu üçüncü kez çalıştı (KG-M37-9 artık iki değil ÜÇ gözlem) — tetik Salih'te.
- SONUÇ (gözlenecek): [açık] — masa madde 7/26/28 bu girdilerle açılır; kalibrasyon koşumu (v1 sınama seti) masa öncesi de koşulabilir, bütçe kararı gerektirmiyor.
- **YENİ KOŞUM AÇILDI — üretim freni Salih emriyle bu kalemde delindi (07-30 gece):** `cc/gorev-2026-07-30-7.md` = **karar-yönlendirme filtre katmanı** (hangi karar Salih'e, hangisi otomasyona). Salih gerekçesi: "bir noktada her kararı benim vermemem gerekecek." Bu masa-hizmetli DEĞİL, yeni konu — fren kararının m.16 kapsamında Salih tarafından delinmesi, kayda geçer.
- **Emrin tasarımı (Carvis, Katman-2):** 6 bölüm — eksenler (geri-alınabilirlik · risk üçlüsü · etki yarıçapı · değer tercihi · kalibrasyon · emsal · sıklık×maliyet, her biri "oyunlanabilir mi" testiyle) · mimari (politika-olarak-kod ↔ model yargısı ↔ melez; eskalasyon protokolü; **post-hoc geri çağırma**; toplu onay; sessiz kalma hakkı) · **dinamik eşik** (sicil-temelli genişleme, asimetrik daralma, sınıf kayması = en olası sessiz arıza, yanlış-yükseltme ↔ yanlış-indirme asimetrisi) · **§D bizim karar külliyatımızla somutlaştırma** (senaryo-defteri + cc/defter + teslim raporları = etiketli karar verisi; geriye dönük "hangisi Salih'e gitmemeliydi / gitmeliydi ama gitmedi") · emsaller ve ölçülmüş tuzaklar (otomasyon yanlılığı · uyarı yorgunluğu · onay tiyatrosu · beceri erozyonu · **son-insan sendromu**) · üç kurulabilir tasarım (en az biri BUGÜN kurulabilir).
- **Çıkar çakışması şartı emre YAZILDI:** filtre Carvis'in yetkisini genişleten bir mekanizmadır; emri de Carvis yazdı. Rapordan istenen: çakışmayı açıkça işaretlemesi ∧ en az bir tasarımın Carvis yetkisini GENİŞLETMEDEN (yalnız kayıt/görünürlük artırarak) kurulması. Gerekçe: m.6 kör-onay yasağının kendi tasarımımıza uygulanması.
- SONUÇ (gözlenecek): [açık] — rapor düşünce ingest; filtre kararları K-009/K-010 kapılarıyla kesişiyor, imza Salih.
- **İKİNCİ YENİ KOŞUM (Salih emri 07-30 gece):** `cc/gorev-2026-07-30-8.md` = **Docker Desktop — nedir, entegre edilir mi, nasıl.** Carvis çerçevelemesi: soru genel geldi ama üç açık kalemin üstüne düşüyor — (a) 30-6'nın koşullu kilidi (konteyner farklı KATMANDA sınır: "ayar yasakladığı için yazamıyor" ↔ "dosya orada yok") ⇒ K-010/A2 kapısına aday cevap · (b) 30-5'in "kör paket = ayrı dizin" önerisinin sert hali · (c) K-002 tekrarlanabilir ortam + K-011.
- **Emre yazılan frenler:** bu koşumda Docker KURULMAZ (kurulum = m.31 Katman-1, geri-alınması pahalı sistem değişikliği) · izolasyonun GERÇEK sınırı zorunlu bölüm, tehdit modeli açıkça "kendi ajanımızın kazara yazımı", saldırgan değil — "yapısal" kelimesinin hak edilip edilmediği sorgulanacak · **S5 = kurmama seçeneği ciddiye alınarak, en güçlü haliyle yazılacak** (worktree izolasyonu · ayrı dizin · WSL2 doğrudan zaten neyi karşılıyor) · lisans birincil kaynaktan doğrulanacak · "Docker iyidir" cümlesi rapora giremez, her iddia ya rakama ya bizim kartımıza bağlanır.
- **Carvis şerhi (m.6):** Docker bir bağımlılık ekler ve JARVIS'in mevcut bağımlılık sayısı düşük (git · CC · Cowork · PowerShell). m.42 katı-başlangıç ilkesiyle gerilim var: erken karmaşıklık. Bu yüzden sentez üç yol istiyor ve en az biri 1 saatte geri-alınabilir pilot olmak zorunda.
- SONUÇ (gözlenecek): [açık] — rapor düşünce ingest; kurulum kararı Salih'in.
- **ÜÇÜNCÜ YENİ KOŞUM (Salih emri 07-30 gece):** `cc/gorev-2026-07-30-9.md` = **yagizkaterli skill ailesi** (5 skill: foundation · frictionless · human-steps · perfect-form · idea-boost) — uyarlama tasarımı + feedback. Salih emri: "kendimize göre uyarlayıp kullanalım + feedback versin."
- **Emre yazılan frenler:** **V25 altın kuralı PAZARLIKSIZ** (kurulum yok, desen alınır, kendimiz yazarız; dış metin kopyalanmaz) · bu koşumda SKILL DOSYASI ÜRETİLMEZ (üretim K-016 ayrı koşumu) · **örtüşme taraması uyarlamadan ÖNCE** (bizde zaten var mı · kanonla çelişiyor mu · ajansız ölçeğimize uyuyor mu) · `idea-boost` 07-18'de incelendi ⇒ tekrarlanmaz, o notun hükümleri girdi · **"beşi de faydalı" sonucu şüpheli** — eleme bu koşumun işi.
- **Carvis'in işaret ettiği aday gerilimler (doğrula ya da çürüt, m.16 formatında):** human-steps "her insan-eylemini yüzeye çıkar" ↔ **m.4 soru eşiği** · perfect-form "tükenene kadar çalış" ↔ bağlam-şişmesi/kapanış disiplini (V11) · frictionless "insanın adım sayısı maliyet fonksiyonudur" ↔ **m.31 Katman-1 zorunlu-sorma listesi** (bazı sorular sayı azaltmak için atlanamaz) · foundation "altı yasa" ↔ 40 maddelik tüzük (madde madde eşleme istendi; eşleşmeyen yasa = gerçek katkı).
- **Kesişim uyarısı:** frictionless + human-steps, 30-7'nin (karar-yönlendirme filtresi) soru ailesinden — emir kesişimi §5'te AYRI işaretlemeyi ve filtre kararlarını 30-7'ye/masaya bırakmayı şart koşuyor; iki koşum birbirinin yerine geçmez.
- SONUÇ (gözlenecek): [açık] — rapor düşünce ingest; hangi skill'lerin ÜRETİLECEĞİ kararı Salih'in (K-016 kapsamı).
- **DÖRDÜNCÜ YENİ KOŞUM (Salih emri 07-30 gece):** `cc/gorev-2026-07-30-10.md` = **icra katmanı** — hangi tekrarlar koda taşınır (token yerine hazır kod) + hangi dille (Go/Rust sorusu). 
- **Carvis SIRA DÜZELTMESİ (m.6, emri değiştirmez):** iki soru var ve ikincisi birincinin ön-koşulu — dil seçimi, koda taşınacak iş yükü tanımlanmadan cevaplanamaz. Emir §1-§3'te "ne taşınır", §4'te dil; dile erken atlayan rapor işini yapmamış sayılır.
- **Carvis İKİNCİ ŞERHİ (m.6):** "Go mu Rust mı" aday kümesini daraltıyor olabilir — bugün çalışan kodumuz shell+PowerShell+Python, Claude Agent SDK Python/TS'te yaşıyor. Emir Go ∧ Rust ∧ Python ∧ TypeScript ∧ PowerShell ∧ **"karışıma devam"** seçeneklerini AYNI ölçütlerle tartmayı şart koşuyor; Salih'in sorduğu iki dil ayrıcalıklı muamele görmez.
- **Ölçülen başlangıç noktası:** JARVIS'te bugün çalışan kod **126 satır / 4 dosya / 3 dil** (pretool-core-tel.sh 20 · session-start.sh 10 · gece-senkron.ps1 22 · verify-push.py 74) ⇒ soru "sıfırdan hangi dil" değil, "bu 126 satır nereye evrilir".
- **Emrin çekirdek ayrımı:** (a) tam deterministik ⇒ koda taşınır · (b) yargı gerektiren ama şablonlanabilir ⇒ araçla desteklenir, model işi kalır · (c) saf yargı ⇒ dokunulmaz. Yanlış sınıflandırma raporun yapabileceği en pahalı hata.
- **Token iddiası HİPOTEZ olarak işaretlendi:** net kazanç = tasarruf × koşum_sayısı − (yazım + bakım × zaman); **başabaş noktası** istendi (hangi sıklığın altında kod yazmak ZARARDIR). Ters maliyetler emre yazıldı: bakım · **bayatlama** (kod kanonla senkron kalmazsa sessizce yanlış şey zorlar — okuma-defteri %23 bayat referans bulgusu) · **görünürlük bedeli** (model hatası görünür, kod hatası sessiz).
- **Zemin:** okuma-defteri md.3 kod-entegrasyonu sentezi — "kod metnin yerine geçmez, DOĞRULANAMAYAN kısmını devralır" + masa madde 27 (zorlanabilirlik etiketi) + 30-6'nın koşullu kilidi (icra katmanının ilk müşterisi olabilir).
- SONUÇ (gözlenecek): [açık] — rapor düşünce ingest; kod yazımı ayrı koşum, karar Salih'in.
- **30-10 GENİŞLETİLDİ — loop dönüşümü (Salih ek emri: "bu son görevi bir loop'a nasıl dönüştürebiliriz"):** ayrı koşum AÇILMADI, §5b olarak eklendi. Gerekçe: loop tasarımı da neyin kodlanacağını bilmeden yapılamaz — ayrı emir, az önce düzeltilen sıra hatasının tekrarı olurdu.
- **Carvis çerçevelemesi:** loop kanonda YARI kurulu — **m.43 skill eşiği zaten bir tekrar sayacıdır** (üçüncü tekrar ⇒ aday; KG-M37-9 şu an tam bu durumda). Fark: sayaç bugün Carvis'in kafasında, tetik Salih'te. Loop = sayacın ve eşiğin dosyaya/koda devri; sıfırdan icat değil, mevcut mekanizmanın genellemesi.
- **ÇELİŞKİ KAPISI (m.16) emre YAZILDI:** halka 1-2-5-6 (gözlem · eşik · ölçüm · bayatlama-geri alma) sabit-promptlu ∧ deterministik ∧ salt-okur ⇒ m.30 tanımıyla **OTOMASYON**, K-009 kapsamı, bugün açılabilir. Halka 3 (yazım) = sistemin neyi kodlayacağını KENDİSİNİN seçmesi ⇒ prompt ∧ iş-seçimi devri ⇒ **CANLI AJAN**, K-010 kapsamı, BUGÜN BLOKE (A2 kapısı 30-6'nın koşullu-kilit bulgusuyla daha da uzaklaştı). İstenen tasarım: **halka 3 insanda kalırken dönen loop** — sistem sayar, eşiği aşanı kuyruğa koyar, tahmini kazançla Salih'e sunar; kod Salih tetiğiyle yazılır; loop sonucu ölçer ve eşiğini günceller.
- **Emre gömülen ek sorular:** kaç halka otomatikleşirse "loop" olur (yoksa hatırlatıcı mı) · durma koşulu (loop-eng Faz 2-4 dersi; m.37'nin "tek promptta çözülür olgunluğunda optimizasyon durur" kuralının kodifikasyon karşılığı) · **kendi kendini besleme riski** (loop iş bulamayınca iş İCAT eder mi — canlı örnek: 30-6'nın ilk taslağındaki gereksiz testler, senaryo-defteri 07-30 (4) dersi; fren gömülmeli) · 30-7 kesişimi (halka 2 eşiği ile karar-yönlendirme filtresi eşiği AYNI soru — çelişirse masaya) · m.35 bağlantısı (ölçüm şeması beklenti vektörüyle uyumlu kurulmalı).
- **Teslim şartı:** her halka "bugün açılabilir / K-009 ön-koşullu / K-010 ön-koşullu" etiketiyle verilir; etiketsiz halka kabul edilmez.
