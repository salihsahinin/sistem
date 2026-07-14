# cc/ — Claude Code Köprü Kanalı (m.17'nin ilk somut uygulaması; deneysel m.29)

> **Açıklama notu:** Üçlü sohbet düzeninin (Salih karar verici · Carvis köprü/derleyici · CC uygulayıcı) dosya kanalı. Kural: Salih 2026-07-12 4. oturum kararı. CC canlı ajan DEĞİLDİR (K-010 delinmez) — tetik ŞİMDİLİK Salih'te (revizyon 07-14, V52: tetik-sahipliği ilkesel değil araçsal, nihai misyon otomasyon; tam-otomasyon adayları K-018 gündeminde).

## Akış
1. **Görev emri (Carvis yazar):** `gorev-YYYY-MM-DD-N.md` — şablon aşağıda.
2. **Koşum (Salih):** CC'ye tek satır: `C:\JARVIS\cc\gorev-YYYY-MM-DD-N.md dosyasını oku ve uygula.`
3. **Rapor (CC yazar):** `rapor-YYYY-MM-DD-N.md` — adres görev emrinde hazır.
4. **Sunum (Carvis):** raporu okur, KENDİ değerlendirmesiyle Salih'e sunar (katıldığı/katılmadığı ayrı işaretli — kör aktarım yasak, m.6/m.7).
5. **Karar (Salih):** nihai karar her zaman Salih'in.

## Koşum-komutları kuralı (Salih emri 07-15; envanterle kesinleşti aynı gün)
Her görev emrinin "Koşum konfigürasyonu" bölümü, Salih'in CC'ye gireceği komutları AYNEN yazar (karışıklık olmasın diye): `/model` → model + efor kademesi menüden seçilir (ör. Opus → High) + tek satır koşum komutu. Envanter kaydı (07-15): CC 2.1.209 native win32; `/effort` ayrı komutu yok — efor /model menüsünün parçası; Remote Control mevcut (K-018 girdisi).

## Görev emri şablonu
```
# CC Görev Emri — YYYY-MM-DD-N
## Koşum konfigürasyonu (CC'ye girilecek komutlar AYNEN + model/efor; CC'yi C:\JARVIS kökünden başlat — yoksa .claude/agents kayıtları görünmez, 07-15 dersi)
## Bağlam (CC'nin bilmesi gereken minimum)
## Görev (tek net iş)
## DONE