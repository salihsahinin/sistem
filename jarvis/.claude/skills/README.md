# Skill hazinesi kataloğu (Karar 96 F6 seçim-isabeti; tavan yok; 2026-09-15)

*Amaç: hazine büyürken doğru anda doğru skill'in seçilmesini korumak. Sütunlar: ad · tür (T-R ritüel / T-O orkestratör / T-Y yan-etkili / T-Ü üretici) · icra türü (hangi iş akışı çağırır) · description (tetik cümlesi, özet). Her yeni skill bu tabloya satır ekler (skill-kapisi P3). Deneme skill'leri `kuyruk/skill-deneme/`. Metadata bütçesi ~100 token × skill sayısı, ölçülür, engel değil.*

*Karar 117 (2026-10-17): skill'ler deterministik adımda önce Rust ikilisini çağırır (`../target/release/<araç>`; Python yedek), kural hükmünü yeniden anlatmaz, `lean/Kanon/<Modül>.lean`'e pointer verir; tüzük ve `core/` parçalıdır (`Read` hook'u kalanı ekler, Bash'te `baglam genislet`).*

| ad | tür | icra türü | description (özet) |
|---|---|---|---|
| `atlas-kosum` | T-O orkestratör | araştırma (m.40b) | Araştırma sorusunu dik alan-ailelerine bölüp paralel Atlas ajanları koşturur — m.40b v0.2 diyalektiği: çoklu-bağımsız tez → hedefli antitez (¬) → maskeli hakeml |
| `karar-masasi` | T-Ü üretici | karar sunumu (Lavish masası; ≥2 hüküm) | bekleyen hükümleri deterministik DaisyUI masası olarak üretir (İB-88 P2 09-15: script + şablon + tersine çıkarıcı + test 12/12, masa-12 eşdeğerlik; P3 topraklama bekliyor) |
| `celiski-kapisi` | T-Ü üretici | karar öncesi m.16 | Yeni karar/kural/kanon-değişikliği önerisinde kanonu tarar; çelişki varsa karar **alınmadan önce** çelişki + artı/eksi + plan raporu sunar (m.16). Kullan: "çelişki  |
| `damitma` | T-Y yan-etkili | ingest/damıtma turu | Kanonun damıtma/ingest turunu koşar (S-E); kuyruk/gelen dosyalarını ingest v2 triyajından geçirir, boyut-FLAG'li sıcak dosyaları bütçeye indirir (arşiv-pointer) |
| `gorev-emri-derleme` | T-Ü üretici | işçi/lider emri derleme · **devir emri A1** (md + lojik blok → `devir-md2json`, İB-93 09-16) | Salih'in araştırma/görev beyanını künyeli, görev-fonksiyonu-şablonlu ajan emrine derler (S-K). Tetik; "araştırma emri yaz", "görev emri derle", "emri hazırla",  |
| `halusinasyon-engelleyici` | T-Ü üretici | olgusal/atıflı çıktı üretimi | Halüsinasyona müsait görevin **çıktısını** doğrulama zinciriyle üretir; her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR etiketli, önce H derecesi hesaplanır (Rust `derece`; hüküm `Kanon.Halusinasyon`) |
| `karar-hatti` | T-O orkestratör | karar üretimi (ölçek-eşiği üstü) | Ölçek-eşiği üstü kararı **baştan sona** işleyen orkestratör — çocuk skill'leri sırayla çağırır, kendisi iş yapmaz: (1) celiski-kapisi (m.16; çelişkide **durur**) → (2)  |
| `karar-kaydet` | T-Y yan-etkili | karar kaydı (yan-etkili) | Verilmiş bir kararı senaryo-defterine standart blokla yazar ve ayrı commit atar (S-J; karar-hatti tamamlayıcısı). **yalnız** elle tetik; Salih ya da seans akışı "ka |
| `karar-modeli` | T-Ü üretici | karar üretimi (3 model) | Ölçek-eşiği üstü karar/tasarım sorusu için **farklı** matematiksel temelli 3 karar modeli üretir — en az biri karşıt-temelli, hepsi token×zaman×kalite×risk eksenler |
| `lojik-ceviri` | T-Ü üretici | kural/emir Lean 4 koduna (S-D v2, Karar 114) | Doğal-dil talimatı/kuralı Lean 4 koduna çevirir: atomik önermeler → `structure`, dallar → `inductive` + karar fonksiyonu, done-yüklemi → `Bool`, özellikler → `theorem`; `lake env lean` ile derlenmeden teslim edilmez |
| `pipeline-kosum` | T-O orkestratör | proje-ölçekli görev icrası | Kun-Chen formatlı görev pipeline'ını kurar ve uçtan uca yürütür (P-1); manifest + emir → scout → rapor → sentez → ship → teslim, tüm durum diskte (restart-proof |
| `seans-acilis` | T-R ritüel | ritüel: seans başı | Jarvis'in (ajan; eski ad Carvis) depo seans-AÇILIŞ ritüelini koşar. Salih "seans başı" (standart tetik), "seansı devral", "seans aç", "oturuma başlayalım" dediğ |
| `seans-kapanis` | T-R ritüel | ritüel: seans bitimi | Jarvis'in (ajan; eski ad Carvis) depo seans-KAPANIŞ ritüelini koşar. Salih "seans bitimi" (standart tetik; jarvis klasörü oturumunda BU ritüel), "kapat", "bitir |
| `sinav-grill` | T-Ü üretici | öğrenme: Salih tetikli sınav | Salih'in bir plan/karar/konu anlayışını adversarial Sokratik sorgulamayla sınar (S-I); tek-tek sorular, karar-ağacı inişi, [S]/[O]/[T] haritası + bulanık-blok l |
| `skill-kapisi` | T-O orkestratör | skill üretimi/evrimi | Skill **adayını** (fikir, kutu satırı, taslak ya da mevcut skill) kapı-ağacından yürütür (K0 **gerek** → K1 **değer** → **inşa** → K2 **topraklama** → K3 **biçim**+**tür**); GEÇTİ/BEKLET/O |
| `wiki-sayfa-yaz` | T-Y yan-etkili | wiki üretimi | Wiki-delta'dan ya da kuyruk adayından standarda uygun wiki sayfası üretir (W-1); 6-blok şablon + index + [[link]] turu. Tetik; "wiki'ye yaz", "sayfa aç", "wiki  |
| `yol-planla` | T-Ü üretici | proje planı | Proje-ölçekli görevi (durum,zaman)-düğümlü senaryo-grafa döküp topoloji + maliyet-tavanı + onarım kuralını **yol-planı** bloğu olarak üretir (S-Ü); planı üretir, KO |
| `ogren` | T-R ritüel | öğrenme yan-oturumu ("seans başı, <şerit>", "öğret", "kutu N'den devam") | dört fazlı ders akışı + oturum protokolü (İB-89 09-15: deneme v0.1 → hazine v0.2; K4 kanıt H1-H3 + G1; P3 = ilk canlı koşum v0.2) |
| `emekli-anahtar-cascade` | T-Y yan-etkili | ad/tetik/kavram emekliliği ("X'i emekli et", "X yerine Y", "cascade koş") | anahtar kaydı satırı + deterministik yayılım `tools/anahtar-cascade.py` (kaydet · tara · uygula --onay · readme); İB-90 09-15, ilk canlı koşum ajan-adi (Carvis→Jarvis) |

Toplam 19 skill (deneme alanı boş; `ogren` 09-15 hazineye geçti) · üretim sırası (Karar 96 M5): karar-masasi ✓P2 → ogren evrimi ✓P2 → acilis-kapilari ✓ → cascade ✓P2 → KILAVUZ→skill-kapisi ✓ (İB-92, references/) → friday-devir ✓ (İB-93 09-16, İB-93) → …

## Dış hazineler
- alan ajanlarının ortak `ogren` kopyası `../sablonlar/skills/ogren/` (uygulama + terminal görsel yolu, 2026-10-16).
- staj reposu `~/staj başlangıç/.claude/skills/` (staj-acilis, staj-kapanis) — jarvis'e yalnız ad; içerik md.49.
