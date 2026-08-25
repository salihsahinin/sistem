# paralel-oturum-protokolu

**Üst blok:** Aynı anda açık birden çok Jarvis oturumu (terminal + masaüstü uygulaması + telefon) birbirinin işini bozmasın diye 4 kural. Salih imzası 2026-08-17 masa (KB-08 + KB-09 + KB-10 H4); kaynak vakalar: 08-12 (Docker motoru/kaynak çakışması), 08-15 (vaka-2, mükerrer koşum), 08-16 (vaka-3, 518k mükerrer workflow) · 08-21 (vaka-4, resume-körlüğü: numara çakışması + pointer kırılması). Durum: KURAL (deneysel damga m.29 — eşikler ilk 10 seansta kalibre). Uygulama: `seans-acilis` §1.4-1.5, `seans-kapanis` §7, KILAVUZ "Paralel seans protokolü".

**Çekirdek — 4 kural:**
1. **Canlı-oturum kapısı (açılış + HER RESUME — Salih imzası 08-21, Karar 57):** son commit ≤15 dk ∧ kapsülde o seansın kapanış kaydı yok → "paralel-oturum şüphesi" beyanı; diğer oturumun manifestte SAHADA görünen işi ikinci kez koşulmaz, onun dosyalarına yazılmaz; hat paylaşımı Salih'e tek soru.
   *Resume eki (vaka-4, 08-21):* uzun oturumda özet-yenileme/dönüş sonrası ilk cevaptan önce kapı YENİDEN koşar (`git log -5` + kapsül başı) — vaka-4: resume-körlüğü seans-11↔12 karar-numarası çakışması (51-53 çift kullanım) + damıtma sonrası 14 kırık pointer üretti; onarım [ariza] f60d84e..bc4afd5.
2. **Koşum-önü manifest kapısı:** Workflow/atlas/pipeline açmadan önce `cc/pipeline-*.md` manifesti + `git log -15` okunur — iş zaten koşmuş/koşuyorsa devralınır, yeniden koşulmaz.
3. **Paylaşılan kaynak freni:** servis/konteyner/port/DB/soket açmadan önce mevcut durum okunur (`docker ps`, `lsof -i :PORT`); çakışma varsa KURULMAZ, bildirilir; mevcut olan kullanılır. **Motor kapatma freni:** paylaşılan daemon (Docker vb.) yalnız diğer hatta iş kalmadığı doğrulanınca kapatılır.
4. **Commit freni (H4):** başka jarvis oturumu canlıyken `git add -A` YASAK; her oturum kendi dosyalarını yol vererek commit'ler (`git add <yol>`); ekleme-esaslı yazım (yeniden oku → altına ekle) korunur.

**Neden:** paralel seans Jarvis'in kendi kararı (m.36 rev.); tek çalışma ağacı + iki oturum = birinin yarım işini diğerinin yayımlaması, mükerrer koşum (08-15/16 toplam ~549k token), sessiz kaynak bozulması. Senkron elle yürür (K-009 otomasyonu açılınca otomatikleşmesi beklenir).

**Gotchas:** yanlış-pozitif (sen kapatmışsın ama commit taze) → tek soru yeter, iş durmaz · staj oturumu ayrı klasör/ayrı ritüel (md.49) ama paylaşılan makine kaynakları (Docker/port) bu kurala TABİ · telefon oturumu yan-oturumdur, kanon yazmaz (m.41) · **araç-kaynaklı dal değişimi (vaka 08-21 s13):** diğer oturumun [[no-mistakes]] koşumu working tree'yi dala geçirip merge yürütebilir (UU çakışma + staged dosyalar) — bu hâldeyken commit atmak merge'i yabancı adına tamamlar ya da yanlış dala yazar; git-yazma işlemleri ağaç main'e dönüp temizlenene dek BEKLETİLİR, sonra pathspec'li commit (`git commit -- <yol>`) diğer oturumun stage'ini dışarıda tutar · manifest-kapısı grep'i varyant-toleranslı yazılır (tire/boşluk: `ATLAS[- ]?V59` vakası 08-21 — tireli desen boşluklu başlığı ıskaladı, kısmi mükerrer koşum; KURAL-ADAYI Salih'te).

**Süpersede zinciri:** `PARALEL-VARDIYA-ILK-DENEME.md` (07-12 ilk deneme talimatı) → bu sayfa (arıza kayıtlarıyla kural).

**Bağlantılar:** [[ingest-semasi]] · [[pointer-sistemi]] · kaynak vakalar: `kuyruk/gelen-2026-08-12-paralel-oturum-kaynak-cakismasi.md` · `kuyruk/gelen-2026-08-15-paralel-oturum-vaka-2.md` · `kuyruk/gelen-2026-08-16-paralel-oturum-vaka-3.md` (üçü İNGEST EDİLDİ 08-17). · [[silver-saglik]] (karşı-link 08-22) · [[dil-secimi]] (karşı-link 08-26) · [[anakronizm-freni]] (karşı-link 08-26)
