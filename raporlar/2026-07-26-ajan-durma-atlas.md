# Ajanlar Neden Duruyor — sonlanma, kota, dayanıklılık

*Kayıt: 2026-07-26 · Carvis (CC, yan-oturum m.41) · Talep: "stopped olan ajanlarım neden duruyor bunu çözmek için ne yapabiliriz ne öğrenmem lazım araştır atlasları koş rapor çıkar"*

**Aileler:** A25 (sonlanma taksonomisi) · A26 (kota mimarisi) · A27 (dayanıklılık ve sürdürme)
**Kanıt rejimi:** Bu aile, oturumun **en yüksek kanıt değerli** ailesidir. Üç bağımsız birincil katman kullanıldı: **kurulu CLI kaynağı** (`cli.js` zod şemaları) · **canlı transkriptler** (115 alt-ajan, bu oturumun kendi verisi) · **ham doküman markdown'ı** (`.md` son ekiyle doğrudan çekim). Neredeyse tüm bulgular **[D]**.

---

## 0 — Önce düzeltme: sorunun öncülü yanlıştı

Salih "**stopped** olan ajanlarım neden duruyor" diye sordu. Ölçüm bunu düzeltiyor:

> **[D] `Stopped` durumuna YALNIZ üç yolla girilir:** `Ctrl+X` · `claude stop`/`claude kill` · sürecin dışarıdan öldürülmesi (`kill`).
> **Oturum limiti, hız limiti, max_turns, stall zaman aşımı — hepsi `Failed` üretir, `Stopped` DEĞİL.**

Ampirik teyit, bu oturumun kendi verisinden: **35 bildirim → 22 `completed`, 13 `failed`, 0 `stopped`.** Yani bu oturumda **hiçbir ajan "stopped" olmadı**; hepsi ya bitti ya `failed` oldu.

**Ve asıl bulgu şu:** `Stopped` aslında sistemin **en net tanımlı** durumudur (yalnız insan/dış müdahale). Belirsiz olan **`Failed`**'dır — limit, API hatası, stall ve araç hatası hepsi oraya yığılır. Kafa karışıklığının kaynağı Stopped değil, **Failed'ın aşırı yüklenmiş olması**.

**Bir kategori hatası daha [D]:** `claude agents` komutu **alt-ajanları hiç göstermez**. İki ayrı dünya var:
| | Arka plan oturumu | Alt-ajan (subagent) |
|---|---|---|
| Nerede görünür | `claude agents` | `/tasks`, @-mention |
| Durum dosyası | `~/.claude/jobs/<id>/state.json` | `~/.claude/projects/<slug>/<uuid>/subagents/agent-<id>.jsonl` |
| Bu makinede | **`~/.claude/jobs/` HİÇ YOK** | **115 transkript var** |

Bizim koştuğumuz her şey **alt-ajan**. `claude agents`'a bakarak onları aramak sonuçsuz kalır.

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
- SDK'da `is_error: false` görmek → limit-ölmediği anlamına **gelmez** (§3'e bak)

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

**▲ Yapısal fark:** hata şemasında **`result` alanı HİÇ YOK**. Ajan limite çarptığında metin çıktısı için ayrılmış alan tamamen kayboluyor.

**▲ TUZAK [D-kod]:** `error_max_turns` ve `error_max_budget_usd` için **`is_error = false`**. `cli.js`'te birebir: `subtype:"error_max_turns", ..., is_error:!1`. → **`is_error` ile limit-ölümlerini filtreleyen her kod bunları kaçırır.** Daima `subtype`'a bak.

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

---

## 4 — Teşhis kılavuzu (uygulanabilir, bugün)

**Adım 0 — Hangi dünyadasın?** `claude agents` satırı → arka plan oturumu. `Agent`/`Task` ile açtığın → **alt-ajan**, `claude agents`'ta asla görünmez.

**Adım 1 — Ebeveyn transkriptinde bildirimin `<status>`'una bak.**
- `completed` → iş bitti, `<result>` gerçek rapordur. Dur.
- `stopped` → **insan veya dış süreç öldürdü.** Sistem değil. Kasıtlıydı.
- `failed` → **DUR, terminal sanma.** Adım 2.

**Adım 2 — Transkriptin SON KAYDINA bak** (tek en keskin ayırt edici):

| Gördüğün | Anlamı | Yapılacak |
|---|---|---|
| `isApiErrorMessage: true` + `stop_reason: "stop_sequence"` | **API ölümü.** Metin `You've hit your session limit` → kota; `Request rejected (429)` → hız limiti; `Server is temporarily limiting` → geçici kısıtlama | Adım 3, sonra limit kalkınca **resume et, sıfırdan başlatma**. Opus limitiyse `/model` ile geç |
| `stop_reason: "tool_use"` + metin bloğu yok | **Araç çağrısının ORTASINDA öldü** — abort/stall/süreç ölümü | Stall watchdog aşılmış olabilir; uzun `Bash`/`WebFetch` varsa eşiği yükselt |
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

**Adım 3 — Kısmi işi kurtar. Bildirimin `<result>`'ına GÜVENME.**

**[X] Dokümanın "partial work isn't lost" ifadesi, dosya seviyesinde doğru — bağlam seviyesinde yanıltıcı.** "Last output" kelimenin tam anlamıyla **son assistant metin bloğudur**; bir araştırma ajanında bu, araç çağrısından önceki tek cümlelik ara-nottur. Ölçülen `<result>` uzunlukları: **0, 71, 137, 147, 160 karakter.** İçerikleri:
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

1. **[D] Alt-ajanlar prompt cache'ten yararlanamaz.** *"A subagent starts its own conversation with its own system prompt and tool set... It builds its own cache, starting with no cache hits on its first call. **Subagents use the five-minute TTL even on a subscription**, since the automatic one-hour TTL applies to the main conversation."*
2. **[D] Cache okumaları ITPM'e sayılmaz, ama cache OLUŞTURMA sayılır.** N alt-ajan = N ayrı cache oluşturma.

→ **10 paralel ajan, tek ajanın 10 katından DAHA FAZLA ITPM baskısı yapar.**
→ **Pratik sonuç: uzun ömürlü az sayıda ajan > kısa ömürlü çok sayıda ajan.** Aynı iş 30 ajan yerine 10 ajana bölünürse **20 cache-oluşturma turu tasarruf edilir.**

**[X] Çözülmemiş gerilim:** `CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY` = **10** ("read-only tools **and subagents** that can execute in parallel") vs `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` = **20**. Dokümanlar ikisini birbirine bağlamıyor. En tutarlı okuma: 10 = yürütme kapısı, 20 = muhasebe kapısı. **Pratik bağlayıcı sınır 10.**

---

## 9 — Paralel koşum bütçe kuralı

Gözlenen tabloyu (112 alt-ajan · 17 API ölümü · WebSearch defalarca tükendi) dokümante mekanizmalara oturtunca:

1. **Dalga genişliği ≤ 10, sabit.** Bağlayıcı sınır 20 değil **10**. Üstü paralellik satın almaz — yalnız kuyrukta bekler, ama oturum-toplamı sayacını (200) ve WebSearch bütçesini (200) tüketir. **112 ajanlık koşum, 200'lük tavanın yarısını tek koşumda harcadı.**
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

**▲ İki kritik istisna [D]:**
1. **Yerleşik `Explore` ve `Plan` ajanları tek-atışlıktır, agent ID döndürmezler → SÜRDÜRÜLEMEZLER.** Uzun/pahalı işlerde `general-purpose` veya özel ajan kullanılmalı.
2. **Kullanıcının kendi durdurduğu ajan otomatik sürdürülmez**; `SendMessage` "ajan iptal edildi" reddiyle döner. Çözüm: alt-ajan panelindeki transkripte yazmak bu bayrağı temizler.

**[D] `/rewind` checkpointing iş dayanıklılığı için DEĞİL, kod içindir.** Sınırları sert: **bash ile değiştirilen dosyalar izlenmez**, **alt-ajanların yaptığı düzenlemeler geri alınmaz** ("bunları geri almak için git kullanın"). Dokümanın kendi ifadesi: *"checkpoint'leri 'yerel geri al', Git'i 'kalıcı tarihçe' olarak düşünün."*
→ **JARVIS'in "her karar bir commit" kuralı (m.10) bu boşluğu zaten kapatıyor.** Kayda değer: kanonumuz bu noktada dokümandan önce doğruydu.

**▲ [D] Anthropic'in kendi tavsiyesi transkript kurtarmaya karşı:** *"Oturum sürdürmeye güvenme. İhtiyacın olan sonuçları (analiz çıktısı, kararlar, dosya diff'leri) uygulama durumu olarak yakala ve taze bir oturumun promptuna geçir. Bu, transkript dosyalarını ortalıkta taşımaktan çoğu zaman daha sağlamdır."*
→ Yani: **artımlı dosya > transkript kurtarma.** Bu, Salih'in "veri kaybı istemiyorum" talimatının teknik karşılığıdır — ve bu oturumda raporları koşum bitmeden diske yazıp commit'lemenin gerekçesi.

---

## 11 — Uygulanabilir desenler (değer yargılı)

### Bugün, sıfır altyapı

| # | Desen | Değer |
|---|---|---|
| **U1** | **`Explore`/`Plan` yerine `general-purpose` kullan** uzun işlerde — ilk ikisi **sürdürülemez** | **ÇOK YÜKSEK** — maliyet sıfır, kazanç yapısal |
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

## 13 — İddia listeleri (antitez için hazır, **⊨¬2**)

**A25:** ① Stopped yalnız insan/dış müdahaleyle girilir; limit ve stall **Failed** üretir. ② `claude agents` alt-ajanları hiç göstermez. ③ Agent view iki ortogonal ekseni tek satırda gösterir; `∙` sonlanma durumu değildir. ④ `is_error` limit-ölümlerini filtrelemez; yalnız `subtype` ayırt eder. ⑤ Hata subtype'lı mesajda `result` alanı şemadan tamamen yoktur. ⑥ Tek keskin ayırt edici `isApiErrorMessage: true` + sentetik `stop_reason: "stop_sequence"`'tır. ⑦ `failed` terminal değildir; aynı task-id sonradan `completed` bildirebilir. ⑧ "Partial work isn't lost" dosya seviyesinde doğru, bağlam seviyesinde yanıltıcıdır. ⑨ *(A26 tarafından çürütüldü — §6)*

**A26:** ① Bağlayıcı paralellik sınırı 20 değil **10**'dur. ② WebSearch bütçesi hız limiti değil oturum sayacıdır ve **sessiz** tükenir. ③ Alt-ajanlar cache'ten yararlanamaz; "10 ajan = 10x" **alt sınırdır**. ④ "resets at X" sıfırlanma değil **tam dolum** anıdır. ⑤ Abonelik penceresi ile API penceresi farklı mekanizmalardır. ⑥ İşçileri Sonnet'e almak **ayrı bir ITPM kovası açma** hamlesidir. ⑦ Watchdog başarı garantisi değil, **başarısızlığı duvar-saatine çeviren takastır**. ⑧ Batch'e taşınan iş senkron kotayı **hiç yemez** + %50 ucuz. ⑨ `/usage` otoriter değildir — makine-yerel tahmindir.

**A27:** ① Kesilen alt-ajanın işi kaybolmaz; `SendMessage` ile tam bağlamıyla sürdürülebilir. ② **Erken ve sık metin üretmek**, dayanıklılık kazandıran en ucuz tek müdahaledir. ③ Explore/Plan sürdürülemez, uzun işlerde kullanılmamalı. ④ Tek kişilik sistemde Temporal kurmak aşırı-mühendisliktir. ⑤ Exactly-once ulaşılamazdır; hedef her adımı at-least-once'a güvenli kılmaktır. ⑥ Yasak olan `random()` değil, **kayıt-dışı non-determinizm**. ⑦ Checkpointing iş dayanıklılığı için tasarlanmamıştır; **git tek gerçek kontrol noktasıdır**. ⑧ Anthropic'in kendi dokümanı **artımlı dosyayı transkript kurtarmaya tercih eder**.

---

## 14 — Açık borçlar

| # | Borç | Not |
|---|---|---|
| C1 | **Antitez (Aşama 2) bu aile için de koşulmadı** | A5'ten beri süregelen borç; iddia listeleri §13'te hazır |
| C2 | **Sürüm çatalı: kurulu ikili v2.1.42, dokümanlar ~v2.1.217** | `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` kurulu ikilide **grep'te yok**. Dokümandaki stall davranışı **bu makinede geçerli olmayabilir** — ana atlastaki stall-watchdog analizini bu ışıkta yeniden okumak gerek |
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
- **V71 — Sürdürülemez ajan yasağı.** `Explore`/`Plan` uzun/pahalı işlerde kullanılmasın (U1). Küçük kural, dayanağı [D], maliyeti sıfır.

---

## 16 — Kapanış damgası

**Aile:** A25 · A26 · A27 — üçü de **⊨¬2** (antitez koşulmadı)
**Kanıt tabanı:** **[D] ağırlıklı** — kurulu `cli.js` zod şemaları · 115 alt-ajan transkripti (kendi ölçümümüz) · ham doküman markdown'ı. Bu, oturumun en güçlü kanıt tabanıdır.
**Çözülen çelişki:** `api_retries_exhausted` — A26 lehine (§6), gerekçe kayıtlı
**Düzeltilen kendi hükmüm:** A25'in "3'ten 2'si teslim edilmedi" sayısı — tam-oturum verisiyle **[X]**; mekanizma korunur, sayı düşer (§2)
**Salih'in sorusuna doğrudan cevap:** ajanların **"stopped" olmadı** — `failed` oldular, ve `failed` **terminal değildi**. Kök neden ajanlarda değil, **koşum zarfının aşılmasındaydı** (§9).
