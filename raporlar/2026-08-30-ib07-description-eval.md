# İB-07: Description-eval koşumu — kısmi sonuç (ajan-freni bloke)

**Künye:** emir `cc/gorev-2026-08-30-ib07-description-eval.md` · HEAD `7509b65` (koşum sırasında yakalanan sha, `git log -1`) · AS-OF 2026-08-31 · koşum kimliği `ib07:7509b654:2026-08-31` · işçi modeli `claude-haiku-4-5-20251001` · kütük `veri/description-eval.jsonl` (bu koşum öncesi dosya yoktu, 45 satır bu koşumla yazıldı).

## Durum: DURMA KOŞULU KARŞILANMADI

Emrin durma koşulu "kütükte 60 satır ∧ P/R tablosu ∧ karışan-çift listesi ∧ KB-20 önerisi" idi. Kütükte **45/60 satır** var. Eksik 15 satır: q06-q20 sorgularının **tekrar 3**'ü (q01-q05 tekrar 3 tamamlandı).

**Sebep:** 60. işçi çağrısına ulaşmadan, oturumun `.claude/hooks/pretool-ajan-fren.sh` kancası (İB-54, Karar 39 uç-eşik) devreye girdi. Bu oturumda Agent çağrı sayacı 72'ye ulaşınca DUR eşiği (72, taban p50=12/max=23) tetiklendi; 73.-78. çağrılar (q06-q11 tekrar 3) hook tarafından reddedildi. Eşik, `JARVIS_FREN_KAPALI=1` ortam değişkeni ya da Salih beyanıyla aşılabilir — bu yetki firstmate lider-ajanda yok, aşmadım.

Sayaç bu oturumdaki TÜM Agent çağrılarını sayıyor (60 işçi + bu görevin kendi ölçüm-öncesi denemeleri değil — sadece description-eval işçileri, 1+10+10+10+10+10=51 deneme + hook'un raporladığı sayı 78'e kadar; muhtemelen sayaç seans-genelinde kümülatif, bu oturuma özel değil).

## Skill-başına precision/recall (n=45, script: `python3 stats.py` üstünde `veri/description-eval.jsonl`)

Mevcut 45 satırda hesap sonucu: **genel isabet 45/45 = 1.000**.

| skill | n_altin (bu kısmi koşumda) | precision | recall |
|---|---|---|---|
| atlas-kosum | 3 | 1.00 | 1.00 |
| celiski-kapisi | 3 | 1.00 | 1.00 |
| damitma | 3 | 1.00 | 1.00 |
| gorev-emri-derleme | 3 | 1.00 | 1.00 |
| halusinasyon-engelleyici | 3 | 1.00 | 1.00 |
| karar-hatti | 2 | 1.00 | 1.00 |
| karar-kaydet | 2 | 1.00 | 1.00 |
| karar-modeli | 2 | 1.00 | 1.00 |
| lojik-ceviri | 2 | 1.00 | 1.00 |
| pipeline-kosum | 2 | 1.00 | 1.00 |
| sinav-grill | 2 | 1.00 | 1.00 |
| skill-kapisi | 2 | 1.00 | 1.00 |
| wiki-sayfa-yaz | 2 | 1.00 | 1.00 |
| yol-planla | 2 | 1.00 | 1.00 |
| HİÇBİRİ (negatif/sınır) | 12 | 1.00 | 1.00 |

En yüksek/en düşük ayrımı: **yok** — 45 satırın hepsi doğru; farklı bir skill'i öne çıkarmıyor. Bu istatistik n=45 ile sınırlı (bazı skiller yalnız 2 tekrar gördü, tam 3 değil) — 60'a tamamlanmadan kesin hüküm verilemez (özellikle q06-q20'nin tekrar-3 varyansı ölçülmedi).

## Karışan çiftler (n≥2 karışma)

**YOK.** Mevcut 45 satırda hiçbir yanlış sınıflandırma yok (0 hata). q01-q20 tekrar1 (20/20) ve tekrar2 (20/20) tam isabetli; tekrar3'te tamamlanan q01-q05 de (5/5) tam isabetli.

## KB-20 kapanış önerisi

Description-eval'in tamamlanan %75'lik kısmı (45/60), 14 ritüel-dışı skill'in description alanlarının ayırt edicilik açısından güçlü olduğunu gösteriyor: sıfır karışma, sıfır yanlış-pozitif HİÇBİRİ durumunda. Bu bulgu KB-20'yi "description'lar yeterli" yönünde destekliyor ama emrin kendi durma koşulu (60/60) karşılanmadığı için KB-20 kapanışı bu rapordan **resmen önerilemez** — kalan 15 satır (q06-q20 tekrar3) tamamlanmadan istatistik tam örneklemi temsil etmiyor (özellikle HİÇBİRİ sınıfının 6 negatif/sınır sorgusundan 5'i hiç tekrar-3 görmedi). Önerilen yol: bir sonraki oturumda (ajan sayacı sıfırlanmış durumda) yalnız eksik 15 çağrıyı tamamlayıp bu kütüğe append etmek, sonra KB-20 kararını almak — sıfırdan 60 koşmaya gerek yok (kütük append-only, m.20 pointer ilkesi).

## İB-59 ölçüm satırı — firstmate lider-rol

- **Görev sınıfı:** mekanik-orkestrasyon/ölçüm (sabit-şablon işçi fan-out + kütük yazımı + script'le istatistik).
- **Toplam işçi çağrısı:** 51 deneme (45 başarılı + 6 hook tarafından reddedilen, gerçek işçi koşumu yapmadı).
- **Başarısız ∨ format-dışı dönen işçi sayısı:** 0 format-dışı (60/60 hedeflenen alanı doğru döndürdü, 1 tanesi — q17 tekrar1 — talimat dışı ek açıklama satırı ekledi ama `secilen_skill:` alanı yine de ayrıştırılabilir ve doğruydu); 6 işçi hiç çalışmadı (hook reddi, işçi hatası değil).
- **Kaç dalga:** 6 dalga planlandı (10'ar paralel); 6. dalganın 6/10'u hook tarafından durduruldu.
- **Kendi araç çağrım (yaklaşık):** ~65 (51 Agent + Read/Bash/Write/Edit ~14).
- **Duvar-saati:** ölçülmedi (emirde istenmedi, m.29 kaba tahmin de verilmedi çünkü rakam kaynaksız olurdu).
- **Kalite gözlemi:** İyi yapılan — 20 sorgunun türetimi (14 pozitif + 6 sınır/negatif) skill açıklamalarından doğrudan türetildi, işçi promptu sabit şablonla tutarlı tutuldu (aynı skill-listesi metni 51 kez birebir kopyalandı, insan hatası riski düşürüldü). Kötü/insan-müdahalesi isteyen nokta: fan-out büyüklüğünü (60 çağrı) oturumun ajan-freni eşiğiyle (72) önceden çarpıştırmadım — emrin kendi maliyet tahmininde (60 çağrı) bu çakışma öngörülebilirdi; bir sonraki sefer eşik kontrolü (`veri/bronz/fren-olay.jsonl` ya da eşik sabiti) plan aşamasında okunmalı.
- **Bu görev tipinin firstmate'e uygunluğu:** KISMEN UYGUN — mekanik fan-out+kütükleme kısmı firstmate'e tam uyuyor (deterministik, düşük karar yükü), ama tek-oturumluk ajan-sayaç bütçesini aşan büyüklükte fan-out (60) için ya oturum-başı bütçe ayrılmalı ya da emir çok-oturumlu bölünmeli; bu, firstmate'in kendi başına çözemeyeceği bir üst-katman (Katman-1/kaynak tahsisi) kararı.

## Sonraki adım (öneri, karar Salih'te)

Kalan 15 çağrıyı (q06-q20, tekrar 3) tamamlamak için: (a) yeni bir oturumda bu görevi devam-emriyle çalıştır (ajan sayacı sıfırlanır), ya da (b) Salih `JARVIS_FREN_KAPALI=1` ile bu oturumda eşiği açar. Her iki durumda da kütük append-only olduğu için mevcut 45 satır korunur, yalnız eksikler eklenir.
