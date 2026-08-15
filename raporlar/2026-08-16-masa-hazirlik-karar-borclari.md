# Karar-Borcu Masası — Hazırlık Dosyası (Salih için, İNSAN register)

*Carvis/Fable, 2026-08-16 seans-7 (kişisel hesap; Opus'ta zorla durdurulan 60c91bbb oturumundan devralındı — Opus 0 dosya yazmıştı, hiçbir çıktısı devralınmadı). Emir: Salih 08-16 00:46 "sistemdeki karar borçlarını Kun Chen'in kullandığı skill ile kapatacağız — 1 masa-öncesi hazırlık dosyası yaz; okuduktan sonra karar masası aşamalarına geçelim (bağlam datasını çeken; veri tabloları ve veri yapıları oluşturma sürecimize de yardımcı)" + 00:58 "devral, masa öncesi hazırlık dosyasını yaz". Format emsali: `raporlar/2026-08-03-masa-hazirlik-L8.md` (Kun-Chen L8 masası) + `raporlar/2026-08-02-masa-hazirlik-K2.md`. Deneysel m.29. Kural: **hiçbir kalemde hüküm verilmez — karar alanı BOŞ, "MASAYA" damgalı** (Salih 08-03 (c) maddesi).*

## 0. Koşum künyesi — emir doğrulaması (m.46a) + topraklama

| Alan | Değer | Sonuç |
|---|---|---|
| Emir kaynağı | Opus oturumu `60c91bbb` 00:46 (transkriptten okundu) + bu oturum 00:58 "devral" | **EŞLEŞTİ** |
| Fiilî HEAD SHA (yazım anı) | `90bb53d` (seans-5/6 kapanışları dahil) | — |
| Yazılabilir yüzey kontrolü | bu dosya · `veri/karar-borcu.jsonl` · `tools/karar-borcu-tablo.py` — koşum başında **YOKTU** | `-repl` GEREKMEDİ |
| Halüsinasyon derecesi (halusinasyon-paketi §2) | H = 5 / eşik 7 (v3d v4 v5 v7b v9 v10 − v8) → **F1+F2 ZORUNLU, skill opsiyonel** | uygulandı |
| F1 kaynak-topraklama | her kalem `dosya:satır` pointer'lı; yükleyici 154/154 pointer'ı diskte doğruladı (kırık 0) | **PASS** |
| F2 destek-kontrolü | 154 kaynak satırının metni döküldü ve elle okundu (Carvis); iddia↔satır uyumsuzluğu 0, 2 nüans nota işlendi (KB-24 K2-d "EKLE-birleşik", KB-30 Katman-2 çerçevesi) | **PASS** |
| Tarama maliyeti | 3 Explore işçisi (Sonnet 5): 163k + 216k + 173k = **552k token** (kısıntı hedefi ~250k'nın ~2,2×; kapsam-notu §G) · ana döngü Fable ölçülmedi [?] | m.39 damgalı |
| Ham → birleşik | 108 ham kalem (A36 · B45 · C27) → **37 Salih karar-borcu (KB) + 14 Carvis icra-borcu (İB) + 1 kapandı-paketi (KP, 6 kalem ayıklandı)** | tekilleştirme Carvis |

**Hüküm: DOĞRULAMA PASS.** Emir aynen uygulanıyor; Opus'un topladığı "malzeme" (format emsali, skill zinciri, sqlite şeması) yeniden okunarak sıfırdan kuruldu.

---

## (A) ÖN YAZI

**Bu dosya nedir:** Sistemde açık duran, senin hükmünü bekleyen karar kalemlerinin TEK envanteri — kapsül "Salih kararları" satırı, senaryo-defteri, iki masa gündemi, kuyruk/gelen dosyaları, fikir kutuları, 08-14/15/16 pipeline manifestleri ve raporları tarandı (kaynak listesi §G). Her kalem: kaynak satırı · seçenekler (varsa aynen) · Carvis önerisi (m.6: kibarca tavsiye + gerekçe, kör-onay yok) · bağımlılık · imzayla anında yürürlük mü · imza sonrası icra borcu. **Hiçbir kalemde hüküm yok.**

**İki yüzü var (çift muhasebe):** bu insan-yüzü dosya + `veri/karar-borcu.jsonl` (makine-yüzü; aynı 52 satır). Tablolar JSONL'den script'le türetildi — ikisi çelişemez. `tools/karar-borcu-tablo.py` JSONL'yi `veri/baglam.sqlite` içine `karar_borcu` + `karar_borcu_kaynak` tabloları olarak yükler (kaynak pointer → `kayit` tablosuna bağ), CSV görünümü `veri/gorunum/v_karar_borcu.csv`. Detay §F — "bağlam datasını çeken" ayak budur.

**Nasıl okunur (masa sırası önerisi — bağımlılık haritasıyla):**
1. **§C.0 Kapanış-teyidi (KB-33/34/35 + KB-37)** — 4 kalem, ~5 dk: bayat görünen satırlar; "konusuz → düş" ya da "hâlâ karar" teyidi. Listeyi küçültür.
2. **§C.1 S1 taze sistem-tasarımı (KB-01…07)** — 7 kalem: 08-16'da seçenek+öneriyle önüne konmuş kararlar (Hat-6 K1/K2/K3, stokastik atlası E2/E3/E4, bus-matrix satırı). En yüksek kaldıraç: world-model ölçüm işlerini, koşum-profilini ve üç kanon şerhini kilit açar. Çoğu **İMZA** yolu (metin hazır), üçü **MODEL-hazır** (m.37 üç-şık verili).
3. **§C.2 S3 oturum-disiplini (KB-08…13)** — 6 kalem: paralel-oturum vakaları 1/2/3 (4 günde 3 vaka, biri ~549k mükerrer koşum), staj-hasadı kuralları, senkron/çatal freni, D-0803-1, şerhli-5. Ucuz kurallar, yüksek tekrar-değeri.
4. **§C.3 S2 yön + S4 şerh (KB-14…22)** — 10 kalem: spec-kit yolu, agile tetiği, Windows, K-016 kapanışı, dal silimi, K-022 beyanı, damıtma imzası; kanon şerh paketleri.
5. **§C.4 S5 eski masa artıkları (KB-23…32)** — 10 kalem: EK-6 külliyatı (kendi oturumu), g22/g23/g24, K2 kalanları, m.37 v2, tavan-rejim, pozitif-karşılık, L8 BEKLET, K1-g, denetçi=GPT, AGENTS.md. Çoğu **BEKLET/TEYİT** — masa bunları ya tetikleyip tarihler ya da yeniden-tetik yazıp uyutur.
6. **§C.5 S6 kutu süpürmesi (KB-36, 13 alt-kalem)** — tek tur ≤20 dk: V-numara ver / BEKLET(tetik) / RET.

**"Masa yolu" sütunu (Kun-Chen zinciriyle eşleme):** **TEYİT** = konusuz mu, tek cümle · **İMZA** = metin hazır, karar-kaydet ile hüküm satırı · **MODEL-hazır** = m.37 üç-şık + öneri verili → karar-modeli doğrudan · **MODEL** = seçenekler masada türetilir (karar-hatti: celiski-kapisi → karar-modeli) · **ATLAS** = araştırma emri gerekir (gorev-emri-derleme → atlas-kosum) · **BEKLET-tetikli** = uyur, tetik yazılıdır. Masa kabuğu: `pipeline-kosum` (manifest diskte, restart-proof) → kalem başına `karar-hatti` → kayıt `karar-kaydet` (elle tetik). Masa çıktısı = hüküm satırları → world-model "karar" sürecine (KB-07).

**Bugün hangi kararlar verilebilir, hangileri kalır:** §C.0-C.3 kalemlerinin tamamı tek oturumluk ölçek (metin/şık kararı); §C.4'ün EK-6 külliyatı (KB-23) ayrı oturum ister — bu masa yalnız "ne zaman, hangi kümeler" sorusunu karara bağlar. §C.5 tek süpürme.

**Masa sonunda ne değişmiş olacak:** (i) kapsül "Salih kararları" satırı sıfırlanır ya da açık kalanlar tarih+tetikle yeniden yazılır; (ii) `veri/karar-borcu.jsonl` durum alanları güncellenir, kapananlar `karar-kaydet` hüküm satırına akar; (iii) imzayla anında yürürlüğe girenler (§D) aynı vardiyada kanona yazılır (Katman-2 icra, veto=revert).

---

## (B) TERİMLER VE KONULAR SÖZLÜĞÜ (bir kez; aşağıda tekrar edilmez)

- **Karar borcu / icra borcu:** Karar borcu = Salih'in hükmünü/imzasını bekleyen kalem (m.31 Katman-1: kural/kanon değişimi, silme-birleştirme, geri-alınması zor iş, dışa çıkacak iş, para, rol, değer tercihi). İcra borcu = Carvis'in yapacağı, karar gerektirmeyen iş (Katman-2: yapar + kaydeder + commit'ler; veto = revert). İcra borçları masaya girmez, §E'de listelenir.
- **Durum etiketleri:** İMZASIZ (metin var, imza yok) · BEKLET (bilinçli ertelendi, tetik yazılı) · Salih'te (kapsül/teslim listesinde açıkça sana atanmış) · masaya (kaynak dosya "masa kararı" demiş) · kısmen-kapandı · belirsiz · kapandı (kanıtlı — yalnız KP-01'de).
- **m.16 çelişki kapısı:** yeni karar önceki kararla çelişiyorsa önce çelişki + artı/eksi + plan raporu. **m.37 karar modeli:** üç-model kıyası (token×zaman×beklenen-kalite) + karşıt-temel, önerilen işaretli. **m.6:** öneri = kibarca tavsiye + gerekçe. **m.29:** deneysel damga (sabitler kalibrasyona açık). **m.43:** tekrar-sayacı (Laplace τ=0,8 ⇒ k=3; 90-gün pencere ∨ Salih emri) — bir aday üçüncü görüldüğünde üretime aday olur.
- **Hat-6 K1/K2/K3:** `cc/karar-onerisi-2026-08-16-hat6.md` — jarvis→DB (V-1 tablosunun rolü) · model×effort koşum-profili · kendini-geliştiren düğüm pilotu. **V-1:** `veri/baglam.sqlite` bağlam→veri tablosu (37,7k kayıt; şema v0/v1). **World-model / galaxy şeması / bus matrix / grain:** `core/world-model-tasarimi.md` — süreç-başına "1 satır = ne?" bildirimi (grain) + süreç×boyut matrisi (bus matrix); conformed boyut = bağlam-anahtar-kaydı.
- **Stokastik atlası E1-E5:** `cc/rapor-2026-08-16-1.md` entegrasyon önerisi — E1 wiki (yapıldı), E2 ajan-metodolojisi şerhi, E3 m.37 ex-ante tahmin alanı, E4 halüsinasyon-paketi şerhleri, E5 tahmin-defteri skill adayı (m.43 sayacı 1/3).
- **Vaka-1/2/3 (paralel oturum):** 08-12 paylaşılan-kaynak çakışması · 08-15 canlı-oturum şüphesi · 08-16 mükerrer koşum (~549k) — kural adayları `kuyruk/gelen-*.md`. **Şerhli-5:** 08-03 model-düşümü sırasında Opus'un yazdığı 5 kalem (`model değişikliği…/ingest-2026-08-03.md`); kanon sayılmaz, tek tek imza ister. **D-0803-1:** araç-yükleme usulü ders adayı.
- **EK-6 külliyatı:** 07-30/08-01 graf-hattı 13 raporun ~106 Katman-1 kalemi (9 küme) — masa-1/2 kapsamı DIŞINDA bırakılıp "ayrı tur" denen külliyat. **g20-g24, K1-a..l, K2-a..n:** eski masa gündemlerinin kalem kodları (`kuyruk/masa-gundemi-2026-07-30.md`, `-K2-2026-08-02.md`).
- **Spec-kit yolu A/B/C:** A dar-deneme · B desen-aktarımı · C bekle-izle (`raporlar/2026-08-13-spec-kit-atlas-raporu.md` §8). **K-016 / K-022:** pano kartları (ilk skill turu / staj). **L8:** Kun-Chen workflow hattı (firstmate); K1-1…K1-12 L8 masası kalemleri.
- **Kun-Chen masa zinciri:** `pipeline-kosum` (kabuk) → `karar-hatti` (celiski-kapisi → atlas-kosum → karar-modeli) → `karar-kaydet`. Bu dosya zincirin GİRDİSİdir; koşum bu dosyanın kapsamı değil.

---

## (C) KARAR KALEMLERİ (masa gündemi) — Katman-1, 37 kalem

### C.0 — Kapanış-teyidi (bayat görünen satırlar; masa sırası 0-3)

**KB-37 — Damıtma planı imzası (senaryo-defteri ~150KB→48KB · KILAVUZ 18,7→16KB) — ACİL**
1. *Ne karar veriliyor:* plan-imza (Carvis planı çıkarır → Salih imzalar → damitma koşar) / doğrudan koş (K-019 planı zaten imzalı — 08-01) / ertele
2. *Neden şimdi masada:* kayıt 2026-08-03 · durum **Salih'te** · tür kapanis-hukmu · masa yolu **TEYİT+İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* K-019 damıtma planı 08-01'de imzalı (senaryo-defteri:386); damitma v1.1 ŞEMA-DALI aktif — yeni imza yerine 'koş' beyanı yetebilir (TEYİT)
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet — koşum emri
5. *İcra borcu (imza sonrası):* damitma koşumu (İngest-bekleyenler dahil, İB-02)
6. *Not:* bu envanterin kaynak dosyaları büyüdükçe pointer'lar kayar — damıtma öncesi snapshot alınmalı (yükleyici SHA damgalar)
*Kaynak:* `core/durum-kapsulu.md:23` · `core/durum-kapsulu.md:30` · `kuyruk/senaryo-defteri.md:386`
**Karar: BOŞ — MASAYA.**

**KB-33 — KAPANIŞ-TEYİDİ: A1 hükmü (K-010 temel-katman sicili) — 08-12 kararıyla konusuz mu?**
1. *Ne karar veriliyor:* konusuz → listeden düş (sicil deftere işlenmeye devam eder) / hüküm ver
2. *Neden şimdi masada:* kayıt 2026-08-02 · durum **belirsiz** · tür kapanis-hukmu · masa yolu **TEYİT**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* defter 08-12: 'K-010/A-kapıları firstmate önünde kapı olmaktan çıktı; sicil yine de deftere işlenir' → A1 hükmü kapı olarak KONUSUZ, kapsül satırı bayat (Carvis okuması; Salih teyidi)
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet — kapsül satırı düşer
5. *İcra borcu (imza sonrası):* kapsül temizliği
6. *Not:* A-26/A-27 (K1-7 A3 sayımı) aynı gerekçeyle kapandı sayıldı
*Kaynak:* `core/durum-kapsulu.md:25` · `kuyruk/senaryo-defteri.md:467` · `kuyruk/senaryo-defteri.md:615`
**Karar: BOŞ — MASAYA.**

**KB-34 — KAPANIŞ-TEYİDİ: Ana-oturum tanımı (model=Fable şartı) + Dispatch BEKLET**
1. *Ne karar veriliyor:* kapandı say (terminal=ana-sıra ∧ Fable — CLAUDE.md m.41 satırı zaten 'CC ana-sıra ↔ Fable ∧ Salih beyanı') / (model=Fable) şartını ayrıca yaz / Dispatch ayrı kalem
2. *Neden şimdi masada:* kayıt 2026-07-23 · durum **kısmen-kapandı** · tür Katman-1-kural · masa yolu **TEYİT**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* kapandı sayılabilir; Dispatch K-018/K-009 gündemine ait
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet
5. *İcra borcu (imza sonrası):* yok
6. *Not:* —
*Kaynak:* `kuyruk/build-tartisma-notlari.md:71` · `kuyruk/build-tartisma-notlari.md:72` · `core/durum-kapsulu.md:13`
**Karar: BOŞ — MASAYA.**

**KB-35 — KAPANIŞ-TEYİDİ: KILAVUZ açık soruları — mobil kilit gevşetme (Fable) + Cowork-genelleme (Cowork emekli → konusuz)**
1. *Ne karar veriliyor:* Cowork yarısı konusuz → düş; mobil kilit kalsın/gevşesin
2. *Neden şimdi masada:* kayıt 2026-07-19 · durum **kısmen-kapandı** · tür Katman-1-kural · masa yolu **TEYİT**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* —
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet — KILAVUZ satırı
5. *İcra borcu (imza sonrası):* KILAVUZ damıtma turunda yazım
6. *Not:* —
*Kaynak:* `KILAVUZ.md:85` · `KILAVUZ.md:101` · `core/durum-kapsulu.md:13`
**Karar: BOŞ — MASAYA.**

### C.1 — S1 taze sistem-tasarımı (08-16; seçenek + öneri hazır)

**KB-01 — Hat-6 K1: V-1 tablosuna yazım-anı ölçüm-kapısı**
1. *Ne karar veriliyor:* (a) yalnız-okur kalsın · (b) yazım-anı ölçüm-kapısı (ingest/damıtma hattına kolon-istatistiği+NDV+token/birim üretimi) · (c) tam medallion (bronz/silver/gold DB'de)
2. *Neden şimdi masada:* kayıt 2026-08-16 · durum **Salih'te** · tür Katman-1-kural · masa yolu **MODEL-hazır**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* (b) ÖNERİLEN — düşük risk, ucuz geri-alma (script satırı)
4. *Bağımlılık:* İB-06 · *Yürürlük imzayla anında mı:* Hayır — damitma/ingest adımına script bağı (Katman-2 icra)
5. *İcra borcu (imza sonrası):* world-model §6 ilk 3 ölçüm işi otomatikleşir
6. *Not:* Hat-6 sentez-yalnız (scout açılmadı); [BOŞLUK] gold-katman kazancı ölçümsüz
*Kaynak:* `cc/karar-onerisi-2026-08-16-hat6.md:5` · `cc/karar-onerisi-2026-08-16-hat6.md:11`
**Karar: BOŞ — MASAYA.**

**KB-02 — Hat-6 K2: model×effort koşum-profili şablon alanı**
1. *Ne karar veriliyor:* (a) görev-fonksiyonu şablonuna kalıcı 'koşum-profili' alanı (model×effort×bağlam) · (b) serbest kalsın (elle, koşum-başına)
2. *Neden şimdi masada:* kayıt 2026-08-16 · durum **Salih'te** · tür Katman-1-kural · masa yolu **MODEL-hazır**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* (a) ÖNERİLEN
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Hayır — şablon yazımı (Katman-2)
5. *İcra borcu (imza sonrası):* core/sablonlar/gorev-fonksiyonu.md alanı + tetik-denetim güncellemesi
6. *Not:* eko-profil ~%40-55 token gözlemi tek-vardiyalık, sistematik A/B kıyası yok [BOŞLUK]
*Kaynak:* `cc/karar-onerisi-2026-08-16-hat6.md:13` · `cc/karar-onerisi-2026-08-16-hat6.md:18`
**Karar: BOŞ — MASAYA.**

**KB-03 — Hat-6 K3: kendini-geliştiren düğüm ilk pilotu**
1. *Ne karar veriliyor:* (a) dar pilot: skill-koşum düğümleri · (b) geniş pilot: pano/kart yaşam-döngüsü · (c) süreç-keşfi katmanı
2. *Neden şimdi masada:* kayıt 2026-08-16 · durum **Salih'te** · tür olcek-pilot · masa yolu **MODEL-hazır**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* (a) ÖNERİLEN
4. *Bağımlılık:* KB-01 · *Yürürlük imzayla anında mı:* Hayır — pilot tasarımı + koşum
5. *İcra borcu (imza sonrası):* pilot kartı (pano) + ölçüm tablosu
6. *Not:* world-model §3 learned-katman: durum-denkliği testi yalnız sonlu-durum alt-alanlarında
*Kaynak:* `cc/karar-onerisi-2026-08-16-hat6.md:20` · `cc/karar-onerisi-2026-08-16-hat6.md:26`
**Karar: BOŞ — MASAYA.**

**KB-04 — E2: ajan-metodolojisine stokastiklik-yerleşim kuralı**
1. *Ne karar veriliyor:* imza / red / metin revizesi
2. *Neden şimdi masada:* kayıt 2026-08-16 · durum **İMZASIZ** · tür serh-damga · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* tek cümle şerh: üretim/keşif stokastik · orkestrasyon+doğrulama deterministik · tekrarlı iş kodda; stokastik dal açmadan önce 'hata bütçesi ne?' sorusu
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet — tek cümle şerh (core/ajan-metodolojisi.md)
5. *İcra borcu (imza sonrası):* yok
6. *Not:* stokastik atlası 5/30/1/0, V26 3/3; MAD eşleşmiş bütçede DÜŞTÜ
*Kaynak:* `cc/rapor-2026-08-16-1.md:304` · `kuyruk/build-tartisma-notlari.md:132`
**Karar: BOŞ — MASAYA.**

**KB-05 — E3: m.37 karar kaydına ex-ante tahmin alanı + Brier izleme**
1. *Ne karar veriliyor:* imza / red / yalnız kayıt (izleme sonra)
2. *Neden şimdi masada:* kayıt 2026-08-16 · durum **İMZASIZ** · tür serh-damga · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* isteğe-bağlı ex-ante tahmin alanı (doğal-frekans formatlı, [?] damgalı) + sonuç gözlemi → Brier (≥50 olayda değerlendirilir; şimdi yalnız KAYIT); belirsizlik beyanı aleatorik/epistemik + model-koşulu
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Hayır — karar-kaydet şablon alanı (Katman-2)
5. *İcra borcu (imza sonrası):* karar-kaydet skill alanı; E5 tahmin-defteri skill adayı m.43 sayacı 1/3 (Salih öne çekebilir)
6. *Not:* kalibrasyon kazancı literatürde mütevazı ama kalıcı (Brier %6-12); geri-bildirimli pratik şart
*Kaynak:* `cc/rapor-2026-08-16-1.md:305` · `cc/rapor-2026-08-16-1.md:308`
**Karar: BOŞ — MASAYA.**

**KB-06 — E4: halüsinasyon-paketine F4/F6/F10 şerhleri + T=0 freni**
1. *Ne karar veriliyor:* paket imza / kalem-kalem / red
2. *Neden şimdi masada:* kayıt 2026-08-16 · durum **İMZASIZ** · tür serh-damga · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* F4 bağımsızlık-şartı vurgusu · F6 propriety zemini kaydı · yeni fren 'T=0-tekrarlanabilirlik varsayımı YASAK; audit = çıktı-log' · F10 kalibrasyon-karşılaştırma protokol-damgası
4. *Bağımlılık:* KB-17 · *Yürürlük imzayla anında mı:* Evet — şerh satırları (core/halusinasyon-paketi.md)
5. *İcra borcu (imza sonrası):* yok
6. *Not:* KB-17 (V26/md.21 şerhleri) ile aynı dosyaya dokunur — birlikte yazılırsa tek tur
*Kaynak:* `cc/rapor-2026-08-16-1.md:306`
**Karar: BOŞ — MASAYA.**

**KB-07 — Bus matrix'e 'karar-borcu' süreç satırı + envanterin kanonik konumu**
1. *Ne karar veriliyor:* (a) bus matrix'e satır: karar-borcu (1 satır = 1 açık kalem; kapanınca 'karar' sürecine hüküm satırı) · (b) 'karar' süreci içinde durum alanı olarak (ayrı süreç yok) · (c) yalnız rapor, tablo kalıcılaşmasın
2. *Neden şimdi masada:* kayıt 2026-08-16 · durum **masaya** · tür Katman-1-kural · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* (a) — bu dosyayla birlikte gelen veri/karar-borcu.jsonl + tools/karar-borcu-tablo.py deneysel m.29 (Katman-2 kuruldu; kanon satırı Salih'te)
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet — tek satır (bus matrix)
5. *İcra borcu (imza sonrası):* kapanan kalemlerin karar-kaydet ile hüküm satırına akıtılması (kural yazılırsa)
6. *Not:* bu hazırlık dosyasının kendi ürettiği kalem; world-model §2 'süreç-başına grain bildirimi' kuralına uyum
*Kaynak:* `core/world-model-tasarimi.md:12` · `core/world-model-tasarimi.md:21`
**Karar: BOŞ — MASAYA.**

### C.2 — S3 oturum-disiplini kural adayları

**KB-08 — Vaka-2 canlı-oturum kapısı + Vaka-3 koşum-önü manifest kapısı (seans-acilis'e)**
1. *Ne karar veriliyor:* imza (ikisi) / yalnız vaka-2 / metin revizesi
2. *Neden şimdi masada:* kayıt 2026-08-15 · durum **İMZASIZ** · tür Katman-1-kural · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* canlı-oturum kapısı: son commit ≤15 dk ∧ kapsülde kapanış yok → 'paralel-oturum şüphesi' beyanı + diğer oturumun SAHADA işini koşmama · koşum-önü manifest kapısı: Workflow açmadan hat manifesti + git log okunur
4. *Bağımlılık:* KB-09 · *Yürürlük imzayla anında mı:* Evet — seans-acilis §1.4 metni (bugün deneysel olarak zaten uygulanıyor)
5. *İcra borcu (imza sonrası):* skill metni + eval satırı
6. *Not:* 3 vaka / 4 gün (08-12, 08-15, 08-16 ~549k mükerrer koşum); bu oturumun açılışında da 3 canlı oturum vardı
*Kaynak:* `kuyruk/gelen-2026-08-15-paralel-oturum-vaka-2.md:20` · `kuyruk/gelen-2026-08-16-paralel-oturum-vaka-3.md:16` · `raporlar/vardiya-teslim-2026-08-15-seans3-terminal.md:19`
**Karar: BOŞ — MASAYA.**

**KB-09 — Vaka-1: paylaşılan-kaynak + motor-kapatma freni (paralel oturum protokolü)**
1. *Ne karar veriliyor:* taslak imza / revize / red
2. *Neden şimdi masada:* kayıt 2026-08-12 · durum **İMZASIZ** · tür Katman-1-kural · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* taslak dosyada; tek kaynak JARVIS (staj tarafında yazılmaz)
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet — kural metni
5. *İcra borcu (imza sonrası):* dosyanın ingest'i (İB-02) + wiki 'paralel-oturum-protokolu' sayfası
6. *Not:* vaka-1/2/3 tek 'paralel-oturum protokolü' başlığında birleştirilebilir
*Kaynak:* `kuyruk/gelen-2026-08-12-paralel-oturum-kaynak-cakismasi.md:51` · `kuyruk/gelen-2026-08-12-paralel-oturum-kaynak-cakismasi.md:117`
**Karar: BOŞ — MASAYA.**

**KB-10 — Staj-hasadı kural adayları: git add -A yasağı (H4) + skill iki-ev/ikilenme (H6) + 'üretici-beyanı≠kanıt' wiki adı**
1. *Ne karar veriliyor:* kalem-kalem imza/red
2. *Neden şimdi masada:* kayıt 2026-08-12 · durum **masaya** · tür Katman-1-kural · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* —
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* H4 evet (kural) · H6 hayır (doğrulama gerekir)
5. *İcra borcu (imza sonrası):* H6 ikilenme doğrulaması; wiki sayfası
6. *Not:* md.49: staj VERİSİ taşınmaz, yöntem yönü serbest — bu kalemler yöntemdir
*Kaynak:* `kuyruk/gelen-2026-08-12-staj-yontem-hasati.md:35` · `kuyruk/gelen-2026-08-12-staj-yontem-hasati.md:50` · `kuyruk/gelen-2026-08-12-staj-hasadi-2-yontem-eslemesi.md:53` (+1)
**Karar: BOŞ — MASAYA.**

**KB-11 — Senkron/çatal fren paketi: stash-önce · kalıcı otomatik-hizalama · pull-önce · yalancı-OK kök-neden**
1. *Ne karar veriliyor:* paket imza / yalnız stash-önce / Mac'te senkron yokken BEKLET
2. *Neden şimdi masada:* kayıt 2026-07-23 · durum **Salih'te** · tür Katman-1-kural · masa yolu **TEYİT+İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* gece-senkron Mac'te koşmuyor (Salih 08-11 'gerek yok') — paketin yarısı konusuz olabilir; stash-önce elle-pratik olarak imzalanabilir
4. *Bağımlılık:* KB-33 · *Yürürlük imzayla anında mı:* stash-önce evet; script frenleri senkron yeniden kurulursa
5. *İcra borcu (imza sonrası):* gece-senkron script'i (PS1) Mac'e uyarlanırsa pull-önce + ls-remote adımı
6. *Not:* V43-yarış deseninin 2. tekrarı (08-04); Windows akıbetine (KB-33) bağlı
*Kaynak:* `core/durum-kapsulu.md:25` · `kuyruk/senaryo-defteri.md:550` · `kuyruk/build-tartisma-notlari.md:75` (+1)
**Karar: BOŞ — MASAYA.**

**KB-12 — D-0803-1 araç-yükleme usulü (ağır ToolSearch oturum başında / ayrı oturum)**
1. *Ne karar veriliyor:* imza (ders → KILAVUZ usul) / red
2. *Neden şimdi masada:* kayıt 2026-08-03 · durum **Salih'te** · tür Katman-1-kural · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* usul adayı metni raporda hazır: büyük-bağlamlı oturumun geç evresinde toplu araç-yükleme prompt-cache kırar → kota-fallback; ağır yüklemeler oturum BAŞINDA ya da ayrı oturumda
4. *Bağımlılık:* — · *Yürürlük imzayla anında mı:* Evet — KILAVUZ ders satırı
5. *İcra borcu (imza sonrası):* yok
6. *Not:* kök-neden ölçümü 08-03 (tools_changed cache-kırılması ~152K token)
*Kaynak:* `core/durum-kapsulu.md:25` · `raporlar/2026-08-03-model-dusumu-olcum.md:40`
**Karar: BOŞ — MASAYA.**

**KB-13 — Şerhli-5 kalem (08-03 model-düşümü ingest'i): hangisi kanona geçer**
1. *Ne karar veriliyor:* kalem-kalem: (1) UIPI hükmü (2) K-018 çıkarımı (3) model-düşümü tespit protokolü (4) yem hipotezi — ölçümle YANLIŞLANDI (5) usage+model tek-betik
2. *Neden şimdi masada:* kayıt 2026-08-03 · durum **Salih'te** · tür Katman-1-kural · masa yolu **İMZA**
3. *Carvis önerisi / rapor yönü (m.6 — karar değil):* (3) bugün fiilen kullanıldı (bu oturum 8 transkripti JSONL model-alanıyla ayrıştırdı) → usul adayı güçlü; (4) düşer; (5) İB-08 usage-otomasyonuyla birleşik
4. *Bağımlılık:* İB-08 · *Yürürlük imzayla anında mı:* (3) evet — KILAVUZ usul satırı; diğerleri hayır
5. *İcra borcu (imza sonrası):* kanona geçen kalemlerin şerhli klasörden yazımı
6. *Not:* kapsülde 'şerhli 5 kalem' 13 gündür Salih listesinde
*Kaynak:* `core/durum-kapsulu.md:25` · `model değişikliği ile orijinalliği bozulmuş olan chat/ingest-2026-08-03.md:12` · `model değişikliği ile orijinalliği bozulmuş olan chat/ingest-2026-08-03.md:22` (+1)
**Karar: BOŞ — MASAYA.**

### C.3 — S2 yön/entegrasyon + S4 kanon şerh-adayları (kompakt kartlar)

| # | Kalem | Durum · kayıt | Seçenekler | Öneri (m.6) | Yol | Bağ. | Kaynak |
|---|---|---|---|---|---|---|---|
| KB-14 | Spec-kit entegrasyon yolu A/B/C + V1 ölçek-şerhi (m.16) | Salih'te · 2026-08-13 | A dar-deneme (tek küçük projede spec-kit) · B desen-aktarımı (spec/plan/tasks desenini kendi şablonlarımıza) · C bekle-izle | Carvis (karar değil): V1 iterasyon-önce ilkesi korunur + ölçek-eşiği şerhi eklenir (küçük işte süreç yükü ~10×) | MODEL-hazır | — | `raporlar/2026-08-13-spec-kit-atlas-raporu.md:82` · `raporlar/2026-08-13-spec-kit-atlas-raporu.md:90` (+2) |
| KB-15 | Agile-metodoloji araştırma tetiği (sprint↔vardiya, backlog↔pano/kuyruk) | Salih'te · 2026-08-12 | tetik çek (atlas ekonomi ~150-250k) / kutuda beklet / red | — | ATLAS | — | `fikir-kutusu.md:94` · `raporlar/vardiya-teslim-2026-08-12-l8-mac.md:9` (+1) |
| KB-16 | Windows kurulumunun akıbeti (paralel mi terk mi) + gece-senkron kaderi | Salih'te · 2026-08-12 | paralel sürdür / terk (arşiv, m.8) / dondur (Salih gün seçince K-011 ile birlikte) | — | İMZA | — | `raporlar/vardiya-teslim-2026-08-12-l8-mac.md:19` · `core/durum-kapsulu.md:17` |
| KB-20 | K-016 kapanış hükmü (DONE-eşiği fiilen aşıldı) + description-eval turu | Salih'te · 2026-07-23 | kapat (SON BİTEN'e) / açık tut (description-eval turu DONE'a dek) / kapsam genişlet (skill-üretim şeması sonrası hazine 14) | — | İMZA | İB-07 | `core/pano.md:13` · `core/durum-kapsulu.md:25` (+1) |
| KB-21 | 9 tam-merge'li claude/ dalının silimi (m.8) | Salih'te · 2026-08-14 | sil (yerel+uzak; tam-merge kanıtı git ile) / yalnız uzak / arşiv etiketi (tag) + sil / dokunma | — | İMZA | — | `raporlar/vardiya-teslim-2026-08-14-anasira-terminal.md:21` · `core/durum-kapsulu.md:25` |
| KB-22 | K-022 'envanter 11/11 canlı' beyanı → entegrasyon masasının açılması | Salih'te · 2026-08-13 | beyan ver (masa açılır) / beyan yok (P6 Mac uyarlaması önce) / envanteri Carvis doğrulasın (script) | — | TEYİT | İB-15 | `core/durum-kapsulu.md:15` |
| KB-17 | 08-15 kanon şerh-adayları: V26 son-üçlük örneklemi · md.21 derece-sorma yasağı şerhi · damıtma %50→sorgu-uyumu | İMZASIZ · 2026-08-15 | kalem-kalem imza/red (3 kalem) | V26 örneklem 'rastgele' → 'son üçlük ağırlıklı + tüm sayısal iddialar' (FActScore konum bulgusu) · md.21 yasağı koşulsuz değil (yüksek-tabanda önce üret sonra doğrula) · damıtma hedefi orana değil sorgu-uyumuna | İMZA | — | `core/halusinasyon-paketi.md:63` · `core/halusinasyon-paketi.md:64` (+2) |
| KB-18 | Metodoloji şerh paketi: m.44 RouteLLM çapası [X] · m.43 N=3 gerekçesi + τ-türetimi/pencereli sayaç · m.46(a) SHA→şablon-sonu · m.40b antitez borcu (12 yapı-taşı) | İMZASIZ · 2026-08-14 | paket imza / kalem-kalem (5) / red | stokastik atlası m.44 RouteLLM [X] durumunu DESTEKLER yönde (bandit/öğrenilmiş-yönlendirme n<50 ölçümsüz) — [X] kalır; m.43 τ=0,8⇒k=3 türetimi + 90-gün penceresi şerh olarak yazılır | İMZA | — | `raporlar/vardiya-teslim-2026-08-14-anasira-terminal.md:20` · `core/ajan-metodolojisi.md:18` (+3) |
| KB-19 | Skill-hazine description bütçesi: 7962>7200 char aşımı — /context ölçümüyle eşik yeniden türetilir | masaya · 2026-08-15 | eşiği ölçümle yeniden türet (Salih /context koşar, ~1 dk) / eşiği kaldır (yalnız platform 1536/desc) / 7200 kalsın + zorla kısalt | ölçüm-önce (m.35): /context çıktısı gelmeden sabit değişmez | TEYİT+İMZA | — | `cc/karar-onerisi-2026-08-16-hat6.md:30` · `raporlar/2026-08-15-skill-semasi-test-turu.md:29` (+2) |

*Her satır için Karar: BOŞ — MASAYA. Uzun seçenek metinleri JSONL'de tam; burada kısaltılmadı, tablo geniştir — yatay kaydır.*

### C.4 — S5 eski masa artıkları (EK-6, g22-24, K2 kalanları, m.37 v2, tavan-rejim, pozitif-karşılık, L8, K1-g, denetçi, AGENTS.md)

| # | Kalem | Durum · kayıt | Seçenekler | Öneri (m.6) | Yol | Bağ. | Kaynak |
|---|---|---|---|---|---|---|---|
| KB-23 | EK-6 külliyatı (~106 K1 kalemi / 9 küme) — kendi masa oturumu | masaya · 2026-08-01 | ayrı masa oturumu (Kun-Chen pipeline: küme-başına karar-hatti) / küme-başına önceliklendirip yalnız 2-3 küme / DONDUR (tarih damgalı, tetik yazılı) | — | MODEL | KB-24, KB-25 | `kuyruk/senaryo-defteri.md:462` · `kuyruk/masa-gundemi-2026-07-30.md:532` |
| KB-24 | g22 bellek/RAM B1-B5 · g23 loop-desen K1-a..l · g24 rejim-etiketi tetiği (K1-24) · K2-d tetik(D8) alanı — EK-6 turuyla | BEKLET · 2026-08-01 | EK-6 oturumuna bağlı kalsın / g23+K2-d (tetik/loop) öne çekilsin — skill-tetikleme şeması 08-15 bunların bir kısmını fiilen kapsamış olabilir (TEYİT) | teyit-önce: Hat-2 tetikleme şeması (9-alanlı çağrı sözleşmesi) K2-d/g23 tetik kalemlerini süpersede etti mi — Carvis çapraz okuma (Katman-2, ~1 koşum) | TEYİT | KB-23 | `kuyruk/masa-gundemi-2026-07-30.md:549` · `kuyruk/masa-gundemi-2026-07-30.md:553` (+2) |
| KB-25 | K2 kalanları: K2-e kısıt-profili alanı (BEKLET) · K2-l m.40b hayatta-kalma serisi hükmü · K2-m ölçüm-kültürü arızası (sistemik) | BEKLET · 2026-08-02 | EK-6/g20 oturumunda / K2-l+K2-m şimdi (08-15/16 koşum serisi yeni veri: 5 m.40b ekonomi-koşumu SAĞLAM 3-20 aralığı) / BEKLET | K2-l için yeni veri var: rapor-1..5,8,9 hayatta-kalma serisi (39/54 · 28/19 · 30/63 · 15/49 · 3/20 · 20/33 · 6/16) — hüküm için yeter mi Salih'te | MODEL | KB-23 | `kuyruk/masa-gundemi-K2-2026-08-02.md:28` · `kuyruk/masa-gundemi-K2-2026-08-02.md:36` (+2) |
| KB-26 | m.37 v2: fıkra yürürlüğü (kalibrasyon koşumu şartı) + eksen-örtüsü fıkrası İMZASIZ | İMZASIZ · 2026-08-01 | kalibrasyon koşumunu (İB-10) bekle / içerik-imzalı fıkraları şartsız yürürlüğe al / eksen-örtüsü v2 sentezini ayrı imzala | — | MODEL | İB-10, KB-05 | `kuyruk/senaryo-defteri.md:391` · `kuyruk/build-tartisma-notlari.md:100` (+1) |
| KB-27 | Koşum-tavanı paketi: çağrı-sayısı deterministik freni + tavan-rejim Öneri A/B/C (rejim-etiketi ilkesi) | İMZASIZ · 2026-08-01 | A sınıf-bazlı anomali-freni / B mekanik düzeltmeler / C REJİM-ETİKETİ ilkesi / paket | dosyada: A→B hattı + C rejim-etiketiyle genel ilke; 08-15 ekonomi-rejimi (−%30) fiilen bir rejim-etiketi uygulaması | MODEL-hazır | İB-08 | `kuyruk/senaryo-defteri.md:380` · `kuyruk/gelen-2026-08-01-tavan-rejim-karari.md:11` (+1) |
| KB-28 | Pozitif-karşılık aday listesi (8 eski yasak → pozitif kural) | İMZASIZ · 2026-08-02 | satır-satır imza (8) / paket / red | m.8/m.23/m.33/m.39/m.7 + KILAVUZ×2 + m.38 için karşılıklar dosyada | İMZA | — | `kuyruk/pozitif-karsilik-borclari.md:5` · `kuyruk/pozitif-karsilik-borclari.md:12` |
| KB-29 | L8 hattı BEKLET: K1-2…K1-9 + K1-11 ('Codex-inşa' açıklaması Salih'ten) + P4 çelişki kalemleri | BEKLET · 2026-08-03 | BEKLET sürsün (tetik: workflow kurulup çalışınca — L8 Faz 5 firstmate koştu 08-13 → tetik DOLMUŞ olabilir, TEYİT) / yeniden masaya / K1-11 için Salih 1 cümle | — | TEYİT | KB-22 | `kuyruk/senaryo-defteri.md:516` · `raporlar/2026-08-03-masa-hazirlik-L8.md:178` (+1) |
| KB-30 | K1-g: monolit referans dilimi (varyant c) koşulsun mu (V1 verim tanımı için) | Salih'te · 2026-08-01 | koş (bütçe ~1 koşum) / koşma (V1 verim tanımı hesaplanamaz kalır) | — | İMZA | — | `kuyruk/senaryo-defteri.md:409` |
| KB-31 | Denetçi = aile-dışı model (GPT) + tester model seçimi (paraya koşullu) | Salih'te · 2026-07-22 | aile-dışı denetçi (para) / aile-içi (mevcut m.40b maskeli hakem) / BEKLET (K-010 ∧ bütçe) | stokastik atlası: çok-ajanlı tartışma eşleşmiş bütçede tek-ajanın altında (MAD DÜŞTÜ) — aile-dışı denetçinin kazancı ölçümsüz | BEKLET-tetikli | — | `kuyruk/build-tartisma-notlari.md:67` · `kuyruk/build-tartisma-notlari.md:69` |
| KB-32 | AGENTS.md köprüsü (BEKLET; K39 sunucu-taraflı koruma koşulu) | BEKLET · 2026-07-30 | BEKLET sürsün / koşulu değiştir (gitleaks host TEMİZ 08-02, sunucu koruma izle-modunda) / red | — | TEYİT | — | `kuyruk/masa-gundemi-2026-07-30.md:338` · `kuyruk/senaryo-defteri.md:450` (+1) |

*Öneri (Carvis, karar değil): bu kümede masa iki şey yapar — (i) EK-6 için tarih + hazırlık dosyası emri (bu formatın kardeşi), (ii) kalanları TEYİT/BEKLET-tetikli olarak damgalar. KB-24 nüansı: K2-d hükmü zaten "EKLE — g23 ile birleşik" (kaynak satırı), açık olan icrasıdır.*

### C.5 — S6 kutu/kuyruk süpürmesi (KB-36; 13 alt-kalem, tek tur)

*Ne karar veriliyor:* tek süpürme turu: her satır için numara-ver / BEKLET(tetik yaz) / RET; ya da EK-6 masasına ekle · *Öneri:* süpürme turu (≤20 dk): 13 satır — hiçbiri tek başına inşa istemiyor, çoğu 'kayıt statüsü' kararı

| Alt | Kalem | Kaynak | Beklenen karar biçimi |
|---|---|---|---|
| a | UFUK paketi ×3 — skill-dili arayüzü · konuşma=sistem-geliştirme · çağrılabilir-sistem (numarasız, Salih vizyonu 07-30) | `fikir-kutusu.md:86-88` | V-numara / UFUK-kalsın |
| b | Alt-ajan-aracılı içerik-karantina deseninin KILAVUZ'a yazımı | `fikir-kutusu.md:90` | yaz (m.29) / kutuda kalsın |
| c | Şablon-aday: emir sürümü + koşum-ortası revizyon kanalı | `fikir-kutusu.md:92` | E1 şablon masasına / RET |
| d | Önerme→DbC→PBT skill adayı — V-numara (sayım belgesiz) | `raporlar/2026-08-15-skill-semasi-test-turu.md:38` | numara ver / BEKLET |
| e | ai2ai rapor formatı Katman-1 adayları (gorev-emri şablonu + KILAVUZ rapor-katman zinciri) | `kuyruk/gelen-2026-08-01-ai2ai-rapor-karari.md:19` | yaz / BEKLET |
| f | Ölçek-yasaları K1-K4 (sözlük 13 satır · dosya-iniş-yeri · ölçüm-hedefi · θ/γ sırası) — ölçüm Ö-1/Ö-2 yapıldı, hüküm yok | `kuyruk/gelen-2026-08-01-olcek-yasalari.md:169-172` | 4 kısa hüküm |
| g | Öğretim taban-yoklaması adım-0 kuralı (V55 masasıyla) | `fikir-kutusu.md:93` | imza / BEKLET(V55) |
| h | S6 hukuki-çevre mini-masası (küçük, aciliyet düşük) | `kuyruk/senaryo-defteri.md:443` | tarih ver / uyut |
| i | Kaçırılan-tetik m.43 sayacı: 30-16/30-17/30-25 = 3 mü? | `kuyruk/skill-fikir-kutusu.md:26` | evet→aday satırı / hayır |
| j | A7 geriye-dönük denetim ailesi (V38/V40 MEZUN-BEKLEMEDE) | `fikir-kutusu.md:67`, `core/tuzuk-v0.md:63` | koş / kapat |
| k | Sözlük Skill Hazinesi'ne yol-planla girişi (sözlük DONDU) | `cc/karar-onerisi-2026-08-16-hat6.md:31` | ekle / dondur |
| l | V13 ekip-lideri atamaları + loop hiyerarşisi (rol; 07-12'den açık) | `fikir-kutusu.md:29` | ata / K-010'a bağla |
| m | Semantik-compiler ajanı (ai2ai→insan çevirisi; rol adayı) | `fikir-kutusu.md:89` | rol kaydı / kutuda |

**Karar: BOŞ — MASAYA (13 ayrı imza alanı).**

---

## (D) YÜRÜRLÜK / BORÇ AYRIMI (imzayla anında yürürlük mü — icra borcu ne)

| Kalem | İmzayla anında yürürlük | İcra borcu (Katman-2, Carvis) |
|---|---|---|

| KB-01 Hat-6 K1: V-1 tablosuna yazım-anı ölçüm-kapısı | Hayır — damitma/ingest adımına script bağı (Katman-2 icra) | world-model §6 ilk 3 ölçüm işi otomatikleşir |
| KB-02 Hat-6 K2: model×effort koşum-profili şablon alanı | Hayır — şablon yazımı (Katman-2) | core/sablonlar/gorev-fonksiyonu.md alanı + tetik-denetim güncellemesi |
| KB-03 Hat-6 K3: kendini-geliştiren düğüm ilk pilotu | Hayır — pilot tasarımı + koşum | pilot kartı (pano) + ölçüm tablosu |
| KB-04 E2: ajan-metodolojisine stokastiklik-yerleşim kuralı | Evet — tek cümle şerh (core/ajan-metodolojisi.md) | yok |
| KB-05 E3: m.37 karar kaydına ex-ante tahmin alanı + Brier izleme | Hayır — karar-kaydet şablon alanı (Katman-2) | karar-kaydet skill alanı; E5 tahmin-defteri skill adayı m.43 sayacı 1/3 (Salih öne çekebilir) |
| KB-06 E4: halüsinasyon-paketine F4/F6/F10 şerhleri + T=0 freni | Evet — şerh satırları (core/halusinasyon-paketi.md) | yok |
| KB-07 Bus matrix'e 'karar-borcu' süreç satırı + envanterin kanonik konumu | Evet — tek satır (bus matrix) | kapanan kalemlerin karar-kaydet ile hüküm satırına akıtılması (kural yazılırsa) |
| KB-08 Vaka-2 canlı-oturum kapısı + Vaka-3 koşum-önü manifest kapısı (seans-a… | Evet — seans-acilis §1.4 metni (bugün deneysel olarak zaten uygulanıyor) | skill metni + eval satırı |
| KB-09 Vaka-1: paylaşılan-kaynak + motor-kapatma freni (paralel oturum protok… | Evet — kural metni | dosyanın ingest'i (İB-02) + wiki 'paralel-oturum-protokolu' sayfası |
| KB-10 Staj-hasadı kural adayları: git add -A yasağı (H4) + skill iki-ev/ikil… | H4 evet (kural) · H6 hayır (doğrulama gerekir) | H6 ikilenme doğrulaması; wiki sayfası |
| KB-11 Senkron/çatal fren paketi: stash-önce · kalıcı otomatik-hizalama · pul… | stash-önce evet; script frenleri senkron yeniden kurulursa | gece-senkron script'i (PS1) Mac'e uyarlanırsa pull-önce + ls-remote adımı |
| KB-12 D-0803-1 araç-yükleme usulü (ağır ToolSearch oturum başında / ayrı otu… | Evet — KILAVUZ ders satırı | yok |
| KB-13 Şerhli-5 kalem (08-03 model-düşümü ingest'i): hangisi kanona geçer | (3) evet — KILAVUZ usul satırı; diğerleri hayır | kanona geçen kalemlerin şerhli klasörden yazımı |
| KB-14 Spec-kit entegrasyon yolu A/B/C + V1 ölçek-şerhi (m.16) | Hayır — yol seçimine göre icra | A: pilot proje kartı · B: şablon revizyonu · C: izleme satırı |
| KB-15 Agile-metodoloji araştırma tetiği (sprint↔vardiya, backlog↔pano/kuyruk… | Hayır — araştırma emri | gorev-emri-derleme + atlas-kosum |
| KB-16 Windows kurulumunun akıbeti (paralel mi terk mi) + gece-senkron kaderi | Evet — kapsül satırı; terk ise arşiv işi | K-011 taşıma kartı ilişkilendirmesi; PS1 script arşivi |
| KB-17 08-15 kanon şerh-adayları: V26 son-üçlük örneklemi · md.21 derece-sorm… | Evet — şerh satırları | KB-06 ile aynı yazım turu |
| KB-18 Metodoloji şerh paketi: m.44 RouteLLM çapası [X] · m.43 N=3 gerekçesi … | Evet — şerh satırları (core/ajan-metodolojisi.md, tüzük m.43/m.46) | m.40b antitez borcu 12 yapı-taşı için ayrı ekonomi-koşumu (Salih onayıyla) |
| KB-19 Skill-hazine description bütçesi: 7962>7200 char aşımı — /context ölçü… | Evet — sabit değişimi (core/skill-uretim-semasi.md) | kapi-denetim.py F1e eşiği; 08-16 sıkıştırma 8840→7962 yapıldı |
| KB-20 K-016 kapanış hükmü (DONE-eşiği fiilen aşıldı) + description-eval turu | Evet — pano kart hareketi | description-eval 20×3×14 koşumu (İB-07) |
| KB-21 9 tam-merge'li claude/ dalının silimi (m.8) | Evet — git komutu (Salih ya da Carvis onayla) | branch listesi + merge-base kanıtı komut bloğu |
| KB-22 K-022 'envanter 11/11 canlı' beyanı → entegrasyon masasının açılması | Evet — beyan | entegrasyon masası hazırlık dosyası (bu formatın kardeşi) |
| KB-23 EK-6 külliyatı (~106 K1 kalemi / 9 küme) — kendi masa oturumu | Hayır — masa planı | masa-öncesi hazırlık dosyası (bu format) EK-6 için |
| KB-24 g22 bellek/RAM B1-B5 · g23 loop-desen K1-a..l · g24 rejim-etiketi teti… | Hayır | süpersede çapraz-okuma raporu |
| KB-25 K2 kalanları: K2-e kısıt-profili alanı (BEKLET) · K2-l m.40b hayatta-k… | Hayır | K2-e: kısıt yükü ölçümü önce |
| KB-26 m.37 v2: fıkra yürürlüğü (kalibrasyon koşumu şartı) + eksen-örtüsü fık… | Şartsız alınırsa evet | denetçi kalibrasyon koşumu (İB-10) |
| KB-27 Koşum-tavanı paketi: çağrı-sayısı deterministik freni + tavan-rejim Ön… | C evet (ilke); A/B icra | fren tasarımı (Workflow budget + kapı) |
| KB-28 Pozitif-karşılık aday listesi (8 eski yasak → pozitif kural) | Evet — tüzük şerh satırları | yazım turu |
| KB-29 L8 hattı BEKLET: K1-2…K1-9 + K1-11 ('Codex-inşa' açıklaması Salih'ten)… | Hayır | L8 hazırlık dosyası güncellemesi |
| KB-30 K1-g: monolit referans dilimi (varyant c) koşulsun mu (V1 verim tanımı… | Evet — koşum emri | koşum + ölçüm-bankı satırı |
| KB-31 Denetçi = aile-dışı model (GPT) + tester model seçimi (paraya koşullu) | Hayır | yok |
| KB-32 AGENTS.md köprüsü (BEKLET; K39 sunucu-taraflı koruma koşulu) | Hayır | K39 durumu teyidi (üç ölçüt) |
| KB-33 KAPANIŞ-TEYİDİ: A1 hükmü (K-010 temel-katman sicili) — 08-12 kararıyla… | Evet — kapsül satırı düşer | kapsül temizliği |
| KB-34 KAPANIŞ-TEYİDİ: Ana-oturum tanımı (model=Fable şartı) + Dispatch BEKLE… | Evet | yok |
| KB-35 KAPANIŞ-TEYİDİ: KILAVUZ açık soruları — mobil kilit gevşetme (Fable) +… | Evet — KILAVUZ satırı | KILAVUZ damıtma turunda yazım |
| KB-36 Kutu adayları — V-numara/kayıt/imza süpürmesi: UFUK paketi ×3 · alt-aj… | Evet — kutu satırı damgaları | kutu/kuyruk yazımı |
| KB-37 Damıtma planı imzası (senaryo-defteri ~150KB→48KB · KILAVUZ 18,7→16KB)… | Evet — koşum emri | damitma koşumu (İngest-bekleyenler dahil, İB-02) |

---

## (E) İCRA BORÇLARI — Carvis (Katman-2; masaya GİRMEZ, bilgi için) — 14 kalem

| # | İş | Durum · kayıt | Bağ. | Not | Kaynak |
|---|---|---|---|---|---|
| İB-01 | Bulut ritüel-kopyaları güncellemesi (seans-acilis/seans-kapanis adları) — Salih girişi ~5 dk | icra-sırada · 2026-08-15 | — | Salih tarayıcı girişi gerektirir | `cc/pipeline-2026-08-15-baglam-silver-katmani.md:16` · `raporlar/vardiya-teslim-2026-08-15-seans3-terminal.md:26` (+1) |
| İB-02 | İngest bekleyen: paralel-oturum kaynak-çakışması (08-12) + 2 KILAVUZ raporu (HAM, 08-05) | icra-sırada · 2026-08-14 | KB-37 | — | `core/durum-kapsulu.md:24` |
| İB-03 | md.49 yazım turu (tüzük + pano K-022) + sözlük raporu ingest'i + K2-n geriye-dönük damga denetimi | icra-sırada · 2026-08-03 | — | K2-n kural imzalı, denetim kapsam sayımı yapılmadı (maliyet [?]) | `core/durum-kapsulu.md:26` · `kuyruk/senaryo-defteri.md:493` (+1) |
| İB-04 | Wiki kuyruğu (~12 aday: gnhf/treehouse/lavish/no-mistakes/spec-kit/ajan-metodolojisi/baglam-anahtar-kaydi/paralel-oturum-protokolu/veri-tablosu + 07-30 dörtlüsü) | icra-sırada · 2026-07-30 | — | — | `wiki/README.md:30` · `kuyruk/masa-gundemi-2026-07-30.md:407` (+1) |
| İB-05 | Erteleme kapsamı (geçiş bitince): Türkçeleştirme · Orca hook temizliği · find-skills · SKILL.md mükerrer şerh · lease iadeleri · kural-entegrasyonu | icra-sırada · 2026-08-04 | — | 'geçiş bitince' tetiği: terminal ana-sıra 08-14 → tetik DOLDU | `core/durum-kapsulu.md:27` |
| İB-06 | Kalibrasyon borçları (koşum-sayısı eşikli): skill-kapısı τ/W/β/n_val 10 koşum · H formülü ≥50 olay · U-skoru 5 damıtma · anahtar-kaydı k1/k2 10 emeklilik · world-model §6 ölçüm işleri (NDV→tekrar→dil-çarpanı→sort-key→durum-denkliği) | icra-sırada · 2026-08-15 | KB-01 | karar değil, sayaç; masaya girmez | `core/skill-uretim-semasi.md:103` · `core/halusinasyon-paketi.md:31` (+3) |
| İB-07 | Description-eval tam koşumu (20 sorgu × 3 × 14 skill; K-016 borcu) | icra-sırada · 2026-08-15 | KB-20 | KB-20 (K-016 kapanışı) buna bağlı | `raporlar/2026-08-15-skill-semasi-test-turu.md:27` · `raporlar/2026-08-15-skill-semasi-test-turu.md:45` |
| İB-08 | Usage-otomasyon: panelsiz ölçüm-bankı akışı yol seçimi (i JSONL-parse betiği · ii OTLP/telemetri · iii ccusage-sınıfı) + model-düşümü tespiti tek betikle | icra-sırada · 2026-08-02 | — | KB-13 (5) ve KB-27 buna bağlı | `kuyruk/senaryo-defteri.md:478` · `model değişikliği ile orijinalliği bozulmuş olan chat/ingest-2026-08-03.md:17` |
| İB-09 | Yol-C V26-yakalama etkisi ölçümü (opus/sonnet pin kararına girdi) | icra-sırada · 2026-08-01 | — | pin kararı Salih'te ama ölçüm önce | `kuyruk/senaryo-defteri.md:359` · `kuyruk/senaryo-defteri.md:379` |
| İB-10 | Denetçi kalibrasyon koşumu (md.28) + zorlanabilirlik etiket turu (md.27) + m.37 A7 matematiksel-temel denetimi | icra-sırada · 2026-08-01 | KB-26 | KB-26 m.37 v2 yürürlüğü kalibrasyona bağlı | `kuyruk/senaryo-defteri.md:444` · `kuyruk/m37-taslak-karar-modeli.md:27` |
| İB-11 | Dosya düzeltme borçları paketi (md.43, 5 madde) + kalan iki mini test (Plan-ajanı, kapsül-geri-gelme) + Adım-0 managed-settings testi (Salih terminali) | icra-sırada · 2026-07-30 | — | m.8 usulü | `kuyruk/senaryo-defteri.md:460` · `kuyruk/masa-gundemi-2026-07-30.md:400` (+2) |
| İB-12 | B2/B7/B9 kalan borç kalemleri (hakem 7 ölçüm · PENS ölçek tanımları · öz-sayım↔panel farkı) + dil-sınırı↔loop-sınırı hipotez sınaması | belirsiz · 2026-08-02 | — | n=3 çürütmeye yeter, doğrulamaya yetmez | `kuyruk/build-tartisma-notlari.md:118` · `kuyruk/build-tartisma-notlari.md:120` (+2) |
| İB-13 | P6 betiği Mac uyarlaması + dörtlü deftere | icra-sırada · 2026-08-12 | KB-22 | kapsül 'sonraki ilk iş 2' | `core/durum-kapsulu.md:31` · `core/durum-kapsulu.md:15` |
| İB-14 | K2-d/g23 tetik kalemleri ↔ skill-tetikleme şeması süpersede çapraz-okuması (KB-24 teyidi) | icra-sırada · 2026-08-16 | KB-24 | bu hazırlık dosyasının önerdiği teyit işi | `kuyruk/masa-gundemi-K2-2026-08-02.md:27` · `kuyruk/masa-gundemi-2026-07-30.md:553` |

**Ayıklananlar (kapandı, kanıtlı — masaya girmez):** Cowork→CC 6-aşamalı geçiş sırası · V64 Cowork saf-dışı · D-0802-1 emir-konumu şablon alanı · skill rename gunaydin→seans · K-010 A1 kapısı ilanı · K1-7 dış-koşucu A3 sayımı. Kanıt: core/durum-kapsulu.md:13 (Cowork emekli) · core/sablonlar/gorev-emri.md:6 (K2-b imza) · cc/pipeline-2026-08-15-baglam-silver-katmani.md:50 (rename TAM) · kuyruk/senaryo-defteri.md:615 (K-010 kapıları çıktı). İcra: kaynak satırlarına damıtma turunda "KAPANDI + pointer" damgası.

---

## (F) VERİ YAPISI — envanterin makine-yüzü (world-model §2 kuralına uyum)

**Grain bildirimi:** `karar-borcu` süreci — **1 satır = 1 açık karar kalemi** (Salih hükmü ya da Carvis icrası bekleyen). Kapanınca `karar` sürecine (bus matrix v1: "1 satır = 1 hüküm") bir hüküm satırı olarak akar; bu tablo hükmün ÖN-DURUMUdur. Bus matrix satırı önerisi = **KB-07** (Katman-1; tablo Katman-2 olarak kuruldu, kanon satırı senin).

**Boyutlar (conformed):** zaman (`kayit_tarihi`, `snapshot_tarih/sha`) · dosya (`karar_borcu_kaynak.dosya_id` → `dosya`/`kayit` tabloları; pointer `kayit_id`'ye bağlanır — 154 pointer'ın 133'ü mevcut `kayit` satırına eşleşti, kalan 21'i baglam.sqlite'ın 08-15 snapshot'ından SONRA yazılmış/kaymış satırlar [08-16 dosyaları + kapsül] — `baglam-tablo.py` yeniden koşunca eşleşir) · katman (1/2) · küme (S1…S7, I, KP) · anahtar (`tur`, `masa_yolu`).

**Dosyalar:**
- `veri/karar-borcu.jsonl` — gerçek kaynak (izlenir, ~35 KB). Alanlar: `borc_id` (kararlı anahtar; KB-nn Salih · İB-nn Carvis · KP-nn kapandı-paketi) · `baslik` · `kume` · `tur` · `katman` · `karar_sahibi` · `durum` · `kayit_tarihi` · `kaynak[]` (dosya:satır) · `secenekler` · `oneri` · `bagimlilik[]` (borc_id) · `kapanis_kaniti` · `masa_sirasi` · `masa_yolu` · `yururluk_aninda` · `icra_borcu` · `not` · `birlesik[]` (tarayıcı geçici id'leri — köken izi).
- `tools/karar-borcu-tablo.py` — yükleyici (stdlib; şema doğrulama + pointer topraklama FAIL-LOUD + `karar_borcu`/`karar_borcu_kaynak` tabloları + `v_karar_borcu_ozet` görünümü + `veri/gorunum/v_karar_borcu.csv`). Koşum: `python3 tools/karar-borcu-tablo.py --snapshot 2026-08-16` (deterministik; snapshot tarihi açık verilir). Çıkış 3 = kırık pointer var.
- `veri/gorunum/v_karar_borcu.csv` — izlenen gold görünüm (küçük).

**Örnek sorgular (sqlite3 veri/baglam.sqlite):**
```
select kume, durum, count(*) from karar_borcu where katman=1 group by 1,2;          -- küme×durum
select borc_id, baslik, yas_gun from karar_borcu order by yas_gun desc limit 10;      -- en yaşlı borçlar
select b.borc_id, k.dosya_id, k.satir, k.satir_metin from karar_borcu b join karar_borcu_kaynak k using(borc_id) where b.borc_id='KB-14';
select * from v_karar_borcu_ozet;
```

**Güncelleme kuralı (öneri, deneysel):** masa hükmü → JSONL satırında `durum` değişir + `kapanis_kaniti` = defter satırı pointer'ı; kapananlar 30 gün sonra KP paketine iner (silinmez — m.8). Pointer kayması: kaynak dosyalar değişince satır numaraları kayar; yükleyici snapshot SHA damgalar, F2 dökümü (`karar_borcu_kaynak.satir_metin`) hangi satırın kaydığını gösterir. **Damıtma (KB-37) bu dosyaların satırlarını kaydıracak → damıtma öncesi bu snapshot commit'li kalsın, sonra pointer'lar yeniden çözülür (1 koşum).**

**Neden bu şekil (Opus'un plan cümlesiyle uyumlu, ama ölçülmüş):** insan-yüzü rehber tek başına 3. masada yeniden yazılır (L8/K2 emsali: her masa kendi hazırlık dosyasını sıfırdan kurdu, tekrar); makine kaydı satır-başına köken izi taşıdığı için bir sonraki masa `durum!='kapandı'` sorgusuyla açılır. Çift muhasebe (şema-sıkıştırma ilkesi): sorgu-anı ↔ depo aynı satırdan türer.

---

## (G) KAPSAM NOTU / KÖR NOKTALAR (dürüstlük şartı)

- **Taranan kaynaklar:** kuyruk/senaryo-defteri.md (161 KB — işaretleyici grep + hedefli okuma; 07-30(7) ARIZA KAYDI bloğu s.232-334 yüzeysel) · kuyruk/masa-gundemi-2026-07-30.md (md.1-49 tamamı KAPANDI — yalnız artıklar) · masa-gundemi-K2 · m37-taslak (A2-A6 icra adımları taranmadı) · pozitif-karsilik-borclari · core/durum-kapsulu.md + core/pano.md · build-tartisma-notlari · fikir-kutusu.md + kuyruk/skill-fikir-kutusu.md · kuyruk/gelen-*.md (8) · KILAVUZ.md (grep) · cc/pipeline-2026-08-1x (4) · cc/karar-onerisi hat6 · cc/rapor-2026-08-16-1 (E-blokları) · cc/rapor-2026-08-15-{1..5,8,9} (yalnız Salih/karar/şerh bölümleri) · vardiya-teslim 08-12/14/15 · spec-kit raporu · skill-şeması test-turu · cc/defter (08-1x) · wiki/README kuyruk · core/{world-model,skill-uretim,halusinasyon,sema-sikistirma,baglam-anahtar} (grep). **Taranmayan:** ogrenme/, arşiv klasörleri, 08-11 öncesi vardiya teslimleri, utopik-havuz, okuma-defteri.
- **Kapanış-kontrolü grep tabanlıdır** — yanlış-negatif riski: bir kalem defterde/commit'te kapanmış olup burada açık görünebilir (özellikle S5 eski masa artıkları). Bu yüzden C.0'a ek olarak her kalemin masa yolu TEYİT içerir; senin "bu kapandı" beyanın kanıt sayılır (KP'ye iner, pointer'la).
- **Kapsül-satırı bayatlığı:** "A1 hükmü" (KB-33) 08-12 defter kaydına göre kapı olmaktan çıkmış görünüyor ama kapsül 08-15'te hâlâ listeliyor — kapsül SNAPSHOT'tır (ingest v2 ilkesi), gerçek kaynak defter; masa teyidi bunu çözer.
- **Kaynak pointer'ları 08-16 01:36 HEAD `90bb53d` snapshot'ına göredir;** seans-3/6 kapanış commit'leri (01:01, 01:16) tarama sırasında geldi — kapsül pointer'ları yeniden doğrulandı (154/154 satır metni okundu). Sonraki değişiklikler kaydırabilir; yükleyici FAIL-LOUD.
- **Bütçe sapması:** tarama 552k token (hedef ~150-250k). Neden: senaryo-defteri + masa gündemi büyük ve yoğun; işçilere "kapanış-kontrolü için repo-genelinde grep" verildi (doğruluk için tercih, maliyeti ikiye katladı). Kısıntı rejimine aykırı — kayıt düşüldü.
- **Ölçülmeyen:** ana döngü token'ı [?]; Salih okuma süresi (L8 dosyası 36 KB'a karşı bu dosya ~52 KB) — beklenen okuma 25-40 dk [?].
