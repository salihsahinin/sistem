# Sokrates ajanı: depo-içi bağlam (01)

AS-OF 2026-10-29 (sistem saati). Kapsam: yalnız `jarvis/` + kök `AGENTS.md`; `veri/bronz`, `arsiv/`, başka ajan dizinleri okunmadı. Arama anahtarları: Sokrat*, elenchus, maieutik, grill, sorgulama. `elenchus` ve `maieutik` terimleri depoda **hiç geçmiyor** (0 eşleşme, `jarvis/` genel taraması; veri/bronz ve arsiv hariç). Yalnız "Sokratik" (sinav-grill, grill-me raporu, hukuk vaka yöntemi) geçiyor.

Not: `kuyruk/senaryo-defteri.md` alt-ajan okuma kilidi (İB-83) nedeniyle okunamadı; K3 hükmü ikincil kaynaklardan (devir dosyası, skill-fikir-kutusu) alındı.

## (a) Bulgular (dosya:satır + özet)

| Dosya:satır | Özet |
|---|---|
| `.claude/skills/sinav-grill/SKILL.md:1-26` | Tek yerel Sokratik mekanizma: Salih tetikli adversarial sorgulama skill'i (S-I, v1, 2026-08-14). Ayrıntı (b). |
| `.claude/skills/sinav-grill/evals/evals.json:4-12` | 3 eval: E1 tetiklenir ("sınava çek"), E2 model-inisiyatifi tetiklemez, E3 ders anlatımı tetiklemez; m.23/m.33 notu. description_eval tetik listesi: sınav, sınava çek, grill, sorguya çek, beni bu konuda sına. |
| `wiki/sozluk.md:123-124` | Sözlük girdisi: "adversarial Sokratik sorgulama", yalnız Salih tetiği, "ben asla kendiliğimden başlatmam (V55 korunur)". |
| `raporlar/2026-07/2026-07-21-grill-me-skill-arastirma.md:20-87` | Kaynak desen: mattpocock/skills `grilling` motoru (MIT), tam metin 51-71; 5 mekanik kural 77-81; grill-me / grilling / grill-with-docs / batch-grill-me ailesi tablosu 42-47. |
| `raporlar/2026-07/2026-07-21-grill-me-skill-arastirma.md:99-106` | V55 pasif-okuma varsayılanı (2026-07-15) ile ilişki: grill, üstüne binen isteğe bağlı doğrulama geçişi; [S]/[O]/[T] zorluk kadranı, "bulanık blok" mevcut kavram. |
| `raporlar/2026-07/2026-07-21-grill-me-skill-arastirma.md:118-149` | Hazır Türkçe şablon (sınayıcı rolü, kaynak yapıştırma zorunlu, tek soru, "kendi cümlenle anlat", kaynaktan birebir alıntıyla düzeltme, kanıtsız övgü yok, kapanış: GEÇTİ/BULANIK/Takip). |
| `raporlar/2026-07/2026-07-21-grill-me-skill-arastirma.md:174-177` | Tuzaklar: sycophancy riski (arXiv 2605.14604, ön baskı, K), kaynaksız halüsine düzeltme, testing effect. |
| `raporlar/2026-10-17-hazir-karsilik-denetimi.md:87` | sinav-grill ↔ Anthropic `grill-me` hazır karşılık satırı: "üstüne kur"; [S]/[O]/[T] haritası ve yalnız-Salih-tetiği yerel eklentidir. (Not: 07-21 raporu grill-me'nin Anthropic değil Pocock'a ait olduğunu belgeliyor, satır 26-31; denetim satırındaki "(Anthropic)" ifadesi ile çelişir, bkz. aşağı "Açık nokta".) |
| `raporlar/2026-10-17-skill-revizyon-denetimi.md:7` | sinav-grill: bulgu yok. |
| `raporlar/2026-10-16-md-lean-envanter.md:151` | sinav-grill "yalnız-Salih-tetik yasağı" Kanon.Yasaklar'a kesim adayı (küçük iş). |
| `raporlar/2026-07/2026-07-21-cc-yan-oturum-devri.md:33-36` | K3 karar kaydı: V55'i bozma, isteğe bağlı grilling geçişi + K-016 ile natif skill. Karar: yalnız Salih tetiği. |
| `kuyruk/skill-fikir-kutusu.md:15` | S-I satırı: "YALNIZ Salih beyanı: sınav / grill, varsayılana gömülmez (V55 korunur, K3 hükmü 07-21)"; ÜRETİLDİ 08-14. |
| `.claude/skills/ogren/SKILL.md:48` | `ogren` akışı: `sinav-grill` tek cümleyle önerilir; Salih "sınav" demeden koşulmaz. |
| `raporlar/2026-09/2026-09-09-ai-ile-ogrenme-transkript-analizi.md:29` | sinav-grill yalnız Salih tetiğiyle, ders sonunda; grill ders-içi adım-quiz'i değil (KISMİ eşleşme). |
| `kuyruk/masa-gundemi-8-2026-09-03.md:70`, `kuyruk/masa-gundemi-9-2026-09-08.md:64` | Öğrenme md serisi önerisi: her bölüm sonunda sınav-grill tetiği. |
| `raporlar/2026-08/2026-08-15-skill-semasi-test-turu.md:18` | Skill şeması testi: sinav-grill GEÇTİ, kullanıcı-yalnız tetik. |
| `raporlar/2026-08/2026-08-30-ib07-description-eval.md:45` | description-eval: sinav-grill 3 test, 1.00 / 1.00. |
| `raporlar/2026-07/2026-07-26-tech-stack-atlas.md:277` | Hukuk vaka/Sokratik yöntem "kanıtlı öğretim modeli" varsayımı **desteklenmiyor**: etkililik araştırması ağırlıkla işletme alanında, yöntem gözden düşmüş; hukuk muhakeme biçimi olarak alınabilir, öğretim modeli olarak alınamaz. (Aynı hüküm: `raporlar/2026-07/2026-07-26-SOZEL-tech-stack.md:161`, §5.3-19, ikincil kaynak.) |
| `cc/rapor/2026-07/rapor-2026-07-29-2.md:254` | tech-stack §5.3-19 hükmü K47 (ülke damgası) kapsamında DEĞİL; pedagoji hükmü. |
| `cc/rapor/2026-07/rapor-2026-07-30-12.md:219` | "S13: Sokratik kol 1. oturumda kaybetti, 3. oturumda kazandı": yeni üslup ilk oturumlarda düşük çıkar, kesişme noktası vardır; ölçüm kesişmeye kadar sürmeli. (S13 kaynağı bu dosyada değil, başka dosyadaki ölçüm; doğrulanmadı.) |
| `kaynak-kodu/README.md:21`, `.claude/skills/README.md:22` | Skill envanteri: sinav-grill T-Ü üretici, "öğrenme: Salih tetikli sınav". |
| `.claude/agents/` | Yalnız iki ajan dosyası: `research-agent.md` (adı `atlas`) ve `hakem.md`. Sokrates/sınav ajanı **yok**. |

**Açık nokta:** (1) Depoda "Sokratik" bir **ajan** yok; yalnız skill. (2) `hazir-karsilik-denetimi.md:87` ile `grill-me-skill-arastirma.md:26-31` kaynak sahipliğinde (Anthropic/Pocock) ayrışıyor; 07-21 raporu birincil kaynak çekimi (D) olduğundan güvenilir olan odur [?: denetim satırı yanlış kısaltma olabilir, doğrulanmadı].

## (b) sinav-grill tam mekanizma

**Frontmatter:** `name: sinav-grill`; description tek paragraf (tetik + yasaklar içinde); başka alan yok (`SKILL.md:1-4`).

**Tetik kuralı:** yalnız Salih beyanı: "sınav", "sınava çek", "grill", "sorguya çek" (`SKILL.md:3`). Model kendi inisiyatifiyle **asla** tetiklemez; "bunu sınayayım mı?" diye önermek bile V55 ihlali sayılır (`:22`). Kapsam dar tutulur (`:11`).

**Adımlar (`:10-19`):**
1. Kapsamı al (plan / karar / öğrenilen konu / yazdığı kod); "her şeyi sına" koşulmaz.
2. Sorgulama döngüsü: tek seferde tek soru, cevabı bekle · karar ağacını dal dal in, bağımlılıkları tek tek çöz · her soruda önerilen cevabını ver · olguyu sorma (dosyadan/ortamdan bul), yalnız Salih'in kararları ve anlayışı sorulur · sorular sertleşir ama içerik hakkında kalır, kişisel/psikolojik yorum yok (m.7/m.23).
3. Anlama haritası: her alt-konu etiketi **[S]ağlam** (kendi cümleleriyle türetebildi) · **[O]rta** (tarif etti, türetemedi) · **[T]emelsiz** (ezber/boşluk). Ek çıktı: **bulanık-blok listesi** (cevaplanamayan/çelişen noktalar) + tekrar-kuyruğu önerisi ("yanlışı kuyruğa at, 2-3 gün sonra tekrar").
4. Ortak-anlayış kapısı: Salih "tamam, anlaştık" demeden eyleme geçilmez; sınav sonucu otomatik iş doğurmaz.

**Gotchas / yasaklar (`:21-26`):** kendiliğinden tetiklenme yasağı · yumuşatma yok (önerilen cevap sorudan sonra, Salih cevapladıktan sonra kıyas için açılabilir) · derece şişirmesi yok ([S] "türetebildi" kanıtı ister, doğru kelime yetmez) · kapsam sürünmesi yok (yeni konu = yeni tur notu) · skill kaydetme/commit yapmaz, harita rapor olarak döner, kayıt seans akışının işidir.

**Köken:** Pocock `grilling` (MIT), V25 gereği kurulmadı, yeniden yazıldı (`:6-8`). Pocock'ta olup yerelde olmayan: periyodik özet duraklaması, kapanış özeti formatı (GEÇTİ/BULANIK/Takip) ve "kaynak yapıştırma zorunlu" kuralı yalnız 07-21 raporunun şablonunda var (`:118-149`), skill'e girmedi.

## (c) Mevcut ajan dosyası biçimi

Konum: `jarvis/.claude/agents/<ad>.md`. Biçim: YAML frontmatter + Türkçe gövde.

`hakem.md:1-9` alanları: `name` · `description` (uzun; "Kullan; ..." ve "Kullanma; ..." cümleleri, Karar numaraları, çağrı koşulu) · `color: red` · `tools: Read, Grep, Glob, WebFetch, WebSearch` (salt-okur) · `model: sonnet` · `memory: project` · `maxTurns: 60`.

`research-agent.md:1-8` (adı atlas): `name` · `description` (örnekli, `<example>` blokları) · `color: blue` · `tools: Read, Write, Grep, Glob, Bash, WebFetch, WebSearch, Task, mcp__context7__*` · `context7: true` · `model: sonnet`.

Gövde iskeleti (hakem): `# AJAN: <ad> (...) — vX.Y, tarih (Karar/İB atıfları)` → Model ve eskalasyon → Amaç → Kimlik sınırı → Girdi sözleşmesi → Usul (sıralı) → Yasaklar → Çıktı iskeleti → sonda HTML yorumu sürüm/ölçüm borcu/ad eşitliği (`hakem.md:11-48`). Ajan metodolojisi gereği: işçi promptu = tek uzmanlık + araç kısıtı + "sadece bunu yap" sınırı + çıktı bütçesi; tek cümlelik `çağrı-koşulu` (Claude Code `description` deseni) lider tarafından okunur (`core/ajan-metodolojisi.md:35`).

## (d) Sokrates ajanının uyması gereken kanon kuralları

**Üslup**
- Kök md.11 / tüzük m.7: övgü yok, çıplak veri, gözlem işin kendi ölçütüyle (`core/tuzuk-v0.md:19`). Vurgu kalın; büyük harf yalnız kısaltma ya da backtick jeton; Salih'e düz yazıda ve commit/PR metninde em-dash yok (kök md.6, md.11; user CLAUDE.md).
- Üslup m.6: gerekçeli uyarı, kör-onay yok (`tuzuk-v0.md:18`). Boş geçiş ("harika!") yok (07-21 şablonu kural 7).
- Seçenek sunumu: ne demek · ne yaparım · artı · eksi · öneri+gerekçe, öneri ilk sırada. Cevap başına az konu. Rakam kaynaklı, kestirim `[?]`, zaman-bağımlı iddia AS-OF damgalı (kök md.8).

**Yasaklar**
- m.23: günlük-özüt, ruh hâli takibi ve psikolog rolü yasak; denetçi ajan psikolog rolüne giremez (`core/tuzuk-v0-m17.md:7`).
- m.33: Salih'e ayıklık/HI sorgusu yok, üsteleme/tekrar-sorma yok (`core/tuzuk-v0-m32.md:2`; gövde Lean `Kanon`'da).
- Sorgu içerik hakkındadır, Salih'in durumu hakkında değil (`sinav-grill/SKILL.md:3,17`).
- Model-inisiyatifli tetik yok; yalnız Salih beyanı (K3 hükmü, V55).

**Tek-yazar (kök md.14, Karar 103 M3)**
- Her dosyanın yazarı dizin sahibi ajan; başka ajan dizinine yazım yok, istek devir birimiyle (`cc/gelen/`) gider.
- Ajan kural yazamaz, kural adayı sunar (kök md.2, m.42 d). Ajan kanonu (`<ajan>/AGENTS.md`) Jarvis yazar, Salih imzalar. Katman-1 (kanon, rol, yeni ajan doğumu) yalnız Salih imzası.
- Commit: pathspec-only `git add <yol>`, İngilizce mesaj, önek `[icra]`; push yalnız Salih beyanıyla (kök md.5, md.14).

**İzolasyon (kök md.1, md.15, md.16)**
- Ajan yalnız kendi kanonunu (`<ajan>/AGENTS.md` + `<ajan>/core/`) ve kök dosyayı okur; başka ajanın dizini okunmaz. `ogrenme/` Salih'indir, ajanlara kapalı. `gunluk/` kapalı.
- Salih'e doğrudan yazmaz; dönüş `cc/giden/` dosyası ile Jarvis üzerinden; emir `cc/gelen/` + oturum mesajı.
- Alt-ajan okuma kilidi (İB-83): kapsül/pano/defter/kütükler/transkript okunamaz (bu koşumda `senaryo-defteri.md` reddedildi).
- Alan ajanı doğumu: `jarvis/tools/alan-ajani-dogur.py`; ad ölçütü `jarvis/lean/Kanon/AjanAdi.lean`; doğum = charter §0b doğum belgesi + bakım-maliyeti satırı (kök md.1, Karar 104 M5). Alan içinde perspektif ayrımı varsayılan yalnız hakem; "sorgulayıcı" ayrı ajan olarak ayrılacaksa kanıt gerekir: bağlam sızıntısı ∨ yapan≠ölçen ihlali (Karar 104 M6).

**Mevcut kanonla gerilim noktaları (m.16 çelişki kapısı için aday)**
- sinav-grill "yalnız Salih tetiği" ↔ ajan olarak çağrılabilirlik: ajan description'ı model-tetiklemeyi açar (Agent aracı description'a bakar). Çözüm adayı: description'a "yalnız Salih beyanıyla çağrılır" + çağıran emrinde Salih beyanı alıntısı zorunlu.
- "Skill kaydetme/commit yapmaz" ↔ ajanın harita çıktısı yazması: hakem deseni (salt-okur, tam metin döndür, çağıran kaydeder) uyumlu.
- Karar 106 / `ajan-metodolojisi.md §6b`: alan ajanı varsayılan Sonnet 5 medium; eskalasyon kayıtlı.
- 07-30-12 satır 219 (S13) bulgusu: Sokratik kolun ilk oturumda geride kalması beklenir; ölçüm tek oturumla yargılanmaz.
- hukuk vaka yöntemi hükmü (tech-stack §5.3-19): Sokratik yöntem "kanıtlı öğretim modeli" olarak savunulamaz; Sokrates ajanı gerekçesini öğretim etkililiği iddiasına değil, anlama ölçümü (ertelenmiş boşluk, V55) işlevine dayandırmalı.
