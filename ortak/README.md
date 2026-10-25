# ortak/ — ortak çalışma alanı: durum kütüğü + akış grafı (Karar 113 M2 · Karar 121 · Karar 122)

## Doğruluk kaynağı
`durum-olay.jsonl`: ekle-yalnız olay kütüğü; satır = bir JSON olay. Kütük elle düzenlenmez, silinmez; güncel durum olayların katlanmasıyla hesaplanır.
- İş olayları: `ac` (`id`, `alan`, `is`, `sonraki_eylem`, `kanit`, `girdi`, `hedef`, `tur: is|hedef`, `son_gecerlilik`, `oturum`) · `al` · `bitir` · `tuket` · `bayatla`. Durumlar: acik · islemde · tamam · tuketildi · bayat.
- Seans olayları (Karar 122): `seans_ac` (`oturum`, `alan`, `hedef_cumle`) · `seans_kapat` (`oturum`, `hedef_tutuldu`, `kayit` = teslim kaydı yolu, `etiket`). Olaylardaki `oturum` alanı seansı işe bağlar (açtı / aldı / bitirdi).
- Ajan mesaj yazmaz, görev atamaz: seans başında kendi alanının konumunu okur, bitirdiğini `bitir`, tükettiğini `tuket` ile işaretler.

## Graf (türetilmiş görünüm; her `seans-kapat`'ta ve `durum graf` ile yeniden üretilir)
Düğüm = iş kaydı (`#id`) · hedef kaydı (altıgen) · seans (sayfa). Kenar = `girdi` (bağımlılık: girdi bitmeden iş sırada değildir) · `hizmet` (iş → hedef) · `açtı`/`bitirdi` (seans → iş) · `sonra` (seans → sonraki seans, aynı alan). **Sırada** = açık ∧ iş ∧ hiçbir girdisi açık/işlemde değil (`Kanon/AkisGraf.lean` `sirada`).
| Dosya | Okuyucu | Ne |
|---|---|---|
| `akis-graf.json` | Claude | tüm sistem; `dugumler` + `kenarlar`, deterministik sıra (`akis-graf v1`) |
| `durum oturum-basi --alan A` | Claude | ≤2 KB brif: `KONUM` (son seans + hedef yoklaması) · `SIRADA` · `bekler<-#n` · `HEDEF`; `--json` tipli |
| `durum graf --alan A --metin` | Claude | kenar listesi (graf dili); D2 kaynağı LLM'e verilmez |
| `graf/akis-<alan>.d2` · `.svg` · `graf/akis-tum.d2` · `.svg` | Salih | alan başına ve tüm sistem; render `d2 --layout=elk` (`--render` bayrağı) |
| `SALIH-OZET.md` | Salih | tek md: alan başına konum · son seansta ne değişti · karar · Salih'i bekleyen · sırada · görsel yolu (ASD-STE100 Türkçe; cümleler seans kayıtlarından) |
| `<alan>/raporlar/seans/seans-teslim-<tarih>-<etiket>.json` | Claude | seans kapanış kaydı: beş soru + hedef yoklaması (Claude) + `olcum` (Rust: git HEAD/dal/commit/dosya, durum sayaçları, süre); şablon `sablon/seans-teslim-girdi.json` |

md kapsül (`<alan>/core/durum-kapsulu.md`) ve pano **dondu** (2026-10-25): okunmaz, yazılmaz; arşiv-pointer.

## Komutlar (`jarvis/kod/durum/`, ikili `target/release/durum.exe`; kütük cwd'den yukarı bulunan `ortak/`)
`durum ac --alan sage --is "S4 dersi" --sonraki "Meditations 4. kitap PROBE" [--girdi 1,2] [--hedef 7] [--tur hedef] --oturum <seans>` · `durum al 1` · `durum bitir 1 --kalan "S5|PROBE"` · `durum oturum-basi --alan sage [--json]` ·
`durum seans-ac --alan sage --hedef "tek cümle"` · `durum seans-kapat --alan sage --oturum 2026-10-25-sage --girdi raporlar/seans/seans-teslim-girdi-2026-10-25.json --etiket s4 --render` · `durum graf [--alan A] [--metin] [--render]` · `durum ozet`.

Bilinen sınır: worktree'de kütük kopyadır; iki yan oturum aynı anda `ac` yaparsa `id` çakışır (durum #27). Seans kapanışında PR gecikmeden açılır, birleştirme Jarvis'te.
