# Ders Kaydı — P3: RoPE, Uzun-Context & Lost-in-the-Middle (2026-07-19, DONE)

> Üçüncü paralel öğrenme oturumu (Cowork/Opus, "günaydın, öğrenme p3"). P1 DONE'dan devraldı (bulanık blok yok). Derinlik [O]. Teslim: tek dosya HTML ders (6 blok + görseller + Yarı-2) — Salih'e chat'te iletildi + `dersler/2026-07-19-P3-rope-context.html`. **Salih onayı: "hepsini okudum istendiği miktarda anladım" → P3 DONE.** Canon güncellemesi (mufredat Durum + kapsül öğrenme satırı) ana-sıraya devredildi (öğrenme şeridi canon'a yazmaz — P1/P2 ile aynı kural): devir `raporlar/vardiya-teslim-2026-07-19-ogrenme-P3.md`.

## Sıra notu (çelişki kapısı, m.16)
Müfredat sırası P2 idi; Salih P3 dedi. Kontrol: P3, P2'ye bağımlı DEĞİL — P0-a'nın RoPE [S] ipini devralır ("P3'e köprü" notu). P2 ayrı dal (inference/sampling), sırada bekliyor. Emir korundu, sıralama bozulmadı.

## Ne oldu (sıra)
1. **Açılış:** kapsül + öğrenme protokolü (README v2) okundu; P1 DONE olduğu için bulanık-blok telafisi yok, doğrudan P3.
2. **Araştırma (m.40 araştırma-önce):** lost-in-the-middle (Liu 2023/TACL 2024), context rot (Chroma 2025), Anthropic bağlam-mühendisliği (dikkat bütçesi + n² + JIT/compaction/not-tutma), RoPE (RoFormer) doğrulandı.
3. **Yarı-1 (6 blok, [O], görselli — hepsi gerçek SVG):**
   - Blok 1 · pozisyon problemi + öğrenilmiş pos-emb duvarı (1024 satır tablo, ötesi tanımsız).
   - Blok 2 · RoPE = Q/K'yı pozisyonla döndürme → attention yalnız GÖRELİ mesafeyi görür (saat-ibresi sezgisi, "kırmızı araba" örneği poz 7-8 vs 39-40, Δ=1 sabit).
   - Blok 3 · frekans bantları [S] (hızlı=yakın, yavaş=uzak mesafe) + ekstrapolasyon sınırı (eğitilen uzunluk ötesinde bozulma; YaRN/NTK isim düzeyinde).
   - Blok 4 · lost-in-the-middle U eğrisi (baş+son yüksek, orta çukur; ortadaki bilgi ~ hiç vermemek).
   - Blok 5 · context rot (uzunlukla tedrici bozulma; uçurum değil eğim; distractor + düşük-benzerlik hızlandırır; P1 O(n²)/dikkat-bütçesi bağı).
   - Blok 6 (çekirdek) · 200-satır tavanının mekanik nedeni = dikkat bütçesi + lost-in-the-middle + context rot birleşimi → sıcak katman güvenilir bölgede kalacak kadar kısa; m.20 pointer + m.34'ün mekanik gerekçesi.
4. **DONE kapısı içeriği hazır:** (a) pos-emb↔RoPE farkı (b) 200-satır tavanının mekanik nedeni — ders içinde açık kutu olarak verildi. Salih okuyup "anladım/bulanık blok" dönünce kapı işaretlenir.
5. **Yarı-2 (m.37 3-model):** JARVIS bağlam/hafıza yerleşimi. A (düz/hepsini-yükle, ~0.55↓) · **B (kısa çekirdek + pointer, ✅ ~0.85)** · C (katmanlı + compaction + not-tutma, ~0.90 ama uzun-oturum-kazançlı). Öneri = B (mevcut m.20/m.34 hizalı, prototip fazına uygun); C'nin compaction+not-tutma parçaları P6'ya köprülendi. Rakamlar deneysel/proxy (m.39).

## Format v2 notu
- Pasif-okuma + derinlik etiketi + 2-3 kavram/blok + self-Q&A + JARVIS senaryo + her yapısal kavrama GERÇEK SVG + sonuna kadar işlenen örnek uygulandı. Görsel-atıf/görsel-yok hatası yapılmadı (6 blok = 6+ SVG, hepsi gömülü).
- [O] bloklar [T]'ye göre kısa; tek teslimde okunabilir uzunlukta.

## Yarı-2 kararı → Şerit 1'e devir
Model B (kısa çekirdek + pointer). Nihai karar + uygulama ANA OTURUMDA (Katman-1/2). C→geçiş kriteri P6'da tasarlanır. Senaryo-defteri kaydı Şerit 1'de.

## Açık borç / taşınan
- Taşınan: modern-tokenizer kesin ölçümü (P1'de banda indirildi) — bu partisyonu ilgilendirmez.
- Yeni: yok.

## Sonraki oturum
- **P2 — Inference & sampling: KV-cache, temperature** [O] (müfredat sırası; sıra Salih'te — P4 halüsinasyon da adaydır).
- Açılış girdisi P2 için: P1 Blok 1'in O(n²)'si + bu dersin dikkat-bütçesi çerçevesi (KV-cache bütçenin bir kısmını nasıl geri kazanır) + ajanlarda düşük-temperature gerekçesi.

## DONE kapısı (Salih onayı 07-19 — geçti)
- [x] pos-emb ↔ RoPE farkı söylenebiliyor
- [x] 200-satır tavanının mekanik nedeni söylenebiliyor
- Ölçüm notu: pasif-okuma modeli → gerçek anlama ölçümü uygulamaya taşınır (hata koşumda çıkarsa oraya gömülür).

## Açılış-hatası düzeltmesi (kendi kaydım — kör onay yok, kendime de)
Oturumu **bayat kapsülle** açtım: `CHAT-KAPSULU-2026-07-13.md`'yi okudum, canon `core/durum-kapsulu.md` (07-19) yerine. README step-1 "kapsül okunur" = canon durum-kapsulu. Sonuç: Salih'e verdiğim çelişki-kapısı notu ("müfredat sırası P2, sen P3 dedin") **eksik bilgiye** dayanıyordu — canon kapsül (07-19, satır 12) P2'nin zaten paralel oturumda koşulduğunu (devir bekliyor) söylüyor. Yani P3 zaten doğru sıradaki adımdı; sonuç değişmedi ama gerekçem yanlış zemindeydi. Ders: açılışta İLK okunan dosya `core/durum-kapsulu.md` olmalı (mufredat/chat-kapsül değil).
