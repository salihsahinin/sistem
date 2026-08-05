# KILAVUZ — L8 / Kun-Chen Workflow'u JARVIS'te Kullanmak

*Salih için, İNSAN register. Tek başına, yardımsız okunur. Karar yok, ingest yok — bu bir **kullanım** dosyasıdır.*
*Kaynaklar: `raporlar/kaynak-L8-agentic-workflow-transkript.md` (video) · `cc/rapor-2026-08-03-4.md` (analiz) · `raporlar/2026-08-03-masa-hazirlik-L8.md` (masa) · P1/P2/P3/P6 saha kayıtları (`kuyruk/senaryo-defteri.md` 08-04/08-05 blokları). Sahada doğrulanmamış her satır `[?]` ile işaretli (m.39).*
*Rakamlar `[deneysel m.29]` — bant olarak okunur, tek sayı olarak alıntılanmaz.*

---

## 0. Bu kılavuz nasıl okunur

Üç giriş kapısı var, hangisi lazımsa oradan gir:

| Ne istiyorsun | Nereye git |
|---|---|
| "5 dakikam var, özet" | §1 (tek sayfa) + §6.0 (karar ağacı) |
| "terimi duyunca ne anlamalıyım" | §2 sözlük |
| "şimdi şu işi yapacağım, nasıl?" | §6 senaryolar — 12 senaryo, komutlarıyla |
| "makinemde ne kurulu, komut ne" | §4 envanter + komut kartı |
| "neyi YAPMAM lazım" | §5 kırmızı çizgiler |

**Bu kılavuzun tek iddiası:** Kun Chen'in düzenini "birebir kopyalamak" mümkün değil ve gerekli de değil — çünkü zincirin **tepesi (firstmate) Windows'ta bugün yok**, ve **alt üç katmanı zaten kurulu ve sahada koştu.** Aşağıdaki her şey bu iki cümlenin açılımı.

---

## 1. Tek sayfa

### 1.1 Videonun tek cümlelik tezi
**Darboğaz araç değil, sensin — ve çözüm daha hızlı çalışmak değil, kendini incelemeden çıkarıp süreç kurmak.**

Videodaki her araç bu tek tezin bir uygulaması:

| Araç | Seni hangi darboğazdan çıkarır |
|---|---|
| lavish | **okuma** darboğazı — metin duvarı okuyup karar verme |
| no-mistakes | **inceleme** darboğazı — her diff'i senin gözünle onaylama |
| gnhf | **bekleme** darboğazı — ajanın başında oturma, uyku saatlerinin boşa gitmesi |
| treehouse | **defter** darboğazı — "hangi klasörde ne yapıyordum" bilgisini kafanda taşıma |
| firstmate | **bağlam-değiştirme** darboğazı — oturumlar arası zıplama |

### 1.2 Gemi metaforu (Kun Chen'in kendi çerçevesi)
Sen **kaptansın**, ajanlar **tayfa**, ve en tepede **birinci kaptan (firstmate)** var — tayfayı o yönetir, sen yalnız onunla konuşursun. Beş katmanlı tırmanış: (1) gemiyi kur → (2) tayfayı eğit (hafıza + skill) → (3) tek tayfayla çalış → (4) çok tayfayla paralel çalış → (5) birinci kaptanı işe al.

**JARVIS karşılığı:** metafor ailemiz gemi değil **şirket** (vardiya, pano, tüzük, teslim raporu — V12). Çeviri tablosu: kaptan = Salih (m.1) · birinci kaptan = Carvis'in üst-orkestratör şapkası (m.17 köprü + m.44) · tayfa = CC/ajan koşumları. **CEO rolü devredilmez (m.44)** — yani firstmate kurulsa bile o Carvis'in *gövdesi* olur, yerine geçmez.

### 1.3 Bugün nerede duruyoruz

| Partisyon | İş | Durum | Ne kazandırdı |
|---|---|---|---|
| **P1** | treehouse + gnhf kurulumu | ✅ DONE 08-04 | izolasyon havuzu + durma-koşullu koşum, iki fren modu sahada doğrulandı |
| **P3** | plan yüzeyi (lavish + yerleşik pano/Artifact) | ✅ DONE 08-04 | metin duvarı yerine tıklanabilir yüzey |
| **P2** | no-mistakes doğrulama hattı | ✅ DONE 08-04 | 2 koşum uçtan uca, 2 PR merge, **eskalasyon fiilen çalıştı** |
| **P6** | enstrümantasyon | ✅ DONE 08-05 | `tools/olcum-dortlu.py` + dörtlüler deftere betikle düştü |
| **P5** | firstmate | ❌ **BLOKE** | Windows native desteği yok; PR #1340 (native) / #1400 (WSL) merge değil `[?] güncel durum yeniden bakılmalı` |
| **P4** | kanon masası (12 K1 kalemi) | ⏸ BEKLET | Salih beyanı: "workflow oturdu" denince açılır |

**Yani:** zincirin 4/5'i sende çalışıyor. Eksik olan tek şey "tek muhatap" katmanı — ve onun ikamesi zaten var: **Carvis.**

### 1.4 Sana ne kazandırmadığı (dürüst satır)
Senin 08-03'teki asıl şikâyetin şuydu: *"devamlı bağlam ekleyip context şişirip yapmak istediğim şeyde ilerleyemiyorum."* Bu şikâyetin **iki kaynağı** vardı ve bu araçlar yalnız birine dokunuyor:

- **Kod katmanı** (yaz → doğrula → PR) → no-mistakes + gnhf + treehouse bunu **çözdü**.
- **Karar/kanon katmanı** (masa yükü, her koşumda senin tetiğin, ritüel token'ı) → bunu araç çözmez; **P4 masası + Ç2/Ç4 imzaları** çözer, ve o masa şu an BEKLET'te (senin kararın).

Bunu bilerek kullan: araçlar günlük iş hacmini büyütür, kanon yükünü küçültmez.

---

## 2. Terimler sözlüğü

*Her terim: **ne demek** · **bizdeki karşılığı** · **ne zaman ağzından çıkar**.*

### 2.A Kavramlar (araç değişse de kalır)

**1. Workflow (çalışma düzeni)**
Bir işin baştan sona hangi adımlarla, hangi araçlarla yürütüldüğünü tarif eden düzen. İçerik değil, **yapı**.
*Bizde:* bu kelimenin ortak tanımının olmaması 08-03'te istem kaybına yol açtı — bu kılavuzun var olma sebebi.
*Ne zaman dersin:* "workflow'u değiştirelim" = "adımların sırasını/aracını değiştirelim", "daha çok bağlam ekleyelim" değil.

**2. Harness (ajan koşum ortamı)**
Ajanı çalıştıran program: Claude Code, Codex CLI, Pi, OpenCode. Ajanın komut alıp araç çağırdığı kabuk.
*Bizde:* Cowork + CC birer harness. `[?]`
*Ne zaman dersin:* "harness değiştirdim" = model değiştirmedim, **kabuğu** değiştirdim.

**3. Agent-agnostic (ajan-bağımsızlık)**
Düzeni tek bir ajan/model markasına bağlamamak. Kun Chen'in en katı ilkesi: *"the landscape is changing very, very fast"* (11:01).
*Bizde:* m.41 model-pin'i ("kanon kararı yalnız Fable'da") bunun **tersi** yönde — çelişki Ç3, hüküm masada (K1-3).
*Ne zaman dersin:* bir araç seçerken "bu yalnız Claude'la çalışıyor mu?" sorusu.

**4. Progressive disclosure (kademeli açılım)**
Ajan açılışta yalnız başlığı/özeti yükler; gövdeyi gerçekten gerekince okur. Bağlam şişmesinin ilacı.
*Bizde:* m.20 pointer ilkesi — **birebir aynı kök**, bağımsız türetilmiş. Bu konuda bir eksiğimiz yok.

**5. Adversarial review (karşıt-gözle inceleme)**
Bir değişikliği, onu üreten ajandan **ayrı ve taze bir bağlamda**, kasten çürütmeye çalışan bağımsız tur.
*Bizde:* m.40b (tez → antitez → hakem) aynı aile; alan farklı (bizimki araştırma, no-mistakes'inki kod).
*Şerh:* terim no-mistakes README'sinde literal geçmiyor `[?]` — transkriptin anlatımı.

**6. Escalation (eskalasyon)**
Hattın kendi başına çözemeyeceği, **yargı gerektiren** bulguyu insana yükseltmesi. Mekanik hata otomatik düzeltilir; niyete dokunan şey durur ve sorar.
*Bizde:* m.31 Katman-1/Katman-2 ayrımının makine karşılığı. **Sahada görüldü:** P2 koşum-2'de hat "niyet ile test-sözleşmesi çelişiyor, bu karar meselesi — sessizce yamalanmaz" deyip durdu, sen karara bağladın.
*Ne zaman duyarsın:* TUI'de `ask-user` düştüğünde. **Bu iyi haberdir** — hattın çalıştığının kanıtı.

**7. Risk assessment / riske göre inceleme derinliği**
Her değişikliğe eşit dikkat verilmez; PR gövdesindeki risk etiketi ne kadar bakacağını belirler. Kun Chen: *"For low risk changes, I don't really look at the diff at all"* (32:51).
*Bizde:* m.37(e) + m.42(e) aynı şeyi zaten söylüyor ama **fiilen uygulanmıyor** (Ç4 — gerçek çelişki, hüküm masada K1-4).

**8. Kanıt artefaktı (evidence)**
"Bitti" yetmez; çalıştığının kanıtı üretilir — ekran görüntüsü, log, test çıktısı, video.
*Bizde:* m.9 proof-of-work = push'lanmış commit. Kun Chen bunu **genişletiyor**: commit + kanıt. Çelişki yok, ekleme var.

**9. Durma koşulu (stop condition)**
Uzun koşumun ne zaman biteceğinin **yazılabilir** tanımı. Yazılamıyorsa loop kurulmaz.
*Bizde:* KILAVUZ DONE kuralının loop karşılığı — birebir aynı disiplin.

**10. Worktree (çalışma kopyası)**
Aynı git deposunun diskte ayrı klasöre açılmış paralel kopyası. İki ajanın aynı dosyaya basmasını önler.
*Bizde:* `claude --worktree` yerleşik var. Eksik olan **havuz yönetimi** — onu treehouse veriyor.

**11. Lease (kira)**
treehouse'un havuzdaki bir kopyayı "şu an kullanımda" diye işaretlemesi. Sekmeyi kapatınca serbest kalır.
*Ne zaman görürsün:* `treehouse status` çıktısında. Şu an deneme deposunda **4 lease açık** (temizlik borcu).

**12. Ajan ergonomisi / AXI**
Ajana verdiğin aracın **tasarımı** performansını belirler. Ölçüm: GitHub'a MCP ile erişmek CLI'ya kıyasla ~3× token + 2× gecikme. AXI = bunun 10 maddelik standardı (token-verimli çıktı, tanımlı boş-durum, yapısal hata kodları…).
*Bizde:* kanonda karşılığı yok (E11 = EKSİK-İNŞA); pratikte tesadüfen uyumluyuz (git CLI kullanıyoruz, MCP değil).
*Ne zaman dersin:* yeni bir araç/MCP eklerken "bu ajanın kaç token'ını yakıyor?"

**13. Telemetri**
Aracın kullanım verisini geliştiricisine göndermesi. gnhf ve no-mistakes'te **varsayılan AÇIK**.
*Bizde:* ikisi de kapatıldı (`GNHF_TELEMETRY=0`, `NO_MISTAKES_TELEMETRY=0`) — kurulum öncesi user-env ile.

**14. Kaptan zihniyeti / darboğaz kayması**
Sistem iyileşince darboğaz "ne yapılacağını bilmek"e kayar; enerji yön belirlemeye gider.
*Bizde:* senin "darboğaz ben oldum" beyanınla aynı olgu (m.44 rol katmanları).

### 2.B Araçlar

| Terim | Bir cümlede | Bizde durum |
|---|---|---|
| **treehouse** | git worktree **havuzu** — müsait kopyayı bul/yarat, kullan, çıkınca iade et | ✅ kurulu (v2.1.1) |
| **gnhf** (goodnight-have-fun) | hedef + durma koşulu + token/iterasyon tavanı ile kendi başına koşan orkestratör | ✅ kurulu |
| **no-mistakes** | ittiğin değişikliği izole kopyada doğrulayıp PR'a kadar götüren ve PR'a dadılık eden boru hattı | ✅ kurulu (v1.41.2) |
| **lavish** | planı/kararı metin duvarı yerine tıklanabilir, üstüne not düşülebilir HTML sayfası olarak sunan araç | ✅ kurulu (skill) |
| **firstmate** | tek muhatap orkestratör — işi kendisi bölüp tayfaya dağıtır | ❌ Windows'ta yok |
| **AXI** | ajan-ergonomik araç tasarım standardı (10 ilke) | ilke seti — kurulum yok |
| **npx skills** | skill yükleyici/yönetici CLI (Vercel) | ✅ kullanıldı (lavish bununla indi) |
| **tmux** | terminal oturumunu sunucuda canlı tutan katman | ⛔ gerekmiyor — biz **dosya-kalıcılığı** kullanıyoruz (kapsül + vardiya devri); bizimki cihazdan bağımsız |
| **WezTerm / Neovim** | terminal emülatörü / klavye-odaklı editör | opsiyonel, düşük öncelik |
| **OpenSuperWhisper** | yerel ses→metin | ❌ yalnız macOS — desen alınır, araç alınmaz (V25) |

---

## 3. Ne-ne işe yarar (araç × senin gerçek işin)

### 3.1 no-mistakes — **en yüksek getirili kalem**
**Ne yapar:** ajan "bitti" dediğinde değişikliği hatta sokarsın; hat şunları yapar: dal aç → commit → **izole worktree'de** doğrula → asıl niyeti çıkar → uzak ana dalın üstüne rebase + çakışmaları çöz → **karşıt-gözle inceleme (taze bağlam)** → uçtan uca test + kanıt kaydı → doküman güncelle → lint → push + PR aç → **PR merge olana kadar dadılık** (CI hatası/çakışma çıkarsa o ilgilenir).
README üst-seviye adım sırası: **Review → Test → Docs → Lint → Push → PR → CI.**

**Sana ne kazandırır:** diff okumaktan çıkarsın. PR gövdesindeki **risk değerlendirmesine** bakıp ne kadar inceleyeceğine karar verirsin.

**Sahada ne oldu (P2, `[deneysel m.29]`):**
- Koşum-1: test/doc'suz fonksiyon ittin → hat **eksik testi kendisi yazdı** (safe-fix sınıfı), PR #1 merge. Duvar-saati ~1025 sn (ajan payı ~148 sn).
- Koşum-2: davranış değiştirip testi güncellemedin → hat **DURDU ve sordu** → sen karara bağladın, PR #2 merge. ~453 sn.
**Ders:** hat mekanik eksiği kendisi tamamlıyor, niyet çelişkisinde duruyor. Eskalasyon sınırı doğru yerde.

**Ne zaman KULLANMA:** JARVIS kanon reposunda (§5). Ayrıca 2 satırlık tipo düzeltmesinde — hat 7 adım koşar, iş 10 saniyeliktir.

### 3.2 gnhf — uzun koşum
**Ne yapar:** bir hedef + durma koşulu verirsin, koşullardan biri sağlanana kadar döngüde koşar; her iterasyonda küçük, dokümante commit atar. Token ve iterasyon tavanı vardır — **tavana çarpınca kendiliğinden durur.**

**`/goal`'a karşı tek gerçek üstünlüğü: bütçe freni.** Kun Chen'in kendi gerekçesi (36:03): `/goal` ile yatarsan sabah haftalık kotanın bittiğini görebilirsin; gnhf'te tavanı sen koyarsın.
*Bizim dilimizde:* m.42(b) **Özgürlük ≤ Toparlanabilirlik** ilkesinin ta kendisi.

**Sahada ne oldu (P1):** iki durma modunun **ikisi de** doğrulandı — koşum-1 tavan-freniyle durdu (150K tavan, fiilî 158.587'de kesildi, ~2 dk, 0 commit); koşum-2 hedef koşuluyla durdu (`stop condition met`, ~1 dk 13 sn, 1 commit).
**Kritik kalibrasyon notu:** gnhf'in token sayacı **cache okumalarını da sayıyor** (587K "in"in 587.433'ü cache-read). Yani 150K gibi bir tavan, CC'nin açılış bağlamı yüzünden iş başlamadan dolabilir. Gerçek koşumda tavanı milyon bandında tut.

**Ne zaman KULLANMA:** yargı gerektiren, doğrulanamayan hedeflerde ("mimariyi güzelleştir"). gnhf **doğrulanabilir** hedefler içindir: test kapsamını yükselt, sayfa yükleme süresini düşür, "ilk kullanılabilirlik sorununu bul, düzelt, tekrarla".

### 3.3 treehouse — paralellik zemini
**Ne yapar:** repo içinde `treehouse` yazarsın, seni taze bir worktree'ye bırakır; `treehouse status` hangi kopyaların kullanımda olduğunu gösterir; sekmeyi kapatınca kopya havuza döner ve bir dahakine yeniden kullanılır.

**Sana ne kazandırır:** "hi-bit-2 klasöründe ne yapıyordum?" sorusunu ortadan kaldırır — Kun Chen'in ifadesiyle worktree'nin **defter borcunu** öder.

**Ne zaman KULLANMA:** tek iş koşuyorsan gereksiz. Değeri **≥2 paralel ajan** olduğunda başlar.

### 3.4 lavish — karar yüzeyi
**Ne yapar:** planı/kararı HTML sayfası olarak açar (projenin kendi tasarım diliyle), üstünde işaretleme/not bırakabilirsin, alttaki seçeneklere tıklayarak kararı verirsin, geri bildirim terminale dönmeden ajana gider (`lavish-axi poll` döngüsü).

**Sana ne kazandırır:** m.18(c) detaylı durum raporu ve m.40(a) 3-model sunumu bugün **metin duvarı** olarak geliyor. En yüksek "Salih-yükü" getirisi olan kalem bu.

**Yerleşik alternatif:** CC'nin kendi etkileşimli panosu (P3'te sahada kullanıldı — düğmeyle akışı sürdürdün). Lavish'in yerleşikte olmayan fazlası: **tarayıcıda işaretle-geri-bildir döngüsü.**

**⛔ KIRMIZI ÇİZGİ:** `lavish-axi share` = ht-ml.app'e **PUBLIC yayın**. JARVIS/kanon içeriğiyle YASAK (m.14 + md.49). Ajan bu komutu asla koşmaz — `~\.claude\settings.json` deny kilidi canlı. Gerekirse **sen** kendi terminalinden `--password` ile koşarsın.

### 3.5 `tools/olcum-dortlu.py` — ölçüm (bizim yazdığımız)
**Ne yapar:** gnhf JSONL log'unu ve no-mistakes `state.sqlite`'ını okuyup her koşum için **(token · duvar-saati · iterasyon · sonuç)** dörtlüsünü markdown tablo olarak çıkarır; `--append` ile senaryo-defterine yazar (mükerrer koşum atlanır, eksik alan `[?]`).

**Neden önemli:** m.35 "ölçüm-öncelikli" ilkesinin bedelini düşürür — veriyi **işi yavaşlatarak değil, boru hattını enstrümante ederek** topluyoruz. Ç7'nin kurtarma önerisi buydu ve icra edildi.

---

## 4. Envanter ve komut kartı

### 4.1 Makinede ne, nerede (08-05 itibarıyla)

| Ne | Yol / sürüm |
|---|---|
| Deneme deposu (kanon-DIŞI) | `C:\dev\wf-deneme` → GitHub `salihsahinin/wf-deneme` (**private**, md.49) |
| treehouse | `C:\Users\sasah\AppData\Local\treehouse\treehouse.exe` · v2.1.1 |
| treehouse havuzu | `~\.treehouse\wf-deneme-eddecb\1..4` — **4 lease açık, iade borcu** |
| gnhf | npm global · log: `<repo>\.gnhf\runs\<id>\gnhf.log` (JSONL) |
| no-mistakes | v1.41.2 · durum: `~\.no-mistakes\state.sqlite` · log: `~\.no-mistakes\logs\<run>\*.log` · daemon: Task Scheduler |
| lavish | `~\.agents\skills\lavish` (universal) + `~\.claude\skills\lavish` (elle kopya) |
| Ölçüm betiği | `C:\JARVIS\tools\olcum-dortlu.py` |
| Telemetri | gnhf ✅ kapalı · no-mistakes ✅ kapalı (user-env) |
| share kilidi | `~\.claude\settings.json` → `permissions.deny` 3 kalıp (yedek: `settings.json.bak-20260804`) |

### 4.2 Komut kartı (kopyala-yapıştır)

```powershell
# --- İZOLASYON -------------------------------------------------
treehouse                 # taze worktree'ye düşer (subshell); exit → havuza iade
treehouse status          # hangi kopya kullanımda / boşta
treehouse return <yol>    # elle iade   [?] --help ile doğrula

# --- UZUN KOŞUM ------------------------------------------------
gnhf --help                              # ÖNCE bunu koş: flag adları buradan doğrulanır
gnhf "<hedef cümlesi>" --stop-when "<durma koşulu>" `
     --max-iterations <N> --max-tokens <T>          # [?] tam sözdizimi --help ile teyit
#   ŞART: temiz working-tree'li git reposu
#   Tavan: cache-read dahil sayılır → milyon bandında tut (150K ERKEN durdurur)

# --- DOĞRULAMA HATTI -------------------------------------------
no-mistakes doctor        # sağlık kontrolü (git · gh · runner)
git push no-mistakes      # asıl tetik: değişikliği hatta sokar
no-mistakes               # TUI (canlı koşumu izle / ask-user'a cevap ver)
no-mistakes -y            # headless
/no-mistakes <görev>      # ajan içinden skill olarak

# --- PLAN YÜZEYİ -----------------------------------------------
/lavish                   # ajan içinden: kararı HTML artefakt olarak aç
lavish-axi poll           # tarayıcıdaki geri bildirimi ajana taşır
# lavish-axi share        # ⛔ YASAK (public yayın) — deny kilidi canlı

# --- ÖLÇÜM -----------------------------------------------------
python C:\JARVIS\tools\olcum-dortlu.py                 # önizleme
python C:\JARVIS\tools\olcum-dortlu.py --append        # deftere yaz
python C:\JARVIS\tools\olcum-dortlu.py --repo C:\dev\baska-repo
```

**Windows tuzağı (P2'de hat yakaladı):** PowerShell `Set-Content` CRLF + BOM yazar. Dosya yazarken **`-Encoding utf8NoBOM`** kullan.

---

## 5. Kırmızı çizgiler

1. **JARVIS kanon reposunda (`C:\JARVIS`) hiçbir araç koşturulmaz.** Ne gnhf, ne no-mistakes, ne treehouse. Gerekçe: m.8 (silme yasağı) + m.31 (Katman-1) riski — bir otomat kanona yazarsa geri alma maliyeti yüksek. Araçlar `C:\dev\wf-deneme`, PortRisk ya da staj deposunda koşar. Bu, Model A'nın "kabul edilen bedeli"ne karşı konmuş frendir.
2. **`lavish-axi share` ⛔** — public yayın. Deny kilidi ajanı durdurur; sen bilinçli koşarsan `--password` ile.
3. **Artefaktlar PUBLIC üretilmez** (md.49 revize, imzalı). Yerel/özel yeter.
4. **Staj verisi JARVIS'e taşınmaz** (md.49 sınır beyanı) — yazılı izin yoksa.
5. **Telemetri kurulum ÖNCESİ kapatılır** (emsal: P1/P2).
6. **İnternetten skill kurma disiplini:** Kun Chen'in kuralı ("ölçülmemiş skill kurma") bizde daha katı — **yıldız yasağı** (KILAVUZ md.33) + eval şartı + SKILL.md'yi kurmadan önce okuma (P3'te lavish'e uygulandı; yan ürün `find-skills` Snyk'te Med Risk çıktı, kullanılmıyor).
7. **m.9 saklı:** iş push'lanmış commit'le sayılır. no-mistakes bunu genişletir (kanıt artefaktı), yerine geçmez.

---

## 6. Örnek kullanım senaryoları

### 6.0 Karar ağacı — "hangi araç?"

```
İş kanon reposunda mı (C:\JARVIS)?
├── EVET → araç YOK. Carvis + CC hattı. (S5)
└── HAYIR ↓
    Ne yapacaksın?
    ├── Ne yapılacağı BELİRSİZ → lavish/pano ile plan turu (S2)
    ├── Ne yapılacağı BELLİ, tek iş, kısa → ajan + git push no-mistakes (S1)
    ├── Ne yapılacağı BELLİ, 2+ bağımsız iş → treehouse × N sekme (S4)
    ├── Hedef doğrulanabilir + uzun/tekrarlı → gnhf (S3)
    └── Sadece soru soruyorum → hiçbiri; düz sohbet
```

---

### S1 · Tek dosyalık kod değişikliği (PortRisk'te bir bug)
**Durum:** getiri hesabında bir hata var, düzeltme belli.

1. `C:\Users\sasah\dev\portrisk` içinde ajanı aç, düzeltmeyi yaptır.
2. `git push no-mistakes`
3. **Ekranın başında bekleme** — başka işe geç. Hat: Review → Test → Docs → Lint → Push → PR.
4. Hat bitince PR'ı aç. **Önce risk değerlendirmesine bak**, diff'e değil.
   - Risk düşük → diff'e bakma, merge.
   - Risk orta/yüksek → yalnız işaretlenen dosyalara bak.
5. Hattın kendi düzelttiklerini (eksik test, lint, BOM) PR gövdesinden denetle — "bunlar gerçekten istediğim şey mi?"

**Beklenen duvar-saati:** ~[7-20 dk bandı] `[deneysel m.29]` (P2 ölçümü: 453-1025 sn).
**Ne zaman DUR:** hat `ask-user`'a düşerse — o **karar meselesidir**, hattın yamalamasına izin verme.

---

### S2 · "Nasıl yapsak?" — belirsiz iş (plan turu)
**Durum:** bir özelliğin nasıl kurulacağına karar verilmemiş.

1. Ajana **seçenek üret** dedirt: "3 seçenek çıkar, tartışalım."
2. `/lavish` (ya da CC'nin yerleşik panosu) → seçenekler tıklanabilir sayfa olarak açılır.
3. Sayfa üzerinde işaretle, not düş, seçenek düğmesine bas. `lavish-axi poll` geri bildirimi ajana taşır.
4. Karar netleşince "başla" de — **icra sırasında müdahale etme.**
5. Bitince S1'e geç (`git push no-mistakes`).

**Neden bu sıra:** Kun Chen'in gözlemi — zaman **başta** (planlama) ve **sonda** (kalite eşiği) harcanır; ortası ajanındır. Ortayı ne kadar uzatırsan o kadar paralel iş açarsın.

---

### S3 · Gece koşumu / uzun tekrarlı iş (gnhf)
**Durum:** "PortRisk'in test kapsamını yükselt" ya da "uygulamayı 7 yaşında bir çocuk gibi kullan, ilk kafa karıştıran şeyi bul-düzelt-tekrarla."

1. Repo **temiz** olmalı (commit'siz değişiklik varsa gnhf başlamaz).
2. `gnhf --help` ile flag adlarını teyit et `[?]`.
3. Koşumu üç şeyle başlat: **hedef** + **durma koşulu** + **tavan**.
   - Durma koşulu yazılamıyorsa **loop kurulmaz** (KILAVUZ DONE kuralı).
   - Tavanı milyon bandında tut — cache-read sayılıyor.
4. Yat / başka işe geç.
5. Sabah: `.gnhf\runs\<id>\gnhf.log` + commit listesi. **Hangi commit'i alacağına sen karar verirsin** — otomatik merge yok.
6. `python C:\JARVIS\tools\olcum-dortlu.py --append` → dörtlü deftere.

**İki durma modu da sahada doğrulandı:** tavan-freni ve hedef-koşulu.
**Ne zaman KULLANMA:** hedef doğrulanamıyorsa. "Kodu güzelleştir" bir gnhf hedefi değildir.

---

### S4 · Aynı anda 3 iş (treehouse)
**Durum:** üç bağımsız küçük iş var, hiçbiri diğerini beklemiyor.

1. Repoda `treehouse` → 1. sekme, taze kopya, ajanı aç, işi ver, sonuna **"bitince no-mistakes koştur"** ekle.
2. Yeni sekme → `treehouse` → 2. iş. Aynısı.
3. Yeni sekme → `treehouse` → 3. iş.
4. `treehouse status` ile kimin nerede olduğunu gör (kafanda tutma).
5. Sekmeyi kapat → kopya havuza döner.

**Kural:** aynı klasörde iki ajan koşturma — birbirinin dosyasına basar.
**Temizlik:** iş bitince lease'leri iade et; şu an 4 açık lease borcu var.

---

### S5 · JARVIS kanon reposunda iş (rapor, tüzük, karar)
**Durum:** tüzük maddesi yazımı, masa hazırlığı, kapsül/pano güncellemesi, araştırma raporu.

**Araç kullanılmaz.** Hat şudur: Carvis emri derler → CC ya da Cowork koşar → çıktı `raporlar/` veya `cc/`ye düşer → Carvis yorumlar (kör aktarım yasak, m.6/m.7) → sen karar verirsin → yazım turu ayrı commit'le kanona iner.

**Neden:** kanon reposunda otomat koşturmak m.8/m.31 riski taşır; Model A'nın kabul edilmiş freni budur.
**Buradaki hızlanma araçtan gelmez** — P4 masasının imzalarından gelir (Ç2 tetik yükü, Ç4 masa yükü). O masa senin "workflow oturdu" beyanını bekliyor.

---

### S6 · Staj işi (Otonet/Otoplus, 11 Ağu)
**Durum:** rolün "doğrulama katmanı" — agentic coding ekibinde üretilen kodu denetlemek.

- **no-mistakes tam bu rolün makinesi.** Hattın adım dizisi (niyet çıkarımı → karşıt inceleme → kanıtlı test → doküman → lint) senin elle yapacağın denetimin şablonu; ne bulduğunu okuyup öğrenirsin.
- **Sınır:** staj verisi JARVIS'e taşınmaz (md.49). Staj reposu ayrı yaşar; JARVIS'ten yalnız **desen** gider, veri gelmez.
- **İlk hafta için hazır cümle:** "değişiklik doğrulaması için izole worktree + taze bağlamda karşıt inceleme + kanıt artefaktı" — bu üçlü senin ölçülmüş deneyimin (2 koşum, 2 PR).

---

### S7 · Araştırma / öğrenme işi
**Durum:** "şu konuyu araştır", "bunu öğrenmek istiyorum".

**gnhf değil.** Araştırma hattı ayrı: m.40 çift-atlas + m.40b diyalektiği + CC görev emri. gnhf **doğrulanabilir hedef** makinesidir; araştırmanın durma koşulu yazılamaz.
Öğrenme şeridi de ayrı yürür (`ogrenme/mufredat.md`).

---

### S8 · Karar masası (m.37 sunumu)
**Durum:** 3 model + karşıt-temel sunulacak, sen imza atacaksın.

1. Carvis 3 modeli hazırlar.
2. **Metin duvarı yerine** `/lavish` veya yerleşik pano — her model bir kart, altında seçim düğmeleri.
3. Sen kartlara not düşersin, seçersin.
4. Karar `kuyruk/senaryo-defteri.md`'ye iner (m.37).

**Ölçüm borcu:** metin duvarı ↔ artefakt karşılaştırma notu (okuma süresi + karar netliği) — P3 DONE-yükleminde vardı, ilk gerçek koşumda düşülecek.

---

### S9 · Ölçüm alma
Her anlamlı koşumdan sonra:
```powershell
python C:\JARVIS\tools\olcum-dortlu.py --append
```
Çıktı: koşum başına **token · duvar-saati · iterasyon · sonuç**. Mükerrer koşum atlanır, bulunamayan alan `[?]` yazılır (m.39).
**Neden her seferinde:** m.35'in verisi budur; elle toplanırsa toplanmaz.

---

### S10 · Bir şey ters gitti (teşhis)
**Altın kural (P2 dersi):** **hüküm log'dan verilir, semptomdan değil.**

| Belirti | Gerçek kök (sahada görülen) | Ne yap |
|---|---|---|
| "wait for run within 5s" | daemon değil — **boş diff** (dalda gerçek değişiklik yok, hat tüm adımları atlayıp bitiyor) | `~\.no-mistakes\logs\<run>\rebase.log` → "empty diff after rebase" |
| gnhf 2 dakikada durdu | tavan cache-read'le doldu | tavanı yükselt, `gnhf.log`'da `max tokens reached` satırına bak |
| "kurulmadı" sanısı | özet ekranı yanıltır (lavish vakası) | **diske bak**, kurulum yoluna git |
| Kapı deposuna tekrar push hook'u tetiklemiyor | aynı SHA | boş commit ile yeniden tetikle |
| Türkçe karakter bozuk | PowerShell BOM | `-Encoding utf8NoBOM` |

---

### S11 · Yeni araç ya da skill kurulacak
1. **Yıldız sayısına bakma** (md.33 yasak). Bak: indirme sırası + son sürüm tarihi + bakımcı sayısı.
2. SKILL.md / README'yi **kurmadan önce oku** — ne çalıştırıyor, nereye yazıyor, dışarı veri gönderiyor mu.
3. Telemetri varsa **kurulumdan önce** kapat.
4. Eval şartı: JARVIS skill'i eval setiyle doğar; çıplak "%100 geçti" yasak.
5. Reddedilen araç gerekçesiyle "şu an alınmaz" listesine yazılır — altı ay sonra aynı soru gelince cevap hazır.

**Emsal:** firstmate bu sınavdan bugün **geçemiyor** — 554 açık issue, sürüm etiketi yok, Haziran 2026 doğumlu. gnhf ve treehouse geçiyor (semver disiplinli, düşük issue). Sınav zaten yapıldı.

---

### S12 · "Tek muhatapla konuşmak" — firstmate yokken
**Durum:** nihai hedefin buydu; araç Windows'ta yok.

**İkame bugün çalışıyor ve adı Carvis.** Fark şu: firstmate bir **program** (tmux sekmesi açar, treehouse çağırır, no-mistakes koşturur, sonuçları toplar); Carvis bir **protokol** (sen söylersin, o emri derler, koşumu dağıtır, çıktıyı kendi değerlendirmesiyle sunar).

Pratikte tek muhatap düzenine en yakın günlük akış:
1. Sabah: "günaydın" → kapsül + pano → tek net sıradaki iş.
2. Gün içinde: işi **cümleyle** ver, aracı seçmeyi Carvis'e bırak (m.25 ölçek-tercihi).
3. Paralel iş gerekiyorsa S4; uzun iş gerekiyorsa S3 — sekmeleri sen açarsın (firstmate'in yapmadığı tek şey bu).
4. Akşam: "uyucam" → teslim + kapsül + push.

**Ne zaman değişir:** firstmate'in Windows PR'ları (#1340 native / #1400 WSL) merge olursa `[?]` — o zaman P5 açılır. Kontrol etmek bir dakikalık iştir, ayda bir bak.

---

## 7. Bir gün nasıl geçer (şablon)

| Zaman | Ne |
|---|---|
| Açılış | "günaydın" → kapsül/pano → tek sıradaki iş |
| İlk blok | Belirsiz işi **plan turuna** sok (S2). Belli işleri sırala. |
| Paralel blok | 2-3 işi treehouse sekmelerinde başlat, her birine "bitince no-mistakes" ekle (S4) |
| Beklerken | Kanon işi (S5) ya da öğrenme — **ajanın başında oturma** |
| Toplama | PR'lara git, **risk etiketine göre** incele, merge et |
| Kapanış öncesi | `olcum-dortlu.py --append` (S9) |
| Kapanış | "uyucam" → teslim + kapsül + push. Uzun iş varsa gnhf'i gece koşumuna bırak (S3) |

---

## 8. Eksik kalanlar ve senin masanda bekleyenler

**İnşa borçları:**
- **P5 / firstmate** — Windows bekliyor. İkame: Carvis (S12).
- **lavish ilk gerçek CC koşumunda test edilmedi** — ilk uygun koşumda 1 deneme, sonuç deftere.
- **4 treehouse lease iadesi** + `find-skills` silme kararı (m.8 gereği sende).
- **Türkçeleştirme turu** — koşum çıktıları İngilizce; `.no-mistakes.yaml`/global config dil yönergesi araştırılacak (senin beyanın: "en son her şey bitince"). Not: m.10 commit-İngilizce kuralı saklı.

**Karar bekleyenler (P4 masası — "workflow oturdu" beyanınla açılır):**
- K1-2 · CC Model-1 → Model-3 geçiş koşullarının yeniden türetilmesi (**tetik yükü** — şikâyetinin merkezi)
- K1-3 · m.41'in bölünmesi (yetki-sınırı ↔ model-pin)
- K1-4 · m.37(e) risk-göre-derinliğin **zorlanabilir** hale gelmesi (**masa yükü** — bağlam şişmesinin en büyük iç kaynağı)
- K1-5 · m.8 silme ↔ arşiv hükmü · K1-6 · orca arşivi · K1-7 · K-010 A3 yazımı · K1-8 · sözlük sırası + SZ-10 · K1-9 · m.13 ayrımı · K1-11 · "Codex-inşa" açıklaması

**Kapı ilişkisi (K-010):** gnhf koşumları A3'ün istediği kanıtı doğrudan üretiyor; no-mistakes'in izole-worktree + eskalasyon disiplini A2 guardrail saha-testinin malzemesi. **Kapı delinmedi — kapı bu yolla doluyor.**

---

## 9. Künye ve şerhler

**Bu kılavuz ne yapmadı:** karar almadı · kanon (`core/`, `CLAUDE.md`) yazmadı · kapsül/pano/senaryo-defteri güncellemedi (**ingest yok — senin emrin**) · V-numarası atamadı · yeni rakam üretmedi.

**Kaynak ayrımı:**
- `[D-belge]` sınıfı: araç README'leri (rapor-4 §II.1 taraması, 08-03 ölçüm anı).
- Saha: P1/P2/P3/P6 koşumları (`kuyruk/senaryo-defteri.md` 08-04 / 08-05 blokları).
- `[?]` işaretliler: gnhf tam CLI sözdizimi (`--help` ile teyit edilecek) · `treehouse return` imzası · firstmate Windows PR'larının güncel merge durumu · "harness" teriminin bizdeki resmi karşılığı (kanonda tanımlı değil).

**Bilinen sapma (m.39, rapor-4'ten taşındı):** transkriptin anlattığı no-mistakes adım dizisi README'de bu granülerlikte yok; "adversarial review" ve "rebase" terimleri README'de literal geçmiyor — kavramlar "Review" adımı içinde örtük olabilir. Yani §3.1'deki adım anlatımı **transkripte** dayanıyor, birincil belgeye değil.

**Rakamların statüsü:** tüm süre/token değerleri `[deneysel m.29]` — N=2 (gnhf) ve N=5 (no-mistakes) koşumdan geliyor, sertifika değil.

---

**Kılavuz sonu.**
