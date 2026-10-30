#!/usr/bin/env bash
# BÜYÜK-HARF VURGU FRENİ — Stop hook (deneysel m.29; kurulum 2026-09-15, Salih yan-görevi 09-15:
# "caps lock açık bir şekilde kelime vurgusu görmek istemiyorum"; kök neden analizi
# raporlar/2026-09/buyuk-harf-vurgu-analizi-2026-09-15.md).
# Mekanizma: cevap bitince son asistan mesajı + son turun araç girdileri (widget/Write/Edit, v0.3) taranır; kısaltma/kod dışı ≥4 harfli tamamı-büyük
# sözcük varsa Claude durdurulmaz, "kalın harfe çevir" gerekçesiyle devam ettirilir (decision=block).
# Sınır: hook gösterilmiş çıktıyı GERİ ÇEKEMEZ; yalnız ekleme yaptırır. Bu yüzden düzeltme TEK SATIR
# (09-15 vakası: "cevabı yeniden yaz" talimatı aynı soruyu iki kez gösterdi → yan oturum transkripti
# 4ac5ca1c kayıt 449/453). Ölçüm: block sayısı 5 seans sonra (defter 09-15 Salih hükmü).
# Sonsuz döngü freni: stop_hook_active=true ise (ikinci tur) fren pas geçer.
# Beyaz liste: teknik kısaltmalar + kanon durum sözcükleri (DONE/PASS/FAIL/AS-OF) + faz adları.
# Kod blokları (```…```) ve satır-içi kod (`…`) taranmaz; Salih beyanı alıntıları ("aynen: …") taranmaz.
. "$(dirname "${BASH_SOURCE[0]}")/rust-yonlendir.sh" stop-buyuk-harf   # Rust varsa exec; yoksa aşağısı (durum #1)
# Karar 118 M2 (Salih 2026-10-17; icra 2026-10-30): Python gövdesi arsiv/kod/python/hooks/stop-buyuk-harf.sh'a indi (m.8: taşındı, silinmedi).
# Buraya düşüldüyse jarvis-hook ikilisi yok (ya da JARVIS_HOOK_PYTHON=1): uyarı ver, hiçbir şeyi engelleme, sessiz çık.
cat > /dev/null
echo "jarvis-hook yok (stop-buyuk-harf): önce cargo build --release -p jarvis-hook (Karar 118 M2; eski Python gövdesi arsiv/kod/python/hooks/stop-buyuk-harf.sh)" >&2
exit 0
