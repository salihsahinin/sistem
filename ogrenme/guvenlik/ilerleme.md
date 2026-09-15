# guvenlik serisi — ilerleme (Karar 94 EK-3; açılış tetiği "seans başı, guvenlik")

| G | Durum | Tarih | Ders kaydı | Sapma / not |
|---|---|---|---|---|
| G1 | kavramsal DONE · pratik KALAN (Salih eli) | 2026-09-14/15 | `dersler/2026-09-14-g1-prompt-injection-i.md` + `g1-injection-seti/` | 8/8 kutu doğru. **Pratik düzeltme (Salih 09-15):** Jarvis'in promptfoo koşumu REFERANS koşumdur, Salih uygulaması yapılmadı → pratik KALAN; Salih `g1-injection-seti/` komutunu kendi koşar, sonucu referansla karşılaştırır. Referans: 10 vakalık promptfoo koşumu, assertion-ASR=0,10 ama davranışsal-ASR=0,00 (vaka 5 yanlış-pozitif, bkz. basarisizlik-analizi.md) — G6 regresyon adayı. |
| G2 | — | | | |
| G3 | — | | | |
| G4 | — | | | |
| G5 | — | | | |
| G6 | — | | | |
| G7 | — | | | |

Sonraki: G1 pratik (Salih eli: `cd ogrenme/guvenlik/g1-injection-seti && npx --yes promptfoo@latest eval -c promptfooconfig.yaml`), sonra G2 (Lethal trifecta + en-az-yetki; ayrı sohbet; ogren v0.1 iskeleti: PROBE → PLAN DAG → TEACH kutu → CLOSE; sektör başlıkları ders başında canlı teyit).
