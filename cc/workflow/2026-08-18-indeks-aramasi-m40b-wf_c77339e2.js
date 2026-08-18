export const meta = {
  name: 'indeks-aramasi-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — index seek (B-tree traversal + heap fetch) mantığı Jarvis bağlam verisinde satır-bazlı erişim için nasıl kullanılır; hazır ürünler (gorev-2026-08-18-1)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-18-1.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi; Claude Code (terminal/masaüstü) üzerinde çalışır. Sahibin sorusu (aynen): "index'in kök-dal-yaprak katmanlarında gezinip aranan değerin heap'teki adresini bulması ve o adrese tek seferde 'atlaması' sürecine index seek (bazı kaynaklarda index scan) denir. Ham bağlam verisini kullanıp spesifik satır-bazlı bir işlem yapmamız gerekeceği zaman (OLTP gibi), Postgres'in işleyiş mantığından 'B-tree traversal + heap fetch' mantığını nasıl kullanırız? Bu işi kolaylaştıracak halihazırda kullanılan metod/uygulama/tool ürünleri varsa sıfırdan inşa etmek yerine onları sistemde kullanacak şekilde tasarla." Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin, Jarvis için tasarım yapmazsın.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; yeniden keşfetme, ÜSTÜNE KOY):
- Jarvis sondajı (deterministik, 08-18): ham bağlam = bronz (git-izlenen 492 md/json/jsonl ~9,5 MB) → silver veri/baglam.sqlite (SQLite 3.51.0; 51 MB; 4 KB sayfa; 12.464 sayfa; journal_mode=delete, WAL değil; ANALYZE hiç koşmamış — sqlite_stat1 yok; tablolar rowid'li, WITHOUT ROWID yok). kayit 41.961 satır (markdown bloğu; PK kayit_id = "<yol>#<satir_bas>-<satir_son>#<sha8>" ≈49 karakter = dosya+satır-aralığı ADRESİ; metin ort. 222 B, maks 10,6 KB) · referans 50.718 · json_kayit 6.724 · hareket 1.440 · dosya 492 · anahtar 321 · karar_borcu 67. İndeksler: PK autoindex'ler + ix_kayit_dosya(dosya_id,sira) · ix_ref_kayit(kayit_id) · ix_ref_tur_deger(ref_turu,ref_deger) · ix_json_dosya(dosya_id). B-tree derinlikleri (dbstat): kayit tablo b-tree 3 seviye (kök 19 hücre → 20 iç → 8.317 yaprak, +14 overflow) · kayit PK indeksi 3 seviye · ix_ref_tur_deger 3 seviye · karar_borcu tablo 2 seviye, PK indeksi 1 sayfa. Planlar: PK noktasal → SEARCH USING INDEX 0,004 ms · dosya+satır aralığı → SEARCH ix_kayit_dosya 0,005 ms · referans→kayit JOIN iki SEARCH 143 satır 0,10 ms · metin LIKE '%…%' → SCAN 16,2 ms · indekssiz satir_bas=? → SCAN 5,3 ms; CLI .expert bu sorguya CREATE INDEX kayit(satir_bas,satir_son) önerdi (danışman çalışıyor). Derleme: FTS5 ✓ DBSTAT ✓ RTREE ✓. Kurulu DEĞİL: sqlite3_analyzer, duckdb, psql/postgres, datasette, sqlite-utils. grep -rn bronz md üstünde 0,25 s; sed -n 'N,Np' ≈0 ms (dosya-satır = "heap" adresi). Bugünkü erişim: Read/Grep/sed (dosya) + sqlite3 CLI/Python (görünüm/CSV); silver'a satır-bazlı YAZIM YOK — hat silver'ı bronz'dan SIFIRDAN yeniden üretir (tmp→replace, functional DE, idempotens kanıtlı).
- Verili (önceki raporlar): OLTP↔OLAP ayrımı ERİŞİM-TASARIMI ayrımıdır (şema · indeks türü · görünüm materyalizasyonu); SQLite satır-yönelimli B-ağacı yürütücüsü, OLAP'ta zayıf; Jarvis ölçeğinde motor ayrımı gerekmez, üstünlük eşik-koşullu (~1M satır 20-50×; <100k rejimi ölçüsüz). Tam-metin erişim = SQLite FTS5+bm25 (ayrı masa kalemi; BU koşumda kapsam dışı). Vektör DB yok (bilinçli erteleme). Pointer ilkesi: özet + adres. Deterministik tasarım. HAZIRI TEMEL AL. Token −%30.
- Bilinmeyen (çekirdek): heap fetch'in tam mekanizması ve "tek atlama" iddiasının sınırları · terim haritası (seek↔scan hangi motorda ne) · SQLite'ta aynı yolun adı/ölçümü ve hangi hazır ürün satır-bazlı erişim/yazımı kodsuz karşılar · ajan tarafında "işaretçi → atlama" erişiminin ÖLÇÜLMÜŞ kazancı ve MCP/CLI ürünlerin güvenlik-olgunluğu.
- Kural: motor + sürüm DAMGASI zorunlu (Postgres 16/17 · SQLite 3.4x/3.5x · InnoDB 8.x · SQL Server); satıcı beyanı D sayılmaz.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / kaynak kodu README / standart metni / arXiv-ACL / GitHub). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam/sürüm yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur (rakam · yüzde · tarih · sayım · sürüm) — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz (benchmark tablosu/metodoloji görülmedikçe K).
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma. Motor+sürüm damgası her iddiada.
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, Jarvis şeması TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'MOTOR MEKANİZMASI + TERİM HARİTASI (Postgres kanonu)',
    questions: `A1. Postgres B-tree inişi: kök→iç→yaprak (Lehman-Yao B-link; src/backend/access/nbtree/README), sayfa 8 KB, fanout ↔ derinlik (kaç satırda kaç seviye — sayı+kaynak), yaprakta ne var (index tuple + TID = blok no + satır işaretçisi), _bt_search/_bt_first; heap fetch = TID ile heap sayfası + line pointer → tuple; NEDEN heap fetch zorunlu (indekste görünürlük yok — MVCC xmin/xmax; HOT zinciri).
A2. Plan düğümleri + planlayıcı seçimi: Index Scan (seek + range, satır başına heap fetch) · Index Only Scan (visibility map all-visible ise heap atlanır; INCLUDE covering) · Bitmap Index Scan + Bitmap Heap Scan (çok satırda TID'leri sırala, heap'i sıralı oku) · Seq Scan; maliyet sabitleri (seq_page_cost=1, random_page_cost=4, cpu_index_tuple_cost, effective_cache_size), planlayıcının hangi seçicilikte hangi düğümü seçtiği (sayı varsa); EXPLAIN (ANALYZE, BUFFERS) ile heap fetch sayısı ("Heap Fetches: n", shared hit/read) — ölçüm yöntemi.
A3. Terim haritası (resmî dokümanla): SQL Server "Index Seek" ↔ "Index Scan" (+ Key Lookup/RID Lookup = heap fetch) · Postgres "Index Scan / Index Only Scan / Bitmap" (Postgres'te "seek" terimi var mı?) · MySQL/InnoDB clustered PK + secondary index → PK ile ikinci arama (EXPLAIN type ref/eq_ref/range/index) · SQLite "SEARCH … USING INDEX" ↔ "SCAN". Sahibin cümlesi ("index seek, bazı kaynaklarda index scan; tek seferde atlama") hangi motor için ne kadar doğru — kaynaklı düzeltme.
A4. Heap ↔ kümelenmiş yerleşim: Postgres heap sırasızdır (CLUSTER tek-seferlik, pg_stats.correlation), InnoDB/SQL Server clustered index = tablo; heap fetch maliyeti korelasyona bağlı (sayı+kaynak); HOT (heap-only tuple) güncellemelerin indeks bakımı; fillfactor.`,
    antitezHint: '"index seek" evrensel terim değil · Postgres index scan "tek atlama" değil (satır başına heap fetch, rastgele G/Ç; küçük tabloda seq scan kazanır; index-only scan visibility map\'e bağlı) · derinlik/fanout sayıları veri tipine bağlı, sabit değil.' },
  { key: 'B', title: 'JARVIS MOTORU SQLite: AYNI MEKANİZMA + HAZIR ÜRÜNLER (motor tarafı)',
    questions: `B1. SQLite dosya biçimi: tablo b-tree (rowid anahtarlı; veri yaprakta = fiilen kümelenmiş "heap"), indeks b-tree (anahtar + rowid yaprakta), noktasal sorgu = indeks inişi + rowid ile tablo b-tree'ye ikinci iniş (heap fetch eşdeğeri); covering index (ikinci iniş atlanır — EQP'de "COVERING INDEX"), WITHOUT ROWID (clustered PK), overflow sayfaları (büyük metin), sayfa boyutu/derinlik/fanout (sayı+kaynak; resmî fileformat.html + queryplanner.html).
B2. Planlayıcı + ölçüm: NGQP, EXPLAIN QUERY PLAN (SEARCH/SCAN/COVERING/AUTOMATIC INDEX), ANALYZE/sqlite_stat1/PRAGMA optimize (etkisi ne zaman görülür; küçük tablolarda planı bozar mı — kaynak), kısmi/ifade indeksleri, JSON generated column + indeks, PRAGMA index_info/index_xinfo, dbstat/sqlite3_analyzer (derinlik, sayfa), CLI .expert (sqlite3_expert — nasıl çalışır, güvenilirlik), WAL modu (okuyucu/yazıcı eşzamanlılığı, journal_mode=delete farkı), resmî sınırlar (limits.html; whentouse.html "SQLite ne zaman uygun").
B3. Satır-bazlı YAZIM/OLTP deseni: INSERT … ON CONFLICT DO UPDATE (UPSERT, hangi sürümden), RETURNING, transaction/savepoint, tek-yazıcı sınırı; "silver'ı sıfırdan yeniden üret" (functional DE) ↔ satır-bazlı upsert — kaynaklı artı-eksi; SQLite'ın "35% faster than filesystem" küçük-blob ölçümü ve dosya-satır ↔ DB-satır seçimi için kaynaklı ölçüt.
B4. HAZIR ÜRÜNLER (motor tarafı; her biri için: ne yapar · kurulum · satır-bazlı işlem yüzeyi · bakım durumu · sürüm): sqlite-utils (CLI+Python: insert/upsert/rows/--where/create-index/enable-fts) · Datasette (JSON API /db/table/pk.json, satır uç noktası) · DuckDB sqlite_scanner (aynı dosya üstünde OLAP; OLTP'ye uygun mu?) · yerel Postgres (Postgres.app/Homebrew) ve pglite (WASM/gömülü) — tek-kullanıcı 50 MB veride gerekçe var mı · Postgres indeks danışmanları (hypopg, Dexter, pganalyze index advisor) ↔ SQLite .expert · litestream (yedek). Sayı+kaynak; "yoksa yok".`,
    antitezHint: 'SQLite zaten otomatik seek yapıyor, 50 MB\'da tasarım gereksiz · ANALYZE küçük tabloda planı bozabilir · .expert güvenilmez/sınırlı · yerel Postgres/DuckDB gereksiz · upsert yerine sıfırdan yeniden üretim daha güvenli · sqlite-utils/Datasette tek geliştirici projeleri, bakım riski.' },
  { key: 'C', title: 'AJAN-ERİŞİM DESENİ ("işaretçi bul → adrese atla") + HAZIR ÜRÜNLER (LLM tarafı)',
    questions: `C1. Anthropic/Claude Code kanonu: context engineering "just-in-time retrieval" (hafif tanımlayıcı/işaretçi tut, gerektiğinde yükle), memory tool (yol-adresli dosya erişimi), Claude Code Read (offset/limit = satır-aralığı getirme) + Grep -n (satır no = adres) + Glob; agentic search ↔ RAG önyükleme; resmî cümle + varsa sayı; "işaretçi → tam getirme" için ÖLÇÜLMÜŞ token/doğruluk kazancı var mı (yoksa AÇIKÇA yok).
C2. Kod-indeksleri = index seek emsali: ctags/readtags (sıralı tags dosyası + ikili arama), LSP go-to-definition, Sourcegraph SCIP/LSIF önceden hesaplanmış indeks, tree-sitter; Cursor/Copilot kod-indeksleme (belgelenmişse); ajanın "sembol → dosya:satır" atlaması — mekanizma + kaynak.
C3. DB erişimi için MCP/CLI ürünleri (her biri: yüzey — salt-okur mu / satır yazımı var mı · güvenlik (SQL enjeksiyonu, yıkıcı komut freni, salt-okur bayrağı) · bakım/arşiv durumu · sürüm): referans sqlite ve postgres MCP sunucuları (modelcontextprotocol/servers — arşivlendi mi?), Postgres MCP Pro (crystaldba: EXPLAIN + indeks ayarı), mcp-alchemy, mcp-server-motherduck (DuckDB), sqlite-utils/Datasette'in ajan kullanımı, Claude Code Bash+sqlite3 CLI (mevcut yol) — hangisi "hazırı temel al"a uyar.
C4. LLM'in noktasal sorgu üretme güvenilirliği + ajan-hafızası emsalleri: text-to-SQL ölçümleri (Spider/BIRD execution accuracy; basit WHERE eşitliği ↔ karmaşık; sayı+kaynak) — LLM'in yazdığı WHERE'in yanlış satır getirme riski; ajan-hafızası sistemlerinde anahtarlı/SQL erişim (Letta archival memory Postgres+SQL, Mem0 SQLite history tablosu, Zep) — exact-key ↔ vektör; "sqlite as agent memory" desenleri (yayımlanmış).`,
    antitezHint: 'MCP DB sunucuları olgunlaşmamış/arşivli · text-to-SQL hata oranı noktasal sorguda bile yüksek · JIT getirme kazancı ölçülmemiş · 8 MB korpusta grep 0,25 s — indeks kazanç getirmez · kod-indeksi emsali metin-kanona taşınmaz.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['mekanizma-terim','motor-ayarı','hazır-ürün','erişim-deseni','ölçüm-yöntemi','girmez']
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
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS, description: 'yerleşim sınıfı' }, jarvis: { type: 'string', enum: JARVIS, description: 'Jarvis eşlemesi (sondajdaki mevcut duruma göre)' }, confidence: { type: 'string', enum: ['D','K'] } } } },
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
  // ÇÜRÜTÜLEMEDİ satırları örnekleme GİRMEZ (¬T'yi destekleyen kaynak yok = antitezin kendi beyanı — 08-17 kural düzeltmesi)
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
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + motor-sürüm damgası; 'hazır-ürün' yalnız bakım/güvenlik durumu bilinen ürünlerde) + kör noktalar (aranıp bulunamayan; özellikle küçük-ölçek 10⁴-10⁵ satır ölçümü ve 'işaretçi→atlama' token kazancı ölçümü yoksa AÇIKÇA) + survival sayımı.
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

log('gorev-2026-08-18-1 sahada: 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: 'cc/gorev-2026-08-18-1.md', families: out }