# Aile B: sahadaki çözümler ve harness yükleme semantiği (atlas-kosum, durum #18, 2026-10-16)

Koşucu: Sonnet işçi (tez ve antitez ayrı, bağımsız). Antiteze yalnız iddia listesi verildi. Metin ajan dönüşlerinden aktarıldı. Yerel Claude Code 2.1.302.

## Tez raporu

(1) Claude Code resmi belgesi (https://code.claude.com/docs/en/memory, AS-OF 2026-10-16, açıldı):
1. `@path` içe aktarılan dosyalar "expanded and loaded into context at launch alongside the CLAUDE.md that references them"; göreli yol içe aktaran dosyaya göre.
2. "Imported files can recursively import other files, with a maximum depth of four hops."
3. İzinli uzantı listesi bulunamadı; `.lean` yüklenmemesi yalnız yerel ölçüm.
4. Satır içi mi sona mı: belge yazmaz.
5. Kod aralığı ve çit kod bloğu içindeki `@` atlanır.
6. "Imports … don't reduce its context cost, because imported files also load at launch."
7. Proje dışı içe aktarma onay ister; kullanıcı kapsamı onaysız.
8. Dosyalar kökten çalışma dizinine birleştirilir; `CLAUDE.local.md`, `CLAUDE.md`'den sonra.
9. Alt dizin `CLAUDE.md` tembel yüklenir.
10. `.claude/rules/*.md` `paths:` frontmatter ile koşullu.
11. Blok düzeyi HTML yorumları ayıklanır.
12. AGENTS.md v2.1.277+ doğrudan okunur (CLAUDE.md yoksa); `@AGENTS.md` çift okunmaz.
13. Windows'ta symlink yerine `@AGENTS.md` önerilir (`core.symlinks` kapalıysa symlink tek satırlık metin olur).
14. InstructionsLoaded: gözlem içindir, karar denetimi yok (https://code.claude.com/docs/en/hooks, kısmi okundu).
15. SessionStart `additionalContext` system-reminder içinde ilk istemden önce; 10.000 karakter üstü dosyaya.
16. SessionStart ekinin CLAUDE.md'ye göre sırası bulunamadı.

(2) Diğer araçlar: 17. AGENTS.md standardı include'suz (https://agents.md). 18. Gemini CLI `@file.md` içe aktarma, derinlik 5, satır içi görünüm çıkarımsal (memport.md). 19. Codex: dizin başına bir dosya, boş satırla birleştirme, 32 KiB sınır, include yok. 20. Cursor `.mdc`; `@file` "not inlined into the prompt". 21. Copilot `applyTo` glob, include yok. 22. Aider `--read`, include yok.

(3) Kod-talimat birleşimi: 23. Verso "Written in Lean. Checked by Lean." 24. doc-gen4 kod → HTML. 25. Org-babel noweb `<<NAME>>` yerinde açar. 26. WEB/CWEB tangle/weave (Wikipedia, ikincil). 27. Quarto include = kopyala-yapıştır.

Sonuç: satır içi transclusion yapanlar Quarto, Org-babel, WEB; Claude Code belgesi yerleşimi açmıyor; üçlüye en yakın model WEB tangle/weave ve Verso; hazır araç bulunamadı; Windows symlink riski yüzünden üretilmiş md daha güvenli.

## Antitez raporu

Açılan: memory (tam), hooks (0-200.000 / 270.831 karakter), Gemini `memoryImportProcessor.ts` (ham, 424 satır), Cursor, Codex, agents.md, Aider, VS Code Copilot, lean-lang.org Cedar.

| # | Hüküm | Kanıt | URL |
|---|---|---|---|
| T1 belge yerleşimi yazmaz | daraldı | AGENTS.md bölümü: `@AGENTS.md` en üstteyse "Claude reads the imported file first, then the rest" → belge import noktasında yerleşim izlenimi verir; yerel "ebeveynden sonra" bulgusuyla çelişir; çözüm yerel deney. | code.claude.com/docs/en/memory |
| T2 maliyet düşmez | çürütemedim | İki yerde ham alıntı; maliyeti düşüren mekanizmalar `paths:` kuralları, skill'ler, alt dizin CLAUDE.md. | aynı |
| T3 üretilmiş md daha güvenli | daraldı | Belgenin Windows çaresi `@AGENTS.md` içe aktarması, üretilmiş md değil; bu makinede `core.symlinks=true`; Edit/Write symlink üzerinden yazmayı reddeder. | aynı |
| T4 InstructionsLoaded yalnız gözler | çürütemedim | "no decision control … can't block or modify instruction loading"; `additionalContext` listesinde yok. | code.claude.com/docs/en/hooks |
| T5 SessionStart sırası belgesiz | çürütemedim | Sıra cümlesi okunan kısımda yok; son 70.831 karakter okunmadı. | aynı |
| T6 diğer araçlarda include yok | daraldı | Copilot (VS Code): Markdown bağı ve `chat.includeReferencedInstructions` ayarı var. | code.visualstudio.com/docs/copilot/customization/custom-instructions |
| T7 Gemini satır içi (kesin değil) | çürütemedim, doğrulandı | `memoryImportProcessor.ts` satır 327/365/379: `@yol` yerinde değiştirilir; varsayılan `tree`, `maxDepth: 5`; CLI'nin modu seçimi doğrulanmadı. | raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/utils/memoryImportProcessor.ts |
| T8 üçlüyü sunan hazır araç yok | çürütemedim (iki bacak hazır) | Cedar (AWS): Lean modeli + üretim Rust + diferansiyel test, "No new Cedar version is released unless its model, proofs, and differential tests are current"; Aeneas/Charon/hax ters yön (Rust → Lean). | lean-lang.org/use-cases/cedar · arXiv 2407.01688 · arXiv 2605.30106 |
