# Tech Stack — sözel önerme karşılığı

> Kaynak: `raporlar/2026-07-26-tech-stack-atlas.md` · Register: düz lojik · Compiler: **KAPALI**
> Okuma kuralı: **öncülü sağlanmayan bir önermenin sonucu geçerli DEĞİLDİR.**

**Numaralandırma:** kaynağın kendi kodları korunur — `M1`–`M19` (ölçülmüş), `F1`–`F18` (folklor), `R1`–`R41` (A23 ölçümleri), `L7`–`L15` (müfredat), `B1`–`B9` (borçlar), `V64`–`V67` (kutu).

**Kanıt sütunu:** *kendi ölçümümüz* = bu makinede/ham veriden hesaplandı · *birincil* = birincil kaynağa inildi · *ikincil* = abstract katmanından, birincil metinden doğrulanmadı · *çelişkili* = hüküm yok · *çıkarım* = bileşim, ölçüm değil · *aranamadı* = erişim/bütçe engeli, **yokluk kanıtı DEĞİL** · *arandı, yok* = **yokluk bulgusudur**.

**Antitez sütunu:** bu ailenin antitezi **araçsız** koştu (`tool_uses = 0`) ⇒ **mantıksal** saldırılar tam güçtedir; **olgusal karşı örnekler hatırlama düzeyindedir** ve borç açar, hüküm değiştirmez. *"Sağ çıktı"* damgaları **aynı-aile şerhlidir**: antitez ajanları tez ajanlarıyla aynı model ailesindendi.

---

## 0. Erişim rejimi ve dürüstlük kapısı

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§0.1** | Şu kanallar erişime kapalıydı: ScienceDirect, SpringerLink, SAGE, Wiley, ACM DL, IEEE Xplore, Cambridge Core, JSTOR, Royal Society, PubMed tam metin, tüm `*.edu` ve `*.github.io` adresleri, **tüm PDF'ler** (arXiv PDF dahil), `arxiv.org`, `github.com` HTML, `api.crossref.org`, `semanticscholar.org`.<br>Açık olanlar: `raw.githubusercontent.com`, `pypi.org`, `registry.npmjs.org`.<br>⚠️ `github.com`'un açık olduğu **görev brifinginde söylenmişti ve yanlıştı**; ajan ölçüp düzeltti. | ölçüm | — |
| **§0.2** | Sonuç: akademik bulguların **tamamı ikincil kaynaktır** — arama motoru abstract katmanından, birincil metinden değil.<br>Ondalıklar **teyit edilmemiş sayılmalıdır**; **yön** güvenilirdir. | çıkarım | — |
| **§0.3** | Bu ailede bir istisna vardır: kapalı yayıncıların **etrafından dolaşılıp kendi ölçümü üretildi**. PyPI, npm ve replikasyon CSV'leri üzerinden **dört bağımsız birincil ölçüm** yapıldı.<br>Bu, oturumdaki tüm ailelerin **en güçlü birincil veri tabanıdır**. | kendi ölçümümüz | — |

---

## 1. Ailenin tek cümlelik bulgusu

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§1.1** | Teknoloji seçimi hakkında **ölçülmüş** olan şey neredeyse tümüyle **ekosistem sağlığıdır** — terk oranı, bakımcı yoğunlaşması, bağımlılık gecikmesi, yıldız sahteciliği. Yani **seçtiğin şeyin hayatta kalıp kalmayacağı**.<br>**Ölçülmemiş** olan ise neredeyse tümüyle **karar verme yöntemidir** — innovation token, Technology Radar, ATAM, ADR, "boring technology". Yani **nasıl seçmen gerektiği**.<br>Pratikte dolaşan kuralların **hiçbirinin sonucu ölçülmemiştir**.<br>Herkesin baktığı sinyal (**yıldız**) ölçülmüş şekilde **bozuktur**; kimsenin öncelikli bakmadığı sinyal (**indirme / bağımlı sayısı**) ölçülmüş şekilde **güçlüdür**.<br>Bu asimetri, raporun tüm tasarım önerilerinin dayanağıdır. | çıkarım | çürütülemedi |

---

## 2. A22 — kendi ölçtüğümüz veri

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§2.1** | PyPI'nın tam paket indeksi çekildi (**857.893 proje**), seed'li rastgele 500 paket örneklendi, **478'i geçerli** çıktı.<br>Son sürümü 1 yıldan eski olanlar **%69,0**; 2 yıldan eski **%54,2** (±4,5 puan); 3 yıldan eski %43,9; 5 yıldan eski %26,6.<br>Medyan *"son sürümden beri geçen süre"* **856 gündür (2,3 yıl)**.<br>Sadece 1 sürümü olanlar %30,8; hem 1 sürümlü hem 2 yıldan durgun olanlar (*"ölü doğmuş"*) **%17,4**.<br>Sonuç: rastgele bir PyPI paketi **medyan olarak 2,3 yıldır terk edilmiştir** ⇒ *"PyPI'da paket var"* bilgisi tek başına **neredeyse sıfır bilgi taşır**. | kendi ölçümümüz | çürütülemedi |
| **§2.2** | Dört indirme katmanı × 500 paket ölçüldü.<br>İlk 500'de: 1 yıldan durgun %17,6, **2 yıldan durgun %8,6**, 3 yıldan %4,4; medyan 63 gün; medyan sürüm sayısı 59,5.<br>2.000–2.500 bandında: %28,4 / %15,2 / %10,6; medyan 128 gün.<br>7.000–7.500 bandında: %44,4 / %31,4 / %23,4; medyan 262 gün.<br>14.500–15.000 bandında: %43,2 / %35,2 / %26,4; medyan 237 gün.<br>Rastgele örneklemde: %69,0 / **%54,2** / %43,9; medyan 856 gün.<br>Sonuç: gradyan **monotonik ve çok güçlüdür**; en üst 500'de terk oranı rastgele pakete göre **6,3 kat** düşüktür. | kendi ölçümümüz | daraltıldı → K4 (bkz. §3.4-4) |
| **§2.3** | npm registry'den 374 sorguyla **220.469 paket** toplandı ve bağımlı sayısına göre katmanlandı.<br>En çok bağımlısı olan 100'de tek bakımcı **%29,0**; 2 yıldan durgun %16,0.<br>En çok bağımlısı olan 1.000'de tek bakımcı **%41,3**; 2 yıldan durgun **%35,8**.<br>En çok bağımlısı olan 10.000'de tek bakımcı %49,9; 2 yıldan durgun %46,2.<br>Toplanan 220 binin tamamında tek bakımcı **%77,7**.<br>En çok bağımlısı olan 1.000 paketin **%17,8'i hem tek bakımcılı hem 2 yıldan durgundur**.<br>Somut: `lodash` 197.330 bağımlı ve 1 bakımcı; `axios` 178.615 ve 1; `chalk` 158.494 ve 1; `colors` 22.079 ve 1, son yayın 2019-09.<br>⚠️ **Ajanın kendi dürüstlük notu, aynen taşınır:** npm'in `maintainers` alanı **yayın hesabı** sayar, insan sayısı değil. `@types/node`'un tek bakımcısı aslında bir bot hesabıdır; org sahipli paketlerde ekip üyeleri görünmez.<br>Sonuç: bu sayı bus factor'ı **ölçmez**; **yayın yetkisi yoğunlaşmasını** ölçer ⇒ tedarik zinciri riski için doğru metriktir, *"kaç kişi bu kodu biliyor"* için **değildir**. | kendi ölçümümüz | çürütülemedi |
| **§2.4** | Yıldız manipülasyonu replikasyon verisinden hesaplandı.<br>Düşük aktivite sezgiseli **4.904 depo / 1.031.443 şüpheli yıldız**; lockstep sezgiseli **8.894 depo / 2.157.864 şüpheli yıldız**; birleşim **13.508 depo**.<br>Lockstep'le işaretlenen depoların **%89,5'inde** yıldızların en az yarısı sahte; **%81,4'ünde en az %90'ı sahte**.<br>Düşük aktivite ile işaretlenenlerin **3.672'sinin toplam en az 1.000 yıldızı vardır** ⇒ bunlar küçük spam depoları değil, **"başarılı görünen" projelerdir**.<br>Somut: `HKUDS/LightRAG` 10.956 yıldızın **7.596'sı (%69)** şüpheli; `yangchris11/samurai` 5.746'nın **5.365'i (%93)**; `ComposioHQ/composio` 15.088'in 6.759'u (%45).<br>Yayımlanmış hâli: 2019-07 ile 2024-12 arası **yaklaşık 6 milyon şüpheli sahte yıldız / 15.835 depo**; kampanyalar 2024'te **iki büyüklük mertebesi** büyüdü; **2024 Temmuz zirvesinde yıldız aktivitesi olan tüm depoların %16'sı** bir kampanyayla ilişkiliydi.<br>Sonuç: bir AI/LLM deposunun yıldızının üçte ikisinin satın alınmış olabilmesi, **yıldızı seçim kriteri olarak kullanılamaz kılar**.<br>*Not: makalenin ilk sürümü "4,5 milyon", yayımlanan sürümü "6 milyon" der — çelişki değil, **sürüm farkıdır**.* | kendi ölçümümüz ∧ ikincil | çürütülemedi |

---

## 3. A22 — ölçülmüş ile folklor

### 3.1 Ölçülmüş

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **M1** | Rastgele bir PyPI paketi terk edilmiştir: %54,2'si 2 yıldan durgun, medyan 856 gün. | kendi ölçümümüz (n=478) | çürütülemedi |
| **M2** | İndirme popülerliği bakım aktifliğini öngörür: ilk 500'de %8,6, rastgelede %54,2; ilişki monotoniktir. | kendi ölçümümüz (4×500) | daraltıldı → K4 |
| **M3** | Kritik npm paketlerinde yayın yetkisi tek hesapta toplanmıştır: ilk 1.000'in %41,3'ü tek bakımcılı. | kendi ölçümümüz (220k) | çürütülemedi |
| **M4** | Kritik paketlerin bir kısmı hem tek bakımcılı hem durgundur: ilk 1.000'in %17,8'i. | kendi ölçümümüz | çürütülemedi |
| **M5** | Az sayıda hesap tüm ekosisteme erişir: 100'den az bakımcı npm'in %50'sine ulaşır. | ikincil | çürütülemedi |
| **M6** | Bus factor tipik olarak çok düşüktür: projelerin %65'inde en fazla 2, %46'sında tam 1. | ikincil | çürütülemedi |
| **M7** | Yaygın paketler de terk edilir ve kullanıcı tepki vermez: yaklaşık %15'i 6 yılda terk edilir; **çoğu alt proje terk edilmiş bağımlılığı hiç değiştirmez**. | ikincil | çürütülemedi *(K4'ün mekanizmasını destekler)* |
| **M8** | Deprecated bağımlılık kullanımı yaygındır: istemcilerin %27'si doğrudan, %54'ü geçişli olarak kullanır. | ikincil | çürütülemedi |
| **M9** | Bağımlılık gecikmesi nicelleştirilebilir: medyan 106 gün (0 major, 1 minor, 2 patch geride). | ikincil | çürütülemedi |
| **M10** | GitHub yıldızı endüstriyel ölçekte sahte üretilebilir: yaklaşık 6 milyon şüpheli yıldız / 15.835 depo; zirvede %16. | kendi ölçümümüz ∧ ikincil | çürütülemedi |
| **M11** | İşaretlenen depoların çoğunda yıldızın çoğu sahtedir: %81,4'ünde en az %90'ı. | kendi ölçümümüz | çürütülemedi |
| **M12** | Yıldız kod kalitesini göstermez: anlamlı korelasyon yoktur; sürücüler tanıtım ve trenddir. | ikincil | çürütülemedi |
| **M13** | Dil seçiminin hataya etkisi ya yoktur ya çok küçüktür: 11 dilden yalnız 4'ü anlamlı, etki *"son derece küçük"*. | ikincil | çürütülemedi |
| **M14** | Dil çeşitliliği hata eğilimini artırır: 628 proje / 17 dil, pozitif ilişki. ⚠️ M13'ün metodolojik uyarısı buna da uygulanır — aynı veri kaynağı ailesi, aynı sınıf regresyon. | ikincil | çürütülemedi |
| **M15** | Mimari borç kod borcundan hızlı faiz biriktirir: 3–5 kat; borcun %44,2'si pozitif faizlidir. | ikincil | çürütülemedi |
| **M16** | Gevşek bağlı mimari teslim başarımını öngörür (çok yıllı modelleme). | ikincil | çürütülemedi |
| **M17** | Kütüphane göçü kaliteyi genelde iyileştirir: 57.447 proje; bağlaşım düşer, uyum artar. | ikincil | çürütülemedi |
| **M18** | ADR pratiği pilot sonrası terk edilir: 921 deponun yaklaşık **%50'sinde 5'ten az kayıt** vardır. | ikincil | çürütülemedi |
| **M19** | Fikirlerin çoğu hedeflediği metriği iyileştirmez: yaklaşık üçte biri pozitif; başarısızlık %70–90. | ikincil | çürütülemedi |

### 3.2 Folklor — ölçümü yok, ama ölçülmüş gibi dolaşıyor

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **F1** | *"Her şirketin yaklaşık 3 innovation token'ı vardır"* — **tamamen ölçülmemiştir**. Sayı retoriktir; kalibrasyonu yoktur. | arandı, yok | çürütülemedi *(bkz. §3.4-1 notu)* |
| **F2** | *"Boring technology seç, daha iyi sonuç alırsın"* — **ölçülmemiştir**. Sonuç değişkeni hiç tanımlanmamıştır ve *"boring"* tanımı post-hoc ayarlanabildiği için tez **yanlışlanabilir değildir**. | arandı, yok | çürütülemedi |
| **F3** | *"Yeni teknoloji yüksek operasyonel yük getirir"* — ölçülmemiş stereotiptir; karşı tez de ölçülmemiştir. | arandı, yok | — |
| **F4** | Technology Radar halkalarının isabetli olduğu — **öngörü doğruluğu hiç yayımlanmamıştır**; retrospektif yoktur. | arandı, yok | — |
| **F5** | ATAM'ın mimari kararları iyileştirdiği — **kontrollü çalışma yoktur**; yalnız uygulama vakaları vardır. | arandı, yok | — |
| **F6** | ISO/IEC 25010'un kalite öngördüğü — bu bir taksonomidir; alt karakteristikten metriğe eşleme **standartta yoktur**. | birincil | — |
| **F7** | ADR'nin *"daha iyi karar"* sağladığı — **ölçüm yoktur**. Ölçülenler yalnız benimseme ve anlaşılırlıktır. | arandı, yok | — |
| **F8** | *"Lock-in pahalıdır"* — varsayılmıştır. Alanın kendi itirafı: çok az kurum switching cost ölçer. | arandı, yok | — |
| **F9** | *"CNCF 2025: %42'si monolite dönüyor"* — **birincil kaynakta doğrulanamadı**; yalnız içerik çiftliği sitelerinde. ⇒ **KULLANILMAYACAK.** | doğrulanamadı | — |
| **F10** | *"Gartner 2025: %60'ı mikroservisten pişman"* — doğrulanamadı; tek kaynak bir blog yazısı. | doğrulanamadı | — |
| **F11** | *"Mikroservis göçlerinin %73'ü başarısız"* — doğrulanamadı. | doğrulanamadı | — |
| **F12** | *"O'Reilly 2025: %62'si ilk 12 ayda ROI sorunu yaşıyor"* — doğrulanamadı. | doğrulanamadı | — |
| **F13** | *"Teknik borç: %23 hız düşüşü, %31 defect artışı, %287 ROI, 4,7 ay başabaş"* — doğrulanamadı; içerik çiftliği izlenimi. ⇒ **KULLANILMAYACAK.** | doğrulanamadı | — |
| **F14** | *"Büyük yeniden yazımların şu kadarı başarısız"* — **sağlam rakam yoktur**. Kaynakların itirafı: *"rakam yayımlayan taraf bir şey satıyor."* | arandı, yok | — |
| **F15** | *"COBOL göçlerinin %67'si başarısız"* — doğrulanamadı. | doğrulanamadı | — |
| **F16** | YAGNI'nin maliyet modeli — muhakemedir; *"%30-50'si hiç kullanılmaz"* bir danışmanlık öz beyanıdır. | ikincil | — |
| **F17** | *"Rakip/alternatif sayısına bak"* heuristiği — **hiçbir ölçüm yoktur**; bu kriter üzerine literatür bulunamadı. | arandı, yok | — |
| **F18** | *"Küçük takım monolit kullanmalı"* — ölçülmemiştir; mevcut tek kohort çalışması **ters yönde** sonuç verir. | ikincil | — |

### 3.3 Hakem müdahaleleri

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§3.3-1** | **Alanın amiral gemisi kanıtı çöktü.** 729 GitHub projesi üzerinde 11 dil ile hata yoğunluğu arasında anlamlı ilişki bulan çalışma, bağımsız yeniden analizde **yalnızca kısmen** tekrarlanabildi (eksik kod, dil sınıflandırma hataları); **çoklu hipotez düzeltmesi sonrası yalnız 4 dil anlamlı kaldı ve etki büyüklüğü *"son derece küçük"* oldu**.<br>Orijinal yazarlar çürütme, yeniden analiz ekibi karşı çürütme yayımladı ⇒ **tartışma kapanmadı, hüküm yoktur**.<br>Sonuç: *"Hangi teknolojiyi seçtiğin ölçülebilir şekilde kaliteyi etkiler"* iddiasının **en çok atıf alan kanıtı yeniden analizde büyük ölçüde buharlaştı**. Bu, ailenin **en önemli tek bulgusudur**. | çelişkili | çürütülemedi |
| **§3.3-2** | ***"Boring technology"* yanlışlanabilir değildir.** Tezin **kendi savunucularından** gelen itiraf — *"boring bir liste değil kültür meselesidir; neyin sıkıcı sayıldığı ekibin beceri setine göre değişir"* — tezi **test edilemez** kılar: tanım sonuca göre ayarlanabiliyorsa hipotez değildir.<br>⚠️ Bu, F2'nin folklor sayılmasının gerekçesidir — ve gerekçe *"kanıt bulunamadı"* **değildir**. Epistemolojik olarak kritik bir ayrımdır. | birincil (savunucu beyanı) | çürütülemedi |
| **§3.3-3** | **Ölçek folkloru ters yönde ölçülmüştür.** Registered report kohort çalışması: baştan mikroservis kullanan projeler ile benzer monolitik projeler karşılaştırıldı; sonuç **mikroservislerin geliştirme hızını iyileştirdiğini doğruladı**.<br>⚠️ Kohort açık kaynak projelerdir; **tek kişilik kişisel sisteme genellenmesi şüphelidir** — ama F18 folklorunun ölçümle *desteklenmediğini* göstermeye yeter.<br>Ters yönde de kayıt vardır: hakemli literatürde mikroservisten monolite dönen **dört** belgelenmiş vaka (Istio kontrol düzlemi, Amazon Prime Video izleme servisi, Segment, InVision) ve **dördünde de gerekçe maliyettir**.<br>Sonuç: **iki yön de ölçülmüştür, ikisi de zayıftır** ⇒ bu eksende karar verecek kanıt yoktur. | ikincil ∧ çelişkili | çürütülemedi |

### 3.4 A22 iddia listesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§3.4-1** | *"Choose boring technology"* ve innovation token **ölçülmemiş pratisyen tezleridir**; *"boring"* tanımı post-hoc ayarlanabildiği için tez **yanlışlanabilir değildir**. | çıkarım | çürütülemedi *(antitezin "bu sezgisel bir bütçeleme kuralıydı, yanlışlanabilirlik standardı uygulanamaz" itirazı **reddedildi**: standart tezin kendisine değil, **karar gerekçesi olarak kullanılışına** uygulandı)* |
| **§3.4-2** | Teknoloji seçim çerçevelerinin (ADR, Technology Radar, ATAM, ISO 25010) **hiçbirinin kendi faydası ölçülmemiştir**; ölçülen tek şey benimseme oranlarıdır. | arandı, yok | çürütülemedi |
| **§3.4-3** | GitHub yıldızı seçim kriteri olarak kullanılamaz: endüstriyel ölçekte sahte üretilir ve kod kalitesiyle korelasyonu yoktur. | kendi ölçümümüz ∧ ikincil | çürütülemedi |
| **§3.4-4** | İndirme ve bağımlı sayısı, yıldızın aksine, bakım aktifliğini **toplu düzeyde** güçlü ve monotonik biçimde öngörür — **paket başına garanti değildir**.<br>⚠️ Ölçümümüz bir **katman agregasıdır**; bu bir **dağılım** iddiasıdır. Karşı örnekler: `moment.js` bakım moduna geçtiği hâlde indirmeleri devasa kaldı; `request` deprecated ilan edildikten sonra yıllarca yüksek kaldı ⇒ **ekosistem ataleti**.<br>Bu karşı örnekler **doğrulanmadı** (hatırlama düzeyinde), ama mekanizma kendi M7 bulgumuzla uyumlu olduğu için **kabul edildi**. Agregayı **çürütmezler**; *"paket başına öngörü"* okumasını **yasaklarlar**. | kendi ölçümümüz | daraltıldı → K4 |
| **§3.4-5** | Rastgele bir açık kaynak paketi terk edilmiştir; **terk edilmemişlik istisnadır, kural değildir**. | kendi ölçümümüz | çürütülemedi |
| **§3.4-6** | Yaygın kullanılan paketlerin büyük kısmında yayın yetkisi tek hesapta yoğunlaşmıştır; bu, ölçek büyüdükçe azalmaz, **yalnız en tepede** azalır. | kendi ölçümümüz | çürütülemedi |
| **§3.4-7** | Teknoloji seçiminin sonuca etkisine dair **en çok atıf alan ampirik kanıt, bağımsız yeniden analizde büyük ölçüde geçersizleşmiştir**. | çelişkili | çürütülemedi |
| **§3.4-8** | Ölçek bağımlı folklorun (mikroservis/monolit) ölçülmüş hâli, folklorun **tersi yönde** sonuç verir — dayanak **kohort çalışmasıdır**, tek bir vaka değil.<br>⚠️ Antitez *"Prime Video tek vakadır, ölçülmüş statüsüne yükseltilemez"* dedi; **kısmen kabul edildi**: dayanağımız o vaka değildi, ama **iddia metni bunu belirtmiyordu** ⇒ dayanak artık iddianın içinde yazılıdır. | ikincil | daraltıldı → K8 |
| **§3.4-9** | Teknoloji seçimi tartışmasında dolaşan yüzde rakamlarının kayda değer bir kısmı, birincil kaynakta doğrulanamayan **içerik çiftliği kökenli uydurmalardır**. | doğrulanamadı | çürütülemedi |

---

## 4. A22 — bulunamayanlar

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§4.1** | *"Innovation token"* kavramının **herhangi bir ampirik operasyonelleştirmesi yoktur** — ne token sayısını kalibre eden ne token harcamasıyla sonucu ilişkilendiren tek bir çalışma. Tez 2015'ten beri dolaşıyor ve **11 yılda hiç test edilmemiştir**. | arandı, yok | — |
| **§4.2** | *"Boring technology seçen projeler daha iyi sonuç verdi mi"* sorusunu soran **hiçbir çalışma yoktur**. Teknoloji yaşı/olgunluğu ile proje sonucu ilişkisini **yazılım bağlamında** ölçen çalışma yoktur; bulunanlar inşaat, ulaştırma ve patent alanındadır ve **transfer etmez**. | arandı, yok | — |
| **§4.3** | Technology Radar'ın **retrospektif isabeti** ölçülmemiştir: *"Adopt'a alınan blip'ler 5 yıl sonra ne oldu"* analizi ne üreticide ne üçüncü tarafta vardır. | arandı, yok | — |
| **§4.4** | ATAM'ın **kontrollü değerlendirmesi yoktur**: uygulayan ile uygulamayan proje karşılaştırması yapılmamıştır. | arandı, yok | — |
| **§4.5** | ADR'lerde **gözlenmiş sonuç alanı yoktur** — ne 13 şablonda, ne literatürde *"kararlar sonradan doğru çıktı mı"* ölçülmüştür.<br>⇒ Bu boşluk **hem pratikte hem akademide açıktır** ve **özgün katkı alanıdır**. | arandı, yok | — |
| **§4.6** | *"Rakip/alternatif sayısı"* kriterinin ölçümü yoktur; bu heuristiği inceleyen **hiçbir çalışma** bulunamadı. | arandı, yok | — |
| **§4.7** | Lock-in'in **nicel bedeli** ölçülmemiştir: switching cost'u *fiilen* ölçen (tahmin ya da anket değil) çalışma yoktur. | arandı, yok | — |
| **§4.8** | Rewrite başarısızlık oranının **güvenilir tahmini yoktur**; yalnız vaka anekdotları ve taraflı sektör rakamları vardır. | arandı, yok | — |
| **§4.9** | **Tek kişilik ölçekte teknoloji seçimi ölçülmemiştir.** Tüm ampirik literatür ya ekosistem ölçeğinde ya kurumsal takım ölçeğindedir; solo geliştirici ya da kişisel sistem bağlamına doğrudan konuşan **hiçbir ölçüm yoktur**.<br>⇒ Bu, **ailedeki en büyük kanıt boşluğudur ve Salih'in tam olarak bulunduğu yerdir**. | arandı, yok | — |

---

## 5. A24 — karar vermeyi öğrenme

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§5.1-1** | Sezgisel uzmanlık **iki koşul birlikte** sağlanınca güvenilirdir: ortam geçerli ipuçları barındıracak kadar **düzenli** olmalı, ve uzman bu düzenlilikleri **hızlı ve belirsizlik içermeyen geri bildirimle** uzun süre öğrenmiş olmalı.<br>Biri düşerse *"kendinden emin sezgi **sistematik hataya** döner."*<br>Yüksek geçerlilikli ortam **gerek şarttır, yeter şart değildir**. | ikincil | çürütülemedi |
| **§5.1-2** | *"Kind"* ve *"wicked"* öğrenme ortamları ayrılır. Wicked ortam, sonuçların eylemlerle korelasyonunun belirsiz, aldatıcı ya da yok olduğu; geri bildirimin eksik ya da yanıltıcı olduğu ortamdır.<br>Öneri: kişi hangi ortamda pasif öğrendiğini **seçerek** sezgisini eğitebilir. | ikincil | çürütülemedi |
| **§5.1-3** | Mimari kararların bu ölçütü karşılayıp karşılamadığını **doğrudan ölçen çalışma bulunamadı**.<br>Dolaylı kanıtlar ortamı **kötü** tarafa koyar: mimari teknik borç **gecikmeli** tezahür eder (*"büyük ve uzun ömürlü sistemler bundan muzdarip; küçük ve kısa ömürlüler sorun olmadan ölüyor"*) ⇒ karar ile sonucun görünmesi arasındaki gecikme **sistem ömrü mertebesindedir**.<br>Geri bildirim geldiğinde bile kirlidir: **sonuç yanlılığı** 2023 replikasyonunda **orijinalden güçlü** çıkmıştır — orijinal d = .21–.53 iken replikasyon **d = .77 [.62, .93] → 1.1 [.94, 1.26]** — ve katılımcılar *"sonuca bakmamalıyım"* **dedikleri hâlde**.<br>⚠️ **Ajanın çizdiği sınır korunur:** *"mimari kötü öğrenme ortamıdır"* hükmü **bir bileşimdir, literatür bulgusu değildir**. Kahneman-Klein ölçütünü yazılım mühendisliğine formel uygulayan tek şey blog düzeyinde yorumdur.<br>⇒ **Bu raporun en çok yaslandığı önerme, aynı zamanda en az doğrudan desteklenen önermesidir.** | çıkarım | çürütülemedi |
| **§5.1-4** | Geri bildirim zayıfsa **deneyim uzmanlık üretmez**: 62 değerlendirmenin **32'si (%52)** hekimde yıl arttıkça performansın **düştüğünü**, 13'ü (%21) ilişkisizlik bildirdi; yalnız **1'i (%2)** tüm çıktılarda artış buldu.<br>Yazılıma özgü paralel: mesleki yıl programcı performansını **kötü yordar**; *"sanayide kazanılan deneyimin kalite ve üretkenlik üzerinde hiçbir etkisi görünmüyor, akademide kazanılanın olumlu etkisi var."* Öz değerlendirme de genel olarak performansla korele değildir. | ikincil | çürütülemedi |
| **§5.2-1** | Kasıtlı pratik varyansın **oyunlarda %26, müzikte %21, sporda %18, eğitimde %4, mesleklerde %1'den azını** açıklar.<br>**Meslekler — yazılımın ait olduğu kategori — en düşük dilimdir.**<br>*Not: görev emrindeki "%21 oyun / %18 müzik" rakamları kaymıştı; ajan düzeltti.* | ikincil | çürütülemedi |
| **§5.2-2** | Kasıtlı pratik teorisinin temel çalışmasının **çift kör replikasyonu çekirdek bulguyu tekrarlamadı**; etki büyüklüğü belirgin biçimde küçüktü. *"Öğretmen tasarımlı pratik"* yalnız pratikten **daha fazla varyans açıklamadı** ⇒ teorik tanım, operasyonel tanımdan iyi çalışmadı.<br>Karşı yanıt yayımlandı ⇒ **tartışma kapanmadı**. | çelişkili | çürütülemedi |
| **§5.2-3** | Yazılım mühendisliğine özgü, kasıtlı pratiğin performans varyansındaki payını ölçen çalışma **bulunamadı**. | arandı, yok | — |
| **§5.3-1** | **Vaka sayısı:** kaynak analog yokken çözüm oranı yaklaşık **%10**; **tek** analogla yaklaşık **%30**; ipucuyla yaklaşık **%80**. Şema tümevarımı **iki vakanın karşılaştırılmasıyla** oluşur.<br>Sonuç: tek vaka okumak transferi **düşük bırakır — sıfır değil** (yaklaşık %30, yani analogsuz hâlin üç katı).<br>⚠️ Eski hâli *"neredeyse transfer üretmiyor"* diyordu ve **satırın kendi rakamıyla çelişiyordu**. | ikincil | çürütüldü → K1 |
| **§5.3-2** | **Tekrar ziyaret:** kötü yapılandırılmış alanlarda aynı materyalin **farklı zamanlarda, yeniden düzenlenmiş bağlamlarda, farklı amaçlarla** tekrar ziyareti şarttır. Tek geçişli müfredat **tanım gereği yetersizdir**. | ikincil | çürütülemedi |
| **§5.3-3** | **Başarısızlık başarıdan öğreticidir:** kuruluşlar başarısızlıktan başarıdan **daha fazla** öğrenir ve **başarısızlık bilgisi daha yavaş değer kaybeder** — *"başarıdan gelen bilgi uçucu, başarısızlıktan gelen yıllarca kalıyor."*<br>**Ama:** postmortem *"önerilen yöntem"* olmasına rağmen **tutarlı uygulanmıyor**; ankette az kişi memnun; **birden fazla postmortem'in çıktısını birlikte analiz eden neredeyse yok.** | ikincil | çürütülemedi |
| **§5.3-4** | **Öz açıklama işe yarar:** 64 rapor / 69 etki / 5.917 katılımcı, rastgele etkiler modelinde **g = 0,55**. Çok çeşitli koşulda çalışır. | ikincil | çürütülemedi |
| **§5.3-5** | **Yazılımda kalibrasyon tabanı düşüktür:** profesyonellerin **%90 güvenli** min-maks efor aralıkları gerçek eforu yalnız **%60-70** oranında içerir; projeler ortalama **%30-40 fazla** efor harcar. | ikincil | çürütülemedi |
| **§5.3-6** | **Ailenin en operasyonel bulgusu:** belirsizlik değerlendirmesinin iyileşmesi için **gerek koşul, açıkça formüle edilmiş bir strateji kullanılmasıdır**; **sezgi temelli** değerlendirme **hiç ya da çok az öğrenme** üretir.<br>Uzmanlar geçmiş dersleri nadiren kullanır; **kötü formüle edilmiş geçmiş tavsiye zararlı olabilir**.<br>⇒ Yapılandırılmış yansıtma tek başına yetmez; **yazılı, açık kural şarttır**. | ikincil | çürütülemedi |
| **§5.3-7** | **Kalibrasyon eğitimi işe yarar:** eğitim 3. yılda **%6**, 4. yılda **%7** skor iyileşmesi sağlar; aşırı güveni azaltarak kalibrasyonu ve çözünürlüğü iyileştirir ⇒ **gerçek ama mütevazı**.<br>Ayrıca %98 güven aralığı ıskalama oranı **tek pratik turundan sonra %41'den %23'e** iner. | ikincil | çürütülemedi |
| **§5.3-8** | **Ama koşulsuz değildir:** 70 istihbarat analistiyle yapılan ticari kalibrasyon kursunda iyileşme vardır **ama etki göreve bağlıdır**. Ayrı bir çalışma: *"Pratik skorlama kuralıyla kalibrasyon geri bildirimi güveni kalibre **etmiyor**."*<br>⇒ *"Tahmin + kayıt + skorlama otomatik işler"* iddiası **çelişkili kanıta sahiptir**. | çelişkili | çürütülemedi |
| **§5.3-9** | **Geri bildirim türü ayrışır:** performans geri bildirimi **aşırı güveni** azaltır; çevresel geri bildirim **ayırt ediciliği** iyileştirir. İkisi farklı şeyi düzeltir. | ikincil | çürütülemedi |
| **§5.3-10** | **Dış görüş:** 20 ülke, 5 kıta, 258 altyapı projesinin **%90'ı bütçe aşımına uğramıştır** (demiryolu ortalama %28, köprü-tünel %34, yol %20). Referans sınıfı tahmini 2005'te resmen tavsiye edilmiştir. | ikincil | çürütülemedi |
| **§5.3-11** | **Premortem:** olayın **gerçekleşmiş olduğunu varsaymak**, gelecekteki sonuçların nedenlerini doğru belirlemeyi **%30** artırır ve **eylem temelli** gerekçe sayısını **ikiye katlar**. | ikincil | çürütülemedi |
| **§5.3-12** | **Çapalama:** debiasing atölye deneyinde **12 takımın 10'unda** akıl yürütme iyileşti. Çapalama, mimarların **ilk buldukları çözümü bilinçsizce yeğlemesine** yol açar. | ikincil | çürütülemedi |
| **§5.3-13** | **Yetinmecilik:** tasarımcılar sezgisel ve rasyonel stratejileri **karışık ve sırayla** kullanır; çoğu denek **karar vermeden önce yalnız birkaç gerekçe** üretir. | ikincil | çürütülemedi |
| **§5.3-14** | **Uzman ile acemi farkı:** uzmanların çözüm geliştirmesi **sistematik ve dengelidir**; dengesiz gelişim **zihinsel simülasyonu imkânsız** kılar. Uzmanlığın işareti **enine öncelikliden fırsatçı moda geçebilme yeteneğidir** — yani uzmanlık tek sürece bağlılık değil, **süreç seçimidir**. Genel olarak uzmanlar **davranış ve işlev** düzeyinde, acemiler **yapısal ve yüzeysel** düzeyde çalışır. | ikincil | çürütülemedi |
| **§5.3-15** | **Ters yön — teşvik yapısı:** 591 profesyonelin **%60'ı** işe alanların trendlerden etkilendiğini kabul ediyor; **%82'si** trend teknoloji kullanmanın kendisini çekici kıldığına inanıyor.<br>**Ama %39'u** yerleşik teknolojide deneyimliyi yeğliyor, yalnız **%20'si** trend bileni; ve yalnız **%42'si** yeni teknolojinin kendisini daha iyi geliştirici yaptığına inanıyor.<br>⇒ **Teşvik yapısı ile fayda inancı ayrışıyor.** | ikincil | çürütülemedi |
| **§5.3-16** | **Kontrol bulgusu:** yerleşik pratikte seçim kriteri daha sağlıklıdır — geliştiriciler teknolojiyi **sistem gereksinimleri ve ekipte hâlihazırda var olan beceriler** temelinde seçer. | ikincil | çürütülemedi |
| **§5.3-17** | **Vaka temelli öğrenme etki büyüklükleri indirimli okunur.** Tıpta bu meta-analizler **şüpheli derecede büyük** etkiler bildiriyor (klinik akıl yürütme SMD = 1,78 [1,46, 2,11]). Bu meta-analizlerin çoğu **tek ülke ve tek eğitim kültürü** kaynaklıdır ve etkiler eğitim literatürü normlarının çok üstündedir ⇒ **yayın yanlılığı şüphesiyle indirimlidir**.<br>Aynı şekilde simülasyon çalışmalarının d değerleri (bilgi 1,20; süreç 1,09; hasta çıktısı 0,50) **"müdahale yok" karşılaştırmasına** dayanır — bu tasarım etkiyi **sistematik şişirir**; aktif kontrolle kıyas çok daha küçüktür. | çelişkili | çürütülemedi |
| **§5.3-18** | **Ters bulgu korunur:** problem temelli öğrenme meta-analizleri **çıktı türüne göre işaret değiştirir** — becerilerde sağlam pozitif, **bilgide anlamlı negatif**; ancak elde edilen bilginin **kalıcılığı daha yüksektir**. Uzun vadeli kalıcılık ve beceri ölçümünde üstün, **kısa vadeli bilgi ölçümünde geridedir**.<br>⇒ Bu, ana atlasın *"önce dene, sonra oku"* kararıyla **aynı yöne çıkar** — **ama aynı zamanda bir uyarıdır:** yanlış çıktı ölçülürse vaka temelli yöntem geleneksel yöntemden **geride** görünür. **DONE tanımının ölçtüğü şeyi yanlış seçmesi gerçek bir risktir.** | çelişkili | çürütülemedi |
| **§5.3-19** | **Hukuk vaka yöntemi varsayımı düşer:** *"Hukukta vaka/Sokratik yöntem kanıtlı bir modeldir"* varsayımı **desteklenmiyor**. Etkililik araştırması ağırlıkla işletme alanındadır; uygulayıcı avukatlar yöntemin pratiğe hazırlamada etkili olmadığı görüşündedir; yöntem son on yılda **gözden düşmüştür**.<br>⇒ Hukuk **muhakeme biçimi** olarak alınabilir, **öğretim modeli** olarak alınamaz. | ikincil | çürütülemedi |

### 5.4 A24 iddia listesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§5.4-1** | Yazılım mimarisi kararları **geçersiz** bir öğrenme ortamıdır; bu alanda deneyimden doğal sezgi gelişmez. | çıkarım | çürütülemedi *(§5.1-3'ün şerhi geçerli)* |
| **§5.4-2** | Mimaride yıl sayısı uzmanlık üretmez; geri bildirim mimarisi düzeltilmeden geçen yıllar performansı **düşürebilir**. | ikincil | çürütülemedi |
| **§5.4-3** | Kasıtlı pratik mesleki alanlarda varyansın %1'inden azını açıklar; **yazılım mimarisi için ölçülmüş bir tahmin yoktur**. | ikincil | sağ çıktı ⚠️ — antitezin ifadesiyle *"en sağlam, en spesifik, en doğrulanabilir iddia"* |
| **§5.4-4** | Vaka okumanın öğretici olması için **en az iki zıt vakanın** karşılaştırılması gerekir; tek vaka okuma transferi **düşük bırakır (~%30), sıfırlamaz**.<br>⚠️ Eski hâli *"tek vaka okuma transfer üretmez"* diyordu ⇒ **çürütüldü**, ve bu **bizim iç tutarsızlığımızdı**: §5.3-1 zaten *"tek analogla ~%30"* yazıyordu.<br>⇒ **İki vaka kuralı ayakta**; gerekçesi *"tek vaka işe yaramaz"* değil, **"şema ancak karşılaştırmayla doğar"**. | ikincil | ⛔ çürütüldü → K1 |
| **§5.4-5** | Başarısızlık vakaları başarı vakalarından daha öğretici ve daha kalıcıdır. | ikincil | çürütülemedi |
| **§5.4-6** | **(Sonuç görünür durumdayken) okumak öğretici değildir; (sonuç kapatılarak) okumak — tahmin et, aç, skorla — öğreticidir.** Sonucu bilinen bir kararı okumak, sonuç yanlılığı nedeniyle süreç değerlendirmesini sistematik bozar.<br>⚠️ **Bu cümle yeniden yazıldı.** Eski hâli *"sonuç kapatılmadan okuma öğretici değildir"* idi ve **antitez bunu tam tersine anladı**: *"sonuç açıklanmadan okuma öğretici değildir"* diye okuyup haklı olarak Harvard vaka yöntemini karşı örnek gösterdi — o yöntem sonucu **bilerek saklar**.<br>**İddia ayakta — ama bu bir zafer değil, bir arıza kaydıdır.** Yetkin bir okuyucu, önerme formunda yazılmış bir cümleyi ters anladı; sebep **olumsuzlamanın kapsamının Türkçe yüzeyde ayrışmamasıdır**.<br>⇒ **Türetilen kural (K10):** önerme formunda `¬` kullanılan her cümlede **kapsam parantezle sabitlenir**. | ikincil | yeniden yazıldı → K5 ⭐ |
| **§5.4-7** | Kalibrasyon skorlaması, **insan kolaylaştırıcı olmadan** nesnel performans verisi üretebilen **bulunabilen tek** pratik mekanizmadır.<br>⚠️ *"Tek"* burada **bulunabilen tek** demektir, **kanıtlanmış tek değil**.<br>⚠️ **Bu eğitimin mimari karar öğrenimine transferi ölçülmemiştir.**<br>Antitez bir **çifte standart** yakaladı ve kabul edildi: iddia 2 çerçevelerin etkinliğinin ölçülmediğini söyleyerek şüpheci bir standart uygularken, bu iddia **aynı titizlikte kanıt sunmadan ve daha güçlü bir kesinlikle** kuruluyordu.<br>Ve bunu **kendi raporumuz da söylüyordu** (A24 boşluk #4: *"Mimari kararlarda Brier skorlu tahmin eğitimi denenmemiş"*) — ama **iddia listesine taşınmamıştı**.<br>⇒ Bu, §7'deki **Model C önerisinin dayanağını zayıflatır**. Model C hâlâ önerilir, ama gerekçesi *"en iyi kanıtlı"* değil **"tek uygulanabilir"**tir. | ikincil (transfer: **kestirim**) | daraltıldı → K6 ⭐ |
| **§5.4-8** | Sezgi temelli yansıtma öğrenme üretmez; öğrenme için **açıkça yazılmış bir karar kuralı** gereklidir. | ikincil | çürütülemedi |
| **§5.4-9** | Teknoloji seçiminde en büyük sistematik hata kaynağı bilgi eksikliği değil, **teşvik yapısıdır** — özgeçmiş güdümlü seçim ve büyük ölçek çözümünün transplantı. | ikincil | çürütülemedi |

---

## 6. A23 — DS/ML asgari yığını

*Bu bölümün bulgularının **neredeyse tamamı bu makinede yapılmış kendi ölçümüdür**, literatür aktarımı değildir. Ajan dört alt hat açtı; **alt hatların metnini elinde doğrulayamadığı için aktarmadı ve uydurmadı** — konu alanlarını kendi ölçümüyle kapattı, literatür boşluklarını açıkça işaretledi.*

### 6.1 Paket katmanı

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **R1** | `uv`'nin kendi benchmark dosyasında **sayı yoktur**; içerik yalnızca bir **bar grafiği görselidir**. Ölçüm tabanı **tek bir dosya ve yalnız macOS**'tur.<br>Satıcının kendi uyarısı: *"Benchmark performance may vary dramatically across different operating systems and filesystems."*<br>⇒ *"10-100x"* iddiası **kendi deposunda doğrulanabilir sayıya dayanmıyor**. | birincil (arandı, yok) | çürütülemedi |
| **R2** | Kendi ölçümümüz (bu makine, Linux, Python 3.11.15, uv 0.8.17 ile pip 24.0; 7 doğrudan bağımlılık, 25 pakete açılıyor):<br>venv oluşturma pip 4,08 s ile uv 0,034 s ⇒ **120 kat**. Sıcak kurulum 36,66 s ile 0,39 s ⇒ **93 kat**. **Soğuk kurulum (ağ bağımlı)** 30,27 s ile 7,86 s ⇒ **3,9 kat**. Ortam diski 677 MB ile 514 MB.<br>Sonuç: 93 kat **gerçektir** — ama **mutlak tasarruf yaklaşık 36 saniyedir**.<br>Senaryo soğuksa (CI ya da ilk kurulum) kazanç **3,9 kattır**, çünkü **darboğaz ağdır**.<br>⚠️ Çelişki kaydı: pip'in **sıcak** kurulumu (36,7 s) **soğuk** kurulumundan (30,3 s) yavaştır ⇒ pip'in darboğazı indirme değil, **açma ve kurmadır**. | kendi ölçümümüz | çürütülemedi |
| **R3** | **Asıl gerekçe hız değildir.** `poetry` ortamınıza **49 Python paketi ve 56 MB** sokar; `pip-tools` 8 paket ve 13 MB; `uv` ise **tek statik ikilidir ve sıfır Python bağımlılığı vardır**.<br>⇒ `uv` proje bağımlılık grafiğiyle **hiç kesişmez** ⇒ **asla çakışmaz**. Bu, hızdan **daha sağlam** bir gerekçedir. | kendi ölçümümüz | çürütülemedi |
| **R4** | `src/` düzeni tartışması **karara bağlanmamıştır**: resmî paketleme metni iki düzeni **yan yana koyar**, tavsiye vermez, ampirik iddia içermez — tümü argümantatiftir.<br>Tek somut faydası, kurulu kopya yerine geliştirme kopyasının yanlışlıkla import edilmesini önlemektir ⇒ bu fayda **yalnız paketleyip dağıtıyorsanız** anlamlıdır. | birincil | çürütülemedi |
| **R5** | Ve tartışma pratikte **bedelsiz çözülmüştür**: `uv init --lib` zaten `src/` üretir (0,089 saniye, 14 satır yapılandırma, 6 dosya) ⇒ `src/` bir **maliyet değil, varsayılandır**. | kendi ölçümümüz | çürütülemedi |
| **R6** | Asgari yığının toplam maliyeti ölçüldü: pandas, numpy, scipy, matplotlib, pyarrow, ruff ve pytest birlikte **3,33 saniye**, 26 satır yapılandırma, 24 kilitli paket, 472 MB sanal ortam ve **insanın bakacağı 5 dosya** (4'ü otomatik üretiliyor). | kendi ölçümümüz | çürütülemedi |

### 6.2 Kalite katmanı — ailenin en önemli negatif bulgusu

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **R7** | Gerçekçi bir risk modülüne kasıtlı hatalar konuldu.<br>`ruff` varsayılan ayarla **7 hata** buldu — **hepsi hijyen** (kullanılmayan import ve değişken, mutable default).<br>`ruff --select ALL` **32 hata** buldu — fazladan 25'i docstring, tip notu, telif notu ve tırnak stiliydi ⇒ **gerçek hata artışı sıfırdır**.<br>**Look-ahead hatası (`df['ret'].shift(-1)`) iki modda da tespit edilmedi.** | kendi ölçümümüz | çürütülemedi |
| **R8** | `mypy`'ın ilk izlenimi **%100 gürültüdür**. Bağlam bir veri bilimi dosyasıydı ve `pandas-stubs`, numpy ile scipy kuruluydu (adil koşul).<br>Varsayılan ayarla **1 hata** (scipy stub'ı yok); `--strict` ile **6 hata** (5'i *"annotation eksik"*) ⇒ **gerçek hata sayısı sıfırdır**. | kendi ölçümümüz | çürütülemedi |
| **R9** | Ama `mypy` **iki taraflıdır: tip notlu sınırlarda kâr eder.** Aynı test, anotasyonlu kodda 4 gerçek hatayla koşuldu:<br>`DataFrame` beklenen yere `float` verilmesi **yakalandı**; `int` beklenen yere `str` verilmesi **yakalandı** (yapılandırma dosyası klasiği); eksik return ifadesi **yakalandı**; ama `df["clsoe"]` sütun adı yazım hatası **yakalanamadı**.<br>Sonuç: `mypy` **statik imzalarda kâr eder** ve **DataFrame içeriğinde kördür**. Ve veri biliminde hataların çoğu **DataFrame içindedir** ⇒ kapsama **yapısal olarak dardır**. | kendi ölçümümüz | çürütülemedi |
| **R10** | Bakım ağırlığı: `ruff`'ın **0 doğrudan bağımlılığı**, `mypy`'ın 12, `pytest`'in 14 vardır. `ruff` ile `uv` **aynı ekipten ve ikisi de sıfır bağımlılıklıdır** ⇒ kurulum riski yoktur. | birincil | çürütülemedi |
| **R11** | Tip ipuçlarının hata oranına etkisi üzerine ampirik literatür **aranamadı**: arama bütçesi tükenmişti ve akademik yayıncılar kapalıydı.<br>⚠️ Bu **"bulunamadı" DEĞİLDİR.** R7–R9 kendi kontrollü ölçümümüzdür ve **literatürün yerine geçmez**. | aranamadı | — |

### 6.3 Veri katmanı

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **R12** | `polars`'ın deposunda da **rakam yoktur**: README yalnızca *"very fast"* ve *"one of the best performing"* der, kendi benchmark sayfasına link verir. **Depoda üretilebilir sayı yoktur.** | birincil (arandı, yok) | çürütülemedi |
| **R13** | Kendi ölçümümüz (1,26 milyon satır × 7 sütun; 500 hisse × 2.520 gün; yaklaşık 40 MB parquet; gerçekçi portföy paneli):<br>parquet okuma pandas 0,247 s, polars 0,171 s, duckdb 0,515 s ⇒ **1,4 kat**.<br>**groupby ile 4 agregat** pandas **0,071 s**, polars **0,085 s** ⇒ **0,8 kat — polars YAVAŞ**.<br>sort ve 20 günlük hareketli ortalama 0,403 s ile 0,252 s ⇒ 1,6 kat.<br>universe join ve filtre 0,784 s ile 0,108 s ⇒ **7,2 kat**.<br>hisse başına yüzde değişim 0,279 s ile 0,244 s ⇒ 1,1 kat.<br>Sonuç: polars kazancı **0,8 ile 7,2 kat arasındadır**, ortancası yaklaşık **1,4 kattır**. **Pazarlamanın çağrıştırdığı 10-50 kat yoktur.** Tüm işlemler **1 saniyenin altındadır**. | kendi ölçümümüz | çürütülemedi ⚠️ *(antitezin "db-benchmark'ta polars kat kat hızlı" karşı iddiası **hatırlama düzeyindedir** ∧ antitez kendi belirsizliğini dürüstçe işaretledi; ölçüm hatırlamayı yener ⇒ **rakam korunur**, ama **ölçek bağımlılığı** kaydı güçlenir: bizim ölçümümüz 1,26M satırdır)* |
| **R14** | **Asıl darboğaz import'tur.** Import süreleri: pandas 0,73 s, polars 0,22 s, duckdb 0,12 s, numpy 0,20 s.<br>Beş işlemin pandas toplamı 1,78 saniyedir ⇒ **pandas import'u toplam iş yükünün %29'udur**.<br>⇒ Küçük veride kütüphane seçimi değil, **süreç başlatma baskındır**. | kendi ölçümümüz | çürütülemedi |
| **R15** | Parquet ile CSV karşılaştırması (aynı panel): CSV yazma 9,25 s, okuma 1,68 s, boyut 76,2 MB. Sıkıştırılmış CSV 26,93 s, 1,79 s, 28,6 MB. **Parquet 0,78 s, 0,53 s, 39,7 MB.**<br>Sütun alt kümesi okumada (7 sütundan 2'si) parquet 0,07 s, CSV 0,88 s ⇒ **12,6 kat**. | kendi ölçümümüz | çürütülemedi |
| **R16** | **Parquet'in asıl gerekçesi hız değil, doğruluktur.**<br>CSV round-trip'te `datetime64[us]` **sessizce string'e döner** ⇒ orijinal ile okunan **eşit değildir**. Parquet round-trip'te **bit aynıdır**.<br>⇒ Bir zaman serisi projesinde tarih sütunu string'e dönerse **leksik sıralama** olur ⇒ **sessiz doğruluk hatası**. | kendi ölçümümüz | sağ çıktı ⚠️ *(ayrıca antitez bunu **polars hükmüne karşı silah** olarak kullandı — bkz. R13 ve B8)* |
| **R17** | DVC'nin değeri **ağırlıklı olarak takım içindir**. README'nin kendi ifadeleri: *"Store them in your cloud storage"*, *"Share data and model files"*, *"collaborate with others"*.<br>⚠️ **Düzeltme:** kullanıcı tek kişiyse ve uzak depolama yoksa değer **sıfır DEĞİL, AZALMIŞTIR**. `dvc repro` uzak depolama olmadan da **yerel önbellekleme** (değişmeyen aşamaları atlama) ve **pipeline DAG'ı** sağlar. | birincil | çürütüldü → K3 |
| **R18** | DVC'nin maliyeti **98 paket ve 107 MB**'dır (PyPI'da 82 doğrudan bağımlılık). | kendi ölçümümüz | çürütülemedi |
| **R19** | Bağımsız db-benchmark sayılarına **erişilemedi**: barındıran iki adres de yanıt vermedi.<br>⇒ Hem bağımsız hem satıcı rakamları **aranamadı** ⇒ R13'ün kendi ölçümü bu boşluğu doldurur — **tek ölçekte**. | aranamadı | — |

### 6.4 Deney takibi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **R20** | Gerçek kurulum ağırlığı boş bir sanal ortama kurulup sayıldı: **mlflow 90 paket / 611 MB**; mlflow-skinny 41 / 64 MB; wandb 17 / 98 MB; dvc 98 / 107 MB.<br>**mlflow (611 MB) tüm bilimsel yığından (472 MB) büyüktür** ⇒ deney takibi eklemek ortamı **ikiye katlar**.<br>`mlflow-skinny` **10 kat hafiftir** ve çoğu solo kullanım için yeterlidir — **bu ayrım az bilinir**. | kendi ölçümümüz | çürütülemedi |
| **R21** | **MLflow 3.x dosya deposunu kaldırmıştır.** MLflow 3.14.0 ile `./mlruns` kullanılmaya çalışılınca **istisna fırlatır**: *"The filesystem tracking backend… is in maintenance mode and will not receive further updates. Please migrate to a database backend."*<br>⇒ İnternetteki *"pip install mlflow, mlruns'a yaz, bitti"* tavsiyesinin **tamamı MLflow 2.x içindir ve artık geçersizdir**.<br>Ölçüldü: sqlite arka ucu çalışır, ilk koşumda şema göçü 7,42 saniye ve 791 KB veritabanı; dosya deposu yalnız özel bir ortam değişkeniyle açılır. | kendi ölçümümüz | çürütülemedi |
| **R22** | Basit alternatifin ölçülmüş maliyeti: **8 satır Python, 0 bağımlılık, koşum başına 0,006 saniye**, satır başına bir JSONL kaydı (git SHA dahil).<br>⇒ **90 paket / 611 MB** karşısında **8 satır / 0 paket**. | kendi ölçümümüz | çürütülemedi |
| **R23** | Bakım canlılığı (PyPI son sürümleri): **canlı** olanlar mlflow 3.14.0 (2026-06-17), wandb 0.28.1 (2026-07-16), dvc 3.67.1 (2026-03-31); **terk edilmiş** olanlar backtrader (2023-04-19), pyfolio (2019-04-15), empyrical (2020-10-13). | birincil | çürütülemedi |
| **R24** | *"Kaç deneyden sonra manuel takip kırılır"* eşiği **aranamadı** ve **kestirim de verilmedi**. | aranamadı | — |

### 6.5 Yeniden üretilebilirlik

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **R25** | Tohumlama katmanları **birbirinin yerine geçmez**: eski API ile `[0.548814, 0.715189, 0.602763]`, yeni API ile aynı tohumda `[0.636962, 0.269787, 0.040974]` çıkar.<br>⇒ Farklı akışlardır ⇒ **eski kodu yeni API'ye taşımak sonuçları sessizce değiştirir**. | kendi ölçümümüz | çürütülemedi |
| **R26** | `random_state` verilmeyen bir RandomForest iki fit'te farklı tahmin üretir; `random_state=0` ile aynı üretir. | kendi ölçümümüz | çürütülemedi |
| **R27** | **En sinsi olan `PYTHONHASHSEED`'dir.** Sabitlenmezse `set` sıralaması **her koşumda değişir**: iki ardışık koşumda hisse evreni `['MSFT','AAPL','GOOG','TSLA']` ve `['MSFT','TSLA','AAPL','GOOG']` çıktı. `hash("AAPL")` de süreçler arası değişir.<br>⇒ Hisse evreni bir `set`'ten geliyorsa, **tüm tohumlar doğru olsa bile sütun sırası her koşumda değişir**. | kendi ölçümümüz | daraltıldı → K2 (bkz. §6.9-7) |
| **R28** | Notebook'un sıra dışı çalıştırılması **git diff'te görünmez**: `execution_count` değerleri `[1, 5, 3, 4]` ise okuyucuya *"filtre önce uygulandı"* izlenimi verilir, oysa Sharpe filtreden **önce** hesaplanmıştır.<br>Tespit **3 satır koddur**: kod hücrelerinin `execution_count` listesi `1..N` ile aynı mı? | kendi ölçümümüz | çürütülemedi |
| **R29** | Ağırlık uyarısı: `papermill` 103, `jupytext` 72, `nbdev` 23 doğrudan bağımlılık getirir.<br>⇒ Notebook'u *"düzeltmek"* için kurulan araç, düzeltmeye çalıştığı yığından **ağır olabiliyor**. | birincil | çürütülemedi |
| **R30** | Brifingteki notebook **%4** rakamının birincil doğrulaması **aranamadı**. **Teyit edilmedi, üzerine inşa edildi** — bu ayrım önemlidir ve kayda geçer. | aranamadı | — |

### 6.6 Finansal zaman serisi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **R31** | Minimum backtest uzunluğu formülü **bağımsız olarak doğrulandı**. Gerçek beceri sıfırken ve N varyant denendiğinde beklenen en yüksek in-sample yıllık Sharpe:<br>N=5 için 2 yılda 0,84 / 5 yılda 0,53 / 10 yılda 0,38 / 20 yılda 0,27.<br>N=10 için 1,11 / 0,70 / 0,50 / 0,35.<br>**N=45 için 1,58 / 1,00 / 0,71 / 0,50.**<br>N=128 için 1,85 / 1,17 / 0,83 / 0,59. N=1000 için 2,30 / 1,46 / 1,03 / 0,73.<br>⇒ *"5 yıl veriniz varsa 45'ten fazla bağımsız konfigürasyon denemeyin"* iddiası **birebir doğrulandı**. | kendi hesabımız | çürütülemedi |
| **R32** | **İkinci bağımsız yöntem aynı sonucu verdi.** Monte Carlo: saf gürültü, gerçek edge sıfır, 5 yıl in-sample ve 5 yıl out-of-sample, 200 tekrar.<br>N=1 için en iyi in-sample Sharpe −0,06 ve onun out-of-sample'ı 0,03. N=10 için 0,68 ve −0,04. **N=45 için 0,99 ve −0,01.** N=100 için 1,13 ve 0,01. N=1000 için 1,46 ve −0,04.<br>Simülasyon analitik formülle **iki ondalık basamağa kadar örtüştü** ve out-of-sample Sharpe **her zaman yaklaşık sıfır** çıktı.<br>⇒ **In-sample Sharpe, denenen seçim sayısının fonksiyonudur; becerinin fonksiyonu değildir.** | kendi simülasyonumuz | sağ çıktı ⚠️ — literatürle güçlü örtüşme |
| **R33** | Yayınlanmış finans literatürü aynı yöndedir: 452 anomalinin **%65'i** t>1,96 eşiğini geçemiyor; çoklu test eşiği t>2,78 alınırsa başarısızlık **%82,1**. 316 faktör kataloglandığında yeni faktör eşiğinin **t>3,0** olması gerektiği söyleniyor. 97 öngörücünün getirisi örneklem dışında **%26**, yayın sonrası **%58** düşüyor. | ikincil | çürütülemedi |
| **R34** | **Karşı görüş mevcuttur ve tek taraflı sunulmuyor:** *"Most claimed statistical findings in cross-sectional return predictability are likely true"* başlıklı çalışma, *"çoğu bulgu yanlış"* sonucunu **doğrudan reddediyor**.<br>Erişilemedi, ama **varlığı kayda değerdir** ⇒ **bu literatür tartışmalıdır**. | çelişkili (erişilemedi) | — |
| **R35** | **Veri sızıntısının ölçülmüş etkisi.** Ekonomik gerekçesi olmayan bir öznitelikle: naif karıştırılmış k-fold **R² ≈ +0,85**, purged k-fold **R² ≈ −1,2**.<br>Tamamen öngörülemez bir hedefte naif R² **0,83–0,91** çıktı — **saf gürültüde** — ve purged sonrası ortalama tahmininin altına düştü.<br>Hava kalitesi verisinde 3 normal gecikme ile naif R² 0,07 iken, **tek masum bir kümülatif saat sayacı eklenince naif R² 0,99** oldu; purged değer (−1,52) **kıpırdamadı**. | kendi ölçümümüz | çürütülemedi |
| **R36** | **Dürüstlük notu: sızıntı her zaman felaket değildir.** Aynı kaynakta 4.284 haneli bir veri setinde naif k-fold ile walk-forward arasındaki **zamansal** boşluk yalnız **%1,60** (güven aralığı %1,27–1,94); asıl ısıran sızıntı **hane bazlıydı (%6,03)**.<br>⇒ Ders: hangi bölmeye ihtiyacın olduğu **neyin üzerinde çalıştığına bağlıdır** — kategorik korku değil, **ölçüm**. | ikincil | çürütülemedi |
| **R37** | **Naif look-ahead testi işe yaramıyor.** Klasik *"veriyi kes, sinyal değişiyor mu bak"* testi yazıldı ve **bilinen hatalı fonksiyonu yakalayamadı**.<br>Sebep ölçüldü: `shift(-1)` ile kesme noktası birlikte yalnız **1 satırın** farklılaşmasına izin veriyor, ve eşiklenmiş (boolean) bir sinyalde bu fark **yaklaşık %50 olasılıkla** tesadüfen aynı değere çöküyor. Örnekte 200 satırlık örtüşmede **farklılaşan satır sayısı sıfırdı**.<br>**Çalışan sürüm ölçüldü ve 10 kesme noktasının 10'unda yakalıyor:** kesme noktasını **süpür**, boolean değil **ham float** karşılaştır, **NaN duyarlı** eşitlik kullan.<br>⇒ Bu **yaklaşık 20 satırlık pytest**, `ruff` ve `mypy`'ın **tamamen kör olduğu** hata sınıfını yakalar. | kendi ölçümümüz | sağ çıktı ⚠️ |
| **R38** | **Survivorship bias simüle edildi:** 1000 firma, 10 yıl, gerçek drift yılda %6, zirveden %80 düşende delist ⇒ firmaların **%6,5'i siliniyor**.<br>Eşit ağırlıklı yıllık getiri tam evrende **%5,53**, yalnız hayatta kalanlarda **%6,67** ⇒ **abartma yılda %1,14**.<br>Bu, gerçek fon verisindeki yaklaşık **%0,9/yıl** ölçümü ve genel **%1–4** bandıyla **uyumludur**. | kendi simülasyonumuz | çürütülemedi |
| **R39** | **Look-ahead bias'ın ölçülmüş etkisi:** 48 araştırma sonucundan **37'si**, point-in-time veri yerine gecikmeli veri kullandığı için aylık ortalama spread ve ilk çeyrek getirilerini **abartmıştır**. Kümülatif getiri farkı **%39'a kadar** çıkıyor; 9 baz puanlık bir sapma **%3,8 gerçeklikten sapma** üretiyor. | ikincil | çürütülemedi |
| **R40** | Sızıntı **disiplinler arası sistemiktir**: en az **294 makale ve 17 disiplin**; erken sürümde 329 makale ve 30 alan. Sekiz tipli bir sızıntı taksonomisi vardır. | ikincil | çürütülemedi |
| **R41** | **Ekosistem uyarısı: projenin alanındaki araçların çoğu ölüdür.**<br>Ölü: backtrader (2023-04-19), pyfolio (2019-04-15), empyrical (2020-10-13).<br>Canlı: backtesting 0.6.6 (2026-07-22), vectorbt 1.1.0 (2026-07-05), quantstats (2026-01-13), yfinance 1.5.2 (2026-07-23).<br>`pypbo` (PBO/DSR/MinBTL kütüphanesi) README'sinde kendi kaydını taşıyor: *"TODO: Add test cases"* ⇒ **test edilmemiştir**. | birincil | çürütülemedi |

### 6.7 Asgari uygulanabilir yığın

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§6.7-1** | **Birinci sırada nedensellik testleri (pytest)** gelir — kesme noktası süpüren look-ahead testi. Bu, **projenin doğruluğunu belirleyen tek katmandır**: `ruff` 1 hatanın 0'ını, `mypy` 1'in 0'ını, **bu test 10'un 10'unu** yakalıyor. Sızıntı BTC verisinde R²'yi +0,85 ile −1,2 arasında oynatıyor. Maliyet **yaklaşık 20 satır**. | kendi ölçümümüz | — |
| **§6.7-2** | **İkinci sırada deneme sayacı ve out-of-sample kilidi** gelir. Kaç varyant denendiği yazılmazsa Sharpe **anlamsızdır**: 5 yıl ve 45 varyant, **saf şanstan** Sharpe 1,0 üretir (iki bağımsız yöntem). Maliyet **bir metin dosyası, sıfır bağımlılık**. | kendi ölçümümüz | — |
| **§6.7-3** | Üçüncü sırada **uv** gelir: dört aracın işini tek statik ikiliyle ve **sıfır Python bağımlılığıyla** yapar; `uv init --lib` `src/` düzenini bedava getirir. Maliyet 3,33 saniye. | kendi ölçümümüz | — |
| **§6.7-4** | Dördüncü sırada **pandas, numpy, scipy** gelir: bu ölçekte polars ortanca 1,4 kat ve groupby'da **0,8 kat yavaştır**. Zaten yığındadır. | kendi ölçümümüz | — |
| **§6.7-5** | Beşinci sırada **Parquet (pyarrow)** gelir: gerekçe **hız değil doğruluktur**; yan faydası 12 kat yazma ve 1,9 kat boyut. Maliyet tek satır. | kendi ölçümümüz | — |
| **§6.7-6** | Altıncı sırada **ruff** gelir: sıfır bağımlılık, sıfır yapılandırma; hijyen borcunu sıfırda tutar — **ama hata bulmasını bekleme**. Maliyet yaklaşık 2 saniye. | kendi ölçümümüz | — |
| **§6.7-7** | Yedinci sırada **pytest** gelir: birinci ve ikinci maddeyi çalıştıran koşum aracıdır. 14 bağımlılık. | kendi ölçümümüz | — |
| **§6.7-8** | Sekizinci sırada **tohum disiplini** gelir: yeni API'de tohumlu generator, her sklearn çağrısında `random_state`, `PYTHONHASHSEED=0`, ve `set` yerine `sorted()`. Gerekçe: `set` sıralaması koşumlar arası değişir, **tüm tohumlar doğruyken bile**. Maliyet **4 satır**. | kendi ölçümümüz | — |
| **§6.7-9** | Dokuzuncu sırada **JSONL deney kaydı (git SHA'lı)** gelir: 8 satır, 0 bağımlılık, 0,006 saniye — **90 paket ve 611 MB'a karşı**. | kendi ölçümümüz | — |
| **§6.7-10** | Onuncu sırada **notebook yalnız keşif, modül gerçek** kuralı ve `execution_count` kontrolü gelir: sıra dışı çalıştırma git diff'te görünmez. Maliyet 3 satır. | kendi ölçümümüz | — |
| **§6.7-11** | Toplam: **yaklaşık 3,3 saniye kurulum, 26 satır yapılandırma, tek ek dosya.** | kendi ölçümümüz | — |

### 6.8 Ne alınmaz

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§6.8-1** | **MLflow ve W&B alınmaz:** 90 paket / 611 MB, tüm yığından (472 MB) büyük; ayrıca MLflow 3.x dosya deposunu kaldırdığı için *"sadece pip install"* tavsiyeleri **geçersizdir**. Yerine 8 satır JSONL. Gerekirse `mlflow-skinny` (41 paket / 64 MB). | kendi ölçümümüz | çürütülemedi |
| **§6.8-2** | **DVC alınmaz:** 98 paket / 107 MB ve değeri **ağırlıklı olarak takım ve bulut** senaryosundadır.<br>⚠️ **Düzeltme:** tek kişide değer **sıfır değil, azalmıştır** — `dvc repro` yerel önbellekleme ve pipeline DAG'ı sağlar. **Hüküm değişmez, gerekçe düzelir:** azalmış değer 98 paketlik maliyeti **karşılamaz**. Yerine SHA256 ve tarihli klasör. | birincil | çürütüldü → K3 |
| **§6.8-3** | **poetry alınmaz:** ortama 49 paket / 56 MB sokar; uv aynı işi **sıfır Python bağımlılığıyla** yapar. | kendi ölçümümüz | çürütülemedi |
| **§6.8-4** | **`mypy --strict` başlangıçta alınmaz:** ilk çıktı %100 gürültü ve 0 gerçek hatadır; sütun adı hatasını yakalayamaz. **Sonradan**, kararlı `src/` modüllerinin imzalarında değerlidir — orada 4 hatanın 3'ünü yakalar. | kendi ölçümümüz | çürütülemedi |
| **§6.8-5** | **`ruff --select ALL` alınmaz:** 7'den 32 hataya çıkar ve **gerçek hata artışı sıfırdır**. | kendi ölçümümüz | çürütülemedi |
| **§6.8-6** | **polars şimdi alınmaz:** ortanca 1,4 kat, groupby'da yavaş, tüm işlemler 1 saniyenin altında. Veri 5-10 GB'ı aşarsa ya da iş yükü join ağırlıklı olursa **yeniden değerlendirilir** (orada 7,2 kat).<br>⚠️ **Gerekçe EKSİK işaretlendi:** bu hüküm **yalnız hız eksenine** dayanıyor. Antitezin yakalaması: R16'nın kendi mantığı (*"parquet'in gerekçesi hız değil dtype bütünlüğü"*) polars'a geri uygulanırsa, polars'ın asıl argümanı da hız değil **şema katılığı, lazy-evaluation'da erken tip hatası, Arrow bellek modeli ve null semantiği tutarlılığı** olabilir. **Bu eksen ölçülmedi** ⇒ B8 borcu.<br>⇒ Hüküm ayakta, ama *"ölçtük ve eledik"* demek **yanlış olur**. | kendi ölçümümüz (tek eksen) | daraltıldı → K7 |
| **§6.8-7** | **papermill, jupytext ve nbdev alınmaz:** sırasıyla 103, 72 ve 23 doğrudan bağımlılık. Çözüm araç eklemek değil, **mantığı `src/`'ye taşımaktır**. | birincil | çürütülemedi |
| **§6.8-8** | **Docker alınmaz:** `uv.lock` tek kişilik projede yeterlidir; maliyeti bu ölçekte getirisini aşar. | çıkarım | çürütülemedi |
| **§6.8-9** | **backtrader, pyfolio ve empyrical alınmaz — terk edilmişlerdir** (son sürümleri 2023, 2019, 2020). | birincil | çürütülemedi |

### 6.9 A23 iddia listesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§6.9-1** | uv'nin 93 katlık sıcak kurulum avantajı haftada yaklaşık **36 saniye** tasarruf ettirir; asıl gerekçesi hız değil, **sıfır bağımlılıklı tek ikili** olmasıdır. | kendi ölçümümüz | çürütülemedi |
| **§6.9-2** | Bu ölçekte polars ortanca 1,4 kattır ve groupby'da yavaştır; şimdi almak **erken optimizasyondur**. — hüküm korunur, **gerekçe eksiktir** (K7). | kendi ölçümümüz | daraltıldı → K7 |
| **§6.9-3** | Statik analiz araçları finansal zaman serisi projesindeki **doğruluk kritik hata sınıfını yapısal olarak yakalayamaz**. | kendi ölçümümüz | çürütülemedi |
| **§6.9-4** | Deney takibi araçları tek kişilik ölçekte **net negatiftir**. | kendi ölçümümüz | çürütülemedi |
| **§6.9-5** | Bir backtest'in in-sample Sharpe'ı, **denenen varyant sayısı raporlanmadan yorumlanamaz**. | kendi ölçümümüz | sağ çıktı ⚠️ |
| **§6.9-6** | Parquet'i tercih etmenin baskın gerekçesi hız ya da boyut değil, **dtype bütünlüğüdür**. | kendi ölçümümüz | sağ çıktı ⚠️ |
| **§6.9-7** | **Hash sırasına duyarlı kod yolu içeren** hiçbir koşum, `PYTHONHASHSEED` sabitlenmeden tam olarak yeniden üretilebilir değildir — tüm RNG tohumları doğru olsa bile.<br>⚠️ Eski hâli *"hiçbir koşum"* diyordu ⇒ **fazla geniş**. Hash sırası **yalnız hash duyarlı kod yollarını** etkiler; saf numpy/pandas sayısal hattı (sabit sütun sırası, array tabanlı) **bağımsız olabilir**.<br>Ve **kendi ölçümümüz (R27) zaten mekanizmayı `set` sıralaması üzerinden gösteriyordu** ⇒ koşul **`set` kullanımıdır**, evrensel değildir. Pratik tavsiye **değişmez**. | kendi ölçümümüz | daraltıldı → K2 |
| **§6.9-8** | Naif look-ahead testi eşiklenmiş sinyallerde işe yaramaz ve **yanlış güven verir**. | kendi ölçümümüz | sağ çıktı ⚠️ |
| **§6.9-9** | DVC'nin tek kişilik projedeki getirisi **azalmıştır** ve **98 paketlik maliyeti karşılamaz**.<br>⚠️ Eski hâli *"getirisi sıfırdır"* diyordu ⇒ **çürütüldü**. **Hüküm (alınmaz) değişmez, gerekçe düzelir.** | birincil | çürütüldü → K3 |

### 6.10 A23 — kapatılamayanlar

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§6.10-1** | **Aranamadı** (bütçe ya da kapı engeli — **yokluk kanıtı DEĞİL**): tip ipuçlarının hata oranına etkisi literatürü, bağımsız pandas-polars sayıları, notebook %4 rakamının birincil doğrulaması, manuel takip kırılma eşiği, ruff'ın bağımsız hız ölçümü, R34'teki karşı görüşün rakamları. | aranamadı | — |
| **§6.10-2** | **Arandı, rakam yok** (bu bir **yokluk bulgusudur**): uv deposunda sayısal benchmark, polars deposunda sayısal iddia. | arandı, yok | — |
| **§6.10-3** | **Kapatılamayan şeritler:** Kalite ve Veri alt şeritlerinin **literatür** taraması dönmedi. **Ajan içeriklerini elinde doğrulayamadığı için aktarmadı ve uydurmadı**; her iki alanın **ölçüm** tarafını kendi deneyleriyle kapattı. | — | — |

---

## 7. Üç model ve karar önerisi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§7.1** | **Model A — çerçeve benimseme.** Yerleşik endüstri çerçevelerinden bir alt küme alınır; her yığın kararı ADR olarak yazılır, altı ayda bir kendi radar güncellenir.<br>Artıları: hazır şablon vardır, ortak sözlük kurar, benimsemesi kolaydır, CV'de tanınır.<br>Eksileri: **F4 ile F7 arası hepsi folklordur** — bu çerçevelerin hiçbirinin *sonucu* ölçülmemiştir. 921 deponun yaklaşık %50'sinde 5'ten az kayıt vardır ⇒ pilot sonrası terk oranı yüksektir, ve JARVIS zaten tek kişiliktir ⇒ terk riski daha da yüksektir.<br>⇒ **Ölçülmemiş bir yöntemi benimsemek, ölçüm önceliğiyle doğrudan çelişir.** | çıkarım | — |
| **§7.2** | **Model B — ekosistem sağlığı eşiği.** Karar *yöntemi* değil, karar *girdisi* standartlaştırılır: her bağımlılık için **indirme sırası** (ilk 500'de mi), **son sürüm tarihi** ve **bakımcı sayısı** zorunludur. Yıldıza **hiç bakılmaz**.<br>Artıları: dayandığı her şey **ölçülmüştür**; *"ilk 500'de kal"* kuralı terk riskini **6,3 kat** düşürür; tek kişilik ölçekte uygulanabilir (üç sayı, üç API çağrısı).<br>Eksileri: *seçtiğin şeyin yaşayıp yaşamayacağını* ölçer, *doğru şeyi seçip seçmediğini* **değil** ⇒ asimetrinin ölçülmüş yarısını alır, **ölçülmemiş yarısını boş bırakır**. Yenilikçi ama az kullanılan bir aracı **sistematik olarak reddeder**; *"popüler olan doğrudur"* kaymasına açıktır. | kendi ölçümümüz | — |
| **§7.3** | **Model C — kapatılmış geri bildirim döngüsü.** Karar yöntemi **öğrenme mekanizmasıyla birleştirilir**: her yığın kararında önce tahmin ve olasılık yazılır, sonra kaynak açılır, Brier skorlanır.<br>Artıları: mimarinin **kötü öğrenme ortamı** olma sorununu doğrudan hedefler — geri bildirim döngüsünü **yapay olarak kısaltır**. *"Yazılı açık strateji"* gerek koşulunu **yapısal olarak** sağlar. Brier skoru **insan kolaylaştırıcının yerini tutan tek nesnel metriktir** ve JARVIS'te insan kolaylaştırıcı yoktur. Model B'yi **içerir**, dışlamaz.<br>Eksileri: kalibrasyon eğitiminin işe yaradığı **çelişkili kanıta sahiptir**; GJP'de bile kazanım **%6-7**, mütevazıdır. Sürtünme yüksektir: her karar öncesi yazma zorunluluğu, küçük kararlarda **terk edilme riski** taşır. | çıkarım | — |
| **§7.4** | **Öneri: Model C, Model B'yi girdi olarak alacak şekilde — ama sürtünme eşikli.**<br>Birincisi: **ölçüm önceliği Model A'yı eler.** Ölçülmemiş çerçeve benimsemek, bu oturumun kendi bulgusuyla çelişir.<br>İkincisi: **Model B tek başına yetersiz ama vazgeçilmezdir.** Ölçülmüş yarıyı almamak için sebep yoktur, ama ölçülmemiş yarıyı boş bırakmak da kabul edilemez.<br>Üçüncüsü: **Model C'nin zayıflığı dürüstçe kaydedilir** — kalibrasyonun etkisi tartışmalıdır, **ama alternatifi yoktur**. İnsan kolaylaştırıcı olmayan bir sistemde nesnel performans verisi üretebilen başka mekanizma **bulunamadı**. Yani bu, *"en iyi kanıtlı seçenek"* değil, **"tek uygulanabilir seçenektir"** — fark önemlidir.<br>⚠️ **K6 sonrası iki ek kayıt:** *"tek mekanizma"* **bulunabilen tek** demektir, kanıtlanmış tek değil; ve **kalibrasyon eğitiminin mimari karara transferi ölçülmemiştir** — GJP'nin %6-7'si tahmin görevlerinde ölçülmüştür.<br>⇒ Model C yine de önerilir, ama Salih bunu *"kanıtlanmış yöntem"* olarak değil, **"ölçülmemiş ama tek uygulanabilir yöntem, ve kendi ölçümünü üretecek biçimde kurulmuş"** olarak imzalamalıdır. L7 ve L15'in Brier deltası **tam olarak bu transferi ölçer**.<br>Dördüncüsü: **sürtünme eşiği zorunludur.** ADR'lerin %50'si 5 kayıttan sonra terk edildiyse, tam protokol her karara uygulanamaz. Eşik önerisi: **yalnız geri alması pahalı kararlar** tam protokole girer (publish, para, kişisel veri, pahalı geri alma, yön değişimi); altı Model B'nin üç sayısıyla geçilir.<br>**Bu bir Katman 1 kararıdır ve Salih imzası bekler.** | çıkarım | daraltıldı → K6 |

---

## 7.1 A24 müfredatı

*Tasarımın tek cümlelik gerekçesi: mimari, geri bildirimi **yıllar mertebesinde gecikmiş** ve **sonuç yanlılığıyla kirlenmiş** kötü bir öğrenme ortamıdır. Bu yüzden müfredat **konu öğretmez**; **yapay olarak kapatılmış bir geri bildirim döngüsü imal eder**. Tek mekanizma: tahmin et, yaz, aç, skorla.*

**Değişmez kurallar:** kaynak açılmadan önce tahmin ve gerekçe dosyaya yazılır · her oturumda **en az iki vaka** karşılaştırılır · sonuç açılmadan önce **süreç puanı** verilir · her oturum çıktısı **açıkça formüle edilmiş bir kural** içerir · skorlama şüpheli olduğu için her oturum hem **Brier** hem **kural transferi** ile ölçülür.

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **L7** | **Taban kalibrasyon:** 25 ikili teknoloji seçimi önermesi (%50-100 güven) ve 10 aralık tahmini (%90). Ölçülen şey konu bilgisi değil, **kendi güven ayarıdır**.<br>DONE: Brier skoru **sayı olarak** dosyada ve %90 aralıklarının isabet oranı yazılı. Beklenen taban yaklaşık **%60-70**. **Skorun iyi ya da kötü olması DONE'u etkilemez — kaydedilmiş olması DONE'dur.** | çıkarım | — |
| **L8** | **Kör kata:** gerçek bir sistemin **yalnız gereksinimleri** verilir, mimarisi gizlenir. Yığın kararı, gerekçe ve 3 olasılıklı tahmin yazılır, sonra gerçek mimari açılır.<br>DONE: 1 kata artefaktı ve 3 skorlanmış tahmin. **Ek ölçüt:** yazılan gerekçe sayısı — *yetinmecilik göstergesi*; 3'ten az gerekçeyle karar verildiyse işaretlenir. | çıkarım | — |
| **L9** | **Zıt vaka çifti:** aynı problemde **ters** karar vermiş iki gerçek vaka okunur ve ortak şema çıkarılır.<br>DONE: **en fazla 5 koşul değişkeni** listesi — kararı çeviren eşikler. Doğrulama **üçüncü, görülmemiş** vakaya uygulanır ve tahmin önce yazılır. **Şema 3. vakayı tutmuyorsa oturum DONE değildir**, revize edilir. | çıkarım | — |
| **L10** | **Karar arşivi (sonucu kapalı):** en az 5 yıllık gerçek kararlar okunur; **yalnız gerekçe ve alternatifler bölümü** okunur, kabul/red ve bugünkü durum **tahmin edilir**, sonra açılır.<br>DONE: en az 8 karar, her biri için tahmin ve olasılık kaydı, Brier hesabı. **Kritik ölçüt:** L7 tabanına göre **Brier deltası** raporlanır — **kötüleşme de geçerli sonuçtur**. | çıkarım | — |
| **L11** | **Başarısızlık serisi:** tek bir kategoriden 5 postmortem okunur; her biri okunmadan önce *"bu kategoride kök neden ne olur"* tahmini yazılır.<br>DONE: *"başarısızlık modu → mimari önkoşul"* tablosu, **en az 10 satır**, her satırda URL. Her satır **mimariye atfedilebilir** ya da **operasyonel** diye etiketlenir; ayrım oranı raporlanır. | çıkarım | — |
| **L12** | **Süreç-sonuç ayrıştırma:** kendi geçmiş 3 kararı **sonuca bakmadan** süreç rubriğiyle puanla (alternatif sayısı, ödünleşim yazılı mı, geri alma maliyeti düşünülmüş mü, varsayım yazılı mı), sonra sonuca bak ve yeniden puanla.<br>DONE: iki puan seti ve fark tablosu. Ölçülen şey **kendi sonuç yanlılığının büyüklüğüdür** (beklenen: sıfırdan farklı). Rubrik dosyası **kalıcı artefakt** olur. | çıkarım | — |
| **L13** | **Çapa kırma ve premortem:** güncel yığın kararına (a) ilk aklına gelen çözümü yaz ve **kenara koy**, (b) *"6 ay sonra bu seçim battı, neden?"* sorusunu sor, (c) özgeçmiş güdümlü seçim ve büyük ölçek transplantı kontrolü yap.<br>DONE: **en az 8 başarısızlık nedeni**, **eylem temelli** ifadeyle; bunlardan **en az 2'si tasarımı fiilen değiştirmiş** olmalı. Değiştirmediyse **"neden değiştirmedi"** yazılır. | çıkarım | — |
| **L14** | **Dış görüş / referans sınıfı:** kendi proje türü için **en az 5 karşılaştırılabilir gerçek proje** bulunur, süre/ekip/maliyet sayıları toplanır, kendi tahmini **aralık** olarak dış görüşten üretilir.<br>DONE: 5 satırlık referans sınıfı tablosu (sayılar ve URL) ve kendi tahmininin **iç görüş ile dış görüş** iki versiyonu; **ikisinin farkı yazılı**. | çıkarım | — |
| **L15** | **Yeniden kalibrasyon ve kapanış:** L7 ile **aynı formatta** yeni bir set (aynı sorular değil).<br>DONE: Brier deltası ve %90 aralık isabet deltası. **Dürüstlük şartı:** iyileşme yoksa **"iyileşme yok"** yazılır — negatif sonuç müfredatın başarısızlığı değil, **ölçümün çalıştığının kanıtıdır**. | çıkarım | — |
| **§7.1-1** | **Kadans:** L7 ve L15 çerçeve oturumlarıdır; aradakiler sıralanabilir, **ama L9 (zıt çift) L10'dan ÖNCE** gelmelidir — şema olmadan arşiv okumak **yüzeysel ipucu toplamaya** döner.<br>**İskele düşürme:** L11'den sonra rubrik ve hatırlatma kartı zorunlu olmaktan çıkar (uzmanlık tersine dönmesi riskine karşı, d = 0,971). **Bu düşüşün doğru zamanı ölçülmedi.**<br>**Tekrar ziyaret:** L9'un vaka çifti L13'te **farklı amaçla yeniden okunur**, yeni vaka eklemeden. | çıkarım (zamanlama: **kestirim**) | — |
| **§7.1-2** | **Müfredatın kendi zayıflığı (ajanın beyanı, korunuyor):** L10 ve L11'in mimari karar kalitesini artırdığına dair **ölçülmüş kanıt yoktur**. Mekanizma gerekçesi sağlamdır, **sonuç kanıtı yoktur** ⇒ bu iki oturum müfredatın **en spekülatif kısmıdır**, ve DONE'ları bu yüzden *"kavrayış"* değil **artefakt sayısı** olarak tanımlanmıştır. | kestirim | — |
| **§7.1-3** | **İkinci zayıflık:** L12'nin rubriği **kendi imalatımız** olmak zorundadır — valide edilmiş bir mimari karar kalitesi rubriği literatürde **bulunamadı**. Yani L12 kendi ölçüm aracını da üretir; bu, ölçümün **kalibre edilmemiş** olduğu anlamına gelir. | kestirim | — |

---

## 8. Açık borçlar

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **B1** | ~~A23 inmedi~~ ⇒ **KAPANDI**; §6 olarak eklendi. | — | kapandı |
| **B2** | ~~Antitez koşulmadı~~ ⇒ **KAPANDI 2026-07-26.** A22, A24 ve A23 için **araçsız** koştu ⇒ mantıksal saldırılar tam güçte, olgusal karşı örnekler hatırlama düzeyinde. Sonuç: **K1–K8**. | ölçüm | kapandı |
| **B3** | Akademik rakamların **hiçbiri birincil metinden değildir**. Erişim açık bir oturumda teyit gerekir; öncelik: kasıtlı pratik yüzdeleri, simülasyon d değerleri, GJP %6-7. | aranamadı | — |
| **B4** | `arxiv.org/html/...` yolu **denenmedi** — açık listede olmadığı için atlandı. Kısıt gevşerse **en yüksek getirili tek kanaldır**. | — | — |
| **B5** | Mimari uzmanlıkta **protokol analizi güncel değildir**: temel çalışmalar 1984-2010 arası ve tek haneli ya da onlu denek sayılıdır. **Bulut, mikroservis ve yönetilen hizmet çağında uzman-acemi protokol çalışması yoktur.** | arandı, yok | — |
| **B6** | **Tek kişilik ölçekte teknoloji seçimi ölçümü yoktur** — ailenin en büyük kanıt boşluğu ve Salih'in tam bulunduğu yer. **Kapatılamaz, ama üretilebilir.** | arandı, yok | — |
| **B7** | Model C'nin **sürtünme eşiği ölçülmedi**: eşiğin doğru yeri bir **tahmindir**; L15'te ölçülebilir. | kestirim | — |
| **B8** | **polars'ın şema katılığı ve null semantiği ekseni ölçülmedi** (K7). R13 yalnız **hız** eksenindedir; *"şimdi alınmaz"* hükmü ayakta ama **eksik gerekçelidir**. | — (yeni) | K7'den doğdu |
| **B9** | **Kalibrasyonun mimari karara transferi ölçülmedi** (K6). Model C'nin çekirdek varsayımıdır; L7'den L15'e Brier deltası bunu ölçmek üzere tasarlanmıştır ⇒ **borç, modelin kendi içinde kapanacaktır**. | — (yeni) | K6'dan doğdu |

---

## 9. Fikir kutusu adayları

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **V64** | **"Kaynak kapalıysa veriyi üret."** Kapalı yayıncıların etrafından dolaşılıp PyPI, npm ve replikasyon CSV'lerinden **dört bağımsız birincil ölçüm** üretildi. Bu, oturumun en güçlü birincil veri tabanıdır ve **taktik olarak tekrarlanabilir**: birincil kaynak kapalıysa replikasyon deposu, registry API'si ya da ham veri CSV'si denenir. Atlas brifinglerine **standart madde** adayıdır. | kendi ölçümümüz | — |
| **V65** | **Kendi boşluğumuzu kendimiz doldurmak.** B6 literatürde **kapatılamaz** ama JARVIS'te **üretilebilir**: L7–L15 zaten Brier skoru üretiyor. Örneklem 1 olur — ama **ölçülmüş** bir 1'dir, ve alan bunun *hiç* ölçülmediğini söylüyor. | çıkarım | — |
| **V66** | **ADR'ye "gözlenmiş sonuç" alanı.** 13 şablonun hiçbirinde yoktur, literatürde de soru sorulmamıştır. Kendi şablonumuza eklemek **hem pratik hem özgündür**: karar anını değil, **kararın sonucunu** kayda geçirir. Model C'nin doğal artefaktıdır. | arandı, yok | — |
| **V67** | **Yıldız yasağı.** JARVIS'te hiçbir kararda GitHub yıldızı **kriter olarak anılmaz**; yerine indirme sırası, son sürüm tarihi ve bakımcı sayısı kullanılır. Kural küçüktür, dayanağı ölçülmüştür. | kendi ölçümümüz | — |
| **K10** | *(Yeni, K5'ten türedi.)* **Önerme formunda `¬` kullanılan her cümlede kapsam parantezle sabitlenir.** Doğuş sebebi: antitez bizim bir cümlemizi **tam tersine** okudu, çünkü olumsuzlamanın kapsamı Türkçe yüzeyde ayrışmıyordu. | ölçüm (canlı vaka) | — |

---

## 10. Kapanış

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§10.1** | Aile A22, A24 ve A23'tür; **antitez koştu** (araçsız, 0 araç çağrısı).<br>Sonuç: **3 çürütme** (K1 vaka sayısı, K3 DVC, iç tutarsızlık kaydı), **5 daraltma** (K2, K4, K6, K7, K8), **1 yeniden yazım** (K5, olumsuzlama kapsamı) ve **3 sağ çıkan iddia**. | ölçüm | — |
| **§10.2** | **İki şerh birlikte okunur.** Birincisi: araçsız tur olduğu için **mantıksal** saldırılar (iç çelişki, aşırı genelleme, ölçüm kapsam uyuşmazlığı) **tam güçtedir**; **olgusal karşı örnekler hatırlama düzeyindedir** ve borç açar, hüküm değiştirmez.<br>İkincisi: *"sağ çıktı"* damgası **"aynı-aile hakemi karşısında sağ kaldı"** demektir — antitez ajanları tez ajanlarıyla aynı model ailesindendi ve öz tercih sapması aile düzeyine yayılır. | çıkarım | — |
| **§10.3** | **Kanıt tabanı:** dört kendi ölçümümüz (PyPI n=478, PyPI 4×500, npm 220.469, StarScout ham CSV), A23'ün tamamı bu makinede kendi ölçümü, geri kalan tümü **ikincil** ve abstract katmanından. | — | — |
| **§10.4** | **Karar önerisi:** Model C (B içerilerek, sürtünme eşikli) — **Katman 1, Salih imzası bekler**. Gerekçe *"en iyi kanıtlı"* değil, **"tek uygulanabilir ve kendi varsayımını ölçecek biçimde kurulmuş"**. | çıkarım | daraltıldı → K6 |
| **§10.5** | **En değerli meta bulgu:** antitezin **yanlış anlaması** (K5), metnimizin kendi belirsizliğinin **ölçümü** oldu.<br>*"Antitez ajanının yanlış anladığı her cümle, o cümlenin yeniden yazılması gereken yerdir."* | çıkarım | — |
