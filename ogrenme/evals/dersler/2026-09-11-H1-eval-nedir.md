# Eval nedir, neden test≠eval — ders 1 (2026-09-11; ogren v0.1)

## Ön-bağlam
yok

## Anlayış haritası
| İplik | Seviye | Kanıt (soru no) |
|---|---|---|
| Yazılım testi / assert kavramı | yok | S1 |
| LLM çıktısının stokastik doğası | temel | S2 (temel ✓), S3 (ileri ✗) |
| Temel istatistik / ölçüm (accuracy) | temel | S4 (temel ✓, emin değil notu), S5 (precision/recall ✗) |
| YAML söz dizimi | yok | S6 |
| promptfoo / eval araç ekosistemi | yok | S7 |

## Plan
DAG görseli: bkz. sohbetteki mcp__visualize çıktısı (bu oturuma özgü, kalıcı kopya gerekirse `raporlar/gorsel-2026-09-11-evals-h1-dag.html`).

Düğüm listesi (sınırın üstü, ≤8 düğüm):
1. Birim testi nedir (İplik 1 sıfırdan)
2. Eval nedir, test'ten farkı (İplik 2 sınırını aşar: stokastiklik → tam-eşleşme neden yetmez)
3. Eval bileşenleri: görev · vaka · metrik · yargıç
4. 3 katman: uçtan-uca / trajektori / bileşen
5. Regresyon seti fikri
6. YAML ile eval vakası yazımı (İplik 4 sıfırdan)
7. promptfoo ile 1 koşum (İplik 5 sıfırdan)
8. pass@k formülü + elle örnek (Karar 73)

## Düğümler
### Kutu 1 — Birim testi nedir
- Akıl-adımı: unit test = sabit girdi için sabit beklenen çıktıyı kontrol eden assert; eşitse PASS, değilse FAIL.
- Örnek: `assert topla(2,3)==5`.
- Soru: `kare(4)` 15 döndürürse ne olur? → Cevap: FAIL (gerçek≠beklenen). Sonuç: **DOĞRU**.

### Kutu 2 — Eval nedir, test'ten farkı
- Akıl-adımı: LLM çıktısı stokastik → tam-eşleşme assert yetersiz; eval = metrik/yargıçla esnek değerlendirme.
- Örnek: "Paris" vs "Fransa'nın başkenti Paris'tir" — assert FAIL eder, eval doğru sayabilir.
- Soru: test/eval farkını özetleyen seçenek → Cevap: a (sabit beklenen vs metrik/yargıç). Sonuç: **DOĞRU**.

### Kutu 3 — Eval bileşenleri: görev · vaka · metrik · yargıç
- Akıl-adımı: görev (iş) · vaka (somut örnek) · metrik (ölçme kuralı) · yargıç (metriği uygulayan: kod/insan/LLM).
- Örnek: görev "toplama çöz", vaka 23+45=?/68, metrik exact match, yargıç = Python eşitlik kodu.
- Soru: bu kurulumda yargıç kim? → Cevap: a (Python eşitlik kontrolü). Sonuç: **DOĞRU**.

### Kutu 4 — Üç katman: uçtan-uca / trajektori / bileşen
- Akıl-adımı: uçtan-uca=son çıktı · trajektori=araç-çağrısı yolu · bileşen=tek parça izole test.
- Örnek: hava durumu ajanı — uçtan-uca son cümle, trajektori API çağrı sırası, bileşen yorumlama adımı.
- Soru: doğru API sırasını ara adımdan kontrol eden katman? → Cevap: a (trajektori). Sonuç: **DOĞRU**.

### Kutu 5 — Regresyon seti fikri
- Akıl-adımı: geçmiş gerçek hataların vaka olarak biriktiği kalıcı set; her değişiklikte koşulur, hatanın geri gelmediği kontrol edilir.
- Örnek: geçmiş üretim hatası "23+45=?"→yanlış cevap → sete eklenir, sonraki koşumlarda tekrar denetlenir.
- Soru: regresyon setinin temel amacı? → Cevap: a. Sonuç: **DOĞRU**.

### Kutu 6 — YAML ile eval vakası yazımı
- Akıl-adımı: YAML = anahtar:değer + liste + girinti ile veri yapısı; eval vakası vars/assert alanlarıyla yazılır.
- Örnek: `tests: - vars: {soru:...} assert: - type: contains, value: "68"`.
- Soru: `value: "68"` ne demek? → Cevap: a (beklenen/aranan değer). Sonuç: **DOĞRU**. (Salih: terim hatırlatması istendi, glossary verildi.)
- Mini pratik düzeltmesi: yeni vaka eklerken mevcut `vars` bloğuna satır eklenmez — `tests:` listesine yeni bağımsız `-` elemanı (kendi vars+assert'iyle) açılır. Sonuç: **AÇIK** (kavram genel olarak doğru, liste-mekanizması ilk denemede net değildi, düzeltmeyle devam edildi).

### Kutu 7 — promptfoo ile 1 koşum
- Akıl-adımı: promptfoo = YAML'daki vakaları okuyup modeli çağıran, assert'e göre PASS/FAIL hesaplayan CLI aracı.
- Örnek: config'te prompt şablonu + provider + tests; `promptfoo eval` 20 satırlık sonuç tablosu üretir.
- Soru: `promptfoo eval` ne yapar? → Cevap: a. Sonuç: **DOĞRU**.
- Salih notu: sadece okunan örnek yeterli değil, bizzat yapılan bir mini-pratik adımı istendi → kutu 6/7 sonrasına "şimdi sen dene" eklendi; haftalık DONE zaten bunun genişletilmiş hali.

### Kutu 8 — pass@k formülü (Karar 73)
- Formül: pass@k = 1 − C(n−c,k)/C(n,k); n=deneme sayısı, c=doğru sayısı, k=alt-küme boyutu.
- Elle örnek: n=5,c=2,k=1 → C(3,1)/C(5,1)=3/5 → pass@1=0,4.
- Soru: n=4,c=1,k=1 → Cevap: a (0,25). Sonuç: **DOĞRU**.
- Ek vaka (Salih istedi): "17 asal mı?" 4 kez soruldu, 1'i doğru → pass@1=1/4=0,25, formülle tutarlı.

## AÇIK düğümler
- Kutu 6: YAML liste-mekanizması (`tests:` altında her `-` bağımsız bir vaka) ilk denemede net değildi; düzeltmeyle geçildi. Sonraki derste hızlı hatırlatma faydalı olabilir.

## Salih notu
- Kutu 6-7 arası: "somut örnek okumak yetmiyor, bizzat yapayım" → mini pratik eklendi, kalıcı kural adayı olarak hafızaya da işlendi (feedback-ders-elle-pratik-adimi).

## Kalan
(yok — 8/8 düğüm işlendi)
