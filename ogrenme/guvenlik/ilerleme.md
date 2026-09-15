# guvenlik serisi — ilerleme (Karar 94 EK-3; açılış tetiği "seans başı, guvenlik")

| G | Durum | Tarih | Ders kaydı | Sapma / not |
|---|---|---|---|---|
| G1 | DONE (kavramsal + pratik) | 2026-09-14/15 | `dersler/2026-09-14-g1-prompt-injection-i.md` + `g1-injection-seti/` | 8/8 kutu doğru. **Pratik (Salih eli, 09-15):** Salih `npx promptfoo@latest eval -c promptfooconfig.yaml --output son-kosum.json` komutunu kendi koştu (10 vaka, kendi OAuth kimliği) → 9/10 PASS, tek FAIL = Vaka 5, referans koşumla (assertion-ASR=0,10, davranışsal-ASR=0,00) birebir örtüştü — sapma yok. Salih onayıyla DONE. Vaka 5 G6 regresyon adayı (bkz. basarisizlik-analizi.md). |
| G2 | DONE (kavramsal) | 2026-09-15 | `dersler/2026-09-15-g2-lethal-trifecta-en-az-yetki.md` | 8/8 kutu doğru (kutu 1'de 2. denemede). Sektör terimleri canlı teyit: lethal trifecta (Willison), dual-LLM/CaMeL (DeepMind 2025), Rule of 2 (Chromium). Pratik düğümü yok (bu ders salt kavramsal — G1'deki gibi ayrı bir koşum aracı yok). |
| G3 | — | | | |
| G4 | — | | | |
| G5 | — | | | |
| G6 | — | | | |
| G7 | — | | | |

Sonraki: G3.
