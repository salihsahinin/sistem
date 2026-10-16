# Maskeli hakem raporu: bağlam sırası (durum #18, 2026-10-16)

Hakem: kalıcı `hakem` ajanı (Sonnet 5.5), salt-okur, maskeli. Girdi: aile A/B/C raporları, V26 sondaj tablosu, `raporlar/2026-10-16-baglam-sirasi-import-deneyi.md`. Dönüş aynen kaydedildi (biçim sadeleştirildi).

## Usul
Maske ihlali yok. V26: S4 tutmadı (belgenin "imported file first" ifadesi), o rapor K tavanında; S7, S8 sondajsız → K. Eski model kuşağı bulguları D alamaz.

## Kovalar
- **Sağlam 25** (D 11: A1, A2, A4, A6, A7, A13, A14, B1, B2, B3, B5 · sağlam-K 14: A3, A9, A12, B6, B8, B9, B12, B13, C2, C3, C4, C7, C8, C9)
- **Daraldı 12:** A5 (derinlik ≤4, tekrarsız `@`) · A10 (kök sayımı belirsiz) · A11 (yalnız tek `@` ağacında) · B7 (yalnız `core.symlinks` kapalı klonlarda) · B10 (Copilot hariç) · B11 (Gemini CLI modu doğrulanmadı) · B14 ("tek paket bulunamadı") · C1 (GPT-3.5, 2023, belge QA) · C5 (primacy yoğunluğa bağlı) · C6 (BGQA-3, GPT-3.5) · C10 (U-şekil evrensel değil) · C12 (hook koşulsuz garanti değil, kanarya probu şart)
- **Düştü 3:** A8 (kuyruk kaydırma tek dönüşüm) · B4 (belge: içe aktarma önce) · C11 (knapsack + DP)

## Hayatta-kalma
A 14 iddia: sağlam 10 (%71) / daraldı 3 / düştü 1 · B 14: 9 (%64) / 4 / 1 · C 12: 6 (%50, D 0) / 5 / 1 · **Toplam 40: sağlam 25 (%62,5; D 11) / daraldı 12 (%30) / düştü 3 (%7,5)**.

## m.16 işareti
Belgenin AGENTS.md bölümü ile 2.1.302 ham istek sırası çatışıyor; kanon ölçüme dayanmalı ve sürüm damgası taşımalı.

## Hüküm
**Formal model:** otomatik yükleme rejiminde bağlam, `@` ağacının pre-order düzleştirmesidir, `L(f) = metin(f) ++ L(i₁) ++ … ++ L(iₖ)`; hedef yapı `List` serbest monoidi; `Ls_eq_flatten_map` ve `chain_L` Lean 4.35.0'da Mathlib'siz derlenir. Geçerlilik şartı derinlik ≤4 ve tekrarsız `@` (n=4, tek sürüm). **Dönüşüm:** satır içi açılım olmadığından kesim sonrası md kuyruğu ayrı dosyaya alınır, Lean parçası `.lean.md` bağıyla içe aktarılır; zincir ve yelpaze (kardeş `@`, derinlik 1) iki geçerli biçim. Read rejiminde sıra yalnız Rust genişleticisiyle korunur. **Kesim kuralı:** konum literatürüne değil tür ayrımına (deterministik, koşullu, anlatı) dayanır; knapsack/DP düştü; hook ile %100 uyum varsayılmaz, kanarya probu ister. Açık ölçüm borçları: `@` dedup, kökün 4 sıçramaya dahil olup olmadığı, symlink'in başka klonlardaki davranışı, Gemini CLI modu.
