# Masa Gündemi — 9. Lavish Masası (2026-09-08 gece)

*Tetik: Salih 09-08 22:15 ("seans başı, en son yapılacaklarda neler vardı? karar masasını hazırlayıp açarak başlayalım") + 22:40 ("fable 5 ile kurulan karar masaları formatında bir karar masası istiyorum" — ilk md→HTML yüzeyi RET; yüzey 7. masa biçiminde ELLE yeniden yazıldı, `tools/masa-html.py` yalnız md teslim kopyası için). Yüzey `.lavish/masa-9-2026-09-08.html` → teslim kopyası `raporlar/masa/masa-9-karar-yuzeyi-2026-09-08.html`. Hazırlayan Carvis/Fable, HEAD 9da948c. Hüküm Salih'te; her kalemde ÖNERİLEN ilk sırada (m.40 eki: ne demek · ne yaparım · artı · eksi). Deneysel m.29; rakamlar kaynaklı m.39. Kalem numaraları 8. masadan AYNEN taşındı (Karar 87 "sonraki masaya aynen taşınır"); M12 09-08 eklendi; M13-M15 Cowork devri §3'ten (`cc/devir/devir-2026-09-03-sonnet-icra-cowork.md`).*

**Bayat-satır düzeltmeleri (Karar 74 dersi — kanon çapraz-okuma, 22:45):** (1) masa-8 M7 ② ve ⑥ ZATEN KAPANMIŞ — 08-31 ek tur 2: İB-07 kalan 15 hücre `e1308d0` (60/60), İB-66 bağımsız hakem `e8909f5`; ledger KB-20 kapandı → M7 kalanlar ⑤ + devir F4-14 + F4-15 olarak yeniden yazıldı · (2) kapsül havuzu "T-A triyaj scripti" → DONE 09-03 (`tools/ta-triyaj.py`, `raporlar/2026-09/2026-09-03-ta-triyaj-ilk20.md`); Cowork "U5 şiddet formülü" bu scriptin formülü → M13 · (3) Cowork devri "`kod-orani-olcum.py --denetle`" → bayrak `tools/karantina.py --denetle`'de (bugün PASS, kayıt 0) · (4) manifest 17 → 25; `tur` = pipeline 18 · icra 6 · rapor 1 (enum dışı 2 değer) → M3 · (5) anakronizm 196/116 → bugün 161/52 (cc 36 · raporlar 14 · core 1 · wiki 1) → M4.

**Sağlık turu 09-08 gece:** test kapısı 102 OK / 7 skip (94 sn) · kural sayacı 19/100 · katman-hatti exit 0 · silver-sağlık error 5 / warn 5 / aday 5 (T-B-YETİM 385, T-A-ÖNELEME 6.999) · boyut: defter 45,1/48 · **kutu 20,9/20 AŞIM** · KILAVUZ 13,5/16 · pano 9,6/12 · kapsül 7,6/8 · CLAUDE.md 6,8/7 · bağlam: 09-04 Fable tepe 427.877 (172 tur >128k), 09-02 Cowork Sonnet 741.072 · skill 16 / description 7.379/7.380.

**Seans-başı durumu (m.18):** HEAD 9da948c 09-08 18:02, origin'e 2 commit ileri (push Salih beyanı bekler, m.9) · son commit 4 saat önce → paralel-oturum şüphesi YOK · silver BAYAT idi → `katman-hatti.py` koştu, exit 0 (WARN: kaynak_tarihi>çekim 7 · ajan araç çağrısı>54: 34) · çalışma ağacında 46 değişmiş türev dosya (09-08 katman koşumundan, commit'lenmemiş) + `.lavish/` + `Başlıksız.canvas` + `raporlar/gorsel-2026-09-04-word-ram-mekanizma.html` izlenmiyor.

**Kapsül "Sonraki ilk iş" havuzu (08-30'dan beri açık, karar GEREKTİRMEYEN):** ~~T-A triyaj scripti~~ DONE 09-03 · İB-64a/b/c araştırma emirleri · İB-53 ilk dilim + Cosma-CSV · İB-13 veri-siz iskelet · İB-60 loop-dedektör kalibrasyonu · İB-04 wiki 1-2 sayfa · İB-06 sayaç eşikleri · İB-56 · İB-72→71→70→73 sırası · seans-21 teslim raporu borcu · kapsül "Önceki" zinciri kısaltma (9,1/8 KB sınırda).

**Salih el işleri (karar değil):** A3 kalan 2 uzun-loop · İB-11 (d)(e) 10 dk · Finder md varsayılanı VS Code · bulut skill kopyaları (KB-10) · MIT 6.006/6.042J Ders-1 okuma + mat-felsefesi onayı (Karar 73 hattı) · galeri ek-bulgular dokümanını okuma.

## Kalemler

### M3 · Karar 86 D5 açık sorusu — manifest `tur` proxy mü, şema alanı mı
Karar 86 D5 enum `{pipeline, loop, hibrit, matris, belirsiz→masa}`; icra (45ce557) proxy'ledi. **Bugün:** 25 manifest — pipeline 18 · icra 6 · rapor 1 → 7 manifest enum DIŞI (09-03 Cowork birimleri), kapı v0.2 yakalamamış. `hibrit` ayrımı mevcut alanlardan çıkmıyor.
- **(a) ÖNERİLEN — Proxy kalır + isteğe bağlı `tur_ustyazim` alanı** (yalnız Fable yazar, gerekçe zorunlu) **+ enum-dışı 7 manifest düzeltilir + kapıya enum testi:** Artı: şema büyümez, hibrit istisna olarak işaretlenir, uyum açığı kapanır. Eksi: hibrit sayımı elle.
- **(b) Y1/Y2/Y3 yüklem alanları şemaya:** Artı: İB-65'in beklediği ayrım deterministik. Eksi: 17 manifest + kapı v0.2 + 8 test yeniden.
- **(c) Beklet (3 hibrit vaka görülene dek):** Eksi: bugün hibrit vaka yok, ölçüm gelmez.

### M4 · Karar 86 D6-3 — anakronizm tarihli-dosya muafiyeti (KURAL)
Bugünkü koşum 161 bulgu / İHLAL 52 (cc 36 · raporlar 14 · core 1 · wiki 1 — `wiki/uc-register.md:12`) / UYARI 109; 09-02'de 196/116. (a) seçilirse ihlal 52 → 2, ikisi kanon yüzeyinde.
- **(a) ÖNERİLEN — Dosya adındaki `YYYY-MM-DD` = AS-OF damgası sayılır; `raporlar/`+`cc/` tarihli dosyalar muaf, `core/`+`wiki/` muaf DEĞİL:** Artı: gürültü düşer, kanon yüzeyi korunur. Eksi: tarihli dosya içindeki "bugün" iddiaları da muaf sayılır.
- **(b) Muafiyet yok, her satır damgalı:** Artı: tek kural. Eksi: 116 ihlal el işi.
- **(c) Yalnız `raporlar/` muaf:** ara yol.

### M5 · Skill kabul kuralı (görselleştir dersi, Katman-1 aday)
İB-77: 8 işçi atlas + v0.1→v0.3 üç düzeltme → ret (09-03). Kabul kapısı skill-kapisi (K0-K3) yapıyı ölçtü, Salih beğenisini ölçmedi.
- **(a) ÖNERİLEN — Deneme sürümü kuralı:** yeni skill önce `kuyruk/skill-deneme/<ad>/` (hazineye ve `~/.claude/skills`'e girmez), Salih ≥1 canlı koşum + "kabul" sözü → hazine; tüzük ek fıkra + skill-kapisi K4 "kullanıcı-kabulü". Artı: ret ucuzlar. Eksi: deneme sürümü tetiklenemez → Salih elle çağırır.
- **(b) Mevcut kapı yeter, vaka tekil:** Eksi: aynı bedel yeniden ödenebilir.
- **(c) 3-koşum kuralı:** Artı: veri toplar. Eksi: ret 3 koşum sonra gelir, daha pahalı.

### M6 · Galeri devri 5 soru (`cc/devir/devir-2026-09-02-opus-galeri-yaprak-doluluk.md` §6; jarvis-dışı)
Tek kutuda 5 cevap: "1a 2a 3a 4a 5a" gibi yaz.
- **(a) ÖNERİLEN paket:** 1 derinlik 3 kalıcı (8 yaprak okunur; d4 %91,74 yedek) · 2 derinlik 2 denenmez · 3 `zaman-testi-model_v2u.json` arşive taşınır (m.8) · 4 2,5 GB türev temizlenir (yeniden üretim ~10 dk) · 5 odak eşiği %60/≥3 araç U1 çıktısına dek sabit.
- **(b) Karşıtlar:** 1 d4'e dön · 2 tek koşum dene · 3 sil · 4 kalsın · 5 %50/≥2'ye gevşet.

### M7 · 08-31 devrinin KALAN gerçek soruları (② ve ⑥ kapanmış — üstteki düzeltme)
⑤ rapor-yolu usulü (prompt `cc/rapor-…`, emir `raporlar/…`; işçi emri uyguladı) · F4-14 İB-07 "üst sınır" şerhi: altın sorgu setini ölçülen sistem türetti → bağımsız sorgu seti ayrı İB mi? (ledger KB-20 kapandı) · F4-15 İB-66 gerekçeleri (OTel GenAI, Braintrust) bağımsız hakemde zayıfladı → yeni kanıt turu mu, şerhle mi?
- **(a) ÖNERİLEN — ⑤ emir dosyası kazanır (prompt yalnız varsayılan) · F4-14 ayrı İB (bağımsız sorgu seti, Sonnet 1 birim ~15 çağrı), KB-20 kapalı kalır · F4-15 şerhle kalır:** Artı: üçü tek commit; üst-sınır şerhi kaybolmaz. Eksi: İB-66 tasarımı iki zayıf dayanakla yaşar (K-010 A4 açıkken uygulanmıyor).
- **(b) ⑤ hep `raporlar/` · F4-14 İB açılmaz · F4-15 yeni kanıt turu (2 işçi):** Artı: gerekçeler tazelenir. Eksi: cc/ ayrımı bozulur; bugün karşılığı olmayan tasarıma 30 çağrı.
- **(c) Karışık — nota "⑤a 14b 15a" yaz.**

### M8 · İB-75 bağlam-devri ekip-lideri v0 — tetik zamanı
Salih notu 09-02: "yakın tarih". 09-08 ölçümü: bu seans bağlam tepe 409k, 153 tur 128k üstünde (c6887d3) — İB-71 baseline artık ELDE.
- **(a) ÖNERİLEN — Bu masa sonrası ilk boş seansta tasarım emri (gorev-emri-derleme → atlas-kosum):** Artı: M2 damıtma DONE 09-04, İB-71 ölçümü var; 8. masadaki ön-koşullar sağlandı. Eksi: bir seans daha Fable bağlamı büyük çalışır.
- **(b) Hemen bu seansta:** Eksi: masa + hükümlerin icrasıyla paralel üçüncü iş.
- **(c) İB-70 bir tur sonra:** Eksi: "yakın tarih" notuna uzak.

### M9 · Senkron kütüğü 08-04'ten beri FAIL-ff (`gece-senkron.ps1` Windows)
Son satır hâlâ 2026-08-04 FAIL-ff (bugün doğrulandı); Mac'te eşlenik yok; açılış ritüeli adım 2.4 bayat satırı her seans okuyor.
- **(a) ÖNERİLEN — Kütüğü emekli et, ritüel adımını kaldır; gece işi gnhf'ye bağlı (Karar 84):** Artı: bayat okuma biter. Eksi: sayaç tarihçesi donar (arşivde kalır).
- **(b) Mac launchd eşleniği (İB aç):** Artı: sayaç sürer. Eksi: yeni otomat + push freni m.9 ile çelişir.
- **(c) Beklet.**

### M10 · Karantina ilk tescil (mekanizma Cowork U3'te KURULDU: `arsiv/karantina/` + `kod-orani-olcum.py --denetle`; tescil yetkisi Salih)
- **(a) ÖNERİLEN — `arsiv/kuyruk-arsiv/gorsellestir-skill-2026-09-03/` → karantinaya ilk tescil (BAKMA-GEREK-YOK bayrağı):** Artı: mekanizmanın ilk gerçek girdisi; tarama araçları okumaz. Eksi: `kod-envanter.py` git ls-files kullandığı için orada YİNE görünür (M14).
- **(b) Arşivde kalsın, karantinaya girmesin:** Eksi: 8 KB SKILL.md + spec'ler ingest/erişim taramalarına düşmeye devam eder.

### M11 · İB-73 Jarvis eğitim serisi — format hükmü
09-08'den yeni veri: SHAP + kümeleme ders serileri md/HTML karışık yürüdü, Salih 09-08 "her derse görsel + görsel atıflı metin" istedi (hafıza: feedback-gorsel-anlatim-atifli).
- **(a) ÖNERİLEN — md bölüm serisi `ogrenme/jarvis-serisi/` + her bölümde ≥1 mcp__visualize görsel + görsele atıflı metin + bölüm sonu sınav-grill tetiği:** Artı: VS Code yüzeyi (Karar 80), pointer'lı, 09-08 görsel kuralıyla uyumlu. Eksi: mcp__visualize çıktısı md'ye gömülemez → görsel ayrı HTML dosyası, md'den link.
- **(b) Lavish HTML bölümleri:** Artı: annotasyon + görsel aynı sayfada. Eksi: kanon dışı yüzey, tarihçe zayıf.
- **(c) Beklet.**

### M12 · Prompt-başı dosya seçimi: model yorumu mu, deterministik hook mu (Katman-1; Salih 09-08 "önerini karar masasına taşı")
Ölçüm 09-08 (HEAD ae36f9d): her promptta sabit yük CLAUDE.md 6,9 KB + skill description 7,4 KB (16 skill) + MEMORY.md indeks 2,5 KB ≈ 19 KB; kapsül/pano/tüzük/hafıza dosyaları yalnız Carvis kararıyla okunur. Prompt-başı dosya basan hook (UserPromptSubmit) YOK; yalnız PreToolUse ×2 + SessionStart var. Sonuç: aynı prompt → farklı seansta farklı dosya seti mümkün; CLAUDE.md §6 deterministik tasarım ilkesiyle örtüşmez.
- **(a) ÖNERİLEN — UserPromptSubmit hook + anahtar-kelime→dosya tablosu (`core/prompt-dosya-tablosu.tsv`, ilk sürüm ≤10 satır):** Ne demek: prompt metni tabloyla eşleşirse hook o dosyanın YALNIZ ilk N satırını/pointer'ını bağlama basar ("seans" → kapsül başı; "m.NN" → tüzük o madde; "hafıza/feedback" → ilgili memory dosyası). Yaparım: hook script + tablo + 3 test + hareket kütüğüne olay satırı. Artı: deterministik, kütüğe düşer, tablo Salih'çe okunur/düzenlenir. Eksi: eşleşmeyen konu yine model yorumuna kalır; tablo bakımı; yanlış eşleşme = boşa ~1-3 KB.
- **(b) Mevcut kalır, seçim kütüğe düşer:** Ne demek: hook yok; hareket kütüğüne "gerekçe" alanı eklenir. Artı: sıfır yeni mekanizma, tekrar-üretim kayıtla (§6 ikinci fıkra). Eksi: determinizm sağlanmaz, yalnız izlenir.
- **(c) Konu-başı ayrı CLAUDE.md profili (öğrenme / iş / jarvis-geliştirme):** Ne demek: staj örneği gibi klasör başına kendi CLAUDE.md'si. Artı: konu dışı 19 KB düşer. Eksi: üç kanon kopyası bakımı; m.16 kanon-tekliği sorusu.

### M13 · T-A triyaj şiddet formülü (Cowork U5; Karar 83 B3)
`tools/ta-triyaj.py`: `siddet = (uzunluk_a+uzunluk_b) × tekrar_sayısı(anahtar_terim)` — 6.999 ÖNELEME adayı çiftini sıralar; alternatif (uzunluk-farkı) eş-boy/tam-kopya çiftleri alta ittiği için elendi; rapor `raporlar/2026-09/2026-09-03-ta-triyaj-ilk20.md` iki formülü tablolu gösteriyor. Fiilen kullanılıyor, kanonda imzasız.
- **(a) ÖNERİLEN — Toplam-uzunluk × tekrar onaylanır; kanon satırı + ilk-20 damıtma sırası:** Artı: tam-kopya en üste çıkar, deterministik. Eksi: uzun ama tekil çiftler kısa-çok-tekrarla eşitlenebilir.
- **(b) Uzunluk-farkı formülü:** Eksi: devir raporunda elenme gerekçesi var.
- **(c) İki formül yan yana kalır, karar 10 koşum sonra:** Eksi: dedektör çıktısı iki sütunlu, okunması ağır.

### M14 · Kod-envanter karantina açığı — `tools/kod-envanter.py` git ls-files kullanıyor (Cowork devri §2)
Karantinaya taşınan dosya git-tracked kaldıkça envanterde görünür; `kod-orani-olcum.py` (os.walk) dışlıyor, `kod-envanter.py` dışlamıyor → iki sayım tutmaz.
- **(a) ÖNERİLEN — `kod-envanter.py`'ye aynı `arsiv/karantina/` dışlaması + 1 test (10 dk, Katman-2):** Artı: iki sayım tutar. Eksi: yok.
- **(b) `kod-envanter.py` emekli, tek sayım `kod-orani-olcum.py`:** Artı: paylaşılan-yardımcı sorunu (U4: `git_head()` 24 script'te tekrar) bir adım azalır. Eksi: envanterin git-tracked ayrımı kaybolur.

### M15 · U2 `.venv` dışlama — repo envanteri (Cowork devri §3)
`.venv` 35k dosya (gitignore'lu) kod/diğer sayılarını şişiriyor; görev kapsamı yalnız `.git`/`veri/bronz`/`veri/gorunum` diyordu, bilerek düzeltilmedi.
- **(a) ÖNERİLEN — `.gitignore` kurallarını dışlama kaynağı yap (`git check-ignore` ∨ pathspec), İB-71 baseline yeniden koşulur:** Artı: tek kaynak, `.venv` ve gelecek ignore'lar otomatik. Eksi: baseline sayıları değişir, 09-03 raporuna "eski ölçüm" şerhi.
- **(b) Yalnız `.venv` sabit listeye:** Artı: 1 satır. Eksi: bir sonraki büyük klasörde aynı sorun.
- **(c) Kalsın:** Eksi: kod/md oranı (İB-75 girdisi) yanlış.

### M16 · Bu seansın icra sırası (masa sonrası; karar değil öncelik)
Hükümler düştükten sonra bu seansta ne koşulsun? Kutuya sıra yaz.
- **(a) ÖNERİLEN — Hükümlerin icrası (Karar 88 defter bloğu + ledger + kapsül) → kutu damıtma (20,9/20) → M14/M15 küçük kod → kapsül "Önceki" kısaltma → seans-21 teslim borcu → (M8a ise) İB-75 emri:** Artı: masa borçları kapanır, havuz ilerler. Eksi: araştırma kalemi (İB-64, İB-75) bu seansa girmez.
- **(b) Hükümler + İB-75 tasarım emri (M8 b ise):** Eksi: bağlam büyür.
- **(c) Yalnız hükümler, seans kapanır:** Artı: kısa seans, Fable bağlamı temiz. Eksi: havuz yerinde sayar.

## Masa sonrası icra (Fable)
Hükümler → `kuyruk/senaryo-defteri.md` Karar 88 bloğu · ledger · kapsül · masa md + yüzey commit. Push yalnız Salih beyanıyla (m.9; origin'e 2 commit birikmiş).
