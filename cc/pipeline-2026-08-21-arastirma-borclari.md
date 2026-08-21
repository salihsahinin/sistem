# Pipeline Manifesti — Araştırma Borçları Koşumu (2026-08-21, paralel oturum s13)

*Salih emri (08-21 akşam, paralel-oturum açılışı): "sistemdeki araştırma borçlarını pipeline kur koş". Desen: P-1 pipeline-kosum v1. Rejim: **[maliyet-öncelikli]** (token kısıntısı %30 — işçi bütçesi 10-15k, effort low/medium, aile ≤3). Oturum düşerse yeni oturum BURADAN devralır.*

## Paralel-oturum şerhi (canlı-oturum kapısı, Karar 57)
Açılışta son commit 1 dk taze (146eab1, masa parti-6) → diğer oturum CANLI. Bu pipeline'ın frenleri:
- **Yazım alanı:** yalnız bu manifest + `cc/gorev-2026-08-21-arastirma-borclari.md` + `cc/rapor-2026-08-21-ab*.md` + seans-teslim raporu + `veri/bronz/tahmin-olay.jsonl` (append-only). 
- **DOKUNULMAZ (masa oturumunun sahası):** `veri/karar-borcu.jsonl` · `fikir-kutusu.md` · `kuyruk/senaryo-defteri.md` · `core/durum-kapsulu.md` · `core/pano.md`. Ledger/kutu/kapsül güncellemeleri teslim raporunda DEVİR-NOTU olarak ana oturuma bırakılır.
- Commit'ler `git add <yol>` ile (git add -A yasak); karar ALINMAZ (bulgular D/K/X etiketli rapor; hüküm Salih/ana-oturum masasında).

## Kapsam (araştırma-borcu envanteri — açılış taraması bu oturum)
| Borç | Kaynak kayıt | Tetik durumu |
|---|---|---|
| AB-1 skill-bakım sistemi | fikir-kutusu.md:101 (Salih emri 08-20 "araştırması yapılmak üzere not et"; tetik: Salih "araştır" emri) | bu emirle ÇEKİLDİ; V25 (kutu:50) hazır-araç taraması bindirmeli |
| AB-2 idempotens sistematik entegrasyonu | ledger İB-39 (Salih 08-20 KB-18 eki; icra-sırada, "araştırma koşumu tetik Salih") | bu emirle ÇEKİLDİ |
| AB-3 usage-otomasyon yol seçimi | ledger İB-08 (masa_yolu "İCRA (m.40 araştırma-önce)"; kısa atlas şartı) | araştırma-önce şartı bu koşumla kapanır |
| AB-4 token-verim okuyucu ön-katmanı | fikir-kutusu.md:79 V59 "ARAŞTIRILACAK" + cc/gorev-2026-07-22-1.md §3 ATLAS-V59 | emir 07-22'de yazılmış, HİÇ KOŞMAMIŞ (manifest kapısı: cc/rapor'larda ATLAS-V59 izi 0) **⟨ŞERH 21:5x — YANLIŞ ÇIKTI: cc/rapor-2026-07-22-1.md:111 "ATLAS V59" (boşluklu) bölümü VAR; tireli grep ıskaladı → kısmi mükerrer koşum, ders teslim raporunda⟩** |
| AB-5 cascade-failure kaynak doğrulama | cc/rapor-2026-08-15-3.md:538 ("araştırma-borcu olarak kaydedilmeli" — ledger'da kaydı YOK; kayıt devir-notuna) | bu emirle ÇEKİLDİ |
| KAPSAM DIŞI | UFUK üçlüsü (Katman-1 vizyon, karar yok) · KB-17b taban-oranı + İB-10 hakem-sapması (ölçüm koşumu, araştırma değil) · KB-31 (BEKLET-tetikli: Codex alımı) | girmedi |

## Görev tablosu
| Rol | Şekil | İş | Intake | Teslim | Durum |
|---|---|---|---|---|---|
| S-1a | scout (atlas-tez) | AB-1 skill-bakım: dış pratik taraması + tasarım hammaddesi | emir §S-1a | cc/rapor-2026-08-21-ab1-tez.md | DONE |
| S-1b | scout (atlas-antitez) | AB-1 refütasyon: "periyodik bakım gereksiz, kullanım-anı sinyali yeter" | emir §S-1b | cc/rapor-2026-08-21-ab1-antitez.md | DONE |
| S-2 | scout (tek-şerit + antitez-borcu) | AB-2 idempotens: iç desen envanteri + dış standart/desen + boşluk listesi | emir §S-2 | cc/rapor-2026-08-21-ab2-idempotens.md | DONE |
| S-3 | scout (kısa atlas) | AB-3 usage: (i)JSONL-parse / (ii)OTLP / (iii)ccusage kıyas + öneri | emir §S-3 | cc/rapor-2026-08-21-ab3-usage.md | DONE |
| S-4a | scout (atlas-tez) | AB-4 V59 reader-model desenleri + kalite-kaybı ölçümü + m.20/m.34 bileşme | emir §S-4a | cc/rapor-2026-08-21-ab4-tez.md | DONE |
| S-4b | scout (atlas-antitez) | AB-4 refütasyon: "ön-okuyucu kalite kaybı token kazancını yer" | emir §S-4b | cc/rapor-2026-08-21-ab4-antitez.md | DONE |
| S-5 | scout (mini doğrulama) | AB-5 arxiv 2605.17288 okuma + D/K/X etiket + uygulanabilirlik | emir §S-5 | cc/rapor-2026-08-21-ab5-cascade.md | DONE |
| G-1 | sentez (Carvis) | maskeli hakemlik: hayatta-kalan bulgular + borç-başına sonuç bloğu | S-1..S-5 raporları | teslim raporu §sentez | DONE |
| SH-1 | ship (Carvis) | commit'ler + devir-notu (ledger/kutu güncellemesi ana oturuma) | G-1 | seans-teslim raporu | DONE |
| T | teslim | kaptan beyanı | tüm satırlar DONE | tek cümle | DONE |

*Paralellik-uygunluk testi: 5 borç bağımsız keşif (ortak üretim yok) → paralel serbest; tez↔antitez kolları m.40b gereği zaten birbirinden habersiz koşar → 7 işçi tek dalga.*

## Olay günlüğü
- 21:24 açılış: canlı-oturum kapısı işledi (146eab1 1 dk taze → paralel fren aktif); manifest kapısı: araştırma-borcu pipeline'ı daha önce koşmamış (cc/pipeline-* 8 dosya tarandı, git log -15 temiz).
- 21:2x envanter: ledger 77 kayıt tarandı (İB-08/İB-39 araştırma sınıfı; KB-31 BEKLET-tetikli kapsam dışı), kutu araştırma-tetikli 2 kalem (skill-bakım, V59), rapor-08-15-3:538 kayıtsız araştırma-borcu bulundu.
- 21:3x emir derlendi; ilk Kapı-Ö koşumu BLOKE (kayit alanı eksik) → onarıldı → GEÇTİ; 7 koşum-profili tahmini bronz'a yazıldı (HEAD 146eab1); açılış commit'i b8f0a38; 7 işçi tek dalgada salındı (6× sonnet + 1× haiku).
- 21:4x-21:5x raporlar indi (7/7, tüm done_yuklemi DRFR PASS). V26 örneklem denetimi (3 nokta): S-5 arxiv künyesi Carvis'çe çapraz açıldı — künye D teYİT, ama ajanın "doğrusal olmayan artış" güçlendirmesi özette YOK → DAYANAKSIZ düşürüldü · S-4a contextual-retrieval rakamları (%35/%49/%67 + $1.02/M) kaynakta birebir PASS · S-3 "internal format" alıntısı sessions sayfasında birebir PASS.
- 21:5x ARIZA-DERSİ: manifest kapısının "ATLAS-V59 hiç koşmamış" hükmü YANLIŞ çıktı (tire↔boşluk grep ıskası; 07-22 raporunda bölüm varmış) → AB-4 kısmen mükerrer; hafifletici: S-4a o raporu kendiliğinden bulup pointer'la üstüne koydu, tekrar-araştırma sınırlı kaldı. Kural adayı devir-notunda.
- 22:0x G-1 sentez + SH-1 commit'ler; teslim raporu `raporlar/seans-teslim-2026-08-21-arastirma-borclari.md`; T beyanı verildi. Tahmin↔gerçek işlemesi (ambar) ana-oturum/kapanış ritüeline devir.
