#!/usr/bin/env bash
# OKUMA-İZİN KİLİDİ — PreToolUse hook (Read · Grep · Glob · Bash); alan ajanının okuma kilidi (Karar 91/99/100/101/105).
# İzinli: ajan dizini + depo kökündeki kanon dosyaları + sablonlar/ + .claude/okuma-izin-ek kökleri + geçici + harness; dışı exit 2.
# v0.2-v0.6 (2026-09-10..09-21): bash içinde gömülü Python gövdesi (tarihçe git log'da).
# v0.7 (2026-11-10): gövde Rust `jarvis-hook okuma-izin` (jarvis/kod/hook/src/okuma_izin.rs); bu dosya ince sarmaldır.
#   Düzeltmeler: Git Bash /c/ öneki çözülür · fail-closed (ikili yok ya da bozuk JSON = exit 2) · Windows geçici dizini izinli.
# Tek kaynak bu dosya (friday); alan ajanı kopyaları birebir aynıdır, ajan adına bağlı satır içermez.
# Arama: <depo kökü>/target/release → kopya worktree ise ana kopyanın target/release (.git dosyasındaki gitdir'den).
_oi_dizin="${CLAUDE_PROJECT_DIR:-$PWD}"
_oi_kok="$(cd "$_oi_dizin/.." 2>/dev/null && pwd)"
_oi_adaylar="$_oi_kok"
if [ -n "$_oi_kok" ] && [ -f "$_oi_kok/.git" ]; then
  _oi_gd="$(sed -n 's/^gitdir: //p' "$_oi_kok/.git")"
  [ -n "$_oi_gd" ] && _oi_adaylar="$_oi_adaylar ${_oi_gd%/.git/worktrees/*}"
fi
for _oi_k in $_oi_adaylar; do
  for _oi_p in "$_oi_k/target/release/jarvis-hook.exe" "$_oi_k/target/release/jarvis-hook"; do
    [ -x "$_oi_p" ] && exec "$_oi_p" okuma-izin
  done
done
echo "OKUMA-İZİN KİLİDİ: jarvis-hook ikilisi yok (aranan: ${_oi_adaylar:-$_oi_dizin/..}/target/release); çağrı engellendi (fail-closed). Depo kökünde: cargo build --release -p jarvis-hook" >&2
exit 2
