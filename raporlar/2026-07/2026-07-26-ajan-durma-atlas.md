# Ajanlar Neden Duruyor — sonlanma, kota, dayanıklılık

*Kayıt: 2026-07-26 · Carvis (CC, yan-oturum m.41) · Talep: "stopped olan ajanlarım neden duruyor bunu çözmek için ne yapabiliriz ne öğrenmem lazım araştır atlasları koş rapor çıkar"*

**Aileler:** A25 (sonlanma taksonomisi) · A26 (kota mimarisi) · A27 (dayanıklılık ve sürdürme)
**Kanıt rejimi:** Bu aile, oturumun **en yüksek kanıt değerli** ailesidir. Üç bağımsız birincil katman kullanıldı: **kurulu CLI kaynağı** (`cli.js` zod şemaları) · **canlı transkriptler** (115 alt-ajan, bu oturumun kendi verisi) · **ham doküman markdown'ı** (`.md` son ekiyle doğrudan çekim). Neredeyse tüm bulgular **[D]**.

---

## ⛔ DÜZELTME KAYDI — 2026-07-26 antitez turu (bu bölüm sonradan eklendi)

**Bu rapor teslim edildikten SONRA antitez koştu ∧ gerçek hatalar buldu.** Antitez `tool_uses = 48` ile çalıştı: `code.claude.com/docs/en/*.md` ham `curl` ile çekildi ∧ kurulu `cli.js` grep'lendi ⇒ **kanıt sınıfı [D]**, model belleği değil. Hakemlik kaydı: `raporlar/2026-07-26-antitez-hakemlik.md` §5.

| Düzeltme | Nerede | Ne oldu |
|---|---|---|
| **K14 ⭐⭐** | §10 · §11 U1 · §13 A27③ · §15 V71 | **Explore/Plan sürdürülemezliğinin dokümanda dayanağı BULUNAMADI ⇒ ASKIYA ALINDI** |
| **K11 ⭐** | §1 · §3 · §13 A25④ | `is_error = false` **çürütüldü ⇒ [X]**; pratik tavsiye korunur, gerekçesi düşer |
| **K12 ⭐** | §8 · §13 A26③ | *"Alt-ajanlar cache'ten yararlanamaz"* **yanlış**; isabet sıfırı yalnız ilk çağrıda |
| **K13 ⭐** | §8 · §9 · §13 A26① | *"Bağlayıcı sınır 10"* **üç ayrı mekanizmayı birleştirmiş**; sayı korunur, gerekçe düzelir |
| K15 | §0 · §13 A25① | `Stopped` çerçevesi makine kapanmasında çatlıyor |
| K16 | §0 · §13 A25② | `claude agents` **belirli koşulda** alt-ajanları listeler |
| K17 | §3 · §13 A25⑤ | `result` alanının yokluğu **dile bağlı** |
| K18 | §4 · §13 A25⑥ | *"tek keskin ayırt edici"* süperlatifi düşer |
| H16 | §4 · §13 A25⑧ | *"yalnız son metin bloğu"* formülasyonu abartılı-dar |
| **§3.1 (yeni)** | §3 · §4 · §14 C2 | ⭐ **Taksonomide olmayan dördüncü durum ölçüldü: SESSİZ ÖLÜM** (bildirim üretmeyen sonlanma) ∧ **asılma nöbetçisi bu sürümde YOK** |

⚠️ **En pahalı hata sınıfı burada görüldü (M5):** K14, tek bir alt-ajanın aktardığı doğrulanmamış bir iddiaydı ∧ **"ÇOK YÜKSEK değer, maliyet sıfır"** etiketiyle tavsiye listesinin **başına** konmuştu. Türetilen kural adayı: `tavsiye_sırası = 1 ⇒ dayanağı BAĞIMSIZ doğrulanmış olmalı`.

---

## 0 — Önce düzeltme: sorunun öncülü yanlıştı

Salih "**stopped** olan ajanlarım neden duruyor" diye sordu. Ölçüm bunu düzeltiyor:

> **[D] `Stopped` durumuna üç yolla girilir:** `Ctrl+X` · `claude stop`/`claude kill` · sürecin dışarıdan öldürülmesi (`kill`).
> **Oturum limiti, hız limiti, max_turns, stall zaman aşımı — hepsi `Failed` üretir, `Stopped` DEĞİL.**
>
> **[K15 · antitez daraltması] "YALNIZ" kelimesi düştü.** `agent-view.md`: **makine kapanması** da dışarıdan süreç sonlandırmadır ∧ `Failed` üretir, `Stopped` değil ⇒ *"ancak ve ancak bu üç yol"* çerçevesi bu kenar-durumda çatlıyor. İkinci daraltma: **agent-view oturum durumu ≠ alt-ajan task durumu**; bu iddia ikisini birleştiriyor olabilir. Ana hüküm (*limit → Failed, Stopped değil*) **ayakta**.

Ampirik teyit, bu oturumun kendi verisinden: **35 bildirim → 22 `completed`, 13 `failed`, 0 `stopped`.** Yani bu oturumda **hiçbir ajan "stopped" olmadı**; hepsi ya bitti ya `failed` oldu.

**Ve asıl bulgu şu:** `Stopped` aslında sistemin **en net tanımlı** durumudur (yalnız insan/dış müdahale). Belirsiz olan **`Failed`**'dır — limit, API hatası, stall ve araç hatası hepsi oraya yığılır. Kafa karışıklığının kaynağı Stopped değil, **Failed'ın aşırı yüklenmiş olması**.

**Bir kategori hatası daha [D]:** `claude agents` komutu alt-ajanları **ayrı satır olarak listelemez**. İki ayrı dünya var:
| | Arka plan oturumu | Alt-ajan (subagent) |
|---|---|---|
| Nerede görünür | `claude agents` | `/tasks`, @-mention |
| Durum dosyası | `~/.claude/jobs/<id>/state.json` | `~/.claude/projects/<slug>/<uuid>/subagents/agent-<id>.jsonl` |
| Bu makinede | **`~/.claude/jobs/` HİÇ YOK** | **115 transkript var** |

Bizim koştuğumuz her şey **alt-ajan**. `claude agents`'a bakarak onları aramak sonuçsuz kalır.

> **[K16 · antitez daraltması] "Hiç göstermez" düştü.** `sub-agents.md` bir geri-düşüş yolu tanımlıyor: *"`claude agents` bir sayı ∧ ardından yapılandırılmış alt-ajanlarını basıp çıkıyorsa, agent view kullanılamıyor demektir."* ⇒ **agent view kapalıysa komut yapılandırılmış alt-ajanları listeler.** Ana tablo iddiası (*alt-ajanlar ayrı satır olarak listelenmez*) **doğru kalır**; mutlak "hiç" **yanlıştır**.

---

## 1 — İki eksen tek satırda gösteriliyor

**[D]** Agent view **iki ortogonal ekseni** aynı satırda gösterir:

| Eksen | Değerler |
|---|---|
| **Görev durumu** | Working · Needs input · Idle · Completed · Failed · Stopped |
| **Süreç canlılığı (ikon)** | `✻`/`✽` süreç canlı, hemen cevap verir · **`∙` süreç çıkmış** — "peek, reply, attach yapabilirsin, Claude kaldığı yerden devam eder" · `✢` `/loop` uykusu |

**`∙` bir sonlanma durumu DEĞİLDİR.** Boşta ~1 saat kalan oturumun sürecini süpervizör kaynak boşaltmak için kapatır; transkript ve durum diskte kalır. "Ajan öldü" sanılan şeylerin bir kısmı budur.

**Yanlış alarm listesi (ölüm değil):**
- `∙` ikonu → süreç çıktı, durum değil
- `Needs input` → izin/soru/sandbox/MCP kimlik doğrulaması bekliyor; çalışmıyor **ama ölmedi**
- SDK'da `is_error` alanına bakarak limit-ölümü elemeye çalışmak → **bu alan güvenilmez, `subtype`'a bak** (§3'e bak, K11)

---

## 2 — ▲ En önemli bulgu: `failed` TERMİNAL DEĞİL

**[D-ölçüm]** Bu oturumda üç ajan 04:11–04:15 arasında oturum limitinden `failed` bildirdi (limit sıfırlanması 04:50). Üçünün de transkripti **05:08–05:12'ye kadar yazmaya devam etti** — limit kalkınca devam edip raporlarını **bitirdiler**.

A25 ajanı bunu ölçtüğünde "üçünden yalnız biri ikinci bir `completed` gönderdi; 3 rapordan 2'si teslim edilmedi" hükmünü verdi.

### ▲ Bu hükmü tam-oturum verisiyle doğruladım — ve düzeltiyorum

Kendi taramam (115 transkript, hata damgasından **sonra** >1500 karakter rapor üretenler):

| agent | API hatası | raporu bitirdi | boyut | ebeveyne ulaştı mı? |
|---|---|---|---|---|
| a42b10d91a6e5aa0b | 04:15:21 | 05:08:15 | 21.539 | ✅ `completed` 05:08:15 |
| ae36ca7e628426646 | 04:10:06 | 05:10:07 | 20.274 | ✅ `completed` 05:10:07 |
| a35469f5cfcb60562 | 04:11:51 | 05:10:12 | 34.998 | ✅ `completed` 05:10:12 |
| a30319a895816429b | 04:09:56 | 05:10:15 | 21.300 | ✅ `completed` 05:10:15 |
| ae8b34d118ee49232 | 04:11:45 | 05:12:38 | 30.542 | ✅ `completed` 05:12:38 |

**Beşi de teslim edildi. Bu oturumda veri kaybı YOK.**

**Ama bu bir tesadüf değil, bir müdahalenin sonucu:** o beş ajanı limit kalktıktan sonra **elle `SendMessage` ile sürdürdüğüm için** teslim edildiler. Müdahale olmasaydı A25'in hükmü doğru olacaktı — raporlar diskte kalacaktı.

**Damga:** A25 bulgu 17'nin **mekanizması [D] doğrudur** (`failed` terminal değildir; ajan sonradan bitirebilir). **Sayısı ("3'ten 2'si kayıp") [X] yanlıştır** — ölçüm resume'lar kayda geçmeden önce alınmış. Mekanizma korunur, sayı düşer.

**Operasyonel sonuç:** `failed` gördüğünde ajanı **ölü sayma**. Limit sıfırlandıktan sonra `SendMessage` ile sürdür — tam bağlamıyla kaldığı yerden devam eder.

---

## 3 — Sonlanma taksonomisi: katmanlar arası kayıp

**[D-kod]** SDK `result` mesajı iki şemanın union'ı:

- **Başarı:** `{subtype:"success", ..., result: string, ...}`
- **Hata:** `{subtype: "error_during_execution" | "error_max_turns" | "error_max_budget_usd" | "error_max_structured_output_retries", ..., errors: string[], ...}`

**▲ Yapısal fark:** hata şemasında **`result` alanı yok** (TypeScript). Ajan limite çarptığında metin çıktısı için ayrılmış alan kayboluyor.

> **[K17 · antitez daraltması] Bu dile bağlıdır, iddia dil belirtmiyordu.** TypeScript için doğru: `result` alanı şemada **yoktur**. **Python dataclass'ı ise tüm varyantları tek şekle düzleştirir** ⇒ `result` alanı **vardır ∧ değeri `None`'dır**. Kod yazarken alanın **yokluğuna** değil, **`subtype`'a** bakılır — bu iki dilde de doğrudur.

**▲ TUZAK — ve bu tuzağın kendisi çürütüldü:**

> **[K11 · antitez ÇÜRÜTMESİ — ⭐ yüksek ⇒ `⊨X`, çözülmedi]**
> **Bizim iddiamız:** `error_max_turns` ∧ `error_max_budget_usd` için `is_error = false`. Dayanak: kurulu `cli.js` v2.1.42'de birebir `subtype:"error_max_turns", ..., is_error:!1`.
> **Antitez, `agent-sdk/python.md`'den birebir:** *"`is_error`: `True` when the conversation ended in an error state. **Always `True` on the `error_*` subtypes.**"*
> **Hüküm: DOĞRUDAN ÇELİŞKİ, çözülmedi.** Olası uzlaştırmalar — **hiçbiri doğrulanmadı**: ① minifiye kod okuması yanlış olabilir · ② CLI'nin iç üretim yolu ile SDK'nın belgelenmiş sözleşmesi **farklı katmanlar** olabilir · ③ sürüm kayması (kurulu `v2.1.42` ↔ doküman `~v2.1.217`).
> **PRATİK SONUÇ — tavsiye ayakta, gerekçesi düştü:** *"limit-ölümlerini `is_error` ile filtreleyemezsin"* gerekçesi **artık güvenilmez**. Ama filtre yazacaksan **`subtype`'a bak** — bu **her iki senaryoda da** doğru kalır. Yani yapılacak iş değişmiyor, **neden yapıldığı** değişiyor.

### Katmanlar arası kayıp — Claude'un tekil zaafı

| | (a) iş bitti | (b) bütçe/limit | (c) dış iptal | (d) altyapı hatası |
|---|---|---|---|---|
| **Temporal** | COMPLETED | `MAXIMUM_ATTEMPTS_REACHED` | **CANCELED ≠ TERMINATED** | FAILED / TIMED_OUT |
| **LangGraph** | normal dönüş | `GraphRecursionError` | `NodeCancelledError` / `GraphDrained` | `NodeTimeoutError` / `NodeError` |
| **Claude SDK** | `success` | `error_max_turns` / `error_max_budget_usd` | *(subtype yok)* | `error_during_execution` |
| **Claude UI** | Completed | **→ Failed** | Stopped | **→ Failed** |
| **Celery** | SUCCESS | *(→ FAILURE)* | REVOKED | FAILURE |

**Ortak desen:** üçü de (a)/(c)/(d)'yi ayırıyor; **ayrışma noktası (b)**. Temporal ve LangGraph bütçeyi birinci-sınıf yapıyor, Celery yapmıyor. Claude SDK yapıyor — **ama UI katmanı 4 hata subtype'ını tek `Failed`'a çöktürüyor** (`task_notification` enum'u yalnız 3 değerli: `completed`/`failed`/`stopped`).

→ **Zaaf taksonomide değil, katmanlar arası kayıpta:** SDK'da 5 ayırt edilebilir terminal durum var, ekranda 3 kalıyor, **(b)+(d) ayrımı tamamen siliniyor.**

### ⛔ 3.1 — TAKSONOMİ EKSİK: dördüncü ve kayıtsız durum (canlı ölçüm, 15:56)

*Bu bölüm rapor teslim edildikten sonra, A5–A21 antitez turları koşarken **ölçülerek** eklendi.*

**Gözlem:** üç antitez ajanı da `15:10–15:11` arasında son kaydını yazdı ∧ **45 dakika boyunca hiçbir yeni kayıt düşmedi.** 45 saniye arayla alınan iki örnekte `boyut`, `satır sayısı` ∧ `mtime` **üçü de birebir aynı** ⇒ `büyüme = 0`.

**Son kayıt imzası (üçünde de aynı):** `type = assistant` ∧ `content = ['text']` ∧ `isApiErrorMessage = None` ∧ `stop_reason = None`
⇒ **§4'teki hiçbir imzaya uymuyor:** API ölümü değil (17-vakalık sınıf değil), araç ortası ölüm değil (`tool_use` yok). **Metin ürettiler, sonra sustular.**

**Ve kritik olan:** `SendMessage` üçüne de **`"had no active task"`** döndürdü ⇒ ajan ölü ∧ çalışmıyor.
⇒ **AMA HİÇBİR `task_notification` GELMEDİ.** Ne `completed`, ne `failed`, ne `stopped`.

> ### ⭐ HÜKÜM — §3 tablosuna EK
> **`sonlanma_modu = SESSİZ ÖLÜM`:** ajan durur ∧ aktif görevi kalmaz ∧ **hiçbir bildirim üretmez.**
> ⇒ Yukarıdaki tablo *"SDK 5 durum → UI 3 değer"* diyordu. Bu vaka **dördüncü ve kayıtsız** bir durumdur: **bildirim üretmeyen sonlanma**.
> ⇒ **§4 teşhis kılavuzu bu vakayı YAKALAYAMAZ** — kılavuz `<status>` alanından başlıyor, burada `<status>` **hiç doğmuyor**.
> ⇒ **Kılavuza eklenmesi gereken adım:** `bildirim_yok ∧ süre > beklenen` ⇒ **transkriptin `mtime`'ını ∧ satır sayısını ÖRNEKLE**, bildirimi bekleme.

**⭐ Ve teşhis dürtme sonrası DEĞİŞTİ:** `SendMessage` gönderildi ⇒ üçü de **29-34 saniyede tam raporla** döndü ∧ **`tool_uses = 0`**.
Üçüncüsünün ilk cümlesi: *"Donmuş değilim — önceki turda tam sonucu ürettim ve döndürdüm."*
⇒ **`hesaplama = BİTMİŞTİ (15:11)`** ∧ **`teslim = OLMADI`**
⇒ **Bu bir HESAPLAMA asılması DEĞİL, bir TESLİM arızasıdır.** İş 45 dakika boyunca **diskte hazır bekledi**, ebeveyn beklemeye devam etti.

| Kayıp modu | İş durumu | Sürdürmenin işlevi | Maliyet |
|---|---|---|---|
| Hesaplama asılması | **yapılmamış** | onu **yaptırır** | tam koşum |
| **Teslim arızası** | **yapılmış** | onu yalnız **taşır** | **~30 saniye** |

⇒ **Pratik kural: `süre > beklenen` ⇒ önce DÜRT, sonra endişelen.** Maliyet 30 saniye; alternatif 45 dakika boş bekleme.

**Bu vakanın kendi dersi:** `bildirim_yokluğu ≢ çalışıyor`. Bekleme uzadıkça *"hâlâ çalışıyor"* varsayımı güçleniyordu ∧ **yanlıştı**. Bu, P73'ün (*"kaynak tükendi ≡ iş bitti"*) **kardeşidir**.

**Kurtarma kaydı:** `ara_metin` üçünde de **mevcuttu** ⇒ kesilme anında iş diskteydi, `kayıp = 0` ⇒ **V69 ("iskelet-önce") üçüncü kez karşılığını verdi.**

---

## 4 — Teşhis kılavuzu (uygulanabilir, bugün)

**Adım 0 — Hangi dünyadasın?** `claude agents` satırı → arka plan oturumu. `Agent`/`Task` ile açtığın → **alt-ajan**, `claude agents`'ta asla görünmez.

**⛔ Adım 0.5 — BİLDİRİM HİÇ GELMEDİ Mİ?** *(§3.1'den eklendi — kılavuzun eski hâli bu vakayı kaçırıyordu.)*
`bildirim_yok ∧ süre > beklenen` ⇒ **bildirimi bekleme.** Transkriptin `mtime`'ını ∧ satır sayısını **iki kez örnekle** (45 sn arayla). `büyüme = 0` ise ajan **sessizce ölmüş** olabilir ⇒ doğrudan `SendMessage` gönder. Maliyet ~30 saniye; alternatif saatlerce boş bekleme. **Bildirim yokluğu, çalıştığı anlamına gelmez.**

**Adım 1 — Ebeveyn transkriptinde bildirimin `<status>`'una bak.**
- `completed` → iş bitti, `<result>` gerçek rapordur. Dur.
- `stopped` → **insan veya dış süreç öldürdü.** Sistem değil. Kasıtlıydı.
- `failed` → **DUR, terminal sanma.** Adım 2.

**Adım 2 — Transkriptin SON KAYDINA bak** (en keskin ayırt edici — *"tek"* değil, bkz. K18):

| Gördüğün | Anlamı | Yapılacak |
|---|---|---|
| `isApiErrorMessage: true` + `stop_reason: "stop_sequence"` | **API ölümü.** Metin `You've hit your session limit` → kota; `Request rejected (429)` → hız limiti; `Server is temporarily limiting` → geçici kısıtlama | Adım 3, sonra limit kalkınca **resume et, sıfırdan başlatma**. Opus limitiyse `/model` ile geç |
| `stop_reason: "tool_use"` + metin bloğu yok | **Araç çağrısının ORTASINDA öldü** — abort/stall/süreç ölümü | ~~Stall watchdog aşılmış olabilir; uzun `Bash`/`WebFetch` varsa eşiği yükselt~~ **[K] 2026-07-30 ana-sıra:** bayat satır — §14 C2 hükmüyle çelişiyordu (nöbetçi bu sürümde YOK, eşik diye bir şey yok); kaynak `cc/rapor-2026-07-29-4.md` §6.2 Ç-c |
| Son kayıt `type: "user"` (tool_result) | Araç döndükten hemen sonra öldü — süreç/bağlantı kaybı | Resume dene |
| Normal metin, hata yok, ama bildirim `failed` | **Ajan bildirimden SONRA devam edip bitirmiş** (§2) | **Transkripti oku — rapor orada.** Bildirime güvenme |
| `Task "<desc>" (<id>) was stopped by the user.` (isMeta) | **Kullanıcı iptali.** Dahili `killed` → gösterimde `stopped` | Kasıtlıydı. **Ayırt edici işaret:** bu mesajda "TaskOutput ile kontrol et" cümlesi HİÇ geçmez |

**115 transkriptte son-kayıt imza dağılımı [D-ölçüm]:**

| İmza | Sayı | Anlam |
|---|---|---|
| Normal metin, `stop_reason: null` | 72 | Normal bitiş |
| **`isApiErrorMessage: true` + `stop_sequence`** | **17** | **API hatası ölümü** |
| Normal metin, `stop_reason: "end_turn"` | 13 | Normal bitiş |
| `stop_reason: "tool_use"`, metin yok | 6 | Araç ortasında öldü |
| Boş son metin | 4 | Belirsiz kesinti |
| Son kayıt `type: "user"` | 3 | Araç sonrası öldü |

> **[K18 · antitez daraltması]** Eşleşmenin kendisi **kaynak kodda doğrulandı ⇒ `⊨D`**: `kjq()` sabit-kodlu `stop_reason:"stop_sequence"` üretiyor ∧ `CY()` `isApiErrorMessage:!0` basıyor. **Ama "tek" süperlatifi doğrulanamadı** — `isApiErrorMessage` alanı başka bağlamlarda da kullanılıyor. İmza **geçerli**, tekelliği **düştü**.

**Adım 3 — Kısmi işi kurtar. Bildirimin `<result>`'ına GÜVENME.**

**[X] Dokümanın "partial work isn't lost" ifadesi, dosya seviyesinde doğru — bağlam seviyesinde yanıltıcı.** "Last output" pratikte **son assistant metin bloğuna indirgenir**; bir araştırma ajanında bu, araç çağrısından önceki tek cümlelik ara-nottur.

> **[H16 · antitez daraltması]** *"Ebeveyne **yalnız** son assistant metin bloğu geçer"* formülasyonu **abartılı-dar**. Aktarılan şey **biriken kısmi çıktı + hata notudur**, tek bir blok değil. Bulgunun özü (**ebeveyne giden şey gerçek raporun kendisi değildir**) ayakta; *"tek blok"* mekanizma tarifi düzeltiliyor. Ölçülen uzunluklar bu düzeltmeden **etkilenmiyor** — 0-160 karakter zaten ölçümdür. Ölçülen `<result>` uzunlukları: **0, 71, 137, 147, 160 karakter.** İçerikleri:
- *"Line 3 is in. Waiting on the other three."*
- *"Proxy blocks direct curl to .gov/eur-lex. Let me dispatch parallel research lines..."*

→ Ebeveyne **~100 karakterlik gürültü** gidiyor; onlarca dakikalık birikmiş araştırma **transkriptte kalıyor**. Bir vakada `<result>` tamamen boştu.

**Kurtarma:** `output_file` zaten transkripte **symlink**'tir. Tümünü okuma (bağlam taşar); yalnız >500 karakterlik assistant metin bloklarını çek — bu eşik ara-notları eleyip gerçek rapor bloklarını bırakır.

---

## 5 — %22'lik kaybın mekanizması

**[D]** v2.1.199'dan itibaren: API hatasıyla biten alt-ajan,
- **metin üretmişse** → kısmi çıktı + "kesildi" notu döner
- **hiçbir şey üretmemişse VEYA yalnız araç çağrısı yapmışsa** → `Agent terminated early due to an API error` ile **tamamen başarısız olur**

**▲ "Sadece araç çağrısı" şekli tam olarak bir araştırma ajanının profilidir** (20 WebFetch, sonra tek rapor). Ölçülen 17 API ölümü + 6 araç-ortası ölüm bu imzayı taşıyor.

→ **Bu, %22'lik kaybın en olası tek mekanizmasıdır.** İş teorik olarak kurtarılabilir (transkript diskte), ama **varsayılan akışta kurtarılmaz.** Çelişki değil, boşluk.

**Damga [?]:** A27 bunu **hipotez** olarak işaretledi, ölçüm olarak değil. Doğrulama yolu somut ve bende var: son kayıt tipi `tool_use` mu `text` mi — §4'teki tablo tam olarak bunu ölçüyor. **6 vaka `tool_use` ile öldü** → mekanizma teyitli, ama payı (6/115 = %5) hipotezin öngördüğünden düşük. Yani mekanizma gerçek, **ağırlığı abartılmış**.

---

## 6 — Kota mimarisi: 16 ayrı limit

**[D]** Sistemde **on altı** ayrı limit var ve çoğu birbirinden bağımsız:

| # | Limit | Pencere | Nasıl görülür |
|---|---|---|---|
| 1 | **Oturum limiti** (abonelik) — tüm modeller ortak, chat+Cowork paylaşımlı | **Yuvarlanan 5 saat** | `rate_limits.five_hour.used_percentage` + `resets_at` (epoch) |
| 2 | **Haftalık limit** — oturum limitiyle **eşzamanlı** işler | 7 gün | `rate_limits.seven_day` |
| 3 | **Opus limiti** — yalnız Opus istekleri | Oturumla aynı | `/model` ile Sonnet'e geç → **çalışma durmaz** |
| 4 | RPM / ITPM / OTPM (API) — model sınıfı başına ayrı | **Token bucket, sürekli dolum** | 429 + `anthropic-ratelimit-*` |
| 5 | **Acceleration limit** — ani artışa karşı | Belgelenmemiş | Sebebi ayırt edilemeyen 429 |
| 6 | **WebSearch oturum bütçesi** | **Oturum boyu, pencere yok** | **GÖRÜNMEZ** — §7 |
| 7 | Web-search org hız limiti | Belgelenmemiş | Batch'te otomatik throttle |
| 8 | **Eşzamanlı araç/alt-ajan** | Anlık | `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY` = **10** |
| 9 | Eşzamanlı alt-ajan | Anlık | `..._MAX_CONCURRENT_SUBAGENTS` = 20 |
| 10 | **Oturum-toplamı alt-ajan** | Oturum boyu | `..._MAX_SUBAGENTS_PER_SESSION` = **200**, `/clear` sıfırlar |
| 11 | Alt-ajan derinliği | — | `..._MAX_SUBAGENT_SPAWN_DEPTH` = **1** (varsayılanda alt-ajan alt-ajan doğuramaz) |
| 12 | Fast mode | Ayrı havuz | Abonelikte yalnız usage credits |
| 13 | Aylık harcama tavanı (API) | Takvim ayı | Start $500 / Build $1.000 / Scale $200.000 |
| 14 | Bağlam / auto-compact | — | **Limit değil**, modelin max input'u |
| 15 | Batch limitleri | 24 saat | **Senkron kotayı etkilemez** + %50 indirim |
| 16 | **529 Overloaded** | — | **Kotanıza SAYILMAZ** |

**▲ Pencere mekaniği yanlış anlaşılıyor [D]:** API tarafı **token bucket**'tır — *"capacity is continuously replenished up to your maximum limit, rather than being reset at fixed intervals."* Dolayısıyla `reset` başlıkları "sıfırlanma anı" değil **"tam dolum anı"**dır. → **Reset'i beklemek gerekmez, kısmi kapasite daha önce açılır.**
Abonelik tarafı ise **yuvarlanan pencere + ilan edilmiş reset anı**. **İkisi farklı mekanizma; birinden çıkarılan sezgi diğerinde yanlıştır.**

**▲ [X] Çelişki, kayda geçiyor:** A25, `claude_code.api_retries_exhausted` telemetri olayının **var olmadığını** buldu (kurulu `cli.js` v2.1.42'de grep boş + WebFetch özeti "yok" dedi). A26, aynı olayın **var olduğunu** buldu — `total_attempts` ve `total_retry_duration_ms` nitelikleriyle birlikte, **ham markdown'dan** (`.md` son ekiyle doğrudan çekim).
**Hüküm: A26 haklı.** İki bağımsız gerekçe: (a) ham markdown, WebFetch özetinden üstündür — A26 bunu ayrıca kendi yöntem notunda yakaladı (*"WebFetch özeti alanı 'yok' dedi, ham markdown var olduğunu gösterdi"*); (b) kurulu ikili **v2.1.42**, dokümanlar **~v2.1.217** — sürüm farkı grep'in boş dönmesini zaten açıklıyor. A25'in ölçümü kendi bağlamında doğru, **genellemesi yanlış**.
→ **Kural olarak kaydediliyor:** `code.claude.com` / `platform.claude.com` için **daima `.md` son ekiyle doğrudan çek**, WebFetch özetine güvenme. Bu ailedeki tüm sayısal iddialar bu yolla alındı.

---

## 7 — ▲ Sessiz bozulma: WebSearch bütçesi

Bu, bu ailenin **en yüksek getirili tek bulgusu** ve oturumda gözlenen "bulunamadı" raporlarının gerçek açıklaması.

**[D]** *"A session can make at most 200 WebSearch calls, counted across the main conversation and every subagent it spawns, so searches made by parallel research fan-outs count against the same limit."*

- Bu bir **hız limiti değil**, bir **oturum sayacıdır** — pencere yok, `/clear`'a kadar birikir
- **Ana konuşma + tüm alt-ajanlar aynı havuzdan yer**
- Ayarlanabilir: `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`, varsayılan **200**, tavansız, ama **kapatılamaz**

**▲ Ve tükendiğinde HATA DÖNMEZ:** *"You don't see the notice: a capped call appears in the conversation as a search that did nothing."*

→ **Bu, bir dalganın sessizce boş dönebileceği ve bunun fark edilmeyeceği anlamına gelir.** Oturumda A8, A12 ve A18'in alt-hatlarının "bulunamadı" demesinin sebebi büyük olasılıkla budur — **doğru cevap "aranamadı"ydı.**

**Aritmetik:** 112 alt-ajan × ajan başına 2 arama = **224 > 200**. Zarf zaten aşılmıştı.

**Çözüm, ölçülmüş:** görev emrinde **URL verilirse ajan WebSearch değil WebFetch kullanır** ve bütçeden hiç yemez. A26 ajanının kendisi bu araştırmayı **2 WebSearch ile** bitirdi, çünkü dokümanları doğrudan çekti.

---

## 8 — ▲ Paralel koşumun gizli maliyeti

**[D]** *"running ten agents in parallel uses quota roughly ten times as fast as running one."*

**Ama bu iyimser bir alt sınırdır.** İki mekanizma daha var:

1. **[D] Alt-ajan cache'i SIFIRDAN başlar — ama sıfırda kalmaz.** *"A subagent starts its own conversation with its own system prompt and tool set... It builds its own cache, **starting with no cache hits on its first call and warming up across its own turns**. **Subagents use the five-minute TTL even on a subscription**, since the automatic one-hour TTL applies to the main conversation."*
2. **[D] Cache okumaları ITPM'e sayılmaz, ama cache OLUŞTURMA sayılır.** N alt-ajan = N ayrı cache oluşturma.

→ **10 paralel KISA ÖMÜRLÜ ajan, tek ajanın 10 katından DAHA FAZLA ITPM baskısı yapar.**
→ **Pratik sonuç: uzun ömürlü az sayıda ajan > kısa ömürlü çok sayıda ajan.** Aynı iş 30 ajan yerine 10 ajana bölünürse **20 cache-oluşturma turu tasarruf edilir.**

> **[K12 · antitez ÇÜRÜTMESİ — ⭐ yüksek]** Bu maddenin eski hâli *"Alt-ajanlar prompt cache'ten yararlanamaz"* diyordu ⇒ **fazla güçlü ∧ yanlış**. Doğrusu: `ilk_çağrı → isabet = 0` ∧ `sonraki turlar → KENDİ cache'ini ısıtır` ∧ `TTL = 5 dk` (ana konuşmanın 1 saati yerine).
> ⇒ *"10 ajan = 10× alt sınır"* çıkarımı **yalnız kısa ömürlü ajanlar için** ayakta kalır.
> ⇒ **Ve bu düzeltme §8'in tavsiyesini zayıflatmıyor, GÜÇLENDİRİYOR:** uzun ömürlü ajan kendi önbelleğini ısıttığı için *"az sayıda uzun ömürlü > çok sayıda kısa ömürlü"* tercihinin **mekanizması artık nettir** — eskiden yalnız *"cache yok"* deniyordu, şimdi *"cache var ama ısınması zaman ister"* deniyor.

**Eşzamanlılık — ÜÇ AYRI MEKANİZMA, birleştirilmez:**

| Mekanizma | Değer | Ne yapar |
|---|---|---|
| `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | **20** | Belgelenmiş **alt-ajan eşzamanlılık sınırı** |
| `MAX_TOOL_USE_CONCURRENCY` | **10** | Paralel **araç + alt-ajan yürütme kapısı** — ayrı mekanizma |
| *"10 oturum ≈ 10× kota"* (`agent-view.md`) | — | **Kota tüketim kuralı, sert sınır DEĞİL** |

> **[K13 · antitez ÇÜRÜTMESİ — ⭐ yüksek]** Eski hâli bu **üç sayıyı tek bir "bağlayıcı sınır 10" hükmüne** birleştirmişti. Antitez `sub-agents.md` ∧ `env-vars.md` ∧ `agent-view.md`'yi ayrı ayrı okudu ⇒ **üçü farklı şeydir**.
> ⇒ **§9'un dalga zarfı (10 ajan) hâlâ savunulabilir** — ama gerekçesi *"sert sınır 10'dur"* **değil**, `yürütme kapısı ⊕ kota tüketimi`. **Sayı korunur, gerekçe düzelir.**

---

## 9 — Paralel koşum bütçe kuralı

Gözlenen tabloyu (112 alt-ajan · 17 API ölümü · WebSearch defalarca tükendi) dokümante mekanizmalara oturtunca:

1. **Dalga genişliği ≤ 10, sabit.** *(Gerekçe K13 ile düzeltildi:)* belgelenmiş alt-ajan eşzamanlılık sınırı **20**'dir; **10** ise paralel **yürütme kapısıdır**; *"10 oturum ≈ 10× kota"* ise ayrı bir **tüketim** kuralıdır. Zarfın 10'da tutulmasının sebebi **sert bir sınır değil**, yürütme kapısı + kota tüketiminin bileşimidir. Üstü paralellik satın almaz — yalnız kuyrukta bekler, ama oturum-toplamı sayacını (200) ve WebSearch bütçesini (200) tüketir. **112 ajanlık koşum, 200'lük tavanın yarısını tek koşumda harcadı.**
2. **WebSearch'ü ajan başına tayınla.** `N_ajan × arama_başına ≤ 200`. Daha iyisi: **emirde URL ver → WebFetch kullanılır → bütçeden yemez.** Dalga sonunda sayacı kontrol et (sessiz tükeniyor).
3. **Model: işçi Sonnet, sentez Opus, tarama Haiku.** **Opus 5'in ayrı ITPM kovası var** → işçiler Sonnet'e alınırsa işçi trafiği Opus kovasından **hiç yemez**. Aynı kotayla iki paralel havuz. *(V59 tam olarak bunu söylüyordu — artık mekanizması da elimizde.)*
4. **Effort'u ajan-başına düşür.** Varsayılan **`high`**; düşünme token'ları **çıktı olarak** faturalanır. Getirme/tarama ajanlarına `effort: low|medium`, sentez ajanı `high`. **112 ajanlık koşumda tek başına en büyük token kalemi budur.**
5. **Cache'i alt-ajandan bekleme** (§8) — az sayıda uzun ömürlü ajan tercih et.
6. **Dalgaları kademeli başlat.** Acceleration limit'in tek reçetesi bu; 10 ajanı aynı saniyede açmak ortalama düşük olsa bile **burst-429** tetikler. 2-3 saniye ara yeter.
7. **Sonlanmayı hataya çevir, sessiz bırakma** — v2.1.199+ zaten yapıyor; denetim için `query_source="subagent"` kırılımı var.
8. **Watchdog'u bilerek aç.** `CLAUDE_CODE_RETRY_WATCHDOG=1`, cevapta reset zamanı varsa **kör backoff yerine pencerenin bitişini bekler** → 5 saatlik limite çarpan ajan **saatlerce asılı kalabilir**. Kural: **yalnız gözetimsiz koşumda**; interaktif dalgada hızlı başarısızlık + yeniden dalga daha ucuz.
9. **Sert tavan koy.** Print-mode'da `--max-budget-usd` — alt-ajan harcaması tavana sayılır, tavan dolunca background ajanlar durdurulur.

> **Zarf:** dalga = **10 ajan · Sonnet · effort medium · 2-3 sn aralı başlatma · ajan başına ≤2 WebSearch (tercihen 0 + URL) · toplam oturum ≤ 60-80 ajan · sert bütçe tavanı · gözetimsizde watchdog açık.**

**▲ Kendi payıma düşen hüküm:** gözlenen 112 ajanlık koşum bu zarfın **dışındaydı**. %22'lik limit-kaynaklı sonlanma **anomali değil, beklenen sonuçtur**. Sorun ajanlarda değil, **onları nasıl koştuğumdaydı** — belgelenmiş uyarılara rağmen aynı anda 4-5 aile açtım, her biri kendi alt-hatlarını doğurdu. Bu, ana atlastaki L1 dersinin ("ölç, sonra teorileştir") ikinci vakası: **teoriyi ölçümden önce kurdum.**

---

## 10 — Sürdürme: kurtarma mekanizmaları

**[D] Kesilen bir alt-ajanın işi kurtarılabilir.** Alt-ajan transkriptleri ana konuşmadan **bağımsız** dosyalarda tutuluyor ve üç garanti var:
- Ana konuşma compact olduğunda alt-ajan transkriptleri **etkilenmez**
- "Claude Code'u yeniden başlattıktan sonra aynı oturumu sürdürerek bir alt-ajanı sürdürebilirsiniz"
- Temizlik `cleanupPeriodDays` ile, varsayılan **30 gün**

**[D] Sürdürme aracı `SendMessage`:** *"Sürdürülen alt-ajanlar, önceki tüm tool çağrıları, sonuçları ve akıl yürütmesi dahil tam konuşma geçmişini korur."* Tamamlanmış bir alt-ajan `SendMessage` alınca **yeni `Agent` çağrısı olmadan** arka planda otomatik sürdürülür. **Ve [D]: sürdürme, eşzamanlılık limitini kontrol etmeden taze slot alır** — kurtarma yolu kapasite kapısından muaf.

**▲ İki istisna — biri ASKIDA, biri [D]:**
1. **`[?]` ASKIDA — kural olarak KULLANILMAZ:** *"Yerleşik `Explore` ve `Plan` ajanları tek-atışlıktır, agent ID döndürmezler → sürdürülemezler."*
2. **[D] Kullanıcının kendi durdurduğu ajan otomatik sürdürülmez**; `SendMessage` "ajan iptal edildi" reddiyle döner. Çözüm: alt-ajan panelindeki transkripte yazmak bu bayrağı temizler.

> **[K14 · antitez — ⭐⭐ KRİTİK, dayanak BULUNAMADI]** Antitez `sub-agents.md`'yi okudu: **Explore/Plan için sürdürülemezlik istisnasına dair hiçbir kayıt yok.** Bu ajanlar için tutulan tek istisna, CLAUDE.md ∧ git-status'u **yüklememeleridir**.
> ⇒ Bu iddia bir alt-ajanın (A27) aktarımıydı ∧ **doğrulanmadan** U1 olarak öne çıkarıldı.
> ⇒ **Doğrulanana kadar *"Explore/Plan kullanma"* diye bir kural ÇIKARILMAZ.** İddia yanlış olduğu için değil, **dayanağı gösterilemediği için** askıdadır — doğru da çıkabilir, ama şu an kanıt yok.
> ⇒ Doğrulama yolu ucuz ∧ elde: bir `Explore` ajanı açıp dönen nesnede `agent_ID` var mı diye bakmak yeter. **Bu, sonraki turun ilk işlerinden biri olmalı.**

**[D] `/rewind` checkpointing iş dayanıklılığı için DEĞİL, kod içindir.** Sınırları sert: **bash ile değiştirilen dosyalar izlenmez**, **alt-ajanların yaptığı düzenlemeler geri alınmaz** ("bunları geri almak için git kullanın"). Dokümanın kendi ifadesi: *"checkpoint'leri 'yerel geri al', Git'i 'kalıcı tarihçe' olarak düşünün."*
→ **JARVIS'in "her karar bir commit" kuralı (m.10) bu boşluğu zaten kapatıyor.** Kayda değer: kanonumuz bu noktada dokümandan önce doğruydu.

**▲ [D] Anthropic'in kendi tavsiyesi transkript kurtarmaya karşı:** *"Oturum sürdürmeye güvenme. İhtiyacın olan sonuçları (analiz çıktısı, kararlar, dosya diff'leri) uygulama durumu olarak yakala ve taze bir oturumun promptuna geçir. Bu, transkript dosyalarını ortalıkta taşımaktan çoğu zaman daha sağlamdır."*
→ Yani: **artımlı dosya > transkript kurtarma.** Bu, Salih'in "veri kaybı istemiyorum" talimatının teknik karşılığıdır — ve bu oturumda raporları koşum bitmeden diske yazıp commit'lemenin gerekçesi.

---

## 11 — Uygulanabilir desenler (değer yargılı)

### Bugün, sıfır altyapı

| # | Desen | Değer |
|---|---|---|
| **U1** | ⛔ **ASKIDA `[?]` — tavsiye olarak KULLANILMAZ.** *"`Explore`/`Plan` yerine `general-purpose` kullan, ilk ikisi sürdürülemez."* Öncülün dokümanda dayanağı **bulunamadı** (K14). Doğrulanmadan kural çıkarılmayacak; doğrulama yolu §10'da | **ASKIDA** — eski değer etiketi (*"ÇOK YÜKSEK, maliyet sıfır"*) **geri çekildi**. Bu etiket, doğrulanmamış bir maddeyi listenin başına taşıyan şeydi (M5) |
| **U2** | **Ajan promptuna "önce iskelet, sonra doldur"**: ilk bulguyu bulur bulmaz **kısa ara metin** üret (araç çağrısı değil, metin). Sebep §5: metin varsa kısmi çıktı döner, **sadece araç çağrısı varsa her şey kaybolur** | **ÇOK YÜKSEK** — en yüksek kazanç/maliyet oranı. Yeni araç yok, yeni dosya yok |
| **U3** | **Uzun araştırma ajanlarını arka plana al** — arka planda son çıktı ebeveyne dahil edilir, ön planda tool-şekilliyse hepsi kaybolur | **YÜKSEK** |
| **U4** | Tekrar eden ajanlara **`memory: project`** — `.claude/agent-memory/` git'le versiyonlanır; **artımlı yazmanın kanona uygun biçimi** (rapor-dosyası yasağını ihlal etmez) | **YÜKSEK** — ama yalnız tekrar eden ajanlar için |
| **U5** | Script'li koşumda **`--session-id <UUID>`** — kurtarma anahtarını işten **önce** elinde tut | **YÜKSEK** — maliyet sıfır |
| **U6** | **`git commit` = tek gerçek checkpoint** (§10) | **YÜKSEK** — JARVIS'te zaten kurulu |
| **U7** | **Kesilen ajanı `SendMessage` ile sürdür**, yeniden başlatma | **YÜKSEK** — değeri tamamen "biliyor olmakta" |

### Yakın vade (bir oturumluk kurulum)

| # | Desen | Değer |
|---|---|---|
| **U8** | `SessionEnd` hook'u ile transkript arşivi — 30 günlük pencereyi aşan kayıt katmanı | **ORTA** — 30 gün zaten uzun |
| **U9** | **İşi Continue-As-New mantığıyla parçala**: tek dev ajan yerine, öncekinin özet durumunu girdi alan 2-3 ajanlık zincir | **ORTA-YÜKSEK** — ama **granülarite bedava değil**, her yeni ajan bağlamı yeniden kurar |
| **U10** | Idempotency key ile yeniden-çalıştırma güvenliği (`<run-id>-<adım-id>`) | **ORTA** — yalnız push/publish sınırında |
| **U11** | **At-least-once'ı kabul et, exactly-once'ı kovalama** — her adımı tekrar-güvenli yap, tekrarı engellemeye çalışma | **YÜKSEK — ama kural değil, zihniyet** |

### ▲ Aşırı — tek kişilik sistemde YAPMA

| # | Desen | Neden hayır |
|---|---|---|
| **U12** | **Temporal/Restate/DBOS kurmak** | Service + persistence store + Worker filosu ister; determinizm kısıtları **tüm iş akışı kodunu yeniden yazdırır**. Çözdüğü problem "binlerce eşzamanlı workflow, çoklu makine, çoklu takım". **Kavramları al, çalışan sistemi alma.** *Bu araştırmanın en net yargısı budur.* |
| **U13** | Kendi WAL / event-sourcing katmanını yazmak | LLM çağrısı deterministik değildir — replay aynı sonucu vermez. **Git zaten append-only log'un.** |
| **U14** | Saga/telafi altyapısı | Tek kişilik repoda geri alma = `git revert`. **Kavram olarak öğren, sistem olarak kurma.** Tek istisna: `git push` sınırının ötesi (yayınlama) |
| **U15** | `/loop` ile limit-sonrası otomatik retry | Kaçırılan tetiklemeler telafi edilmez, 7 günde ölür, oturum açık+boşta olmalı. **Limit-sonrası kurtarma için tasarlanmamış.** Ayrıca kontrolsüz retry döngüsü **zararın kendisidir** — burada zarar = haftalık kotanın sessizce yenmesi |

---

## 12 — Öğrenme sırası (L16–L22)

*Salih'in "ne öğrenmem lazım" sorusunun cevabı. Sıra **ön koşul zinciri**dir: her kavram bir öncekinin çözemediği problemi çözer. Kaynakların hepsi bu koşumda **birincil kaynaktan doğrulandı** ve **ücretsiz + web erişimli**.*

**▲ Erişim taktiği kaydı:** Bu ailede kapalı siteler (`postgresql.org`, `kafka.apache.org`, `sqlite.org`) **kaynak depolarından** okundu ve bu, kanıt kalitesini **düşürmedi — yükseltti**. PostgreSQL WAL dokümanı `postgres/postgres` içindeki `wal.sgml`'den, Kafka teslim semantiği `apache/kafka` içindeki `docs/design/design.md`'den alındı. V64 (§tech-stack §9) burada ikinci kez doğrulandı.

| # | Katman | Ne çözer | Ajan karşılığı | Kaynak |
|---|---|---|---|---|
| **L16** | **Teslim garantileri** — at-most-once / at-least-once / exactly-once (ön koşul: yok) | "İş tekrarlanabilir mi, kaybolabilir mi?" sorusunu **yanıtlanabilir** kılar. Diğer her kavramın çerçevesi | Kesilen ajanı yeniden çalıştırmak = at-least-once seçmek. Çalıştırmamak = at-most-once | Kafka `design.md`, "Message Delivery Semantics" — **~15 dk** |
| **L17** | **Idempotency + idempotency key** (ön koşul: L16) | At-least-once'ı **yaşanabilir** kılan tek şey. Tekrar zararsızsa tekrardan korkmazsın | Ajanı iki kez koşturmak sistemi bozmuyorsa, kesilme **felaket değil gecikmedir** | Temporal `activity-definition.mdx` — **~10 dk** |
| **L18** | **Write-ahead log + checkpoint** (ön koşul: L17) | WAL kalıcılığı **ucuz** yapar (sıralı append), checkpoint kurtarmayı **kısa** yapar | "Her bulguyu bulunca yaz" = **WAL**. "Bölüm bitti, özet çıkar" = **checkpoint**. İkisi farklı şeydir; karıştıranlar ya çok yazar ya hiç yazmaz | PostgreSQL `wal.sgml` — **~20 dk** |
| **L19** | **Retry politikaları, timeout, heartbeat** (ön koşul: L17-L18) | Ne zaman tekrar denenir, kaç kez; ve "hâlâ çalışıyor mu yoksa öldü mü?" | **Heartbeat = ilerleme yükü taşıyan kalp atışı.** Ajanın periyodik ara-durum bildirmesi aynen bu | Temporal `detecting-activity-failures.mdx` + **Celery `faq.rst`** ("otomatik retry ne zaman zararlı" — nadir birincil metin) |
| **L20** | **Durable execution: event history + replay + determinizm** (ön koşul: L16-L19) | Öncekileri tek programlama modelinde birleştirir | **Kesin ayrım çizgisi: LLM çağrısı = Activity** (kaydedilir, replay edilmez), **akış kontrolü = Workflow** (deterministik, replay edilir). Ajan iş akışı tasarımının omurgası | Temporal `understanding-temporal.mdx` → `workflow-definition.mdx` (**alanın en yoğun tek sayfası**) → Go **ve** TypeScript basics (aynı problemin iki farklı çözümü — fark öğretici) |
| **L21** | **Continue-As-New → Saga** (ön koşul: L20) | L21a: sonsuz-uzun işin geçmişi nasıl sınırlanır. L21b: geri alınamaz adımlar nasıl geri alınır | L21a = "tek dev ajan yerine zincir" (U9). L21b = **yalnız publish/push sınırında** geçerli | Temporal `continue-as-new.mdx` + `saga-pattern.mdx` |
| **L22** | **Claude Code'un kendi dayanıklılık yüzeyi** (paralel okunabilir) | Kavramların bu sistemdeki karşılıkları | §4 teşhis kılavuzunun dayanağı | `sessions` → `sub-agents` → `agent-sdk/sessions` → `checkpointing` → `errors` → `costs` — **~90 dk** |

**▲ Sıranın en önemli atlaması L20'dir.** Determinizm kısıtı, L16-L19 anlaşılmadan **keyfi** görünür; anlaşıldıktan sonra **kaçınılmaz** görünür.

**▲ Bir öncül düzeltmesi [X]:** "`Date.now()` / `random()` durable execution'da yasaktır" **yanlıştır**. TypeScript SDK'da bunlar **deterministik sürümleriyle değiştirilir** ve doğrudan kullanılabilir; Go SDK'da API ikamesi gerekir (`workflow.Now()`). Ayrıca **Side Effect** kaçış kapağı var: non-determinizm **yasaklanmıyor, kaydediliyor**. Doğru genel ilke: **yasak olan `random()` değil, kayıt-dışı non-determinizm.**

**Kitap katmanı — dürüst uyarı:** *Designing Data-Intensive Applications* (Kleppmann) bu alanın standart tek-cilt referansıdır, **ama ücretli** ve bu koşumda içeriği doğrulanamadı. Bölüm eşlemesi verilirse kestirim olur → **[?]**. Sıra: L16-L21'i ücretsiz birincil kaynaklardan bitirdikten **sonra**; kitap **sentezdir, giriş değildir**.

---

## 13 — İddia listeleri — **ANTİTEZ KOŞTU, hükümler işlendi**

*Bu bölümün başlığı `⊨¬2` (antitez koşulmadı) idi. **Artık değil:** antitez 2026-07-26'da araçlı olarak koştu (`tool_uses = 48`, ham doküman + kurulu `cli.js`). Her iddianın yanına çıkan hüküm yazıldı.*

**A25:** ① Stopped insan/dış müdahaleyle girilir; limit ve stall **Failed** üretir — **DARALDI (K15):** makine kapanması istisnası + oturum/task durumu ayrımı. ② `claude agents` alt-ajanları ayrı satır göstermez — **DARALDI (K16):** *"hiç"* yanlış, agent view kapalıysa listeler. ③ Agent view iki ortogonal ekseni tek satırda gösterir; `∙` sonlanma değildir — **⊨S ⊨D**, antitezin ifadesiyle *"tam isabet"*, doküman ikisini ayrı tablolarda listeliyor. ④ `is_error` limit-ölümlerini filtrelemez — **⛔ ÇÜRÜTÜLDÜ (K11) ⇒ ⊨X**; pratik tavsiye (`subtype`'a bak) korunur. ⑤ Hata subtype'lı mesajda `result` alanı yoktur — **DARALDI (K17):** TS'de yok, Python'da var ∧ `None`. ⑥ `isApiErrorMessage: true` + sentetik `stop_reason` **tek** keskin ayırt edicidir — **DARALDI (K18):** eşleşme ⊨D, *"tek"* düşer. ⑦ `failed` terminal değildir — **çürütülemedi**. ⑧ "Partial work isn't lost" bağlam seviyesinde yanıltıcıdır — **DARALDI (H16):** *"yalnız son blok"* abartılı-dar. ⑨ *(A26 tarafından çürütüldü — §6)*

**A26:** ① Bağlayıcı paralellik sınırı 10'dur — **⛔ ÇÜRÜTÜLDÜ (K13):** üç ayrı mekanizma birleştirilmiş; zarf korunur, gerekçe düzelir. ② WebSearch bütçesi oturum sayacıdır ∧ **sessiz** tükenir — **⊨S ⊨D ⭐**, `tools-reference.md` birebir doğruladı. ③ Alt-ajanlar cache'ten yararlanamaz — **⛔ ÇÜRÜTÜLDÜ (K12):** ilk çağrıda isabet 0, sonra kendi cache'ini ısıtır. ④ "resets at X" **tam dolum** anıdır — **⊨S ⊨D**. ⑤ Abonelik penceresi ile API penceresi farklı mekanizmalardır — **⊨S ⊨D**. ⑥ İşçileri Sonnet'e almak ayrı ITPM kovası açar — **çürütülemedi**. ⑦ Watchdog bir **takastır** — **⊨S ⊨D**, `env-vars.md` birebir. ⑧ Batch senkron kotayı yemez + %50 ucuz — **çürütülemedi**. ⑨ `/usage` otoriter değildir — **çürütülemedi**.

**A27:** ① Kesilen alt-ajanın işi `SendMessage` ile sürdürülebilir — **⊨S ⊨D**, *"exactly where it stopped"*. ② Erken ∧ sık metin üretmek en ucuz dayanıklılık müdahalesidir — **çürütülemedi** *(mekanizma teyitli, ağırlığı ölçülmüş: 6/115 = %5)*. ③ **Explore/Plan sürdürülemez — ⛔ ASKIDA (K14): dokümanda dayanak BULUNAMADI.** ④ Tek kişilik sistemde Temporal aşırı-mühendisliktir — **çürütülemedi**. ⑤ Exactly-once ulaşılamazdır — **çürütülemedi**. ⑥ Yasak olan kayıt-dışı non-determinizmdir — **çürütülemedi**. ⑦ Checkpointing dayanıklılık için değildir; git tek gerçek kontrol noktasıdır — **⊨S ⊨D ⭐**, *"dokümanın kendi çerçevesi bu"*. ⑧ Anthropic artımlı dosyayı transkript kurtarmaya tercih eder — **çürütülemedi**.

**Test edilemeyenler:** API token-bucket iç mekaniği · ITPM kovalarının sayısal tahsisatı · Batch ayrıntıları ⇒ `platform.claude.com` **erişim listesinde değildi**, ne doğrulandı ne çürütüldü. Temporal/durable-execution teorisi ⇒ kapsam dışı, birincil kaynaklar kapalı. **Bunlar `bulunamadı` değil, `aranamadı`dır.**

---

## 14 — Açık borçlar

| # | Borç | Not |
|---|---|---|
| C1 | ~~Antitez (Aşama 2) bu aile için de koşulmadı~~ → **KAPANDI 2026-07-26** | Antitez araçlı koştu (`tool_uses = 48`); **4 gerçek hata buldu** (K11-K14) ∧ 5 daraltma üretti. Hükümler §13'e işlendi. Yeni borç: **K14'ün öncülünü doğrula** (bir `Explore` ajanı açıp `agent_ID` dönüyor mu bak) |
| C2 | ~~Sürüm çatalı: dokümandaki stall davranışı geçerli olmayabilir~~ → **KAPANDI 2026-07-26, OLUMSUZ YÖNDE** | **Asılma nöbetçisi bu sürümde YOK.** İki bağımsız ölçüm yakınsadı: ① antitez kurulu `cli.js`'te `watchdog`, `idleAgent`, `stuckDetection`, `hungTask`, `healthCheck` terimlerinin **hiçbirini** bulamadı; ② §3.1 canlı vakası — üç ajan **45 dk** sessiz kaldı ∧ belgelenmiş **10 dk**'lık eşiğe rağmen abort edilmediler. ⇒ *"geçerli olmayabilir"* değil, **geçerli değil**. **Hiçbir otomatik koruma yok**; asılma tespiti tamamen ebeveynin işi |
| C3 | **429 ölümünün canlı imzası gözlenmedi** | 115 transkriptte terminal API hatalarının **17/17'si oturum limitiydi**. 429'un `stop_reason` imzasının aynı olup olmadığı **ampirik doğrulanmadı** — aynı kod yolundan geçtikleri için aynı olması beklenir `[?]` |
| C4 | Pro/Max için **sayısal tahsisat hiçbir açık dokümanda yok** | Dokümanlar bilinçli olarak yalnız **pencere yapısını** yayımlıyor, **büyüklüğü** değil |
| C5 | `blocking_limit` ve `rapid_refill_breaker` **tanımsız** | SDK enum'unda yalnız **değer olarak** geçiyor; kota-koruma mekanizmaları oldukları **kestirimdir** `[?]` |
| C6 | Oturum penceresinin **token mi mesaj mı** ölçtüğü belgelenmemiş | `used_percentage` yüzde veriyor, payda tanımsız. Token-ağırlıklı olması kuvvetle muhtemel `[?]` |
| C7 | HTTP `Idempotency-Key` **IETF taslağına erişilemedi** | Kavram Temporal'dan [D] karşılandı; **standart başlık semantiği** (anahtar ömrü, çakışma, 409) doğrulanamadı → L17'de boşluk |
| C8 | Alt-ajan token'ının ana oturum token'ıyla **aynı katsayıyla** sayılıp sayılmadığı | "Aynı kotadan yer" belgeli, katsayı belirtilmemiş |

---

## 15 — Fikir kutusu adayları

- **V68 — `.md` doğrudan çekim kuralı.** §6'daki [X] çelişkisinin dersi: `code.claude.com` / `platform.claude.com` için **daima `.md` son ekiyle ham çekim**; WebFetch özeti alanları **sessizce düşürüyor**. İki bağımsız vakada doğrulandı (`api_retries_exhausted`, env-vars varsayılanları). Atlas brifinglerine standart madde.
- **V69 — "İskelet-önce" ajan protokolü.** U2: ajan ilk bulguyu bulur bulmaz kısa **metin** üretsin. Kayıp modunu "her şey gitti"den "kısmi döndü"ye çevirir, maliyeti sıfır. **Ajan görev şablonuna zorunlu madde adayı.**
- **V70 — Dalga zarfı sabiti.** §9'un reçetesi (10 ajan · Sonnet · effort medium · ≤2 WebSearch · 2-3 sn aralı) KILAVUZ'a sayısal kural olarak girmeye aday. **V59'un mekanizması artık elimizde** — "ucuz model" tavsiyesi, aslında "ayrı ITPM kovası açma" hamlesiymiş.
- **V71 — ⛔ GERİ ÇEKİLDİ (K14).** *"Sürdürülemez ajan yasağı: `Explore`/`Plan` uzun/pahalı işlerde kullanılmasın."* Dayanağın `[D]` olduğu iddiası **doğrulanamadı**; antitez dokümanda karşılığını bulamadı. **Aday olarak kutuya girmez** — önce öncül doğrulanır, sonra yeniden değerlendirilir.
- **V82 — Bildirim beklenmez, transkript büyümesi örneklenir.** (§3.1'den; numarayı hakemlik kaydı §9b veriyor.) Uzun koşumlarda `task_notification` beklemek **yanlış sinyaldir** — bildirim hiç gelmeyebilir. Bunun yerine transkriptin `mtime`'ı ∧ satır sayısı periyodik örneklenir. Ölçüm **iki `stat` çağrısıdır**, maliyeti sıfırdır.
- **Kural adayı (numarasız — Salih atar) — "Liste başı kanıt kapısı".** M5'ten türedi: `tavsiye_sırası = 1 ⇒ dayanağı BAĞIMSIZ doğrulanmış olmalı`. **Üç bağımsız vakası var:** K14 (Explore/Plan), K35 (eksen başına 4 kategori), K39 (yayımlama eşiği). Üçü de doğrulanmadan öne çıkarıldı, üçü de antitezde düştü. *(V numarası bilerek verilmedi — m.41: bu yüzey öneri üretir, kanon kilitlemez.)*

---

## 16 — Kapanış damgası

**Aile:** A25 · A26 · A27 — **antitez KOŞTU (2026-07-26, araçlı, `tool_uses = 48`)**
**Antitez sonucu:** ⛔ **4 gerçek hata** (K11 `is_error` ⇒ ⊨X · K12 cache · K13 eşzamanlılık · **K14 Explore/Plan ⇒ ASKIDA**) ∧ 5 daraltma (K15-K18, H16) ∧ 5 doküman-doğrulamalı `⊨S`.
**⚠️ `⊨S` okuma kuralı:** genel olarak `⊨S` = *"aynı-aile hakemi karşısında sağ kaldı"*, çünkü antitez ajanları tez ajanlarıyla aynı model ailesindendi. **Bu aile bu şerhten MUAFTIR** — kanıt modelin belleğinden değil, ham dokümandan ∧ kurulu koddan geldi.
**Kanıt tabanı:** **[D] ağırlıklı** — kurulu `cli.js` zod şemaları · 115 alt-ajan transkripti (kendi ölçümümüz) · ham doküman markdown'ı. Bu, oturumun en güçlü kanıt tabanıdır. **Ve buna rağmen 4 hata çıktı** — güçlü kanıt tabanı, hata yokluğu demek değildir.
**Çözülen çelişki:** `api_retries_exhausted` — A26 lehine (§6), gerekçe kayıtlı
**Düzeltilen kendi hükmüm:** A25'in "3'ten 2'si teslim edilmedi" sayısı — tam-oturum verisiyle **[X]**; mekanizma korunur, sayı düşer (§2)
**Salih'in sorusuna doğrudan cevap:** ajanların **"stopped" olmadı** — `failed` oldular, ve `failed` **terminal değildi**. Kök neden ajanlarda değil, **koşum zarfının aşılmasındaydı** (§9).
