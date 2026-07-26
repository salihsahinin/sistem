# Tech Stack Atlası — seçim, öğrenme, ölçüm

*Kayıt: 2026-07-26 · Carvis (CC, yan-oturum m.41) · Talep: "öğrenme hattına tech stackleri ve sistemlerde projelerde tech stack oluşturmayı öğrenmem gerekiyor / araştır atlasları koş rapor yaz (sadece ai to ai)"*

**REGISTER BEYANI:** Salih açıkça **"(sadece ai to ai)"** dedi. Bu raporun insan-yüzü (`INSAN-*`) muadili **üretilmeyecek**; compiler formülü (`2026-07-26-compiler-formulu.md`) F8 gereği bu dosyaya uygulanmaz. Teknik kayıt tek kayıttır.
> **⚠️ BU BEYAN AŞILDI (2026-07-26, `cc/gorev-2026-07-26-1.md` §2).** Salih sonradan **iki insan-yüzü register** emri verdi: `INSAN-tech-stack.md` (kavrayış) + `SOZEL-tech-stack.md` (düz lojik). Yukarıdaki beyan **kronolojik olarak öncedir** ∧ yeni emirle geçersizleşmiştir. Silinmiyor (m.8), **üstü çiziliyor**. Teknik kayıt **hâlâ tek karar kaynağıdır**; insan-yüzü dosyalar karar kaynağı değildir.

> ## ⛔ DÜZELTME KAYDI — 2026-07-26 antitez turu *(teslim SONRASI eklendi)*
> Antitez **araçsız** koştu (`tool_uses = 0`) ⇒ tüm saldırı **modelin kendi eğitim bilgisinden** yapıldı. Bu ayrım hakemlikte uygulandı: **mantıksal saldırı → hüküm değiştirir · olgusal karşı-örnek → borç açar, hüküm değiştirmez.** Hakemlik: `raporlar/2026-07-26-antitez-hakemlik.md` §2.
>
> | Düzeltme | Nerede | Ne oldu |
> |---|---|---|
> | **K1** | §5.3 · §5.4 ④ | `tek vaka → transfer üretmez` → **transfer DÜŞÜK (~%30), sıfır DEĞİL** — kendi raporumuz zaten öyle diyordu |
> | **K5** ⭐ | §5.4 ⑥ | **Olumsuzlama kapsamı** düzeltildi ∧ parantezle sabitlendi — antitez cümleyi **ters okudu** |
> | **K6** | §5.4 ⑦ · §7 Model C | `tek pratik mekanizma` → **`bulunabilen tek`**; mimariye transferi `[?]` |
> | K2 | §6.9 ⑦ | `hiçbir koşum` → **hash-sırasına duyarlı kod yolu içeren** koşum |
> | K3 | §6.8 · §6.9 ⑨ | `DVC getirisi = 0` → **azalmış**; hüküm (ALINMAZ) değişmez, gerekçe düzelir |
> | K4 | §3.4 ④ | `güçlü öngörür` → **toplu düzeyde; paket-başına garanti değil** |
> | K7 | §6.8 polars | Hüküm korunur; **şema-katılığı ∧ null-semantiği ekseni ÖLÇÜLMEDİ** borcu eklenir |
> | K8 | §3.4 ⑧ | Dayanak (**kohort çalışması**) iddia metnine taşınır |
>
> ⭐ **Bu turun en değerli bulgusu bir çürütme değil, bir YANLIŞ ANLAMADIR (K5).** Yetkin bir okuyucu, önerme formunda yazılmış bir cümlemizi **tam tersine** anladı — çünkü olumsuzlamanın kapsamı Türkçe yüzeyde ayrışmıyordu. Bu, lojik→kod raporunun uyardığı tuzağın **canlı vakasıdır**: *"olumsuzlamanın kapsamı doğal dilde belirsiz olduğunda kod sessizce yanlış dalı seçer."* Burada kod değil **bir model** seçti — ve yanlış seçti.
> ⇒ **Türetilen kural (K10):** önerme formunda `¬` kullanılan her cümlede **kapsam parantezle sabitlenir**.

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
4. İndirme/bağımlı sayısı, yıldızın aksine, bakım aktifliğini **toplu düzeyde** güçlü ve monotonik biçimde öngörür — **paket başına garanti DEĞİLDİR**.
   > **[K4 · antitez daraltması]** Ölçümümüz (M2) bir **katman agregasıdır**: top-500'de terk %8,6, rastgelede %54,2. Bu bir **dağılım** iddiasıdır. Antitezin karşı-örnekleri (`moment.js` bakım moduna geçtiği hâlde indirmeleri devasa kaldı; `request` deprecated ilan edildikten sonra yıllarca yüksek kaldı) **en üst katmandaki aykırı değerlerdir** ∧ agregayı **çürütmez** — ama *"güçlü öngörür"* ifadesi paket-başına okunmaya açıktı. Karşı-örnekler `[K-hatırlama]`dır (doğrulanmadı); mekanizma (**ekosistem ataleti**) kendi M7 bulgumuzla uyumlu olduğu için **kabul edildi**.
5. Rastgele bir açık kaynak paketi terk edilmiştir; terk edilmemişlik istisnadır, kural değildir.
6. Yaygın kullanılan paketlerin büyük kısmında yayın yetkisi tek hesapta yoğunlaşmıştır; bu, ölçek büyüdükçe azalmaz, yalnız en tepede azalır.
7. Teknoloji seçiminin sonuca etkisine dair en çok atıf alan ampirik kanıt, bağımsız yeniden analizde büyük ölçüde geçersizleşmiştir.
8. Ölçek-bağımlı folklorun (mikroservis/monolit) ölçülmüş hali, folklorun tersi yönde sonuç vermektedir — **dayanak: ICSME 2023 registered report KOHORT ÇALIŞMASI**, tek bir vaka değil.
   > **[K8 · antitez kısmen haklı]** Antitez *"Prime Video tek vakadır, 'ölçülmüş' statüsüne yükseltilemez"* dedi. **Kısmen kabul:** bizim dayanağımız o vaka **değildi**, kohort çalışmasıydı — ama **iddia metni bunu belirtmiyordu** ⇒ dayanak artık iddianın **içinde** yazılı. Prime Video, §3.3 ▲3'teki **ters yön** listesinde ayrı bir kayıttır, bu iddianın dayanağı değil.
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
| **Vaka sayısı** | Gick & Holyoak: kaynak analog yokken çözüm ~%10; **tek** analogla ~%30; ipucuyla ~%80. Şema tümevarımı **iki vakanın karşılaştırılmasıyla** oluşuyor. **Tek vaka okumak transferi DÜŞÜK bırakır — sıfır değil (~%30, yani analogsuz hâlin ~3 katı).** *(K1 ile düzeltildi; eski hâli "neredeyse transfer üretmiyor" diyordu ∧ satırın kendi rakamıyla çelişiyordu.)* | [K] |
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

### 5.4 A24 iddia listesi — **ANTİTEZ KOŞTU, hükümler işlendi**

*Bu başlık `⊨¬2` idi. **Artık değil.***

1. Yazılım mimarisi kararları Kahneman-Klein anlamında **geçersiz** bir öğrenme ortamıdır; bu alanda deneyimden doğal sezgi gelişmez. — **çürütülemedi** *(ama §5.1'in kendi şerhi geçerli: bu bir **bileşimdir**, literatür bulgusu değil)*
2. Mimaride yıl sayısı uzmanlık üretmez; geri bildirim mimarisi düzeltilmeden geçen yıllar performansı **düşürebilir**. — **çürütülemedi**
3. Deliberate practice mesleki alanlarda varyansın %1'inden azını açıklar; yazılım mimarisi için ölçülmüş bir DP tahmini yoktur. — **⊨S**, antitezin ifadesiyle *"en sağlam, en spesifik, en doğrulanabilir iddia"* ⚠️ *(aynı-aile şerhi geçerli)*
4. Vaka okumanın öğretici olması için **en az iki zıt vakanın** karşılaştırılması gerekir; tek vaka okuma transferi **DÜŞÜK bırakır (~%30), SIFIRLAMAZ**. — **⛔ ÇÜRÜTÜLDÜ (K1)**
   > **[K1]** Eski hâli *"tek vaka okuma transfer üretmez"* diyordu. Antitez kaynağın kendi verisini gösterdi: `tek_analog → ~%10-30 transfer`, **sıfır değil**. Ve bu, **bizim İÇ TUTARSIZLIĞIMIZDI** — §5.3 zaten *"tek analogla ~%30"* yazıyordu. ⇒ Gerçek iddia: `tek_vaka → transfer DÜŞÜK ∧ ≠ sıfır` ∧ `şema_tümevarımı ⇔ karşılaştırma`. **İki vaka kuralı ayakta**; gerekçesi *"tek vaka işe yaramaz"* değil, *"şema ancak karşılaştırmayla doğar"*.
5. Başarısızlık vakaları başarı vakalarından daha öğretici ve daha kalıcıdır. — **çürütülemedi**
6. **(Sonuç GÖRÜNÜR durumdayken) okumak öğretici değildir**; **(sonuç kapatılarak) okumak — tahmin → aç → skorla — öğreticidir.** Sonucu bilinen bir kararı okumak, sonuç yanlılığı nedeniyle süreç değerlendirmesini sistematik bozar.
   > **[K5 · ⭐ olumsuzlama kapsamı — YENİDEN YAZILDI]** Eski hâli *"sonuç kapatılmadan okuma öğretici değildir"* idi. Kastedilen ayrıştırma `[sonuç kapatılmadan] [okuma]` = **sonuç GÖRÜNÜRKEN okumak**. Antitez bunu **tam tersine** okudu (*"sonuç açıklanmadan okuma öğretici değildir"*) ∧ haklı olarak HBS vaka yöntemini karşı-örnek gösterdi — o yöntem sonucu **bilerek saklar**.
   > **İddia AYAKTA — ama bu bir zafer değil, bir ARIZA kaydıdır.** Yetkin bir okuyucu önerme formunda yazılmış bir cümleyi ters anladı; sebep **olumsuzlamanın kapsamının belirsizliğiydi** (`¬(kapatılmış) ∧ okuma` mı, `kapatılmış ∧ ¬okuma` mı — Türkçe yüzeyde ayrışmıyor).
   > ⇒ **Kural (K10):** önerme formunda `¬` kullanılan her cümlede **kapsam parantezle sabitlenir**.
7. Kalibrasyon skorlaması, **insan kolaylaştırıcı olmadan** nesnel performans verisi üretebilen **BULUNABİLEN TEK** pratik mekanizmadır — *"tek"* burada **bulunabilen tek** demektir, **kanıtlanmış tek DEĞİL**. `[?]` **Bu eğitimin mimari karar öğrenimine transferi ÖLÇÜLMEMİŞTİR.**
   > **[K6 · antitez tam isabet — çifte standart kabul edildi]** İddia 2, çerçevelerin (ADR/Radar/ATAM) etkinliğinin ölçülmediğini söyleyerek **şüpheci bir standart** uyguluyordu; iddia 7 ise kalibrasyonun *"tek pratik mekanizma"* olduğunu **aynı titizlikte kanıt sunmadan** ∧ **daha güçlü** bir kesinlikle iddia ediyordu.
   > Ve bunu **bizim kendi raporumuz da söylüyordu** (A24 boşluk #4: *"Mimari kararlarda Brier-skorlu tahmin eğitimi denenmemiş"*) — ama **iddia listesine taşınmamıştı**. `M1`'in vakası: iddia listesi, raporun kendisinden zayıf çıktı.
   > ⇒ Bu, §7'deki **Model C önerisinin** dayanağını zayıflatır. Model C hâlâ önerilir — ama gerekçesi *"en iyi kanıtlı"* değil, **"tek uygulanabilir"**.
8. Sezgi-temelli yansıtma öğrenme üretmez; öğrenme için **açıkça yazılmış bir karar kuralı** gereklidir. — **çürütülemedi**
9. Teknoloji seçiminde en büyük sistematik hata kaynağı bilgi eksikliği değil, **teşvik yapısıdır** (özgeçmiş güdümlü seçim + büyük-ölçek çözümünün transplantı). — **çürütülemedi**

---

## 6 — A23 · DS/ML asgari yığını

> **REGISTER NOTU:** Bu bölüm, Salih'in 07-26 hükmünden (ai-to-ai = tam önerme formu, P144) SONRA yazıldı ve **önerme formundadır**. Dosyanın §1–§5'i hükümden önce yazıldığı için eski register'dadır. Karışıklık kasıtlı değil, **kronolojiktir** ve kayda geçer.

**Kanıt notu — bu ailenin ayırt edici özelliği:** A23'ün bulgularının neredeyse tamamı **bu makinede yapılmış kendi ölçümüdür** `[D-ölçüm]`, literatür aktarımı değil. Ajan dört alt-hat açtı; **alt-hatların metnini elinde doğrulayamadığı için aktarmadı ve uydurmadı** — konu alanlarını kendi ölçümüyle kapattı, literatür boşluklarını açıkça işaretledi. *Bu davranış, B7/B8 kuralının (bkz. araştırma-promptu atlası) canlı doğrulamasıdır.*

### 6.1 Paket katmanı

**R1** `[D]` — SATICI İDDİASI RAKAMSIZ
`uv/BENCHMARKS.md → sayı = ∅` ∧ `içerik = yalnız bar_grafik_GÖRSELİ`
`ölçüm_tabanı = tek_dosya (Trio docs-requirements.in) ∧ yalnız_macOS`
Satıcının kendi uyarısı: *"Benchmark performance may vary dramatically across different operating systems and filesystems."*
⇒ **"10-100x" iddiası kendi deposunda doğrulanabilir sayıya dayanmıyor.**

**R2** `[D-ölçüm]` — KENDİ ÖLÇÜMÜMÜZ (bu makine, Linux, Py 3.11.15, uv 0.8.17 vs pip 24.0; 7 doğrudan → 25 paket)

| İşlem | pip | uv | oran |
|---|---|---|---|
| venv oluşturma | 4,08 s | 0,034 s | **120×** |
| sıcak kurulum | 36,66 s | 0,39 s | **93×** |
| **soğuk kurulum (ağ-bağımlı)** | 30,27 s | 7,86 s | **3,9×** |
| ortam diski | 677 MB | 514 MB | pip 1,32× büyük |

⇒ `93× = gerçek` ∧ **`mutlak_tasarruf ≈ 36 saniye`**
⇒ `senaryo = soğuk (CI ∨ ilk_kurulum)` ⇒ `kazanç = 3,9×` — çünkü **darboğaz ağdır**
⇒ Satıcı bandı `sıcak → doğrulanıyor` ∧ `soğuk → doğrulanmıyor`
**⊨X** `pip_sıcak (36,7 s) > pip_soğuk (30,3 s)` ⇒ pip'in darboğazı indirme değil, **açma/kurma**.

**R3** `[D-ölçüm]` — ⭐ ASIL GEREKÇE HIZ DEĞİL
`poetry → 49 Python_paketi ∧ 56 MB` **ortamınıza girer**
`pip-tools → 8 paket ∧ 13 MB`
`uv → tek_statik_ikili ∧ 0 Python_bağımlılığı`
⇒ `uv ∩ proje_bağımlılık_grafiği = ∅` ⇒ **asla çakışmaz**
⇒ Bu, hızdan **daha sağlam** bir gerekçedir.

**R4** `[D]` — `src/` TARTIŞMASI KARARA BAĞLANMAMIŞ
`PyPA_metni → iki_düzeni_yan_yana_koyar ∧ tavsiye = ∅ ∧ ampirik_iddia = ∅` (tümü argümantatif)
`tek_somut_faydası = kurulu_kopya_yerine_geliştirme_kopyasının_yanlışlıkla_import_edilmesini_önlemek`
⇒ Bu fayda **yalnız paketleyip DAĞITIYORSANIZ** anlamlıdır.
**R5** `[D-ölçüm]` — ve tartışma pratikte **bedelsiz** çözülmüş: `uv init --lib` zaten `src/` üretiyor (0,089 s, 14 satır `pyproject.toml`, 6 dosya) ⇒ `src/ = maliyet_değil, VARSAYILAN`.

**R6** `[D-ölçüm]` — ASGARİ YIĞININ TOPLAM MALİYETİ
`pandas ⊕ numpy ⊕ scipy ⊕ matplotlib ⊕ pyarrow ⊕ ruff ⊕ pytest` ⇒ **3,33 saniye** · 26 satır `pyproject.toml` · 24 kilitli paket · 472 MB venv · **insanın bakacağı 5 dosya** (4'ü otomatik üretiliyor).

### 6.2 Kalite katmanı — ⭐ ailenin en önemli negatif bulgusu

**R7** `[D-ölçüm]` — ruff FİNANSAL HATALARIN HİÇBİRİNİ GÖRMÜYOR
Gerçekçi bir risk modülüne kasıtlı hatalar konuldu.
`ruff(varsayılan) → 7 hata` — **hepsi hijyen** (kullanılmayan import/değişken, mutable default)
`ruff(--select ALL) → 32 hata` — fazladan 25'i docstring, tip-notu, telif notu, tırnak stili
`gerçek_hata_artışı(ALL) = 0`
**`look_ahead_hatası (df['ret'].shift(-1)) → İKİ MODDA DA tespit edilmedi`**

**R8** `[D-ölçüm]` — mypy'ın İLK İZLENİMİ %100 GÜRÜLTÜ
`bağlam = veri_bilimi_dosyası` ∧ `pandas-stubs ⊕ numpy ⊕ scipy kurulu` (adil koşul)
`mypy(varsayılan) → 1 hata` (scipy stub'ı yok)
`mypy(--strict) → 6 hata` (5'i "annotation eksik")
`gerçek_hata = 0`

**R9** `[D-ölçüm]` — ⭐ İKİ TARAFLI: mypy TİP-NOTLU SINIRLARDA KÂR EDİYOR
Aynı test, anotasyonlu kodda 4 gerçek hatayla:
- `annualise(df, 252)` → `DataFrame` beklenen `float` **✔**
- `annualise(1.5, "252")` → `str` beklenen `int` **✔** *(config dosyası klasiği)*
- return ifadesi eksik **✔**
- `df["clsoe"].mean()` — sütun adı yazım hatası — **✘ YAKALANAMADI**

⇒ **`mypy → statik_imzalarda kâr` ∧ `mypy → DataFrame_içeriğinde KÖR`**
⇒ Ve `veri_biliminde hataların_çoğu ∈ DataFrame_içi` ⇒ **kapsama yapısal olarak dar.**

**R10** `[D]` — BAKIM AĞIRLIĞI (PyPI metadata): `ruff → 0 doğrudan bağımlılık` · `mypy → 12` · `pytest → 14`. `ruff ∧ uv = aynı ekip ∧ ikisi de 0 bağımlılık` ⇒ kurulum riski yok.

**R11** `[ARANAMADI]` — tip ipuçlarının hata oranına etkisi üzerine ampirik literatür. `WebSearch_bütçesi = tükendi` ∧ `akademik_yayıncılar = 403`.
⇒ **"Bulunamadı" DEĞİL.** R7–R9 kendi kontrollü ölçümümüzdür ∧ **literatür yerine GEÇMEZ.**

### 6.3 Veri katmanı

**R12** `[D]` — polars'ın deposunda da RAKAM YOK. README yalnız *"very fast"*, *"one of the best performing"* ∧ kendi benchmark sayfasına link. `depoda_üretilebilir_sayı = ∅`.

**R13** `[D-ölçüm]` — ⭐ KENDİ ÖLÇÜMÜMÜZ (1,26M satır × 7 sütun; 500 hisse × 2520 gün; ~40 MB parquet; gerçekçi portföy paneli)

| işlem | pandas | polars | duckdb | polars kazancı |
|---|---|---|---|---|
| parquet okuma | 0,247 s | 0,171 s | 0,515 s | 1,4× |
| **groupby → 4 agregat** | **0,071 s** | **0,085 s** | 0,092 s | **0,8× (polars YAVAŞ)** |
| sort + 20g hareketli ort. | 0,403 s | 0,252 s | – | 1,6× |
| universe join + filtre | 0,784 s | 0,108 s | – | **7,2×** |
| hisse başına pct_change | 0,279 s | 0,244 s | – | 1,1× |

⇒ `polars_kazancı ∈ [0,8× , 7,2×]` ∧ `ortanca ≈ 1,4×`
⇒ **Pazarlamanın çağrıştırdığı 10-50× YOK.** Tüm işlemler `< 1 saniye`.

**R14** `[D-ölçüm]` — ⭐ ASIL DARBOĞAZ IMPORT
`import: pandas 0,73 s · polars 0,22 s · duckdb 0,12 s · numpy 0,20 s`
`5_işlemin_pandas_toplamı = 1,78 s` ⇒ **`pandas_import / toplam_iş_yükü = %29`**
⇒ **Küçük veride kütüphane seçimi değil, SÜREÇ BAŞLATMA baskındır.**

**R15** `[D-ölçüm]` — PARQUET vs CSV (aynı panel)

| format | yazma | okuma | boyut |
|---|---|---|---|
| CSV | 9,25 s | 1,68 s | 76,2 MB |
| CSV.gz | 26,93 s | 1,79 s | 28,6 MB |
| **Parquet** | **0,78 s** | **0,53 s** | **39,7 MB** |

`sütun_alt_kümesi (7 → 2)` ⇒ `parquet 0,07 s vs CSV 0,88 s = 12,6×`

**R16** `[D-ölçüm]` — ⭐ PARQUET'İN ASIL GEREKÇESİ HIZ DEĞİL, **DOĞRULUK**
`CSV_round_trip → datetime64[us] SESSİZCE str'e döner` ⇒ `orig.equals(csv) = False`
`Parquet_round_trip` ⇒ `True` (bit-aynı)
⇒ `zaman_serisi_projesi ∧ tarih_sütunu = str` ⇒ **leksik sıralama** ⇒ **sessiz doğruluk hatası.**

**R17** `[D]` — DVC'nin DEĞERİ TAKIM İÇİNDİR
README'nin kendi ifadeleri: *"Store them in your cloud storage"*, *"Share data and model files"*, *"collaborate with others"*
`kullanıcı = tek_kişi` ∧ `uzak_depolama = ∅` ⇒ **`değer ≈ 0`**
**R18** `[D-ölçüm]` `DVC_maliyeti = 98 paket ∧ 107 MB` (PyPI'da 82 doğrudan bağımlılık).

**R19** `[ERİŞİLEMEDİ]` — bağımsız db-benchmark SAYILARI. `duckdblabs.github.io = HTTP 000` (`*.github.io` kapalı) ∧ `pola.rs/benchmarks.html = HTTP 000`.
⇒ Hem bağımsız hem satıcı rakamları **aranamadı** ⇒ R13'ün kendi ölçümü bu boşluğu doldurur.

### 6.4 Deney takibi

**R20** `[D-ölçüm]` — ⭐ GERÇEK KURULUM AĞIRLIĞI (boş venv'e kurulup sayıldı)

| araç | paket | disk |
|---|---|---|
| **mlflow** | **90** | **611 MB** |
| mlflow-skinny | 41 | 64 MB |
| wandb | 17 | 98 MB |
| dvc | 98 | 107 MB |

`mlflow (611 MB) > tüm_bilimsel_yığın (472 MB)`
⇒ **Deney takibi eklemek ortamı İKİYE KATLIYOR.**
⇒ `mlflow-skinny = 10× hafif` ∧ çoğu solo kullanım için yeterli — **bu ayrım az biliniyor.**

**R21** `[D-ölçüm]` — ⭐ KRİTİK VE GÜNCEL: MLflow 3.x DOSYA DEPOSUNU KALDIRDI
`MLflow 3.14.0 ∧ ./mlruns` ⇒ **istisna fırlatır**:
> *"The filesystem tracking backend (e.g., './mlruns') is in maintenance mode and will not receive further updates. Please migrate to a database backend (e.g., 'sqlite:///mlflow.db')"*

⇒ **İnternetteki "pip install mlflow, mlruns'a yaz, bitti" tavsiyesinin TAMAMI MLflow 2.x içindir ∧ artık GEÇERSİZDİR.**
Ölçüldü: `sqlite_arka_ucu → çalışıyor` ∧ `ilk_koşum_şema_göçü = 7,42 s ∧ 791 KB db`; `dosya_deposu → yalnız MLFLOW_ALLOW_FILE_STORE=true ile` ∧ `tek_koşum → 10 dosya`.

**R22** `[D-ölçüm]` — BASİT ALTERNATİFİN ÖLÇÜLMÜŞ MALİYETİ
`8 satır Python ∧ 0 bağımlılık ∧ 0,006 s/koşum ∧ satır_başına_bir_JSONL_kaydı (git SHA dahil)`
⇒ `90 paket / 611 MB` **karşısında** `8 satır / 0 paket`.

**R23** `[D]` — BAKIM CANLILIĞI (PyPI son sürüm, bugün çekildi)
`CANLI: mlflow 3.14.0 (2026-06-17) · wandb 0.28.1 (2026-07-16) · dvc 3.67.1 (2026-03-31)`
`TERK EDİLMİŞ: backtrader (2023-04-19) · pyfolio (2019-04-15) · empyrical (2020-10-13)`

**R24** `[ARANAMADI]` — "kaç deneyden sonra manuel takip kırılır" eşiği. **Kestirim verilmedi.**

### 6.5 Yeniden üretilebilirlik

**R25** `[D-ölçüm]` — TOHUMLAMA KATMANLARI BİRBİRİNİN YERİNE GEÇMİYOR
`np.random.seed(0) → [0.548814, 0.715189, 0.602763]`
`np.random.default_rng(0) → [0.636962, 0.269787, 0.040974]`
⇒ Farklı akışlar ⇒ **eski kodu yeni API'ye taşımak sonuçları SESSİZCE değiştirir.**

**R26** `[D-ölçüm]` `RandomForestRegressor(n_estimators=30)` ∧ `¬random_state` ⇒ iki fit farklı tahmin. `random_state=0` ⇒ aynı.

**R27** `[D-ölçüm]` — ⭐ EN SİNSİ: `PYTHONHASHSEED`
`¬PYTHONHASHSEED` ⇒ `set_sıralaması her_koşumda DEĞİŞİR`
İki ardışık koşum: `['MSFT','AAPL','GOOG','TSLA']` vs `['MSFT','TSLA','AAPL','GOOG']`
`hash("AAPL")` de süreçler arası değişiyor (−6300815829564892180 vs 8214638119298906547)
⇒ **`hisse_evreni ⟵ set` ⇒ tüm tohumlar doğru olsa BİLE sütun sırası her koşumda değişir.**

**R28** `[D-ölçüm]` — NOTEBOOK SIRA-DIŞI ÇALIŞTIRMA GİT DIFF'TE GÖRÜNMEZ
`execution_count = [1, 5, 3, 4]` ⇒ okuyucuya *"filtre önce uygulandı"* izlenimi ∧ gerçekte `Sharpe` filtreden **ÖNCE** hesaplanmış.
`tespit = 3 satır` (kod hücrelerinin `execution_count` listesi `1..N` ile aynı mı?)

**R29** `[D]` — AĞIRLIK UYARISI: `papermill → 103` · `jupytext → 72` · `nbdev → 23` doğrudan bağımlılık.
⇒ **Notebook'u "düzeltmek" için kurulan araç, düzeltmeye çalıştığı yığından ağır olabiliyor.**

**R30** `[ARANAMADI]` — brifingteki notebook `%4` rakamının birincil doğrulaması. **Teyit edilmedi, üzerine inşa edildi** — *bu ayrım önemlidir ve kayda geçer.*

### 6.6 Finansal zaman serisi — ⭐ en yüksek değerli blok

**R31** `[D-hesap]` — MinBTL FORMÜLÜ BAĞIMSIZ OLARAK DOĞRULANDI
`gerçek_beceri = 0` ∧ `N varyant denendi` ⇒ beklenen en yüksek in-sample yıllık Sharpe:

| N | 2 yıl | 5 yıl | 10 yıl | 20 yıl |
|---|---|---|---|---|
| 5 | 0,84 | 0,53 | 0,38 | 0,27 |
| 10 | 1,11 | 0,70 | 0,50 | 0,35 |
| **45** | 1,58 | **1,00** | 0,71 | 0,50 |
| 128 | 1,85 | 1,17 | 0,83 | 0,59 |
| 1000 | 2,30 | 1,46 | 1,03 | 0,73 |

⇒ *"5 yıl veriniz varsa 45'ten fazla bağımsız konfigürasyon denemeyin"* iddiası **birebir doğrulandı** (`N=45 ∧ 5_yıl → 1,000`).

**R32** `[D-simülasyon]` — İKİNCİ BAĞIMSIZ YÖNTEM AYNI SONUCU VERDİ
Monte Carlo: saf gürültü, `gerçek_edge = 0`, 5y in-sample / 5y out-of-sample, 200 tekrar

| N | en iyi in-sample SR | onun out-of-sample SR'ı |
|---|---|---|
| 1 | −0,06 | 0,03 |
| 10 | 0,68 | −0,04 |
| **45** | **0,99** | **−0,01** |
| 100 | 1,13 | 0,01 |
| 1000 | 1,46 | −0,04 |

`simülasyon ≈ analitik_formül` (2 ondalık basamağa kadar: 45→0,99 vs 1,00 · 100→1,13 vs 1,13 · 1000→1,46 vs 1,46)
`out_of_sample ≈ 0` **her zaman**
⇒ **`in_sample_Sharpe = f(seçim_sayısı)` ∧ `≠ f(beceri)`**

**R33** `[K]` — YAYINLANMIŞ FİNANS LİTERATÜRÜ AYNI YÖNDE
`452 anomali → %65'i t>1,96 eşiğini geçemiyor` ∧ `çoklu_test_eşiği t>2,78 → başarısızlık %82,1`
`316 faktör kataloglandı → yeni faktör eşiği t>3,0 olmalı` (t>2,0 değil)
`97 öngörücü → getiri örneklem_dışında %26 ↓ ∧ yayın_sonrası %58 ↓`

**R34** `[X]` — ▲ KARŞI GÖRÜŞ MEVCUT, TEK TARAFLI SUNULMUYOR
*"Most claimed statistical findings in cross-sectional return predictability are likely true"* başlıklı çalışma, "çoğu bulgu yanlış" sonucunu **doğrudan reddediyor**. `erişilemedi (arXiv 403)` ∧ **varlığı kayda değer**.
⇒ **Bu literatür TARTIŞMALIDIR.**

**R35** `[D]` — VERİ SIZINTISININ ÖLÇÜLMÜŞ ETKİSİ
`Binance BTC/USDT günlük, 20-bar ileri getiri` ∧ `ekonomik_gerekçesi_olmayan_öznitelik`:
`naif_karıştırılmış_k_fold → R² ≈ +0,85` ∧ `PurgedKFold → R² ≈ −1,2`
`tamamen_öngörülemez_hedef → naif R² 0,83..0,91` **(saf gürültüde!)** ∧ purged sonrası ortalama-tahmini altında
`UCI_hava_kalitesi: 3_normal_lag → naif R²=0,07` ∧ `+ tek_masum_kümülatif_saat_sayacı → naif R²=0,99` ∧ `purged (−1,52) KIPIRDAMIYOR`

**R36** `[X]` — ▲ DÜRÜSTLÜK NOTU: SIZINTI HER ZAMAN FELAKET DEĞİL
Aynı kaynak: `4.284_haneli Low Carbon London` ⇒ `naif_k_fold ↔ walk_forward zamansal_boşluk = %1,60 (GA %1,27–1,94)`; asıl ısıran sızıntı **hane-bazlı (%6,03)**.
⇒ **Ders: hangi bölmeye ihtiyacın olduğu neyin üzerinde çalıştığına bağlıdır — kategorik korku değil, ÖLÇÜM.**

**R37** `[D-ölçüm]` — ⭐ NAİF LOOK-AHEAD TESTİ İŞE YARAMIYOR
Klasik *"veriyi kes, sinyal değişiyor mu bak"* testi yazıldı ⇒ **bilinen hatalı fonksiyonu YAKALAYAMADI.**
Sebep ölçüldü: `shift(-1) ∧ kesme_noktası` ⇒ yalnız **1 satır** farklılaşabiliyor ∧ eşiklenmiş (boolean) sinyalde bu fark `~%50` olasılıkla tesadüfen aynı değere çöküyor. Örnekte `200 satırlık örtüşme → farklılaşan_satır = 0`.

**ÇALIŞAN SÜRÜM** (ölçüldü, `10/10` kesme noktasında yakalıyor):
`kesme_noktasını_SÜPÜR ∧ boolean_değil_HAM_FLOAT_karşılaştır ∧ NaN_DUYARLI_eşitlik`
⇒ **~20 satırlık bu pytest, ruff ∧ mypy'ın tamamen kör olduğu hata sınıfını yakalar.**

**R38** `[D-simülasyon]` — SURVIVORSHIP BIAS
`1000 firma ∧ 10 yıl ∧ gerçek_drift %6/yıl ∧ delist(zirveden −%80)` ⇒ `firmaların %6,5'i siliniyor`
`eşit_ağırlıklı_yıllık_getiri: tam_evren %5,53` vs `yalnız_hayatta_kalanlar %6,67`
⇒ **`abartma = %1,14/yıl`** — gerçek fon verisindeki `~%0,9/yıl` ölçümü ∧ genel `%1–4` bandı `[K]` ile **uyumlu**.

**R39** `[K]` — LOOK-AHEAD BIAS'IN ÖLÇÜLMÜŞ ETKİSİ (Compustat PIT vs gecikmeli veri)
`48 araştırma_sonucundan 37'si → PIT-temelli aylık ortalama spread ∧ Q1 getirilerini ABARTMIŞ`
`kümülatif_getiri_farkı → %39'a kadar` · `9 baz puanlık sapma ⇒ %3,8 gerçeklikten sapma`

**R40** `[K]` — SIZINTI DİSİPLİNLER ARASI SİSTEMİK: en az `294 makale ∧ 17 disiplin`; erken sürümde `329 makale / 30 alan`. 8 tipli sızıntı taksonomisi.

**R41** `[D]` — ⭐ EKOSİSTEM UYARISI: PROJENİN ALANINDAKİ ARAÇLARIN ÇOĞU ÖLÜ
`ÖLÜ: backtrader (2023-04-19) · pyfolio (2019-04-15) · empyrical (2020-10-13)`
`CANLI: backtesting 0.6.6 (2026-07-22) · vectorbt 1.1.0 (2026-07-05) · quantstats (2026-01-13) · yfinance 1.5.2 (2026-07-23)`
`pypbo (PBO/DSR/MinBTL) → README'de kendi kaydı: "TODO: Add test cases"` ⇒ **test edilmemiş.**

### 6.7 ASGARİ UYGULANABİLİR YIĞIN (öncelik sırasıyla)

| # | Katman | Gerekçe | Maliyet |
|---|---|---|---|
| **1** | **Nedensellik testleri (pytest)** — kesme-noktası süpüren look-ahead testi | Projenin doğruluğunu belirleyen **tek** katman. `ruff 0/1` · `mypy 0/1` · **bu test 10/10** (R37). Sızıntı BTC'de R²'yi `+0,85 ↔ −1,2` oynatıyor (R35) | ~20 satır |
| **2** | **Deneme sayacı + out-of-sample kilidi** | Kaç varyant denendiği yazılmazsa Sharpe **anlamsızdır**. 5 yıl ∧ 45 varyant = Sharpe 1,0 **saf şanstan** (R31, R32 — iki bağımsız yöntem) | 1 metin dosyası, 0 bağımlılık |
| **3** | **uv** | 4 aracın işini tek statik ikili ∧ **0 Python bağımlılığı** (R3). `uv init --lib` → `src/` bedava (R5) | 3,33 s (R6) |
| **4** | **pandas + numpy + scipy** | Bu ölçekte polars ortanca 1,4× ∧ groupby'da **0,8× yavaş** (R13) | zaten yığında |
| **5** | **Parquet (pyarrow)** | **Hız değil DOĞRULUK** (R16). Yan fayda: 12× yazma, 1,9× boyut | tek satır |
| **6** | **ruff** | 0 bağımlılık, 0 config — hijyen borcunu sıfırda tutar, **ama hata bulmasını BEKLEME** (R7) | ~2 s |
| **7** | **pytest** | 1–2'yi çalıştıran koşum aracı | 14 bağımlılık |
| **8** | **Tohum disiplini** — `default_rng(seed)` · her sklearn'de `random_state` · `PYTHONHASHSEED=0` · `set` yerine `sorted()` | `set` sıralaması koşumlar arası değişiyor, **tüm tohumlar doğruyken bile** (R27) | 4 satır |
| **9** | **JSONL deney kaydı (git SHA'lı)** | 8 satır / 0 bağımlılık / 0,006 s (R22) **vs** 90 paket / 611 MB (R20) | 8 satır |
| **10** | **notebook = yalnız keşif; modül = gerçek** + `execution_count` kontrolü | Sıra-dışı çalıştırma git diff'te görünmez (R28) | 3 satır |

> **Toplam: ~3,3 saniye kurulum · 26 satır yapılandırma · tek ek dosya.**

### 6.8 NE ALINMAZ — gerekçeli

| Araç | Hüküm | Gerekçe |
|---|---|---|
| **MLflow / W&B** | **ALINMAZ** | 90 paket / **611 MB** > tüm yığın (472 MB) (R20) ∧ MLflow 3.x dosya deposunu **kaldırdı**, "sadece pip install" tavsiyeleri **geçersiz** (R21). Yerine 8 satır JSONL (R22). *Gerekirse `mlflow-skinny`: 41/64 MB* |
| **DVC** | **ALINMAZ** *(hüküm değişmedi)* | 98 paket / 107 MB (R18) ∧ değeri **ağırlıklı olarak takım + bulut** senaryosunda (R17). **[K3 düzeltmesi:** tek kişide `değer ≈ 0` **DEĞİL, AZALMIŞ**. Antitez haklı: uzak depolama olmasa da `dvc repro` **yerel önbellekleme** (değişmeyen aşamaları atlama) ∧ **pipeline DAG'ı** sağlar. Bizim gerekçemiz deponun kendi *"takım + bulut"* vurgusuna dayanıyordu — bu **değeri azaltır, sıfırlamaz**.**]** ⇒ Yeni gerekçe: `azalmış değer < 98 paketlik maliyet`. Yerine: SHA256 + tarihli klasör |
| **poetry** | **ALINMAZ** | 49 paket / 56 MB ortama girer (R3); uv aynı işi **0 Python bağımlılığıyla** yapıyor |
| **mypy `--strict`** | **BAŞLANGIÇTA ALINMAZ** | İlk çıktı %100 gürültü, 0 gerçek hata (R8) ∧ sütun adı hatasını yakalayamıyor (R9). **Sonra**, kararlı `src/` modüllerinin imzalarına değer — orada 3/4 yakalıyor |
| **ruff `--select ALL`** | **ALINMAZ** | 7 → 32 hata ∧ **gerçek hata artışı 0** (R7) |
| **polars** | **ŞİMDİ ALINMAZ** *(hüküm korunur, gerekçe EKSİK olarak işaretlendi)* | Ortanca 1,4× ∧ groupby'da yavaş ∧ tüm işlemler `<1 s` (R13). Veri `>5-10 GB` ∨ `join`-ağırlıklı iş yükü olursa **yeniden değerlendir** (orada 7,2×).<br>**[K7 · antitez ince yakalama — ⚠️ EKSİK GEREKÇE]** İddia 15'in kendi mantığı (*"parquet'in gerekçesi hız değil dtype bütünlüğü"*) **polars'a geri uygulanırsa**: polars'ın asıl argümanı da hız değil **şema katılığı, lazy-evaluation'da erken tip hatası, Arrow bellek modeli, null-semantiği tutarlılığı**dır. ⇒ Bu hüküm **yalnız hız eksenine** dayanıyor ∧ **şema-katılığı ∧ null-semantiği ekseni ÖLÇÜLMEDİ** ⇒ **yeni borç (B8)**. Hüküm ayakta, ama *"ölçüldü ve elendi"* demek **yanlış olur** — bir eksende ölçüldü, diğerinde ölçülmedi.<br>⚠️ Antitezin *"db-benchmark'ta polars groupby kat kat hızlı"* karşı-iddiası: **kendi ölçümümüz (R13, bu makinede, 1,26M satır) bunu göstermiyor** ∧ antitez kendi belirsizliğini dürüstçe işaretledi (*"emin değilim"*) ⇒ `[D]` ölçüm `[K-hatırlama]`yı yener, **rakam korunur** — ama **ölçek bağımlılığı** kaydı güçlenir: bizim ölçümümüz **1,26M satırdır**, db-benchmark ölçekleri farklıdır |
| **papermill / jupytext / nbdev** | **ALINMAZ** | 103 / 72 / 23 doğrudan bağımlılık (R29). Çözüm araç eklemek değil, **mantığı `src/`'ye taşımak** |
| **Docker** | **ALINMAZ** | `uv.lock` tek kişilik projede yeterli; maliyeti bu ölçekte getirisini aşar |
| **backtrader / pyfolio / empyrical** | **ALINMAZ — TERK EDİLMİŞ** | Son sürümler 2023 · 2019 · 2020 (R41) |

### 6.9 A23 iddia listesi — **ANTİTEZ KOŞTU, hükümler işlendi**

① uv'nin 93× sıcak-kurulum avantajı haftada ~36 saniye tasarruf eder; asıl gerekçesi hız değil, **sıfır-bağımlılıklı tek ikili** olmasıdır. — **çürütülemedi**
② Bu ölçekte polars ortanca 1,4×'tir ∧ groupby'da yavaştır; şimdi almak **erken optimizasyondur**. — **hüküm korunur, gerekçe EKSİK (K7):** yalnız **hız** ekseninde ölçüldü; **şema-katılığı ∧ null-semantiği ekseni ölçülmedi** ⇒ B8 borcu.
③ Statik analiz araçları finansal zaman serisi projesindeki **doğruluk-kritik hata sınıfını yapısal olarak yakalayamaz**. — **çürütülemedi**
④ Deney takibi araçları tek kişilik ölçekte **net negatiftir**. — **çürütülemedi**
⑤ Bir backtest'in in-sample Sharpe'ı, **denenen varyant sayısı raporlanmadan yorumlanamaz**. — **⊨S**, literatürle güçlü örtüşme ⚠️ *(aynı-aile şerhi)*
⑥ Parquet'i tercih etmenin baskın gerekçesi hız veya boyut değil, **dtype bütünlüğüdür**. — **⊨S**; ayrıca antitez bunu **②'ye karşı silah olarak** kullandı (bkz. K7)
⑦ **Hash sırasına duyarlı kod yolu içeren** hiçbir koşum, `PYTHONHASHSEED` sabitlenmeden tam olarak yeniden üretilebilir değildir — tüm RNG tohumları doğru olsa bile.
   > **[K2 · antitez daraltması]** Eski hâli *"hiçbir koşum"* diyordu ⇒ **fazla geniş**. `hash_sırası → yalnız hash-duyarlı kod yollarını etkiler`; saf numpy/pandas sayısal hattı (sabit sütun sırası, array-tabanlı) **bağımsız olabilir**. Ve **bizim kendi ölçümümüz (R27) zaten mekanizmayı `set` sıralaması üzerinden gösteriyordu** ⇒ koşul **`set` kullanımıdır**, evrensel değil. Pratik tavsiye (`PYTHONHASHSEED=0` + `set` yerine `sorted()`) **değişmez**.
⑧ Naif look-ahead testi eşiklenmiş sinyallerde işe yaramaz ∧ **yanlış güven verir**. — **⊨S**, çürütülemedi
⑨ DVC'nin tek kişilik projedeki getirisi **azalmıştır** ∧ **98 paketlik maliyeti karşılamaz**. — **⛔ ÇÜRÜTÜLDÜ (K3):** eski hâli *"getirisi sıfırdır"* diyordu. `dvc repro` uzak depolama olmadan da **yerel önbellekleme ∧ pipeline DAG'ı** sağlar ⇒ **değer azalır, sıfırlanmaz**. **Hüküm (ALINMAZ) değişmez, gerekçe düzelir.**

### 6.10 A23 — kapatılamayanlar

`ARANAMADI (bütçe/gate engeli — yokluk kanıtı DEĞİL):` tip ipuçlarının hata oranına etkisi literatürü (R11) · bağımsız pandas-vs-polars sayıları (R19) · notebook %4 rakamının birincil doğrulaması (R30) · manuel takip kırılma eşiği (R24) · ruff'ın bağımsız hız ölçümü · R34'teki karşı-görüşün rakamları
`ARANDI, RAKAM YOK (bu bir YOKLUK BULGUSUDUR):` uv deposunda sayısal benchmark (R1) · polars deposunda sayısal iddia (R12)
`KAPATILAMAYAN ŞERİTLER:` Kalite ∧ Veri alt-şeritlerinin **literatür** taraması dönmedi. **Ajan içeriklerini elinde doğrulayamadığı için aktarmadı ∧ uydurmadı**; her iki alanın **ölçüm** tarafını kendi deneyleriyle kapattı.

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
   > **[K6 · ŞERH GÜÇLENDİRİLDİ]** Antitez bu noktada bir **çifte standart** yakaladı ∧ kabul edildi (§5.4 ⑦). İki ek kayıt:
   > ① *"Tek mekanizma"* ifadesi **"bulunabilen tek"** demektir, **"kanıtlanmış tek"** değil. Bulunamamış olması, olmadığı anlamına gelmez.
   > ② `[?]` **Kalibrasyon eğitiminin MİMARİ KARAR öğrenimine transferi ÖLÇÜLMEMİŞTİR.** GJP'nin %6-7 kazancı **tahmin görevlerinde** ölçüldü; mimari karara taşındığı **gösterilmedi**. Model C'nin çekirdek mekanizması bu transferin **varsayımı** üzerine kuruludur.
   > ⇒ Model C **yine de önerilir** — ama Salih bunu imzalarken *"kanıtlanmış yöntem"* değil, **"ölçülmemiş ama tek uygulanabilir yöntem, ve kendi ölçümünü üretecek şekilde kurulmuş"** olarak imzalamalıdır. L7/L15'in Brier deltası tam olarak bu transferi ölçer ⇒ **model kendi varsayımını sınayacak biçimde tasarlanmıştır.**
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
| B2 | ~~Aşama 2 (antitez) koşulmadı~~ → **KAPANDI 2026-07-26** | A22 ∧ A24 ∧ A23 için koştu (**araçsız**, `tool_uses = 0`) ⇒ mantıksal saldırılar tam güçte, olgusal karşı-örnekler `[K-hatırlama]`. Sonuç: **K1-K8**. §3.4 ∧ §5.4 ∧ §6.9 hükümlerle güncellendi |
| **B8** | **polars'ın şema-katılığı ∧ null-semantiği ekseni ÖLÇÜLMEDİ** (K7) | R13 yalnız **hız** eksenindedir. *"Şimdi alınmaz"* hükmü ayakta ama **eksik gerekçelidir**. Ölçüm yolu: lazy-evaluation'da erken tip hatası yakalama + null semantiği tutarlılığı testi |
| **B9** | **Kalibrasyonun mimari karara transferi ölçülmedi** (K6) | Model C'nin çekirdek varsayımı. L7→L15 Brier deltası bunu ölçmek üzere tasarlandı ⇒ **borç, modelin kendi içinde kapanacak** |
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

**Aile:** A22 · A24 · A23 — **antitez KOŞTU** (2026-07-26, **araçsız**, `tool_uses = 0`)
**Antitez sonucu:** 3 çürütme (K1 vaka sayısı · K3 DVC · K9 iç tutarsızlık) · 5 daraltma (K2, K4, K6, K7, K8) · 1 **yeniden yazım** (K5, olumsuzlama kapsamı) · 3 `⊨S`
**⚠️ İki şerh, birlikte okunur:**
① **Araçsız tur** ⇒ **mantıksal** saldırılar (iç çelişki, aşırı-genelleme, ölçüm-kapsam uyuşmazlığı) **tam güçtedir**; **olgusal karşı-örnekler** (`moment.js`, `request`, HBS vaka yöntemi, db-benchmark) **`[K-hatırlama]`**'dır ∧ borç açar, hüküm değiştirmez.
② `⊨S` = **"aynı-aile hakemi karşısında sağ kaldı"** — antitez ajanları tez ajanlarıyla aynı model ailesindendi ∧ öz-tercih sapması aile düzeyine yayılır.
**Kanıt tabanı:** 4 × [D] kendi ölçümümüz (PyPI n=478 · PyPI 4×500 · npm 220.469 · StarScout ham CSV) · A23'ün tamamı bu makinede **kendi ölçümü** · geri kalan tümü **[K]**, abstract katmanından
**Karar önerisi:** Model C (B içerilerek, sürtünme eşikli) — **Katman 1, Salih imzası bekler.** ⚠️ K6 sonrası gerekçe *"en iyi kanıtlı"* değil, **"tek uygulanabilir ∧ kendi varsayımını ölçecek biçimde kurulmuş"**
**Register:** teknik kayıt **tek karar kaynağıdır**; insan-yüzü iki register (`INSAN-tech-stack.md` + `SOZEL-tech-stack.md`) sonraki emirle **üretildi** ∧ karar kaynağı **değildir**
**En değerli meta-bulgu:** antitezin **yanlış anlaması** (K5), metnimizin kendi belirsizliğinin **ölçümü** oldu — *"antitez ajanının yanlış anladığı her cümle, o cümlenin yeniden yazılması gereken yerdir"*
