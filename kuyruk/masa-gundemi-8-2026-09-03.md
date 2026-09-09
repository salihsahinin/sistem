# Masa Gündemi — 8. Lavish Masası (2026-09-03 akşam)

*Tetik: Salih 09-03 akşam ("bu oturumda açılması gereken karar masasını hazırla, lavish ile açacağız"). Yüzey `.lavish/masa-8-2026-09-03.html` → teslim kopyası `raporlar/masa/masa-8-karar-yuzeyi-2026-09-03.html`. Hazırlayan Carvis/Fable, HEAD 7339271. Hüküm Salih'te; her kalemde ÖNERİLEN ilk sırada (m.40 eki: ne demek · ne yaparım · artı · eksi). Deneysel m.29; rakamlar kaynaklı m.39.*

**Masa öncesi FİİLEN yapılan (Katman-2, veto = revert):** görselleştir skill'i arşive indi (7339271) · Cowork icra promptu derlendi `cc/prompt/prompt-2026-09-03-sonnet-icra-cowork.md` (M1 hükmüne kadar VARSAYIM: Sonnet 5 / medium / pipeline / `~/jarvis`).

**Bayat satır düzeltmesi:** kapsül "erisim-fts AXI kapı SERBEST" diyordu; manifest `ib-58-erisim-fts-axi` = `tamam` (commit f3240ad). Kapsülden düşer.

## Kalemler

### M1 · İcra yan-oturumu: nerede · model · effort · biçim (Karar 86 D2 ile çelişki, m.16)
Karar 86 D2(a): icra = TEK Fable ana oturumu + Sonnet işçi pipeline'ı; D2(b) ikinci Fable oturumu 2× token gerekçesiyle RET. Salih 09-03: paralel Cowork icra oturumu. Uzlaştıran kaynak: Karar 84 EK(2) izlenen nöbet = ayrı oturum, prompt Carvis'ten.
- **(a) ÖNERİLEN — Cowork · `~/jarvis` · Sonnet 5 · medium · pipeline (worktree yok):** D2(a)'nın ruhu korunur (tek planlayıcı Fable, işçi Sonnet). Yaparım: prompt hazır, Salih yapıştırır; ben masa + damıtmaya dönerim. Artı: Fable tokeni 1×, Fable bağlamı temiz kalır (D2 Salih notu). Eksi: Sonnet kararsız kaldığında birim durur, devir notuyla bana döner (prompt bunu emrediyor).
- **(b) Cowork · Fable · medium:** D2(b) canlanır. Artı: tanımsız seçimlerde durmaz. Eksi: 2× Fable tokeni; iki Fable oturumu = iki karar merci riski (yan-oturum karar alamaz kuralı zorlanır).
- **(c) gnhf worktree · Sonnet · sensiz:** Karar 84 şerit-1. Artı: en ucuz, izole. Eksi: Salih izlemek istiyor; U1 galeri birimi `.venv` + jarvis-dışı klasöre bağlı, worktree'de kırılır.

### M2 · Damıtma imzası (Katman-1; 08-30'dan beri açık)
Aşım: defter 68,7/48 KB · kutu 22,3/20 · KILAVUZ 16,8/16 · pano 12,3/12 · kapsül sınırda.
- **(a) ÖNERİLEN — Bu seansta, Cowork icra koşarken Fable damıtma turu (`damitma` skill'i; defter + pano önce):** Artı: paralel; defter en büyük aşım. Eksi: Cowork ile ayak-izi çakışması → damıtma yalnız `kuyruk/`+`core/pano.md`, Cowork `tools/`+`raporlar/` (paralel-kapi bunu doğrular).
- **(b) Cowork devri bittikten sonra ayrı seans:** Artı: tek yazan. Eksi: bir seans daha aşımda çalışılır.
- **(c) Beklet:** Eksi: tetik 4 gündür açık; kapsül 8 KB'a dayandı.

### M3 · Karar 86 D5 açık sorusu — manifest `tur` proxy mü, şema alanı mı
17 manifestin tümü `pipeline` çıkıyor; `hibrit` ayrımı mevcut alanlardan çıkmıyor.
- **(a) ÖNERİLEN — Proxy kalır + isteğe bağlı `tur_ustyazim` alanı** (yalnız Fable yazar, gerekçe zorunlu): Artı: şema büyümez, hibrit istisna olarak işaretlenir. Eksi: hibrit sayımı elle.
- **(b) Y1/Y2/Y3 yüklem alanları şemaya:** Artı: İB-65'in beklediği ayrım deterministik. Eksi: 17 manifest + kapı v0.2 + 8 test yeniden.
- **(c) Beklet (3 hibrit vaka görülene dek):** Eksi: bugün hibrit vaka yok, ölçüm gelmez.

### M4 · Karar 86 D6-3 — anakronizm tarihli-dosya muafiyeti (KURAL)
Denetim 196 bulgu / 116 ihlal; büyük kısmı tarihli rapor dosyalarındaki damgasız iddialar.
- **(a) ÖNERİLEN — Dosya adındaki `YYYY-MM-DD` = AS-OF damgası sayılır; `raporlar/`+`cc/` tarihli dosyalar muaf, `core/`+`wiki/` muaf DEĞİL:** Artı: gürültü düşer, kanon yüzeyi korunur. Eksi: tarihli dosya içindeki "bugün" iddiaları da muaf sayılır.
- **(b) Muafiyet yok, her satır damgalı:** Artı: tek kural. Eksi: 116 ihlal el işi.
- **(c) Yalnız `raporlar/` muaf:** ara yol.

### M5 · Skill kabul kuralı (görselleştir dersi, Katman-1 aday)
İB-77: 8 işçi atlas + v0.1→v0.3 üç düzeltme → ret (09-03 22:10). Kabul kapısı skill-kapisi (K0-K3) yapıyı ölçtü, Salih beğenisini ölçmedi.
- **(a) ÖNERİLEN — Deneme sürümü kuralı:** yeni skill önce `kuyruk/skill-deneme/<ad>/` (hazineye ve `~/.claude/skills`'e girmez), Salih ≥1 canlı koşum + "kabul" sözü → hazine; tüzük ek fıkra + skill-kapisi K4 "kullanıcı-kabulü". Artı: ret ucuzlar (atlas ve 3 sürüm bedeli ödenmez). Eksi: deneme sürümü tetiklenemez → Salih elle çağırır.
- **(b) Mevcut kapı yeter, vaka tekil:** Eksi: aynı bedel yeniden ödenebilir.
- **(c) 3-koşum kuralı (mevcut kalibrasyon satırı):** Artı: veri toplar. Eksi: ret 3 koşum sonra gelir, daha pahalı.

### M6 · Galeri devri 5 soru (`cc/devir/devir-2026-09-02-opus-galeri-yaprak-doluluk.md` §6; jarvis-dışı)
1. Derinlik 3 kalıcı mı? **(a) ÖNERİLEN** kalıcı (8 yaprak okunur; d4 %91,74 yedek) · (b) d4'e dön.
2. Derinlik 2 denensin mi? **(a) ÖNERİLEN** hayır (etkileşim öğrenemez) · (b) tek koşum dene.
3. `zaman-testi-model_v2u.json` silinsin mi? **(a) ÖNERİLEN** arşiv klasörüne taşı (m.8) · (b) sil.
4. 2,5 GB türev temizlensin mi? **(a) ÖNERİLEN** evet, yeniden üretim ~10 dk · (b) kalsın.
5. Odak eşiği %60 / ≥3 araç? **(a) ÖNERİLEN** U1 çıktısı görülene dek sabit · (b) %50 / ≥2'ye gevşet.

### M7 · 08-31 devir soruları kalanlar (①③④ Karar 86'da kapandı)
- **② İB-07 kalanı (15 çağrı):** (a) ÖNERİLEN Cowork kademe 3'e ek birim (sorgu seti dış-kaynaklı yeniden türetilir) · (b) KB-20'yi mevcut 45/60 ile kapat · (c) beklet.
- **⑤ Rapor yolu usulü:** (a) ÖNERİLEN emir dosyası kazanır, prompt yalnız varsayılan verir (bu promptta böyle) · (b) hep `raporlar/`.
- **⑥ İB-66 hakem sapması:** (a) ÖNERİLEN maskeli hakem yeniden koşulur (Sonnet, ~15 çağrı) sonra masaya · (b) mevcut sentez şerhle masaya.

### M8 · İB-75 bağlam-devri ekip-lideri v0 — tetik zamanı
Salih notu 09-02: "yakın tarih". Fable bağlamı bu seansta yine büyük.
- **(a) ÖNERİLEN — M2 damıtma + U2 İB-71 baseline sonrası ilk seans:** Artı: bağlam ölçüsü (kod/md oranı) elde olur, tasarım ölçüme oturur. Eksi: 1-2 seans gecikme.
- **(b) Hemen (bu seansta tasarım emri):** Eksi: damıtma ve icra ile üçüncü paralel iş.
- **(c) İB-71 + İB-70 iki tur sonra:** Eksi: "yakın tarih" notuna uzak.

### M9 · Senkron kütüğü 08-04'ten beri FAIL-ff (`gece-senkron.ps1` Windows)
Mac'te gece senkron eşleniği yok; açılış ritüeli adım 2.4 bayat satırı her seans okuyor.
- **(a) ÖNERİLEN — Kütüğü emekli et, ritüel adımını kaldır; gece işi gnhf'ye bağlı (Karar 84):** Artı: bayat okuma biter. Eksi: sayaç tarihçesi donar (arşivde kalır).
- **(b) Mac launchd eşleniği (İB aç):** Artı: sayaç sürer. Eksi: yeni otomat + push freni m.9 ile çelişir (push Salih beyanıyla).
- **(c) Beklet.**

### M10 · Karantina ilk tescil (İB-72 mekanizması Cowork U3'te kurulur; tescil yetkisi Salih)
- **(a) ÖNERİLEN — `arsiv/kuyruk-arsiv/gorsellestir-skill-2026-09-03/` ilk tescil (BAKMA-GEREK-YOK bayrağı):** Artı: mekanizmanın ilk gerçek girdisi; tarama araçları arşivi okumaz. Eksi: yok (git tarihçesi durur).
- **(b) Arşivde kalsın, karantinaya girmesin:** Eksi: 8 KB SKILL.md + spec'ler ingest/erişim taramalarına düşmeye devam eder.

### M11 · İB-73 Jarvis eğitim serisi — format hükmü
- **(a) ÖNERİLEN — md bölüm serisi `ogrenme/jarvis-serisi/` + her bölüm sonunda sınav-grill tetiği:** Artı: VS Code yüzeyi (Karar 80), pointer'lı. Eksi: görsel yok (görselleştir emekli; gerekirse mcp__visualize tek tek).
- **(b) Lavish HTML bölümleri:** Artı: annotasyon. Eksi: kanon dışı yüzey, tarihçe zayıf.
- **(c) Beklet (damıtma sonrası).**

### M12 · Prompt-başı dosya seçimi: model yorumu mu, deterministik hook mu (Katman-1; Salih 09-08 "önerini karar masasına taşı")
Ölçüm 09-08 (HEAD ae36f9d): her promptta sabit yük CLAUDE.md 6,9 KB + skill description 7,4 KB (16 skill) + MEMORY.md indeks 2,5 KB ≈ 19 KB; kapsül/pano/tüzük/hafıza dosyaları yalnız Carvis kararıyla okunur. Prompt-başı dosya basan hook (UserPromptSubmit) YOK; yalnız PreToolUse ×2 + SessionStart var. Sonuç: aynı prompt → farklı seansta farklı dosya seti mümkün; §6 deterministik tasarım ilkesiyle örtüşmez.
- **(a) ÖNERİLEN — UserPromptSubmit hook + anahtar-kelime→dosya tablosu (`core/prompt-dosya-tablosu.tsv`, ilk sürüm ≤10 satır):** Ne demek: prompt metni tabloyla eşleşirse hook o dosyanın YALNIZ ilk N satırını/pointer'ını bağlama basar ("seans" → kapsül başı; "m.NN" → tüzük o madde; "hafıza/feedback" → ilgili memory dosyası). Yaparım: hook script + tablo + 3 test + hareket kütüğüne olay satırı. Artı: deterministik, kütüğe düşer, tablo Salih'çe okunur/düzenlenir. Eksi: eşleşmeyen konu yine model yorumuna kalır; tablo bakımı (bir satır girer bir satır çıkar); yanlış eşleşme = boşa ~1-3 KB.
- **(b) Mevcut kalır, seçim kütüğe düşer:** Ne demek: hook yok; Carvis prompt-başı hangi dosyayı neden açtığını `veri/bronz/hareket-olay.jsonl`'e zaten yazıyor, buna "gerekçe" alanı eklenir. Artı: sıfır yeni mekanizma, tekrar-üretim kayıtla (§6 ikinci fıkra). Eksi: determinizm sağlanmaz, yalnız izlenir.
- **(c) Konu-başı ayrı CLAUDE.md profili (öğrenme / iş / jarvis-geliştirme):** Ne demek: klasör ayrımı gibi (staj örneği) konu başına alt-klasör + kendi CLAUDE.md'si. Artı: konu dışı 19 KB düşer. Eksi: üç kanon kopyası bakımı; jarvis-geliştirme zaten ana klasör, ayrım yalnız öğrenme/iş için anlamlı; m.16 kapsam sorusu (kanon tekliği).

## El işleri (karar değil, Salih tetiği)
A3 kalan ayak (uzun-loop sayacı 1/3) · İB-11 (d)(e) 10 dk · Finder md varsayılanı VS Code · bulut skill kopyaları (KB-10) · galeri gerçek 3 matris CSV'si.

## Masa sonrası icra (Fable)
Hükümler → `kuyruk/senaryo-defteri.md` Karar 87 bloğu · ledger · kapsül · M2(a) ise damıtma turu bu seansta.
