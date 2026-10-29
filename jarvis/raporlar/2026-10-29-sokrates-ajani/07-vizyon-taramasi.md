# 07 Vizyon taraması: persona ajanı için sektör / literatür / GitHub kombinasyon analizi (2026-10-29, hedef #72; Salih sorusu: "ajan yap görevi geldiği anda vizyon doğru kurulmalı")

Girdi: 07a persona spec biçimleri · 07b eval çerçeveleri ve metrikler · 07c repo yapıları ve kombinasyonlar (üç Atlas, canlı web, AS-OF 2026-10-29). Bu rapor sentez + fark listesi + uygulama kaydı + kural adayı.

## 1. Sektörde kombinasyon (ne tekrar ediyor)
| Katman | Yaygın seçim | Kanıt |
|---|---|---|
| Persona tanımı | tek markdown/JSON kart: kimlik + konuşma stili + **örnek diyaloglar** + açılış; sert kurallar ayrı dosya (nadir ama en iyi örnekte var) | Character Card V2/V3 (fiili standart), SillyTavern 35k yıldız; Claude Code subagent = frontmatter + gövde (07a); socrates-agent repo `.claude/rules/` ayrımı (07c #1) |
| Bilgi sınırı | hiçbir şemada birinci sınıf alan değil; serbest metin + lorebook; Character-LLM "koruyucu sahne" (dönem dışı soruya şaşkınlık örnekleri) | 07a |
| Drift önlemi | periyodik kimlik yeniden beyanı; hitap/örnek çeşitliliği (aynı 5 örneğe yakınsama arızası) | ContextEcho [K], 07c desen 3 ve kaçınılan hatalar |
| Ölçüm | LLM judge rubriği (persona benchmark'larının hepsi), judge üreticiden farklı model; **ucuz deterministik denetim (regex yasak liste) + pahalı LLM denetimi katmanı**; hileli soru seti | 07b (PersonaGym, CharacterEval, CharacterBench, InCharacter, RoleBench; judge-insan korelasyonu 0,36-0,75), 07c desen 4-5 |
| Çok-turlu test | simüle kullanıcı: promptfoo `simulated-user` + `llm-rubric` (MIT, yerel) ya da DeepEval ConversationSimulator; `claude plugin eval` tek-tur kapı | 07b |
| Anakronizm metriği | hazır yok (TimeChara, Boundary Consistency kavramsal); kendi tuzak seti + regex + rubrik | 07b |
| Repo yapısı | persona dosyası · rules · ornekler (dönen banka) · test (hileli sorular + doğrulayıcı) · kaynak korpus + künye · hafıza (3 kademe) · sürüm/HANDOFF | 07c §4 |
| Olgunluk | Sokrates odaklı repolar 0-342 yıldız, çoğunda eval yok; "persona + eval" olgun referans bulunmadı; mevcut 18 simülasyon + maskeli hakem emsallerin ilerisinde | 07c dürüstlük notu |

## 2. Fark listesi (Sokrates v0.4 → v0.5) ve uygulama
| # | Fark | Uygulandı | Nerede |
|---|---|---|---|
| 1 | Sert kurallar kimlikten ayrı, denetlenebilir liste | evet | `C:\sistem\sokrates\.claude\rules\karakter-yasaklari.md` (desktop yüzeyinde otomatik yüklenir) |
| 2 | Örnek diyalog bankası (mes_example) + promptta 3 örnek | evet | `ornekler/ornek-diyaloglar.md` (6 örnek, tur 3 `GEÇTİ` turlarından); §7 "Örnek konuşmalar" |
| 3 | Hileli soru seti + ucuz deterministik doğrulayıcı | evet | `test/tuzak-sorular.yaml` (20) + `test/tuzak-kosum.py` (`claude -p --agent sokrates`, API anahtarsız; yasak/kelime/soru işareti/em-dash) |
| 4 | Çok-turlu simüle kullanıcı + llm-rubric (hazır araç) | config yazıldı, koşulmadı (ANTHROPIC_API_KEY yok) | `test/promptfooconfig.yaml` (promptfoo 0.125.1; judge Opus, üretici Sonnet) |
| 5 | Hitap/benzetme çeşitliliği (yakınsama arızası) | evet | §7 konuşma kuralı + rules biçim maddesi |
| 6 | Sürüm izi / HANDOFF | evet | `SURUM.md` (+ kanon §9) |
| 7 | Kaynak korpus + künye (uydurma alıntı kapısı) | hayır, borç | Platon metinleri (Gutenberg/Perseus) `kaynak/` altına indirilmeli; indirilen dosya = güvensiz veri, ayrı dizin |
| 8 | Hafıza (oturum özeti) | hayır, borç | `hafiza/`; Letta blok deseni ya da Claude Code `memory: project` alanı |
| 9 | Prompt sıkıştırma (1341 kelime, bütçe 900) | hayır, borç | örnekler ve yasak liste rules dosyasına taşınınca prompt küçülür; agent/skill yüzeyi rules okumaz, çözüm: yüzey başına farklı türetme |
| 10 | Regresyon: `claude plugin eval` tek-tur kapı | hayır, borç | ürün klasörünü plugin yapısına alınca |

## 3. Yöntem denetimi (Salih sorusu)
Önceki akışta eksik düğüm: **"araç-metrik-repo kombinasyon analizi"** inşadan önce yoktu; mekanizma taraması (Claude Code yüzeyleri) vardı, eval harness ve persona spec taraması yoktu; rubrik ve simülasyon elle yazıldı (hazır karşılık kapısı Karar 119 kısmen atlandı). Sonuç olarak yapı emsallerden geri değildi (eval içeren emsal az) ama standart alanlar (örnek diyalog, ayrı kurallar, tuzak seti, deterministik denetim) sonradan eklendi.

## 4. Kural adayı (core/ajan-metodolojisi.md için; Katman-1, Salih imzası)
**Vizyon taraması düğümü:** "X ajanı yap" görevinin ilk düğümü sabit: (a) persona/rol spec biçimleri, (b) eval çerçeveleri + benchmark + metrikler, (c) örnek repo yapıları ve araç kombinasyonları (yıldız/lisans/eval var mı), (d) Claude Code yüzeyleri ve mevcut modlar; çıktı = seçilen kombinasyon + gerekçe + fark listesi; ancak ondan sonra kişilik/kod yazılır. Atlas emri şablonuna "mevcut modlar ve hazır araçlar üzerinden üretim tavsiyesi ver" satırı eklenir. Hazır karşılık kapısı (Karar 119) eval harness'ı da kapsar.

## 5. Kanıt sınırı
Yıldız sayıları anlık; persona repoları çoğunlukla 0-3 yıldız (tasarım örneği, uzlaşı değil). Judge önyargı rakamları blog aktarımı [K]. LangSmith/Braintrust/Inspect çok-turlu desteği doğrulanmadı [X]. Anthropic cookbook persona örnekleri taranmadı [X].
