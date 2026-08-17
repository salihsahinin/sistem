---
name: skill-kapisi
description: Bir skill ADAYINI (yeni fikir, kutu satırı, taslak ya da mevcut skill) kapı-ağacından yürütür (K0 GEREK → K1 DEĞER → İNŞA → K2 TOPRAKLAMA → K3 BİÇİM+TÜR) ve GEÇTİ/BEKLET/ONAR/RET hükmü + tür-demeti üretir; deterministik kapılar script'le, iddia-topraklama bağımsız doğrulayıcıyla. Tetik; "kapıdan geçir", "şema testi", "skill adayını değerlendir", yeni skill üretimi/evrimi ÖNCESİ (zorunlu), hazine denetimi. KULLANILMAZ; skill'in kendisini yazmak için, skill'i çalıştırmak için, m.25 küçük direkt işlerde.
argument-hint: "<aday: ad + amaç + tetik-kalıbı | skill dizini>"
metadata: { owner: carvis, version: "1.0.0-deneysel-m29", kural: "core/skill-uretim-semasi.md" }
---

# skill-kapisi — kapı-ağacı koşum talimatı (v1, 2026-08-15)

Kural kaynağı: `core/skill-uretim-semasi.md` (ağaç + düğüm sözlüğü + formüller) · graf: `core/skill-uretim-semasi.d2` · deterministik denetim: `scripts/kapi-denetim.py`. İlke: kapı prompt'la kurulmaz — her düğüm yapısal sinyale bağlanır (script / bağımsız doğrulayıcı / eval / dış-kayıt); üretici ≠ doğrulayıcı.

## Adımlar
1. **Aday künyesi** (tek blok): `ad · amaç (1 cümle) · tetik-kalıbı · köken (aşağıdan: m.43 sayaç k_W ∨ yukarıdan: Salih emri) · mevcut skill mi (evrim) yeni mi`. Künye yoksa kapı koşmaz — önce künye.
2. **K0 GEREK:** `¬kapsanmış(a,H) ∧ (Y1 ∨ Y2 ∨ Y3)`. Hazineyi tara (`ls .claude/skills/` + sözlük "Skill Hazinesi"): tam kapsama → **RET-0** (NOOP satırı kutuya, dur). Kısmî kapsama → yaprak "evrim(s)" notu al, devam. Y1 için skill'siz bir koşum yap ya da geçmiş koşumu göster (DRFR'de ≥1 ✗ ∨ tutarsızlık); Y2 kanon-LAZY kuralı; Y3 |adım|≥3 ∧ sabit sıra. Üçü de hayırsa **RET-0** ("tek-adımlı iş, n ne olursa olsun").
3. **K1 DEĞER:** `Z1 ∨ Z2`. Z1: k_W (son 90 gün, özdeş↔varyant ayrı sayılır) ≥ 3 (τ=0,8 Laplace) ∧ (Δ̂ bilinmiyor ∨ k_W·Δ̂ ≥ 1,25·C_inşa). Z2: Salih'in Katman-1 emri (bütçe atlanır; K2/K3 ATLANMAZ). İkisi de hayır → **BEKLET**: `kuyruk/skill-fikir-kutusu.md`'ye satır (m.43 sayaç bölümü) — zayıf-yeni aday yalnız Salih onayıyla (Z2) ilerler.
4. **İNŞA (eval-önce, K-016):** önce `evals/evals.json` (≥3 test + should_trigger ≥5 + should_not_trigger ≥5), sonra skill'siz baseline notu, sonra eval'i geçen MİNİMAL gövde. Mevcut skill için bu adım "eksik evals'i tamamla"dır.
5. **K2 TOPRAKLAMA:** (a) `python3 .claude/skills/skill-kapisi/scripts/kapi-denetim.py <skill-dizini> --repo ~/jarvis` → **R** referans-varlığı (yol · m.NN · skill adı) + biçim ön-raporu; (b) **İ** iddia-topraklama: gövdedeki tüm sayısal iddialar + rastgele n_val = min(|iddia|, max(3, ⌈|iddia|/2⌉)) iddia için BAĞIMSIZ doğrulayıcı (alt-ajan ya da ayrı tur) — yalnız İDDİA metni verilir, gerekçe/kaynak VERİLMEZ (CoVe-Factored); TUTMUYOR → iddia K/X'e ya da çıkar; (c) **¬P**: skill'in kendi kalite-kontrolü yalnız "dikkatli ol/uydurma" talimatı mı? Öyleyse yapısal sinyale bağla. Düşerse **ONAR-2** (script'in eksik listesiyle geri; ≤3 tur, sonra BEKLET).
6. **K3 BİÇİM+TÜR:** şekil FIRST (T-R ritüel > T-O orkestratör > T-Y yan-etkili > T-Ü üretici; iki şekil eşit ağırlıkta → BÖL); F1-F4 script'ten, F5 tek-sorumluluk hakem gözüyle; tür-özel: T-Y → `disable-model-invocation: true` + script/plan-validate-execute + m.31 · T-R/T-O ∧ yan-etki → adım Salih-beyanına bağlı · T-O → paralellik-uygunluk + handoff kontratı + her çağrısı tetiklenme şemasına uyar (`core/skill-tetikleme-semasi.md`: 9 alan, T-Y örtük/alt-ajandan çağrılmaz) · T-R → zaman-kayması freni · T-Ü → "commit yapmaz". F1e hazine-bütçesi uyarısı çıkarsa yeni skill sığana dek hazine kısaltılır ya da `/context` ile bütçe ölçülür. Düşerse **ONAR-3**.
7. **Yaprak + kayıt:** hüküm `ÜRET-{R|O|Y|Ü} × {yeni|evrim}` + faset-demeti ⟨tetikleyici · yürütme · yan-etki · basamak · köken⟩; kutu satırı güncelle (ÜRETİLDİ/BEKLET/RET); sözlük Skill Hazinesi girişi (üretim tamamlanınca); **ölçüm satırı**: `kuyruk/skill-fikir-kutusu.md` "kapı-ağacı koşumları" tablosuna aday · katman-başına ✓/✗ · tür · süre (10 koşumda kalibrasyon: τ/W/β/n_val). Hüküm bloğu ≤ yarım sayfa; karar Salih'e sunulur (Katman-2: yapar+kaydeder, veto=revert). Skill kaydetme/commit yapmaz; commit seans akışının işidir.

## Gotchas
- **Tekrar sayısını doğrulama sanma:** k_W yalnız K1'i açar; K2 topraklamasını ASLA ikame etmez (aynı-model tekrarların %43'ü 10/10 yeniden üretilir).
- **Sıra sözleşmedir:** artefaktsız K2 koşma (önce İNŞA); K1'i K0'dan önce koşma (kolay iş için değer hesabı israf).
- **Doğrulayıcıya gerekçe sızdırma:** iddia listesi + kaynak-URL/pointer VERİLMEZ, yalnız iddia; sızarsa çıpalı doğrulama = kapı boş.
- **Heuristik ≠ hüküm:** script'in şekil-tahmini ve uyarıları (K) yardımcıdır; birincil şekli sen FIRST kuralıyla yazarsın, script'i düzeltirsin.
- **Sabitleri kanıt sanma:** τ=0,8 · W=90g · β=0,25 · n_val · 1024/7200 char DENEYSEL (transfer); ölçüm satırı yazılmadan koşum bitmez.
- **Yan-etki kaçağı:** T-Y skill'de flag yoksa "iyi niyet" yetmez — flag yapısal fren (m.31'in koda gömülüşü).
