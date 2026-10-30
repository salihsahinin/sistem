#!/usr/bin/env bash
# ALT-AJAN OKUMA KİLİDİ — PreToolUse hook (Read · Grep · Glob · Bash). İB-83 (Karar 92 M7-1, Salih 2026-09-10: "jarvisin alt ajanı
# çalıştırırken de kendi içerisindeki diğer context windowu okuma kabiliyetini kısıtlarız"). Kaynak: Friday tur-2 S3 — hook girdisinde
# `agent_id` "Present only when the hook fires inside a subagent call" (code.claude.com/docs/en/hooks, AS-OF 2026-09-10).
# Mekanizma: agent_id VARSA (= alt-ajan) → "başka bağlam pencereleri" listesi RED (exit 2): oturum transkriptleri (~/.claude/projects/**),
# Jarvis'in sıcak hafızası (kapsül · pano · defter · fikir kutusu · MEMORY), hareket/bağlam kütükleri (veri/bronz/*olay.jsonl), Friday reposu,
# staj/galeri dış projeler (md.49). Ana-sıra (agent_id yok) etkilenmez. Her RED bronz olaya düşer: veri/bronz/altajan-okuma-olay.jsonl.
# Emrin `baglam` listesi bir gün hook'a ulaşırsa (ortam değişkeni / .aktif-emir dosyası) izin-listesi moduna geçilir; v0 = yasak-listesi.
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" pretool-altajan-okuma   # Rust varsa exec; yoksa aşağısı (durum #1)
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/pretool-altajan-okuma.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse jarvis-hook ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "jarvis-hook yok (pretool-altajan-okuma): önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/pretool-altajan-okuma.sh)" >&2
exit 0
