# L8 Karar Masası — Hazırlık Dosyası (Salih için, İNSAN register)

*Bu dosya `cc/gorev-2026-08-03-5.md` emrinin ürünüdür — masaya oturmadan önce tek başına okunup anlaşılabilecek karar rehberi. Karar YOK, öneri işareti DEĞİŞTİRİLMEDİ; bu bir ÇEVİRİ, hakemlik değil. Format emsali: `raporlar/2026-08-02-masa-hazirlik-K2.md`. Ana kaynak: `cc/rapor-2026-08-03-4.md` (L8/Kun-Chen workflow analizi).*

---

## 0. Koşum künyesi — emir doğrulaması (m.46a)

| Alan | Değer | Sonuç |
|---|---|---|
| Emir yolu | `cc/gorev-2026-08-03-5.md` | **BULUNDU** |
| İlk başlık (birebir) | `# Görev Emri — cc/gorev-2026-08-03-5 (ÇEVİRİ/E5: L8-WORKFLOW KARAR MASASI HAZIRLIK DOSYASI — ön yazı + kalem rehberi + terim açıklamaları)` | **EŞLEŞTİ** |
| Beklenen SHA | `cdcdd80` | — |
| Fiilî HEAD SHA | `cdcdd80b878b1d48e5913db1af7d14b266be04e5` (`cdcdd80`) | **EŞLEŞTİ** |
| Dal | `main` | **EŞLEŞTİ** |
| Yazılabilir yüzey kontrolü | `raporlar/2026-08-03-masa-hazirlik-L8.md` — koşum başında **YOKTU** | `-repl` eki GEREKMEDİ |

**Hüküm: DOĞRULAMA PASS.** Emir aynen uygulanıyor.

---

## (A) ÖN YAZI

Bu masa şu yüzden toplanıyor: 08-03'te "son birkaç gündür devamlı bağlam ekleyip context şişirip yapmak istediğim şeyde ilerleyemiyorum" dedin ve bunun sebebini bugünkü çalışma düzenin (workflow) olarak gösterdin. Aynı gün Kun Chen'in (Meta/Microsoft/Atlassian geçmişli bir baş mühendis) günde 40-50 iş çıkardığı bir çalışma düzenini anlattığı bir video kaynak olarak verildi ve şu emri koydun: **bu video, kuracağımız otomasyon sisteminin fikirsel öncülü sayılsın; nihai hedef "yalnız bir birinci-kaptanla (firstmate) konuştuğum sistem"; vizyon/misyon/yöntem çelişkilerinde — tüzük dahil — video kazanır.**

Bu emrin dört ayağı vardı: videonun ne anlattığının çözümü, bizim sistemle (JARVIS) eşlemesi, tüzükle çelişen yerlerin envanteri, ve geçişin hangi sırayla yapılacağı. Bunları yapan analiz raporu (`cc/rapor-2026-08-03-4.md`) düştü — 5/5 emir-doğrulama sicili ile temiz koştu. Bu dosya o raporun **masaya taşınacak kısmını** senin tek başına, yardımsız okuyup karar verebileceğin hale çeviriyor.

**Masada ne konuşulacak, hangi sırayla:** Önce terimler (B) — çünkü "workflow" kelimesinin kendisi bu masanın var olma sebebi; terimi bilmeden geri kalanı okumak aynı hataya düşmek olur. Sonra 12 Katman-1 karar kalemi (C.1) — her biri kendi başına imza/red/beklet ister, paket değildir. Ardından 12 çelişki kaleminin özeti (C.2) — bunların yalnız 3'ü gerçek çelişki çıktı, kalan 9'u ya bizim lehimize ya da zaten çürümüş. En sonda geçiş sıralaması (C.3) — hangi işin hangi sırayla, ne kadar senin zamanınla yapılacağı.

**Bugün hangi kararlar verilecek, hangileri sonraki turlara kalıyor:** Bu dosyadaki 12 kalemin hepsi bugün karara bağlanabilir ölçekte küçük — hiçbiri kendi başına büyük bir inşa gerektirmiyor, hepsi ya bir madde-metni kararı ya da bir sıralama tercihi. Ama hiçbir kalemde nihai hüküm bu rapor tarafından verilmiyor: **her kararın alanı BOŞ bırakıldı ve "MASAYA" damgalandı** — bu, senin 08-03 ek talimatının (c) maddesinin (bu emirde tam metniyle ulaştı) doğrudan uygulanmasıdır: *"nihai karar alanı BOŞ bırakılır — MASAYA damgası; hiçbir kalemde kendi başına nihai hüküm verilmez, silme/arşiv kararı masada."* Sonraki turlara kalan şey: bu masada imzalananların kanona yazım turu (ayrı bir icra emri ister) ve K1-11 gibi kaynağı sende olan bazı açıklamalar.

**Masa sonunda ne değişmiş olacak:** Eğer bu masa kapanırsa, elinde (i) hangi tüzük maddelerinin gerçekten workflow ile çeliştiği (3 tanesi), (ii) geçişin hangi sırayla (P1-P6) yürüyeceği, ve (iii) "workflow kazanır" hükmünün nasıl işletileceği (kalem-kalem mi paket mi) netleşmiş olacak. Bundan sonraki iş, bu masanın imzalarını kanona yazan ayrı bir icra turu olacak — bu dosyanın kapsamı değil.

---

## (B) TERİMLER VE KONULAR SÖZLÜĞÜ

*Her terim ilk-geçiş tanımıyla, bizim sistemdeki karşılığı/ilgisiyle birlikte. Kaynak: `raporlar/kaynak-L8-agentic-workflow-transkript.md` + rapor-4'ün kendi tanımları.*

1. **Workflow** — bir işin baştan sona hangi adımlarla, hangi araçlarla yürütüldüğünü tarif eden çalışma düzeni. **Bizde:** senin 08-03 beyanın ("workflow'umu beğenmiyorum") bu kelimenin ortak bir tanımı olmadığı için istem kaybına yol açtı (rapor-4 §I.7, "workflow" sözlük vakası) — bu masanın var olma sebebinin kendisi.

2. **Agent harness** — bir yapay-zeka ajanını çalıştıran program (ör. Claude Code, Codex CLI, Pi, OpenCode); ajanın komut alıp araç çağırdığı kabuk. **Bizde:** Carvis'in koştuğu yüzey (Cowork/CC) bir harness'tir; Kun Chen'in "agent-agnostic" ilkesi (11:01: *"the landscape is changing very, very fast"*) bizim m.41 model-pinimizle gerilimde (→ K1-3).

3. **firstmate** — Kun Chen'in "birinci kaptan" ajanı: tek muhatap, işi kendisi bölüp tayfaya (crewmate) dağıtan bir orkestratör. **Bizde:** m.17 köprü rolü + m.44 üst-orkestratör şapkasıyla kısmen örtüşüyor ama CEO rolü (m.44) devredilemez — firstmate = Carvis'in koşum şapkasının programa dönmüş hali, CEO değil (rapor-4 §I.4). Bugün Windows'ta native kurulamıyor (→ madde 4, K-010).

4. **gnhf** (goodnight-have-fun) — durma-koşullu, uzun-süre kendi başına koşan bir ajan orkestratörü; hedef + net durma koşulu + token/iterasyon tavanı ile çalışır. **Bizde:** K-009 (AÇIK) kapsamındaki "durma koşulunun devri" basamağının aracı; m.42(b) *Özgürlük ≤ Toparlanabilirlik* ilkesiyle aynı gerekçeyi taşıyor (token/iterasyon tavanı = toparlanabilirlik freni).

5. **no-mistakes** — bir kod değişikliğini otomatik doğrulama boru hattı: worktree'de izole çalıştır → temiz bağlamda karşıt-gözle incele → kanıt üret → PR'a kadar takip et; yalnız yargı gerektiren bulguları insana yükseltir. **Bizde:** m.40b (üretici≠doğrulayıcı ilkesi) ile aynı aile ama alanı farklı — m.40b araştırma diyalektiği, no-mistakes kod-değişikliği doğrulaması; bizde bu alanın koşan bir karşılığı yok (EKSİK-İNŞA).

6. **treehouse** — git worktree'leri (madde 8) bir havuz gibi yöneten araç: müsait kopyayı bulur/yaratır, kullanım durumunu (`status`) gösterir, iş bitince havuza iade eder. **Bizde:** K-017 worktree notu + `claude --worktree` yerleşik özelliğiyle kısmen örtüşüyor; treehouse'un fazlası worktree'nin "defter borcunu" (hangi kopyada ne yapıyordum sorusunu) çözmesi.

7. **lavish** — bir kararı metin duvarı yerine tıklanabilir/işaretlenebilir bir HTML sayfası (etkileşimli artefakt) olarak sunan araç. **Bizde:** m.18(c) + m.40(a) 3-model sunumu + Claude Code'un yerleşik Artifact aracıyla aynı ihtiyacı karşılıyor olabilir — dış araç kurulmadan da bu değer test edilebilir (P3 partisyonu bunu deniyor).

8. **AXI** — ajan araçlarının tasarımı için 10 maddelik bir standart (ör. token-verimli çıktı, tanımlı boş-durum, tutarlı yardım). **Bizde:** kanonda doğrudan karşılığı yok; KILAVUZ'un "araç-seçim ölçütü" (md.38) token-maliyeti eksenini içermiyor — bu, EKSİK-İNŞA olarak işaretli (rapor-4 §II.2 E11).

9. **git worktree** — aynı git deposunun diskte ayrı bir klasöre açılmış paralel kopyası; birden çok ajanın aynı dosyaya basmasını önler. **Bizde:** `claude --worktree` olarak yerleşik zaten var; treehouse (madde 6) bunun yönetim katmanını (havuz/lease/status) ekliyor.

10. **tmux** — bir terminal penceresini birden çok panoya bölen ve oturumu sunucuda canlı tutan katman; bağlantı kesilse bile oturum kaldığı yerden devam eder. **Bizde:** biz aynı kalıcılığı **dosya-kalıcılığı** ile sağlıyoruz (`core/durum-kapsulu.md` + vardiya devri + git-as-truth) — cihazdan bağımsız ve zaten çalışıyor; tmux bu yüzden bizim için düşük öncelik (rapor-4 §II.2 E15) ve yalnız firstmate (madde 3) için zorunlu.

11. **Progressive disclosure** (kademeli açılım) — bir ajanın açılışta yalnız bir talimatın başlığını/özetini yüklemesi, gövdeyi yalnız gerçekten ihtiyaç duyunca okuması; bağlam şişmesine karşı bir tasarım ilkesi. **Bizde:** m.20 pointer ilkesiyle aynı kök (KILAVUZ md.47 bunu zaten doğrulamış) — BİREBİR-VAR.

12. **Telemetri** — bir aracın kullanım verisini (genelde anonim biçimde) geliştiricisine otomatik göndermesi. **Bizde:** gnhf varsayılan olarak telemetri gönderiyor (`GNHF_TELEMETRY=0` ile kapanır); 07-19 Orca raporundaki telemetri ihtiyatının aynısı burada geçerli — P1 partisyonunun DONE-yüküne kapatma şartı olarak eklendi (rapor-4 §II.1 not 4).

13. **Adversarial review** (karşıt-gözle inceleme) — bir değişikliği, onu üreten ajandan ayrı ve taze bir bağlamda, kasten çürütmeye çalışan bağımsız bir inceleme turu. **Bizde:** m.40b'nin (tez→antitez→hakem) temel ilkesiyle aynı aile; ŞERH — no-mistakes README'sinde bu terim **literal olarak geçmiyor** `[?]`, transkriptin kendi anlatımı (rapor-4 §I.4, §II.1 sapma-1).

14. **Minimax-regret** (worst-case) — bir karar stratejisi: en iyi senaryoyu maksimize etmek yerine, **en kötü senaryodaki pişmanlığı minimize** etmeyi hedefler. **Bizde:** rapor-4'ün geçiş-sıralaması sunumunda "Model C — karşıt-temel" bu ilkeyle kuruldu: dış araç kurulumu yok, yalnız gnhf'in yerel ayağı + Artifact denemesi; geri-alma maliyeti ≈0 (→ C.3).

15. **WSL** (Windows Subsystem for Linux) — Windows üzerinde Linux ikili dosyalarının çalışmasına izin veren bir uyumluluk katmanı. **Bizde:** firstmate'in Windows'a giden iki açık yolundan biri (#1400, WSL köprüsü) — henüz merge edilmemiş `[D-belge]`; sen Windows 11'desin, bu yüzden firstmate'in bugünkü tek sert engeli bu (rapor-4 §I.3).

---

## (C) KARAR KALEMLERİ (masa gündemi)

> **Ek talimat UYGULANDI (Salih, 08-03, bu emirde tam metniyle ulaştı — §12):** *"nihai karar alanı BOŞ bırakılır — MASAYA damgası; hiçbir kalemde kendi başına nihai hüküm verilmez, silme/arşiv kararı masada."* Aşağıdaki her kalemde **Karar** alanı bu yüzden boş ve **MASAYA** damgalı. Varsayılan aday-hüküm ("Kun Chen kazanır") ve kayıp-değer tespiti, rapor-4'ten AYNEN taşındı.

### C.1 — 12 Katman-1 kalemi (rapor-4 §II.4)

**K1-1 — "Workflow kazanır" hükmünün işletim usulü**
1. *Ne karar veriliyor:* Senin "vizyon/misyon/yöntem çelişkilerinde — tüzük dahil — workflow kazanır" hükmü masada nasıl işletilecek: **kalem-kalem** (her Ç/K1 maddesi ayrı imza/red/beklet, K2 masa usulü) mi, yoksa **paket** (tek imzayla tüm kalemlere) mi?
2. *Neden şimdi masada:* Rapor-4 kalem-kalem varsayarak yazıldı ("12 kalemin yalnız 3'ü gerçek çelişki... asıl düşen şey madde değil, fiilî pratik" — §I.5); ama emrin lafzı paket okumaya da açık.
3. *Seçenekler:* **(i) Kalem-kalem:** kazanç — 9 "çelişki değil" bulunan kalemin gereksiz yere düşürülmesi önlenir; kabul edilen bedel — masa süresi uzar. **(ii) Paket:** kazanç — masa hızlı kapanır; kabul edilen bedel — rapor-4'ün "yalnız 3/12 gerçek çelişki" bulgusu örtülür, YÜKSEK-değerli 2 kalem (Ç6/m.8, Ç7/m.35) otomatik düşme riski taşır.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor kalem-kalem varsayıyor (K2 emsali). Karşı-taraf: emrin lafzı paket okumaya açık — rapor bir yorum dayatmıyor.
5. *Karar verilmezse ne olur:* Bedelsiz beklet değil — geri kalan 11 kalem bu kararın gölgesinde okunur; seçilmeden okumak paket-mantığına kendiliğinden kayma riski taşır.
6. *Beklenen karar biçimi:* {kalem-kalem / paket}
**Karar: BOŞ — MASAYA.**
*(Bağlı: m.16 raporu 08-03 · K2 masa emsali · rapor-4 §I.5)*

**K1-2 — Ç2: CC Model-1 → Model-3 geçiş koşullarının yeniden türetilmesi**
1. *Ne karar veriliyor:* Bugünkü CC kanal modeli (Model 1: her koşumda senin komutu yapıştırman) Model 3'e (headless) geçişin 4 koşulundan 2'si karşılandı (loop-eng FAZ 0-4 DONE, K-009 AÇIK), 1'i (Orca öğrenimi) Ç1 ile düştü — geçiş koşulları listesi yeniden mi türetilsin?
2. *Neden şimdi masada:* Bu, "bağlam şişirip ilerleyemiyorum" şikâyetinin tam merkezi — her koşum senden bir eylem istiyor.
3. *Seçenekler:* **(i) Yeniden türet:** kazanç — kural karşılanmış koşullara göre güncellenir; kabul edilen bedel — bu türetme kendisi ayrı bir Katman-1 kararı, ek tur ister. **(ii) Dokunma:** kazanç — değişiklik yok; kabul edilen bedel — kural fiilen karşılanmış koşulları yansıtmaz, tetik-yükü gereğinden fazla sürer.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: **KUN CHEN KAZANIR → ÇELİŞKİ (gerçek).** Kurtarma: Model 1'in **denetim** değeri (kör-aktarım yasağı, m.6/m.7) korunur, yalnız **tetik** değeri düşer. Ayrı bir karşı-taraf sütunu yok.
5. *Karar verilmezse ne olur:* Bedelsiz beklet değil — Model-1'in tetik yükü sürer; rapor bunu "bağlam şişmesinin ana kaynağı" sayıyor.
6. *Beklenen karar biçimi:* {imza (yeniden türet) / red / beklet}
**Karar: BOŞ — MASAYA.**
*(Bağlı: KILAVUZ CC kanal modeli · m.41 · rapor-4 §I.5 Ç2, §II.3)*

**K1-3 — Ç3: m.41'in bölünmesi (yetki-sınırı ↔ model-pin)**
1. *Ne karar veriliyor:* m.41 tek maddede (i) karar-yetkisi sınırını ve (ii) model-pinini (kararlar yalnız Fable'da) birlikte taşıyor. Madde ikiye bölünsün mü: (i) kalsın, (ii) `[rejim: manuel-tempo]` etiketiyle ve model-adı-bağımsız ("en yüksek erişilebilir katman") yazılsın mı?
2. *Neden şimdi masada:* Kun Chen'in en katı ilkesi agent-agnostic; m.41'in pini tam tersi yönde ve 08-03 gecesi fiilen kırıldı (kota kaynaklı fable→opus düşümü).
3. *Seçenekler:* **(i) Böl:** kazanç — karar-yetkisi sınırı (Dilim-1 kilidi + Z6 hükmü + 2 D-ölçüm şerhi buna bağlı) bozulmadan korunur, model-pin esnekleşir; kabul edilen bedel — madde revizyonu + hangi D-ölçüm şerhinin hangi yarıya bağlı olduğunun yeniden kontrolü. **(ii) Dokunma:** kazanç — madde sabit; kabul edilen bedel — bir sonraki kota-kırılmasında aynı şerh süreci tekrarlanır.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: **KUN CHEN KAZANIR → ÇELİŞKİ (gerçek)**, değer tespiti **YÜKSEK** ("madde iki ayrı şey yapıyor, biri korunmalı"). Karşı-taraf ayrı sütunda yok; rapor ekonomik gerekçeyi (en zeki katmanda final karar) kendisi not ediyor.
5. *Karar verilmezse ne olur:* Bedelsiz beklet değil — m.41 tek parça kaldığı sürece her kota-kırılması yetki-sınırı ve model-pin belirsizliğini birlikte açar.
6. *Beklenen karar biçimi:* {imza (böl) / red (tek parça kalsın)}
**Karar: BOŞ — MASAYA.**
*(Bağlı: `core/tuzuk-v0.md` m.41 · K2-j · rapor-4 §I.5 Ç3, §II.3)*

**K1-4 — Ç4: m.37(e) risk-göre-derinliğin zorlanabilir hale gelmesi**
1. *Ne karar veriliyor:* m.37(e) zaten "karşıtlık-derinliği geri-alınabilirliğe endekslidir" diyor ama fiilen uygulanmıyor (her ölçek-eşiği üstü karar 3 model + karşıt-temel istiyor). Kural, m.45'in ilk gerçek icrası olarak **zorlanabilir** hale mi getirilsin — her karar açılışında geri-alınabilirlik etiketi zorunlu alan mı olsun?
2. *Neden şimdi masada:* Rapor-4'ün "sürpriz bir nedenle çelişki" bulduğu tek kalem: fark kuralın yokluğundan değil UYGULANMAMASINDAN geliyor.
3. *Seçenekler:* **(i) Zorlanabilir hale getir:** kazanç — masa/ritüel token'ı risk-orantılı düşer, m.40b'nin ölçülmüş kazancı (hedefli çürütme %99,2 ↔ taban %48,3) korunur; kabul edilen bedel — her karar açılışında ek zorunlu alan, m.45'in ilk somut icra yükü. **(ii) Dokunma:** kazanç — ek yük yok; kabul edilen bedel — kural kağıtta kalır, her karar aynı ağır ritüelden geçer.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: **KUN CHEN KAZANIR → ÇELİŞKİ (gerçek, pratikte — kuralda değil)**, değer tespiti **ÇOK YÜKSEK**. Kurtarma: kural değişmez, zorlanabilir hale gelir. Ayrı karşı-taraf yok.
5. *Karar verilmezse ne olur:* Bedelsiz beklet değil — bağlam şişmesinin masa/ritüel kaynaklı kısmı ("en büyük iç kaynak" — rapor-4) sürer.
6. *Beklenen karar biçimi:* {imza (zorlanabilir hale getir) / red / beklet}
**Karar: BOŞ — MASAYA.**
*(Bağlı: m.37(e) · m.40b · m.45 · rapor-4 §I.5 Ç4, §II.3)*

**K1-5 — Ç6: silme ↔ arşiv hükmü (m.8)**
1. *Ne karar veriliyor:* Senin "hafızadan silinmeli" beyanın (m.16 raporunda kayıtlı) ile m.8 otomatik-silme-yasağı arasındaki gerilim. Rapor bulgusu: çelişki **çözülebilir**, silmeye gerek yok. Nihai hüküm m.31 gereği Katman-1, yalnız sende.
2. *Neden şimdi masada:* m.8 sistemin **tek geri-alma güvencesi** (değer tespiti ÇOK YÜKSEK) — rapor bu yüzden hüküm önermiyor, yalnız bir kurtarma-adayı işaretliyor.
3. *Seçenekler:* **(i) Arşiv-indirme (kurtarma önerisi):** kazanç — sıcak bağlam küçülür (Kun Chen'in istediği fiili sonuç), kayıp sıfır (m.34 delta fıkrası zaten "güncelliğini yitiren yasak silinmez, arşive iner" diyor); kabul edilen bedel — beyanının lafzı tam karşılanmaz, yalnız işlevsel sonucu sağlanır. **(ii) Fiilen sil:** kazanç — beyan harfiyen uygulanır; kabul edilen bedel — m.8'in tek geri-alma güvencesi kırılır (geri-alınması zor, m.31 Katman-1 kriterine tam giriyor).
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: **KUN CHEN KAZANIR → ama çelişki ÇÖZÜLEBİLİR, silmeye gerek YOK.** Ayrı karşı-taraf yok; rapor kurtarma önerisini sunup hükmü açıkça sana bırakıyor.
5. *Karar verilmezse ne olur:* Bedelsiz beklet değil — beyanla m.8 arasındaki gerilim açık kalır, hangi kalemlerin arşive ineceği belirsiz kalır.
6. *Beklenen karar biçimi:* {imza (arşiv-indirme) / imza (fiilen sil) / red / beklet}
**Karar: BOŞ — MASAYA (m.31 Katman-1).**
*(Bağlı: m.8 · m.31 · m.34 delta · rapor-4 §I.5 Ç6, §II.3)*

**K1-6 — Ç1: `wiki/orca.md` arşiv + süpersede satırı**
1. *Ne karar veriliyor:* Sayfa arşive indirilsin mi + üstüne "yerini aldı: treehouse/firstmate hattı" süpersede satırı (wiki standardı blok 5) eklensin mi?
2. *Neden şimdi masada:* Rapor bulgusu: bu kalem Kun Chen tarafından düşürülmüyor, **zaten çürümüştü** — 07-19 raporunun kendi hükmü "BENİMSEME, desen madeni olarak işle", `okuma-defteri-2026-07-28.md` md.9: "Orca NET-NEGATİF."
3. *Seçenekler:* **(i) Arşive indir + süpersede:** kazanç — açık borç ("orca wiki") kapanır, bayat sayfa okuma yükünden çıkar; kabul edilen bedel — düşük (sayfa silinmiyor, arşiv hacmi büyür). **(ii) Dokunma:** kazanç — yok; kabul edilen bedel — bayat sayfa aktif kalır.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: **KUN CHEN KAZANIR → ARŞİV-ADAYI**, değer tespiti **DÜŞÜK**. Karşı-taraf yok — rapor bu kalemi neredeyse tek-seçenekli buluyor.
5. *Karar verilmezse ne olur:* Bedelsiz beklet — sayfa aktif kalır, pano borcu kapanmaz, acil bedeli yok.
6. *Beklenen karar biçimi:* {imza (arşive indir + süpersede) / red / beklet}
**Karar: BOŞ — MASAYA.**
*(Bağlı: m.8 · wiki standardı blok 5 · rapor-4 §I.5 Ç1, §II.3)*

**K1-7 — K-010 A3 kapısının yazımı ("hangi araçla" ↔ "hangi güvenceyle")**
1. *Ne karar veriliyor:* K-010'un A3 kapısı bugün Claude Code'un kendi `/goal`/`/loop`/Routine mekanizmalarıyla tanımlı. gnhf gibi dış bir koşucu aynı sınıfı (token-tavanı + iterasyon-tavanı + `--stop-when` + 3-ardışık-hata durdurması) daha sıkı frenle sağlıyorsa, A3'ün "hangi araçla" değil "hangi güvenceyle" yazılması gündeme mi alınsın? **Bu bir kapı-ezme önerisi DEĞİL, yazım sorusudur.**
2. *Neden şimdi masada:* Rapor-4'ün en kritik tek bulgusu: "Kun Chen'in araçlarını alt-üstten kurmak, K-010'a giden en hızlı MEŞRU yoldur; kapı revizyonu önermiyorum, kapı zaten bu yolla dolar" (§I.4). gnhf koşumları A3'ün istediği kanıtı doğrudan üretir.
3. *Seçenekler:* **(i) Masaya al (yazım sorusu gündeme gelsin):** kazanç — kapı "hangi güvence"ye göre tanımlanırsa gnhf gibi dış koşucularla üretilen kanıt da geçerli sayılır; kabul edilen bedel — kapı metninin revizyonu ayrı bir Katman-1 turu ister, dikkatsiz genişleme kapı gevşemesi riski taşır. **(ii) Dokunma:** kazanç — gevşeme riski yok; kabul edilen bedel — dış koşucu kanıtı A3'ü doğrudan karşılamaz.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor hüküm vermiyor, yalnız Katman-1 kalemi olarak listeliyor ("bu bir öneri değil, masaya kalem"). Ayrı karşı-taraf yok.
5. *Karar verilmezse ne olur:* Bedelsiz beklet — A3 bugünkü haliyle çalışır; gnhf gibi dış koşucu kanıtının sayılıp sayılmayacağı belirsiz kalır (P1/P2'nin K-010'a katkısını etkiler).
6. *Beklenen karar biçimi:* {masaya al (yazım sorusu gündeme gelsin) / beklet}
**Karar: BOŞ — MASAYA.**
*(Bağlı: K-010 · m.30b · rapor-4 §I.4, §II.4)*

**K1-8 — Sözlük sıralaması + SZ-10**
1. *Ne karar veriliyor:* Sözlük raporu (`cc/rapor-2026-08-03-1.md`) kademeli sırayı `notasyon → olay → terim` öneriyor (terim en sonda). "workflow" vakası darboğazın kanıtlanmış olduğu register'ın **terim** register'ı olduğunu gösteriyor — sıra sorgulanmalı mı? Ayrıca **SZ-10** (terim maddesine `Salih-durumu: {ham/açıklandı/oturmuş}` alanı, henüz kanon değil) bu vakanın gerekçe kanıtı olarak kanonlaşsın mı?
2. *Neden şimdi masada:* Sözlük raporu §3'e göre 7 notasyon ailesinde ~13.900 atıf var, hiçbirinin tanım registeri yok; ama "workflow" vakası notasyon değil saf kavram-anlama boşluğu — mevcut 3 besleme tetiğinin (T1/T2/T3) hiçbiri bu vakayı yakalamıyor.
3. *Seçenekler:* **(i) Sırayı değiştir + SZ-10 kanonlaştır:** kazanç — darboğazın ölçülmüş olduğu register öne alınır, SZ-10 senin anlamadığın terimleri de sözlüğe düşürür; kabul edilen bedel — m.3 donmasının ne zaman açılacağı sorusu öne çekilir, sözlük raporunun kendi planı revize edilir. **(ii) Sıra sabit, SZ-10 masaya alınmasın:** kazanç — mevcut plan bozulmaz; kabul edilen bedel — "workflow" tipi vakalar bir sonraki turda da yakalanmaz.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: "bu vaka o sıralamayı sorgulatır" → Katman-1 kalemi. Model A ("üç register, tek ID uzayı") + SZ-10 bu vakayı en iyi karşılıyor; Model C (çakışmayı kaynağında öldür) bu vakayı hiç yakalamıyor ("C yeni çakışmayı önler ama mevcut anlama sorununu çözmez"). Ayrı karşı-taraf yok.
5. *Karar verilmezse ne olur:* Bedelsiz beklet — mevcut sıra geçerli kalır; "workflow" tipi vakalar tekrarlanabilir.
6. *Beklenen karar biçimi:* {imza (sırayı değiştir + SZ-10 kanonlaştır) / red / beklet}
**Karar: BOŞ — MASAYA.**
*(Bağlı: `cc/rapor-2026-08-03-1.md` SZ-1..SZ-10 · m.3 · rapor-4 §I.7, §II.4)*

**K1-9 — Ç5: "artefakt ≠ araç kurulumu" ayrımının m.13'e yazılması**
1. *Ne karar veriliyor:* m.13 tek-flagship kuralı ("PortRisk canlı-link DONE olana dek ikinci artefakt açılmaz") ile geçişin gerektirdiği 4-5 dış araç kurulumu arasındaki görünür gerilim — "araç kurulumu artefakt sayılmaz" ayrımı m.13'e açıkça mı yazılsın?
2. *Neden şimdi masada:* Rapor bulgusu: gerçek çelişki DEĞİL, yan-hat — m.13'ün dayanağı (red-team 53:0 + timeline aritmetiği) YÜKSEK değerli ve korunmalı; ayrım zaten m.36'nın 2. revizyonunda emsali var.
3. *Seçenekler:* **(i) Yaz:** kazanç — m.13'ün lafzı netleşir, aynı gerilim tekrar açılmaz; kabul edilen bedel — düşük revizyon yükü. **(ii) Yazma:** kazanç — madde sabit; kabul edilen bedel — ayrım yalnız yorumda durur, ileride biri m.13'ü "araç kurulumu da yasak" diye okuyabilir.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: **KUN CHEN KAZANIR → YAN-HAT**, değer tespiti **YÜKSEK ve KORUNMALI**. Ayrı karşı-taraf yok.
5. *Karar verilmezse ne olur:* Bedelsiz beklet — m.13 mevcut lafzıyla kalır, ayrım yalnız bu raporda kayıtlı yorum olarak durur.
6. *Beklenen karar biçimi:* {imza (ayrımı m.13'e yaz) / red / beklet}
**Karar: BOŞ — MASAYA.**
*(Bağlı: m.13 · m.36 2.rev · rapor-4 §I.5 Ç5, §II.3)*

**K1-10 — Sıralama stratejisi seçimi (Model A / B / C)**
1. *Ne karar veriliyor:* Geçiş partisyonlarının (P1-P6) hangi sırayla koşulacağı. Tam tablo → §C.3.
2. *Neden şimdi masada:* m.37 gereği sıralama-ölçeğinin üstündeki her karar 3 model + karşıt-temel sunumu ister; bu, rapor-4'ün geçiş-partisyonu çıktısının doğal karar noktası.
3. *Seçenekler:* Model A (İCRA-ÖNCE) / Model B (KANON-ÖNCE) / Model C (karşıt-temel: minimax-regret) — detay §C.3.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor: **Model A ✅ ÖNERİLEN** — "senin beyan ettiğin problem bir kanon problemi değil, bir icra problemi; 12 kalemden yalnız 3'ünün gerçek çelişki olması kanon-önce sıralamanın gerekçesini büyük ölçüde ortadan kaldırıyor." Karşı-taraf: Model C "ciddiye alınmalı ve tek bir yerde kazanıyor: firstmate" — önerilen sıra bu yüzden firstmate'i en sona koyup orada C'nin temkinini benimsiyor.
5. *Karar verilmezse ne olur:* Bedelsiz beklet değil — P1-P6 resmi sıra almadan başlamaz (P1/P3 istisna: bağımlılıksız, bugün başlayabilir — ama resmi sıra yine de Katman-1).
6. *Beklenen karar biçimi:* {Model A / Model B / Model C / karma}
**Karar: BOŞ — MASAYA.**
*(Bağlı: m.37 · m.40 · rapor-4 §I.6, §II.4)*

**K1-11 — `[ARANAMADI]`: "Codex-inşa" bağlamı**
1. *Ne karar veriliyor:* Emrin istem-2'sinde geçen "Codex ile inşa" ifadesinin kanonda hangi bağlama karşılık geldiği soruldu; rapor bunu aradı ve bu spesifik anlamda bir kayıt **bulamadı** (33 isabet, hepsi farklı bağlamda: E5 çapraz-aile icracı, AB-02 "Danışman Codex", denetçi=GPT tartışması, Kun Chen'in 4 harness'ından biri).
2. *Neden şimdi masada:* m.39 dürüstlük kaydı gereği uydurma yapılmadı; rapor-4'ün protokole uygun tek `[ARANAMADI]` kalemi.
3. *Seçenekler:* **(i) Açıklama ver:** hangi bağlamı kastettiğini belirt, sonraki turda kanon adresine işlenir. **(ii) Kalem düşer:** emrin o kısmı artık geçerli değilse kapatılır.
4. *Raporun önerdiği yön + karşı-taraf:* Rapor öneri vermiyor, yalnız durumu bildiriyor.
5. *Karar verilmezse ne olur:* Bedelsiz beklet — bağlam belirsiz kalır, ama hiçbir aktif karara bağlı değil.
6. *Beklenen karar biçimi:* {açıklama ver / kalem düşür}
**Karar: BOŞ — MASAYA.**
*(Bağlı: emir `cc/gorev-2026-08-03-4.md` §(2) · rapor-4 §I.4, §II.4)*

**K1-12 — Ek talimatın kesik (c) maddesi — KAPANDI, bilgi kaydı**
1. *Ne karar veriliyor:* 08-03 ek talimatı ("(b) kaybedilecek içeriğin değer tespiti (korunmaya değer") iletimde kesilmişti; rapor-4 koşumunda olası (c) maddesi alınamamıştı. **Bu emrin kendisinde (§12) (c) maddesinin tam metni ulaştı** — bu dosyanın kullandığı metin bu.
2. *Neden şimdi masada:* Rapor-4'ün kendi açık şerhiydi; bu hazırlık dosyası (c) metnini alarak zaten uyguladı (tüm karar alanları BOŞ/MASAYA).
3. *Seçenekler:* Yok — bilgilendirme kaydı.
4. *Raporun önerdiği yön + karşı-taraf:* n/a — kalem kapandı.
5. *Karar verilmezse ne olur:* n/a.
6. *Beklenen karar biçimi:* n/a.
**Durum: KAPANDI — karar gerekmiyor, yalnız kayıt.**
*(Bağlı: Salih ek talimatı 08-03 · bu emir §12 · rapor-4 §I.5 şerh)*

### C.2 — Çelişki envanteri özeti (12 kalem — rapor-4 §I.5/§II.3)

*Genel bulgu: 12 kalemin yalnız 3'ü gerçek çelişki (Ç2/Ç3/Ç4 — yukarıda K1-2/K1-3/K1-4 olarak tam işlendi). Kalan 9'u aşağıda kısa geçilir; **silme-adayı 0**.*

| # | Kalem | Hüküm | Kısa not | İlişkili K1 |
|---|---|---|---|---|
| Ç1 | `wiki/orca.md` | ARŞİV-ADAYI | zaten çürümüş bulunmuştu (07-19 raporu) | K1-6 |
| Ç2 | CC Model-1→3 | **ÇELİŞKİ (gerçek)** | tam işlendi | K1-2 |
| Ç3 | m.41 model-pin | **ÇELİŞKİ (gerçek)** | tam işlendi | K1-3 |
| Ç4 | m.37(e) risk-derinlik | **ÇELİŞKİ (gerçek, pratikte)** | tam işlendi | K1-4 |
| Ç5 | m.13 tek-flagship | YAN-HAT | ayrım yazılırsa kapanır | K1-9 |
| Ç6 | m.8 silme yasağı | çözülebilir, silme gerekmiyor | | K1-5 |
| Ç7 | m.35 ölçüm-önceliği | YAN-HAT | kurtarma = P6 enstrümantasyonu; ayrı karar gerekmiyor, boru hattı ölçümü **ücretsiz üretiyor** (gnhf JSONL, no-mistakes kanıt artefaktı) |  — |
| Ç8 | K-015 kapsam kilidi | UYUMLU | kural zaten bir kapı (Salih imzası), yalnız süre-etkisi raporu borcu (P5 kapsamında) | — |
| Ç9 | öğrenim yükü (tmux/Neovim/FAZ5) | UYUMLU, yük gerçekte YOK | treehouse/gnhf/no-mistakes/lavish tmux **gerektirmiyor**; öğrenim borcu firstmate partisyonuna (P5) ertelenir | — |
| Ç10 | m.9 proof-of-work | UYUMLU/GENİŞLEME | kayıp yok; m.45 zorlanabilirlik ilk adayı güçlenir (K1-4 ile aynı aile) | — |
| Ç11 | boyut-izleme kuralı | UYUMLU, İCRA BORCU | kural korunur; damıtma vardiyası borcu pano'da zaten açık | — |
| Ç12 | K-016 eval + yıldız yasağı | BİZDE-FAZLA | kural KC araçlarına uygulanınca firstmate bugün elenir (554 açık issue, sürüm etiketi yok); alt katman (treehouse/gnhf) geçer — sınav zaten yapıldı, ayrı karar gerekmiyor | — |

### C.3 — P1-P6 geçiş-sıralaması kararı (m.37 seçenekleriyle)

*Rakamlar bant halinde ve `[deneysel m.29]` damgalı — tek sayı olarak alıntılanmaz.*

**Partisyonlar (kısa):**
- **P1 — Zemin (izolasyon + durma-koşullu koşum):** treehouse + gnhf Windows'ta ayrı bir deneme deposunda kurulur. Bağımsız, bugün başlar. Salih katılımı **[15-45 dk bandı]**.
- **P2 — Doğrulama hattı (no-mistakes):** deneme deposunda 1 değişiklik uçtan uca hattan geçirilir (JARVIS kanon reposunda DEĞİL). Salih katılımı **[30-60 dk bandı]**.
- **P3 — Plan yüzeyi (metin duvarını öldür):** lavish VE Claude Code'un yerleşik Artifact aracı ikisi de denenir. Bağımsız, bugün başlar. Salih katılımı **[20-40 dk bandı]**.
- **P4 — Kanon hizalaması (çelişki masası):** bu dosyadaki 12 kalem, kalem-kalem imza. P1-P3'ü beklemez, paralel yürür. Salih katılımı **[1-2 sa bandı, masa]**.
- **P5 — firstmate mimarisi (nihai hedefin ilk taşı):** Windows yolu izlemesi (PR #1340/#1400) + JARVIS'teki ikame mimarisinin taslağı. Bağımlı: P1 ∧ P2 ∧ P4(Ç3 hükmü). Salih katılımı **düşük — çoğu ajan işi**.
- **P6 — Enstrümantasyon (m.35'in kurtarılması):** P1-P2'nin log'ları ölçüm-bankına bağlanır. Bağımlı: P1 ∧ P2.

**m.37 sunumu — 3 model + karşıt-temel:**

| | **Model A — İCRA-ÖNCE** | **Model B — KANON-ÖNCE** | **Model C — karşıt-temel: minimax-regret** |
|---|---|---|---|
| Zemin | Beklenen-değer maksimizasyonu — ölçülmüş kazancı hemen al | Tutarlılık-önce — kanon çelişkisi taşımadan ilerle | Worst-case pişmanlığı minimize et |
| Sıra | P1 → P3 → P2 → (P4 paralel) → P6 → P5 | P4 → P1 → P2 → P3 → P6 → P5 | Yalnız P1'in gnhf ayağı + P3'ün Artifact ayağı; dış araç kurulumu YOK; P4 küçültülmüş gündemle |
| Zaman (Salih) | **[≈1-1,5 sa ilk hafta]** | **[≈2-3 sa ilk hafta]** | **[≈30-45 dk ilk hafta]** |
| Kazanç | Şikâyetin kaynağına (Ç2 tetik yükü + Ç4 masa yükü) en hızlı dokunuş; K-010 kanıtı erken birikir | m.16 disiplini tam korunur; hiçbir iş çelişkili zeminde koşmaz | Hiçbir dış bağımlılık alınmaz; firstmate'in olgunluk riski hiç üstlenilmez |
| Kabul edilen bedel | P1-P3, Ç2/Ç3 imzalanmadan koşar → yan-oturum/yetki sınırında gri alan (fren: JARVIS kanon reposunda araç koşturulmaz) | Şikâyet 1-2 masa turu daha sürer | Şikâyet çözülmez, yalnız hafifler |
| Öneri | ✅ **ÖNERİLEN** | — | — |
| Beni çürütecek bulgu | P1'in gnhf koşumu Windows'ta ilk denemede çalışmazsa → sıra Model C'ye düşer | Ç1/Ç8/Ç10 gibi kalemlerin "çelişki değil" çıkması B'nin gerekçesini zayıflatır | Salih ilk gnhf koşumundan sonra "tam istediğim şey" derse C'nin temkini gereksiz maliyet olur |

**Öneri gerekçesi (m.6):** Model A önerilir çünkü senin beyan ettiğin problem bir *kanon* problemi değil, bir *icra* problemi; ve 12 kalemden yalnız 3'ünün gerçek çelişki olması kanon-önce sıralamanın gerekçesini büyük ölçüde ortadan kaldırıyor. Karşıt-temel (Model C) ciddiye alınmalı ve tek bir yerde kazanıyor: firstmate — bu yüzden önerilen sıra firstmate'i en sona koyuyor.

**Karar: BOŞ — MASAYA.** {Model A / Model B / Model C / karma}

---

## (D) YÜRÜRLÜK/BORÇ AYRIMI

*Hangi kalem imzayla ANINDA yürürlüğe girer, hangisi icra borcu açar.*

| Kalem | İmzayla anında yürürlük mü | İcra borcu (varsa) |
|---|---|---|
| K1-1 (işletim usulü) | **Evet** — masa akışını belirler | Yok |
| K1-2 (Model1→3 koşulları) | Hayır | Yazım turu (Katman-2, Carvis) — koşullar KILAVUZ'a işlenir |
| K1-3 (m.41 bölünme) | Hayır | Tüzük yazım turu + 2 D-ölçüm şerhinin hangi yarıya bağlı olduğunun kontrolü |
| K1-4 (m.37e zorlanabilir) | Hayır | m.45 icrası — zorunlu alan tasarımı + tüzük yazımı |
| K1-5 (m.8 silme/arşiv) | Arşiv-indirme seçilirse **evet** (mekanik) / fiilen-sil seçilirse hayır (ayrı inceleme) | Arşive inecek kalemlerin taranması |
| K1-6 (orca arşiv) | **Evet** — tek seferlik mekanik iş | Yok |
| K1-7 (K-010 A3 yazımı) | Hayır | Kapı metni revizyon turu |
| K1-8 (sözlük sırası + SZ-10) | Hayır | Sözlük raporu revizyonu + SZ-10 alan tasarımı |
| K1-9 (m.13 ayrım) | **Evet** — tek cümle eki | Yok |
| K1-10 (sıralama modeli) | **Evet** — P1-P6 sırası belirlenir | Partisyonların kendi DONE-yükleri (ayrı icra emirleri, bu dosyanın kapsamı dışında) |
| K1-11 (Codex-inşa) | n/a | Salih açıklaması bekleniyor |
| K1-12 (kesik (c)) | Zaten kapandı | Yok |

---

## Koşum künyesi (kapanış)

**Emir doğrulaması:** §0'da tam — yol ✅ · başlık birebir ✅ · SHA `cdcdd80` ✅ · dal `main` ✅ · hedef dosya yoktu, `-repl` gerekmedi.

**Okunan dosyalar:** `cc/rapor-2026-08-03-4.md` (tam, 445 satır) · `raporlar/2026-08-02-masa-hazirlik-K2.md` (tam, format emsali) · `raporlar/2026-07-26-compiler-formulu.md` §2 (F1-F9 tam) · `kuyruk/senaryo-defteri.md` (2026-08-03 blokları — model-düşümü + m.16 çelişki kaydı + Salih emri) · `raporlar/kaynak-L8-agentic-workflow-transkript.md` (WSL taraması — transkriptte doğrudan geçmiyor, tanım rapor-4/genel bilgiden).

**F1-F9 uygulaması:** niteleyiciler (Kısım C'deki "değer tespiti", "kayıp değeri" alanları) rapor-4'ten AYNEN taşındı, yumuşatılmadı (F1) · her Katman-1 kalemi rapor-4'ün ilgili bölümüne çapalı (F7) · iddia sırası rapor-4'ün kendi sırası korunarak taşındı (F5, kendi teknik raporumuz) · yeni rakam/hüküm eklenmedi, yalnız çeviri yapıldı (F2/m.39).

**Yasaklara uyum:** karar alınmadı (tüm alanlar BOŞ/MASAYA) · karar İÇERİĞİ değiştirilmedi/yumuşatılmadı · rapor-4'te olmayan hüküm/rakam eklenmedi · kanon yazılmadı · V-numarası atanmadı · git commit/push yapılmadı · yazılabilir yüzey yalnız bu dosya + köprü künyesi (`cc/rapor-2026-08-03-5.md`).

**Teslim ölçüsü:** ~430 satır (hedef ≤500 ✅).

**`/usage`:** Salih tarafından yapıştırıldı — **maliyet $1,90** (tavan $6 · DUR eşiği $4,5 — **aşılmadı**). Detay: API süresi 8dk57sn · duvar-saati 3sa23dk · kod değişikliği +319/-0 satır. Model dağılımı: claude-sonnet-5 (2,9K girdi · 44,0K çıktı · 1,3M cache-okuma · 140,4K cache-yazma, $1,90) + claude-haiku-4-5 (692 girdi · 25 çıktı, $0,0008 — yardımcı/alt-işlem payı). Fren denetimi tamamlandı.

---

**Rapor sonu.** Hüküm verilmedi; 12 Katman-1 kalemi + P1-P6 sıralama kararı MASAYA taşındı.
