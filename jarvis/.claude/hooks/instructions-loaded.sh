#!/usr/bin/env bash
# TALİMAT-YÜKLEME KÜTÜĞÜ — InstructionsLoaded hook (deneysel m.29; kurulum 2026-09-15, Karar 96 M4).
# Amaç: hangi CLAUDE.md / .claude/rules dosyasının hangi seansta, hangi nedenle (session_start ·
# nested_traversal · path_glob_match · include · compact) bağlama yüklendiğini deterministik kütüklemek.
# Kullanım: bağlam-izleme (İB-81 ön-koşulu; Salih 09-10: "bağlama neyin girdiğini yalnız model bilir")
# + S-kaynak madenciliğinin okunma ayağı (tools/baglam-skill-aday.py) + üç-yuva davranış ölçümü.
# Ham girdi olduğu gibi saklanır (alan şeması belgede tam değil; ilk seanslardan sonra şema çıkarılır).
# Hiçbir şeyi engellemez; çıkış 0. Kütük: veri/bronz/talimat-yukleme-olay.jsonl (ekleme-esaslı).
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" instructions-loaded   # Rust varsa exec; yoksa aşağısı (durum #1)
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/instructions-loaded.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse jarvis-hook ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "jarvis-hook yok (instructions-loaded): önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/instructions-loaded.sh)" >&2
exit 0
