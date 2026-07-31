# Skill Fikir Kutusu

*(Ev kararı: Fable süzgeci 07-19, Katman 2 — K-019 boyut sigortası gereği ana fikir-kutusundan ayrı. Kural: aday buraya tek satır + pointer'la düşer; tam metin kaynak raporda. "Tekrarlayan-küme→skill" kuralı kanon ADAYI — imza masasında. Üretim kapısı: K-016 (tetik: K-015 DONE ya da Salih öne çeker); her skill eval'le doğar.)*

| # | Aday | Tetik-kalıbı | Öncelik | Kaynak | Statü |
|---|---|---|---|---|---|
| S-A | karar-modeli (3 model + karşıt-temel + defter bloğu) | "3 model / karar modeli" | YÜKSEK (07-17'de 2×) | `raporlar/2026-07-17-skill-fikri-kutusu.md` §3.1/§8.3 | **ÜRETİLDİ 07-19** (`.claude/skills/karar-modeli/`; eval 3/3; description-eval borcu açık) |
| S-B | atlas-kosum (alan-ailesi fan-out + V26 + sentez) | "araştır / atlas koştur" | YÜKSEK (07-17'de 6×) | aynı rapor §3.3 | **ÜRETİLDİ 07-19** (`.claude/skills/atlas-kosum/`; eval 3/3; ilk canlı koşum sahası bekliyor) |
| S-C | celiski-kapisi (kanon-tarama → çelişki+artı/eksi+plan) | yeni karar anı | ORTA | aynı rapor §2-C | **ÜRETİLDİ 07-21** (`.claude/skills/celiski-kapisi/`; eval 4/4; description-eval borcu açık) |
| S-D | lojik-çeviri (NL → ∧∨¬→↔; X∧Y→Z) | loop/kural tanımı | ORTA | aynı rapor §2-D | ADAY |
| S-E | damitma (katmanlı özüt + pointer koru + arşiv) | "damıt / ingest" | ORTA | aynı rapor §2-E | ADAY |
| S-F | vardiya-teslim (kapsül + teslim + git disiplini) | "teslim / kapat" | ORTA (kısmi: hizalama) | aynı rapor §2-F | ADAY |
| S-G | karar-hatti (bileşik: C→B→A→taslak; ince orkestratör; kayıt hat DIŞI) | "tam karar hattı" | K-016'da S-A sonrası | aynı rapor §3.2 + skill-nasil-olusturulur §5/§10 | **ÜRETİLDİ 07-22** (`.claude/skills/karar-hatti/`; eval 4/4; description-eval borcu açık) |
| S-H | seans-basla/bitir (CHECKLIST formunda; fiil-DSL dondu) | oturum aç/kapa | DÜŞÜK — destek-eşiği bekler | `raporlar/2026-07-18-seans-yasam-dongusu-senkron-skill.md` §4b | DONDURULDU-BEKLİYOR |
| S-I | sinav/grill (anlama-kapısı ölçüm geçişi; tez→sorgu→sert düzeltme) | YALNIZ Salih beyanı: "sınav / grill" — varsayılana gömülmez (V55 korunur, K3 hükmü 07-21) | ORTA | `raporlar/2026-07-21-grill-me-skill-arastirma.md` + senaryo-defteri 07-21/K3 | ADAY (K-016; Pocock kurulmaz, desen madenlenir — V25) |
| S-J | karar-kaydet (defter-bloğu yazım + commit; elle-tetik, `disable-model-invocation`) | yalnız Salih/vardiya-akışı tetiği | ORTA (S-G tamamlayıcısı) | S-G tasarım notu + skill-nasil-olusturulur §5 | ADAY |

Üretim standardı (K-016 açılınca): eval-önce akış · description = NE+NE ZAMAN+negatif-tetik · yan-etki = ayrı elle-tetik skill · <500 satır · çok-modelde test — `raporlar/2026-07-17-skill-nasil-olusturulur.md`.

## m.43 sayaçları (eşik altı — ≥3'te aday satırına döner)
- **ölçüm-aracı-yanıldı** — n=2: ① PowerShell 5.1 ANSI karakter sayımı (30-5, defter md.16) · ② Türkçe `İ` grep tuzağı (`grep -i` `İ`↔`i` eşlemiyor → yanlış-pozitif "terim kanonda yok" bulgusu; `cc/rapor-2026-07-30-25.md` P26/P29). Üçüncü vakada m.43 tetiklenir. Kayıt: 2026-07-31 onarım turu (Carvis).
- **kaçırılan-tetik** — sayım Katman-1'de (KG-25-3: 30-16 · 30-17 · 30-25 = 3 mü? Salih masasında; eşik dolduysa aday satırı oradan döner).

> **[K] ŞERH — 2026-07-31 (Carvis, öz-bildirim):** Bu dosya onarım turunda yanlışlıkla `cat >` ile ÜZERİNE yazıldı (ls çıktısı 20 satırda kesildiği için dosya yok sanıldı — "ölçüm-aracı-yanıldı" sınıfının ta kendisi, ama araç değil operatör hatası). Orijinal içerik commit'li kanondan (`git show HEAD:`) anında geri yüklendi, kayıp yok; bu bölüm sonradan eklendi. m.8 ihlal girişimi olarak kayda geçirildi.
