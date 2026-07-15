# Ders Kaydı — P0 tamamlama (Opus öğrenme oturumu, 2026-07-15, DONE)

> **Açıklama notu:** İlk paralel öğrenme oturumu (Cowork/Opus, "günaydın, öğrenme"). `2026-07-15-P0a-transformer-ici.md` devir talimatından devraldı; P0-a bulanık-blok telafisi + RoPE ilk geçiş + P0-b tamamı burada koştu. P0 (a+b) DONE — Salih "sezgisel olarak tamam" beyanı.

## Ne oldu (sıra)
1. **Açılış hatası + düzeltme:** Oturum bayat kapsülle 11 maddelik yeni mini-teşhisle açıldı; Salih "son haliyle baştan al" dedi → devir talimatı okundu, gerçek açılış = "hangi bloklar bulanık?" tek sorusu.
2. **P0-a bulanık-blok tespiti:** Salih blok 1-2 net; "2'nin özetiyle, 3'ten başla" → bulanık = 3+ (Q/K/V ve sonrası).
3. **P0-a v2 telafisi (görselli):**
   - Blok 3 · self-attention Q/K/V — görsel `self_attention_qkv_akisi` (skor→softmax→ağırlıklı toplam, "kenar"→"nehir" örneği). Salih: "sezgisel anladım".
   - Blok 4+5 · causal mask + multi-head — anlatıldı; NOT: bu blokta görsel üretilmedi ama metinde görsele atıf yapıldı (hata, Salih işaretledi). Salih sezgisel onayladı, görsel ertelendi.
   - Blok 6+7 · FFN/residual/layernorm + öğrenilmiş pos-emb — görsel `transformer_blok_anatomisi`.
   - **RoPE [S] ilk geçiş** — görsel `pos_emb_vs_rope_farki` (DONE kapısı: öğrenilmiş=mutlak&tablo-sınırlı · RoPE=göreli&uzun-bağlam dostu). Dönme matematiğine girilmedi.
4. **RoPE→JARVIS senaryosu (Salih sorusu):** düzeltme — RoPE'yi kullanmıyoruz, *sonucunu* kullanıyoruz (lost-in-the-middle → kritik bilgi kenarda+kısa bağlamda → durum-kapsulu üstte+kısa, m.20 pointer). P3'e köprü.
5. **P0-b (görselli):**
   - Blok 1 · tokenizer/BPE/tuzaklar — görsel `tokenizer_parca_ve_tuzaklar`. BPE örneği (the→th→the) tam açıldı (Salih format-notu üzerine).
   - Blok 2 · special token'lar + pretraining/SFT/RLHF + halüsinasyon kökü [S] — görsel `egitim_hatti_ve_halusinasyon`. Halüsinasyon kökü: hedef "olası metin", "doğru" değil → m.39/V8/V26 sigortası.

## Salih format geri bildirimleri (v2'ye işlenecek)
- **"Örnekleri sonuna kadar aç":** örnek verince tek cümlede bırakma, adım adım işlet (BPE the-örneği gibi). → README v2 destek elementlerine eklendi.

## Bulgu — Türkçe kanon token maliyeti (DENEYSEL, proxy; açık borç)
- Kendi/GPT tokenizer'ıyla ölçüm **yapılamadı** (tiktoken openaipublic 403 + HF SOCKS proxy bloklu). AÇIK BORÇ: gerçek tokenizer'la (Claude'un kendisi ya da çevrimdışı BPE) ölç.
- Offline ara bulgu (bizim 3 cümlelik örnekle): Türkçe karakter/byte = İngilizce'nin ~0.85x'i (daha AZ) — sondan eklemeli.
- Literatür (proxy, web): GPT-4o Türkçe ~1.8 tok/kelime vs İngilizce ~1.23 → **~1.5x token** (eski tokenizer'da ~2x). Karakter≠token; ters yön çünkü tokenizer İngilizce-ağırlıklı.
- **Karar (Salih Katman-1, öneri verildi):** kanon Türkçe kalsın (okunabilirlik değeri; ~1.5x prototipte bağlayıcı değil); yük sıcak katmanda → damıtma/pointer ile küçük tut; commit mesajları zaten İngilizce (m.10). Bütçe bağlayıcı olunca gerçek ölçümle yeniden bak.

## Yarı-2 kararı (Katman-2)
P0 ön-koşul kapısı; ayrı m.37 3-model Yarı-2 ZORLANMADI. Temel kavramların JARVIS uygulaması P1 (token ekonomisi), P3 (RoPE→200-satır), P5-P6 (context eng.) partisyonlarında zaten gelecek — devir talimatındaki not uygulandı.

## Sonraki oturum
- **P1 — Token ekonomisi & bağlam=maliyet** [T]. Açılışta bu kaydın token-bulgusu P1'e doğrudan girdi (Türkçe ~1.5x + damıtma gerekçesi).
- Açık borç taşınır: gerçek-tokenizer ölçümü (P1 içinde yapılabilir).
