# Hakem raporu — quant müfredat Atlas koşumu (2026-09-22; `subagent_type: hakem`, Opus 5.5 eskalasyon (b): V26 tez-D `TUTMADI` 3/5 ≥ 3 → çağıran Jarvis eskalasyonu; hakemin `[sapma]` notu eskalasyon gerekçesini görmediği içindir, kural sağlanmıştır)

`[tip: hakem | kaynak: jarvis-terminal 09-22 | tarih: 2026-09-22 | hedef: cc/rapor | sema: v2 | koken: hakem/claude-opus-5-5/2026-09-22]`

Aşağısı hakemin döndürdüğü metnin aynen kaydıdır (çağıran yazdı; hakem yazmaz).

---

# Maskeli hakem raporu · quant müfredat ve konu-bağımlılık DAG'ı

**Tarih:** 2026-09-22 (sistem saati) · **Rol:** maskeli hakem (atlas-kosum aşama 3; Karar 103 M1) · **Model+effort:** Opus 5.5, düşük effort. Ajan tanımı Sonnet 5 varsayılanını öngörür; bu koşumun Opus 5.5 ile çalışması ne Salih beyanına ne de `TUTMADI` ≥3 kuralına dayanıyor. `[sapma]` olarak kayda geçer. · **Girdi:** 8 rapor (tez A-D, antitez A-D) ve 40 satırlık V26 sondajı: 25 `TUTTU`, 7 `TUTMADI`, 8 `ERİŞİLEMEDİ`. **K tavanı** 4 rapora uygulandı: tez-A, tez-B, tez-D ve antitez-A.

**Kendi doğrulamam:** bütçe 8/7 kullanıldı, çekimler 2026-09-22.
- [Oxford MCF ders bileşenleri](https://www.maths.ox.ac.uk/members/students/postgraduate-courses/msc-mcf/mscmcf-course-components)
- [QuantStart okuma listesi](https://www.quantstart.com/articles/Quantitative-Finance-Reading-List/)
- [arXiv 2604.15531](https://arxiv.org/abs/2604.15531)
- [ETH MSc QF](https://math.ethz.ch/studies/master-programmes/master-quantitative-finance.html)
- WebSearch: [Grinold-Kahn içindekiler](https://www.amazon.com/Active-Portfolio-Management-Quantitative-Controlling/dp/0070248826), [Morningstar-CRSP](https://newsroom.morningstar.com/news/news-details/2026/Morningstar-Completes-Acquisition-of-CRSP-and-Extends-Relationship-with-Vanguard/default.aspx), [UZH önkoşul sayfası](https://www.msfinance.uzh.ch/en/admission/eligibilityandprerequisites.html). Arama özetleri en fazla K sayıldı.

## Usul beyanı
- **Maskeleme:** tez ve antitez kimliği hükme girmedi. Her satır "iddia + kanıt gücü" olarak tartıldı, kıyas aile başına ayrı yapıldı.
- **Maske ihlali:** emirde yok. V26 dosyasındaki "tez-C en sağlam aile" notu değerlendirme cümlesi; hükme sokulmadı.
- **V26 tavanı:** tavanlı raporların bulguları en fazla K. İstisna olarak kendi birincil çekimimle birebir doğruladığım üç nokta D aldı: A7, A8, A11.
- **Etiketler:** D = birincil kaynakta birebir, güncel ve adversarial turda ayakta. K = tek kaynak, ikincil ya da tavanlı. X = çürüdü ya da dayanaksız.
- **Kovalar:** "sağlam" = ayakta kalan (D ya da tavan kaynaklı K). "Daraldı" = yalnız yazılan koşulda doğru.
- **AS-OF:** tüm canlı iddialar için 2026-09-22 erişim tarihi.
- **Girdi dışı dosyalar:** `iddia-{A..D}.md` emirde yok, okunmadı.

### V26 düzeltmeleri
| # | V26 ya da girdi hükmü | Kendi bulgum | Etki |
|---|---|---|---|
| 1 | antitez-A #10: Oxford 2 haftalık 5 giriş dersi `ÇÜRÜDÜ` | Tezin gösterdiği sayfa birebir veriyor: "starts two weeks before Michaelmas term with five introductory courses" | Antitez hükmü düştü; A7 = D |
| 2 | antitez-B #1: "QuantStart 2026 listesinde Shreve hâlâ var" | Sayfa 2013 tarihli ve Shreve'i hiç anmıyor | B1 düştü; V26 notu 1 teyit edildi |
| 3 | antitez-C #5: arXiv 2604.15531 López de Prado yöntemlerini daraltıyor | Özette López de Prado ya da CPCV geçmiyor | Daraltma dayanaksız (X); C5 ayakta |
| 4 | Oxford tezi için %30 ağırlık, 25-40 sayfa | Sayfa sayfa sınırını ve ağırlığı vermiyor | A9 = X |
| 5 | ETH-UZH hazırlık kursu yok | ETH sayfası bu konuda sessiz | A13 daraldı |

## İddia tablosu
Tüm satırların AS-OF'u 2026-09-22; model sürümü uygulanmaz.

**Aile A · programlar**
| # | İddia | Kanıt | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|
| A1 | CMU önkoşulları: Calc I-II, LinAlg, olasılık, OOP dili | cmu.edu/mscf/admissions | K | sağlam | Antitez teyit etti, tavanlı |
| A2 | CMU Prep 4 hafta | mscf-math-prep | X | düştü | 3 hafta; V26 ve antitez birlikte |
| A3 | ML II (46927) önkoşulu 46921+46923+46926 | kurs sayfası | K | daraldı | Birincil sayfa listelemiyor, yalnız dolaylı liste |
| A4 | Baruch 36 kredi (12+24), 2018 kayması | yalnız WebSearch | K | daraldı | Birincil sayfaya iki koşumda da erişilemedi |
| A5 | NYU Core L1 5 ders, L2, 5 seçmeli/15 kredi, 3 haftalık bootcamp | NYU academics | K | sağlam | V26 `TUTTU`, tavanlı |
| A6 | Columbia MSFE yapısı | CBS/IEOR karışık | K | daraldı | Program kimliği belirsiz; seminer 16 dersin içinde |
| A7 | Oxford: Michaelmas öncesi 2 hafta, 5 giriş dersi | kendi çekimim | D | sağlam | Birebir |
| A8 | Oxford Michaelmas çekirdeği (4 + C++1), Hilary çekirdeği (4) + seçmeliler | kendi çekimim | D | sağlam | Birebir |
| A9 | Oxford tezi %30, 25-40 sayfa | course-components | X | düştü | Gösterilen kaynakta yok. Antitezin "≤40 sayfa"sı da bu URL'de yok `[?]` |
| A10 | Princeton 5+11 / 10 ders, çekirdek dönem sırası | bcf.princeton.edu | K | sağlam | V26 `TUTTU`, tavanlı |
| A11 | ETH-UZH 36+24+30 = 90 ECTS | kendi çekimim | D | sağlam | Birebir |
| A12 | ETH-UZH ölçü teorisi ve stokastik hesap "önerilir" | UZH (arama özeti) | K | sağlam | İkincil özet |
| A13 | ETH-UZH'de hazırlık kursu yok | ETH sayfası | K | daraldı | Kaynak sessiz; yokluk kanıtlanmadı |
| A14 | Ortak desen: hazırlık → çekirdek-1 → çekirdek-2 → seçmeli → tez | A5/A7/A8/A10 | K | daraldı | Hazırlık bloğu CMU, NYU ve Oxford'da var; Princeton'da belirtilmemiş |

**Aile B · klasik kaynak sırası**
| # | İddia | Kanıt | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|
| B1 | Shreve I-II "omurga" | QuantStart | X | düştü | Kaynakta Shreve yok; iddia olarak dayanaksız |
| B2 | Joshi: "stokastik hesap göründüğünden az önemli"; Oksendal, Karatzas-Shreve, Chung | magmasystems (2006) | K | sağlam | V26 `TUTTU` ×2; ikincil barındırıcı, 2006 metni |
| B3 | Joshi'nin Hull, Baxter-Rennie, Wilmott yorumları ve kendi kitabı (2003) | aynı | K | sağlam | V26 `TUTTU`; eski kuşak ("o zaman böyle") |
| B4 | Björk'te ayrı ölçü teorisi bölümleri | OUP (boş dönüş) | K | daraldı | İçindekiler doğrulanamadı |
| B5 | Hull için QuantStart'ın okuma tavsiyesi | QuantStart | K | daraldı | Sayfa 2013 tarihli, Hull 8. baskı; güncel değil |
| B6 | QuantNet MFE öncesi kitap listesi | 403 | K | daraldı | Yalnız arama özeti |
| B7 | Grinold-Kahn "3 kısım" | arama özeti | K | daraldı | 4. kısım (Implementation) eksik; liste eksik |
| B8 | Jorion → Meucci sırası | model hafızası `[?]` | X | düştü | Dayanaksız |
| B9 | Björk-Shreve kıyası "hiçbir kaynakta yok" / "forumlar kıyaslıyor" | 403 snippet | K | çelişkili | İki taraf da birincil kaynaksız |
| B10 | Stevens FE630 stokastik hesabı önkoşul sayıyor | fsc.stevens.edu | D | sağlam | V26 `TUTTU`, birincil, tavansız |
| B11 | Columbia MAFN sırası zinciri destekliyor | math.columbia.edu | K | daraldı | Sondajlanmadı; yalnız ders listesi |

**Aile C · veri tarafı**
| # | İddia | Kanıt | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|
| C1 | Campbell-Lo-MacKinlay: 1997 (basım 1996-12-29), içerik, önkoşul | press.princeton.edu | D | sağlam | V26 `TUTTU`, birincil |
| C2 | Tsay 3. baskı (2010), içerik | wiley.com | D | sağlam | V26 `TUTTU` |
| C3 | Hamilton (1994), CLM'den önce okunur | Amazon karşılaştırması | K | daraldı | Kronoloji doğru; müfredat sırası test edilmedi |
| C4 | López de Prado, Cornell ORIE 5256, 10 modül | quantresearch.org + Cornell FA26 | K | daraldı | Yazarın sitesinde D; Cornell FA26 kataloğu "Financial Big Data", syllabus yok |
| C5 | López de Prado kitaplarının kapsamı | Wiley/CUP özeti | K | sağlam | Antitezin daraltması dayanaksız çıktı (düzeltme 3) |
| C6 | LLM kodda 2-4x, belgelemede 3-5x hız | zerve.ai ↔ arXiv 2605.04779 | K | çelişkili | Satıcı blogu, tek kaynak. g=0.33 standart etki büyüklüğü, hız çarpanı değil: karşılaştırılamaz |
| C7 | LLM alfa üretmiyor, üretkenlik altyapısı | zerve.ai | K | daraldı | Yalnız satıcı görüşü; çürütülmedi |
| C8 | Chan kitapları pratik konumda | Goodreads | K | sağlam | İkincil |
| C9 | Isichenko (2021), Paleologo (2025, az matematik) | Wiley | K | sağlam | Yayıncı metni |
| C10 | Meta-analiz: kodlamada g=0.33 [0.09, 0.58], öğrenmede g=0.14 [-0.18, 0.47] | arXiv 2605.04779 | D | sağlam | V26 `TUTTU`, 2026 |

**Aile D · uygulama ve kariyer**
| # | İddia | Kanıt | Etiket | Kova | Gerekçe |
|---|---|---|---|---|---|
| D1 | vectorbt açık kaynağı bakım modunda, PRO ~$25/ay | GitHub README | K | daraldı | Bakım modu teyitli; fiyat doğrulanmadı `[?]` |
| D2 | backtrader bakımı durmuş | GitHub/PyPI | K | daraldı | PyPI 2023-04-19, master'da 2026-03-27'ye dek PR: yavaşlamış, durmamış |
| D3 | vectorbt + zipline + QuantConnect üçlüsü | bloglar | K | daraldı | Düşük yetkeli kaynaklar |
| D4 | QuantConnect Python ve C# destekliyor | QC docs | K | sağlam | Tavanlı |
| D5 | yfinance ticari kullanımda risk taşıyor | yfinance belgesi, Yahoo ToS | K | sağlam | İki kaynak |
| D6 | Polygon "görece pahalı" | massive.com/pricing | D | daraldı | Ücretsiz Basic ve $29/ay Starter var; yalnız üst katmanlar için doğru |
| D7 | Morningstar CRSP'yi satın aldı (2026-02-02, $365M) | arama özeti ve newsroom | K | sağlam | Birebir çekilmedi |
| D8 | CIZ formatı 2026'da devreye girdi, SIZ 2026'da kalkıyor | tidy-finance | X | düştü | Doğrusu: CIZ 2022, SIZ'in son güncellemesi 2024 sonu |
| D9 | Mikroyapı sırası: O'Hara → Harris → Hasbrouck → Bouchaud | ikincil | K | daraldı | Resmî sıra yok (yazar da söylüyor) |
| D10 | Mülakat kitabı çekirdek seti | bloglar | K | sağlam | İkincil |
| D11 | 150 MFAQ 2. baskı çekirdek kitap | fepress | K | daraldı | Güncel olan 3. baskı (2024, ISBN 978-1734531244) |
| D12 | Kadoa: 521 pozisyon, 59 firma, medyan $210k | kadoa.com | K | daraldı | Canlı sayfa; firma sayısı 59-60, AS-OF anlık |
| D13 | Türkiye'de tek örnek: Algocor | Boğaziçi kariyer | K | sağlam | İlan tarihsiz; ikinci örnek teyitsiz |
| D14 | Jane Street NY taban maaşı $300.000 | canlı ilan | D | sağlam | V26 `TUTTU` ×2, birincil |
| D15 | Researcher/trader/developer rol farkı, sınırlar bulanık | bloglar | K | sağlam | İkincil |
| D16 | Python akıcılığı asgari beklenti | quantvault | K | sağlam | Tek ikincil kaynak |

## DAG kenarları
Etiketler: D = birincil kaynakta açık önkoşul · K = dönem sırası ya da çıkarım · X = dayanaksız ya da ters yön.
| Kenar | Hüküm | Dayanak |
|---|---|---|
| Calc & LinAlg → Probability | K | Genel; öğrencide mevcut |
| Probability → Measure Theory | K, daraldı | UZH "exposure önerilir": tavsiye, önkoşul değil |
| Measure Theory → Stochastic Calculus | K, daraldı | Yalnız titiz yolda; Rutgers/Bayes/Stony Brook ölçü teorisiz işliyor (antitez-A, sentez) |
| Probability → Stats & Fin. Data Analysis | K | Oxford: giriş Probability, sonra Michaelmas Stats (dönem sırası) |
| Python → Financial Computing (C++) | K | Çıkarım |
| Computing → Numerical Methods | X | Oxford'da ikisi aynı dönem (Michaelmas), paralel |
| Stochastic Calculus → Derivatives | K | CMU 46971'in önkoşulu 46944 (tavanlı); Oxford'da aynı dönem |
| Derivatives → Fixed Income | X | Yön şüpheli: CMU'da Fixed Income (46956), 46971'in önkoşulu; Princeton'da FIN521, AP II'nin alternatifi |
| Stats → Econometrics / ML | K | Princeton: güz FIN505, bahar FIN504 (dönem sırası) |
| Derivatives + Numerical → Risk & Portfolio | X | NYU'da Risk & Portfolio, stokastik hesapla aynı Core L1'de |
| Risk & Portfolio → QRM | K | Çıkarım |
| Stochastic Calculus → Stochastic Control | K | Oxford Michaelmas'tan Hilary'ye (A8, D) |
| Econometrics / ML → Deep Learning | K | Oxford Hilary; önkoşul yazılı değil |
| FI + QRM + StochControl → Capstone | K, daraldı | Yalnız dönem sırası; iki taraf da resmî önkoşul bulamadı |
| Prob & Measure → Stochastic Calculus (B) | K | Joshi'nin Chung önerisi |
| Stochastic Calculus → Discrete / Binomial | X | Ters yön: binom model stokastik hesap gerektirmez; Shreve'de Vol I (kesikli) Vol II'den önce |
| Discrete → Continuous / Martingale | K | Shreve I→II yapısı (ikincil) |
| Martingale → PDE approach | K, daraldı | Joshi iki yaklaşımı alternatif sayıyor; sıra değil |
| PDE → Björk arbitrage framework | X | `[?]`, dayanaksız |
| Martingale → Portfolio & Active Management | K, daraldı | FE630 stokastik hesap istiyor (B10, D); Grinold-Kahn istemez |
| Portfolio → VaR → Meucci | X | B8; Meucci yalnız LinAlg + kalkülüs istiyor (antitez-B, K) |
| Probability → Hamilton → Tsay | K | Çıkarım |
| Tsay → CLM | K, daraldı | CLM'nin önkoşulu "temel istatistiksel yöntem" (C1, D); Tsay şart değil |
| CLM → ML (López de Prado) | K | ORIE modül 1 "ekonometri tuzakları" ile uyumlu |
| ML → Backtest / Portfolio Construction | D | López de Prado sitesindeki modül sırası (yazarın kendi sitesi) |
| → Isichenko → Paleologo | K, daraldı | Paleologo daha az matematikli; öne alınabilir |
| → LLM-augmented practice | K | Tek satıcı kaynağı (C6, C7) |
| Python → Data → Vectorized → Event-driven → QuantConnect | K, daraldı | Çerçeveler alternatif, zincir değil; kaynaklar düşük yetkeli |
| O'Hara → Harris → Hasbrouck | K | Resmî sıra yok (D9) |
| Stochastic Calculus + Probability → Interview prep → Job market | K | Çıkarım |

## Kovalar
- **Sağlam (24):** A1, A5, A7, A8, A10, A11, A12 · B2, B3, B10 · C1, C2, C5, C8, C9, C10 · D4, D5, D7, D10, D13, D14, D15, D16. D alanlar: A7, A8, A11, B10, C1, C2, C10, D14; kalanı tavan ya da ikincil kaynak yüzünden K.
- **Daraldı (20):** A3, A4, A6, A13, A14 · B4, B5, B6, B7, B11 · C3, C4, C7 · D1, D2, D3, D6, D9, D11, D12.
- **Düştü (5):** A2, A9, B1, B8, D8. Ayrıca iki antitez hükmü düştü: antitez-A #10 ve antitez-C #5.
- **Çelişkili (2):** B9 (Björk-Shreve kıyası var mı yok mu; iki taraf da birincil kaynaksız) · C6 (satıcı hız çarpanı ile meta-analiz etki büyüklüğü aynı birimde değil).

## m.16 işaretli çelişkiler
Emirde kanon alıntısı verilmedi. İşaretlenecek kanon çelişkisi yok.

## Hayatta-kalma
Toplam: 51 iddia · sağlam 24 / daraldı 20 / düştü 5 · çelişkili 2
| Aile | İddia | Sağlam | Daraldı | Düştü | Çelişkili |
|---|---|---|---|---|---|
| A | 14 | 7 | 5 | 2 | 0 |
| B | 11 | 3 | 5 | 2 | 1 |
| C | 10 | 6 | 3 | 0 | 1 |
| D | 16 | 8 | 7 | 1 | 0 |

DAG: 30 kenar · D 1 / K 24 (11'i daraldı) / X 5

## Hakem hata kaydı
Hafızaya giren madde (aynen): "Antitez çürütmesi: kaynak ve birim. Sondajlanmamış ÇÜRÜDÜ'de tezin URL'sini kendin çek; etki büyüklüğü ≠ hız çarpanı." Dosya: hakem ajan-hafızası `feedback-antitez-curutmesi-kaynak-ve-birim.md` (+ MEMORY.md dizin satırı).
