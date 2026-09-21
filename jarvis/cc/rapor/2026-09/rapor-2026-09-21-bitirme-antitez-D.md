# Antitez Raporu D (¬D) — Bitirme Tezi İddia Listesi Çürütme Girişimi

**Rol:** Atlas ANTİTEZ ajanı, açık Devil's-Advocate — her iddianın (T) değilini (¬T) destekleyen kanıt arandı.
**Çekim tarihi (AS-OF):** 2026-09-21
**Yöntem:** Bağımsız web araştırması (WebSearch + WebFetch); tez raporu, gerekçesi, URL'leri görülmedi. Model-hafızası (kesim: 2026-01) yalnız ipucu olarak kullanıldı, hiçbir rakam hafızadan doğrulanmadan yazılmadı.
**Disiplin notu:** WEF'in ana rapor sayfaları (`weforum.org/stories/...`, `weforum.org/publications/.../digest/`) WebFetch'te `403 Forbidden` döndürdü; birincil PDF (`reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf`) WebFetch boyut sınırını (10 MB) aştığı için `curl` ile indirilip `pdftotext` ile metne çevrilerek birincil kaynaktan doğrudan alıntılandı (18.6 MB, HTTP 200). YTÜ bitirme kılavuzu PDF'i aynı yöntemle (curl+pdftotext) okundu; WebFetch ikili formatı doğrudan çözemedi.

---

## D1 — BLS mathematicians %1 / statisticians %11 (2025-2035)

**Çürütme girişimi:** BLS OOH sayfasının yalnızca birleşik "mathematicians and statisticians" kategorisi (%10) verdiği, ayrı meslek rakamlarının bulunmadığı ihtimali test edildi.

**Bulgu:** [BLS OOH — Mathematicians and Statisticians](https://www.bls.gov/ooh/math/mathematicians-and-statisticians.htm) sayfası "Job Outlook" tablosunda üç ayrı satır veriyor: Mathematicians **%1**, Statisticians **%11**, birleşik "Mathematicians and Statisticians" **%10** (2025-2035), yıllık ortalama ~2.000 açık pozisyon. Rakamlar iddiayla birebir örtüşüyor.

**Sonuç:** `ÇÜRÜTÜLEMEDİ`

---

## D2 — WEF Future of Jobs 2025: "data scientist" + "AI/ML specialist" var, "mathematician" ayrı listelenmiyor

**Çürütme girişimi:** WEF raporunun taksonomisinde "Mathematicians, Actuaries and Statisticians" adında bir meslek olup olmadığı ve "en hızlı büyüyen roller" tablosunda tam olarak "Data Scientist" ibaresinin geçip geçmediği arandı.

**Bulgu (birincil PDF, `curl`+`pdftotext` ile doğrudan okundu — [WEF Future of Jobs Report 2025 PDF](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf), s.19, Figure 2.2 "Top fastest growing jobs"):
Tam liste (15 meslek): Big Data Specialists, FinTech Engineers, AI and Machine Learning Specialists, Software and Applications Developers, Security Management Specialists, Data Warehousing Specialists, Autonomous and Electric Vehicle Specialists, UI and UX Designers, Light Truck or Delivery Services Drivers, Internet of Things Specialists, **Data Analysts and Scientists**, Environmental Engineers, Information Security Analysts, Devops Engineer, Renewable Energy Engineers.

- "AI and Machine Learning Specialists" tam adıyla listede (#3) — iddiayla birebir örtüşüyor.
- "Data Scientist" tek başına bir başlık **değil**; birleşik başlık "Data Analysts and Scientists" (#11) olarak geçiyor — iddia hafif gevşek ifade edilmiş.
- "Mathematicians, Actuaries and Statisticians" genel taksonomide (Table A3, "Computer and Mathematical" iş ailesi, s.103) meslek olarak **var**, ama bu 15'lik büyüme listesinde **yok** — iddianın "ayrıca listelenmiyor" kısmı doğrulandı.

**Sonuç:** `DARALDI: "data scientist" tam bu adla değil "Data Analysts and Scientists" birleşik başlığıyla geçiyor; "mathematician" büyüme top-15'inde doğrulandı biçimde yok (genel taksonomide var ama büyüme listesinde değil)`

---

## D3 — Epoch AI FrontierMath Tier 4: 48 özel sorudan 17'si (Ocak 2026)

**Çürütme girişimi:** Tier 4'ün toplam soru sayısının 48 değil 50 (kamuya açık 2 + özel 48) olabileceği, "17" rakamının başka bir tarihe/versiyona ait olabileceği test edildi.

**Bulgu:** [Epoch AI FrontierMath Tier 4 v1](https://epoch.ai/benchmarks/frontiermath-tier-4-v1) — Tier 4 toplam 50 problem, 2'si kamuya açık ("frontiermath-tier-4-2025-07-01-public"), **48'i özel** ("frontiermath-tier-4-2025-07-01-private") — yani "48 özel soru" ifadesi doğru okunmuş (48 = özel alt küme, toplam değil). [Epoch AI Substack — "New record on FrontierMath Tier 4"](https://epochai.substack.com/p/new-record-on-frontiermath-tier-4), yayın tarihi **2026-01-23**: "the pass@the-kitchen-sink for Tier 4 (all problems solved ever) is now 17/48 (35%)." GPT-5.2 Pro tek başına 15/48 çözdü, önceki rekor kümülatif olarak 13/48 idi, GPT-5.2 Pro 4 yeni soru ekledi → 17/48. Tarih ve rakam iddiayla birebir örtüşüyor.

**Sonuç:** `ÇÜRÜTÜLEMEDİ`

---

## D4 — Terence Tao: matematikçinin rolü problem seçimi/doğrulama/sunuma kayıyor

**Çürütme girişimi:** Tao'nun bu görüşü ifade ettiği birincil kaynağın (kendi web sayfası) bu iddiayı destekleyip desteklemediği doğrudan kontrol edildi; ikincil haber kaynaklarının abartma ihtimali test edildi.

**Bulgu:** [Terence Tao — "Tao on AI: a living summary"](https://teorth.github.io/tao-web/ai-views.html) (Tao'nun kendi GitHub Pages sayfası, birincil kaynak): matematikçilerin "routine proofs and calculations"tan uzaklaşıp "narrative-building and judging the promise of a new technique"e kayacağını, "breaking a problem into tractable pieces is where value lies" dediğini doğruluyor. AMS Notices makalesinde de beş aşama (proof generation, verification, exposition, publication, canonicalization) ayrımı var; AI ilk ikisinde ilerliyor, kalanı insan işi kalıyor.

**Sonuç:** `ÇÜRÜTÜLEMEDİ`

---

## D5 — Mathlib ~2 milyon satır

**Çürütme girişimi:** Rakamın "1.9 milyon" mu "2+ milyon" mu olduğu, hangi tarihe ait olduğu kontrol edildi.

**Bulgu:** [Lean Lang — Mathlib use case sayfası](https://lean-lang.org/use-cases/mathlib/) (birincil kaynak, Lean FRO): "With over two million lines of formalized mathematics, Mathlib has become one of the most extensive mathematical libraries available in any proof assistant." Sayfa tarih damgası taşımıyor (footer "© 2026 Lean FRO"), ama "iki milyon satır" ifadesi doğrudan doğrulandı. Diğer kaynaklar 1.9 milyon/210.000+ teorem gibi yakın rakamlar veriyor — rounding farkı, çelişki değil.

**Sonuç:** `ÇÜRÜTÜLEMEDİ`

---

## D6 — Harmonic: Formal Verification Engineer + Research Engineer ilanları (Eylül 2026)

**Çürütme girişimi:** İlanların hâlâ açık olup olmadığı, tarih damgası taşıyıp taşımadığı test edildi.

**Bulgu:** [Harmonic Careers](https://www.harmonic.fun/careers/) — bugün (2026-09-21) çekilen sayfada "Formal Verification Engineer" (Palo Alto, Londra) ve üç ayrı "Research Engineer" pozisyonu (Formal Methods; Technical Lead; RL & Formal Methods) dahil 9 mühendislik pozisyonu FULL TIME olarak açık listeleniyor (Ashby HQ üzerinden başvuru). Sayfada açık tarih damgası yok, ama AS-OF çekim tarihi itibarıyla ilanlar canlı.

**Sonuç:** `ÇÜRÜTÜLEMEDİ`

---

## D7 — Anthropic Economic Index: "computer and mathematical" ~%30 Claude kullanımı vs ~%4 işgücü

**Çürütme girişimi:** Kesin rakamların "~30/~4" yuvarlamasından belirgin şekilde saptığı, farklı rapor sürümlerinde farklı sayılar olabileceği test edildi.

**Bulgu:** [Anthropic — "Introducing the Anthropic Economic Index"](https://www.anthropic.com/news/the-anthropic-economic-index) (ilk yayın 2025-02-10, arXiv:2503.04761 tabanlı, ~1M Claude.ai konuşması): Claude kullanım payı **%37.2**, ABD işgücü payı **%3.4** — kesin rakamlar. [Anthropic Economic Index — Ocak 2026 raporu](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report): "computer and mathematical tasks... representing **a third** [~%33] of conversations on Claude.ai and nearly half [~%46] of 1P API traffic" — işgücü payı bu raporda ayrı yüzde olarak verilmiyor (eyalet-düzey korelasyon analizine geçilmiş).

**Sonuç:** `DARALDI: kesin oran rapor sürümüne göre %33-37.2 arasında değişiyor (Şubat 2025: %37.2, Ocak 2026: ~%33), "~%30" hafif düşük yuvarlama; "~%4" (%3.4, yalnız ilk rapor) doğru ama Ocak 2026 raporunda işgücü payı ayrıca verilmiyor`

---

## D8 — İTÜ Matematik Mühendisliği: MAT4901/MAT4902, 4 şablon (TR/EN)

**Çürütme girişimi:** Ders kodlarının güncel olup olmadığı, şablon sayısının gerçekten 4 olup olmadığı (2 değil) kontrol edildi.

**Bulgu:** [İTÜ Matematik Mühendisliği — Bitirme/Staj](https://matmuh.itu.edu.tr/egitim/lisans/bitirme-staj) sayfası MAT4901 ve MAT4902 kodlarını doğruluyor; 4 ayrı şablon listeleniyor: MAT4901 (TR), MAT4901E (EN), MAT4902/MAT492 (TR), MAT4902E/MAT492E (EN) — 2 dil × 2 ders = 4.

**Sonuç:** `ÇÜRÜTÜLEMEDİ`

---

## D9 — YTÜ EEF: bölüme göre "Bitirme Tezi" ya da "Bitirme Projesi"

**Çürütme girişimi:** Adlandırmanın gerçekten bölüme göre değiştiği mi yoksa tüm bölümlerde aynı mı olduğu, birincil kılavuz metninden doğrudan kontrol edildi.

**Bulgu:** [YTÜ Elektrik Mühendisliği — Bitirme Çalışması Yazım Kılavuzu PDF](https://elm.yildiz.edu.tr/sites/elm.yildiz.edu.tr/files/2024-05/bitirme-calismasi-yazim-kilavuzu.pdf) (curl+pdftotext ile doğrudan okundu), s.2, dış kapak talimatı: "Bilgisayar Mühendisliği Bölümünde **Bitirme Projesi**; Elektronik ve Haberleşme Mühendisliği ve Elektrik Mühendisliği Bölüm'lerinde **Bitirme Tezi veya Bitirme Projesi**." Birebir örtüşüyor.

**Sonuç:** `ÇÜRÜTÜLEMEDİ`

---

## D11 — YTÜ/İTÜ Matematik Mühendisliği'ne özgü AI/Lean odaklı bitirme yönergesi bulunamadı

**Çürütme girişimi:** Hedefli aramayla (Türkçe + İngilizce) böyle bir yönergenin var olup olmadığı arandı; ayrıca YTÜ Matematik Mühendisliği'nin bölüm sayfasının içerik taşıyıp taşımadığı doğrudan ziyaret edilerek test edildi.

**Bulgu:** Hedefli aramalar (`Türkiye matematik mühendisliği bitirme tezi yönergesi yapay zeka odaklı bölüm`, `YÖK Tez Merkezi yapay zeka matematik lisans tezi Lean formal verification Türkiye`) AI/Lean'e özgü bir yönerge döndürmedi — yalnızca genel "Yapay Zeka Akademik Tez Programı" (Savunma Sanayii ile ortak, disiplinler-arası) bulundu. [YTÜ Matematik Mühendisliği bölüm sayfası](https://matmuh.yildiz.edu.tr/) doğrudan ziyaret edildi: sayfa "Sayfa Hazırlanıyor..." mesajıyla **inşa halinde**, hiçbir bitirme/ders içeriği yok — bu, iddiayı zayıflatmak yerine güçlendiriyor (genel içerik bile yok, AI/Lean-özel içerik hiç yok).

**Sonuç:** `ÇÜRÜTÜLEMEDİ (ek kanıtla güçlendi: YTÜ Matematik Mühendisliği sayfası tamamen boş/inşa halinde)`

---

## D12 — Tao: de Bruijn faktörü ~20 (2023-24), düşüşte, 1'in altına engel yok

**Çürütme girişimi:** Rakamın "~20" değil farklı bir değer olabileceği, "düşüşte" ifadesinin abartı olabileceği birincil kaynaktan test edildi.

**Bulgu:** [Tao'nun kendi özet sayfası](https://teorth.github.io/tao-web/ai-views.html) (birincil kaynak): 2023-24 döneminde de Bruijn faktörü ilk hesaplaması **~20**, eğilim düşüş, sonuç: "no fundamental obstacle to falling below 1." İddiayla birebir örtüşüyor. **Ek nüans (iddiada yok, raporda not edilmeli):** aynı sayfa 2025-26 döneminde otomatik biçimselleştirmenin "essentially emptied the queue of unclaimed formalization tasks" dediğini de ekliyor — yani ölçütün kendisi hızla anlamını yitiriyor olabilir; bu iddiayı çürütmüyor ama güncelliğini sınırlıyor.

**Sonuç:** `ÇÜRÜTÜLEMEDİ (nüans: ölçütün kendisi 2025-26'da hızla eskiyor, ama ~20/düşüş/1-altı-engel-yok rakamları doğru)`

---

## EK-SORU-1 — Türkiye'de bitirme tezi/projesi kuralları web'de var mı? YÖK Tez Merkezi'nde AI×matematik örneği var mı?

**Bulgu:** İTÜ Matematik Mühendisliği için EVET — [bitirme-staj sayfası](https://matmuh.itu.edu.tr/egitim/lisans/bitirme-staj) ders kodları (MAT4901/4902) ve 4 şablonla birlikte web'de erişilebilir. YTÜ Matematik Mühendisliği için HAYIR — [bölüm sayfası](https://matmuh.yildiz.edu.tr/) "Sayfa Hazırlanıyor..." durumunda, hiçbir içerik yok; buna karşın YTÜ'nün Elektrik-Elektronik Fakültesi'nin (matematik mühendisliği değil) kendi kılavuz PDF'i var (D9). [YÖK Ulusal Tez Merkezi](https://tez.yok.gov.tr/UlusalTezMerkezi/) arama arayüzü konu/anahtar-kelime bazlı çalışıyor ve üyelik gerektirmiyor, ancak bu oturumda AI×matematik (Lean/formal verification) konulu spesifik bir lisans/yüksek lisans tezi örneği **doğrulanmadı** — yalnızca genel "yapay zeka" temalı 84 yüksek lisans tezinden oluşan bir derleme makalesi bulundu (dergipark.org.tr), doğrudan Tez Merkezi sorgusu bu oturumda çalıştırılmadı (arama motoru üzerinden metin arama yapıldı, Tez Merkezi'nin kendi arama formu doldurulmadı).

## EK-SORU-2 — AI çağında matematik mezunlarına talep ARTTIĞINA dair kanıt var mı?

**Bulgu:** EVET, güçlü kanıt var — ama BLS'in dar "mathematician" meslek koduna değil, komşu unvanlara (quant researcher, AI/ML research scientist, formal verification engineer) yansıyor. [PwC 2025 Global AI Jobs Barometer](https://youngandcalculated.substack.com/p/quant-finance-vs-ai-labs-where-the) üzerinden aktarılan veri: AI becerilerinde ücret primi 2024'te %25'ten 2025'te **%56**'ya çıktı; AI iş ilanları 2025'te yıllık **%78** arttı, nitelikli aday havuzu yalnız %24 büyüdü (~3.4 açık pozisyon/aday). Somut maaş verisi: Anthropic L5 araştırmacı $700-950k, OpenAI L5 mühendis ~$1.15M toplam paket, Meta üst-düzey paketler 4 yılda $300M'a kadar — quant finans üst düzey ($600k-$1.5M) ile karşılaştırıldığında AI lab'lerin matematik-yoğun PhD talebinde quant finansı geride bıraktığı görülüyor. Harmonic'in D6'da doğrulanan açık formal-verification ilanları da bu talebin somut bir örneği. Bu, D1'in BLS "mathematician" %1 büyüme rakamıyla gerilim içinde: dar meslek sınıflandırması, matematik becerisinin AI-bitişik unvanlara kayan gerçek talebini muhtemelen eksik yakalıyor.

---

## Özet Tablo

| İddia | Sonuç |
|---|---|
| D1 | ÇÜRÜTÜLEMEDİ |
| D2 | DARALDI |
| D3 | ÇÜRÜTÜLEMEDİ |
| D4 | ÇÜRÜTÜLEMEDİ |
| D5 | ÇÜRÜTÜLEMEDİ |
| D6 | ÇÜRÜTÜLEMEDİ |
| D7 | DARALDI |
| D8 | ÇÜRÜTÜLEMEDİ |
| D9 | ÇÜRÜTÜLEMEDİ |
| D11 | ÇÜRÜTÜLEMEDİ (güçlendi) |
| D12 | ÇÜRÜTÜLEMEDİ (nüanslı) |

**Açılan (WebFetch ile gerçekten okunan) kaynak sayısı:** 18 (bunlardan 2'si `curl`+`pdftotext` yoluyla, WebFetch'in doğrudan erişemediği ikili/büyük PDF'ler için). Başarısız denemeler: 4 (`weforum.org` 403 ×3, `ehm.yildiz.edu.tr` 404, `matematik.yildiz.edu.tr` DNS hatası — bunlar ana rapora dahil edilmedi, yalnız burada disiplin notu olarak kayıtlı).
