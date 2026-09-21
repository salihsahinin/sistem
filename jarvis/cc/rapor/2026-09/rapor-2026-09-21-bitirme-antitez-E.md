# Antitez Raporu (¬E) — Bitirme Tezi İddia Seti E

**Çekim tarihi (AS-OF):** 2026-09-21
**Rol:** Atlas ANTİTEZ ajanı — Devil's Advocate, tez raporunu görmeden, yalnız iddia listesinden çalıştı (CoVe-Factored, bağımsız).
**Disiplin notu:** WebSearch bütçesi koşum sırasında tükendi (oturum payı paylaşımlı); E11/E12 sonrası araştırma tamamen WebFetch ile (doğrudan arşiv/kurum sayfaları) yürütüldü. Model hafızası ayrı işaretlenir, hiçbir sayı doğrulanmadan rapor edilmez.

---

## İddia Başına Sonuç

### E1 — Princeton matematik senior thesis: resmî sayfa sınırı yok, tipik 20-40 sayfa
**Çürütme girişimi:** math.princeton.edu bölüm sayfası doğrudan WebFetch ile açıldı.
**Bulgu:** Sayfa birebir doğruluyor: "there are no formal length requirements... About 20-40 pages when single-spaced seems typical." En iyi tezlerin bazıları 10 sayfa altı, bazıları 100 sayfa üstü.
**Kaynak:** https://www.math.princeton.edu/undergraduate/majors/independent-work (AS-OF 2026-09-21)
**Sonuç:** ÇÜRÜTÜLEMEDİ

### E2 — Cambridge Part III essay: 5.000-8.000 kelime, 20-30 sayfa
**Çürütme girişimi:** maths.cam.ac.uk ve dpmms.cam.ac.uk (T.W. Körner, "How to Write a Part III Essay") kaynaklarında arandı.
**Bulgu:** "expected length... normally be between 20 and 30 pages and should only exceptionally be more than 35 pages"; "an excellent essay typically requires about 5000 words... unhappy if a topic required more than about 8000 words." Sayılar örtüşüyor.
**Kaynak:** https://www.maths.cam.ac.uk/postgrad/part-iii/current/examinations-and-essays · https://www.dpmms.cam.ac.uk/~twk10/Essay.pdf (AS-OF 2026-09-21, WebSearch snippet üzerinden — doğrudan WebFetch denenmedi, bütçe kısıtı)
**Sonuç:** ÇÜRÜTÜLEMEDİ (dar doğrulama: birincil kaynak snippet düzeyinde teyit edildi, tam sayfa WebFetch yapılmadı)

### E3 — Oxford Part C dissertation: 7.500 kelime sınırı
**Çürütme girişimi:** maths.ox.ac.uk dissertations sayfası doğrudan WebFetch.
**Bulgu:** "a written dissertation with a word limit of 7,500 words, which usually equates to 25-35 pages... absolute page limit of 50 pages." İddiadaki rakam birebir, ek olarak 50 sayfa mutlak tavan bilgisi bulundu (iddiada yoktu, tamamlayıcı).
**Kaynak:** https://www.maths.ox.ac.uk/members/students/undergraduate-courses/teaching-and-learning/part-c-students/teaching-and-learning/dissertations (AS-OF 2026-09-21)
**Sonuç:** ÇÜRÜTÜLEMEDİ

### E4 — Princeton dört ölçüt: alan bilgisi, özgünlük, titiz mantık, net sunum
**Çürütme girişimi:** Aynı bölüm sayfası WebFetch ile taranıp dört ölçüt madde madde karşılaştırıldı.
**Bulgu:** Sayfa dört ayrı başlık altında neredeyse birebir aynı dili kullanıyor: "advanced mathematical content... substantial familiarity with the relevant literature", "original point of view or individual mathematical style", "mastery of rigorous logical thinking", "clear mathematical exposition."
**Kaynak:** https://www.math.princeton.edu/undergraduate/majors/independent-work (AS-OF 2026-09-21)
**Sonuç:** ÇÜRÜTÜLEMEDİ

### E5 — Stanford CS senior project: beş farklı ders/yol
**Çürütme girişimi:** cs.stanford.edu/bs-requirements-senior-project sayfası doğrudan WebFetch, tüm seçenekler tek tek sayıldı.
**Bulgu:** Tam beş seçenek listelendi: (1) CS194/CS194W, (2) CS210B (kurumsal ortaklı proje), (3) CS191/CS191W (bağımsız araştırma), (4) Senior Honors Thesis, (5) CS294 (yönlendirilmiş araştırma).
**Kaynak:** https://www.cs.stanford.edu/bs-requirements-senior-project (AS-OF 2026-09-21)
**Sonuç:** ÇÜRÜTÜLEMEDİ (sayı tam eşleşti)

### E6 — Imperial, Kevin Buzzard "Formalising Mathematics", Lean 4, son sınıf lisans + MSc
**Çürütme girişimi:** Kevin Buzzard'ın resmî kurs sayfası WebFetch ile açıldı, hedef kitle cümlesi aranarak "MSc" ifadesi doğrulanmaya çalışıldı.
**Bulgu:** Sayfa "This document is written for people with some mathematical experience (e.g., people in the final year of an undergraduate mathematics degree)" diyor — "e.g." (örneğin) kullanımı bu kitleyi TEK hedef olarak değil ÖRNEK olarak sunuyor; fetch edilen metinde "MSc" ifadesi açıkça geçmiyor (ayrı bir bölümde olabilir, doğrulanamadı). 2024 sürümünün Lean 4 ile yazıldığı ve Ocak-Mart 2024'te koştuğu ayrıca doğrulandı.
**Kaynak:** https://www.ma.imperial.ac.uk/~buzzard/xena/formalising-mathematics-2024/ · https://github.com/ImperialCollegeLondon/formalising-mathematics-2024 (AS-OF 2026-09-21)
**Sonuç:** DARALDI: koşul — Lean 4 + son-sınıf-lisans kısmı doğrulandı; "MSc" ifadesi fetch edilen sayfada bulunamadı, "e.g." dili iddianın "yalnızca bu iki grup" ima ettiği kesinliği zayıflatıyor.

### E7 — CMU 15-311/15-217, Lean etkileşimli kanıt asistanı
**Çürütme girişimi:** cs.cmu.edu/~mheule kurs sayfaları ve avigad.github.io/lamr resmî ders notları WebSearch snippet'iyle tarandı.
**Bulgu:** Her iki kurs numarası da (15-311 ve 15-217) aynı içeriği farklı dönemlerde sunuyor; ders açıkça "Lean 4 programming language and theorem prover" ile SAT/SMT çözücüleri birlikte kullanıyor, Lean'i "interactive theorem prover" olarak konumlandırıyor.
**Kaynak:** https://www.cs.cmu.edu/~mheule/15217-f21/ · https://www.cs.cmu.edu/~mheule/15311-s25/ · https://avigad.github.io/lamr/ (AS-OF 2026-09-21)
**Sonuç:** ÇÜRÜTÜLEMEDİ

### E8 — Harvard SEAS 2024 lisans tezi (Leonard Tang), LLM sağlamlığı/matematiksel başarısızlık
**Çürütme girişimi:** Harvard DASH kayıt sayfası doğrudan WebFetch ile açılıp derece türü (PhD mi Bachelor mı?) sorgulandı.
**Bulgu:** Atıf metni birebir: "Tang, Leonard. 2024. Automated and Flexible Stress-Testing for the Robustification of Large Language Model Systems. **Bachelors Thesis**, Harvard University Engineering and Applied Sciences." Özet, LLM'lerin "temel aritmetikte zorlanma" gibi çelişkilerinden bahsediyor — "matematiksel görevlerdeki başarısızlıklar" çerçevesiyle örtüşüyor.
**Kaynak:** https://dash.harvard.edu/items/1639db4a-f7ab-4e39-8c2d-6a2edfc0af01 (AS-OF 2026-09-21)
**Sonuç:** ÇÜRÜTÜLEMEDİ

### E11 — Üst-13 kurumun 5 isimli arşivinde ("Lean 4"/"autoformalization"/"physics-informed" + 2024-2026 lisans tezi) doğrulanmış kayıt yok
**Çürütme girişimi (iki okuma ayrıştırıldı):**
- **Dar okuma** (tam anahtar kelime + tam olarak bu 5 arşiv): Harvard DASH'te doğrudan arama yapıldı — "senior thesis" + "autoformalization" → **"Your search returned no results."** Ayrıca "physics-informed" + "senior thesis" → **yine sıfır sonuç.** İki sorgu da doğrudan WebFetch ile teyit edildi. Princeton DataSpace (dataspace.princeton.edu) iki farklı URL biçimiyle denendi, ikisi de **401 Unauthorized** döndü — erişilemedi, iddia ne doğrulanabildi ne çürütülebildi. MIT DSpace (dspace.mit.edu) arama sayfası **404** verdi. ETH Research Collection'da ilgili bir bitstream iki kez **429 Too Many Requests** ile bloklandı.
- **Geniş okuma** (aynı konular, üst-düzey kurumlarda HERHANGİ bir lisans tezi/araştırma projesi, 5 arşive sınırlı olmadan — EK-SORU-1'in asıl kapsamı): TUM'un Physics-enhanced Machine Learning kürsüsü sayfasında üç adet AÇIKÇA "Bachelor thesis" etiketli, fizik+sinir-ağı temalı tez bulundu (bkz. EK-SORU-1 tablosu), Harvard DASH'te Leonard Tang'ın 2024 Bachelor's tezi (LLM matematik-bitişik) doğrulandı, Duke Math+ 2024 programında "AlgebraInLean" adlı Lean 4 tabanlı LİSANS ARAŞTIRMA PROJESİ bulundu.
**Kaynak:** https://dash.harvard.edu (arama sonuçları, AS-OF 2026-09-21) · https://dataspace.princeton.edu (401, AS-OF 2026-09-21) · https://dspace.mit.edu (404, AS-OF 2026-09-21) · https://www.research-collection.ethz.ch (429, AS-OF 2026-09-21) — ayrıntılar EK-SORU-1 tablosunda.
**Sonuç:** DARALDI: koşul — dar/lafzi okuma (tam anahtar kelime + isimlendirilmiş 5 arşiv) elde edilen kanıtla AYAKTA KALDI (Harvard DASH'te iki doğrudan sorgu sıfır sonuç verdi; diğer üç arşiv erişilemedi, çürütülemedi de doğrulanamadı da). Ancak iddianın taşıdığı geniş çıkarım — "bu konularda hiçbir üst-kurum lisans çalışması yok" — TUM/Harvard/Duke örnekleriyle KISMEN ÇÜRÜDÜ; sadece isimlendirilen 5 arşivin dışında.

### E12 — Imperial, ETH, EPFL, TUM'da "senior thesis" kalıbının doğrudan karşılığı yok
**Çürütme girişimi:** Dört kurumun resmî müfredat sayfaları tek tek WebFetch ile açıldı.
**Bulgu:**
- **ETH Zürih:** Bachelor Mathematics müfredat sayfası üçüncü yıl bileşenleri arasında açıkça **"Seminars, Bachelor's thesis"** listeliyor — doğrudan karşılık VAR.
- **EPFL:** MATH-397 "Mathematics project (bachelor)" — 5. VE 6. dönemde ZORUNLU, 14 hafta × 12 saat/hafta, 12 kredi, yazılı rapor + sözlü sunum zorunlu. Bu, ABD-tipi senior thesis'e yapısal olarak çok yakın — doğrudan karşılık VAR.
- **TUM:** SCML kürsüsü sayfasında beş öğrencinin işi açıkça "Bachelor thesis" (Bachelorarbeit) etiketiyle listeleniyor — doğrudan karşılık VAR.
- **Imperial:** Yalnız M4R (4. yıl MSci araştırma projesi) bulundu; bu, entegre yüksek lisans (MSci) programının 4. yılına özgü, standart 3 yıllık BSc matematik derecesinde zorunlu bir tez olup olmadığı bu koşumda DOĞRULANAMADI.
**Kaynak:** https://ethz.ch/en/studies/bachelor/bachelors-degree-programmes/natural-sciences-and-mathematics/mathematics.html · https://edu.epfl.ch/coursebook/en/mathematics-project-bachelor-MATH-397 · https://www.cs.cit.tum.de/en/scml/teaching/student-projects/ (üçü de AS-OF 2026-09-21)
**Sonuç:** ÇÜRÜDÜ (üç kurum için: ETH, EPFL, TUM — açık ve isimlendirilmiş "Bachelor's thesis/project" yapıları bulundu) + DARALDI (Imperial için: yalnız MSci/4.-yıl M4R doğrulandı, 3 yıllık BSc'de zorunlu tez doğrulanamadı — iddia bu tek kurum için ayakta kalabilir).

---

## EK-SORU-1 — Lisans tezi/araştırma projesi örnekleri (2024-2026)

**Hedef:** ≥8 doğrulanmış örnek. **Elde edilen:** 5 doğrulanmış + 1 bulunan-ama-erişilemeyen (bayraklı). Diğer sekiz kurumda (MIT, Princeton, Cambridge, Oxford, Stanford, Berkeley, Caltech, CMU, Imperial, EPFL) bu koşumda doğrulanmış bir örnek BULUNAMADI — bunun nedeni kanıtlanmış yokluk değil, WebSearch bütçesinin tükenmesi + birden fazla arşivin 401/404/429 ile erişime kapalı olmasıdır (aşağıda ayrıntılı).

| Kurum | Yıl | Başlık | Yazar | Konu | Lisans kanıtı | URL |
|---|---|---|---|---|---|---|
| TUM (SCML) | 2024 | Solving the three-body problem with neural networks | Andreas Merrath | Fizik + sinir ağı | Sayfada açıkça "Bachelor thesis" | https://www.cs.cit.tum.de/en/scml/teaching/student-projects/ |
| TUM (SCML) | 2025 | Learning Hamiltonian Functions of Handwritten Digits using Neural Networks | Cagan Akin | Fizik-bilgili ML (Hamiltonian) | Sayfada açıkça "Bachelor thesis" | https://www.cs.cit.tum.de/en/scml/teaching/student-projects/ |
| TUM (SCML) | 2026 | Random Feature Hamiltonian Networks for N-Body Problems | Sofia Koufogazou Loukianova | Fizik-bilgili ML | Sayfada açıkça "Bachelor thesis" | https://www.cs.cit.tum.de/en/scml/teaching/student-projects/ |
| Harvard SEAS | 2024 | Automated and Flexible Stress-Testing for the Robustification of Large Language Model Systems | Leonard Tang | LLM matematik/sağlamlık | DASH atıf metninde "Bachelors Thesis" | https://dash.harvard.edu/items/1639db4a-f7ab-4e39-8c2d-6a2edfc0af01 |
| Duke Math+ | 2024 | AlgebraInLean (AIL) | Öğrenci ekibi (PM: Colleen Robles) | Lean 4 formalizasyonu | "Undergraduate research program" (tez değil, lisans ARAŞTIRMA PROJESİ) | https://math.duke.edu/mathplus/2024/formalization-mathematics |
| ETH Zürih | belirsiz | Formalizing Automated Market Makers in the Lean 4 Theorem Prover | belirsiz | Lean 4 formalizasyonu | **BULUNDU AMA DOĞRULANAMADI** — bitstream 2 denemede 429 döndü | https://www.research-collection.ethz.ch/server/api/core/bitstreams/4deec035-9831-47b5-b1c1-6edc7d15bc07/content |

**Erişim engelleri (bayraklı, çürütme ne başarılı ne başarısız sayılır):**
- Princeton DataSpace: 401 Unauthorized (2 deneme, 2 farklı URL biçimi)
- MIT DSpace: arama sayfası 404, ana thesis-arşiv sayfası (math.mit.edu/academics/undergrad/uthesis.php) 404
- Cambridge Apollo (repository.cam.ac.uk): tek bulunan kayıt bir NeurIPS 2022 konferans bildirisiydi ("Autoformalization with Large Language Models", Wu/Jiang/Li/Rabe/Staats), lisans tezi DEĞİL — WebFetch ile doğrudan doğrulandı.
- Cambridge CST Part II arşivi (cl.cam.ac.uk/teaching/projects/overseers/archive.html): Microsoft OAuth login'e yönlendirdi, kimlik doğrulama gerektiriyor — erişilemedi.

**Genel değerlendirme:** ≥8 hedefine ulaşılamadı (5/8 + 1 bayraklı). Bulunanlar E11'in lafzi/dar okumasını çürütmüyor (isimlendirilen 5 arşivin dışında kaldılar) ama E11/E12'nin taşıdığı geniş iddiayı — "bu konularda üst-düzey kurumlarda hiçbir lisans işi yok" — kısmen çürütüyor.

## EK-SORU-2 — Jüri riskleri hakkında ders/yönerge düzeyinde uyarı

**Aranan kaynaklar:** Stanford CS senior project SSS sayfası, Princeton matematik bölümü majors-info PDF'i (2021 sürümü, kısmen okunamadı — sıkıştırılmış/kodlanmış metin), Duke Math+ formalizasyon programı sayfası, Kevin Buzzard'ın Imperial kurs sayfası.
**Bulgu:** Hiçbirinde "AI kanıt açıklama / Lean→doğal dil" ya da "LLM matematik değerlendirme" konusunun özgünlük, tekrarlanabilirlik ya da hızla eskime riski hakkında ders/yönerge düzeyinde açık bir uyarı BULUNAMADI.
**Sonuç:** BULUNAMADI. Bu, böyle bir uyarının hiçbir yerde var olmadığı anlamına gelmez — WebSearch bütçesi bu soruya ayrılan taramadan önce tükendiği için tarama sığ kaldı (yalnız 4 sayfa WebFetch ile kontrol edildi, department-özel "thesis proposal guidelines" ya da akademik-dürüstlük sayfaları taranamadı). Epistemik durum: DÜŞÜK GÜVEN, negatif sonuç — yokluk kanıtı değil, arama-sınırlılığı kanıtı.

---

## Kaynak Hiyerarşisi Notu
Birincil kaynaklar (bölüm/kurum resmî sayfaları, arşiv kayıt sayfaları) ağırlıklı kullanıldı. WebSearch snippet'leri (E2, E7) ikincil doğrulama düzeyinde kaldı — doğrudan WebFetch ile teyit edilmedi, bütçe kısıtı nedeniyle. Model hafızası (kesim öncesi) hiçbir iddiada tek başına kaynak olarak kullanılmadı; her sonuç canlı arama/fetch ile bağlandı.

## Açılan Kaynak Sayısı
WebFetch ile açılan benzersiz URL sayısı: 20+ (başarılı içerik dönenler ~14, hata/blok dönenler ~8: 401×2, 404×3, 429×2, 302-auth×1). ≥5 şartı fazlasıyla karşılandı.
