# Planlanmış Optimize Etme Fikirleri — Rapor + Fikir-Kutusu Bloğu Adayı (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); merge/canon=Fable (m.41). Kaynak: Salih 07-18 — "ileride optimizasyon gerektiğinde neler yapabileceğimizi konuştuk, not aldık, yöntemler oluşturduk; bunlar için **'Planlanmış Optimize Etme Fikirleri'** diye bir fikir-kutusu bloğu; şimdiye kadar yaptıklarımız + gelecekte yapabileceklerimiz bağlamında araştır." **Bu blok = fikir-kutusu ADAYI; m.41: Fable/ana-sıra fikir-kutusu.md'ye işler.** Atlas backlog-yönetim şeridi koşuyor (§3 dönünce rafine).

---

## 1. Neden bu blok (kanon bağı)
- **m.5 (sorun-güdümlü iterasyon):** erken optimize etme; sigortalar hariç. → optimizasyon ERTELENİR, tetikle çalışır.
- **m.37 yakınsama:** iş sınıfı "tek promptta çözülür" olgunluğuna ulaşınca optimizasyon DURUR. → her madde bir yakınsama-hedefi.
- **A7 (matematiksel-temel denetimi kuyruğu):** sezgisel eşiklerin türetilme kuyruğu zaten böyle bir backlog — bu blok onu genelleştirir.
- **Bağ:** her madde geri-alınabilirlik raporu (6) alanıyla + WSJF önceliğiyle etiketlenir; tetik = senaryo-defteri verisi/eşiği.

## 2. ★ Blok içeriği — bu oturumun + bilinen deferred optimizasyonları
Şema (her madde): **ad — tetik-koşulu · bağımlılık · beklenen-kazanç · maliyet · geri-alınabilirlik · kaynak-pointer.**

| # | Optimizasyon | Tetik-koşulu | Bağımlılık | Kazanç | Maliyet | Geri-al. | Kaynak |
|---|---|---|---|---|---|---|---|
| O1 | Otonomi merdiveni derinliği (RC→/goal→/loop→Routines→Dispatch; "canlı ajan" çizgisi) | Salih K-009 açılış beyanı | loop-eng F2/4 (karşılandı) | otomasyon kapasitesi | orta | tek-yönlü-orta (mimari) | otomasyon 3model |
| O2 | Ses PoC → tam ses (L1/G5) | L2 formalize + Salih "başla" | G4 guardrail (O4) | hands-free geliştirme | orta | iki-yönlü | otomasyon §L1 |
| O3 | Kararlar kısmı O1-ride-existing → O2/O3 dashboard | karar-hacmi eşiği aşılınca | senaryo-defteri + köprüler | uzaktan karar hızı | O1 düşük/O3 yüksek | iki-yönlü | otomasyon §9 |
| O4 | PreToolUse guardrail + SessionStart hook | gözetimsiz dilim ÖNCESİ (G4<G5) | — | yapısal güvenlik | düşük | iki-yönlü | CC §6 |
| O5 | Yakınsayan formül (Contextual-TS/BOHB) | yeterli senaryo-defteri verisi + K-020 infra | senaryo-defteri hacmi | skill-arama yakınsar | orta | iki-yönlü | yakınsama §5.2 |
| O6 | Durağan-olmama düzeltmesi (discounted/kayan-UCB) | O5 canlı + kayma gözlenince | O5 | garanti korunur | orta | iki-yönlü | yakınsama §5.4 **(NEXT WAVE #1)** |
| O7 | 4-facet kategorizasyon + taksonomi-indüksiyon (TnT-LLM/kümeleme) | skill-kutusu dolup düz-uzay yavaşlayınca | skill-fikir-kutusu | arama-uzayı yapılanır → yakınsar | orta | iki-yönlü | yakınsama §4 |
| O8 | Geri-alınabilirlik alanı + WSJF öncelik | karar-hacmi + plan-çakışması | senaryo-defteri | rework önlenir, plan optimize | düşük | iki-yönlü | reversibility rapor (6) |
| O9 | karar-hatti bileşik skill + skill-creator eval | K-016 açılış | K-015 DONE | karar-hattı otomatik | orta | iki-yönlü | skill raporları (2,4) |
| O10 | desirability ödül + regret-eğrisi ölçümü (senaryo-defterine) | ilk V39/K-020 koşumu | ölçüm-infra | yakınsama ÖLÇÜLÜR | düşük | iki-yönlü | yakınsama §5.3 |
| O11 | Meta-öğrenme (L2O "formül=politika") | yeterli görev-verisi (uzun vade) | O5 + hacim | context→kombo politikası | yüksek | iki-yönlü | yakınsama §5.1 |
| O12 | A7 matematiksel-temel denetimi (sezgisel→türetilmiş) | iş bitince (kapanış adımı) | tüm deneysel rakamlar | rakamlar temellenir | orta | iki-yönlü | m37-taslak A7 |
| O13 | Modern-tokenizer kesin ölçümü | öğrenme P2+ | — | TR/EN oranı kesinleşir | düşük | iki-yönlü | kapsül açık-borç |
| O14 | K-019 kutu-damıtma + boyut-izleme + prefix-ölçeklenme | ilk boş vardiya | — | bağlam-boyut sigortası | düşük | iki-yönlü | pano K-019 |

**Not (kendine-referans):** Bu blok, geri-alınabilirlik+WSJF çerçevesini (bu oturumun 6. raporu) KENDİ optimizasyon-backlog'una uyguluyor — sistem kendi çıktısıyla kendini organize ediyor (m.35 tezinin küçük örneği).

## 3. Backlog yönetimi (Atlas — DONE)
"optimization debt" adında kanonik çerçeve YOK → sentez: **teknik-borç + last-responsible-moment + reel-opsiyon.**
**★ KRİTİK ayrım — iki maliyet sınıfı** (blok şemasına `C_carry` alanı eklenir):
- **Taşıyan borç (C_carry > 0):** ertelendikçe her geçişte sürtünme (faiz işler) → **erken-tetik eğilimli.**
- **Saf spekülatif opsiyon (C_carry ≈ 0):** yakınsayan formül, otonomi merdiveni gibi — beklerken BEDAVA → **reel-opsiyon; belirsizlik/LRM'e dek beklet, ÇOĞU BUDANIR** (YAGNI kazanır). *Oturumun O1-O14'ünün çoğu C_carry≈0 = saf opsiyon → armed + çoğu asla exercise edilmez.*
**Çerçeveler:** WSJF (CoD÷iş-boyu) · Cost-of-Delay (Reinertsen: sezgisel tahmin ~50× sapar → sayısallaştırma tek başına kazanç) · RICE/ICE (belirsiz maddeye; düşük Confidence skoru otomatik bastırır) · Knuth premature-opt (= **m.5 atası**) · LRM (Poppendieck) · YAGNI (4 maliyet: build/delay/carry/repair) · Reel-opsiyon (McDonald-Siegel: belirsizlik↑→bekleme değeri↑; convenience-yield = şimdi-yapmanın getirisi) · Improvement Kata · Technical-Debt Register · ADR (append-only; **resmi "deferred" statüsü YOK** → uyarlanır).
**Blok şeması eki:** her maddeye `C_carry` + `Durum: deferred|armed|triggered|dropped` + `son-gözden-geçirme` (hijyen).
**Backlog-hijyen (rot önleme):** periyodik denetim + oto-bayrak (bayat+hizasız kapat) · **aynı-format kuralı** (ikinci-sınıf liste kurma; normal işle aynı birim) · herkes bayrak asabilir · **★ m.37-yakınsama budaması** (bir iş-sınıfı yakınsadı → o sınıfın tetiklenmemiş C_carry≈0 maddeleri budanır = **opsiyon vadesi doldu**) · **"drop" ≠ sil** (m.8: `dropped` damgası + gerekçe, arşive iner).

## 4. Tetik-koşulu formülü (Atlas — DONE; iki katmanlı)
**Katman 1 — KAPI (un-defer eşiği):** `P(gerek) · E[V] − C_carry·t − fırsat_kaybı > OptionValue(bekle)`. Ama bu tek başına ERKEN tetikler → reel-opsiyon düzeltmesi (belirsizlik↑ → OptionValue↑ = **m.5**; LRM'de OptionValue→0 = **m.5 istisnası**):
```
armed → triggered  ⟺  ANY:
  (a) belirsizlik çözüldü → P(gerek) ≈ 1 (spekülatif değil, kanıtlı ihtiyaç)
  (b) Son-Sorumlu-An yaklaştı (LRM; beklemek bir alternatifi öldürecek)
  (c) ağrı-sinyali eşiği aştı (ölçülebilir metrik)
```
**Ağrı-sinyali örnek eşikleri (soyut→somut):** O5 skill-formül: "aynı 2 skill elle ≥3× ardışık kombinlendi" · O7 kategorizasyon: "sınıflandırılamayan kart > N" · O1 otonomi: "aynı onay-tipi ≥K ardışık sorunsuz → bir üst basamak."
**Katman 2 — SIRA (aynı anda çok armed):** `WSJF = CoD/İş-boyu` (olgun) veya `RICE = (Reach·Impact·Confidence)/Effort` (belirsiz; düşük Confidence skoru bastırır — spekülatif için doğru).

## 4.5 Ek kanon bağı (Atlas)
- **m.5 "sigortalar hariç":** yüksek-zaman-kritiklik/risk (geri-alması zor, güvenlik) maddeler `armed` değil **doğrudan yüksek-WSJF** — m.5 bunları önden yapmaya zaten izin verir.
- **m.37 yakınsama = budama motoru:** her POP'a `Sınıf` etiketi; senaryo-defteri o sınıfın karar-tekrarını = yakınsamasını ölçer; yakınsayınca opsiyon vadesi dolar → budanır.
- **Ayrım (karıştırma):** **skill-fikir-kutusu = NE inşa edilecek** · **POP = NE ZAMAN olgunlaştırılacak** (meta-kuyruk). senaryo-defteri = *neden ertelendi*; POP = *ne zaman kalkacak*.

## 5. Açık sorular (Salih cevabı bekleniyor — KARAR ALINMADI; rapora taşındı)
- Blok nerede yaşar: `fikir-kutusu.md` içinde "Planlanmış Optimize Etme" bölümü mü, ayrı `kuyruk/planli-optimizasyon.md` mi?
- Tetik: elle mi (Salih/Carvis beyanı) yoksa otomatik-eşik mi (senaryo-defteri ağrı-sinyali)?
- Öncelik-skoru: WSJF mi, basit değer×geri-alınabilirlik mi, geri-alınabilirlik raporunun (6) formülü mü?
- Backlog budama periyodu (backlog-rot önleme) ne olsun?
