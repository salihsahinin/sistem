# Perspektif partisyonu — Atlas koşumu teslimi (2026-09-18, Karar 102)

*Soru: çok-ajanlı sistemde ajan sınırı hangi perspektife göre çizilir; alt-ajan ile kalıcı ajan farkı; öğrenme oturumu ayrı ajan mı; model katmanlaması. Usul: m.40b v0.2 — 4 aile tez (Sonnet) → 4 hedefli antitez (Sonnet, yalnız iddia listesi) → V26 örneklem-denetimi (35 sondaj) → maskeli hakem (Opus 5 medium). Ham raporlar `cc/rapor/2026-09/rapor-2026-09-18-perspektif-*.md` (10 dosya). Rakamlar hakem raporundan; deneysel m.29; AS-OF 2026-09-18.*

## 1. Tek bakışta
| Perspektif | Hüküm | Gerekçe sınıfı | Kanıt |
|---|---|---|---|
| Hakem / değerlendirici | **ayrılmalı** | yapan ≠ ölçen + önceden bağlam paylaşmama | D · 2 güncel kaynak (Cognition 2026-04 Code-Review-Loop: 2 hata/PR, %58 şiddetli; Claude Code sub-agents belgesi 2026-09) |
| Gözetim / orkestrasyon | **ayrılmalı** (zaten ayrı: Jarvis) | bağlam sıkıştırma + paralellik | D |
| İcra · araştırma | **ayrılmalı** (zaten ayrı: Atlas/işçi) | salt-okur paralel alt-görev | D |
| İcra · refactor / taşıma | **kalmalı** (tek iş-parçacığı) | paralel yazan ajan bağlamı kirletir, çelişen zımni karar | D · Cognition 2025-06 + Anthropic 2026-02 |
| İcra · doküman · ölçüm | belirsiz | kaynak tek/ikincil | K |
| İcra · hakem kurma | belirsiz | kaynak yok | X |
| Antitez / red-team | belirsiz | tek kaynak, tarihsiz/model damgasız (güvenlik alanı) | K |
| Planlama | belirsiz | sayısal destek V26'da düştü (yanlış kaynak eşleşmesi) | K |
| Öğretim / tutor | belirsiz | akademik kaynak model-sürümsüz; pratisyen vakası yok | K |

Ayrılmalı eşiği: ≥2 bağımsız güncel-kuşak kaynak. Üç satır geçti; ikisi zaten ayrı. **Ayrılmamış tek D satırı: hakem.**

## 2. Alt-ajan ≠ kalıcı ajan (hakem §ii, D)
Alt-ajan = izole bağlam + tek dönüş kanalı (yalnız son mesaj) + kısıtlanabilir yetki; kalıcı ajan = adlandırılmış kalıcı **dizin** (`memory` alanı, MEMORY.md ilk 200 satır/25 KB sistem promptuna) + kendi deposunu yazma yetkisi. Süreç kalıcılığı hiçbir üründe yok; "kalıcı ajan" pratikte kalıcı dizindir. "Hafıza dizinleri birbirini göremez, by design" alıntısı güncel belgede yok → X. Maliyet: çok-ajan ≈15× sohbet token'ı, tek ajan ≈4× (Anthropic 2025-06, eski kuşak).

## 3. Model katmanlaması (hakem §iii)
- "İşçiler ucuz model" → **destekli** (güncel, D).
- "En güçlü model yalnız orkestratör" → **çelişir**: ölçülmüş tek düzen tersi (Opus 4 lider + Sonnet 4 işçi, +%90,2, eski kuşak); güncel pratik (Cognition 2026-04 "Smart Friend") sabit hiyerarşi değil, ucuz model varsayılan + talep-üzerine eskalasyon.
- "Kalıcı liderler orta model (Opus)" → **dayanaksız**: hiçbir kaynak yok. Salih'in "Opus daha iyi olur" tahmini dış kanıtla ne destekleniyor ne çürütülüyor; iç ölçüm konusu.

## 4. Öğrenme oturumu ayrı ajan mı
Belirsiz (K). Tutor literatürü rol ayrımını savunuyor (DeepTutor 2026-04: kalıcı öğrenci modeli; PETITE 2026-04 generator/evaluator ayrımı, Qwen2.5-Coder-7B) ama model-sürümü ve pratisyen vakası eksik. Karar 102 (2): literatür yetmedi → iç ölçüm. Ölçülecek: `ogren` oturumlarında Jarvis kanonunun bağlamda kapladığı pay ve öğretim kalitesine etkisi (hakem §vi).

## 5. Hayatta kalma (48 iddia)
Sağlam 33 · daralan 8 · düşen 7. Aile: A 10/2/0 · B 10/1/1 · C 5/3/4 · D 8/2/2. En sağlam aile sektör öncülleri (A), en zayıf akademik (C: yanlış kaynak eşleşmesi ×2, yön hatası ×1). V26 denetimi 5 raporda `TUTMADI` buldu; hakem 3 ek sondajla düzeltti.

## 6. m.16 çelişkiler (hakem işaretledi, çözmedi)
1. Kanon hakemi **alt-ajan** sayıyor (Karar 93 M7-1, Karar 99 M6); kanıt "önceden bağlam paylaşmayan, beklentisi maskelenmiş ayrı ajan" istiyor. Bu koşumda maske usulle uygulandı, mekanizmayla değil.
2. Karar 89 üç katmanı (Fable → Opus 5 lider → Sonnet işçi) dış kanıtla değil iç tercihle duruyor; "orta model kalıcı lider" için kaynak yok.
3. Güncel kuşak sabit hiyerarşiden uzaklaşıyor (eskalasyon deseni).
4. "Ana-sıra proje işini yapmaz" ile "refactor tek iş-parçacığında kalmalı" gerilimde: sorun paralellik değil, yazma yetkisinin dağıtılması.

## 7. Masa kalemi (hakem §viii; önerilen ilk sırada)
**Hangi perspektif önce ayrı ajana çıkarılsın?**
1. **Kalıcı, bağlam paylaşmayan hakem ajanı (öneri):** `.claude/agents/hakem` tanımı, salt-okur, beklenti maskesi emir şablonunda, V26 sondajı girdisine bağlı. Artı: tek D + ayrılmamış satır; yazma yok, geri-alma riski sıfır; bu koşum mekanizmanın kanıtı (7 düşen, 8 daralan). Eksi: token ≈15×; hakem kendi kaynak hatasını yapabilir, V26 zorunlu kalır.
2. **Aynı ajanda temiz-bağlam hakem turu:** ucuz, yeni dosya yok; ama yapan ≠ ölçen yalnız usulde, yetkide değil; kanıt bunu ölçmüyor.
3. **Ertele, iç ölçüm:** rakam kendi verimizden; ama D satırını geciktirir ve ölçüm zaten hakem ajanı ister (döngüsel).

Bağlantı: İB-108 hakem ajanı (Karar 99 M6 ilk vaka) = seçenek 1'in icrası; m.16 çelişki 1 bu kalemle çözülür (hakem alt-ajan mı kalıcı ajan mı → hakem bulgusu: kalıcı dizin, maskeli, salt-okur).

## 8. Sırada
Zincir 2/2 emri: **gelişen hafıza mimarisi** (girdi: §2 tablosu — kalıcı ajan = kalıcı dizin; MEMORY.md bütçesi; ajan başına dizin; FIFO/çekirdek deseni literatürde nasıl). Koşum profili gerçekleşen: 10 ajan (4+4+1 denetçi+1 hakem), alt-ajan toplam ≈864k token, duvar-saati ≈32 dk (bildirim sayaçları).
