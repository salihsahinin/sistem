# İB-69 / AİLE-2 — ANTİTEZ (m.40b v0.2)

**Künye:** rol antitez (işçi, salt-okur) · AS-OF 2026-08-31 · model claude-sonnet-5 (effort orta, rejim maliyet-öncelikli) · dizin `/Users/HasanSalihSahin/jarvis` · WEB YOK, kanıt yalnız iç dosyalardan · yazılan tek dosya bu rapor.

**Sınanan dört tez:** (a) `cc/rapor-2026-08-31-ib69-a2-envanter.md` · (b) `cc/rapor-2026-08-31-ib69-a2-k020.md` · (c) `cc/rapor-2026-08-31-ib69-a2-kural.md` · (d) `cc/rapor-2026-08-31-ib69-a2-pilot.md` · şema `raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md`.

**Denenen çürütme sayısı: 10.** Sonuç: **3 ÇÜRÜTÜLDÜ · 4 ZAYIFLATILDI · 3 DAYANDI.**

---

## Ç-01 | tez-d §A.5 "N_cagri=30, 144'ün ~%21'i" | ZAYIFLATILDI (tez-d kendi de flagledi, ama kanıtla büyütülüyor)

**İddia (tez-d, aynen):** "30 / 144 ≈ %21 — bu şeridin TEK BAŞINA payı düşük... güncel `sayac_oturum` değeri bu tasarım turunda ÖLÇÜLMEDİ."

**Çürütme:** `raporlar/2026-08-30-ib07-description-eval.md:9,11,48` şu rakamları veriyor: matris **60 hücre** planlandı (20 sorgu × 3 tekrar), ama gerçekleşen: "51 deneme" (45 başarılı + 6 hook-reddi) VE hook sayacı **72'ye ulaştı** ("73.-78. çağrılar reddedildi" → 72 çağrı geçti, sayaç zaten 72'de DURDUR'a çarptı). Yani planlanan 60 hücreye karşı gerçek sayaç tüketimi **72-78 çağrı** (%20-30 fazlası) — fark, lider'in kendi Agent-alt-çağrıları + oturumun önceki etkinliğinden geliyor (rapor kendi de: "muhtemelen sayaç seans-genelinde kümülatif, bu oturuma özel değil", satır 11). `.claude/hooks/pretool-ajan-fren.sh:27-37` doğrular: matcher yalnız `tool_name in (Agent,Task)`, `st["sayac"]` OTURUM state dosyasında (`ajan-fren-<sid>.json`) tutulur, sıfırlanmaz — **hem lider hem alt-ajan çağrıları aynı tek sayaca yazılır.**

**KANIT:** `raporlar/2026-08-30-ib07-description-eval.md:7,9,11,48-51` · `.claude/hooks/pretool-ajan-fren.sh:27-37`.

**ŞİDDET: ZAYIFLATILDI** — tez-d'nin "1 hücre = 1 çağrı" aritmetiği (hücre_tipi=tek_cagri için) DOĞRU; ama "%21" hesabı `sayac_oturum=0` varsayıyor ve bunu KENDİSİ de "ölçülmedi" diye işaretlemişti. IB-07 emsali bu boşluğun teorik değil FİİLİ olduğunu gösteriyor: planlanan/gerçek oranı 60/72-78 ≈ **1,2-1,3×**. Tez-d'nin "güvenli koşum şartı: sayac_oturum ≤ 114" önerisi bu yüzden iyimser — pilot 30 çağrı planlıyor ama lider'in kendi orkestrasyon-alt-çağrıları (varsa) da aynı sayaca yazılacağından güvenli üst sınır 114 değil, tarihsel oranla ~90-95 sayılmalı.

**Önerilen düzeltme:** tez-d'nin §A.5'ine "N_cagri=30 yalnız hücre-çağrılarıdır; lider'in kendi Agent-alt-çağrıları (varsa) ayrıca sayaca eklenir, IB-07 emsali +%20-30 gösteriyor" notu eklensin.

---

## Ç-02 | tez-a "İB-06'nın bugün koşulabilir hiçbir alt-kalemi yok" | DAYANDI

**İddia (tez-a, aynen):** "İB-06... bugün hiçbir alt-kalemi hemen koşulamaz" (5 alt-borç, hepsi eşik-altı sayaç: 2/10, 3/50, 0/5, 1/10, sıralı-zincir).

**Sınama:** `veri/karar-borcu.jsonl` İB-06 satırı (`kaynak`: `core/skill-uretim-semasi.md:103` vb.) doğrulandı, `icra_borcu` alanı birebir aynı sayaçları taşıyor: "kapı 2/10 koşum · H-kayıt 3/50 · damıtma 0/5 · emeklilik 1/10". `core/skill-uretim-semasi.md:103` civarı (bölüm 5) "10 koşumdan sonra ... τ/W/β/n_val kalibrasyonu" diyor — bu GERÇEK skill-kapısı koşum olayı sayısı, sentetik/tarihsel grid'le doldurulamaz çünkü `kuyruk/skill-fikir-kutusu.md:35-41` "Kapı-ağacı koşumları (ölçüm satırları — şema §5 kalibrasyon; 10 koşumda τ/W/β/n_val gözden geçirilir)" başlığı altında GERÇEK TARİHLİ satırlar tutuyor (08-15, 08-15, 08-29 ...) — sayaç bu tablonun satır sayısıdır, geriye dönük hesaplanabilir bir istatistik değil, olay-defteridir. `v_skill_kosum.csv` (42 satır, skill-kullanım özet görünümü) farklı bir sayaçtır (kaynak/skill/model bazlı toplam koşum), İB-06'nın τ/W/β kalibrasyon-kapı-koşumu sayacıyla AYNI ŞEY DEĞİL — karıştırılırsa yanlış-pozitif "veri zaten var" sonucuna varılır.

**KANIT:** `veri/karar-borcu.jsonl` (İB-06 satırı, `icra_borcu` alanı) · `kuyruk/skill-fikir-kutusu.md:35-41` · `veri/gorunum/v_skill_kosum.csv` (ayrım için karşı-kontrol).

**ŞİDDET: DAYANDI** — geriye dönük/sentetik grid taraması önerisi çürütülemedi çünkü sayaç TANIM GEREĞİ gerçek-olay defteridir (yeni skill-kapısı koşumu her seferinde elle tabloya düşüyor), var olan bronz/silver kütüklerinden yeniden türetilemez. Tez-a'nın önceliklendirmesi (İB-06'yı "en güçlü aday görünüyor ama bugün koşulamaz" diye işaretlemesi) DOĞRU KALIYOR.

---

## Ç-03 | tez-c "17 manifestten 0'ı matris-koşum, göç maliyeti 0 dosya" | DAYANDI (ama komşu-göç karıştırılmasın)

**İddia (tez-c, aynen):** "taradığım 17 manifestten (`ls veri/manifest/`) 0 tanesi matris-koşum yapıyor... göç maliyeti 0 dosya."

**Sınama:** `veri/manifest/*.json` (17 dosya) tek tek `tur` alanı çekildi: 14×`pipeline`, 1×`loop` (`loop-kapanis-bu-oturum.json`), 2× hesaba katılmayan (grep listesinde göründü ama `tur` satırı farklı biçimde) — **hiçbirinde `tur=matris` yok, hiçbirinde `matris:{...}` bloğu yok.** İddia sayısal olarak DOĞRU.

**Çelişki denemesi (İB-65 §5.2):** `raporlar/2026-08-31-ib65-loop-pipeline-secim-atlas.md:245` gerçekten diyor ki "2 mevcut manifestin `tur` değeri düzeltilecek (`loop-kapanis-bu-oturum`: loop→hibrit; `sahada-damitma-s22`: pipeline→hibrit)". Bu SATIR var ama **matris'le ilgisi YOK** — `hibrit` tür-düzeltmesi (İB-65'in kendi 4-değerli önerisi kapsamında), `matris` (aile-2'nin 5. aday değeri) değil. Yani tez-c'nin iddiası ile İB-65'in bu tespiti FARKLI eksenlerde: biri "matris göçü" (0), diğeri "hibrit göçü" (2). Çelişki YOK, ama tez-c raporunda bu ayrımı okuyucuya AÇIKÇA yazmıyor — okuyucu "göç maliyeti tamamen sıfır" sanabilir, oysa manifest-hijyeni genelinde 2 dosyalık AYRI bir göç borcu zaten kayıtlı.

**KANIT:** `veri/manifest/*.json` (17 dosya, elle grep) · `raporlar/2026-08-31-ib65-loop-pipeline-secim-atlas.md:245`.

**ŞİDDET: DAYANDI** (matris-özel iddia doğru) — **ama düzeltme önerisi:** tez-c'nin raporuna "bu 0 rakamı yalnız `matris` değeri içindir; `hibrit` göçü (2 dosya, İB-65 kaynaklı) AYRI ve zaten kayıtlı bir borçtur, karıştırılmasın" notu eklensin.

---

## Ç-04 | tez-c "hücre-tavanı ≤72" türetimi | ZAYIFLATILDI (kendi savunması sağlam ama tek-matris varsayımı tez-a'nın kendi listesiyle çelişiyor)

**İddia (tez-c, aynen):** "tek bir matrisin oturum payı ≤72 (=DURDUR'un yarısı)... 0,8×144=115 rakamı... doğrudan taşınması gerekçesiz olur."

**Sınama:** `.claude/hooks/pretool-ajan-fren.sh:8-11` UYARI=72/DURDUR=144 rakamlarını doğruluyor; tez-c'nin token-bütçesi (KAPI-1, 0,8 payı) ile çağrı-sayısı (KAPI-2) kaynaklarını ayırma gerekçesi TUTARLI, kendi olası itirazını (115 mi 72 mi) zaten önceden savunmuş.

**Ama:** tez-a'nın kendi önceliklendirmesi (`cc/rapor-2026-08-31-ib69-a2-envanter.md` §1, "Hemen koşulabilir" listesi) toplamda: İB-07 kalan **15** + İB-58 **16** + EK-1 **~35** + EK-4 (küçük ama belirsiz N) + EK-2 (belirsiz N) = yalnız ilk üç kalemin toplamı **66** hücre — tez-c'nin "≤72 tek matrisin payı" tavanına ZATEN neredeyse tamamen dokunuyor, EK-4/EK-2 eklenince aşıyor. Eğer bu oturumda tez-a'nın önerdiği gibi BİRDEN FAZLA "hemen koşulabilir" matris aynı oturumda çalıştırılırsa (Salih'in kayıtlı tercihi: "icra listesi onaysız devam + kademeli paralel" — `feedback-icra-listesi-onaysiz-devam.md`), "72 = tek matrisin payı, kalanı diğer İB'lere" varsayımı 3. kalemde zaten tükeniyor; tez-c'nin "tek matrisin oturumun tek işi olmadığını" savunan gerekçesi PRATİKTE ilk 2-3 kalemle çürüyor.

**KANIT:** `.claude/hooks/pretool-ajan-fren.sh:8-11` · `cc/rapor-2026-08-31-ib69-a2-envanter.md` §1 (İB-07=15, İB-58=16, EK-1≈35) · memory `feedback-icra-listesi-onaysiz-devam.md`.

**ŞİDDET: ZAYIFLATILDI** — sayının KENDİSİ (72) savunulabilir kalıyor, ama "bu tavan matrisi 'oturumun tek işi' varsayımına hapsetmiyor" gerekçesi tez-a'nın kendi önerdiği çoklu-matris programıyla çelişiyor; 72 rakamı TEK matris için makul ama AYNI OTURUMDA sıralanan 3-4 matrisin TOPLAMI için yetersiz — toplam oturum payı ayrı bir formülle (Σ N_cagri ≤ 0,8×144 ≈ 115, ya da DURDUR'un tamamı) hesaplanmalı, kalem-başı değil.

**Önerilen düzeltme:** ≤72 kalem-başı tavan KORUNSUN ama "OTURUM TOPLAMI Σ N_cagri ≤ 115 (0,8×144)" ikinci bir üst-kapı olarak eklensin — aksi halde art arda 2 kalem (İB-07 15 + İB-58 16 = 31, sorun yok) ile 3. kalem (EK-1 35, toplam 66) arasında görünmez bir aşım riski oluşur.

---

## Ç-05 | tez-b "M3 (ve M2) M-1 ölçüm borcunu KAPATABİLİR mi" — alt-ajan token görünürlüğü | ZAYIFLATILDI (kritik ama tam çürütme değil)

**İddia (dolaylı, tez-b M2/M3 + tez-d §A.8):** tez-d §A.8 "M-1 borcu KAPANIR — 30 hücrenin `token_giris/token_cikis/token_onbellek_okuma/sure_ms` alanları doğrudan bu koşumdan yazılır."

**Kritik kanıt:** `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:126` birebir: *"Claude Agent SDK dokümanı birebir şunu söylüyor — `parent_tool_use_id` alanı `StreamEvent` (token-delta) mesajlarında **her zaman null**; alt-ajanların token-seviyesi delta'ları ana oturuma **forward edilmez**; parent atfını yalnız TAMAMLANMIŞ mesajlar taşır"* [DESTEKLİ, code.claude.com/docs/en/agent-sdk/streaming-output, AS-OF 2026-08-31].

**Ama karşı-kanıt aynı raporda (satır 122):** G6 satırı "`usage` alanı önbellek-okuma/yazma ayrımını ve `result.usage.modelUsage` dökümünü taşıyor ama izleyici hiç göstermiyor" — yani TAMAMLANMIŞ turlarda `result.usage` alanı GERÇEKTEN VAR, sorun görünürlük/gösterim eksikliği (`gnhf-izle.py` bunu okumuyor), token verisinin YOKLUĞU değil. Ancak bu kanıt **gnhf CLI turları** bağlamında (worktree loop, çok-turlu), tez-d'nin pilotu ise **Agent/Task tool alt-ajan çağrısı** (tek-atım, aynı oturum içi fan-out) — iki farklı mekanizma; gnhf'nin `result.usage` alanının Agent-tool subagent dönüşünde de aynen mevcut olup olmadığı bu koşumda TEYİT EDİLEMEDİ.

**KANIT:** `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:122,126,140` · tez-d §A.8, §A.4.

**ŞİDDET: ZAYIFLATILDI** — "alt-ajan token delta'ları ana oturuma forward edilmez" cümlesi GERÇEK ve DESTEKLİ, ama bu CANLI STREAM için geçerli; TAMAMLANMIŞ mesajda `usage` alanının var olduğu aynı kaynakta yazılı. Yani M-1'i kapatmak muhtemelen MÜMKÜN (tamamlanmış Agent-tool sonucundan `usage` okunabilir) ama bu, HİÇBİR tez raporunda (b, d) doğrulanmadı — ikisi de "script SONUCU kaydeder" diyor ama "sonuç" olarak alt-ajanın token alanlarının GERÇEKTEN kendisine (lider'e) döndüğünü kanıtlamadı. Bu, tez-d'nin "M-1 borcu KAPANIR" ifadesini "muhtemelen kapanır, ama alt-ajan→lider token-aktarımı BİZZAT PİLOTTA doğrulanmalı" seviyesine indirir.

**Önerilen düzeltme:** tez-d §A.4/§A.8'e "Agent tool dönüş paketinde `usage`/`token_*` alanlarının fiilen dolu geldiği pilotun İLK hücresinde doğrulanmalı; dolu gelmezse M-1 açık kalır, `sure_ms` yalnız duvar-saati ile yaklaşık ölçülür" notu eklensin.

---

## Ç-06 | tez-d "300k iterasyon tabanı TEYİT EDİLDİ" | ZAYIFLATILDI ("ÖLÇÜLDÜ" damgası aşırı kesin)

**İddia:** tez-d §B.5 "TEYİT EDİLDİ (yaklaşık/dolaylı)"; aile-1 §4 TANIM bloğu ise "T_gnhf = 300k [**ÖLÇÜLDÜ**, önbellek-okuma DAHİL...]" diyor.

**Kaynak satır (`raporlar/2026-08-31-k010-a3-loop-1.md:12`):** *"tur-1 TEMİZ + İngilizce commit geçti; **token tavanı doldu** (535k/500k, 2 iterasyon)... iterasyon tabanı ~300k."*

**Aritmetik denetim:** 535k / 2 iterasyon ≈ **267,5k**, metinde "~300k" olarak yuvarlanmış (267,5→300 ≈ %12 yukarı yuvarlama). Bu rakam (a) tek bir iterasyonun temiz ölçümü DEĞİL, 2 iterasyonun TOPLAM tavan-aşımından geriye bölünerek TÜRETİLMİŞ bir ORTALAMA; (b) iki iterasyonun eşit maliyette olduğu varsayılıyor (önbellek-okuma birinci iterasyonda soğuk/pahalı, ikincide sıcak/ucuz olabilir — asimetri kütükte ayrıştırılmadı); (c) n=2 çok küçük örneklem.

**KANIT:** `raporlar/2026-08-31-k010-a3-loop-1.md:12-13` · aile-1 §4 TANIM bloğu ("ÖLÇÜLDÜ" damgası) · tez-d §B.5.

**ŞİDDET: ZAYIFLATILDI** — rakam UYDURULMAMIŞ, kaynağı gerçek ve tez-d'nin kendi şerhi ("yaklaşık/dolaylı") dürüst; ama aile-1'in TANIM bloğundaki düz "ÖLÇÜLDÜ" damgası (şerhsiz) yanıltıcı — bu bir n=2 türetilmiş ortalama, kalibrasyon-kalite bir ölçüm değil. **Önerilen düzeltme:** aile-1 §4'teki "T_gnhf = 300k [ÖLÇÜLDÜ...]" ifadesi "T_gnhf ≈ 300k [n=2 türetilmiş ortalama, dolaylı, DESTEKLİ ama ÖLÇÜLDÜ değil — bkz. k010-a3-loop-1:12]" olarak indirilsin.

---

## Ç-07 | tez-a "İB-67/İB-68 ikinci ekseninin değer kümesi emirde AÇIK yazılı değil" | ÇÜRÜTÜLDÜ (İB-67) / ZAYIFLATILDI (İB-68)

**İddia (tez-a, aynen):** "İB-67 / İB-68 — ikinci eksenin (doğrulama/pazar ölçütü) değer kümesi ilgili görev emirlerinde bu koşumda AÇILMADI — yalnız borç-havuzu özeti okundu, emir dosyalarının tam metni taranmadı (bütçe/effort kısıtı)."

**Sınama (İB-67):** `cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md:7` (S2) birebir: "Çıktı: aday × yenilik-durumu (**YOK-bulundu / KISMİ / DÜŞTÜ**) × en-yakın-komşu × kanıt-URL tablosu, AS-OF damgalı." — ikinci eksenin değer kümesi **3 kapalı kategori** olarak AÇIKÇA yazılı, emirde. Tez-a bu dosyayı bütçe kısıtından tam okumadığını itiraf etmişti (§3 not) — itiraf doğru çıktı ama sonuç [?] YANLIŞ oldu.

**Sınama (İB-68):** `cc/gorev-2026-08-31-ib68-urun-aday-envanteri.md:7,11` (S2 + durma koşulu): "pazar-sinyali alanı dolu ya da 'sinyalsiz' damgalı" — burada ikinci eksen kapalı bir kategorik küme DEĞİL (serbest pazar-sinyali metni + bir kaçış-değeri "sinyalsiz"), yani İB-67 kadar temiz değil ama TAM AÇIK-UÇLU da değil.

**KANIT:** `cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md:7` · `cc/gorev-2026-08-31-ib68-urun-aday-envanteri.md:7,11`.

**ŞİDDET:**
- İB-67 → **ÇÜRÜTÜLDÜ.** Tez-a'nın §1 sıralamasında İB-67'yi "eksen tanımı eksik (önce netleştirme borcu)" listesine (madde 9) koyması YANLIŞ; İB-67 aslında "eksen tanımı eksik" değil, "UYGUN — eksen tanımı mevcut, aday-doğrulama koşulabilir" sınıfına taşınmalı (8 aday × 3 kategori = N_hücre=24, tam faktöriyel).
- İB-68 → **ZAYIFLATILDI.** "sinyalsiz" damgası bir kaçış-değeri sağlıyor ama pazar-sinyali ekseni İB-67 gibi kapalı-küme değil; tez-a'nın "netleştirme borcu var" hükmü kısmen geçerli kalıyor (Ö2 kapalılık kısmi sağlanıyor, tam değil).

**Önerilen düzeltme:** tez-a §1 madde 9'u ikiye ayırsın: İB-67 → "hemen koşulabilir" listesine taşınsın (N=24); İB-68 → "eksen tanımı eksik" listesinde kalsın ama gerekçe "pazar-sinyali serbest-metin + sinyalsiz kaçışı, kapalı küme değil" olarak güncellensin.

---

## Ç-08 | aile-1 §6.1 Ö-A ("aynı dosyaya yazan hücreler paralel olamaz") ↔ hem aile-1 §6.2 hem tez-d §A.2'nin "Ö-A nötr" hükmü | ZAYIFLATILDI (şemanın kendi iç tutarlılığı sorgulanıyor)

**İddia (aile-1 §6.1, aynen):** "Ö-A ... aynı dosyaya yazan hücreler aynı turda paralel olamaz (`tools/paralel-kapi.py:113`: büyüyen ayak-izi → varsayılan SIRALI)."

**Uygulama (aile-1 §6.2, IB-07):** "Ö-A nötr (tek append-only kütük, çakışma yok)."
**Uygulama (tez-d §A.2, pilot):** "Ö-A (PK-10 ayak izi): nötr. Tüm hücreler tek append-only kütüğe... yazıyor... SIRALI zorunluluğu yok."

**Sınama:** `tools/paralel-kapi.py:111-113` okundu: `PK-10` kuralı yalnız `x['tur']=='loop' and y['tur']=='loop'` çiftleri için "büyüyen iterasyon ayak izi → SIRALI" der; genel `cakisma(x,y)` fonksiyonu ise (satır 105-108) iki birimin ayak-izi (dosya yolu) kesişirse ve `sira` kenarı yoksa **RED** (çakışma) döner — yalnız SIRALI değil. Yani script'in gerçek davranışı: aynı dosyaya yazan İKİ AYRI BİRİM arasında (sıra beyan edilmezse) **RED**, aile-1'in metninin dediği gibi sadece "SIRALI" değil. Ama bu kural İKİ AYRI ÜST-DÜZEY BİRİM (paralel-kapı manifest kayıtları) arası içindir — bir MATRİSİN KENDİ İÇİNDEKİ hücreler tek bir birim sayılır, paralel-kapı bunlara hiç bakmaz. Dolayısıyla "Ö-A nötr" hükmü aslında paralel-kapı'nın kapsamına GİRMEDİĞİ için savunulabilir — ama aile-1'in §6.1'deki genel-geçer prosa ifadesi ("aynı dosyaya yazan hücreler paralel olamaz") kendi uygulamasıyla (§6.2, tez-d) ÇELİŞİYOR GİBİ okunuyor; append-only'nin POSIX düzeyinde atomik olup olmadığı (kısa satır, `O_APPEND`) hiçbir yerde teyit edilmedi.

**KANIT:** `raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md` §6.1 Ö-A · §6.2 · `tools/paralel-kapi.py:95-113` · tez-d §A.2.

**ŞİDDET: ZAYIFLATILDI** — sonuç (Ö-A nötr) muhtemelen DOĞRU (matris-içi hücreler paralel-kapı'nın birim-arası kapsamına girmiyor, append atomikliği pratikte kısa JSON satırlarında sorun çıkarmıyor) ama şemanın §6.1 metni bunu AÇIKÇA gerekçelendirmiyor — "aynı dosyaya yazan hücreler paralel olamaz" cümlesi ile "tek append-only kütük → nötr" hükmü YAN YANA durunca okuyucuyu yanlış yönlendirebilir. **Önerilen düzeltme:** §6.1 Ö-A tanımına "İSTİSNA: matris-içi hücrelerin ORTAK append-only kütüğe yazması bu kuralın kapsamı DIŞINDADIR (paralel-kapı birim-arası çalışır, hücre-arası değil); POSIX kısa-satır append atomikliği varsayılır, doğrulanmadı [?]" notu eklensin.

---

## Ç-09 | tez-b M1 "risk — CC Agent uyumu doğrulanmamış, kritik" | DAYANDI

**İddia:** promptfoo Python provider HTTP'ye bağımlı değil ama CC Agent'ın senkron/paralel semantiğiyle, `tokenUsage` alanının dönüp dönmediğiyle, PK-10 ayak-izi kısıtıyla çakışıp çakışmayacağı doğrulanmadı.

**Sınama:** Ç-05'te bulunan kanıt (alt-ajan token delta'sının forward edilmediği, ama tamamlanmış mesajda `usage` alanının var olduğu) tam da bu riski DOĞRULUYOR — promptfoo'nun `tokenUsage` alanının CC Agent'tan gelip gelmeyeceği hâlâ AÇIK, M1'in kendi raporunun "en büyük risk kalemi" dediği şey gerçekten çözülmemiş kaldı; hiçbir dosyada promptfoo-CC Agent köprüsünün test edildiğine dair kanıt yok.

**KANIT:** Ç-05'in aynı kanıtı · tez-b §"KRİTİK BULGU" ve MODEL 1 "risk" bölümü.

**ŞİDDET: DAYANDI** — tez-b'nin M1'i "riskli/doğrulanmamış" olarak işaretlemesi ve M2'yi önermesi, Ç-05'in ortaya çıkardığı genel token-görünürlük belirsizliğiyle TUTARLI; çürütülemedi.

---

## Ç-10 | tez-d §A.2 "Ö-C kararı: model DIŞ, sorgu İÇ" (prompt-cache paylaşımı gerekçesi) | DAYANDI

**İddia:** model sabitlenince "sabit 14-skill listesi metni" prompt-cache'e bir kez yazılır, sorgu ekseni dış olsaydı model art arda değişeceği için cache ısınması bozulurdu.

**Sınama:** `raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md` §6.2 (İB-07 emsali) aynı ölçütü ("sorgu ekseni dış olursa 14-skill listesi metni iç eksen boyunca yeniden kullanılır → sorgu DIŞ") kullanıyor, tez-d bunu ikinci eksen (model) eklenince tutarlı biçimde GENİŞLETİYOR (paylaşım sınırı artık model sınırına taşınıyor). `veri/description-eval.jsonl:1`'deki `isci_model` alanı ve İB-07'nin "aynı skill-listesi metni 51 kez birebir kopyalandı" notu (rapor satır 53) modelin sabit tutulduğunu, prompt şablonunun DEĞİŞMEDİĞİNİ doğruluyor — Ö-C uygulaması iç tutarlı.

**KANIT:** aile-1 §6.2 · tez-d §A.2 · `raporlar/2026-08-30-ib07-description-eval.md:53`.

**ŞİDDET: DAYANDI** — çürütme denemesi (aynı ölçütün farklı eksen çiftine tutarsız uygulanmış olabileceği ihtimali) boşa çıktı; uygulama tutarlı.

---

## Sonuç özeti

| # | hedef | şiddet |
|---|---|---|
| Ç-01 | tez-d %21 hesabı (sayac_oturum=0 varsayımı) | ZAYIFLATILDI |
| Ç-02 | tez-a İB-06 "hiçbir alt-kalem koşulamaz" | DAYANDI |
| Ç-03 | tez-c "göç maliyeti 0 manifest" | DAYANDI (komşu-göçle karıştırılmasın) |
| Ç-04 | tez-c hücre-tavanı ≤72 (tek-matris varsayımı) | ZAYIFLATILDI |
| Ç-05 | tez-b/d M-1'in M2/M3 ile kapanabilirliği | ZAYIFLATILDI |
| Ç-06 | tez-d 300k "TEYİT EDİLDİ" / aile-1 "ÖLÇÜLDÜ" damgası | ZAYIFLATILDI |
| Ç-07 | tez-a İB-67/68 "eksen tanımı eksik" | ÇÜRÜTÜLDÜ (İB-67) / ZAYIFLATILDI (İB-68) |
| Ç-08 | aile-1 §6.1 Ö-A prosa ↔ §6.2/tez-d uygulaması | ZAYIFLATILDI |
| Ç-09 | tez-b M1 CC Agent uyumsuzluk riski | DAYANDI |
| Ç-10 | tez-d Ö-C (model dış/sorgu iç) gerekçesi | DAYANDI |
