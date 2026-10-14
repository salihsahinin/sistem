# Veri rolleri ilan beceri taraması: Data Engineer, Data Analyst, Data Scientist

**AS-OF 2026-10-09** (sistem saati). Örneklem 2026-04 ile 2026-10-09 arası tarihli ya da taramada canlı görünen ilanlardan, ayrıca daha eski ilanlardan oluşur; her ilanın durumu tabloda yazılı. Kaynak çekimi ve sayım aynı gün yapıldı. Sayıların tamamı aşağıdaki 48 ilandan sayıldı (tablo 2 ve 3, `veri.py` içindeki kodlamadan üretildi); çıkarım ve boşluk tahminleri `[?]` ile işaretli.

## 1. Özet

- **N = 48 ilan**: Data Engineer (DE) 19, Data Analyst (DA) 16, Data Scientist (DS) 13. Bunların **29'u "güncel" alt küme (G)**: 2026-06 sonrası tarihli ya da taramada canlı (DE 11, DA 11, DS 7). Kalan 19'u süresi dolmuş, eski ya da tarihsiz (E). Her tabloda hem N=48 hem G sayımı var.
- Türkiye ilanı 13 (İstanbul 11, Ankara 2); bunların yalnız 3'ü (iyzico, Spyke Games, Trendyol) taramada canlıydı. Geri kalanı global/uzaktan Avrupa ve ABD.
- Çekirdek: **SQL 37/48 (%77)** ve **Python 39/48 (%81)** üç rolde de ilk iki sırada. DE'de sonraki dilim: bulut (10/19, %53), orkestrasyon (10/19, %53), veri modelleme (9/19, %47).
- Güncel DE alt kümesinde (N=11) bulut %73, orkestrasyon %73, SQL %82, Python %73: ilanlar eski örneklemden daha "platform" odaklı.
- Junior etiketli ilanların çoğu metinde 2+ yıl istiyor (Doodle, Matrix, ShippyPro, B&A, iyzico). Gerçek intern ilanı DE'de yalnız 3 (TikTok, Atlassian, Rocket; üçü de ABD/Avustralya, üçü de süresi dolmuş); bu ilanlar yalnız SQL + Python + temel veritabanı istiyor.

## 2. Yöntem

1. **Toplama.** WebSearch ile arama (araç yalnız ABD çıktısı veriyor, sonuç kalitesi düşük), ardından ilan sayfaları WebFetch ile açıldı. Canlı ilan listeleri için üç toplayıcı sayfa kullanıldı: remoterocketship.com (Avrupa junior DE, entry-level DA, junior DS filtreleri), builtin.com (remote entry-level data listesi), eudatajobs.com. Türkiye için builtin.com, lever (Trendyol), techcareer.net, kariyermerkezi.bogazici.edu.tr, webrazzi, career.io/qureos kayıtları açıldı.
2. **Çıkarım.** Her ilan sayfasından zorunlu ("requirements / must have / minimum qualifications") ve tercih ("nice to have / preferred / plus / advantage") beceriler ayrıştırıldı. Ayrıştırmayı WebFetch'in küçük modeli yaptı; ben etiketleri tek tek okuyup `veri.py` içine kodladım. **Etiketsiz ilanlarda** "Requirements" altındaki her şey zorunlu sayıldı; "veya" ile verilen alternatif listelerinde (ör. "Airflow veya Dagster") listelenen her araç sayıldı.
3. **Normalizasyon.** PySpark/Apache Spark/Databricks-Spark = Spark; Airflow/Dagster/Prefect/Composer = Orkestrasyon; BigQuery/Snowflake/Redshift ayrı tutuldu; AWS, Azure, GCP herhangi biri geçtiğinde ayrıca "Bulut (genel)" sayıldı; Great Expectations/Monte Carlo/birim testi = Veri kalitesi/test; Power BI/Tableau/Looker/Qlik/dashboard = BI/dashboard (araç adları ayrıca da sayıldı); Claude Code/Copilot/Cursor gibi araçlar = AI kodlama araçları; LLM/embedding/GenAI = LLM/GenAI.
4. **Sayım.** n/N bir becerinin ilanda (zorunlu ya da tercih bölümünde) geçme sayısıdır; "zorunlu bölümde n" yalnız zorunlu sayılanlar. Aynı beceri aynı ilanda bir kez sayıldı.
5. **İkincil kaynaklar** bölüm 7'de ayrı işaretli; ana sayımlara karışmadı.

## 2.1 Sınırlar (önemli)

- **Canlılık hedefi tam karşılanamadı.** Taramada LinkedIn, Kariyer.net ve Glassdoor ilan sayfalarına erişilemedi (giriş duvarı/403); Türkiye ilanlarının çoğu süresi dolmuş sayfalardan geldi. "Canlı" etiketi, o sayfanın tarama anında içerik göstermesi ve toplayıcıda Eylül/Ekim 2026 tarihli görünmesi demektir; başvuru açıklığı ayrıca doğrulanmadı.
- **Tarihler.** Toplayıcılar yıl göstermiyor ("09-28" gibi); sıralama ve "X gün önce" ifadelerinden 2026 çıkarıldı `[?]`. Bazı ilanlarda tarih yok (tabloda "tarih yok").
- **Örneklem küçük ve yanlı.** N=48 bir piyasa anketi değil. Uzaktan Avrupa ağırlıklı toplayıcı ilanları fazla temsil ediliyor; Türkiye alt kümesi N=13 ve çoğu eski. Rol başına yüzdeler ±1 ilan değişiminde 5-9 puan oynar.
- **Seviye etiketleri** toplayıcıdan geliyor ("Junior; Mid-level" iki etiketi birden basıyor); metindeki yıl şartı etiketten daha güvenilir kabul edildi ve tabloya yazıldı.
- **DA örneklemi** uzaktan/ABD ve çalışan-öğrenci ilanları içeriyor; birkaç DA ilanı (Eneba, NMS, GitBook) beceri listesi çok kısa olduğu için tabloda düşük yoğunlukta.
- Alt-ajan kullanılmadı; token/süre tahmini yazılmadı.

## 3. İlan tablosu (N=48)

Grup: G = güncel alt küme (2026-06 sonrası tarihli ya da canlı), E = eski, süresi dolmuş ya da tarihsiz. Tarihte yıl yazmıyorsa 2026 `[?]`. Seviye sütunu etiket + metindeki yıl şartı.

| ID | Rol | Şirket | Konum | Seviye | Tarih | Durum | Grup | URL |
|---|---|---|---|---|---|---|---|---|
| DE01 | DE | iyzico | İstanbul (uzaktan/hibrit) | Entry (etiket); metin 2-3 yıl | ~2026-09 (1 ay önce) | canlı | G | https://builtin.com/job/data-engineer/11068447 |
| DE02 | DE | Doodle | İspanya (uzaktan) | Jr/Mid (etiket); 2+ yıl | 2026-10 (5 saat önce) | canlı | G | https://www.remoterocketship.com/company/doodle/jobs/data-infrastructure-engineer-spain-remote/ |
| DE03 | DE | B&A Consulting | İtalya (uzaktan) | Jr/Mid (etiket); 2-5 yıl | 2026-10 (dün) | canlı | G | https://www.remoterocketship.com/company/b-a-consulting-srl/jobs/data-engineer-gcp-analytics-italy-remote/ |
| DE04 | DE | Matrix Global | Avrupa (uzaktan) | Jr/Mid (etiket); Spark 2+ yıl | 09-28 | canlı | G | https://www.remoterocketship.com/gb/company/matrix-global/jobs/data-engineer-europe-remote/ |
| DE05 | DE | ShippyPro | İtalya (uzaktan) | Mid (Jr etiketli); ~2 yıl | 09-21 | canlı | G | https://www.remoterocketship.com/company/shippypro/jobs/data-platform-engineer-mid-level-italy-remote/ |
| DE06 | DE | Ideagen | Birleşik Krallık (uzaktan) | Jr/Mid (etiket); Associate | 09-10 | canlı | G | https://www.remoterocketship.com/gb/company/huddle/jobs/associate-ai-data-engineer-united-kingdom-remote/ |
| DE07 | DE | Gismart | Ukrayna (uzaktan) | Junior (etiket); 1-2 yıl | 08-05 | canlı | G | https://www.remoterocketship.com/company/gismart/jobs/data-engineer-ukraine-remote/ |
| DE08 | DE | Vibe.co | Fransa (uzaktan) | Junior (etiket) | 07-23 | canlı | G | https://www.remoterocketship.com/company/vibe-co/jobs/data-engineer-measurement-reporting-france-remote/ |
| DE09 | DE | OLX Group | Portekiz (uzaktan) | Jr/Mid (etiket) | 08-11 | canlı | G | https://www.remoterocketship.com/company/olx-group/jobs/data-engineer-domain-data-portugal-remote/ |
| DE10 | DE | JobLeads (müşteri ilanı) | Avrupa (uzaktan) | Belirtilmemiş; 3+ yıl | 2026-09-23 (sayfa tarihi) | canlı | G | https://eudatajobs.com/search/d/mudwnqi3bne0aexe7zf |
| DE11 | DE | Trendyol | İstanbul/Maslak (hibrit) | Belirtilmemiş; 2+ yıl | tarih görünmüyor (canlı) | canlı | G | https://jobs.lever.co/trendyol/0fa776e8-9a0f-40ee-8376-2968c53294e4 |
| DE12 | DE | Cognira | İstanbul/Fatih (hibrit) | Junior | kaldırıldı 2026-05-06 | süresi doldu | E | https://builtin.com/job/junior-data-engineer/7808255 |
| DE13 | DE | TikTok | San Jose, ABD | Intern (2026 yaz) | 2025-12-19 | süresi doldu | E | https://www.themuse.com/jobs/tiktok/data-engineer-intern-ads-data-2026-summer-bsms |
| DE14 | DE | Atlassian | Sidney, Avustralya (uzaktan) | Intern (2026 yaz) | ~2026-03 (6+ ay önce) | süresi doldu | E | https://jobs.accel.com/companies/atlassian/jobs/67873078-data-engineer-intern-2026-summer-australia |
| DE15 | DE | Rocket Companies | Detroit, ABD | Intern (2026 yaz) | ~2026-03 (6+ ay önce) | süresi doldu | E | https://portfoliojobs.tcv.com/companies/rocket-companies/jobs/65053035-data-engineer-intern-summer-2026 |
| DE16 | DE | Link Group | Varşova (uzaktan) | Senior | tarih yok | süresi doldu | E | https://justjoin.it/offers/link-group-senior-data-engineer-warszawa-data-c5fbc86d |
| DE17 | DE | Klient Just Join IT | Chorzów, Polonya (hibrit) | Mid; 3+ yıl | tarih yok | süresi doldu | E | https://justjoin.it/job-offer/klient-just-join-it-data-engineer-chorzow-data |
| DE18 | DE | Softtech | İstanbul (hibrit) | 2-4 yıl | 2025-01-16 | süresi doldu | E | https://www.techcareer.net/jobs/detail/data-engineer-3997207 |
| DE19 | DE | Huawei Türkiye Ar-Ge | İstanbul/Ankara/İzmir | Junior | kaldırıldı 2025-10-10 | süresi doldu | E | https://builtin.com/job/data-engineer-ag-im-data/2995635 |
| DA01 | DA | Spyke Games | İstanbul/Şişli (uzaktan) | Entry (etiket) | ~2026-09-16 (23 gün önce) | canlı | G | https://builtin.com/job/data-analyst/11203876 |
| DA02 | DA | Lingaro | Uzaktan (27 konum) | Entry (etiket) | ~2026-10-01 (8 gün önce) | canlı | G | https://builtin.com/job/rgm-data-analyst/11458469 |
| DA03 | DA | GitBook | Uzaktan/ofis (28 konum) | Entry (etiket) | ~2026-09-30 (9 gün önce) | canlı | G | https://builtin.com/job/data-insights/11435195 |
| DA04 | DA | Parker Hannifin | Uzaktan (27 konum) | Entry (etiket) | ~2026-09 (yeniden yayın) | canlı | G | https://builtin.com/job/data-analyst-i/9919143 |
| DA05 | DA | Eneba | Uzaktan (27 konum) | Entry (etiket) | ~2026-09-24 (15 gün önce) | canlı | G | https://builtin.com/job/payment-analyst/11351897 |
| DA06 | DA | Recidiviz | California/New York (uzaktan) | Entry-level | 09-30 | canlı | G | https://www.remoterocketship.com/us/company/recidiviz-org/jobs/data-analyst-entry-level-united-states-remote/ |
| DA07 | DA | SouthState Bank | ABD (uzaktan) | Intern (2027 yaz) | 09-28 | canlı | G | https://www.remoterocketship.com/us/company/southstatebank/jobs/data-analytics-intern-united-states-remote/ |
| DA08 | DA | JobLeads (müşteri ilanı) | Avrupa (uzaktan) | Experienced; 5+ yıl | 2026-09-21 (sayfa tarihi) | canlı | G | https://eudatajobs.com/search/d/muazccd8uyjawwnahm8 |
| DA09 | DA | Volkswagen Group | Almanya (uzaktan, çalışan öğrenci) | Entry; çalışan öğrenci | 09-25 | canlı | G | https://www.remoterocketship.com/company/volkswagen-group/jobs/working-student-data-analytics-controlling-worldwide-remote/ |
| DA10 | DA | ANDRITZ | Brezilya (uzaktan) | Entry; stajyer | 09-16 | canlı | G | https://www.remoterocketship.com/company/andritz/jobs/data-analysis-intern-worldwide-remote/ |
| DA11 | DA | National Management Software | New Jersey (uzaktan) | Entry; 0-2 yıl | 08-21 | canlı | G | https://www.remoterocketship.com/us/company/national-management-software/jobs/entry-level-data-analyst-business-analyst-new-jersey-remote/ |
| DA12 | DA | Bilyoner | İstanbul | Intern (3.-4. sınıf) | ~2025 (geçen yıl) | süresi doldu | E | https://app.qureos.com/jobs/data-intern-1756377922956 |
| DA13 | DA | Gizli firma (techcareer.net) | Ankara | 2-4 yıl | 2026-06-03 | süresi doldu | E | https://www.techcareer.net/en/jobs/detail/finansal-analist-bi-analitik-4467957 |
| DA14 | DA | LMB Medikal | İstanbul/Beylikdüzü | 4-6 yıl | 2025-09-10 | süresi doldu | E | https://www.techcareer.net/en/jobs/detail/veri-analisti-4252075 |
| DA15 | DA | Gizli firma (techcareer.net) | Ankara | 4-6 yıl | 2025-10-03 | süresi doldu | E | https://www.techcareer.net/en/jobs/detail/is-analisti-4274231 |
| DA16 | DA | IQlogg | Belirtilmemiş | Entry; 1+ yıl | tarih görünmüyor | tarihsiz | E | https://app.joinhandshake.com/jobs/4683369/share_preview |
| DS01 | DS | Satalia | Yunanistan (uzaktan) | Junior; 0-2 yıl | tarih görünmüyor (canlı) | canlı | G | https://careers.satalia.com/jobs/8511011-junior-data-scientist-greece |
| DS02 | DS | Matrix Global | Avrupa (uzaktan) | Jr/Mid (etiket); 2+ yıl | 10-02 | canlı | G | https://www.remoterocketship.com/gb/company/matrix-global/jobs/data-scientist-europe-remote/ |
| DS03 | DS | Synthomer | Hollanda/Belçika/BK (uzaktan) | Jr/Mid (etiket); 2-5 yıl | 09-30 | canlı | G | https://www.remoterocketship.com/company/synthomer/jobs/data-scientist-netherlands-remote/ |
| DS04 | DS | United Talent Agency | İspanya (uzaktan) | Jr/Mid (etiket) | 07-13 | canlı | G | https://www.remoterocketship.com/company/unitedtalent/jobs/data-scientist-spain-remote/ |
| DS05 | DS | Sporty Group | Birleşik Krallık (uzaktan) | Jr/Mid (etiket); 2+ yıl | 06-29 | canlı | G | https://www.remoterocketship.com/gb/company/sporty-group-2/jobs/data-scientist-europe-asia-united-kingdom-remote/ |
| DS06 | DS | Mobilint | İspanya (uzaktan) | Jr/Mid (etiket) | 06-23 | canlı | G | https://www.remoterocketship.com/company/mobilint/jobs/data-scientist-face-biometrics-spain-remote/ |
| DS07 | DS | Chubb | Meksika | Entry-level | 2026-06-09 | süresi doldu | G | https://jobs.anitab.org/companies/chubb/jobs/82079396-data-scientist-junior-mx-auto |
| DS08 | DS | Axiom | Birleşik Krallık (uzaktan) | Jr/Mid (etiket); 2+ yıl | 04-01 | canlı? | E | https://www.remoterocketship.com/gb/company/axiomdata-io/jobs/data-scientist-united-kingdom-remote/ |
| DS09 | DS | Kreativstorm | Almanya (uzaktan) | Junior | 2025-12-10 | canlı? | E | https://www.remoterocketship.com/company/kreativstorm-de/jobs/junior-data-scientist-germany-remote/ |
| DS10 | DS | ING Türkiye | İstanbul (konum belirsiz) | Uzman; 4+ yıl | 2026-01-06 | süresi doldu | E | https://www.techcareer.net/en/jobs/detail/junior-data-scientist-8098 |
| DS11 | DS | Prometeia | İstanbul | Junior | tarih yok (2025 ©) | süresi doldu? | E | https://kariyermerkezi.bogazici.edu.tr/tr/node/5177 |
| DS12 | DS | Gizli firma (studentjob.es) | Madrid | Junior; 1-2 yıl | tarih yok | inaktif | E | https://www.studentjob.es/ofertas/8480458-junior-data-scientist |
| DS13 | DS | Jotform | İstanbul | Belirtilmemiş | tarih yok | süresi doldu | E | https://webrazzi.com/en/kariyer/jotform-yazilim-as/data-scientist |

### 3.1 İlan başına beceriler (Z = zorunlu bölüm, T = tercih bölümü; Bulut (genel) otomatik eklendi)

| ID | Z (zorunlu) | T (tercih) |
|---|---|---|
| DE01 | SQL, Python, ETL/ELT, Veri modelleme, Linux, Git | Kafka/streaming, Orkestrasyon, Veri kalitesi/test, LLM/GenAI |
| DE02 | Kafka/streaming, Redshift, Orkestrasyon, Bulut (genel), CI/CD, Terraform/IaC, Kubernetes, Lakehouse/tablo formatı, Veri modelleme, Veri kalitesi/test | dbt |
| DE03 | GCP, BigQuery, Bulut (genel), Looker | - |
| DE04 | Spark, SQL, Git, Hadoop, Python, Linux, ML, ETL/ELT | Orkestrasyon, Docker, Kubernetes |
| DE05 | Python, SQL, Docker, AWS, Bulut (genel), AI kodlama araçları | - |
| DE06 | ETL/ELT, Python, SQL, Veri kalitesi/test | LLM/GenAI, MLOps, AWS, Bulut (genel) |
| DE07 | Veri modelleme, Lakehouse/tablo formatı, ETL/ELT, AWS, Bulut (genel), Redshift, Orkestrasyon, SQL, Python | Terraform/IaC, dbt, Spark, Tableau |
| DE08 | ETL/ELT, SQL, Veri modelleme, Orkestrasyon, dbt | - |
| DE09 | SQL, Python, Veri modelleme, Bulut (genel), AWS, Redshift, Spark, Lakehouse/tablo formatı, Orkestrasyon, Veri kalitesi/test, AI kodlama araçları | - |
| DE10 | SQL, Veri modelleme, Python, Orkestrasyon, AI kodlama araçları, Git, CI/CD, Linux, Azure, Bulut (genel) | Power BI, Microsoft Fabric |
| DE11 | Java/Scala, Spark, Bulut (genel), GCP, Kafka/streaming, Lakehouse/tablo formatı, Orkestrasyon, SQL, NoSQL, Veri kalitesi/test, Docker, Kubernetes, CI/CD, Terraform/IaC, Git, BigQuery, Snowflake | Python |
| DE12 | Python, SQL, Git, CI/CD, Java/Scala, Veri kalitesi/test | Spark, Orkestrasyon, Databricks, Kubernetes |
| DE13 | SQL, NoSQL, Python, Java/Scala, Veri modelleme, ETL/ELT | Hadoop, Spark, Kafka/streaming, Snowflake, Databricks, BigQuery, Veri kalitesi/test |
| DE14 | Python, SQL | - |
| DE15 | SQL, NoSQL | Python, Bulut (genel), CI/CD |
| DE16 | dbt, Python, AWS, Bulut (genel) | Databricks, Orkestrasyon, Snowflake, Terraform/IaC, CI/CD, Kubernetes, ML |
| DE17 | SQL, Python, Veri modelleme | Snowflake, dbt |
| DE18 | SQL, ETL/ELT, Veri modelleme | - |
| DE19 | SQL, Linux, Python | Spark, Hadoop |
| DA01 | SQL, BigQuery, Looker, Tableau, BI/dashboard, Bulut (genel) | - |
| DA02 | SQL, Excel, Power BI, BI/dashboard | Python, R |
| DA03 | SQL, Veri modelleme | - |
| DA04 | SQL, Python, Veri modelleme, LLM/GenAI | İstatistik |
| DA05 | - | BI/dashboard, SQL |
| DA06 | SQL, Python | BI/dashboard, Looker, Tableau, GCP, BigQuery, Bulut (genel) |
| DA07 | Excel | Power BI, SQL, Snowflake, Python, R, Bulut (genel) |
| DA08 | Power BI, BI/dashboard, SQL | Azure, Bulut (genel), Microsoft Fabric, Python |
| DA09 | Python, R | Power BI, Tableau, BI/dashboard, Azure, Bulut (genel) |
| DA10 | BI/dashboard, AI kodlama araçları | Power BI, Excel, Python |
| DA11 | Excel | - |
| DA12 | - | SQL, Python, R, BI/dashboard |
| DA13 | SQL, Python, R, Power BI, BI/dashboard, Excel, İstatistik | - |
| DA14 | Excel | Power BI, BI/dashboard, LLM/GenAI |
| DA15 | SQL, Python, R, Power BI, BI/dashboard, Excel, İstatistik | - |
| DA16 | SQL, Python, Tableau, BI/dashboard, Veri kalitesi/test | Bulut (genel) |
| DS01 | Python, ML, İstatistik, LLM/GenAI | - |
| DS02 | Python, Spark, MLOps, Orkestrasyon, İstatistik, ML | Bulut (genel) |
| DS03 | Python, SQL, Databricks, Spark, Bulut (genel), İstatistik, ML | - |
| DS04 | İstatistik, Python, SQL, NoSQL, CI/CD, ML, Git | Spark, Hadoop, Orkestrasyon, Derin öğrenme |
| DS05 | ML, Python, İstatistik, Lineer cebir/olasılık, SQL, AI kodlama araçları | - |
| DS06 | Derin öğrenme, ML, Python, Git, C++, AI kodlama araçları | - |
| DS07 | Python, SQL, Tableau, BI/dashboard, Git, AI kodlama araçları, İstatistik | ML |
| DS08 | Python, SQL, İstatistik, ML, BI/dashboard | - |
| DS09 | Python, R, ML | - |
| DS10 | Python, Spark, SQL, Git, Linux, ML, Derin öğrenme, MLOps, BI/dashboard | GCP, BigQuery, Bulut (genel) |
| DS11 | Python, ML, Derin öğrenme, SQL, NoSQL, Linux, Java/Scala, C++ | - |
| DS12 | İstatistik, ML, Python, R, SQL | Bulut (genel), Derin öğrenme, Spark, Hadoop, BI/dashboard, Power BI, Tableau, Git |
| DS13 | Python, SQL, İstatistik, PHP | ML |

## 4. Frekans tabloları

Sütunlar: ilanda geçme n/N ve %, zorunlu bölümde geçme n ve %. İlk 32 (toplam) ve 25 (rol) beceri.

### 4.1 Toplam (N=48)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| Python | 39/48 | 81 | 32 | 67 |
| SQL | 37/48 | 77 | 34 | 71 |
| Bulut (genel) | 20/48 | 42 | 10 | 21 |
| BI/dashboard | 16/48 | 33 | 10 | 21 |
| ML | 15/48 | 31 | 12 | 25 |
| İstatistik | 12/48 | 25 | 11 | 23 |
| Orkestrasyon | 12/48 | 25 | 7 | 15 |
| Spark | 12/48 | 25 | 6 | 12 |
| Veri modelleme | 11/48 | 23 | 11 | 23 |
| Git | 10/48 | 21 | 9 | 19 |
| Power BI | 10/48 | 21 | 4 | 8 |
| Veri kalitesi/test | 8/48 | 17 | 6 | 12 |
| R | 8/48 | 17 | 5 | 10 |
| AI kodlama araçları | 7/48 | 15 | 7 | 15 |
| ETL/ELT | 7/48 | 15 | 7 | 15 |
| Excel | 7/48 | 15 | 6 | 12 |
| CI/CD | 7/48 | 15 | 5 | 10 |
| Tableau | 7/48 | 15 | 3 | 6 |
| Linux | 6/48 | 12 | 6 | 12 |
| BigQuery | 6/48 | 12 | 3 | 6 |
| NoSQL | 5/48 | 10 | 5 | 10 |
| AWS | 5/48 | 10 | 4 | 8 |
| Derin öğrenme | 5/48 | 10 | 3 | 6 |
| Kubernetes | 5/48 | 10 | 2 | 4 |
| LLM/GenAI | 5/48 | 10 | 2 | 4 |
| dbt | 5/48 | 10 | 2 | 4 |
| Hadoop | 5/48 | 10 | 1 | 2 |
| Snowflake | 5/48 | 10 | 1 | 2 |
| Java/Scala | 4/48 | 8 | 4 | 8 |
| Lakehouse/tablo formatı | 4/48 | 8 | 4 | 8 |
| GCP | 4/48 | 8 | 2 | 4 |
| Kafka/streaming | 4/48 | 8 | 2 | 4 |

### 4.2 Toplam, yalnız güncel alt küme G (N=29)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| Python | 22/29 | 76 | 17 | 59 |
| SQL | 21/29 | 72 | 19 | 66 |
| Bulut (genel) | 15/29 | 52 | 9 | 31 |
| Orkestrasyon | 10/29 | 34 | 7 | 24 |
| Veri modelleme | 8/29 | 28 | 8 | 28 |
| ML | 8/29 | 28 | 7 | 24 |
| BI/dashboard | 8/29 | 28 | 5 | 17 |
| AI kodlama araçları | 7/29 | 24 | 7 | 24 |
| Git | 7/29 | 24 | 7 | 24 |
| İstatistik | 7/29 | 24 | 6 | 21 |
| Spark | 7/29 | 24 | 5 | 17 |
| Power BI | 6/29 | 21 | 2 | 7 |
| ETL/ELT | 5/29 | 17 | 5 | 17 |
| Veri kalitesi/test | 5/29 | 17 | 4 | 14 |
| Tableau | 5/29 | 17 | 2 | 7 |
| CI/CD | 4/29 | 14 | 4 | 14 |
| Lakehouse/tablo formatı | 4/29 | 14 | 4 | 14 |
| AWS | 4/29 | 14 | 3 | 10 |
| BigQuery | 4/29 | 14 | 3 | 10 |
| Excel | 4/29 | 14 | 3 | 10 |
| LLM/GenAI | 4/29 | 14 | 2 | 7 |
| Linux | 3/29 | 10 | 3 | 10 |
| Redshift | 3/29 | 10 | 3 | 10 |
| Docker | 3/29 | 10 | 2 | 7 |
| GCP | 3/29 | 10 | 2 | 7 |
| Kafka/streaming | 3/29 | 10 | 2 | 7 |
| Kubernetes | 3/29 | 10 | 2 | 7 |
| Looker | 3/29 | 10 | 2 | 7 |
| Terraform/IaC | 3/29 | 10 | 2 | 7 |
| Azure | 3/29 | 10 | 1 | 3 |
| R | 3/29 | 10 | 1 | 3 |
| dbt | 3/29 | 10 | 1 | 3 |

### 4.3 Data Engineer (N=19)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| SQL | 16/19 | 84 | 16 | 84 |
| Python | 15/19 | 79 | 13 | 68 |
| Bulut (genel) | 10/19 | 53 | 8 | 42 |
| Orkestrasyon | 10/19 | 53 | 6 | 32 |
| Veri modelleme | 9/19 | 47 | 9 | 47 |
| ETL/ELT | 7/19 | 37 | 7 | 37 |
| Veri kalitesi/test | 7/19 | 37 | 5 | 26 |
| Spark | 7/19 | 37 | 3 | 16 |
| CI/CD | 6/19 | 32 | 4 | 21 |
| Git | 5/19 | 26 | 5 | 26 |
| AWS | 5/19 | 26 | 4 | 21 |
| Kubernetes | 5/19 | 26 | 2 | 11 |
| dbt | 5/19 | 26 | 2 | 11 |
| Lakehouse/tablo formatı | 4/19 | 21 | 4 | 21 |
| Linux | 4/19 | 21 | 4 | 21 |
| Kafka/streaming | 4/19 | 21 | 2 | 11 |
| Terraform/IaC | 4/19 | 21 | 2 | 11 |
| Snowflake | 4/19 | 21 | 1 | 5 |
| AI kodlama araçları | 3/19 | 16 | 3 | 16 |
| Java/Scala | 3/19 | 16 | 3 | 16 |
| NoSQL | 3/19 | 16 | 3 | 16 |
| Redshift | 3/19 | 16 | 3 | 16 |
| BigQuery | 3/19 | 16 | 2 | 11 |
| Docker | 3/19 | 16 | 2 | 11 |
| Hadoop | 3/19 | 16 | 1 | 5 |

### 4.4 Data Engineer, G (N=11)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| SQL | 9/11 | 82 | 9 | 82 |
| Bulut (genel) | 8/11 | 73 | 7 | 64 |
| Python | 8/11 | 73 | 7 | 64 |
| Orkestrasyon | 8/11 | 73 | 6 | 55 |
| Veri modelleme | 6/11 | 55 | 6 | 55 |
| ETL/ELT | 5/11 | 45 | 5 | 45 |
| Veri kalitesi/test | 5/11 | 45 | 4 | 36 |
| Git | 4/11 | 36 | 4 | 36 |
| Lakehouse/tablo formatı | 4/11 | 36 | 4 | 36 |
| AWS | 4/11 | 36 | 3 | 27 |
| Spark | 4/11 | 36 | 3 | 27 |
| AI kodlama araçları | 3/11 | 27 | 3 | 27 |
| CI/CD | 3/11 | 27 | 3 | 27 |
| Linux | 3/11 | 27 | 3 | 27 |
| Redshift | 3/11 | 27 | 3 | 27 |
| Docker | 3/11 | 27 | 2 | 18 |
| Kafka/streaming | 3/11 | 27 | 2 | 18 |
| Kubernetes | 3/11 | 27 | 2 | 18 |
| Terraform/IaC | 3/11 | 27 | 2 | 18 |
| dbt | 3/11 | 27 | 1 | 9 |
| BigQuery | 2/11 | 18 | 2 | 18 |
| GCP | 2/11 | 18 | 2 | 18 |
| LLM/GenAI | 2/11 | 18 | 0 | 0 |
| Azure | 1/11 | 9 | 1 | 9 |
| Hadoop | 1/11 | 9 | 1 | 9 |

### 4.5 Data Analyst (N=16)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| SQL | 12/16 | 75 | 9 | 56 |
| BI/dashboard | 12/16 | 75 | 7 | 44 |
| Python | 11/16 | 69 | 6 | 38 |
| Power BI | 8/16 | 50 | 4 | 25 |
| Excel | 7/16 | 44 | 6 | 38 |
| R | 6/16 | 38 | 3 | 19 |
| Bulut (genel) | 6/16 | 38 | 1 | 6 |
| Tableau | 4/16 | 25 | 2 | 12 |
| İstatistik | 3/16 | 19 | 2 | 12 |
| Veri modelleme | 2/16 | 12 | 2 | 12 |
| BigQuery | 2/16 | 12 | 1 | 6 |
| LLM/GenAI | 2/16 | 12 | 1 | 6 |
| Looker | 2/16 | 12 | 1 | 6 |
| Azure | 2/16 | 12 | 0 | 0 |
| AI kodlama araçları | 1/16 | 6 | 1 | 6 |
| Veri kalitesi/test | 1/16 | 6 | 1 | 6 |
| GCP | 1/16 | 6 | 0 | 0 |
| Microsoft Fabric | 1/16 | 6 | 0 | 0 |
| Snowflake | 1/16 | 6 | 0 | 0 |

### 4.6 Data Analyst, G (N=11)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| SQL | 8/11 | 73 | 6 | 55 |
| BI/dashboard | 7/11 | 64 | 4 | 36 |
| Python | 7/11 | 64 | 3 | 27 |
| Power BI | 5/11 | 45 | 2 | 18 |
| Bulut (genel) | 5/11 | 45 | 1 | 9 |
| Excel | 4/11 | 36 | 3 | 27 |
| R | 3/11 | 27 | 1 | 9 |
| Tableau | 3/11 | 27 | 1 | 9 |
| Veri modelleme | 2/11 | 18 | 2 | 18 |
| BigQuery | 2/11 | 18 | 1 | 9 |
| Looker | 2/11 | 18 | 1 | 9 |
| Azure | 2/11 | 18 | 0 | 0 |
| AI kodlama araçları | 1/11 | 9 | 1 | 9 |
| LLM/GenAI | 1/11 | 9 | 1 | 9 |
| GCP | 1/11 | 9 | 0 | 0 |
| Microsoft Fabric | 1/11 | 9 | 0 | 0 |
| Snowflake | 1/11 | 9 | 0 | 0 |
| İstatistik | 1/11 | 9 | 0 | 0 |

### 4.7 Data Scientist (N=13)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| Python | 13/13 | 100 | 13 | 100 |
| ML | 13/13 | 100 | 11 | 85 |
| SQL | 9/13 | 69 | 9 | 69 |
| İstatistik | 9/13 | 69 | 9 | 69 |
| Git | 5/13 | 38 | 4 | 31 |
| Derin öğrenme | 5/13 | 38 | 3 | 23 |
| Spark | 5/13 | 38 | 3 | 23 |
| BI/dashboard | 4/13 | 31 | 3 | 23 |
| Bulut (genel) | 4/13 | 31 | 1 | 8 |
| AI kodlama araçları | 3/13 | 23 | 3 | 23 |
| C++ | 2/13 | 15 | 2 | 15 |
| Linux | 2/13 | 15 | 2 | 15 |
| MLOps | 2/13 | 15 | 2 | 15 |
| NoSQL | 2/13 | 15 | 2 | 15 |
| R | 2/13 | 15 | 2 | 15 |
| Orkestrasyon | 2/13 | 15 | 1 | 8 |
| Tableau | 2/13 | 15 | 1 | 8 |
| Hadoop | 2/13 | 15 | 0 | 0 |
| CI/CD | 1/13 | 8 | 1 | 8 |
| Databricks | 1/13 | 8 | 1 | 8 |
| Java/Scala | 1/13 | 8 | 1 | 8 |
| LLM/GenAI | 1/13 | 8 | 1 | 8 |
| Lineer cebir/olasılık | 1/13 | 8 | 1 | 8 |
| PHP | 1/13 | 8 | 1 | 8 |
| BigQuery | 1/13 | 8 | 0 | 0 |

### 4.8 Data Scientist, G (N=7)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| Python | 7/7 | 100 | 7 | 100 |
| ML | 7/7 | 100 | 6 | 86 |
| İstatistik | 6/7 | 86 | 6 | 86 |
| SQL | 4/7 | 57 | 4 | 57 |
| AI kodlama araçları | 3/7 | 43 | 3 | 43 |
| Git | 3/7 | 43 | 3 | 43 |
| Spark | 3/7 | 43 | 2 | 29 |
| Bulut (genel) | 2/7 | 29 | 1 | 14 |
| Derin öğrenme | 2/7 | 29 | 1 | 14 |
| Orkestrasyon | 2/7 | 29 | 1 | 14 |
| BI/dashboard | 1/7 | 14 | 1 | 14 |
| C++ | 1/7 | 14 | 1 | 14 |
| CI/CD | 1/7 | 14 | 1 | 14 |
| Databricks | 1/7 | 14 | 1 | 14 |
| LLM/GenAI | 1/7 | 14 | 1 | 14 |
| Lineer cebir/olasılık | 1/7 | 14 | 1 | 14 |
| MLOps | 1/7 | 14 | 1 | 14 |
| NoSQL | 1/7 | 14 | 1 | 14 |
| Tableau | 1/7 | 14 | 1 | 14 |
| Hadoop | 1/7 | 14 | 0 | 0 |

### 4.9 Türkiye ilanları, tüm roller (N=13: DE 5, DA 5, DS 3)

| Beceri | Geçiş n/N | % | Zorunlu bölümde n | % |
|---|---|---|---|---|
| SQL | 12/13 | 92 | 11 | 85 |
| Python | 10/13 | 77 | 8 | 62 |
| BI/dashboard | 6/13 | 46 | 4 | 31 |
| Git | 4/13 | 31 | 4 | 31 |
| Linux | 4/13 | 31 | 4 | 31 |
| Spark | 4/13 | 31 | 2 | 15 |
| Excel | 3/13 | 23 | 3 | 23 |
| Java/Scala | 3/13 | 23 | 3 | 23 |
| İstatistik | 3/13 | 23 | 3 | 23 |
| BigQuery | 3/13 | 23 | 2 | 15 |
| Bulut (genel) | 3/13 | 23 | 2 | 15 |
| ML | 3/13 | 23 | 2 | 15 |
| Power BI | 3/13 | 23 | 2 | 15 |
| R | 3/13 | 23 | 2 | 15 |
| Veri kalitesi/test | 3/13 | 23 | 2 | 15 |
| Orkestrasyon | 3/13 | 23 | 1 | 8 |
| CI/CD | 2/13 | 15 | 2 | 15 |
| Derin öğrenme | 2/13 | 15 | 2 | 15 |
| ETL/ELT | 2/13 | 15 | 2 | 15 |
| NoSQL | 2/13 | 15 | 2 | 15 |
| Veri modelleme | 2/13 | 15 | 2 | 15 |
| GCP | 2/13 | 15 | 1 | 8 |
| Kafka/streaming | 2/13 | 15 | 1 | 8 |
| Kubernetes | 2/13 | 15 | 1 | 8 |
| LLM/GenAI | 2/13 | 15 | 0 | 0 |

## 5. Öncelik sıralı konu listesi (hedef: Data Engineer Intern / junior)

Sıralama ölçütü: DE ilanlarındaki frekans (özellikle güncel alt küme G), zorunlu bölümde geçme, sonra DA/DS'ye taşınabilirlik. Boşluk tahminleri adayın beyan ettiği profile (Python, SQL, SQLite, git, bronze/silver/gold) göre kestirimdir `[?]`; aday ölçülmedi. Frekanslar bölüm 4 tablolarından.

| # | Konu | Ayrıntı | Hangi rollerde (n/N) | Neden öncelikli | Boşluk `[?]` | CV ürün fikri (GitHub) |
|---|---|---|---|---|---|---|
| 1 | SQL (ileri) | Pencere fonksiyonları, CTE, join stratejisi, sorgu planı ve optimizasyon | DE 16/19 (%84), DA 12/16 (%75), DS 9/13 (%69); toplam 37/48 (%77); Türkiye alt kümesi 12/13 | Tek beceri olarak en yüksek zorunlu oranı (DE zorunlu 16/19). Huawei, iyzico, Trendyol sorgu optimizasyonu istiyor | Düşük-orta: SQLite kullanıyor; pencere fonksiyonu ve EXPLAIN derinliği bilinmiyor | SQLite/DuckDB üzerinde 40 sorgulu "window function + EXPLAIN QUERY PLAN" çalışma defteri; her sorgu için indeks öncesi/sonrası ölçüm tablosu |
| 2 | Python (veri işleme, test, paketleme) | pandas/pyarrow, modüler yapı, pytest, CLI | DE 15/19 (%79), DA 11/16 (%69), DS 13/13 (%100); toplam 39/48 (%81) | Tüm rollerde ilk iki beceri; "production-level Python" ifadesi DE'de tekrarlanıyor (Gismart, Link Group, iyzico) | Düşük | Mevcut bronze/silver/gold işini pytest + tip ipuçları + `pyproject.toml` ile kurulabilir paket ve CLI olarak yayımla |
| 3 | Bulut (AWS) | S3, IAM, Glue, Athena, Redshift, Lambda | DE bulut 10/19 (%53), G'de 8/11 (%73); AWS 5/19 (%26); Redshift 3/19; toplam bulut 20/48 (%42) | Güncel DE ilanlarında en yüksek dilimlerden; DEA-C01 bu konunun doğrudan karşılığı (Ideagen, Gismart, ShippyPro, OLX AWS/Redshift istiyor) | Yüksek: pratik bulut deneyimi beyan edilmedi | S3 + Glue + Athena ile bronze/silver/gold lakehouse; ücretsiz katman, maliyet notu README'de |
| 4 | Orkestrasyon | Airflow (alternatif: Dagster/Prefect): DAG, zamanlama, retry, backfill | DE 10/19 (%53), G'de 8/11 (%73); zorunlu 6/19; toplam 12/48 | Güncel DE'de bulutla birlikte en yüksek dilim; Gismart, Doodle, JobLeads production DAG istiyor; Cognira ve iyzico tercih bölümünde | Orta-yüksek: kurulum ve DAG yazımı deneyimi yok varsayımı | Docker Compose ile Airflow; günlük ingest, bronze->silver->gold DAG'ı, retry ve alarm; DAG testleri |
| 5 | Veri modelleme | Star schema, fact/dimension, SCD tip 2, medallion mimarisi | DE 9/19 (%47, hepsi zorunlu bölümde), DA 2/16; toplam 11/48 | Zorunlu bölümde 9/19: tercih değil beklenti. OLX açıkça medallion architecture yazıyor; adayın katman deneyimiyle örtüşüyor | Orta: katman kavramı var, boyutsal model formalizasyonu belirsiz | Açık bir veri setinden star schema + SCD2 gold katmanı; ER şeması, yükleme SQL'i ve veri sözlüğü |
| 6 | ETL/ELT ve veri kalitesi | Idempotent yükleme, şema doğrulama, kalite testleri (Great Expectations / dbt test), gözlemlenebilirlik | ETL/ELT DE 7/19 (%37); veri kalitesi/test DE 7/19 (%37), G'de 5/11 (%45); toplam 8/48 | Güncel DE'de yaklaşık yarısı; Doodle, OLX, Ideagen, Trendyol zorunlu bölümde | Orta: kural tabanlı kalite kontrolü yazılmamış olabilir | Silver katmanına 20 kurallı kalite raporu (null oranı, tekillik, referans bütünlüğü); CI'da koşar, çıktı markdown rapor |
| 7 | Spark | PySpark/Spark SQL: DataFrame API, partition, shuffle kavramı | DE 7/19 (%37), DS 5/13 (%38); toplam 12/48 (%25); Türkiye 4/13 | DE'de zorunlu 3/19 ama tercih bölümünde sık (TikTok, Cognira, Huawei, Gismart); Türkiye'de Trendyol, Huawei, Cognira, ING | Yüksek: dağıtık işleme deneyimi beyan edilmedi | NYC taksi açık verisinin (birkaç GB) PySpark ile bronze->gold dönüşümü; aynı sorgunun SQLite ve Spark süre karşılaştırması |
| 8 | Git, CI/CD, Docker, Linux | Git akışı, GitHub Actions, Dockerfile, Linux CLI | Git DE 5/19, toplam 10/48; CI/CD DE 6/19 (%32); Linux DE 4/19, Türkiye 4/13 (%31); Docker DE 3/19 | Junior ilanların ortak yazılım mühendisliği temeli satırı (Cognira, iyzico, Huawei, JobLeads) | Düşük: git var; Actions ve Docker belirsiz | Tüm projelerde GitHub Actions ile lint + pytest + docker build; WSL/Linux'ta çalışan Dockerfile |
| 9 | dbt | Model, test, kaynak tazeliği, doküman, Jinja makroları | DE 5/19 (%26), G'de 3/11; zorunlu 2/19 (Link Group, Vibe.co); toplam 5/48 | Avrupa uzaktan ilanlarda analitik mühendislik köprüsü; Trendyol Analytics Engineer ilanı aynı alanda | Yüksek | `dbt-duckdb` ile madde 5-6'daki modeli dbt projesine taşı; `dbt docs` çıktısı yayında |
| 10 | Lakehouse / tablo formatları | Parquet, Delta Lake, Apache Iceberg temelleri | DE 4/19 (%21), G'de 4/11 (%36), hepsi zorunlu bölümde (Doodle, Gismart, OLX, Trendyol) | Güncel ilanlarda öne çıkıyor; DEA-C01 kapsamıyla ilişkisi doğrulanmadı `[?]` | Yüksek | Parquet bölümlü depolama + Iceberg/Delta tablosu; time travel sorgusu örneği |
| 11 | AI kodlama araçları / LLM okuryazarlığı | AI destekli geliştirme akışı ve çıktıyı doğrulama | Toplam 7/48 (%15), G'de 7/29 (%24); DE G 3/11, DS G 3/7; LLM/GenAI ayrıca 5/48 | Yeni 2026 kalıbı: ShippyPro, OLX, JobLeads, Chubb, Sporty, Mobilint zorunlu bölümde yazıyor | Düşük: Claude Code kullanımı mevcut | README'de AI destekli geliştirme akışı bölümü: hangi çıktı nasıl doğrulandı, test kanıtı; repodaki hareket günlüğü örnek olarak gösterilebilir |
| 12 | Terraform / IaC | Terraform ile bulut kaynağı tanımı | DE 4/19 (%21), G'de 3/11 (%27); zorunlu 2/19 | AWS çalışmasıyla birlikte düşük ek maliyetle gelir; Doodle, Trendyol zorunlu bölümde | Yüksek | Madde 3'teki lakehouse'u Terraform modülü olarak yaz; `terraform plan` çıktısı README'de |
| 13 | Akış (Kafka) | Topic, partition, consumer group, CDC | DE 4/19 (%21), G'de 3/11; zorunlu 2/19 | Doodle, Trendyol zorunlu; iyzico Kafka/Debezium'u tercih sayıyor; junior için tercih sınıfı | Yüksek | Docker'da tek düğüm Kafka; olayları bronze katmana yazan mini üretici/tüketici hattı |
| 14 | BI / görselleştirme | Power BI, Tableau, Looker; gold katman üstünde dashboard | DA 12/16 (%75), Power BI DA 8/16 (%50); DE'de yalnız 3/19 (DE03, DE07, DE10); Türkiye BI 6/13 | DE hedefi için düşük öncelik; DA'ya kayma ihtimaline sigorta | Orta | Gold katman üstüne Streamlit ya da Power BI Desktop paneli; kaynak madde 3'teki lakehouse |

Not: Matematik mühendisliğinden gelen **istatistik ve ML** DS rolünde kritik (ML 13/13, İstatistik 9/13) ama DE'de ML yalnız 2/19 (Matrix, Link Group). DE hedefinde fark yaratıcı sayılır, listenin dışında tutuldu; DS'ye geçiş seçeneği için avantaj `[?]`.

### 5.1 AWS DEA-C01 ile eşleşme (kestirim `[?]`)

Sertifika kapsamı bu çalışmada incelenmedi; eşleşme taranan ilanlardan çıkarım. DE ilanlarında AWS 5/19 (%26), bulut (herhangi) 10/19 (%53); DE'de Azure 1/19 (JobLeads) ve GCP 2/19 (B&A, Trendyol) de var. Yani AWS odaklı sertifika, DE ilanlarının yaklaşık yarısında doğrudan karşılık bulmuyor `[?]`. Okunan ilan özetlerinde sertifika şartı görülmedi (ilan metinleri sertifika terimi için ayrıca taranmadı). Pratik öneri `[?]`: sertifikadan önce madde 3 ve 4'ü proje olarak bitir; sertifika CV'de ek sinyal olur, ilan şartı değil.

## 6. Doğrulama notları

- Sayımlar `veri.py` (48 kayıt) ve `hesapla.py` ile üretildi; betikler oturumun scratchpad dizininde, depoya alınmadı.
- Tablo 3'teki URL'ler tarama anında içerik döndüren adreslerdir; "süresi doldu" durumundaki sayfaların beceri metni okunabildi, başvuruya kapalı olabilir.
- ING (DS10) ilanı techcareer.net kaydından okundu; konum alanı belirsiz (Hollanda/İstanbul çelişkisi).
- Etiket çelişkileri (ör. Spyke "Entry" etiketi ama metin "experienced", ShippyPro "Mid-level" ama "Junior" etiketli) tabloda yazıldı, sayımı etkilemez.

## 7. İkincil kaynaklar (ayrı işaretli, ana sayıma dahil değil)

| Kaynak | Ne ölçülmüş | Bulgu | Not |
|---|---|---|---|
| 365 Data Science, "The Data Engineer Job Market in 2026" (https://365datascience.com/career-advice/data-engineer-job-market/) | Indeed ABD, 1000 ilandan 703 ilgili ilan; makale 2026-04-23, grafikler "2024" etiketli | SQL %79,4; Python %73,7; Azure %74,5; AWS %49,5; Spark %41,1; Kafka %16,2; Snowflake %11,7; Docker %9; Airflow %3,3 | Sayfa açılıp okundu. Azure yüzdesi tuhaf yüksek (kaynakta da uyarı var); Airflow %3,3 bizim DE örneklemindeki %53'ten çok düşük, fark büyük ölçüde örneklem/anahtar kelime yöntemi ve ABD-Avrupa farkı `[?]` |
| careery.pro, "Data Analyst Skills & Tools You Need in 2026" (https://careery.pro/blog/data-analyst-careers/data-analyst-skills) | Makale 2026-02-17; yüzdeler LinkedIn/Indeed 2025 analizlerine atfedilmiş, örneklem büyüklüğü verilmemiş | SQL %92; Excel/Sheets %75; Tableau/Power BI/benzeri %65+; Python %55+; İstatistik %45+; Looker %20; R %15 | Sayfa açılıp okundu. Eğitim-şirketi blogu; örneklem yok. Bizim DA sayımıyla (SQL %75, BI %75, Python %69, Excel %44) yön olarak uyumlu |
| Medium, "I Analyzed 500 Data Science Job Posts in 2026" (https://medium.com/ai-analytics-diaries/i-analyzed-500-data-science-job-posts-in-2026-heres-exactly-what-they-want-eaac5980590b) | 500 DS ilanı | SQL ilanların %64'ünde açıkça geçiyor | **Yalnız arama özetinden**; sayfa 403 verdi, açılamadı. Doğrulanmadı |

Ek not (yalnız arama özeti, doğrulanmadı): bir DEV Community yazısı 2026'da DE ilanlarının yalnız %3'ünün açıkça entry-level (2 yıl ve altı) olduğunu iddia ediyor (https://dev.to/datadriven/entry-level-data-engineering-is-gone-heres-the-proof-4d3n); tek veri setine dayanan görüş yazısı. Örneklem junior/mid ağırlıklı seçildiği için bu oranı doğrulamaz ya da çürütmez.

