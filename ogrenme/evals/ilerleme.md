# evals serisi — ilerleme (Karar 94 M2; açılış tetiği "seans başı, evals")

| H | Durum | Tarih | Ders kaydı | Sapma / not |
|---|---|---|---|---|
| H1 | `DONE` | 2026-09-11 | `dersler/2026-09-11-H1-eval-nedir.md` · `h1-eval-seti/` (20 vaka, GSM8K, KAYNAK.md) | promptfoo koşumu: 18/20 `PASS` (%90); pass@1=c/n=18/20=0,90 (kutu 8 formülüyle tutarlı). İlk koşumda `eval-seti.yaml`'da yanlışlıkla ikinci bir `tests:` sarmalayıcısı vardı (promptfoo dosyanın doğrudan liste olmasını bekliyor) — düzeltildi (commit efcc40a). Ayrıca Claude Code OAuth kimliği süresi dolmuştu, `claude /login` ile tazelendi. |
| H2 | `DONE` | 2026-09-11 | `dersler/2026-09-11-H2-deterministik-kontroller.md` · `h2-eval-seti/` (21 vaka: contains/regex/equals+1 kırmızı) | 18/21 `PASS` (%85,71): kırmızı vaka beklendiği gibi `FAIL` + Josh/Carlos hataları (H1'den) farklı prompt/assert'le **aynen** tekrar çıktı → tesadüf değil, gerçek regresyon adayı doğrulandı |
| H3 | `DONE` | 2026-09-14 | `dersler/2026-09-11-H3-llm-as-judge-1.md` · `h3-eval-seti/` (AKIS.md, elle-puanlama.md, yargic-sonuc) | κ=1,0 (n=10, 10/10 tam uyum, Salih ile yargıç aynı 2 vakada — Carlos, trenler — hemfikir). Josh vakası bu kez doğru çıktı (stokastiklik); trenler yeni hata adayı, teyitsiz |
| H4 | — | | | |
| H5 | — | | | |
| H6 | — | | | |
| H7 | — | | | |

Sonraki: H4. **DURAKLATILDI 09-14 (Salih: başka konuya geçiş); H4-H7 açık, ürün turu H7'de.**
