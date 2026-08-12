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

## Tetik / bağlantı

- H1 + H2 aynı gövdenin iki yüzü: **doğrulama, sistemin kendi beyanına değil üretilen sonuca bakmalı.** Ölçüm bankı şemasına aday kural.
- H3 doğrudan araç-koşum disiplini; skill yazımında hemen uygulanabilir.
- H4 paralel-vardiya tasarımına aday fren; Kun-Chen workflow kurulumunda masaya gelmeli.
- H5 + H6 Mac göç borcu listesine.
