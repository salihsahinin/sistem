---
name: fetch-ozetleyici-kurgu-bayragi
description: WebFetch özetleyicisinin "bu sayfa kurgusal/var değil" demesi kanıt değildir; kesim-sonrası içerikte üretilen gürültüdür, çürütme sayılmaz
metadata:
  type: feedback
---

WebFetch'in küçük özetleyici modeli, kendi bilgi kesiminden **sonraki** tarihli sayfalar için "this appears to be a fictitious webpage", "this article does not exist", "a future date" gibi hükümler üretir; aynı cevapta sayfanın gerçek içeriğini birebir alıntılamayı sürdürür. Bu bayrak **veri değil gürültüdür**: hükme sokulmaz, çürütme sayılmaz. Karar, dönen içeriğin kendisine ve çapraz tutarlılığa bakılarak verilir.

**Why:** 2026-09-21 hakem koşumunda iki ayrı çekim (claymath.org/news/navier-stokes-announcement/ ve stanfordtechreview.com) "var değil/kurgusal" etiketiyle döndü ama ikisi de tam alıntı, tablo rakamı ve tarih verdi; içerik ayrıca bağımsız ikinci sayfayla (claymath "Active" sayfası) tutarlıydı. Bayrağa uyulsaydı doğrulanmış iki nokta yanlışlıkla `ÇÜRÜDÜ` yazılacaktı. Bu, 2026-07-17 dersinin ayna hâli: orada "403 = doğrulandı sanmak" hatası vardı, burada "özetleyici kurgu dedi = çürüdü sanmak".

**How to apply:** Çekim cevabında kurgu/gelecek-tarih uyarısı görünce (a) uyarıyı rapora "özetleyici bayrağı, hükme sokulmadı" diye yaz, (b) dönen birebir alıntıları normal kanıt gibi tart, (c) mümkünse aynı iddiayı ikinci bir URL'den çapraz doğrula. Gerçek `ERİŞİLEMEDİ` yalnız HTTP hatası, boş gövde ya da ikili/parse edilemeyen içeriktir. Bkz. [[dogrulama-butcesi-hedefleme]].
