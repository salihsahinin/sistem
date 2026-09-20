---
name: feedback-ders-elle-pratik-adimi
description: "ogren skill'inde (ders akışı) araç/format öğreten düğümlerde salt okunan örnek yetmiyor, Salih'in bizzat deneyeceği bir mini adım istenir"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8e00e0dc-e89f-4d1f-a098-d73ee63e63bb
  modified: 2026-09-11T08:19:08.832Z
---

`ogren` skill'i (dört fazlı ders akışı: `PROBE`→`PLAN`→`TEACH`→`CLOSE`) ile işlenen derslerde, bir araç/dosya-format öğreten düğümde (ör. YAML yazımı, promptfoo koşumu) yalnızca "somut örnek" okumak yeterli gelmiyor — Salih "aklımda tam canlanmıyor" diyerek kendisinin bizzat deneyeceği bir mini-pratik adım istedi (2026-09-11, [[project-evals-ogrenme-serisi]] H1 dersi, kutu 6-7 arası).

**Why:** Pasif okuma ile örneği kendi elinle üretmek arasındaki fark — edilgen anlatım yalnızca tanıma yol açar, üretim/pratik kalıcı öğrenmeyi sağlar. Bu, mevcut "benzetme değil doğrudan" ve "görsel atıflı" öğretim ilkelerinin (feedback-anlatim-bicimi-dogrudan.md) doğal uzantısı.

**How to apply:** `ogren` skill'inin `TEACH` fazında, bir düğüm somut bir araç/format/komut öğretiyorsa (soyut kavram değil, "nasıl yazılır/çalıştırılır" türü), soru öncesi ya da sonrası kısa bir "şimdi sen dene" adımı ekle: kullanıcıdan örneğe benzer küçük bir varyasyonu kendi kendine üretmesini iste (örn. örnek YAML vakasına benzer yeni bir vaka yazdır), sonra değerlendir. Salt kavramsal/teorik düğümlerde (ör. tanım karşılaştırması) buna gerek yok — mevcut soru formatı yeterli. 09-15: kural `ogren` v0.2 §3'e girdi; eki [[pratik-salih-eli]] (komutu Salih koşar, Jarvis'in koşumu referans, `DONE` yalnız Salih beyanıyla).
