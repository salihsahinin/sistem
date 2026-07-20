# B3 — LLM Council / Debate Maliyet-Fayda (V53) — Atlas Raporu (2026-07-20)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ, karar ALINMADI) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: **5** (nedir/yöntemler · kalite-faydası · maliyet-ekonomisi · JARVIS-uyum/V53 · ünlü-isimler) → 10 literatür/pratisyen şeridi + 1 çoklu-model/konsey karar envanteri.
> **Kanıt kısıtı (dürüstlük):** Karpathy llm-council README doğrudan çekildi **[D]**; arXiv HTML/PDF'lerin çoğu + together.ai + cognition.ai egress-403 → o bulgular WebSearch-özeti **[K]**. Doğrulanamayanlar (PoLL "~7× ucuz", "Anthropic/OpenAI council savunuyor", ileri-tarihli arXiv ID'leri) §5'te işaretli.
> **Salih notu:** "Council/Debate ne olduğu bana tekrar açıklanmalı" — §0 kutusunda ve §1 Aile A'da SADE açıklama var.
> **Okuma sırası (Fable):** §0 Carvis sentezi (+ "nedir" kutusu) + §4 dürüst bayraklar → yeterli. Detay: §1 aile bulguları · §2 ünlü isimler · §3 karar-envanteri kontrolü · §5 V26 · §6 açık sorular.

---

## §0 — Carvis sentezi (önce oku)

**"LLM Council / Debate NEDİR" (Salih için sade tanım):** Tek mekanizmanın varyant ailesi — *"birden çok model/rol bağımsız cevap üretir → birbirini eleştirir/oylar/sıralar → bir 'başkan' tek cevaba sentezler."* Varyantlar: **Multi-Agent Debate** (Du'23 — N ajan tur-tur birbirini görüp yakınsar); **Self-Consistency** (Wang'22 — tek model çok-örneklem, çoğunluk-oyu; "iç konsey", en ucuz); **Mixture-of-Agents** (Together AI — proposer→aggregator katmanları); **LLM-as-Jury/PoLL** (çeşitli küçük modeller puanlar, DEĞERLENDİRME için); **Karpathy llm-council** (3 aşama: bağımsız görüşler → ANONİM çapraz-sıralama → Başkan sentezi). **V53 ≈ Karpathy council birebir.**

**En sağlam kesişim (beş ailenin İKİ şeridinin de + envanterin ortak dediği):**

1. **"Council/Debate" tek tutarlı yöntem DEĞİL — ve değeri, hangi varyant olursa olsun, ÇEŞİTLİLİKTEN gelir, "tartışma/başkan" mekaniğinden değil.** Kanıt convergent: A-antitez (martingale — debate oylamanın ötesinde beklenen kazanç vermez), B-tez (**KİLİT KOŞUL = heterojenlik**), D-tez (literatürün 4 ilkesinden yük-taşıyan = model/rol heterojenliği). [D/K]

2. **Kazanç GERÇEK ama görev-dar: doğrulanabilir-cevaplı akıl-yürütme/matematikte güçlü** (Du +8…+14.8, self-consistency +17.9, MoA +7.6, olgusal hata −%30) — **açık-uçlu/öznel işte zayıf-ila-negatif** (conformity/sycophancy doğruluğu DÜŞÜREBİLİR). JARVIS'in çekirdek işi (kanon/wiki/araştırma) çoğunlukla açık-uçlu kip → council'ın KANITLI kazancı burada devrede değil. [K]

3. **Maliyet süperlineer** (ham 17-49×, disiplinli 2.1-2.5×, aralık 4-220×); eşit-bütçe tek-derin-koşum çoğu kez council'ı yakalar/geçer (DPI); abonelik haftalık-tavanı (A2) N×R hızlı yenir; council **B1'in çift-atlas ×2 en akut maruziyetini KATLAR**. Kısılabilir (seçici-tetik −%27.5, ucuz-panel+tek-sentez, erken-durma ~7.9×, batch %50) ama yine de çarpan-vergi. [K]

4. **UZLAŞTIRMA: JARVIS council'ın değerini ZATEN akıllı yoldan alıyor — çeşitliliği YAPIDAN, çoklu-modelden değil.** m.42(f) açıkça: çeşitlilik karşıt-temel/persona/tez-antitezden alınır, **sampling gürültüsünden DEĞİL**. Çift-atlas = debate; m.37 karşıt-temel = gerçekten-zıt akıl-yürütme zeminli adversarial jüri (EV↔minimax, Bayes↔frekans). Bu, antitezin "homojen Fable-council = korelasyonlu hata" eleştirisini ETKİSİZLEŞTİRİR: yapısal çeşitlilik = inşa-yoluyla-çeşitlilik, model-ailesiyle değil — hem tek-aile içinde işler hem daha ucuz. [D-kanon]

5. **Dolayısıyla V53 AYRI bir council katmanı olarak gereksiz/çift-sayım** (çift-atlas zaten council — D-antitez), Fable-pin üstünde homojen (m.30/V56), ve maliyet-mekanizması tam devrede iken kazanç-mekanizması (model-çeşitliliği + nesnel-doğru-cevap) JARVIS'te yok. **Tek GENUINE yeni kaldıraç:** (a) **anonim çapraz-sıralama** (ucuz, m.7-hizalı, ödünç alınabilir); (b) kalite-kapılı model-ailesi çeşitliliği (Fable-pin bütçesiyle çelişir — V56 ERTELENDİ; ve yalnız nesnel-görevde yardım eder). [D/K]

**JARVIS'e ne demek (gözlem, KARAR DEĞİL — m.41):**

- **Dürüst manşet:** JARVIS council/debate'in SAVUNULABİLİR çekirdeğini (yapısal çeşitlilik + ayrı düşük-temp yargıç + Carvis/m.17 başkan-sentezi) zaten koşuyor ve bir model-council'ından DAHA UCUZA alıyor. V53'ü genel yeni katman yapmak, çoğunlukla devrede-olmayan bir kazanç için maliyeti (B1 ×2) çift-sayar.
- **Literatürün "işe yaratan-şey" kontrol listesi = zaten kanon:** yapısal rol-çeşitliliği (m.37 karşıt-temel), proposer-bağımsızlığı (m.40b ¬T), düşük-temp ayrı-yargıç (m.42), kalite-kapılı heterojenlik (yeni). Tek ucuz-ödünç primitive = **anonim çapraz-sıralama**, ve o da nadir Katman-1 (kanon/para/publish) sigortasına yakışır — C-tez'in maliyet-kısma kaldıraçları (seçici-tetik, tek-pahalı-sentez, erken-durma, batch %50) V53'ün KENDİ kural-adaylarına (eşik/token-tavanı/ucuz-A-B) birebir eşleşir.
- **En keskin dürüst gerilim:** council kazancı ya model-çeşitliliği (Fable-pin/V56 ile kapalı) ya nesnel-doğru-cevap (JARVIS işi çoğunlukla öznel) gerektirir — JARVIS'te ikisi de yok; AMA yapısal çeşitlilik (karşıt-temel) bunu tek-aile içinde çeşitlilik-imal ederek atlatır. Tasarım-içgörüsü: **model-council ekleme; sahip olduğun yapısal-çeşitlilik doğru, bütçe-uyumlu ikamedir.**
- **En yüksek-kaldıraçlı üç gözlem:** (1) V53'ü genel council katmanı olarak EKLEME (çift-sayım + homojen); (2) tek ucuz-ödünç = anonim çapraz-sıralama, nadir Katman-1 sigortasına; (3) doğru optimizasyon yönü DAHA AZ katman + erken-sonlandırma (D-antitez, C-tez), council eklemek değil.

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile A — "Council/Debate nedir" (meta)
- **Tez:** (Tam tanım §0 kutusu.) Beş varyant tek iskeleti paylaşır: çeşitlilik → etkileşim → toplama. "Başkan" iki tip: oylayıcı-toplayıcı (mekanik) vs sentezleyici-başkan (okur/tartar/birleştirir); anonimleştirme = marka-yanlılığı freni. V53 ≈ Karpathy 3-aşama. [D/K]
- **Antitez (¬):** Tutarlı tek yöntem değil, gevşek etiket (varyantlar ampirik farklı); kazancın çoğu oylama/çeşitlilikten, "tartışma"dan değil (Debate-or-Vote martingale); JARVIS'in çift-atlas+m.37'si özü zaten taşır → V53 yeniden-adlandırma riski; başkan tek-nokta-önyargı. [K]
- **Kesişim:** NET tanım verildi; "council" tek-mekanizma değil, çeşitlilik-toplama şemsiyesi — ve değer-yaratan bileşen (çeşitlilik) JARVIS'te zaten yapısal olarak var.

### Aile B — Kalite/doğruluk faydası
- **Tez:** Sayısal kazançlar gerçek: Du GSM8K 85 vs 77 (+8), aritmetik +14.8, olgusal −%30; self-consistency +17.9; MoA AlpacaEval 65.1 vs GPT-4o 57.5 (+7.6); PoLL jüri daha insan-uyumlu+ucuz. **KİLİT KOŞUL: çeşitlilik** (heterojen model); homojen = korelasyonlu hata. [K]
- **Antitez (¬):** Kazanç görev-dar (doğrulanabilir-cevap, JARVIS'in açık-uçlu kanonu DEĞİL); conformity/sycophancy debate'i yanlışa götürebilir (zayıf model stance-yanlılığının ~%3.6'sını düzeltir); self-consistency serbest-biçim çıktıda çöker; eşit-bütçe tek-güçlü geçemez; Self-MoA > Mixed-MoA (+3.8 — model-karıştırma çoğu zaman zarar); başkan = bias-amplification. [K]
- **Kesişim:** Kazanç ANLAMLI ama yalnız (heterojen ∧ nesnel-doğru-cevap) rejiminde — bu JARVIS'in çalışma-kipi DEĞİL. "Koşulsuz üstünlük" savunulamaz; "yapısal-çeşitlilik + doğru görev" savunulur.

### Aile C — Maliyet/token ekonomisi
- **Tez:** Ham maliyet gerçek (SC 40-64×, kuadratik) AMA kısılabilir: ucuz-panel+tek-sentez (MoA-Lite GPT-4o'yu ucuza geçti), erken-durma (Adaptive-Consistency ~7.9× ↓, <%0.1 kayıp), seçici-tetik (−%27.5/+%6.2), batch %50; panel 3-5; yüksek-bahis/geri-alınamaz = sigorta (m.31-L1). **V53 kural-adayları birebir eşleşiyor.** [K]
- **Antitez (¬):** Süperlineer (S²-MAD 36-49×; Cost-of-Consensus 2.1×; aralık 4-220×); izole öz-düzeltme yönlendirilmemiş homojen debate'i geçer (**JARVIS atlas'ları aynı-aile → tam bu tuzak**); eşit-bütçe tek-derin yakalar; Pareto yalnız +1.3/+2.7; abonelik-tavanı N×R hızlı yenir; çift-atlas zaten council → çift-sayım; 2-çeşitli ≈ 16-homojen. [K]
- **Kesişim:** Council maliyeti yalnız nadir Katman-1 (kanon/para/publish) + maliyet-kısılmış + gerçekten-çeşitli kurulumda haklı; ensemble paylaşılan-sistematik-yanlılığı gidermez → Salih (insan) son-merci kalır (m.31-L1).

### Aile D — JARVIS-uyum (V53)
- **Tez:** Council literatürünün 4 yerleşik ilkesi JARVIS'te ZATEN yaşıyor — yapısal rol-çeşitliliği=m.37, proposer-bağımsızlığı=m.40b¬T, düşük-temp ayrı-yargıç=m.42, (kalite-kapılı heterojenlik=yeni). Convergent design: JARVIS bağımsızca aynı ilkelere vardı. V53'ün tek genuine yeni kaldıracı: (a) anonim çapraz-sıralama, (b) kalite-kapılı model-ailesi çeşitliliği (kalite-kapısı şart: Rethinking MoA zayıf-model girdisi ortalamayı düşürür). [K]
- **Antitez (¬):** V53 = çift-sayım; Fable-tek-aile → homojen → kazanç YOK (martingal); gerçek çok-model abonelik-DIŞI (m.30 pin); ekstra başkan m.7 öz-kayırmayı ARTIRIR (Fable-council Fable'ı puanlar); karar-doğrulama zaten kanonda (m.16/m.4/V26/m.7); Cognition tek-şerit; doğru yön DAHA AZ katman + erken-sonlandırma. Steelman: kazanç için (model-çeşitliliği ∧ nesnel-cevap) gerek — JARVIS'te ikisi de yok. [D/K]
- **Kesişim:** İki şerit teşhiste HEMFİKİR (değer=çeşitlilik, yapı zaten kanon); ayrışma sonuçta — D-tez "iki genuine kaldıraç ekle", D-antitez "kazanç-mekanizması inactive/maliyet aktif → ekleme, buda". Uzlaşı: genel council katmanı EKLEME; tek ucuz-ödünç = anonim çapraz-sıralama (nadir Katman-1); model-çeşitliliği Fable-pin bütçesiyle çelişir (Salih kararı).

### Aile E — Ünlü isimler / pratisyen
- **Tez:** Karpathy llm-council [D README], Du debate, Verga PoLL (Cohere), Together MoA, Wang self-consistency (Google) — hepsi "çeşitli görüş topla + hakemlet + sentezle" kalitesini ölçülebilir artırıyor. Ama "Anthropic/OpenAI savunuyor" DOĞRULANAMADI [?]; desenler ucuz-panel ↔ pahalı-çok-katman diye ayrışıyor. [D/K]
- **Antitez (¬):** Karpathy KENDİ "eğlence hack'i, desteklenmez, üretim değil"; Cognition "don't build" + "what's-actually-working" (yalnız dar desen: yazma tek-şeritli); MAD ≈ CoT+self-consistency null; "LLMs Cannot Self-Correct Yet"; jüri korelasyonlu-hata (aynı-aile judge'lar aynı yanlılığı paylaşır, çoğunluk büyütebilir); konsensüs "önce tek iyi-prompt'lu model, orkestrasyon yalnız ölçülmüş sınır olunca". [K]
- **Kesişim:** E-tez ve E-antitez YAKINSIYOR — otorite figürü (Karpathy) bile projesini "hack" diyor; pratisyen çizgisi "council son-çare"; kazanç-veren-şey çeşitlilik, protokol değil. JARVIS için: council'ı adı için benimseme; sahip olduğun yapısal-çeşitliliği koru, katman/tur SAYISINI m.21+V26 ile frenle.

---

## §2 — Ünlü isimler / kaynak tablosu

| İsim | Yöntem | Özü | JARVIS bağı | Kaynak | Etiket |
|---|---|---|---|---|---|
| Andrej Karpathy | llm-council | 3-aşama: görüş→anonim sıralama→başkan; "cumartesi hack'i, üretim değil" | V53 ≈ birebir; anonim-sıralama = m.7 teknik karşılığı | [github.com/karpathy/llm-council](https://github.com/karpathy/llm-council) | [D] |
| Du et al. (2023) | Multi-Agent Debate | N ajan tur-tur yakınsar; matematik +8-14.8, olgusal −%30 | çift-atlas debate'in akademik çekirdeği | [arXiv 2305.14325](https://arxiv.org/abs/2305.14325) [X] · [kod](https://github.com/composable-models/llm_multiagent_debate) | [K] |
| Wang et al. (2022, Google) | Self-Consistency | Tek model çok-CoT çoğunluk-oyu; GSM8K +17.9 | m.42(f) bunu DIŞLAR (düşük-temp zorunlu) | [arXiv 2203.11171](https://arxiv.org/abs/2203.11171) | [K] |
| Together AI / Wang (2024) | Mixture-of-Agents | proposer→aggregator katmanları; AlpacaEval 65.1 vs GPT-4o 57.5 | m.37 taslağı Model C emsali; m.21 ile gerilimli | [arXiv 2406.04692](https://arxiv.org/abs/2406.04692) [X] | [K] |
| Verga et al. (Cohere, 2024) | PoLL jüri | Çeşitli küçük panel > tek dev-judge; tek-model yanlılığı ↓ | V26 örneklem-denetimi akrabası; **DeepMind değil Cohere** | [arXiv 2404.18796](https://arxiv.org/abs/2404.18796) | [K] |
| Cognition (Walden Yan) | Don't Build Multi-Agents | Tek-şerit; çoklu-ajan kırılgan/çelişir | V53 tek-yazar (Carvis) ilkesini bozar | [cognition.ai](https://cognition.com/blog/dont-build-multi-agents) [X] | [K] |
| Karşı-literatür | Stop Overvaluing MAD · Rethinking MoA · Nine-Judges-Two-Votes | MAD ≈ CoT+SC; Self-MoA>Mixed; korelasyonlu-hata | "koşulsuz üstünlük" savunulamaz | [2502.08788](https://arxiv.org/abs/2502.08788) · [2502.00674](https://arxiv.org/html/2502.00674v1) | [K] |

---

## §3 — Karar-envanterimizin kategori + kontrolü (council merceğiyle)

| Karar/kimlik | Council-deseni denkliği | Statü | Kontrol (bu araştırmanın verdiği) |
|---|---|---|---|
| **m.37 + karşıt-temel** | adversarial jury/debate (gerçekten-zıt zeminler) | imzalı kanon | ✅ Council'ın "yapısal çeşitlilik" ilkesinin birebiri; tek-aile içinde çeşitlilik-imal eder → homojenlik tuzağını atlar. |
| **m.40b çift-atlas** | debate (bağımsız tez∧¬T) | imzalı kanon | ✅ Proposer-bağımsızlığı; ZATEN bir council → V53 çift-sayım. ⚠️ ×2 maliyet en akut maruziyet (B1). |
| **m.42(f) çeşitlilik-bütçesi** | jury + yapısal-debate; düşük-temp yargıç | imzalı kanon | ✅ "Çeşitlilik YAPIDAN, sampling'den değil" = literatürün heterojenlik-bulgusu + düşük-temp-judge best-practice. Self-consistency'yi DIŞLIYOR (doğru). |
| **m.17 köprü / m.30 pin** | chairman-synthesis (Carvis; en-üst katman) | imzalı kanon | ✅ Başkan-sentez rolünün kanon yeri; ⚠️ Fable-pin → model-council homojen olur. |
| **V53 LLM Council** | debate+jury+chairman (üçü) | **ham fikir, KARAR ALINMADI** | ⚠️ Genel katman = çift-sayım + homojen; tek genuine kaldıraç = anonim çapraz-sıralama; "token maliyeti BİLİNMİYOR" notu bu kartın açık borcu. |
| **V8/V16/V26/V31 değerlendirici ajanlar** | jury-evaluator (gözlemci/tester/kalibrasyon) | ham fikir / kanon-tasarım | ✅ Ayrı-değerlendirici ilkesi (PoLL/m.7 hizalı); V26 örneklem-denetimi = ucuz jüri. |
| **V56 Kimi (farklı-aile)** | çoklu-MODEL çeşitliliği | **ERTELENDİ (Fable-only bütçe)** | ⚠️ Council kazancının gerektirdiği model-çeşitliliği tam burada kapalı → gerilim işaretli. |
| **karar-modeli SKILL (S-A) / Model C** | debate+jury motoru / MoA+chairman | üretildi (eval 3/3) / kanon-örnek | ✅ m.37 council'ını zaten koşuyor; "zıt zeminlerin KESİŞİMİ = en sağlam" = triangülasyon. |

**Özel vurgu — çoklu-MODEL vs çoklu-ÖRNEKLEM (kanon gerilimi):** m.42(f) çoklu-örneklemi (self-consistency, yüksek-temp N-sampling) değerlendirici/icra ajanlarında AÇIKÇA dışlıyor (düşük-temp zorunlu); çeşitliliği YAPIDAN alıyor. m.30 Fable-pin farklı-AİLE çoklu-modeli bütçeyle kapatıyor. V53(c) ve V56, "çoklu-rol (tek model) mü çoklu-model (farklı aile) mi" sorusunu bilinçle ÖLÇÜME bırakıyor — karara bağlanmamış.

---

## §4 — Yanlış/zayıf gördüklerim (dürüst bayraklar — KARAR ALMADAN, m.41)

1. **"LLM Council/Debate" gevşek etiket, tek mekanizma değil** — V53'ü "council benimseme" diye sunmak, spesifik mekanizma olmadan pazarlama-halesini ithal etme riski. Kanıtlı değer = ÇEŞİTLİLİK, ve JARVIS'te yapısal-çeşitlilik zaten var.
2. **Council'ın kanıtlı kazancı doğrulanabilir-cevaplı görevlerde** — tam da JARVIS'in açık-uçlu kanon/araştırmasının DIŞI; kazanç-sayılarını (Du +8, self-consistency +17.9) JARVIS-tahmini gibi ithal etmek lisanssız (m.39, A4'ün laboratuvar-sayıları tuzağının aynısı).
3. **Fable-pin (m.30/V56) her JARVIS "council"ını homojen yapar = korelasyonlu hata = council'ın battığı rejim** ("2-çeşitli ≈ 16-homojen"); AMA yapısal çeşitlilik (m.42f karşıt-temel) bunu atlar — bu ayrım BULANIKLAŞTIRILMAMALI: naif Fable-instance-council'ı hata modu, karşıt-temel değil.
4. **Ekstra başkan m.7 öz-kayırmayı ARTIRIR** (Fable-council Fable-çıktısını puanlar = maksimum öz-tanıma-yanlılığı). JARVIS'in mevcut ayrımı (m.7/m.16/m.28 denetçi-ayrı, karar-modeli SKILL "üret ama kaydı yazma") doğru koruma; V53 başkanı bunu çökertmemeli.
5. **Öz-referans (maliyet notu):** B3'ün KENDİSİ 11 çift-atlas ajanı koşup "V53 katman olarak gereksiz, çekirdek zaten kanon" sonucuna vardı — bu raporun bayrakladığı çift-atlas ×2 maliyet-maruziyetinin bir örneği daha (A2/B1/B2 gibi).
6. **Doğrulanamayanlar (m.39):** PoLL "~7× ucuz" [X]; PoLL atfı "Google/DeepMind" YANLIŞ (Cohere); "Anthropic/OpenAI council savunuyor" DOĞRULANAMADI [?]; birkaç arXiv ID ileri-tarihli göründü [?]; Karpathy llm-council = kendi "eğlence hack'i" [D]. Taşındı, laundering YOK.
7. **Karşı-literatür güçlü** (Stop Overvaluing MAD, Rethinking MoA, Self-MoA>Mixed, Nine-Judges-Two-Votes) — "council kaliteyi artırır" KOŞULSUZ söylenemez; yalnız "yapısal + heterojen + nesnel-görevde".

---

## §5 — V26 örneklem-denetimi

| Ajan/şerit | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| E-tez | "PoLL Google/DeepMind, ~7× ucuz" | **Yanlış atıf + doğrulanamadı** — Cohere; ~7× [X] | Düzeltildi (§2); sayı raporda öne çıkarılmadı |
| E-tez | "Anthropic/OpenAI council savunuyor" | **DOĞRULANAMADI** — resmi beyan yok | [?]; tez ayağı Karpathy+akademi+Together üzerinden ayakta |
| A-tez/E | "PoLL arXiv 2404.18796 / ileri-tarihli ID'ler" | **İkincil/[?]** — bazı ID'ler ileri-tarihli göründü | [?]; yük-taşıyan iddialar çok-kaynak yakınsamalı |
| C-antitez | "izole öz-düzeltme > homojen debate; 2≈16" | **Arama-özeti** — çok-kaynak | [K]; JARVIS homojenlik-tuzağı argümanının çekirdeği |
| m.42(f) | "self-consistency değerlendiricide dışlanmış" | **Kanon-DOĞRULANDI** — düşük-temp zorunlu | [D-kanon]; JARVIS self-consistency yolunu bilinçle reddetmiş |
| Karpathy | "llm-council = üretim önerisi mi" | **Hayır** — README "vibe-coded Saturday hack, unsupported" | [D]; E-tez/antitez yakınsamasının çıpası |
| Egress | arXiv HTML/PDF · together.ai · cognition.ai | **403** | İlgili bulgular [K]; Karpathy README doğrudan [D] |

---

## §6 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **V53 ayrı council katmanı olarak EKLENMELİ mi, yoksa mevcut yapısal-çeşitlilik (m.37+m.40b) yeterli mi?** — kanıt "çift-sayım + homojen"e işaret ediyor ama karar Salih'te (V53 kanon-adayı, Katman-1).
2. **Tek ucuz-ödünç primitive — anonim çapraz-sıralama — nadir Katman-1 (kanon/para/publish) kararlarına sigorta olarak eklensin mi?** — m.7-hizalı, ucuz; ama yine "kur değil, deseni yeniden-yaz" (V25).
3. **"Çoklu-rol (tek Fable) vs çoklu-model (farklı aile)" ölçüm borcu (V53c/V56) ne zaman/nasıl kapatılsın?** — model-çeşitliliği Fable-pin bütçesiyle (V56 ERTELENDİ) çelişir; nesnel-görev azlığında kazanç zaten sınırlı.
4. **Council maliyet-kısma kaldıraçları (seçici-tetik, erken-durma, batch %50) çift-atlas'ın KENDİSİNE uygulanmalı mı?** — B1'in "çift-atlas ×2 en akut maruziyet" bulgusuyla birleşince, doğru yön ekleme değil BUDAMA olabilir.
5. **Değerlendirici ayrımı (m.7) V53 başkanında nasıl korunur** — Fable-council Fable'ı puanladığında öz-kayırma maksimum; ayrı-model-judge Fable-pin ile çelişir.

---

*Bu rapor B3 kartının çıktısıdır (m.41 yan-oturum): 5 aile × 2 şerit + 1 envanter = 11 Atlas koşumu, çift-atlas (tez ∧ ¬tez). Karar ALINMADI, kanon DEĞİŞMEDİ; yalnız bulgu + "nedir" açıklaması + kategori/kontrol + dürüst bayraklar sunuldu. V53'ün "token maliyeti BİLİNMİYOR" açık borcu bu raporla kısmen kapandı (süperlineer, kısılabilir, Katman-1'e ayrılmalı). Sıradaki kuyruk: B4 (Adaptif-optimizasyon: non-stationary bandit O6 + meta-learning/L2O O11).*
