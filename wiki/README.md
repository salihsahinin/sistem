# wiki/ — Jarvis'in Beyni (eski ad: Şirketin Beyni)

> **Açıklama notu:** K-012 build adım 3 çıktısı (2026-07-12). Kavram-başına LLM-wiki sayfaları (#5 ana rol, Salih teyitli; #16). Yazım standardı DENEYSEL DAMGALI (m.29) — kullanım verisiyle kalibre edilir. Kaynak desen: Karpathy LLM-wiki + v2 uzantısı (confidence/süpersede; pointer: `raporlar/2026-07-12-K013-ekosistem-arastirmasi.md`).

## Yazım standardı — sayfa şablonu (6 blok)
1. **Üst blok:** 1-2 cümle tanım · durum (GÜNCEL/BAYAT) · son-teyit tarihi · kaynaklar · kaba güven (düşük/orta/yüksek — kaç kaynak + ne kadar taze + çelişen var mı).
2. **Çekirdek:** kavram sade dille + **1 kanonik damıtılmış örnek** (Salih kuralı 07-12: ham senaryo sayfaya girmez — raporda/logda pointer'la durur; sayfaya deseni yeniden üretebilen EN KÜÇÜK hali yazılır; örnek bağlam-verimi yüksek seçilir).
3. **SOP:** "okuyucu pazartesi sabahı ne YAPAR" — adım adım prosedür (uygunsa). İleride hedef-model parametresi taşıyabilir (#17 ufku: Fable prosedür yazar, alt model uygular); İLK PARTİDE model parametresi YOK.
4. **Gotchas:** o kavramda fiilen yapılan hatalardan biriken tuzak listesi (yaşayan bölüm).
5. **Süpersede zinciri:** çelişen/güncellenen iddia silinmez — "yerini aldı: [tarih, yeni iddia]" damgasıyla işaretli durur (m.8 + çelişki kapısının wiki hali).
6. **[[wiki-link]]'ler + index kaydı** (V24 standardı; index = bu dosyanın alt bölümü, ~100 sayfaya dek yeterli).

Tempo kuralı: oturum başına 1-2 sayfa, toplu üretim yok (07-10 Salih kararı).

## Index
- [[token-x-zaman]] — iki eksenli maliyet modeli (tüzük dipnotu; farklılaşma tezinin çekirdeği)
- [[pointer-sistemi]] — m.20; özet sıcakta, detay dosyada
- [[adversarial-hayatta-kalma]] — m.40b v0.2 sağlamlık ölçütü; DARALTILDI/DÜŞTÜ kovaları (eklendi 07-22, K-019 turu)
- [[ai2ai-rapor-formati]] — ajandan-ajana rapor/emir biçim standardının derleyici sayfası (md.19-25 + m.46 + zarf disiplini; kural koymaz, adresler; eklendi 08-21, Karar 54e)
- [[sozluk]] — Carvis sözlüğü (Homebase'ten taşındı 07-15; DONDU — ekleme yalnız Salih talimatıyla, m.3)
- [[loop-engineering]] — loop kurma el kitabı (Homebase'ten taşındı 07-15)
- [[orca]] — Orca/ADE notları (Homebase'ten taşındı 07-15)
- [[kokenler-karpathy-llm-wiki]] — LLM-wiki fikrinin kökeni, Karpathy gist (taşındı 07-15)
- [[olcum-banki]] — kalıcı sayısal ölçüm defterinin kural sayfası: m.39 giriş kuralı · m.8 çürüme kuralı · uyarı-satırı sınıfı (eklendi 08-01 gece, ana-sıra)
- [[uc-register]] — üç REGISTER + kenar-başına biçim (K2-f kanon adı; eski "üç dil" süpersede; tek-IR'ın düşme gerekçesi B3; eklendi 08-03, K2 icra turu)
- [[gorsel-artefakt-dogrulama]] — SVG/HTML artefaktın okunabilirliği gözle değil bbox ölçümüyle sınanır; sessiz görsel hata sınıfı + bayat-sekme tuzağı (eklendi 08-12, staj hasadı)
- [[ingest-semasi]] — çok-sekme çıktı akışının zarf+tip+triyaj sözleşmesinin anlatımı; sözleşmenin kendisi core/ingest-semasi.md (eklendi 08-14, ingest pipeline turu; index kaydı 08-14 wiki-sayfa-yaz ilk koşumuyla tamamlandı)
- [[stokastik-dusunce]] — **EMEKLİ/RED (Salih 08-17):** stokastik entegrasyon geri alındı; sayfa artık halef ilkeyi taşır — DETERMİNİSTİK TASARIM (LLM'ler ve makineler deterministik düşünür, deterministik tasarlanır); eski içerik `kuyruk/arsiv-stokastik-dusunce-wiki-2026-08-16.md`
*(index tamlama 07-22, K-019 turu — dört sayfa taşınmış ama index'e işlenmemişti)*
- [[paralel-oturum-protokolu]] — çoklu oturumun 4 kuralı (canlı-oturum kapısı · manifest kapısı · paylaşılan kaynak/motor freni · git add -A yasağı) — Salih imzası 08-17 masa (KB-08/09/10)
- [[baglam-veri-ambari]] — bağlam VERİTABANI (operasyonel, V-1) ↔ bağlam VERİ AMBARI (analitik: aynı SQLite'ta ayrı şema/görünüm; erişim-tasarımı ayrımı; bitemporal + SCD-2 + olay↔nesne köprü) tanımı + Jarvis içerik örnekleri (olgu/boyut/mart) — 'context warehouse' dışta tanımsız, m.29 (eklendi 08-16, rapor-16-3 turu)

## Kuyruk (sonraki oturumlar)
- baglam-anahtar-kaydi — silver-katman anahtar/emeklilik/yayılım/metrik kavramı; kural core/baglam-anahtar-kaydi.md, denetim tools/anahtar-denetim.py; ilk vakalar günaydın/Cowork/uyucam (08-15 seans-3 kapanış hasadı).
- paralel-oturum-protokolu — vaka-1 (port çakışması 08-12) + vaka-2 (emir üstyazımı 08-15) + vaka-3 (çift-koşum 08-16) birleşik: canlı-oturum kapısı + koşum-önü manifest kapısı kural adayları (kuyruk/gelen-*-paralel-oturum-vaka-*.md); Katman-1 imza sonrası yazılır.
- veri-tablosu (V-1) — bağlam→veri tablosu v0 şeması (dosya/kayit/referans/anahtar/json_kayit + görünümler), idempotens, sorgu örnekleri; kaynak veri/README.md (08-15 kapanış hasadı).
- ajan-metodolojisi — görev-fonksiyonu + hafıza-manifesti + B1-B4 merdiveni + lider/işçi dörtlüsü; kural core/ajan-metodolojisi.md, anlatım sayfası aday (08-15 kapanış hasadı).
- gnhf / treehouse / lavish — L8 araç üçlüsü aday sayfaları: durma-koşullu koşum (K-009/A3 kanıt bağı) · worktree havuzu/lease · yerel işaretle-geri-bildir döngüsü + share-yasağı (08-04 L8 seans hasadı; kaynak cc/rapor-2026-08-03-4.md + teslim 08-04).
- loop-aday-yüklemi — L3 kademeli form + tekrar-birimi + loop↔skill sınırı (g23 raporu; masa kararlarından SONRA yazılır — 08-01 gece hasadı).
- indeks-aramasi — 'index seek' düzeltilmiş tanım + terim haritası (SQL Server Index Seek/Key Lookup · Postgres Index Scan/IOS/Bitmap · SQLite SEARCH↔SCAN + rowid ikinci iniş · InnoDB PK) + Jarvis erişim yolu (kök→dal→yaprak→heap: kapsül işaretçisi → silver anahtar → kayit_id → aralık; sha8 tazelik) — KB-53/54 imzası sonrası (kaynak `cc/rapor-2026-08-18-1.md` S1-S4).
- silver-saglik — silver temizlik-test mekanizması (bayrak+güncel-görünüm+kuyruk; T-Ç/T-B/T-A; canary + as-of eval) — KB-39..42 imzası sonrası (kaynak `cc/rapor-2026-08-17-1.md` S1-S6).
- hafiza-teknik-envanteri — 'LLM hafıza yönetimi' şemsiyesi ↔ ~10 teknik × Jarvis J1-J15 eşleme matrisi — KB-43..45 sonrası (kaynak `cc/rapor-2026-08-17-2.md` S2).
- baglam-butcesi — bağlam-penceresi kategori anlamları + mutlak-token kural seti + Jarvis sondajı — KB-50..52 sonrası (kaynak `cc/rapor-2026-08-17-4.md` S1-S3).
- skill-katmanlari — proje-skill vs hesap-skill + terfi süzgeci + pointer-ilkeli skill deseni (07-23 hasadı).
- kucuk-n-eval — smoke vs sertifika ayrımı + Clopper-Pearson cebi + 3×-koşum ilacı (07-23 sayı-araştırma hasadı; kaynak cc/rapor-2026-07-23-1.md).
- rol-katmanlari (m.44) — köle ≠ üst-orkestratör ≠ domain-lider (eski ad: CEO ≠ …; emekli 08-17); aday sayfa (07-21 borcu).
- Çelişki kapısı (m.16) — sonraki oturum adayı (07-12 canlı örnekleri tazeyken); Salih notu: kontrol DAİMA dar kapsamlı, "tüm projeyi tara" yasak sınıfı.
- DONE kuralı / loop temelleri — loop verisi gelince (Salih 07-12: "beraber loop kurup düşünürken revize ederiz; bu haliyle KILAVUZ'da dursun yeter").
- İlk parti kalanı (5 kavram planı, 07-10) — tempo kuralıyla sırada.
