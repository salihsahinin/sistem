# KILAVUZ.md — JARVIS Kullanım Kılavuzu (v1)

> **Açıklama notu:** K-012 build adım 2 çıktısı (2026-07-12; m.26: anlama-kapısı yerine kılavuz — Salih buradan okur, takıldığı yerde Jarvis izah eder). Format deneysel-damgalı başlar (m.29), kullanım verisiyle kalibre edilir. Kural kaynağı her zaman tüzük; burası "nasıl kullanılır" yüzeyidir.

## Oturum nasıl işler
- **"seans başı"** (eski selamlama tetiği emekli 08-15, `core/baglam-anahtar-kaydi.md`) → seans açılışı: kapsül + pano okunur, kısa teslim özeti + tek net sıradaki iş sunulur.
- İş sırasında ne söylersen görev olarak devralınır (m.25); küçük iş direkt yapılır, proje ölçekli işe kart/ajan — ölçek-tercihi Jarvis'te.
- **Kapanış ("seans bitimi"):** seans teslim + hasat/ingest + kapsül güncellenir + commit; push m.9 gereği Salih beyanıyla. Jarvis bağlam-şişmesinde kapanışı kendisi önerir (V11).
- **Bağlam-şişme çağrısı (Salih emri 07-19):** Jarvis, oturum bağlamının şiştiğini ve kalite riskini gördüğünde bunu **kendiliğinden** belirtir; seans kapanışı + yeni seans önerir (kapanış = teslim raporu + kapsül tazeleme; yeni seans kapsülden devralır — m.27 hattı).
- Her karar ayrı commit, [damıtma]/[icra] (+[ariza]/[revert], Karar 55); push **yalnız** Salih beyanıyla (m.9; eski 'otomatik push' satırı süpersede — arşiv §3).
- **Ağır araç yükleme usulü (Salih imzası 08-17 masa KB-12; ölçüm `raporlar/2026-08/2026-08-03-model-dusumu-olcum.md`):** çoklu MCP/ToolSearch yüklemesi oturum **başında** ya da **ayrı** oturumda; uzun oturumun geç evresinde **yapılmaz** (prompt-cache kırılması ~152K token → kota → düşüm).

## Nerede ne var — hangi soruya hangi dosya (Friday parti-5 devri 09-09, yerleştirme 09-10; CLAUDE.md §7 klasör listesi, burası soru→dosya)

Klasörlerde *ne* olduğu için `README.md` klasör haritasına bak (m.20: burada tekrar edilmez). Bu bölüm *hangi soruyu sorduğunda hangi dosyayı açacağını* söyler: soruyu soldan bul, ilk açılacak dosyayı sağdan al, derine inmen gerekirse o dosyanın pointer'ını izle.

| Soru | İlk açılacak |
|---|---|
| Bugün nerede kaldık, sıradaki ilk iş ne? | `core/durum-kapsulu.md` |
| Hangi iş açık, kim üstünde, `DONE` ne? | `core/pano.md` |
| Bu kural nereden geliyor, kim karar verdi? | `core/tuzuk-v0.md` → `kuyruk/senaryo-defteri.md` |
| Bu seansta ne teslim edildi? | `raporlar/YYYY-MM/` (ay dizini README'si) |
| Bu ajana ne emredildi, ne cevap verdi? | `cc/gorev/YYYY-MM/` → `cc/rapor/YYYY-MM/` |
| Bu terim ne demek? | `wiki/sozluk.md` |
| Bu rakam nereden çıktı? | `veri/` + `tools/SCRIPTLER.md` |
| Emekli / eski içerik nereye indi? | `arsiv/README.md` |

Ayrıntı her zaman dizinin kendi `README.md`'sindedir; bu tablo yalnız kapıyı gösterir. Dosya adındaki tarih AS-OF damgasıdır (Karar 88 M4). Hiçbir şey silinmez: emekli içerik `arsiv/` altına iner ve yerinde pointer bırakır (m.8).

## Paralel seans protokolü (Salih kararı 2026-07-12 sabah; m.36 revizyonunun operasyonel devamı — deneysel damga m.29)
- **Eski iki-chat modeli (Cowork/Windows dönemi) arşive indi** (damıtma 08-29 → `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2026-08-29.md` §1); canlı düzen aşağıdaki Karar 71 satırı + wiki 4-kural.
- **KURAL (Salih imzası 08-17 masa KB-08/09/10):** çoklu oturumun 4 kuralı `wiki/paralel-oturum-protokolu.md` — canlı-oturum kapısı · koşum-önü manifest kapısı · paylaşılan kaynak/motor freni · **`git add -A` yasak, `git add <yol>`** (H4).
- **ÜÇ-KATMAN çok-oturum düzeni (Karar 71, 08-26; PR-per-chat `RET`; tam gerekçe defterde):** (1) kanon+karar+push **tek** ana-sıra oturumda; yan-oturum karar almaz, `kuyruk/devir-*.md` bırakır · (2) kod-sınıfı paralel iş treehouse worktree ∨ no-mistakes PR hattı · (3) commit **sop**: hedefli `git add <yol>` + pathspec'li commit (vaka-5) + her resume'da git-log kapısı (Karar 57).

## Arşive inenler (damıtma 08-17) — üçlü sohbet düzeni · CC kanal modeli · CC-geçiş S2 hibrit-matris · Mobil Köprü Protokolü → tam metin `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2026-08-17.md`

## Emir ve soru dili
- Ne dersen emirdir; önceki kararla çelişki varsa önce çelişki raporu gelir (m.16).
- **Yanılma-yönü dili (Karar 79 D3/KL18-9):** "yanlış-pozitif/yanlış-negatif" terim çifti kullanılmaz (iki alanın konvansiyonu ters çalışır); yerine "hangi yönde yanılır" yazılır.
- **Çıktı-dili soru formatı + framing koruması (V6):** Jarvis sana soru sorarken seçenekleri somut **sonuç** örnekleriyle sunar ("A seçilirse şu olur") ve soru cümlesi yönlendirme içermez — seçenekler yansız yazılır; Jarvis kendi önerisini ayrıca, gerekçesiyle işaretler (m.6).
- **Kapasite cevabı üç halden biri (#9):** "yaparım" (direkt yapılır) · "yapamam" (neden + ne gerekirdi) · "proje gerekir" (kart açılır, kaba token×zaman tahmini verilir). Belirsiz "bakarız" cevabı yasak.

## Kart ve kutu kuralları
- **DONE kuralı (Salih onayı 07-12):** yazılabilir, doğrulanabilir `DONE` tanımı olmayan kart açılmaz. İyi örnek: "pytest yeşil + push". Kötü örnek: "İngilizceyi geliştir". Loop dönemi karşılığı: durma koşulu yazılamayan loop kurulmaz.
- **Çürüdü-işareti (Salih onayı 07-12):** fikir kutusunda 30 gün işlenmeyen madde "`BAYAT`" damgalanır; düşme **yalnız** Salih onayıyla (m.8 otomatik-silme yasağı korunur).
- **Gürültü listesi (deneysel):** kutuya **dosyalanmaz** → model/sürüm duyuruları (somut yetenek yoksa) · kaynaksız prompt numaraları · araç-haber gürültüsü · kurulum-kopyası. **istisna**: Salih 'araştır' emri listeyi ezer. Pozitif karşılık (md.22): takılan kalem tek satır pointer'la teslim-notuna.

## Tasarım ilkeleri (sıkıştırılmış 09-04; tam gerekçeler + Salih aynen-beyanları `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2026-09-04.md` §1)
- **Yapı-darboğazı yerleşim (Salih imzası 08-29, Karar 79 D3/KL18-13; kaynak `cc/rapor/2026-08/rapor-2026-08-01-18.md:389`):** yerleşim/öncelik talep verisinden değil yapının darboğazlarından ("işler nereden geçiyor"); ölçüm: talep-bazlı greedy 6,7-7,9× çöker, topoloji-bazlı değişmez.
- **Tarama-yöntemi seçimi (KB-57 A, 08-21, Karar 64):** anahtar varsa **search** · küçük tablo tam agregasyon **scan** · çok-kolon agregasyon → parquet/DuckDB · bronz metin → rg · keşif → **sample** · silver yenilemesi sonrası `ANALYZE` · **automatic index** → kalıcı indeks adayı · **like** önek → aralık; karar değişkeni **dokunulan sayfa** (yüzde-eşiği yazılmaz). Tarif `wiki/tarama-yontemleri.md`.
- **Adresli erişim (KB-53/54 A, 08-21, Karar 62; ölçüm 27-563× token):** adres varsa **aralık** oku; anahtar varsa silver blok (sha8 yeniden hesaplanır, tutmazsa dosyaya düş + bayrak); bütün dosya yalnız adressizken; silver tazeliği açılış kapısında; sayaç İB-29.
- **Graf-dili v0 (KB-60 A, 08-22, Karar 67):** graf `graf/` script-türetimli d2+svg (`tools/pointer-graf.py`; elle düzenlenmez); düğüm adı = D2 anahtarı; yapısal soru SQL, yorum panoya; sürüm+sha `graf/pointer-sistemi-v0-uretim.json`; plan `raporlar/2026-08/2026-08-22-graf-dili-uzun-vade-plani.md` §1.
- **Dil-seçimi (KB-64 A, 08-26, Karar 69):** kural kaynağı `wiki/dil-secimi.md`; 9 sınıfın 7'si Python-stdlib+bash, Go/Rust yalnız MCP/dış-dağıtım tetiğinde, **cue** girmez; dil geçişi **otomatik değil** — Salih masası (şerh aynen arşivde).
- **GİRMEZ — agile pratikleri (KB-49 A, 08-21, Karar 56):** story point · velocity · planning poker · flow efficiency · **sle** olasılık beyanı · daily standup · "Sprint" adı; kaldırma Katman-1; gerekçeler arşivde.
- **Alt-ajan içerik-karantinası (Karar 54b, 08-21; m.29):** dış/hacimli içerik ana bağlama girmez — alt-ajanda işlenir, özet+pointer döner.
- **Öğretim taban-yoklaması adım-0 (Karar 54g, 08-21):** yeni konudan önce Salih'in terim tabanı yoklanır, anlatım seviyelenir.
- **Sürtünmesizlik (#18):** sık akışın çağrısı kolay + çapalı; ilk soru "çağırmak kaç saniye sürer?"
- **Bayat-kapsül riski (V4):** yanlış kapsül boş kapsülden kötü; kapanış disiplini atlanmaz.
- **Jarvis-içi araç sınırı (E-1, Karar 76, 08-29):** no-mistakes + treehouse **serbest** · gnhf **koşullu** (worktree ∧ yazılı bütçe ∧ push kapalı) · hiçbir otomat kanona (core/ · CLAUDE.md · tüzük · defter) yazamaz.
- **HAZIRI temel AL (Salih Katman-1 08-17 KB-14; V25 tersine):** hazır araç/yöntem/metrik varsa onu temel al, sıfırdan benzerini yazma; seçim ölçütü yıldız-yasağı üçlüsü; istisna gerekçeli (m.16). Salih örneği (WezTerm) arşivde.
- **Ölçek şerhi — V1 iterasyon > spec-first (08-17 KB-14):** m.25 eşiği üstü çok-ajan/otomasyon işinde intake spec-önce olabilir; altında iterasyon esas. Spec-kit kurulmadı, deseni alındı.
- ~~**Metafor haritası (V12)**~~ `EMEKLİ` 08-17: terimler metaforsuz, tek anahtar (`core/baglam-anahtar-kaydi.md`); sözlük `DONDU` (m.3).
- **md yüzeyi — insan-yüzü rapor biçimi:** QuickLook **iptal** (Karar 72) → Obsidian → **VS code (Karar 80, 08-29; update 09-04 — eski satır Obsidian diyordu)**; **gfm** tablo · görev kutusu · ```mermaid · dipnot · `<details>` · `[[wikilink]]` · `$matematik$` serbest; ilk-12-satır damga kuralı baki; HTML teslim etkilenmez. Link biçimi ileri-dönük md-link (Karar 72 EK, seçim A), geçmiş gövde yeniden yazılmaz (m.8); türev harita `tools/obsidian-harita.py`.
- **Yıldız yasağı (md.33, Salih imzası 08-01):** GitHub yıldızı ölçüt olamaz; adaylar indirme-sırası + son-sürüm + bakımcı üçlüsüyle tablolanır; reddedilen "şu an alınmaz" listesine (md.34).
## ~~Skill-yazım standardı (K-013)~~ arşive indi (damıtma 08-29 → `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2026-08-29.md` §4); canlı standart aşağıdaki 'Skill Standardı' bölümü + oradaki eval kuralı.
## Boyut-izleme — sıcak-dosya bütçesi (imzalı kural, Salih 07-22; rakamlar deneysel m.29)
Her oturum açılışında okunan dosyalar sabit boyut-bütçeli yaşar; **aşım hata değil tetiktir** — aşan dosya ilk boş seansta Salih-imzalı planla damıtılır (silme yok: tam metin arşive, özüt+pointer; m.8/m.34). Bütçeler: kapsül 8KB ∧ ≤40 satır (hook sert-kapısı) · pano 12KB · fikir-kutusu 20KB · senaryo-defteri 48KB (`FLAG`: token-bazlı yeniden-bütçe adayı) · CLAUDE.md 8KB · KILAVUZ 16KB. Kapanışta tek bakış; aşan varsa teslim raporuna 'boyut-tetiği' düşer. Revizyon tetiği: context-ekonomisi değişimi; iki turda bir kalibrasyon. Gerekçe + araştırma tarihçesi: `kuyruk/k019-taslak-boyut-izleme.md` + arşiv 08-29 §2. **konum** ekseni: her-tur-okunanlar bağlam tepesinde (lost-in-middle).

## Sayı-araştırma kapısı (Salih emri 07-23 — kural)
Sistem parametresi olacak her deneysel sayı (eşik, bütçe, sayaç, örneklem) CC araştırması koşulmuş-ve-okunmuş bağlamda seçilir (m.40'ın sayılara genişletilmesi). Araştırmasız mevcut sayılar **geçici** damgayla yürürlükte; rapor gelince yeniden türetilir/onaylanır, fark deftere. Envanter: `raporlar/2026-07/2026-07-23-deneysel-sayi-denetimi.md` · ilk tur: `cc/rapor/2026-07/rapor-2026-07-23-1.md` (4 hüküm uygulandı). Kalite-proxy'ler (m.39) kapının konusu değil — onların yolu ölçüm.

## Öz-usage usul kuralı (Salih beyanı 08-01 sözlü → metinleşme Salih imzası 08-01 masa)
Salih'in kendi /usage, /context ve bağlam-doluluk yorumları **yorum** statüsündedir, karar/ölçüm değil ("bağlam şişti" beyanı tek başına eşik tetiklemez — 08-01-2: doz-cevap yok). İterasyon yönünü üst model verir; Salih veto her zaman açık (m.31). Ölçüm hattı: Yol-1 bağlam-sayacı kurulunca beyanlar veriyle kalibre edilir.

## Durum görünürlüğü (m.18)
Her iş cevabının sonunda insan-yüzü tek satır (`▸ Şu an · Sıra · Açık`); "şu an ne yapıyoruz" dersen anlaşılır dilde detaylı durum raporu dosyası üretilir; makine-yüzü kapsül/pano/şablonlarda yaşar.

## Model-değişimli oturum protokolü (Salih imzası, 2026-07-13 — kural, deneysel değil)
Oturum ortasında model değişikliği yaşanırsa o oturumun orijinalliği bozulmuş sayılır: ingest'i kanon-yüzeyine değil şerhli klasöre yazılır — `arsiv/chat-model-degisikligi/ingest-YYYY-MM-DD.md` (eski klasör adı "model değişikliği ile orijinalliği bozulmuş olan chat/", parti 1 taşıması 2026-09-09). Buradaki içerik **şerhli kopya** statüsündedir; çelişki durumunda commit'li kanon (fikir kutusu / kuyruk / kapsül) kazanır. Şerhli içeriğin karar statüsü kazanması için ayık/temiz oturumda taranıp normal kanon yoluna işlenmesi gerekir. Gerekçe: bağlam hijyeni (07-13 vakasının standartlaşması).

## Skill Standardı (K-016 açılışı 07-19; el kitabı: `raporlar/2026-07/2026-07-17-skill-nasil-olusturulur.md` — burası özet, çelişkide rapor + code.claude.com/docs kazanır)
- **Eval kuralı (Salih onayı 07-12; revizyon Salih imzası 07-23 — kaynak `cc/rapor/2026-07/rapor-2026-07-23-1.md`):** her JARVIS skill'i eval setiyle doğar. Küçük-N eval = **SMOKE/regresyon-kanaryası, sertifika değil** — çıplak "%100 geçti" raporu **yasak**; sonuç aralığıyla (Clopper-Pearson: 6/6→[%54,%100]) ya da "smoke-only" ibaresiyle verilir. Yeni setlerde: negatif ~10 (pariteye yaklaş — 3 negatif yanlış-pozitifi bağlamaz) + her vaka ≥3× koşum (non-determinizm ilacı; vaka eklemekten ucuz). 20-sorgu description-eval skill-creator protokolüne **tam** hizalı: 8-10 should + 8-10 should-not · her sorgu 3× · 60/40 held-out · ≤5 iterasyon. Mevcut skill'lere geriye dönük eval soğuk kuyrukta. *(md.22 pozitif karşılığı fiilen bu maddede tanımlı — aralıkla ya da smoke-only ibaresiyle ver; imza kaydı 08-20 KB-28.)*
- **Eval-önce akış:** önce ≥3 senaryoluk `evals/evals.json` + baseline (skill'siz koşum), **sonra** minimal gövde; description ince-ayarı EN **son**. Eval'siz yayın `YOK`.
- **Description:** 3. şahıs · NE + NE **zaman** (gerçek kullanıcı ifadeleriyle) + **negatif** tetik ("X'te kullanma") · ≤1024 karakter.
- **Gövde:** <500 satır · emir-kipli numaralı adım · tek sorumluluk · "Gotchas" bölümü en yüksek sinyal · detay `references/` (bir seviye derin).
- **Yan-etki freni (★):** kayıt/commit/deploy adımı **ayrı** `disable-model-invocation: true` skill'e — muhakeme skill'i blok **üretir**, dosyaya **yazmaz** (m.31/m.9 koda gömülü).
- **Kompozisyon:** skill'ler birbirini literal çağırmaz; bileşik iş = `context: fork` orkestratör + küçük çocuk skill'ler + sabit-format handoff + fail-loud.
- **Yayın-öncesi:** 20-sorgu description eval (10 tetiklemeli + 10 tetiklemesiz) · çok-modelde test · versiyon damgası (`0.x-deneysel-m29`).
- **Ev:** `.claude/skills/<ad>/SKILL.md` (repo, git'e commit — dağıtım gece-senkron/pull ile).
- **Hazine tavanı kalktı (Karar 96, Salih 09-15):** char/adet tavanı ve "yeni skill = emekli-aday" kuralı süpersede; yönetim = seçim-isabeti (description standardı · katalog `.claude/skills/README.md` · tetiklenme isabeti ölçümü). Şema `core/skill-uretim-semasi.md` §4b.

## Deneysel notlar — 2026-07-29 (m.29; tam gerekçeler `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2026-08-30.md`)
- **D3:** değer üretilir üretilmez diske; teslim taslağı seans **ortasında** açılır. · **D4:** kanon edit'leri seans sonunda toplu (CC'de settings-deny yapısal). · A.11 iki-yüzey şerhi arşivde.
