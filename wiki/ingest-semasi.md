# İngest Şeması — Anlatım

*Bu sayfa ANLATIR, kural koymaz. Sözleşmenin kendisi: `core/ingest-semasi.md` (jarvis v2) + `~/staj başlangıç/ingest-semasi.md` (staj v1). Kanıt tabanı: `cc/rapor/2026-08/rapor-2026-08-14-1.md`. İlgili: [[pointer-sistemi]].*

## Sorun neydi?

Staj döneminde aynı anda 3-5 sekme açık: staj oturumu + jarvis oturumu + konu-başına yan sekmeler. Her sekme kendi bağlamında bir şeyler üretiyor; çıktılar dağınık kalıyor, borçlar sessizce yığılıyor, kapsül/hafıza hızla şişiyor. Veri mühendisliğinde bunun bilinen adı var: **şemasız ingest → data swamp** (bataklık). Data engineer'ların veri şeması neyse, bizim de bilgi-akışı için aynı disipline ihtiyacımız vardı.

## Fikir tek cümlede

**Her oturum çıktısı, kim olduğunu söyleyen küçük bir zarfla tek toplama noktasına düşer; oradan tipine göre doğru rafa dağıtılır; raflar dolunca eşikte topluca damıtılır; ve hiçbir kayıt sessizce kaybolamaz.**

## Beş parça

**1. Zarf — 5 alan, fazlası yok.** Her kayıt tek satırla kendini tanıtır:
`[tip: karar | kaynak: jarvis-terminal 08-14 | tarih: 2026-08-14 | hedef: defter | sema: v2]`
Neden sadece 5? Araştırmanın en güçlü bulgusu: **ağır şema ölür.** En olgun metadata standartları (Dublin Core, schema.org) sıfır zorunlu alanla tasarlanmış; tek zorunlu form-adımı kaldırmanın ölçülmüş bedeli +%45 dönüşüm ($300M button vakası). Doldurulamayan alana `-` yazılır — alan atlanmaz ("doldurulmadı" ile "yok" ayrımı korunur).

**2. Tip — kapalı 8'li küme.** karar · kural-adayı · borç · bulgu · ders · kavram · ham · diger. Her tipin varsayılan bir evi var (karar→defter, ders→KILAVUZ, kavram→wiki...). `borç` tipinin özel kuralı: `dogrulama:` alanı şart ve **DONE = o prosedür koştu** — "yapıldı yazıldı" değil. Borç-yığılmasının panzehiri tam bu satır.

**3. Triyaj — 4 soru (Mem0'dan).** Kayıt kanona girerken sorulur: eşdeğeri var mı (**NOOP** — dokunma) · mevcut kaydı tamamlıyor mu (**UPDATE** — güçlendir, çift açma) · çelişiyor mu (**GEÇERSİZ-KIL** — eskiyi silme, tarih damgala; m.8/m.16 ile birebir) · hiçbiri mi (**ADD**). Bu triyaj, ölçülmüş sistemlerde token maliyetini ~%73, gecikmeyi %91 düşüren mekanizmanın araçsız hâli.

**4. Katman akışı — event sourcing.** `kuyruk/` = append-only olay günlüğü ve **gerçek kaynak**; kapsül = **snapshot** (hız optimizasyonu — kaybolsa sistem kuyruk+defter+git log'dan yeniden kurulur); pano = projeksiyon. Kuyruk kaydı asla silinmez; hata düzeltme = telafi kaydı ekle. Bu, m.8'in (silme yasağı) mühendislik gerekçesidir.

**5. Tetikler ve bütçeler.** Kapsül ≤200 satır (aşınca damıtma, ~%50 boşalt) · damıtma tetiği = kuyruğa girenlerin **önem toplamı ≥150** (40 önemsiz not tetiklemez, 8 kritik not tetikler) · paralel sekmeden dönen devir raporu **≈1.000-2.000 token** tavanlı · damıtma her oturumda değil **eşikte ve toplu** (her damıtma bir maliyettir — LSM dersi).

## Bir günün akışı (örnek)

Sabah stajda üç sekme açtın. Yan sekmede Airflow araştırması yaptırdın → kapanışta günlüğe `Gelen: airflow-scheduler` bölümü olarak **özetini** yapıştırdın (ham döküm değil). Öğleden sonra jarvis sekmesinde bir karar çıktı → sekme kapanırken `kuyruk/gelen-2026-08-14-x.md`'ye zarflı tek dosya bıraktı. Akşam ana vardiya triyaj koştu: 2 kayıt NOOP (zaten kanonda), 1 UPDATE (mevcut wiki sayfasına işlendi), 1 çelişki (eski karara geçersiz-damgası + sana çelişki raporu), 3 ADD, 1 kayıt tip alamadı → SINIFLANDIRILAMADI'ya düştü, yarın tekrar denenecek. Hiçbir şey kaybolmadı; kapsül şişmedi.

## Matematiksel temel (neden "anlamlı")

- **Append-only log + snapshot + projeksiyon** = event sourcing — durum her an ham kayıtlardan yeniden türetilebilir; snapshot bozulsa bilgi kaybı sıfır.
- **Önem × üstel çürüme + kümülatif eşik** = Generative Agents getirim modeli (`önem 1-10`, λ kaynakta 0,995/sandbox-saati, tetik Σönem≥150; ablasyon etki büyüklüğü d=8.16). **[DÜZELTİLDİ 08-21, Karar 59 (KB-42 A): kaynak 0,995/sandbox-SAATİ (α üçlüsü = 1, gerekçesiz); Jarvis'e değer TAŞINMAZ — form tazelik(t)=d^t, t=SEANS, d kalibre edilmemiş [?] (ölçüm gelene dek skorlamada kullanılmaz); T-Ç6 kuralı doğdu: katsayı = kaynaktaki değer+birim, aksi damgalı — `core/ingest-semasi.md:47` + `cc/rapor/2026-08/rapor-2026-08-17-1.md` S4]** v1 şemasındaki `e^(−λt)` formülünün eksik iki parçası buradan tamamlandı.
- **Eşikli toplu compaction** = LSM-tree — write amplification >10: her damıtma pahalıdır, o yüzden seyrek ve toplu yapılır.
- **Bütçeler** = MemGPT'nin %70-uyarı/%100-tahliye/%50-boşaltma üçlüsü + Claude Code'un 200-satır/25KB indeks limiti (aşan kısım hiç yüklenmez — sıcak bağlam sabit-bütçeli tutulmak zorunda).

## Gotchas

- **Zarfı atlama, değeri atla:** bilinmeyen alana `-` yaz; zarfsız kayıt triyaja giremez.
- **DONE tiyatrosu:** doğrulama prosedürü koşmadan borç kapatma — en pahalı sessiz hata sınıfı.
- **Kapsüle tarihçe yazma:** kapsül "şu an"dır; hikâye commit'lerde ve raporlarda yaşar.
- **`diger` sayacı yükseliyorsa** yeni bir tip doğuyor demektir — küme additive-only genişletilir, tip asla silinmez (deprecated edilir).
- **Damıtmayı erkene alma:** eşik gelmeden damıtmak write-amplification'dır; eşiği bekle, toplu yap.

**Bağlantılar:** · [[ai2ai-rapor-formati]] (karşı-link 08-22) · [[baglam-veri-ambari]] (karşı-link 08-22) · [[kokenler-karpathy-llm-wiki]] (karşı-link 08-22) · [[paralel-oturum-protokolu]] (karşı-link 08-22) · [[silver-saglik]] (karşı-link 08-22) · [[baglam-anahtar-kaydi]] (karşı-link 08-29)
