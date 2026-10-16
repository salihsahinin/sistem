# rust-yonlendir.sh — Jarvis hook'larının Rust yönlendiricisi (Karar 113 M7, durum #1; Salih 2026-10-16 seçenek A).
# Kaynaklanır, kendi başına koşmaz: her hook betiği stdin'i okumadan önce `. rust-yonlendir.sh <alt-komut>` der.
# Mekanizma: jarvis-hook programı bulunursa stdin'i ona bırakıp exec eder (betiğin geri kalanı koşmaz); bulunmazsa
# sessizce döner ve betiğin Python gövdesi koşar (düşüş yolu; program olmayan makine/worktree hook'suz kalmaz).
# Arama sırası: bu kopyanın <kök>/target/release → kopya worktree ise ana kopyanın target/release (.git dosyasındaki gitdir'den).
# JARVIS_HOOK_PYTHON=1 Rust'ı atlar (fark testi, acil geri alma). Program `cargo build --release -p jarvis-hook` ile üretilir.
_ry_jarvis="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && { pwd -W 2>/dev/null || pwd; })"
if [ "${JARVIS_HOOK_PYTHON:-}" != 1 ]; then
  _ry_kok="${_ry_jarvis%/*}"
  _ry_adaylar="$_ry_kok"
  if [ -f "$_ry_kok/.git" ]; then
    _ry_gd="$(sed -n 's/^gitdir: //p' "$_ry_kok/.git")"
    _ry_adaylar="$_ry_adaylar ${_ry_gd%/.git/worktrees/*}"
  fi
  for _ry_k in $_ry_adaylar; do
    for _ry_p in "$_ry_k/target/release/jarvis-hook.exe" "$_ry_k/target/release/jarvis-hook"; do
      [ -x "$_ry_p" ] && exec "$_ry_p" "$1" --repo "$_ry_jarvis"
    done
  done
fi
unset _ry_kok _ry_adaylar _ry_gd _ry_k _ry_p
