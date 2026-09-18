export const meta = {
  name: 'pointer-graf-d2-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — Jarvis pointer/anahtar sisteminin grafı: hangi graf dosya tipi (D2 önde), hangi şema, LLM↔graf iletişimi; determinizm-önceliği (Karar 65) (gorev-2026-08-22-2)',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları + deterministik damgası (üst model, high)' },
  ],
}

const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, TÜRKÇE markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi; Claude Code (masaüstü) üzerinde çalışır. Sahibin emri (aynen): "bizim tüm pointer sistemimizin (database primary keyler ve sistemin kuruluşundaki ilkemiz doğrultusundaki sürecimiz) graflar için olan güncel dosya tipinde grafını oluştur. böylece senle böyle konuşmamızın yanında aynı zamanda graflarla da iletişim sağlamaya başlayalım, böylece llm'lerin geleceği olan graf engineering'e pratik olur. araştırarak başla atlasları koşarak, sonra ilk d2'yi göreceğim şekilde … ilk çıktıdan sonraki uzun vade graf dilinde konuşma için de planlama yap". İlk çıktı dosya tipi D2 (.d2) olarak belirlenmiştir (sahip); alternatiflerin amaç-matrisi yine kanıtlanır. Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin, .d2 dosyasını sen yazmazsın (Carvis deterministik script ile yazar).
DETERMİNİZM ÖNCELİĞİ (sahibin Katman-1 kuralı, aynen: "determinizmle çelişkilerde determinizm kazanır"): yerleşim motoru/araç/biçim/yöntem determinizmle çelişiyorsa (rastgele tohumlu yerleşim · tescilli/bulut yerleşim (TALA) · LLM-üretimli graf İÇERİĞİ · sürümü sabitlenemeyen SaaS render) ve deterministik karşılığı varsa (ELK/dagre sabit girdi → sabit çıktı · script-türetimli düz-metin dosya · sabit düğüm/kenar sıralaması · LLM yalnız yorum/etiket katmanında) DETERMİNİZM KAZANIR. Her araç/biçim/yöntem iddiasına "deterministik: e / h / — (+ tek cümle neden)" damgası vur.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; yeniden keşfetme, ÜSTÜNE KOY):
- Jarvis pointer/anahtar envanteri (deterministik, 08-22; sqlite3 3.51.0): silver veri/baglam.sqlite — kayit (PK kayit_id = yol#satir_bas-satir_son#sha8 = dosya+satır ADRESİ; dosya_id → dosya; bolum_yolu H1›H2›H3; ingest zarfı zarf_*) · dosya (PK dosya_id; katman sıcak 35 / ılık 81 / soğuk 406 / yapısal 48 × dizin core/kuyruk/wiki/cc/raporlar/veri/.claude/ogrenme/tools; blob_sha; ilk/son commit) · referans (kayit_id → kayit; 11 tür: anahtar_terim 29.247 · dosya_pointer 8.071 [hedef_var 6.964 çözümlü / 1.107 KIRIK; hedef_yol] · tuzuk_madde 7.669 · etiket 5.408 · url 3.476 · v_no 3.099 · kart 2.025 · tarih 1.819 · skill_adi 1.456 · sha 628 · wiki_link 164) · anahtar (PK anahtar_id; 328: tuzuk_madde 137 · v_no 82 · wiki_sayfa 43 · anahtar_terim 27 · kart 23 · skill 16; durum gozlenen/aktif/deprecated; replaced_by → anahtar = SÜPERSEDE zinciri; gecerli_bas/bitis = SCD-2) · karar_borcu (PK borc_id KB-n/İB-n; bagimlilik) + karar_borcu_kaynak (borc_id × dosya_id × satir × kayit_id; 246/246 çözümlü) · hareket (araç kütüğü) · prompt · json_kayit (JSON-pointer) · uretim (git_head_sha, script_sha = türetme provenansı). Gold görünümler v_referans_sayim · v_kirik_pointer · v_olgu_referans · v_anahtar_terim_dosya. Üretim hattı: bronz (git-izlenen md/json/jsonl 570) → silver (SQLite, sıfırdan yeniden üretim, idempotent) → gold (CSV) = veri-türetme (lineage) grafı. Makine: d2 v0.8.1 kurulu (dagre + ELK bundled; TALA yok), dot/mmdc yok, Python 3.9.6.
- Pointer İLKESİ ve süreci (kanon): m.20 özet + adres (detay sıcak bağlama taşınmaz; karar anında pointer izlenir, dosya okunur) · m.21 dönüş yolu (özet kısalır, pointer düşmez) · m.22 arşiv pointer (bayat kayıt silinmez, arşive iner, pointer güncellenir) · m.8 silme yasağı → süpersede · anahtar-kaydı emeklilik protokolü (BACKWARD sıra) · ingest zarfı (tip/kaynak/tarih/hedef/şema/önem/geçerli-bitiş). Kuruluş kronolojisi: 07-11 tüzük m.20-22 → 07-12 PAT kararı kanonik örnek → 08-15 silver katmanı → 08-18 adresli-erişim kuralı.
- 07-18 pointer raporu (VERİLİ; KARAR ALINMADI): Model A typed-link graph ÖNERİ — düğüm = pointer; kenar = tipli bağ (destekler · çürütür · genişletir · supersedes · bağımlı · rafine · karşıt-temel); pointer türleri (kanon · wiki · karar · rapor · ders · pop); hub/MOC routing; katmanlı-hibrit K0 sıcak 1-satır özet / K1 tipli graf / K2 hub / K3 makine erişim; açık sorular: bağlar tipli mi · ölçek fallback · MOC elle mi.
- 07-24 graf-mühendisliği (VERİLİ): "etiketi alma, pratiği al"; "graph engineering" 2026-07 X etiketi, kurumsal tanım yok; 146 md'nin %92,5'i graf-yetim (o gün), elle index bayatlar → türetilmiş index; orkestrasyon grafı ölçülmüş ve kaybediyor; insan-kürasyonlu ↔ oto-inşa graf getiri farkı ÖLÇÜLMEMİŞ; egress 403'lerde raw.githubusercontent CSV/README yolu işledi.
- rapor-2026-08-22-1 (VERİLİ): LLM-inşa graf (GraphRAG/Mem0g) GİRMEZ (h; kazanç yalnız LLM-hakemde); insan-yazımı referans grafı deterministik; world-model: taban ilişkisel kalır, graf motoru ayrıştırılmaz; "ham blok gerçek kaynak; matris/gömme türetilmiş ve KAYIPLI görünüm" → graf dosyası da türetilmiş görünümdür.
- Kanon ilkeleri: deterministik tasarım + Karar 65 · pointer m.20 · HAZIRI TEMEL AL · açık kaynak/okunabilirlik (graf dosyası git-diff'lenebilir düz metin) · Türkçe etiketler (Unicode SORU) · plan A* vaat etmez · token −%30.
- Bilinmeyen (çekirdek): hangi dosya tipi hangi amaç için "güncel" (insan-görsel / makine-değişim / sorgulanabilir) ve D2'nin yeri · PK/FK + pointer türleri + süpersede + zaman + katman TEK grafta nasıl şemalanır (ER/PROV-O/OpenLineage/typed-link standardı var mı) · 49k-düğümlü tam grafın okunur ölçeği — şema-düzeyi ↔ örnek-düzeyi ↔ hub kademelemesi · LLM'in D2/Mermaid/DOT üretme-okuma doğruluğu (ölçüm) ve graf kodlamanın LLM akıl yürütmesine etkisi · yerleşim determinizmi (aynı .d2 → aynı SVG?) · graf-dilinde konuşma protokolü emsalleri ve ölçümü.
- Kural: ÜRÜN + SÜRÜM + TARİH damgası (D2 v0.8.x · Mermaid v11.x · Graphviz x.y · ELK x.y; makale → yıl + veri kümesi); satıcı beyanı D sayılmaz; hazır-ürün sürümlerini özetten kopyalama, releases sayfasından oku (08-22-1 dersi: ranx v0.3.5 ↔ v0.3.21).`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / kaynak kodu README-releases / standart metni / arXiv-ACL / GitHub API). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam/sürüm yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır (raw.githubusercontent yolunu dene).
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. SATICI PAZARLAMA iddiası D sayılmaz.
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma. Ürün+sürüm+tarih damgası her iddiada. Her araç/biçim/yöntem iddiasında determinism alanı dolu (e / h / — + neden).
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Paket KURMA, yerel d2 KOŞMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, .d2 YAZMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'GRAF DOSYA TİPİ + ARAÇ ("graflar için güncel dosya tipi"; D2 önde)',
    questions: `A1. D2 (terrastruct/d2): güncel sürüm + lisans + dil özellikleri (shapes: sql_table/class/… · classes · layers/scenarios/steps · imports/vars · grid · links/tooltips · markdown/LaTeX · Unicode/Türkçe) · CLI (render svg/png/pdf; watch; --layout) · yerleşim motorları dagre / ELK (bundled) / TALA (tescilli, ücretli?) — DETERMİNİZM: aynı .d2 → aynı SVG mi (tohum, sıralama; belgelenmiş mi); büyük graf sınırları (düğüm sayısı/performans/okunurluk rakamı); GitHub/Obsidian/VS Code render desteği. Sayı + sürüm + kaynak.
A2. Alternatifler AMAÇ-MATRİSİ: Mermaid (erDiagram/classDiagram/flowchart; GitHub/Obsidian native render; v11) · Graphviz DOT (büyük graf, olgun yerleşim; sürüm) · PlantUML · Excalidraw/Obsidian Canvas JSON · GraphML/GEXF (Gephi/yEd) · JSON Graph Format · Cypher/openCypher · RDF Turtle/JSON-LD — hangisi insan-görsel / makine-değişim / sorgulanabilir; git-diff dostluğu; olgunluk/bakım/lisans; deterministik render. "Tek kaynak dosya → çok çıktı" deseni (D2 layers; DOT→svg; JGF→D2 dönüştürücü var mı).
A3. "GÜNCEL" sinyalleri (ölçülebilir): GitHub native render kapsamı (Mermaid ✓, D2?), yıldız/sürüm-tarihi/commit ritmi (GitHub API), editör eklentileri, LLM eğitim-verisi yaygınlığının dolaylı sinyali; satıcı beyanı değil ölçülebilir sayı.
A4. Dosya tipi ↔ graf MODELİ: property-graph (tipli kenar + özellik) ↔ RDF üçlü ↔ ER; D2/Mermaid/DOT'ta tipli kenar/özellik/zaman ifade etme yolları; SQLite kenar tablosundan dosyaya deterministik türetme deseni (hazır araç var mı).`,
    antitezHint: 'D2 niş/tek-şirket bağımlı · Mermaid fiilen standart (GitHub render) · DOT daha olgun/büyük graf · görsel diller makine-değişim için yanlış araç (GraphML/JGF/Turtle) · yerleşim deterministik değil · "güncel" = moda.' },
  { key: 'B', title: 'POINTER/PK SİSTEMİNİN GRAF ŞEMASI (ne düğüm, ne kenar; zaman/süpersede/katman; ölçek kademelemesi)',
    questions: `B1. ER/şema standartları: crow's-foot · IDEF1X · DBML/dbdiagram · D2 sql_table (PK/FK gösterimi) · SQLite şemasından ER üreten hazır araçlar (eralchemy, schemacrawler, sqlite-erd, dbml-cli…; bakım/sürüm) — PK/FK grafı için "hazırı temel al" adayı.
B2. Typed-link / provenance standartları: PROV-O (Entity/Activity/Agent; wasDerivedFrom · wasRevisionOf · invalidatedAtTime → süpersede/SCD-2 karşılığı) · OpenLineage / dbt lineage DAG (kaynak→türev = bronz→silver→gold) · CiTO (supports/disputes/extends) · SKOS (broader/related) · schema.org · ADR supersedes graf araçları · Zettelkasten/Obsidian typed-link (Dataview/Juggl/Breadcrumbs) — Jarvis'in 7 bağ-türüne (07-18) ve referans 11 türüne eşleme; standart → D2 ifadesi.
B3. Ölçek/kademeleme: 49k düğüm okunmaz → şema-düzeyi graf (tablolar + referans türleri + katmanlar, ~20-60 düğüm) · örnek-düzeyi alt-graf (bir kayıt/karar çevresi, 1-2 sıçrama) · hub/MOC katmanı; kademelemenin dosya karşılığı (D2 layers/steps; ayrı dosyalar; link ile drill-down); deterministik sıralama (düğüm/kenar sabit sırada → git-diff) — yayımlanmış kural/ölçüm (kaç düğüm okunur: insan-faktörü literatürü varsa, sayı).
B4. Zaman + süpersede + katman + kırık pointer: bitemporal kenar (valid_from/valid_to; Graphiti/Zep emsali) · SCD-2 anahtar kaydı · sıcak/ılık/soğuk katmanın görselde sınıf/renk/küme olarak gösterimi (D2 classes/style) · kırık pointer (hedef_var=0) işaretleme · "sistemin kuruluş süreci" kronolojisi (07-11 → 08-22) graf üstünde (D2 steps/scenarios ↔ timeline).`,
    antitezHint: 'ER diyagramı yeter, typed-link şeması aşırı-mühendislik · PROV-O ağır/benimsenmemiş · hub/MOC elle bakım bayatlar (07-24) · şema-düzeyi graf gerçek pointer\'ları gizler · zaman boyutu görselde okunmaz.' },
  { key: 'C', title: 'LLM↔GRAF İLETİŞİMİ ("graf dilinde konuşma"; uzun vade)',
    questions: `C1. LLM'in graf DOSYASI ÜRETME doğruluğu: D2/Mermaid/PlantUML/DOT üretim ölçümleri (sözdizim geçerliliği, anlamsal doğruluk; hangi dil hangi modelde daha güvenilir; derle→hata→düzelt döngüsü) — kaynaklı sayı; determinizm (aynı istem → aynı graf? h) ve deterministik varyant (script-türetimi + LLM yalnız yorum/etiket).
C2. LLM'in graf OKUMA/akıl yürütmesi: "Talk like a Graph" (Fatemi ve ark. 2023: kodlama biçimi — kenar listesi / adjacency / doğal dil — ve görev etkisi, sayılar) · GraphQA / NLGraph · GraphToken · Graph-of-Thoughts · KG-prompting — LLM'e graf HANGİ BİÇİMDE verilmeli (D2 kaynağı mı, kenar listesi mi, JSON mu, görsel mi); bağlam maliyeti.
C3. İletişim protokolü emsalleri: diagram-as-code round-trip (insan düzenler → LLM okur → LLM yazar → render) · Excalidraw/Mermaid/D2'nin Claude/Cursor/Copilot entegrasyonları · Obsidian Canvas · "graph engineering" pratiği (07-24 VERİLİ) · Anthropic/Claude Code'un diyagram üretme kanonu; senkron (graf ← kanon türetme, bayatlama — 07-24 dersi); determinizm: dosya-tipi + script üretimi e, LLM içerik h.
C4. Ölçüm + yol haritası: graf-iletişiminin faydası nasıl ölçülür (anlama testi, hata oranı, token, süre; küçük eval tarifi) · emsal yol haritaları (şema-düzeyi → örnek-düzeyi → sorgulanabilir → konuşma protokolü) · "graf dilinde konuşma"nın deterministik çekirdeği (hangi kısım script, hangi kısım LLM).`,
    antitezHint: 'LLM\'ler diyagram kodunda sık hata yapar · graf okuma için kenar listesi/doğal dil yeterli, görsel LLM\'e gereksiz · "graf dili" insana yarar makineye değil (ya da tersi) · round-trip senkron bakım borcu · ölçüm literatürü zayıf.' },
]

const PLACEMENTS = ['dosya-tipi','şema-kuralı','d2-idiomu','iletişim-protokolü','araç','ölçüm-yöntemi','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','determinism','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih/sürüm (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'ürün+sürüm+tarih ∨ veri-kümesi+metrik + örneklem/kapsam; yoksa "-"' },
    determinism: { type: 'string', description: 'araç/biçim/yöntem iddiasıysa "e" / "h" / "—" + tek-cümle neden; iddia araç/yöntem değilse "-"' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') + damga' },
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
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','jarvis','deterministic','confidence'], properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS }, jarvis: { type: 'string', enum: JARVIS }, deterministic: { type: 'string', enum: ['e','h','—'] }, confidence: { type: 'string', enum: ['D','K'] } } } },
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
Çıktı: 4-10 iddia (her soruya ≥1), her biri kaynaklı; gaps/access_blocks/budget_note doldur. Sayısal iddialarda figure ZORUNLU; her iddiada ürün-sürüm damgası; araç/biçim/yöntem iddialarında determinism alanı dolu.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')
  return agent(
`ROL: Atlas ANTİTEZ ajanı (açık Devil's-Advocate) — aile ${fam.key}: ${fam.title}.
Sana bir başka araştırmacının İDDİA satırları veriliyor; GEREKÇELERİ ve KAYNAKLARI kasıtlı olarak verilmiyor (çıpalama freni). Görevin: her iddianın DEĞİLİNİ (¬T) savunacak BİRİNCİL kanıt aramak — "alternatif bakış" değil, lojiksel ters. Çürütemediysen "ÇÜRÜTÜLEMEDİ" yaz ve ne aradığını belirt; süs-antitez ÜRETME. Kısmen çürüttüysen DARALTILDI + daraltılmış hâlini yaz. Determinizm-önceliği gereği: iddia bir aracı/biçimi "deterministik" sayıyorsa aksini (rastgele yerleşim, sürüm kayması) da ara.
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
`ROL: V26 örneklem-denetçisi (aile ${fam.key}). Aşağıdaki iddia→URL çiftleri KURAL-TABANLI seçildi (çıktının son üçte-birinden ≥1 + tüm sayısal iddialar). Her biri için KAYNAĞA İN (WebFetch): iddia ve rakam kaynak metinde GERÇEKTEN var mı? Sonuç: TUTUYOR / TUTMUYOR / ERİŞİLEMEDİ (403-paywall). Not: tek cümle — kaynakta ne gördün (rakamı/sürümü aynen aktar). Uydurma yok; yorum yok; yalnız doğrula. Repoya dosya yazma, alt-ajan açma.
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
    const P = `Önerme P: ${c.claim}\n  kanıt: ${c.source_url} · rakam: ${c.figure} · kapsam: ${c.scope} · deterministik: ${c.determinism}`
    const N = x ? `Önerme ¬P: ${x.negation}\n  kanıt: ${x.evidence_url} · rakam: ${x.figure} · not: ${x.note} · karşı-tarafın öz-değerlendirmesi: ${x.verdict}` : `Önerme ¬P: (karşı-taraf bu önermeye itiraz getirmedi)`
    return `### ${c.id}\n${tezFirst ? 'Taraf-1 — ' + P + '\nTaraf-2 — ' + N : 'Taraf-1 — ' + N + '\nTaraf-2 — ' + P}`
  }).join('\n\n')
  const extras = ((r.anti && r.anti.extra_counter_claims) || []).map(c => `- [${c.id}] ${c.claim} — ${c.source_url} · ${c.figure} · ${c.scope} · deterministik: ${c.determinism}`).join('\n')
  const v26txt = (r.v26 && r.v26.checks || []).map(c => `- [${c.claim_id}] ${c.url} → ${c.result}: ${c.note}`).join('\n')
  return agent(
`ROL: MASKELİ HAKEM — aile ${fam.key}: ${fam.title}. Sen üretici koşumların devamı DEĞİLSİN; iki tarafın hangisinin "tez" hangisinin "antitez" olduğu sana SÖYLENMİYOR — iddia+kanıt olarak tart.
Ölçüt = adversarial-hayatta-kalma: bilgili karşı-tarafın çürütmeyi deneyip BAŞARAMADIĞI önerme SAĞLAM; kısmen çürüyen DARALDI (hayatta kalan daraltılmış hâlini yaz); çürüyen DÜŞTÜ; iki taraf da güçlü ve uzlaşmazsa ÇELİŞKİLİ. Kanıt gücü: birincil > ikincil; rakamlı > rakamsız; sürüm-damgalı > damgasız. KAYNAK-DENETİMİ kuralı (V26): bir tarafın denetlenen iddiası TUTMUYOR çıktıysa o tarafın o ailedeki TÜM iddiaları K'ya düşer (nota yaz). Şüphede kaynağa kendin inebilirsin (WebFetch), bütçe idareli (≤6). HAZIR-ÜRÜN SÜRÜM damgalarını (D2/Mermaid/Graphviz/ELK/araçlar) üreticiden kopyalama — releases sayfasından kendin yeniden çek ve yapı-taşına damgala.
DETERMİNİZM ÖNCELİĞİ (sahibin kuralı, Karar 65): yapı-taşı deterministik değilse (deterministic=h) ya "girmez" ya da deterministik varyantıyla BİRLİKTE yazılır; çelişkide determinizm kazanır — hükümlerde açıkça uygula.
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + deterministic e/h/— + ürün-sürüm damgası) + kör noktalar (aranıp bulunamayan; özellikle yerleşim determinizmi ölçümü · LLM-D2 üretim doğruluğu · okunur düğüm-sayısı eşiği · Türkçe/Unicode yoksa AÇIKÇA) + survival sayımı.
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

log('gorev-2026-08-22-2 sahada: 3 aile × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok; determinizm-önceliği (Karar 65) + sürüm yeniden-çekme kuralı hakemde')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: (args && args.emir) || 'cc/gorev-2026-08-22-2.md', families: out }