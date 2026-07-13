# cc/ — Claude Code Köprü Kanalı (m.17'nin ilk somut uygulaması; deneysel m.29)

> **Açıklama notu:** Üçlü sohbet düzeninin (Salih karar verici · Carvis köprü/derleyici · CC uygulayıcı) dosya kanalı. Kural: Salih 2026-07-12 4. oturum kararı. CC canlı ajan DEĞİLDİR (K-010 delinmez) — tetik ŞİMDİLİK Salih'te (revizyon 07-14, V52: tetik-sahipliği ilkesel değil araçsal, nihai misyon otomasyon; tam-otomasyon adayları K-018 gündeminde).

## Akış
1. **Görev emri (Carvis yazar):** `gorev-YYYY-MM-DD-N.md` — şablon aşağıda.
2. **Koşum (Salih):** CC'ye tek satır: `C:\JARVIS\cc\gorev-YYYY-MM-DD-N.md dosyasını oku ve uygula.`
3. **Rapor (CC yazar):** `rapor-YYYY-MM-DD-N.md` — adres görev emrinde hazır.
4. **Sunum (Carvis):** raporu okur, KENDİ değerlendirmesiyle Salih'e sunar (katıldığı/katılmadığı ayrı işaretli — kör aktarım yasak, m.6/m.7).
5. **Karar (Salih):** nihai karar her zaman Salih'in.

## Görev emri şablonu
```
# CC Görev Emri — YYYY-MM-DD-N
## Bağlam (CC'nin bilmesi gereken minimum)
## Görev (tek net iş)
## DONE tanımı (ölçülebilir)
## Sınırlar
- C:\JARVIS\core\ dosyalarına YAZMA (yalnız Salih kararıyla değişir)
- portrisk public reposuna iç-mutfak dosyası YAZMA
- Görev dışına çıkma; çıkmak gerekiyorsa rapora "SINIR AŞIMI ÖNERİSİ" başlığıyla yaz, yapma
- Commit atma — commit kararı Carvis/Salih'te (m.9: portrisk commit'leri Salih'in elinden)
## Rapor adresi
C:\JARVIS\cc\rapor-YYYY-MM-DD-N.md (ne yaptın · ne çıktı · ne takıldı · öneriler)
```

## İsimlendirme
Aynı günde birden çok görev: N artar (gorev-2026-07-13-1, -2...). Biten görev+rapor çiftleri ayda bir `cc/arsiv/`e iner (m.8 — silinmez).
