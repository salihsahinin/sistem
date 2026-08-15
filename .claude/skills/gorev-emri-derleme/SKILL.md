---
name: gorev-emri-derleme
description: Salih'in araştırma/görev beyanını künyeli, görev-fonksiyonu-şablonlu ajan emrine derler (S-K). Tetik; "araştırma emri yaz", "görev emri derle", "emri hazırla", ajan/atlas/pipeline koşumu öncesi emir dosyası gerektiğinde. KULLANILMAZ; emir dosyası gerektirmeyen küçük direkt işlerde (m.25 ölçek-tercihi), karar üretiminde (karar-modeli/karar-hatti) ve emrin kendisinin koşumunda (koşum atlas-kosum/pipeline-kosum işidir).
---

# Görev-emri derleme (S-K, v1 — 2026-08-14; m.43 eşiği + 30-15 §6 melez deseni)

İçerik liderden/Salih'ten gelir; bu skill MEKANİK KAPILARI garanti eder (30-15: mekanik kapı skill yolunda ≈0/5 hata). Kural kaynağı: `core/ajan-metodolojisi.md` + iskelet `core/sablonlar/gorev-fonksiyonu.md`.

## Adımlar
1. **Ölçek kontrolü:** iş emir-dosyasız yapılacak kadar küçükse DERLEME — direkt yap (m.25). Emir dosyası proje-ölçekli/ajanlı işler içindir.
2. **İskeleti doldur** (`core/sablonlar/gorev-fonksiyonu.md`): alan adları görevin kendi dilinden ("alan adı talimattır") · `kapsam_disi` ZORUNLU dolu ("sana ait olmayan" — iş-tekrarı freni) · dallar numaralı, m.38 bağlaçlı, **dal+koşul ≤5** (aşarsa görevi BÖL) · `done_yuklemi` boolean (derece ifadesi yasak) · blok sırası: statik önce, tarih/SHA/tetikleyen-mesaj EN SONDA (cache).
3. **Mekanik kapılar (her emirde):** rakam-damgası şartı (m.39: rakam kaynaklı, kestirim `[?]`) · dürüstlük şartı (uydurma YASAK, "bulunamadı" meşru, erişim engeli bayraklanır) · D/K/X etiket disiplini · işçi dönüş bütçesi ≈1-2k token · teslim adresi (`cc/rapor-YYYY-MM-DD-N.md`) · KANONDA-BİLİNENLER bloğu (mükerrer araştırma freni — ilgili eski rapor bulgularını "verili kabul et, üstüne koy" diye listele).
3b. **Halüsinasyon derecesi (paket v1 — `core/halusinasyon-paketi.md` §2):** ÇIKTI SÖZLEŞMESİ'ne `halusinasyon_derecesi` yaz — `python3 .claude/skills/halusinasyon-engelleyici/scripts/derece.py --v… [--pahali-geri-alma]` (v1 nadirlik · v2 tazelik · v3a-d çıktı-türü · v4 uzunluk · v5 bileşiklik · v6 öncül · v7a-c kaynak · v8 doğrulayıcı · v9 runtime · v10 dil). H ≥ eşik (7 / pahalı-geri-alma 4) ∨ atıf/künye çıktısı ⇒ SKILL TETİKLERİ bloğuna `halusinasyon-engelleyici` çağrısı (cagri_kipi literal ya da örtük; kaynak-topraklama + bağımsız doğrulayıcı zorunlu); 4 ≤ H < eşik ⇒ emre F1+F2 (yapılandırılmış kaynak + destek-kontrolü) koşulu.
4. **SKILL TETİKLERİ bloğu (tetiklenme şeması v1 — `core/skill-tetikleme-semasi.md`):** emir bir skill çağırıyorsa çağrı başına 9 alan (skill · tetik_kosulu · cagri_kipi · girdi · baglam · yan_etki_damgasi · done_yuklemi · hata_yolu · sira) + kayit satırı; çağrı yoksa "yok" yaz. Sonra deterministik Kapı-Ö: `python3 .claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py <emir> --repo ~/jarvis` — BLOKE çıkarsa emir teslim edilmez (yan-etkili skill örtük/alt-ajandan çağrılamaz; derece ifadesi yasak; retry ≤3; FAIL-LOUD).
5. **Künye + kayıt:** dosya `cc/gorev-YYYY-MM-DD-N.md`; pipeline'a bağlıysa manifest tablosuna intake satırı.
6. **Son okuma:** emri Salih'in beyanına karşı kontrol et — beyanda olup emirde olmayan koşul var mı (DRFR mantığı: her koşul tek tek).

## Gotchas
- **Dev-fonksiyon tuzağı:** her şeyi tek emre sıkıştırma — koşul arttıkça izleme düşer (Multi-IF 0,877→0,707); böl, zincirle.
- **`kapsam_disi` boş bırakma:** belgeli arıza sınıfı (iki ajan aynı işi yapar, bir konu boşta kalır).
- **Paralel emirlerde** dağıtım öncesi zorunlu soru: alt-görevler bağımsız bilgi mi topluyor, ortak çıktı mı üretiyor? Ortak-üretim → tek şerit ∨ paylaşılan karar-manifesti.
- Skill kaydetme/commit yapmaz; commit vardiya akışının işidir (yan-etki freni).
