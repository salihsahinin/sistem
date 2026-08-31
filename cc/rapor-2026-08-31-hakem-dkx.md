# Maskeli Hakem — D/K/X hükümleri (İB-67 + İB-68 aday havuzu)

**Künye:** AS-OF 2026-08-31 · maskeli hakem (m.40b) · model opus · dizin `/Users/HasanSalihSahin/jarvis` · web KULLANILMADI, yalnız 8 verilen rapor değerlendirildi · kaynak dosyalar: `cc/rapor-2026-08-31-ib67-{c-ic-envanter,a1,a2,a3}-*.md`, `cc/rapor-2026-08-31-ib68-{c-ic-envanter,b1,b2,b3}-*.md`

**Hüküm kuralı:** D = kanıt iddiayı taşıyor (repo-içi birebir alıntılı ölçüm ∨ açılmış birincil kaynak) · K = kanıtın bir kısmı var, birleşim/kritik ayak eksik · X = kaynak açılmamış + sayısal/kesin ∨ `[?]` üzerine kurulu ∨ iddia kanıtı aşıyor. Sertlik kuralı uygulandı: "arama-sonucu" etiketli (URL açılmamış) kaynağa dayanan sayısal/kesin iddia ≤ K; tutar/rakam içeriyorsa X.

---

## (1) D/K/X iddia tablosu

| # | Kaynak | İddia (ayırt edici) | Hüküm | Gerekçe |
|---|---|---|---|---|
| 1 | ib67-C | Kırık dosya_pointer 1.306 / toplam 9.793 (çözümlü 8.487) | **D** | Repo-içi kapsama haritasından birebir alıntı, üretici pointer'lı |
| 2 | ib67-C | Satırlı pointer (`yol:123`) 380, satırsız backtick 4.999 | **D** | Aynı repo-içi ölçüm, birebir alıntı |
| 3 | ib67-C | "dosya:satır + layout birleşik şeması emsalsiz alan" | **X** | Emsalsizlik dış-tarama hükmü; A1 aynı iddiayı DAYANAKSIZ etiketledi, kanıtı aşıyor |
| 4 | ib67-C | En yakın tabanlar SourcetrailDB/SARIF/Sprotty `trace` | **K** | İsimler makul komşu; A1'de yalnız SourcetrailDB arama-sonucu olarak çıktı, SARIF/Sprotty karşılaştırması yapılamadı |
| 5 | ib67-C | D2 üretimi 58/58 kenar, P=R=1,0, 5/5 birebir | **D** | `tools/d2-eval.py` + `veri/d2-eval.jsonl` pointer'lı, birebir alıntı |
| 6 | ib67-C | Okuma: kenar listesi 24/25 = %96, SQL-devri 25/25 = %100 | **D** | Repo-içi eval kütüğünden birebir alıntı, tek hata (o5) adlandırılmış |
| 7 | ib67-C | Biçim-ayrımı 5,5× (2,4 KB ↔ 13,0 KB) | **D** | Repo-içi ölçüm, iki uç değer alıntılı |
| 8 | ib67-C | "Literatürde D2 için benchmark yok, bu ilk ölçümdür" | **K** | Yokluk hükmü repo-içi ölçümle kanıtlanamaz; A1 bağımsız olarak "D2'ye özel yayın bulunamadı" dedi ama tarama arama-sonucu düzeyinde |
| 9 | ib67-C | ask_oran sınıflama sayımı: ANA-SIRA 3 · BELİRSİZ 11 · HEADLESS-ADAY 6 · ZATEN-HEADLESS 27 (47) | **D** | `tools/headless-esleme.py` + silver `hareket` kaynaklı, satır örnekli |
| 10 | ib67-C | Veri tabanı 62 oturum / 4.206 çağrı | **D** | Silver katman ölçümü, pointer'lı |
| 11 | ib67-C | ask_oran "insan kararı gerekliliğini dolaylı gözlemden çıkarsayan" özgün proxy | **X** | Özgünlük ayağı A2'de HiL-Bench + Levels-of-Autonomy ile çürüğe düştü; iddia kanıtı aşıyor |
| 12 | ib67-C | Kural envanteri: T0+T1 = 71 birim / 21,8 KB; toplam 1.017 birim / 339.142 B / 49 dosya | **D** | `tools/kural-envanter.py` + gold görünüm pointer'lı, birebir alıntı |
| 13 | ib67-C | ≤100 birim eşiği: "ortalama 2 çağrı-skill ile 71 + 2×14,5 = 100" | **K** | Aritmetik repo-içi ölçümden türetilebilir; "ortalama 2 skill" varsayımı ölçülmemiş |
| 14 | ib67-C | IFScale: en iyi model 500 talimatta %68 | **D** | A3'te birincil kaynak (arXiv 2507.11538) AÇILDI ve rakam birebir teyit edildi |
| 15 | ib67-C | "Kural bütçesini IFScale'e karşı kalibre eden İLK ölçüm" | **K** | Ölçüm D; "ilk" ayağı A3'te yalnız bulunamama (negatif kanıt) ile desteklendi |
| 16 | ib67-C | 12 araç × 5 kriter matrisinde K1∧K2∧K3∧K4 = 0/12 | **K** | Matris dış araç iddialarına dayanıyor, sütunlarda 1-4 `[?]` var; A3 LumiMAS'ı açamadı → çürütülemedi de |
| 17 | ib67-C | Darboğaz K3: 12 araçta yalnız 1 net EVET (Devin) | **K** | Aynı matrisin türevi; Devin satırı açılmış kaynakla doğrulanmadı |
| 18 | ib67-C | Kendi denetimi: örneklem sondajı 9 iddiadan 5'ini doğruladı (%55,6), 6 ihlal | **D** | Raporun kendi denetim sayımı, birebir alıntılı ve kendi aleyhine |
| 19 | ib67-C | İB-66 hakem dağılımı D 27 · K 11 · X 8 | **D** | Birebir alıntılı iç sayım |
| 20 | ib67-C | Boşluğu kapatan tasarım "sıfır-ek-token maliyetli" | **X** | Maliyet iddiası; hiçbir ölçüm/alıntı verilmemiş |
| 21 | ib67-A1 | SourcetrailDB, source-map spec, lcodemaps, parse-then-place layout IR mevcut | **K** | Hepsi "arama-sonucu, açılmadı"; varlıkları makul, içerik eşleşmesi doğrulanmamış |
| 22 | ib67-A1 | İB-53 için birleşik yayın "GÖSTERMEDİ" ama negatif kanıt zayıf | **D** | Raporun kendi sınırını açıkça beyan etmesi, kanıt-düzeyiyle tutarlı |
| 23 | ib67-A1 | MermaidSeqBench (2511.14967) / OmniDiagram / M³²Bench / DW-Bench / Lost-in-Serialization D2 içermiyor | **K** | Arama-sonucu düzeyinde; "D2 yok" negatif hükmü açılmış kaynakla test edilmedi |
| 24 | ib67-A1 | ONTO JSON'a göre %46-51 token azaltımı | **X** | Açılmamış kaynaktan sayısal iddia |
| 25 | ib67-A1 | GraphLLM bağlam uzunluğunu %96,45 azaltıyor | **X** | Açılmamış kaynaktan kesin ondalık rakam |
| 26 | ib67-A1 | Token-verimlilik: List-of-Edges <3000 token, JSON-LD >13000 token | **X** | Açılmamış kaynaktan sayısal aralık |
| 27 | ib67-A1 | CoAgent (2606.15376) Bernstein-türü kontrolü LLM-ajanına uyarlıyor ve LLM'i conflict-yargısına dahil ediyor | **K** | Doğrudan rakip olarak makul; içerik açılmamış, MTPO detayı doğrulanmamış |
| 28 | ib67-A1 | ATM "pre-write admission" (2607.00041) bizim kapı kavramına çok yakın | **X** | Rapor kendi içinde "içerik bu turda açılmadı `[?]`" diyor; yakınlık hükmü `[?]` üstüne kurulu |
| 29 | ib67-A2 | Cache-read maliyeti standart girdinin ~%10-25'i | **X** | Açılmamış "genel bulgu" üzerinden sayısal aralık |
| 30 | ib67-A2 | "~300k/iterasyon taban + ajan-turu-uykusu maliyet sınıfı" birleşimi literatürde bulunamadı | **K** | Bulunamama beyanı dürüst; ama tabanın kendisi bu raporda ölçümle desteklenmiyor |
| 31 | ib67-A2 | "Ajanın kendi repo-güvenlik freniyle çarpışması" ayrı olay sınıfı olarak literatürde yok | **K** | Negatif tarama sonucu; 3 sorguluk arama-sonucu tabanı zayıf |
| 32 | ib67-A2 | HiL-Bench: tam bilgiyle %75-89 pass@3, ne zaman soracağını bilmesi gerektiğinde %4-24 | **X** | Açılmamış kaynaktan iki sayısal aralık |
| 33 | ib67-A2 | Uncertainty-Aware Clarification: mesaj sıklığı 0,7-8,3/koşum | **X** | Açılmamış kaynaktan sayısal aralık |
| 34 | ib67-A2 | Levels of Autonomy (2506.12469) log/diary'den post-hoc otonomi sınıflaması öneriyor → ask_oran'a çok yakın | **K** | Mekanizma yakınlığı makul; kaynak açılmamış, birebir eşleşme test edilmemiş |
| 35 | ib67-A2 | A1-A4 merdiveni mekanizma düzeyinde önceden var (Autonomy Gate, Falsifiable Release Gates, CAGE-1, Augment L0-L4) | **K** | Beş bağımsız komşu ismi + iki farklı hat (akademik/endüstri) yakınsıyor; hiçbiri açılmadı, ama çokluk hükmü taşıyor |
| 36 | ib67-A2 | "%40 müdahale gerektiren ajan üretime hazır değil" (Augment) | **X** | Açılmamış blog kaynağından sayısal eşik |
| 37 | ib67-A3 | IFScale künyesi: yazarlar, arXiv 2507.11538, 15 Temmuz 2025, N=10→500, 20 model/7 sağlayıcı | **D** | Birincil kaynak açıldı ve raporda beyan edildi — havuzdaki tek tam-doğrulanmış dış künye |
| 38 | ib67-A3 | ManyIFEval / AGENTIF / Many-Tier Hierarchy (2604.09443) kural-bütçesi eksenine kısmen komşu | **K** | Arama-sonucu düzeyi; "T0-T4 eksenine özgü değil" ayrımı makul ama doğrulanmamış |
| 39 | ib67-A3 | T0-T4 taşıyıcı-sınıfı × görev-sınıfı çapraz tablosu literatürde YOK | **K** | Rapor kendisi "negatif kanıt mutlak ispat değil `[?]`" diyor |
| 40 | ib67-A3 | LumiMAS (2508.12412) gerçek-zamanlı çok-ajan gözlem sunuyor → 0/12 için potansiyel ÇELİŞKİ | **K** | Rapor açıkça "kaç kriteri karşıladığı doğrulanmadı `[?]`" diyor; risk gerçek, hüküm askıda |
| 41 | ib67-A3 | Parçalı gözlemlenebilirlik üst-tezi survey'lerle destekli, yani yeni değil | **K** | Survey adları arama-sonucu; tema-düzeyi çıkarım makul |
| 42 | ib68-C | `veri/bronz/hareket-olay.jsonl` 5163 satır | **D** | Birebir ölçülmüş repo-içi sayım |
| 43 | ib68-C | AXI uyumu: `tools/*.py` 43 · `--json` 8 · `--sessiz` 30 | **D** | Dosya-içi ölçüm satırı, kaynaklı |
| 44 | ib68-C | paralel-kapı pilotu: 8 birim / 28 çift, N=1→2→3, çakışma 0, kapı çıkışı 0, ~14 eşzamanlı ajan | **D** | `raporlar/2026-08-30-paralel-kademe-pilot.md` pointer'lı, birebir |
| 45 | ib68-C | gnhf e600a7: 3M token tavan, 3/3 iterasyon, 0 arıza | **D** | `raporlar/...k010-a3-loop-1.md:12-13` satır-pointer'lı |
| 46 | ib68-C | `veri/manifest/*.json` 17 dosya · `tools/gnhf-izle.py` 92 satır, çıkış kodu 0/2 | **D** | Doğrudan dosya sayımı/okuması |
| 47 | ib68-C | Karar-masası: "7 karttan 5'i tek turda hükme bağlandı" | **K** | Tek koşum, anlatı kaydından; raporun kendisi "kod-çekirdeği bulunamadı `[?]`" diyor |
| 48 | ib68-C | Repo-freni PreToolUse canlı PASS vakası var | **X** | Rapor "bu ajanın bütçesinde doğrulanmadı `[?]`" diyor — `[?]` üstüne kurulu |
| 49 | ib68-C | A1-A4 durum: A1 5/5, A2 tamam, A3 2/3, A4 bekliyor | **D** | `kuyruk/k010-zincir-2026-08-29.md:1-56` pointer'lı; A3'ün eksikliği açıkça beyan edilmiş |
| 50 | ib68-B1 | Ajan-gözlemlenebilirlik alanında ≥8 isimli aktif oyuncu (LangGraph Studio, AgentOps, Langfuse, Phoenix, Braintrust, LangSmith, AutoGen Studio…) | **K** | İsim çokluğu tutarlı ve çapraz-raporla örtüşüyor; hiçbiri açılmadı |
| 51 | ib68-B1 | AgentOps ~5,6k GitHub yıldızı | **X** | Açılmamış tek arama-sonucundan sayısal iddia |
| 52 | ib68-B1 | Langfuse 2026-01'de Clickhouse tarafından satın alındı | **X** | Açılmamış tek kaynaktan kesin olay/tarih iddiası |
| 53 | ib68-B1 | Claude-Code JSONL izleyicisi olarak ≥8 ücretsiz OSS klon var (claude-code-log-viewer-cli, claude-code-trace, agent-flow…) | **K** | İsim listesi zengin ve iç-tutarlı; hiçbiri açılmadı, yıldız/aktiflik `[?]` |
| 54 | ib68-B1 | OpenTelemetry GenAI Semantic Conventions AXI'nin en güçlü doğrudan rakibi; CNCF'ye geçti (2026-05) | **K** | Rakiplik hükmü makul ve kategori-doğru; CNCF tarihi açılmamış kaynak → tarih ayağı zayıf |
| 55 | ib68-B1 | "%89 üretim kullanıcısı OTel uyumluluğunu çok önemli görüyor" | **X** | Açılmamış tek kaynaktan sayısal iddia |
| 56 | ib68-B1 | Helicone "bakım modunda" | **X** | Rapor kendi içinde DAYANAKSIZ/tek-kaynak diyor |
| 57 | ib68-B2 | Nx 22.7 "task sandboxing" gerçek I/O'yu deklarasyonla karşılaştırıp ihlal işaretliyor → Bernstein-benzeri en yakın kavramsal rakip | **K** | Mekanizma eşleşmesi ikna edici ve ayrımı (deklare-sonra doğrulama ≠ koşum-öncesi kapı) net; kaynak açılmadı |
| 58 | ib68-B2 | Crystal 2026-02'de DEPRECATED, kullanıcılar Nimbalyst'e yönlendi | **K** | Rakip-blog kaynağı, açılmadı; tutar içermiyor, olay-iddiası olarak K |
| 59 | ib68-B2 | Conductor ücretli plan VAR | **K** | Rapor iki çelişen kaynak beyan ediyor (ÇELİŞİR notu) → tek yönlü kesinlik yok |
| 60 | ib68-B2 | Invariant Labs 2025-06'da Snyk tarafından satın alındı | **X** | Açılmamış kaynaktan kesin M&A olay+tarih iddiası |
| 61 | ib68-B2 | Repo-freni için "rakip yok" iddiası ÇELİŞİR — alan doygun (Lakera, NeMo, OPA, Claude Code hooks) | **K** | Kategori doygunluğu çok kaynakla tutarlı; tekil doğrulama yok |
| 62 | ib68-B2 | HumanLayer (YC F24) karar-masasının doğrudan-isim rakibi, ücretli planı var | **K** | Ürün-tanımı eşleşmesi güçlü; fiyat/finansman ikinci-el (getlatka), rapor kendisi DAYANAKSIZ diyor |
| 63 | ib68-B3 | Langfuse Core $29 / Pro $199 / Enterprise $2.499, LangSmith $39/koltuk, Braintrust $249, Galileo $100 | **X** | Açılmamış arama-sonucundan TUTAR — sertlik kuralı gereği X |
| 64 | ib68-B3 | Continue.dev $2,1M seed aldı ve Anysphere tarafından satın alındı; Starter $3/M token, Team $20/koltuk | **X** | Açılmamış kaynaktan tutar + M&A iddiası |
| 65 | ib68-B3 | "Koşum-sayılı kanıt kapısı" kavramına birebir eşleşen ürün adı bulunamadı; en yakını isimsiz shadow/canary/percentage/full deseni | **K** | Negatif tarama; 3 sorgu, hiçbir kaynak açılmadı |
| 66 | ib68-B3 | Aider'ın ücretli planı/fatura altyapısı YOK (saf OSS, tek geliştirici) | **K** | Yaygın-bilgiyle tutarlı, kategori-doğru; kaynak açılmadı |
| 67 | ib68-B3 | Genel agent-eval/gözlemlenebilirlik pazarı DOYGUN ve ödeme-kanıtlı | **K** | Çoklu ürün + fiyat-sayfası varlığı yakınsıyor; tutarlar X'lendi, doygunluk hükmü ayakta |

---

## (2) Toplam sayım

| Hüküm | Adet | Pay |
|---|---|---|
| **D (destekli)** | 19 | %28,4 |
| **K (kısmi)** | 31 | %46,3 |
| **X (dayanaksız/çürük)** | 17 | %25,4 |
| **Toplam** | 67 | — |

Kaynak dosya bazında: ib67-C 12D/5K/3X · ib67-A1 1D/4K/3X · ib67-A2 0D/4K/4X · ib67-A3 1D/4K/0X · ib68-C 8D/1K/1X (49 dahil) · ib68-B1 0D/4K/4X · ib68-B2 0D/5K/1X · ib68-B3 0D/3K/2X.
Yapısal örüntü: **tüm D'ler repo-içi ölçümlerden ve tek açılmış dış kaynaktan (IFScale) geliyor**; dış-kaynak ailelerinde (A1/A2/B1/B3) sıfır D var — 8 raporun tamamında birincil kaynak yalnız BİR kez açılmış.

---

## (3) İB-67 aday hükümleri (YENİLİK)

| # | Aday | Hüküm | Tek cümle gerekçe |
|---|---|---|---|
| 1 | İB-53 dosya:satır+layout birleşik IR | **KISMİ** | Repo-içi pointer sayımları sağlam ama "emsalsiz" hükmü SARIF/Sprotty/mdast ile hiç karşılaştırılamadı, yani yenilik ne kuruldu ne yıkıldı. |
| 2 | İB-49 D2 eval | **KISMİ (YOK-bulundu'ya en yakın)** | Ölçümlerin tamamı repo-içi, birebir ve tekrar-üretilebilir; "D2 için benchmark yok" alt-iddiası bağımsız antitez turunda ayakta kaldı, ama "tool-offload > metin-sayma" ve "biçim↔token farkı" mekanizmaları DW-Bench/Lost-in-Serialization/ONTO ile zaten kaplı. |
| 3 | paralel-kapı / Bernstein kapısı | **KISMİ** | CoAgent aynı problem uzayında rakip çözüm olarak duruyor ve ATM'nin "pre-write admission" başlığı açılmadan kaldı; ayakta kalan tek fark "LLM'siz + beyan-edilmiş manifest + koşum-öncesi" bileşimi. |
| 4 | gnhf vakaları (token tabanı / fren çarpışması) | **DÜŞTÜ** | ~300k taban ve uyku-maliyeti olgu-kaydı düzeyinde, cache-read/bütçe-farkındalık literatürü zaten var; "kendi freniyle çarpışma" ise tek vaka, yenilik iddiası olarak çerçevelenemiyor. |
| 5 | İB-57 ask_oran | **DÜŞTÜ** | Soru-sorma sıklığından otonomi türetme HiL-Bench'te doğrudan ölçülüyor ve Levels-of-Autonomy log-tabanlı post-hoc sınıflandırmayı zaten öneriyor; geriye yalnız yerel eşik seçimi kalıyor. |
| 6 | A1-A4 otonomi merdiveni | **DÜŞTÜ** | Kanıt-kapılı kademeli otonomi hem akademik (Falsifiable Release Gates, CAGE-1) hem endüstriyel (Autonomy Gate, L0-L4 pilot-to-production) beş ayrı komşuyla karşılanıyor; özgün pay yalnız adlandırma. |
| 7 | İB-51 kural envanteri / IFScale | **KISMİ (havuzun en güçlüsü)** | Tek tam-doğrulanmış dış çapa burada (IFScale %68@500 birincil kaynaktan teyitli) ve repo-içi 1.017 birim ölçümü sağlam; düşen kısım "talimat sayısı↔uyum eğrisi" fikri, ayakta kalan kısım T0-T4 taşıyıcı ekseni. |
| 8 | İB-66 nested-loop boşluğu | **KISMİ** | Metodoloji (tarama-öncesi sabit kriter + 0/12) özgün ve raporun kendi denetimi dürüst (%55,6 doğrulama, 6 ihlal), ama matrisin dayandığı 12 araç iddiası açılmadı ve LumiMAS doğrudan çelişki riski `[?]` olarak açık kaldı. |

**İB-67 dağılımı: YOK-bulundu 0 · KISMİ 5 · DÜŞTÜ 3.**

---

## (4) İB-68 aday hükümleri (PAZAR / REKABET)

| # | Aday | PAZAR | REKABET | Tek cümle gerekçe |
|---|---|---|---|---|
| 1 | Gözlemlenebilir nested-loop koşucusu | **SİNYALLİ** | **DOYGUN** | Kategoride en az beş ödeme-katmanlı oyuncu (AgentOps/Langfuse/Braintrust/Arize AX/LangSmith) var; para akıyor ama "iç-içe + seviye-ayrımlı + müdahale" farkı hiçbir aramada tarif edilmedi. |
| 2 | paralel-kapı + manifest | **SİNYALLİ** | **ORTA** | Worktree-orkestrasyon katmanında ödeme (Conductor) ve kapanış (Crystal) sinyalleri birlikte var; mekanizma eşleşmesi seyrek — en yakını Nx'in deklare-SONRA I/O ihlal bayrağı, koşum-ÖNCESİ kapı değil. |
| 3 | karar-masası | **SİNYALLİ** | **ORTA** | HumanLayer ürün-tanımı + ücretli plan + YC izleriyle doğrudan-isim rakip; bitişik araçlar (Langfuse annotation, n8n, Temporal) tam örtüşmüyor, ama repo tarafında kod-çekirdeği yok `[?]`. |
| 4 | A1-A4 merdiveni | **SİNYALLİ** | **DOYGUN** | Kuşatıcı eval/TRiSM pazarı ödeme-kanıtlı ve kalabalık (Braintrust/LangSmith/Galileo + ModelOp/Scrut/AllTrue); "koşum-sayılı kanıt kapısı" dili seyrek ama bunun ürün-talebine dönüştüğüne dair tek sinyal yok. |
| 5 | gnhf-izle izleyici | **SİNYALSİZ** | **DOYGUN** | Sekiz ücretsiz OSS klonu aynı işi yapıyor ve hiçbirinde fiyat sayfası bulgusu yok — ödeme istekliliği kanıtı sıfır. |
| 6 | repo-freni | **SİNYALLİ** | **DOYGUN** | Lakera ücretli API + Invariant/Snyk M&A ile kategori hem ödemeli hem konsolide oluyor; üstelik Claude Code'un kendi hook sistemi ürünün altında yerleşik alternatif olarak duruyor. |
| 7 | hareket kütüğü + AXI | **SİNYALLİ** | **DOYGUN** | AgentOps ve W&B Weave ücretli planlarıyla kategori ödemeli; ama standart ekseninde OTel GenAI conventions CNCF desteğiyle doğrudan üstte, AXI'nin "standart" konumlandırması savunulamaz. |

**İB-68 dağılımı: SİNYALLİ 6 · SİNYALSİZ 1 · rekabet DOYGUN 5 / ORTA 2 / SEYREK 0.**

---

## (5) Hayatta kalan en güçlüler

**En güçlü paper adayı — İB-49 (D2 üretim/okuma mini-eval).** Havuzda tek başına dört D-etiketli, repo-içi, deterministik harness'la tekrar-üretilebilir ölçüm taşıyan aday bu (58/58 P=R=1,0 · %96↔%100 · 5,5×) ve antitez turunda "D2 için benchmark yok" ayağı çürütülemedi; İB-51 dış-çapası daha sağlam ama katkısı kalibrasyon adımına, İB-66 ise doğrulanmamış 12-araç matrisine dayanıyor.

**En güçlü ürün adayı — İB-68-2 (paralel-kapı + manifest rejimi).** Tek aday ki hem D-etiketli çalışan kanıtı var (8 birim/28 çift, N=1→3, çakışma 0, ~14 eşzamanlı ajan) hem rekabeti DOYGUN değil ORTA hem de en yakın rakibin (Nx) mekanizması ölçülebilir biçimde farklı (koşum-öncesi deterministik hüküm ↔ koşum-sonrası ihlal bayrağı).

---

*Not: Bu hakemlik yeni iddia üretmez; yalnız verilen 8 rapordaki iddiaları kanıt gücüne göre sınıflar. Web kullanılmadı — dış kaynakların DOĞRULANMASI değil, raporlardaki doğrulama-DURUMU değerlendirildi.*
