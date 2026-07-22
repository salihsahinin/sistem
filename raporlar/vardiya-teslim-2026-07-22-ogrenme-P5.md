# Vardiya Teslim — Öğrenme Şeridi P5 (2026-07-22)

> Şerit 2 (öğrenme) → Şerit 1 (ana-sıra) devir. Öğrenme oturumu canon'a YAZMAZ (P1/P3 ile aynı kural); ana-sıra bu dosyadan ingest eder. Kaynak oturum: Cowork/Opus, "günaydın öğrenme — p5'ten devam". Açılış canon kapsülden yapıldı (`core/durum-kapsulu.md`, 07-21) — P3 açılış-hatası tekrarlanmadı.

## 1. Sonuç
**P5 (Context eng. I: JIT yükleme, @path tuzağı) DONE (07-22).** Salih onayı: "p5 okudum anladım."
- Ders kaydı: `ogrenme/dersler/2026-07-22-P5-context-eng-jit.md`
- Ders (HTML, görselli): `ogrenme/dersler/2026-07-22-P5-context-eng-jit.html` + artefakt `p5-context-eng-jit`
- Derinlik [T], pasif-okuma v2, 6 blok + 6 gerçek SVG + Yarı-2.
- DONE kapısı geçti: (a) `@import` = eager (launch'ta tam genişler → context kazandırmaz) (b) CLAUDE.md yumuşak-200 (hepsi yüklenir, uyum ↓) vs MEMORY.md sert-200∨25KB (ötesi düşer) farkı.

## 2. Canon'a uygulanacak (ana-sıra ingest)
> UYARI: on-disk `mufredat.md` bayat — P3 DONE işaretlenmemiş + "Sıradaki oturum" satırı hâlâ "P2" diyor (P3 devrinin edit'leri uygulanmamış). Aşağıdaki set **P3 + P5'i birlikte** düzeltir; ana-sıra ingest'te ikisi de uygulanmalı.

**A) `ogrenme/mufredat.md` — Omurga tablosu:**
- P3 satırı, Durum: `—` → **`DONE (07-19)`** (birikmiş)
- P5 satırı, Durum: `—` → **`DONE (07-22)`**

**B) `ogrenme/mufredat.md` — P0 bloğu son satırı ("Sıradaki oturum"):**
- Mevcut (bayat): "Sıradaki oturum: **P2 (KV-cache, temperature) [O]**."
- Önerilen yeni satır:
  > "P1 DONE (07-17) · P2 (KV-cache) 07-19 paralel koşuldu — **devir ingest hâlâ bekliyor** · P3 DONE (07-19, `dersler/2026-07-19-P3-rope-context.md`) · P5 DONE (07-22, `dersler/2026-07-22-P5-context-eng-jit.md`). **Açık borç: P4 (halüsinasyon) [S]** — default-next, atlanmadı, seçilmedi. Sıradaki: **P4** ya da **P6 (Context eng. II)** ya da Salih seçimi."

**C) `core/durum-kapsulu.md` — YALNIZ Şerit 2 satırı (satır 11):**
- Mevcut: "**Şerit 2 (öğrenme):** P3 KOŞULDU 07-19 — ama kayıtları UNTRACKED ... Sıradaki oturum **P4** (müfredat) — P3'ü tekrar KOŞMA ..."
- Öneri: "**Şerit 2 (öğrenme):** **P5 DONE (07-22)** (ders `.md/.html` + artefakt; Yarı-2 Model B → Şerit 1 aday). P3 DONE (07-19) · P2 devir ingest hâlâ bekliyor · **P4 açık borç** (atlanmadı). Kayıt commit borcu Salih'in makinesinde (mount'tan git YAZMA yok). Sıradaki: P4 ∨ P6 ∨ Salih seçimi — P3/P5'i tekrar KOŞMA (K-019 çift-koşum önlemi)."

## 3. Yarı-2 kararı → Şerit 1 aday (senaryo-defteri)
**Soru:** JARVIS bağlam/kanon yükleme mimarisi mekanik olarak nasıl kurulmalı? **3 model, 4-tuple (token, zaman, beklenen-kalite); rakamlar deneysel/proxy (m.39).**
- A — @import merkezi (CLAUDE.md'ye kapsül+tüzük+pano @import): token ~12-15K/açılış sabit · yavaş, prefix şişer · kalite ~0.50 (bağlam şişkinliği + context rot + uyum ↓). **✗ elenir.**
- **B — kısa index + Read-on-demand ✅ ÖNERİ:** token ~2-3K sıcak, sabit · hızlı, kararlı-prefix cache dostu · kalite ~0.85. m.20/m.34'ün birebir mekaniği; `@import` tuzağından kaçar. P3 Yarı-2 Model B'nin CC-mekanik karşılığı.
- C — bölümlenmiş JIT (path-scoped rules + skills + topic dosyaları): token en düşük · orta (kurulum maliyeti) · kalite ~0.90 ama kazanç ancak çok-alan/çok-projeli olgunlukta.

**Öneri = B** (prototip fazına uygun, mevcut kanonla hizalı, en iyi token/kalite dengesi). **Köprü:** C'nin path-scoped-rules + skills parçası + B→C geçiş kriteri (çok-alan/çok-proje eşiği; oturum-uzunluğu) **P6 (Context eng. II)**'ye. Nihai karar + uygulama ana-sırada (Katman-1/2). Senaryo-defteri kaydı ana-sırada düşülür.

**Somut JARVIS aksiyonu (ana-sıra değerlendirmesi için):** mevcut yapı zaten B'ye yakın (CLAUDE.md 5.8KB pointer/kimlik; durum-kapsulu 3.4KB index; tüzük 40KB Read'le açılıyor). P5'in netleştirdiği kural: **tüzük/senaryo-defteri/rapor gövdesi ASLA CLAUDE.md'ye @import edilmemeli** — pointer + Read-on-demand kalmalı. Kapsül, MEMORY.md sert-kısa disiplininde tutulmalı (şişerse token değil, sessiz-kesilme riski). Denetlenecek: CLAUDE.md içinde backtick'siz `@...` satırı var mı (istemsiz eager yükleme).

## 4. Açık / taşınan
- **P4 (halüsinasyon) açık borç** — atlanmadı, seçilmedi; istenen oturumda alınır.
- **P2 devir ingesti** hâlâ ana-sırada bekliyor (bu devirle karışmasın — ayrı iş; P3 devrinden taşındı).
- **mufredat.md ingest backlog** — P3 edit'leri + P5 edit'leri birlikte uygulanmalı (madde 2).
- Modern-tokenizer kesin ölçümü (O13) — bu partisyonu ilgilendirmez.

## 5. Not
- Kayıtların git commit'i Salih'in makinesinde (proof-of-work m.9; mount'tan git YAZMA yok). Bu oturum dosyaları diske yazdı: ders `.md` + `.html` + bu devir. Commit + push Salih'te.
