# Staj hattından yöntem hasadı (2026-08-12) — Docker/Airflow seansı

*Kaynak: staj oturumu (Carvis, Mac Cowork, 11:40–19:53), `~/staj başlangıç`. Salih açık talimatı: "jarvisi geliştirirken işimize yarayacak olanları jarvis dosyasına ingestle" — md.49 tek-yön sınırının yazılı istisnası, YALNIZ yöntem kalemleri için. Şirket şeması / gerçek veri / iç doküman TAŞINMADI (seansta zaten yoktu; tüm malzeme public Docker+Airflow). Statü: HAM HASAT, karar değil; seçim turu/tüzük turu beklemez ama kanona kendiliğinden girmez. Kaydeden: Carvis staj-oturumu.*

## H1 — [D-ölçüm] Sağlık göstergesi ⊬ iş yükü kanıtı

- Gözlem: `healthy(s) ∀s ∈ S` (|S|=6) ∧ `HTTP-200(ui)` ∧ `api-version-döndü` ∧ `∀t ∈ tasks: failed(t)`.
- Yani: yığın-seviyesi sağlık sinyalleri ile iş-seviyesi başarı arasında **implikasyon yok**. Healthcheck kendi tanımladığı şeyi ölçer (`/api/v2/version` cevaplıyor mu), iş yükünü değil.
- JARVIS karşılığı: ölçüm bankında "servis ayakta / komut çıkış-kodu 0" sınıfı metrikler **koşum kanıtı sayılamaz**. Her yığın-doğrulaması en az bir **uçtan uca iş koşumu** + sonucun okunmasını içermeli.
- Genelleme: `yesil-ekran(x) → calisiyor(x)` YANLIŞ. Doğrusu: `is-kostu(x) ∧ sonuc-okundu(x) → calisiyor(x)`.
- Serit5 raporu §1 "boş test tiyatrosu" sınıfının altyapı versiyonu. Aynı gövde, farklı yüzey.

## H2 — [D-ölçüm] Sessiz konfigürasyon yutması + rastgele fallback

- Vaka: `AIRFLOW__API__JWT_SECRET` yazıldı; geçerli bölüm `api_auth`. Airflow bilinmeyen bölümü **hata ∧ uyarı üretmeden** yuttu.
- Fallback davranışı (kaynak: imaj içi `configuration.py:488`): secret yoksa her süreç `os.urandom(16)` ile **kendi** anahtarını üretir → dağıtık bileşenler arasında imza uyuşmazlığı → `Signature verification failed`.
- Zincir: `yanlış-anahtar-adı → sessiz-yoksayma → süreç-yerel-rastgele-varsayılan → dağıtık-uyuşmazlık → is-yükü-ölür ∧ altyapı-sağlıklı-görünür`.
- JARVIS karşılığı: config-sürücülü her sistemde **"ayar yazıldı" ≠ "ayar etkin"**. Ayrı doğrulama adımı zorunlu — burada `airflow config get-value <bölüm> <anahtar>` ile okundu. Skill/hook/settings yazan her koşum aynı borcu taşır: yazdıktan sonra **sistemin kendisine sor**, dosyaya bakma.
- Alt kural: varsayılanı "güvenli rastgele" olan ayarlar en tehlikeli sınıf — eksiklik hata vermez, çalışma zamanında ayrışma üretir.

## H3 — [D-ölçüm] Donma bir sinyaldir; dış CLI çağrıları sınırlandırılmalı

- Vaka: daemon kapalıyken `docker info` / `docker ps` hata vermedi, **süresiz asılı kaldı**. Soket *dosyası* yerinde (`ls -l` doğruladı), arkasında dinleyen yok → istemci bağlantı bekliyor.
- İki ajan-turu yandı (120 sn + 240 sn timeout). `perl -e 'alarm N; exec @ARGV'` sarmalayıcısı Go binary'sinde **kesmedi** — alarm exec sonrası beklendiği gibi davranmadı.
- Çalışan desen: protokol seviyesinde sınırlı yoklama —
  `curl -s --max-time 3 --unix-socket ~/.docker/run/docker.sock http://localhost/_ping` → `OK` | boş.
- JARVIS karşılığı: skill/araç koşumlarında **dış CLI'a timeout'suz sorgu atma**. Bounded probe + `until` döngüsü deseni; döngü üst sınırı ajan turu bütçesinin altında kalmalı (240 sn'lik poll döngüsü tek başına bir turu yedi).
- Genelleme: hata ⊬ tek arıza biçimi. `{hata, yanlış-cevap, **sessizlik**}` üçlüsü; üçüncüsü en pahalısı çünkü zaman yer ve teşhis sinyali taşımaz.

## H4 — [D-belge] Paralel oturum sürtünmesi: `git add -A` süpürmesi

- Gözlem: yan oturum (Sonnet) checkpoint atarken `git add -A` kullandı; **bu oturumun yarım dosyaları** (`airflow-docker/docker-compose.yaml`, `docker-sozluk.md`) o commit'e girdi (`a7f31f3`). Ayrıca `airflow-docker/dags/` içine benim koymadığım bir DAG düştü.
- Zarar oluşmadı (aynı çalışma ağacı, dosyalar zaten hedeflenen içerikteydi) ama desen kırılgan: **iki oturum + tek çalışma ağacı + `add -A` = bir oturum diğerinin yarım işini yayımlar.**
- CLAUDE.md'deki mevcut fren ("yan oturum mevcut dosyayı DÜZENLEMEZ") bu vakayı **kapsamıyor** — düzenleme değil, *commit'leme* yoluyla temas.
- Aday kural (Salih masasına, karar değil): paralel vardiyada `git add -A` yasak; her oturum **kendi dosyalarını yol vererek** commit'ler (`git commit <path>`).
- Ekleme-esaslı yazım kuralı ise **çalıştı**: günlük dosyasına yazmadan önce yeniden okuma yapıldı, `Edit` eşleşmedi, yan oturumun 40+ satırı korunarak altına eklendi. Kural doğrulandı.

## H5 — [D-belge] macOS göç borcu: uygulamalar DMG'den koşuyor

- `/Volumes/` altında takılı kurulum imajları: `Docker` · `Claude` · `Slack` · `VS Code` · `Obsidian` · `DBeaver Community`.
- Çalışan Docker süreci: `/Volumes/Docker/Docker.app/...` — `/Applications/Docker.app` mevcut ve **aynı sürüm** (4.86.0) olmasına rağmen `open -a Docker` DMG kopyasını seçti (Launch Services kayıt sırası).
- Risk: imaj çıkarılırsa uygulama yarısında ölür; güncelleme hattı ikiye ayrılır; disk boşuna dolu.
- ⚠️ **`/Volumes/Claude` üstünden Cowork oturumu koşuyor olabilir** — eject oturumu düşürür. Temizlik sıralı ve Claude sonda yapılmalı.
- Hafızadaki "Windows'a özgü 3 kalem açık" borcunun muhtemel dördüncü kalemi; JARVIS Mac göç listesine eklenmeli.

## H6 — [K] Skill isim ikilenmesi (açık kalem)

- Skill listesinde iki ad: `gunaydin-vardiya` ∧ `anthropic-skills:gunaydin-vardiya`. Diskte **tek dosya** (`~/jarvis/.claude/skills/gunaydin-vardiya/SKILL.md`); ikincisi senkron kopya.
- Şimdilik zararsız; ayrışırlarsa hangi sürümün koştuğu belirsizleşir → sessiz davranış farkı (H2 ile aynı sınıf).
- Not: bu seansta bulunan diğer iki kalem (`C:\JARVIS` sabit yolu · staj hattının eksikliği) JARVIS oturumunca **kapatıldı** — `132f597`, `b1338c7`. Bu kalem açık kaldı mı, JARVIS oturumu doğrulasın.

## H7 — [D-yöntem] Tahmin-önce çevriminin sessiz ön-koşulu: taban seviye

*(Ekleyen: ana staj oturumu, Docker öğretim hattı 13:30–14:10. Yukarıdaki H1-H6 yan oturumun hasadı; bu kalem orada yok.)*

- **Vaka:** Docker Ders 1'e 5 adımlı çevrimin kitabına uygun biçimde başlandı — 5 soruluk yazılı tahmin seti, koşumdan önce, soğuk. Salih beşini de cevaplayamadı. Sebep bilgi eksikliği DEĞİL, **referans eksikliği**: "postgres ne demek bilmiyorum", "konteyner dediğin şeyi görmeden bilemem", "terminale yazınca ne oluyor bilmiyorum".
- **Teşhis:** `tahmin-yazilabilir(x)` yükleminin sessiz bir ön-koşulu var — öğrenenin `x`'e ait en az bir **duyusal referansı** (görmüş/çalıştırmış/ekranda karşılaşmış) olmalı. Referans yoksa çevrim tahmin değil **boşluk** üretir; oturum ilerlemez ve öğrenen kendini beceriksiz sanır (ikinci maliyet, ölçülmüyor).
- **Formel:** `taban(x) ∧ 5-adimli-cevrim(x) → ogrenme(x)` — kanon bugüne dek yalnız sağ tarafı yazıyordu, `taban(x)` yazılı değildi. STAJ-PLANI m."pazarlıksız kurallar" çevrimi koşulsuz ilan ediyor.
- **Çalışan desen (aynı oturumda koşuldu, sonuç alındı):** taban altındayken **göster→adlandır** turu — (1) çalıştır ve gördür, (2) `🏷️ bunun adı X` ile terimi koy, (3) tersini gösterip sınırı çiz (konteyneri sil → yazı gitti; volume ile tekrarla → yazı kaldı). 40 dakikada 9 terim, hepsi ekranda kanıtlı. Tahmin çevrimi ertesi güne (soğuk tekrar) ertelendi — **iptal değil, sıralama.**
- **JARVIS karşılığı:** aynı hata sınıfı Carvis'in kendi çıktı-tasarımında da var — *anlama-kapısı* (`ogrenme/anlama-kapisi.md`) ve V55 "öğretme revizyonu" hattı, öğrenenin tabanını ölçmeden kapı açıyor. Aday kural: **her öğretim turu, ilk adımda taban yoklamasıyla açılır; taban altındaysa çevrim adım-1'den değil adım-0'dan (göster→adlandır) başlar.**
- **Akraba:** m.25 (öğretme) · V55 (KURAL ADAYI, imza masasında — bu vaka onun canlı kanıtı) · m.5 (sorun-güdümlü) · H1 ile ortak gövde: *beyan değil sonuç ölçülür* — burada beyan "çevrim koşuldu", sonuç "5/5 boş cevap".
- **Yan kayıt (kullanıcı profili, karar değil):** Salih öğrenme kanalını açıkça beyan etti — *"görsel odaklı daha iyi öğreniyorum; bana bir şey yaptırıp 'bu gördüğün şeyin adı x' gibi tanımlamalar yap."* Bu bir tercih beyanı, ölçülmüş bir bulgu değil; ölçüm ertesi günkü soğuk tekrarda gelir (gösterilen ≠ hatırlanan).

## Tetik / bağlantı

- H1 + H2 aynı gövdenin iki yüzü: **doğrulama, sistemin kendi beyanına değil üretilen sonuca bakmalı.** Ölçüm bankı şemasına aday kural.
- H3 doğrudan araç-koşum disiplini; skill yazımında hemen uygulanabilir.
- H4 paralel-vardiya tasarımına aday fren; Kun-Chen workflow kurulumunda masaya gelmeli.
- H5 + H6 Mac göç borcu listesine.
- H7 öğretim-tasarımı hattına: V55 imza masasına canlı kanıt olarak eklenir; anlama-kapısı metni taban-yoklaması alanı için gözden geçirilir. Çürütme koşulu ucuz: ertesi günkü soğuk tekrarda Docker terimleri tutmazsa göster→adlandır turu tek başına yetmiyor demektir (o zaman sorun sıralama değil, tekrar aralığı).

---

## H8 — [D-ölçüm] Görsel artefaktın sessiz hata sınıfı: üretildi ≠ okunabilir

*(Ekleyen: ana staj oturumu ~19:56, veri-ambarı anlatım hattı. H1-H6 yan oturumun, H7 Docker öğretim hattının; bu kalem ikisinde de yok.)*

- **Vaka:** 7 şekilli bir öğrenme HTML'i üretildi (elde çizilmiş SVG). Dosya geçerli, tarayıcı hata vermiyor, konsol temiz. Tarayıcı paneli ise ekran görüntüsünden sonra her seferinde kapandı, kaydırma komutları zaman aşımına düştü — **göz kontrolü fiilen imkânsızdı.**
- **Teşhis:** görsel artefaktın kendine özgü bir arıza sınıfı var — `üretildi(x) ∧ ¬hata(x) ∧ ¬okunabilir(x)`. Metin kutu dışına taşar, iki etiket üst üste biner, ok başı görünmez kalır. Derleyici yok, test yok, uyarı yok. Kod tarafındaki *sessiz mantık hatası*nın artefakt yüzeyi.
- **Çalışan desen:** göz yerine ölçüm — DOM'dan her metnin `getBBox()` alınır, üç tarama koşar: (1) `viewBox` taşması, (2) metin-metin kesişimi (tolerans eşikli), (3) `url(#id)` referansının aynı belgede çözülmesi. Tek koşumda 2 gerçek arıza çıktı: 96 px etiket örtüşmesi + 10 adet `context-stroke` ok başı (tarayıcı desteği tekdüze değil, sessizce kaybolur). Düzeltildi, ikinci tur `{badMarkers:[], overlaps:[], overflow:[]}`. **Panel hiç açılmadan artefakt doğrulandı.**
- **H1 ile bağ:** aynı gövde, üçüncü yüzey. H1 "servis sağlıklı ⊬ iş koştu", H2 "ayar yazıldı ⊬ ayar etkin", H8 "dosya üretildi ⊬ artefakt okunabilir". Ortak yüklem: **üretici aracın kendi beyanı kanıt sayılmaz.** Üçünün de çözümü aynı biçimde: bağımsız bir ölçüm, sonucun okunması.
- **Kendi ayağına sıkma tuzağı (aynı vakada yaşandı):** denetim, diskteki güncel sürümü yansıtmayan bayat bir sekmede koştu ve düzeltilmiş referansları "kırık" gösterdi. Ters yönü daha pahalı — eski temiz sürümde koşan denetim yeni arızayı hiç görmez, üstelik "temiz" raporlar. *Doğrulama aracının okuduğu sürüm, doğrulanan sürüm mü?* Aynı yüklem [[pointer-sistemi]] gotcha'sındaki mount/senkron tuzağıyla (07-12) aynı — iki vaka, birleştirme adayı.
- **JARVIS karşılığı:** artefakt üreten her koşum (HTML rapor, diyagram, görsel anlatım) teslimden önce ölçüm kapısından geçer; "iyi görünüyor" teslim gerekçesi değildir. Ekran görüntüsü de yeterli değil — tek ekran kapsar, 7 şekilli dosyada örneklem hatasıdır.
- **Kapsam sınırı (fazla söz vermemek için):** bu tur yalnız metin-metin kesişimini tarıyor; metin-çizgi ve kutu-kutu örtüşmesi ölçülmüyor.
- **Çıktı:** [[gorsel-artefakt-dogrulama]] wiki sayfası (6 bloklu şema, SOP + 6 gotcha) + index kaydı.
