# İB-69 aile-1 (d) — Nested-loop eksen eşlemesi: DIŞ-LOOP ↔ İÇ-KOŞUM karar kuralı

AS-OF: 2026-08-31 · Kapsam: yalnız iç kaynak (Read/Grep), web yok, kod koşulmadı. Dil: TÜRKÇE.

## 0. Terminoloji ve semboller

İki eksenli LLM koşum matrisi: eksen `X`, eksen `Y` (kardinalite `|X|`, `|Y|`), hücre = tek koşu. `dış(X)` ≔ X sayaçla dolaşılır, her X-değeri için Y'nin TAMAMI iç-koşum olarak yürütülür (İB-66 §5.1 tanımına bağlı — bkz. §3 aşağıda). `M_X`, `M_Y` = eksen kurulum maliyeti (bağlam yükleme, önbellek, model yükleme). `T` = birim hücre maliyeti (İB-66 §5, gnhf birimi ~300k örneği). Kaynaklar: `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:§5` (seviye tanımı + §5.2 + §5.3 şablon-1/3), `tools/paralel-kapi.py:93-113` (PK-1 Bernstein, PK-10), `raporlar/2026-08-29-ib63-paralel-pipeline-atlas.md:50` (PK-10 tanımı).

## 1. Dört seçim ölçütü — m.38 lojik form

### (i) MALİYET / yeniden-kullanım

**Tanım:** eksen sabitlenince paylaşılabilecek pahalı kurulum (bağlam yükleme, önbellek-okuma, model/skill yükleme) o eksenin DIŞ olmasını gerektirir — kurulum bir kez yapılıp iç-koşumlar boyunca tekrar kullanılır.

```
kurulum_paylasilir(X,Y) ↔ ( M_X ≥ M_Y ) ∧ ( kurulum(X) iç-koşumlar(Y) boyunca DEĞİŞMEZ )
DIŞ_maliyet(X) ↔ kurulum_paylasilir(X,Y) ∧ ¬kurulum_paylasilir(Y,X)
¬(DIŞ_maliyet(X) ∧ DIŞ_maliyet(Y))   [ikisi de kazanamaz — biri sıfır kurulum paylaşımlıysa karar tektir]
```

Örnek: 14 skill × 20 sorgu matrisinde skill tanımı/bağlamı (`SKILL.md`, örnek-vaka) yüklemek pahalı, sorgu değişimi ucuzdur (yalnız değişken enjeksiyonu — bkz `cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md:17` Nunjucks). → skill DIŞ, sorgu İÇ.

### (ii) BAĞIMSIZLIK

**Tanım:** bir eksenin hücreleri birbirinden BAĞIMSIZSA (Bernstein 3/3 ∅ — `tools/paralel-kapi.py:112` `return 'PARALEL-SERBEST', 'Bernstein 3/3 ∅'`) o eksen paralel dış-tur adayıdır; bağımlıysa (bir hücrenin çıktısı bir sonrakinin girdisi/durumu ise) sıralı İÇ olmak zorundadır — çünkü İB-66 §5.1 (iii) "tam kapsama" şartı zaten iç'i sıralı yürütmeyi varsayar.

```
BAGIMSIZ(X) ↔ ∀ i,j ∈ degerler(X), i≠j: cakisma(hücre_i, hücre_j) = ∅ ∧ ¬veri_bagimliligi(hücre_i, hücre_j)
DIŞ_bagimsizlik(X) ↔ BAGIMSIZ(X) ∧ ¬BAGIMSIZ(Y)
BAGIMSIZ(X) ∧ BAGIMSIZ(Y) → ikisi de dış-aday, (i)'e devret  [çatışma çözümü aşağıda §2]
¬BAGIMSIZ(X) ∧ ¬BAGIMSIZ(Y) → nested(X,Y) GEÇERSİZ, iki-loop değil masaya git  [İB-65 S1 madde 1.6 emsali]
```

### (iii) ERKEN-DURDURMA (successive halving)

**Tanım:** eleme (SH/Hyperband tipi budama, `cc/rapor-2026-08-31-ib69-a1-literatur.md:§3` — "en kötü yarıyı eler") yalnız SIRALANABİLİR bir performans sinyali olan eksende yapılabilir; o eksen ELENEBİLİR ise İÇ konuma değil, **rung/round sayacı olarak ayrı bir üçüncü boyut** gerektirir — iki-eksenli matriste doğrudan "dış/iç" ikilisine sığmaz (aşağıda §3'te İB-66 §5.1(iii) ile çelişki not edilir).

```
ELENEBILIR(X) ↔ (∃ kısmi_skor: hücreler(X) SIRALANABİLİR) ∧ (dusuk_performans_alt_kume(X) ATILABILIR)
ELENEBILIR(X) → oncelik(X, "elenen eksen") ∧ ¬zorunlu(dış(X))
   [elenen eksen ne dış ne iç olarak temiz eşlenmez — bkz §3 uyarısı]
¬ELENEBILIR(X) ∧ ¬ELENEBILIR(Y) → bu ölçüt kullanılamaz, (i)/(ii)'ye devret
```

### (iv) PK-10 AYAK İZİ (dosya çakışması)

**Tanım:** aynı dış-loop turunda çalışan hücreler AYNI dosyaya yazıyorsa aynı turda paralel olamaz (`tools/paralel-kapi.py:113` `'SIRALI', 'PK-10 büyüyen iterasyon ayak-izi (v0: seri)'`; İB-65 S1 §4.3 `ayak-izi(A) ∩ ayak-izi(B) ≠ ∅ → ¬paralel(A,B)`).

```
YAZAR_CAKISMASI(X) ↔ ∃ i,j ∈ degerler(X), i≠j: yazilan_yollar(hücre_i) ∩ yazilan_yollar(hücre_j) ≠ ∅
DIŞ_pk10(X) ↔ ¬YAZAR_CAKISMASI(X)   [X sabitken İÇ eksen boyunca yazılan dosyalar ayrık olmalı]
YAZAR_CAKISMASI(X) → X SIRALI (append-only kütükle korunmadıkça) — X dış olsa da olmasa da paralel dış-tur ADAYı DEĞİL
```

## 2. Çatışma önceliği (gerekçeli)

**Sıra: (iv) PK-10 > (ii) BAĞIMSIZLIK > (i) MALİYET > (iii) ERKEN-DURDURMA.**

- **(iv) en üstte:** dosya çakışması bir GÜVENLİK/doğruluk kısıtıdır, zaten koşan tooling'de (`paralel-kapi.py`) sabit uygulanıyor — verimlilik tercihi bunu geçersiz kılamaz; iki hücre aynı dosyaya yazıyorsa hangi eksen "daha ucuz" ya da "daha bağımsız" olduğu önemsizdir, önce SIRALI'ya düşer.
- **(ii) ikinci:** bağımsızlık, paralel dış-tur için YAPISAL ön-koşuldur (Bernstein). Maliyet avantajı varsa da bağımlı bir ekseni dış yapıp paralelleştirmek YARIŞ KOŞULU (race) üretir — kazanç sanaldır, çünkü paralel-serbest hükmü zaten bağımsızlık gerektirir.
- **(i) üçüncü:** PK-10 ve bağımsızlık şartlarını geçen adaylar arasında verimlilik tercihi — hangi eksen daha pahalı kurulum paylaşıyorsa o dış olur.
- **(iii) en altta ve KOŞULLU:** erken-durdurma optimizasyondur, zorunlu bir yapı kısıtı değil; ayrıca §3'te gösterildiği gibi İB-66'nın kendi seviye tanımıyla (tam-kapsama şartı) gerilimlidir — bu yüzden çatışmada ilk üçe HER ZAMAN yenilir; (iii) yalnız ilk üçü BAĞLAMAYAN bir üçüncü "round" boyutu olarak eklenebilir, iki-eksenli dış/iç ikilisinin YERİNE geçmez.

## 3. İB-66 §5 uyum denetimi — matris eksenleri gerçekten SEVİYE mi

İB-66 §5.1 formal tanımı: seviye `L` ⟺ (i) kendi sayacı `i_L` ∧ (ii) kendi durma yüklemi `done_L` ∧ (iii) `L`'nin gövdesi `L+1`'in TAM koşumunu içerir (`raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:§5.1`).

- **(i) sayaç, (ii) durma yüklemi:** iki eksenli çarpım matrisinde (promptfoo tipi, `cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md:7-15`) HER iki eksen de kendi sayacına ve "N. değere ulaştım" durma yüklemine sahip olabilir — bu iki şart matriste doğal olarak sağlanır.
- **(iii) tam kapsama:** BU şart SIKIDIR ve koşulludur. Klasik "grid" matrisinde (promptfoo, İB-49 d2-eval, İB-07 3B grid) dış eksen her değerinde iç ekseni TAM yürütür → dış GERÇEK SEVİYE'dir, İB-66 §5.2 madde-1/3 emsaline uyar ("alt-süreç başlatma… kendi sayacı, kendi durma yüklemi" ya da "tekrar sayacı + kendi done yüklemi olan blok").
- **Ama erken-durdurmalı (SH/Hyperband) matriste bu KIRILIR:** dış tur (round `r`) her değerinde iç ekseni (config kümesi) TAM yürütMEZ — yarısı budanır (`cc/rapor-2026-08-31-ib69-a1-literatur.md:§3` "en kötü yarıyı eler"). Bu, İB-66 §5.1(iii)'ün doğrudan ihlalidir: gövde bir sonraki seviyenin TAM koşumunu kapsamıyor, KISMİ koşumunu kapsıyor. **Sonuç: SH kullanılan bir "dış×iç" matris, İB-66'nın formal tanımına göre GERÇEK NESTED-LOOP DEĞİLDİR** — §5.2 madde-(e) "aynı sayaca bağlı iç for"a da tam uymaz (çünkü iç küme round'lar arasında BÜZÜLÜYOR, sabit değil); en yakın sınıflandırma yeni bir alt-tür olarak masaya gitmelidir (İB-65 S1 madde 1.6: "iç katman terminate etmiyorsa/klasik biçimde kapsanmıyorsa nested değil, masa kararı").
- **"Matris = 2 seviye" iddiası KOŞULLUDUR:** yalnız TAM faktöriyel (erken-durdurmasız) grid için doğrudur. SH/Hyperband eklenirse üçüncü bir boyut (round sayacı) gerekir ve iç ekseni artık "seviye" değil "azalan aday kümesi" olarak modellemek gerekir — bu İB-69-a1-arac raporundaki Optuna `SuccessiveHalvingPruner`in rung/bracket mekanizmasıyla örtüşür (`cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md:38`).

## 4. Somut eşleme — İB-07 (20 sorgu × 3 tekrar × 14 skill)

Kaynak: `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md:§1,§5` (İB-07 satırı) ve `raporlar/2026-08-30-ib07-description-eval.md` (freni kesintisi).

4 ölçütle test:

- **(i) MALİYET:** skill (14) sabitlendiğinde skill-bağlamı/örnek-vakası bir kez yüklenip 20×3=60 sorgu-tekrar çiftine tekrar kullanılabilir → skill DIŞ adayı. Sorgu/tekrar ekseni sabitlense skill bağlamı her seferinde yeniden yüklenir (kazanç yok). **(i) skill'i DIŞ ister.**
- **(ii) BAĞIMSIZLIK:** hem skill hem sorgu hem tekrar eksenleri birbirinden bağımsız (aynı LLM-judge çağrısı başka bir sorgu/tekrar/skill'in sonucuna bağlı değil, `veri/description-eval.jsonl` şeması append-only tekil satır — `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md:15`). **(ii) çatışma çözmüyor — üç eksen de bağımsız-aday**, (i)'e devreder.
- **(iii) ERKEN-DURDURMA:** İB-07'de aday elemesi YOK (altın-etiket karşılaştırması hepsi tam koşuluyor) — bu ölçüt İB-07'de UYGULANAMAZ (`ELENEBILIR` hiçbir eksen için sağlanmıyor).
- **(iv) PK-10:** üç eksen de aynı kütük dosyasına (`veri/description-eval.jsonl`, append-only) yazıyor — bu YAZAR_CAKISMASI'nı append-only zaten ÇÖZÜYOR (çakışma yok, tekil satır kilidi gerekmiyor); dolayısıyla PK-10 hiçbir ekseni dış/iç olarak ayırt etmiyor, nötr.

**Sonuç:** 4 ölçütten yalnız (i) karar veriyor → **skill DIŞ, (sorgu×tekrar) İÇ** olmalıydı (14 dış-tur × 60 iç-koşum), emirdeki gerçek sıralama da zaten böyle görünüyor ("20 sorgu × 3 tekrar × 14 skill" ifadesi sıra belirtmiyor, ama `altin_etiket` skill-sabit karşılaştırma birimidir).

**Ajan-freni 45/60 kesintisi doğru eşlemeyle önlenir MİYDİ — HAYIR.** `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md:48` birebir: ".claude/hooks/pretool-ajan-fren.sh TÜM oturumdaki Agent çağrılarını sayıyor, tek bir görev-emrine özel değil… muhtemelen sayaç seans-genelinde kümülatif". Bu bir **oturum-genelinde kümülatif ajan-sayaç tavanı** (İB-54/Karar 39) — dış/iç eksen eşlemesi bu sayacı etkilemez, çünkü kesinti PK-10 (dosya ayak-izi) sınıfında değil, PK-9/ajan-tavanı sınıfındadır. Eksen eşlemesi optimizasyonu maliyeti/paralelleşmeyi iyileştirir ama bu spesifik kesintinin KÖKÜ farklı bir kısıttır — **[?] doğrulanmadı**: sayaç 60 çağrıyı 45'te kestiyse, dış-tur=skill (14 dış) ile iç-tur=sorgu×tekrar (60 iç) yapısında toplam Agent çağrı SAYISI aynı kalır (60 hücre = 60 çağrı, eksen sırası çağrı SAYISINI değiştirmez) — dolayısıyla eşleme kararı bu arızayı yapısal olarak önleyemezdi.

## 5. Maliyet çarpımı ve erken-durdurma indirimi

- **Toplam maliyet değişmez mi:** hücre başına birim maliyet `T` sabitse, `toplam ≈ |X|×|Y|×T` — çarpım DEĞİŞMEZ hangi eksen dış/iç seçilirse seçilsin (İB-66 §5 çarpım kuralı `∏_L (yineleme_L × birim_L)`, `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:§5.2` "Maliyet sonucu"). **Fark yalnız KURULUM maliyetinde**: dış eksen seçimi kurulum-paylaşımını etkiler (§1-i) — `toplam ≈ |dış|×M_dış + |dış|×|iç|×T_hücre`, `M_dış` az sayıda kez ödenir; yanlış eksen dış seçilirse `toplam ≈ |dış'|×M_dış' + …` ile `M_dış'` gereksiz çok kez ödenir (14 kez skill-yükleme yerine 60 kez).
- **Erken-durdurma indirim formülü** (Hyperband/SH, `cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md:38`, `reduction_factor η` varsayılan 4): iç ekseni ELENEBİLİR bir aday-kümesi olarak modelleyip round-başına `1/η` oranında budarsanız toplam iç-koşum sayısı `|iç| × (1 + 1/η + 1/η² + … )` ≈ `|iç| × η/(η-1)` olur (geometrik seri, tam `|iç|×round_sayısı` yerine) — **indirim yalnız ELENEBİLİR eksen İÇ (aday) konumdayken mümkündür**; dış eksen (round sayacı `r`) elenmez, artan bütçeyle büyür. Eğer bunun tersini yapıp "elenebilir eksen"i dış seçerseniz (her elenebilir-değer için iç'i tam koşturursanız) indirim YOK OLUR — bu da §3'teki uyarıyla tutarlı: elenebilir eksen İÇ/aday-küme rolünde olmalı, dış rolünde değil.

## Kaynak listesi

| Kaynak | Kullanım |
|---|---|
| `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:§5.1,§5.2,§5.3` | seviye formal tanımı, çarpım kuralı |
| `raporlar/2026-08-31-ib65-loop-pipeline-secim-atlas.md:§3` (S1 madde 1.6, §4) | nested geçerlilik, PK-10 madde 4 |
| `tools/paralel-kapi.py:93-113` | PK-1 Bernstein, PK-10 kural kodu |
| `raporlar/2026-08-29-ib63-paralel-pipeline-atlas.md:50` | PK-10 tanımı |
| `cc/rapor-2026-08-31-ib69-a1-literatur.md:§3` | SH/Hyperband erken-durdurma tanımı |
| `cc/rapor-2026-08-31-ib69-a1-arac-promptfoo-optuna.md:7-15,35-38` | promptfoo eksen çarpımı, Optuna SH pruner parametreleri (η) |
| `cc/rapor-2026-08-31-ib69-a1-ic-emsal.md:§1,§5,§48` | İB-07 emsal tablosu, ajan-freni kök-neden alıntısı |
| `raporlar/2026-08-30-ib07-description-eval.md` | İB-07 kesinti durum bloğu (45/60) — [?] bu koşumda ayrıca açılmadı, ic-emsal raporundan alıntı |

**[?] işaretli iddialar:** (a) "eşleme kararı ajan-freni kesintisini önlemezdi" hükmü, ic-emsal raporundaki tek bir alıntıya dayanıyor — hook script'inin (`.claude/hooks/pretool-ajan-fren.sh`) kendisi bu koşumda okunmadı, dolayısıyla sayacın gerçekten "seans-genelinde kümülatif" olduğu BİREBİR doğrulanmadı, yalnız İB-07 raporunun kendi çıkarımı aktarıldı. (b) SH indirim formülündeki `η/(η-1)` yaklaşımı genel bandit-literatür bilgisidir, bu oturumda birincil kaynaktan (Hyperband makalesi tam metni) formül düzeyinde doğrulanmadı — yalnız "adaptive resource allocation and early-stopping" ifadesi doğrulandı (`cc/rapor-2026-08-31-ib69-a1-literatur.md:§3`).
