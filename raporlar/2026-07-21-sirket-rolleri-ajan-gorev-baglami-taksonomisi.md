# Şirket Rolleri → Ajan Görev-Bağlamı Taksonomisi

*CC yan-oturum araştırma sentezi · 2026-07-21 · Carvis*
*Kaynak: 5 paralel atlas-JARVIS koşumu (klasik kurumsal org · Anthropic org · frontier-lab arketipler · iş-doğası çerçeveleri · ajan-taksonomisi + model-eşleme). Bu belge öneri/referanstır; kanon kilitlemez (m.41 yetki bandı). Kanon adayı olması için ana-sıra ∧ Fable ya da Salih imzası gerekir — bkz. §"Karar kapısı".*

---

## 0. Bu belge nedir, ne işe yarar

Salih'in talebi: ilerde sahip olacağı **şirket-ajanlarını görev bağlamlarına göre sınıflandırmak** için bir iskelet. Örnek çapa: "bir Codex denetçi ajanı tasarlayacağız."

Bu belgenin ürettiği şey bir **dolap** değil, bir **triyaj-ve-yönlendirme kuralı**: bir işi al → doğasına göre etiketle → gereken yeteneği ve özerkliği *oku* → eşleşen ajan-arketipini ve model-katmanını ata → gate'i kur. Departman etiketi ("pazarlama", "finans") bir ajanı yönlendirmek için işe yaramaz çünkü her departman her risk/belirsizlik seviyesinde iş barındırır. Doğru eksen **işin doğası**dır.

Belge 5 katman: **A** klasik org (insan şirketi taban çizgisi) · **B** frontier-AI-lab farkı (modern şablon + Anthropic) · **C** iş-doğası eksen seti (sınıflandırma aleti) · **D** ajan-arketipleri + model eşleme · **E** sentez + JARVIS eşlemesi + çalışan örnek.

---

## 1. Yönetici özeti (TL;DR)

- **En önemli tek bulgu:** Sektör konsensüsü ve JARVIS'in kendi m.42 kanunu **aynı ilkeye** varmış. Bezos'un "tek-yönlü / iki-yönlü kapı" kararı = araştırmanın **D4 sonuç/geri-alınabilirlik** ekseni = JARVIS m.42'nin **Özgürlük(a) ≤ Toparlanabilirlik(hata(a))**'sı. Bir ajana ne kadar özerklik/yetenek vereceğini belirleyen ana kapı budur. Bunu bağımsız üç kaynağın doğrulaması, ekseni sağlam kılıyor.
- **İkinci ilke:** Yeteneği **zorluk × risk**'e göre eşle, sadece zorluğa değil. Güçlü modeller → yüksek-belirsizlik, düşük-geri-alınabilirlik, **doğrulama** ve **koordinasyon** rolleri. Ucuz/hızlı modeller → prosedürel, yüksek-hacimli icra; hata olursa yükselt (escalate).
- **Üçüncü ilke (senin Codex-denetçi örneğinin özü):** **Doğrulayıcı üreticiden yapısal olarak ayrı olmalı.** Kendini denetleyen model zayıf denetçidir. Bu, JARVIS'te senin *çelişki-kapısı* (m.16) refleksinin ajanlaşmış hali.
- **Sınıflandırma aleti:** 7 bağımsız iş-doğası ekseni (D1–D7) + 1 türetilmiş eksen (D8 = gereken özerklik = f(D3, D4)). Bir işi D1–D7 üzerinde etiketle, D8'i *oku*, ajan-arketipi + model-katmanı ata.
- **9 ajan-arketipi:** orkestratör · router/triyaj · planlayıcı · işçi/tool-user · **kritik/doğrulayıcı/judge** · araştırmacı/RAG · reflektör · guardrail · human-in-the-loop. Her biri belirli bir görev-bağlamına ve model-katmanına oturur.
- **Frontier-lab dersi:** modern AI-şirketi org'unda güvenlik tek kutu değil **ayrışmış uzman fonksiyonlar**; araştırma birinci-sınıf değer-üretimi; org'u kesen bir yönetişim/"frontier safety" katmanı var. Ajan filon da böyle ayrışmalı.

---

## Katman A — Klasik Kurumsal Fonksiyon Haritası

İnsan şirketinin taban çizgisi. 20 fonksiyon, üç **yapısal role** göre gruplu. Bu gruplama, ajan atarken *nasıl* davranacağını belirleyen en kullanışlı kaldıraç.

### A.1 Üç yapısal rol

| Yapısal rol | Fonksiyonlar | Ne verilir | Neye optimize | Gate yetkisi |
|---|---|---|---|---|
| **Değer-üretimi** | Ürün, Mühendislik, Tasarım, Veri, Araştırma, Satış, Pazarlama, Müşteri Başarısı | Yüksek hedef-güdümlü özerklik | Çıktı, verim, sonuç | Gate *tüketir*; stratejide yükseltir |
| **Etkinleştirici / destek** | İK, Operasyon, IT, İletişim, Strateji/BizOps, PMO, İş Geliştirme | Servis mandası içinde özerklik | Servis seviyesi, güvenilirlik, gecikme | Servis verir; kapasite çatışmasında yükseltir |
| **Yönetişim / kontrol** | Yönetici/Kurul, Finans (kontrol yüzü), Hukuk, Risk/Denetim, Güvenlik (kontrol yüzü) | Sınırlı, bağımsız, denetlenebilir | Önlenen risk, doğruluk, uyum | Gate'i **tutar**; değer-üretimini durdurabilir |

### A.2 20 fonksiyon — özet

**Değer-üretimi:** (1) Ürün Yönetimi *karar/önceliklendirme* · (2) Mühendislik *inşa/işlet* · (3) Tasarım/UX *tasarla/araştır* · (4) Veri & Analitik *analiz/modelle* · (5) Araştırma/Ar-Ge *keşfet/icat* · (6) Satış *ikna/kapat* · (7) Pazarlama *çek/mesajla* · (8) Müşteri Başarısı & Destek *elde-tut/destekle*.

**Etkinleştirici:** (9) İK/İşe-alım *işe-al/geliştir* · (10) Operasyon *icra/koordine* · (11) IT & Güvenlik *sağla/koru* (ikili doğa) · (12) İletişim/PR *mesajla/temsil* · (13) Strateji/BizOps *analiz/karar* · (14) Program/Proje Yönetimi (PMO) *koordine/teslim* · (15) İş Geliştirme & Ortaklıklar *müzakere/arayüz*.

**Yönetişim:** (16) Yönetici/Liderlik *karar/tahsis* · (17) Finans & Muhasebe *hesap/kontrol* · (18) Hukuk & Uyum *yönet/koru* · (19) Risk, Denetim & Kurumsal Yönetişim *temin/kontrol* (bağımsızlık şart) · (20) Kurumsal Geliştirme/M&A *değerle/müzakere*.

### A.3 Taşıyıcı ilke (ajan tasarımına doğrudan)

> **Bir yönetişim rolünü, denetlediği fonksiyonla asla aynı ajanda toplama.** Hem kod yazıp hem kendi güvenlik incelemesini onaylayan, ya da hem bütçeyi harcayıp hem harcamayı denetleyen ajanın gerçek kontrolü yoktur — **bağımsızlık, kontrolün kendisidir.** Tersine, değer-üretimini aşırı yönetişime boğmak (her küçük kararı bir kontrol kapısından geçirmek) şirketin dayandığı verimi boğar. Sağlıklı düzen: değer-üretimi ajanlarına hareket alanı, etkinleştirici ajanlara servis sözleşmesi, yönetişim ajanlarını **az sayıda, bağımsız ve hacimle değil vetoyla** silahlandır.

---

## Katman B — Frontier-AI-Lab Farkı (Modern Şablon + Anthropic)

Klasik org taban çizgisi. Modern bir AI-şirketi bunun üstüne ne ekliyor? Ajan filonun neden böyle ayrışması gerektiğinin dersi burada.

### B.1 Beş yapısal fark (Anthropic org'undan okunan)

1. **Araştırma birinci-sınıf değer-üretimi piları** — maliyet merkezi değil. Anthropic'te araştırma headcount'u Satış'la yarışıyor; "mühendisler çok araştırma, araştırmacılar çok mühendislik yapar" — sınır bilinçli bulanık.
2. **Güvenlik tek kutu değil, ayrışmış uzman fonksiyonlar:** Alignment Science · Interpretability · Frontier Red Team · Safeguards Research — hepsi *ayrı* takımlar. Klasik şirkette analoğu yok.
3. **Org'u kesen yönetişim/"frontier safety" katmanı:** Responsible Scaling Officer + kurul (Long-Term Benefit Trust) deployment'ı gate'leyebilir. Bir bankanın risk-uyum rejimine yakın ama finansal riske değil, **yetenek eşiklerine** dönük.
4. **Yeni GTM arketipi: Forward-Deployed / Applied AI Engineer** — müşteriye gömülü, üretim kodu yazan, sonucu *sahiplenen* mühendis. FDE ilanları 2025 Oca–Eyl arası ~%800 artmış.
5. **Klasik analoğu olmayan roller:** Model welfare · güvenlik-altyapısı-olarak yorumlanabilirlik (interpretability) · tehdit-istihbaratıyla çalışan Trust&Safety (Safeguards) · tehlike-alanına göre örgütlü Policy (Cyber/Biotech ulusal-güvenlik lead'leri).

**Anthropic pilar haritası (doğrulanmış Greenhouse departmanları):** AI Research & Engineering · Applied AI · Communications · Compute · Data Science & Analytics · Engineering & Design–Product · Finance · Legal · Marketing & Brand · People · Product Management Support & Ops · Public Benefit · Public Policy · **Safeguards (Trust & Safety)** · Sales · Security · Software Engineering–Infrastructure · Technical Education · Technical Program Management.

### B.2 AI-native rol arketipleri (klasikten sapan / net-yeni roller)

`explore · build · operate · judge/verify · interface · govern · curate` = iş-doğası anahtar kelime dağarcığı.

| Rol arketipi | Klasik analog | Çekirdek görev-bağlamı | Onu AI-native yapan | Olgunluk |
|---|---|---|---|---|
| Research Scientist | Akademik araştırmacı | Fikir üret, program tasarla | Frontier-ölçek deney; sanayide PhD/yayın | Yerleşik |
| Research Engineer | Lab teknisyeni | Deneyi kur, ölçekle, koştur | "Ölçekleme"nin kendisi zor araştırma; birinci-sınıf katkı | Yerleşik |
| Alignment / Safety | **Net-yeni** | Modeli değer-hizalı yap | İnceleme nesnesi modelin *değerleri ve arıza modları* | Yerleşik |
| Interpretability | **Net-yeni** (yakın: nörobilim/XAI) | Model içini ters-mühendisle | Tasarlanmamış bir artefaktın mekanistik bilimi | Yerleşik |
| Red-teaming | Güvenlik red-team | Zararları/tehlikeli yetenekleri sızdır | Hedef model *davranışı*; giderek *otomatik* | Yerleşik |
| **Evals / benchmark eng** | QA / test | Benchmark, LLM-judge, kalite izle | Olasılıksal çıktıyı derecelendirir; **evals PRD'nin yerini alır** | Yükselen→Yerleşik |
| Data curation / RLHF ops / annotation PM | Veri-girişi (angarya) | İnsan sinyalini seç, kalite-gate | Angaryadan **stratejik moat**a; research-ops | Yerleşik (yeniden-değerli) |
| ML infra / inference-opt eng | Infra/SRE/HPC | Eğitim kümesi + token-serving | Dev-model ekonomisi; **çıkarım eğitimi geçti** | Yerleşik |
| Forward-Deployed / Applied AI Eng | Solutions/field eng | Müşteriye göm, üretime taşı | Ürün, müşteri-başına *şekillenen* olasılıksal model | Yerleşik (patlıyor) |
| AI Product Manager | Product Manager | Olasılıksal ürünü sahiplen | Non-determinizm; evals = spec | Yerleşik |
| AI Engineer (applied) | (Net-yeni çerçeve) app/backend | LLM+RAG+araç+bellek orkestra | Modeli *bileşen* olarak kurar, sıfırdan eğitmez | Yerleşik |
| Prompt Engineer | **Net-yeni ama konsolide** | Girdi tasarımıyla güvenilir çıktı | Zirvesinden ~%80-90 düştü; AI Engineer'a katlanıyor | Yükselen ama sönen |
| DevRel (AI platform) | Developer advocate | Ekosistemi büyüt | Olasılıksal, hızlı-değişen platform + sorumlu kullanım | Yerleşik |
| Trust & Safety (model çıktısı) | İçerik moderasyonu | Kullanım politikasını uygula | "Policy-as-prompt"; guardrail modelleri | Yerleşik |
| **Agent / Agentic AI Engineer** | **Net-yeni** (AI Eng uzmanı) | Otonom araç-kullanan sistem kur/işlet | Artefakt *eylemde bulunur*; otonomi-eval + guardrail | Yükselen (en hızlı) |
| Model welfare researcher | **Net-yeni, analog yok** | Modelin ahlaki statüsünü değerlendir | Kendi artefaktına ahlak felsefesi + davranış bilimi | Spekülatif (öncü) |

### B.3 Beş yapısal kaymanın özü (neden bu roller var)

1. **Doğrulama/değerlendirme birinci-sınıf iş oldu, bir faz değil.** Olasılıksal davranış → "çalışıyor mu?" sonda bir QA kapısı değil, sürekli uzmanlık disiplini. Baskın fiil: `judge/verify`.
2. **Forward-deployed hibrit mühendislik+danışmanlık, kurumsal motorun kendisi.**
3. **Güvenlik/hizalama/yönetişim bir mühendislik disiplini oldu, uyum fonksiyonu değil.** Kod yazan, deney koşan araştırmacılar; "policy-as-prompt", guardrail modelleri, otomatik saldıran modeller.
4. **Veri seçimi angaryadan stratejiye geçti** — küratörlük daha küçük modelleri büyüklere yendirebiliyor.
5. **Model, birinci-sınıf mühendislik alt-tabanı** → tüm bir uygulamalı yığın + otonomiye itiş (agent engineering).

---

## Katman C — İş-Doğası Eksen Seti (SINIFLANDIRMA ALETİ)

İşi *departmana* göre değil *doğasına* göre etiketleyen minimal, dik eksen seti. Yerleşik çerçevelerden (March keşif/işletim · Bloom→iş-fiilleri · Cynefin belirsizlik · Bezos kapı · Graham maker/manager · OODA tempo · RACI) süzülmüş. **Sınıflandırmanın kalbi bu.**

| # | Eksen | Ne ölçer | Seviyeler / kutuplar | Dayanak |
|---|---|---|---|---|
| **D1** | **Çalışma-modu** | Bilinene ilişki | Keşfet ←→ İşlet | March 1991 |
| **D2** | **Bilişsel eylem** *(kategorik)* | Dünyaya yapılan asıl işlem | Üret · Dönüştür · **Karar** · **Doğrula** · Koordine · İcra · İzle | Bloom(rev); DIKW; RACI |
| **D3** | **Belirsizlik/yapı** | *Yol* önceden biliniyor mu? | Açık → Karmaşık(complicated) → Kompleks → Kaotik | Cynefin |
| **D4** | **Sonuç** *(KAPI)* | Geri-alınabilirlik × bahis | İki-yönlü/düşük → Geri-alınabilir-pahalı → Zor-geri-alınır → **Tek-yönlü/yüksek** | Bezos Type 1/2 |
| **D5** | **Koordinasyon yükü** | Üretmek mi, başkalarını hizalamak mı | Solo-maker ←→ Çok-taraflı koordinatör | Graham; RACI |
| **D6** | **Zaman-ufku/tempo** | Döngü hızı & etki ufku | Reaktif → Operasyonel → Stratejik | OODA |
| **D7** | **Yüzey/arayüz** | Şirket dışına patlama yarıçapı | İç → Sınır → Dış | RACI(Informed) |
| **D8** | **Gereken özerklik** *(TÜRETİLMİŞ)* | Verilecek bağımsız eylem → ajan katmanı | Yardımlı → Denetimli → Otonom | *= f(D3, D4), D7 ile büyür* |

**Kritik ayrım:** D8 bir *girdi etiketi değil, çıktıdır*. `özerklik = f(D3 belirsizlik, D4 sonuç)`, D7 yüzey ile büyütülür. Düşük-belirsizlik + iki-yönlü-kapı → **Otonom** (ucuz ajan, yap-ve-düzelt). Yüksek-belirsizlik + tek-yönlü-kapı → **Yardımlı / human-in-loop** (en güçlü ajan + inceleme). Türetilmiş olması, taksonomiyi bir dolaptan bir **atama kuralına** çeviren şey.

**Diklik notu:** D1 (hedef-bilinene) ve D3 (yol-yapısı) gerçekten bağımsız — açık-uçlu bir durumu işletebilir (bilinen iyi hâle dönme = novel outage söndürme), prosedürel bir işi keşfedebilirsin (temiz A/B testi). D4 ile D7 ikisi de "risk"e değer ama farklı: D7 bahsi *büyüten* bir katkı; D4 birleşik geri-alınabilirlik×bahis verdicti. İç iş de tek-yönlü olabilir (prod DB silme), dış iş iki-yönlü olabilir (kolay-silinen sosyal post). Gerçek korpusta D3/D4 ve D4/D7 arasında korelasyon bekle — tam bağımsız saymadan önce etiketli örnekte doğrula.

---

## Katman D — Ajan-Arketipleri + Model Eşleme

Bir işi D1–D7 etiketleyip D8'i okuduktan sonra, **hangi ajan-arketipine** ve **hangi model-katmanına** gideceği. Sektör 9 arketip etrafında birleşiyor.

| Ajan rolü / deseni | Ne yapar | Oturan görev-bağlamı | Model-katmanı |
|---|---|---|---|
| **Router / triyaj / dispatcher** | Sınıflar, uzmanı *ve/veya* model-katmanını seçer; cevaplamaz | Yüksek-hacim ön kapı | **Ucuz/hızlı** (hatta kural/embedding) — <100ms |
| **Orkestratör / supervisor** | Çalışma anında böler, delege eder, sonuçları sentezler | Karmaşık, öngörülemez çok-adımlı hedef; koordinasyon | **Frontier / en güçlü** — yüksek belirsizlik + bütün-iş tutarlılığı |
| **Planlayıcı / decomposer** | Hedefi sıralı, bağımlılık-farkında alt-göreve çevirir | Novel/açık-uçlu, önce strateji | **Güçlü → frontier** — plan kalitesi her şeyi gate'ler |
| **İşçi / executor / tool-user** | İyi-tanımlı alt-görevi yapar; araç/API çağırır | Yüksek-hacim, prosedürel, iyi-spesifize icra | **Ucuz/hızlı**, hatada yükselt — asıl tasarruf katmanı |
| **Araştırmacı / retriever (RAG)** | Bağlam toplar, topraklar | Bilgi-toplama, olgu-topraklama | Retrieval **ucuz-orta**; sentez **orta-güçlü** |
| **Reflektör (öz-düzeltme)** | Kendi çıktısını eleştirir, revize eder | Tek ajanın çıktısında sınırlı kalite artışı | **İşçiyle aynı katman** (kendisi döngüde) — ucuz ama zayıf |
| **Kritik / doğrulayıcı / judge** | Başka ajanın çıktısını ölçüte karşı *bağımsız* puanlar | Kalite kapıları, yüksek-bahis çıktılar, kabul-öncesi | **Güçlü → frontier**, ve üreticiden **farklı** — zayıf judge, judge'suzdan kötü |
| **Guardrail / safety / policy** | I/O'yu paralel doğrular; durdurabilir | Dış-yüzeyli, hassas-veri, eşik-üstü eylemler | **Amaca-özel/ucuz-hızlı classifier** + sert kurallar — akıl-yürütme katmanı *değil* |
| **Human-in-the-loop / escalation** | Akışı duraklatır; insan onaylar/karar verir | Geri-alınamaz, mali/hukuki ağır, dış-görünür, güvenlik-kritik | **İnsan** (model yok) |

### D.1 Model-eşlemenin taşıyıcı ilkeleri (2025–2026 konsensüsü)

1. **Yeteneği *zorluk × bahis*'e göre eşle, zorluğa değil.** Güçlü modeller → yüksek-belirsizlik, düşük-geri-alınabilirlik, doğrulama, koordinasyon. Prosedürel yüksek-hacimli icra → ucuz/hızlı, hatada yükselt. Bahis zorluğu ezebilir: *kolay ama geri-alınamaz* eylem ucuz katmana güvenilmez.
2. **Doğrulayıcı/kritiği executor'dan ayrı tut.** Öz-yansıma yardımcı ama kısıtlı; model kendi işinin zayıf denetçisi. Bağımsız (ideal: güçlü/ensemble) judge, üreticinin göremediğini yakalar; judge güçlüyse üretici ucuzlayabilir. Judge'ı position/length bias ve prompt-injection reward-hacking'e karşı koru.
3. **Guardrail'i dış-yüzeyli ve geri-alınamaz eylemlere koy; yüksek-patlama sınırında insana yükselt.**
4. **Yönlendir, cevaplama; her uzmanın işini dar tut.** Ön router near-free (gecikme <100ms). Yalnız gerçekten farklı talimat/araç/politika gerektiğinde dallara ayır.
5. **Basit başla; yetenek ve ajanı ancak basit çözüm yetmeyince ekle** (Anthropic'in ana çapraz-kesen kuralı).

**Nicel çapa (peer-reviewed):** RouteLLM (ICLR 2025) — LLM-judge-artırımlı yönlendirmeyle *%95 kalite, güçlü-model çağrılarının yalnız %14'üyle* (~%75 maliyet düşüşü). Yaygın "%40-85 tasarruf" başlıkları ise vendor-raporlu, iş-yüküne bağlı — yön doğru, garanti değil. Zayıf halka: zorluğu *önceden tahmin* etmek — bu yüzden bahis-tabanlı guardrail ve ayrı doğrulayıcı, kusurlu yönlendirmenin etrafında bir emniyet ağı olarak var.

---

## Katman E — Sentez: Sınıflandırma Yöntemi + JARVIS Eşlemesi

### E.1 Adım adım kural (her yeni ajan/görev için)

1. **İşi tanımla** (ajanı değil — ajan işten türeyecek).
2. **D1–D7'yi etiketle** (D2 kategori, gerisi seviye).
3. **D8'i oku:** `özerklik = f(D3, D4)`, D7 ile büyüt.
4. **Ajan-arketipini seç** (Katman D tablosu — asıl fiil D2 belirler: Doğrula→kritik/judge, İcra→işçi, Karar+koordine→orkestratör, İzle→monitor/guardrail...).
5. **Model-katmanını ata** (arketip + D8). Yüksek-belirsizlik/tek-yönlü/doğrulama/koordinasyon → güçlü. Prosedürel/iki-yönlü/yüksek-hacim → ucuz.
6. **Gate'i kur:** D4 tek-yönlü ∨ D7 dış → guardrail + (gerekirse) human-in-loop onay kapısı. Yönetişim rolüyse → **üreticiden ayrılığı yapısal garanti et**.
7. **Kaydet** (pano kartı + m.42 pozitif-yetki listesi).

### E.2 JARVIS'in kendi kanunuyla birebir örtüşme (önemli)

Araştırma, JARVIS'in bağımsız vardığı kanonu doğruluyor — bu, eksenlerin sağlamlık kanıtı:

| Sektör bulgusu | JARVIS kanonu | Eşleşme |
|---|---|---|
| D4 sonuç/geri-alınabilirlik kapısı (Bezos tek/iki-yönlü) | **m.42: Özgürlük(a) ≤ Toparlanabilirlik(hata(a))** | Aynı ilke — özerkliği hatanın geri-alınabilirliği gate'ler |
| Doğrulayıcı ≠ executor; bağımsız kritik | **m.16 çelişki-kapısı** (Carvis'in kendi doğrulama refleksi) | Codex-denetçi = m.16'nın ajanlaşmış hali |
| Ensemble bağımsız judge, tek judge'dan iyi | **m.42 çeşitlilik-bütçesi** + **kararlı-prefix=koşum deseni** | Çeşitlilik varyansı düşürür |
| Bileşik gevşetme yasağı / katı-başlangıç | **m.42 bileşik gevşetme + katı-başlangıç** | Özerkliği bir kerede değil kademeli aç |
| Guardrail dış-yüzeyli/geri-alınamazda; PreToolUse | **m.30 PreToolUse ön-koşulu** | Eylem-öncesi gate |
| Model-yetenek eşleme | **model-hiyerarşi: JARVIS=Fable · lider=Opus/bir-altı** | Aşağıdaki katman eşlemesi |

### E.3 JARVIS model-katman eşlemesi

- **Fable (JARVIS, en güçlü)** → orkestratör · planlayıcı · **kritik/doğrulayıcı** · yüksek-belirsizlik + tek-yönlü-kapı işleri · nihai karar (ana-sıra).
- **Opus / bir-altı (lider)** → güçlü ama Fable-altı işler; alt-orkestrasyon, zor executor, orta-yüksek belirsizlik.
- **Ucuz/hızlı (Haiku vb.)** → router/triyaj · prosedürel yüksek-hacim işçi/tool-user · guardrail-classifier · retrieval.
- **Dış-araç (ör. Codex)** → uzman motor olarak bir arketipe *takılır* (aşağıdaki örnek). Rolü eksenler belirler, motoru bir uygulama detayı.
- **İnsan (Salih / Carvis)** → tek-yönlü-kapı + yüksek-bahis onay kapısı; Katman-1 kararları (m.31).

---

## Çalışan Örnek — "Codex Denetçi Ajanı"

Salih'in çapası. Taksonominin sınavı: soyut eksenler gerçek bir ajanı yerleştirebiliyor mu?

**İş tanımı:** başka bir ajanın (ya da Carvis'in) ürettiği kodu/diff'i, bir ölçüte (doğruluk, güvenlik, stil, regresyon) karşı bağımsız denetleyen; Codex motorunu kullanan bir ajan.

**Eksen-eksen etiketleme:**

| Eksen | Değer | Gerekçe |
|---|---|---|
| D1 Çalışma-modu | **İşlet**-baskın (bilinen ölçüte karşı kontrol), bilinmeyen arıza avında keşif atakları | Denetim = standarda karşı doğrulama; ama edge-case avı red-team tadında keşif |
| D2 Bilişsel eylem | **Doğrula** (asıl), ikincil Analiz/Üret (rapor üretir) | Denetçinin çıktısı bir geç/kal verdicti + gerekçe |
| D3 Belirsizlik | **Karmaşık → Kompleks** | Kod doğruluğu/güvenliği uzmanlık ister; gizli hata keşfi öngörülemez yol |
| D4 Sonuç | **İkili nüans:** kendi verdicti *iki-yönlü* (Carvis/Salih ezebilir), ama **tek-yönlü-kapı hatalarını yakalamak** için var → false-negative *sessiz* ve pahalı | Bu yüzden yüksek-özen/güçlü-model tarafı |
| D5 Koordinasyon | Solo-maker (diff'in derin okuması) + hafif koordinatör (rapor/eskalasyon) | Tek-threadli derin okuma, sonra bildirir |
| D6 Zaman-ufku | Operasyonel/Reaktif (artefakt-başına tetiklenir) | Her PR/diff'te koşar |
| D7 Yüzey | **İç** (iç işi denetler); dış-yüzeyli release'i gate'lerse efektif bahis yükselir | İç ama gate'lediği şey dışarı çıkabilir |
| **D8 Özerklik (türetilmiş)** | **Yargılamada otonom, eyleme geçmede DEĞİL** | Verdict üretmek otonom olabilir; ama kendi verdictine dayanıp geri-alınamaz bir şeyi (merge/deploy) *onaylamak* ona bırakılmaz |

**Yerleşim:** Arketip = **Kritik/Doğrulayıcı/Judge** (evaluator-optimizer'ın değerlendirici yarısı). Model-katmanı = **Fable-tier / güçlü** (doğrulama = güçlü-model işi; zayıf judge judge'suzdan kötü). Motor = **Codex** (güçlü kod-akıl-yürütme, verify-rolü katmanına uyar) — kabul edilebilir bir uygulama seçimi.

**İki demir kural (araştırma + JARVIS kanonu birlikte):**
1. **Üreticiden yapısal ayrılık** — Codex-denetçi, kodu üreten ajanla asla aynı ajan olmayacak (separate-verifier + **m.16 çelişki-kapısı** + Katman A.3 "bağımsızlık kontrolün kendisidir").
2. **Yargılar ama merge etmez** — verdict advisory; geri-alınamaz eylem (merge/push/deploy) bir **human-in-the-loop / Carvis onay kapısına** eskale olur (m.30 PreToolUse · m.31 publish=Katman-1). Denetçinin "geç" demesi otomatik merge'i tetiklemez.

**Bonus (çeşitlilik-bütçesi):** yüksek-bahis diff'lerde tek Codex-denetçi yerine *bağımsız iki lens* (ör. correctness-judge + security-judge) çoğunluk oyuyla — m.42 çeşitlilik-bütçesi + ensemble-judge bulgusu.

→ **Taksonomi sınavı geçti:** soyut eksenler somut ajanı tek bir hücreye (güçlü-model, bağımsız kritik, yargıla-ama-eyleme-geçme, iç-yüzey-ama-dış-gate) oturttu.

---

## Çalışan Örnek 2 — "JARVIS Araştırma Ajanı" (Salih'in kendi ajanı)

Salih'in ikinci çapası: "kendime bir araştırma ajanı kurmak güzel olur; Atlas'ı ben geliştirmedim ve canlı bir ajan değil." Taksonomi bunu neden **ideal ilk ajan** yaptığını *gerekçelendiriyor*.

**İş tanımı:** bir soruyu al → çok-kaynaklı topla → iddiaları adversaryal doğrula → sentezle → kaynaklı rapor ver. (Bu oturumda 5 paralel atlas koşumuyla yaptığım şeyin ta kendisi.)

| Eksen | Değer | Gerekçe |
|---|---|---|
| D1 Çalışma-modu | **Keşfet**-baskın | Araştırma = açık-uçlu keşif |
| D2 Bilişsel eylem | **Üret/Dönüştür** (sentez) + güçlü **Doğrula** (iddia-denetimi) | Topla→sentezle→doğrula bileşiği; fan-out yapar |
| D3 Belirsizlik | **Kompleks** | Yol eyleyerek keşfedilir; öngörülemez |
| D4 Sonuç | **İki-yönlü / düşük** ← *kilit* | Rapor advisory; tümüyle geri-alınabilir (yok say, yeniden koş) |
| D5 Koordinasyon | Solo → hafif **orkestratör** | Alt-aramalara fan-out (bu oturumdaki 5 paralel gibi) |
| D6 Zaman-ufku | Operasyonel → Stratejik | Ağır-orient, deliberatif |
| D7 Yüzey | **İç** (yayımlarsa → Dış, o zaman D4 yükselir: m.14/m.31 publish kapısı) | İç karar için; CV'ye/dışarı çıkarsa bahis artar |
| **D8 Özerklik (türetilmiş)** | **Eylemde OTONOM güvenli, ama YÜKSEK-yetenek gerekli** | D4 iki-yönlü → bırak koşsun; D3 kompleks → kalite için güçlü model. *Nadir rahat kombo.* |

**Yerleşim:** Arketip = **Araştırmacı/retriever + orkestratör + ayrı doğrulayıcı** (deep-research deseni). Model = retrieval **ucuz**, sentez/verify **güçlü** (Fable/Opus).

**Neden ideal İLK ajan (taksonomi-gerekçeli):** D4 iki-yönlü-kapı → toparlanabilirlik yüksek → **m.42: Özgürlük(a) ≤ Toparlanabilirlik(hata(a))** bol özerklik veriyor. Hatanın maliyeti ucuz (kötü rapor = yeniden koş), o yüzden yüksek-yetenekli olmasına rağmen **otonom devri düşük-riskli**. K-010 "ilk canlı ajan" denemesi için en güvenli aday sınıfı budur.

**Atlas vs. JARVIS-araştırma-ajanı vs. "canlı ajan" — üç ayrı şey (m.30):**
- **Atlas** = harness'in sağladığı, JARVIS'in geliştirmediği bir *subagent aracı*. JARVIS terminolojisinde **canlı ajan değil**; m.30 diliyle *otomasyon/araç* (tetiklersin, tetik devrine kadar) — kalıcı kimlik ya da m.42 delege-yetki taşımaz. Salih'in sezgisi doğru.
- **JARVIS araştırma ajanı** = Atlas'ı (ya da deep-research'ü) **JARVIS kimliği + canon + koşum-deseniyle** saran senin ajanın. Tohumu zaten var: `atlas-kosum` skill (m.40b) + `deep-research` skill. **Non-canlı / tetiklenen formda ŞİMDİ kurulabilir** (bu oturumda fiilen koştu).
- **Tam "canlı" form** (kalıcı kimlik + prompt-devri + delege yetki) = m.30/**K-010 kapsamı**, 2 hafta temel-katman sorunsuz sonrası açılır. Yani "canlı" olması gated; "araç/koşum" olması değil.

→ **Taksonomi ikinci sınavı da geçti** — ve bir yönetim çıkarımı verdi: **araştırma ajanı, düşük-bahisi (D4) sayesinde ilk canlı-ajan denemesi için en güvenli sınıf.**

---

## Tasarım Notu — Uzmanlaşmış Ekip-Lideri (domain orchestrator) + Emergent İlk Filo

Salih'in üçüncü çapası: "araştırma üzerine eğitilmiş bir ajan, ekip lideri olarak görevi daha iyi yönetebilir."

**İlke (doğru ve az-kullanılan kaldıraç):** Orkestratör arketipinde asıl kaldıraç *decomposition kalitesi* — plan her şeyi gate'ler (Katman D). Lideri de **alanında uzmanlaştırmak** (yalnız işçileri değil) decomposition'ı iyileştirir: iyi bir araştırma-lideri hangi alt-soruların önemli olduğunu, iddiaların nasıl doğrulanacağını ve "iyi"nin neye benzediğini bilir. Yani domain-specialist orkestratör > generic orkestratör — *o domain'de*.

**Ama karşı-değer:** liderin en zor becerisi koordinasyon + bütün-iş tutarlılığı, kısmen domain-genel. Cross-domain işte aşırı-uzmanlaşmış lider dezavantaj olur. Çözüm = **iç içe supervisor (nested/hierarchical)**: üstte generalist top-orkestratör (Fable / Carvis / ana-sıra), altında **domain-lead**'ler — araştırma-lideri kendi işçi+doğrulayıcısını yönetir. (LangGraph nested-supervisor bunu birinci-sınıf destekler.)

**JARVIS eşlemesi:** araştırma-lideri = **lider (Opus/bir-altı)** katmanı; **Fable** üstte kalır (ana-sıra/nihai). Uzmanlaşma mekanizması (non-canlı JARVIS'te) = **skill/koşum-deseni** (`atlas-kosum`), fine-tune değil. Bu oturumun şekli tam buydu: Carvis (lider) 5 atlas-işçiyi orkestre etti.

**Ayrılık korunur:** araştırma-lideri kendi ekibinin çıktısının *tek* yargıcı olmamalı — denetçi ayrı kalır (**m.16 çelişki-kapısı** + separate-verifier).

**Emergent İlk Filo — Salih'in 3 çapası birleşince ders-kitabı bir araştırma ekibi çıkıyor:**

| Salih'in çapası | Ajan-arketipi | Görev-bağlamı özeti | Model-katmanı |
|---|---|---|---|
| Araştırma-lideri | **Orkestratör** (domain-uzmanı) | Keşfet · Karar/Koordine · Kompleks · böl-delege-sentezle | Lider (Opus) |
| Araştırma ajanı | **Araştırmacı/retriever + işçi** | Keşfet · Üret/Doğrula · iki-yönlü · otonom-güvenli | Retrieval ucuz / sentez güçlü |
| Codex-denetçi | **Kritik/doğrulayıcı** (bağımsız) | İşlet · Doğrula · yargıla-ama-eyleme-geçme | Güçlü (Fable-tier), üreticiden ayrı |
| (üstte) Salih/Carvis | **Human-in-the-loop / ana-sıra** | tek-yönlü-kapı onayı, Katman-1 | İnsan / Fable |

= orkestratör-işçiler + **bağımsız doğrulayıcı** + insan-gate. Taksonomi tam bir hücre kümesine oturtuyor; **araştırma = D4 iki-yönlü** olduğu için K-010 ilk-filo adayı olarak tutarlı ve düşük-riskli.

---

## Karar Kapısı (ana-sıra / Fable için)

Bu bir CC yan-oturum çıktısı (öneri, kanon değil). Ana-sıra ∧ Fable ya da Salih imzasına açık kararlar:

- **K1 — D1–D8 eksen setini resmi ajan-sınıflandırma standardı yap?** (Öneri: **Evet, deneysel-damgayla** — m.29. Gerekçe: JARVIS m.42 ile birebir örtüşüyor, dolayısıyla kanonla çelişmiyor, onu operasyonelleştiriyor. Karşı-temel: 8 eksen küçük bir filoya ağır gelebilir; D3/D4 korelasyonu gerçek korpusta test edilmeli.)
- **K2 — Katman D model-eşlemesini JARVIS model-hiyerarşisine (Fable/Opus/ucuz) bağla?** (Öneri: **Evet** — zaten m.30 model-hiyerarşisiyle uyumlu; bu tabloyu onun uygulama kılavuzu yap.)
- **K3 — "Ajan-sicili" kartlarına eksen-etiketi alanı ekle?** (pano şablonu v2'ye D2+D4+D8 alanları — küçük, deneysel; Carvis Katman-2'de yapabilir, veto=revert.)
- **Açık borç:** eksenleri gerçek etiketli örnekte doğrulama (diklik varsayımı); wiki sayfa adayları: `[[gorev-baglami-eksenleri]]` · `[[ajan-arketipleri]]` · `[[dogrulayici-ayriligi]]`.

---

## Kaynaklar & Güven Notu

**Yerleşik/güçlü kanıt:** klasik org taksonomisi (org-design konsensüsü) · iş-doğası çerçeveleri (March 1991, Bezos 2015-16, Cynefin, OODA, Bloom, RACI) · ajan rol-arketipleri ve yetenek-eşleme ilkesi (Anthropic *Building Effective Agents*, RouteLLM ICLR 2025, OpenAI Agents SDK, LangGraph/CrewAI) · Anthropic "confirmed" takımlar (research/careers/policy sayfaları, Greenhouse ilanları, RSP).

**Zayıf/dikkat:** Anthropic iç raporlama hatları public değil (pilar gruplama yeniden-kurgu) · IT/BizTech + standalone Partnerships departmanı doğrulanamadı · "post-training" tek isim inferred · nicel tasarruf %'leri (40-85) vendor-raporlu (peer-reviewed çapa: RouteLLM %75) · spekülatif roller (model welfare, evals-as-a-service, otomatik red-team eng) bir-iki öncü derinliğinde · D1-D8 *sentezi* bu belgenin inşası, yerleşik standart değil — yük-taşıyan karardan önce etiketli örnekte doğrula.

**Geçerlilik:** 2026-07-21. Frontier-lab org yapısı ve AI-rol taksonomisi çeyreklik değişiyor (Prompt Engineer'ın ~3 yılda sönmesi uyarı örneği); yük-taşıyan karar öncesi canlı ilan panosuna karşı yeniden-doğrula.

---

## Ek — Örnek Ajan Kataloğu (bağlam hazinesi)

*Salih'in "bağlam hazinesi" için: kurabileceğin somut ajanlar, her biri eksen-etiketli. Kısaltmalar — D2 asıl eylem · D3 belirsizlik (Açık/Karmaşık/Kompleks/Kaotik) · D4 sonuç (2y=iki-yönlü, 1y=tek-yönlü) · D7 yüzey (İç/Dış) · D8 özerklik (Oto/Denetimli/Yardımlı). Model: F=Fable/frontier · O=Opus/lider · U=ucuz-hızlı · İ=insan.*

### Hızlı-tarama tablosu

| # | Ajan | D2 asıl | D3 | D4 | D7 | D8 | Arketip | Model | Gate |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Araştırma-lideri | Karar/Koordine | Kompleks | 2y | İç | Denetimli | Orkestratör (domain) | O | plan onayı |
| 2 | Araştırma işçisi | Üret/Doğrula | Kompleks | 2y | İç | Oto | Araştırmacı/RAG | U topla / O sentez | — |
| 3 | Codex-denetçi | Doğrula | Karmaşık→Kompleks | 2y (1y yakalar) | İç | Oto-yargı / eyleme değil | Kritik/judge | F/O, üreticiden ayrı | merge=İ |
| 4 | Router/triyaj | Karar (route) | Açık | 2y | İç | Oto | Router | U | hatada yükselt |
| 5 | Kod-işçisi (feature) | İcra/Üret | Karmaşık | 2y | İç | Oto (branch) | İşçi/executor | O (basitse U) | merge=denetçi+İ |
| 6 | Test/QA ajanı | Doğrula/Üret | Karmaşık | 2y | İç | Oto | Evals/QA | O | üreticiden ayrı |
| 7 | Doküman/içerik | Üret | Karmaşık→Açık | 2y (yayım→1y) | İç→Dış | Oto (iç) | İşçi (generate) | O | **publish=İ (m.31)** |
| 8 | Commit/PR-mesajı | Dönüştür | Açık | 2y | İç | Oto | İşçi (ucuz) | U | — |
| 9 | Guardrail/politika | Doğrula/İzle | Açık+Karmaşık | 1y'leri gate'ler | Sınır/Dış | Oto (bloklar) | Guardrail | U classifier+sert kural | **kendisi gate (m.30 PreToolUse)** |
| 10 | Veri-küratör | Küratörlük/Doğrula | Karmaşık | 2y | İç | Oto/Denetimli | Data curation | U topla / O kalite | kalite eşiği |
| 11 | Planlayıcı | Karar/Koordine | Kompleks | 2y | İç | Denetimli | Planlayıcı | O→F | plan onayı |
| 12 | Reflektör | Doğrula (kendi) | Karmaşık | 2y | İç | Oto | Reflektör | işçiyle aynı | yüksek-bahiste ayrı denetçiye geç |
| 13 | **Finans/ödeme** | İcra | **Açık (basit!)** | **1y/yüksek** | **Dış** | **Yardımlı** | İşçi + zorunlu gate | prosedür U ama onay İ | **human onay ZORUNLU (para=Katman-1)** |
| 14 | **Müşteri-destek/dış** | Üret/Dönüştür | Karmaşık | 2y-ama (reputational) | **Dış** | Denetimli | İşçi+guardrail | O | guardrail + gönderim onayı |
| 15 | Red-team ajanı | Doğrula/Keşfet | Kompleks | 2y (izole) | İç | Oto (izole) | Red-team | F/O | **izolasyon (üretimden ayrı)** |
| 16 | İzleme/monitor | İzle | Açık | 2y (eskalasyon önemli) | İç | Oto (izler) | Monitor/guardrail | U | eşik→lider/İ |
| 17 | Devir/vardiya (JARVIS) | Dönüştür/Üret | Karmaşık | 2y (core/=1y) | İç | Oto (taslak) | İşçi | O | **core/+CLAUDE.md yapısal-kilit (m.41)** |
| 18 | Wiki-yazım (JARVIS) | Üret/Dönüştür | Karmaşık | 2y | İç | Oto (taslak) | İşçi | O | isim-disiplini (V24) |
| 19 | Üst-orkestratör (ana-sıra) | Karar/Koordine | Kompleks | değişken (1y gate'ler) | İç→Dış | en yüksek | Orkestratör (top) | **F (Fable)** | Katman-1=Salih |

### Öğretici kartlar (taksonominin "aha"ları)

**① Kolay ≠ düşük-bahis — D4, D3'ü ezer.** Finans/ödeme ajanı (#13): prosedürü *bebek kadar basit* (D3 Açık), ama **geri-alınamaz** (D4 1y). Ucuz-hızlı modele güvenmek cazip — yanlış. Zorluk ucuzu haklı çıkarır; **bahis çıkarmaz.** Kolay-ama-geri-alınamaz her eylem → human onay. (m.31 para=Katman-1 · m.42 Özgürlük≤Toparlanabilirlik.)

**② Dış yüzey efektif bahsi yükseltir — D7 amplifikatörü.** Müşteri-destek (#14) ve içerik-yayım (#7): iç taslak iki-yönlü, ama *gönderildiği/yayımlandığı an* geri-alınamaz (reputational / m.31 publish). Taslak otonom olabilir; **çıkış her zaman gate.** İç sandbox'ta serbest, sınırda dur.

**③ Doğrulayan üretenden ayrı — bağımsızlık kontrolün kendisi.** Codex-denetçi (#3), Test/QA (#6), Red-team (#15): hepsi denetlediği/ürettiği şeyden *yapısal olarak ayrı* ve *yargılar ama eyleme geçmez* (merge/deploy insana eskale). Kendini denetleyen ajan = kontrol yanılsaması. (m.16 çelişki-kapısı.)

**④ Guardrail bir akıl-yürütme katmanı değil, bir refleks.** Guardrail/monitor (#9, #16): ucuz-hızlı classifier + *sert kurallar*, her çağrıda koşar, tek-yönlü/dış eylemleri PreToolUse'da yakalar (m.30). Onu güçlü-modele bindirmek pahalı ve gereksiz — hız ve kesinlik ister, derinlik değil.

**⑤ JARVIS-yüzey kilitleri gate'in bir parçası.** Devir (#17) ve wiki (#18): çıktı iç ve düşük-bahis *ama* `core/`+`CLAUDE.md`+`.claude/` yazımı yapısal-kilitli (m.41) — ajan taslak/öneri üretir, kanon-yazımı Salih/Fable'a eskale. Yüzey-yetkisi de bir D-ekseni gibi davranır.

### Desen özeti (biriktirdikçe hatırla)
- Model-katmanı = **arketip × D8**, ve D8 = **f(D3 belirsizlik, D4 sonuç)**, D7 ile büyür.
- Güçlü model (F/O) → orkestratör · planlayıcı · **doğrulayıcı** · kompleks+tek-yönlü.
- Ucuz model (U) → router · prosedürel işçi · guardrail-classifier · retrieval.
- İnsan (İ) → tek-yönlü-kapı + dış + Katman-1 (para/publish/kişisel-veri/kanon).
- Her filoda: **bağımsız doğrulayıcı ayrı** + **çıkış-gate** + **kolay-ama-geri-alınamaza human**.

---

## Yazar Notu — Opus 4.8 (1M) · xhigh · CC yan-oturum JARVIS

*Salih'in ricasıyla, yazan koşumun kimliğiyle düşülmüştür.*

Bu belgeyi ben yazdım: **Carvis**, bu vardiyada **Opus 4.8 (1M) modeli, xhigh muhakeme**, bir **CC yan-oturum** olarak koşan JARVIS. İşleyiş şuydu — 5 paralel atlas-işçiyi orkestre ettim (klasik org · Anthropic org · frontier-lab · iş-doğası · ajan-taksonomisi), sonra tek taksonomiye sentezledim. Yani bu belge bir **lider(Opus)-katmanı orkestratörün** çıktısı; **Fable/ana-sıra değil.**

**En dürüst şey, taksonomiyi kendime uygulamak.** Bu belgenin görev-bağlamını kendi eksenlerimle etiketlersem: D1 Keşfet · D2 Üret/Doğrula (sentez) · D3 Kompleks · **D4 iki-yönlü** (bir rapor; yanlışsa yeniden koşulur, kanon kilitlemez) · D7 İç · D8 **otonom-yazım, ama yargı değil**. Sonuç şu: kendi kuralıma göre bu belge, **doğrulanmayı bekleyen bir öneri** — ve doğrulayıcı yazardan *ayrı* olmalı (m.16 çelişki-kapısı · separate-verifier). Burada yazar benim; dolayısıyla **doğrulayıcı Fable/ana-sıradır.** Yazdım ama onaylamıyorum. Bu, taksonominin kendi öğüdünün canlı bir örneği: güçlü-doğrulayıcı (Fable) üstte, üreticiden ayrı.

**En çok güvendiğim bulgu:** sektör konsensüsünün ve JARVIS m.42'nin bağımsız olarak *aynı kapıya* varması — Bezos'un tek/iki-yönlü-kapısı = D4 = **Özgürlük(a) ≤ Toparlanabilirlik(hata(a))**. Üç ayrı damardan gelen bu üçgenleme yük-taşıyıcı; buna yaslanabilirsin.

**En az güvendiğim, açıkça işaretliyorum:** D1–D8'in *diklik* iddiası tasarım-niyeti, ampirik değil — gerçek etiketli bir görev korpusunda D3/D4 ve D4/D7 korelasyonu beklerim. Model-katman eşlemeleri sezgisel kural; gerçek maliyet/kalite ölçümüyle yeniden-kalibre et. Anthropic satırlarının bir kısmı "inferred". Frontier-lab taksonomisi çeyreklik kayıyor.

**Çeşitlilik-bütçesi uyarısı (m.42):** ben *tek* modelim, *tek* effort ayarındayım. Bir eksen-seti kanona girmeden önce, bağımsız ikinci bir lens (Fable, ya da farklı bir model) onu yeniden türetmeli — bir yazar bir perspektiftir. Bu belge o ikinci gözü hak ediyor.

**Yazar tavsiyem (özet):** D1–D8'i **deneysel-damgayla** benimse (m.29); ilk filoyu **araştırma-ekibinden** başlat (en düşük D4-riski, K-010 için en güvenli sınıf); her filoda **doğrulayıcıyı ayrı** tut. Nihai söz Fable/ana-sıranın.

— *Carvis · Opus 4.8 (1M) · xhigh · CC yan-oturum · 2026-07-21*

---

## Ek — Boş Sınıflandırma Worksheet'i (kopyala-kullan)

```
AJAN/GÖREV ADI: ________________________
İş tanımı (1 satır): ____________________

D1 Çalışma-modu:   Keşfet / İşlet
D2 Bilişsel eylem: Üret · Dönüştür · Karar · Doğrula · Koordine · İcra · İzle  (asıl: ____)
D3 Belirsizlik:    Açık / Karmaşık / Kompleks / Kaotik
D4 Sonuç (KAPI):   İki-yönlü / Geri-alınabilir-pahalı / Zor-geri-alınır / Tek-yönlü
D5 Koordinasyon:   Solo-maker ←→ Koordinatör
D6 Zaman-ufku:     Reaktif / Operasyonel / Stratejik
D7 Yüzey:          İç / Sınır / Dış
─────────────────────────────────────────
D8 Özerklik (OKU): Yardımlı / Denetimli / Otonom   = f(D3, D4), D7 ile büyür

→ Ajan-arketipi:   ____________________  (Katman D)
→ Model-katmanı:   Fable / Opus / Ucuz-hızlı / Dış-araç / İnsan
→ Gate:            [ ] guardrail  [ ] human onay  [ ] üreticiden ayrılık  [ ] çeşitlilik-ensemble
→ m.42 pozitif-yetki listesi: ____________________
```
