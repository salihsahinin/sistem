# Seans Teslimi — Tahmin↔Gerçek Ambar Katmanı (2026-08-21, Kun-Chen P-1 koşumu)

**Tek cümle:** KB-02/03 icra borcu kapandı — üst modelin alt-model koşum tahminleri artık ambarda yapılandırılmış yaşıyor, sapma `v_kosum_tahmin_sapma` görünümünden tek sorguyla okunuyor, skill-koşum pilotu `v_skill_kosum` görünümünü aldı, gorev-emri-derleme'ye "skill koşucusu = alt model" alanı işlendi; İB-40 monolit referans dilimi aynı emirle koşuldu ve ilk V1 verim karşılaştırması aşağıda.

**Pipeline:** `cc/pipeline-2026-08-21-tahmin-gercek-ambar.md` · Emir: `cc/gorev-2026-08-21-1.md` · Commit'ler: `cd820eb` (manifest+emir) · `c7ecb80` (SH-1 tamamı) · bu rapor.
**Koşum özeti:** 3 Sonnet scout (12:21→12:28, paralel) + 1 Opus monolit (12:21→12:35) + Carvis sentez/ship (12:28→12:41). Salih'in yokluğunda, "devam bekleme" emriyle uçtan uca.

## 1. Ne kuruldu (adresli)
- **Bronz:** `veri/bronz/tahmin-olay.jsonl` — 32 satır: 7 tarihî koşumun (08-17×4 + 08-18×3; wf_id'ler DB-doğrulanmış) tüm rol tahminleri S-1a envanterinden elle/deterministik backfill + bu koşumun 4 tahmini. Grain: 1 satır = 1 (görev-emri, rol); aile-BAĞIMSIZ (gerçek aile-bazlı — JOIN gold'da).
- **Silver:** `amb_olgu_tahmin` (22 kolon; `tools/ambar-tablo.py` additive yükleyici) + sözleşme `veri/sozlesme/amb_olgu_tahmin.json` + 3 yeni veri-testi (`katman-olcum.py`: unique · wf ilişkisi · bant min≤max) — hat koşumu 13/13 PASS.
- **Gold:** `veri/gorunum/v_kosum_tahmin_sapma.csv` — JOIN wf_id + rol_norm (deterministik CASE; `amb_olgu_kosum.rol` serbest metin olduğu için) + durum etiketi ALTINDA/BANDA/ÜSTÜNDE/FORMÜL/TAHMİN-YOK/GERÇEK-YOK. `veri/gorunum/v_skill_kosum.csv` — iki dürüst blok: ana-sıra prompt sayımı (skill json_each ile atomik) + yalnız KESİN agent_type→skill eşlemesi (atlas→atlas-kosum); kayıplı haritalama GÖMÜLMEDİ.
- **Test:** `tools/testler/test_tahmin_katmani.py` — 5/5 PASS (gerçek script CLI koşumu, geçici repo; tüm paket 29 test OK).
- **Kural alanı:** `.claude/skills/gorev-emri-derleme/SKILL.md` — KB-03 A (Karar 17) "skill koşucusu = alt model" paragrafı + tahmin-bronz yazım adımı (Katman-2 icra; core/ dosyalarına dokunulmadı).

## 2. Tarihî sapma tablosu ilk kez sayısal (v_kosum_tahmin_sapma, 7 koşum)
ÜSTÜNDE 25 · BANDA 22 · TAHMİN-YOK 18 · FORMÜL 15 · GERÇEK-YOK 4 · ALTINDA 4. En büyük sapmalar: V26 5,41× (wf_bb445659 — İB-19'un doğduğu koşum) · ANTİTEZ 3,95× ve 3,47× (wf_fc0e9f76 — KB-02 ilk revizyon verisi). Kaynak: DB sorgusu 12:40. *(M-1'in el sayımı 34/24/5 farklı evrende: formül satırlarını çarpımla banda çevirip saymış; görünüm formülü ayrı etiketler — tanım farkı, çelişki değil.)*

## 3. İB-40 — pipeline ↔ monolit ilk V1 verim karşılaştırması (Karar 45; ölçüm-bankı satırları)
Kalite = emirdeki done-yüklemi koşullarının deterministik sayımı (Karar 48 uyumu: serbest öz-analiz yok).

| eksen | PIPELINE (3 Sonnet scout + Fable sentez) | MONOLİT (1 Opus, bölmeden) |
|---|---|---|
| alt-model çıktı-token | 72.579 (30.433+16.404+25.742) | **59.473** |
| duvar-saati (keşif+tasarım) | **14 dk** (12:21→12:35 G-1; scout paraleli 7 dk) | 14 dk (12:21→12:35) — eşit |
| araç çağrısı | 63 (21+13+29) | 42 |
| done-koşul sayımı | A 4/4 · B 4/4 · C 4/4 (DRFR blokları raporlarda) | 21/21 beyan (A∧B∧C∧tasarım; DRFR raporda) |
| tasarım çıktısı | DDL+2 görünüm CANLI (kod yazıldı, 5/5+13/13 test) | DDL+2 görünüm TASLAK (koşulmamış) |
| yalnız bir tarafın bulduğu | 4. kayıt (rapor-08-17-3) [S-1a] · rol serbest-metin JOIN engeli [Carvis V26 denetimi] | `hareket` tablosunda 40 Skill çağrısı = v_skill_kosum için 2. kaynak · sapma ön-sayımı · D-KATMAN1 çelişki bayrağı |
| üst-model payı | ölçülemedi [?] (ana-sıra oturumu ambara düşmüyor) | — (yok) |

**Dürüst okuma (tek koşum, genelleme değil):** monolit token'da %18 ucuz ve tek başına kapsamı bitirdi; pipeline aynı duvar-saatinde CANLI+test edilmiş implementasyona ulaştı ve iki tekil bulgu üretti — ama monolitin `hareket`-kanalı bulgusunu pipeline KAÇIRDI (aşağıda devşirme adayı). n=1; V1 verim tanımı için taban çizgisi, hüküm değil.

## 4. Tahmin↔gerçek 5. kayıt — kendi sapmam (KB-02 zinciri)
Sonnet scout çıktı-token tahminlerim 4,1-7,6× AŞTI (2-4k tahmin ↔ 16-30k gerçek); Opus monolit 3,0× AŞTI (12-20k ↔ 59,5k). Araç/süre tahminleri 7/8 eksende bandaydı ya da hafif aştı. **Revizyon (İB-19 deseni):** keşif-scout Sonnet taban bandı ≈15-30k çıktı; monolit Opus ≈40-60k; "dilim küçük → çıktı küçük" varsayımı YANLIŞ — rapor gövdesi + okuma turları çıktıyı şişiriyor. Kayıt ambara girdi (bronz 4 satır; gerçekleşen amb_olgu_kosum'da).

## 5. Salih'e açık kalemler (hüküm/imza bekleyen)
1. **Eşik kuralı TASLAĞI (KB-03 İB'nin son parçası — imzayla yürür, imzasız YÜRÜMEZ):** "Bir skill×model çifti v_skill_kosum'da n≥10 olduğunda medyan token/süre bandı hesaplanır; yeni koşum bandın 2× üstüne çıkarsa seans kapanışında sapma satırı raporlanır. Otomatik kural değişikliği YOK; her değişiklik ölçüm + Salih imzasıyla."
2. **FAIL damga alanı (Katman-1):** v_skill_kosum'un FAIL kolonu bugün hep NULL — hiçbir ambar tablosunda koşum-sonucu damgası yok. Öneri: bronz kosum-olay'a `sonuc` alanı (done-yüklemi PASS/FAIL, emirden) — şema kararı Salih'te.
3. **M-1 D-KATMAN1 çelişki bayrağı:** `cc/gorev-2026-08-17-3.md:7` üst modele tahmin yazmış (KB-02'ye aykırı). İcra tercihim: bronz ham kalır (m.8) — satır "TARİHÎ KAYIT" damgalı girdi; kural İHLALİ olarak silinmedi. Farklı hüküm istersen satır damgası değişir.
4. **Monolitten devşirme adayı (İB):** v_skill_kosum'a `hareket` tablosu kanalı (40 Skill çağrısı, skill×model kesin; token/süre yok) — M-1 raporu §C.
5. **İB adayı:** Agent-tool koşumlarında (wf_id'siz) tahmin↔gerçek OTOMATİK eşleşme anahtarı yok — bronz kosum-olay'a gorev_emri alanı gerekir; bugün bu koşumun eşleşmesi bu raporda elle.

## 6. DRFR — pipeline done-yüklemi
Kapsül kalemi "KB-02/03: ambar tahmin↔gerçek kolonları" → KARŞILANDI (amb_olgu_tahmin + sapma görünümü) · "v_kosum_tahmin_sapma" → KARŞILANDI · "v_skill_kosum" → KARŞILANDI (FAIL ekseni NULL-damgalı, kaynak alan Salih'te) · "gorev-emri-derleme alanı" → KARŞILANDI · İB-40 bindirme → KARŞILANDI (§3) · eşik kuralı taslağı → YAZILDI, imza Salih'te.
