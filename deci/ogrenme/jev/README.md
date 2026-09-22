# Jev / System One Karar Modelleri — Sıfırdan Uygulama Serisi (Karar 108, 2026-09-22)

> **Salih beyanı (09-22, aynen):** "yeni çıkan yapay zeka jev'i de kullanmaya başlayalım o da bir ajanımız olsun ama jevin ne olduğunu nasıl çalıştığını ve sisteme nasıl implement edeceğimizi öğrenmem için seri oluştur". Seri üç soruyu sırayla kapatır: **ne** (J1-J2) · **nasıl çalışır** (J3-J4) · **sisteme nasıl girer** (J5-J6).

**Yüzey:** bu dizin (`~/sistem/deci`), ajan Deci (Sonnet 5 medium + eskalasyon), açılış tetiği **"seans başı, jev"**. Ders iskeleti (`PROBE` · `PLAN` DAG · kutu başlıkları) Jarvis'ten `cc/gelen/ders-J<N>.md` ile gelir; ajan `TEACH`/`CLOSE` koşar (Karar 105 M4). **Pratik = Salih'in eli**: komutu/çağrıyı Salih koşar, ajan iskele + yorum; `DONE` yalnız Salih beyanıyla.

## Zemin (AS-OF 2026-09-22, canlı çekildi; kaynaklar altta)
- **Ne:** TypeSafe AI'nin (SF, kurucu Diogo Almeida — eski OpenAI, RLHF/InstructGPT; Erik Gafni, Sasha Sheng) "System One" modeli. Metin üretmez; **typed karar + kalibre olasılık + confidence** döndürür. Sürüm `jev-1.13.0`; erken erişim **2026-09-15** (waitlist, `console.typesafe.ai`); $40M seed (DCVC), değerleme $200M (Forbes) `[K]`.
- **Üç primitif:** `Choice` (≤255 seçenek; `choice` + `probabilities` + `confidence`) · `Score` (2-10 sıralı seviye; kesirli skor) · `Noul` (evet/hayır olasılığı 0-1). İstek = **state** (string / JSON / metin dizisi) + N **question**; tüm sorular tek geçişte paralel değerlendirilir ("adding questions barely changes the response time").
- **Eğitim:** sentetik veri + RLCD (Reinforcement Learning for Calibrated Decisions: olasılık **sonuca** karşı optimize, insan tercihine değil) `[K — satıcı beyanı, ağırlık/spec yayımlanmadı]`.
- **Rakamlar (satıcı, kendi iç iş-yükü; bağımsız tekrar yok):** gecikme 70-500 ms · $0,042 / M giriş token, çıkış ücretsiz · "40-200× hızlı, 40-400× ucuz"; tepe 193,6× / 444,6× · sınıflandırmada doğruluk %67,8 (frontier-konsensüs etiketine karşı; Sonnet 5 ile başa baş) `[K]`.
- **SDK:** `pip install typesafe-sdk` · `npm i @typesafe-ai/sdk` · Java `typesafe-java-sdk` · Pydantic AI `Agent('typesafe:jev-latest', output_type=...)` (bool → noul, Literal/Enum → choice, IntEnum docstring → score; `provider_details` = confidence/probabilities/scores) · Vercel/Netlify AI Gateway, OpenRouter.
- **Sınırlar (docs):** metin/kod/özet üretmez · sayma ve tarih aritmetiğinde güvenilmez · talimatı **harfiyen** okur (olumsuzlama, kapsam sözcükleri) · bağlam şişince doğruluk düşer · **state adversarial sayılmaz** (kullanıcı içeriği cevabı bükebilir → Gard bağı).

## Müfredat — 6 hafta (oturum 1,5-2 sa; `DONE` yazılı)
| J | Konu | Sektör başlığı (EN; AS-OF 2026-09-22, ders başında yeniden teyit) | Tek-satır `DONE` (Salih yapar) | Formül (Karar 73) | Araç / kaynak |
|---|---|---|---|---|---|
| J1 | **Ne bu:** LLM ↔ karar modeli; neden metin değil tip; kalibre olasılık ne demek; RLCD; adın kaynağı (Jevons paradoksu) | *System One Models* · *Structured Judgment* · *Calibrated Decision Model* · *Jevons Paradox* | konsol erişimi (waitlist) + ilk `Noul` çağrısı; cevap JSON'unu yapıştırma | kalibrasyon: Brier = (1/N)Σ(p−y)² · ECE = Σ (n_b/N)·\|acc_b − conf_b\| (elle 10 örnek) | docs.typesafe.ai/introduction · Wikipedia Jev · DataCamp yazısı |
| J2 | **Üç primitif + istek anatomisi:** choice/score/noul; state + questions; seçenek **açıklaması** etkisi (çıplak etiketle confidence 0,60'a düşer, docs örneği); paralel soru | *Decision Primitives* · *Choice / Score / Noul* · *State + Questions* · *Option Descriptions* | 10 örnek bilet üzerinde 3 primitifle 3 soru; açıklamalı ↔ çıplak seçenek confidence farkı tablo | confidence = karar eşiğinden marj; entropi H = −Σ p log p (dağılım "kararsızlığı") | typesafe-sdk (Python) · dev.to pratik kılavuz |
| J3 | **Kalibrasyon + eşik tasarımı:** confidence-gated routing; eylem başına eşik (okuma >0,5 · finans >0,85 örneği); retrieve-then-judge; "jaggedness page" | *Confidence-Gated Routing* · *Human Escalation* · *Retrieve-then-Judge* · *Model Jaggedness* | kendi 50 etiketli örnekte reliability diagram + eşik seçimi | beklenen zarar E = P(hata)·maliyet; eşik τ*: E_otomatik(τ) = E_insan | sklearn `calibration_curve` · TypeSafe jaggedness sayfası |
| J4 | **Mimari desenler:** kaskad (Jev yönlendirir, kod/LLM icra eder), spekülatif fan-out, soru ayrıştırma ("her faktör ayrı soru, mantık kodda"), maliyet hesabı | *Decision Cascade* · *Speculative Fan-out* · *Question Decomposition* · *Cost-per-decision* | 1 M bilet senaryosu: LLM-tek ↔ kaskad maliyet tablosu (docs: ≈$6.480 ↔ $30.400 `[K]`) | maliyet = Σ_dal P(dal)·c_dal; hız = maks(paralel) | Spring AI / Vercel AI SDK kılavuzları |
| J5 | **Sisteme implement:** Jarvis karar noktaları — (a) hakem D/K/X ön-sınıflama · (b) ingest v2 triyaj (tip/hedef) · (c) hook `RED` haklı/haksız sayacı · (d) eskalasyon tetiği; Pydantic AI köprüsü; güvenlik: state adversarial değil → Gard vaka seti | *Decision Layer in Agent Systems* · *Router / Judge Separation* · *Prompt-injection surface of decision models* | (a) ya da (c) için prototip: 30 kayıt, Jev ↔ Sonnet 5 etiket uyumu (κ) | Cohen κ = (p_o − p_e)/(1 − p_e); yapan ≠ ölçen (hakem eval'i Tart'a) | Pydantic AI docs · Jarvis `tools/` · `cc/giden/` öneri şablonu |
| J6 | **Eval + ürün turu:** kendi trafiğinde doğruluk/kalibrasyon ölçümü (satıcı %67,8 iddiası ↔ kendi ölçüm), regresyon seti, kapanış: hangi karar noktası üretime | *Offline Eval of Decision Models* · *Calibration Drift* · *Production Gate* | ürün turu hükmü masaya (3 seçenek, biri "hiçbiri") | hayatta-kalma: Jev doğru / toplam, Wilson %95 GA | promptfoo (Tart H-serisi ile ortak) |

## Sınırlar
- md.49: şirket/staj verisi yok; oyuncak vakalar + depo içi kayıtlar (hakem raporları, hook kütükleri).
- Her satıcı rakamı `[K]`; **D** yalnız kendi koşumunla (m.39, Karar 68). Jev erken erişimde: waitlist açılmazsa J1-J4 kavramsal `DONE`, pratik `KALAN`.
- Hazırı temel al: SDK/Pydantic köprüsü kullanılır, kendi HTTP sarmalayıcısı yazılmaz.

## Ders kaydı biçimi
`dersler/YYYY-MM-DD-JN-konu.md`, şema `ogren` §5. Kutu başlığı yanında sektör başlığı.

## Kaynaklar (çekim 2026-09-22)
- https://docs.typesafe.ai/introduction · https://docs.typesafe.ai/llms.txt (tam indeks)
- https://en.wikipedia.org/wiki/Jev_(AI_model) · https://www.datacamp.com/blog/system-one-models-jev
- https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e
- https://pydantic.dev/docs/ai/models/typesafe/ · https://spring.io/blog/2026/09/21/spring-ai-typesafe-structured-judgment/ · https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk
