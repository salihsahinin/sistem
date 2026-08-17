export const meta = {
  name: 'skill-semasi-m40b',
  description: 'm.40b çift-atlas: 4 aile × (tez → CoVe-Factored antitez → V26 örneklem → maskeli hakem) — skill-üretim kapı-ağacı araştırması',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara' },
    { title: 'V26', detail: 'örneklem kaynak-denetimi (ajan başına ≥1 iddia)' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları' },
  ],
}

// ---------- ortak bloklar ----------
const KANON = `KANONDA ZATEN BİLİNENLER (verili kabul et; yeniden araştırma, ÜSTÜNE KOY):
- Jarvis tüzük m.43: "aynı adım kümesi ≥3 tekrar → skill ADAYI"; eşik N=3 DENEYSEL; kaynağı Rule of Three (Fowler 1999) — LLM alanında ampirik doğrulaması YOK. Aday ≠ üretim; üretim = eval-önce akış (K-016).
- Skill üretim standardı (Anthropic skill-creator + docs, 07-17 raporu): eval-ÖNCE akış (skill'siz koştur → 3 senaryo eval → baseline → minimal gövde) · description = NE + NE ZAMAN + NEGATİF-TETİK, ≤1024 char · gövde <500 satır, tek sorumluluk · yan-etkili skill = disable-model-invocation (elle tetik) · deterministik adım → script · skill'ler birbirini literal çağırmaz; orkestratör zincirler; pratik zincir sınırı ~3-4 skill [doğrulanmadı] · description-eval 20 sorgu × 3 koşum.
- Ajan-metodolojisi v1: dal+koşul toplamı ≤5 (Multi-IF 3 turda 0,877→0,707 dayanağı) · done-yüklemi boolean · lojik→kod merdiveni B1 serbest-NL → B2 kontrollü-NL/lojik → B3 şablon/DSL/skill → B4 kod; basamak-geçiş 3-soru kapısı (adım sayısı tahmin edilebilir? sabit yol kodlanabilir? model-kararı gerekli mi?) · AWM: kural-tabanlı indüksiyon ≈ LM-tabanlı · üretici≠doğrulayıcı.
- Anthropic çok-ajan: efor-ölçekleme (basit 1 ajan/3-10 çağrı · kıyas 2-4 · karmaşık 10+); "workflow=önceden tanımlı yol ↔ agent=model yönlendirmesi"; ajan-desenleri: prompt-chain / routing / parallel / orchestrator-worker / evaluator-optimizer.
- Epistemik dersler (08-13 spec-kit koşumu): kanıt sürüm-damgasız taşınmaz · varlık ≠ canlılık · alıntı toplamak ≠ kanıt tartmak.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: arXiv/resmî docs/standart metni/GitHub). Rakamlar kaynaklı; kestirimse "[?]" ile işaretle. Örneklem/kapsam yaz (çıplak yüzde yasak).
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur (arama yapıldı, yok). "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = arama-özeti/ikincil, teyide muhtaç · X = doğrulanamadı/çelişkili.
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma.
- Arama bütçesi İDARELİ (~15-25 arama; bilinen birincil kaynaklara doğrudan git). Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır (StructuredOutput). Karar ALMA, şema TASARLAMA — o başkasının işi; sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'KAPI-AĞACI YAPISI (kaç katman · katman-başına kaç düğüm · ebeveyn sayısı · bağlanma kuralı)',
    questions: `A1. Boolean kabul/ret ağaçlarının FORMAL semantiği: Fault Tree Analysis / attack trees (AND-OR kapıları, minimal kesim kümesi), DMN karar tabloları (hit policy), guard-clause zinciri — bir "aday-kabul ağacı" için hangi formalizm; AĞAÇ (tek ebeveyn) mi DAG/polihiyerarşi (çok ebeveyn) mi — standartlar (ISO 25964 tezaurus, SKOS broader/narrower, ontoloji-mühendisliği kılavuzları) ne der?
A2. DERİNLİK/GENİŞLİK sayısal çapaları: Stage-Gate (Cooper — kaç kapı/aşama, kapı-başına kaç kriter) · klinik triyaj ağaçları (ESI karar-noktası sayısı, START, Manchester) · WHO cerrahi güvenlik checklist'i (madde/durak sayısı), Gawande "kill point"leri · DevOps kalite-kapısı sayıları · Miller 7±2 / Cowan 4±1 · ML karar-ağacı derinlik↔genelleme (overfitting; MDL) — "katman ve düğüm sayısı" için ölçülü aralık.
A3. SIRA ilkesi: en ucuz / en ayırt-edici koşul ÖNCE (information gain, fail-fast, guard clauses); katman-içi AND (∀ koşul) vs OR (∃ koşul) kuralı — "Y ∨ Z sağlanırsa alt katmana geç" tasarımının literatür karşılığı ve riski (OR-katmanı kabul-oranını nasıl şişirir?).
A4. Yolun TÜR ürettiği tasarımlar: sınıflandırma ağacı yaprakları = sınıf; biyolojide dikotom anahtar (determination key) — kabul + sınıflandırma aynı yürüyüşte; belgeli tasarım kuralları (her düğüm tek ikili soru; MECE; couplet yazım kuralları).`,
    antitezHint: 'Olası ters yönler: düz checklist derin ağacı yener · AND-OR formalizmi küçük kütüphanede aşırı-mühendislik · derin kapı-ağaçları yanlış-ret üretir · polihiyerarşi standartlarda serbesttir (ağaç zorunlu değil).' },
  { key: 'B', title: 'TEKRAR-EŞİĞİ n + SAYISAL KOŞULLAR ("matematiksel olarak anlamlı" sayı)',
    questions: `B1. Rule of Three kaynakları (Roberts 1998 "three strikes and you refactor", Fowler Refactoring; DRY/WET) — konvansiyon mu ölçüm mü; karşı-görüş (AHA programming, "premature abstraction", "wrong abstraction") var mı?
B2. MATEMATİKSEL eşik adayları: istatistiksel rule-of-three (0/n → %95 üst sınır 3/n) · Laplace ardışıklık kuralı P(tekrar|k gözlem)=(k+1)/(k+2) · Apriori minimum-support · SPRT (sıralı olasılık-oran testi) — hangisi "aynı iş tekrar edecek mi" sorusuna uygun; k=2/3/5 için sayısal değerler ve varsayımlar.
B3. MÜHENDİSLİK analogları — "yorumla → derle" = "NL → skill": JIT sıcak-kod eşikleri (HotSpot CompileThreshold / Tier3InvocationThreshold / Tier4 · V8 tier-up (Ignition→Sparkplug→Maglev→TurboFan) · PyPy trace eşiği — GERÇEK rakamlar + gerekçe) · cache-admission politikaları (W-TinyLFU doorkeeper "2. erişimde kabul", 2Q, ARC ghost list) — "pahalı katmana kabul için k isabet" rakamları.
B4. MALİYET-FAYDA kesişimi: otomasyon değer mi formülü (XKCD 1205 "Is It Worth the Time" tablosu: sıklık × kazanılan-süre × ufuk ≥ inşa maliyeti) → n_min = C_inşa / Δ_kullanım; skill/prompt için ÖLÇÜLMÜŞ Δ (skill-ile vs skill'siz token/süre — Anthropic skill-creator benchmark, TROVE/AWM/Voyager kullanım-sayısı ve budama eşikleri) var mı? Kütüphane budama: kaç kullanımdan az = emekli?`,
    antitezHint: 'Olası ters yönler: hiçbir "matematiksel n" yoktur, JIT eşikleri elle ayarlanmış sabitlerdir · Laplace/rule-of-three varsayımları burada geçersiz (bağımsız-özdeş deneme değil) · erken soyutlama zararı ölçülüdür (n büyük olmalı) ya da tersine gecikme maliyeti (n küçük olmalı) · skill Δ ölçümü yok.' },
  { key: 'C', title: 'HALLUCINATION-FRENİ / DOĞRULAMA KAPILARI (üretilen artefaktın topraklanması)',
    questions: `C1. LLM'lerin var-olmayan araç/paket/prosedür üretme ORANLARI: package hallucination (Spracklen ve ark. 2024/2025 "We Have a Package for You"; slopsquatting), tool-hallucination benchmark'ları (ToolBench/ToolAlpaca/BFCL "hallucinated/irrelevant API"), prosedür/adım uydurma — rakam + örneklem + model kuşağı.
C2. Araç-üretim (tool-making) hatlarında KABUL KAPILARI ve ölçülmüş etkisi: LATM (LLMs as Tool Makers: maker→verifier, unit-test kapısı) · CREATOR · CRAFT · ToolMaker · Voyager self-verification · TROVE (kullanım-temelli trim) · AWM — hangi kapı hangi hata sınıfını ne kadar düşürdü?
C3. Üretici≠doğrulayıcı + kanıt-pointer zorunluluğu: eval-önce (Anthropic skill-creator with/without baseline) · CoVe (Chain-of-Verification) · self-consistency · "her adım kaynağa bağlı" (grounding/attribution) — KABUL KAPISI olarak ölçülmüş etki; dış-geribildirimsiz öz-düzeltmenin başarısızlık kanıtı (Huang ve ark. 2023 vb.).
C4. Kapı-zinciri matematiği: seri kapıların kabul-oranı çarpımsal (∏ p_i) — kapı sayısı arttıkça iyi adayın düşme olasılığı (yanlış-negatif) ↔ hallucination sızması (yanlış-pozitif); optimal kapı sayısı/sıralaması için model (ROC, seri-test duyarlılık×özgüllük, "swiss cheese" modeli); klinik seri/paralel-test literatürü uygulanabilir mi?`,
    antitezHint: 'Olası ters yönler: doğrulama kapıları üretilen prosedürde hallucination\'ı ölçülür biçimde düşürmez · eval-önce süreç tiyatrosudur · package-hallucination rakamları yeni modellerde çöktü (sorun geçici) · kapı-zinciri iyi adayları öldürür (yanlış-negatif baskın).' },
  { key: 'D', title: 'TAKSONOMİ + ÇAĞRI GRAFI (yol → tür; çok skill\'de yönlendirme)',
    questions: `D1. Araç/skill SAYISI ↔ seçim doğruluğu: kaç araçtan sonra bozuluyor (BFCL, "tool count vs accuracy" çalışmaları, Anthropic tool-search / MCP tool-search bağlam-azaltma rakamı, "Less is More" tool-selection, Gorilla) · Claude Code skill description bütçesi (≤1024 char; listeleme kesme 1536 [doğrulanmamış]) — düz liste kaç skill'e dek çalışır?
D2. HİYERARŞİK / faceted araç-erişimi kazancı: AnyTool (hiyerarşik API retriever) · ToolLLM/ToolBench (16k API, kategori→araç→API ağacı) · HuggingGPT · ToolRet — hiyerarşi düz aramaya karşı ölçülü kazanç; kaç seviye; kategori-başına kaç araç?
D3. Sınıflandırma kuramı: hiyerarşik vs faceted (Ranganathan PMEST) · polihiyerarşi standardı (ISO 25964-1 / SKOS: bir kavramın birden çok broader'ı olabilir mi?) · ontoloji derinlik/kardeş-sayısı kılavuzları (ör. "≤4-5 seviye", "7±2 kardeş" iddiaları kaynaklı mı?) — "ağaç mı DAG mı, her düğüm kaç ebeveyn" için standart cevap.
D4. Skill-TÜR eksenleri: Claude Code'un yerleşik tür ayrımları (skill/hook/subagent/command · context:fork · disable-model-invocation · user-invocable · allowed-tools) · Anthropic ajan-desenleri (prompt-chain / routing / parallel / orchestrator-worker / evaluator-optimizer) · Voyager / JARVIS-1 skill-graph — tür ekseni önerileri (yan-etkili↔etkisiz · ritüel↔araç · scout↔ship · elle↔oto-tetik).`,
    antitezHint: 'Olası ters yönler: <100 skill\'de taksonomi/hiyerarşi kazancı yoktur, description kalitesi tek belirleyicidir · hiyerarşik retriever düz embedding aramayı geçmez · polihiyerarşi yönlendirmeyi bozar · Miller 7±2 kardeş-sayısı için geçersiz atıftır.' },
]

// ---------- şemalar ----------
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','schema_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'örneklem/kapsam/sürüm/model kuşağı; yoksa "-"' },
    schema_suggestion: { type: 'string', description: 'bu bulgu şemaya nasıl oturur (kök-koşul / katman-koşulu / sayısal-eşik / tür-ekseni / sıra-kuralı / girmez)' },
  } }
const TEZ_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','claims','gaps','access_blocks','budget_note'],
  properties: {
    family: { type: 'string' },
    claims: { type: 'array', minItems: 6, maxItems: 24, items: CLAIM },
    gaps: { type: 'array', items: { type: 'string' }, description: 'aranıp bulunamayanlar (kör nokta adayları)' },
    access_blocks: { type: 'array', items: { type: 'string' }, description: '403/paywall/[ARANAMADI]' },
    budget_note: { type: 'string', description: 'kaç arama yapıldı, bütçe bitti mi' },
  } }
const REBUT = { type: 'object', additionalProperties: false, required: ['target_id','negation','verdict','evidence_url','figure','note'],
  properties: {
    target_id: { type: 'string' },
    negation: { type: 'string', description: '¬T: savunulan ters önerme (tek cümle)' },
    verdict: { type: 'string', enum: ['ÇÜRÜTÜLDÜ','DARALTILDI','ÇÜRÜTÜLEMEDİ'] },
    evidence_url: { type: 'string', description: 'URL ya da "bulunamadı"' },
    figure: { type: 'string' },
    note: { type: 'string', description: 'DARALTILDI ise daraltılmış hâl; ÇÜRÜTÜLEMEDİ ise ne arandı' },
  } }
const ANTI_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','rebuttals','extra_counter_claims','budget_note'],
  properties: {
    family: { type: 'string' },
    rebuttals: { type: 'array', items: REBUT },
    extra_counter_claims: { type: 'array', items: CLAIM, description: 'tezde olmayan ama şemayı ilgilendiren KARŞI yönlü bulgular' },
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
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','confidence'],
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: ['kök-koşul','katman-koşulu','sayısal-eşik','tür-ekseni','sıra-kuralı','yapı-kuralı'] }, confidence: { type: 'string', enum: ['D','K'] } } } },
    blind_spots: { type: 'array', items: { type: 'string' } },
    survival: { type: 'object', additionalProperties: false, required: ['saglam','daraldi','dustu','celiskili'], properties: { saglam: { type: 'integer' }, daraldi: { type: 'integer' }, dustu: { type: 'integer' }, celiskili: { type: 'integer' } } },
  } }

// ---------- deterministik "rastgele" (seed'li LCG; Math.random yasak) ----------
let rng = (args && args.seed) ? args.seed : 12345
function nextRand(n) { rng = (rng * 1103515245 + 12345) % 2147483648; return rng % n }

// ---------- aşamalar ----------
const tezStage = (fam) => agent(
`ROL: Atlas TEZ araştırmacısı — aile ${fam.key}: ${fam.title}. Bağımsız çalışıyorsun; başka ailenin sorusuna cevap verme.
Bağlam: Jarvis (kişisel LLM-operasyon sistemi) skill üretimi için kökten dallara akan BOOLEAN kapı-ağacı şeması kuruyor (her düğüm matematiksel-anlamlı koşul; en alt dala ulaşan aday skill olur; yol = skill türü). Senin ailen bu şemanın bir boyutuna kanıt getirir.

${KANON}

ARAŞTIRMA SORULARI (yalnız bunlar):
${fam.questions}

${DISIPLIN}
Çıktı: 6-24 iddia (her soruya ≥1), her biri kaynaklı; gaps/access_blocks/budget_note doldur.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: 'atlas', effort: 'high', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')  // gerekçe/kaynak GEÇMEZ (CoVe-Factored)
  return agent(
`ROL: Atlas ANTİTEZ ajanı (açık Devil's-Advocate) — aile ${fam.key}: ${fam.title}.
Sana bir başka araştırmacının İDDİA satırları veriliyor; GEREKÇELERİ ve KAYNAKLARI kasıtlı olarak verilmiyor (çıpalama freni). Görevin: her iddianın DEĞİLİNİ (¬T) savunacak BİRİNCİL kanıt aramak — "alternatif bakış" değil, lojiksel ters. Çürütemediysen "ÇÜRÜTÜLEMEDİ" yaz ve ne aradığını belirt; süs-antitez ÜRETME. Kısmen çürüttüysen DARALTILDI + daraltılmış hâlini yaz.
Ek olarak: tezde OLMAYAN ama şemayı ilgilendiren karşı-yönlü bulgular varsa extra_counter_claims'e ekle. Yön ipuçları (bağlayıcı değil): ${fam.antitezHint}

${KANON}

İDDİALAR:
${claimsOnly}

${DISIPLIN}`,
    { label: `antitez:${fam.key}`, phase: 'Antitez', agentType: 'atlas', effort: 'high', schema: ANTI_SCHEMA }
  ).then(anti => ({ tez, anti }))
}

const v26Stage = (r, fam) => {
  if (!r || !r.tez) return null
  const t = r.tez.claims.filter(c => /^https?:/.test(c.source_url))
  const a = (r.anti && r.anti.rebuttals) ? r.anti.rebuttals.filter(x => /^https?:/.test(x.evidence_url)) : []
  const picks = []
  if (t.length) { const i = nextRand(t.length); picks.push({ claim_id: t[i].id, claim: t[i].claim, url: t[i].source_url, figure: t[i].figure }) }
  if (t.length > 1) { let j = nextRand(t.length); if (picks[0] && t[j].id === picks[0].claim_id) j = (j + 1) % t.length; picks.push({ claim_id: t[j].id, claim: t[j].claim, url: t[j].source_url, figure: t[j].figure }) }
  if (a.length) { const k = nextRand(a.length); picks.push({ claim_id: `¬${a[k].target_id}`, claim: a[k].negation, url: a[k].evidence_url, figure: a[k].figure }) }
  if (!picks.length) return Promise.resolve({ ...r, v26: { family: fam.key, checks: [] } })
  return agent(
`ROL: V26 örneklem-denetçisi (aile ${fam.key}). Aşağıdaki iddia→URL çiftlerine KAYNAĞA İNEREK bak: URL'yi getir (WebFetch), iddia ve rakam kaynak metinde GERÇEKTEN var mı? Sonuç: TUTUYOR / TUTMUYOR / ERİŞİLEMEDİ (403-paywall). Not: tek cümle — kaynakta ne gördün. Uydurma yok; yorum yok; yalnız doğrula.
${picks.map((p,i)=>`${i+1}. [${p.claim_id}] "${p.claim}" — rakam: ${p.figure} — URL: ${p.url}`).join('\n')}`,
    { label: `v26:${fam.key}`, phase: 'V26', effort: 'low', schema: V26_SCHEMA }
  ).then(v26 => ({ ...r, v26 }))
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
Ölçüt = adversarial-hayatta-kalma: bilgili karşı-tarafın çürütmeyi deneyip BAŞARAMADIĞI önerme SAĞLAM; kısmen çürüyen DARALDI (hayatta kalan daraltılmış hâlini yaz); çürüyen DÜŞTÜ; iki taraf da güçlü ve uzlaşmazsa ÇELİŞKİLİ (saklama, öyle yaz). Kanıt gücü: birincil > ikincil; rakamlı > rakamsız; sürüm-damgalı > damgasız; kaynak-denetimi TUTMUYOR çıkan tarafın o iddiası K'ya düşer. Şüphede kaynağa kendin inebilirsin (WebFetch), ama bütçe idareli.
Sonda: bu aileden ŞEMAYA GİRECEK 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: kök-koşul / katman-koşulu / sayısal-eşik / tür-ekseni / sıra-kuralı / yapı-kuralı) + kör noktalar (aranıp bulunamayan; şema tasarımcısı bilmeli) + survival sayımı.
Şema bağlamı: Jarvis skill üretimi için kökten dallara akan boolean kapı-ağacı (her düğüm matematiksel-anlamlı koşul; yaprak = skill kabul + tür).

## ÇİFTLER
${pairs}

## KARŞI-TARAFIN EK BULGULARI (teze itiraz dışı)
${extras || '(yok)'}

## KAYNAK-DENETİMİ (bağımsız örneklem)
${v26txt || '(yapılamadı)'}

## Tezin kendi beyan ettiği boşluklar/erişim engelleri
${(r.tez.gaps||[]).map(g=>'- '+g).join('\n') || '(yok)'}
${(r.tez.access_blocks||[]).map(g=>'- ⚠ '+g).join('\n')}`,
    { label: `hakem:${fam.key}`, phase: 'Hakem', schema: HAKEM_SCHEMA }
  ).then(hakem => ({ ...r, hakem, mask }))
}

log('S-1 sahada: 4 aile × tez→antitez→V26→hakem (pipeline, barrier yok)')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, families: out }