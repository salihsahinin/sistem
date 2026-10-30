#!/usr/bin/env bash
# AJAN FAN-OUT FRENİ — PreToolUse hook, matcher: Agent (İB-54 adım 2; Karar 74 M-4 (d) paket A "sınıf-bazlı deterministik çağrı-freni";
# Karar 39 Salih: "fren tetiklenme koşulu zor olsun, aşırı uç senaryolar için çalışsın; kaliteyi kısmayalım").
# Kök neden (raporlar/2026-08/2026-08-29-ib54-delinme-kok-neden.md KN-1/KN-2/KN-4): fren metindeydi, ölçüm harcamadan SONRAYDI, fan-out atomikti.
# Bu hook freni KOŞUM KATMANINA taşır: her Agent çağrısı TAAHHÜT ANINDA sayılır (oturum başına sayaç); UYARI eşiğinde bronz olay,
# DURDUR eşiğinde çağrı engellenir (exit 2 + gerekçe). Workflow ajanları bu hook'tan GEÇMEZ — onlar için cc/workflow/fren-sablonu.js.
# Eşikler (m.29 deneysel; taban silver amb_olgu_kosum @b16b1a9, 29 wf: ajan/wf p50 12 · max 23; hareket: Agent/oturum max 11):
#   UYARI  = 36  (p50 × 3 — Öneri A "medyan × ~3")      DURDUR = 72  (UYARI × 2 ≈ max × 3 — aşırı uç)  [tek-katman tabanı, AS-OF 2026-08-29]
# REVİZYON (Salih B-hükmü 2026-08-31, devir cc/devir/devir-2026-08-31-opus-icra.md soru-1): sayaç oturum-geneli ve alt-ajan çağrılarını da
# sayıyor → lider→işçi (firstmate) iki-katmanlı koşum tek-katman tabanını yapısal aşıyor (ölçüm: 78 çağrı / 4 birim ≈ 20/birim).
# Yeni varsayılan: UYARI 72 · DURDUR 144 (2× katman çarpanı). Katman-başına ayrı sayaç (seçenek A) masa kalemi olarak kuyrukta.
# REJİM ETİKETİ (tüzük m.46(d), Karar 39 C): [rejim: manuel-tempo · kota-bol · ekonomi −%30 (Salih 08-15) · AS-OF 2026-08-29] — rejim
# değişince (K-009/K-010 otomasyon) eşikler OTOMATİK yeniden açılır, taşınmaz. Salih beyanıyla geçici kapatma: JARVIS_FREN_KAPALI=1 (olay yazılır).
# Kayıt: bronz veri/bronz/fren-olay.jsonl (append-only; 1 satır = 1 fren olayı) · sayaç durumu .claude/hooks/state/ (gitignore, oturum başına).
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" pretool-ajan-fren   # Rust varsa exec; yoksa aşağısı (durum #1)
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/pretool-ajan-fren.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse jarvis-hook ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "jarvis-hook yok (pretool-ajan-fren): önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/pretool-ajan-fren.sh)" >&2
exit 0
