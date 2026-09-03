---
name: gorsellestir
description: Salih "görselleştir" dediğinde o anki içeriği (son cevap ∨ belirtilen bölüm) sınıflandırır, literatür-tabanlı karar tablosuyla görsel türünü seçer, spec yazar, tools/gorsellestir.py ile tek-dosya HTML üretip LLM'siz kapıdan geçirir; yan-oturumda da çalışır. KULLANMA: resim üretimi, Lavish review, graf/ yeniden-üretimi, sözdizimi öğretimi.
metadata: { owner: carvis, version: "0.1.0-deneysel-m29", kaynak: "raporlar/2026-09-03-ib77-gorsellestir-atlas.md" }
---

# gorsellestir — o anki içeriği doğru görsele çevir (İB-77, v0.1, 2026-09-03)

**Kritik talimatlar (ilk blok):** (1) LLM yalnız **spec** yazar; üretim + doğrulama `python3 /Users/HasanSalihSahin/jarvis/tools/gorsellestir.py` (deterministik, saat okumaz). (2) Kapı PASS olmadan teslim yok; ≤2 yeniden-spec, sonra HATA damgalı teslim. (3) Uydurma veri YOK: sayısal görselde değerler kaynak partisyondan birebir. (4) Kanon/commit yazmaz (T-Ü). (5) Yan-oturumda (cwd jarvis değil) çıktı `<cwd>/gorsel/`, jarvis kütüğüne yazılmaz. (6) HTML içeriği sohbete dökülmez — yol + `open` (KB-50). (7) Katman-1 karar gerektiren şey yok; sınıf belirsizse TEK soru (m.4).

## Adımlar
1. **Hedef partisyon:** Salih bölüm belirttiyse o; yoksa SON cevap. Partisyonu 1-3 cümleyle özetle (`kaynak_ozet`) ve pointer yaz (`kaynak_pointer`: dosya yolu ∨ "oturum: <tarih> <kısa başlık>").
2. **İçerik sınıfı (Munzner: abstraction):** tek alan doldur — `icerik_sinifi ∈ {surec, kavram-iliskisi, karsilastirma, hiyerarsi, zaman-akisi, mekanizma, sayisal-dagilim, sayisal-iliski, zaman-serisi, sayisal-karsilastirma, parca-butun, akis-miktari}`. Birden fazla sınıf ∧ ayrılabilir → bölüm başına ayrı görsel (en fazla 3); ayrılamaz → tek soru. Görselleştirilecek yapı yoksa (sohbet, tek cümle) → "yapı yok" beyanı, görsel üretme.
3. **Tür + araç (idiom → algorithm):** karar tablosu `references/karar-tablosu.md` (sentez §3 ile aynı). Öncelik: d2 (elk) / dot çevrimdışı-deterministik → Mermaid (timeline, sankey, mindmap, sequence) → Vega-Lite (sayısal) → HTML tablo (nitel karşılaştırma). Kural: bar/area eksen 0'dan; pasta yerine çubuk; Okabe–Ito palet (script enjekte eder); >12 düğüm → böl. **Kip (Salih hükmü 09-03):** varsayılan `cdn` (Mermaid/Vega-Lite tarayıcıda CDN ile render); Salih "offline/çevrimdışı" derse ∨ çıktı ağsız açılacaksa `--offline` — Vega-Lite `vl-convert`, Mermaid `mmdc` ile yerelde SVG'ye çevrilip gömülür, HTML'de dış URL sıfır, kapı gerçek render'ı doğrular (cdn kipinde yalnız yapısal).
4. **Öğrenme kuralları (yön, rakamsız):** coherence (süs yok — Salih "hatırlatıcı olsun" derse gevşer), signaling (ana öğe vurgulu), spatial contiguity (`aciklama` maddeleri görselin yanında, 1-5 madde), concept map hiyerarşik + etiketli ok, "ilk kez öğrenilen" konuda önce çözülmüş örnek.
5. **Spec dosyası yaz** (scratchpad ∨ `<cwd>/gorsel/`): `{baslik, kaynak_ozet, kaynak_pointer, icerik_sinifi, gorsel_turu, arac, spec, aciklama[], tarih (bugünün ISO tarihi — sistemden), ogrenme_notu?}`.
6. **Üret + doğrula:** `python3 /Users/HasanSalihSahin/jarvis/tools/gorsellestir.py <spec.json> --dogrula --json` → `gecti` ∧ çıkış 0 mu? FAIL → `kontroller[]`'daki düşen kontrolü düzelt, ≤2 tur. Çıktı yolu script'ten (`cikti`).
7. **Teslim (CLAUDE.md §5):** tam mutlak yol + `open <yol>` komutu (tarayıcı) + tek satır: sınıf · tür · araç · kapı sonucu (örn. "doğrulama 7/7 PASS"). Jarvis içindeyse Lavish opsiyonel (Salih isterse). Kütük (jarvis içi) script tarafından `veri/bronz/gorsel-olay.jsonl`'a yazılır — sen yazmazsın.

## 9-alanlı çağrı (skill-tetikleme-semasi)
skill=gorsellestir · tetik_kosulu="görselleştir"/eş kalıplar (evals) · cagri_kipi=kullanıcı-tetikli (model önerir, kendiliğinden koşmaz) · girdi=hedef partisyon · baglam=cwd (jarvis ↔ yan-oturum) · yan_etki_damgasi=yok · done_yuklemi=HTML ∧ kapı PASS ∧ yol teslim · hata_yolu=≤2 yeniden-spec → HATA damgalı · sira=tekil.

## Gotchas
- **Sınıfı görselin cazibesine göre seçme:** önce içerik sınıfı, sonra tür — "sankey güzel" diye akış-miktarı olmayan süreci sankey yapma (Munzner sırası).
- **Sayısal görselde tablo sayımı:** kapı `data.values` satır sayısını sayar; kaynak tabloda 4 satır varsa 4 satır — eksik/fazla satır = uydurma.
- **Metin satırları DENEYSEL (m.29):** karar tablosunun metin (süreç/kavram/hiyerarşi…) satırları literatürde normatif kaynağa sahip değil (İB-77 hakem T1 = X); Salih "yanlış tür" derse tabloya kalibrasyon satırı düşer, savunma yok.
- **Mermaid/Vega-Lite çevrimiçi:** CDN olmadan açılmaz; çevrimdışı gerekiyorsa d2/dot/tablo seç (kapı bunu bilmez — sen seç).
- **Data-ink minimalizmi kural değil** (Bateman 2010): "süs yok" varsayılan, öğrenme-hatırlama isteğinde bilinçli gevşet.
- Skill commit yapmaz; kanon yazmaz; yan-oturumda staj/öğrenme kuralı: çıktı yerel, jarvis'e taşıma Salih devir notuyla.
