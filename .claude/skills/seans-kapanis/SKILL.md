---
name: seans-kapanis
description: Carvis'in JARVIS vardiya-KAPANIŞ ritüelini koşar. Salih "seans bitimi" (standart tetik; jarvis klasöründen açık oturumda BU ritüel — staj işareti değildir), "kapat", "bitiriyorum", "vardiyayı kapat" dediğinde ya da oturumu bitirme sinyali verdiğinde HER YÜZEYDE çalışır; bağlam-şişmesinde Carvis kendisi de önerir (V11). Kapanış selamı zaman işareti DEĞİLDİR ve tek başına tetik DEĞİLDİR (emekli tetikler: `core/baglam-anahtar-kaydi.md`). Teslim raporu + hasat + ingest + kapsül + commit/push üretir; push'suz gün SAYILMAZ (m.9). KULLANILMAZ; açılışta ("seans başı" → seans-acilis), ara özette ("hizala"), JARVIS-dışı vedalaşmada ve STAJ OTURUMLARINDA (staj klasöründen açılan oturum — ayrım klasörle, Salih 08-15); staj kapanışı staj-kapanis ritüelidir, jarvis kanonuna yazmaz, teslim/kapsül/push üretmez.
---

# Seans bitimi — vardiya kapanışı (Carvis, v0.3-deneysel-m29 — ad: vardiya-kapanis → seans-kapanis + uyucam-sınıfı tetik emekliliği [Salih Katman-1 08-15]; v0.2: staj kapısı 08-12)

## 0. STAJ KAPISI (önce bu)
Oturum STAJ KLASÖRÜNDEN açıldıysa ∨ beyan AÇIKÇA staj bağlamındaysa → BU RİTÜEL KOŞULMAZ. **AYRIM KLASÖRLE yapılır (Salih 08-15): "seans bitimi" cümlesi tek başına staj işareti DEĞİLDİR — jarvis oturumunda jarvis kapanışıdır.** ZAMAN-KAYMASI FRENİ: kapanış sözünden gece/gündüz çıkarımı yapılmaz; zaman yalnız sistem kaynağından. Staj oturumu jarvis kanonuna YAZMAZ (md.49); kapanışı staj klasörünün kendi ritüeli (günlük toparlama + yerel checkpoint) yapar. Tek cümleyle beyan et, staj kapanışına geç.

Kapanış = hafıza yazımıdır: bir sonraki vardiya yalnız burada yazılanı devralır. Bayat kapsül boş kapsülden kötüdür (V4). Şablonların kaynağı `core/sablonlar/` — çelişkide şablon dosyası kazanır.

## 1. Yüzey + hat tespiti
- Kanon-yazım kanalı var mı? (PC: doğrudan · bulut: origin-klon + PAT ile commit/push; mount'ta git komutu YASAK — yazım klondan push'lanır, mount'u senkron scripti eşitler.)
- Kanal YOKSA: tam ritüel koşulamaz → kapanış notunu "HAM FİKİR / PC'de ingest edilecek" damgasıyla üret, Salih'e açıkça söyle: **bu gün m.9 gereği HENÜZ SAYILMADI**, ana vardiya devralınca sayılır.
- Hat: prototip mi PortRisk mi? Paralel-vardiya senkron kuralı: yalnız KENDİ şeridinin dosya/satırlarına dokun; iki oturum açıksa push öncesi pull zorunlu.

## 2. Teslim raporu (`core/sablonlar/vardiya-teslim.md` — beş soru)
`raporlar/vardiya-teslim-YYYY-MM-DD-<hat/etiket>.md` dosyasına: bugün gerçekten ne değişti · hangi karar verildi (kaynak+gerekçe+geri-açma) · hangi fikir ADAY kaldı (karar değil) · sonraki ilk iş · yeniden-açma koşulu.

## 3. Hasat (`core/sablonlar/hasat.md`)
Özütler (3-5, birer satır) · **wiki-delta**: güncellenecek/açılacak sayfa → `wiki/README.md` kuyruğuna (yazım sonraki oturumlara yayılır; mevcut sayfaya tuzak çıktıysa Gotchas'a DOĞRUDAN işle) · verilebilir miydi (V20, çift-yönlü kapasite verisi) · token×zaman etiketi (V28 hammaddesi). Damga yalnız gönüllü beyanla; beyansızlık düşürmez (m.33).

## 4. İngest turu (m.34 katmanlı: ham dışta, damıtılarak içe)
- **ŞEMA (08-14 AKTİF):** her kayıt `core/ingest-semasi.md` sözleşmesiyle işlenir — 5-alanlık zarf + kapalı tip + 4-soru triyajı (NOOP/UPDATE/GEÇERSİZ-KIL/ADD; silme yok, geçersiz-damgası); devir dosyası bütçesi ≈1-2k token; sınıflandırılamayan kayıt → `kuyruk/SINIFLANDIRILAMADI.md` (sessiz düşürme yasak); sayaçlar teslim raporuna (giren/NOOP/UPDATE/geçersiz/ADD/DLQ).
- Oturumda doğan kalıcı-aday fikirler → `fikir-kutusu.md` (fikir-kutusu-adayı formatı).
- Ölçek-eşiği üstü kararlar → `kuyruk/senaryo-defteri.md` (m.37 kaydı: modeller+seçim+gözlem alanı).
- Karara bağlanmamış bulgular → `kuyruk/build-tartisma-notlari.md`. Silme YOK — bayatlayan arşive iner (m.8).
- Model değişimi yaşandıysa: ingest kanona DEĞİL şerhli klasöre (`model değişikliği ile.../ingest-YYYY-MM-DD.md`) — KILAVUZ protokolü.

## 5. Kapsül tazeleme (`core/durum-kapsulu.md`)
Üzerine yazılır, arşiv değildir. Yalnız kendi şeridinin satırları; güncelleme satırı + "şu an" + borçlar + "sonraki ilk iş". Bütçe: **≤8KB VE ≤40 satır** (SessionStart hook `1,40p` sert-kapısı — aşan kuyruk sessizce düşer).

## 6. Boyut-izleme tek bakış (İMZALI kural 07-22)
Sıcak dosya bütçeleri: kapsül 8KB/40sat · pano 12KB · fikir-kutusu 20KB · senaryo-defteri 48KB · CLAUDE.md 8KB · KILAVUZ 16KB. Aşım hata değil TETİK: teslim raporuna "boyut-tetiği: <dosya>" satırı düş; damıtma ilk boş vardiyada Salih-imzalı planla.

## 7. Commit + push (m.9 — proof-of-work)
Karar başına AYRI commit · İngilizce mesaj · [damıtma]/[icra] etiketi (V5, m.10). Push origin'e; bulut yüzeyde klondan. Push başarılıysa kapanış beyanı: **"gün sayıldı"** + insan-yüzü tek satır (m.18: ▸ Kapandı · Sonraki ilk iş · Açık borç). Push atılamadıysa bunu GİZLEME — gün sayılmadı de, nedenini yaz.

## Gotchas
- **Kapsül-şişirme:** kapanış heyecanıyla kapsüle tarih anlatma — tarihçe commit'lerde ve teslim raporlarında yaşar; kapsül yalnız "şu an + sıradaki".
- **Çift-şerit çiğneme:** diğer hattın kapsül satırına/teslim dosyasına dokunma (07-12 senkron kuralı).
- **Sessiz push arızası:** push hata verirse "commit attım" diye geçme; m.9 push ister, commit değil.
- **Övgü kapanışı:** "harika bir gündü" merci yok (m.7) — kapanış çıplak veridir.
