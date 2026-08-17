export const meta = {
  name: 'baglam-kompozisyon-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — bağlam-penceresi kompozisyonu: kategori yüzdeleri ne söyler, Jarvis için hangi aralık (gorev-2026-08-17-4)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-17-1.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi; Claude Code (terminal/masaüstü) ve Cowork üzerinde çalışır. Sahibin sorusu: "Cowork'te 'Context window' sekmesini açınca bağlam penceresinin anlık olarak hangi kategorilerden yüzde kaç oluştuğunu görüyorum. Bu oranlar bize ne söyler? Jarvis'i geliştirirken oranları hangi aralıkta tutmalıyız?" Kategoriler (Claude Code /context eşdeğeri): sistem promptu · sistem araçları · MCP araçları · özel ajanlar · hafıza dosyaları (CLAUDE.md vb.) · skill'ler · mesajlar · boş alan · otomatik-sıkıştırma tamponu. Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; yeniden keşfetme, ÜSTÜNE KOY):
- Jarvis sondajı (deterministik, transkript usage alanları): oturum başı bağlam 44,5k token = ~22k cache-okuma (harness sistem promptu + araç tanımları + yerleşik skill listesi) + ~22,5k cache-yazım (Jarvis-özel: CLAUDE.md 6,99 KB + auto-memory + hook önizleme + 16 skill açıklaması 9,0 KB + ajan listesi); oturum içinde 452k'ya çıktı (1M pencerede %45; medyan 279k) — büyüme araç çıktıları + mesajlar. CLAUDE.md bütçesi ≤7 KB (v1 14 KB'da uzun koşumlarda davranış bozuldu — sahibin gözlemi, ölçülmemiş). Kapsül 16,3 KB/40 satır; SessionStart hook çıktısı 25,8 KB → harness yalnız 2 KB önizleme bağlama koydu (enjeksiyon fiilen çalışmıyor). MCP araç şemaları ToolSearch ile ertelenmiş. Kararlı-önek disiplini (statik önce, dinamik sonda) + prompt cache fiyatı (okuma 0,1×; yazma 1,25×/2×) verili.
- Verili bulgular: tek alakasız cümle GSM8K −22,6 puan ("yok say" +5,4 geri alır) · Mem0 tam-bağlam 72,9 > seçilmiş 66,9 ama token −%93 · bağlamı daraltmak 79k→9,6k %73→%84 · çelişkili iki sürüm yan yana: hiyerarşi uyumu %98→%20 · Multi-IF 3 turda 0,877→0,707 · Anthropic context editing (100k tetik, keep=3) + compaction · Letta blok karakter sınırlı · LongMemEval uzun-bağlam modellerinde −%30-55 · alt-ajan dönüşü ≈1-2k token, ana bağlamdan ayrı.
- Bilinmeyen (çekirdek): kategorilerin resmî tanımı/hesaplanışı · autocompact eşiği/tamponu ve 200k↔1M farkı · hangi kategori oranı için ÖLÇÜLMÜŞ bozulma eşiği var · diğer sistemlerin yayımlanmış bütçeleri · deterministik ölçüm/kayıt yolu.
- Kural: model kuşağı + pencere boyutu DAMGASI zorunlu (2023 200k ↔ 2025-26 1M farklı davranır); satıcı beyanı D sayılmaz.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / standart metni / arXiv-ACL / GitHub). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur (rakam · yüzde · tarih · sayım) — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz (benchmark tablosu/metodoloji görülmedikçe K).
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma.
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, test seti TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'KATEGORİLER + RESMÎ KILAVUZ (Anthropic; "bu oranlar ne söyler")',
    questions: `A1. Claude Code /context çıktısı ve Cowork/masaüstü "Context window" sekmesi: kategoriler (System prompt · System tools · MCP tools · Custom agents · Memory files · Skills · Messages · Free space · Autocompact buffer …) — resmî tanımlar, hangi dosya/kaynaktan gelir, hangileri STATİK önek (cache'lenebilir) hangileri DİNAMİK; yüzde neye göre (pencere 200k/1M; tampon dahil mi); resmî doküman URL'si.
A2. Autocompact/compaction mekaniği: tetik eşiği (yüzde/token), tampon boyutu, CLAUDE_AUTOCOMPACT_PCT_OVERRIDE/ayarlar, /compact ve /clear davranışı, "context low" uyarı eşikleri, 1M pencere (beta) farkları; kaynaklı sayılar.
A3. Anthropic bağlam-mühendisliği rehberi ("Effective context engineering for AI agents"; Claude Code best practices; Tool Search/MCP tool bloat; skills description bütçesi/listeleme sınırı; memory files/CLAUDE.md boyut önerisi): "attention budget", context rot, minimal-yüksek-sinyal, JIT retrieval, compaction, alt-ajan izolasyonu — her biri için resmî cümle + varsa SAYI (tool search token azaltma yüzdesi; CLAUDE.md için rakam var mı?).
A4. Kategori-başına "sağlık" yorumu resmî mi: Anthropic herhangi bir kategori için ORAN/eşik öneriyor mu (MCP araçları > %X ⇒ tool search; memory > Y token uyarısı); yoksa "bulunamadı" (kör).`,
    antitezHint: 'kategoriler UI kolaylığı, resmî semantik yok · Anthropic hiçbir kategori için oran önermiyor · autocompact eşikleri sürümden sürüme değişti, sabit değil.' },
  { key: 'B', title: 'ÖLÇÜLMÜŞ ETKİ (literatür; "hangi aralık")',
    questions: `B1. Uzun-bağlam bozulması: Chroma "Context Rot" (2025, 18 model), NoLiMa, RULER, LongBench v2, "Lost in the Middle" — kullanılan bağlam yüzdesi/uzunluğu ↔ doğruluk eğrisi; hangi doluluk oranında (%50? %70? %90?) ölçülür düşüş başlıyor; model kuşağı damgalı; 1M pencerede aynı mı.
B2. Statik-önek/talimat yükü: sistem promptu uzunluğu ve kısıt sayısı ↔ talimat-uyum (IFEval/Multi-IF verili — YENİ/derinleşen ölçüm), araç-tanımı sayısı/token'ı ↔ araç-seçim doğruluğu (BFCL, "tool overload", "less is more" tool selection, Anthropic tool search kanıtı), skill/komut listesi büyüklüğü ↔ tetikleme doğruluğu — sayı+kaynak.
B3. Mesaj/araç-çıktısı payı: araç sonuçlarının bağlamdaki payı ↔ hata (context editing gerekçesi), "conversation history length ↔ performance" ölçümleri (LongMemEval verili — yeni), alt-ajan izolasyonunun ölçülmüş kazancı (Anthropic multi-agent research system: kalite ↔ token çarpanı; başka ölçüm) — hangi oran aralığı.
B4. Compaction/özet kaybı: otomatik özetlemenin ölçülmüş bilgi kaybı (MemGPT, Anthropic compaction, "summarization loss"/"context compression" çalışmaları: hangi oranda kayıp), ne zaman /clear > /compact; ölçülmüş.`,
    antitezHint: 'context rot eski/küçük modellerde; 2025-26 1M modellerinde bozulma yok/çok küçük · araç-sayısı etkisi tool-search ile çözüldü · compaction kaybı ihmal edilebilir · "doluluk yüzdesi" bozulmanın nedeni değil, içerik türü.' },
  { key: 'C', title: 'JARVIS UYGULAMASI: EMSAL BÜTÇELER + ÖLÇÜM YÖNTEMİ + POLİTİKA DESENLERİ',
    questions: `C1. Diğer sistemlerin YAYIMLANMIŞ bağlam bütçeleri/limitleri (sayı+kaynak): Letta hafıza bloğu karakter sınırı, MemGPT core memory boyutu, Cursor rules/.cursorrules limitleri, GitHub Copilot instructions/AGENTS.md boyut önerisi, Cline memory bank, OpenAI Codex AGENTS.md, Gemini CLI GEMINI.md, LangGraph/LangMem — "statik talimat/hafıza için X token/karakter" emsalleri.
C2. Ölçüm yöntemi: Claude Code transkript şeması (usage.input_tokens / cache_creation_input_tokens / cache_read_input_tokens; cache_creation.ephemeral_5m/1h) — hangi alan hangi kategoriye karşılık gelir; Claude Code OTel telemetri (CLAUDE_CODE_ENABLE_TELEMETRY, metrikler/olaylar), /cost, /context; OTel gen_ai semantik konvansiyonları; LLM-observability araçlarında (Langfuse/Datadog/Helicone) "context utilization" metrikleri — kompozisyonun deterministik zaman-serisi olarak kaydı için emsal.
C3. Politika desenleri (yayımlanmış): Anthropic context engineering; Manus "context engineering for AI agents" (KV-cache hit rate = en önemli metrik, append-only, tool masking, file system as context, recitation); LangChain context engineering (write/select/compress/isolate); Cognition/Devin notları; "context budget" tahsis kuralları (statik/dinamik/serbest yüzdeleri) varsa sayı; ne zaman alt-ajan/izolasyon; ne zaman compact/clear.
C4. Kayıt/alarm: bağlam-sağlık metriklerinin telemetride nasıl loglandığı ve eşiklendiği (uyarı yorgunluğu — verili), "context low" ergonomisi; Jarvis'e uygun grain için EMSAL (işçi tasarlamaz, örnek getirir).`,
    antitezHint: 'başka sistemlerin limitleri keyfî, ölçümsüz · transkript alanlarından kategori çıkarılamaz (yalnız toplam) · KV-cache hit rate metriği tek-kullanıcıda anlamsız · "context engineering" blogları anekdot.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['kategori-anlamı','oran-aralığı','ölçüm-yöntemi','politika-kuralı','bütçe-emsali','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'örneklem/kapsam/sürüm/model kuşağı; yoksa "-"' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') + model-kuşağı/pencere damgası' },
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
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS, description: 'teknik-sınıfı' }, jarvis: { type: 'string', enum: JARVIS, description: 'Jarvis eşlemesi (sondajdaki mevcut duruma göre)' }, confidence: { type: 'string', enum: ['D','K'] } } } },
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
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + model-kuşağı/pencere-boyutu damgası; 'oran-aralığı' yalnız ölçülmüş dayanakla) + kör noktalar (özellikle 'oran → bozulma' ölçümü yoksa AÇIKÇA) (aranıp bulunamayan; özellikle küçük-ölçek ölçümü yoksa AÇIKÇA) + survival sayımı.
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

log('gorev-2026-08-17-4 sahada: 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: 'cc/gorev-2026-08-17-4.md', families: out }
