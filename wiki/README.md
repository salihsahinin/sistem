# wiki/ — Şirketin Beyni

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
- [[sozluk]] — Carvis sözlüğü (Homebase'ten taşındı 07-15; DONDU — ekleme yalnız Salih talimatıyla, m.3)
- [[loop-engineering]] — loop kurma el kitabı (Homebase'ten taşındı 07-15)
- [[orca]] — Orca/ADE notları (Homebase'ten taşındı 07-15)
- [[kokenler-karpathy-llm-wiki]] — LLM-wiki fikrinin kökeni, Karpathy gist (taşındı 07-15)
*(index tamlama 07-22, K-019 turu — dört sayfa taşınmış ama index'e işlenmemişti)*

## Kuyruk (sonraki oturumlar)
- skill-katmanlari — proje-skill vs hesap-skill + terfi süzgeci + pointer-ilkeli skill deseni (07-23 hasadı).
- rol-katmanlari (m.44) — CEO ≠ üst-orkestratör ≠ domain-lider; aday sayfa (07-21 borcu).
- Çelişki kapısı (m.16) — sonraki oturum adayı (07-12 canlı örnekleri tazeyken); Salih notu: kontrol DAİMA dar kapsamlı, "tüm projeyi tara" yasak sınıfı.
- DONE kuralı / loop temelleri — loop verisi gelince (Salih 07-12: "beraber loop kurup düşünürken revize ederiz; bu haliyle KILAVUZ'da dursun yeter").
- İlk parti kalanı (5 kavram planı, 07-10) — tempo kuralıyla sırada.
