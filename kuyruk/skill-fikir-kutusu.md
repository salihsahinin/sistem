# Skill Fikir Kutusu

*(Ev kararı: Fable süzgeci 07-19, Katman 2 — K-019 boyut sigortası gereği ana fikir-kutusundan ayrı. Kural: aday buraya tek satır + pointer'la düşer; tam metin kaynak raporda. "Tekrarlayan-küme→skill" kuralı kanon ADAYI — imza masasında. Üretim kapısı: K-016 (tetik: K-015 DONE ya da Salih öne çeker); her skill eval'le doğar.)*

| # | Aday | Tetik-kalıbı | Öncelik | Kaynak | Statü |
|---|---|---|---|---|---|
| S-A | karar-modeli (3 model + karşıt-temel + defter bloğu) | "3 model / karar modeli" | YÜKSEK (07-17'de 2×) | `raporlar/2026-07-17-skill-fikri-kutusu.md` §3.1/§8.3 | **ÜRETİLDİ 07-19** (`.claude/skills/karar-modeli/`; eval 3/3; description-eval borcu açık) |
| S-B | atlas-kosum (alan-ailesi fan-out + V26 + sentez) | "araştır / atlas koştur" | YÜKSEK (07-17'de 6×) | aynı rapor §3.3 | **ÜRETİLDİ 07-19** (`.claude/skills/atlas-kosum/`; eval 3/3; ilk canlı koşum sahası bekliyor) |
| S-C | celiski-kapisi (kanon-tarama → çelişki+artı/eksi+plan) | yeni karar anı | ORTA | aynı rapor §2-C | ADAY |
| S-D | lojik-çeviri (NL → ∧∨¬→↔; X∧Y→Z) | loop/kural tanımı | ORTA | aynı rapor §2-D | ADAY |
| S-E | damitma (katmanlı özüt + pointer koru + arşiv) | "damıt / ingest" | ORTA | aynı rapor §2-E | ADAY |
| S-F | vardiya-teslim (kapsül + teslim + git disiplini) | "teslim / kapat" | ORTA (kısmi: hizalama) | aynı rapor §2-F | ADAY |
| S-G | karar-hatti (bileşik: C→B→A→kaydet; context:fork orkestratör; kayıt AYRI `disable-model-invocation` skill) | "tam karar hattı" | K-016'da S-A sonrası | aynı rapor §3.2 + skill-nasil-olusturulur §5/§10 | ADAY |
| S-H | seans-basla/bitir (CHECKLIST formunda; fiil-DSL dondu) | oturum aç/kapa | DÜŞÜK — destek-eşiği bekler | `raporlar/2026-07-18-seans-yasam-dongusu-senkron-skill.md` §4b | DONDURULDU-BEKLİYOR |
| S-I | sinav/grill (anlama-kapısı ölçüm geçişi; tez→sorgu→sert düzeltme) | YALNIZ Salih beyanı: "sınav / grill" — varsayılana gömülmez (V55 korunur, K3 hükmü 07-21) | ORTA | `raporlar/2026-07-21-grill-me-skill-arastirma.md` + senaryo-defteri 07-21/K3 | ADAY (K-016; Pocock kurulmaz, desen madenlenir — V25) |

Üretim standardı (K-016 açılınca): eval-önce akış · description = NE+NE ZAMAN+negatif-tetik · yan-etki = ayrı elle-tetik skill · <500 satır · çok-modelde test — `raporlar/2026-07-17-skill-nasil-olusturulur.md`.
