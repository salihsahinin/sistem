export const meta = {
  name: 'dil-secimi-ekosistem-m40b',
  description: 'm.40b ekonomi: 3 aile × (tez → CoVe-Factored antitez → V26 kural-tabanlı örneklem → maskeli hakem) — Jarvis + Jarvis-gibi ürün ekosistemi için hangi iş sınıfı hangi dilde (Go/Rust/Python/TS/shell + CUE-sınıfı konfig/şema/politika dilleri); determinizm-önceliği (Karar 65); gorev-2026-08-26-1',
  phases: [
    { title: 'Tez', detail: 'aile başına bağımsız atlas tez koşumu (Opus, medium)', model: 'opus' },
    { title: 'Antitez', detail: 'yalnız iddia listesi verilir (gerekçesiz) — ¬T ara (Opus, medium)', model: 'opus' },
    { title: 'V26', detail: 'KURAL-TABANLI örneklem: son üçte-birden ≥1 URL li iddia + TÜM sayısal iddialar (Sonnet, low)', model: 'sonnet' },
    { title: 'Hakem', detail: 'taraf-maskeli kıyas → SAĞLAM/DARALDI/DÜŞTÜ/ÇELİŞKİLİ + yapı-taşları + deterministik damgası (üst model, high)' },
  ],
}

// ---------- ortak bloklar (emir: cc/gorev-2026-08-26-1.md) ----------
const BAGLAM = `BAĞLAM: Jarvis = tek-kullanıcılı, TÜRKÇE markdown-kanon + SQLite tabanlı kişisel LLM-operasyon sistemi; Claude Code (terminal/masaüstü, Mac) üzerinde çalışır; kodunun YAZARI LLM'dir (üst model orkestratör, Opus/Sonnet işçiler), sahibi (Matematik Müh. 3. sınıf, Python bilir, sistem dili deneyimi yok) kodu OKUR ve denetler. Sahibin emri (aynen): "jarvis bir sistem ve jarvis gibi ürünlerle bir ekosistem oluşturmak istiyorsam hangi durumlar için sistemde kodları hangi dilde (örneğin go, cue lang'de yazdığı gibi) yazmak en mantıklıdır bunu araştır". Senin ailen bu sorunun bir boyutuna DIŞ KANIT getirir; kararı sen vermezsin, Jarvis için kod/şema yazmazsın, dil ÖNERMEZSİN — hangi durumda hangi dilin ÖLÇÜLMÜŞ/BELGELİ üstünlüğü olduğunu kaynaklı yazarsın.
DETERMİNİZM ÖNCELİĞİ (sahibin Katman-1 kuralı, aynen: "determinizmle çelişkilerde determinizm kazanır"): her dil/araç/yöntem iddiasına "deterministik: e / h / — (+ neden, tek cümle)" damgası vur — derleme/kurulum tekrar-üretilebilir mi (reproducible build, bağımlılık kilidi), çıktı aynı girdiye aynı mı, LLM-üretimli kodun dil-nadirliğiyle oynaklığı; bilmiyorsan "—" ve neyin bilinmediğini yaz.
DİĞER DEĞİŞMEZLER: HAZIRI TEMEL AL (hazır standart/araç varsa göster, sıfırdan icat yok) · AÇIK KAYNAK + OKUNABİLİRLİK (sahip okuyabilmeli; kaynak dosyalar Türkçe, kod tanımlayıcıları istisna — Unicode/Türkçe tanımlayıcı desteği bir ölçüttür) · bağımlılık/araç-zinciri ekleme görünür bedeldir (+1) · CV/öğrenme ekseni teknik uygunluğu EZMEZ.`

const KANON = `KANONDA ZATEN BİLİNENLER (verili; yeniden keşfetme, ÜSTÜNE KOY):
- Jarvis sondajı (08-26, deterministik — Mac 26.6.1 / Python 3.9.6 sistem / node v26.7.0 / sqlite3 3.51.0 / rg 14.1.1): çalışan kod = 43 Python dosyası / 8.583 satır (tools/ 27 script 6.675 satır; hepsi STDLIB-ONLY, üçüncü-parti paket yok; en büyüğü 985 satır) + 10 Claude-Code-Workflow script'i / 2.048 satır JavaScript (Workflow DSL = JS zorunlu; seçim değil dayatma) + 2 bash hook / 68 satır (PreToolUse teli 24 · SessionStart 44) + 1 PowerShell 22 satır (Windows artığı, terk). Kurulu DEĞİL: go · cargo/rustc · cue · pkl · nickel · jsonnet · opa · dhall · deno · bun · uv. Tüketilen üçüncü-parti ikililer: ripgrep (Rust) · treehouse (Go, Mach-O arm64, brew) · gnhf + lavish-axi + gh-axi + chrome-devtools-axi (hepsi Node/TS, npm) · sqlite3 (C) · DuckDB (C++). Mac başlangıç-gecikmesi (n=10 medyan): yerel exe taban 1,6 ms · bash 2,1 · sqlite3 2,7 · python3 boş 15,4 · python3 + stdlib import 26,7 · node boş 23,8 · PreToolUse hook (bash+python) 30,7 ms · SessionStart 67,7 · tipik tools/ script 105,5. ⇒ derlenmiş ikilinin çağrı başına TAVAN kazancı ≈14 ms.
- rapor-2026-07-30-10 (VERİLİ, m.40b; 126 satırlık Jarvis + Windows ölçümü, 07-31): H1 ayrım işlerde değil FAZLARDA (tespit deterministik → kod; onarım/yargı → model) · H2 token hipotezi yalnız okuma-yoğun kontrollerde; asıl gerekçe ZORLAMA · H4 dil sorusunun cevabı MİMARİ çıktı (6 süreç→1: kazancın %95,2'si dil değiştirmeden) · H5 (07-31 itibarıyla) Rust'ın resmî Anthropic SDK'sı YOK, Go API SDK var Agent SDK yok, Agent SDK yalnız Python+TS — BU BUGÜN GÜNCELLENMELİ · H6 şema katmanı yalnız makine okuyunca doğar · §4.6 iş-sınıfı hükmü: dedektör/hook = Python stdlib tek dosya · zamanlanmış iş = platform-yerli · sunucu-taraf zorlama = YAML/ayar · üçüncü-parti denetim araçları ikili olarak tüketilir · Rust hiçbir sınıfta · Go'nun TEK meşru tetiği = tek-ikili olarak BAŞKA MAKİNEYE dağıtım (o gün tetik yoktu; bugünkü "ekosistem/ürün" sorusu tam o tetiği sorar).
- Kanon ilkeleri: Karar 65 determinizm önceliği · hazırı temel al · açık kaynak + Türkçe kaynak dosyalar · m.30 policy-as-code = regex/liste (LLM-judge değil) · m.42 bağımlılık ekleme +1 bedel · pointer ilkesi · her eşik YEREL ölçümle kalibre edilir · Mac tek canlı alan.
- E-4 (sahip beyanı 08-24): "Kun Chen'in yaptığı gibi ürünler oluşturabilmek" → bugün tools/*.py deterministik çekirdek + ince SKILL.md tetik katmanı; eksik: (a) axi-standardı (makine-okur stdout JSON + ilerleme stderr + ajan-ergonomik alt-komutlar) (b) paketleme/sürümleme. Codex CLI yakında alınacak (Karar 46). Kun Chen ürün ailesi: treehouse Go · gnhf/lavish-axi/gh-axi/chrome-devtools-axi Node/TS.
- Jarvis'in şema/kural yükü (B ailesi için): bronz JSONL kayıt şemaları (zorunlu alan + enum; Python doğrulayıcı) · karar-borcu ledger enum'ları · PreToolUse deny/allow listesi (bash + regex) · SKILL.md/agent frontmatter (YAML) · settings.json · veri sözleşmeleri (freshness/test; Python) · tüzük maddeleri m.38 bağlaç setiyle (∧ ∨ ¬ → ↔) yazılı ama makine-okur DEĞİL · pipeline manifestleri Markdown tablo.
- Bilinmeyen (çekirdek): (i) 8,6k-satırlık Python-stdlib + JS-workflow sistemi için iş-sınıfı × dil matrisi hâlâ "Python + platform-yerli" mi; hangi sınıfta (uzun-ömürlü süreç/MCP sunucusu · dağıtılabilir ürün · sıcak hook · veri hattı) Go/TS/Rust ÖLÇÜLMÜŞ kazanç getirir · (ii) CUE-sınıfı dillerin bu şema/kural yükünde yeri; hangi durumda JSON Schema + Python/TS doğrulayıcıyı geçer · (iii) ekosistem için protokol + dağıtım kanalı + polyglot/plugin hazır standartları · (iv) geçiş eşiği: hangi ölçüm prototip dilinden çıkartır (rakamlı vakalar) · (v) LLM'in dil-başına kod-üretim doğruluğu ve nadir-dil etkisi.
- Kural: ÜRÜN + SÜRÜM + TARİH damgası zorunlu (Go 1.2x · Rust 1.8x · Python 3.1x · CUE v0.1x · Pkl 0.2x · OPA 1.x · SDK sürümü · benchmark → model + veri kümesi + metrik + tarih); "X daha hızlı/güvenli" iddiası ölçüm+kapsam olmadan K; dil-savunucusu blog/satıcı yazısı D sayılmaz (ölçüm tablosu ya da resmî duyuru görülmedikçe).`

const DISIPLIN = `ÇIKTI DİSİPLİNİ (zorunlu):
- Her iddiaya URL (birincil kaynak: resmî docs / kaynak kodu README-releases / resmî duyuru / standart metni / arXiv-ACL / benchmark liderlik tablosu). Rakamlar kaynaklı; kestirimse "[?]". Örneklem/kapsam/sürüm/veri-kümesi yaz (çıplak yüzde yasak). Her sayısal iddiada figure alanını doldur — sonradan KAYNAĞA İNİLEREK denetlenecek.
- UYDURMA YASAK. "bulunamadı" meşru sonuçtur. "[ARANAMADI]" = arama hiç yapılamadı (bütçe/erişim). Erişim engeli (403/paywall) açıkça bayraklanır.
- Etiket: D = birincil kaynaktan doğrulandı · K = ikincil/özet, teyide muhtaç · X = doğrulanamadı/çelişkili. Satıcı/dil-savunucusu iddiası D sayılmaz.
- Niceleyici ayrımı: "her" (∀) ↔ "bazı" (∃) karıştırma. Ürün+sürüm+tarih ∨ veri-kümesi damgası her iddiada. Her dil/araç/yöntem iddiasında determinism alanı dolu (e / h / — + neden).
- Bütçe İDARELİ: ~10-15 dış erişim; bilinen birincil kaynağa DOĞRUDAN git; arama yalnız var/yok negatifi için. Bütçe biterse belirt.
- Repoya/diske HİÇBİR DOSYA YAZMA. Paket KURMA, yerel sınama YAPMA. Alt-ajan AÇMA. Tek çıktın yapısal cevaptır. Karar ALMA, dil ÖNERME, Jarvis kodu/şeması TASARLAMA — sen kanıt getir.`

const FAMILIES = [
  { key: 'A', title: 'SİSTEM ÇEKİRDEĞİ — İŞ SINIFI × DİL (Go · Rust · Python · TypeScript · shell): ölçülmüş kıyas + Anthropic/MCP SDK güncel dil desteği + agentic-CLI fiilî dağılım + LLM dil-başına kod-üretim doğruluğu + araç-zinciri/tekrar-üretilebilirlik',
    questions: `A1. İş sınıfı başına ölçülmüş kıyas: (1) sıcak hook / kısa-ömürlü CLI (başlangıç gecikmesi: derlenmiş ikili ↔ Python ↔ Node; yayımlanmış ölçümler, ms + platform) · (2) veri hattı/ETL (SQLite/DuckDB/parquet işleme; Python stdlib ↔ Go ↔ Rust throughput; tek-kullanıcı 10⁴-10⁵ satır ölçekte fark var mı) · (3) uzun-ömürlü süreç / daemon / MCP sunucusu (eşzamanlılık modeli, bellek, hata izolasyonu, sinyal/yeniden-başlatma) · (4) dağıtılabilir ürün ikilisi (tek-dosya / cross-compile: Go · Rust · PyInstaller/PyOxidizer/PyApp/uv · Bun compile / Node SEA / pkg — çıktı boyutu MB + kurulum adımı + notarization) · (5) LLM-çağıran orkestrasyon (SDK dilleri). Her hücre: rakam + kaynak + kapsam.
A2. Anthropic ekosistemi GÜNCEL (2026-08): Claude Agent SDK hangi dillerde resmî (Python · TypeScript · Go? · Rust? · Java? — resmî doküman + repo tarihi/sürüm) · Anthropic API SDK listesi güncel · MCP resmî SDK'ları (TypeScript · Python · Go · Rust/rmcp · Java · C# · Kotlin · Swift · Ruby — sahiplik: modelcontextprotocol org altında resmî mi, topluluk mu; sürüm; tarih) · Claude Code'un kendi dili + hook/plugin/skill sözleşmesi (hook = herhangi bir çalıştırılabilir; stdin JSON → stdout/exit kodu; hangi dilde yazılabilir — resmî doküman).
A3. Agentic-CLI/ajan-araç ekosisteminin FİİLÎ dil dağılımı (kaynak kodu/README/duyuru, sürüm+tarih): Claude Code (TS) · OpenAI Codex CLI (TS → Rust GEÇİŞ: tarih + resmî gerekçe + varsa rakam) · Gemini CLI (TS) · aider (Python) · goose (Rust) · opencode (Go/TS?) · gh CLI (Go) · treehouse (Go) · gnhf (TS) · ripgrep/uv/ruff (Rust) · esbuild (Go) · Turborepo (Go→Rust: gerekçe) · Bun (Zig) · Deno (Rust) — ortak desen: hangi İŞ SINIFI hangi dile gitmiş, NEDEN (resmî beyanla).
A4. LLM kod-üretim doğruluğu DİL BAŞINA (Jarvis'in yazarı LLM): MultiPL-E · HumanEval-X · SWE-bench Multilingual · Aider polyglot leaderboard · McEval/MdEval · BigCodeBench — Python ↔ TypeScript ↔ Go ↔ Rust ↔ bash pass@1 / çözüm oranı sayıları (model adı + tarih + veri kümesi); nadir/az-veri dilde hata artışı kanıtı; "statik tip + derleyici hatası ile LLM kendini düzeltir" iddiasının ÖLÇÜMÜ (tip/derleyici geri-beslemesi kazancı — kaynak); Go/Rust için LLM-ajan tamamlama oranı kıyası varsa.
A5. Bağımlılık/araç-zinciri bedeli + tekrar-üretilebilirlik: uv.lock/pip ↔ package-lock ↔ go.mod/go.sum ↔ Cargo.lock; reproducible build durumu (Go -trimpath varsayılan tekrar-üretilebilirlik · Rust · Python wheel/PyInstaller) · tek-kişilik bakım (sürüm yükseltme sıklığı, kırılma oranı — kaynak) · Python 3.9 EOL tarihi (resmî) ve macOS sistem Python'una yaslanmanın riski · stdlib-only stratejisinin sınırı (hangi işte 3.-parti kaçınılmaz).`,
    antitezHint: '07-30 hükmü bugün de doğru: Python stdlib her sınıfta yeter · Go\'nun tek tetiği dağıtım, o da uv tool/pipx ile Python\'da çözülür · Mac\'te başlangıç gecikmesi ölçülemez kadar küçük · LLM\'ler Go/Rust\'ta EŞİT ya da daha kötü yazar, derleyici geri-beslemesi kazancı ölçümsüz · Agent SDK dil desteği hâlâ Python+TS · Codex Rust geçişi ölçek/güvenlik gerekçeli, kişisel sisteme taşınmaz.' },
  { key: 'B', title: 'KONFİG · ŞEMA · POLİTİKA · KURAL DİLLERİ — hangi DURUMDA CUE-sınıfı dil (CUE · Pkl · Dhall · Nickel · Jsonnet · KCL · Starlark · HCL · Rego/OPA · Cedar · Datalog), hangi durumda JSON Schema + Python/TS doğrulayıcı',
    questions: `B1. Dil envanteri (her biri: ne çözer · tip/kısıt modeli · determinizm (saf mı, yan-etkisiz mi, sonlanması garanti mi) · gömülü olduğu dil/araç-zinciri (Go-yerli: CUE/HCL/Starlark/Rego; JVM: Pkl; Rust: Nickel; Haskell: Dhall; C++: Jsonnet) · sürüm/olgunluk/lisans/bakım (son sürüm tarihi) · Unicode/Türkçe alan adı desteği (tanımlayıcı gramerinden) · editör/LSP · çıktı JSON/YAML/kod üretimi): CUE · Pkl · Dhall · Nickel · Jsonnet · KCL · Starlark · HCL · Rego/OPA · Cedar · JSON Schema (2020-12) · TOML/YAML · Python pydantic/dataclass · TS zod/typebox.
B2. DURUM × DİL kanıtı: (1) JSONL kayıt şeması doğrulama (zorunlu alan, enum, tip; satır-akışı) · (2) politika-as-code (araç-çağrısı deny/allow listesi; hook policy; "regex/liste, LLM-judge değil" kuralı) — OPA/Rego · Cedar · CUE constraint · düz JSON + Python: hangisi ne zaman kazanır, belgeli vaka (ör. AI-ajan araç-izin politikası için OPA/Cedar kullanan gerçek ürün var mı) · (3) konfig ÜRETİMİ/birleştirme (çok-ortam, kalıtım, DRY; settings.json / skill tanımı / pipeline manifesti) · (4) veri sözleşmesi (freshness/test/contract: dbt tests · Great Expectations · Soda · pandera · CUE) · (5) KURAL LOJİĞİ (∧∨¬→↔ ile yazılmış tüzük maddesinin makine-okur/çalıştırılır formu: Datalog (Soufflé · Mangle · Logica · Datomic-tarzı) · Rego · Alloy/TLA+ spec · CUE) — tek-kullanıcı kişisel sistemde hangi durumda gerçekçi, kanıt/vaka.
B3. CUE özelinde derin (resmî doküman + repo): unification/lattice modeli · şema+veri+kısıt tek dilde · cue vet/export/import/def · Go gömme (cuelang.org/go) · OpenAPI/JSON Schema/Protobuf/Go-tip içe-aktarma · güncel sürüm (v0.1x, tarih) ve kararlılık beyanı · bilinen sınırlar (fonksiyon yok, koşullu mantık, öğrenme eğrisi, hata mesajları, Unicode tanımlayıcı kuralı) · gerçek kullanıcılar (Dagger · Kubernetes ekosistemi · diğer) · LLM'in CUE üretim doğruluğu (nadir dil; benchmark/kanıt var mı — yoksa AÇIKÇA yok).
B4. Kişisel/tek-kullanıcı ölçekte eşik: "JSON Schema + doğrulayıcı" ne zaman yetmez (kalıtım/DRY/kısıtlar-arası bağımlılık/çok-ortam eşiği) — yayımlanmış kural/vaka var mı · konfig dili ekleme bakım borcu (yeni araç zinciri, LSP, öğrenme saati) rakamları · JSON Schema'nın kendi sınırları (kısıtlar-arası bağımlılık, hesaplama) belgeli.`,
    antitezHint: 'CUE gereksiz: JSON Schema + Python/TS doğrulayıcı yeter · yeni konfig dili öğrenme/araç-zinciri bedeli kazancı aşar · LLM nadir dilde (CUE/Nickel/Pkl/Dhall) halüsinasyon yapar, eğitim verisi az · Rego/Cedar tek-kullanıcı sistemde aşırı · Datalog pratik değil · CUE pre-1.0 ve kırıcı değişiklik geçmişi · Unicode tanımlayıcı sınırı Türkçe alan adlarını kırar · konfig dili = ikinci gerçek-kaynak riski.' },
  { key: 'C', title: 'EKOSİSTEM — "JARVIS GİBİ ÜRÜNLER": ajan-ergonomik protokol (axi/MCP) · dağıtım kanalı · polyglot yönetimi + plugin mimarisi · GEÇİŞ EŞİĞİ vakaları · çok-ürün aile anatomisi',
    questions: `C1. Ajan-ergonomik ürün standardı: "axi" deseni (makine-okur stdout JSON/TOON + ilerleme stderr + alt-komut + kısa çıktı) hangi HAZIR standartlara oturur — MCP tool sözleşmesi (stdio/HTTP) · JSON-RPC 2.0 · Claude Code plugin/skill/agent/hook spec (resmî doküman: dosya formatı, dil serbestliği) · agent-skills açık spec · CLI --json konvansiyonları (gh · kubectl · jq · clig.dev) — dilden bağımsızlık derecesi; stdio-MCP sunucusu için dil seçimi ölçütleri (başlangıç gecikmesi × SDK olgunluğu × dağıtım) kaynaklı.
C2. Dağıtım kanalı kıyası (kullanıcı başına kurulum adımı · indirme boyutu MB · çalışma-zamanı bağımlılığı · macOS imzalama/notarization gereği · otomatik güncelleme · sürümleme): Homebrew formula/tap · npm/npx · pipx / uv tool install · go install · cargo-binstall · GitHub release tek-ikili · Claude Code plugin marketplace — hangi dil hangi kanala doğal (resmî doküman); tek-kullanıcı → 10 kullanıcı → açık-kaynak topluluk ölçeğinde hangi kanal ne zaman (vaka/kaynak).
C3. Polyglot yönetimi: tek-kaynak şema → çok-dil üretimi (JSON Schema → Python/TS/Go tipleri: datamodel-codegen · quicktype · json-schema-to-typescript · go-jsonschema; CUE → Go/TS; Protobuf) · mono-repo/multi-repo · ortak test/CI · plugin dili bağımsızlığı (WASM: Extism · wasmtime · component model — olgunluk, sürüm, gecikme, kısıt) · "dil sayısı" bakım maliyeti ölçümü (kaynak: çok-dilli repo çalışmaları, hata oranı, ekip büyüklüğü).
C4. GEÇİŞ EŞİĞİ vakaları (rakamlı, resmî beyan): Codex CLI TypeScript→Rust (2025: gerekçe — başlangıç, bellek, Node-bağımsız kurulum, güvenlik sandbox; varsa rakam) · Turborepo Go→Rust · uv/ruff (neden Python değil; hız rakamları) · Pydantic v2 core Rust (hız rakamı) · esbuild Go tercihi (yazarın gerekçesi) · Bun Zig · Deno Rust · Zed · KARŞI ÖRNEKLER: Python'da kalan büyük ajan/araç projeleri (aider · LangChain · Home Assistant · Ansible) ve TS'de kalanlar (Claude Code · Gemini CLI) gerekçeleriyle — "prototip dilinden ne zaman çık" için yayımlanmış kural/eşik (satır · kullanıcı sayısı · p95 gecikme · kurulum şikâyeti · güvenlik) var mı.
C5. Çok-ürün aile anatomisi: aynı yazarın Go (treehouse) + Node/TS (gnhf, *-axi) seçimi — repo/README'de gerekçe var mı; Anthropic/OpenAI/Google CLI ekiplerinin çok-dil politikası (resmî beyan varsa); kişisel-sistem → ürün ailesi geçişinde ilk ürün hangi sınıftan başlar (gözlemlenmiş desen: "iç araç → CLI → plugin → SDK" sırası; kaynak); Claude Code plugin marketplace'te yayımlanan eklentilerin dil dağılımı (örneklem + tarih).`,
    antitezHint: 'ekosistem için tek dil şart değil, MCP/stdio dilden bağımsız · dağıtım için uv tool/pipx yeter, tek-ikili gerekmez · yeniden-yazma vakaları milyon-kullanıcı ölçeğinde, kişisel sisteme taşınmaz · WASM plugin erken/olgun-değil · polyglot maliyeti abartılıyor ∨ tam tersi tek-kişilik bakımda ölümcül · "iç araç → ürün" sırası için kanıt yok, anekdot.' },
]

// ---------- şemalar ----------
const PLACEMENTS = ['iş-sınıfı→dil-kuralı','konfig-şema-dili-kuralı','hazır-ürün-araç','dağıtım-kuralı','geçiş-eşiği','ölçüm-yöntemi','girmez']
const JARVIS = ['kullanıyoruz-eş','kısmi','eksik-aday','girmez']
const CLAIM = { type: 'object', additionalProperties: false, required: ['id','claim','label','source_url','figure','scope','determinism','placement_suggestion'],
  properties: {
    id: { type: 'string', description: 'A1-1 gibi: soru-no + sıra' },
    claim: { type: 'string', description: 'tek cümle iddia (Türkçe)' },
    label: { type: 'string', enum: ['D','K','X'] },
    source_url: { type: 'string', description: 'URL ya da "bulunamadı" ya da "[ARANAMADI]"' },
    figure: { type: 'string', description: 'rakam/eşik/sayı/tarih/sürüm (kaynaklı; kestirimse [?]); yoksa "-"' },
    scope: { type: 'string', description: 'ürün+sürüm+tarih ∨ veri-kümesi+metrik+model + örneklem/kapsam; yoksa "-"' },
    determinism: { type: 'string', description: 'dil/araç/yöntem iddiasıysa "e" / "h" / "—" + tek-cümle neden (tekrar-üretilebilir derleme/kurulum; aynı girdi→aynı çıktı; LLM-üretim oynaklığı); iddia yöntem değilse "-"' },
    placement_suggestion: { type: 'string', description: 'yerleşim (' + PLACEMENTS.join(' / ') + ') + Jarvis eşlemesi (' + JARVIS.join(' / ') + ') + damga' },
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
    note: { type: 'string', description: 'DARALTILDI ise daraltılmış hâl; ÇÜRÜTÜLEMEDİ ise ne arandı; determinizm itirazı varsa burada' },
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
    building_blocks: { type: 'array', minItems: 3, maxItems: 8, items: { type: 'object', additionalProperties: false, required: ['block','source_url','placement','jarvis','deterministic','confidence'],
      properties: { block: { type: 'string' }, source_url: { type: 'string' }, placement: { type: 'string', enum: PLACEMENTS, description: 'yerleşim sınıfı' }, jarvis: { type: 'string', enum: JARVIS, description: 'Jarvis eşlemesi (sondajdaki mevcut duruma göre)' }, deterministic: { type: 'string', enum: ['e','h','—'], description: 'Karar 65: h ise yapı-taşı "girmez" ya da deterministik varyantıyla birlikte yazılır' }, confidence: { type: 'string', enum: ['D','K'] } } } },
    blind_spots: { type: 'array', items: { type: 'string' } },
    survival: { type: 'object', additionalProperties: false, required: ['saglam','daraldi','dustu','celiskili'], properties: { saglam: { type: 'integer' }, daraldi: { type: 'integer' }, dustu: { type: 'integer' }, celiskili: { type: 'integer' } } },
  } }

// ---------- V26 KURAL-TABANLI seçim (Salih imzası 08-17; deterministik — rastgele YOK) ----------
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
Çıktı: 4-10 iddia (her soruya ≥1), her biri kaynaklı; gaps/access_blocks/budget_note doldur. Sayısal iddialarda figure alanı ZORUNLU dolu; her iddiada ürün-sürüm ∨ veri-kümesi damgası; dil/araç/yöntem iddialarında determinism alanı dolu.`,
  { label: `tez:${fam.key}`, phase: 'Tez', agentType: 'atlas', model: 'opus', effort: 'medium', schema: TEZ_SCHEMA })

const antitezStage = (tez, fam) => {
  if (!tez) return null
  const claimsOnly = tez.claims.map(c => `${c.id}: ${c.claim}`).join('\n')  // gerekçe/kaynak GEÇMEZ (CoVe-Factored)
  return agent(
`ROL: Atlas ANTİTEZ ajanı (açık Devil's-Advocate) — aile ${fam.key}: ${fam.title}.
Sana bir başka araştırmacının İDDİA satırları veriliyor; GEREKÇELERİ ve KAYNAKLARI kasıtlı olarak verilmiyor (çıpalama freni). Görevin: her iddianın DEĞİLİNİ (¬T) savunacak BİRİNCİL kanıt aramak — "alternatif bakış" değil, lojiksel ters. Çürütemediysen "ÇÜRÜTÜLEMEDİ" yaz ve ne aradığını belirt; süs-antitez ÜRETME. Kısmen çürüttüysen DARALTILDI + daraltılmış hâlini yaz. Determinizm-önceliği gereği: iddia bir dili/aracı "deterministik/tekrar-üretilebilir" sayıyorsa bunun aksini (kilit-dosyası sürüklenmesi, derleme çıktısı farkı, LLM-üretim oynaklığı) da ara.
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
    const P = `Önerme P: ${c.claim}\n  kanıt: ${c.source_url} · rakam: ${c.figure} · kapsam: ${c.scope} · deterministik: ${c.determinism}`
    const N = x ? `Önerme ¬P: ${x.negation}\n  kanıt: ${x.evidence_url} · rakam: ${x.figure} · not: ${x.note} · karşı-tarafın öz-değerlendirmesi: ${x.verdict}` : `Önerme ¬P: (karşı-taraf bu önermeye itiraz getirmedi)`
    return `### ${c.id}\n${tezFirst ? 'Taraf-1 — ' + P + '\nTaraf-2 — ' + N : 'Taraf-1 — ' + N + '\nTaraf-2 — ' + P}`
  }).join('\n\n')
  const extras = ((r.anti && r.anti.extra_counter_claims) || []).map(c => `- [${c.id}] ${c.claim} — ${c.source_url} · ${c.figure} · ${c.scope} · deterministik: ${c.determinism}`).join('\n')
  const v26txt = (r.v26 && r.v26.checks || []).map(c => `- [${c.claim_id}] ${c.url} → ${c.result}: ${c.note}`).join('\n')
  return agent(
`ROL: MASKELİ HAKEM — aile ${fam.key}: ${fam.title}. Sen üretici koşumların devamı DEĞİLSİN; iki tarafın hangisinin "tez" hangisinin "antitez" olduğu sana SÖYLENMİYOR — iddia+kanıt olarak tart.
Ölçüt = adversarial-hayatta-kalma: bilgili karşı-tarafın çürütmeyi deneyip BAŞARAMADIĞI önerme SAĞLAM; kısmen çürüyen DARALDI (hayatta kalan daraltılmış hâlini yaz); çürüyen DÜŞTÜ; iki taraf da güçlü ve uzlaşmazsa ÇELİŞKİLİ (saklama, öyle yaz). Kanıt gücü: birincil > ikincil; rakamlı > rakamsız; sürüm/veri-kümesi damgalı > damgasız. KAYNAK-DENETİMİ kuralı (V26): bir tarafın denetlenen iddiası TUTMUYOR çıktıysa o tarafın o ailedeki TÜM iddiaları K'ya düşer (nota yaz). Şüphede kaynağa kendin inebilirsin (WebFetch), bütçe idareli (≤6). HAZIR-ÜRÜN/DİL SÜRÜM KURALI (08-22): yapı-taşı bir ürün/dil/SDK sürümü taşıyorsa sürümü ve tarihini KENDİN yeniden çek, tarafların yazdığına güvenme.
DETERMİNİZM ÖNCELİĞİ (sahibin kuralı, Karar 65): yapı-taşı deterministik değilse (deterministic=h) ya "girmez" ya da deterministik varyantıyla BİRLİKTE yazılır; çelişkide determinizm kazanır — bunu hükümlerde açıkça uygula.
Sonda: bu aileden JARVIS'e girecek 3-8 yapı-taşı (yalnız SAĞLAM/DARALDI önermelerden; her biri kaynak URL + yerleşim: ${PLACEMENTS.join(' / ')} + Jarvis-eşleme: ${JARVIS.join(' / ')} + deterministic e/h/— + ürün-sürüm ∨ veri-kümesi damgası; 'hazır-ürün-araç' yalnız bakım/lisans/sürüm durumu bilinen ürünlerde) + kör noktalar (aranıp bulunamayan; özellikle LLM dil-başına doğruluk GÜNCEL model sayısı · tek-kişilik polyglot bakım ölçümü · CUE LLM-üretim ölçümü · Agent SDK Go/Rust güncel durumu · kişisel-ölçek geçiş eşiği yoksa AÇIKÇA) + survival sayımı.
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

log('gorev-2026-08-26-1 sahada: 3 aile (A sistem-çekirdeği × dil · B konfig/şema/politika dilleri · C ekosistem/dağıtım/geçiş) × tez(opus)→antitez(opus)→V26 kural-tabanlı(sonnet)→hakem(üst model) — pipeline, barrier yok; determinizm-önceliği (Karar 65) tüm rollerde')
const results = await pipeline(FAMILIES, tezStage, antitezStage, v26Stage, hakemStage)
const out = {}
FAMILIES.forEach((f, i) => { out[f.key] = results[i] || null })
const done = FAMILIES.filter((f,i)=>results[i] && results[i].hakem).map(f=>f.key)
log(`Tamam: hakem çıktısı olan aileler = ${done.join(',') || 'yok'}`)
return { date: args && args.date, emir: (args && args.emir) || 'cc/gorev-2026-08-26-1.md', families: out }