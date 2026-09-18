# KILAVUZ arşivi — damıtma 2026-08-29 (Karar 74 M-3a; m.8 silme yok)

*Kaynak: KILAVUZ.md damıtma-öncesi hali. §1 Cowork/Windows dönemi paralel-seans tarifi (süpersede: Karar 71 üç-katman düzeni + `wiki/paralel-oturum-protokolu.md`; günaydın tetikleri 08-15 emekli, C:\JARVIS 08-12 terk) · §2 boyut-izleme gerekçe/tarihçe kuyruğu · §3 eski push satırı.*

## §1 — Paralel seans protokolü (eski model)

- **Model (m.36 2. rev hizası):** JARVIS projesi İKİ paralel Cowork chat'inde yürür — Jarvis'in iki yarısı: **(1) Prototip seansı** (K-015 şeridi — loop-eng, K-009, K-010, ajan-defter; ÖNCELİK BU) ve **(2) Ölçüm-bankı seansı** (K-002 PortRisk — hasat/etiketleme verisi üretir; çatışmada prototip kazanır). Açılışta hangi hattaysan söylersin: "günaydın, prototip" (ya da sadece "günaydın" — varsayılan bu hat) / "günaydın, PortRisk" — günaydın taraması kapsülden o şeridin durumunu alır. Belirsizse Carvis sorar (tek soru).
- **Prototip seansı kurulumu:** her zamanki gibi `C:\JARVIS` mount'u (Homebase eklenebilir).
- **Ölçüm-bankı (PortRisk) seansı kurulumu:** oturum `C:\JARVIS` mount'uyla açılır + yanına `C:\Users\sasah\dev\portrisk` klasörü eklenir. İç-mutfak dosyası (CLAUDE.md, seans kuralı, teslim raporu) public portrisk reposuna ASLA yazılmaz — bağlam hep JARVIS'ten okunur, portrisk'e yalnız proje kodu/testi gider.
- **Senkron kuralı (çakışma önleme):** her seans kapanışta (a) kendi teslim raporunu `raporlar/`a AYRI dosya yazar (`YYYY-MM-DD-<hat>-teslim.md`), (b) kapsülde YALNIZ kendi şeridinin satırını günceller — diğer şeridin satırına dokunulmaz, (c) kendi commit'lerini atar/push'lar. İki oturum aynı anda açıksa push öncesi pull zorunlu.
- Misyon notu: senkron şimdilik elle yürür — K-009 otomasyonu açılınca bu disiplinin otomatikleşmesi beklenir (geçici kabul, Salih 07-12).

## §3 — Eski oturum satırları (süpersede 08-29)

- **Kapanış** ("end of day" / "bitiriyorum" / "uyucam"): seans teslim + kapsül güncellenir + push atılır. Carvis kapanışı kendi de önerebilir (V11 — fiilen yerleşik davranış).
- Push'lar Carvis'ten otomatik gider (`.secrets/github-pat`); her karar ayrı commit, [damıtma]/[icra] etiketli (V5).

## §2 — Boyut-izleme satırının gerekçe/tarihçe kuyruğu (tam metin)

Her oturum açılışında okunan dosyalar sabit boyut-bütçeli yaşar; **aşım hata değil TETİKTİR** — aşan dosya ilk boş seansta Salih-imzalı planla damıtılır (silme yok: tam metin arşive, sıcakta özüt+pointer; m.8/m.34). Bütçeler: kapsül 8KB **ve ≤40 satır** (SessionStart hook `1,40p` sert-kapısı — aşan kuyruk CC'de sessizce düşer) · pano 12KB · fikir-kutusu 20KB · senaryo-defteri 48KB · CLAUDE.md 8KB · KILAVUZ 16KB. Kapanışta kapanan Carvis tabloya tek bakış atar; aşan varsa teslim raporuna "boyut-tetiği: <dosya>" düşer. **Revizyon tetiği (Salih şerhi 07-22):** context-ekonomisi (pencere/fiyat) ya da bütçe anlamlı değişirse tablo yeniden türetilir; her iki damıtma turunda bir kalibrasyon. Gerekçe + türetme: `kuyruk/k019-taslak-boyut-izleme.md`. **Araştırma güncellemesi (Salih imzası 07-23; `cc/rapor/2026-07/rapor-2026-07-23-1.md`):** birim KB kalır AMA 20KB+ dosyalar token'la DA izlenir (Türkçe fertilite: KB anti-muhafazakâr); 8/12/20/8/16 ONAYLANDI · 48KB FLAG (damıtma seansında token-bazlı yeniden bütçe/bölme) · ×1,4 onaylı (≈%70 emsali). **Yeni eksen — KONUM:** her-tur-okunan dosyalar bağlam tepesinde (lost-in-middle ~35 puan).

## §4 — Skill-yazım standardı (K-013 dönemi, tam metin; eval kuralı canlı bölüme taşındı)

## Skill-yazım standardı (deneysel damga m.29; kaynak: resmi skill-creator + best-practices — K-013 raporu; Salih onayı 07-12)
- SKILL.md <500 satır — tetiklenince gövde bağlama komple yüklenir, bu ~5K token tavanı demek (resmi tavsiye; kullanım verimizle kalibre edilir).
- Açıklama alanı = "ne yapar + ne zaman kullanılır" — tetikleme isabetini bu belirler.
- Her skill'e **Gotchas bölümü**: skill-başına biriken hata/tuzak listesi (ingest defterinin skill karşılığı).
- Yan-etkili işler (commit, push, publish) `disable-model-invocation` ile yalnız elle tetiklenir — model kendi kendine çalıştıramaz.
- Deterministik iş skill'e script olarak gömülür (model kodu her seferinde yeniden türetmesin).
- **Eval kuralı (Salih onayı 07-12; REVİZYON Salih imzası 07-23 — kaynak `cc/rapor/2026-07/rapor-2026-07-23-1.md`):** her JARVIS skill'i eval setiyle doğar. Küçük-N eval = **SMOKE/regresyon-kanaryası, sertifika DEĞİL** — çıplak "%100 geçti" raporu YASAK; sonuç aralığıyla (Clopper-Pearson: 6/6→[%54,%100]) ya da "smoke-only" ibaresiyle verilir. Yeni setlerde: negatif ~10 (pariteye yaklaş — 3 negatif yanlış-pozitifi bağlamaz) + her vaka ≥3× koşum (non-determinizm ilacı; vaka eklemekten ucuz). 20-sorgu description-eval skill-creator protokolüne TAM hizalı: 8-10 should + 8-10 should-not · her sorgu 3× · 60/40 held-out · ≤5 iterasyon. Mevcut skill'lere geriye dönük eval soğuk kuyrukta. *(md.22 pozitif karşılığı fiilen bu maddede tanımlı — aralıkla ya da smoke-only ibaresiyle ver; imza kaydı 08-20 KB-28.)*
- Not: progressive disclosure ilkesi = m.20 pointer sistemiyle aynı kök (bağımsız doğrulama, K-013).


## §5 — Sıkıştırılan satırların tam metinleri (Karar 71 · gürültü listesi)

(bkz. git geçmişi cf4c7c5 sonrası hâli; Karar 71 tam metni defterde de yaşar)
