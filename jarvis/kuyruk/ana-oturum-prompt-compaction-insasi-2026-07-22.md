# ANA OTURUM PROMPTU — blok: "compaction inşası"

> Salih: aşağıdaki `====` arasını ana oturuma **olduğu gibi yapıştır**. Üstündeki bu satır prompta dahil değil.
> Kaynak: Şerit 2 / P5+P6 (Context Engineering I–II), 2026-07-22. Bu prompt **ikinci-model denetiminden geçmiş** haldir: P6 oturumunun kendi bulgularından biri bu denetimde çürütüldü ve prompta düzeltilmiş olarak girdi.

====

Carvis, "compaction inşası" bloğunu açıyoruz. Bu, K-015'in (sıcak katman / bağlam mimarisi) somut inşa fazı. Girdi: Şerit 2'nin P5 (JIT yükleme, `@path` tuzağı) ve P6 (compaction, not-tutma, izolasyon) partisyonları. Devir dosyaları: `raporlar/vardiya/vardiya-teslim-2026-07-22-ogrenme-P5.md` ve `raporlar/vardiya/vardiya-teslim-2026-07-22-ogrenme-P6.md`, ders kayıtları `ogrenme/dersler/2026-07-22-P5-*` ve `2026-07-22-P6-*`.

**Bu promptun iddialarına güvenme.** Prompt bir öğrenme oturumunda üretildi, o oturum canon'a yazamaz ve bir bulgusu zaten geri çekildi. Aşağıdaki Faz A senin kendi doğrulaman; Faz A bitmeden Faz C'deki hiçbir hükmü kanona ya da senaryo-defterine geçirme.

## FAZ A — ARAŞTIRMA (m.40: mekanizma kararından önce dış araştırma; zorunlu)

Birincil kaynaklardan doğrula. Kaynak sayfalar (07-22'de erişildi):
- `https://platform.claude.com/docs/en/build-with-claude/prompt-caching`
- `https://code.claude.com/docs/en/context-window` (bölüm: "What survives compaction")
- `https://code.claude.com/docs/en/memory`
- `https://code.claude.com/docs/en/how-claude-code-works` (bölüm: "When context fills up")
- `https://code.claude.com/docs/en/sub-agents`

Cevaplanacak sorular — her birine **evet/hayır + birebir alıntı + URL**:

1. Prompt-cache geçersizleşmesi hangi granülerlikte çalışır: **blok** mu, satır mı? Prefix-hash kümülatif mi? "Cache hit için breakpoint'e kadar %100 aynılık" ifadesi hâlâ geçerli mi? Kaç breakpoint var, lookback penceresi kaç blok?
2. Katman sırası **tools → system → messages** mi? Bir üst katmandaki değişiklik alttakileri düşürüyor mu?
3. **CLAUDE.md sistem promptunun içinde mi, yoksa sistem promptundan sonra bir kullanıcı mesajı olarak mı** enjekte ediliyor? (Bu, "hangi dosya byte-stabil olmalı" sorusunun cevabını belirliyor.)
4. Compaction **iki aşamalı mı** — önce eski tool çıktılarının temizlenmesi, sonra konuşmanın özetlenmesi? Öyleyse oturum başında Read edilen bir dosyanın çıktısı hangi aşamada gidiyor?
5. "What survives compaction" tablosunu birebir çıkar: kök CLAUDE.md + unscoped rules, auto memory, `paths:` frontmatter'lı rules, nested CLAUDE.md, çağrılmış skill gövdeleri, skill listesi, sistem promptu — her biri ne oluyor? Skill kırpma limitleri (token/skill ve toplam) ve **kırpmanın dosyanın başını mı sonunu mu koruduğu** nedir?
6. CLAUDE.md'de compaction'ı yönlendiren bölümün **birebir başlığı** nedir, hangi başlık seviyesi, dosyanın neresine konuyor? `/compact <focus>` sözdizimi nedir? Auto-compact varsayılan açık mı, eşiği ayarlanabilir mi (`settings.json` anahtarı var mı)?
7. **Thrashing**: tek bir dosya/tool çıktısı çok büyükse ne oluyor, eşik/davranış nedir?
8. MEMORY.md sert limiti (satır ∨ KB) ve limit aşımında ne oluyor — sessiz düşme mi, hata mı, ikisi mi? Frontmatter/HTML yorumları sayılıyor mu?
9. `@path` import'ları eager mi, kaç hop, backtick kaçışı geçerli mi? (P5 hükmünün tazeliği.)
10. Sub-agent: kendi penceresi, ana konuşmayı görmemesi, yalnız özet döndürmesi, `fork` istisnası, `memory` alanı — hâlâ böyle mi? Ajan-takımı token çarpanı için resmî bir rakam var mı?

**Faz A çıktısı:** 10 maddelik doğrulama tablosu (iddia · doğrulandı/çürütüldü/bulunamadı · alıntı · URL · tarih). Bu tablo senaryo-defterine "07-22 CC-mekanik doğrulama koşumu" olarak girer.

## FAZ B — DENETİM (kendi sistemimize bak; Faz A'nın kurallarıyla)

Bu denetim P6 oturumunda **yapılamadı** — device bridge düştü ve seans sonuna kadar dönmedi. Açık borç, ilk somut adım bu.

1. `CLAUDE.md` (proje kökü + varsa `.claude/CLAUDE.md` + `CLAUDE.local.md` + `~/.claude/CLAUDE.md`):
   - Backtick'siz `@...` satırı var mı? (İstemsiz eager yükleme — P5 tuzağı.) Varsa ne çekiyor, kaç KB?
   - İçinde **volatil/tarihli** içerik var mı (tarih, "şu an", sayaç, durum)? Oturumlar arası byte-stabil mi?
   - Satır sayısı ve KB'si nedir? 200 satır hedefine göre nerede?
   - Compaction bölümü (Faz A.6'da bulduğun birebir başlıkla) var mı?
   - **Not:** aradığın şey "volatil satır tepede mi" DEĞİL — o kriter geçersiz (Faz C.1). Aradığın: volatil içerik bu dosyada **hiç** var mı.
2. `core/durum-kapsulu.md`: boyutu, hangi mekanizmayla yükleniyor (Read mi, import mu, MEMORY.md mi)? Yükleniş biçimi, compaction'da başına ne geleceğini belirliyor.
3. `.claude/rules/` var mı, `paths:` frontmatter kullanan kural var mı? (Varsa: compaction'da kayboluyorlar — kalması gerekenler köke taşınmalı.)
4. Skill'ler (`atlas-kosum`, `karar-modeli`, diğerleri): SKILL.md'lerin ilk N satırında kritik talimat var mı? (Kırpma yönüne göre — Faz A.5.)
5. Oturum akışında **CLAUDE.md'ye oturum ortasında yazılıyor mu**? Tüzük (≈40KB) oturum ortasında Read ediliyor mu, kaç kez?

## FAZ C — BU OTURUMDAN GELEN BULGU SETİ (doğrula ya da çürüt, körlemesine alma)

1. **[GERİ ÇEKİLMİŞ BULGU — tekrar açma]** P6 oturumu önce "kapsülün en volatil satırı (`**Güncelleme:**`) dosyanın en tepesinde = prefix-invalidation anti-pattern" dedi. İkinci-model denetiminde bu **çürütüldü**: cache blok granülerliğinde çalışır, kapsül tek bir `tool_result` bloğudur, satırı tepeden dibe taşımak kazanç getirmez. Blok-5'in öğrettiği kural doğru, **uygulaması** yanlıştı. Satır sırası cache'i değil **kesilmeyi** etkiler (MEMORY.md sert limiti, SKILL.md kırpması) — ve orada yön terstir: tepede olmak korur. Faz A.1/A.3 ile teyit et; teyit ederse bu düzeltme senaryo-defterine "denetim kendi bulgusunu çürüttü" vakası olarak girsin.
2. **Compaction'ı pasif kullanıyoruz, stratejik kullanmıyoruz.** Auto-compact her oturumda üstümüzde çalışıyor; ama CLAUDE.md'de yönlendirme bölümü yok, `/compact <focus>` alışkanlığı yok, kapsül compaction'a göre tasarlanmadı.
3. **İki-parçalı sıcak katman yapısal olarak VAR** (CLAUDE.md stabil / kapsül ayrı dosya, `@import` edilmiyor). Eksik olan yapı değil **disiplin**: oturum-ortası CLAUDE.md yazımı, büyük dosyaların tekrar-Read'i, kapsülün compaction'da erken temizlenmesine karşı bir refleksin olmaması.
4. **"CC'den araştırıldı mı?"** — facts evet (Atlas 07-15), hot-layer **yapısı** hayır. P5/P6 ilk yapısal denetim.

## FAZ D — İNŞA (öneri; ölçek m.37 eşiğini aşıyorsa 3 matematiksel model kur)

Aday kalemler — sırala, ölç, öner:

- **D1 · Compaction yönlendirmesi:** CLAUDE.md'ye Faz A.6'daki birebir başlıkla bölüm ekle. İçerik önerisi: *koru* = aktif kararlar, açık borçlar, çelişki-kapısı raporları, dosya yolları; *at* = ham araştırma çıktıları, tool logları, ara akıl yürütme. Kısa tut (CLAUDE.md byte-bütçesi).
- **D2 · Yeniden-okuma refleksi:** compaction sonrası (ya da uzun oturumda periyodik) kapsülü + açık borç listesini yeniden Read etme kuralı. Gerekçe: kapsül bir tool çıktısıdır, compaction'ın birinci aşamasında temizlenir.
- **D3 · Not-tutma sertleştirmesi (asıl kaldıraç):** değer üretilir üretilmez diske yaz — compaction'ı olay olmaktan çıkar. m.9 (push'lanmış commit) + m.34 (katmanlı ingest) bunun zaten kanonik hali; eksik olan oturum-içi refleks.
- **D4 · CLAUDE.md yazım disiplini:** kanon edit'leri toplu ve seans sonunda; oturum ortasında CLAUDE.md'ye yazma. (Faz A.3 doğrularsa gerekçe: prefix'i o noktadan itibaren düşürür.)
- **D5 · Skill baş-yükleme:** SKILL.md'lerde kritik talimat ilk satırlara (kırpma yönü).
- **D6 · Kapsül boyut/biçim politikası:** MEMORY.md sert limitine göre hedef boyut + "kritik içerik tepede" kuralı. (Not: bu kural **kesilme** gerekçesiyle, cache gerekçesiyle değil.)
- **D7 · Tüzük yükleme politikası:** 40KB'lik tüzüğün oturum ortasında kaç kez ve nasıl Read edildiği; thrash riski varsa bölümlü okuma ya da index+topic ayrımı.

## FAZ E — "NE YANLIŞ YAPIYOR OLABİLİRİZ" (hipotez listesi; doğrula, sonra hükme bağla)

- Yüzey farkı: bu kuralların bir kısmı **Claude Code CLI** dokümanından geliyor. Cowork oturumlarının aynı compaction/CLAUDE.md mekaniğini kullandığı **varsayıldı, doğrulanmadı**. Doğrula; farklıysa iki yüzey için ayrı politika gerekir.
- Kanon dosyaları büyüdükçe (tüzük 40 madde, senaryo-defteri, CC defteri) sıcak katman değil **sıcak-dışı okuma trafiği** şişiyor olabilir; ölçülmedi.
- `paths:` frontmatter'lı kural yazdıysak, o kurallar compaction'da sessizce kayboluyor olabilir — kimse fark etmez.
- "Pointer ilkesi" (m.20) doğru uygulanıyor ama **pointer'ın kendisi** compaction'da eriyorsa işaret ettiği yer bulunamaz; D2 bunun sigortası.
- Öğrenme şeridinin çıktısı ana-sıraya devrediliyor ama **ingest gecikiyor** — mount'ta müfredat/kapsül bayat görüldü (07-22). Bu, bilgi mimarisi sorunu değil, akış sorunu; ayrı kalem.

## FAZ F — ÇIKTI

1. Faz A doğrulama tablosu (senaryo-defterine).
2. Faz B denetim raporu (bulgular + dosya/satır referansları).
3. D1–D7 için: yap / yapma / ertele + gerekçe. m.37 eşiğini aşan kalemlerde 3 model (token × zaman × beklenen-kalite, sayısal, deneysel damgalı — m.39) ve işaretli öneri; Salih'e görünür sun, onay bekleme, veto açık.
4. Katman-1'e düşen ne varsa (kanon metni değişikliği, kural ekleme, silme-birleştirme) ayrı listelensin — Salih imzası gerekir.
5. Değişen dosyaların commit'i Salih'te (m.9). Mount'tan git YAZMA yok.

## SINIRLAR VE AÇIK BORÇLAR

- **m.16 notu — B→C onayı:** Salih P6'da "Model B'den C'ye geçişi onaylıyorum" dedi. Kayıt: bu bir **yol haritası + kriter onayı**dır (B şimdi → C, araştırma-filosu D4 canlıya alınınca), "C'yi bugün inşa et" değil. C'nin tetiği K-009/K-010'a bağlı ve ikisi kanonda **bloke**; vizyon merdiveni canlı ajanı en son basamağa koyuyor. Salih "hayır, şimdi inşa" derse bu K-009/K-010'u yeniden açan **Katman-1** kararıdır ve merdiven çelişkisi ayrıca raporlanır.
- **Şerit 2 ingest backlog:** `mufredat.md` Durum sütunu P3/P4/P5/P6 + "Sıradaki oturum" satırı + kapsül Şerit-2 satırı; ayrıca P2 devir ingesti hâlâ açık. Tam set P5 ve P6 devir dosyalarının 2. bölümlerinde.
- **P7 (tool-use temelleri)** Salih tarafından başka bir oturuma bırakıldı — bu blokta başlatma.
- **Güvenlik borcu (bağlantılı değil ama açık):** PAT remote URL'de düz metin, ~10 Ekim'de ölüyor — credential-helper'a taşıma + yenileme tek hamlede.

====
