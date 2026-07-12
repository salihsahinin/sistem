# Öneri Dosyası — Ingest/Katmanlı-Hafıza Şeması v1 (İMZASIZ TASLAK)

*2026-07-12, Carvis. K-015 madde 1. Kaynaklar: m.34 (katmanlı ingest) · V21 (dıştan içe + Salih'in 07-12 koşullu-geçiş detayı) · V9 (önem formülü) · V30 (iterasyon verimi) · Homebase havuz #9/#4 (pointer). Akış hattı gereği: bu dosya öneri aşamasıdır — Salih imzalarsa şema kanonlaşır, m.34'ün operasyonel eki olur. Tüm eşikler deneysel damgalı (m.29/V12).*

## 1. Katman haritası (mevcut dosyalara oturur — yeni klasör İCAT EDİLMEZ)

| Katman | Rol | Yaşadığı yer | Giriş bariyeri |
|---|---|---|---|
| **K3 — dış (ham giriş)** | her şey önce buraya | `fikir-kutusu.md` + `raporlar/` (vardiya teslimleri, mobil notlar, ajan raporları) | gürültü listesi (KILAVUZ; tek filtre bu) |
| **K2 — orta (damıtılmış)** | kavram/karar adayı | `wiki/` sayfaları + `kuyruk/` öneri dosyaları | aşağıdaki geçiş koşulu G1 |
| **K1 — iç (çekirdek)** | en önemli özütler; sıcak bağlamı besler | `core/` (tüzük · kapsül · pano) + `CLAUDE.md` | YALNIZ Salih imzası (m.31 Katman 1) + kaynak+gerekçe+geri-açma |
| **K0 — arşiv** | düşen her şey | `arsiv/` | silme yok (m.8); arşivden geri çıkış serbest (pointer korunur) |

## 2. Geçiş koşulları (Salih'in 07-12 ilkesi: dıştan içe, KOŞULLU)

- **G1 (K3→K2, damıtma):** madde şu ikisinden birini sağlayınca damıtılır — (a) bir karara/aktif işe fiilen dokundu (kullanım-tetikli, m.5 ile aynı ruh), ya da (b) ≥2 bağımsız kaynakta/oturumda tekrar etti (bu sabah V30+V21'in birleşmesi gibi). Takvimle otomatik promote YOK — koşul gelmeyen madde K3'te bekler, 30 günde BAYAT işareti alır (KILAVUZ; düşme Salih onaylı).
- **G2 (K2→K1, kanonlaşma):** yalnız Salih imzası. Carvis aday gösterir + kanıt paketler; imza yoksa K2'de yaşamaya devam eder.
- **G3 (şişme → derine özüt, m.34):** bir K3 dosyası eşiği aşınca (deneysel eşik: fikir kutusunda >40 aktif madde YA DA seçim-turu öncesi birikme) toplu özüt turu açılır: sağ kalanlar damıtılır, gerisi K0'a iner.

## 3. Önem ve log ağırlığı (deneysel formüller — ölçüm-öncelikli, m.35)

- **Önem (V9):** `önem = katman-tabanı × e^(−λt)` — katman-tabanı: K1=4, K2=2, K3=1; t = son dokunmadan geçen gün; her kullanım t'yi sıfırlar (kullanılan madde çürümez). λ başlangıcı: BAYAT-30g kuralıyla tutarlı olacak şekilde kalibre edilir (deneysel).
- **Log ağırlığı (V30, çıktı tarafı):** rapora/deftere ne girer sorusunda aday kural `ağırlık ∝ surprisal` — beklenen/rutin çıktı loglanmaz, sapma loglanır. Örnek: "pytest yeşil" tek satır; "pytest'in mount yüzünden yanlış-yeşil verdiği vaka" tam kayıt.
- **Ölçüm:** şemanın ilk deneği kendisi — her vardiya teslimine 3 sayaç: `giren madde / damıtılan / karara dokunan`. ~10 vardiya verisi birikince V30 formülü (V=ΔG/C) ilk kez gerçek sayıyla denenir; V28 etiketleme verisiyle aynı havuz.

## 4. Açık sorular → Salih cevapları (07-12)

1. **G1(b) = 2 kaynak** (Salih). 3'e geçiş ileride optimizasyon opsiyonu olarak kayıtlı — ihtiyaç doğunca denenir.
2. **G3 = 40 madde, deneysel OK** (Salih). Token sorunu çıkarsa sayıyı değiştirmek optimizasyon opsiyonu. **EK (Salih revizyonu):** K3 ile K2 arasına işler büyüyünce bir ARA KATMAN (çalışma adı: K2.5 — damıtma tamponu) eklenebilir; G3 eşiği aşıldığında özüt doğrudan K2'ye değil bu ara katmana yapılır. Ara katman ŞİMDİ AÇILMAZ (m.5 sorun-güdümlü) — açılış tetiği: ilk G3 aşımı.
3. TETİKLİ/UFUK başlangıç modeli — gömülü mü ayrı mı: **CEVAP BEKLİYOR** (detaylı izah istendi, oturumda verildi).

*İmza alanı: [ ] Salih onayı — tarih: ______ (onayla birlikte şema m.34'ün operasyonel eki olur, K-015 madde 1 DONE)*
