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

## Toplama (append-only)

### AB-01 · Karar-yazmanı (decision secretary) — TANIMLANDI · **PARK (uzun vade)**
- **Ham beyan** (2026-07-20 · beyansız · *SES-POC dikte örneği*): "Şirkette alınan önemli kararları benim için karar raporu olarak tutacak bir yazman lazım. Canlı [ajan] olarak yüklenebilir, yani yapabilir — ama uzun vade için hazinede dursun."
- **Yapabilir (m.42a):** ölçek-eşiği üstü önemli kararları tespit et → her biri için karar-raporu üret (mevcut `senaryo-defteri.md` m.37 şablonu: bağlam + 3-model + karşıt-temel + seçim + gözlem + ders; ya da sade karar + gerekçe + geri-açma) → deftere/arşive düşür → karar-başına-commit + [damıtma]/[icra] etiketi (m.10/V5) disiplinine bağla.
- **Kırmızı çizgiler (m.42a):** karar VERMEZ, yalnız KAYDEDER · `core/` · tüzük · `CLAUDE.md` · `.claude/` YAZMAZ (m.41 kilidi) · publish / para / kişisel-veri kararını kendi başına kaydetmez → Salih'e flag'ler (m.31 Katman-1) · **katı-başlangıç (m.42d):** taslak karar-raporu üretir, Salih/Carvis onaylar; onaysız deftere yazmaz.
- **Ölçek (token×zaman):** az × kısa (karar-anı işi).
- **Katman tahmini (m.30c):** kalıcı işçi (tek-kullanımlık DEĞİL — kararlar birikmeli, ajan-wiki'si atama anında başlar m.30a) · konum: Carvis altında.
- **Model tahmini (m.42g):** bir-altı, deterministik düşük-temperature (yazman = düşük yaratıcılık, doğruluk kritik; m.42f icra-ajanı deterministik).
- **Risk (m.42e):** DÜŞÜK — hata sınıfı = eksik/yanlış kayıt + atıf-hatası (yanlış tarih/karar); geri-alma ucuz (rapor revize/revert git); sigorta = V26 örneklem-denetimi + Salih onay kapısı.
- **Bağımlılık/tetik:** canlı atama **K-010 TETİKLİ** (prompt+kimlik devri eşiği, m.30 ek fıkrası) · **Salih kararı: PARK** — uzun vade için hazinede bekler, şimdi canlı kurulmaz · **ÖRTÜŞME:** `senaryo-defteri.md` (m.37 karar kayıtları) = bu ajanın otomatize edeceği MEVCUT altyapı → yeni format değil, o defterin + m.10 karar-commit'lerinin bakımı. K-010 açılınca ilk aday işçilerden.
- **Statü:** TANIMLANDI (parked) · **Hiyerarşi konumu:** atanmadı (aday: Carvis → kalıcı "karar-yazmanı" işçisi).
