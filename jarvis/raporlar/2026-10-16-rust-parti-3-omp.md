# Rust taşıma parti 3: kural araçları + Lean bağı (durum #14, Karar 114)

AS-OF 2026-10-16. Dal `oturum/2026-10-16-omp-rust3` (başlangıç: `origin/main` `7a79a8a`); parti 2 dalına (PR #7) dokunulmadı. Bu iş ondan bağımsızdır: `py.rs`/`argparse.rs`/`harness_anahtar.rs` PR #7'den küçültülmüş kopya olarak `jarvis/kod/kural/src/` altında durur (birleşince ortak crate'e taşınabilir; iki crate de `jarvis-hook`'u yol bağımlılığı olarak kullanır, o `origin/main`'dedir).

`[sapma]` Kök `Cargo.lock` da commit'e girdi (yeni crate bağımlılıkları; takipli dosya, işlenmezse `--locked` derleme bozulur). Başka kök dosyaya dokunulmadı (`Cargo.toml`: yalnız `members`).

## 1. Taşınan araçlar

| Python | Rust (`jarvis/kod/kural/`) | Python satır | Rust satır |
|---|---|---|---|
| `.claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py` | `src/tetik.rs`, bin `tetik-denetim` | 91 | 270 |
| `.claude/skills/halusinasyon-engelleyici/scripts/derece.py` | `src/derece.rs`, bin `derece` | 53 | 81 |
| `tools/skill-esik.py` | `src/skill_esik.rs`, bin `skill-esik` | 61 | 205 |
| `tools/paralel-kapi.py` | `src/paralel.rs` + `src/pyjson.rs`, bin `paralel-kapi` | 242 | 661 + 283 |
| `tools/ad-esitligi-denetim.py` | `src/ad_esitligi.rs`, bin `ad-esitligi-denetim` | 83 | 151 |
| (ortak, parti 2'den küçültülmüş) | `src/py.rs`, `src/argparse.rs`, `src/harness_anahtar.rs` | - | 416 + 489 + 55 |

Küçültme: `argparse.rs`'ten `append`/`nargs="*"` atıldı, `type=float` eklendi (`skill-esik`); `py.rs`'ten alt süreç/zaman aşımı/`errors="ignore"` okuma atıldı, `float()`/`repr(float)`, `re.I` katlama (`katla`), `UnicodeDecodeError` iletisi eklendi. `pyjson.rs`: Python 3.11 `json.load` hata iletilerinin (`Expecting value`, `Expecting ',' delimiter`, `Extra data`, `Invalid control character`, `Invalid \escape`, ...) konum dahil karşılığı; `paralel-kapi` bütünlük hatalarında Python iletisini aynen basıyor. `paralel-kapi.py`'deki `tur_turet` `main`'den çağrılmıyor (Python'da da); taşındı ve Python işleviyle ayrıca denendi.

Python dosyalarına, `.claude/` ve `SKILL.md` dosyalarına dokunulmadı; araçların Rust'a bağlanması yapılmadı.

## 2. Lean bağı

`jarvis/lean/lakefile.toml`: iki `lean_exe` ve `defaultTargets` genişletildi; yeni dosyalar `TetikMain.lean`, `DereceMain.lean` (kalıp `Main.lean`: stdin `anahtar=değer` satırları, `---` ile ayrılmış kayıtlar, kayıt başına bir hüküm satırı, çıkış 2 = girdi hatası). Mevcut `Kanon/*.lean` dosyalarına dokunulmadı.

| exe | Spec işlevleri | Girdi/çıktı |
|---|---|---|
| `tetik` | `Kanon.SkillTetik.kapiO`, `kapiS` | `kapi=O` (varsayılan): `Cagri` alanları → `reddet`·`iste`·`anaSiraya`·`atla`·`cagir`; `kapi=S`: `Sonuc` alanları → `gecti`·`tekrar`·`failLoud` |
| `derece` | `Kanon.Halusinasyon.hukum`, `cikisKodu` | `v1..v10` (+`v3a-d`,`v7a-c`) ve `pahali` bayrakları → çıkış kodu 0/5/10 |

`lake build`: 38/38 iş başarılı.

## 3. Fark testi sonucu

`cargo test -p jarvis-kural` (8 test, geçti; `cargo clippy -p jarvis-kural --all-targets` uyarısız). Karar 115'e göre araç başına en çok ~40 durum; argparse kısaltma ve `COLUMNS` matrisleri yapılmadı.

### 3.1 Python = Rust (süreç düzeyi: stdout, stderr, çıkış kodu, yazılan dosyalar)
Düzen parti 2'deki gibi: iki geçici kök, aynı adım iki yanda koşar. **215/215 durum eşit.**

| Araç | Durum | İçerik |
|---|---|---|
| `derece` | 36 | tek bayraklar, eşik sınırları (H=3/4/6/7; pahalı 3/4), v7c/v8 indirimleri, v3a override, `--json`, kullanım (çıkış 2) |
| `tetik-denetim` | 45 | `yok` biçimleri, iyi/kötü çağrı, her sert kapı, yumuşak kapı sınırları (derinlik 2/3, işaret 3/4), T-Y kuralları, başlık/CRLF/BOM, `--repo` biçimleri, skill dizini kenarları |
| `skill-esik` | 43 | n=9/10 sınırı, tam 2x / 2x+1, pencere 23 sa / 25 sa, `--saat/--carpan/--esik-n` değerleri, tek/çift medyan, float, çok model, başka `agent_type` |
| `paralel-kapi` | 46 | Bernstein çiftleri, glob/snapshot/bölüm, silver/kanon/dışlama/loop, canlı/tamam, dalgalar/kademe/öncelik, uyarılar, bütünlük hataları (15 bozuk JSON biçimi, çevrim, kopya, eksik alan), `…` kırpma sınırı 3/4 |
| `ad-esitligi-denetim` | 32 | K1/K2/K3, `ı`/`İ` denkliği, muaf dosyalar, gizli/atlanan dizinler, geçersiz UTF-8 |
| `paralel-kapi` `tur_turet` | 13 | Python işlevi doğrudan çağrılır; `main` çağırmadığından süreç testi yok |

Bu 215 içinde 16 durumda stderr karşılaştırılmaz (`.atla()`): 13'ü Python traceback'i (bkz. 4.1), 3'ü (`skill-esik` DB yok `--json`, `paralel-kapi` dizin yok iki durum) çökme değildir, stderr da eşittir. Gerçek veri dumanı (bu worktree'nin gerçek `jarvis/` dizini, gerçek `cc/gorev/*/*.md`): 259 koşum (124 emir dosyası x düz/`--json` + diğer araçlar) çıktı ve çıkış kodu **259/259 eşit**.

Duyarlılık kontrolü (geçici mutasyon, sonra geri alındı): `skill-esik` `>` yerine `>=`, `ad-esitligi` muaf listesinden bir ad, `tetik` iç içe sınırı 3 yerine 4, `paralel` `…` kırpma sınırı 3 yerine 4. İlk koşumda son ikisini fixture yakalamadı; sınır değerli iki durum eklendi, ardından yakalandı.

### 3.2 Python = Rust = Lean (üç yönlü hüküm)
| Test | Kapsam | Sonuç |
|---|---|---|
| `derece` | 15 bayrak + pahalı sınıfı = **65.536 bileşimin tamamı**: Lean `derece` ikilisi, Rust `derece::hukum`, Python `derece.py` (modül bir kez yüklenir, her bileşimde `main()`) | 65.536/65.536 aynı çıkış kodu; dağılım {0: 2.102, 5: 3.459, 10: 59.975} |
| `tetik` | Python ve Rust ikilisi ile Lean `kapiO`, gözlenebilir altı bit (skill var, alanlar tam, kip literal/örtük, yan-etkili, alt-ajan, derece ifadesi) = 64 bileşim | 64/64: Python/Rust GEÇTİ ⇔ Lean `cagir`; Lean ilk-isabet sınıfı (`iste`/`anaSiraya`/`atla`) Python'un düşen kapılarıyla tutarlı. Lean dağılımı {iste 32, atla 21, anaSiraya 6, cagir 5} |
| `tetik` Kapı-S | Lean `kapiS` ikilisi, 16 girdi bileşimi x 4 deneme = 64 | 64/64 md kuralıyla (done ∧ şema ∧ hata kanalı → geçti; aksi deneme<3 → tekrar, aksi failLoud). Python karşılığı yok; yalnız ikili bağlantı denetimi |

Üç yönlü toplam: 65.536 + 64 bileşim (Python = Rust = Lean) + 64 Kapı-S (Lean). Lean ikilisi yoksa bu iki test atlanır (skill-kapi fark testindeki kalıp); bu koşumda ikili derlenmişti.

## 4. Python, Rust ve Lean arasındaki ayrışmalar

### 4.1 Python istisnası (traceback) olan durumlar
Python traceback basar ve 1 ile çıkar; Rust aynı çıkış kodu ve stdout ile `[HATA] Python karşılığında yakalanmamış istisna olurdu: ...` yazar. Durumlar:
- `tetik-denetim`: olmayan emir dosyası; `--repo` son argüman; `--repo X emir.md` (Python ilk `--`'siz argümanı `X` sayar ve onu dosya olarak açar; bu kusur birebir korundu); UTF-8 olmayan emir ya da SKILL.md.
- `skill-esik`: `amb_olgu_kosum` tablosu yok ya da DB değil; `--saat nan/inf/1e12` (`OverflowError`/`ValueError`); boş token/süre listesi; karışık türde model anahtarları.
- `paralel-kapi`: manifest üst düzey değeri sayı/bool/null ya da tüm alanları içeren metin; `birim_id` metin değil; `sira`/`yazar`/`okur` beklenen türde değil (Python alana dokunduğunda çöker; Rust alanı okurken çöker, tek birimli planda Python çökmeyebilir).

### 4.2 Bilinçli farklar (Python ↔ Rust)
1. **Yeni satır** Rust'ta `\n` (Python Windows'ta stdout'a `\r\n`; hook ve parti 2'deki aynı karar). Test `\r` siler.
2. **Varsayılan jarvis dizini:** Python betik konumuna göre, Rust `CLAUDE_PROJECT_DIR`'a, yoksa çalışma dizinine göre çözer (`skill-esik --repo`, `ad-esitligi-denetim`, `harness_anahtar`). `ad-esitligi` ve `tetik` aracın kendi Python dosyasını aynı yoldan atlar.
3. **`re.I` denkliği:** `ı`/`İ`/`ſ` için katlama (`py::katla`); Python `re`'nin diğer nadir eşdeğerlikleri (Yunanca `ς`/`σ` gibi) taklit edilmedi.
4. **`fnmatch`:** `[...]` küme biçimleri `fnmatch.translate` mantığıyla çevrilir; ters eğik çizgi ve çıplak `]` gibi uç biçimler denenmedi `[?]`. Windows'ta büyük/küçük harf duyarsız (Python gibi; test: `Dizin/A.md` ~ `dizin/a.md`).
5. **JSON:** `NaN`/`Infinity` sabitleri `null` olarak okunur (Python `float`); sayılar `i64`/`u64`/`f64`'e sığar (Python sınırsız tamsayı).
6. **`skill-esik`:** `{med:.0f}` ve `{x:.1f}` Rust biçimlendirmesiyle; Python `float` gösterimi (`1e+16`, `2.0`) `py::float_repr` ile taklit edilir, yalnız tipik aralıkta denendi. SQLite DB okuma/yazma kipinde açılır (Python gibi); açılış hatası iletisi `: <uri>` eki kırpılarak eşitlenir.
7. **`paralel-kapi` JSON hata iletisi konumu** kod noktası indeksidir (Python gibi); Windows'ta dizin adlı `x.json` için `[Errno 13] Permission denied` (POSIX'te `[Errno 21]` yazılır; yalnız Windows'ta denendi).
8. **`os.walk` sırası** (ad-esitligi K3 çıktı sırası) işletim sisteminin dizin okuma sırasıdır; Rust `read_dir` ile aynı; yalnız NTFS'te denendi.

### 4.3 Lean ↔ Python/Rust (spec ile uygulamanın örtüşmediği yerler)
Bunlar fark testinde iddia olarak sabitlenmedi (test çıktısında `[ayrisma]` satırları); spec/araç hizalama kararı Salih'indir.
1. **`kip = yasak`:** Python/Rust O3 kapısını geçirir (`yasak` geçerli kip, çağrı GEÇTİ, çıkış 0); Lean `kapiO` `yetkili` ile `anaSiraya` verir (yasak kip hiç çağrılmaz). Test çıktısı: `Rust/Python çıkış 0 · Lean anaSiraya`.
2. **İç içe koşul derinliği 3:** Python/Rust O5-icice yumuşak kapıdır (△, çıkış 0); Lean `tetikBicimi` derinlik ≤ 2 ihlalinde `atla` verir. Test çıktısı: `Rust/Python çıkış 0 · Lean atla`. Sınırlar da farklı: Python `eğer/ise/→` işareti ≤ 3, Lean `dalSayisi ≤ 5`.
3. **Alan sayısı:** Python 10 alan (`skill`, `tetik_kosulu`, `cagri_kipi`, `girdi`, `baglam`, `yan_etki_damgasi`, `done_yuklemi`, `hata_yolu`, `sira`, `kayit`) arar, mesajı "9 alan dolu"; Lean `alanlarTam` "dokuz alan". Sayı farkı iki tarafta da sabit.
4. **Python'un gözlemlemediği Lean girdileri:** `tetikDogru`, `girdiTam`, `celiskiTemiz`, `tetikAracCiktisindan` Python'dan türetilemez; üç yönlü testte sabit "temiz" verildi. Yan-etki bilgisi skill dosyası yoksa bilinmez: Python `yan_etkili=false` sayar, Lean girdisinde de öyle.
5. **Python'da olup Lean'de karşılığı olmayan kapılar:** O6-retry, O6-failloud, O7-done-boolean, O8-damga, O5-negatif. Lean `kapiS` (done, şema, hata kanalı, deneme) ise Python'da yok; yalnız Lean ikilisinin bağlantı denetimi yapıldı.
6. **`derece`:** Lean = Rust = Python, ayrışma yok (65.536 bileşim).

## 5. Karşılaşılan sorunlar
1. **Eşik sınırlarını fixture yakalamadı:** `tetik` işaret sayısı 3/4 ve `paralel` `…` 3/4 sınırları ilk durum kümesinde yoktu; mutasyon kontrolü bulgusu, durumlar eklendi.
2. **Test düzeni:** `ad-esitligi` adımında `tools` dizinini silmek betiğin kendisini de siliyordu; yalnız fixture dosyaları silinir. `skill-esik` fixture'ında `veri/` yokken DB oluşturulamıyordu; `create_dir_all` eklendi.
3. **Python JSON hata iletileri:** `paralel-kapi` bütünlük hatası metnine Python'un `JSONDecodeError` iletisi girdiğinden C çözücünün konum kuralları (`Invalid \uXXXX escape` için `end - 5` gibi) taklit edildi; 15 bozuk biçimle denendi.
4. **Test sandbox'ında Windows kabuğu:** Git-Bash'te göreli `./target/...` yolu bulunamadı, ad hoc kontroller Python üzerinden yapıldı.
5. **Satır sonları:** `write` ile yazılan dosyalar karışık satır sonu üretmişti; commit öncesi `jarvis/kod/kural/` ve Lean dosyaları LF'ye çevrildi.

## 6. Harcanan token, süre, maliyet

Kaynak: omp oturum kütüğü (`~/.omp/agent/sessions/--C--sistem-wt-omp-rust2--/2026-10-16T12-40-34-247Z_01a144ba-....jsonl`), parti 3 görev mesajından (14:00:23Z) son kayıtlı asistan mesajına (14:24:21Z) kadar 42 asistan mesajının `usage` alanları toplamı. Model `anthropic/claude-sonnet-5-5` (medium).

| Kalem | Değer |
|---|---|
| Girdi (önbelleksiz) | 86 token |
| Çıktı | 143.349 token |
| Önbellek okuma | 16.905.577 token |
| Önbellek yazma | 189.289 token |
| Toplam (kütükteki `totalTokens`) | 17.238.301 token |
| Maliyet (kütükteki `cost.total`) | 3,88 USD |
| Duvar süresi | 23 dk 58 sn |
| Model yanıt süresi toplamı (`duration`) | 1237,9 sn |

Sayaç bu raporu yazmadan önceki son mesaja kadardır; rapor yazımı, commit, push, PR ve son yanıt dahil değildir.

## 7. Koşum
```
cd jarvis/lean && lake build                # tetik ve derece ikilileri (üç yönlü test için)
cargo test -p jarvis-kural                  # Python 3.11 + git + (Lean ikilileri) gerekir
cargo run -p jarvis-kural --bin derece -- --v1 --v2 --v5 --json
```
