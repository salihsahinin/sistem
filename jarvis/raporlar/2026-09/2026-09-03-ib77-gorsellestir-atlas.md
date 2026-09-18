# İB-77 SENTEZ — "görselleştir" komutu: literatür-tabanlı görsel seçimi, araç zinciri, LLM'siz doğrulama kapısı, skill tasarımı v0

**Künye.** Derleyen: Carvis (Fable 5.1, ana-sıra) · 2026-09-03 · AS-OF 2026-09-03 · Emir `cc/gorev-2026-09-03-ib77-gorsellestir-atlas.md` · Zincir (m.40b v0.2, Karar 85/86 rejimi — tüm işçiler Sonnet): tez A/B/C (`cc/rapor-2026-09-03-ib77-gorsel-{A,B,C}.md`) → antitez A/B (CoVe, yalnız iddia listesi) → V26 (`…-v26.md`: 11 iddia, 9 açılma, 0 ihlal, 2 KISMİ, %86) → maskeli hakem (`…-hakem.md`, sentezden AYRI ajan — Karar 86 D3-i; maskeleme sızıntısı beyanlı K2-k). **Hakem sayımı: 25 iddia → D 14 (%56) · K 7 (%28) · X 4 (%16); SAĞLAM 6 (%24) · DARALDI 15 (%60) · DÜŞTÜ 4 (%16).** Fiilen açılan birincil kaynak: A 4 + B 4 + antitez 5 + V26 9 = 22. Fable ölçümleri: `d2` v0.8.1 ve `dot` 15.1.1 aynı girdi → bayt-bayt aynı SVG; d2 SVG font gömülü/self-contained; `jsonschema` paketi yok; skill description bütçesi 8.861/7.380 char (`tools/skill-butce.py`).

## 1. Hayatta kalan çekirdek (adversarial'dan sağlam çıkanlar)
- **Sayısal içerik için görsel-tür seçimi** kaynaklı ve sağlam: data-to-viz karar ağacı (6 dal: numeric · categoric · num+cat · maps · network · time series — "5" DÜŞTÜ) [D] · FT Visual Vocabulary 9 kategori [D] · Cleveland–McGill algısal sıralama (pozisyon > uzunluk > açı > alan > renk; ratio-estimation görevlerinde, Heer & Bostock replikasyonuyla) [DARALDI, D].
- **Kavram haritası:** Novak/Ausubel — en genel kavram üstte, etiketli önerme okları [D]; öğrenme etkisi var ama heterojen büyüklük [DARALDI].
- **Munzner 4 katman** (domain → abstraction → idiom → algorithm) [D] — skill'in adım yapısı bu katmanları izler: içerik sınıfı (abstraction) → görsel türü (idiom) → araç/render (algorithm).
- **Araçlar:** Mermaid 11.x CDN-ESM tek-dosya gömme [D] · Vega-Lite 6.x JSON grammar + resmi şema URL'i (şema URL'i tek başına doğrulama SAĞLAMAZ — DARALDI) [D] · `vl-convert` CLI mevcut [D, kurulu değil] · LIDA 4 modül [D] · VisEval 3 eksen (geçerlilik/uygunluk/okunabilirlik) [D].
- **Lie factor** boyut-orantısı çarpıtmasını yakalar; "0,95–1,05" aralığı raporun eklemesiydi (V26 KISMİ) — skill'de kural olarak yalnız "bar/area eksen sıfırdan başlar" (deterministik) yazılır.

## 2. Düşen / kural olamayan (kullanılamaz kanıt)
1. "Düşük data-ink = chart junk" NORM DEĞİL — Bateman 2010: süsleme anlamayı bozmuyor, 2-3 hafta sonra hatırlamayı artırıyor → skill: **süs yok** kararı öğrenme-hatırlama görevinde ZORUNLU değil, varsayılan sade ama "hatırlatıcı görsel" isteği izinli.
2. Spatial contiguity "~1,10" YOK — Ginns 2006 d=0,85 (üst sınır 1,02); temporal 1,30 ile karıştırılmış. Skill kural metnine efekt büyüklüğü YAZILMAZ (m.39), yalnız yön.
3. Mayer coherence/signaling/contiguity: YÖN sağlam, BÜYÜKLÜK tartışmalı (2025 meta-analizleri küçük/çelişkili) → kural olarak "uygula", rakam olarak "yazma".
4. Worked-example: yalnız ACEMİ öğrenicide (expertise-reversal) → skill, "ilk kez öğrenilen konu" işaretinde önce çözülmüş örnek görseli önerir; ileri düzeyde önermez.
5. **"Metin türü → diyagram türü" için normatif literatür kaynağı YOK** (T1 = X; en yakın: Tversky — oklu diyagram = işlevsel/nedensel, oksuz = yapısal). Karar tablosunun metin satırları **DENEYSEL (m.29)** damgalıdır; Munzner görev-soyutlamasından türetilmiştir; kalibrasyon = koşum kütüğü + Salih'in "doğru görsel mi" beyanı.
6. ChartMimic hata sınıfları 4'tür (kod/metin/tip/renk); "GPT-4o lider" 2024 anlık görüntüsü (Direct 82,2 / Customized 61,6).

## 3. KARAR TABLOSU v0 — içerik sınıfı → görsel tür → araç (tipli; `icerik_sinifi` enum = tools/gorsellestir.py ile aynı)
| `icerik_sinifi` | Ne zaman (yüklem) | Birincil tür | Araç (öncelik) | Damga |
|---|---|---|---|---|
| `surec` | adımlar sıralı ∧ dallanma olabilir | akış diyagramı (oklu = işlevsel, Tversky) | d2 (elk) → Mermaid flowchart | DENEYSEL (T1) |
| `kavram-iliskisi` | ≥3 kavram ∧ etiketlenebilir ilişki | concept map (genel üstte, etiketli ok) | d2 → dot | D (Novak) + DENEYSEL eşleme |
| `karsilastirma` | ≥2 şey × ≥2 özellik, nitel | tablo/matris | HTML tablo | DENEYSEL |
| `hiyerarsi` | ağaç ilişkisi, oksuz = yapısal | ağaç | dot (rankdir=TB) → Mermaid mindmap | DENEYSEL |
| `zaman-akisi` | olaylar tarihli/sıralı, sayısal değil | timeline | Mermaid timeline | DENEYSEL |
| `mekanizma` | "nasıl çalışır", parçalar+bağlantı | etiketli şema | d2 | DENEYSEL |
| `sayisal-dagilim` | tek sayısal değişken | histogram / kutu | Vega-Lite | D (data-to-viz) |
| `sayisal-iliski` | 2 sayısal değişken | scatter | Vega-Lite | D |
| `zaman-serisi` | sayısal × zaman | çizgi | Vega-Lite | D |
| `sayisal-karsilastirma` | kategori × sayı | çubuk (uzunluk/pozisyon kodlaması) | Vega-Lite bar (eksen 0'dan) | D (C-M, FT) |
| `parca-butun` | paylar toplamı = bütün | treemap / yığılmış çubuk (pasta değil — açı kodlaması zayıf) | Vega-Lite | D (C-M) |
| `akis-miktari` | kaynak→hedef miktar | sankey | Mermaid sankey-beta | D (data-to-viz) |
| belirsiz / birden fazla | — | TEK soru ∨ bölüm başına ayrı görsel | — | m.4 |

Araç önceliği gerekçesi: d2/dot **çevrimdışı + kurulu + deterministik (ölçüldü) + SVG gömülü** → varsayılan; Mermaid/Vega-Lite CDN (çevrimiçi render; tarayıcısız doğrulama YOK → yalnız yapısal kapı) → d2/dot'un vermediği türlerde. `vl-convert` (pip) kurulursa Vega-Lite de çevrimdışı/deterministik olur — Salih beyanı.

## 4. Öğrenme kuralları (skill'e giren; yön kuralları, rakamsız)
K1 coherence: süs/alakasız öğe yok (varsayılan; hatırlama-görevinde gevşetilebilir — Bateman) · K2 signaling: ana kavram/adım vurgulu · K3 spatial contiguity: açıklama görselin YANINDA (grid), ayrı sayfada değil · K4 segmenting: >12 düğüm/adım → böl, iki görsel · K5 concept map hiyerarşik, oklar etiketli · K6 worked-example: yalnız "ilk kez" konularda önce örnek · K7 sayısal: eksen 0'dan (bar/area), renk-körü-güvenli palet (Okabe–Ito), pasta yerine çubuk · K8 her görsel kaynak partisyonuna pointer taşır (anakronizm/hesap verebilirlik).

## 5. Doğrulama kapısı (LLM'siz, `tools/gorsellestir.py --dogrula`)
Şema (zorunlu alanlar + enum) · araç-özel (d2/dot render exit 0; Mermaid tür satırı; Vega-Lite mark/encoding/data + bar-area zero + palet; tablo satır uzunlukları) · HTML (5 zorunlu blok, <2 MB, dış URL yalnız cdn.jsdelivr.net) · determinizm (aynı spec → aynı bayt; script saat okumaz). Sınır beyanı: Mermaid/Vega-Lite tarayıcısız render doğrulanamaz — T2 koşulu ("model-bağımlı geçerlilik") kapıyı zorunlu kılar; Sonnet/Fable spec üretir, kapı düşerse spec yeniden yazılır (≤2 tur), sonra HATA damgalı teslim.

## 6. Skill tasarımı v0 — `gorsellestir` (T-Ü üretici; 9-alanlı çağrı)
skill: gorsellestir · tetik_kosulu: Salih "görselleştir"/eş kalıplar (evals should_trigger) · cagri_kipi: kullanıcı-tetikli (model önerebilir, kendiliğinden koşmaz) · girdi: hedef partisyon (son cevap ∨ belirtilen bölüm) · baglam: cwd (jarvis ↔ yan-oturum) · yan_etki_damgasi: yok (raporlar/·gorsel/ yazımı, jarvis içinde bronz kütük; kanon/commit yok) · done_yuklemi: HTML üretildi ∧ kapı PASS ∧ yol+open teslim edildi · hata_yolu: kapı FAIL ≤2 yeniden-spec, sonra HATA damgalı teslim; sınıf belirsiz → tek soru · sira: tekil. Yan-oturum: `~/.claude/skills/gorsellestir` symlink; script mutlak yol.

## 7. skill-kapisi hükmü (K0–K3)
K0 GEREK: hazine taraması — lavish (review yüzeyi), dataviz/artifact-design/diagramming (harness rehberleri, Türkçe "görselleştir"le tetiklenmez, üretici+kapı değil), pointer-graf (yalnız graf/) → KISMÎ kapsama, yaprak YENİ; Y2 (kanon-LAZY kural tablosu) ∧ Y3 (≥3 sabit adım) ✓. K1 DEĞER: Z2 Salih Katman-1 emri ✓ (bütçe atlanır). İNŞA: evals.json ✓ (5 test, 8/7 tetik). K2: R → `kapi-denetim.py` koşumu (ship sonrası) · İ → bu sentezin sayısal iddiaları hakemli (25 iddia zinciri) · ¬P → kapı script'tir ✓. K3: şekil T-Ü (kanon yazmaz, commit yapmaz; bronz kütük append = ölçüm, yan-etki değil) · F1 description ≤1024 ✓ ama **Σ_H = 8.861 > 7.380 → F1e AŞIM (yeni skill'den bağımsız, zaten aşımda)** → ONAR-3 kalemi Salih'e: bütçe kapsamı (proje ∨ kullanıcı ∨ plugin listesi) yeniden kalibre + 4 uzun description kısaltma (≥1.781 char). **Hüküm: GEÇTİ-ŞARTLI** — F1e Salih kalemi; kalan kapılar ship sonrası script'le.

## 8. Ölçüm + kalibrasyon (m.29)
`veri/bronz/gorsel-olay.jsonl` (jarvis içi koşumlar): sınıf · tür · araç · kapı sonucu · yeniden-spec sayısı. 10 koşumda: sınıf dağılımı, kapı FAIL oranı, Salih "doğru görsel mi" 0/1 beyanı (gönüllü, m.33) → karar tablosunun DENEYSEL satırları D/K'ya terfi eder ya da düzelir. Yan-oturum koşumları kütüksüz (staj geçici-hafıza kuralı) — Salih isterse çıktı dosyası jarvis'e devir notuyla taşınır.

## 9. Salih'e açık kalemler
1. Description bütçesi: kapsam kalibrasyonu + hangi 4 description kısalır (F1e).
2. `pip install vl-convert-python` (Vega-Lite çevrimdışı/deterministik render) — paket kurulumu beyanı.
3. Mermaid/Vega-Lite CDN bağımlılığı (çevrimdışı açılmaz) kabul mü, yoksa yalnız d2/dot/tablo ile mi kalınsın?
4. Karar tablosunun metin satırları DENEYSEL — 10 koşum kalibrasyonu için "doğru mu" beyanı verecek misin (gönüllü)?
