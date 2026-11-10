# Depo denetimi 2026-11-10: ham işçi raporları (oda 202611101157; özet ve hüküm listesi raporlar/2026-11/denetim-depo-2026-11-10.md)

---

## Rapor 1

**Rapor: görev #1, Rust crate'leri ve hook zinciri denetimi**

Yan etki: tart'ın hareket kütüğüne yanlışlıkla 5 satır yazdım, sonra geri aldım. Süre ölçümü için `tart/.claude/hooks/hareket-kutuk.sh` betiğini doğrudan koşturdum, betik `tart/veri/bronz/hareket-olay.jsonl` dosyasına 5 satır ekledi. Eklenenlerin tümü benimdi: `"yol": "x"`, oturum alanı boş. Yalnız bu son 5 satırı sildim. Dosyanın denetimden önce gelen 7 satırlık değişikliği yerinde duruyor (`git diff --stat`: +7). Bunun dışında hiçbir dosyaya dokunmadım. Yalnız scratchpad'e bir test betiği yazdım: `C:\Users\sasah\AppData\Local\Temp\claude\d37de251d0e91747\2b89f382-f56c-4601-a9b6-20ce97e32187\scratchpad\t.py`

**Ne yaptım:** Kök `Cargo.toml` ile 7 crate'in manifestini okudum. Hook crate'inin dispatch, core_tel, altajan_okuma, ajan_fren, session_start ve ortak modüllerini okudum. Ayrıca okunanlar: `bin/hook-dispatch.sh`, 10 adet `settings.json`, jarvis hook betikleri, 8 ajanın `okuma-izin.sh` ve `hareket-kutuk.sh` kopyaları, git-hooks. Kilitlere hazır JSON girdisi verip çıkış kodlarını ölçtüm, süreleri ölçtüm. İkililerin derleme tarihini kaynak commit'leriyle karşılaştırdım: tüm ikililer güncel, 10-26 sonrasında yalnız testler değişmiş. Belgelerde anılan ikili adlarıyla `[[bin]]` listesi de uyuşuyor.

**Bulgular (önem sırasıyla)**

1. `jarvis/kod/hook/src/altajan_okuma.rs:167` | bozuk | Git Bash yolu (`/c/...`) Windows yoluna çevrilmiyor. `realpath("/c/sistem/...")` sonucu `C:\c\sistem\...` oluyor, yasak listesiyle eşleşmiyor. Test: alt-ajan `cat /c/sistem/sistem/jarvis/core/durum-kapsulu.md` komutunda exit 0, göreli yolda exit 2 | `^/([a-zA-Z])/` önekini `X:/` biçimine çevir | kesin
2. `friday/.claude/hooks/okuma-izin.sh:46` (8 kopyanın hepsi, `coz`) | bozuk | Aynı atlatma. Test: tart'ta `cat /c/sistem/sistem/jarvis/CLAUDE.md` exit 0, `C:/...` biçimi exit 2 | `coz` içinde MSYS yol çevirisi ekle | kesin
3. `jarvis/kod/hook/src/core_tel.rs:13` | bozuk | Yönlendirme deseni yalnız göreli yolu yakalıyor. Test: `echo x > /c/sistem/sistem/jarvis/core/deneme.md` exit 0 | Desene mutlak önek ekle ya da yolu önce çöz | kesin
4. `.git/config` (`core.hooksPath=tools/git-hooks`) | bozuk | `C:\sistem\sistem\tools\git-hooks` diye bir dizin yok; betikler `jarvis/tools/git-hooks` altında. Commit-msg ve pre-commit telleri sessizce devre dışı | Değeri `jarvis/tools/git-hooks` yap | kesin
5. `jarvis/tools/git-hooks/pre-commit:11,17` | bozuk | Dosya deseni monorepo öncesinden kalma, köke göreli: `^(CLAUDE\.md|core/...)` kalıbı `jarvis/core/...` yollarını yakalamaz. `$KOK/tools/git-hooks/caps-say.py` yolu da yok. Ayrıca Rust `buyuk-harf-temizle` yerine Python sürümüne bağlı | Desenlere `jarvis/` öneki ekle, `$KOK/jarvis/tools/...` yolunu kullan, Rust ikilisine geç | kesin
6. `jarvis/kod/hook/src/dispatch.rs:37-40` | bozuk | Dispatcher ajan ayarından yalnız `hooks[olay]` okuyor. Ajanların `permissions.deny` ve `ask` kuralları (push frenleri, `git add -A` yasağı, `Edit(core/tuzuk*)`) kökten açılan oturumda hiç uygulanmıyor. Kök ayarda da deny yok (`_not` alanı bunu söylüyor) | Deny kurallarını dispatcher'da PreToolUse ile eşle ya da kök ayara birleşik deny yaz | kesin
7. `friday/.claude/settings.json:11` + 7 alan ajanı `settings.json:5-10` + `sablonlar/ajan-iskelet/claude-ayar/settings.json:5` | bozuk | `Read(~/sistem/jarvis/**)` gibi Mac yolları. `~/sistem` dizini yok (`ls`: No such file), deny kuralları etkisiz; şablon her doğumda bunu çoğaltıyor | Yolları `//c/sistem/sistem/...` ya da göreli `../jarvis/**` biçimine çevir | kesin
8. `tart/.claude/hooks/okuma-izin.sh:36` (`izinli` listesi) | bozuk | İzinli geçici dizinler `/tmp`, `/private/tmp`, `/private/var/folders`, hepsi Mac'e özgü. Windows geçici dizini ev altında kaldığı için engelleniyor. Test: `C:/Users/sasah/AppData/Local/Temp/x.txt` exit 2 | `tempfile.gettempdir()` ekle | kesin
9. Ajan hook'ları (`okuma-izin.sh`, `hareket-kutuk.sh`) | verimsiz | Rust karşılıkları yok, hâlâ her çağrıda Python koşuyor. Kökten açılan oturumda ajan cwd'sinde araç çağrısı başına zincir: bash → hook-dispatch.exe → `bash -c` → bash → python. Ölçüm 3,03 sn / 5 çağrı ≈ 0,6 sn. Tek başına hareket-kutuk 1,13 sn / 5 ≈ 0,23 sn | İkisini `jarvis-hook okuma-izin` ve `jarvis-hook hareket-kutuk` alt komutlarına taşı | kesin
10. `jarvis/kod/hook/src/session_start.rs:133,152` + `rituel/src/acilis.rs:263,309` | tutarsız | Silver bayatsa `python3 tools/katman-hatti.py` öneriliyor, oysa Rust `katman-hatti` var ve skill'ler onu birincil sayıyor | Metni `../target/release/katman-hatti` yap | kesin
11. `jarvis/kod/hook/src/session_start.rs:174` | tutarsız | Brif `denetim tools/ad-esitligi-denetim.py` diyor; dosya arşivde (Karar 118 M2) | `target/release/ad-esitligi-denetim` yaz | kesin
12. `jarvis/kod/rituel/src/katman_hatti.rs:19-49,59-67` | bozuk | İkili bulunamazsa `tools/hareket-tablo.py`, `silver-saglik.py`, `baglam-seyir.py`, `anakronizm-denetim.py`, `ambar-tablo.py` betiklerine düşüyor. Bunlar arşivlendi, dosya yok. `ikili_bul` ana worktree'ye bakmadığı için worktree'de hat düşer | Düşüş yolunu kaldır, net hata ver; ana worktree aramasını `rust-yonlendir.sh` mantığıyla ekle | kesin
13. `jarvis/kod/hook/src/session_start.rs:155` | tutarsız | `repo/../target/release/durum.exe` sabit: `.exe` taşınabilir değil ve worktree düşüşü yok | Platforma göre uzantı + gitdir düşüşü ekle | kesin
14. `jarvis/kod/kural/src/{argparse,py,harness_anahtar}.rs` ↔ `rituel/src/` aynı adlı dosyalar | gereksiz | Ayrışmış kopyalar: argparse 489/632 satır, py 416/572, harness_anahtar 55/71. py.rs'te 23 fonksiyon imzası ortak | Ortak bir crate'e (ör. jarvis-ortak) taşı | kesin
15. `jarvis/tools/{katman-hatti,kural-sayaci,baglam-tablo,buyuk-harf-temizle,kod-orani-olcum,prompt-dosya,paket-yonlendir}.py` | gereksiz | Rust karşılıklarıyla birlikte canlı duruyor. Skill'ler "yedek python3" diyor; çift bakım | Importlib bağımlılığı çözülünce arşive indir, skill'lerden yedek satırını kaldır | kesin
16. `jarvis/kod/arac/src/alan_ajani.rs:94-96` | tutarsız | Windows'ta CRLF yazıyor. deci, vega ve sage hook'ları indekste `i/crlf`; tart, gard, span ve calc'ınkiler `i/lf`. Git Bash'te çalışıyor (test: exit 2 doğru çıktı), POSIX'te bozulur | `.sh` dosyalarını LF yaz, `.gitattributes` içine `*.sh eol=lf` ekle | kesin
17. `jarvis/kod/hook/src/core_tel.rs:14` | bozuk | `\b(mv|cp|rm|touch|tee|...)\b.*core/` deseni salt-okur komutu da kesiyor; ör. `grep -n tee core/x.md` | Komut adını satır başında ya da ayraç sonrasında ara | kesin
18. `jarvis/.claude/settings.json` PreToolUse | verimsiz | Her Bash çağrısı 2 hook çalıştırıyor (core-tel + altajan), her biri bash + rust-yonlendir sarmalıyla. Ölçüm: sarmalı çağrı 0,146 sn, doğrudan exe 0,050 sn | Exe'yi settings'ten doğrudan çağır ya da iki denetimi tek alt komutta birleştir | kesin
19. Kök `.claude/settings.json` PostToolUse `.*` | verimsiz | Kök cwd'de ajan yokken bile her araç çağrısında dispatcher başlıyor: 0,545 sn / 5 ≈ 0,11 sn | Matcher'ı daralt ya da ajan dışı cwd'de bash'siz kısa yol aç | kesin
20. `friday/.claude/hooks/okuma-izin.sh:24-25` (8 kopya) | bozuk | Fail-open: Python yoksa `exit 0`, JSON bozuksa `exit 0`. Test: geçersiz JSON girdisi exit 0 | Kilit fail-closed olsun (exit 2) | kesin
21. `friday/.claude/settings.json:16` + alan ajanları | tutarsız | Hook komutu göreli (`bash .claude/hooks/okuma-izin.sh`); jarvis `${CLAUDE_PROJECT_DIR}` kullanıyor. Oturum içinde `cd` yapılınca dosya bulunamaz, exit 127 hata sayılmaz ve kilit atlanır | `"$CLAUDE_PROJECT_DIR"/.claude/hooks/...` yap | şüpheli
22. `jarvis/kod/arac/Cargo.toml:14` | gereksiz | `unicode-normalization` bağımlılığı arac içinde hiç kullanılmıyor (grep: 0 dosya) | Bağımlılığı sil | kesin
23. `jarvis/kod/hook/src/session_start.rs:164,189` | gereksiz | `let _ = oku_py;` ve `let _ = py_truthy;` kullanılmayan import'u bastırıyor; fonksiyonun adı da bayat (`python_kismi`) | Import'ları ve bastırmayı kaldır, adı değiştir | kesin
24. `jarvis/kod/hook/src/session_start.rs:186-188` | bozuk | `b.truncate(KAPI)` bayt sınırında kesiyor; çok baytlı Türkçe karakter ortadan bölünebilir | Kesmeyi `char_indices` ile karakter sınırında yap | şüpheli
25. `jarvis/kod/hook/src/dispatch.rs:47` | bozuk | Matcher `"*"` olursa `^(?:*)$` derlenmiyor, `unwrap_or(false)` yüzünden hook sessizce atlanıyor. Claude Code `*` değerini "hepsi" sayar. Bugün kullanan yok | `*` değerini boş matcher gibi ele al | kesin (gizli hata)
26. `jarvis/kod/hook/src/dispatch.rs:34-36` | gereksiz | Çift koşum freni yalnız kök ayar ajan projesinden yüklenirse tetiklenir; o durumda `CLAUDE_PROJECT_DIR` kök olur ve fren hiç devreye girmez | Ölçüp ölüyse kaldır | şüpheli
27. `jarvis/kod/hook/src/dispatch.rs:57-89` | verimsiz | Çocuk sürece zaman aşımı yok; asılan Python hook tüm aracı bekletir | `wait_timeout` ekle | kesin
28. `jarvis/kod/hook/src/paket.rs:275` | bozuk | `as_array().unwrap()...find().unwrap()`: pid manifestte yoksa ya da manifest bozuksa panik, UserPromptSubmit exit 101 | `?` ya da `let-else` ile sessiz çık | şüpheli
29. `jarvis/kod/skill-kapi/src/denetim.rs:18`, `arac/src/buyuk_harf.rs:62`, `arac/src/alan_ajani.rs:25`, `arac/src/kod_orani.rs:39` | tutarsız | Yardım metinleri `python3 tools/...py` kullanımını gösteriyor | İkili adına çevir | kesin
30. `jarvis/kod/arac/src/alan_ajani.rs:220` | tutarsız | Üretilen hook başlığı "`jarvis/tools/alan-ajani-dogur.py` yamasıyla üretilir" diyor; üretici artık Rust | Metni güncelle | kesin
31. `jarvis/kod/arac/src/yol_tasi.rs:23-28` | gereksiz | Tek seferlik Mac göçü (`~/jarvis` → `~/sistem/jarvis`, `-Users-HasanSalihSahin-*`); Windows'ta anlamsız | Arşive indir | şüpheli
32. `jarvis/kod/hook/src/altajan_okuma.rs:155` | gereksiz | Yasak listesinde Mac döneminden `~/Desktop/repo` | Doğrula, gereksizse çıkar | şüpheli
33. `bin/hook-dispatch.sh:15-16` + `jarvis/.claude/hooks/rust-yonlendir.sh:15` | bozuk | `for _hd_k in $_hd_aday` tırnaksız; boşluk içeren yolda bölünür | Dizi ya da satır satır okuma kullan | şüpheli
34. `jarvis/kod/hook/src/ajan_fren.rs:32-34` | verimsiz | `state/ajan-fren-<oturum>.json` hiç temizlenmiyor (bugün 26 dosya, ignore'da) | Oturum başında eskileri sil | kesin
35. `jarvis/.claude/hooks/userprompt-dosya.sh:3-5` | tutarsız | Başlık yorumu hâlâ `tools/prompt-dosya.py` ve `tools/paket-yonlendir.py` akışını anlatıyor | Yorumu Rust alt komutuna göre güncelle | kesin
36. `bin/hook-dispatch.sh:23-25` + 7 jarvis hook düşüşü | tutarsız | İkili yoksa tüm kilitler (core-tel, altajan, okuma-izin) exit 0. Karar 118 M2 bunu bilinçli seçmiş, ama yeni klon ya da worktree'de kilitler kapalı kalıyor | Kilit hook'larında ikili yoksa exit 2'yi değerlendir (Salih kararı) | şüpheli

**Doğrulama kanıtı**
- Atlatma testleri (`python3 .../scratchpad/t.py`): `/c/...` yolu üç kilitte de exit 0, `C:/...` ve göreli yol exit 2.
- `git config --show-origin core.hooksPath` → `tools/git-hooks`; `ls tools/git-hooks` → No such file.
- `git ls-files --eol` → deci, vega, sage hook'ları `i/crlf`.
- Süre ölçümleri `time` ile: 0,6 · 0,146 · 0,050 · 0,11 sn / çağrı.
- `ls -d ~/sistem` → yok.

**Done koşulu:** Sağlandı; kanıtlı 36 bulgu döndü.

**Açık kalan**
- Claude Code'un üst dizindeki `settings.json` dosyasını yükleyip yüklemediği dosyadan doğrulanamadı (madde 21 ve 26 buna bağlı, şüpheli).
- Madde 6 ve 7 Katman-1 kanon ayarı; düzeltme Salih kararı ister.

Taranan dosya: 91 Rust dosyası Grep ile tarandı (yaklaşık 15'i okundu), 7 crate manifesti + kök `Cargo.toml`, 10 `settings.json`, 12 jarvis hook betiği, 24 ajan hook betiği, 3 git-hook, `bin/hook-dispatch.sh`.
Taranmayan alan: rituel, kural, arac, durum ve baglam crate'lerinin iş mantığı satır satır okunmadı (yalnız desen taraması yapıldı); `tests/` dizinleri; katman-hatti'nin çağırdığı yaklaşık 15 Python aracı; `jarvis/.claude/skills/**` yalnız ikili ve betik adı için tarandı.
Genel hüküm: Rust geçişi jarvis hook'larında tamam, ikililer güncel. En büyük risk Windows yol biçimi: Git Bash'in `/c/` yolu üç kilidi de atlatıyor; Mac yollu deny kuralları ve yanlış `core.hooksPath` yüzünden git ve izin frenleri sessizce kapalı. Ajan hook'ları Python'da kaldığı için araç çağrısı başına yaklaşık 0,6 sn ödeniyor.

---

## Rapor 2

## Denetim: C:\sistem\sistem\jarvis\tools

Salt-okur çalıştım, hiçbir dosyayı değiştirmedim ve hiçbir script koşturmadım. Çağıran sayısı yaklaşık değerdir. Arşiv, `veri/`, `raporlar/`, `kuyruk/`, `cc/`, `wiki/`, patch dosyaları ve SCRIPTLER.md sayılmadı. Python testleri ve diğer script'lerin kendi içindeki anmaları ayrı yazıldı.

### Tablo

Rust karşılığı olan satırlar için ikili dosya `../target/release/` altındadır. `katman_hatti.rs` Python adımlarını `tools/…py` yoluyla çağırır; tabloda "katman_hatti.rs" yazan çağıranlar bunlardır.

| script | çağıran | Rust karşılığı | hüküm |
|---|---|---|---|
| katman-hatti.py | seans-acilis SKILL (yedek), KURULUM.md, 3 test | var: kod/rituel/src/katman_hatti.rs + katman-hatti.exe | kopya, Python gereksiz |
| kural-sayaci.py | seans-kapanis ve seans-acilis SKILL, kod-envanter.py, kural-envanter.py | var: kod/rituel/src/sayac.rs + kural-sayaci.exe | kopya |
| buyuk-harf-temizle.py | git-hooks/pre-commit | var: kod/arac/src/buyuk_harf.rs + buyuk-harf-temizle.exe | kopya |
| kod-orani-olcum.py | karantina.py, kod-envanter.py, 3 test | var: kod/arac/src/kod_orani.rs + kod-orani-olcum.exe | kopya |
| baglam-tablo.py | katman_hatti.rs (yedek), core/*.md, bag-tablo.py, anahtar-denetim.py | var: kod/rituel/src/baglam_tablo.rs + baglam-tablo.exe | kopya, yalnız yedek |
| prompt-dosya.py | kod/hook tests/ortak/mod.rs (fark testi), hook-dispatch yedeği, paket-yonlendir.py, test | var: kod/hook/src/prompt_dosya.rs | kopya; fark testi referansı |
| paket-yonlendir.py | hook fark testi, hook-dispatch yedeği, test | var: kod/hook/src/paket.rs | kopya; fark testi referansı |
| harness_anahtar.py | prompt-tablo.py, kosum-maliyeti.py (import) | var: kural/src/harness_anahtar.rs ve rituel/src/harness_anahtar.rs | kopya; arsiv/kod/python/tools/harness_anahtar.py ile bayt-eşit (md5) |
| baglam_oku.py | tuzuk-iz-tarama.py, prompt-dosya.py, sunum-proof-of-work.py, hook fark testi | yok | canlı (yardımcı modül) |
| ambar-parquet.py | katman_hatti.rs, kolon-olcum, tarama-plan-duckdb | yok | canlı |
| bag-tablo.py | katman_hatti.rs | yok | canlı |
| deneyim-tablo.py | katman_hatti.rs, damitma ve gorev-emri-derleme SKILL | yok | canlı |
| devir-ani.py | katman_hatti.rs, test | yok | canlı |
| erisim-fts.py | katman_hatti.rs, test | yok | canlı |
| karar-borcu-tablo.py | katman_hatti.rs, damitma ve karar-kaydet SKILL | yok | canlı |
| katman-olcum.py | katman_hatti.rs | yok | canlı |
| kolon-olcum.py | katman_hatti.rs, test | yok | canlı |
| loop-dedektor.py | katman_hatti.rs, test | yok | canlı |
| obsidian-harita.py | katman_hatti.rs | yok | canlı |
| pointer-graf.py | katman_hatti.rs | yok | canlı |
| prompt-tablo.py | katman_hatti.rs | yok | canlı |
| tarama-plan.py | katman_hatti.rs, test | yok | canlı |
| tarama-plan-duckdb.py | katman_hatti.rs | yok | canlı |
| akis-graf-html.py | mods/jarvis-graf (README, araclar.ts, test), ortak/akis-graf.json | yok | canlı |
| anahtar-denetim.py | damitma ve emekli-anahtar-cascade SKILL, silver_saglik.rs anması, 2 test | yok | canlı |
| anahtar-cascade.py | emekli-anahtar-cascade SKILL | yok | canlı |
| wiki-baglanti.py | damitma ve wiki-sayfa-yaz SKILL | yok | canlı |
| ta-triyaj.py | core/veri-muhendisligi-katmani.md, test | yok | canlı |
| yuzey-parmak-izi.py | core/baglam-anahtar-kaydi.md, tuzuk-v0-m41.md | yok | canlı (yalnız doküman anması) |
| kosum-maliyeti.py | KURULUM.md | yok | canlı (zayıf) |
| sunum-proof-of-work.py | KURULUM.md | yok | canlı (zayıf) |
| sunum-son50.py | sunum-proof-of-work.py | yok | canlı (zayıf) |
| karantina.py | yalnız test_karantina.py | yok | ölü aday |
| kod-envanter.py | karantina.py, test, AXI-STANDARDI.md | yok | ölü aday; kısmen bozuk (bulgu 9) |
| skill-butce.py | yalnız test | yok (skill_esik.rs başka işlev) | ölü aday |
| denetci-kalibrasyon.py | 0 | yok | ölü aday |
| d2-eval.py | yalnız denetci-kalibrasyon.py | yok | ölü aday |
| erisim-kalibrasyon.py | yalnız erisim-fts.py anması | yok | ölü aday |
| erisim-vektor.py | asof-eval, erisim-kalibrasyon, denetci-kalibrasyon | yok | ölü aday (zincir kendi içinde) |
| asof-eval.py | 0 | yok | ölü aday |
| atlas-derle.py | 0 | yok | ölü aday |
| baglam-skill-aday.py | yalnız core/skill-uretim-semasi.md ve instructions-loaded.sh yorumu | yok (hook Rust'a taşındı) | ölü aday |
| kural-envanter.py | yalnız denetci-kalibrasyon.py ve fikir-kutusu.md | yok | ölü aday |
| headless-esleme.py | 0 | yok | ölü aday |
| olcum-dortlu.py | 0 | yok | ölü aday |
| pointer-kayma.py | 0 | yok | ölü aday |
| silver-saglik-kalibrasyon.py | 0 | yok | ölü aday |
| tuzuk-iz-tarama.py | 0 | yok | ölü aday |
| verify-push.py | 0 | yok | ölü aday |
| masa-html.py | 0, SCRIPTLER.md'de yok | var: arac/src/masa.rs (masa-uret) | ölü aday / kopya |
| gnhf-izle.py | 0 | yok | ölü aday; bozuk (bulgu 11) |
| pano-akis.py | yalnız buyuk-harf-temizle.py anması | yok | ölü aday; pano 2026-10-25'te dondu |
| gece-senkron.ps1 | yalnız arşiv | yok | emekli (SCRIPTLER'da üstü çizili); bayat yol |
| git-hooks/pre-commit, commit-msg, caps-say.py | `core.hooksPath` | yok | bozuk (bulgu 1) |

### Bulgular

1. `tools/git-hooks/pre-commit:11-13` | bozuk | `.git/config` içinde `core.hooksPath=tools/git-hooks` var. Git bunu çalışma ağacı köküne göre çözer (`C:\sistem\sistem\tools\git-hooks`), ama bu dizin yok (`ls` doğruladı). Betiğin kendisi de `$KOK/tools/git-hooks/caps-say.py` yolunu ve kökte `core/…`, `.claude/skills/…` desenlerini bekliyor; bu yollar artık `jarvis/…` altında. Büyük harf teli ve commit-msg teli fiilen çalışmıyor. | Elle `hooksPath = jarvis/tools/git-hooks` yap ve betikteki yolları `jarvis/` önekiyle yaz; ya da Rust `buyuk-harf-temizle` ile `hook-dispatch`'e taşı. Kanon tel olduğu için Salih kararı gerekir. | kesin
2. `tools/git-hooks/commit-msg:6-7` | tutarsız | Başlık "bilinçli ertelenmiş, hook devreye alınmadı" diyor; `hooksPath` ise ayarlı ama yanlış dizine bakıyor. | Başlık yorumunu gerçek duruma göre güncelle. | kesin
3. `kod/rituel/src/katman_hatti.rs:19-41,47-49` | tutarsız | Rust hat, Python betiklerini `tools/…` altında çağırıyor; bu yüzden 15 Python script canlı. `tools/ambar-tablo.py`, `hareket-tablo.py`, `baglam-seyir.py`, `silver-saglik.py`, `anakronizm-denetim.py` artık yok (arşive taşındı). Rust bunları önce ikiliyle koşuyor, ikili yoksa var olmayan Python yedeğine düşüyor. | Yedek yolunu kaldır ya da arşive yönlendir. Kalan 15 adımı Rust'a taşıma kararı ayrı. | kesin
4. `tools/katman-hatti.py` (17 KB) | gereksiz | Rust `katman-hatti.exe` var. Python yalnız seans-acilis SKILL:27 "yedek" satırı ve 3 testte duruyor. | Karar 118 M2 gibi `arsiv/kod/python/tools/` altına indir, SKILL yedek satırını sil. | kesin
5. `tools/kural-sayaci.py`, `buyuk-harf-temizle.py`, `kod-orani-olcum.py` | gereksiz | Üçünün Rust ikilisi `target/release/` altında var, SCRIPTLER.md satırları 102 ve 104 de bunu söylüyor. Python hâlâ `kod-envanter.py:190`, `pre-commit`, 3 test ve SKILL anmalarına bağlı. | Bağlı yerleri Rust'a çevirip arşive indir. | kesin
6. `tools/harness_anahtar.py` | gereksiz | `arsiv/kod/python/tools/harness_anahtar.py` ile bayt-eşit (md5 aynı). Rust karşılığı iki crate'te var. Yalnız `prompt-tablo.py:15` ve `kosum-maliyeti.py:29` import ediyor. | Arşiv kopyasından biri sil ya da import'ları Rust çıktısına çevir (m.8: silme yerine arşiv). | kesin
7. `tools/SCRIPTLER.md:55` | tutarsız | `hareket-tablo.py` kök `tools/` tablosunda aktif satır olarak duruyor. Dosya yalnız `arsiv/kod/python/tools/` altında var. | Satırı Rust ya da arşiv notuyla değiştir. | kesin
8. `tools/SCRIPTLER.md:14-17,88` | tutarsız | `masa-uret.py` (skills/karar-masasi/scripts içinde yok), `kapi-denetim.py` (skills/skill-kapisi/scripts içinde yok), `devir-md2json.py` ve `test_devir_md2json.py` (kök `tools/`te yok) aktif script gibi listelenmiş. `.claude/skills/karar-masasi/scripts/` yalnız `masa-spec-cikar.py` ve `masa-uret-test.py` içeriyor. Bunların Rust karşılıkları var (`masa-uret.exe`, `skill-kapi.exe`, `devir-md2json.exe`). | Satırları "Rust" notuna çevir. | kesin
9. `tools/SCRIPTLER.md` | tutarsız | Dizinde olup listede olmayan 2 dosya: `baglam_oku.py` (canlı yardımcı modül) ve `masa-html.py`. | `baglam_oku.py` için satır ekle; `masa-html.py` için ölü adaydır, arşivle ya da sil. | kesin
10. `tools/kod-envanter.py:181,185-190` | bozuk | Gecikme ölçümü `["python3",…]` ile `/usr/bin/true` çağırıyor (Mac/Linux). Windows'ta `subprocess` bash shim'i (`~/bin/python3`) çalıştıramaz. `/usr/bin/true` yol kontrolsüz ekleniyor. `tools/kural-sayaci.py` satırı da arşive gidecek script'e bağlı. | Yalnız ölü adayı arşivlemek yeterli; canlı tutulacaksa `sys.executable` ve Windows komutuna çevir. | şüpheli (çalıştırmadım)
11. `tools/gnhf-izle.py:17` | bozuk | `KOK = expanduser("~/sistem/jarvis-gnhf-worktrees")`; `~/sistem` Windows'ta yok (`ls ~/sistem` hata verdi). Çağıranı yok. | Arşivle. | kesin
12. `tools/olcum-dortlu.py:7-10` | gereksiz | Başlıkta `~/sistem/jarvis/tools/…`, `C:\JARVIS\tools\…` ve `~/dev/wf-deneme` yolları var. Çağıranı yok. | Arşivle. | kesin
13. `tools/gece-senkron.ps1:5-6` | gereksiz | `C:\JARVIS` ve `raporlar\usage\senkron-log.jsonl` sabit yolları; Karar 81/KB-16 ile emekli, SCRIPTLER'da üstü çizili. m.8 gereği dosya duruyor ama `tools/` altında yaşıyor. | `arsiv/zamanlanmis-gorev/` altına indir (orada XML'i var). | kesin
14. `tools/pano-akis.py` | gereksiz | `core/pano.md` 2026-10-25'te dondu. Script pano kartlarını parse eder ve `YIL = 2026` sabitine dayanır. Çağıranı yok. | Emekli mekanizma; arşive indir. | kesin
15. `tools/asof-eval.py`, `atlas-derle.py`, `denetci-kalibrasyon.py`, `d2-eval.py`, `headless-esleme.py`, `pointer-kayma.py`, `silver-saglik-kalibrasyon.py`, `tuzuk-iz-tarama.py`, `verify-push.py` | gereksiz | Hiçbir canlı çağıranı yok (hook, skill, core, KILAVUZ, `kod/**`, `mods`, `bin`). Yalnız kendi içlerinde ve eski arşiv anmaları. | Toplu arşive indir; Salih onayı gerekir. | kesin (çağıran yok); karar şüpheli
16. `tools/erisim-kalibrasyon.py`, `erisim-vektor.py`, `kural-envanter.py` | gereksiz | Yalnız ölü adaylar `asof-eval`, `denetci-kalibrasyon` ve kendi aralarında anılıyor. `erisim-fts.py`'yi `karantina.py` anıyor, kendisi canlı. | 15. maddeyle birlikte arşivle. | şüpheli
17. `tools/baglam-skill-aday.py` | gereksiz | Anan tek şey `core/skill-uretim-semasi.md` ve `instructions-loaded.sh:6` yorumu. Hook gövdesi `jarvis-hook`'a taşındı. | Arşive indir; skill-uretim-semasi.md satırını güncelle. | şüpheli
18. `tools/karantina.py`, `kod-envanter.py`, `skill-butce.py` | verimsiz | Yalnız kendi testleriyle bağlı; testler de bu script'lere özel. Bakım yükü (16 testten 4'ü). | Arşivle ya da canlı tutulacaksa SCRIPTLER'a işlevini yaz. | şüpheli
19. `tools/masa-html.py` | gereksiz | Çağıran yok, SCRIPTLER'da yok, `masa-uret` (Rust, `kod/arac/src/masa.rs`) aynı işi yapıyor. | Arşivle. | kesin
20. `tools/obsidian-harita.py:43` | tutarsız | `VARSAYILAN_IGNORE` içinde `arsiv/claude-izler/`; bu dizin yok (`ls arsiv` doğruladı). | Satırı sil. | kesin
21. `tools/baglam-tablo.py:487,496` | tutarsız | Yol önek listesi `~/sistem/jarvis/` ve `C:/JARVIS/` içeriyor; Windows kökü `C:\sistem\sistem\jarvis`. | `C:/sistem/sistem/jarvis/` ekle. | şüpheli
22. `tools/sunum-proof-of-work.py:52` | tutarsız | `raporlar/vardiya/vardiya-teslim-` önekini sayıyor; `raporlar/vardiya` dizini var ama "vardiya" mekanizması seans'a döndü. | Önek yoksa sayacı kaldır. | şüpheli
23. `tools/sunum-proof-of-work.py:6`, `sunum-son50.py:5` | tutarsız | Başlıkta `open -R <dosya> + open <dosya>` (macOS komutu). | `explorer /select,` ya da `start` ile değiştir. | kesin
24. `tools/kural-envanter.py:32` | tutarsız | Regex içinde `open -R`; Mac'e özgü teslim ifadesini arıyor, Windows teslimini görmez. | `explorer` desenini ekle. | şüpheli
25. `tools/anahtar-cascade.py:17`, `gnhf-izle.py:10,17` | tutarsız | Kullanım örneklerinde `~/sistem/jarvis` ve `python3 …` yolları. | Windows yoluna çek. | kesin
26. `tools/testler/test_fren_hook.py:8`, `test_lean_skillkapi.py:3` | tutarsız | Test `.claude/hooks/pretool-ajan-fren.sh` bash hook'unu koşuyor; diğer hook gövdeleri Rust'a taşındı. `test_lean_skillkapi.py` `~/.elan/bin` ile `lake`'e bağlı (Windows'ta `.elan` yolu farklı olabilir). | Hook Rust'a taşınınca Rust testine çevir. | şüpheli
27. `tools/testler/` (16 test) | tutarsız | `test_prompt_dosya.py`, `test_paket_yonlendir.py`, `test_kod_orani.py` Rust'a taşınmış işlevlerin Python sürümünü sınıyor. Rust tarafında zaten `kod/hook/tests/hook_fark*.rs` fark testi var. | Python script arşive inince bunları da arşivle. | şüpheli
28. `tools/AXI-STANDARDI.md` | tutarsız | "İlk uygulama: `katman-hatti.py --json`" diyor; ilk uygulama artık Rust ikilisi. | Metni güncelle. | kesin
29. `tools/__pycache__` (112 `.pyc`), `testler/__pycache__` (39) | tutarsız | Git'te izlenmiyor: `git ls-files . | grep -c pycache` = 0 ve `.gitignore:4` `__pycache__/`. Ama dizinde artık olmayan script'lerin önbelleği duruyor (`hareket-tablo`, `hafiza-ayna`, `alan-ajani-dogur` vb.) ve Python 3.11 ile 3.13 çift sürüm var. | Temizlik gerekmez (ignore'lu); isteğe bağlı sil. | kesin
30. `tools/.DS_Store` (10 KB, Mac artığı) | gereksiz | Git'te izlenmiyor ama dizinde duruyor. `../friday/.DS_Store` ise `git status`'ta `M` görünüyor, yani izleniyor. | `.DS_Store` satırını `.gitignore`'a ekle ve izlenen kopyayı çıkar (`friday/` bu işin kapsamında değil). | kesin

### Sonuç

- **Taranan dosya:** 52 kök `.py`, 1 `.ps1`, 3 `git-hooks/` dosyası, 16 `testler/*.py`, `SCRIPTLER.md`, `AXI-STANDARDI.md`, iki `testler/veri/*.jsonl`, `akis-graf-html.sablon.html`. Ayrıca `__pycache__` içindeki 112 + 39 dosya adı karşılaştırıldı.
- **Hüküm özeti:** 15 canlı Python script (katman_hatti.rs çağırıyor) ve 12 diğer canlı. 8 Rust'la kopya. 16 ölü aday. 3 bozuk (`git-hooks/*`, `gnhf-izle.py`, `kod-envanter.py` kısmen).
- **Doğrulanmayan noktalar:**
  - Script'ler koşturulmadı, bulgu 10'un Windows davranışı çalıştırılarak kanıtlanmadı.
  - `core.hooksPath` çözümleme davranışı git belgesine ve dizinin yokluğuna dayanıyor; commit denemesiyle sınanmadı.
  - Kök `arsiv/kod/python/` yalnız kopya tespiti için tarandı. `jarvis/.claude/skills/*/scripts/` yalnız `ls` ile bakıldı.
  - Çağıran taraması metin eşleşmesidir; dinamik yol kurma (örn. `"tools/" + ad`) yakalanmamış olabilir.
  - Grep'te `.gitignore` kuralları dışlandı; `--hidden` yalnız `.claude` ve `.githooks` için ayrıca koşuldu.

---

## Rapor 3

**Rapor: görev #3, kanon ve skill denetimi (salt-okur, hiçbir dosya değişmedi)**

**Ne yaptım:** Kapsamdaki 126 dosyadan backtick içindeki yolları script'le çıkardım ve her birinin depoda olup olmadığını denedim. Bayat terimleri (kapsül/pano, Mac yolu, Carvis, gece-senkron, python3, Opus 5) Grep ile taradım. Bütçeleri wc ile ölçüp `lean/Kanon/Butce.lean` tavanlarıyla karşılaştırdım. Skill frontmatter, tetik ve kopyaları ayrıca denetledim.

## Bulgular (önem sırasıyla)

1. `jarvis/AGENTS.md:3` | tutarsız | "Durum → `core/durum-kapsulu.md`" yazıyor; aynı dosyanın §3'ü (satır 17) "Karar 122, kapsül/pano dondu" diyor | pointer'ı `durum oturum-basi` + `raporlar/seans/*.json` yap | kesin
2. `jarvis/AGENTS.md:9` | bayat | "Seans öncekini kapsülden devralır" (Karar 122 sonrası) | "seans kaydından + durum kütüğünden devralır" yaz | kesin
3. `jarvis/AGENTS.md:37` ve `:40` | bayat | "`core/` kanon, kapsül, pano" ve "(→ kapsül/pano/defter/git log)" | dondu notu düş ya da durum kütüğünü göster | kesin
4. `README.md:32` (kök) | bayat | Ajan okuma sırası hâlâ "`core/durum-kapsulu.md` → `core/pano.md`" | jarvis/AGENTS §3 sırasıyla hizala | kesin
5. `jarvis/README.md:13` ve `:38` | bayat | Okuma sırası 2. adım ve tablodaki "ilk açılacak" = durum-kapsulu.md | `durum oturum-basi` yap | kesin
6. `jarvis/KILAVUZ.md:6,8,9,19,20,62` | bayat | Açılışta "kapsül + pano okunur", kapanışta "kapsül güncellenir"; soru tablosu kapsül/pano gösteriyor | Karar 122 akışına çevir | kesin
7. `jarvis/.claude/skills/seans-kapanis/SKILL.md:3` | tutarsız | description "… + kapsül + commit/push üretir", aynı dosyanın §5'i (satır 35) "kapsül/pano yazılmaz" diyor; satır 11 "Bayat kapsül boş kapsülden kötüdür" | description'dan "kapsül"ü çıkar, satır 11'i kayda çevir | kesin
8. `jarvis/core/ajan-metodolojisi.md:16-17` | bayat | eager sınıfı "CLAUDE.md · kapsül · pano" | eager listesini güncelle | kesin
9. `jarvis/core/ingest-semasi.md:27,45` | bayat | `borç` tipi hedefi "kapsül 'Açık borçlar' / pano" | hedefi durum kütüğü yap | kesin
10. `jarvis/kaynak-kodu/README.md:19` | bayat | "Durum" satırı kapsül/pano | güncelle | kesin
11. `README.md:20` (kök) | bozuk | `jarvis/tools/alan-ajani-dogur.py` yok; kök `AGENTS.md:5` aynı aracı Rust `target/release/alan-ajani-dogur` sayıyor (Python gövdesi `arsiv/kod/python/`) | Rust ikiliye çevir | kesin
12. `jarvis/.claude/skills/emekli-anahtar-cascade/SKILL.md:11` | bozuk | `tools/ad-esitligi-denetim.py` yok; `target/release/ad-esitligi-denetim.exe` var | Rust yoluna çevir | kesin
13. `jarvis/core/baglam-anahtar-kaydi.md:494,508` | bozuk | aynı kayıp `tools/ad-esitligi-denetim.py` | Rust yolu | kesin
14. `jarvis/.claude/skills/gorev-emri-derleme/SKILL.md:27` | bozuk | yedek `tools/skill-esik.py` yok (Rust `skill-esik.exe` var) | yedek ibaresini sil | kesin
15. `jarvis/core/ajan-metodolojisi.md:40` | bozuk | "hesap `tools/skill-esik.py`" yok | `../target/release/skill-esik` | kesin
16. `jarvis/core/ajan-metodolojisi.md:67` | bozuk | `core/desenler.md` yok | arşivdeki yerini göster ya da sil | kesin
17. `jarvis/core/ajan-metodolojisi.md:58` | bozuk | `.claude/agents/orkestrator.md` yok (satır üstü çizili, ama aynı satırda yeni hüküm "Opus 5 medium") | yeni hükmü Opus 5.5 yaz, ölü yolu temizle | kesin
18. `jarvis/core/ajan-metodolojisi.md:39,58` · `core/tuzuk-v0-m42.md:1` · `core/tuzuk-v0-m44.md:1` · `.claude/agents/research-agent.md:18` | tutarsız | "lider = Opus 5"; `ajan-metodolojisi.md:55`, kök README ve jarvis/AGENTS:9 "Opus 5.5 (Karar 106)" diyor | Opus 5.5'e hizala (tüzük için Salih imzası gerekir) | kesin
19. `jarvis/core/halusinasyon-paketi.md:55` | tutarsız | Birincil komut `python3 …/derece.py`; skill `halusinasyon-engelleyici:12` ve `gorev-emri-derleme:15` Rust `../target/release/derece`'yi birincil, Python'u yedek sayıyor | Rust'ı birincil yaz | kesin
20. `jarvis/.claude/agents/research-agent.md:5` | bozuk | tools listesinde `mcp__context7__get-library-docs` var; oturumdaki context7 araçları `resolve-library-id` ve `query-docs` | adı `query-docs` yap | şüpheli
21. `jarvis/.claude/agents/research-agent.md:2` | tutarsız | dosya adı `research-agent.md`, frontmatter `name: atlas` | dosyayı `atlas.md` yap (m.8: eski ad pointer) | kesin
22. `jarvis/.claude/agents/hakem.md:5-7` | tutarsız | tools Read/Grep/Glob/Web, "salt-okur, yazmaz"; `memory: project` yüzünden oturumda etkin araçlar Write ve Edit'i de içeriyor (ajan listesinde görülüyor) | sözleşmeye "yalnız hafıza dizinine yazar" ekle ya da memory'yi kapat | şüpheli
23. Global skill'ler `anthropic-skills:gunaydin-vardiya` ve `vardiya-kapanis` | gereksiz | oturumda hâlâ etkin; Carvis, `C:\JARVIS`, "günaydın" tetiği taşıyorlar; `kaynak-kodu/README.md:39` 08-17'den beri "KALDIRILACAK" diyor | claude.ai'dan kaldır (Salih eli) | kesin
24. `seans-acilis` description ile `anthropic-skills:dev-run-planner` ve `gunaydin-vardiya` | tutarsız (çakışan tetik) | üçü de "oturuma başlayalım" tetiğini taşıyor | jarvis skill'inden bu kalıbı çıkar ya da global skill'leri kaldır | kesin
25. `jarvis/.claude/skills/seans-acilis/SKILL.md:18` ve `ogren/SKILL.md:12,16` | tutarsız | öğrenme şeritleri (evals · guvenlik · mit-6006 · mit-6042j · mat-felsefesi) jarvis'teki `ogren` skill'ine yönleniyor; skill `ogrenme/<şerit>/`'i okuyup yazıyor. Kök `AGENTS.md:5` "`ogrenme/` ajanlara kapalı" diyor ve bu alanlar Tart/Gard/Calc ajanlarına verilmiş | yönlendirmeyi alan ajanlarına bağla ya da istisnayı kanona yaz | kesin
26. `jarvis/core/sokrates-ajani.md:213` | verimsiz (bütçe aşımı) | §7 başlığı "≤900 kelime" diyor; ölçüm `wc -w` = 1592 (skill kopyasının gövdesi 1600) | metni buda ya da sınırı güncelle | kesin
27. `.claude/agents/sokrates.md:9` ile `.claude/skills/sokrates/SKILL.md:9` | tutarsız (iki kopya) | ikisi de `core/sokrates-ajani.md` §7'nin kopyası ve "yeniden türet" diyor; tools/ altında türetici yok; diff sonu farklı (kartlar satırı ↔ `$ARGUMENTS`) | türetici script yaz ya da tek kopyaya indir | kesin
28. `jarvis/.claude/skills/README.md` | tutarsız | katalogda 19 skill var, `sokrates` yok; `sokrates/evals/` da yok (`skill-standardi.md:7`: "Eval'siz yayın `YOK`") | katalog satırı ve eval ekle | kesin
29. `jarvis/KILAVUZ.md:53` | tutarsız (sayı) | "CLAUDE.md 8KB"; `Butce.lean:20` ve jarvis/AGENTS:3 7 KB (7168) diyor; aynı satır donmuş kapsül/pano bütçelerini hâlâ sayıyor | 7 KB yaz, dondu notu düş | kesin
30. `~/.claude/projects/C--sistem-sistem/memory/MEMORY.md` | verimsiz (bütçe aşımı) | `Butce.lean:6` hafıza indeksi tavanı 4 KB; ölçüm 6303 bayt | indeksi buda (kapsam sınırında) | kesin
31. `jarvis/kaynak-kodu/README.md:5-8` | bayat (Mac) | "Nasıl açarım (Finder)", `open ~/jarvis/kaynak-kodu`, ⌘⇧. kısayolu | Windows Explorer komutu ve gizli dosya ayarı | kesin
32. `jarvis/AGENTS.md:9,12,23` | bayat (Mac) | "depo = `~/sistem`", "Finder'da görünür", "cwd `~/sistem/jarvis`" | `C:\sistem\sistem`, Explorer | kesin
33. `README.md:8-16` (kök) | bayat (Mac) | dokuz ajan satırında "cwd `~/sistem/<ajan>`" | Windows yolu | kesin
34. `jarvis/core/ajan-metodolojisi.md:57` | bayat (Mac) | "tek Fable ana oturumu (`~/jarvis`)" | `C:\sistem\sistem\jarvis` | kesin
35. `KURULUM.md:6,10,12,49,68` | bayat/bozuk | Mac clone yolu `~/sistem`; `python3 tools/katman-hatti.py` (Rust var); `/Users/HasanSalihSahin`; kayıp `tools/acilis-kapilari.py`, `tools/yol-tasi.py`, `tools/alan-ajani-dogur.py`; §6 "Kapsül …" | dosyayı Windows + Rust + Karar 122'ye göre yeniden yaz (ya da tarihli kayıt diye damgala) | kesin
36. `KURULUM.md:9,43-44` | tutarsız (kopya kayması) | `sablonlar/harness/claude-global-CLAUDE.md` "birebir kopya" deniyor; canlı `~/.claude/CLAUDE.md`'den farklı (13 ↔ 11 satır, şablonda hâlâ "Mac"); settings.json da farklı | şablonu canlıdan yeniden al | kesin
37. `KURULUM.md:51` ile §4 tablosundaki `.venv` satırı | tutarsız | satır 51 "`jarvis/.venv` silindi" ve "no-mistakes symlink'i Mac yolunda" diyor; tablo ".venv boş sanal ortam" diyor; symlink bugün `/c/Users/sasah/.no-mistakes`'e bakıyor | iki ifadeyi düzelt | kesin
38. `jarvis/.claude/skills/skill-kapisi/references/skill-standardi.md:13` | bayat | "dağıtım gece-senkron/pull ile" (Karar 81 iptal) | "git pull ile" | kesin
39. `jarvis/.claude/skills/seans-kapanis/SKILL.md:14` ve `seans-acilis/SKILL.md:26` | bayat | bulut "mount'u senkron scripti eşitler" / "mount'ta git yasak" (Cowork dönemi) | Windows birincil düzene göre buda | şüpheli
40. `jarvis/.claude/skills/seans-acilis/SKILL.md:17` | bayat | SNAPSHOT zemini `CHAT-KAPSULU-*` / `CEP-KAPSULU-*`; bunlar yalnız `arsiv/kurulus-2026-07/`'de (07-11/13) | son seans JSON kaydını zemin yap | kesin
41. `jarvis/README.md:15` | bozuk | `00_MASTER_PLAN.md` … `03_DUVAR_RAPORU.md` jarvis kökünde yok, `arsiv/kurulus-2026-07/`'de | yolu düzelt | kesin
42. `jarvis/README.md:23,42,43` | bayat/bozuk | "vardiya-teslim-* dosya adı; cascade sürüyor" (raporlar/seans'ta 53 seans-teslim, 0 vardiya); ilk açılacak `raporlar/seans-teslim-*.md` (artık `raporlar/seans/*.json`); `ogrenme/` jarvis altında değil, kökte | güncelle | kesin
43. `jarvis/README.md:18-31` ile `:35-44` | gereksiz (iki yerde aynı içerik) | aynı dosyada iki "Klasör haritası"; jarvis/AGENTS §7 ve KILAVUZ ile üçüncü kopya | tek haritaya indir | kesin
44. `jarvis/core/varlik-felsefesi.md:21,22,28` | bozuk | göreli md bağlantısı `ogrenme/kaynaklar/...` `core/` altından `jarvis/core/ogrenme`'ye çözülür, yok | `../../ogrenme/...` yap | kesin
45. `AGENTS.md:5` (kök) ile `README.md:17` | tutarsız | kök kanon "`<alan>-hakem/` ya da ortak `hakem/`" dizini diyor; ikisi de yok, README hakemi `jarvis/.claude/agents/hakem` sayıyor | kök metni ajan tanımı yoluna çevir | kesin

**Ek gözlemler (listeye sığmayan, düşük önem):**
- `seans-kapanis:70` eski yol `veri/sozlesme/tarama-plan.jsonl`'u anıyor; dosya şimdi `veri/tarama-plan.jsonl`.
- Kök `.gitignore` `.DS_Store`'u dışlıyor ama `friday/.DS_Store` git'te izleniyor.
- `jarvis/.gitignore` `.lavish/` satırı kökteki `**/.lavish/` satırının kopyası.
- `tools/katman-hatti.py`, `kural-sayaci.py` ve `baglam-tablo.py` Rust ikilileriyle çift uygulama olarak duruyor; skill'ler bunları "yedek" diye anıyor (bakım maliyeti, şüpheli).
- `paylasim/ekip-skilleri/seans-basi` "seans başı" tetiğini seans-acilis ile paylaşıyor; aynı projeye kurulmadığı için şu an canlı çakışma yok.

## Doğrulama kanıtı
- `bash scratchpad/yol.sh`: 177 kırık aday buldu; göreli ve şablon yanlış pozitifleri eledim, kalanlar yukarıda. Script: `C:\Users\sasah\AppData\Local\Temp\claude\d37de251d0e91747\2b89f382-f56c-4601-a9b6-20ce97e32187\scratchpad\yol.sh`
- `ls`/`[ -e ]` taraması: `YOK tools/skill-esik.py`, `YOK tools/ad-esitligi-denetim.py`, `YOK core/desenler.md`, `YOK .claude/agents/orkestrator.md`, `YOK jarvis/00_MASTER_PLAN.md`, `YOK jarvis/tools/alan-ajani-dogur.py`.
- `wc`: kök AGENTS.md 22 satır / 7081 B (sınırda değil, geçer). jarvis/AGENTS.md 40 satır / 7164 B; tavan 7168, yani 4 bayt pay kaldı, aşmıyor. KILAVUZ 10227 B (tavan 16 KB). fikir-kutusu 19448 B (tavan 20 KB). MEMORY.md 6303 B (tavan 4 KB, aşıyor).
- Sokrates §7 için `wc -w` = 1592. `diff` agent ↔ skill kopyası: yalnız son satırlar farklı. `diff -q` harness şablon ↔ canlı: iki dosya da farklı.
- Bütün skill description'ları ≤1024 karakter (en uzunu `ogren` 861). Frontmatter'ların hepsi `---` ile açılıp kapanıyor; bozuk frontmatter yok.

## Done koşulu
Sağlandı: kırık atıf, çelişki ve bayat talimat bulguları kanıtlı liste olarak yukarıda.

## Taranan / taranmayan
- **Taranan:** 126 dosya (core 42 dosya + `core/sablonlar` + `paket-kapsul`, 20 SKILL.md + references, 3 ajan, kaynak-kodu, paylasim, kök ve jarvis üst düzey dosyaları).
- **Taranmayan:**
  - `core/durum-kapsulu.md` ve `core/pano.md`: alt-ajan okuma kilidi (İB-83) reddetti; "dondu" damgası doğrudan doğrulanamadı.
  - `kuyruk/senaryo-defteri.md` aynı kilitle kapalı; karar numaralarının defterle eşleşmesi denetlenmedi.
  - friday ve alan ajanı dizinleri: kök README:29'daki `okuma-izin.sh` atfı doğrulanmadı.
  - `kaynak-kodu/lavish|no-mistakes|obsidian` symlink içerikleri.
  - Tüzük parçalarının gövde metni: yalnız hedefli Grep yapıldı.

## Genel hüküm
- Kanonun omurgası sağlam: Lean hükümleri ve Rust ikilileri metinde anıldığı yerde var. Bütçeler (MEMORY.md ve Sokrates §7 dışında) tutuyor.
- En büyük sorun Karar 122 sonrası yarım kalan geçiş. Kapsül/pano 9 canlı dosyada hâlâ okuma/yazma hedefi olarak duruyor; jarvis/AGENTS.md kendi içinde çelişiyor.
- İkinci sorun Mac→Windows ve Python→Rust geçişinin kalıntıları: KURULUM.md, kaynak-kodu/README, `~/sistem` yolları ve kayıp `.py` yedekleri.
- Üçüncü sorun claude.ai'daki emekli global skill'ler. Hâlâ etkinler ve tetik çakışması üretiyorlar.

---

## Rapor 4

Salt-okur denetim bitti. Hiçbir dosyaya, git durumuna dokunulmadı. Tek tavsiye notu: `.claude/` içeren Bash komutları PreToolUse teline takılıyor, bu yüzden CRLF doğrulamasını Grep ile yaptım.

## Bulgular (önem sırasıyla)

1. `*/.claude/settings.json` (friday hariç 7 alan ajanı), `sablonlar/ajan-iskelet/claude-ayar/settings.json` | **bozuk** | deny kuralları `Read(~/sistem/jarvis/**)`, `Write(~/sistem/sablonlar/**)` vb. Mac yolu. Bu makinede `~/sistem` = `C:\Users\sasah\sistem` ve yok (`ls -d ~/sistem` hata verdi). Depo `C:\sistem\sistem`'de. | Yolu Windows depo köküne göre yeniden yaz (şablon + 8 kopya). | kesin (yolun yokluğu doğrulandı). Deny'nin bu çözümlemeyle eşleşmediğini varsayıyorum, harness davranışını çalıştırıp denemedim. Okuma kilidi hook'ta olduğu için sızıntı sınırlı, ama yazma ve push frenleri deny'ye bağlı.
2. `friday/.claude/` | **tutarsız** | Şablondaki `agents/hakem.md`, `agent-memory/hakem/`, `okuma-izin-ek`, `skills/ogren` yok. `okuma-izin.sh` v0.5 (v0.6 `okuma-izin-ek` desteği ve `AJAN_HOOK_TEST` yok). settings deny'sinde `Edit(kanon/**)`/`Write(kanon/**)` var; `kanon/` yok (`friday/README.md:3` "kanon/ symlink emekli" diyor). `ogrenme/**` ve `sablonlar/**` yazma deny'si yok. | Friday'i şablona göre yeniden doğur ya da bilinçli sapmayı belgele. | kesin
3. `friday/.DS_Store` | **gereksiz** | `git ls-files friday/.DS_Store` izliyor (ilk import commit'i 51952480); kök `.gitignore`'da `.DS_Store` var ama izlenen dosya etkilenmez. `git status`'ta sürekli `M`. | `git rm --cached friday/.DS_Store`. | kesin
4. `sage|vega|deci/.claude/hooks/*.sh` | **tutarsız** | `git ls-files --eol`: sage 3, vega 3, deci 2 hook `i/crlf w/crlf`. tart, gard, span, calc LF. Şablon LF. sage'de CRLF'li hook'u çalıştırdım, exit=2 döndü, yani çalışıyor. | Hepsini LF'ye çevir, `.gitattributes` ile `*.sh text eol=lf` sabitle (şu an `.gitattributes` yok). | kesin
5. `deci/.claude/hooks/okuma-izin-test.sh:26,43,44` (vega, sage, gard aynı) | **tutarsız** | `tart` kopyasından tek fark `tart`→`<ajan>` yol adı. Şablonda test dosyası yok, `claude-ayar/` altında hook dizini da yok. Hook'lar şablona değil doğurucu kodda. | Şablonu tek kaynak yap (hook'lar `claude-ayar/hooks/`), kopyaları üretici yenilesin. | şüpheli (doğurucu Rust'ın kaynağına bakmadım)
6. `tart|gard|span|calc|deci|vega|sage/AGENTS.md:1` | **bozuk** | "üretici `jarvis/tools/alan-ajani-dogur.py`": bu yol yok (`ls jarvis/tools/alan-ajani*` hata). Python gövdesi `arsiv/kod/python/tools/alan-ajani-dogur.py`'de; canlı olan `target/release/alan-ajani-dogur.exe`. | Atfı `target/release/alan-ajani-dogur` (Rust) olarak güncelle. Kanon dosyası, yalnız Salih imzasıyla. | kesin
7. `sablonlar/ajan-iskelet/claude-ayar/settings.json:2` (`_not`) ve 7 ajan `settings.json` `_not` | **bozuk** | Aynı ölü `jarvis/tools/alan-ajani-dogur.py` atfı. | `_not` metnini düzelt (şablon + kopyalar). | kesin
8. `deci/AGENTS.md`, `vega/AGENTS.md` | **bozuk** | Anılan `urun/` dizini yok. | Dizini aç ya da atfı kaldır. | şüpheli (planlanmış dizin olabilir)
9. `tart|gard|span|calc|deci|vega|sage/AGENTS.md`, `friday/AGENTS.md` | **tutarsız** | `arsiv/kapsul-YYYY-MM-DD.md` kalıp atfı gerçek dosya sanılırsa kırık görünür. Ayrıca md kapsül/pano Karar 122'de dondu (`ortak/README.md`), ama §3 hafıza hâlâ kapsülü "birincil" yazıyor. | AGENTS.md §3'ü Karar 122 durumuna göre sadeleştir. | şüpheli
10. `span/cc/giden/2026-10-19-iskelet-gerekli-claude-mods-M1.md` | **tutarsız** | Span, Jarvis'ten M1-M5 ders iskeleti istemiş; `span/cc/gelen/` yalnız `.gitkeep`, 22 gün yanıtsız. Dosya içeriğinde `okuma-izin.sh`'in `plugin-authoring` tip dosyasını engellediği de yazıyor. | Jarvis yanıt versin ya da talebi kapat. | kesin (yanıt dosyasının yokluğu doğrulandı)
11. `vega/cc/gelen/ders-Q1.md`, `deci/cc/gelen/ders-J1.md` | **tutarsız** | İskeletler 09-22'den beri duruyor; `vega/ogrenme/quant/ilerleme.md:5` Q1 "sırada", `deci/core/durum-kapsulu.md:9` J1 "0 ders". Yanıtsız değil, işlenmemiş gelen. | Salih'in seans kararına bırak. | şüpheli (bilinçli bekleme olabilir)
12. `veri/hafiza-ayna/-Users-HasanSalihSahin-sistem/MANIFEST.json` (kök, izlenmeyen) | **gereksiz** | `dosya_sayisi: 0`, `anahtar: C--sistem`. Gerçek hafıza anahtarı `C--sistem-sistem`. `jarvis/veri/hafiza-ayna/` altında izlenen asıl kopya var. Kökten yanlış cwd'yle koşmuş `hafiza-ayna` çıktısı. | Silme yok (m.8): arşive indir ya da `.gitignore`. Üretici kökten koşulmasın. | kesin
13. `.gitignore:` (kök) | **tutarsız** | Eksik: `ortak/oda/` (oda modu çalışma durumu, izlenmeyen), `veri/` (kök, izlenmeyen), `projects/*/.godot/`, `projects/*/test_cikti/`, `projects/*/referans/`. Mevcut kural kümesi yalnız `.obsidian/`, `.DS_Store`, `__pycache__/`, `catboost_info/`, `.venv`, `.lavish`, MIT arşivleri, `/target/`. | Bu 5 kalıbı ekle; aksi halde `git add -A` riskli (zaten deny'de yasak). | kesin
14. `projects/portal-parkur/referans/` (154 MB), `test_cikti/` (11 MB), `.godot/` (28 KB) | **gereksiz** | Proje 10-26'da `C:\sistem\portal-parkur`'a taşındı, bu dizindeki `README.md` kendini "pointer" ilan ediyor, `git ls-files projects` yalnız README. İkisi de izlenmeyen, başka depoya ait ham referans. 165 MB bu klasörde duruyor. | Yeni repoya taşı ya da `.gitignore`; silme Salih kararı. | kesin
15. `sage/veri/bronz/hareket-olay.jsonl`, `vega/...`, `deci/...` | **tutarsız** | tart ve gard'da izleniyor (`git ls-files`), sage/vega/deci'de izlenmiyor (`??`). `calc/veri/`, `span/veri/` için `.gitkeep` izlenmiyor (`??`). Aynı dosya, farklı muamele. | Tek karar: ya hepsi izlenir ya `**/veri/bronz/hareket-olay.jsonl` ignore'a girer. friday'de 118 satır izleniyor, tart'ta 10, gard'da 12. | kesin
16. `sablonlar/ajan-iskelet/claude-ayar/skills/seans-kapanis/SKILL.md:19`, `sablonlar/ajan-iskelet/README.md.tmpl:28`, 7 ajan README + `friday/README.md:31` | **tutarsız** | Denetim komutu `python3 -c "...hareket-olay.jsonl..."`. `python3 --version` = 3.11.5 var (çalışır), ama Rust'a geçiş ilkesiyle (`Cargo.toml:1`) çelişir. | `hareket-tablo.exe` ya da `jq` kullan. | şüpheli
17. `KURULUM.md` (7), `README.md:8-16`, `friday/README.md:7,30`, 7 ajan `README.md:7` | **bozuk** | Mac kalıntısı: `~/sistem`, `/Users/HasanSalihSahin`, `brew`, `Finder`, `python3 tools/katman-hatti.py` (`KURULUM.md:10`; kullanıcı CLAUDE.md "Windows kopyası 2026-09-22 KURULUM.md §3" diyor). | Windows 11 yollarına güncelle ya da başa AS-OF "Mac dönemi" damgası koy. | kesin
18. `friday/README.md:3,13` | **tutarsız** | "Opus 5 medium" derken `friday/AGENTS.md:3` ve kök `README.md:9` "Opus 5.5" (Karar 106). | README'yi Opus 5.5'e getir. | kesin
19. `friday/README.md:30` | **bozuk** | Örnek komut `/Users/HasanSalihSahin/jarvis/...` ve `kanon/tuzuk-v0.md` (`kanon/` emekli). | Komutu güncelle. | kesin
20. `sablonlar/harness/claude-global-CLAUDE.md:9,13` | **tutarsız** | "Finder'da göster", "~/jarvis · ~/friday" Mac yolu; canlı `~/.claude/CLAUDE.md` Windows'a göre "Explorer" diyor. Şablon kopyası canlı sürümle ayrışmış. | Şablonu canlı dosyaya göre yenile. | kesin
21. `.claude/settings.json` (kök, izlenen) vs `.claude/settings.local.json` (40 Mac yolu eşleşmesi) | **tutarsız** | `settings.local.json` kullanıcı git ignore'unda (`C:\Users\sasah/.config/git/ignore` kuralı), depoda izlenmiyor, iyi. İçinde 40 `/Users/...|~/sistem` geçişi var: bayat izin satırları. | Ayıkla (kişisel, kapsam sınırında). | şüpheli
22. `git config remote.no-mistakes.url` | **bozuk** | `/Users/HasanSalihSahin/.no-mistakes/repos/c674481304c5.git`, Windows'ta yok. `portal-parkur` içinden `git remote -v` de bunu gösteriyor. | Remote'u yeniden bağla ya da kaldır. | kesin
23. `ortak/graf/` | **tutarsız** | Yalnız `akis-jarvis`, `akis-sage`, `akis-span`, `akis-tum` var; `akis-tart|gard|calc|deci|vega|friday` yok. `ortak/README.md` "alan başına" üretim der. | Seans açılmayan alanlar için üretimin bilinçli atlandığını README'ye yaz. | şüpheli
24. `ortak/oda/aktif.json`, `ortak/oda/202611101157-...json` | **gereksiz** | Oda modu çalışma durumu, izlenmeyen, repoya ait değil. | `.gitignore` (13 ile birlikte). | kesin
25. `gunluk/.claude/settings.json` | **tutarsız** | `claudeMdExcludes` Windows + Mac biçimli 7 girişi karışık tutuyor (`**/Users/sasah/.claude/CLAUDE.md`). `gunluk/CLAUDE.md` düz dosya, symlink değil (`ls -la`). Ajan olmadığı için kabul edilebilir, ama diğer her dizin symlink. | Not düş, ya da AGENTS.md → symlink yap. | şüpheli
26. `jarvis/raporlar/jarvis/*visual-check*.png` (4 dosya, izlenen) | **gereksiz** | Kapsam dışı (jarvis/) ama izlenen ikili örnek, bilgi olarak. | Jarvis denetim kapsamına bırak. | şüpheli

## Doğrulandı, sorun yok
- 8 `AGENTS.md` (27-31 satır, ≤40 bütçe içinde) ve 8 `CLAUDE.md` symlink'i (`120000`) var; `gunluk/CLAUDE.md` düz dosya.
- `ogren` skill symlink'i 7 alan ajanında `../../../sablonlar/skills/ogren` olarak çözülüyor ve içerik geliyor.
- 8 ajanda `.aktif-devir` yok, bayat değil.
- `friday/cc/gelen/` içindeki 9 devir dosyasının her birinin `friday/cc/giden/` altında eşi var.
- `hareket-kutuk.sh` kopyaları CR'siz karşılaştırmada 7 ajanda aynı (friday hariç).
- `hakem.md` 7 ajanda alan satırı dışında şablonla uyumlu (tart karşılaştırması).
- `bin/hook-dispatch.sh` + `target/release/hook-dispatch.exe` + `alan-ajani-dogur.exe` var; çağrılan ikililer eksik değil.
- İzlenen büyük dosyalar yalnız `jarvis/veri/*` (kapsam dışı); kökte alan ajanı altında `__pycache__`/`.pyc`/`.exe` izlenmiyor.
- Kök `arsiv/kod/python/`: canlı kopyası olmayan arşiv (`bin/hook-dispatch.sh` Rust ikilisine yönlendiriyor). 35 izlenen dosya, 452 KB.
- `ortak/` içinde kullanılmayan dosya bulamadım. Kullanım kanıtı `ortak/README.md`'de var.

## Özet
- **Taranan:** 8 ajan dizininin `.claude/`, `cc/`, `core/`, `kuyruk/`, `veri/`, `ogrenme/` (izlenen sayıma bak), şablon (12 dosya), `ortak/` (13), `gunluk/` (2), `projects/` (1 izlenen + 3 izlenmeyen dizin), `arsiv/` (35), `bin/` (1), kök `veri/` (1), `.gitignore`, `KURULUM.md`, `README.md`. `git ls-files` kontrolü tüm depo (jarvis dahil) üzerinde. Yaklaşık 380 dosya, yalnızca kanıtlı olanlar listelendi.
- **Taranmayan:** `jarvis/`, `ogrenme/`, `target/`, `.git/`, `projects/portal-parkur/.godot` içeriği. `ogrenme/` altındaki izlenmeyen `dosya-mimarisi/` ve `ontolojik-encode/` kapsam dışı. `hook` dosyalarının satır satır mantığına (yalnız fark + çalıştırma) girilmedi; `okuma-izin-test.sh` toplu koşulmadı (bunu `write` riskine karşı atladım). Doğurucu Rust kaynağı okunmadı (bulgu 5 bu yüzden şüpheli).
- **Genel hüküm:** Alan ajanları kendi aralarında tutarlı (hook ve skill kopyaları aynı kaynaktan), ama hepsi bir Mac kalıntısı taşıyor. En ciddi sorun deny kurallarındaki `~/sistem/...` yolları (bulgu 1). İkinci grup: Friday şablondan ayrışmış (bulgu 2), CRLF/LF karışıklığı (bulgu 4), ölü `alan-ajani-dogur.py` atfı (bulgu 6-7). Kök `.gitignore` eksikleri ve izlenmeyen artıklar (13-15, 12) kolay düzeltilir. Yapısal çürüme ya da kayıp dosya yok.

---

## Rapor 5

Denetim bitti. 24 bulgu var (üst sınır 40). Hiçbir dosya değiştirilmedi.

**Engel:** PreToolUse kancası (İB-83) `kuyruk/senaryo-defteri.md` içeren her komutu reddetti. Dosyanın satır sayısı ölçülemedi. Yalnız `ls` ile bayt boyutu görüldü: 118292 bayt.

**Bulgular (önem sırasıyla)**
1. `C:\Users\sasah\.claude\dev-mods\5fcbb2ab-34fa-448c-8233-031f1fab19f3\jarvis-oda\.claude-plugin\plugin.json:3` | tutarsız | Canlı kopyada oda 0.4.1, graf 0.1.0. Kanon kopyada 0.6.0 ve 0.2.0. Canlı kopyada `hooks/src/` ve `tests/` yok. `~/.claude/settings.json:4` `CLAUDE_CODE_PLUGIN_DIRS` ile modları doğrudan repodan yüklüyor. | Canlı kopya ölü. `mods/README.md:3` hâlâ "canlı kopya dev-mods'ta" diyor; metni güncelle. | kesin
2. `dev-mods/` altında 5 uuid dizininden 4'ü boş (`0260f3bb`, `1335bea6`, `8a8635fb`, `d9c9d64f`). Beşincisi (`5fcbb2ab`) eski kopya. | gereksiz | Dizin listesi ve `find` çıktısı. | Boş 4 dizin ve eski kopya arşive taşınsın (silme yasağı m.8). | kesin
3. `veri/erisim-eval.jsonl` (19450053 B), `veri/bronz/baglam-olay.jsonl` (10629936), `veri/anakronizm-denetim.jsonl` (9953526), `veri/katman-olcum.jsonl` (9523655), `veri/bronz/hareket-olay.jsonl` (6497485) | verimsiz | Beşi de git'te izleniyor ve `git status` her biri için `M` gösteriyor (her oturumda değişiyor). `erisim-eval.jsonl` için 15 commit var. | Eklemeli (append-only) olanları aylık parçala, ya da türev olanları `.gitignore`'a al. Karar Salih'in. | şüpheli (pack boyutu yalnız 49 MiB, yani şişme sınırlı)
4. `graf/pointer-sistemi-v0-*.d2/.svg/.json/.txt` | verimsiz | 23 dosya izleniyor; hepsi `tools/pointer-graf.py` çıktısı ve `git status`'ta `M`. `graf/README.md` "aynı silver → aynı çıktı" diyor. `pointer-sistemi-v0-tam.svg` 186254 B, `pointer-graf.py:89` onu "arşiv amaçlı" diye tanımlıyor. | `tam.*` ve `kirik.svg` izlemeden çıkarılsın ya da graf türevleri gitignore'a alınsın. | şüpheli
5. `wiki/adversarial-hayatta-kalma.md:17` | bozuk | `[[rol-katmanlari]]` hedefi yok. `wiki/README.md:58` aynı sayfayı "aday sayfa (07-21 borcu)" diye anıyor. | Sayfayı aç ya da bağlantıyı düz metne çevir. | kesin
6. `wiki/no-mistakes.md:35` | bozuk | `[[treehouse]]` hedefi yok. `wiki/README.md:51` "treehouse kuyrukta kaldı" diyor, 08-04'ten beri açılmamış. | Sayfa aç ya da düz metne çevir. | kesin
7. `wiki/README.md:71` | bozuk | `[[skill-hazinesi-secim-isabeti]]` hedefi yok. Satırda "**kuyruk**" yazıyor, yani kasıtlı olabilir. | Düz metne çevir. | şüpheli
8. `wiki/README.md:11`, `wiki/gnhf.md:30`, `wiki/lavish.md:34`, `wiki/baglam-veri-ambari.md:26` | tutarsız | `[[wiki-link]]` ve `[[link]]` yer tutucu metin; bağlantı denetiminde yalancı kırık olarak çıkıyor. | Backtick içine al. | kesin
9. `mods/jarvis-oda/hooks/register.tsx:1` ve `mods/jarvis-oda/tests/oda.test.tsx:1` | tutarsız | Başlıklar "v0.5", `plugin.json` 0.6.0. Graf modunda kod ve manifest tutarlı (0.2.0). | Başlıkları v0.6 yap. | kesin
10. `mods/ITERASYON-2026-11-03.md:3` | tutarsız | "register.tsx (673 satır) / (268 satır)" yazıyor. Şimdiki sayılar 122 ve 40 satır (`wc -l`). Mantık `hooks/src/`'e taşınmış. | Tarihsel kayıt sayılabilir; yine de "bölünmeden önceki sayı" notu eklenebilir. | şüpheli
11. `mods/jarvis-oda/.claude-plugin/types/` ve `mods/jarvis-graf/.claude-plugin/types/` | gereksiz | `claude-code/index.d.ts` 664209 B ve `claude-code-tools/index.d.ts` 193890 B iki mod dizininde de var (toplam ≈1,7 MB). `.gitignore` içinde `*` olduğu için `git check-ignore` izlenmediğini doğruladı. | Sorun yok; yalnız disk kopyası. İstenirse tek paylaşılan konuma indirilebilir. | kesin
12. `mods/jarvis-oda/hooks/src/ortak.ts` ve `mods/jarvis-graf/hooks/src/ortak.ts` | verimsiz | Dosya başlığı "aynı tutulur (paket yok, kopya)" diyor. İkisi de 2772 B (içerik karşılaştırması yapamadım, diff komutum yol hatası verdi). `metin.ts` iki modda farklı (8126 / 7374 B). | Kopya kayması riski var; paylaşılan paket ya da sürüm kontrolü. | şüpheli
13. `veri/gorunum/v_guncel_anahtar.csv`, `v_okuma_orani.csv`, `v_silver_kuyruk.csv`, `v_silver_kuyruk_ozet.csv`, `v_silver_saglik_son.csv` | gereksiz | `tools/`, `core/`, `wiki/`, `kuyruk/*.md` altında anılmıyor. Üretici `kod/rituel/src/silver_saglik.rs`'te geçiyor (`v_guncel_anahtar` için), diğerlerinin üreticisini bulamadım. | Tüketici var mı bakılsın; yoksa üretimden çıkar. | şüpheli
14. `kuyruk/senaryo-defteri.md` | verimsiz | 118292 B, tek dosya. Satır sayısı ölçülemedi (kanca engeli). | Yıl-ay parçalara böl, ana dosyada indeks bırak. | şüpheli (satır sayısı yok)
15. `kuyruk/masa-gundemi-2026-07-30.md` (72519 B), `build-tartisma-notlari.md` (48153), `okuma-defteri-2026-07-28.md` (40305), `utopik-havuz.md` (37210), `arsiv-fikir-kutusu-2026-07.md` (30335) | verimsiz | Tarihli, eski, büyük dosyalar kuyruk kökünde duruyor. Dosya adındaki `arsiv-` önekleri kuyrukta olduklarını gösteriyor. | `kuyruk/arsiv/` altına taşı (dizin boş duruyor). | şüpheli
16. `kuyruk/arsiv/` | gereksiz | Boş dizin (`ls` çıktısı boş, 0 izlenen dosya) ama dosya yerleşim planı arşivi buraya bekliyor. | Ya doldur ya da kaldır. | kesin
17. `kuyruk/gelen-2026-08-01-*` (3 dosya), `gelen-2026-08-12-*` (3), `gelen-2026-08-15/16/30-*` (3) | verimsiz | 9 `gelen-` dosyası kuyruk kökünde. Kararlara işlendiği doğrulanamadı: defter okunamadı; `core/ wiki/ cc/rapor` içinde yalnız `rapor-2026-08-01-5.md` ve `rapor-2026-08-31-ib68-c-ic-envanter.md` anıyor. | İşlenenleri arşive taşı. | şüpheli
18. `kuyruk/masa-spec-13..18-*.json` (6 dosya, 10962–24324 B) | verimsiz | Eylül'den kalma masa spec çıktıları, kökte duruyor. | Arşive taşı. | şüpheli
19. `lean/Kanon/*.lean` | tutarsız | 34 modülün 9'unun `.lean.md` eşi yok: AjanAdi, AkisGraf, AlanAjani, BaglamSirasi, Butce, Izolasyon, ParalelOturum, Sabitler, SeansAcilis. Kalan 25'in eşi var. | Eşleri yaz ya da eşsiz modüllerin gerekçesini belirt. | kesin
20. `lean/Kanon/Zorlanabilirlik.lean:3` | gereksiz | "Uygulayan kod: yok". Kök ve jarvis `AGENTS.md` bu modülü anmıyor. | Kâğıt üzerinde modül; yaşam durumunu net bırak. | şüpheli
21. `kuyruk/ders-gbm/` | gereksiz | Ders dosyaları dışında `catboost_info/` içinde 15049 dosya var (gitignore'da, yani izlenmiyor). | Üretim çıktısı temizlenebilir. | kesin (izlenmiyor)
22. `wiki/sozluk.md` | tutarsız | `DONDU` (`wiki/README.md:20`); satır 95 başlığı 08-14 Salih talimatıyla eklenmiş (açıkça yazılı). Son commit 2e13dc4c taşıma commit'i, yazım yok. | Tutarlı; dondu sayılıyor ve yazılmıyor. | kesin
23. `veri/` (1,5 G toplam) | verimsiz | İzlenmeyen büyük dosyalar: `baglam.sqlite` 354099200 B, `erisim-vektor.sqlite` 604254208 B, `erisim-vektor-bge.npy` ve `-e5.npy` 221114496 B her biri. `erisim-vektor-*` Eylül 22'den beri değişmemiş. | Hepsi `.gitignore`'da (`jarvis/.gitignore`), çelişki yok. Ölçüm kolu kullanılmıyorsa vektör dosyaları arşive. | şüpheli
24. Lean yapılandırma | tutarlı | `lakefile.toml` (3 `lean_exe`, 2 `lean_lib`), `lean-toolchain` v4.35.0, `lake-manifest.json` `packages: []`. `Kanon.lean` 34 import, `Kanon/*.lean` 34 dosya; içe aktarılmayan ya da dosyası olmayan yok. `sorry`, `axiom`, yoruma alınmış `theorem/lemma` yok. | Sorun yok. | kesin

**Doğrulanan temizler:** `AGENTS.md` ve `jarvis/AGENTS.md`'te anılan 10 yol (`Kanon/AjanAdi`, `AjanYetki`, `CeliskiKapisi`, `Commit`, `DeneyselRakam`, `Izolasyon`, `KararYetkisi`, `ParalelOturum`, `YanOturumSinir` ve `SeansAcilis`/`Butce`/`KararSunum`/`AlanAjani` diske göre) var. `veri/` içinde izlenen sqlite/npy/parquet yok (yalnız iki parquet JSON sözleşmesi). Kuyrukta boş ya da aynı içerikli dosya yok. Wiki'de 25 sayfanın hepsi `README.md` indeksinde.

**Özet**
- Taranan: lean 34 modül + 3 giriş + Gorev + yapılandırma; mods iki mod, 12 `src/` dosyası, 2 README, canlı kopya; graf 23 izlenen dosya; wiki 26 dosya; kuyruk 69 üst düzey + ders-gbm; veri 183 izlenen dosya (yapı ve boyut).
- Taranmayan: senaryo-defteri içeriği (kanca engeli), Lean teoremlerinin doğruluğu (derleme Jarvis'te), jsonl içerikleri, `ders-gbm/ihale_verisi.csv` içeriği (md.49 açısından bakılmadı), `.lake` derleme çıktısı.
- Genel hüküm: Çekirdek sağlam (Lean modülleri tutarlı, kırık yol yok). Asıl sorunlar: ölü canlı mod kopyası ve ona dönük README metni (1, 2), her oturumda değişen izlenen türev dosyalar (3, 4), 3 gerçek kırık wiki bağlantısı (5, 6, 7), eski dosyaların kuyruk kökünde birikmesi (15, 17, 18).

---

## Rapor 6

**Denetim raporu: jarvis/cc, jarvis/raporlar, jarvis/arsiv (salt-okur; 10 Kas 2026)**

Not: alt-ajan okuma kilidi (İB-83) `cc/gelen`, `cc/giden`, `.aktif-devir` ve `cc/devir/**` içeriğini engelledi. (h) bakılamadı. `git ls-files` ile `cc/gelen`, `cc/giden` ve `.aktif-devir` için izlenen dosya yok.

**Bulgular (önem sırasıyla)**

1. `cc/pipeline/pipeline-2026-08-14-ajan-metodolojisi.md:8-12` | tutarsız | Görev tablosu G-1, SH-1 ve T için BEKLİYOR diyor. Satır 16-18 "G-1 + SH-1 DONE… Tüm görevler DONE" diyor. `core/ajan-metodolojisi.md` mevcut. Açılış kapısı "SAHADA" kelimesini ilk 1500 karakterde bulup "açık" sayıyor (`kod/rituel/src/acilis.rs:200` kelimeler SAHADA/AÇIK/KOŞUYOR/YARIM). | Tablo durum sütununu DONE yap. | kesin
2. `cc/pipeline/pipeline-2026-08-14-ingest-semasi.md:8-13,27` | tutarsız | Tablo BEKLİYOR, satır 27 "T — TESLİM… Tüm görevler DONE". `core/ingest-semasi.md` mevcut. Kapı 1 "SAHADA" eşleşmesiyle uyarıyor. | Tablo durumunu DONE yap. | kesin
3. `cc/pipeline/pipeline-2026-08-15-baglam-silver-katmani.md:17,26,27` | tutarsız | T-6, İ-3 ve T-V1 KUYRUKTA kalmış. Satır 38 T-W1 kapandı ve satır 50 SH-10 KISMİ diyor. Dosyada SAHADA/AÇIK/YARIM yok. Kapıdaki tek eşleşme satır 7'de "seans-2 … pipeline'ını koşuyor" (başka hattın durumu) ve yanlış alarm. | Üç satırı DONE, KISMİ ya da iptal yap. Kapıda kelime eşleşmesini durum sütununa daralt. | kesin (yanlış alarm), şüpheli (İ-3'ün gerçekten bitip bitmediği)
4. `cc/pipeline/pipeline-2026-08-22-erisim-fts.md:19-20` | tutarsız | Durum KISMEN-KAPANDI ve "Kalan" listesi var. Kod `tools/erisim-fts.py` mevcut. Kapı yine "SAHADA" ile uyarıyor. Gerçekten kısmen açık. | Kalan işleri ledger'a bağla. Kapı için bir "KISMEN-KAPANDI, kalan ledger'da" damgası ekle. | şüpheli
5. `cc/pipeline/pipeline-2026-08-22-silver-saglik.md:22-24` | tutarsız | KISMEN-KAPANDI, kalan 3 madde İB-42'de. Dosyada `tools/silver-saglik.py` geçiyor ama bu dosya `tools/` altında yok (`git ls-files` yalnız `silver-saglik-kalibrasyon.py` gösteriyor). Rust'a taşındığı için ben öyle okudum, doğrulamadım. | Dosyada Rust karşılığına pointer ekle. | şüpheli
6. `cc/README.md` (tümü) | tutarsız | README düz yerleşimi anlatıyor: `gorev-YYYY-MM-DD-N.md` ve `C:\JARVIS\cc\...`. Gerçek yerleşim `cc/gorev/YYYY-MM/`, `cc/rapor/YYYY-MM/` ve `cc/pipeline/`. `cc/workflow/README.md` da `cc/pipeline-2026-...` ve `cc/gorev-2026-08-..` eski yollarını yazıyor. | README'leri alt dizin yerleşimine göre güncelle. | kesin
7. `raporlar/` kök dizini | tutarsız | `raporlar/README.md` ay klasörü düzenini tarif ediyor. Kökte 38 izlenen dosya var: 22 adet `*-son-50-prompt.md`, 12 adet `2026-10-16/17-*` konu raporu, `2026-10-30-python-arsiv-fark-testi.md`, `gorsel-2026-09-04-word-ram-mekanizma.html`, `hareket-gunlugu-2026-09-09.md`. | Konu raporlarını `raporlar/2026-10/`, görseli `raporlar/gorsel/` altına taşı. | kesin
8. `raporlar/hareket-gunlugu-2026-09-09.md` | tutarsız | `raporlar/hareket/hareket-gunlugu-2026-09-09.md` da var ve içerik farklı (`cmp` char 124). Aynı gün iki günlük, biri yanlış dizinde. | Kök kopyasını `hareket/` altına birleştir ya da yeniden adlandır. | kesin
9. `raporlar/*-son-50-prompt.md` (40 dosya, 413.990 bayt toplam) | verimsiz/tutarsız | 22 dosya kökte, 18 dosya ay klasörlerinde. Aynı veri `veri/gorunum/v_son_50_prompt.csv` içinde de var (içerik eşliğini kontrol etmedim). | Yerleşimi tek yere topla. Üretici betik ayın klasörüne yazsın. | şüpheli
10. `raporlar/2026-09/yol-tasi-kuru-2026-09-18.diff` ve `yol-tasi-uygula-2026-09-18.diff` | gereksiz | sha1 aynı, 59.799 bayt. Başlıkta `/Users/HasanSalihSahin/...` (Mac yolu). Dry-run ve uygula çıktısı birebir aynı. | Birini sil ya da arşive indir. | kesin
11. `arsiv/worktree-kalinti-2026-11-10/sage/degisiklik.patch` ve `span/degisiklik.patch` | bozuk | İkisi de 0 bayt ve izleniyor. | Boş yamaları kaldır, README'ye "yama boş" notu düş. | kesin
12. `arsiv/worktree-kalinti-2026-11-10/omp-rust-p1/degisiklik.patch` | verimsiz | 1.502.865 bayt, kapsamın en büyük izlenen dosyası. | Sıkıştır ya da büyük yama için pointer bırak. | şüpheli
13. `arsiv/README.md` | tutarsız | README şu girdileri listelemiyor: `worktree-kalinti-2026-11-10`, `md-lean-gecis`, `zamanlanmis-gorev`, `memory-arsivi-*` (4 dosya), `kapsul-2026-*` (9 dosya), `ogrenme-oturum-protokolu-v2-2026-09-15.md`, `AGENTS-statik-levha-2026-08-21.md`. | README'ye bu girdileri ekle. | kesin
14. `cc/d2-eval/okuma-1..4.json`, `sql-1,2,3,5.json`, `uretim-1,2,3,5.d2` | gereksiz | Her grupta 4 dosya sha1 aynı. `okuma-5.json` aynı boyutta ama farklı içerik. Tekrar koşumları eval girdisi olarak anlamlıysa bulgu değil. | Aynıysa koşum başına tek kopya ve sayaç tut. | şüpheli
15. `cc/denetci-kalibrasyon/kosum-k1.json`, `k2.json`, `k3.json` | gereksiz | Üçünün sha1'i aynı. `kosum-k1-tur1.json` vb. 98 bayt, tur1 dosyalarıyla aynı boyutta. | Aynı kural: tekrar koşumsa tek kopya. | şüpheli
16. `raporlar/seans/seans-canli-2026-10-26-jarvis-2.json` | tutarsız | 21 json'dan biri tamamen farklı şema (`as_of`, `ne_yapildi`, `salih_karar_bekleyen`). Baskın şemanın 17 anahtarı eksik. | `seans-canli-*` için ayrı şema belgele ya da baskın şemaya göre yeniden üret. | kesin
17. `raporlar/seans/seans-teslim-2026-10-26-portal-parkur-kapanis-graf-karar-124-125.json` | tutarsız | Baskın şemada `kapanis` anahtarı eksik. | Anahtarı ekle ya da şemada isteğe bağlı say. | kesin
18. `raporlar/seans/seans-teslim-2026-11-03-dosya-mimarisi-hazirlik-oda-repo.json` | tutarsız | `hasat` ve `kapanis` anahtarları eksik. | Aynı. | kesin
19. `raporlar/seans/seans-teslim-girdi-*.json` (11 dosya) | tutarsız | `alan`, `etiket`, `olcum`, `oturum`, `sema`, `tarih` yok. Bunlar girdi, `seans-teslim-*.json` çıktı şeması. Aynı dizinde karışık duruyor. | Girdi dosyalarını `seans/girdi/` altına al ya da README'de ayır. | şüpheli
20. `raporlar/seans/` | tutarsız | 65 dosyanın 21'i json, geri kalanı md. Aynı tür belge iki biçimde. Bozuk JSON yok (21/21 ayrıştı). | Biçim kuralını README'de yaz. | kesin
21. `cc/gorev/2026-07/gorev-2026-07-17-1.md`, `2026-07-28-2`, `2026-08/gorev-2026-08-01-21`, `2026-08-02-2`, `2026-08-03-3`, `2026-08-15-7`, `2026-08-21-1` | tutarsız | 7 görev emrinin eşleşen `rapor-*.md` dosyası yok. 08-15-7 ve 08-21-1 pipeline işçi özeti olarak sonuçlanmış olabilir, kontrol etmedim. | Her birine "teslim = ..." pointer'ı ekle. | şüpheli
22. `cc/rapor/2026-07/rapor-2026-07-21-1.md`, `cc/rapor/2026-08/rapor-2026-08-26-3.md` | tutarsız | Eşleşen `gorev-*.md` yok. | Görev emri pointer'ı ekle. | şüpheli
23. `cc/workflow/2026-08-17-agile-m40b-wf_fc0e9f76.js` | gereksiz | Dışarıdan (workflow dizini dışı) referansı yok. Yalnız `cc/workflow/README.md` listeliyor. Diğer 12 script'in en az 1 dış referansı var. | Kullanılmıyorsa arşive indir. | şüpheli
24. `cc/devir/friday-2026-09-09-parti5/devir-2026-09-09-parti5/readme/cc/...` | verimsiz | İç içe aynalanmış dizin ağacı (`readme/cc/gorev/2026-07/README.md`, `readme/raporlar/...`: 9 dosya). Güncel README'lerden farklı blob (taslak önerisi). İçeriğe hook yüzünden bakamadım. | Taslaksa tek dosyaya indir ya da arşivle. | şüpheli
25. `arsiv/karantina/Basliksiz-2026-09-05.canvas` | gereksiz | 2 bayt, başlıksız. | Boşsa arşivden çıkar ya da README'de nedenini yaz. | şüpheli
26. `.claude/skills/pipeline-kosum/evals/evals.json:4`, `tools/testler/test_kolon_katmani.py:2`, `tools/testler/test_tarama_plan.py:2` | tutarsız | Eski düz yolu (`cc/pipeline-2026-...`) gösteriyor. Gerçek yol `cc/pipeline/`. Yalnız yorum ve docstring, kod işlevi kırılmıyor. | Yolları güncelle. | kesin
27. `wiki/baglam-anahtar-kaydi.md:3` ve `.claude/skills/yol-planla/evals/evals.json` | tutarsız | Eski `cc/(rapor|gorev)-2026-...` düz yoluna atıf. | Aynı. | kesin
28. `arsiv/README.md` içindeki kalıp (`arsiv/kapsul-YYYY-MM-DD.md`, `arsiv/tuzuk-madde-arsivi-YYYY-MM-DD.md`) | tutarsız | Bu iki ad ya da şablon `git grep` ile canlı dosyalarda geçiyor ama dosyaları yok (şablon adı, kırık pointer değil). Bilgi amaçlı. | Gerekmez, şablon olduğunu belirt. | şüpheli
29. `raporlar/2026-10-29-sokrates-ajani/` | tutarsız | Ay klasörü yerine tarihli konu klasörü, kökte (13 dosya). Diğer konu raporları `raporlar/2026-10/` altında. | `raporlar/2026-10/` altına taşı. | şüpheli
30. `raporlar/2026-11-01-son-50-prompt.md` vs `raporlar/2026-11-10-son-50-prompt.md` | tutarsız | `2026-11-10-son-50-prompt.md` izlenmiyor (`git status` `??`). Diğer 40 günlük snapshot izleniyor. | Seans kapanışında commit'e al. | kesin
31. `raporlar/hareket/hareket-gunlugu-2026-11-10.md` | tutarsız | `git status` ` M`: değişmiş, commit'lenmemiş. 14:49 satır 35 adımı "hata" olarak kayıtlı, hemen ardından aynı komut "tamam". Kayıt bütünlüğü açısından bilgi. | Seans kapanışında commit'e al. | kesin

**Boyut ve ikili listesi (>1 MB ya da png/pdf/sqlite/zip)**
- `arsiv/worktree-kalinti-2026-11-10/omp-rust-p1/degisiklik.patch`: 1.502.865 bayt
- `raporlar/2026-08/skill-doctor-rapor-2026-08-29.html`: 1.185.342 bayt
- `raporlar/jarvis/jarvis-genel-bakis-archify-2026-08-29.visual-check.{1440x900,2048x1320}.{dark,light}.png`: 4 png (boyutlarını ölçmedim)
- pdf, sqlite, zip, `.DS_Store` izlenen yok.

**Özet**
- Taranan dosya sayısı: cc 510, raporlar 485, arsiv 83 (git ls-files). Hepsi için ad, boyut, sha1 ve boş dosya taraması yapıldı. İçerik okuması örneklemeli: 5 pipeline, 7 gorev başlığı, 21 seans json şeması (tamamı), README'ler.
- Taranmayan: `cc/gelen`, `cc/giden`, `.aktif-devir` ve `cc/devir/**` içeriği (alt-ajan okuma kilidi, (h) bakılamadı). `cc/rapor` ve `cc/gorev` içerikleri tek tek okunmadı. d2-eval, kanit-bulucu, denetci-kalibrasyon yalnız ad ve sha ile baktım. Görev kapsamında olmayan canlı kod referansları yalnız `git grep` ile tarandı.
- Genel hüküm: Bozuk JSON, açık kalmış manifest ya da kritik büyük ikili yok. Sorun yapısal tutarsızlık ve gürültü. Açılış kapısının 5 "açık" uyarısından 2'si (ajan-metodolojisi, ingest-semasi) güncellenmemiş durum alanı, 1'i yanlış alarm (baglam-silver, kelime eşleşmesi), 2'si (erisim-fts, silver-saglik) gerçekten kısmen açık. Kapının kelime eşleşmesi bu yanlış alarmların kaynağı. Kalan işler: README'lerin yerleşimle eşlenmesi, `raporlar/` kökünün toparlanması ve birkaç kopya/boş dosya.

Değiştirilen dosya yok. Jarvis kök dizini: `C:\sistem\sistem\jarvis`.
