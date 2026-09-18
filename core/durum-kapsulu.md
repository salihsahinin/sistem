# Durum Kapsülü — Friday

*Her oturumun İLK okuduğu dosya. SICAK katman: üzerine yazılır, arşiv değildir. Bütçe ≤4 KB / ≤20 satır. FIFO: "Şu an" listesi en fazla 8 madde; 9. madde girince en eski `arsiv/kapsul-YYYY-MM-DD.md`'ye iner (silme yok). Tarihçe `raporlar/` + git log.*

**Güncelleme:** 2026-09-18 tur-4 — uygulama turu bitti: hook v0.3 (alt-ajan dalı + Z1/Z2 onarımı), deny bloğu, desen 21. Test 22 PASS · 0 FAIL. İşçi 0, emir-kaynaklı sapma 0, Jarvis'e yazım 0.

## Şu an
- Hook v0.3 canlı: `agent_id` varsa işçi liderin bağlam penceresini okuyamaz (kapsül · pano · defter · kutu · `veri/bronz/**` · transkriptler; kendi `tool-results/`'ı muaf), `RED` olayı `veri/bronz/altajan-okuma-olay.jsonl`'a düşer. Ana-sıra davranışı değişmedi.
- Z1 (Bash izin listesi) ve Z2 (`cd` + göreli yol) kapandı; Z3b (yolun tamamı değişkende) **K** — metin taramasının belgelenmiş sınırı.
- `settings.json` deny 5 → 20 satır (3b listesi, `core/` hariç). Canlı kanıt: yasak yol `Read` ile reddedildi, ret mesajı izin ayarından geldi; `kanon/` okunmaya devam ediyor.
- Test dosyası 22 vaka, `FRIDAY_HOOK_TEST` yalnız kütük yazımını kapatıyor, `exit 2` kararını değil (Jarvis örneğindeki hata kopyalanmadı).
- Desen 21 çekirdekte (symlink ve `!` semantiğini belgeden oku); toplam 21 madde.
- Açık, Salih/Jarvis'te: ayrıştırıcının `grep` desenini yol sanması artık çağrı durduruyor (3 seçenek) · Jarvis örnek hook'unun bayrak hatası · alt-ajan listesine `cc/gelen/**` · Z3b için sandbox.
- Geçiş ölçüsü (emir-kaynaklı sapma/devir): 2 · 1 · 0 · 0 → A1 → A2 için **2/2** (doğrulama Jarvis'te).
- Koşum sayacı 4/10.

## Sonraki ilk iş
0. Jarvis'in doğrulama sonucunu bekle (`ÖLÇEN`: test + canlı deneme yeniden koşulur); sonra §3'teki beş sorunun hükmüne göre ilerle.
