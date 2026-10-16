# Aile A: sıra korumanın matematiksel modeli + Lean ispatı (atlas-kosum, durum #18, 2026-10-16)

Koşucu: Sonnet işçi (tez ve antitez ayrı, bağımsız). Antiteze yalnız iddia listesi verildi (CoVe-Factored). Metin ajan dönüşlerinden aktarıldı, biçim sadeleştirildi.

## Tez raporu

**Özet:** Doğru model, rose tree üzerinde pre-order düzleştirmedir. Hedef yapı serbest monoid (List). Kesimden sonra özgün sırayı veren dönüşüm "kuyruk kaydırma"dır. Lean taslağı 4.35.0 ile derlendi (Mathlib yok).

İddialar:
1. Claude Code `@path` içe aktarmaları "ebeveyni başlatırken genişletilip bağlama yüklenir". Göreli yol içe aktaran dosyaya göre çözülür. Özyineleme en çok dört sıçrama. Backtick ve çit kod bloğu içindeki `@` atlanır. Satır içi mi sonda mı sorusunun cevabı belgede yok. · https://code.claude.com/docs/en/memory · AS-OF 2026-10-16 · açıldı
2. İçe aktarmalar bağlam maliyetini düşürmez ("imported files also load at launch"). · aynı URL · açıldı
3. Transclusion = başka belgeye atıfla dahil etme; Nelson, *Literary Machines* (1980). Kavramsal olarak satır içi yerleşim; ölçümle ters düşer. · https://en.wikipedia.org/wiki/Transclusion · açıldı (ikincil); Nelson kitabı açılmadı
4. noweb öbek sözdizimi `<<ad>>`; tangle/weave iç işleyişi ana sayfada yok. · https://www.cs.tufts.edu/~nr/noweb/ · açıldı, yetersiz
5. Tangle `<<ad>>` referansını o noktada açar (satır içi); weave kaynak sırasını korur. · kaynak yok, model hafızası · [?]
6. Lean 4 `List.flatten` listelerin listesini sırayı koruyarak birleştirir. · https://lean-lang.org/doc/reference/latest/Basic-Types/Linked-Lists/ · açıldı
7. Yerel `lean --version` = 4.35.0; taslak hatasız derlendi. · yerel koşum

Model karşılaştırması: rose tree pre-order düzleştirme önerildi (L(f) = metin(f) ++ L(i1) ++ … ++ L(ik)); serbest monoid homomorfizması hedef cebir (`Ls = flatten ∘ map L`); transclusion ve tangle satır içi olduğu için uymaz; linear extension gereksiz (pre-order DFS tek tam sıra verir).

Dönüşüm (kuyruk kaydırma): f0 = s1..sk + sonunda `@f1`; f1 = s(k+1)..sm + `@f2`; zincir. Değişmez: her düğümün metni kendi aralığının başındaki parçalar, çocuk alt ağaçlar sırayla kalanı kaplar. Kesimden sonraki md kuyruğu da ayrı dosyaya alınmalı.

Lean taslağı: `inductive Tree | node (txt : List Nat) (kids : List Tree)`; karşılıklı `Tree.L`/`Tree.Ls`; `theorem Ls_eq_flatten_map : Tree.Ls ks = (ks.map Tree.L).flatten`; `def chain`; `theorem chain_L : (chain cs).L = cs.flatten`.

Sınırlar: ebeveyn-sonrası davranış yalnız yerel ölçüme dayanır; Read rejimini kapsamaz; Knuth WEB/Org-babel/Xanadu birincil metinleri açılmadı.

## Antitez raporu

Açılan: code.claude.com/docs/en/memory · manpages.debian.org notangle.1 · orgmode.org Noweb-Reference-Syntax · TANGLE.WEB (xeroxparcarchive, kısmen) · yerel Lean 4.35.0. Açılamayan: tufts notangle.1.html 404, Knuth 1984 makalesi.

| # | Hüküm | Kanıt | URL |
|---|---|---|---|
| T1 rose tree pre-order | daraldı | "maximum depth of four hops" → derinlik ≤ 4. Düz `@` için dedup (ziyaret kümesi) doğrulanmadı; varsa model ağaç değil, ziyaret kümeli graf DFS'idir. | https://code.claude.com/docs/en/memory |
| T2 tangle satır içi, uymaz | çürütemedim, hafif daraldı | notangle: aynı adlı öbekleri birleştirir, girintiyi korur; Org: referans yerinde değiştirilir; WEB: aynı adlı modüller `text_link` ile sona eklenir. Referans ebeveynin son öğesiyse yerinde açma = ebeveynden sonra ekleme; Claude semantiği tangle'ın kuyruk-konumlu alt kümesi. | notangle.1 · orgmode · TANGLE.WEB |
| T3 kuyruk kaydırma tek dönüşüm | çürüdü | (a) 4 sıçrama sınırı zinciri en çok 5 dosyayla sınırlar. (b) Yelpaze: f0 = ilk parça + sonunda `@p2 @p3 … @pk` kardeş içe aktarmaları; derinlik 1, sıra korunur. (c) Ön-derleme (tangle) ile tek dosya: Read rejiminde de çalışır; bedel üretici + diff testi. (d) Üç yöntemin bağlam maliyeti aynı. | https://code.claude.com/docs/en/memory |
| T4 4 hop | çürütemedim | Birebir alıntı belgede. Kök dahil mi belirsiz. | aynı |
| T5 linear extension gereksiz | daraldı | Aynı hedef dizi için çok sayıda ağaç şekli var (tasarım uzayı eşdeğerlik sınıfı); `.claude/rules/` `paths` kuralları tembel yüklenir, sıra sabit değil; katmanlar arası sıra ayrı hiyerarşi. Tek `@` ağacında doğru, bağlamın tamamında değil. | aynı |
| T6 Lean ispatı Mathlib'siz | çürütemedim | Yerel 4.35.0'da `structure Node` + karşılıklı özyineleme ile `chain_L` hatasız derlendi. Genel ağaç teoremi kanıtlanmadı, yalnız zincir. | lean-lang.org v4.11.0 sürüm notu · Recursive-Definitions · yerel |

Açık: `@` dedup ölçümü; derinlik sayımında kök dahil mi.
