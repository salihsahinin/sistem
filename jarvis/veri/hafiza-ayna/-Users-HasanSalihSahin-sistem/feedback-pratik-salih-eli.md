---
name: pratik-salih-eli
description: Öğrenme pratiği Salih'in elidir; Jarvis'in kendi koşumu pratik sayılmaz, `DONE` yalnız Salih beyanıyla (09-15 G1 arızası)
metadata:
  type: feedback
---

Salih 09-15: güvenlik G1'de "pratiği sürdürelim" emri üzerine Sonnet yan oturum 10 vakayı yazdı, promptfoo'yu kendi koştu, analiz etti ve ilerleme tablosuna G1 `DONE` yazdı; Salih tek satır ("login yaptım, koşumu tekrar dene") yazmıştı. Salih: "pratik aşamasını yapmadığımız halde pratik yapıldı saydı."

**Why:** Öğrenme iskeletinde (ogren, [[ogretim-iskeleti-ogren-sektor-basligi]]) "şimdi sen dene" adımı Salih'in yapması için var; model koşarsa öğrenme olmaz, üstelik sonraki turda model kendi yazdığı DONE'u okuyup konuyu atlar.

**How to apply:** Pratik düğümünde Jarvis iskeleyi (config, şablon, tek komut) hazırlar, komutu Salih koşar, çıktıyı Jarvis yorumlar. Jarvis'in koşumu = "referans koşum". İlerleme/ders dosyasına `DONE` yalnız Salih "yaptım" dediğinde. Kural `.claude/skills/ogren/SKILL.md` §3 + Gotchas.
