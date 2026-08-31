# Opus icra oturumu prompt'u — 2026-08-31 (derleyen: Carvis/Fable ana oturum)

*Salih bu dosyanın "PROMPT" bölümünü kopyalayıp yeni bir Claude Code oturumuna (model: Opus, effort: **medium**) yapıştırır. Çıktı ana oturuma (Fable) devir dosyasıyla döner; push ana oturumdan atılır.*

**Effort gerekçesi:** iş icra ağırlıklı — kararlar verilmiş, 7 görev emri hazır ve künyeli; Opus'un işi orkestrasyon + sentez, açık uçlu tasarım değil. High effort maliyeti artırır, sonucu değiştirmez (m.4 mantığı). İşçi-ajan bütçeleri emirlerde/aşağıda ayrıca kısıtlı (Salih 08-15 token kuralı).

---

## PROMPT (buradan aşağısını yapıştır)

seans başı jarvis geliştirme — İCRA YAN-OTURUMU (Opus). Kurallar önce:

1. **Yetki (m.41):** Sen yan-oturumsun; KARAR ALMAZSIN, kanona (core/, CLAUDE.md, tüzük, kapsül, pano) YAZMAZSIN. `git push` YASAK (m.9 — push ana oturumdan). Ana oturum (Fable) canlı → commit'lerde `git add <dosya-yolu>` kullan, `git add -A` YASAK (H4). Çelişki görürsen durup devir notuna yaz, kendin çözme.
2. **Token kısıntısı (Salih 08-15):** işçi-ajan bütçesi 10-15 araç çağrısı, effort low-medium, eşzamanlı ajan ailesi ≤ 3. Tek araç çıktısı >~10k token bağlama dökülmez → dosyaya yaz + pointer (KB-50).
3. **Koşum-önü manifest kapısı:** başlamadan `git log -15` + `veri/manifest/` oku — koşulmuş işi ikinci kez koşma. Her iş biriminin manifesti `veri/manifest/`e yazılır; kapı `tools/paralel-kapi.py` (kullanımı `tools/SCRIPTLER.md`). Ayak-izi çakışan birimler AYNI ANDA koşmaz.

**İş listesi (sıra ve kademe aşağıda; tüm emirler künyeli, oku ve aynen uygula):**

**Kademe 1 — firstmate pilotu (İB-59 ölçümü bu koşumdan; Karar 83 EK-2 onaylı):**
- `cc/gorev-2026-08-30-ib07-description-eval.md` — firstmate LİDER-ROLDE koştur.
- `cc/gorev-2026-08-30-ib09-yolc-v26-etki.md` — firstmate LİDER-ROLDE koştur.
- İkisinin ayak izi ayrıksa paralel (N=2), değilse sıralı. Her koşum için İB-59 ölçüm satırı bırak (lider-rol maliyet/kalite gözlemi).

**Kademe 2 — atlas beşlisi (araştırma; ayak-izi kuralları Karar 83):**
- `cc/gorev-2026-08-30-ib65-loop-pipeline-secim-atlas.md` ve `cc/gorev-2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md` — ayak izleri ayrık, paralel açılabilir (N=2).
- `cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md` + `cc/gorev-2026-08-31-ib68-urun-aday-envanteri.md` — ORTAK TARAMALI: tek tarama, iki rapor; birlikte tek birim olarak koş.
- `cc/gorev-2026-08-31-ib69-matris-kosum-atlas.md` — kendi içinde SIRALI 2 aile (emirde yazılı); K-020 girdisi. En sona bırak.
- Kademe ilkesi: N 1→2→3'ü aşma; bir birim bitmeden yenisini açarken paralel-kapi'den geçir.

**Teslim usulü (her birim için):**
- Rapor → `cc/rapor-2026-08-31-<konu>.md` (Türkçe, künyeli, her rakam kaynaklı, AS-OF damgalı — anakronizm freni Karar 68).
- Birim bitince manifest durumunu güncelle + karar başına ayrı `[icra]` commit (`git add <yol>`).
- H ≥ 7 çıktı (atıf/URL/DOI yoğun) → halüsinasyon-engelleyici zinciri (emirlerde eşik varsa o geçerli).

**Kapanış:** tüm birimler bitince (ya da bütçe/engel nedeniyle durunca) DEVİR DOSYASI yaz: `cc/devir-2026-08-31-opus-icra.md` — biten/kalan birimler, rapor yolları, commit sha'ları, İB-59 ölçüm özeti, açık sorular. Push ATMA; "devir hazır" de ve dur. Seans-kapanış ritüeli KOŞMA (o ana oturumun işi).

---

## Ana oturum (Fable) dönüş kontrol listesi
- [ ] Devir dosyası + raporlar okunur, çelişki kapısından geçirilir
- [ ] İB-59 ölçümü değerlendirilir (firstmate lider-rol pilotu)
- [ ] İB-69 çıktısı K-020 kartına bağlanır
- [ ] Commit'ler doğrulanır → push Salih beyanıyla
