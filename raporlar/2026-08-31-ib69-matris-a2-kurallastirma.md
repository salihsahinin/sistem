# İB-69 / AİLE-2 — MATRİS-KOŞUMDAN OTOMASYONA: KURALLAŞTIRMA PAKETİ

**Künye:** emir `cc/gorev-2026-08-31-ib69-matris-kosum-atlas.md` · HEAD `c1f5c05` (`git rev-parse --short HEAD`, koşum anı) · **AS-OF 2026-08-31** · zincir m.40b v0.2 (4 dik tez → antitez → V26 örneklem → maskeli hakem → sentez) · **7 Agent çağrısı** (6 işçi Sonnet-5 `[rejim: maliyet-öncelikli]`, 1 hakem Opus-5) · aile-başına ajan tavanı 10, aşılmadı · **aile-1'in MATRİS-KOŞUM ŞEMASI v0 OKUNDU ve üstüne kuruldu** (`raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md`).

**Kapsam beyanı:** bu belge TASARIM ve GİRDİdir. Prototip inşa EDİLMEDİ, hiçbir matris KOŞULMADI, **K-020 kararı VERİLMEDİ**, manifest dosyaları DEĞİŞTİRİLMEDİ (şema önerileri TASLAK). Kanon (`core/`, `CLAUDE.md`, `kuyruk/`, `tools/`, `veri/manifest/`) salt-okundu.

**Ham işçi raporları:**
- `cc/rapor-2026-08-31-ib69-a2-envanter.md` — (a) uygun-iş envanteri
- `cc/rapor-2026-08-31-ib69-a2-k020.md` — (b) K-020 3 model
- `cc/rapor-2026-08-31-ib69-a2-kural.md` — (c) manifest + prompt + fren kuralları
- `cc/rapor-2026-08-31-ib69-a2-pilot.md` — (d) pilot tasarımı + açık uçlar
- `cc/rapor-2026-08-31-ib69-a2-antitez.md` · `cc/rapor-2026-08-31-ib69-a2-v26.md` · `cc/rapor-2026-08-31-ib69-a2-hakem.md`

---

## 0. Sorunun cevabı, tek paragraf

Matris deseninden otomasyona geçiş, **yeni bir motor kurmak değil, mevcut üç mekanizmayı (manifest · append-only kütük · ajan-fren sayacı) eksen sözleşmesiyle birbirine bağlamaktır.** Envanter bunu doğruluyor: 35 açık iş kaleminden yalnız **12'si matris-uygun**, ve bugün hemen koşulabilir olanların hepsi (İB-07 kalanı, İB-58 AXI denetimi, erişim/silver kalibrasyon grid'leri) **LLM'siz ya da tek-çağrılık deterministik** işlerdir — yani otomasyonun ilk kazancı zeki bir harness'ten değil, **zaten var olan script'lerin eksenlerini dışa çıkarmaktan** gelir. Üç kritik hüküm zinciri kesti: (A) **çağrı maliyeti çarpansal değil toplamsaldır** — hücre başına çarpan 1,00, matris-dışı oturum tabanı ölçülmüş 27 çağrı (İB-07, n=1), ön-koşul `N_hücre + sayac_oturum ≤ 143`; ne tez-c'nin ≤72 tavanı ne antitezin ×1,2-1,3 payı ayakta kaldı. (B) **`T_hucre` ölçüm borcu (M-1) pilotla KAPANMAZ** — alt-ajan token deltaları ana oturuma iletilmiyor (`İB-66:126`), tek gerçekçi mekanizma tamamlanmış mesajların `usage` alanının transkriptten hasadıdır (`İB-66:122`) ve `tools/hareket-tablo.py`'de `usage` grep'i **0 eşleşme** veriyor — bu ayrı bir icra kalemidir, K-020'nin hiçbir modeline ait değildir. (C) **İB-06 bugün koşulamaz** — emrin "en güçlü aday" beklentisi çürüdü: beş alt-borcun sayaçları eşik-altı (kapı 2/10 · H-kayıt 3/50 · damıtma 0/5 · emeklilik 1/10) ve beşincisi sıralı zincir (Ö-B ihlali). Kurallaştırma tarafında paket hazır: manifest için iki taslak (S-A `tur`'a `matris` değeri / S-B ayrı `matris` bloğu — **her ikisinde de göç maliyeti 0 dosya**), prompt şablonu İB-66 Şablon-1+2'nin iki-boyutlu örneklemesi olarak çıktı (**5. şablon değil**), fren kuralı sabit sayı değil **denklem** oldu. Pilot tasarlandı ama **bugün bloke**: 2. modelin TAM snapshot id'si yok, bu aile-1 §1 Ö1'in (eksen `degerler` TAM küme) ihlalidir — onay meselesi değil, şema-ihlali.

---

## 1. (a) UYGUN-İŞ ENVANTERİ — 35 kalem sınıflandı, hepsi pointer'lı

**Dağılım (hakem awk sayımıyla düzeltildi):** **12 UYGUN · 23 UYGUN-DEĞİL = 35 hükümlü satır.** (Kaynak: `cc/rapor-2026-08-31-ib69-a2-envanter.md` tablosu; havuz `veri/karar-borcu.jsonl` 27 açık kalem + İB-06'nın 5 alt-borcu + 4 araç-türetimli aday.)

### 1.1 UYGUN — hemen koşulabilir (6)

| iş | pointer | eksen-A × eksen-B | çıktı tipi | N_hücre | not |
|---|---|---|---|---|---|
| **İB-07 kalanı** | `raporlar/2026-08-30-ib07-description-eval.md:5-9`; kütük `veri/description-eval.jsonl` | sorgu q06-q20 (15) × tekrar-3 (1) | etiket (`secilen_skill`) | **15** | hakem kütükten saydı: 45 satır, tekrar dağılımı {1:20, 2:20, 3:5} → 60−45=15. En güçlü aday. |
| **İB-58 (AXI)** | `veri/karar-borcu.jsonl` (İB-58) | script (2) × AXI maddesi A1-A8 (8) | etiket (UYUMLU/UYUMSUZ/N-A) | `[?] 16` | LLM'siz deterministik denetim. **`[?]`**: `tools/AXI-STANDARDI.md` hiçbir koşumda AÇILMADI — 16 sayısı doğrulanmadı. |
| **EK-1 erişim-kalibrasyon** | `tools/erisim-kalibrasyon.py:28,76-92` | genişletme-ağırlığı (7) × yöntem (5) | sayı (recall5/mrr/ndcg10) | `[?] ~35` | araç ZATEN matris koşuyor (İB-43). **`[?]`**: script açılmadı, 7×5 teyit edilmedi; ayrıca erişim ailesi daha önce PK-12 BEKLE'yle donmuştu. |
| **EK-2 d2-eval yeni kol** | `tools/d2-eval.py:100-104` | `--kol` × koşum kimliği | sayı (precision/recall) | değişken | İB-49'un kanıtlı harness'i; `kaydet()` her satıra `ts`+`git_head` yazıyor (V26 doğruladı). |
| **EK-4 silver-sağlık pencere** | `tools/silver-saglik-kalibrasyon.py:22` | `--pencere` grid (4) × zaman-dilimi | sayı | ~4×n | tek parametreyi grid'e açmak; LLM'siz, mevcut kütükten türer. |
| **İB-67** — *şartlı, ayrı kefe* | `cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md:6,7,9,11` | aday (8, emir `:6`) × **dik aile {A akademik, B endüstri, C iç envanter}** (3, emir `:9`) | `sema` {yenilik_durumu ∈ {YOK-bulundu, KISMİ, DÜŞTÜ}, en_yakin_komsu, kanit_url} | **24** | Eksen VAR (tez-a'nın "eksen eksik" hükmü X). **Uyarı:** `:7`'deki üçlü **çıktı etiket uzayıdır, eksen DEĞİL** — antitezin "8×3 kategori" türetimi aile-1 §1'in adıyla uyardığı hatanın tekrarı. Web zorunlu, hücre başına ≥3 arama izi, emrin kendi maliyeti 1,5-2M token `[?]` → İB-58/EK-1/EK-4 ile aynı kefeye KONMAZ. |

### 1.2 UYGUN — eksen tanımı eksik / veri eşiği bekliyor (6)

| iş | pointer | eksik olan | N_hücre |
|---|---|---|---|
| İB-06a skill-kapısı τ/W/β/n_val | `core/skill-uretim-semasi.md:103` | koşum sayacı **2/10** | ~9-16 |
| İB-06b H formülü ağırlıkları | `core/halusinasyon-paketi.md:31` | olay sayacı **3/50**; ağırlık-grid boyutu tanımsız | `[?]` |
| İB-06d anahtar-kaydı k1/k2 | `core/baglam-anahtar-kaydi.md` `[?]` (k1/k2 tanım satırı bulunamadı) | emeklilik sayacı **1/10** | `[?]` |
| İB-09 genişletme | `raporlar/2026-08-30-ib09-yolc-v26-etki.md:9-15` | yeni "ara-zorluk vaka" kümesi TANIMLANMAMIŞ | n×2 |
| İB-68 | `cc/gorev-2026-08-31-ib68-urun-aday-envanteri.md` | 2. eksen (pazar-doğrulama ölçütü) kapalı küme değil `[?]` (emir dosyası açılmadı) | ~16-24 `[?]` |
| EK-3 denetçi-kalibrasyon | `tools/denetci-kalibrasyon.py:56-57` | `--puanla` değer kümesi kodda taranmadı | `[?]` |

### 1.3 UYGUN-DEĞİL — 23 kalem, dört alt-sınıf

- **(ii) KARAR-GEREKTİREN → MASA (6):** KB-17, KB-26, KB-31 (BEKLET-tetikli), İB-39 (atlas koştu, 8 masa kalemi Salih'te), İB-53, İB-13 — *hepsi `veri/karar-borcu.jsonl` ilgili `borc_id` satırı*. Ortak gerekçe: kalan iş **karar**, koşum değil; Katman-1.
- **(i) TEK-ATIŞ (6):** KB-27, KB-34 (`tools/yuzey-parmak-izi.py` tek koşum), İB-03, İB-36 (ctypes tek özellik), **İB-06c** U-skoru (0/5, n grid'e yetmez), **İB-06e** world-model §6 (`core/world-model-tasarimi.md:57-61` — "NDV→tekrar→dil-çarpanı→sort-key→durum-denkliği" SIRALI zincir = aile-1 §6.1 **Ö-B bağımsızlık ihlali**).
- **(iii) SERBEST-METİN → aile-1 §2 Ö1 ihlali (5+):** İB-04 (wiki), İB-56 (Codex atlası), İB-64a/b/c (K-010 aşama araştırmaları), İB-65, İB-66. Çıktı kompoze düzyazı → T1-T5 deterministik toplamaya girmez.
- **(iv) İNSAN-GİRİŞİ (4):** İB-01 (Salih'in tarayıcı girişi), İB-11 (md.43 (d)(e) + Adım-0 managed-settings), İB-13, İB-59 (pilot iş seçimi Salih'in + çıktısı kalite gözlemi).

### 1.4 Envanterin iki sert bulgusu

1. **İB-06 emrin beklentisini ÇÜRÜTTÜ.** `veri/karar-borcu.jsonl` İB-06 `icra_borcu` alanı birebir: *"kapı 2/10 koşum · H-kayıt 3/50 · damıtma 0/5 · emeklilik 1/10"*. Dördü de eşik-altı, beşincisi sıralı zincir. **İB-06'nın bugün koşulabilir hiçbir alt-kalemi yoktur.** Tez ve antitez bu noktada birleşti, hakem D verdi. Eşikler gerçek-kullanım olay defterine bağlı; sentetik/tarihsel veriyle doldurulamıyor.
2. **Matris-uygunluk LLM'le değil, TİPLİLİKLE korele.** Hemen koşulabilir 6 işin 5'i **LLM'siz**. Otomasyon kazancının ilk dalgası model çağırmıyor — aile-1 §3'ün "toplama LLM'siz ve deterministik" kuralının envanterdeki fiili karşılığı budur.

---

## 2. (b) K-020 BİRLEŞME ÖNERİSİ — 3 model (KARAR VERİLMEDİ)

**Açılan birincil kaynaklar (bu ailede 8 gerçek WebFetch: tez-b 5 + V26 3):** promptfoo.dev/docs/providers/python/ **AÇILDI** · promptfoo.dev/docs/integrations/ci-cd/ **AÇILDI** · optuna.readthedocs.io/…/optuna.study.Study.html **AÇILDI** · optuna.readthedocs.io/…/optuna.study.create_study.html **AÇILDI** (`load_if_exists` resume — V26 doğruladı) · docs.wandb.ai/guides/sweeps/ **AÇILDI**. **`[?]` açılamadı:** W&B self-hosted controller mimarisi · lm-eval per-sample jsonl alan şeması.

### 2.1 Modeller

| | **M1 — hazır araç sarmalama** (promptfoo) | **M2 — kendi harness genellemesi** (`d2-eval.py` deseni) | **M3 — KARŞIT-TEMELLİ: hiç altyapı kurma** |
|---|---|---|---|
| **Temel** | deklaratif eval-config; matris aracın YAML'ında yaşar | kod-olarak-matris; stdlib-only script, eksenler json sözleşmeden | **hiçbir yürütücü yok**: sözleşme json + mevcut manifest/kütük + işçi-ajan disiplini |
| **token (kurulum)** | orta-yüksek | orta | ~sıfır |
| **token (hücre ek yükü)** | düşük `[?]` (T_hucre ölçülmedi → göreceli) | ~sıfır | ~sıfır (disipline bağlı) |
| **zaman (kurulum)** | ~1 gün **+ doğrulanmamış CC Agent köprüsü** | ~yarım gün | dakikalar |
| **kalite (§5'in 13 alanı)** | ~3-5 otomatik / 8-10 elle | **9/13 otomatik** (hakem düzeltmesi: tez-b'nin "13/13"ü X — `token_giris/token_cikis/token_onbellek_okuma/sure_ms`'in KAYNAĞI yok) | 0/13 otomatik, 13/13 disipline bağlı |
| **risk — md.49** | düşük (lokal), `[?]` teyitsiz | yok | yok |
| **risk — bağımlılık** | npm/Node zinciri, terk-riski | stdlib-only | yok |
| **risk — CC Agent uyumu** | **doğrulanmamış, KRİTİK** | uyumlu (çağrıyı sarmıyor) | uyumlu (aynı sebep) |

**M1'in çekirdek bulgusu [DESTEKLİ, promptfoo.dev/docs/providers/python/, AS-OF 2026-08-31, 2 kez açıldı]:** Python provider'ın `call_api` imzası HTTP'ye bağımlı değil — yerel/özel mantık sarılabilir. **DÜZELTME (V26 ihlali):** tez-b'nin dokümana atfettiği *"subprocess çağrıları"* ibaresi sayfada **hiç geçmiyor** — bu ibare raporun ÇIKARIMIDIR, DESTEKLİ damgası hak etmiyor. Claude Code Agent çağrısının bu köprüye fiilen oturduğu **hiçbir yerde doğrulanmadı** — M1'in bugün elenmesinin gerekçesi budur.

### 2.2 Öneri ve karar şartı

**ÖNERİLEN: M2** (kendi harness'in eksen-genel hâli), gerekçe: kanıtlı desen (`tools/d2-eval.py` 172 satır, `kaydet()` her satıra `ts`+`git_head` yazıyor — V26 doğruladı), stdlib-only, CC Agent çağrısını sarmıyor, envanterin hemen-koşulabilir 6 işinin 5'i zaten LLM'siz olduğu için M2'nin kör noktası (token alanları) o işlerde ISIRMIYOR.

**Tez-b'nin "önce M3 çünkü M-1'i ölçer" sıralaması ÇÜRÜDÜ (hakem X).** M-1 ne M2 ne M3 ile kapanır; kapanma mekanizması **her iki modelde de aynı üçüncü bileşendir** (§7 madde 1). Sıra kararı M-1'den bağımsızlaştı.

**K-020 KARARI VERİLMEDİ (emir yasağı; hüküm masada).** Verilebilmesi için gereken iki ölçüm:
1. **usage-kaynağı sondası** (1 Agent çağrısı, ucuz): dönüş paketinde `usage` var mı; transkript sidechain satırında `usage` + parent atfı dolu mu.
2. **M1 köprü denemesi**: promptfoo Python provider'ından tek bir CC Agent çağrısı gerçekten dönüyor mu.
Bu ikisi gelmeden M1↔M2 "hücre başına ek yük" ekseni **sayısal değil görecelidir**.

---

## 3. (c) KURAL + ŞEMA PAKETİ (m.38 formu)

### 3.1 P1 — Manifest matris-koşum birim tipi (TASLAK, hüküm masada)

**S-A — `tur` değer kümesine `matris` eklemek** (İB-65 §5.1 yüklem-ağacına 4. soru):
```
TUR ::= {pipeline, loop, hibrit, belirsiz, matris}
Y4 (yeni): eksen_carpimi_tanimli?
  Y4 = E  ∧  Y1(SÜREKLİ?) = H  ∧  Y3(iç-sıra-sabit) = E   →   tur = matris
```
`matris` `hibrit`in alt-sınıfı DEĞİL, **kardeş** sınıftır: hibritin (N,M) tavanı SAYIdır, matrisin "tavanı" bir EKSEN listesidir ve kardinalite değerlerden türer (aile-1 §1 Ö1/Ö2).
*Artı:* tek alanda kalır, İB-65'in `hibrit` eklemesiyle aynı m.40c risk sınıfı. *Eksi:* yüklem ağacı 3→4, `belirsiz` dalına yeni çakışma yüzeyi (SÜREKLİ ∧ iç-sıra-sabit ∧ eksen-çarpımı → hibrit mi matris mi).

**S-B — `tur`'a dokunmadan ayrı blok:**
```
tur ∈ {pipeline, hibrit} (değişmez)  ∧  matris = {eksenler, tekrar, erken_durdurma, hucre_tipi} | null
  matris ≠ null → ( |matris.eksenler| ≥ 2 ∧ (∃e: e.rol=dis) ∧ (∃e: e.rol=ic) )       [aile-1 §1 Ö1]
  matris ≠ null ∧ matris.erken_durdurma = kademe_esigi → matris.esik ZORUNLU ∧ SABİT
```
*Artı:* İB-65 şemasına sıfır dokunuş; matris zaten kendi iç yapısı olan bir obje, tek-atomlu sınıflandırıcıya sıkıştırılması zorunlu değil. *Eksi:* iki kaynaktan okunur — `tur=pipeline` + `matris≠null` bir aracı yanıltabilir; envanter taramasında gözden kaçma riski S-A'dan yüksek.

**GÖÇ MALİYETİ — hakem kesin sayımı:** `veri/manifest/` = **17 dosya**, `tur` dağılımı **{pipeline: 16, loop: 1}**, matris bloğu taşıyan **0**. → **her iki seçenekte de bugün değişmesi gereken manifest: 0.** Yeni birimler değerle DOĞAR.
**Şerh:** bu sıfır YALNIZ `matris` içindir. İB-65 kaynaklı **hibrit göçü 2 dosya** (`loop-kapanis-bu-oturum.json` loop→hibrit, `sahada-damitma-s22.json` pipeline→hibrit) AYRI ve kayıtlı borçtur — "toplam manifest göçü sıfır" DENMEZ. (Antitezin "14 pipeline + 1 loop + 2 sayılamayan" ara-sayımı yanlış, kullanılmadı.)

### 3.2 P2 — Prompt şablonu (dış-loop → iç-matris)

İB-66 Şablon-1'in bütçe yüklemi **aynen devralındı**, üstüne aile-1 §4 KAPI-2 eklendi (İB-66'da yoktu — bu tek AYRILMA noktasıdır, çelişki değil genişletme):
```
GİRDİ SÖZLEŞMESİ: veri/sozlesme/<is>-eksen.json                      [aile-1 §1]

∀ i_dis ∈ dis.degerler:  kurulum_dis(i_dis)                          [M_dis, bir kez]
  ∀ i_ic ∈ ic.degerler, ∀ t ∈ 1..tekrar:
     hucre_anahtari := serile(i_dis, i_ic, t)                        [aile-1 §2, TEKİL]
     RESUME:  hucre_anahtari ∈ kütük  →  ATLA (idempotency, §2 Ö3)
              hucre_anahtari ∉ kütük  →  ÇAĞIR
     ÇAĞRI:   cikti := cagir(sablon_id, eksen_degerleri) ; cikti.tip ∈ {etiket,sayi,sema}
     APPEND:  bronz jsonl satırı, aile-1 §5'in 13 alanı, append-only

Ö1 (İB-66 Şablon-1, AYNEN):  (b_iç ≥ T_hücre) ∧ (N_dış×N_iç×tekrar×b_iç ≤ 0,8×B_oturum)
Ö2 (KAPI-2, YENİ):           N_hucre + sayac_oturum_anlik ≤ 143
  ¬Ö2 → matrisi oturuma BÖL (RESUME yüklemi bunu zaten karşılar, ek mekanizma gerekmez)

done ↔ ( ∀(i_dis,i_ic,t): hucre_anahtari ∈ kütük )  ∨  ( B_harcanan ≥ 0,8×B_oturum )
```
**"Matris yeni bir seviye midir?" — İB-66 §5.1'in üç şartıyla test:** (i) kendi sayacı ✅ (i_dis,i_ic,t) · (ii) kendi durma yüklemi ✅ · (iii) alt seviyenin TAM koşumu → **KOŞULLU**.
```
tam_faktoriyel ∧ ¬erken_durdurma  →  matris = 2 SEVİYE, ve Şablon-1(dış)+Şablon-2(iç)'in
                                      iki-boyutlu ÖRNEKLEMESİDİR — 5. şablon DEĞİL      [D]
erken_durdurma = kademe_esigi     →  (iii) kırılır (büzülen aday kümesi) → İB-66 §5.2'nin
                                      hiçbir sınıfına girmiyor → YENİ ALT-TÜR → MASAYA
```
Bu, aile-1 §6.3'ün bağımsız olarak vardığı sonucun aynısıdır — iki aile çakışıyor, çelişmiyor.

### 3.3 P3 — Fren kuralları (hakem düzeltmeleriyle)

**F-1 · Çağrı aritmetiği TOPLAMSALDIR, çarpansal değil.**
```
Ölçüm (İB-07, n=1, deneysel — raporlar/2026-08-30-ib07-description-eval.md:9,11,48):
  planlanan hücre 60 · fiilen yapılan hücre-çağrısı 51 (45 kayıt + 6 hook reddi) · sayaç 78
  matris-DIŞI oturum tüketimi = 78 − 51 = 27 çağrı
  lider'in non-Agent araçları (~14 Read/Bash/Write) SAYACA GİRMEZ (matcher yalnız Agent/Task)
HÜKÜM: hücre başına çarpan = 1,00 ;  fazlalık sabit ve toplamsal (27) ;
       antitezin ×1,2-1,3 modeli X (N büyüdükçe fazlalığı yanlış büyütür)
```

**F-2 · Hücre tavanı SABİT SAYI DEĞİL, DENKLEMDİR.**
```
Ö: N_hucre + sayac_oturum_anlik ≤ 143
   [.claude/hooks/pretool-ajan-fren.sh:11 eşikler (UYARI=72 / DURDUR=144),
    :27 matcher ("Agent","Task"), :30-32 state, :37 sayac += 1, :46 `n >= durdur` → BLOKE
    ⇒ 144. çağrı reddedilir, son izinli çağrı 143]
Planlama-zamanı tek sayı isteniyorsa:  N_hucre ≤ 143 − 27 = 116
   — ve bu, oturumdaki TÜM matris hücrelerinin TOPLAMIDIR, kalem başına değil.
REDDEDİLENLER: ≤72 (=144/2, ölçümden değil yuvarlamadan; gerekçesi de yanlıştı — 72'yi dolduran
   60-65 hücre değil, 51 hücre + 27 tabandı)  ·  Σ ≤ 115 (=0,8×144; 0,8 payı KAPI-1'in TOKEN
   konvansiyonudur, çağrı sayacına gerekçesiz taşınamaz)
KURAL: sayaç okunabiliyorsa taban TAHMİN EDİLMEZ, koşum anında OKUNUR.
```

**F-3 · Bütçe kalıtımı: TEK SAYAÇ.** İB-65'in `hibrit` tanımı zaten `butce_sayaci = "tek"` şart koşuyor; matris bunun eksen-versiyonudur. `N_dış × N_iç × tekrar` tek bir `N_cagri`'ye toplanır; dış ve iç eksenler AYRI fren sayacı TUTMAZ (hook zaten oturum-genelinde tek `sayac` tutuyor, alt-ajan çağrıları dahil — `pretool-ajan-fren.sh:30-32,37`). İB-66 Şablon-3'ün fren-kalıtımı aynen geçerli.
`[?]` **Açık kalıyor:** `hucre_tipi = gnhf_iterasyonu` hücreler ayrı CLI süreci olduğu için PreToolUse hook'undan GEÇMEYEBİLİR — fiziksel olarak muhtemel, **test kanıtı yok**, sayı türetilmedi.

**F-4 · A1-sicil ilişkisi: KAPSAM-DIŞI (çelişki değil).** A1 = *"5 ardışık başarılı otomasyon-koşumu ∧ açık incident 0; birim = pipeline-koşumu"* (`core/pano.md:34` + `kuyruk/k010-zincir-2026-08-29.md:55`, Karar 81 EK-2, Salih imzası 08-30 — V26 iki pointer'ı da birebir doğruladı). Matris `tur = matris` (S-A) ∨ `tur=hibrit ∧ matris≠null` (S-B) birimidir, `tur=pipeline` değildir → **A1 sayacına +1 KATKI VERMEZ**. A1 zaten 5/5 KESİN ve dondu; geriye dönük etki yok. *İleri dönük soru masada:* matris-koşumları A1-benzeri ayrı bir sicil mi tutmalı (Katman-1).

**F-5 · Pointer düzeltmesi (V26 bulgusu).** Tez-c'nin hook pointer'ları `9-10 / 27 / 22-24` YANLIŞ; gerçek konumlar **`11 / 37 / 30-32`**. İçerik hükmü değişmiyor, ama m.20 gereği düzeltildi — yukarıdaki F-2 bloğunda doğru satırlar kullanıldı.

---

## 4. (d) PİLOT TASARIMI — KOŞULMADI, ve bugün BLOKE

### 4.1 Düzeltilmiş boyut: 30 değil **20 hücre**

Tez-d 5 sorgu × 2 model × tekrar-3 = 30 hücre önerdi. **Hakem kütükten saydı:** `veri/description-eval.jsonl`'de q06-q10 için `tekrar=1` ve `tekrar=2` satırları **haiku kolonunda ZATEN VAR** (10 satır). 30 hücrenin 10'u mükerrer koşumdur (%33 israf; aile-1 §2 Ö3'ün "çakışma olayı" sınıfı).
```
DÜZELTİLMİŞ TASARIM
  haiku kolonu : q06-q10 × tekrar-3 (yalnız eksik olan)         =  5 hücre
  yeni model   : q06-q10 × tekrar 1,2,3                          = 15 hücre
  TOPLAM N_hucre = 20   ;   hucre_tipi = tek_cagri  →  N_cagri = 20
  T4 (tekrar varyansı) yeni model üzerinden ölçülür; haiku'nunki kütükte zaten var.
```

### 4.2 Eksen sözleşmesi ve dış/iç kararı

```
EKSEN#1  ad=model      tip=kategorik  rol=DIŞ  degerler=["claude-haiku-4-5-20251001", "[?]"]
EKSEN#2  ad=sorgu_id   tip=kategorik  rol=İÇ   degerler=[q06..q10]   kaynak=veri/sozlesme/description-eval-sorgular.json
tekrar=3 · erken_durdurma=yok · hucre_tipi=tek_cagri
```
**Dış/iç gerekçesi (aile-1 §6, Ö-A > Ö-B > Ö-C):** Ö-A nötr (tek append-only kütük, birim-içi), Ö-B nötr (hücreler bağımsız), **Ö-C karar veriyor** — sabit 14-skill listesi metni model sabitken önbellek-önekinde kalır, model değişince önek geçersizleşir → **model DIŞ, sorgu İÇ**. (`ib07:53`: aynı skill-listesi metni 51 kez birebir kopyalanmış.) Hakem D verdi.

### 4.3 BLOKE — aile-1 §1 Ö1 ihlali

**Pilot bugün koşulamaz.** EKSEN#1'in `degerler` kümesinde `"[?]"` var; aile-1 §1 Ö1 `degerler`i **TAM küme** olarak tanımlıyor ve Ö2 kardinalitenin DOSYADAN türetilmesini şart koşuyor. `"[?]"` bir değer değil, boşluktur. Bu **bir onay meselesi değil, şema-ihlalidir**: ikinci modelin TAM API snapshot id'si (kısa ad YASAK) sözleşme dosyasına yazılmadan matris tanımlı değildir.

### 4.4 Kütük: YENİ DOSYA zorunlu

Mevcut `veri/description-eval.jsonl` **8 alanlı**: `altin_etiket, isabet, isci_model, kosum_id, secilen_skill, sorgu_id, tekrar, ts`. Aile-1 §5'in 13 alanının 8'i eksik ∨ farklı adlı (`model` → `isci_model`; `hucre_anahtari`, `git_head`, `hucre_tipi`, `eksen_degerleri`, `toplama_yontemi`, `token_*`, `sure_ms`, `kosum_durumu` YOK). Aynı dosyaya append = **karışık şemalı kütük** = §3 deterministik toplamanın girdi şartının ihlali. Tez-d'nin *"uzantı ya da yeni dosya"* seçeneği **KAPATILDI: yeni dosya.**

### 4.5 Maliyet (kaba, m.29) ve KAPI denetimi

```
KAPI-2 (çağrı):  N_hucre = 20  →  ön-koşul  sayac_oturum_anlik ≤ 143 − 20 = 123
                 (koşum anında hook state'inden OKUNUR, tahmin edilmez)
KAPI-1 (token):  toplam ≈ 2 × M_dis  +  20 × T_hucre
                 T_hucre  =  ÖLÇÜLMEDİ  (borç M-1)  →  SAYISAL TOKEN RAKAMI VERİLMEZ.
                 Parametrik kalır; tahminle doldurulmadı (m.29).
```

### 4.6 Pilotun ölçüm çıktısı — DÜZELTME

Tez-d "bu pilot M-1'i kapatır" dedi; **hakem X verdi.** Pilot 20 satır yazar ama `token_giris/token_cikis/token_onbellek_okuma/sure_ms` alanlarının **kaynağı yoktur** (§7 madde 1). Pilot M-1'i kapatmaz; kapatan şey ayrı bir hasat işidir.

---

## 5. KARAR-MASASI KALEMİ TASLAĞI (m.31 — bu rapor HÜKÜM VERMEZ)

> **Kalem adı:** Matris-koşum birim tipi kurallaşsın mı, ve İB-07 pilot matrisi hangi kural paketiyle koşulsun?
>
> **Bağlam:** 35 açık iş kaleminden 12'si matris-uygun, 6'sı bugün koşulabilir (5'i LLM'siz). Mevcut 17 manifestin 0'ı matris; göç maliyeti sıfır. Aile-1 şeması v0 hazır, aile-2 kural paketi (P1/P2/P3) hazır. Pilot tasarlandı ama 2. modelin TAM snapshot id'si olmadığı için §1 Ö1'i sağlamıyor.
>
> **Karar-A (manifest):** S-A (`tur`'a `matris` değeri, Y4 yüklemi) ∨ S-B (ayrı `matris` bloğu). İkisinde de bugünkü göç 0 dosya. *Öneri:* **S-A** — `tur`-okuyan araçlar İB-65'in `hibrit` eklemesiyle aynı risk sınıfında; S-B'nin "iki kaynaktan oku" riski envanter taramasında gözden kaçma üretir. *Karşıt:* S-B, İB-65'in yüklem ağacına hiç dokunmaz (o kalem hâlâ masada — önce o karara bağlanabilir).
> **Karar-B (fren):** hücre tavanı sabit sayı yerine **denklem** (`N_hucre + sayac_oturum ≤ 143`, planlama tavanı 116) onaylanır mı.
> **Karar-C (pilot):** 20-hücrelik İB-07 sorgu×model matrisi koşulsun mu; ön şart 2. modelin TAM snapshot id'sinin Salih'çe verilmesi (şema-ihlali kapanır).
> **Karar-D (K-020):** hüküm VERİLMEZ; önce iki ölçüm — usage-kaynağı sondası (1 çağrı) + M1 köprü denemesi.
>
> **Artı:** desen zaten 3 kez fiilen koştu (İB-07, İB-49, atlas aile×şerit); kurallaştırma yeni motor değil, mevcut üç mekanizmanın bağlanması; göç maliyeti sıfır.
> **Eksi:** yüklem ağacı büyür (S-A) ∨ iki-kaynak riski doğar (S-B); `kademe_esigi` alt-türü ayrı Katman-1 kararı; M-1 ölçüm borcu ayrı icra kalemi olarak açılır.
> **Bağlı borçlar:** M-1 `T_hucre` · `kademe_esigi` alt-türü · İB-65 hibrit göçü 2 dosya · `gnhf_iterasyonu` hücrelerinin hook'tan geçip geçmediği `[?]` · matris-koşumları için ayrı sicil sorusu (F-4).
> **m.16 kapısı:** kalem masaya çelişki-kapısından geçerek girer; aile-1 şemasıyla bilinen çelişki YOK (§6).

---

## 6. AİLE-1 ŞEMASINA UYUM DENETİMİ

| Şema maddesi | Uyum | Not |
|---|---|---|
| §1 Ö1/Ö2 (eksen `degerler` TAM küme, kardinalite dosyadan) | **UYULDU — ve pilot bu maddeden BLOKE edildi** | tez-d'nin `"[?]"` değeri Ö1'i ihlal ediyordu; sentez şemayı üstün tuttu (§4.3). Antitezin İB-67 türetimi de §1'in "eksen ≠ etiket uzayı" uyarısını ihlal ediyordu; düzeltildi (§1.1). |
| §2 Ö1 tiplilik (¬serbest_metin) | **UYULDU** | envanterin (iii) alt-sınıfı doğrudan bu maddeden türedi (5+ iş elendi). |
| §2 Ö3 idempotency | **UYULDU — pilot düzeltildi** | 10 mükerrer hücre çıkarıldı, 30→20 (§4.1). |
| §3 Karar 65 (LLM'siz toplama) | **UYULDU** | hemen-koşulabilir 6 işin 5'i LLM'siz; toplama ayrı adım olarak korundu. |
| §4 iki taban + iki kapı | **UYULDU, kapı-2 SAYISALLAŞTIRILDI** | KAPI-2'nin `DURDUR` sabiti 144 olarak teyit edildi (commit `5218209`), off-by-one düzeltildi (≤143). |
| §5 kütük 13 alan | **UYULDU** | "mevcut dosya uzantısı" seçeneği kapatıldı (§4.4). |
| §6 Ö-A > Ö-B > Ö-C | **UYULDU** | pilotun model-DIŞ kararı Ö-C'den; İB-06e Ö-B ihlaliyle elendi. |
| §6.3 (`kademe_esigi` yeni alt-tür) | **UYULDU — bağımsız doğrulandı** | P2'nin İB-66 §5.1 testi aynı sonuca vardı. |

### 6.1 AYRILDIĞIMIZ / ŞEMAYA ŞERH DÜŞTÜĞÜMÜZ 4 NOKTA

1. **§4 TANIM bloğu — `T_gnhf = 300k [ÖLÇÜLDÜ]` damgası DÜŞER.** Kaynak satır açıldı (`raporlar/2026-08-31-k010-a3-loop-1.md:12`, birebir: *"token tavanı doldu (535k/500k, 2 iterasyon) … gnhf token birimi = önbellek-okuma DAHİL; iterasyon tabanı ~300k"*). Ölçülen şey **2 iterasyonun TOPLAMIDIR (535k)**; 535k ÷ 2 = **267,5k**, "~300k" bundan **%12,1 yukarı yuvarlanmış** bir ortalamadır. Önerilen şerh:
   `T_gnhf ≈ 300k [TÜRETİLDİ, ÖLÇÜLMEDİ — 535k ÷ 2 iterasyon = 267,5k, +%12,1 yuvarlama; n=2; soğuk/sıcak önbellek asimetrisi ayrıştırılmadı; önbellek-okuma DAHİL; kaynak k010-a3-loop-1:12, vaka e2e715, AS-OF 2026-08-31. Bir eşiğe/kapıya sokulmadan önce n≥3 temiz iterasyon ölçümü gerekir.]`
2. **§4'e F-1 eklenmeli:** çağrı maliyeti toplamsaldır (çarpan 1,00 + sabit oturum tabanı 27, n=1), ve KAPI-2'nin doğru sınırı **143**'tür (hook `n >= 144`'te bloke eder).
3. **§6.1 Ö-A'ya kapsam şerhi:** *"matris-İÇİ hücrelerin ortak append-only kütüğe yazması bu kuralın kapsamı DIŞINDADIR (paralel-kapı birim-ARASI çalışır, hücre-arası değil); POSIX kısa-satır append atomikliği VARSAYILDI, doğrulanmadı `[?]`."*
4. **§2'ye açıklık:** `cikti.tip = sema` durumunda deterministik toplama YALNIZ enum/sayı alanları üzerinde tanımlıdır; serbest-metin alanları (İB-67'nin `en_yakin_komsu`, `kanit_url`'ü gibi) kütükte taşınır ama T1-T5'e GİRMEZ.

**İB-66 §5'ten tek AYRILMA:** Şablon-1'e KAPI-2 çağrı-sayacı eklendi (İB-66'da yoktu). Bu genişletmedir, çelişki değil — aile-1 §6.2'nin "İB-07'yi kesen kısıt token değil çağrı sayacıydı" tespitiyle örtüşüyor.
**İB-65 §5'ten AYRILMA YOK:** S-A/S-B ikisi de %29 kapsama açığının devamı olarak konumlandı; M1 yüklem-ağacı korundu (S-A ona 4. soruyu ekler, S-B ona hiç dokunmaz).

---

## 7. AİLE-1'DEN DEVREDİLEN 6 AÇIK UÇ — HER BİRİNE CEVAP

1. **M-1 `T_hucre` ölçüm borcu — AÇIK KALIYOR, ama mekanizması artık BİLİNİYOR.** Pilotla KAPANMAZ. Kanıt: `raporlar/2026-08-31-ib66-…-atlas.md:126` — *"alt-ajanların token-seviyesi delta'ları ana oturuma forward edilmez; parent atfını yalnız TAMAMLANMIŞ mesajlar taşır"*; `:122` — *"`usage` alanı önbellek-okuma/yazma ayrımını ve `result.usage.modelUsage` dökümünü taşıyor ama izleyici hiç göstermiyor"*. Yani veri **transkriptte diskte VAR**, hiçbir araç okumuyor: `grep "usage\|token" tools/hareket-tablo.py` → **0 eşleşme**. **Tek gerçekçi mekanizma: transkript `usage` hasadı** (mesaj-başına `usage` + parent/sidechain atfı → `hucre_anahtari` eşlemesi; gnhf tarafında karşılığı `.gnhf/runs/*/iteration-N.jsonl`). Bu **ayrı bir icra kalemidir**, K-020'nin hiçbir modeline ait değildir. Ön adım: **1 çağrılık usage-kaynağı sondası**.
2. **`kademe_esigi` alt-türü — AÇIK KALIYOR (Katman-1).** İki bağımsız türetim aynı sonuca vardı: tam faktöriyel matris İB-66 §5.1'in üç şartını sağlar (2 seviye), kademeli matris (iii)'ü kırar ve İB-66 §5.2'nin hiçbir sınıfına girmez → yeni alt-tür, hüküm Salih'te. Bu rapor hüküm vermedi.
3. **K-020 birleşme kararı — VERİLMEDİ (emir yasağı).** 3 model üretildi (M1 promptfoo / M2 kendi harness ÖNERİLEN / M3 karşıt-temelli altyapısız), 4 eksende sayısal. Karar öncesi gereken iki ölçüm §2.2'de. Tez-b'nin "M-1 sıralamayı belirler" gerekçesi çürütüldü.
4. **Manifest matris birim tipi — TASLAK HAZIR, hüküm masada.** S-A ve S-B eksiksiz, m.38 formunda; **göç maliyeti her ikisinde de 0 dosya** (17 manifest sayıldı: 16 pipeline + 1 loop). Sentezin önerisi S-A (§5 Karar-A), ama İB-65'in kendi `tur` kalemi de masada olduğu için ona bağlanabilir.
5. **`[?]` 300k ham ölçüm teyidi — KAPANDI.** `raporlar/2026-08-31-k010-a3-loop-1.md:12` açıldı, rakam orada ve birim ("gnhf token birimi", "önbellek-okuma DAHİL") birebir yazılı. **Ama "ÖLÇÜLDÜ" damgası düşer** — 535k/2 = 267,5k, "~300k" %12,1 yuvarlama, n=2 (§6.1 madde 1).
6. **Uygun-iş envanteri — KAPANDI.** 35 kalem sınıflandı, hepsi pointer'lı: 12 UYGUN (6 hemen koşulabilir, 6 eksen/veri bekliyor) · 23 UYGUN-DEĞİL (4 alt-sınıf). Emrin "İB-06 en güçlü aday" beklentisi ÇÜRÜTÜLDÜ.

---

## 8. ZİNCİR SONUCU

**Hakem D/K/X:** 35 iddia — **D=15 · K=4 · X=16.** Maske çalıştı: iki noktada hem tez hem antitez ayrı ayrı X aldı (hücre-tavanı payı; İB-67 ekseni). Antitezin "DAYANDI" dediği bir iddia (İB-67 taşınması) sonucu doğru ama türetimi çürük olduğu için X aldı.

**V26 ihlali: 1** (5 iddia denetlendi, 3 tam DOĞRULANDI, 2 KISMEN, 0 sahte-pointer ihlali) — `cc/rapor-2026-08-31-ib69-a2-k020.md:22`'de promptfoo dokümanına atfedilen *"subprocess çağrıları"* ibaresi sayfada **yok**; DESTEKLİ damgası hak edilmemiş (çekirdek iddia — HTTP-bağımsızlık — DESTEKLİ kalır). İkinci KISMEN: tez-c'nin hook pointer'ları kaymış (F-5'te düzeltildi). **8 gerçek WebFetch** açıldı (tez-b 5 + V26 3); açılmayan hiçbir URL'ye DESTEKLİ damgası verilmedi.

**Şemadan/tezlerden ÇIKARILANLAR:** ×1,2-1,3 çağrı çarpanı (X) · ≤72 sabit hücre tavanı (X) · Σ ≤ 115 ikinci kapı (X) · sayac_oturum ≤ 114 (X → 113) · "pilot M-1'i kapatır" (X) · M2'nin 13/13 kalite skoru (X → 9/13) · "M3 önce çünkü M-1'i ölçer" gerekçesi (X) · "description-eval.jsonl uzantısı" seçeneği (X) · 30-hücrelik pilot (X → 20) · `T_gnhf` "ÖLÇÜLDÜ" damgası (X).

**`[?]` KALAN — sentez sayı türetmedi:** İB-58'in 16 hücresi (`tools/AXI-STANDARDI.md` hiç açılmadı) · EK-1'in 7×5=35'i (script açılmadı) · EK-3'ün `--puanla` kümesi · İB-68'in 2. ekseni · `gnhf_iterasyonu` hücrelerinin ajan-fren hook'undan geçip geçmediği · `tools/paralel-kapi.py` satır iddiaları · W&B self-hosted controller · lm-eval per-sample şeması · İB-06b/d'nin grid boyutları.

---

## 9. DURMA KOŞULU DENETİMİ

| madde | durum |
|---|---|
| uygun-iş envanteri ≥10 iş, sınıflandırılmış ve pointer'lı | ✅ **35 kalem** (12 UYGUN / 23 UYGUN-DEĞİL), §1 |
| K-020 birleşme önerisi 3 model, ≥1 karşıt-temelli, sayısal | ✅ M1/M2/M3, M3 karşıt-temelli, 4 eksende tablo (§2.1) |
| kural + şema paketi m.38 formunda | ✅ P1 (S-A/S-B yüklemli) · P2 (şablon) · P3 (F-1…F-5), §3 |
| pilot tasarımı (maliyet kaba, KOŞULMAZ) | ✅ §4 — 20 hücre, KOŞULMADI, token parametrik (T_hucre ölçülmedi) |
| karar-masası kalemi taslağı | ✅ §5 (Karar-A/B/C/D) |
| künye (emir yolu, HEAD sha, AS-OF, ajan sayısı, işçi modeli) | ✅ başlık |
| aile-1 şemasına uyum denetimi (uyum + ayrılma) | ✅ §6 + §6.1 (4 şerh) |
| 6 devredilen açık uca cevap | ✅ §7 (2 KAPANDI, 4 açık — her birine gerekçe) |

**SAĞLANMAYAN:** yok. **YASAK İHLALİ:** yok — prototip inşa/koşum yapılmadı, K-020 kararı verilmedi, kanon ve manifest dosyaları değiştirilmedi, `git add/commit/push` yapılmadı, açılmamış kaynağa DESTEKLİ damgası verilmedi.
