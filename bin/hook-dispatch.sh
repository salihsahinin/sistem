#!/usr/bin/env bash
# hook-dispatch.sh — sistem kökü tek hook girişi (Karar 101; F1 taslağı 09-18, F4'te ~/sistem/bin/ altına alındı + çift-koşum freni).
# Mekanizma: harness hangi ayar dosyasını yüklerse yüklesin, bu script oturum cwd'sinden (stdin JSON "cwd", yoksa $PWD)
# ajanı bulur (~/sistem/<ajan>/…) ve o ajanın KENDİ .claude/settings.json'ındaki hooks[<olay>] kayıtlarını, matcher'ı
# tool_name'e uygulayarak, CLAUDE_PROJECT_DIR=<ajan dizini> ile sırayla koşturur (mini hook-koşucu). Ajan hook'ları
# değişmeden çalışır; ajanın kaydı yoksa exit 0. Harness-nötr (yalnız dosya + stdin), backend-nötr.
# Çıkış: herhangi bir ajan hook'u 2 dönerse 2 (stderr aynen), aksi hâlde 0; stdout'lar birleştirilir.
set -u
OLAY="${1:?olay adı gerekli}"
KOK="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
# Rust yönlendirme (durum #11, Karar 113 M7; kalıp jarvis/.claude/hooks/rust-yonlendir.sh): hook-dispatch programı bu kopyada ya da
# worktree ise ana kopyada varsa stdin'i ona bırakıp exec eder; yoksa uyarı verip sessiz çıkar (Karar 118 M2). JARVIS_HOOK_PYTHON=1 Rust'ı atlar.
if [ "${JARVIS_HOOK_PYTHON:-}" != 1 ]; then
  _hd_kok="$(cd "$KOK" && { pwd -W 2>/dev/null || pwd; })"
  _hd_aday="$_hd_kok"
  [ -f "$KOK/.git" ] && _hd_gd="$(sed -n 's/^gitdir: //p' "$KOK/.git")" && _hd_aday="$_hd_aday ${_hd_gd%/.git/worktrees/*}"
  for _hd_k in $_hd_aday; do
    for _hd_p in "$_hd_k/target/release/hook-dispatch.exe" "$_hd_k/target/release/hook-dispatch"; do
      [ -x "$_hd_p" ] && exec "$_hd_p" --kok "$_hd_kok" "$OLAY"
    done
  done
fi
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/hook-dispatch.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse hook-dispatch ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "hook-dispatch yok: önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/hook-dispatch.sh)" >&2
exit 0
