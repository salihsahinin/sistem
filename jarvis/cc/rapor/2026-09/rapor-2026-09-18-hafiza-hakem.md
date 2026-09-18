# Maskeli hakem raporu — kalıcı ajan hafızası (tez A/B/C + antitez A/B/C + V26 denetimi)

**Tarih:** 2026-09-18 (sistem saati) · **Rol:** maskeli hakem, bağımsız · **Effort:** medium · **Dil:** Türkçe
**Girdi:** 6 üretici rapor + V26 örneklem-denetimi (48 sondaj, 38 `TUTTU`, 5 `TUTMADI`, 5 `URL YOK`).
**Hakemin kendi doğrulaması:** 3 WebFetch (bütçe 8/3 kullanıldı): `platform.claude.com/docs/en/build-with-claude/context-editing`, `anthropic.com/engineering/multi-agent-research-system`, `code.claude.com/docs/en/memory`. Tüm çekimler 2026-09-18.

## Usul beyanı

- **Maskeleme:** iddialar tez/antitez etiketiyle değil, iddia + kanıt gücü olarak tartıldı. Üretici raporların kendi hükümleri (`ÇÜRÜTÜLEMEDİ`/`DARALDI`/`ÇÜRÜDÜ`) girdi sayıldı, hüküm sayılmadı.
- **V26 tavanı:** `TUTMADI` ≥1 olan raporların (tez-A, tez-C, antitez-A) bulguları en fazla `K`. **İstisna:** hakemin kendi WebFetch'iyle birincil kaynaktan birebir doğruladığı üç nokta tavandan muaf (bağımsız doğrulama = yeni kanıt).
- **Etiket:** `D` = birincil kaynakta birebir ∧ güncel kuşak (2025-Q3 sonrası ∧ 4.x+/5) ∧ adversarial turda ayakta · `K` = doğrulandı ama tek-kaynaklı / yazar-taraflı / ikincil / eski kuşak / AS-OF eksik · `X` = çürüdü ya da dayanaksız.
- **AS-OF kuralı:** AS-OF ya da model sürümü olmayan iddia en fazla `K` ve tasarım girdisi olarak düşer.
- **Sağlamlık** = adversarial hayatta kalma, popülerlik değil.

### V26 düzeltmeleri (ilgili iddiaya işlendi)

| Düzeltme | Doğru hâli | Etkilenen iddia |
|---|---|---|
| MEMORY.md "otomatik kısaltma" | Dosya kendiliğinden kısaltılmaz. Sınıra yakınken uyarı, sınır aşılınca yazma başarılı olur ama hata döner ve **limit üstü kısım sonraki yüklemede düşer** (hakem fetch'iyle birebir teyitli) | tez-A #2 |
| Mem0 "4 aşama" | Akademik kaynak 2 faz, güncel resmi doküman 3 aşama, **4 olan şey operasyon sayısı** (`ADD`/`UPDATE`/`DELETE`/dokunma) | tez-A #11 |
| Gloaguen "~%3 düşüş" | Gerçek: **%0,5** (SWE-bench Lite) ve **%2** (AGENTbench); maliyet artışı **+%20** doğru | tez-C #10 |
| antitez-B'nin MemoryOS "DARALDI" hükmü | **Hatalı.** 32+ sn gecikme ve 1,3M-7,04M token rakamları arXiv:2602.19320 Tablo 5'te birebir var; antitez yanlış makaleyi (2506.06326) aradı. İddia **sağlam** sayılır | tez-B #7 |

---

## (i) Katman × mekanizma × hüküm

| Katman | Yazma tetiği | Yazar | Sıkıştırma / unutma | Fren | Güncel-kuşak kaynak | En güçlü kaynak (AS-OF · model) | Etiket |
|---|---|---|---|---|---|---|---|
| **Çalışma / oturum** | Eşik-tetikli: bağlam doluluğu sınıra yaklaşınca (compaction), her turda aday ölçümü (OpenAI). İndeks yazımı sonrası boyut ölçümü (Claude Code) | Sistem/harness otomatik (insan ve model kararı yok); indekse Claude | Compaction = özetle + yeni pencereyi özetle başlat. Context editing = eski tool-result'ları **sunucu tarafında** promptan düşür. İndekste limit üstü satır sessizce düşer | Ölçüm-tetikli eşik (200 satır / 25 KB indeks; ~%83,5 oto-sıkıştırma, ~%60 proaktif). İnsan onayı **yok** | 5 (4 `D`, 1 `K`) | `code.claude.com/docs/en/memory` (çekim 2026-09-18 · Claude Code v2.1.2xx) | `D` |
| **Epizodik** | Olay bitince ya da oturum sonunda toplu aktarım; bazı sistemlerde her mesaj çiftinde çıkarım | Model (self-write) ya da ayrı arka-plan yöneticisi | Konsolidasyon + çelişki çözümü; zaman damgası (`modified` alanı) ile bayatlık ölçümü | Köken zinciri (yazar kimliği + türetme yolu), kapsam denetimi. Frensizlik ölçülmüş arıza üretti: çelişki tespiti **%49**'a düştü | 4 (3 `D`, 1 `K`) | `arxiv.org/html/2602.19320v1` (2026-02-22 · gpt-4o-mini, Qwen-2.5-3B) | `D` |
| **Semantik / çekirdek** | **Toplu (batch)**: tek olayda değil, veri birikince örüntü ayrıştırılır | Ajan önerir, **insan kabul eder** (pratisyen deseni); ürünlerde model doğrudan yazar | Sabit token tavanı, yeni satır girerse eski satır çıkar. Türetilebilir içerik (dizin listesi, mimari özeti) budanır, gerekçe ve tuzak kalır | Bütçe (örnek 5.000 token, yazarın kendi ifadesiyle illüstratif) + insan incelemesi. Ölçülmüş zarar: **%0,5-%2** başarı düşüşü, **+%20** maliyet, zarar özellikle depo-özeti bölümlerinde | 4 (2 `D`, 2 `K`) | `arxiv.org/html/2602.11988v1` (2026-02-12, rev 2026-06-23 · Sonnet 4.5, GPT-5.2, GPT-5.1-Mini, Qwen3-30B) | `D` |
| **Prosedürel / skill** | Koşullu: yalnız ilgili göreve girildiğinde yüklenir. Deterministik tetik için araç-öncesi/sonrası hook | İnsan yazar (skill gövdesi), ajan çağırır | Bağlamda sürekli durmaz, çağrıda yüklenir (sıkıştırma yerine **yüklememe**) | Hook deterministik, talimat değil. Hook'un kendi arızası ölçüldü: küçük bütçede **18 dersin 2'si** görünüp kalanı sessizce düştü, düzeltme = kesilme bildirimi satırı | 4 (1 `D`, 3 `K`) | `code.claude.com/docs/en/memory` (çekim 2026-09-18 · v2.1.2xx) skills pointer'ı | `D` |
| **Paylaşılan / çok-ajan** | Alt-ajan kendi dizinine yazar; paylaşımda kapsam (fleet) kuralına göre | Her ajan kendi yazarı; paylaşılan bankada tek yazıcı ya da kapsam kuralı | Alt-ajan yalnız **1.000-2.000 token** özet döndürür; ayrıntılı iz üst ajana geçmez | İzolasyon varsayılan: ana konuşmanın oto-hafızası alt-ajana yüklenmez (fork istisna), alt-ajanın hafızası **ayrı dizin**. Doğru uygulanan yönetişimde fleet-dışı sızıntı **0/80**, görünürlük **117/120** | 4 (2 `D`, 2 `K`) | `arxiv.org/html/2606.24535v1` (2026-06-23 · model sürümü verilmemiş, üretim harness) | `D` |

**Satır notu (çalışma/oturum):** tez-A #6 (`context editing = istemci taraflı`) hakemin kendi fetch'iyle **çürüdü**: dedike sayfa birebir "Context editing is applied server-side before the prompt reaches Claude" diyor ve istemci tam geçmişi korur. Anthropic'in memory-tool sayfası tersini yazıyor, yani **satıcının iki resmi sayfası kendi içinde çelişiyor**; dedike sayfa birincil sayılır. Tasarım sonucu: sunucu tarafı düzenleme, ajanın kendi disk kaydını silmez, iki katman ayrıdır.

---

## (ii) Mevcut düzenin 8 bileşeni ↔ literatür karşılığı

| # | Bileşen | Literatür karşılığı | Hüküm | Gerekçe (kaynak sayısı) | Etiket |
|---|---|---|---|---|---|
| 1 | **Kapsül** (sıcak, FIFO 8 madde → arşiv) | Her seans yüklenen indeks + compaction özeti; ölçüm-tetikli bütçe | **değişmeli** | FIFO madde-sayısı yerine **ölçüm-tetikli bütçe** (satır/KB) + düşen maddenin arşiv kanıtı. ≥2 güncel kaynak: Claude Code indeks limiti ve sessiz düşme (çekim 2026-09-18, `D`), Kun Chen sabit token tavanı (2026 içi, `K`), oto-sıkıştırma eşiği %83,5 (2026-04-06, `K`) | `D` |
| 2 | **Pano** (kart) | Birebir karşılık **yok**; en yakını ajan durum-scratchpad'i (ADK `State`) | **belirsiz** | Literatür kart-yüzeyinin getirisini ölçmüyor; ≥2 güncel kaynak şartı karşılanmıyor. İç ölçüme düşer | `K` |
| 3 | **Karar defteri** (hüküm kaydı, kural yalnız insan imzasıyla) | Epizodik + **köken (provenance)**: yazar kimliği, türetme zinciri, zaman damgası | **eklenmeli** | Kayda **yazar kimliği + model sürümü + AS-OF** alanı. ≥2 güncel kaynak: köken zinciri 50/50 derinlik-4 zincir doğru yeniden inşa, p50 291 ms/hop (2026-06-23, `D`); Claude Code `modified` frontmatter damgası v2.1.214+ (çekim 2026-09-18, `D`) | `D` |
| 4 | **Fikir kutusu** | Toplu (batch) inceleme kuyruğu + insan kabul kapısı | **korunmalı** | Pratisyen deseniyle birebir örtüşüyor: "tek örnekle gürültü ile örüntü ayrılmaz", "ben incelemeden hiçbir şey yazılmaz". Tek pratisyen kaynağı, yazarın kendi aracı (`K`) | `K` |
| 5 | **Çekirdek desenler** (10 koşumda yeniden-oluşum, ekleme insan kabulüyle) | Semantik + prosedürel damıtma; batch-tabanlı örüntü onayı | **korunmalı** | Mekanizma desteklenir, **eşik rakamı (10) literatürde yok**. Damıtmanın nicel getirisi bu taramada yanıtsız kaldı (iki makalenin tabloları PDF'ten çıkarılamadı, sayı alınmadı) | `K` |
| 6 | **Bronz → silver → gold** | Ham epizodik kütük → çıkarım/konsolidasyon → görünüm; Mem0 ve LangMem arka-plan yöneticisiyle aynı şekil | **eklenmeli** | Boruya **sessiz-arıza sayacı**: yapılandırılmış hafıza yazımı zayıf modelde sessizce bozuluyor (format hatası %30,38 Qwen-2.5-3B, %17,91 gpt-4o-mini, `D`); ayrıca kopya-kapısının çelişki dedektöründen önce çalışması tespit oranını %49'a düşürüyor (`D`). İki güncel kaynak şartı karşılanır | `D` |
| 7 | **Harness memory** (`~/.claude/projects/<proje>/memory/`, MEMORY.md indeks) | Ürün-özelliğiyle **birebir aynı şey** (eşleme değil, kimlik) | **korunmalı** (+1 beyan) | İndeks 200 satır/25 KB, konu dosyaları talep üzerine, alt-ajan ayrı dizin, oto-hafıza dosyaları temizlik süpürmesinden **hariç** (silme yasağıyla uyumlu). Hakem fetch'iyle birebir (`D`). Eklenecek beyan: bu dizin **depo dışında ve makine-yerel**, yani açık-kaynak görünürlük ilkesinin dışında kalıyor (bkz. bölüm vii) | `D` |
| 8 | **Skill** (koşullu bilgi) | Prosedürel hafıza, talep üzerine yükleme; deterministik tetik için hook | **korunmalı** | Resmi doküman ayrımı birebir kuruyor: her seans duran içerik kurala, koşullu içerik skill'e. Hook, talimattan güçlü fren olarak ayrıca adlandırılıyor (`D`) | `D` |

**Eşleme özeti:** korunmalı 4 (kutu, çekirdek, harness memory, skill) · eklenmeli 2 (karar defteri köken alanı, bronz→silver sessiz-arıza sayacı) · değişmeli 1 (kapsül bütçesi) · belirsiz 1 (pano).

---

## (iii) Kendini-geliştiren hafızanın frenleri

**1. İnsan onayı.** En dikkat çekici bulgu: **insan onayının getirisine dair ölçüm yok.** Aranan üç kaynakta da boşluk doğrulandı: yönetişim makalesi (arXiv:2603.11768, 2026-03) kendi ifadesiyle "belirli bir yazılım uygulaması değil, teorik mimari" ve üç hipotezini yürütmemiş; güvenlik taraması insan-döngü etkisini ölçmüyor; kendini-geliştiren ajan taraması yalnız normatif öneri veriyor. İncelenen **yedi üründen hiçbirinde** hafıza yazımında zorunlu insan onayı yok. Zorunlu onay yalnız **pratisyen** tarafında görülüyor (Kun Chen: öneri listesi, her madde tek tek kabul ya da ret). Hüküm: insan onayı **normatif olarak destekli, ampirik olarak ölçülmemiş** (`K`). Jarvis kanonundaki "kural yalnız insan imzasıyla" kuralı literatürden **ileride**, literatürce çürütülmüş değil.

**2. Bütçe.** Ölçülmüş ve `D`:
- İndeks bütçesi 200 satır / 25 KB; aşımda yazma başarılı, **hata döner**, limit üstü sonraki yüklemede düşer.
- Her zaman yüklenen dosya için sabit token tavanı (örnek 5.000; yazarın kendi ifadesiyle "for example", zorunlu değer değil).
- Ampirik ortalama: AGENTS.md 142 satır, CLAUDE.md 287 satır, Copilot yönergesi 310 satır.
- Bütçe freni **kendi arızasını üretir**: küçük geri-çağırma bütçesinde ajan 18 eşleşen dersten yalnız 2'sini gördü ve kalan 16'nın varlığını bilemedi. Düzeltme, kesilmeyi bildiren tek satırlık not oldu. Ders: **her bütçe kesmesi görünür olmalı.**

**3. Ölçülmüş getiri ve zarar.**

| Ölçüm | Değer | Kaynak (AS-OF · model) | Etiket |
|---|---|---|---|
| Hafıza aracı + bağlam düzenleme birlikte | **+%39** temel çizgiye göre | claude.com/blog/context-management (2025-09-29 · Sonnet 4.5) | `D` |
| Yalnız bağlam düzenleme | **+%29** (fark olan 10 puan hafıza aracından) | aynı | `D` |
| 100 turluk arama görevinde token | **-%84** | aynı | `D` |
| LLM-üretilen bağlam dosyası, başarı | **-%0,5** (SWE-bench Lite) / **-%2** (AGENTbench) | arxiv 2602.11988 §4.2 (2026-02 · Sonnet 4.5, GPT-5.2, Qwen3-30B) | `D` |
| Aynı çalışma, çıkarım maliyeti | **+%20'den fazla** | aynı | `D` |
| Aynı çalışma, nüans | Açık talimatlar iyi izleniyor; zarar **depo-özeti** bölümlerinden geliyor | aynı | `D` |
| Bağlam dosyalarının bayatlaması | **%50'si** ilk taahhütten sonra hiç güncellenmemiş (466 depo) | usewire.io (2026-05-18 · MSR 2026 verisi) | `D` |
| Yapılandırılmış hafızada sessiz arıza | %30,38 (Qwen-2.5-3B) / %17,91 (gpt-4o-mini) format hatası | arxiv 2602.19320 Tablo 4 (2026-02) | `D` |
| Hafıza inşa maliyeti | 1,3M-7,04M token; MemoryOS 32+ sn/tur | arxiv 2602.19320 Tablo 5 (2026-02) | `D` |
| Frensiz paylaşımda çelişki tespiti | **%49** (n=200); admission'a girenlerin 90/90'ı doğru çözüldü | arxiv 2606.24535 (2026-06) | `D` |
| Frensiz paylaşımda yetki sızıntısı | trust-1 ajan fleet-dışı satıra erişti; kesişim-dışı probların **%43,9'u** kısıtlı satır gösterdi | aynı | `D` |
| Doğru yönetişimde | sızıntı **0/80**, görünürlük **117/120 (%97,5)**, yazma-görünürlük p50 **0,83 sn** | aynı | `D` |
| Kendini-geliştiren hafıza mimarisi kazancı | +%25,7 (GPT-4o) / +%36,8 (GPT-5.1) rölatif F1 | arxiv 2605.13941 (2026-05 · GPT-4o, GPT-5.1) | `K` (yazar-taraflı, replikasyon yok) |
| Çok-ajan mimarisi kazancı | **+%90,2** iç araştırma değerlendirmesinde, ~**15×** token | anthropic.com/engineering/multi-agent-research-system (2025-06 · Opus 4 lider + Sonnet 4 işçi) | `K` (kuşak 2025-Q3 öncesi) |

**Kestirimle okunması gereken sentez:** hafıza mimarisinin getirisi modelin gücüyle **birlikte** ölçekleniyor. Küçük model + karmaşık yapılandırılmış hafıza = sessiz bozulma; güçlü model + aynı mimari = kazanç büyüyor. Bu sentez iki kaynağın yakınsamasından çıkar, tek bir kaynakta yazılı değil (`K`).

---

## (iv) Reddedilen ya da geri alınan mekanizmalar

| Mekanizma | Ne oldu | Kanıt gücü |
|---|---|---|
| LLM'e depo taratıp otomatik bağlam dosyası ürettirme (`/init` tarzı) | Başarıyı düşürüyor, maliyeti artırıyor. **Daraltma:** zarar bütün dosyada değil, **depo-özeti** bölümlerinde; açık talimatlar iyi izleniyor | `D` |
| Talimat-tetikli ders geri-çağırma | Hook-tetiğe geçildi. **Daraltma:** tek yönlü göç değil; hook desteklemeyen araçta görev-başı sorgu hâlâ kullanılıyor, yani araç yeteneğine göre paralel iki mekanizma. Hook'un kendi sessiz veri kaybı sonradan giderildi | `K` |
| Tek olaydan sonra anlık kanon güncellemesi | Toplu incelemeye çevrildi (tek örnekle gürültü ile örüntü ayrılmıyor) | `K` |
| Alt-ajan başına izole hafıza | Üçüncü parti bir katman bunu kasten kırıp tek paylaşımlı banka kuruyor. **Uyarı:** kaynak, ürünü satan tarafın kendi yazısı (çıkar çatışması); harness'in kendi varsayılanı hâlâ izolasyon | `K` |
| "Mem0 dört aşamalı pipeline" anlatısı | **Reddedildi.** Akademik kaynak 2 faz, güncel doküman 3 aşama, 4 olan operasyon sayısı | `D` |
| "Bağlam düzenleme istemci taraflıdır" tarifi | **Reddedildi.** Dedike sayfa sunucu taraflı diyor; satıcının ikinci sayfası çelişiyor | `D` (hakem fetch'i) |
| MemGPT'nin `core/recall/archival` adlandırması | Canlı dokümantasyonda bu üçlü doğrulanamadı (`/memory/overview` 404); güncel terim seti "memory blocks / shared memory / archival memory". Üçlü adlandırma **eski kuşak** (2023) terminolojisi | `K` |
| SDK taraflı compaction | Satıcı sunucu taraflıyı öneriyor, `compaction_control` parametresi TypeScript ve Ruby SDK'larında **deprecated** | `D` (hakem fetch'i) |

---

## (v) Hayatta kalma: 36 iddia

| Aile | Sağlam | Daralan | Düşen | Düşen/daralan kalemler |
|---|---|---|---|---|
| **A** (harness/ürün) | 6 | 4 | **2** | Düşen: #6 bağlam düzenleme yönü ters · #11 Mem0 "4 aşama". Daralan: #2 indeks aşım mekanizması, #7 stream bloke iddiası, #10 Letta 3-katman adlandırması, #12 LangMem üçlü ayrımı |
| **B** (akademik) | **12** | 0 | 0 | Yok. #7 antitez tarafından daraltılmıştı, V26 denetimi bu daraltmayı hatalı buldu ve iddia **geri yükseltildi** |
| **C** (pratisyen) | 9 | 3 | 0 | Daralan: #3 "sabit" bütçe değil illüstratif örnek · #10 %3 yerine %0,5-%2 ve zarar yalnız depo-özetinde · #11 tek yönlü göç anlatısı yanlış |
| **Toplam** | **27** | **7** | **2** | 36/36 |

**Etiket dağılımı (V26 tavanı uygulanmış hâliyle):** `D` 14 · `K` 20 · `X` 2. Aile A ve aile C iddiaları raporlarındaki `TUTMADI` nedeniyle tavanla `K`'ye iniyor; hakemin kendi üç fetch'iyle doğruladığı noktalar (indeks limiti ve sessiz düşme, alt-ajan izolasyonu, bağlam düzenlemenin sunucu tarafı, `modified` damgası, skills ayrımı) tavandan muaf ve `D`.

**Aile dayanıklılığı sıralaması:** B > C > A. Aile B'nin tek zayıflığı kaynak türü (EvolveMem rakamları makalenin kendi ölçümü, bağımsız replikasyon yok), aile A'nın zayıflığı satıcı dokümantasyonunun **kendi içindeki tutarsızlığı**.

---

## (vi) İç ölçüme kalanlar

Literatür bu altı soruya rakam vermiyor; Jarvis kendi koşumundan ölçmek zorunda.

1. **Kapsül eşiği:** FIFO 8 madde mi, satır/KB ölçümü mü? Dışarıda madde-sayısı eşiği kullanan tek örnek yok, hepsi boyut ölçüyor.
2. **Çekirdek desen eşiği:** "10 koşumda yeniden-oluşum" rakamının dışarıda karşılığı yok. Batch ilkesi destekli, sayı iç ölçüm.
3. **İnsan onayının getirisi:** dünyada ölçülmemiş. Jarvis'in onaylı ve onaysız yazma turlarını karşılaştıran iç A/B, dışarıda olmayan bir veri üretir.
4. **Damıtmanın nicel getirisi:** bu taramada yanıtsız kaldı (iki makalenin tabloları çıkarılamadı). Silver kuyruk boyut-öncesi/sonrası ölçümü iç veriden gelir.
5. **Sessiz arıza oranı:** bronz→silver yazımında format hatası oranı, dışarıdaki %17,91-%30,38 bandıyla kıyaslanabilir tek sayı.
6. **Pano kartlarının okunma oranı:** bileşen 2'nin hükmü "belirsiz"; yalnız iç `v_okuma_orani` benzeri ölçüm karara götürür.

---

## (vii) m.16 çelişkileri

**Çelişki 1 — "Ajan hafızaya yazar, kurala yazamaz" ile ürünlerin oto-hafızası.**
Bulgu: harness oto-hafızası Claude'un kendi yazdığı, her seansa yüklenen ve davranışı yönlendiren dosyadır. Yüzeyde kural yazıyor gibi görünür.
Çözüm (çelişki **yok**, ayrım keskinleştirilmeli): resmi doküman ayrımı zaten kuruyor. Hafıza ve kanon dosyaları "bağlamdır, dayatılan yapılandırma değildir"; bir eylemi **modelin kararından bağımsız** engellemek isteniyorsa mekanizma hook'tur. Yani Jarvis'teki `PreToolUse` teli **gerçek kural katmanı**, kanon dosyası ise güçlü bağlamdır. Öneri: kanona tek satırlık ayrım eklensin, "kural = hook ∨ Salih imzalı kanon; hafıza = ajanın kendi yazdığı, davranışı yönlendiren ama dayatmayan kayıt". Kural değişikliği değil, mevcut kuralın netleşmesi.

**Çelişki 2 — "Silme yasağı" ile literatürdeki unutma mekanizmaları.**
Bulgu: Mem0 `DELETE` operasyonu, arka-plan konsolidasyon, indeks limitinde **sessiz düşme**, "bayat girdileri birleştir ya da düşür" yönergesi. Hepsi silme yasağıyla yüzeyde çelişir.
Çözüm: yasak korunur, çünkü kanon zaten "sıcak yüzeyden düşürme ≠ silme, arşiv + pointer" diyor. Gerçek arıza silme değil **sessizlik**: indekste limit üstü satır kimseye haber vermeden düşüyor, geri-çağırma bütçesi kesince ajan kesildiğini bilmiyor (18 dersten 2'si vakası). Öneri: silme yasağına **görünürlük şartı** eklensin, "hiçbir düşürme sessiz olamaz; her düşürme arşiv pointer'ı + kesilme bildirimi üretir". Bu, yasağı gevşetmez, sıkılaştırır.

**Çelişki 3 — Açık kaynak/görünürlük ilkesi (Katman-1) ile harness hafızasının konumu.**
Bulgu: oto-hafıza dizini depo dışında, makine-yerel, makineler arası paylaşılmıyor, git'te görünmüyor. "Jarvis'in her hareketi bu klasörde görünür düz dosyadır" ilkesiyle doğrudan çelişir.
Çözüm **Salih imzası ister** (Katman-1): `autoMemoryDirectory` ayarı ile dizin depo içine alınabilir (resmi doküman, `D`), ama bu md.49 sınırı ve gizlilik ile çakışır (üçüncü şahıs verisi hafızaya düşerse depoya girer). Hakem hüküm vermez, kalem masaya çıkar.

---

## (viii) Masa kalemi taslağı — mevcut düzene ilk eklenecek/değişecek mekanizma

**Karar sorusu:** Hafıza düzenine ilk hangi mekanizma eklenir ya da değişir?

### Seçenek A — Sessiz düşme freni: ölçüm-tetikli kapsül bütçesi + düşürme kanıtı (**önerilen**)
- **Ne demek:** Kapsülün "FIFO 8 madde" eşiği, satır/KB ölçümüne çevrilir; sıcak yüzeyden düşen her madde arşiv pointer'ı üretir ve kapsülün sonuna tek satırlık kesilme bildirimi yazılır ("N madde arşive indi, adres: ...").
- **Ne yaparım:** Kapsül yazımından sonra koşan bir ölçüm adımı (satır ve KB), eşiğe yakınken uyarı, eşik üstünde düşürme + pointer + bildirim satırı. Mevcut kapanış ritüeline takılır, yeni yüzey gerekmez.
- **Artı:** İki bağımsız ölçülmüş arızayı birden kapatır (indeks limitinde sessiz düşme, bütçe kesmesinde sessiz veri kaybı). Silme yasağını gevşetmeden sıkılaştırır. Dışarıda aynı arızanın düzeltmesi zaten uygulanmış ve yayınlanmış, yani hazır desen.
- **Eksi:** Madde sayısı yerine boyut ölçmek kapsülün "8 madde" sezgisini bozar; ilk turlarda eşik kalibrasyonu iç ölçüm ister (dışarıda Jarvis'e uyan rakam yok).

### Seçenek B — Karar defterine köken alanı (yazar kimliği + model sürümü + AS-OF)
- **Ne demek:** Her defter bloğuna kimin yazdığı, hangi model sürümüyle ve hangi çekim tarihiyle yazıldığı alanı eklenir.
- **Ne yaparım:** Defter şablonuna üç alan; yazımda otomatik doldurma; sonradan "bu hüküm hangi kuşakta verildi" sorgusu mümkün olur.
- **Artı:** Anakronizm frenini ve rakam disiplinini veri düzeyinde zorunlu kılar. İki güncel `D` kaynağı destekliyor (köken zinciri ölçümü, ürünün `modified` damgası). Çok-ajanlı düzende yazar kimliğinin kaybı ölçülmüş bir arıza sınıfı.
- **Eksi:** Var olan defter bloklarına geriye dönük doldurma gerektirir (ya da "bu tarihten sonra" kesme çizgisi); tek-ajanlı bugünkü kullanımda getirisi gecikmeli.

### Seçenek C — Kanon dosyalarından depo-özeti bölümlerinin budanması
- **Ne demek:** Her zaman yüklenen dosyalardan koddan türetilebilir içerik (dizin listesi, mimari özeti) çıkarılır, yalnız tuzak, gerekçe ve varsayılandan sapan kural kalır.
- **Ne yaparım:** Kanon dosyalarını bu ölçütle tarayıp aday satır listesi çıkarırım, Salih imzalar.
- **Artı:** Tek `D` etiketli doğrudan zarar ölçümü bu alanda (+%20 maliyet, zarar depo-özeti bölümlerinde). Ölçüt dışarıda tanımlı ve uygulanmış.
- **Eksi:** Jarvis kanonu zaten ≤80 satır/≤7 KB ve pointer ilkeliyle yazılmış, yani **kazanılacak alan dar**; ölçülen zarar 142-310 satırlık şişkin dosyalarda gözlendi, buradaki düzene aktarımı doğrudan değil.

**Öneri gerekçesi:** A ilk sırada, çünkü tek başına iki ayrı ölçülmüş arıza sınıfını kapatıyor ve mevcut kanonun en sert kuralıyla (silme yasağı) çelişmek yerine onu uygulanabilir hâle getiriyor. B ikinci, çünkü getirisi çok-ajanlı düzen büyüdükçe artar. C üçüncü, çünkü ölçülmüş zarar gerçek ama bu depodaki kanon zaten o zararın bandının dışında.

---

## Sınırlar

- Yalnız verilen 7 dosya + 3 hakem WebFetch kullanıldı; deponun başka dosyası okunmadı (mevcut düzen tarifi emirdeki ≤1 KB özetten alındı, kanon dosyaları açılmadı).
- Aile B'nin sayısal omurgası üç makaleye dayanıyor ve EvolveMem rakamları makalenin kendi ölçümü; bağımsız replikasyon literatürü henüz yok.
- İnsan onayının etkisine dair **hiçbir** ampirik rakam bulunamadı; bu raporun en büyük boşluğu ve iç ölçümün en yüksek değerli kalemi.
- Çok-ajan üstünlüğü rakamı (+%90,2) 2025-06 kuşağından (Opus 4 / Sonnet 4), güncel-kuşak eşiğinin altında kalıyor, tasarım girdisi olarak `K`.
