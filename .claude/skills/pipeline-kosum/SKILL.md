---
name: pipeline-kosum
description: Kun-Chen formatlı görev pipeline'ını kurar ve uçtan uca yürütür (P-1); manifest + emir → scout → rapor → sentez → ship → teslim, tüm durum diskte (restart-proof). Tetik; "pipeline kur", "pipeline olarak yap", araştır-VE-implemente-et sınıfı proje-ölçekli görevler. KULLANILMAZ; küçük direkt işlerde (m.25), salt araştırmada (atlas-kosum yeter), salt karar üretiminde (karar-hatti), seans ritüellerinde.
---

# Pipeline koşum (P-1, v1 — 2026-08-14; m.43 eşiği: spec-kit + ingest + metodoloji koşumları = 3)

Desen kaynağı: firstmate (tek irtibat · scout/ship görev şekilleri · intake sözleşmesi · durum diskte) + `core/ajan-metodolojisi.md` §4 (lider/işçi) + ingest şeması (teslim zarfı).

## Adımlar
1. **Manifest aç** (`cc/pipeline-YYYY-MM-DD-<konu>.md`): görev tablosu — S-n (scout) · G-n (sentez) · SH-n (ship) · T (teslim); sütunlar: şekil / iş / intake / teslim / durum. Altına olay günlüğü. Oturum düşerse yeni oturum buradan devralır.
2. **Görev emrini derle** → `gorev-emri-derleme` skill'i (görev-fonksiyonu iskeleti + mekanik kapılar + KANONDA-BİLİNENLER bloğu).
3. **Scout'u sal:** lider deseni (lider modeli: Karar 85 09-02 — Opus EMEKLİ, FS-masası hükmüne dek lider rolü Fable ana-sırada, paralel araştırmacılar Sonnet ∨ doğrudan atlas-kosum). Dağıtım öncesi zorunlu: paralellik-uygunluk testi (bağımsız keşif mi, ortak üretim mi?). Rejim etiketi + model kademesi (işçi liderden pahalı olamaz) emirden gelir.
4. **Teslim al:** raporu DOSYADAN oku (bildirim özetinden değil); gerekiyorsa V26 örneklem denetimi (kritik rakamlara kendin in). Manifest'e S-n DONE + olay satırı.
5. **Sentez (G) Carvis'te:** rapor + kanon açık-uçları → tasarım. Kanon-aday üretiliyorsa m.40b antitez borcunu AÇIKÇA kaydet (tek-şerit rapor kanonlaşmaz).
6. **Ship (SH):** implementasyon + wiring (CLAUDE.md/kapsül pointer'ları) + commit (push yetki beyanına tabi). Çıktılar ingest-şeması zarfıyla kayda girer.
7. **Teslim (T):** manifest'te tüm satırlar DONE → tek-cümle kaptan beyanı: "**<X> hazır ve sisteme gömülü**". Beyan verilmeden pipeline kapanmış sayılmaz.

## Gotchas
- **Erken implementasyon:** rapor dosyası inmeden SH'ye başlama (akış sırası sözleşmedir).
- **Manifest bayatlaması:** her faz geçişinde durum sütunu + olay günlüğü güncellenir; güncellenmemiş manifest üzerinden beyan verme.
- **Scout kirliliği:** araştırmacılar yalnız kendi rapor dosyasına yazar — repoya başka dosya kaydeden alt-ajan çıktısı (rel.md vakası) commit ÖNCESİ süpürülür (scratchpad'e, silme değil).
- **Beyan disiplini:** Salih beyana göre diğer sekmeleri kapatır — tüm SH'ler bitmeden "hazır" deme.
