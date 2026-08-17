export const meta = {
  name: 'hafiza-teknik-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — LLM hafıza-yönetimi teknik envanteri × Jarvis kullanılan/kullanılmayan haritası (gorev-2026-08-17-2)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-17-1.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi (deterministik tasarım; stdlib-only Python 3.9 + SQLite; bronz ≈2M token; günde ~5-15 karar). Sahibin sorusu: "LLM'de hafıza oluşturmak için bugün LLM-wiki + bağlam veritabanı kullanıyoruz; literatürde/sektörde modern ve fiilen kullanılan 'LLM hafıza yönetimi' teknikleri (şemsiye terim değil, TEK TEK) hangileri; kullanmadığımız hangileri girmeli?" Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin.`

const KANON = `KANONDA ZATEN BİLİNENLER — JARVIS HAFIZA ENVANTERİ (verili; "kullanıyoruz" eşlemesinde bunu kullan, yeniden keşfetme):
J1 LLM-wiki (Karpathy deseni; 15 sayfa + sözlük + index/log) · J2 bağlam veritabanı: kanon markdown'ın 1:1 türetilmiş ilişkisel silver tabloları (41,9k blok, 47k referans, 321 anahtar) + bitemporal ambar (koşum/prompt/karar olguları) · J3 anahtar-değer kaydı (kavram/tetik/ad başına tek güncel değer, SCD-2 emeklilik + cascade) · J4 özet belleği: seans başında okunan üzerine-yazılan durum kapsülü (≤200 satır) + pano · J5 çalışma belleği enjeksiyonu: CLAUDE.md (≤7 KB) + SessionStart hook (kapsül ilk 40 satır) + Claude Code auto-memory dizini (user/feedback/project notları) · J6 graf: referans tablosu (blok→madde/kart/skill/dosya/URL) + wiki [[link]] — KG üçlüsü değil · J7 prosedürel hafıza: 16 skill (SKILL.md+script+evals) + ajan tanımları · J8 epizodik ham kayıt: transkriptler → bronz kütükler (prompt-olay, koşum-olay, hareket-olay = her araç çağrısı) + seans-teslim raporları · J9 karar günlüğü append-only + karar-borcu envanteri · J10 konsolidasyon: eşikte-toplu damıtma turu + seans-kapanış hasadı + ingest triyajı NOOP/UPDATE/GEÇERSİZ-KIL/ADD (Mem0 deseni) + sıcak/ılık/soğuk katman · J11 kararlı-önek + prompt-cache disiplini · J12 git = olay deposu · J13 ERİŞİM: grep + SQL + pointer + katalog-önce; embedding/vektör YOK (bilinçli erteleme, ölçüm tetikli), BM25/FTS YOK, LLM-rerank YOK · J14 unutma/bayatlık: yalnız katman etiketi; deterministik test mekanizması ayrı emirde karar masasında · J15 parametrik hafıza (fine-tune/LoRA/knowledge-editing) YOK; uzun-bağlam "her şeyi yükle" YOK.
Verili bulgular: bağlamı daraltmak doğruluğu yükseltebilir (79k→9,6k token: %73,2→%83,6) · LLM çelişki-denetçisi FP %22-56 (ikinci göz, kapı değil) · yan yana çelişkili sürüm: hiyerarşi uyumu %98→%20 · Karpathy: ~100 kaynak/yüzlerce sayfada index-önce, embedding gereksiz (ÖLÇÜMSÜZ iddia) · Mem0 LOCOMO'da tam-bağlama karşı %26 göreli iyileşme + maliyet düşüşü · LongMemEval 500 soru/5 yetenek.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / standart metni / arXiv-ACL / GitHub). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur (rakam · yüzde · tarih · sayım) — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz (benchmark tablosu/metodoloji görülmedikçe K).
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma.
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, test seti TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'LİTERATÜR TAKSONOMİSİ + TERİM AYRIŞTIRMASI (şemsiye ↔ somut teknik; ölçülmüş kazanç; Jarvis eşlemesi)',
    questions: `A1. 2024-26 survey taksonomileri: "A Survey on the Memory Mechanism of LLM-based Agents" (Zhang ve ark. 2024), "From Human Memory to AI Memory" (2025), MemOS/"memory operating system" hattı, CoALA (Sumers 2023: working/episodic/semantic/procedural), 2025-26 "memory in LLM agents" derlemeleri — hafıza TÜRLERİ (working/episodic/semantic/procedural/parametric) × İŞLEMLERİ (write/encode · store/organize · retrieve · update · forget/consolidate) matrisi; hangi terimler ŞEMSİYE ("memory management", "long-term memory"), hangileri TEKNİK.
A2. Somut TEKNİKLER ve birincil sistemler — her biri için mekanizma tek cümle + ölçülmüş kazanç (benchmark, n) + Jarvis J1-J15 eşlemesi (kullanıyoruz-eş / kısmi / eksik-aday): MemGPT/Letta (tiering, core/archival/recall), Generative Agents (recency×importance×relevance + reflection), Reflexion, MemoryBank (Ebbinghaus), A-MEM (Zettelkasten-vari bağlantılı notlar), Mem0 (ADD/UPDATE/DELETE/NOOP + graph), Zep/Graphiti (temporal KG), HippoRAG/GraphRAG/RAPTOR (yapılandırılmış erişim), MemoRAG, sleep-time compute (Letta 2025), ExpeL/AutoGuide (deneyimden kural), Voyager (skill library), Titans/"memory as parameters", knowledge editing (ROME/MEMIT), KV-cache/context compression (LLMLingua, CacheBlend).
A3. Benchmark'lar ve ne ölçtükleri: LongMemEval (5 yetenek), LoCoMo, MemBench, MSC, MemoryAgentBench, 2025-26 long-horizon setleri — hangi teknik hangi yetenekte kazandırıyor (rakam+n); tek-kullanıcı ajan İŞLETİMİNE transfer sınırı.
A4. Karpathy LLM-wiki deseninin literatür karşılığı: "LLM-maintained knowledge base", "agentic wiki", semantic memory as documents, docs-as-memory — akademik/sektörel adı ve ölçülmüş emsali; index-önce iddiasının kanıtı var mı.`,
    antitezHint: 'taksonomiler keyfî/uyumsuz, "teknik" ayrımı yapay · benchmark kazançları sohbet-asistanı senaryosundan, ajan-işletimine transfer etmez · LLM-wiki deseninin akademik karşılığı yok / ölçümü yok.' },
  { key: 'B', title: 'SEKTÖR PRATİĞİ — fiilen DEPLOY edilmiş hafıza teknikleri (resmî doküman; satıcı pazarlaması D sayılmaz)',
    questions: `B1. Model sağlayıcıları: Anthropic (Claude memory tool / memory beta, Claude Code auto-memory + CLAUDE.md, context editing/compaction, prompt caching, "context management"), OpenAI (ChatGPT memory: saved memories + chat-history reference; API conversation state), Google (Gemini memory/personalization) — hangi teknik: dosya-tabanlı mı, özet mi, vektör mü, kullanıcıya görünür mü; belgeli sınırlar/sayılar.
B2. Ajan çerçeveleri/hafıza ürünleri: LangGraph store + LangMem (semantic/episodic/procedural üçlüsü, memory tools), Letta (MemGPT), Mem0 (ürün: graph memory, kendi benchmark'ı), Zep, Cognee, Supermemory, Memori, "memory layer" SaaS'ları — mimari (KV · vektör · graf · SQL · dosya) + belgeli ölçüm; satıcı benchmark'ı K.
B3. Kod-ajanı/IDE hafızaları: Cursor rules/memories, GitHub Copilot memory/instructions, Windsurf memories, Cline memory bank, OpenAI Codex AGENTS.md — "dosya-tabanlı talimat/hafıza" deseninin sektör standardı olup olmadığı; Jarvis J5/J7 ile eşleme.
B4. Kişisel bilgi-yönetimi + LLM: Obsidian/Notion AI, "second brain" araçları, qmd (BM25+vektör hibrit, LLM rerank; Karpathy'nin andığı), Recoll/ripgrep+LLM, SQLite FTS5 tabanlı arama — küçük kişisel korpus için hangi erişim tekniği yaygın; ölçüm varsa.`,
    antitezHint: 'sektör "hafıza" ürünleri pazarlama; deployed özellik özet+vektörden ibaret · dosya-tabanlı hafıza standart değil, geçici · IDE hafızaları talimat dosyası, "hafıza" değil.' },
  { key: 'C', title: 'JARVIS REJİMİNDE EKSİK ADAYLARIN ÖLÇÜLMÜŞ KAZANCI (yalnız kullanılmayanlar: erişim · pekiştirme/yansıma · epizodik kullanım · parametrik/uzun-bağlam/cache)',
    questions: `C1. ERİŞİM: sözcüksel (BM25 / SQLite FTS5) ↔ yoğun (embedding) ↔ hibrit ↔ LLM-rerank — 10⁴-10⁵ parça / tek-kullanıcı / markdown korpusunda ÖLÇÜLMÜŞ kıyas (BEIR küçük alt-kümeleri, kişisel-korpus çalışmaları, "BM25 hâlâ güçlü" bulguları, hibrit kazancı); SQLite FTS5'in Python 3.9 stdlib sqlite3'te varlığı (birincil kaynak); index-önce/pointer stratejisinin (Karpathy) yoğun erişime karşı ölçümü varsa.
C2. PEKİŞTİRME/YANSIMA: periyodik konsolidasyon (Generative Agents reflection ablasyonu, sleep-time compute, MemGPT özetleme, "memory summarization" ablasyonları), deneyimden-kural çıkarma (ExpeL, AutoGuide, self-evolving agents) — ölçülmüş kazanç + maliyet; eşikte-toplu damıtmadan (J10) farkı; deterministik-tasarım kuralıyla bağdaşan biçimi (kural+kod, LLM aday-üretici).
C3. EPİZODİK BELLEĞİN KULLANIMI: ham transkript/koşum kütüğünden (J8) "deneyim" hafızasına dönüştürme — trajectory retrieval, few-shot from past episodes, experience replay ajanlarda ölçülmüş kazanç; ne zaman değer üretiyor, ne zaman gürültü.
C4. PARAMETRİK/UZUN-BAĞLAM/CACHE: fine-tune/LoRA/knowledge-editing kişisel ajanda (ölçüm + bedel; GİRMEZ ise kanıtla), uzun-bağlam ↔ RAG ödünleşimi 2025-26 ölçümleri (1M pencere), KV-cache/prompt-cache tekniklerinin (context caching, CacheBlend) tek-kullanıcı ajanda ölçülmüş tasarrufu — J11'in ötesinde ne var.`,
    antitezHint: 'BM25/FTS5 küçük korpusta embedding’e denk (vektör gereksiz) YA DA tersi (embedding kazancı ölçülü) · yansıma/konsolidasyon LLM-yargısı deterministik kuralla çelişir ve kazancı küçük · epizodik replay gürültü ekler · uzun-bağlam RAG’ı gereksiz kılıyor / kılmıyor · knowledge-editing kararsız.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['erişim','yazma-güncelleme','unutma','pekiştirme','yapı-organizasyon','parametrik','işletim-yaşam-döngüsü','ölçüm-metriği','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'örneklem/kapsam/sürüm/model kuşağı; yoksa "-"' },
    placement_suggestion: { type: 'string', description: 'teknik-sınıfı (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') — ör. "erişim · eksik-aday (J13)"' },
  } }
const TEZ_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','claims','gaps','access_blocks','budget_note'],
  properties: {
    family: { type: 'string' },
    claims: { type: 'array', minItems: 4, maxItems: 10, items: CLAIM },
    gaps: { type: 'array', items: { type: 'string' }, description: 'aranıp bulunamayanlar (kör nokta adayları)' },
    access_blocks: { type: 'array', items: { type: 'string' }, description: '403/paywall/[ARANAMADI]' },
    budget_note: { type: 'string', description: 'kaç arama/fetch yapıldı, bütçe bitti mi' },
  } }
const REBUT = { type: 'object', additionalProperties: false, required: ['target_id','negation','verdict','evidence_url','figure','note'],
  properties: {
    target_id: { type: 'string' },
    negation: { type: 'string', description: '¬T: savunulan ters önerme (tek cümle)' },
    verdict: { type: 'string', enum: ['ÇÜRÜTÜLDÜ','DARALTILDI','ÇÜRÜTÜLEMEDİ'] },
    evidence_url: { type: 'string', description: 'URL ya da "bulunamadı"' },
    figure: { type: 'string', description: 'rakam varsa; yoksa "-"' },
    note: { type: 'string', description: 'DARALTILDI ise daraltılmış hâl; ÇÜRÜTÜLEMEDİ ise ne arandı' },
  } }
const ANTI_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','rebuttals','extra_counter_claims','budget_note'],
  properties: {
    family: { type: 'string' },
    rebuttals: { type: 'array', maxItems: 10, items: REBUT },
    extra_counter_claims: { type: 'array', maxItems: 3, items: CLAIM, description: 'tezde olmayan ama mekanizmayı ilgilendiren KARŞI yönlü bulgular' },
    budget_note: { type: 'string' },
  } }
const V26_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','checks'],
  properties: {
    family: { type: 'string' },
    checks: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','url','result','note'],
      properties: { claim_id: { type: 'string' }, url: { type: 'string' }, result: { type: 'string', enum: ['TUTUYOR','TUTMUYOR','ERİŞİLEMEDİ'] }, note: { type: 'string' } } } },
  } }
const HAKEM_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','verdicts','building_blocks','blind_spots','survival'],
  properties: {
    family: { type: 'string' },
    verdicts: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','verdict','surviving_form','reason'],
      properties: { claim_id: { type: 'string' }, verdict: { type: 'string', enum: ['SAĞLAM','DARALDI','DÜŞTÜ','ÇELİŞKİLİ'] }, surviving_form: { type: 'string', description: 'hayatta kalan (gerekirse daraltılmış) önerme; DÜŞTÜ ise "-"' }, reason: { type: 'string', description: '≤2 cümle: hangi kanıt hangi kanıtı neden yendi' } } } },
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','jarvis','confidence'],
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS, description: 'teknik-sınıfı' }, jarvis: { type: 'string', enum: JARVIS, description: 'Jarvis eşlemesi (J1-J15 envanterine göre)' }, confidence: { type: 'string', enum: ['D','K'] } } } },
    blind_spots: { type: 'array', items: { type: 'string' } },
    survival: { type: 'object', additionalProperties: false, required: ['saglam','daraldi','dustu','celiskili'], properties: { saglam: { type: 'integer' }, daraldi: { type: 'integer' }, dustu: { type: 'integer' }, celiskili: { type: 'integer' } } },
  } }

// ---------- V26 KURAL-TABANLI seçim (Salih imzası 08-17; deterministik — rastgele YOK) ----------
// (a) ajanın çıktısının SON ÜÇTE BİRİNDEN ≥1 URL'li iddia + (b) TÜM sayısal iddialar (figure rakam içerir ∨ iddia metninde % / n= / × kalıbı)
const isUrl = s => /^https?:\/\//.test(s || '')
const isNumeric = (fig, txt) => (fig && fig !== '-' && /\d/.test(fig)) || /\d+\s?%|\bn\s?=\s?\d|\d+\s?×|\d+\s?pp\b/.test(txt || '')
function v26Picks(items, idOf, txtOf, urlOf, figOf) {
  const picks = []; const seen = new Set()
  const add = (it, why) => { const id = idOf(it); if (seen.has(id)) return; seen.add(id); picks.push({ claim_id: id, claim: txtOf(it), url: urlOf(it), figure: figOf(it), why }) }
  const n = items.length
  if (!n) return picks
  // (a) son üçte-bir: ilk URL'li iddia
  const start = Math.floor(n * 2 / 3)
  for (let i = start; i < n; i++) { if (isUrl(urlOf(items[i]))) { add(items[i], 'son-üçte-bir'); break } }
  // (b) tüm sayısal iddialar (URL'li olanlar denetlenir; URL'siz sayısal iddia derlemede KAYNAKSIZ damgası alır)
  items.forEach(it => { if (isNumeric(figOf(it), txtOf(it)) && isUrl(urlOf(it))) add(it, 'sayısal') })
  return picks
}

// ---------- aşamalar ----------
const tezStage = (fam) => agent(
`ROL: Atlas TEZ araştırmacısı — aile ${fam.key}: ${fam.title}. Bağımsız çalışıyorsun; başka ailenin sorusuna cevap verme.
${BAGLAM}

${KANON}

ARAŞTIRMA SORULARI (yalnız bunlar):
${fam.questions}

${DISIPLIN}
Çıktı: 4-10 iddia (her soruya ≥1), her biri kaynaklı; gaps/access_blocks/budget_note doldur. Sayısal iddialarda figure alanı ZORUNLU dolu.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')  // gerekçe/kaynak GEÇMEZ (CoVe-Factored)
  return agent(
`ROL: Atlas ANTİTEZ ajanı (açık Devil's-Advocate) — aile ${fam.key}: ${fam.title}.
Sana bir başka araştırmacının İDDİA satırları veriliyor; GEREKÇELERİ ve KAYNAKLARI kasıtlı olarak verilmiyor (çıpalama freni). Görevin: her iddianın DEĞİLİNİ (¬T) savunacak BİRİNCİL kanıt aramak — "alternatif bakış" değil, lojiksel ters. Çürütemediysen "ÇÜRÜTÜLEMEDİ" yaz ve ne aradığını belirt; süs-antitez ÜRETME. Kısmen çürüttüysen DARALTILDI + daraltılmış hâlini yaz.
Ek olarak: tezde OLMAYAN ama mekanizmayı ilgilendiren karşı-yönlü bulgular varsa extra_counter_claims'e ekle (≤3). Yön ipuçları (bağlayıcı değil): ${fam.antitezHint}
${BAGLAM}

${KANON}

İDDİALAR:
${claimsOnly}

${DISIPLIN}`,
    { label: `antitez:${fam.key}`, phase: 'Antitez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: ANTI_SCHEMA }
  ).then(anti => ({ tez, anti }))
}

const v26Stage = (r, fam) => {
  if (!r || !r.tez) return null
  const tezPicks = v26Picks(r.tez.claims, c => c.id, c => c.claim, c => c.source_url, c => c.figure)
  // ÇÜRÜTÜLEMEDİ satırları örnekleme GİRMEZ (¬T'yi destekleyen kaynak yok = antitezin kendi beyanı; TUTMUYOR orada tutarlılıktır — 08-17 A ailesi bulgusu)
  const antiItems = ((r.anti && r.anti.rebuttals) ? r.anti.rebuttals : []).filter(x => x.verdict !== 'ÇÜRÜTÜLEMEDİ')
  const antiPicks = v26Picks(antiItems, x => `¬${x.target_id}`, x => `${x.negation} [${x.verdict}: ${x.note}]`, x => x.evidence_url, x => x.figure)
  const picks = tezPicks.concat(antiPicks)
  const rule = { tez: tezPicks.map(p => `${p.claim_id}(${p.why})`), antitez: antiPicks.map(p => `${p.claim_id}(${p.why})`) }
  if (!picks.length) return Promise.resolve({ ...r, v26: { family: fam.key, checks: [] }, v26_rule: rule })
  return agent(
`ROL: V26 örneklem-denetçisi (aile ${fam.key}). Aşağıdaki iddia→URL çiftleri KURAL-TABANLI seçildi (çıktının son üçte-birinden ≥1 + tüm sayısal iddialar). Her biri için KAYNAĞA İN (WebFetch): iddia ve rakam kaynak metinde GERÇEKTEN var mı? Sonuç: TUTUYOR / TUTMUYOR / ERİŞİLEMEDİ (403-paywall). Not: tek cümle — kaynakta ne gördün (rakamı aynen aktar). Uydurma yok; yorum yok; yalnız doğrula. Repoya dosya yazma, alt-ajan açma.
${picks.map((p,i)=>`${i+1}. [${p.claim_id}] "${p.claim}" — rakam: ${p.figure} — URL: ${p.url}`).join('\n')}`,
    { label: `v26:${fam.key}`, phase: 'V26', model: 'sonnet', effort: 'low', schema: V26_SCHEMA }
  ).then(v26 => ({ ...r, v26, v26_rule: rule }))
}

const hakemStage = (r, fam, idx) => {
  if (!r || !r.tez) return null
  const rebutBy = {}
  ;((r.anti && r.anti.rebuttals) || []).forEach(x => { rebutBy[x.target_id] = x })
  const mask = {}
  const pairs = r.tez.claims.map((c, i) => {
    const x = rebutBy[c.id]
    const tezFirst = ((idx + i) % 2 === 0)
    mask[c.id] = tezFirst ? 'Taraf-1=tez' : 'Taraf-1=antitez'
    const P = `Önerme P: ${c.claim}\n  kanıt: ${c.source_url} · rakam: ${c.figure} · kapsam: ${c.scope}`
    const N = x ? `Önerme ¬P: ${x.negation}\n  kanıt: ${x.evidence_url} · rakam: ${x.figure} · not: ${x.note} · karşı-tarafın öz-değerlendirmesi: ${x.verdict}` : `Önerme ¬P: (karşı-taraf bu önermeye itiraz getirmedi)`
    return `### ${c.id}\n${tezFirst ? 'Taraf-1 — ' + P + '\nTaraf-2 — ' + N : 'Taraf-1 — ' + N + '\nTaraf-2 — ' + P}`
  }).join('\n\n')
  const extras = ((r.anti && r.anti.extra_counter_claims) || []).map(c => `- [${c.id}] ${c.claim} — ${c.source_url} · ${c.figure} · ${c.scope}`).join('\n')
  const v26txt = (r.v26 && r.v26.checks || []).map(c => `- [${c.claim_id}] ${c.url} → ${c.result}: ${c.note}`).join('\n')
  return agent(
`ROL: MASKELİ HAKEM — aile ${fam.key}: ${fam.title}. Sen üretici koşumların devamı DEĞİLSİN; iki tarafın hangisinin "tez" hangisinin "antitez" olduğu sana SÖYLENMİYOR — iddia+kanıt olarak tart.
Ölçüt = adversarial-hayatta-kalma: bilgili karşı-tarafın çürütmeyi deneyip BAŞARAMADIĞI önerme SAĞLAM; kısmen çürüyen DARALDI (hayatta kalan daraltılmış hâlini yaz); çürüyen DÜŞTÜ; iki taraf da güçlü ve uzlaşmazsa ÇELİŞKİLİ (saklama, öyle yaz). Kanıt gücü: birincil > ikincil; rakamlı > rakamsız; sürüm-damgalı > damgasız. KAYNAK-DENETİMİ kuralı (V26): bir tarafın denetlenen iddiası TUTMUYOR çıktıysa o tarafın o ailedeki TÜM iddiaları K'ya düşer (nota yaz). Şüphede kaynağa kendin inebilirsin (WebFetch), bütçe idareli (≤6).
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + teknik-sınıfı: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} — envanter J1-J15'e göre; 'eksik-aday' yalnız ölçülmüş kazanç varsa) + kör noktalar (aranıp bulunamayan; özellikle küçük-ölçek ölçümü yoksa AÇIKÇA) + survival sayımı.
${BAGLAM}

## ÇİFTLER
${pairs}

## KARŞI-TARAFIN EK BULGULARI (teze itiraz dışı)
${extras || '(yok)'}

## KAYNAK-DENETİMİ (bağımsız, kural-tabanlı örneklem)
${v26txt || '(yapılamadı)'}

## Tezin kendi beyan ettiği boşluklar/erişim engelleri
${(r.tez.gaps||[]).map(g=>'- '+g).join('\n') || '(yok)'}
${(r.tez.access_blocks||[]).map(g=>'- ⚠ '+g).join('\n')}`,
    { label: `hakem:${fam.key}`, phase: 'Hakem', effort: 'high', schema: HAKEM_SCHEMA }
  ).then(hakem => ({ ...r, hakem, mask }))
}

log('gorev-2026-08-17-2 sahada: 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: 'cc/gorev-2026-08-17-2.md', families: out }
