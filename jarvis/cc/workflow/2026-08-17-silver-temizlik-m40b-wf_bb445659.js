export const meta = {
  name: 'silver-temizlik-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — silver katman çelişki/bayatlık temizlik-test mekanizması araştırması (gorev-2026-08-17-1)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-17-1.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi. Bağlam verisi üç katman: BRONZ = git-izlenen markdown/jsonl (ham, append-only, silme yasak) · SİLVER = veri/baglam.sqlite (bronz'dan 1:1 türetilmiş, tipli, agrege-olmayan tablolar: kayit=markdown blok 41.961 satır, referans, anahtar, karar_borcu…) · GOLD = görünümler. Silver, LLM'in (Carvis) asıl faydalanacağı hafızadır. Sahibin emri: "bronz'da artık kullanılmayan bağlam kalabilir ama silver'da bağlam ÇELİŞKİLERİ ve ARTIK FAYDALANILMAYACAK bağlam temizlenmeli; bunun için bir TEST MEKANİZMASI kuralım". Senin ailen bu mekanizmanın bir boyutuna DIŞ KANIT getirir; tasarımı sen yapmazsın.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili kabul et; yeniden araştırma, ÜSTÜNE KOY):
- Silver bugün: 41.961 blok, %89,7'si soğuk (arşiv/rapor); zarf-tabanlı çelişki görünümü 0 satır (zarflı kayıt 13); anahtar tablosunda emeklilik kolonları boş (10 emekli değer silver'a JOIN edilmemiş); mevcut testler: unique/not_null/relationships/accepted_values + kırık-pointer + sözleşme + freshness — çelişki/bayatlık testi YOK.
- Silver yüklemi (kanon): 1:1 kaynak eşleme, tipli, tekil, agrege-olmayan, türetilmiş (elle düzenlenmez; kod-SHA + girdi-SHA), veri-testleri PASS. Bronz silinmez (m.8).
- Anahtar-kaydı v1: SCD-2 + çift-zaman (gecerli_bas/bitis; tek-güncel ⟺ bitiş boş; deterministik max(tarih)); survivorship kaynak-önceliği; emeklilik = damga+gerekçe+replaced_by tekil+tarih, silme değil; cascade = açık yeniden-yazım, RESTRICT; sıcak bağlama TEK sürüm çıkar (yan yana çelişki: hiyerarşi uyumu %98→%20; doğruluk %85-87→%10-44).
- LLM çelişki-denetçisi FP %22-56 / FN ≤%64 ⇒ ikinci göz, kapı değil; anlam kayması gömme/istatistikle DEĞİL deterministik sayımla; eşik = kalibrasyon (≥10 insan-etiketli koşum) + karar-maliyeti; iki-aşamalı merdiven UYARI/EYLEM; STALE metriği (eski kayıt top-1 %88,2; yazma-anı güncelleme-yargısı %3,3); dbt hard_deletes politikası ilk yazımdan önce; Kafka tombstone penceresi.
- İngest triyajı NOOP/UPDATE/GEÇERSİZ-KIL/ADD (Mem0 deseni) verili; Zep/Graphiti bitemporal kenar geçersizleştirme verili.
- Veri-mühendisliği: dbt staging kuralı, medallion sözleşmeleri, şekil/içerik sözleşme ayrımı, freshness sözleşmesi, COST tabanı (grep+SQLite'ı geçmeyen katman eklenmez) verili. Bağlamı daraltmak doğruluğu yükseltebilir (79k→9,6k token: %73,2→%83,6) verili.
- Deterministik tasarım kuralı: test = kural + kod; LLM en fazla aday-üretici; rastgelelik tasarım aracı değil. stdlib-only Python 3.9 + SQLite; tek kullanıcı; ~42k satır.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / standart metni / arXiv-ACL / GitHub). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur (rakam · yüzde · tarih · sayım) — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili.
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma.
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, test seti TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'ÇELİŞKİ SAPTAMA TESTLERİ (silver\'da, deterministik-önce)',
    questions: `A1. Sürüm/zaman-tutarlılık testleri SCD-2/bitemporal tablolarda: dbt_utils (mutually_exclusive_ranges · unique_combination_of_columns · sequential_values · expression_is_true), dbt snapshots dbt_valid_from/to + dbt_is_deleted, Great Expectations / Soda (SodaCL) karşılıkları — "anahtar başına TAM BİR güncel satır", "geçerlilik aralıkları örtüşmez", "boşluk yok", "geçersiz-kılan kayıt daha yeni" yüklemleri; resmî tanım + ölçülmüş yakalama/yanlış-alarm varsa; SQLite'ta yazılabilirlik.
A2. Anahtar-düzeyi KISIT testleri (bilgi tabanı tutarlılığı): Wikidata property constraints (single-value · conflicts-with · one-of · contemporary · inverse) ve ihlal raporlarının ÖLÇÜLMÜŞ hacmi/çözülme oranı; SHACL/ShEx shape validation; OWL tutarsızlık akıl yürütme — "conflicts-with" sınıfının deterministik çelişki-testi olarak kullanımı; küçük ölçekte (10²-10⁵ üçlü) bedel.
A3. Doğal-dil çelişki saptama KB/hafıza üstünde — YALNIZ YENİ/derinleşen kanıt (verili: LLM denetçi FP %22-56): belge-içi/belgeler-arası çelişki tespiti (ContraDoc, WikiContradict devamı, 2025-26 "self-contradiction in LLM memory"), LLM-hafıza sistemlerinin güncelleme/çatışma mantığının ÖLÇÜLMÜŞ doğruluğu (LongMemEval knowledge-update alt-kümesi, LoCoMo, MemBench, A-MEM, MemoryOS, Letta) — özellikle "deterministik ön-eleme (aynı anahtar/aynı konu/zaman penceresi) → LLM yalnız daraltılmış çiftlere" hunisinin ölçülmüş precision/maliyet kazancı.
A4. Karantina/expectations deseni: Databricks DLT/Lakeflow expectations (expect / expect_or_drop / expect_or_fail, karantina tablosu) · dbt store_failures · GE unexpected rows — silver'ın "temiz" olması bronz'a dokunmadan nasıl sağlanır: satır DÜŞÜRME (filtre) ↔ BAYRAK (is_valid/is_current) ↔ karantina tablosu — resmî tanımlar, hangisi varsayılan, geri-eşleme (lineage) korunumu, ölçülmüş bedel; "silver = validated non-aggregated representation" ile uyumu.`,
    antitezHint: 'SCD-2/kısıt testleri yalnız YAPISAL çelişkiyi yakalar, Jarvis çelişkileri anlamsaldır (yanlış güven) · Wikidata kısıt ihlalleri yığılıp çözülmüyor (ölçülmüş birikim) · NLI/LLM çelişki tespiti hâlâ düşük precision · karantina deseni satır-düzeyi kalite içindir, anlatı belgesine uymaz · bayrak kolonu 1:1 yüklemini bozar/karmaşıklaştırır.' },
  { key: 'B', title: 'BAYATLIK / ARTIK-FAYDASIZ BAĞLAM (deterministik yüklem + unutmanın ölçülmüş fayda/zararı)',
    questions: `B1. Retention/tiering/weeding kuralları: Delta VACUUM/retention · Iceberg expire_snapshots · doküman/wiki bakımı: Wikipedia orphan/dead-end/"update needed" bakım kategorileri ve ölçülmüş hacimleri, Confluence/Notion "stale content" politikaları, "last reviewed" tazelik SLA'ları (Google/Stripe/GitLab handbook doc-freshness kuralları — kaynaklı) · kütüphane weeding: CREW/MUSTIE (Misleading · Ugly · Superseded · Trivial · Irrelevant · Elsewhere) kriter setleri — "faydasız" için yerleşik, kısmen deterministik yüklem setleri; sayısal eşikleri (kaç yıl dolaşımsız vb.) kaynaklı.
B2. LLM-hafıza sistemlerinde unutma/eviction: MemGPT/Letta core↔archival tiering, Generative Agents recency×importance×relevance (λ 0,99 verili), MemoryBank Ebbinghaus eğrisi, ACT-R base-level activation (CoALA/agents), reflection/consolidation — unutmanın/budamanın görev doğruluğuna ÖLÇÜLMÜŞ etkisi (ablasyon: budama var/yok; recall kaybı ↔ distractor kazancı); "az ama güncel hafıza" bulguları.
B3. Kullanım-tabanlı "faydasız" yüklemleri: 0-referans/yetim kayıt, superseded_by dolu, kapalı-durum (kapandı/emekli), son-atıf yaşı; cache eviction analogları (LRU/LFU/ARC/W-TinyLFU frequency-recency: hangi kombinasyon "bilgi" için) · wiki/DMS bakım metrikleri (orphan/dead-end/inbound-link=0) · "rarely used ≠ useless" karşı-kanıtı; kaynaklı sayı, uydurma yok.
B4. Bayat/ilgisiz bağlamın PROMPT'ta bedeli: irrelevant-context çalışmaları (Shi ve ark. 2023 "distracted by irrelevant context", "Lost in the middle" devamı, 2024-26 uzun-bağlam distractor ölçümleri) · bağlam budama (Provence, RECOMP, LLMLingua) ölçülmüş doğruluk/maliyet — "silver'dan sıcak bağlama yalnız güncel+ilgili çıkar" gerekçesinin ölçülmüş tabanı (79k→9,6k bulgusu VERİLİ; YENİ kanıt).`,
    antitezHint: 'unutma zarar verir (recall kaybı; "kapsama > temizlik") · kullanım-tabanlı eviction bilgi için yanlış (nadir ≠ faydasız) · MUSTIE öznel · doc-freshness kadansları folklor, ölçümsüz · irrelevant-context zararı oyuncak görevlerde ölçüldü, gerçek ajan işine transfer etmez.' },
  { key: 'C', title: 'TEST MEKANİZMASININ KENDİSİ (nasıl kurulur, nasıl ölçülür, ne zaman koşar)',
    questions: `C1. Veri-testi çerçevelerinin test taksonomisi + şiddet + koşum modeli: dbt tests (generic/singular, severity warn/error, error_if/warn_if eşikleri, store_failures) · Great Expectations (suite/checkpoint/data docs) · Soda (SodaCL) · pandera · Deequ (constraint suggestion, metrik anomali tespiti) — SQLite/stdlib'te yazılabilir asgari küme; "kalite kapısı" sıralaması (şema → bütünlük → içerik → tutarlılık); tek-kişilik ölçekte bedel.
C2. Testin-testi: veri-kalite kontrollerinin mutasyon/hata-enjeksiyonu ile ölçülmesi ("data quality mutation testing", "synthetic anomaly injection", canary/tohum satır: bronz'a bilinen çelişki ek → silver testi yakalıyor mu), altın-küme/regresyon veri setleri, precision/recall'ın insan-etiketle hesaplanması — ölçülmüş yakalama oranları, boyutlar (n), kaynaklı.
C3. LLM-hafıza kalite eval'i (silver temizliğinin ajana faydası nasıl ölçülür): LongMemEval (knowledge-update · temporal-reasoning kategorileri, n), LoCoMo, MemBench, "as-of"/point-in-time soru setleri, Zep STALE benzeri metrikler — küçük yerel eval tasarımı (kaç soru, nasıl üretilir, güvenilirlik) için ölçülmüş emsal; "temiz-silver ile / ham-bronz ile" A/B'nin literatürdeki karşılığı.
C4. Gating + kadans: pre-commit/CI'da veri testleri (dbt build fail semantiği, çıkış kodları), uyarı yorgunluğu (warn/error eşikleri, alarm-fatigue ölçümleri), tek-kullanıcı için koşum kadansı (her hat koşumu ↔ günlük ↔ damıtma turunda) — kaynaklı öneri; "test sonucu → insan triyaj kuyruğu" akış emsalleri.`,
    antitezHint: '40k satırda test bedeli faydayı aşar · veri-kalite mutasyon testi olgunlaşmadı · hafıza benchmark\'ları tek-kullanıcı markdown\'a transfer etmez · CI gating uyarı yorgunluğu doğurur · altın-küme kendisi bayatlar.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['test-tanımı','silver-yüklemi','temizlik-kuralı','bayatlık-yüklemi','ölçüm-metriği','sayısal-eşik','süreç-kuralı','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'örneklem/kapsam/sürüm/model kuşağı; yoksa "-"' },
    placement_suggestion: { type: 'string', description: 'bu bulgu Jarvis test-mekanizmasına nasıl oturur: ' + PLACEMENTS.join(' / ') },
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
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','confidence'],
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS }, confidence: { type: 'string', enum: ['D','K'] } } } },
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
  const antiItems = (r.anti && r.anti.rebuttals) ? r.anti.rebuttals : []
  const antiPicks = v26Picks(antiItems, x => `¬${x.target_id}`, x => x.negation, x => x.evidence_url, x => x.figure)
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
Sonda: bu aileden JARVIS TEST-MEKANİZMASINA girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')}) + kör noktalar (aranıp bulunamayan; özellikle küçük-ölçek ölçümü yoksa AÇIKÇA) + survival sayımı.
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

log('gorev-2026-08-17-1 sahada: 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: 'cc/gorev-2026-08-17-1.md', families: out }
