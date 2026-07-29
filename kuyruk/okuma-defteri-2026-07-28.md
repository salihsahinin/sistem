# Okuma Defteri — CC 07-26 teslimi (23 rapor, ~1 MB)

*Amaç: 8 kaynak (AI-to-AI) + 15 insan-yüzü (INSAN/SOZEL) raporun BAĞLAM KAYBI OLMADAN sindirilmesi. Yöntem: aile-bazlı partisyon — aynı konunun üç yüzü (kaynak + SOZEL + INSAN) aynı oturumda okunur, oturum sonunda hasat bu deftere yazılır. Sonraki oturum defterden devralır; sıcak bağlama güvenilmez (m.20/m.34). Salih emri 07-28.*

**İşbölümü:** Carvis 4 okuma vardiyasında TÜMÜNÜ okur + hasat yazar · Salih INSAN- (ve isterse SOZEL-) dosyaları kendi temposunda okur — Salih'in okuma notları/itirazları bu defterin "Salih şerhi" satırlarına ingest edilir.

## Vardiya planı (boyut-dengeli; dosyalar `raporlar/2026-07-26-*`)

| # | Aile(ler) | Dosyalar | Hacim | Durum |
|---|---|---|---|---|
| O1 | pasif-ogrenme | `pasif-ogrenme-atlas` + `SOZEL-pasif-ogrenme` + `INSAN-pasif-ogrenme` | ~276 KB | **DONE 07-28** (hasat aşağıda) |
| O2 | onerme-formu + lojik-kod | `LOJIK-onerme-formu` + `SOZEL-onerme-formu` + `lojik-kod-atlas` + `SOZEL-lojik-kod` + `INSAN-lojik-kod` | ~243 KB | BEKLİYOR |
| O3 | tech-stack + arac-entegrasyonu | `tech-stack-atlas` + `SOZEL-tech-stack` + `INSAN-tech-stack` + `arac-entegrasyonu` + `SOZEL-arac-entegrasyonu` + `INSAN-arac-entegrasyonu` | ~268 KB | BEKLİYOR |
| O4 | ajan-durma + arastirma-promptu + kod-entegrasyonu | `ajan-durma-atlas` + `SOZEL-ajan-durma` + `INSAN-ajan-durma` + `arastirma-promptu-atlas` + `SOZEL-arastirma-promptu` + `INSAN-arastirma-promptu` + `kod-entegrasyonu` + `SOZEL-kod-entegrasyonu` + `INSAN-kod-entegrasyonu` | ~300 KB | BEKLİYOR |

**Çapraz görevler (okuma sırasında toplanır):**
- Ç1 (r≈0,31 ters-yön): iki ucu O1 (`pasif-ogrenme §7.2`) ve O4 (`arastirma-promptu §4.2`) — her iki vardiya kendi ucunun kanıtını hasada yazar; uzlaştırma önerisi O4 sonunda derlenir.
- Askıdaki K14/K35/K39 geçen her yer işaretlenir (kural olarak KULLANILMAZ).
- S6 (yargı çevresi) için hukuk hükmü taşıyan pasajlar listelenir.
- Katman-1 karar masasına girdi olacak bulgular "KARAR-GİRDİSİ" etiketiyle yazılır.

## Hasat şablonu (her vardiya doldurur)
```
### O# HASAT — <tarih, yüzey>
- Ana hükümler (madde madde, kanıt damgasıyla):
- K-düzeltmelerinin etkisi (hangi eski hüküm düştü):
- KARAR-GİRDİSİ maddeleri:
- Ç1/S6/K39 dokunuşları:
- Salih şerhi (varsa):
- Sonraki vardiyaya devir notu:
```

## Hasatlar

### O1 HASAT — 2026-07-28, PC Cowork ana vardiya (Carvis/Fable)

**Okunan:** `pasif-ogrenme-atlas` (1181 satır, tam) + `SOZEL-pasif-ogrenme` (357 satır, tam) + `INSAN-pasif-ogrenme` (466 satır, tam).

**Raporun kendi kanıt kısıtı (her hükmün üstünde):** akademik host 10/10 ret ⇒ A1/A2/A3'te [D] YOK, tavan [K]; A4/A5/A7'de [D] var (teknik upstream depolar). Rapor karar-öncesi TARAMA'dır, KANIT değildir (§0/§20.5); akademik rakamlar borç-1 (yeniden doğrulama) kapanana dek hüküm taşımaz. A5-A8 tez şeritlerinin antitezi ilk teslimde eksikti; 07-26 ikinci turda A5-A21 için koştu (kaveat: araç kanıtları kesinti-öncesi turdan). A6 hâlâ AÇIK NÖTR.

**Ana hükümler (kanıt damgasıyla):**
1. **S1 [K, sağ çıktı]:** LLM kalıcı bellek altyapısı olmadan öğrenen-modelini oturumlar arası TAŞIMAZ ⇒ seviye/öğrenen modeli DOSYADA yaşamalı. Kapsül/defter mimarisi doğru; eksik = öğrenen-durumu alanı. Mekanizması hazır: alt-ajan `memory:` alanı (ilk 200 satır/25KB, [D]).
2. **S2 [K, sağ çıktı]:** LLM sentezinden öğrenme, özdeş olgu kümesinde bile daha sığ (7 deney, n=10.462; tek ekip, replikasyonsuz). "Carvis anlatsın, ben okuyayım" modelinin ölçüldüğü koşul bu. Ama üç eksen ayrılır (§5.4): okuma vs didinme → okuma kazanır (acemi); okuma vs önce-dene → dene kazanır (PS-I, 53 çalışma); okuma vs geri-çağırma → geri-çağırma kazanır.
3. **S3 [K, sağ çıktı]:** yanlış öğrenilen düzeltmeyle TAM silinmez (4 meta-analiz) ⇒ kalite kapısı üretim-anında = normatif değil EKONOMİK argüman (en ucuz nokta). "Sonra düzeltiriz" savunma değil.
4. **S4-S6 [D]:** bellek-benchmark rakamları kıyaslanamaz (Zep/Mem0 ihtilafı, LoCoMo %6,4 hatalı altın) · doğru asılma primitifi = progress deadline (ama H34: bu sürümde nöbetçi YOK) · 13 ADR şablonunun hiçbirinde "gözlenmiş sonuç" alanı yok ⇒ m.37 senaryo-defteri + SONUÇ alanı literatürde karşılıksız katkı alanı.
5. **Donma ölçümü [kendi telemetri, N=24]:** ağ hipotezi çürüdü; süre ↔ en-uzun-tek-duraklama r=0,95; 18 duraklamadan 2'si gerçek patoloji = ajanın KENDİ yazdığı Bash bekleme/yoklama döngüsü (600 s tavan = eski watchdog penceresiyle çakışık). 300 s eşiği %100 kesin AMA N=2 ⇒ GÖZLEM, kural değil (§9.6: n=30'da bile p95 GA kurulamaz). Ucuz tedbir üçlüsü: "Bash bekleme döngüsü yazma" kuralı · eşik indirimi · senkron alt-ajandan kaçınma → Salih kararı #6.
6. **A6 istatistik çerçevesi [açık nötr]:** sabit timeout = hazard hakkında örtük iddia · koşan iş = sağdan sansürlü · ağır kuyrukta "bekledik, bitmek üzeredir" TERS (Pareto'da MRL yaşla artar) · restart ölçütü CV>1 · watchdog kurulunca informative censoring → politika kendi verisini kirletir (L6) · eşik = Neyman-Pearson tipi "hangi hatayı sert kısıtlıyorsun" sorusu.
7. **Model B önerisi (m.37 3-model, §16):** "önce dene (Salih 2-3 cümle) → ders = düzeltme → ayrı referanslı doğrulayıcı → dosyaya kayıt". K1-K6 kısıtlarının 6/6'sını tek karşılayan model; V55'i iptal etmez, önüne adım ekler. A(hasat) K2/K3/K5'i karşılamıyor; C(tam hat) K-010 kapılarına ve ölçülmemiş ROI'ye takılı. → Salih kararı #1.
8. **K6 sert kısıt:** staj görevleri sistemin substratı OLAMAZ (anonimleştirme 3 yönden çürük; NDA türev materyali kapsar; tek yol prosedürel = yazılı izin). Substrat = JARVIS'in kendi karar akışı. K-022 ile temas eden en kritik satır.
9. **A7/A10 ajan bulguları:** çoklu-ajan %90,2 kazancı token'la karışık (varyansın %80'i token; token-eşitlenmiş kıyas YOK) · MAST: başarısızlığın %41,8'i spesifikasyon ⇒ mimari değil görev tanımı düzelt · model çeşitliliği ≫ persona çeşitliliği (V59 gerekçesi maliyet→KALİTE) · konsey MP mimarisi 9 benchmark'ın 8'inde kaybediyor (ama JARVIS m.40b'ye doğrudan transfer ETMİYOR — CoVe-Factored + hakem kesmiyor; geçen iki uyarı: zorunlu karşıtlık zararlı, aynı-model persona sahte çeşitlilik) · kendi işini denetleyen ajan pozitife sapar (öğrenme ajanının kendi dersini onaylayamamasının 2. bağımsız gerekçesi).
10. **A8 kategori:** sorun sayı değil — iki arıza: tek-eksenlilik (kaynak × teyit ayrılmalı, Admiralty/ICD-203) + X'in "çelişkili"yle "doğrulanamadı"yı birleştirmesi (STIX ValueError = formal kanıt). En yüksek getirili tek değişiklik: X'i ikiye böl + eksen-dışı YARGILANAMAZ. %87-köşegen dersi: derece sordurma, iki olgusal soru sor + kural üretsin. Hakemliğin makinesi etiketin YANINDA: diagnostiklik (= m.40b adversaryal-hayatta-kalma ilkesinin bağımsız doğrulaması), yanlılık bağımsızlığı, tiplenmiş saldırı, çelişkiyi veri olarak sakla, oy sayma yasağı.
11. **A9/A11 persona:** %85 = üçüncü-şahıs tahmin + insan-tutarsızlık paydası (ham ~0,72; bireysel r=0,20) · tarihsel figür = kamusal algı üretir (Dennett: uzman ayırt etme %51) · persona doğruluk artırmıyor + kişiselleştirme ikna artırıyor = öğrenme sisteminde en kötü bileşim · hukuk: Einstein (publicity 2005'te düştü) ≠ Karpathy (ELVIS Act, AB1836, CDPA m.84 ticari-kullanımsız); özel kullanım ↔ yayım eşiği dört dalda aynı yerde; Walters savunması (disclaimer) persona sistemine TRANSFER OLMAZ; Historical Figures/Himmler vakası: eğitim vaadi yanıltıcılığı ağırlaştırır.
12. **A12 senkron:** kısa-vade hedef (telefon-PC senkron) TEKNİK OLARAK MEVCUT [D]; K36/K37/K38 üçü aynı yönde: sistem sanılandan DAYANIKLI ("oturum kırılgan" varsayımlı tedbirler yeniden değerlendirilebilir). Routines kapı modeli: özerklik koşum-içi, denetim koşum-sonrası, yazma dal-kısıtlı — AMA K39 sonrası: o kapı otomatik değil, AÇIKÇA yapılandırılmalı. Giyilebilir ufku: [ARANAMADI] — sıfır doğrulanmış rakam.
13. **A13 compiler [en sağlam aile, D-hesap]:** kayıp = muğlaklaşma (%74,1) · epistemik güç %38,7 değişiyor · negatif kutup ~7× oynak · "sadık kal" talimatı TERS TEPİYOR (OR 4,85) ⇒ F1: niteleyici metnin DIŞINDA ayrı alanda yaşar (Carvis'in kendi şerh-erimesi vakasından doğdu). Tıp emsali: olgun rejimde bile güven-bilgisi uyumu %0,7.
14. **A14 graf:** hangi-kenarlar ≫ kaç-kenar (ters-U) · tek bozuk ajan avantajın tamamını siler · bellek zehri 27-31 turda ~%100, ölçek korumuyor · çare kenar değil ROL (Challenger+Inspector %96,4 geri kazanım) · "3-5 ajanla başla" · LLM'ler hata-oranı talimatını uygulayamıyor (%20 iste → %1,56 gerçekleşir) ⇒ kendi eval tasarımlarımıza da uyarı.
15. **A15 hukuk katmanı [tamamı K + K47 şerhli]:** asıl risk telif değil SÖZLEŞME · ajan asla kimlik doğrulamaz (tekil-nedensellik iddiası K40 ile düştü, etken ayakta) · URL geçerliliği ≠ atıf doğruluğu (link >%94, olgusal %39-77) · güvenli alıntı uzunluğu diye kural YOK · ajan kendi atıflarının son denetçisi olamaz.

**K-düzeltmelerinin etkisi (hangi eski hüküm düştü):**
- **H34 ⭐:** "async stall watchdog var ama dar" → nöbetçi bu sürümde HİÇ YOK; asılma tespiti tamamen ebeveynin işi. (Dikkat: INSAN dosyası §6 hâlâ eski hali anlatıyor — aşağıda.)
- **K33:** hafıza kırpması sessiz değil — ajana sayısal uyarı gider; boyut disiplini gerekçesi "uyarı ajana gider, Salih'e gitmez"e döndü (K-019 bağlantılı).
- **K34:** "heartbeat'siz iş durdurulamaz" bu sistemde yanlış — TaskStop task_id ile durdurur; ajanlar durdurulabilir, saptanamamaları ayrı sorun.
- **K35 ⭐ ASKIDA:** "eksen başına optimum ≈ 4" kaynaksız — kategori önerisinin tek somut sayısıydı; eksen ayrımı ayakta, sayı yalnız tasarım-tercihi olarak imzalanabilir.
- **K36/K37/K38:** oturum sürekliliği sınırlarının üçü tersine döndü (cihazlar-arası kalıcı; arka-plan oturumu terminal kapanışına dayanıklı; Desktop "Continue in" yerelden web'e itebiliyor).
- **K39 ⭐⭐:** "ajan yayım eşiğini kendi geçemez" ÇÜRÜDÜ (Routines onaysız push/PR mümkün) — güvenlik varsayımıydı; settings-deny'li push kilidimiz ayakta, ama bu varsayıma yaslanan korumasız yüzey taraması Salih masasında.
- **K40-K43:** tekil-nedensellik düştü (çok-faktör norm) · "her koşulda/tam güçle" mutlak nicelemeler düştü · "kanıt yok" → [ARANAMADI] çerçevesi (K42; K19/K20 ile aynı hata sınıfı) · DAG kısıtı yöntemin, alanın değil (K43).
- **K47 ⭐:** A11/A15'in tüm hukuk hükümleri ülkesiz; Türk hukuku hiç yoklanmadı ⇒ damgasız hüküm kullanılmaz (S6 masası).

**KARAR-GİRDİSİ maddeleri (Katman-1 masasına):**
- KG-1: **Model A/B/C** — Carvis önerisi B; §16.2 karşılaştırması sayısal, maliyetler [?] kestirim.
- KG-2: **Kategori şeması** — eksen ayrımı + X'in ikiye bölünmesi ayakta ve en yüksek getirili; kademe sayısı K35 gereği yalnız tasarım-tercihi olarak imzalanabilir. Uygulama şartı: derece sordurma, iki olgusal soru + kural.
- KG-3: **V59 gerekçe değişimi** — maliyet→kalite (A10/13.4 kanıtıyla); tetik öne çekilsin mi.
- KG-4: **Ajan donma tedbir üçlüsü** (ucuz, bugün uygulanabilir) — ama eşik rakamı N=2, kural olarak yazılamaz.
- KG-5: **Öğrenme ajanı** — tasarım paketi (§18.a: Bash yok, WebSearch yok, farklı model, ayrı doğrulayıcı, memory:project, eşleştirilmiş A/B eval) onayı AYRI, devreye alma (K-010 kapı-bağımlı) AYRI. Aleyhte cid­di not: S3 ⇒ "geri alması ucuz" yalnız dosya için doğru, Salih'in kafası için değil ⇒ K4 pazarlık dışı.
- KG-6: **Fikir konseyi (V6x)** — üç sert itiraz; yaşayabilir dar hal: farklı MODEL + üçüncü-şahıs format + erken-uzlaşma freni. Kutuda mı, dar deneme mi, düşsün mü.
- KG-7: **S6 yargı çevresi** + **K39 güvenlik taraması** (kapsülde zaten kayıtlı; bu vardiya kanıt adreslerini doğruladı).
- KG-8: **K-022 teması:** K6 kısıtı staj hattına doğrudan girdi — staj verisi JARVIS'e taşınmaz, yazılı izin yoksa. Staj oturumu açılırken bu sınır beyan edilmeli.

**Ç1/S6/K39 dokunuşları:**
- **Ç1 (r≈0,31) — bu ucun kanıtı (§7.2 + SOZEL §7.2-3):** hüküm "ÇÜRÜTÜLDÜ": künye iki bağımsız aramada hiçbir çalışmaya bağlanamadı; karşı kanıt [D]: MT-Bench resmî depo ">%80 uyum = insan-insan seviyesi", sağlık derlemesi r 0,40-0,94 medyan 0,69. AMA SOZEL antitez sütunu şerhi: *"bu düzeltme başka bir ailede yeniden açıldı; hüküm kapanmış sayılmaz."* ⇒ Ç1 uzlaştırması O4 (`arastirma-promptu §4.2` "açık") okunmadan derlenemez — plana uygun, O4 sonunda. Muhtemel uzlaşma çizgisi şimdiden görünüyor: §7.3 tablosu — yargıç performansı RUBRİK-BAĞIMLI (kusur-tespiti %94+ ↔ açık-uçlu kalite r=0,13-0,48); "0,31 çürütüldü" ile "yargıç açık-uçlu rubrikte zayıf" aynı anda doğru olabilir; künyesiz 0,31 rakamı her durumda kullanılmaz.
- **S6:** hukuk pasajları A11 (§14 tamamı: publicity/GDPR/AI Act/CDPA/iftira) + A15 (§A15 tamamı: sözleşme/ToS, lisans, alıntı, kişisel veri) — ikisi de bölüm-geneli K47 şerhli, ülkesiz, Türk hukuku yok. S6 karar girdisi hazır.
- **K39:** §A15-4 + §A12-4 çapraz okuma kritik: "insan kapısı koşum sonrası" bir garanti değil YAPILANDIRMA; K-009/K-010 tasarımına doğrudan girdi.
- **K14:** bu ailede yeni dokunuş yok (Cowork-yüzey testi 07-28 kapsülde; CC-yüzey testi cc/gorev-2026-07-28-1.md Görev 2'de).

**Salih şerhi:** *(henüz yok — Salih INSAN-pasif-ogrenme'yi kendi temposunda okuyacak)*

**Sonraki vardiyaya devir notu:**
1. **⚠️ TUTARSIZLIK BULUNDU — INSAN dosyası K-düzeltmelerini TAŞIMIYOR:** `INSAN-pasif-ogrenme` §6 hâlâ "bekçi var ama kör noktalı/yalnız async" anlatıyor (H34 öncesi hal), §7 "sayı olarak: eksen başına dört"ü damgasız/askısız sunuyor (K35 ihlali), §11 çürütülen üç oturum-sınırını (K36/K37/K38) hâlâ geçerli sınır diye listeliyor. Kapsüldeki "K1-K47 8 kaynak rapora uygulandı" kaydıyla tutarlı — INSAN dosyaları güncellenmemiş. **Salih bu dosyayı okumadan önce bilmeli; A13/F1 dersinin canlı örneği.** Düzeltme işi: ayrı küçük vardiya ya da CC görevi (m.8: üstü çizili + [K] gerekçeyle).
2. Ç1'in bu ucu hasatta; O4'te `arastirma-promptu §4.2` okunurken hangi ailede "yeniden açıldığı" tespit edilmeli (SOZEL şerhi aile adı vermiyor — muhtemelen arastirma-promptu'nun kendisi).
3. O2'ye özel bağ: A13 compiler bulguları (F1-F9) LOJIK/SOZEL-onerme-formu ailesinin zemininde — O2 okuması bu hasadın 13. maddesini referans alsın.
4. Akademik yeniden-doğrulama borcu (§20.2 liste: Bastani, Kestin, Keiser&Arthur, Sinha&Kapur, Staab, Park, Rocher) hâlâ açık; erişimi açık oturumda öncelikli.
