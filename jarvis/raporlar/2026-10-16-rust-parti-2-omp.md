# Rust taşıma parti 2: ritüel araçları (durum #3, Karar 113 M7)

AS-OF 2026-10-16. Dal `oturum/2026-10-16-omp-rust2` (başlangıç: `git merge --ff-only main` ile `0b187a8`). Push yok, PR yok.

`[sapma]` Kök `Cargo.lock` da commit'e girdi: `jarvis/kod/rituel` bağımlılıkları (`sha2`, `unicode-normalization`, `jarvis-hook` yol bağımlılığı) 94 satır ekledi; takipli dosya olduğundan işlenmezse `--locked` derleme bozulur. Başka kök dosyaya dokunulmadı (`Cargo.toml`: yalnız `members` listesi).

## 1. Taşınan araçlar

| Python (`jarvis/tools/`) | Rust (`jarvis/kod/rituel/`) | Python satır | Rust satır |
|---|---|---|---|
| `harness_anahtar.py` (lib modülü) | `src/harness_anahtar.rs` (lib; bin yok) | 50 | 71 |
| `acilis-kapilari.py` | `src/acilis.rs` + `src/bin/acilis_kapilari.rs` (bin `acilis-kapilari`) | 183 | 384 |
| `sicak-katman-fifo.py` | `src/fifo.rs` + bin `sicak-katman-fifo` | 129 | 197 |
| `hafiza-ayna.py` | `src/ayna.rs` + bin `hafiza-ayna` | 98 | 188 |
| `kural-sayaci.py` | `src/sayac.rs` + bin `kural-sayaci` | 87 | 153 |
| (ortak) | `src/argparse.rs` (Python 3.11 argparse alt kümesi), `src/py.rs` (Python davranış yardımcıları) | - | 493 + 387 |

Crate `jarvis-rituel` (kök `Cargo.toml` `members` listesine eklendi). `acilis-kapilari` sqlite3 yerine `rusqlite` (`bundled`), hook crate'iyle aynı sürüm (0.32). Python dosyalarına, `.claude/` ve `SKILL.md` dosyalarına dokunulmadı; ritüellerin Rust'a bağlanması yapılmadı (ayrı iş).

`argparse.rs`: önek kısaltması (`--rep`), `--x=değer`, `nargs="*"`, `append`, `type=int` (alt çizgi, işaret, Unicode rakam), `-h` yardım metni (usage sarması, `COLUMNS`), hata iletileri (`unrecognized arguments`, `ambiguous option`, `expected one argument`, `invalid int value`, `ignored explicit argument`). Usage/hata metninde program adı Python'daki gibi `*.py` kalır (bayt eşitliği için bilinçli).

## 2. Fark testi sonucu

Düzen hook parti 1'dekiyle aynı: `tests/ortak/mod.rs` iki ayrı geçici kök kurar (`<kök>/jarvis/...`, kökte `.git`, `<kök>/ev` sahte ev dizini), aynı adımı eski betikle (`python tools/*.py`) ve yeni ikiliyle koşturur; stdout, stderr, çıkış kodu ve yazılan dosyalar (`veri/`; `ts`/`zaman` alanları maskeli) karşılaştırılır. Git sha'ları iki kökte aynıdır (sabit tarihli commit'ler). Dakika sınırında yaş kayması için adım çifti dakika sonunda bekletilir.

**Sonuç: 638/638 durum eşit** (`cargo test -p jarvis-rituel`: 9 test + 1 `anahtar_fark` testi geçti, 87,44 sn).

| Test | Durum |
|---|---|
| argparse (4 araç x 45: bayrak, kısaltma, hata, `--` biçimleri) | 180 |
| yardım genişliği (4 araç x 32: `COLUMNS` 20..200, 0, -5, abc, `1_0`, boş; `-h` ve hata) | 128 |
| `sicak-katman-fifo` (kapsül/pano/MEMORY/AGENTS.md sınırları, NFD başlık, CRLF, Unicode satır sınırları, `--repo` biçimleri) | 52 |
| `hafiza-ayna` (yeni/aynı/değişen/kaynakta-yok, `--kuru`, ek anahtarlar, bozuk/alışılmadık manifest) | 49 |
| `kural-sayaci` (kural birimi işaretleri, `--esik`, `--skill`, `--kutuk`, hook çıktısı, yol biçimleri) | 56 |
| `acilis-kapilari` (commit yaşı/kapsül damgası/saat dilimi 26; transkript+dal+worktree 30; manifest+silver 53; konu/alan/`--repo` 26) | 140 |
| `harness_anahtar` (anahtar türetme 19, dizin durumları 7 x 2) | 33 |
| **Toplam** | **638** |

Bu 638 içinde 21 durumda stderr metni karşılaştırılmaz (`.atla()`); stdout, çıkış kodu ve yazılan dosyalar yine eşit. 18'i Python'da yakalanmamış istisna (traceback) olan durum (aşağıda 3.1), 3'ü `--repo "-a b"` adımının çökmeyen araçlardaki kopyası.

Duyarlılık kontrolü (geçici mutasyon, sonra geri alındı): `kural-sayaci` örnek sınırı 3 yerine 2 ve `sicak-katman-fifo` `madde_basi` sonundaki `:` temizliği kaldırıldığında test kırıldı. İkincisini ilk fixture yakalamamıştı; `Eski:başlık:` ve `...iki nokta:` maddeli iki adım eklendi, ardından yakalandı.

Gerçek veri dumanı (kum değil, bu worktree'nin gerçek `jarvis/` dizini ve gerçek `~/.claude`): 8 koşum (`acilis-kapilari`, `sicak-katman-fifo`, `hafiza-ayna --kuru`, `kural-sayaci --dosya AGENTS.md`; her biri düz ve `--json`), çıkış kodu ve çıktı Python ile eşit (zaman damgası maskeli).

`cargo clippy -p jarvis-rituel --all-targets`: uyarısız.

## 3. Python'dan ayrışan davranış

### 3.1 Python istisnası (traceback) olan durumlar
Python traceback basar ve 1 ile çıkar; Rust aynı çıkış kodu ve stdout ile `[HATA] Python karşılığında yakalanmamış istisna olurdu: ...` yazar (metin taklit edilmez). Durumlar:
- `acilis-kapilari`: `--repo` yok olan dizin; `git log` boş (commit'siz depo) iken düz metin modu (`son5` KeyError; `--json` modu çalışır); satır sınırı karakteri (U+2028) içeren commit konusu; `baglam.sqlite` içinde NULL/metin olmayan `git_head_sha`/`uretim_zamani`; `cc/pipeline/pipeline-*.md` adlı dizin.
- `sicak-katman-fifo`, `kural-sayaci`: UTF-8 olmayan girdi dosyası (`UnicodeDecodeError`); dosya yerine dizin (sicak-katman-fifo).
- `hafiza-ayna`: `MANIFEST.json` kökü liste, `dosyalar` liste değil ya da öğesi nesne değil.
- `kural-sayaci --kutuk`: `veri/` dizini yok.

### 3.2 Bilinçli farklar (davranışsal, testte normalize edilir)
1. **Yeni satır:** Python Windows'ta stdout ve metin dosyalarına `\r\n` yazar; Rust her zaman `\n` (hook crate'indeki aynı karar). Test `\r` siler. Mac'te fark olmaması beklenir `[?]` (bu makinede denenmedi).
2. **Varsayılan jarvis dizini:** Python betik konumuna göredir (`tools/..`); Rust ikilisinin betik konumu yok: `CLAUDE_PROJECT_DIR`, yoksa çalışma dizini (hook crate'iyle aynı kural). `jarvis/` dışından, `CLAUDE_PROJECT_DIR` olmadan koşulursa `harness_anahtar` anahtarları ve varsayılan `--repo` farklı dizine çözülür.
3. **git doğrudan çağrılır** (Python `shell=True`/cmd.exe). Kabuk tırnak/metakarakter yorumu yok. Ek olarak Python, `PYTHONUTF8=1` olmadan git çıktısını yerel kod sayfasıyla çözer (Türkçe commit konusu bozulur); Rust her zaman UTF-8 çözer (düzeltme sayılır; kum testi `PYTHONUTF8=1` ile koşar).
4. **`-h` genişliği:** `COLUMNS` (geçerli ve >0) yoksa 80. Python, `COLUMNS` yokken gerçek terminal genişliğini sorar; etkileşimli terminalde yardım metni sarması farklı olabilir. Boru/dosya çıktısında eşittir (testli).
5. **`textwrap`:** yardım metni sarması yalnız boşlukta kırar; tire üzerinden bölme yok. Mevcut yardım dizelerinde (`KB-50`, `m.29`) tireli bölme tetiklenmez; yeni yardım dizesi eklenirse yeniden doğrulanmalı.
6. **Karakter sınıfları:** Python `str.isspace`/`\s`/`re.I` ile Rust `regex` arasında nadir Unicode kenarları (örn. `re.I` ile `i`/`ı`/`İ` denkliği `kural-sayaci` ve K2 `AÇIK|SAHADA|YARIM|KOŞUYOR` için elle eklendi; NFC için `unicode-normalization` crate'inin Unicode sürümü Python 3.11'inkinden yeni). `int()` için Unicode ondalık rakam tablosu (Nd) elle tutulan listedir; listedeki betikler dışında bir rakam kümesi Rust'ta hata verir.
7. **`glob`/yol:** K2 manifest listeleme `glob.glob` yerine dizin okur; repo yolu `[` gibi glob metakarakteri içerirse Python'un `glob.glob` çağrısı farklı eşleşebilir `[?]` (denenmedi); Rust yolu olduğu gibi okur. Windows'ta dosya adı eşleşmesi büyük/küçük harfe duyarsızdır (Python glob'unda olduğu gibi); `*.jsonl` eşleşmesi de öyle.
8. **Komut satırı:** geçerli UTF-8 olmayan argüman Rust'ta `lossy` çevrilir.
9. **sqlite hata iletisi:** `rusqlite` açılış hatasına ekler `: <uri>`; kırpılır. Denenen üç ileti (`unable to open database file`, `no such table: uretim`, `file is not a database`) Python ile eşit; başka SQLite hata iletileri doğrulanmadı.

## 4. Karşılaşılan sorunlar
1. **Test `teston` ifadesi:** görev metnindeki "jarvis/kod/rituel/teston" `tests/` dizini olarak yorumlandı (hook parti 1 düzeni).
2. **Dakika sınırı kayması:** commit yaşı dakika cinsinden; eski/yeni koşum arasında dakika dönerse çıktı farklı çıkıyordu (paralel koşumda bir kez görüldü). Çözüm: temel commit tarihleri 60'ın katı + adım çifti dakikanın son 5 saniyesinde bekletilir + yaşa bağlı gruplar dakika başına hizalanır.
3. **Python `textwrap` incelikleri:** dar genişlikte (`COLUMNS=10`) uzun sözcük bölünürken satır sonunda boşluk kalıyor (`adı tarihi `); `_wrap_chunks`/`_handle_long_word` birebir taklit edildi.
4. **`int()` Unicode rakam** (`٣`): ilk sürüm yalnız ASCII kabul ediyordu; test yakaladı, tablo eklendi.
5. **rusqlite hata iletisi** sonuna `: file:...` ekliyordu (bkz. 3.2/9); test yakaladı.
6. **Dosya sistemi:** test düzeni `.sil(x).dosya(x)` sırasında önce silmeli; dizin/dosya geçişi `PermissionDenied` veriyordu.
7. **Yazma biçimi:** araçlarla yazılan dosyalar karışık satır sonuyla (CRLF/LF) oluşmuştu; commit öncesi tüm `rituel/` dosyaları LF'ye çevrildi.
8. **Ortam:** komut kabuğu Git-Bash değil; `./target/...` göreli ikili yolu bulunamadı, ad hoc eşitlik denemeleri Python üzerinden yapıldı (kalıcı testlerde etkisi yok).

## 5. Harcanan token ve süre

Kaynak: omp oturum kütüğü (`~/.omp/agent/sessions/--C--sistem-wt-omp-rust2--/2026-10-16T12-40-34-247Z_01a144ba-....jsonl`), görev mesajından (13:10:42Z) son kayıtlı asistan mesajına (13:49:25Z) kadar 72 asistan mesajının `usage` alanları toplamı. Model: `anthropic/claude-sonnet-5-5` (medium).

| Kalem | Değer |
|---|---|
| Girdi (önbelleksiz) | 146 token |
| Çıktı | 193.015 token |
| Önbellek okuma | 13.221.442 token |
| Önbellek yazma | 257.366 token |
| Toplam (kütükteki `totalTokens`) | 13.671.969 token |
| Maliyet (kütükteki `cost.total`) | 4,28 USD |
| Duvar süresi | 38 dk 43 sn |
| Model yanıt süresi toplamı (`duration`) | 1629 sn |

Sayaç bu raporu yazmadan önceki son mesaja kadardır; rapor yazımı, commit ve son yanıt dahil değildir. Duvar süresinin büyük bölümü fark testi koşumlarıdır (tam takım 87,44 sn; acilis grupları dakika hizalaması nedeniyle ayrı ayrı yaklaşık 60 sn).

## 6. Koşum

```
cargo test -p jarvis-rituel                 # 638 durum; Python 3.11 + git + bash PATH'te olmalı
cargo run -p jarvis-rituel --bin kural-sayaci -- --json
```
