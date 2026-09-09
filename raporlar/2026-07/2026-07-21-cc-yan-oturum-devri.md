# CC Yan-Oturum — KARAR DOSYASI (nihai hükmü Fable-JARVIS ana-sıra verir) — 2026-07-21

> **Amaç ve mercii (m.41 / m.42):** Bu bir Opus **yan-oturum** çıktısıdır (Carvis-Opus hazırladı) ama **karar mercii değildir.** Buradaki açık kararların **nihai hükmünü Fable-JARVIS ana-sıra verir** (model hiyerarşisi: Salih + Fable-Jarvis en üstte, Opus altında — m.30 ek fıkra / m.42(g); kanon kararı geçerlilik yolu m.41: ana-sıra ∧ Fable). Belge **baştan sona bu bilinçle** hazırlandı: her karar, Fable'ın doğrudan hüküm verebileceği biçimde **seçenek + kanıt + Carvis-önerisi + karşıt-temel** ile paketlendi (m.37 karar-modeli deseni). Fable hükmü verir; **canon/skill dosya yazımı masaüstü ana-sıra dönüşünde işlenir** (model farketmez — 8600e3f). Salih (Patron) her zaman override edebilir (m.31).

---

## 1. Bağlam — bu oturumda ne oldu (Fable'ın karar zemini)

1. **m.40b yöntem değişikliği (çift-atlas → multi-hop).** Salih yeni 3-aşamalı tasarım getirdi: **(1)** tezleri koştur → **(2)** tezleri OKUYAN hedefli antitez (¬) → **(3)** tez↔antitez kıyas/hakemlik. m.16 kapısı açıldı: eski kanonun **"bağımsızlık şartı"** (atlas-kosum SKILL step 3) + **"kesişim = en sağlam"** (step 6 = m.37 triangülasyon) ile literal çelişki. Salih detaylı iki kararı ("şimdi değil/sonra") **Fable'ın hükmüne bıraktı** → §2'de K1/K2 olarak paketlendi.
2. **Üç araştırma raporu üretildi + main'e pushlandı** (commit 9d56a3c): `multihop-oneshot-literatur.md` · `grill-me-skill-arastirma.md` · `ekran-yakalama-hotkey-arastirma-hatti.md`.
3. **Yakalama-hattı fikri** (ekran-görüntüsü + hotkey → oto-araştırma; SES-POC'un görsel kardeşi): tasarım hazır (ShareX + AutoHotkey + `claude --bare -p`), inşa "ilerde".
4. **Git senkron:** 3 rapor + bu dosya main'de; makine origin'le tam senkron.

---

## 2. FABLE'IN HÜKME BAĞLAYACAĞI KARARLAR

### K1 — m.40b sağlamlık ölçütü *(canon; ana-sıra∧Fable)*
- **Karar:** Multi-hop'ta antitez tezi gördüğü için "kör-kesişim = en sağlam" doktrini (m.40b step 6 / m.37 triangülasyon) düşüyor. Yerine ne?
- **Seçenekler:** **(A)** adversarial-hayatta-kalma (bilgili antitezin çürütmeyi deneyip başaramadığı iddia = sağlam çekirdek) · **(B)** kör-triangülasyonu koru (ek bir kör-bağımsız antitez, +1.5–2× token) · **(C)** Hegelci-sentez (Aşama-3 kıyas değil sentez üretir).
- **Kanıt (`multihop-oneshot-literatur.md`):** eski "bağımsızlık" zaten kısmen yanılsamaydı — korelasyonlu LLM hataları, Condorcet bağımsızlık koşulu ampirik çöküyor, ensemble ~+0.00 F [51]. Hedefli Devil's-Advocate çürütme dramatik güçlü: **%99.2 vs %48.3** [46].
- **Carvis önerisi:** **(A) adversarial-hayatta-kalma** — kör-kesişimden güçlü sağlamlık sinyali, yeni akışın doğal ürünü.
- **Karşıt-temel (Fable tartsın):** (B) lehine zemin = bağımsız triangülasyon farklı bir doğruluk-sinyali; ×2 token m.35 ölçüm-önceliğiyle bilinçli ödenebilir. (A)'nın riski: sağlamlığı tek ölçüte indirgemek.

### K2 — m.40b koşum aygıtı *(canon; ana-sıra∧Fable)*
- **Karar:** Üç aşama gerçek Atlas araştırma ajanlarıyla mı, Carvis'in saf muhakemesiyle mi koşsun?
- **Seçenekler:** **(A)** ajanlı-hibrit (Aşama-1/2 gerçek dış tarama, Aşama-3 Carvis kıyas) · **(B)** saf-muhakeme (üç aşama içsel, dış ajan yok).
- **Kanıt:** explicit decomposition latent tek-geçişi çok geçiyor — CoT **%92.8** vs latent **%7.6** [6]; ToT **%74** vs CoT **%4** [23].
- **Carvis önerisi:** **(A) ajanlı-hibrit** — dış-kanıt genişliği + multi-hop birlikte korunur.
- **Karşıt-temel:** (B) daha ucuz/hızlı; ama "atlas"ın asıl araştırma değeri düşer, içe kapanır.
- **K1+K2 ortak tasarım şerhi (raporun eklediği):** antitez ajanına tezin **İDDİASINI** ver, **GEREKÇESİNİ verme** (CoVe-Factored → çıpalama/anchoring freni [28][37]). Aşama-1 (tez) çıpalama-riski taşımaz (önceki çıktı yok) → çoklu-seed bağımsız üretim orada korunur.

### K3 — grill-me *(öğrenme-şeridi varsayılanı; ana-sıra∧Fable)*
- **Karar:** (a) V55 pasif-okuma varsayılanı korunsun mu · (b) Pocock skill'i kurulsun mu yoksa K-016 eval-önce akışıyla JARVIS-natif `sinav`/`grill` skill'i mi üretilsin.
- **Kanıt (`grill-me-skill-arastirma.md`):** gerçek viral skill (mattpocock/skills, `grilling` motoru); öğrenme şeridinin ertelenmiş "gerçek anlama ölçümü" boşluğuna birebir oturuyor; [S]/[O]/[T] + "bulanık blok" ile eşleşiyor.
- **Carvis önerisi:** V55'i **bozma**; üstüne **isteğe-bağlı** grilling doğrulama-geçişi + K-016 ile natif `sinav` skill'i (öğrenme etiketleriyle gömülü).
- **Karşıt-temel:** ekstra sürtünme tempoyu düşürür (V55 pasif-okumaya geçişin ilk gerekçesi tam buydu).

### K4 — yakalama-hattı otomasyon sınıfı *(m.30 / K-010)*
- **Karar:** yarı-otomatik (Salih notu girer+koşumu görür = m.30 otomasyon, şimdi serbest) vs tam-otomatik (habersiz `dontAsk` = canlı-ajana yaklaşır, K-010 kapısı) + auth çatalı (API-key vs abonelik setup-token).
- **Carvis önerisi:** **yarı-otomatikle başla**; K-010 olgunlaşınca (temel 2 hafta sorunsuz) tam-otomatik değerlendir.

---

## 3. Açık borçlar / Fable kararından SONRA (masaüstü ana-sıra dönüşünde)
- **Kapsül + pano'ya bu raporlara pointer** (canon → hiçbir mobil oturum yazamaz, 8600e3f).
- Fable K1/K2 hükmü → **m.40b v0.2 amendment metni + atlas-kosum SKILL v0.2** yazımı.
- Untracked, benim değil: `raporlar/...-anlatimli-rehber.docx` (ben oluşturmadım) + P3 ders dosyaları.
- Güvenlik: PAT remote URL'inde düz metin (`git remote -v`) → credential-helper önerisi.

## Pointer'lar
- Üç rapor: `raporlar/2026-07-21-*` · bu dosya: `raporlar/2026-07-21-cc-yan-oturum-devri.md` · commit `9d56a3c`.
- İlgili canon: m.40b (tüzük md.40 ek fıkra) · atlas-kosum SKILL · m.16 · m.37 (karar-modeli + karşıt-temel) · m.41 · m.42 · m.30/K-009/K-010.
