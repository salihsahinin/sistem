# Ajan Bağlam Hazinesi — HAM TOPLAMA yüzeyi

> **Statü: yan-oturum (CC) çıktısı — nihai form Fable'a ait (Salih beyanı 2026-07-20).** Bu dosya kanon DEĞİL; m.41 gereği CC yüzeyi hazineyi kilitleyemez. Buradaki iş: Salih'in günlük hayatta "şunu yapan bi ajanım olsun" dediği her beyanı KAYBETMEDEN, yapılandırmaya hazır halde biriktirmek. **Nihai "bağlam hazinesi" şemasını (kalıcı form) Fable/ana-sıra hazırlar** — bu dosya o inşaya ham veri + aday şema önerisi olarak girer (m.20 pointer, m.8 silme yok). Format deneysel (m.29).

## Ne için var (Salih talebi, 2026-07-20)
Kural niyeti: *"Bundan sonra günlük hayatta 'şunu yapan bi ajanım olsun' dediğimde, sen bu verileri ajan bağlamı sınıfında toplarsın; sonra o verileri uygun ajanlara tanımlayarak hiyerarşiyi inşa ederiz."* Yani üç aşamalı boru hattı:
1. **TOPLA** — ham beyan buraya düşer (bu yüzeyin işi; bugün işler).
2. **TANIMLA** — Carvis her beyanı m.42a pozitif-yetki formuna çevirir (ne YAPABİLİR + kırmızı çizgiler + ölçek + katman + model tahmini). Atama algoritması Carvis'te (m.30).
3. **ATA / HİYERARŞİYE KOY** — uygun ajana/katmana bağlanır. **Bu aşama canlı ajan = K-010 TETİKLİ** (m.30 ek fıkrası: prompt+kimlik devri K-010 eşiği). Yani toplama+tanımlama bugün, canlı atama K-010 açılınca.

## Kanon bağı
- **m.30** (atama mimarisi): kalıcılık · ajan-başına ingest · katmanlama (ekip lideri → altına işçi katmanı token-zaman verimi gerekince) · atamayı Carvis yapar, kararı Salih'in token-zaman limiti değiştirir.
- **m.42** (ajan-yetki kanunu): (a) pozitif yetki listesi · (b) Özgürlük(a) ≤ Toparlanabilirlik(hata(a)) · (c) bileşik gevşetme · (d) katı-başlangıç · (e) RİSK boyutu · (f) çeşitlilik-bütçesi · (g) model-hiyerarşi (JARVIS=Fable · ekip lideri=Opus/bir-altı).
- Bu yüzey o iki maddenin önündeki **giriş katmanı**dır; kararı bozmaz, besler (m.16 kapısı: çelişki yok — kontrol edildi 07-20).

## Aday şema (ÖNERİ — Fable nihai formu belirler)
Her beyan bir kayıt; alanlar Fable'ın nihai hazinesine taşınabilir aday sütunlar:

| Alan | Açıklama |
|---|---|
| ID | AB-nn |
| Ham beyan | Salih'in cümlesi birebir + tarih + damga (ayık/HI/mobil — m.33; beyansızsa "beyansız") |
| Yapabilir (m.42a) | Ajanın NE yapabileceği — pozitif liste; "ne yapacağı" değil |
| Kırmızı çizgiler (m.42a) | Açık yasaklar / dokunamayacakları |
| Ölçek (token×zaman) | az/orta/çok × kısa/uzun — Salih limiti (m.30, tanım dipnotu) |
| Katman tahmini (m.30c) | tek-kullanımlık işçi / kalıcı işçi / ekip lideri |
| Model tahmini (m.42g) | Fable / Opus / bir-altı |
| Risk (m.42e) | hata-olasılığı × maliyet × geri-alma-maliyeti — kısa not |
| Bağımlılık / tetik | K-010 tetikli mi · başka ajana bağlı mı · blokaj |
| Statü | TOPLANDI → TANIMLANDI → ATANDI |
| Hiyerarşi konumu | atandığında: üst ajan + katman |

## Toplama (append-only — henüz beyan yok)

| ID | Ham beyan (tarih · damga) | Yapabilir | Kırmızı çizgiler | Ölçek | Katman | Model | Risk | Bağımlılık/tetik | Statü |
|---|---|---|---|---|---|---|---|---|---|
| — | *(Salih ilk "şunu yapan bi ajanım olsun" dediğinde buraya düşecek)* | | | | | | | | |
