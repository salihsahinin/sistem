---
name: feedback-vurgusuz-anlatim-capslock-yok
description: Salih 09-14 açıklamalarda caps-lock/büyük harfli kelimelerle vurgu istemiyor
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 76a8d28a-23cd-4c2e-9b83-bd4a69fe50d7
  modified: 2026-09-14T09:00:09.979Z
---

Açıklama metinlerinde büyük harfli kelimelerle (caps lock) vurgu yapılmasın.

**Why:** Salih 09-14'te doğrudan belirtti; okurken rahatsız edici/bağırma hissi veriyor olabilir.

**How to apply:** Vurgu gerekiyorsa kalın yazı (markdown `**...**`) ya da cümle yapısıyla ver, tüm-büyük-harf kelime kullanma. [[feedback-anlatim-bicimi-dogrudan]] ile birlikte oku — ikisi de anlatım biçimini sadeleştirme yönünde.

**Ek (Karar 97, 09-15):** kural "büyük harf = kod": tamamı büyük harfli sözcük yalnız kısaltma ya da backtick içinde durum jetonu (`DONE`, `KALAN`); 3 harfli caps (`VAR`, `SANA`) da yasak; kanon 09-15'te `tools/buyuk-harf-temizle.py` ile temizlendi, pre-commit teli yeni caps'i reddeder, Stop hook çıktıda tek satır düzeltme ekler.
