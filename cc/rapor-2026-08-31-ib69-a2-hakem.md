# İB-69 / AİLE-2 — MASKELİ HAKEM (m.40b v0.2)

**Künye:** rol **maskeli hakem** · AS-OF 2026-08-31 · model **opus** (Opus-5) · HEAD `c1f5c05` (`git rev-parse --short HEAD`, koşum anı) · dizin `/Users/HasanSalihSahin/jarvis` · **WEB YOK** (emir gereği; iç kanıt) · kanon salt-okur, yazılan tek dosya budur.

**Maske beyanı:** iddialar kaynağına göre değil kanıtına göre yargılandı. Tez ile antitezin AYNI hatayı yaptığı **iki nokta** ayrı ayrı X aldı (H-18/H-34 hücre-tavanı payı; H-03/H-32 İB-67 ekseni). Antitezin "DAYANDI" dediği bir iddia da (Ç-07 İB-67 taşınması) **gerekçesi çürük** olduğu için X aldı — sonuç doğru, türetim yanlış.

**Kendim açtığım dosyalar (bu koşumda okundu):**
`raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md` (tam, 235 satır) · `cc/rapor-2026-08-31-ib69-a2-envanter.md` (tam) · `-a2-k020.md` (tam) · `-a2-kural.md` (tam) · `-a2-pilot.md` (tam) · `-a2-antitez.md` (tam) · `-a2-v26.md` (tam) · `raporlar/2026-08-30-ib07-description-eval.md` (tam, 58 satır) · `.claude/hooks/pretool-ajan-fren.sh` (tam, 62 satır) · `raporlar/2026-08-31-k010-a3-loop-1.md:1-30` · `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md:115-142` · `cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md:1-22` · `veri/manifest/*.json` (17 dosya, `ls` + `tur` grep) · `veri/description-eval.jsonl` (45 satır, python3 ile sorgu×tekrar dağılımı) · `veri/karar-borcu.jsonl` (İB-06 satırı) · `tools/hareket-tablo.py` (usage/token grep)

**AÇMADIĞIM kaynaklar → hiçbirine DESTEKLİ damgası verilmedi (`[?]`):** `tools/erisim-kalibrasyon.py` · `tools/d2-eval.py` · `tools/denetci-kalibrasyon.py` · `tools/silver-saglik-kalibrasyon.py` · `tools/paralel-kapi.py` · `tools/AXI-STANDARDI.md` · `cc/gorev-2026-08-31-ib68-*.md` · `core/pano.md` · `kuyruk/k010-zincir-2026-08-29.md` · tüm dış URL'ler.

---

## 1. İDDİA HÜKÜMLERİ — 35 ayrık iddia · **D=15 · K=4 · X=16**

### (a) Envanter tezi

`H-01 | İB-06'nın beş alt-borcunun hiçbiri bugün koşulamaz (sayaçlar eşik-altı) | veri/karar-borcu.jsonl İB-06 icra_borcu alanı birebir: "kapı 2/10 koşum · H-kayıt 3/50 · damıtma 0/5 · emeklilik 1/10" | D | Sayaçları kendim çektim, dördü de eşik-altı; beşincisi (world-model §6) sıralı zincir. Emrin beklentisiyle çelişen bu bulgu doğru ve açıkça işaretlenmiş.`

`H-02 | İB-06e sıralı bağımlılık taşıdığı için Ö-B (bağımsızlık) ihlali → matris değil | karar-borcu İB-06 başlığı: "NDV→tekrar→dil-çarpanı→sort-key→durum-denkliği" | D | Ok işaretleri sıralı zinciri borç kaydının kendisinde taşıyor; aile-1 §6.1 Ö-B'nin doğru uygulaması.`

`H-03 | İB-67'nin ikinci ekseninin değer kümesi emirde açık yazılı DEĞİL | cc/gorev-2026-08-31-ib67-...md:7 ve :9 | X | Emir :7 çıktı etiket kümesini ({YOK-bulundu/KISMİ/DÜŞTÜ}) ve :9 "Aileler (dik): A akademik · B endüstri/araç · C iç envanter" üçlüsünü AÇIKÇA yazıyor. Tez-a dosyayı açmadığını itiraf etmiş (§3), [?] hükmü yanlış çıktı.`

`H-04 | İB-07'nin kalan işi tam 15 hücredir | veri/description-eval.jsonl: 45 satır; tekrar dağılımı {1:20, 2:20, 3:5} → 60−45=15, eksik olan q06-q20 tekrar3 | D | Kütüğü python3 ile saydım; iddia birebir doğrulandı.`

`H-05 | İB-58 kalan iş 2 script × 8 AXI maddesi = 16 hücre, LLM'siz | tools/AXI-STANDARDI.md · İB-58 raporu — İKİSİ DE bende AÇILMADI; tez-a da açmadığını §3'te itiraf ediyor | K | İki bağımsız açılmamış kaynağa dayanan sayı; ne doğrulanabilir ne çürütülebilir. Sentez bunu SAYI olarak değil "[?] 16" olarak taşımalı.`

`H-06 | EK-1 erişim-kalibrasyon 7 ağırlık × 5 yöntem ≈ 35 hücre, hemen koşulabilir, LLM maliyeti sıfır | tools/erisim-kalibrasyon.py:28,76-92 — bende AÇILMADI | K | Değer kümelerinin (7 ve 5) script'te gerçekten yazılı olduğu teyit edilmedi; ayrıca PK-12 BEKLE durumu erisim ailesinde daha önce iş dondurmuştu, "hemen" damgası kontrol istiyor.`

`H-07 | Envanter tablosu "27+4 satır" | awk sayımı: hükümlü satır = 12 UYGUN + 23 UYGUN-DEĞİL = 35 | X | Başlık 31 diyor, tablo 35 hükümlü satır taşıyor (İB-06 beş alt-satıra bölündüğü için). Küçük ama §1 Ö2 (yalanlanabilirlik: sayı METİNDEN değil kaynaktan) ilkesinin kendi raporunda ihlali.`

`H-08 | utopik-havuz md.17 açık borç havuzunda DEĞİL, matrise girmesi Katman-1 onayı ister | kuyruk/utopik-havuz.md:34 — bende AÇILMADI | K | Doğru görünüyor ama teyit etmedim; hükmün kendisi (Katman-1 kapısı) zaten ihtiyatlı.`

### (b) K-020 tezi

`H-09 | promptfoo Python provider HTTP API'ye bağımlı DEĞİL, call_api herhangi bir Python fonksiyonunu sarar | V26 raporu, promptfoo.dev/docs/providers/python/ 2 kez WebFetch | D | Bağımsız V26 turu imzayı ve "proprietary or local models" örneklerini doğruladı; çekirdek iddia sağlam.`

`H-10 | Doküman "subprocess çağrıları ... örnekliyor" [DESTEKLİ damgalı] | V26 ikinci turu: "subprocess" kelimesi sayfada HİÇ GEÇMİYOR | X | Dokümanın söylemediği somut bir örnek dokümana atfedilmiş; DESTEKLİ damgası hak edilmemiş. V26'nın tek gerçek bulgusu ve haklı.`

`H-11 | M2 (kendi harness) aile-1 §5'in 13 alanının TAMAMINI otomatik üretebilir ("13/13 potansiyel, en yüksek skor") | token_giris/token_cikis/token_onbellek_okuma alanlarının KAYNAĞI hiçbir yerde gösterilmemiş; grep "usage\|token" tools/hareket-tablo.py → 0 eşleşme; İB-66:126 alt-ajan token-delta'sının forward EDİLMEDİĞİNİ söylüyor | X | Script LLM'i çağırmıyorsa (M2'nin kendi artısı) token alanlarını NEREDEN alacağı tanımsız. 13/13 iddiası kaynağı olmayan 4 alanı otomatik sayıyor; gerçek üst sınır 9/13. Bu, M2'yi M1'in üstüne çıkaran "kalite" satırının belkemiğiydi.`

`H-12 | M3'te 13 alanın hiçbiri otomatik değil, hepsi işçi-ajan disiplinine bağlı | tez-b kendi eksen tablosu; İB-07'nin elle-resume dersi | D | Kendi zaafını dürüstçe yazmış; İB-07 emsali bu riskin fiili olduğunu gösteriyor.`

`H-13 | Önerilen sıra "M3 ile pilot koş (M-1'i ölç), sonra M2'ye genişle" — çünkü M3 M-1'i kapatan doğru ilk adım | M-1'in kapanma mekanizması ne M2'de ne M3'te var (H-11 kanıtı) | X | Sıranın GEREKÇESİ çürük: M3 de M-1'i kapatamaz (tez-b bunu §M3 risk satırında yarım kabul ediyor: "M-1 borcu burada da AŞILMAZ, yalnız ertelenir" — ama sonra öneri gerekçesinde tam tersini söylüyor). İç çelişki.`

`H-14 | M1'in en büyük riski doğrulanmamış CC Agent köprüsüdür | tez-b §KRİTİK BULGU + repo genelinde promptfoo-CC köprü testi kanıtı YOK + İB-66:126 | D | Risk gerçek ve kapatılmamış; M1'i bugün için elemek için yeterli gerekçe.`

`H-15 | tools/d2-eval.py 172 satır; kaydet() her satıra ts + git_head'i otomatik ekliyor | V26 wc -l + fonksiyon okuması | D | Bağımsız doğrulandı, tam isabet.`

### (c) Kural tezi

`H-16 | 17 manifestten 0'ı matris-koşum; matris eklenirse göç maliyeti 0 dosya | ls veri/manifest/ = 17 dosya; grep '"tur"' = 16 pipeline + 1 loop; hiçbirinde matris bloğu yok | D | Kendim saydım: 17 dosya, tur değerleri {pipeline:16, loop:1}. Matris değeri için etkilenen dosya = 0. Kesin.`

`H-17 | (ANTİTEZ Ç-03) "17 dosya: 14×pipeline, 1×loop, 2× hesaba katılmayan" | benim sayımım: 16 pipeline + 1 loop = 17, hepsi sayıldı, "hesaba katılmayan" yok | X | Antitez doğrulama yaptığını söylediği sayımı yanlış yapmış (14+1+2). Sonucu (0 matris) doğru ama ara-sayıları çürük — maske gereği ayrı X.`

`H-18 | Hücre-tavanı ≤72 (=DURDUR/2); gerekçe "İB-07 emsali 60-65 hücrenin eski 72 eşiğini doldurduğunu gösteriyor" | ib07:9,11,48: gerçek hücre-çağrısı 51 (45+6), sayaç 78; 78−51=27 çağrı matris-DIŞI oturum tüketimi | X | Gerekçe yanlış: 72'yi dolduran 60-65 hücre değil, 51 hücre + 27 matris-dışı çağrıdır. 72 sayısı 144/2 yuvarlamasından geliyor, ölçümden değil. Sayının kendisi muhafazakâr olduğu için zararsız ama TÜRETİM çürük (doğru türetim §3'te).`

`H-19 | DURDUR=144 / UYARI=72; sayaç oturum-geneli, alt-ajan çağrıları dahil, Agent/Task matcher'ıyla artar | pretool-ajan-fren.sh:20 (env varsayılanları), :27 (matcher), :30-32 (session state), :37 (sayac += 1), :46 (n >= durdur → bloke) | D | Hook'u satır satır okudum; içerik hükmü tam doğru.`

`H-20 | Matris koşumu A1 sicilini +1 ETKİLEMEZ (A1 birimi = "pipeline-koşumu" okumasıyla ONAYLI) | V26 iki pointer'ı da birebir doğruladı (pano.md:34, k010-zincir:55); ben açmadım | D | Bağımsız V26 turu tam isabet raporladı; kapsam-dışı hükmü (çelişki değil) doğru kurgulanmış.`

`H-21 | Hook pointer'ları: "satır 9-10 eşikler · satır 27 sayac += 1 · satır 22-24 state okuma" | gerçek: 11 · 37 · 30-32 | X | Kendi okumamla V26'yı doğruladım. İçerik doğru, üç pointer da hedefi kaçırıyor — m.20 pointer ilkesi ihlali, otomatik doğrulayıcıyı yanlış satıra gönderir.`

`H-22 | gnhf_iterasyonu hücreler ajan-fren hook'undan GEÇMEYEBİLİR [?] | hook matcher yalnız ("Agent","Task") PreToolUse; gnhf ayrı CLI süreci | K | Fiziksel olarak muhtemel (ayrı süreç → PreToolUse yok) ama test kanıtı yok. Tez-c bunu zaten [?] işaretlemiş — dürüst; K olarak KALIR, sentez sayı türetmemeli.`

### (d) Pilot tezi

`H-23 | N_hücre=30, hucre_tipi=tek_cagri → N_cagri=30 (1 hücre = 1 Agent çağrısı) | hook:37 her Agent/Task çağrısında sayac += 1 | D | Doğru ve kesin; çarpan yok (bkz. §3-i).`

`H-24 | "Güvenli koşum şartı: sayac_oturum ≤ 114" | hook:46 `if n >= durdur` → 144. çağrı BLOKE, son izinli çağrı 143. → sayac_oturum + 30 ≤ 143 → sayac_oturum ≤ 113 | X | Bir birim yanlış (114 → 113). 114'te 30. hücre n=144 olur ve reddedilir; matris son hücresinde kesilir. Küçük ama fren-eşiğinde tam da kritik olan sınır.`

`H-25 | "Ö1 (tamlık) sağlanıyor: iki eksen de ≥1 değer taşıyor" | tez-d §A.1 EKSEN#2 degerler = ["claude-haiku-4-5-20251001", "[?]"] | X | §1 Ö1 `degerler`i "TAM küme" olarak tanımlıyor ve §1 Ö2 kardinalitenin DOSYADAN türetilmesini şart koşuyor. "[?]" bir değer değil, boşluktur. Pilot bugün Ö1'i SAĞLAMIYOR; tez-d aynı sayfada hem [?] bırakıp hem "sağlanıyor" diyor — iç çelişki. Bu, koşum-öncesi bloke edici bir kusurdur.`

`H-26 | Pilot "İB-07'nin açık 15 hücresinden 5'ini de kapsar (iki kuş)" | veri/description-eval.jsonl sayımı: q06-q10 için tekrar1=1, tekrar2=1, tekrar3=0 (her biri) → haiku kolonundaki 15 hücrenin 10'u ZATEN KÜTÜKTE | X | 30 hücrenin 10'u mükerrer koşumdur (yeni bilgi sıfır, aile-1 §2 Ö3 "çakışma olayı" sınıfı). Gerçek getiri: 5 borç hücresi + 15 yeni-model hücresi = 20 bilgi taşıyan hücre / 30 çağrı → %33 israf. Doğru pilot tasarımı haiku kolonunu yalnız tekrar3'e (5 hücre) daraltır: 5 + 15 = 20 hücre, 20 çağrı.`

`H-27 | 300k "TEYİT EDİLDİ (yaklaşık/dolaylı)" — rakam k010-a3-loop-1:12'de gerçekten var | sed -n '1,30p' ile satır 12 açıldı: "token tavanı doldu (535k/500k, 2 iterasyon) ... gnhf token birimi = önbellek-okuma DAHİL; iterasyon tabanı ~300k" | D | Satır birebir orada, "önbellek-okuma DAHİL" ibaresi birebir var. Tez-d'nin şerhi ("yaklaşık/dolaylı") dürüst ve doğru. Aile-1 §8 açık-ucu #5 KAPANDI.`

`H-28 | Aile-1 §4 TANIM: "T_gnhf = 300k [ÖLÇÜLDÜ, önbellek-okuma DAHİL]" | 535k / 2 iterasyon = 267,5k; "~300k" %12 yukarı yuvarlama; n=2; soğuk/sıcak önbellek asimetrisi ayrıştırılmamış | X | ÖLÇÜLDÜ damgası yanlış. Ölçülen şey 2 iterasyonun TOPLAMIDIR (535k); 300k ondan geriye bölünmüş, yuvarlanmış bir ORTALAMA. m.29 (her rakam kaynaklı + deneysel damgalı) gereği damga indirilmeli. Şerh metni §3-ii'de.`

`H-29 | Ö-C kararı: model DIŞ / sorgu_id İÇ (önbellek paylaşımı model sınırında) | aile-1 §6.2 aynı ölçüt; ib07:53 "aynı skill-listesi metni 51 kez birebir kopyalandı" | D | Ölçüt tutarlı genişletilmiş; model değişimi önbellek-önekini geçersiz kılar, sabit tutulan eksen dış olmalı. Uygulama iç tutarlı.`

`H-30 | Pilot kütüğü "veri/description-eval.jsonl uzantısı ya da yeni dosya" olabilir | mevcut kütükte 8 alan var: altin_etiket, isabet, isci_model, kosum_id, secilen_skill, sorgu_id, tekrar, ts | X | Mevcut kütükte hucre_anahtari, git_head, hucre_tipi, eksen_degerleri, toplama_yontemi, token_*, sure_ms, kosum_durumu YOK ve model alanı `isci_model` adıyla duruyor (13-alan şemasının 8/13'ü eksik/farklı adlı). Aynı dosyaya append = karışık-şemalı kütük = §3 deterministik toplamanın girdi şartının ihlali. "Ya da" seçeneği kapatılmalı: YENİ DOSYA zorunlu.`

### (e) Antitez

`H-31 | Ç-01: "planlanan/gerçek oranı 60/72-78 ≈ 1,2-1,3×; güvenli üst sınır 114 değil ~90-95 sayılmalı" | ib07: 51 hücre-çağrısı (45+6) + 27 matris-dışı çağrı = 78 | X | Fazlalık ÇARPANSAL değil TOPLAMSALDIR: matris büyüklüğünden bağımsız, sabit bir oturum-tabanıdır (İB-07'de 27 çağrı). ×1,2-1,3 modeli N büyüdükçe fazlalığı yanlış biçimde büyütür, N küçüldükçe yanlış biçimde küçültür. 90-95 sayısı bu yanlış modelden türediği için geçersiz.`

`H-32 | Ç-07: "İB-67 aslında 8 aday × 3 kategori = N_hücre=24, tam faktöriyel" | gorev-ib67:7 — {YOK-bulundu/KISMİ/DÜŞTÜ} ÇIKTI etiketidir; aile-1 §1 "Sık yapılan hata": eksen ≠ etiket uzayı | X | Antitez, aile-1 hakeminin İB-07'de yakaladığı hatanın BİREBİR AYNISINI yapıyor (14 skill'i eksen sanmak = 3 kategoriyi eksen sanmak). Gerçek ikinci eksen emir :9'daki dik aileler {A akademik, B endüstri, C iç envanter}; 8 × 3 = 24 sayısı tesadüfen aynı çıkıyor ama türetim çürük. Sonuç doğru, gerekçe X.`

`H-33 | Ç-05: alt-ajan token delta'ları canlı akışta forward EDİLMEZ (parent_tool_use_id StreamEvent'te her zaman null) ama TAMAMLANMIŞ sonuçta result.usage/modelUsage VAR | ib66:122 (G6) ve :126 (İ-27 sert kısıt) — ikisini de kendim okudum | D | Alıntılar birebir doğru. Antitezin en değerli bulgusu; M-1'in mekanizma sorusunu doğru yere koyuyor (§3-iii).`

`H-34 | Ç-04: "OTURUM TOPLAMI Σ N_cagri ≤ 115 (0,8×144) ikinci üst-kapı olarak eklensin" | 0,8 payı aile-1 §4 KAPI-1'in TOKEN bütçesi konvansiyonu; tez-c bunu çağrı sayacına taşımanın gerekçesiz olduğunu doğru saptamış | X | Antitez, tez-c'nin doğru olarak reddettiği taşımayı geri getiriyor — hem de tez-c'yi çürüttüğü aynı maddede. Çağrı sayacı sert ve tam sayılı bir kaynaktır; 0,8 payı yerine ölçülmüş oturum-tabanı (27) düşülmelidir (§3-i).`

`H-35 | Ç-08: aile-1 §6.1 Ö-A'nın "aynı dosyaya yazan hücreler paralel olamaz" prozası, §6.2/tez-d'nin "tek append-only kütük → Ö-A nötr" hükmüyle yan yana yanıltıcı; şerh gerekli | tools/paralel-kapi.py bende AÇILMADI, ama iki metnin YÜZEY çelişkisi doğrudan okunuyor | D | Kapsam ayrımı (paralel-kapı birim-ARASI, matris hücreleri birim-İÇİ) hükmü doğru ve şema metnine şerh gerçekten gerekiyor. Not: paralel-kapi.py satır iddialarına DESTEKLİ vermiyorum (açmadım), yalnız çelişki-yüzeyi bulgusuna D veriyorum.`

---

## 2. KENDİM DOĞRULADIĞIM BEŞ ZORUNLU KALEM

### (i) Pilot çağrı aritmetiği — **kesin sayı: çarpan 1,00; toplamsal taban 27; güvenli sınır sayac_oturum ≤ 113**

**Ham veriler (kendi okumam):**
- `.claude/hooks/pretool-ajan-fren.sh:27` matcher `tool_name in ("Agent","Task")`; `:37` `st["sayac"] += 1`; `:46` `if n >= durdur` → **144. çağrı bloke, son izinli çağrı 143**; `:20` varsayılan `UYARI=72 · DURDUR=144`.
- `raporlar/2026-08-30-ib07-description-eval.md:9` "sayaç 72'ye ulaşınca ... 73.-78. çağrılar reddedildi" · `:11` "1+10+10+10+10+10=51 deneme" · `:48` "51 deneme (45 başarılı + 6 hook tarafından reddedilen)" · `:51` "Kendi araç çağrım (yaklaşık): ~65 (51 Agent + Read/Bash/Write/Edit ~14)".

**Aritmetik:**
```
İB-07: planlanan hücre        = 60
       fiilen yapılan hücre-çağrısı = 51   (45 kaydedildi + 6 hook reddi)
       oturum sayacının ulaştığı  = 78
       matris-DIŞI oturum tüketimi = 78 − 51 = 27 çağrı
       lider'in kendi non-Agent araçları (~14 Read/Bash/Write) SAYACA GİRMEZ (matcher yalnız Agent/Task)
```
**Hüküm:** Hücre başına çarpan **1,00**'dir — 30 hücre → **tam 30 Agent çağrısı**. Antitezin "×1,2-1,3 güvenlik payı" modeli **X**: 78/60 oranı, hücre başına bir ek yükü değil, matristen bağımsız SABİT bir oturum tabanını (27 çağrı) ölçüyor. Doğru model **toplamsaldır**:
```
N_cagri_toplam = N_hucre × 1,00 + sayac_oturum_anlik
Koşum ön-koşulu (hook :46 off-by-one dahil):
  N_hucre + sayac_oturum_anlik ≤ 143
30 hücrelik pilot için:  sayac_oturum ≤ 113        [tez-d'nin "114"ü BİR FAZLA — X]
Ölçülmüş taban (n=1, İB-07): 27 çağrı  →  planlama-zamanı varsayılanı:
  N_hucre ≤ 143 − 27 = 116                          [oturumdaki TÜM matris hücrelerinin toplamı]
```
Sentez bu üç sayıyı taşımalı: **çarpan 1,00 · taban 27 (n=1, deneysel) · sınır 113 (30-hücrelik pilot için) / 116 (planlama tavanı)**. Kural olarak: sayaç okunabiliyorsa taban TAHMİN EDİLMEZ, koşum anında okunur.

### (ii) 300k'nın epistemik statüsü — **ÖLÇÜLMEDİ; n=2 türetim; `[?]` KALKAR, "ÖLÇÜLDÜ" DÜŞER**

`raporlar/2026-08-31-k010-a3-loop-1.md:12` (kendi okumam, birebir): *"tur-1 TEMİZ + İngilizce commit geçti; **token tavanı doldu** (535k/500k, 2 iterasyon) | **gnhf token birimi = önbellek-okuma DAHİL**; iterasyon tabanı ~300k."*

Üç hüküm:
1. **`[?]` teyit borcu KAPANIR** — satır açıldı, rakam gerçekten orada, birim (gnhf iterasyonu) ve önbellek kapsamı ("önbellek-okuma DAHİL") birebir yazılı. Aile-1 §8 açık-uç #5 ve §4'teki `[?]` şerhi silinebilir.
2. **"ÖLÇÜLDÜ" damgası DÜŞER** — ölçülen büyüklük 2 iterasyonun TOPLAMIDIR (535k). 535k ÷ 2 = **267,5k**; metindeki "~300k" bundan **%12,1 yukarı yuvarlanmış** bir ortalamadır. n=2, ve iki iterasyonun eşit maliyette olduğu (soğuk/sıcak önbellek asimetrisi yok) varsayılmıştır — kütükte ayrıştırılmamış.
3. **Aile-1 §4 TANIM bloğuna düşecek şerh (aynen alınabilir):**
   ```
   T_gnhf ≈ 300k   [TÜRETİLDİ, ÖLÇÜLMEDİ — 535k/500k tavan aşımı ÷ 2 iterasyon = 267,5k,
                    metinde ~300k'ya yuvarlanmış (+%12,1); n=2; iterasyonlar arası soğuk/sıcak
                    önbellek asimetrisi ayrıştırılmadı; önbellek-okuma DAHİL.
                    Kaynak: raporlar/2026-08-31-k010-a3-loop-1.md:12, vaka e2e715, AS-OF 2026-08-31.
                    [?] teyit borcu KAPANDI (satır açıldı). Kalibrasyon-kalite ölçüm DEĞİL:
                    T_gnhf'yi bir eşiğe/kapıya sokmadan önce n≥3 temiz iterasyon ölçümü gerekir.]
   ```

### (iii) M-1 (T_hucre) hangi MEKANİZMAYLA kapanır — **pilotla KAPANMAZ; ayrı bir hasat işi gerekir**

Kendi okumam, `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md`:
- **:122 (G6)** — *"`usage` alanı önbellek-okuma/yazma ayrımını ve `result.usage.modelUsage` dökümünü taşıyor ama izleyici hiç göstermiyor"*.
- **:126 (İ-27 sert kısıt)** — *"`parent_tool_use_id` alanı `StreamEvent` (token-delta) mesajlarında her zaman null; alt-ajanların token-seviyesi delta'ları ana oturuma forward edilmez; **parent atfını yalnız TAMAMLANMIŞ mesajlar taşır**"*.

Antitezin okuması **DOĞRU** (H-33 = D). Sonuçları:
- **Kapanmaz:** (a) canlı stream'den — fizik sınırı; (b) tez-d §A.8'in varsaydığı gibi "hücre koşulur, satır yazılır" akışından — çünkü **Agent tool'un lider'e dönüşünde `usage` alanının bulunduğu HİÇBİR YERDE gösterilmedi**; (c) M3'ün "işçi kendi token'ını yazsın" disipliniyle — işçi kendi token sayımını bilmez; (d) M2'nin harness'iyle — harness LLM'i çağırmadığı için token'ı görmez (H-11'in çürüttüğü nokta).
- **Kapanır — tek gerçekçi mekanizma:** **transkript hasadı**. İB-66:126 "parent atfını TAMAMLANMIŞ mesajlar taşır" diyor; tamamlanmış assistant mesajları `usage` (+`modelUsage`, önbellek-okuma/yazma ayrımlı) taşıyor (:122). Yani veri oturum transkriptinde DİSKTE VAR, yalnız hiçbir araç onu okumuyor: `grep -n "usage\|token" tools/hareket-tablo.py` → **0 eşleşme** (kendim koştum). Hareket kütüğü zaten transkriptten araç çağrılarını hasat ediyor (CLAUDE.md §2) ama token alanlarına hiç dokunmuyor.
- **Gereken EK İŞ (M-1'in gerçek maliyeti):** `tools/hareket-tablo.py`'ye (ya da yeni bir `tools/token-hasat.py`'ye) mesaj-başına `usage` okuma + `parent_tool_use_id`/sidechain ile hücreye atıf + `hucre_anahtari`'na eşleme. gnhf tarafında karşılığı `.gnhf/runs/*/iteration-N.jsonl`'in `usage` alanını okumaktır (İB-66 Model A maddesi (c) ile aynı iş). **Bu, pilotun bir yan-ürünü değil, ayrı bir icra kalemidir.**
- **Ön-koşul sonda (1 çağrılık, ucuz):** tek bir Agent çağrısı yapılıp (a) dönüş paketinde `usage` var mı, (b) transkript satırında sidechain mesajının `usage`'ı ve parent atfı dolu mu — bakılır. **Bu sonda yapılmadan M-1'in kapanacağı SÖYLENEMEZ.**

**K-020 önerisine belirleyici etkisi:** M-1'in kapanması **ne M2'ye ne M3'e bağlıdır** — üçüncü ve ortak bir bileşene (transkript-usage hasadı) bağlıdır. Dolayısıyla tez-b'nin "önce M3 çünkü M-1'i ölçer" gerekçesi çöker (H-13 = X). K-020 sıralaması M-1'den **bağımsızlaşır**; kararın gerçek girdisi başka yerdedir (aşağıda §3).

### (iv) Manifest göç maliyeti — **17 manifest · {pipeline:16, loop:1} · matris için etkilenen dosya = 0**

```
ls veri/manifest/ | wc -l                    → 17
grep -h '"tur"' veri/manifest/*.json | sort | uniq -c
  →  1  "tur": "loop",
    15  "tur": "pipeline",
     1  "tur": "pipeline", "pist": "K-015", ...
     (= 16 pipeline + 1 loop = 17, TAMAMI sayıldı)
```
**Hüküm:** tez-c'nin "0 dosya" sonucu **D**; antitezin ara-sayımı ("14 pipeline, 1 loop, 2 hesaba katılmayan") **X** — 17'nin tamamı `tur` taşıyor, sayılamayan dosya yok. Matris eklenirse (S-A ya da S-B) **bugün değişmesi gereken manifest sayısı: 0**. Yeni birimler bu değerle doğar.
**Şerh (antitez Ç-03'ün haklı uyarısı):** bu 0, YALNIZ `matris` içindir. İB-65 kaynaklı ayrı bir **hibrit göçü 2 dosya** borcu vardır (`loop-kapanis-bu-oturum.json`: loop→hibrit, `sahada-damitma-s22.json`: pipeline→hibrit — ikisi de `ls` çıktımda mevcut). Karıştırılmamalı; sentez "toplam manifest göçü sıfır" dememeli.

### (v) İB-67 gerçekten "hemen koşulabilir" mi — **eksen VAR ama antitezin gösterdiği eksen YANLIŞ; "hemen" ŞARTLI**

`cc/gorev-2026-08-31-ib67-paper-aday-bulgu-envanteri.md` (kendi okumam):
- **:7 (S2)** — *"Çıktı: aday × yenilik-durumu (YOK-bulundu / KISMİ / DÜŞTÜ) × en-yakın-komşu × kanıt-URL tablosu, AS-OF damgalı."* → bu **kapalı bir ÇIKTI ETİKET kümesidir** (§2 Ö2'yi tam sağlar), **eksen DEĞİLDİR**.
- **:9 (Aileler, dik)** — *"A akademik literatür · B endüstri/araç pratiği · C iç envanter (web'siz)"* → **gerçek ikinci eksen budur**, kapalı 3-değerli küme, emirde açıkça yazılı.
- **:6 (S1)** — 8 aday ön-listesi (①-⑧) emirde birebir sayılı.
- **:11 (durma koşulu)** — "aday başına ≥3 bağımsız arama izi" · **:10** — izinli araçlar WebFetch/WebSearch.

**Hüküm:**
1. Tez-a'nın "ikinci eksen emirde açık yazılı değil" hükmü **X** (H-03) — aile ekseni yazılı.
2. Antitezin "8 aday × 3 kategori = 24 tam faktöriyel" türetimi **X** (H-32) — etiket uzayını eksen sanmış; bu, aile-1 §1'in "sık yapılan hata" olarak adlandırdığı ve İB-07'de bizzat düzelttiği hatanın tekrarıdır.
3. **Doğru matris:** `8 aday × 3 aile (A/B/C) = 24 hücre`, çıktı tipi `sema` = `{yenilik_durumu ∈ {YOK-bulundu, KISMİ, DÜŞTÜ}, en_yakin_komsu, kanit_url}`. §2 Ö1 sağlanır **kısmen**: yalnız `yenilik_durumu` alanı deterministik toplanabilir; `en_yakin_komsu`/`kanit_url` serbest metindir ve T1-T5'e girmez — şerh gerekir.
4. **"Hemen koşulabilir" mi:** **ŞARTLI EVET.** Şartlar: (a) C ailesi web'siz koşar ama A/B aileleri **WebFetch/WebSearch zorunlu** — LLM'siz/ucuz sınıfına GİRMEZ, envanterin "hemen koşulabilir" listesindeki İB-58/EK-1/EK-4 ile aynı maliyet sınıfında değildir; (b) hücre başına "≥3 bağımsız arama izi" şartı bir hücreyi tek Agent çağrısına eşitlemez → `hucre_tipi` `tek_cagri` DEĞİL, çok-aramalı bir birim; N_cagri = 24 varsayımı iyimser; (c) emrin kendi maliyet satırı (`:13`) **"kaba işçi-maliyet 1,5-2M token [?]"** diyor — bu, "hemen koşulabilir küçük iş" tanımına uymaz.

**Sonuç:** İB-67 **UYGUN**tur ve **eksen tanımı EKSİK DEĞİLDİR**; ama "hemen koşulabilir" listesine İB-58/EK-1/EK-4 ile aynı kefede konamaz — ayrı bir "eksen hazır, maliyet yüksek, web gerektirir" sınıfına konmalıdır.

---

## 3. ÇATIŞMA HÜKÜMLERİ (tez ↔ antitez, sayıyla)

| # | Çatışma | Tez | Antitez | **HAKEM HÜKMÜ** |
|---|---|---|---|---|
| Ç-A | **hücre-tavanı** | tez-c: ≤72 (=144/2) | Ç-04: 72 kalsın + oturum toplamı Σ ≤ 115 (0,8×144) | **İKİSİ DE X.** 72 ölçümden değil yuvarlamadan geliyor (gerekçesi de yanlış: 72'yi dolduran 51 hücre + 27 taban'dı); 0,8 payı TOKEN konvansiyonunun çağrı sayacına gerekçesiz taşınmasıdır (tez-c bunu doğru reddetmişti, antitez geri getiriyor). **Doğru kural sabit sayı değil, denklemdir: `N_hucre ≤ 143 − sayac_oturum_anlik`.** Planlama-zamanı tek sayı isteniyorsa: **116** (=143 − ölçülmüş taban 27, n=1 deneysel) ve bu oturumdaki TÜM matris hücrelerinin TOPLAMI içindir, kalem başına değil. |
| Ç-B | **güvenli N_cagri sınırı** | tez-d: sayac_oturum ≤ 114 | Ç-01: ~90-95 | **İKİSİ DE X, doğru sayı 113.** Hook `n >= 144`'te bloke ediyor → son izinli çağrı 143 → `sayac_oturum ≤ 143 − 30 = 113`. Antitezin 90-95'i çürük bir ×1,2-1,3 çarpan modelinden türedi (fazlalık çarpansal değil, toplamsal ve sabittir: 27). |
| Ç-C | **K-020 sırası: M2 mi M3 mü önce** | tez-b: M3 pilot → M2 (gerekçe: M3 M-1'i ölçer) | Ç-05: M-1'in kapanabilirliği doğrulanmadı | **Gerekçe X, sıra K.** M-1 ne M2 ne M3 ile kapanır (§2-iii): kapanma mekanizması **transkript `usage` hasadı**dır ve her iki modelde de AYNI ek iştir. Dolayısıyla M-1 sıralamayı **belirlemez** — tez-b'nin öneri gerekçesi kendi M3-risk satırıyla çelişiyor ("M-1 burada da AŞILMAZ, yalnız ertelenir"). **K-020 KARARI VERİLMEZ (emir yasağı).** Karar verilmeden önce gelmesi gereken iki ölçüm: **(1) usage-kaynağı sondası** — 1 Agent çağrısı; dönüş paketinde ve transkript sidechain satırında `usage` + parent atfı dolu mu; **(2) M-2 köprü denemesi** — promptfoo Python provider'ından tek bir CC Agent çağrısı gerçekten dönüyor mu (H-14). Bu ikisi gelmeden M1↔M2 "hücre başına ek yük" ekseni sayısal değil görecelidir ve M2'nin "13/13" kalite üstünlüğü **9/13'e** iner (H-11). |
| Ç-D | **İB-06 bugün koşulabilir mi** | tez-a: hayır | Ç-02: DAYANDI (hayır) | **ÇATIŞMA YOK — ikisi de haklı, D.** `veri/karar-borcu.jsonl` İB-06 `icra_borcu` alanını kendim okudum: "kapı 2/10 · H-kayıt 3/50 · damıtma 0/5 · emeklilik 1/10". Dördü de eşik-altı, beşincisi sıralı zincir. **İB-06'nın hiçbir alt-kalemi bugün koşulamaz** — bu, emrin "en güçlü aday" beklentisini çürüten bulgudur ve sentezin ön yüzüne çıkmalıdır. |
| Ç-E | **envanter dağılımı düzeltilmeli mi** | tez-a: İB-67 "eksen eksik" listesinde | Ç-07: İB-67 "hemen koşulabilir"e taşınsın (13→14 değil, aşağıdaki sayılar) | **Düzeltme GEREKLİ ama emirdeki "13→14" sayısı da yanlış.** awk sayımı: tablo **12 UYGUN / 23 UYGUN-DEĞİL = 35 hükümlü satır** (başlığın "27+4" = 31 iddiası X, H-07). İB-67 zaten **UYGUN** sınıfındadır — taşınma UYGUN toplamını DEĞİŞTİRMEZ (12 kalır); değişen şey alt-listedir: "hemen koşulabilir" **5 → 6**, "eksen tanımı eksik" **6 → 5**. Ve bu taşıma **şartlıdır** (§2-v): İB-67 web gerektirir, hücresi tek-çağrı değildir, emir kendi maliyetini 1,5-2M token `[?]` yazıyor → İB-58/EK-1/EK-4 ile aynı kefeye konmaz, **"eksen hazır · yüksek maliyet · web gerektirir"** diye üçüncü bir alt-listeye konmalıdır. İB-68 ise "eksen tanımı eksik"te KALIR (pazar-sinyali kapalı küme değil; ben emir dosyasını açmadım, antitezin bulgusu `[?]`). |

---

## 4. ŞEMA UYUM DENETİMİ (aile-1 üst otorite)

| Şema maddesi | Çelişen tez | **HÜKÜM** |
|---|---|---|
| **§1 Ö1/Ö2 (eksen `degerler` TAM küme; kardinalite dosyadan, metinden değil)** | **tez-d** (EKSEN#2 = [haiku, "[?]"] ama "Ö1 sağlanıyor" diyor) · **antitez Ç-07** (etiket uzayını eksen sayıyor) | **ŞEMA HAKLI, İKİ TEZ DE ÇELİŞİYOR.** [?] bir değer değildir → pilot bugün Ö1'i sağlamaz, koşulamaz (bloke edici). Antitezin İB-67 türetimi §1'in adıyla andığı "sık yapılan hata"nın tekrarıdır. |
| **§2 Ö1 tiplilik (¬serbest_metin)** | çelişen yok; ama **İB-67 hücresi** `sema` tipli ve alanlarının 2'si (en_yakin_komsu, kanit_url) serbest metin | **ŞEMA HAKLI, ŞERH GEREKİR:** `sema` tipli hücrelerde deterministik toplama YALNIZ enum alanları üzerinde tanımlıdır; serbest-metin alanları kütükte taşınır ama T1-T5'e girmez. Bu, §2'ye eklenmesi gereken bir açıklıktır. |
| **§2 Ö3 idempotency (aynı `hucre_anahtari` → çakışma olayı)** | **tez-d** pilotu | **ŞEMA HAKLI:** haiku kolonundaki 10 hücre (q06-q10 × tekrar1,2) kütükte zaten var (H-26). Anahtar `model`i içerdiği için teknik çakışma doğmaz ama koşum %33 mükerrerdir — şemanın ruhu (aynı işi iki kez koşma) ihlal edilir. |
| **§3 Karar 65 (LLM'siz deterministik toplama)** | çelişen yok | **UYUMLU.** tez-a serbest-metin işleri doğru eledi; tez-c toplama katmanına dokunmadı; tez-b M2/M3'te toplama ayrı adım. |
| **§4 iki taban + iki kapı** | **tez-d/aile-1'in kendi §4'ü**: `T_gnhf = 300k [ÖLÇÜLDÜ]` | **ŞEMA KENDİ İÇİNDE HATALI → §2-ii şerhi ile DÜZELTİLİR** (X). İki-taban ayrımının KENDİSİ (T_gnhf ≠ T_hucre) doğru ve korunur; hatalı olan yalnız damgadır. KAPI-2'nin (çağrı sayacı) eklenmesi tezlerce doğru uygulandı — tez-c bunu İB-66 Şablon-1'e taşıyarak boşluğu kapattı (uyumlu genişletme). |
| **§5 kütük 13 alan** | **tez-d** ("mevcut description-eval.jsonl uzantısı ya da yeni dosya") | **ŞEMA HAKLI:** mevcut kütük 8 alanlı ve `model` alanı `isci_model` adında (H-30). Aynı dosyaya append §3'ün girdi şartını bozar. "Uzantı" seçeneği KAPATILMALI. |
| **§6 Ö-A > Ö-B > Ö-C** | **antitez Ç-08** (§6.1 prozası ↔ §6.2/tez-d uygulaması) | **ŞEMA ESASTA HAKLI, METNİ ŞERH İSTER.** Öncelik sırası ve tez-d'nin Ö-C uygulaması (model DIŞ, H-29 = D) doğru. §6.1 Ö-A'nın proza cümlesine "matris-İÇİ hücrelerin ortak append-only kütüğe yazması bu kuralın kapsamı dışındadır (paralel-kapı birim-ARASI çalışır); POSIX kısa-satır append atomikliği varsayılmıştır, doğrulanmadı `[?]`" notu eklenmeli. |

**Genel şema hükmü:** Dört tezden **hiçbiri şemayı bilerek çiğnemiyor**; iki fiili çelişki var (tez-d §1 Ö1, tez-d §5 kütük) ve ikisinde de **ŞEMA HAKLIDIR**. Şemanın kendi iki metin kusuru (§4 "ÖLÇÜLDÜ" damgası, §6.1 Ö-A prozası) tezlerce değil hakemlikçe bulundu ve düzeltilmelidir.

---

## 5. SENTEZE ZORUNLU DÜZELTMELER (madde madde, rakamlı)

1. **Çağrı aritmetiği toplamsaldır, çarpansal değil.** Sentez ×1,2-1,3 güvenlik payını KULLANMAYACAK. Yazılacak: hücre başına çarpan **1,00**; matris-dışı oturum tabanı **27 çağrı** (İB-07 ölçümü, n=1, deneysel); ön-koşul **`N_hucre + sayac_oturum_anlik ≤ 143`**.
2. **Güvenli sınır 114 değil 113** (30 hücrelik pilot için). Hook `n >= 144`'te bloke eder; son izinli çağrı 143.
3. **Hücre-tavanı sabit 72 DEĞİL.** Sabit sayı isteniyorsa **116** (=143−27) ve bu, oturumdaki TÜM matris hücrelerinin TOPLAM tavanıdır, kalem başına değil. 0,8 payı (115) çağrı sayacına taşınmaz — o bir token konvansiyonudur.
4. **Aile-1 §4 TANIM bloğu düzeltilecek:** `T_gnhf = 300k [ÖLÇÜLDÜ]` → **`T_gnhf ≈ 300k [TÜRETİLDİ: 535k ÷ 2 iterasyon = 267,5k, +%12,1 yuvarlama; n=2; önbellek asimetrisi ayrıştırılmadı; önbellek-okuma DAHİL; kaynak k010-a3-loop-1:12; `[?]` teyit borcu KAPANDI]`** (tam metin §2-ii'de).
5. **M-1 pilotla KAPANMAZ.** Sentez "pilot M-1'i kapatır" cümlesini kaldıracak. M-1'in tek gerçekçi mekanizması **transkript `usage` hasadı**dır (İB-66:122 `result.usage`/`modelUsage` diskte VAR; :126 canlı delta forward EDİLMEZ ama tamamlanmış mesaj parent atfı taşır; `tools/hareket-tablo.py`'de `usage`/`token` grep'i **0 eşleşme**). Gereken ek iş: hasat script'ine mesaj-başına `usage` okuma + `hucre_anahtari` eşlemesi — **ayrı bir icra kalemi**.
6. **M-1'den önce 1 çağrılık USAGE-KAYNAĞI SONDASI konacak:** tek Agent çağrısında (a) dönüş paketinde `usage` var mı, (b) transkript sidechain satırında `usage` + parent atfı dolu mu. Bu sonda yapılmadan hiçbir modelin M-1'i kapatacağı yazılmayacak.
7. **K-020: M2'nin "13/13" kalite skoru 9/13'e indirilecek** — `token_giris/token_cikis/token_onbellek_okuma/sure_ms`'in kaynağı yoktur (madde 5). **Sıra kararı M-1'e bağlanmayacak** (M-1 her iki modelde de aynı ek işi gerektiriyor). **K-020 hükmü VERİLMEYECEK** — masada; verilebilmesi için gereken iki ölçüm: usage-kaynağı sondası (madde 6) + M-2 promptfoo↔CC Agent köprü denemesi.
8. **Pilot bugün KOŞULAMAZ — Ö1 ihlali.** EKSEN#2 `degerler` içinde `"[?]"` var; §1 Ö1 TAM küme şart koşuyor. 2. modelin TAM API snapshot id'si Salih'ten gelmeden pilot §1'i sağlamaz. Sentez bunu "onay bekliyor" değil **"şema-ihlali, bloke"** olarak yazacak.
9. **Pilot 30 hücre değil 20 hücre olmalı.** `veri/description-eval.jsonl` sayımı: q06-q10 için tekrar1 ve tekrar2 haiku'da ZATEN VAR (10 satır). 30 hücrenin 10'u mükerrer (%33 israf). Düzeltilmiş tasarım: **haiku kolonu yalnız tekrar3 (5 hücre) + yeni model tam 15 hücre = 20 hücre / 20 çağrı**; T4 (tekrar varyansı) yeni model üzerinden ölçülür, haiku'nun tekrar varyansı kütükte zaten mevcut.
10. **Pilot YENİ kütük dosyasına yazacak.** Mevcut kütük 8 alanlı (`altin_etiket, isabet, isci_model, kosum_id, secilen_skill, sorgu_id, tekrar, ts`) ve §5'in 13 alanının 8'i eksik/farklı adlı. "description-eval.jsonl uzantısı" seçeneği kapatılacak — karışık şema §3 deterministik toplamayı bozar.
11. **Manifest göçü: 17 dosya · {pipeline:16, loop:1} · matris için etkilenen 0.** Sentez ayrıca şerh düşecek: bu 0 YALNIZ `matris` içindir; İB-65 kaynaklı **hibrit göçü 2 dosya** (`loop-kapanis-bu-oturum.json`, `sahada-damitma-s22.json`) ayrı ve kayıtlı bir borçtur. Antitezin "14 pipeline + 1 loop + 2 sayılamayan" ara-sayımı sentezde KULLANILMAYACAK (yanlış).
12. **İB-67 sınıfı düzeltilecek.** İkinci eksen = emir `:9`'daki **dik aileler {A akademik, B endüstri, C iç envanter}** → **8 aday × 3 aile = 24 hücre**. Emir `:7`'deki {YOK-bulundu/KISMİ/DÜŞTÜ} **eksen DEĞİL, çıktı etiket uzayıdır** — antitezin "8 × 3 kategori" türetimi sentezde KULLANILMAYACAK (aile-1 §1'in adıyla uyardığı hata). Hücre tipi `sema`; toplama yalnız `yenilik_durumu` alanı üzerinde tanımlı.
13. **İB-67 "hemen koşulabilir" listesine ÇIPLAK taşınmayacak.** Web (WebFetch/WebSearch) zorunlu, hücre başına ≥3 arama izi şartı var, emrin kendi maliyeti 1,5-2M token `[?]`. Üçüncü bir alt-liste açılacak: **"eksen hazır · yüksek maliyet · web gerektirir"**. İB-68 "eksen tanımı eksik"te kalır.
14. **Envanter sayıları düzeltilecek:** başlık "27+4 satır" → gerçek **35 hükümlü satır (12 UYGUN / 23 UYGUN-DEĞİL)**. İB-67 taşınması UYGUN toplamını değiştirmez (12 kalır); "hemen koşulabilir" **5→6**, "eksen eksik" **6→5**.
15. **İB-06 bulgusu sentezin ön yüzüne çıkacak:** beş alt-borcun HİÇBİRİ bugün koşulamaz (kapı 2/10 · H 3/50 · damıtma 0/5 · emeklilik 1/10 · world-model sıralı zincir). Emrin "en güçlü aday" beklentisiyle çelişir; tez-a ve antitez bu noktada birleşiyor ve haklılar.
16. **Aile-1 §6.1 Ö-A'ya şerh:** "matris-İÇİ hücrelerin ortak append-only kütüğe yazması bu kuralın kapsamı DIŞINDADIR (paralel-kapı birim-ARASI çalışır, hücre-arası değil); POSIX kısa-satır append atomikliği VARSAYILDI, doğrulanmadı `[?]`".
17. **Aile-1 §2'ye açıklık:** `cikti.tip = sema` durumunda deterministik toplama YALNIZ enum/sayı alanları üzerinde tanımlıdır; serbest-metin alanları kütükte taşınır, T1-T5'e girmez.
18. **Pointer düzeltmesi (tez-c):** hook pointer'ları `9-10 / 27 / 22-24` → gerçek **`11 / 37 / 30-32`**. İçerik hükmü değişmiyor, pointer'lar okuyucuyu yanlış satıra gönderiyor (m.20).
19. **DESTEKLİ damgası düzeltmesi (tez-b):** promptfoo dokümanına atfedilen **"subprocess çağrıları"** ibaresi sayfada YOK; ya kaldırılacak ya "raporun ÇIKARIMI" olarak işaretlenecek. Doğrulanan çekirdek (HTTP-bağımsız, yerel model/özel mantık sarılabilir) DESTEKLİ kalır.
20. **`[?]` KALACAK kalemler (sentez sayı üretmeyecek):** İB-58'in 16 hücresi (AXI-STANDARDI ve İB-58 raporu hiçbir koşumda açılmadı) · EK-1'in 7×5=35'i (script açılmadı) · gnhf_iterasyonu hücrelerinin ajan-fren hook'undan geçip geçmediği · İB-68'in ikinci ekseni · `tools/paralel-kapi.py` satır iddiaları.

---

## 6. HAKEM YASAK BEYANI
K-020 kararı **VERİLMEDİ** (hüküm Salih'in masasında; verilebilmesi için gereken iki ölçüm madde 7'de). Hiçbir prototip inşa/koşum yapılmadı. Kanon (`core/`, `CLAUDE.md`, `kuyruk/`, `tools/`, `veri/manifest/`) salt-okundu, değiştirilmedi. Açmadığım hiçbir kaynağa DESTEKLİ damgası verilmedi (§Künye'deki `[?]` listesi).
