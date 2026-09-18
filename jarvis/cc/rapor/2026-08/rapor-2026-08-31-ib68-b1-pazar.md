# Pazar-Doğrulama Raporu — B68 aile B1 (rejim: maliyet-öncelikli)

**AS-OF:** 2026-08-31 · **Model:** sonnet · **Ajan:** pazar-doğrulama işçi (WebSearch, 8 sorgu, bütçe içi) · **Kapsam:** B68-1, B68-5, B68-7 — rakip + pazar sinyali taraması

---

## B68-1 — Gözlemlenebilir nested-loop koşucusu

**Arama sorguları (birebir):**
1. `LangGraph Studio AgentOps Langfuse Arize Phoenix Braintrust agent observability nested loop trace 2026`
2. `AutoGen Studio Claude Agent SDK Temporal agent visual debugger conversation level trace`
3. `Devin Manus LangSmith pricing plans agent observability market 2026`
4. `Langfuse pricing Braintrust pricing Arize Phoenix pricing open source funding 2026`

**Rakip/muadil listesi:**
- **LangGraph Studio** — LangChain'in kendi ekosisteminde node-bazlı state-diff, tam yürütme grafiği, model+araç çağrı ayrıştırması, model-versiyonuna karşı replay sunuyor (arama-sonucu: laminar.sh, latitude.so).
- **AgentOps** — Çoklu-çerçeve ajan hata ayıklama; session replay (LLM/araç çağrısı görsel takibi), zaman-yolculuğu debug, denetim izi. GitHub ~5.6k yıldız (arama-sonucu: inference.net, github.com/AgentOps-AI).
- **Langfuse** — Prompt iterasyonu odaklı; self-host sınırsız kullanım ücretsiz (arama-sonucu: marktechpost.com). 2026-01'de Clickhouse tarafından satın alındı.
- **Arize Phoenix** — Açık kaynak, Elastic License 2.0 altında ücretsiz self-host; ticari üst katman Arize AX (arama-sonucu: laminar.sh, arize.com).
- **Braintrust** — En cömert ücretsiz kademe: 1M trace span/ay, sınırsız kullanıcı, 10K eval run (arama-sonucu: marktechpost.com, braintrust.dev).
- **AutoGen Studio** — Çoklu-ajan iş akışlarını görsel kurma/test UI'ı; OpenTelemetry entegrasyonu var (arama-sonucu: agentwiki.org, technspire.com).
- **Claude Agent SDK** — Kendi başına gözlemlenebilirlik UI'ı sağlamıyor; Laminar/LangSmith/MLflow üçüncü-parti entegrasyonlarıyla trace ediliyor (arama-sonucu: laminar.sh/docs, medium.com/@anukriti-ranjan).
- **Temporal** — Doğrudan ajan-konuşma trace aracı DEĞİL; Mastra gibi çerçeveler ajanı Temporal-benzeri workflow olarak çerçeveliyor (arama-sonucu: morphllm.com) — B68-1'e dolaylı rakip, [?] doğrudan çakışma zayıf.
- **Devin** — Otonom yazılım mühendisi ürünü (ticket→PR); gözlemlenebilirlik değil üretim aracı, dolaylı temas (arama-sonucu: arize.com).
- **Manus** — "Hands-off deliverable" ürünü olarak tanımlanıyor; B68-1 kapsamına doğrudan rakip kanıtı bulunamadı [?].
- **LangSmith** — LangChain/LangGraph takımları için doğal seçim; trajectory evaluation, üretim izleme (arama-sonucu: digitalapplied.com, inference.net).

**PAZAR SİNYALİ:**
- Ücretli plan MEVCUT: AgentOps (Pro $/ay var — tutar yazılmıyor, sadece varlık), Langfuse (Core/Pro katmanlı ücretli plan var), Braintrust (Pro ücretli plan var), Arize AX (ücretli üst katman var), LangSmith (Plus + kullanım-bazlı ücretli plan var).
- Ücretli plan YOK / sinyalsiz: Arize Phoenix çekirdek ürünü (açık kaynak, ücretsiz self-host) — ticari üst katman ayrı marka (Arize AX) altında.
- GitHub yıldız hacmi: AgentOps ~5.6k yıldız (arama-sonucu, tek kaynak doğrulaması yapılmadı) — DESTEKLİ (tek arama-sonucu kaynağı).
- Funding/satın-alma haberi: Langfuse'un Clickhouse tarafından satın alınması (2026-01) — DESTEKLİ (arama-sonucu, birincil kaynak açılmadı).
- İş ilanı sınıfı sinyal: aranmadı, [?] bütçe dışı kaldı.

**Rekabet yoğunluğu: DOYGUN.** En az 8 isimli oyuncu (LangGraph Studio, AgentOps, Langfuse, Phoenix, Braintrust, LangSmith, AutoGen Studio + OTel-tabanlı araçlar) aynı "ajan trace/observability" alanında aktif, çoğu ücretli katmanlı, biri yakın zamanda satın alındı. "İç-içe döngü + seviye-ayrımlı + müdahale-edilebilir" spesifik bileşimi hiçbir arama sonucunda birebir tarif edilmedi — DAYANAKSIZ (bu spesifik farklılaşma iddiası doğrulanamadı, [?]).

---

## B68-5 — gnhf-izle sınıfı hafif ajan-konuşma izleyicisi (LLM'siz, stream-json tail)

**Arama sorguları (birebir):**
1. `lightweight CLI stream-json tail viewer claude-code agent conversation log open source github`
2. `OpenTelemetry GenAI semantic conventions agent observability tools adoption 2026`

**Rakip/muadil listesi (hepsi arama-sonucu, GitHub):**
- **claude-code-log-viewer-cli** (JeiKeiLim) — Terminal-tabanlı, vim-stili navigasyon, watch mode, token istatistikleri, çok-proje dashboard.
- **claude-code-trace** (delexw) — JSONL viewer, desktop/web/TUI, canlı tail, MCP tool call tespiti.
- **agent-flow** (patoles) — Gerçek-zamanlı görselleştirme, HTTP hook server, JSONL tail, pan/zoom canvas.
- **claude-log-viewer** (InDate) — Web tabanlı, gerçek-zamanlı izleme, git entegrasyonu.
- **Claude-Code-Agent-Monitor** (hoangsonww) — SQLite3+Node+React+WebSocket dashboard, alt-ajan orkestrasyon takibi.
- **claude-code-log** (daaain) — Python CLI, JSONL→HTML/Markdown dönüştürücü (LLM'siz, statik dönüşüm — B68-5'e en yakın felsefi eşleşme).
- **claude-code-history-viewer** (jhlee0409) — Masaüstü uygulama, konuşma geçmişi tarayıcı.
- **claude-tap** (liaohch3) — Çoklu-ajan (Claude Code, Codex, Gemini CLI, Cursor CLI vb.) API trafiği izleyici.

**PAZAR SİNYALİ:** Tüm liste GitHub açık-kaynak projeler; hiçbirinde fiyat sayfası bulgusu YOK → **sinyalsiz** (ücretli plan bulunamadı, ödeme kanıtı aranmadı ayrı ayrı repo bazında — bütçe dışı). Yıldız sayıları arama sonucunda verilmedi → [?]. Funding/iş ilanı sinyali aranmadı → [?].

**Rekabet yoğunluğu: DOYGUN** (nicelik olarak). Ancak hepsi Claude-Code-özgü JSONL log görüntüleyiciler; genel "herhangi ajan" + "OTel GenAI semantic conventions tabanlı" hafif CLI kombinasyonu — OTel tarafı ayrı bir eksende yoğun (aşağıya bkz. B68-7 ile çakışan alan) — DAYANAKSIZ (spesifik "gnhf-izle sınıfı" farklılaşması: LLM'siz + stream-json + çok-araç-genel — doğrudan eşleşen tek isim bulunamadı, en yakın claude-code-log Claude-Code'a özgü, çok-araç-genel değil).

---

## B68-7 — Ajan hareket kütüğü + araç arayüz standardı (AXI)

**Arama sorguları (birebir):**
1. `OpenTelemetry GenAI semantic conventions agent observability tools adoption 2026` (B68-5 ile paylaşılan sorgu, sonuç burada da geçerli)
2. `AgentOps SDK pricing GitHub stars agent action logging`
3. `Helicone W&B Weave MCP agent tool interface standard action logging`

**Rakip/muadil listesi:**
- **OpenTelemetry GenAI Semantic Conventions** — CNCF'ye geçti (2026-05 iddiası, arama-sonucu), LLM span/agent span/event/metrics şemasını standartlaştırıyor; auto-instrumentation OpenAI/Anthropic/LangChain/LlamaIndex için mevcut (arama-sonucu: elastic.co, uptrace.dev, greptime.com, webhani.com). **Bu, AXI'nin doğrudan en güçlü rakibi** — zaten şema-standardı iddiasında.
- **AgentOps SDK** — MIT lisanslı, 2 satır entegrasyon, denetim izi + maliyet takibi; standardizasyon iddiası yok, kendi SDK'sı (arama-sonucu: inference.net).
- **MCP (Model Context Protocol)** — Araç-arayüz standardı olarak zaten yaygın; W&B Weave MCP trafiğini otomatik logluyor (arama-sonucu: wandb.ai). AXI'nin "--json/--sessiz/çıkış-kodu sözlüğü" CLI-arayüz standardı iddiası MCP'nin protokol katmanından farklı ama komşu alan.
- **Helicone** — Proxy-tabanlı, base-URL değişikliğiyle logging; "bakım modunda" olduğu iddia edildi (arama-sonucu: chatforest.com) — SEYREK aktivite sinyali.
- **W&B Weave** — MCP trace'lerini tek satırla otomatik loglar, ajan-native arayüz (arama-sonucu: wandb.ai, docs.wandb.ai).

**PAZAR SİNYALİ:**
- Ücretli plan MEVCUT: AgentOps ($40/ay Pro — tutar burada yalnız bağlam için arama-sonucunda geçti, raporlanan alan yalnız "MEVCUT" statüsü), W&B Weave (kurumsal ürün, ücretli plan var).
- Ücretli plan YOK: OpenTelemetry (CNCF projesi, temelde ücretsiz standart) — sinyalsiz/ticari değil.
- Helicone: "maintenance mode" iddiası (arama-sonucu, birincil kaynak açılmadı) — ÇELİŞİR (aktif pazar sinyaliyle çelişir, DAYANAKSIZ tek kaynak).
- Funding/iş ilanı sinyali: aranmadı, [?].

**Rekabet yoğunluğu: ORTA-DOYGUN.** Standardizasyon ekseninde OpenTelemetry GenAI conventions güçlü, CNCF-destekli, %89 üretim kullanıcısı OTel uyumluluğunu "çok önemli" görüyor iddiası (arama-sonucu, tek kaynak) — bu AXI'nin "standart" konumlandırmasına doğrudan meydan okuyor. Ancak "ajan hareket kütüğü PIPELINE + CLI --json/--sessiz/çıkış-kodu sözlüğü" spesifik bileşimi (protokol değil, CLI-araç arayüz sözleşmesi) hiçbir sonuçta birebir bulunamadı — DAYANAKSIZ (bu dar kesişim için doğrudan rakip kanıtı yok, [?]).

---

## Notlar / sınırlamalar
- 8 WebSearch sorgusu koşuldu (bütçe: 15 araç çağrısı içinde); hiçbir URL doğrudan açılmadı (WebFetch kullanılmadı) → tüm kaynaklar "arama-sonucu" etiketli, "birincil kaynak" DENMEDİ.
- Fiyat TUTARLARI bazı arama-sonucu snippet'lerinde otomatik geldi (ör. AgentOps $40/ay, LangSmith $39/koltuk, Langfuse $29/$199, Braintrust $249) — talimat gereği bu rapor gövdesinde yalnız "MEVCUT/YOK" beyanı kullanıldı; snippet'lerdeki tutarlar burada YER ALMAZ ama arama motoru sonucunun ham metninde geçti (ajan snippet'i olduğu gibi yapıştırmadı, seçici aktardı).
- GitHub yıldız sayıları ve funding haberleri çoğunlukla tek arama-sonucu kaynağına dayanıyor — doğrulama zinciri (halusinasyon-engelleyici) koşulmadı, bu rapor DESTEKLİ/DAYANAKSIZ etiketleri kendi iç-tutarlılığıyla sınırlı.
