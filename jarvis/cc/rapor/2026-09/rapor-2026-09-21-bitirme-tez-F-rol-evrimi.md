# Tez-F: Matematikçinin Rolü — "AI Matematiği Yönetme" Hipotezi (ATLAS/TEZ)

**AS-OF:** 2026-09-21 · **Ajan:** atlas (aile F, TEZ rolü) · **Model-hafızası kesim:** 2026-01 (kesim sonrası her iddia doğrulanmış kaynakla işaretli)

**Hipotez:** "AI matematiği çok iyi yapacaksa insan matematikçinin / matematik mühendisinin rolü AI'ın yaptığı matematiği yönetmek olur."

**Disiplin notu:** Alıntılar ≤15 kelime, gerisi paraphrase. Etiket D (doğrulanmış birincil kaynak) / K (kanıt zayıf/ikincil) / X (spekülasyon).

---

## 1. Görev-düzeyi analiz (O*NET + Eloundou + Anthropic Economic Index + Microsoft)

**O*NET 15-2021.00 "Mathematicians" görev listesi** (D — birincil kaynak, doğrudan açıldı, https://www.onetonline.org/link/summary/15-2021.00, AS-OF 2026-09-21, O*NET sürüm tarihi sayfada belirtilmedi):

12 görev listelendi: (1) başkalarına mentorluk, (2) alanda bilgi güncel tutma (dergi/konferans), (3) yeni ilkeler/ilişkiler geliştirme, (4) araştırmayı yayma (rapor/makale/sunum), (5) varsayım kümeleri kurup sonuçlarını keşfetme, (6) hesaplama + sayısal analiz uygulama, (7) nicelik/büyüklük/biçim ilişkilerini ele alma, (8) geleneksel alanlarda (cebir, geometri, olasılık, mantık) araştırma, (9) matematiksel/istatistiksel model geliştirme, (10) kuramı iş/mühendislik/bilim problemlerine uygulama, (11) hesaplamalı yöntem geliştirme, (12) şifreleme sistemleri tasarlama/çözme.

**Maruziyet değerlendirmesi (görev-maruziyet tablosu aşağıda §"Görev-maruziyet tablosu"):** Doğrudan bir O*NET-15-2021 satırlı Eloundou vd. (2023) exposure tablosu bu koşumda AÇILAMADI — hem `arxiv.org/abs/2303.10130` hem `arxiv.org/pdf/2303.10130` denendi; abstract sayfası genel bulguyu verdi (D, kısmi), tam PDF ikinci denemede "corrupted/binary" döndü (X — erişim engeli, bayraklı). Genel bulgu (D, https://arxiv.org/abs/2303.10130, Science 384(6702):1306-08, 2023/2024): ABD işgücünün **~%80'i** görevlerinin en az **%10'unun** LLM'den etkilenebileceği, **~%19'u** görevlerinin en az **%50'sinin** etkilenebileceği bulundu. Occupation-düzeyinde matematikçiye özel puan bu koşumda doğrulanamadı → **bulunamadı, meşru boşluk**.

**Anthropic Economic Index, Haziran 2026 raporu** (D — doğrudan açıldı, https://www.anthropic.com/research/economic-index-june-2026-report, AS-OF rapor tarihi 2026-06-26): "Computer and Mathematical occupations" anket katılımcılarının **~%30'unu** oluşturuyor (ABD istihdamının yalnız %4'üne karşın) — aşırı temsil, ama bu üst kategori (matematikçiyi değil "computer and mathematical" grubunu, örn. yazılımcıları da kapsar) ile sınırlı. Rapor "en düşük-özerklik çıktıları matematik/hesaplama, çeviri ve S&C'dir" diyor (D, kısa alıntı: "math or calculations, translations, and Q&As") — yani matematik görevlerinde Claude yüksek özerklikle (kendi başına karar verip ilerleme) değil, düşük özerklikle (insan yönlendirmesine bağlı) çalışıyor; bu bulgu hipotezle KISMEN ÇELİŞİYOR — "yönetme" senaryosu yüksek-özerklik AI + insan denetimi varsayar, oysa veri matematik görevlerinin hâlâ düşük-özerklik (insan adım adım yönlendiriyor) ucunda kaldığını gösteriyor. Rapor açık "augmentation vs automation" oranını matematik için ayrı vermiyor (K — genel metodoloji notu var, sayı yok).

**Microsoft "Working with AI" (2025)** (K — WebSearch özeti üzerinden, doğrudan açılmadı, https://www.microsoft.com/en-us/research/publication/working-with-ai-measuring-the-occupational-implications-of-generative-ai/, yazar Kiran Tomlinson, 2025-07): 200.000 Bing Copilot konuşması, O*NET IWA sınıflandırması. Bulgu: konuşmaların **%40'ında** kullanıcı hedefi ile AI eylemi tamamen farklı — AI çoğu zaman "koç/danışman" gibi davranıyor, kullanıcının görevini doğrudan yapmıyor. Matematikçiye özgü satır bu aramada görülmedi (bulunamadı). Araştırmacılar açıkça "iş kaybı" sonucu çıkarmamak konusunda uyarıyor (D-benzeri alıntı, ikincil özet).

**Genel kanıt durumu (§1):** Görev-düzeyinde matematikçiye özgü otomasyon/artırma oranı **doğrudan ölçülmüş olarak bulunamadı**; en yakın veri "computer and mathematical" üst kategorisi (Anthropic) ve genel LLM-exposure metodolojisi (Eloundou). Bu, alt soru 1'in "hangi görevler otomasyona/artırmaya gidiyor" kısmını **kesin cevaplayamıyor** — hipotez sınamasını doğrudan görev verisiyle değil, dolaylı kanıtla (aşağıdaki §2-4) yapmak zorunda kalıyoruz.

---

## 2. Matematikçilerin kendi tarifleri

**Terence Tao, ICM 2026 (Proceedings için makale + 2026-07-24 halka açık konuşma), "Mathematics in the age of AI"** (D — arXiv HTML doğrudan açıldı, https://arxiv.org/html/2608.16753v1 = arXiv:2608.16753, AS-OF 2026-08): Tao matematiksel problem çözmeyi üç aşamaya ayırıyor: **üretim (generation)**, **doğrulama (verification)**, **sindirim (digestion — anlama, bağlamlama, açıklama)**. AI ilk aşamada iyi, ikincide ilerliyor, üçüncü aşama "AI araçlarının optimize etmesine EN AZ elverişli aşama" (paraphrase). Kritik alıntı: biçimsel doğrulanmış kanıt "artık yazarının itibarına ya da özenine bağlı değildir" (D, ≤15 kelime paraphrase-alıntı karışık). Tao ayrıca "hiçbir insanın yeterince anlamadığı doğrulanmış bir kanıt" kabul etmeme uyarısı yapıyor. Önerdiği ölçüt: yazarlar sonuçları hakkında net, uzman-düzeyi bir konuşma **yapamıyorsa** yayımlanmamalı. **Tao'nun insan rolü tanımı**: küratörlük, açıklama, sentez — bireysel başarıları kolektif anlayışa çevirme. Bu, hipotezdeki "yönetim" kelimesinden daha spesifik: Tao "yönetici" demiyor, "küratör/sindirici/açıklayıcı" diyor.

**25 Fields Madalyalısı deklarasyonu, "A Severe Misalignment of AI in Mathematics"** (D — doğrudan açıldı, https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/, yayım 2026-09-11, 2026-09-16 itibarıyla 7.200+ imzacı — K, ikincil kaynaktan sayı: https://cryptobriefing.com/fields-medal-winners-ai-mathematics-misalignment/). İmzacılar arasında Tao, Peter Scholze, 2026 Fields madalyalısı Yu Deng (K, ikincil kaynak listesi). Deklarasyon tarihlemesi: OpenAI'nin ~10.000 ajanla Navier-Stokes özel-durum sonucunu duyurmasından **3 gün sonra** yayımlandı (K, ikincil kaynak). Merkezi argüman: matematiğin amacı "artan bir doğru-cevap yığını üretmek değil, anlayış ve bu anlayışın gelecek kuşaklara aktarılmasıdır" (paraphrase). Doğrudan alıntı: "problem çözmek yalnızca kavramsal anlayışa ulaşmak için bir araç ve vekildir" (paraphrase, orijinal İngilizce daha uzun). İnsan rolü tanımı — aktarım zincirinin taşıyıcısı: "istekli matematikçiler olmadan AI'ın ürettiği fikirler matematik kanonuna asla tam olarak girmez" (paraphrase). Endişe: hız (AI şirketleri sonuçları topluluğun doğrulama kapasitesini aşan hızda duyuruyor), atıf/intihal riski, eğitici değerin kaybı.

**MIT Technology Review, OpenAI Navier-Stokes tartışması (2026-09-08)** (D — doğrudan açıldı, https://www.technologyreview.com/2026/09/08/1143747/what-openais-latest-controversy-tells-us-about-the-future-of-math/): OpenAI'nin dahili sistemi Navier-Stokes özel-durumunu günler içinde çözdü ama **10.000 eşzamanlı ajan** ve "milyonlarca dolar" maliyetle; buna karşın NYU'lu Tristan Buckmaster ve Anthropic çalışanı Levent Alpöge benzer sonuca ~1 yılda halka açık modellerle ulaşmıştı ve atıf tartışması çıktı (K — ikincil habercilik, isimler ve olay örgüsü çapraz doğrulanmadı, tek kaynak). Tao'dan alıntı (paraphrase): problemler çoğu zaman çözümün kendisi için değil, çözüm arayışının doğurduğu yeni matematik dalları için önemlidir; özel şirketlerin "başarısız denemeleri" gizlemesi bu gelişim sürecini kesintiye uğratır.

**Akshay Venkatesh, "Human Mathematics in the Age of Reasoning Machines"** (D — PDF doğrudan açıldı ve ilk 10 sayfası okundu, https://www.math.ias.edu/~akshay/research/HumanMath.pdf, tarih PDF üzerinde görünmüyor — AS-OF erişim 2026-09-21, Harvard Ahlfors dersinin genişletilmiş hâli): Venkatesh "yönetici/orkestratör" terimini kullanmıyor; odağı **kavramların psikolojik/bilişsel işlevi**. Ana tez: "mekanik akıl yürütme yalnız matematiği NASIL yaptığımızı değil, NE OLDUĞUNU değiştirecek" (paraphrase). AlphaProof örneği: Venkatesh kendi sayı-kuramı stratejisiyle (modulo-p indirgeme) AlphaProof'un stratejisini (modulo ab+1, birleşik modül) karşılaştırıyor — insan ve makine "farklı kavramsal ekonomiler" kullanıyor. Stephanie Dick'in AURA (OTTER'ın öncülü) çalışmasından alıntı: makineye devredilen kısım "matematik problemi hakkında değil, program davranışı hakkında" içgörü üretti (paraphrase) — bu, "AI'ı yönetmenin" kendi başına yeni bir zihinsel beceri (araç davranışını anlama) gerektirdiğine işaret ediyor, ama Venkatesh bunu düz "yönetim" olarak çerçevelemiyor; makalenin geri kalanı (§3 sonrası, bu koşumda okunmadı) kavram-dili değişimine odaklanıyor — kapsam dışı kaldı, **bulunamadı (tam metin)**.

**Kevin Buzzard, "Human mathematicians are being outcounterexampled" (2026-07-20)** (D — orijinal blog doğrudan açıldı, https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/): Üç örnek — Erdős Birim-Uzaklık sanısına ChatGPT karşı-örneği (Mayıs), 60 yıllık Grothendieck sorusuna Claude Fable 5 biçimsel çürütmesi (Temmuz), 100 yıllık Jacobian sanısına 3B polinom karşı-örneği (Temmuz). Merkezi iddia (paraphrase, ≤15 kelime alıntı): "karşı-örnek arama... AI'ın insandan şimdiden hızlı olduğu araştırma matematiği kısmı." Buzzard'ın insan rolü tanımı: **biçimsel önerme formülasyonu** ("eğer insanlar bir Lean ifadesinin sanının özünü yakaladığında hemfikirse, doğrulama bir triviyalite hâline gelir" — paraphrase) + **sonuçların yorumlanması/anlamının çıkarılması**. Bu, Buzzard'ı "insan = doğrulayıcı + problem-çevirici + anlam-çıkarıcı" konumuna yerleştiriyor — "yönetici" kelimesi geçmiyor ama fonksiyonel olarak yakın.

**Değerlendirme (§2 özet):** Hiçbir birincil metin "matematikçi = AI yöneticisi" ifadesini birebir kullanmıyor. Bulunan terimler: küratör/açıklayıcı/sentezleyici (Tao), aktarım-zincirinin taşıyıcısı (Fields deklarasyonu), problem-çevirici + doğrulayıcı + yorumlayıcı (Buzzard), kavram-tasarımcısı (Venkatesh, dolaylı). Bu terimler hipotezin "yönetim" iddiasını **kısmen destekliyor ama daraltıyor**: rol tek bir "yönetici" şapkası değil, en az dört ayrı fonksiyona (doğrulama, formülasyon, sindirim/açıklama, kavram-tasarımı) bölünmüş görünüyor.

---

## 3. Ortaya çıkan rol adları ve iş tanımları

### Rol adları tablosu

| Rol | Kurum | Görev cümlesi (paraphrase/kısa alıntı) | AS-OF | URL |
|---|---|---|---|---|
| Formal Verification Engineer | Harmonic | "Aristotle biçimsel akıl yürütme ajanını kullanarak üretim donanım/yazılımını doğrulama"; "scope requirements, define properties, execute formal proofs" | 2026-09-21 (ilan erişimi) | https://www.harmonic.fun/careers/ |
| Research Engineer, Formal Methods | Harmonic | Yazılım/donanım özelliklerini ifade etme ve kanıtlama yaklaşımları geliştirme; AI araştırmacılarıyla sistem eğitiminde işbirliği | 2026-09-21 | https://www.harmonic.fun/careers/ |
| Research Engineer, Technical Lead | Harmonic | RL teknikleriyle teorem-kanıtlamada ilerlemeye liderlik; "araştırma vizyonu geliştirme ve önceliklere göre icrayı yönetme" | 2026-09-21 | https://www.harmonic.fun/careers/ |
| Research Engineer (genel) | Harmonic | RL ile biçimsel yöntemleri bütünleştiren algoritmalar geliştirme (2026-04-07'de kaldırılmış ilan — K, ikincil kaynak Built In) | 2026-04-07 (ilan tarihi, ikincil) | https://builtin.com/job/research-engineering-lead-formal-methods/4775975 |
| Lean 4 Proof Engineer | Alignerr (ilan platformu) | Matematikçilerin ileri düzey argümanları Lean 4'te biçimselleştirmesi; uzaktan, $170-200/saat | 2026-09-21 | https://www.alignerr.com/jobs/d61fdffd-b1a1-4cf7-9eae-6c0e3d39df83 |
| Principal Engineer | Lean FRO | (K — yalnız başlık görüldü, görev cümlesi bu koşumda açılmadı) | 2026-09-21 | https://lean-lang.org/fro/about/ |
| Researcher / Senior Researcher | Epoch AI | "toplumun AI yeteneklerini ve yörüngelerini anlamasını geliştirme" | 2026-09-21 | https://epoch.ai/about/careers |
| Software Engineer, Benchmarking | Epoch AI | Sınır AI modellerini değerlendirme, yeni benchmark'lar geliştirme, altyapı bakımı | 2026-09-21 | https://epoch.ai/about/careers |
| Research Engineer/Scientist/AI Systems Engineer, RSI | OpenAI | Gerçek araştırma iş akışlarını otomatikleştirme, değerlendirme tasarımı (K — sayfa 403 verdi, yalnız başlıktan çıkarım, WebSearch özeti) | 2026-09-21 (erişim engelli) | https://openai.com/careers/research-engineer-research-scientist-ai-systems-engineer-rsi-san-francisco/ |
| (Gauss ürünü — rol adı yok) | Math, Inc. | Maryna Viazovska'nın 2022 Fields kanıtlarının (küre paketleme, 8/24 boyut) ~200K satır biçimsel doğrulaması (K, ikincil kaynak f4.fund) | 2026-03 | https://f4.fund/startups/math-inc |

**Not:** "autoformalization engineer" ve "AI evaluation researcher (math)" tam unvanları bu koşumda **birebir ilanla doğrulanamadı** — en yakın eşleşmeler yukarıdaki tablo (Formal Verification/Proof Engineer, Benchmarking, RSI). Bu iki spesifik unvan için: **bulunamadı** (X — model-hafızasında "duyulmuş" olabilir ama doğrulanmadı, yazılmadı).

---

## 4. Yazılım mühendisliğinden analoji

**Anthropic, "How AI is transforming work at Anthropic" (2025-12-02)** (D — doğrudan açıldı, https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic): 132 mühendis/araştırmacı anketi + 53 derinlemesine görüşme + Claude Code kullanım verisi (2025-08 civarı). Bulgular: bir mühendis kendini "net-yeni kod yazan değil, kod gözden geçiren/düzelten" olarak tanımlıyor, "1, 5 ya da 100 Claude" sorumluluğu taşıyor (paraphrase + kısa alıntı). Başka biri işinin "%70'inden fazlası gözden geçirme ve düzeltme" (paraphrase). Görev karmaşıklığı 5-puanlık ölçekte **3.2 → 3.8**'e çıktı; art arda araç çağrısı sayısı **%116 arttı** (9.8 → 21.2); insan müdahalesi transkript başına **%33 azaldı** (6.2 → 4.1 tur). "Denetim paradoksu": etkin AI gözetimi, tam da azalan uygulamalı kodlamayla aşınabilecek teknik becerileri gerektiriyor (paraphrase). Bir mühendis: becerilerin aşınması "AI'ı güvenle kullanma yeteneğim açısından sorunlu" (kısa alıntı).

**METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (2025-07-10)** (K — doğrudan açılmadı, WebSearch özeti, https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/): 16 deneyimli açık-kaynak geliştiricisiyle RCT; AI araçlarıyla geliştiriciler görevleri **%19 daha yavaş** tamamladı ama kendilerini **%20 daha hızlı** sandılar. Bu, "yönetme daha verimli" varsayımına doğrudan **karşı kanıt** — en azından tanıdık, olgun kod tabanlarında deneyimli geliştiriciler için mevcut (2025-erken) araçlarla. Yazarlar bunun genellenebilirliğini sınırlıyor (aşinalık + repo olgunluğu etkeni).

**Analoji matematiğe taşınabilir mi?** Kanıt YALNIZ Tao ve Fields deklarasyonu üzerinden dolaylı: her ikisi de "doğrulama/sindirim insanda kalır" diyor — bu, yazılımdaki "gözden geçirme/düzeltme" rolüne yapısal olarak benziyor (D-destekli benzerlik, ama doğrudan "matematikçi de mühendis gibi yönetici olacak" diyen birincil kaynak **bulunamadı**). METR'nin "yönetim algısı gerçek hızdan daha iyimser" bulgusu, matematik camiasının hız/atıf endişesiyle (Fields deklarasyonu, OpenAI/Navier-Stokes tartışması) tematik olarak örtüşüyor ama METR matematik değil yazılım geliştirme üzerine (K — analoji, doğrudan transfer değil).

---

## 5. Rol haritası (3 kova)

### Kova (i) — Ölçülmüş kayma (görev verisiyle, D)
- Yazılım mühendisliğinde ölçülmüş: görev karmaşıklığı artışı, araç-çağrısı artışı, insan-müdahale azalışı (Anthropic, 2025-12-02, D). **Matematik-özgü eşdeğeri bu koşumda bulunamadı.**
- Anthropic Economic Index: matematik görevleri düşük-özerklik ucunda (D) — bu aslında "insan hâlâ adım adım yönlendiriyor," tam-otomatik yönetim senaryosunun henüz gerçekleşmediğine işaret.
- METR: yazılımda AI-destekli hız algısı ile gerçek hız arasında ters yön (D, ama math değil).
- **Yetkinlik adayı:** biçimsel doğrulama (Lean/Aristotle/Gauss ilanlarıyla D-destekli, gerçek işe alım talebi var).

### Kova (ii) — Uzman öngörüsü (kim, ne zaman, URL; D birincil metin ama öngörü niteliğinde)
- Tao (2026-07-24/08, arXiv:2608.16753): insan rolü küratörlük/sindirim/açıklama; "en az AI-optimize edilebilir aşama" sindirim.
- Buzzard (2026-07-20, xenaproject.wordpress.com): insan rolü biçimsel önerme formülasyonu + sonuç yorumlama; karşı-örnek üretiminde AI zaten daha hızlı.
- 25 Fields Madalyalısı (2026-09-11, terrytao.wordpress.com): insan rolü aktarım-zinciri taşıyıcılığı + topluluk-onayı süreci; hız/atıf endişesi.
- Venkatesh (tarihsiz PDF, math.ias.edu): insan rolü kavram-tasarımı/bilişsel-ekonomi; "yönetim" çerçevesini kullanmıyor.
- **Yetkinlik adayları:** problem seçimi (Tao — hangi sorular "insan gelişimini teşvik eden" sorular), sindirim/sunum (Tao, Fields deklarasyonu), biçimsel doğrulama okuryazarlığı (Buzzard), kavram-tasarımı/yeni dil geliştirme (Venkatesh).

### Kova (iii) — Spekülasyon (X, kanıt yok ya da tek-kaynak ikincil habercilik)
- "Matematik mühendisi" adında tek, birleşik yeni meslek unvanının kendisi — bu koşumda hiçbir birincil kaynakta bu tam unvan bulunamadı; en yakın somut unvanlar parçalı (Formal Verification Engineer, Proof Engineer, Benchmarking Engineer).
- "AI'ı yönetmek" tek-fonksiyon iddiası — kanıt bunun yerine ≥4 ayrı fonksiyona (doğrulama, formülasyon, sindirim, kavram-tasarımı) işaret ediyor; hipotezin tekil "yönetici" çerçevesi kanıtla **daraltılıyor/parçalanıyor**.
- Sistem tasarımı yetkinliği (10.000-ajan koordinasyonu gibi) — yalnız MIT Tech Review'in tek ikincil haberinden (K), doğrudan bir "bu artık matematikçinin işi" beyanı bulunamadı.
- Sayısal modelleme+ML yetkinliği — bu koşumda hiçbir kaynakta doğrudan tartışılmadı (**bulunamadı**, alt soru 5'in listesindeki adaylardan biri ama kanıtsız).

---

## Görev-maruziyet tablosu

| O*NET görev (15-2021.00) | Maruziyet kanıbı | Kanıt | AS-OF | Not |
|---|---|---|---|---|
| Yeni ilke/ilişki geliştirme (üretim) | Yüksek — AI ilerliyor | Tao: "generation"da AI iyi (D) | 2026-08 | |
| Hesaplama/sayısal analiz uygulama | Yüksek | Eloundou genel LLM-exposure (D, occupation-özel değil) | 2023/2024 | Matematikçiye özgü satır bulunamadı |
| Araştırmayı yayma (rapor/makale) | Orta-Düşük (insanda kalıyor) | Fields deklarasyonu: topluluk-onayı süreci insanda (D) | 2026-09-11 | |
| Doğrulama (görev listesinde açık madde yok ama zımni) | Orta — AI ilerliyor ama insan hâlâ gerekli | Tao: verification "iyi ilerliyor" ama "hiç kimsenin anlamadığı" kanıt reddedilmeli (D) | 2026-08 | |
| Alanda bilgi güncel tutma / mentorluk | Düşük (insan-insan etkileşimi) | Fields deklarasyonu: "human transmission chain" (D) | 2026-09-11 | |
| Model geliştirme (matematiksel/istatistiksel) | Bulunamadı — doğrudan veri yok | — | — | Alt soru 5'teki "sayısal modelleme+ML" adayı kanıtsız kaldı |
| Şifreleme sistemleri tasarlama | Bulunamadı — bu koşumda taranmadı | — | — | |

---

## Açılan birincil kaynaklar (WebFetch ile GERÇEKTEN açıldı)

1. https://www.onetonline.org/link/summary/15-2021.00 — O*NET Mathematicians görev listesi (D)
2. https://www.anthropic.com/research/economic-index-june-2026-report — Anthropic Economic Index, Haziran 2026 (D)
3. https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/ — 25 Fields Madalyalısı deklarasyonu (D)
4. https://www.harmonic.fun/careers/ — Harmonic açık ilanlar (D)
5. https://www.math.ias.edu/~akshay/research/HumanMath.pdf — Venkatesh, "Human Mathematics in the Age of Reasoning Machines" (D, ilk 10 sayfa)
6. https://arxiv.org/html/2608.16753v1 — Tao, "Mathematics in the age of AI" (ICM 2026) (D)
7. https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic — Anthropic iç-çalışma raporu (D)
8. https://arxiv.org/abs/2303.10130 ve /abs/2303.10130v6 — Eloundou vd. "GPTs are GPTs" özeti (D, kısmi — tam tablo açılamadı)
9. https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/ — Buzzard'ın orijinal blogu (D)
10. https://epoch.ai/about/careers — Epoch AI açık ilanlar (D)
11. https://www.technologyreview.com/2026/09/08/1143747/what-openais-latest-controversy-tells-us-about-the-future-of-math/ — MIT Tech Review, OpenAI/Navier-Stokes tartışması (D)

## Bulunamadı / erişim engeli

- **arxiv.org/pdf/2303.10130** (Eloundou tam PDF) — WebFetch "corrupted/binary" içerik döndürdü; O*NET-15-2021 satırlı exposure tablosu bu koşumda doğrulanamadı. Bayrak: erişim engeli.
- **openai.com/careers/research-engineer-research-scientist-ai-systems-engineer-rsi-san-francisco/** — HTTP 403. Bayrak: erişim engeli.
- **"autoformalization engineer" / "AI evaluation researcher (math)"** tam unvanlı ilan — arandı, birebir bulunamadı.
- **Jeremy Avigad, "Mathematicians in the Age of AI" (2026-03-03, arXiv:2603.03684)** ve **Commelin/Jamnik/Ochigame/Taelman/Venkatesh, "Shaping the Future of Mathematics in the Age of AI" (Notices AMS 2026, arXiv:2603.24914)** — yalnız WebSearch'te başlık/özet görüldü, WebFetch ile AÇILMADI (zaman/kapsam kısıtı, ≥5 kotası zaten karşılandığı için bu koşumda atlandı). Antitez ya da sentez ajanı bu iki kaynağı açabilir.
- Emily Riehl, Michael Harris, Tim Gowers'ın 2025-2026 spesifik yazıları — bu koşumda hiç aranmadı/açılmadı (kapsam dışı kaldı, zaman kısıtı).
- Matematikçiye özgü (15-2021 satırı) Microsoft "Working with AI" occupation-düzeyi veri — WebFetch yapılmadı, yalnız WebSearch özeti kullanıldı (K seviyesinde kaldı).
- Lean FRO "Principal Engineer" ilanının tam görev cümlesi — yalnız başlık görüldü, içerik açılmadı.

---

**Epistemolojik not:** Bu rapor 2026-09-21 itibarıyla erişilebilen kanıtın bir anlık görüntüsüdür. Hipotez ("AI matematiği yönetmek" = tek fonksiyon) kanıtla kısmen DARALTILDI: birincil metinler (Tao, Buzzard, Fields deklarasyonu) insan rolünü tekil "yönetim" yerine en az dört ayrı fonksiyona (doğrulama, formülasyon/çeviri, sindirim-açıklama, kavram-tasarımı) bölüyor; iş ilanları ("Formal Verification Engineer," "Proof Engineer") bu fonksiyonlardan yalnız birini (doğrulama/biçimsellştirme) somut, işe-alınabilir bir rol olarak yansıtıyor — "yönetici" unvanı iş piyasasında bulunamadı.
