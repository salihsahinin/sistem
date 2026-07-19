# K-009 İcra Sırası — birleşik kuyruk (2026-07-19)

*(Salih emri: raporlardaki yapılacak/incelenecek kalemleri mevcut işlem sırasına optimize entegre et. Sıralama ölçütü: bağımlılık > geri-alınabilirlik/güvenlik (G4<G5) > kaldıraç. Kaynaklar: K-009 gündemi + rapor 1/3/7/10/12 + süzgeç 07-19.)*

**Dilim 0 — bugün, masada:**
0.1 ~~m.42 imzası~~ **DONE 07-19** (tüzüğe girdi).
0.2 Ev dosyaları AÇILDI ✓ (skill-kutusu · POP · icra-sırası — bu commit).
0.3 PC senkron `/goal` (2 dk) — Salih terminali.

**Dilim 1 — ilk otomasyon paketi (Karar 1+2 imzalı; hepsi iki-yönlü kapı):**
1.1 ~~PreToolUse kilidi yazımı~~ **KURULDU 07-19** (.claude/settings.json permissions-deny; TEST Salihin ilk CC oturumunda — deneysel m.29).
1.2 ~~SessionStart hook + banner + CLAUDE.md satırı~~ **KURULDU 07-19** (.claude/hooks/session-start.sh; **TEST PASS 07-19**).
1.3 ~~Kararlı-prefix kapsamı~~ **KARAR 07-19:** sınıf = koşum deseni (TTL-içi aynı-önek tekrarı; rol farketmez); interaktif kapsül-önce kalır.
1.4 ~~JSONL usage-log asgarisi~~ **AÇILDI 07-19** (`raporlar/usage/` + şema; ilk müşteri senkron scripti).
1.5 ~~Gecelik senkron m.37 koşumu~~ **KARAR+KURULUM 07-19:** A+C aşısı (LLM'siz ff-only script, `tools/gece-senkron.ps1`); kalan: schtasks kaydı (Salih, tek komut — script başında yazılı) + ilk gece gözlemi.

**Dilim 2 — köprü + ses (Karar 3 sırası):**
2.1 ~~L2 mobil-köprü protokolü~~ **YAZILDI 07-19** (KILAVUZ §Mobil Köprü Protokolü; deneysel m.29).
2.2 Ses PoC: niyet-yakalama/triyaj kapsamı, ölçümlü (WER+gecikme+görev-başarı → defter) — O2. **BAŞLADI 07-19 (ikinci günaydın): kanal = Model A (telefon diktesi + mobil köprü, defter bloğu); protokol KILAVUZ §Mobil Köprü'ye SES-POC eki ile; toplama PASİF (Salih emri: ayrı test oturumu yok, doğal kullanımda birikir); ölçüm tetiği Salih beyanı.**

**Dilim 3 — skill hattı (K-016; tetik Salih'te — "skill araştırmasına geleceğiz" 07-19):**
3.1 K-016 açılış kararı + ilk skill: S-A karar-modeli (eval-önce akış) → S-B atlas-kosum → S-G karar-hatti. **S-A + S-B ÜRETİLDİ 07-19 (ikinci günaydın): `.claude/skills/karar-modeli/` (SKILL.md + temeller + defter-şablonu + evals); A/B eval 3/3 PASS, baseline'a fark = kontrat-uyumu (grading dosyası); açık borç: 20-sorgu description eval + çok-model test + CC saha tetiklemesi. S-B `atlas-kosum` aynı akışla (eval 3/3; antitez=¬ şerhi gömülü); sırada S-G karar-hatti orkestratörü.**
3.2 ~~"Tekrarlayan-küme→skill" kuralı imzası~~ **DONE 07-19 (m.43, günaydın vardiyası).**
3.3 Madenleme pilotu (rapor 8; küçük, elle-tetik).

**Dilim 4 — tetikli/bekleyen:**
4.1 Gece-araştırma tek-atış pilotu (PreToolUse-sonrası; sert-bütçe+tur-tavanı freni) — rapor 12.
4.2 İmza-masası kalemleri #2-#6 (tüzük oturumu; süzgeç raporu listesi).
4.3 Kitap kararı (PI önerisi) — Salih, acele yok.
4.4 K-019 boş vardiya (O14) · K-010 tasarım paketi (held-out şartlı, rapor 15) — kendi tetiklerinde.
