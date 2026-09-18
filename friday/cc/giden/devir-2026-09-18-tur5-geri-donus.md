# Geri-dönüş — devir-2026-09-18-tur5 (Friday, AS-OF 2026-09-18; şema `core/sablonlar/geri-donus-v0.md`)

## 1. biten
| iş | kanıt_yolu |
|---|---|
| C1 hook v0.4: Bash'te yol adayları yalnız dosya-komutlarının argümanlarından; `grep/rg/egrep/fgrep/sed/awk/jq/find` ilk argümanı desen sayılır; tırnak soyulur; değişkenli belirteçte sabit önek denetlenir; yönlendirme hedefleri ve `cd` takibi korundu; Read/Grep/Glob dalı değişmedi | `.claude/hooks/okuma-izin.sh` |
| C1 alt-ajan dalına `cc/gelen/**` eklendi; liderin kendi emrini okuması etkilenmedi (D3 doğrulandı: test vakası + bu koşumun kendisi) | aynı dosya, `ALT_YASAK` |
| C2 test 22 → 30 vaka; 30 `PASS` · 0 `FAIL`; bronz kütüğe yazmıyor; bayrak `exit 2`'yi kapatmıyor | `.claude/hooks/okuma-izin-test.sh`, çıktı `cc/giden/devir-2026-09-18-tur5/uygulama-raporu.md` §4 |
| C3 `CLAUDE.md`'ye Edit-usulü satırı; dosya 4.195 B → **4.090 B** (bütçe 4.096) | `CLAUDE.md` §5 |
| C4 uygulama raporu: diff özeti · test çıktısı aynen · iki canlı kanıt (desen geçer **D**, `cat` ile açık yol `RED` **D**) · komut listesinin eksik kalabileceği durumlar paragrafı | `cc/giden/devir-2026-09-18-tur5/uygulama-raporu.md` |

## 2. kalan
| iş | neden_kaldı |
|---|---|
| Z3b (yolun tamamı değişkende) | Karar 100 M5: bu turda dokunulmaz, sandbox K-010 A4 gündeminde. |
| Komut kümesinin kapsamadığı okuma yolları (`git show`, uzak çalıştırıcılar, satır-içi yorumlayıcı kodu, `=` ile birleşik bayrak değeri) | Tanıma listesi sonlu; tazeleme kuralı raporda (§6). Kümeyi genişletmek emrin dışında → kural adayı. |
| `.claude/settings.json` | `YASAK` gereği bu turda dokunulmadı. |

## 3. acik_sorular_salih (hüküm yok)
1. Komut kümesi genişlesin mi (`git show`/`git cat-file`, `xxd`/`od`/`strings`, `perl -ne`/`ruby -e`) — yoksa liste bugünkü hâliyle mi kalsın?
2. `bash betik.sh` çağrısında bugün yalnız betiğin yolu denetleniyor, içeriği değil; betik içi okumalar için ayrı bir kural gerekir mi?
3. Emrin `KAPANIŞ` satırındaki seri etiketi ("tur-2 2 · tur-3 1 · tur-4 0") benim kayıtlarımdan bir tur kayık (bende tur-1 2 · tur-2 1 · tur-3 0 · tur-4 0). Hangi etiketleme kanona geçsin?
4. `CLAUDE.md` bütçesi bayt mı karakter mi? Bayt kabul ettim (tur-2 ölçümüyle aynı); karakterle dosya zaten 3.8 KB'ydi.
5. Ayrıştırıcı artık "tanıma listesi"; kümede olmayan komut taranmadan geçiyor. Bu, kilidin ilan metniyle ("izinli kökler dışı → RED") nasıl uyumlanmalı?

## 4. sonraki_ilk_is
Jarvis test çıktısını ve iki canlı kanıtı yeniden koşup doğrulasın (`ÖLÇEN`); sonra §3'teki beş soru Salih'e.

## 5. diskteki_dosyalar
| yol | commit_dışı |
|---|---|
| `.claude/hooks/okuma-izin.sh` · `.claude/hooks/okuma-izin-test.sh` · `CLAUDE.md` | hayır |
| `cc/giden/devir-2026-09-18-tur5/uygulama-raporu.md` · `cc/giden/devir-2026-09-18-tur5-geri-donus.md` | hayır |
| `core/durum-kapsulu.md` · `core/pano.md` · `kuyruk/senaryo-defteri.md` · `kuyruk/fikir-kutusu.md` | hayır |
| `raporlar/seans-teslim-2026-09-18-tur5-ayristirici.md` | hayır |
| `cc/gelen/.aktif-devir` | silindi (kapanış adımı) |

## 6. sayac
{ ajan_çağrısı: 0, araç_çağrısı: bu devir **17** (kapanış yazımından önceki ölçüm; kütükte `devir_id = devir-2026-09-18-tur5`), kapanış çağrılarıyla ≈ 23 `[?]`, işçi_sayısı: 0, alt_ajan_token: 0 }
Emrin tavanı 45 — aşılmadı. Açılan dış sayfa: 0 (R1 bu turda yeniden açılmadı; tur-2/tur-3 okumaları kullanıldı).
Kilit tetiklenmesi: 1 kez — `DONE C4`(ii) gereği bilerek yapılan `cat` denemesinde. Tur-4'teki yanlış-pozitif bu turda tekrarlamadı.

## 7. sapmalar
**Emir-kaynaklı sapma sayısı: 0.** İki uyarlama açık:

| emir_maddesi | ne_yapıldı | neden sapma sayılmadı |
|---|---|---|
| `DONE C1` komut listesi | Listeye `ls find awk grep rg egrep fgrep tee touch mkdir stat file md5 shasum nl cut` eklendi | Madde "en az bunlar" diyor; `ls ~/jarvis/cc` gibi mevcut test vakaları aksi hâlde kapsam dışı kalır ve kilit gevşerdi. |
| `DONE C3` "bütçe aşılmamış" | Edit satırı eklenirken beş yer kısaltıldı | Dosya emirden önce zaten 4.195 B ile bütçe üstündeydi; "bir satır girer, bir satır çıkar" kuralı uygulandı, hiçbir kural kaldırılmadı. |

Emir dışı gözlem (sapma değil): emrin `KAPANIŞ` satırındaki sapma serisi etiketi benim kayıtlarımdan bir tur kayık; §3 soru 3.

## 8. tohum_desen_kullanimi
| desen | kullanıldı | neden |
|---|---|---|
| 20 (kontrol listesi / liste eskir) | evet | Komut kümesinin eksik kalabileceği durumlar ayrı paragraf; tazelemeyi listeyi gören taraf yapar. |
| 21 (kural önermeden önce semantiği oku) | evet | Ayrıştırıcı değişikliği `settings.json` deny bloğuna dokunmadan yapıldı; deny semantiği tur-3'te belgelenmişti. |
| 4 (yapan ≠ ölçen) | evet | Testi ve canlı kanıtı ben koştum; doğrulama `ÖLÇEN` gereği Jarvis'te. |
| 10 (pathspec-only git) | evet | `git add <yol>`; push yok. |
| m.39 rakam | evet | 30/0, 22 → 30 vaka, 4.195 → 4.090 B, 17 çağrı ölçüldü; kapanış payı `[?]`. |

## 9. ledger_onerisi (öneri)
| ib_no | önerilen_durum |
|---|---|
| Karar 100 M1 (ayrıştırıcı v0.4) | uygulandı — 30 vaka `PASS`, iki canlı kanıt |
| Karar 100 M3 (`cc/gelen/**`) | uygulandı — alt-ajan `RED`, lider serbest (D3) |
| Karar 100 M4 (Edit usulü) | uygulandı — `CLAUDE.md` §5, bütçe içinde |
| Karar 100 M5 (Z3b) | açık bırakıldı, dokunulmadı |
| Kural adayı | komut kümesinin genişletilmesi · betik-içi okuma · ilan metni ile tanıma listesi uyumu |

## 10. durma_nedeni
tamamlandı (yeniden deneme kullanılmadı; D1/D2 tetiklenmedi, D3 doğrulandı, D-KATMAN1 → üç kural adayı)

## + kapsul_eklenen
- Tur-5 bitti: ayrıştırıcı v0.4 — Bash'te yalnız dosya-komutlarının argümanları yol sayılıyor; desen dizesi artık çağrı durdurmuyor, `cat` ile açık yol hâlâ kesiliyor (iki canlı kanıt).
- Alt-ajan yasak listesine `cc/gelen/**` girdi; lider kendi emrini okumaya devam ediyor (D3). Test 30 `PASS` · 0 `FAIL`.
- `CLAUDE.md` 4.090 B (bütçe 4.096) ve Edit-usulü satırı eklendi. Açık: komut kümesi sonlu (tanıma listesi), Z3b M5 ile açık.

## + cekirdek_adayi (Salih "kabul" derse `core/desenler.md`)
- "Bir güvenlik taramasını inkâr listesinden tanıma listesine çevirdiğinde kazandığın isabeti, kaybettiğin kapsamla birlikte yaz": v0.4 desen/argüman ayrımını kazandı, ama kümede olmayan her okuma komutunu kapsam dışına çıkardı; ikisi aynı değişikliğin iki yüzü ve ikincisi ancak yazıldığı yerde tazelenebilir (desen 20 ile eş).
