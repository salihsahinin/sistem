# Atlas ANTİTEZ raporu — aile A (sektör öncülleri) — 2026-09-18

Yöntem: her iddianın ¬T'sini destekleyen birincil kaynak arandı. Bulunamazsa "ÇÜRÜTÜLEMEDİ" yazıldı (meşru sonuç). Yalnız web; ≥2 kaynak WebFetch ile gerçekten açıldı.

---

### 1. Opus 4 lider / Sonnet 4 işçi ayrımı — bağlam sıkıştırma + paralellik gerekçesi
**¬T kanıtı:** Bulunamadı. Anthropic'in kendi mühendislik yazısı gerekçeyi doğrudan doğruluyor: orkestratör-işçi deseni, "reasoning'i çoklu bağımsız context window'a yaymak" ve paralellik için kurulmuş; Opus 4 lider + Sonnet 4 işçi tek-ajan Opus 4'ü araştırma değerlendirmesinde %90.2 geçmiş.
**Kaynak:** anthropic.com/engineering/multi-agent-research-system (AS-OF: yayın ~2025-06, çekim 2026-09-18); kuşak: Opus 4 / Sonnet 4.
**Hüküm: ÇÜRÜTÜLEMEDİ**

### 2. Atıf ekleme (CitationAgent) ve LLM-judge değerlendirme, üretici ajandan ayrı
**¬T kanıtı:** Bulunamadı. Aynı birincil kaynak: "sistem araştırma döngüsünden çıkıp tüm bulguları CitationAgent'a aktarır" (üretimden sonraki ayrı adım) ve "LLM judge... rubric'e göre değerlendirdi" (üretici ajan dışı, ayrı değerlendirme).
**Kaynak:** anthropic.com/engineering/multi-agent-research-system, doğrudan alıntı: "passes all findings to a CitationAgent" · "We used an LLM judge that evaluated each output against criteria in a rubric" (AS-OF çekim 2026-09-18).
**Hüküm: ÇÜRÜTÜLEMEDİ**

### 3. Anthropic sıkı-bağımlı/paylaşılan-bağlam görevlerde (çoğu kodlama dahil) çok-ajanı uygun görmüyor
**¬T kanıtı (kısmi):** Anthropic'in kendisi 2026-02-05'te Agent Teams'i (Opus 4.6) yayınladı — birden çok Claude Code oturumu aynı kod tabanında paralel çalışıyor, "C compiler" mühendislik yazısında da doğrulandı. Ancak bu makale aynı zamanda claim'i DOLAYLI DOĞRULUYOR: ajanlar "minimal shared context" ile izole Docker konteynerlerinde, kilit dosyası mekanizmasıyla koordine oldu; gerçekten sıkı-bağımlı işte (Linux kernel'i tek görev olarak derleme) başarısız oldular — "Every agent would hit the same bug, fix that bug, and then overwrite each other's changes" — ve çözüm paylaşılan bağlamı ARTIRMAK değil, dış-oracle (GCC karşılaştırma) ile işi ayrıştırmaktı.
**Kaynak:** anthropic.com/engineering/building-c-compiler (AS-OF yayın 2026-02-05, çekim 2026-09-18, Opus 4.6); daily.dev/sitepoint Agent Teams haberleri (2026-02-06, Opus 4.6).
**Hüküm: DARALDI** — orijinal iddia (sıkı-bağımlı/paylaşılan-bağlam kodlamada uygunsuz) 2026-02 Opus 4.6 kuşağında ürün ölçeğinde teyit edildi: paralel çoklu-ajan kodlama ancak bağlam paylaşmayarak (izolasyon+kilit+dış-oracle) çalışıyor; paylaşılan-bağlam/sıkı-bağımlı senaryoda hâlâ başarısız.

### 4. Cognition, 2025 ortası paralel-yazan çoklu ajanı bağlam kirlenmesi + çelişen zımni kararlar gerekçesiyle toptan reddetti
**¬T kanıtı:** Bulunamadı. Cognition'ın kendi "Don't Build Multi-Agents" (2025-06-12) yazısı: "the tempting architecture of parallel sub-agents is inherently fragile, doomed by context isolation that leads to conflicting decisions and unusable results."
**Kaynak:** cognition.com/blog/dont-build-multi-agents (AS-OF yayın 2025-06-12, çekim 2026-09-18); GitHub paper_notes özeti aynı tarihi doğruluyor.
**Hüküm: ÇÜRÜTÜLEMEDİ**

### 5. Cognition 2025'te yalnız salt-okur alt-görevleri ayrı ajana verilebilir buldu, yazma yetkili paralel ajanları reddetti
**¬T kanıtı:** Kısmi — makale genel kural olarak "yalnız salt-okur" ifadesini birebir kullanmıyor; somut örnek Claude Code subtask'ları için: "the subtask agent is usually only tasked with answering a question, not writing any code." Bu genel ilke değil, tek örnek; iddia biraz geniş yorumlanmış olabilir ama makalenin gövde argümanı (paralel yazma yetkisi = çelişen kararlar riski) aynı yönde.
**Kaynak:** cognition.com/blog/dont-build-multi-agents (aynı, çekim 2026-09-18).
**Hüküm: DARALDI** — örnek doğrulanıyor, ama "genel kural" formülasyonu makalede birebir yok; tek örnekten genellenmiş.

### 6. Cognition 2026 ortasında pozisyonunu kısmen geri aldı; Code-Review-Loop deseni
**¬T kanıtı:** Bulunamadı, tersine doğrudan doğrulanıyor. Cognition'ın "Multi-Agents: What's Actually Working" yazısı reversal'ı kendisi açıklıyor: "map-reduce-and-manage" deseni + review-loop.
**Kaynak:** cognition.com/blog/multi-agents-working (AS-OF çekim 2026-09-18; yayın tarihi makalede açık değil ama "10 ay sonra" referansı 2025-06'dan ~2026 başına işaret ediyor — AS-OF belirsiz, [?] işaretlenir).
**Hüküm: ÇÜRÜTÜLEMEDİ** (yayın tarihi kesinliği düşük — kestirim [?])

### 7. Code-Review-Loop: incelemeci yazanla bağlam paylaşmıyor, ~2 hata/PR, %58 şiddetli
**¬T kanıtı:** Bulunamadı; birebir doğrulandı. "we found this technique to work best when the coding and review agents do not share any context beforehand" ve "Devin Review catches an average of 2 bugs per PR, of which roughly 58% are severe (logic errors, missing edge cases, security vulnerabilities)."
**Kaynak:** cognition.com/blog/multi-agents-working (çekim 2026-09-18).
**Hüküm: ÇÜRÜTÜLEMEDİ**

### 8. Cognition 2026: model kademelemesi sabit hiyerarşi değil, küçük modelin kendi kararıyla eskalasyon istediği düzen ("Smart Friend")
**¬T kanıtı:** Bulunamadı; birebir doğrulandı: "let the primary/smaller model decide when a situation was tricky enough to be worth consulting the smarter/expensive model" — makale bunu zorluk olarak da çerçeveliyor ("the model deciding when to delegate isn't the smarter one"), yani mekanizma kusursuz sunulmuyor, ama tanım iddiayla örtüşüyor.
**Kaynak:** cognition.com/blog/multi-agents-working (çekim 2026-09-18).
**Hüküm: ÇÜRÜTÜLEMEDİ**
Karşıt-kamp arayışı (sabit hiyerarşik kademelemeyi savunanlar): arama sonuçlarında (dev.to "Default-to-Flagship Is Now a Cost Bug", ArXiv "Cluster, Route, Escalate") ağırlıklı olarak dinamik/kural-tabanlı routing savunuluyor; saf sabit-hiyerarşi savunan güçlü bir birincil kaynak bulunamadı — bu da 8'i dolaylı destekliyor.

### 9. Claude Agent SDK: alt-ajan varsayılan hafızasız + ebeveyn bağlamından izole; yalnız son mesaj döner
**¬T kanıtı:** Bulunamadı; birebir doğrulandı, resmî dokümantasyondan: "its context window starts fresh, with no parent conversation" ve "only its final message returns to the parent." Not: SDK'de `memory: 'user'|'project'|'local'` alanı var ama bu ayar-tabanlı hafıza kaynağıdır, ebeveynin konuşma geçmişini paylaşmaz — izolasyon iddiasını çürütmüyor, daraltmıyor bile.
**Kaynak:** code.claude.com/docs/en/agent-sdk/subagents (çekim 2026-09-18; sürüm notu: TS SDK v0.3.219+/Python v0.2.127+ ve Claude Code v2.1.219+ referans alınıyor).
**Hüküm: ÇÜRÜTÜLEMEDİ**

### 10. Claude Agent SDK'de alt-ajan başına model seçimi ve araç kısıtlaması birinci sınıf alanlar
**¬T kanıtı:** Bulunamadı; birebir doğrulandı — `AgentDefinition` tablosunda `tools`, `model`, `effort`, `disallowedTools` doğrudan alanlar; "Tool restrictions" ve model override ayrı bölümlerde belgelenmiş.
**Kaynak:** code.claude.com/docs/en/agent-sdk/subagents (aynı, çekim 2026-09-18).
**Hüküm: ÇÜRÜTÜLEMEDİ**

### 11. Opus 5'in alt-ajan çağırma eğilimi yüksek → ürün düzeyinde derinlik/eşzamanlılık/harcama sınırları eklendi
**¬T kanıtı:** Bulunamadı; birincil kaynaktan birebir doğrulandı: "Claude Opus 5 delegates to subagents more readily than earlier models, so the depth, concurrency, and spend limits matter most on queries that run Opus 5" + `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (varsayılan 3) + `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (varsayılan 20) + `max_budget_usd`.
**Kaynak:** code.claude.com/docs/en/agent-sdk/subagents, bölüm "Run Opus 5 with subagents" (çekim 2026-09-18; TS SDK v0.3.219+/Claude Code v2.1.219+).
**Hüküm: ÇÜRÜTÜLEMEDİ**

### 12. Cursor Plan Mode planlamayı icradan ayırır, blog gerekçeyi açıkça belirtmiyor, yalnız sonuç iyileşmesini bildiriyor
**¬T kanıtı:** Bulunamadı; birebir doğrulandı. Resmî blogun en yakın ifadesi: "We've seen this significantly improve the code generated" — nedensellik mekanizması açıklanmıyor, yalnız gözlemlenen sonuç bildiriliyor.
**Kaynak:** cursor.com/blog/plan-mode (çekim 2026-09-18, AS-OF yayın tarihi sayfada açık değil — [?]).
**Hüküm: ÇÜRÜTÜLEMEDİ**

---

## Ek not — çürütülemedi kümesinin niteliği
Aile A iddialarının büyük çoğunluğu (1,2,4,6,7,8,9,10,11,12) doğrudan birincil kaynaklarla (Anthropic/Cognition/Claude SDK resmî dokümanları) birebir örtüşüyor; bunlar için anlamlı bir ¬T bulunamadı — bu, iddiaların iyi çıpalandığını gösterir, antitez ajanının başarısızlığı değil. Tek gerçek DARALMA 3 numarada: Anthropic'in kendisi 2026-02'de (Opus 4.6, Agent Teams / C-compiler) paralel çoklu-ajan kodlamayı ürün ölçeğinde başarıyla kullandı — ama bunu paylaşılan-bağlamı ARTIRARAK değil, izolasyon+kilit+dış-oracle ile sıkı-bağımlılığı BYPASS ederek yaptı; yani orijinal iddianın özü (sıkı-bağımlı/paylaşılan-bağlamda çok-ajan zayıf) 2026 kuşağında da geçerli kaldı, sadece "kodlamanın çoğu" ifadesi ölçek örnekleriyle daraltılabilir.
