# Araç ve Model Entegrasyonu — "sadece Claude" nasıl değişir

> **Mod:** yan-oturum (m.41) · Aileler: **A19** (model çeşitliliği: denetçi/işçi, yerel) · **A20** (hızlı çıkarım: Cerebras/Groq) · **A21** (araç ekosistemi: OpenCode, Orca ADE, MCP/ACP) + ek araç anketi
> ⚠️ **Antitez KOŞTU (2026-07-26).** Sonuç: 1 çürütme (K45), 1 daraltma (K46), **4 birincil kaynakla DOĞRULAMA** (§9c.4).

> ## ⛔ DÜZELTME KAYDI — 2026-07-26 antitez turu *(teslim SONRASI eklendi)*
> Hakemlik: `raporlar/2026-07-26-antitez-hakemlik.md` §9c.
>
> | Düzeltme | Nerede | Ne oldu |
> |---|---|---|
> | **K45** | §3.4 | *"Tek markdown katmanı paylaşılabilir"* **mutlak hâliyle çürütüldü** — kendi komşu önermeleri tarafından iç-tutarsız kılınıyor |
> | **K46** | §3.5 | Protokolde **çağıran/çağrılan ayrımı DARALDI** — `claude mcp serve` ile Claude Code **hem istemci hem sunucu** olabiliyor ⇒ rol **sabit değil** |
>
> **Ve dört iddia birincil kaynakla DOĞRULANDI** (`⊨S ⊨D`, **doküman doğrulamalı ⇒ aynı-aile şerhinden muaf**):
> - §1.5 — OpenAI-uyumlu katman üretime uygun değil ∧ önbellek yok ⇒ `platform.claude.com` birebir: *"not considered a long-term or production-ready solution"* + *"Prompt caching is not supported"*
> - §2.4-1 — genel OpenAI-uyumlu sağlayıcı **sürücü olarak kabul edilmiyor** ⇒ `llm-gateway-protocol.md`
> - §2.4-2 — **sağlayıcı değişimi önbelleği sıfırlıyor** ⇒ `prompt-caching.md`
> - §3.6 — ⭐ **kalıcı izin onayları worktree'ler arasında PAYLAŞILIYOR** ⇒ `settings.md` — *antitez bunu **güvenlik açısından önemli** diye ayrıca işaretledi*
> **Geçerlilik: 26 Temmuz 2026.** Bu ailede sürüm ve yıldız rakamları **haftalar içinde bayatlar**; yapısal bulgular (kim hangi dosyayı okuyor, izin varsayılanları, protokol yerleşimi) uzun ömürlü.
> **Tetikleyen:** Salih 07-26 — *"tool olarak sadece Claude'un kendisi ve Claude aracılığıyla oluşturulmuş ürünler yer alıyor, bunu değiştirmemiz lazım... gerekirse denetçi ChatGPT, işçi opensource model"*

---

## 0. ÖNCE BİR DÜZELTME — kendi ajanımın hatası

A19, senin sisteminde **claude-code-router'ın kurulu olduğu** sonucuna vardı ve buna dayanarak "en ucuz giriş kapısı, maliyet ~sıfır" önerisi kurdu. Gerekçesi: oturum ortamında `/root/.ccr/` dizini var.

**Carvis doğruladı: YANLIŞ.** `/root/.ccr/` bu bulut oturumunun **agent proxy**'si — README'nin ilk satırı *"Claude Code agent proxy"*, içinde yalnız CA sertifikaları var (`ca-bundle.crt`, `agent-proxy-ca.crt`, `java-truststore.p12`). `ccr` komutu **yok**, router yapılandırması **yok**.

⇒ Router önerisi hâlâ değerlendirilebilir, ama **maliyeti sıfır değil**; gerçek bir kurulum işi. Bu, dizin adından yapılan çıkarımın nasıl yanlış gidebileceğinin canlı örneği ve V26 sınıfı bir yakalama.

---

## 1. A19 — MODEL ÇEŞİTLİLİĞİ: "denetçi ChatGPT, işçi opensource" sezgisi

### 1.1 Sezgi ölçülmüş olarak DOĞRU — ama gerekçesi sandığından farklı

**Çapraz-aile doğrulama > aynı-aile doğrulama > öz-doğrulama** [K]. 37 model × 9 benchmark: *"cross-family verification is especially effective… benefits decrease as solver and verifier become more similar."* En büyük kazanç matematiksel/mantıksal/yapısal görevlerde.

⇒ Denetçiyi **başka modele** vermek yetmiyor; **başka aileye** vermek gerekiyor.

**Neden — mekanizma [K]:** öz-tercih sapması **aile düzeyine yayılıyor**. Hakem, aynı sağlayıcının akraba modellerine de not şişiriyor. ArenaHard'da modelin kendi çıktısına verdiği not sapması **−%38 ile +%90** arasında, ve sapma modelin kendi çıktısının düşük perplexity'sinden kaynaklanıyor — yani **mimari bir tercih, düzeltilebilir bir prompt hatası değil**. Daha yetenekli modeller daha güçlü öz-tercih gösteriyor.

⇒ Opus'a Sonnet denetletmek sapmayı **kısmen taşır**.

### 1.2 Ama bağımsızlık SATIN ALINAMIYOR

[K] ICML'25, 350+ model: **iki model birlikte hata yaptığında %60 oranında aynı yanlış cevapta buluşuyorlar.** Ve kritik: *"büyük ve daha isabetli modeller, mimarileri ve sağlayıcıları farklı olsa bile yüksek korelasyonlu hata yapıyor."*

⇒ Bu, bu oturumda A10'da bulunan **"9 hakem ≈ 2 bağımsız oy"** ölçümüyle **bağımsız olarak aynı yere** çıkıyor. İki ayrı çalışma, aynı sonuç — yakınsak.
⇒ **Çapraz-sağlayıcı denetçi bir kalkan değil, ikinci bir süzgeç.**

### 1.3 Jüriyi büyütme, çeşitlendir

[K] Çok-ajanlı toplulaştırmada (oylama ve tartışma, ikisinde de): **2 heterojen ajan, 16 homojen ajanı geçiyor** — 8× ajan azalması.

### 1.4 Maliyet gerekçesi ZAYIF — aile içi merdiven zaten var

[D] Fiyat (2026-07-26, $/MTok giriş-çıkış): **Opus 5 = 5/25 · Sonnet 5 = 2/10 · Haiku 4.5 = 1/5.** Önbellek okuma taban girdinin **0,1×**'i; Batch **%50**.
⇒ Opus→Haiku **5×**, Opus→Sonnet **2,5×** ucuzluk, sağlayıcı değiştirmeden.

[D] Ve Anthropic bunu resmen öneriyor: alt-ajan tanımında `model` alanı (`sonnet|opus|haiku|fable|inherit`) ve `effort` alanı var; dokümanın faydalar listesinde madde aynen: *"Control costs by routing tasks to faster, cheaper models like Haiku."*

⇒ **Çapraz-sağlayıcıya geçmenin gerekçesi tasarruf DEĞİL, hata bağımsızlığı olmalı.**

**Router rakamı da abartılı [D/K]:** RouteLLM deposu *"%85'e varan maliyet düşüşü, GPT-4 performansının %95'i korunarak"* diyor — ama bu tek benchmark'a özel. Aynı çalışmanın diğer setlerinde eşlenmiş kalitede tasarruf **MMLU'da ~%45, GSM8K'da ~%35**. Muhakeme yükü arttıkça yönlendirme kazancı düşüyor. Bizim işimiz muhakeme+araç ağırlıklı ⇒ gerçekçi bant **%35–45** `[?]`.

### 1.5 Çapraz-sağlayıcının GİZLİ maliyeti

[D] **Anthropic'in OpenAI-uyumlu katmanı üretim için ÖNERİLMİYOR** — resmî cümle: *"This compatibility layer is primarily intended to test and compare model capabilities, and is not considered a long-term or production-ready solution for most use cases."*

Somut kayıplar:
- `strict` **yok sayılıyor** ⇒ araç JSON şemaya uyma garantisi yok
- `response_format` **yok sayılıyor**
- **prompt caching desteklenmiyor** ⇒ uzun kanon bağlamı olan bir sistemde girdi maliyeti **10×'a** çıkabilir (önbellek okuma 0,1× yerine tam fiyat)
- `logprobs`, `seed`, `reasoning_effort`, `metadata` yok sayılıyor
- **desteklenmeyen alanlar hata vermeden SESSİZCE düşüyor**

⇒ Anthropic'e Anthropic API'siyle, diğerlerine kendi API'leriyle gidilmeli; çeviri bir geçit katmanının işi.

### 1.6 "Açık kaynak" ≠ "yerel" — bu ayrım kritik

[D] Aider polyglot, aynı ölçüm harness'ı:

| Model | Skor |
|---|---|
| GPT-5 (high) | **%88,0** |
| Gemini 2.5 Pro | %83,1 |
| DeepSeek-V3.2 Reasoner | %74,2 |
| Claude Opus 4 (32k thinking) | %72,0 |
| DeepSeek R1 | %71,4 |
| Qwen3 235B-A22B | %59,6 |
| **Qwen3 32B** *(tüketici donanımı sınıfı)* | **%40,0** |
| Llama 4 Maverick | %15,6 |

⇒ **Tüketici donanımında koşan sınıf %40, frontier %88.** Ama büyük açık-ağırlıklı modeller (%71–74) frontier'a yaklaşıyor — **ve onlar yerelde koşmuyor, API'den alınıyor.** "Açık kaynak" ile "yerel" iki ayrı karar; karıştırılmamalı.

**Ve uzun-ufukta açık BÜYÜYOR [K]:** araç sayısı arttıkça **%7–85**, araç yanıtı uzadıkça **%7–91**, çok-turlu konuşma uzadıkça **%13–40** performans düşüşü. Kısa-ufuk varyantında %40–50 başarı, aynı görev uzun etkileşim geçmişine gömüldüğünde **%10'un altına** düşebiliyor — hem de ilgili bilgi bağlamda dururken.

**Ek uyarı [K]:** standardize harness ile satıcı harness'ı arasındaki fark **10–30 puan**. Model kartlarındaki skorlar senin sisteminde alacağın skor değil.

### 1.7 Yerelin tartışmasız kazandığı yer

[K] **Gömme (embedding):** nomic-embed-text 137M, mxbai-embed-large 335M, Jina v5-text-small 677M. Bu boyutlar CPU'da bile koşar, ~1 GB RAM. **Yerelin en net kazandığı katman bu.**

[K] **16 GB sınıfı gerçekten koşuyor:** gpt-oss-20b, 20,9B toplam / **3,6B aktif** MoE, MXFP4 yerli nicemleme ile **~13 GB**, 16 GB bellekte 128K bağlam, Apache-2.0.

⚠️ [X] **gpt-oss-20b'nin ajanik/SWE skoru çelişkili** — bir kaynak %60,7 diyor, başkaları ~%62'yi 120b'ye atfediyor. **Bu rakama dayanarak karar verilmemeli.**

[D] **Nicemleme kalite kaybı için llama.cpp'nin KENDİ dokümanında tablo YOK** — yalnız *"can be minimized by using a suitable imatrix file"*. Üçüncü-taraf ölçümler dağınık: %1–5 · 1,6 puan · **7,8 puan** · <%1 · "ortalama %99 geri kazanım, en kötü %96". ⇒ **Kararı modele göre ver, kurala göre değil.**

### 1.8 ROL → MODEL EŞLEME

**Tasarım ilkesi:** çeşitlendirmenin getirisi maliyette değil **hata bağımsızlığında**; maliyet zaten aile içi merdivenle düşüyor. Çapraz-sağlayıcıyı **yalnız denetim rolüne** harca.

| Rol | Model | Gerekçe |
|---|---|---|
| Üst-orkestratör + kanon kararları | **Opus 5** (değişmez) | Uzun-ufuk çok-turlu iş; §1.6'daki düşüş burada en pahalı |
| **Hakem / denetçi / çelişki kapısı (m.16)** | **Farklı sağlayıcı, farklı aile** | §1.1 (çapraz-aile üstünlüğü) + §1.2 (öz-tercih aile düzeyinde) + §1.3 (2 heterojen > 16 homojen) |
| İşçi / üretici | **Sonnet 5** | 2,5× ucuz, aynı araç olgunluğu, prompt caching çalışıyor |
| Mekanik: sınıflandırma, etiketleme, commit mesajı | **Haiku 4.5** → sonra yerel 20B'yi **ölç** | 5× ucuz; dar ve tekrarlı iş |
| **Gömme / indeksleme** | **Yerel** (137M–335M) | §1.7 — en net kazanç, veri hiç çıkmıyor |
| Gizli veri dokunan iş | **Yerel** gpt-oss-20b | Aktarım riski teknik olarak sıfırlanıyor |
| **Ajanik kodlama** | **Yerelde YAPMA** | §1.6: %40 vs %88, uzun-ufukta daha kötü |

**Uygulama sırası:**
1. **Aile içi merdiven** (0 maliyet, ~1 saat): alt-ajan frontmatter'larına `model:` + `effort:`. Beklenen tasarruf %40–70 `[?]`.
2. **Tek bir çapraz-sağlayıcı denetçi** — yalnız çelişki kapısı ve rapor doğrulama. **A19'un asıl kazancı bu.**
3. **Yerel gömme** — vault indeksleme.
4. **Ölç, sonra genişlet** — yerele devredilecek her alt-görev önce ölçülür (BFCL sınıfı araç-çağırma ölçümü). Tahminle devretme.

**Kaçınılacaklar:** LiteLLM self-host (24 Mart 2026'da PyPI'a kimlik-bilgisi hasat eden zararlı sürümler yüklendi — **her yeni soyutlama katmanı yeni bir tedarik-zinciri yüzeyi**) · Anthropic'in OpenAI-uyumlu ucunu ana yol yapmak · jüriyi büyütmek.

---

## 2. A20 — CEREBRAS SORUSU: büyük ölçüde "hayır", ve tam olarak nerede "evet"

### 2.1 Öldürücü ölçüm: hız neredeyse hiçbir yere dokunmuyor

[D] Bağımsız, açık iz veri seti: gerçek Claude Code + Codex oturumları, **357.161 LLM turu, 432.510 araç kaydı, 43 geliştirici**, CC BY 4.0.

**Duvar-saati ayrışması [K]:** insan düşünme **%92,3** · araç yürütme **%4,8** · **LLM üretimi %3,3**.
(Depo README'sinin metodoloji notu bunu birinci elden doğruluyor: Claude ≈ %90, Codex ≈ %94 insan boşta-bekleme.)

⇒ **Hızlı çıkarımın dokunabileceği dilim, toplam sürenin otuzda biri.**

### 2.2 Ve iş yükünün ŞEKLİ bunu daha da kötüleştiriyor

[K] Kodlama-ajanı iş yükü: **medyan önek ~120k token, medyan çıktı ~200 token.** İz genelinde girdi çıktıyı **294× aşıyor**.

**Ajanın hesabı:** 120k önek / 200 çıktı token ise tur başına decode 2.000 t/s'de ~0,1 sn, 500 t/s'de ~0,4 sn ⇒ fark **~0,3 saniye**. Cerebras'ın ölçülen ilk-token gecikmesi ise **1,54 saniye** — farkın **beş katı**.

⇒ **4× decode üstünlüğü bu iş sınıfında ölçülemez hâle geliyor.**

**Hız rakamları (bağımsız üçüncü taraf) [K]:** gpt-oss-120b'de Cerebras ~**1.933 t/s**, Groq ~**476–493 t/s**.
⚠️ [X] Aynı model için dolaşan 2.042 ve ~3.000 rakamları var; **ölçen ve tarih belirtilmeden verilen ~3.000'i kullanma**; savunulabilir bant **1.900–2.100**.

### 2.3 Görünürdeki çelişki ve çözümü — bu ayrım önemli

Başka bir çalışma *"LLM çıkarımı toplam koşum süresinin %71–98'i"* diyor. **Çelişki gerçek değil, payda farkı:** o ölçüm **insansız benchmark koşumları**; iz verisi ise **insanın döngüde olduğu** gerçek oturumlar.

⇒ **İnsan devredeyken hız neredeyse önemsiz; ajan otonom koşarken model süresi gerçekten baskın.**

### 2.4 Üç ek engel

1. **[D] Claude Code rastgele OpenAI-uyumlu sağlayıcıyı sürücü model olarak KABUL ETMİYOR.** Desteklenen liste: Anthropic API/Console, Bedrock, Claude Platform on AWS, Vertex, Foundry + bu protokolleri konuşan geçitler. Genel OpenAI-uyumlu uç **listede yok**.
   ⇒ Cerebras/Groq bu sisteme ancak **araç seviyesinde** girer: script ya da MCP sunucusu olarak **taşeron**, sürücü değil.
2. **[D+K] Sağlayıcı değiştirmek önek önbelleğini kaybettiriyor.** Turların **%95,7'si** önbellek isabeti alıyor. Bir turu başka sağlayıcıya taşımak 120k token'lık öneği **soğuk prefill'e** zorlar — kazanılan decode süresinden büyük olma ihtimali yüksek.
   ⇒ **Hızlı çıkarım konuşmanın ortasına serpiştirilmemeli**, kendi başına duran işlere verilmeli.
3. **[K] Kalite uçurumu sağlayıcıda değil, model ailesinde.** SWE-bench Pro: Claude Sonnet 4 **42,70 ±3,59** · gpt-oss-120b **16,20 ±2,67** (~2,6×).
   ⇒ *Hızlı sağlayıcıya geçmek "aynı işi daha hızlı" değil, "farklı bir zekâ sınıfıyla daha hızlı" demek.*

### 2.5 Yapısal farklar (birincil SDK'lardan [D])

| | Cerebras | Groq |
|---|---|---|
| API yüzeyi | **4 uç** (`chat/completions`, `completions`, `models`×2) | + **Batch API + Files API** |
| **Batch** | **YOK** | **VAR** — 24h–7d penceresi, %50 indirim |
| Araç çağırma | `tools`, `tool_choice`, `parallel_tool_calls` ✓ | ✓ |
| `service_tier` | auto/default/flex/priority | auto/on_demand/**flex**/performance |
| Model listesi | SDK'da enum yok (katalog kapalı) | SDK'da enum sabit; **hepsi açık-ağırlıklı** |

[D] **Cerebras entegrasyonunun gizli tuzağı:** SDK istemcisi kurulurken TTFT'yi düşürmek için `/v1/tcp_warming`'e istek atılıyor ve resmî uyarı *"istemciyi tekrar tekrar kurarsanız performans kötüleşir"* diyor. Her araç çağrısında yeni istemci yaratan naif entegrasyon, satın alınan hızın bir kısmını geri verir.

[K] **Groq'un flex katmanı indirim DEĞİL:** 10× yüksek hız limiti veriyor ama fiyat on_demand ile aynı — bir **kapasite kanalı**.

### 2.6 HANGİ İŞ NEREYE

**Tek kural: kararı çıktı-token sayısı ile "birinin gerçekten beklemesi" belirler.**

| İş | Nereye | Gerekçe |
|---|---|---|
| Kodlama ajanı ana döngüsü | **Claude, değiştirme** | Decode farkı ~0,3 sn, TTFT bunun 5 katı, önbellek kaybı bunu da aşar, kalite 2,6× |
| İnsanın döngüde olduğu her etkileşim | **Claude** | Sürenin %92,3'ü zaten insan düşünmesi |
| **Ajanın kendi bekleme döngüleri (senin %35'in)** | **Hiçbir sağlayıcı — orkestrasyon düzeltmesi** | O süre üretim değil; token/sn ile satın alınamaz, **bedava** kazanılır |
| Uzun serbest üretim (taslak, toplu çeviri, büyük diff, sentetik veri) | **Hızlı çıkarım** | Tek yer ki çıktı token'ı yüksek → 4× üstünlük süreye dönüşür |
| Yüksek akıl-yürütme bütçeli koşum | **Hızlı çıkarım** | Akıl yürütme token'ları da çıktı token'ıdır |
| Gecelik wiki üretimi, toplu sınıflandırma, eval koşumları | **Batch (%50)** | Kritik yolda kimse beklemiyor; kaliteyi de korur |
| Ucuz ön-filtre / eleme | Hızlı çıkarım, küçük model | llama-3.1-8b $0,05/$0,08 |
| Kişisel veri | **Yerel** | — |

> **Operasyonel kural: çıktı token'ı binlerle ölçülüyorsa hızlı çıkarıma, kimse beklemiyorsa batch'e, geri kalan her şey Claude'da kalır.**

---

## 3. A21 — ARAÇ EKOSİSTEMİ

### 3.1 Orca ADE doğrulandı — ve zaten kendi wiki'mizde var

[D] **"Orca ADE" = `stablyai/orca`.** README: *"The AI Orchestrator for 100x builders. Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place."* MIT, v1.4.157-rc.0, ~29,3k ★, **günlük sürüm**.

**Orca bir ajan DEĞİL — ajanların yaşadığı EV.** Kendi modeli, talimat dosyası, promptu yok. **29 CLI ajanını** destekliyor. Çekirdek model: **1 görev = 1 git worktree = 1 ajan.**

⚠️ [D] **Sistemin kendi kanonunda zaten var:** `wiki/orca.md`, 2026-07-09'da yazılmış, o gün ~13k yıldız kaydedilmiş (bugün ~29,3k → 3,5 ayda **2,3×**). Ve sayfanın kendi uyarısı bugün de geçerli: *"Senin darboğazın hiçbir zaman araç eksikliği olmadı; gönderilmiş çıktı."*

[K] **İsim karışıklığı gerçek:** Microsoft'un Orca dil **modeli** · Orca Security · GNOME Orca ekran okuyucu (Linux'ta `orca` komut çakışması) · Letta ADE (aynı kısaltma, farklı iş). Ayrıca `stablyai/orca` README'sini birebir kopyalayan **klon depolar** var ⇒ tedarik zinciri riski, yalnız `stablyai/orca`.

### 3.2 OpenCode — ve ASIL RİSK

[D] MIT, **v1.18.5 (24 Tem 2026)**, ~185–190k ★ [X], **haftada 1–2 sürüm**. Depo `sst/opencode` → `anomalyco/opencode`'a geçmiş.

**Hem terminal ajanı hem sunucu, ve mimari olarak zorunlu şekilde:** *"When you run `opencode` it starts a TUI and a server. Where the TUI is the client that talks to the server."* 75+ sağlayıcı, MCP istemcisi, Bun çalışma zamanı.

⚠️ **[D] ASIL RİSK — izin modeli asimetrisi.** OpenCode dokümanı açıkça: *"OpenCode starts from permissive defaults: **Most permissions default to `allow`**."* Yalnız `doom_loop`, `external_directory` ve `.env` okuması kısıtlı. Ve `--auto` bayrağı tüm onayları atlar.

⇒ **Bu deponun Dilim-1 yapısal kilidi (`Edit(core/**)`, `Edit(CLAUDE.md)`, `Edit(.claude/**)` deny) YALNIZ Claude Code'da geçerlidir.** OpenCode aynı depoda açılırsa **kilit yoktur.**

⚠️ **[D] Ve yeniden yazım sessizce hatalı olabilir:** OpenCode'da *"`*` matches zero or more of any character"* — yani `/` dahil. Claude Code glob kullanıyor (`**` ayrı anlam taşır). `core/**` → `core/*` çevirisi **kilitte delik bırakabilir**. Bu, elle yapılan ve **sessiz başarısız olan** bir işlem.

### 3.3 Ekosistemin durumu — iki araç kimlik değiştirmiş, biri ölmüş

| Araç | Durum |
|---|---|
| **Continue** | ⚠️ **ÖLÜ.** *"no longer actively maintained and is read-only for all users."* 35,1k ★ ama Cursor tarafından satın alındı [K]. **Kurmayın.** |
| **OpenHands** | **PİVOT ETTİ.** Artık kodlama ajanı değil, *"self-hosted developer control center for coding agents"* — Claude Code/Codex/Gemini'yi ACP ile koşuyor. **Orca'nın rakibi, Claude Code'un değil.** 82,1k ★ ama kod `software-agent-sdk` (930 ★) ve `agent-canvas` (223 ★) depolarına taşınıyor ⇒ **82,1k miras sinyali.** |
| **Goose** | **Linux Foundation'a (AAIF) bağlandı.** 51,7k ★, **220 açık konu** — listenin en temiz oranı. Haftalık sürüm. |
| **Aider** | **DURMUŞ.** Son sürüm Şub 2026, son commit May 2026, **442 açık PR**, **MCP YOK** (PR birleştirilmeden kapatıldı). |
| **Codex CLI** | 101,5k ★, **5k+ açık konu** (en yüksek yük). ⚠️ `wire_api = "chat"` artık **sert hata** veriyor — üçüncü-taraf sağlayıcı Responses API konuşmak zorunda. |
| **Cline** | 65,1k ★, 646 konu, bugün commit'li. **Claude Code'un en güçlü işlevsel ikizi**; farkı yüzey genişliği (IDE + CLI + Kanban + SDK). |
| **Gemini CLI** | 106,2k ★ (en yüksek), 873 konu. **Ücretsiz katman: 60 istek/dk, 1.000 istek/gün, 1M bağlam** + Google Search grounding. **En düşük giriş maliyeti** (`npx`, sıfır kurulum). |

⚠️ **Yıldız sayısı olgunluk ölçütü olarak BOZUK — ve kanıtı elimizde:** Continue 35,1k ★ ile öldü; OpenHands 82,1k ★ ile kategori değiştirdi; Aider 47,7k ★ ile durdu; buna karşılık Goose 220 açık konuyla en temiz hijyene sahip.
⇒ **Olgunluk ölçütü: son commit tarihi × sürüm kadansı × açık-konu/PR birikimi.** Bu üçlüde sıralama tamamen değişiyor.

### 3.4 ⭐ ENTEGRASYON KATMANI — hüküm

**Soru: tek bir markdown talimat katmanı birden çok aracı besleyebilir mi?**

**EVET — okunan katman için kanıtlanmış; yürütülen katman için HAYIR.**

**Kanıtlanan taraf — üç bağımsız [D], üç ayrı üreticiden:**
1. **[D] Anthropic köprüyü resmen belgeliyor:** *"Claude Code reads `CLAUDE.md`, not `AGENTS.md`. If your repository already uses `AGENTS.md`... create a `CLAUDE.md` that imports it."* İki yol: `@AGENTS.md` içe-aktarımı veya `ln -s AGENTS.md CLAUDE.md`.
2. **[D] OpenCode köprüyü TERS yönde YERLEŞİK sunuyor:** *"For users migrating from Claude Code, OpenCode supports Claude Code's file conventions as fallbacks: Project rules: `CLAUDE.md`... Global rules: `~/.claude/CLAUDE.md`... Skills: `~/.claude/skills/`"*
3. **[D] Gemini CLI kaynak kodu:** `context.fileName` *"Accepts either a single string or an array of strings"* ⇒ `["GEMINI.md","AGENTS.md","CLAUDE.md"]` yazılabilir.

⇒ Üç büyük üretici bağımsız olarak aynı sonuca varmış: **talimat katmanı tek olmalı, köprü araç tarafında kurulmalı.**

**[D] AGENTS.md uyumluluk listesinde 23 araç var — ve Claude Code YOK.** (Kaynak kodundan birebir çıkarıldı.) Ama Anthropic köprüyü belgelediği için bu bir engel değil.

**[D] Beceriler bedava taşınıyor:** OpenCode altı yerden `SKILL.md` okuyor ve ikisi **`.claude/skills/`** ile **`~/.claude/skills/`**. ⇒ Bu sistemdeki 4 beceri (`atlas-kosum`, `celiski-kapisi`, `karar-hatti`, `karar-modeli`) OpenCode'a **sıfır taşıma maliyetiyle** görünür.

**⚠️ Çürüyen taraf — ve en tehlikeli kısım:**

| Taşınan | Taşınmayan |
|---|---|
| CLAUDE.md (geri-düşüş yoluyla) | `.claude/agents/` — alt-ajan tanımları |
| 4 beceri (`.claude/skills/`) | `.claude/hooks/` — 2 kanca |
| | `settings.json` izin bloğu — **Dilim-1 yapısal kilidi** |

⇒ **Paylaşılabilir yüzey %100, yürütülebilir yüzey %0.** Ve taşınmayan şey **izin kilidinin ta kendisi**.

> **[K45 · antitez ÇÜRÜTMESİ — mutlak hâl düşer]** *"Tek markdown katmanı paylaşılabilir"* iddiası **mutlak biçimde** yazılmıştı ⇒ **çürütüldü**, ve çürüten şey **kendi komşu önermeleriydi**: hemen yukarıdaki tablo zaten *"yürütülebilir yüzey %0"* diyor.
> ⇒ Kapsam sabitlenir: **`paylaşılabilir(OKUNAN_KATMAN) = %100`** ∧ `paylaşılabilir(YÜRÜTÜLEBİLİR_KATMAN) = %0`.
> ⇒ ⚠️ **Bu, düzeltmenin en rahatsız edici tarafı:** rapor doğru hükmü **zaten vermişti** (§3.4'ün kendi tablosu), ama **iddia listesine mutlak hâliyle** yazılmıştı. Yani hata analizde değil, **özetleme adımındaydı** — iddia listesi raporun kendisinden zayıf çıktı.
> ⇒ Pratik sonuç değişmiyor: `CLAUDE.md` paylaşılır, **izin kilidi paylaşılmaz**.

### 3.5 Üçüncü protokol: ACP — asıl fay hattı

**[D] MCP fiili standart, ajan→araç yönünde.** OpenCode `@modelcontextprotocol/sdk` yamalıyor, Goose 70+ eklentiyi MCP ile bağlıyor, Cline `cline mcp` sunuyor, Codex hem istemci hem **sunucu**. **7 araçtan 6'sında var** ⇒ ayırt edici gücünü yitirdi.

**[D] ACP (Agent Client Protocol) editör↔ajan yönünü çözüyor** ve asıl ayrımı o yapıyor:
- **Goose ve OpenHands, Claude Code'u ÇAĞIRIYOR.** Goose'un `claude-acp` sağlayıcısı Claude Code'u **goose'un model sağlayıcısı** olarak koşuyor — **mevcut Claude aboneliğini kullanarak, token başına API ücreti olmadan.** Ve *"ACP providers pass goose extensions through to the agent as MCP servers"* ⇒ goose'un eklenti kütüphanesi Claude Code'a MCP sunucusu olarak aktarılıyor. **Bu örtüşme değil, KATMANLAMA.**
- **Cline ve Gemini CLI kendilerini ACP ajanı olarak SUNUYOR** — yani çağrılan taraf.

⇒ **Doğru soru "MCP destekliyor mu" değil, "ACP'de hangi yönde duruyor: çağıran mı, çağrılan mı".**

> **[K46 · antitez daraltması — rol sabit değil]** Bu çerçeve, her aracın **sabit bir yön** taşıdığını varsayıyordu ⇒ **daraldı**. `claude mcp serve` ile **Claude Code hem istemci hem sunucu** olabiliyor; Codex için de aynısı zaten kayıtlı (§3.5'te *"hem istemci hem sunucu"* yazılı).
> ⇒ Doğrusu: **yön bir araç özelliği değil, bir KURULUM tercihidir.** Aynı araç, farklı kurulumda farklı yönde durur.
> ⇒ **Soru yeniden yazılır:** *"bu araç hangi yönde duruyor"* değil, **"bu kurulumda hangi yönde durmasını istiyorum"**. Ayrımın pratik değeri **artıyor** — çünkü artık bir kısıt değil, bir **tasarım kaldıracı**.

**[K] A2A bu ekosistemde YOK.** Taranan hiçbir kodlama aracının dokümanında geçmiyor.

### 3.6 Araç eklemenin maliyeti

**[D] Yapısı alt-ajan izolasyonuyla aynı, ama para yerine insan-zamanıyla ödeniyor.** A7'de ölçülmüştü: alt-ajan ana pencerede 5.680 token tasarruf, kendi başlangıç yükü 3.790 ⇒ ~1,5:1. Araç çeşitliliğinde tekrarlanan yük **talimat katmanının bakımı**.

**[D] Sürüm temposu = bakım yükü:** OpenCode haftada 1–2, Orca **günlük**. İkisini eklemek haftada ~3–9 sürüm-olayı izlemek demek.

**[D] MCP eklemek de bedava değil.** OpenCode'un kendi uyarısı: *"MCP servers add to your context... Certain MCP servers, like the GitHub MCP server, tend to add a lot of tokens and can easily exceed the context limit."* ⇒ **Her koşumda ödenen sabit bağlam vergisi.**

**[D] Ve net-negatif eşiği için somut kanıt var:** Orca'nın varlık nedeni paralel worktree, ama **Claude Code bunu artık yerleşik yapıyor** — `claude --worktree`, alt-ajanlar için `isolation: worktree`, `.worktreeinclude`, `worktree.baseRef`, agent-view.
⇒ **Eklenecek aracın çekirdek yeteneği mevcut aracın yerleşik yeteneğiyle örtüşüyorsa, ekleme net negatiftir.**

⚠️ **[D ∧ ⊨S] Worktree'ler paylaşılan durum taşıyor — ANTİTEZ DOĞRULADI:** *"A worktree gets its own files and branch, but it shares the repository's `.git` directory, project-scope plugins, and **saved permission approvals** with the main checkout."* ⇒ Bir worktree'de verilen *"bir daha sorma"* onayı **tüm paralel ajanları bağlar**.
> **⭐ Antitez bu maddeyi ayrıca GÜVENLİK AÇISINDAN ÖNEMLİ diye işaretledi.** Doğrudan sonuç: paralel worktree'lerde koşan ajanlar **izin yüzeyini paylaşır** ⇒ birinde verilen kalıcı onay, ötekiler için de **sessizce** geçerlidir. Dilim-1 kilidi `settings.json` deny ile yapısal olduğu için ayakta; ama **kalıcı onayla genişletilen her izin, tüm paralel yüzeye yayılır**.

⚠️ **[D] Symlink tuzağı — §3.4'teki tavsiyeyle çarpışıyor:** *"Claude Code refuses to create a worktree when `.claude`, `.claude/worktrees`, or the worktree directory itself is a symlink."* AGENTS.md↔CLAUDE.md symlink'i **güvenli** (dosya seviyesi); ama `.claude/` **dizinini** symlink'lemek worktree'leri kırar.

---

## 4. SENTEZ — "hangi tooldan ne kadar"

### 4.1 Sıfır maliyetli, bugün yapılabilir — ve KANITLANMIŞ

Ek bir ajan koşumu bu soruyu üç bağımsız kanıt hattıyla kapattı.

**Kanıt 1 — Anthropic symlink'i RESMEN belgeliyor.** Birebir:
> *"**Claude Code reads `CLAUDE.md`, not `AGENTS.md`.** If your repository already uses `AGENTS.md` for other coding agents, create a `CLAUDE.md` that imports it so both tools read the same instructions without duplicating them."*
> ```
> @AGENTS.md
> ```
> *"**A symlink also works** if you don't need to add Claude-specific content:"*
> ```bash
> ln -s AGENTS.md CLAUDE.md
> ```
> *"On Windows, creating a symlink requires Administrator privileges or Developer Mode, so use the `@AGENTS.md` import instead."*

**Kanıt 2 — vahşi doğada ölçüldü (32 depo tarandı).** Ajan symlink'i `raw.githubusercontent.com`'un davranışıyla tespit etti (symlink çekildiğinde içerik olarak **hedef dosya adı** döner):

| Desen | Depolar |
|---|---|
| **A — symlink** (`CLAUDE.md` → `AGENTS.md`) | modelcontextprotocol · vercel/next.js · openai/openai-agents-python · PostHog · cal.com · turso |
| **A tersi** (`AGENTS.md` → `CLAUDE.md`) | **oven-sh/bun** · **sst/sst** |
| **B — `@import`** | block/goose (`@AGENTS.md`, 10 bayt) · getsentry/sentry · cloudflare/workers-sdk |
| **C — kopyalama (ANTİ-DESEN)** | langchain-ai/langchain: iki dosya **md5 birebir aynı** (18.830 bayt), elle senkronda tutuluyor |

⭐ **En güçlü artefakt — `prisma/prisma`: BİR dosya, ÜÇ ad.**
```
AGENTS.md  = 34.378 bayt gerçek dosya
CLAUDE.md  → symlink "AGENTS.md"   ┐ md5'leri
GEMINI.md  → symlink "AGENTS.md"   ┘ birebir aynı
```
Tek kaynak → Claude Code + Codex/Cursor/VS Code + Gemini CLI. **Senin sorunun bu depoda çözülmüş halde duruyor.**
Ve `huggingface/transformers` kanonik dosyayı gizli dizinde tutuyor: `AGENTS.md → .ai/AGENTS.md`, `CLAUDE.md → .ai/AGENTS.md` — kök temiz kalıyor.

**Kanıt 3 — araçlar zaten birbirinin dosyasını okuyor.** GitHub Copilot cloud agent 4 ad okuyor (`copilot-instructions.md` + `AGENTS.md` + `CLAUDE.md` + `GEMINI.md`) · VS Code 4 ad · OpenHands 5 ad (**büyük/küçük harf duyarsız**) · Continue 4 ad · Cline 4 ad · Goose 2 ad · OpenCode `AGENTS.md` → yoksa `CLAUDE.md`, hatta `~/.claude/CLAUDE.md`.
⇒ **Birleşme sen bir şey yapmadan da oluyor.** Symlink yalnız kalan boşluğu — Claude Code'un katı `CLAUDE.md` ısrarını — kapatıyor.

**JARVIS için öneri — yön önemli.** Anthropic `AGENTS.md`'yi kanonik alıp `CLAUDE.md`'yi link yapıyor; ama senin tüzüğün her yerde `CLAUDE.md`'ye atıf veriyor ve o dosya kanonun parçası. **Kanonu bozmayan yön:**
```bash
ln -s CLAUDE.md AGENTS.md     # bun/sst deseni — CLAUDE.md kanonik kalır
```
Bu tek komut **23 aracın okuyabileceği bir yüzey açar ve hiçbir mevcut davranışı değiştirmez.** Windows'ta symlink yönetici hakkı istediği için alternatif: `AGENTS.md` içine tek satır `@CLAUDE.md`.

⚠️ **Sınır — semantik uyum ≠ sözdizimsel uyum.** Dosya okunur, ama Claude Code'un `@import`'u, `.claude/rules/` frontmatter'ı, Cursor'ın `.mdc` frontmatter'ı **taşınmaz**. Ortak dosya **düz markdown** olmalı; araca özgü olan ayrı kalmalı.

⚠️ **Ve uyumluluk listesi şişirilmiş [D]:** AGENTS.md'nin resmî listesinde **Aider var, ama Aider AGENTS.md'yi otomatik OKUMUYOR** — depo genelinde sıfır eşleşme. Listedeki bağlantı elle `--read` yapılan bir sayfaya çıkıyor. **Listeye güvenme, kaynağa bak.**

### 4.1b Protokol katmanı tek çatı altında birleşti — ve bu yapısal bir bulgu

**[D] MCP artık Anthropic'in değil.** 9 Aralık 2025'te **Linux Foundation altındaki Agentic AI Foundation'a (AAIF)** bağışlandı. Kurucular: **Anthropic, Block, OpenAI**; destekçiler: Google, Microsoft, AWS, Cloudflare, Bloomberg.

Ve kritik cümle: *"MCP joins two other founding projects: **goose** by Block and **AGENTS.md** by OpenAI as founding projects."*

⇒ **Protokol katmanı (MCP) ile talimat katmanı (AGENTS.md) rakip değil — aynı vakfın kurucu projeleri.** Bu, tek-talimat-katmanı stratejisinin uzun ömürlü olacağının en güçlü yapısal sinyali.

**Ekosistem ölçüldü [D]:** ajan resmî registry API'sini **kendisi sayfaladı** (591 sayfa): **18.566 benzersiz MCP sunucusu**, 59.043 toplam kayıt. Mayıs 2026'da ~9.652'ymiş ⇒ iki ayda **~2×**.
**12 araçtan 11'i MCP istemcisi.** Tek istisna Aider.

**[D] A2A senin problemin için YANLIŞ KATMAN.** v1.0.1, Linux Foundation, 8 şirketlik TSC, 150+ kuruluş — gerçek ve büyük. Ama kendi dokümanı MCP'yle ilişkisini *"distinct but highly complementary"* diye tanımlıyor: **MCP = araçlar ve kaynaklar, A2A = uzak/opak ajanlar.** Ve incelenen **12 kodlama aracından hiçbiri A2A konuşmuyor**. Senin senaryon tek makinede, aynı dosya sistemine bakan yerel ajanlar. **Yok say.**

⇒ Bakılacak üçüncü protokol A2A değil, **ACP** (§3.5).

### 4.2 Düşük maliyetli, yüksek getirili

| Adım | Ne | Neden |
|---|---|---|
| 1 | **Alt-ajan `model:`/`effort:` merdiveni** | 0 maliyet, %40–70 tasarruf `[?]`, Anthropic'in kendi önerisi |
| 2 | **Tek çapraz-aile denetçi** (çelişki kapısı + rapor doğrulama) | A19'un asıl kazancı; çapraz-aile > aynı-aile ölçülmüş |
| 3 | **Yerel gömme** (Ollama, 137M–335M) | Yerelin tartışmasız kazandığı tek katman |
| 4 | **Gemini CLI ikinci görüş için** | Ücretsiz katman (1.000 istek/gün) + `npx` sıfır kurulum + Google Search grounding — bağımsız ikinci-görüş için en ucuz kapı |

### 4.3 Şartlı — koşul sağlanırsa

- **Goose:** yalnız *katmanlama* için. `claude-acp` ile Claude Code'u alta koyar, kendi eklenti kütüphanesini MCP olarak geçirir, **mevcut aboneliği kullanır**. Kod-dışı otomasyon ihtiyacın doğarsa mantıklı; yoksa değmez.
- **OpenCode:** yalnız çok-sağlayıcı ihtiyacı gerçekten doğarsa. ⚠️ **Girmeden önce izin bloğunu elle çevir ve glob anlambilimini test et** — yoksa `core/` kilidi delinir.

### 4.4 Şu an ALINMAZ — gerekçeli

| Araç | Neden |
|---|---|
| **Continue** | Ölü. Salt-okunur. |
| **Orca ADE** | Çekirdek değeri (paralel worktree + panel) Claude Code'da **yerleşik**. Ve kendi wiki'mizin uyarısı: *"darboğazın hiçbir zaman araç eksikliği olmadı; gönderilmiş çıktı."* Günlük sürüm temposu ayrı bir bakım vergisi. |
| **OpenHands** | Orca ile aynı işi yapıyor; **ikisini birden almak anlamsız**. Docker + Node 22.12 + uv — listenin en pahalı kurulumu. |
| **Aider** | Durmuş, **MCP yok** ⇒ ekosisteme bağlanamıyor. |
| **Cline** | Claude Code'un en güçlü ikizi; IDE'de yaşamıyorsan katma değer yok. |
| **Codex CLI** | Doğrudan ikiz; ChatGPT aboneliği yoksa anlamsız. |
| **Cerebras/Groq (ana döngü için)** | §2 — decode farkı ölçülemez, önbellek kaybı bunu aşar, kalite 2,6× düşer. **Yalnız uzun-üretim işlerine.** |
| **LiteLLM self-host** | Tedarik-zinciri saldırısı emsali + tek kişilik sistemde bakım yok. |

### 4.5 Ve tekrar edilmesi gereken tek uyarı

Bu oturumun kendi kanonunda duran cümle, üç ailenin de sonucunu özetliyor:

> *"Senin darboğazın hiçbir zaman araç eksikliği olmadı; gönderilmiş çıktı."*

A21'in ölçümleri bunu çürütmüyor, **destekliyor**: eklenebilecek 7 araçtan biri ölü, ikisi kategori değiştirmiş, üçü Claude Code'un ikizi, biri yerleşik yeteneği tekrarlıyor. Gerçek kazanç araç sayısında değil, **model rolünün ayrışmasında** (§1.8) ve **doğrulama katmanının dışsallaşmasında** (kod-entegrasyonu raporu §4).

---

## 5. AÇIK BORÇLAR

1. ~~A19, A20, A21 için Aşama 2 (antitez) koşulmadı~~ → **KAPANDI 2026-07-26.** Sonuç: **1 çürütme** (K45, mutlak paylaşılabilirlik), **1 daraltma** (K46, protokol yönü sabit değil), **4 birincil kaynakla doğrulama** (OpenAI-uyumlu katmanın üretime uygunsuzluğu · sürücü model kısıtı · sağlayıcı değişiminin önbelleği sıfırlaması · **worktree'lerin izin onaylarını paylaşması**).
   ⚠️ Doğrulanan dördü **doküman doğrulamalıdır** ⇒ aynı-aile şerhinden **muaftır**.
2. **A19'un en önemli açık sayısı:** aynı-aile ile çapraz-aile doğrulama arasındaki farkın **puan cinsinden büyüklüğü**. Sıralama doğrulandı, büyüklük PDF'te kaldı.
3. **Çapraz-sağlayıcıya geçince prompt performansının ne kadar düştüğü ÖLÇÜLMEMİŞ.** Anthropic "prompt'unu yeniden yazmayı düşün" diyor ama rakam vermiyor. **Planın gizli maliyeti burada.**
4. **Cerebras'ın resmî fiyatı ve hız limitleri doğrulanamadı** — kullanılan rakamlar ~8 ay eski üçüncü-taraf veritabanından. **Karar öncesi teyit edilmeli.**
5. **"token/s artışı ajan görev süresini X% kısaltır" biçiminde kontrollü deney YOK.** §2.2'deki hesap Carvis/atlas türetmesi, ölçüm değil.
6. **Nicemleme kalite kaybının tarafsız referans tablosu bulunamadı.**
7. **Araç eklemenin net getirisi üzerine dış ampirik çalışma YOK** — §3.6'daki hüküm yetenek-örtüşmesi argümanına dayanıyor.
8. ~~A22–A24 koşuyor~~ → **KAPANDI**; `raporlar/2026-07-26-tech-stack-atlas.md` olarak teslim edildi.
9. **Yeni (K46'dan):** `claude mcp serve` ile Claude Code'un **sunucu tarafında** durduğu bir kurulum **denenmedi**. §3.5'in ACP çerçevesi artık bir kısıt değil **tasarım kaldıracı** olduğuna göre, bu denenmeye değer bir yön.
