# A1 lojik blok — devir emri formatı (İB-84 A1 · İB-93, 2026-09-16)

Kaynak karar: Karar 92 M3 EK (Salih 09-10: görev = sohbete bırakılan dosya; md → lojik → json → python) ve İB-84 revizyonu (Friday tur-2 B2: md + json çifti senkron çıkmadı → tek kaynak md, json türev). Geçiş planı `kuyruk/gorev-format-gecis-plani-2026-09-10.md`.

## Kural
- Emir md'sinin **bağlayıcı** kısmı ```` ```lojik ```` çitidir; düz yazı yalnız gerekçe. Alıcı ajan bloğu okur, gerekçeyi ister okur.
- json elle yazılmaz: `python3 tools/devir-md2json.py <emir.md>` → `<DEVİR_ID>.json` (aynı dizin). Çelişkide md kazanır; `--dogrula <json>` farkı çıkış 3 ile bildirir.
- Şema ihlali (eksik alan, çıktı-başına done eksik, çıktı yolu `YAZMA_İZNİ` dışında, dal > 5, dalda `→` yok) → çıkış 2, emir **gönderilmez**.

## Alanlar (hepsi zorunlu; büyük harf = kod jetonu)
| alan | tip | json karşılığı | kaynak |
|---|---|---|---|
| `DEVİR_ID` `KAYNAK_YÜZEY` `HEDEF_KATMAN` `TARİH` `EMİR_YOLU` | skaler | `kimlik.*` | devir-birimi v0 |
| `BAĞLI_DEVİR` | skaler (önceki devir_id) | `kimlik.bagli_devir` | Friday tur-2 eksik alan 2 |
| `NİÇİN_ŞİMDİ` | skaler | `gorev.nicin_simdi` | eksik alan 1 |
| `AMAÇ` | tek cümle | `gorev.amac` | v0 |
| `ÇIKTI` | sözlük `Cn: yol` | `gorev.ciktilar` | eksik alan 3 (çıktı-başına) |
| `DONE` | sözlük `Cn: boolean yüklem` | `gorev.done_cikti_basina` + birleşik `done_yuklemi` (∧) | eksik alan 3 |
| `DALLAR` | liste `Dn: eğer … → …` (≤5) | `gorev.dallar[]` | v0 + ajan-metodolojisi |
| `YAZMA_İZNİ` `YASAK` | liste | `yetki.yazma_izni[]` `baglam.yasak[]` | Friday tur-2 2. aşama notu: kilit görsün |
| `EAGER` `LAZY` `KARAR_ÖZETİ` | liste | `baglam.*` | v0 |
| `KAPALI_GÖZ_ÖZETİ` | skaler (envanter pointer'ı) | `baglam.kapali_goz_ozeti` | eksik alan 4 (desen 20 ön-koşulu) |
| `ÖLÇEN` | skaler | `yetki.olcen` | eksik alan 5 (yapan ≠ ölçen) |
| `BÜTÇE` | `k=v k=v …` | `butce.*` | v0 |
| `YENİDEN_DENEME` `GİT_İZNİ` `PUSH` `KARAR_YETKİSİ` | skaler | `gorev.yeniden_deneme` `yetki.*` | v0 |

Sabit satırlar `KARAR_ÖZETİ`'nde: Karar 89 (Opus medium) · Karar 93 ad-eşitliği · İB-84 A1 ("çelişkide md kazanır").

## Geçiş ölçüsü (A1 → A2)
Emir-kaynaklı `[sapma]` / devir (Friday sayar, Jarvis doğrular); arka arkaya 2 devirde 0 → A2 (json tek başına). Sayım: tur-1 2 · tur-2 1 · tur-3 (ilk A1) bekleniyor.

İlk örnek: `~/friday/cc/gelen/gorev-2026-09-16-tur3.md` (kopya `cc/devir/friday-2026-09-16-tur3/`).
