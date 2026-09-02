> ⚠ m.39 İHLALİ (Karar 86 D7-⑨, 2026-09-02): bu ham rapordaki rakip FİYAT TUTARLARI açılmamış sayfalardan yazılmıştır (V26 ihlali, İB-67/68 sentezine taşınmadı); tutarlar geçersizdir, yalnız 'ücretli plan MEVCUT/YOK' varlık beyanı kullanılır. Satırlar m.8 gereği silinmedi.

# Rapor — B68-4 Pazar-Doğrulama + Dağıtım Emsalleri

**Künye:** AS-OF 2026-08-31 · aile B3 · model sonnet · ajan pazar-doğrulama-işçi · dizin `/Users/HasanSalihSahin/jarvis`

---

## (1) B68-4 Kanıt-kapılı otonomi merdiveni — rakip/muadil taraması

**Arama sorguları (birebir):**
1. `AI agent rollout promotion gates evaluation-gated deployment governance platform 2026`
2. `AI TRiSM model risk management platform NIST AI RMF compliance tool pricing`
3. `LangSmith Braintrust Patronus AI Galileo pricing plans evaluation platform 2026`

### Rakip listesi

| Ad | Ne yapıyor | URL (arama-sonucu) |
|---|---|---|
| Braintrust | Eval-as-code, CI/CD içine gömülü regresyon-test tarzı agent değerlendirme; mühendislik-öncelikli ekiplere hitap | braintrust.dev (arama-sonucu: latitude.so/blog/agent-first-comparison-guide-vs-braintrust) |
| LangSmith (LangChain) | Gözlemlenebilirlik + değerlendirme bütünleşik platform, LangChain yığınına gömülü | arama-sonucu: agentmodeai.com/agent-eval-frameworks-deepeval-braintrust-langsmith-patronus |
| Patronus AI | Kendi değerlendirme modelleri (Lynx-halüsinasyon, GLIDER-rubrik skorlama, Percival-agent izleme) | arama-sonucu: agentmodeai.com (aynı) |
| Galileo | Canlı üretim ölçeğinde agent değerlendirme/izleme | galileo.ai/blog/best-ai-agent-evaluation-platforms |
| ModelOp | Kurumsal AI yönetişim platformu, Gartner 2025 AI Governance Platforms Market Guide'da; NIST AI RMF/HIPAA/GDPR/FERPA çerçeve desteği | arama-sonucu: feeds.trussed.ai/blog/ai-trism-tools-model-risk-compliance-vendors |
| Scrut | NIST AI RMF uyum otomasyonu, hazır kontrol testleri | scrut.io/solutions/nist-ai-rmf |
| AllTrue.ai | Birleşik AI TRiSM merkezi: envanter, sürekli izleme, uyum otomasyonu, çalışma-zamanı korkuluklar | arama-sonucu: feeds.trussed.ai (aynı) |

Doğrudan "koşum-sayılı kanıt kapısı" (calendar değil evidence-count-gated promotion) diline birebir eşleşen ürün adı bulunamadı — en yakın kavramsal eşleşme Braintrust'ın CI-gated eval akışı ve genel "dört-aşamalı rollout gate" (shadow → canary → percentage → full) endüstri deseni; bu desen isimsiz, blog-seviyesinde tarif ediliyor (arama-sonucu: futureagi.com/blog/agent-rollout-strategies-2026).

### Pazar sinyali

| Ürün | Fiyat sayfası | Sinyal sınıfı | Değerlendirme |
|---|---|---|---|
| Langfuse | VAR (langfuse.com/pricing-self-host) | ödeme kanıtı VAR: Hobby ücretsiz, Core $29/ay, Pro $199/ay, Enterprise $2.499/ay | ödeme-doğrulanmış |
| LangSmith | VAR | LangSmith Plus $39/koltuk/ay (arama-sonucu) | ödeme-doğrulanmış |
| Braintrust | VAR | Braintrust Pro $249/ay (arama-sonucu) | ödeme-doğrulanmış |
| Galileo | VAR | Galileo Pro $100/ay (arama-sonucu) | ödeme-doğrulanmış |
| Patronus AI | [?] açılmadı | fiyat sayfası doğrulanamadı | sinyalsiz |
| ModelOp | [?] açılmadı | kurumsal satış modeli (fiyat sayfası muhtemelen yok/talep-üzerine) | sinyalsiz |
| Scrut | [?] açılmadı | — | sinyalsiz |
| AllTrue.ai | [?] açılmadı | — | sinyalsiz |
| "Kanıt-kapılı otonomi merdiveni" (B68-4 kavramı, isim eşleşmesi) | YOK | doğrudan muadil ürün bulunamadı | sinyalsiz |

GitHub yıldız / funding / iş ilanı sınıfı sinyal ayrı arama yapılmadı (bütçe); yalnız fiyat-sayfası varlığı doğrulandı.

### Rekabet yoğunluğu ve etiket

- **Genel agent-evaluation/observability pazarı (Langfuse/LangSmith/Braintrust/Galileo/Patronus sınıfı): DOYGUN.** Çok sayıda ödeme-doğrulanmış, olgun ürün var, 2026 karşılaştırma blogları yoğun.
- **AI TRiSM / NIST-RMF uyum aracı sınıfı (ModelOp/Scrut/AllTrue): ORTA.** Az sayıda kurumsal oyuncu, Gartner tanınırlığı var ama fiyat şeffaflığı düşük (çoğu talep-üzerine satış).
- **"Koşum-sayılı kanıt kapısı" spesifik kavramı (takvim değil, kanıt-sayısıyla otonomi kademelendirme): SEYREK / bulunamadı.** En yakın pratik "dört-aşamalı rollout gate" (shadow/canary/percentage/full) — bu da trafik-yüzdesi tabanlı, koşum-sayılı kanıt-eşiği tabanlı değil.

**Etiket: DESTEKLİ (genel eval/gözlemlenebilirlik + TRiSM/uyum pazarı doygun-orta yoğunlukta VE ödeme kanıtlı) — ancak B68-4'ün özgül mekanizması (takvim yerine koşum-sayılı kanıt kapısı ile otonomi merdiveni) için DAYANAKSIZ; birebir muadil bulunamadı, boşluk iddiası bu taramayla çürütülmedi ama doğrulanmadı da.**

---

## (2) Dağıtım/iş-modeli emsalleri (tek kişilik geliştirici için)

**Arama sorguları (birebir):**
1. `Langfuse open source to commercial cloud pricing plan`
2. `Aider Continue.dev open source developer tool business model pricing funding`

### Emsal tablosu

| Ad | Dağıtım sınıfı | Ücretli plan | Gözlem (artı/eksi) |
|---|---|---|---|
| Langfuse | açık-kaynak+bulut (MIT çekirdek, ücretli bulut katmanları) | VAR (Hobby ücretsiz → Core $29 → Pro $199 → Enterprise $2.499/ay; aşım $8/100k birim) | Artı: MIT lisans tüm çekirdek işlevi (tracing/eval/prompt) kapsıyor, benimseme hızlı; Eksi: yalnız SCIM/audit-log/RBAC/UI-özelleştirme ücretli — kurumsal gelir yüzeyi dar, self-host kullanıcı ücretsiz kalabiliyor (gelir kaçağı riski) |
| Aider | saf açık-kaynak (Apache-2.0, tek geliştirici bakımlı — Paul Gauthier) | YOK (ücretli ürün, fatura altyapısı, kariyer sayfası yok; kullanıcı kendi model API anahtarını kullanıp sağlayıcıya öder) | Artı: sıfır bakım-gelir çatışması, token maliyeti kullanıcıda, geliştirici yükü düşük; Eksi: gelir yüzeyi yapısal olarak yok — bilinçli konumlanma, ölçeklenmiyor |
| Continue.dev | açık-kaynak+bulut (temel özellik ücretsiz, barındırılan model erişimi + takım kontrolleri ücretli) | VAR (Starter: $3/milyon token barındırılan model; Team: $20/koltuk/ay — admin kontrol, kullanım paneli) | Artı: seed-fonlama aldı ($2,1M) ve Anysphere tarafından satın alındı — çıkış emsali var; Eksi: token-geçişli fiyatlama marj riski taşır, model sağlayıcı fiyat değişimine bağımlı |

### Dağıtım sınıfı başına artı-eksi

**Açık-kaynak+destek/bulut (Langfuse, Continue.dev tipi):**
- Artı: geniş ücretsiz taban → hızlı benimseme, kurumsal katmanla (uyum/RBAC/audit) net gelir ayrımı, self-host güven inşa eder.
- Eksi: çekirdek işlev ücretsizse (Langfuse gibi) kurumsal olmayan kullanıcı asla ödemeyebilir; bakım yükü hem OSS hem bulut altyapısını kapsar — tek kişilik geliştirici için ikili yük.

**Araç (CLI, tek satış / gelirsiz) — Aider tipi:**
- Artı: bakım yükü minimal, fatura/destek altyapısı gerekmez, geliştirici zamanını üründe tutar.
- Eksi: gelir modeli yok; sürdürülebilirlik bağışa/sponsorluğa/ana işe bağlı; ölçek planı yok.

**SaaS (LangSmith/Braintrust/Galileo tipi, tam kapalı-bulut):**
- Artı: net ücretli katman ($39–$249/ay aralığı gözlendi), gelir öngörülebilir, kurumsal satışa uygun.
- Eksi: tek kişilik geliştirici için müşteri destek/güvenlik-uyum (SOC2 vb.) yükü ağır; DOYGUN pazarda farklılaşma zor (yukarıda tespit edildi).

---

## Kısıtlar ve açık noktalar
- Patronus AI, ModelOp, Scrut, AllTrue.ai fiyat sayfaları AÇILMADI (bütçe sınırı) — hepsi `[?]`.
- GitHub yıldız sayısı / iş ilanı sınıfı sinyal taranmadı (yalnız fiyat-sayfası varlığı ile sınırlı sinyal).
- Tüm rakamlar arama-sonucu özetinden alınmıştır, birincil kaynak sayfası açılıp doğrulanmamıştır — "arama-sonucu" etiketiyle işaretlendi, "birincil kaynak" denmedi.
- Tahmini gelir/kullanıcı rakamı YAZILMADI (yasak); yalnız VAR/YOK/[?] fiyat-sayfası varlığı beyan edildi.
