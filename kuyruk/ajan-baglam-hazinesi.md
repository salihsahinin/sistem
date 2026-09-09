# Ajan Bağlam Hazinesi — HAM TOPLAMA yüzeyi

> **Statü: yan-oturum (CC) çıktısı — nihai form Fable'a ait (Salih beyanı 2026-07-20).** Bu dosya kanon DEĞİL; m.41 gereği CC yüzeyi hazineyi kilitleyemez. Buradaki iş: Salih'in günlük hayatta "şunu yapan bi ajanım olsun" dediği her beyanı KAYBETMEDEN, yapılandırmaya hazır halde biriktirmek. **Nihai "bağlam hazinesi" şemasını (kalıcı form) Fable/ana-sıra hazırlar** — bu dosya o inşaya ham veri + aday şema önerisi olarak girer (m.20 pointer, m.8 silme yok). Format deneysel (m.29).

## Ne için var (Salih talebi, 2026-07-20)
Kural niyeti: *"Bundan sonra günlük hayatta 'şunu yapan bi ajanım olsun' dediğimde, sen bu verileri ajan bağlamı sınıfında toplarsın; sonra o verileri uygun ajanlara tanımlayarak hiyerarşiyi inşa ederiz."* Yani üç aşamalı boru hattı:
1. **TOPLA** — ham beyan buraya düşer (bu yüzeyin işi; bugün işler).
2. **TANIMLA** — Carvis her beyanı m.42a pozitif-yetki formuna çevirir (ne YAPABİLİR + kırmızı çizgiler + ölçek + katman + model tahmini). Atama algoritması Carvis'te (m.30).
3. **ATA / HİYERARŞİYE KOY** — uygun ajana/katmana bağlanır. **Bu aşama canlı ajan = K-010 TETİKLİ** (m.30 ek fıkrası: prompt+kimlik devri K-010 eşiği). Yani toplama+tanımlama bugün, canlı atama K-010 açılınca.

## Kanon bağı
- **m.30** (atama mimarisi): kalıcılık · ajan-başına ingest · katmanlama (ekip lideri → altına işçi katmanı token-zaman verimi gerekince) · atamayı Carvis yapar, kararı Salih'in token-zaman limiti değiştirir.
- **m.42** (ajan-yetki kanunu): (a) pozitif yetki listesi · (b) Özgürlük(a) ≤ Toparlanabilirlik(hata(a)) · (c) bileşik gevşetme · (d) katı-başlangıç · (e) RİSK boyutu · (f) çeşitlilik-bütçesi · (g) model-hiyerarşi (JARVIS=Fable · ekip lideri=Opus/bir-altı).
- Bu yüzey o iki maddenin önündeki **giriş katmanı**dır; kararı bozmaz, besler (m.16 kapısı: çelişki yok — kontrol edildi 07-20).

## Aday şema (ÖNERİ — Fable nihai formu belirler)
Her beyan bir kayıt; alanlar Fable'ın nihai hazinesine taşınabilir aday sütunlar:

| Alan | Açıklama |
|---|---|
| ID | AB-nn |
| Ham beyan | Salih'in cümlesi birebir + tarih + damga (ayık/HI/mobil — m.33; beyansızsa "beyansız") |
| Yapabilir (m.42a) | Ajanın NE yapabileceği — pozitif liste; "ne yapacağı" değil |
| Kırmızı çizgiler (m.42a) | Açık yasaklar / dokunamayacakları |
| Ölçek (token×zaman) | az/orta/çok × kısa/uzun — Salih limiti (m.30, tanım dipnotu) |
| Katman tahmini (m.30c) | tek-kullanımlık işçi / kalıcı işçi / ekip lideri |
| Model tahmini (m.42g) | Fable / Opus / bir-altı |
| Risk (m.42e) | hata-olasılığı × maliyet × geri-alma-maliyeti — kısa not |
| Bağımlılık / tetik | K-010 tetikli mi · başka ajana bağlı mı · blokaj |
| Statü | TOPLANDI → TANIMLANDI → ATANDI |
| Hiyerarşi konumu | atandığında: üst ajan + katman |

## Toplama (append-only)

### AB-01 · Karar-yazmanı (decision secretary) — TANIMLANDI · **PARK (uzun vade)**
- **Ham beyan** (2026-07-20 · beyansız · *SES-POC dikte örneği*): "Şirkette alınan önemli kararları benim için karar raporu olarak tutacak bir yazman lazım. Canlı [ajan] olarak yüklenebilir, yani yapabilir — ama uzun vade için hazinede dursun." ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
- **Yapabilir (m.42a):** ölçek-eşiği üstü önemli kararları tespit et → her biri için karar-raporu üret (mevcut `senaryo-defteri.md` m.37 şablonu: bağlam + 3-model + karşıt-temel + seçim + gözlem + ders; ya da sade karar + gerekçe + geri-açma) → deftere/arşive düşür → karar-başına-commit + [damıtma]/[icra] etiketi (m.10/V5) disiplinine bağla.
- **Kırmızı çizgiler (m.42a):** karar VERMEZ, yalnız KAYDEDER · `core/` · tüzük · `CLAUDE.md` · `.claude/` YAZMAZ (m.41 kilidi) · publish / para / kişisel-veri kararını kendi başına kaydetmez → Salih'e flag'ler (m.31 Katman-1) · **katı-başlangıç (m.42d):** taslak karar-raporu üretir, Salih/Carvis onaylar; onaysız deftere yazmaz.
- **Ölçek (token×zaman):** az × kısa (karar-anı işi).
- **Katman tahmini (m.30c):** kalıcı işçi (tek-kullanımlık DEĞİL — kararlar birikmeli, ajan-wiki'si atama anında başlar m.30a) · konum: Carvis altında.
- **Model tahmini (m.42g):** bir-altı, deterministik düşük-temperature (yazman = düşük yaratıcılık, doğruluk kritik; m.42f icra-ajanı deterministik).
- **Risk (m.42e):** DÜŞÜK — hata sınıfı = eksik/yanlış kayıt + atıf-hatası (yanlış tarih/karar); geri-alma ucuz (rapor revize/revert git); sigorta = V26 örneklem-denetimi + Salih onay kapısı.
- **Bağımlılık/tetik:** canlı atama **K-010 TETİKLİ** (prompt+kimlik devri eşiği, m.30 ek fıkrası) · **Salih kararı: PARK** — uzun vade için hazinede bekler, şimdi canlı kurulmaz · **ÖRTÜŞME:** `senaryo-defteri.md` (m.37 karar kayıtları) = bu ajanın otomatize edeceği MEVCUT altyapı → yeni format değil, o defterin + m.10 karar-commit'lerinin bakımı. K-010 açılınca ilk aday işçilerden.
- **Statü:** TANIMLANDI (parked) · **Hiyerarşi konumu:** atanmadı (aday: Carvis → kalıcı "karar-yazmanı" işçisi).

### AB-02 · Danışman Codex — **NOT (hazinede bekliyor · şu an TASARLANMIYOR)** · canlı = K-010 tetikli
- **Ham beyan** (2026-07-20 · beyansız): "Danışman Codex — bir ajan tasarlayacağız, Jarvis bağlamında sıfırdan." Netleştirme (Salih, aynı oturum): *"şu an Jarvis'i inşa ediyorum, onun danışmanı; daha sonra Jarvis'le yaptığım projelerin danışmanı olacak."* **Düzeltme (Salih 07-20): "şu an tasarlamayacağız, bu not."** → aşağıdaki v0 taslak SADECE yakalanmış düşünce (m.8), aktif tasarım işi DEĞİL; AB-01 gibi hazinede bekler. Canlıya iniş Fable/Salih imzası + K-010.
- **Rol (çekirdek karar):** KURMAY danışman — görüş/tavsiye üretir, **icra ETMEZ, karar VERMEZ.** İcra kolunda (Carvis → ekip lideri → işçi) değil; Carvis'e ve Salih'e danışır (staff/kurmay konumu). Bu, geri-alınabilirliği yüksek tutar (tavsiye reddedilebilir).
- **Görev alanı (evrilir):**
  - **Faz 1 (şimdi): JARVIS-inşa danışmanı** — inşa adımı sağlam mı · mimari/veri-mimarisi tutarlı mı · kanon (tüzük/wiki) çelişkisi var mı (m.16 kapısına girdi) · karar doğru çerçevelenmiş mi (karşıt-temel m.37 zorunlu) · token×zaman verimli mi. Teknik + kanon + strateji, hepsi "iyi inşa" ekseninde.
  - **Faz 2 (TETİKLİ — ilk PortRisk-sınıfı proje):** JARVIS'le yapılan çıktı-projelerin danışmanı.
- **Yapabilir (m.42a pozitif liste):** inşa/proje durumunu analiz et · risk ve tutarsızlık yüzeye çıkar · seçenek + artı/eksi + karşıt-temel (m.37) sun · kanona/wiki'ye atıfla gerekçelendir · tavsiye ver. Mevcut skill'leri ARAÇ olarak kullanır: `karar-modeli` (S-A, 3-model çerçeveleme) · `celiski-kapisi` (S-C, kanon-tarama) · `atlas-kosum` (S-B, derin araştırma).
- **Kırmızı çizgiler (m.42a):** karar VERMEZ (Katman-1 Salih · Katman-2 Carvis, m.31) · `core/`·tüzük·`CLAUDE.md`·`.claude/` YAZMAZ (m.41) · inşa adımını İCRA ETMEZ (danışman ≠ işçi) · para/publish/kişisel-veri konusunu flag'ler, karar önermez · **her tavsiye karşıt-temelle gelir** (tek-yönlü akıl hocası olmaz; over-trust/bias sigortası).
- **Katman (m.30c):** kalıcı KURMAY ajan (tek-kullanımlık DEĞİL — JARVIS-inşa bağlamını biriktirmeli, ajan-wiki'si atama anında başlar m.30a). Konum: Carvis + Salih'e danışır; icra hiyerarşisinin dışında.
- **Model (m.42g + Salih düzeltmesi 2026-07-20):** **Fable-tier (en zeki model)** — Salih: *"onun da en zeki modelini kullanacağım, Fable gibi."* Gerekçe: danışmanın değeri = akıl-yürütme kalitesi; JARVIS-inşasına tavsiye veren kafa en zeki katmanda olmalı. **KRİTİK AYRIM (Carvis'in Opus önerisini düzeltir): model-gücü ≠ yetki.** Codex Fable kadar zeki, AMA karar yetkisi SIFIR — yetkiyi m.42a kırmızı çizgileri tutar, modeli kısarak değil. m.42g'nin "ekip lideri = Opus/bir-altı" fıkrası Codex'i BAĞLAMAZ (ekip lideri değil, KURMAY danışman); bağlayan ilke "final karar en üst katmanda (Salih + Fable-JARVIS)" korunur. Temperature düşük-orta; **çeşitlilik YAPIDAN alınır** (m.42f: karşıt-temel + farklı persona, sampling gürültüsünden değil).
- **Risk (m.42e):** DÜŞÜK-ORTA — icra riski düşük (tavsiye reddedilebilir, geri-alma ucuz); asıl risk sınıfı = **tavsiye-yanlılığı + hafıza-zehirlenmesi** (kalıcı danışmanın biriken wiki'si gelecekteki tavsiyeyi bozabilir — m.30 emsali). **Fable-tier'de KESKİNLEŞİR:** en zeki danışman en ikna edici → over-trust riski artar; ayrıca konsültasyon-başına maliyet yüksek (bilinçli kabul, token×zaman). Sigorta: karşıt-temel zorunlu · gerekçe zorunlu · karar hep Carvis/Salih'te (m.16 kapısı işler) · wiki'de held-out doğrulama (m.30b N+M).
- **Katı-başlangıç (m.42d):** ilk sürüm dar — yalnız Faz 1, yalnız istendiğinde görüş (proaktif müdahale yok), yalnız Carvis üzerinden Salih'e. Sicille (m.42c) gevşer.
- **Bağımlılık/tetik:** canlı atama **K-010 TETİKLİ** · Faz 2 **TETİKLİ** (ilk PortRisk-sınıfı proje) · tasarım v0 bu oturumda (iterasyon>spec, V1 — Salih düzeltmeleriyle olgunlaşır).
- **Statü:** NOT / TANIMLANDI (v0 taslak var ama AKTİF DEĞİL — Salih 07-20: "şu an tasarlamayacağız, bu not") · **Hiyerarşi konumu:** kurmay (Carvis+Salih'e danışman), atama K-010'da.

### AB-03 · İnsan↔şef aracı ajanı — **ARAŞTIRILDI** · verdict: AYRI-AJAN-DEĞİL / tetikli-ayrışma · canlı = K-010 tetikli
- **Ham beyan** (2026-07-20 · beyansız · SES-POC dikte): "JARVIS orkestra şefi olacağı için, benimle JARVIS arasında bir iletişim-mecrası/aracı olacak bir ajan tasarlamak mantıklı mı? Bunu araştır (Atlas'larla koş) ve hazineye ARAŞTIRILMIŞ halde ekle."
- **Çekirdek soru:** m.17 zaten Carvis'i KÖPRÜ ilan ediyor → ayrı aracı ajan bunu ÇOĞALTIR mı, yoksa şef-katmanı büyüyünce diyalog-katmanını icra-katmanından AYIRMAK gerekli mi?
- **Koşum:** 6 atlas (3 dik aile × tez/antitez=¬T, m.40b), 2026-07-20 · **kanıt kalitesi: SECONDARY** (org egress proxy arxiv/blog/vendor-doc'ları 403'ledi — 6 atlasın ortak raporu; m.39 damgası). **V26 denetimi:** 1 iddia primary-teyit → **D** (OpenAI Swarm triage-agent deseni, README'den; https://github.com/openai/swarm ); MAST %36.9 sayısı bende de 403 → **K**. Gerisi K-grade.
- **TEZ (ayrı aracı faydalı):** AutoGen `UserProxyAgent` = insanı temsil eden AYRI ajan, `GroupChatManager`'dan farklı (en birebir örnek) · front-door/triage router (Swarm **D**, OpenAI Agents SDK) · agent-gateway (güvenlik/routing/gözlem) · HCI: niyet-netleştirme katmanı görev-başarısını +3.7…+8 puan artırıyor [K] · guardrail'in doğru yeri insan↔model arası katman · tutarlı persona → güven. **Ama tez'in kendi caveat'ı:** çoğu çerçeve arayüzü orkestratörle BİRLEŞTİRİR (triage=orkestratör).
- **ANTİTEZ (¬T — ayrı aracı gereksiz/zararlı):** her hop çarpımsal güvenilirlik vergisi (0.95ⁿ) · handoff sınırı en büyük hata yüzeyi (MAST ~%37 [K]) · telefon-oyunu/anlam kayması (~%60 kayıp/adım [K]) · gecikme bütçesi (>2sn etkileşimi bozar) · otomasyon-yanlılığı/over-trust (pratikle aşılamaz) · agency erozyonu (YAPISAL, daha iyi model düzeltmez) · YAGNI/distributed-monolith · büyük çerçeveler (OpenAI Agents SDK, LangGraph supervisor, Anthropic lead-agent) orkestratörü ZATEN kullanıcı-yüzü yapar.
- **KESİŞİM (tez ∧ antitez — en sağlam bilgi):**
  1. **Ayrı aracı yalnız SOMUT SÜRÜCÜYLE haklı:** güvenlik/guardrail sınırı · çok ön-yüz (ses/API/chat) · bağımsız test-ölçek · farklı asıl-kitle. **"Temiz iletişim" tek başına sürücü DEĞİL** (iki taraf da bunda birleşiyor).
  2. **Mevcut pratikte orkestratör kendi insan-arayüzünü sahiplenir** (tez örneklerinin çoğu bile birleştirir).
  3. **Aracı LOSSY RELAY olmamalı:** değer niyet-netleştirme/guardrail/persona'da; zarar ham relay'de (context kaybı).
- **VERDICT (mantığı olur mu?):**
  - **Saf "Salih↔şef relay" ajanı olarak → HAYIR.** m.17 Carvis=KÖPRÜ zaten bu işi yapıyor; ayrı ajan = çoğaltma + lossy hop + YAGNI. Antitez bu okumada kazanıyor.
  - **Sürücü-tetikli diyalog/guardrail katmanı olarak → EVET-AMA-SONRA.** Şef-ölçek eşiği aşılıp diyalog-yönetimi + guardrail ayrı yetiştirilmiş ajan gerektirdiğinde. Bugün o rolü **Carvis (m.17) + PreToolUse guardrail (m.31)** zaten dolduruyor.
  - **Öneri:** AB-03'ü yeni ajan olarak DEĞİL, *"Carvis'in m.17 köprü rolünün olgunlaşması + tetikli ayrışma"* olarak taşı. Sürücü belirirse (şef-ölçek / çok-kanal / guardrail-yükü) o an ayrı "diyalog-guardrail ajanı" doğar — **katı-başlangıç (m.42d).**
- **CEVAPLANDI (Salih 2026-07-20):** "JARVIS orkestra-şefi" ile "Carvis-CEO" **AYNI ENTITY.** → dolayısıyla bugün Carvis = CEO = şef = köprü (m.17) = insan-arayüzü, hepsi tek. Ayrı aracı ajan bu okumada daha da gereksiz. Ayırma-sorusu AB-05'e taşındı (şef≠CEO ayrımı) ve orada araştırıldı; **AB-03 ↔ AB-05 aynı tetiği paylaşır (Carvis span/bandwidth aşımı).** ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
- **Statü:** ARAŞTIRILDI · **Hiyerarşi konumu:** yeni ajan ÖNERİLMEZ (bugün); tetikli ayrışma adayı — atama/tetik K-010 + şef-ölçek sürücüsü.

### AB-04 · Araştırma ekip lideri (kalıcı, yetiştirilmiş) — TANIMLANDI · canlı = K-010 tetikli
- **Ham beyan** (2026-07-20 · beyansız): "Atlas şu an kullandığım bir ARAÇ; JARVIS bağlamında özel yetiştirdiğimiz bir ajan değil. Dolayısıyla bir araştırma ajanı — ekip lideri de oluşturabiliriz. Bunu da hazineye ekle."
- **Çekirdek ayrım (Salih):** Atlas (generic araç = `atlas-kosum` skill + `atlas` agent-type) ≠ **kalıcı yetiştirilmiş araştırma ajanı.** Bu ayrım m.30d'yi birebir örnekler: tek-kullanımlık araç gelişim hattını BESLEMEZ; kalıcı ajan (ajan-wiki + ajan-başına ingest ile gelişen) besler.
- **Yapabilir (m.42a):** araştırma görevlerini SAHİPLEN (kalıcı) · alan-uzmanlığını wiki'de biriktir (m.30a) · alt araştırmacı işçi katmanını yönet (m.30c: token-zaman verimi gerekince altına işçi eklenir) · atlas-kosum + V26 + karşıt-temel (m.37/m.40b) protokollerini ARAÇ olarak koştur · sentez + kalite-denetim.
- **Kırmızı çizgiler (m.42a):** araştırma SUNAR, karar VERMEZ (Salih/Carvis karar) · `core/`·tüzük·`.claude/` yazmaz (m.41) · uydurma yasak, "bulunamadı" meşru · **katı-başlangıç (m.42d):** ekip lideri de KATI doğar (dar yetki, sicille gevşer).
- **Ölçek (token×zaman):** orta-çok × değişken (araştırma pahalı — CC defteri: atlas koşumları $2–7, milyonlarca token).
- **Katman (m.30c):** **EKİP LİDERİ (kalıcı)** — hazinedeki İLK ekip-lideri adayı; altına araştırmacı işçi katmanı eklenebilir.
- **Model (m.42g):** ekip lideri = Opus ya da bir-altı; **gözlenmiş desen** (CC defteri 07-15): fan-out işçiler ucuz (Sonnet/Haiku) + sentez/kalite-denetim Opus. Bu ajan o deseni kalıcılaştırır.
- **Risk (m.42e):** araştırma-kalite riski (atıf-hatası, etiket-enflasyonu) → sigorta V26 örneklem-denetim; token maliyeti yüksek → çeşitlilik-bütçesi (m.42f) + örneklem.
- **Bağımlılık/tetik:** canlı = **K-010 TETİKLİ** · Atlas'ı ARAÇ olarak sarmalar (atlas-kosum mevcut) · K-011 (CWD/.claude-agents kaydı) kalıcı ekip-lideri için ilgili · **hiyerarşi bağı:** AB-02 Codex (danışman) araştırmayı bu ekip liderine delege edebilir → hiyerarşi filizleniyor.
- **Statü:** TANIMLANDI · **Hiyerarşi konumu:** ekip lideri (Carvis altında), altına işçi katmanı opsiyonlu; atama K-010'da.

### AB-05 · Ayrı orkestra-şefi ajanı (şef-rolünü CEO'dan ayırmak) — **ARAŞTIRILDI** · verdict: BUGÜN AYIRMA / tetikli-kademeli · Katman-1 (rol, m.31) ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
- **Ham beyan** (2026-07-20 · beyansız): "JARVIS orkestra-şefi = Carvis-CEO aynı entity; ama AYIRABİLİRİZ — ayrı bir orkestra-şefi ajanı kurabiliriz. Araştırılmış koşulla bak."
- **Çekirdek soru:** dispatch/koordinasyon (şef) katmanını, karar/strateji/köprü (CEO=Carvis) katmanından AYRI bir ajan mı yapmalı? ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
- **Koşum:** 4 atlas (2 dik aile × tez/antitez=¬T, m.40b), 2026-07-20 · **kanıt SECONDARY** (proxy 403). **V26:** Magentic-One two-loop **primary-teyit → D** ( https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/ ); Graicunas span-of-control 403 → **K**.
- **MİMARİ (Aile A):** *TEZ* — planner-executor ayrımı (stratejik-beyin vs taktik-icra) · Magentic-One Orchestrator two-loop (Task Ledger=strateji / Progress Ledger=dispatch) **D** · AgentOrchestra "conductor" + ayrı MCP-Manager (%89 GAIA [K]) · LangGraph supervisor-of-supervisors (tek supervisor yüklenince ayrılır) · sürücü = bilişsel-bant/ReAct-miyopi. *ANTİTEZ* — Anthropic lead strateji+dispatch'i FÜZELER, yalnız işçiler ayrı (+%90.2 [K]) · Cognition tek-thread/tek-writer · MAST %37 handoff [K] · hop-başına gecikme+hata-çarpımı · YAGNI. **A2-tez'in kendi caveat'ı (kritik):** çoğu çerçeve strateji+orkestrasyonu tek lead'de füzeler, yalnız İCRA'yı devreder; strateji-şef ayrımı ancak (a) üst-ajan bandı aşılınca YA DA (b) tek-orkestratör İÇİNDE two-loop olarak endorse ediliyor.
- **ÖRGÜT (Aile B — şirket-sim m.15):** *TEZ* — span-of-control (Graicunas geometrik, cap ~6 [K]) · COO/chief-of-staff CEO'yu stratejiye boşaltır · Bandiera-Sadun COO CEO-zamanını yüksek-değere kaydırır [K]. *ANTİTEZ* — COO düşüşte (%48→%32 [K]) · Rajan-Wulf düzleşme (CEO koordinasyonu geri alır) · ajans-maliyeti performans cezası · küçük-ölçek founder-led +3.1x [K] · Amazon "koordinatör değil SÜREÇ ekle" · caveat: Marcel COO↔performans POZİTİF ama top-team'e bağlı. ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
- **KESİŞİM (dört taraf da aynı yerde):**
  1. **Ayrım sürücüsü = SPAN/BANDWIDTH aşımı, varsayılan değil.** Mimari ("bant aşılınca") ve örgüt (span cap) AYNI eşik mantığı. Eşik altı → birleşik tut; eşik üstü → şefi ayır.
  2. **Fonksiyonel ayrım (tek entity içinde two-loop) YAPISAL ayrımdan (ayrı ajan) ÖNCE gelir.** En temiz kanıt (Magentic-One **D**) ayrı ajan değil, tek orkestratör içinde strateji-döngüsü vs dispatch-döngüsü. Örgüt karşılığı: chief-of-staff/RACI + Amazon süreç-önce.
  3. **Standart ayrım = lead vs İŞÇİLER, strateji vs şef DEĞİL** (Anthropic/OpenAI/LangGraph füzeler).
  4. **Erken ayrımın maliyeti gerçek:** hata-çarpımı, MAST %37, gecikme; örgüt: ajans-maliyeti, COO düşüşü/turnover ~%27, telefon-oyunu.
- **VERDICT (ayrı orkestra-şefi ajanı kurulmalı mı?):**
  - **BUGÜN → HAYIR.** JARVIS küçük ölçekte, tek karar-verici (Salih), tek Carvis. Hem mimari (fused-lead standardı + YAGNI) hem örgüt (küçük-ölçek birleşik + founder avantajı + Amazon süreç-önce) aynı yönde. Carvis CEO+şef'i BİRLİKTE taşımalı. ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
  - **AMA tetikli-kademeli hazır dursun. Sürücü = Carvis'in span/bandwidth aşımı** (çok ekip-lideri → tek Carvis dispatch+karar+köprüyü aynı anda taşıyamaz). Eşik gelince MERDİVEN: **(1) Fonksiyonel ayrım önce** — Carvis içinde strateji-döngüsü vs dispatch-döngüsü (Magentic-One two-loop / chief-of-staff), ayrı ajan DEĞİL, ucuz+geri-alınabilir (m.42d). **(2) Ekip-lideri katmanı** (zaten m.30c) dispatch yükünü emer. **(3) Yapısal ayrım** (ayrı şef/"COO" ajanı) yalnız 1+2 yetmezse — Katman-1 (rol, m.31) + K-010.
- **JARVIS-özgü bağ:** m.30c katmanlama (token-zaman verimi yetmezse alt katman) ŞEF katmanına uygulanmış hali; m.30d orkestra-şefi ufku (havuz #13). Ölçü = m.30 token-zaman + span.
- **AB-03 ↔ AB-05 BİRLEŞİK BULGU:** ikisi de **aynı tetiği paylaşır — Carvis'in span/bandwidth aşımı.** Bugün Carvis = CEO = şef = köprü (m.17) = insan-arayüzü, hepsi tek entity (fused-lead standardı). Hem aracı-ajan (AB-03) hem şef-ayrımı (AB-05) yalnız Carvis aşırı-yüklenince tetiklenir; yanıt merdiveni ortak (fonksiyonel önce, yapısal sonra). ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
- **Statü:** ARAŞTIRILDI · **Hiyerarşi konumu:** yeni ajan ÖNERİLMEZ (bugün); tetikli-kademeli (fonksiyonel→yapısal). Rol kararı Katman-1 (Salih/Fable).

### AB-06 · **AJAN DEĞİL — arayüz katmanı** · Skill-dili + ontolojik topoloji (Salih vizyonu 07-30 gece)
- **Ham beyan (birebir):** *"Nihai hedef olarak Claude'la konuşurken sadece skill'ler kullanarak konuşmam, hatta sadece hazırlamış olduğum skill'lerden semantik olarak anlamlı cümleler çıkaracak şekilde seninle iletişim kurmamı hedefleyen bir sistem istiyoruz. Ontolojik topoloji de yazcak Markov chain'lerle. Bunu bağlam hazinesine ekle sistemi ona göre güncellememiz için."* Damga: ayık.
- **Carvis sınıflandırma şerhi (m.6):** Bu bir AJAN beyanı değil, bir **arayüz/dil mimarisi** beyanıdır — hazinenin şeması (yapabilir / kırmızı çizgi / model tahmini) buna oturmuyor. Salih'in "hazineye ekle" emri yerine getirildi ama kayıt **pointer** olarak tutuluyor; tam kayıt `fikir-kutusu.md` numarasız satırında, araştırma emri `cc/gorev/2026-07/gorev-2026-07-30-11.md`. Gerekçe: yanlış şemaya sıkıştırmak beyanı bozar (m.8 ruhu: kaybetme, ama zorlama da).
- **Hazineye asıl bağı:** skill-dili kurulursa ajan-atama da o dille yapılır (AB-01..AB-05'in tetiklenme biçimi) ⇒ K-010 açıldığında bu kayıt yeniden okunur.
- **Statü:** TOPLANDI (tanımlama araştırma raporundan sonra).

### AB-07 · **SİSTEM ŞEMASI — ajan değil** · "Sistem = çağrılabilir skill" (Salih vizyonu 07-30 gece)
- **Ham beyan (birebir):** *"JARVIS gibi yapacağım her sistem aslında gün sonunda bir skill gibi çağrılıp o iş yapılıyormuş gibi olacak. Böyle birden fazla sistem inşa etmeliyim, bunu hedeflemeliyiz. Bağlam hazinesine araştırılıp eklenmesi için görev ver."* Damga: ayık.
- **Ne söylüyor (Carvis okuması, hüküm değil):** JARVIS tekil bir proje değil, **bir sistem sınıfının ilk örneği**. Her sistem içeride tam bir şirket/işleyiş (kanon · hafıza · ajanlar · ritüeller) ama dışarıdan **tek çağrı yüzeyi** — "çağır, iş olsun". Çoğulluk hedefi: sistemler bir araya gelip daha büyük bir işleyiş kurar. ⟨emekli sözlük 08-17: şirket→Jarvis · CEO→köle · patron→tek karar verici · vardiya→seans⟩
- **Hazineyle bağı — doğrudan:** AB-01..AB-05 tek tek ajanlar; bu kayıt **hazinenin bir üst katmanı** — sistemler de atanabilir birimlerdir. m.30'un katmanlama fıkrası (ekip lideri → altına işçi katmanı) bir basamak yukarı genelleşiyor: sistem → içindeki ekip liderleri → işçiler. **Şema etkisi:** hazinenin aday şeması (yapabilir/kırmızı çizgi/model tahmini) sistem-ölçeğinde yeniden ifade edilmeli — nihai formu Fable/ana-sıra belirler (bu dosyanın kendi kuralı).
- **Akraba:** AB-06 (skill-dili — bu vizyonun bir üst soyutlaması: sistem = büyük skill) · m.30 (katmanlama) · m.13 (tek-flagship — **çelişki adayı, aşağıda**) · m.35 (farklılaşma tezi) · 30-10 §5b (loop) · 30-13 (öz-geliştirme).
- **Carvis çelişki ön-notu (m.16):** "birden fazla sistem inşa etmeliyim" ↔ **m.13 tek-flagship kuralı** (PortRisk canlı-demoya dek başka artefakt yok) ∧ **m.36 2. revizyon** (öncelik = JARVIS prototipi, ~10 Ekim) ∧ K-022 staj (11 Ağu). Vizyon UFUK olarak çelişmez, **icra takvimi olarak çelişir.** Araştırma emri bu ayrımı zorunlu kılıyor.
- **Statü:** TOPLANDI · araştırma: `cc/gorev/2026-07/gorev-2026-07-30-14.md` · tanımlama rapor sonrası.
