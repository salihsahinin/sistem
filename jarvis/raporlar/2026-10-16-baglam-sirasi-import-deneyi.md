# Bağlam sırası: `@`-içe aktarma deneyi (hafıza → Lean/Rust geçişi, adım 1)

AS-OF 2026-10-16 · Claude Code 2.1.302 · Windows 11 · deneysel (n = 4 koşum, model `sonnet`, `claude -p --setting-sources project --tools ""`)
Deney dosyaları: oturum scratchpad'i `import-deney/`, `import-deney2/` (geçici; düzen aşağıda aynen).

## Soru
md dosyasının bir parçası Lean'e taşındığında Claude Code bağlamı hangi sırayla yükler? `@yol` içe aktarması kesim noktasında mı açılır, `.lean` dosyasını kabul eder mi?

## Düzen
`CLAUDE.md`: baş metin, sonra ayrı satırlarda `@parca/b-lean.lean`, `@parca/c-txt.txt`, `@parca/a-son.md`, `@parca/d-orta.md`; `a-son.md` içinde `@ic.md`. Her dosyada tekil bir işaret jetonu. Model, talimat bloklarını göründükleri sırayla listeledi.

## Bulgular
| # | Bulgu | Kanıt |
|---|---|---|
| B1 | `.lean` uzantılı dosya içe aktarılmaz; hata vermez, sessizce atlanır. | deney 1 ve 2: `lean02` jetonu yok, blok yok |
| B2 | `.md` ve `.txt` içe aktarılır. | `txt03`, `son04` blokları |
| B3 | İçe aktarılan dosya kesim noktasında açılmaz; ebeveynin **tamamından sonra** ayrı blok olarak gelir. `@` satırı ebeveyn metninde ham kalır. | deney 1: `kirmizi71, mavi72, yesil73` tek blokta, `mor91` ayrı blokta sonra |
| B4 | Bloklar önden sıralı derinlik-öncelikli (pre-order DFS) dizilir: ebeveyn, sonra her içe aktarma yazılış sırasıyla, her birinin kendi içe aktarmaları hemen ardından. | deney 2: `bas01, txt03, son04, ic06, orta05` |
| B5 | `.lean` dosyasına `.lean.md` uzantılı sembolik bağ kurulursa içerik yüklenir, sıra B4'e uyar. | deney 2b: `bas01, lean02, txt03, son04, ic06, orta05` |
| B6 | `@` satırı ebeveynin en üstünde olsa bile içe aktarılan dosya ebeveynden **sonra** gelir. Resmi belgedeki "`@AGENTS.md` üstteyse önce o okunur" ifadesi 2.1.302'de tutmaz. | deney 3 (`@ust.md` + gövde): ham API isteğinde sıra `govde01, ust02` |

**Ölçüm yöntemi (B3-B6 için birincil):** model beyanına ek olarak, `ANTHROPIC_BASE_URL` yerel bir dinleyiciye yönlendirildi ve `/v1/messages` gövdesi yakalandı (yetki başlıkları kaydedilmedi). Deney 2 ve 3'ün sırası ham istekten okundu; model beyanıyla aynı.

## Sonuç (formalizasyonun girdisi)
Otomatik yükleme rejiminde bağlam `L(f) = metin(f) ++ L(i₁) ++ … ++ L(iₖ)` (i = f'nin içe aktarmaları, yazılış sırasıyla). Satır içi konum korunmaz, bu yüzden "md başı → Lean → md sonu" sırası için md'nin kesim sonrası kısmı da ayrı dosyaya alınıp Lean'den sonra içe aktarılmalı. Okuma rejiminde (skill'in `Read` ile açtığı `core/` dosyaları) `@` hiç açılmaz; orada sıra ancak bir genişletici (Rust) ile korunur.

Açık: içe aktarma derinlik sınırı ve sembolik bağın git/Windows klonlarında davranışı bu deneyde ölçülmedi.
