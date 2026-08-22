# Pipeline Durumu — Silver-sağlık paketi (İB-42 icrası; Karar 58 = KB-39/40/41 (a)) · 2026-08-22 seans-14 (icra oturumu, Carvis/Fable, oturum 11b49d44)

*Künye: kaynak karar `veri/karar-borcu.jsonl` KB-39/40/41 (kapanış kanıtı 08-21 seans-11 Karar 58) · şartname `cc/rapor-2026-08-17-1.md` Sentez S2 (Adım 0-6) · icra borcu İB-42 (eski İB-15..18 birleşik). Salih emri 08-22 ~18:40: "bu oturum anlık icra oturumu, icra borçlarından birini aç başla" — seçim Carvis (m.4: sonucu değiştirmeyen seçim; gerekçe: karar beklemeyen en büyük kalem, hiçbir manifestte sahada değil, İB-43/44 bunun üstüne biner). Koşum-önü kapı: `git log -15` + manifestler tarandı — bu iş daha önce KOŞMAMIŞ. Paralel-oturum şüphesi (seans-13 oturumu 18:24 resume) → commit'ler yollu `git add`.*

## Kapsam (Karar 58'in KODA çevrilmesi; deterministik, stdlib, LLM yok)
| SH | ne | kanıt (done-yüklemi) | durum |
|---|---|---|---|
| SH-0 | Manifest + ledger SAHADA damgası | bu dosya + İB-42 `not` | ✅ 08-22 18:5x |
| SH-1 | `tools/silver-saglik.py` v0: anahtar-kaydı → silver `anahtar_kaydi` (İB-16) · `kayit.gecerlilik/gecerlilik_neden/tespit_tarihi` türetilmiş kolonlar (additive) · T-Ç1..6 testleri · T-B 4 yüklem + 2 koruma · T-A ön-eleme (çift sayımı; LLM çağrısı YOK — prompt dosyası) · `silver_kuyruk` + `v_guncel_*` + özet görünümler · append-only `veri/silver-saglik.jsonl` (1 satır = 1 test × 1 koşum) + olay-kaynaklı `veri/silver-kuyruk.jsonl` (ACILDI/KAPANDI; tespit_tarihi buradan) · çıkış 6 yalnız `--kapi` ile (geliştirme = uyarı modu, C-EK-3) · `--test` canary (tohumlu ihlal → ilgili test FAIL vermeli) | script + kurallar `veri/sozlesme/silver-saglik-kurallar.json` + canary PASS + iki koşum byte-eş (ts hariç) | ⏳ |
| SH-2 | `katman-hatti.py` adımı (olcum'dan önce, uyarı kanalı) + `katman-olcum` sözleşme güncellemesi (kayit +3 kolon; anahtar_kaydi/silver_kuyruk sözleşmeleri) + gold CSV'ler | hat PASS; preflight EK→PASS | ⏳ |
| SH-3 | seans-kapanis + damitma kapı satırı (`--kapi`; T-Ç error → çıkış 6, hat durur) · SCRIPTLER satırı · veri/README bölümü | dosyalar | ⏳ |
| SH-4 | Kapanış: manifest T beyanı + ledger İB-42 (kısmen/kapandı + kalan) + kapsül satırı + commit | — | ⏳ |

## Kapsam DIŞI (kalan borç; bu oturumda koşmaz)
- T-A LLM kanıt-bulucu KOŞUMU (alt model; ilk 10 koşum insan-etiketli kalibrasyon — KB-41) → ayrı tetik; script yalnız aday çiftleri + prompt'u üretir.
- Adım 6b as-of eval (n≈20-30 soru; `v_guncel` ↔ ham `kayit`) → ayrı kalem (eski İB-18).
- Sabit kalibrasyonu (pencere 3 seans, eşikler) ≥10 koşum sonra (m.29).

## Kütük
- 18:40 açılış; sondaj: silver `anahtar` 328 satır, tümü `gozlenen`, `replaced_by/gecerli_bitis` 0 dolu → kayıt JSON'u (10 anahtar, emekli+halef) silver'a script JOIN edecek · sıcak 912 / ılık 3.326 / soğuk 45.552 kayit · soğuk 412 dosyanın 227'si sıcak/ılık'tan 0 `dosya_pointer` (YETİM adayı havuzu) · zarf 11 (bitiş 0) · sqlite 3.51.0 (pencere fonksiyonu var) · teslim dosyası 54 (SEANS sayacı kaynağı).
