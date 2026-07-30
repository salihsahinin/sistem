# A2 — JARVIS İşletme-Maliyeti & Abonelik Ekonomisi — Atlas Raporu (2026-07-20)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ, karar ALINMADI) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: **5** (abonelik-limiti · çok-ajan çarpanı · optimizasyon-desenleri · bütçe-tavanı · ünlü-isimler) → 10 literatür/pratisyen şeridi + 1 maliyet-karar envanteri.
> **Kanıt kısıtı (dürüstlük):** Fiyat/limit/caching için **yetkili iç referans (claude-api skill, önbellek 2026-06)** kullanıldı [D]. Web şeritlerinde birkaç birincil kaynak (anthropic.com/engineering, a16z, epoch, augmentcode) egress-403 verdi → o rakamlar WebSearch-özeti [K]. **Fable modeli:** web ajanları kamuya-açık Fable fiyatı bulamadı ("belgeli tier değil" [?]) — çünkü model çok yeni (bilgi-cutoff); ama iç referansta Fable 5 = **$10/$50 per MTok [D]** doğrulandı. Bu çelişki §5'te uzlaştırıldı.
> **Okuma sırası (Fable):** §0 Carvis sentezi + §4 dürüst bayraklar → yeterli. Detay: §1 aile bulguları · §2 ünlü isimler · §3 maliyet-kararlarının kategori+kontrolü · §5 V26 · §6 açık sorular.

---

## §0 — Carvis sentezi (önce oku)

**Soru (A2):** JARVIS'i (çok-yüzey Cowork+CC · çok-ajan paralel-vardiya/çift-atlas/subagent · otomasyon) koşmanın gerçek maliyeti nedir, abonelik bütçesinde nasıl tutulur? Bağlam: Salih ana modeli BÜTÇE gerekçesiyle Fable'a sabitledi (V56; "abonelik kapsamı"), Fable-only kapsam sorusu (yan-oturum Opus / fan-out Sonnet dahil mi) çelişki-kapısıyla Salih'te açık.

**Çıpa fiyatlar [D, claude-api referansı]:** Fable 5 **$10/$50** · Opus 4.8 **$5/$25** · Sonnet 5 **$3/$15** ($2/$10 tanıtım) · Haiku 4.5 **$1/$5** (per 1M token, giriş/çıkış). Cache-read ~0.1× · cache-write 1.25× (5dk TTL) / 2× (1sa). Batch API %50 indirim. **Abonelik [K, web]:** Pro $20 · Max 5× $100 · Max 20× $200 · Team $25-125/koltuk; kota Cowork+CC arasında PAYLAŞIMLI; 5-saatlik pencere + haftalık tavan.

**Kesişim (tez∧antitez'in ORTAK dediği — en sağlam):**

1. **Abonelik JARVIS'in NORMAL işi için çok güçlü (API'ye karşı 2-15× ucuz) — ama JARVIS'in İMZA deseni tam da bu ekonomiyi kıran şey.** Ağır interaktif/tek-thread işte >%90 cache-read → bir vaka 10B token = $15k API vs ~$800 Max (%93 tasarruf) [K]. AMA: kota Cowork+CC arasında paylaşımlı [D], haftalık tavan bilerek power-user'ı (JARVIS'in tam profili) kısar [D], **fan-out kotayı N× yer** ve **subagent parent-cache önekini miras almaz** (soğuk başlar, tam fiyat) [K] — aboneliğin cache-avantajı fan-out'ta çöker. ⇒ Abonelik-değeri GERÇEK ama **koşullu:** eşzamanlılık sınırlı + orkestratör ucuz-model + önek-disiplini.

2. **Çok-ajan/fan-out DEĞER ama yalnız dar bir sınıfta; çoğu JARVIS işinde israf.** Anthropic'in kendi sistemi tek-ajanı %90.2 geçti ama ~15× token [K]; token-harcaması başarı varyansının ~%80'i [K]. AMA çok-ajan yalnız "iş değeri artan performansı ödüyorsa" ekonomik (Anthropic'in kendi sınırı); Cognition "Don't Build Multi-Agents"; güvenilirlik çarpımsal çöker (0.95¹⁰≈%60 → retry → token); eşit-bütçede tek-ajan çok-ajanı yakalar; seri-derin akıl yürütmede fan-out net-artı değil [K]. ⇒ Fan-out net-artı YALNIZ genişlik-öncelikli + bölünebilir + yüksek-değerli işte (K-017-tipi tarama) — **m.25 ölçek-optimizasyonuyla birebir.**

3. **Maliyet-optimizasyon desenleri gerçek ve bileşik keser — JARVIS'e en uyan ikisi caching + routing.** caching %90 [D], Haiku 5× [D], routing %48-85 (RouteLLM %95 kalite %26 çağrıyla [D]), Batch %50 [D], LLMLingua 2-20× [D]. AMA "ucuz model ≠ ucuz iş" fiyat-tersine-dönmesi (5 çiftin 1'i, doğru metrik başarılı-iş-başına) [K]; caching kırılgan (TTL 5dk, önek byte-identik) [K]; batch interaktif-uyumsuz. ⇒ Antitezden sağ çıkan + JARVIS-uyumlu ikisi: **prompt-caching (SessionStart kararlı-önek!)** + **görev-ölçek routing (m.25 zaten manuel router)**.

4. **Bütçe-tavanı desenleri var ve K-009 planıyla birebir — ama "vendor limit ≠ kill-switch" ve enforcement ajan-DIŞI olmalı.** Üçlü (step-limiti + wall-clock/curfew + token-cap) = kaçakların %90'ı [K]; LiteLLM gerçek hard-cut; cost-velocity kesici; Anthropic Console spend-limit [D]. AMA kaçak-maliyet BELGELİ bir başarısızlık modu: Claude Code **#68110** tek çağrı → **48+ ajan / 1.5M+ token, derinlik limiti yok** [D]; $500M/ay kaza; gecikmeli fatura; kill-switch istek-yolunda olmalı [K]. ⇒ K-009 üçlüsü doğru MVP ama **cost-velocity + ajan-dışı enforcement + derinlik-limiti** eksik.

5. **Ünlü isimler: capability-first + maliyet-optimizasyonunu ölçeğe ERTELE (ölçüm + birkaç kaldıraç).** OpenAI resmi "en güçlü modelle başla → sonra distille et"; Karpathy "don't be a hero"; LLMflation fiyat yılda ~10× düşüyor → erken optimizasyon amorti olur; "$100/ay altında mühendis-zamanı > token tasarrufu" [K]. Willison/Huyen/Yan/Husain: ölçüm + caching/routing/kademe. ⇒ Pre-scale JARVIS için ince token-optimizasyonu erken; erken de gereken tek kontrol = **kaçak-guardrail**.

**JARVIS'e ne demek (gözlem, KARAR DEĞİL — m.41):**
- **"Fable bütçe için" (V56) abonelik-kapsamında SAĞLAM** — ama iki dürüst keskinleştirme: (a) Fable API'de EN pahalı tier ($10/$50 > Opus $5/$25); "bütçe" yalnız abonelik düz-ücretine bağlı, aşım'a sıçrarsa Fable en pahalı; (b) asıl bütçe-riski MODEL değil DESEN — haftalık saat-bazlı tavanı yakan fan-out eşzamanlılığı, model-bağımsız (Aile-A/B antitez + pratisyen konsensüs). "Hangi model" bütçenin asıl kaldıracı değil; "kaç eşzamanlı ajan × hangi sıklıkta" öyle.
- **En yüksek-kaldıraçlı, JARVIS-hizalı, antitez-dayanıklı üç hamle (harita, öneri değil):** (1) SessionStart kararlı-önekinde prompt-caching disiplini (Model-C işi tam bu); (2) görev-ölçek routing (m.25 — küçük iş ucuz model, yalnız eşik üstü tırmandır); (3) kaçak-guardrail (cost-velocity + ajan-dışı kill-switch + derinlik-limiti), ki K-009 üçlüsü buna muhtaç.
- **Çift-atlas varsayılanı (m.40-ek) en büyük maliyet-maruziyeti** — Anthropic çok-ajanı yüksek-değerli işle sınırlarken JARVIS TÜM araştırmayı çift-koşuyor; m.25 eşiğine bağlanabilir.

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile A — Abonelik/fiyatlandırma gerçeği
- **Tez:** Abonelik API'ye karşı 2-15× ucuz (Max 20× = $200 düz vs $600-1.500 API-değeri; cache-read %90 sayesinde). Solo-Salih + çok-ajan için tek Max 20× optimal. [K]
- **Antitez (¬):** Kota Cowork+CC PAYLAŞIMLI [D]; haftalık tavan power-user'ı bilerek kısar (Ağu 2025) [D]; Max'te Opus kotası dar (15-40 saat/hafta) [K]; fan-out N× yer; aşım → standart API fiyatı [D]; limitler dinamik SIKILAŞIYOR [K].
- **Kesişim:** Abonelik-değeri GERÇEK ama eşzamanlılık-sınırlı + cache-disiplinli koşulunda; fan-out üç koşulu da kırar.

### Aile B — Çok-ajan/fan-out maliyet çarpanı
- **Tez:** Anthropic çok-ajan %90.2 kalite kazancı, ~15× token'a değer (breadth-first/yüksek-değerli işte); token = %80 başarı-varyansı. [K]
- **Antitez (¬):** 15× yüksek-değerli işle SINIRLI; Cognition "don't build multi-agents"; güvenilirlik 0.95¹⁰≈%60; çarpan 1.6-6.2× (patolojik 4-220×); çift-atlas ×2 tabana biner; kişisel bütçede sürdürülemez. [K/D]
- **Kesişim:** Fan-out net-artı yalnız genişlik-öncelikli/bölünebilir/yüksek-değerli işte (m.25 eşiği); çoğu JARVIS işi bu profile uymuyor.

### Aile C — Maliyet-optimizasyon desenleri
- **Tez:** caching %90 [D], Haiku 5× [D], routing %48-85 [D/K], Batch %50 [D], LLMLingua 2-20× [D], heartbeat ~7× [?]; bileşik çarpar. En uyan: caching (SessionStart) + routing (m.25).
- **Antitez (¬):** "ucuz≠ucuz-iş" (fiyat-tersine, 5'te 1) [K]; caching kırılgan (TTL 5dk, önek-byte, subagent cache-miss); router sessiz yanlış-yönlendirme; sıkıştırma kalite/halüsinasyon riski; batch interaktif-uyumsuz; erken-optimizasyonun kendi zaman maliyeti. [K]
- **Kesişim:** Doğru metrik = başarılı-iş-başına maliyet; JARVIS'e sağ-çıkan ikisi caching (önek-disiplinli) + task-scale routing; gerisi dar/riskli.

### Aile D — Bütçe-tavanı/kota mimarisi
- **Tez:** Üçlü (step + wall-clock/curfew + token) = kaçakların %90'ı; LiteLLM gerçek hard-cut; cost-velocity; Anthropic Console spend-limit; BAMAS (AAAI-26). K-009 üçlüsüyle birebir. [D/K]
- **Antitez (¬):** Kaçak BELGELİ — #68110 (48+ ajan/1.5M token, limitsiz) [D]; $500M/ay; ~1 gün gecikmeli fatura; kill-switch istek-yolunda olmalı; vendor "limit" çoğu uyarı, kesme değil (OpenAI hard-cap kaldırıldı) [K]. Tek hard-cap yetmez. [K/D]
- **Kesişim:** K-009 üçlüsü doğru MVP; eksik = cost-velocity kesici + ajan-DIŞI enforcement + derinlik-limiti (fan-out özyinelemesine karşı). Bu oturumdaki 8-saat-6-ajan-stall canlı örnek.

### Aile E — Ünlü isimler / maliyet-yönetimi
- **Tez:** Willison (cost-tracking), Anthropic (caching), Huyen (maliyet-gecikme, AI Eng. böl.9), Yan (caching kalıbı), Husain (ucuzdan-pahalıya kademe), swyx (maliyet-eğrisi). İki eksen: ölçüm + kaldıraç. [D/K]
- **Antitez (¬):** OpenAI "en güçlü modelle başla → distille et"; Karpathy "don't be a hero"; LLMflation ~10×/yıl → erken optimizasyon amorti; "$100/ay altı: mühendis-zamanı > tasarruf". [D/K]
- **Kesişim:** capability-first + optimizasyonu ölçeğe ERTELE; pre-scale JARVIS için ince-optimizasyon erken, tek gereken kaçak-guardrail. ("maliyet umursanmaz" DEĞİL — "ölçeğe ertele".)

---

## §2 — Ünlü isimler haritası (maliyet-yönetimi)

| İsim | Yaklaşım | Eksen | Kaynak (çoğu web-özeti [K]) |
|---|---|---|---|
| Simon Willison | Token/maliyet-takibi + fiyat-kıyası (llm-prices.com) | ÖLÇÜM | llm-prices.com; simonwillison.net |
| Anthropic (resmi) | Prompt caching (cache-read %90) | KALDIRAÇ | platform.claude.com prompt-caching [D] |
| Chip Huyen | Inference maliyet-gecikme dengesi (AI Eng. böl.9) | KALDIRAÇ | aie-book [D] |
| Eugene Yan | "Caching: gecikme+maliyet düşür" kalıbı | KALDIRAÇ | eugeneyan.com/llm-patterns |
| Hamel Husain | Ucuzdan-pahalıya kademe (prompt→fine-tune) | KADEME | hamel.dev/evals-faq |
| swyx / Latent Space | Maliyet-eğrisi ekonomisi (Artificial Analysis) | ÖLÇÜM | latent.space |
| **OpenAI (resmi)** | **"En güçlü modelle başla, doğruluğu tuttur, SONRA distille et"** | **CAPABILITY-FIRST** | developers.openai.com model-selection [D] |
| **Andrej Karpathy** | **"Don't be a hero" (erken-optimizasyon karşıtı)** | **CAPABILITY-FIRST** | karpathy.github.io/recipe |
| a16z / Epoch | LLMflation: fiyat ~10×/yıl düşüyor | ERTELE | a16z LLMflation (403) [K] |

**Ders:** İki kamp değil, iki FAZ — önce capability (en güçlü model, ölçüm), sonra ölçekte optimizasyon (caching/routing/kademe). JARVIS pre-scale olduğundan capability-first fazındadır; tek istisna kaçak-guardrail (ölçek beklemez).

---

## §3 — Maliyet-kararlarımızın merceğiyle KATEGORİ + KONTROL

Envanter (senaryo-defteri D-serisi + tüzük m.30-42 + fikir-kutusu V28/39/53/56 + planlı-optimizasyon O5/O10/O13) maliyet merceğiyle 4 kategoriye ayrılıyor.

**Kategori A — Maliyet ÖLÇÜLMÜŞ + koşumla doğrulanmış:** **D11** (V39 dar koşum: $7,16 · 19,5 dk duvar · /usage TAM — **tek eksiksiz maliyet-çifti**); D4 (K-017: ~2,4M token · 8,5 dk — token gerçek, kalite türetilmiş).

**Kategori B — Maliyet-boyutlu ama ÖLÇÜLMEDEN koştu (görünmez maliyet):** D7 (Opus+maks-efor, **token boş** — /usage istenmedi), D8 (**token+süre boş** — bulut-Routine yapısal), D10 (8× ölçülmedi), D13 (gece token bekliyor), D14 (×2 bekliyor), D20 (WER bekliyor). → **Kritik: maliyet-çifti D11'e kadar hiçbir blokta tam değildi.**

**Kategori C — Sayı-içeren ama TÜRETİLMEMİŞ (m.39/A7 risk-bölgesi):** D1 (5/3/%5/15), m.31 (N=5), m.42(e) RİSK-formülü, V53 (~2,5× — E4 Debate'ten, bizim için ölçülmemiş), V56 (fiyat kaynaklar-arası ÇELİŞKİLİ [?]).

**Kategori D — Bütçe-riski taşıyan:** V56/Fable-only kapsam (Salih'te AÇIK), D14 çift-atlas ×2, D7/D8/D13 görünmez-maliyet koşumları, V53 council ~2,5×, bulut-Routine yapısal maliyet-körlüğü, m.30 Fable→Opus yükseltme.

**Mercek bulgusu:** Envanter maliyet-yönetiminin ön-koşulunu ihlal ediyor — **ölçmeden yönetemezsin.** Maliyet-boyutlu 10 karardan yalnız D11 tam ölçüldü; bulut-Routine'de token YAPISAL boş kalıyor (D8), ki bu tam #68110/8-saat-stall sınıfı görünmez-maliyet riskidir. JARVIS bunu zaten işaretlemiş (D8: "maliyet-gözlem mekanizması K-009 tasarım girdisi"); D11'in /usage-emri deseni standart tetik olmalı görünüyor.

---

## §4 — Yanlış / zayıf gördüklerim (dürüst bayraklar — KARAR ALMADIM, DEĞİŞTİRMEDİM)

1. **"Fable bütçe için" gerekçesi yalnız abonelik-kapsamında geçerli — asıl bütçe-riski model değil DESEN.** Fable API'de en pahalı tier ($10/$50 > Opus $5/$25); "bütçe" flat-fee'ye bağlı, aşım'a sıçrarsa Fable en pahalı. Daha önemlisi: haftalık saat-bazlı tavanı yakan fan-out eşzamanlılığı, model-bağımsız (Aile-A/B antitez + pratisyen konsensüs). Bayrak: "hangi model" bütçenin asıl kaldıracı değil; "kaç eşzamanlı ajan × hangi sıklıkta" öyle. *(Gözlem; V56/Fable-only kapsam kararı zaten Salih'te açık.)*

2. **Çoğu maliyet-kararı MALİYET ÖLÇÜLMEDEN koştu (D7/D8/D10/D13/D14); yalnız D11 tam.** Bütçe yönetiminin ön-koşulu ölçüm; bulut-Routine token yapısal boş. Bayrak: /usage-emri (D11 deseni) standart tetiğe bağlanmadan gece-otomasyon (K-009) maliyeti görünmez birikir — #68110/8-saat-stall sınıfı risk. *(Gözlem; D8 bunu K-009 tasarım-girdisi olarak zaten işaretlemiş.)*

3. **Çift-atlas varsayılanı (m.40-ek: TÜM araştırma çift-koşum) en büyük maliyet-maruziyeti.** Anthropic çok-ajanı yüksek-değerli işle sınırlıyor; antitez çoğu işin uymadığını söylüyor. JARVIS'in "koşullu çift-atlasa daralma" tetiği REAKTİF (bütçe baskısını bekler), proaktif ölçek-eşiği kapısı değil. Bayrak: çift-atlas her araştırmada değil, yalnız genişlik-öncelikli/yüksek-değerli/bölünebilir işte net-artı; m.25 eşiğine bağlanabilir görünüyor. *(Gözlem — bu raporun A2 koşumu bile 11-ajan çift-atlas: yüksek-değerli mi tartışılır.)*

4. **K-009 kota-üçlüsü (kota-JSONL + curfew + tur-limiti) doğru MVP ama kaçak-guardrail'i tamamlanmamış.** Aile-D antitez: tek hard-cap yetmez; #68110 (48+ ajan, derinlik limiti yok) + bu oturumdaki 8-saat-6-ajan-stall canlı kanıt. Eksik: **cost-velocity kesici** (saatlik harcama-hızı) + **enforcement ajan-DIŞI** (ajan atlayamasın) + **derinlik/sayı-limiti** (bir çağrının N-ajan doğurmasına karşı). Bayrak: mevcut üçlü zaman/tur/token'ı kapsar ama özyinelemeli alt-ajan fan-out'unu yakalamaz. *(Gözlem.)*

5. **"ucuz model ≠ ucuz iş" (V56 dersi) ile D11 gözlemi çelişebilir — görev-sınıfına bağlı.** V56: Haiku çok-turlu işte toplam token'ı kötüleştirdi. Ama D11'de haiku fan-out maliyeti DÜŞÜRDÜ, kaliteyi değil. Aile-C antitez fiyat-tersine-dönmesini doğruluyor (5'te 1). Bayrak: "ucuz model" kararı tek genel kural değil — analitik/çok-turlu işte pahalı, mekanik/tek-turlu işte ucuz; V56-dersi + D11-karşı-gözlem birlikte okunmalı. *(Gözlem; m.35 ölçüm-öncelik bunu kalibre eder.)*

6. **Maliyet-çarpanları BİNER: V53 council (~2,5×) + çift-atlas (×2) + fan-out (base 4-15×).** Aynı koşumda birleşirse çarpanlar toplanmaz, birleşerek büyür (Aile-B antitez). Bayrak: council + çift-atlas + fan-out'un aynı işte üst üste binip binemeyeceği — birbirini dışlayan mı katmanlı mı — tanımlanmamış; en pahalı kombinasyon budur. *(Gözlem.)*

**Genel not:** JARVIS'in çekirdek sezgisi (Fable-abonelik + ucuz-orkestratör + m.25 ölçek-optimizasyonu + K-009 kota-üçlüsü) doğru yönde. Bayraklar "yanlış yapıyorsunuz" değil; "asıl kaldıraç desen-eşzamanlılığı, ölçüm eksik, guardrail tamamlanmamış" uyarılarıdır.

---

## §5 — V26 örneklem-denetimi

| Şerit/kaynak | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| Çıpa fiyat | Fable $10/$50, Opus $5/$25, Haiku $1/$5; cache-read 0.1×, write 1.25/2× | **[D]** (claude-api iç referans) | "Fable en pahalı tier" bulgusu sağlam |
| Aile-C tez | Prompt-caching cache-read = base'in %10'u (%90 indirim) | **[D]** (Anthropic docs, ajan fetch etti) | Optimizasyon ayağı sağlam |
| Aile-D antitez | Claude Code #68110: tek çağrı → 48+ ajan, 1.5M+ token | **[D]** (github fetch) | Kaçak-risk ayağı sağlam |
| Aile-B | Anthropic multi-agent ~15× token / %90.2 kalite | **[K]** (anthropic.com 403 → snippet) | Çürütülmedi; birincil-teyit yok |
| Fable web-fiyatı | "Fable belgeli tier değil" | **UZLAŞTIRILDI:** web bulamadı (yeni model/cutoff), iç referans [D] $10/$50 | [?] → [D] |

**Sonuç:** Fiyat çıpası + caching + #68110 birincil/yetkili doğrulandı [D]; Anthropic-15× snippet düzeyinde [K] (egress-403). Bu koşumda 403 A5'ten hafif; kavramsal iskelet güvenilir, birkaç tekil rakam [K].

---

## §6 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **Fable-only kapsam** (yan-oturum Opus / fan-out Sonnet dahil mi) — zaten Salih'te açık; bu rapor "asıl kaldıraç model değil eşzamanlılık" verisini ekliyor, karar değişmedi.
2. **Çift-atlas m.25 eşiğine bağlanmalı mı?** Varsayılan-açık/tetikle-daralt yerine varsayılan-eşikli (yalnız genişlik-öncelikli/yüksek-değerli işte) — Katman-1 kanon dokunuşu, Salih+ana-sıra.
3. **K-009 guardrail'i cost-velocity + ajan-dışı enforcement + derinlik-limiti ile tamamlanacak mı?** Aile-D önerdiği üçlü-ötesi; K-009 tasarım gündemi.
4. **/usage-emri (D11 deseni) standart tetik olacak mı?** Görünmez-maliyet (D7/D8) çözümü; K-009/K-019 tasarım girdisi.
5. **Council + çift-atlas + fan-out kombinasyonu** dışlayan mı katmanlı mı — en pahalı senaryo, tanımsız.
6. **Abonelik katmanı seçimi** (Max 20× vs Team) — Katman-1 para kararı, Salih; bu rapor yalnız fiyat-veri sunar.

---

*Koşum: A5-yöntemi (m.40b çift-atlas) · 5 aile × 2 şerit = 10 Atlas ajanı + 1 maliyet-karar envanteri (Explore) + claude-api yetkili fiyat referansı + Carvis V26 denetimi. Ham şerit çıktıları bu oturumun task-transcript'lerinde; bulgular yukarıda etiket+URL ile gömülü. Sıradaki kuyruk: A4 · B1 · B2(+ne-o) · B3 · B4 · B5(+ne-o).*
