# Araştırma Raporu — AI ve Matematik Araştırması, Eylül 2026 Durumu (Atlas TEZ, Aile C)

**Çekim tarihi (AS-OF):** 2026-09-21
**Ajan:** Atlas TEZ (aile C, bağımsız koşum)
**Hedef:** Lisans bitirme tezi (1 akademik yıl, tek öğrenci, matematik mühendisliği) ölçeğinde çalışılabilir AI+matematik açık problem/araç alanlarının haritası.

Etiket anahtarı: **D** = birincil kaynaktan doğrulandı · **K** = ikincil kaynak/arama özetiyle kısmi doğrulandı · **X** = doğrulanamadı/çelişkili/spekülatif.

---

## 1. Kilometre taşları (2025-09 → 2026-09)

- **IMO 2025 (2025-07-21), altın madalya eşiği — D.** Google DeepMind, Gemini Deep Think'in gelişmiş bir sürümüyle 6 sorudan 5'ini çözüp 42 üzerinden 35 puan aldığını duyurdu; süreç uçtan uca doğal dilde, 4.5 saatlik yarışma süresi içinde, insan müdahalesi olmadan işledi. IMO Başkanı çözümleri "açık, hassas" olarak nitelendirdi. Kaynak: [DeepMind blog](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/) (AS-OF 2025-07-21, WebFetch ile açıldı).
  - Karşılaştırma (D, aynı kaynak): 2024'te AlphaProof + AlphaGeometry 2, problemleri önce Lean'e çevirmek için uzman gerektiriyordu, 2-3 gün hesaplama sürüyordu, gümüş seviyesinde (28/42, 4 problem) kaldı.
  - **OpenAI de aynı gün (2025-07-21) 35/42 ile altın eşiğine ulaştığını duyurdu — K** (arama özeti, WebFetch ile ayrıca doğrulanmadı; bağımsız kaynak: TechCrunch/Zvi Substack başlıkları).
  - **Harmonic'in Aristotle sistemi, Lean 4'te BİÇİMSEL doğrulanmış çözümlerle 5/6 problemi çözerek altın-eşdeğeri sonuç bildirdi — K** (arXiv 2510.01346 ve 2507.15855 başlık/özetleri arama sonucundan; PDF doğrudan açılmadı). Aristotle'ı diğerlerinden ayıran nokta: doğal dil değil, doğrudan Lean 4 kanıt arama (Monte Carlo Graph Search) + geometri çözücü kombinasyonu.
- **IMO 2026 (Şangay, 2026-07 sonu), "mükemmel skor" iddiası — K, doğrulama sınırlı.** Çin şirketi RedNote'un (Xiaohongshu) `dots-note-3.0` modelinin 6 sorunun tümünü çözerek 42/42 aldığı bildiriliyor (SCMP, Rohan Paul/X, Zamin.uz — hiçbiri WebFetch ile birincil açılmadı, yalnız WebSearch özeti). **Çelişki bayrağı:** bir başlık ("Four AIs Scored a Perfect 42/42 on IMO 2026") 2026 IMO'da BİRDEN FAZLA modelin mükemmel skor aldığını ima ediyor; bu makale açılmadı, sayı teyit edilemedi — **X, Salih'e sorulmalı / ek doğrulama gerekir.**
- **Erdős problemleri — D (Quanta Magazine, WebFetch ile açıldı, AS-OF 2026-08-03).** Thomas Bloom'un erdosproblems.com veritabanına göre makale yayım tarihinde (2026-08-03) 565 problem "çözüldü", 652'si açık. OpenAI 2026-05-20'de birim-mesafe (unit distance) sanısını çürüttüğünü duyurdu, 2026-08-01'de 10 ek ilerleme iddia etti. Google DeepMind toplam 13 problemde ilerleme bildirdi (4 yeni çözüm + 9 daha önce bilinen ama unutulmuş çözümün yeniden keşfi). Kullanılan araçlar: GPT-5.2 Pro, Gemini, Aristotle (Harmonic). **Önemli kısıt (D, aynı kaynak):** Bloom'un kendi uyarısı — üretilen bazı makaleleri "hiçbir insan okumadı"; doğrulama sorunu açık; bazı kullanıcılar zaten çözülmüş problemleri "çözdüm" diye yanlış bildirdi.
  - Erdős Problem #1196 (asal küme büyüklüğü), 2026-05, Terence Tao'nun da dahil olduğu ekip — **K** (WebSearch özeti, ayrı doğrulanmadı).
- **FrontierMath / Epoch AI — D (iki sayfa WebFetch ile açıldı).**
  - `FrontierMath Tiers 1-3 (v2)`: 2026-06-12'de yeniden yayımlandı; 295 problem (Tier 1-3) + 43 problem (Tier 4) = 338 toplam; v2, Tier 1-3'te 123, Tier 4'te 12 hatalı problemi düzeltti, sırasıyla 5 ve 7 problem çıkarıldı. Sayfada canlı model skoru YOKTU (2026-09-21 itibarıyla). Kaynak: [Epoch AI FrontierMath Tiers 1-3 v2](https://epoch.ai/benchmarks/frontiermath-tiers-1-3-v2).
  - GPT-5 için ~%25, o4-mini için ~%20 skor iddiası yalnız arama özetinde geçti, WebFetch ile doğrudan sayfada teyit edilmedi — **K**.
  - `FrontierMath Erdős`: 2026-09-01'de duyuruldu (yani bu rapordan 20 gün önce); 652 açık Erdős probleminin ~%10'unu (68 problem) kapsıyor; Lean'de biçimsel kanıt/çürütme isteniyor, problem başına 300$ ve 72 saat bütçe sınırı var. **Sonuç (D):** yalnız GPT-6 Astra biçimsel koşuda 2/68 (%3) çözdü; ek gayri-resmi denemelerle toplam 5 çözüme ulaşıldı; GPT-5.6 Sol, GPT-5.5, Claude Fable 5.1, Claude Fable 5 dahil diğer TÜM test edilen modeller %0 aldı. Kaynak: [Epoch AI — Announcing FrontierMath Erdős](https://epoch.ai/latest/announcing-frontiermath-erdos) (AS-OF 2026-09-01).
- **Biçimsel kanıtlayıcı rakip modeller (K, arama özetiyle):**
  - DeepSeek-Prover-V2-671B (arXiv 2504.21801, 2025-04): MiniF2F-test %88.9 pass, PutnamBench 658 problemden 49'unu çözüyor. Açık kaynak (Hugging Face `deepseek-ai/DeepSeek-Prover-V2-671B`).
  - Goedel-Prover-V2 (arXiv 2508.03613, 2025-08): 32B model MiniF2F'te pass@32 %88.1, 2 tur hata-düzeltmeyle %90.4; rakiplerden "80× daha küçük" model iddiasıyla state-of-the-art.
  - Kimina-Prover: 72B/8B/70B varyantları, bazı konfigürasyonlarda MiniF2F %92.2.
  - AxiomProver (Axiom Math), 2026 başı: Putnam 2025'in tüm problemlerine Lean-doğrulanmış çözüm ürettiğini iddia ediyor (arama özeti, doğrudan açılmadı) — **X, tek kaynaklı iddia, teyit gerekir.**
- **"AI matematikçi" iddiaları — K.** "AI Mathematician: Towards Fully Automated Frontier Mathematical Research" (arXiv 2505.22451, 2025-05) başlığı bulundu ama içerik açılmadı. Leiden Declaration on AI and Mathematics adlı bir bildirge var (leidendeclaration.ai) — muhtemelen alan topluluğunun ortak tutum belgesi; içerik açılmadı, yalnız başlık düzeyinde not.

## 2. Biçimsel doğrulama ekosistemi (Lean 4 / Mathlib)

- **Mathlib boyutu — D (leanprover-community.github.io/mathlib_stats.html, WebFetch, AS-OF sayfa çekim tarihi 2026-09-21, sayfanın kendi güncelleme tarihi görünmedi).** 288.718 teorem, 136.941 tanım, 772 katkıcı. **Dikkat:** WebSearch özeti farklı (daha eski) rakamlar verdi — "2025-05 itibarıyla 210.000+ teorem, 100.000+ tanım", "1,2M satır kod, 1.200+ katkıcı" (gitnux.org / lean-lang.org kaynaklı, WebFetch ile açılmadı) — **K, çelişkili, resmi istatistik sayfası (D) daha güncel/güvenilir kabul edildi.**
- **Mathlib 2026'da Demailly Ödülü (açık bilim) aldığı iddiası — K**, tek kaynaklı arama özeti, doğrudan açılmadı.
- **Açık veri setleri/benchmarklar (D + K karışık):**
  - miniF2F: 488 problem, IMO/AIME/AMC ve ders kitabı kaynaklı — **K**.
  - PutnamBench — **D, iki farklı sayfa WebFetch ile açıldı, rakamlar arasında hafif tutarsızlık var:**
    - arXiv özet sayfası (2407.11214, açılan): 1.692 el-yapımı biçimlendirme, 640 teorem, Lean 4 + Isabelle tümünde, Coq'ta "önemli bir alt küme".
    - GitHub reposu (trishullab/PutnamBench, açılan): 1.724 biçimlendirme; Lean 4 (672), Isabelle (640), Coq (412); Lean4/Isabelle Apache 2.0, Coq MIT lisanslı; gayrı-resmi ifadeler MAA izniyle. 1962-2025 kapsıyor.
    - **Sapma nedeni muhtemelen sürüm farkı** (arXiv makalesi ilk sürüm, GitHub canlı/güncel) — teze başlarken GitHub sürümü esas alınmalı.
  - ProofNet: lisans-düzeyi matematik, Lean 3 hedefli autoformalization — **K**, tek arama özetinden.
- **Araçlar — D (github.com/lean-dojo/LeanCopilot, WebFetch ile açıldı).** MIT lisanslı, açık kaynak. GPU **isteğe bağlı** ("Optional (recommended if you have a CUDA-enabled GPU)") — CPU'da da çalışabiliyor, tek-GPU/laptop ölçeğine uygun görünüyor. Linux/macOS/Windows/WSL destekleniyor. Git LFS ve (kaynaktan derlemek isteyenler için) CMake≥3.7 + C++17 gerekiyor; çoğu kullanıcı için "önceden derlenmiş sürüm" indiriliyor, derleyici gerekmiyor. Sayfada net bir "son güncelleme tarihi" gösterilmedi, yalnız 939 commit sayısı görüldü — **kesin AS-OF veremiyorum, tarih X.**
  - LeanDojo-v2: uçtan uca eğitim/değerlendirme/dağıtım çerçevesi — **K**, arama özetinden, doğrudan açılmadı.
- **Autoformalization genel durumu — K.** Birden fazla 2026 tarihli arXiv makalesi bulundu (ProofBridge 2510.15681, Herald veri seti, Monotonic Reference-Free Refinement 2601.23166) ama hiçbiri WebFetch ile açılmadı; yalnız başlık/kısa özet düzeyinde bilgi var. Alan aktif ama net bir "çözüldü" iddiası yok.

## 3. AI kanıtını insana açıklama / çevirme hattı

- **Doğrudan birincil kaynak: arXiv 2607.07779 ("From Solvers to Research: LLM-Driven Formal Mathematics at the Research Frontier"), 2026-07-10, v1 — D, WebFetch ile açıldı.** Bu makale açıkça "proof explanation & interpretability"i bir AÇIK SORUN olarak listeliyor: biçimsel kanıtların NEDEN işlediğini anlama ve insan-okunur hale getirme konusunda büyük bir boşluk var; gayrı-resmi/biçimsel matematik arasındaki yorumlanabilirlik farkını kapatacak yöntemlere ihtiyaç olduğunu vurguluyor. Aynı makale, erişilebilir/lisans-ölçekli yönler olarak şunları öneriyor: biçimsel matematik öğreten etkileşimli LLM arayüzleri, rutin matematiksel görevler için benchmark veri setleri, insan-AI hibrit işbirliği modelleri, öğrenciler için etkileşimli kanıt-rafine sistemleri.
- **İlgili sistemler (K, arama özetinden, açılmadı):**
  - "Natural Language Translation of Formal Proofs through Informalization of Proof Steps and Recursive Summarization" (arXiv 2509.09726, 2025-09) — biçimsel kanıt adımlarını doğal dile çevirip özyinelemeli özetleme.
  - Visored — "Controlled-Natural-Language Prover for LLM-Generated Mathematics" (arXiv 2606.17581, 2026-06).
  - LeanTutor — "Verified AI Mathematical Proof Tutor" (arXiv 2506.08321, 2025-06).
  - ProofBridge — doğal dil ↔ Lean 4 ortak gömme (embedding) modeli, çapraz-modal erişim (arXiv 2510.15681).
- **Değerlendirme:** Bu hat, 2026-09 itibarıyla literatürde HENÜZ olgunlaşmamış, aktif ama dağınık bir alan — kesin bir "standart yöntem" yok; bu da lisans tezine uygun bir boşluk (aşağıdaki tabloya not edildi).

## 4. Uygulamalı matematik: PINN, nöral operatörler, sembolik regresyon

- **PINN/Nöral operatör anket makalesi — K (arXiv 2511.04576, "Physics-Informed Neural Networks and Neural Operators for Parametric PDEs: A Human-AI Collaborative Analysis"; ICAIS 2025 AI Track'e gönderilmiş, kendisi "alandaki ilk AI-işbirlikli anket" olduğunu iddia ediyor).** Doğrudan açılmadı, yalnız arama sonucu özeti. FNO'nun (Li ve ark., ICLR 2021) spektral yöntemle sıfır-atış süper-çözünürlük sağladığı; 2025-2026'da SC-FNO (Behroozi ve ark., ICLR 2025) gibi genişlemeler olduğu belirtiliyor.
- **Sembolik regresyon: PySR — K, arama özetinden.** Açık kaynak, Julia tabanlı `SymbolicRegression.jl` motoruyla Python arayüzü; evrimsel algoritma + gradyansız sabit-optimizasyonu ("Evolve-Simplify-Optimize" döngüsü). Lorenz çekicisi, doğrusal olmayan sarkaç, Lotka-Volterra gibi dinamik sistemlerde başarılı olduğu bildiriliyor. `gplearn`'den daha güvenilir, `Operon`'dan (C++) daha erişilebilir olarak konumlandırılıyor.
- **PINN + sembolik regresyon kombinasyonu — K, birden fazla 2025 makalesi bulundu, açılmadı:** kompozit plaka değerlendirmesinde (ScienceDirect, 2025), doğrusal olmayan PDE'lerin analitik yaklaşık çözümlerinde (Springer Neural Computing and Applications, 2025) PINN çıktısı + PySR ile kapalı-form denklem türetme. Bu, lisans tezi için doğrudan taklit edilebilir bir METODOLOJİK KALIP (aşağıdaki tabloya alındı).
- **Lisans/yüksek lisans tezi örneği bulundu mu?** Doğrudan "bu bir lisans tezidir" diye etiketlenmiş bir kaynak BULUNAMADI; yukarıdaki makaleler araştırma makalesi düzeyinde ama yöntem karmaşıklığı (PINN kur + PySR ile postprocess) bir lisans tezi kapsamına indirgenebilir niteliktedir — bu bir ÇIKARIM'dır, kaynakta açıkça "lisans tezi" denmiyor (**X** olarak işaretliyorum: iddia benim çıkarımım, kaynağın kendi iddiası değil).

## 5. Lisans-ölçekli somut proje kalıpları

Bkz. aşağıdaki tablo. Risk/hesaplama değerlendirmesi benim (Atlas TEZ) sentezimdir; literatür örneği verilenler kaynaklı, verilmeyenler benim çıkarımımdır ve öyle işaretlenmiştir.

---

## Lisans-ölçekli proje kalıpları tablosu

| Kalıp | Araç | Veri | Hesaplama ihtiyacı | Risk (1-2 satır) | Literatür örneği (URL) |
|---|---|---|---|---|---|
| miniF2F/PutnamBench alt-kümesinde açık-kaynak prover'ı (Goedel-Prover-V2 32B veya Kimina 8B) fine-tune/prompt-engineer edip yeni bir tactic/heuristic önerme | Lean 4, LeanCopilot (MIT, GPU isteğe bağlı), Hugging Face model ağırlıkları | miniF2F (488 problem), PutnamBench (GitHub, Apache/MIT) | Tek GPU yeterli olabilir (32B model quantize edilirse); CPU'da da LeanCopilot çalışabiliyor (D) ama yavaş | Var olan SOTA'yı geçmek zor; ölçülebilir küçük artış (ör. belirli problem sınıfında) daha gerçekçi hedef | [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613), [LeanCopilot](https://github.com/lean-dojo/LeanCopilot) |
| AI-üretimi Lean kanıtını doğal dile çevirip "okunabilirlik" ölçütüyle değerlendirme (insan matematikçi anketi ile) | LLM API (GPT/Claude), Lean 4 kanıt korpusu, basit bir informalization pipeline | Mathlib'ten seçilmiş kanıt alt kümesi (288.718 teorem, D) veya miniF2F çözümleri | Düşük — API çağrıları + küçük değerlendirme seti, GPU gerekmeyebilir | Alan (§3) HENÜZ olgunlaşmamış; ölçüt tanımlamak (ne "iyi açıklama"?) tezin kendisi kadar zor olabilir | [arXiv 2509.09726](https://arxiv.org/pdf/2509.09726) (Informalization + Recursive Summarization) |
| PySR ile bilinen bir PDE/ODE sisteminden (ör. Lotka-Volterra, sarkaç) veri üretip PINN çıktısını sembolik forma geri çevirme, gürültü dayanıklılığını test etme | PySR (açık kaynak, MIT benzeri), PyTorch/JAX PINN çerçevesi | Sentetik veri (simülasyonla üretilir, dışarıdan veri gerekmez) | Orta — PINN eğitimi için tek GPU yeterli; PySR CPU-yoğun ama laptop ölçeğinde çalışır | İyi bilinen bir kalıp, "yenilik" bulmak zor; küçük bir varyant (ör. yeni bir PDE sınıfı, gürültü modeli) gerekir | [Springer 2025 makalesi](https://link.springer.com/article/10.1007/s00521-025-11450-9) |
| Erdős problemleri veritabanından (erdosproblems.com) küçük/orta ölçekli AÇIK bir problemi seçip mevcut açık-kaynak prover + literatür-tarama LLM ile deneme; SONUÇ NE OLURSA OLSUN (çözülmese bile) metodolojiyi belgeleme | GPT/Claude API, Lean 4, erdosproblems.com yorum sistemi | erdosproblems.com (652 açık problem, D) | Değişken; çoğu deneme düşük maliyetli (API + CPU) ama doğrulama insan-emeği ister | YÜKSEK — Bloom'un kendi uyarısı (D, §1): üretilen kanıtları kimse doğrulamayabilir; tez'in kendisi yanlış-pozitif üretme riski taşır, danışman denetimi şart | [Quanta Magazine](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/) |
| FNO/nöral operatör ile klasik bir PDE (ısı, dalga, Burgers) çözücüsünü hızlandırma ve klasik sayısal yöntemle (FEM/FD) karşılaştırma | PyTorch, `neuraloperator` kütüphanesi (FNO referans implementasyonu) | Sentetik simülasyon verisi | Orta-yüksek — eğitim için GPU önerilir ama küçük 1D/2D problemlerde laptop GPU yeterli olabilir | İyi belgelenmiş bir alan, çok sayıda hazır kod var; "yeni katkı" bulmak gerekir (ör. belirsizlik ölçümü, hata sınırı) | [arXiv 2511.04576](https://arxiv.org/html/2511.04576v3) |
| FrontierMath Erdős tarzı küçük ölçekli bir "AI kanıt bütçesi" deneyi: belirli bir açık-kaynak prover'a problem başına zaman/token bütçesi koyup başarı oranı-maliyet eğrisini çıkarma | Açık kaynak prover (DeepSeek-Prover-V2 veya Goedel-Prover-V2), Lean 4 | miniF2F/PutnamBench alt kümesi | Orta — büyük modelse (671B) bulut/API gerekir, küçük varyant (7B-32B) tek GPU'da olur | Değerlendirme metodolojisi tekrarlanabilir olmalı; Epoch AI'nin 300$/72 saat protokolü doğrudan örnek alınabilir (D, §1) | [Epoch AI FrontierMath Erdős](https://epoch.ai/latest/announcing-frontiermath-erdos) |

---

## Açılan birincil kaynaklar (WebFetch ile GERÇEKTEN açıldı)

1. https://epoch.ai/benchmarks/frontiermath-tiers-1-3-v2 (AS-OF sayfanın kendi tarihi: 2026-06-12 güncelleme)
2. https://leanprover-community.github.io/mathlib_stats.html (çekim: 2026-09-21, sayfa güncelleme tarihi görünmedi)
3. https://epoch.ai/latest/announcing-frontiermath-erdos (AS-OF: 2026-09-01)
4. https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/ (AS-OF: 2025-07-21)
5. https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/ (AS-OF: 2026-08-03)
6. https://github.com/lean-dojo/LeanCopilot (çekim: 2026-09-21, sürüm tarihi görünmedi)
7. https://arxiv.org/abs/2407.11214 (PutnamBench özet sayfası; makalenin ilk sürümü 2024-07, GitHub'daki güncel veriyle hafif farklı)
8. https://github.com/trishullab/PutnamBench (çekim: 2026-09-21)
9. https://arxiv.org/pdf/2607.07779 (AS-OF: 2026-07-10, v1)

Toplam: **9 birincil kaynak GERÇEKTEN açıldı** (istenen minimum 4'ün üzerinde).

## Bulunamadı / erişim engeli

- https://arxiv.org/pdf/2407.11214 — PDF ikili (binary) içerik olarak döndü, metne çevrilemedi; `arxiv.org/abs/...` sayfasına dönülerek özet alındı (yukarıda #7). **Bayrak: PDF-parse engeli.**
- FrontierMath'te GPT-5 (~%25) ve o4-mini (~%20) skor iddiaları yalnız arama motoru özetinde geçti; Epoch AI'nin kendi sayfasında (WebFetch ile açılan) bu rakamlar GÖRÜLMEDİ — sayfa "erişim tarihi itibarıyla canlı leaderboard verisi yok" durumunda. **Bayrak: rakam kaynağı ikincil, doğrudan doğrulanamadı.**
- IMO 2026 "dört AI mükemmel skor aldı" başlığı (digitalapplied.com) açılmadı; RedNote/dots-note-3.0 dışındaki üç iddia teyit edilemedi. **Bayrak: sayısal çelişki, çözülmedi.**
- Aristotle/Harmonic'in IMO 2025 makaleleri (arXiv 2510.01346, 2507.15855) yalnız başlık/özet düzeyinde arama sonucundan alındı, WebFetch ile açılmadı.
- AxiomProver'ın "Putnam 2025'in tümünü çözdü" iddiası tek kaynaklı (arama özeti), doğrulanamadı.
- Leiden Declaration on AI and Mathematics (leidendeclaration.ai) ve "AI Mathematician" makalesi (arXiv 2505.22451) başlık düzeyinde bulundu, içerik açılmadı.
- Mathlib'in "Demailly Ödülü" aldığı iddiası tek kaynaklı, doğrulanamadı.

---

**Epistemolojik not:** Bu rapor 2026-09-21 çekim tarihli bir anlık görüntüdür. AI-matematik alanı bu dönemde hızla değişiyor (bkz. §1'deki 12 aylık kilometre taşı yoğunluğu); rapordaki rakamlar birkaç ay içinde eskiyebilir. Erdős problemleri hattındaki doğrulama sorunu (Bloom'un uyarısı, §1/tablo) özellikle ciddiye alınmalı — bir lisans tezi bu alanı seçerse, "AI çözdü" iddialarını KENDİ başına doğrulamadan kabul etmemesi gerekir.
