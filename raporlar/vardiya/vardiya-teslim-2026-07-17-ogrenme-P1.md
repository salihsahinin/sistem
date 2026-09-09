# DEVİR — Öğrenme Oturumu (P1 + P2) → Ana Sıra

> **DAMGA: ANA OTURUMDA İŞLENECEK (ham/aday).** Öğrenme (Şerit 2) oturumunun ana sıraya (Şerit 1) devri. Bu oturum canon'a YAZMADI: push yok, `core/`/`CLAUDE.md` değişmedi (Salih talimatı 07-17: "bu oturumdan çıkarılan dersler ve alınan kararlar ana oturumda işlenir"). Ana oturum: (a) ders kayıtlarını `ogrenme/dersler/`e yerleştirir, (b) kapsül öğrenme-satırını + müfredat P1/P2 durumunu günceller, (c) maddeleri panoya/senaryo-defterine işler, (d) klon-push atar.

**Tarih:** 2026-07-17 · **Oturumlar:** P1 (Token Ekonomisi) DONE + P2 (KV-cache & Temperature) DONE · **Sonraki:** P3

---

## 1) Ana oturumun işleyeceği KARAR ve MADDELER

### KARAR-1 (P1 · Katman-1 — NİHAİ KARAR ANA OTURUMDA, Salih önünde)
**Model B — Kararlı-prefix / değişken-suffix okuma düzeni.** Salih 07-17: "uygulama, ana oturumda nihai karar verilir."
- **Öneri:** oturum-açılış okuma sırasını en durağan içerik önce (önbellek), en oynak sonra olacak şekilde düzenle. Somut: CLAUDE.md sabit blok → `durum-kapsulu` + `pano` okuma sırasında SONA. Gerekçe: prefix-invalidation — oynak dosya önde → arkasındaki her şeyin prompt-cache'i her oturum çürür (örnek modelde ~8× açılış farkı, deneysel m.39).
- **Dokunacağı yer:** `CLAUDE.md` "oturum açılış okuma sırası" (Katman-1). Bu oturum DOKUNMADI.
- **Şart (Salih keskinleştirmesi):** "durağan çekirdek"e büyük dosya (tüzük tam metni, wiki) KONMAZ — boyutları yüzünden soğuk/pointer kalır. Sıcak-kararlı önek yalnızca küçük çekirdek.

### KARAR-2 (P2 · ilke — K-010'da devreye girer)
**Rol-bazlı determinizm/temperature politikası (Model B).** İcra ajanları (Atlas, subagent) düşük-temp/deterministik; üretim/keşif işleri yüksek-temp. Ajan-defter şemasına (K-010) "temp/determinizm" alanı olarak yazılır.
- **Dürüst kayıt:** temperature ŞU AN harness-sabit (Cowork/CC), kontrol bizde değil. Bu, K-010'da kendi ajanlarımızı API/SDK ile kurunca devreye girecek İLKE — hemen uygulanacak ayar değil.
- **Gerekçe:** icra tekrarlanabilir+denetlenebilir (V8/V26 uyumlu); keşif çeşitliliği (m.35) korunur. Devir: senaryo-defteri + K-010 ajan-defter notu.

### ARAŞTIRMA MADDESİ (P1 · Salih 07-17: "prefix ölçeklenme sigortası araştırılacak")
**Prefix-ölçeklenme sigortası — "wiki/kanon şişerse ne yaparız?"**
- **Problem (Salih tespiti):** kararlı-prefix, öneğin küçük+değişmez olmasına bel bağlar. Wiki büyürse ikisi de bozulur: büyüme=değişim (yeni/düzenlenen sayfa öneği oynatır → cache düşer); büyüklük tek başına maliyet (cache-read ~0.1× ama ≠0; O(n²) yine işler; TTL dolunca tam write; KV-cache belleği lineer büyür — P2). "Sonsuz büyüyen önek" yok, tavanı var.
- **İlke (bu oturumun cevabı):** önek büyüyen depo değil, sabit-boyutlu bütçe. Büyüme SOĞUK katmana (pointer/retrieval) gider; sıcak çekirdek damıtmayla ~sabit küçük tutulur. Büyük bilgi, kararlı olsa BİLE, boyutu yüzünden soğuk kalır.
- **Bağlı planlı iş (yeni yetim iş DEĞİL):** P6 (compaction) · P11 (m.34 damıtma) · P12 (RAG sınırları + geri-çağırma) · **K-019** (kutu-damıtma + boyut-izleme borcu).
- **Aday sahiplik:** araştırma → CC köprüsü (Atlas) ya da ilgili partisyon. Ana oturum: senaryo-defterine + K-019 notuna işle.

### AÇIK BORÇ GÜNCELLEME (P1)
- **TR/EN token oranı GERÇEK ÖLÇÜLDÜ (P0 borcu kısmen kapandı).** Claude eski açık BPE'si (pakete gömülü) · 6 kanon-tarzı çift: **TR/EN = 1.89×** (aralık 1.64–2.11×), tok/kelime TR 3.25 / EN 1.17, `durum-kapsulu.md` = 3.209 token. Bu eski/İngilizce-ağırlıklı tokenizer = kötümser üst-bant; modern çok-dilli ~1.5×. **Gerçek band ~1.5–1.9×.** Kalan açık: modern tokenizer kesin sayısı (vocab 403). Durum: **OPEN → PARTIALLY-CLOSED.**
- Teyit: kanon Türkçe kalır (Salih Katman-1), yük damıtma+pointer'la yönetilir. Ölçüm çürütmedi, sınırladı.

---

## 2) Ders kayıtları taslağı (ana oturum → `ogrenme/dersler/`)

### 2A → `2026-07-17-P1-token-ekonomisi.md`
# Ders Kaydı — P1: Token Ekonomisi & Bağlam = Maliyet (2026-07-17, DONE)
> İkinci paralel öğrenme oturumu (Cowork/Opus). P0 DONE'dan devraldı. [T]. Teslim: tek dosya HTML (6 blok + görseller + Yarı-2). Salih "tamam anladım" → DONE.
- **Sıra:** açılış → açık borç (tiktoken/HF 403 → gömülü BPE ile gerçek ölçüm 1.89×) → Yarı-1 6 blok [T] görselli (bağlam=O(n²) · input≠output · prompt-cache · prefix-invalidation · m.20/V37=maliyet-müh · Türkçe maliyet) → DONE kapısı geçti → Yarı-2 m.37 (Model B okuma-sırası) → Salih katkısı: prefix-ölçeklenme sigortası + "büyük bilgi kararlı olsa bile boyutu yüzünden soğuk kalır" ilkesi.
- **Yarı-2 kararı:** Model B (§1 KARAR-1). Nihai + uygulama ana oturumda (Katman-1).
- **Sonraki:** P2.

### 2B → `2026-07-17-P2-kv-cache-temperature.md`
# Ders Kaydı — P2: Inference & Sampling — KV-cache & Temperature (2026-07-17, DONE)
> [O]. Teslim: tek dosya HTML (4 blok + görseller + Yarı-2). P1'den devraldı.
- **Sıra:** Blok 1 KV-cache (naif üretimin israfı → bir kez hesapla-sakla; O(n²)→O(n)) · Blok 2 KV-cache neden pahalı (cache bağlamla lineer büyür → bellek tavanı; her yeni token tüm cache'i okur → gecikme) + **AHA köprü: prompt-cache = KV-cache'in çağrılar-arası saklanması, P1↔P2 birleşti** · Blok 3 temperature (logits→softmax→sampling; düşük=keskin/deterministik, yüksek=düz/çeşitli) · Blok 4 ajanlarda düşük temp (güvenilirlik/tekrarlanabilirlik/geçerli tool-call/denetlenebilirlik; V8/V26 uyumlu).
- **DONE kapısı geçti:** KV-cache neden pahalılaştırır + ajanlarda neden düşük temp — sebebiyle söylenebiliyor.
- **Yarı-2 kararı:** Model B rol-bazlı determinizm (§1 KARAR-2), K-010 ajan-defter ilkesi.
- **Sonraki:** P3.

---

## 3) Kapsül öğrenme-satırı — önerilen metin (ana oturum `core/durum-kapsulu.md`)
`**Öğrenme (Şerit 2):** P1 (Token ekonomisi) + P2 (KV-cache/temperature) DONE 07-17. P1 DONE-kapısı: prefix-invalidation + m.20/V37=maliyet-müh; P2: KV-cache neden pahalı (bellek+gecikme) + ajanda düşük-temp. AHA: prompt-cache = KV-cache'in çağrılar-arası hali. Açık borç: TR/EN ölçüldü (1.89× eski BPE; band ~1.5–1.9×; modern kesin sayı açık). Devir kararları: (1) Model B okuma-sırası — ana oturumda nihai karar; (2) prefix-ölçeklenme sigortası — araştırılacak (P6/P11/P12/K-019); (3) rol-bazlı determinizm ilkesi — K-010 ajan-defter. Sıradaki: P3 (RoPE & lost-in-the-middle) [O]. Devir dosyası: raporlar/vardiya-teslim-2026-07-17-ogrenme-P1.md`

## 4) Müfredat (ana oturum `ogrenme/mufredat.md`)
P1 Durum `—` → **DONE (07-17)** · P2 Durum `—` → **DONE (07-17)** · Sıradaki: P3.
