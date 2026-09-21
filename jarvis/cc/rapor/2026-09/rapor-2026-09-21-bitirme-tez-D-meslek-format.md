# Araştırma Raporu — Atlas TEZ (Aile D)

**Konu:** Matematik mühendisliği / uygulamalı matematik mesleğinin AI çağında ≈2036 formu + Türkiye'de matematik mühendisliği bitirme tezi biçim/kapsam kuralları + AI×matematik kesişiminde örnek lisans tezleri
**Çekim tarihi (AS-OF):** 2026-09-21
**Ajan:** Atlas — TEZ (aile D), bağımsız, tek-taraflı araştırma
**Disiplin notu:** Her iddia URL + AS-OF damgalı. Rakamlar kaynaklı; kestirim `[?]`. Model hafızasından (kesim ≤2026-01) gelen bilgi ayrı etiketlendi ve mümkün olduğunca canlı doğrulandı.

---

## 1. Meslek öngörüsü (WEF, BLS, Epoch AI, Anthropic, matematikçi görüşleri)

**BLS — Mathematicians and Statisticians (D, birincil, WebFetch ile açıldı):**
BLS Occupational Outlook Handbook sayfası şu anda **2025-2035** dönemini kapsıyor (sayfa son güncelleme: 2026-08-27). Genel meslek grubu için istihdam büyümesi "%10, ortalamadan çok daha hızlı" olarak veriliyor; ancak alt kırılımda **"mathematicians" (matematikçiler) için yalnızca %1 büyüme**, **"statisticians" (istatistikçiler) için %11 büyüme** projekte ediliyor. Yılda ortalama ~2.000 açık pozisyon, toplam net artış 3.400 iş (2025-2035). Sayfada AI/otomasyon etkisine dair açık bir ifade **yok** — büyüme gerekçesi veri artışı ve iş kararları olarak veriliyor.
Kaynak: https://www.bls.gov/ooh/math/mathematicians-and-statisticians.htm — AS-OF 2026-09-21 (sayfa tarihi 2026-08-27). D.

**WEF Future of Jobs Report 2025 (K, ikincil — ham PDF 10 MB sınırını aştığı ve digest sayfası 403 verdiği için doğrudan açılamadı, WebSearch özetleriyle çapraz doğrulandı):**
Rapor Ocak 2025'te yayınlandı, 1.000+ işveren / 14 milyon+ çalışan / 22 sektör / 55 ekonomiyi kapsıyor. "Big Data Specialists", "AI and Machine Learning Specialists", "Fintech Engineers", "Data Scientists" en hızlı büyüyen roller arasında **açıkça listeleniyor**; **"mathematician" (matematikçi) meslek adı en hızlı büyüyen/azalan listelerde ayrıca geçmiyor** — yani WEF taksonomisi matematikçiyi kendi başına bir kategori olarak izlemiyor, "data scientist"/"AI specialist" şemsiyesi altına düşüyor gibi görünüyor. "AI and big data" ve "analytical thinking" en hızlı yükselen beceri kategorileri arasında sayılıyor (rapor genel bulgusu; spesifik yüzde rakamı bu turda doğrulanamadı — `[?]`). İşyerlerinin %39'unun çekirdek becerilerinin 2030'a kadar değişeceği belirtiliyor.
Kaynak: https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf (erişim engeli: 10 MB limiti) + https://www.weforum.org/stories/2025/01/future-of-jobs-report-2025-the-fastest-growing-and-declining-jobs/ (WebSearch özeti) — AS-OF 2026-09-21, rapor yayın tarihi 2025-01. K (ikincil, PDF'in kendisi açılamadı; başlık/istatistikler arama motoru özetinden).

**Epoch AI — FrontierMath (D, birincil, WebFetch ile açıldı):**
FrontierMath, 70+ matematikçinin katkısıyla oluşturulan, 338 sorudan oluşan (Tier 1-4) bir AI matematik kıyaslaması; Tier 4 araştırma-seviyesi problemleri içeriyor ve bir soru genelde bir uzmana saatler-günler sürüyor. Sayfa doğrudan içerikte model performans zaman serisi vermiyor, ancak WebSearch üzerinden çapraz doğrulanan bir Our World in Data grafiği (ourworldindata.org/grapher/ai-frontiermath-over-time) modellerin zaman içindeki skorunu izliyor. Ayrı bir arama sonucuna göre **Tier 4'te 2026 Ocak itibarıyla 48 özel sorudan yalnızca 17'si tüm modeller tarafından toplamda çözülmüş** durumda — yani en zor katman büyük ölçüde doymamış.
Kaynak: https://epoch.ai/frontiermath — AS-OF 2026-09-21. D (benchmark tanımı) / K (Tier-4 17/48 rakamı, WebSearch özeti, doğrudan sayfada görülmedi, ikincil).

**Anthropic Economic Index (K, ikincil — WebSearch özeti; doğrudan WebFetch bu turda yapılmadı):**
"Computer and mathematical" meslek kategorisi Claude kullanımında ABD işgücündeki payının (~%4) çok üzerinde bir temsile (~%30 anket payı) sahip; enterprise API trafiğinin neredeyse yarısını oluşturuyor. Kullanım augmentation-ağırlıklı (%57 augment / %43 otomasyon) — yani matematik/yazılım işlerinde AI şu an büyük ölçüde "yardımcı", "yerine geçen" değil.
Kaynak: https://www.anthropic.com/economic-index — AS-OF 2026-09-21. K (ikincil, sayfa doğrudan açılmadı).

**Terence Tao — AI ve matematiğin geleceği (D, birincil, WebFetch ile açıldı — teorth.github.io/tao-web/ai-views.html):**
Tao'nun kendi derlediği görüş sayfasına göre matematikçilerin işi; problemi parçalara ayırma/yönlendirme, sonuçları doğrulama-anlamlandırma ve içgörü sağlama etrafında yeniden şekilleniyor. Yükselen yetkinlikler: üst-düzey stratejik düşünme, doğrulama/eleştiri ("red-team" işi), sunuş/özümseme, problem seçimi. Düşüş riski taşıyan: rutin hesaplama ve "sağlamlığı kanıtlanmış" ispat yazımı — ama Tao bunun öğrenciler için sabır/derin-öğrenme kaybı riski taşıdığını da vurguluyor. Ayrıca Mart 2026'da Tanya Klowden ile "Mathematical methods and human thought in the age of AI" başlıklı bir arXiv ön-baskısı yayınladı; Eylül 2026 tarihli ICM 2026 konuşma metni "Mathematics in the age of AI" (teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf) de aynı temayı işliyor (bu PDF bu turda ayrıca açılmadı, K).
Kaynak: https://teorth.github.io/tao-web/ai-views.html — AS-OF 2026-09-21. D.

**Kevin Buzzard / Mathlib Initiative (D/K karışık — WebSearch özeti, doğrudan WebFetch yapılmadı):**
Buzzard, 2025 Oxford Strachey Lecture'da "Will computers prove theorems?" başlıklı bir konuşma verdi; Mathlib (Lean kütüphanesi) yaklaşık iki milyon satır bilgisayar-doğrulanmış matematik içeriyor ve "Mathlib Initiative" AI-hızlandırmalı keşif çağında matematiğin titizliğini korumayı hedefliyor.
Kaynak: https://lims.ac.uk/event/ai-and-the-formalisation-of-mathematics/ , https://www.renaissancephilanthropy.org/insights/kevin-buzzard-and-alex-kontorovich-on-the-future-of-formal-mathematics-a-mathlib-initiative-interview — AS-OF 2026-09-21. K (ikincil, WebSearch özeti).

**Model-hafızası (doğrulanmadı) notu:** Kevin Buzzard'ın "Xena Project" ve "de Bruijn faktörü" (biçimsel/gayri-biçimsel ispat uzunluk oranı, tipik tahmin 4-10x) kavramı benim kesim-öncesi (≤2026-01) bilgimde de var; bu turda WebSearch ile "de Bruijn factor" tanımı ve genel aralığı çapraz doğrulandı (K, Wikipedia + leanprover-community arşivi), ancak Lean'e özgü **güncel sayısal değer bu turda birincil kaynaktan teyit edilemedi** — Tao'nun ai-views sayfasında "2023-24'te ~20 olan oranın düştüğü, 1'in altına inmesine 'temel bir engel olmadığı'" ifadesi geçiyor (D, doğrudan alıntı-yakın paraphrase, teorth.github.io kaynaklı).

---

## 2. Sektör talebi kanıtı (iş ilanları)

**Harmonic (D, birincil, WebFetch ile açıldı — harmonic.fun/careers):**
Eylül 2026 itibarıyla sayfada 9-10 açık pozisyon listeleniyor; matematik/formal-verification'a doğrudan bağlı olanlar: **Formal Verification Engineer** (Palo Alto, Londra — "verify production hardware and software with Aristotle"), **Research Engineer** (RL + formal theorem proving odaklı, birden fazla varyant: genel, Formal Methods, Technical Lead, Training & Inference). Şirket 2025 IMO'da (Uluslararası Matematik Olimpiyatı) Aristotle modeliyle altın-madalya seviyesi performans iddia ediyor (WebSearch özeti, K). Sayfada ilan tarihleri belirtilmiyor.
Kaynak: https://harmonic.fun/careers/ — AS-OF 2026-09-21. D (ilan listesi) / K (IMO iddiası, ikincil kaynaktan).

**Epoch AI (K, ikincil):** mathjobs.org üzerinde bir "Epoch AI" ilanı bulundu (https://www.mathjobs.org/jobs/3427) fakat bu turda içerik WebFetch ile açılmadı; ilan detayı doğrulanmadı — `[?]`.

**"Math Inc" (bulunamadı):** Bu isimde bir şirkete dair spesifik ilan bu turda WebSearch'te bulunamadı; genel "AI mathematics" arama sonuçları Indeed/ZipRecruiter'ın toplu ilan listeleme sayfalarına düşüyor, spesifik ilan ayıklanamadı.

**DeepMind / Anthropic / OpenAI / quant firmaları:** Bu turda bu şirketler için doğrudan "Lean" / "formal verification" / "mathematical reasoning" ilanı taraması yapılmadı (zaman/tur kısıtı) — **eksik kapsam, işaretlendi**. Model-hafızasından (doğrulanmadı): DeepMind'in AlphaProof/AlphaGeometry ekiplerinin ve OpenAI'nin matematik-akıl yürütme ekiplerinin var olduğu biliniyor ama güncel açık ilan bu turda teyit edilmedi.

---

## 3. Türkiye bitirme tezi biçimi (YTÜ, İTÜ)

**İTÜ Matematik Mühendisliği (D, birincil, WebFetch ile açıldı — matmuh.itu.edu.tr/egitim/lisans/bitirme-staj):**
Sayfa 4 şablon sunuyor: MAT4901 (TR), MAT4901E (EN), MAT4902/MAT492 (TR), MAT4902E/MAT492E (EN) — yani bitirme çalışması **iki dönemlik** (4901 + 4902 kod yapısı tipik olarak güz+bahar ayrımına işaret eder, ama bu **çıkarım**, sayfada açıkça "iki dönem" yazmıyor — `[?]`). Ayrıca bir "Matematik Müh. Tasarımı (Bitirme Çalışması)" komisyon mektubu şablonu var. Sayfa sayısı, jüri yapısı, "araştırma" vs "uygulama" ayrımı, yazılım/kod teslimi kabulü **bu sayfada açıkça belirtilmiyor**; sayfa, kapsamlı kurallar için "Fen-Edebiyat Fakültesi Bitirme Çalışması Teslimi Esasları" PDF'ine yönlendiriyor.
Kaynak: https://matmuh.itu.edu.tr/egitim/lisans/bitirme-staj — AS-OF 2026-09-21. D (var olan bilgi) / bulunamadı (detay kuralları).

**İTÜ Fen-Edebiyat Fakültesi belgeler sayfası (D, birincil, WebFetch ile açıldı — fe.itu.edu.tr/ogrenciler/belgeler):**
Aranan "Bitirme Çalışması Teslimi Esasları" PDF'i bu sayfada **doğrudan bulunamadı**; bunun yerine "Araştırma Projesi Sınav Tutanağı" (.doc) ve "Araştırma Projesi Başvuru Formu" (.docx) belgeleri mevcut — bunların bitirme süreciyle ilişkisi (aynı süreç mi, ayrı bir "araştırma projesi" dersi mi) bu turda **netleştirilemedi**.
Kaynak: https://fe.itu.edu.tr/ogrenciler/belgeler — AS-OF 2026-09-21. D (belgelerin varlığı) / bulunamadı (esaslar PDF'i).

**YTÜ Matematik Mühendisliği (bulunamadı — matematik bölümüne özgü yönerge):**
mtm.yildiz.edu.tr/duyurular sayfası WebFetch ile açıldı ancak bitirme tezi/projesine dair doğrudan bir duyuru/PDF **bulunamadı**. Bölümün "Yönetmelikler" ve "Formlar, Belgeler, Dilekçe" sayfalarına yönlendirme var ama bu turda ayrıca taranmadı.
Kaynak: https://mtm.yildiz.edu.tr/duyurular — AS-OF 2026-09-21. Bulunamadı.

**YTÜ genel format örneği (D, birincil — PDF gerçekten indirilip okundu, Elektrik-Elektronik Fakültesi):**
Matematik Mühendisliği'ne özgü olmasa da, **aynı üniversitenin** Elektrik-Elektronik Fakültesi "Bitirme Çalışması Yazım Kılavuzu" (2024-05 tarihli, sunucu dizin damgası) PDF'i açılıp okundu. Kılavuz şunu netleştiriyor: **bölüme göre çalışma adı değişiyor** — "Bilgisayar Mühendisliği Bölümünde Bitirme Projesi", "Elektronik ve Haberleşme Mühendisliği ve Elektrik Mühendisliği Bölümü'lerinde Bitirme Tezi veya Bitirme Projesi". Dış kapak **beyaz karton cilt** olmalı; kitap yapısı: dış kapak → iç kapak → ön sayfalar (içindekiler, şekil/tablo/sembol/kısaltma listeleri) → özet/abstract → tez metni (giriş/ana metin/sonuç) → son sayfalar (kaynaklar/ekler/özgeçmiş). Deneysel olmayan çalışmalarda dahi "Uygulama" bölümü zorunlu tutuluyor. Sayfa sayısı, jüri yapısı, yazılım teslimi konusunda **bu kılavuzda açık rakam/kural yok**. **Önemli sınır:** bu belge Matematik Mühendisliği'ne değil Elektrik-Elektronik Fakültesi'ne ait; Matematik Mühendisliği'nin YTÜ'de hangi fakülteye bağlı olduğu ve aynı şablonu paylaşıp paylaşmadığı bu turda doğrulanmadı — **analojiyle aktarılmamalı**.
Kaynak: https://elm.yildiz.edu.tr/sites/elm.yildiz.edu.tr/files/2024-05/bitirme-calismasi-yazim-kilavuzu.pdf — AS-OF 2026-09-21 (belge tarihi ~2024-05, dizin damgası). D (belge içeriği) ama alan-dışı örnek.

---

## 4. Örnek lisans/yüksek lisans tezleri (2023-2026), AI×matematik kesişiminde

| Tez | Kurum/Yıl | Seviye | URL | Etiket |
|---|---|---|---|---|
| "Physics-informed Neural Networks for Encoding Dynamics in Real Physical Systems" | Cambridge, Mühendislik Bölümü, Ocak 2024 | **MPhil (yüksek lisans)**, lisans değil | https://arxiv.org/pdf/2401.03534 | D — WebSearch ile başlık/kurum/tarih/URL doğrulandı, PDF'in kendisi bu turda açılmadı (K seviyesinde teyit) |
| ProofNet — Lean 4 versiyonu (Xin ve ark., 2024) — lisans-seviyesi matematik autoformalization | arXiv, 2024 | Araştırma makalesi (tez değil) | arXiv (spesifik ID bu turda not edilmedi) | K, WebSearch özeti |
| LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization | arXiv, 2026 | Araştırma makalesi | https://arxiv.org/pdf/2606.05400 | K, WebSearch başlığı görüldü, içerik açılmadı |
| Beyond the Library: An Agentic Framework for Autoformalizing Research Mathematics | arXiv, 2026 | Araştırma makalesi | https://arxiv.org/pdf/2606.31134 | K |
| U-MATH / UGMathBench (üniversite-seviyesi LLM matematik değerlendirme kıyaslamaları) | arXiv/ICLR 2025 | Araştırma makalesi (tez değil) | https://arxiv.org/pdf/2412.03205 | K |
| Berkeley EECS teknik raporu — "Benchmarking LLMs on Advanced Mathematical Reasoning" (Yue, Klein) | UC Berkeley, 2025 | **Teknik rapor / muhtemelen MS tezi** | https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-121.pdf | K, başlık/kurum görüldü, içerik açılmadı |

**Önemli bulgu:** Bu turda taranan kaynakların büyük çoğunluğu **arXiv araştırma makalesi**, üniversitelerin resmi tez arşivi kayıtları **değil** — yani "tez" etiketi çoğu satırda gevşek kullanılıyor; gerçek bir tez-deposu (ProQuest, üniversite repository) taraması bu turda yapılmadı, bu bir **kapsam boşluğu**.

**Türkiye'den örnek (YÖK Tez Merkezi):** Bu turda "Lean", "biçimsel doğrulama", "autoformalization" anahtar kelimeleriyle YÖK Ulusal Tez Merkezi'nde (tez.yok.gov.tr) **doğrudan eşleşen bir Matematik Mühendisliği lisans/yüksek lisans tezi bulunamadı**. Bulunan tek somut veri: 2017-2021 arası Bilgisayar Mühendisliği alanında yapay zeka konulu 84 yüksek lisans tezi olduğunu bildiren bir dergi makalesi (dergipark.org.tr/tr/pub/okufbed/article/1062622) — bu, Matematik Mühendisliği'ne özgü değil ve konuyu (Lean/AI×matematik) doğrudan kapsamıyor. YÖK'ün ayrıca bir "Yapay Zeka Akademik Tez Programı" başlattığı görülüyor (aa.com.tr haberi, K, 2026 civarı) ama bu programın Matematik Mühendisliği'ne özgü çıktısı bu turda doğrulanmadı. **Sonuç: Türkiye'den somut örnek bulunamadı** — YÖK Tez Merkezi arama arayüzü (tez.yok.gov.tr/UlusalTezMerkezi/tarama.jsp) gerçek zamanlı sorgu gerektiriyor, WebSearch/WebFetch ile indekslenmiş içerik sınırlı.

---

## 5. Tez tipleri taksonomisi

| # | Tip | Gerekli ön bilgi | Beklenen çıktı | Jüri açısından risk | Kaynaklı örnek / kestirim |
|---|---|---|---|---|---|
| i | Biçimselleştirme tezi (formalization) | Lean/Coq/Isabelle söz dizimi, tip kuramı, ilgili matematik alt-dalı | Formal kanıt deposu (Mathlib'e katkı ya da bağımsız proje) + doğal-dil rapor | Jüri Lean bilmiyorsa değerlendirme zorlaşır; "çalışıyor mu" kanıtı derleyici çıktısıyla nesnel ama "özgünlük" tartışmalı olabilir | D — Mathlib Initiative / Buzzard örneği (lims.ac.uk, K) gerçek emsal; Türkiye'de emsal bulunamadı |
| ii | Ölçme/benchmark tezi | İstatistik, deney tasarımı, LLM API kullanımı, ölçüt (metric) tasarımı | Yeni/uyarlanmış benchmark + model karşılaştırma sonuçları | Kıyaslama "kirlenmesi" (data contamination) riski; sonuçlar birkaç ay içinde eskiyebilir (hızlı model ilerlemesi) | D — U-MATH/UGMathBench (arxiv.org/pdf/2412.03205, K) doğrudan emsal |
| iii | Araç/yazılım tezi | Yazılım mühendisliği + matematik alan bilgisi | Çalışan araç/kütüphane (ör. autoformalization asistanı) + kullanıcı değerlendirmesi | "Bu bir tez mi yoksa yazılım projesi mi" tartışması; İTÜ'nün "Bitirme Projesi" vs "Bitirme Tezi" ayrımı (YTÜ kılavuzunda da görülen ayrım) burada devreye girer | D — YTÜ kılavuzu (elm.yildiz.edu.tr PDF) "Bitirme Projesi" adlandırmasını doğrudan destekliyor |
| iv | Uygulamalı-sayısal tezi (PINN, neural operator vb.) | PDE/sayısal analiz + derin öğrenme | Model + hata analizi + karşılaştırmalı sayısal sonuçlar | Klasik sayısal yöntemlerle adil kıyas yapılmazsa jüri itirazı riski yüksek | D — Cambridge MPhil PINN tezi (arxiv.org/pdf/2401.03534) emsal, fakat yüksek lisans seviyesinde |
| v | Kuramsal/analitik tezi | Klasik matematik (analiz, cebir, vb.) derinliği | İspat/teorem + AI'nin rolü (araç mı, konu mu) net ayrılmalı | AI'nin ispatı "üretmesi" ile öğrencinin "anlaması" arasındaki fark jüride tartışma konusu olabilir (Tao'nun "derin öğrenme kaybı" uyarısı, D, teorth.github.io) | K — doğrudan kaynaklı örnek bu turda bulunamadı, kestirim `[?]` |
| vi | Meta/sosyal-bilim tezi (AI'nin matematik mesleğine etkisi) | Bilim sosyolojisi/STS, anket metodolojisi, literatür taraması | Nitel/nicel etki analizi (bu raporun kendisi bu tipe örnek) | "Kanıt mı görüş mü" ayrımı yapılmazsa zayıf; WEF/BLS/Anthropic gibi kaynaklarla nicel temellendirme şart | D — bu raporda kullanılan WEF/BLS/Anthropic Economic Index kaynakları bizzat emsal teşkil ediyor |

---

## Açılan birincil kaynaklar (WebFetch ile gerçekten açılan/okunan)

1. https://www.bls.gov/ooh/math/mathematicians-and-statisticians.htm — BLS istihdam projeksiyonları
2. https://matmuh.itu.edu.tr/egitim/lisans/bitirme-staj — İTÜ Matematik Müh. bitirme şablonları
3. https://fe.itu.edu.tr/ogrenciler/belgeler — İTÜ Fen-Edebiyat Fakültesi belgeler sayfası
4. https://harmonic.fun/careers/ — Harmonic açık pozisyonlar
5. https://epoch.ai/frontiermath — FrontierMath benchmark tanımı
6. https://teorth.github.io/tao-web/ai-views.html — Terence Tao'nun AI görüşleri
7. https://mtm.yildiz.edu.tr/duyurular — YTÜ Matematik Müh. duyurular (bilgi bulunamadı ama sayfa açıldı)
8. https://elm.yildiz.edu.tr/sites/elm.yildiz.edu.tr/files/2024-05/bitirme-calismasi-yazim-kilavuzu.pdf — YTÜ EEE bitirme yazım kılavuzu (PDF indirilip 3 sayfası okundu; alan-dışı emsal)

**Toplam gerçekten açılan kaynak: 8** (kota: en az 4).

---

## Bulunamadı / erişim engeli

- **WEF Future of Jobs Report 2025 ham PDF** — WebFetch "maxContentLength 10485760 aşıldı" hatası verdi (dosya >10 MB). Digest sayfası (weforum.org/publications/.../digest/) **403 Forbidden** döndü. Bu iki kaynak yalnız WebSearch özetiyle (ikincil) temsil edildi.
- **YTÜ Matematik Mühendisliği'ne özgü bitirme tezi yönergesi** — bölüm duyurular sayfasında bulunamadı; "Yönetmelikler" ve "Formlar, Belgeler" alt-sayfaları bu turda ayrıca taranmadı (kapsam dışı bırakıldı, zaman kısıtı).
- **İTÜ "Fen-Edebiyat Fakültesi Bitirme Çalışması Teslimi Esasları" PDF'i** — matmuh.itu.edu.tr'nin yönlendirdiği belge, fe.itu.edu.tr/ogrenciler/belgeler sayfasında doğrudan bulunamadı; sayfada yalnızca "Araştırma Projesi" formları vardı, ilişkisi netleşmedi.
- **"Math Inc" şirketi** — bu isimde bir kuruluşa dair ilan/sayfa bulunamadı.
- **DeepMind / OpenAI / quant firmaları için spesifik "Lean"/"formal verification" ilanları** — bu turda taranmadı (kapsam boşluğu, sonraki tura bırakıldı).
- **YÖK Tez Merkezi'nde Matematik Mühendisliği + AI/Lean kesişiminde somut bir lisans/yüksek lisans tez kaydı** — bulunamadı; arama motoru indeksi tez.yok.gov.tr içeriğini yeterince kapsamıyor, canlı arayüz sorgusu gerekiyor.
- **Epoch AI mathjobs.org ilanı (mathjobs.org/jobs/3427)** — bulundu ama içerik bu turda açılmadı, `[?]`.
- **FrontierMath Tier-4 "17/48" rakamının birincil kaynağı** — epoch.ai/frontiermath sayfasında görülmedi; yalnız WebSearch özetinde geçti, ikincil kaynak.

---

**Epistemik not:** Bu rapor 2026-09-21 tarihli tek-turlu (TEZ, aile D) bir araştırmadır; antitez ajanı tarafından çapraz sorgulanacak şekilde tasarlandı. Belirsizlikler ve bulunamayan kalemler bilinçli olarak "bulunamadı" diye işaretlendi, doldurulmadı.
