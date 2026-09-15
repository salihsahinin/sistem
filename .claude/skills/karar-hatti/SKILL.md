---
name: karar-hatti
description: Ölçek-eşiği üstü kararı BAŞTAN SONA işleyen orkestratör — çocuk skill'leri sırayla çağırır, kendisi iş yapmaz: (1) celiski-kapisi (m.16; çelişkide DURUR) → (2) gerekirse atlas-kosum (m.40b araştırma-önce) → (3) karar-modeli (m.37) → (4) sunum + defter-bloğu TASLAĞI. Kullan: "tam karar hattı", "bu kararı hattan geçir", "baştan sona işle" dendiğinde ya da yeni mekanizma/araç sınıfı kararlarda. KULLANMA: su-bardağı işler; tekil ihtiyaçta çocuğu tek çağır ("3 model sun" → karar-modeli, "araştır" → atlas-kosum, "çelişki var mı" → celiski-kapisi). argument-hint: "<karar sorusu tek cümle>"
metadata: { owner: jarvis, version: "0.1.0-deneysel-m29" }
---

# karar-hatti — orkestratör koşum talimatı

Kanon zinciri: m.16 · m.37 · m.40 (a-b-c + v0.2) · m.31 (katmanlar) · m.44 (orkestrasyon Jarvis'te — bu skill üst-orkestratör şapkasının karar-işleme hattı). İlke: orkestratör İNCE kalır — iş çocuklarda, sıra ve kapılar burada (decomposition kalitesi asıl kaldıraç).

## Adımlar

1. **Ölçek + tekil-ihtiyaç kontrolü.** Eşik altı → hat koşmaz, iş direkt. Tekil ihtiyaç (yalnız araştırma / yalnız 3-model / yalnız çelişki) → ilgili çocuğu TEK BAŞINA çağır, hattı açma (m.25).
2. **Karar sorusunu sabitle.** Tek cümle + m.38 formu; hat boyunca değişmez (değişirse hat BAŞA döner — kayan-soru freni).
3. **ÇOCUK 1 — celiski-kapisi.** Kanon taraması. Çıktı iki yollu: **temiz** → devam · **çelişki** → HAT DURUR; çelişki raporu Salih'e/ana-sıraya taşınır, atlas ve karar-modeli ÇAĞRILMAZ (çelişki çözülmeden model karşılaştırması israf). Salih yönü geldikten sonra hat kaldığı yerden ya da başa dönerek koşar.
4. **Araştırma-önce kontrolü (m.40b).** Soru "dışarıda çözülmüş olma ihtimali olan" sınıfta mı (yeni mekanizma/araç/desen)? **Evet** → **ÇOCUK 2 — atlas-kosum** (v0.2 multi-hop; rapor sunumdan ÖNCE biter). **Hayır — iç-önceliklendirme** → atlas ATLANIR (m.40b muafiyeti; muafiyet dönemsel geriye-dönük denetime tabi — bunu sunumda tek satırla belirt).
5. **ÇOCUK 3 — karar-modeli.** m.37: 3 model (token×zaman×beklenen-kalite, sayısal) + karşıt-temel + RİSK boyutu (m.42e). Atlas koşulduysa bulguları (hayatta-kalan çekirdek + düşen iddialar) kanıt olarak BESLE — model seçenekleri saha örnekleriyle desteklenir.
6. **Sunum (m.40a).** "Bu ne / neden masada" özetiyle görünür sunum. Katman ayrımı: **Katman-2** → önerilen işaretli, onay BEKLENMEZ, veto açık · **Katman-1** (kanon/kural, pahalı geri-alma, para, rol, dışarı çıkan iş) → Salih imzası BEKLENİR.
7. **Kayıt taslağı — yazım YOK.** Senaryo-defteri bloğunu şablona uygun TASLAK olarak üret ve sunuma iliştir; defter yazımı + commit hattın DIŞINDA, seans akışında yapılır (yan-etki freni; ileride ayrı elle-tetik `karar-kaydet` skill'i — S-kutusu adayı).

## Gotchas

- Orkestratöre iş kaçırma — çelişki analizi, arama, model üretimi ÇOCUKLARDA yaşar; orkestratör sıra+kapı+veri-taşıma yapar. Şişen orkestratör = iki yerde yaşayan, ayrışan mantık.
- Çocuklar arası veri geçişinde HAM VERİ taşı (çelişki raporu metni, atlas iddia+kanıt listesi), kendi özetinle inceltme — m.40b v0.2 arayüz kuralının hat-içi karşılığı.
- Adım 3 kapısını "küçük çelişki, devam edelim" diye ezme — kapının değeri erken durmasında; DARALTMA etiketi geldiyse (çelişki değil) devam meşru, raporda görünür.
- Soru hat ortasında evrilirse yeni soru = yeni hat (adım 2 freni); eski koşum çıktıları yeni soruya miras "kanıt" değildir.
- Hat defter yazmaz, kanon yazmaz, commit atmaz (yan-etki freni). Taslak üretir, teslim eder.
