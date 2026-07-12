# Fikir Kutusu Adayı — İterasyon Verimi (2026-07-12, mobil)

**Statü:** HAM FİKİR / hipotez. Mobilde alındı, kalıcı karar değil. PC'de (C:\JARVIS + Homebase) ingest edilecek. Cep kapsülü 07-10 snapshot'ı güncel değil — bu not onun üzerine yazılmaz, ayrı ingest edilir.

## Fikir (Salih, kendi cümleleriyle özetlenmiş)
Çıktıların iterasyonuyla optimizasyon artırılacak. Çıktıdan ne kadar çok veri toplanırsa o kadar optimizasyon mümkün — ama çok veri = çok bellek tüketimi. Tanım: **iterasyon verimi** = iterasyon başına elde edilen optimizasyon kazancının bellek maliyetine oranı. Uzun vadeli hedef: iterasyon verimini artırmak ya da en kötü korumak. Takas: bellek tüketimini azalttıkça optimize edecek veri de azalır. Bunun üzerine **matematik temelli bir formülizasyon** geliştirilmeli.

## Carvis şerhi (ingest'te değerlendirilecek, karar değil)
1. **#28 ile akrabalık:** #28 (bağlam-yoğunluğu optimizasyonu) girdi tarafı — max bağlam/token. Bu fikir çıktı/telemetri tarafı — max optimizasyon-kazancı/bellek. Ayrı fikir mi, #28'in geri-bildirim uzantısı mı? Salih karar verecek.
2. **Literatür bağı (tekerlek uyarısı):** value of information, sample efficiency, active learning (hangi veriyi saklamaya/etiketlemeye değer sorusu). Formülizasyon sıfırdan değil bu çerçevelerden başlamalı — #7 protokolüne (3 aday + stat kartı) uygun aday.
3. **Surprisal köprüsü:** Salih'in entropi çalışmasıyla doğrudan bağ — düşük-surprisal çıktı loglamak bellek yakar, az bilgi taşır. Aday kural: log ağırlığı ∝ surprisal; usage-weighted decay'in çıktı-tarafı simetriği.
4. **Formül iskeleti (taslak, sınanmamış):**
   V(iterasyon verimi) = ΔG / C, burada ΔG = iterasyondan elde edilen optimizasyon kazancı (ölçüsü tanımlanmalı: hata düşüşü? done'a yaklaşma?), C = saklanan verinin bellek/token maliyeti. Azalan getiri beklenir: dG/dC monoton azalan → optimal saklama noktası dG/dC = birim bellek fırsat maliyeti olduğu yer. Açık soru: ΔG'nin ölçülebilir tanımı — done ne kadar nicel, ΔG o kadar ölçülebilir (B-koşulu ile aynı mantık).

## Tüzük hatırlatması
Akış hattı: fikir kutusu → öneri dosyası → tüzük; aşama atlanmaz. Taslak-inşa serbest, UYGULAMA build kapısına tabi. Ve çapa: tek metrik push'lanmış PortRisk commit'i — bu fikir S1'in önüne geçmez.
