export const meta = {
  name: 'anakronizm-freni-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — "anakronizm yasak" (Salih Karar 68) kuralını MEKANİKLEŞTİRECEK önleme yöntemleri: LLM zamansal zemin · bitemporal/as-of/TTL kayıt katmanı · ajan/işletim damga+lint pratiği; determinizm-önceliği; gorev-2026-08-26-2',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları + deterministik + as-of damgası (üst model, high)' },
  ],
}

const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, TÜRKÇE markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi (Claude Code, Mac). Asistan (Carvis) bir LLM'dir: eğitim-verisi kesimi Ocak 2026, BUGÜN 2026-08-26 (~7-8 ay boşluk). Sahibin Katman-1 hükmü (aynen): "bundan sonra sistemde anakronizm yapmayı yasaklıyorum bunu önleyecek şekilde nasıl yapacağını araştır". ANAKRONİZM (çalışma tanımı): zaman-bağımlı bir iddianın (sürüm · SDK durumu · benchmark skoru · fiyat · 'en güçlü model' · ürün özelliği · kanon kaydı) geçerli olduğu zaman belirtilmeden ya da yanlış zamana ait olarak bugünün durumu gibi sunulması. Bugün yaşanan üç vaka: (i) 07-30 tarihli 'Rust SDK yok' hükmü 08-26'ya dek güncel sanıldı (yeniden çekilince MCP'de Tier-1 çıktı); (ii) 2025-04 tarihli benchmark sayısı konuşmada as-of damgasız 'düşük' diye söylendi; (iii) asistan eğitim-hafızasından skor anlattı. Üç kanal: ESKİ KAYIT (kanon) · MODEL HAFIZASI (kesim) · KONUŞMA (damgasız aktarım). Senin ailen 'NASIL ÖNLENİR' sorusunun bir boyutuna DIŞ KANIT getirir; karar vermezsin, Jarvis için kod/şema yazmazsın.
DETERMİNİZM ÖNCELİĞİ (Karar 65): önleme mekanizması kural/kod/şema tabanlı olmalı — 'modele hatırlatma/dikkat et' mekanizma sayılmaz (ölçülmüş etkisi varsa yalnız ek katman). Her yöntem/ürün iddiasına "deterministik: e / h / — (+ neden)" damgası. DİĞER: HAZIRI TEMEL AL · açık kaynak/Türkçe kaynak dosyalar · +1 araç-zinciri görünür bedel · m.8 bayat kayıt silinmez, damgalanır/arşive iner.
KENDİ ÇIKTINDA ANAKRONİZM YASAK: her iddiada AS-OF (kaynağın tarihi ∨ senin çekim tarihin 2026-08-26) yazılı olacak; damgasız iddia hakem tarafından düşürülür.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; ÜSTÜNE KOY):
- Jarvis'te var olan zaman mekanizmaları: (1) seans-açılış 'zaman-kayması freni' (selamlama zaman işareti değil; tarih yalnız sistem saatinden) · (2) silver tazelik kapısı (silver'ın git-sha'sı ≠ HEAD → 'bayat' uyarısı + yeniden üretim) · (3) halüsinasyon-derece formülünde v2 'tazelik' bayrağı (+1) · (4) anahtar kaydı SCD-2 + çift-zaman (gecerli_bas/gecerli_bitis; olay-zamanı ↔ işlem-zamanı; damgasız kayıt kabul edilmez) · (5) ambar amb_* tabloları bitemporal (valid_time_bas/son + system_time) · (6) bayat-kapsül riski kuralı · fikir-kutusu 30-gün BAYAT damgası · (7) rakam damgası kuralı (kaynaklı; kestirim [?]) · deneysel damga · (8) hakem kuralı: hazır-ürün sürümü hakem tarafından yeniden çekilir · (9) atlas disiplini 'ürün+sürüm+tarih zorunlu' · (10) LongMemEval (verili): zaman-farkındalı sorgu +%6,8-11,3 · Zep/Graphiti çift-zamanlı graf (K). EKSİK: kanon metninde as-of damgası zorunlu değil (yalnız rakamlar için); asistanın eğitim-kesimi beyanı yok; 'hangi olgu sınıfı ne kadar sürede bayatlar' listesi yok; tarihsiz iddia için deterministik lint yok; CHAT çıktısı için damga kuralı yok (yalnız rapor).
- Bilinmeyen (çekirdek): (i) anakronizm sınıfları ve hangi mekanizmanın hangisini ÖLÇÜLMÜŞ azalttığı (date-in-prompt · retrieval-with-timestamps · search-augmentation · self-declared cutoff · bitemporal kayıt · lint) · (ii) olgu sınıfı → bayatlama süresi taksonomisi için yayımlanmış temel · (iii) Türkçe markdown kanonunda ucuz ve deterministik damga biçimi + regex lint fizibilitesi · (iv) chat çıktısında damga zorunluluğunun uygulanabilir biçimi · (v) modelin kendi kesimini bilme güvenilirliği (ölçüm) · (vi) hazır araç: docs tazelik botu / 'as of' şablonu / stale-lint.
- Kural: ÜRÜN + SÜRÜM + TARİH; benchmark → veri kümesi + model + tarih; ölçümsüz 'çalışır' iddiası K; satıcı yazısı D değil.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil: arXiv/ACL makalesi · standart metni (SQL:2011, W3C PROV, HTTP RFC) · resmî doküman · kaynak kodu README · Wikipedia şablon dokümantasyonu). Rakamlar kaynaklı; kestirimse "[?]". Kapsam/veri-kümesi/sürüm yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanı dolu.
- Her iddiada AS-OF: kaynağın yayın/sürüm tarihi ∨ çekim tarihi (2026-08-26) scope alanında yazılı. Damgasız iddia = ihlal.
- UYDURMA YASAK; "bulunamadı" meşru; "[ARANAMADI]" = bütçe/erişim; 403/paywall bayraklanır.
- Etiket: D birincil · K ikincil/teyide muhtaç · X doğrulanamadı. Niceleyici ayrımı (∀/∃). Determinism alanı dolu.
- Bütçe ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git.
- Repoya/diske HİÇBİR DOSYA YAZMA. Paket KURMA. Alt-ajan AÇMA. Karar ALMA, Jarvis şeması TASARLAMA — kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'LLM ZAMANSAL ZEMİN (literatür): kesim tarihi · zamansal uyumsuzluk · hızlı-değişen olgu taksonomisi · ÖLÇÜLMÜŞ hafifletmeler',
    questions: `A1. Knowledge cutoff ↔ effective cutoff ("Dated Data", Cheng ve ark. 2024: modelin fiilî kesimi beyan edilenden ne kadar geride; sayılar) · temporal misalignment (Luu ve ark. 2022: zamanla performans düşüşü, görev başına) · modelin KENDİ kesim tarihini bilme doğruluğu (ölçüm var mı; satıcı beyanı vs ölçülen).
A2. FreshQA / FreshLLMs (Vu ve ark. 2023): olgu sınıfları (never-changing · slow-changing · fast-changing · false-premise) ve model doğruluğu sınıf başına; FreshPrompt (arama-artırma) kazancı sayıları; RealTimeQA; TimeQA/TemporalWiki/StreamingQA — hangi mekanizma hangi sınıfta ne kadar kazandırıyor (sayı + tarih).
A3. "Bugünün tarihi promptta" etkisi (ölçülmüş: tarih verilince zamansal cevaplar düzeliyor mu; satıcı sistem-promptlarında current-date alanı — Anthropic/OpenAI resmî kılavuz) · time-aware retrieval (TimeR4 · TempRALM · zaman-ağırlıklı skorlama · LongMemEval time-aware query) sayıları.
A4. Anakronizm TAKSONOMİSİ için yayımlanmış çerçeve: TimeML/TIMEX3 zamansal ifade çözümleme · document creation time · temporal validity of facts (Wikidata P585/P580/P582) · "temporal validity change prediction" · LLM çıktısında tarihli-iddia tespiti / time-aware fact-checking (ölçüm).`,
    antitezHint: 'date-in-prompt etkisi küçük/ölçümsüz · FreshQA kazancı arama-erişimine bağlı, kişisel sistemde geçersiz · modeller kesimini bilmez, beyan işe yaramaz · taksonomiler literatürde tutarsız · time-aware retrieval kazancı veri-kümesine özgü.' },
  { key: 'B', title: 'VERİ/KAYIT KATMANI: geçerlilik zamanı kayıtta nasıl taşınır (bitemporal · SCD2 · PROV · Wikidata) · as-of sorgusu · TTL/tazelik testi — deterministik bayatlık tespiti',
    questions: `B1. Bitemporal model: SQL:2011 system-versioned + application-time period tabloları (hangi motorlarda: MariaDB · Db2 · SQL Server temporal · Postgres uzantı; SQLite'ta eşdeğer desen) · Snodgrass valid-time/transaction-time · SCD Type 2 · event sourcing — "as-of" sorgusu nasıl yazılır; determinizm (aynı as-of → aynı cevap); kaynak + sürüm/tarih.
B2. Bilgi tabanlarında geçerlilik: Wikidata point-in-time (P585) / start-end (P580/P582) niteleyicileri + "as of" kuralı · W3C PROV generatedAtTime/invalidatedAtTime · Zep/Graphiti valid_at/invalid_at/expired_at (resmî doküman) · LLM-wiki/kişisel-bilgi desenlerinde "last verified" alanı — hangisi markdown+SQLite kanonuna en ucuz taşınır (kanıt: doküman/örnek).
B3. Tazelik SLA/TTL: dbt source freshness (warn_after/error_after) · Great Expectations/Soda tazelik testleri · HTTP Cache-Control max-age / Expires / ETag + revalidation semantiği (RFC 9111) · DNS TTL — "olgu sınıfı → TTL" tablosu kuran yayımlanmış örnek var mı; bayatlık testi çıktısı deterministik mi.
B4. ASOF join (DuckDB ASOF JOIN · kdb+ aj · Postgres) + "bir tarihe göre en son geçerli kayıt" sorgusunun hazır biçimi; SQLite'ta karşılığı (window/correlated subquery) — gecerli_bas/gecerli_bitis kolonlarıyla as-of sorgusu kurulabilir mi (doküman kanıtı, sürüm).`,
    antitezHint: 'bitemporal tablo tek-kullanıcı markdown kanonunda aşırı · SQLite\'ta ASOF yok, window sorgusu yavaş/karmaşık · TTL tabloları keyfi, olgu sınıfı belirlenemez · Wikidata niteleyicileri LLM-wiki\'ye taşınmaz · dbt freshness yalnız yükleme zamanı ölçer, içerik geçerliliğini değil.' },
  { key: 'C', title: 'AJAN/İŞLETİM PRATİĞİ: damga kuralları (as-of) · "iddia etmeden önce doğrula" politikaları · docs tazelik · deterministik ANAKRONİZM LİNT · hazır araçlar',
    questions: `C1. Satıcı kılavuzları: Anthropic (sistem promptunda current-date; knowledge cutoff beyanı; resmî kesim değerleri; Claude Code CLAUDE.md/memory bayatlığı önerisi) · OpenAI (cutoff + browsing politikası) · ajan çerçevelerinde "verify-before-assert"/tool-first politikaları (resmî doküman) — tarih + URL.
C2. Wikipedia {{As of}} şablonu + "Articles containing potentially dated statements" bakım kategorisi (nasıl çalışır; bot/lint; ölçek sayısı) · gazetecilik dateline/"at press time" kuralları · stil kılavuzlarında "as of" zorunluluğu — ucuz, insan-okur damga biçimleri.
C3. Docs-as-code tazelik: "last reviewed / review-by" başlıkları (Google developer documentation style guide, GitLab docs, Microsoft Learn ms.date) · actions/stale · docs freshness linters (Vale kural örneği; markdownlint özel kural) · kod: #[deprecated(since)] (Rust) · // Deprecated: (Go) · OpenAPI deprecated · @since — sürüm-damgalı kullanımdan-kaldırma deseni; determinizm.
C4. Deterministik ANAKRONİZM LİNT fizibilitesi: metinde tarihsiz sürüm/sayı/"en güncel"/"artık yok"/"şu an" kalıplarını yakalayan araçlar (HeidelTime · SUTime · dateparser — Türkçe desteği var mı) · "iddia + as-of + kaynak-tarihi" üçlüsünü zorlayan şema örneği (schema.org dateModified/temporalCoverage · ClaimReview datePublished) · bayat-iddia oranı metriği için hazır tanım (ölçüm).`,
    antitezHint: 'As-of şablonu insan disiplini, makine zorlamaz · lint yanlış-pozitif üretir, Türkçe zamansal-ifade desteği yok · satıcılar kesim tarihini muğlak bırakır, beyan güvenilmez · stale-bot kapatır, düzeltmez · "verify-before-assert" token maliyeti ölçümsüz.' },
]

const PLACEMENTS = ['tazelik-sınıfı-kuralı','kayıt-şeması','damga-kuralı','canlı-çekim-kuralı','denetim-yöntemi','hazır-ürün-araç','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','determinism','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sürüm/tarih (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'AS-OF ZORUNLU: kaynak yayın/sürüm tarihi ∨ çekim tarihi 2026-08-26 + veri-kümesi/model/kapsam' },
    determinism: { type: 'string', description: 'yöntem/ürün iddiasıysa "e"/"h"/"—" + tek-cümle neden; değilse "-"' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') + damga' },
  } }
const TEZ_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','claims','gaps','access_blocks','budget_note'],
  properties: { family: { type: 'string' }, claims: { type: 'array', minItems: 4, maxItems: 10, items: CLAIM }, gaps: { type: 'array', items: { type: 'string' } }, access_blocks: { type: 'array', items: { type: 'string' } }, budget_note: { type: 'string' } } }
const REBUT = { type: 'object', additionalProperties: false, required: ['target_id','negation','verdict','evidence_url','figure','note'],
  properties: { target_id: { type: 'string' }, negation: { type: 'string' }, verdict: { type: 'string', enum: ['ÇÜRÜTÜLDÜ','DARALTILDI','ÇÜRÜTÜLEMEDİ'] }, evidence_url: { type: 'string' }, figure: { type: 'string' }, note: { type: 'string', description: 'DARALTILDI ise daraltılmış hâl; ÇÜRÜTÜLEMEDİ ise ne arandı; AS-OF tarihi' } } }
const ANTI_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','rebuttals','extra_counter_claims','budget_note'],
  properties: { family: { type: 'string' }, rebuttals: { type: 'array', maxItems: 10, items: REBUT }, extra_counter_claims: { type: 'array', maxItems: 3, items: CLAIM }, budget_note: { type: 'string' } } }
const V26_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','checks'],
  properties: { family: { type: 'string' }, checks: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','url','result','note'], properties: { claim_id: { type: 'string' }, url: { type: 'string' }, result: { type: 'string', enum: ['TUTUYOR','TUTMUYOR','ERİŞİLEMEDİ'] }, note: { type: 'string' } } } } } }
const HAKEM_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','verdicts','building_blocks','blind_spots','survival'],
  properties: {
    family: { type: 'string' },
    verdicts: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','verdict','surviving_form','reason'], properties: { claim_id: { type: 'string' }, verdict: { type: 'string', enum: ['SAĞLAM','DARALDI','DÜŞTÜ','ÇELİŞKİLİ'] }, surviving_form: { type: 'string', description: 'hayatta kalan önerme, AS-OF damgalı; DÜŞTÜ ise "-"' }, reason: { type: 'string' } } } },
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','jarvis','deterministic','confidence'], properties: { block: { type: 'string', description: 'yapı-taşı, AS-OF damgalı' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS }, jarvis: { type: 'string', enum: JARVIS }, deterministic: { type: 'string', enum: ['e','h','—'] }, confidence: { type: 'string', enum: ['D','K'] } } } },
    blind_spots: { type: 'array', items: { type: 'string' } },
    survival: { type: 'object', additionalProperties: false, required: ['saglam','daraldi','dustu','celiskili'], properties: { saglam: { type: 'integer' }, daraldi: { type: 'integer' }, dustu: { type: 'integer' }, celiskili: { type: 'integer' } } },
  } }

const isUrl = s => /^https?:\/\//.test(s || '')
const isNumeric = (fig, txt) => (fig && fig !== '-' && /\d/.test(fig)) || /\d+\s?%|\bn\s?=\s?\d|\d+\s?×|\d+\s?pp\b/.test(txt || '')
function v26Picks(items, idOf, txtOf, urlOf, figOf) {
  const picks = []; const seen = new Set()
  const add = (it, why) => { const id = idOf(it); if (seen.has(id)) return; seen.add(id); picks.push({ claim_id: id, claim: txtOf(it), url: urlOf(it), figure: figOf(it), why }) }
  const n = items.length
  if (!n) return picks
  const start = Math.floor(n * 2 / 3)
  for (let i = start; i < n; i++) { if (isUrl(urlOf(items[i]))) { add(items[i], 'son-üçte-bir'); break } }
  items.forEach(it => { if (isNumeric(figOf(it), txtOf(it)) && isUrl(urlOf(it))) add(it, 'sayısal') })
  return picks
}

const tezStage = (fam) => agent(
`ROL: Atlas TEZ araştırmacısı — aile ${fam.key}: ${fam.title}. Bağımsız çalışıyorsun; başka ailenin sorusuna cevap verme.
${BAGLAM}

${KANON}

ARAŞTIRMA SORULARI (yalnız bunlar):
${fam.questions}

${DISIPLIN}
Çıktı: 4-10 iddia (her soruya ≥1), kaynaklı ve AS-OF damgalı; gaps/access_blocks/budget_note doldur.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')
  return agent(
`ROL: Atlas ANTİTEZ ajanı (açık Devil's-Advocate) — aile ${fam.key}: ${fam.title}.
Sana bir başka araştırmacının İDDİA satırları veriliyor; GEREKÇELERİ ve KAYNAKLARI kasıtlı olarak verilmiyor (çıpalama freni). Görevin: her iddianın DEĞİLİNİ (¬T) savunacak BİRİNCİL kanıt aramak — lojiksel ters. Çürütemediysen "ÇÜRÜTÜLEMEDİ" + ne aradığın; kısmen çürüttüysen DARALTILDI + daraltılmış hâl. Determinizm-önceliği gereği: iddia bir mekanizmayı "deterministik/zorlanabilir" sayıyorsa aksini (insan disiplini, yanlış-pozitif, yan-etki) da ara. Anakronizm yasağı: kendi kanıtlarını da AS-OF damgala.
Tezde OLMAYAN karşı-yönlü bulgular varsa extra_counter_claims'e ekle (≤3). Yön ipuçları (bağlayıcı değil): ${fam.antitezHint}
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
  const antiItems = ((r.anti && r.anti.rebuttals) ? r.anti.rebuttals : []).filter(x => x.verdict !== 'ÇÜRÜTÜLEMEDİ')
  const antiPicks = v26Picks(antiItems, x => `¬${x.target_id}`, x => `${x.negation} [${x.verdict}: ${x.note}]`, x => x.evidence_url, x => x.figure)
  const picks = tezPicks.concat(antiPicks)
  const rule = { tez: tezPicks.map(p => `${p.claim_id}(${p.why})`), antitez: antiPicks.map(p => `${p.claim_id}(${p.why})`) }
  if (!picks.length) return Promise.resolve({ ...r, v26: { family: fam.key, checks: [] }, v26_rule: rule })
  return agent(
`ROL: V26 örneklem-denetçisi (aile ${fam.key}). Aşağıdaki iddia→URL çiftleri KURAL-TABANLI seçildi. Her biri için KAYNAĞA İN (WebFetch): iddia ve rakam kaynak metinde GERÇEKTEN var mı? Sonuç: TUTUYOR / TUTMUYOR / ERİŞİLEMEDİ. Not: tek cümle — kaynakta ne gördün (rakamı aynen; kaynağın TARİHİNİ de yaz). Uydurma yok; yorum yok. Repoya dosya yazma, alt-ajan açma.
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
    const P = `Önerme P: ${c.claim}\n  kanıt: ${c.source_url} · rakam: ${c.figure} · kapsam/as-of: ${c.scope} · deterministik: ${c.determinism}`
    const N = x ? `Önerme ¬P: ${x.negation}\n  kanıt: ${x.evidence_url} · rakam: ${x.figure} · not: ${x.note} · karşı-tarafın öz-değerlendirmesi: ${x.verdict}` : `Önerme ¬P: (karşı-taraf bu önermeye itiraz getirmedi)`
    return `### ${c.id}\n${tezFirst ? 'Taraf-1 — ' + P + '\nTaraf-2 — ' + N : 'Taraf-1 — ' + N + '\nTaraf-2 — ' + P}`
  }).join('\n\n')
  const extras = ((r.anti && r.anti.extra_counter_claims) || []).map(c => `- [${c.id}] ${c.claim} — ${c.source_url} · ${c.figure} · ${c.scope} · deterministik: ${c.determinism}`).join('\n')
  const v26txt = (r.v26 && r.v26.checks || []).map(c => `- [${c.claim_id}] ${c.url} → ${c.result}: ${c.note}`).join('\n')
  return agent(
`ROL: MASKELİ HAKEM — aile ${fam.key}: ${fam.title}. Üretici koşumların devamı DEĞİLSİN; hangi tarafın tez/antitez olduğu söylenmiyor — iddia+kanıt olarak tart.
Ölçüt = adversarial-hayatta-kalma: çürütülemeyen SAĞLAM; kısmen çürüyen DARALDI (hayatta kalan hâl AS-OF damgalı); çürüyen DÜŞTÜ; uzlaşmaz ÇELİŞKİLİ. Kanıt gücü: birincil > ikincil; rakamlı > rakamsız; tarih damgalı > damgasız. V26 kuralı: bir tarafın denetlenen iddiası TUTMUYOR ise o tarafın o ailedeki TÜM iddiaları K'ya düşer. **AS-OF KURALI (Karar 68): damgasız (tarihsiz) iddia otomatik DARALDI ('as-of belirsiz') ya da DÜŞTÜ.** Hazır-ürün/sürüm taşıyan yapı-taşında sürümü ve tarihini KENDİN yeniden çek. Şüphede WebFetch (≤6).
DETERMİNİZM ÖNCELİĞİ (Karar 65): yapı-taşı deterministik değilse (h) ya "girmez" ya da deterministik varyantıyla birlikte; "modele hatırlatma" tek başına mekanizma değildir.
Sonda: JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI'dan; her biri AS-OF damgalı + URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + deterministic e/h/— + sürüm/veri-kümesi damgası) + kör noktalar (özellikle Türkçe lint · chat-çıktısı damgası · kesim-tarihi öz-bilgi ölçümü · kişisel-ölçek uygulama yoksa AÇIKÇA) + survival.
${BAGLAM}

## ÇİFTLER
${pairs}

## KARŞI-TARAFIN EK BULGULARI
${extras || '(yok)'}

## KAYNAK-DENETİMİ (bağımsız, kural-tabanlı örneklem)
${v26txt || '(yapılamadı)'}

## Tezin beyan ettiği boşluklar/engeller
${(r.tez.gaps||[]).map(g=>'- '+g).join('\n') || '(yok)'}
${(r.tez.access_blocks||[]).map(g=>'- ⚠ '+g).join('\n')}`,
    { label: `hakem:${fam.key}`, phase: 'Hakem', effort: 'high', schema: HAKEM_SCHEMA }
  ).then(hakem => ({ ...r, hakem, mask }))
}

log('gorev-2026-08-26-2 sahada: 3 aile (A LLM zamansal zemin · B bitemporal/as-of/TTL kayıt · C damga/doğrula-önce/lint pratiği) × tez(opus)→antitez(opus)→V26(sonnet)→hakem(üst model); as-of damgası zorunlu (Karar 68); determinizm-önceliği (Karar 65)')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: (args && args.emir) || 'cc/gorev-2026-08-26-2.md', families: out }