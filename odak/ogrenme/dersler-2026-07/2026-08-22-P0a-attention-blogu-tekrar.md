# Ders Kaydı — P0-a tekrar: attention bloğu [T] (2026-08-22, seans-13 açılış sorusu)

> **Açıklama notu:** Salih'in "llm'lerde attention bloğu nasıl çalışır" sorusuna seans-13 açılışında verilen cevabın kaydı. Zemin: `2026-07-15-P0-opus-oturumu.md` (blok 3 Q/K/V "sezgisel"; blok 4-5 mask/multi-head görseli ERTELENMİŞTİ → bu oturumda yapısal harita olarak verildi). Derinlik [T]: mekanizma + elle seçilmiş sayısal örnek + 2 görsel (`attention_sorgu_yelpazesi_icti_ornegi`, `attention_blogu_islem_sirasi_yapisal`; sohbet içi widget, dosyaya gömülmedi). Öğretme modeli: pasif-okuma v2 (README §2), örnek sonuna kadar açık (Salih format notu 07-15).

## Mekanizma (tek kafa, 6 adım)
1. İzdüşüm: `qᵢ = W_Q xᵢ`, `kᵢ = W_K xᵢ`, `vᵢ = W_V xᵢ` — üç öğrenilmiş matris, aynı girdiden üç rol (neyi arıyorum / ben neyim / bulunursam ne taşırım).
2. Skor: `sᵢⱼ = qᵢ·kⱼ / √d_k` — n×n matris; maliyet bağlam uzunluğunun karesi; √d_k softmax doygunluğunu önler.
3. Nedensel maske: `j > i → sᵢⱼ = −∞` — eğitimde tek geçişte her pozisyon sonrakini tahmin eder, gelecek sızmaz; çıkarımla tutarlılık.
4. Softmax satır bazında: `aᵢⱼ = e^{sᵢⱼ}/Σₖ e^{sᵢₖ}` — ağırlıklar ≥ 0, toplam 1.
5. Ağırlıklı toplam: `zᵢ = Σⱼ aᵢⱼ vⱼ` — toplanan v'dir, k yalnız eşleşme içindir.
6. Çıkış izdüşümü + artık bağlantı: `hᵢ = xᵢ + W_O zᵢ` → LayerNorm → FFN. Attention = pozisyonlar ARASI bilgi taşıma; FFN = pozisyon İÇİ işlem.

## Sayısal örnek (3 token, d = 2; sayılar elle seçildi, temiz aritmetik için)
Cümle `kedi süt içti`. x₁=[1,0], x₂=[0,1], x₃=[1,2]. W_Q=[[0,−1],[1,0]] → q=[−x₂,x₁]: q₁=[0,1], q₂=[−1,0], q₃=[−2,1]. W_K=birim → k=x. W_V=[[0,1],[1,0]] → v₁=[0,1], v₂=[1,0], v₃=[2,1].
- Satır 3 (`içti`): skor [−2, 1, 0] → ÷√2 [−1,414, 0,707, 0] → softmax [0,07, 0,62, 0,31] → z₃ = [1,23, 0,38] → h₃ = x₃+z₃ = [2,23, 2,38] (W_O birim).
- Satır 1: yalnız kendini görür (maske) → a₁=[1,0,0], z₁=v₁=[0,1]. Satır 2: skor [−1, 0, maskeli] → a₂=[0,33, 0,67, 0], z₂=[0,67, 0,33].
- Okuma: `içti` ağırlığının %62'sini `süt`e, %31'ini kendine, %7'sini `kedi`ye verdi; taşınan içerik v'lerin bu oranlı karışımı.

## Çok kafa + KV-önbellek
- Multi-head: d → h parça; her parçada ayrı W_Q/W_K/W_V ile 2-5 bağımsız koşar; concat → W_O. Yayımlanmış değerler: GPT-2 small d=768, 12 kafa×64, 12 katman · Llama-2-7B d=4096, 32 kafa×128, 32 katman. Kafa rolleri eğitim sonrası yorumlanır (Anthropic 2022 "induction heads": daha önce geçen token'ın ardılını kopyalayan kafa).
- KV-önbellek: çıkarımda geçmiş k,v saklanır, yeni token yalnız q hesaplar → bellek bağlamla doğrusal, toplam skor maliyeti karesel → "bağlam = maliyet" (P1) buradan.

## JARVIS'e bağ (RoPE→JARVIS dersinin devamı, 07-15)
- Softmax toplamı 1 → uzun bağlamda ağırlık seyrelir → kapsül üstte+kısa, m.20 pointer ilkesi bunun mekanik karşılığı.
- Maske → talimat cevaptan ÖNCE gelmeli (CLAUDE.md'nin ilk yüklenmesi).
- Deterministik tasarım (CLAUDE.md §6): blok matris çarpımı + softmax; rastgelelik yalnız son token örneklemesinde.

## Durum
Salih'in "sezgisel anladım" (07-15) seviyesinin üstüne [T] geçiş verildi; anlama teyidi bu kayıtta YOK (pasif-okuma modeli — teyit Salih beyanıyla). Açık kalan: blok 4-5 için ertelenen illüstratif mask/multi-head görseli (bugünkü yapısal harita maske adımını kapsar; çok-kafa dağılımı ayrı çizilmedi).
