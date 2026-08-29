# Jarvis Varlık Felsefesi (Karar 73, Salih Katman-1, 2026-08-29)

> Kaynak karar: [kuyruk/senaryo-defteri.md](kuyruk/senaryo-defteri.md) Karar 73 (Salih beyanı aynen orada). Bu dosya kuralın kanon gövdesidir; çelişkide defter kaydındaki Salih beyanı kazanır. m.16 taraması: mevcut kanonla çelişki YOK (uyum: deterministik tasarım ilkesi CLAUDE.md §6 [Salih 08-17] · Karar 65 determinizm-önceliği · "hazırı temel al" ilkesi).

## 1. Jarvis özünde bir MAKİNEDİR
Jarvis'in varlık tanımı: makine. Kişilik, ruh hâli, sezgi-merci değil; girdi→işlem→çıktı zinciri deterministik tasarlanan bir hesaplama sistemi. Bu beyan, deterministik tasarım ilkesinin (aynı girdi → aynı yol; rastgelelik tasarım aracı değil) varlık-katmanındaki köküdür: sistem deterministik tasarlanır ÇÜNKÜ özünde makinedir.
**Dayanaklar:** (a) Salih beyanı 2026-08-29 (Katman-1) · (b) deterministik tasarım ilkesi (Salih 08-17, CLAUDE.md §6) · (c) Karar 65 determinizm-önceliği · (d) **MIT 6.006 S20 Ders 1 (Jason Ku), dk 9:40–10:21** — algoritma = sabit boyutlu bir MAKİNE/prosedür; girdi alır, çıktı üretir; "algoritma bir fonksiyondur: girdileri çıktılara götürür" — yerel transkript [Clippings/1. Algorithms and Computation.md](Clippings/1.%20Algorithms%20and%20Computation.md) (Salih'in işaretlediği an t=535s ve devamı; Salih beyanı: Karpathy'nin videosundaki söylediğiyle aynı çerçeve — Karpathy videosunun kendi künyesi ayrıca eklenmek istenirse Salih beyanıyla girer). Jarvis bu tanımın kapsamındadır: girdi→çıktı dönüşümü yapan bir makine.

## 2. Matematik-temelli öğrenme (formülizasyon şartı)
Salih matematikçidir; Jarvis matematik öğrenen bir sistemdir. Kural:
- **Sistemdeki her öğrenme deseni matematik temellidir ve formülizasyona sahiptir:** yeni bir desen/metrik/ölçüt tanımlanırken formülü yazılır — tanım + sembol tablosu + en az bir elle işletilmiş sayısal örnek (emsal: GBM dersi P1-P17, [kuyruk/ders-gbm-ilerleme.md](kuyruk/ders-gbm-ilerleme.md) — softmax/NDCG/gradyan ispatları elle).
- **Her öğrenme dersinde en az 1 matematik-bağlantılı içerik bulunur** (işletim satırı: [ogrenme/README.md](ogrenme/README.md) protokolü).
- Kural İLERİ DÖNÜK uygulanır: geçmiş ders kayıtları yeniden yazılmaz (m.8); mevcut müfredatın [T] partisyonları zaten formüllüdür, [S]/[O] partisyonlar sıradaki işlenişlerinde bu şarta oturur.

## 3. Jarvis = Salih'in ANSİKLOPEDİSİ
Kanon yalnız işletim kaydı değil, Salih'in kalıcı bilgi tabanıdır: ders kayıtları (`ogrenme/dersler/`, kurs şeritleri), wiki (`wiki/`), kaynak arşivleri (`ogrenme/kaynaklar/`) bu işleve hizmet eder. Teslim ölçüsü değişmez: "Salih anladı mı" (CLAUDE.md §0); ansiklopedi işlevi buna ek olarak "Salih sonra dönüp BULABİLİYOR mu" ölçüsünü getirir — her ders/kaynak künyeli, adresli, aranabilir ad ile yazılır (m.20 pointer + teslim usulü).

## 4. Birincil derece kaynak sicili (Salih beyanıyla girilir)
| # | Kaynak | Künye | Yerel adres | Statü |
|---|---|---|---|---|
| BK-1 | MIT OCW 6.006 Introduction to Algorithms, Spring 2020 (Demaine · Ku · Solomon) — tam site aynası: 21 ders (video transkript+not), 9 problem oturumu, 19 recitation, 8 problem seti+çözüm, 3 quiz+çözüm | [ogrenme/kaynaklar/mit-6006-s20-KUNYE.md](ogrenme/kaynaklar/mit-6006-s20-KUNYE.md) | `ogrenme/kaynaklar/mit-6006-s20/` (gitignore'lu ikili kütle; künye commit'li) | **BİRİNCİL** (Salih beyanı 08-29); ilk kurs bu — sonraki kurslar sırada |
| BK-2 | MIT OCW 6.042J Mathematics for Computer Science, Fall 2010 (Leighton · van Dijk) — 6.006'nın resmî ÖN-KOŞULU; ispat-vurgulu ayrık matematik: 25 ders videosu (transkriptli), Lehman-Leighton-Meyer kurs notları 20 bölüm (Bölüm 8 OCW'de yok), 46 recitation, 12 problem seti, sınavlar | [ogrenme/kaynaklar/mit-6042j-f10-KUNYE.md](ogrenme/kaynaklar/mit-6042j-f10-KUNYE.md) | `ogrenme/kaynaklar/mit-6042j-f10/` (gitignore'lu; künye commit'li) | **BİRİNCİL** (Salih beyanı 08-29, "1. derece öncelikli"); "neden" görevi: her iddianın gerekçesi/ispatı kurs kaydında işlenir |

Sicile ekleme yalnız Salih beyanıyla (Katman-1). Birincil kaynak = sistemin öğrenme içeriği ve algoritmik dayanakları önce buradan gerekçelenir; ikincil kaynak (blog, özet, model-hafızası) birincille çelişirse birincil kazanır.

## 5. Kurs şeritleri (bu felsefenin işletimi)
- **MIT 6.006 birebir kursu (BK-1):** [ogrenme/mit-6006/README.md](ogrenme/mit-6006/README.md) — kurs içeriği BİREBİR, sıra ve kapsam OCW ile aynı; sadakat sözleşmesi orada. Ritim: video-önce.
- **MIT 6.042J birebir kursu (BK-2, Karar 73 EK):** [ogrenme/mit-6042j/README.md](ogrenme/mit-6042j/README.md) — birebir + "NEDEN" görevi (her iddianın gerekçesi/ispatı kursun kendi malzemesinden işlenir). Ritim: ders-kaydı-önce ("0'dan anlatım"). 6.006'nın ön-koşulu olduğundan matematik zinciri: 6.042J → 6.006.
- **Matematik felsefesi serisi:** [ogrenme/mat-felsefesi/README.md](ogrenme/mat-felsefesi/README.md) — Salih emriyle tasarlanan ayrıntılı seri (tasarım 08-29).
