# İB-75 + İB-64c — Bağlam-devri ekip-lideri v0: tasarım paketi (SEÇENEK; hüküm masa-10)

*Üreten: Opus 5 lider-ajan (effort medium, Karar 89), yan-oturum — tüzük m.41: KANON KARARI ALINMADI, `core/` · `CLAUDE.md` · `.claude/` · tüzük dosyalarına yazım = 0. Emir: `cc/gorev-2026-09-09-ib75-baglam-devri-ekip-lideri.md`. Manifest: `veri/manifest/u8-ib75-baglam-devri-ekip-lideri.json`. Tarih: 2026-09-09. H = 11 ≥ eşik 7 → `halusinasyon-engelleyici` zinciriyle üretildi (derece.py 09-09, exit 10). Rejim: kalite-öncelikli.*

**Bu belge bir HÜKÜM DEĞİL, bir SEÇENEK PAKETİDİR.** (a)-(d) tasarım adayı, (e) üç karar modeli, (f) tohum-desen kullanım kaydı. Karar Salih'indir (masa-10).

---

## 0. Koşum künyesi (ne fiilen koştu)

| Aşama | Ne | Model | Ajan | Araç çağrısı | Çıktı |
|---|---|---|---|---|---|
| 1 | Tez A (statik lider desenleri) | Sonnet | 1 | 8 | `cc/rapor-2026-09-09-ib75-tez-a.md` |
| 1 | Tez B (bağlam-devri mekanizmaları) | Sonnet | 1 | 11 | `cc/rapor-2026-09-09-ib75-tez-b.md` |
| 1 | Tez C (yetki-sınırlı lider) | Sonnet | 1 | 12 | `cc/rapor-2026-09-09-ib75-tez-c.md` |
| 1b | Antitez A (¬ aile A) | Sonnet | 1 | 12 | `cc/rapor-2026-09-09-ib75-antitez-a.md` |
| 1b | Antitez B (¬ aile B ∧ ¬ aile C) | Sonnet | 1 | 14 | `cc/rapor-2026-09-09-ib75-antitez-b.md` |
| 1b | İç-envanter (yerel, internetsiz) | Sonnet | 1 | 11 | `cc/rapor-2026-09-09-ib75-envanter.md` |
| 1c | **Maskeli hakem** (AYRI çağrı, sentezi görmedi) | Opus 5 medium | 1 | 13 | `cc/rapor-2026-09-09-ib75-hakem.md` |
| 2 | Sentez (bu belge) | Opus 5 medium (lider) | — | — | bu dosya |
| 3 | 3 karar modeli | Opus 5 medium (lider) | — | — | §(e) |

**D1 dalı:** `raporlar/` altında İB-64c raporu YOK (09-09 kontrolü) → aksi dal, çift-atlas KOŞULDU. İB-64c saha sorusu bu koşumun aile A/B/C'sine gömüldü; İB-64c ayrıca koşulmasına gerek kalmadı (durum önerisi §7).
**Kotalar:** her tez/antitez işçisi ≥2 birincil kaynağı fiilen WebFetch ile açtı (toplam açılan birincil kaynak: 13 ayrı URL). V26 kural-tabanlı örneklem hakeme verildi (tüm sayısal iddialar + son-üçlük kaynak iddiası + 3 URL'siz/model-hafızası iddiası). Yapan ≠ ölçen: hakem çağrısına emir, beklenti ve iddiaların kimden geldiği VERİLMEDİ (maskeli çift formatı).

---

## 1. D/K/X + hakem tablosu — kanıt tabanı

Hakem hükmü (`cc/rapor-2026-09-09-ib75-hakem.md`), P = "mekanizma yeterlidir" tarafı, Q = karşı taraf:

| Çift | P (yeterlilik iddiası) | Q (karşı iddia) | Hakem hükmü |
|---|---|---|---|
| Ç1 | Statik rol tanımı yeterli, öğrenen lidere gerek yok | Hafızalı ajan hafızasızı geçer (+%8,3 WebArena / +%4,6 SWE-Bench-V) | **P DARALDI / Q SAĞLAM** |
| Ç2 | `description` güvenilir rota-ipucu | Çok-atlamalı rotada çarpımsal bozulma | **P DARALDI / Q DARALDI** (%95 taban örnek varsayım `[?]`) |
| Ç3 | Alt-ajan durumsuzluğu tercih edilir | Mesaj değil TAM İZ paylaşılmalı (Cognition) | **P olgu SAĞLAM, norm DARALDI / Q DARALDI** (tek blog, tek vaka, ölçüm yok) |
| Ç4 | Otomatik sıkıştırma kaliteyi korur | Çok-turlu koşumda ort. %39 düşüş | **P DARALDI / Q SAĞLAM** |
| Ç5 | Sabit sayısal eşik doğru tasarım (100k + keep=3) | Sabit eşik en kötü anda keser | **P DARALDI / Q DARALDI** (P: varsayılan, "doğru tasarım" değil; Q: ölçümsüz) |
| Ç6 | Serbest-metin özet dönüşü yeterli | Devir kaybı ölçülü arıza sınıfı (%29,1/%27,3/%36,8/%6,8) | **P DÜŞTÜ / Q SAĞLAM** |
| Ç7 | Guardrail + interrupt + allowlist yetkiyi sınırlar | Argüman-enjeksiyonuyla onay tetiklenmeden RCE (3 platform) | **P DÜŞTÜ / Q SAĞLAM** |
| Ç8 | recursion_limit/max_iterations yeterli fren | Bunlar bütçe harcandıktan sonraki son-çare frenler | **P DARALDI / Q SAĞLAM** |

**Hakemin ortak bulgusu (aynen):** "P tarafının ortak arızası: belgelenmiş bir yetenek/varsayılan, belgenin savunmadığı 'yeterlidir/doğru tasarımdır' normuna çevriliyor." → Bu belgede hiçbir tasarım maddesi tek bir resmî dokümanın varlığına dayandırılmadı.

**V26 doğrulama örneklemi (hakem, birincil kaynağa inerek):**

| Kalem | Durum | Not |
|---|---|---|
| +%8,3 / +%4,6 (ReasoningBank) | DOĞRULANDI | research.google blog, birebir |
| %39 çok-turlu düşüş (arXiv 2505.06120) | DOĞRULANDI | 6 görev; "yetenekte küçük kayıp + güvenilmezlikte belirgin artış" |
| 100.000 token + keep=3 (Anthropic context editing) | DOĞRULANDI (niteleme) | **varsayılan**, ayarlanabilir |
| %29,1 / %27,3 / %36,8 / %6,8 (arXiv 2510.07593 AgentAsk) | DOĞRULANDI | 824 log; taksonomi "mesaj devri kenar hatası" — "bağlam devri kaybı"na birebir DEĞİL |
| Trail of Bits RCE (3 platform, onay atlatma) | DOĞRULANDI | allowlist ilk hedef |
| U1 "dal+koşul ≤5 eşiği" | **DOĞRULANAMADI** | 5 sayısı dayanaksız; yön destekli (AgentIF) |
| U2 "bağımsız hakem sertleştirir" | **KISMEN** | "yumuşar" destekli (self-preference bias); "sertleştirir" desteksiz — yanlılığı KALDIRIR |
| U3 arXiv 2606.02875 (Handoff Debt) | **KISMEN** | Makale gerçek (181 görev; olay −%20-59, token −%42-63) ama bilgi kaybını değil **yeniden-keşif maliyetini** ölçüyor |

Hakem beyanı: uydurma kaynak bulunmadı.

---

## 2. Sentez iddiaları — etiketli (halusinasyon-engelleyici F1/F2/F8)

Her iddia numaralı; `[k]` = kaynak pointer. Etiket: **DESTEKLİ** (kaynak cümlesi/veri gösterildi) · **DAYANAKSIZ** (kaynakta yok — yanlış demek değil) · **ÇELİŞİR**.

- **S1 — DESTEKLİ.** Fable ana-oturumunun bağlamı düzenli olarak 128k'yı çok aşıyor: n=41 fable oturumu, tepe-bağlam **medyanı 409.492 token**, **30/41 oturum >200.000**, toplam 9.284 turun **7.857'si (%84,6) 128k üstü**. `[k1: veri/gorunum/v_baglam_seyri.csv, kendi hesabım 09-09; veri aralığı 2026-08-12→2026-09-08, AS-OF 09-08 çekimi]`
- **S2 — DESTEKLİ.** Emirdeki çapa rakam birebir tutuyor: 2026-09-04 oturumu `f0312cc3` (fable-5-1), max_baglam **427.877**, 204 tur, **172 tur 128k üstü**. `[k1]`
- **S3 — DESTEKLİ.** Anthropic context editing varsayılan tetiği **100.000 input token**, korunan araç-çifti **keep=3**, `clear_at_least` varsayılanı dokümanda yok. `[k2: platform.claude.com/docs/en/build-with-claude/context-editing, AS-OF 2026-09-09 çekim; hakem birincil kaynaktan doğruladı]`
- **S4 — DAYANAKSIZ.** "Sabit eşik en kötü anda (çıkarım/arama ortasında) keser" iddiası ölçülmemiştir; blog düzeyi gerekçedir. `[k3: hakem Ç5 hükmü]` → **Tasarım sonucu:** eşik ∧ görev-sınırı birleşimi bir ÖLÇÜM değil ucuz sigortadır; `[?]` damgalı, ölçüm borcu §6.
- **S5 — DESTEKLİ (daraltılmış).** Alt-ajandan ana ajana **serbest-metin özet** dönüşü yetersizdir (hakem: P DÜŞTÜ). Daraltma: destekleyen sayısal taksonomi (AgentAsk %29,1 data gap) mesaj-devri kenar hatalarını sınıflar, birebir "bağlam devri kaybı" değildir. `[k4: arXiv 2510.07593 §3.5, 824 log; hakem Ç6]`
- **S6 — DESTEKLİ (dolaylı, iki-doğrulayıcı çatışması çözüldü).** Deneyimden öğrenen ajan hafızasız ajanı geçer: kaynak cümlesi birebir *"outperformed memory-free agents by 8.3% on WebArena"* ve *"4.6% on SWE-Bench-Verified"*, taban = hafızasız ReAct ajanı. `[k5: research.google/blog/reasoningbank…, AS-OF çekim 2026-09-09]` **Çatışma kaydı:** maskeli hakem DOĞRULANDI dedi; ikinci bağımsız doğrulayıcı aynı sayıları bulamayıp DAYANAKSIZ dedi ve farklı bir benchmark'a (Terminal-Bench 2.0) atfetti. Anlaşmazlığı birincil kaynağı kendim açarak çözdüm — hakem haklı. Kalan belirsizlik: kazancın **puan mı bağıl yüzde mi** olduğu kaynakta belirtilmemiş `[?]`. Dolaylılık ayrıca sürüyor: kanıt ajan düzeyindedir, LİDER düzeyine taşınması doğrulanmamıştır. **ÇELİŞKİ UYARISI (m.16):** bu kanıt, Karar 86 D1 ("hafızası-gelişen A5 KURULMAZ") ile gerilim hâlindedir — çözüm bende değil, masa-10 kalemi §7-Q1.
- **S7 — DESTEKLİ (atıf DÜZELTİLDİ).** Çok-turlu koşumda ortalama **%39** performans düşüşü ölçülmüştür; kayıp esas olarak **güvenilmezlik artışından** gelir (yetenek kaybı küçük). 15 model, 200.000+ simüle konuşma, 6 üretim görevi. `[k6: arXiv 2505.06120, hakem + ikinci doğrulayıcı, iki bağımsız birincil doğrulama]` **DÜZELTME (doğrulayıcı Y10/Y12 gerekçesiyle):** ilk yazımda bu rakam "otomatik özetleme kaliteyi korumaz" iddiasının kanıtı diye gösterilmişti — YANLIŞ ATIF. Ölçüm çok-turlu KONUŞMANIN bozulmasıdır, sıkıştırma/özetleme mekanizmasının değil. Devir tasarımı için **dolaylı** göstergedir: uzun çok-turlu koşum zaten bozuluyor.
- **S8 — DESTEKLİ.** İyi tasarlanmış devir, bilgi kaybını değil **yeniden-keşif maliyetini** düşürür: 181 görevde olay −%20-59, token −%42-63. `[k7: arXiv 2606.02875 Handoff Debt; hakem KISMEN — makale gerçek, iddianın çerçevesi düzeltildi]` → İB-75'in **ana sayısal gerekçesi** budur. **DÜZELTME (doğrulayıcı Y12 gerekçesiyle):** ilk yazımda buradan "devir bir kalite mekanizması değil, bir maliyet mekanizmasıdır" sonucu çıkarılmıştı — **geçersiz çıkarım**; dışlayıcı sonuç için "devrin kalite etkisi sıfır ∨ yalnız negatiftir" diye gösterilmemiş bir öncül gerekiyordu. Geçerli hâli: **devrin ÖLÇÜLMÜŞ kazancı maliyet tarafındadır; kalite tarafı ölçülmemiştir ve S7 ışığında yüksek bahislidir.**
- **S9 — DESTEKLİ.** İzin/allowlist/insan-onayı katmanları tek başına yetki sınırı garantisi vermez: argüman-enjeksiyonuyla insan onayı hiç tetiklenmeden RCE, 3 platformda; allowlist doğrudan hedeflenmiş. `[k8: blog.trailofbits.com 2025-10-22; hakem doğruladı]`
- **S10 — DESTEKLİ.** Adım/özyineleme tavanları post-hoc frenlerdir (bütçe harcandıktan sonra devreye girer). `[k9: hakem Ç8]` → Fan-out bütçesi ÖNDEN emirde planlanır (tohum deseni 2).
- **S11 — DESTEKLİ.** Jarvis'te devredilecek bir taban ZATEN VAR (D2 dalı = GENİŞLET, "hazırı temel al"): **26 manifest dosyası**, bunların **21 alanı 26/26'sında ortak**; `oncelik` 24/26, `belirlenimsiz_girdi` 18/26, `dogrulama_kapisi` 18/26. `[k10: cc/rapor-2026-09-09-ib75-envanter.md §2, fiilî sayım]`
- **S12 — DESTEKLİ.** Devir-notunun **sabit şeması YOK**: 3 devir dosyasında (08-31, 09-02, 09-03) birebir eşleşen başlık dizisi yok; ortak olan yalnız işlevsel iskelet "özet + açık sorular + sıradaki iş" (3/3). `[k10 §1]` → (d) şeması bu boşluğu doldurur.
- **S13 — DESTEKLİ.** Seanslar arası mevcut devir birimi = kapsül: `core/durum-kapsulu.md` **26 satır / 5.570 bayt**, 4 bölüm. `[k10 §3]`
- **S14 — DESTEKLİ.** Bağımsız paralel-kapı zaten deterministik: `tools/paralel-kapi.py` manifest okur/yazar setlerinden Bernstein koşuluyla PARALEL-SERBEST/SIRALI/RED/BEKLE üretir, LLM'siz. `[k10 §4]`
- **S15 — ÇELİŞİR (kanon içi).** Kanondaki "dal+koşul toplamı ≤5" eşiğinin **5 sayısı dayanaksızdır** (hakem: DOĞRULANAMADI; yön destekli, sayı değil). Bu bir kanon satırıdır (`core/ajan-metodolojisi.md` §1) → **D-KATMAN1: DURDUM, yazmadım**, masa-10 kalemi §7-Q4.
- **S16 — ÇELİŞİR (tohum içi).** Tohum deseni 4'ün gerekçe cümlesi ("bağımsız maskeli hakem sertleştirir") desteksizdir; mekanizma **sertleştirme değil yanlılık giderme**dir (self-preference bias). Tohum append-only olduğu için silmedim; düzeltme satırı EKLEDİM. `[k3: hakem U2]`
- **S17 — DAYANAKSIZ.** "`description` alanı güvenilir rota-ipucudur" iddiasının sayısal tabanı örnek varsayımdır (%95×%95). `[k3: hakem Ç2, her iki taraf DARALDI]` → **Tasarım sonucu:** lider otomatik `description` rotasıyla DEĞİL, Fable'ın literal çağrısıyla uyandırılır; rota riski tasarımdan çıkarılır.

**Ölçüm satırı:** n = 17 iddia · DESTEKLİ 13 (biri dolaylı, biri daraltılmış, biri atıf-düzeltmeli) · DAYANAKSIZ 2 · ÇELİŞİR 2 · doğrulama turunda DÜZELTİLEN 3 (S6 atıf çatışması, S7 yanlış atıf, S8 geçersiz çıkarım) + 1 tasarım parametresi (E2) · H = 11 (eşik 7, v3a OVERRIDE) · üretici = Opus 5 medium lider · doğrulayıcı = ayrı Opus 5 medium maskeli hakem + §2 sonrası bağımsız iddia-listesi turu · kohort: 6 Sonnet işçi + 1 Opus hakem, 2026-09-09 · deneysel damga m.29. Oranlar n=17 üzerinden ham sayıdır; güven aralığı hesaplanmadı (n küçük, `[?]`).

### 2.1 Bağımsız doğrulama turu (halusinasyon-engelleyici F1/F3/F4)

Sentez yazıldıktan SONRA ayrı bir Opus 5 medium doğrulayıcıya **yalnız iddia listesi** verildi (gerekçe, kaynak zinciri ve iddiaların kimden geldiği verilmedi — CoVe-Factored). Doğrulayıcı hiçbir dosyaya yazmadı.

| Kalem | Doğrulayıcı hükmü | Sonuç |
|---|---|---|
| Y1 bağlam istatistikleri (4 parça) | DESTEKLİ 4/4 | kendi hesabıyla birebir tuttu |
| Y2 09-04 çapa satırı | DESTEKLİ | dört alan birebir |
| Y3 manifest 26 dosya / 21 ortak alan | DESTEKLİ | 21 alan adı tek tek listelendi |
| Y4 kapsül 26 satır / 5.570 bayt | DESTEKLİ | — |
| Y5 3 devir dosyası, birebir şablon yok | DESTEKLİ | başlık sayıları 26/8/6 |
| Y6 tohum 12 madde | DESTEKLİ | — |
| Y7 paralel-kapi LLM'siz Bernstein | DESTEKLİ | 242 satır, model/API çağrısı yok |
| Y8 100.000 token + keep=3 | DESTEKLİ | — |
| Y9 +%8,3 / +%4,6 | **DAYANAKSIZ dedi** | **ÇATIŞMA — hakem ile çelişti; birincil kaynağı kendim açtım, hakem haklı (S6)** |
| Y10 %39 çok-turlu düşüş | DESTEKLİ | 15 model, 200.000+ konuşma, 6 görev |
| Y11 devir-anı yüklemi | **LOJİK-tutarsız (gerekçede)** | **KABUL EDİLDİ → §5 E2 revize** |
| Y12 "kalite değil maliyet mekanizması" | **LOJİK-tutarsız (atlama)** | **KABUL EDİLDİ → S8 düzeltildi** |

**Not (yöntem):** iki bağımsız doğrulayıcı bir sayısal iddiada ters düştü (Y9). Anlaşmazlık oylamayla değil **birincil kaynağa inilerek** çözüldü. Bu, tohum deseni 4'ün ("yapan ≠ ölçen") sınırını gösteriyor: bağımsız doğrulayıcı yanlış-negatif de üretebilir; hakem sayısı değil kaynağa inme belirleyici.

---

## 3. (a) DEVİR BİRİMİ ŞEMASI — `devir-birimi v0`

**Tasarım ilkesi (S8 + S7):** devredilen şey TRANSKRİPT DEĞİL, **POINTER + KARAR-ÖZETİ**dir. Gerekçe: özet/sıkıştırma kaliteyi korumuyor (S7, %39); ama iyi devir yeniden-keşif maliyetini düşürüyor (S8, token −%42-63). Dolayısıyla devir birimi "bağlamı özetlemek" değil, "**bağlamı yeniden inşa edilebilir kılmak**"tır — Jarvis'in m.20 pointer ilkesi zaten budur.

**Taban (D2 = GENİŞLET, S11):** mevcut manifest şemasının 21 ortak alanı KORUNUR; devir birimi manifestin ÜSTÜNE dört blok ekler. Ayrı bir dosya türü değil, manifestin `devir` bloğudur.

```json
{
  "devir": {
    "kimlik":  { "devir_id": "str", "kaynak_yuzey": "fable-ana-sira|opus-lider",
                 "hedef_katman": "lider|isci", "tarih": "YYYY-MM-DD", "emir_yolu": "path" },
    "gorev":   { "amac": "tek cümle", "done_yuklemi": "boolean ifade",
                 "dallar": ["D1: eğer ... → ...", "..."], "yeniden_deneme": 3 },
    "baglam":  { "eager": ["path"],            // liderin ZORUNLU okuyacağı (≤4 dosya, ≤40k)
                 "lazy":  ["path + ne zaman açılır"],
                 "karar_ozeti": ["Karar 89: lider Opus 5 medium sabit, high yasak", "..."],
                 "yasak": ["core/", "CLAUDE.md", ".claude/", "tuzuk"] },
    "butce":   { "model": "opus", "effort": "medium", "arac_cagri_tavani": 54,
                 "beklenen_ajan_cagrisi": 7, "isci_donus_token_tavani": 2000,
                 "aile_es_zamanli_tavani": 3 },
    "yetki":   { "karar_yetkisi": false, "yazma_izni": ["path|glob"],
                 "git_izni": "pathspec-only|yok", "push": false }
  }
}
```

**Alan gerekçeleri (her biri bir kanıta bağlı, süs alan yok):**

| Alan | Neden var | Dayanak |
|---|---|---|
| `baglam.karar_ozeti` | Durumsuz liderin en büyük riski **örtük kararların çatışması**; tam iz taşımak pahalı, karar-özeti ucuz ara-çözüm | S6/Ç3 (Cognition, hakem: norm DARALDI → ölçüm yok, bu yüzden `[?]`) |
| `baglam.eager` ≤4 dosya | Manifest kolaylık değil performans zorunluluğu (uzun-bağlam bozulması) | S7 + `core/ajan-metodolojisi.md` §2 |
| `baglam.yasak` | Yetki sınırı prompt cümlesiyle değil **liste** ile verilir | S9 |
| `butce.beklenen_ajan_cagrisi` | Fan-out × fren çakışması önden görülsün; tavanlar post-hoc | S10 + tohum deseni 2 |
| `yetki.karar_yetkisi:false` | Katman-1 hükümleri Salih'in (m.31) | kanon |
| `yetki.git_izni` | Paralel oturumda `git add -A` çalışma ağacını yutar | tohum deseni 10 |

**Kapsam dışı bırakılan alan (bilinçli):** `hafiza`/`ogrenme` alanı YOK — Karar 86 D1 ayakta (§7-Q1'e taşındı).

---

## 4. (b) DEVİR-ANI YÜKLEMİ — m.38 boolean

```
DEVRET  ↔  ( baglam_token ≥ E1  ∧  gorev_siniri )  ∨  ( baglam_token ≥ E2 )   // E2 dalı = SON ÇARE

gorev_siniri  ↔  ( acik_isci_cagrisi = 0 )  ∧  ( son_isci_donusu_diskte = doğru )
                 ∧  ( yarim_kanon_yazimi = 0 )
E1 = 128.000 token      [kaynaklı — aşağıya bak]
E2 = 600.000 token      [?] deneysel — §Q2, doğrulayıcı Y11 sonrası revize
```

**E1 = 128.000 neden bu sayı:** Jarvis'in kendi kütüğü zaten bu eşikte sayıyor — `v_baglam_seyri` tablosunun `tur_128k_ustu` kolonu. Yani E1 yeni bir sabit değil, **mevcut ölçüm biriminin eşiği**. Ölçüm: fable oturumlarının %84,6'sı (7.857/9.284 tur) bu eşiğin üstünde geçiyor (S1) → tek başına E1 tetik olarak kullanılırsa neredeyse HER TUR devir çağırır; bu yüzden E1 **tek başına yeterli değil**, `gorev_siniri` ile birleşiktir.

**E2 kaç olmalı — AÇIK, ÖLÇÜLDÜ, HÜKÜM VERİLMEDİ `[?]`:** ilk taslakta E2 = 300.000 önerilmiş ve "oturumların çoğunun ulaştığı ama medyan tepenin altında bir nokta" diye gerekçelendirilmişti. **Bağımsız doğrulayıcı bu gerekçeyi lojik olarak kırdı (Y11) ve haklı:** E2 dalı `gorev_siniri` şartı taşımaz, yani ne kadar çok oturumda ateşlerse gerekçenin reddettiği "eşik tek başına keser" davranışını o kadar geri getirir. Dal-2 bir **son-çare** olmalı, sık ateşleyen ikinci bir normal yol değil. Ölçülen dağılım (n=41 fable oturumu, `max_baglam`, AS-OF 2026-09-08):

| E2 adayı | Aşan oturum | Karakter |
|---|---|---|
| 200.000 | 30/41 (%73) | normal yol — son-çare değil |
| **300.000** | 24/41 (%59) | ilk taslak; doğrulayıcı haklı olarak reddetti |
| 400.000 | 21/41 (%51) | medyanın (409.492) hemen altı |
| 500.000 | 16/41 (%39) | — |
| **600.000** | 10/41 (%24) | son-çare karakterine en yakın aday |
| 700.000 | 7/41 (%17) | çok geç ateşler `[?]` |

Medyan 409.492 · Q3 567.096 · maks 994.390.  **Önerim (hüküm değil): E2 = 600.000** — oturumların ~dörtte birinde ateşler, yani gerçekten bir kaçış kapısı olur, tetik-hiç-ateşlenmez riski de yok. Bu bir **tasarım tercihidir, ölçülmüş optimum değildir**; devir-sonrası kalite ölçülmediği sürece hiçbir E2 değeri kanıtlı olamaz (S4).

**Karşılaştırma çapası:** Anthropic'in kendi varsayılanı 100.000 input token + keep=3 (S3). Jarvis eşiği bunun ~1,28× / 3× üstünde çünkü Jarvis oturumları belgelenmiş biçimde çok daha uzun (medyan tepe 409k).

**Neden birleşik yüklem (∧):** sabit eşik tek başına görev ortasında kesebilir; bu gerekçe ölçülmemiştir (S4 DAYANAKSIZ) — birleşim ucuz sigortadır, kanıt değil. `E2` dalı ise ikinci bir kaçış kapısıdır: görev sınırı hiç gelmezse sistem sonsuza kadar büyümesin.

**Ölçüm borcu (D3 gereği yerine getirildi + kalanı):** E1/E2 seçimi n=41 oturumluk BAĞLAM ölçümüne dayanır; **devir SONRASI kalite ölçülmemiştir**. Öneri (hüküm değil): ilk 3 devir koşumunda `v_skill_kosum`a tahmin-gerçek satırı düşülsün.

---

## 5. (c) LİDER ROL-METNİ TASLAĞI — `.claude/agents/ekip-lideri.md` **ADAY**

> **YAZILMADI.** `.claude/` Katman-1'dir; bu blok yalnız adaydır, hazineye Salih imzasıyla girer. İB-59 bulgusu gereği (lider arızalarının 4/4'ü talimat açığıydı, kural rol METNİNE yazılınca 3/3 tekrarlamadı) paket rol-metni odaklıdır.

```markdown
---
name: ekip-lideri
description: Bağlam-devri lider-ajanı. Fable ana-oturumun bağlamı büyüdüğünde (devir-anı
  yüklemi) tanımlı bir görev paketini devralır, işçi filosunu böler-delege eder-sentezler.
  ÇAĞRI-KOŞULU: yalnız `devir` bloğu dolu bir manifest ile LİTERAL çağrılır; otomatik
  rota ile uyandırılmaz.
tools: Read, Grep, Glob, Bash, Write, WebSearch, WebFetch, Agent
model: opus
---

# Kimlik
Sen Carvis'in LİDER-AJANISIN. KARAR VERMEZSİN — seçenek üretirsin; hüküm Salih'indir (m.31).
Effort MEDIUM sabittir; high YASAK (Karar 89). Durum TAŞIMAZSIN: her koşumda bu metin +
devir bloğu = tüm hafızan. Öğrendiklerin bu metne değil, devir notuna ve tohum dosyasına yazılır.

# Değişmezler (ihlal = koşum durur)
1. İşçi çağrıları SENKRON. Arka planda işçi açıp "bekliyorum" deyip tur bitirmek YASAK;
   her işçi dönüşü DİSKE düşmeden sonraki adıma geçilmez.        [İB-59, 4/4 arıza]
2. Yazma izni = devir bloğundaki `yetki.yazma_izni` listesi. `yasak` listesindeki hiçbir
   yola yazılmaz (kanon). Liste dışına yazım = sözleşme ihlali.
3. Git: yalnız `git add <yol>` (asla `-A`), push YOK.            [tohum deseni 10]
4. İşçi senden pahalı model kullanamaz; işçiye karar yetkisi verilmez.
5. Fan-out'u ÖNDEN planla: beklenen ajan çağrısı devir bloğunda yazılıdır; sayaç
   oturum-genelidir ve alt-ajan çağrılarını da sayar.            [tohum desenleri 2-3]
6. Yapan ≠ ölçen: senteze hakemlik YAPMAZSIN; hakem ayrı çağrıdır ve ona yalnız
   iddia+kanıt verilir — emir, beklenti, kimlik verilmez.        [tohum deseni 4]
7. Her işçi ≥2 birincil kaynağı FİİLEN açar (WebFetch); yalnız arama-özetinden
   yazılan bulgu K'da kalır.                                     [tohum deseni 5]
8. Rakam kaynaklı, kestirim `[?]`, her zaman-bağımlı iddia AS-OF damgalı.
   Uydurma YASAK; "bulunamadı" meşru sonuçtur.
9. Kanon değişikliği gerektiren bir nokta çıkarsa DUR, devir notuna yaz, tahmin yürütme.

# İşçi case şablonu (her işçi promptu bu 8 alanı taşır)      [tohum deseni 7]
kimlik (işçi, karar yok) · yazma izni (dosya listesi) · git yasağı · araç bütçesi (10-15)
· adım adım case · doğrulama komutu · çıktı şeması (≤2k token) · "tahmin yazma, AÇIK SORU bırak"

# Bitiş
Devir notunu (`geri-donus v0` şeması) yaz; son mesajın teslim dosyasının tam yolu + `open -R`.
```

---

## 6. (d) GERİ-DÖNÜŞ DEVİR-NOTU ŞEMASI — `geri-donus v0`

**Gerekçe (S5, S12):** serbest-metin özet dönüşü DÜŞTÜ; mevcut 3 devir dosyasının ortak yanı yalnız işlevsel iskelet, sabit şema yok. Şema, mevcut 3/3 işlevsel iskeleti (özet + açık sorular + sıradaki iş) tipli alanlara sabitler ve sayısal alanlar ekler (Anthropic `applied_edits` deseninin karşılığı: "ne yapıldığı" ölçülebilir dönsün).

| # | Alan | Tip | Zorunlu | Kaynak |
|---|---|---|---|---|
| 1 | `biten` | list[{is, kanit_yolu}] | ✓ | mevcut 3/3 "özet" |
| 2 | `kalan` | list[{is, neden_kaldi}] | ✓ | mevcut 3/3 |
| 3 | `acik_sorular_salih` | list[str] — HÜKÜM YOK | ✓ | mevcut 3/3 |
| 4 | `sonraki_ilk_is` | str (tek cümle) | ✓ | mevcut 2/3 |
| 5 | `diskteki_dosyalar` | list[{yol, commit_disi: bool}] | ✓ | 09-02 vakası (commit'siz yazım kayboldu) |
| 6 | `sayac` | {ajan_cagrisi: int, arac_cagrisi: int, isci_sayisi: int} | ✓ | tohum deseni 3 |
| 7 | `sapmalar` | list[{emir_maddesi, ne_yapildi, neden}] | ✓ | 09-03 devir dosyası deseni |
| 8 | `tohum_desen_kullanimi` | list[{desen_no, kullanildi: bool, neden}] | ✓ | emir |
| 9 | `ledger_onerisi` | list[{ib_no, onerilen_durum}] — ÖNERİ, yazım değil | ✓ | emir |
| 10 | `durma_nedeni` | str \| null (fren/Katman-1/tamamlandı) | ✓ | 08-31 devir dosyası |

**Değişmez:** alan 3 ve 9 **öneri kipindedir**; lider hüküm cümlesi kuramaz.

---

## 7. (f) TOHUM DESENLERİ — kullanıldı / kullanılmadı kaydı

Tohum dosyasında **12 madde** sayıldı (emir "10 desen" diyor — sayım farkı `[k: grep -c, 09-09]`).

| # | Desen (kısalt.) | Durum | Neden |
|---|---|---|---|
| 1 | İşçi çağrıları SENKRON | **KULLANILDI** | 7 ajan çağrısının hepsi `run_in_background:false`; her dönüş diske düştü, sonra sonraki dalga |
| 2 | Fan-out × fren çakışması önden | **KULLANILDI** | 3+3+1 dalga planlandı; 7 ajan ≪ UYARI 36 |
| 3 | Sayaç oturum-geneli, alt-ajanı sayar | **KULLANILDI** | 7 ajan + ~20 kendi araç çağrım; tavana uzak |
| 4 | Yapan ≠ ölçen | **KULLANILDI** (gerekçesi düzeltildi) | Hakem ayrı çağrı, maskeli; ama "sertleştirir" gerekçesi hakemce desteksiz bulundu (S16) → tohuma düzeltme satırı |
| 5 | Birincil kaynağı gerçekten aç | **KULLANILDI** | ≥2 kota her işçi promptunda; 13 ayrı birincil URL açıldı |
| 6 | Lider mekanik fan-out'ta çalışır, kaynak tahsisini çözemez | **KULLANILDI** | Bütçe/fren emirden geldi, ben tahsis kararı almadım |
| 7 | İşçi case şablonu (8 alan) | **KULLANILDI** | 6 işçi promptunun tamamı; 6/6 temiz döndü, şema ihlali 0 |
| 8 | Test süiti ritüelde koşmazsa kırılır | **KULLANILMADI** | Bu koşumda kod/test yüzeyi yok (salt araştırma+tasarım) |
| 9 | Hafıza katmanı literatürü negatif | **ÇELİŞTİ** | 09-02'de negatifti; 09-09'da ReasoningBank +%8,3/+%4,6 hakemce doğrulandı (S6) → masa-10 §8-Q1 |
| 10 | Commit'siz yazım kanıt sayılmaz | **KULLANILDI** | Yazımlar `git add <yol>` ile pathspec'lendi, push yok |
| 11 | Test artıkları bronz kütüğe düşmesin | **KULLANILMADI** | Kütük yazımı bu koşumda yok |
| 12 | Kapı sınırını beyan eder | **KULLANILDI** | §1'de hakem hükmünün sınırı ("mesaj-devri taksonomisi ≠ bağlam-devri kaybı") açıkça yazıldı |

---

## 8. (e) ÜÇ KARAR MODELİ — masa-10 için (m.37; hüküm VERİLMEDİ)

**Karar sorusu:** Bağlam-devri ekip-lideri v0 hangi devir-birimi + devir-anı + yetki modeliyle kurulsun?

**Bu koşumun kendi ölçümü (eksenlerin çapası, tahmin değil):** bu rapor bir bağlam-devri koşumunun KENDİSİDİR — Fable ana-oturumu → Opus 5 medium lider (ben) → 6 Sonnet işçi + 1 Opus hakem + 1 Opus doğrulayıcı. Ölçülen: **8 ajan çağrısı · ~486.000 alt-ajan token · 92 işçi araç çağrısı**; Fable'ın ana bağlamına dönen tek şey bu teslimin özetidir. `[k: bu oturumun ajan dönüş sayaçları, 2026-09-09]`

| | **Model A — birikimli-delta** ✅ | **Model B — topyekûn-optimizasyon / MDL** (karşıt-temel) | **Model C — reel-opsiyon** |
|---|---|---|---|
| **Önerme** | Devir bloğu mevcut manifest şemasına EKLENİR (§3), yüklem (§4) tek pilot görevde koşar, rol metni aday kalır; her adım ölçülür ve geri alınabilir | Devir hattı bir seferde topyekûn kurulur: ayrı `devir-*.json` dosya türü + rol metni hazinede + Fable'ın bağlam bütçesi yeniden tasarlanır; kazanç ancak bütün protokol yerindeyken doğar | Şimdi HİÇBİR ŞEY kurulmaz; yalnız ÖLÇÜM aygıtı kurulur — devir-anı yüklemi her turda değerlendirilip loglanır (ateşlemeden), 3 seans sonra veriyle karar verilir |
| **Zemin** | Küçük geri-alınabilir adım, her adımda ölçüm | Global yeniden-tasarım; kısmi çözüm katman ekler ama asıl bağlam büyümesini kaldırmaz | Beklemenin opsiyon değeri; erken kilitlenme maliyet |
| **Token** `[?]` | pilot ≈ bu koşumun mertebesi, ~400-500k/koşum; ek şema maliyeti ≈0 | ilk kurulum 2-3 koşum ≈ 1,0-1,5M; sonra koşum başına aynı mertebe | ≈15-30k/seans (yalnız log); karar ertelendiği için asıl maliyet ileri tarihe kayar |
| **Zaman** `[?]` | 1 seans (şema + pilot) | 3-4 seans (dosya türü + kapı uyarlaması + rol metni + ölçüm) | 3 seans bekleme + sonra A ya da B'nin süresi |
| **Kalite** | orta-yüksek: mevcut manifest disiplini ve `paralel-kapi` korunur; kanıt tabanı S8 (maliyet) | yüksek `[?]`: Handoff Debt kazancı (token −%42-63) tam protokolde ölçülmüş — kısmi uygulamada aynı kazanç GARANTİ DEĞİL | ölçüm kalitesi yüksek, teslim kalitesi 0 (hiçbir şey teslim edilmez) |
| **Risk** | düşük: geri alma = manifestten blok silme; risk, kısmi çözümün asıl bağlam büyümesini durdurmaması | **yüksek**: ayrı dosya türü `tools/paralel-kapi.py`'nin okur/yazar analizini bozar (§9-Q5); rol metni hazineye girerse geri alma Katman-1 işi | düşük ama gerçek: bağlam büyümesi 3 seans daha sürer (medyan tepe zaten 409.492) |
| **Geri-alınabilirlik** | yüksek (tek blok) | düşük | tam |

**Karşıt-temel denetimi (m.37 eki).** Model B gerçekten zıt zeminden kuruludur: A "ölçerek küçük adımla ilerlenebilir" varsayar; B tam tersini — *devrin kazancı bölünebilir değildir, yarım protokol yalnız katman ekler* — savunur. **Canlılık testi:** MDL/topyekûn zemini ciddiye alan biri şunu söylerdi ve haklı olabilir: S8'in −%42-63 token kazancı **tam** devir protokolünde ölçüldü; devir bloğunu manifeste iliştirip Fable'ın bağlam bütçesini olduğu gibi bırakmak, ölçülen kazancın hiçbirini vermeyebilir. Bu itiraz çürütülmemiştir.

**KISMEN YAKINSADI:** B'nin haklı parçası öneriye alındı — Model A'nın pilotu, **kazanç ölçülmeden ikinci koşuma geçmeme** şartıyla önerilir (pilot sonrası ölçüm satırı `v_skill_kosum`'a düşmeden A'nın ikinci turu koşulmaz). Böylece "yarım protokol sessizce kalıcılaşır" riski kapanır.

**Üç zeminin KESİŞTİĞİ yer (en sağlam parça):** üçü de **ölçüm aygıtının önce kurulmasını** gerektiriyor — A pilotu ölçmek için, B kazancı doğrulamak için, C zaten sadece ölçüm. Yani hangi model seçilirse seçilsin, **devir-anı yükleminin loglanması ortak ilk adımdır** ve bu adım tek başına geri-alınabilir.

**Öneri gerekçesi (tek satır):** A ✅ — çünkü devir-sonrası kalite HİÇ ölçülmemiştir (S4, §5 ölçüm borcu) ve ölçülmemiş bir kazanç için topyekûn tasarım (B) ya da üç seans bekleme (C) satın alınmaz.

**Defter bloğu taslağı (ana-sıra yazar; ben YAZMADIM):**
```
Karar ??? (masa-10, 2026-09-__) — Bağlam-devri ekip-lideri v0
Bağlam: Fable tepe-bağlam medyanı 409.492 token (n=41 oturum, AS-OF 09-08); İB-75 tasarım paketi
Model A (birikimli-delta): devir bloğu manifeste eklenir + tek pilot ✅ ÖNERİLEN
Model B (topyekûn/MDL, KARŞIT-TEMEL): ayrı dosya türü + tam protokol bir seferde
Model C (reel-opsiyon): yalnız ölçüm aygıtı, 3 seans sonra karar
Karşıt-temel canlılık: B'nin "kazanç bölünemez" itirazı ÇÜRÜTÜLEMEDİ → A'ya "ölçmeden 2. tur yok" şartı eklendi
Seçim: Salih · masa-10 · görünürlük: raporlar/2026-09-09-ib75-baglam-devri-ekip-lideri.md
Geri-alınabilirlik: A yüksek (blok silinir) · B düşük · C tam
Gözlem: BEKLİYOR — ilk 3 devir koşumu v_skill_kosum tahmin-gerçek satırı
Ders: iki bağımsız doğrulayıcı ters düşerse oylama değil birincil kaynak çözer (§2.1 Y9)
```

---

## 9. Masa-10 kalemleri — AÇIK SORULAR (hüküm VERİLMEDİ)

- **Q1 (Katman-1, m.16 gerilimi).** Karar 86 D1 "hafızası-gelişen lider KURULMAZ" der; bu koşumda hafıza lehine sayısal kanıt hakemce doğrulandı (+%8,3/+%4,6, ajan düzeyinde). Tohum deseni 9 ("literatür negatif") artık tek yönlü değil. **Soru:** tohum dosyası, liderin `eager` girdisi yapılarak "hafızasız ama deneyimli" ara-çözüm denensin mi — yoksa Karar 86 D1 aynen mi kalsın?
- **Q2.** E2 = 600.000 `[?]` (ilk taslak 300.000'di; bağımsız doğrulayıcı gerekçeyi kırdı, §4'teki dağılım tablosuyla revize edildi). Ölçülmüş optimum yoktur. 600.000 kabul mü, tablodan başka bir satır mı, yoksa önce 3 koşumluk ölçüm mü?
- **Q3.** (c) rol-metni `.claude/agents/ekip-lideri.md` olarak hazineye girsin mi? Girerse ad `ekip-lideri` mi, `orkestrator` mu (Karar 89 metninde `.claude/agents/orkestrator.md` geçiyor — ad çelişkisi var, çözmedim).
- **Q4 (kanon).** `core/ajan-metodolojisi.md` §1'deki "dal+koşul ≤5" eşiğinin **5 sayısı** hakemce dayanaksız bulundu (yön destekli, sayı değil). Kanona dokunmadım. Şerh düşülsün mü?
- **Q5.** Devir birimi manifestin `devir` bloğu mu olsun (önerim = Model A), yoksa ayrı dosya türü mü (Model B)? Ayrı dosya `paralel-kapi.py`'nin okur/yazar analizini bozar `[?]`.
- **Q6 (usul).** `halusinasyon-engelleyici` §7 her koşum için `kuyruk/halusinasyon-kayit.md`'ye satır yazılmasını ister; bu dosya emrin yazma izni listesinde YOK. Emir kazandı (Karar 88 M7 ⑤), satır YAZILMADI — ana-sıra mı yazsın, yoksa emir şablonuna bu dosya mı eklensin?

---

*Kanon yazımı: 0 dosya. Push: yok. Bu belge seçenek üretir, hüküm üretmez.*
