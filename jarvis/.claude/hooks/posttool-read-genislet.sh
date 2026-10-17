#!/usr/bin/env bash
# BAĞLAM SIRASI — PostToolUse(Read) hook'u (Karar 117 mekanizma 1a, okuma rejimi; kurulum 2026-10-17).
# Read `@yol` satırlarını açmaz; okunan md dosyası içe aktarma taşıyorsa içe aktarılan bloklar otomatik yükleme
# sırasıyla (ebeveyn → çocuklar, pre-order) araç sonucunun ardına ek bağlam olarak eklenir. Gövde Rust:
# jarvis-hook posttool-read-genislet (kod/hook/src/read_genislet.rs, kural kod/baglam). Hiçbir şeyi engellemez.
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" posttool-read-genislet   # Rust varsa exec
# Rust yoksa düşüş: ek bağlam üretilmez (dosya yine Read ile okunmuştur; içe aktarmalar elle okunur).
cat > /dev/null
exit 0
