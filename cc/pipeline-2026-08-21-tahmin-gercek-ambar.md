# Pipeline — Tahmin↔Gerçek Ambar Katmanı (Kun-Chen P-1, 2026-08-21)

**Konu:** KB-02/03 kapanış icra borcu — üst modelin alt-model koşum tahminleri (kosum_profili) ambara yapılandırılmış girer; sapma görünümle ölçülür; skill-koşum pilotu (KB-03) kendi görünümünü alır; gorev-emri-derleme'ye "skill koşucusu = alt model" alanı eklenir.
**Bindirme (İB-40, Karar 45):** aynı emir bir de MONOLİT dilim (tek ajan, bölmeden) koşulur; iki sonuç ölçüm-bankına satır (token×süre×kalite) — V1 verim tanımının ilk gerçek verisi. Bütçe ~2× bilinçli (m.35).
**Emir:** `cc/gorev-2026-08-21-1.md` · **Rejim:** maliyet-öncelikli (scout+monolit) · **Seçim gerekçesi:** kapsül "Sonraki ilk iş" 2. maddesinin Salih hükmü beklemeyen ilk kalemi; manifest kapısı tarandı (7 manifest), mükerrer koşum yok.

## Görev tablosu
| Görev | şekil | iş | intake | teslim | durum |
|---|---|---|---|---|---|
| S-1a | scout (Sonnet) | tahmin↔gerçek kayıt envanteri: künye tabloları + tahmin bantları yapılandırılmış çıkarım | emir §GİRDİLER + dilim A | `cc/rapor-2026-08-21-1a.md` | DONE 12:28 |
| S-1b | scout (Sonnet) | ambar/hat wiring: ambar-tablo.py + katman-hatti + test kalıbı + additive ekleme noktaları | emir §GİRDİLER + dilim B | `cc/rapor-2026-08-21-1b.md` | DONE 12:25 |
| S-1c | scout (Sonnet) | skill-koşum verisi: amb_olgu_prompt doluluk + prompt-tablo.py + KB-03 pilot gereksinimi + şablon alanı yeri | emir §GİRDİLER + dilim C | `cc/rapor-2026-08-21-1c.md` | DONE 12:27 |
| M-1 | monolit referans (Opus, İB-40) | AYNI emir bölmeden tek ajanda: keşif + tasarım önerisi (DDL + görünüm SQL + alan metni) | emir TAMAMI | `cc/rapor-2026-08-21-M1.md` | DONE 12:35 |
| G-1 | sentez (Carvis) | scout raporları + kanon → tasarım kararı (tahmin verisinin bronz/silver yolu, görünüm SQL'leri, alan metni) | S-1a/b/c raporları DOSYADAN | manifest olay günlüğü + SH-1 planı | DONE 12:35 |
| SH-1 | ship (Carvis) | bronz tahmin kaydı + silver yükleyici + `v_kosum_tahmin_sapma` + `v_skill_kosum` + SKILL.md alanı + test + katman-hatti koşumu | G-1 kararı | commit(ler) `[icra]` | DONE 12:41 |
| SH-2 | ship (Carvis) | ölçüm-bankı: pipeline↔monolit karşılaştırma satırları (İB-40) + bu koşumun tahmin↔gerçek kaydı ambara | M-1 raporu + amb_olgu_kosum | teslim raporu §3-4 | DONE 12:44 |
| T | teslim | teslim raporu + kapsül/pano wiring + kaptan beyanı | tüm satırlar DONE | `raporlar/seans-teslim-2026-08-21-tahmin-gercek-pipeline.md` | DONE 12:45 |

## Kosum profili (KB-02 — üst model Fable tahminleri, yalnız alt modeller; gerçekleşen koşum sonrası yanına)
| görev | model×effort | tahmin çıktı-token | tahmin araç | tahmin süre | gerçekleşen (amb_olgu_kosum, 12:39 koşumu) |
|---|---|---|---|---|---|
| S-1a | Sonnet × low | 2-4k | 8-15 | 2-4 dk | 30.433 tok (7,6× AŞTI) · 21 araç (AŞTI) · 6,1 dk (AŞTI) |
| S-1b | Sonnet × low | 2-4k | 10-18 | 2-4 dk | 16.404 tok (4,1× AŞTI) · 13 araç (BANDA) · 3,4 dk (BANDA) |
| S-1c | Sonnet × low | 2-4k | 10-18 | 2-4 dk | 25.742 tok (6,4× AŞTI) · 29 araç (AŞTI) · 5,6 dk (AŞTI) |
| M-1 | Opus × medium | 12-20k | 30-50 | 8-15 dk | 59.473 tok (3,0× AŞTI) · 42 araç (BANDA) · 13,3 dk (BANDA) |

*Sapma dersi (5. kayıt): çıktı-token tahminlerim keşif-dilimi işlerde sistematik ALTTA — "dilim küçük" varsayımı yanlış; rapor gövdesi + okuma turları çıktıyı 4-8× şişiriyor. Revizyon (İB-19 deseni): keşif-scout Sonnet ≈15-30k, monolit Opus ≈40-60k taban bandı; araç/süre tahminleri sağlam.*

## Olay günlüğü
- 12:14 Seans açılışı; borç seçimi (KB-02/03 icra + İB-40 bindirme); manifest kapısı PASS (mükerrer koşum yok); canlı-oturum eşiği tetiklenmedi (son commit 56 dk önce); çalışma ağacındaki `veri/gorunum/v_karar_borcu.csv` değişikliğine DOKUNULMUYOR (başka koşumun izi olabilir — git add yol-bazlı).
- 12:20 Emir derlendi (H=2 GEREKMEZ; SKILL TETİKLERİ: yok); Kapı-Ö tetik-denetim PASS (exit=0); manifest+emir commit `cd820eb`.
- 12:19 PARALEL OTURUM TESPİTİ: seans-11 masa hattı canlı (commit 4c65433, 12:18 — Karar 48-50: kendini-analiz kısıtı kanonlaştı + KB-46/47 icra). Dosya kesişimi yok (masa: pano/defter/ritüel; icra: tools/ambar/cc). İB-40 kalite karşılaştırması Karar 48 uyumu için deterministik done-yüklemi kontrol listesiyle yapılacak (serbest öz-analiz değil). KB-47 gereği seans hedefi: "KB-02/03 icra borcu pipeline ile kapanır, İB-40 bindirmeli."
- 12:21 S-1a/1b/1c (Sonnet) + M-1 (Opus) paralel dağıtıldı; süre ölçümü başlangıcı 12:21.
- 12:25 S-1b DONE (3,4 dk · 13 araç — tahmin bandında; token kesin değeri ambar koşumunda). Kritik bulgu: tahmin verisi için bronz kaynak YOK (atlas-derle.py tahmini yalnız rapor tablosuna yazıyor) → bronz+silver+gold zinciri sıfırdan; katman-olcum gold tarafı glob'la otomatik, silver sözleşme + testler manuel additive.
- 12:27 S-1c DONE (5,6 dk · 29 araç — İKİSİ DE tahmin üstü: araç 29>18, süre 5,6>4 dk; sapma kaydı SH-2'ye). Kilit bulgu: v_skill_kosum'un İKİ hammaddesi var — amb_olgu_prompt (sonraki_skill 28/224 dolu; %85 Fable = ana-sıra ölçümü) ↔ amb_olgu_kosum (332 gerçek alt-model koşumu; ama SKILL ADI ve FAIL kolonu YOK) — aralarında JOIN anahtarı EKSİK. Alan yeri adayları: SKILL.md satır 19 altı + skill-tetikleme-semasi 9-alan tablosu.
- 12:28 S-1a DONE (6,1 dk · 21 araç — İKİSİ DE tahmin üstü: araç 21>15, süre 6,1>4 dk; sapma SH-2'ye). Bulgular: 36 künye satırı + 3 prose bölümü çıkarıldı; 08-18 raporlarında tahmin kolonu VAR (yalnız çıktı-token); EK BULGU: rapor-2026-08-17-3 de dolu tahmin künyesi taşıyor → 4. veri noktası; granülarite: tahmin aile-BAĞIMSIZ ↔ gerçek aile-BAZLI → JOIN gold'da; bronz öneri tahmin-olay.jsonl 15 alan.
- 12:28 Scout fazı kapandı (3/3). Sonnet×low işçi tahminlerim sistematik ALTTAN sapmış (3 işçinin 2'sinde araç+süre üstten aşıldı) — SH-2'de kayda girecek. G-1 sentez başlıyor (raporlar dosyadan + V26 örneklem denetimi); M-1 hâlâ sahada, sentez girdisi DEĞİL (bağımsız referans, karşılaştırma SH-2'de).
- 12:33 V26 örneklem denetimi 3/3 TUTTU (1a künye satırı birebir · 1c doluluk 224/28/332 · 1b gold tuple satır 186). Denetim EK BULGU verdi: amb_olgu_kosum.rol SERBEST METİN ("Atlas TEZ araştırmacısı", "MASKELİ HAKEM", 58 boş) → sapma JOIN'i deterministik normalize CASE ister. 7 wf_id tam formu DB'den doğrulandı.
- 12:44 SH-2: İB-40 karşılaştırması + 5. tahmin kaydı teslim raporuna (deterministik done-yüklemi sayımı; Karar 48 uyumlu). M-1 DONE 12:35 (13,3 dk · 42 araç · 59,5k çıktı — araç/süre BANDA, çıktı 3× AŞTI). SH-1 commit c7ecb80; teslim `raporlar/seans-teslim-2026-08-21-tahmin-gercek-pipeline.md`.
- 12:35 **G-1 SENTEZ KARARI:** (1) tahmin AYRI bronz `veri/bronz/tahmin-olay.jsonl` + silver `amb_olgu_tahmin` — amb_olgu_kosum'a kolon EKLENMEZ (granülarite: tahmin (emir,rol) aile-BAĞIMSIZ ↔ gerçek aile-BAZLI; S-1a bulgusu) · (2) yükleyici ambar-tablo.py'ye ADDITIVE (hazırı temel al; katman-hatti ADIMLAR değişmez) · (3) v_kosum_tahmin_sapma: JOIN wf_id + rol_norm (deterministik CASE; V26-denetim bulgusu) + durum etiketi ALTINDA/BANDA/ÜSTÜNDE/FORMÜL · (4) v_skill_kosum: UNION ALL iki dürüst blok — 'prompt' (skill json_each split × sonraki_model × n; token/süre/FAIL NULL = veri-yok≠0) + 'kosum-vekil' (yalnız KESİN eşleme atlas→atlas-kosum; eşlenemeyen agent_type şeffaf skill=NULL satırı); kayıplı haritalama görünüme GÖMÜLMEZ (deterministik tasarım) · (5) FAIL kolonu görünümde var, bugün hep NULL — kaynak damga alanı YOK, Katman-1 önerisi teslim raporuna · (6) SKILL.md:19 altına KB-03 paragrafı (Salih Karar 17 icrası, Katman-2); core/ dosyalarına DOKUNULMAZ (Katman-1) · (7) backfill: 7 koşum (08-17×4 + 08-18×3, wf_id'ler DB-doğrulanmış) + bu koşumun 4 tahmini; elle/deterministik giriş, otomatik parse YOK (format tutarsız, S-1a) · (8) şemaya S-1a'nın 15 alanına ek tahmin_girdi_min/max (yeni-girdi bantları veri, atılmaz) · (9) test yeni dosya `tools/testler/test_tahmin_katmani.py` (discovery glob otomatik) + katman-olcum SOZLESME_TABLOLAR/TESTLER additive · (10) eşik kuralı TASLAĞI teslim raporuna (yürürlük Salih imzası). SH-1 başlıyor.
