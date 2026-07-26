# Tech Stack Atlası — seçim, öğrenme, ölçüm

*Kayıt: 2026-07-26 · Carvis (CC, yan-oturum m.41) · Talep: "öğrenme hattına tech stackleri ve sistemlerde projelerde tech stack oluşturmayı öğrenmem gerekiyor / araştır atlasları koş rapor yaz (sadece ai to ai)"*

**REGISTER BEYANI:** Salih açıkça **"(sadece ai to ai)"** dedi. Bu raporun insan-yüzü (`INSAN-*`) muadili **üretilmeyecek**; compiler formülü (`2026-07-26-compiler-formulu.md`) F8 gereği bu dosyaya uygulanmaz. Teknik kayıt tek kayıttır.

**Aile kapsamı:** A22 (teknoloji seçiminin ölçülmüş kanıt tabanı) · A24 (karar-vermeyi öğrenme müfredatı) · A23 (DS/ML asgari yığını) — **A23 koşum sırasında, ek olarak inecek (§6 boş bırakıldı, borç kaydı §8'de).**

---

## 0 — Dürüstlük kapısı

Bu oturumun tüm ailelerinde geçerli olan erişim rejimi burada da geçerli:

| Kanal | Durum |
|---|---|
| ScienceDirect · SpringerLink · SAGE · Wiley · ACM DL · IEEE Xplore · Cambridge Core · JSTOR · Royal Society · PubMed tam metin | **403** |
| `*.edu` · `*.github.io` · **tüm PDF'ler** (arXiv PDF dahil) | **403** |
| `arxiv.org` · `export.arxiv.org` · `mcfunley.com` | **403** |
| `github.com` (HTML) · `api.github.com` · `codeload.github.com` | **403** ← *görev brifinginde "açık" denmişti; A22 ajanı düzeltti* |
| `api.crossref.org` · `semanticscholar.org` | **403** → DOI/atıf doğrulaması yapılamadı |
| **`raw.githubusercontent.com`** | **AÇIK** |
| **`pypi.org`** (proxy bypass listesinde) | **AÇIK — doğrudan** |
| **`registry.npmjs.org`** (proxy bypass listesinde) | **AÇIK — doğrudan** |
| `api.npmjs.org` (indirme sayıları) | 403 → search API'nin gömdüğü `downloads`/`dependents` alanları kullanıldı |

**Sonuç:** akademik bulguların **tamamı [K]** — arama motoru abstract katmanından, birincil metinden değil. Ondalıklar teyit edilmemiş sayılmalı; **yön** güvenilir.

**Ama bu ailede bir istisna var ve önemli:** A22, kapalı yayıncıların etrafından dolaşıp **kendi ölçümünü üretti**. PyPI + npm + StarScout replikasyon CSV'leri üzerinden **4 bağımsız [D] ölçüm** — bu oturumdaki tüm ailelerin en güçlü birincil veri tabanı. Kaynak kapalıysa *veriyi kendin üret* taktiği burada tam karşılığını verdi ve V-kutusuna girmeyi hak ediyor (§9, V64).

**Protokol borcu:** Aşama 2 (antitez) A22 ve A24 için **koşulmadı** — A5'ten beri süregelen borç. İddia listeleri (§3.4, §5.4) antitez için hazır bırakıldı, saldırıya uğramadılar. Bu ailenin tüm hükümleri **⊨¬2** damgalıdır.

---

## 1 — Ailenin tek cümlelik bulgusu

> Teknoloji seçimi hakkında **ölçülmüş** olan şey neredeyse tümüyle *ekosistem sağlığı*dır (terk oranı, bakımcı yoğunlaşması, bağımlılık gecikmesi, yıldız sahteciliği) — yani **seçtiğin şeyin hayatta kalıp kalmayacağı**. **Ölçülmemiş** olan ise neredeyse tümüyle *karar verme yöntemi*dir (innovation token, Technology Radar, ATAM, ADR, "boring technology") — yani **nasıl seçmen gerektiği**.

Pratikte dolaşan kuralların **hiçbirinin sonucu ölçülmemiştir.** Buna karşılık:
- Herkesin baktığı sinyal (**yıldız**) ölçülmüş şekilde **bozuktur**,
- Kimsenin öncelikli bakmadığı sinyal (**indirme / bağımlı sayısı**) ölçülmüş şekilde **güçlüdür**.

Bu asimetri, aşağıdaki tüm tasarım önerilerinin dayanağıdır.

---

## 2 — A22 · Kendi ölçtüğümüz veri [D]

Bu bölümdeki dört tablo bu oturumun **en yüksek kanıt değerli** malzemesidir: birincil kaynağa erişim olmadan, ham registry verisinden hesaplandı.

### 2.1 PyPI terk oranı — uniform rastgele örneklem

Yöntem: PyPI tam paket indeksi çekildi (**857.893 proje**, 2026-07-26), seed'li rastgele 500 paket örneklendi, her biri için `pypi.org/pypi/<ad>/json`'dan tüm sürüm dosyalarının yükleme tarihleri toplandı. **n = 478 geçerli.**

| Ölçüt | Rastgele PyPI paketi |
|---|---|
| Son sürüm > 1 yıl önce | **69,0%** |
| Son sürüm > 2 yıl önce | **54,2%** (±4,5 pp, %95 GA) |
| Son sürüm > 3 yıl önce | 43,9% |
| Son sürüm > 5 yıl önce | 26,6% |
| **Medyan "son sürümden beri geçen süre"** | **856 gün (2,3 yıl)** |
| Sadece 1 sürümü olan | 30,8% |
| 1 sürüm VE >2 yıl durgun ("ölü doğmuş") | 17,4% |

→ **Rastgele bir PyPI paketi, medyan olarak 2,3 yıldır terk edilmiştir.** "PyPI'da paket var" bilgisi tek başına **neredeyse sıfır bilgi taşır**.

### 2.2 Popülerlik ↔ bakım gradyanı — PyPI, 4 katman × n=500

Kaynak: `hugovk/top-pypi-packages` (ClickHouse tabanlı resmi indirme sayıları, 15.000 satır).

| İndirme sırası | >1 yıl durgun | >2 yıl durgun | >3 yıl durgun | Medyan gün | Medyan sürüm sayısı |
|---|---|---|---|---|---|
| 1–500 | 17,6% | **8,6%** | 4,4% | 63 | 59,5 |
| 2.000–2.500 | 28,4% | 15,2% | 10,6% | 128 | 33,5 |
| 7.000–7.500 | 44,4% | 31,4% | 23,4% | 262 | 18 |
| 14.500–15.000 | 43,2% | 35,2% | 26,4% | 237 | 18 |
| *rastgele (sıralamasız)* | *69,0%* | *54,2%* | *43,9%* | *856* | *3* |

→ **Monotonik ve çok güçlü gradyan.** İndirme sayısı bakım aktifliğini *gerçekten* öngörüyor: en üst 500'de terk oranı rastgele pakete göre **6,3 kat** düşük.

### 2.3 npm terk + bakımcı yoğunlaşması — 220.469 paket

Yöntem: npm registry search API, 374 sorgu; her kayıt `dependents`, `maintainers`, son yayın tarihi içeriyor. Bağımlı sayısına göre katmanlandı.

| Katman | bakımcı = 1 | bakımcı ≤ 2 | >1 yıl durgun | >2 yıl durgun | Medyan gün |
|---|---|---|---|---|---|
| En çok bağımlısı olan 100 | **29,0%** | 51,0% | 25,0% | 16,0% | 76 |
| En çok bağımlısı olan 1.000 | **41,3%** | 63,8% | 47,0% | **35,8%** | 297 |
| En çok bağımlısı olan 10.000 | 49,9% | 68,6% | 56,6% | 46,2% | 584 |
| Toplanan tümü (220k) | **77,7%** | 86,1% | 63,2% | 54,4% | 824 |

En çok bağımlısı olan **1.000 paketin %17,8'i hem tek bakımcılı hem >2 yıl durgun.**

Somut: `lodash` 197.330 bağımlı / 1 bakımcı · `axios` 178.615 / 1 · `chalk` 158.494 / 1 · `mkdirp` 23.714 / 1 / 2023-04 · **`colors` 22.079 / 1 / 2019-09** · `buffer` 10.507 / 1 / 2020-11

**▲ KAVEAT (ajanın kendi dürüstlük notu, aynen taşınıyor):** npm `maintainers` alanı *yayın hesabı* sayar, **insan sayısı değil**. `@types/node` (1 bakımcı) aslında bir bot hesabıdır; org sahipli paketlerde ekip üyeleri görünmez. Bu sayı bus factor'ı değil, **yayın-yetkisi yoğunlaşmasını** ölçer — tedarik zinciri riski için doğru metrik, "kaç kişi bu kodu biliyor" için **değil**.

### 2.4 Yıldız manipülasyonu — replikasyon verisinden hesaplandı

Kaynak: He ve ark. StarScout replikasyon deposu, 250101 kesim tarihli ham CSV'ler; sayım ajan tarafından yapıldı.

- Düşük-aktivite sezgiseli: **4.904 depo, 1.031.443 şüpheli yıldız**
- Lockstep (eşzamanlı küme) sezgiseli: **8.894 depo, 2.157.864 şüpheli yıldız**
- Birleşim: **13.508 depo**
- Lockstep'le işaretlenen depoların **%89,5'inde yıldızların ≥%50'si sahte**; **%81,4'ünde ≥%90'ı sahte**
- Düşük-aktivite ile işaretlenenlerin **3.672'sinin toplam ≥1.000 yıldızı var** → küçük spam depoları değil, **"başarılı görünen" projeler**

Somut: `HKUDS/LightRAG` 10.956 → **7.596 (%69)** · `ComposioHQ/composio` 15.088 → 6.759 (%45) · `yangchris11/samurai` 5.746 → **5.365 (%93)** · `NirDiamant/RAG_Techniques` 9.457 → 4.943 (%52) · `localsend/localsend` 54.133 → 6.901

→ **Bir AI/LLM deposunun yıldızının üçte ikisinin satın alınmış olabilmesi, yıldızı seçim kriteri olarak kullanılamaz kılar.**

Yayımlanmış hali (He, Yang, Burckhardt, Kapravelos, Vasilescu, Kästner — ICSE 2026): 2019-07–2024-12 arası **~6 milyon şüpheli sahte yıldız / 15.835 depo**; kampanyalar 2024'te **iki büyüklük mertebesi** büyüdü; **2024 Temmuz zirvesinde yıldız aktivitesi olan tüm depoların %16'sı** bir kampanyayla ilişkili. GitHub, işaretlenen depoların ~%91'ini ve şüpheli hesapların %62'sini Ekim 2024'e dek sildi.

*Not (çelişki değil, sürüm farkı): makalenin ilk sürümü "4,5 milyon", yayımlanan sürümü "6 milyon" der. Dolaşımdaki iki rakamın kaynağı budur.*

---

## 3 — A22 · ÖLÇÜLMÜŞ vs FOLKLOR

### 3.1 ÖLÇÜLMÜŞ (rakam ve yöntem var)

| # | İddia | Rakam | Kanıt |
|---|---|---|---|
| M1 | Rastgele PyPI paketi terk edilmiştir | %54,2 >2 yıl durgun; medyan 856 gün | **[D] kendi ölçümümüz**, n=478, ±4,5pp |
| M2 | İndirme popülerliği bakım aktifliğini öngörür | %8,6 (top 500) → %54,2 (rastgele), monotonik | **[D] kendi ölçümümüz**, 4×500 |
| M3 | Kritik npm paketlerinde yayın yetkisi tek hesapta | Top-1000'in %41,3'ü tek bakımcı | **[D] kendi ölçümümüz**, 220k paket |
| M4 | Kritik paketlerin bir kısmı hem tek-bakımcılı hem durgun | Top-1000'in %17,8'i | **[D] kendi ölçümümüz** |
| M5 | Az sayıda hesap tüm ekosisteme erişir | <100 bakımcı → npm'in %50'si | [K] Zimmermann, USENIX Sec'19 |
| M6 | Bus factor tipik olarak çok düşük | %65'inde ≤2; %46'sında =1 | [K] Avelino / Ricca |
| M7 | Yaygın paketler de terk ediliyor, kullanıcı tepki vermiyor | ~%15'i 6 yılda terk; çoğu alt-proje değiştirmiyor | [K] Miller, ICSE'25 |
| M8 | Deprecated bağımlılık kullanımı yaygın | İstemcilerin %27'si doğrudan, %54'ü geçişli | [K] Cogo |
| M9 | Bağımlılık gecikmesi nicelleştirilebilir | medyan 106 gün / (0 major, 1 minor, 2 patch) | [K] Zerouali, 500k paket |
| M10 | GitHub yıldızı endüstriyel ölçekte sahte üretilebiliyor | ~6M şüpheli / 15.835 depo; zirvede %16 | **[D] ham veri** + [K] ICSE'26 |
| M11 | İşaretlenen depoların çoğunda yıldızın çoğu sahte | %81,4'ünde ≥%90 sahte | **[D] kendi hesabımız** |
| M12 | Yıldız ↛ kod kalitesi | Anlamlı korelasyon yok; sürücüler tanıtım/trend | [K] Borges & Valente |
| M13 | Dil seçiminin hataya etkisi ya yok ya çok küçük | 11 dilden yalnız 4'ü anlamlı, etki "son derece küçük" | [K] Berger, TOPLAS'19 |
| M14 | Dil çeşitliliği hata eğilimini artırır | 628 proje / 17 dil, pozitif ilişki | [K] Kochhar (M13 uyarısı geçerli) |
| M15 | Mimari borç kod borcundan hızlı faiz biriktirir | 3–5 kat; borcun %44,2'si pozitif faizli | [K] SATD literatürü |
| M16 | Gevşek bağlı mimari teslim başarımını öngörür | Çok yıllı DORA modellemesi | [K] DORA / Accelerate |
| M17 | Kütüphane göçü kaliteyi genelde iyileştirir | 57.447 proje; coupling↓ cohesion↑ | [K] arXiv 1907.07724 |
| M18 | ADR pratiği pilot sonrası terk ediliyor | 921 deponun ~%50'sinde <5 kayıt | [K] Buchgeher |
| M19 | Fikirlerin çoğu hedeflediği metriği iyileştirmez | ~1/3 pozitif; başarısızlık %70–90 | [K] Kohavi, on binlerce deney |

### 3.2 FOLKLOR (ölçümü yok — ama ölçülmüş gibi dolaşıyor)

| # | Dolaşan iddia | Durum |
|---|---|---|
| F1 | **"Her şirketin ~3 innovation token'ı vardır"** | **Tamamen ölçülmemiş.** Sayı retorik; kalibrasyonu yok. |
| F2 | **"Boring technology seç" → daha iyi sonuç** | **Ölçülmemiş.** Sonuç değişkeni hiç tanımlanmamış; "boring" tanımı post-hoc ayarlanabildiği için **yanlışlanabilir değil**. |
| F3 | "Yeni teknoloji = yüksek operasyonel yük" | Ölçülmemiş stereotip (karşı-tez de ölçülmemiş). |
| F4 | Technology Radar halkaları isabetlidir | **Öngörü doğruluğu hiç yayımlanmadı.** Retrospektif yok. |
| F5 | ATAM mimari kararları iyileştirir | **Kontrollü çalışma yok.** Sadece uygulama vakaları. |
| F6 | ISO/IEC 25010 kalite öngörür | Taksonomi; alt-karakteristik→metrik eşlemesi standartta yok. |
| F7 | ADR "daha iyi karar" sağlar | **Ölçüm yok.** Ölçülenler yalnız benimseme ve anlaşılırlık. |
| F8 | "Lock-in pahalıdır" | Varsayılmış. Alanın kendi itirafı: çok az kurum switching cost ölçüyor. |
| F9 | **"CNCF 2025: %42'si monolite dönüyor"** | **Birincil kaynakta doğrulanamadı.** Yalnız içerik-çiftliği sitelerinde. **KULLANILMAYACAK.** |
| F10 | "Gartner 2025: %60'ı mikroservisten pişman" | Doğrulanamadı; tek kaynak Medium. |
| F11 | "Mikroservis göçlerinin %73'ü başarısız" | Doğrulanamadı. |
| F12 | "O'Reilly 2025: %62'si ilk 12 ayda ROI sorunu" | Doğrulanamadı. |
| F13 | "Teknik borç: %23 hız↓, %31 defect↑, %287 ROI, 4,7 ay başabaş" | Doğrulanamadı; içerik-çiftliği izlenimi. **KULLANILMAYACAK.** |
| F14 | "Büyük yeniden yazımların %X'i başarısız" | **Sağlam rakam yok.** Kaynakların itirafı: "rakam yayımlayan taraf bir şey satıyor." |
| F15 | "COBOL göçlerinin %67'si başarısız" | Doğrulanamadı. |
| F16 | YAGNI'nin maliyet modeli | Muhakeme; "%30-50 hiç kullanılmaz" danışmanlık öz-beyanı. |
| F17 | **"Rakip/alternatif sayısına bak" heuristiği** | **Hiçbir ölçüm yok.** Bu kriter üzerine literatür bulunamadı. |
| F18 | Küçük takım monolit kullanmalı | Ölçülmemiş; mevcut tek kohort çalışması **ters yönde** sonuç veriyor. |

### 3.3 ▲ Hakem müdahalesi — üç işaret

**▲1 — Amiral gemisi çöktü [X].** Ray, Posnett, Devanbu, Filkov (FSE 2014 / CACM 2017), 729 GitHub projesi: 11 dil ↔ hata yoğunluğu anlamlı ilişki. Berger ve ark. (TOPLAS 2019) bağımsız yeniden-analizde **yalnızca kısmen** tekrarlayabildi (eksik kod, dil sınıflandırma hataları); çoklu hipotez düzeltmesi sonrası **yalnız 4 dil anlamlı kaldı, etki büyüklüğü "son derece küçük"**. Orijinal yazarlar çürütme, Berger ekibi karşı-çürütme yayımladı; **tartışma kapanmadı.**
→ *Bu ailenin en önemli tek bulgusu.* "Hangi teknolojiyi seçtiğin ölçülebilir şekilde kaliteyi etkiler" iddiasının en çok atıf alan kanıtı yeniden analizde **büyük ölçüde buharlaştı**. Aynı metodolojik kırılganlık M14 (Kochhar) için de geçerli — aynı veri kaynağı ailesi, aynı sınıf regresyon.

**▲2 — "Boring technology" yanlışlanabilir değil.** Tezin kendi savunucularından gelen itiraf ("boring bir liste değil kültür meselesi; neyin sıkıcı sayıldığı ekibin beceri setine göre değişir") tezi **test edilemez** hale getiriyor: tanım sonuca göre ayarlanabiliyorsa hipotez değildir. Epistemolojik olarak kritik kusur — F2'nin folklor sayılmasının gerekçesi budur, "kanıt bulunamadı" değil.

**▲3 — Ölçek folkloru ters yönde ölçülmüş [X].** ICSME 2023 registered report + dergi sürümü, kohort çalışması: baştan mikroservis kullanan GitHub projeleri ile benzer monolitik projeler karşılaştırıldı; sonuç **mikroservislerin geliştirme hızını iyileştirdiğini doğruladı**. Kohort açık kaynak projelerdir, **tek kişilik kişisel sisteme genellenmesi şüphelidir** — ama F18 folklorunun ölçümle *desteklenmediğini* göstermeye yeter. Aynı zamanda A24 bulgu 40 (hakemli literatürde mikroservisten monolite dönen **dört** belgelenmiş vaka: Istio kontrol düzlemi, Amazon Prime Video izleme servisi, Segment, InVision — dördünde de gerekçe **maliyet**) ters yönü destekliyor. **İki yön de ölçülmüş, ikisi de zayıf → bu eksende karar verecek kanıt yok.**

### 3.4 A22 iddia listesi (antitez için hazır, **⊨¬2**)

1. "Choose boring technology" ve innovation token, ölçülmemiş pratisyen tezleridir; "boring" tanımı post-hoc ayarlanabildiği için tez yanlışlanabilir değildir.
2. Teknoloji seçim çerçevelerinin (ADR, Technology Radar, ATAM, ISO 25010) hiçbirinin kendi faydası ölçülmemiştir; ölçülen tek şey benimseme oranlarıdır.
3. GitHub yıldızı seçim kriteri olarak kullanılamaz: endüstriyel ölçekte sahte üretilir, kod kalitesiyle korelasyonu yoktur.
4. İndirme/bağımlı sayısı, yıldızın aksine, bakım aktifliğini güçlü ve monotonik biçimde öngörür.
5. Rastgele bir açık kaynak paketi terk edilmiştir; terk edilmemişlik istisnadır, kural değildir.
6. Yaygın kullanılan paketlerin büyük kısmında yayın yetkisi tek hesapta yoğunlaşmıştır; bu, ölçek büyüdükçe azalmaz, yalnız en tepede azalır.
7. Teknoloji seçiminin sonuca etkisine dair en çok atıf alan ampirik kanıt, bağımsız yeniden analizde büyük ölçüde geçersizleşmiştir.
8. Ölçek-bağımlı folklorun (mikroservis/monolit) ölçülmüş hali, folklorun tersi yönde sonuç vermektedir.
9. Teknoloji seçimi tartışmasında dolaşan yüzde rakamlarının kayda değer bir kısmı birincil kaynakta doğrulanamayan, içerik-çiftliği kökenli uydurmalardır.

---

## 4 — A22 · Bulunamayanlar (kanıt boşlukları)

1. **"Innovation token" kavramının herhangi bir ampirik operasyonelleştirmesi.** Ne token sayısını kalibre eden, ne token harcamasıyla sonucu ilişkilendiren tek çalışma. Tez 2015'ten beri dolaşıyor ve **11 yılda hiç test edilmemiş.**
2. **"Boring technology seçen projeler daha iyi sonuç verdi mi"** sorusunu soran hiçbir çalışma. Teknoloji yaşı/olgunluğu ↔ proje sonucu ilişkisini yazılım bağlamında ölçen çalışma yok (bulunanlar inşaat/ulaştırma/patent alanında — transfer etmez).
3. **Technology Radar'ın retrospektif isabeti.** "Adopt'a alınan blip'ler 5 yıl sonra ne oldu" analizi ne ThoughtWorks'te ne üçüncü tarafta var.
4. **ATAM'ın kontrollü değerlendirmesi.** Uygulayan vs uygulamayan proje karşılaştırması yok.
5. **ADR'lerde gözlenmiş-sonuç alanı.** Ne 13 şablonda var, ne literatürde "kararlar sonradan doğru çıktı mı" ölçülmüş. → **Bu boşluk hem pratikte hem akademide açık; oturumun ADR bulgusuyla birleşince özgün katkı alanı.** (§7 M3 buradan doğuyor.)
6. **"Rakip/alternatif sayısı" kriterinin ölçümü.** Bu heuristiği inceleyen hiçbir çalışma yok.
7. **Lock-in'in nicel bedeli.** Switching cost'u *fiilen* ölçen (tahmin/anket değil) çalışma yok.
8. **Rewrite başarısızlık oranının güvenilir tahmini.** Sadece vaka anekdotları ve taraflı sektör rakamları.
9. **Tek kişilik ölçekte teknoloji seçimi.** Tüm ampirik literatür ya ekosistem ölçeğinde ya kurumsal takım ölçeğinde. Solo geliştirici / kişisel sistem bağlamına doğrudan konuşan **hiçbir ölçüm yok** — **bu ailedeki en büyük kanıt boşluğu, ve Salih'in tam olarak bulunduğu yer.**

---

## 5 — A24 · Karar-vermeyi öğrenme: ortam geçerliliği

### 5.1 Çekirdek — mimari "kötü" bir öğrenme ortamıdır

**[K] Kahneman & Klein (2009, *Am. Psychologist* 64(6):515-526):** sezgisel uzmanlık **iki koşul birlikte** sağlanınca güvenilir — (a) ortam geçerli ipuçları barındıracak kadar **düzenli**, (b) uzman bu düzenlilikleri **hızlı ve belirsizlik içermeyen geri bildirimle** uzun süre öğrenmiş. Biri düşerse "kendinden emin sezgi **sistematik hataya** döner". Yüksek geçerlilikli ortam **gerek şart, yeter şart değil**.

**[K] Hogarth, Lejarraga & Soyer (2015):** "kind" vs "wicked" öğrenme ortamları. Wicked = sonuçların eylemlerle korelasyonu belirsiz/aldatıcı/yok, geri bildirim eksik veya yanıltıcı. Öneri: kişi hangi ortamda pasif öğrendiğini **seçerek** sezgisini eğitebilir.

**[K][X-boşluk] Mimari kararların bu ölçütü karşılayıp karşılamadığını doğrudan ölçen çalışma BULUNAMADI.** Dolaylı kanıtlar ortamı **kötü** tarafa koyuyor:
- Mimari teknik borç **gecikmeli** tezahür ediyor: "büyük ve uzun ömürlü sistemler ATD'den muzdarip; küçük ve kısa ömürlüler ATD gerçek bir sorun olmadan ölüyor" → karar ile sonucun görünmesi arasındaki gecikme **sistem ömrü mertebesinde**.
- Geri bildirim geldiğinde bile kirli: **sonuç yanlılığı** (Baron & Hershey 1988) 2023 replikasyonunda **orijinalden güçlü** çıktı — orijinal d = .21–.53; replikasyon **d = .77 [.62,.93] → 1.1 [.94,1.26]** — katılımcılar "sonuca bakmamalıyım" **dedikleri halde**.

**▲ Hakem notu:** A24 ajanı burada dürüst bir sınır çizdi ve bu sınır korunuyor — *"bulgu 4'teki argüman **benim bileşimim**, literatür bulgusu değil."* Kahneman-Klein ölçütünü yazılım mühendisliğine formel uygulayan tek şey blog düzeyinde yorum. Yani **"mimari kötü öğrenme ortamıdır" hükmü çıkarım, ölçüm değil** — bu raporun en çok yaslandığı önerme aynı zamanda en az doğrudan desteklenen önermesidir. Kayda geçer.

**[K] Deneyim ≠ uzmanlık, geri bildirim zayıfsa.** Choudhry ve ark. (2005, *Annals of Internal Medicine*) sistematik derlemesi: **62 değerlendirmenin 32'si (%52)** hekimde yıl arttıkça performansın **düştüğünü**, 13'ü (%21) ilişkisizlik bildirdi; yalnız **1'i (%2)** tüm çıktılarda artış buldu.

**[K] Yazılıma özgü paralel:** mesleki yıl programcı performansını **kötü** yordar; "sanayide kazanılan deneyimin kalite ve üretkenlik üzerinde hiçbir etkisi görünmüyor, akademide kazanılanın olumlu etkisi var". Öz-değerlendirme de genel olarak performansla korele değil.

### 5.2 Deliberate practice — kanıt durumu zayıf

**[X] Macnamara, Hambrick & Oswald (2014, *Psych. Science*)** meta-analizi: kasıtlı pratik varyansın **oyunlarda %26, müzikte %21, sporda %18, eğitimde %4, mesleklerde <%1**'ini açıklıyor. **Meslekler — yazılımın ait olduğu kategori — en düşük dilim.**
*▲ Düzeltme: görev emrinde verdiğim "%21 oyun / %18 müzik" rakamları kaymıştı; ajan düzeltti, doğrusu yukarıdaki sıralamadır.*

**[X] Macnamara & Maitra (2019, *R. Soc. Open Sci.* 6:190327):** Ericsson, Krampe & Tesch-Römer (1993) kemancı çalışmasının çift-kör replikasyonu **çekirdek bulguyu tekrarlamadı**; etki büyüklüğü belirgin küçük. "Öğretmen-tasarımlı pratik" yalnız-pratikten **daha fazla varyans açıklamadı** — DP'nin teorik tanımı operasyonel tanımından iyi çalışmadı. Ericsson tarafı 2020'de karşı yanıt yazdı; **tartışma kapanmadı → [X]**.

**[K][BOŞLUK] Yazılım mühendisliğine özgü, DP'nin performans varyansındaki payını ölçen çalışma BULUNAMADI.**

### 5.3 Vaka okuma, kalibrasyon, çapa — mekanizma kanıtları

| Mekanizma | Bulgu | Etiket |
|---|---|---|
| **Vaka sayısı** | Gick & Holyoak: kaynak analog yokken çözüm ~%10; **tek** analogla ~%30; ipucuyla ~%80. Şema tümevarımı **iki vakanın karşılaştırılmasıyla** oluşuyor. **Tek vaka okumak neredeyse transfer üretmiyor.** | [K] |
| **Tekrar ziyaret** | Spiro, Bilişsel Esneklik: kötü-yapılandırılmış alanlarda aynı materyalin **farklı zamanlarda, yeniden düzenlenmiş bağlamlarda, farklı amaçlarla** tekrar ziyareti şart. Tek-geçişli müfredat tanım gereği yetersiz. | [K] |
| **Başarısızlık > başarı** | Madsen & Desai (2010, *AMJ*), yörünge fırlatma: kuruluşlar başarısızlıktan başarıdan **daha fazla** öğreniyor ve **başarısızlık bilgisi daha yavaş değer kaybediyor** ("başarıdan gelen bilgi uçucu, başarısızlıktan gelen yıllarca kalıyor"). | [K] |
| **Ama postmortem sahada çalışmıyor** | Postmortem "önerilen yöntem" olmasına rağmen **tutarlı uygulanmıyor**; ankette az kişi memnun; **birden fazla postmortem'in çıktısını birlikte analiz eden neredeyse yok**. | [K] |
| **Öz-açıklama** | Bisra ve ark. (2018, *Educ. Psych. Review*): 64 rapor / 69 etki / 5.917 katılımcı, rastgele etkiler **g = 0.55**. Çok çeşitli koşulda çalışıyor. | [K] |
| **Yazılımda kalibrasyon tabanı** | Jørgensen, Teigen & Moløkken (2004): profesyonellerin **%90 güvenli** min-maks efor aralıkları gerçek eforu yalnız **%60-70** oranında içeriyor; projeler ort. **%30-40 fazla** efor harcıyor. | [K] |
| **▲ Ailenin en operasyonel bulgusu** | Jørgensen & Gruschke (2009, *IEEE TSE* 35(3)): belirsizlik değerlendirmesinin iyileşmesi için **gerek koşul, açıkça formüle edilmiş bir strateji kullanılması**; **sezgi-temelli** değerlendirme **hiç ya da çok az öğrenme** üretiyor. Uzmanlar geçmiş dersleri nadiren kullanıyor; kötü formüle edilmiş geçmiş tavsiye **zararlı** olabiliyor. → *Yapılandırılmış yansıtma tek başına yetmiyor; **yazılı, açık kural** şart.* | [K] |
| **Kalibrasyon eğitimi işe yarar…** | Tetlock/Mellers GJP: eğitim 3. yılda **%6**, 4. yılda **%7** skor iyileşmesi; aşırı-güveni azaltarak kalibrasyon ve çözünürlüğü iyileştiriyor. **Gerçek ama mütevazı.** Alpert & Raiffa: %98 GA ıskalama oranı **tek pratik turundan sonra %41 → %23**. | [K] |
| **…ama koşulsuz değil [X]** | Kelly ve ark. (2024): 70 istihbarat analisti, ticari kalibrasyon kursu — iyileşme var **ama etki göreve bağlı**. Martin (2025): "Pratik skorlama kuralıyla kalibrasyon geri bildirimi güveni kalibre **etmiyor**." → "tahmin + kayıt + skorlama otomatik işler" iddiası **çelişkili kanıta sahip**. | [X] |
| **Geri bildirim türü ayrışıyor** | Performans geri bildirimi **aşırı-güveni** azaltıyor; çevresel geri bildirim **ayırt ediciliği** iyileştiriyor. İkisi farklı şeyi düzeltiyor. | [K] |
| **Dış görüş** | Flyvbjerg, Holm & Buhl: 20 ülke / 5 kıta / 258 altyapı projesi, **%90'ı bütçe aşımı** (demiryolu ort. %28, köprü-tünel %34, yol %20). APA 2005'te referans sınıfı tahminini resmen tavsiye etti. | [K] |
| **Premortem** | Mitchell, Russo & Pennington (1989): olayın **gerçekleşmiş olduğunu varsaymak** gelecekteki sonuçların nedenlerini doğru belirlemeyi **%30** artırıyor; **eylem-temelli** gerekçe sayısını ikiye katlıyor. | [K] |
| **Çapalama** | Debiasing atölye deneyi: 16 öğrenci + 20 uygulayıcı; ayrıca 44 y.lisans / 12 takım — **12 takımın 10'unda akıl yürütme iyileşti**. Çapalama mimarların **ilk buldukları çözümü bilinçsizce yeğlemesine** yol açıyor. | [K] |
| **Yetinmecilik** | Tang & van Vliet: tasarımcılar sezgisel ve rasyonel stratejileri **karışık ve sırayla** kullanıyor; çoğu denek **karar vermeden önce yalnız birkaç gerekçe** üretiyor → **satisficing**. | [K] |
| **Uzman ↔ acemi** | Adelson & Soloway: uzmanların çözüm geliştirmesi **sistematik ve dengeli**; dengesiz gelişim **zihinsel simülasyonu imkânsız** kılıyor. Guindon: uzmanlık işareti **enine-öncelikliden fırsatçı moda geçiş yeteneği** — yani uzmanlık tek sürece bağlılık değil, **süreç seçimi**. Genel: uzmanlar **davranış ve işlev** düzeyinde, acemiler **yapısal/yüzeysel** düzeyde çalışıyor. | [K] |
| **Ters yön — teşvik yapısı** | Résumé-Driven Development, 591 profesyonel: **%60** işe alan trendlerin ilan içeriğini etkilediğini kabul; **%82** trend teknoloji kullanmanın kendisini çekici kıldığına inanıyor. **Ama %39** yerleşik teknolojide deneyimliyi yeğliyor, yalnız **%20** trend bileni; ve yalnız **%42'si** yeni teknolojinin kendisini **daha iyi geliştirici** yaptığına inanıyor. → **Teşvik yapısı ile fayda inancı ayrışıyor.** | [K] |
| **Kontrol** | Yerleşik pratikte seçim kriteri daha sağlıklı: geliştiriciler teknolojiyi **sistem gereksinimleri ve ekipte hâlihazırda var olan beceriler** temelinde seçiyor. | [K] |

**▲ Hakem müdahalesi — vaka-temelli öğrenme etki büyüklükleri indirimli okunuyor [X].** Tıpta CBL meta-analizleri **şüpheli derecede büyük** etkiler bildiriyor (klinik akıl yürütme SMD = 1.78 [1.46, 2.11]; 16 RCT / 956 öğrenci ile teorik bilgi MD = 5.21). Bu meta-analizlerin çoğu **tek ülke/tek eğitim kültürü** kaynaklı ve etki büyüklükleri eğitim literatürü normlarının çok üstünde → **yayın yanlılığı şüphesiyle indirimli.** Aynı şekilde Cook ve ark. (2011, *JAMA*) simülasyon d değerleri (bilgi d=1.20, süreç d=1.09, hasta çıktısı d=0.50) **"müdahale yok" karşılaştırmasına** dayanıyor — bu tasarım etkiyi **sistematik şişirir**; aktif kontrolle kıyas çok daha küçüktür.

**▲ Ters bulgu korunuyor [X].** PBL meta-analizleri **çıktı türüne göre işaret değiştiriyor**: Dochy ve ark. (2003) becerilerde sağlam pozitif, **bilgide anlamlı negatif**; ancak elde edilen bilginin **kalıcılığı** daha yüksek. Strobel & van Barneveld: uzun-vadeli kalıcılık ve beceri ölçümünde üstün, **kısa-vadeli bilgi ölçümünde geride**. → *Bu, ana atlasın Model B ("önce dene, sonra oku") kararıyla aynı yöne çıkıyor* — **ama aynı zamanda bir uyarı:** yanlış çıktı ölçülürse vaka/problem temelli yöntem geleneksel yöntemden **geride** görünür. DONE tanımının ölçtüğü şeyi yanlış seçmesi gerçek bir risk.

**▲ Hukuk vaka yöntemi varsayımı düşüyor.** "Hukukta vaka/Sokratik yöntem kanıtlı bir modeldir" varsayımı **desteklenmiyor**: etkililik araştırması ağırlıkla işletme alanında; uygulayıcı avukatlar yöntemin pratiğe hazırlamada etkili olmadığı görüşünde; yöntem son on yılda **gözden düşmüş**. Fikir kutusundaki "hukuksal layer" fikri (talep (g)) bu bulguyla birlikte okunmalı — hukuk *muhakeme biçimi* olarak alınabilir, *öğretim modeli* olarak alınamaz.

### 5.4 A24 iddia listesi (antitez için hazır, **⊨¬2**)

1. Yazılım mimarisi kararları Kahneman-Klein anlamında **geçersiz** bir öğrenme ortamıdır; bu alanda deneyimden doğal sezgi gelişmez.
2. Mimaride yıl sayısı uzmanlık üretmez; geri bildirim mimarisi düzeltilmeden geçen yıllar performansı **düşürebilir**.
3. Deliberate practice mesleki alanlarda varyansın %1'inden azını açıklar; yazılım mimarisi için ölçülmüş bir DP tahmini yoktur.
4. Vaka okumanın öğretici olması için **en az iki zıt vakanın** karşılaştırılması gerekir; tek vaka okuma transfer üretmez.
5. Başarısızlık vakaları başarı vakalarından daha öğretici ve daha kalıcıdır.
6. Sonucu bilinen bir kararı okumak, sonuç yanlılığı nedeniyle süreç değerlendirmesini sistematik bozar; **sonuç kapatılmadan okuma öğretici değildir**.
7. Kalibrasyon skorlaması, **insan kolaylaştırıcı olmadan** yapılandırılmış yansıtmanın gerektirdiği nesnel performans verisini üretebilen tek pratik mekanizmadır.
8. Sezgi-temelli yansıtma öğrenme üretmez; öğrenme için **açıkça yazılmış bir karar kuralı** gereklidir.
9. Teknoloji seçiminde en büyük sistematik hata kaynağı bilgi eksikliği değil, **teşvik yapısıdır** (özgeçmiş güdümlü seçim + büyük-ölçek çözümünün transplantı).

---

## 6 — A23 · DS/ML asgari yığını

**KOŞUM SÜRÜYOR.** A23 ve alt-hatları (veri katmanı: polars/duckdb/parquet/dvc · kalite katmanı: ruff/mypy/pytest · deney takibi n=1 · yeniden üretilebilirlik ve notebook'lar · nbdev/jupytext/papermill · Parquet vs CSV ölçümü · MLflow ağrı noktaları · W&B ücretsiz katman ve gizlilik · ortam sabitleme kayması · manuel takip eşiği) hâlâ dönmedi.

**Bu bölüm bilerek boş bırakıldı.** İndiğinde bu dosyaya **§6 olarak eklenecek**, ayrı dosya açılmayacak — aile bütünlüğü korunur. Borç §8'de kayıtlı.

*Şu ana dek inen alt-hatlar (nbdev/jupytext/papermill · ortam sabitleme kayması · manuel takip eşiği) A23'ün kendi sentezinde toplanacağı için burada tekrarlanmadı — çift-kayıt riski.*

---

## 7 — m.37 · Üç model

**Karar sorusu:** JARVIS'te teknoloji/yığın seçimi hangi yöntemle yapılacak ve bu yöntem öğrenme hattına nasıl bağlanacak?

### Model A — Çerçeve benimseme (ADR + Technology Radar + ATAM alt kümesi)

Yerleşik endüstri çerçevelerinden bir alt küme alınır; her yığın kararı ADR olarak yazılır, altı ayda bir kendi Radar'ımız güncellenir.

- **Artı:** hazır şablon var (12+ şablon, doğrudan çekildi) · ortak sözlük kurar · benimseme kolay · CV'de tanınır.
- **Eksi:** **F4-F7 hepsi folklor** — bu çerçevelerin hiçbirinin *sonucu* ölçülmemiş. M18: 921 deponun **~%50'sinde 5'ten az kayıt** → pilot sonrası terk oranı yüksek, ve JARVIS zaten tek kişilik (terk riski daha da yüksek). Ölçülmemiş yöntemi benimsemek, **ölçüm önceliği (m.35) ile doğrudan çelişir**.
- **Maliyet:** düşük kurulum, orta sürdürme.

### Model B — Ekosistem-sağlığı eşiği (ölçülmüş vekil)

Karar *yöntemi* değil, karar *girdisi* standartlaştırılır. Her bağımlılık için üç sayı zorunlu: **indirme sırası** (top-500 içinde mi?), **son sürüm tarihi**, **bakımcı/yayın-yetkisi sayısı**. Yıldız **hiç bakılmaz** (M10-M12).

- **Artı:** dayandığı her şey **[D] ölçülmüş** (M1-M4, M10-M12). "Top-500'de kal" kuralı terk riskini **6,3 kat** düşürüyor — ölçülmüş bir eşik, retorik değil. Tek kişilik ölçekte uygulanabilir: üç sayı, üç API çağrısı. **F2'nin ("boring") ölçülmemiş halinin yerine geçen ölçülmüş vekil.**
- **Eksi:** *seçtiğin şeyin yaşayıp yaşamayacağını* ölçer, *doğru şeyi seçip seçmediğini* değil — §1'deki asimetrinin ölçülmüş yarısını alır, ölçülmemiş yarısını **boş bırakır**. Yenilikçi ama az kullanılan bir aracı sistematik olarak reddeder (yanlış-negatif; A22 kendisi bunun ölçülmediğini söylüyor). "Popüler olan doğrudur" kaymasına açık.
- **Maliyet:** düşük — üç sayı, script'lenebilir.

### Model C — Kapatılmış geri bildirim döngüsü (tahmin → yaz → aç → skorla)

Karar yöntemi **öğrenme mekanizmasıyla birleştirilir**. Her yığın kararında önce tahmin + olasılık yazılır, sonra kaynak/sonuç açılır, Brier skorlanır. A24 müfredatı (§7.1) bunun eğitim tarafı, ekosistem eşiği (Model B) girdi tarafı.

- **Artı:** mimarinin **kötü öğrenme ortamı** olma sorununu (§5.1) doğrudan hedefler — geri bildirim döngüsünü **yapay olarak kısaltır**. Jørgensen & Gruschke'nin gerek koşulunu (**yazılı açık strateji**) yapısal olarak sağlar. Brier skoru **insan kolaylaştırıcının yerini tutan tek nesnel metrik** — JARVIS'te insan kolaylaştırıcı yok, bu belirleyici. Model B'yi **içerir** (girdi olarak kullanır), dışlamaz.
- **Eksi:** kalibrasyon eğitiminin işe yaradığı **çelişkili kanıta sahip** [X] — Martin (2025) doğrudan reddediyor, Kelly (2024) "göreve bağlı" diyor. GJP'de bile kazanım **%6-7**, mütevazı. Sürtünme yüksek: her karar öncesi yazma zorunluluğu, küçük kararlarda **terk edilme riski** (M18'in ADR'de ölçtüğü tam bu).
- **Maliyet:** orta-yüksek sürdürme; kurulum düşük.

### ▲ Öneri: **Model C, Model B'yi girdi olarak alacak şekilde — ama sürtünme eşikli**

Gerekçe:
1. **m.35 (ölçüm önceliği) Model A'yı eliyor.** Ölçülmemiş çerçeve benimsemek, bu oturumun kendi bulgusuyla çelişir.
2. **Model B tek başına yetersiz ama vazgeçilmez.** §1'in asimetrisi: ölçülmüş yarıyı almamak için sebep yok, ama ölçülmemiş yarıyı boş bırakmak da kabul edilemez.
3. **Model C'nin zayıflığı dürüstçe kaydedilmeli:** kalibrasyon eğitiminin etkisi tartışmalı. **Ama alternatifi yok** — insan kolaylaştırıcı olmayan bir sistemde nesnel performans verisi üretebilen başka mekanizma bulunamadı (A24 boşluk #4-5). Yani bu, "en iyi kanıtlı seçenek" değil, **"tek uygulanabilir seçenek"** — fark önemli, kaydediliyor.
4. **Sürtünme eşiği zorunlu (M18 dersi).** ADR'lerin %50'si 5 kayıttan sonra terk edildiyse, tam-protokol her karara uygulanamaz. **Eşik önerisi:** yalnız *geri alması pahalı* kararlar (m.31 ölçek eşiğiyle aynı kesim — publish / para / kişisel veri / pahalı geri-alma / yön değişimi) tam Model C protokolüne girer; altı Model B'nin üç sayısıyla geçilir.

**Bu Katman 1 kararıdır (m.31: değer tercihi + yöntem kanonu). Salih imzası bekler.**

---

## 7.1 — A24 müfredatı · L7–L15 (öğrenme hattına ek)

*Ana atlasın L1–L6'sı stall vakasından türetilmişti; bu blok karar-verme hattıdır. Numaralandırma çakışmasın diye L7'den başlıyor.*

**Tasarımın tek cümlelik gerekçesi:** Mimari, geri bildirimi **yıllar mertebesinde gecikmiş** ve **sonuç yanlılığıyla kirlenmiş** kötü bir öğrenme ortamıdır (§5.1). Bu yüzden müfredat **konu öğretmez**; **yapay olarak kapatılmış geri bildirim döngüsü imal eder.** Tek mekanizma: **tahmin et → yaz → aç → skorla.** Bu tek mekanizma aynı anda üretken başarısızlığı, öz-açıklamayı (g=0.55), kalibrasyonu ve AAR'ın talep ettiği **nesnel performans verisini kolaylaştırıcı olmadan** sağlar.

**Değişmez kurallar (her oturumda geçerli):**
- **Yazmadan açma.** Kaynak/çözüm/sonuç açılmadan önce tahmin + gerekçe dosyaya yazılır.
- **Tek vaka yasak: her oturumda en az iki vaka karşılaştırılır.** Tek analog transferi ~%30'da bırakıyor; karşılaştırma şema üretiyor (Gick & Holyoak, Spiro).
- **Sonuç ayrı, süreç ayrı puanlanır.** Sonuç açılmadan önce süreç puanı verilir. (Sonuç yanlılığı d ≈ 0.8–1.1.)
- **Her oturum çıktısı "açıkça formüle edilmiş bir kural" içerir.** Sezgisel yansıtma öğrenme üretmiyor; yazılı strateji **gerek koşul** (Jørgensen & Gruschke).
- **Skorlama şüpheli → ikili ölçüm.** Kalibrasyon tek başına yeterli değil [X] → her oturum hem **Brier** hem **"kural transferi"** ile ölçülür.

| # | Oturum | İçerik | DONE (ölçülebilir) |
|---|---|---|---|
| **L7** | **Taban kalibrasyon** | 25 ikili teknoloji-seçimi önermesi (%50-100 güven) + 10 aralık tahmini (%90). Konu bilgisi değil, **kendi güven ayarı** ölçülür. | Brier skoru **sayı olarak** dosyada; %90 aralıklarının isabet oranı yazılı. Beklenen taban ≈ **%60-70**. Skorun iyi/kötü olması DONE'u etkilemez — **kaydedilmiş olması** DONE'dur. |
| **L8** | **Kör kata** | Gerçek bir sistemin **yalnız gereksinimleri** verilir (mimarisi gizli). Yığın kararı + gerekçe + 3 olasılıklı tahmin ("bu seçim X'te tıkanır: %p") yazılır. Sonra gerçek mimari açılır. | 1 kata artefaktı + 3 tahmin skorlanmış. **Ek ölçüt:** yazılan gerekçe sayısı — *yetinmecilik göstergesi*; 3'ten az gerekçeyle karar verildiyse işaretlenir. |
| **L9** | **Zıt vaka çifti** | Aynı problemde **ters** karar vermiş iki gerçek vaka (ör. mikroservise bölen ↔ monolite dönen sistemler — Istio, Prime Video, Segment, InVision). Ortak şema çıkarılır. | **≤5 koşul değişkeni** listesi — kararı çeviren eşikler. Doğrulama: **üçüncü, görülmemiş** vakaya uygulanır; tahmin önce yazılır. Şema 3. vakayı tutmuyorsa oturum **DONE değil**, revize edilir. |
| **L10** | **Karar arşivi (sonucu kapalı)** | ≥5 yıllık gerçek kararlar: PEP/RFC/ADR arşivleri. **Yalnız "Rationale + Alternatives" bölümü** okunur; kabul/red ve bugünkü durum **tahmin edilir**, sonra açılır. | ≥8 karar okundu, her biri için tahmin + olasılık kaydedildi, Brier hesaplandı. **Kritik ölçüt:** L7 tabanına göre **Brier deltası** raporlanır — kötüleşme de geçerli sonuçtur. |
| **L11** | **Başarısızlık serisi** | `danluu/post-mortems` içinden **tek kategoriden** 5 postmortem. Her biri okunmadan önce "bu kategoride kök neden ne olur" tahmini yazılır. (Başarısızlık bilgisi daha yavaş değer kaybediyor.) | "Başarısızlık modu → mimari önkoşul" tablosu, **≥10 satır**, her satırda URL. Her satır **mimariye atfedilebilir / operasyonel** diye etiketlenir; ayrım oranı raporlanır. |
| **L12** | **Süreç-sonuç ayrıştırma** | Kendi geçmiş 3 kararını, **sonuca bakmadan** süreç rubriğiyle puanla (alternatif sayısı · ödünleşim yazılı mı · geri-alma maliyeti düşünülmüş mü · varsayım yazılı mı). Sonra sonuca bak, yeniden puanla. | İki puan seti + fark tablosu. Ölçülen: **kendi sonuç yanlılığının büyüklüğü** (beklenen: sıfırdan farklı). Rubrik dosyası **kalıcı artefakt** olur. |
| **L13** | **Çapa kırma + premortem** | Güncel yığın kararına: (a) ilk aklına gelen çözümü yaz ve **kenara koy** (çapalama), (b) premortem — "6 ay sonra bu seçim battı, neden?" (+%30 neden), (c) hatırlatma kartı: **RDD kontrolü** + **büyük-ölçek transplantı kontrolü**. | **≥8 başarısızlık nedeni**, **eylem-temelli** ifadeyle. Bunlardan **≥2'si tasarımı fiilen değiştirdi** (diff/metin olarak görünür). Değiştirmediyse "**neden değiştirmedi**" yazılı. |
| **L14** | **Dış görüş / referans sınıfı** | Kendi proje türü için **≥5 karşılaştırılabilir gerçek proje** bul, süre/ekip/maliyet sayılarını topla, kendi tahminini **aralık** olarak dış görüşten üret. | 5 satırlık referans sınıfı tablosu (sayılar + URL) + kendi tahmininin **iç görüş ve dış görüş** iki versiyonu; **ikisinin farkı yazılı**. |
| **L15** | **Yeniden kalibrasyon + kapanış** | L7 ile **aynı formatta** yeni set (aynı sorular değil). | Brier deltası + %90 aralık isabet deltası. **Dürüstlük şartı:** iyileşme yoksa "**iyileşme yok**" yazılır — negatif sonuç müfredatın başarısızlığı değil, **ölçümün çalıştığının kanıtıdır**. |

**Kadans ve sıra:**
- L7 ve L15 **çerçeve** oturumlarıdır; aradakiler sıralanabilir, **ama L9 (zıt çift) L10'dan ÖNCE** gelmelidir — şema olmadan arşiv okumak **yüzeysel ipucu toplamaya** döner.
- **İskele düşürme:** L11'den sonra rubrik/hatırlatma kartı zorunlu olmaktan çıkar, isteğe bağlıya döner (uzmanlık tersine dönmesi **d=0.971** riskine karşı). Bu düşüşün **doğru zamanı ölçülmedi** — `[?]`.
- **Tekrar ziyaret:** Bilişsel esneklik gereği L9'un vaka çifti, L13'te **farklı amaçla yeniden okunur** — yeni vaka eklemeden.

**▲ Müfredatın kendi zayıflığı (ajanın beyanı, korunuyor):** L10 ve L11'in mimari karar kalitesini artırdığına dair **ölçülmüş kanıt yok**. Mekanizma gerekçesi sağlam (vaka sayısı, başarısızlık kalıcılığı, öz-açıklama g=0.55), **sonuç kanıtı yok**. Bu iki oturum müfredatın **en spekülatif** kısmıdır — ve DONE'ları bu yüzden "kavrayış" değil **artefakt sayısı** olarak tanımlandı.

**▲ İkinci zayıflık, bizim eklememiz:** L12'nin rubriği **kendi imalatımız** olmak zorunda — valide edilmiş bir mimari karar kalitesi rubriği literatürde **bulunamadı** (A24 boşluk #8). Yani L12 kendi ölçüm aracını da üretiyor; bu, ölçümün **kalibre edilmemiş** olduğu anlamına gelir. Damga: `[?]`.

---

## 8 — Açık borçlar

| # | Borç | Durum |
|---|---|---|
| B1 | **A23 (DS/ML asgari yığını) inmedi** — §6 boş | Koşum sürüyor; indiğinde bu dosyaya §6 olarak eklenecek |
| B2 | **Aşama 2 (antitez) A5–A27 için koşulmadı** | Uzun süreli protokol borcu; §3.4 ve §5.4 iddia listeleri hazır bekliyor |
| B3 | Akademik rakamların **hiçbiri birincil metinden değil** | Erişim açık bir oturumda teyit; öncelik: Macnamara 2014 yüzdeleri · Cook 2011 d değerleri · GJP %6-7 |
| B4 | `arxiv.org/html/...` **denenmedi** | Açık listede olmadığı için atlandı. Kısıt gevşerse **en yüksek getirili tek kanal** — debiasing deneyi, mikroservis issue çalışması, RDD hepsinin HTML sürümü var görünüyor |
| B5 | Mimari uzmanlıkta **protokol analizi güncel değil** | Adelson & Soloway (n=5), Guindon, Tang — 1984-2010, tek haneli/onlu denek. **Bulut/mikroservis/yönetilen hizmet çağında uzman-acemi protokol çalışması yok** |
| B6 | **Tek kişilik ölçekte teknoloji seçimi ölçümü yok** | Ailenin en büyük kanıt boşluğu; Salih'in tam bulunduğu yer. Kapatılamaz — **üretilebilir** (§9 V65) |
| B7 | Model C'nin **sürtünme eşiği** ölçülmedi | M18 dersinden türetildi ama eşiğin doğru yeri tahmin; L15'te ölçülebilir |

---

## 9 — Fikir kutusu adayları

- **V64 — "Kaynak kapalıysa veriyi üret."** A22, kapalı yayıncıların etrafından dolaşıp PyPI + npm + replikasyon CSV'lerinden **4 bağımsız [D] ölçüm** üretti. Bu, oturumun en güçlü birincil veri tabanı ve **taktik olarak tekrarlanabilir**: birincil kaynak kapalıysa → replikasyon deposu · registry API'si · ham veri CSV'si. Atlas brifinglerine **standart madde** olarak girmeye aday.
- **V65 — Kendi boşluğumuzu kendimiz doldurmak.** B6 (tek kişilik ölçekte seçim ölçümü yok) **literatürde kapatılamaz** ama JARVIS'te **üretilebilir**: L7–L15 zaten Brier skoru üretiyor. n=1 ama **ölçülmüş** n=1 — ve alan bunun *hiç* ölçülmediğini söylüyor. Özgün katkı alanı.
- **V66 — ADR'ye "gözlenmiş sonuç" alanı.** 13 şablonun hiçbirinde yok, literatürde de soru sorulmamış (A22 boşluk #5, A24 boşluk #3). Kendi ADR şablonumuza eklemek **hem pratik hem özgün**: karar anını değil, **kararın sonucunu** kayda geçirir. Model C'nin doğal artefaktı.
- **V67 — Yıldız yasağı.** M10-M12 gereği: JARVIS'te hiçbir kararda GitHub yıldızı **kriter olarak anılmaz**; yerine indirme sırası + son sürüm tarihi + bakımcı sayısı. Kural küçük, dayanağı [D]. Tüzüğe değil, KILAVUZ'a aday.

---

## 10 — Kapanış damgası

**Aile:** A22 ⊨S-değil (**⊨¬2**) · A24 ⊨S-değil (**⊨¬2**) · A23 **açık**
**Kanıt tabanı:** 4 × [D] kendi ölçümümüz (PyPI n=478 · PyPI 4×500 · npm 220.469 · StarScout ham CSV) · geri kalan tümü **[K]**, abstract katmanından
**Karar önerisi:** Model C (B içerilerek, sürtünme eşikli) — **Katman 1, Salih imzası bekler**
**Register:** teknik tek kayıt; insan-yüzü muadili **talep gereği üretilmedi**
