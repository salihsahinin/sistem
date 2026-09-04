# Damıtma turu teslimi — 2026-09-04 (Karar 87 M2 a)

*Carvis/Fable ana oturum · başlangıç HEAD 8f8dfc5 · AS-OF 2026-09-04 01:xx · deneysel m.29 · her rakam script çıktısından (m.39). Tetik: Salih imzası (masa-8 M2 "a") + boyut-FLAG 4 dosya (08-30'dan beri açık). Kural kaynağı `core/ingest-semasi.md`; skill `damitma`.*

## 1. Sonuç tek satır
4 aşım dosyası bütçeye indi, 5 arşiv dosyası açıldı, hiçbir satır silinmedi (m.8), pointer 291/291 sağlam, sıcak anahtar ihlali 0, testler yeşil.

## 2. Boyut tablosu (bayt → KB, `stat -f%z`)
| Dosya | Önce | Sonra | Bütçe | Arşiv |
|---|---|---|---|---|
| `kuyruk/senaryo-defteri.md` | 76,0 | **44,7** | 48 | `kuyruk/arsiv/senaryo-defteri-arsiv-2026-09-04.md` (§1 seans-13 + Karar 65-68 · §2 Karar 79→84 EK-2 + 08-29→31 icra blokları; 32,6 KB) |
| `fikir-kutusu.md` | 24,0 | **18,5** | 20 | `kuyruk/arsiv/fikir-kutusu-arsivi-2026-09-04.md` (§1 V26-V62 tam satırlar) |
| `KILAVUZ.md` | 20,0 | **13,5** | 16 | `kuyruk/arsiv/KILAVUZ-arsiv-2026-09-04.md` (§1 Tasarım ilkeleri tam metin) |
| `core/pano.md` | 12,7 | **9,6** | 12 | `kuyruk/arsiv/pano-arsivi-2026-09-04.md` (§1 K-015 · §2 K-009 · §3 K-010 tam satırlar) |
| `core/durum-kapsulu.md` | 12,0 | 9,1 | 8 | — (SINIRDA; "Önceki" zinciri sonraki kapanışta kısalır) |

## 3. Sorgu-uyumu (KB-17c: hedef oran değil, cevap verebilme)
| Dosya | Cevap vermeye devam ettiği sorular | Nasıl |
|---|---|---|
| Defter | "Karar N ne dedi, nerede?" · "son iki masanın tam hükümleri?" · "Salih aynen ne dedi?" | Karar 65-68 ve 79-84 index satırı + arşiv pointer'ı; Karar 85/86/87 + 09-03 icra blokları TAM kaldı; aynen-beyanlar arşivde işaretli |
| Kutu | "hangi fikir bekliyor, tetiği ne, statüsü ne?" | V27-V62: etiket · özüt · damga (ayık/mobil/beyansız korundu) · statü; tam metin arşiv §1; V26 kanonlaşmış satırına indi; V56 statüsüne Karar 85 notu (UPDATE) |
| KILAVUZ | "kural ne, kim imzaladı, kaynağı ne?" | 16 ilke: ad + imza/Karar + kural çekirdeği + kaynak pointer; gerekçe metinleri arşivde |
| Pano | "kart durumu, kapı, sırada ne?" | K-015/K-009/K-010 güncel-durum + kapı tanımı; açılış gündemleri ve tarihçe arşivde |

## 4. Triyaj sayaçları (şema §3)
| giren | NOOP | UPDATE | GEÇERSİZ-KIL | ADD | DLQ |
|---|---|---|---|---|---|
| 1 bronz (`gelen-2026-08-30-a1-sayac-karar.md`) | 1 (hüküm Karar 83 EK-2'de zaten kanonda; damgalandı) | 3 | 0 | 0 | 0 |

UPDATE'ler: (1) KILAVUZ md-yüzeyi satırı "Obsidian" diyordu → Karar 80 (VS Code) işlendi, bayat satır 08-29'dan beri duruyordu; (2) kutu V56 statüsü Karar 85 (işçi = Sonnet) notu; (3) pano K-009 satırına senkron-kütüğü FAIL + masa-8 M9 pointer'ı. Kapsül "erisim-fts AXI serbest" bayat satırı önceki commit'te düştü (f3240ad tamam).

## 5. Erozyon sayacı
Kaybolan niteleyici/pointer: **0** — kısaltılan her blok tam metniyle arşivde; pano'dan çıkan 7 pointer (`ogrenme/loop-eng-yol-haritasi.md`, `ogrenme/mufredat.md`, bbycroft, `cc/rapor-2026-07-23-1.md`, `cc/gorev-2026-07-22-1.md`, G0-G6 raporu, `kuyruk/build-tartisma-notlari.md`) arşiv §1-§3'te; kutu damga niteleyicileri (ayık/mobil/beyansız) kısa satırda korundu. `python3 tools/pointer-kayma.py --ref HEAD` → pointer 291 · KAYMIŞ 0 · KIRIK 0. `karar-borcu-tablo.py` → 140 kalem · kaynak pointer 381 · kırık 0.

## 6. Kapılar
| Kapı | Sonuç |
|---|---|
| `anahtar-denetim.py` | ilk koşum sıcak ihlal 3 (kapsüle yazdığım "Cowork" — emekli anahtar, izinli kalıp "Cowork sekmesi") → düzeltildi → **TEMİZ (sıcak 0, bütünlük 0)**; ılık ihlal 132 tarihçe dosyalarında (EYLEM sınıfı, bu turun kapsamı dışı) |
| `silver-saglik.py --kapi` | exit 0 · ERROR 0 · WARN 2 (T-C3-ılık 111, T-C6 1 — bilinen) · ADAY 4 (T-B-YETİM 311/351 eşik altı · T-B-KAPANDI 105 · T-A-ONELEME 500/6985 → U5 triyaj raporu `raporlar/2026-09-03-ta-triyaj-ilk20.md`) |
| `katman-hatti.py` | ilk koşum T-C3-sıcak 2 (aynı Cowork satırları) → düzeltme sonrası temiz |
| Birim testleri | 102 test OK (7 skip) — damıtma öncesi ve sonrası |
| `deneyim-tablo.py` | 3 test PASS · **v_deneyim_cift: 0 çift** → kural adayı yazılmadı (m.39) |

## 7. Yansıma (dış geri-besleme var: Salih hükümleri M1/M2 + 102 test + 4 Cowork commit'i; ≤5 satır)
1. Bayat kural satırı 6 gün fark edilmeden durdu (KILAVUZ Obsidian ↔ Karar 80) — kaynak: bu tur UPDATE (1); Karar 80 icrası KILAVUZ'a yansımamıştı.
2. Kapsül damıtma-turu satırları emekli anahtarla ("Cowork") yazıldı, kapı yakaladı — kaynak: anahtar-denetim koşumu; ders: kapsüle yazmadan önce `Cowork sekmesi` kalıbı.
3. Defter büyümesinin kaynağı Lavish masaları (Karar 83: 7 satır ≈ 10 KB) — kaynak: bayt-aralık ölçümü (173-236 = 29 KB); masa hükümleri masa-sonrası aynı seansta index'e inmeli (aday: seans-kapanis §6'ya "masa bloğu ≥5 KB → index" satırı, Salih imzası).
4. Sonnet yan-oturumu 7/7 birimi fren 0 ile bitirdi (Karar 87 M1 tek-seferlik) — kaynak: `cc/devir-2026-09-03-sonnet-icra-cowork.md` + 102 test; Karar 86 D2 kalibrasyonuna 1 gözlem.
5. Erozyon 0 ölçüldü ama "sorgu-uyumu" testi elle (tablo §3); otomatik sorgu seti yok — aday: İB-20 eval sorularına damıtma-sonrası 5 soru.

## 8. Değişen dosyalar (commit bu turun sonunda, `git add <yol>`)
`kuyruk/senaryo-defteri.md` · `fikir-kutusu.md` · `KILAVUZ.md` · `core/pano.md` · `core/durum-kapsulu.md` · `kuyruk/gelen-2026-08-30-a1-sayac-karar.md` · 4 yeni arşiv · bu rapor. Üretici script'ler scratchpad'de (tek-kullanımlık; kalıcı araç yok — mevcut `pointer-kayma`/`karar-borcu-tablo` kapı olarak kullanıldı).
