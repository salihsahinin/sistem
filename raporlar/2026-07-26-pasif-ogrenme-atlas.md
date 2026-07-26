# Pasif Öğrenme Modeli · Ajan Donması · Kaynak Kategorizasyonu — Atlas Raporu (2026-07-26)

> **Mod:** yan-oturum (m.41 — CC bulut) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: 8 (A1–A8)
> **Koşum:** 8 tez atlası + 8 antitez atlası (CoVe-Factored: antiteze yalnız çıplak iddia listesi verildi, gerekçe/kaynak VERİLMEDİ) + hakemlik (Carvis) + 1 yerel ölçüm (bu oturumun kendi telemetrisi)
> **Tetikleyen:** Salih 07-26 — (1) pasif öğrenme modeliyle karar-akışından öğrenme metni üretimi, staj bağlamı · (2) araştırma ajanlarının donması, DS bakışıyla çözüm + oturumlaştırma · (3) şirkete ajan ataması · (4) kaynak-kategori sayısının optimumu

---

## 0. KANIT KISITI — bu raporun en önemli satırı (dürüstlük beyanı)

**Bu oturumda hiçbir akademik kaynağa inilemedi.** Kurumsal egress politikası, denenen akademik hostların tamamını CONNECT düzeyinde reddetti (403 / bağlantı kurulamadı). Carvis 10 hostla ayrıca ölçtü: **10/10 ret**.

```
export.arxiv.org · ncbi.nlm.nih.gov · doi.org · scholar.google.com · researchgate.net
core.ac.uk · api.crossref.org · biorxiv.org · psycnet.apa.org · link.springer.com   → hepsi ret
```

Bunun üç sert sonucu var ve raporun her satırı bu kısıtın altında okunmalıdır:

1. **A1, A2, A3 ailelerinde D etiketi hak eden TEK BİR bulgu yoktur.** m.40b'de D = "birincil kaynağa inildi"; bu oturumda mümkün değildi. Tavan **K**'dir.
2. **A4, A5, A7 ailelerinde D vardır** — çünkü bu ailelerin kaynakları akademik değil teknik: `platform.claude.com`, `code.claude.com`, `github.com`, ve özellikle **`raw.githubusercontent.com` üzerinden dokümantasyonun upstream depoları** (kubernetes/website, temporalio/documentation, celery/celery, github/docs, circleci/circleci-docs, buildkite/docs, mdn/content, torvalds/linux, envoyproxy/envoy, nginx/nginx.org, open-telemetry/semantic-conventions-genai, anthropics/anthropic-sdk-python). Bu, kapalı hostun etrafından dolaşmak DEĞİL — aynı metnin kaynağına inmektir ve [D] etiketini hak eder.
3. **V26 örneklem-denetimi klasik haliyle koşulamadı.** "Rastgele iddia seç, kaynağa in, doğrula" adımı fiziksel olarak kapalıydı. Yerine **çapraz-sorgu denetimi** koşuldu (aynı rakam bağımsız sorgularda tekrar ediyor mu) ve V26 yerine geçtiği İDDİA EDİLMİYOR. Bölüm 10'a bakınız.

**Sonuç: bu rapor karar-öncesi TARAMA olarak kullanılabilir, KANIT olarak kullanılamaz.** Akademik rakamların tüzük anlamında hüküm taşıması için erişimi açık bir oturumda yeniden doğrulanması gerekir (bölüm 12, açık borç #1). Teknik [D] bulguları bu borcun dışındadır.

---

## 1. YÖNETİCİ ÖZETİ — hayatta kalan çekirdek

Adversaryal saldırıdan sağ çıkan iddialar (bilgili bir antitez ajanı çürütmeyi deneyip **başaramadı**):

| # | Hayatta kalan çekirdek | Aile | Etiket |
|---|---|---|---|
| S1 | Bir LLM, kalıcı bellek altyapısı olmadan önceki oturumlardan öğrenen-modeli **taşımaz**; kalıcılık modelin değil **uygulama katmanının** özelliğidir. | A1 | K |
| S2 | LLM sentezinden öğrenmek, **çekirdek olgular aynı sunulsa bile** web aramasıyla öğrenmeye göre daha sığ bilgi üretir (7 deney, n=10.462). | A2 | K |
| S3 | Halüsinasyonlu bir içerik bir kez öğrenildiğinde, sonraki düzeltme etkiyi **tamamen silmez** (4 bağımsız meta-analiz aynı yöne). | A4 | K |
| S4 | Ajan-belleği satıcı rakamları **kıyaslanamaz**; LoCoMo protokol boşlukları + çözülmemiş satıcı ihtilafı birincil kaynakla doğrulandı. | A4 | D |
| S5 | Doğru asılma-saptama primitifi mutlak zaman aşımı değil, **her ilerleme olayında sıfırlanan** progress deadline'dır. | A5 | D |
| S6 | 13 ADR şablonunun **hiçbirinde** "gözlenmiş sonuç / karar doğru çıktı mı" alanı yoktur; hepsi karar-anı yakalama şemasıdır. | A4 | D |

Çürüyen ya da ciddi daralan iddialar bölüm 3–9'da aile aile verilmiştir. **Bu koşumun en değerli çıktısı çürüyenlerdir** — çünkü üçü doğrudan Salih'in tasarımını değiştirir (bölüm 11).

---

## 2. ÖLÇÜM — ajan donması (Carvis, yerel telemetri, N=24)

Bu bölüm atlas çıktısı değildir. Salih'in "bazı araştırma ajanları donuyor" bildirimi üzerine, **bu oturumun kendi alt-ajan transkriptleri veri seti olarak kullanılarak** ölçülmüştür. m.35 (ölçüm-öncelik) uyarınca teoriden önce koşuldu.

**Veri:** 24 alt-ajan koşumu, toplam 139 dk duvar-saati, olay-zaman damgaları JSONL transkriptlerinden.

### 2.1 Hipotez ve çürütülmesi

**H0 (Carvis'in ilk hipotezi):** Ajanlar ağ çağrılarında asılı kalıyor — proxy 403'lerine takılan `WebFetch`/`curl`.

**H0 ÇÜRÜTÜLDÜ.** Araç başına bekleme dağılımı:

| Araç | n | p50 (s) | p90 (s) | max (s) |
|---|---|---|---|---|
| WebSearch | 359 | 0,7 | 7,0 | **11,0** |
| WebFetch | 281 | 0,2 | 1,2 | **10,4** |
| Bash | 113 | 0,4 | 3,1 | **600,1** |

`WebSearch` ve `WebFetch` maksimumları ~11 saniyede tavana vuruyor — bu araçların zaman aşımı **çalışıyor**. Ağ kaynaklı asılma yok.

### 2.2 Gerçek bulgular

- **Süre ile en uzun tek duraklama arasında r = 0,95 (N=24).** Bir ajanın ne kadar sürdüğü neredeyse tamamen tek bir duraklamayla açıklanıyor — iş hacmiyle değil.
- **Verim tersine dönüyor.** Hızlı ajanlar 25–43 olay/dk üretirken yavaş ajanlar 4–11 olay/dk. En yavaş ajan (1173 s) 81 olay üretti; 105 saniyelik bir ajan 72 olay üretti. **Yavaş ajan daha çok iş yapmıyor — duruyor.**
- **Toplam duvar-saatinin %35'i, ajan başına tek bir duraklamanın içinde geçiyor** (139 dk'nın 48 dk'sı).

### 2.3 Kök neden — 60 saniyeyi aşan 18 duraklamanın ayrıştırılması

| Sınıf | Adet | Ne olduğu |
|---|---|---|
| **Gerçek patoloji** | **2** | Ajanın **kendi yazdığı bekleme döngüsü**: biri `Bash(timeout=600000)`, diğeri `for i in $(seq 1 30); do if [ -f ... ]` — yani alt-ajan çıktısını **yoklayarak (polling)** bekleme |
| Uzun üretim | 16 | Ajanın 200 KB+ raporunu yazdığı üretim süresi — patoloji değil |

**Salih'in gördüğü belirtinin tam açıklaması budur:** ajan `sleep`/yoklama döngüsündeyken süreç canlıdır, CPU'dadır, ama bağlam büyümez — çünkü gerçekten hiçbir şey üretmemektedir.

### 2.4 Eşik seçimi — maliyet-duyarlı, ve neden sezgi yanlış

| Eşik | İşaretlenen | Gerçek patoloji | Kesinlik |
|---|---|---|---|
| 60 s | 18 | 2 | **%11** |
| 120 s | 11 | 2 | %18 |
| 250 s | 5 | 2 | %40 |
| 300 s | 2 | 2 | **%100** |

"120 saniyedir çıktı yok → öldür" gibi sezgisel bir kural, **her 6 müdahaleden 5'inde sağlıklı bir ajanı öldürürdü** — üstelik tam da raporunu yazan, yani en değerli ajanları. Doğru eşik veriden çıkar.

**Ama:** pozitif örneklem **N = 2**. Bu eşiğe güvenmek için çok küçüktür. Bu, başlı başına bir ders konusudur (bölüm 11.2, oturum L4).

### 2.5 Ölçümün kendi sınırı (dürüstlük)

- 18 duraklamanın 16'sı "araç bloğu olmayan asistan olayı"nı takip ediyor. Bunlar uzun üretim OLARAK yorumlandı, çünkü bu ajanlar gerçekten çok büyük raporlar üretti. Ancak **bu veriden "uzun üretim" ile "asılı akış" ayrıştırılamaz** — ikisi de dışarıdan sessizlik olarak görünür. Bu bir **tanımlanabilirlik (identifiability)** sorunudur ve ayrıştırmak için token-düzeyi telemetri gerekir (`gen_ai.client.operation.time_per_output_chunk` — A5/32).
- N=24 tek oturumdan; koşumlar zaman-ayrık değil, aynı ağ/kota koşullarını paylaşıyor. Genellenebilirliği sınırlıdır.

---

*(Bölüm 3–12 koşum devam ederken yazılmaktadır: A1–A8 aile bulguları, hakemlik hükümleri, V26 ikamesi, tasarım önerisi, ajan tasarım paketi, açık borçlar.)*
