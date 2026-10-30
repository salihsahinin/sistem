#!/usr/bin/env bash
# JARVIS SessionStart hook — BRİF ≤2 KB (KB-51 (a), Salih imzası 08-21 Karar 61; icra İB-24 2026-08-22 seans-14).
# Tarihçe: kurulum 2026-07-19 (Dilim 1: kapsül ilk 40 satır + yetki bandı, 11 KB); rev 08-16/08-17 yetki bandı GK-2.
# Neden indi: harness yalnız ~2 KB önizlemeyi bağlama koyar (25,8 KB → 2 KB; KB-51) → tam kapsül BURADA DEĞİL, elle okunur (CLAUDE.md §3).
# İB-27 (KB-54 (a) Karar 62): silver tazelik — uretim.git_head_sha ≠ HEAD → "BAYAT" + katman-hatti tarifi (otomasyon: tespit; koşum ritüelde).
# Karar 68 (08-26): ZAMAN-ZEMİNİ satırı — bugün (sistem saati) + model kesim tablosu; anakronizm freni.
# Çıktı sert-kapılı: head -c 2000. Her satır tek bakışta; deterministik (yalnız disk + git).
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" session-start   # Rust varsa exec; yoksa aşağısı (durum #1)
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/session-start.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse jarvis-hook ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "jarvis-hook yok (session-start): önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/session-start.sh)" >&2
exit 0
