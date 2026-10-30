# Python arşiv fark testi (Karar 118 M2) — 2026-10-30

`[tip: rapor | kaynak: claude-code yan-oturum Fable 5.1 (worktree py-arsiv-karar-118-m2) | tarih: 2026-10-30 | hedef: raporlar | koken: jarvis/ana-sıra emri, durum #22]`

**`[sapma]` Arşiv konumu:** emir `jarvis/arsiv/kod/python/` dedi; depoda Karar 117 EK-3 parti 2 (commit `a5130b4`) ile açılmış ve `tools/SCRIPTLER.md` satır 105-106'nın işaret ettiği **kök `arsiv/kod/python/tools/`** zaten var (ambar-tablo, anakronizm-denetim, bayat-cekim, devir-md2json, harness_anahtar). Tek arşiv konumu ilkesiyle (m.8 pointer tek adrese iner) dosyalar oraya indi; hook gövdeleri kardeş dizin `arsiv/kod/python/hooks/`. Karar 118 M2 metni de `arsiv/kod/python/` der, `jarvis/` öneki emrin yorumuydu.

## Yöntem

- Rust ikilisi: ana kopya `C:/sistem/sistem/target/release/<ad>.exe` (worktree'de `target/` yok; `cargo build --release` 2026-10-30 öncesi ana kopyada yapılmış).
- Python aracı: worktree `jarvis/tools/<ad>.py`, `python` 3.x, `PYTHONUTF8=1`.
- Her çift aynı cwd (`jarvis/`) ve aynı argümanla koştu; stdout, stderr ve çıkış kodu kıyaslandı. Tur 1 `--help` (16 araç). Tur 2 yazma yapmayan argüman (`--kuru` / `--json` / salt tespit; 10 araç).
- **Tek sistematik fark:** Windows'ta Python stdout'a `\r\n`, Rust `\n` yazıyor. `diff --strip-trailing-cr` sonrası 16/16 araç tur 1'de ve 10/10 araç tur 2'de bayt bayt eşit. Program adı dahil (Rust ikilisi `usage: <ad>.py` basıyor).
- Yazma yapan alt komutlar koşulmadı (emir). `yol-tasi --kuru` iki tarafta da `raporlar/2026-09/yol-tasi-kuru-2026-10-30.diff` üretti (kuru koşum çıktısı); bu koşum artığı commit'lenmedi, kaldırıldı.
- Ham çıktılar oturum scratchpad'inde (`.../scratchpad/out/<ad>.<arg>.{py,rs}.{out,err}`); depoya girmedi.

## Sonuç tablosu

| araç | Rust komut | Python komut | sonuç | not |
|---|---|---|---|---|
| acilis-kapilari | `../target/release/acilis-kapilari --help` · `--json` | `python3 tools/acilis-kapilari.py --help` · `--json` | **GEÇTİ** (2/2 eşit, çıkış 0/0) | tespit eder, yazmaz → **arşiv** |
| ad-esitligi-denetim | `--help` · `--json` | aynı | **GEÇTİ** (2/2, çıkış 0 · 4) | çıkış 4 = eksik var, iki tarafta aynı → **arşiv** |
| alan-ajani-dogur | `--help` · `kuyruk/alan-ajanlari-2026-09-28.json --kuru` | aynı | **GEÇTİ** (2/2, çıkış 0) | Rust kökü worktree `Cargo.toml`'dan buldu → **arşiv** |
| baglam-seyir | `--help` · `--kuru --sessiz` | aynı | **GEÇTİ** (2/2, çıkış 0 · 1) | tur 2 iki tarafta aynı hata (transkript dizini yok, worktree anahtarı) → **arşiv** |
| baglam-tablo | `--help` | aynı | GEÇTİ (1/1) · **YERİNDE** | `tools/anahtar-denetim.py:38` ve `tools/testler/test_katman_tek_tanim.py` dosyayı `importlib` ile yüklüyor; arşive inerse anahtar-denetim (Rust karşılığı yok) kırılır. SCRIPTLER 103 zaten "yerinde kaldı" der |
| buyuk-harf-temizle | `--help` | aynı | GEÇTİ (1/1) · **YERİNDE** | `tools/git-hooks/caps-say.py:8` (`pre-commit` teli) `donustur()` için `importlib` ile yüklüyor; pre-commit Rust'a bağlanmadan taşınamaz |
| hafiza-ayna | `--help` · `--kuru --json` | aynı | **GEÇTİ** (2/2, çıkış 0 · 2) | tur 2 iki tarafta `KAYNAK-YOK` (worktree anahtarı), çıkış 2 aynı → **arşiv** |
| hareket-tablo | `--help` · `--kuru --sessiz --tarih 2026-10-30` | aynı | **GEÇTİ** (2/2, çıkış 0) | → **arşiv**; `katman-hatti` adım `hareket` zaten ikiliyi tercih eder |
| katman-hatti | `--help` | aynı | GEÇTİ (1/1) · **YERİNDE** | `tools/testler/test_tarama_plan.py:12,55` ve `test_kolon_katmani.py:442` hattı Python betiğiyle koşturuyor (bu iki test yerinde kalan tarama-plan / kolon katmanını sınar); SessionStart brifi ve 6 kanon dosyası `python3 tools/katman-hatti.py` tarifini taşıyor |
| kod-orani-olcum | `--help` | aynı | GEÇTİ (1/1) · **YERİNDE** | `tools/karantina.py:128`, `tools/kod-envanter.py:61`, `testler/test_kod_envanter.py`, `testler/test_kod_orani.py` `DISLA_DIZIN` için yüklüyor (Karar 88 M14). SCRIPTLER 104 zaten "yerinde kaldı" der |
| kural-sayaci | `--help` | aynı | GEÇTİ (1/1) · **YERİNDE** | `tools/kural-envanter.py:44` `importlib` ile yüklüyor (birim tanımı tek kaynak) |
| paralel-kapi | `--help` · `--json --sessiz` | aynı | **GEÇTİ** (2/2, çıkış 0 · 1) | tur 2 JSON (27 birim, bütünlük hataları listesi) bayt bayt eşit → **arşiv** (+ `testler/test_paralel_kapi.py` birlikte iner) |
| sicak-katman-fifo | `--help` · `--json --tarih 2026-10-30` | aynı | **GEÇTİ** (2/2, çıkış 0) | listeler, taşımaz → **arşiv** |
| silver-saglik | `--help` · `--kuru --sessiz` | aynı | **GEÇTİ** (2/2, çıkış 0 · 1) | tur 2 iki tarafta `[HATA] silver yok` (worktree'de sqlite yok) → **arşiv**. Not: Rust `kod_sha` için `tools/silver-saglik.py` baytlarını okuyordu (`silver_saglik.rs:1585`); dosya yokken sabit `silver-saglik-rust` sha'sına düşer, davranış değişmez, yalnız `kosum_id` türetimi sabitlenir |
| skill-esik | `--help` | aynı | **GEÇTİ** (1/1, çıkış 0) | tur 2 yok: tek işlevi sqlite okuması, worktree'de yok; `--help` + Rust fark testi `kod/kural/tests/kural_fark.rs` → **arşiv** |
| yol-tasi | `--help` · `--kuru` | aynı | **GEÇTİ** (2/2, çıkış 0) | kuru koşum raporu (391 B) eşit → **arşiv** |

Özet: 16/16 fark testini geçti; **11 arşive indi**, **5 yerinde kaldı** (sebep: başka Python dosyası `importlib` ya da alt süreçle yüklüyor; Rust karşılığı olmayan o dosyalar kırılırdı).

## Rust ikilisi olup Python'u zaten arşivde ya da `tools/` dışında olanlar (bu turda dokunulmadı)

- `ambar-tablo` · `anakronizm-denetim` · `bayat-cekim` · `devir-md2json`: Python `arsiv/kod/python/tools/` (Karar 117 EK-3 parti 2).
- `derece` ↔ `.claude/skills/halusinasyon-engelleyici/scripts/derece.py` · `tetik-denetim` ↔ `.claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py` · `masa-uret` ↔ `.claude/skills/karar-masasi/scripts/masa-uret.py`: skill betikleri; emir kapsamı `tools/` idi. Fark testleri `kod/kural/tests` ve Rust tarafında var; aynı kuralla arşive inebilirler (**takip**).
- `durum` · `baglam` · `skill-kapi` · `jarvis-hook` · `hook-dispatch`: doğrudan Rust doğdu ya da Python karşılığı hook gövdesi (aşağıda).

## Hook'lar (adım 5)

Rust karşılığı `jarvis-hook <olay>` / `hook-dispatch` olan 7 hook'un Python gövdesi + kök `bin/hook-dispatch.sh` gövdesi `arsiv/kod/python/hooks/`'a kopyalandı; canlı betikte `rust-yonlendir.sh` kaldı, ikili yoksa `önce cargo build --release -p jarvis-hook` uyarısı (stderr) + çıkış 0. `posttool-read-genislet.sh` zaten Rust-only idi (gövde yok); `pretool-altajan-okuma-test.sh` ve `stop-buyuk-harf-test.sh` test sürücüleri (hook değil) dokunulmadı. `python3 -c` ile yalnız JSON ayrıştıran hook'lar (`pretool-core-tel`, `pretool-ajan-fren`, `stop-buyuk-harf`) için de Rust alt komutu var; aynı işlem uygulandı.

## Takip (bu PR dışı)

1. Rust fark testleri (`kod/rituel`, `kod/kural`, `kod/hook` `tests/ortak/mod.rs`) Python kaynağını `jarvis/tools/` yoksa `arsiv/kod/python/` altından alacak biçimde güncellendi; `cargo test` bu oturumda koşulmadı/koşuldu bilgisi PR gövdesinde.
2. `session_start.rs:178` brif metni `tools/ad-esitligi-denetim.py` diyor; araç arşivde. Tek sözcük, yeniden derleme ister.
3. Kanon/wiki/README'lerde `python3 tools/<ad>.py` tarifleri (KURULUM.md 4, `veri/README.md` 7, `core/baglam-anahtar-kaydi.md` 5, alan ajanı AGENTS/kapsül satırları) tarihçe sayıldı, dokunulmadı; Katman-1 dosyalar Salih imzası ister.
4. Skill betikleri (derece, tetik-denetim, masa-uret) için aynı arşiv turu.
5. `pre-commit` teli Rust `buyuk-harf-temizle`'ye bağlanırsa `buyuk-harf-temizle.py` + `caps-say.py` arşive inebilir; `anahtar-denetim.py` ve `kural-envanter.py` Rust'a geçince `baglam-tablo.py` ve `kural-sayaci.py` de.
