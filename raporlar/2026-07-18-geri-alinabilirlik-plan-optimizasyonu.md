# Geri-Alınabilirlik Notu + Önem-Sıralı Plan Optimizasyonu — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); merge/canon=Fable (m.41). Kaynak: Salih 07-18 — "geriye-dönük maliyeti önlemek için kararlarımıza geri-alınabilirliğini de not alalım; notlardan ileride faydalanır, planları önem sırasına göre optimize ederiz." **Salih: 3 model sun (m.37 karar-modeli kalıbı).** Atlas dış-tarama koşuyor (§4 dönünce rafine).

---

## 1. Problem + kanon bağı
- **İstek:** her kararın **geri-alınabilirliğini** not et → (a) rework (geriye-dönük maliyet) önle · (b) notlardan sonra faydalan · (c) planları **önem sırasına** optimize et.
- **Zaten kanonda:** m.31 (geri-alınabilirlik = Katman-1 eşiği; pahalı-geri-alma Salih'e) · kararlar-kısmı (onay-derinliği geri-alınabilirliğe endeksli, iki-yönlü/tek-yönlü kapı) · escalation-ladder **kontrol ≈ f(otonomi × geri-alınamazlık × blast-radius)** · m.37(e) (karşıtlık-derinliği geri-alınabilirliğe endeksli). Yani geri-alınabilirlik JARVIS'te zaten örtük eksen — Salih bunu **açık, kayıtlı ve plan-optimize edici** yapmak istiyor.

## 2. Üç matematik-temelli model (m.37) — geri-alınabilirlik nasıl notlanır + plan nasıl optimize edilir?
Parametreler: token (kurulum) × zaman × beklenen-kalite × RİSK.

### Model A — Skaler geri-alınabilirlik-etiketi + "son-sorumlu-an" (beklenen-rework min.) ✅ ÖNERİ
- **Ne:** her karara skaler alan: **geri-alınabilirlik ∈ {iki-yönlü-kolay · orta · tek-yönlü-pahalı}** + **blast-radius** {dar · geniş}. Plan opt.: **beklenen-rework = P(değişir) × geri-alma-maliyeti**'ni minimize et; geri-alınamaz kararı **son-sorumlu-ana** ertele (geri-alınabilir/ucuz olanı önce yap, geri-alınamaz olanı daha çok bilgi gelene dek beklet).
- token DÜŞÜK (tek alan + basit sıralama) · zaman KISA · kalite 7.5 (pratik; belirsizliği tam modellemez) · **RİSK DÜŞÜK** (m.31 ile birebir; ucuz).
- Kanon: m.31 · Lean "last responsible moment".

### Model B — Reel-opsiyon / opsiyon-değeri (belirsizlik altında beklenen-değer)
- **Ne:** geri-alınabilirlik = **opsiyon-değeri**; geri-alınamaz karar optionality TÜKETİR → "geri-alınamazlık primi" (kararın aşması gereken eşik). Belirsizlik yüksekse **beklemenin opsiyon-değeri** artar. Plan opt.: esnekliği koruyan sıralama; geri-alınamaz-yüksek-belirsizlik ertelenir; WSJF + reel-opsiyon düzeltmesi.
- token ORTA (opsiyon-değeri + belirsizlik tahmini) · zaman ORTA · kalite 8.5 (belirsizliği en doğru modeller) · **RİSK ORTA** (hesap karmaşıklığı, tahmin gürültüsü).
- Kanon: reel-opsiyonlar · kararlar-kısmı onay-derinliği.

### Model C — KARŞIT-TEMEL: Worst-case / minimax-regret önem-sıralaması
- **Ne:** ortalama/beklenen-rework'ü DEĞİL, yanlış geri-alınamaz karardan doğacak **MAKSİMUM pişmanlığı** minimize et. Alan: **worst-case blast-radius**; önem = f(geri-alınamazlık × blast-radius); en-yüksek-pişmanlıklı geri-alınamaz hamleye en sert kapı + en geç icra; geri-alınabilir olan serbest.
- **Karşıt-temel (m.37 ek):** Model C ← **Savage minimax-regret / robust karar teorisi**; A/B'nin ortalama/beklenen-değer varsayımına ZIT (worst-case). Aygıt: minimax-regret + f(geri-alınamazlık×blast-radius) escalation-ladder (isim değil). Canlılık: robust optimization + Amazon "one-way door" pratiği canlı ✓.
- token YÜKSEK (her karara worst-case analizi) · zaman YÜKSEK · kalite(ortalama) 6 (mutlu-yolda aşırı-ihtiyat) · **RİSK: worst-case EN DÜŞÜK, fırsat-maliyeti YÜKSEK**.

## 3. Öneri + triangülasyon (m.37 §9.5)
**Öneri = A** (skaler etiket + son-sorumlu-an), B'nin opsiyon-değeriyle (yüksek-belirsizlik kararlarında) ve C'nin worst-case kapısıyla (geri-alınamaz-yüksek-blast) aşılanmış.
**Zıt temeller NEREDE YAKINSIYOR (gerçek triangülasyon → YÜKSEK güven):**
1. **Karara "Geri-alınabilirlik:" alanı ekle** — A(rework-etiketi) · B(opsiyon-primi) · C(worst-case blast) hepsi bir geri-alınabilirlik kaydı ister.
2. **Geri-alınamaz kararı ERTELE (son-sorumlu-an) + daha sert KAPILA** — A(beklenen-rework↓) · B(opsiyon-değeri koru) · C(worst-case pişmanlık sınırla). Üç zıt temel → aynı eylem.
**NEREDE AYRIŞIYOR (BENİM kararım değil):** kesin **öncelik-formülü** (beklenen-rework vs opsiyon-değeri vs worst-case-regret) — ayar/veri kararı; Salih + senaryo-defteri verisi.
**★ ATLAS ÇÖZÜMÜ (ayrışmayı kapatan):** bu üç model RAKİP değil, **geri-alınabilirlik onları SEÇER** → iki-yönlü kapı = **A (beklenen-değer/WSJF)** · tek-yönlü kapı = **C (minimax-regret)** · **B'nin opsiyon-değeri = ERTELEME zamanlaması** (son-sorumlu-ana kadar beklet). Yani üçü tamamlayıcı; seçici mekanizma = geri-alınabilirlik alanı. JARVIS bunu 07-17'de sahada zaten yaptı (V39 beklenen-değer + iki minimax karşıt-temel).

## 4. Dış-tarama (Atlas — DONE)
**★ Çekirdek ders:** geri-alınabilirlik İKİ AYRI işe koşulur — **(a) KAPI/eskalasyon** (ne kadar deliberasyon + kim onaylar + ertelenir mi) ve **(b) SIRA** (ucuz/geri-alınabilir önce, pahalı/geri-alınamaz son-sorumlu-ana kapılanır). Karıştırınca ya aşırı-yavaşlık (Amazon "her şeyi Type-1 sayma" hastalığı) ya geri-alınamaz hata.

**Çerçeveler:** iki-yönlü/tek-yönlü kapı (Bezos Type-2/1) = **m.31 eşiğinin isimli teorik temeli** · reel-opsiyonlar (Dixit-Pindyck: geri-alınamazlık primi + bekleme-opsiyonu değeri) · **Last Responsible Moment** (Poppendieck: ertele AMA LRM geçince default'a düşme) · **ADR+status** (superseded, SİLME YOK = m.8 + m.16 birebir) · Decision Journal (Kahneman: beklenen-sonucu önce yaz = m.39 Brier) · **WSJF** (CoD÷iş-boyu = "önem sırasına optimize"nin cevabı) · minimax-regret (Savage) · **reversibility×blast skorlama** (AI-ajan yönetişimi = escalation-ladder'ımızın DIŞ EŞİ, planlama-anında skorla).

**★★ En kritik bulgu — geri-alınabilirlik AMAÇ-FONKSİYONUNU seçer** (§5.4 sentezi): **iki-yönlü kapı** (tekrar eden, olasılık tahmin-edilebilir, hata ucuz) → **beklenen-değer/WSJF (Model A)** · **tek-yönlü kapı** (tek-atış, olasılık bilinmez, felaket-kuyruk) → **minimax-regret (Model C)**. JARVIS bunu SAHADA ZATEN uyguluyor (07-17 V39 "beklenen-değer zemini" + iki blok "minimax karşıt-temel") — formül onu **açık kural** yapar. → §3'teki "ayrışma" (hangi formül?) böylece ÇÖZÜLÜR: geri-alınabilirlik seçer.

**Triangülasyon delili:** escalation-ladder `f(otonomi×geri-alınamazlık×blast)` ↔ dış "otonomi tavanı geri-alınamazlıkla ters orantılı" neredeyse birebir → formül **sezgisel değil, temellenmiş** (A7'de "türetilmiş" etiketi alır). **07-15 "RİSK sütunu"** (Salih'in 4. boyut adayı) bu alanın TOHUMU — öneri onu formalleştirir, yeni boyut icat etmez.

**⚠ Uyarı — cost-of-change eğrisi (Boehm):** "rework önle" motivasyonu olur AMA **kanıt sayma** — Beck XP-2'de geri çekti, ampirik desteksiz; rework'ü azaltan = feedback-loop + tersinirlik-tasarımı (test/CI/aşamalandırma/YAGNI), eğriyi varsaymak değil.

## 5. Somut öneri (Atlas rafine; tartışma; karar Salih+Fable'da)
**(A) senaryo-defteri alanı** (m.37 "Karşıt-temel:" satırı gibi; 07-15 "RİSK sütunu"nu formalleştirir, yeni boyut icat etmez):
```
- Geri-alınabilirlik (m.37 ek): [İKİ-YÖNLÜ | TEK-YÖNLÜ | KARMA]
  · blast:[dar|orta|geniş] · geri-alma:[ucuz|orta|pahalı]
  · LRM:[tarih/koşul | "yok"] · Kapı:[Katman-2 | Katman-1]
  · not: {hangi opsiyonu kapatıyor — ADR "consequences" muadili}
```
Doldurma planlama-anında: `Kapı` = geri-alma × blast türevi (pahalı ∨ geniş → Katman-1); `LRM` tek-yönlü kararda ZORUNLU (boşsa "bekleme opsiyonu ne zaman ölür?" cevapsız → blok eksik). Ucuz form (3 enum+tarih+satır) → m.37 "optimizasyon anti-optimizasyona dönmesin" şerhine uyar.

**(B) İki AYRI skor (Atlas'ın kritik dersi — karıştırma):**
- **KAPI:** `K = geri-alınamazlık × blast; K≥θ → Katman-1 + LRM'e kapıla, K<θ → Katman-2 serbest.` (reversibility daha ağır: `irr^a·blast^b, a>b`).
- **SIRA (WSJF türevi + bayatlık):** `Değer-yoğunluğu = (Değer + Zaman-kritikliği + Risk/Fırsat + Bayatlık(t)) / İş-boyu.`
- **ETKİN ÖNCELİK:** `EÖ = Değer-yoğunluğu × Φ`; **Φ=1** iki-yönlü (hemen/paralel/ucuz-önce) · **Φ=τ** tek-yönlü, `τ = 1 − (LRM'e slack / pencere)` (LRM uzak→τ≈0→BEKLE; LRM yakın→τ→1→öne fırla, default'a düşmesin). = "geri-alınabilir önce, geri-alınamaz son-sorumlu-ana bastır, LRM'de otomatik öne çek."

**(C) Bağlar:** yakınsama-ödülü `desirability' = desirability + λ·geri-alınabilirlik` (ceteris paribus tersinilir modeli ödüller — reel-opsiyon "flexibility=value" seçim-mekanizmasına gömülü) · kararlar-kısmı onay-derinliği bu alandan türer · **m.31 değişmez** ama `K=irr×blast≥θ` ile SAYISALLAŞIR (A7'de "türetilmiş" etiketi) · ADR superseded-modeli = m.8 silme-yasağı + m.16 zaten defterde işliyor.

## 6. Açık sorular (Salih cevabı bekleniyor — KARAR ALINMADI)
- Geri-alınabilirlik alanı senaryo-defterine mi (her karar), yoksa yalnız ölçek-eşiği üstü kararlara mı?
- Öncelik-formülü: hangi model (A beklenen-rework / B opsiyon / C worst-case) varsayılan? (yoksa hibrit mi?)
- Geriye dönük: mevcut senaryo-defteri kararlarına retroaktif etiketleme yapılsın mı?
- desirability'ye geri-alınabilirlik terimi eklensin mi (yakınsama raporu §5.2 ile birleşim)?
