#!/usr/bin/env python3
"""İB-43 altın soru seti büyütme (25 → ≥100; Karar 66 / Karar 74 M-2 a). Her soru: (id, yetenek, soru, beklenen_dosya[], dogrulama_terim).
Kapı: beklenen her dosya VAR ∧ dogrulama_terim dosyada GEÇİYOR (büyük/küçük harf duyarsız) → eklenir; aksi halde listelenir, eklenmez.
Çekimserlik soruları: beklenen [] — korpusta cevap OLMAMALI; otomatik sağlama: terim hiçbir md/json dosyasında geçmiyorsa PASS (zayıf kontrol, kestirim damgalı)."""
import json, os, subprocess, sys
REPO = "/Users/HasanSalihSahin/jarvis"; YOL = os.path.join(REPO, "veri/sozlesme/erisim-eval-sorular.jsonl")
NOT = "Carvis-yazımı KESTİRİM 08-29 (İB-43 ≥100 büyütme; Karar 66 + Karar 74 M-2 a); beklenen dosya doğrulama-terimiyle grep PASS; Salih teyidi bekler"
S = [
 # ---- bilgi-cikarma (15) ----
 ("S26","bilgi-cikarma","anakronizm yasağı zaman-bağımlı iddia AS-OF damgası model hafızası kesim",["wiki/anakronizm-freni.md","CLAUDE.md"],"AS-OF"),
 ("S27","bilgi-cikarma","damıtma hedefi oran değil sorgu-uyumu hangi sorulara cevap vermeli",[".claude/skills/damitma/SKILL.md"],"SORGU-UYUMU"),
 ("S28","bilgi-cikarma","karar-borcu tablo kırık pointer FAIL-LOUD çıkış kodu 3",["tools/SCRIPTLER.md","tools/karar-borcu-tablo.py"],"kırık"),
 ("S29","bilgi-cikarma","hareket kütüğü araç çağrıları transkriptten bronz hareket-olay jsonl",["CLAUDE.md","tools/SCRIPTLER.md"],"hareket-olay"),
 ("S30","bilgi-cikarma","damıtma sonrası sessiz satır kayması pointer-kayma eski satır metni",["tools/SCRIPTLER.md",".claude/skills/damitma/SKILL.md"],"pointer-kayma"),
 ("S31","bilgi-cikarma","bayatlık kuyruğu seans kapanışında N=3 yeniden-çekim 90 gün eşik",["wiki/anakronizm-freni.md",".claude/skills/seans-kapanis/SKILL.md"],"90 gün"),
 ("S32","bilgi-cikarma","tipli bağ katmanı wasRevisionOf süpersede bag tablosu kural-tabanlı",["veri/README.md","tools/bag-tablo.py"],"wasRevisionOf"),
 ("S33","bilgi-cikarma","Lavish masa karar yüzeyi kuyruk-prompt Send&End hükümler",["kuyruk/senaryo-defteri.md"],"Lavish"),
 ("S34","bilgi-cikarma","ekran ses kaydı screencapture önce haber onay permissions ask",["core/durum-kapsulu.md","kuyruk/senaryo-defteri.md"],"screencapture"),
 ("S35","bilgi-cikarma","world model tasarımı grain bildirimi 1 satır ne",["core/world-model-tasarimi.md"],"grain"),
 ("S36","bilgi-cikarma","kural sayacı eşzamanlı kural sayısı eşik 100",[".claude/skills/seans-acilis/SKILL.md",".claude/skills/seans-kapanis/SKILL.md"],"kural-sayaci"),
 ("S37","bilgi-cikarma","FTS5 BM25 erişim katmanı genişletme zaman güncel yüzey eval",["tools/erisim-fts.py","tools/SCRIPTLER.md"],"fts5"),
 ("S38","bilgi-cikarma","deterministik tasarım aynı girdi aynı yol rastgelelik tasarım aracı değil",["CLAUDE.md","core/tuzuk-v0.md"],"deterministik"),
 ("S39","bilgi-cikarma","teslim usulü tam mutlak yol open -R Finder ilk ekran mobil uyum",["CLAUDE.md"],"open -R"),
 ("S40","bilgi-cikarma","idempotens sistematik entegrasyon araştırması icra borcu KB-18",["kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-21.md","kuyruk/senaryo-defteri.md"],"idempoten"),
 # ---- cok-oturum (15) ----
 ("S41","cok-oturum","Opus yan-oturumu devir dosyası Fable ana-sıra icra Karar 70 EK",["kuyruk/devir-2026-08-26-seans17-fable.md","core/durum-kapsulu.md"],"devir"),
 ("S42","cok-oturum","GBM CatBoost dersi YetiRank QuerySoftMax sızıntı hatası uplift",["kuyruk/ders-gbm-ilerleme.md","core/durum-kapsulu.md"],"YetiRank"),
 ("S43","cok-oturum","galeri scoring korelasyon Spearman Redshift SQL feature temizliği",["raporlar/seans-teslim-2026-08-29-galeri-scoring-korelasyon.md","core/durum-kapsulu.md"],"Spearman"),
 ("S44","cok-oturum","entegrasyon masası 13 kalem E-4 erteleme beyanı masa sırası",["kuyruk/masa-gundemi-entegrasyon-2026-08-21.md","core/durum-kapsulu.md"],"E-4"),
 ("S45","cok-oturum","fren delinme $30,94 1,89× çağrı sayısı freni kök neden analizi",["raporlar/2026-08-29-ib54-delinme-kok-neden.md","kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-17.md"],"30,94"),
 ("S46","cok-oturum","pointer grafı İB-48 3/3 kapandı graf adımı hatta anakronizm lint",["core/durum-kapsulu.md","graf/README.md"],"İB-48"),
 ("S47","cok-oturum","Karar 71 PR-per-chat ret üç katmanlı çok-oturum düzeni ana-sıra yan-oturum",["KILAVUZ.md","core/durum-kapsulu.md"],"Karar 71"),
 ("S48","cok-oturum","vaka-5 pathspec commit SOP kapanmış yan-oturumun dosyaları",["kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-29.md","core/durum-kapsulu.md"],"vaka-5"),
 ("S49","cok-oturum","MIT 6.042J birebir kurs BK-2 varlık felsefesi matematik ansiklopedi",["core/varlik-felsefesi.md","kuyruk/senaryo-defteri.md"],"6.042J"),
 ("S50","cok-oturum","deneyim çifti PASS FAIL yörüngesi kural adayı ExpeL kanalı",[".claude/skills/damitma/SKILL.md","tools/SCRIPTLER.md"],"deneyim"),
 ("S51","cok-oturum","bağlam seyri statik önek 128K üstü oturum uzun-koşum hasat listesi",[".claude/skills/seans-kapanis/SKILL.md","core/durum-kapsulu.md"],"128K"),
 ("S52","cok-oturum","skill hazinesi 16 skill repo tek kaynak bulut kopyaları silinecek",["core/durum-kapsulu.md"],"hazinesi 16"),
 ("S53","cok-oturum","staj klasör ayrımı md.49 staj verisi Jarvis'e taşınmaz",["core/pano.md",".claude/skills/seans-acilis/SKILL.md"],"md.49"),
 ("S54","cok-oturum","Kun-Chen ailesi no-mistakes lavish gnhf treehouse sürümleri",["core/durum-kapsulu.md"],"treehouse"),
 ("S55","cok-oturum","iki ölçüm noktası Sonnet pini alt-ajan payı %15,4 %31,7",["cc/rapor-2026-08-01-4.md","kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-17.md"],"31,7"),
 # ---- zamansal (15) ----
 ("S56","zamansal","2026-08-29 damıtma turu dört dosya bütçe altına indi",["raporlar/2026-08-29-damitma-turu.md"],"2026-08-29"),
 ("S57","zamansal","Karar 74 ikinci Lavish masası 9/9 hükümleri 08-29",["kuyruk/senaryo-defteri.md"],"Karar 74"),
 ("S58","zamansal","Karar 69 ilk Lavish masa KB-62..68 08-26",["kuyruk/senaryo-defteri.md"],"Karar 69"),
 ("S59","zamansal","08-22 seans-14 paralel icra oturumu İB-42 İB-43 kısmen kapandı",["core/durum-kapsulu.md"],"SEANS-14"),
 ("S60","zamansal","Karar 73 08-29 jarvis varlık felsefesi makine matematik",["kuyruk/senaryo-defteri.md","core/varlik-felsefesi.md"],"Karar 73"),
 ("S61","zamansal","cleanupPeriodDays 365 Salih imzası 08-01 gece iz saklama",["kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-17.md"],"cleanupPeriodDays"),
 ("S62","zamansal","2026-08-21 damıtma turu defter 89,6 28,4 arşiv",["raporlar/2026-08-21-damitma-turu.md","core/durum-kapsulu.md"],"28,4"),
 ("S63","zamansal","gece senkron son kayıt FAIL-ff 2026-08-04",["raporlar/usage/senkron-log.jsonl"],"FAIL-ff"),
 ("S64","zamansal","Mac geçişi 08-12 L8 envanter 11/11 canlı beyanı Karar 35",["core/pano.md","raporlar/vardiya-teslim-2026-08-12-l8-mac.md"],"11/11"),
 ("S65","zamansal","Karar 62 adresli erişim 08-18 vakası 25/27 blok uyuşmazlığı",[".claude/skills/seans-acilis/SKILL.md"],"25/27"),
 ("S66","zamansal","hareket günlüğü 2026-08-29 bu seansın araç çağrıları",["raporlar/hareket-gunlugu-2026-08-29.md"],"2026-08-29"),
 ("S67","zamansal","Karar 39 08-20 kök-neden önce fren tetiklenme koşulu zor",["kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-21.md"],"Karar 39"),
 ("S68","zamansal","K-009 otomasyon açılışı 07-19 kurucu kararlar imzalı",["core/pano.md"],"K-009"),
 ("S69","zamansal","anahtar kaydı 2026-08-15 günaydın emekli seans başı güncel",["core/baglam-anahtar-kaydi.md"],"2026-08-15"),
 ("S70","zamansal","Karar 57 resume eki canlı-oturum kapısı her resume'da git log",[".claude/skills/seans-acilis/SKILL.md"],"Karar 57"),
 # ---- bilgi-guncelleme (15) ----
 ("S71","bilgi-guncelleme","patron yerine Salih'in rol adı ne oldu",["core/baglam-anahtar-kaydi.md"],"patron"),
 ("S72","bilgi-guncelleme","vardiya yerine oturum birimi adı",["core/baglam-anahtar-kaydi.md"],"vardiya"),
 ("S73","bilgi-guncelleme","şirket simülasyonu yerine çalışma modeli adı",["core/baglam-anahtar-kaydi.md"],"şirket simülasyonu"),
 ("S74","bilgi-guncelleme","uyucam yerine kapanış tetiği ne",["core/baglam-anahtar-kaydi.md"],"uyucam"),
 ("S75","bilgi-guncelleme","QuickLook standardı iptal md açma yüzeyi ne oldu",["core/durum-kapsulu.md"],"QuickLook"),
 ("S76","bilgi-guncelleme","iki-chat Cowork modeli arşive indi yerine hangi düzen",["KILAVUZ.md","kuyruk/arsiv/KILAVUZ-arsiv-2026-08-29.md"],"Cowork"),
 ("S77","bilgi-guncelleme","K-019 damıtma planı imzalandı sonra koştu mu",["raporlar/2026-08-21-damitma-turu.md","core/durum-kapsulu.md"],"damıtma"),
 ("S78","bilgi-guncelleme","Windows klonu terk kanon Mac tek canlı alan KB-16",["core/durum-kapsulu.md"],"KB-16"),
 ("S79","bilgi-guncelleme","gunaydin-vardiya skill'inin yeni adı",["core/baglam-anahtar-kaydi.md"],"gunaydin-vardiya"),
 ("S80","bilgi-guncelleme","kapsül güncelleme satırı en son hangi seans kapandı",["core/durum-kapsulu.md"],"Güncelleme"),
 ("S81","bilgi-guncelleme","silver tazelik kapısı hook BAYAT uyarısı katman-hatti koşumu",[".claude/skills/seans-acilis/SKILL.md"],"BAYAT"),
 ("S82","bilgi-guncelleme","kayit tablosuna cekim_tarihi kaynak_tarihi kolonu eklendi sözleşme 1.2.0",["veri/README.md"],"cekim_tarihi"),
 ("S83","bilgi-guncelleme","sözlük dondu emekli işaretleri metafor",["wiki/sozluk.md","core/durum-kapsulu.md"],"emekli"),
 ("S84","bilgi-guncelleme","ffmpeg ekran kaydı freninin kapsamı dışında mı Karar 70 EK",["core/durum-kapsulu.md"],"ffmpeg"),
 ("S85","bilgi-guncelleme","SessionStart hook kapsülü değil 2 KB brif basıyor kapsül elle okunur",[".claude/skills/seans-kapanis/SKILL.md"],"2 KB"),
 # ---- cekimserlik (15): korpusta cevap yok ----
 ("S86","cekimserlik","Jarvis LADDER LOGIC donanım tanım modülü",[],"ladder logic"),
 ("S87","cekimserlik","Jarvis Terraform AWS altyapı modülü",[],"terraform"),
 ("S88","cekimserlik","IMC Prosperity leaderboard sıralaması puanı",[],"leaderboard sıra"),
 ("S89","cekimserlik","Fama-French faktör regresyonu beta katsayıları sonucu",[],"beta katsayı"),
 ("S90","cekimserlik","DEA-C01 sınav sonucu puanı geçti mi",[],"sınav puanı"),
 ("S91","cekimserlik","Jarvis iOS uygulaması SwiftUI kodu",[],"swiftui"),
 ("S92","cekimserlik","Jarvis Fortran sayısal modülü",[],"fortran"),
 ("S93","cekimserlik","Jarvis web arayüzü React bileşenleri",[],"react bileşen"),
 ("S94","cekimserlik","Salih'in doğum tarihi",[],"doğum tarihi"),
 ("S95","cekimserlik","Otonet staj ilk hafta 5 sorusunun cevapları",[],"ilk hafta cevap"),
 ("S96","cekimserlik","Jarvis lisans dosyası MIT mi Apache mi",[],"apache license"),
 ("S97","cekimserlik","GitHub Actions CI workflow yaml Jarvis",[],"actions/checkout"),
 ("S98","cekimserlik","PortRisk yfinance veri indirme betiği kodu",[],"yf.download"),
 ("S99","cekimserlik","Jarvis Slack botu webhook entegrasyonu",[],"slack webhook"),
 ("S100","cekimserlik","Jarvis Erlang OTP servisi",[],"erlang"),
]
def icerir(rel, terim):
    try:
        return terim.lower() in open(os.path.join(REPO, rel), encoding="utf-8", errors="replace").read().lower()
    except OSError:
        return None
r = subprocess.run(["git", "ls-files", "-z"], cwd=REPO, capture_output=True, text=True)
HARIC = ("cc/2026-08-29-erisim-soru-buyutme.py", "veri/sozlesme/erisim-eval-sorular.jsonl", "veri/erisim-eval.jsonl", "veri/gorunum/v_erisim_eval.csv")  # üreticinin kendisi + soru/eval kütükleri korpus sayılmaz (kendi-kendini-kirletme: 08-29 vakası, 13 sahte düşen)
tum = [f for f in r.stdout.split("\0") if f.endswith((".md", ".json", ".jsonl", ".py", ".sh", ".yaml", ".yml")) and f not in HARIC]
gecen, dusen = [], []
for sid, yet, soru, dosyalar, terim in S:
    if dosyalar:
        sorun = [f"{d}: {'YOK' if icerir(d, terim) is None else 'TERİM YOK'}" for d in dosyalar if not icerir(d, terim)]
    else:
        vur = [f for f in tum if icerir(f, terim)]
        sorun = [f"korpusta geçiyor: {', '.join(vur[:3])}"] if vur else []
    (dusen if sorun else gecen).append((sid, yet, soru, dosyalar, terim, sorun))
print(f"geçen {len(gecen)} · düşen {len(dusen)}")
for x in dusen:
    print("  DÜŞEN", x[0], x[1], "|", x[2][:60], "|", x[5])
if "--yaz" in sys.argv:
    mevcut = {json.loads(l)["id"] for l in open(YOL, encoding="utf-8") if l.strip() and not l.startswith("#")}
    with open(YOL, "a", encoding="utf-8") as fh:
        n = 0
        for sid, yet, soru, dosyalar, terim, _ in gecen:
            if sid in mevcut:
                continue
            fh.write(json.dumps({"id": sid, "soru": soru, "yetenek": yet, "beklenen_dosya": dosyalar, "not": NOT + f"; doğrulama-terimi: {terim}"}, ensure_ascii=False) + "\n"); n += 1
    print("yazılan:", n)
