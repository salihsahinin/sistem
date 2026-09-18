# Damıtma Turu Raporu — 2026-08-21 (S-E; boyut-tetiği ACİL, Salih onayı "devam")

**Tek cümle:** Dört FLAG'li sıcak dosya sorgu-uyumu hedefiyle damıtıldı (tam metinler üç arşiv dosyasında, kayıp 0), 5 bekleyen bronz gelen NOOP-damgalandı; defter ve kapsül bütçeye indi, pano/kutu kalan aşımları yazılı gerekçeli.

## Sonuç tablosu (her rakam bu turun `stat`/`wc` ölçümlerinden)
| dosya | önce | sonra | bütçe | durum |
|---|---|---|---|---|
| kuyruk/senaryo-defteri.md | 89,6 KB | **28,4 KB** | 48 | ✓ (−%68) |
| core/pano.md | 21,5 KB | **12,8 KB** | 12 | 0,8 aşım — kalan şişkinlik CANLI kart gövdelerinde (K-015/K-022/K-009/K-010); kart damıtması ayrı Salih kararı |
| fikir-kutusu.md | 30,9 KB | **24,8 KB** | 20 | 4,8 aşım — kalan satırların tümü karar-bekleyen/tetikli (recall-önce); süpürme zaten masada: **KB-36** |
| core/durum-kapsulu.md | 9,6 KB | **7,1 KB / 26 satır** | 8 / 40 | ✓ |

## Ne nereye indi (m.8: silme yok; her kesikte yerinde pointer)
- **Defter:** 08-16→08-20 karar blokları (63,7 KB; Karar 1-47 + Beyan 9-15 tam metin) → `kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-21.md`; yerinde seans-başına tek-satır hüküm indexi. Kalem-detay birincil kaynağı `veri/karar-borcu.jsonl`.
- **Pano:** Güncelleme "Önceki:" zinciri (07-30→08-12, 14 kayıt, 9,1 KB) + SON BİTEN 07-11→07-15 kapanışları → `kuyruk/arsiv/pano-arsivi-2026-08-21.md` §1-2. Kartlara dokunulmadı.
- **Kutu:** 11 satır → `kuyruk/arsiv/fikir-kutusu-arsivi-2026-08-21.md` — kanonlaşmış (V26·V60), kapanmış (V64), MEZUN-tarihçesi, koşup biten (agile/KB-15 · world-model ×2/W-1), RED (tahmin-defteri), UFUK üçlüsü (kutuda tek-satır pointer, tam metin arşivde). Karar-bekleyen/tetikli TÜM satırlar kaldı.
- **Kapsül:** kapanmış seans anlatı satırları (7-12) tam metin `pano-arsivi §3`'e; yerinde tek-satır özetler + güncel PR durumu (PR #2 MERGE). Erozyon sayacı: kaybolan niteleyici/pointer **0** (hepsi arşivde tam metin).

## İngest sayaçları (şema §3)
giren 5 · **NOOP 5** · UPDATE 0 · GEÇERSİZ-KIL 0 · ADD 0 · DLQ 0. Beş gelen dosyasının içeriği zaten borç kütüğünde izleniyordu (ai2ai + ölçek-yasaları → KB-36 [masada] · tavan-rejim → Karar 39 · staj-hasadı ×2 → KB-10); dosyalara "İNGEST EDİLDİ · 08-21" damgası basıldı, bronz olarak yerlerinde kaldılar. Anahtar-değeri değişimi yok → anahtar-denetim gerekmedi (GEÇERSİZ-KIL 0).

## Sorgu-uyumu beyanı (KB-17c — oran sonuç, hedef değil)
Damıtılmış dosyaların cevap verdiği sorular: defter → "hangi seans hangi kararı verdi + arşiv/kütük adresi"; pano → "hangi kart hangi durumda + DONE eşiği"; kutu → "hangi fikir hâlâ ADAY + tetiği ne"; kapsül → "şu an ne açık + sonraki ilk iş + Salih'te ne var". Tarihçe-anlatısı sorguları arşiv dosyalarına yönlenir (pointer'lar yerinde).

## Açık uçlar
- Pano 0,8 KB + kutu 4,8 KB kalan aşım: tetik yazılı (kart damıtması Salih kararı; kutu süpürmesi KB-36 masası). Tur sayısı 1/≤3.
- İB-02'nin diğer yarısı (2 KILAVUZ HAM raporu, 08-05) bu turun kapsamına girmedi — gelen-*.md sınıfı değil raporlar/ sınıfı; ayrı ingest kalemi olarak kapsülde duruyor.
