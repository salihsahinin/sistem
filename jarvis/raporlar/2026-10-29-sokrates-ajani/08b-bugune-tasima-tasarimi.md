# 08b. Tarihsel kişiyi bugüne taşıma: LLM ve kurgu tasarımı

AS-OF 2026-10-29 (canlı web). Araştırmacı: atlas. Soru: time-displaced / transposed historical persona nasıl kuruluyor, hangi kurallar iyi sonuç veriyor. Çıktı Sokrates ajanı (Sokrates bugünü bilir) tasarımına girdi olacak.

**Ön not (ontolojik):** Literatürün büyük kısmı **ters** problemi çalışıyor: tarihsel figür ölümünden sonrasını bilmemeli (sızıntı = hata). Bizim tasarım tersi: Sokrates bugünü **bilir**. Ama iki problem aynı mekanizmayı paylaşır: model kimin neyi bildiğini rol içinde tutarlı yönetemiyor. Bu yüzden sızıntı literatürü ters yönde okunur (bkz. Bölüm 3, K-8 ve D/K/X).

## 1. Örnekler tablosu

| Örnek | Tür | Bugünü biliyor mu / nasıl kurulmuş | Kaynak | Sınıf |
|---|---|---|---|---|
| Platon diyalogları | Kurgu/felsefe | Platon, Sokrates'in ağzına **kendi o günkü görüşünü** koyar ("mouthpiece theory"); Sokrates'in tarihsel görüşü kaynaklar arasında çelişir (Xenophon pratik öğütçü, Aristophanes karikatür) | [SEP Socrates, §2, §2.1, §2.2](https://plato.stanford.edu/entries/socrates/) | D |
| Kreeft "Socrates Meets ..." (Descartes, Hume, Kant, Kierkegaard, Machiavelli, Marx, Jesus) | Kurgu | Sokrates, modern bir yazarın metnini saf akılla çapraz sorgular; "Machiavelli" kitabında ölümden sonra bir Oxford tutoryali kurgusu; "Jesus" kitabında Sokrates bir ilahiyat okuluna yazılır (çağdaş kampüs). Sokrates'in modern bilgiyi nasıl edindiği ön sözde incelenmedi | [PhilArchive kaydı](https://dc2.philarchive.org/rec/KRESMM), [Goodreads özeti](https://www.goodreads.com/book/show/549005), [IVP](https://ivpress.com/socrates-meets-jesus) | K |
| Bill & Ted's Excellent Adventure (1989) | Kurgu/komedi | Figürler 1988 San Dimas'a getirilir, ortamı bilmez, şaşırır; mizah figürün modern yaşama tepkisinden doğar. "So-Crates" tepkisi merak + yardım isteği | [Wikipedia](https://en.wikipedia.org/wiki/Bill_%26_Ted%27s_Excellent_Adventure), [VODzilla](https://vodzilla.co/reviews/vod-film-review-bill-teds-excellent-adventure/) | K |
| Character-LLM (Shao ve ark., EMNLP 2023) | LLM, ince ayar | Beethoven, Kleopatra, Sezar; profil + yeniden kurulmuş deneyim sahneleri; **protective experiences** (karakter dışı soruda "bilmiyorum" öğretme; ör. Beethoven'a Python sorusu) | [arXiv 2310.10158](https://arxiv.org/abs/2310.10158) | D |
| Historical Figures Chat (uygulama) | Ürün | Sınırlı veriyle "konuşmanın nasıl olabileceğini" tahmin eder; haberlerde olgu hataları, Nazi figürlerinin pişman gösterilmesi; geliştirici: "often wrong, and when wrong, confidently wrong" | [Rolling Stone](https://www.rollingstone.com/culture/culture-news/historical-figures-ai-chat-bot-lies-dead-people-1234664257/), [PopSci](https://www.popsci.com/technology/historical-figures-app-chatgpt-ethics/) (arama özetinden; sayfalar ayrıca açılmadı) | K |
| Hello History | Ürün | 400+ figür, kullanım öncesi doğrulama uyarısı; mimari ve "bugünü biliyor mu" bilgisi **yayımlanmamış** | [Hello History araştırma sayfası](https://www.hellohistory.ai/for-research), [freetech4teach](https://freetech4teach.teachermade.com/?p=645) | X (mimari bulunamadı) |
| Khanmigo tarihî figür sohbeti | Ürün | Üçüncü taraf site "Einstein, Shakespeare ile konuş" özelliğini listeliyor; kurulum/guardrail dokümanı bulunamadı | [KidsAiTools](https://www.kidsaitools.com/ko/tools/khanmigo-tutor) | X |
| Character.ai tarihî karakterler | Ürün | Bu aramada hiçbir kaynak bulunamadı | (yok) | X |
| Talkie-1930 / "Vintage LLM" | Araştırma | 1930 öncesi metinle eğitilmiş model; yine de "1930'a güvenilir biçimde oturmuş" değil, kendini ~1860 sayıyor (yazarın 100 denemesinin medyanı) | [Res Obscura](https://resobscura.substack.com/p/are-vintage-llms-the-start-of-a-new) (blog, bireysel görüş) | K |

## 2. Arızalar

| # | Arıza | Kanıt | Güven |
|---|---|---|---|
| A1 | **Anachronistic compositing:** model, figürü popüler kültür bileşimiyle (ör. Hamilton müzikali duygu yapısı) konuşturur; belgesel kayıt yerine sonradan kurulmuş anlatı | [AI Engineer talk, Miranda Hypothesis](https://ai.engineer/talks/the-miranda-hypothesis-how-hamilton-the-musical-poisoned-your-persona-evals). Talkta sonuç raporlanmadı, tasarım ve yorum; tek kanıt yazarın okuması | Düşük-orta |
| A2 | **Bilgi sınırı ihlali:** rol-oyunda figür ölümünden sonrasını bilir. Çekimserlik ölüm sonrası: Llama %18,7, Claude %9,6, Gemma ve GPT-4.1 %3 altı; Llama'da ölüm sonrası yanıt oranı %93,8 | [Concept Incongruence, arXiv 2505.14905](https://arxiv.org/html/2505.14905) (100 figür, 1890-1993) | Yüksek (hakemsiz ön baskı, tek çalışma) |
| A3 | **Rol-oyunu dünya bilgisini bozar:** rol-oyunda zaman temsili kayar (Llama ölüm yılı RMSE 2,6'dan 10,8 yıla; genel zamansal soru doğruluğu %85,0'dan %38,6'ya) | aynı makale | Yüksek (bir model ailesi) |
| A4 | **Fark etme ama uymama:** model sınırı tanır, yine de olgusal yanıt verir ("compliance failure"), bilgiyi bastıramaz | [CHARM, arXiv 2609.01352](https://arxiv.org/abs/2609.01352) (özet düzeyi, 40 karakter, 6 LLM) | Orta (yalnız özet okundu) |
| A5 | **Nokta-zamanı halüsinasyon:** GPT-4o sıfır-atış tutarlılığı ort. %64,5; gelecek-tipi doğruluk %46,0. Kısıtsız RAG gelecek bilgisini içeri sızdırarak durumu kötüleştirebilir | [TimeChara, arXiv 2405.18027](https://arxiv.org/html/2405.18027v1) (Harry Potter, LotR vb., 14 karakter) | Yüksek (kurgu karakter, tarihsel değil) |
| A6 | **Kesim talimatı doğrudan sorulanda işler, dolaylıda düşer;** zincirleme düşünce (CoT) sızıntıyı artırabilir (GPT-4o Hard 0,505 iken ZS-CoT 0,251) | [Can LLMs Be Constrained to the Past?](https://www.alphaxiv.org/abs/2606.05804.md) (alphaxiv özeti) | Orta |
| A7 | **Persona çerçevesi ("bugün X tarihi") açık talimattan ("X sonrası bilgiyi kullanma") daha çok sızdırır** | [arXiv 2605.14636](https://arxiv.org/pdf/2605.14636) (yalnız arama özeti) | Düşük-orta |
| A8 | **Güvenle yanlış / aklama:** olgu hatası, rahatsız edici figürlerin pişman gösterilmesi | Rolling Stone, PopSci (yukarıda) | Orta |
| A9 | **Modern değer yükleme (ventriloquism):** model modern kaygı, jargon ve analiz çerçevesini figüre enterpole eder. "Ventriloquism" terimiyle akademik kaynak **bulunamadı**; yalnız bir Substack denemesi bu iddiayı yapıyor. Kanıtlı kısım: persona tabanlı tarih yeniden anlatımları aynı olayı çelişkili çerçeveler ([EMNLP 2025 makalesi, arama özeti](https://repositum.tuwien.at/handle/20.500.12708/200467?mode=full) ile birlikte) | [Res Obscura](https://resobscura.substack.com/p/are-vintage-llms-the-start-of-a-new): "no privileged access to the inner lives" | Düşük (terim), orta (olgu) |
| A10 | **Kaynak-sız görüş:** figür adına olmayan ifade üretilir; Platon-Sokrates ayrımı bu sorunun felsefedeki karşılığı (SEP). Ölçüt: Prism Experiment tasarımında "belgesel tutarlılık" %35, "anakronizm tespiti" %40 ağırlık (tasarım, sonuç yok) | SEP, AI Engineer talk | Orta |

## 3. Tasarım kuralları (gerekçeli)

Her kural: kural, gerekçe, kanıt sınıfı. [T] = kanıttan çıkarım, doğrudan test edilmedi.

**K-1. Bilgi ayrımı iki katmanlı kur: "dünyayı bilen" ve "kendi görüşü"ni ayır.** Sokrates bugünün genel olgusunu bilir (bu tasarım tercihi), ama bir konuda **kendi pozisyonunu** bildirmez: soru sorar. Gerekçe: Sokrates'in tarihsel görüşü zaten kaynaklarda tartışmalı (SEP §2); elenktik yöntem pozisyon yerine soru üretir, "uydurma görüş" riskini yapıdan düşürür. [T] Sınıf: D (SEP) + [T].

**K-2. Her tahmin etiketli ve kaynağa bağlı: "Sokrates bunu söylerdi" yerine "Platon'un X diyalogunda Y soruluyor, o yöntemle bu soruya şunu sorardım".** Gerekçe: Platon-ağızlık sorunu (SEP) ve Prism tasarımındaki belgesel tutarlılık ölçütü; kaynak yoksa görüşü "bilmiyorum, tahmin" diye işaretle. Sınıf: K.

**K-3. Açık, kısa, olumlu bilgi sınırı yaz; persona çerçevesine güvenme.** "Bugünün genel bilgisini bilirsin" tek cümle + "kendi tarihsel görüşünü yalnız kaynak kartı varsa bildirirsin". Gerekçe: açık talimat, "bugün X tarihi" persona çerçevesinden daha az sızdırır (A7); Concept Incongruence'ta açık spesifikasyon çekimserliği +%75-88 artırdı (Claude +%88,4) ama genel doğruluğu −%7,3 (Claude), −%13,7 (GPT) düşürdü. Sınıf: D (Concept Incongruence), K (A7).

**K-4. Sınır yönünü tersine çevirince de "tanı ama uy" kuralı gerek.** Sokrates'in bildiği alan açık yazılmazsa model ya her şeyi bilen asistana (rol kaybı) ya da hiçbir şeyi bilmeyen figüre (sahte cehalet) kayar. CHARM'daki "fark eder ama uymaz" (A4) bunun simetriği: sınırı belirtmek yetmez, davranışa dönüşmesi gerekir. Kural: bildiğini örnekle ve soruyla göster, bilgi dökümü yapma. Sınıf: [T].

**K-5. Terimi bil, jargonla konuşma: "yapay zekâ" yerine örnekle tarif et, sorulursa terimi kullan.** Gerekçe: A9 (modern jargon ve çerçeve yükleme), Bill & Ted'de komedi/öğrenme figürün **kendi dünyasından** modern şeyi tarif etmesinden doğar. Test: kullanıcı terimi söylerse Sokrates tanıdığını gösterir ("senin dediğin mekanizmayı şöyle anlıyorum:") ama kendi cümlesinde kendi benzetmesini kullanır. Sınıf: K [T].

**K-6. Anakronizmin tersini de test et.** Üç test sınıfı: (a) bugün genel olgusunu **bilmeli** (ör. bir telefonu tarif eder), bilmiyormuş gibi davranırsa hata; (b) kendi ölümünden sonraki **kişisel görüşü uydurmamalı** (ör. "Kant hakkında ne düşünürdün" → soruyla yanıt, kesin hüküm yok); (c) ton: modern argo, kurumsal asistan sesi yok. Gerekçe: TimeChara'daki dört sınıf (future/past-absence/past-presence/past-only) ve Character-LLM'in değerlendirme alanları (kişilik, hafıza, tutarlılık, değerler, halüsinasyon). Sınıf: D (taksonomi), [T] (ters çevirme).

**K-7. Ton kimliği sabit, bilgi kapısı kart-bazlı.** Sabit ve her zaman yüklü: elenktik yöntem, hitap, ironi, üslup. Değişen ve koşullu: bugünün konu verisi. Gerekçe: SillyTavern'in "constant" ve "keyword" ayrımı ile aynı desen (Bölüm 4); Output style her istekte gönderilir, kart ise gerektiğinde yüklenir. Sınıf: D (SillyTavern, Claude Code docs), [T].

**K-8. Sızıntı literatürünü yönü ters olarak oku; geri çevrilemeyen tek ders "sınırı konuşma boyunca yenile".** CoT/uzun akıl yürütme sızıntıyı artırabilir (A6) ve model uzun konuşmada rolden çıkar. Kural: ajan her kritik yanıttan önce (a) "şu an hangi bilgiyi kullanıyorum, bugünün olgusu mu, Sokrates'in tarihsel kaynağı mı" kısa iç denetimi yapar (Self-Recall'ın bizdeki eşi: kısa ara çıktı, uzun değil). Sınıf: K (alphaxiv özeti), [T].

**K-9. Rahatsız edici ya da tartışmalı konularda "tek ses" yerine kayıt göster.** A8 (aklama) ve A1 (tek boyutlu karşıt): Sokrates'in kendi ölüm mahkûmiyetine tepkisi gibi yerlerde Platon (Apologia) ve Xenophon'un farklı anlatımları kayıtlı. Kural: çelişen kaynak varsa ikisi de anılır. Sınıf: D (SEP: Xenophon pastiş, Aristophanes karikatür).

**K-10. Kullanıcıya "bu bir rol-oyunu, tarihsel Sokrates değil" bildirimi tek kez, oturum başında.** Hello History ve Historical Figures Chat'in ortak uyarı deseni; ayrıca Vintage LLM yazarı modelin "iç dünyaya erişimi yok" der. Yineleme rol akışını bozar. Sınıf: K.

**K-11. Değerlendirme: dedikodu değil, preregistered örnek soru seti.** Kişilik uyumu (InCharacter %80,7) tarihsel sadakati ölçmez; kendi soru setimiz (bilmeli / bilmemeli / uydurmamalı üç kova) hakem ajanla maskeli koşar. Sınıf: K (talk iddiası), [T].

## 4. Bağlam verisi biçimi önerisi

**Olgu zemini (D):**
- SillyTavern: keywords ve başlıklar bağlama girmez, içerik **kendi başına anlaşılır** olmalı; kısa tut; **constant** entry her zaman yüklenir, anahtar eşleşenler bütçe dolana kadar; bütçe dolunca eşleşse bile yeni entry eklenmez ([SillyTavern World Info docs](https://docs.sillytavern.app/usage/worldinfo.md)). Varsayılan bütçe sayısı resmi dokümanda **yok**; üçüncü taraf bir rehber %25 diyor (doğrulanmadı).
- Claude Code **output style:** tek Markdown dosyası (`.claude/output-styles/`), talimatı her istekte gönderilir, **alt-ajanlar** (fork hariç) kendi system prompt'unu çalıştırır, yani output style onları etkilemez ([Output styles docs](https://code.claude.com/docs/en/output-styles)). Dosyada başka dosya import özelliği dokümanda **yok**.
- Claude Code **CLAUDE.md:** `@yol/dosya` ile import edilir, göreli yol içeren dosyaya göre çözülür, özyineleme **en çok dört atlama**; import edilen dosya **bağlam maliyetini düşürmez**, CLAUDE.md ile birlikte yüklenir; tek dosya için 200 satır altı önerilir; yalnız bölüme ait kural `.claude/rules/` ile yola göre yüklenir ([Memory docs](https://code.claude.com/docs/en/memory)).

**Öneri (tasarım, [T]):** iki katman, kart sayısı küçük.

1. **Çekirdek (tek dosya, sabit):** Sokrates kimliği, yöntem, ton, hitap, bilgi sınırı kuralları (K-1 ila K-6), kart kullanım kuralı. Hedef: 150 satır altı (CLAUDE.md önerisiyle uyumlu, deneysel sınır [?]). Output style olarak ya da ajan dosyasının gövdesi olarak tutulur.
2. **Kaynak kartları (ayrı dosyalar, koşullu):** konu başına **bir** kart. Her kart kendi başına anlaşılır (SillyTavern kuralı).

Kart şablonu:

```
# KART: <konu adı>
ANAHTARLAR: <konu kelimeleri, eş anlamlılar>
TUTUM (Sokrates'in sorgu hamlesi): <2-4 soru kalıbı, Platon diyalogu atfıyla>
BUGUNKU VERI: <3-6 olgu cümlesi, tarihli, kaynaklı>
TAHMIN (etiketli): <"Tahmin:" ile başlayan 1-2 cümle; hangi diyaloğa dayandığı>
SINIR: <bu konuda uydurmayacağı şeyler>
KAYNAK: <Platon/Xenophon/ikincil, URL ya da bölüm>
```

**Yükleme yolu:**
- Kartlar `kartlar/` altında, `@kartlar/<konu>.md` ile CLAUDE.md'de import edilebilir (tüm kartlar her zaman yüklenir, maliyet düşmez) **ya da** alt-ajan `Read` aracıyla konu eşleşince okur (yalnız `sokrates` ajanı `Read` aracına sahip; bu, koşullu yüklemeye uyar). İkinci yol bütçe açısından üstündür, ama okuma kararı modele kalır (deterministik değil).
- Kaç kart: kanıtlı bir sayı yok. Taslak: **8 ila 15 kart** ile başla (konu sayısına göre [?], deneysel); her kart ≤ 25 satır. Ölç: kart kullanım oranı, "sızıntı" ve "uydurma" kovaları (K-11), ardından kart ekle.
- Tek dosyada (output style) mi: çekirdek için evet; kart verisi için hayır, çünkü output style dosyasında import yolu yok ve her istekte tamamı gönderilir.

## 5. D/K/X

D = doğrulandı (birincil kaynak okundu), K = kısmi (özet ya da dolaylı kaynak), X = bulunamadı ya da doğrulanamadı.

| İddia | Sınıf | Not |
|---|---|---|
| Platon Sokrates'e kendi görüşünü söyletir (mouthpiece) | D | SEP §2.2 |
| Concept Incongruence rakamları (çekimserlik, RMSE, doğruluk düşüşü) | D | arXiv HTML okundu; tek çalışma, hakemsiz olabilir |
| TimeChara rakamları (%64,5, %46,0, %82,2, %87,5) | D | arXiv HTML'nin ilk 100k karakteri; kurgu karakter |
| Character-LLM protective experiences; <100 sahne yeterli, ~1,6K sahne/karakter | D | arXiv HTML ilk bölüm; nicel ablation yok, yalnız nitel örnek |
| Output style / CLAUDE.md import teknik detayları | D | Claude Code resmi dokümanı |
| SillyTavern world info mekanikleri | D | Resmî doküman |
| CHARM temporal bulgusu (compliance failure) | K | Yalnız özet; sayılar okunmadı |
| Recall-based prompting (SR→QR) etkisi | K | alphaxiv özeti |
| Persona çerçevesi açık talimattan çok sızdırır (arXiv 2605.14636) | K | Yalnız arama özeti; makale açılmadı |
| ExAnte "~%90 sızıntı" | K | Arama özetinde var, ExAnte özet sayfasında yok; bu raporda rakam olarak kullanılmadı |
| Hamilton/Lincoln compositing | K | Talk, sonuç raporlanmamış, konuşmacı yorumu |
| Historical Figures Chat eleştirileri (Hoover, Nazi aklama) | K | Arama özeti, sayfa ayrıca okunmadı |
| Kreeft yöntemi: Sokrates saf akılla modern yazarı sorgular | K | Yayıncı/okur özetleri; ön söz okunmadı; Freud'un ayrı kitabı doğrulanamadı |
| Bill & Ted komedi tekniği kasıtlı "fish out of water" mı | K | Olay örgüsünden çıkarım, kaynak o terimi kullanmıyor |
| Hello History, Khanmigo, Character.ai: bugünü biliyor mu, nasıl kurulmuş | **X** | Hiçbir resmî kaynakta mimari bulunamadı |
| "Ventriloquism" akademik terim | **X** | Kaynak yok; yalnız blog düzeyi iddia |
| Counterfactual persona "what would X think" tahmin kalitesi üzerine ölçüm | **X** | Doğrudan ölçüm çalışması bulunamadı; Prism Experiment yalnız tasarım |
| Optimal kart sayısı (8-15) | **X** | Kanıtsız taslak [?]; ölçümle ayarlanmalı |

**Sınır ve geçerlilik:** AS-OF 2026-10-29. Çoğu kaynak ön baskı ve özet düzeyi; Hello History, Khanmigo, Character.ai satırları bu aramada boş çıktı, ayrı bir turda ürün dokümanları ve basın incelemeleriyle doldurulabilir. Tasarım kuralları [T] etiketliyse kanıttan çıkarımdır, Sokrates ajanında ölçülmeden "doğrulandı" sayılmaz.
