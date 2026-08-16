#!/usr/bin/env bash
# JARVIS SessionStart hook (deneysel m.29; kurulum 2026-07-19, Dilim 1 paketi)
# Amaç: CC her açılışta CANLI kanonu okur + yetki bandını görür (rapor 3 Opsiyon 2: mimari > talimat)
# rev 2026-08-16 (Carvis/Fable, Salih "düzelt"): yetki bandı m.41 GEÇİŞ KAYDI'na hizalandı — Cowork-dönemi metni (CC=yan-oturum · ana-sıra(Cowork) · settings-deny kilidi) bayattı; kalıntı-referans kapatıldı (bağlam-anahtar-kaydı: ana-sira-yuzeyi)
echo "=== JARVIS SessionStart ==="
echo "--- YETKİ BANDI (m.41 + GEÇİŞ KAYDI 08-12/08-14): Bu yüzey TERMİNAL (CC) = ANA-SIRA (Cowork emekli). Kanon/inşa kararı geçerliliği: (ana-sıra ∧ model = Fable) ∨ Salih açık imzası — GEREKLİLİK, yeterlilik değil; non-Fable ya da yan-oturum (bulut/mobil chat, yan sekme) karar ALMAZ, bulguyu devir dosyasıyla taşır. Edit-deny kilidi KALKTI (efb2c13); kalan frenler: git push onaya tabi (m.9 push şartı BAKİ) · md.49 share freni · PreToolUse teli. Katman-1 (core/, CLAUDE.md, tüzük) yalnız Salih kararıyla; Katman-2 Carvis yapar+commit'ler, veto = revert. ---"
echo "--- core/durum-kapsulu.md (ilk 40 satır) ---"
sed -n '1,40p' core/durum-kapsulu.md 2>/dev/null || echo "(kapsül okunamadı)"
echo "--- core/pano.md güncelleme satırı ---"
sed -n '1,8p' core/pano.md 2>/dev/null || echo "(pano okunamadı)"
echo "=== /SessionStart ==="
