# Graf Dilinde Konuşma — Uzun-Vade Planı v0 (2026-08-22, seans-13; pipeline `cc/pipeline-2026-08-22-pointer-graf-d2.md` P4)

*Salih emri (aynen): "böylece senle böyle konuşmamızın yanında aynı zamanda graflarla da iletişim sağlamaya başlayalım böylede llm'lerin geleceği olan graf engineeringe pratik olur … ilk çıktıdan sonraki uzun vade graf dilinde konuşma için de planlama yap". Kanıt tabanı: `cc/rapor-2026-08-22-2.md` (m.40b, 3 aile; yapı-taşları A/B/C-YTn — tümü bu dosyada pointer'lı) + yerel ölçümler (bu oturum). Statü: PLAN (deneysel m.29) — karar değil; Katman-1 kalemleri KB-60'ta. Determinizm-önceliği Karar 65 her kademeye işlenmiştir.*

## 0. Bugün ne var (G0 — teslim edildi)
- **Kaynak-of-truth değişmedi:** bronz (markdown/jsonl) → silver (`veri/baglam.sqlite`). Graf = TÜRETİLMİŞ görünüm (`core/world-model-tasarimi.md:8`: "gömme/matris türetilmiş ve KAYIPLI görünümdür"); elle çizilmez, `tools/pointer-graf.py` türetir (07-24 dersi: elle index bayatlar).
- **Dosya çifti:** `.d2` (kaynak, git-diff'lenebilir) + `.svg` (render) — d2 v0.8.1 (tag 2026-08-07; release notu yok → sürüm kaydı tag+SHA), yerleşim ELK (bundled; dagre yedek; TALA tescilli → GİRMEZ) [A-YT1/A-YT6/B-YT1]. Çıktı yalnız SVG (+ascii/txt); PNG/PDF/PPTX Chromium ister → kanona girmez [A-YT5] (bu oturum: d2 PNG asılı kaldı, doğrulandı).
- **Kademeleme:** 5 pano (genel · silver PK/FK · pointer türleri→hedefler · ilke→mekanizma · kronoloji), pano başına ≤20-50 düğüm (Ghoniem 2005: >20 düğümde matris yol-bulma dışı görevlerde üstün) [B-YT6]; 49k düğümlü tam graf .d2'ye değil sayım/CSV'ye.
- **Üç görünüm, tek kaynak:** insan = SVG panoları · LLM = `graf/pointer-sistemi-v0-kenarlar.txt` (script-üretimli kenar/incident listesi — GraphQA: kodlama biçimi 4,8-61,8 puan fark yaratır, D2 kaynağı LLM'e verilmez) [C-YT4] · sorgu = SQLite gold (`v_kirik_pointer`, `v_referans_sayim`, `v_olgu_referans`) [C-YT5].
- **Üretim kaydı + determinizm ölçümü:** `graf/pointer-sistemi-v0-uretim.json` — d2 sürümü · motor · pano sha256 · 5 pano × 5 koşum = BİREBİR (ELK; dagre n=2 BİREBİR). ELK adaptörü randomSeed set etmiyor → garanti dokümanda yok, yerel ölçüm şart [A-YT2/B-YT7/C-YT2]. Türkçe etiket render 1/1 ✓ (yerel).
- **Yorum katmanı ayrımı:** düğüm/kenar içeriği silver'dan; ilke/kronoloji = kanon SABİTİ (script içinde pointer'lı); LLM yalnız `#` yorum/tooltip katmanında — içerik yazmaz [C-YT3].

## 1. Protokol v0 — "graf dilinde konuşma" (deterministik çekirdek bölüşümü)
| Kural | İçerik | Dayanak |
|---|---|---|
| P1 Adresleme | Konuşmada düğüm/kenar adı = D2 anahtarı (ör. `silver.anahtar.replaced_by`, `pointer.dosya_pointer`, `ilke.m20`); pano adı önek (`genel.` · `silver.` · `pointer.` · `ilke.` · `kronoloji.`). Kimlikler script'ten gelir, sabittir. | A-YT3, C-YT4 |
| P2 Soru yönlendirme | Yapısal soru (kaç kenar · kırık pointer · erişilebilir mi · hangi dosyalar) → SQL/gold görünüm, LLM sorguyu yazar, motor yürütür, LLM yorumlar; anlam/tasarım sorusu → pano + kenar listesi referansıyla cevap. LLM grafı "kafadan çözmez" (GraphQA: yapıya göre %5,9-91,7 oynar). | C-YT5 |
| P3 Değişiklik | Graf elle düzenlenmez; değişiklik = kanon/silver değişikliği → `pointer-graf.py --render 2` yeniden türetir; kanon-sabiti (ilke/kronoloji) değişirse script sabiti + kaynak pointer güncellenir (ayrı commit). | 07-24, C-YT3 |
| P4 Üretim kaydı | Her türetimde uretim.json: d2 sürümü · motor · sha256 · n-koşum eşitliği; d2 yükseltme = ayrı commit + yeniden ölçüm (sürümler-arası eşitlik beklenmez; master'da dagro v0.2.0 yerleşim kayması). | A-YT2 |
| P5 Görünüm sınırı | Kanon graf dosyası = .d2 + .svg; Mermaid (GitHub/Artifact yerleşik render) ve DOT (büyük graf) yalnız script-türetimli İKİNCİL görünüm, kaynak değil; JSON Canvas girmez. | A-YT7/A-YT8, C-YT7/C-YT8 |
| P6 Ölçüm | Birincil metrikler deterministik: d2 derleme çıkış kodu · üretilen .d2'den parse edilen düğüm/kenar kümesi ↔ model JSON simetrik fark = 0 · render sha eşitliği · token/süre; LLM-hakem yalnız A/B tercihinde (mutlak puan yok). | C-YT6 |

## 2. Kademeler (kronolojik partisyonlar; kapı = kanıt akışı, takvim yok)
| Kademe | DURUM giriş → çıkış | Kapı (dış sinyal) | İş | Katman |
|---|---|---|---|---|
| **G0** (bugün) | şema-düzeyi 5 pano + kenar listesi + üretim kaydı | Salih teyidi/düzeltmesi (P3 kapısı) | — | K2 icra (yapıldı) |
| **G1 örnek-düzeyi + otomasyon** | yalnız şema → bir kaydın/kararın çevresi (1-2 sıçrama) panosu (`--odak <kayit_id ∨ KB-n>`), kırık-pointer panosu (`v_kirik_pointer` 1.107), türetim `tools/katman-hatti.py`'ye adım (her hat koşumunda graf yenilenir, bayatlama 0) | script testleri PASS + 2-koşum sha BİREBİR + hat koşumu yeşil | script genişletme; ölçek: odak panosu ≤50 düğüm | K2 icra (İB adayı) |
| **G2 tipli-bağ katmanı** | tipsiz/FK kenar → tipli kenar enum: süpersede = `prov:wasRevisionOf`, destek/itiraz = CiTO (`supports/disputes/extends/updates…`), türetme = OpenLineage kavramları (Job=script, Dataset=tablo/dosya, sourceCode facet); bitemporal alanlar anahtar kaydına (created_at + valid/invalid/expired, Graphiti şeması; LLM-inşa hattı girmez); tip ataması KURAL-tabanlı (anahtar.durum/replaced_by/bağ alanı), LLM atamaz | 07-18 Model A açık soruları Salih kararı (bağ tipli mi · enum · bitemporal alan) — **Katman-1** | şema + silver additive kolon + script | K1 karar (KB-60) |
| **G3 graf-iletişim eval'i** | ölçüm yok → D2 mini-eval: (a) LLM'in .d2 üretme/okuma doğruluğu (derleme kodu + küme eşitliği), (b) kenar-listesi ↔ SQL aynı soru kıyası, (c) token/süre; N≥5 koşum; LLM-hakem yalnız A/B | eval dosyası + sonuç tablosu | Jarvis'e özgü; literatürde D2 benchmark yok (yalnız Mermaid/UML) | K2 icra (İB adayı) |
| **G4 kompozisyon + ikincil görünümler** | ayrı dosyalar → D2 `layers/scenarios/steps` tek-dosya (kronoloji = steps; drill-down `link`), Mermaid erDiagram script-türetimli (Artifact/GitHub), DOT yedek (≥100 düğüm) — hepsi ölçümle | G1 + G3 sonuçları | d2 sürüm kayması izlenir | K2 icra |
| **G5 geri-besleme döngüsü** | graf gösterir → kanon düzelir: kırık pointer onarım akışı (1.107 → 0 hedefi), süpersede zinciri denetimi, graf-yetim dosya oranı (07-24'te %92,5) yeniden ölçümü | ölçüm satırları `veri/` | "etiketi alma, pratiği al" | K2 icra / fikir-kutusu |

## 3. Determinizm şartnamesi (tüm kademeler)
Aynı silver → aynı model JSON (sıralı) → aynı .d2 (bytewise sıralama, locale-bağımsız) → aynı SVG (aynı d2 sürümü + motor; N≥2 sha eşitliği kaydı) · LLM içerik yazmaz · TALA/SaaS render/LLM-graf GİRMEZ · rastgele tohum kullanılmaz · sürüm yükseltmesi = bilinçli commit + yeniden ölçüm [Karar 65; A-YT2/A-YT6; C-YT1-3].

## 4. Riskler (kaynaklı)
Bayatlama (türetim hat'a bağlanana dek elle tetik — 07-24 dersi) · d2 sürüm kayması (0.8.x changelog yok; dagro v0.2.0 master) · okunurluk eşiği (Ghoniem verisi rastgele graflar; ER/D2 için ölçüm yok → pano başına ≤50 düğüm kural, deneysel) · LLM içerik sızması (yorum katmanına sınır) · ELK seed (ölçümle kapatıldı, garanti yok) · Mermaid/GitHub render sürümü pinlenemez (ikincil görünüm) · bakım: her yeni tablo/referans türü script sabitlerine dokunur (REF_HEDEF/FK — test gerekir).

## 5. Karar masası kalemi (KB-60, ÖNERİ-damgalı; hüküm Salih)
**(a) ÖNERİLEN — Protokol v0 + G1/G3 icra-borcu olarak açılır; G2 tipli-bağ Katman-1 masası ayrı kalem:** ne → P1-P6 kuralları KILAVUZ'a pointer, `pointer-graf.py` katman-hatti adımı (G1), D2 mini-eval (G3) İB kalemleri; artı → bugünkü deterministik yığın üstüne, karar gerektirmeyen işler hemen; eksi → G2 (07-18 açık soruları) beklemeye devam. **(b) G2 hemen (tipli-bağ enum + bitemporal alanlar şimdi):** artı → typed-link grafı tek seferde; eksi → silver şema kararı + 07-18 soruları masa görmeden. **(c) G0'da dur:** artı → sıfır bedel; eksi → bayatlama + graf-dili pratiği ölçümsüz kalır.

*Cevaplanmamış sorular (m.41):* okunur düğüm eşiği D2/ELK için ölçüsüz · LLM-D2 üretim doğruluğu (frontier modellerde) ölçüsüz · ELK randomSeed varsayılanı kaynakla doğrulanmadı (yerel sha ölçümü kapatıyor) · Türkçe collation/sıralama (script bytewise — yeterli mi) · 49k düğüm DOT/sfdp süresi ölçülmedi.
