# Denetim devam notu: 2026-11-10 (kontrollü duruş, Salih: "pc'yi geçici olarak kapatmam gerekiyor")

**Ne bu:** depo denetiminin kaldığı yer. Salih "devam" dediğinde buradan sürülür. Ana rapor: `raporlar/2026-11/denetim-depo-2026-11-10.md`; karar kaydı: defter Karar 128; ham işçi raporları (1-6): `cc/rapor/2026-11/rapor-2026-11-10-depo-denetimi-ham.md`; tüm oda kaydı (19 görev, raporlar tam metin): `../ortak/oda/202611101157-depo-denetimi-2026-11-10.json`.

**AS-OF:** 2026-11-10 16:25. Seans `2026-11-10-jarvis` açık (kapatılmadı). Koşan işçi yok. `cargo test --workspace` son koşumda tamamı geçti; `lake build` 82 iş başarılı.

## Bitti ve commit'li

- Push'lanmış: `e570c292`, `f6c45c5d` (ilk tur).
- Push bekleyen: `593f6ca6` (kalem 1-2: ajan kilidi Rust + deny yolları) · `c718c167` (kalem 3: git telleri) · `8b83e10f` (kalem 4: kanon + Karar 128) · `8bba1132` (kalem 5: arşiv) · `097a7fef` (kütük tek yazım, karar-borcu pointer'ları, 13 bayat gold görünüm arşivi) · bu notla gelen commit (tur 4: `durum` kütüğü sağlamlığı, `baglam-tablo` git meta, açılış kapısı K1, FIFO, `arac` ve `baglam` varsayılanları).

## Tur 4'te ne değişti (son commit)

- `durum`: `seans-kapat` teslim dosyasını doğrulamadan önce ezmiyor; aynı gün ikinci kapanış sıra eki alıyor; alan uyuşmazlığı reddediliyor; çıktı dosyaları geçici dosya + rename ile yazılıyor; yazan komutlar kilit dosyasıyla sıralanıyor; `--help` çalışıyor; brif bayt tavanı korunuyor.
- `baglam-tablo`: `git log` tüm depodan alınıp `jarvis/` önekiyle eşleniyor; ilk commit'i boş dosya 313 → 0, ilk commit tarihleri monorepo öncesine iniyor; Rust ve Python 1369 dosyada aynı (işçi ölçümü). Okunamayan dosya adımı düşürmüyor.
- `ambar-tablo` tek transaction; `graf` adımı panoları bir kez çiziyor (hat içi determinizm testi T5 "atlandı" görünür).
- Açılış kapısı K1 donmuş kapsül yerine `ortak/durum-olay.jsonl` kütüğüne bakıyor; `sicak-katman-fifo` listesinden kapsül ve pano çıktı. Python referansları aynı biçimde güncellendi.
- `masa-uret` ve `buyuk-harf-temizle` varsayılan deposu `<depo kökü>/jarvis`; `kod-orani-olcum` `.rs` ve `.lean` dosyalarını kod sayıyor; `baglam denetle ../AGENTS.md` doğru dosyayı gösteriyor (çıktı artık mutlak yol).
- Jarvis'in verdiği iki teknik alt-karar (Salih adına, itiraz edilirse geri alınır): Ö1 `git log` tam depo + önek eşleme · Ö2 fark testindeki dakika sınırı yarışı (`rituel_fark.rs` commit zamanları 60'ın katı).

## Devam edilecekler (sırayla)

1. **Push:** yukarıdaki commit'ler Salih beyanı bekliyor.
2. **Durum kütüğü:** oda görevleri iş #89-#107 olarak açık duruyor; biten her biri `durum bitir --kanit <commit>` ile kapatılacak.
3. **Tur 4 uçtan uca doğrulama (yapılmadı):** `katman-hatti` tam koşumu ve yeni süre ölçümü (önceki 97 sn; `baglam` adımı tek başına 13,5 sn ölçüldü); `seans-kapat` gerçek kapanışta yeni kilit ve sıra eki davranışı.
4. **Ana rapora ek:** tur 3 ve tur 4 bulguları (raporlar 12-14: 84 bulgu) `denetim-depo-2026-11-10.md` §3'e işlenecek. Henüz listeye girmemiş önemli kalemler:
   - `durum` kütüğünde tek bozuk satır bütün komutları kilitliyor (`lib.rs` ≈268, 363); UTC ve yerel tarih karışıyor.
   - `rituel`: transkriptler her koşumda üç ayrı adımda baştan okunuyor; `anakronizm-denetim.jsonl` her koşumda tüm bulguları yeniden ekliyor (sınırsız büyüme); `bayat_cekim` ve `anakronizm` Windows'ta ters bölülü yol üretip eşleşme kaçırıyor; `ambar_tablo.rs:631` metin `prompt_id` değerini harf harf bölüyor; kütüklerde CRLF ve LF karışık; `silver_saglik` var olmayan Python dosyasının özetini `kod_sha` sayıyor.
   - `arac`: `devir_md2json` md'den gelen kimliği süzmeden dosya adına koyuyor ve izin öneki ayraçsız; `yol_tasi` tek seferlik Mac göç aracı.
   - `kural`: `argparse`, `py`, `harness_anahtar` kopyaları `rituel` ile ayrışmış (`float_repr` farklı yuvarlıyor).
   - Python: `duckdb` kurulu değil, üç hat adımı kalıcı atlanıyor ve `kolon-olcum` yine de 354 MB tabloyu tarıyor; `tarama-plan` her koşumda veritabanını kopyalayıp ANALYZE ediyor; `erisim-fts` FTS dizinini her koşumda baştan kuruyor; `sunum-proof-of-work.py` Mac yolu ve `head` bağımlılığı; `wiki-baglanti.py` Windows yolunu URI'ye düz basıp hatayı yutuyor.
   - Veri: `talimat-yukleme-olay.jsonl` içinde 35 birleşik + 3 yırtık kayıt duruyor (neden düzeltildi, eski satırlar onarılmadı).
   - `tools/testler/test_fren_hook.py`: 2 test gerçek oturumun fren sayacını okuduğu için kırık.
   - `ogrenme/dosya-mimarisi/` ve `ogrenme/ontolojik-encode/` ders kayıtları 2026-11-01'den beri commit'siz; `ogrenme/README.md` ve `mufredat.md` taşınmış derslere eski yollarla işaret ediyor.
   - Span'ın 2026-10-19 devri: okuma kilidi şikâyeti bugün çözüldü (Windows geçici dizini artık izinli); M1-M5 ders iskeleti isteği hâlâ yanıtsız.
   - Açılış kapısı K2 kelime eşleşmesi (bitmiş pipeline'ı açık gösteriyor) duruyor.
5. **Seans kapanışı:** `seans-kapanis` ritüeli (hareket kütüğü, hafıza aynası, silver, türev dosyalar: `veri/`, `graf/pointer-sistemi-*`, `ortak/` bu oturumda commit'lenmedi).

## Bilinen riskler

- Git telleri artık açık: çıplak büyük harf içeren kanon dosyası ya da Türkçe karakterli commit konu satırı reddedilir (bilinçli atlama: `--no-verify`).
- Alan ajanı kilidi fail-closed: `target/release/jarvis-hook.exe` yoksa ajan oturumlarında okuma çağrıları engellenir (`cargo build --release -p jarvis-hook` ile çözülür).
- Ajan deny kuralları `//c/sistem/sistem/...` mutlak yoluna bağlı; depo başka yere taşınırsa şablon + 8 kopya güncellenir.
