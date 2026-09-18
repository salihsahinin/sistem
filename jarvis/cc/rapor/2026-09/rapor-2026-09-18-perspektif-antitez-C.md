# Atlas ANTİTEZ Raporu — Aile C (akademik/benchmark literatürü, 2025-2026)

**AS-OF (çekim):** 2026-09-18. **Yöntem:** yalnız web (WebSearch+WebFetch); her satırda kaynak URL + yayın tarihi + model/kuşak. Süs-antitez yok; çürütemediğim yerde "ÇÜRÜTÜLEMEDİ" yazdım.

**Açılan (gövde/bulgu okunan) kaynaklar:** 6 — [2605.00914](https://arxiv.org/abs/2605.00914) (Cost of Consensus), [2604.02460](https://arxiv.org/html/2604.02460v1) (FRAMES tek/çok-ajan), [2502.08788](https://arxiv.org/abs/2502.08788) (Stop Overvaluing MAD), [2604.08931](https://arxiv.org/html/2604.08931) (PETITE tutor-student), [2508.03686](https://arxiv.org/pdf/2508.03686) (CompassVerifier), [2603.04722](https://arxiv.org/pdf/2603.04722) (Model Medicine / Ephemeral Cognition — PDF sıkıştırılmış, sınırlı erişim).

**Not (AS-OF anomalisi):** Aranan birincil kaynakların bir kısmının arXiv id'si 2026 yılına ait (2605.xxxxx = Nisan/Mayıs 2026, 2604.xxxxx). Bu id'ler bugünün (2026-09-18) *gelecek*inde değil geçmişinde kalıyor — arXiv YYMM biçiminde 2605 = 2026-05, 2604 = 2026-04; bugünden (2026-09) geriye dönük, tutarlı. Anakronizm yok, sadece kesim-tarihi-sonrası (Ocak 2026 kesim) yeni literatür.

---

## İddia 1 — 7-8B homojen modellerde izole self-correction debate'i geçer

**Hüküm: ÇÜRÜTÜLEMEDİ (¬T aranmadı bulunamadı, T'nin kendisi birincil kaynakla doğrulandı).**
[Cost of Consensus (2605.00914)](https://arxiv.org/abs/2605.00914), gönderim 2026-04-29, ACM AI and Agentic Systems'a sunulu: N=10 homojen ajan (Qwen2.5-7B, Llama-3.1-8B, Ministral-3-8B), R=3 tur, GSM-Hard/MMLU-Hard. Ministral-3-8B GSM-Hard'da debate %20,7 < self-correction %48,3 < tek-ajan zero-shot %24,7. Llama-3.1-8B'de debate %39,3, self-correction %41,0 (istatistiksel fark yok). ¬T yönünde (debate'in bu sınıfta üstün olduğu) birincil kanıt aranmış, **bulunamamıştır** — tersine tüm bulgular T'yi güçlendiriyor. Model/kuşak: 7-8B, 2024-2025 açık ağırlıklı.

## İddia 2 — Homojen debate'te sycophantic uyum %85,5, doğru muhakemeyi terk %70

**Hüküm: ÇÜRÜTÜLEMEDİ.**
Aynı kaynak (2605.00914) + [Peacemaker or Troublemaker (2509.23055)](https://arxiv.org/pdf/2509.23055, 2025-09) ve [Talk Isn't Always Cheap (2509.05396)](https://arxiv.org/pdf/2509.05396, 2025-09) bağımsız olarak sycophantic conformity'yi ana başarısızlık modu olarak doğruluyor; "correctness payoff" müdahalesinin doğru→yanlış geçişleri azaltmadığı bile gösterilmiş (yani karşı-önlem bile işe yaramıyor — T'yi zayıflatan değil güçlendiren bir bulgu). Rakamların hangi spesifik modele ait olduğu özette açık değil (gövde PDF gerekir), ama üç bağımsız makale yönü doğruluyor.

## İddia 3 — Debate izole self-correction'a göre 2,1-3,4× token tüketir

**Hüküm: DARALDI.**
Rakamın kendisi (2605.00914) "unguided homogeneous" mimariye özgü, ve makale açıkça "up to 28.631 token/problem" diyor — bu **belirli bir mimari sınıfı** için geçerli. Karşı-kanıt: [S²-MAD (2502.04790)](https://arxiv.org/abs/2502.04790, 2025-02), redundancy filtering + selective participation ile token maliyetini **%94,5'e kadar** azaltıyor — yani "debate = 2,1-3,4× pahalı" evrensel bir mimari özelliği değil, optimize edilmemiş/yapılandırılmamış debate'in özelliği. İddia genel bir "debate" hükmü gibi sunulursa yanıltıcı; "yapılandırılmamış homojen debate" olarak daraltılmalı.

## İddia 4 — Güncel-kuşak modellerde (Gemini 2.5 Pro/Flash, Qwen3-30B, DeepSeek-R1-70B) eşit token bütçesinde tek-ajan ≥ sıralı çok-ajan

**Hüküm: ÇÜRÜDÜ (model-bağımlı, iddianın "eşit token bütçesinde tek-ajan HER ZAMAN ≥" biçimi yanlış).**
Kaynağın kendisi — [FRAMES tek/çok-ajan (2604.02460)](https://arxiv.org/html/2604.02460v1) — Gemini-2.5-Pro için **tam tersini** gösteriyor: 5000 token bütçesinde Sequential çok-ajan %66,0 doğruluk, tek-ajan %60,0 (yani çok-ajan +6 puan üstün). Qwen3-30B'de tersi (tek-ajan %24,0 > Sequential %22,3). Yani iddia "her modelde" değil, **model ailesine göre değişken ve en az bir güncel-kuşak modelde (Gemini-2.5-Pro) çok-ajan tek-ajanı geçiyor** — bu doğrudan T'nin evrenselliğini çürütür. Model/kuşak: Gemini-2.5-Pro, Qwen3-30B, DeepSeek (2026-04 makale).

## İddia 5 — FRAMES'te tek/çok-ajan farkı %1,5-%14,6 arası (model ailesine göre)

**Hüküm: ÇÜRÜTÜLEMEDİ (aralık kabaca tutarlı, ama işaret yönü iddia edilenin tersini de içeriyor).**
Aynı kaynaktan çıkan sayılarla (Qwen3-30B farkı 1,7pp; Gemini farkı 6,0pp — ama **çok-ajan lehine**) aralık büyüklük olarak makul, ama iddia "fark" derken yönünü belirtmiyor; gerçekte fark bazen çok-ajan lehine. Aralığın büyüklüğü çürütülemedi, yönü konusunda iddia 4'teki gibi tek-taraflılık yanıltıcı.

## İddia 6 — Model heterojenliği debate başarısızlığına evrensel panzehirdir

**Hüküm: DARALDI.**
[Stop Overvaluing Multi-Agent Debate (2502.08788)](https://arxiv.org/abs/2502.08788, 2025-02) özetinde heterojenliği tam olarak "universal antidote" (evrensel panzehir) diye **öneriyor** — yani bu iddia savunucu makalenin kendi diliyle örtüşüyor, T zaten bu kaynağa dayanıyor gibi görünüyor. Ancak [Heterogeneous LLM Debate Under Adversarial Peers (2606.19826)](https://arxiv.org/pdf/2606.19826, 2026-06) başlığı bile "adversarial peers karşısında replacement costs / resilience sınırları" diyor — yani heterojenlik kayıtsız şartsız iyileştirici değil, düşman/gürültülü ajan karşısında maliyetli. Ayrıca [Demystifying MAD (2601.19921)](https://arxiv.org/html/2601.19921v2, 2026-01) rol atamasına göre std sapma ±3,5 puan rapor ediyor — heterojenlik rastgele uygulanırsa **performansı düşürebiliyor**. "Evrensel" iddiası daralıyor: heterojenlik koşullu fayda, panzehir değil reçete.

## İddia 7 — Orkestrasyon en fazla +4,6 puan karşılığında 2-4× token maliyeti

**Hüküm: DARALDI.**
[DAAO (2509.11079)](https://arxiv.org/pdf/2509.11079, 2025-09) daha iyi puan/maliyet oranı rapor ediyor: mevcut otomatik orkestrasyon yöntemlerine göre %3,5-15,2 doğruluk artışı, LLM routing yöntemlerine göre %3,2-10,2 — yani "en fazla +4,6 puan" hükmü orkestrasyon sınıfının tamamı için değil, spesifik (muhtemelen naif) bir kurulum için geçerli; zorluk-farkında orkestrasyon daha yüksek kazanç/maliyet oranı sunabiliyor.

## İddia 8 — Maliyet-farkındalıklı orkestrasyon doğruluğu %0,90-11,92 artırır

**Hüküm: ÇÜRÜTÜLEMEDİ.**
[Cost-Aware Model Orchestration (2512.01099)](https://arxiv.org/pdf/2512.01099, 2025-12) tam bu aralığı rapor ediyor ("absolute gains from 0.90% to 11.92%") — iddia muhtemelen doğrudan bu kaynaktan alınmış; ¬T aranmış, karşı bulgu yok.

## İddia 9 — "TDP" yönteminin %82 token tasarrufu iddiası doğrulanamaz

**Hüküm: ÇÜRÜTÜLEMEDİ (kaynağın kendisi bulunamadı).**
"TDP" adıyla arXiv'de %82 token tasarrufu iddia eden bir makale bulunamadı (arama: "token diagnostic pruning", "token decision protocol" — negatif sonuç). Karşılaştırma için bulunan en yakın yöntem [DeepPrune (2510.08483)](https://arxiv.org/pdf/2510.08483, 2025-10), %52,5-91,6 (AIME'de %79,6-91,6) token tasarrufu bildiriyor — farklı isim, örtüşen büyüklük mertebesi ama "TDP" adıyla eşleşmiyor. İddianın kendisi zaten "doğrulanamaz" diyor; bunu **ne doğrulayabildim ne çürütebildim** — kaynak izi yok.

## İddia 10 — "Ephemeral Cognition" ampirik değil kavramsal bir çerçeve

**Hüküm: ÇÜRÜTÜLEMEDİ (kısmi erişim).**
[Model Medicine (2603.04722)](https://arxiv.org/pdf/2603.04722, 2026-03) terimi "yapısal olarak kendi deneyimini biriktiremeyen varlıkta bilişsel işleme" olarak tanımlıyor, Agent Differentiation (ana ajan kalıcı dosya/kabuk erişimi vs alt-ajan görev-bağlamlı, kalıcılık yok) örneğiyle açıklıyor — bu **kavramsal/taksonomik** bir çerçeveleme, ölçülmüş deney/benchmark rastlanmadı (PDF sıkıştırılmış geldiği için gövde tam okunamadı, tablo/deney bölümü doğrulanamadı). Bulgu T yönünde ama düşük güvenle (erişim sınırlı).

## İddia 11 — Üretici/değerlendirici ayrımının hata oranına etkisine dair güncel-kuşak sayısal kanıt yoktur

**Hüküm: ÇÜRÜDÜ.**
[PETITE (2604.08931)](https://arxiv.org/html/2604.08931, 2026-04), Qwen2.5-Coder-7B-Instruct (4-bit NF4) ile APPS benchmark'ında somut rakamlar veriyor: PETITE (generator/evaluator ayrımı, 2 iterasyon) %31,62 başarı / 5.277 ort. token; Multi-Agent Debate %28,97 / 23.630 token; Self-Refine %27,59 / 15.285 token. Verimlilik oranı (başarı/token) PETITE=5,99 vs MAD=1,23. Ayrıca [CompassVerifier (2508.03686)](https://arxiv.org/pdf/2508.03686, 2025-08-06) GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, O1-Preview, Qwen2, DeepSeek dahil güncel-kuşak modellerde verifier performansını ölçüyor (VerifyBench'te üst-sıra skorer farkı %0,55-2,0). Yani sayısal kanıt **var**; iddia çürüyor.

## İddia 12 — Tutor mimarilerinde rol-ayrımı yaygın ama birincil kaynakla doğrulanmamış

**Hüküm: ÇÜRÜDÜ (kısmen — "doğrulanmamış" kısmı yanlış, "yaygın" kısmı doğru).**
PETITE (2604.08931, yukarıda) tam olarak tutor-student rol ayrımını birincil deneyle doğruluyor (APPS benchmark, somut rakamlar). Ayrıca [Voting Protocols for Role-Constrained Multi-Agent Tutoring (2606.08030)](https://arxiv.org/pdf/2606.08030, 2026-06) ve Wang et al. 2025a (curriculum/dialogue/assessment ajan ayrımı) ek birincil doğrulama sağlıyor. "Yaygın ama doğrulanmamış" hükmü artık geçerli değil — en azından 2025-2026 için birden fazla birincil kaynakla doğrulanmış durumda.

---

**Epistemik not:** İddia 1-3 ve 8 kaynağı doğrudan destekliyor gibi görünüyor (muhtemelen bu iddialar zaten o makalelerden damıtılmış); asıl çürüme/daralma İddia 4, 6, 7, 11, 12'de. İddia 9 için kaynak izi bulunamadı — bu, iddianın "doğrulanamaz" hükmünü DOLAYLI olarak destekliyor (negatif arama sonucu, kanıt değil).
