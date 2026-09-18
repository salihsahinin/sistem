# Sistem monorepo — F5 kanıt tablosu (2026-09-18 16:1x, Jarvis Fable ana-sıra; Karar 101 geri-açma koşulu)

*Ölçüm: Friday oturumu `~/sistem/friday` (Opus 5 medium, worktree kapalı) 16:07'de "seans başı" ile açıldı; Jarvis ana-sıra oturumu aynı anda canlı. Kaynaklar: Friday transkripti `~/.claude/projects/-Users-HasanSalihSahin-sistem-friday/a4a5c5da….jsonl` (66 satır) · `friday/veri/bronz/hareket-olay.jsonl` · Friday açılış brifi (Salih yapıştırdı). Deneysel m.29; sayılar m.39.*

| # | Kanıt | Ölçüm | Hedef | Sonuç | Etiket |
|---|---|---|---|---|---|
| 1 | Friday bağlamına yüklenen kanon dosyaları | `~/.claude/CLAUDE.md` · `~/sistem/CLAUDE.md` (kök) · `~/sistem/friday/CLAUDE.md` | `jarvis/CLAUDE.md` yok | **Jarvis satırı 0** — geri-açma koşulu sağlanmadı, izolasyon geçerli | D |
| 2 | Friday transkriptinde `sistem/jarvis` yolu | 0 satır | 0 | geçti | D |
| 3 | Friday hareket kütüğünde Jarvis yolu / RED | 4 çağrı (3 Bash + 1 Skill), Jarvis yolu 0, RED 0 | 0 | geçti | D |
| 4 | Hook çift-koşumu (kök dispatcher + ajan ayarı) | transkript tool_use 5 · kütük 4 (Skill çağrısı kütüğe düşmez); çift satır yok | 1× | geçti; hangi `settings.json`'ın yüklendiği doğrudan görülmedi, çift kayıt olmaması dispatcher freninin ya da tek-yüklemenin sonucu | K |
| 5 | Friday'in kök kanonu okuması | Brif kök `../AGENTS.md`'yi okudu, `kanon/` bağının emekli olduğunu doğru yorumladı | okur | geçti | D |
| 6 | Paralel oturum kapısı Friday tarafında | Son commit `499337c` 7 dk, "başka oturum canlı" şüphesi + `git add <yol>` beyanı | şüphe + H4 | geçti | D |
| 7 | Jarvis K1 kapısı `friday/` commit'lerini tanır | `[friday+jarvis+kök]` alanı d59211f'de görünür | görünür | geçti | D |

**Açık:** Friday `seans-acilis` skill'i 4. adımda `kanon/tuzuk-v0.md` arıyor (bayat; Friday tespiti) → Jarvis düzeltir (`friday/.claude/skills/seans-acilis/SKILL.md`, Edit) · hangi `settings.json`'ın yüklendiği için hook echo ölçümü tur-6'da (`SISTEM_AJAN` env izi) · Friday tur-5 §3 beş soru Salih'te.
**Hüküm önerisi:** F5 `DONE`; Karar 101 geri-açma tetiklenmedi. İB-108'e geçilir.
