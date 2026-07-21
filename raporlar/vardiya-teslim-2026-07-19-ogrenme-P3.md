# Vardiya Teslim — Öğrenme Şeridi P3 (2026-07-19)

> Şerit 2 (öğrenme) → Şerit 1 (ana-sıra) devir. Öğrenme oturumu canon'a YAZMAZ (P1/P2 ile aynı kural); ana-sıra bu dosyadan ingest eder. Kaynak oturum: Cowork/Opus, "günaydın, öğrenme p3".

## 1. Sonuç
**P3 (RoPE & uzun-context, lost-in-the-middle) DONE (07-19).** Salih onayı: "hepsini okudum istendiği miktarda anladım."
- Ders kaydı: `ogrenme/dersler/2026-07-19-P3-rope-context.md`
- Ders (HTML, görselli): `ogrenme/dersler/2026-07-19-P3-rope-context.html`
- Derinlik [O], pasif-okuma v2, 6 blok + 6 gerçek SVG + Yarı-2.
- DONE kapısı geçti: (a) pos-emb↔RoPE farkı (b) 200-satır tavanının mekanik nedeni (dikkat bütçesi + lost-in-the-middle + context rot birleşimi → m.20 pointer'ın mekaniği).

## 2. Canon'a uygulanacak (ana-sıra ingest)
**A) `ogrenme/mufredat.md` — Omurga tablosu, P3 satırı:**
- Durum sütunu: `—` → **`DONE (07-19)`**

**B) `ogrenme/mufredat.md` — P0 bloğu son satırı ("Sıradaki oturum"):**
- Mevcut: "Sıradaki oturum: **P2 (KV-cache, temperature) [O]**."
- Güncel gerçek: P1 DONE (07-17) · **P3 DONE (07-19)** · P2 07-19 paralel oturumda koşuldu, **P2 devir dosyası hâlâ ingest bekliyor** (bkz. durum-kapsulu 07-19 satır 12). Önerilen yeni satır:
  > "P3 DONE (07-19, ders: `dersler/2026-07-19-P3-rope-context.md`). P2 (KV-cache) 07-19 paralel koşuldu — devir ingest bekliyor. Sıradaki [O] oturum: **P4 (halüsinasyon) [S]** ya da Salih seçimi."

**C) `core/durum-kapsulu.md` — YALNIZ Şerit 2 satırı (satır 12):**
- Mevcut: "**Şerit 2 (öğrenme):** P2 (KV-cache, temperature) paralel oturumda koşuldu (07-19) — devir dosyası bekleniyor; gelince ingest."
- Öneri: "**Şerit 2 (öğrenme):** P3 DONE (07-19, ders: `dersler/2026-07-19-P3-rope-context.md`; Yarı-2 Model B → Şerit 1 aday). P2 (KV-cache) 07-19 paralel koşuldu — devir ingest bekliyor. Sıradaki: P4 [S] ya da Salih seçimi."

## 3. Yarı-2 kararı → Şerit 1 aday (senaryo-defteri)
**Soru:** JARVIS bağlam/hafıza yerleşimi mimarisi. **3 model, 4-tuple (token, zaman, beklenen-kalite); rakamlar deneysel/proxy (m.39).**
- A — düz/hepsini-yükle: token yüksek+büyüyen · yavaş · kalite ~0.55↓ (context rot + lost-in-the-middle).
- **B — kısa çekirdek + pointer ✅ ÖNERİ:** token düşük-sabit (~2-3K) · hızlı (kararlı-prefix cache) · kalite ~0.85. Mevcut m.20/m.34'ün mekanik karşılığı.
- C — katmanlı + compaction + not-tutma: token orta · orta · kalite ~0.90 ama kazanç ancak uzun ajan-oturumlarında.

**Öneri = B** (prototip fazına uygun, mevcut kanonla hizalı, en iyi token/kalite dengesi). **Köprü:** C'nin compaction + not-tutma parçaları **P6 (Context eng. II)**'ye — orada B→C geçiş kriteri (oturum-uzunluğu eşiği) tasarlanır. Nihai karar + uygulama ana-sırada (Katman-1/2). Senaryo-defteri kaydı ana-sırada düşülür.

## 4. Protokol düzeltmesi (açılış-hatası — kendi kaydım)
Bu oturum **bayat kapsülle açıldı**: `CHAT-KAPSULU-2026-07-13.md` okundu, canon `core/durum-kapsulu.md` (07-19) yerine. Sonuç: Salih'e verilen çelişki-kapısı notu ("sıra P2 idi") eksik zemindeydi — canon kapsül P2'nin zaten koşulduğunu söylüyordu. Sonuç değişmedi (P3 doğru adımdı) ama gerekçe yanlıştı.
**Öneri (README güncellemesi adayı, Salih/ana-sıra kararı):** öğrenme protokolü step-1'e açık kural — "açılışta İLK okunan dosya `core/durum-kapsulu.md`; CHAT-KAPSULU yalnız chat/mobil yüzey içindir, Cowork öğrenme oturumu canon kapsülü okur."

## 5. Açık / taşınan
- P2 devir ingesti hâlâ ana-sırada bekliyor (bu devirle karışmasın — ayrı iş).
- Modern-tokenizer kesin ölçümü (O13 / P1'den banda inmiş) — bu partisyonu ilgilendirmez.
