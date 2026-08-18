export const meta = {
  name: 'tarama-yontemleri-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — tarama yöntemleri (seq/index/index-only/bitmap/TID/parallel/sample/skip-scan; SQLite/DuckDB/grep tarama sözlüğü; ajan tarama stratejisi + plan-regresyon testi) — gorev-2026-08-18-3, pipeline tarama-yontemleri S-1',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları (üst model, high)' },
  ],
}

const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi (Claude Code). Veri: bronz (git-izlenen md/jsonl ~9,5 MB) → silver SQLite (kayit 41.961 satır, referans 50.718; indeksler ix_kayit_dosya(dosya_id,sira), ix_ref_kayit, ix_ref_tur_deger; ANALYZE hiç koşmamış) → gold görünüm/CSV; opsiyonel kolon katmanı (parquet + DuckDB, PR'da). Sahibin talebi (aynen): "bağlam tablo verileriyle tarama yapacağın zaman seq scan gibi diğer tarama metotlarını araştırıp nasıl kullanacağını sisteme entegre etmek üzere araştır" — yani: hangi tarama yöntemleri var (seq scan, index scan, index-only, bitmap, TID, parallel, sample, skip-scan …), hangi soruda/veride hangisi seçilir, Jarvis'in motorlarında (SQLite · DuckDB/parquet · grep) karşılıkları ne, ajan (Carvis) erişim yolunu nasıl seçmeli ve bu bir plan-testi olarak sisteme nasıl gömülür. Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin, Jarvis için tasarım/kod yapmazsın.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; yeniden keşfetme, ÜSTÜNE KOY):
- Jarvis sondajı (08-18, SQLite 3.51.0, EXPLAIN QUERY PLAN, kopya DB, sıcak): SELECT count(*) FROM kayit → SCAN kayit USING COVERING INDEX 0,07 ms · WHERE blok_turu=… (indekssiz) → SCAN kayit 5,4 ms · rowid BETWEEN → SEARCH USING INTEGER PRIMARY KEY 0,03 ms · kayit_id='x' OR (ref_turu=… AND ref_deger=…) → MULTI-INDEX OR 0,01 ms · dosya_id LIKE 'core/%' → SCAN USING COVERING INDEX 0,81 ms (LIKE önek optimizasyonu SEARCH'e dönmedi; case_sensitive_like kapalı) · join indekssiz kolonda → SEARCH USING AUTOMATIC COVERING INDEX 28,3 ms · IN(…) → SEARCH COVERING 0,01 ms · skip-scan: bileşik indeksin 2. kolonu ref_deger='K-015' ANALYZE ÖNCESİ SCAN COVERING 1,08 ms → ANALYZE SONRASI SEARCH (ANY(ref_turu) AND ref_deger=?) 0,02 ms (54×) · ORDER BY dosya_id,sira LIMIT 5 → SCAN COVERING 0,01 ms. Noktasal PK 0,004 ms; LIKE '%…%' SCAN 16 ms; .expert danışmanı çalışıyor. grep -rc bronz md 0,24 s; ripgrep ≈0. Parquet: kayit 11 row group (ROW_GROUP_SIZE 4096, dosya_id sıralı); DuckDB Q1 kolon-chunk 60 KB ↔ SQLite ~41 MB sayfa.
- Verili raporlar: index seek mekanizması (SQLite SEARCH; rowid ikinci iniş; covering; 'index seek' SQL Server terimi; Postgres Index Scan/IOS/Bitmap) · kolon deposu (geç materyalizasyon 3× + sıkıştırma 2×; kolon taklidi kaybeder; Jarvis ölçeğinde önbellek-içi → CPU) · KB-53 erişim yolu (adres → aralık; katman-olcum EQP testi 'noktasal sorgu SCAN olmaz' icra borcu İB-25) — bu koşum İB-25'i kapsayan plan-regresyon testi için kanıt toplar.
- Kanon: deterministik tasarım · hazırı temel al · pointer ilkesi · veri katmanı v1 (stdlib/SQLite; yazım-anı ölçüm kapısı) · token −%30 · açık-kaynak okunabilirlik.
- Bilinmeyen (çekirdek): tarama kataloğu + planlayıcı seçim mantığı (ölçülmüş geçiş noktaları) · SQLite'ta hangi optimizasyonların ANALYZE/ayar gerektirdiği (skip-scan, LIKE, OR) · parquet/DuckDB tarama davranışı küçük ölçekte · ajan için 'hangi soruda hangi tarama' ölçülmüş kural · plan-regresyon testi deseninin en yalın taşınabilir hâli.
- Kural: motor + sürüm DAMGASI zorunlu (PG17/18 · SQLite 3.51 · DuckDB 1.4/1.5 · ripgrep sürümü); satıcı beyanı D sayılmaz.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / kaynak kodu README / hakemli makale / GitHub). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam/sürüm yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı. Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz.
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma. Motor+sürüm damgası her iddiada.
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, Jarvis kuralı/kodu TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'TARAMA YÖNTEMLERİ KATALOĞU + PLANLAYICI SEÇİMİ (Postgres kanonu)',
    questions: `A1. Katalog (PG17/18 resmî): Seq Scan · Index Scan · Index Only Scan · Bitmap Index Scan + Bitmap Heap Scan (exact/lossy, Recheck) · TID Scan / TID Range Scan · Parallel Seq/Index/Bitmap Scan (worker sayısı, min_parallel_table_scan_size) · Sample Scan (TABLESAMPLE SYSTEM/BERNOULLI) · Function/Values/CTE/Subquery Scan · Skip Scan (PG18) — her biri: ne yapar, ne zaman seçilir, EXPLAIN'de nasıl görünür (rows/loops/Buffers/Heap Fetches/Heap Blocks).
A2. Planlayıcı seçim mantığı: maliyet formülü + seçicilik (istatistik, korelasyon) → seq↔bitmap↔index geçiş noktaları; resmî örnekler (using-explain tenk1: hangi filtrede hangi düğüm); "küçük tabloda seq scan optimal" kuralı; enable_seqscan/enable_indexscan/… GUC'ları teşhis aracı olarak; ölçülmüş geçiş yüzdesi var mı (dolaşımdaki %5-10 kuralı birincil kaynakta doğrulandı mı).
A3. Ölçüm/okuma: EXPLAIN (ANALYZE, BUFFERS, COSTS OFF), auto_explain, pg_stat_user_tables (seq_scan/idx_scan sayaçları — "tarama-yöntemi karışımı" metriği), pg_stat_statements; hangi metrik "yanlış tarama yöntemi" alarmıdır (sayı+kaynak).
A4. Anti-desenler/kayıp durumları (resmî/hakemli): düşük seçicilikte index scan (rastgele G/Ç), bitmap lossy'ye düşme (work_mem), parallel scan küçük tabloda ek yük, TABLESAMPLE SYSTEM'in blok yanlılığı — ölçüm.`,
    antitezHint: 'geçiş noktaları donanım/önbellek bağımlı, evrensel eşik yok · TABLESAMPLE/parallel küçük tabloda anlamsız · Postgres kataloğu SQLite/DuckDB\'ye birebir taşınmaz · pg_stat sayaçları tek kullanıcıda gürültü.' },
  { key: 'B', title: 'JARVIS MOTORLARINDA TARAMA SÖZLÜĞÜ (SQLite + DuckDB/parquet + grep)',
    questions: `B1. SQLite EQP sözlüğü (resmî eqp.html / queryplanner.html / optoverview.html): SCAN table · SCAN … USING [COVERING] INDEX (indeks-sıralı ya da indeks-only tam tarama) · SEARCH … USING INDEX / INTEGER PRIMARY KEY (rowid aralığı) · MULTI-INDEX OR · AUTOMATIC [COVERING] INDEX (ne zaman kurulur, maliyeti) · skip-scan (koşul: ANALYZE + stat1; ortalama-tekrar eşiği — sayı+kaynak) · LIKE/GLOB optimizasyonu (case_sensitive_like, NOCASE indeks) · IN operatörü · ORDER BY indeksle · USE TEMP B-TREE · kısmi/ifade indeksleri; her etiket için ne zaman seçilir, PRAGMA optimize/ANALYZE bağımlılığı.
B2. SQLite planlayıcı davranışı (NGQP): stat1 yokken varsayımlar; .expert ile öneri; sorgu-plan kararlılığı sürümler arası (3.4x→3.5x değişen optimizasyonlar) — resmî sürüm notları/doküman.
B3. DuckDB/parquet tarama: projection pushdown, filter pushdown (row-group min/max, bloom), paralel row-group taraması, EXPLAIN ANALYZE çıktısı, SAMPLE/USING SAMPLE (reservoir/bernoulli/system) — küçük dosyada davranış; sqlite_scanner üzerinden pushdown var mı.
B4. Metin taraması: grep/ripgrep mekanizması (bellek-haritalı, SIMD, .gitignore, paralel), ölçülmüş hız kıyası (resmî benchmark), FTS5 ile sınır (ne zaman grep yeter, ne zaman indeks) — kaynaklı.`,
    antitezHint: 'SQLite optimizasyonları sürümle değişir, skip-scan/LIKE koşulları kırılgan · grep zaten yeter (0,24 s) · DuckDB pushdown küçük dosyada ölçüsüz · AUTOMATIC INDEX zaten yeterince akıllı, indeks bakımı gereksiz.' },
  { key: 'C', title: 'AJAN TARAMA STRATEJİSİ + ENTEGRASYON DESENLERİ (plan-regresyon testi, tarama-karışımı metriği, küçük-veri kuralı)',
    questions: `C1. Ajan/LLM'in erişim-yolu seçimi (Claude Code Read/Grep/Glob dokümanı; Anthropic context engineering "agentic search"; ilerlemeli açığa çıkarma): tam okuma ↔ grep ↔ işaretçi/indeks ↔ örnek (head/TABLESAMPLE) ↔ agregasyon — resmî tavsiye + ölçülmüş token/doğruluk (varsa; yoksa AÇIKÇA yok).
C2. Plan-regresyon testi deseni: Postgres regress testleri EXPLAIN (COSTS OFF) plan-şekli assert'leri; SQLite test takımı do_eqp_test/do_execsql_test EQP karşılaştırması; sqllogictest; CI'da "plan değişti" alarmı; pg_hint_plan/pg_plan_guarantee (yalnız envanter) — küçük bir depoya taşınabilir en yalın biçim (kaynaklı).
C3. Tarama-yöntemi karışımı metriği: pg_stat_user_tables.seq_scan/idx_scan, SQLite sqlite3_stmt_status (FULLSCAN_STEP/AUTOINDEX/…), DuckDB OPERATOR_ROWS_SCANNED — "yanlış yöntem" alarm eşikleri (kaynaklı); tek-kullanıcı ölçekte anlamı.
C4. Küçük veri kuralı: "her şeyi seq scan yap" ne zaman doğru (tablo ≤ N sayfa; bellek-içi), indeks/istatistik bakımının maliyeti ne zaman kazancı aşar — ölçülmüş/resmî; LLM'in plan metnini okuyup doğru yöntemi seçebilmesi (text-to-SQL + EXPLAIN geri-besleme çalışmaları) — sayı+kaynak.`,
    antitezHint: 'plan-regresyon testi küçük tek-kullanıcı repoda bakım yükü · LLM plan okuma ölçümü yok · "her şeyi seq scan" bu ölçekte doğru · sqlite3_stmt_status sayaçları Python\'dan erişilemez.' },
]

const PLACEMENTS = ['tarama-terim','seçim-kuralı','ölçülmüş-eşik','motor-ayarı','erişim-deseni','ölçüm-yöntemi','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','placement_suggestion'],
  properties: {
    id: { type: 'string' }, claim: { type: 'string' }, label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string' }, figure: { type: 'string' }, scope: { type: 'string' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') + motor-sürüm damgası' },
  } }
const TEZ_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','claims','gaps','access_blocks','budget_note'],
  properties: { family: { type: 'string' }, claims: { type: 'array', minItems: 4, maxItems: 10, items: CLAIM }, gaps: { type: 'array', items: { type: 'string' } }, access_blocks: { type: 'array', items: { type: 'string' } }, budget_note: { type: 'string' } } }
const REBUT = { type: 'object', additionalProperties: false, required: ['target_id','negation','verdict','evidence_url','figure','note'],
  properties: { target_id: { type: 'string' }, negation: { type: 'string' }, verdict: { type: 'string', enum: ['ÇÜRÜTÜLDÜ','DARALTILDI','ÇÜRÜTÜLEMEDİ'] }, evidence_url: { type: 'string' }, figure: { type: 'string' }, note: { type: 'string' } } }
const ANTI_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','rebuttals','extra_counter_claims','budget_note'],
  properties: { family: { type: 'string' }, rebuttals: { type: 'array', maxItems: 10, items: REBUT }, extra_counter_claims: { type: 'array', maxItems: 3, items: CLAIM }, budget_note: { type: 'string' } } }
const V26_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','checks'],
  properties: { family: { type: 'string' }, checks: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','url','result','note'], properties: { claim_id: { type: 'string' }, url: { type: 'string' }, result: { type: 'string', enum: ['TUTUYOR','TUTMUYOR','ERİŞİLEMEDİ'] }, note: { type: 'string' } } } } } }
const HAKEM_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','verdicts','building_blocks','blind_spots','survival'],
  properties: {
    family: { type: 'string' },
    verdicts: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['claim_id','verdict','surviving_form','reason'], properties: { claim_id: { type: 'string' }, verdict: { type: 'string', enum: ['SAĞLAM','DARALDI','DÜŞTÜ','ÇELİŞKİLİ'] }, surviving_form: { type: 'string' }, reason: { type: 'string' } } } },
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','jarvis','confidence'], properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS }, jarvis: { type: 'string', enum: JARVIS }, confidence: { type: 'string', enum: ['D','K'] } } } },
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
Çıktı: 4-10 iddia (her soruya ≥1), her biri kaynaklı; gaps/access_blocks/budget_note doldur. Sayısal iddialarda figure alanı ZORUNLU dolu; her iddiada motor+sürüm damgası.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')
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
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + motor-sürüm damgası; 'ölçülmüş-eşik' yalnız ölçülmüş dayanakla; 'seçim-kuralı' = 'hangi soruda/veride hangi tarama' biçiminde tek cümle) + kör noktalar (aranıp bulunamayan; özellikle küçük-ölçek 10⁴-10⁵ satır ve ajan erişim-yolu ölçümü yoksa AÇIKÇA) + survival sayımı.
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

log('gorev-2026-08-18-3 sahada (pipeline tarama-yontemleri S-1): 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: 'cc/gorev-2026-08-18-3.md', families: out }