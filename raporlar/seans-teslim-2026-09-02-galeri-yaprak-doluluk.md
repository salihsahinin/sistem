# Seans teslim — galeri-sıralama: ağaç yüzeyi sürüm-bağımsızlaştırma + yaprak doluluğu (2026-08-31 → 09-02)

**Hat:** jarvis-dışı iş şeridi (m.15 / md.49 — Otonet galeri-scoring).
**Yüzey:** Claude Code masaüstü, ana-sıra, Opus 5.
**Çalışma alanı:** `kuyruk/galeri-siralama/` — **COMMIT'LENMEZ** (Karar 73 EK, `.gitignore:39`).
Bu rapor o klasörün dışına çıkan tek kayıttır ve yöntem düzeyindedir.
**Devir:** `cc/devir-2026-09-02-opus-galeri-yaprak-doluluk.md` (Fable'a).

---

## Bugün gerçekten ne değişti

### 1. `05_agac_html.py` sürüm-bağımsızlaştırıldı (v1'e sabit kodluydu)

Betik `model.cbm` + `veri/` + sabit test tarihi `2026-07-31` + sabit örnek lot `IH0120-L01`
ile çalışıyordu; metinlerde "552 ağaç", "64 yaprak", "64 kolon" gömülüydü. Yapılanlar:

- `ortak.py` bayrakları (`--v2 --uzun --tohum`) + yeni `--model` / `--veri` / `--lot` bayrakları.
- **Bölme artık `03_egit.py` ile ortak** oransal %68/%12/%20 kuralı. Sabit tarih uzun takvimde
  test kümesini 1.420 yerine 320 lot gösteriyordu — ekip notu §15'teki aynı hata sınıfı.
- Örnek lot test kümesinden deterministik seçiliyor; ağaç/yaprak/kolon/aday sayıları modelden türüyor.
- Sözlük sekmesi modelin gerçek feature listesine göre süzülüyor (64 → 63 kolon).
- Bayraksız koşum eski davranışını korur; çıktı adı sürüme göre ayrışır.

**Sözlük sekmesi öneme göre yeniden dizildi** (Salih isteği): sıra no + SHAP-benzeri önem çubuğu
(`PredictionValuesChange`, toplam 100) + bölme sayısı; aile süzmesinde de sıra korunuyor,
sayaç satırı seçili ailenin toplam önem payını veriyor.

### 2. Yaprak doluluğu masası — ölçüldü, teşhis kondu, hedef revize edildi

Ayrıntı ve tablolar ekip notunda: `kuyruk/galeri-siralama/bulgular-model-eksikleri.md` §17.
Özet:

- **Boş yaprakların %26,6'sı yapısal olarak imkânsız** (aynı kolonun iki eşiği aynı ağaçta →
  çelişkili bit kombinasyonu). Mock data ile ASLA dolmaz. Hedef "her yaprakta ≥20" değil
  **"mümkün her yaprakta ≥20"** olarak kurulmalı.
- **`min_data_in_leaf` bu modelde ölü parametre:** doğrudan test edildi, `SymmetricTree`'de
  yok sayılıyor (aynı boş yaprak sayısı). Belgeye değil çıktıya bakılarak bulundu.
- **4× mock veri** (3 yeni tohum evreni, 1.611.460 satır) + **derinlik araması**:
  %61,4 → **%96,25** (≥20 satırlı yaprak), **kalite bedeli 0,5 puan** (HR@1 0,711 → 0,706).
- **Asıl kaldıraç derinlik, veri değil:** 4× veri +13 puan, derinlik 6→3 +22 puan.
  Kombinasyon sayısı 2^derinlik ile üstel büyüdüğü için veri katlamak bir seviyeyi telafi etmiyor.
- Test **ayrı evrende** (tohum 77) yapıldı: hem yeni evren hem zaman-ileri.

**Seçilen model:** `model_yogun_d3.cbm` (1.999 ağaç × 8 yaprak).
**Yüzey:** `agac-semasi-model_yogun_d3-veri2u_s77.html` (4,20 MB, 1.480 test lotu, açıldı).

### 3. Silinenler

`zaman-testi.html` + `11_zaman_testi.py` + `12_zaman_html.py` — Salih istemediği bir işti
(yanlış anlama: "ağaç yüzeyi yeni modelle" yerine "zaman-ileri bozulma testi" üretilmişti).
Ara çıktı `zaman-testi-model_v2u.json` duruyor (yetim, silme kararı Salih'te).

---

## Hangi karar verildi (kaynak + gerekçe + geri-açma)

**Katman-1 kanon kararı YOK.** Bu şerit jarvis-dışı iş; kararlar iş-tarafı tasarım kararları:

1. **Doluluk hedefi "mümkün her yaprakta ≥20" olarak kuruldu** (Carvis ölçümü, Salih'e bildirildi).
   *Gerekçe:* yapısal imkânsız yapraklar ölçülü bir gerçek (%26,6); "her yaprak" hedefi
   matematiksel olarak ulaşılamaz. *Geri-açma:* ölçüt `13_yaprak_doluluk.py`'de tek yerde.
2. **Nihai model derinlik 3** (d6/d5/d4/d3 arasından). *Gerekçe:* doluluk %96,25, kalite bedeli
   0,5 puan. *Geri-açma:* dört model de diskte (`model_yogun_d{3,4,5,6}.cbm`), HTML tek komutla
   yeniden üretilir.
3. **Bölme mantığı tek kurala bağlandı** (05 → 03 ile ortak oransal bölme).
   *Gerekçe:* §15'te aynı hata metrikleri 4× yanlış göstermişti. *Geri-açma:* yok, düzeltme.

---

## Hangi fikir ADAY kaldı (karar DEĞİL)

- **Derinlik 2 denemesi** — %99'a çıkarabilir ama model etkileşim öğrenemez; koşulmadı.
- **Gerçek veride doluluk ölçümü** — mock çoğaltma orada yok, tek kaldıraç derinlik olacak.
- **`zaman-testi-model_v2u.json`'un silinmesi** — Salih tetiği bekliyor.
- **2,5 GB türev veri temizliği** — `veri2u_s4{3,4,5}` + `veri2u_kalabalik` yeniden üretilebilir.

---

## Sonraki ilk iş

1. **YARIM KALAN GÖREV — Salih'in 2. emri:** yeni trim deneyi. Betikler yazıldı
   (`16_yeni_trim.py` + `17_yeni_trim_html.py`), koşum makine yeniden başlayınca kesildi.
   Devir dosyasında tek komutluk koşum reçetesi var.
2. Ekip notu §17 gerçek veri geldiğinde doluluk ölçümüyle güncellenir.

## Yeniden-açma koşulu

Gerçek 3 matris CSV'si geldiğinde (Karar 83 E1 beklemesi sürüyor) bütün hat yeniden koşulur;
mock çoğaltma adımı (`14_veri_birlestir.py`) o zaman DEVRE DIŞI kalır.

---

## Boyut / hijyen

- boyut-tetiği: defter 56,5/48 · kutu 22,3/20 · KILAVUZ 16,8/16 · pano 12,2/12 (08-31'den devren açık).
- Galeri klasörü diski: **2,5 GB** (türev, gitignore'lu, tohum 42/43/44/45/77 ile yeniden üretilir).
- araç-çıktısı aşımı: yok (uzun çıktılar dosyaya yazıldı, bağlama pointer'la girdi).
- **uzun-koşum: max bağlam 299.952 (199 tur 128K üstünde; 238 tur, çıktı 309.213 token)** — bu oturum ölçülen en uzun koşum ailesinden; eğitim beklemeleri turların çoğunu oluşturdu.
- kural-eşiği: 19 / 100 (OK) · silver-sağlık kapısı ÇIKIŞ 0 (2 WARN: T-C3 ılık kalıntı 109, T-C6 kalibre-edilmemiş sabit 1; ADAY: YETİM 301/eşik 351, KAPANDI 97, SÜPERSEDE 4, T-A çift 500/6.692) · skill-eşik: 6 çift, yeni-pencere sapması 0 · bayat-çekim: kuyruk 0 aday, çekim 0/3.

## Hasat kontrol listesi (Karar 61)

1. **Kalıcı kural/karar adayı ingest'e girdi mi?** Evet — üç iş-tarafı karar teslim raporunda, kanon adayı yok.
2. **Açık pipeline/manifest T beyanı aldı mı?** Bu şeritte manifest kullanılmadı; yarım kalan birim devir §2'de SAHADA damgasıyla duruyor.
3. **Tahmin↔gerçek kaydı (KB-02) ambara düştü mü?** Ajan/Workflow koşumu YOK (bu oturum tamamen tek-oturum icra); skill-eşik koşuldu, sapma 0.
4. **Paralel oturum / devir notu var mı?** Evet — `cc/devir-2026-09-02-opus-galeri-yaprak-doluluk.md` (Fable'a).

## Özütler (hasat)

1. **Bir parametrenin belgesi değil çıktısı bağlar:** `min_data_in_leaf` CatBoost belgesinde var, simetrik ağaçta ölü — iki koşumun çıktısı karşılaştırılarak bulundu.
2. **Kombinasyon uzayı üstel büyür, veri doğrusal:** 4× veri bir derinlik seviyesini telafi etmiyor; doluluk problemi veri değil yapı problemi.
3. **Boşluğun bir kısmı doldurulamaz:** yapısal imkânsız yaprak kavramı, "her X için veri topla" hedeflerinin genel sınırı — hedefi "mümkün her X" diye kurmak gerekiyor.
4. **Sabit kodlu bölme mantığı sessiz metrik hatası üretir:** aynı hata bu klasörde ikinci kez çıktı (§15, sonra 05_agac_html.py); tek kural tek yerde.
5. **Yanlış anlaşılan emir maliyeti:** zaman-testi hattı baştan sona üretilip silindi — teslimden önce "hangi HTML" tek cümleyle teyit edilmeliydi.

## Wiki-delta

- `wiki/` kuyruğuna aday: **"yapısal imkânsız yaprak"** (simetrik ağaçlarda kombinasyon çelişkisi) — ölçüm yöntemiyle birlikte; kaynak `kuyruk/galeri-siralama/13_yaprak_doluluk.py`.
