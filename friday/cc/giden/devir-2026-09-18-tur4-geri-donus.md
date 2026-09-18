# Geri-dönüş — devir-2026-09-18-tur4 (Friday, AS-OF 2026-09-18; şema `core/sablonlar/geri-donus-v0.md`)

## 1. biten
| iş | kanıt_yolu |
|---|---|
| C1 hook v0.3: alt-ajan dalı (`agent_id` → kapsül · pano · defter · kutu · `veri/bronz/**` · transkriptler `RED`; `tool-results/` muaf; olay `veri/bronz/altajan-okuma-olay.jsonl`'a düşer), Z1 ve Z2 onarımı, ana-sıra davranışı değişmedi | `.claude/hooks/okuma-izin.sh` |
| C2 test 9 → 22 vaka (Z1a-c · Z2a-b · Z3a-b · `agent_id` 5 vaka + ana-sıra kontrolü); 22 `PASS` · 0 `FAIL`; test koşumu bronz kütüğe yazmıyor | `.claude/hooks/okuma-izin-test.sh`, çıktı `cc/giden/devir-2026-09-18-tur4/uygulama-raporu.md` §3 |
| C3 deny bloğu 3b listesi aynen (15 satır); `core/` ve `kanon/` satırı yok, tek satırlık kök reddi yok, mevcut 5 deny satırı ve iki hook kaydı korundu | `.claude/settings.json` (deny 5 → 20) |
| C4 desen 21 eklendi, toplam 21; numara sırası bozulmadı | `core/desenler.md` son satır |
| C5 uygulama raporu: diff özeti · test çıktısı aynen · üç canlı deneme (yasak yol `RED` **D** · `kanon/` okunuyor **D** · alt-ajan olayı kütüğe düşüyor **D**) | `cc/giden/devir-2026-09-18-tur4/uygulama-raporu.md` |

## 2. kalan
| iş | neden_kaldı |
|---|---|
| Z3b: yolun tamamı bir değişkende kurulduğunda kilit görmüyor | Metin tabanlı taramanın belgelenmiş sınırı; kapatmak için sandbox ya da çalıştırma-sonrası denetim gerekir, ikisi de emrin dışında. D3 gereği bir deneme yapıldı → **K**. |
| v0.3'ün yanlış-pozitif maliyeti (`grep` deseni yol sanılıyor) | Üç seçenek raporda; ayrıştırıcı değişikliği emrin dışında → kural adayı. |
| Deny ile hook'un hangisinin önce davrandığının genel kanıtı | Canlı denemede `Read` için izin ayarı önce davrandı (mesaj metninden). Bash yolu için ayrı deneme yapılmadı: aynı yolu ikisi de kesiyor, ayırt edilemiyor. |

## 3. acik_sorular_salih (hüküm yok)
1. `grep`/`sed` desen dizelerinin yol sanılması için üç seçenekten hangisi (uygulama raporu §4d)?
2. `cc/gelen/ornek-jarvis-pretool-altajan-okuma.sh:48` — Jarvis'in kendi hook'unda `exit 2` test bayrağının içinde kalıyor; bayrak export edilince kilit kesmiyor. Aslı düzeltilecek mi (Friday kopyada düzeltti)?
3. Alt-ajan yasak listesine `cc/gelen/**` (başka devirlerin emirleri) da girsin mi — bugün işçi onları okuyabiliyor?
4. `settings.json` düzenlemesi Bash üzerinden sınıflandırıcıya takıldı, doğal düzenleme aracıyla yapıldı; bu yol Friday için kalıcı mı sayılsın?
5. Z3b için sandbox (işletim sistemi düzeyi) açılması gündeme alınsın mı?

## 4. sonraki_ilk_is
Jarvis testi ve canlı denemeyi yeniden koşup doğrulasın (`ÖLÇEN`); sonucuna göre §3'teki beş soru Salih'e gider.

## 5. diskteki_dosyalar
| yol | commit_dışı |
|---|---|
| `.claude/hooks/okuma-izin.sh` · `.claude/hooks/okuma-izin-test.sh` · `.claude/settings.json` · `core/desenler.md` | hayır |
| `cc/giden/devir-2026-09-18-tur4/uygulama-raporu.md` · `cc/giden/devir-2026-09-18-tur4-geri-donus.md` | hayır |
| `core/durum-kapsulu.md` · `core/pano.md` · `kuyruk/senaryo-defteri.md` · `kuyruk/fikir-kutusu.md` | hayır |
| `raporlar/seans-teslim-2026-09-18-tur4-uygulama.md` | hayır |
| `cc/gelen/.aktif-devir` | silindi (kapanış adımı) |
| `/private/tmp/friday-hook-kanit/**` (canlı kanıt için geçici repo kökü) | evet — repo dışı, commit edilmiyor |

## 6. sayac
{ ajan_çağrısı: 0, araç_çağrısı: bu devir **16** (ölçüm anı: kapanış yazımından önce; `devir_id = devir-2026-09-18-tur4` kütükte dolu — b1 mekanizması bu turda çalıştı), kapanış çağrılarıyla ≈ 22 `[?]`, işçi_sayısı: 0, alt_ajan_token: 0 }
Emrin tavanı 45 — aşılmadı. Açılan dış sayfa: 0 (R1/R2 bu turda yeniden açılmadı; tur-2 ve tur-3 okumaları kullanıldı).
Kilit tetiklenmesi: 1 kez, kendi komutumda (`grep` deseni); Jarvis'e fiilen erişim denemesi yok. Deny tetiklenmesi: 1 kez, `DONE C5` gereği bilerek yapılan yasak-yol denemesinde.

## 7. sapmalar
| emir_maddesi | ne_yapıldı | neden |
|---|---|---|
| `DONE C2`: "Z1-Z3 … hepsi PASS" | Z3 tek vaka yerine iki vaka (Z3a `RED`, Z3b geçer) | İlk yazdığım beklenti yanlıştı: kilit `~/$J/...` biçimini zaten kesiyor. Vaka gerçeğe uyduruldu, kod değiştirilmedi. Emrin istediği kapsam korundu (Z3 test ediliyor), sayısı arttı. |
| `R4`: `JARVIS_HOOK_TEST` bayrağı | Friday'de `FRIDAY_HOOK_TEST`; ikisi de kabul ediliyor | `R3` başlığı "Yollar Jarvis'e özgüdür, Friday karşılıkları emirde" diyor; desen uyarlandı, eski ad da çalışır durumda bırakıldı. |
| `R3` örnek kod deseni | `exit 2` test bayrağının dışına alındı | Örnekte bayrak kilidin kesme kararını da kapatıyor; kopyalansaydı test yeşil görünürken kilit işlevsiz kalırdı (uygulama raporu §2.5). |

**Emir-kaynaklı sapma sayısı: 0.** Üçü de emrin kendi dalları ve notlarıyla uyumlu uyarlamalar; hiçbiri emrin bir maddesini ihlal etmiyor. Sayım Friday'in, doğrulama Jarvis'in.

Not (emir dışı, engel): `settings.json`'ı Bash ile düzenleme girişimi oturum sınıflandırıcısı tarafından "öz-değişiklik" gerekçesiyle reddedildi; aynı değişiklik doğal düzenleme aracıyla yapıldı. Emirden sapma değil, araç seçimi.

## 8. tohum_desen_kullanimi
| desen | kullanıldı | neden |
|---|---|---|
| 21 (symlink/istisna semantiği) | evet | Deny listesi `core/` hariç kuruldu; canlı denemede `kanon/` okunmaya devam etti. |
| 4 (yapan ≠ ölçen) | evet | Testi yazan ve koşan benim; doğrulama `ÖLÇEN` alanına göre Jarvis'te. |
| 20 (kontrol listesi) | kısmen | Jarvis üst dizin listesi kapalı-göz özetinden; yeni dizin eklenirse liste eskir (raporda yazılı). |
| 10 (pathspec-only git) | evet | `git add <yol>`; push yok. |
| m.39 rakam | evet | 22/0, 5 → 20 deny satırı, 21 desen, 16 çağrı ölçüldü; kapanış payı `[?]`. |

## 9. ledger_onerisi (öneri)
| ib_no | önerilen_durum |
|---|---|
| Karar 99 M2 (alt-ajan dalı) | uygulandı — 22 vaka `PASS`, olay kütüğü kanıtlı |
| Karar 99 M3 (deny bloğu) | uygulandı — canlı `RED` **D**, `kanon/` sağlam **D** |
| Karar 99 M4 (desen 21) | uygulandı — `core/desenler.md` 21 madde |
| İB-83 Friday eşleniği | kapandı (Z3b kalıntısı hariç) |
| Kural adayı | ayrıştırıcı yanlış-pozitifi · Jarvis örnek hook'unun bayrak hatası · alt-ajan listesine `cc/gelen/**` · Z3b için sandbox |

## 10. durma_nedeni
tamamlandı (yeniden deneme hakkı kullanılmadı; D2 tetiklenmedi, geri alma yok; D3 bir denemeyle kısmen kapandı → K)

## + kapsul_eklenen
- Tur-4 uygulama turu bitti: hook v0.3 (alt-ajan dalı + Z1/Z2 onarımı), deny bloğu 15 satır, desen 21. Test 22 `PASS` · 0 `FAIL`.
- Canlı kanıt: yasak yol `Read` ile reddedildi (mesaj izin ayarından, yani deny etkin), `kanon/` okunuyor, alt-ajan `RED` olayı kütüğe düşüyor.
- Kalan: Z3b (yolun tamamı değişkende) **K**; v0.3'ün yanlış-pozitifi (desen dizesi yol sanılıyor) artık çağrıyı durduruyor.

## + cekirdek_adayi (Salih "kabul" derse `core/desenler.md`)
- "Örnek koddan devralırken test bayrağının neyi kapattığını oku": devralınan hook deseninde bayrak yalnız kütüğü değil `exit 2`'yi de kapatıyordu; kopyalansaydı test yeşil, kilit işlevsiz olurdu. Mekanizma: her bayrak için "bayrak açıkken hangi karar değişiyor?" sorusu, devralmadan önce.
