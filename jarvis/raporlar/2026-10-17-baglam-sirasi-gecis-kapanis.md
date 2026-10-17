# Bağlam sırası korumalı md → Lean/Rust geçişi: kapanış (durum #18, Karar 117)

AS-OF 2026-10-17 · Claude Code 2.1.302 · kaynaklar: `raporlar/2026-10-16-baglam-sirasi-import-deneyi.md` (ölçüm B1-B8), `raporlar/2026-10-16-baglam-sirasi-formalizasyon-sentez.md` (model), `raporlar/2026-10-16-baglam-sirasi-envanter.md` (162 bölüm).

## 1. Ne yapıldı
| Parti | PR | Kapsam |
|---|---|---|
| altyapı | (main `df1990d`) | `kod/baglam` (genislet/denetle), `Kanon.BaglamSirasi` (zincir + yelpaze teoremleri) |
| 1 | #9 | tüzük m.46, m.47; `prompt-dosya` hook'u ve 3 Python aracı genişletilmiş okumaya |
| 2 | #11 | tüzük m.43, m.45; `CeliskiKapisi`, `Commit` genişletmesi |
| 3 | #12 | tüzük m.8-10, m.16 (EK-2: parçalı tüzük, görünüm kopyası yok) |
| 4 | #13, #14 | tüzük m.28-31, m.33, m.39-42, m.44 (omp + Sonnet işçiler) |
| pointer | #15 | kök kanon md kalır, maddeler Lean'e pointer (EK-1) |
| 5 | #16, #17 | `core/` 4 dosya; PostToolUse `Read` genişletici hook'u |
| izin | #18 | etkisiz `Write(...)` kuralları kalktı; tüzük onayı tüm parçalara |
| 6 | bu PR | Karar 114 modülleri 7 `core/` dosyasına Lean eki olarak bağlandı |

## 2. Son durum (ölçüm, 2026-10-17)
- `baglam denetle`: tüzük 29 blok + 9 `core/` dosyası, toplam 0 ihlal.
- Lean: `lake build` 80/80 (son tam koşum, parti 5).
- Okuma rejimi: PostToolUse `Read` hook'u ana oturumda canlı; içe aktarılan bloklar `Read` sonucunun ardından sırayla gelir (bu oturumda iki dosyada gözlendi).

## 3. Yerleşim kuralı (uygulanan)
- Kural metni kesildiyse (tüzük): kesilen yerde kısa md satırı, hemen ardından Lean modülü, kalan md ayrı parçada.
- Kural metni kesilmediyse (`core/`, anlatı karışık): md tam kalır; Lean, kapsadığı son bölümün ardına ya da dosya sonundaki "Lean eki"ne gelir; "ayrışırsa kod kazanır".

## 4. Kalan / sınıflanan
- Anlatı (md'de kalır): tüzük m.1-7, m.11-15, m.17-27, m.32, m.34-38 · `world-model-tasarimi.md` §4 · `.claude/rules/ogrenme.md`, `tools.md` (yol koşullu kısa usul notu).
- Harness memory: md kalır (Claude Code biçimi); kural içeren notlar ileride Lean'e aday.
- Açık ölçüm: `sema-sikistirma.md` §1 formülünün Rust icrası yok (envanter D/Rust) · `skill-tetikleme-semasi.md` §4 yasak 1/6/7'nin `SkillTetik`'teki karşılığı doğrulanmadı.
- Sonraki iş: durum #19 skill revizyonu.
