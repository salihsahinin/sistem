# arsiv/kod/python — Rust'a taşınmış Python kaynakları (Karar 118 M2)

**Neden:** Karar 118 M2 (Salih, 2026-10-17; `jarvis/kuyruk/senaryo-defteri.md` satır 262): aynı görevi yapan kodun yalnız son sürümü bakımda kalır. Rust karşılığı fark testini geçen Python aracı ve hook betiklerinin Python gövdesi buraya iner (m.8 silme yasağı: taşınır, silinmez; yerinde pointer `jarvis/tools/SCRIPTLER.md`). Fark testleri: `jarvis/raporlar/2026-10-30-python-arsiv-fark-testi.md` (bu tur) · `arsiv/kod/rust-fark-testleri/` (Karar 117 EK-3 parti 2).

**Bakım yok:** buradaki dosyalar değiştirilmez; Rust fark testleri (`jarvis/kod/{rituel,kural,hook}/tests/ortak/mod.rs`) eski davranışı buradan okur. Çalıştırmak gerekirse `jarvis/` köküne kopyalanır (bağıl yollar `tools/` varsayar); hook gövdeleri `jarvis/.claude/hooks/rust-yonlendir.sh` yanına kopyalanır ve `JARVIS_HOOK_PYTHON=1` ile koşar.

## tools/ (Python aracı → Rust ikilisi `target/release/<ad>`, kaynak `jarvis/kod/`)

| dosya | Rust karşılığı | indiği tarih |
|---|---|---|
| `tools/ambar-tablo.py` | `ambar-tablo` (`kod/rituel/src/ambar_tablo.rs`) | 2026-10-17 (Karar 117 EK-3 parti 2) |
| `tools/anakronizm-denetim.py` (+ `testler/test_anakronizm_denetim.py`) | `anakronizm-denetim` (`kod/rituel/src/anakronizm_denetim.rs`) | 2026-10-17 |
| `tools/bayat-cekim.py` | `bayat-cekim` (`kod/rituel/src/bayat_cekim.rs`) | 2026-10-17 |
| `tools/devir-md2json.py` (+ `testler/test_devir_md2json.py`) | `devir-md2json` (`kod/arac/src/devir_md2json.rs`) | 2026-10-17 |
| `tools/harness_anahtar.py` | kütüphane modülü `kod/{kural,rituel}/src/harness_anahtar.rs` (canlı kopya `jarvis/tools/harness_anahtar.py` fark testi için durur) | 2026-10-17 |
| `tools/testler/test_tahmin_katmani.py` | — (ambar-tablo testi) | 2026-10-17 |
| `tools/acilis-kapilari.py` | `acilis-kapilari` (`kod/rituel/src/acilis.rs`) | 2026-10-30 (Karar 118 M2) |
| `tools/ad-esitligi-denetim.py` | `ad-esitligi-denetim` (`kod/kural/src/ad_esitligi.rs`) | 2026-10-30 |
| `tools/alan-ajani-dogur.py` | `alan-ajani-dogur` (`kod/arac/src/alan_ajani.rs`) | 2026-10-30 |
| `tools/baglam-seyir.py` | `baglam-seyir` (`kod/rituel/src/seyir.rs`) | 2026-10-30 |
| `tools/hafiza-ayna.py` | `hafiza-ayna` (`kod/rituel/src/ayna.rs`) | 2026-10-30 |
| `tools/hareket-tablo.py` | `hareket-tablo` (`kod/rituel/src/hareket.rs`) | 2026-10-30 |
| `tools/paralel-kapi.py` (+ `testler/test_paralel_kapi.py`) | `paralel-kapi` (`kod/kural/src/paralel.rs`) | 2026-10-30 |
| `tools/sicak-katman-fifo.py` | `sicak-katman-fifo` (`kod/rituel/src/fifo.rs`) | 2026-10-30 |
| `tools/silver-saglik.py` | `silver-saglik` (`kod/rituel/src/silver_saglik.rs`) | 2026-10-30 |
| `tools/skill-esik.py` | `skill-esik` (`kod/kural/src/skill_esik.rs`) | 2026-10-30 |
| `tools/yol-tasi.py` | `yol-tasi` (`kod/arac/src/yol_tasi.rs`) | 2026-10-30 |

Yerinde kalanlar (Rust karşılığı var, başka Python dosyası yüklüyor): `baglam-tablo.py` · `buyuk-harf-temizle.py` · `katman-hatti.py` · `kod-orani-olcum.py` · `kural-sayaci.py` (gerekçe raporda).

## hooks/ (bash betiği içindeki Python gövdesi → `jarvis-hook <olay>` / `hook-dispatch`, kaynak `jarvis/kod/hook/`)

| dosya | Rust karşılığı | indiği tarih |
|---|---|---|
| `hooks/hook-dispatch.sh` (kök `bin/`) | `hook-dispatch` (`kod/hook/src/bin/hook_dispatch.rs`) | 2026-10-30 |
| `hooks/instructions-loaded.sh` | `jarvis-hook instructions-loaded` (`talimat.rs`) | 2026-10-30 |
| `hooks/pretool-ajan-fren.sh` | `jarvis-hook pretool-ajan-fren` (`ajan_fren.rs`) | 2026-10-30 |
| `hooks/pretool-altajan-okuma.sh` | `jarvis-hook pretool-altajan-okuma` (`altajan_okuma.rs`) | 2026-10-30 |
| `hooks/pretool-core-tel.sh` | `jarvis-hook pretool-core-tel` (`core_tel.rs`) | 2026-10-30 |
| `hooks/session-start.sh` | `jarvis-hook session-start` (`session_start.rs`) | 2026-10-30 |
| `hooks/stop-buyuk-harf.sh` | `jarvis-hook stop-buyuk-harf` (`buyuk_harf.rs`) | 2026-10-30 |
| `hooks/userprompt-dosya.sh` | `jarvis-hook userprompt` (`prompt_dosya.rs` + `paket.rs`) | 2026-10-30 |

Canlı betikler (`jarvis/.claude/hooks/*.sh`, `bin/hook-dispatch.sh`) yalnız `rust-yonlendir.sh` + ikili-yok uyarısı taşır.
