# Rapor — AB-4 Antitez: V59 Okuyucu-Önkatmanı Refütasyonu

**Rol:** S-4b (v59-okuyucu-onkatman-antitez) · **Model:** sonnet · **Tarih:** 2026-08-21
**Bağımsızlık notu:** Bu koşum ab4-tez raporunu okumadan yürütüldü (m.40b gereği).

## Refütasyon İddiası (verilen, gerekçesiz)
"Ön-okuyucu katmanının kalite kaybı token kazancını YER: ucuz-model özeti kritik ayrıntıyı düşürür, pahalı model eksik bağlamla daha çok tur atar; uçtan-uca maliyet ve hata birlikte artar."

## Bulgular

### D — Doğrulanmış (kaynağı açıldı/okundu)

**D1. Özetleme kararları çarpıtır — sayısal.**
"When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis" (Hoyoung Lee ve ort., arXiv:2606.29251v2, 2026-07-08). https://arxiv.org/html/2606.29251
20-madde bütçesi altında test edilen 4 sıkıştırma yönteminin TÜMÜ, karar-çevirme (decision-flip) oranını yeniden-okuma gürültü tabanına (~%11) göre 2 kattan fazla artırdı. Mekanizma: **decontextualization** — MD&A'da bağlamsal pay (uyarı/nitelik/karşılaştırma) %25'ten %9'a düşüyor; başlık-bulgu korunuyor ama yorumu değiştiren çerçeve siliniyor. Ayrıca modeller-arası anlaşma yalnız ~%75 (model-bağımlı bilgi kaybı). İddianın (a) kısmını (ucuz özet kritik ayrıntı düşürür) doğrudan ve sayısal destekler.

**D2. Kademeli sistemde ara-aşama pahalı modelden daha verimsiz olabilir — yapısal kanıt.**
"Is Escalation Worth It? A Decision-Theoretic Characterization of LLM Cascades" (Dylan Bouchard, arXiv:2605.06350v1, 2026-05-07). https://arxiv.org/html/2605.06350v1
Sabit çok-aşamalı kaskadlar ("full fixed chains") ikili (doğrudan) zarfın (pairwise envelope) altında kalıyor; optimize edilmiş alt-dizi kaskadları anlamlı held-out kazanç sağlamıyor. Üretim-öncesi (pre-generation) router, 5 veri kümesinden 4'ünde en iyi kaskad politikasını geçiyor — çünkü ucuz modelin ÜRETİM maliyetinden kaçınıyor. Sayısal: SimpleQA'da optimal ikili %15,1 maliyet azaltımı, tam-zincir yalnız %1,3, diagnostic router %26,7. Yani zorunlu bir ara-okuma/özetleme aşaması eklemek, doğrudan yönlendirmeye göre DAHA AZ verimli olabiliyor — iddianın (c) kısmına (uçtan-uca maliyet artışı) yapısal destek.

**D3. Zayıf modelin yanlış kabul/red kararı pahalı modele fazladan tur bindiriyor.**
"UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing" (arXiv:2605.18796). https://arxiv.org/pdf/2605.18796
Kalibre edilmemiş belirsizlikle çalışan zayıf model, kabul/red kararında hata yaptığında bu hata pahalı modele gereksiz bir ek geçiş (turn) yüklüyor ve toplam kaskad maliyetini "dramatik biçimde" yükseltebiliyor. İddianın (b) kısmını (pahalı model daha çok tur atar) doğrudan destekler.

**D4. Çok-ajanlı/kademeli sistemde tek hata yaygın başarısızlığa dönüşebilir.**
"From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration" (Yizhe Xie ve 7 ort., arXiv:2603.04474, gönderim 2026-03-04, rev. 2026-05-11). https://arxiv.org/abs/2603.04474
Tek bir hata enjeksiyonu "yaygın başarısızlığa" yol açabiliyor; üç kırılganlık sınıfı tanımlanmış (cascade amplification, topological sensitivity, consensus inertia). Önerilen müdahale çalışma modları genelinde koşumların ≥%89'unda nihai "enfeksiyonu" engelliyor — tersinden okunursa, müdahalesiz durumda kayda değer bir başarısızlık riski var. İddianın (c) kısmına (hata büyümesi) destek; ancak bu makale çok-ajan işbirliği bağlamında, doğrudan "okuyucu→özet→pahalı-model" zinciri değil — kısmi transfer.

**D5. Otoregresif birikimli hata — kaba oran (hakemsiz kaynak, dikkatle kullanılmalı).**
"Compounding Error Effect in Large Language Models: A Growing Challenge" (wand.ai blog). https://wand.ai/blog/compounding-error-effect-in-large-language-models-a-growing-challenge
İddia: %1'lik adım-başı hata oranı, 200. token'e kadar kümülatif olarak ~%87 hata olasılığına dönüşebilir; karmaşık çok-aşamalı görevlerde doğruluk katlanarak düşüyor. **Uyarı:** hakemli yayın değil, blog; yazar/hesaplama metodolojisi doğrulanmadı — K'ya yakın D, düşük yetke ile okunmalı.

**D6. Erken-aşama halüsinasyon çok-ajan sistemde yayılıyor (nitel doğrulama, sayısal çıkarım kısıtlı).**
"Hallucination Cascade: Analyzing Error Propagation in Multi-Agent LLM Systems" (Jamshidi, Moradi Dakhel, Nafi, Khomh; arXiv:2606.07937, 2026-06-09). https://arxiv.org/pdf/2606.07937
Erken aşama halüsinasyonların sonraki ajan aşamalarını zincirleme etkilediğini ve performansı önemli ölçüde düşürdüğünü doğruluyor. PDF metin çıkarımında somut sayısal oran görünmedi (erişim kısıtı — tam PDF ayrıştırılamadı, yalnız özet düzeyi doğrulandı).

### K — Kaynaklı ama tek-kaynak/derinlemesine açılmadı

**K1.** "Lost in the Middle: How Language Models Use Long Contexts" (Liu ve ort., TACL 2024 / arXiv:2307.03172). https://arxiv.org/abs/2307.03172 — WebSearch özetiyle sınırlı (PDF açılmadı). U-şekilli performans eğrisi: uzun bağlamın ortasındaki bilgi zayıf kullanılıyor. Bir okuyucu-katmanının ürettiği özet, sonraki pahalı-model bağlamında "ortada" konumlanırsa aynı zayıflığa maruz kalabilir — dolaylı destek.

**K2.** NeuralTrust "LLM Model Routing" blogu (arama özeti, açılmadı) — kaskadlar ucuz-model çağrısının maliyetini HER sorguya (frontier'a gidecek olanlar dahil) bindiriyor; toplam maliyet C = C^w + C^d + P(red)·C^s formülü. İddianın (c) kısmına dolaylı sayısal-yapı desteği.

**K3.** "When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack" (arXiv:2605.17288) — bu URL'yi BEN açmadım (S-5'in ayrı görevi bu kaynağın tekil doğrulamasını yapıyor; mükerrer iş yapılmadı). Arama özeti: düşmanca pertürbasyonlar hem görev performansını hem kaskadın maliyet-verimlilik avantajını AYNI ANDA bozabiliyor — iddiayı destekler nitelikte ama benim tarafımdan D olarak damgalanamaz, K kalır.

**K4.** Klinik özetleme halüsinasyon/atlama oranları (%1,47 / %3,45, npj Digital Medicine çerçevesi) — yalnız arama özeti, açılmadı. Özetleme kayıplarının küçük ama sıfır-olmayan olduğuna dair ek K-düzey veri noktası.

### X — Belirsiz/çelişkili (dürüstlük gereği, iddiaya kısmen ters)
**X1.** Aynı kaskad-routing taramasında karşılaşılan bir bulgu: "sınıflandırma, evet/hayır soruları, yapılandırılmış çıkarım ve ÖZETLEME görevleri küçük modellerde neredeyse her zaman sorunsuz" (NeuralTrust/genel routing literatürü, arama özeti). Bu, iddianın (a) kısmıyla kısmen ÇELİŞİYOR: basit/yapılandırılmış özetleme için kalite kaybı ihmal edilebilir olabilir; kayıp riski büyük olasılıkla AÇIK-UÇLU/karmaşık özetlemeyle sınırlı (bkz. D1'in finansal-analiz bağlamı, ki bu açık-uçlu bir görevdir). Dürüstlük gereği kaydedildi; refütasyon lehine argüman inşa ETMEDİM, yalnız çıkan gerilimi bildiriyorum.

## Jarvis'e Uygulanabilirlik
V59 deseni ("ucuz-okuyucu → damıtık özet → pahalı model") tam olarak D1-D3'ün test ettiği yapı: bir kademe daha eklemek, doğrudan yönlendirmeye göre her zaman net kazanç DEĞİLDİR (D2); ara-katmanın kararı (ne düşer, ne kalır) hatalıysa pahalı model eksik bağlamla ek tur harcar (D3), ve özetin "decontextualization" riski (D1) — m.20 pointer ilkesinin ("özet+adres") tam bu riske karşı bir kısmi zırh olduğunu gösteriyor: adres (kaynağa geri erişim yolu) varsa pahalı model eksik gördüğünde kaynağa dönebilir, X1'in işaret ettiği gibi risk büyük olasılıkla açık-uçlu/karmaşık okuma görevlerinde yoğunlaşır (basit pointer-özetleme değil). Sonuç: refütasyon iddiası GENEL OLARAK dış kanıtla destekleniyor, ancak koşulsuz değil — kapsamı "açık-uçlu, çok-adımlı okuma" ile sınırlı görünüyor; sentez/karar S-4a ile birlikte Carvis'in hakemliğinde (bu raporun kapsamı dışı).

## F2 — Destek Tablosu

| İddia parçası | Kaynak(lar) | D/K/X |
|---|---|---|
| (a) ucuz-model özeti kritik ayrıntıyı düşürür | D1 (arXiv:2606.29251), D5 (wand.ai), K1 (arXiv:2307.03172), K4 (npj) | D (ana), X1 ile sınırlandırılmış |
| (b) pahalı model eksik bağlamla daha çok tur atar | D3 (arXiv:2605.18796), D2 (arXiv:2605.06350) | D |
| (c) uçtan-uca maliyet ve hata birlikte artar | D2 (arXiv:2605.06350), D4 (arXiv:2603.04474), D6 (arXiv:2606.07937), K2 (NeuralTrust), K3 (arXiv:2605.17288) | D (ana) |
| Karşı-sinyal (basit özetleme küçük modelde sorunsuz) | X1 (arama özeti, kaynak tekil değil) | X |

## Cevaplanamayanlar
- V59'a ÖZGÜ ("okuyucu-modeli → damıtık özet → pahalı-model") bir uçtan-uca maliyet-tersine-dönme (net negatif ROI) vaka çalışması bulunamadı; kanıtlar genel kaskad/routing ve genel özetleme literatüründen TRANSFER ediliyor, birebir mimari testi değil.
- Bilgi kaybının hangi eşikte token-kazancını tam olarak yediğine dair sayısal bir kırılma noktası (breakeven) hiçbir kaynakta verilmedi.
- D6 (Hallucination Cascade) makalesinin somut sayısal sonuçlarına PDF erişim kısıtı nedeniyle ulaşılamadı — yalnız özet düzeyinde doğrulandı, FAIL-LOUD bayrağı: tam metin okunamadı.
- K1 ve K2 kaynakları tam metin açılmadan (yalnız arama özetiyle) kullanıldı — istenirse ek bir dalga bunları D'ye yükseltebilir.
