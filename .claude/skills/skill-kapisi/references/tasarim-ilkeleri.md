# Tasarım ilkeleri (skill-kapisi referansı)

> **Taşınma (İB-92, Karar 96 M2 A5, 2026-09-15):** bu metin `KILAVUZ.md`'den aynen taşındı (m.8: silme yok, KILAVUZ'da pointer kaldı); kural kaynağı yine tüzük/karar numaraları, burada yalnız gövde. Skill üretimi/evrimi sırasında `skill-kapisi` K1/K3 kapılarında okunur. Büyük-harf = kod kuralı (Karar 97) uygulanmış hâl.

## Kaynak başlık: Tasarım ilkeleri (sıkıştırılmış 09-04; tam gerekçeler + Salih aynen-beyanları `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2026-09-04.md` §1)
- **Yapı-darboğazı yerleşim (Salih imzası 08-29, Karar 79 D3/KL18-13; kaynak `cc/rapor/2026-08/rapor-2026-08-01-18.md:389`):** yerleşim/öncelik talep verisinden değil yapının darboğazlarından ("işler nereden geçiyor"); ölçüm: talep-bazlı greedy 6,7-7,9× çöker, topoloji-bazlı değişmez.
- **Tarama-yöntemi seçimi (KB-57 A, 08-21, Karar 64):** anahtar varsa **search** · küçük tablo tam agregasyon **scan** · çok-kolon agregasyon → parquet/DuckDB · bronz metin → rg · keşif → **sample** · silver yenilemesi sonrası `ANALYZE` · **automatic index** → kalıcı indeks adayı · **like** önek → aralık; karar değişkeni **dokunulan sayfa** (yüzde-eşiği yazılmaz). Tarif `wiki/tarama-yontemleri.md`.
- **Adresli erişim (KB-53/54 A, 08-21, Karar 62; ölçüm 27-563× token):** adres varsa **aralık** oku; anahtar varsa silver blok (sha8 yeniden hesaplanır, tutmazsa dosyaya düş + bayrak); bütün dosya yalnız adressizken; silver tazeliği açılış kapısında; sayaç İB-29.
- **Graf-dili v0 (KB-60 A, 08-22, Karar 67):** graf `graf/` script-türetimli d2+svg (`tools/pointer-graf.py`; elle düzenlenmez); düğüm adı = D2 anahtarı; yapısal soru SQL, yorum panoya; sürüm+sha `graf/pointer-sistemi-v0-uretim.json`; plan `raporlar/2026-08/2026-08-22-graf-dili-uzun-vade-plani.md` §1.
- **Dil-seçimi (KB-64 A, 08-26, Karar 69):** kural kaynağı `wiki/dil-secimi.md`; 9 sınıfın 7'si Python-stdlib+bash, Go/Rust yalnız MCP/dış-dağıtım tetiğinde, **cue** girmez; dil geçişi **otomatik değil** — Salih masası (şerh aynen arşivde).
- **GİRMEZ — agile pratikleri (KB-49 A, 08-21, Karar 56):** story point · velocity · planning poker · flow efficiency · **sle** olasılık beyanı · daily standup · "Sprint" adı; kaldırma Katman-1; gerekçeler arşivde.
- **Alt-ajan içerik-karantinası (Karar 54b, 08-21; m.29):** dış/hacimli içerik ana bağlama girmez — alt-ajanda işlenir, özet+pointer döner.
- **Öğretim taban-yoklaması adım-0 (Karar 54g, 08-21):** yeni konudan önce Salih'in terim tabanı yoklanır, anlatım seviyelenir.
- **Sürtünmesizlik (#18):** sık akışın çağrısı kolay + çapalı; ilk soru "çağırmak kaç saniye sürer?"
- **Bayat-kapsül riski (V4):** yanlış kapsül boş kapsülden kötü; kapanış disiplini atlanmaz.
- **Jarvis-içi araç sınırı (E-1, Karar 76, 08-29):** no-mistakes + treehouse **serbest** · gnhf **koşullu** (worktree ∧ yazılı bütçe ∧ push kapalı) · hiçbir otomat kanona (core/ · CLAUDE.md · tüzük · defter) yazamaz.
- **HAZIRI temel AL (Salih Katman-1 08-17 KB-14; V25 tersine):** hazır araç/yöntem/metrik varsa onu temel al, sıfırdan benzerini yazma; seçim ölçütü yıldız-yasağı üçlüsü; istisna gerekçeli (m.16). Salih örneği (WezTerm) arşivde.
- **Ölçek şerhi — V1 iterasyon > spec-first (08-17 KB-14):** m.25 eşiği üstü çok-ajan/otomasyon işinde intake spec-önce olabilir; altında iterasyon esas. Spec-kit kurulmadı, deseni alındı.
- ~~**Metafor haritası (V12)**~~ `EMEKLİ` 08-17: terimler metaforsuz, tek anahtar (`core/baglam-anahtar-kaydi.md`); sözlük `DONDU` (m.3).
- **md yüzeyi — insan-yüzü rapor biçimi:** QuickLook **iptal** (Karar 72) → Obsidian → **VS code (Karar 80, 08-29; update 09-04 — eski satır Obsidian diyordu)**; **gfm** tablo · görev kutusu · ```mermaid · dipnot · `<details>` · `[[wikilink]]` · `$matematik$` serbest; ilk-12-satır damga kuralı baki; HTML teslim etkilenmez. Link biçimi ileri-dönük md-link (Karar 72 EK, seçim A), geçmiş gövde yeniden yazılmaz (m.8); türev harita `tools/obsidian-harita.py`.
- **Yıldız yasağı (md.33, Salih imzası 08-01):** GitHub yıldızı ölçüt olamaz; adaylar indirme-sırası + son-sürüm + bakımcı üçlüsüyle tablolanır; reddedilen "şu an alınmaz" listesine (md.34).
