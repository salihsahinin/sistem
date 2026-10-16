# Aile C: kesim noktası seçimi ve maliyet (atlas-kosum, durum #18, 2026-10-16)

Koşucu: Sonnet işçi (tez ve antitez ayrı, bağımsız). Antiteze yalnız iddia listesi verildi. Metin ajan dönüşlerinden aktarıldı.

## Tez raporu

Erişim: 5 arXiv sayfası açıldı (4 özet, 2 gövde); Lost in the Middle PDF ikili geldi, rakamlar ar5iv HTML'den. Bellman/knapsack/TextTiling kaynakları açılmadı.

1. Uzun bağlamda ilgili bilgi baş/sonda iken performans en yüksek, ortada düşer. · https://arxiv.org/abs/2307.03172 · 2023 (TACL) · açıldı
2. GPT-3.5-Turbo, 20 belge QA: 1. sırada %75.8, ortada %53.8, sonda %63.2; closed-book %56.1. · https://ar5iv.labs.arxiv.org/html/2307.03172 · açıldı (araç özeti)
3. Sorguyu verinin önüne ve arkasına koymak key-value retrieval'da neredeyse mükemmel; çoklu belge QA'da etkisi minimal. · aynı · açıldı
4. Hipotez: talimat ince-ayarı başı ağırlıklandırıyor olabilir; temel model MPT-30B de U gösteriyor. · aynı · açıldı
5. IFScale: 20 model, 500 talimat; en iyi model %68. · https://arxiv.org/abs/2507.11538 · 2025-07 · açıldı
6. IFScale (10/100/250/500): gemini-2.5-pro %100/98.4/84.8/68.9; o3 %100/98.2/97.8/62.8; claude-3.7-sonnet %100/94.8/72.9/52.7. · https://arxiv.org/html/2507.11538 · açıldı
7. Üç bozulma deseni: eşik, doğrusal, üstel. · aynı
8. Primacy oranı orta yoğunlukta tepe, 300+ talimatta ~1.0-1.5; claude-3.7-sonnet 2.67/1.77/1.39. · aynı
9. Kod biçimli prompt koşullu akıl yürütmede GPT-3.5'te +22.52, Mistral +16.78, Mixtral +7.75. · https://arxiv.org/abs/2401.10065 · 2024 · açıldı (özet)
10. Prompt biçimi GPT-3.5'te %40'a kadar fark. · https://arxiv.org/abs/2411.10541 · açıldı
11. IFEval: 25 tür doğrulanabilir talimat, ~500 prompt; programla doğrulama. · https://arxiv.org/abs/2311.07911 · açıldı
12. md vs Lean/kod spec ajan uyumunu doğrudan karşılaştıran ölçüm bulunamadı (5 kaynakla sınırlı).

Öneri: sınıflandırma (D deterministik → Rust/Lean, K koşullu → Lean, A anlatı → md) → maliyet (t_i token, L_i yüklenme, R istek sayısı) → kök için 0/1 knapsack (bütçe 80 satır/7 KB) → bitişik aralıklarla O(n²) DP segmentasyon (geçiş cezası λ) → isteğe bağlı konum ayarı (sıra korumayla çelişir) → IFEval tarzı md-only vs md+Rust doğrulama. Konum bulgusu "sırayı koru" hedefini doğrudan desteklemez; sıra bir ayar parametresidir, korumak bilinçli ödünleşim.

## Antitez raporu

Açılan: arXiv 2307.03172 (PDF metni), 2507.11538 (HTML), 2401.10065 (HTML, son ~24K karakter okunmadı), 2508.07479 (abs), Chroma Context Rot. İkincil: GitHub/claudeissues, SOPBench/FASTRIC arama özetleri.

| # | Hüküm | Kanıt | URL |
|---|---|---|---|
| T1 LiM rakamları | çürütemedim; kapsam daraldı | PDF: 75.8/57.2/53.8/55.4/63.2, closed-book 56.1. Yalnız GPT-3.5 (2023); Claude-1.3 neredeyse düz (59.9/55.9/56.8/57.2/60.1); görev belge-QA. | https://arxiv.org/abs/2307.03172 |
| T2 IFScale | daraldı | Rakamlar doğru (gemini 68.9, özet 68). Primacy düşük yoğunlukta ~0, 150-200'de tepe, 300+'da kaybolur; "sonraki talimat daha sık ihlal" genellemesi çöker. ≤80 satır kök %100 bölgesinde. | https://arxiv.org/html/2507.11538 |
| T3 kod biçimi +22.52 | daraldı (güçlü) | Yalnız GPT-3.5 BGQA-3 (50.29 vs 27.77 F1); CondQA'da kod kaybediyor; LLaMA-2 7B'de kazanç yok; GPT-4 test edilmedi. 2407.08440: NL kurallar formal FOL'dan çoğu zaman iyi (özet). | https://arxiv.org/html/2401.10065 · https://arxiv.org/pdf/2407.08440 |
| T4 doğrudan ölçüm yok | çürütemedim; "yoktur" yerine "bulamadık" | SOPBench (kod oracle vs NL), FASTRIC (NL içinde FSM; ters-U) dolaylı, sonuç karışık; tam metin açılmadı. | https://arxiv.org/pdf/2503.08669 · https://arxiv.org/html/2512.18940v1 |
| T5 U-şekil 2025-26'da geçerli | daraldı | Veseli vd. 2025: LiM pencerenin ~%50'sine kadar; sonra recency. Chroma (18 model): NIAH'ta konum varyasyonu yok; Repeated Words'te primacy. U evrensel değil. | https://arxiv.org/abs/2508.07479 · https://www.trychroma.com/research/context-rot |
| T6 DP + knapsack en uygun | çürüdü | Amaç fonksiyonu ölçülmemiş, λ ve değerler keyfi; kök bütçesinde n küçük, açgözlü ≈ knapsack; daha basit: kural kural sınıflandır, sınıfa göre taşı, sırayı pointer ile koru. (Mantıksal argüman, kaynak yok.) | — |
| T7 Rust hook = %100 uyum | çürüdü | claude-code issue #63786 (Bash ile Write/Edit hook'u aşıldı), #29709, #14493, #69970 (v2.1.176 Bash PreToolUse sessizce çalışmadı), #20946 (bypass modu). Kanarya probu önerilir. Sayfalar tek tek açılmadı. | claudeissues.com/issue/63786 · github.com/anthropics/claude-code/issues/29709 · claudeissues.com/issue/69970 · /14493 · /20946 |
