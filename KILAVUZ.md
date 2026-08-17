# KILAVUZ.md — JARVIS Kullanım Kılavuzu (v1)

> **Açıklama notu:** K-012 build adım 2 çıktısı (2026-07-12; m.26: anlama-kapısı yerine kılavuz — Salih buradan okur, takıldığı yerde Carvis izah eder). Format deneysel-damgalı başlar (m.29), kullanım verisiyle kalibre edilir. Kural kaynağı her zaman tüzük; burası "nasıl kullanılır" yüzeyidir.

## Oturum nasıl işler
- **"seans başı"** (eski selamlama tetiği emekli 08-15, `core/baglam-anahtar-kaydi.md`) → seans açılışı: kapsül + pano okunur, kısa teslim özeti + tek net sıradaki iş sunulur.
- İş sırasında ne söylersen görev olarak devralınır (m.25); küçük iş direkt yapılır, proje ölçekli işe kart/ajan — ölçek-tercihi Carvis'te.
- **Kapanış** ("end of day" / "bitiriyorum" / "uyucam"): seans teslim + kapsül güncellenir + push atılır. Carvis kapanışı kendi de önerebilir (V11 — fiilen yerleşik davranış).
- **Bağlam-şişme çağrısı (Salih emri 07-19):** Carvis, oturum bağlamının şiştiğini ve kalite riskini gördüğünde bunu KENDİLİĞİNDEN belirtir; seans kapanışı + yeni seans önerir (kapanış = teslim raporu + kapsül tazeleme; yeni seans kapsülden devralır — m.27 hattı).
- Push'lar Carvis'ten otomatik gider (`.secrets/github-pat`); her karar ayrı commit, [damıtma]/[icra] etiketli (V5).
- **Ağır araç yükleme usulü (Salih imzası 08-17 masa KB-12; ölçüm `raporlar/2026-08-03-model-dusumu-olcum.md`):** çoklu MCP/ToolSearch yüklemesi oturum BAŞINDA ya da AYRI oturumda; uzun oturumun geç evresinde YAPILMAZ (prompt-cache kırılması ~152K token → kota → düşüm).

## Paralel seans protokolü (Salih kararı 2026-07-12 sabah; m.36 revizyonunun operasyonel devamı — deneysel damga m.29)
- **Model (m.36 2. rev hizası):** JARVIS projesi İKİ paralel Cowork chat'inde yürür — Jarvis'in iki yarısı: **(1) Prototip seansı** (K-015 şeridi — loop-eng, K-009, K-010, ajan-defter; ÖNCELİK BU) ve **(2) Ölçüm-bankı seansı** (K-002 PortRisk — hasat/etiketleme verisi üretir; çatışmada prototip kazanır). Açılışta hangi hattaysan söylersin: "günaydın, prototip" (ya da sadece "günaydın" — varsayılan bu hat) / "günaydın, PortRisk" — günaydın taraması kapsülden o şeridin durumunu alır. Belirsizse Carvis sorar (tek soru).
- **Prototip seansı kurulumu:** her zamanki gibi `C:\JARVIS` mount'u (Homebase eklenebilir).
- **Ölçüm-bankı (PortRisk) seansı kurulumu:** oturum `C:\JARVIS` mount'uyla açılır + yanına `C:\Users\sasah\dev\portrisk` klasörü eklenir. İç-mutfak dosyası (CLAUDE.md, seans kuralı, teslim raporu) public portrisk reposuna ASLA yazılmaz — bağlam hep JARVIS'ten okunur, portrisk'e yalnız proje kodu/testi gider.
- **Senkron kuralı (çakışma önleme):** her seans kapanışta (a) kendi teslim raporunu `raporlar/`a AYRI dosya yazar (`YYYY-MM-DD-<hat>-teslim.md`), (b) kapsülde YALNIZ kendi şeridinin satırını günceller — diğer şeridin satırına dokunulmaz, (c) kendi commit'lerini atar/push'lar. İki oturum aynı anda açıksa push öncesi pull zorunlu.
- **KURAL (Salih imzası 08-17 masa KB-08/09/10):** çoklu oturumun 4 kuralı `wiki/paralel-oturum-protokolu.md` — canlı-oturum kapısı · koşum-önü manifest kapısı · paylaşılan kaynak/motor freni · **`git add -A` yasak, `git add <yol>`** (H4).
- Misyon notu: senkron şimdilik elle yürür — K-009 otomasyonu açılınca bu disiplinin otomatikleşmesi beklenir (geçici kabul, Salih 07-12).

## Üçlü sohbet düzeni — CC köprüsü (Salih kararı 07-12; m.17'nin ilk uygulaması; deneysel m.29)
*ARŞİVE İNDİ (damıtma 08-17; Cowork/geçiş dönemi tarifi) → `kuyruk/arsiv/KILAVUZ-arsiv-2026-08-17.md:5`.*

## Emir ve soru dili
- Ne dersen emirdir; önceki kararla çelişki varsa önce çelişki raporu gelir (m.16).
- **Çıktı-dili soru formatı + framing koruması (V6):** Carvis sana soru sorarken seçenekleri somut SONUÇ örnekleriyle sunar ("A seçilirse şu olur") ve soru cümlesi yönlendirme içermez — seçenekler yansız yazılır; Carvis kendi önerisini ayrıca, gerekçesiyle işaretler (m.6).
- **Kapasite cevabı üç halden biri (#9):** "yaparım" (direkt yapılır) · "yapamam" (neden + ne gerekirdi) · "proje gerekir" (kart açılır, kaba token×zaman tahmini verilir). Belirsiz "bakarız" cevabı yasak.

## Kart ve kutu kuralları
- **DONE kuralı (Salih onayı 07-12):** yazılabilir, doğrulanabilir DONE tanımı olmayan kart açılmaz. İyi örnek: "pytest yeşil + push". Kötü örnek: "İngilizceyi geliştir". Loop dönemi karşılığı: durma koşulu yazılamayan loop kurulmaz.
- **Çürüdü-işareti (Salih onayı 07-12):** fikir kutusunda 30 gün işlenmeyen madde "BAYAT" damgalanır; düşme YALNIZ Salih onayıyla (m.8 otomatik-silme yasağı korunur).
- **Gürültü listesi (deneysel damga; Salih düzeltir):** kutuya DOSYALANMAZ → model/sürüm duyuruları (işimizi değiştiren somut yetenek yoksa) · kaynaksız tek-tweet prompt numaraları · "X aracı çıkmış" haber gürültüsü (yazılı tetiğimize dokunmuyorsa) · başkasının kurulumunun bütünüyle kopyası (V25 altın kuralı: desen alınır, kurulum alınmaz). **İSTİSNA (Salih, 07-12):** "araştır bakayım" emri listeyi ezer — istek üzerine her şey araştırılır; liste yalnız kutuya-kayıt filtresidir.

## Tasarım ilkeleri
- **Sürtünmesizlik (#18):** sık kullanılan her akışın çağrısı kolay olur ve çapası kurulur; yeni mekanizma tasarlarken ilk soru "bunu çağırmak kaç saniye sürer?"
- **Bayat-kapsül riski (V4):** kapsül kapanışta güncellenmezse sonraki seans yanlış yere çapalar — yanlış kapsül, boş kapsülden kötüdür; kapanış disiplini bu yüzden atlanmaz.
- **Metafor haritası (V12):** sistem terimleri tek metafor ailesinden gelir (şirket: seans, pano, tüzük, teslim raporu); yeni terim aile içinde türetilir, tanımı sözlüğe işlenir (sözlük v1 DONDU — ekleme yalnız Salih talimatıyla, m.3).
- **Araç-seçim ölçütü — yıldız yasağı (Salih imzası 08-01 masa-2 md.33):** GitHub yıldız sayısı araç seçiminde ölçüt OLAMAZ; pozitif karşılığı: adaylar indirme-sırası + son-sürüm-tarihi + bakımcı-sayısı üçlüsüyle tablolanır. Reddedilen araç gerekçesiyle "şu an alınmaz" listesine işlenir (md.34) — altı ay sonra aynı soru gelince cevap hazır.

## Skill-yazım standardı (deneysel damga m.29; kaynak: resmi skill-creator + best-practices — K-013 raporu; Salih onayı 07-12)
- SKILL.md <500 satır — tetiklenince gövde bağlama komple yüklenir, bu ~5K token tavanı demek (resmi tavsiye; kullanım verimizle kalibre edilir).
- Açıklama alanı = "ne yapar + ne zaman kullanılır" — tetikleme isabetini bu belirler.
- Her skill'e **Gotchas bölümü**: skill-başına biriken hata/tuzak listesi (ingest defterinin skill karşılığı).
- Yan-etkili işler (commit, push, publish) `disable-model-invocation` ile yalnız elle tetiklenir — model kendi kendine çalıştıramaz.
- Deterministik iş skill'e script olarak gömülür (model kodu her seferinde yeniden türetmesin).
- **Eval kuralı (Salih onayı 07-12; REVİZYON Salih imzası 07-23 — kaynak `cc/rapor-2026-07-23-1.md`):** her JARVIS skill'i eval setiyle doğar. Küçük-N eval = **SMOKE/regresyon-kanaryası, sertifika DEĞİL** — çıplak "%100 geçti" raporu YASAK; sonuç aralığıyla (Clopper-Pearson: 6/6→[%54,%100]) ya da "smoke-only" ibaresiyle verilir. Yeni setlerde: negatif ~10 (pariteye yaklaş — 3 negatif yanlış-pozitifi bağlamaz) + her vaka ≥3× koşum (non-determinizm ilacı; vaka eklemekten ucuz). 20-sorgu description-eval skill-creator protokolüne TAM hizalı: 8-10 should + 8-10 should-not · her sorgu 3× · 60/40 held-out · ≤5 iterasyon. Mevcut skill'lere geriye dönük eval soğuk kuyrukta.
- Not: progressive disclosure ilkesi = m.20 pointer sistemiyle aynı kök (bağımsız doğrulama, K-013).

## Boyut-izleme — sıcak-dosya bütçesi (İMZALI kural, Salih 07-22; rakamlar deneysel m.29)
Her oturum açılışında okunan dosyalar sabit boyut-bütçeli yaşar; **aşım hata değil TETİKTİR** — aşan dosya ilk boş seansta Salih-imzalı planla damıtılır (silme yok: tam metin arşive, sıcakta özüt+pointer; m.8/m.34). Bütçeler: kapsül 8KB **ve ≤40 satır** (SessionStart hook `1,40p` sert-kapısı — aşan kuyruk CC'de sessizce düşer) · pano 12KB · fikir-kutusu 20KB · senaryo-defteri 48KB · CLAUDE.md 8KB · KILAVUZ 16KB. Kapanışta kapanan Carvis tabloya tek bakış atar; aşan varsa teslim raporuna "boyut-tetiği: <dosya>" düşer. **Revizyon tetiği (Salih şerhi 07-22):** context-ekonomisi (pencere/fiyat) ya da bütçe anlamlı değişirse tablo yeniden türetilir; her iki damıtma turunda bir kalibrasyon. Gerekçe + türetme: `kuyruk/k019-taslak-boyut-izleme.md`. **Araştırma güncellemesi (Salih imzası 07-23; `cc/rapor-2026-07-23-1.md`):** birim KB kalır AMA 20KB+ dosyalar token'la DA izlenir (Türkçe fertilite: KB anti-muhafazakâr); 8/12/20/8/16 ONAYLANDI · 48KB FLAG (damıtma seansında token-bazlı yeniden bütçe/bölme) · ×1,4 onaylı (≈%70 emsali). **Yeni eksen — KONUM:** her-tur-okunan dosyalar bağlam tepesinde (lost-in-middle ~35 puan).

## Sayı-araştırma kapısı (Salih emri 07-23 — kural)
Sistem parametresi olacak her deneysel sayı (eşik, bütçe, sayaç, örneklem) CC araştırması koşulmuş-ve-okunmuş bağlamda seçilir (m.40'ın sayılara genişletilmesi). Araştırmasız mevcut sayılar GEÇİCİ damgayla yürürlükte; rapor gelince yeniden türetilir/onaylanır, fark deftere. Envanter: `raporlar/2026-07-23-deneysel-sayi-denetimi.md` · ilk tur: `cc/rapor-2026-07-23-1.md` (4 hüküm uygulandı). Kalite-proxy'ler (m.39) kapının konusu değil — onların yolu ölçüm.

## Öz-usage usul kuralı (Salih beyanı 08-01 sözlü → metinleşme Salih imzası 08-01 masa)
Salih'in kendi /usage, /context ve bağlam-doluluk yorumları YORUM statüsündedir, karar/ölçüm değil ("bağlam şişti" beyanı tek başına eşik tetiklemez — 08-01-2: doz-cevap yok). İterasyon yönünü üst model verir; Salih veto her zaman açık (m.31). Ölçüm hattı: Yol-1 bağlam-sayacı kurulunca beyanlar veriyle kalibre edilir.

## Durum görünürlüğü (m.18)
Her iş cevabının sonunda insan-yüzü tek satır (`▸ Şu an · Sıra · Açık`); "şu an ne yapıyoruz" dersen anlaşılır dilde detaylı durum raporu dosyası üretilir; makine-yüzü kapsül/pano/şablonlarda yaşar.

## Model-değişimli oturum protokolü (Salih imzası, 2026-07-13 — kural, deneysel değil)
Oturum ortasında model değişikliği yaşanırsa o oturumun orijinalliği bozulmuş sayılır: ingest'i kanon-yüzeyine değil şerhli klasöre yazılır — `model değişikliği ile orijinalliği bozulmuş olan chat/ingest-YYYY-MM-DD.md`. Buradaki içerik ŞERHLİ KOPYA statüsündedir; çelişki durumunda commit'li kanon (fikir kutusu / kuyruk / kapsül) kazanır. Şerhli içeriğin karar statüsü kazanması için ayık/temiz oturumda taranıp normal kanon yoluna işlenmesi gerekir. Gerekçe: bağlam hijyeni (07-13 vakasının standartlaşması).

## CC kanal modeli kararı (Salih, 2026-07-13 günaydın)
*ARŞİVE İNDİ (damıtma 08-17; Cowork/geçiş dönemi tarifi) → `kuyruk/arsiv/KILAVUZ-arsiv-2026-08-17.md:11`.*

## CC-geçiş düzeni — S2 hibrit-matris (Salih imzası 08-01 masa-2, K1-24-a; md.9 glide-path revizesi; bağlayıcı kayıt senaryo-defteri)
*ARŞİVE İNDİ (damıtma 08-17; Cowork/geçiş dönemi tarifi) → `kuyruk/arsiv/KILAVUZ-arsiv-2026-08-17.md:15`.*

## Mobil Köprü Protokolü (Dilim 2.1; Salih kararı 07-19 — rapor-1 Adım 0'ın icrası; deneysel m.29)
*ARŞİVE İNDİ (damıtma 08-17; Cowork/geçiş dönemi tarifi) → `kuyruk/arsiv/KILAVUZ-arsiv-2026-08-17.md:19`.*

## Skill Standardı (K-016 açılışı 07-19; el kitabı: `raporlar/2026-07-17-skill-nasil-olusturulur.md` — burası özet, çelişkide rapor + code.claude.com/docs kazanır)
- **Eval-önce akış:** önce ≥3 senaryoluk `evals/evals.json` + baseline (skill'siz koşum), SONRA minimal gövde; description ince-ayarı EN SON. Eval'siz yayın YOK.
- **Description:** 3. şahıs · NE + NE ZAMAN (gerçek kullanıcı ifadeleriyle) + NEGATİF tetik ("X'te kullanma") · ≤1024 karakter.
- **Gövde:** <500 satır · emir-kipli numaralı adım · tek sorumluluk · "Gotchas" bölümü en yüksek sinyal · detay `references/` (bir seviye derin).
- **Yan-etki freni (★):** kayıt/commit/deploy adımı AYRI `disable-model-invocation: true` skill'e — muhakeme skill'i blok ÜRETİR, dosyaya YAZMAZ (m.31/m.9 koda gömülü).
- **Kompozisyon:** skill'ler birbirini literal çağırmaz; bileşik iş = `context: fork` orkestratör + küçük çocuk skill'ler + sabit-format handoff + fail-loud.
- **Yayın-öncesi:** 20-sorgu description eval (10 tetiklemeli + 10 tetiklemesiz) · çok-modelde test · versiyon damgası (`0.x-deneysel-m29`).
- **Ev:** `.claude/skills/<ad>/SKILL.md` (repo, git'e commit — dağıtım gece-senkron/pull ile).

## Deneysel notlar — 2026-07-29 (m.29 damgalı; kaynak: cc/rapor-2026-07-29-3.md + P6 dersi)
- **D3 not-tutma refleksi:** değer üretilir üretilmez diske; teslim TASLAĞI seans ORTASINDA açılır, kapanış tamamlar. Gerekçe: 07-22 P6 dosya-kaybı vakası + kapsül/hook çıktısı compaction 2. aşamada özete erir.
- **D4 ana-sıra yüzeyi:** kanon edit'leri seans sonunda toplu; oturum-ortası CLAUDE.md yazımı yok (CC'de settings-deny ile yapısal; ana-sırada davranış kuralı).
- **İki-yüzey şerhi (A.11):** CC dokümanından türetilen bağlam-mekaniği kuralları Cowork'e OTOMATİK taşınmaz; Cowork tarafı [ARANAMADI]. Yeni mekanik kural yalnız CC-yüzeyi için yazılır, Cowork'e genelleme Salih masasına.
