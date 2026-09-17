# Kaynak damgası (m.39, md.49)

- Veri: 10 injection vakası, tamamı bu oturumda üretildi (kendi üretimimiz) — kamu veri seti kullanılmadı çünkü G1 seviyesinde amaç mekanizma türlerini (doğrudan, sahte-sistem, sahte-delimiter, sızdırma, dolaylı-yönlendirme, HTML-yorum, rol-değiştirme, base64-gizleme, sahte-yetki, veri-sızdırma) tek tek örneklemekti.
- Toy agent: tek görevli "web sayfası özetleyici", naif/savunmasız sistem promptu (`prompt.txt`) — G1 kutu 6-8'deki savunma katmanları **bilerek** uygulanmadı, baseline ASR ölçmek içindi.
- Model: `anthropic:messages:claude-haiku-4-5-20251001`, Claude Code OAuth kimliği (apiKeyRequired:false, H1 deseni).
- Koşum tarihi (AS-OF): 2026-09-15.
- md.49: tamamı oyuncak veri, şirket/staj bağlantısı yok.
- Sonuç dosyası: `sonuc.json` (promptfoo ham çıktısı, git'e eklenmedi — büyük/tekrarlanabilir; koşum komutu üstte).
