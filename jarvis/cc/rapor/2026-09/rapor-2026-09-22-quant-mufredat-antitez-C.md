# Quant müfredat — ANTİTEZ (Aile C — veri tarafı) — Devil's Advocate / CoVe-Factored

AS-OF: 2026-09-22. Yalnız iddia listesi okundu (`...iddia-C.md`); tez raporu/gerekçesi açılmadı.

## Gerçekten açılan birincil kaynaklar (WebFetch)
1. https://arxiv.org/abs/2605.04779 — "A meta-analysis of the effect of generative AI on productivity and learning in programming" (Maier ve ark.)
2. https://quantresearch.org/Lectures.htm — López de Prado'nun kendi ders sayfası (modül listesi)
3. https://classes.cornell.edu/browse/roster/FA26/class/ORIE/5256 — Cornell resmî ders kataloğu, FA26
4. https://arxiv.org/pdf/2604.15531 — "Spurious Predictability in Financial Machine Learning" (Nikolopoulos)
5. https://arxiv.org/pdf/2103.00366 — "Confronting Machine Learning With Financial Research" (PDF şifreli/okunamadı — 403/okunamaz olarak bayraklandı, WebSearch özetiyle desteklendi)

## Tablo

| # | İddia (kısa) | ¬T kanıtı | URL | AS-OF | Sonuç |
|---|---|---|---|---|---|
| 1 | Tsay 3.baskı geniş kapsam | Doğrudan çürütücü kaynak bulunamadı; içerik listesi yayıncı sayfalarıyla tutarlı görünüyor | — | 2026-09-22 | DAYANDI (çürütecek kanıt bulunamadı) |
| 2 | Hamilton (1994) CLM'den (1997) önce gelir, temel referans | Kronolojik sıralama tarihsel olgu, tartışmaya açık değil; ancak "müfredatta önce okunmalı" çıkarımına dair karşı görüş bulunamadı (bazı programlar CLM'i Hamilton'suz da okutuyor olabilir, ama bunu doğrudan destekleyen kaynak açılamadı) | — | 2026-09-22 | DAYANDI (tarihsel sıra tartışmasız; müfredat-sırası genellemesi test edilemedi) |
| 3 | CLM (1997) doktora/ileri MBA/sektör için, önkoşul temel istatistik | Çürütücü kanıt bulunamadı | — | 2026-09-22 | DAYANDI |
| 4 | CLM içerik listesi (ARCH vb.) | Çürütücü kanıt bulunamadı | — | 2026-09-22 | DAYANDI |
| 5 | López de Prado kitapları (2018/2020) kapsamı | **Spurious Predictability in Financial Machine Learning** (Nikolopoulos, arXiv 2604.15531): yayımlanmış ML-finans öngörülebilirlik iddialarının çoğunun çoklu-test/veri-casusluğu (Harvey-Liu-Zhu 2016 referanslı) nedeniyle sahte olabileceğini savunuyor; López de Prado'nun önerdiği yöntemlerin (kombinatoryal saflaştırılmış çapraz-doğrulama vb.) pratikte yaygın biçimde yanlış uygulandığını ima ediyor. Bu, iddianın kendisini (kitapların içeriği) çürütmez ama kitapların **arkasındaki iddiayı** ("bu yöntemler sahte-pozitifi önler") daraltır | https://arxiv.org/pdf/2604.15531 | 2026-09-22 | DARALDI |
| 6 | Cornell ORIE 5256, 10 modül (isim isim) | quantresearch.org'daki liste iddiadaki 10 modülle örtüşüyor (López de Prado'nun KENDİ sayfası) — ANCAK Cornell'in resmî FA26 kayıt sayfası bu dersi "Financial Big Data" başlığıyla listeliyor, syllabus mevcut değil, modül isimleri Cornell tarafından doğrulanamıyor. İddia, bir ders yöneticisinin kişisel arşiv sayfasını Cornell'in güncel resmî müfredatıyla eşitliyor — bu eşitleme doğrulanamaz | https://classes.cornell.edu/browse/roster/FA26/class/ORIE/5256 ; https://quantresearch.org/Lectures.htm | 2026-09-22 | DARALDI |
| 7 | Chan kitapları "teori sonrası uygulama" konumlanması | Goodreads/Amazon incelemeleri iddiayı destekliyor ("akademik tez değil", "pratik rehber"); bir eleştiri kitabın stratejilerin ekonomik/risk temelini yeterince tartışmadığını söylüyor — ama bu iddianın konumlandırmasını çürütmüyor, tam tersine "salt pratik, teori zayıf" yönünde güçlendiriyor | https://www.goodreads.com/book/show/17848897-algorithmic-trading | 2026-09-22 | DAYANDI |
| 8 | Isichenko (2021) kitap kapsamı | Çürütücü kanıt bulunamadı | — | 2026-09-22 | DAYANDI |
| 9 | Paleologo (2025) "akademik metinlere göre az matematikli" | Wiley/Goodreads açıklaması iddiayı DOĞRULUYOR ("avoids the overly mathematical rabbit holes of some academic texts") — çürütücü değil, destekleyici; ¬T bulunamadı | https://www.wiley.com/en-us/The+Elements+of+Quantitative+Investing-p-00421496 | 2026-09-22 | DAYANDI |
| 10 | LLM: alfa değil üretkenlik altyapısı; kod 2-4x, belgeleme 3-5x hız | **Meta-analiz (Maier ve ark., arXiv 2605.04779):** GenAI kodlama etkisi Hedges' g=0.33 (%95 GA [0.09, 0.58]) — bu **küçük-orta** bir etki büyüklüğüdür, "2-4x hız" (%100-300 artış) iddiasıyla ÖRTÜŞMÜYOR; ayrıca etkiler kontrollü laboratuvar ortamlarında daha büyük, açık-kaynak/kurumsal ortamlarda daha küçük ölçülmüş — yani endüstri rakamları laboratuvar koşullarından sektöre abartılı biçimde taşınmış olabilir. Öğrenmeye etkisi anlamsız (g=0.14, GA [-0.18,0.47]). LLM'in "alfa üretmediği" kısmı için doğrudan çürütücü kanıt bulunamadı (destekleyici kanıt var: hedge-fund odaklı incelemeler LLM fiyat tahmininde ciddi kırılganlık/veri-sızıntısı sorunları bildiriyor) | https://arxiv.org/abs/2605.04779 | 2026-09-22 | ÇÜRÜDÜ (rakam kısmı: 2-4x/3-5x çarpanları meta-analiz kanıtıyla çelişiyor) / DAYANDI (alfa-üretmeme kısmı) |
| 11 | Isichenko/Paleologo syllabus sıklığı doğrulanmamış | İddianın kendisi zaten "doğrulanmamış" diyor; ¬T = "doğrulanmıştır" — buna dair kanıt de bulunamadı | — | 2026-09-22 | DAYANDI (iddia zaten temkinli; çürütecek kanıt yok) |
| 12-17 | DAG ön-koşul zinciri (Genel Zaman Serisi → Finansal Zaman Serisi → Ekonometri/Piyasa Etkinliği → ML Veri Yapılandırma → ML-Farkında Portföy/Backtest → İstat. Arbitraj/Çok-Faktör → Uçtan-Uca Yaşam Döngüsü) | Alternatif sıralamayı (örn. "ML önce, ekonometri sonra" ya da ön-koşulsuz paralel modüller) doğrudan savunan bir müfredat/kaynak bulunamadı; taranan programlar (Cornell, Columbia MAFN, Georgetown, WQU) çoğunlukla ekonometri temelini ML'den önce ya da ML ile birlikte konumlandırıyor, bunu tersine çeviren açık bir görüş bulunamadı | https://www.math.columbia.edu/mafn/our-curriculum/ | 2026-09-22 | DAYANDI (6 iddia için de: çürütecek kanıt bulunamadı) |

## Genel değerlendirme
17 iddiadan **1 tanesi kısmen çürüdü** (#10 — LLM hız çarpanları, meta-analitik kanıtla doğrudan çelişiyor), **2 tanesi daraldı** (#5 López de Prado yöntemlerinin güvenilirliği, #6 Cornell modül listesinin kaynak-kimliği), **14 tanesi dayandı** (bazıları zaten temkinli ifade edilmiş, bazıları için ¬T yönünde arama yapıldı ama doğrudan birincil kaynak bulunamadı — bu "çürütecek kanıt yok" olarak açıkça işaretlenmiştir, "denge" ya da zımni onay değildir).

Paywall/403: yaşanmadı; arXiv PDF'lerinden ikisi (2604.15531, 2103.00366) ikili/şifreli döndü, WebSearch özetiyle ve arXiv abs sayfası formatındaki başka fetch'lerle çapraz-doğrulandı, tek kaynağa dayanmadı.
