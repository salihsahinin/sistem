# İB-51 atlas — TEZ aile B (dış emsaller + ölçüm) — ham işçi çıktısı (Sonnet, effort düşük; 15/15 dış erişim; 2026-08-29)

Künye: emir `cc/gorev-2026-08-29-ib51-atlas.md` · HEAD 6a975f5 eşleşti.

B-1. Cursor kuralları `.cursor/rules/*.mdc` uzantısıyla saklanır; düz `.md` yok sayılır. K · https://cursor.com/docs/context/rules · AS-OF 2026-08-29 (çekim).
B-2. Cursor 4 kural türü: Always Apply (`alwaysApply:true`) · Apply Intelligently (`description` var, `globs` yok — ajan karar verir) · Apply to Specific Files (`globs`) · Apply Manually (`@`). K · aynı URL.
B-3. Copilot `.github/instructions/*.instructions.md` `applyTo` glob'u eşleşince otomatik; örnek `applyTo: "app/models/**/*.rb"`, çoklu desen virgülle. D · https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions · AS-OF 2026-08-29.
B-4. Copilot `excludeAgent: "code-review"` alanıyla belirli ajanlar hariç tutulabilir. D · aynı URL.
B-5. docs.windsurf.com/windsurf/cascade/memories → 307 → docs.devin.ai/desktop/cascade/memories ("Devin Desktop"). D · AS-OF 2026-08-29.
B-6. Cognition, Windsurf'ü 2 Haziran 2026'da "Devin Desktop" olarak yeniden markaladı. K · https://news.creeta.com/en/windsurf-renamed-devin-desktop-2026/ (ikincil).
B-7. Devin Desktop kural `trigger` değerleri: always_on · model_decision · glob · manual. D · https://docs.devin.ai/desktop/cascade/memories.
B-8. Devin Desktop sınırlar: global_rules.md ≤6.000 karakter · .devin/rules/*.md ≤12.000 karakter/dosya. D · aynı URL.
B-9. Eski `.windsurf/rules` geriye-uyumlu okunur; tercih `.devin/rules`. K · aynı URL.
B-10. Cline `.clinerules/` frontmatter'sız dosyalar her istekte; `paths` glob dizisi koşullu aktivasyon, eşleşme DETERMİNİSTİK (dosya yolu/açık sekme/görünür panel/düzenlenmiş dosya), model kararına bağlı değil. D · https://docs.cline.bot/customization/cline-rules.
B-11. Aider'da yol/glob-tetikli kural mekanizması belgelenmemiş: `/read`/`--read` elle ya da `.aider.conf.yml read:` her-zaman. X (yokluk) · https://aider.chat/docs/usage/conventions.html.
B-12. IFScale (arXiv:2507.11538): 500 talimatlı kıyaslama, 20 model; en iyi sınır-model 500 yoğunlukta %68 doğruluk (birebir alıntı). D · https://arxiv.org/abs/2507.11538 · v1 2025-07-15/16.
B-13. IFScale 3 bozulma paterni: threshold / linear / exponential decay; erken-sıra talimat yanlılığı. K (PDF çekilemedi; eşik rakamları yok).
B-14. Claude Code bağlam-penceresi sayfası DEMONSTRATİF simülasyon: `.claude/rules/` `paths:` kuralı 380 token, başka biri 290; proje CLAUDE.md 1.800; global 320 — kurgusal, ampirik değil. K · https://code.claude.com/docs/en/context-window.
B-15. Blog tahmini "20 global Cursor kuralı ~2.000 ekstra token/mesaj" — resmî teyit yok. X [?] · medium.com/@peakvance/…
B-16 (son üçte bir). Cursor ve Devin Desktop kök `AGENTS.md`'yi frontmatter'sız her-zaman-aktif alternatif olarak destekliyor. K (iki D gözlemin sentezi).

Tetik semantiği tablosu: Cursor (her-zaman · model-seçimli · glob · elle) · Copilot (glob) · Devin Desktop (always_on · model_decision · glob · manual) · Cline (her-zaman · glob deterministik) · Aider (elle · her-zaman) · Claude Code `.claude/rules/*` `paths:` glob (aile A referansı).

Kanıt kısıtı: bütçe tam; IFScale PDF ikili (eşik rakamları yok); sayfalarda revizyon tarihi yok → AS-OF = çekim; rebrand tarihi ikincil; kural-sayısı↔token ampirik benchmark bulunamadı; 403 yaşanmadı.
