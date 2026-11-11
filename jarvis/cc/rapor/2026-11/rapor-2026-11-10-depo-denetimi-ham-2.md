# Depo denetimi 2026-11-10: ham işçi raporları, ikinci tur (12-14: crate iş mantığı ve canlı Python araçları; özet raporlar/2026-11/denetim-depo-2026-11-10.md §5)

---

## Rapor 12

## Rapor: görev #12, rituel crate satır düzeyinde denetimi

Salt-okur çalıştım; dosya değiştirmedim, ikili, hook ya da cargo koşmadım. Bulgular kodu okuyarak çıktı. Zaman etkileri ölçülmedi; her bulgunun sonunda kesin ya da şüpheli diye işaretli.

Kodun dışında üç doğrulama yaptım:
- `veri/baglam.sqlite` dosyasını salt-okur sorguladım (`mode=ro`).
- `git log -1 -- core/ajan-metodolojisi.md` sonucunu karşılaştırdım.
- `tools/`, `../target/release/` ve `graf/` dizinlerini listeledim.

### Bulgular (önem sırasıyla)

1. `baglam_tablo.rs:288` | bozuk | `git log --format=... --name-status -M -c` ne `--relative` ne `-- .` alıyor | `git log` yolları depo kökünden verir (`jarvis/core/x.md`), `git ls-files` ise `jarvis/` altından (`core/x.md`); izler `--relative -- .` eklenmeli | kesin. Kanıt: 1366 dosyanın 311'inde `ilk_commit='-'`; `core/ajan-metodolojisi.md` için son_commit 2026-09-15 yazıyor, gerçeği 2026-10-17. Monorepo sonrası commitler hiç sayılmıyor. Aynı komut tüm monorepo geçmişini tarıyor (1321 commit), yani yavaşlık da yaratıyor.
2. `ambar_tablo.rs:627-731` | verimsiz | `ekle(&con, "INSERT INTO amb_olgu_kosum ...")` çağrılarının önünde `BEGIN` yok | INSERT'ler tek transaction içine alınmalı | kesin. Her satır ayrı commit ve ayrı fsync ediliyor. Diğer modüller (`baglam_tablo` 2266, `hareket` 874, `seyir` 473) transaction kullanıyor.
3. `seyir.rs:369-375` | verimsiz | `(SELECT b2.baglam FROM baglam_olay b2 WHERE b2.oturum_id=b.oturum_id ORDER BY b2.sira LIMIT 1)` | `CREATE INDEX ... ON baglam_olay(oturum_id, sira)` eklenmeli | indeks yokluğu kesin, süre etkisi şüpheli. Grup başına iki iç içe sorgu var ve indeks yok. Görünüm üç kez sorgulanıyor (541, 543, 588).
4. `hareket.rs:410-426`, `seyir.rs:190-204`, `ambar_tablo.rs:354-376` | verimsiz + kopya mantık | `for ad in jsonl_dosyalar(proje_dizin) { ... std::fs::read(&yol)` | Her koşumda tüm transkriptler baştan okunup çözülüyor. `ambar`, yeni koşum süzgecini (587) her ajan transkripti okunduktan sonra uyguluyor. Değişme zamanına (mtime) ya da konum imine dayalı artımlı okuma ve tek ortak tarayıcı gerekli | kesin.
5. `katman_hatti.rs:31-35` | verimsiz | `"tools/pointer-graf.py", ..., "--render", "2"` | `pointer-graf.py:486-488` her .d2 panosunu 2 kez `d2 --layout=elk` ile render ediyor; `graf/` altında 7 adet .d2 var. Bu, her koşumda 14 d2 süreci demek [?]. `--render 2` yalnız ölçüm koşumunda verilmeli | kod kesin, süre şüpheli.
6. `katman_hatti.rs:20-42` | verimsiz | 14 adım hâlâ `tools/*.py` | Her biri ayrı Python yorumlayıcısı açıyor, kendi `git rev-parse`'ını koşuyor ve sqlite'ı yeniden açıyor. `erisim --insa --eval` FTS dizinini her seferinde baştan kuruyor | kesin.
7. `hareket.rs:780`, `ambar_tablo.rs:561`, `anakronizm_denetim.rs:417`, `ayna.rs:148`, `fifo.rs:100` | tutarsız | `unwrap_or_else(harness_anahtar::jarvis)` önce `CLAUDE_PROJECT_DIR`'e bakıyor | `katman-hatti` `current_dir(&repo)` veriyor ama `--repo` geçmiyor; ortam değişkeni farklı bir dizini gösterirse bu adımlar başka repoya yazar. `seyir`, `silver`, `baglam` ise çalışma dizinini kullanıyor. `katman-hatti` her alt adıma `--repo` geçmeli | mekanizma kesin, gerçekleşmesi şüpheli.
8. `baglam_tablo.rs:1993` | bozuk | `std::fs::read(&tam).map_err(...)?` | İzlenen ama çalışma ağacında silinmiş tek bir .md ya da .json bütün `baglam` adımını düşürür, `katman-hatti` da 363'te durur. Bu dosya `notlar` listesine yazılıp atlanmalı | kesin.
9. `acilis.rs:72-80,112-122` | gereksiz/bozuk | `read_to_string(repo.join("core").join("durum-kapsulu.md"))` | Kapsül 2026-10-25'te dondu. Dosya yerindeyse `kapsul_eski` hep true olur ve son 15 dakikadaki her commit `ŞÜPHE` üretir; arşivdeyse dal ölüdür. Dal kaldırılmalı ya da yeni durum kaynağına bağlanmalı | şüpheli: dosyanın yerini okuma kilidi yüzünden göremedim.
10. `fifo.rs:102-104` | gereksiz | `("kapsul", ... "durum-kapsulu.md"), ("pano", ... "pano.md")` | Donmuş dosyalar için FLAG ve arşiv önerisi üretiliyor; bu ikisi listeden çıkarılmalı | kesin.
11. `anakronizm_denetim.rs:471-479` | verimsiz | `OpenOptions::new().append(true)...write_all(dok)` | Her koşum tüm D1/D2/D3 bulgularını yeniden ekliyor; aynı gün içinde aynı `kosum_id` tekrar ediyor ve kütük sınırsız büyüyor. `bayat_cekim.rs:179` bu dosyanın tamamını okuyor. Son koşum ayrı dosyaya yazılmalı, kütüğe yalnız fark eklenmeli | kesin.
12. `silver_saglik.rs:1540-1543` | gereksiz | `tools/anahtar-denetim.py` yoksa `FileNotFoundError` | İşlev Rust'ta yeniden yazılmış; bu betik arşive inerse silver adımı çöker. Bu kontrol kaldırılmalı | kesin.
13. `silver_saglik.rs:1585` | tutarsız | `std::fs::read(... "silver-saglik.py")` | Betik arşivde (doğrulandı), bu yüzden `kod_sha` sabit kalıyor ve `kosum_id` kod değişikliğini yansıtmıyor. Benzeri `baglam_tablo.rs:2356`. Yerine ikili sürümü ya da derleme anındaki git SHA'sı kullanılmalı | kesin.
14. `baglam_tablo.rs:1278-1281` | verimsiz | `Path::new(&py::join(b.repo_kok, &norm)).exists()` | Çözülemeyen her pointer için 2 dosya sistemi `stat` çağrısı yapılıyor; veritabanında 6957 kırık pointer var. `repo_yollar` kümesi yeterli, `stat` kaldırılmalı | kesin.
15. `bayat_cekim.rs:274`, `anakronizm_denetim.rs:428` | bozuk | `py::relpath(&py::abspath(kaydet), &repo)` | Windows'ta `py.rs:297` yolu `SEP='\\'` ile birleştirdiği için `core\x.md` çıkıyor. Silver ve `cekim-olay` ise `core/x.md` ile anahtarlıyor, `tarihli_muaf` de `raporlar/` önekini arıyor; eşleşme kaçıyor. `/` biçimine çevrilmeli | kesin.
16. `silver_saglik.rs:625,1265` | verimsiz | `UPDATE kayit SET gecerlilik=NULL ...` ve ardından iç içe sorgulu tam `UPDATE` | 80.699 satır her koşumda iki kez baştan yazılıyor; tek geçiş yeterli | kesin.
17. `hareket.rs:799,828,864` | verimsiz | bronz dosya iki kez okunup çözülüyor, ayrıca `DELETE FROM hareket` ve tam yeniden INSERT var | Tek okuma ve yalnız yeni satırların eklenmesi yeterli | kesin.
18. `hareket.rs:208-210` | bozuk | `if !p.starts_with('/')` ve büyük-küçük harfe duyarlı `ap.starts_with(&onek)` | `/c/sistem/...` biçimli yollar ve küçük harf sürücü (`c:\`) için `repo_ici=false` çıkar | şüpheli.
19. `seyir.rs:19` ile `hareket.rs:7` | tutarsız | `SATIR_SONU = "\r\n"` (Windows) ile "her zaman LF" yorumu çelişiyor | `seyir` ve `silver_saglik.rs:1236` kütüklere CRLF yazıyor, `hareket`, `ambar` ve `anakronizm` LF yazıyor. Tek kurala indirilmeli | kesin.
20. `ambar_tablo.rs:631` | bozuk | `Some(Value::String(s)) => s.chars().map(...)` | Metin olarak gelen `prompt_id` harf harf ayrı ID'lere bölünüyor (Python hatası olduğu gibi taşınmış). Tek öğeli liste olmalı | kesin.
21. `silver_saglik.rs:505` | bayat | `"2026".to_string()` | `kayit_tarihi` boşsa yıl 2026 varsayılıyor; snapshot yılı kullanılmalı | kesin.
22. `acilis.rs:263,309` | bayat | `katman-hatti (~12 sn, ...)` | Gerçek süre 120 saniyenin üstünde (emirdeki bilgi); metin güncellenmeli | kesin.
23. `silver_saglik.rs:1058` | bayat | `"medyan 234 × 1,5; Karar 83 B1"` | Sabit kodlu kalibrasyon metni kuraldaki `uyari_esigi` değerinden ayrışabilir | kesin.
24. `hareket.rs:53,721`, `ambar_tablo.rs:599`, `seyir.rs:533` | gereksiz | `Üretici tools/hareket-tablo.py` | Üretici betikler arşivde; ikili adı yazılmalı | kesin.
25. `baglam_tablo.rs:1012,1020` | bayat | `["/jarvis/", "c:/jarvis/"]`, `"~/sistem/jarvis/"` | Eski Windows ve Mac yolları. Ters bölülü `C:\sistem\sistem\jarvis\` biçimi `yol_at`'ta zaten yakalanmıyor | kesin.
26. `katman_hatti.rs:173,183` | gereksiz | `.venv/bin/python` önce deneniyor; `python3` dalı var | Mac döneminden kalma; Windows'ta zararsız ölü yol | kesin.
27. `ayna.rs:107-110` | verimsiz | `std::fs::copy(&ky, ...)` SHA değişmemişse bile her dosyada koşuyor | Yalnız `yeni` ya da `degisen` dosyalar kopyalanmalı | kesin.
28. `sayac.rs:105` | şüpheli | `Command::new("bash")` | Windows'ta PATH sırasına göre WSL bash çalışabilir; ayrıca yan etkili `session-start.sh` hook'unu koşturuyor | şüpheli.
29. `anakronizm_denetim.rs:487` | bozuk | `format!("{},{},...", b.dosya, ...)` | CSV alanları tırnaklanmıyor; virgüllü dosya adı satırı kaydırır | kesin.
30. `baglam_tablo.rs:2425` | şüpheli | `std::fs::rename(&tmp_yolu, &db_yolu)` | Windows'ta hedef veritabanı başka bir süreçte açıksa yeniden adlandırma başarısız olur ve bütün adım çöker | şüpheli.

### Okuma kapsamı

- **Satır satır okunanlar:** `katman_hatti.rs`, `py.rs`, `baglam_tablo.rs` (tamamı), `silver_saglik.rs` (tamamı), `hareket.rs`, `ambar_tablo.rs`, `seyir.rs`, `anakronizm_denetim.rs`, `acilis.rs`, `bayat_cekim.rs`, `sayac.rs`, `ayna.rs`, `fifo.rs`, `harness_anahtar.rs`, `lib.rs`. Ek olarak `tools/pointer-graf.py:478-499`.
- **Kısmen okunan:** `argparse.rs` (1-250; Python CLI taklidi, iş mantığı yok).
- **Okunmayanlar:** `argparse.rs` 250-632, `src/bin/*.rs` (her biri 5 satırlık sarmalayıcı), `tests/`.
- **Erişemediklerim:** transkript dizini ve `core/durum-kapsulu.md` / `core/pano.md`; okuma kilidi (İB-83) reddetti. Bu yüzden transkript boyutunu ve kapsülün yerini ölçemedim.

### katman-hatti yavaşlığının en olası 3 nedeni

Ölçülmedi, kod ve veritabanı kanıtına dayanıyor:

1. **Tüm transkriptlerin her koşumda üç kez baştan taranması** (bulgu 4) ve **`ambar`'ın transaction'sız satır satır INSERT'i** (bulgu 2). Windows'ta her commit fsync ve journal dosyası işlemi demek; bu, Windows'la Mac arasındaki farkı da açıklayabilir.
2. **`graf` adımında 14 d2 elk render'ı** (bulgu 5) ve **14 ayrı Python süreci** (bulgu 6).
3. **`baglam` adımının kendisi:** `uretim` tablosunda son koşum `python_surumu='3.11.5'`, `sure_sn=36.55` (2026-11-10 14:56). Yani son silver Python'la üretilmiş ve yalnız bu adım 36,5 sn sürmüş. İkililer 15:15'te yeniden derlenmiş; Rust ikili bulunamazsa `katman_hatti.rs:310` yalnız `baglam` için Python'a düşüyor. Buna `seyir` görünümünde indeks yokluğu ekleniyor (bulgu 3).

### Done ve açık kalanlar

**Done koşulu sağlandı:** crate'in iş mantığı satır düzeyinde okundu, kanıtlı 30 bulgu yukarıda.

**Açık kalanlar:**
- Adım başına gerçek süre ölçülmedi; doğrulamak için `katman-hatti --json` çıktısındaki `sure_s` alanı okunmalı. Bu koşu yan etkili olduğu için yapmadım.
- Bulgu 9'un gerçek etkisi, kapsül dosyasının yeri öğrenilince netleşir.
- Bulgu 1 düzeltilirse `dosya.ilk_commit/son_commit` değerleri ve T-B-YETIM yaş hesabı değişir; silver-sağlık kuyruğu kayabilir.

---

## Rapor 13

[sapma yok] Okuma tamamlandı. 30 bulgu önem sırasıyla aşağıda. Hiçbir dosyayı değiştirmedim. `durum` ikilisini yalnız yardım için koştum (`durum.exe --help` ve argümansız). `baglam.exe denetle` salt-okur olduğu için bulgu 3'ü yeniden üretmek amacıyla koştum. cargo ve hook koşmadım, git durumuna dokunmadım.

**Bulgular**

1. `jarvis/kod/durum/src/main.rs:311,382` | bozuk | `yukle(&yol)?` … `ekle(&yol, &yeni)?` (kilit yok, okuma ile append arası açık) | İki oturum aynı anda `ac` koşarsa ikisi de aynı id'yi yazar. Sonraki her `katla` "id en az N+1" hatası verir, kütük bütünüyle okunamaz olur. Çözüm: `ac` çevresinde dosya kilidi (fs2/`LockFileEx`) ya da yazımdan önce yeniden oku ve doğrula | kesin
2. `jarvis/kod/durum/src/lib.rs:268,363` | bozuk | `d.uygula(o, "0000-00-00")?` ve `o.id < self.sonraki_id()` | Tek bir geçersiz satır, örneğin worktree birleşmesinde id sırası tersine düşmüş bir satır, tüm alt komutları çıkış 1'e kilitler. Çözüm: katlarken id'ye göre sırala ya da bozuk satırı uyarıyla atla | kesin (birleşme senaryosu çıkarım)
3. `jarvis/kod/baglam/src/lib.rs:80` | bozuk | `Component::ParentDir => { sade.pop(); }` boş yolda etkisiz | Göreli `..` sessizce düşüyor. Yeniden üretim: `jarvis` dizininde `baglam denetle ../AGENTS.md` çıktısı `AGENTS.md` (yani `jarvis/AGENTS.md`). Mutlak yolla aynı komut doğru dosyayı veriyor. Çözüm: çözmeden önce `std::path::absolute` uygula | kesin
4. `jarvis/kod/arac/src/masa.rs:286` | bozuk | `yol_ekle(... expanduser("~")), "sistem"), "jarvis")` | Windows'ta `C:\Users\sasah\sistem\jarvis` var olmayan bir yol. SKILL.md `--repo` vermeden çağırıyor, bu yüzden HTML repo dışına yazılır ve dizinleri `create_dir_all` kurar. Şablon ise `kok_coz()` ile bulunuyor, tutarsız. Çözüm: varsayılanı `kok_coz()/jarvis` yap | kesin
5. `jarvis/kod/arac/src/buyuk_harf.rs:477` | bozuk | `format!("{ev}{}sistem{}jarvis", ...)` | Aynı bayat Mac varsayılanı. `--repo` verilmezse repo dosyaları atlanır, `--uygula` yalnız `~/.claude/CLAUDE.md` ile hafıza dosyalarını yeniden yazar. Çözüm: `harness_anahtar::jarvis()` ya da `kok_coz` | kesin
6. `jarvis/kod/arac/src/buyuk_harf.rs:440` | bozuk | `let og = repo.join("ogrenme");` | `jarvis/ogrenme` yok, gerçek dizin `C:\sistem\sistem\ogrenme` (ls ile doğrulandı). `--katman ogrenme` hep boş kalır. Çözüm: yolu düzelt ya da katmanı kaldır (`ogrenme/` ajanlara kapalı) | kesin
7. `jarvis/kod/durum/src/main.rs:463-465` | bozuk | `unwrap_or_else(|| "seans".into())` ve `seans-teslim-{tarih}-{etiket}.json` | Aynı gün `--etiket`siz ikinci kapanış birincinin teslim kaydının üstüne yazar. Çözüm: dosya varsa sıra eki ekle ya da oturum adını dosya adına kat | kesin
8. `jarvis/kod/durum/src/main.rs:480,486` | bozuk | `dosya_yaz(...kayit_rel...)` çağrısı `defter.uygula(&o)` öncesinde | Zaten kapanmış seansta komut reddedilir ama teslim dosyası önce ezilmiş olur. Çözüm: önce `uygula`, sonra yaz | kesin
9. `jarvis/kod/durum/src/main.rs:449,462` | tutarsız | `let alan = a.alan()?;` ile `seans.alan` karşılaştırılmıyor | Başka alanın seansı yanlış `{alan}/raporlar/seans/` altına kaydedilir. Çözüm: `seans.alan != alan` ise kullanım hatası ver | kesin
10. `jarvis/kod/durum/src/main.rs:118` | bozuk | `std::fs::write(yol, icerik)` | `akis-graf.json` ve `SALIH-OZET.md` yaz-yeniden-adlandır kullanmadan, yerinde yazılıyor. Eşzamanlı kapanışta ya da yarıda kesilmede dosya kırpık kalır. Çözüm: geçici dosyaya yaz, sonra `rename` | kesin
11. `jarvis/kod/durum/src/lib.rs:182` ve `main.rs:336` | bozuk | `s.as_str() < tarih_kismi(bugun)` ile `a.al("son-gecerlilik").map(String::from)` | Tarih biçimi doğrulanmıyor. `11/12/2026` gibi bir değer sözlük sırasıyla hemen bayat sayılır. Çözüm: `YYYY-MM-DD` denetimi ekle | kesin
12. `jarvis/kod/durum/src/lib.rs:498-505` | bozuk | `KONUM {alan}: seans … hedef: {h}` bayt tavanına bakmadan basılıyor | Uzun seans hedefi brifi 2048 bayt sınırının (`OTURUM_BASI_BAYT`) üstüne çıkarır. "Açık iş yok" dalında da tavan denetimi yok. Çözüm: hedefi `kisalt` ile kırp | kesin
13. `jarvis/kod/durum/src/main.rs:35` | bozuk | `v.ends_with(".json")` | `graf --json C:\x\graf` (uzantısız yol) konumsal sayılır ve varsayılan `ortak/akis-graf.json` ezilir. 2026-10-26 arızası yalnız `.json` uzantısı için kapanmış. Çözüm: `--json`u komuta göre ayrıştır | kesin
14. `jarvis/kod/durum/src/main.rs:224` | tutarsız | `if let Some(se) = seanslar.last()` | Özet son açılan seansı konum gösteriyor, `oturum-basi` ise `konum()` ile açık seansı öne alıyor. İki yüzey farklı konum söyleyebilir. Çözüm: `defter.konum(alan)` kullan | kesin
15. `jarvis/kod/durum/src/main.rs:308-310` ve `lib.rs:494` | tutarsız | `ts` UTC (`simdi_iso`), `bugun` yerel (`yerel_tarih`) | Yerel 00:00-03:00 arasında "kapandı" tarihi UTC ile önceki günü, teslim dosya adı yerel günü gösterir. Çözüm: ts'i yerel ofsetle yaz ya da gösterimde çevir | kesin
16. `jarvis/kod/durum/src/main.rs:311,123,488` | verimsiz | Her çağrıda `yukle` bütün kütüğü katlıyor. `ac` ayrıca `git worktree list` süreci başlatıp her worktree kütüğünü parse ediyor. `seans-kapat` bütün D2 dosyalarını ve JSON'u yeniden yazıyor | Çözüm: önbellek ya da artımlı katlama, yalnız değişen alanı yaz | kesin
17. `jarvis/kod/durum/src/main.rs:36-40` | tutarsız | `durum --help` çıktısı "durum: --help değer ister", çıkış 2 | Yardım bayrağı yok, kullanım metni yalnız hata yolunda basılıyor. Yardımdaki 11 komut koddaki 11 dalla uyuşuyor; belgelenmemiş ya da çalışmayan alt komut yok. Çözüm: `-h/--help` → kullanım metni, çıkış 0 | kesin
18. `jarvis/kod/arac/src/devir_md2json.rs:702,711` | bozuk | `ebeveyn_birlestir(&yol, &format!("{devir_id}.json"))` | md'den gelen `DEVİR_ID` (örneğin `../x`) süzülmeden dosya adına giriyor ve emir dizini dışına yazabiliyor. Çözüm: ad karakterlerini süz | kesin
19. `jarvis/kod/arac/src/devir_md2json.rs:355` | tutarsız | `yol.starts_with(kalip.trim_end_matches('*'))` | Önek ayraçsız: `cc/gelen` izni `cc/gelen-baska/` yolunu da geçiriyor. Windows'ta `fnmatch` harf duyarsız, `starts_with` duyarlı. Çözüm: ayraçla sınırla, harfi normalize et | kesin
20. `jarvis/kod/arac/src/kod_orani.rs:84` ve `:22,39` | tutarsız | `".py" \| ".sh" \| ".sql" => "kod"` | Rust ve Lean dosyaları (`.rs`, `.lean`) "diger" kovasına düşüyor, kod oranı göçten sonra anlamsız. Yardım metninde `~/sistem/jarvis` ve `python3 tools/...` geçiyor (bayat). Çözüm: `.rs`/`.lean`/`.toml` ekle, metni güncelle | kesin
21. `jarvis/kod/arac/src/kod_orani.rs:258` | gereksiz | `fn tarih_ayristir` | `jarvis_rituel::py::iso_tarih` ile aynı işi yapan kopya; crate o modülü zaten içe alıyor. Çözüm: `py::iso_tarih` kullan | kesin
22. `jarvis/kod/arac/src/yol_tasi.rs:18-29,171` | gereksiz | `"-Users-HasanSalihSahin-jarvis"`, `format!("{home}/jarvis")`, `"raporlar", "2026-09"` | Tek seferlik Mac göç aracı, iş bitmiş (SCRIPTLER.md:90 "tek seferlik"). Windows'ta `home` ters bölüyle geldiği için çiftler hiç eşleşmez. Çözüm: arşive indir (Salih kararı) | kesin
23. `jarvis/kod/kural/src/skill_esik.rs:116` | tutarsız | `OpenFlags::SQLITE_OPEN_READ_WRITE` | Yalnız SELECT yapılıyor ama DB yazma kipinde açılıyor, yazan süreçle kilit çakışması riski var. Çözüm: `SQLITE_OPEN_READ_ONLY` | kesin
24. `jarvis/kod/kural/src/argparse.rs:2` ve `py.rs:1` | tutarsız | Belge "`nargs="*"`, `append`" ve "zaman aşımlı alt süreç" diyor | kural kopyasında bunların hiçbiri yok (yalnız rituel kopyasında var). Çözüm: belge satırlarını düzelt | kesin
25. `jarvis/kod/kural/src/py.rs:341` ve `rituel/src/py.rs:474` | tutarsız | kural `float_repr` eşit uzaklıkta yuvarlamayı düzeltmiyor, rituel düzeltiyor | Aynı adlı işlev iki crate'te farklı metin üretebilir, `skill_esik` çıktısı etkilenir. Çözüm: tek kopyada birleştir | kesin (kod düzeyinde), tetikleyen girdi şüpheli
26. `jarvis/kod/kural/src/lib.rs:4-5` ve `argparse.rs:8-12` | gereksiz | "PR #7 birleşince ortak crate'e taşınabilir" | arac crate zaten `jarvis_rituel::{py,argparse}` kullanıyor, yani ortak kullanım çalışıyor. Engeller ve davranış farkları aşağıda (f) bölümünde. Çözüm: kural'ı `jarvis_rituel`'e bağla, kopyaları kaldır | kesin
27. `jarvis/kod/kural/src/paralel.rs:81-174` ve `arac/src/devir_md2json.rs:151-315` | gereksiz | iki ayrı `fnmatch.translate` uygulaması (biri regex, biri token tabanlı) | Çözüm: tek ortak uygulama | kesin
28. `jarvis/kod/kural/src/paralel.rs:547-551` | tutarsız | `Command::new("git")...output()` çıkış durumuna bakılmıyor, zaman aşımı yok | Repo değilse `"?"` yerine boş metin döner; rituel'deki `calistir_zamanli` kullanılmıyor. Çözüm: durum denetimi ekle, `calistir_zamanli` kullan | kesin
29. `jarvis/kod/kural/src/ad_esitligi.rs:117` | gereksiz | `jp(&["tools", "ad-esitligi-denetim.py"])` | Dosya arşive taşınmış (`ls tools/` ile doğrulandı), dışlama artık ölü. K2 taraması ayrıca `veri/` ve `arsiv/` altındaki her uygun dosyayı tümüyle okuyor (verimsiz, büyüklük ölçülmedi). Çözüm: satırı kaldır, `arsiv`/`veri` dizinlerini atla | kesin (ölü dışlama), şüpheli (maliyet)
30. `jarvis/kod/kural/src/py.rs:43,47` | gereksiz | `pub fn lstrip_kume`, `pub fn rstrip_kume` | kural crate'inde (src ve tests) çağıran yok, grep ile doğrulandı. Çözüm: kaldır ya da ortak crate'e bırak | kesin

**(f) kural ile rituel kopyaları arasındaki davranış farkları**
- `argparse`: ondalık değer tipi (`Tip::Ondalik`) yalnız kural'da var; `skill_esik --carpan/--saat` buna bağlı. `nargs="*"`, `append`, `choices`, konumsal argüman ve karşılıklı dışlayan grup yalnız rituel'de var. `Secenek` yapısı uyumsuz: kural'da `tip: Tip`, rituel'de `tamsayi: bool`.
- `py.rs`: `float`, `katla`, `katlanmis_ara`, `utf8_hata_iletisi` yalnız kural'da. `calistir_zamanli`, `sh`, `Sha1`, `iso_tarih`, `oku_yoksay`, `saga_hizala` yalnız rituel'de. `float_repr` iki kopyada farklı yuvarlıyor (bulgu 25).
- `harness_anahtar`: `proje_dizin` ve `ozet` yalnız rituel'de; ortak işlevler bayt düzeyinde aynı.
- Ortak crate'e taşımanın engeli yalnız API birleştirme işi: `Tip::Ondalik` ve kural'a özgü dört işlevi rituel'e eklemek. Fark testleri (`kural/tests/ortak/mod.rs`) arşivdeki Python betiklerine düşebildiği için taşıma onları bozmaz. Tek risk `float_repr` farkının `skill_esik` çıktısını değiştirmesi.

**Done:** sağlandı. Dört crate satır düzeyinde okundu, 30 kanıtlı bulgu var.

**Satır satır okunan dosyalar** (hepsi `C:\sistem\sistem\jarvis\kod\` altında):
- `durum\src\lib.rs`, `durum\src\main.rs`
- `kural\src\{paralel,argparse,py,pyjson,harness_anahtar,ad_esitligi,skill_esik,lib}.rs`
- `arac\src\{devir_md2json,buyuk_harf,kod_orani,masa,yol_tasi}.rs`
- `baglam\src\lib.rs`, `baglam\src\bin\baglam.rs`
- `rituel\src\{py,argparse,harness_anahtar}.rs`: yalnız kural kopyasıyla `diff` farkları okundu.

**Okunmayanlar:**
- `durum\tests\cli.rs`
- `kural\src\{tetik,derece}.rs` (kapsam listesinde yoktu), `kural\tests\*` (yalnız `ortak/mod.rs` için grep yapıldı)
- `kural\src\bin\*`, `arac\src\bin\*` (5 satırlık sarmalayıcılar)
- `arac\src\alan_ajani.rs` (emir gereği; yalnız `kok_coz` tanımına bakıldı), `arac\src\difflib.rs`, `arac\Cargo.toml`
- `rituel\src\argparse.rs` farkının ilk 200 satırdan sonrası

**Açık kalan:** Bulgu 1, 2 ve 10'daki eşzamanlılık sorunlarını kodu okuyarak çıkardım, iki oturumu aynı anda koşarak denemedim (yazan komut koşmak yasaktı). Bulgu 22'deki arşive indirme kararı Salih'in. Öneri aracıyla öneri bırakmadım.

---

## Rapor 14

## Bulgular (önem sırasıyla, 24 satır)

Hiçbir betik koşturulmadı; dosyalar değişmedi. İki yerde alt-ajan okuma kilidi devreye girdi (kapsül/pano, transkript dizini); bu yollara dokunulmadı.

1. `loop-dedektor.py:154-158` | verimsiz | `for k in kayit: for ug,ukw in uzun: ... any(ug[i:i+len(g)]==g` | `kapsanan` hesabını `k_W` kovasına göre grupla; kayıtları uzunluğa göre sırala; n-gram'ları küme olarak tut | şüpheli (ölçülmedi)
   - Mantık: tüm n-gram'lar × tüm ADAY'lar iç içe döngü, ek olarak alt-dizi taraması.
   - 90 günlük `hareket` n=2..5 ile büyüyor, bu yüzden `katman-hatti` yavaşlığının baş adayı.
2. `prompt-tablo.py:61-80` | verimsiz | `for e in rows[i+1:]:` | önce tek geçişte "sonraki asistan modeli/skill" dizisi çıkar; `rows[i+1:]` kopyasını kaldır | kesin
   - Her prompt için liste kopyası ve ileri tarama var.
   - Bronz append-only olduğu halde (`:100-108`) bütün transkript JSONL'leri her koşumda baştan okunuyor.
   - Önbellek yok (uuid/mtime ile atlama yapılmıyor).
3. `kolon-olcum.py:257,244-250` | verimsiz | `duckdb=None` iken `r = sqlite_olc(db, sablon...` yine koşar | duckdb yoksa `ambar-parquet.py` gibi en başta çıkış 4 ver | kesin
   - Bu makinede `duckdb` kurulu değil (`ModuleNotFoundError`). Çıktı yalnız 12 `ATLANDI` satırı + sqlite sayacı.
   - Q1-Q6 sqlite'ta 3'er tam tarama yapıyor. Q6 `avg(length(metin))` 354 MB `kayit` tablosunu okuyor. Her sorgu için ayrıca `dbstat` sayımı var.
4. `katman_hatti.rs:34` + `pointer-graf.py:486-488` | verimsiz | `"--render", "2"` → `subprocess.run(["d2","--layout=elk",...` | hatta `--render 1`; sha eşitliği ölçümü ayrı koşuma | kesin
   - 4 pano + kırık panosu = 5 d2/ELK süreci × 2 = 10 render; yalnız determinizm ölçmek için.
   - `.d2` içeriği değişmediyse render atlanabilir.
5. `tarama-plan.py:133-136` | verimsiz | `shutil.copyfile(db, kopya)` + `kon2.execute("ANALYZE")` | analiz-kopya'yı kaldır, ya da yalnız şema/`stat1` değişince koş | kesin
   - Her koşumda 354 MB DB kopyalanıp ANALYZE ediliyor.
   - `katman-hatti.py:56` yorumu "~1 sn" diyor, bu yanlış. `hijyen` (`katman-hatti.py:156`, Rust'ta da var) aynı DB'ye ikinci ANALYZE yapıyor.
6. `erisim-fts.py:76-82` | verimsiz | `DROP TABLE IF EXISTS kayit_fts; ... INSERT INTO kayit_fts(kayit_fts) VALUES('optimize')` | `content='kayit'` harici-içerik FTS5 ya da `uretim.git_head_sha` değişmediyse atla | şüpheli (ölçülmedi)
   - FTS tam yeniden kurulum: `metin` kopyalanıyor, sonra `optimize`.
   - `:71,:74` satır başına ilişkili alt-sorgu var (`GROUP_CONCAT DISTINCT`, `COUNT`).
7. `bag-tablo.py:75-89` | verimsiz | `SELECT ... k.metin ... .fetchall()` ardından satır başı `SELECT kayit_id FROM kayit WHERE ...` | `hedef_yol` için indeks ya da tek JOIN; `metin` yerine regex'i SQL'e al | şüpheli
   - `kayit.metin` tamamı belleğe alınıyor, her satırda ikinci sorgu çalışıyor.
   - `hedef_yol LIKE 'arsiv/kuyruk-arsiv/%'` yüklemi indekssiz.
8. `katman-hatti.py:35-39,191` | bozuk+gereksiz | `"tools/ambar-tablo.py"`, `"tools/hareket-tablo.py"`, `"tools/baglam-seyir.py"`, `"tools/silver-saglik.py"`, `"tools/anakronizm-denetim.py"` | betiği `arsiv/kod/python/tools/` altına taşı; kanon Rust `katman_hatti.rs` | kesin
   - Bu 5 betik artık `tools/` altında yok; `katman-hatti.py` koşarsa adımlar `KOD 2` ile düşer.
   - Rust aynı hattı taşımış (`katman_hatti.rs:1`).
9. `katman-hatti.py:125`, `ambar-parquet.py:150`, `tarama-plan-duckdb.py:100` | bozuk (Windows) | `os.path.join(repo, ".venv", "bin", "python")` | Windows'ta `.venv\Scripts\python.exe`; mesajlarda `.venv/bin/pip` | kesin
   - `.venv` zaten yok. duckdb kurulmadıkça 3 parquet adımı sonsuza dek `ATLANDI`.
   - `veri/parquet/*.parquet` 2026-09-22 (Mac) tarihli, bayat.
10. `wiki-baglanti.py:70-76` | bozuk (Windows) | `sqlite3.connect("file:%s?mode=ro" % db, uri=True)` + `except sqlite3.Error: pass` | `urllib.request.pathname2url` kullan (`tarama-plan.py:119` gibi) | şüpheli
    - Windows yolu `C:\...` (ters eğik çizgi) URI'ye düz basılıyor.
    - Hata yutuluyor, `yetim_pointer_kazanan` sessizce hep 0 kalabilir.
11. `sunum-proof-of-work.py:29,65` | bozuk | `sh("git log --reverse ... | head -1", R)` ve `glob(expanduser("/private/tmp/claude-501/-Users-HasanSalihSahin-sistem-jarvis/*/tasks/*.output"))` | `git rev-list --max-parents=0` + Python içinde ilk öğe; Mac glob'unu kaldır | kesin (`:65`) / şüpheli (`:29`)
    - `shell=True` Windows'ta cmd.exe; `head` PATH'te yoksa `ilk=""` olur ve `date.fromisoformat("")` çöker.
    - `:65` Mac yolu Windows'ta hiç eşleşmez; `workflow` ölçümü hep "ölçüm dosyası yok".
12. `anahtar-denetim.py:34-40` | tutarsız | `spec.loader.exec_module(m); return m.katman_bul` (`baglam-tablo.py`) | katman tanımını tek yere al; `baglam-tablo.py`'yi test-oracle olarak sabitle | şüpheli
    - "Tek tanım" iddiası Python yedeğine bağlı; gerçek silver üreticisi Rust `baglam-tablo.exe`, ikisi ayrışabilir.
    - `baglam-tablo.py` arşive inerse `except Exception: return None` ile stale `_katman_yerel`'e (`:18-31`) düşer. `anahtar-cascade.py:8` aynı modülü yüklüyor.
13. `baglam-skill-aday.py:18-22,38-42` | tutarsız | `SICAK = {"CLAUDE.md","core/durum-kapsulu.md","core/pano.md",...}` ve `"ogrenme/README.md"` | `SICAK` tanımını `durum oturum-basi` çıktısına bağla; `ogrenme/` satırını sil; `--repo` ekle | kesin
    - Kapsül/pano 10-25'te dondu; "sıcak" tanımı eski.
    - `jarvis/ogrenme/` yok (`ogrenme/` bir üst dizinde ve ajanlara kapalı); dal sessizce atlanıyor.
    - Yollar `cwd`'ye göreli (`Path("core")`, `connect("veri/baglam.sqlite")`); `except Exception` hatayı yutuyor.
14. `buyuk-harf-temizle.py:134-143` | gereksiz+tutarsız | `repo / "ogrenme" / "README.md"` ... `sorted((repo / "ogrenme").glob("*/dersler/*.md"))` | Rust `buyuk-harf-temizle.exe` kanon; Python'u arşive indir | şüpheli
    - Aynı işi Rust ikilisi (`kod/arac/src/bin/buyuk_harf_temizle.rs`) yapıyor.
    - `jarvis/ogrenme/` yok, `ogrenme` kümesi ölü dal.
    - `:150` koşulu `p.exists() and p.name != "SKILL.md" or (p.exists() and p.name == "SKILL.md")` özünde `p.exists()`.
15. `obsidian-harita.py:83-88` | tutarsız/bozuk | `repo_kok = os.getcwd()`; `con = sqlite3.connect(a.db)`; `FROM uretim LIMIT 1` | `--repo` ekle; bağlanmadan önce var olma kontrolü; `ORDER BY uretim_zamani DESC` | kesin
    - Yanlış `cwd`'de boş bir `veri/baglam.sqlite` yaratır.
    - `uretim` sorgusu `ORDER BY`'sız; diğer betikler `ORDER BY uretim_zamani DESC` kullanıyor, damga stale olabilir.
16. `pointer-graf.py:190` | tutarsız | `subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])` | `cwd=repo` ekle | kesin
    - Diğer betikler `cwd=repo` veriyor; burada süreç `cwd`'sine bağlı.
17. `pointer-graf.py:525-584` | bozuk | `f"... WHERE borc_id='{x}'"`, `LIKE '%{x}'` | parametreli sorgu | kesin (düşük etki)
    - `--odak` değerindeki `'` sorguyu kırar; parametre yerine f-string interpolasyonu kullanılıyor.
18. `erisim-fts.py:244`, `deneyim-tablo.py:42`, `wiki-baglanti.py:24` | tutarsız | `ap.add_argument("--repo", default=os.getcwd())` | `dirname(dirname(abspath(__file__)))` | kesin
    - Öbür betikler betiğin üst dizinini varsayılan alıyor; bunlar `cwd`'yi.
19. `yuzey-parmak-izi.py:46,28` | tutarsız | `not os.getcwd().startswith(env.get("HOME", "/"))`; `env.get("__CFBundleIdentifier")` | Windows'ta yol karşılaştırmasını `os.path.normcase`/`expanduser("~")` ile yap; Mac anahtarlarını at | şüpheli
    - `cwd` `C:\...`, `HOME` Git Bash'te `/c/Users/...` ya da yok → `mount_ipucu` hep `True`.
    - `__CFBundleIdentifier` Mac'e özgü.
20. `katman-olcum.py:184-187`, `erisim-fts.py:290-292` | verimsiz | `with open(tp...) for line in fh: rows.append(json.loads(line))` | yalnız son koşum satırlarını oku (dosya sonundan) ya da döndürmeli (rotating) kütük | şüpheli
    - `tarama-plan.jsonl` (2,5 MB) her koşumda baştan okunuyor.
    - `erisim-eval.jsonl` (19 MB), `katman-olcum.jsonl` (9,5 MB) sınırsız büyüyor.
21. `devir-ani.py:112-116` | bozuk | `except Exception: continue` ... `except Exception: pass` | okuma hatasında dur ya da uyar | şüpheli
    - Mevcut anahtar kümesi okunamazsa boş sayılır, aynı satırlar kütüğe tekrar eklenir.
22. `anahtar-cascade.py:44-48` | bozuk | `except Exception: pass` (`git ls-files` başarısız) | hatayı bildir | kesin
    - `git ls-files` düşerse yalnız `.md` taraması sessizce sürer; kapsam `.py/.sh/.json/.html` kayıp.
23. Eski adı gösteren mesajlar | tutarsız | `loop-dedektor.py:113` ("tools/hareket-tablo.py"), `deneyim-tablo.py:55` ("ambar-tablo.py"), `bag-tablo.py:135` ("baglam-tablo.py"), `ambar-parquet.py:133` ("tools/katman-hatti.py") | mesajları `target/release/<ad>` ya da Rust komutuna çevir | kesin
    - Hata mesajları arşive inmiş ya da Rust'a geçmiş betikleri işaret ediyor.
24. `tarama-plan.py:30`, `tarama-plan-duckdb.py:22-25` | tutarsız (düşük) | `("core/durum-kapsulu.md", 12, 12)` | donmuş olmayan bir sondaj dosyası seç | şüpheli
    - Kapsül dondu; sondaj anahtarı donmuş dosyaya bağlı. Plan sınıfı veriye bağlı değil, yani etki yok; yalnız bayat bağ.

**Taşıma/oracle notu (bulgu değil):** `prompt-dosya.py`, `paket-yonlendir.py`, `baglam_oku.py` Rust hook testlerinde eski taraf olarak koşuyor (`kod/hook/tests/ortak/mod.rs:84,183`). Bu yüzden gereksiz sayılmadı. `prompt-dosya.py:169` `sys.stdin.read()` varsayılan kodlamayla okuyor (Windows cp1254), `paket-yonlendir.py:331` ise UTF-8 çözüyor: tutarsız, ama yalnız test oracle'ı olarak koşuyor.

**Dosya yolu belirtilmiş yanlış varsayımlar:** `raporlar/vardiya/` var (`sunum-proof-of-work.py:52` ölü dal değil). `veri/parquet/*.parquet` Eylül'den kalma.

## Okunan dosyalar
Tamamı ya da ilgili bölümleri: `katman-hatti.py`, `tarama-plan.py`, `katman-olcum.py`, `erisim-fts.py`, `pointer-graf.py` (100-262, 320-350, 440-654), `ambar-parquet.py`, `kolon-olcum.py`, `tarama-plan-duckdb.py`, `obsidian-harita.py`, `loop-dedektor.py`, `devir-ani.py`, `bag-tablo.py`, `prompt-tablo.py`, `karar-borcu-tablo.py` (20-140), `deneyim-tablo.py`, `harness_anahtar.py`, `baglam_oku.py`, `yuzey-parmak-izi.py`, `baglam-skill-aday.py`, `sunum-proof-of-work.py` (1-110), `sunum-son50.py` (1-60), `kosum-maliyeti.py`, `wiki-baglanti.py`, `anahtar-denetim.py` (14-75), `anahtar-cascade.py` (20-70), `ta-triyaj.py` (1-60), `pointer-kayma.py` (20-60), `prompt-dosya.py` (1-60), `buyuk-harf-temizle.py` (125-150), `akis-graf-html.py` (60-90) + `grep` taramaları. Ayrıca `kod/rituel/src/katman_hatti.rs` (1-80), `kod/hook/tests/ortak/mod.rs`.

## Okunmayanlar
- `baglam-tablo.py` (1019 satır, yalnız `git`/`tur_bul`/`main` kesitleri). Gerçek adım Rust `baglam-tablo.exe`; Python yalnız yedek. `baglam-tablo.py:177`'de tek `git log --name-status -M -c` bütün geçmişi tarıyor, ölçülmedi.
- `karar-borcu-tablo.py` 140-222, `paket-yonlendir.py` gövdesi, `prompt-dosya.py` 60+, `anahtar-denetim.py` 75+, `anahtar-cascade.py` 70+, `ta-triyaj.py` 60+, `pointer-kayma.py` 60+, `sunum-*` HTML şablon gövdeleri, `akis-graf-html.py` 1-60 ve 90+, `pointer-graf.py` 1-96 ve 262-320.
- Alt-ajan okuma kilidi: transkript dizini (prompt-tablo girdisi, boyut ölçülemedi), `veri/bronz/hareket-olay.jsonl` (satır sayısı ölçülemedi), `core/durum-kapsulu.md`, `core/pano.md`.

## `katman-hatti` yavaşlığı için en olası 3 Python adımı
Ölçüm yok; yalnız kod okumasına dayanan tahmin.
1. **`loop`** (`loop-dedektor.py:154-158`): iç içe döngü + alt-dizi taraması (bulgu 1).
2. **`kolon-olcum`** (`kolon-olcum.py:257`) birlikte **`tarama`** (`tarama-plan.py:135-136`): duckdb olmadığı halde 6 sorgu × 3 tam tarama ve 354 MB DB kopyası + ANALYZE (bulgu 3, 5).
3. **`prompt`** (`prompt-tablo.py:61-80`): O(n²) transkript taraması, önbelleksiz (bulgu 2). `erisim` (FTS tam yeniden kurulum, bulgu 6) ve `graf` (10 ELK render, bulgu 4) çok yakın ardıllar.

Gerçek sıralama için Rust `katman-hatti`'nin `--json` çıktısındaki `sure_s` alanı yeterli; yeni ölçüm gerekmez.
