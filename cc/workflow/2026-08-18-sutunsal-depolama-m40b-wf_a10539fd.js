export const meta = {
  name: 'sutunsal-depolama-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — sütunsal depolama: bağlam veri ambarından kolon-bazlı okuma/yazma Jarvis ölçeğinde nasıl; hazır ürünler; ölçülmüş eşik (gorev-2026-08-18-2, pipeline kolon-katmani S-1)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-18-2.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi; Claude Code üzerinde çalışır. Veri katmanı: bronz (git-izlenen md/jsonl) → silver (SQLite tablolar, 51 MB) → gold (SQL görünümleri + CSV); ayrıca aynı SQLite'ta ayrı şema "bağlam veri ambarı" (amb_* olgu/boyut tabloları + martlar). Sahibin talebi (aynen): "Columnar storage — Redshift'te veriler satır satır değil kolon kolon diskte ayrı bloklar hâlinde tutulur; sorgu birkaç kolona ihtiyaç duyduğunda gereksiz kolonları hiç diskten okumadan atlar, geniş çok-satırlı aggregation sorgularında I/O'yu minimuma indirir. Bağlam veri ambarı üzerinden OLAP-tarzı analiz yapacağımız zaman ambardan kolon-bazlı okuma ve yazma yapabilmeliyiz. Nasıl yapacağımızı araştır; hazır ürünler varsa sıfırdan yazma." Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin, Jarvis için tasarım/kod yapmazsın.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; yeniden keşfetme, ÜSTÜNE KOY):
- Jarvis sondajı (deterministik, 08-18; izole venv duckdb 1.4.5; SQLite 3.51.0): en büyük tablo kayit 41.961 satır (34,2 MB sayfa; geniş metin kolonu ort. 222 B) · referans 50.718 · amb_olgu_kosum 248 · karar_borcu 67; gold = görünüm + CSV (~140 KB izlenen). Parquet yazımı (DuckDB COPY TO, ZSTD): kayit 174 ms → 6,85 MB (metin 3,75 · metin_kisa 2,31 · kayit_id 0,41 · token_kestirim 0,05 MB); referans 41 ms → 0,56 MB; sıralı (ORDER BY dosya_id, ROW_GROUP_SIZE 4096) 65 ms → 7,18 MB / 11 row group. Okuma (sıcak önbellek): Q1 dosya×token group-by SQLite 7,6 ms ↔ DuckDB←sqlite_scanner 10,7 ↔ parquet 0,7 ↔ native 0,8 ms; Q2 11,2/8,8/0,5/0,8; Q3 6,2/8,0/0,5/0,4; Q4 2,0/7,1/1,3/1,7; Q5 join 72,9/19,6/6,1/3,9; Q6 avg(length(metin)) geniş kolon 13,6/10,2/17,5/1,6. Q1 okunan byte: parquet 0,05 MB = %0,8 ↔ SQLite ~34,2 MB tarar. Karşı-sondaj: SQLite covering indeks (dosya_id, token_kestirim) → Q1 1,3 ms, 1,84 MB okur (sorgu başına "dikey dilim", her kolon-kombinasyonu ayrı indeks ister). Kurulu değil: duckdb CLI, pyarrow, polars.
- Verili (önceki raporlar): parquet iç mekanizması (row group/page/encoding/min-max/bloom/sort key/ROW_GROUP_SIZE) ARAŞTIRILDI — yeniden açma · OLTP↔OLAP = erişim-tasarımı ayrımı; SQLite satır-yönelimli, DuckDB gömülü×analitik; kazanç eşik-koşullu (~1M satır 20-50×; <100k rejimi ölçüsüz); "DuckDB/ayrı motor ≤10 MB'da kanıtsız, yerel ölçüm şart" · OLTP noktasal erişim (index seek) ayrı raporda.
- Kanon kısıtları: veri katmanı v1 stdlib/SQLite; "grep+SQLite'ı geçmeyen katman eklenmez; ölçüm tetikli"; additive-only şema + sözleşme + yazım-anı ölçüm kapısı; her ship ≥1 DE-artefakt; deterministik tasarım; hazırı temel al; gold CSV git'te izlenir, sqlite/jsonl gitignore; açık-kaynak okunabilirlik.
- Bilinmeyen (çekirdek): kolon deposunun ölçülmüş kazancının küçük ölçekte (10⁴-10⁵ satır, <100 MB) genel eşiği · Redshift mekaniklerinin gömülü karşılığı ve DEA-C01 eşleme tablosu · "kolon-bazlı yazma" için doğru yazım deseni ve Iceberg/Delta gereksizlik eşiği · DuckDB depolama-biçimi kararlılığı/tek-yazıcı sınırları · parquet'i git'te izleme sınırı · "okunan byte" ölçüm yöntemi.
- Kural: motor + sürüm DAMGASI zorunlu (DuckDB 1.x · Redshift RA3/serverless tarih · SQLite 3.51 · Parquet format); satıcı beyanı D sayılmaz.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / hakemli makale (SIGMOD/VLDB) / standart spec / GitHub). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam/sürüm yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı. Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz (Redshift/DuckDB/Polars benchmark'ları metodoloji görülmedikçe K).
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma. Motor+sürüm damgası her iddiada.
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, Jarvis şeması/kodu TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'MEKANİZMA + ÖLÇÜLMÜŞ KAZANÇ (kolon ↔ satır; Redshift somutu; yazma semantiği; küçük ölçek)',
    questions: `A1. Kolon-deposu üstünlüğünün kaynağı (Abadi-Madden-Hachem 2008 SIGMOD "Column-Stores vs. Row-Stores: How Different Are They Really?": satır deposunda dikey partisyon / indeks-only simülasyonu neden yetmez; geç materyalizasyon, sıkıştırma, blok iterasyonu, invisible join — hangi bileşen kaç kat; C-Store/Vertica, MonetDB/X100 vektörlü yürütme; "Design and Implementation of Modern Column-Oriented DB Systems" 2013) — sayı + kaynak; kolon deposu ne zaman KAYBEDER (noktasal/geniş-satır getirme, küçük tablo, çok-kolon seçimi; tuple reconstruction maliyeti) — ölçüm varsa.
A2. Redshift somut mekanikleri (resmî AWS dokümanı): kolon başına 1 MB blok, zone map (blok min/max), sort key (compound/interleaved), dist key/style, sıkıştırma encoding'leri (AZ64/LZO/ZSTD/… otomatik), COPY toplu yükleme, VACUUM/ANALYZE, küçük-yazım anti-deseni (tek satır INSERT), materialized view; her biri için sayı+URL; hangi kavramın gömülü/parquet karşılığı olduğu (yalnız kaynaklı eşleştirme).
A3. "Kolon-bazlı YAZMA" gerçekte ne: kolon depolarında yazım toplu/row-group'tur (immutable dosya, append + compaction; C-Store WS/RS + tuple mover; Redshift unsorted region; DuckDB row group + WAL); tek-satır güncelleme = yeniden yazım; ölçülmüş yazım maliyeti/amplifikasyon; "kolon-bazlı okuma+yazma" isteği için doğru işlem birimi.
A4. Küçük ölçek: kolon↔satır farkının ÖLÇÜLDÜĞÜ en küçük veri seti/bellek-içi rejim (bellek-içi/önbellekte I/O tasarrufu → CPU/bellek-bandı tasarrufuna döner mü; sayı); "I/O'ya hiç dokunmama" iddiasının sıcak-önbellek altında anlamı.`,
    antitezHint: 'kolon-deposu kazancı yalnız disk-I/O-bağlı büyük veride; bellek-içi küçük tabloda fark yok/tersine · satır deposunda covering indeks aynı I/O tasarrufunu verir · Redshift mekanikleri gömülüye taşınmaz · geç materyalizasyon çok-kolon seçiminde kaybettirir.' },
  { key: 'B', title: 'GÖMÜLÜ HAZIR ÜRÜNLER JARVIS ÖLÇEĞİNDE (motor/format tarafı)',
    questions: `B1. DuckDB (sürüm damgalı): native depolama ↔ parquet dış tablo ↔ sqlite_scanner (hangisi ne zaman), COPY TO parquet seçenekleri (ROW_GROUP_SIZE, COMPRESSION, PARTITION_BY, KV_METADATA), parquet_metadata(), EXPLAIN ANALYZE/profiling ile okunan byte, tek-yazıcı/eşzamanlılık modeli, DEPOLAMA BİÇİMİ sürümler arası kararlılığı (native .duckdb ↔ parquet taşınabilirliği), Python/CLI kurulum boyutu, lisans; dbt-duckdb (parquet ihracı) — resmî.
B2. Format seçenekleri: Parquet ↔ Arrow IPC/Feather ↔ DuckDB native ↔ CSV (bugünkü gold) — okuma/yazma/boyut/araç-desteği ölçümleri (resmî/hakemli); parquet'te şema evrimi (union_by_name), key-value metadata (SHA/tazelik damgası için), sıralama/row-group ayarı küçük dosyada.
B3. Alternatif motorlar/kütüphaneler: Polars (lazy scan_parquet, projection pushdown), pyarrow.dataset, chDB/ClickHouse-local, SQLite tarafında "kolon" (covering indeks dikey dilim — sınırı; sqlite-parquet-vtable üçüncü parti durumu) — hangisi "hazırı temel al"a uyar, bakım/olgunluk damgası.
B4. Git'te ikili veri: parquet dosyalarını repo'da izlemenin sınırları (GitHub dosya/repo boyut sınırları, LFS, diff'siz ikili; küçük gold parquet ↔ büyük silver parquet), açık-kaynak okunabilirlik açısından CSV↔parquet ikilemi — resmî sınırlar + yaygın pratik (kaynaklı).`,
    antitezHint: 'DuckDB depolama biçimi sürümler arası bozulur, tek-yazıcı, kurulum ağır · parquet git\'te ikili yük, diff yok · CSV yeter · Polars/chDB gereksiz katman · sqlite covering indeks yeterli.' },
  { key: 'C', title: 'AMBAR OKUMA/YAZMA TASARIM DESENLERİ (gold = parquet "lakehouse-lite" + ölçüm + DEA-C01 eşleme)',
    questions: `C1. Dosya-tabanlı analitik katman deseni: medallion gold'un parquet olarak yazımı — partisyon (Hive-style; küçük veride "partisyonlama zararlı" eşiği), sort key seçimi, idempotent partisyon üstüne-yazma (functional DE) ↔ append-only + compaction; Iceberg/Delta/Hudi'nin gereksizlik eşiği (tek yazıcı, <1 GB, snapshot=git); DuckDB'nin delta/iceberg eklentileri (yalnız durum).
C2. Şema sözleşmesi + tazelik: parquet şema evrimi additive kuralı, dbt/dlt/great-expectations "schema contract" desenleri, üretim damgası (git SHA, kod SHA) parquet KV metadata'da; silver (SQLite) ↔ gold (parquet) eşdeğerlik testi (aynı sorgu iki motorda aynı sonuç) — yayımlanmış desen/araç.
C3. Ölçüm yöntemi: sorgu başına okunan byte / row group eleme (DuckDB profiling EXPLAIN ANALYZE, PRAGMA enable_profiling, parquet_metadata) — küçük ölçek için "kolon katmanı kazandırdı mı" kanıt tasarımı; katman-oran metrikleri (bronz/silver/gold byte); benchmark disiplini (sıcak/soğuk önbellek, tekrar sayısı).
C4. Redshift ↔ gömülü eşleme (DEA-C01 öğrenme değeri, kaynaklı): sort key ↔ ORDER BY row-group · zone map ↔ parquet min/max · dist key ↔ (yok/partisyon) · encoding ↔ parquet dictionary/ZSTD · COPY ↔ COPY TO/FROM · VACUUM ↔ compaction/rewrite · ANALYZE ↔ metadata istatistikleri · materialized view ↔ gold parquet; ajan/LLM'in analitik sorgu yolu (DuckDB MCP durumu, text-to-SQL üzerinden gold sorgusu) — yalnız kaynaklı.`,
    antitezHint: 'partisyon/lakehouse küçük veride zararlı (small files) · parquet immutability "kolon-bazlı yazma"yı toplu yeniden yazıma indirger · Iceberg/Delta gereksiz ama tutarlılığı kim sağlar · okunan-byte ölçümü önbellek altında anlamsız · Redshift↔parquet eşlemesi öğretici benzetme, mekanik değil.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['mekanizma-terim','ölçülmüş-eşik','hazır-ürün','yazım-deseni','okuma-deseni','ölçüm-yöntemi','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih/sürüm (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'motor + sürüm + örneklem/kapsam; yoksa "-"' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') + motor-sürüm damgası' },
  } }
const TEZ_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','claims','gaps','access_blocks','budget_note'],
  properties: {
    family: { type: 'string' },
    claims: { type: 'array', minItems: 4, maxItems: 10, items: CLAIM },
    gaps: { type: 'array', items: { type: 'string' } },
    access_blocks: { type: 'array', items: { type: 'string' } },
    budget_note: { type: 'string' },
  } }
const REBUT = { type: 'object', additionalProperties: false, required: ['target_id','negation','verdict','evidence_url','figure','note'],
  properties: {
    target_id: { type: 'string' },
    negation: { type: 'string' },
    verdict: { type: 'string', enum: ['ÇÜRÜTÜLDÜ','DARALTILDI','ÇÜRÜTÜLEMEDİ'] },
    evidence_url: { type: 'string' },
    figure: { type: 'string' },
    note: { type: 'string' },
  } }
const ANTI_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','rebuttals','extra_counter_claims','budget_note'],
  properties: {
    family: { type: 'string' },
    rebuttals: { type: 'array', maxItems: 10, items: REBUT },
    extra_counter_claims: { type: 'array', maxItems: 3, items: CLAIM },
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
      properties: { claim_id: { type: 'string' }, verdict: { type: 'string', enum: ['SAĞLAM','DARALDI','DÜŞTÜ','ÇELİŞKİLİ'] }, surviving_form: { type: 'string' }, reason: { type: 'string' } } } },
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','jarvis','confidence'],
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS }, jarvis: { type: 'string', enum: JARVIS }, confidence: { type: 'string', enum: ['D','K'] } } } },
    blind_spots: { type: 'array', items: { type: 'string' } },
    survival: { type: 'object', additionalProperties: false, required: ['saglam','daraldi','dustu','celiskili'], properties: { saglam: { type: 'integer' }, daraldi: { type: 'integer' }, dustu: { type: 'integer' }, celiskili: { type: 'integer' } } },
  } }

// ---------- V26 KURAL-TABANLI seçim (Salih imzası 08-17; deterministik) ----------
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

// ---------- aşamalar ----------
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
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + motor-sürüm damgası; 'ölçülmüş-eşik' yalnız ölçülmüş dayanakla; 'hazır-ürün' yalnız bakım/sürüm durumu bilinen ürünlerde) + kör noktalar (aranıp bulunamayan; özellikle küçük-ölçek 10⁴-10⁵ satır ölçümü ve önbellek-altı I/O iddiası yoksa AÇIKÇA) + survival sayımı.
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

log('gorev-2026-08-18-2 sahada (pipeline kolon-katmani S-1): 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: 'cc/gorev-2026-08-18-2.md', families: out }