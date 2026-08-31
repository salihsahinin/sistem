# İB-67 — Paper-adayı bulgu envanteri + literatür-yenilik doğrulama atlası

**Künye:** emir `cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md` · HEAD `5218209` · **AS-OF 2026-08-31** · ajan sayısı 10 (C 2 · A 3 · B 3 · V26 1 · hakem 1) · işçi modeli **sonnet** (rejim maliyet-öncelikli, 10-15 araç/işçi) · hakem **opus** (maskeli) · İB-68 ile **ORTAK TARAMA** (tek koşum, iki rapor).

**Sınıf:** H≥7 (atıf/URL yoğun). Her yenilik iddiası DESTEKLİ / DAYANAKSIZ / ÇELİŞİR etiketli; kaynak bulunamayan hücre `[?]`, uydurulmadı. Bu rapor **hüküm vermez** — masa-kalemi taslağı üretir (m.31, karar Salih'in).

---

## 0. Ana bulgu (çıplak)

8 aday adversarial taramadan geçti. **YOK-bulundu 0 · KISMİ 5 · DÜŞTÜ 3.** Yani hiçbir aday "literatürde eşdeğeri yok" hükmünü alamadı; 3 aday doğrudan düştü.

Yapısal uyarı (hakem tespiti, bu koşumun en önemli metodolojik bulgusu): **8 işçi raporunun tamamında birincil kaynak yalnız 1 kez açıldı** (IFScale, arXiv 2507.11538). Dış-kaynak ailelerinde (A1/A2/B1/B3) hakemden **sıfır D** çıktı. Dolayısıyla buradaki "DÜŞTÜ" hükümleri arama-sonucu düzeyinde sağlam, "KISMİ" hükümlerinin bir kısmı ise **negatif kanıt zayıflığından** kaynaklanıyor — "bulamadık" ≠ "yok". Paper kararı öncesinde birincil-kaynak açma turu şart (masa-kalemi 3).

---

## 1. Aday × yenilik-durumu × en-yakın-komşu × kanıt tablosu (AS-OF 2026-08-31)

| # | Aday | Repo-pointer (çalışan kanıt) | Elde olan ölçüm | Yenilik durumu | En-yakın-komşu (arama-sonucu; açılmadı) | İddia etiketi |
|---|---|---|---|---|---|---|
| ① | İB-53 — `dosya:satır` + layout **birleşik IR** şeması | `raporlar/2026-08-29-ib53-atlas.md`; `raporlar/2026-08-29-ib53-kapsama-haritasi.md` §1-§4 | dosya_pointer ref 9.793 (çözümlü 8.487 · kırık 1.306); satırlı pointer 380 | **KISMİ** | SourcetrailDB (kod-indeks, layout yok) · Source map spec `tc39.es/ecma426` · lcodemaps · Parse-Then-Place (arXiv 2308.12700) · Numbat/Pyrrha | **DAYANAKSIZ** — "emsalsiz" hükmü SARIF/Sprotty/mdast-Point/Pandoc sourcepos ile hiç karşılaştırılamadı `[?]` |
| ② | İB-49 — D2 dili LLM üretim/okuma mini-eval | `raporlar/2026-08-29-ib49-d2-mini-eval.md`; harness `tools/d2-eval.py`; `veri/d2-eval.jsonl` | üretim 58/58 P=R=1,0 (5/5 birebir) · okuma kenar-listesi 24/25=0,96 ↔ SQL 25/25=1,0 · token 2,4 KB ↔ 13,0 KB = **5,5×** | **KISMİ** (havuzda YOK-bulundu'ya en yakın) | MermaidSeqBench (2511.14967) · OmniDiagram (2604.05514) · M3²Bench · DW-Bench (2604.18964) · Lost-in-Serialization (2511.10234) · ONTO (2604.17512) · GraphLLM | **KARMA**: "D2 için benchmark yok" alt-iddiası **DESTEKLİ**; "tool-offload > metin-sayma" ve "biçim↔token farkı" mekanizmaları **DAYANAKSIZ** (zaten kaplı) |
| ③ | İB-63 / `paralel-kapi` — Bernstein-koşullu, LLM'siz, koşum-**öncesi** eşzamanlılık kapısı | `tools/paralel-kapi.py`; `veri/manifest/*.json` (17 manifest); `raporlar/2026-08-30-paralel-kademe-pilot.md` | 8 birim / 28 çift matrisi · N=1→2→3 kademe · çakışma 0 · kapı çıkışı 0 · ~14 eşzamanlı ajan | **KISMİ** | **CoAgent (arXiv 2606.15376)** — Bernstein'ı LLM-ajanlarına uyarlıyor ama LLM'i conflict-yargısına dahil ediyor · Position: MAS Should Prioritize Concurrency Control (2608.18092) · **ATM: CID-Brokered Pre-Write Admission (2607.00041)** — başlık çok yakın, içerik açılmadı `[?]` · LatticeMind (2608.08236) | **DAYANAKSIZ** — CoAgent aynı problem uzayında rakip çözüm; ayakta kalan fark yalnız "LLM'siz + beyan-edilmiş manifest + koşum-öncesi" bileşimi |
| ④ | gnhf vakaları — otonom-araç × repo-freni çarpışması + önbellek-okumalı iterasyon-tabanı (~300k) + ajan-turu-uykusu maliyet sınıfı | `raporlar/2026-08-31-k010-a3-loop-1.md:12-13` (e600a7: 3M tavan, 3/3 iterasyon, 0 arıza); `tools/gnhf-izle.py` | 3M token tavan · 3/3 iterasyon 0 arıza; "~300k taban" `[?]` (bu koşumda birebir doğrulanmadı) | **DÜŞTÜ** | Don't Break the Cache (2601.06007) · BAGEN: Are LLM Agents Budget-Aware? (2606.00198) · IterResearch (2511.07327) · AgentDoG 1.5 (2605.29801) | **DAYANAKSIZ** — cache-read/bütçe-farkındalık mekanizması yerleşik; kalan kısım olgu-kaydı, yenilik olarak çerçevelenemiyor |
| ⑤ | İB-57 — `ask_oran` proxy'siyle iş-sınıfı → yüzey türetme | `raporlar/2026-08-29-ib57-headless-esleme-taslak.md` §0-§3; `tools/headless-esleme.py` | 47 sınıf: ANA-SIRA 3 · BELİRSİZ 11 · HEADLESS-ADAY 6 · ZATEN-HEADLESS 27 (62 oturum / 4.206 çağrı tabanı) | **DÜŞTÜ** | **HiL-Bench (2604.09408)** — ask-rate'i doğrudan ölçüyor, "judgment, not capability" · **Levels of Autonomy (2506.12469)** — log'dan post-hoc otonomi sınıflandırması · Uncertainty-Aware Clarification (2606.03135) · DeskCraft (2606.03103) | **ÇELİŞİR** — çekirdek sinyal (soru sıklığı → otonomi) doğrudan komşularda ölçülüyor; geriye yerel eşik seçimi kalıyor |
| ⑥ | K-010 A1-A4 — kanıt-kapılı otonomi merdiveni (koşum-sayılı, takvimsiz; go-gate ≠ reliability) | `kuyruk/k010-zincir-2026-08-29.md:1-56` | A1 5/5 KESİN · A2 kapı tamam · A3 2/3 · A4 bekliyor | **DÜŞTÜ** | Falsifiable Release Gates (2607.13070) · CAGE-1 (2607.03510) · "The Autonomy Gate" (vadim.blog) · "Evidence-Driven Release Gates" — PROMOTE/HOLD/ROLLBACK · Augment Code pilot→production L0-L4 | **ÇELİŞİR** — mekanizma hem akademik hem endüstriyel 5 ayrı komşuyla karşılanıyor; özgün pay yalnız A1-A4 adlandırması |
| ⑦ | İB-51 — 1.017 kural-birimi envanteri + IFScale ≤100 çapası | `raporlar/2026-08-29-ib51-kural-envanteri.md` §1-§3; `raporlar/2026-08-29-ib51-atlas-kural-yukleme.md`; `tools/kural-envanter.py`; `veri/gorunum/v_kural_envanter.csv` | T0+T1 = **71 birim / 21,8 KB**; toplam **1.017 birim / 339.142 B**; eşik hesabı 71 + 2×14,5 = 100 | **KISMİ** (hakem: "havuzun en güçlüsü") | **IFScale (arXiv 2507.11538, 2025-07-15) — BİRİNCİL KAYNAK AÇILDI, %68@500 DOĞRULANDI** · ManyIFEval (Findings-EMNLP 2025) · AGENTIF (Tsinghua KEG) · Many-Tier Instruction Hierarchy (2604.09443) · Curse of Instructions | **KARMA**: dış çapa **DESTEKLİ** (tek doğrulanmış birincil kaynak); "talimat sayısı↔uyum düşüşü" fikri **DAYANAKSIZ** (zaten var); T0-T4 taşıyıcı × görev-sınıfı çapraz tablosuna eşleşme bulunamadı `[?]` |
| ⑧ | İB-66 — gözlemlenebilir nested-loop boşluğu (12 araç × 5 kriter, 0/12) | `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md` §0-§2 | **K1∧K2∧K3∧K4 hepsi EVET: 0/12**; darboğaz K3 (1/12 net EVET); kendi denetimi: V26 doğrulama %55,6, 6 ihlal; hakem D 27/K 11/X 8 | **KISMİ** | From Agent Traces to Trust (2606.04990) — 6 boyutlu provenance taksonomisi · MAST hata taksonomisi · **LumiMAS (2508.12412)** — gerçek-zamanlı çok-ajan gözlem, doğrudan çelişki adayı `[?]` · Confident AI "thread-level observability" `[?]` | **KARMA**: metodoloji (tarama-öncesi sabit kriter + 0/12) ayakta; üst-tez "parçalı gözlemlenebilirlik" **DAYANAKSIZ** (survey'lerde var); LumiMAS açılmadığı için ÇELİŞME riski `[?]` |

**Dağılım: YOK-bulundu 0 · KISMİ 5 (①②③⑦⑧) · DÜŞTÜ 3 (④⑤⑥).**

### Adversarial arama izi (≥3/aday — durma koşulu)

| Aile | Adaylar | Sorgu sayısı | Ham rapor |
|---|---|---|---|
| A1 | ①②③ | 11 (3+4+4) | `cc/rapor-2026-08-31-ib67-a1-literatur.md` |
| A2 | ④⑤⑥ | 9 (3+3+3) | `cc/rapor-2026-08-31-ib67-a2-literatur.md` |
| A3 | ⑦⑧ | 12 (6+6) | `cc/rapor-2026-08-31-ib67-a3-literatur.md` |
| C (iç envanter, web'siz) | ①②⑤⑦⑧ | — | `cc/rapor-2026-08-31-ib67-c-ic-envanter.md` |
| C (③④⑥ kanıtı) | ③④⑥ | — | `cc/rapor-2026-08-31-ib68-c-ic-envanter.md` (ortak; İB-68'de yazıldı) |
| Araç-pratiği ayağı (ORTAK) | tümü | 20+ | `cc/rapor-2026-08-31-ib68-b1/b2/b3-*.md` → **İB-68 raporuna pointer** |

Tüm sorgu metinleri ham raporlarda birebir kayıtlı.

---

## 2. V26 antitez + birincil-kaynak sondajı

Ham rapor: `cc/rapor-2026-08-31-v26-denetim.md`. Örneklem 9 iddia; **7/9 TAM doğrulandı (%78)**, 2/9 KISMİ, **0/9 çürütüldü**.

- **Uydurma arXiv kimliği: BULUNAMADI.** Sondajlanan 6 kimlik (2606.15376 CoAgent · 2607.00041 ATM · 2601.06007 Don't Break the Cache · 2606.00198 BAGEN · 2604.09408 HiL-Bench · 2607.13070 Falsifiable Release Gates) **hepsi gerçek** ve iddia edilen konuyu işliyor. Halüsinasyon freni bu koşumda tuttu.
- **İhlal sayısı: 4** — (1) sayısal-iddia-kaynaksız: B3 raporu açılmamış sayfalardan tutar yazdı (aşağıda), (2-3) açılmamış-kaynağa-"DESTEKLİ" damgası (B1, B2), (4) SEO-gürültü grubu (2026 "best tools" karşılaştırma blogları).
- **m.39 düzeltmesi:** B3 ham raporundaki rakip fiyat tutarları bu senteze **taşınmadı**; yalnız "ücretli plan MEVCUT/YOK" varlık beyanı kullanıldı. Ham rapordaki tutarlar V26 ihlali olarak damgalıdır, güvenilmez.

---

## 3. Maskeli hakem (opus) — D/K/X

Ham rapor: `cc/rapor-2026-08-31-hakem-dkx.md`. 67 iddia: **D 19 (%28,4) · K 31 (%46,3) · X 17 (%25,4)**.

Dosya bazında: ib67-C 12D/5K/3X · ib67-A1 1D/4K/3X · ib67-A2 0D/4K/4X · ib67-A3 1D/4K/0X · ib68-C 8D/1K/1X · ib68-B1 0D/4K/4X · ib68-B2 0D/5K/1X · ib68-B3 0D/3K/2X.

Okuma: **tüm D'ler repo-içi ölçümlerden geliyor.** Sistemin kendi hakkındaki verisi sağlam, dışarı hakkındaki verisi bu bütçede zayıf.

---

## 4. Paper iskeleti (durma koşulu: ≥1)

### İSKELET-1 — İB-49 (hayatta kalan en güçlü aday)

- **Katkı cümlesi:** "Diyagram-dili (D2) üretiminde kural-tabanlı dönüşüm LLM'e deterministik-doğru çıktı verdirirken (58/58, P=R=1,0), aynı grafın yapısal SORGULANMASINDA metin-üzerinden-sayma (%96) yerine sorgunun SQL motoruna devri hatasız (%100) sonuç verir; ve insan-okunurluk ile LLM-girdi-verimliliği arasında aynı bilgi için 5,5× ölçülü bir biçim-ayrımı vardır."
- **Venue sınıfı:** kısa/workshop sınıfı — LLM4Code / MSR / NIER-track / ICSE-workshop; tam-konferans (ACL/ICSE ana track) için ölçek yetersiz.
- **Mevcut kanıt (VAR):** `tools/d2-eval.py` deterministik harness (LLM çağırmaz, stdlib + d2 CLI) · `veri/d2-eval.jsonl` kütük · 58/58 üretim · 25 okuma sorusu (5 soru × 5 işçi) · 2,4 KB ↔ 13,0 KB token ölçümü.
- **Gereken EK deney (kaba maliyet):**
  1. **Örneklem büyütme** — 5 işçi / 5 soru çok küçük; ≥3 model × ≥50 soru × ≥5 graf. *Kaba: 1 orta koşum ailesi.* `[?]` token
  2. **Çapraz-dil kontrolü** — D2 ↔ Mermaid ↔ PlantUML ↔ kenar-listesi aynı grafta; "D2'ye özgü mü, biçime mi özgü" ayrımı. **Zorunlu**, çünkü A1 taraması mekanizma-iddialarını (tool-offload, biçim-verimlilik) zaten kaplı buldu — katkı ancak D2 ekseninde durabilir.
  3. **Baz-çizgi olarak DW-Bench / Lost-in-Serialization protokolüne bağlanma** — "hazırı temel al" ilkesi; kendi metriğini icat etme.
  4. **Kırılma noktası** — graf büyüdükçe %96↔%100 farkının nasıl değiştiği (ölçek eğrisi).
- **Risk:** en-yakın-komşuların üçü (DW-Bench, Lost-in-Serialization, ONTO) katkının iki ayağını zaten kaplıyor; ayakta kalan tek ayak "D2 için ilk benchmark". Bu tek başına workshop sınırında bir katkı.
- **Salih'in rolü / CV bağı (K-004):** harness + veri Salih'in kendi sisteminde üretildi; tekrar-üretilebilir, açık kaynak (md.14 remote private → yayın öncesi Katman-1 kararı gerekir).

### İSKELET-2 (yedek) — İB-51 + İB-66 birleşimi

- **Katkı cümlesi:** "Çalışan bir çok-ajanlı sistemde YAZILI KURAL BÜTÇESİ deterministik olarak ölçülebilir (T0-T4 taşıyıcı × görev-sınıfı, 1.017 birim / 339.142 B) ve dış talimat-uyum eğrisine (IFScale %68@500) karşı yerel bir ≤100-birim eşiği kalibre edilebilir."
- **Neden yedek:** İB-51 tek **doğrulanmış birincil dış çapaya** sahip aday (IFScale açıldı). Zayıflığı: temel fikir (talimat sayısı ↔ uyum düşüşü) zaten yayınlanmış; özgün pay T0-T4 taşıyıcı ekseninde ve bu eksenin literatürde olmadığı **kanıtlanamadı** `[?]`.
- **Gereken EK deney:** taşıyıcı-sınıfı ekseninin ampirik etkisi — aynı kural bütçesi farklı taşıyıcılara dağıtıldığında uyum değişiyor mu (kontrollü A/B). Bu, mevcut kanıtta **YOK**; iddianın tamamı şu an tanımsal.

---

## 5. Masa-kalemi taslağı (Salih'e — hüküm verilmemiştir)

**MK-67/1 — Paper yazılsın mı, yazılırsa hangisi?**
- (a) **İB-49 D2 eval'i workshop kısa-makalesine taşı** — ne demek: ek deney 1-4 koşulur, katkı "D2 için ilk benchmark" ekseninde daraltılır. Artı: elde tekrar-üretilebilir harness ve gerçek sayı var; en düşük halüsinasyon riski. Eksi: katkı dar, iki ayağı literatürde kaplı; venue sınıfı düşük. **Öneri: ilk sırada** — çünkü hayatta kalan tek "ölçüm-ağırlıklı" aday bu.
- (b) **Hiçbiri; önce birincil-kaynak turu koş** — ne demek: 0 paper kararı, bunun yerine ①③⑧ için URL'leri gerçekten açan ikinci tur. Artı: bu koşumun en büyük zaafı (8 raporda 1 açılmış kaynak) kapanır; ①③⑧'in KISMİ'si YOK-bulundu'ya dönebilir ya da düşer. Eksi: bir tur daha maliyet, paper gecikir. **Gerekçe: (a)'nın önkoşulu da bu — sırayla değil, (b) sonra (a).**
- (c) **Paper hattını kapat, bulguları iç kayıt olarak bırak** — Artı: sıfır maliyet, K-015/K-022 saat rekabeti korunur. Eksi: 5 KISMİ aday ölçülmeden gömülür.

**MK-67/2 — Düşen 3 aday (④⑤⑥) ne olacak?** Yenilik yok ≠ değer yok: ⑤ ve ⑥ İB-68'de ürün adayı olarak duruyor. Öneri: paper hattından çıkar, ürün hattında kalsınlar.

**MK-67/3 — Metodolojik borç:** "birincil kaynak açılmadan yenilik hükmü verilmez" kuralı bu koşumda **ihlal edilmedi ama sınırda kalındı** (1/8). Karar: gelecek m.40b koşumlarında işçi başına ≥2 zorunlu WebFetch açma kotası konsun mu?

---

## 6. Ham rapor pointer'ları

- İç envanter (C1): `cc/rapor-2026-08-31-ib67-c-ic-envanter.md`
- Literatür antitez: `cc/rapor-2026-08-31-ib67-a1-literatur.md` · `-a2-literatur.md` · `-a3-literatur.md`
- Araç-pratiği / endüstri ayağı (ORTAK, İB-68'de): `cc/rapor-2026-08-31-ib68-b1-pazar.md` · `-b2-pazar.md` · `-b3-pazar-dagitim.md`
- V26 denetim: `cc/rapor-2026-08-31-v26-denetim.md`
- Maskeli hakem: `cc/rapor-2026-08-31-hakem-dkx.md`
- İkiz rapor: `raporlar/2026-08-31-ib68-urun-aday-envanteri.md`
