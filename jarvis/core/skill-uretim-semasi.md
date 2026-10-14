# Skill-Üretim Şeması v1 — Kapı-Ağacı (hallucination-freni) · aktif: Salih emri 2026-08-15

*Salih'in tasarımı ("kökten dallara akan boolean ağaç; her düğüm matematiksel-anlamlı koşul; en alt dala ulaşan aday skill olur; yol = tür") araştırma-sınanmış hâli. Kanıt: `cc/rapor/2026-08/rapor-2026-08-15-1.md` (m.40b tam şerit: 4 aile × tez→CoVe-Factored antitez→V26→maskeli hakem, 16 işçi; 39 `SAĞLAM` · 54 `DARALDI` · 1 `DÜŞTÜ` · 0 **çelişkili**). Tüm sayısal eşikler **deneysel** m.29 (kör-nokta: kapı-ağacı ↔ LLM-skill için ölçülmüş çalışma `YOK`; sayılar klinik/JIT/tezaurus/checklist alanlarından TRANSFERdir — üst-sınır olarak alınır, ölçümle kalibre edilir). Koşum skill'i: `.claude/skills/skill-kapisi/` · graf kaynağı: `core/skill-uretim-semasi.d2` (D2 — Salih 08-15: graflar D2 ile; render türev artefakt `raporlar/2026-08/2026-08-15-skill-uretim-semasi.svg`) · deterministik denetim: `.claude/skills/skill-kapisi/scripts/kapi-denetim.py`.*

## 0. Beş tasarım ilkesi (kanıttan)
1. **Yapı = ağaç-yürüyüşü + faset-demeti.** Kabul yürüyüşü **tek** yol (hit-policy **unique** — bir aday tek yaprağa düşer; iki şekle birden uyuyorsa **böl** = tek-sorumluluk kuralı, **dmn unique** ihlali). Tür = yol (birincil şekil) + yürüyüşte toplanan fasetler (**collect**: tetikleyici · yürütme-yeri · yan-etki · basamak · köken). Formalizm çoklu-ebeveyne izin verir (attack-tree = rooted DAG; SKOS polihiyerarşi) — tek-ebeveyn kilidi **bizim** eklediğimiz aksiyomdur, açıkça yazılır; döngü **yasak**. [A-YT1, A-YT3, D-YT6]
2. **Katman sayısı kanıtla değil amaçla savunulur.** Saf AND/OR ağacında derinlik kabul-kümesini değiştirmez (Mauw&Oostdijk Thm 1-2, **fta**→**dnf**); bizim ağaç faset (öznitelik) de ürettiği için derinlik **sabitlenir**: 4 kapı katmanı + yaprak (**esi** v5: 4 karar noktası/5 yaprak; Stage-Gate tipik 5, riske ölçekli). Katman-başına düğüm ≤5 (kanon dal-bütçesi; checklist artefaktı <10 üst sınır); toplam kapı kalemi ≤19 (**who** checklist analoğu). Bir düğümün ya 0 ya ≥2 çocuğu vardır (tek-çocuklu katman = dejenere kapı). Cowan ~4 / Miller 7±2 bu şemaya **taşınmaz**. [A-YT2, A-YT5, D-YT8]
3. **Sıra: ucuz+çok-eleyen önce; öncelik-kısıtı rank'i ezer.** Bağımsız kapılarda beklenen-maliyet-minimum sırası c_i/(1−p_i) artan (Teorem, ≡ DB rank kuralı). Öncelik kısıtı: GEREK/çözülebilirlik → **değer** → (inşa) → **topraklama** → **biçim** (Voyager ablasyonu: görev-seçimi −%93 > doğrulama −%73; artefakt yokken doğrulama yapılamaz). Erken çıkış her katmanda (**esi**). [A-YT6, A-YT7, A-YT8, C-YT4]
4. **Tekrar ≠ doğrulama; kapı prompt'la kurulmaz.** Aynı-model tekrar geçerlilik kanıtı değildir (halüsinasyonların %43'ü 10/10 yeniden üretilir) → tekrar sayacı yalnız **aday-tetikleyici** (m.43 ile uyumlu: aday ≠ üretim). "Uydurma" talimatı ölçülür etki vermez (−2,7/−1,1 puan), öz-gözden-geçirme prompt'u akıl-yürütmeyi **düşürür** (GSM8K 95,5→89,0) → her kapı **yapısal** dış sinyale bağlanır (script/kaynak-denetimi/eval/dış-kayıt); üretici ≠ doğrulayıcı; doğrulayıcıya iddia verilir gerekçe verilmez (CoVe-Factored). Aynı katmandaki kapılar **farklı** hata sınıfına bakar (korelasyonlu kapılar ∏-formülünü sahte-güvenliğe çevirir). Her kapı bedel-defteri taşır (yanlış-negatif bedeli — CoVe doğru varlıkların %36'sını da eler). [C-YT1..3, C-YT7, C-YT8]
5. **Sabit n yok; eşik = beyan edilmiş (τ, önsel) ∨ ardışık test; sayaç pencereli; değer = tekrar × iş-boyutu.** N=3'ün matematiksel içeriği yoktur (Fowler/Roberts konvansiyonu; ampirik dayanak 0). Türetim: Laplace P(tekrar|k)=(k+1)/(k+2) ≥ τ ⇒ k ≥ (2τ−1)/(1−τ); **beyan edilen eşik k=3 (Karar 78 08-29: birim=görev gerekçesiyle — zincir 3→5→3, uniform önselde τ≈0,8; ara beyan k=5 Karar 30 "zorlaşsın")** — eski beyan τ=0,8 ⇒ k=3 idi (Jeffreys önselinde k=2) — m.43'ün eşiği bu beyanla anlam kazanır. Sayaç ömür-boyu toplam değil son-W-pencere (PyPy decay, TinyLFU reset); eşik çıplak sayı değil bütçe: n×Δ ≥ C_inşa (V8 bütçe = katsayı × bytecode_length; **xkcd** 1205 = Δ×sıklık×ufuk; xkcd 1319 bakım payı). iid varsayımı şerhli (ajan tekrarları bağımsız değil → τ üst-sınır/sezgi düzeyinde). [B-YT2, B-YT3, B-YT6, B-YT7]

## 1. Ağaç (özet — makine-okur kaynak: `core/skill-uretim-semasi.d2`)
```
K0 GEREK ──hayır──▶ RET-0 (aday değil)
  │evet
K1 DEĞER (Z1 ∨ Z2) ──hayır──▶ BEKLET (kutu; sayaç işler; zayıf-yeni → Z2 = Salih onayı)
  │evet
[İNŞA — eval-önce: ≥3 eval → baseline → minimal gövde]
  │
K2 TOPRAKLAMA (R ∧ İ ∧ ¬P) ──hayır──▶ ONAR-2 (eksik liste; ≤3 tur, sonra BEKLET)
  │evet
K3 BİÇİM+TÜR (şekil FIRST: T-R > T-O > T-Y > T-Ü; F1..F5 ∧ tür-özel) ──hayır──▶ ONAR-3
  │evet
YAPRAK: ÜRET-{R|O|Y|Ü} × {yeni|evrim}  →  BAKIM (ağaç-dışı düzeltme kapısı)
```
Sayım: 4 kapı katmanı · kapı düğümü 1+2+3+4=10 · yaprak 4 · terminal 3 (RET/BEKLET/ONAR) · toplam kalem 17 ≤ 19 · her katman ≤5 düğüm ✓.

## 2. Düğüm sözlüğü (a = aday; H = hazine; her koşul boolean, m.38 bağlaçları)
> **Kod (2026-10-14, md → kod pilotu):** §1 ağacı ve bu bölümdeki kapı formülleri `lean/Kanon/SkillKapi.lean`'de kanoniktir (hüküm fonksiyonu + 5 kanıt; ikili `skillkapi`, test `tools/testler/test_lean_skillkapi.py`). Metinle kod ayrışırsa **kod** kazanır; buradaki metin gerekçe ve kaynak içindir.

### K0 — gerek (kök; eleme kapısı; AND-üstü-OR; ucuz + yüksek-ret)
`K0 := ¬kapsanmış(a,H) ∧ (Y1 ∨ Y2 ∨ Y3)`
- `kapsanmış(a,H) := ∃ s∈H: tetik(s) ⊇ tetik(a) ∧ çıktı(s) ⊇ çıktı(a)` — tam kapsama → RET-0 (NOOP: S-F örneği); **kısmî** kapsama (tetik ⊇ ∧ çıktı ⊉) → aday devam eder ama yaprak = **EVRİM(s)** (yeni skill değil sürüm; **awm** eylem-dizisiyle tekilleştirme).
- `Y1 baseline-boşluk := skill'siz koşumda DRFR'de ≥1 koşul karşılanmadı ∨ 2 bağımsız koşumda çıktı tutarsız` — "Claude'un tek başına kolayca yapamadığı iş" (Anthropic skill-creator; ölçüm değil doküman-otoritesi) → eval-önce adım 1'in kendisi. [B-YT1]
- `Y2 kanon-kuralı := ∃ kural∈kanon: gerekli(a,kural) ∧ kural∈LAZY` — iş, sıcak bağlamda olmayan bir kural/pointer setini taşımayı gerektiriyor.
- `Y3 araç-zinciri := |adım(a)| ≥ 3 ∧ sıra sabit` — 3-soru kapısında ≥2 evet (adım tahmin edilebilir · sabit yol) → B3/B4 adayı.
- Hayır → **RET-0** (kutuya girmez; tek-adımlı sorgu için skill yok — "n ne olursa olsun").

### K1 — değer (sayım kapısı; OR — Salih'in "Y ∨ Z" katmanı; m.43'ün iki paralel hattı)
`K1 := Z1 ∨ Z2`
- **Z1 aşağıdan-veri:** `k_W ≥ k_τ ∧ (Δ̂ bilinmiyor ∨ k_W·Δ̂ ≥ (1+β)·C_inşa)`
  - `k_W` = son W penceredeki tekrar sayısı (oturumlar-arası; özdeş tekrar ve **farklı-bağlam varyantı ayrı sayılır** — varyant sayısı düşükse yaprak "dar-şablon", yüksekse "genel-yetenek" [B-YT7]).
  - `k_τ = ⌈(2τ−1)/(1−τ)⌉`; **beyan k = 3 (Karar 78 08-29 — tekrar-birimi = görev; skill-öncesi loop tekrarı da aynı görev-sayacına sayılır [F2/F3]; τ≈0,8; zincir: 3 → 5 [Karar 30] → 3 [Karar 78, birim gerekçesi] — İB-14'ün τ-çelişki adayı bu beyanla `KAPANDI`)** (m.43 eşiği). W = 90 gün [? deneysel; PyPy decay/TinyLFU reset ilkesi, değer kalibre edilecek]. β = 0,25 bakım payı [? deneysel; xkcd 1319 ilkesi]. Δ̂ = kullanım-başına tasarruf (token+dk; skill-creator with/without çifti; skill-BAŞINA ölçülür, evrensel değer yok [B-YT8]) — inşa öncesi bilinmiyorsa kapı geçer, BAKIM'da ilk pencerede ölçülür.
- **Z2 yukarıdan-ihtiyaç:** `Katman-1 emir(a)` (Salih beyanı) → bütçe atlanır; **K2/K3 atlanmaz** (topraklama ve biçim her zaman).
- Hayır → **BEKLET**: kutu satırı + sayaç (`kuyruk/skill-fikir-kutusu.md` m.43 sayaçları); zayıf-yeni aday (k_W<k_τ) yalnız Z2 yoluyla geçer = kanondaki "Salih onayı" hükmü.

### [inşa] — eval-önce (K-016): ≥3 eval yaz → skill'siz baseline → eval'i geçen minimal gövde → K2'ye gir. (Artefaktsız topraklama yapılamaz — sıra sözleşmedir.)

### K2 — topraklama (eleme kapısı; and; hallucination-freni — yapısal dış sinyal)
`K2 := R ∧ İ ∧ ¬P`
- **R referans-varlığı (deterministik, B4 script):** `∀ r∈ref(a): var(r)` — gövde+description'daki her dosya yolu / tüzük maddesi (m.NN) / skill adı / araç-komut yetkili kayıtta **var** (repo · tüzük indeksi · hazine listesi · `which`). Kök halüsinasyon kapısı: dış-kayıt kontrolü; çapraz-model uzlaşı ya da tekrar **ikame değil** (5 sınır modelin ortak uydurduğu 127 paket). [C-YT1]
- **İ iddia-topraklama (bağımsız doğrulayıcı, CoVe-Factored):** `∀ c∈iddia_sayısal(a) ∪ örneklem(iddia(a), n_val): kaynak(c)∈kanon∪URL ∧ doğrulayıcı(c)=TUTUYOR` — doğrulayıcı ≠ üretici; yalnız **iddia** verilir; n_val = min(|iddia|, max(3, ⌈|iddia|/2⌉)) [? deneysel; literatürde n=3 "yetersiz belgeli"]. **tutmuyor** → o iddia K/X'e ya da çıkar. [C-YT5, C-YT6c]
- **¬P prompt-kapısı yasağı:** `kapı(a) ⊆ {script, kaynak-denetimi, eval, dış-kayıt}` — skill'in kendi kalite-kontrolü yalnız "dikkatli ol / uydurma" talimatından ibaretse kapı **sayılmaz** (etkisiz ölçüldü). [C-YT3]
- Hayır → **ONAR-2** (mekanik eksik-referans/iddia listesi ile geri; ≤3 tur, sonra `BEKLET`). Onarım = ayrı düğüm (yürütülebilir hata + güçlü model koşuluyla kazandırır — **creator**), eleme değil.

### K3 — biçim + tür (çatal + eleme; first hit-policy şekil için, and biçim için)
**Şekil (first, sıra bildirilmiş: T-R > T-O > T-Y > T-Ü — ilk tutan birincil tür; ikinciller faset olarak collect):**
- `T-R RİTÜEL := tetik(a) ∈ {oturum-sınırı, olay(SessionStart/Stop/…)}`
- `T-O ORKESTRATÖR := çağırır(a) ≥2 skill ∨ ≥1 alt-ajan/pipeline`
- `T-Y YAN-ETKİLİ := ∃ adım: yazar(kanon: core/·CLAUDE.md·.claude/·tüzük·defter) ∨ commit ∨ push ∨ publish ∨ mesaj-gönder`
- `T-Ü ÜRETİCİ := aksi` (rapor/öneri/çeviri/karar-taslağı; cc/·raporlar/·scratchpad yazımı yan-etki sayılmaz)
- İki şekil "birincil" iddiasında eşit ağırlıkta → **unique** ihlali → **BÖL**.

**Ortak biçim koşulları (and; deterministik script F1-F4, F5 hakem):**
- `F1 description := NE + NE-ZAMAN + NEGATİF-TETİK ("KULLANILMAZ/KULLANMA") ∧ 3.şahıs ∧ len ≤ 1024 char` (kanon 07-17; platform kesme 1536 char/skill, CC docs 08-2026) **∧ Σ_H len(desc) ≤ 0,9 × liste-bütçesi = 7.380 char** (%1 bağlam @200k = 2.000 token × **4,1 char/token — çevrim ölçüldü**: Salih /context 08-20, 15 yüklü skill 7.837 char ≈ 1,9k token; KB-19 Karar 33; eski 6-8k belirsizlik bandı kapandı. Aşımda platform en az çağrılanın description'ını **sessizce** düşürür = kaçırılan-tetik mekanizması; yeni skill sığmıyorsa hazine kısaltılır ya da çapa değişikliği Salih'e). [D-YT2]
- `F2 gövde < 500 satır ∧ referans ≤1 seviye derin`
- `F3 evals/evals.json: tests ≥ 3 ∧ should_trigger ≥ 5 ∧ should_not_trigger ≥ 5` (eval-önce; tam description-eval 20×3 = K-016 borcu, kapı değil)
- `F4 numaralı adımlar ∧ "Gotchas" bölümü var` (en yüksek-sinyal bölüm)
- `F5 tek sorumluluk` (şekil UNIQUE'ten türer; description'daki yetenekler tek aileden — hakem)

**Tür-özel koşullar (birincil şekle ∧ collect edilen fasetlere göre):**
- T-Y birincil → `disable-model-invocation: true` **zorunlu** ∧ yan-etki adımı script/plan-validate-execute ∧ m.31 kapısı yazılı. [D-YT3]
- T-R/T-O birincil ∧ yan-etki faseti → yan-etki adımı Salih-beyanına bağlı (özel tetik cümlesi) ∧ m.31 kapısı yazılı (elle-flag zorunlu değil — ritüel UX; doküman "tavsiye").
- T-O → paralellik-uygunluk sorusu gövdede ∧ handoff kontratı (dosya/format) ∧ yürütme-yeri (ana/fork/arka-plan) yazılı. Zincir sınırı için platform tavanı `YOK` (1+5 = kullanıcı-yığması); kanon "~3-4 skill" [A] → düşürüldü.
- T-R → zaman-kayması freni ∧ klasör-ayrımı ∧ staj negatif-tetiği.
- T-Ü → "commit yapmaz" beyanı ∧ çıktı disiplini (D/K/X ∨ ingest zarfı).
- Hayır → **ONAR-3** (mekanik eksik-alan listesi).

### Yapraklar (kabul + tür): `ÜRET-R | ÜRET-O | ÜRET-Y | ÜRET-Ü` × `{yeni | evrim(s)}` + faset-demeti `⟨tetikleyici: kullanıcı-yalnız|model+kullanıcı|olay · yürütme: ana|fork|arka-plan · yan-etki: var|yok · basamak: B2|B3|B4 · köken: aşağıdan|yukarıdan⟩`. Yaprak = kutu satırı "üretildi" + sözlük Skill Hazinesi girişi + tür-demeti (ileride çağrı-grafı düğümü).

### Bakım (ağaç-dışı düzeltme kapısı — esi "reassess", TroVE budama)
- Sayaç pencereli: kullanım(son W) < λ, `λ = max(1, ½·log10(N))` (N = pencere içindeki toplam görev; jarvis ölçeğinde λ=1) → **EMEKLİ-ADAY** (arşiv-pointer; m.8 silme yok). İlk pencerede ölçülen k·Δ < (1+β)·C_inşa → **emekli-aday**.
- Platform eşikleri sürüm-damgalı yeniden okunur (1536/%1/5.000-25.000 compaction; alt-ajan derinliği 5→1→3 oynadı).
- Yukarı-düzeltme: BEKLET'teki aday yeni tekrar/emirle K1'e geri girer.
- **BAKIM-KK — kullanım-kanıtı katmanı (Karar 75, Salih emri 08-29; hazırı temel al: Warp skill-doctor, `~/dev/common-skills/.agents/skills/skill-doctor/`; her şey yerel, transkript dışarı çıkmaz):** periyodik transkript notlaması (verimlilik + kod-kalitesi rubrikleri, 45-gün pencere / 12-oturum örneklem) BAKIM'a üçüncü sinyali ekler — sayaç ve Δ̂ "ne kadar kullanıldı"yı, **bakım-kk** "kullanılınca ne oldu"yu ölçer:
  - **Kanıt-izli öneri kuralı:** skill-düzenleme önerisi **yalnız** başarısız-oturum kanıtına dayanır (ham rubrik puanı <0,5 olan oturumlar); genel best-practice'ten öneri üretilmez; her öneri oturum + puanlayıcı + an atfı taşır (m.39'un bakım karşılığı).
  - **Tetiklenmeme sinyali:** başarısız oturumda tetiklenmesi gereken skill hiç tetiklenmemişse bu çoğunlukla **description** sorunudur → **DESCRIPTION-ONAR adayı** (ONAR-3'ün kullanım-kanıtlı varyantı; İB-07 description-eval'e girdi).
  - **Öneri = diff, dosyaya dokunmaz:** öneriler ayrı dizinde unified-diff olarak durur; uygulanması = **evrim adayı** olarak bu ağaca girer (K0'dan; hızlı yol Z2 Salih imzası). Otomatik uygulama `YOK` (skill-doctor'un "uygulayayım mı" adımı devre dışı).
  - **Kapsama sayacı:** `skill_coverage` (örneklem oturumlarında ≥1 skill tespiti oranı) pencere-başına ölçüm satırına yazılır; düşük kapsama = tetikleme-isabeti sorunu adayı.
  - Tetik: Salih emri ∨ pencere dolumu (45 gün [? deneysel m.29, skill-doctor varsayılanıyla hizalı; ilk koşum 08-29, kalibrasyon 3 koşumda]).

## 3. Bedel-defteri (her kapı için: sinyal türü · yanlış-negatif bedeli · nerede ödenir)
| Kapı | Sinyal | YN bedeli | Ödendiği yer |
|---|---|---|---|
| K0 | baseline koşum + hazine taraması | gerçek ihtiyacın "kolay iş" sanılması | 1 skill'siz koşum (ucuz) |
| K1 | sayaç + Salih beyanı | değerli-ama-nadir işin beklemesi (Z2 kaçış yolu) | ~0 |
| K2-R | script | yol/madde adı değişikliğinde yanlış alarm | ~0 (deterministik) |
| K2-İ | bağımsız doğrulayıcı | doğru iddianın K'ya düşmesi (CoVe: doğru varlıkların %36'sı elendi — bedel **büyük**) | 1 alt-ajan çağrısı |
| K3 | script + hakem | biçim tutuculuğu (iyi ama alışılmadık skill'in onarıma dönmesi) | ~0 |
En ucuz kapı en zayıf kapı değildir burada — çünkü R/K3 deterministik; ama **maliyet-sıralı kapı seçimi yasak** ilkesi korunur: K2-İ pahalı ve bedelli olsa da atlanamaz.

## 4. m.16 çelişki taraması + şerh-adayları (Katman-1)
- **m.43 (eşik):** çelişki `YOK` — eşik sabit sayı değil beyan edilmiş τ'nun fonksiyonu; **Salih 08-20 (KB-18) eşiği doğrudan 5'e beyan etti** (uniform önselde τ≈0,857; 08-15 τ=0,8⇒k=3 beyanı süpersede), sayaç **pencereli** (W=90 gün) + varyant/özdeş ayrımı baki. **Şerh `İMZALANDI` (08-20):** m.43 metnine eşik-revizyonu + gerekçe fıkrası (Rule-of-Three atfı tarihsel not) düşüldü.
- **07-17 standardı ≤1024 char ↔ platform 1536:** çelişki yok (1024 daha sıkı); ama **hazine-toplamı bütçesi yeni koşul** (F1 ikinci yarısı) — **ÖLÇÜM yapıldı (08-20, KB-19):** eşik 7.380 char (çevrim 4,1 ölçülü); o günkü hazine 16 skill = 8.220 char → aşım 840 char. **GİDERİLDİ (08-21, defter Karar 43):** Salih koşullu hükmü ("çapa bilimsel/güncel kaynaklıysa A") — çapa kaynak-denetimi `GEÇTİ`: %1 = platformun kendi sabiti `skillListingBudgetFraction 0.01` (D-YT2 [D], code.claude.com/docs/en/skills, 08-2026; `cc/rapor/2026-08/rapor-2026-08-15-1.md:429`), 200k = KB-03 skill-koşucularının (Opus/Sonnet) penceresi → A dalı: kısaltma turu — 10+1 description tıraşlandı (tetik cümleleri birebir korundu), 8.220 → **7.379 char `PASS`**.
- **07-17 "~3-4 skill zinciri [A]":** platform sınırı **değil** (kullanıcı-yığması 1+5) → şerh düşürüldü; zincir sınırı = bağlam-bütçesi (compaction 5.000/skill, 25.000 toplam).
- **Yan-etkili → `disable-model-invocation`:** yalnız T-Y **birincil** şekilde zorunlu; ritüel/orkestratörün yan-etki adımı Salih-beyanı kapısıyla yeter (mevcut ritüel UX'iyle uyum). 07-17 §4 kuralı **daraltıldı** (doküman "tavsiye" düzeyi).
- **Antitez borcu:** bu şema tam m.40b şeridiyle koştu (08-14 metodoloji borcunun aksine) — kanonlaşma öncesi antitez borcu `YOK`; ölçüm borcu **var** (aşağıda).

## 4b. v1.1 eki — S-kaynak, üç yuva, sınırsız hazine, determinizm katmanı (Karar 96, Salih hükmü 2026-09-15 masa-12; kanıt: md→skill atlas koşumu `cc/rapor/2026-09/rapor-2026-09-15-md-skill-hakem.md`, taslak `kuyruk/skill-uretim-semasi-v1.1-taslak-2026-09-15.md`; deneysel m.29)
- **S-kaynak (üçüncü aday kapısı):** bağlam-uzayı madenciliği — `tools/baglam-skill-aday.py` her md bölümünü boyut × koşulluluk × prosedür × (1 − okunma) ile skorlar; tetik 5 kapanışta bir ∨ sıcak-katman tavan aşımı ∨ Salih emri. Resmî kural (code.claude.com/docs/en/memory, D): "multi-step procedure or only matters for one part of the codebase → skill or path-scoped rule"; CLAUDE.md'de yalnız her seans gereken olgu/kural kalır.
- **Üç yuva (yerleşim kuralı, üç soru):** her seans gerekli mi → `CLAUDE.md` (hedef <200 satır) · yalnız belli dosya/dizinle mi → `.claude/rules/*.md` + `paths:` (dosya okununca yüklenir) · yalnız belli iş türünde mi → skill (description eşleşince yüklenir; metadata ~100 token/skill her seans, gövde <5k token). Taşınan bölüm kaynakta pointer + tek cümle bırakır (m.8, m.20).
- **K0 Y2' koşullu-yük:** `bölüm her seans yükleniyor ∧ (koşul-dili ≥ eşik ∨ adım ≥ 3) ∧ okunma-oranı düşük` — skor katsayıları kalibresiz [?], 10 koşumda ölçülür.
- **Kendinden-üretilen skill freni:** md'den mekanik çıkarma yetmez; eval-önce (≥3 eval + skill'siz baseline) korunur (SkillsBench abstract, D: kuratörlü skill +16,6 pp; self-generated ≈0 ikincil K).
- **F6 seçim-isabeti (hazine tavanı kalktı — Salih 09-15 aynen: "skill hazinesi için tavan limit olmasını istemiyorum … hazine devamlı büyüyecek. odaklanmamız gereken nokta büyüyen skill hazinesini doğru yönetebilmek yani doğru zamanda doğru skilleri hazineden seçip kullanabilme özelliğini korumak"):** KB-19 char tavanı (7.380) ve "yeni skill = emekli-aday" FIFO kuralı `SÜPERSEDE`; yerine dört mekanizma: (i) metadata bütçesi yalnız **ölçülür** (N × ~100 token, seans brifinde satır; uyarı, engel değil) · (ii) description standardı zorunlu: 3. şahıs · NE + NE **zaman** + **negatif** tetik (skill-tetikleme-semasi K2 alanları) + yayın-öncesi 20-sorgu description eval (İB-07 hattı) · (iii) hazine kataloğu `.claude/skills/README.md`: ad · tür (T-R/T-O/T-Y/T-Ü) · tetik cümlesi · icra türü (hangi pipeline/ritüel çağırır) — SessionStart brifine yalnız katalog adresi · (iv) **bakım-kk** tetiklenme isabeti: kaçırılan-tetik + yanlış-tetik + `skill_coverage` pencere başına; isabet düşerse **description-onar** (emeklilik değil). Kaynak: Anthropic "install many Skills without context penalty" (overview, D); seçim yükü description kalitesine biner.
- **Determinizm katmanı:** deterministik adım = script ("low freedom: run exactly this"); plan-validate-execute deseni (ara çıktı dosyaya → script doğrular → uygula); skill metni model-yorumlu kalır → sorgulanabilirlik = script çıktısı + hareket kütüğü (best-practices, D).
- **Görev icrası bağı (Salih: "skiller kalıp prompt … görev icrası tasarımının parçası"):** skill = kalıp-prompt + script; İB-84 A1-A3 görev formatı (md+lojik → json → python) ile aynı eksen: A3'e ulaşan görev = script'li skill adayı. **İcra-türü değerlendirmesi (Salih 09-15 M6):** her aday "hangi icra türünde nasıl kullanılır" satırı taşır (ritüel / orkestratör / işçi emri / öğrenme ürün turu); satırsız aday K1'e giremez.
- **Öğrenmeden skill (Karar 94 EK-4 + Karar 96 M6/M7):** ürün turu adım (g); staj kökenli bilgi **genelleştirilmiş formatta** (işyeri verisi/adı yok, md.49) jarvis hazinesine girebilir — tek hazine, yerleşim icra-türü satırıyla. **Kavram dersi kuralı (Salih 09-15 aynen: "kavram dersi skill olmaz ama kullanılabileceği icra çeşidi ve bağlamı tespit edilerek o icra türü için skille çevrilebilir"):** kavram → icra-türü + bağlam eşlemesi (ör. RoPE/uzun-bağlam → ingest uzun-belge stratejisi); eşleme varsa o icra türü için aday, yoksa `BEKLET` (RET-0 değil).
- **Hız ilkesi (Salih 09-15 M5: "çok fazla kontrol ilerleme hızını yavaşlatır"):** üretim **partisyonlu** — P1 iskelet + description + 3 eval (1 seans) → P2 gövde + skill'siz baseline → P3 topraklama + katalog satırı; kontrol = deterministik script kapıları (K2-R, K3 F1-F5) otomatik; pahalı K2-İ bağımsız doğrulayıcı yalnız T-Y/T-O; Salih kontrolü yalnız yaprakta (yayın) ve hüküm gerektiren yerleşimde.
- **Dağıtım:** yan oturumda üretilen skill branch + PR (Karar 95); merge ana-sıra. **Ölçüm:** `InstructionsLoaded` hook kütüğü (`veri/bronz/talimat-yukleme-olay.jsonl`) S-kaynak okunma ayağı + üç yuva davranışı; 10 koşumdan sonra §5 ile birlikte değerlendirilir.
- **m.16:** m.43 çelişki yok (ikinci giriş kapısı) · KB-19 tavan → süpersede (Salih 09-15) · m.20/m.8 uyumlu · İB-81 erteleme dokunulmadı.

## 5. Ölçüm planı (deneysel damgayı kaldırmanın yolu)
Her `skill-kapisi` koşumu `kuyruk/skill-fikir-kutusu.md`'ye tek satır: aday · katman-başına geçti/düştü · tür · süre. 10 koşumdan sonra: (i) hangi kapı en çok eliyor (c/(1−p) sırası doğrulanır), (ii) yanlış-negatif vakaları (sonradan gerekli çıkan RET/BEKLET), (iii) τ/W/β/n_val kalibrasyonu. **BAKIM-KK koşum satırı (Karar 75):** tarih · örneklem n · verim/kalite ham ortalama · skill_coverage · öneri sayısı (kabul/toplam) — aynı dosyaya. Kör noktalar tam listesi: rapor "Kör noktalar" bölümleri (45 kalem).
