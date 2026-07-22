# Öğrenme Müfredatı v1 — 2026-07-15 (Atlas ilk koşumundan damıtıldı; K-021 adım 4)

> **Açıklama notu:** Kaynak: `cc/rapor-2026-07-15-1.md` (8 eksen, 41 iddia denetimli: 32 D / 9 K / 0 X). Bu dosya OMURGA + durum takibi; eksen detayı, kaynaklar ve bulgular raporda (pointer m.20 — buraya kopyalanmaz). Oturum protokolü: `ogrenme/README.md` (Yarı-1 0'dan anlatım pasif-okuma modeliyle + Yarı-2 m.37 3-model JARVIS uygulaması). Partisyon ≈ 1 oturum (1,5–3h). Her oturum kapanışında bu tablonun Durum sütunu güncellenir.

## Ön-koşul kapısı — P0 (REVİZE 07-15: pasif-okuma oturumlarıyla işlenir; Karpathy videoları Salih'in kendi hattı, Gemini transkriptle — P0 DONE'una bağlı değil)
Kapsam: ZtH Ders 7 + Ders 8 + "Deep Dive into LLMs" içeriğinin kavramsal karşılığı. DONE: Salih öğrenilmiş-pos-embedding ≠ RoPE farkını ve tokenizer tuzaklarını söyleyebiliyor.
**P0 (a+b) DONE — 07-15 Opus öğrenme oturumu; Salih "sezgisel olarak tamam" beyanı.** Ders kaydı: `dersler/2026-07-15-P0-opus-oturumu.md`. P1 DONE (07-17, ders: `dersler/2026-07-17-P1-token-ekonomisi.md`; devir: `raporlar/vardiya-teslim-2026-07-17-ogrenme-P1.md`). P1 DONE (07-17) · P2 (KV-cache) 07-19 paralel koşuldu — **devir ingest hâlâ bekliyor** · P3 DONE (07-19, `dersler/2026-07-19-P3-rope-context.md`) · P5 DONE (07-22, `dersler/2026-07-22-P5-context-eng-jit.md`). P4 OKUNDU (07-22, Salih beyanı — 07-22 çelişki-sorusuyla netleşti; ayrı ders-kaydı yok). Sıradaki: **P6 (Context eng. II — B→C geçiş kriterini kurar)** ya da Salih seçimi.
**Mini-teşhis SONUÇLANDI (07-15, ana-sıra oturumunda):** 12/12 kontrol noktası bulanık → P0 sıfırdan. Katman-2 kararı: P0 ikiye bölündü (m.21):
- **P0-a — Transformer'ın içi** [O; RoPE alt-başlığı S]: tahmin döngüsü · embedding · self-attention Q/K/V · causal mask · multi-head · FFN/residual/layernorm · pos-emb↔RoPE. Durum: **DONE** (Opus oturumu 07-15) — bulanık bloklar (3 Q/K/V, 4-5 mask/multi-head, 6-7 FFN/pos-emb) v2 görselli telafi edildi + RoPE [S] ilk geçiş yapıldı; DONE kapısı geçti. Ders kayıtları: `dersler/2026-07-15-P0a-transformer-ici.md` (v1) + `dersler/2026-07-15-P0-opus-oturumu.md` (telafi).
- **P0-b — Tokenizer + eğitim hattı** [O; eğitim hattı S]: BPE · tokenizer≠model · tuzaklar · special token'lar · pretraining/SFT/RLHF + halüsinasyon kökü. Durum: **DONE** (Opus oturumu 07-15) — 2 blok v2 görselli işlendi; BPE the-örneği tam açıldı. Ders kaydı: `dersler/2026-07-15-P0-opus-oturumu.md`.

## Omurga (P1–P19 ≈ ~49h; bağımlılık-sıralı)
| P | Oturum | Tek-satır DONE | Eksen | ~Süre | Derinlik | Durum |
|---|---|---|---|---|---|---|
| P1 | Token ekonomisi & bağlam=maliyet | prompt-cache prefix-invalidation kuralı + m.20/V37 = maliyet-mühendisliği açıklanır | L7+L1 | 2.5h | [T] | **DONE (07-17)** |
| P2 | Inference & sampling: KV-cache, temperature | KV-cache bağlamı neden pahalılaştırır + ajanlarda düşük-temperature gerekçesi | L8 | 2.5h | [O] | — |
| P3 | RoPE & uzun-context, lost-in-the-middle | ZtH pos-emb ↔ RoPE farkı + 200-satır eşiğinin mekanik nedeni | L8+L1/L2 | 2.5h | [O] | **DONE (07-19)** |
| P4 | Neden halüsinasyon | eğitim-kaynaklı neden → V8/V26'nın varoluş gerekçesi | L8 | 2h | [S] | **OKUNDU (07-22, Salih beyanı; ayrı ders-kaydı dosyası yok — gece oturumu)** |
| P5 | Context eng. I: JIT yükleme, `@path` tuzağı | V37 seçici-yükleme + m.20'nin DOĞRU lazy implementasyonu (@import ≠ lazy!) | L1 | 2.5h | [T] | **DONE (07-22)** |
| P6 | Context eng. II: compaction, not-tutma, izolasyon | K-015 şemasının cacheable-prefix + compaction stratejisi taslağı | L1 | 3h | [T] | — |
| P7 | Tool-use temelleri: function-calling döngüsü | bir JARVIS aracının şema + is_error tasarımı yazılır | L5 | 2.5h | [O] | — |
| P8 | MCP mimarisi + ne zaman sunucu (V25 testi) | MCP-ekle/ekleme kararı V25 + güven-sınırıyla gerekçelenir | L5 | 2.5h | [O] | — |
| P9 | Skills/Tools/Subagents/MCP karar çerçevesi | K-009 nightly-sync mekanizma seçimi gerekçelenir | L5 | 2.5h | [T] | — |
| P10 | Hafıza I: CoALA + dosya-primitifleri | K3→K0 ↔ CoALA (working/episodic/semantic/procedural) eşlemesi | L3 | 2.5h | [O] | — |
| P11 | Hafıza II: katmanlı mimari + m.34 damıtma | m.34 promote/merge/delete karar-ağacı taslağı (Mem0 esinli) | L3 | 2.5h | [T] | — |
| P12 | Hafıza III: RAG sınırları + geri-çağırma ölçümü | m.20 pointer-over-embedding gerekçesi + geri-çağırma ölçüm fikri | L3 | 2.5h | [O] | — |
| P13 | Orkestrasyon I: agentic döngü + taksonomi | V13/V17 topolojisi Anthropic taksonomisine yerleştirilir | L2 | 2.5h | [O] | — |
| P14 | Orkestrasyon II: fan-out, peer, m.30 kalıcılık | sonraki-topoloji adımı + kalıcılık modeli (uyku≠restart) taslağı | L2 | 2.5h | [O] | — |
| P15 | **Orkestrasyon III: "ne zaman ÇOKLU-ajan DEĞİL"** | ajan-say ölçekleme hedefine KAPI-kuralı yazılır + V8/V26 spec taslağı | L2 | 3h | [T] | — |
| P16 | Güvenlik I: injection, lethal trifecta | mimari>talimat yetki-ayrımı: hangi subagent neyi ALMAZ | L6 | 2.5h | [O] | — |
| P17 | Güvenlik II: memory poisoning, otonomi merdiveni | K-009 "canlı ajan nerede başlar" merdiven taslağı + nightly-sync provenance sigortası | L6 | 3h | [T] | — |
| P18 | Eval I: eval-seti, LLM-as-judge + bias | 20-50 görevlik eval-set iskeleti + judge'ı Salih-yargısına doğrulama planı | L4 | 3h | [T] | — |
| P19 | Eval II: kalibrasyon/Brier + küçük-N/V39 | m.37 kalibrasyon döngüsü + V39 durdurma-kuralı + "kararlı çalışma" ölçüsü | L4 | 2.5h | [T] | — |

*Derinlik sütunu (format v2, 07-15): [S] sezgisel · [O] orta · [T] tam — tanımlar `README.md` protokolünde. Atama Carvis Katman-2 (ölçüt: JARVIS kararlarına uzaklık); Salih istediğinde değiştirir. [S]/[O] partisyonlarda süre tahmini pratikte kısalır — tablo süreleri üst sınır sayılır.*

## Düğüm notları (raporun öncelik-şekillendiren bulguları)
1. **P15 = müfredatın kilit düğümü:** çoklu-ajan çoğu görevde tek-ajanı %6-41 GEÇEMİYOR + ~15x token (L2+L7 bağımsız yakınsama) — "ajan sayısını ölçekle" hedefi açık KAPI-kuralı ister; meşru sonuç "uzun süre orchestrator-worker kal" olabilir. K-009/K-010 kapsamını bu partisyonun çıktısı disipline eder.
2. **@path tuzağı (P5):** CLAUDE.md `@import` lazy DEĞİL, launch'ta tam yüklenir — m.20 pointer implementasyonu buna göre; iki AYRI 200-satır kuralı var (CLAUDE.md yumuşak / MEMORY.md sert 200-satır∨25KB).
3. **P16-P17 = K-009 tasarım ön-koşulu** (güvenlik-kapısı önerisi; rapor öneri 3).
4. **P18-P19 erken-tohum:** kalibrasyon alışkanlığı ilk öznel model-seçiminde gerekir — Ağustos'u bekletmez. Fatebook V25-istisna adayı (SALİH KARARI BEKLİYOR).
5. **Karpathy revizyonu (K-015 madde 3) bu müfredatla BİRLEŞTİ:** P0 + P1-P4 = eski "Karpathy revizyonu"nun genişletilmiş hali; ayrı iş kalmadı. Loop-eng Faz 2+4 ANA SIRADA ayrı yürür (`ogrenme/loop-eng-yol-haritasi.md`).

## Açık kararlar
- ~~P0 durumu~~ KARARA BAĞLANDI (07-15): mini-teşhis açılışı (yukarıda).
- **Fatebook — BEKLEMEDE (Salih, 07-15):** "önce sistemi anlayayım (en kötü sezgisel), sonra belki hafif revize ederek kullanırız" → sıra: kalibrasyon/Brier kavramı P19'da (ya da erken mini-anlatımla) anlaşılır → SONRA benimseme kararı; muhtemel yol dosya-temelli/revize kullanım. O zamana dek senaryo-defteri tahminleri defterde birikir, skorlanmaz.
- İlk oturum tarihi ("günaydın, öğrenme") — tetik ÇEKİLEBİLİR; paralel deneme = JARVIS + öğrenme çifti.
- **AÇIK BORÇ — gerçek tokenizer ölçümü (07-15, Opus oturumu):** Türkçe/İngilizce token oranı kendi tokenizer'ımızla ÖLÇÜLEMEDİ (tiktoken openaipublic 403 + HF SOCKS proxy bloklu). Şimdilik proxy rakam: GPT-4o ~1.5x (eski BPE ~2x). P1'de çevrimdışı BPE ya da Claude'un kendi tokenizer'ıyla ölç. Karar: kanon Türkçe kalsın (Salih Katman-1; okunabilirlik > ~1.5x, prototipte bağlayıcı değil) — detay ders kaydında.
- **P0 durumu KAPANDI (07-15 Opus):** P0-a + P0-b DONE; Yarı-2 (m.37 3-model) P1/P3/P5-P6'ya foldlandı (Katman-2, devir talimatı notu).
