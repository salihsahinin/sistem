# Ajanlar Neden Duruyor — sözel önerme karşılığı

> Kaynak: `raporlar/2026-07-26-ajan-durma-atlas.md` · Register: düz lojik · Compiler: **KAPALI**
> Okuma kuralı: **öncülü sağlanmayan bir önermenin sonucu geçerli DEĞİLDİR.**

**Numaralandırma:** kaynağın kendi adresleri korunur. `§0.1` = kaynak §0'ın birinci önermesi. `U1`, `L16`, `C1`, `V68` kodları kaynaktakiyle **aynıdır**.

**Kanıt sütunu:** *birincil* = birincil kaynağa inildi · *ölçüm* = bu makinede/bu oturumda ölçüldü · *çelişkili* = kaynaklar çelişkili, hüküm yok · *kestirim* = ölçülmemiş · *çıkarım* = ölçüm değil, bileşim.

**Antitez sütunu:** bu ailenin antitezi 2026-07-26'da **araç kullanarak** koştu (48 araç çağrısı, ham doküman + kurulu `cli.js`). Dolayısıyla buradaki *"sağ çıktı"* damgaları **aynı-aile şerhinden muaftır** — kanıt modelin belleğinden değil, kaynağın kendisinden geldi.

---

## §0 — Öncül düzeltmesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§0.1** | `Stopped` durumuna üç yolla girilir: `Ctrl+X`, `claude stop`/`claude kill`, ve sürecin dışarıdan öldürülmesi.<br>Oturum limiti, hız limiti, maksimum tur sayısı ve asılma zaman aşımı ise **`Failed`** üretir, `Stopped` üretmez. | birincil | daraltıldı → K15: makine kapanması da dışarıdan sonlandırmadır ∧ `Failed` üretir ⇒ *"yalnız üç yol"* çerçevesi bu kenar-durumda çatlar. Ayrıca oturum durumu ile alt-ajan task durumu aynı şey değildir. |
| **§0.2** | Bu oturumun 35 bildiriminin 22'si `completed`, 13'ü `failed`, **0'ı `stopped`**'tır.<br>Yani bu oturumda hiçbir ajan `stopped` olmamıştır. | ölçüm | aile koştu, hüküm yok |
| **§0.3** | `Stopped` sistemin **en net tanımlı** durumudur, çünkü yalnız insan ya da dış müdahaleyle oluşur.<br>Belirsiz olan `Failed`'dır: limit, API hatası, asılma ve araç hatası hepsi oraya yığılır.<br>Kafa karışıklığının kaynağı `Stopped` değil, **`Failed`'ın aşırı yüklenmiş olmasıdır**. | çıkarım | aile koştu, hüküm yok |
| **§0.4** | `claude agents` komutu alt-ajanları **ayrı satır olarak listelemez**.<br>Arka plan oturumu `claude agents`'ta görünür ve durumu `~/.claude/jobs/<id>/state.json`'dadır; bu makinede bu dizin **hiç yoktur**.<br>Alt-ajan `/tasks` ve @-mention ile görünür ve transkripti `~/.claude/projects/<slug>/<uuid>/subagents/agent-<id>.jsonl`'dadır; bu makinede **115 transkript vardır**.<br>Koşulan her şey alt-ajandır ⇒ onları `claude agents` içinde aramak sonuçsuzdur. | birincil ∧ ölçüm | daraltıldı → K16: *"hiç göstermez"* yanlış. Agent view kullanılamıyorsa `claude agents` bir sayı ∧ ardından yapılandırılmış alt-ajanları listeler. |

---

## §1 — İki eksen

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§1.1** | Agent view iki ortogonal ekseni **aynı satırda** gösterir.<br>Görev durumu ekseni: Working, Needs input, Idle, Completed, Failed, Stopped.<br>Süreç canlılığı ekseni: `✻`/`✽` süreç canlı, `∙` süreç çıkmış, `✢` loop uykusu. | birincil | sağ çıktı — antitezin ifadesiyle *"tam isabet"*; doküman ikisini ayrı tablolarda listeliyor |
| **§1.2** | `∙` işareti bir **sonlanma durumu değildir**.<br>Yaklaşık 1 saat boşta kalan oturumun sürecini süpervizör kaynak boşaltmak için kapatır; transkript ve durum **diskte kalır**.<br>*"Ajan öldü"* sanılan şeylerin bir kısmı budur. | birincil | sağ çıktı |
| **§1.3** | Yanlış alarm listesi: `∙` ikonu süreç çıkışıdır, durum değildir. `Needs input` izin, soru, sandbox ya da MCP kimlik doğrulaması bekliyor demektir — çalışmıyor ama **ölmemiştir**.<br>SDK'daki `is_error` alanına bakarak limit ölümü elemeye çalışmak **güvenilmezdir**; `subtype`'a bakılır. | birincil | üçüncü madde çürütüldü → K11 (bkz. §3.3) |

---

## §2 — `failed` terminal değil

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§2.1** | Bir ajan t₀ anında limitten `failed` bildirdiyse ve t₁ > t₀ anında limit sıfırlandıysa, ajan **çalışmaya devam edebilir ve raporunu bitirebilir**.<br>Ölçüm: beş ajan 04:09–04:15 arasında `failed` bildirdi, limit 04:50'de kalktı, beşi de 05:08–05:12 arasında 20.274 ile 34.998 karakter arası rapor üretti ve **beşi de teslim edildi**. | ölçüm | aile koştu, hüküm yok |
| **§2.2** | Bu oturumda veri kaybı **sıfırdır** — ama bu bir sistem özelliği değil, bir **müdahalenin sonucudur**.<br>O beş ajan limit kalktıktan sonra **elle `SendMessage` ile sürdürüldüğü için** teslim edildi. Müdahale olmasaydı raporlar diskte kalacaktı. | ölçüm ∧ çıkarım | aile koştu, hüküm yok |
| **§2.3** | A25 ajanının hükmü *"3 rapordan 2'si teslim edilmedi"* idi.<br>Tam oturum taraması bunu düzeltir: **mekanizma doğrudur** (`failed` terminal değildir), **sayı yanlıştır** (ölçüm, sürdürmeler kayda geçmeden önce alınmıştı).<br>Yani mekanizma korunur, sayı düşer. | ölçüm | aile koştu, hüküm yok |
| **§2.4** | Operasyonel sonuç: `failed` görüldüğünde ajan **ölü sayılmaz**. Limit sıfırlandıktan sonra `SendMessage` ile sürdürülür ve tam bağlamıyla kaldığı yerden devam eder. | çıkarım | aile koştu, hüküm yok |

---

## §3 — Sonlanma taksonomisi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§3.1** | SDK'nın `result` mesajı iki şemanın birleşimidir.<br>Başarı şeması: `subtype: "success"` ve bir `result: string` alanı.<br>Hata şeması: `subtype` değeri `error_during_execution`, `error_max_turns`, `error_max_budget_usd` ya da `error_max_structured_output_retries` ve bir `errors: string[]` alanı. | birincil | aile koştu, hüküm yok |
| **§3.2** | Hata şemasında `result` alanı yoktur — **ama bu dile bağlıdır**.<br>TypeScript'te alan şemada **yoktur**. Python dataclass'ı tüm varyantları tek şekle düzleştirdiği için alan **vardır ve değeri `None`'dır**.<br>Kod yazarken alanın yokluğuna değil, `subtype`'a bakılır. | birincil | daraltıldı → K17: iddia dil belirtmiyordu ⇒ yarısı yanlıştı |
| **§3.3** | `subtype` değeri `error_max_turns` ya da `error_max_budget_usd` iken `is_error` alanının değeri **çözülmemiştir**.<br>Kurulu `cli.js` v2.1.42'de birebir `is_error:!1` (false) okundu.<br>`agent-sdk/python.md` ise birebir şunu diyor: *"`is_error`: hata durumunda biten konuşmalarda `True`. `error_*` alt tiplerinde **daima `True`**."*<br>Uzlaştırma adayları — hiçbiri doğrulanmadı: minifiye kod okuması yanlış olabilir; CLI'nin iç üretim yolu ile SDK'nın belgelenmiş sözleşmesi farklı katmanlar olabilir; sürüm kayması olabilir (v2.1.42 ile yaklaşık v2.1.217 arası).<br>**Pratik hüküm ayakta, gerekçesi düştü:** limit ölümlerini ayırt etmek için `subtype`'a bakılır — bu her iki senaryoda da doğrudur. | çelişkili | ⛔ çürütüldü → K11 |
| **§3.1** | **Taksonomi eksiktir: dördüncü ve kayıtsız bir sonlanma durumu ölçüldü.**<br>Ajan durur, aktif görevi kalmaz ve **hiçbir bildirim üretmez** — ne `completed`, ne `failed`, ne `stopped`.<br>Ölçüm: üç ajan 15:10–15:11 arasında son kaydını yazdı ve 45 dakika boyunca dosya boyutu, satır sayısı ve değişiklik zamanı **birebir aynı** kaldı ⇒ büyüme sıfırdır.<br>Son kayıt imzası üçünde de aynıydı: tip `assistant`, içerik `['text']`, `isApiErrorMessage` yok, `stop_reason` yok ⇒ §4'teki **hiçbir imzaya uymuyor**: ne API ölümü ne araç ortası ölüm. Metin ürettiler, sonra sustular.<br>`SendMessage` üçüne de *"aktif görevi yoktu"* döndürdü ⇒ ajan ölüdür ve çalışmamaktadır.<br>Sonuç: §4 teşhis kılavuzu bu vakayı **yakalayamaz**, çünkü kılavuz durum alanından başlar ve burada durum alanı **hiç doğmaz**.<br>Kılavuza eklenen adım: bildirim yoksa ve süre beklenenden uzunsa, transkriptin değişiklik zamanı ve satır sayısı **örneklenir**, bildirim beklenmez. | ölçüm | — (yeni, teslim sonrası) |
| **§3.1b** | **Teşhis dürtme sonrası değişti: bu bir hesaplama asılması değil, bir teslim arızasıdır.**<br>`SendMessage` gönderildiğinde üçü de **29 ile 34 saniye arasında tam raporla** döndü ve **hiç araç çağırmadı**.<br>Ajanın kendi ifadesi: *"Donmuş değilim — önceki turda tam sonucu ürettim ve döndürdüm."*<br>Yani hesaplama 15:11'de bitmişti; teslim olmamıştı. İş 45 dakika boyunca **diskte hazır bekledi**, ebeveyn beklemeye devam etti.<br>Hesaplama asılmasında iş yapılmamıştır ve sürdürme onu **yaptırır** (tam koşum maliyeti). Teslim arızasında iş yapılmıştır ve sürdürme onu yalnız **taşır** (yaklaşık 30 saniye).<br>Pratik kural: süre beklenenden uzunsa **önce dürt, sonra endişelen**.<br>Ders: **bildirimin yokluğu, çalıştığı anlamına gelmez.** Bu, P73'ün (*"kaynak tükendi ≡ iş bitti"*) kardeşidir.<br>Kurtarma kaydı: ara metin üçünde de **mevcuttu** ⇒ kesilme anında iş diskteydi, kayıp sıfırdı ⇒ *"iskelet önce"* protokolü (V69) **üçüncü kez** karşılığını verdi. | ölçüm | — (yeni, teslim sonrası) |
| **§3.4** | Katmanlar arası kayıp: SDK'da **5 ayırt edilebilir** terminal durum vardır; ekranda **3 kalır**; bütçe ile altyapı hatası ayrımı **tamamen silinir**.<br>`task_notification` enum'u yalnız üç değer taşır: `completed`, `failed`, `stopped`.<br>Kıyas: Temporal'da CANCELED ile TERMINATED farklıdır; LangGraph'ta GraphRecursionError, NodeCancelledError ve NodeTimeoutError farklıdır; Celery bütçeyi ayırmaz.<br>Ortak desen: bu sistemlerin hepsi *"iş bitti"*, *"dış iptal"* ve *"altyapı hatası"*nı ayırır; **ayrışma noktası bütçedir**.<br>Sonuç: zaaf taksonomide değil, **katmanlar arası kayıptadır**. | birincil | aile koştu, hüküm yok |

---

## §4 — Teşhis kılavuzu

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§4.1** | Adım 0: `claude agents` satırındaysa arka plan oturumudur; `Agent`/`Task` ile açıldıysa alt-ajandır. | birincil | bkz. §0.4 daraltması |
| **§4.1b** | **Adım 0.5: bildirim hiç gelmediyse bekleme.**<br>Bildirim yoksa ve süre beklenenden uzunsa, transkriptin değişiklik zamanı ve satır sayısı **45 saniye arayla iki kez örneklenir**. Büyüme sıfırsa ajan **sessizce ölmüş** olabilir ⇒ doğrudan `SendMessage` gönderilir.<br>Maliyet yaklaşık 30 saniyedir; alternatif saatlerce boş beklemedir. | ölçüm | — (yeni, §3.1'den) |
| **§4.2** | Adım 1: bildirimin durumu `completed` ise iş bitmiştir ve sonuç alanı gerçek rapordur.<br>`stopped` ise insan ya da dış süreç öldürmüştür; sistem değil, kasıtlıdır.<br>`failed` ise **terminal sanılmaz** ve Adım 2'ye geçilir. | birincil | aile koştu, hüküm yok |
| **§4.3** | Adım 2: transkriptin son kaydına bakılır. Bu **en keskin** ayırt edicidir — *"tek"* değil.<br>`isApiErrorMessage: true` ve `stop_reason: "stop_sequence"` birlikteyse API ölümüdür; metin oturum limitini, hız limitini ya da geçici kısıtlamayı söyler; limit kalkınca **sürdürülür, sıfırdan başlatılmaz**.<br>`stop_reason: "tool_use"` varken metin bloğu yoksa araç çağrısının **ortasında** ölmüştür.<br>Son kayıt `type: "user"` ise araç döndükten hemen sonra ölmüştür.<br>Normal metin varken bildirim `failed` ise ajan bildirimden **sonra** devam edip bitirmiştir ⇒ transkript okunur, bildirime güvenilmez.<br>`isMeta` ile *"was stopped by the user"* varsa kullanıcı iptalidir; ayırt edici işaret, bu mesajda *"TaskOutput ile kontrol et"* cümlesinin **hiç geçmemesidir**. | birincil | daraltıldı → K18: eşleşme kaynak kodda doğrulandı, ama *"tek keskin ayırt edici"* süperlatifi doğrulanamadı — alan başka bağlamlarda da kullanılıyor |
| **§4.4** | 115 transkriptin son kayıt imzası dağılımı: normal metin ve `stop_reason: null` 72 vaka (normal bitiş); `isApiErrorMessage` ve `stop_sequence` 17 vaka (API hatası ölümü); normal metin ve `stop_reason: "end_turn"` 13 vaka (normal bitiş); `stop_reason: "tool_use"` ve metin yok 6 vaka (araç ortasında ölüm); boş son metin 4 vaka (belirsiz kesinti); son kayıt `type: "user"` 3 vaka (araç sonrası ölüm). | ölçüm | aile koştu, hüküm yok |
| **§4.5** | Adım 3: bildirimin sonuç alanına **güvenilmez**.<br>*"Kısmi iş kaybolmaz"* ifadesi dosya seviyesinde doğru, bağlam seviyesinde yanıltıcıdır.<br>Ölçülen sonuç alanı uzunlukları 0, 71, 137, 147 ve 160 karakterdir; içerikleri ara not gürültüsüdür — örneğin *"Line 3 is in. Waiting on the other three."*<br>Yani ebeveyne yaklaşık 100 karakterlik gürültü gider, onlarca dakikalık birikmiş araştırma **transkriptte kalır**. Bir vakada sonuç alanı tamamen boştu.<br>Kurtarma: `output_file` zaten transkripte symlink'tir; tümü okunmaz (bağlam taşar), yalnız 500 karakterden uzun assistant metin blokları çekilir — bu eşik ara notları eler. | birincil ∧ ölçüm | daraltıldı → H16: *"ebeveyne yalnız son metin bloğu geçer"* formülasyonu abartılı-dardır; aktarılan şey biriken kısmi çıktı ve hata notudur. Ölçülen uzunluklar bundan **etkilenmez**. |

---

## §5 — Kayıp mekanizması

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§5.1** | Sürüm v2.1.199'dan itibaren: API hatasıyla biten alt-ajan **metin üretmişse** kısmi çıktı ve *"kesildi"* notu döner.<br>**Hiçbir şey üretmemişse ya da yalnız araç çağrısı yapmışsa** *"Agent terminated early due to an API error"* mesajı gelir ve **tamamen başarısız olur**. | birincil | aile koştu, hüküm yok |
| **§5.2** | *"Sadece araç çağrısı"* şekli tam olarak bir **araştırma ajanının profilidir** — 20 WebFetch, sonra tek rapor.<br>Ölçülen 17 API ölümü ve 6 araç ortası ölüm bu imzayı taşır.<br>Bu, %22'lik kaybın **en olası tek mekanizmasıdır**. İş teorik olarak kurtarılabilir (transkript diskte durur), ama **varsayılan akışta kurtarılmaz**. | çıkarım | aile koştu, hüküm yok |
| **§5.3** | Mekanizmanın **ağırlığı** kestirimdir: araç çağrısı sırasında ölüm 115 vakanın 6'sında görüldü, yani **%5**.<br>Bu, hipotezin öngördüğünden düşüktür ⇒ mekanizma gerçektir, **ağırlığı abartılmıştır**. | ölçüm (ağırlık: kestirim) | aile koştu, hüküm yok |

---

## §6 — Kota mimarisi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§6.1** | Sistemde **on altı** ayrı limit vardır ve çoğu birbirinden bağımsızdır.<br>Oturum limiti tüm modeller için ortaktır ve yuvarlanan 5 saatlik penceredir. Haftalık limit oturum limitiyle **eşzamanlı** işler. Opus limiti yalnız Opus isteklerine uygulanır ⇒ `/model` ile Sonnet'e geçilirse **çalışma durmaz**.<br>API tarafında RPM, ITPM ve OTPM model sınıfı başına ayrıdır. Acceleration limit belgelenmemiştir ve sebebi ayırt edilemeyen 429 üretir.<br>WebSearch oturum bütçesinin **penceresi yoktur** ve **görünmezdir**.<br>Eşzamanlı araç/alt-ajan sınırı 10, eşzamanlı alt-ajan sınırı 20, oturum toplamı alt-ajan sınırı 200'dür (`/clear` sıfırlar), alt-ajan derinliği 1'dir (varsayılanda alt-ajan alt-ajan doğuramaz).<br>Bağlam ve auto-compact bir **limit değildir**, modelin maksimum girdisidir.<br>Batch limitleri senkron kotayı **etkilemez** ve %50 indirimlidir. 529 Overloaded hataları kotaya **sayılmaz**. | birincil | aile koştu, hüküm yok |
| **§6.2** | API tarafı bir **token bucket**'tır: *"kapasite sabit aralıklarla sıfırlanmak yerine maksimum limitinize kadar sürekli olarak yeniden doldurulur."*<br>Dolayısıyla `reset` başlıkları sıfırlanma anını değil **tam dolum anını** gösterir ⇒ **reset'i beklemek gerekmez**, kısmi kapasite daha önce açılır.<br>Abonelik tarafı ise yuvarlanan pencere ile ilan edilmiş reset anının bileşimidir.<br>İkisi farklı mekanizmadır; birinden çıkarılan sezgi diğerinde **yanlıştır**. | birincil | sağ çıktı |
| **§6.3** | A25 ailesi `claude_code.api_retries_exhausted` telemetri olayının **var olmadığını** buldu; dayanağı kurulu `cli.js` v2.1.42'de boş grep ve WebFetch özetinin *"yok"* demesiydi.<br>A26 ailesi aynı olayın **var olduğunu** buldu ve niteliklerini verdi (`total_attempts`, `total_retry_duration_ms`); dayanağı ham markdown'dı.<br>Hüküm: **A26 haklıdır.** Birinci gerekçe: ham markdown WebFetch özetinden üstündür ve A26 bunu kendi yöntem notunda yakaladı. İkinci gerekçe: kurulu ikili v2.1.42, dokümanlar yaklaşık v2.1.217 sürümündedir ⇒ sürüm farkı boş grep'i açıklar.<br>A25'in ölçümü kendi bağlamında doğrudur, **genellemesi yanlıştır**. | birincil (çelişki çözüldü) | aile koştu, hüküm yok |
| **§6.4** | Kural (V68): `code.claude.com` ve `platform.claude.com` için **daima `.md` son ekiyle doğrudan çekim** yapılır; WebFetch özetine güvenilmez. | çıkarım | aile koştu, hüküm yok |

---

## §7 — WebSearch bütçesi

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§7.1** | Bir oturum **en fazla 200 WebSearch** çağrısı yapabilir ve bu sayaç **ana konuşma ile onun doğurduğu her alt-ajan için ortaktır** ⇒ paralel araştırma dalgalarının yaptığı aramalar **aynı limitten yer**. | birincil | sağ çıktı ⭐ — `tools-reference.md` birebir doğruladı |
| **§7.2** | Bu bir hız limiti **değildir**, bir **oturum sayacıdır**: penceresi yoktur, `/clear`'a kadar birikir.<br>Ayarlanabilir (`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`, varsayılan 200, tavansız), ama **kapatılamaz**. | birincil | sağ çıktı |
| **§7.3** | Bütçe tükendiğinde **hata dönmez**: *"Uyarıyı görmezsin: sınırlanmış bir çağrı, konuşmada hiçbir şey yapmamış bir arama olarak görünür."*<br>Sonuç: bir dalga **sessizce boş dönebilir** ve bu fark edilmez. | birincil | sağ çıktı ⭐ |
| **§7.4** | 112 alt-ajan çarpı ajan başına 2 arama = **224 > 200** ⇒ zarf **zaten aşılmıştı**.<br>Sonuç: A8, A12 ve A18 alt-hatlarının *"bulunamadı"* demesinin sebebi büyük olasılıkla budur ⇒ doğru cevap **"aranamadı"**dır. | ölçüm ∧ çıkarım | aile koştu, hüküm yok |
| **§7.5** | Çözüm ölçülmüştür: görev emrinde **URL verilirse** ajan WebSearch değil **WebFetch** kullanır ve bütçeden hiç yemez.<br>A26 ajanı bu araştırmayı **2 WebSearch ile** bitirdi, çünkü dokümanları doğrudan çekti. | ölçüm | aile koştu, hüküm yok |

---

## §8 — Paralel koşumun gizli maliyeti

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§8.1** | *"On ajanı paralel koşturmak, kotayı bir ajan koşturmanın kabaca on katı hızda tüketir."*<br>Bu bir **iyimser alt sınırdır**; iki mekanizma daha vardır. | birincil | aile koştu, hüküm yok |
| **§8.2** | Alt-ajan kendi konuşmasını, kendi sistem promptunu ve kendi araç setini kullanır ⇒ **kendi cache'ini kurar** ve **ilk çağrısında hiç isabet almaz**, sonraki turlarda **kendi cache'ini ısıtır**.<br>Alt-ajanlar **abonelikte bile** 5 dakikalık TTL kullanır; 1 saatlik otomatik TTL yalnız ana konuşmaya uygulanır. | birincil | ⛔ çürütüldü → K12: eski hâli *"alt-ajanlar cache'ten yararlanamaz"* diyordu ⇒ fazla güçlü ∧ yanlış |
| **§8.3** | Cache **okumaları** girdi token dakika limitine sayılmaz; cache **oluşturma** sayılır ⇒ N alt-ajan = N ayrı cache oluşturma.<br>Sonuç: 10 paralel **kısa ömürlü** ajan, tek ajanın 10 katından **daha fazla** baskı yapar.<br>Sonuç: az sayıda uzun ömürlü ajan, çok sayıda kısa ömürlü ajandan üstündür; aynı iş 30 yerine 10 ajana bölünürse **20 cache oluşturma turu** tasarruf edilir. | birincil | K12 bu sonucu **zayıflatmıyor, güçlendiriyor**: uzun ömürlü ajan kendi cache'ini ısıttığı için tercihin mekanizması artık nettir |
| **§8.4** | Eşzamanlılıkta **üç ayrı mekanizma** vardır ve birleştirilmez.<br>`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` varsayılanı **20**'dir ⇒ belgelenmiş alt-ajan eşzamanlılık sınırı budur.<br>`MAX_TOOL_USE_CONCURRENCY` **10**'dur ⇒ paralel araç ve alt-ajan **yürütme kapısıdır**.<br>*"10 oturum ≈ 10 kat kota"* ifadesi **üçüncü ve tamamen farklı** bir şeydir: bir tüketim kuralıdır, sert sınır değildir. | birincil | ⛔ çürütüldü → K13: eski hâli üç sayıyı tek bir *"bağlayıcı sınır 10"* hükmüne birleştirmişti |

---

## §9 — Dalga zarfı

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§9.1** | Dalga genişliği en fazla 10 olmalıdır. Gerekçe **sert bir sınır değil**, yürütme kapısı ile kota tüketiminin bileşimidir.<br>Üstü paralellik satın almaz — yalnız kuyrukta bekler, ama oturum toplamı sayacını (200) ve WebSearch bütçesini (200) tüketir.<br>112 ajanlık koşum, 200'lük tavanın yarısını **tek koşumda** harcadı. | birincil ∧ ölçüm | gerekçesi çürütüldü → K13; **sayı korunur** |
| **§9.2** | WebSearch ajan başına tayınlanır: ajan sayısı çarpı ajan başına arama, 200'ü aşmamalıdır.<br>Daha iyisi: emirde URL verilir ⇒ WebFetch kullanılır ⇒ bütçeden yenmez.<br>Dalga sonunda sayaç kontrol edilir, çünkü **sessiz tükenir**. | birincil | aile koştu, hüküm yok |
| **§9.3** | Model ataması: işçi Sonnet, sentez Opus, tarama Haiku.<br>Opus 5'in **ayrı bir girdi token dakika kovası** vardır ⇒ işçiler Sonnet'e alınırsa işçi trafiği Opus kovasından **hiç yemez** ⇒ aynı kotayla iki paralel havuz elde edilir.<br>V59 tam olarak bunu söylüyordu; artık **mekanizması da elimizdedir**. | birincil | aile koştu, hüküm yok |
| **§9.4** | Effort ajan başına düşürülür. Varsayılan `high`'tır ve düşünme token'ları **çıktı olarak** faturalanır.<br>Getirme ve tarama ajanlarına `low` ya da `medium`, sentez ajanına `high` verilir.<br>112 ajanlık koşumda bu, **tek başına en büyük token kalemidir**. | birincil | aile koştu, hüküm yok |
| **§9.5** | Dalgalar kademeli başlatılır. Acceleration limit'in tek reçetesi budur; 10 ajanı aynı saniyede açmak, ortalama düşük olsa bile patlama kaynaklı 429 tetikler. **2-3 saniye ara yeterlidir**. | birincil | aile koştu, hüküm yok |
| **§9.6** | `CLAUDE_CODE_RETRY_WATCHDOG` açıkken ve cevap reset zamanı taşıyorken, sistem kör geri çekilme yerine **pencerenin bitişini bekler** ⇒ 5 saatlik limite çarpan ajan **saatlerce asılı kalabilir**.<br>Kural: **yalnız gözetimsiz koşumda açılır**; interaktif dalgada hızlı başarısızlık ve yeniden dalga daha ucuzdur. | birincil | sağ çıktı — `env-vars.md` birebir doğruladı |
| **§9.7** | Sert bütçe tavanı konur: print modunda `--max-budget-usd`. Alt-ajan harcaması tavana sayılır; tavan dolunca arka plan ajanları durdurulur. | birincil | aile koştu, hüküm yok |
| **§9.8** | Zarf: **10 ajan, Sonnet, orta effort, 2-3 saniye aralıklı başlatma, ajan başına en fazla 2 WebSearch (tercihen 0 ve URL), oturum toplamı 60-80 ajan, sert bütçe tavanı, gözetimsizde watchdog açık.**<br>Gözlenen 112 ajanlık koşum bu zarfın **dışındaydı** ⇒ %22'lik limit kaynaklı sonlanma **anomali değil, beklenen sonuçtur**.<br>Sorun ajanlarda değil, **onları koşturma biçimindeydi**: belgelenmiş uyarılara rağmen aynı anda 4-5 aile açıldı ve her biri kendi alt-hatlarını doğurdu.<br>Bu, ana atlastaki L1 dersinin (*"ölç, sonra teorileştir"*) ikinci vakasıdır: **teori ölçümden önce kuruldu.** | çıkarım | aile koştu, hüküm yok |

---

## §10 — Sürdürme

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§10.1** | Kesilen bir alt-ajanın işi kurtarılabilir; transkriptler ana konuşmadan **bağımsız** dosyalarda tutulur.<br>Ana konuşma compact olduğunda alt-ajan transkriptleri **etkilenmez**.<br>Claude Code yeniden başlatıldıktan sonra aynı oturum sürdürülerek bir alt-ajan sürdürülebilir.<br>Temizlik `cleanupPeriodDays` ile yapılır, varsayılanı **30 gündür**. | birincil | sağ çıktı |
| **§10.2** | Sürdürme aracı `SendMessage`'dır: *"Sürdürülen alt-ajanlar, önceki tüm araç çağrıları, sonuçları ve akıl yürütmesi dahil tam konuşma geçmişini korur."*<br>Tamamlanmış bir alt-ajan `SendMessage` alınca **yeni bir `Agent` çağrısı olmadan** arka planda otomatik sürdürülür.<br>Sürdürme, eşzamanlılık limitini **kontrol etmeden** taze slot alır ⇒ kurtarma yolu kapasite kapısından **muaftır**. | birincil | sağ çıktı |
| **§10.3** | **ASKIDA — kural olarak kullanılmaz:** *"Yerleşik `Explore` ve `Plan` ajanları tek atışlıktır, agent ID döndürmezler, dolayısıyla sürdürülemezler."*<br>Bu iddianın dokümanda **dayanağı bulunamadı**. Antitez `sub-agents.md`'yi okudu; bu ajanlar için tutulan tek istisna CLAUDE.md ve git-status'u **yüklememeleridir**.<br>İddia bir alt-ajanın aktarımıydı ve **doğrulanmadan** tavsiye listesinin başına konuldu.<br>Doğrulanana kadar *"Explore/Plan kullanma"* diye bir kural **çıkarılmaz**. Yanlış olduğu için değil, **dayanağı gösterilemediği için**.<br>Doğrulama yolu ucuzdur: bir `Explore` ajanı açılır, dönen nesnede agent ID var mı bakılır. | kestirim | ⛔ ASKIYA ALINDI → K14 |
| **§10.4** | Kullanıcının kendi durdurduğu ajan otomatik sürdürülmez; `SendMessage` *"ajan iptal edildi"* reddiyle döner.<br>Çözüm: alt-ajan panelindeki transkripte yazmak bu bayrağı temizler. | birincil | aile koştu, hüküm yok |
| **§10.5** | `/rewind` checkpointing iş dayanıklılığı için **değil**, kod içindir.<br>Bash ile değiştirilen dosyalar **izlenmez**; alt-ajanların yaptığı düzenlemeler **geri alınmaz**.<br>Dokümanın kendi ifadesi: *"checkpoint'leri 'yerel geri al', Git'i 'kalıcı tarihçe' olarak düşünün."*<br>Sonuç: JARVIS'in m.10 kuralı bu boşluğu **zaten kapatıyor**; kanon bu noktada dokümandan önce doğruydu. | birincil | sağ çıktı ⭐ |
| **§10.6** | Anthropic'in kendi tavsiyesi transkript kurtarmaya **karşıdır**: *"Oturum sürdürmeye güvenme. İhtiyacın olan sonuçları uygulama durumu olarak yakala ve taze bir oturumun promptuna geçir. Bu, transkript dosyalarını ortalıkta taşımaktan çoğu zaman daha sağlamdır."*<br>Sonuç: **artımlı dosya, transkript kurtarmadan üstündür.** Bu, *"veri kaybı istemiyorum"* talimatının teknik karşılığıdır ve raporları koşum bitmeden diske yazıp commit'lemenin gerekçesidir. | birincil | aile koştu, hüküm yok |

---

## §11 — Uygulanabilir desenler

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **U1** | ⛔ **ASKIDA.** *"Uzun işlerde `Explore`/`Plan` yerine `general-purpose` kullan, çünkü ilk ikisi sürdürülemez."*<br>Öncül doğrulanmadı (bkz. §10.3). Eski değer etiketi (*"çok yüksek değer, sıfır maliyet"*) **geri çekildi** — o etiket, doğrulanmamış bir maddeyi listenin başına taşıyan şeydi. | kestirim | ⛔ askıya alındı → K14 |
| **U2** | Ajan promptuna *"önce iskelet, sonra doldur"* konur: ilk bulguyu bulur bulmaz **kısa bir ara metin** üretilir — araç çağrısı değil, metin.<br>Gerekçe §5'tedir: metin varsa kısmi çıktı döner, yalnız araç çağrısı varsa **her şey kaybolur**.<br>Değer: en yüksek kazanç/maliyet oranı. Yeni araç yok, yeni dosya yok. | birincil | aile koştu, hüküm yok |
| **U3** | Uzun araştırma ajanları arka plana alınır: arka planda son çıktı ebeveyne dahil edilir; ön planda araç şekilliyse hepsi kaybolur. | birincil | aile koştu, hüküm yok |
| **U4** | Tekrar eden ajanlara `memory: project` verilir; `.claude/agent-memory/` git'le versiyonlanır ⇒ **artımlı yazmanın kanona uygun biçimidir** ve rapor dosyası yasağını ihlal etmez.<br>Yalnız tekrar eden ajanlar için geçerlidir. | birincil | aile koştu, hüküm yok |
| **U5** | Script'li koşumda `--session-id <UUID>` kullanılır ⇒ kurtarma anahtarı işten **önce** elde tutulur. Maliyeti sıfırdır. | birincil | aile koştu, hüküm yok |
| **U6** | `git commit` **tek gerçek checkpoint**'tir (§10.5). JARVIS'te zaten kuruludur. | birincil | sağ çıktı |
| **U7** | Kesilen ajan `SendMessage` ile sürdürülür, yeniden başlatılmaz. Değeri tamamen **biliyor olmaktadır**. | birincil | sağ çıktı |
| **U8** | `SessionEnd` hook'u ile transkript arşivi kurulur ⇒ 30 günlük pencereyi aşan kayıt katmanı. Değer orta, çünkü 30 gün zaten uzundur. | birincil | aile koştu, hüküm yok |
| **U9** | İş Continue-As-New mantığıyla parçalanır: tek dev ajan yerine, öncekinin özet durumunu girdi alan 2-3 ajanlık zincir.<br>Uyarı: **granülarite bedava değildir** — her yeni ajan bağlamı yeniden kurar. | birincil | aile koştu, hüküm yok |
| **U10** | Idempotency key ile yeniden çalıştırma güvenliği sağlanır (`<koşum-id>-<adım-id>`). Yalnız push/publish sınırında geçerlidir. | birincil | aile koştu, hüküm yok |
| **U11** | At-least-once kabul edilir, exactly-once kovalanmaz: her adım tekrar güvenli yapılır, tekrar engellenmeye çalışılmaz.<br>Bu bir **kural değil, zihniyettir**. | ikincil | aile koştu, hüküm yok |
| **U12** | Temporal, Restate ya da DBOS **kurulmaz**. Service, kalıcılık deposu ve Worker filosu ister; determinizm kısıtları **tüm iş akışı kodunu yeniden yazdırır**.<br>Çözdüğü problem *"binlerce eşzamanlı workflow, çoklu makine, çoklu takım"*tır.<br>**Kavramları al, çalışan sistemi alma** — bu araştırmanın en net yargısıdır. | çıkarım | çürütülemedi |
| **U13** | Kendi write-ahead log'unu ya da event-sourcing katmanını yazma. LLM çağrısı deterministik değildir; replay aynı sonucu vermez. **Git zaten append-only log'undur.** | çıkarım | aile koştu, hüküm yok |
| **U14** | Saga/telafi altyapısı kurma. Tek kişilik repoda geri alma `git revert`'tür. Kavram olarak öğrenilir, sistem olarak kurulmaz. Tek istisna `git push` sınırının ötesidir (yayınlama). | çıkarım | aile koştu, hüküm yok |
| **U15** | `/loop` ile limit sonrası otomatik yeniden deneme kurma. Kaçırılan tetiklemeler telafi edilmez, 7 günde ölür, oturumun açık ve boşta olmasını gerektirir.<br>Ayrıca **kontrolsüz yeniden deneme döngüsü zararın kendisidir** — buradaki zarar, haftalık kotanın sessizce yenmesidir. | birincil | aile koştu, hüküm yok |

---

## §12 — Öğrenme sırası

*Sıra bir **ön koşul zinciridir**: her kavram bir öncekinin çözemediği problemi çözer. Kaynakların hepsi bu koşumda birincil kaynaktan doğrulandı ve hepsi ücretsiz + web erişimli.*

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **L16** | **Teslim garantileri** (ön koşul yok): *"İş tekrarlanabilir mi, kaybolabilir mi?"* sorusunu yanıtlanabilir kılar; diğer her kavramın çerçevesidir.<br>Ajan karşılığı: kesilen ajanı yeniden çalıştırmak at-least-once seçmektir; çalıştırmamak at-most-once seçmektir.<br>Kaynak: Kafka `design.md`, "Message Delivery Semantics" — yaklaşık 15 dakika. | birincil | aile koştu, hüküm yok |
| **L17** | **Idempotency ve idempotency key** (ön koşul L16): at-least-once'ı yaşanabilir kılan **tek** şeydir; tekrar zararsızsa tekrardan korkulmaz.<br>Ajan karşılığı: ajanı iki kez koşturmak sistemi bozmuyorsa, kesilme **felaket değil gecikmedir**.<br>Kaynak: Temporal `activity-definition.mdx` — yaklaşık 10 dakika. | birincil | aile koştu, hüküm yok |
| **L18** | **Write-ahead log ve checkpoint** (ön koşul L17): WAL kalıcılığı **ucuz** yapar (sıralı append), checkpoint kurtarmayı **kısa** yapar.<br>Ajan karşılığı: *"her bulguyu bulunca yaz"* WAL'dır; *"bölüm bitti, özet çıkar"* checkpoint'tir. İkisi farklı şeydir; karıştıranlar ya çok yazar ya hiç yazmaz.<br>Kaynak: PostgreSQL `wal.sgml` — yaklaşık 20 dakika. | birincil | aile koştu, hüküm yok |
| **L19** | **Retry politikaları, timeout, heartbeat** (ön koşul L17-L18): ne zaman ve kaç kez tekrar denenir; ve *"hâlâ çalışıyor mu yoksa öldü mü?"*<br>Ajan karşılığı: heartbeat, **ilerleme yükü taşıyan kalp atışıdır**; ajanın periyodik ara durum bildirmesi tam olarak budur.<br>Kaynak: Temporal `detecting-activity-failures.mdx` ve Celery `faq.rst` (*"otomatik retry ne zaman zararlı"* — nadir bir birincil metin). | birincil | aile koştu, hüküm yok |
| **L20** | **Durable execution: event history, replay, determinizm** (ön koşul L16-L19): öncekileri tek programlama modelinde birleştirir.<br>Kesin ayrım çizgisi: **LLM çağrısı Activity'dir** (kaydedilir, replay edilmez); **akış kontrolü Workflow'dur** (deterministik, replay edilir). Bu, ajan iş akışı tasarımının omurgasıdır.<br>Kaynak: Temporal `understanding-temporal.mdx`, sonra `workflow-definition.mdx` (alanın en yoğun tek sayfası), sonra Go **ve** TypeScript basics — aynı problemin iki farklı çözümüdür, fark öğreticidir. | birincil | aile koştu, hüküm yok |
| **L21** | **Continue-As-New ve Saga** (ön koşul L20): birincisi sonsuz uzun bir işin geçmişinin nasıl sınırlanacağını, ikincisi geri alınamaz adımların nasıl geri alınacağını çözer.<br>Ajan karşılığı: birincisi *"tek dev ajan yerine zincir"*tir (U9); ikincisi **yalnız publish/push sınırında** geçerlidir.<br>Kaynak: Temporal `continue-as-new.mdx` ve `saga-pattern.mdx`. | birincil | aile koştu, hüküm yok |
| **L22** | **Claude Code'un kendi dayanıklılık yüzeyi** (paralel okunabilir): kavramların bu sistemdeki karşılıkları; §4 teşhis kılavuzunun dayanağıdır.<br>Kaynak sırası: `sessions` → `sub-agents` → `agent-sdk/sessions` → `checkpointing` → `errors` → `costs` — yaklaşık 90 dakika. | birincil | aile koştu, hüküm yok |
| **§12.1** | Sıranın en önemli atlaması **L20'dir**. Determinizm kısıtı, L16-L19 anlaşılmadan **keyfî** görünür; anlaşıldıktan sonra **kaçınılmaz** görünür. | çıkarım | aile koştu, hüküm yok |
| **§12.2** | *"`Date.now()` ve `random()` durable execution'da yasaktır"* önermesi **yanlıştır**.<br>TypeScript SDK'da bunlar deterministik sürümleriyle **değiştirilir** ve doğrudan kullanılabilir; Go SDK'da API ikamesi gerekir (`workflow.Now()`).<br>Ayrıca Side Effect kaçış kapağı vardır: non-determinizm **yasaklanmıyor, kaydediliyor**.<br>Doğru genel ilke: yasak olan `random()` değil, **kayıt dışı non-determinizmdir**. | birincil (çelişki) | aile koştu, hüküm yok |
| **§12.3** | *Designing Data-Intensive Applications* bu alanın standart tek cilt referansıdır, **ama ücretlidir** ve bu koşumda içeriği **doğrulanamadı**. Bölüm eşlemesi verilirse bu bir **kestirim** olur.<br>Sıra: L16-L21 ücretsiz birincil kaynaklardan bitirildikten **sonra**; kitap **sentezdir, giriş değildir**. | kestirim | aile koştu, hüküm yok |
| **§12.4** | Erişim taktiği: bu ailede kapalı siteler (`postgresql.org`, `kafka.apache.org`, `sqlite.org`) **kaynak depolarından** okundu ve bu, kanıt kalitesini **düşürmedi — yükseltti**.<br>PostgreSQL WAL dokümanı `postgres/postgres` içindeki `wal.sgml`'den, Kafka teslim semantiği `apache/kafka` içindeki `docs/design/design.md`'den alındı. | ölçüm | aile koştu, hüküm yok |

---

## §14 — Açık borçlar

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **C1** | ~~Antitez bu aile için koşulmadı~~ ⇒ **KAPANDI 2026-07-26.** Antitez araçlı koştu (48 araç çağrısı) ve **4 gerçek hata** buldu (K11-K14) ile 5 daraltma üretti.<br>Yeni borç: **K14'ün öncülü doğrulanacak** — bir `Explore` ajanı açılıp dönen nesnede agent ID olup olmadığına bakılacak. | — | kapandı |
| **C2** | ~~Sürüm çatalı borcu~~ ⇒ **KAPANDI, OLUMSUZ YÖNDE.**<br>Kurulu ikili **v2.1.42**, dokümanlar yaklaşık **v2.1.217**'dir. Dokümandaki asılma davranışı bu makinede **geçerli değildir** — *"olmayabilir"* değil, ölçüldü.<br>İki bağımsız ölçüm yakınsadı: antitez kurulu `cli.js`'te `watchdog`, `idleAgent`, `stuckDetection`, `hungTask` ve `healthCheck` terimlerinin **hiçbirini** bulamadı; §3.1 canlı vakasında üç ajan **45 dakika** sessiz kaldı ve belgelenmiş **10 dakikalık** eşiğe rağmen abort edilmediler.<br>Sonuç: **asılma nöbetçisi bu sürümde yoktur** ⇒ hiçbir otomatik koruma yoktur; asılma tespiti tamamen ebeveynin işidir.<br>⚠️ Bu, listeden bir madde silmek değil, **bir güvencenin kaybıdır**. | ölçüm | kapandı → H34 + §3.1 |
| **C3** | 429 ölümünün canlı imzası **gözlenmedi**: 115 transkriptte terminal API hatalarının **17'sinin 17'si de** oturum limitiydi.<br>429'un `stop_reason` imzasının aynı olup olmadığı **ampirik doğrulanmadı**; aynı kod yolundan geçtikleri için aynı olması **beklenir** — ama bu bir beklentidir. | kestirim | aile koştu, hüküm yok |
| **C4** | Pro ve Max için **sayısal tahsisat hiçbir açık dokümanda yoktur**.<br>Dokümanlar bilinçli olarak yalnız **pencere yapısını** yayımlıyor, **büyüklüğünü** değil. | birincil (yokluk) | aile koştu, hüküm yok |
| **C5** | `blocking_limit` ve `rapid_refill_breaker` **tanımsızdır**: SDK enum'unda yalnız **değer olarak** geçerler. Kota koruma mekanizmaları oldukları bir **kestirimdir**. | kestirim | aile koştu, hüküm yok |
| **C6** | Oturum penceresinin **token mi mesaj mı** ölçtüğü belgelenmemiştir. `used_percentage` yüzde verir, paydası tanımsızdır. Token ağırlıklı olması kuvvetle muhtemeldir — bu da **kestirimdir**. | kestirim | aile koştu, hüküm yok |
| **C7** | HTTP `Idempotency-Key` IETF taslağına **erişilemedi**. Kavramın kendisi Temporal'dan birincil kaynakla karşılandı; **standart başlık semantiği** (anahtar ömrü, çakışma, 409) **doğrulanamadı** ⇒ L17'de boşluk.<br>⚠️ Bu bir **"aranamadı"** vakasıdır, "yok" değil. | — (erişilemedi) | aile koştu, hüküm yok |
| **C8** | Alt-ajan token'ının ana oturum token'ıyla **aynı katsayıyla** sayılıp sayılmadığı bilinmiyor. *"Aynı kotadan yer"* belgelidir; katsayı belirtilmemiştir. | — (belgelenmemiş) | aile koştu, hüküm yok |
| **C9** | Antitezin test **edemediği** iddialar: API token-bucket iç mekaniği, ITPM kovalarının sayısal tahsisatı, Batch ayrıntıları ⇒ `platform.claude.com` **erişim listesinde değildi**. Ne doğrulandı ne çürütüldü.<br>Temporal ve durable execution teorisi ⇒ kapsam dışı, birincil kaynaklar kapalı.<br>⚠️ Bunlar **"aranamadı"**dır, "bulunamadı" değil. | — (erişilemedi) | test edilemedi |

---

## §15 — Fikir kutusu adayları

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **V68** | `.md` doğrudan çekim kuralı: `code.claude.com` ve `platform.claude.com` için **daima `.md` son ekiyle ham çekim** yapılır; WebFetch özeti alanları **sessizce düşürür**.<br>İki bağımsız vakada doğrulandı (`api_retries_exhausted`, env-vars varsayılanları). Atlas brifinglerine standart madde adayıdır. | birincil | aile koştu, hüküm yok |
| **V69** | *"İskelet önce"* ajan protokolü: ajan ilk bulguyu bulur bulmaz kısa bir **metin** üretsin.<br>Kayıp modunu *"her şey gitti"*den *"kısmi döndü"*ye çevirir; maliyeti sıfırdır. Ajan görev şablonuna **zorunlu madde adayıdır**. | birincil | aile koştu, hüküm yok |
| **V70** | Dalga zarfı sabiti: §9'un reçetesi (10 ajan, Sonnet, orta effort, en fazla 2 WebSearch, 2-3 saniye aralı) KILAVUZ'a sayısal kural olarak girmeye adaydır.<br>V59'un mekanizması artık elimizdedir: *"ucuz model"* tavsiyesi aslında **ayrı ITPM kovası açma** hamlesiymiş. | birincil | gerekçesi K13 ile düzeltildi; sayı korunur |
| **V71** | ⛔ **GERİ ÇEKİLDİ.** *"Sürdürülemez ajan yasağı: `Explore`/`Plan` uzun ve pahalı işlerde kullanılmasın."*<br>Dayanağının birincil kaynak olduğu iddiası **doğrulanamadı**; antitez dokümanda karşılığını bulamadı. **Aday olarak kutuya girmez** — önce öncül doğrulanır. | kestirim | ⛔ geri çekildi → K14 |
| **V82** | **Bildirim beklenmez, transkript büyümesi örneklenir.**<br>Uzun koşumlarda `task_notification` beklemek **yanlış sinyaldir**, çünkü bildirim hiç gelmeyebilir (§3.1). Bunun yerine transkriptin değişiklik zamanı ve satır sayısı periyodik olarak örneklenir.<br>Ölçüm **iki `stat` çağrısıdır**; maliyeti sıfırdır. | ölçüm | — (yeni) |
| *(numarasız)* | **"Liste başı kanıt kapısı"** — V numarası bilerek verilmedi; m.41 gereği bu yüzey öneri üretir, kanon kilitlemez. Numarayı Salih atar.<br>Kural: bir tavsiye listenin **birinci sırasındaysa**, dayanağı **bağımsız olarak doğrulanmış** olmalıdır.<br>**Üç bağımsız vakası vardır:** K14 (Explore/Plan sürdürülemezliği), K35 (eksen başına 4 kategori), K39 (ajan yayımlama eşiğini geçemez). Üçü de doğrulanmadan öne çıkarıldı; üçü de antitezde düştü. | çıkarım | — (yeni) |

---

## §16 — Kapanış

| # | Önerme (sözel) | Kanıt | Antitez |
|---|---|---|---|
| **§16.1** | Aile A25, A26 ve A27'dir ve **antitez koştu** (2026-07-26, araçlı, 48 araç çağrısı).<br>Sonuç: **4 gerçek hata** (K11 `is_error` çelişkisi, K12 cache, K13 eşzamanlılık, **K14 Explore/Plan askıda**), 5 daraltma (K15-K18, H16) ve 5 doküman doğrulamalı *"sağ çıktı"* damgası. | ölçüm | — |
| **§16.2** | Genel kuralda *"sağ çıktı"* damgası **"aynı-aile hakemi karşısında sağ kaldı"** anlamına gelir, çünkü antitez ajanları tez ajanlarıyla aynı model ailesindendir.<br>**Bu aile bu şerhten muaftır**: kanıt modelin belleğinden değil, ham dokümandan ve kurulu koddan geldi. | çıkarım | — |
| **§16.3** | Bu ailenin kanıt tabanı oturumun **en güçlüsüydü** — kurulu `cli.js` zod şemaları, 115 alt-ajan transkripti, ham doküman markdown'ı.<br>**Ve buna rağmen 4 hata çıktı** ⇒ güçlü kanıt tabanı, hata yokluğu **demek değildir**. | çıkarım | — |
| **§16.4** | Salih'in sorusuna doğrudan cevap: ajanlar **`stopped` olmadı**; `failed` oldular, ve `failed` **terminal değildi**.<br>Kök neden ajanlarda değil, **koşum zarfının aşılmasındaydı**. | ölçüm ∧ çıkarım | — |
