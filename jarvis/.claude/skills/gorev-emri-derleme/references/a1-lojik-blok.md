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
| `KAPALI_GÖZ_ÖZETİ` | liste (envanter pointer'ları) | `baglam.kapali_goz_ozeti[]` | eksik alan 4 (desen 20 ön-koşulu) |
| `ÖLÇEN` | skaler | `gorev.olcen` (v0.2; v0.1'de `yetki.olcen`) | eksik alan 5 (yapan ≠ ölçen) |
| `BÜTÇE` | `k=v k=v …` | `butce.*` | v0 |
| `OTURUM` | `devam` \| `yeni` | `oturum.durum` | v0.2 — Friday tur-3 a2 (işletimsel talimat düz yazıda kalmasın) |
| `AÇILIŞ_ADIMLARI` | liste (isteğe bağlı) | `oturum.acilis_adimlari[]` | v0.2 a2 |
| `KAPANIŞ` | liste | `gorev.kapanis[]` | v0.2 a3 (kapsül · pano · defter · commit · son mesaj) |
| `KAYNAKLAR` | sözlük `Rn: url` — blokta URL/doküman anılıyorsa **zorunlu** | `kaynaklar` | v0.2 a1 (URL bağlayıcı metinde) |
| `YENİDEN_DENEME` `GİT_İZNİ` `PUSH` `KARAR_YETKİSİ` | skaler | `gorev.yeniden_deneme` `yetki.*` | v0 |

Sabit satırlar `KARAR_ÖZETİ`'nde: Karar 89 (Opus medium) · Karar 93 ad-eşitliği · İB-84 A1 ("çelişkide md kazanır").

## Emir-kaynaklı sapma tanımı (v0.2, Friday tur-3 a4)
**Sapma** = bloktaki bir alanın (`DONE` · `DALLAR` · `YAZMA_İZNİ` · `YASAK` · `KAPANIŞ`) uygulanamaması ya da iki alanın çelişmesi yüzünden alıcının blok dışına çıkması; her biri geri-dönüş `sapmalar` tablosunda `emir_maddesi` ile. **Sapma sayılmaz:** bir dalı (`Dn`) izlemek · `YASAK`'ın kendi istisnası (B5) · örtük izinli hafıza işi (m.42(h)) · düz yazıyı okumak. **Blok-eksiği** (ayrı sayaç): alıcının işi bitirmek için düz yazıya ya da bağlama başvurmak zorunda kaldığı bilgi (tur-3: a1 URL, a2 oturum, a3 kapanış → v0.2 alanları). Sayan Friday, doğrulayan Jarvis.

**`.aktif-devir` (b1):** script json'la birlikte emir dizinine `.aktif-devir` (DEVİR_ID) yazar; alıcı geri-dönüşte siler. "Oturum devam" hâlinde `seans-acilis` koşmadığı için kütük v0.3 `devir_id` bu dosyadan dolar.

## Geçiş ölçüsü (A1 → A2)
Emir-kaynaklı `[sapma]` / devir (Friday sayar, Jarvis doğrular); arka arkaya 2 devirde 0 → A2 (json tek başına). Sayım: tur-1 2 · tur-2 1 · tur-3 (ilk A1) **0** (Jarvis doğruladı; blok-eksiği 3 → v0.2). A2 için 1/2; tur-4 v0.2 blokla 0 çıkarsa A2.

İlk örnek: `~/friday/cc/gelen/gorev-2026-09-16-tur3.md` (kopya `cc/devir/friday-2026-09-16-tur3/`).
