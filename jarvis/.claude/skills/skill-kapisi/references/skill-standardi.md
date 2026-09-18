# Skill Standardı (skill-kapisi referansı)

> **Taşınma (İB-92, Karar 96 M2 A5, 2026-09-15):** bu metin `KILAVUZ.md`'den aynen taşındı (m.8: silme yok, KILAVUZ'da pointer kaldı); kural kaynağı yine tüzük/karar numaraları, burada yalnız gövde. Skill üretimi/evrimi sırasında `skill-kapisi` K1/K3 kapılarında okunur. Büyük-harf = kod kuralı (Karar 97) uygulanmış hâl.

## Kaynak başlık: Skill Standardı (K-016 açılışı 07-19; el kitabı: `raporlar/2026-07/2026-07-17-skill-nasil-olusturulur.md` — burası özet, çelişkide rapor + code.claude.com/docs kazanır)
- **Eval kuralı (Salih onayı 07-12; revizyon Salih imzası 07-23 — kaynak `cc/rapor/2026-07/rapor-2026-07-23-1.md`):** her JARVIS skill'i eval setiyle doğar. Küçük-N eval = **SMOKE/regresyon-kanaryası, sertifika değil** — çıplak "%100 geçti" raporu **yasak**; sonuç aralığıyla (Clopper-Pearson: 6/6→[%54,%100]) ya da "smoke-only" ibaresiyle verilir. Yeni setlerde: negatif ~10 (pariteye yaklaş — 3 negatif yanlış-pozitifi bağlamaz) + her vaka ≥3× koşum (non-determinizm ilacı; vaka eklemekten ucuz). 20-sorgu description-eval skill-creator protokolüne **tam** hizalı: 8-10 should + 8-10 should-not · her sorgu 3× · 60/40 held-out · ≤5 iterasyon. Mevcut skill'lere geriye dönük eval soğuk kuyrukta. *(md.22 pozitif karşılığı fiilen bu maddede tanımlı — aralıkla ya da smoke-only ibaresiyle ver; imza kaydı 08-20 KB-28.)*
- **Eval-önce akış:** önce ≥3 senaryoluk `evals/evals.json` + baseline (skill'siz koşum), **sonra** minimal gövde; description ince-ayarı EN **son**. Eval'siz yayın `YOK`.
- **Description:** 3. şahıs · NE + NE **zaman** (gerçek kullanıcı ifadeleriyle) + **negatif** tetik ("X'te kullanma") · ≤1024 karakter.
- **Gövde:** <500 satır · emir-kipli numaralı adım · tek sorumluluk · "Gotchas" bölümü en yüksek sinyal · detay `references/` (bir seviye derin).
- **Yan-etki freni (★):** kayıt/commit/deploy adımı **ayrı** `disable-model-invocation: true` skill'e — muhakeme skill'i blok **üretir**, dosyaya **yazmaz** (m.31/m.9 koda gömülü).
- **Kompozisyon:** skill'ler birbirini literal çağırmaz; bileşik iş = `context: fork` orkestratör + küçük çocuk skill'ler + sabit-format handoff + fail-loud.
- **Yayın-öncesi:** 20-sorgu description eval (10 tetiklemeli + 10 tetiklemesiz) · çok-modelde test · versiyon damgası (`0.x-deneysel-m29`).
- **Ev:** `.claude/skills/<ad>/SKILL.md` (repo, git'e commit — dağıtım gece-senkron/pull ile).
- **Hazine tavanı kalktı (Karar 96, Salih 09-15):** char/adet tavanı ve "yeni skill = emekli-aday" kuralı süpersede; yönetim = seçim-isabeti (description standardı · katalog `.claude/skills/README.md` · tetiklenme isabeti ölçümü). Şema `core/skill-uretim-semasi.md` §4b.
