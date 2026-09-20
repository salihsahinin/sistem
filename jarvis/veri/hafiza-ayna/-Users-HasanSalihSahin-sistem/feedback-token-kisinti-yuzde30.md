---
name: feedback-token-kisinti-yuzde30
description: "Salih emri (2026-08-15): token tüketim hızı ~%30 düşürülecek — koşum tasarımı kısıtlı-bütçe rejiminde"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 914d8e47-f03d-46d2-a755-114e700f687e
  modified: 2026-08-15T20:57:35.166Z
---

Salih 2026-08-15 gece (hesap değişimi sonrası "tokenim çok hızlı bitti"): token tüketim hızını ~%30 düşürecek şekilde devam et. Her iki paralel jarvis oturumuna birden verildi.

**Why:** Aynı gün içinde 6+ m.40b workflow'u (her biri 0,65-1,23M ajan-tokeni) + paralel oturumlar 5-saatlik pencere limitini iki kez tüketti; bir de yarım kalan koşumun tez'lerinin farkında olmadan yeniden koşması (cache oturuma bağlı) israf üretti.

**How to apply:** (a) m.40b işçi arama bütçesi 15-25 → **10-15**; V26 örneklem ≤3 → ≤3 ama işçi effort: tez/antitez **medium**, V26 **low**, hakem **medium** (yalnız Katman-1-kritik sentezlerde high); antitez "en zayıf ~12-16 iddiaya odaklan" talimatı. (b) Aile sayısı: emir genişse bile 4 yerine 3'e bölmeyi öner. (c) Yarım kalan workflow'u **asla** sıfırdan koşturma — journal'dan tamamlanmış sonuçları çek, devam-script'ine göm (örnek: `~/.claude/jobs/*/tmp/m40b-devam.js` deseni), yalnız eksik aşamaları koştur. (d) Büyük veri bloklarını tool-çağrısında bastırma — Bash/python ile dosyaya göm. (e) Ölçüm: her workflow'un totalTokens'ı manifeste yazılıyor; kısıntı-öncesi taban ~1,0-1,2M/16-işçi — hedef ≤0,7M eşdeğer-kapsam. İlgili: [[feedback-parallel-sessions-keep-talking]]
