# Bitirme tezi, revize 5: danışman özeti + ilk iki hafta planı (2026-10-19)

`[tip: rapor | kaynak: jarvis-terminal 10-19 | tarih: 2026-10-19 | hedef: raporlar/2026-10 | sema: v2 | koken: jarvis/claude-fable-5-1/2026-10-19]`

> **Bağlam:** 09-21 atlas raporu (`raporlar/2026-09/2026-09-21-bitirme-tezi-ai-matematik-atlas.md`) altı aile ve Ö1-Ö6 önerilerini çıkardı. 10-19 seansında arkadaşların getirdiği dört aday ve beşinci başlık tartışıldı; Salih'in seçimi **revize 5**, kendi dilimi **veri/algoritma**. Ekip: 1 arkadaş robotik (sabit), 1 arkadaş alan belirsiz, Salih robotik dışı. Güvenlik bileşeni yok (Salih şartı).
> **Kanıt durumu:** kaynaklar 10-19 canlı aramayla doğrulandı (AS-OF 2026-10-19); kestirimler `[?]`; araç adları model hafızasından olanlar "doğrulanmadı" damgalı. İTÜ çatısı MAT4901/MAT4902 atlas raporu aile D'den [D].

## A. Danışman özeti (tek sayfa)

**Başlık (TR):** Robot kol kontrolünde on-policy, off-policy ve model-tabanlı pekiştirmeli öğrenmenin tek protokolde kıyası: model-hatası sınırının deneysel sıkılığı ve eğitim kararlılığının istatistiksel ölçümü
**Title (EN):** A Unified-Protocol Comparison of On-Policy, Off-Policy and Model-Based Reinforcement Learning for Robotic Arm Control: Empirical Tightness of the Model-Error Bound and Statistical Training Stability

**Ekip:** 3 öğrenci, ortak tez, kişi başına ayrı teori ve sonuç bölümü. Çatı: İTÜ Matematik Mühendisliği bitirme (MAT4901 güz + MAT4902 bahar) [D].

**Tek paragraf:** Pekiştirmeli öğrenmenin üç ailesi (on-policy: PPO; off-policy: SAC; model-tabanlı: MBPO) simülasyondaki aynı robot kolda, aynı görevlerde, aynı örnek bütçesiyle ve aynı istatistik protokolüyle kıyaslanır. Kıyas iki matematiksel soruya bağlanır. Birincisi: model-tabanlı yöntemde ajanın öğrendiği fizik modelinin hatası politikanın gerçek performansına ne kadar mal olur; literatürdeki teorik sınır deneyde ne kadar sıkıdır? İkincisi: "kararlılık" eğitimin tohumdan tohuma tutarlılığı olarak tanımlanır ve güven aralıklı ölçülür. Çıktı: açık tezgâh + protokol, sınır-sıkılık tablosu, istatistiksel olarak savunulabilir kıyas, üç teori bölümü.

**Araştırma soruları:**
- **S1 Örnek verimliliği:** üç aile aynı görevlerde kaç ortam adımıyla hangi başarıya ulaşır; eğri uydurmayla "%80 başarı için N örnek" güven aralığı.
- **S2 Model-hatası sınırı:** Janner ve ark. (2019) "gerçek getiri ≥ model getirisi − C" sınırında C model hatası ve politika kaymasından oluşur; C_teorik robot kolun ufku ve ölçülen model hatasıyla hesaplanır, C_gözlenen ile kıyaslanır: sınır sıkı mı gevşek mi?
- **S3 Eğitim kararlılığı:** tohumlar arası varyans, ıraksama oranı, hiperparametre duyarlılığı; Agarwal ve ark. (2021) protokolü (çeyrekler-arası ortalama, bootstrap güven aralığı, performans profili).

**Neden özgün (canlı arama 10-19):** PPO/SAC kıyasları robot kolda var ve sonuç karışık (RMBench: iki tür benzer; iki elli görevde PPO büyük paralel simülasyonla SAC'ı geçiyor; Fetch kolda DDPG/TD3/SAC). Model-tabanlı aileyi aynı protokolde robot kola koyan çalışma **bulunamadı**. Sınırın deneysel sıkılığını robot kolda ölçen çalışma **bulunamadı**. Agarwal protokolü RL kıyaslarında hâlâ seyrek.

**Yöntem:**
- Ortak tezgâh: MuJoCo + Gymnasium-Robotics (Fetch kolu; Panda seçenek). Görevler: Reach (zorunlu), Push (hedef), PickAndPlace (koşullu `[?]`). Bozma takımı: kütle, sürtünme, gecikme.
- Algoritmalar: PPO (Stable-Baselines3), SAC (Stable-Baselines3), MBPO (mbrl-lib; model hafızası, doğrulanmadı).
- Protokol: tohum sayısı güç analiziyle seçilir (hedef 10, en az 5 `[?]`); eşit ortam-adımı bütçesi; değerlendirme 100 bölüm; rliable ile çeyrekler-arası ortalama + bootstrap güven aralığı + performans profili.

**Matematiksel içerik, üye başına:**
- **Üye R (robotik):** Lagrange dinamiği, Jacobian, sistem tanılama; öğrenilmiş dinamik modelin (topluluk ağı) çok-adımlı tahmin hatası; fizik-bilgili model varyantı.
- **Üye E (eğitim hattı):** MDP, politika gradyanı ve kırpılmış amaç (PPO), maksimum-entropi aktör-kritik (SAC), kısa hayali koşum şeması (MBPO).
- **Üye S (Salih, teori + veri):** (i) sınır türetmesi: Janner 2019 sınırının ufuk, indirim, model hatası ve politika kayması terimleriyle kol için sayısallaştırılması; (ii) varyans ayrıştırma: aileler arası fark ile tohum-içi varyansın bootstrap/ANOVA ile ayrılması; (iii) öğrenme eğrisi uydurma (lojistik ya da güç yasası) ve N-örnek güven aralığı; (iv) deney tasarımı: tohum sayısı güç analizi.

**Ölçütler:** başarı oranı · hedef hatası · %80 başarıya örnek sayısı · tohum varyansı · ıraksama oranı · model hatası (R) · sınır boşluğu C_teorik − C_gözlenen (S) · duvar-saati süresi.

**Takvim `[?]`:** Bitirme 1 (güz): tezgâh + üç aile Reach'te + sınır türetmesi + protokol v1. Bitirme 2 (bahar): Push + bozma takımı + tam tohum matrisi + sınır-sıkılık tablosu + yazım.

**Riskler ve çare:** MBPO 7 eklemde ağır → önce Reach, gerekirse eklem sayısı düşük görev. "Aileler arası fark yok" → sağlam istatistikle meşru bulgu (RMBench'in bulduğu da bu). Tohum bütçesi → güç analiziyle N. Sınır gevşek çıkarsa → bu da bulgu; Janner'ın kendi notu analizin kötümser olduğu yönünde. Hesaplama: orta GPU `[?]`; ücretsiz bulut tohum matrisi için yetmeyebilir.

**Danışmana sorular:**
1. Yazılım bileşenli tez MAT4901 şablonunda kabul mü?
2. Üç kişilik ortak tezde bölüm ayrımı ve bireysel değerlendirme nasıl?
3. Bölüm ya da laboratuvar GPU erişimi var mı?
4. "Stability analysis" terimi için eğitim kararlılığı yeterli mi, kontrol kararlılığı (Lyapunov) da bekleniyor mu?

**Kaynaklar (10-19 canlı):**
- Janner, Fu, Zhang, Levine (2019). When to Trust Your Model: Model-Based Policy Optimization. NeurIPS. arXiv 1906.08253.
- Agarwal, Schwarzer, Castro, Courville, Bellemare (2021). Deep RL at the Edge of the Statistical Precipice. NeurIPS. arXiv 2108.13264. Araç: rliable.
- RMBench (2022). Benchmarking Deep RL for Robotic Manipulator Control. arXiv 2210.11262.
- Chen ve ark. (2022). Towards Human-Level Bimanual Dexterous Manipulation with RL. arXiv 2206.08686.
- Off-Policy Deep RL Algorithms for Robotic Manipulator Tasks (2022). arXiv 2212.05572.
- Ng, Harada, Russell (1999). Policy invariance under reward transformations. ICML. (ödül şekillendirme kullanılırsa)

## B. İlk iki hafta planı (üç kişi)

**Gün 1, ortak (2 saat):** roller yazılı · tek git deposu, üç kişi klasörü + ortak `protokol/` · koşum kaydı şeması kararlaştırılır: `seed, algo, task, env_step, success, return, wall_s` (CSV) · haftalık 1 saat senkron günü.

| Hafta | Üye R (robotik) | Üye E (eğitim hattı) | Üye S (Salih, teori + veri) |
|---|---|---|---|
| 1 | MuJoCo + Gymnasium-Robotics kurulum · FetchReach'te rastgele politika koşumu · gözlem/eylem uzayı belgesi · bozma parametrelerinin (kütle, sürtünme) simülatörde yeri | Stable-Baselines3 kurulum · PPO ve SAC, FetchReach, 3 tohum × 200k adım `[?]` · öğrenme eğrileri CSV şemasıyla | Janner 2019 §4 okuma, sınır türetmesini kendi notasyonuyla 2 sayfa yeniden yazma · Agarwal 2021 okuma, rliable kurulum · oyuncak veride (Pendulum) çeyrekler-arası ortalama + bootstrap hattı |
| 1 `done` | `env_smoke.py` 1000 adım hatasız + 1 sayfa ortam belgesi | 2 algoritma × 3 tohum CSV + eğri grafiği | `sinir-turetme-v0.md` + `degerlendir.py` oyuncak veride çalışır |
| 2 | Dinamik model verisi (rastgele + E'nin politikasından geçişler) · tek-adım model eğitimi · çok-adımlı tahmin hatası eğrisi (1..H adım) | mbrl-lib kurulum · MBPO Pendulum/HalfCheetah smoke · FetchReach'e uyarlama girişimi | E'nin CSV'leri `degerlendir.py`'den geçer: ilk güven aralıklı tablo · tohum sayısı güç analizi · R'nin model hatasıyla ilk C_teorik · eğri uydurma denemesi |
| 2 `done` | model hata eğrisi grafiği + veri seti | MBPO 1 tohum koşuyor | protokol raporu v1 (2 sayfa) + ilk C_teorik sayısı |

**Hafta 2 sonu kapısı:** üç `done` tamam mı? Tamamsa 3. hafta danışman toplantısı (A bölümü + ilk grafikler). Değilse kayan dilim yazılı, toplantı ertelenmez; eksik "eksik" diye gider.

**Salih'in eli (CLAUDE.md pratik kuralı):** kurulum ve koşumlar Salih'in kendi makinesinde; Jarvis referans koşum yapmaz, `done` beyanı Salih'ten.

## C. Pointer
- Bu dosya: `jarvis/raporlar/2026-10/2026-10-19-bitirme-tezi-revize5-danisman-ozeti-ilk-iki-hafta.md`
- Adaylar ve tablo: 10-19 seans transkripti; özet hafıza notunda (`user-bitirme-tezi-matematik-muhendisligi.md`, Ek 1-5).
- Zemin: `raporlar/2026-09/2026-09-21-bitirme-tezi-ai-matematik-atlas.md` (Ö1-Ö6; §5 danışman görüşmesi adımları).
