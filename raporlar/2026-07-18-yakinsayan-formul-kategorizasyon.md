# Yakınsayan Skill-Kombinasyon Formülizasyonu + Kategorizasyon — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit izinli (Salih 07-18; merge/canon=Fable, m.41). Kaynak: Salih 07-18 — "davranışlarıma RASTGELE kombinasyon uygulayarak skill geliştireceğiz AMA zamanla YAKINSAYAN bir formülizasyon olmalı, rastgele olmamalı; kaldıraç = tekrar eden talimatları doğru KATEGORİZE etmek." Bu = **m.35 farklılaşma tezinin matematiksel omurgası.** Atlas 2 şerit: kategorizasyon (DONE) + yakınsama-matematiği (DONE).

---

## 1. Problem (Salih'in çerçevesi)
- Skill'ler = Salih'in tekrar eden davranışlarından yapı-taşı kombinasyonları.
- Naif hâl: **rastgele kombinasyon** (evrimsel/genetik arama; m.37/V39 dış-anahtar).
- İstenen: **zamanla YAKINSAYAN formül** — rastgele değil, veriyle (senaryo-defteri 4-tuple) kararlı bir politikaya oturan.
- **Kaldıraç (Salih):** tekrar eden talimatları DOĞRU KATEGORİZE etmek.

## 2. Neden kategorizasyon yakınsamayı sağlar (kategorizasyon şeridi — DONE)
**Çekirdek matematik:** düz uzayda N ayrık talimat → **2^N** kombinasyon; yapı yoksa arama ~rastgele, yakınsama üstel-yavaş. **Faceted (çok-eksenli) uzayda** kombinasyonlar **tip-uyumluluğuyla budanır**; öğrenme **facet-başına TOPLAMSAL** (kombinasyon-başına ÇARPIMSAL değil) olur.
- **(a) kategori = context → contextual bandit:** düz bandit "en iyi tek kol", contextual "bağlam→kol politikası"; hiyerarşik partisyon regret yakınsamasını hızlandırır; ödül bileşenlere ayrılabildiğinde odaklı güncelleme ~**√n_f** faktörü hız [abstract, bayraklı].
- **(b) kategori = option → Hierarchical RL:** soyut aksiyonlar arama-uzayını çarpıcı küçültür + kredi-atamasını kolaylaştırır (örneklem+hesap karmaşıklığı düşer).
- **(c) faktörlü temsil → bileşimsel genelleme + TRANSFER:** Voyager skill-kütüphanesi 15.3× hız + yeni-dünyaya transfer [abstract]; kategorize-edilmemiş yaklaşım transfer edemez.
- **U-eğrisi ödünleşimi (kategori-sayısı):** çok AZ → underfit (bağlam ayrışmaz, gürültülü); çok ÇOK → her kategori seyrek, veri-kıtlığı (regret ~ bağlam×kol hücre sayısı). **Tatlı nokta = minimum-yeterli partisyon** (küçük-kardinaliteli MECE facet'ler).

## 3. Yerleşik taksonomiler/yöntemler (kategorizasyon şeridi)
| Yöntem | Ne | JARVIS'e |
|---|---|---|
| ISO 24617-2 dialog-act (9-boyut faceted) | iletişimsel-işlev standardı | Facet-1 işlev şablonu |
| CLINC150/MASSIVE (domain→intent) | 2-katman intent benchmark | Facet-2 alan şablonu |
| AGENTIF (kısıt×temsil + meta-kısıt) | ajan-talimat tipolojisi | m.16 çelişki/"karar üstüne karar" = meta-kısıt |
| TnT-LLM (KDD'24) | LLM taksonomi-indüksiyonu (2-faz) | taksonomiyi veriden ÜRET |
| Embedding-küme + LLM-adlandır (NILC/LUMI/Dial-In) | yeni-niyet keşfi | "tekrarlayan-küme→skill" madenciliği |
| Task/Process mining (Frequent Episode Mining) | tekrar eden görev-DİZİsi keşfi | "araştır→kaydet→devret" workflow tespiti |
| Faceted classification (Ranganathan PMEST) | çok-eksenli sınıflama teorisi | 4-facet iskeletin teorik temeli |

## 4. ★ JARVIS için 4-FACET kategorizasyon iskeleti (kategorizasyon şeridi önerisi)
Salih'in kümelerini TEK hiyerarşiye değil **4 bağımsız eksene** oturt (faktörlü → öğrenme toplamsal → yakınsar):
- **Facet 1 — İşlev (NE yapar):** karar · araştırma · kayıt-damıtma · dönüşüm(çeviri/format) · devir-teslim(kapsül) · icra-yapım · yönetim-meta(kural/veto/düzeltme). *(ISO 24617-2 + AGENTIF meta-kısıt.)*
- **Facet 2 — Nesne (NEYE dokunur):** kanon/tüzük · wiki/bilgi · kod/artefakt · ajan/köprü · oturum/bağlam. *(CLINC/MASSIVE domain.)*
- **Facet 3 — Ölçek/yetki (m.31):** Katman-1(Salih) · Katman-2(Carvis) · alt-karar(soru-yok). *(En ayırt edici bandit-bağlam ekseni; kol-uzayını doğrudan budar.)*
- **Facet 4 — Tekrar imzası:** tek-seferlik · tekrar-eden · periyodik-kadans. *(task-mining frekans; yalnız tekrar-eden/periyodik = skill adayı.)*

**İşleyiş:** keşif (git-log/raporlar/cc embed→küme→LLM-adlandır) → yerleştirme (küme = 4-facet tuple'ında NOKTA; skill = kararlılaşmış BÖLGE) → kombinasyon (facet-uyumlu YOL; tip-uyumsuz budanır, ör. alt-karar bir Katman-1 çıktısını publish edemez) → yakınsama (bağlam=facet-tuple, her facet ayrı/toplamsal öğrenilir → yeni talimat türü yalnız ilgili facet'i günceller).
**Neden yakınsar (tek cümle):** facet-sayısı küçük (4) + facet-kardinalitesi küçük (3-7) → kombinasyon-uzayı çarpımsal büyürken öğrenme facet-başına toplamsal kalır (U-eğrisi tatlı noktası); TnT-LLM/task-mining ile facet'ler veriden zamanla rafine (statik değil).

## 5. Yakınsayan formülizasyon (yakınsama-matematiği şeridi — DONE)
**Çekirdek tez:** rastgele/genetik ↔ yakınsayan farkı = **bellek + olasılıksal model (önsel/posterior).** "Yakınsama garantisi" matematiksel olarak **pişmanlık sınırı (regret bound):** kümülatif R(T) alt-doğrusal (sublinear) ise R(T)/T → 0 → en-iyi kombinasyona **KANITLI yakınsama.** Salih'in "rastgele değil, zamanla yakınsayan" = **"kategorize-uzaya posterior koy, pişmanlığı alt-doğrusal tut."**
- **Rastgele düşman DEĞİL, BELLEKSİZ-rastgele düşman** (Bergstra-Bengio: rastgele grid'i yener — etkin-boyut düşükse). Yapı = önsel + kategorizasyon + credit-assignment. Salih'in "azalan epsilon, daralan UCB" sezgisi = **TEOREM** (ε_n=1/n → O(log n); UCB genişliği √(log n / n_i) daralır).

### 5.1 Yöntem sıralaması (garanti tipiyle)
| Yöntem | Yakınsama garantisi | JARVIS |
|---|---|---|
| UCB1 | güçlü, O(log n) pişmanlık | ilk basit/parametresiz seçici |
| **Thompson Sampling** | **asimptotik OPTİMAL** (Lai-Robbins alt-sınırını doldurur) | **önseli (defter) doğal alır; az-veri+gürültü sağlam** |
| **Contextual bandit/LinUCB** | güçlü, Õ(√dT), context'e koşullu | **kategori=context — 4-facet ile birebir** |
| GP-UCB / BO | no-regret | **pahalı-az-değerlendirme rejimi (LLM çağrısı=pahalı)** |
| Successive-Halving/Hyperband/ASHA | orta-güçlü, rastgeleden ≤sabit-kat yavaş | bütçe/kalan-zaman eleme (m.35) |
| **BOHB** | **güçlü+pratik (Hyperband hızı + BO garantisi)** | **en iyi bileşik = m.35'in matematiği** |
| Sequential-Halving/best-arm | güçlü (sabit-bütçe en-iyi-kol) | çevrimdışı **skill-dondurma** turu |
| SA / CMA-ES | garanti gerçek ama pratik-dışı yavaş / dar sınıf | ana döngü için ÖNERİLMEZ |
| L2O meta-öğrenme | zayıf/koşullu (eğitim-dağılımına bağlı) | Salih'in "formül=politika" vizyonu ama **çok-veri ister, ERKEN** |

### 5.2 ★ SOMUT yakınsayan-formül (iki şeridin BİRLEŞİMİ)
JARVIS rejimi: pahalı koşum · az örnek · gürültülü kalite · kategorik-yapılandırılmış uzay · çok-amaçlı ödül · context var →
> **4-facet kategorize-talimat-uzayı üzerine, desirability-skalerli 4-tuple ödüllü, bütçe-farkında Contextual Thompson Sampling / BOHB.**
- **Bağlam x** = 4-facet tuple (§4) → context vektörü. *(kategorizasyon şeridi ile birleşim noktası.)*
- **Kol a** = seçim-dizisi (karar-noktalarındaki seçim-birimleri kombinasyonu; V39 dili).
- **Ödül r** = **desirability D(a) = [d_kalite · d_token · d_zaman]^(1/3)** (Derringer-Suich geometrik ortalama); **sıfır-desirabilite bir amacı ÖLDÜRÜR** (kalite eşiğin altında → skor 0 → "kalite pahasına ucuzluk" kaçağı kapanır; V54/worst-case ile uyumlu).
- **Politika π** = Contextual Thompson Sampling: (kategori, kombinasyon) başına posterior; örnekle → en-yüksek seç → gözle → güncelle. **Önsel = senaryo-defteri credit-assignment** (soğuk-başlangıç çözümü).
- **Bütçe (m.35 kalan-zaman)** = BOHB: ucuz kısmi-koşumla çok aday ele → hayatta kalanı tam-bütçeye terfi; kalan-zaman azalınca keşif otomatik daralır.
- **Keşif çizelgesi** = TS posterior-daralması (ekstra epsilon gerekmez; "yakınsayan" davranış YAPIYA gömülü).
**Neden rastgele/genetikten üstün:** GA/rastgele yalnız asimptotik kapsama, yakınsama-HIZI garantisi YOK; posterior → O(log T)–Õ(√T) pişmanlık = **kanıtlı yakınsayan.** **Ontolojik:** bir "skill" zaten **YAKINSAMIŞ bir politikadır** (context→kombinasyon kararlı eşleme). Bandit/BO koşumları paylaşılan posterior üzerinden bağlar; genetik onları izole bırakır.

### 5.3 Yakınsama nasıl ÖLÇÜLÜR (senaryo-defterine)
- **Kümülatif pişmanlık R(T) = Σ[D(a*) − D(a_t)];** eğri düzleşiyorsa (alt-doğrusal) yakınsıyor; R(T)/T → 0 hedef.
- **Basit pişmanlık** = skill-dondurma turu metriği.
- **JARVIS ölçütü:** kategori-başına "en-iyi-skor-şimdiye-dek" + "koşum-başına-pişmanlık" grafiği senaryo-defterine → **düşen eğri = yakınsama kanıtı**; düz-yüksek eğri = önsel/çizelge gözden geçir.

### 5.4 ★ KRİTİK açık risk — durağan-olmama (stationarity)
Garantilerin çoğu **durağan ödül** varsayar (kol kalitesi kaymaz). JARVIS'te model güncellenir + görev-dağılımı kayar → **durağan-DEĞİL.** Çözüm: iskontolu/kayan-pencere UCB (Garivier-Moulines — *doğrulanmadı*) veya periyodik yeniden-başlatma. **Göz ardı edilirse yakınsama garantisi GEÇERSİZLEŞİR.** Ayrıca az-örnekte garanti asimptotik → pratik **ÖNSELİN kalitesine** bağlı ("garanti sonsuzda, pratik önselde"). → sonraki araştırma dalgasının #1 adayı.

## 6. Kanon bağı
- **m.35** (kombinasyon-başına beklenti vektörü + kalan-zaman politikası) = bu formülün ta kendisi; 4-facet = beklenti-vektörünün bağlamı.
- **m.37/V39** (kombinasyon-dizisi, ardışık-deney) = arama; kategorizasyon onu rastgeleden yakınsayana çevirir.
- **senaryo-defteri** 4-tuple = ödül sinyali; credit-assignment = facet-başına atıf.
- **skill fikri kutusu** = keşfedilen facet-noktaları; **K-020** (Optuna/ASHA/promptfoo) = koşum altyapısı.

## Kaynaklar (yakınsama şeridi — birincil, doğrulandı)
UCB1 Auer+2002 · Thompson Kaufmann+2012/Agrawal-Goyal · LinUCB Li+2010 · GP-UCB Srinivas+2010 · rastgele-arama Bergstra-Bengio 2012 · Successive-Halving Karnin+2013 · Hyperband Li+2017 · BOHB Falkner+2018 · desirability Derringer-Suich 1980 · çok-amaçlı-BO qNEHVI Daulton+2021 · L2O Chen+2022. (Kategorizasyon şeridi kaynakları ayrı: ISO 24617-2 · TnT-LLM KDD'24 · TaxoGen · Faceted/Ranganathan · CLINC/MASSIVE · Voyager.)

## Doğrulanmamış bayraklar
- Kategorizasyon: arxiv/hackernoon/emergentmind 403-bloke → abstract-seviyesi: Hierarchical-CB √n_f · Dial-In %94.4 · TnT-LLM Faz-1 alt-adım · Voyager 15.3×. "Patron-asistanı talimat-taksonomisi" hazır literatürü YOK → 4-facet SENTEZ.
- Yakınsama: **durağan-olmama en yüksek açık risk** (garantiler durağan-ödül varsayar; JARVIS kayar → iskontolu-UCB/yeniden-başlatma şart). Regret sınırları ASİMPTOTİK → az-örnekte pratik önselin kalitesine bağlı. Garivier-Moulines discounted-UCB · Lai-Robbins 1985 orijinali → doğrudan çekilmedi (dolaylı teyitli). JARVIS-uyum eşlemeleri Atlas'ın mühendislik yargısı — deneyle sınanmalı.
