# veri/ — Bağlam → Veri Tablosu (şema v0, deneysel m.29)

*Silver-katman veri alanı. Üretici: `tools/baglam-tablo.py` (Python 3.9, STDLIB ONLY). Emir: `cc/gorev-2026-08-15-7.md`; hat: `cc/pipeline-2026-08-15-baglam-silver-katmani.md` (S-6 metrikleri bu tablodan sorgulanır). Şema v0 **deneysel m.29** — additive-only evrilir: alan/tablo silinmez, yeniden adlandırılmaz; yeni alan opsiyonel gelir. Damga: 2026-08-15, ship işçisi (lider Carvis).*

## Koşum

```
python3 tools/baglam-tablo.py              # repo kökü = tools/'un üstü; çıktı veri/
python3 tools/baglam-tablo.py --repo <yol> --cikti <dizin> [--sessiz]
```

- Girdi: `git ls-files -z` ile izlenen `.md/.json/.jsonl` dosyaları (çalışma ağacındaki içerik okunur; `core.quotepath=off` — ASCII-dışı yollar dahil).
- Çıktı: `veri/baglam.sqlite` (6 tablo + 7 görünüm) · `veri/baglam.jsonl` (`kayit` satırları, JSON/satır) · `veri/gorunum/<gorunum>.csv` (≤5.000 satır; aşarsa ilk 5.000 + `# UYARI` satırı).
- Git izleme: `baglam.sqlite` ve `baglam.jsonl` **gitignore'lu** (büyük, türetilmiş); `veri/gorunum/*.csv` **izlenir** (küçük gold görünümler) — İ-2 kararı (Carvis 08-15): `v_bolum_yogunluk` (1 MB, kesilen) · `v_anahtar_terim_dosya` (217 KB) · `v_dosya_envanter` (105 KB) de gitignore'lu; izlenen dört CSV: `v_referans_sayim` · `v_kirik_pointer` · `v_zarf_kayitlar` · `v_celiski_adayi` (toplam ≈140 KB). Snapshot çürür; gerçek kaynak = script + commit SHA (5 sn'de yeniden üretim).
- Süre: ~5 sn (433 dosya, 8,1 MB md). Alt-süreç: yalnız `git ls-files`, `git rev-parse HEAD`, tek geçiş `git log --name-status -M -c`. `blob_sha` in-process hesaplanır (`git hash-object` ile birebir aynı: sha1("blob <n>\0"+içerik)).
- Dallar: D1 `git ls-files` başarısız → FAIL-LOUD çıkış 2 · D2 UTF-8 açılamayan dosya → `dosya.tur=diger`, `okunabildi=0`, kayıt üretilmez, `uretim.notlar.utf8_hatasi`'na yazılır · D3 zarf 5 zorunlu alandan azıyla eşleşirse → `zarf_json={"kismi": true, …}`, `zarf_*` alanları boş · D4 aynı `kayit_id` ikinci kez üretilirse → sona `~2`, `uretim.notlar.kayit_id_cakisma` sayacı.
- Determinizm: tek zaman alanı `uretim.uretim_zamani`; `uretim.sure_sn` ölçümdür. CRLF → LF normalize edilir, BOM düşer (aynı içerik farklı checkout'ta aynı `kayit_id`).

## İdempotens kanıtı (2026-08-15, HEAD `c5f15ea`)

Script iki kez art arda koştu (script_sha `07e450a7…`); karşılaştırma: `kayit_id` kümesi (37.668 satır) **fark 0**; `veri/baglam.jsonl` byte-özdeş (`cmp`); `referans` (42.944) · `anahtar` (312) · `dosya` (433) · `json_kayit` (1.821) tablo dökümleri özdeş; `veri/gorunum/*.csv` 7/7 özdeş (`diff -r`). `uretim.kayit_id_kume_sha` = `3905dfa71de2523b6b68ad64dd51f38930002e72` her iki koşumda. Yalnız `uretim.uretim_zamani` ve `sure_sn` (5,06 vs 5,07 sn) farklı. Yeniden doğrulama: iki koşum arasında `sqlite3 veri/baglam.sqlite "select kayit_id_kume_sha from uretim"` değerini karşılaştır.

## Şema v0 (SQLite; alan adı talimattır — Türkçe)

### `dosya` — dosya envanteri (1 satır / izlenen dosya)
`dosya_id` (repo-göreli yol, PK) · `dizin` (ilk segment; kök için `.`) · `katman` ∈ {sicak, ilik, soguk, yapisal} · `tur` ∈ {kanon, kapsul, pano, tuzuk, skill, eval, wiki, sozluk, kuyruk, gelen, defter, rapor, teslim, emir, pipeline, ders, kutu, log, diger} · `boyut_bytes` · `satir_sayisi` · `blob_sha` · `ilk_commit` / `son_commit` (ISO, `%cI`; izlenmiyorsa `-`) · `baslik` (ilk `# ` satırı; yoksa dosya adı) · `token_kestirim` (bytes/4) · **ek (v0.1 additive):** `uzanti` · `okunabildi` (0/1, D2).

**Katman kuralı (sıralı):** json/jsonl → `yapisal` · `CLAUDE.md`, `core/*`, `.claude/skills/*/SKILL.md` → `sicak` · `raporlar/*`, `cc/rapor-*`, `cc/gorev-*`, `ogrenme/*`, "model değişikliği…" klasörü, arşiv (`*/arsiv/*`, `arsiv-*`, `*-arsiv*`) → `soguk` · `kuyruk/*`, `wiki/*`, `fikir-kutusu.md`, `cc/pipeline-*`, `cc/defter.md`, kök md'ler, `.claude/**` (SKILL.md dışı md: references/agents), `cc/README.md` → `ilik` · kalan → `soguk`.
**Tür kuralı:** yol+ada göre (`tur_bul`): `CLAUDE.md`→kanon · `core/durum-kapsulu.md`, `*KAPSULU*`→kapsul · `core/pano.md`→pano · `core/tuzuk*`→tuzuk · diğer `core/*` (şemalar, şablonlar)→kanon · `.claude/skills/**` md→skill, `evals/*.json`→eval · `wiki/sozluk.md`→sozluk, `wiki/*`→wiki · `kuyruk/gelen-*`→gelen, `kuyruk/*fikir-kutusu*`→kutu, `kuyruk/*defter*` (sema hariç)→defter, diğer `kuyruk/*`→kuyruk · `cc/defter.md`→defter · `cc/gorev-*`→emir · `cc/rapor-*`→rapor · `cc/pipeline-*`→pipeline · `raporlar/vardiya-teslim-*`→teslim, `raporlar/**.jsonl`→log, diğer `raporlar/*`→rapor · `ogrenme/dersler/*`→ders · "model değişikliği…"→log · `fikir-kutusu.md`→kutu · adı "rapor" içeren→rapor · `.claude/settings.json`, `.mcp.json`→diger · belirsiz→diger.

### `kayit` — markdown blok kaydı (1 satır / blok)
`kayit_id` = `<yol>#<satir_bas>-<satir_son>#<sha1(metin)[:8]>` (PK) · `dosya_id` · `sira` (0..n) · `bolum_yolu` (H1 › H2 › H3, " › " ile; H4+ başlıklar kayıt olur ama yola girmez) · `blok_turu` ∈ {baslik, paragraf, madde, tablo_satiri, tablo_baslik, kod, alinti, yatay_cizgi, frontmatter} · `satir_bas`, `satir_son` (1-tabanlı) · `metin` (ham blok; kod bloğu tek kayıt; `tablo_baslik` = başlık satırı + ayraç satırı; `madde` = madde + girintili devam satırları) · `metin_kisa` (ilk 200 karakter, tek satır) · `token_kestirim` (utf-8 bytes/4, yukarı yuvarlı) · `tarih_ipucu` (metindeki EN ERKEN konumdaki tarih: `YYYY-MM-DD` ∨ `DD-MM` ∨ `MM-DD`, bulunduğu hâliyle; kısa biçimde iki parçadan biri ≤12 olmalı) · `tarih_iso` (yalnız tam tarihse) · zarf alanları: `zarf_tip`, `zarf_kaynak`, `zarf_tarih`, `zarf_hedef`, `zarf_sema`, `zarf_onem`, `zarf_gecerli_bitis`, `zarf_json` (tüm zarf alanları JSON; ilk `[tip: … | … ]` zarfı — köşeli-parantez derinliğiyle kapanır, `baglanti: [[x]]` bozmaz; anahtarlar Türkçe-ASCII katlanır: `geçerli-bitiş`≡`gecerli-bitis`) · `madde_derinlik` (liste girintisi/2; tab=4).

### `referans` — kayıt içi atıflar (n satır / kayıt)
`kayit_id` · `ref_turu` · `ref_deger` (normalize) · `ham` (eşleşen metin) · `konum` (metin içi offset) · **ek (additive):** `hedef_var` (0/1; yalnız dosya_pointer) · `hedef_yol` (çözülen repo yolu).
Türler: `tuzuk_madde` (`m.N`/`md.N` ayrı; harf eki korunur: `m.40b`) · `v_no` (`V\d+`, büyük V) · `kart` (`K-\d{3}`) · `wiki_link` (`[[hedef]]`, `#`/`|` sonrası atılır) · `dosya_pointer` (`.md/.py/.d2/.svg/.json/.jsonl/.sh/.ps1` uzantılı yol-biçimli token; URL içi maskelenir; `\` sonrası (Windows yolu) ve `-12.md` kısaltmaları alınmaz; normalize: `~/jarvis/`, `/…/jarvis/`, `C:/JARVIS/`, `./`, `../` önekleri düşer; çözüm sırası: repo yolu → kaynak dosyanın dizinine göreli → çıplak ad ise repo'daki ilk eş-adlı dosya) · `skill_adi` (`.claude/skills/*` klasör adlarıyla birebir, büyük/küçük duyarsız; `damıtma`≠`damitma` — Türkçe katlama YOK) · `sha` (7-40 hex, ≥1 harf; 7-12 hex yalnız ±40 karakterde `commit|sha|git|head|revert|hash|blob|push|merge|`` ` komşuluğu varsa) · `tarih` (ISO tam, ay/gün aralık kontrollü) · `url` (http/https) · `etiket` (`[D]`/`[K]`/`[X]`/`[ARANAMADI]`/`[?]`) · `anahtar_terim` (v0 seed listesi; **büyük/küçük ve Türkçe-ASCII duyarsız** — metin uzunluk-koruyan 1:1 haritayla katlanır, offset'ler geçerli kalır; Türkçe ek kuyruğu kabul edilir: kapsülden/vardiyayı/şemasının/skill'i sayılır, "semantik"/"panorama"/"stajyer" sayılmaz).
**anahtar_terim kanonik değerleri (27):** gunaydin · seans basi · seans bitimi · uyucam · vardiya · kapsul · pano · tuzuk · damitma · ingest · zarf · atlas · antitez · hakem · workflow · pipeline · skill · halusinasyon · sema · staj · cowork · terminal · ana-sira (ana-sıra ∨ ana sıra) · yan-oturum · katman-1 (Katman-1 ∨ Katman 1) · katman-2 · celiski (emirdeki "m.16 çelişki|celiski" → terim `çelişki`).

### `anahtar` — gözlenen anahtar kaydı (seed; otomatik türetilir)
`anahtar_id` (`<tur>:<deger>`, PK) · `tur` ∈ {skill, kart, tuzuk_madde, v_no, anahtar_terim, wiki_sayfa} · `deger` · `kaynak_dosya` (skill→SKILL.md yolu; kart→`core/pano.md`; tuzuk_madde→`core/tuzuk-v0.md`; wiki_sayfa→sayfa yolu ya da `-` (sayfası olmayan `[[link]]`); diğerleri `-`) · `durum`="gozlenen" (v0'da hepsi) · `replaced_by`, `gecerli_bas`, `gecerli_bitis` (VAR, BOŞ — SH-9'da `core/baglam-anahtar-kaydi.md`'den dolar) · `referans_sayisi` · `sicak_referans_sayisi` · `ilk_gorulme`/`son_gorulme` (emir gereği: atıf yapan dosyaların `son_commit` değerlerinin min/max'ı). Kapsam: tüm skill klasörleri, tüm seed terimler (0 atıflı olsa da), gözlenen kart/madde/V-no değerleri, wiki sayfaları ∪ gözlenen `[[link]]` hedefleri.

### `json_kayit` — düzleştirilmiş JSON/JSONL
`dosya_id` · `satir_no` (jsonl için 1-tabanlı; json için NULL) · `json_yolu` (JSON pointer: `/tests/0/id`; `~0`/`~1` kaçışlı) · `deger` (skaler string) · `deger_tipi` ∈ {string, number, boolean, null}. Boş dizi/nesne satır üretmez. **Hariç:** `.claude/settings.json`, `.mcp.json` (yalnız `dosya`'da adları). Bozuk JSON → `uretim.notlar.json_hatasi`.

### `uretim` — tek satır koşum künyesi
`uretim_zamani` (tek zaman alanı) · `git_head_sha` · `dosya_sayisi` · `kayit_sayisi` · `referans_sayisi` · `sema_surumu`="v0" · `script_sha` (script dosyasının sha1'i) · **ek:** `anahtar_sayisi` · `json_kayit_sayisi` · `sure_sn` · `python_surumu` · `kayit_id_kume_sha` (sıralı `kayit_id` listesinin sha1'i — idempotens karşılaştırma anahtarı) · `notlar` (JSON: utf8_hatasi / json_hatasi / kayit_id_cakisma / csv_kesildi).

## Görünümler (gold; SQL VIEW + `veri/gorunum/*.csv`)
- `v_referans_sayim` — ref_turu × ref_deger: toplam, sicak, ilik, soguk, dosya_sayisi (toplam↓).
- `v_anahtar_terim_dosya` — anahtar_terim × dosya (katman, tur, sayi). "günaydın kaç dosyada?" → `SELECT count(*) FROM v_anahtar_terim_dosya WHERE anahtar_terim='gunaydin'`.
- `v_zarf_kayitlar` — zarflı kayıtlar (tam ve kısmi; tip/kaynak/tarih/hedef/sema/onem/gecerli_bitis + zarf_json).
- `v_dosya_envanter` — dosya × katman/tur/boyut/satır/token/ilk-son commit/blob_sha/başlık.
- `v_bolum_yogunluk` — dosya × bolum_yolu: kayıt sayısı, token toplamı, satır aralığı (CSV'de 5.000 satır tavanı aşılır — tam küme sqlite'ta).
- `v_kirik_pointer` — `dosya_pointer` olup repo'da (izlenen ∨ diskte) bulunmayan yollar: yol, `yol_bicimi` ∈ {yol, ciplak_ad}, sayi, dosya_sayisi, ilk_dosya, ilk_kayit. `ciplak_ad` (AGENTS.md, MEMORY.md…) çoğunlukla dış-dünya araştırma atfıdır; `yol` biçimliler gerçek adaydır (ör. `core/baglam-anahtar-kaydi.md` — henüz yazılmamış SH-9 dosyası).
- `v_celiski_adayi` — aynı anahtar_terim için, aynı dosyada, ZARFLI kayıtlar arasında `zarf_gecerli_bitis` dolu VE boş olanların birlikte bulunması (kaba v0; zarf sayısı düşükken çoğu koşumda boş).

## Bilinen sınırlar (v0)
- Markdown ayrıştırma satır-tabanlı ve CommonMark'ın alt kümesi: setext başlık yok (`---` her yerde yatay çizgi/frontmatter kapanışı), HTML blokları paragraf sayılır, liste devam satırı yalnız girintiliyse maddeye yapışır, tablo ayraç satırı `tablo_baslik` bloğuna dahildir.
- Boşluk içeren yollar (`~/staj başlangıç/…`, "model değişikliği…" klasörü) `dosya_pointer` olarak parça yakalanır (`başlangıç/ingest-semasi.md`); `dosya_id` tarafı sorunsuzdur.
- Bir kayıtta yalnız İLK zarf ayrıştırılır; şablon zarfları (`[tip: … | … ]`, `<yüzey+hat>`) gerçek zarf gibi tam sayılır.
- `anahtar_terim` ek-kuyruğu sezgisel: nadir yanlış-pozitif/negatif olabilir (ör. `sema:` zarf anahtarı terim sayılır; "terminals" sayılır).
- `sha` 7-12 hex komşuluk kuralına bağlı; `git cat-file -e` doğrulaması yapılmıyor (opsiyonel bırakıldı).
- `ilk_commit`/`son_commit` HEAD soyağacından tek geçiş (`-M -c`: rename zinciri + merge'de çözülen dosyalar dahil); `--follow` ile birebir aynı olmayabilir.
- `anahtar.ilk_gorulme` emir gereği `son_commit` min'idir (bir terimin gerçek ilk görüldüğü commit değil) — S-6'da `ilk_commit` tabanlı alternatif değerlendirilmeli.
- Emirdeki `git ls-files | grep -E '\.(md|json|jsonl)$'` sayımı 431 verir çünkü git ASCII-dışı yolları tırnaklar (`core.quotepath`); `-z` ya da `-c core.quotepath=off` ile 433 = `dosya` satır sayısı.

## Şema evrimi (öneri; additive)
`kayit.baslik_seviye` · `referans.baglam` (±40 karakter pencere) · `anahtar.durum` değerleri {gozlenen, aktif, deprecated} + `replaced_by` (SH-9) · `dosya_pointer` için `yol_bicimi` alanının tabloya inmesi · `json_kayit`'ta boş kap satırı (`deger_tipi=bos`) · terim listesi `veri/anahtar-terimler.json` dış dosyasına (koda gömülü liste yerine).

## Katmanlar (veri-mühendisliği katmanı v1 — 2026-08-16, deneysel m.29; kanon `core/veri-muhendisligi-katmani.md`)
Katman = KOŞUL, ad değil (yüklemler kanon §2). **BRONZ** = git-izlenen md/jsonl/json + koşum kütükleri (provenans = commit) · **SİLVER** = bu klasördeki `baglam.sqlite` tabloları (1:1 grain, tipli, tekil, agrege-olmayan, türetilmiş — iki damga: kod SHA + `uretim.git_head_sha`) · **GOLD** = `gorunum/*.csv` + `v_*` görünümler (her metrik tek yerde; agregasyon yalnız burada).
- `sozlesme/<tablo>.json` — şekil sözleşmeleri (kolon+tip; additive-only; kırıcı = silme/tip/kısıt/yeniden-ad). Üretim: `python3 tools/katman-olcum.py --sozlesme-yaz` (yalnız ilk kurulum/sürüm artışında).
- `katman-olcum.jsonl` — APPEND-ONLY ölçüm kütüğü (grain: 1 satır = 1 ölçüm olgusu: volume · oran silver/bronz, gold/bronz · veri-testi · sözleşme preflight · freshness). Üretim: `python3 tools/katman-olcum.py` (çıkış 3 test-error · 4 kırıcı sözleşme · 5 freshness-error). Oran-eşiği k=3 koşumdan sonra önerilir. İlk koşum 08-16: bronz 466/9,5 MB · silver 44,0 MB (kayit.metin 8,2 MB) · gold 11/2,91 MB · silver/bronz 4,64×.
- `yetkinlik-haritasi.jsonl` — öğrenme-değeri conformed boyutu (DEA-C01 domain'leri; kalem etiketi kavram/beceri ↔ servis-adlı; domain-% hesaplanmaz) · `de-pratik.jsonl` — pratik birimi olgu tablosu (geri-bildirim sinyalsiz birim sayılmaz).
- **Hat sırası (sözleşme): `python3 tools/katman-hatti.py`** = `baglam-tablo.py` (silver çekirdek; tmp→replace ile SIFIRDAN yazar) → `karar-borcu-tablo.py` (bronz `karar-borcu.jsonl`) → `prompt-tablo.py` (bronz `bronz/prompt-olay.jsonl` ← jarvis transkriptleri; silver `prompt`; gold `v_son_50_prompt` + `raporlar/<tarih>-son-50-prompt.md`) → `katman-olcum.py`. Sonradan eklenen her silver tablo kendi bronz kaynağından deterministik yeniden yüklenir (functional DE); yeni yükleyici listeye EKLENİR. `bronz/` = repo-dışı koşum kütüklerinden repoya alınan ham+provenanslı olay kütükleri (append-only; tekil anahtar kaynak uuid).
- **Bağlam veri ambarı v0 (`amb_*`, aynı sqlite; `tools/ambar-tablo.py`, hat adım 4):** `amb_olgu_kosum` (bronz `bronz/kosum-olay.jsonl` ← alt-ajan transkriptleri; 1 satır = 1 ajan koşumu, ham usage token) · `amb_olgu_prompt` · `amb_olgu_karar_borcu` (bitemporal: system_time + valid_time) · görünümler `amb_boyut_anahtar` (SCD-2) · `amb_kopru_olay_nesne` (factless+qualifier) · `amb_boyut_vardiya` · martlar `v_amb_kosum_maliyet` · `v_amb_acilis_brifi` (as-of) → `gorunum/v_amb_*.csv`. Tanım: `wiki/baglam-veri-ambari.md`; ilk çıktı: `raporlar/2026-08-16-baglam-ambari-v0.md`.
