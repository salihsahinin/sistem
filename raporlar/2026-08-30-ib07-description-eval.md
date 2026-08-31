# İB-07: Description-eval koşumu — TAMAMLANDI (60/60)

**Künye (1. tur):** emir `cc/gorev-2026-08-30-ib07-description-eval.md` · HEAD `7509b65` (koşum sırasında yakalanan sha) · AS-OF 2026-08-31 · koşum kimliği `ib07:7509b654:2026-08-31` · işçi modeli `claude-haiku-4-5-20251001` · kütük `veri/description-eval.jsonl` — 45/60 satır yazıldı, kesintiye uğradı.

**Künye (2. tur — tamamlama):** HEAD `e8909f5` (`git rev-parse --short HEAD`, koşum başında) · AS-OF 2026-08-31 · koşum kimliği `ib07-ek:e8909f5:2026-08-31` · işçi modeli `claude-haiku-4-5-20251001` (Agent tool `model: "haiku"`) · kütük aynı dosya, append-only, eski 45 satıra dokunulmadı — eklenen 15 satır (q06-q20, tekrar 3).

## Kesinti tarihçesi (m.8: eski bulgu silinmez, not olarak korunur)

1. tur (2026-08-30/31), 45. işçi çağrısından sonra oturumun `.claude/hooks/pretool-ajan-fren.sh` kancası (İB-54, Karar 39 uç-eşik) devreye girdi — Agent çağrı sayacı 72'ye ulaşınca DUR eşiği tetiklendi, 73.-78. çağrılar (q06-q11 tekrar 3) reddedildi. Firstmate'te eşik-aşma yetkisi yoktu, koşum kısmi (45/60) durumda kapatıldı ve rapor "kısmi sonuç (ajan-freni bloke)" başlığıyla teslim edildi.

2. tur (2026-08-31), fren revize edilip pay açıldıktan sonra emir `cc/gorev-2026-08-30-ib07-description-eval.md` yeniden koşuldu: kalan 15 hücre (q06-q20 × tekrar 3) 5 dalga hâlinde, dalga başına 3 senkron Agent çağrısıyla (`run_in_background: false`) tamamlandı, her dalga sonrası kütüğe append edildi. Toplam bu turda 15 Agent çağrısı; hook reddi görülmedi.

## Eksik hücre doğrulaması (adım 1, python ile)

```
c=Counter(sorgu_id for row in jsonl)  # koşum öncesi
q01-q05: 3'er tekrar (tam) · q06-q20: 2'şer tekrar (eksik tekrar-3) → eksik = 15×tekrar3
```
Koşum öncesi 45 satır, `q06`-`q20` her biri 2 kez (tekrar 1-2), `q01`-`q05` her biri 3 kez — eksik tam olarak **q06-q20 tekrar 3 = 15 hücre** olarak doğrulandı, hesapla değil script ile.

## Kütük

Ekleme sonrası satır sayısı python ile doğrulandı: **60/60**, her `sorgu_id` tam 3 kez geçiyor, eksik/fazla yok.

## Skill-başına precision/recall (n=60, script ile hesaplandı)

```python
tp[g]+=1 if altin_etiket==secilen_skill else fp[secilen]+=1; fn[altin]+=1
```

**Genel isabet: 60/60 = 1.000**

| skill | TP | FP | FN | precision | recall |
|---|---|---|---|---|---|
| atlas-kosum | 3 | 0 | 0 | 1.00 | 1.00 |
| celiski-kapisi | 3 | 0 | 0 | 1.00 | 1.00 |
| damitma | 3 | 0 | 0 | 1.00 | 1.00 |
| gorev-emri-derleme | 3 | 0 | 0 | 1.00 | 1.00 |
| halusinasyon-engelleyici | 3 | 0 | 0 | 1.00 | 1.00 |
| karar-hatti | 3 | 0 | 0 | 1.00 | 1.00 |
| karar-kaydet | 3 | 0 | 0 | 1.00 | 1.00 |
| karar-modeli | 3 | 0 | 0 | 1.00 | 1.00 |
| lojik-ceviri | 3 | 0 | 0 | 1.00 | 1.00 |
| pipeline-kosum | 3 | 0 | 0 | 1.00 | 1.00 |
| sinav-grill | 3 | 0 | 0 | 1.00 | 1.00 |
| skill-kapisi | 3 | 0 | 0 | 1.00 | 1.00 |
| wiki-sayfa-yaz | 3 | 0 | 0 | 1.00 | 1.00 |
| yol-planla | 3 | 0 | 0 | 1.00 | 1.00 |
| HİÇBİRİ (negatif/sınır, 6 sorgu × 3) | 18 | 0 | 0 | 1.00 | 1.00 |

En düşük P/R skill'i: **yok** — n=60'ın tamamı doğru sınıflandı, hiçbir skill diğerlerinden geride değil.

## Karışan çiftler (n≥2 karışma, n=60 ile yenilendi)

**YOK.** 60 satırın tamamında 0 hata; `(altın_etiket, seçilen_skill)` çiftlerinden hiçbiri farklı değil. 1. turdaki "karışma yok" bulgusu 2. turla birlikte n=60'ta da doğrulandı — yeni bir karışma çıkmadı.

## KB-20 kapanış önerisi

Description-eval **tamamlandı**: n=60'ta genel isabet 1.000, skill-başına precision/recall tamamı 1.00/1.00, sıfır karışan çift. Bu, 14 ritüel-dışı skill'in description alanlarının bu altın sorgu setine karşı tetikleme açısından tam ayırt edici olduğunu gösteriyor — description-eval borcu (K-016) bu ölçüm turunun done-yüklemi açısından **KAPANABİLİR**.

**ZORUNLU KALICI ŞERH (Salih emri, aynen taşınıyor):** altın sorgu setini **ölçülen sistemin kendisi türetti** (içeriden türetilmiş set); bu, sonucu yukarı yanlı kılabilir — bağımsız sorgu seti olmadan bu ölçüm skill-tetikleme doğruluğunun **ÜST SINIRINI** verir, gerçek beklenen başarımı değil. n=60'a tamamlanmış "mükemmel" skor bu şerhi güçlendiriyor: aynı sistemin ürettiği sorgularda %100 isabet, description'ların bağımsız/gerçek kullanıcı ifadelerine karşı ne kadar sağlam olduğu hakkında hiçbir şey söylemiyor. KB-20 kapanışı bu üst-sınır çerçevesiyle kayda geçmeli; bağımsız sorgu setiyle yeniden ölçüm ayrı bir borç olarak açık kalabilir.

**Şablon-farkı şerhi (emirde istenen `[?]`):** 2. tur işçilerine verilen 14-skill listesi metni 1. turun şablonuyla karakter-birebir aynı olduğu GARANTİ EDİLEMEZ — 2. tur, `.claude/skills/*/SKILL.md` dosyalarından bu oturumda yeniden okunan description'larla kuruldu; 1. tur promptu bu oturumda görülmedi, yalnız kütükteki sonuçlar görüldü. İçerik anlamca aynı (kaynak dosyalar değişmedi, m.16/görev yasağı gereği dokunulmadı) ama biçimsel forma­tlama (madde numarası, satır sonları) 1. ve 2. tur arasında farklı olabilir. Bu, tekrar-1/2 kolu (1. tur şablonu) ile tekrar-3 kolu (2. tur şablonu) arasında düşük ama sıfır olmayan bir ölçüm-tutarlılığı riski taşır `[?]`.

## İB-59 ölçüm satırı — 2. tur (firstmate lider-rol, tamamlama koşumu)

- **Görev sınıfı:** mekanik-orkestrasyon/ölçüm (sabit-şablon işçi fan-out + kütük append + script'le istatistik), 1. turun devamı.
- **Toplam işçi çağrısı (2. tur):** 15 Agent çağrısı (haiku, araçsız, tek-alan dönüş) — planlanan 15/15 tamamlandı.
- **Format-dışı dönen işçi sayısı:** 0/15 — her çağrı `secilen_skill: <ad>` tek satırını tam beklenen biçimde döndürdü, ayrıştırma sorunu yaşanmadı.
- **Dalga sayısı:** 5 dalga, dalga başına 3 senkron çağrı (emirde istenen 3'erli/5 dalga deseniyle birebir); her dalga sonrası kütüğe append edildi (5 append işlemi + 1 doğrulama).
- **Senkron disiplin gözlemi:** tüm 15 çağrı `run_in_background: false` ile, arka plana atıp beklemeden yapıldı; hiçbir çağrı hook/ajan-freniyle reddedilmedi (1. turdaki kesintiye neden olan eşik bu turda aşılmadı — pay yeterliydi).
- **Kendi araç çağrım (yaklaşık, 2. tur):** ~21 (15 Agent + Bash ~5 + Read/Write ~2).
- **Kalite gözlemi:** 1. turun sabit-şablon disiplini korundu (14-skill listesi metni 15 çağrıda birebir aynı); tek risk yukarıdaki şablon-farkı şerhi (1. tur ile 2. tur arası karakter-birebir eşleşme garanti edilemez).

## Kapanış

Emrin durma koşulu ("kütükte 60 satır ∧ skill-başına P/R tablosu ∧ karışan-çift listesi ∧ KB-20 önerisi") **karşılandı**. Sonraki adım Salih kararına bırakılıyor: KB-20'yi bu üst-sınır çerçevesiyle mi kapatmak, yoksa bağımsız sorgu setiyle ikinci bir ölçüm turu mu açmak.
