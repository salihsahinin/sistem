# İB-66 — Gözlemlenebilir iç-içe (nested) LLM loop sistemi: atlas sentezi

**Künye**
- Emir: `cc/gorev-2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md`
- Koşum HEAD: `081cb1f` (main)
- **AS-OF 2026-08-31** — tüm ürün/standart iddiaları bu tarihe damgalıdır; sonraki okumada yeniden doğrulanmalıdır (Karar 68).
- Ajan sayısı: **6 işçi** (A1, A2, B, C, ANTİTEZ, V26) · işçi modeli **sonnet** · hakemlik + sentez: lider-ajan, model **opus**
- **Koşum arızası (şeffaflık):** 7. ajan (maskeli hakem, opus) AÇILAMADI — `.claude/hooks/pretool-ajan-fren.sh` (İB-54 / Karar 39) oturumun 72. Agent çağrısında DURDUR eşiğini uyguladı. Fren Salih beyanı olmadan aşılmadı; hakemlik lider-ajan tarafından, iddiaları maskeli kimlikle (İ-01…) sıralayarak koşuldu. Bağımsızlık kaybı bir zayıflıktır ve burada beyan edilir.
- Ham işçi raporları: `cc/rapor-2026-08-31-ib66-{a1,a2,b,c,antitez,v26,hakem}.md`
- **HÜKÜM YOKTUR** — bu rapor masaya girdi hazırlar (m.31); karar Salih'indir.

---

## KOŞUM KESİNTİSİ (eksik beyanı)

Bu oturumun ajan-freni (`.claude/hooks/pretool-ajan-fren.sh` — İB-54 / Karar 39) DURDUR eşiğine ulaştı (sayaç 78, eşik 72). Frenin kaldırılması Salih beyanı gerektirir; aşılmadı.

**KOŞULAN adımlar (6 işçi, hepsi sonnet, raporları diskte):**
- A ailesi — ürün/pazar taraması: **KOŞULDU**, iki işçiye bölündü (A1: 6 araç, A2: 6 araç) → 12 araç
- B ailesi — mimari/standart emsalleri: **KOŞULDU** (5 başlık)
- C ailesi — iç envanter (web'siz): **KOŞULDU** (5 başlık, pointer'lı)
- ANTİTEZ (CoVe-Factored): **KOŞULDU** — 9 iddia sondajlandı
- V26 örneklem denetimi: **KOŞULDU** — 9 iddia birincil-kaynak sondajı

**KOŞULAMAYAN adım:**
- **Maskeli hakem AYRI ajan olarak açılamadı.** 7. Agent çağrısı fren tarafından engellendi. Hakemlik lider-ajan (model opus) tarafından, iddiaları maskeli kimlikle (İ-01…İ-46) sıralayarak ve kaynak aileyi hükümden sonra açarak koşuldu → `cc/rapor-2026-08-31-ib66-hakem.md`. **Bağımsız hakem yoktur; sentezi yazan ile hakemlik eden aynı ajandır.** Bu, m.40b zincirinin çapraz-denetim değerini düşürür ve raporun en zayıf metodolojik noktasıdır.

**SAĞLANMAYAN durma-koşulu maddeleri:**
1. Bağımsız maskeli hakemlik (yukarıda).
2. Matriste **4 hücre `[?]` kaldı** ve kapatılamadı: CrewAI K1, Temporal K1, Langfuse K1, Arize Phoenix K1 — dördü de canlılık kriteri. Ek işçi açılamadığı için bu boşluklar doldurulmadı.
3. Model A'nın ön koşulu — `parent_tool_use_id`'nin GERÇEK bir nested gnhf koşumunda dolduğunun doğrulanması — yapılmadı (koşum gerektirir, yasak sınırında; masaya taşındı).

**Hüküm damgası:** araç örneklemi eksik DEĞİLDİR (emir ≥10 istedi, 12 tarandı), ama **hücre örneklemi eksiktir**: 60 hücrenin 13'ü `[?]`. Hüküm bu nedenle **KISMİ** olarak verilmiş ve §2'de "kapalı değil" kaydıyla sınırlandırılmıştır. Hiçbir `[?]` hücre tahminle doldurulmamıştır.

---

## 0. Kriter seti (taramadan ÖNCE yazıldı — bulanıklık freni)

| Kod | Kriter | EVET sayılma şartı |
|---|---|---|
| **K1** | CANLILIK | Koşum HÂLÂ SÜRERKEN akış görünür. Post-hoc / batch-export / "replay" = HAYIR |
| **K2** | KONUŞMA-GRANÜLÜ | Gösterilen birim ajanın KONUŞMA turu: assistant metni + araç çağrısı gövdesi okunur. Yalnız span/latency/token metriği = HAYIR |
| **K3** | İÇ-İÇE SEVİYE AYRIMI | ≥2 iç-içe döngü seviyesi AYRI ve EŞZAMANLI yüzeylerde. Tek düz ağaç/liste = KISMİ |
| **K4** | MÜDAHALE | Koşum sürerken duraklat / mesaj enjekte / dallandır / iptal / state düzenle |
| **K5** | ÜRÜN-OLGUNLUĞU | GA / genel kullanıma açık = EVET; beta / araştırma prototipi / OSS-demo = KISMİ |

Kriterler taramadan önce sabitlendi ve koşum boyunca değiştirilmedi.

---

## 1. Kriter matrisi × 12 araç (hakem düzeltmeleri uygulanmış)

Her hücre birincil kaynağa ve AS-OF 2026-08-31'e bağlıdır. `[?]` = kaynak bulunamadı/doğrulanamadı — **"yok" DEĞİL, "bilinmiyor"**. Hücre gerekçeleri `cc/rapor-2026-08-31-ib66-hakem.md` (İ-01…İ-46) ve ham aile raporlarındadır.

| # | Araç | K1 canlılık | K2 konuşma | K3 seviye | K4 müdahale | K5 olgunluk | Birincil kaynak |
|---|---|---|---|---|---|---|---|
| 1 | LangGraph Studio + LangSmith | EVET* | `[?]` | `[?]`▲ | **EVET** | KISMİ | docs.langchain.com/oss/python/langgraph/interrupts · /langsmith/studio |
| 2 | AgentOps | HAYIR | KISMİ | KISMİ | HAYIR | EVET | docs.agentops.ai/v2/introduction · github.com/AgentOps-AI/agentops |
| 3 | AutoGen Studio (AutoGen/AG2) | EVET | EVET | HAYIR | `[?]` | **HAYIR** | microsoft.github.io/autogen — kaynağın kendi beyanı: "not production-ready" |
| 4 | CrewAI AMP / Enterprise | `[?]` | KISMİ | `[?]` | `[?]` | EVET | docs.crewai.com/en/observability/tracing · crewai.com/agent-management-platform |
| 5 | OpenAI Agents SDK tracing | **HAYIR** | EVET | `[?]`▲ | HAYIR | EVET | openai.github.io/openai-agents-python/tracing (batch export, "may not appear immediately") |
| 6 | Temporal Web UI | `[?]`▲ | **HAYIR** | KISMİ | **EVET** | EVET | docs.temporal.io/web-ui · /child-workflows |
| 7 | Claude Agent SDK / Managed Agents | KISMİ | EVET | KISMİ | **HAYIR**▲ | KISMİ (beta) | platform.claude.com/docs/en/managed-agents/* · code.claude.com/docs/en/agent-sdk/{streaming-output,subagents} |
| 8 | **Devin — Managed Devins** | KISMİ | EVET | **EVET** | **EVET** | EVET | cognition.com/blog/devin-can-now-manage-devins · docs.devin.ai |
| 9 | Manus (My Computer) | EVET | `[?]` | **HAYIR** | EVET | EVET | manus.im/blog/manus-my-computer-desktop |
| 10 | Langfuse | `[?]` | EVET | KISMİ | HAYIR | EVET | langfuse.com/docs/observability/* |
| 11 | Arize Phoenix | `[?]` | `[?]`▲ | KISMİ | HAYIR | EVET | arize.com/docs/phoenix |
| 12 | **Braintrust** | **EVET**▲ | EVET | KISMİ | HAYIR | `[?]` | braintrust.dev/docs/observe/view-logs ("Live tail") · /docs/guides/traces |

`*` WebSearch özetinden, birincil metinle birebir eşleşmedi (hakem: K).
`▲` ANTİTEZ ∨ V26 sondajıyla DÜZELTİLEN hücre:
- **1-K3**: A1 "HAYIR" demişti → hedef sayfa 404, ne doğrulandı ne çürütüldü → `[?]`
- **5-K3**: "tek dikey ağaç" → doküman görsel sunumu hiç söylemiyor (aşırı-belirlilik) → `[?]`
- **6-K1**: "liveness… real-time" alıntısı gösterilen birincil sayfada BULUNAMADI (kaynak eşleşmesi hatalı) → `[?]`
- **7-K4**: "kısmi" → birincil `subagents` sayfasında `pause`/`interrupt`/mid-task enjeksiyon YOK; yalnız tamamlanmış/limit-durmuş ajanın SIRALI resume'u → **HAYIR**
- **11-K2**: "token-level zoom" alıntısı resmî dokümanda yok, ikincil/SEO → `[?]`
- **12-K1**: A2 `[?]` demişti → birincil doküman "**Live tail** — new rows highlighted with a flash animation, streaming pauses when the tab is hidden" → **EVET**

**Sütun sayımı:**

| Kriter | EVET | KISMİ | HAYIR | `[?]` |
|---|---|---|---|---|
| K1 | 4 | 2 | 2 | 4 |
| K2 | 6 | 2 | 1 | 3 |
| K3 | **1** | 6 | 2 | 3 |
| K4 | 4 | 0 | 6 | 2 |
| K5 | 8 | 2 | 1 | 1 |

**K1∧K2∧K3∧K4 hepsi EVET olan araç: 0 / 12.**

---

## 2. HÜKÜM (matristen gerekçeli, model hafızasından değil)

> **KISMİ.** Beş kriteri BİRLİKTE karşılayan ürün **YOK** (0/12); kriterler ayrı ayrı **VAR**.

Matristen okunan gerekçe zinciri:

1. **Darboğaz K3'tür.** 12 araçta yalnız **1** net EVET (Devin: koordinatör + N managed Devin, her biri ayrı izole oturum). Kalan 11'de ya tek-ağaç KISMİ (6), ya HAYIR (2), ya `[?]` (3).
2. **K3'ü karşılayan tek araçta K1 düşüyor.** Devin'de her alt-oturum kendi *session link*'inde; tüm seviyeleri TEK ekranda eşzamanlı akıtan konsolide pano hiçbir birincil kaynakta tarif edilmiyor (ANTİTEZ bağımsız sorguladı, hüküm AYAKTA).
3. **K1'i net karşılayanlarda K3 ya da K5 düşüyor.** Braintrust: K1+K2 EVET (Live tail), ama K3 tek-ağaç KISMİ, K4 HAYIR. Manus: K1+K4 EVET, K3 kategorik HAYIR (tek-ajan ürünü). AutoGen Studio: K1+K2 EVET, ama K5 kaynağın kendi beyanıyla HAYIR ("araştırma prototipi, üretime uygun değil") + K3 HAYIR.
4. **K2 6 araçta EVET ama hiçbirinde K3 ile birlikte değil.** Aradığımız üçlü — canlı ∧ konuşma-granüllü ∧ seviye-ayrımlı — hiçbir üründe birleşmiyor.
5. **K4 ürün sınıfına göre kategorik ayrışıyor.** Gözlem araçları (AgentOps, Langfuse, Phoenix, Braintrust) tasarım gereği kontrol katmanı sunmuyor: 4/4 HAYIR. Kontrol sunanlar (LangGraph, Temporal, Devin, Manus) ise K2 ya da K3'te düşüyor.

**Salih'in negatif bulgusu ÇÜRÜTÜLEMEDİ.** Ancak "hiçbir ürün yaklaşmıyor" biçimindeki güçlü versiyonu iki noktada zayıfladı ve raporda kayıtlıdır: Devin K3+K4'te, Braintrust K1+K2'de gerçek karşılık üretiyor. Ayrıca 4 hücre `[?]` kaldığı için (CrewAI ve Temporal K1, Langfuse/Phoenix K1) hüküm **kapalı değil**: bu 4 boşluk doldurulursa hüküm sertleşebilir ya da yumuşayabilir.

**Denetim şeffaflığı:** V26 örneklem sondajı 9 iddiadan **5'ini tam doğruladı (%55,6)**, 2 KISMİ, 2 DESTEKLEMİYOR, 0 ölü URL; **6 ihlal** listelendi (2 yanlış kaynak-eşleşmesi, 2 aşırı-genelleme, 1 SEO/ikincil kaynak, 1 bağlam eksikliği). Hepsi yukarıda matrise düzeltme olarak işlendi. ANTİTEZ 9 iddiadan 4 AYAKTA / 1 DÜŞTÜ / 2 BELİRSİZ / 2 sondaj yapılmadı. Hakem dağılımı **D 27 · K 11 · X 8**.

---

## 3. "Chat olarak gözlemlenemiyor" → GEREKSİNİM listesi (S2 girdisi)

Salih'in gerekçesi ("gnhf nested olsa da ürün olarak sunulamaz, çünkü görev akışı chat olarak gözlemlenemiyor") 8 gereksinime çözülür. Her biri iç envanterden (aile C) ya da matristen türetilmiştir:

| # | Gereksinim | Neden (kanıt) |
|---|---|---|
| G1 | Her kayıt satırı okunur bir KONUŞMA turu olmalı: assistant metni + araç çağrısı gövdesi + araç sonucu | Matriste K2 = ayrım noktası; `gnhf-izle.py` bunu zaten yapıyor (`tools/gnhf-izle.py:30-49`) |
| G2 | Her satır **seviye etiketi** (L0…L3) + parent referansı taşımalı | `gnhf-izle.py` `parent_tool_use_id`'yi hiç okumuyor → K3 boşluğunun kök nedeni |
| G3 | Canlılık: append-only kütük + tail, gecikme ≤ 2 sn | Zaten var (`:66-86`, `sleep(2)`, bayt-ofsetli kısmi-satır güvenli) |
| G4 | Çoklu eşzamanlı koşum / çoklu worktree tek yüzeyde | Şu an yalnız EN YENİ worktree'nin EN SON koşumu izleniyor (`:20-22`, `:60-63`) |
| G5 | Seviye filtresi: "yalnız L1 göster", "L2'yi aç/kapa" | Emsal: Temporal'ın "her child kendi event history'si, parent'ta yalnız referans olayı" deseni |
| G6 | Bütçe görünürlüğü: her turda ÖNBELLEK-OKUMA DAHİL kümülatif token | `usage` alanı önbellek-okuma/yazma ayrımını ve `result.usage.modelUsage` dökümünü taşıyor ama izleyici hiç göstermiyor; 535k/500k tavan arızası bu körlükte yaşandı |
| G7 | Asgari müdahale kancası: iptal + bir sonraki iterasyona not enjekte | K4 pazarda 6/12 HAYIR; Claude Agent SDK'da mid-run müdahale birincil kaynakta YOK → bizde de yalnız **iterasyon sınırında** mümkün |
| G8 | Kalıcılık: gnhf worktree transkriptleri merkezi hareket kütüğüne düşsün | `raporlar/2026-08-31-k010-a3-loop-1.md:22` — açık kapsama açığı |

**Tasarımı sınırlayan sert teknik kısıt (birincil kaynak, İ-27):** Claude Agent SDK dokümanı birebir şunu söylüyor — `parent_tool_use_id` alanı `StreamEvent` (token-delta) mesajlarında **her zaman null**; alt-ajanların token-seviyesi delta'ları ana oturuma **forward edilmez**; parent atfını yalnız TAMAMLANMIŞ mesajlar taşır (`code.claude.com/docs/en/agent-sdk/streaming-output`, AS-OF 2026-08-31). Sonuç: **alt-ajan seviyesi (L2) canlı token akışıyla değil, ancak tamamlanmış mesaj granülüyle etiketlenebilir.** Bu, "her seviye tam canlı" hedefinin fizik sınırıdır — tasarım buna göre yapılmalıdır, aşılamaz.

---

## 4. S2 — Gözlemlenebilir sürüm: 3 tasarım modeli (m.37)

**Sayısal taban (ölçülmüş, tek kaynak damgalı):** gnhf iterasyon tabanı ~300k token (önbellek-okuma dahil); e2e715 koşumu 2 iterasyonda 535k/500k tavanı doldurdu; e600a7 koşumu 3M tavan + tek-çağrılı uzun uyku (2×590 sn, 12×100 sn yerine) ile 3/3 iterasyonu 0 arızayla bitirdi (`raporlar/2026-08-31-k010-a3-loop-1.md:12-13`). Aşağıdaki tahminler bu tabana göredir ve **işçi/gnhf koşumları içindir**. Referans iş: 3 iterasyonluk bir gnhf koşumu ≈ 900k token.

### Model A — **Tek akış, seviye-etiketli kütük + tek canlı pano** (ÖNERİLEN)
Matematiksel temel: *tek append-only olay dizisi + parent referansıyla ağaç yeniden kurulumu* (Temporal event-history + OTel parent_span_id emsali). Kütük tek, görünüm türetilmiş.
- Yapılacak: `gnhf-izle.py`'ye (a) `parent_tool_use_id`/`session_id` okuma + L0…L3 seviye etiketleme, (b) çoklu worktree tail, (c) `usage` kümülatif bütçe satırı, (d) `--seviye` filtresi. Yüzey: terminal; HTML pano opsiyonel ikinci adım.
- **Token:** gözlem ek maliyeti **0** — izleyici dosya okur, LLM turu üretmez. 3 iterasyonluk iş ≈ **900k** (değişmez).
- **Zaman:** koşum başına ek gecikme ≈ 0 (2 sn polling); inşa ≈ **1 oturum / ~120 satır kod**.
- **Kalite:** G1 ✓ G2 ✓ G3 ✓ G4 ✓ G5 ✓ G6 ✓ G7 kısmi (iterasyon sınırında) G8 ✓ → **8/8'in 7,5'i**. K3 karşılığı "tek pano + seviye şeritleri" — pazardaki tek-ağaç KISMİ'sinin üstünde, Devin'in ayrı-oturum EVET'inin altında.
- **Risk (orta-düşük):** L2 (alt-ajan) etiketi yalnız tamamlanmış mesajlarda çözülür (İ-27 sert kısıtı) → alt-ajanın *içi* canlı akmaz, başlangıç/bitiş akar. İkinci risk: `parent_tool_use_id`'nin gnhf koşumlarında gerçekten dolduğu **kanıtlanmadı** (elimizdeki tek örnek dosyada tüm değerler `None`, üstelik dosya gnhf worktree'sinden değil ikame projeden) → **inşa öncesi 1 gerçek nested gnhf koşumuyla doğrulanmalı.**

### Model B — **Katman-ayrık çoklu-pane** (tmux / N ayrı tail)
Matematiksel temel: *uzamsal ayrıştırma* — korelasyon yerine fiziksel ayrım; her seviyeye ayrı pencere.
- Yapılacak: `gnhf-izle.py --worktree` zaten var; ince bir tmux açılış script'i. Kod değişikliği ≈ **0-20 satır**.
- **Token:** ek **0**. İş yine ≈ **900k**.
- **Zaman:** inşa ≈ **30 dk**.
- **Kalite:** G1 ✓ G3 ✓ G4 ✓ (fiziksel) · G2 ✗ (korelasyon insanda) G5 ✗ G6 ✗ G7 ✗ G8 ✗ → **8/8'in 3,5'i**. K3'te en güçlü görsel ayrım, K2'de eşit, ama "hangi L2 hangi L1'e ait" sorusu ekranda cevaplanmaz.
- **Risk (düşük):** hiçbir şey bozulmaz, ama 3+ pane insan dikkatini böler; ölçek 2 seviyeyi geçince okunmaz olur.

### Model C — **KARŞIT-TEMELLİ: yüzey inşa etme; seviye başına ayrı oturum aç**
Matematiksel temel: *iç-içeliği düzleştirme* — nesting'i N paralel düz koşuma çevir; gözlem yüzeyi zaten insanın oturduğu chat'tir. Bu model İB-66'nın hipotezini reddeder: "sorun gözlem aracı eksikliği değil, iç-içe koşma tercihi."
- Yapılacak: **hiçbir kod**. Her seviye kendi Claude Code oturumunda; koordinasyon devir dosyasıyla.
- **Token:** her seviye kendi bağlamını taşır → 3 seviye × ~300k taban = **~900k** + koordinasyon/devir turları ≈ +%20-25 → **~1,1M**. Model A'ya göre **+200k (+%22)**.
- **Zaman:** duvar-saati paralellikle düşebilir, ama insan dikkati 3'e bölünür ve devir dosyaları elle yazılır → pratikte **koşum başına +1 oturum yükü**.
- **Kalite:** G1 ✓✓ (gerçek chat, en yüksek K2) G3 ✓ · G2 ✗ (seviye ilişkisi kayıtta yok) G4 ✗ G5 ✗ G6 ✗ G7 ✓ (her oturumda tam müdahale) G8 ✗ → **8/8'in 4'ü**, ama K2'de tek tam-puan.
- **Risk (yüksek):** durma-koşulu kompozisyonu tamamen elle → iç done ⊄ dış değişmez kilitlenmesi denetimsiz. İç-içelik kaybolduğu için İB-66'nın asıl sorusu (2x-nesting mekaniği) cevapsız kalır. Ayrıca m.4 yüzey kuralı: yan-oturum karar almaz.

### Karşılaştırma

| Eksen | A (tek akış + pano) | B (çoklu-pane) | C (yüzey yok, ayrı oturum) |
|---|---|---|---|
| Gözlem ek token | 0 | 0 | **+~200k / koşum (+%22)** |
| Referans iş toplamı | ~900k | ~900k | ~1,1M |
| İnşa süresi | ~1 oturum (~120 satır) | ~30 dk (~20 satır) | 0 |
| Gereksinim kapsaması (8) | **7,5** | 3,5 | 4 |
| K2 (konuşma) | yüksek | yüksek | **en yüksek** |
| K3 (seviye) | yüksek (şeritli) | orta-yüksek (fiziksel, korelasyonsuz) | düşük (düzleşir) |
| Risk | orta-düşük | düşük | **yüksek** |

**Öneri: Model A**, gerekçe: gözlem maliyeti sıfır token, 8 gereksinimin 7,5'ini kapsıyor, mevcut parçanın (`gnhf-izle.py` v0) üstüne inşa ediliyor — sıfırdan yazılmıyor (CLAUDE.md §6 "hazırı temel al"). **Ön koşul:** İ-27 kısıtı ve `parent_tool_use_id`'nin gnhf koşumlarında dolup dolmadığı, inşadan ÖNCE tek bir gerçek nested koşumla doğrulanmalı (elimizdeki örnek yetersiz). Model B, A'nın inşası beklenirken **bugün kullanılabilecek 30 dakikalık köprü**dür; ikisi çelişmez. Model C reddedilmez ama ölçüsü ayrıdır: iç-içeliğin GEREKLİ olmadığı işlerde C zaten daha ucuz bir seçenektir — İB-65'in "loop ya da pipeline" sorusuna girdi olarak bırakılır.

---

## 5. S3 — Seviye-sayım formal tanımı + prompt şablonları

### 5.1 Seviye nedir (formal)

> **Tanım.** Bir katman `L` bir SEVİYEDİR ⟺ (i) kendi yineleme sayacı `i_L` vardır ∧ (ii) kendi durma yüklemi `done_L(i_L, durum)` vardır ∧ (iii) `L`'nin gövdesi `L+1`'in TAM koşumunu (başlangıcından `done_{L+1}`'e kadar) içerir.
>
> Kısaca: **seviye = döngü-tutucu**. Sayaç ∧ durma yüklemi ∧ tam-kapsama, üçü birden.

Bizim yığında (`raporlar/2026-08-31-k010-a3-loop-1.md:19` ile uyumlu):

| Seviye | Tutucu | Sayaç | Durma yüklemi |
|---|---|---|---|
| **L0** | dış-loop (`/loop`, Monitor, cron) | tur no | tetik iptali ∨ dış koşul |
| **L1** | gnhf iterasyonu | `iteration-N` | `--stop-when` ∨ token tavanı |
| **L2** | ajan araç-döngüsü (assistant ↔ tool turları) | `num_turns` | `stop_reason` ∨ `maxTurns` |
| **L3** | tur-içi tempo (uyku/kontrol) | uyku sayacı | sayaç dolumu |

### 5.2 Hangi ekleme GERÇEK seviye ekler, hangisi eklemez

**EKLER** (üç şartı da doğurur):
1. **Alt-süreç başlatma** — prompt'a "gnhf koş" yazmak: yeni CLI koşumu, kendi `iteration` sayacı, kendi `--stop-when`. → **"Loop prompt'una 'gnhf koş' eklemek 2x nesting midir?" sorusunun cevabı: EVET**, çünkü yeni bir bağımsız (sayaç ∧ durma) çifti doğar. L0 dış-loop'un içine tam bir L1 yerleşir.
2. **Alt-ajan çağrısı** (`Agent` tool — v2.1.63'te `Task`'tan yeniden adlandırıldı, sonucu `agentId: <id>` taşır; birincil kaynak, İ-28): kendi araç-döngüsü + kendi `maxTurns`.
3. **Tekrar sayacı + kendi `done` yüklemi olan blok** — "koşul sağlanana kadar tekrarla" kalıbı.

**EKLEMEZ** (biri ya da birkaç şartı doğurmaz):
- (a) Prompt'un uzaması, adım listesi eklenmesi — **sıralı**, sayaç yok.
- (b) Aynı seviyede daha çok araç çağrısı — L2 zaten var, yenisi doğmaz.
- (c) Retry / yeniden deneme — aynı `done` yüklemi altında tekrar, yeni yüklem değil.
- (d) Kütükleme/görüntüleme katmanı eklemek (izleyici, pano) — koşum akışını tutmaz, **gözlem seviyesi ≠ döngü seviyesi**.
- (e) Aynı sayaca bağlı iç `for` — tek yineleme uzayı.

**Maliyet sonucu (çarpım kuralı):** toplam ≈ `∏_L (yineleme_L × birim_L)`. L1 birimi ölçülmüş ~300k'dır. Dolayısıyla L0'a 3 tur × L1'e 3 iterasyon = 9 × 300k ≈ **2,7M** — 500k tavanla koşulamaz; e2e715 arızası tam bu çarpımın görülmemesiydi.

### 5.3 Prompt şablonları (m.38 lojik formunda)

#### Şablon-1 — DIŞ SEVİYE: bütçe kalıtımı ∧ çarpım freni
```
TANIM: B_dış = bu seviyeye verilen token tavanı
       N     = başlatılacak iç koşum sayısı
       b_iç  = iç seviyeye devredilecek tavan
       T     = ölçülmüş iç-seviye taban maliyeti (gnhf: 300k, önbellek-okuma DAHİL)

Ö1 (ön-koşul, koşumdan ÖNCE denetlenir):
   (b_iç ≥ T) ∧ (N × b_iç ≤ 0,8 × B_dış)  →  koşuma izin ver
   ¬(N × b_iç ≤ 0,8 × B_dış)              →  koşma; N'i küçült ∨ B_dış'ı yükselt ∧ Salih'e bildir

Ö2 (kalıtım): her iç koşum ÇAĞRILIRKEN b_iç AÇIKÇA yazılır;
   ¬(tavan yazıldı) → iç koşum başlatılmaz  [varsayılan tavan devralma YASAK]

Ö3 (durma):
   done_dış ↔ (hedef_sağlandı ∨ i_dış ≥ N ∨ B_harcanan ≥ B_dış)
   B_harcanan = Σ(input + output + cache_read + cache_creation)   [önbellek-okuma DAHİL]
```

#### Şablon-2 — İÇ SEVİYE: durma-koşulu kompozisyonu ∧ kilitlenme freni
```
TANIM: Δdurum_dış(i) = i'inci iç koşumun dış seviyede ÖLÇÜLEBİLİR bıraktığı değişiklik
       (yeni dosya ∨ değişen alan ∨ ilerleyen sayaç — "rapor yazdım" beyanı SAYILMAZ)

Ö1 (bağlanma): ∀i ( done_iç(i) → Δdurum_dış(i) ≠ ∅ )
Ö2 (kilitlenme tespiti):
   ∃i ( done_iç(i) ∧ Δdurum_dış(i) = ∅ )  →  KİLİTLENME
   KİLİTLENME → iç seviye zorla durur ∧ dış seviyeye "ilerleme yok" olayı yazılır ∧ i_dış artırılmaz
Ö3 (iç done dış done'u İMA ETMEZ):
   ¬( done_iç → done_dış )   [iç bitti diye dış bitmiş sayılmaz]
Ö4 (dış durma iç'i keser):
   done_dış → ∀ açık iç koşum: iptal ∧ kısmi sonuç kütüğe yazılır
```

#### Şablon-3 — FREN KALITIMI (m.10 vakası)
```
TANIM: T = ana repoda etkin herhangi bir tel/fren (hook, kural, kanon kısıtı)

Ö1: ∀T ( T etkin →
        ( T iç koşuma AÇIKÇA bildirilir )  ∨  ( T iç koşum için devre-dışı bırakılır ) )
    ¬Ö1  →  iç koşum "habersiz tel" riski taşır  [08-30/31 vakası: m.10 commit-dili teli
            gnhf'nin Türkçe iterasyon özetine çarptı, koşum a20630'da durdu]

Ö2 (uygulama): gnhf iterasyon commit özetleri İNGİLİZCE yazılır  [Karar 84 uygulama notu]
Ö3 (fren ≠ arıza): tel çarpması kütüğe FREN olayı olarak yazılır, hata olarak değil
```

#### Şablon-4 — KÜTÜK SEVİYELERİ (gözlem sözleşmesi)
```
Ö1: ∀ kütük satırı s: s.seviye ∈ {L0, L1, L2, L3} ∧ s.parent_ref tanımlı ∨ s.seviye = L0
Ö2: s.tip = tam_mesaj  →  s.parent_ref doldurulabilir
    s.tip = token_delta →  s.parent_ref = null   [SDK sert kısıtı, İ-27 — aşılamaz]
Ö3: her iterasyon sonunda kümülatif bütçe satırı yazılır (önbellek-okuma dahil)
Ö4: ∀ seviye L: L kendi dosyasını tutar ∧ L-1'e yalnız {başladı, bitti, özet} referans satırı yazar
    [Temporal child-event-history emsali — üst kütüğün şişmesini önler]
```

---

## 6. Masa-kalemi taslağı (Salih'e karar için)

> **Masa kalemi — İB-66 / Gözlemlenebilir nested loop.** Pazar taraması bitti: 12 araç × 5 kriter matrisi kuruldu, AS-OF 2026-08-31, birincil kaynaklı, antitez + örneklem denetiminden geçti. **Hüküm KISMİ: beş kriteri birlikte karşılayan ürün YOK (0/12); darboğaz K3 — iç-içe seviyelerin ayrı canlı yüzeyi, 12 araçta yalnız 1 net karşılık (Devin) ve orada da canlılık kısmi.** Negatif bulgun ayakta, ama "hiçbiri yaklaşmıyor" biçimi iki noktada zayıfladı (Devin K3+K4, Braintrust K1+K2 — Live tail).
>
> **Karar 1 (inşa):** A (`gnhf-izle.py`'yi seviye-farkında + çoklu-koşum + bütçe-görünür yap, ~1 oturum, gözlem token maliyeti 0, 8 gereksinimden 7,5) · B (tmux çoklu-pane köprü, 30 dk, 3,5/8) · C (yüzey yok, seviye başına ayrı oturum, +%22 token, iç-içelik düzleşir). **Öneri: A**, B bugünlük köprü olarak yanında.
> **Karar 2 (ön koşul):** A'ya başlamadan önce TEK bir gerçek nested gnhf koşumu koşulup `parent_tool_use_id`'nin gerçekten dolduğu doğrulanmalı — elimizdeki örnek dosya gnhf'ye ait değil ve tüm değerleri boş.
> **Karar 3 (kural):** §5.3'teki 4 şablon (bütçe kalıtımı + çarpım freni · durma-koşulu kompozisyonu + kilitlenme · fren kalıtımı · kütük seviyeleri) tüzüğe/`core/`'a kural olarak girsin mi, yoksa emir şablonu olarak `cc/`'de mi kalsın?
> **Karar 4 (kapsama):** gnhf worktree transkriptlerinin merkezi hareket kütüğüne düşmesi ayrı İB açılsın mı (G8).
> **Not (koşum arızası):** hakem ajanı ajan-freni DURDUR eşiğinde (72. çağrı) açılamadı; hakemlik lider-ajanca maskeli koşuldu — bağımsızlık kaybı beyan edilmiştir.

---

## 7. Durma koşulu denetimi

| Emir maddesi | Durum |
|---|---|
| Kriter matrisi taramadan önce yazıldı | ✅ §0, koşum boyunca değişmedi |
| ≥10 araç matriste, birincil kaynak + AS-OF | ✅ **12 araç**, §1; 4 hücre dürüstçe `[?]` |
| "yok/var/kısmi" hükmü matristen gerekçeli | ✅ §2, **KISMİ**, 5 maddeli sütun-gerekçesi |
| Tasarım 3 model sayısal (≥1 karşıt-temelli) | ✅ §4, A/B/C; C karşıt-temelli; token×zaman×kalite×risk tabloda |
| Seviye-sayım formal tanımı | ✅ §5.1-5.2 |
| ≥2 prompt şablonu m.38 formda | ✅ §5.3, **4 şablon** |
| Masa-kalemi taslağı | ✅ §6 |
| **Eksik** | Maskeli hakem AYRI ajanla koşulamadı (ajan freni); 4 `[?]` hücre (CrewAI/Temporal/Langfuse/Phoenix K1) kapatılmadı; Model A ön koşulu (gerçek nested koşumda `parent_tool_use_id` doğrulaması) yapılmadı — inşa öncesi şart olarak masaya taşındı |
