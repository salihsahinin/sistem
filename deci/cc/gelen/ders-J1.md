# Ders iskeleti J1 — Jev nedir: LLM ↔ karar modeli (Jarvis → Deci, 2026-09-22; Karar 105 M4 devir birimi)

`[tip: ders-iskelet | kaynak: jarvis-terminal 09-22 | tarih: 2026-09-22 | hedef: deci/ogrenme/jev | sema: ogren v0.3 | koken: jarvis/claude-fable-5-1/2026-09-22]`

Şerit: `ogrenme/jev` · hafta **J1** · README tablosu satırı J1. Sektör başlıkları AS-OF 2026-09-22 (kaynaklar README'de); ders başında canlı teyit (Karar 68). Bu dosya `PROBE` + `PLAN` + kutu başlıklarını taşır; `TEACH`/`CLOSE` ajanın işi.

## PROBE — iplikler (≤5) ve sorular (≤12; doğru şık konumu rastgele; (e) bilmiyorum sabit)
İplik 1 **olasılık kalibrasyonu** · 2 **LLM çıktı biçimi (metin ↔ yapısal)** · 3 **sınıflandırma temelleri** · 4 **API/SDK çağrı modeli** · 5 **maliyet/gecikme muhakemesi**.

1. (İplik 1, temel) "Model %70 dedi" ifadesinin **kalibre** olması ne demektir? (a) modelin 10 tahminden 7'sinde emin olması · (b) %70 dediği olayların uzun vadede ≈%70 gerçekleşmesi · (c) modelin doğruluk oranının %70 olması · (d) olasılığın 0,7'ye yuvarlanması · (e) bilmiyorum. **Doğru: b.**
2. (İplik 1, üst) Brier skoru 0 ile 1 arasında; hangi durumda **0**'dır? (a) her tahmin 0,5 · (b) tahminler rastgele · (c) her olaya doğru sonuca 1, yanlışa 0 olasılık verilmiş · (d) hiçbir tahmin yapılmamış · (e) bilmiyorum. **Doğru: c.**
3. (İplik 2, temel) Bir LLM'den "bu bileti hangi ekibe yönlendireyim" cevabı alırken çıktının yazılımda kullanılabilmesi için tipik ek adım nedir? (a) çıktıyı ayrıştırıp (parse) doğrulamak · (b) sıcaklığı yükseltmek · (c) daha uzun prompt · (d) modeli yeniden eğitmek · (e) bilmiyorum. **Doğru: a.**
4. (İplik 2, üst) "Structured output / JSON şeması" LLM'de neyi garanti eder, neyi etmez? (a) biçimi garanti eder, doğruluğu etmez · (b) doğruluğu garanti eder · (c) hem biçimi hem doğruluğu · (d) hiçbirini · (e) bilmiyorum. **Doğru: a.**
5. (İplik 3, temel) Üç sınıflı bir yönlendirme için modelin döndürdüğü `[0,1 · 0,7 · 0,2]` nedir? (a) sınıf başına maliyet · (b) sınıf üzerinde olasılık dağılımı · (c) üç ayrı karar · (d) güven aralığı · (e) bilmiyorum. **Doğru: b.**
6. (İplik 3, üst) Aynı dağılımda **entropi** neyi ölçer? (a) modelin hızını · (b) kararsızlık: dağılım düzleştikçe artar · (c) en yüksek olasılığı · (d) sınıf sayısını · (e) bilmiyorum. **Doğru: b.**
7. (İplik 4, temel) Bir API çağrısında "state + N soru tek geçişte" ne kazandırır? (a) N ayrı gidiş-dönüş yerine tek gecikme · (b) daha ucuz model · (c) daha uzun bağlam · (d) hiçbir şey · (e) bilmiyorum. **Doğru: a.**
8. (İplik 4, üst) `typesafe:jev-latest` gibi bir model adında `latest` ne risk taşır? (a) hiçbiri · (b) sürüm değişince davranış değişebilir, sabit sürüm (`jev-1.13.0`) tekrar-üretilebilirlik verir · (c) daha pahalı · (d) daha yavaş · (e) bilmiyorum. **Doğru: b.**
9. (İplik 5, temel) 1 M karar için model A 0,03 $/karar, model B 0,0002 $/karar; fark kaç kat? (a) ≈15 · (b) ≈150 · (c) ≈1.500 · (d) ≈15.000 · (e) bilmiyorum. **Doğru: b** (0,03/0,0002 = 150).
10. (İplik 5, üst) Ucuz karar modeli yanlış yönlendirirse maliyet nereden çıkar? (a) çıkmaz · (b) hata × hatanın maliyeti: beklenen zarar E = P(hata)·c · (c) yalnız token · (d) yalnız gecikme · (e) bilmiyorum. **Doğru: b.**

Ön-bağlam Salih verirse ("bildiklerim: …") o iplik atlanır. Çıktı: `## Anlayış haritası` (iplik · seviye · kanıt soru no).

## PLAN — DAG (görsel önce, `mcp__visualize`; düğüm numaralı; bilinen düğümler çıkar)
```
1 LLM çıktısı = metin (ayrıştırma + doğrulama yükü)
2 Karar = tip + olasılık (choice · score · noul)          ← 1
3 Kalibrasyon: Brier · ECE · reliability diagram         ← 2
4 Confidence = karar eşiğinden marj; entropi             ← 2, 3
5 RLCD: olasılık sonuca karşı eğitilir (satıcı beyanı)   ← 3
6 Satıcı rakamı ↔ bağımsız ölçüm (K/D ayrımı)           ← 3, 5
7 Ad: Jevons paradoksu → ucuz karar = daha çok karar     ← 6
8 "Ne değil": metin/kod üretmez, sayma/tarih zayıf, state adversarial değil ← 2
```
Kenarlar: 1→2 · 2→3 · 2→4 · 3→4 · 3→5 · 3→6 · 5→6 · 6→7 · 2→8. Derinlik: 2,3,4 [T] · 5,6 [O] · 1,7,8 [S]. Olgusal düğümler 5-6-7: `halusinasyon-engelleyici` derece; satıcı rakamları DESTEKLİ-K etiketiyle anlatılır.

## Kutu başlıkları (TEACH sırası = DAG topolojik sırası; ≤8 düğüm/seans)
- Kutu 1 — Metin çıktısının yükü · Sektör: *Unstructured vs Structured Output*
- Kutu 2 — Typed karar üçlüsü · Sektör: *System One Models* · *Decision Primitives (Choice/Score/Noul)*
- Kutu 3 — Kalibrasyon ölçüleri · Sektör: *Calibration (Brier, ECE, Reliability Diagram)* — **Karar 73 formülü:** Brier = (1/N)Σ(pᵢ−yᵢ)²; elle 10 örnek tablo; ECE bin=5.
- Kutu 4 — Confidence ve entropi · Sektör: *Decision Confidence / Margin* · *Shannon Entropy*
- Kutu 5 — RLCD · Sektör: *Reinforcement Learning for Calibrated Decisions* (satıcı terimi; spec yayımlanmadı, `[K]`)
- Kutu 6 — Satıcı iddiası ↔ ölçüm · Sektör: *Vendor Benchmark Skepticism* — 193,6× / 444,6× / %67,8 rakamları kaynak + "kendi iç iş-yükü" şerhiyle.
- Kutu 7 — Ad ve ekonomi · Sektör: *Jevons Paradox*
- Kutu 8 — Sınırlar · Sektör: *Model Limitations / Prompt-injection surface* (Gard bağı: state adversarial sayılmaz)

**"⌥ Jarvis notu" adayları:** Kutu 2 → hakem D/K/X etiketi bir `choice`; Kutu 3 → `v_skill_kosum` tahmin-gerçek ambarı kalibrasyon verisi; Kutu 8 → Gard G1 injection seti.

## Pratik (Salih'in eli)
`DONE` satırı README J1: konsol erişimi (waitlist) + ilk `Noul` çağrısı, cevap JSON'u derse yapıştırılır. Erişim yoksa: kavramsal `DONE`, pratik `KALAN`; alternatif pratik = 10 örnekle elle Brier/ECE hesabı (kâğıt + Python).

## CLOSE
Ders kaydı `ogrenme/jev/dersler/2026-MM-DD-J1-jev-nedir.md` (şema §5) · `ilerleme.md` satırı · `## Kalan` · Jarvis'e dönüş `cc/giden/J1-geri-donus.md` (sapma + iskelet isteği J2).
