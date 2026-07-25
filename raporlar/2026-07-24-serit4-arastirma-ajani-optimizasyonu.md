# Şerit 4 — Şirkete En Optimize Araştırma Ajanı Nasıl Kurulur (Atlas Raporu, 2026-07-24)

> **Mod:** yan-oturum (m.41) — öneri üretir, kanon KİLİTLEMEZ. `core/` · `CLAUDE.md` · `.claude/` yazılmadı.
> **Soru (Salih, 07-24):** "İyi bir araştırma ajanı nasıl oluşturulur; şirkete en optimize araştırma ajanını nasıl kurarız?"
> **Şerit:** 3 aile açıldı, **üçü de rapor yazdı**. Ek olarak iki alt-ajan bağımsız rapor döndürdü (hakem güvenilirliği · kaskad hatası).
> **Kaynak:** `scratchpad/S4-A{2,3}-seritA.md` + iki alt-ajan dönüşü
> **⚠ İşlenmemiş malzeme:** `scratchpad/S4-A1-seritA.md` (yerleşik araştırma-ajanı tasarımları, 35 KB) diskte duruyor ama **bu rapora işlenmedi** — özeti dönmeden oturum kesildi, sonradan diskte bulundu. Literatür tarafı bu ölçüde eksik; ana-sıra ingest etmeli.

## 0. Bu raporun özel konumu

Bu şerit, **bugünkü koşumun kendisini veri olarak kullanıyor.** 20+ ajanlık gerçek bir çalıştırma yapıldı, tavanlara çarpıldı, bütçeler tüketildi, bir ajan bir başkasının teşhisini çürüttü. Yani buradaki bulguların önemli kısmı literatür değil, **yerinde ölçüm** — ve kanıt hiyerarşisinde bu en üst basamak.

**Kanıt kısıtı:** Egress politikası çoğu hostu 403'ledi; oturum ortasında **WebSearch bütçesi de tükendi (200/200)**. Açık kalan tek verimli kanal `raw.githubusercontent.com` oldu. Aşağıdaki [K] etiketlerin çoğu WebSearch'ün özet katmanından geliyor — yani bir LLM'in okuduğu sayfayı özetlemesi. Bu raporun kendisi, araştırdığı sorunun bir örneğidir.

## 1. BLUF — optimize araştırma ajanının şekli

Kanıt üç şeyde yakınsıyor, ve üçü de bizim mevcut tasarımımızın *bir kısmını* doğrulayıp *bir kısmını* yıkıyor:

1. **Fan-out doğru işte doğru.** Salt-okunur, genişlik-öncelikli araştırmada çok-ajan tek-ajanı geçiyor. Cognition'ın revize konumu bunu net söylüyor: çok-ajan **yazma tek şeritte kaldığında** ve ek ajanlar **eylem değil zekâ kattığında** çalışıyor. Atlas fan-out'umuz tam bu sınıfta.
2. **Ajanın kendisi şişman, ve şişmanlığı bedava değil.** 468 satırlık tanım her spawn'da önbelleksiz ödeniyor.
3. **Asıl zayıf halka ajan değil, hakemlik.** Üretici ve hakem aynı model ailesindeyken öz-tercih yanlılığı devreye giriyor; uzunluk yanlılığı bizim uzun raporlarımızı doğrudan vuruyor.

## 2. Yerleşik kanıt: çok-ajanlı araştırma ne zaman kazanır

| Bulgu | Etiket |
|---|---|
| Anthropic'in kendi araştırma sistemi (Opus lider + Sonnet işçi) tek-ajanı **%90,2** geçti; bedeli **~15× token**; performans varyansının **%80'ini** token harcaması açıklıyor | [K] (birincil 403) |
| Agent teams, standart oturuma göre **~7×** token; resmi hüküm: "araştırma, inceleme ve yeni özellik işinde fazla token genelde değer; rutin işte tek oturum daha ucuz" | **[D]** |
| **Cognition revizyonu (Nisan 2026):** "Don't build multi-agents" geri çekilmedi, daraltıldı — çalışan desen **tek-yazar (single writer)**; ek ajanlar zekâ katmalı, eylem değil. Çalıştığı söylenen üç desen: Code-Review-Loop · Smart Friend · map-reduce-and-manage | [K] |
| **MAST taksonomisi:** MAS hatalarının ~%79'u spesifikasyon + koordinasyondan (Specification & System Design %41,8 · Inter-Agent Misalignment %36,9 · Verification %21,3); ajan zekâsından değil | [D] repo / [K] sayılar |
| **Çok-turlu kayıp:** modeller çok-turlu konuşmada tek-turluya göre ortalama **%39** düşüyor; "yanlış dönüşten sonra toparlayamıyor". Parçaları birleştirip tek turda vermek temel çizginin %95,1'ini koruyor → **kayıp bilgi kaybından değil, etkileşim biçiminden** | **[D]** |
| **τ-bench pass^k çürümesi:** aynı görev tekrar denendiğinde başarı üstel düşüyor (0,460→0,225) | **[D]** |
| **Kaskad hatası evrensel DEĞİL:** doğrusal devirde halüsinasyon *sönümlenebiliyor* (amplifikasyon faktörü 0,64) ama olgusal doğruluk aşınıyor (0,789→0,769); buna karşılık **konsensüs/iterasyon topolojilerinde** tek hata tohumu sistemik yanlış konsensüse katılaşıyor. **Fark topolojide: doğrusal devir ≠ karşılıklı onaylama döngüsü.** | [K] |
| **Self-conditioning:** model kendi geçmiş hatalarını bağlamında görürse sonraki adımlarda daha çok hata yapıyor; model büyütmek çözmüyor | [K] |

### 2.1 Bunun m.40b'ye tercümesi

- **İyi haber:** m.40b doğrusal devir tarafında — tez ajanları birbirini görmüyor, antitez iddia-only alıyor, hakem ayrı. Karşılıklı onaylama döngüsü *değil*. Kaskad literatürünün tehlikeli saydığı topoloji bizde yok.
- **Kötü haber:** MAST'ın "%79 spesifikasyon + koordinasyon" bulgusu bizim en zayıf noktamıza denk geliyor — bugünkü koşumda ajanların **görev emirlerini ben yazdım** ve ikisi (T3-A1 ↔ T3-A2) doğrudan çelişen sonuçlara vardı. Çelişkinin kaynağı ajan zekâsı değil, benim aile tanımlarımdaki örtüşmeydi.
- **Uyarı:** bu oturum çok uzun sürdü. Self-conditioning bulgusu, uzun oturumun sonundaki yargıların başındakinden daha güvenilir olmadığını söylüyor.

## 3. ★ m.40b'nin üç zayıf halkası (bu koşumda görüldü)

### 3.1 Hakem ile üretici aynı model ailesinde

**Bulgu:** Öz-tercih (self-preference) yanlılığı ölçülmüş: bir model kendi ürettiği metni tanıyabiliyor (GPT-4 fine-tuning'siz %73,5) ve tanıma yeteneği ile kendi çıktısını kayırma şiddeti **lineer korele** [K]. Alt-ajanın kendi çıkardığı sonuç aynen:

> *"Claude üretimi raporları Claude hakemle puanlamak tam da riskli konfigürasyondur — hakem ile üreticinin model ailesi ayrıştırılmalı."*

Bizim zincirde tez, antitez **ve** hakem hepsi Claude. Bu, protokolün adı konmamış bir zayıflığı.

**Çözüm yönü (karar değil):** hakem katmanını farklı model ailesine taşımak; ya da m.42(f)'nin kendi ilkesini uygulamak — *"çeşitlilik yapıdan alınır, sampling gürültüsünden değil"* — yani hakemliği tek modele bırakmayıp yapısal olarak farklı roller/kısıtlarla desteklemek.

### 3.2 Uzunluk yanlılığı bizim rapor biçimimizi vuruyor

**Bulgu [K, iki bağımsız aramada tutarlı]:** "tekrarlayan liste" saldırısında GPT-3.5 ve Claude-v1 **~%91** kanma oranı gösteriyor — yani şişirilmiş, listeli, uzun metin hakemi yanıltıyor. Ayrıca "tutarlılık ≠ geçerlilik": bir hakem kendi içinde >0,95 tekrarlanabilir olup aynı anda sistematik yanlı olabiliyor [K].

**Bizim raporlarımız uzun ve listeli.** Hakemlik uzunluğu kalite sanabilir.

**Çözüm yönü:** hakeme giden malzemeyi iddia-listesine indirgemek (zaten yapıyoruz — antitez iddia-only alıyor) ve **hakemliğe de aynı disiplini uygulamak**: hakem tam raporu değil, maskeli iddia+kanıt çiftlerini görsün.

### 3.3 Örneklem-denetimi bu yüzeyde yapılamıyor

V26 "ajan başına ≥1 rastgele kaynak iddiası seç, kaynağa in, doğrula" diyor. **Egress politikası bunu yapısal olarak imkânsız kıldı** — Anthropic dokümanları ve GitHub ham dosyaları dışında hiçbir kaynağa inilemiyor.

Bugün denetim yapabildiğim tek yer yerel ölçümlerdi (repo dosyaları, git tarihi, `claude --version`, `env`) — ve orada **gerçek denetim** oldu, üstelik bir kez ajanı haklı çıkardı (wiki index %67 kaybı), bir kez de kendi hipotezimi çürüttü (iç içe ajan çıkarımı).

**Kural sonucu:** V26 ya yüzeye koşullanmalı ("kaynağa inilebiliyorsa kaynak denetimi, inilemiyorsa tutarlılık denetimi — ve tabloda ayrı etiketlensin") ya da araştırma yüzeyinin ağ politikası değişmeli. **Bu ikisinden birini seçmek Katman-1 kararı.**

## 4. Maliyet: bugünkü koşumun ölçülen gerçeği

| Bulgu | Etiket |
|---|---|
| `CLAUDE_EFFORT=xhigh` set **ve** atlas tanımında `effort:` alanı yok → bugünkü 20 ajanın hepsi **Opus 5 + xhigh** koştu. Bu bir karar değil, önceki oturumdan miras | **[D]** yerel `env` |
| Alt-ajan **kendi önbelleğini kurar, ilk çağrısında hiç isabet almaz** → 468 satır tanım (~4.000 token) + CLAUDE.md her spawn'da önbelleksiz ödenir; 20 spawn ≈ **110.000 token salt önsöz** | [D] mekanizma / [?] rakam |
| Dört deterministik tavan var, hepsi *yükseltilebilir ama kapatılamaz*: eşzamanlı alt-ajan (20) · oturum başı alt-ajan (200) · spawn derinliği · oturum başı WebSearch (200). **Bugün üçüne de çarpıldı** | **[D]** + yerinde gözlem |
| `MAX_THINKING_TOKENS` bu ortamda **ölü** — Opus 5 adaptif akıl yürütür; gerçek kol `effort` | **[D]** |
| Resmi model kademesi: teammate'ler için Sonnet · karmaşık mimari için Opus · basit alt-ajan için haiku. **Ama `CLAUDE_CODE_SUBAGENT_MODEL` env'i frontmatter dahil her şeyi ezer** → V59 ajan-başına frontmatter ile kurulmalı, env ile değil | **[D]** |

### 4.1 ★ V59 sandığımızdan zor

Resmi efor tablosu **iki yönlü** tavsiye veriyor: `low` için *"basit görevler… örneğin alt-ajanlar"*, `xhigh` için *"ayrıntılı web araması için önerilen başlangıç"*. **Bizim atlas tam olarak ayrıntılı-web-araması ajanı.**

Üstüne kritik bir mekanizma: **düşük efor yalnız düşünmeyi değil araç çağrı sayısını da kısıyor.** Yani bir araştırma ajanında kalite kaybı önce *kapsamda* görünür — daha az kaynak taranır — akıl yürütmede değil. Bu, araştırma için en kötü kayıp türü, çünkü fark edilmesi zor: rapor akıllı görünür, sadece daha az şey görmüştür.

**Sonuç:** V59 "işçilere ucuz model" biçiminde uygulanamaz. Uygulanabilir biçimi: **rol ayrımı** — tarama/çekme işi ucuz, sentez/hakemlik pahalı. Ve bunun kanıtı Anthropic'in kendi deseninde var (Opus lider + Sonnet işçi, %90,2 kazanç).

## 5. Atlas tanımı için somut değişiklik listesi

**SİL — frontmatter**
1. `Task` aracı — ölü giriş
2. `mcp__context7__*` araçları — sunucu bağlı değil, oturumda hiçbir araca eşleşmiyor
3. `context7: true` — desteklenen bir frontmatter alanı **değil**, tamamen etkisiz

**SİL — gövde (≈300 satır, %64 kısalma)**
4. `ACADEMIC PAPER RESEARCH MODE` — JARVIS'te kullanılmıyor; gerekirse `skills:` ile talep üzerine yüklenir
5. Context7 epistemoloji bölümleri — ölü ayak, ajanı boş tura sokuyor
6. `WAVE PROTOCOL` — `atlas-kosum` skill'iyle çakışan ikinci ayrıştırma protokolü. **Ayrıştırma Carvis'in işi, işçinin değil**
7. `RESEARCH METHODOLOGY` Faz 1-4 — Opus 5 rehberinin kaldırılmasını istediği doğrulama iskelesi
8. `Phase 5` + `OUTPUT_FORMAT` şablonları — `docs/research/` JARVIS'te **yok**; çıktı şekli görev emrinde yaşar
9. `EPISTEMOLOGICAL SELF-AWARENESS` — "I have access to Context7" **fiilen yanlış**; ajana kendi yeteneği hakkında yanlış bilgi veriyor
10. `TRIGGERS` + `CAPABILITIES` — delegasyonu `description` alanı yönetir

**EKLE — frontmatter**
11. `effort:` — tarama hattı yüksek, çekme/doğrulama düşük. **Tek satırla en büyük tasarruf kaldıracı**
12. `maxTurns:` — ajan-başına deterministik döngü tavanı
13. `SendMessage` — koşum-ortası düzeltme bunsuz çalışmıyor

**EKLE — gövde**
14. Kapsam kilidi (istenen kapsamı aşma yasağı)
15. Rapor uzunluğu kalibrasyonu — **hem token maliyeti hem hakem uzunluk-yanlılığı için**
16. Ucuz-önce arama sırası: **toplu indir + yerel grep**, sayfa-sayfa WebFetch değil. *(Bu koşumun yerel dersi: bir ajanın [D] bulgularının ~%80'i tek bir 6,3 MB'lık indirmeden geldi.)*

**DEĞİŞTİR**
17. `model: opus` alias'ı — Salih bu kararı verdiği gün başka bir modele işaret ediyordu, bugün Opus 5'e çözülüyor. **Alias = habersiz model göçü.** Ya tam kimliğe sabitle ya da bilinçli alias tercihini deftere damgala
18. Çıktı disiplini bloğunu **dosyanın sonuna** taşı — uzun sistem promptu için resmi azaltıcı
19. **Delegasyon kotasını atlas'a değil Carvis'e yaz** — atlas zaten spawn edemiyor; kotayı ihlal eden orkestratör

**JARVIS tarafı (Katman-1 / Salih kararı — `.claude/` yapısal kilitli)**
20. `settings.json` `env` bloğuna deterministik tavanlar (eşzamanlı alt-ajan, oturum başı alt-ajan, spawn derinliği, WebSearch)
21. `SubagentStop` hook'u → ajan tipi + bitiş zamanı `cc/defter.md`'ye tek satır: **sıfır token maliyetiyle kalıcı maliyet defteri**
22. V59 eval'i: aynı görev emrini bir kez yüksek, bir kez çok-yüksek eforla koş, `/usage` alt-ajan kırılımını karşılaştır. **Anthropic sayı vermediği için bu tek deney V59'un gerçek dayanağı olur**

## 6. ★ En büyük bulgu: araştırma kapasitesinin tavanı ajan değil, ağ politikası

En iyi ajan tasarımı bile erişemediği kaynağı doğrulayamaz. Bugün:

- Şerit 1 (Anthropic dokümanları) **36 [D]** üretti.
- Şerit 2 Aile 1 (dış web) **tek bir [D] üretemedi.**
- Fark ajanda değil, **izin listesinde.**

Ve ajanlar bu kısıtı aşmak için üç teknik geliştirdi — üçü de kaydedilmeye değer:
1. **Kaynak-dosya ikamesi:** bloke bir doküman sayfasının kaynak `.md`'sini resmi GitHub reposundan indir.
2. **Ham veri inişi:** benchmark leaderboard'larının CSV'lerine doğrudan in — ikincil aktarım yerine sayının kendisi.
3. **Birinci-el ölçüme dönüş:** dış kaynak yoksa kendi repona in. Bu, kanıt hiyerarşisinde *daha yukarı* çıkmaktır — ve bugünün en iyi iki bulgusu (wiki index %67 kaybı, efor mirası) böyle geldi.

**Bu üçü atlas tanımına "arama sırası" olarak yazılmalı.**

## 7. Öneri — üç katmanlı araştırma ajanı

Kanıtın işaret ettiği yapı, tek bir "atlas" değil **rol ayrımı**:

| Katman | İş | Model/efor | Gerekçe |
|---|---|---|---|
| **Toplayıcı** | ham kaynak indirme, grep, ölçüm | ucuz / düşük efor | Deterministik iş; kalite kaybı riski düşük |
| **Tez/antitez** | okuma, iddia çıkarma, çürütme denemesi | orta-yüksek | Düşük efor kapsamı kısar — araştırmada en kötü kayıp |
| **Hakem** | maskeli kıyas, hayatta-kalma hükmü | **farklı model ailesi** (öz-tercih freni) | §3.1 |

Ve üç kural: **yazma tek şeritte** (Cognition revizyonu) · **hakem iddia görsün, rapor görmesin** (uzunluk yanlılığı) · **her koşumda maliyet deftere** (SubagentStop hook).

## 8. Cevaplanmamış sorular (m.41)

1. Hakem katmanı için farklı model ailesi erişilebilir mi? Değilse öz-tercih yanlılığı nasıl frenlenir?
2. V26 yüzeye koşullanacak mı, yoksa ağ politikası mı değişecek? (Katman-1)
3. Bugünkü koşumun gerçek token maliyeti kaç? `/usage` alınmadı — ölçülmeden V59 kararı verilemez.
4. Alt-ajanların açtığı çocuk işlerin mekanizması ne? Gözlemle sabit, mekanizma [X].
5. S4-A1 (yerleşik araştırma-ajanı tasarımları) raporu **diskte ama işlenmedi** — `scratchpad/S4-A1-seritA.md`. Bu raporun literatür tarafı o ölçüde eksik; ingest edilince §2 ve §7 gözden geçirilmeli.

---

*Yan-oturum çıktısı. Kanon kilitlenmedi. Karar ana-sırada (m.41).*
