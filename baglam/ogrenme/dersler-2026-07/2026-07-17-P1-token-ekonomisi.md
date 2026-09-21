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

> Yerleştirme: ana-sıra Cowork oturumu 07-17 (devir dosyasından, öğrenme oturumu canon'a yazmadı — kural gereği).
