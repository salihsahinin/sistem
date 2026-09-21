# LLM-as-judge I: rubrik yazımı · konum/uzunluk yanlılığı · çift-değerlendirme — ders 3 (2026-09-11; ogren v0.1)

## Ön-bağlam
H1-H2'den taşınan: eval bileşenleri (görev/vaka/metrik/yargıç — kutu 3, H1), yargıcın insan/kod/LLM olabileceği (H1 kutu 3), deterministik metriklerin sınırı (H1 basarisizlik-analizi: yüzeysel metrik *neden*i açıklamıyor). Bu ders tam da o boşluğu (LLM-as-judge) dolduruyor.

## Anlayış haritası
| İplik | Seviye | Kanıt |
|---|---|---|
| LLM-as-judge kavramı | yok | S1 |
| Rubrik | yok | S2 |
| Konum/uzunluk yanlılığı | ileri (tavan) | S3 (tahmin ✓), S4 (✓) |
| Çift-değerlendirme | yok | S5 |
| Şans-düzeltmeli uyum (κ'nın nedeni) | yok | S6 |

## Plan
DAG görseli: sohbetteki mcp__visualize çıktısı.

Düğüm listesi (≤8):
1. LLM-as-judge nedir (sıfırdan)
2. Rubrik yazımı (sıfırdan, örnekli)
3. Yanlılıkları azaltma pratiği (kısa — iplik zaten ileri seviyede)
4. Çift-değerlendirme nasıl yapılır (sıfırdan)
5. Şans payı kavramı — neden ham yüzde uyum yeterli değil
6. Cohen κ formülü + sembol tablosu + elle örnek (Karar 73)
7. DeepEval G-Eval tanıtımı (hazırı temel al)
8. `DONE` tanıtımı: 10 vakaya rubrikli yargıç, kendi elle puanla karşılaştır

## Düğümler
### Kutu 1 — LLM-as-judge nedir
- Akıl-adımı: başka bir LLM'i yargıç olarak kullanma; nitel/öznel kriterlerde deterministik metriğin yetersiz kaldığı yeri doldurur.
- Örnek: chatbot cevabını kibarlık/doğruluk/özlülük kriterleriyle yargıç LLM'e puanlatmak.
- Soru: neden contains yerine LLM-as-judge? → Cevap: b (nitel kriter, yargılama gerektirir). Sonuç: **DOĞRU**.

### Kutu 2 — Rubrik yazımı
- Akıl-adımı: kriter+puan ölçeği+gerekçe → tutarlılık/yanlılık azaltmanın temeli.
- Örnek: doğruluk kriteri için 5/3/1 puan tanımları.
- Soru: rubrik neden iyi? → Cevap: b. Sonuç: **DOĞRU**.

### Kutu 3 — Yanlılıkları azaltma pratiği
- Akıl-adımı: konum yanlılığını **test** etmek için A-B/B-A iki sıralı koşum; uzunluk yanlılığını **azaltmak** için rubrikte "uzunluk kriter değil" ifadesi.
- Örnek: çeviri A/B karşılaştırması iki sırayla, sonuç değişirse yanlılık kanıtı.
- Soru: konum yanlılığını test etme yolu? → Cevap: d. Sonuç: **DOĞRU**.

### Kutu 4 — Çift-değerlendirme nasıl yapılır
- Akıl-adımı: insan + yargıç LLM aynı vakaları **bağımsız** puanlar (birbirini görmeden), sonra karşılaştırılır.
- Örnek: 10 çözüm, Salih ayrı puanlar, yargıç LLM ayrı puanlar, sonra sütunlar karşılaştırılır.
- Soru: neden bağımsız puanlama önemli? → Cevap: b (çapraz kirlenme riski). Sonuç: **DOĞRU**.

### Kutu 5 — Şans payı kavramı
- Akıl-adımı: rastgele kararlarda bile belli bir şans-eseri uyum beklenir; ham yüzde bunu çıkarmaz, şişirilmiş görünür.
- Örnek: hep "doğru" diyen yargıç, %80 doğru vaka setinde %80 ham uyum verir ama ayırt etme yeteneği yoktur.
- Soru: bu %80 neyi yanlış gösterir? → Cevap: a. Sonuç: **DOĞRU**.

### Kutu 6 — Cohen κ formülü (Karar 73)
- Formül: κ=(p_o−p_e)/(1−p_e); p_o=gözlenen uyum, p_e=şans-eseri beklenen uyum.
- Elle örnek: 2×2 tablo (İnsan 7 doğru/3 yanlış, LLM 6/4, uyuşma 5+2=7) → p_o=0,7, p_e=0,54, κ≈0,348.
- Soru: p_o=0,8,p_e=0,5 → κ? → Cevap: b (0,6). Sonuç: **DOĞRU**.

### Kutu 7 — DeepEval G-Eval (hazırı temel al)
- Akıl-adımı: `GEval(criteria=..., evaluation_params=..., threshold=...)` — rubrik fikrinin hazır kütüphane hali. (Canlı doğrulandı: deepeval README 2026-09-11.)
- Örnek: `criteria="Determine if actual output is correct based on expected output"`.
- Soru 1: `criteria` neye karşılık gelir? → Cevap verilen: e (bilmiyorum, yanlış). Düzeltme yapıldı.
- Soru 2 (tekrar, farklı açıdan): kutu 2'deki rubrik neyi tanımlıyordu? → Cevap: b. Sonuç: **AÇIK** (ilk denemede kaçırıldı, düzeltmeyle geçildi).

### Kutu 8 — done tanıtımı: 10 vakaya rubrikli yargıç, elle puanla karşılaştır
- Akıl-adımı: rubrik (kutu2) + yargıç LLM (kutu1,7) + elle bağımsız puan (kutu4) + κ (kutu6) — hepsi tek pratikte birleşiyor. Bu adım (elle puanlama) otomatikleştirilemez, Salih'e ait.
- Altyapı hazırlandı: `h3-eval-seti/` (AKIS.md 4 adımlı akış, eval-seti-plain.yaml/eval-seti-judge.yaml, elle-puanlama.md worksheet). Koşum ve elle puan Salih'i bekliyor.

## Açık düğümler
- Kutu 7: `GEval`/`criteria`'nın rubrik karşılığı olduğunu ilk denemede bağlayamadı; düzeltmeyle geçildi.

## Salih notu

## Kalan
(yok — 8/8 düğüm işlendi)

## Done (haftalık çıktı — kısmi, Salih'in elle puanı bekleniyor)
- `h3-eval-seti/AKIS.md`: 4 adımlı bağımsız çift-değerlendirme akışı.
- `h3-eval-seti/eval-seti-plain.yaml` (yargısız, kör çıktı) + `eval-seti-judge.yaml` (llm-rubric, pass=doğru/fail=yanlış).
- `h3-eval-seti/elle-puanlama.md`: Salih'in dolduracağı worksheet.
- **Sonuç (2026-09-14):** Salih'in elle puanı: 8 doğru/2 yanlış (Carlos #6, İki tren #8 — trenler yeni bir hata, ilk kez görüldü). Yargıç LLM (`llm-rubric`): 8 pass/2 fail — **aynı 2 vaka**. p_o=1,0, p_e=0,68, **κ=1,0** (10/10 tam uyum).
- Not: n=10 küçük örneklem; tek koşumluk bu sonuç genel bir "yargıç kusursuz" iddiası değildir, ama H4 hedefi (κ≥0,6) rahatça aşıldı.
- Ek gözlem: Josh (%150 artış) vakası bu koşumda **doğru** çıktı (70000) — H1/H2'de hep 195000 diyordu; model stokastikliğinin (kutu 2, H1) canlı örneği. Trenler vakası ise yeni bir hata — regresyon setine eklenmeye aday, tek koşumda henüz teyitsiz.
