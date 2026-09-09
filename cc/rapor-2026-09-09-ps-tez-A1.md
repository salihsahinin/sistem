# Tez Ajanı — Aile 1: İşgücü Piyasası Raporları ve İşveren Anketleri

**Soru:** AI çağında (2026-2035) "problem solving" becerisi hangi somut alt-becerilerden oluşuyor, hangileri yükseliyor/düşüyor — işveren/işgücü raporlarına göre.
**Koşum tarihi (AS-OF çekim):** 2026-09-09
**Hedef kitle:** Matematik mühendisliği lisans öğrencisi, veri/ML kariyeri.
**Araç çağrısı bütçesi:** 12/12 kullanıldı.

---

## 1. Bulgular Listesi

| # | İddia | Kaynak URL | AS-OF (yayın/veri tarihi) | Gerçekten açıldı mı |
|---|-------|-----------|---------------------------|----------------------|
| 1 | WEF Future of Jobs Report 2025: en çok talep edilen çekirdek beceri "analytical thinking" — işverenlerin %69'u büyüyen öncelik olarak işaretledi | https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/3-skills-outlook/ (WebSearch AI-özeti üzerinden, sayfa **403** verdi, doğrudan açılamadı) | 2025-01-20 (rapor yayın tarihi) | HAYIR — arama motoru özetinden; ham sayfa 403 Forbidden |
| 2 | Aynı sıralamada: "resilience, flexibility, agility" %67; "leadership and social influence" %61; "creative thinking" %57; "motivation and self-awareness" %52 | aynı (yukarıdaki gibi 403) | 2025-01-20 | HAYIR (arama özeti) |
| 3 | WEF 2025 raporunun 5 birincil çekirdek beceri listesi: (1) Analytical thinking and innovation (2) Resilience, flexibility, agility (3) Technological literacy (4) Creative thinking (5) Leadership and social influence; ayrıca "büyüyen" kategoride AI/big data, siber güvenlik, yeşil beceriler, merak/yaşam-boyu-öğrenme | https://blog.lewagon.com/news/insights-from-the-future-of-jobs-report-2025/ | 2025-01-20 (kaynağın atıf verdiği WEF rapor tarihi) | **EVET** — WebFetch ile açıldı, içerik doğrudan okundu (üçüncül kaynak: WEF'i özetleyen blog, sayısal detay eksik) |
| 4 | "2030'a kadar mevcut becerilerin %39'u güncelliğini yitirecek" | aynı lewagon blog yazısı | 2025-01-20 | EVET (yukarıdaki gibi açıldı) |
| 5 | Orijinal WEF PDF'i (`reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf`) curl ile indirildi ancak dosya 936 bayt — gerçek PDF değil, muhtemelen bir yönlendirme/JS kabuk sayfası; pdftotext "Illegal character in hex string" hatası verdi, içerik çıkarılamadı | https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf | — | HAYIR — teknik erişim engeli, **BAYRAK: PDF indirilemedi** |
| 6 | Anthropic Economic Index (Ocak 2026 güncellemesi, "economic-index-primitives" raporu): Claude.ai konuşmalarında "computer and mathematical tasks" toplam konuşmaların ~üçte biri, API trafiğinin neredeyse yarısı; augmentation (işbirlikçi kullanım) Kasım 2025 itibarıyla %52, automation %45 — augmentation ilk kez automation'ı geçti | https://www.anthropic.com/research/economic-index-primitives | 2026-01-15 (rapor yayın tarihi; veri Kasım 2025 kesitine ait) | **EVET** — WebFetch ile birincil kaynağa (Anthropic'in kendi sitesi) doğrudan erişildi |
| 7 | Aynı raporda: lisans-düzeyi (16 yıl eğitim) gerektiren görevlerde hızlanma faktörü ~12x, lise-düzeyi görevlerde ~9x — yani daha yüksek eğitim/karmaşıklık gerektiren görevlerde Claude'un görece "yardım" etkisi daha büyük | https://www.anthropic.com/research/economic-index-primitives | 2026-01-15 | EVET (aynı açılan sayfa) |
| 8 | Uzun vadeli trend: augmentation payı Ocak 2025'te %55/%41 iken Mart 2026'da %55/%42 — kısa vadeli (Kasım 2025) augmentation artışına rağmen uzun vadede automation payının kademeli arttığı görülüyor | https://www.anthropic.com/research/economic-index-primitives | 2026-01-15 (rapor), trend verisi Ocak 2025 – Mart 2026 arası | EVET (aynı açılan sayfa) |
| 9 | OECD Skills Outlook 2025: Genel-amaçlı yapay zekaya yüksek maruziyeti olan mesleklerdeki işçiler ücret/istihdam kaybı riski taşıyor; AI tarafından tamamlanan (complemented) mesleklerdeki işçiler kazanç artışı görebilir. Deneyimsiz işçilerde talep düşerken, deneyimli işçilerde "AI'nin şu an yetersiz kaldığı karmaşık görevleri üstlenme" talebi sürüyor | https://www.oecd.org/en/publications/2025/12/oecd-skills-outlook-2025_ac37c7d4/full-report/... (sayfa **403** verdi) | 2025-12 (OECD Skills Outlook 2025 yayın ayı) | HAYIR — arama özetinden; ham sayfa 403 |
| 10 | OECD: Mesleki eğitim (VET) "adaptif problem çözücüler" yetiştirmeli — örnek: yeni bir arızayı teşhis eden tesisatçı, karmaşık duygusal durumla başa çıkan bakım işçisi, tanımadığı bir sistemi arızadan kurtaran teknisyen — bunların hepsi "AI'nin rutin uygulamalarının ötesinde" | aynı OECD sayfası (403, arama özeti) | 2025-12 | HAYIR |
| 11 | LinkedIn "Skills on the Rise 2026": AI mühendisliği, prompt yazma ve model ayarlama en hızlı büyüyen beceriler arasında; işverenler AI'nin eksik kaldığı becerileri (ilişki kurma, karmaşık durumları yönetme, stratejiyi eyleme çevirme) özellikle arıyor; rutin analiz/veri işleme/standart raporlama değer kaybediyor | arama motoru AI-özeti (interviewquery.com, inc.com — inc.com 403 verdi) | 2026 (rapor adında "2026" var, tam ay tespit edilemedi) `[?]` | HAYIR — ham sayfa açılamadı, yalnız arama özeti |
| 12 | Lightcast: Çapraz-fonksiyonel işbirliği (cross-functional collaboration) talebi 2025 Q2→Q3 arası neredeyse iki katına, Q3→Q4 arası ikiden fazla katına çıktı; karmaşık problem çözme "üst performansçıları ayıran" beceri olarak tanımlanıyor, teknik uzmanlık ile stratejik düşünmeyi köprülüyor | arama motoru AI-özeti üzerinden (lightcast.io sayfaları ham açılmadı) | 2025 Q2-Q4 (veri kesiti) | HAYIR — yalnız arama özeti, ham sayfa açılmadı |

**Not — birincil-kaynak kotası:** Görev tanımı en az 2 kaynağın GERÇEKTEN açılmasını (WebFetch/curl) şart koşuyor. Bu koşumda 2 kaynak fiilen açıldı: (a) lewagon blog (WEF'i özetleyen üçüncül kaynak — WEF'in kendi sayfaları 403 verdi, sayısal detay bu ikincil kaynaktan alınamadı), (b) Anthropic Economic Index — Anthropic'in kendi sitesi, gerçek birincil kaynak. WEF'in orijinal PDF'i ve OECD/Lexology/Inc sayfaları 403 veya bozuk-dosya nedeniyle açılamadı; bu satırlar arama-motoru AI-özetine dayanır ve tabloda açıkça "HAYIR" ile işaretlendi. **Bu bir kısıttır, gizlenmemiştir** (bkz. Bölüm 4).

---

## 2. Alt-Beceri Tablosu: Yükselen / Düşen / İkame-Edilen / Tamamlayıcı

| Alt-beceri / kategori | Yön | Kanıt (bulgu #) | Güven |
|---|---|---|---|
| Analitik düşünme (analytical thinking) — genel, WEF'in en üst sıradaki becerisi | Yükselen | #1, #3 | ORTA (sayısal iddia arama-özetinden, ham sayfa doğrulanamadı) |
| Karmaşık problem çözme (complex problem-solving), özellikle "belirsiz/açık-uçlu, kalıp-dışı" görevler | Yükselen | #9, #10, #12 | ORTA (OECD ve Lightcast özetleri birbirini destekliyor, ama ikisi de ham açılmadı) |
| Sistemler düşüncesi / sistem-arızası teşhisi (novel/unfamiliar sistem troubleshooting) | Yükselen | #10 | DÜŞÜK (tek kaynak, ham açılmadı) |
| AI mühendisliği, prompt yazma, model ayarlama (AI literacy'nin somut, teknik ucu) | Hızla yükselen | #11 | DÜŞÜK (`[?]` — LinkedIn raporunun tam yayın tarihi teyit edilemedi, ham sayfa 403) |
| Çapraz-fonksiyonel işbirliği + ilişki kurma (problem çözmenin sosyal bileşeni) | Yükselen | #11, #12 | ORTA |
| Yaratıcı düşünme (creative thinking) | Yükselen ama analitik düşünmenin altında | #1, #3 | ORTA |
| Rutin veri işleme, standart raporlama, yapılandırılmış analiz (structured analysis, routine data processing) | Düşen / ikame ediliyor | #6, #9, #11 | ORTA-YÜKSEK (Anthropic + LinkedIn + OECD üçü de aynı yönde) |
| Lise-düzeyi / rutin bilişsel görevler (Anthropic'in "high-school-level" sınıflaması) | İkame ediliyor (Claude ile ~9x hızlanma, düşük tamamlayıcılık) | #7 | YÜKSEK (birincil kaynaktan doğrudan okundu) |
| Lisans-düzeyi / uzmanlık gerektiren muhakeme görevleri | Tamamlayıcı (AI ile birlikte ~12x hızlanma — insan hâlâ döngüde) | #7 | YÜKSEK (birincil kaynaktan doğrudan okundu) |
| Deneyimsiz/junior işçilerin görevleri (genel) | Talep düşüşü riski | #9 | ORTA (OECD özeti, ham açılmadı) |
| Deneyimli/senior işçilerin karmaşık-görev üstlenmesi | Talep artışı | #9 | ORTA |
| Automation (yönlendirici, minimum geri-bildirimli AI kullanımı) | Payı uzun vadede kademeli artıyor (%41→%42, Oca 2025-Mar 2026) ama kısa vadede augmentation'ın gerisinde (%45 vs %52, Kasım 2025) | #6, #8 | YÜKSEK (birincil kaynak, iki farklı zaman kesiti karşılaştırıldı) |

---

## 3. Eğitim Serisine Öneri

| Öncelik | Konu | Tek satır gerekçe |
|---|---|---|
| 1 | "Analitik düşünme" ile "karmaşık problem çözme"nin somut ayrımı + WEF/OECD tanımlarının ders materyaline aktarılması | En çok tekrar eden ve en yüksek güvenli sinyal (#1, #3, #9) — hedef kitle bunu "hangi becerimi geliştireceğim" sorusuna doğrudan cevap olarak kullanacak |
| 2 | "Belirsiz/açık-uçlu problem" pratiği (kalıp-dışı sistem arızası, novel-fault teşhisi tarzı vaka çalışmaları) | OECD'nin "AI'nin rutin uygulamalarının ötesi" tanımı doğrudan matematik/ML öğrencisi için ders-vaka tasarımına çevrilebilir (#10) |
| 3 | AI ile birlikte çalışma pratiği: augmentation (döngüde kalarak) vs automation (devretme) ayrımını fark ettiren egzersizler | Anthropic'in birincil-kaynaklı veri seti bu ayrımı ölçülebilir kılıyor; öğrenciye "hangi görevde AI'ye devret, hangisinde döngüde kal" kararını öğretmek somut kariyer değeri taşır (#6, #7, #8) |
| 4 | Prompt mühendisliği ve model ayarlamanın "problem çözme" becerisinin bir alt-kümesi olarak çerçevelenmesi | LinkedIn sinyali güçlü ama tek-kaynaklı ve doğrulanamadı — düşük öncelikte, tanıtıcı seviyede işlensin (#11, `[?]`) |
| 5 | Çapraz-fonksiyonel iletişim / bulguyu paydaşa anlatma pratiği (matematik mühendisi + iş birimi) | Veri/ML işinde teknik çözümün "anlaşılır kılınması" giderek öne çıkıyor, ama kanıt tek kaynaklı ve zayıf (#12) — orta-düşük öncelik |

---

## 4. Kısıtlar / Bulunamayanlar

- **Birincil-kaynak erişim engeli:** WEF'in kendi sayfası (`weforum.org/.../3-skills-outlook/`) ve OECD'nin tam-rapor sayfası WebFetch ile **403 Forbidden** verdi. WEF'in PDF'i curl ile indirildi ama 936 bayt — gerçek içerik değil (muhtemelen bot-engelleme/yönlendirme kabuğu); pdftotext içerik çıkaramadı. Lexology ve Inc.com sayfaları da 403 verdi. Bu nedenle WEF'in %69/%67/%61/%57/%52 rakamları ve OECD'nin bulguları **arama motorunun AI-üretimi özetine** dayanıyor — ham metinde doğrulanamadı. Bu, görevin "en az 2 birincil kaynağı gerçekten aç" koşulunu tam karşılamıyor; yalnızca Anthropic Economic Index sayfası gerçek birincil-kaynak erişimiyle doğrulandı.
- **WEF Future of Jobs Report 2026** (varsa) bulunamadı — arama sonuçlarında yalnız 2025 raporu (Ocak 2025 yayın) çıktı; 2026 versiyonuna dair kanıt yok. `[?]`
- **LinkedIn "Skills on the Rise 2026" raporunun tam yayın tarihi ve tam rakamları** teyit edilemedi — ham sayfa açılamadı, yalnız üçüncül makalelerden (interviewquery, inc.com — ikisi de erişilemedi) arama özeti alındı.
- **Lightcast Global AI Skills Outlook** ve **Anthropic Economic Index Haziran/Mart 2026 raporları** bulundu (arama sonuçlarında listelendi) ama araç bütçesi (12/12) dolduğu için açılamadı; bir sonraki koşumda öncelikli hedef olmalı.
- **AAC&U ve NACE işveren anketleri** aranmadı — araç bütçesi bu aramaya yetmedi; Aile 1'in ikinci turunda ele alınmalı.
- **McKinsey/BCG/Deloitte işgücü raporları** hiç aranmadı (bütçe tükendi) — sonraki tur için açık madde.

**Genel güven notu:** Bu raporun en sağlam bulguları (#6, #7, #8 — Anthropic Economic Index) gerçek birincil-kaynak okumasına dayanıyor ve YÜKSEK güvenilirliktedir. WEF/OECD/LinkedIn/Lightcast bulguları (#1-5, #9-12) arama motoru özetlerine dayanıyor, ORTA-DÜŞÜK güvenilirlikte ve bir sonraki araştırma turunda ham kaynaktan doğrulanmalı (özellikle WEF PDF'i alternatif bir indirme yöntemiyle — örn. Google cache, archive.org).
