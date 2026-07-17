# DEVİR — Öğrenme Oturumu P1 → Ana Sıra

> **DAMGA: ANA OTURUMDA İŞLENECEK (ham/aday).** Bu dosya öğrenme (Şerit 2) oturumunun ana sıraya (Şerit 1) devridir. Bu oturum canon'a YAZMADI: push yok, `core/` ve `CLAUDE.md` değişmedi (Salih talimatı 07-17: "bu oturumdan çıkarılan dersler ve alınan kararlar ana oturumda işlenir"). Ana oturum: (a) ders kaydını `ogrenme/dersler/`e yerleştirir, (b) kapsül öğrenme-satırını + müfredat P1 durumunu günceller, (c) 2 maddeyi panoya/senaryo-defterine işler, (d) klon-push atar.

**Tarih:** 2026-07-17 · **Oturum:** P1 (Token Ekonomisi & Bağlam = Maliyet) · **Sonuç:** P1 DONE (Salih onayı: "tamam anladım")

---

## 1) Ana oturumun işleyeceği KARAR ve MADDELER

### KARAR (Katman-1 — NİHAİ KARAR ANA OTURUMDA, Salih önünde)
**Model B — Kararlı-prefix / değişken-suffix okuma düzeni.** Salih 07-17: "uygulama, ana oturumda nihai karar verilir."
- **Öneri (P1 Yarı-2, m.37):** oturum-açılış okuma sırasını, en durağan içerik önce (önbellek), en oynak içerik sonra olacak şekilde düzenle. Somut: durağan çekirdek (CLAUDE.md sabit blok) → sonra `durum-kapsulu` + `pano` okuma sırasında SONA. Gerekçe: prefix-invalidation — oynak dosya önde ise arkasındaki her şeyin prompt-cache'i her oturum çürür (örnek modelde ~8× açılış maliyeti farkı, deneysel m.39).
- **Uygulama dokunacağı yer:** `CLAUDE.md` "oturum açılış okuma sırası" talimatı (Katman-1). Bu oturum DOKUNMADI.
- **Not (Salih'in keskinleştirmesiyle):** "durağan çekirdek"e büyük dosya (tüzük tam metni, wiki) KONMAZ — onlar boyutları yüzünden zaten soğuk/pointer kalır (bkz. madde 2). Sıcak-kararlı önek yalnızca küçük çekirdektir.

### ARAŞTIRMA MADDESİ (Salih 07-17: "prefix ölçeklenme sigortası araştırılacak")
**Prefix-ölçeklenme sigortası — "wiki/kanon şişerse ne yaparız?"**
- **Problem (Salih'in tespiti):** kararlı-prefix stratejisi öneğin (1) küçük ve (2) değişmez olmasına bel bağlar. Wiki aktif büyürse ikisi de bozulur: büyüme=değişim (her yeni/düzenlenen sayfa öneği oynatır → cache düşer); büyüklük tek başına maliyet (cache-read ~0.1× ama ≠0; O(n²) yine işler; TTL dolunca tam write). "Sonsuz büyüyen önek" yoktur, tavanı var.
- **İlke (bu oturumun cevabı):** önek büyüyen bir depo değil, **sabit-boyutlu bütçe**. Büyüme SOĞUK katmana (pointer/retrieval) gider; sıcak çekirdek damıtmayla ~sabit küçük tutulur. Büyük bilgi, kararlı olsa BİLE, boyutu yüzünden soğuk kalır.
- **Bağlı olduğu planlı iş (yeni yetim iş DEĞİL):** P6 (compaction) · P11 (m.34 damıtma promote/merge/delete) · P12 (RAG sınırları + geri-çağırma ölçümü) · **K-019** (kutu-damıtma + boyut-izleme borcu). Bu araştırma bunları tetikleyen somut soru.
- **Aday sahiplik:** araştırma → CC köprüsü (Atlas) ya da ilgili partisyon oturumu. Ana oturum: senaryo-defterine + K-019 notuna işle.

### AÇIK BORÇ GÜNCELLEME
- **TR/EN token oranı — GERÇEK ÖLÇÜLDÜ (P0 borcu kısmen kapandı).** Claude'un eski açık BPE'siyle (pakete gömülü, indirim gerektirmedi) 6 kanon-tarzı çift: **TR/EN = 1.89×** (aralık 1.64–2.11×), tok/kelime TR 3.25 / EN 1.17, `durum-kapsulu.md` = 3.209 token. Bu eski/İngilizce-ağırlıklı tokenizer = kötümser üst-bant; modern çok-dilli (Claude 3+, GPT-4o) daha iyi sıkıştırır → literatür ~1.5×. **Gerçek band: ~1.5–1.9×.** Kalan açık: modern tokenizer kesin sayısı (o vocab'lar sandbox'ta 403). Borç durumu: **OPEN → PARTIALLY-CLOSED.**
- Karar teyidi (Salih Katman-1, P0'da): kanon Türkçe kalır (okunabilirlik > ~1.5×; prototipte bağlayıcı değil), yük damıtma+pointer'la yönetilir. Ölçüm bunu çürütmedi, sınırladı.

---

## 2) Ders kaydı taslağı (ana oturum → `ogrenme/dersler/2026-07-17-P1-token-ekonomisi.md`)

# Ders Kaydı — P1: Token Ekonomisi & Bağlam = Maliyet (2026-07-17, DONE)

> İkinci paralel öğrenme oturumu (Cowork/Opus, "günaydın, öğrenme"). P0 (a+b) DONE'dan devraldı. Derinlik [T]. Teslim: tek dosya HTML ders (6 blok + görseller + Yarı-2) — Salih'e chat'te iletildi. Salih: "tamam anladım" → P1 DONE.

## Ne oldu (sıra)
1. **Açılış:** kapsül + öğrenme protokolü okundu; P0 DONE olduğu için bulanık-blok telafisi yok, doğrudan P1.
2. **Açık borç kapatma denemesi (başta):** tiktoken/HF vocab indirimi yine 403 (P0'daki blok) → Claude'un eski açık tokenizer'ı (anthropic paketine gömülü) ile GERÇEK ölçüm yapıldı: TR/EN 1.89×.
3. **Yarı-1 (6 blok, [T], görselli):** Blok 1 bağlam=O(n²) maliyet · Blok 2 input≠output fiyat · Blok 3 prompt-cache (prefix, write~1.25× / read~0.1×) · Blok 4 (çekirdek) prefix-invalidation + kararlı-prefix kuralı · Blok 5 m.20 pointer + V37 = maliyet-mühendisliği · Blok 6 Türkçe kanon maliyeti (gerçek ölçüm).
4. **DONE kapısı geçti:** prefix-invalidation kuralı + m.20/V37 = maliyet-mühendisliği açıklandı; Salih sezgisel onayladı.
5. **Yarı-2 (m.37 3-model):** okuma-sırası yeniden tasarımı; Model B ✅ önerildi.
6. **Salih katkısı (kuralı keskinleştirdi):** kararlı-prefix + büyüyen wiki gerilimi → "prefix-ölçeklenme sigortası" araştırma maddesi doğdu; büyük bilgi kararlı olsa bile boyutu yüzünden soğuk kalmalı ilkesi eklendi.

## Format v2 notu
- Pasif-okuma + derinlik etiketi + 2-3 kavram/blok + self-Q&A + JARVIS senaryo + her yapısal kavrama gerçek görsel + sonuna kadar işlenen sayısal örnek uygulandı. Görsel-atıf/görsel-yok hatası bu sefer yapılmadı (hepsi SVG olarak üretildi).
- İyileştirme adayı: [T] bloklar uzun; Salih tek teslimde tamamını okudu — gelecek [T] oturumlarında blok-blok teyit istenebilir (Salih tercihi bekler).

## Yarı-2 kararı → Şerit 1'e devir
Model B (kararlı-prefix okuma-sırası). Nihai karar + uygulama ANA OTURUMDA (Katman-1). Detay: bu devir dosyası §1.

## Sonraki oturum
- **P2 — Inference & sampling: KV-cache, temperature** [O]. Açılış girdisi: Blok 1'in O(n²)'si (KV-cache bunun bir kısmını nasıl geri kazanır) + ajanlarda düşük-temperature gerekçesi.
- Taşınan açık borç: modern-tokenizer kesin ölçümü (P1'de band'a indirildi).

---

## 3) Kapsül öğrenme-satırı — önerilen metin (ana oturum `core/durum-kapsulu.md` günceller)
`**Öğrenme (Şerit 2):** P1 (Token ekonomisi) DONE 07-17 — DONE kapısı: prefix-invalidation + m.20/V37=maliyet-müh. Ders HTML teslim. Açık borç TR/EN ölçüldü (1.89× eski BPE; band ~1.5–1.9×; modern kesin sayı hâlâ açık). Devir: Model B okuma-sırası (ana oturumda nihai karar) + prefix-ölçeklenme sigortası (araştırılacak; P6/P11/P12/K-019). Sıradaki oturum: P2 (KV-cache, temperature) [O]. Devir dosyası: raporlar/vardiya-teslim-2026-07-17-ogrenme-P1.md`

## 4) Müfredat (ana oturum `ogrenme/mufredat.md` günceller)
P1 Durum sütunu `—` → **DONE (07-17)**. Sıradaki: P2.
