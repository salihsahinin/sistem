# JARVIS Arayüzü — Çok-Sayfa / İzleyici-Kategorili / Mod-Sayfaları — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); nihai karar = Fable (m.41). Kaynak: Salih 07-18 — "karar arayüzünün bir başka kısmı koşan ajanlar/model/effort/görev/usage tablosu (senin de okuduğun kısım); arayüzde senin gördüklerin + benim özel sayfalarım; ör. 'Konuşarak İnşa Modu 1' sayfası farklı dizayn — yöntemi+yapımını araştır çift atlas, rapora ekle." Atlas 2 şerit: gözlemlenebilirlik (DONE) + rol/mod-adaptif mimari (DONE). **+ ANTİTEZ red-team** (§9; 07-18 çift-atlas=tez+antitez kuralı retroaktif eklendi).

---

## 1. Vizyon + kanon bağı
- **Kararlar kısmı (rapor 1 §9) = bu arayüzün BİR sayfası.** Salih genişletti: çok-sayfa + izleyici-kategorili + mod-sayfaları.
- **Tek veri-omurgası = git-as-truth** (senaryo-defteri + git-log + cc/defter + yeni usage-logu) → **çok görünüm** (m.18 üç-yüz: makine/insan/talep-üzerine). Her sayfa = aynı omurganın bir PROJEKSİYONU (event-sourcing/CQRS).
- İzleyici ayrımı = **m.28 iki-düzlem** (iş-düzlemi paylaşılan / kişi-düzlemi Salih-özel) yankısı.

## 2. Sayfa taksonomisi (izleyici × tür)
**İzleyici kategorileri (Salih'in ayrımı):**
- **Paylaşılan — Carvis hazırlar, Salih denetler** ("senin de okuduğun kısım"): gözlemlenebilirlik/orkestrasyon.
- **Salih-özel** ("benim kendim bakmam için"): kişisel bakış / karar / mod-sayfaları.
**Sayfa türleri (adaylar):**
- **Kararlar kısmı** (rapor 1 §9) — bekleyen 3-model kararları, sesli/mobil onay. [Salih-birincil, Carvis-besler]
- **Gözlemlenebilirlik tablosu** — koşan ajanlar/model/effort/görev + usage/maliyet. [Paylaşılan — Carvis+Salih] → §3.
- **Mod-sayfaları** — "Konuşarak İnşa Modu 1" (oyun, hands-free, farklı dizayn). [Salih-özel] → §6.
- **Pano/kapsül görünümü** (AKTİF/BEKLEYEN/BLOKE, durum). [Paylaşılan]
- **POP-backlog** (planlanmış optimizasyon, rapor 7) + **karar-defteri/log** (senaryo-defteri) + **öğrenme-şeridi** görünümleri.

## 3. Gözlemlenebilirlik tablosu — "koşan ajanlar + usage" (Atlas A — DONE)
**★ Kilit ayrım:** "koşan ajanlar" (canlı, olay-güdümlü durum-makinesi) ≠ "usage tablosu" (trace/metrik, post-hoc). **Hiçbir araç ikisini birden vermez** (Langfuse/Phoenix/Helicone hepsi trace-temelli, koşum bitince; canlı-durum yalnız orkestrasyon-UI [Vibe Kanban] ya da hook-panosu [disler]) → **hibrit** şart.
**★★ Claude Code sinyalleri ZATEN yayınlıyor** (sıfırdan enstrümantasyon DEĞİL):
- **OTel** (`CLAUDE_CODE_ENABLE_TELEMETRY=1`): `claude_code.cost.usage` öznitelikleri = **`model` · `effort`(low..max) · `agent.name` · `query_source`(main/subagent) · `skill.name`** — *tam senin kolonların, birinci-sınıf.* `token.usage` + `api_request` (canlı, ~5sn).
- **Headless JSON** (`-p --output-format json`): `total_cost_usd` (cache dahil gerçek fatura) + **`modelUsage`** (model-başına $) + `duration_ms`.
- **Hooks**: `SubagentStart`→"koşuyor" / `SubagentStop`→"bitti" (canlı durum).
**Maliyet-atıf (çift-sayım tuzağı):** `total_cost_usd` = top-seviye OTORİTE (alt-ajanlar DAHİL); ajan-kırılımı onun PARTİSYONU, üstüne ekleme YOK. `total ≈ Σ(agent×model×query_source) cost.usage`.
**Feed = event-sourcing (git-as-truth'a birebir):** append-only JSONL olay-logu → "tablo" = logun PROJEKSİYONU. "koşan" = Start-var-Stop-yok. **Bu m.18 üç-yüz:** makine=JSONL log · insan=tek satır ("3 ajan koşuyor · bugün $2.14 · en pahalı atlas/opus") · talep-üzerine=tam tablo.
**Veri modeli (öneri, V25: kurulum değil dosya-temelli):** `raporlar/usage/olaylar-YYYY-MM-DD.jsonl`, alanlar OTel-GenAI + Claude Code ile hizalı (taşınabilirlik bedava): `{ts,event,run_id,session_id,agent,class,model,effort,query_source,task,status,duration_ms,tokens{in,out,cacheRead,cacheCreation},cost_usd}`.
**Araç referansları (kurma, deseni al):** Langfuse (MIT, maliyet-view referansı) · Vibe Kanban (koşan-ajan pano UI) · disler hook-panosu (SubagentStart/Stop event-akışı) · OTel-GenAI semconv (alan-adları, "Development" statüsü).
**Kanon bağı:** **G4 gözlemlenebilirlik paneli = bu sayfanın ta kendisi** · K-020 besleme (V25 gerilimi: desen-oku-dosya-yaz) · 07-17 ajan-gözlem önerisi (auto-/usage = SubagentStop'ta cost append) · m.37/V39 (bu tablo model-seçim kalibrasyonunun ÖLÇÜM altyapısı — effort×model×maliyet olmadan m.37 öznel) · K-009 "maliyet-gözlem" gündeminin somut cevabı.

## 4. İzleyici + mod-adaptif mimari (Atlas B — DONE)
**Yakınsama:** "tek doğruluk-kaynağı → izleyiciye göre çok görünüm" (SSOT→multi-view = git-as-truth + **m.18**) ve "glanceable = calm technology = ikinci-ekran companion" bağımsız literatürlerde aynı ilkelere vardı.
**Desenler:** persona-bölütlü dashboard (tek ürün, kullanıcı-tipine farklı ilk-görünüm; one-size churn üretir) · rol-bazlı görünüm/RBAC (aynı veri, role göre KPI = **paylaşılan vs Salih-özel**) · operasyonel/analitik/stratejik tipoloji (pano=operasyonel, vardiya-teslim=analitik) · dashboard-IA 6-ilke + görev-bazlı gezinme · **bağlam-adaptif UI / Focus-Mode** (arayüz aktif-uygulama/saate göre yeniden-şekillenir = **mod tetiği**: oyun-odağı→Mod 1) · **voice-first/eyes-free** · **glanceable/preattentive/calm** (1-2sn'de anlaşılır, en az dikkat) · voice+ekran multimodal/10-foot-UI · **earcon eyes-free** · **kesinti 4-katman** (Tier-1 sesli keser, altı sessiz kuyruk) · notification(farkındalık)≠alert(eylem-talep) · **ikinci-ekran companion (oyun)** = Mod 1'in doğrudan modeli (ana ekran=oyun baş-aktör, companion 1-2sn destekler-dağıtmaz).
**Sayfa-haritası — 3 kategori (SSOT → m.18 yüzler):**
- **A · Paylaşılan/Gözlemlenebilirlik** (Carvis hazırlar, Salih denetler): Durum · Pano · **Orkestrasyon/Ajan [BLOKE K-009]** · Vardiya-teslim · Hafıza/karar-tarihçesi · Wiki.
- **B · Salih-özel:** Kararlar/onay kuyruğu (m.31 eşik + m.16 artı-eksi-plan + veto=revert) · **Kişi düzlemi (m.28, yalnız Salih, karantina)** · Fikir kutusu.
- **C · Mod sayfaları (bağlam-adaptif):** Konuşarak İnşa Modu 1 (§6) · Uyku/gece-vardiyası [BLOKE] · Günaydın modu.
Ayrım ekseni = **izleyici (m.28) × aciliyet (op/analitik) × mahremiyet (m.14)**.
**Dürüstlük (şerit-B):** "rapor 1 §9" + "L1 ses" şerit-B'nin taramasında repoda görünmedi (bu oturumun branch raporları; şerit semantik-çapa aldı) — ama ikisi de bu oturumda commit'li (`2026-07-17-otomasyon-vizyon-mimarisi-3model.md`); "oyun ikinci-ekranı" kanonda YENİ (m.27 üstüne sentez).

## 5. Önerilen sayfa-haritası (ön-taslak; §4 rafine edecek)
| Sayfa | İzleyici | Dizayn özü | Veri kaynağı |
|---|---|---|---|
| Kararlar kısmı | Salih-birincil | öneri-vurgulu 3-model kartı, sesli/mobil onay | senaryo-defteri (pending) |
| Gözlemlenebilirlik | Paylaşılan (Carvis+Salih) | canlı koşan-ajan satırı + usage tablosu | usage JSONL projeksiyonu |
| Pano/kapsül | Paylaşılan | AKTİF/BEKLEYEN/BLOKE + durum tek-satır | pano.md + kapsül |
| Konuşarak İnşa Modu 1 | Salih-özel | tek-bakışta, sesli-öncelikli, minimal (§6) | pending karar + sıradaki-iş + son-çıktı |
| POP-backlog / karar-log / öğrenme | Salih-özel/paylaşılan | liste/timeline | ilgili dosyalar |

## 6. "Konuşarak İnşa Modu 1" — sayfa taslağı (Atlas B — DONE; TASARIM, inşa emri değil m.13)
**Model:** oyun = baş aktör (PC penceresi+eller oyunda), telefon = **ikinci-ekran companion** (destekler-dağıtmaz). **Tetik:** oyun pencere-odağı alınca mod otomatik açılır (bağlam-adaptif, iOS-Focus benzeri) — rapor 1 §L1 "oyun=pencere-odağı→ikinci-ekran/telefon" kuralının somutlaşması.
**Dizayn ilkeleri (kaynaklı):** ① sesli-öncelikli eyes-free birincil (ekran tamamlayıcı) · ② glanceable/calm (okuma <1-2sn, sessiz-DND varsayılan) · ③ earcon+kısa-TTS döngüsü (dinliyor→işliyor→bitti/hata; göz oyunda→ses döngüyü kapatır) · ④ **kesinti-katmanı: yalnız Tier-1 (m.31 Katman-1 kararı) sesli KESER**, gerisi sessiz kuyruk · ⑤ kol-mesafesi tipografi (büyük/yüksek-kontrast, tek birincil satır = m.18 insan-yüzü).
**Ekran (telefon dikey, tek bakış):**
```
ŞU AN: auth-modülü · Adım 3/5 · commit ✓   ← insan-yüzü (m.18), büyük punto
● KOŞUYOR   (yeşil çip — preattentive)
🔊 "test koşuyor" (son TTS izi)
⚠ KARAR GEREK → [dokun]  "PortRisk publish?"  ← YALNIZ Tier-1 (m.31); sesli sorar
▾ 3 bilgi bekliyor  (ambient, sessiz kuyruk)
```
**Ses döngüsü:** komut → *earcon dinliyorum* → işlem → *earcon işliyorum* → kısa TTS özet → *earcon bitti/hata*. Salih gözünü oyundan almadan: komut ver → sesli teyit al → yalnız "KARAR GEREK" earcon'unda ekrana bak.
**Kanon:** m.18 (aynı git-verisi, moda-özel yeni yüz) · m.28 (yalnız İŞ düzlemi; kişi düzlemi Mod 1'e sızmaz) · m.31 (KARAR-GEREK kartı = Katman-1 onayın sesli-minimal hali) · m.13 (TASARIM, build değil) · m.27/V25 (telefon-PC companion ön-koşul, bugün yok; Happy = aday köprü, rapor 1 §L1).

## 7. İnşa (build) — omurga + tech (ön-taslak)
- **Tek veri = git-as-truth; sayfalar = projeksiyon** (event-sourcing). Build opsiyonları kararlar-kısmıyla aynı (rapor 1 §9.6): O1 ride-existing (skill/view + Remote Control) · O2 Artifact karar/tablo kartları · O3 dedicated dashboard (senaryo-defteri+usage-JSONL'i git'ten okuyan hafif app). Gözlemlenebilirlik: dosya-temelli JSONL + jq projeksiyon (V25).
- **Öneri (rapor 1 ile tutarlı):** en ucuz yüz (O1/JSONL) önce, ölçülerek büyür (Model B ölçüm-önce).

## 8. Kanon bağı (özet)
m.18 (tek veri çok yüz) · m.28 (izleyici iki-düzlem) · G4 (gözlemlenebilirlik) · kararlar-kısmı (rapor 1 §9) · L1 ses (rapor 1) · POP O3 (dashboard) · K-020/K-009 (ölçüm+maliyet-gözlem) · V25 (kurulum değil desen).

## 9. ANTİTEZ (çift-atlas karşıt-şerit — 07-18 kuralı retroaktif) — Red-Team + Sentez
> **Çerçeve:** m.37 karşıt-temelin girdisi; tezi ÇÜRÜTMEK değil en güçlü karşıtını STEELMAN etmek. Tez ile BİRLİKTE okunur, yerine geçmez.

**Top karşı-argümanlar (kaynaklı):**
- **Dashboard mezarlığı:** panellerin ~%60-70'i kullanılmaz/terk edilir (endüstri-iddiası). Statik-pano "perfidy" — bayatlar, gerçek sorunu değil önceden-tahmini gösterir (Charity Majors, ⚠snippet). Alert/metrik-yorgunluğu sinyali gömer (IBM).
- **Build-vs-buy bakım-yükü:** özel aracın yıllık bakımı ~%20-30; tek-kullanıcıda da kaçmaz; bu repo private/CV-dışı (m.14) → UI'nin dış-değer üretimi sıfır.
- **★ Gözlemlenebilirlik paneli GEREKSİZ olabilir:** "koşan-ajan/model/effort/usage tablosu" zaten Claude Code **native OTel**'de yayınlanıyor (birincil-doküman, GÜÇLÜ ayak). Üstelik **şu an canlı ajan YOK** (K-009/K-010 bloke, m.30 kapalı) → gözlemlenecek nesne mevcut değil → şimdi-inşa = boş-panele yatırım = **YAGNI/speculative-generality** (Fowler).
- **★ Ses + oyun-oynarken-inşa hata:** dikte kodda düşük-doğruluk (ASR sözdizim/jargon/noktalama); Shneiderman (CACM 2000): problem-çözme ile konuşma AYNI beyin-bölgesi → "zor iş konuşmadan yapılır"; ses geçici/bellek-yükü (7±2); **dual-task interference** çakışan bilişsel kaynak İKİ görevi de bozar; kesinti→tam-odak ~23dk + attention-residue (Mark/Leroy). "İkinci-ekranda ciddi inşa" doğrudan çürür.

**Tezin GERÇEKTEN ayakta kaldığı yer (dürüst steelman):** ① navigasyon-ihtiyacı gerçek (ama mevcut markdown/terminal/git-log yeter — bespoke web-UI değil); ② canlı-ajan tablosu **m.30 aktivasyonunda** meşru-değerli (bugün değil — zamanlama); ③ ses **düşük-sözdizim/yüksek-niyet** işinde 3-5x hızlı (fikir-yakalama, `fikir-kutusu` kuyruklama, wiki-düzyazı dikte — kod-yazımı DEĞİL); earcon/read-back doğru azaltıcı.

**SENTEZ (diyalektik — eksen: zamanlama × kapsam):**
- **Antitez kazanır (bugün, tek-kullanıcı, ajan-öncesi):** gözlemlenebilirlik-sayfasını **ERTELE** (tetik = m.30 yürürlük; o güne dek native-OTel'i hazır-backend'e [SigNoz/Grafana="buy"] bağla, bespoke inşa etme); Salih-özel/mod-sayfaları **kanıt-güdümlü** (m.5, önce tekrarlayan-ağrı sonra sayfa); "oyun-oynarken ciddi inşa" iddiasını **DÜŞÜR**.
- **Tez kazanır (dar, doğru kapsam):** ses-modu = **niyet-yakalama/triyaj** (kod-yazımı değil); LLM-onarım + sesli read-back zorunlu (geçicilik azaltıcı); navigasyon = mevcut yüzeyi genişlet, somut yetersizlikte bespoke'a terfi.
- **Tek cümle:** *Rapor 10'un iki fazla-uzanan iddiası — "çok-sayfalı UI'yi ŞİMDİ inşa et" + "oyun oynarken ciddi kod yaz" — YAGNI (zamanlama) ve dual-task/ses-ergonomisi (kapsam) tarafından yıkılır; ama altındaki iki gerçek ihtiyaç (gezilebilir yüzey + boş-zaman niyet-yakalama) mevcut yüzeyi genişleterek ve sesi triyaja daraltarak, bespoke-inşa ve eş-zamanlı bilişsel-çakışma olmadan karşılanır.*
- ⚠ **Bayraklar:** arxiv 2601.15339 (sesli-kod ASR) erişilemedi/DOĞRULANMADI; "%60-70 / %20-30" endüstri-iddiası (hakemli-değil); Charity Majors snippet-düzeyi. GÜÇLÜ ayaklar: native-OTel (birincil-doküman), Shneiderman (CACM), Gloria Mark/Leroy (hakemli).

## 10. Açık sorular (Salih/Fable — KARAR ALINMADI)
- Sayfa kategorileri: kesin liste ne (paylaşılan vs Salih-özel hangi sayfalar)?
- Gözlemlenebilirlik: OTel açılsın mı (CLAUDE_CODE_ENABLE_TELEMETRY=1) yoksa yalnız hook+headless-json JSONL mi?
- "Konuşarak İnşa Modu 1": ikinci-ekran (telefon) mi, odaktan-bağımsız daemon mı birincil?
- Build: O1 ride-existing mi O3 dashboard mı ilk?
