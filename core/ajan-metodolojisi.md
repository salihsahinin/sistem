# Ajan-Tasarım Metodolojisi v1 (AKTİF: Salih emri 2026-08-14)

*Salih'in iki-parametre sezgisinin (GÖREV = fonksiyon · HAFIZA = import) araştırma-sınanmış hâli. Kanıt: `cc/rapor-2026-08-14-2.md` (Opus lider + 4 atlas; D-ağırlıklı; ⚠️ m.40b antitez şeridi KOŞULMADI — tek-şerit borcu açık). Tüm eşikler deneysel m.29. Doldurulabilir iskelet: `core/sablonlar/gorev-fonksiyonu.md`. Bu belge A5 ekip-lideri tasarım paketinin araştırma-önkoşulunu doldurur ve S-K (görev-emri-derleme) şablon temelini verir.*

## 1. Görev = FONKSİYON (ama küçük fonksiyon)

- **Tipli alanlar; alan adı talimattır.** Görev-emri başlıkları kozmetik değil davranışsaldır (DSPy: `research_request` ≠ `request`, başka hiçbir şey değişmeden çıktı kalitesi değişir). Alanlar `ad: tip` yazılır; adlar görevin kendi dilinden seçilir.
- **Sözleşme üçlüsü:** `ön-koşul` (trigger) · `değişmez` (predicate) · **`done-yüklemi`** (postcondition — boolean değerlendirilebilir; "iyi bir rapor" gibi derece ifadesi YASAK) + `yeniden-deneme tavanı` (varsayılan 3). Kanıt: AgentSpec >%90 güvensiz-yürütme önleme, DSPy Assertions +%164 kısıt-geçme, CrewAI guardrail+retry=3.
- **Dallar birinci-sınıf ve numaralı.** Koşullar gövdeye gömülmez; `D1: eğer X ∧ ¬Y → ... · D2: aksi → ...` biçiminde m.38 bağlaçlarıyla ayrı yazılır (LangGraph `Command(goto)` deseninin metin karşılığı). Katman-1 sınıfı karar gerektiren dal = `DUR + Salih'e sor` (interrupt deseni = m.31 kapısı).
- **DAL-BÜTÇESİ FRENİ (bu bölümün en önemli kuralı):** sözleşme zenginleştikçe DEĞİL, küçüldükçe tutar — koşul/tur arttıkça başarı ölçülü düşüyor (Multi-IF: o1-preview 3 turda 0,877→0,707). Bir görev-fonksiyonunda **dal+koşul toplamı ≤5** (deneysel); aşılıyorsa fonksiyon BÖLÜNÜR — büyük iş = fonksiyon ZİNCİRİ, dev fonksiyon değil. Bu, m.21'in ilk ampirik dayanağıdır.
- **Done ölçümü ayrıştırılır (DRFR):** teslimde emirdeki her koşul tek tek "karşılandı/karşılanmadı" işaretlenir; tek bir "başarılı mı" derecesi sorulmaz.

## 2. Hafıza = MANİFEST (import analojisi, düzeltmeyle)

- **Düzeltme (Salih sezgisine):** Claude Code `@import` LAZY değil **EAGER**'dır — "imports load at launch... doesn't reduce context". İmport analojisi biçimce doğru, maliyetçe yanıltıcı. Gerçek JIT: path-scoped rules (glob-tetikli) · skill Seviye-2/3 · konu dosyaları.
- **Üç-kademeli açılım (manifestin omurgası):** Seviye-1 = her kalemin `ad + tek-satır ne-zaman-okunur` künyesi (her zaman yüklü, küçük) → Seviye-2 = gövde (model alaka görürse) → Seviye-3 = ek dosyalar (gerektiğinde). Jarvis'te fiilen var (kapsül/pano = S1, pointer'lı dosyalar = S2/3) — artık YAZILI kural.
- **EAGER ↔ LAZY etiketi:** kanondaki her bağlam dosyası iki sınıftan birindedir. EAGER: CLAUDE.md · kapsül · pano (bütçeli, m.22 sıcak katman). LAZY: wiki · raporlar · kuyruk · defter (pointer'la açılır). Yeni dosya varsayılan LAZY doğar.
- **SIRA KURALI (cache gerekçesi — sert):** statik önek EN ÖNDE, dinamik ek EN SONDA. Breakpoint son-özdeş-önek bloğuna konmazsa cache hiç tutmaz → %90 maliyet + %85 gecikme kazancı sıfırlanır. Ajan-promptu blok sırası SABİT: [kimlik → rol → araçlar → kanon-özeti] statik · [göreve-özel veri → tarih/SHA → tetikleyen mesaj] sonda. (Şerh-adayı: m.46(a) SHA alanı dinamiktir, şablon SONUNA taşınmalı.)
- **Bütçe alanı:** her görev-manifesti yaklaşık token tavanı taşır; işçi dönüşü ≈1-2k token özet (ingest şeması §5 ile aynı bütçe). Gerekçe üç bağımsız bozulma kanıtı: NoLiMa (32K'da 13 modelin 11'i taban-%50 altı; GPT-4o %99,3→%69,7) · Lost-in-the-Middle U-eğrisi · Chroma context-rot ("tek distraktör bile" düşürür). **Manifest kolaylık değil performans zorunluluğudur;** m.20 pointer sistemi literatürle birebir — jarvis burada önde.

## 3. Lojik→Kod MERDİVENİ (m.38/m.46 registerleri arası geçiş)

Dört basamak: **(B1) serbest Türkçe → (B2) kontrollü-NL/lojik** (m.38 bağlaçları, EARS-kalıbı, done-yüklemi) **→ (B3) şablon/DSL** (görev-fonksiyonu iskeleti, workflow-YAML, skill) **→ (B4) deterministik kod** (betik/araç).

- **Varsayılan basamak AŞAĞIDIR; yukarı çıkmak kanıt ister** (Anthropic: "karmaşık sisteme yalnızca basit çözüm başarısız olunca geç").
- **Basamak-geçiş kapısı üç soru:** (i) adım sayısı önceden tahmin edilebilir mi? (ii) sabit yol kodlanabilir mi? (iii) model-kararına gerçekten ihtiyaç var mı? → evet/evet/hayır ⇒ bir basamak YUKARI (koda dondur). Kriter SAYI değil DOĞA ("code is deterministic"). Kazanç kanıtları: Voyager 15,3× · CodeAct +%20 · PAL +15pp · MCP kod-yürütme %98,7 token.
- **m.43 şerhi (dürüstlük):** "N=3 tekrar → skill" eşiği ampirik literatürde YOK; kaynağı Rule of Three (Fowler 1999) — ödünç konvansiyon. Deneysel damgası doğru; gerekçesine bu atıf düşülmeli (Salih masası). **(İMZALANDI 08-20 KB-18 — atıf m.43'e düşüldü; eşik Salih revizyonuyla N=5.)**
- **Damıtma ucuz-önce:** tekrar-tespiti önce deterministik yapılır (dedup + filtre, LLM'siz) — AWM: kural-tabanlı ≈ LM-tabanlı (SR 35,6 vs 35,5). Ve kazanç FORMATTAN değil YAPIDAN gelir (kod-stili ↔ metin-stili farkı küçük; format-tax ile aynı yön) — her şeyi B4'e çevirmek gerekmez, B2/B3 meşru duraklardır.

## 4. Lider ≠ İşçi (delegasyon prensipleri — A5 temeli)

- **Delegasyon-sözleşmesi DÖRTLÜSÜ (her işçi görevi 4 alanı taşır):** `hedef` · `çıktı-formatı+bütçesi` · `araç/kaynak kılavuzu` · **`görev-sınırları`** ("sana ait OLMAYAN" dahil). Dördüncü alan bizim şablonların en zayıf halkasıydı ve eksikliği belgeli arıza üretir (Anthropic: 2 ajan aynı işi yaptı, bir konu boşta kaldı).
- **Prompt-içerik ayrımı:** LİDER promptu = kimlik listesi + "ne zaman kime" haritası + sentez sorumluluğu · İŞÇİ promptu = tek uzmanlık + araç kısıtı + "sadece bunu yap" sınırı + çıktı bütçesi. Her işçi tanımında tek-cümlelik **`çağrı-koşulu`** alanı (lider YALNIZ bunu okur — Claude Code `description` deseni; m.42(a) pozitif-yetkinin doğal yeri).
- **PARALELLİK-UYGUNLUK TESTİ (dağıtımdan önce zorunlu soru):** "Bu alt-görevler BAĞIMSIZ bilgi mi topluyor, ORTAK bir çıktı mı üretiyor?" Bağımsız-keşif → paralel serbest (atlas koşumları güvenli tarafta). Ortak-üretim → ya paylaşılan karar-manifesti ya TEK ŞERİT (Cognition: "örtük kararlar çatışır" — Flappy Bird vakası).
- **Maliyet-tavanı:** işçi, liderden pahalı modelde koşamaz (aşağı-yönlü kademeleme serbest). **Rejim etiketi:** her koşum `[rejim: kalite-öncelikli]` ∨ `[rejim: maliyet-öncelikli]` taşır — Anthropic 15×-token/%90,2-kalite ile FrugalGPT %98-ucuzluk aynı mekanizmanın ters hedefleri; karıştırılmaz (m.46(c) genişlemesi).
- **Kendini-analiz kısıtı (Salih Katman-1, 2026-08-21 seans-11; defter Karar 48):** çıktı ANALİZİ yalnız üstten alta akar — bir model kendi çıktısını analiz ETMEZ (Fable dahil: üstü yok → kendini-analiz sıklığı ≈ 0). Gerekçe (Salih beyanı): modelin kendi kendini analizi artı sağlamaz; sağlayıcı bunu kendi yayınlanmamış üst modelleriyle zaten yapar [K — Salih değerlendirmesi]. İSTİSNA: uzun-periyot TOPLU özet analizi (örn. 1 haftalık koşum-süreç özetleri) — bağlam veri-ambarında OLAP işlemi sınıfı: birim çıktı değil dönem DESENİ incelenir. Deterministik doğrulama (test, script, şema/sözleşme kontrolü) kendini-analiz SAYILMAZ — serbest. KB-02 'üst model kendi koşumunu tahmin etmez, yalnız ölçülür' kuralının genişletmesi (m.16 çelişki yok).
- **MODEL HİYERARŞİSİ (Salih Katman-1, 2026-08-17 masa KB-02/KB-03):** üst model (ana-sıra, bugün Fable) = orkestratör + koşum-tahmincisi + hakem; alt modeller (Opus, Sonnet, Haiku) = skill/iş koşucuları — Jarvis skill'lerini alt modellere TETİKLETİR. Koşum-profili tahmini (model×effort×bağlam×token) yalnız üst model yapar ve yalnız kendinden düşük modeller için; üst model kendi koşumunu tahmin ETMEZ (yalnız ölçülür); gerçekleşen sonuç bir sonraki tahmini revize eder (ambar `amb_olgu_kosum`; deterministik: kural-tabanlı revizyon, loglu). Kendini-geliştiren düğüm pilotu (KB-03 A) bu alt-model skill koşumlarının verisiyle açılır (`v_skill_kosum` — CANLI 08-21, pipeline tahmin-gercek-ambar).
- **Skill eşik kuralı (Salih imzası 2026-08-21, defter Karar 51):** bir skill×model çifti `v_skill_kosum`da n≥10'a ulaştığında medyan token/süre bandı hesaplanır; yeni koşum bandın 2× üstüne çıkarsa seans kapanışında sapma satırı raporlanır (`tools/skill-esik.py`, deterministik). OTOMATİK kural değişikliği YOK — her eşik/kural değişikliği ölçüm + Salih imzasıyla.
- **Delegasyon varsayılan KAPALI** (CrewAI `allow_delegation=False` ile aynı yön — m.42(d) katı-başlangıç kanonu sektörle hizalı; işçi işçi doğuramaz, lider açıkça yetki verir).
- **Efor ölçekleme (bilinen, teyitli):** basit iş 1 ajan/3-10 çağrı · kıyas 2-4 ajan · karmaşık 10+ — görev-emrine ajan-sayısı bu cetvelle yazılır.

## 5. Salih masası şerh-adayları — HÜKÜMLER (paket imza 08-20 seans-11, masa KB-18)

1. **m.44 çapası — İMZALANDI:** RouteLLM rakamı [X] kaldı; tüzük m.44 satırına şerh düşüldü (çapa değil anekdot; katman kuralı ayakta).
2. **m.43 gerekçesi — İMZALANDI + REVİZYON:** eşik N=3→**5** (Salih: "skill oluşumu zorlaşsın"); Rule-of-Three atfı + "LLM alanında doğrulanmadı" notu m.43'e düşüldü; pencereli sayaç (W=90 gün) baki; skill-işlev fıkrası (deterministik icra aracı) m.43'e eklendi.
3. **m.46(a) — İMZALANDI + İCRA:** SHA alanı `core/sablonlar/gorev-emri.md` SONUNA taşındı (görev-fonksiyonu şablonu zaten uyumluydu).
4. **m.40b borcu — İCRA BORCU:** 12 yapı-taşına hedefli antitez turu kabul; koşum ayrı ekonomi-onayına tabi (tetik Salih).

## Firstmate rolü (Salih beyanı 08-29, Karar 76 E4 — aynen: "ana ajan gene jarvis olsun firstmate jarvisin ve benim kullandığım bir ajan olsun nasıl çalıştığını ve hangi konularda başarılı çalıştığını da tespit edelim")
Ana ajan JARVIS'tir (m.44 baki — üst-orkestratörlük devredilmez); firstmate = Jarvis'in VE Salih'in kullandığı YARDIMCI ajan — ikame değil araç. Hangi iş sınıfında başarılı çalıştığı beyan'la değil ÖLÇÜMLE tespit edilir: koşum kayıtları (görev sınıfı · sonuç · süre/token) → başarı-tespiti ölçüm borcu İB-59; rol tanımının kalıcı metni bu ölçümle masaya döner.

## Koşum hijyeni ekleri
- **Heredoc-python hijyeni (BAKIM-KK 08-29 kanıtı, Salih imzası Karar 77 — oturum 11b49d44: 18 hata-benzeri çıktı, ≥3 düzeltme turu):** ≥15 satırlık python işi Bash heredoc'a değil scratchpad'de `.py` dosyasına yazılır ve oradan koşulur — "deterministik iş script'e gömülür" kuralının koşum-anı karşılığı; sözdizim hatası yazım katmanında yakalanır.
