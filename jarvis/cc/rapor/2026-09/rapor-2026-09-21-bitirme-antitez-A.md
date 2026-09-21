# Antitez Raporu A — "AI Navier-Stokes'u Çözdü" İddia Kümesi

**Rol:** Atlas ANTİTEZ (¬A) — Devil's Advocate, tez raporunu görmeden, yalnız iddia listesiyle çalıştı (CoVe-Factored).
**Çekim tarihi (sistem):** 2026-09-21
**Yöntem:** Her iddia için aksini/daraltan kanıt arandı; WebSearch + WebFetch + arXiv API (curl) ile ≥3 kaynak fiilen açıldı.

---

## A1 — DeepMind/Brown/NYU/Stanford Eylül 2025 çalışması, Millennium Prize iddia etmedi

**Çürütme girişimi:** Kurum listesi doğru mu, denklem listesi doğru mu, Millennium Prize iddiası gerçekten yok mu diye kontrol edildi. Birincil kaynak olarak arXiv API'den (WebFetch'in PDF-özet araçlarının tutarsız/olası halüsinasyonlu sonuçlar verdiği görüldüğü için) ham özet metni çekildi.

**Bulunan kanıt:**
- arXiv 2509.14185 "Discovery of Unstable Singularities" — resmi özet (arXiv API, `export.arxiv.org/api/query?id_list=2509.14185`, ham XML): "we present multiple new, unstable self-similar solutions for **the incompressible porous media equation and the 3D Euler equation with boundary**" — yeni aileler yalnız **IPM** ve **sınırlı-alan (boundary'li) 3D Euler** için bulunmuş. Özet metni, "**boundary-free Euler and Navier-Stokes cases**" ifadesini AÇIK/çözülmemiş problem olarak anıyor, keşfedilen denklemler arasında saymıyor.
- DeepMind blog (deepmind.google/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/, 2025-09-18): kurumlar "Brown University, New York University and Stanford University" + Google DeepMind olarak doğrulandı; makale Millennium Prize'ın çözüldüğünü **iddia etmiyor** — "Finding any singularity in the Navier-Stokes equations is one of the six famous Millennium Prize Problems that are still unsolved" cümlesiyle açıkça çözülmedi diyor.
- İkincil kaynaklar (emergentmind, WebSearch özetleri) makalenin gövdesinde 2D Boussinesq denklemi için de sonuç (1 kararlı + 3 kararsız + aday 4. kararsız çözüm) bulunduğunu belirtiyor — bu A1'in listesinde YOK, ama gerçek denklem kapsamının bir parçası.
- WebFetch'in `arxiv.org/pdf/2509.14185` denemesi makaleyi "CCF model (1D active scalar)" olarak tanımladı — bu, arXiv API'nin ham özetiyle DOĞRUDAN ÇELİŞİYOR ve muhtemelen PDF ayrıştırma hatası/halüsinasyon; bu nedenle bu özel bulgu **reddedildi**, yalnız API'nin ham metni esas alındı.

**URL:** https://export.arxiv.org/api/query?id_list=2509.14185 (AS-OF 2026-09-21) · https://deepmind.google/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/ (AS-OF 2026-09-21, yayın 2025-09-18) · https://arxiv.org/abs/2509.14185

**Sonuç: DARALDI.** Kurum listesi (DeepMind+Brown+NYU+Stanford) ve "Millennium Prize'ı çözdüğünü iddia etmedi" kısmı doğrulandı. Ancak **denklem listesi abartılı**: resmi özet yalnız IPM + sınırlı-alan 3D Euler için "yeni aile keşfedildi" diyor; "Navier-Stokes" ve sınırsız (boundary-free) "Euler" özet metninde AÇIK PROBLEM olarak anılıyor, keşif listesinde değil. Doğru koşul: "...IPM, sınırlı-alan Euler (ve muhtemelen 2D Boussinesq) denklemlerinde... ama Euler (sınırsız) ve Navier-Stokes'ta DEĞİL, bunlar motive edici açık problem olarak anıldı."

---

## A2 — Buckmaster (NYU) + Alpöge (Anthropic), Eylül 2026, IPM/2D Boussinesq/3D Euler zorlamalı sonlu-zaman patlaması, Lean'de biçimsel kanıt

**Çürütme girişimi:** Tarih, isimler, kurumlar, denklem listesi, "Lean'de biçimsel kanıt" iddiası sorgulandı.

**Bulunan kanıt:**
- Terence Tao blog (terrytao.wordpress.com, gönderi tarihi 2026-09-07): başlık bizzat "Finite time blowup **with smooth forcing term** for the incompressible porous medium, Boussinesq, and incompressible Euler equations" — üç denklem (IPM, Boussinesq, Euler) ve "smooth forcing" (düzgün zorlama) teyit edildi.
- Aynı kaynak: "As is now remarkably feasible in the modern era of autoformalization agents, their work has also been formalized in Lean" — Lean formalizasyonu teyit edildi.
- Unite.AI (unite.ai/buckmaster-and-alpoge-post-ai-fluid-blowup-proofs-dispute-openai-contact/): yazarlar Tristan Buckmaster (NYU) ve Levent Alpöge (Anthropic) olarak doğrulandı, üç ayrı preprint + Lean formalizasyonları içeren kamuya açık repo.
- lilting.ch zaman çizelgesi: "15 Ağustos: Boussinesq/Euler sonuçları… 7 Eylül (geç): Buckmaster'ın makaleleri yayınlandı" — yayın Eylül 2026 içinde, A2 ile uyumlu.

**URL:** https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/ (AS-OF 2026-09-21) · https://www.unite.ai/buckmaster-and-alpoge-post-ai-fluid-blowup-proofs-dispute-openai-contact/ (AS-OF 2026-09-21) · https://lilting.ch/en/articles/navier-stokes-openai-blowup-dispute (AS-OF 2026-09-21)

**Sonuç: ÇÜRÜTÜLEMEDİ.** İddianın hiçbir öğesine (isim, kurum, tarih, denklem listesi, "zorlamalı", "Lean'de biçimsel kanıt") karşı kanıt bulunamadı; birden çok bağımsız kaynak (Tao'nun kendi blogu, Unite.AI, lilting.ch) çapraz doğruluyor.

---

## A3 — Terence Tao, Buckmaster-Alpöge çalışmasını "muazzam bir başarı" diye niteledi ve Lean formalizasyonunu doğruladı

**Çürütme girişimi:** Tam alıntı arandı; "doğruladı" kelimesi Tao'nun bizzat Lean kodunu çalıştırıp kontrol ettiği anlamına mı geliyor, yoksa yalnız varlığını mı not ediyor diye ayrıştırıldı.

**Bulunan kanıt:**
- X/officechai.com (officechai.com/ai/terrance-tao-calls-buckmaster-alpoges-fluid-dynamics-proofs-a-remarkable-achievement…): başlıkta bizzat "a remarkable achievement" ifadesi — "muazzam bir başarı" çevirisiyle örtüşüyor, teyit edildi.
- Tao'nun blogundan WebFetch: "they have made enough of a breakthrough that it looks very feasible to complete these goals in the near future" — güçlü olumlu nitelendirme teyit edildi.
- Lean konusunda Tao'nun TAM cümlesi: "their work has **also been formalized** in Lean" — yalnız VARLIĞINI bildiriyor. Tao ayrıca "I was also fortunate to have Tristan Buckmaster explain the main ideas… although I still need to work some more…to digest things more" diyor — yani kendisi işi **tam sindirmediğini** açıkça itiraf ediyor. Tao'nun bizzat Lean derleyicisini çalıştırdığına veya kanıtı satır satır doğruladığına dair hiçbir ifade bulunamadı.

**URL:** https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/ (AS-OF 2026-09-21) · https://officechai.com/ai/terrance-tao-calls-buckmaster-alpoges-fluid-dynamics-proofs-a-remarkable-achievement-says-could-help-solve-navier-stokes/ (AS-OF 2026-09-21, WebSearch üzerinden görüldü, doğrudan fetch edilmedi)

**Sonuç: DARALDI.** "Muazzam bir başarı" kısmı ("remarkable achievement") sözcüğü sözcüğüne teyit edildi. Ama "Lean formalizasyonunu doğruladı" fazlası: Tao yalnız formalizasyonun **var olduğunu** bildiriyor ve kendisinin konuyu **tam sindirmediğini** itiraf ediyor; kendisinin bağımsız olarak Lean kanıtını çalıştırıp/kontrol edip "doğruladığına" dair kanıt yok. Doğru koşul: "...ve Lean formalizasyonunun VAR OLDUĞUNU blogunda belirtti (kendisinin bizzat derleyip teyit ettiğine dair ifade yok)."

---

## A4 — OpenAI, 8 Eylül 2026, dahili modelle Navier-Stokes sonlu-zamanda tekillik iddiası

**Çürütme girişimi:** Tarih, "dahili/unreleased model" detayı, "Navier-Stokes" (Euler değil) detayı sorgulandı.

**Bulunan kanıt:**
- Çoklu bağımsız kaynak (WebSearch özetleri: kingy.ai, xenospectrum.com, ultrathink.ai, fortune.com) tutarlı: "OpenAI announced on September 8, 2026, that an unreleased internal model had proved finite-time blowup for the three-dimensional Navier–Stokes equations."
- xenospectrum.com fetch: "OpenAI, 3D sıkıştırılamaz Navier-Stokes denklemlerinde sonlu zamanda tekillik (blowup) oluştuğunu iddia etmektedir… pürüzsüz zorlamanın mevcut olduğu senaryo."
- GitHub deposu adı bulundu: `openai/NavierStokesAndEuler` (Lean sertifikaları) — hem NS hem Euler sonuçlarını barındırdığını gösteriyor (bkz. A5).

**URL:** https://xenospectrum.com/en/openai-navier-stokes-singularity-clay-dispute/ (AS-OF 2026-09-21) · https://kingy.ai/blog/navier-stokes-ai-proof-claims-dispute/ (AS-OF 2026-09-21) · openai.com/index/navier-stokes-solution/ (403 Forbidden, WebFetch ile doğrudan açılamadı — bkz. Engeller)

**Sonuç: ÇÜRÜTÜLEMEDİ.** Tarih (8 Eylül 2026), "dahili/yayınlanmamış model" ve "Navier-Stokes" detaylarının hiçbirine karşı kanıt bulunamadı; birden çok bağımsız haber kaynağı örtüşüyor.

---

## A5 — Açık kaynaklar, OpenAI'nin kanıtladığı denklem/zorlama konusunda birbiriyle çelişiyor

**Çürütme girişimi:** Bu iddianın kendisi zaten "kaynaklar arasında belirsizlik var" diyor; bunu doğrulamak için erken ve geç dönem haberleri karşılaştırıldı, ayrıca "gerçekten çelişki var mı yoksa artık netleşti mi" sorgulandı.

**Bulunan kanıt:**
- WebSearch sentezi (Scientific American, WebNovis, kingy.ai, thenextweb.com üzerinden): "OpenAI produced **two separate results: forced Navier–Stokes and unforced Euler**… OpenAI's agents first resolved the unforced Euler regularity problem, using nearly 100 agents in roughly 50 hours… Earlier coverage, including Scientific American's statement that the Clay formulation was solved, preceded the public proof… many outlets conflated OpenAI's forced Navier-Stokes result with the more difficult unforced versions."
- kingy.ai fetch: OpenAI'nin ana iddiası "zorlamalı Navier-Stokes" (Teorem 1.1, Clay'in C/D seçenekleri) + AYRICA "zorlamasız Euler" sonucu — iki farklı sonuç aynı duyuru içinde, medyada karıştırılmış.
- xenospectrum.com fetch ise OpenAI'nin sonucunu tek/net "3D sıkıştırılamaz Navier-Stokes, zorlamalı" olarak anlatıyor, Euler'i yalnız Buckmaster-Alpöge'ye atfediyor — bu, kingy.ai'nin "OpenAI'nin AYRICA bir Euler sonucu da var" tespitiyle **doğrudan örtüşmüyor** (biri OpenAI'ye iki sonuç atfediyor, diğeri yalnız NS atfediyor).

**URL:** https://kingy.ai/blog/navier-stokes-ai-proof-claims-dispute/ (AS-OF 2026-09-21) · https://xenospectrum.com/en/openai-navier-stokes-singularity-clay-dispute/ (AS-OF 2026-09-21) · https://www.scientificamerican.com/article/openai-claims-blockbuster-math-breakthrough-amid-swirl-of-controversy/ (WebSearch özetinden, doğrudan fetch edilmedi)

**Sonuç: ÇÜRÜTÜLEMEDİ (aksine, doğrulandı).** Kaynaklar arasında gerçek bir ayrışma bulundu: (a) OpenAI'nin duyurusunun kaç ayrı sonuç içerdiği (yalnız zorlamalı NS mi, yoksa AYRICA zorlamasız Euler de mi) konusunda ikincil kaynaklar birbiriyle uyuşmuyor; (b) erken haberler (ör. Scientific American) kanıt yayınlanmadan önce "Clay problemi çözüldü" demiş, sonradan düzeltilmiş. İddia güçlü destek buluyor.

---

## A7 — Clay Matematik Enstitüsü resmî sitesi, 21 Eylül 2026 itibarıyla Navier-Stokes'u "Active" listeliyor, ödül duyurusu yok

**Çürütme girişimi:** Site doğrudan fetch edildi; ayrıca CMI'nin 11 Eylül 2026 "apparently settled" duyurusuyla çelişip çelişmediği kontrol edildi.

**Bulunan kanıt:**
- Doğrudan WebFetch (claymath.org/millennium-problems/navier-stokes-equation/): "Sayfanın başında 'Active' etiketi bulunmaktadır… problemin hala çözülmemiş ve açık bir Millennium Prize Problem olarak devam ettiğini göstermektedir." Sayfanın kesin son güncelleme tarihi görünmüyor ama telif hakkı "© 2026".
- CMI'nin ayrı duyuru sayfası (claymath.org/news/navier-stokes-announcement/, 11 Eylül 2026): "problem görünüşte çözülmüştür" (apparently settled) diyor AMA "sorunu tam olarak çözen kişi/kişiler duyuruda adlandırılmamış", "değerlendirme süreci kasıtlı olarak yavaş", ödül verilmedi. Bu, ana problem listeleme sayfasının hâlâ "Active" etiketini taşımasıyla **çelişmiyor** — ikisi de "resmi ödül/kesinleşme yok" sonucuna varıyor, yalnız duyuru sayfası daha "kutlayıcı" bir dil kullanıyor.

**URL:** https://www.claymath.org/millennium-problems/navier-stokes-equation/ (AS-OF 2026-09-21) · https://www.claymath.org/news/navier-stokes-announcement/ (AS-OF 2026-09-21, gönderi 2026-09-11)

**Sonuç: ÇÜRÜTÜLEMEDİ.** İddianın her öğesi (Active statüsü, ödül duyurusu yok, 21 Eylül itibarıyla) doğrudan site fetch'iyle teyit edildi.

---

## A8 — Buckmaster, Bubeck'in kendisini tehdit ettiğini ve OpenAI'nin verilerine izinsiz eriştiğini iddia etti

**Çürütme girişimi:** "Tehdit" kelimesinin abartı olup olmadığı, Bubeck'in kendi versiyonuyla çelişip çelişmediği kontrol edildi.

**Bulunan kanıt:**
- thenextweb.com başlığı: "OpenAI's Bubeck denies trying to cut Anthropic mathematician from credit" — Bubeck kendi versiyonunu anlatıyor, SUÇLAMAYI TAMAMEN reddetmiyor ama çerçeveyi değiştiriyor.
- WebSearch sentezi: Buckmaster'a göre Bubeck "Why would you ruin your career?" dedi, akademisyen olduğunu hatırlattığında "If you don't want me to be nice, then I don't have to be nice" yanıtını verdi — bu, "tehdit" olarak okunabilecek somut alıntı.
- Bubeck'in kendi tarafı: "never ever" Alpöge'yi yazarlıktan çıkarmayı istemediğini söylüyor, görüşmenin "hostile" hale geldiğini ve kendisinin "a litany of slander" ile karşılaştığını iddia ediyor — yani Bubeck de KARŞI-İDDİADA bulunuyor (suçlamaların asılsız olduğunu iddia ediyor).
- Veri erişimi: Buckmaster "whether the model had been trained on, or had access to, our sessions in Codex" diye SORUYOR — bu kesin bir suçlama değil, bir ŞÜPHE/soru olarak ifade edilmiş; OpenAI 10 Eylül'de Buckmaster'ın Codex promptlarının sonucu etkilemiş olamayacağını açıkladı (kendi savunması).

**URL:** https://thenextweb.com/news/bubeck-navier-stokes-account-apology-altman (AS-OF 2026-09-21) · https://fortune.com/2026/09/08/openai-says-it-cracked-navier-stokes-math-grand-challenge-buckmaster-accusation-cheating-intimidation-tao-lament/ (AS-OF 2026-09-21) · https://the-decoder.com/openai-researcher-allegedly-pressured-mathematician-to-drop-anthropic-co-author-from-math-breakthrough-paper/ (AS-OF 2026-09-21)

**Sonuç: DARALDI.** "Tehdit" iddiası somut alıntılarla destekleniyor ama tek taraflı (Buckmaster'ın versiyonu); Bubeck bunu "iftira" diyerek reddediyor — yani bu bir o-dedi-bu-dedi anlaşmazlığı, kanıtlanmış olgu değil. "İzinsiz veri erişimi" kısmı Buckmaster tarafından SORU/ŞÜPHE olarak ifade edilmiş, kesin suçlama değil; OpenAI bunu reddetti. Doğru koşul: "...Buckmaster iddia etti (Bubeck reddediyor, tarafsız doğrulama yok); 'izinsiz erişim' kısmı Buckmaster'ın kendi ifadesinde bir soru/şüphe olarak geçiyor, kanıtlanmış olgu olarak değil."

---

## A9 — Fefferman, sonucun çözüldüğüne sevindi ama kahramanlar Córdoba ve Martínez-Zoroa dedi

**Çürütme girişimi:** Tam alıntı arandı, "sevindi" kelimesinin abartı olup olmadığı kontrol edildi.

**Bulunan kanıt:**
- Quanta Magazine (WebFetch + WebSearch çapraz doğrulama): "I was thrilled that the problem was solved," said Charles Fefferman of Princeton University, who wrote the Clay Institute's official description of the Navier-Stokes problem. "The heroes of the story, he said, are Córdoba and Martínez-Zoroa."
- CUNEF Universidad haberi ve Infobae: Córdoba (Fefferman'ın doktora öğrencisi) ve Martínez-Zoroa'nın 2023 makalesinin fikri temel olarak tanındığı bağımsız kaynaklarla teyit edildi.

**URL:** https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/ (AS-OF 2026-09-21) · https://www.cunef.edu/en/luis-martinez-zoroa-investigador-de-cunef-universidad-es-reconocido-como-referente-internacional-en-los-avances-sobre-el-problema-de-navier-stokes/ (AS-OF 2026-09-21, WebSearch üzerinden görüldü)

**Sonuç: ÇÜRÜTÜLEMEDİ.** "Thrilled" (sevindi) ve "heroes are Córdoba and Martínez-Zoroa" ifadeleri birebir teyit edildi, birden fazla bağımsız kaynak (Quanta, İspanyolca basın) çapraz doğruluyor.

---

## A10 — Tao, matematik problemlerinin AI şirketlerince pazarlama için "strip-mine" edilmesinden endişeli

**Çürütme girişimi:** "Strip-mine" kelimesinin gerçekten Tao'ya ait olup olmadığı, bağlamın "pazarlama" ile ilgili olup olmadığı kontrol edildi.

**Bulunan kanıt:**
- WebSearch sentezi (IBM, PANews, teorth.github.io "Terence Tao on AI — a living summary", VnExpress): "The Navier-Stokes regularity problem is just the latest in a string of problems that have been 'strip-mined' for solutions by AI" — Tao'ya doğrudan atfedilen ifade.
- Ek bağlam: "The AI industry is convinced that conquering the subject's 'objective' truth is how companies will persuade investors that they're on the path to superintelligence" — pazarlama/yatırımcı bağlamı teyit edildi.
- Yirmi beş Fields Madalyalı (Tao dahil) ortak bildirge imzaladığı bilgisi de bulundu — bu, A10'un tek kişilik bir görüş olmadığını, daha geniş bir kaygının parçası olduğunu gösteriyor.

**URL:** https://teorth.github.io/tao-web/ai-views.html (AS-OF 2026-09-21) · https://panews.io/articles/01a083c5-6d5a-7384-be70-d9eee539859c (AS-OF 2026-09-21, WebSearch üzerinden görüldü, doğrudan fetch edilmedi) · https://www.ibm.com/think/news/will-ai-solve-math-too-fast-navier-stokes-terence-tao (AS-OF 2026-09-21, WebSearch üzerinden görüldü)

**Sonuç: ÇÜRÜTÜLEMEDİ.** "Strip-mine" ifadesi ve pazarlama/yatırımcı bağlamı birden çok bağımsız kaynakla (IBM, PANews, Tao'nun kendi web sayfası özeti) çapraz doğrulandı.

---

## EK-SORU — "AI Navier-Stokes'u çözdü" cümlesinin en güçlü savunması nedir?

**Sorgulanan üç alt-soru ve bulgular:**

1. **Millennium Prize sorusu gerçekten çözüldü mü?** Hayır, resmî olarak değil. CMI'nin ana problem sayfası 21 Eylül 2026 itibarıyla hâlâ "Active" (claymath.org/millennium-problems/navier-stokes-equation/, WebFetch ile doğrudan doğrulandı); ödül verilmedi; "sorunu tam olarak çözen kişi/kişiler duyuruda adlandırılmamış" (CMI'nin kendi duyurusu, 11 Eylül 2026).
2. **OpenAI'nin sonucu zorlamasız (unforced) Navier-Stokes'u kapsıyor mu?** Hayır. Birden çok kaynak (kingy.ai, xenospectrum.com) OpenAI'nin sonucunun Clay'in **C ve D** (zorlamalı/forced) seçeneklerini kapsadığını, asıl "zor" ve popülerin kastettiği **A ve B** (zorlamasız/unforced existence-smoothness) seçeneklerine DOKUNULMADIĞINI teyit ediyor.
3. **Clay ödül süreci başladı mı?** Kısmen. CMI resmi bir "duyuru" yayınladı ve "değerlendirme süreci"nin başladığını söylüyor, ama bunu kasıtlı olarak yavaş yürüteceğini vurguluyor; OpenAI kendisi ödülü talep etmeyeceğini açıkladı (WebSearch sentezi, openai.com doğrudan fetch edilemedi — 403).

**En güçlü savunma:** İddia yalnızca DAR/TEKNİK bir okumada savunulabilir: OpenAI'nin sonucu, Clay'in kendi resmi problem tanımındaki dört alternatiften (A/B/C/D) ikisini (C ve D — zorlamalı patlama örneği) matematiksel olarak tam karşılıyor gibi görünüyor ve bunu yazan otorite (Fefferman) "thrilled" tepkisi verdi, CMI de "apparently settled" dedi — bunlar gerçek, doğrulanmış otorite kabulleri. Ancak GENİŞ/POPÜLER okumada ("Navier-Stokes'un pürüzsüz çözümlerinin sonsuza dek var olup olmadığı" sorusu, yani A/B) iddia savunulamaz: bu kısım hâlâ dokunulmamış, CMI resmi statüsü hâlâ "Active", ödül verilmemiş, bağımsız hakemli inceleme tamamlanmamış. Yani en güçlü savunma "kısmi/teknik zafer, popüler soru değil" çerçevesidir — tam "çözüldü" iddiası popüler anlamda savunulamaz.

---

## Açılan Kaynaklar (WebFetch ile fiilen açılan)

1. https://www.claymath.org/news/navier-stokes-announcement/
2. https://terrytao.wordpress.com/2026/09/07/finite-time-blowup-with-smooth-forcing-term-for-the-incompressible-porous-medium-boussinesq-and-incompressible-euler-equations/ (2 kez, farklı sorgularla)
3. https://deepmind.google/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/
4. https://lilting.ch/en/articles/navier-stokes-openai-blowup-dispute
5. https://www.claymath.org/millennium-problems/navier-stokes-equation/
6. https://arxiv.org/abs/2509.14185
7. https://arxiv.org/pdf/2509.14185 (sonuç tutarsız/güvenilmez bulundu, reddedildi — bkz. A1)
8. https://kingy.ai/blog/navier-stokes-ai-proof-claims-dispute/
9. https://xenospectrum.com/en/openai-navier-stokes-singularity-clay-dispute/
10. https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/

Ayrıca birincil kaynak metni `curl` ile arXiv API'den (export.arxiv.org) çekildi — bu, WebFetch'in PDF-özetleme aracının verdiği çelişkili sonuçları çözmek için gerekliydi.

**Denemede başarısız / açılamayan:** https://openai.com/index/navier-stokes-solution/ — HTTP 403 Forbidden (WebFetch ile). Bu, A4/A5/EK-SORU için OpenAI'nin BİRİNCİL kaynağının doğrudan görülemediği, yalnız ikincil kaynaklar (haber siteleri) üzerinden yeniden inşa edildiği anlamına gelir — **önemli sınırlama**, rapor bu boşlukla ilerledi.

## Engeller

- OpenAI'nin resmi duyuru sayfası ve 166 sayfalık PDF'i doğrudan erişilemedi (403); tüm A4/A5/EK-SORU bulguları ikincil/üçüncül kaynaklardan (Fortune, kingy.ai, xenospectrum, Scientific American haberleri) yeniden inşa edildi — birincil kaynak eksikliği bir doğrulama sınırıdır.
- arXiv PDF'ini otomatik özetleyen araç (WebFetch) en az bir kez (2509.14185 için) ham metinle DOĞRUDAN ÇELİŞEN, muhtemelen halüsinasyonlu bir özet üretti ("CCF model / 1D active scalar" iddiası); bu, bu raporun "AI araçlarının otomatik PDF özetleri de çapraz doğrulama gerektirir" şeklinde bir metodolojik notudur.
- Tüm bulgular çekim tarihi (2026-09-21) itibarıyladır; olay hâlâ gelişmekte olan bir tartışma (Buckmaster-OpenAI-Bubeck anlaşmazlığı, CMI değerlendirme süreci) olduğundan gelecekte değişebilir.
