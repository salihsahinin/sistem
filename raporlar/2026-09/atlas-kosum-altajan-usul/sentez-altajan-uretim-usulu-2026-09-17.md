# Alt-ajan tanımı üretim usulü — Atlas Raporu (2026-09-17)
> **Mod:** ana-sıra (Fable) · şerit: m.40b v0.2 (3 tez ∥ → 3 hedefli antitez → maskeli hakem Opus 5 medium) · aile sayısı: 3 · AS-OF 2026-09-17, canlı çekim
> **Kanıt kısıtı (dürüstlük):** maskeleme sızdı (hakem beyanı: yöntem paragrafları rolü ifşa etti; K2-k şerhi gereği açık beyan) · Inspect AI trajectory-eval birincil kaynağı bulunamadı (X) · promptfoo satın-alma iddiası düştü (kaynaksız) · P2'de 1 iddia bütçede doğrulanamadı.
> **Dosyalar:** tez `tez-F1/F2/F3-*.md` · antitez `antitez-A1/A2/A3-*.md` · hakem `hakem-2026-09-17.md` · V26 sondajı: 15.000 token canlı D; atlas rapor sayımı 141 D / 167≠180 K; 403-dosya sayımı tanıma bağlı K.

## Aile başına bulgular
### Aile 1 — Claude Code subagent sözleşmesi (F1 ↔ A1)
- **Tez:** 25 iddia (23 D). **Antitez:** 0 çürüdü · 5 daraldı · 16 çürütülemedi. **Hakem:** 22 sağlam / 3 daraldı.
- Sağlam çekirdek: `name`+`description` zorunlu, 16 opsiyonel alan (`tools` `disallowedTools` `model` `effort` `permissionMode` `maxTurns` `skills` `mcpServers` `hooks` `memory` `background` `isolation` `color` `initialPrompt` `omitClaudeMd` `experimental`); description'lar toplam 15.000 token; otomatik devir = görev + description + bağlam; `disallowedTools` önce; model çözümleme sırası çağrı → frontmatter → env → oturum; alt-ajan ana geçmişi görmez, CLAUDE.md hiyerarşisini görür (Explore/Plan hariç), Claude Code sistem promptunu ve auto-memory'yi görmez; `skills` tam içerik enjekte; `memory` üç kapsam; `hooks` ajana özel (PreToolUse/PostToolUse/Stop); `agent_id`/`agent_type` yalnız alt-ajan içinde; her zaman kaldırılan araçlar listesi.
- Daralan: sistem promptu gövdesi için resmî **sayısal** uzunluk tavsiyesi yok (CLAUDE.md için 200-satır nüansı ayrı) · `effort` kapsamı kısmî · `memory` yolları.

### Aile 2 — Ajan tasarım desenleri 2026 (F2 ↔ A2)
- **Tez:** 22 iddia (13 D). **Antitez:** 1 çürüdü · 4 daraldı · 16 çürütülemedi. **Hakem:** 12 sağlam / 9 daraldı / 2 düştü.
- Sağlam: orchestrator-workers = merkezî LLM görevi dinamik böler, işçilere dağıtır, sentezler; alt-görevler önceden tanımlı değil · "Building effective agents" rol promptu yapısı vermez, iş-akışı desenleri verir · araç açıklaması = prompt mühendisliği ("işe yeni başlayana anlatır gibi") · Anthropic rehberinde formal en-az-yetki/pozitif-liste çerçevesi **yok**, yerine ölçüm önerisi (süre, çağrı, token, hata) · hibrit bağlam yükleme (ön-getirme + otonom keşif) · prompt XML/Markdown bölümlü, "minimal = beklenen davranışı tam ortaya koyan asgari küme" · rol promptu iki uçtan kaçınır (katı if-else ↔ belirsiz yönlendirme) · Agent Skills = progressive disclosure.
- Düşen: promptfoo'nun 2026-03 satın alımı (kaynaksız) · "agentic context engineering tek otoriter kaynağı yok" (arXiv 2510.04618 / ICLR 2026 karşı kanıt).
- Daralan: en-az-yetki ilkesi Anthropic metninde değil, Jarvis pratiğinde · trajectory-first eval "standart" iddiası K (promptfoo belgeli, Inspect AI değil) · yapan ≠ ölçen birincil kaynak yok, ikincil destek.

### Aile 3 — Atlas'ın gelişim dersleri (F3 ↔ A3)
- **Tez:** 15 iddia. **Antitez:** 1 çürüdü · 2 daraldı · 3+ çürütülemedi. **Hakem:** 9 sağlam / 2 daraldı / 0 düştü / **1 çelişkili**.
- Sağlam: 9 commit (07-14 → 09-10), `model` 3 kez değişti · FELSEFİ TEMELLER kategori-kuramı/ontolojik yığın hiçbir koşuma geri gelmiyor (07-24 raporunda zaten silinmeye aday) · Aşama 5 `docs/research/…` yolu geçersiz (dizin yok; gerçek `cc/rapor/`, `raporlar/`) · EPİSTEMOLOJİK ÖZ-FARKINDALIK işlev üretmiyor, Context7 iddiası fiilen yanlış · fiilen işleyen parçalar: **Kanıt Hiyerarşisi** (9 raporda) + **V26 örneklem-denetimi** · Aşama 1 üçlemesi FELSEFİ TEMELLER'in tekrarı · model-katman mantığı HTML yorumda gömülü, gövdede yok · 403/paywall tekrarlayan arıza sınıfı (≥5 rapor; 56-143 dosya).
- Düşen (tez): "gövde durağan kaldı" — revizyon logu her kararda büyümüş.
- **Çelişkili:** DALGA PROTOKOLÜ yeni şablona alınsın mı — 07-24 bağımsız raporu ile F3 karşıt; kanıt eşit → Salih hükmü.

## V26 örneklem-denetimi
| Ajan | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| F1 | "15,000 tokens" (İ3) | canlı sayfada birebir | D |
| F3 | cc/rapor 'atlas' 141 · raporlar 180 | 141 eş · 167 | K (180 daraldı) |
| A3 | 403/paywall 56 dosya | 143 (geniş regex) | K, sayım tanımı |
| F3/hakem | research-agent.md 18.633/18.645 B | 18.645 | D |

## Sentez
- **Hayatta kalan çekirdek (43 madde; hakem listesi `hakem-2026-09-17.md` sonunda):** alt-ajan tanımı = frontmatter (zorunlu 2 + seçilmiş opsiyoneller) + bölümlü kısa gövde; gövde "minimal ama tam"; kanıt hiyerarşisi + V26 kuralı + erişim-arızası kuralı taşınır; felsefi/ontolojik süs, geçersiz çıktı yolu, öz-farkındalık bölümü taşınmaz; model-katman kuralı gövdede görünür yazılır; en-az-yetki araç listesi Jarvis pratiği olarak kalır (dış doğrulaması yok, iç kanıtı var: Karar 91 kilit vakaları).
- **Yalnız-tez ayakta:** trajectory-eval standardı (K) · yapan ≠ ölçen (K, iç kanıt: İB-66 55,6→44,4).
- **Çelişkili (X):** DALGA PROTOKOLÜ'nün şablona girmesi.
- **Hayatta-kalma oranı (m.40b v0.2 gözlemi):** 60 iddia → sağlam 43 (%72) · daraldı 14 (%23) · düştü 2 (%3) · çelişkili 1.

## Cevaplanmamış sorular (Salih'e)
1. DALGA PROTOKOLÜ (MECE ayrıştırma sorusu) yeni şablonda tutulsun mu, yoksa yalnız `atlas-kosum` SKILL'inde mi kalsın (hakem: çelişkili)?
2. Şablonun kanon yeri: `core/sablonlar/altajan-tanim-v0.md` (Katman-1, Salih) mi, skill referansı mı?
3. Atlas'ın kendisi yeni şablona göre **damıtılsın mı** (18,6 KB → tahmini 7-9 KB `[?]`; silme yok, eski metin arşive)?
