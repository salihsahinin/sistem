# Bağlam sırası korumalı md → Lean/Rust geçişi: formalizasyon sentezi (durum #18, adım 2)

AS-OF 2026-10-16 · Claude Code 2.1.302 · atlas-kosum (3 aile × tez + antitez, Sonnet; V26 sondaj; maskeli hakem) · hayatta-kalma 25/40 sağlam (%62,5), 12 daraldı, 3 düştü.
Kaynaklar: `cc/rapor/2026-10/rapor-2026-10-16-baglam-sirasi-aile-{A,B,C}.md` · `-v26-sondaj.md` · `-hakem.md` · ölçüm `raporlar/2026-10-16-baglam-sirasi-import-deneyi.md`.

## 1. Model
Bir dosya sıralı parça listesidir; parça ya metin ya içe aktarmadır. İki yükleme rejimi var:

- **Otomatik rejim** (oturum başında `CLAUDE.md` zinciri): `L(f) = metin(f) ++ L(i₁) ++ … ++ L(iₖ)`. İçe aktarma satır içinde açılmaz; `@` satırının yeri ne olursa olsun ebeveynin bütün metninden sonra, yazılış sırasıyla, pre-order DFS ile gelir. Ölçüm ham API isteğinden (B3-B6). Şart: derinlik ≤ 4 sıçrama (belge), `.lean` atlanır, `.lean.md` bağı yüklenir.
- **Okuma rejimi** (skill'in `Read` ile açtığı `core/` dosyaları): `@` açılmaz. Sıra ancak bir genişletici (satır içi transclusion yapan Rust aracı) ile korunur.

Sıra değişmezi: özgün belge parça kimlikleri dizisi `s = s₁…sₙ` ise, geçişten sonraki dosya ağacı `T` için `L(T) = s`. Lean'de `List` serbest monoidi üzerinde ifade edilir (`Ls = flatten ∘ map L`); zincir için `chain_L` ispatlı (yerel derleme).

## 2. Dönüşüm
Bir md dosyasının ortasından bir parça Lean'e kesildiğinde:
1. Kesimden önceki md parçası dosyada kalır.
2. Lean parçası `lean/Kanon/X.lean`'dir; bağlama `X.lean.md` symlink'i ile girer.
3. Kesimden sonraki md kuyruğu da ayrı bir dosyaya taşınır (yoksa Lean'den önce okunur).
4. Ebeveynin sonuna sırayla `@X.lean.md` ve `@kuyruk.md` yazılır (yelpaze, derinlik 1). Zincir de geçerli ama 4 sıçrama sınırına takılır; yelpaze tercih edilir.

Okuma rejiminde aynı ağaç, Rust genişleticisiyle (`@` satırını yerinde açan) tek akış olarak okunur. Bu, otomatik rejimle aynı sırayı vermez (satır içi ≠ ebeveyn-sonrası); bu yüzden dönüşümde `@` satırları her zaman dosyanın **sonunda** tutulur. Böylece iki rejim aynı sırayı üretir. Bu, kurulacak denetimin ana kuralıdır.

## 3. Kesim kuralı
Parça türüne göre: deterministik (girdi → karar, makine doğrular) → Rust icra (+ gerekiyorsa Lean spec) · koşullu kural/done-yüklemi → Lean · anlatı, gerekçe, üslup, değer → md. Knapsack/DP düştü (amaç fonksiyonu ölçülemez). Konum literatürü (Lost in the Middle, IFScale) eski kuşak ve belge-QA'dır; tasarım girdisi sayılmaz. Hook ile uyum %100 varsayılmaz; taşınan her kural için kanarya probu.

## 4. Maliyet olgusu
İçe aktarma bağlam maliyetini düşürmez (belge, iki yerde). Her oturumda yüklenen zincire bir Lean modülü eklemek her isteğe token ekler. Kök kanonlar kasten küçük (≤25/≤80 satır). Hangi Lean modülünün otomatik rejime, hangisinin okuma rejimine gireceği bir değer kararıdır.

## 5. Açık ölçüm borçları
`@` dedup (aynı dosya iki kez içe aktarılırsa) · 4 sıçramaya kök dahil mi · symlink'in `core.symlinks` kapalı klonlarda davranışı (bu makinede `true`).
