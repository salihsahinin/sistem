# Planlanmış Optimize Etme Fikirleri (POP)

*(Ev kararı: Fable süzgeci 07-19, Katman 2. Şema: her madde = tetik-koşulu · C_carry (taşıma maliyeti: >0 = beklerken faiz işler, ≈0 = saf opsiyon/bedava bekler) · Durum {deferred · armed · triggered · dropped}. Tetik = elle beyan (otomatik-eşik ölçüm-altyapısı sonrası). Budama = m.37 yakınsama; drop ≠ sil (m.8). Tam gerekçeler: `raporlar/2026-07/2026-07-18-planlanmis-optimizasyon-fikirleri.md`.)*

| # | Optimizasyon | Tetik | C_carry | Durum |
|---|---|---|---|---|
| O1 | Otonomi merdiveni derinliği | Salih K-009 beyanı | ≈0 | **TRIGGERED→KAPANDI 07-19** (m.30 ek fıkrası) |
| O2 | Ses PoC → tam ses | L2 köprü DONE + Salih "başla" | ≈0 | armed (sıra kararı 07-19: köprü sonrası) |
| O3 | Kararlar-konsolu dashboard | karar-hacmi eşiği | ≈0 | deferred |
| O4 | PreToolUse + SessionStart hook | ilk gözetimsiz dilim ÖNCESİ | >0 (her gün talimat-riski) | **ARMED — Dilim 1'de (07-19 Karar 2)** |
| O5 | Yakınsayan formül (Contextual-TS/BOHB) | defter verisi + K-020 | ≈0 | deferred |
| O6 | Durağan-olmama düzeltmesi | O5 canlı + kayma | ≈0 | deferred |
| O7 | 4-facet kategorizasyon | skill-kutusu düz-uzayda yavaşlayınca | ≈0 | deferred |
| O8 | Geri-alınabilirlik alanı + öncelik | karar-hacmi | ≈0 | **TRIGGERED-KISMEN 07-19** (alan deneysel canlı; formüller A7'de) |
| O9 | karar-hatti bileşik skill + eval | K-016 açılış | ≈0 | armed |
| O10 | desirability + regret-eğrisi ölçümü | ilk V39/K-020 koşumu | ≈0 | deferred |
| O11 | Meta-öğrenme (L2O) | uzun-vade veri hacmi | ≈0 | deferred |
| O12 | A7 matematiksel-temel denetimi | iş kapanışları | >0 (sezgisel eşik birikir) | armed |
| O13 | Modern-tokenizer kesin ölçümü | öğrenme P2+ | ≈0 | armed (P2 koşuyor) |
| O14 | K-019 kutu-damıtma + boyut-izleme | ilk boş seans | >0 (kutu şişiyor) | armed |
