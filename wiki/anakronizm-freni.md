# Anakronizm freni — zaman-bağımlı iddia AS-OF damgasız çıkmaz (Karar 68)

**Tanım:** Anakronizm = zaman-bağımlı bir iddianın (sürüm · SDK/ürün durumu · benchmark skoru · fiyat · "en güçlü model" · kanon kaydı · "artık yok/var") geçerli olduğu ZAMAN belirtilmeden ya da yanlış zamana aitken bugünün durumu gibi sunulması. Salih Katman-1 hükmü (2026-08-26, aynen): "bundan sonra sistemde anakronizm yapmayı yasaklıyorum". Üç kanal: **ESKİ KAYIT** (kanon/rapor tarihli ama tarihsiz aktarılır) · **MODEL HAFIZASI** (eğitim kesimi; beyan edilen kesim ≠ fiilî kesim) · **KONUŞMA** (chat cevabında damgasız sayı/durum). Önleme MEKANİKTİR (Karar 65): damga kuralı + kesim tablosu + canlı-çekim tetiği + deterministik lint + bayatlık kuyruğu; "modele dikkat et" mekanizma değildir.
**Durum:** GÜNCEL · **son teyit:** 2026-08-26 (seans-16) · **kaynaklar:** `cc/rapor-2026-08-26-2.md` (m.40b wf_9030bba4, 3 aile × 12 işçi; hayatta-kalma 1/29/1/0 — as-of kuralı hakemleri daralttı; V26 46/4/7) · `veri/model-kesim.jsonl` (satıcı tablosu, V26 ✓ 2026-08-26) · `tools/anakronizm-denetim.py` · **güven:** orta — mekanizma emsalleri D (Wikipedia/Microsoft/Google/RFC 9111/dbt/Wikidata/PROV), Jarvis ölçeğinde etkisi ÖLÇÜLMEDİ (kör nokta); Türkçe kalıp listesi kaynaksız, deneysel m.29.

## Çekirdek

**Kanonik örnek (08-26, üç vaka tek zincirde):** 07-30 raporu "Rust'ın resmî SDK'sı yok" [31 Temmuz 2026 itibarıyla doğru] → 08-26'da damgasız "Rust hiçbir sınıfta" diye taşındı (ESKİ KAYIT) → yeniden çekilince MCP'de Tier-1 çıktı. Aynı gün Carvis 2025-04 tarihli Multi-SWE-bench sayısını "Go'da düşük" diye tarihsiz söyledi (KONUŞMA) ve eğitim-hafızasından SWE-bench skoru anlattı (MODEL HAFIZASI). Tek düzeltme her üçünü kapatır: **iddia + AS-OF + kaynak tarihi**, ve zaman-bağımlı sınıfta cevaptan ÖNCE canlı çekim.

**Mekanizma seti (ÖNERİ; kanon statüsü KB-66):**

| # | Mekanizma | Kural | Emsal (AS-OF) | Jarvis'te |
|---|---|---|---|---|
| M1 | **Damga kuralı** | zaman-bağımlı her iddia `AS-OF YYYY-MM-DD` (çekim) ∨ kaynak tarihi taşır; CHAT dahil ("(2025-04 ölçümü)", "(çekim 2026-08-26)") | Wikipedia `{{As of}}` + gizli bakım kategorisi (~93k sayfa; kural: now/currently/recently yasak) · Microsoft Learn zorunlu `ms.date` (derleme hatası) — çekim 2026-08-26 | wiki/rapor üst bloğu "son teyit" + rapor "Kayıt:" satırı; chat damgası YENİ |
| M2 | **Kesim tablosu** | model hafızasından gelen iddia = "AS-OF ≤ kesim, doğrulanmadı" damgası; kesim model-başına satıcı tablosundan okunur, beyana güvenilmez (açık modellerde fiilî kesim beyanın ~4 yıl gerisinde ölçüldü — Cheng vd. 2024-09) | Anthropic sistem promptu `{{currentDateTime}}` + `<knowledge_cutoff>` bloğu (Opus 5, 2026-07-24); models/overview tablosu (çekim 2026-08-26): Fable 5 Jan/Jan 2026 · Opus 5 May/May 2026 · Sonnet 5 Jan/Jan 2026 · Haiku 4.5 Feb 2025/Jul 2025 | `veri/model-kesim.jsonl` + SessionStart brifinde ZAMAN-ZEMİNİ satırı (bugün sistem saatinden) |
| M3 | **Canlı-çekim tetiği** | zaman-bağımlı sınıfa düşen iddia (sürüm/skor/durum/fiyat) cevaptan ÖNCE canlı kaynaktan çekilir, kanıtın tarihi prompta/cevaba yazılır; bayat kayıt yeniden doğrulanmadan KULLANILAMAZ (must-revalidate) | FreshQA/FreshPrompt: hızlı-değişen olguda çıplak GPT-4 %12,0 → tarih-damgalı kanıtla %75,6 (ölçüm 2023-04, v2 2023-11) · RFC 9111 tazelik aritmetiği (2022-06) | hakem "sürümü yeniden çek" kuralı (08-22) → tüm zaman-bağımlı sınıfa genelleşir |
| M4 | **Kayıt şeması** | zaman-bağımlı kayıt `gecerli_bas/gecerli_bitis` (olay-zamanı) + `cekim_tarihi` (erişim) + `kaynak_tarihi` (yayın); as-of(t) = bas ≤ t ∧ (bitis boş ∨ bitis > t); anahtar başına bas UNIQUE | Wikidata P580/P582/P585 + P813 (retrieved) + P577 (published) · PROV generatedAtTime/invalidatedAtTime (2013) · SQL Server `FOR SYSTEM_TIME AS OF` yüklemi · SQLite pencere fonksiyonu (3.25+) | anahtar kaydı SCD-2 + ambar bitemporal VAR; `cekim_tarihi` alanı eksik |
| M5 | **Deterministik lint** | D1: tarihsiz paragrafta sürüm/skor = İHLAL, zaman-çivi sözcüğü (şu an/artık/henüz/en güncel/en güçlü/yakında…) = UYARI · D2: dosya ilk 12 satırda tarih yoksa İHLAL · D3: en yeni damga > eşik → BAYAT-ADAY kuyruğu | Vale `conditional` ("kalıp varsa aynı kapsamda tarih") v3.18.0 (2026-08-20) · Google timeless-documentation 12-grup yasak listesi (2024-10-15) · actions/stale 60+7 gün (v11.0.0, 2026-07-28) | `tools/anakronizm-denetim.py` (stdlib; Vale +1 zincir → KB-67) |
| M6 | **Bayatlık kuyruğu + boşaltma** | D3 kuyruğu `v_bayat_aday`; seans kapanışında N kayıt yeniden-çekim; SİLME yok (m.8), damga tazelenir ya da yeni sürüm satırı | Wikipedia 2010 alt-kategorisinde hâlâ 3.126 açık sayfa (çekim 2026-08-26) → boşaltma politikası olmadan damga = kalıcı borç | boşaltma politikası KB-68 |
| M7 | **Tazelik sınıfı** | iddia {zaman-bağımsız \| zaman-bağımlı}; sabit "sınıf→gün" tablosu YOK (bayatlama görevler arası ~30× yayılır; Luu vd. 2022) → `cekim_tarihi` + yeniden-çekim tetiği; eşik günleri kestirim [?] | FreshQA never/slow/fast (2023-11); Luu TD 0,26…7,72 F1/yıl (2022) | eşik 90 gün varsayılan (KB-67) |

**Türkçe zaman-çivi sözcükleri (deneysel; kaynak yok, Google listesinin çevirisi):** şu an(da) · şimdilik · hâlâ · artık · henüz · yakında · son zamanlarda · en güncel · en güçlü · en son sürüm · en yeni · bugün itibarıyla · yeni/eski sürüm · desteklenmiyor · "resmî SDK'sı yok" · henüz yok. Kullanılacaksa yanına tarih/sürüm konur ("2026-08-26 itibarıyla", "v1.7.0'da").

## SOP — "bir sayı/durum söyleyeceğim"
1. İddia zaman-bağımlı mı? (sürüm · skor · fiyat · var/yok · "en …") Değilse damga gerekmez.
2. Kaynağım ne? **Kanon kaydı** → kaydın tarihini yaz, 90 günü geçtiyse yeniden çek. **Model hafızası** → "AS-OF ≤ kesim (Fable 5: 2026-01), doğrulanmadı" damgala ya da canlı çek. **Canlı çekim** → çekim tarihi + kaynağın kendi tarihi (leaderboard "last updated" gibi) — ikisi de yazılır.
3. Cevaba damgayı koy: "Go %7,5 (Multi-SWE-bench, 2025-04; çekim 2026-08-26)".
4. Dosyaya yazıyorsan `python3 tools/anakronizm-denetim.py --dosya <yol>` → İHLAL 0 olmadan commit etme (uyarılar sayılır, engellemez).
5. Seans kapanışında `v_bayat_aday` kuyruğundan N kaydı yeniden çek (KB-68 politikası gelene dek N=3 öneri).

## Gotchas
- **"Bilmiyorum" ≠ "yok":** S-0 ajanı "Claude Mythos Preview bilinen ad değil" yazdı — kendi kesiminden hüküm. Yokluk iddiası zaman-bağımlı sınıfta ancak canlı kaynakla kurulur.
- **Leaderboard da bayatlar:** Aider sayfası "last updated 2025-11-20" — "güncel liderlik tablosu" bile tarihsiz okunursa anakronizm.
- **Beyan ≠ fiilî kesim:** satıcı "reliable" ve "training" kesimi ayrı verir (Haiku 4.5: Feb 2025 / Jul 2025); kanona tek sayı yazılmaz, model-başına satır.
- **Damga doğruluk DEĞİLDİR:** `ms.date`/`#[deprecated(since)]` biçimi denetler, içeriği değil; lint D1/D2 de öyle — canlı çekim ayrı adım.
- **Kuyruk boşaltılmazsa damga borçtur** (Wikipedia 16 yıllık kategori).
- **Lint yanlış-pozitif:** ilk kalıp seti 201 dosyada 1.665 vuruş verdi ("Katman-1", çıplak %); kalibre edildi; oran ölçülmeden eşik sertleştirilmez.

## Süpersede zinciri
- seans-acilis §0 "zaman-kayması freni" (08-15: selamlama ≠ zaman işareti) → **genişledi [2026-08-26]:** her zaman-bağımlı iddia için damga + kesim tablosu; §0 aynen kalır.
- halüsinasyon paketi v2 "tazelik" bayrağı (+1) → **tamamlandı [2026-08-26]:** bayrak derecelendirir, bu sayfa mekanizmayı verir.
- `cc/gorev-2026-08-26-2.md` KANON bloğu "Carvis kesimi Ocak 2026" → **düzeltildi [2026-08-26]:** doğru ama modelsizdi; model-başına tablo `veri/model-kesim.jsonl`.

## Bağlantılar
[[dil-secimi]] (tetikleyen vaka) · [[silver-saglik]] (bayatlık adayları T-B) · [[adversarial-hayatta-kalma]] · [[olcum-banki]] (m.39 rakam damgası) · [[paralel-oturum-protokolu]] · [[baglam-veri-ambari]] (bitemporal) · [[pointer-sistemi]] (adres + tarih) · [[stokastik-dusunce]] (Karar 65)

**Bağlantılar:** · [[baglam-anahtar-kaydi]] (karşı-link 08-29)
