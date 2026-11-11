# md → Lean 4 envanteri (Karar 114 taşıma adayları)

AS-OF 2026-10-16 · yalnız okuma, tek rapor dosyası · yöntem: bölüm başlıkları + satır uzunlukları + kural işaretleri (eşik, boolean koşul, if-then, tablo, yasak) okundu; çevrilebilir bayt payları **okuma tabanlı kestirimdir `[?]`**, ölçüm değildir (±%30 [?]).

Ölçüt kalıbı (okunan üç modül): `Kanon.SkillKapi` (kapı ağacı + first-hit şekil + `Hukum`), `Kanon.SkillTetik` (boolean kapılar + yasak listesi + sayısal alan sınırları), `Gorev.Sablon` (Girdi structure, Dal inductive, karar first-hit, done, 3 theorem). Gerekçe, tarihçe, atıf, rakam kaynağı, anlatı md'de kalır; Lean başlığında Türkçe özet + md pointer'ı durur.

## 1. Özet tablo

Bayt = `wc -c` (ölçüm). Çevrilebilir bayt `[?]`. Modül sayısı = önerilen ayrı `Kanon.X` dosyası (aynı modülü paylaşan dosyalar tek sayılır, bkz. §2).

| Dosya | Toplam bayt | Çevrilebilir bayt `[?]` | Pay `[?]` | Modül | Öncelik |
|---|---:|---:|---:|---:|---|
| core/tuzuk-v0.md (m.1-47) | 61679 | 21000 | %34 | 12 | Yüksek |
| core/ajan-metodolojisi.md | 17655 | 5500 | %31 | 3 | Orta |
| core/baglam-anahtar-kaydi.md | 34500 | 4500 | %13 (JSON kayıt veridir) | 2 | Orta |
| core/halusinasyon-paketi.md | 13169 | 5500 | %42 | 2 | Yüksek |
| core/ingest-semasi.md | 6951 | 4200 | %60 | 2 | Yüksek |
| core/sema-sikistirma.md | 8649 | 3600 | %42 | 1 | Orta |
| core/veri-muhendisligi-katmani.md | 15537 | 2800 | %18 | 2 | Düşük |
| core/world-model-tasarimi.md | 11819 | 1500 | %13 | 1 | Düşük |
| core/skill-uretim-semasi.md (§1-2 taşındı; kalan) | 23930 | 3500 | %15 | 2 | Orta |
| core/skill-tetikleme-semasi.md (§2-4 taşındı; kalan) | 10516 | 400 | %4 | 0 (SkillTetik'e ek) | Düşük |
| core/deterministik-tasarim.md | 2362 | 800 | %34 | 1 | Düşük |
| core/varlik-felsefesi.md | 5206 | 300 | %6 | 0 | Yok |
| core/durum-kapsulu.md · core/pano.md | 2552 · 10337 | 0 | %0 (durum kaydı) | 0 | Yok |
| AGENTS.md (kök) | 6265 | 3000 | %48 | 4 | Yüksek |
| jarvis/AGENTS.md | 7167 | 1600 | %22 | 2 | Orta |
| jarvis/.claude/skills/*/SKILL.md (19 dosya) | 106025 | 19200 | %18 | 9 | Orta |
| jarvis/.claude/rules/*.md (3 dosya) | 3670 | 600 | %16 | 1 | Düşük |
| jarvis/wiki/paralel-oturum-protokolu.md | 10130 | 3500 | %35 | 2 | Yüksek |
| 8 ajan AGENTS.md (friday tart gard span calc deci vega sage) | 31986 | 7200 | %23 | 1 (ortak şablon) | Orta |
| **Toplam (kapsam)** | **~390000** (jarvis/AGENTS.md bir kez) | **~88700** | **~%23** | **~47** | |

Not: modül sayısı toplamı farklı dosyaların aynı modülde birleşmesiyle (örn. ingest, anahtar emeklilik, karar zinciri) ~35 benzersiz modüle iner `[?]`.

Gözlem 1: ağırlık tüzükte (21 KB) ve skill gövdelerinde (19 KB); fakat **sık yüklenen** dosyalar (kök AGENTS, jarvis/AGENTS, alan AGENTS, protokol) küçük ve çevrilebilir payı yüksek, kod karşılığı hazır.
Gözlem 2: **Kural-kod sapması bulundu.** tüzük m.46(d) "PreToolUse sayaç uyarı 36 / durdur 72" der; `kod/hook/src/ajan_fren.rs` varsayılanı uyarı 72 / durdur 144 (env `JARVIS_FREN_UYARI`/`JARVIS_FREN_DURDUR` ile değişir). Lean modülü yazılırken tek doğru sayı seçilmeli (Salih kararı gerekebilir; bkz. §4).

## 2. core/tuzuk-v0.md, madde (m.NN) düzeyi

Satır numaraları dosya satırı; "bayt" madde satırının uzunluğu (`awk length`, ±UTF-8). m.1-47 var, m.48-49 bu dosyada yok (`md.49` kök AGENTS.md'de ve başka dosyalarda atıf olarak geçer). Kod sütunu: o kuralı bugün uygulayan (varsa) tool/hook.

| m. | Satır | Bayt | Çevrilebilir bayt `[?]` | İçerik türü | Modül | Mevcut kod | Zorluk · gerekçe |
|---|---|---:|---:|---|---|---|---|
| 1 | 13 | 161 | 120 | yasak (klavyede başkası şüphesi → kalıcı değişiklik yok) | Kanon.Yetki | yok | kolay · tek boolean koşul |
| 2 | 14 | 220 | 80 | yasak (kimse Salih'e rol atayamaz) | Kanon.Yetki | yok | kolay · kimlik/yetki matrisi |
| 3 | 15 | 181 | 100 | yasak (sözlük DONDU; değişiklik yalnız Salih ∧ gerekçe ∧ geri-açma) | Kanon.Yasaklar | yok | kolay · tek koşul |
| 4 | 16 | 165 | 130 | eşik (girdi sonucu değiştirir mi → sor, değilse yap+kaydet) | Kanon.Yetki | yok | kolay · if-then |
| 5 | 17 | 322 | 150 | dal (sorun-güdümlü; geç-tespiti-pahalı sınıf istisna) | Kanon.Yetki | yok | kolay · sınıf listesi sonlu |
| 6 | 18 | 129 | 0 | üslup tavsiyesi | yok | `stop-buyuk-harf` kısmen | çevrilemez · tespit LLM |
| 7 | 19 | 340 | 100 | yasak (övgü-merci) + pozitif karşılık | Kanon.Yasaklar | yok | orta · tespit içerik yargısı, yalnız yasak/karşılık eşlemesi çevrilir |
| 8 | 20 | 284 | 200 | yasak (otomatik silme) → arşive in + pointer | Kanon.Yasaklar | yok (yalnız kanon freni) | kolay |
| 9 | 21 | 167 | 130 | done-yüklemi (gün sayılır ↔ push'lanmış commit) | Kanon.Commit | `tools/verify-push.py`, `tools/sunum-proof-of-work.py` | kolay |
| 10 | 22 | 472 | 350 | sınıflandırma (önek `[icra]/[damıtma]/[ariza]/[revert]`, dil İngilizce, karar başına commit) | Kanon.Commit | kod yok (hook'ta yalnız `git add -A` yasağı: `.claude/hooks/*` ve Rust'ta yok, ajan settings deny) | kolay |
| 11-12, 14-15 | 26-30 | ~2300 | 0 | karar kaydı, tarihçe, anlatı | yok | yok | çevrilemez |
| 13 | 28 | 444 | 100 | yasak (tek-flagship; geri-açma koşulu) | Kanon.Yasaklar | yok | kolay · kayıt tarihsel, koşul tek |
| 16 | 34 | 927 | 350 | kapı (çelişki varsa karar öncesi rapor; 3 durum kodu bilgi/uyarı/acil) | Kanon.CeliskiKapisi | `celiski-kapisi` skill (LLM), kod yok | kolay · karar fonksiyonu; çelişki tespiti girdi |
| 17-18 | 35-36 | ~1180 | 100 | biçim (durum bloğu üç yüz) | yok | yok | çevrilemez ağırlıkla |
| 19 | 37 | 283 | 80 | eşik (≤30 dk sınırı) | Kanon.Yasaklar | yok | kolay · tek sayı |
| 20 | 38 | 283 | 80 | biçim kuralı (özet + pointer) | Kanon.Yerlesim | `tools/pointer-kayma.py`, `tools/pointer-graf.py` | orta · pointer geçerliliği dosya sistemi girdisi |
| 21 | 39 | 390 | 100 | formül (detay seviyesi = f(token, zaman, iş büyüklüğü)) | Kanon.Yerlesim | yok | zor · parametre yok, kalibrasyon sonra |
| 22 | 40 | 507 | 250 | sınıflandırma (kural/yasak yerleşimi ufka göre: kapsül ∨ pano ∨ kanon ∨ skill) | Kanon.Yerlesim | `tools/kural-envanter.py` | orta · üç-yuva kararıyla birleşir |
| 23 | 41 | 808 | 250 | yasak (ruh hali takibi, günlük-özüt kullanımı, psikolog rolü) | Kanon.Yasaklar | yok | orta · tespit yargı |
| 24, 26, 27, 32, 35 | 42,44,45,50,54 | ~3000 | 0 | vizyon, tez, kapanış kaydı | yok | yok | çevrilemez |
| 25 | 43 | 868 | 100 | dal (mod yok, görev-ölçek optimizasyonu) | Kanon.Yetki | yok | zor · "optimizasyon" tanımsız |
| 28 | 46 | 879 | 150 | durum (denetçi raporu iki parça) | Kanon.CeliskiKapisi | yok | orta |
| 29 | 47 | 753 | 200 | biçim sınırı (açıklama 1 satır, en çok 3 cümle) + deneysel meta kural | Kanon.Yerlesim | yok | kolay · sayı eşiği |
| 30 | 48 | 5115 | 1200 | sınıflandırma (kalıcı ajan atama, katmanlama; otomasyon ↔ canlı-ajan devretme merdiveni: kontrol/durma/tetik devri = otomasyon, prompt/kimlik devri = canlı ajan) | Kanon.AjanYetki | `tools/alan-ajani-dogur.py`, `kod/durum` | orta · (a)-(d) anlatı, ek fıkra net sınıf tablosu |
| 31 | 49 | 1207 | 600 | sınıflandırma (Katman-1 listesi: kanon, silme-birleştirme, geri-alınması zor, dışarı çıkacak iş, para, rol, değer) + ölçek eşikleri | Kanon.Yetki | kod yok (hook `core_tel` yazımı keser) | kolay |
| 33 | 51 | 851 | 250 | yasak (ayıklık sorgusu hiçbir yüzeyde) | Kanon.Yasaklar | yok | kolay |
| 34 | 53 | 2100 | 900 | durum makinesi (damıtma(d) → ∀m karar ∈ {koru, damıt, arşiv}; monolitik yeniden-özüt yasak ∨ Salih emri) | Kanon.Ingest | `damitma` skill, `tools/sicak-katman-fifo.py`, `tools/ta-triyaj.py` | orta · delta kuralı net, katman geçiş koşulları ingest-semasi'ne bağlı |
| 36 | 55 | 2323 | 150 | dal (öncelik çatışmasında prototip kazanır); gerisi revizyon tarihçesi | Kanon.Yetki | yok | çevrilemez ağırlıkla |
| dipnot | 57, 59 | 1301 | 0 | tanım (token×zaman) | yok | yok | çevrilemez · tanım metni |
| 37 | 61 | 3834 | 1700 | kapı ağacı (eşik üstü ∧ ... → 3 model; karşıt-temel a-e; Katman-1 onay şart / Katman-2 seç; geri-alınabilirlik 3 etiket; yakınsama) | Kanon.KararModeli | `karar-modeli` + `karar-hatti` skill, kod yok | orta · karşıtlık "canlılık" yargı, kalan dallar çevrilir |
| 38 | 63 | 3247 | 1300 | yasak listesi + sınıflandırma (rapor-dili paketi: niceleyici ayrımı, `[aranamadı]`, özet niteleyici taşımazsa `EKSİK`, derece-sorma yasağı, çıplak-yüzde yasağı, V numarası yalnız masada) | Kanon.RaporDili | `tools/buyuk-harf-temizle.py` ilgisiz; `tools/asof-eval.py` kısmen | orta · tespit kısmı yargı |
| 39 | 65 | 1281 | 550 | yasak (damgasız rakam, optimal-kıyassız "kaç kat"); pozitif karşılık `[?]` | Kanon.RaporDili | `tools/anakronizm-denetim.py` (tarih), `tools/kural-sayaci.py` | kolay-orta · damga var/yok boolean |
| 40 | 67 | 7300 | 3200 | kapı ağacı (a eşik = m.37; b araştırma-önce; c ilk-çıktı-hızlı lojik formu: düşük maliyet ∨ v1 mevcut → uygula; çift-atlas dönem kuralı; antitez = ¬T; m.40b v0.2 multi-hop) | Kanon.KararSunum | `atlas-kosum` skill, `tools/atlas-derle.py` | orta-zor · v0.2 diyalektiği aşamalı durum makinesi, uzun |
| 41 | 69 | 4444 | 2200 | kapı (kanon/inşa kararı geçerli → (yüzey = ana-sıra ∧ model = en güçlü) ∨ Salih imzası, gereklilik; `switchModelsOnFlag: false`; dış-proje sınırı md.49) | Kanon.KararYetkisi | `kod/hook/src/core_tel.rs`, `pretool-core-tel.sh`, `ajan_fren.rs`, `session_start.rs` | orta · hook'larla fark testi gerekir |
| 42 | 71 | 2928 | 1900 | formül + eşik (Özgürlük ≤ Toparlanabilirlik; Gevşet ← sicil ∧ geri-alınabilir ∧ baskı; risk = p×maliyet×geri-alma; çeşitlilik bütçesi; (h) amaç↔done çelişirse amaç kazanır + `[sapma]`) | Kanon.AjanYetki | `tools/alan-ajani-dogur.py`, `gorev-emri-derleme` | orta · (b)-(f) tanımlı fonksiyon, parametreler `[?]` |
| 43 | 72 | 2653 | 1300 | eşik (tekrar-sayısı(görev) ≥ 3, W = 90 gün; aday ≠ üretim) | Kanon.SkillDogum | `tools/loop-dedektor.py`, `tools/baglam-skill-aday.py` | kolay · `SkillKapi.z1` ile ortak sabitler |
| 44 | 73 | 2178 | 700 | dal (kapsam çok-domain ∨ lider yok → Jarvis; tek-domain ∧ lider → domain-lider) | Kanon.AjanYetki | `tools/alan-ajani-dogur.py` | kolay · iki dal |
| 45 | 74 | 894 | 200 | sınıflandırma (zorlanabilir ↔ ihlali koddan yakalanır) | Kanon.Yasaklar (meta) | `tools/kural-envanter.py` | kolay |
| 46 | 76 | 2475 | 1500 | kapı + eşik ((a) künye/SHA eşleşmezse dur; (b) arama-özeti ⇒ `[K]`; (c) rejim etiketi; (d) 54 çağrı/ajan, 570/workflow, 36 ajan, uyarı 36 / durdur 72) | Kanon.KosumButunluk | `kod/hook/src/ajan_fren.rs`, `pretool-ajan-fren.sh` (sapma var, bkz. §1 Gözlem 2) | kolay-orta · sayılar hazır |
| 47 | 78 | 901 | 600 | done-yüklemi (hazine(skill) ↔ K3-geçti ∧ canlı-koşum ≥ 1 ∧ kabul-sözü) | Kanon.SkillDogum (K4) | `skill-kapisi` skill | kolay · `SkillKapi.Hukum` uzantısı |
| **Toplam** | | **61679** | **~21000 `[?]`** | | **12 modül** | | |

Tüzük için önerilen 12 modül: Kanon.Yetki (m.1,2,4,5,25,31,36) · Kanon.Yasaklar (m.3,7,8,13,19,23,33,45) · Kanon.Commit (m.9,10) · Kanon.Yerlesim (m.20,21,22,29) · Kanon.CeliskiKapisi (m.16,28) · Kanon.Ingest (m.34) · Kanon.KararModeli (m.37) · Kanon.RaporDili (m.38,39) · Kanon.KararSunum (m.40) · Kanon.KararYetkisi (m.41) · Kanon.AjanYetki (m.30 ek, m.42, m.44) · Kanon.SkillDogum (m.43, m.47) · Kanon.KosumButunluk (m.46).
(13 isim sayıldı; Yetki ile Yasaklar'ın tek `Kanon.Yetki`'de birleşmesi 12 verir.)

## 3. Diğer core dosyaları

| Dosya · bölüm (satır) | Tür | Modül | Çevrilebilir bayt `[?]` | Mevcut kod | Zorluk · gerekçe |
|---|---|---|---:|---|---|
| ajan-metodolojisi §3 (21-29) merdiven | kapı (3 soru: adım tahmin edilebilir ∧ sabit yol kodlanabilir ∧ model kararı gerekmez → bir basamak yukarı) | Kanon.Delegasyon | 700 | `tools/paket-yonlendir.py` (ilgili), `kod/hook/src/paket.rs` | kolay |
| ajan-metodolojisi §4 (30-41) delegasyon | yasak + eşik (sözleşme dörtlüsü; paralellik-uygunluk testi; işçi liderden pahalı model kullanamaz; skill eşik n≥10, 2× bandı; delegasyon varsayılan KAPALI; efor cetveli 1/2-4/10+) | Kanon.Delegasyon | 2200 | `tools/skill-esik.py`, `tools/paralel-kapi.py` (PK-1..12), `kod/hook/src/ajan_fren.rs` | orta · cetvel kestirim `[?]` |
| ajan-metodolojisi §6, 6b (52-66) | sınıflandırma + durum (katman/rol → model; eskalasyon tetikleri: Salih beyanı ∨ hakem `TUTMADI` ≥ 3; sessiz eskalasyon yasak) | Kanon.Eskalasyon | 2400 | `tools/alan-ajani-dogur.py` (varsayılan model alanı) | kolay-orta |
| baglam-anahtar-kaydi §2 (17-513) | JSON anahtar kaydı (veri) | yok, JSON kalır (`anahtar-denetim.py` okur) | 0 | `tools/anahtar-denetim.py`, `tools/anahtar-cascade.py` | çevrilemez · veri; Lean'e gömmek bakım yükü |
| baglam-anahtar-kaydi §3 (514-521) emeklilik | durum makinesi (6 adım, sıra backward; sıcak ihlal 0 → commit, ≠0 → `KISMİ`) | Kanon.AnahtarEmeklilik | 1800 | `tools/anahtar-cascade.py`, `tools/anahtar-denetim.py` | kolay |
| baglam-anahtar-kaydi §4 (522-535) metrikler | eşik tablosu (sıcak 0; ılık k1=1 uyarı, k2=10 eylem; halefsiz 0; damgasız 0) | Kanon.AnahtarEmeklilik | 2700 | `tools/anahtar-denetim.py`, `tools/silver-saglik.py` | kolay · tablo doğrudan `def` |
| deterministik-tasarim §2-3 (8-16) | sınıflandırma (iş türü → vurgu var/yok) | Kanon.Deterministik | 800 | yok | kolay |
| halusinasyon-paketi §2 (30-60) | formül (H = Σ w_i v_i, 15 değişken; τ_H = 7 / 4; v3a override; H ≤ 3 / 4-6 / ≥ 7 bantları; fizibilite) | Kanon.Halusinasyon | 4200 | `.claude/skills/halusinasyon-engelleyici/scripts/derece.py` (3298 B) | kolay · en olgun aday, ağırlıklar `[?]` kanıtsız-tercih |
| halusinasyon-paketi §1 (12-29) fren listesi | sınıflandırma (fren → ölçülü / ölçüsüz / kapsam-dışı) | Kanon.Halusinasyon | 1300 | yok | orta · damga yargısı |
| ingest-semasi §1-3 (5-40) | sınıflandırma + first-hit (5 zorunlu alan, 8 tip → hedef tablosu, 4 soru triyaj NOOP/UPDATE/GEÇERSİZ-KIL/ADD) | Kanon.Ingest | 2600 | `damitma` skill, `tools/baglam-tablo.py`; kod karşılığı zarf denetimi yok | kolay · Gorev.Sablon'a en yakın kalıp |
| ingest-semasi §5-7 (45-61) | eşik + yasak (kapsül ≤ 200 satır, %70 uyarı; Σönem ≥ 150; devir ≤ 2000 token; dlq 2 seans; şema additive-only) | Kanon.IngestTetik | 1600 | `tools/sicak-katman-fifo.py`, `kod/hook/src/session_start.rs` | kolay |
| sema-sikistirma §1-2 (12-31) | formül + tablo (mdl kabul; birleştirme s > 0; U skoru: U ≥ 2 şemala / 0-1 olgu-satırı / < 0 ham; 7 satırlık sınıf → karar) | Kanon.SemaSikistirma | 3600 | yok (damitma şema-dalı elle) | kolay · U toplam ± 1 |
| veri-muhendisligi §2 (12-19) | done-yüklemleri (bronz/silver/gold zorunlu yüklemler, yasaklar) | Kanon.KatmanYuklem | 2000 | `tools/silver-saglik.py`, `tools/katman-hatti.py`, `tools/katman-olcum.py` | orta · yüklemler dosya/SQL ölçümü, Lean yalnız hüküm |
| veri-muhendisligi §8b (55-57) | formül (şiddet = (uzunluk_a + uzunluk_b) × tekrar) | Kanon.KatmanYuklem | 500 | `tools/ta-triyaj.py` | kolay |
| world-model §4 (37-43) x tanımı | yasak (tek skaler x yasak; damgasız kapasite saklanmaz; oran yalnız aynı görev+model) | Kanon.XOlcum | 1200 | `tools/baglam-tablo.py`, `tools/ambar-tablo.py` | orta · şema kısıtı |
| world-model §2 (11-28) bus matrix | veri tablosu | yok | 300 | yok | çevrilemez |
| skill-uretim-semasi bakım (81-91) | formül (λ = max(1, ½·log10 N); EMEKLİ-ADAY; BAKIM-KK kanıt-izli öneri kuralı, 45 gün) | Kanon.SkillBakim | 1500 | `tools/skill-esik.py`, `tools/loop-dedektor.py` | orta · log10 için `Nat` yaklaşımı gerek |
| skill-uretim-semasi §4b (109-121) | sınıflandırma (üç yuva: her seans → CLAUDE.md; dosya → rules; iş türü → skill) + S-kaynak skoru + F6 | Kanon.UcYuva | 2000 | `tools/baglam-skill-aday.py`, `tools/skill-butce.py` | orta · skor katsayıları kalibresiz `[?]` |
| skill-uretim-semasi §1-2, skill-tetikleme §2-4 | **zaten taşındı** (SkillKapi, SkillTetik) | | | `kod/skill-kapi`, `tetik-denetim.py` | md'de pointer bırakmak yeter |
| skill-tetikleme §5 (54-56) | sayısal sınırlar (iç içe ≤ 2, dal ≤ 5, retry 3, description ≤ 1024) | SkillTetik'e ek `def` | 400 | `tetik-denetim.py` | kolay |
| varlik-felsefesi · durum-kapsulu · pano | felsefe / durum kaydı | yok | 0-300 | | çevrilemez |

## 4. Kök ve ajan sözleşmeleri, protokol, kural dosyaları

| Dosya · bölüm | Tür | Modül | Çevrilebilir bayt `[?]` | Mevcut kod | Zorluk · gerekçe |
|---|---|---|---:|---|---|
| AGENTS.md (kök) md.1 | yasak + yetki matrisi (başka ajan dizini okunmaz; kendi kanon + kök; `ogrenme/` ajanlara kapalı) | Kanon.Izolasyon | 700 | `kod/hook/src/altajan_okuma.rs`, `ajan_fren.rs`, `okuma-izin.sh` | orta · yol kalıbı girdi |
| AGENTS.md md.1 ad ölçütü (Karar 107+110: gerçek kişi değil ∧ ≤ 4 harf ∧ İngilizce ∧ Türkçe eş sesli değil) | boolean ∧ | Kanon.AjanAdi | 350 | `tools/ad-esitligi-denetim.py`, `tools/alan-ajani-dogur.py` | kolay |
| AGENTS.md md.2, 3, 5 | sıralama/öncelik (Salih güncel talimat > duran kural; Katman-1/2) | Kanon.Oncelik | 700 | yok | kolay |
| AGENTS.md md.4, 6, 8, 9 | yasak + sınıflandırma (silme yasağı; commit önek tablosu; em-dash yasağı; amaç↔done çelişirse `[sapma]`) | Kanon.Commit (m.9-10 ile ortak) | 800 | yok (`stop-buyuk-harf` yalnız caps) | kolay |
| AGENTS.md md.14-15 | yasak (`git add -A` yasak; dizin sahibi yazar; emir `cc/gelen/`) | Kanon.Izolasyon | 450 | yok · ajan settings deny | kolay |
| jarvis/AGENTS.md §4 yetki, §3 okuma sırası, §2 hareket kütüğü | kapı + sıra (Katman-1 listesi; yüzey m.41 GK-2; okuma sırası 1-3) | Kanon.Yetki (m.31 ile), Kanon.OturumBasi | 1600 | `kod/hook/src/session_start.rs`, `core_tel.rs`, `tools/acilis-kapilari.py` | orta |
| 8 alan ajanı AGENTS.md §3-§5 (şablon, `alan-ajani-dogur.py` üretir) | eşik + yasak (kapsül 4 KB/20 satır, ≤ 8 madde; işçi ≤ 36/koşum, araç ≤ 54/işçi, aile ≤ 3; işçi pahalı model yok; `.claude/**`, `core/**` yalnız Edit; yapan ≠ ölçen) | Kanon.AlanAjani (parametre: ad, model) | 7200 (8 × ~900) | `tools/alan-ajani-dogur.py`, `okuma-izin.sh`, `hareket-kutuk.sh` | kolay · tek şablon, 8 örnek fark testi |
| wiki/paralel-oturum-protokolu.md 5 kural (6-11) | kapı (canlı-oturum: son commit ≤ 15 dk ∧ kapsülde kapanış kaydı yok → şüphe; manifest kapısı; paylaşılan kaynak freni; `git add -A` yasak; PR kuralı) | Kanon.ParalelOturum | 2300 | `tools/acilis-kapilari.py`, `tools/paralel-kapi.py`, `.claude/hooks/pretool-*` | kolay · K1 zaten Python |
| paralel-oturum-protokolu EK-5 (12) | karar tablosu (oturum türü → worktree AÇIK/KAPALI; birleştirme yalnız Salih beyanıyla) | Kanon.ParalelOturum | 1200 | `.claude/hooks/rust-yonlendir.sh`, herdr komutu | kolay |
| .claude/rules/{cc,ogrenme,tools}.md | yasak/eşik ufak (alt-ajan dönüşü ≤ 2k token; işçi 10-15 çağrı; hook test kuralı engelleyen hook için) | Kanon.Kosum (Kanon.KosumButunluk'a eklenebilir) | 600 | `tools/AXI-STANDARDI.md` | kolay · çoğu pointer |

## 5. Skill gövdeleri (jarvis/.claude/skills/*/SKILL.md)

Skill gövdesi nasıl-yapılır anlatısıdır; çevrilebilir kısım yalnız kapı/sıra/eşik adımları.

| Skill (bayt) | Çevrilebilir kısım | Bayt `[?]` | Modül | Mevcut kod | Zorluk |
|---|---|---:|---|---|---|
| seans-acilis (8211) | §1 staj kapısı (klasör staj ise ritüel yok), erişim yoksa `SNAPSHOT`; §1.4 canlı-oturum kapısı; §1.5 manifest kapısı; 3b silver tazelik; frenler | 1800 | Kanon.SeansAcilis | `tools/acilis-kapilari.py` K1-K3, `session_start.rs` | kolay · kapı hükmü zaten kodda |
| seans-kapanis (12779) | staj kapısı; kanal yoksa ham fikir; kapsül ≤ 8 KB ∧ ≤ 40 satır; boyut tablosu (kapsül 8 KB/40, pano 12 KB, fikir-kutusu 20, defter 48, CLAUDE.md 7 KB/80, KILAVUZ 16 KB); 6d silver kapı çıkış 6; 6g duman testi | 3000 | Kanon.SeansKapanis + Kanon.Butce | `tools/kural-sayaci.py`, `silver-saglik.py --kapi`, `skill-esik.py`, `hafiza-ayna.py`, `verify-push.py` | kolay |
| damitma (6125) | adım 1 tetik (≥ 40 madde ∨ Σönem ≥ 150 ∨ FLAG ∨ Salih), triyaj, silver kapısı | 1500 | Kanon.Ingest (ortak) | `tools/sicak-katman-fifo.py`, `silver-saglik.py` | kolay |
| ogren (11118) | PROBE ≤ 12 soru ikili arama; yanlış → ≤ 2 tekrar → `açik`; ≤ 8 düğüm/seans; ≤ 3 kavram/teslim; `DONE` yalnız Salih | 2200 | Kanon.Ogren | yok | orta · durum makinesi |
| gorev-emri-derleme (8036) | mekanik kapılar (rakam damgası, dürüstlük), emir iç-tutarlılık dörtlüsü, eskalasyon satırı zorunlu | 1800 | Kanon.GorevEmri (Gorev.Sablon ile bağlı) | `scripts/tetik-denetim.py` | orta |
| atlas-kosum (7323) | aşama sırası tez → antitez → V26 sondaj → maskeli hakem; gerek kontrolü | 1500 | Kanon.KararSunum (m.40 ile) | `tools/atlas-derle.py` | orta |
| karar-hatti (3915) | sıra: çelişki → dur; araştırma-önce kontrolü; Katman-2 onay beklenmez | 1200 | Kanon.KararHatti | yok | kolay |
| celiski-kapisi (3779) | ölçek kontrolü; literal ↔ lojiksel çelişki; emir durumu | 1000 | Kanon.CeliskiKapisi (m.16 ile) | yok | kolay |
| yol-planla (4359) | hedef fonksiyonu seç (seri → yol maliyeti, paralel → makespan); topoloji `birleştirilebilir_mi` | 1000 | Kanon.YolPlan | `tools/paralel-kapi.py` | orta |
| karar-modeli (3428) | eşik, m.40b kapısı, karşıt-temel şartı | 900 | Kanon.KararModeli (m.37 ile) | yok | kolay |
| emekli-anahtar-cascade (4913) | adım sırası, sıcak ihlal 0 → commit | 800 | Kanon.AnahtarEmeklilik (ortak) | `tools/anahtar-cascade.py` | kolay |
| skill-kapisi (7719) | BAKIM-KK adımı; gerisi taşındı | 500 | SkillBakim | `kod/skill-kapi` | kolay |
| pipeline-kosum (2867) | kapanış: tüm satırlar `DONE` ∧ kaptan beyanı | 500 | Kanon.Pipeline | yok | kolay |
| halusinasyon-engelleyici (5233) | derece kapısı (paket ile ortak) | 300 | Kanon.Halusinasyon | `scripts/derece.py` | kolay |
| karar-masasi (4217) · karar-kaydet (2305) · sinav-grill (2802) · wiki-sayfa-yaz (2929) | JSON spec şeması; yalnız-Salih-tetik yasağı; oturum başına 1-2 sayfa | 1200 (4 dosya) | Kanon.Yasaklar'a ekle | `masa-uret.py` | kolay · küçük |
| lojik-ceviri (3967) | meta (zaten Lean şablonu) | 0 | | | |

## 6. Önerilen taşıma partileri

Sıralama ölçütü: önce zaten kodla uygulanan (fark testi hazır) ve sık yüklenen kurallar; her parti 3-5 modül, parti sonunda `lake build` + ilgili Python/Rust ile fark testi (SkillKapi örneği).

**Parti 1 (en sık yüklenen + kod karşılığı hazır; 5 modül, ~10 KB kaynak `[?]`)**
1. Kanon.Izolasyon: kök AGENTS md.1, 14-15 (okuma/yazma yetki matrisi); kod `altajan_okuma.rs`, `ajan_fren.rs`, `core_tel.rs` ile fark testi.
2. Kanon.Commit: kök md.4/6/8/9 + tüzük m.9, 10 (önek tablosu, dil, em-dash, silme yasağı, amaç↔done `[sapma]`).
3. Kanon.AjanAdi: ad ölçütü 4 boolean; `tools/ad-esitligi-denetim.py` ile fark.
4. Kanon.ParalelOturum: protokol 5 kural + EK-5 karar tablosu; `acilis-kapilari.py` K1 ile fark.
5. Kanon.SeansAcilis: K1-K3 kapı hükmü + staj kapısı (her seans yüklenir).

**Parti 2 (kodda sabit sayılar var, kolay; 5 modül)**
Kanon.Halusinasyon (`derece.py` fark testi, en olgun) · Kanon.SkillDogum (m.43 + m.47, SkillKapi sabitleriyle ortak) · Kanon.KosumButunluk (m.46; **önce 36/72 ↔ 72/144 sapmasını Salih'e sor**) · Kanon.Delegasyon (ajan-met §3-4, `skill-esik.py`) · Kanon.SeansKapanis + Butce (boyut tablosu, `kural-sayaci.py`).

**Parti 3 (şablon kalıbına en yakın sınıflandırma/first-hit; 5 modül)**
Kanon.Ingest (+ IngestTetik, damıtma tetikleri, m.34 delta) · Kanon.SemaSikistirma (U skoru) · Kanon.AnahtarEmeklilik (+ metrik tablosu, cascade) · Kanon.KatmanYuklem (+ TaTriyaj formülü) · Kanon.AlanAjani (8 AGENTS'in ortak şablonu, `alan-ajani-dogur.py` çıktısıyla fark).

**Parti 4 (karar zinciri; hepsi LLM yargısı girdisiyle; 5 modül)**
Kanon.CeliskiKapisi (m.16, 28 + skill) · Kanon.KararModeli (m.37 + skill) · Kanon.KararSunum (m.40 + atlas-kosum, en uzun) · Kanon.KararYetkisi (m.41; hook fark testi) · Kanon.KararHatti.

**Parti 5 (zor/orta, parametre kalibrasyonu `[?]` bekleyen; 4-5 modül)**
Kanon.AjanYetki (m.30 ek, 42, 44) · Kanon.RaporDili (m.38 ek, 39) · Kanon.Yerlesim + UcYuva (m.20-22, 29, skill-üretim §4b) · Kanon.Eskalasyon · Kanon.Ogren / Kanon.GorevEmri.

Bırakılacaklar (md'de kalır): durum-kapsulu, pano, varlik-felsefesi, world-model bus matrix, baglam-anahtar-kaydi §2 JSON, tüzük m.6, 11-12, 14-15, 17-18, 24, 26-27, 32, 35 ve dipnotlar.

## 7. Riskler ve açık noktalar

- **Sayı çelişkisi:** tüzük m.46(d) 36/72 ↔ `ajan_fren.rs` varsayılan 72/144. Lean modülü hangi değeri kanon sayar? Kanon değişikliği Salih kararıdır; ben yalnız bildiriyorum.
- Tüzükte çevrilebilir payı olan 6 madde (m.37, 38, 40, 41, 42, 43) 1-4 KB'lık satırlar: satır içi fıkralar (Ek fıkra, GEÇİŞ kaydı) tarihçeyle iç içe; taşıma öncesi "yürürlükteki son hâl" ayıklaması gerekir (m.40 satırı ve m.41 GEÇİŞ KAYDI-2 okuma sırasında kesik görüldü, tam metin Parti 4 başında okunmalı).
- `baglam-anahtar-kaydi.md` 34.5 KB'ının büyük kısmı JSON veri; Lean'e almak getiri sağlamaz, `anahtar-denetim.py` mevcut.
- Karar 114 kuralı: md'de pointer satırı kalır, gerekçe/atıf md'de durur (SkillKapi kalıbı).
- Hariç tutulan: `.claude/agents/*.md` (hakem, research-agent) ve `../sablonlar/*` kapsam dışıydı; ayrı bakılmalı.
- Bayt payları okuma tabanlıdır `[?]`; modül başına gerçek ölçü, ilk Lean yazımında satır sayımıyla doğrulanmalı.
