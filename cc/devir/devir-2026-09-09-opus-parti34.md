# Devir notu — Parti 3-4 dosya düzeni + devir-anı loglayıcı (Opus 5 medium lider, yan-oturum, 2026-09-09)

*Şema: İB-75 §6 `geri-donus v0`. Emir: `cc/gorev/2026-09/gorev-2026-09-09-parti34-dosya-duzeni-devir-ani.md`. Plan: `kuyruk/dosya-duzeni-plani-2026-09-09.md`. Manifest: `veri/manifest/u9-parti34-dosya-duzeni.json`. Commit'ler: `3b0b3d0` · `cb5edf6` · `7a97c2d` · `990863c` (push YOK — m.9).*

## 1. Biten / kalan

| # | İş | Durum | Kanıt |
|---|---|---|---|
| 1 | U1a `cc/` taşıma (338 dosya) | BİTTİ | `3b0b3d0` · rapor 194 · gorev 120 · pipeline 16 · prompt 4 · devir 4 |
| 2 | U1b `raporlar/` taşıma (302 dosya) | BİTTİ | `cb5edf6` · seans 26 · vardiya 47 · hareket 23 · masa 9 · gorsel 11 · jarvis 8 · konu 164 · diger 4 |
| 3 | U1c-1 `tools/*.py` + ledger + SCRIPTLER | BİTTİ | `7a97c2d` · 19 script · ledger kırık 127→0 · SCRIPTLER 9 yol |
| 4 | U1c-2 md pointer + README | BİTTİ | `7a97c2d` · 78 md dosyası / 467 pointer · 13 README |
| 5 | U2 `tools/devir-ani.py` + 3 test + katman-hatti adımı | BİTTİ | `990863c` · jsonl 91 satır · test 118→121 |
| 6 | Kanon (`core/`, `.claude/`, `CLAUDE.md`) yol düzeltmesi | **YAPILMADI (kasıtlı)** | m.41 — §3 listesi ana-sıraya |
| 7 | Karantina tescili | **YAPILMADI (kasıtlı)** | aday yok — §5 |
| 8 | Push | **YAPILMADI** | m.9 — Salih beyanı gerekir |

**Done ölçümü (DRFR, emrin 9 koşulu):**
① `cc/` üst seviyede yalnız tekiller + alt dizinler ✓ (5 tekil: `defter.md`, `README.md`, `oran-2026-07-30-24.py`, `karar-onerisi-2026-08-16-hat6.md`, `2026-08-29-erisim-soru-buyutme.py`)
② `raporlar/` üst seviyede yalnız `usage/` + alt dizinler — **KISMEN**: izlenen dosyalardan yalnız yeni `raporlar/README.md` üstte; ayrıca 3 İZLENMEYEN dosya kökte duruyor (§6)
③ tüm alt dizinlerde README — **KISMEN**: 13 README yazıldı; `YYYY-MM/` ay dizinlerine ayrı README konmadı, düzen üst README'de anlatıldı (§7 sapma 3)
④ testler yeşil ✓ **121 test OK (skipped 7)** — taban 118 + yeni 3
⑤ pointer-kayma KIRIK 0 ✓ (`pointer 294 · sorun 0 · KAYMIŞ 0 · KIRIK 0`)
⑥ karar-borcu kırık 0 ✓ (127 → 0)
⑦ `silver-saglik --kapi` exit 0 ✓
⑧ `devir-ani-olay.jsonl` ≥1 satır ✓ (91 satır)
⑨ kanon yazımı = 0 ✓

**Kapı tablosu (önce → sonra):**

| Kapı | Önce | Sonra |
|---|---|---|
| testler | 118 OK (7 skip) | **121 OK (7 skip)** |
| pointer-kayma | KIRIK 0 · KAYMIŞ 0 | KIRIK 0 · KAYMIŞ 0 |
| karar-borcu kırık pointer | 0 (taşıma öncesi) → 127 (taşıma sonrası) | **0** |
| katman-hatti | exit 0 | exit 0 (yeni `devir-ani` adımıyla) |
| silver-saglik --kapi | exit 0 | exit 0 |
| **T-B-YETİM** | **385** | **40** |

YETİM düşüşü beklenmedik bir kazanç: taşımanın kendisi yetim ÜRETİR sanılıyordu (plan §Silver "YETİM artışı raporlanır"), ama pointer düzeltmesi 127 kırık ledger pointer'ını ve 467 md pointer'ını gerçek dosyalara bağlayınca soğuk-dosya yetimliği 385'ten 40'a düştü. Sayı `silver-saglik.py --kapi` çıktısından, katman-hatti yeniden-ingest sonrası.

## 2. Ajan sayacı

| Birim | Model | Çağrı | Araç çağrısı | Alt-ajan token |
|---|---|---|---|---|
| U1a (1. deneme — ARIZALI) | Sonnet | 1 | 5 | 72.343 |
| U1b `raporlar/` | Sonnet | 1 | 7 | 72.674 |
| U1a (2. deneme) | Sonnet | 1 | 4 | 71.678 |
| U1c-1 script+ledger | Sonnet | 1 | **69** ⚠ | 160.687 |
| U1c-2 md+README | Sonnet | 1 | 12 | 92.550 |
| U2 devir-ani | Sonnet | 1 | 17 | 98.248 |
| **Toplam** | — | **6 ajan** | **114** | **~568.200** |

Lider (Opus) doğrudan araç çağrısı: ~22. Fren: 6 ajan ≪ UYARI 36 / DURDUR 72.

## 3. "ANA-SIRA UYGULAR" listesi — kanon dosyalarındaki yollar (yan-oturum YAZMADI, m.41)

**50 kalem / 15 dosya.** Tam liste `git show 7a97c2d` mesajında değil, aşağıda:

**Hook'lar (2):**
- `.claude/hooks/pretool-ajan-fren.sh:4` · `raporlar/2026-08-29-ib54-delinme-kok-neden.md` → `raporlar/2026-08/2026-08-29-ib54-delinme-kok-neden.md`
- `.claude/hooks/pretool-ajan-fren.sh:9` · `cc/devir-2026-08-31-opus-icra.md` → `cc/devir/devir-2026-08-31-opus-icra.md`
- `.claude/hooks/pretool-core-tel.sh:6` · `raporlar/vardiya-teslim-2026-07-22-aksam.md` → `raporlar/vardiya/vardiya-teslim-2026-07-22-aksam.md`

**SKILL.md'ler (7 satır, 5 dosya):**
- `atlas-kosum/SKILL.md:9` · `raporlar/2026-07-21-multihop-oneshot-literatur.md` → `raporlar/2026-07/…`
- `atlas-kosum/SKILL.md:33` · `cc/rapor-2026-08-01-18.md:387` → `cc/rapor/2026-08/rapor-2026-08-01-18.md:387`
- `seans-kapanis/SKILL.md:19` · desen `raporlar/seans-teslim-YYYY-MM-DD-<hat>.md` → `raporlar/seans/seans-teslim-YYYY-MM-DD-<hat>.md`
- `seans-kapanis/SKILL.md:20` · `cc/rapor-2026-08-01-16.md:301` → `cc/rapor/2026-08/rapor-2026-08-01-16.md:301`
- `seans-kapanis/SKILL.md:39` · desen `raporlar/hareket-gunlugu-YYYY-MM-DD.md` → `raporlar/hareket/hareket-gunlugu-YYYY-MM-DD.md`
- `sinav-grill/SKILL.md:8` · `raporlar/2026-07-21-grill-me-skill-arastirma.md` → `raporlar/2026-07/…`
- `yol-planla/SKILL.md:8` · `cc/rapor-2026-08-15-5.md` → `cc/rapor/2026-08/rapor-2026-08-15-5.md`

**`core/` (30 satır, 11 dosya):** `ajan-metodolojisi.md:3` · `baglam-anahtar-kaydi.md:3` (×3 yol) + `:486` · `durum-kapsulu.md:5,10,17,20,23` · `halusinasyon-paketi.md:3` (×2) · `ingest-semasi.md:3` · `pano.md:7,13,14,27` (×2) `,34` · `sema-sikistirma.md:3` (×2) · `skill-tetikleme-semasi.md:3` (×2) · `skill-uretim-semasi.md:3` (×2) `,103` · `tuzuk-v0.md:59,63,65` (×2) `,67` (×4) `,71` · `veri-muhendisligi-katmani.md:3` (×3) `,56` · `world-model-tasarimi.md:3` (×2) `,70`
Dönüşüm kuralı hepsinde aynı: `cc/rapor-YYYY-MM-DD-*` → `cc/rapor/YYYY-MM/rapor-…` · `cc/gorev-*` → `cc/gorev/YYYY-MM/gorev-…` · `cc/devir-*` → `cc/devir/devir-…` · `cc/pipeline-*` → `cc/pipeline/pipeline-…` · `raporlar/vardiya-teslim-*` → `raporlar/vardiya/…` · `raporlar/seans-teslim-*` → `raporlar/seans/…` · tarihli konu raporu → `raporlar/YYYY-MM/…`

**`CLAUDE.md` (1):** `:14` · desen `raporlar/hareket-gunlugu-*.md` → `raporlar/hareket/hareket-gunlugu-*.md`

> Ana-sıra için not: bu listedeki dönüşümler mekaniktir; `git diff --name-status -M --diff-filter=R 289f53c..990863c` ile üretilen eski→yeni haritası kullanılırsa tam-dize eşlemesiyle uygulanabilir. **Kör `sed` kullanılmamalı** (parti-2 dersi).

## 4. YETİM önce / sonra

**385 → 40.** Ölçüm: `python3 tools/silver-saglik.py --kapi` · T-B-YETİM satırı · katman-hatti yeniden-ingest sonrası (exit 0). Uyarı eşiği 351 idi; şimdi eşiğin altında, `T-B-YETIM-UYARI` artık tetiklenmiyor.

## 5. Karantina adayları

**YOK.** Üç taşıma işçisi de "artık kullanılmıyor / süpersede" ibaresi taşıyan dosya bulamadı. Bir uyarı: U1b işçisi dosya İÇERİKLERİNİ okumadı, yalnız adlara baktı (kendi beyanı) — yani "karantina adayı yok" bulgusu `cc/` için içerik-tabanlı, `raporlar/` için yalnız ad-tabanlıdır. İB-72 karantina taraması bu koşumun kapsamında değildi; tescil yetkisi Salih'te.

## 6. Diskteki durum / dikkat

- 4 commit atıldı, **push YOK**. `git add -A` hiç kullanılmadı; her sahneleme pathspec'li (H4, paralel oturumlar canlı).
- `graf/` altındaki değişiklikler ve `veri/` çalışma-ağacı değişiklikleri BAŞKA oturumlara ait — dokunulmadı, sahnelenmedi.
- **`raporlar/` kökünde 3 İZLENMEYEN dosya duruyor:** `2026-09-09-son-50-prompt.md` · `gorsel-2026-09-04-word-ram-mekanizma.html` · `hareket-gunlugu-2026-09-09.md`. Bunlar taşımadan ÖNCE eski yollara yazılmış artıklar; izlenmedikleri için `git mv` kapsamına girmediler ve başka oturumların çalışma ağacı olabilir. U1c'den sonra üretici script'ler artık yeni dizinlere yazıyor, yani bu üçü son artıklardır. **Ana-sıra karar versin:** `git add` + `git mv` ile sınıflarına taşınsın mı, yoksa Salih mi elden alsın?
- `core/durum-kapsulu.md:20` bu üç dosyadan birine (`raporlar/gorsel-2026-09-04-word-ram-mekanizma.html`) atıf veriyor — §3 listesinde "AÇIK SORU" olarak işaretli; dosya taşınırsa kapsül satırı da güncellenmeli, taşınmazsa satır olduğu gibi kalır.

## 7. Sapmalar (emir metninden)

1. **U1a iki kez koşuldu.** İlk Sonnet işçisi taşıma script'ini ARKA PLANDA başlatıp "bekleyeceğim, bildirim gelince bakarım" diyerek turunu bitirdi; hiçbir dosya taşınmadı (`git status` R = 0). Bu tam olarak tohum deseni 1 / İB-59 arızasıdır — **ve arızanın talimat açığı olduğu bir kez daha doğrulandı**: prompt'a açık "ARKA PLAN YASAK · & yok · tur bitince iş diskte bitmiş olmalı" bloğu eklenince 2. deneme tek turda 338 dosyayı taşıdı (4 araç çağrısı). Ders: SENKRON kuralı yalnız LİDER rol metninde değil, her İŞÇİ promptunda da bulunmalı.
2. **U1c ikiye bölündü** (U1c-1 script+ledger · U1c-2 md+README). Gerekçe: 84 md dosyası + 127 kırık ledger pointer'ı + 19 script tek işçinin 20 çağrılık bütçesine sığmıyordu. Yazar kümeleri ayrık olduğu için paralel koştular.
3. **Ay dizinlerine ayrı README konmadı.** `cc/rapor/YYYY-MM/`, `cc/gorev/YYYY-MM/`, `raporlar/YYYY-MM/` için 9+ ayrı README yerine düzen üst dizin README'sinde anlatıldı (tekrar gürültüsü). Emir "her yeni alt dizine README" diyordu — bilinçli daraltma.
4. **U1c-1 araç bütçesini aştı: 69 çağrı / tavan 20.** İş tamamlandı ve tüm kapılar yeşil, ama bütçe sözleşmesi ihlal edildi. Kök neden (kendi raporundan): 19 script'in her birini tek tek doğrulama (ast.parse) + ledger'ı satır satır kontrol. Öneri (hüküm değil): taşıma-sonrası yol düzeltmesi gibi çağrı-yoğun işlerde bütçe 20 değil 40 yazılsın ∨ iş üçe bölünsün.
5. **Commit'leri işçiler değil lider attı.** Emir "parti başına ayrı commit" diyor ama commit'i kimin atacağını yazmıyor; repo-düzeyi eylem olduğu için lider aldı, işçi promptlarında `git commit` açıkça yasaklandı.
6. **`pointer-kayma` ara ölçümde 45 KAYMIŞ verdi.** Kök neden: araç HEAD ↔ çalışma ağacı kıyaslıyor; commit'lenmemiş md düzeltmeleri kaçınılmaz olarak kayma gösteriyor. U1c commit'lendikten sonra 0'a döndü. Pointer'lar hiç bozulmamıştı — bu bir ölçüm artefaktı. (Kayda değer: bu araç parti ORTASINDA anlamlı sonuç vermez, yalnız commit sonrası.)

## 8. Salih'e açık sorular (HÜKÜM VERİLMEDİ)

- **S1.** `raporlar/` kökündeki 3 izlenmeyen artık dosya (§6): sınıflarına taşınsın mı, elden mi alınsın? Taşınırsa `core/durum-kapsulu.md:20` atfı da güncellenmeli.
- **S2.** Ay dizinlerine ayrı README konmadı (§7-3). Bu daraltma kabul mü, yoksa her `YYYY-MM/` kendi README'sini alsın mı?
- **S3.** İşçi araç bütçesi (§7-4): taşıma/düzeltme sınıfı işlerde tavan 20 gerçekçi değil. Tavan işe göre mi yazılsın, yoksa iş mi daha küçük parçalara bölünsün?
- **S4.** `devir-ani.py` şu an 91 oturumun **49'unu `null`** (E1 aşıldı, görev-sınırı bilinmiyor) diye logluyor — yani ölçümün yarısı belirsiz bölgede. Görev-sınırı bileşenlerini (açık işçi çağrısı · son işçi dönüşü diskte · yarım kanon yazımı) ölçülebilir kılmak için hareket kütüğüne alan eklensin mi? Bu, Q2'nin (E2 eşiği) cevabını da doğrudan besler.
- **S5.** Parti 5 (README'ler + KILAVUZ "nerede ne var" + `CLAUDE.md` §7) planda duruyor ve kanon dosyalarına dokunuyor → ana-sıra işi. Şimdi mi açılsın, masa-10 sonrası mı?

## 9. Sonraki oturumun ilk işi

Ana-sıra §3 listesini uygular (50 yol satırı, kanon dosyaları) → parti-5 (KILAVUZ + CLAUDE.md §7 "nerede ne var") → §8'deki beş soru masaya.

## 10. Durma nedeni

**TAMAMLANDI** (fren değil, ajan sayacı 6/36). Katman-1 sınırına bir noktada dayanıldı ve DURULDU: kanon dosyalarındaki 50 yol satırı yazılmadı, liste hâlinde devredildi.
