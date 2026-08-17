export const meta = {
  name: 'agile-jarvis-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — agile metodolojisi ↔ Jarvis (tek-kişi + ajan) eşlemesi + ölçülebilir metrikler (gorev-2026-08-17-3, KB-15)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-17-3.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı (Salih), markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi (deterministik tasarım; stdlib-only Python 3.9 + SQLite; günde 1-3 "seans" = oturum; karar başına commit; her araç çağrısı loglanır). Roller: tek karar verici (insan) + üst-orkestratör (en güçlü model) + lider/işçi ajanlar (daha zayıf modeller). Soru: agile'ın hangi parçası bu rejime uyar, hangisi uymaz; ölçülebilir metrikler.`

const KANON = `KANONDA ZATEN BİLİNENLER — JARVIS SÜREÇ ENVANTERİ (verili; eşlemede bunu kullan, yeniden keşfetme):
S1 SEANS = oturum (açılış ritüeli → iş → kapanış: teslim raporu + hasat + durum kapsülü + commit/push); zaman-kutulu DEĞİL, günde 1-3 · S2 PANO (AKTİF/BEKLEYEN/BLOKE/SON BİTEN kartları, DONE ölçütü zorunlu; WIP limiti yok) + kuyruk (karar defteri, fikir kutusu) + karar-borcu (açık kararlar listesi) · S3 HASAT (seans sonu özütler, wiki-delta, "verilebilir miydi", token×zaman etiketi) + TESLİM RAPORU (ne değişti · karar · aday · sonraki ilk iş · yeniden-açma) · S4 DONE-YÜKLEMİ boolean (görev = küçük tipli fonksiyon) · S5 PROOF-OF-WORK = push'lanmış commit (gün push'suz sayılmaz) · S6 tek karar verici + üst-orkestratör + lider/işçi ajanlar · S7 ÖLÇÜM: P6 dörtlüsü (token · duvar-saati · iterasyon · sonuç), ajan başına token/süre ambarı, hareket kütüğü (her araç çağrısı), veri testleri, skill sayaçları · S8 iterasyon > spec-first + ölçek şerhi (büyük işte spec→plan→tasks) + sorun-güdümlü optimizasyon · S9 kanon (tüzük) + çelişki kapısı + karar defteri.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / standart metni / arXiv-ACL / GitHub). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur (rakam · yüzde · tarih · sayım) — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz (benchmark tablosu/metodoloji görülmedikçe K).
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma.
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, test seti TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'ÇEKİRDEK EŞLEME — agile/Scrum/Kanban/XP pratiklerinin tanımı (birincil kaynak) + tek-kişi rejiminde ölçülmüş etkisi + Jarvis S1-S9 eşlemesi',
    questions: `A1. Birincil tanımlar: Agile Manifesto (12 ilke), Scrum Guide 2020 (sprint, sprint goal, backlog, daily, review, retro, DoD, increment), Kanban Guide / Anderson (WIP limiti, akış, sınıf-of-service), XP (küçük yayın, sürekli entegrasyon, basit tasarım) — her pratik için tek cümle mekanizma + kaynağı.
A2. Tek-kişi / solo geliştirici / çok küçük takımda agile: ölçülmüş çalışmalar (Personal Kanban, solo Scrum, "agile for one" akademik/pratik kaynaklar; ne kazandırdı, n) — zaman-kutusuz oturumlar (S1) sprint sayılır mı; standup tek kişide neye dönüşür.
A3. Eşleme tablosu (her satır kaynaklı): sprint↔seans · backlog↔pano/kuyruk/karar-borcu · retro↔hasat · review↔teslim raporu · DoD↔done-yüklemi · increment↔push'lanmış commit · WIP limiti↔(yok) · refinement↔damıtma? — uyuyor / kısmi / uymuyor / girmez + gerekçe.
A4. Agile'ın Jarvis'in deterministik-tasarım ve karar-defteri kültürüyle GERİLDİĞİ yerler (örn. "working software over documentation" ↔ kanon-yoğun sistem; "responding to change" ↔ spec→plan→tasks) — literatürde bu gerilimin ölçülmüş çözümü var mı.`,
    antitezHint: 'agile pratikleri takım/örgüt için tasarlandı, tek kişide anlamsız/zararlı · sprint zaman-kutusu olmadan sprint değildir, eşleme sözde · solo agile çalışmaları anekdotal, n küçük · Jarvis zaten fiilen kanban-benzeri, adlandırma dışında kazanç yok.' },
  { key: 'B', title: 'AJANLI GELİŞTİRMEDE AGİLE (2023-26) — insan + LLM-ajan takımlarında uyarlama ve ölçülmüş etki',
    questions: `B1. Literatür/sektör: "AI-assisted / agentic software engineering + agile" (2023-26): sprint içinde ajan görevi, backlog'u ajan işler (issue→PR), retro'yu log/telemetri besler, ajan için DoD — birincil kaynaklar (makale, resmî mühendislik blogu, DORA raporları) + ölçülmüş etki (verim, kalite, n).
B2. DORA 2024/2025 AI raporları ve benzeri: AI kullanımının throughput/stability üzerine ÖLÇÜLMÜŞ etkisi (rakam + n + yön); "AI hızlandırır ama kararlılığı düşürür" türü bulgular; küçük ekip/solo için geçerli mi.
B3. Ajan orkestrasyonunda agile deseni: çok-ajan çerçevelerinin (MetaGPT "SOP", ChatDev, AgentVerse vb.) Scrum-benzeri roller/rituelleri ölçülmüş mü — kazanç deterministik SOP'tan mı, roller/ritüelden mi geliyor.
B4. Solo-geliştirici + ajan rejiminde retrospektif/ölçüm döngüsünün ölçülmüş örneği var mı (log-tabanlı retro, otomatik hasat) — yoksa "bulunamadı".`,
    antitezHint: 'ajanlı takımlarda agile ritüelleri gereksiz maliyet; kazanç araçtan, süreçten değil · DORA AI bulguları büyük örgütlerden, solo rejime transfer etmez · çok-ajan "Scrum" çerçeveleri gösteri, ölçülmüş kazanç SOP\'tan.' },
  { key: 'C', title: 'ÖLÇÜM — hangi agile/flow metrikleri tek-kişi + ajan rejiminde ölçülebilir ve anlamlı; Jarvis S7 ile eşleme',
    questions: `C1. Metrik tanımları (birincil): velocity, cycle time, lead time, throughput, WIP, flow efficiency, DORA dörtlüsü (deployment frequency, lead time for changes, change failure rate, MTTR), burndown — hangisi takım-ölçekli istatistik ister (n), hangisi tek kişide anlamlı.
C2. Küçük-n uyarıları: velocity/story-point tahmininin ölçülmüş güvenilirliği (n, sapma), NoEstimates tartışmasının kanıtı; tek kişide neyi ölçmek işe yarıyor (cycle time? WIP?).
C3. Jarvis S7 verisiyle türetilebilirlik: commit/push (increment) → deployment frequency benzeri; kart açılış→DONE → cycle time; token/süre → maliyet; hareket kütüğü → iterasyon; hangi metrik mevcut veriden deterministik türer, hangisi ek kayıt ister.
C4. "Girmez" listesi kanıtlı: hangi agile pratik/metrik tek-kişi+ajan rejiminde ölçülmüş zarar/anlamsızlık gösteriyor (örn. story point, planning poker, velocity kıyası).`,
    antitezHint: 'flow metrikleri tek kişide de anlamlı (WIP/cycle time istatistik istemez) · DORA solo geliştiriciye uyarlanmış · velocity tek kişide bile tahmin doğruluğunu artırır (ölçülmüş) · Jarvis mevcut verisi bu metrikleri zaten türetiyor.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['ritüel','artefakt','rol','ölçüm-metriği','ilke','girmez']
const JARVIS = ['uyuyor','kısmi','uymuyor','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'örneklem/kapsam/sürüm/model kuşağı; yoksa "-"' },
    placement_suggestion: { type: 'string', description: 'sınıf (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') — ör. "ritüel · kısmi (S1)"' },
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

log('gorev-2026-08-17-3 sahada: 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: 'cc/gorev-2026-08-17-3.md', families: out }
