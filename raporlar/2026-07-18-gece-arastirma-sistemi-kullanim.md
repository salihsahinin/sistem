# Gece-Araştırma Sistemi + JARVIS'i Gece En İyi Kullanma — Rapor (TARTIŞMA)

> **Mod:** rapor · KARAR YOK · commit onaylı (Salih 07-18); nihai karar = Fable (m.41). Kaynak: Salih 07-18 — "(1) geceleri JARVIS bağlamında araştırma yaptırırım; araştırma sonsuz ama araştırılan yerleri öncelik-partisyonlarına ayırırız + hangi konu hangi derinliğe kadar biliriz; belirli noktadan sonra çok-derin kaynaklar; nihai karar sezgisel-anlaşılmış düzeyde Salih+JARVIS birlikte → derin araştırma bitince benim dilime indirgenmeli; bu fikri rapor yaz. (2) JARVIS'i gece en iyi nasıl kullanırım — şirket/kişisel projeler — araştır çift atlas, rapora ekle." Atlas 2 şerit döndü (a10d055f sonsuz-araştırma+derinlik+indirgeme · a84e1c77 gece-kullanım).

---

## 0. BLUF (indirgemenin kendisiyle başlıyoruz — bu raporun formatı = tezinin kanıtı)
Salih'in **iki** sezgisi de bilimde **olgun** karşılıklara oturuyor; sıfırdan icat yok, **eşleme** var:
- **Gece-araştırma sistemi** = VOI/EIG ile sıralı backlog **+** konu-başına derinlik-kaydı (TRL+kanıt-seviyesi+Rumsfeld) **+** doygunlukta duran döngü **+** [S]/[O]/[T]+BLUF ile indirgenmiş günaydın-brifingi. Dördü m.27 gece-vardiyası içinde tek loop.
- **Gece-kullanım** = "gece" üç ayrı şey (sleep-time compute · scheduled/async koşum · batch); JARVIS'in kastı **scheduled/async**. Görev-uygunluğu = **blast-radius × geri-alınabilirlik** (=rapor 6); gece çekirdeği = **Human-on-the-Loop** (gece öner → sabah onayla). Batch API %50 ucuz.

---

## 1. Salih'in fikri (çekirdek — kendi çerçevesi)
- **Araştırma mantıken SONSUZ** → bitmeyi hedefleme; onun yerine **kapsamı yönet.**
- **Öncelik-partisyonu:** araştırılacak alanlar öncelik-partisyonlarına ayrılır.
- **Derinlik-takibi:** her konu için "hangi derinliğe kadar araştırdık" bilinir (kapsam-derinlik haritası).
- **Derin-kaynak eskalasyonu:** belirli noktadan sonra çok-derin/birincil kaynaklardan araştırma.
- **★ İndirgeme:** derin araştırma bitince, Salih'in (uzman-olmayan) anlayabileceği dile indirgenir — çünkü **nihai karar sezgisel-anlaşılmış düzeyde Salih+JARVIS BİRLİKTE** verilir (m.39b işbölümü + m.17 köprü + m.26 kullanım-kılavuzu).

## 2. Gece-araştırma sistemi tasarımı (Atlas A döndü — 4 parça + döngü)
**★ Bu oturumun kendisi bir kanıt/prototip:** 30+ atlas şeridi, çoğu "[S]/[O] derinlik; WebFetch-403 → birincil [T] kaynak çekilemedi" bayrağı koydu = **derin-kaynak eskalasyonu tam da bu şeritlerin işaretlediği açık.** Yani gece-araştırma sistemi, bu oturumun düzenini sistematikleştirir.

Atlas'ın çekirdek bulgusu: dört parçanın her biri ayrı olgun literatüre oturuyor; şeritler **yakınsadı** (VOI hem önceliklendirmenin hem eskalasyonun hem doygunluğun ortak dili çıktı — triangülasyon, m.37 ruhu).

- **Parça 1 — Öncelik partisyonu (= rapor 6/7):** sonsuz backlog'u **research-front**'lara böl (science-of-science: co-citation/bibliographic-coupling ile alanın "sıcak sınırı"). Her cepheyi **Rumsfeld matrisi**'nde "bilinen-bilinmeyen" olarak deftere yaz (backlog'un asıl kaynağı; kör-nokta yönetimi). Sıralama **iki-hızlı:** rutinde **WSJF** (`Gecikme-Maliyeti / İş-Süresi` — token×zaman eksenlerinizle birebir), kritik/geri-alınamaz kararda **EVPPI/ENBS** ile matematiksel doğrulama. Keşif↔derinleşme = **çok-kollu-haydut** (ε gece-başı yüksek → sabaha düşer).
- **Parça 2 — Kapsam-derinlik haritası (= rapor 11 pointer-grafı):** her konu **iki-boyutlu kayıt** taşır — `(TRL 1-9 olgunluk, kanıt-hiyerarşisi seviyesi)` + hedef-derinlik **[S]/[O]/[T]**. TRL tek-skala "olgun ama zayıf-kanıtlı"yı gizler; iki-eksen açığa çıkarır. "Hangi konu hangi derinlikte" = makine-okunur (m.18 makine-yüzü). Skala [S] **sezgisel-tarama** · [O] **orta** (mekanizma, ikincil) · [T] **tam** (birincil/derin, matematik/kanıt). MOC/hub-not (rapor 11) = araştırma-cephesinin giriş noktası.
- **Parça 3 — Eskalasyon (özet→birincil):** özet-katmanda kal; **yalnız** kalan belirsizlik Salih'in kararını değiştirebiliyorsa (EVSI > maliyet, ENBS>0) birincil kaynağa in. Mekanik: kanıt-piramidini tersten tırman (tersiyer→sekonder→**primer**) + **snowballing** (geri: kaynak-listesi tara / ileri: kim atıfladı). **DUR:** arama-doygunluğu (tekrar-isabet ↑, "zaten-listede" oranı yükselir) VEYA ENBS≤0. Pratik: kaç seviye derine önceden karar ver.
- **Parça 4 — ★ İndirgeme (Salih-diline):** çıktı formatı **BLUF açılış** (karar + "so what" ilk cümle — istihbarat-kökenli; karar-verici her kelimeyi okuyamaz) → **[S] sezgisel gövde** (Feynman: jargon = bulanıklık işareti, sadeleştir) → talep üzerine **[O]/[T]** (**progressive disclosure**, Nielsen — [S]/[O]/[T]'nin UX-teorik temeli) → **m.37 üç-model** karar-sunumu. İlke: **"ustalık için değil, KARAR için açıklama"** — her derin bulgu "bu bizim hangi kararımızı nasıl etkiler"e bağlanır (= V55 pasif-okuma + m.17 köprünün araştırmaya uygulanması; ogrenme/README [S] tanımıyla birebir).
- **Döngü — Doygunlukta dur (m.37):** her gece-vardiyası bir konuyu **information-power** beş-boyutuna göre tartar (amaç-darlığı · örnek-özgüllüğü · teori-kullanımı · diyalog-kalitesi · analiz-stratejisi); marjinal bilgi maliyeti aşınca konu **DONE**, sıradaki cepheye geçilir. Log defter/senaryo-defterine (m.37 kalibrasyon hammaddesi).

**Matematik kalp (istendi):** `ENBS = EVSI − maliyet(çalışma); ENBS>0 ise araştır, max-ENBS seç` (VOI: Raiffa-Howard). Bir-sonraki-en-iyi-sorgu: `EIG(ξ) = H[p(θ)] − E H[p(θ|y,ξ)]` (Shannon-entropi azalması = BALD/aktif-öğrenme). **Birleştirici içgörü:** doygunluk = VOI'nin kalitatif yüzü — *bir sonraki adımın beklenen bilgi kazancı maliyetini aşmıyorsa dur.*

**Dürüstlük (Atlas A):** akademik yayıncılar (Springer/Oxford/SMDM) 403 (Cloudflare) → derin-alıntılar WebSearch-özeti + textbook-bilgiden; kavramlar çok-kaynak doğrulandı ama tam-metin okunmadı. Doygunluk eleştirilen kavram (Tight 2024; Guest 2021: önceden öngörülemez, geriye-dönük doğrulanır) → durma-eşiği **deneysel-damgalı** tutulmalı (m.29). SOLO/Bloom, expertise-reversal, PD-yüzde-rakamları [O]-düzey, doğrulanmadı.

## 3. JARVIS'i gece en iyi kullanma (Atlas B döndü — playbook)
**★ Ontolojik netlik — "GECE" üç ayrı şey:**
1. **Sleep-time compute** (Letta/Berkeley) = ajan boştayken bağlamı önden işler; bir *verimlilik tekniği*, gece-işi değil. Salt-okuma/dahili → düşük-blast. (⚠ "3×/10k-token" rakamı ikincil blog, birincil paper çekilmedi.)
2. **Scheduled/async gece-koşumu** = zamanlı/arka-plan ajan gece boyu kod/araştırma üretir (Routines, headless `-p`, cron, background-agents). **Salih'in kastı bu = m.27.**
3. **Gecelik-batch** = çok bağımsız işi asenkron kuyruğa at, %50 indirimli koş. Maliyet katmanı.

**★ Görev-uygunluğu = blast-radius × geri-alınabilirlik (=rapor 6, dış-teyit).** Üç gözetim katmanı:

| Katman | Ne zaman | Gece-uygun |
|---|---|---|
| Human-**in**-Loop (önce-onay) | Geri-alınamaz eylem | HAYIR (gündüz) |
| Human-**on**-Loop (sonra-inceleme) | Güvenilir süreç, sabah incele | **EVET — gece çekirdeği** |
| Human-**out**-Loop (tam otonom) | Ön-onaylı düşük-risk + izleme | Yalnız kanıtlanmış dar iş |

| GECE-gözetimsiz (düşük-blast/geri-alınabilir) | GÜNDÜZ-gözetimli (yüksek-blast/geri-alınamaz) |
|---|---|
| Literatür/araştırma toplama, sentez | `main`'e merge, publish, deploy |
| Kod-üret → **taslak-PR** (merge sabah) | Para / API-anahtarı / secret |
| Deney/backtest süpürmesi (sandbox) | Kayıt-silme, tablo-drop, prod-komut |
| Doküman/özet/sınıflandırma | Kişisel-veri, regüle iş |
| Refactor **izole worktree'de** | Bağımlılık-major-yükseltme (sabah gözle) |
| Bakım: temizlik/damıtma/pointer-tazeleme | Şema/migration, geri-alınamaz veri-dönüşümü |

**Playbook (ortak iskelet, m.27 kadansı):** iyi geceler → uyku-vardiyası spec'i → gece koşum (izole/salt-üretim) → günaydın teslim → sabah insan-onayı. Çıktı daima *öneri/taslak* ("agent proposes, human disposes").
- **ŞİRKET (PortRisk):** gecelik backtest/parametre-süpürmesi (Batch/W&B/Azure-ML sweep) → sabah standart-rapor. **★ Finans-uyarı:** *look-ahead bias* — gece üretilen strateji-kodu **sabah insan-doğrulaması olmadan canlıya/karar-girdisine bağlanmaz** (yüksek-blast). Strateji-seçimi/sermaye-etkisi = m.31 Katman-1, gündüz-Salih.
- **KİŞİSEL:** spec-before-bed → sabah taslak-PR (küçük özellik/bugfix yatmadan spec'le, gece izole-worktree üretir, sabah incele — "taze-göz gece-yarısından iyi"). Bağımsız 2-3 işi paralel fan-out.
- **ÖĞRENME:** Batch API ile "N konu → sentez/özet/kaynak" gece kuyruğu (%50, yan-etkisiz) → sabah `morning` brifingi. Wiki-besleme: gece kavram-sayfası taslağı → sabah insan-damıtması (silme-yok arşiv, m.8/m.34).
- **BAKIM (en gece-uygun, en düşük-blast):** kapsül/pano bayatlık-taraması, pointer-doğrulama (kırık [[wiki-link]]), arşiv-ingest. **DİKKAT:** `core/` yalnız Salih + otomatik-silme yasağı (m.8) → bakım-ajanı **öneri üretir, uygulamaz**; silme/birleştirme Katman-1.

**Maliyet:** Batch API **%50** (girdi+çıktı, tüm modeller, eşiksiz, ≤24s SLA) → gece = doğal batch penceresi. İstifleme: Batch×prompt-caching → sistem-payı efektif ~%5. Headless sert-tavan: `max_budget_usd` (aşınca DURUR) + `max_turns` + oto-compaction. (⚠ 15-Haz-2026 kredi-havuzu faturalaması $20/$100/$200 — ikincil kaynak, resmi docs'a doğrulanmalı; gece-gözetimsiz için bağlayıcı.)

**Güvenlik (gece ne ters gider):** prompt-injection, **memory-poisoning** (sahte talimat kalıcı), **kaçak-maliyet** (token-patlaması), **cascading-failure** (döngü, circuit-breaker yoksa görünmez). Guardrail (JARVIS 07-17 zaten haritaladı): **PreToolUse** = m.31 Katman-1'i koda-dök (allow/deny/ask, policy-as-code); gözetimsizde **`--allowedTools` tek kapı, opsiyonel değil** · sandbox (dosya+ağ egress çiti) · sert bütçe/kota · memory-write-validation + circuit-breaker · **zorunlu sabah-insan-inceleme** ("gece öner, sabah onayla") · izole worktree/`claude/`-önekli dal → gece hiçbir şey `main`'e değmez. **Kanon-uyumu:** G4 güvenlik < G5 otonomi (sıra bozulamaz) → gözetimsiz-gece açılmadan ÖNCE PreToolUse dilimi.

## 4. Kanon bağı
- **m.27 (uyku/günaydın vardiya):** "iyi geceler"→gece-araştırma/koşum vardiyası · "günaydın"→teslim (BLUF+indirgenmiş). Bu rapor m.27'nin araştırma+koşum yüzü; spec-before-bed→morning-review deseniyle birebir.
- **ogrenme/ [S/O/T] + V55:** derinlik-etiketi + indirgeme formatı = progressive-disclosure + expertise-kademeli açıklamanın UX/pedagoji temeli (tam grounded).
- **K-009 (Routines, BLOKE m.30):** gece-gözetimsiz K-009 kapısında; açılış = Katman-1/Salih. Bugün: Faz-4 tek-atış Routine (07-17) + Salih-tetikli/sabah-inceleme. Tasarım hazır, otonomi Salih'te.
- **rapor 1** (otonomi merdiveni = HITL→HOTL→HOOTL) · **rapor 6/7** (blast×geri-alınabilirlik = onay-eşiği + öncelik/tetik) · **rapor 10** (gözlemlenebilirlik = guardrail ön-koşulu) · **rapor 11** (derinlik-haritası = research-MOC) · **rapor 5** (partisyon) · **`morning` skill** (teslim okuyucu-yüzü; ⚠ `skills/` dizini repoda bulunamadı — fikri-kutusunda "kapsanan" listeli, fiziksel dosya doğrulanamadı).
- **m.21 token×zaman:** gece = ucuz-token penceresi (batch); derinlik token-bütçesiyle ölçeklenir. WSJF `İş-Süresi`=zaman, `Gecikme-Maliyeti`=değer.
- **m.37 yakınsama** (saturation durma-kuralı) · **m.34** (derinlik-log ingest hammaddesi).

## 5. Açık sorular (Salih/Fable — KARAR ALINMADI)
- Derinlik skalası [S]/[O]/[T] araştırmaya aynen mi taşınsın, yoksa `(TRL, kanıt-seviyesi)` iki-eksen ayrı mı tutulsun?
- Gece-araştırma Routine olarak mı (K-009 kapısı) yoksa Salih-tetikli tek-atış mı başlasın?
- İndirgeme her gece otomatik (BLUF sabah-brifingi) mi, talep-üzerine mi?
- Kapsam-derinlik haritası ayrı dosya mı (`raporlar/arastirma-cephe-haritasi.md`) yoksa rapor 11 pointer-grafına mı gömülsün?
- Önceliklendirme rutinde WSJF, kritikte ENBS: eşik nerede (hangi karar "kritik" sayılır)?
- Gece-güvenlik: PreToolUse allowlist dilimi K-009 açılışının ÖN-KOŞULU mu (G4<G5)?
