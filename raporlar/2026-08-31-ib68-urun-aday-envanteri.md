# İB-68 — Ürünleşme-adayı bulgu envanteri + pazar doğrulama atlası

**Künye:** emir `cc/gorev-2026-08-31-ib68-urun-aday-envanteri.md` · HEAD `5218209` · **AS-OF 2026-08-31** · ajan sayısı 10 (C 2 · A 3 · B 3 · V26 1 · hakem 1) · işçi modeli **sonnet** (rejim maliyet-öncelikli) · hakem **opus** (maskeli) · İB-67 ile **ORTAK TARAMA** (tek koşum, iki rapor).

> **Katman-1 şerhi:** ürünleşme/satış PARA ve DIŞARI-ÇIKAN-İŞ sınıfıdır (m.4, m.31). Bu rapor **TESPİT + öneri** üretir, **hüküm vermez**. Dışa temas yapılmadı (md.14, remote private).
>
> **m.39 freni:** rakip fiyat TUTARI bu rapora yazılmamıştır. Yalnız "ücretli plan MEVCUT / YOK / `[?]`" varlık beyanı kullanıldı. B3 ham raporundaki dolar tutarları **V26 ihlali** olarak damgalıdır (açılmamış sayfadan sayısal iddia) ve buraya taşınmadı.

---

## 0. Ana bulgu (çıplak)

7 aday tarandı. **Pazar sinyali: SİNYALLİ 6 · SİNYALSİZ 1.** **Rekabet: DOYGUN 5 · ORTA 2 · SEYREK 0.**

Yani: ödeme akan bir pazar var (kategori canlı), ama **hiçbir adayın rekabeti seyrek değil**. Ürün fırsatı bu koşumda "boş alan" değil, en fazla **mekanizma farkı** olarak duruyor — ve bu farkın müşteri tarafından ödemeye değer bulunduğuna dair kanıt hiçbir adayda YOK.

---

## 1. Aday × repo-kanıtı × pazar-sinyali × rekabet × taşıma-maliyeti (AS-OF 2026-08-31)

| # | Aday | Repo-kanıt pointer'ı | Çalışma kanıtı (birebir) | Pazar sinyali (ödeme kanıtı) | En yakın rakip | Rekabet | Taşıma maliyeti |
|---|---|---|---|---|---|---|---|
| ① | Gözlemlenebilir nested-loop koşucusu | `tools/gnhf-izle.py`; `raporlar/2026-08-31-ib66-*.md`; `raporlar/2026-08-31-ib65-*.md` | e600a7 koşumu: 3M token tavan, 3/3 iterasyon, 0 arıza; İB-66 atlası 6 işçi + 1 hakem | **SİNYALLİ** — kategoride en az 5 ödeme-katmanlı oyuncu (ücretli plan MEVCUT; tutar yazılmadı) | LangGraph Studio · AgentOps · Langfuse · Braintrust · LangSmith · Arize AX | **DOYGUN** (≥8 isimli oyuncu) | 4 madde: worktree bağımlılığını genelleştir · stream-json şeması sürüm kilidi · i18n · hata/timeout testi yok |
| ② | **paralel-kapı + manifest rejimi** | `tools/paralel-kapi.py`; `veri/manifest/*.json` (17); `raporlar/2026-08-30-paralel-kademe-pilot.md` | 8 birim / 28 çift matrisi · N=1→2→3 · **çakışma 0 · kapı çıkışı 0** · ~14 eşzamanlı ajan darboğazsız | **SİNYALLİ** — Conductor ücretli plan MEVCUT (çelişen ikinci kaynak var `[?]`); **negatif sinyal:** Crystal 2026-02'de DEPRECATED | **Nx task sandboxing** (22.7): gerçek I/O'yu izleyip deklare edilenle karşılaştırır — **koşum-SONRASI ihlal bayrağı**, koşum-öncesi kapı değil · Bazel · Conductor · Claude Squad · agentree · vibe-kanban | **ORTA** | 4 madde: manifest şeması jenerikleştir · PK-12 kilit mantığını genel kilide bağla · Bernstein grain=dosya (alt-dosya yok) · CLI paketleme (pip/npm) yok |
| ③ | Karar-masası deseni (insan-hüküm kuyruğu) | `kuyruk/arsiv/senaryo-defteri-arsiv-2026-08-29.md:41`; `kuyruk/gelen-2026-08-30-a1-sayac-karar.md:14` | "7 karttan 5'i tek turda hükme bağlandı" (tek koşum). **Ayrı kod-çekirdeği repo'da YOK** `[?]` — desen Lavish kullanım konvansiyonu olarak kayıtlı | **SİNYALLİ** — HumanLayer (YC F24) ücretli plan MEVCUT + finansman izi | **HumanLayer** — isim + ürün tanımı + ödeme üçlü eşleşme (ajan araç-çağrısı öncesi insana onay) · Langfuse annotation queues · Label Studio · n8n "Require approval" · Temporal Signals | **ORTA** | 4 madde: desen kod değil, gerçek bileşen yazılmalı · queueKey mekanizması belgesiz · hüküm-sonrası kayıt otomasyonu yok · m.6/m.40 formatı JARVIS-özel |
| ④ | Kanıt-kapılı otonomi merdiveni (A1-A4) | `kuyruk/k010-zincir-2026-08-29.md:1-56` | A1 **5/5 KESİN** · A2 kapı tamam · A3 2/3 · A4 bekliyor (tam kapanmamış) | **SİNYALLİ** (kuşatıcı eval/TRiSM pazarı ödemeli) ama **özgül mekanizmaya talep sinyali YOK** | Braintrust · LangSmith · Patronus · Galileo · ModelOp · Scrut · AllTrue; en yakın desen trafik-yüzdeli 4-aşamalı rollout gate (kanıt-sayısı değil) | **DOYGUN** | 4 madde: kapı eşikleri JARVIS'e özgü · sayaç elle güncellenen tablo, durum-makinesi değil · A4 çatal tasarımı yok · insan-onay adımı UI/API'ye modellenmeli |
| ⑤ | gnhf-izle sınıfı hafif ajan-konuşma izleyicisi | `tools/gnhf-izle.py:20-52` (92 satır, stdlib-only, LLM yok, çıkış kodu 0/2) | ①'deki koşum izleriyle dolaylı; **ayrı test/ölçüm YOK** `[?]` | **SİNYALSİZ** — bulunan 8 muadilin hiçbirinde fiyat sayfası bulgusu yok; ödeme istekliliği kanıtı **sıfır** | 8 açık-kaynak GitHub log-görüntüleyici (çoğu Claude-Code-özgü, ör. claude-code-log) + OTel GenAI tabanlı araçlar | **DOYGUN** (nicelik) | 4 madde: `.gnhf/runs/` yapısı özel · glob-polling, event-driven değil · yalnız Claude Code stream-json · test/CI yok |
| ⑥ | Repo-freni paketi (policy-as-code) | `.claude/settings.json`; `.claude/hooks/pretool-core-tel.sh` (24 satır) | Hook kendini "tökezleme-teli, sınır değil" diye tanımlıyor; PASS vakası rapor-referanslı, bu koşumda doğrulanmadı `[?]` | **SİNYALLİ** — Lakera ücretli API MEVCUT; **Invariant Labs 2025-06'da Snyk'e SATILDI** (M&A çıkış emsali) | Invariant/Snyk · Lakera Guard · NeMo Guardrails · Guardrails AI · OPA/Conftest · **Claude Code'un kendi PreToolUse hook sistemi (yerleşik alternatif, ürünün altında)** | **DOYGUN** (konsolide oluyor) | 4 madde: regex tel sertleştirilmeli · macOS/Windows taşınabilirlik · settings+hook tek pakete · ajan-fren hook'u incelenmedi |
| ⑦ | Hareket kütüğü + AXI standardı | `tools/hareket-tablo.py`; `tools/AXI-STANDARDI.md` (salt-okur açıldı, değiştirilmedi) | `veri/bronz/hareket-olay.jsonl` **5.163 satır**; AXI uyum: `tools/*.py` 43 script, `--json` 8, `--sessiz` 30 | **SİNYALLİ** — AgentOps / W&B Weave ücretli plan MEVCUT | **OpenTelemetry GenAI semantic conventions (CNCF)** — standart ekseninde doğrudan üstte · MCP · Helicone · AgentOps SDK | **DOYGUN** (ORTA-DOYGUN sınırında) | 4 madde: bronz kaynağı Claude Code transkript formatına bağlı · silver + sözleşme beraber taşınmalı · AXI 43'ün 8'inde tam · i18n |

**Dağılım: SİNYALLİ 6 · SİNYALSİZ 1 (⑤) · DOYGUN 5 · ORTA 2 (②③) · SEYREK 0.**
**Ham rapor:** `cc/rapor-2026-08-31-ib68-c-ic-envanter.md` (iç envanter) · `-b1-pazar.md` (①⑤⑦) · `-b2-pazar.md` (②③⑥) · `-b3-pazar-dagitim.md` (④ + dağıtım emsalleri).

---

## 2. Dağıtım / iş-modeli emsalleri (tek kişilik geliştirici)

Ham rapor: `cc/rapor-2026-08-31-ib68-b3-pazar-dagitim.md` (fiyat tutarları V26-ihlalli, buraya taşınmadı).

| Emsal | Dağıtım sınıfı | Ücretli plan | Gözlenen artı-eksi |
|---|---|---|---|
| Langfuse | açık-kaynak + bulut (MIT çekirdek) | **MEVCUT** | Artı: MIT çekirdek benimseme hızlandırıyor. Eksi: self-host kullanıcı ücretsiz kalıyor → gelir yüzeyi dar (SCIM/audit/RBAC'a sıkışıyor) |
| Aider | saf açık-kaynak | **YOK** (yapısal) | Artı: sıfır ticari yük. Eksi: gelir yolu yok |
| Continue.dev | açık-kaynak + bulut | **MEVCUT** | Artı: fonlama + satın alma çıkış emsali var. Eksi: token-geçişli model marj riski taşır |

**Dağıtım sınıfı artı-eksi (Salih tek-kişi lensiyle):**
- **Açık-kaynak + destek:** artı — md.14 (Jarvis zaten açık kaynak) ile çelişmez, benimseme hızlı, sıfır satış altyapısı; eksi — gelir sinyali zayıf (Aider emsali), destek yükü kişiye biner.
- **Araç (CLI, tek satış / ücretsiz):** artı — en düşük bakım, `paralel-kapi.py` zaten bu biçimde; eksi — ödeme kanıtı bu sınıfta en zayıf (⑤ SİNYALSİZ bulgusu bunun doğrudan örneği).
- **SaaS:** artı — emsallerde ücretli plan burada yoğunlaşıyor; eksi — barındırma + uptime + destek + faturalama, **tek kişilik kapasiteyle K-015/K-022 saat rekabetine doğrudan çarpar**; ayrıca m.4 gereği para/dışarı-çıkan-iş kararı.

---

## 3. V26 antitez + maskeli hakem

- **V26** (`cc/rapor-2026-08-31-v26-denetim.md`): örneklem 9 iddia, **7/9 TAM doğrulandı (%78)**, 2/9 KISMİ, 0/9 çürütüldü. **4 ihlal:** (1) B3'te açılmamış sayfadan fiyat tutarı, (2-3) B1/B2'de açılmamış kaynağa "DESTEKLİ" damgası, (4) SEO-gürültü grubu (2026 "best tools" karşılaştırma blogları — bu tür sayfalar rakip listesini yapay şişiriyor, DOYGUN hükümleri bu yüzden yukarı yanlı olabilir).
- **Hakem** (`cc/rapor-2026-08-31-hakem-dkx.md`, opus, maskeli): 67 iddia → **D 19 · K 31 · X 17**. B ailesinde (B1/B2/B3) **sıfır D** — pazar iddialarının tamamı arama-snippet düzeyinde. Fiyat/M&A/yıldız/yüzde içeren dış iddialar sertlik kuralıyla X'lendi.

**Bunun anlamı:** yukarıdaki "SİNYALLİ" damgaları **ikinci-el kaynağa dayanıyor**. Gerçek ödeme kanıtı (açılmış fiyat sayfası) yalnızca sondaj düzeyinde arandı ve Langfuse sayfasında ham rapordaki rakamlar teyit edilemedi. Ürün kararı öncesinde birincil-kaynak turu şart.

---

## 4. Ürün iskeleti (durma koşulu: ≥1)

### İSKELET — ② paralel-kapı + manifest rejimi (hakem: en güçlü ürün adayı)

Seçilme gerekçesi: tek aday ki (a) hakemden **D-etiketli çalışan kanıt** aldı, (b) rekabeti **DOYGUN değil ORTA**, (c) en yakın rakibin (Nx) mekanizması **ölçülebilir biçimde farklı** — Nx koşum-SONRASI I/O ihlal bayrağı verir, bizimki koşum-ÖNCESİ deterministik hüküm verir.

- **Hedef kullanıcı (tek cümle):** aynı repoda 3+ kodlama ajanını paralel koşturan ve merge/çakışma kaybı yaşayan tek geliştirici ya da küçük ekip.
- **MVP kapsamı — bizde VAR olan ↔ yazılması GEREKEN:**

| Bizde VAR (pointer'lı) | Yazılması GEREKEN |
|---|---|
| Bernstein çift-testi + PK-1..12 kural seti + hüküm sınıfları (PARALEL-SERBEST/SIRALI/RED/BEKLE) — `tools/paralel-kapi.py` | Manifest şemasının jenerikleştirilmesi (şu an İB-63 PROTOTİP-1'e özgü) |
| Deterministik dalga/kademe planı, LLM'siz — `tools/paralel-kapi.py` | Alt-dosya granülü (bugün grain = dosya; fonksiyon/blok düzeyi yok) |
| Manifest formatı + 17 gerçek manifest — `veri/manifest/*.json` | Genel kilit mekanizması (PK-12 "sahada-diğer-oturum" bugün repo-özel dosya kilidi) |
| `--json` / AXI arayüzü — `tools/AXI-STANDARDI.md` | Paketleme + dağıtım (pip/npm yok), kurulum yolu |
| Kanıtlanmış koşum: 8 birim/28 çift, N=1→3, çakışma 0 — `raporlar/2026-08-30-paralel-kademe-pilot.md` | Manifest'i ajanın kendisine yazdırma akışı (bugün elle beyan) — **ürünün gerçek darboğazı bu** |

- **Dağıtım sınıfı (artı-eksi):**
  - **Açık-kaynak CLI (önerilen ilk sıra):** artı — kod zaten bu biçimde, md.14 ile uyumlu, taşıma maliyeti 4 maddeyle en düşük, benimseme testi ucuz. Eksi — ⑤'te gözlenen "OSS CLI = ödeme sinyali sıfır" örüntüsü buraya da uyar; gelir beklenmemeli. **Gerekçe: ürün kararı değil, TALEP ÖLÇÜMÜ olarak koşulur.**
  - **Orkestratör ürünlerine eklenti (Conductor/Claude Squad sınıfı):** artı — kullanıcı zaten orada, kapı onların eksik parçası. Eksi — platform bağımlılığı, Crystal'ın kapanması bu katmanın kırılgan olduğunu gösteriyor.
  - **SaaS:** artı — ödeme emsalleri burada. Eksi — kapı LOKAL dosya sistemine bakar, bulut modeli zorlama olur; tek-kişi kapasitesiyle çarpışır.
- **Salih tek-kişi kapasite notu:** K-015/K-022 saat rekabeti mevcut; taşıma listesi 4 madde + paketleme + "manifest'i ajana yazdırma" akışı — bu son madde tek başına yeni bir tasarım işi, MVP'nin gerçek maliyeti orada. Karar Salih'in (m.31).

---

## 5. Masa-kalemi taslağı (Salih'e — hüküm verilmemiştir)

**MK-68/1 — Ürünleşme hattı açılsın mı?**
- (a) **Sadece ② için talep ölçümü** — ne demek: `paralel-kapi` paketlenip açık-kaynak CLI olarak bırakılır, ödeme değil KULLANIM ölçülür. Artı: en düşük maliyet, en yüksek kanıt gücü olan aday, md.14 ile çelişmez. Eksi: gelir yok; "dışarı çıkan iş" olduğu için yine de Katman-1 kararı. **Öneri: ilk sırada** — çünkü hüküm gerektirmeyen tek adım bu.
- (b) **Önce birincil-kaynak pazar turu** — ne demek: SİNYALLİ damgalarının hepsi ikinci-el; fiyat sayfaları gerçekten açılır. Artı: B ailesinde sıfır-D sorunu kapanır. Eksi: bir tur maliyet. **(a)'nın önkoşulu sayılabilir.**
- (c) **Ürün hattını kapat** — Artı: sıfır maliyet, saat rekabeti korunur, m.4 riski sıfırlanır. Eksi: ② gibi ORTA-rekabetli ve D-kanıtlı bir aday ölçülmeden gömülür.

**MK-68/2 — ⑤ (gnhf-izle) hakkında:** tek SİNYALSİZ aday; 8 ücretsiz muadil var. Öneri: ürün adayı listesinden **düşürülsün**, iç araç olarak kalsın.

**MK-68/3 — ⑦ (AXI) konumlandırması:** "standart" iddiası OpenTelemetry GenAI conventions (CNCF) karşısında savunulamaz. Öneri: AXI iç-araç sözleşmesi olarak kalsın, standart olarak sunulmasın.

**MK-68/4 — m.39 borcu:** B3 ham raporu kendi disiplin beyanını ihlal edip fiyat tutarı yazdı. Karar: ham rapor düzeltilsin mi, yoksa ihlal damgasıyla arşivde mi kalsın (m.8 silme yasağı gereği düzeltme = üstüne not).

---

## 6. Ham rapor pointer'ları

- İç envanter (C2): `cc/rapor-2026-08-31-ib68-c-ic-envanter.md`
- Pazar/rekabet: `cc/rapor-2026-08-31-ib68-b1-pazar.md` · `-b2-pazar.md` · `-b3-pazar-dagitim.md`
- Literatür ayağı (ORTAK, İB-67'de): `cc/rapor-2026-08-31-ib67-a1/a2/a3-literatur.md`
- V26 denetim: `cc/rapor-2026-08-31-v26-denetim.md` · Hakem: `cc/rapor-2026-08-31-hakem-dkx.md`
- İkiz rapor: `raporlar/2026-08-31-ib67-paper-aday-envanteri.md`
