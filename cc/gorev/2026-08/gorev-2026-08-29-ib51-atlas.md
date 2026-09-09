# CC Görev Emri — 2026-08-29 İB-51 atlas: kural yükleme mekanizması (yol-kapsamlı kural ↔ sınıflayıcı hook)

**Künye:** yol `cc/gorev-2026-08-29-ib51-atlas.md` · HEAD 6a975f5 (emir yazım anı) · emir sahibi Carvis (yan icra oturumu, Fable; Salih: "hükümler başka oturumda, kalan icra borçlarından sırayla koş") · İB-51 (3) — Karar 74 M-7 tetiği · skill `atlas-kosum` (m.40b v0.2) · rejim: manuel-tempo · kota-bol · ekonomi −%30 (08-15) · AS-OF 2026-08-29.

## Soru
Jarvis'in kural yükü ölçüldü (`raporlar/2026-08-29-ib51-kural-envanteri.md`: 1.017 kural birimi, 49 taşıyıcı; seans tabanı 71 birim; 9 görev sınıfı). Sorun: her kural her konuşmada yüklenmesin, görev sınıfına uygun alt-küme yüklensin. Aday mekanizmalar (rapor §4): (a) deterministik sınıflayıcı hook (istemi anahtar-kelimeyle sınıflar, pointer satırı enjekte eder) · (b) sınıf-skill'leri · (c) SessionStart brif tablosu · (d) yol-kapsamlı kural dosyaları (dizin/glob tetikli). **Atlas sorusu:** (d) Claude Code'da canlı ve belgeli mi, tetik semantiği ne (hangi dosyaya dokununca yüklenir, ne zaman düşer), bağlam maliyeti nasıl ölçülür; (a)'nın yerine geçer mi, ikisi birleşir mi? Dış emsaller ve kural-yükleme maliyeti/uyum ölçümleri ne diyor?

## Aileler (dik)
- **A — Claude Code yerli mekanizmaları:** yol-kapsamlı kural dosyaları (`.claude/rules/` ve `paths:` frontmatter ya da eşdeğeri) · alt-dizin `CLAUDE.md` yükleme semantiği · hook çıktısıyla bağlam enjeksiyonu (`UserPromptSubmit`/`PreToolUse` additionalContext) · skill description bütçesi. Hedef: resmî belge (code.claude.com/docs), sürüm/tarih damgalı; hangi mekanizma deterministik tetiklenir (kod) hangisi model seçer (skill).
- **B — Dış emsaller + ölçüm:** Cursor Rules (`globs`, `alwaysApply`), GitHub Copilot custom instructions (`applyTo`), Windsurf/Cline/Aider kural dosyaları; kural sayısı ↔ uyum ölçümleri (IFScale sınıfı), bağlam-maliyeti (token) raporları. Hedef: tetik semantiği tablosu + ölçülmüş maliyet/uyum rakamları.

## Çıktı disiplini (zorunlu)
Her iddiaya URL (birincil: resmî docs / standart / arXiv / GitHub) · her iddia AS-OF damgalı (kaynağın tarihi ∨ çekim tarihi; Karar 68) · rakam kaynaklı, kestirimse `[?]` · UYDURMA YASAK, "bulunamadı"/"[ARANAMADI]" meşru · erişim engeli (403/paywall) bayraklanır · etiket D/K/X · bütçe 10-15 dış erişim (WebFetch/WebSearch), bilinen birincil kaynağa DOĞRUDAN git · repoya dosya YAZMA, alt-ajan AÇMA · karar ALMA — kanıt getir. Çıktı: yapısal madde listesi (iddia · etiket · URL · AS-OF); sonunda "SON ÜÇTE BİR" bölümü ayrıca ≥1 kaynaklı iddia içerir (V26 örneklem kuralı).

## Bütçe
Aile başına 1 tez (Sonnet, effort düşük, ≤15 dış erişim) → 2 antitez (CoVe-Factored: yalnız iddia listesi) → V26 (Carvis) → hakem (Carvis, maskeli). Rapor `raporlar/2026-08-29-ib51-atlas-kural-yukleme.md`.
