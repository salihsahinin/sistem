# Denetim: depo taraması 2026-11-10 (bozuk · tutarsız · verimsiz · gereksiz)

**Ne bu:** Salih'in 2026-11-10 emri: "sistem klasörünün tamamını oku; bozuk, tutarsız, verimsiz ya da artık gereksiz her şeyi bul; emin olduğunu düzelt, kalanını incelemem için listele." Bu dosya sonucu taşır: önce düzeltilenler, sonra Salih hükmü bekleyenler.

**Nasıl yapıldı:** mekanik kontroller (Jarvis) + 6 salt-okur denetim işçisi (oda `202611101157`, 2 Opus 5.5 + 4 Sonnet 5.5) + 4 düzeltme işçisi (2 Opus 5.5 + 2 Sonnet 5.5). Ham raporlar: `cc/rapor/2026-11/rapor-2026-11-10-depo-denetimi-ham.md` (≈190 bulgu, kanıtlarıyla). `ogrenme/` içeriği kök md.1 gereği taranmadı.

**AS-OF:** 2026-11-10, HEAD `d3a7008e` üzerine. Tüm sayılar bu oturumun komut çıktılarından.

## 1. Mekanik kontroller

| Kontrol | Sonuç |
|---|---|
| `cargo check --workspace --all-targets` | temiz |
| `lake build` (Lean) | 82 iş başarılı; `sorry`/`axiom` yok; 34 modülün 34'ü import ediliyor |
| Python `py_compile`, `bash -n`, JSON ayrıştırma, kırık symlink | hata yok |
| `cargo test --workspace` (düzeltmelerden önce) | 2 test kırık (`skill-kapi` fark testi; aşağıda D2) |
| `cargo test --workspace` (düzeltmelerden sonra) | hepsi geçti |

## 2. Düzeltilenler (commit'li, push bekliyor)

**D1. Kilit atlatma (Rust hook).** Git Bash yolu `/c/sistem/...` Windows yoluna çevrilmediği için iki kilit atlatılıyordu: alt-ajan okuma kilidi (`cat /c/sistem/sistem/jarvis/core/durum-kapsulu.md` exit 0) ve core yazma teli (`echo x > /c/.../jarvis/core/x.md` exit 0). İkisi de artık exit 2. Uçtan uca doğrulama: gerçek hook betikleri üzerinden 8 senaryo, jarvis tarafındaki 6'sı beklenen kodu veriyor. Dosyalar: `kod/hook/src/altajan_okuma.rs`, `core_tel.rs`.

**D2. Skill kapısı her skill'i düşürüyordu.** `skill-kapi` tüzük maddelerini yalnız `core/tuzuk-v0.md`'den okuyordu; tüzük Karar 117 ile parçalara bölündüğü için m.17 ve sonrası "tüzükte madde yok" sayılıyor, `R-referans-varligi` sert kapısı düşüyordu. Artık `tuzuk-v0-m*.md` parçaları da okunuyor (Rust + Python referansı). `atlas-kosum` ve `seans-acilis` üzerinde: "eksik: yok".

**D3. Diğer Rust düzeltmeleri.** Hook matcher `"*"` sessizce atlanıyordu, artık "hepsi" · SessionStart brifi bayt sınırında kesiliyordu, artık karakter sınırında · `katman-hatti` arşive inmiş 5 Python betiğine düşmeye çalışıyordu, artık net hata veriyor · `alan-ajani-dogur` Windows'ta `.sh` hook'ları CRLF yazıyordu, artık LF · bayat mesajlar (`python3 tools/katman-hatti.py`, `tools/ad-esitligi-denetim.py`) Rust ikililerine çevrildi · kullanılmayan `unicode-normalization` bağımlılığı çıktı.

**D4. Belgeler (canlı talimat satırları).** Karar 122 sonrası hâlâ "kapsülü oku/yaz" diyen ve Mac yolu (`~/sistem`, Finder, `/Users/...`) taşıyan satırlar: kök `README.md`, `KURULUM.md`, `jarvis/README.md`, `jarvis/KILAVUZ.md`, `jarvis/kaynak-kodu/README.md`, `jarvis/cc/README.md`, `jarvis/cc/workflow/README.md`, `jarvis/tools/SCRIPTLER.md`, `jarvis/mods/README.md`. Kırık atıflar: `tools/skill-esik.py`, `tools/ad-esitligi-denetim.py`, `alan-ajani-dogur.py`, gece-senkron (3 skill dosyası). `seans-kapanis` açıklamasından "kapsül" çıktı.

**D5. Kayıt hijyeni.** İki pipeline durum tablosu `DONE` yapıldı (olay günlüğü zaten "Tüm görevler DONE" diyordu) · 4 wiki yer tutucusu (`[[link]]`) backtick'e alındı · `jarvis-oda` başlıkları v0.6 · `friday/.DS_Store` izlemeden çıktı (dosya diskte duruyor) · kök `.gitignore`'a taşınmış ürün artıkları eklendi (`projects/*/.godot|test_cikti|referans`).

**D6. Arşive inen 5 emekli script** (silme yok, `git mv`): `gece-senkron.ps1` → `jarvis/arsiv/zamanlanmis-gorev/`; `gnhf-izle.py` (bozuk yol, çağıran yok), `pano-akis.py` (pano dondu), `masa-html.py` (Rust `masa-uret` var), `olcum-dortlu.py` (çağıran yok) → kök `arsiv/kod/python/tools/`.

## 3. Salih hükmü bekleyenler (önem sırasıyla)

Her kalem: ne · önerim. Ayrıntı ve kanıt ham raporda (rapor no · bulgu no).

### A. Güvenlik frenleri (en önemli)

1. **Alan ajanı kilitleri hâlâ atlatılıyor.** 8 ajandaki `okuma-izin.sh` (Python) aynı `/c/` açığını taşıyor: tart'tan `cat /c/sistem/sistem/jarvis/CLAUDE.md` exit 0. Ayrıca fail-open (Python yoksa ya da JSON bozuksa exit 0) ve izinli geçici dizin listesi Mac'e özgü. Öneri: hook'u `jarvis-hook okuma-izin` alt komutuna taşı (çağrı başına ≈0,6 sn → ≈0,05 sn ölçümü de bunu destekler), 8 ajana üreticiyle yeniden dağıt. Ajan dizini olduğu için imza gerekir. (R1 · 2, 8, 9, 20)
2. **Ajan `settings.json` deny kuralları etkisiz.** `Read(~/sistem/jarvis/**)` gibi Mac yolları; `~/sistem` bu makinede yok. Şablon (`sablonlar/ajan-iskelet/claude-ayar/settings.json`) her doğumda bunu çoğaltıyor. Öneri: şablon + 8 kopyada yolları depo köküne göre yeniden yaz. (R1 · 7, R4 · 1)
3. **Kökten açılan oturumda ajan deny kuralları hiç uygulanmıyor.** Dispatcher ajan ayarından yalnız `hooks` okuyor; `permissions.deny`/`ask` (push freni, `git add -A` yasağı) atlanıyor. Öneri: kök ayara birleşik deny ya da dispatcher'da eşleme. (R1 · 6)
4. **Git hook'ları sessizce kapalı.** `core.hooksPath=tools/git-hooks` var olmayan dizine bakıyor (betikler `jarvis/tools/git-hooks`); betiklerin kendi desenleri de monorepo öncesinden. Düzeltince commit-msg ve büyük harf telleri devreye girer; betik başlığı "bilinçli ertelendi" dediği için yönü sen seçmelisin: (a) yolu ve desenleri düzelt, telleri aç (önerim) ya da (b) `hooksPath` ayarını kaldır, betikleri arşivle. (R1 · 4, 5)
5. **İkili yoksa tüm kilitler exit 0** (Karar 118 M2 bilinçli seçim). Yeni klonda ya da worktree'de kilitler kapalı kalıyor. Öneri: kilit hook'larında ikili yoksa exit 2. (R1 · 36)
6. `core_tel.rs` `mv|cp|rm|touch|tee … core/` deseni salt-okur komutu da kesiyor (ör. `grep -n tee core/x.md`). Öneri: komut adını satır başında ya da ayraç sonrasında ara. (R1 · 17)

### B. Kanon metni (Katman-1, yalnız senin imzanla)

7. **`jarvis/AGENTS.md` kendi içinde çelişiyor:** satır 3 "Durum → `core/durum-kapsulu.md`", satır 9 "kapsülden devralır", satır 37 ve 40 kapsül/pano; §3 ise "dondu" diyor. Ayrıca Mac yolları (satır 9, 12, 23). Dosya tavana 4 bayt uzakta (7164/7168), düzeltme satır dengesi ister. (R3 · 1-3, 32)
8. **`core/` içinde bayat ya da kırık atıflar:** `ajan-metodolojisi.md` (kapsül/pano eager listesi, kayıp `core/desenler.md`, kayıp `.claude/agents/orkestrator.md`, `tools/skill-esik.py`, "Opus 5" ↔ "Opus 5.5", `~/jarvis`), `ingest-semasi.md` (`borç` hedefi kapsül/pano), `baglam-anahtar-kaydi.md` (`ad-esitligi-denetim.py`), `halusinasyon-paketi.md` (birincil komut Python), `varlik-felsefesi.md` (3 kırık göreli bağlantı), tüzük m.42/m.44 başlığı "Opus 5". (R3 · 8, 9, 13, 15-19, 34, 44)
9. **7 alan ajanı `AGENTS.md` satır 1** var olmayan `jarvis/tools/alan-ajani-dogur.py`'yi üretici sayıyor; §3 hafıza hâlâ kapsülü birincil yazıyor; `deci` ve `vega` var olmayan `urun/` dizinini anıyor. (R4 · 6, 8, 9)
10. **Kök `AGENTS.md` md.1** hakem için `<alan>-hakem/` ya da ortak `hakem/` dizini diyor; ikisi de yok, hakem `.claude/agents/hakem.md` olarak yaşıyor. (R3 · 45)
11. **`ogrenme/` çelişkisi:** kök kanon "ajanlara kapalı" diyor; jarvis'teki `ogren` skill'i `ogrenme/<şerit>/` okuyup yazıyor ve şeritler alan ajanlarına verilmiş durumda. İstisna kanona yazılmalı ya da yönlendirme alan ajanlarına bağlanmalı. (R3 · 25)
12. **`core/sokrates-ajani.md` §7** "≤900 kelime" diyor, ölçüm 1592; ajan ve skill kopyaları elle türetiliyor, türetici yok; `sokrates` skill'i katalogda ve eval'i yok. (R3 · 26-28)
13. **Friday şablondan ayrışmış:** hakem ajanı, `okuma-izin-ek`, `ogren` skill'i yok; hook v0.5; deny'de var olmayan `kanon/**`; `README` "Opus 5 medium" ve Mac yolları. Öneri: şablondan yeniden doğur. (R4 · 2, 18, 19)

### C. Gereksiz ya da ölü olanlar (arşiv kararı)

14. **16 ölü aday Python script** (canlı çağıranı yok): `asof-eval`, `atlas-derle`, `denetci-kalibrasyon`, `d2-eval`, `headless-esleme`, `pointer-kayma`, `silver-saglik-kalibrasyon`, `tuzuk-iz-tarama`, `verify-push`, `erisim-kalibrasyon`, `erisim-vektor`, `kural-envanter`, `baglam-skill-aday`, `karantina`, `kod-envanter`, `skill-butce`. Öneri: toplu arşiv (#20 Rust taşıma işinin kapsamını da 59'dan düşürür). (R2 · 15-18)
15. **Rust karşılığı olan 8 Python kopyası** hâlâ canlı dizinde ve skill'lerde "yedek": `katman-hatti`, `kural-sayaci`, `buyuk-harf-temizle`, `kod-orani-olcum`, `baglam-tablo`, `prompt-dosya`, `paket-yonlendir`, `harness_anahtar` (bu sonuncusu arşiv kopyasıyla bayt-eşit). Fark testleri ikisine referans veriyor. Öneri: Karar 118 M2 usulüyle arşive indir, skill'lerden yedek satırını çıkar. (R2 · 4-6, R1 · 15)
16. **claude.ai'daki emekli global skill'ler** hâlâ etkin: `gunaydin-vardiya`, `vardiya-kapanis` (Carvis, `C:\JARVIS`, "günaydın" tetiği) ve `dev-run-planner`; "oturuma başlayalım" tetiği `seans-acilis` ile çakışıyor. `kaynak-kodu/README.md` 08-17'den beri "kaldırılacak" diyor. Yalnız senin elinle kaldırılır. (R3 · 23, 24)
17. **`~/.claude/dev-mods/`:** 4 boş uuid dizini + eski mod kopyası (oda 0.4.1, graf 0.1.0); modlar artık doğrudan repodan yükleniyor. Depo dışı; arşivle ya da sil. (R5 · 1, 2)
18. **`projects/portal-parkur/`** altında 165 MB izlenmeyen artık (`referans/` 154 MB, `test_cikti/` 11 MB); proje ayrı repoda. Artık `.gitignore`'da; yeni repoya taşımak ya da silmek senin kararın. (R4 · 14)
19. Kök `veri/hafiza-ayna/-Users-HasanSalihSahin-sistem/` yanlış cwd ile koşmuş boş çıktı; `ortak/oda/` oda modunun çalışma durumu. İkisi de izlenmiyor. Öneri: ilki arşiv, ikincisi için karar: `.gitignore` mı, kayıt olarak commit mi. (R4 · 12, 13, 24)
20. `kod/kural/src/{argparse,py,harness_anahtar}.rs` ile `kod/rituel/src/` aynı adlı dosyalar ayrışmış kopya (489/632, 416/572, 55/71 satır). Öneri: ortak crate. (R1 · 14)
21. `kod/arac/src/yol_tasi.rs` tek seferlik Mac göçü aracı; `altajan_okuma.rs` yasak listesinde `~/Desktop/repo`. (R1 · 31, 32)

### D. Verimsizlik

22. **Hook zinciri maliyeti:** jarvis'te her Bash çağrısı 2 sarmalı hook koşturuyor (0,146 sn; doğrudan exe 0,050 sn); kök `PostToolUse .*` ajan yokken de dispatcher başlatıyor (≈0,11 sn/çağrı); çocuk sürece zaman aşımı yok. (R1 · 18, 19, 27)
23. **Her oturumda değişen izlenen türev dosyalar:** `veri/erisim-eval.jsonl` (19,5 MB), `bronz/baglam-olay.jsonl` (10,6 MB), `anakronizm-denetim.jsonl` (10 MB), `katman-olcum.jsonl` (9,5 MB), `bronz/hareket-olay.jsonl` (6,5 MB) ve `graf/pointer-sistemi-v0-*` (23 dosya). Öneri: türevleri `.gitignore`'a al, eklemeli olanları aylık parçala. (R5 · 3, 4)
24. **`katman-hatti` süresi:** bu oturumda 120 sn zaman aşımını geçti; brif ve skill "~12 sn" diyor (KURULUM Windows için ≈56 sn yazıyor). Metin ya da hat güncellenmeli.
25. **Hareket kütüğü ajanlar arası tutarsız:** `hareket-olay.jsonl` friday, tart, gard'da izleniyor; sage, vega, deci'de izlenmiyor; calc, span'da `veri/` hiç izlenmiyor. Tek karar gerek. (R4 · 15)
26. `kuyruk/senaryo-defteri.md` 118 KB tek dosya; kuyruk kökünde eski büyük dosyalar, 9 `gelen-*`, 6 `masa-spec-*.json`; `kuyruk/arsiv/` boş. (R5 · 14-18)
27. `raporlar/` kökünde 38 dosya ay klasörü düzeninin dışında (22 `son-50-prompt`, 12 konu raporu); aynı güne iki farklı hareket günlüğü (`raporlar/` ve `raporlar/hareket/`). (R6 · 7-9, 29)
28. `MEMORY.md` hafıza indeksi 6303 bayt; `Butce.lean` tavanı 4 KB. (R3 · 30)

### E. Küçük tutarsızlıklar

29. **Açılış kapısı K2 yanlış alarm veriyor:** ilk 1500 karakterde `SAHADA/AÇIK/KOŞUYOR/YARIM` kelimesi arıyor; "açık borçlar" ya da olay günlüğündeki "S-1 SAHADA" bitmiş pipeline'ı açık gösteriyor. 5 uyarının 2'si bitmiş, 1'i yanlış alarm, 2'si gerçekten kısmen açık (`erisim-fts`, `silver-saglik`). Öneri: eşleşmeyi tablo durum sütununa daralt. (R6 · 1-5)
30. `.gitattributes` yok; sage, vega, deci hook'ları indekste CRLF (üretici düzeltildi, mevcut dosyalar duruyor). Öneri: `*.sh text eol=lf` + yeniden normalleştir. (R4 · 4)
31. `git remote no-mistakes` Mac yoluna bakıyor (`/Users/HasanSalihSahin/.no-mistakes/...`). (R4 · 22)
32. `.claude/agents/research-agent.md`: dosya adı ↔ `name: atlas`; araç listesinde `get-library-docs` (oturumdaki ad `query-docs`); "Opus 5". `hakem.md` "yazmaz" diyor ama `memory: project` Write/Edit veriyor. (R3 · 20-22)
33. 3 kırık wiki bağlantısı: `[[rol-katmanlari]]`, `[[treehouse]]`, `[[skill-hazinesi-secim-isabeti]]`. (R5 · 5-7)
34. 9 Lean modülünün `.lean.md` eşi yok; `Zorlanabilirlik.lean` "uygulayan kod: yok". (R5 · 19, 20)
35. `raporlar/seans/`: 21 JSON'dan 3'ü baskın şemadan sapıyor, girdi ve çıktı dosyaları aynı dizinde, md ve json karışık. (R6 · 16-20)
36. `arsiv/README.md` 7 girdiyi listelemiyor; `worktree-kalinti-2026-11-10` altında 2 boş yama; `raporlar/2026-09/yol-tasi-kuru|uygula` diff'leri bayt-eşit. (R6 · 10, 11, 13)
37. Span'ın 2026-10-19 tarihli devri (`span/cc/giden/…claude-mods-M1.md`) 22 gündür yanıtsız; vega Q1 ve deci J1 ders iskeletleri 09-22'den beri işlenmemiş. (R4 · 10, 11)
38. `jarvis/README.md` içinde iki "Klasör haritası"; `sablonlar/harness/claude-global-CLAUDE.md` canlı dosyadan ayrışmış (hâlâ Mac). (R3 · 43, 36)
39. **Oda modu gözlemi (bu koşumdan):** biten görev raporu Jarvis'e kesilmiş geliyor ve `oda_oku` da kesik gösteriyor; tam metin yalnız `ortak/oda/<id>.json` içinde. Denetim işçisi 1 süre ölçerken `tart` hareket kütüğüne 5 satır yazdı ve geri aldı (salt-okur emrine rağmen hook betiği yan etkili). Öneri: `oda_oku` için tam rapor seçeneği.

## 4. Kapsam dışı kalan

`ogrenme/` içeriği · `cc/gelen`, `cc/giden`, `cc/devir/**` ve `kuyruk/senaryo-defteri.md` içeriği (alt-ajan okuma kilidi işçileri engelledi; karar numaralarının defterle eşleşmesi denetlenmedi) · rituel, kural, arac, durum, baglam crate'lerinin iş mantığı satır satır okunmadı (desen taraması yapıldı) · `katman-hatti`'nin çağırdığı 15 Python adımının içi · jsonl veri içerikleri.

## 5. İkinci tur (2026-11-10 akşam ve 2026-11-11): Karar 128 icrası ve kapsam dışı okuma

**AS-OF:** 2026-11-11, HEAD `4ca74fcf` üzerine. Ham raporlar (12-14, 84 bulgu): `cc/rapor/2026-11/rapor-2026-11-10-depo-denetimi-ham-2.md`.

### 5.1 §3'ten kapananlar (Salih: "1-5 kalemlerini önerdiğin şekillerde uygula")

| §3 kalemi | Sonuç |
|---|---|
| A1 alan ajanı kilitleri | Kapandı: gövde Rust `jarvis-hook okuma-izin`, 8 ajanda aynı sarmal; friday 35/35, diğer yedi ajan 40/40 test; `/c/` atlatması, bozuk JSON ve eksik ikili artık kesiyor |
| A2 deny yolları | Kapandı: şablon + 8 ayar dosyasında `//c/sistem/sistem/...` |
| A4 git telleri | Kapandı: teller açık; ilk commit'lerde 4 dosyada çıplak büyük harf yakaladı |
| B7, B8 kanon metni | Kapandı (jarvis `AGENTS.md` 7157/7168 bayt; `core/` 7 dosya; tüzük m.42, m.44) |
| B9 alan ajanı başlığı | Yalnız üretici adı düzeldi. Ajanların kendi kapsül düzeni ve `urun/` atfı değişmedi (iş #33 ve Salih kararı) |
| C14 ölü betikler | 14'ü arşive indi; `baglam-skill-aday.py` ve `pointer-kayma.py` canlı çıktı (kanon ve damıtma skill'i kullanıyor), kaldı |
| C15 Python kopyaları | 8'den 2'si indi (`kural-sayaci`, `kod-orani-olcum`). Kalan 6'sının canlı bağımlısı var: `katman-hatti.py` (iki Python testi koşturuyor), `baglam-tablo.py` (`anahtar-denetim.py` import ediyor), `prompt-dosya.py` ve `paket-yonlendir.py` (hook fark testlerinin referansı), `buyuk-harf-temizle.py` ve `harness_anahtar.py` (pre-commit teli, canlı import) |
| D24 hat süresi | 97 sn → 58 sn (ölçüm 2026-11-11; `baglam` 27 → 20, `erisim` 21 → 10, `graf` 15 → 1,6, `ambar` 7 → 4). Belgelerdeki "~12 sn" ifadeleri "1-2 dk" oldu |
| E37 Span devri | Okuma kilidi şikâyeti kapandı (Windows geçici dizini artık izinli); M1-M5 ders iskeleti isteği açık |

### 5.2 Kapsam dışı okumada bulunup düzeltilenler

- **Hook kütükleri iç içe yazıyordu:** satır ve satır sonu iki ayrı yazımdı; `talimat-yukleme-olay.jsonl` içinde 35 birleşik + 3 yırtık kayıt. Tek yazıma indi. Eski bozuk satırlar yerinde duruyor.
- **`baglam-tablo` commit tarihleri yanlıştı:** `git log` yolları depo kökünden, dosya listesi `jarvis/` altından geliyordu; monorepo sonrası hiçbir commit sayılmıyordu (1368 dosyanın 313'ünde ilk commit boş). Artık tüm depo log'u `jarvis/` önekiyle eşleniyor: boş 0, Rust ve Python 1369 dosyada aynı.
- **`durum` kütüğü:** `seans-kapat` teslim dosyasını doğrulamadan önce eziyordu; aynı gün ikinci kapanış birincinin üstüne yazıyordu; alan uyuşmazlığı denetlenmiyordu; çıktı dosyaları yerinde yazılıyordu; eşzamanlı `ac` aynı numarayı üretebiliyordu; `--help` hata veriyordu. Yedisi düzeldi, 18 CLI testi geçti; gerçek kullanımda 38 ardışık yazım sorunsuz.
- **Açılış kapısı K1 ve FIFO** donmuş kapsül ve pano dosyalarına bağlıydı; artık `ortak/durum-olay.jsonl` kütüğüne bakıyor.
- **Bayat varsayılan depo yolu:** `masa-uret` ve `buyuk-harf-temizle` `--repo` verilmezse var olmayan `~/sistem/jarvis` yoluna yazıyor ya da repo dosyalarını atlıyordu.
- **`baglam denetle ../AGENTS.md`** yanlış dosyayı (`jarvis/AGENTS.md`) gösteriyordu.
- **`kod-orani-olcum`** `.rs` ve `.lean` dosyalarını kod saymıyordu.
- **`katman-hatti` adım hataları:** üreticisi arşivde olan 13 bayat gold görünüm arşive indi (`arsiv/gorunum-2026-11-10/`); 11 kırık karar-borcu pointer'ı düzeldi (`karar` adımı artık çıkış 0). Hat yalnız kalem 40 yüzünden hâlâ hata koduyla bitiyor.
- **Durum kütüğü:** odanın açtığı 19 iş (#89-#107) kapanmıyordu; elle kapatıldı.

### 5.3 Salih hükmü bekleyen yeni kalemler (önem sırasıyla)

40. **[kapandı 2026-11-11, Karar 129: seçenek (a) uygulandı; hat 17 adım, 46,8 sn]** **`duckdb` kurulu değil.** `parquet` ve `tarama-duckdb` adımları kalıcı atlanıyor, `v_tarama_plan_duckdb.csv` 49,7 gün bayat ve `katman-hatti` yalnız bu yüzden hâlâ hata koduyla (3) bitiyor; `kolon-olcum` duckdb yokken de 354 MB tabloyu tarıyor. Seçenek: (a) kolon kolunu emekli et: üç adımı hattan çıkar, görünümü arşivle (önerim; kol 2026-09-22'den beri çalışmıyor ve tüketicisi yok) ya da (b) `pip install duckdb` ile geri getir. (R14 · 3, 9)
41. **`durum` kütüğünde tek bozuk satır bütün komutları kilitliyor** (`lib.rs` ≈268, 363); worktree birleşmesinde sıra dışı numara bunu tetikler. Öneri: katlarken numaraya göre sırala, bozuk satırı uyarıyla atla. (R13 · 2)
42. **Transkriptler her koşumda üç adımda baştan okunuyor** (`hareket`, `seyir`, `ambar`) ve `anakronizm-denetim.jsonl` her koşumda tüm bulguları yeniden ekliyor (10 MB, sınırsız büyüme). Öneri: artımlı okuma + kütüğe yalnız fark. (R12 · 4, 11)
43. **Windows yol biçimi kaçakları:** `bayat_cekim` ve `anakronizm` ters bölülü yol üretip silver anahtarıyla eşleşmiyor; `hareket.rs` `/c/` ve küçük harf sürücüyü repo dışı sayıyor; kütüklerde CRLF ve LF karışık. (R12 · 15, 18, 19)
44. `ambar_tablo.rs:631` metin gelen `prompt_id` değerini harf harf ayrı kimliklere bölüyor (Python hatası olduğu gibi taşınmış). (R12 · 20)
45. `devir_md2json` md'den gelen devir kimliğini süzmeden dosya adına koyuyor (`../x` emir dizini dışına yazar) ve izin öneki ayraçsız (`cc/gelen` izni `cc/gelen-baska/` yolunu da geçiriyor). (R13 · 18, 19)
46. `kural` crate'indeki `argparse`, `py`, `harness_anahtar` kopyaları `rituel` ile ayrışmış; `float_repr` iki kopyada farklı yuvarlıyor. Engel yalnız API birleştirme. (R13 · 24-26)
47. `silver_saglik` ve `baglam_tablo` `kod_sha` için arşive inmiş Python dosyasını okuyor; koşum kimliği kod değişikliğini yansıtmıyor. (R12 · 13)
48. Python hattı: `tarama-plan` her koşumda veritabanını kopyalayıp ANALYZE ediyor; `erisim-fts` FTS dizinini baştan kuruyor; `prompt-tablo` O(n²) tarıyor. Hattın kalan 58 saniyesinin önemli kısmı burada. (R14 · 2, 5, 6)
49. `sunum-proof-of-work.py` Mac yolu ve `head` komutuna bağlı; `wiki-baglanti.py` Windows yolunu URI'ye düz basıp hatayı yutuyor; `baglam-skill-aday.py` "sıcak" kümesi hâlâ kapsül ve pano. (R14 · 10, 11, 13)
50. `tools/testler/test_fren_hook.py`: 2 test gerçek oturumun fren sayacını okuduğu için kırık (test yalıtımı yok).
51. **Commit'siz ders kayıtları:** `ogrenme/dosya-mimarisi/` ve `ogrenme/ontolojik-encode/` 2026-11-01'den beri izlenmiyor; `ogrenme/README.md` ve `mufredat.md` taşınmış derslere eski yollarla işaret ediyor. `ogrenme/` Salih'in alanı, dokunulmadı.
52. **Oda modu:** biten görev durum kütüğünde açık kalıyor (köprü işi açıyor, kapatmıyor); `oda_oku` raporu kesik gösteriyor; işçilerin önerisi Jarvis uyandıktan sonra görünüyor.
53. `kod/arac/src/yol_tasi.rs` tek seferlik Mac göç aracı; Windows'ta hiç eşleşmiyor. Arşiv kararı. (R13 · 22)
54. `cc/devir/` altındaki tarihli devir kayıtları klasörleme öncesi düz yolları gösteriyor (`cc/rapor-…`, `raporlar/…`); tarihli kayıt olduğu için dokunulmadı.

### 5.4 Jarvis'in Salih adına verdiği iki teknik alt-karar

Ö1: `baglam-tablo` `git log` tam depo + önek eşleme (ilk deneme `--relative` monorepo öncesi geçmişi kesmişti). Ö2: `rituel_fark.rs` fark testindeki dakika sınırı yarışı (commit zamanları 60'ın katına çekildi). İkisi de geri alınabilir.

### 5.5 Hâlâ okunmayan

`argparse.rs` gövdesinin kalanı · `kural/src/{tetik,derece}.rs` · `baglam-tablo.py` gövdesi (1019 satır; yalnız git ve ana akış kesitleri) · crate `tests/` dizinleri · jsonl veri içeriklerinin anlamı (yalnız biçim tarandı) · `ogrenme/kaynaklar/` içeriği.
