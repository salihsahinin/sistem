#!/usr/bin/env bash
# core/-Bash TELİ — PreToolUse hook (deneysel m.29; kurulum 2026-07-23, A2 kapanış eki)
# Amaç: canary'nin kanıtladığı deliği kapatmak — settings-deny yalnız Edit/Write tutar,
# Bash ile core/ + CLAUDE.md + .claude/ yazımı serbestti. Bu bir TÖKEZLEME-TELİ, sınır değil
# (kabuk-taşıyan ajan zaptedilemez — kapsül güvenlik notu 07-22); kaçırdığı desen olabilir,
# yanlış-pozitifte mesajı gör ve komutu yeniden ifade et. Gerekçe: raporlar/vardiya/vardiya-teslim-2026-07-22-aksam.md
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" pretool-core-tel   # Rust varsa exec; yoksa aşağısı (durum #1)
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/pretool-core-tel.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse jarvis-hook ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "jarvis-hook yok (pretool-core-tel): önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/pretool-core-tel.sh)" >&2
exit 0
