# JARVIS'i Geliştirme — Proje Fikirleri, Kronolojik Zorluk Partisyonlarına Ayrılmış

*2026-07-16 · Carvis sentezi · Kaynak: 4 paralel Atlas koşusu (Beyin/Hafıza · Motor/Orkestrasyon · Arayüz/Ses-Proaktiflik · Meta/Öz-gelişim). Web taraması Ocak–Temmuz 2026'yı kapsadı.*

> **Amaç:** V29/#13 ufkuna (Iron Man'in JARVIS'i — sesli · çok-ajanlı · proaktif · her-yüzeyden · öz-gelişen) giden yolu, **zorluk + bağımlılık sırasına** göre partisyonlara bölmek. Her partisyon bir zorluk katmanı; her sınıflandırma bir proje-fikri kategorisi; her kategoride **"örneğin …"** somut örnek.
>
> **İsim şerhi (çakışma önleme):** Bu partisyonlar **G0–G6** (Geliştirme/zorluk ekseni) adıyla anılır — `raporlar/partisyon-plani-P0-P6-2026-07-14.md`'deki **tarihli P0-P6 proje-takvimi** (CV/PortRisk hattı) AYRI eksendir, karıştırılmaz.
>
> **Zorluk etiketi:** Z0 (salt-dosya/prompt) · Z1 (kolay/lokal-script/tek-ajan) · Z2 (orta/çok-ajan+RAG+eval+scheduled) · Z3 (zor/proaktif-otonom+ses+çok-yüzey) · Z4 (ufuk/öz-gelişen+AGI-orkestra).
>
> **Statü:** HAM FİKİR yüzeyi — hiçbir madde karar değildir (m.20 pointer sistemi). Build'e girecek her fikir seçim turundan geçer. Bu rapor fikir-kutusuna pointer olur.

## Bağımlılık omurgası (tek cümle)
**Ölç → cetvele güven → beyni doldur+öz-editlet → şirket motorunu kur → otonomiden ÖNCE bağışıkla → proaktiflik+ses (canlı aktör) → özyinelemeli öz-gelişim.** Ses ve canlı-ajan bilinçli olarak en sonda (en zor + en riskli); JARVIS'in "sıralama ilkesi" ile birebir.

## Partisyon özeti (tek bakış)

| # | Tema | Z-aralığı | KAPI (bir üste geçmek için ne bitmeli) |
|---|------|-----------|----------------------------------------|
| **G0** | Hazır zemin & ölçüm cetveli | Z0–Z1 | Her koşum yapısal/oynatılabilir trace bırakıyor · wiki delta-güncellenebilir formatta · ≥20-50 görevlik eval-seti · Katman-1 kuralları hook'ta |
| **G1** | Değerlendirme & kalibrasyon | Z1–Z2 | "Bu değişiklik daha mı iyi?" otomatik cevaplanıyor · judge-insan uyumu (kappa) raporlu · regresyon yakalanıyor |
| **G2** | İçerik-yakalama & öz-editlenen beyin | Z1–Z2 | Carvis bir wiki/skill'i tekrarlı görevde ölçülebilir biçimde, insan-baştan-yazmadan iyileştiriyor · dış içerik düşük-sürtünmeyle ingest oluyor |
| **G3** | Motor & şirket koordinasyonu | Z2 | Birden çok ajan quality-gate'li · çakışmasız · done-kapılı koordine oluyor |
| **G4** | Güvenlik, bağışıklık & gözlemlenebilirlik | Z2–Z3 | Untrusted içerik kanonu sessizce değiştiremiyor · auditor Katman-1'de Salih'e defer ediyor · koşum maliyeti izlenebilir |
| **G5** | Otonomi, proaktiflik & ses | Z3 | Denetlenen sınırlarda proaktif + sesli davranabiliyor, güvenlik-regresyonu yok (**K-009/K-010 kapısı burada**) |
| **G6** | Öz-gelişen çekirdek / AGI-orkestra şefi | Z4 | (Ufuk) Nesiller boyu ölçülen öz-gelişim, güvenlik-regresyonsuz |

---

## G0 — Hazır Zemin & Ölçüm Cetveli `Z0–Z1`
*Neden ilk: Aşağıdaki hiçbir şey ölçüm+yapı olmadan çalışmaz; öz-gelişim ölçümsüz kördür. İyi haber: JARVIS bunun ~%80'ini zaten yapıyor — sahanın adıyla sağlamlaştırmak yeter.*

- **Dosya-tabanlı hafıza substratı + türetilmiş arama indeksi** `Z0` — markdown+git = kaynak-doğruluk; üstüne yeniden-inşa-edilebilir arama katmanı. **Örneğin:** *Basic Memory* (AI sohbetinden markdown bilgi-grafiği, Obsidian+MCP senkron), *memweave* (vektör-DB'siz; markdown + SQLite indeks), Anthropic *Memory Tool* (just-in-time dosya oku/yaz). *JARVIS:* m.10 (commit=hafıza)/m.8 doğrulandı; eksik tek şey grep yerine BM25/SQLite indeks.
- **Katmanlı sıcak/soğuk hafıza + bağlam sıkıştırma disiplini** `Z0→Z1` — sıcak bağlam yalnız aktif ufku taşır, gerisi pointer'la soğukta. **Örneğin:** *anchored incremental summarization* (durum-kapsülünü sıfırdan değil, uzatarak özetle), Anthropic *context editing/compaction*, "Demand Paging for LLM Context" (bağlam=RAM, dış-depo=disk). *JARVIS:* m.21/m.22/m.18'in bilimsel adı; kayıplı sıkıştırma → kritik kararların hamı git-log'da kalır.
- **Ölçüm-substratı: yapısal trace + kalibrasyon defteri** `Z1` — her Carvis koşumu tekrar-oynatılabilir iz + token×zaman×kalite kolonları bıraksın. **Örneğin:** *OpenTelemetry-GenAI* span şeması (agent/tool/model span'leri; CNCF'den mezun oldu, May 2026), dosya-tabanlı trace + *Fatebook*/Brier defteri. *JARVIS:* senaryo-defteri (m.37) + token×zaman fitting'in yakıtı; sonraki tüm optimizasyon buna muhtaç.
- **Guardrail / policy-as-code** `Z1` — Katman-1 kurallarını prompt-disiplininden çalıştırılabilir sigortaya çevir. **Örneğin:** Claude Code *PreToolUse hook* → publish/para/kişisel-veri eylemini onaysız bloke; *NeMo Guardrails*/*Guardrails AI* (ağır uç). *JARVIS:* m.31 Katman-1/2 + YASAKLAR'ı (m.23) koda dök; "klavyede başkası varsa kalıcı değişiklik yok" (m.1) bile bir hook olabilir. Deterministik olmalı (regex/allowlist, LLM-judge değil).

## G1 — Değerlendirme & Kalibrasyon `Z1–Z2`
*Neden ikinci: Cetvele güvenmeden optimize edilmez. 2026'nın sert bulgusu — naif LLM-judge "yazı-tura" oranında güvenilir olabiliyor.*

- **Eval/judge kalibrasyon harness'i** `Z1→Z2` — judge'ı eval'e sokmadan ÖNCE judge'ı kalibre et. **Örneğin:** *promptfoo*/*Braintrust*/*DeepEval* (YAML-eval, regresyon), + pozisyon-swap & self-consistency; "Reliability without Validity / Coin-Flip Judge" (21 judge, ~541K yargı → sıralamalar 14 pozisyon kayıyor) uyarısı. *JARVIS:* "evaluator ilkesi"ni ölçülebilir disipline çevirir; JARVIS'in Brier-kültürü burada avantaj.
- **Hafıza-recall eval seti** `Z2` — "wiki'yi geliştirdim" yerine "geçen ayki X kararını doğru hatırlıyor mu?" **Örneğin:** *LongMemEval*/*LoCoMo* tarzı ev-yapımı "JARVIS-recall" seti; kritik yeti = *abstention* (bilmediğini bilmek). *JARVIS:* proof-of-work (m.9) + epistemik-humility ilkesinin hafıza-katmanına inişi; genel benchmark birebir transfer olmaz, mini-eval şart.
- **Ajansal aşırı-güven / eylem-kalibrasyonu** `Z2` — tahmin kalibrasyonunu EYLEMLERE genişlet. **Örneğin:** *Self-Grounded Verification* (hata-tespiti +~20 puan), verbalized-confidence + ECE; "RLHF kalibrasyonu bozar" bulgusu. *JARVIS:* Brier defterini "eylemden önce kendi başarısını tahmin eden öz-şüpheci ajan"a çevirir; dizilerde biriken-hata farkındalığı.

## G2 — İçerik-Yakalama & Öz-Editlenen Beyin `Z1–Z2`
*Neden üçüncü: Beyin dolar + kendini düzenler — ama hangi hafıza-edit'inin işe yaradığını bilmek G1-eval'ine muhtaç; yoksa hafıza çürür (context collapse). 2026'nın ana tezi: ajan yeteneği artık modeli büyütmekten değil, hafıza+kod+iş-akışı yapısını değiştirmekten geliyor — tam JARVIS'in zemini.*

- **İçerik-yakalama fabrikası (ingest hattı)** `Z1→Z2` — gümrük→işçi→kalite-kontrol→yaşayan-kütüphane. **Örneğin:** *Snipd* (kulaklıktan podcast anı → transkript+özet → Obsidian markdown), *Whisper large-v3* (video/tweet→transkript), *NotebookLM*. *JARVIS:* #26 fabrika deseninin birebir uygulaması; fikir-kutusunu otomatik besleyen boru hattı. KK adımı atlanamaz (kaynak-gürültüsü).
- **Düşük-sürtünme mobil→sistem köprüsü** `Z1` — Salih'in mevcut acı-noktası; en yüksek ROI ilk adımlardan. **Örneğin:** *Voice MD* (Obsidian; iPhone Action Button → temiz markdown), *claude-code-telegram* (telefondan node'a erişim), sesli-not→faster-whisper→vault inbox. *JARVIS:* sürtünmesizlik ilkesi (#18/#19); aynı köprü ilerde proaktif kanal olur (G5).
- **Mem0-tarzı ADD/UPDATE/DELETE + novelty-gate** `Z1→Z2` — yeni bilgi geldiğinde "çelişen kayıt var mı → güncelle mi geçersiz-kıl mı" kararını LLM tool-call'a devret. **Örneğin:** *Mem0* (extraction + LLM'li ADD/UPDATE/DELETE/NOOP), *SAGE* "Novelty Gate" (her şeyi değil, yalnız şaşırtıcıyı yaz). *JARVIS:* çelişki-kapısını (m.16) mekanikleştirir; **DELETE yerine "arşive-indir"** (m.8 otomatik-silme-yasağı korunur).
- **Evolving playbook / delta-hafıza + dinamik bağlama** `Z1→Z2` — wiki'yi baştan yazma; ID'li maddeye helpful/harmful sayaçlı **delta** ekle + yeni sayfa gelince eskileri otomatik bağla. **Örneğin:** *ACE — Agentic Context Engineering* (delta güncelleme, "context collapse" önler; +~%10 ajan), *A-MEM* (Zettelkasten dinamik link + geçmiş notları güncelleme; NeurIPS 2025). *JARVIS:* wiki=beyin (#5) hedefinin en doğrudan motoru; **en yüksek tekil ROI** — wiki zaten var, sadece delta-disiplini eklenir. Evrim yalnız `wiki/`de, `core/`de yasak.
- **Post-mortem → içgörü çıkarımı** `Z1` — başarı/başarısızlık izini doğal-dil içgörüye soyutla, yeniden kullan. **Örneğin:** *Reflexion* (Actor→Evaluator→Self-Reflection bellek-tamponu), *ExpeL* (trajektori→içgörü). *JARVIS:* cc/defter.md "koşum dersi" akışı zaten primitif Reflexion; eksik = otomatik içgörü-soyutlama (m.37 kararları → kural-adayı).
- **Getirme kalitesi: contextual retrieval + hibrit arama** `Z2` — doğru pointer'ı/kapsülü token-verimli getir. **Örneğin:** Anthropic *Contextual Retrieval* (chunk'a konumlandırıcı cümle ekle), *ColBERT*/late-interaction rerank, Qdrant hybrid. *JARVIS:* pointer/progressive-disclosure'ın kalite motoru; "1 token'a düşen bağlamı maksimize et" (#28). Reranker'ı ancak vault büyüyünce ekle.

## G3 — Motor & Şirket Koordinasyonu `Z2`
*Neden dördüncü: "Ajanlar birbiriyle konuşan şirket" katmanı. Kritik içgörü — aradığın primitiflerin çoğu ARTIK Claude Code'da native; dış framework (LangGraph/CrewAI/Temporal) tek-kişi ölçeğinde çoğunlukla erken/gereksiz.*

- **Native şirket katmanı (Agent Teams)** `Z1→Z2` — lead + teammate'ler, mailbox + paylaşımlı görev listesi + quality-gate hook + görev-claim'de file-locking. **Örneğin:** *Claude Code Agent Teams* (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`; Şub 2026). *JARVIS:* "şirket simülasyonu"nun tam native karşılığı; `TaskCompleted` hook (exit 2→geri-besle) = "done yazılamayan iş devredilmez"in çalıştırılabilir kapısı. **Ama teknik hazır ≠ karar açık: canlı-ajan (K-009/010) burada gündeme gelir.** Token maliyeti doğrusal (her teammate ayrı Claude).
- **Ajan-yazılabilir task-DB / pano motoru** `Z1→Z2` — kartlara makine-okur alan (ID, bağımlılık, durum); `bd ready` = bağımlılığı biten işleri çıkarır. **Örneğin:** *Beads* (gastownhall; artık Dolt-powered, cell-level merge, hash-ID). *JARVIS:* pano.md'nin (AKTİF/BEKLEYEN/BLOKE) makine-yazılabilir motoru; **Beads = kalıcı kuyruk, Agent Teams task-list = oturum-içi canlı** ikilisi. Ekosistem çatallanıyor → birini seç-sabitle.
- **Model routing + cascade** `Z1→Z2` — sorgu-başına en ucuz-yeterli model; ucuzla başla, düşük-güvende üste tırman. **Örneğin:** *RouteLLM* (öğrenilen router, ~%85 maliyet↓ ~%95 kalite [?]), *vLLM Semantic Router*, *FrugalGPT cascade*; native tutamak = subagent `model:` frontmatter. *JARVIS:* token×zaman parametresinin doğrudan mekanizması (#14/#17/#24). Cascade gecikme-vergisi getirir → batch'te değerli, interaktifte dikkat.
- **Evaluator "done-kapısı" + Reflexion loop** `Z1→Z2` — done'u rubrikle gate'le, eleştiriyi bellek-dosyasına yaz. **Örneğin:** *Reflexion* + *Agent-as-judge/AdaRubric* (adım-başına rubrik). *JARVIS:* fabrika çıkış-kapısı (#26); Agent Teams hook = enforcement noktası. **Uyarı: LLM-judge sistematik iyimser** — açık rubrik + örneklem-insan-denetimi yoksa Reflexion maliyeti 10-30× artırır, faydası sıfır.
- **İzolasyonlu paralel ajan** `Z1→Z2` — iki ajan aynı dosyaya dokununca overwrite yok. **Örneğin:** Claude Code subagent `Isolation` frontmatter (geçici git-worktree), *Sculptor* (container izolasyon), *Conductor* (worktree-per-ajan GUI). *JARVIS:* PARALEL-VARDIYA'nın güvenli hali; 4-şerit düzenine doğrudan uygulanır. Worktree çakışmayı çözer ama merge kararını sana bırakır.
- **Ortak bellek / markdown-blackboard** `Z1→Z2` — ajanlar birbirini tanımadan paylaşılan alanda okur/yazar. **Örneğin:** *Letta* (eski MemGPT) 3-katman core/archival/recall, Agent Teams "findings-doc"; markdown-blackboard = sıfır altyapı. *JARVIS:* Letta'nın 3-katmanı = katmanlı yerleşim (m.22) birebir; JARVIS dosya-tabanlı olduğu için markdown-blackboard doğal ev, Mem0/Letta ancak darboğazda.
- **Heterojen council / debate** `Z2` — geri-alınması zor kararlarda çok-model müzakere + adaptif durma. **Örneğin:** *Council Mode* (heterojen konsensüs), *Multi-Agent Debate + Adaptive Stability Detection* (konsensüs sabitlenince kes). *JARVIS:* V53 llm-council'e iki ek — heterojenlik (farklı sağlayıcı kat, kör-nokta paylaşımını önle) + adaptif-durma (token×zaman disiplini). "Confident liar" riski → yalnız yüksek-bahisli kararlarda (m.31 Katman-1).
- **Bi-temporal KG + öz-örgütlenen wiki (grafik olgunlaşınca)** `Z2` — "sil değil, geçersiz kıl"; wiki sayfaları arası ilişkiyi elle değil entity-extraction ile kur. **Örneğin:** *Graphiti* (çift-zamanlı: olay-zamanı + öğrenme-zamanı, geçerlilik-aralıklı kenar), *Simple Graph Builder* (Obsidian; hazır eklenti, LLM entity-extraction). *JARVIS:* m.8 + m.22'nin bilgi-grafiği karşılığı; tam Neo4j ağır gelebilir → frontmatter'da `valid_from/valid_until` ile "yoksul-adam bi-temporal" Z1'de denenir.

## G4 — Güvenlik, Bağışıklık & Gözlemlenebilirlik `Z2–Z3`
*Neden beşinci — otonomiden ÖNCE: Sistem öz-editleyip DIŞ içerik sindirdiği an (ATLAS'ın web-araştırması!) zehirleme+injection canlı vektör olur. Bu katman G5 otonomisinin ön-koşulu.*

- **Hafıza-zehirleme + prompt-injection savunması** `Z2→Z3` — her hafıza oku/yaz'ı tara; dış içeriğe köken/güven etiketi. **Örneğin:** OWASP *ASI06 (Memory & Context Poisoning)*, *CaMeL*/*Dual-LLM*/*Plan-then-Execute* deseni, *AgentPoison* (<%0.1 zehirle >%80 başarı) tehdidi. *JARVIS:* wiki edit'lerine yazma-tarama kapısı + untrusted-web damgası; m.8 zaten savunmacı içgüdü → formelleştir. (Saldırılar çoğunlukla vektör-RAG'de çalışıldı; markdown-wiki boş-nokta ama web-ingest riski yükseltir.)
- **Denetçi / güvenilir-monitör ajanı** `Z2→Z3` — ucuz güvenilir model, pahalı güvenilmez ajanı izler; şüphede Salih'e defer. **Örneğin:** Redwood *AI Control*, *MAST* multi-agent hata taksonomisi (14 mod: %42 kötü-spesifikasyon, %37 koordinasyon, %21 zayıf-doğrulama). *JARVIS:* bilinen 7-gate auditor'ın üstü; çelişki-kapısı (m.16) zaten bir "defer" primitifi; MAST-14 = çok-ajanın hazır checklist'i.
- **Gözlemlenebilirlik paneli** `Z1→Z2` — ajan-trace + token/gecikme/maliyet metrikleri. **Örneğin:** *OTel-GenAI* + *Langfuse*/*Arize Phoenix* (OTel-native). *JARVIS:* token×zaman fitting'in görünür hali; G0 trace-substratının panel formu. (Cowork native OTel yaymayabilir → adaptör gerekebilir [?].)

## G5 — Otonomi, Proaktiflik & Ses `Z3`
*Neden altıncı — en sona, en riskli: Canlı aktör. **K-009/K-010 kapısı burada.** İç sıralama = artan otonomi/risk: zamanlanmış (en güvenli, zaten başladı) → heartbeat → ambient → ses → ortam-yakalama.*

- **Zamanlanmış proaktiflik (cron brifing)** `Z1→Z2` — zamanı sen seçtin → "ne zaman konuşmalı" problemini atlatır; yanlış-tetik ~sıfır. **Örneğin:** *Claude Scheduled Tasks*/*Managed Agents cron*, *Hermes Daily Briefing* (`0 8 * * *` sabah pano+kapsül → Telegram). *JARVIS:* **zaten başladı** (Faz 4 Routine, ilk koşum 16 Tem 09:00); proaktifliğin en güvenli ilk basamağı.
- **Heartbeat proaktif ajan** `Z3` — ucuz script sinyal toplar, pahalı model yalnız eşik aşılınca uyanır. **Örneğin:** *OpenClaw* (self-hosted kişisel-AI + yapılandırılabilir heartbeat + kalıcı bellek + 20+ kanal — JARVIS'in en yakın açık-kaynak ikizi). *JARVIS:* m.24 "hatırlatıcı Carvis'in kendisidir" mekanikleşir; heartbeat maliyet deseni. **Proaktif eylem = canlı-ajan → K-009/010 bloke;** şimdilik OpenClaw'u referans-sök (V25: kurma, ilham al).
- **Ambient "ne zaman konuşmalı" beyni** `Z2→Z3` — arka planda olay-güdümlü, yalnız değerli anda insanı çağır. **Örneğin:** *LangChain Ambient Agents + Agent Inbox* (**notify / question / review** üçlüsü). *JARVIS:* tüzükle birebir — notify=bildir, question=sor (soru-eşiği m.4), review=veto-öncesi göster (m.16/m.31). Asıl zor kısım "araya girmeye değer mi" yargısı; yanlış-kesinti güveni en hızlı yıkan risk.
- **Yüzey-bağımsız sesli kimlik** `Z1→Z2` — metin-Carvis ile sesli-Carvis tek kimlik; sabit "ses parmak-izi". **Örneğin:** tek sabit TTS voice + persona-drift ölçümü (Anthropic *Persona Selection Model*). *JARVIS:* tüzük/kimlik zaten güçlü temel; persona-drift belgelenmiş failure-mode. Ses-klonlama kimlik/rıza riski açar.
- **Sesli katman** `Z2–Z3` — realtime konuş/dinle. **Örneğin:** *Gemini Live* (realtime S2S, OpenAI'dan ~10-20× ucuz → always-on için tek makul native yol), *Pipecat*/*LiveKit Agents* (cascaded DIY, barge-in kontrolü), *Whisper+Piper+Ollama* (lokal/gizlilik, ~$0 marjinal), *openWakeWord* ("Hey Carvis"; false-accept ~<0.5/saat = günde birkaç yanlış-uyanma). *JARVIS:* V29 sesli-ufuk. **Uyarılar:** OpenAI Realtime ~$18/saat always-on'da yıkıcı; native S2S dil-kapsamı dar (Türkçe kalitesi [?]); ses buluta gider (gizlilik).
- **Sleep-time konsolidasyon ajanı** `Z2→Z3` — arka planda parçalı hafızaları birleştir, tekrarı temizle, eskiyeni arşivle ("ajanın rüya görmesi"). **Örneğin:** *Letta sleep-time agents*, *MemU*. *JARVIS:* vardiya-devri deseninin motoru; **tetiklemeli batch** (Carvis vardiya-sonu çağırır) olarak konumlanır — sürekli-daemon değil → K-009/010 yasağıyla çatışmaz.
- **Kesintiye-dayanıklı loop (durable execution)** `Z2→Z3` — uzun iş yarıda kesilse de tekrar-etmeden devam. **Örneğin:** *DBOS* (`@workflow`, durum Postgres'e), *Temporal* (ağır/olgun), ya da **git-commit'i checkpoint sayan kendi loop'un**. *JARVIS:* durum-kapsülü+git-log'un formel hali (m.9 zaten checkpoint felsefesi). Temporal tek-kişi için over-engineering → önce durable-*desenle* yaz, framework alma.
- **Ortam-yakalama / giyilebilir hafıza** `Z3→Z4` — hayat→hafıza→JARVIS beslemesi. **Örneğin:** *Screenpipe* (masaüstü ekran+ses 7/24 lokal kayıt, Whisper transkript, **MCP → Carvis doğrudan sorgular**), *Omi* ($89 açık-kaynak kolye). *JARVIS:* Screenpipe bugün MCP ile bağlanabilir; wiki/hafıza sinerjisi güçlü. **Ama gizlilik devasa** (başkalarını rızasız kaydeder) → m.23 yasakları + K-009 ile zorunlu çelişki-kapısı.

## G6 — Öz-Gelişen Çekirdek / AGI-Orkestra Şefi `Z4` (UFUK)
*Neden en son: Özyinelemeli öz-gelişim ancak ölçüm(G1)+hafıza(G2)+güvenlik(G4)+orkestrasyon(G3) üstünde güvenli/faydalı. Not: mekanizmalar Z2-Z3 olabilir ama HEPSİ alttaki katmanlara bağımlı olduğu için buraya asılı.*

- **Öz-yazılan skill kütüphanesi** `Z2→Z3` — her çözülen problem → adlı, yeniden-kullanılır skill olarak biriksin (retansiyon). **Örneğin:** *Voyager* (yürütülebilir-kod skill kütüphanesi), *Alita* (minimal-tanım + maksimal öz-evrim, MCP'leri kendi üretir). *JARVIS:* Claude Code zaten kod yazıyor; eksik = retansiyon → `skills/`e düşür. ATLAS'ın kendisi ilk örnek. Canlı-çalıştırma K-009/010'da bloke.
- **Reflektif prompt/kimlik-dosyası optimizasyonu** `Z2→Z3` — sistem-prompt'ları/agent-emirlerini gerçek koşum trace'lerinden otomatik iyileştir. **Örneğin:** *GEPA*/*DSPy 3.0* (hata-logunu okur, doğal-dil refleksiyonuyla Pareto-evrim; RL'i +~%20 ve 35× az rollout'la geçer, ~10-50 örnek yeter). *JARVIS:* cc/defter → CLAUDE.md revizyonu döngün = elle-GEPA; **öneri-modunda tut** (GEPA önerir, Salih onaylar — m.8/m.31). Az-örnek verimi tek-kişi ölçeğine ideal; küçük sette overfit riski.
- **Otomatik ajan-tasarım araması** `Z3→Z4` — agent-emri konfigürasyonlarını (model-kombosu, token×zaman) MCTS/successive-halving ile ara. **Örneğin:** *ADAS* (meta-ajan kod-uzayında ajan üretir/arşivler), *AFlow* (operatör-grafında MCTS + açık dolar-maliyeti), *Optuna* successive-halving. *JARVIS:* V39 "karar-noktası dizileri / sequence search"ün LİTERAL formel karşılığı; pahalı → yalnız olgunlaşmış iş-sınıfında.
- **Darwin-Gödel sınıfı öz-modifikasyon** `Z4` — kendi agent-tanımlarını ampirik-doğrulama + arşiv + rollback ile düzenle. **Örneğin:** *DGM* (kendi kodunu değiştirir, her değişikliği doğrular; SWE-bench %20→%50), *SEAL* (kendi finetuning verisini üretir), *Red Queen Gödel Machine* (ajan+değerlendirici koevrimi). *JARVIS:* #27 öz-gelişim döngüsünün kuzey-yıldızı; **git zaten arşiv+rollback sağlıyor** → dosya-seviyesi DGM; senaryo-defteri = koevrilen değerlendirici. Frontier, kararsız, güvenlik-kritik → G4 olmadan açılmaz.
- **Yeni yüzeyler / HUD ufku** `Z4` — görsel-HUD + her-an sesli erişim. **Örneğin:** *Meta Wearables Device Access Toolkit* (Ray-Ban Display, dev-preview 2026). *JARVIS:* en uzak-ufuk; üçüncü-taraf ses-erişimi henüz kapalı [?] → "izle" kategorisi.

---

## Çapraz-kesen uyarılar (hepsinden önce oku)
1. **Canlı-ajan kapısı her şeyi böler:** G3'ün çoğu + G5/G6'nın otonom parçaları **K-009/K-010 kararına** bağlı. Gerçek eşik teknik değil (primitifler native/hazır) — Salih'in otonomi kararı.
2. **Güvenlik otonomiden ÖNCE gelir (G4 < G5):** öz-editleyen + web-sindiren sistem, bağışıklamadan otonomlaştırılırsa zehirleme/injection açık. Sıra bozulamaz.
3. **Judge'a körlemesine güvenme:** 2026 saha bölünmüş — naif LLM-judge "yazı-tura" olabiliyor. G1 (judge-kalibrasyon) G6 (öz-gelişim) için ön-şart; kötü eval öz-gelişimi yanlış yöne hızlandırır.
4. **Maliyet gerçeği (token×zaman):** tek-ajan ~1× → orkestrasyon ~4× → multi-agent ~15× token; "kullanım performans varyansının %80'ini açıklıyor" ve multi-agent yalnız iş **bağımsız-paralel-şeritlere ayrışıyorsa** kazandırır. Sıralı işte tek-ajan+cascade daha ucuz.
5. **Ses maliyeti/dil:** always-on native ses için *Gemini Live* (OpenAI ~10-20× pahalı); *Moshi* lokal-S2S mid-2026 yalnız İngilizce → **Türkçe için gerçek blocker**; lokal cascaded (Whisper+Piper) Türkçe daha güvenli ama Piper TR kalitesi [?].
6. **JARVIS önden gidiyor:** dosya-tabanlı hafıza + "sil-değil-geçersiz-kıl" + katmanlı bağlam = 2026'nın en sıcak akımı; JARVIS'in mevcut mimarisi geriden değil **önden** — en yüksek ROI, yeni altyapı kurmak değil, **zaten yaptığını sahanın en-iyi-pratikleriyle isimlendirip indeksle/delta-disiplinle güçlendirmek** (G0 + G2 evolving-playbook).

## En düşük-risk/en yüksek-getiri ilk hamleler (koordinatör önerisi)
G0 dosya-indeks + ölçüm-substratı → G2 **evolving-playbook (ACE delta + helpful/harmful sayaç)** ve düşük-sürtünme mobil köprü → G1 mini eval-seti. Bu üçü Z0-Z2, birkaç günlük, mevcut mimariye turnkey oturuyor ve alttaki tüm bağımlılık zincirini açıyor.

---

## Yöntem & kaynak şerhi
- **Kaynak:** 4 paralel Atlas koşusu (2026-07-16), her biri son 6-12 ayı web-taradı; toplam ~230K subagent-token, ~88 araç-çağrısı.
- **Güven:** Framework/araç varlıkları (Mem0, Letta, Graphiti, Agent Teams, Beads, OpenClaw, GEPA, DGM, Pipecat, Gemini Live vb.) sağlam/gerçek. **Benchmark yüzdeleri ve yıldız/valuation sayıları büyük ölçüde satıcı/tek-kaynak beyanı `[?]` — yön gösterir, kanıt değil.** Bazı "claw"-markalı ve akıllı-gözlük iddiaları doğrulanamadı.
- **Doğrulanmışlar:** Claude Code Agent Teams (resmi doküman tam okundu), OTel-GenAI CNCF mezuniyeti, gecikme rakamları çapraz-teyitli.
- Bilgi-kesme Ocak 2026; Şubat–Temmuz bulguları web-taramaya dayanır. Bu bir 2026-07-16 anlık-görüntüsüdür; saha aylık hızda değişir — karar-anında ilgili repo/doküman tekrar okunur.
