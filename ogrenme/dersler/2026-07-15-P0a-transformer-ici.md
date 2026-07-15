# Ders Kaydı — P0-a: Transformer'ın içi (2026-07-15, YARIM)

> **Açıklama notu:** Bu ders ANA-SIRA oturumunda koşuldu (öğrenme şeridi o gün paralel oturuma taşındı — Salih kararı). Sonraki öğrenme oturumu (ayrı Cowork oturumu, Opus) BURADAN devralır. Format v2 bu okumadan kalibre edildi → `ogrenme/README.md`.

## Ne oldu
1. **Mini-teşhis (12 kontrol noktası):** Salih sonucu net verdi — hiçbiri net değil → P0 sıfırdan. P0 ikiye bölündü: P0-a (transformer içi) + P0-b (tokenizer + eğitim hattı).
2. **P0-a v1 formatında anlatıldı** (etiketsiz, 7 kavram tek teslimde): tahmin döngüsü · token/embedding · self-attention Q/K/V · causal mask · multi-head · FFN/residual/layernorm · öğrenilmiş pos-emb ↔ RoPE farkı.
3. **Salih okuma durumu:** RoPE öncesine dek okudu (RoPE DAHİL DEĞİL — hiç okunmadı). Kısmi anlama: "bazı yerleri anladım, bazılarını tam anlamadım" — hangi blokların bulanık olduğu ALINMADI (v2 açılış sorusu bunu soracak).
4. **Format geri bildirimi → v2 doğdu:** derinlik etiketi [S]/[O]/[T] + 2-3 kavram/blok tempo + self-Q&A + senaryo + bağ cümlesi + görselleştirme. README'ye işlendi, müfredata Derinlik sütunu eklendi.
5. **Karpathy videoları:** Salih kendi hattında çalışacak (Gemini transkript) — P0 DONE'una bağlı değil.

## Sonraki öğrenme oturumunun açılışı (sıra aynen)
1. "P0-a'nın hangi blokları bulanık?" — tek soru, numara/isim al.
2. Bulanık blokları v2 formatıyla (etiket + görsel + self-Q&A + senaryo) yeniden işle. Ana şüphe bölgesi: Q/K/V mekaniği.
3. RoPE bölümünü v2 ile İLK KEZ anlat ([S] yeter: "göreli mesafe kodlar → uzun bağlam mümkün"; dönme matematiğine girme).
4. P0-a Yarı-2 (m.37 3-model) P0-b sonuna ertelenebilir — temel kavramların JARVIS uygulaması P1/P5-P6'da zaten gelecek; ayrı Yarı-2 zorlanmaz (Katman-2 notu).
5. Bitince P0-b'ye geç.

## v1 anlatımın kavram listesi (yeniden işlerken çapa)
Next-token tahmini + sampling döngüsü · embedding = anlam uzayında nokta ("banka" muğlaklığı örneği) · Q="ne arıyorum" K="bende ne var" V="içerik", skor→softmax→ağırlıklı toplam (vardiya raporu benzetmesi) · causal mask = geleceğe -∞ (kopya çekme engeli) · multi-head = paralel ilişki kanalları (zamir çözen head örneği) · FFN = toplantı-sonrası masa başı hesap; residual = "sıfırdan kurma, düzeltme ekle"; layernorm = ölçek stabilizatörü · öğrenilmiş pos-emb sınırı: 1025. pozisyonun vektörü yok ↔ RoPE: Q/K'yı pozisyona bağlı döndürür, yalnız GÖRELİ mesafe kalır.
