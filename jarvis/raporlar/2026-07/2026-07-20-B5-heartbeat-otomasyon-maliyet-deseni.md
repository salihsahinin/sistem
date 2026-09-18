# B5 — Heartbeat / Otomasyon Maliyet Deseni — Atlas Raporu (2026-07-20)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ, karar ALINMADI) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: **5** (heartbeat-nedir · maliyet-deseni · güvenilirlik/sağlık · JARVIS-uyum/K-009 · ünlü-isimler) → 10 literatür/pratisyen şeridi + 1 heartbeat/otomasyon karar envanteri.
> **Salih notu:** "Heartbeat/otomasyon maliyet deseni ne olduğu bana tekrar açıklanmalı" — §0 kutusunda ve §1 Aile A'da SADE açıklama var.
> **Kanıt kısıtı (dürüstlük):** `code.claude.com/docs` + prompt-caching docs + gece-senkron.ps1 (yerel) doğrudan **[D]**; GitHub emsalleri (#68110 vb.) B1'de birincil-doğrulandı **[D]**; OpenClaw heartbeat issue'ları + arXiv 2603.23064 egress-403/gh-yok → **[K], güven ORTA** (issue-gövdeleri doğrulanamadı, "OpenClaw" anonimleştirilmiş adlandırma olabilir).
> **Okuma sırası (Fable):** §0 Carvis sentezi (+ "nedir" kutusu) + §4 dürüst bayraklar → yeterli. Detay: §1 aile bulguları · §2 ünlü isimler · §3 heartbeat-kararlarımızın kategori+kontrolü · §5 V26 · §6 açık sorular.

---

## §0 — Carvis sentezi (önce oku)

**"NEDİR" (Salih için sade tanım):** **Heartbeat** = bir sistemin/ajanın belli aralıkla kendini uyandırıp "hâlâ buradayım, iş var mı?" diyen küçük periyodik canlılık döngüsü (dağıtık-sistem kökeni: düğümün izleyiciye attığı "hayattayım" sinyali / keep-alive). Üç varyant: **scheduled/cron** (zaman-tetikli), **polling** (periyodik "değişti mi?" yokla), **event-driven** (olay anında tetik). **Otomasyon maliyet deseni** = her tick bir prompt faturasıdır: `maliyet = frekans × (sabit-önek + oynak-veri) × cache-durumu`; TTL-içi önek cache-hit (~0.1×), TTL-dışı cache-miss (tam fiyat + yazma zammı). JARVIS bağı: gecelik-senkron = scheduled heartbeat; uyucam/günaydın = event-driven (Salih beyanı=olay).

**En sağlam kesişim (beş ailenin İKİ şeridinin de + envanterin ortak dediği):**

1. **TANIMLAYICI AYRIM: ucuz LLM'siz health-check/event-tetik ↔ pahalı LLM-per-tick iş-döngüsü.** "Heartbeat" tek kelime iki maliyet-sınıfını kapsıyor (E-tez/E-antitez): klasik altyapı-heartbeat'i (Kubernetes/ZooKeeper) neredeyse bedava/LLM'siz; LLM-ajan "heartbeat"i tam bir muhakeme-turu = pahalı token. **Sağlıklı desen döngü değil, bu AYRIMdır.** JARVIS tasarımı tam güvenli tarafta (A-tez kademe K1→K2; D-tez: gece-senkron.ps1 = LLM'siz tick, $0). [D/K]

2. **LLM-per-tick self-wake bir maliyet-VE-güvenilirlik TUZAĞI.** Maliyet: her tick tam-fiyat (B-antitez #68110/48+ajan, gecede $6000, cache-miss); **5-dk TTL seyrek-heartbeat caching'ini gecelik kadansta TÜMDEN öldürür** (gece-arası TTL ölür → caching İŞE YARAMAZ, B-tez). Güvenilirlik: sessiz-ölüm (compaction-hiç-tetiklenmez #60719, sonsuz-retry #92082), MİMARİ memory-poisoning (arXiv 2603.23064: %91 kalıcı-zehir, C-antitez), liveness≠progress (sağlık-kontrolü semantik-sessiz kusurları kaçırır). HER pratisyen çitliyor (E-tez: MemGPT default-DUR, OpenAI saatlik-kota, LangChain "sil yoksa öde", Karpathy verifier-first) — kimse sınırsız heartbeat sunmuyor → **m.30/K-009 blokajını sektörle HİZALAR.** [K]

3. **JARVIS tüm bu hata-sınıfını YAPISAL atlıyor ve zaten güvenli tarafta.** Heartbeat-döngüsü değil, **vardiya-başı kapsül(üzerine-yaz) + git-log(karar-başına commit)** → compaction-boşluğu tuzağı YOK, çünkü kalıcılık compaction'a değil açık-commit'e bağlı (C-antitez köprüsü). Gece-senkron A+C aşısı = LLM'siz ff-only script (tick=$0, C-aşısı idempotent safe-fail) = "no-agent mode"/wakeAgent-kapısı best-practice'inin birebiri (B-tez/D-tez). Üç kanonik otomasyon-kontrolü (ucuz-deterministik-kapı + idempotent-safe-fail + bütçe-devre-kesici) ≈ K-009'un üç sigortası (ff-only-script + C-aşısı + curfew). [D]

4. **liveness ≠ progress — ve bu oturumun 8-saat-stall'ı kanonik kanıt, üstelik KANONA İŞLENMEMİŞ.** mtime-taze (aldatıcı-canlılık) + byte-sabit (gerçek ilerleme-metriği) = ders kitabı (C-tez/A-antitez). "Byte-değişmedi" gözlemi ZATEN doğru watchdog-sezgisi, sadece otomatikleşmemiş. Doğru düzeltme = progress-watchdog (usage-JSONL byte/satır büyüme-yoklaması, LLM'siz, salt-okunur, dış-gözlemci), alive-heartbeat DEĞİL. **Envanter buldu: stall senaryo-defterinde/kanonda YOK — yalnız 07-20 yan-oturum raporlarında (kanon yazamaz, m.41).** [D-envanter]

5. **Tek meşru heartbeat formu = LLM'siz watchdog/kill-primitifi (stall'ı ÖLDÜRMEK için), üretken self-wake (KOŞMAK için) ASLA.** Bu tam da JARVIS'in çizdiği tetik-devri + guardrail çizgisi (D-antitez). Gelecekte zaman-duyarlı görev doğsa bile → LLM'siz zamanlayıcı bir OLAY üretir, olay bilinen-promptla tek-atış koşumu tetikler (kimlik insanda); periyodik LLM self-wake gereksiz kalır. [D/K]

**JARVIS'e ne demek (gözlem, KARAR DEĞİL — m.41):**

- **Dürüst manşet:** B5, JARVIS'in otomasyon tasarımının doğru, sektörle-hizalı güvenli tarafta olduğunu DOĞRULUYOR — gece-senkron A+C aşısı (LLM'siz ff-only + idempotent safe-fail) ders-kitabı ucuz-heartbeat'i, m.30/K-009 canlı-ajan blokajı her ciddi pratisyenin sınırsız-self-wake'i çitlemesiyle eşleşiyor. Net-yeni: (a) ucuz/pahalı kategori-ayrımı açıkça; (b) caching gecelik kadansta İŞE YARAMAZ (TTL gece-arası ölür) — tek gecelik-kaldıraç JARVIS'in zaten sahip olduğu LLM'siz script; (c) liveness≠progress + somut progress-watchdog tasarımı (usage-JSONL büyüme-yoklaması); (d) 8-saat-stall İŞLENMEMİŞ — bir K-019 vakası.
- **En yüksek-kaldıraçlı üç gözlem (harita, öneri değil):** (1) otomasyonu tick-düzeyinde LLM'SİZ tut (JARVIS zaten öyle) — asla LLM-per-tick self-wake; (2) B1'in işaretlediği eksik guardrail'ler (istek-yolu kill-switch + `max_budget_usd` sert-cap) gelecekteki LLM-otomasyonu için gerçek boşluk — heartbeat'in kendisi değil; (3) bir progress-watchdog ekle (usage-JSONL byte/satır büyüme, dış LLM'siz gözlemci) ki sonraki 8-saat-stall YAKALANSIN, gizlenmesin — salt-okunur/liveness olduğu için K-009/K-010 bloke sınırını ihlal etmez.
- **8-saat-stall muhtemelen senaryo-defterine bir K-019 vakası (liveness-arızası) olarak işlenmeli** — ama bu Katman-1/kanon yazımıdır; soru olarak işaretlendi, yapılmadı (m.41). D-tez'in iki ince-ayarı (sağlayıcı-seviyesi harcama-cap + günaydın-vardiya cache-prefix disiplini) yapısal-eksik değil.

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile A — Heartbeat nedir
- **Tez:** (Tanım §0.) Klasik köken (dağıtık-sistem failure-detection); ajan-bağlamı = scheduled self-wake; üç varyant; JARVIS 4-kademe (K0 pasif → K1 event-hooked → K2 scheduled → K3 polling); tatlı-nokta K1(bugün)→K2(blok kalkınca); K3 yelpaze-dışı. [D/K]
- **Antitez (¬):** Heartbeat UCUZ LLM'siz sinyal; LLM-self-wake turuna eşitlemek kategori-hatası; polling ampirik israf (%95 boş); **KRİTİK: canlılık ≠ ilerleme** (donuk-düğüm ping'e cevap verir; 8-saat-stall = mtime-taze/byte-sabit); klasik failover-faydası tek-vardiyada karşılıksız; doğru soyutlama = watchdog(ilerleme) + event-driven. [D/K]
- **Kesişim:** Heartbeat GERÇEK+iyi-tanımlı desen AMA (i) yalnız LLM'SİZ iken ucuz, (ii) alive-sinyali ≠ progress (watchdog byte/çıktı izlemeli, mtime değil), (iii) failover-makinesi tek-vardiyada yok → savunulabilir JARVIS formu: event-driven insan-kanca + LLM'siz scheduled script + progress-watchdog; tuzak = LLM-per-tick self-wake.

### Aile B — Maliyet deseni
- **Tez:** Maliyet = frekans × (sabit-önek+oynak) × cache-durumu; Anthropic caching 0.1× oku / 1.25× yaz(5dk) / 2× yaz(1sa); en güçlü kaldıraç = **LLM'siz ön-filtre/wakeAgent-kapısı** ($0 tick). **KRİTİK: gecelik kadansta caching İŞE YARAMAZ** (gece-arası TTL ölür); tek gerçek kaldıraç = LLM'siz ff-only script (JARVIS'te zaten var). /usage ile ölç. [D/K]
- **Antitez (¬):** Her tick tam-bedel (boşta bile); kaçak belgeli (#68110, gecede $6000, 5dk'da 4M token); **prompt-cache TTL sessizce 1sa→5dk düştü → seyrek heartbeat hep cache-MISS**; subagent parent-cache miras almaz (soğuk); fatura ~24sa gecikmeli; ortak abonelik-kovası → heartbeat haftalık-tavanı yer, interaktifi kısar; "cache-warmer" = ekstra idle-maliyeti. [D/K]
- **Kesişim:** Maliyet ÖNGÖRÜLEBİLİR/kısılabilir (formül+kaldıraçlar) AMA LLM-per-tick kaçak-eğilimli; gecelik kadansta caching ölü → tek kaldıraç LLM'siz script; **JARVIS'in A+C aşısı tam da tuzağı (LLM-per-tick) atlıyor** (tick=$0).

### Aile C — Güvenilirlik / sağlık
- **Tez (koşullu):** Heartbeat'in değeri PULS değil İLERLEME ölçmesinden; watchdog altın-kuralı (yalnız gerçek-ilerlemede besle); dead-man's switch; heartbeat KONUMU (döngü-içi, iş-sonrası, ilerleme durunca susar); timestamp/exec-probe (byte/içerik-delta). JARVIS: 8-saat-stall = liveness≠progress vakası; usage-JSONL büyüme-yoklaması = doğru-tasarlanmış progress-based dead-man's switch. [D/K]
- **Antitez (¬):** Sessiz-ölüm belgeli (#60719 compaction-hiç, #92082 sonsuz-retry); MİMARİ memory-poisoning (2603.23064: %91 kalıcı/%76 oturum-arası); uzun-ömürlü ajan öz-izlemeden yoksun (#57577 boş-özet → tool-call atlamayı öğrenir); **sağlık-kontrolü semantik-sessiz kusurları KAÇIRIR** ("no dashboard catches"); cascade (ASI08). Azaltıcılar var → ¬T "naif-varsayılan"a daralır; güven ORTA. [K]
- **Kesişim:** Sağlık-izleme yalnız İLERLEME-ölçerse değer üretir, puls-ölçerse zarar; ama semantik-sessiz kusurlar (makul-ama-yanlış) hiçbir progress-watchdog'u tetiklemez → tam güvence yok. **JARVIS yapısal atlıyor** (heartbeat-loop değil, vardiya+açık-commit); doğru pratik ders = uzun-ömürlü-döngü yerine kısa-vardiya + açık-checkpoint (JARVIS'in zaten yaptığı).

### Aile D — JARVIS-uyum (K-009)
- **Tez:** Üç kanonik otomasyon-kontrolü = K-009'un üç sigortası — (1) ucuz deterministik kapı = LLM'siz ff-only script (`model:none, tokens:0`, doğrulandı); (2) idempotent safe-fail = C-aşısı "dokunma" (fail'de SENKRON-UYARI.md); (3) bütçe devre-kesici = curfew/tur-tavanı. Desen K-009'a doğal oturuyor; yapısal-eksik değil, iki ince-ayar (provider-cap + günaydın cache-prefix). [D/K]
- **Antitez (¬):** LLM-heartbeat = B1'in "gözetimsiz-loop" bulgusunun adı-değişmişi (B1 zaten "erken" dedi); periyodik self-update = memory-poisoning katalizörü; **JARVIS'in doğru yolu ZATEN LLM'siz → LLM-heartbeat eklemek net regresyon**; uyucam/günaydın event-driven (polling değil); m.30 sınırı devredilmedi (heartbeat-self-wake K-010 üçlüsüne yakın); 8-saat-stall = liveness-yanılsaması kanıtı; frenler henüz yapısal-dişli değil; m.5 tersinden = sorun yok, çözüm-arayan-yetenek var. [D/K]
- **Kesişim:** İki şerit HEMFİKİR — JARVIS'in mevcut tasarımı (LLM'siz gece-senkron + event-driven kanca + curfew) DOĞRU ve güvenli. LLM-per-tick heartbeat EKLEMEK erken+gereksiz+regresyon; tek meşru genişletme = LLM'siz progress-watchdog (ÖLDÜRMEK için, koşmak için değil) + B1'in eksik guardrail'leri.

### Aile E — Ünlü isimler / pratisyen
- **Tez:** SWIM (Das/Gupta, "suspected" ara-durumu = m.33 analoğu); Kubernetes probes; **MemGPT/Letta (Packer, `request_heartbeat` varsayılan-FALSE = default-DUR)**; Anthropic Routines/Managed-Agents (her fire=yeni session=temiz-bağlam+yeni maliyet); OpenAI Scheduled (saatte-1, kotalı); Karpathy "otonomi kaydırağı, verifier-first". [D/K]
- **Antitez (¬):** event-driven > polling (order-of-magnitude ucuz); MemGPT bilerek default-kapalı (runaway-token); Cognition "gözetimsiz loop = gözetimsiz hata"; Anthropic "gözetimi koru EVET, her-aksiyonu-onayla HAYIR"; heartbeat'in MEŞRU yeri = ucuz altyapı-liveness'i, pahalı LLM-turu DEĞİL. [K]
- **Kesişim:** E-tez ve E-antitez YAKINSIYOR — **HER isim deseni maliyet-freniyle sunuyor** (SWIM suspected, MemGPT default-dur, OpenAI kota, LangChain "sil-yoksa-öde", Karpathy verifier-first); kimse sınırsız heartbeat önermiyor → JARVIS'in m.30/K-009 blokajını sektörle HİZALAR, çürütmez.

---

## §2 — Ünlü isimler / kaynak tablosu

| İsim | Yöntem | Özü | JARVIS bağı | Kaynak | Etiket |
|---|---|---|---|---|---|
| Das/Gupta/Motivala | SWIM protokolü | "Outsourced heartbeat" + "suspected" ara-durum | "Sessizlik=başarısızlık değil" = m.33 | [SWIM PDF](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf) | [D]/[K] |
| Kubernetes / CNCF | liveness/readiness probe | Başarısız probe → öldür+restart | Polling neden ucuz değil; m.30 blok gerekçesi | [kubernetes.io/probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/) | [D] |
| Packer (MemGPT/Letta) | Cognitive-arch heartbeat | `request_heartbeat` varsayılan-FALSE = default-DUR | m.24 + m.41 "kanon kilitlemez" felsefe-hizası | [docs.letta.com/heartbeats](https://docs.letta.com/guides/agents/heartbeats) [X] | [K] |
| Anthropic | Routines / Managed Agents | Bulut cron; her fire=yeni session=yeni maliyet | K-009 send_later/Routine; vardiya metaforu | [claude.com/blog/routines](https://claude.com/blog/introducing-routines-in-claude-code) | [K] |
| OpenAI | Scheduled Tasks | Saatte-1, 3-15 aktif = kotalı | Sınırsız heartbeat kimse sunmuyor | [help.openai.com](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt) | [K] |
| LangChain | LangSmith cron | "Gereksiz cron'u SİL yoksa öde" | Otomasyon-maliyet deseni pratisyen itirafı | [docs.langchain.com/cron](https://docs.langchain.com/langsmith/cron-jobs) | [K] |
| Karpathy | Otonomi kaydırağı | verifier-first; otonomiyi doğrulayıcıyla hak et | m.31/m.41/m.9 kurumsal karşılığı | [latent.space/p/s3](https://www.latent.space/p/s3) | [K] |
| Cognition | Don't leave unattended | Gözetimsiz loop = gözetimsiz hata | m.30 canlı-ajan ihtiyatı | [cognition.ai](https://cognition.ai/blog/closing-the-agent-loop-devin-autofixes-review-comments) | [K] |
| "Mind Your HEARTBEAT!" | Memory-poisoning | Background-exec paylaşılan-session → %91 kalıcı-zehir | Heartbeat-self-loop ihtiyatının akademik zemini | [arXiv 2603.23064](https://arxiv.org/abs/2603.23064) [X] | [K] |

---

## §3 — Heartbeat/otomasyon kararlarımızın kategori + kontrolü

| Karar/kimlik | Heartbeat-deseni | Statü | Kontrol (bu araştırmanın verdiği) |
|---|---|---|---|
| **gece-senkron.ps1 (A+C aşısı)** | LLM'siz-health-check + scheduled | KURULDU 07-19 | ✅ **Ders-kitabı ucuz-heartbeat** (model:none/tokens:0, ff-only, C-aşısı idempotent safe-fail); wakeAgent-kapısı best-practice'inin birebiri. |
| **m.24 hatırlatıcı = Carvis** | event-driven vs scheduled ayrımı | imzalı kanon | ✅ "Hatırlatıcı Carvis'in kendisi" = sürekli-polling yerine olay/zaman-tetik kanonda. |
| **m.27 uyku/günaydın vizyonu** | event-driven (söz-tetikli) | vizyon kaydı | ✅ Söz-tetikli (Salih beyanı=olay), saat değil → polling değil, event-driven. |
| **uyucam/günaydın kancaları** | event-driven | K-009 | ✅ Event-driven; SessionStart hook (Dilim 1.2) da öyle (oturum-açılış tetikli). |
| **m.30 ek (canlı-ajan sınırı)** | curfew-guardrail + sınıflandırma | imzalı kanon | ✅ Sınırsız-self-wake'i çitliyor = her pratisyenle hizalı; heartbeat-self-wake K-010 tarafı. |
| **PreToolUse kilidi (Dilim 1.1)** | curfew-guardrail (LLM'siz) | KURULDU+TEST PASS | ✅ Deterministik policy-as-code; C-antitez'in "deterministik-önce" ile hizalı. |
| **usage-JSONL asgarisi (Dilim 1.4)** | observability/liveness | AÇILDI 07-19 | ✅ Progress-watchdog için hazır sinyal (byte/satır büyüme); ⚠️ watchdog henüz yok. |
| **Gece-araştırma freni (Dilim 4.1)** | curfew-guardrail (bütçe+tur) | tetikli/bekleyen | ⚠️ Doğru yön; sayılar sezgisel; istek-yolu kill-switch + max_budget_usd EKSİK (B1). |
| **Faz-4 tek-atış Routine** | scheduled-batch (bulut) | KAPANDI (run_once_fired) | ✅ Tek-atış + duraklat = güvenli desen; ⚠️ bulut-Routine token-kolonu yapısal boş (liveness zaafı). |
| **V34 skill-avcısı** | scheduled-batch (periyodik) | ham fikir (K-009 tetikli) | ⚠️ "haftada 1" sezgisel; periyodik-Routine sınıfı → maliyet/liveness kuralı gerekir. |
| **V31 tahmin ajanı** | polling-self-wake benzeri | ADAY (tetikli) | ⚠️ ~10-görev ön-şart; self-wake tarafı → m.30 sınırına dikkat. |

**Özel vurgular (envanterden):** (1) gece-senkron TAMAMEN LLM'siz (`git pull --ff-only`, fail'de dokunma-yok, schtasks DAILY 06:00); (2) uyucam/günaydın **event-driven** (söz-tetik), script **scheduled** (saat-tetik) — iki ayrı katman; (3) curfew: PreToolUse KURULU + Dilim-4.1 tetikli, AMA istek-yolu-kill-switch + max_budget_usd EKSİK; (4) usage-JSONL sinyali var ama progress-watchdog inşa edilmemiş; (5) **8-saat-stall senaryo-defterine/kanona İŞLENMEMİŞ** (yalnız 07-20 yan-oturum raporlarında).

---

## §4 — Yanlış/zayıf gördüklerim (dürüst bayraklar — KARAR ALMADAN, m.41)

1. **8-saat-stall KANONA/DEFTERE İŞLENMEMİŞ.** Bu oturumdaki gerçek bir liveness-arızası (6 ajan 8 saat donuk) yalnız 07-20 yan-oturum raporlarında (B1/B2/A2) öz-referanslı geçiyor — senaryo-defterindeki stage-bayat vakaları (K-019 #1/#2/#3) FARKLI olaylar. Karar-kaydı dışında kalmış bir arıza; muhtemelen K-019 vakası olmalı ama bu Katman-1 yazımı — işaretlendi, yapılmadı.
2. **Caching gecelik kadansta İŞE YARAMAZ.** "Kararlı-prefix" cost-lever yalnız oturum-içi tekrar-koşumlarda; gecelik tek-tick'te 5-dk ve 1-sa TTL'lerin ikisi de gece-arası ölür → her gece cache-miss. Tek gecelik-kaldıraç = LLM'siz script (zaten var). Caching'e otomasyon için değer atfetme.
3. **"Heartbeat" kategori-kapsayan kelime** (ucuz-LLM'siz ↔ pahalı-LLM-turu); B5'in maliyet-endişesi aslında LLM-per-tick varyantı hakkında. JARVIS tasarımı onu zaten atlıyor → kaçak (#68110/$6000) GELECEKTEKİ LLM-otomasyonu için risk, bugünkü LLM'siz script için değil.
4. **Eksik guardrail'ler (B1-taşınan):** istek-yolu kill-switch + `max_budget_usd` sert-cap yok; loop-guardrail (3tur/10dk) dış-kaynaklı/kalibresiz; Routines per-tier kota DOĞRULANMADI. Bunlar GELECEKTEKİ LLM-otomasyonunu kapılar, bugünkü scripti değil.
5. **Epistemik (m.39):** OpenClaw/heartbeat bulguları (C-antitez, B1'de de) [K]/**ORTA-güven** — issue-gövdeleri doğrulanamadı, "OpenClaw" anonimleştirilmiş/paralel-evren adlandırma olabilir; arXiv 2603.23064 sayıları (%91/%76) arama-özeti. YÖN (heartbeat sessiz-arıza) iyi-desteklenir; SPESİFİK sayılar/issue'lar orta-güven. Laundering YOK.
6. **Öz-referans:** B5 (tüm B-serisi gibi) 11 çift-atlas ajanı koştu; ve B5'in KENDİ konusu (otomasyon-maliyet + liveness) bu oturumun 8-saat-stall'ı + çift-atlas ×2 maliyetiyle örneklenendir.
7. **Progress-watchdog önerisi benim (gözlem)** — doğru sinyal (usage-JSONL büyüme) var ama watchdog inşa edilmemiş; ve watchdog PROGRESS (byte/içerik-delta) izlemeli, liveness (mtime) değil — yoksa stall'ın aldatmasını tekrarlar.

---

## §5 — V26 örneklem-denetimi

| Ajan/şerit | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| C-antitez/B1 | "OpenClaw #60719/#92082 heartbeat sessiz-ölüm" | **[K], ORTA güven** — issue-gövde doğrulanamadı, adlandırma anonim olabilir | §4-5'e taşındı; YÖN destekli, SPESİFİK sayı ihtiyatlı |
| C-antitez | "Mind Your HEARTBEAT %91/%76" | **Arama-özeti [K]** — arXiv 403 | Direksiyon-argümanı; sayı öne çıkarılmadı |
| B-tez | "prompt-cache TTL 5dk, gecelik caching ölü" | **Docs-DOĞRULANDI [D]** | "Tek gecelik-kaldıraç LLM'siz script" çekirdeği |
| D-tez | "gece-senkron.ps1 model:none/tokens:0/ff-only" | **Dosya-DOĞRULANDI [D]** | K-009 "doğru sigortalar" tezinin çekirdeği |
| Envanter | "8-saat-stall senaryo-defterinde YOK" | **Kanon-DOĞRULANDI [D]** — 0 eşleşme | §4-1 açık K-019 vakası |
| E-tez | "MemGPT `request_heartbeat` varsayılan-FALSE" | **Çok-kaynak [K]** | "Kimse default-continue heartbeat sunmuyor" |
| B1-taşınan | "Routines per-tier kota Pro5/Max15/Ent25" | **DOĞRULANMADI [X]** | Karar dayanağı yapılmadı |

---

## §6 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **8-saat-stall senaryo-defterine bir K-019 liveness-arıza vakası olarak işlensin mi?** — gerçek bir arıza karar-kaydı dışında; ama bu Katman-1/kanon yazımı (Salih).
2. **Progress-watchdog (usage-JSONL byte/satır büyüme-yoklaması, dış LLM'siz gözlemci) kurulsun mu?** — salt-okunur/liveness olduğu için K-009/K-010 bloke sınırını ihlal etmez; sonraki stall'ı YAKALAR. mtime değil byte izlemeli.
3. **B1'in eksik guardrail'leri (istek-yolu kill-switch + max_budget_usd sert-cap) gelecekteki LLM-otomasyonundan ÖNCE mi kurulsun?** — bugünkü LLM'siz script bunları gerektirmiyor; ama m.30 "ilk gözetimsiz dilimden önce" der.
4. **D-tez'in iki ince-ayarı (sağlayıcı-seviyesi harcama-cap + günaydın-vardiya cache-prefix disiplini) uygulanmalı mı?** — yapısal-eksik değil; günaydın-vardiya LLM'in uyandığı tek yer olduğundan cache-prefix orada değer verir.
5. **Gelecekte zaman-duyarlı proaktif görev doğarsa (m.27 vizyonu) — LLM'siz-zamanlayıcı→olay→tek-atış-koşum deseni mi, yoksa periyodik-self-wake mi?** — tüm kanıt ilkini işaret ediyor; periyodik LLM self-wake gereksiz kalıyor.

---

*Bu rapor B5 kartının çıktısıdır (m.41 yan-oturum): 5 aile × 2 şerit + 1 envanter = 11 Atlas koşumu, çift-atlas (tez ∧ ¬tez). Karar ALINMADI, kanon DEĞİŞMEDİ; yalnız bulgu + "nedir" açıklaması + kategori/kontrol + dürüst bayraklar sunuldu. Ana bulgu: sağlıklı desen döngü değil, ucuz-LLM'siz ↔ pahalı-LLM-turu AYRIMI; JARVIS'in gece-senkron A+C aşısı zaten güvenli tarafta; en yüksek-kaldıraçlı boşluk = progress-watchdog (usage-JSONL büyüme) + B1'in eksik guardrail'leri; ve bu oturumun 8-saat-stall'ı defter-dışı bir liveness-vakası. **Bu, "sırayla A2'den gir" kuyruğunun SON raporudur (A2·A4·B1·B2·B3·B4·B5 tamam).***
