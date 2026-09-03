# Görev Emri — İB-64c: K-010 A5 aşama-araştırması — ekip-lideri tasarım paketi çift-atlas ön-koşulu

*Derleyen: Carvis yan-oturum işçisi (gorev-emri-derleme skill'i, 2026-09-03). Kaynak: `veri/karar-borcu.jsonl` İB-64c satırı + `core/pano.md` K-010 kartı + `kuyruk/k010-zincir-2026-08-29.md`. Rejim: Karar 85/86 — Fable planlayıcı, Sonnet işçi; [rejim: maliyet-öncelikli].*

## Görev tanımı (tek cümle)
K-010 A5 (ekip-lideri hattı — CC derin-araştırma + atlas ön-koşullu tasarım paketi) için, hafızası gelişen/statik ekip-lideri (orkestratör-ajan) tasarımlarına dair dış saha/literatür emsalleri çift-atlas (tez↔antitez) yöntemiyle bulunacak; A5 K-010 tetiğini beklemez ve geciktirmez, paralel yürür.

## Kapsam
- **Kapsamda:** ekip-lideri / orkestratör-ajan tasarım desenleri (statik-tanımlı vs. hafızası-gelişen lider, lider↔işçi bağlam-devri, çok-ajan orkestrasyon çerçeveleri); Fable-Sonnet ikilisi (Karar 85/86 §6) ile kıyaslanabilir saha örnekleri; "hafızası gelişen ekip-lideri A5'te KURULMAZ, öğrenme desenleri `kuyruk/ekip-lideri-ogrenme-desenleri.md` TOHUM dosyasına aktarılır" kararının (Salih notu, `core/ajan-metodolojisi.md` §6) ne ölçüde saha-emsalleriyle örtüştüğü.
- **Kapsam dışı:** A1/A2/A3/A4 aşamalarının kendisi (ayrı İB'ler); A5'in fiilen kurulması/implementasyonu (bu emir yalnız araştırma-önkoşulu, tasarım paketini üretmez — tasarım paketi ayrı bir sonraki adım); K-010 GO hükmü (Katman-1).
- **Kaynak-pointer'lar:** `veri/karar-borcu.jsonl` (İB-64c satırı) · `core/pano.md` K-010 kartı A5 satırı ("A5 ekip-lideri hattı [PARALEL]: tasarım paketi CC derin-araştırma + atlas ön-koşullu; gerekçe: Fable kota-tükenişi → görev devri; lider KURULUŞU = K-010 ∧ A5") · `kuyruk/k010-zincir-2026-08-29.md` ADIM-5 satırı ("A5 lider-hattı birleşmesi ayrı tetik") · `core/ajan-metodolojisi.md` §4 (Lider≠İşçi) ve §6 (Fable-Sonnet ikilisi, "Lider katmanı D1 a" — hafızası gelişen ekip-lideri KURULMAZ notu) · `kuyruk/ekip-lideri-ogrenme-desenleri.md` (TOHUM dosyası, varsa oku).

## KANONDA-BİLİNENLER (mükerrer araştırma freni)
Karar 86'nın kendisi zaten bir "ekip-lideri" hükmü verdi: statik skill-orkestratör Fable'da, hafızası-gelişen A5 kurulmaz, öğrenme desenleri TOHUM dosyasına gider. Bu araştırma A5'i YENİDEN TASARLAMAZ — mevcut hükmü dış emsallerle sınar/destekler, A5'in "tasarım paketi" ihtiyacına girdi verir. Firstmate rolü (İB-07/09, `core/ajan-metodolojisi.md` §"Firstmate rolü") zaten kanonda — tekrar araştırılmaz, verili kabul edilir.

## m.40b KONTRAT ŞARTLARI (Karar 86 D3, `core/ajan-metodolojisi.md` §"Ek fıkra — koşum-sözleşmesi üçlüsü")
1. **Yapan ≠ ölçen:** Tez/antitez/sentez yazan Sonnet ajanı aynı koşumda hakemlik YAPAMAZ; hakem ayrı çağrı (Fable ana-sıra ∨ ayrı Sonnet), yalnız ham veri (iddia+kanıt) alır — emrin yazarı/beklentisi verilmez.
2. **V26 URL'siz-iddia kotası:** örneklem son üçlükten ≥1 kaynak iddiası + tüm sayısal iddialar + ≥1 URL'siz/model-hafızası iddia zorunlu örneklenir.
3. **Birincil-kaynak açma kotası:** işçi başına ≥2 kaynak fiilen açılır (WebFetch/curl); yalnız özetten yazılan bulgu K'da kalır, D'ye yükselemez.

Bu iş açıkça "çift-atlas ön-koşullu" diye tanımlı (kaynak-not alanı) — yani m.40b'nin tam üç-aşamalı (tez→hedefli antitez→maskeli hakemlik) formu ZORUNLU, kısaltılmış tek-şerit tarama YETERSİZ sayılır.

## Beklenen çıktı formatı
D/K/X + URL etiketli rapor (`atlas-kosum` şablonu, `.claude/skills/atlas-kosum/references/rapor-sablonu.md`). Sentez bölümü doğrudan "tasarım paketi"nin girdisi olacak şekilde yapılandırılır: hayatta-kalan çekirdek desenler (SAĞLAM) ayrı, daralan/düşen iddialar ayrı listelenir; Fable-Sonnet ikilisiyle kıyas satırı zorunlu.

## SKILL TETİKLERİ
- skill: atlas-kosum
  tetik_kosulu: İB-64c koşuma alınırken (Salih ∨ sıradaki icra oturumu tetiği; K-010 ana zincirinin diğer aşamalarını BEKLEMEZ)
  cagri_kipi: literal
  girdi: arastirma_sorusu = "Ekip-lideri/orkestratör-ajan tasarımlarında (statik vs. hafızası-gelişen lider, lider↔işçi bağlam-devri) hangi saha/literatür desenleri var; Jarvis'in Fable-Sonnet statik-orkestratör kararıyla (Karar 85/86) nasıl kıyaslanır?"
  baglam: hedef=A5 tasarım paketinin araştırma-önkoşulu · çıktı-formatı=D/K/X+URL rapor, işçi dönüşü ≈1-2k özet · araç=WebFetch/WebSearch+Read(iç envanter, `core/ajan-metodolojisi.md` §4/§6, TOHUM dosyası) · sınırlar=A5'i fiilen kurma yok, yalnız araştırma
  yan_etki_damgasi: eklemeli × idempotent:h × dış-dünya:h
  done_yuklemi: rapor D/K/X etiketli ∧ tam üç-aşamalı çift-atlas (tez→hedefli antitez→maskeli hakemlik) koşuldu ∧ m.40b üçlüsü uygulandı ∧ Fable-Sonnet kıyas satırı üretildi
  hata_yolu: sözleşme-ihlali → çağıran (Carvis) düzeltir · yürütme hatası → telafi · retry ≤3 · FAIL-LOUD
  sira: 1/1 · handoff = `raporlar/` altına rapor dosyası + `kuyruk/ekip-lideri-ogrenme-desenleri.md`'ye pointer satırı + senaryo-defteri tek-satır gözlem
  kayit: execute_tool · tool.name=atlas-kosum · agent=Sonnet(işçi) · model+sürüm · tarih → skill sayacı

## ÇIKTI SÖZLEŞMESİ
- halusinasyon_derecesi: atıf/URL-yoğun rapor → H ≥ eşik kabul edilir; atlas-kosum kendi doğrulama zincirini taşır (halusinasyon-engelleyici ayrıca çağrılmaz).
- cikti_bicimi: `raporlar/2026-09-03-ib64c-ekip-lideri-paketi.md` (D/K/X+URL) + `veri/karar-borcu.jsonl` İB-64c satırına durum güncellemesi.
- done_yuklemi: rapor dosyası yazıldı ∧ tam çift-atlas koşuldu ∧ m.40b üçlüsü uygulandı ∧ A5 tasarım paketine pointer düştü — DRFR.
- yeniden_deneme: 3

## Teslim
`raporlar/2026-09-03-ib64c-ekip-lideri-paketi.md` + `veri/karar-borcu.jsonl` durum güncellemesi.
