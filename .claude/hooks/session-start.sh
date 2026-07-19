#!/usr/bin/env bash
# JARVIS SessionStart hook (deneysel m.29; kurulum 2026-07-19, Dilim 1 paketi)
# Amaç: CC her açılışta CANLI kanonu okur + yetki bandını görür (rapor 3 Opsiyon 2: mimari > talimat)
echo "=== JARVIS SessionStart ==="
echo "--- YETKİ BANDI (m.41): Bu yüzey CC = YAN OTURUM. Kanon/inşa kararı yalnız ana-sıra(Cowork) ∧ Fable ya da Salih imzası. Bu oturum öneri üretir, kanon KİLİTLEMEZ; core/ + CLAUDE.md + .claude/ yazımı yapısal kilitli (settings deny), git push onaya tabi. Çıktılar: kuyruk/ cc/ raporlar/ (append-only). ---"
echo "--- core/durum-kapsulu.md (ilk 40 satır) ---"
sed -n '1,40p' core/durum-kapsulu.md 2>/dev/null || echo "(kapsül okunamadı)"
echo "--- core/pano.md güncelleme satırı ---"
sed -n '1,8p' core/pano.md 2>/dev/null || echo "(pano okunamadı)"
echo "=== /SessionStart ==="
