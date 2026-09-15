---
name: karar-modeli
description: Ölçek-eşiği üstü karar/tasarım sorusu için FARKLI matematiksel temelli 3 karar modeli üretir — en az biri karşıt-temelli, hepsi token×zaman×kalite×risk eksenlerinde sayısal karşılaştırmalı; önerileni işaretler, senaryo-defteri bloğu üretir. Kullan: "3 model", "karar modeli", "karşıt gömülü model", "matematik temelli seçenekler" dendiğinde ya da ölçek-eşiği üstü karar anında. KULLANMA: su-bardağı alt-karar, typo/tek-satır düzeltme, sonucu değiştirmeyecek küçük seçimler (m.25/m.37 muafiyeti). argument-hint: "<karar sorusu>"
metadata: { owner: jarvis, version: "0.1.0-deneysel-m29" }
---

# karar-modeli — m.37/m.40 koşum talimatı

Kanon zinciri: m.37 (3-model zorunluluğu) · m.37-eki (karşıt-temel) · m.40a (eşik = m.37 eşiği) · m.40b (araştırma-önce) · m.39 (deneysel-rakam damgası) · m.41 (yüzey yetkisi).

## Adımlar (sırayla, atlama yok)

1. **Eşik kontrolü.** Soru ölçek-eşiği ÜSTÜ mü? Değilse skill'i bırak, kararı direkt ver (m.25). Şüphede: geri-alınması zor ∨ >1 seans etkili ∨ kanon/mimari dokunuşlu → eşik üstü say.
2. **m.40b kapısı.** Karar yeni mekanizma/araç/desen seçimi mi? → sunumdan ÖNCE dış tarama gerekir (atlas-kosum varsa onu çağır; yoksa kısa web taraması). İç-önceliklendirme kararı → muaf, geç.
3. **3 model kur.** Her model için: (a) `references/temeller.md`'den FARKLI bir matematiksel taban seç; (b) önermeyi tek cümlede yaz; (c) token × zaman × beklenen-kalite × RİSK — sayısal ya da sıralı (az/orta/çok) doldur; sayı uydurma, kestirimse `[?]` damgala (m.39).
4. **Karşıt-temel şartı.** ≥1 model, önerinin karar-VARSAYIMINA zıt zeminden kurulur (beklenen-değer ↔ minimax · Bayes ↔ frekans · keşif ↔ sömürü · birikimli-delta ↔ topyekûn-sıkıştırma). İki test: **aygıt gerçek mi** (zıt zemin gerçekten farklı sonuç üretiyor mu) + **canlılık** (o zemini ciddiye alan biri bu modeli savunur muydu). Süs-karşıtlık sayılmaz.
5. **Öneri + triangülasyon.** Önerilen modeli ✅ işaretle, tek-satır gerekçe; zıt zeminlerin KESİŞTİĞİ yeri ayrıca yaz (kesişim = en sağlam parça). Karşıt model kısmen haklıysa "KISMEN YAKINSADI: şu parçası öneriye alındı" de.
6. **Defter bloğu üret.** Şablon: `references/defter-sablonu.md`. Zorunlu satırlar: Bağlam · Model A/B/C tek-satır özet + ✅ · Karşıt-temel (+canlılık verdikti) · Seçim (kim, ne zaman, görünürlük) · Geri-alınabilirlik · Gözlem (bekliyor) · Ders.
7. **Sun, bekleme.** Karşılaştırma Salih'e GÖRÜNÜR sunulur, onay BEKLENMEZ (m.37; veto her zaman açık). Her karar sorusu "bu ne / neden masada" özetiyle açılır (m.40 sunum kuralı 07-19).

## Gotchas (gerçek hata noktaları)

- Defter bloğunu ÜRET ama dosyaya kendin YAZMA/commit'leme — kayıt ayrı adımdır (yan-etki freni; ileride `/karar-kaydet`). Yan-oturumdaysan (m.41) blok devir-dosyasına gömülür, kanon kilitlenmez.
- Üç model "aynı fikrin üç tonu" olursa koşum geçersiz — tabanlar temeller.md'den fiilen FARKLI seçilmeli.
- Rakam yoksa satırı boş bırakma: `≈0` / `[?]` / sıralı ölçek kullan; boş eksen karşılaştırmayı bozar.
- Salih "bu bir emirdir" dediyse model sunma — tek istisna m.16 çelişki raporu (rapor emri değiştirmez).
