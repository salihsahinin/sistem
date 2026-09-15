# Skill hazinesi kataloğu (Karar 96 F6 seçim-isabeti; tavan yok; 2026-09-15)

*Amaç: hazine büyürken doğru anda doğru skill'in seçilmesini korumak. Sütunlar: ad · tür (T-R ritüel / T-O orkestratör / T-Y yan-etkili / T-Ü üretici) · icra türü (hangi iş akışı çağırır) · description (tetik cümlesi, özet). Her yeni skill bu tabloya satır ekler (skill-kapisi P3). Deneme skill'leri `kuyruk/skill-deneme/`. Metadata bütçesi ~100 token × skill sayısı, ölçülür, engel değil.*

| ad | tür | icra türü | description (özet) |
|---|---|---|---|
| `atlas-kosum` | T-O orkestratör | araştırma (m.40b) | Araştırma sorusunu dik alan-ailelerine bölüp paralel Atlas ajanları koşturur — m.40b v0.2 diyalektiği: çoklu-bağımsız tez → hedefli antitez (¬) → maskeli hakeml |
| `celiski-kapisi` | T-Ü üretici | karar öncesi m.16 | Yeni karar/kural/kanon-değişikliği önerisinde kanonu tarar; çelişki varsa karar ALINMADAN ÖNCE çelişki + artı/eksi + plan raporu sunar (m.16). Kullan: "çelişki  |
| `damitma` | T-Y yan-etkili | ingest/damıtma turu | Kanonun damıtma/ingest turunu koşar (S-E); kuyruk/gelen dosyalarını ingest v2 triyajından geçirir, boyut-FLAG'li sıcak dosyaları bütçeye indirir (arşiv-pointer) |
| `gorev-emri-derleme` | T-Ü üretici | işçi/lider emri derleme | Salih'in araştırma/görev beyanını künyeli, görev-fonksiyonu-şablonlu ajan emrine derler (S-K). Tetik; "araştırma emri yaz", "görev emri derle", "emri hazırla",  |
| `halusinasyon-engelleyici` | T-Ü üretici | olgusal/atıflı çıktı üretimi | Halüsinasyona müsait görevin ÇIKTISINI doğrulama zinciriyle üretir; her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR etiketli, önce H derecesi hesaplanır (scripts/derece.p |
| `karar-hatti` | T-O orkestratör | karar üretimi (ölçek-eşiği üstü) | Ölçek-eşiği üstü kararı BAŞTAN SONA işleyen orkestratör — çocuk skill'leri sırayla çağırır, kendisi iş yapmaz: (1) celiski-kapisi (m.16; çelişkide DURUR) → (2)  |
| `karar-kaydet` | T-Y yan-etkili | karar kaydı (yan-etkili) | Verilmiş bir kararı senaryo-defterine standart blokla yazar ve ayrı commit atar (S-J; karar-hatti tamamlayıcısı). YALNIZ elle tetik; Salih ya da seans akışı "ka |
| `karar-modeli` | T-Ü üretici | karar üretimi (3 model) | Ölçek-eşiği üstü karar/tasarım sorusu için FARKLI matematiksel temelli 3 karar modeli üretir — en az biri karşıt-temelli, hepsi token×zaman×kalite×risk eksenler |
| `lojik-ceviri` | T-Ü üretici | kural/emir lojik forma | Doğal-dil talimatı/kuralı m.38 bağlaç setiyle (∧ ∨ ¬ → ↔) lojik forma çevirir (S-D); numaralı dallar, boolean done-yüklemi, niceleyici-sırası denetimi üretir. T |
| `pipeline-kosum` | T-O orkestratör | proje-ölçekli görev icrası | Kun-Chen formatlı görev pipeline'ını kurar ve uçtan uca yürütür (P-1); manifest + emir → scout → rapor → sentez → ship → teslim, tüm durum diskte (restart-proof |
| `seans-acilis` | T-R ritüel | ritüel: seans başı | Jarvis'in (ajan; eski ad Carvis) depo seans-AÇILIŞ ritüelini koşar. Salih "seans başı" (standart tetik), "seansı devral", "seans aç", "oturuma başlayalım" dediğ |
| `seans-kapanis` | T-R ritüel | ritüel: seans bitimi | Jarvis'in (ajan; eski ad Carvis) depo seans-KAPANIŞ ritüelini koşar. Salih "seans bitimi" (standart tetik; jarvis klasörü oturumunda BU ritüel), "kapat", "bitir |
| `sinav-grill` | T-Ü üretici | öğrenme: Salih tetikli sınav | Salih'in bir plan/karar/konu anlayışını adversarial Sokratik sorgulamayla sınar (S-I); tek-tek sorular, karar-ağacı inişi, [S]/[O]/[T] haritası + bulanık-blok l |
| `skill-kapisi` | T-O orkestratör | skill üretimi/evrimi | Skill ADAYINI (fikir, kutu satırı, taslak ya da mevcut skill) kapı-ağacından yürütür (K0 GEREK → K1 DEĞER → İNŞA → K2 TOPRAKLAMA → K3 BİÇİM+TÜR); GEÇTİ/BEKLET/O |
| `wiki-sayfa-yaz` | T-Y yan-etkili | wiki üretimi | Wiki-delta'dan ya da kuyruk adayından standarda uygun wiki sayfası üretir (W-1); 6-blok şablon + index + [[link]] turu. Tetik; "wiki'ye yaz", "sayfa aç", "wiki  |
| `yol-planla` | T-Ü üretici | proje planı | Proje-ölçekli görevi (durum,zaman)-düğümlü senaryo-grafa döküp topoloji + maliyet-tavanı + onarım kuralını YOL-PLANI bloğu olarak üretir (S-Ü); planı üretir, KO |

Toplam 16 skill · deneme: `ogren` (kuyruk/skill-deneme) · üretim sırası (Karar 96 M5): karar-masasi → ogren evrimi → acilis-kapilari → cascade → …

## Dış hazineler
- staj reposu `~/staj başlangıç/.claude/skills/` (staj-acilis, staj-kapanis) — jarvis'e yalnız ad; içerik md.49.
