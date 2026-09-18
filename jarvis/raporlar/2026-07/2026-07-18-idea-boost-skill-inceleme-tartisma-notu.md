# idea-boost Skill İncelemesi — Cowork Tartışma Notu

> **DAMGA: TARTIŞMA NOTU (ham/aday) — KARAR ALINMADI, KANONA DOKUNULMADI.** Salih emri (07-18): "araştırma sonucunu ve yorumları coworkte tartışmak üzere rapor oluştur." İnceleme 07-17 gecesi Atlas koşumuyla yapıldı (dış repo okuması), JARVIS-bağlam analizi 07-18 Cowork ana-sıra/Fable oturumunda Carvis tarafından eklendi. Bu dosya gündem malzemesidir; karar çatalları §4'te, imza gerektirenler işaretli (m.31/m.41).

**Konu:** `https://github.com/yagizkaterli/idea-boost` — küçük açık-kaynak Claude Code skill'i (hızlı fikir-serilerini 7 adımlı tek geçişte işleyip idea-pool'a tek girdi olarak bankalayan akış).
**İlişkili yüzeyler:** `fikir-kutusu.md` (V25 altın kural + V34 skill-avcısı + V-serisi giriş disiplini) · `core/tuzuk-v0.md` (m.16 çelişki kapısı · m.20 pointer · m.25 görev-ölçek · m.31 karar yetkisi) · `cc/rapor-2026-07-13-1.md` (K-017 dış-ürün taraması — bu inceleme aynı ailenin tekil-derin örneği) · V54 (literatür-simetri deseni).

---

## 1. Dış inceleme sonucu (Atlas koşumu, 07-17 gece; kaynak: repo README.md + SKILL.md tam metni, master dalı)

Salih'in verdiği 6-başlıklı sabit formatla:

### 1.1 WHAT-I-UNDERSTOOD
Kullanıcı ard arda yarım-şekilli fikirler fırlattığında her birine tek tek "not aldım" demek yerine, tüm seriyi tek disiplinli geçişte (collect → ground → extend → object → link → steer → bank) işleyip TEK idea-pool girdisine indirgeyen bir Claude Code skill'i. `/idea-boost` komutuyla veya "2+ hızlı seed-mesaj" ile otomatik tetiklenir; yalnız tohum katmanında çalışır, kod/execution yapmaz.

### 1.2 STRONGEST-OBJECTION
Tetikleme–maliyet orantısızlığı: "2+ hızlı seed-mesaj" otomatik tetikleyicisi çok düşük eşik — sıradan sohbette yanlış-ateşlenir, basit ikinci soruya 7-adımlı ağır prosedür biner. Ayrıca GROUND adımı ("ground against existing notes with file pointers") yapılandırılmamış/boş notes dizininde ya çöker ya uydurma pointer üretir — skill'in kendi "no unsourced claims" vaadini ihlal eder. En yüksek değer verilen adım aynı zamanda en kırılgan adım.

### 1.3 STEP-VERDICTS
- COLLECT — KEEP: tek harita üretmesi çekirdek değer.
- GROUND — CHANGE: kaynak yoksa graceful degrade gerek.
- EXTEND — KEEP: etiketleme disiplini temiz ayrım sağlıyor.
- OBJECT — KEEP: zorunlu itiraz en özgün katkı.
- LINK — CHANGE: küçük projede aşırı-mühendislik, opsiyonel olmalı.
- STEER — KEEP: karar çatalları eyleme dönüştürülebilir çıktı.
- BANK — KEEP: tek-girdi append kart-enflasyonunu doğru önlüyor.

### 1.4 WOULD-I-RUN-IT
ONLY-IF — yalnız `/idea-boost` explicit komutuna bağlanırsa; otomatik tetikleyici açıkken hızlı fikir fırlatan kullanıcı için gürültü + token israfı (her ikinci mesajda 7 adım akışı boğar).

### 1.5 ONE-IMPROVEMENT
SKILL.md frontmatter `description` içindeki "fires 2+ rapid seed-messages" tetikleyicisi: eşik en az 3-4 seed + zaman/yoğunluk penceresi, ya da otomatik tetikleme tamamen kaldırılıp yalnız komuta bağlanmalı. İkincil: GROUND adımına "if no ground sources configured, skip with explicit note" fallback'i.

### 1.6 MISREAD-RISK
Ortalama kullanıcı Configuration bölümünü atlar: idea-pool dosyası + ground-sources listesi ayarlanmadan kurulur → BANK var olmayan dosyaya yazmaya çalışır, GROUND kaynak bulamaz. İkincisi: otomatik tetiklemenin farkına varmadan sıradan sohbette 7-adımlı çıktı görüp şaşırma — README otomatik tetiklemeyi vurgulamıyor, yalnız SKILL.md frontmatter'ında gömülü.

---

## 2. JARVIS-bağlam analizi (Carvis, 07-18)

### 2.1 Ana hüküm: KURULMAZ, İLHAM ALINIR
V25 altın kuralı (imzalı, 07-11 gece) bu vakayı doğrudan çözer: *"her skill'i sonunda BİZ kurarız, kurallarını BİZ belirleriz — kaliteli hazır skill'lerden yalnız İLHAM alınır."* idea-boost tam hedef sınıfta: kaliteli fikir taşıyan dış-ürün, kurulum masada değil. Ek çelişki: skill'in kendi kendine ateşlenmesi (otomatik tetik) m.25 görev-ölçek düzenine (ölçek-tercihi Carvis'te, sabit prosedürde değil) ve K-009 öncesi otomasyon-yok sınırının ruhuna aykırı — kurulsaydı m.16 kapısı zaten koşacaktı.

### 2.2 Asıl bulgu: skill, Carvis'in ELLE yaptığı işin dışarıda yazılmış hali
Yedi adımın JARVIS karşılıkları neredeyse birebir mevcut — K-017/V54 çerçevesinde anlamlı veri: fikir-giriş disiplinimiz dışarıda bağımsız keşfedilmiş (dar-odak V39 koşumundaki "9/12 TAM" dersiyle aynı yönde: tasarımlarımız bilinen ailelere oturuyor).

| idea-boost adımı | JARVIS'teki mevcut karşılık | Durum |
|---|---|---|
| COLLECT | Fikir kutusu tek yüzey + tarih/damga satırı | VAR |
| GROUND | m.20 pointer disiplini (tam metin kaynağa işaret eder, kopyalanmaz) | VAR, daha sıkı |
| EXTEND | Carvis şerhi / "akraba:" bağlantı notları | VAR, gayriresmî |
| OBJECT | m.16 çelişki kapısı | VAR ama yalnız KARAR katmanında |
| LINK | [[wiki-link]] standardı (V24) + "İlişkili yüzeyler" blokları | VAR |
| STEER | Seçim turu (aday → seçildi/ertelendi/çürüdü) | VAR |
| BANK | Kutuya tek satır + V-numarası | VAR, ama fikir-başına (seri-başına değil) |

Skill'in en kırılgan adımı (GROUND — kaynak yoksa uydurma pointer) bizde geçersiz: kaynak zemini (kutu, tüzük, raporlar/) mevcut ve m.39 rakam-disiplini uydurmayı ayrıca yasaklıyor.

### 2.3 İlham alınmaya değer 2 nokta (bizde eksik olan)
1. **İtirazın tohum katmanına indirilmesi.** m.16 çelişki kapısı kararlarda çalışıyor; ham fikir kutuya girerken zorunlu itiraz adımı yok — çelişkiler devralınmış borç olarak sonradan yakalanıyor (kanıt: V7↔V8↔V14 çelişki tablosu girişte değil rapor-devrinde oluştu). Aday kural: "kutuya giren her fikir bir satırlık itiraz/çelişki notuyla girer." Ucuz sigorta; maliyeti fikir-başına ~1 satır.
2. **Seri-işleme protokolü.** Salih'in gerçek kullanım deseni tam olarak skill'in hedef deseni (V31-V38 "oyun arası ham not" serileri). Bugün her fikir tek tek V-satırı oluyor; adlandırılmış bir mini-protokol ("bir oturuş = bir toplu geçiş: topla → çelişki tara → seçim-turu çatalları çıkar → kutuya yaz") vardiya-kapanış özütünün fikir-tarafı boşluğunu doldurur. NOT: skill'in "seri = TEK girdi" sıkıştırması bizde V-numaralama + pointer disiplinini kırar — alınacak şey sıkıştırma değil, GEÇİŞİN adlandırılmış/adımlı olması.

### 2.4 Karşı-kayıt (dürüst kayıt, V42 deseni)
- Tohum-katmanı itiraz zorunluluğunun riski: giriş sürtünmesi artar — Salih'in hızlı-fırlatma akışını yavaşlatırsa fikir kaybı üretir (skill'in kendi STRONGEST-OBJECTION'ının bizdeki izdüşümü). Sigorta adayı: itiraz satırı Carvis'in işi, Salih'in akışına dokunmaz; itiraz bulunamazsa "itiraz: yok" yazılır, boş bırakılmaz.
- Mini-protokol adlandırması meta-iş tuzağına (V2 şerhi) yaklaşır: zaten fiilen yapılan işi törenselleştirme riski. Ölçüt: protokol yalnız ≥3 fikirlik serilerde koşar, tekil fikir bugünkü gibi tek satır düşer.

---

## 3. V54 verisi (yan bulgu)
"Şirket simülasyonu dışarıda yok" (K-017) bulgusunun aksine, fikir-giriş disiplinimizin dışarıda küçük ama birebir bir karşılığı ÇIKTI. V54 simetrisinin öteki yarısı: eşleşme bulunması da tasarımın doğrulaması değildir — yalnız "bilinen aileye bağlandı" (V48) kaydıdır. Tek hakem kendi koşum verisi.

## 4. Cowork tartışma gündemi (karar çatalları)

| # | Çatal | Katman | Seçenekler |
|---|---|---|---|
| 1 | Tohum-katmanı itiraz kuralı (§2.3-1) | **Katman 1** (kural/kanon — imza masası, m.41: ana-sıra ∧ Fable ∨ Salih-imza) | (a) kural adayı olarak imza masasına · (b) önce deneysel-damgalı pratik (m.29), N fikir sonra imza · (c) ret |
| 2 | Seri-işleme mini-protokolü (§2.3-2) | Katman 2 aday (format kararı, m.29 deneysel damga) — Salih görüşü alınarak | (a) deneysel başlat (≥3 fikir eşiğiyle) · (b) K-019 boş-vardiya paketine ertele · (c) gereksiz — mevcut pratik yeterli |
| 3 | Kutuya V-kaydı: "V25 altın-kuralın ilk canlı uygulama vakası + 2 ilham maddesi" tek satırı | Katman 2 | (a) yaz · (b) bu rapor pointer'ı yeter, satır açma |
| 4 | V34 (skill-avcısı ajan) bağlantısı: bu inceleme V34'ün elle yapılmış prototipi — K-009 açılış gündemindeki V34 maddesine "ilk manuel koşum örneği" pointer'ı düşülsün mü? | Katman 2 | (a) pointer düş · (b) gerek yok |

**Carvis önerisi (tek cümle):** 1(b) + 2(a) + 3(a) + 4(a) — hepsi ucuz-revert sınıfı (m.40c kademeli-yürürlük kapsamında ŞİMDİ uygulanabilir), yalnız çatal-1'in kural-statüsü imzaya kalır.

---
*Rapor: Carvis, 2026-07-18 (Cowork ana-sıra/Fable). Dış-okuma kaynağı: Atlas koşumu 07-17 gece (repo master dalı; main 404). Proof-of-work: bu dosyanın push'lanmış commit'i (m.9).*
