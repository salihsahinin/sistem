# Büyük harf vurgusu neden sürüyor — kök neden + düzeltme (2026-09-17, Fable ana-sıra; Salih emri "analiz et ve çöz")

*Vaka: Sonnet güvenlik yan oturumu (worktree `2026-09-15-guvenlik-2-4bfcd1`), 09-17 13:26 `g3_denetim_simulasyon` widget'ı: "iki AYRI sunucudan", "BİRLİKTE bağlı" (JS dizesi içinde). Karar 97 (09-15) kanonu temizlemişti; buna rağmen çıktı kirli. Önceki analiz: `raporlar/2026-09/buyuk-harf-vurgu-analizi-2026-09-15.md`.*

## Kök neden (üç bağımsız mekanizma, üçü de ölçüldü)
| # | Mekanizma | Kanıt | Etki |
|---|---|---|---|
| 1 | **Bayat worktree = bayat kanon.** Yan oturumun dalı `3ccf46e`'den açıldı; Karar 97 temizliği (`1c73369`) ondan sonra. Worktree'nin yüklediği CLAUDE.md 30, kapsül 39, rules/ogrenme 4 çıplak caps taşıyor (main'de 0). | `git merge-base` = 3ccf46e; `caps-say.py` worktree/main karşılaştırması | Model kuralı okuyor ama bağlamdaki ~70 örneği taklit ediyor (09-15 analizi: taklit > kural) |
| 2 | **Yan oturumda Stop hook ölü.** Worktree'nin settings.json'u göreli yol taşıyor (`bash .claude/hooks/…`, düzeltme `a59db3b` worktree'de yok). Transkriptte 34/36 Stop hook çağrısı "No such file or directory"; toplam 71 hook hatası (pretool-core-tel 8, altajan-okuma 12, userprompt-dosya 17). | transkript `465f66eb…jsonl` grep | Fren hiç çalışmadı; iki "Stop hook feedback" satırı yalnız cwd'nin rastgele doğru olduğu turlarda |
| 3 | **Hook yalnız metni tarıyordu.** Caps sözcükler `show_widget.widget_code` JS dizesindeydi; hook v0.2 son asistan *metnini* okur, araç girdisini okumaz. Hook çalışsaydı da yakalamazdı. | widget içeriği taraması: `AYRI`, `BİRLİKTE` script dizesinde | Görsel/dosya çıktıları frensiz |
| + | **Öğrenme dosyaları hiç temizlenmemişti.** Karar 97 kapsamı sıcak+ılık kanon; `ogrenme/` "soğuk/tarihçe" sayılmış. Oysa ogren skill'i her açılışta kurs README + ilerleme + önceki dersi okur: guvenlik README 10, ilerleme 8, G1 dersi 19 caps. | `caps-say` taraması: 25 canlı dosyada 291 ihlal | Yan oturumun en yakın örnekleri kirliydi |

Sonuç: sorun modelin "saçmalaması" değil; yan oturum Karar 97'nin hiçbir parçasını (temiz kanon · çalışan hook · temiz ders dosyaları) görmedi. Ana-sırada aynı dönemde ihlal 0.

## Düzeltme (uygulandı, Katman-2)
1. **Stop hook v0.3** (`.claude/hooks/stop-buyuk-harf.sh`): son turun araç girdileri de taranır — `show_widget.widget_code` (etiket/CSS düşer, JS dizeleri kalır), `Write.content`, `Edit.new_string`. Test 10/10 (3 yeni vaka).
2. **`ogrenme` katmanı** `tools/buyuk-harf-temizle.py`'ye eklendi (README · mufredat · şerit README · ilerleme · dersler · eval-seti md'leri); uygulandı: 25 dosya, 187 vurgu → kalın, 104 durum → jeton. Kalan 229 ihlal eski jarvis-müfredat ders kayıtlarında (`ogrenme/dersler/2026-07…08`, `problem-cozme`, `anlama-kapisi`) — yan oturumlar okumuyor, tarihçe; İB-102 eşlemesi açarsa o gün temizlenir.
3. **Pre-commit teli** artık `ogrenme/**/*.md`'yi de sayar.
4. **Açılış kapısı K1** worktree'nin main'in kaç commit gerisinde olduğunu ve hook yollarının eski olup olmadığını yazar; geride ise "yan oturumu kapat, merge, main'den yeni worktree" der. Bugün: 15 commit geride + hook eski.

## Salih'in eli (tek adım)
Sonnet güvenlik oturumunu kapat → ben dalı merge ederim → yeni yan oturum main'den worktree açar (Karar 95 EK zaten böyle der; guvenlik-2 dalı o karardan önce açılmıştı). Yeni oturum temiz kanon + çalışan hook v0.3 + temiz ders dosyalarıyla başlar. Ölçüm: yeni oturumun ilk 3 dersinde widget dahil ihlal sayısı (hedef 0; Karar 97 ölçümü kanıt-kapılı, Karar 98 EK-1).
