---
name: feedback-bash-heredoc-tek-tirnak
description: "Bu makinedeki Bash aracında tek tırnak (') içeren heredoc komutu \"unexpected EOF\" ile tamamen başarısız olur; dosya yazımında Write aracı kullanılır"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 3e1fa2e3-46fa-4ae6-8358-d2c748e49d92
  modified: 2026-10-25T23:58:53.016Z
---

2026-10-26 gözlem: `cat > dosya <<'EOF' ... Mirror's ... EOF` biçimli komut, gövdedeki tek tırnak yüzünden kabuk ayrıştırmasında çöktü (exit 2, hiçbir dosya yazılmadı); üç paralel çağrı aynı anda düştü.

**Why:** Araç komutu tek tırnaklı bir sarmalayıcıdan geçiriyor; heredoc gövdesi korunmuyor.
**How to apply:** Çok satırlı dosya içeriğini Bash heredoc yerine Write/Edit araçlarıyla yaz; Bash'i yalnız komut koşturmak için kullan. Kısa, tırnaksız içerik için heredoc sorunsuz.
