---
paths:
  - "tools/**"
  - ".claude/hooks/**"
---

# Script ve hook kuralı (yalnız `tools/` ya da `.claude/hooks/` dosyalarıyla çalışırken yüklenir; Karar 96 M1, 2026-09-15)

- Yazım standardı `tools/AXI-STANDARDI.md` (iki kanal · çıkış kodu sözlüğü · sabit bayraklar · determinizm); indeks `tools/SCRIPTLER.md` — kalıcı her script'e satır zorunlu (ne yapar · koş · ne zaman).
- Docstring, yorum ve kullanıcı mesajları Türkçe; kod tanımlayıcıları İngilizce serbest.
- Deterministik tasarım: aynı girdi → aynı çıktı; rastgelelik tohumlu; ölçüm scriptleri kanona yazmaz, rapor üretir.
- Kanon dosyalarına (`core/`, `CLAUDE.md`, `.claude/`) Bash ile yazım telde engelli; düzenleme Edit/Write aracıyla ve yalnız Salih kararıyla.
- Hook'lar: girdi stdin JSON; çıktı sözleşmesi Claude Code hooks belgesine göre. Test (Karar 113 M5, icra 2026-10-16): **engelleyen** (exit 2 üretebilen) hook'un yanında `*-test.sh`, bağlanmadan yeşil; kütük/bağlam yazan hook'a ayrı birim testi gerekmez; Rust taşımasında fark testi bir kez. Basit koda yeni birim testi yazılmaz.
- Hareket kütüğü: Bash `description` alanı Türkçe, günlükte okunur.
