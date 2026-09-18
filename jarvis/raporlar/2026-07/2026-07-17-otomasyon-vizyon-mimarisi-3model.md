# Otomasyon Vizyonu — Mimari Araştırması + 3 Matematik-Temelli Model (Devir Raporu)

> **Tek satır:** Salih'in "sesle + telefondan senkron geliştirme" nihai-hedefi için dış-tarama (Atlas 4 şerit) + m.37 3-model sunumu (karşıt-temel dahil). **Bu bir YAN-OTURUM devir dosyasıdır (m.41): kanon KİLİTLENMEDİ; öneri işaretli, seçim K-009 açılışında Salih'te.**
> **Üretim:** 2026-07-17, Cowork yan-oturum (Opus), tetik: Salih emri. Pointer: kapsül "Sonraki ilk iş §2 (K-009 açılış)" · pano K-009 satırı · senaryo-defteri (hazır blok §7).

---

## 0. Yetki çerçevesi (önce sınır)

- **Sınıf:** operasyonel/mimari-**sıralama** kararı (epistemik-kanon değil) → m.37(a) gereği karşıt-temel = zıt **karar-varsayımı** (beklenen-değer ↔ minimax), matematik-felsefesi okulu değil.
- **Geri-alınabilirlik:** sıralama kararı ucuz revert → m.37(e) gereği **1 karşıt-model yeter** (tam adversarial panel değil).
- **m.40b uygulandı:** 3-model sunumundan ÖNCE dış-tarama yapıldı (araştırma-önce). Atlas 4 şerit: ses · mobil-süreklilik · otonomi-yerleşik · guardrail.
- **m.41 uygulandı:** bu yüzey ana-sıra+Fable DEĞİL (Cowork/Opus). Kanon/inşa kararı burada GEÇERLİ olmaz. Bu dosya = **bulgu + aday**; ana sıraya (Şerit 1) taşınır, seçim orada Salih imzasıyla (K-009 açılış oturumu) alınır. İç düzen: P1 devri emsali (`vardiya-teslim-2026-07-17-ogrenme-P1.md`).

---

## 1. Vizyonun anatomisi — 3 yetenek katmanı

| Katman | Salih'in cümlesi | Teknik öz |
|---|---|---|
| **L1 — Sesle-kod** | "LoL oynarken konuşarak inşa" | eller meşgulken ses→görev; darboğaz gecikme DEĞİL, **pencere odağı** |
| **L2 — Mobil-süreklilik** | "seyahatte telefondan senkron devam" | PC oturumunu telefondan sürdür; git-tabanlı süreklilik |
| **L3 — Telefondan-sesle** | "ileride tamamen telefondan konuşarak" | L1 ∘ L2 bileşimi; otonomi + ses aynı anda |

**Kanon çapası:** V29 vizyonu (Iron-Man JARVIS) sıralaması zaten *dosya-zemin → kuyruk → EN SON ses/canlı-ajan*. G0-G6 partisyonunda **ses = G5** (otonomi+proaktiflik+ses), **K-009/K-010 kapısı G5'te**, ve kanon şartı: **"G4 güvenlik < G5 otonomi — sıra bozulamaz."** Yani vizyonun büyük kısmı bugün *teknik olarak* ulaşılabilir; asıl sınır bilinçli otonomi kapısı + güvenlik ön-koşulu.

---

## 2. Dış-tarama sentezi — HAZIR repolar/kaynaklar (Atlas 4 şerit)

### 2.1 L2 — Mobil-süreklilik (en olgun katman; çoğu bugün canlı)

| Çözüm | URL | Resmi/Topluluk | Olgunluk | Rol |
|---|---|---|---|---|
| **Remote Control** | code.claude.com/docs/en/remote-control | Resmi | Research preview | **Ana köprü** — canlı lokal oturumu telefondan sür; yalnız outbound HTTPS, inbound port yok |
| **Routines** | claude.com/blog/introducing-routines-in-claude-code | Resmi | GA | **"Günaydın/iyi geceler vardiya"** — bulutta, laptop kapalıyken; Scheduled/API/GitHub tetik |
| **Claude Code on the web** | code.claude.com/docs/en/claude-code-on-the-web | Resmi | GA | Lokalsiz async; git clone→çalış→PR |
| **Cowork web+mobile** | claude.com/blog/cowork-web-mobile | Resmi | Beta (Max) | Kapsül-devrinin **resmi mobil yüzü**; cihazlar-arası oturum+dosya |
| **Dispatch / Channels** | (aynı docs) | Resmi | GA | Telefondan görev→Desktop oturum · Telegram/Discord iki-yönlü tetik |
| **Happy** (slopus/happy) | github.com/slopus/happy | Topluluk | **Olgun** (MIT, 22.7k★, Haz2026) | Sağlayıcı-**bağımsız** açık köprü; E2E şifreli; self-host sync |
| Vibe Kanban (BloopAI) | github.com/BloopAI/vibe-kanban | Topluluk | Aktif | Çok-ajan orkestrasyon (worktree), mobil Kanban |
| ttyd / sshx + tmux + Tailscale | github.com/tsl0922/ttyd · ekzhang/sshx | Topluluk | Olgun/aktif | Ham terminal-in-browser; güvenlik sende |
| ~~Omnara~~ | github.com/omnara-ai/omnara | Topluluk | **ARŞİV (Şub2026)** | Açık repo terk → SaaS; açık yol için ÖNERİLMEZ |

**Senkron matematiği (Atlas tablosu — Model C/A için kritik):**
| Model | Tutarlılık | Çatışma maliyeti | Dayanıklılık |
|---|---|---|---|
| Tek-canlı-oturum (RC/Happy) | Linearizable | ~0 (tek yazar) | **DÜŞÜK** (tek makine, ~10dk timeout) |
| Bulut-transkript (RC backend/Cowork) | Güçlü-benzeri | Yok (sunucu otorite) | ORTA (ZDR org dışı) |
| **git-as-source-of-truth (JARVIS kapsül)** | Eventual | Merge (kötü durumda insan) | **YÜKSEK** (offline, git-log=hafıza m.10, makine ölse yaşar) |
| CRDT | Strong-Eventual | Otomatik | — (**olgun ürün YOK**, overkill) |

→ JARVIS zaten **tek-yazar** (m.1: klavyede başkası varsa değişiklik yok) → git çatışma ~0 → **git-as-truth doğru dayanıklı taban; mobil katman ÜSTÜNE oturur, yerine değil.**

### 2.2 L1 — Sesle-kod

| Araç | URL | Olgunluk | Lisans | Offline | Rol / oyun-uygunluğu |
|---|---|---|---|---|---|
| **Claude Code yerleşik `/voice`** | code.claude.com/docs/en/voice-dictation | Resmi (Mar2026) | Üründe dahil | Hayır (bulut STT) | Terminal-dikte; **TÜRKÇE var**; oyun-arka-plan **zayıf** (odak gerekir) |
| **Happy Coder** | github.com/slopus/happy | 22.7k★, MIT | MIT | Kısmen | **Oyun-arka-plan EN İYİ** — telefon=mikrofon, PC oyunda |
| **VoiceMode MCP** (mbailey) | github.com/mbailey/voicemode | 1.3k★, MIT | MIT | **Evet** (Whisper+Kokoro ~0.3s) | Claude Code ile **iki-yönlü sesli sohbet** — "konuşarak geliştir" açık çekirdeği |
| Handy (cjpais) | github.com/cjpais/Handy | 26.8k★ | MIT | **Evet** | En olgun açık dikte; global kısayol (oyun-dışı masaüstü) |
| Talon + Cursorless | talonvoice.com · cursorless | 866/1.3k★ | Talon kapalı / eklenti MIT | Evet | Gerçek hands-free — ama **yaşam tarzı** (dik eğri) |
| Motor katmanı | whisper.cpp (51.8k) · faster-whisper (24.3k) · Moonshine (~50ms) · Parakeet TDT (~%3.4 WER) | — | MIT | Evet | Yukarıdakilerin altında koşar |

**Oyun senaryosunun matematiksel özü:** darboğaz **gecikme değil, PENCERE ODAĞI**. `/voice` ve OS-dikte metni odaklı pencereye enjekte eder → LoL tam-ekranken tıkanır. İki temiz kaçış: **(1) kanal-ayrımı** (ses ayrı cihaza = telefon/Happy, PC %100 oyunda) · **(2) odaktan-bağımsız daemon** (wake-word+STT→PTY/tmux; RealtimeSTT/openWakeWord + kendi köprün — **hazır tek-tık ürün YOK, kompozisyon işi**). Streaming+push-to-talk gecikmeyi 50-260ms'e indirir; kod-sözlüğü WER'i şişirir (Claude'un proje/branch-adı hint'i tam bunun için).

### 2.3 L3/Otonomi — yerleşik primitifler (hepsi doğrulandı, çoğu birinci-taraf)

**Kritik düzeltme:** `/goal`, `/loop`, native scheduling **gerçek Anthropic özellikleri** (topluluk `.claude/commands` değil):
- **`/goal`** (GA, v2.1.139+): **koşul-sonlu** oturum-içi loop; her turdan sonra hızlı model (Haiku) tamamlanma-koşulunu değerlendirir → sağlanmadıysa yeni tur. Aslında session-scoped **Stop-hook** sarmalı. Sınır: 1 goal/oturum, koşul ≤4000 char, izin değiştirmez (auto-mode ile eşle).
- **`/loop`** (GA, bundled skill): **zaman-sonlu** cron loop (`CronCreate/List/Delete`). Sınır: session-scoped, 1dk granülerlik, 7-gün expiry, 50 task/oturum.
- **Headless `-p`** (GA): tam ajan-loop non-interaktif; `--output-format json` → `total_cost_usd` (koşum-başına bütçe); `--allowedTools`/`dontAsk` = gözetimsiz sınır; stdin 10MB tavan.
- **Agent SDK** (0.x, aktif, Anthropic Commercial Terms — OSI-açık DEĞİL): ajan-loop'u kütüphane olarak; hooks/subagents/MCP/permissions programatik.
- **subagent + worktree izolasyonu** (GA): ayrı bağlam-penceresi (N subagent ≈ N× token, ana bağlam temiz); `isolation: worktree` dosya-çatışmasını kaldırır. `/batch` 5-30 worktree-izole PR.
- **Routines** (research preview): bulut, laptop-kapalı; **1-saat min granülerlik**, claude.ai login şart, push yalnız `claude/`-önekli dallar, allowlist ağ. Tetik: Scheduled/API(bearer)/GitHub.
- **Hooks** (GA): `PreToolUse` = **allow/deny/ask/modify per tool-call** — non-deterministik ajanın çevresindeki **deterministik policy katmanı**. `SessionStart` context enjekte + `initialUserMessage`. `Stop/SubagentStop` turu bitirmeyi reddeder (= `/goal`'un motoru).
- **MCP** ≠ tetikleyici: MCP ajanın ÇAĞIRDIĞI araç yüzeyi; dıştan koşum başlatmaz → tetik Routines/Channels/hooks'ta.

**Otonomi merdiveni → hazır araç → guardrail-tier → yetki eşlemesi:**
| Basamak | Ne | Hazır araç | Guardrail tier* | Yetki |
|---|---|---|---|---|
| RC | insan sürer, canlı oturum telefondan | Remote Control (preview) | L1-L2 | **ŞİMDİ** |
| /goal | koşul-sonlu oturum-içi loop | /goal (GA) | L2 per-action | ŞİMDİ (gözetimli) |
| /loop | zaman-sonlu cron loop | /loop (GA) | L2-L3 | ŞİMDİ (gözetimli) |
| agent view/subagent | paralel izole | subagent+worktree (GA), agent view (preview), agent teams (exp, OFF) | L3 bounded | ŞİMDİ (araç-işi) |
| Routines | bulut, laptop-kapalı | Routines (preview) | L3-L4 | **K-009 KAPISI** |
| Dispatch | telefon görev→oturum | Dispatch (GA) | L4 | **K-009 KAPISI** |
| "canlı ajan" | ajan karar verir | Agent SDK + Routines API/GitHub trigger | L4-L5 | **K-010, SALİH** |

### 2.4 Guardrail katmanı — G4 (< G5 otonomi/ses; kanon: sıra bozulamaz)

- **Tehdit haritası:** OWASP Agentic Top-10 → **ASI06 Memory & Context Poisoning** (= JARVIS'in OpenClaw heartbeat→memory-poisoning endişesinin resmi adı) + **ASI08 Cascading Failures**; MITRE ATLAS (Memory Manipulation, Context Poisoning); survey: *"JARVIS or Ultron?"* (arxiv 2505.10924) — birebir bizim eksen.
- **Yerleşik guardrail (bedava, birinci-taraf):** **PreToolUse hook** = deterministik allow/deny/ask/modify → **m.31 Katman-1'i koda dök** (G0 policy-as-code; regex/allowlist, LLM-judge değil). Claude Code **sandboxing** (bubblewrap/Seatbelt): dosya+ağ-egress hard boundary = blast-radius sınırı.
- **Harici (ağır uç):** OPA/Rego (Apache-2.0, policy engine) · NeMo Guardrails · Guardrails AI · **LlamaFirewall/AlignmentCheck** (intent-tutarlılık = anti goal-drift) · **Invariant MCP-Scan** (flow-level, bridge-injection/tool-poisoning) · Llama Guard 4 · Rebuff (canary).
- **Eval/judge:** hakem gürültülü sınıflandırıcı (hata >%50 karmaşık işte) → **model-versiyonu pinle**, κ≥eşik tabanı, judge = **HITL tetikleyici**, ikame değil (K-020 hattı: DeepEval/Ragas/Phoenix).
- **Escalation-ladder matematiği (yük-taşıyan ilke):** **kontrol-gücü ≈ f(otonomi × geri-alınamazlık × blast-radius)**; kapı geri-alınamaz eylemden ÖNCE. Anthropic bulgusu: kullanıcı promptların ~%93'ünü onaylıyor (approval-fatigue) → **auto-mode = risk-katmanlı HITL**. Bu formül **m.31 geri-alınabilirlik ekseni + m.37(e) "karşıtlık-derinliği geri-alınabilirliğe endeksli"** ile birebir örtüşür (dış teyit).

---

## 3. Üç matematik-temelli model (m.37) — mimari nasıl SIRALANIR?

Parametreler: **token** (kurulum maliyeti: az/orta/çok) × **zaman** (ilk-çalışan-yeteneğe süre) × **beklenen-kalite** (1-10) × **RİSK** (4. boyut, senaryo-defteri 07-15 emsali).

### Model A — Kaldıraç-önce (beklenen-değer maks., öncül-tahmine göre)
- **Ne:** L2'yi bugün platformdan **devral** (Remote Control + Cowork mobile + git-as-truth + kapsül = zaten çalışıyor; bu oturum kanıt). Ses = en son, ince dikte adaptörü. En yüksek (açılan-yetenek × bugün-çalışma-olasılığı) / maliyet basamağını seç.
- **token DÜŞÜK** (konfig+alışkanlık, yeni altyapı yok) · **zaman ÇOK KISA** (gün) · **kalite 7.5/10** (mutlu-yolda iyi ama **tavan-sınırlı**: ölçüm disiplini yok → token×zaman farklılaşma-tezi kalibre edilemez) · **RİSK ORTA** (platform-bağımlı; aceleyle gözetimsiz senkron K-009 kapısına değer).
- Kanon dayanağı: G0-G6 bulgu #6 "JARVIS önden gidiyor — yeni altyapı kurma, düşük-sürtünme mobil köprü."

### Model B — Ölçüm-önce / kademeli (VoI: bilgi-değeri) — ✅ ÖNERİ
- **Ne:** Merdiveni **deney** olarak koş. Her basamağa 1 **gözetimli** dilim, `/usage` ölç, yalnız **%-iyileşme eşiği** geçince terfi (successive-halving/ASHA; Optuna K-020). L2 önce devralınır ama **enstrümante**. Ses+mobil = ölçülen deney (WER+gecikme+görev-başarı). = A1-A7 partisyonunun ta kendisi; Faz-4 tek-atış Routine bunu zaten yaptı (07-17).
- **token ORTA** (enstrümantasyon+dilimler, her dilim küçük) · **zaman ORTA** (veri toplamanın duvar-saati) · **kalite 8.5/10** (her seçim kalibre; **m.35 farklılaşma tezini doğrudan besler**) · **RİSK DÜŞÜK** (ölçümlü, geri-alınabilir, K-009 kapısına saygılı, G4<G5 her basamakta ölçülür).
- Kanon dayanağı: m.35 ölçüm-önce + m.40c kademeli + A1-A7 + G0 substratı + senaryo-defteri Faz-4 emsali.

### Model C — KARŞIT-TEMEL: Worst-case / minimax-regret (dayanıklılık-önce)
- **Ne:** Otonomiyi ilerletmeden ÖNCE kanalı sertleştir + worst-case kaybı **sınırla**. Local-first offline-hayatta-kalan senkron (git-as-truth). Ses/mobil = **untrusted girdi** → policy-as-code (PreToolUse hook) İLK. En güçlü guardrail'ler önce gözetimsiz basamaklara (Routines/Dispatch). Ortalamayı değil, en-kötü-durum pişmanlığını minimize et.
- **token YÜKSEK** (ihtiyaçtan önce guardrail+dayanıklılık) · **zaman YÜKSEK** (yetenekten önce güvenlik iskelesi) · **kalite(ortalama-durum) 6/10** (mutlu-yolda aşırı-mühendislik, düşük kalite/token) · **RİSK: worst-case EN DÜŞÜK, fırsat-maliyeti EN YÜKSEK** (ulaşılmamış otonomi için inşa → m.5/m.35 sorun-güdümlü ile sürtüşür).

**Karşıt-temel (m.37 ek, 07-17):** Model C ← **Wald minimax karar teorisi + robust/distributionally-robust optimization**; önerilen B'nin **beklenen-değer/VoI (ortalama-durum optimizasyonu)** varsayımına ZIT (m.37a operasyonel eksen — kanonun kendi örneği "beklenen-değer ↔ minimax"). **Aygıt şartı ✓:** gerçek matematiksel aygıttan türetildi — minimax + kontrol-ölçekleme formülü f(otonomi×geri-alınamazlık×blast-radius) (OWASP/SAIF/NIST escalation-ladder), isim-etiketi değil. **Canlılık şartı ✓:** robust optimization + DRO 2020'ler aktif araştırma; OWASP ASI (Ara2025) / SAIF 2.0 / NIST AI 600-1 canlı çerçeveler → bilimsel temelli + bugün savunulabilir.

---

## 4. Öneri + triangülasyon (m.37 §9.5 — asıl çıktı)

**Öneri = B (ölçüm-önce omurga)**, A'nın kaldıraç-sıralamasıyla (L2'yi bedava önce devral) ve C'nin gözetimsiz-basamak guardrail-kapısıyla aşılanmış.

**Zıt temeller NEREDE YAKINSIYOR (gerçek triangülasyon → YÜKSEK güven, hemen aksiyon):**
1. **Senkron = git-as-truth + mevcut kapsül-devri, bespoke senkron DEĞİL.** A(ucuz+çalışır) · B(zaten enstrümante, git-log=hafıza) · C(offline-hayatta-kalan, worst-case-robust local-first). Üç zıt temel → aynı eylem = gerçek triangülasyon.
2. **Ses = çalışan metin-loop'una ince adaptör, EN SON (G5).** A(şimdi en yüksek maliyet/en düşük marj) · B(önce loop enstrümante) · C(ses = en tehlikeli untrusted yüzey, G4 guardrail'den sonra) + V29 sıralaması + G5 yerleşimi + Leon [İZLE]. Oyun için kanal-ayrımı (telefon/Happy) ilk somut PoC.

**NEREDE AYRIŞIYOR (gerçek ödünleşim — BENİM kararım DEĞİL):**
- **Otonomi DERİNLİĞİ** — "canlı ajan" çizgisi hangi basamak; Routines/Dispatch ne kadar sert kapılanır. B/A veri/kaldıraç elverdikçe ilerlet; C sert guardrail-kapısı. = tam olarak **K-009 açık sorusu, Katman 1, SALİH.** Kanon zaten C'ye kısmen yaslı: **G4<G5 "sıra bozulamaz"** + escalation-ladder f(otonomi×geri-alınamazlık×blast-radius). Yani güvenlik-önce sıralaması tartışma değil; tartışılan = **hız/derinlik**.

---

## 5. Somut inşa önerisi (öneri B + yakınsamalar; m.40c düşük-maliyet şeridi)

- **Adım 0 (bu hafta, DÜŞÜK-maliyet, geri-alınabilir):** L2'yi **"mobil köprü protokolü"** olarak formalize et — Remote Control + Cowork mobile + git-as-truth + kapsül-devri; KILAVUZ'a 1 sayfa. G0 "düşük-sürtünme mobil köprü", turnkey. (Bu oturumun kendisi kanıt.)
- **Adım 1 (ölçümlü PoC — B):** Ses = ince adaptör. Oyun için **Happy** (telefon-kanalı) veya ikinci-terminal **VoiceMode MCP**; 1 hands-free oturum, WER+gecikme+görev-başarı `/usage` ile logla → senaryo-defterine. Türkçe: `/voice tr` + VoiceMode yerel Whisper ikisi de kaldırır.
- **Adım 2 (G4 ön-koşulu — C katkısı, gözetimsiz'den ÖNCE):** untrusted-input guardrail = **PreToolUse hook** (deterministik allowlist; m.31 Katman-1 + m.23 YASAKLAR koda). Ses/mobil kanalları gözetimsiz açılmadan önce.
- **Adım 3+ (K-009 kapısı, SALİH):** otonomi derinliği — Routines/Dispatch basamakları, "canlı ajan" çizgisi, memory-write validation (anti-ASI06) + cascade circuit-breaker. Katman 1.

---

## 6. Doğrulanmamış bayraklar (dürüstlük — Atlas notları)

- Routines per-tier günlük koşum tavanı (Pro5/Max15/Ent25) — Nis-May2026 basınından, güncel resmi docs'ta per-tier tamsayı yayınlamıyor → **doğrulanmadı**.
- Background-task 5GB oto-sonlanma eşiği · subagent eşzamanlılık min(16, çekirdek−2) → topluluk kaynağı, resmi değil.
- MINJA/MemoryGraft memory-poisoning saha rakamları (>%98) → survey özeti, birincil paper fetch edilmedi.
- Ragas/DeepEval/TruLens lisansları → convention, doğrudan LICENSE okunmadı.
- Genel: veriler 2026-07-17 web taraması; `/voice` + Remote Control + Routines **preview** → API/sınır değişebilir. Canlı doküman tekrar okunmalı.

---

## 7. Senaryo-defteri'ne HAZIR BLOK (m.41: ana sıra/Salih dosyalar; ben yan-oturumdan yazmam)

```
### 2026-07-17 · K-009/K-018 · otomasyon-vizyonu mimari sıralaması
- Bağlam: Salih emri "sesle+telefondan senkron geliştirme" nihai-hedefi için hazır repo taraması + 3-model mimari sıralama.
- Model A (kaldıraç-önce/EV-maks): token DÜŞÜK · zaman ÇOK KISA · kalite 7.5 · RİSK ORTA — L2 bedava devral, ses en son | Model B (ölçüm-önce/VoI): token ORTA · zaman ORTA · kalite 8.5 · RİSK DÜŞÜK — merdiven=deney, basamak-başına gözetimli dilim+%-eşik | Model C (worst-case/minimax): token YÜKSEK · zaman YÜKSEK · kalite(ort) 6 · RİSK worst-case EN DÜŞÜK/fırsat EN YÜKSEK — guardrail+dayanıklılık önden → ✅ B (A kaldıraç-sırası + C gözetimsiz-guardrail aşısıyla)
- Karşıt-temel (m.37 ek): Model C ← Wald minimax + robust/DRO optimization, B'nin beklenen-değer/VoI ortalama-durum varsayımına zıt; aygıt = f(otonomi×geri-alınamazlık×blast-radius) escalation-ladder (isim değil); canlılık = OWASP ASI/SAIF2.0/NIST600-1 + DRO canlı ✓. Triangülasyon: git-as-truth senkron + ses-en-son iki noktada A+B+C kesişti (gerçek); ayrışma = otonomi derinliği (K-009/Salih).
- Seçim: BEKLEMEDE — K-009 açılış oturumu, Salih (Katman 1). YAN-OTURUM (m.41) kanon kilitlemez; bu blok devir raporundan (raporlar/2026-07-17-otomasyon-vizyon-mimarisi-arastirma-3model.md) taşındı.
- Gözlem: bekliyor (Adım 0 mobil-köprü formalize + Adım 1 ses PoC /usage).
- Ders: —
```

---

## 8. K-009 açılış oturumu için düşen sorular (Salih'e)

1. **"Canlı ajan" çizgisi hangi basamak?** (RC/goal/loop = gözetimli, ŞİMDİ · Routines/Dispatch = bulut-gözetimsiz, kapı · Agent-SDK-karar = K-010). Escalation-ladder + G4<G5 sıralamayı dayatıyor; **hız/derinlik** senin.
2. **L1 ses PoC'una şimdi girilsin mi** (düşük-maliyet, geri-alınabilir — m.40c'ye uyar) yoksa L2 formalize sonrası mı?
3. **Guardrail eşiği:** PreToolUse hook (yerleşik, bedava) ilk otomasyon-dilimiyle BİRLİKTE mi kurulsun (C: evet, gözetimsiz'den önce)?

---

## 9. Kararlar Kısmı (Decision Console) — sesle/mobilden karar alma katmanı [07-18 eki]

> Salih 07-18: m.37 3-model karar stilini otomasyon vizyonuyla BİRLEŞTİR — oyunda sesle, seyahatte telefondan karar al; bunun için "kararlar kısmı" arayüzü. *(Atlas dış-desen şeridi koşuyor; §9.5 dönünce rafine.)*

### 9.1 Çekirdek içgörü: arka-uç ZATEN VAR
- `senaryo-defteri.md` = kararların git-tabanlı DEFTERİ (arka-uç). Her blok = {bağlam · 3 model · karşıt-temel · öneri · **SEÇİM** · gözlem}.
- **"Kararlar kısmı" = bu defterin İNSAN-YÜZÜ ÖN-UCU:** Seçim=BEKLEMEDE kararları sunar → Salih sesle/mobilden çözer → sonuç deftere işlenir. Yeni kavram değil, mevcut kanonun (m.37 görünürlük + m.31 veto + m.9 proof-of-work) UI'ı.

### 9.2 Yetki (CC raporuyla bağ): konsol KARAR VERMEZ, SUNAR + Salih'in kararını YAKALAR
- Katman-1 seçim = Salih (m.31). Konsol m.37 görünürlüğünü sesle/mobile TAŞIR; Carvis SUNAR, Salih SEÇER. Konsolun kendisi karar almaz → **confused-deputy koruması** (CC §6): düşük-yetkili yüzey ajanı kanona kilitletemez.
- Yani "kararlar kısmı" = Salih'in Katman-1 yetkisini uzaktan/sesle KULLANDIĞI arayüz; ajan yetki-bandı değişmez.

### 9.3 Ses akışı (oyun — eller meşgul, kanal-ayrımı)
1. Carvis push: "N bekleyen karar" (Remote Control push / Channels).
2. Salih (telefon/Happy, PC oyunda): "kararları oku".
3. Carvis TTS: her karar = öneri + 3 model tek-cümle + karşıt-temel (kısa).
4. Salih: "B'yi seç" / "veto" / "sonra" → deftere işlenir.
- **Onay-maliyeti ↔ hata-maliyeti:** geri-alınamaz karar → katı doğrulama ("B — emin misin?"); ucuz-geri-alınır → tek-kelime yeter. = m.31 geri-alınabilirlik ekseni sesli-onaya taşınmış.

### 9.4 Mobil akışı (seyahat)
- Karar-kartları: öneri vurgulu + 3 model + karşıt-temel + triangülasyon; tek-dokunuş seç/veto/ertele. Remote Control / Cowork mobile / Artifact üstünde.

### 9.5 Dış-tarama (Atlas DONE) — 3 katman + emsaller
**Üç katmanı karıştırma:** (1) karar-ÜRETİM (bizde var) · (2) onay/disposition arayüzü (agent-proposes-human-disposes) · (3) karar-defteri/audit (git-as-truth = senaryo-defteri). Piyasa 2-3'te olgun AMA **kod-eylemi onayına** (SQL/deploy) odaklı; bizim "3 soyut model + gözlem" niş.
- **Onay-inbox emsalleri:** LangChain **Agent Inbox** (kart/onay UX; Notify/Question/Review; zaman→öncelik sıralaması = karar-kuyruğu önceliklendirme) · LangGraph **interrupt()** (approve/edit/reject/respond motoru) · **HumanLayer** (çok-kanallı: Slack/SMS/WhatsApp = mobil) · **Trigger.dev waitpoint / Inngest** (dayanıklı bekleme — "karar günlerce açık kalır, sonra telefondan onayla") · Slack Block Kit.
- **Git-defter üstü pano emsali:** **Log4brains** (markdown ADR'leri git'te → web pano: zaman-çizelgesi + history graph; Apache-2.0) — ADR ≈ karar-bloğumuz; en yakın hazır iskelet. Alternatif: Astro Content Collections (markdown-as-DB).
- **Çok-seçenekli sunum (bilişsel yük):** Hick yasası + Miller ~7 → **3 seçenek + 1 öneri tam tatlı nokta** (choice-overload altında). En düşük yük = **öneri vurgulu + yan-yana karşılaştırma, tek turda** (sesle sıralı sorma!). → *bizim "öneri işaretli 3 model" formatı literatürle uyumlu.*
- **DÜRÜSTLÜK:** hepsini tek pakette veren ürün **bulunamadı** → kompozisyon. Ama en pahalı parçalar (Remote Control/Channels/Happy/VoiceMode) zaten bizde.

### 9.6 İnşa opsiyonları (TARTIŞMA; karar yok)
- **A — Yerel karar-panosu** (git-as-truth; Log4brains/Astro): karar-blokları frontmatter'lı (`status: pending|selected|vetoed` · `reversible` · `layer`); pano öneri-vurgulu + 3-model yan-yana render; seçim → `seçim`+`gözlem` yaz + commit. Masaüstü/görsel ağırlıklıysa. Artifact karar-kartı burada doğal.
- **B — Bekleme-noktası + çok-kanallı push** (seyahat-first): her karar bir waitpoint (Trigger.dev/HumanLayer) → telefona actionable push (Duo/banka kartı deseni: bağlam+öneri upfront) → dokun/yanıtla → token tamamlan → git'e yaz. Dayanıklı (günlerce bekler).
- **C — Sesli karar-döngüsü** (oyun-first, mevcut köprüler): Routine en-öncelikli bekleyen kararı çeker → VoiceMode/Happy TTS okur → "B, gözlem X" → git commit. **Doğrulama geri-alınabilirliğe göre:** iki-yönlü kapı → implicit ("B kaydedildi" + earcon); tek-yönlü (m.31 Katman-1: publish/para/veri) → **explicit** ("geri-alınamaz, onaylıyor musun?"). Oyun-İÇİ değil **maç-arası digest** (kesme-maliyeti min).
- **★ Öneri (Atlas + benim):** **B ⊕ C tek git-çekirdeği üstünde + A görselleştirme katmanı.** = senaryo-defteri tek veri-modeli, **üç yüz** (sesli/push/pano). **Bu senin m.18 "üç-yüzlü durum bloğu" felsefenle birebir** — onay-derinliği `reversible`/`layer` alanlarından türetilir (matematik → koda). Otomasyon Model B (ölçüm-önce) ile tutarlı: en ucuz yüz (C, mevcut köprüler) önce, ölçülerek büyür.

### 9.7 Matematik açı (Atlas)
- Karar-kuyruğu önceliği = f(bloke-ettiği-iş · bayatlık · geri-alınamazlık).
- Onay↔hata maliyeti: yanlış "evet" pahalı → explicit+tekrar-oku; ucuz/revert → implicit tek-kelime.
- Bildirim batching: aciller anında, gerisi doğal-ara digest (maç-arası); digest engagement +%35.

### 9.6 Açık sorular (Salih cevabı bekleniyor — karar yok)
- "Kararlar kısmı" ayrı UI mı (O2/O3) yoksa mevcut yüzeyler üstünde skill/view mi (O1)?
- Hangi kararlar konsola düşer — yalnız m.37 ölçek-eşiği üstü mü, hepsi mi?
- Sesli-onayda geri-alınamaz kararlar için doğrulama-derinliği?
- Bu, `karar-modeli` skill'inin çıktı-hedefi olur mu (skill 3-model üretir → konsola düşer → Salih sesle seçer → `/karar-kaydet` işler)?
