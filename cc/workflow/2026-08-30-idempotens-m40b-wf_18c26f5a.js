export const meta = {
  name: 'ib39-idempotens-m40b',
  description: 'İB-39 idempotens atlası (emir cc/gorev-2026-08-29-ib39-idempotens-atlas.md): 3 dik aile (A formal/protokol · B araç emsalleri · C iç envanter) × (tez → antitez/ayak-izi doğrulama → V26 kural-tabanlı örneklem → maskeli hakem); işçi Sonnet, hakem Opus, sentez Carvis; ≤12 ajan; fren şablonu İB-54',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız tez (Sonnet, medium; C web\'siz — kaynak kod okur)', model: 'sonnet' },
    { title: 'Antitez', detail: 'A/B: CoVe-Factored ¬T (Sonnet, medium) · C: kaynak-koddan bağımsız ayak-izi doğrulama', model: 'sonnet' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + tüm sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + Jarvis yapı-taşları (Opus, high)', model: 'opus' },
  ],
}

// ---- FREN ŞABLONU (cc/workflow/fren-sablonu.js; İB-54 adım 2, Karar 74 M-4 d paket B; Karar 39 uç-eşikli) ----
const FREN = { AJAN_TAVAN: 36, DALGA_TAVAN: 12, REJIM: 'manuel-tempo · kota-bol · ekonomi -%30 (08-15) · AS-OF 2026-08-30' }
let ajanSayaci = 0
const ajan = (prompt, opts) => {
  ajanSayaci += 1
  if (ajanSayaci > FREN.AJAN_TAVAN) {
    log(`FREN (İB-54): ${ajanSayaci}. ajan — tavan ${FREN.AJAN_TAVAN} (rejim: ${FREN.REJIM}); koşum durduruluyor, kısmi sonuç döndür`)
    throw new Error(`İB-54 ajan tavanı ${FREN.AJAN_TAVAN} aşıldı (${ajanSayaci})`)
  }
  return agent(prompt, opts)
}
// ---- /FREN ----

const TARIH = (args && args.date) || '2026-08-30'
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, TÜRKÇE markdown-kanon + SQLite (silver) + CSV/parquet (gold) tabanlı kişisel LLM-operasyon sistemi (Claude Code, Mac; stdlib Python script'leri tools/*.py, ~43 adet). Asistan (Carvis) bir LLM'dir; eğitim kesimi Ocak 2026, BUGÜN ${TARIH}. Sahibin hedefi (Salih, 08-20 KB-18): "deterministik VE idempotent sistem". KAVRAM AYRIMI (emre gömülü): DETERMİNİZM = aynı girdi → aynı çıktı (Karar 65); İDEMPOTENS = tekrar-uygulama sonucu değiştirmez, f(f(x)) = f(x). Kardeş hedefler, aynı şey DEĞİL.
PROBLEM: yeniden koşum (retry · çift oturum · bağlam-dolu kesinti sonrası devam · aynı script'in iki kez çağrılması) güvenliği yazılı standart değil. Bugünkü desenler: silver DB'yi sıfırdan yeniden yazma (rebuild-from-bronze), append-only JSONL kütükler (bazıları tekil anahtarlı, bazıları çoğalan), tmp→rename atomik yazım (kilitsiz), sha-tabanlı üretim damgası (uretim.git_head_sha), Workflow resume önbelleği. Senin ailen "NASIL STANDARTLAŞIR" sorusunun bir boyutuna KANIT getirir; karar vermezsin, kod yazmazsın, kanon tasarlamazsın.
ANAKRONİZM YASAK (Karar 68): her iddiada AS-OF (kaynağın tarihi ∨ çekim tarihin ${TARIH}); damgasız iddia hakem tarafından düşürülür. Model-hafızasından sürüm/durum anlatma; canlı çek.`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil: RFC/IETF taslağı · resmî doküman · kaynak kodu/README · yayımlanmış makale). Rakamlar kaynaklı; kestirimse "[?]". Sürüm + tarih zorunlu (çıplak "destekler" yasak).
- Her iddiada AS-OF: kaynağın yayın/sürüm tarihi ∨ çekim tarihi ${TARIH} scope alanında yazılı.
- UYDURMA YASAK; "bulunamadı" meşru; "[ARANAMADI]" = bütçe/erişim; 403/paywall bayraklanır.
- Etiket: D birincil · K ikincil/teyide muhtaç · X doğrulanamadı. Determinism alanı: mekanizma deterministik mi (e/h/—) + neden.
- Bütçe ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git.
- Repoya/diske HİÇBİR DOSYA YAZMA. Paket KURMA. Alt-ajan AÇMA. Karar ALMA — kanıt getir.`

const FAMILIES = [
  { key: 'A', web: true, title: 'FORMAL / PROTOKOL: idempotency-key semantiği · exactly-once ↔ at-least-once + dedup · idempotent consumer · veri-hattı idempotensi (dbt/Airflow/rebuild-from-bronze)',
    questions: `A1. HTTP Idempotency-Key IETF taslağı (draft-ietf-httpapi-idempotency-key-header): güncel sürüm numarası + tarihi (canlı çek; 07-26'da ARANAMADI), anahtar kapsamı (kaç saat/ne granül), fingerprint (aynı anahtar + farklı gövde → hangi hata), yeniden-oynatma cevabı; RFC 9110 §9.2.2 idempotent metot tanımı.
A2. Exactly-once vs at-least-once + tekilleştirme: yayımlanmış tanımlar (Kafka EOS dokümanı, Kleppmann DDIA bölüm/örnek, "exactly-once is a lie" tartışması) — hangi katmanda hangi garanti; idempotent consumer / inbox-outbox deseni (microservices.io); dedup penceresi ve anahtar seçimi.
A3. Veri hattı idempotensi: dbt incremental + unique_key + merge stratejisi (resmî doküman, sürüm), Airflow "idempotent task" ilkesi (resmî best-practices sayfası), "rebuild from raw/bronze" ilkesi (medallion mimarisi dokümanı) — hangi desen tekrar-koşumda çoğalma üretmez; append-only kütükte tekil-anahtar/"koşum kimliği" pratiği.
A4. Atomik dosya yazımı ile idempotens ilişkisi: write-temp-then-rename garantisi (POSIX rename atomikliği; fsync tuzakları), git lockfile deseni, "yeniden koşum sonrası kısmi dosya" senaryosu; append-only JSONL'de çift-satır önleme (koşum kimliği · içerik-sha · UNIQUE) emsalleri.`,
    antitezHint: 'Idempotency-Key taslağı hâlâ taslak/uyum yok · exactly-once pratikte at-least-once+dedup, dedup penceresi bitince çoğalır · dbt merge yalnız warehouse\'ta, dosya kütüğünde yok · rename atomik ama fsync\'siz veri kaybı · rebuild-from-bronze idempotent ama pahalı/deterministik değil (zaman damgaları).' },
  { key: 'B', web: true, title: 'ARAÇ EMSALLERİ: Temporal · Stripe · Kafka EOS · Make/Bazel/Nix içerik-adresli yeniden-üretim · Claude Code Workflow resume önbelleği',
    questions: `B1. Temporal: activity idempotency (idempotency token, "activities may run more than once"), workflow determinism constraint (replay; non-deterministic error sınıfı), resmî doküman sürümü/tarihi — determinizm ↔ idempotens ayrımını nasıl koyuyor.
B2. Stripe idempotency keys: anahtar ömrü (saat), aynı anahtar + farklı parametre davranışı, hangi metotlara uygulanır, sunucu tarafı kayıt; resmî API dokümanı (tarih).
B3. Kafka exactly-once semantics (idempotent producer PID+sequence, transactional API, read_committed) — hangi sınır içinde "exactly once"; resmî doküman/KIP-98 tarihi.
B4. İçerik-adresli yeniden-üretim: Make (mtime) vs Bazel (içerik hash + action cache) vs Nix (derivation hash, reproducible builds) — "aynı girdi → aynı çıktı → atla" mekanizmasının kanıtı, determinizm şartı (sandbox/hermetiklik); Claude Code Workflow resume (resumeFromRunId: aynı (prompt, opts) → önbellek) benzeri "kayıt-tabanlı atlama" emsali — resmî doküman + sürüm.`,
    antitezHint: 'Temporal determinizm kısıtı kod-düzeyi disiplin, araç zorlamaz · Stripe anahtarı 24 saat sonra düşer · Kafka EOS yalnız Kafka-içi topolojide · Bazel/Nix hermetiklik kurulum maliyeti kişisel ölçekte aşırı · resume önbelleği prompt değişince tümü düşer.' },
  { key: 'C', web: false, title: 'İÇ ENVANTER (web YOK — kaynak kodu okur): tools/*.py script\'lerinin yeniden-koşum sınıflandırması: idempotent-by-rebuild · append+tekil-anahtar · append-çoğalan · atomik-olmayan yazım',
    questions: `C1. raporlar/2026-08-29-ib39-ic-envanter.md tablosundaki HER script (33 satır) için tek sınıf seç: idempotent-by-rebuild (DROP/sıfırdan yazım) · append+tekil-anahtar (UNIQUE/INSERT OR IGNORE/kayit_id kontrolü) · append-çoğalan (tekrar koşumda satır çoğalır — bilinçli koşum kütüğü mü, hata mı?) · atomik-olmayan yazım (open(...,'w') doğrudan, tmp→rename yok). KANIT = dosya:satır pointer'ı (grep/Read ile; tablo sayıları işaret, kanıt değil). Envanter raporundaki 4 "Okuma" sorusuna cevap.
C2. Çift koşum senaryosu: katman-hatti.py iki oturumda eşzamanlı koşarsa hangi dosyalar son-yazan-kazanır; hangi script'te kilit/kira var (yok ise "yok" de, pointer ile).
C3. Koşum kimliği: hangi kütükler koşumu tekil anlatıyor (uretim.git_head_sha · kosum_id · hareket_id) — çift-satır önleme mekanizması var mı (kod satırı).
C4. veri/README.md sözleşmeleri (append-only, kayit_id_kume_sha) ile kodun uyuşmadığı yerler (varsa, pointer).`,
    antitezHint: 'Tablo sayıları yanıltıcı (desen eşleşmesi ≠ davranış) · "rebuild" idempotent görünür ama zaman damgası/sıra değişir (determinizm kırılır) · tekil anahtar var ama kontrol edilmiyor · kuru koşum bayrağı var ama yazım yolunu kapsamıyor.' },
]

const PLACEMENTS = ['AXI-A4-standart-satiri','kutuk-semasi','yazim-deseni','kosum-kimligi','kilit-kira','test-kapisi','hazir-arac','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','determinism','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ∨ repo dosya:satır (C ailesi) ∨ "bulunamadı" ∨ "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sürüm/tarih (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'AS-OF ZORUNLU: kaynak yayın/sürüm tarihi ∨ çekim tarihi + kapsam' },
    determinism: { type: 'string', description: '"e"/"h"/"—" + tek-cümle neden' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ')' },
  } }
const TEZ_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','claims','gaps','access_blocks','budget_note'],
  properties: { family: { type: 'string' }, claims: { type: 'array', minItems: 4, maxItems: 14, items: CLAIM }, gaps: { type: 'array', items: { type: 'string' } }, access_blocks: { type: 'array', items: { type: 'string' } }, budget_note: { type: 'string' } } }
const REBUT = { type: 'object', additionalProperties: false, required: ['target_id','negation','verdict','evidence_url','figure','note'],
  properties: { target_id: { type: 'string' }, negation: { type: 'string' }, verdict: { type: 'string', enum: ['ÇÜRÜTÜLDÜ','DARALTILDI','ÇÜRÜTÜLEMEDİ'] }, evidence_url: { type: 'string' }, figure: { type: 'string' }, note: { type: 'string', description: 'DARALTILDI ise daraltılmış hâl; ÇÜRÜTÜLEMEDİ ise ne arandı; AS-OF' } } }
const ANTI_SCHEMA = { type: 'object', additionalProperties: false, required: ['family','rebuttals','extra_counter_claims','budget_note'],
  properties: { family: { type: 'string' }, rebuttals: { type: 'array', maxItems: 14, items: REBUT }, extra_counter_claims: { type: 'array', maxItems: 3, items: CLAIM }, budget_note: { type: 'string' } } }
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

const isUrl = s => /^https?:\/\//.test(s || '') || /^[\w./-]+\.py:\d+/.test(s || '')
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

const C_GIRDI = `C AİLESİ GİRDİLERİ (repo, yalnız OKU): raporlar/2026-08-29-ib39-ic-envanter.md (tablo + 4 Okuma sorusu) · veri/README.md (append-only, kayit_id_kume_sha sözleşmeleri) · tools/katman-hatti.py docstring · tools/AXI-STANDARDI.md (A4 satırı) · cc/rapor-2026-07-26-SOZEL-ajan-durma.md:173 (Temporal ön-izi) · tools/*.py (Grep/Read ile kanıt satırı). Kanıt biçimi source_url alanında: "tools/<script>.py:<satır>".`

const tezStage = (fam) => ajan(
`ROL: Atlas TEZ araştırmacısı — aile ${fam.key}: ${fam.title}. Bağımsız çalışıyorsun; başka ailenin sorusuna cevap verme.
${BAGLAM}
${fam.web ? '' : C_GIRDI}

ARAŞTIRMA SORULARI (yalnız bunlar):
${fam.questions}

${DISIPLIN}
Çıktı: 4-14 iddia (her soruya ≥1; C ailesinde her script için 1 sınıflandırma iddiası — 33 script → gruplayarak ≤14 iddiaya sığdır: aynı sınıftaki script'leri tek iddiada listele, her biri için dosya:satır kanıtı), kaynaklı ve AS-OF damgalı; gaps/access_blocks/budget_note doldur.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: fam.web ? 'atlas' : 'general-purpose', model: 'sonnet', effort: 'medium', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')
  const rol = fam.web
    ? `ROL: Atlas ANTİTEZ ajanı (açık Devil's-Advocate, CoVe-Factored) — aile ${fam.key}: ${fam.title}.
Sana bir başka araştırmacının İDDİA satırları veriliyor; GEREKÇELERİ ve KAYNAKLARI kasıtlı olarak verilmiyor (çıpalama freni). Görevin: her iddianın DEĞİLİNİ (¬T) savunacak BİRİNCİL kanıt aramak. Çürütemediysen "ÇÜRÜTÜLEMEDİ" + ne aradığın; kısmen çürüttüysen DARALTILDI + daraltılmış hâl. İddia bir mekanizmayı "idempotent/deterministik" sayıyorsa sınırını (pencere, kapsam, hermetiklik şartı) ara. Kendi kanıtlarını AS-OF damgala.`
    : `ROL: KAYNAK-KODDAN BAĞIMSIZ AYAK-İZİ DOĞRULAYICI — aile C (iç envanter). Sana bir başka ajanın script SINIFLANDIRMA iddiaları veriliyor; onun kanıt satırları verilmiyor. Görevin: her iddiayı tools/*.py kaynağını KENDİN okuyarak (Grep/Read) doğrulamak ya da çürütmek — yazım yolunu izle: open(...,'w') mı, tmp→os.replace mi, INSERT OR IGNORE mı, UNIQUE var mı, kontrol ediliyor mu. Kanıt = dosya:satır. Sınıf yanlışsa ÇÜRÜTÜLDÜ + doğru sınıf; eksik nüans varsa DARALTILDI. ${C_GIRDI}`
  return ajan(
`${rol}
Tezde OLMAYAN karşı-yönlü bulgular varsa extra_counter_claims'e ekle (≤3). Yön ipuçları (bağlayıcı değil): ${fam.antitezHint}
${BAGLAM}

İDDİALAR:
${claimsOnly}

${DISIPLIN}`,
    { label: `antitez:${fam.key}`, phase: 'Antitez', agentType: fam.web ? 'atlas' : 'general-purpose', model: 'sonnet', effort: 'medium', schema: ANTI_SCHEMA }
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
  return ajan(
`ROL: V26 örneklem-denetçisi (aile ${fam.key}). Aşağıdaki iddia→kaynak çiftleri KURAL-TABANLI seçildi. Her biri için KAYNAĞA İN (${fam.web ? 'WebFetch' : 'Read — repo dosyası:satır'}): iddia ve rakam kaynak metinde GERÇEKTEN var mı? Sonuç: TUTUYOR / TUTMUYOR / ERİŞİLEMEDİ. Not: tek cümle — kaynakta ne gördün (rakamı aynen; kaynağın TARİHİNİ/sürümünü de yaz). Uydurma yok; yorum yok. Repoya dosya yazma, alt-ajan açma.
${picks.map((p,i)=>`${i+1}. [${p.claim_id}] "${p.claim}" — rakam: ${p.figure} — kaynak: ${p.url}`).join('\n')}`,
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
  return ajan(
`ROL: MASKELİ HAKEM — aile ${fam.key}: ${fam.title}. Üretici koşumların devamı DEĞİLSİN; hangi tarafın tez/antitez olduğu söylenmiyor — iddia+kanıt olarak tart.
Ölçüt = adversarial-hayatta-kalma: çürütülemeyen SAĞLAM; kısmen çürüyen DARALDI (hayatta kalan hâl AS-OF damgalı); çürüyen DÜŞTÜ; uzlaşmaz ÇELİŞKİLİ. Kanıt gücü: birincil > ikincil; rakamlı > rakamsız; tarih damgalı > damgasız; C ailesinde dosya:satır pointer'ı olmayan iddia otomatik DARALDI. V26 kuralı: bir tarafın denetlenen iddiası TUTMUYOR ise o tarafın o ailedeki TÜM iddiaları K'ya düşer. AS-OF KURALI (Karar 68): damgasız iddia otomatik DARALDI ('as-of belirsiz') ya da DÜŞTÜ. Hazır-ürün/sürüm taşıyan yapı-taşında sürümü ve tarihini KENDİN yeniden çek (WebFetch ≤6; C ailesinde Read).
DETERMİNİZM ↔ İDEMPOTENS AYRIMI: her yapı-taşında hangisini sağladığını ayrı yaz; "modele hatırlatma" mekanizma değildir (Karar 65).
Sonda: JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI'dan; her biri AS-OF damgalı + kaynak + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + deterministic e/h/— + sürüm damgası) + kör noktalar (özellikle: append-çoğalan kütükler bilinçli mi · iki-oturum eşzamanlılığı · kilit/kira yokluğu · tmp→rename fsync) + survival.
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
    { label: `hakem:${fam.key}`, phase: 'Hakem', model: 'opus', effort: 'high', schema: HAKEM_SCHEMA }
  ).then(hakem => ({ ...r, hakem, mask }))
}

log(`İB-39 sahada (AS-OF ${TARIH}): 3 aile (A formal/protokol · B araç emsalleri · C iç envanter) × tez(sonnet)→antitez/ayak-izi(sonnet)→V26(sonnet)→hakem(opus); fren AJAN_TAVAN ${FREN.AJAN_TAVAN}; emir ${(args && args.emir) || 'cc/gorev-2026-08-29-ib39-idempotens-atlas.md'}`)
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'} · ajan sayısı ${ajanSayaci}/${FREN.AJAN_TAVAN}`)
return { date: TARIH, emir: (args && args.emir) || 'cc/gorev-2026-08-29-ib39-idempotens-atlas.md', families: out, fren: { ajan: ajanSayaci, tavan: FREN } }
