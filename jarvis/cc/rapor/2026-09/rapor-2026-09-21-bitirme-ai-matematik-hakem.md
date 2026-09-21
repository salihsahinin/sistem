`[tip: rapor | kaynak: hakem-ajani (Opus, eskalasyon a+b) | tarih: 2026-09-21 | hedef: cc/rapor/2026-09 | sema: v2 | koken: jarvis/hakem-v0.1/claude-opus-5/2026-09-21 | kaydeden: Jarvis, aynen]`

# Maskeli hakem raporu · "Matematik mühendisliği lisans bitirme tezi için AI × matematik araştırması"

**Tarih (sistem):** 2026-09-21
**Rol:** Maskeli hakem (bağımsız, salt-okur; yapan ≠ ölçen, Karar 86 D3-i). Tez/antitez/sentez üretilmedi.
**Model + effort:** Opus 5 (1M bağlam), yüksek effort. Eskalasyon tetiği emirde iki gerekçeyle verildi: (a) Salih beyanı, (b) V26'da `TUTMADI` ≥3 olan rapor sayısı. **Rakam düzeltmesi (m.39):** emir bu sayıyı 6/12 veriyor; üç V26 tablosundan sayım 5/12'dir (¬A 3 · ¬B 3 · tez-D 7 · tez-E 3 · tez-F 3). Eskalasyon (a) şıkkıyla zaten geçerli, bu düzeltme tetiği bozmuyor.
**Girdi:** 12 üretici rapor · 3 V26 sondaj tablosu, toplam 204 sondaj satırı (68 + 68 + 68). Toplam sonuç: `TUTTU` 158 · `TUTMADI` 25 · `URL YOK` 17 · `ERİŞİLEMEDİ` 4.
**Kendi doğrulaması:** bütçe **8/8 kullanıldı**, tamamı WebFetch, çekim tarihi 2026-09-21:
1. `claymath.org/millennium-problems/navier-stokes-equation/`
2. `claymath.org/news/navier-stokes-announcement/`
3. `terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/`
4. `stanfordtechreview.com/articles/openai-buckmaster-navier-stokes-lean-proofs`
5. `arxiv.org/abs/2608.16753`
6. `arxiv.org/abs/2607.07779`
7. `teorth.github.io/tao-web/ai-views.html`
8. `alphaxiv.org/abs/2609.navier-stokes`

---

## Usul beyanı

**Maskeleme.** Raporlar dosya adlarıyla geldi; hangi dosyanın tez hangisinin antitez olduğu tartıya **sokulmadı**. Her satır "iddia + kanıt gücü" olarak tartıldı, iddia kimliğiyle (A1, B13, C10, D2, E11, F6) ve URL ile izlenir. Üretici raporlardaki `ÇÜRÜTÜLEMEDİ`/`DARALDI`/`ÇÜRÜDÜ` hükümleri girdi sayıldı, hüküm sayılmadı; birkaç yerde aynı olguya iki rapor ters hüküm vermişti, karar kanıta bakılarak verildi.

**Maske ihlali (hükme sokulmadı, alıntılanır):**
- `rapor-2026-09-21-bitirme-tez-B-tao.md` §2a: "**Salih'in** 'üstel' formülasyonu doğrudan doğrulanamadı"; §2b: "**Salih'in** iddiasına en yakın bulgu"; §5: "**Salih'in** iki özel iddiası kısmen doğrulandı".
- `rapor-2026-09-21-bitirme-tez-C-ai-matematik-durum.md` satır 17: "X, **Salih'e sorulmalı** / ek doğrulama gerekir."
- Amaç sızıntısı (düşük etkili, yine de kayıt): `antitez-C` EK-SORU-2 "**bitirme tezi** için bu atıf düzeltilmeli"; `tez-D` §5 taksonomisi jüri beklentisi üzerinden yazılmış.
Bu cümlelerdeki "kimin neyi beklediği" bilgisi tartıya girmedi: "üstel" ve "çeviri aracı" iddiaları yalnız birincil kaynak bulunup bulunmadığına bakılarak `X` oldu.

**V26 tavanı.** `TUTMADI` ≥1 olan raporun bulguları en fazla **K**. Tabloların sonucuna göre bu tavan **12 raporun 10'una** uygulanır; muaf olan tek rapor ¬D'dir (0 `TUTMADI`). Ana tablosunda 0 `TUTMADI` çıkan tez-B de tavana girer, çünkü aynı denetim raporu ek bulgu olarak açıkça "`TUTMADI` · yazarlık atfı hatalı" yazmıştır. Sonuç: tablonun gövdesi zorunlu olarak K'dir; **D yalnız benim kendi çekimimle birincil kaynaktan birebir doğruladığım 8 noktadan gelir** ve bunlar aşağıda tek tek listelenmiştir.

**Etiket tanımı.** **D** = birincil kaynakta birebir ∧ güncel kuşak ∧ adversarial turda ayakta · **K** = doğrulandı ama tek-kaynaklı, yazar-taraflı, ikincil, eski kuşak ya da AS-OF eksik · **X** = çürüdü ya da dayanaksız. **Kova** ayrı eksendir: sağlam (koşulsuz ayakta) · daraldı (yalnız yazılı koşulda doğru) · düştü (`X`) · çelişkili (çatışma saklanmadı, üst-küme olarak işaretlendi).

**AS-OF kuralı (Karar 68 · Karar 102 (3)).** AS-OF ya da model sürümü olmayan iddia en fazla K. Bu koşumda iki yapısal AS-OF sorunu var: (i) `teorth.github.io/tao-web/ai-views.html` çok sayıda B, D ve F iddiasının tek dayanağı; kendi çekimimde bu sayfa künyesini "compiled and drafted by an AI assistant (Claude) from Terence Tao's public writing, talks, and interviews, then reviewed and corrected by him" ve "omission is editorial" diye veriyor, yani Tao-onaylı bir derlemedir, ham beyan değildir, tek başına D taşıyamaz; (ii) Eloundou vd. (2023-03) ve Anthropic Şubat-2025 rakamları eski kuşak ölçümlerdir, "o zaman böyle" notudur, 2026 tasarım girdisi değildir.

**Özetleyici bayrağı notu.** İki çekimde (2 ve 4) WebFetch'in özetleyici modeli sayfayı "kurgusal / var değil / gelecek tarihli" diye işaretlerken aynı cevapta sayfanın birebir alıntılarını ve tablo rakamlarını döndürdü. Bu bayrak kesim-sonrası içerikte üretilen bir araç gürültüsüdür, **çürütme sayılmadı**; karar dönen içeriğe ve çapraz tutarlılığa bakılarak verildi (çekim 2'nin içeriği çekim 1 ile tutarlıdır). Bu, 07-17 dersinin ayna hâlidir ve hafızaya yazıldı.

---

### V26 düzeltmeleri

Sondaj tablolarının `TUTMADI` satırları + kendi çekimimle kesinleşen düzeltmeler. Bu satırlar aşağıdaki iddia tablosunda `X` olarak geçer.

| # | Düzeltilen iddia | Kaynakta gerçekte ne var | Dayanak |
|---|---|---|---|
| 1 | arXiv 2608.16753 "Tao & Klowden" | Tek yazar **Terence Tao**; Klowden yok; gönderim 2026-08-17 | Kendi çekimim (5) + V26-1 ek bulgu (arXiv API) |
| 2 | Fields bildirisi "16 Eylül itibarıyla 7.200+ ek imzacı" | Birincilde yalnız "25 initial signatories"; ek sayım **yok**; raporun gösterdiği ikincilde de yok | Kendi çekimim (3) + V26-1 b10 + V26-3 b10 |
| 3 | arXiv 2607.07779 "kanıt açıklama / yorumlanabilirliği açık sorun sayıyor" | Özet bu konulardan **hiç bahsetmiyor**; sayılan boşluklar: datasets, relational structure, mathematical exploration, tool ecosystem, human-AI collaboration; 19 yazar, 2026-07-08 | Kendi çekimim (6) + V26-2 b15 notu |
| 4 | "Üç kaynak OpenAI'nin kapsamı için üç farklı şey söylüyor, çelişki çözülemez" | Çelişki büyük ölçüde yok: ilgili kaynak Buckmaster-Alpöge'yi **forced Euler**, OpenAI'nin Euler sonucunu **unforced** diye ayırıyor; OpenAI'ye atfedilen belge ise **forced Navier-Stokes** diyor. Yani iki ayrı OpenAI sonucu okuması tutarlıdır | Kendi çekimim (4) + (8) |
| 5 | "Stanford Tech Review denetimi" (kurumsal ağırlık iması) | Site kendi künyesinde "An independent publication. **Not affiliated with Stanford University**" diyor | Kendi çekimim (4) |
| 6 | "Scientific American: nearly 100 agents in roughly 50 hours" | Makalede bu rakamlar yok | V26-1 b12 |
| 7 | "the-decoder: OpenAI 10 Eylül'de Codex promptları açıklaması" | Makalede en geç 8 Eylül tarihli genel ret var, 10 Eylül/Codex ifadesi yok | V26-1 b14 |
| 8 | "IBM kaynağında 25 Fields Madalyalı" | IBM sayfasında "strip-mined" var, 25 sayısı yok (sayı başka kaynakta doğru) | V26-1 b11 |
| 9 | "Quanta: 88 saatin ardından 17 saatte formalizasyon" | "88 hours" var, 17 saat ayrıntısı yok | V26-1 b7 |
| 10 | "Mathstodon Ağustos 4-6, 2026, faz 2 adoption mekanizması" | Bu etiketleme `ai-views.html`'de yok | V26-1 b3 |
| 11 | "DeepSeek-Prover-V2 PutnamBench 47/658" | Kaynak **49/658** diyor | V26-2 b13 |
| 12 | "Goedel-Prover-V2 32B, rakiplerden 80× daha küçük" | "80X smaller" iddiası **8B** modele ait, 32B'ye değil | V26-2 b15 |
| 13 | "Aristotle 5/6 problemi çözdü" | Kaynağın özeti yalnız "gold-medal-equivalent performance" diyor, 5/6 yok | V26-2 b4 |
| 14 | "FrontierMath 338 soru / 70+ matematikçi" (epoch.ai/frontiermath'e atıfla) | O sayfada "several hundred" yazıyor; 338 yalnız kardeş sayfada | V26-2 b3 |
| 15 | "FrontierMath Tier-4 17/48" (ourworldindata'ya atıfla) | O sayfa "Tier 4 ... is **not included here**" diyor | V26-2 b4 |
| 16 | "Buzzard 2025 Oxford Strachey Lecture" | İddia verilen iki URL'nin ikisinde de yok | V26-2 a, b6 |
| 17 | "YTÜ kılavuzu 2024-05 tarihli" | PDF'in kendi meta-tarihi **2024-01** (dizin damgası karıştırılmış) | V26-2 b10 |
| 18 | "U-MATH/UGMathBench, ICLR 2025" | Gönderim geçmişinde ICLR referansı yok | V26-2 b14 |
| 19 | "Oxford Part C, matematik programının 4. yılı" | Sayfa yılı belirtmiyor | V26-3 b5 |
| 20 | "CMU honors thesis 2 dönem, 36 kredi birimi" ve "prospectus ≤3 sayfa" | İki rakam da verilen sayfada yok | V26-3 b11, b12 |
| 21 | "Microsoft: konuşmaların %40'ında hedef-eylem uyuşmazlığı" | Sayfada bu yüzde yok | V26-3 b8 |
| 22 | "Tao ICM konuşması 2026-07-24" | arXiv künyesi yalnız "ICM 2026'da verilen konuşmaya dayanıyor" diyor, gün yok | V26-3 b9 + kendi çekimim (5) |
| 23 | "Diğer sekiz kurumda örnek bulunamadı" | Parantezde 10 kurum sayılmış (iç tutarsızlık) | V26-3 c |
| 24 | "20 deneme, 17 başarılı, 3 başarısız" | Raporun kendi listesinde 4 madde `BAŞARISIZ` işaretli (16/4) | V26-3 b1 |
| 25 | "Wikipedia son düzenleme 19 Eylül 2026" | Sayfa 21 Eylül gösteriyor | V26-1 b5 |

**Tavandan muaf tutulan noktalar (kendi çekimimle birincil kaynaktan birebir, bu yüzden D):** Clay "Active" durumu ve ödül yokluğu · Clay 2026-09-11 duyurusunun metni · 25 imzacı ve bildiri tarihi · arXiv 2608.16753 tek yazarlığı · arXiv 2607.07779 içeriği · `ai-views.html` künyesi ve de Bruijn pasajı · OpenAI'ye atfedilen belgenin forced/u=0 kapsamı · aynı belgenin "f=0 hâlâ açık" beyanı.

---

## İddia tablosu

### Aile A: Navier-Stokes iddiası

| # | İddia | Kanıt | AS-OF | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|---|
| A1 | arXiv 2509.14185, yeni kararsız kendine-benzer tekillik aileleri **yalnız IPM + sınırlı-alan 3D Euler** için; sınırsız Euler ve Navier-Stokes özet metninde açık problem olarak anılıyor | arxiv.org/abs/2509.14185 + export.arxiv.org ham XML | 2025-09-17 | K | sağlam | İki rapor ve V26 iki kez doğruladı, ham API metni okundu; V26 tavanı nedeniyle K |
| A2 | DeepMind blogu Millennium Prize'ın çözüldüğünü **iddia etmiyor**; kurumlar Brown, NYU, Stanford | deepmind.google/blog/discovering-new-solutions… | 2025-09-18 | K | sağlam | Her iki raporda ve V26'da `TUTTU`; birincil blog metni |
| A3 | Buckmaster-Alpöge, 2026-09-07, **düzgün zorlamalı** sonlu-zaman patlaması: IPM, 2D Boussinesq, 3D Euler; Lean'de formalize | terrytao.wordpress.com/2026/09/07/… | 2026-09-07 | K | sağlam | Tao'nun kendi bloğu birincil; başlık denklem listesini ve "smooth forcing"i taşıyor |
| A4 | Tao bu çalışmanın Lean formalizasyonunu "doğruladı" | Aynı blog: "their work has **also been formalized** in Lean" + "I still need to work some more… to digest things" | 2026-09-07 | K | **daraldı** | Yalnız koşulda doğru: Tao formalizasyonun **var olduğunu bildiriyor**; kendisinin derleyip denetlediğine dair ifade yok, sindirmediğini yazıyor |
| A5 | OpenAI'ye atfedilen sonuç **forced** (düzgün, kompakt destekli dış kuvvet) 3D Navier-Stokes, **u=0** başlangıç verisi, sınırlı kinetik enerji | Kendi çekimim (8): alphaxiv.org/abs/2609.navier-stokes, "driven by a smooth and compactly supported external force", "the initial data is u=0" | 2026-09-21 çekim | **D** | sağlam | Belgeyi kendim açtım; kapsam ifadesi birebir |
| A6 | Aynı belgeye göre **zorlamasız (f=0) Millennium sorusu açık kalıyor** | Kendi çekimim (8): "the Millennium Problem also asks about the unforced scenario (f=0), which remains open" | 2026-09-21 çekim | **D** | sağlam | İddia setinin en taşıyıcı noktası: kaynağın kendisi geniş okumayı reddediyor |
| A7 | Clay Enstitüsü sayfası Navier-Stokes'u 2026-09-21 itibarıyla **"Active"** listeliyor, ödül verilmedi | Kendi çekimim (1) | 2026-09-21 | **D** | sağlam | Birincil kurum sayfası, durum etiketi birebir |
| A8 | Clay'in 2026-09-11 duyurusu "apparently been settled" diyor, **çözücüyü adlandırmıyor**, süreç "deliberately unhurried" | Kendi çekimim (2) | 2026-09-11 | **D** | sağlam | Bir rapor "tarihli resmî duyuru bulunamadı" demişti; duyuru vardır, ama ödül/isim içermez, yani A7 ile çelişmez |
| A9 | Lean depo sayımları: Buckmaster-Alpöge 1.684.580 satır / 68.179 teorem; OpenAI 616.274 satır / 35.731 teorem | Kendi çekimim (4), stanfordtechreview.com | 2026-09-08 | K | **daraldı** | Yalnız koşulda kullanılabilir: **tek bir bağımsız yayının kendi denetim tablosu**; site "Stanford ile ilişkisi yok" diyor, kurumsal denetim değil, başka kaynakta teyidi yok |
| A10 | "OpenAI'nin ne kanıtladığı üç kaynak arasında çözülemez biçimde çelişiyor" | Kendi çekimim (4) + (8): forced NS (belge) ve unforced Euler (yayın) **ayrı iki sonuç** | 2026-09-21 | **X** | düştü | Çelişki okuma hatasıdır: bir kaynak Euler'in zorlamasız hâlini OpenAI'ye, zorlamalı hâlini Buckmaster-Alpöge'ye atfediyor; "iki ayrı sonuç" okumasıyla kaynaklar uyumlu |
| A11 | Fefferman: "I was thrilled that the problem was solved"; kahramanlar Córdoba ve Martínez-Zoroa | quantamagazine.org/…20260908 | 2026-09-08 | K | sağlam | V26 `TUTTU`; iki bağımsız kaynakta (Quanta + İspanyolca basın) örtüşüyor |
| A12 | OpenAI koşumu ~10.000 özerk ajan, 88 saat | quantamagazine.org/…20260908; coindesk (2.7M mesaj, ~130B token) | 2026-09-08 | K | sağlam | V26 üç ayrı raporda `TUTTU`; birincil OpenAI metni 403 olduğu için ikincil kalıyor |
| A13 | "nearly 100 agents in roughly 50 hours" (Scientific American'a atıfla) | V26-1 b12: makalede yok | 2026-09-21 | **X** | düştü | Atıf kaynakta bulunamadı; A12 ile de çelişiyor |
| A14 | "26 Fields Madalyacısı açık mektup yayımladı" | V26 + kendi çekimim (3): birincil metin **25** initial signatories diyor | 2026-09-11 | **X** | düştü | Sayı yanlış; doğru hâli B10 satırında |
| A15 | Buckmaster, Bubeck'in kendisini tehdit ettiğini ve OpenAI'nin verisine izinsiz eriştiğini iddia etti | fortune.com, thenextweb.com, the-decoder.com | 2026-09-08 | K | **daraldı** | Yalnız koşulda doğru: tek taraflı anlatı, Bubeck reddediyor, tarafsız doğrulama yok; "izinsiz erişim" kısmı Buckmaster'ın kendi ifadesinde **soru**, suçlama değil ("I am not accusing anyone of anything") |
| A16 | "Millennium Prize'ın 26 yılında yalnız Poincaré çözüldü, bu ikincisi olacak" | URL yok (V26 `URL YOK`) | yok | **X** | düştü | Hiçbir açılan kaynakta birebir görülmedi; AS-OF de yok |
| A17 | "Wikipedia sayfası son düzenleme 19 Eylül 2026" | V26-1 b5: sayfa 21 Eylül gösteriyor | 2026-09-21 | **X** | düştü | Tarih tutmuyor; zaten ikincil kaynağın meta verisi, taşıyıcı değil |

### Aile B: Tao'nun Temmuz-Eylül 2026 açıklamaları

| # | İddia | Kanıt | AS-OF | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|---|
| B1 | ICM 2026 Philadelphia genel konuşması "Mathematics in the Age of AI" var | arxiv.org/abs/2608.16753 künyesi "Submitted to the Proceedings of the ICM 2026" (kendi çekimim 5) | 2026-08-17 | K | sağlam | Konuşmanın varlığı birincil künyeyle destekli |
| B2 | Konuşma tarihi **2026-07-24** | Kendi çekimim (5): künyede gün **yok**; tarih yalnız `ai-views.html` kronolojisi ve ikincil aktarımlarda | 2026-07-24 `[?]` | K | **daraldı** | Yalnız koşulda kullanılabilir: "ikincil kronolojiye göre"; birincil kaynakta gün doğrulanmadı |
| B3 | arXiv 2608.16753'ün tek yazarı Terence Tao, gönderim 2026-08-17 | Kendi çekimim (5) | 2026-08-17 | **D** | sağlam | Birincil künye birebir okundu |
| B4 | Makale "Tao & Klowden" ortak çalışmasıdır | Kendi çekimim (5): Klowden yazar değil | 2026-08-17 | **X** | düştü | Yazarlık atfı hatalı; Klowden ortaklığı 2026-03-29 tarihli ayrı bir yazıya ait |
| B5 | Üretim / doğrulama / sindirim üçlemesi; AI ilk ikisini sindirimin çok önüne taşıyor ("impedance mismatch") | Kendi çekimim (7) + arxiv.org/html/2608.16753v1 | 2026-08 | K | sağlam | İçerik birincil makale metninde ve Tao-onaylı derlemede örtüşüyor |
| B6 | `ai-views.html`, Tao'nun yazılarından **bir AI asistanı tarafından derlenip Tao tarafından gözden geçirilmiş** yaşayan bir özettir; "omission is editorial" | Kendi çekimim (7) | 2026-09-21 | **D** | sağlam | Bu sayfa B, D ve F ailelerinde onlarca iddianın tek dayanağı; künyesi onu ham beyan değil düzenlenmiş derleme yapar, tek başına D taşıyamaz |
| B7 | "We can have these 100,000-line proofs that we have to verify, but no one understands them" | quantumzeitgeist.com + simonsfoundation.org; arXiv tam metninde yok | 2026-08-31 | K | **daraldı** | Yalnız koşulda: iki ikincil yayının **konuşmadan** aktardığı alıntı; yazılı makalede geçmiyor, ham kayıt açılmadı |
| B8 | Tao: "We have to slow down. The pace is insane, and there's no reason to be this fast" | officechai.com + bir X repostu; video transkripti açılamadı; blogda ve IBM metninde yok | tarih yok | **X** | düştü | Birincil zincir hiç kapanmadı, konuşmanın tarihi ve yeri yok; AS-OF'suz alıntı hükme giremez (Karar 68) |
| B9 | Tao ilerlemeyi "üstel" diye niteledi | arXiv tam metin taraması: kelime yok; tek atıf doğrudan çekimde teyit edilemedi | 2026-09-21 | **X** | düştü | İki rapor bağımsız olarak aradı, ikisi de bulamadı; arama-özeti kaynaklı halüsinasyon şüphesi kayıtlı |
| B10 | 2026-09-11 "A Severe Misalignment of AI in Mathematics", **25** ilk imzacı, hepsi Fields madalyalısı, Tao dahil | Kendi çekimim (3): "25 initial signatories · all Fields Medallists" | 2026-09-11 | **D** | sağlam | Birincil blogdan birebir |
| B11 | "16 Eylül itibarıyla 7.200+ ek imzacı" | Kendi çekimim (3): birincilde yok; V26 ikincil kaynakta da bulamadı | 2026-09-16 | **X** | düştü | Ne birincilde ne gösterilen ikincilde var; iki ayrı raporda aynı rakam, ikisi de dayanaksız |
| B12 | 2026-09-17 Gowers konuk yazısı "Why I didn't sign the Fields medallists' letter", gowers ve terrytao bloglarında çapraz yayın | terrytao.wordpress.com/2026/09/17/… | 2026-09-17 | K | sağlam | V26 `TUTTU`; kayıtlı, birincil ve tezin karşı kutbunu belgeliyor |
| B13 | 2026-09-12 "After Math" yazısı **Tao'nun tezi değil**, De Toffoli ve Duede konuk yazısıdır | terrytao.wordpress.com/2026/09/12/after-math/ | 2026-09-12 | K | sağlam | Yazar ayrımı raporda açıkça doğrulanmış; "Tao dedi" okumasını engelliyor |
| B14 | 2026-07-27'den 09-09'a Mathstodon gönderilerinin içeriği | Yalnız 2026-09-08 gönderisi ham API ile açıldı; kalanlar `ai-views.html` kronolojisinden | 2026-07/09 | K | **daraldı** | Yalnız koşulda: "Tao-onaylı kronolojiye göre"; ham gönderi metinleri doğrulanmadı, V26 iki gönderide `ERİŞİLEMEDİ` verdi |
| B15 | Bu gönderiler "Ağustos 4-6, 2026, faz 2 adoption mekanizması" diye etiketlenir | V26-1 b3: `ai-views.html`'de böyle bir etiketleme yok | 2026-08 | **X** | düştü | İkincil kaynağın kendi çerçevelemesi, kaynakta karşılığı yok |
| B16 | First Proof, 2026-05-28, dört harness, 10 araştırma problemin 7'si yayın kalitesinde | aiweekly.co / digg.com aktarımı; bir raporun kaynak listesinde URL yok (V26 `URL YOK` ×2) | 2026-05-28 | K | **daraldı** | Yalnız koşulda: ICM slaytlarına atıfla iki ikincil aktarım; slayt PDF'i iki koşumda da metne çevrilemedi |
| B17 | 2026-09-15 "Fast math/slow math" yazısı Ben Antieau'nun konuk yazısıdır; ilgili cümle "Do not work faster than you can understand or effectively communicate" | terrytao.wordpress.com/2026/09/15/fast-math-slow-math/ | 2026-09-15 | K | sağlam | V26 `TUTTU`; B8'deki alıntıyla karıştırılmasını engellediği için ayrı satır |

### Aile C: AI × matematik güncel durum ve araçlar

| # | İddia | Kanıt | AS-OF | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|---|
| C1 | IMO 2025: Gemini Deep Think 6 sorudan 5'i, 35/42, 4,5 saat, uçtan uca doğal dil, IMO başkanı sertifikalı | deepmind.google/blog/advanced-version-of-gemini… | 2025-07-21 | K | sağlam | İki rapor + V26 iki kez `TUTTU` |
| C2 | OpenAI'nin 35/42 iddiası **2025-07-19**'da duyuruldu ve **3 eski IMO madalyalısı** tarafından değerlendirildi, IMO koordinatör rubriğiyle değil | simonwillison.net/2025/Jul/19/…; lesswrong.com/posts/ZkgaPopsBkQgeA2k8 | 2025-07-19 | K | sağlam | İki farklı kaynakta `TUTTU`; sertifikasyon farkı taşıyıcı bir ayrım |
| C3 | "OpenAI de aynı gün (2025-07-21) altın eşiğine ulaştı" | C2'deki kanıt tarihi 07-19 gösteriyor | 2025-07-21 | **X** | düştü | Tarih yanlış; V26 `URL YOK` ile zaten kaynaksızdı |
| C4 | IMO 2026 Şangay'da RedNote dots-note-3.0 42/42 aldığını **iddia etti** | scmp.com/tech/article/3361482 | 2026-07 | K | **daraldı** | Yalnız koşulda: SCMP'nin kendi kaynağı "a post on the model's website"; bağımsız IMO onayı sunulmuyor, "officially graded" ifadesi yalnız ikinci bir ikincil yayında |
| C5 | "IMO 2026'da dört AI mükemmel skor aldı" | Başlık düzeyinde, sayfa açılmadı (V26 `URL YOK`) | 2026-07 | **X** | düştü | Sayı hiçbir açılan kaynakta doğrulanmadı; raporun kendisi de X işaretlemiş |
| C6 | erdosproblems.com: 2026-08-03 itibarıyla 565 çözüldü, 652 açık | quantamagazine.org/why-the-legendary-erdos-problems…20260803 | 2026-08-03 | K | sağlam | İki rapor + V26 iki kez `TUTTU`, birebir aynı rakam |
| C7 | Bloom uyarısı: üretilen bazı AI makalelerini hiçbir insan okumadı, doğrulama açık sorun; bu, 2025-10'daki "GPT-5 var olan çözümleri buldu" olayından **ayrı** bir olaydır | sciencenews.org/article/ai-guardrails-erdos-math-problem | 2026-08 | K | sağlam | Doğrudan alıntı var; iki olayın ayrılması doğru yapılmış ve tez kapsamı için taşıyıcı bir risk notu |
| C8 | FrontierMath Erdős, 2026-09-01: 68 problem (652'nin ~%10'u), problem başına 300$ ve 72 saat; GPT-6 Astra resmî 2/68 (%3), diğer dört model %0, gayri-resmî toplam 5 | epoch.ai/latest/announcing-frontiermath-erdos | 2026-09-01 | K | sağlam | İki rapor + V26 üç kez `TUTTU`; resmî/gayri-resmî ayrımı iki raporda da korunmuş |
| C9 | Mathlib 288.718 teorem, 136.941 tanım, 772 katkıcı | leanprover-community.github.io/mathlib_stats.html | 2026-09-21 çekim | K | sağlam | İki rapor + V26 iki kez `TUTTU`; eski "210.000+" rakamları bayat, çelişki değil |
| C10 | Mathlib "iki milyon satırın üzerinde" biçimselleştirilmiş matematik | lean-lang.org/use-cases/mathlib/ | 2026 (sayfada tarih yok) | K | sağlam | V26 `TUTTU`; AS-OF eksik olduğu için tavan zaten K |
| C11 | PutnamBench 1.724 biçimselleştirme (Lean 4: 672, Isabelle: 640, Coq: 412), Apache-2.0 + Coq için MIT | github.com/trishullab/PutnamBench | 2026-09-21 çekim | K | sağlam | V26 iki kez `TUTTU`; arXiv'deki 1.692/640 sürüm farkıdır, çelişki değil |
| C12 | DeepSeek-Prover-V2-671B, MiniF2F-test %88,9 | arxiv.org/abs/2504.21801 | 2025-04 | K | sağlam | İki rapor + V26 iki kez `TUTTU` |
| C13 | Aynı modelin PutnamBench skoru 47/658 | V26-2 b13: kaynak **49/658** diyor | 2025-04 | **X** | düştü | Rakam yanlış; aynı ailenin diğer raporu doğru vermiş, yani hata tek raporda |
| C14 | Goedel-Prover-V2 32B: MiniF2F pass@32 %88,1, iki turlu öz-düzeltmeyle %90,4 | arxiv.org/abs/2508.03613 | 2025-08 | K | sağlam | İki rapor + V26 iki kez `TUTTU` |
| C15 | Aynı 32B model "rakiplerden 80× daha küçük" | V26-2 b15: "80X smaller" **8B** modele ait | 2025-08 | **X** | düştü | Rakam doğru modele bağlanmamış; tez donanım planı bu satıra dayandırılamaz |
| C16 | arXiv 2607.07779 "kanıt açıklama ve yorumlanabilirliği" açık araştırma sorunu olarak listeliyor ve lisans-ölçekli yönler öneriyor | Kendi çekimim (6): özette bu konular **yok**; sayılan boşluklar datasets, relational structure, mathematical exploration, tool ecosystem, human-AI collaboration | 2026-07-08 | **X** | düştü | Yanlış atıf, kendi birincil çekimimle kesinleşti; bu satıra dayanan proje kalıbı önerisi de dayanaksız kalır |
| C17 | "AI kanıtını insana çevirme" boşluğu kısmen kapalı: arXiv 2509.09726 üniversite-düzeyi ispatların anahtar noktalarının %86'sını yakalıyor | arxiv.org/pdf/2509.09726 | 2025-09 | K | **daraldı** | Yalnız koşulda: tek rapor, tek kaynak, kendi çekimimle doğrulanmadı; ama C16'nın düşmesiyle bu satır "alan tamamen açık" iddiasının karşı ağırlığı olarak duruyor |
| C18 | LeanCopilot MIT lisanslı, GPU **isteğe bağlı**, CPU'da çalışabiliyor | github.com/lean-dojo/LeanCopilot | 2026-09-21 çekim | K | sağlam | İki rapor + V26 iki kez `TUTTU`; "tek laptop" fizibilitesinin taşıyıcı dayanağı |
| C19 | Donanım gerçeği: 671B sınıfı model tek laptopta pratik değil; 32B için 24-48GB VRAM | Rapor kendi `[?]` işaretiyle veriyor, birincil doğrulama yok | 2026-09-21 | K | **daraldı** | Yalnız kestirim olarak kullanılabilir; VRAM rakamı hiçbir birincil kaynakta doğrulanmadı |
| C20 | Harmonic Aristotle 5/6 problemi çözdü | V26-2 b4: özet yalnız "gold-medal-equivalent performance" diyor | 2025-10 | **X** | düştü | Problem sayısı kaynakta yok; "altın-eşdeğeri" ifadesi K olarak ayakta |
| C21 | AxiomProver Putnam 2025'in tümünü çözdü · Mathlib Demailly Ödülü aldı · Leiden Declaration içeriği | Üçü de tek arama-özeti, hiçbiri açılmadı | yok | **X** | düştü | Üç iddia da URL'siz ve tek kaynaklı; raporun kendisi de X/başlık-düzeyi demiş |

### Aile D: meslek öngörüsü + Türkiye tez biçimi

| # | İddia | Kanıt | AS-OF | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|---|
| D1 | BLS 2025-2035: mathematicians **%1**, statisticians **%11**, birleşik **%10**, yılda ~2.000 açık pozisyon | bls.gov/ooh/math/mathematicians-and-statisticians.htm | sayfa 2026-08-27 | K | sağlam | İki rapor + V26 iki kez `TUTTU`; bu ailenin en sağlam rakamı |
| D2 | WEF Future of Jobs 2025 kapsamı: 1.000+ işveren, 14M+ çalışan, 22 sektör kümesi, 55 ekonomi; işlerin %39'unda beceri dönüşümü | reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf (curl + pdftotext) | 2025-01 | K | sağlam | Birincil PDF'ten doğrudan okundu, V26 `TUTTU`; WebFetch 10 MB sınırını aşan dosya doğru yöntemle alınmış |
| D3 | Aynı raporun en hızlı büyüyen 15 mesleği listesinde "AI and Machine Learning Specialists" var, "Data Scientist" tek başına **yok** ("Data Analysts and Scientists" var), "Mathematicians, Actuaries and Statisticians" Table A3'te (s.103) var ama büyüme listesinde yok | Aynı PDF, s.19 Figure 2.2 + s.103 | 2025-01 | K | **daraldı** | Yalnız koşulda: "matematikçi büyüme top-15'inde yok" doğru; "taksonomide hiç yok" yanlış olur |
| D4 | FrontierMath 338 soru, 70+ matematikçi | V26-2 b3: verilen sayfa "several hundred" diyor; 338 yalnız kardeş sayfada doğrulanıyor | 2026-06-12 | K | **daraldı** | Yalnız koşulda: rakam doğru ama **atıf yanlış sayfaya**; tezde kaynak yeniden yönlendirilmeli |
| D5 | FrontierMath Tier 4: 50 problem (2 kamuya açık + 48 özel); kümülatif 17/48 (%35), GPT-5.2 Pro tek başına 15/48, önceki rekor 13 | epoch.ai/benchmarks/frontiermath-tier-4-v1 + epochai.substack.com/p/new-record-on-frontiermath-tier-4 | 2026-01-23 | K | sağlam | Doğru kaynak çiftiyle V26 `TUTTU`; "48 = özel alt küme" okuması doğrulandı |
| D6 | Aynı 17/48 rakamı ourworldindata grafiğinden alınabilir | V26-2 b4: o sayfa "Tier 4 … is not included here" diyor | 2026-01 | **X** | düştü | Verilen kaynak Tier 4'ü açıkça kapsam dışı bırakıyor |
| D7 | Anthropic Economic Index: "computer and mathematical" Claude kullanımında ~%30, ABD işgücünde ~%4 | anthropic.com/news/the-anthropic-economic-index (%37,2 / %3,4, 2025-02-10) · …/january-2026-report (~%33 Claude.ai, ~%46 API, işgücü payı verilmiyor) · …/economic-index-june-2026-report (~%30 anket, %4 istihdam) | 2025-02 → 2026-06 | K | **daraldı** | Yalnız koşulda: oran **rapor sürümüne göre %30-37,2 arasında**; hangi sürümün alıntılandığı yazılmadan sayı kullanılamaz |
| D8 | Kullanım augmentation-ağırlıklı: %57 artırma / %43 otomasyon | Tek rapor, ikincil özet; V26'da ilgili sayfa `ERİŞİLEMEDİ` (JS panosu) | belirsiz | K | **daraldı** | Yalnız koşulda: hangi sürümün rakamı olduğu belirsiz, birincil panoda görülemedi |
| D9 | de Bruijn faktörü 2023-24'te ~20, düşüşte, 1'in altına inmesine "temel bir engel yok" | Kendi çekimim (7): ifade birebir var, **ve aynı cümle** "that measurement has since been overtaken by rapid advances in autoformalization" diye devam ediyor | 2023-24 ölçüm, 2026 not | K | **daraldı** | Yalnız koşulda: rakam doğru ama kaynağın kendisi ölçütü **eskimiş** ilan ediyor; AS-OF kuralı gereği "o zaman böyle" notudur, tasarım girdisi değil |
| D10 | Harmonic'te 9 tam zamanlı mühendislik pozisyonu açık, aralarında Formal Verification Engineer (Palo Alto, Londra) | harmonic.fun/careers/ | 2026-09-21 çekim | K | sağlam | İki rapor + V26 iki kez `TUTTU`; ilanlarda tarih damgası yok, o yüzden yalnız çekim günü için geçerli |
| D11 | İTÜ Matematik Mühendisliği: MAT4901 / 4901E / 4902-492 / 4902E-492E, dört şablon | matmuh.itu.edu.tr/egitim/lisans/bitirme-staj | 2026-09-21 çekim | K | sağlam | İki rapor + V26 iki kez `TUTTU`; "iki dönem" okuması sayfada yazmıyor, çıkarımdır `[?]` |
| D12 | YTÜ kılavuzunda çalışmanın adı bölüme göre değişiyor ("Bitirme Projesi" vs "Bitirme Tezi veya Bitirme Projesi"); beyaz karton cilt; deneysel olmayan işte bile "Uygulama" bölümü zorunlu | elm.yildiz.edu.tr/…/bitirme-calismasi-yazim-kilavuzu.pdf (curl + pdftotext) | belge ~2024 | K | sağlam | İki rapor + V26 iki kez `TUTTU`; **alan dışı**: belge Elektrik-Elektronik Fakültesi'nin, Matematik Mühendisliği'nin değil, raporda da "analojiyle aktarılmamalı" diye işaretli |
| D13 | Bu kılavuz 2024-05 tarihlidir | V26-2 b10: PDF meta-tarihi **2024-01**, "2024-05" sunucu dizin damgası | 2024-01 | **X** | düştü | Dizin yolu belge tarihi sanılmış |
| D14 | YTÜ Matematik Mühendisliği bölüm sayfası "Sayfa Hazırlanıyor…" durumunda, akademik içerik yok | matmuh.yildiz.edu.tr | 2026-09-21 | K | sağlam | V26 `TUTTU`; negatif bulgu doğrudan gözlemle desteklenmiş |
| D15 | Buzzard 2025 Oxford Strachey Lecture "Will computers prove theorems?" | V26-2 a ve b6: verilen iki URL'nin ikisinde de yok | 2025 | **X** | düştü | Kaynak iddiayı taşımıyor; "Mathlib ~2 milyon satır" kısmı ikinci kaynakta ayakta (C10) |
| D16 | Cambridge MPhil PINN tezi, arXiv 2401.03534, Ocak 2024 | arxiv.org/abs/2401.03534; V26-2 b11: "Cambridge"/"MPhil" özet sayfasında yok | 2024-01-07 | K | **daraldı** | Yalnız koşulda: başlık ve tarih doğru; kurum/derece bilgisi doğrulanmadı ve **yüksek lisans** düzeyinde, lisans emsali değil |
| D17 | Berkeley EECS-2025-121 (Yue, Klein), "thesis submitted", 2025-05-16 | www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-121.pdf (curl + pdftotext) | 2025-05-16 | K | sağlam | V26 `TUTTU`; bu ailedeki tek gerçekten tez-formu doğrulanmış örnek |
| D18 | U-MATH / UGMathBench "arXiv / ICLR 2025" | V26-2 b14: gönderim geçmişinde ICLR referansı yok | 2024-12 | **X** | düştü | Konferans bağlantısı kaynakta doğrulanamadı |
| D19 | YÖK Tez Merkezi'nde AI × matematik (Lean / biçimsel doğrulama) konulu Matematik Mühendisliği tezi **bulunamadı**; bulunan tek veri 2017-2021 Bilgisayar Mühendisliği alanında 84 yüksek lisans tezi bildiren bir derleme makalesi, konu dışı | tez.yok.gov.tr (canlı form doldurulmadı) + dergipark.org.tr/tr/pub/okufbed/article/1062622 | 2026-09-21 | K | sağlam | İki rapor da aynı negatifi buldu ve ikisi de "bulunamadı ≠ yok" sınırını açıkça beyan etti; bu, negatif bulgunun doğru raporlanma biçimidir |

### Aile E: küresel üniversite tez biçimi ve örnekler

| # | İddia | Kanıt | AS-OF | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|---|
| E1 | Princeton matematik: resmî uzunluk şartı yok, tek aralıklı tipik 20-40 sayfa; bazıları 10 altı, bazıları 100 üstü | math.princeton.edu/undergraduate/majors/independent-work | 2026-09-21 çekim | K | sağlam | İki rapor + V26 dört sondajda `TUTTU`; bu ailenin en çok çapraz doğrulanan satırı |
| E2 | Princeton dört ölçüt: ileri içerik ve literatür aşinalığı, özgün bakış açısı, titiz mantık, net sunum | Aynı sayfa | 2026-09-21 çekim | K | sağlam | V26 `TUTTU`, dört başlık madde madde eşleşti |
| E3 | Cambridge Part III essay: "mükemmel" için ~5.000, 8.000 kelimeyi aşmamalı; 20-30 sayfa, istisnaen 35; β- notu "upper-second-class final-year project" kalitesi | maths.cam.ac.uk/postgrad/part-iii/current/examinations-and-essays | 2026-09-21 çekim | K | sağlam | İki rapor + V26 üç sondajda `TUTTU` |
| E4 | Oxford Part C: 7.500 kelime sınırı, tipik 25-35 sayfa, **50 sayfa mutlak tavan** | maths.ox.ac.uk/…/dissertations | 2026-09-21 çekim | K | sağlam | V26 üç sondajda `TUTTU`; 50 sayfa tavanı yalnız bir raporda var, gerçek bir ekleme |
| E5 | Part C, matematik programının 4. yılıdır | V26-3 b5: sayfa yıl belirtmiyor | 2026-09-21 | **X** | düştü | Verilen kaynakta yok; genel bilgi olarak doğru olabilir ama bu kanıtla D olamaz |
| E6 | Stanford CS senior project: tam beş yol (CS194/194W, CS210B, CS191/191W, Honors Thesis, CS294); GPA ≥2,0; onur programı başvurusu 1 Mayıs | cs.stanford.edu/bs-requirements-senior-project | 2026-09-21 çekim | K | sağlam | İki rapor + V26 üç sondajda `TUTTU`, seçenekler tek tek sayıldı |
| E7 | CMU SCS honors thesis: 2 dönem, 36 kredi birimi, prospectus ≤3 sayfa | V26-3 b11, b12: üç rakamın hiçbiri verilen sayfada yok | 2026-09-21 | **X** | düştü | Sayfa yalnız Undergraduate Catalog'a yönlendiriyor; rakamlar kaynaksız |
| E8 | Harvard SEAS 2024, Leonard Tang, DASH atıfında "**Bachelors Thesis**" | dash.harvard.edu/items/1639db4a-… | 2024 | K | **daraldı** | Yalnız koşulda emsal: derece türü doğrulandı ama konu **LLM sağlamlık/red-teaming**, AI × matematik değil; bir rapor bunu kendisi de yazmış |
| E9 | Imperial "Formalising Mathematics" 2024 (Buzzard): "final year of an undergraduate mathematics degree" hedefli, Lean 4, Ocak-Mart 2024 koştu, GitHub deposu var | ma.imperial.ac.uk/~buzzard/xena/formalising-mathematics-2024 + github.com/ImperialCollegeLondon/… | 2024 | K | sağlam | İki rapor + V26 iki kez `TUTTU`; "e.g." dili tek hedef kitle iddiasını zayıflatıyor, bu raporda not edilmiş |
| E10 | Aynı kursun hedef kitlesine "MSc" de dahildir | V26-3 b14 notu: "MSc" kelimesi sayfada yok | 2024 | **X** | düştü | Sayfada karşılığı yok |
| E11 | Adı verilen beş tez arşivinde ("Lean 4" / "autoformalization" / "physics-informed", 2024-2026) doğrulanmış lisans tezi kaydı yok | dash.harvard.edu iki sorgu "no results"; dataspace.princeton.edu 401; dspace.mit.edu 404; research-collection.ethz.ch 429 | 2026-09-21 | K | **daraldı** | Yalnız dar okumada ayakta: Harvard'da iki sorgu sıfır döndü, **diğer üç arşiv erişilemedi**, yani doğrulanmadı da çürütülmedi de; "yok" değil "bulunamadı" |
| E12 | Bu konularda üst-düzey kurumlarda hiçbir lisans çalışması yok (geniş okuma) | TUM SCML'de üç ayrı "Bachelor thesis" (2024 Merrath, 2025 Akin, 2026 Koufogazou Loukianova) + Harvard/Tang + Duke Math+ AlgebraInLean | 2024-2026 | **X** | düştü | Geniş okuma somut örneklerle çürüdü; bu, koşumun en net adversarial kazanımlarından biri |
| E13 | Imperial, ETH, EPFL ve TUM'da "senior thesis" kalıbının doğrudan karşılığı yok | ethz.ch Bachelor matematik müfredatı "Seminars, Bachelor's thesis" (3. yıl) · edu.epfl.ch MATH-397 "mandatory", 14 hafta × 12 saat, 12 kredi · cs.cit.tum.de/en/scml Bachelorarbeit listesi | 2026-09-21 çekim | **X** | düştü | Üç kurum için açıkça çürüdü; V26 iki kez `TUTTU` verdi |
| E14 | Aynı iddia Imperial için ayakta kalabilir | Yalnız M4R (MSci 4. yıl) bulundu; 3 yıllık BSc'de zorunlu tez doğrulanmadı | 2026-09-21 | K | **daraldı** | Yalnız Imperial koşuluyla; kanıt eksikliği, kanıtlanmış yokluk değil |
| E15 | arXiv 2602.12891 bir **doktora** tezidir (journal-ref: "ISTA Ph.D. Thesis (2026)"), lisans emsali değildir | arxiv.org/abs/2602.12891 | 2026 | K | sağlam | V26 iki kez `TUTTU`; adayın doğru gerekçeyle reddedilmesi |
| E16 | arXiv 2603.24372'nin "Stanford CS224N Custom Project" olduğu iddiası arama-özeti hatasıdır; gerçek özet sayfasında bu ifade yok | arxiv.org/abs/2603.24372 | 2026 | K | sağlam | Doğru reddetme; arama-özeti halüsinasyonunun yakalandığı ikinci vaka (bkz. B9) |
| E17 | "Diğer sekiz kurumda doğrulanmış örnek bulunamadı" | V26-3 c: parantezde 10 kurum sayılmış | 2026-09-21 | **X** | düştü | İç sayım tutarsızlığı; hükmün yönünü değiştirmiyor ama rakam disiplinini bozuyor (m.39) |
| E18 | Lisans düzeyinde AI × matematik işi bağımsız tez olarak değil **ders projesi** olarak ortaya çıkıyor (Imperial, CMU 15-311/15-217, Stanford CS 99, EPFL CS-643) | ma.imperial.ac.uk · cs.cmu.edu/~mheule · perfect-math-class.leni.sh · edu.epfl.ch (İngilizce sayfa 404) | 2024-2026 | K | **daraldı** | Yalnız koşulda: eğilim doğru yönde ama EPFL ayağı zayıf (CS-643 **doktora okulu** dersi, lisans erişimi doğrulanmadı, sayfa 404) ve Stanford/CMU ayakları yalnız arama-özeti |

### Aile F: matematikçi rolünün evrimi

| # | İddia | Kanıt | AS-OF | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|---|
| F1 | O*NET 15-2021.00 "Mathematicians" 12 görev listeliyor, hiçbirinde AI/yapay zeka geçmiyor; Tasks verisi 2025'te güncellenmiş | onetonline.org/link/summary/15-2021.00 + /link/updates/15-2021.00 | 2025 güncelleme | K | sağlam | İki rapor + V26 üç sondajda `TUTTU`; güncellik ayrıca test edilmiş, yani "bayat veri" itirazı kapatılmış |
| F2 | Eloundou vd.: ABD işgücünün ~%80'i görevlerinin en az %10'unda, ~%19'u en az %50'sinde etkilenebilir | arxiv.org/abs/2303.10130 | 2023-03 | K | **daraldı** | Yalnız koşulda: **2023 kuşağı** ölçüm, akıl yürütme/ajan modelleri öncesi; Karar 68 / Karar 102 (3) gereği "o zaman böyle" notudur. Matematikçiye özel satır iki koşumda da PDF parse hatasıyla alınamadı |
| F3 | Anthropic Economic Index (2026-06-26): "Computer and Mathematical" anket katılımcılarının ~%30'u (ABD istihdamının %4'üne karşın); **en düşük özerklikli çıktılar** "math or calculations, translations, and Q&As" | anthropic.com/research/economic-index-june-2026-report | 2026-06-26 | K | sağlam | İki rapor + V26 iki kez `TUTTU`; ikinci yarısı hipotezle doğrudan gerilim üretiyor, bkz. çelişki listesi |
| F4 | Microsoft "Working with AI": 200.000 anonimleştirilmiş Bing Copilot konuşması, O*NET IWA sınıflandırması | microsoft.com/en-us/research/publication/working-with-ai-… | 2025-07 | K | sağlam | V26 `TUTTU` |
| F5 | Aynı çalışmada konuşmaların %40'ında kullanıcı hedefi ile AI eylemi farklı | V26-3 b8: alınan sayfada bu yüzde yok | 2025-07 | **X** | düştü | Rakam kaynakta bulunamadı; rapor zaten K/arama-özeti diye işaretlemişti |
| F6 | Tao: üretim / doğrulama / sindirim; sindirim "AI araçlarının optimize etmesine en az elverişli" aşama; insan rolü küratörlük, açıklama, sentez, "yönetici" değil | arxiv.org/html/2608.16753v1 + kendi çekimim (7) | 2026-08 | K | sağlam | Birincil makale metni + Tao-onaylı derleme; iki rapor da aynı terimleri buldu |
| F7 | 25 Fields madalyalısı bildirisi, 2026-09-11, "the crucial human transmission chain between mathematicians would be lost" | Kendi çekimim (3) | 2026-09-11 | **D** | sağlam | Birincil metinden birebir |
| F8 | Bildiri 2026-09-16 itibarıyla 7.200+ ek imzacıya ulaştı | Kendi çekimim (3) + V26-3 b10: ne birincilde ne gösterilen ikincilde var | 2026-09-16 | **X** | düştü | B11 ile aynı dayanaksız rakam, iki ayrı ailede tekrarlanmış |
| F9 | Buzzard 2026-07-20: iki ayda üç karşı-örnek (Erdős birim-uzaklık 05-20, 60 yıllık Grothendieck sorusu 07-11, 100 yıllık Jacobian sanısı 07-20); karşı-örnek aramada AI insandan **zaten hızlı** | xenaproject.wordpress.com/2026/07/20/… | 2026-07-20 | K | sağlam | Birincil blog; V26 üç sondajda `TUTTU`, tarih aritmetiği de doğrulandı |
| F10 | Buzzard'ın insan rolü tanımı "biçimsel önerme formülasyonu"dur | Aynı blog: metinde bu ifade yok; bulunan "the true value of work like this is to give humans better understanding of mathematics" | 2026-07-20 | **X** | düştü | İki raporun aynı kaynaktan çıkardığı iki farklı rol tanımı; birincil metin "anlama/içgörü" tarafını destekliyor, "formülasyon" tarafını desteklemiyor |
| F11 | Harmonic'te "Formal Verification Engineer" ilanı var; "AI Manager" / "AI Orchestrator" unvanı **yok** | harmonic.fun/careers/ | 2026-09-21 çekim | K | sağlam | İki rapor + V26 iki kez `TUTTU`; hipotezin iş piyasası ayağını doğrudan sınıyor |
| F12 | Birleşik "matematik mühendisi" / "mathematics engineer" / "AI mathematics manager" unvanı hiçbir ilanda bulunamadı; bulunan unvanlar parçalı (Formal Verification, Proof, Benchmarking) | harmonic.fun · epoch.ai/about/careers · alignerr.com | 2026-09-21 | K | sağlam | İki rapor bağımsız aradı, ikisi de bulamadı; negatif, sınır beyanlı |
| F13 | Alignerr "Lean 4 Proof Engineer", 170-200 $/saat, uzaktan | alignerr.com/jobs/d61fdffd-… | 2026-09-21 çekim | K | **daraldı** | Yalnız koşulda: tek ilan, tek platform; piyasa kanıtı değil tek gözlem |
| F14 | Anthropic iç raporu (2025-12-02): 132 mühendis anketi, 200.000 Claude Code transkripti, ölçüm Şubat-Ağustos 2025; görev karmaşıklığı 3,2 → 3,8; ardışık araç çağrısı +%116 (9,8 → 21,2); insan turu 6,2 → 4,1 (yaklaşık %33 azalma) | anthropic.com/research/how-ai-is-transforming-work-at-anthropic | 2025-12-02 | K | sağlam | İki rapor + V26 dört sondajda `TUTTU`; bu ailenin en sağlam nicel dayanağı |
| F15 | METR (2025-07-10): 16 deneyimli geliştirici, 246 görev; AI ile **%19 daha yavaş**, buna rağmen %20 daha hızlı olduklarına inandılar | metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | 2025-07-10 | K | sağlam | Birincil, V26 `TUTTU`; "yönetmek daha verimli" varsayımına doğrudan karşı kanıt |
| F16 | Aynı bulgu 2026'da hâlâ geçerli | metr.org/blog/2026-02-24-uplift-update/: METR sinyali "unreliable" ilan ediyor, %30-50 seçilim yanlılığı, ham -%18 / -%4 güven aralıkları sıfırı kapsıyor | 2026-02-24 | K | **daraldı** | Yalnız koşulda: 2025 bulgusu çürütülmedi ama 2026 güncelliği **açık**; yön netliği yok |
| F17 | OpenAI koşumu ~10.000 ajan, 2,7 milyon mesaj, ~130 milyar token, 88 saat | coindesk.com/tech/2026/09/09/… | 2026-09-08 | K | sağlam | A12 ile aynı olayın ikinci kaynaktan doğrulanması |
| F18 | Maliyet "milyonlarca dolar" | Yönetici beyanı (ikincil aktarım); ~6,5M$ rakamı raporun kendi perakende-fiyat kestirimi | 2026-09 | K | **daraldı** | Yalnız kestirim olarak; rakam `[?]` işaretli olmalı, birincil maliyet açıklaması yok |
| F19 | "20 deneme, 17 başarılı, 3 başarısız" | V26-3 b1: raporun kendi listesinde 4 madde `BAŞARISIZ` | 2026-09-21 | **X** | düştü | İç sayım tutarsızlığı (gerçek 16/4) |
| F20 | Venkatesh "Human Mathematics in the Age of Reasoning Machines": "yönetici/orkestratör" çerçevesi kullanmıyor, odak kavramların bilişsel işlevi | math.ias.edu/~akshay/research/HumanMath.pdf (ilk 10 sayfa) | PDF'te tarih yok | K | **daraldı** | Yalnız koşulda: AS-OF yok, makalenin yalnız ilk 10 sayfası okundu, kalanı kapsam dışı |
| F21 | Hiçbir birincil kaynak "o hâlde insana gerek kalmaz" pozisyonunu **savunmuyor**; hepsi bunu risk olarak çerçeveliyor; "oversee" diline en yakın örnek bir kişisel blog | scientificamerican.com/article/mathematicians-confront-the-ai-apocalypse/ · proofsandprompts.com/2026/09/10/… | 2026-09 | K | sağlam | Negatif bulgu, iki bağımsız yönden arandı ve arama sınırı beyan edildi |

---

## Kovalar

### Sağlam çekirdek (56 iddia)
Koşulsuz ayakta kalanlar. Tavan gereği çoğu K'dir; **D olanlar** yalnız kendi çekimimle birincil kaynaktan doğruladıklarım: A5, A6, A7, A8, B3, B6, B10, F7.
Öne çıkanlar: Clay'in resmî durumu "Active" ve ödül yok (A7) · OpenAI'ye atfedilen belgenin kendisi zorlamasız Millennium sorusunun açık olduğunu söylüyor (A6) · 25 Fields madalyalısı bildirisi ve tarihi (B10/F7) · BLS %1/%11 (D1) · Princeton/Cambridge/Oxford/Stanford biçim rakamları (E1-E4, E6) · O*NET 12 görevinde AI yok, veri 2025 güncel (F1) · Anthropic 3,2 → 3,8 ve -%33 insan turu (F14) · METR %19 yavaş / %20 hızlı sanma (F15) · Mathlib, PutnamBench, LeanCopilot, FrontierMath Erdős rakamları (C8-C12, C18).

### Daraldı (25 iddia, koşulu yazılı)
Her biri yalnız satırında yazılı koşulda doğrudur:
A4 (Tao formalizasyonun varlığını bildirir, denetlemez) · A9 (tek bağımsız yayının kendi denetim tablosu, kurumsal denetim değil) · A15 (tek taraflı anlatı, karşı taraf reddediyor) · B2 (gün yalnız ikincil kronolojide) · B7 (konuşmadan iki ikincil aktarım, yazılı makalede yok) · B14 (ham gönderiler açılmadı) · B16 (slayt PDF'i metne çevrilemedi) · C4 (kaynağın kaynağı modelin kendi sitesi) · C17 (tek kaynak) · C19 (VRAM kestirimi `[?]`) · D3 (büyüme listesi ≠ taksonomi) · D4 (atıf yanlış sayfaya) · D7 (oran rapor sürümüne göre %30-37,2) · D8 (hangi sürüm belirsiz) · D9 (ölçüt kaynağınca eskimiş ilan edildi) · D16 (yüksek lisans, kurum doğrulanmadı) · E8 (derece doğru, konu AI × matematik değil) · E11 (yalnız dar okuma; üç arşiv erişilemedi) · E14 (yalnız Imperial) · E18 (EPFL ayağı doktora dersi, sayfa 404) · F2 (2023 kuşağı) · F13 (tek ilan) · F16 (2026 güncelliği açık) · F18 (maliyet kestirimi) · F20 (AS-OF yok, kısmi okuma).

### Düştü (32 iddia)
A10, A13, A14, A16, A17 · B4, B8, B9, B11, B15 · C3, C5, C13, C15, C16, C20, C21 · D6, D13, D15, D18 · E5, E7, E10, E12, E13, E17 · F5, F8, F10, F19.
Düşme türleri: **yanlış atıf** (B4 yazarlık · C16 makale konusu · D15 Strachey · D18 ICLR · F10 rol tanımı · D6 ve E5/E7 kaynakta bulunmayan rakam) · **dayanaksız rakam** (B11/F8 7.200+ · A13 100 ajan · A14 26 madalyalı · A16 Poincaré · C5 dört AI · C21 üçlü tek-kaynak) · **iç sayım hatası** (E17, F19) · **sürüm/model karışması** (C13, C15, C20) · **adversarial turda çürüyen geniş okuma** (E12, E13) · **çözülebilir sanılan çelişki** (A10).

### Çelişkili (4 işaret, üst-küme; yukarıdaki sayımlarda zaten yer alıyorlar)
1. **OpenAI kaç sonuç duyurdu?** Bir kaynak OpenAI'ye hem zorlamalı Navier-Stokes hem zorlamasız Euler sonucu atfediyor, bir başkası Euler'i yalnız Buckmaster-Alpöge'ye atfediyor. A10'u çürüten "iki ayrı sonuç" okuması ikincil düzeyde hâlâ tek tip doğrulanmadı; OpenAI'nin birincil metni her koşumda 403 verdiği için kapanmadı.
2. **Talep artıyor mu azalıyor mu?** BLS dar "mathematician" kodu %1 büyüme veriyor (D1, sağlam); aynı ailede AI beceri primi %56, ilan artışı %78, aday havuzu %24 bulguları var. İkisi de kaynaklı; çelişki taksonomiktir (dar meslek kodu ile komşu unvanlar), ama tez kapsamında saklanmadan taşınmalı.
3. **Matematik görevleri düşük özerklikte mi, yoksa 10.000 özerk ajan mı çalışıyor?** F3 (matematik en düşük özerklikli çıktı sınıfı, 2026-06) ile A12/F17 (10.000 özerk ajan, 88 saat, 2026-09) arasında gerçek bir gerilim var. İkisi de doğrulandı; muhtemel açıklama ölçüm birimi farkıdır (genel kullanıcı tabanı vs tek laboratuvar koşumu), ama bu açıklama **hiçbir kaynakta yok**, çıkarımdır `[?]`.
4. **IMO 2026 sonuçları resmî mi?** Bir kaynak "officially graded 42/42" diyor, iddianın temel kaynağı ise "a post on the model's website" diyor. Bağımsız IMO sertifikasyonu hiçbir koşumda doğrulanmadı.

---

## m.16 işaretli çelişkiler

**Girdi yok.** Emirde depo kanonundan alıntı verilmedi; kanon dosyaları bu ajana kapalıdır (bağlam paylaşmama kuralı). Dolayısıyla iddia setinin kanonla çelişip çelişmediği ölçülmedi ve bu başlık altında hiçbir satır işaretlenmemiştir. Kanon alıntısı sonradan verilirse tartılmaya en uygun iki nokta, yukarıda kanıtlanmış hâlleriyle şunlardır: AS-OF damgasız alıntıların kullanımı (B8) ve eski kuşak ölçümlerin güncel tasarım girdisi sayılması (F2, D9).

---

## Hayatta-kalma

**113 iddia · sağlam 56 / daraldı 25 / düştü 32 (· çelişkili 4 işaretli, üst-küme) · etiket dağılımı D 8 / K 73 / X 32 · V26 tavanı 12 raporun 10'una uygulandı, D istisnası yalnız hakemin 8 çekimi.**

---

## Hakem hata kaydı

Bu koşumda iki usul dersi çıktı, ikisi de `/Users/HasanSalihSahin/sistem/jarvis/.claude/agent-memory/hakem/` altına yazıldı ve `MEMORY.md` indeksine pointer eklendi. İçerik hükmü, üretici rapor özeti ya da Salih kararı hafızaya **girmedi**; yalnız usul.

**1. `feedback-fetch-ozetleyici-kurgu-bayragi.md`** (yeni dosya)
> WebFetch'in küçük özetleyici modeli, kendi bilgi kesiminden **sonraki** tarihli sayfalar için "this appears to be a fictitious webpage", "this article does not exist", "a future date" gibi hükümler üretir; aynı cevapta sayfanın gerçek içeriğini birebir alıntılamayı sürdürür. Bu bayrak **veri değil gürültüdür**: hükme sokulmaz, çürütme sayılmaz. Karar, dönen içeriğin kendisine ve çapraz tutarlılığa bakılarak verilir.
> **Why:** 2026-09-21 hakem koşumunda iki ayrı çekim (claymath.org/news/navier-stokes-announcement/ ve stanfordtechreview.com) "var değil/kurgusal" etiketiyle döndü ama ikisi de tam alıntı, tablo rakamı ve tarih verdi; içerik ayrıca bağımsız ikinci sayfayla (claymath "Active" sayfası) tutarlıydı. Bayrağa uyulsaydı doğrulanmış iki nokta yanlışlıkla `ÇÜRÜDÜ` yazılacaktı. Bu, 2026-07-17 dersinin ayna hâli: orada "403 = doğrulandı sanmak" hatası vardı, burada "özetleyici kurgu dedi = çürüdü sanmak".
> **How to apply:** Çekim cevabında kurgu/gelecek-tarih uyarısı görünce (a) uyarıyı rapora "özetleyici bayrağı, hükme sokulmadı" diye yaz, (b) dönen birebir alıntıları normal kanıt gibi tart, (c) mümkünse aynı iddiayı ikinci bir URL'den çapraz doğrula. Gerçek `ERİŞİLEMEDİ` yalnız HTTP hatası, boş gövde ya da ikili/parse edilemeyen içeriktir.

**2. `feedback-dogrulama-butcesi-hedefleme.md`** (yeni dosya)
> Hakem doğrulama bütçesi (≤8 WebFetch) şu iki koşulu **birlikte** sağlayan iddialara harcanır: (a) aynı ailenin iki üretici raporu arasında çelişkili ya da tek-kaynaklı, (b) hüküm ya da alt-karar taşıyıcısı. V26'da iki ayrı raporda `TUTTU` çıkmış olgular yeniden çekilmez.
> **Why:** 2026-09-21 koşumunda 12 raporun 10'unda `TUTMADI` ≥1 çıktı, yani V26 tavanı tabloyu neredeyse tümüyle K'ya bastırdı; D istisnası yalnız hakemin kendi çektiği noktalardan gelebiliyordu. 8 çekim çift-`TUTTU` olgulara (Oxford 7.500 kelime, Epoch 68 problem) harcansaydı tablo tümüyle K kalır, hiçbir tez-antitez çelişkisi çözülmezdi. Hedefli harcama 4 çelişkiyi kapattı: iddia kapsamı (forced/unforced), yazarlık atfı, yanlış makale atfı, imzacı sayısı.
> **How to apply:** Raporları okuduktan sonra çekimden önce "aile-içi çelişki listesi" çıkar, taşıyıcılığa göre sırala, ilk 8'i çek. Kaynağın kurumsal ağırlığını ima eden ad (ör. alan adında üniversite adı geçmesi) tek başına otorite sayılmaz; sayfanın kendi künye cümlesi çekilip rapora yazılır.

---

**Kaydedilecek yol (çağıran yazar):** `cc/rapor/2026-09/rapor-2026-09-21-bitirme-ai-matematik-hakem.md`
**Senaryo-defterine tek satır:** 113 iddia · sağlam 56 / daraldı 25 / düştü 32 (· çelişkili 4) · D 8 / K 73 / X 32 · V26 tavanı 10/12 rapora uygulandı.
