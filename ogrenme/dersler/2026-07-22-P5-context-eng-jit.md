# Ders Kaydı — P5: Context Engineering I — JIT Yükleme & @import Tuzağı (2026-07-22, DONE)

> Beşinci paralel öğrenme oturumu (Cowork/Opus, "günaydın öğrenme — p5'ten devam"). Derinlik [T]. Teslim: tek dosya HTML ders (6 blok + Yarı-2 + 6 gerçek SVG) — Salih'e chat'te iletildi + artefakt (`p5-context-eng-jit`) + `dersler/2026-07-22-P5-context-eng-jit.html`. **Salih onayı: "p5 okudum anladım" → P5 DONE.** Canon güncellemesi (mufredat Durum + kapsül öğrenme satırı) ANA SIRAYA devredildi (öğrenme şeridi canon'a YAZMAZ — P1/P3 ile aynı kural): devir `raporlar/vardiya-teslim-2026-07-22-ogrenme-P5.md`.

## Sıra notu (çelişki kapısı, m.16)
Kapsül (07-21) kayıtlı "sıradaki" = **P4** (halüsinasyon). Salih **P5** dedi. Kontrol yapıldı:
- P5 ekseni **L1** (bağlam/token ekonomisi); ön-koşulu **P1** (DONE 07-17). P4 ekseni **L8** (inference/eğitim), ayrı dal. → **P5, P4'e bağımlı DEĞİL**; P4 atlanınca P5'in bir ön-koşulu düşmez.
- Ayrıca P3 devri (`vardiya-teslim-2026-07-19-ogrenme-P3.md`) sıradakini "P4 [S] **ya da Salih seçimi**" diye açık bırakmıştı → Salih'in P5 seçimi **plan içi**, çelişki değil.
- **Emir korundu, sıralama bozulmadı.** P4 açık borç olarak kaldı (aşağıda).

## Ne oldu (sıra)
1. **Açılış:** `core/durum-kapsulu.md` (canon kapsül, 07-21) İLK okundu — P3 açılış-hatası (bayat CHAT-KAPSULU ile açma) tekrarlanmadı. Ardından `mufredat.md`, `README.md` (protokol v2), `anlama-kapisi.md` (desen tarihçesi), P3 ders + devri okundu. Bulanık blok yok (P1 DONE'dan temiz devir).
2. **Araştırma (m.40 araştırma-önce):** İki güncel kaynak doğrulandı —
   - Claude Code resmî hafıza dokümanı (`code.claude.com/docs/en/memory`): `@import` **eager** ("imported files load at launch"), CLAUDE.md **yumuşak 200** ("loaded in full regardless of length"), MEMORY.md **sert 200∨25KB** ("content beyond that threshold is not loaded"), topic-dosyası lazy (Read-on-demand), load-order (Managed→User→Project→Local), recursion max 4-hop, code-span kaçışı, HTML-yorum çıkarma, `/compact` sonrası yalnız kök CLAUDE.md re-inject.
   - Anthropic Engineering "Effective context engineering for AI agents": JIT vs pre-load + **hibrit** (Claude Code örneği), hafif-kimlikler, progressive disclosure, metadata proxy'leri (boyut/isim/timestamp), high-signal token / dikkat bütçesi.
   - **Sonuç: müfredatın P5 düğüm-notu (#2, @path tuzağı + iki 200-satır kuralı) doğrulandı — tahmin değil, kaynaklı.**
3. **Yarı-1 (6 blok, [T], hepsi gerçek SVG):**
   - Blok 1 · İki strateji: önden-yükle vs JIT (just-in-time) + hibrit (Claude Code) + insan-analojisi (dosya sistemi/yer imi) + P1 dikkat-bütçesi bağı. SVG: iki mimari yan yana.
   - Blok 2 (çekirdek) · `@import` = **eager**, "böldüm=hafifledi" yanılsaması; disk-düzeni ≠ context-maliyeti; recursion 4-hop; backtick code-span kaçışı. Worked: `@tuzuk-v0.md` = ~12K token/açılış vs pointer ~15 token.
   - Blok 3 · İki 200-satır kuralı: CLAUDE.md yumuşak (uyum ↓, veri kaybı yok) vs MEMORY.md sert (201+ sessizce düşer + CC hata). Worked: aynı 250 satır, iki sonuç. SVG: yumuşak/sert kutu kıyası.
   - Blok 4 (çekirdek) · DOĞRU lazy = 4 mekanizma (alt-klasör CLAUDE.md · path-scoped rules · skills · MEMORY.md topic dosyaları); ortak desen index+Read = m.20'nin birebir mekaniği. Worked: Yol A (@import) vs Yol B (index+Read). SVG: m.20 pointer mimarisi (sıcak index → oklar → soğuk gövde).
   - Blok 5 · Progressive disclosure + metadata (boyut/isim/timestamp = bedava relevance) + yükleme sırası (concatenation, geniş→dar) + HTML-yorum + compaction. JARVIS: tarihli dosya adları = ücretsiz sinyal; pointer'a bir-satır metadata ekle.
   - Blok 6 (sentez) · JARVIS dosya-yerleşim tablosu (CLAUDE.md/kapsül SICAK · tüzük/defter/rapor SOĞUK); çekirdek tuzak "kanonu @import'layalım" = m.20 ihlali. Tek-cümle P5 kuralı.
4. **DONE kapısı içeriği verildi:** (a) `@import` neden context kazandırmaz (eager) (b) CLAUDE.md yumuşak vs MEMORY.md sert 200 farkı + JARVIS index'ini neden sert-kısa tasarlattığı. Salih "okudum anladım" → kapı geçti.
5. **Yarı-2 (m.37, 3 model):** JARVIS bağlam-yükleme mimarisi. A (@import merkezi, ~12-15K, kalite ~0.50, ✗) · **B (kısa index + Read-on-demand, ✅ ~2-3K, ~0.85)** · C (path-scoped rules + skills bölümlenmiş JIT, en düşük token/~0.90 ama kurulum maliyeti bugün kazancı aşar). Öneri = B; B→C geçiş kriteri **P6**'ya köprülendi. Rakamlar deneysel/proxy (m.39).

## Format v2 notu
- Pasif-okuma + derinlik etiketi [T] + 2-3 kavram/blok + self-Q&A + JARVIS senaryosu + önceki-blok köprüsü + her yapısal kavrama GERÇEK gömülü SVG + sonuna kadar işlenen worked-örnek uygulandı. Görsel-atıf/görsel-yok hatası yapılmadı (6 SVG, hepsi gömülü).
- [T] bloklar worked-örnekli ve teknik-ayrıntılı (recursion, code-span, load-order) — P3'ün [O] bloklarından daha yoğun, ama tempo/doz korundu (blok başı 2-3 kavram).

## Yarı-2 kararı → Şerit 1'e devir
Model B (kısa index + Read-on-demand). Nihai karar + uygulama ANA OTURUMDA (Katman-1/2). B→C geçiş kriteri P6'da tasarlanır. Senaryo-defteri kaydı Şerit 1'de düşülür.

## Açık borç / taşınan
- **P4 (halüsinasyon, [S])** — müfredatın kayıtlı default-next'i; Salih P5'i seçtiği için AÇIK BORÇ olarak kaldı. Bağımsız dal (L8), istenen oturumda alınır.
- **Ana-sıra ingest backlog (tespit):** on-disk `mufredat.md` bayat görünüyor — P3 DONE işaretlenmemiş (Durum = `—`) ve P0-bloğu "Sıradaki oturum" satırı hâlâ "P2" diyor. P3 devrinin (`vardiya-teslim-2026-07-19-ogrenme-P3.md`) mufredat edit'leri henüz uygulanmamış. Devir dosyasında tam düzeltme seti verildi (P3+P5 birlikte).
- Taşınan: modern-tokenizer kesin ölçümü (O13) — bu partisyonu ilgilendirmez.

## Sonraki oturum
- **P4 — Neden halüsinasyon** [S] (default-next, açık borç) **ya da P6 — Context eng. II** (compaction/not-tutma/izolasyon; P5'in doğal devamı, B→C geçiş kriterini kurar) **ya da Salih seçimi.**
- P6 açılış girdisi (hazır): bu dersin index+Read deseni + Yarı-2 Model B/C ayrımı → P6 "ne zaman C'ye geç" eşiğini tasarlar.

## DONE kapısı (Salih onayı 07-22 — geçti)
- [x] `@import`'un neden context kazandırmadığı (eager: launch'ta tam genişler) söylenebiliyor
- [x] CLAUDE.md yumuşak (hepsi yüklenir, uyum ↓) vs MEMORY.md sert (ötesi düşer) 200-satır farkı söylenebiliyor
- Ölçüm notu: pasif-okuma modeli → gerçek anlama ölçümü uygulamaya taşınır (JARVIS bağlam mimarisi kurulurken hata çıkarsa düzeltme oraya gömülür).
