# Üç Register + Kenar-Başına Biçim

**Üst blok:** Şirkette bilginin üç kayıt-düzeyinde (register: aynı içeriğin hedef-okuyucuya göre biçem katmanı) aktığını ve kenarlar arası TEK ortak ara-biçim (tek-IR) olmadığını söyleyen mimari karar. Durum: **GÜNCEL** · son-teyit: 2026-08-03 (K2 masası) · kaynaklar: `cc/rapor-2026-08-02-1.md` (S1-S6, hakem elemeli) · B3 sayımı (`kuyruk/build-tartisma-notlari.md` 08-02) · K2 kayıtları (`kuyruk/senaryo-defteri.md` K2 bloğu). Güven: **orta** (tek araştırma serisi + iç sayım; birbiriyle tutarlı ama tek dalga).

## Çekirdek
Kanon adı **"üç REGISTER + kenar-başına biçim"** — eski ad "üç dil" (süpersede: K2-f, 2026-08-03; Salih kendi kelimesini değiştirdi; destek verisi B3). "Dil" değil "register", çünkü ortada üç ayrı gramer değil aynı dilin üç hedef-okuyucu biçimi var: **L1 İNSAN** (Salih-okunabilir; E5/F1-F9 kuralları) · **L2 AI-to-AI** (önerme-yapılı, m.38 bağlaç seti) · **L3 makine/kod**. İkinci yarı: biçim REGISTER'a değil KENAR'a bağlanır — tek-IR yoktur.

**Kanonik örnek:** L1→L2 kenarı (görev emri): kontrollü yapılandırılmış-MD, Salih-okunabilirliği ZORUNLU kısıt. L2→L3 kenarı (makine tüketicili): şemalı veri, okunabilirlik kısıtı YOK. Aynı içerik, iki kenarda iki biçim — ortak IR'a çevirmek iki kenarın zıt kısıtlarını tek biçime sıkıştırmak olurdu.

**Tek-IR'ın düşme gerekçesi (B3 sayımı, D-ölçüm 08-02):** üretici cephe N≈1-2 < 3 eşiği ∧ deterministik L2-tüketicisi 0 ⇒ paylaşılan ara-biçimin bakım maliyeti karşılıksız; hakem çekirdeği ayakta kalan tek kural: "tüketicisi makine olan kenarda biçim ŞEMALI".

## SOP — yeni kenar açarken
1. Kenarın üretici ve tüketicisini yaz (kim yazıyor → kim okuyor).
2. Tüketiciye göre register seç: makine → şemalı biçim · Salih → L1/İNSAN (E5, F1-F9) · ajan → L2 önerme-yapılı.
3. Kenarı tek etiketle değil ⟨tetik, icra, denetçi⟩ üçlüsüyle sınıfla (S2: skill/loop/kod/ajan tek eksen değildir).

## Gotchas
- Eski metinlerde "üç dil" geçer — tarih yeniden yazılmaz (m.8); okurken bu sayfaya çevir.
- Hibrit denetçi deseni (üretici LLM ≠ deterministik doğrulayıcı) formal hedef-dil olmadan bedava DEĞİLDİR (S4/K2-g damgası — compiler-formulu §4 şerhi).
- Taşıma-kenarı (E0) çeviri kenarı değildir; 08-02 arızası link/load katmanındaydı (S1) — çeviri kurallarıyla çözülmez.
- B3 sayımı bugünü ölçer; yeni üretici-cephe sınıfı doğarsa (ajan dönemi, K-010 sonrası) B3 YENİDEN sayılır (yeniden-açma kaydı defterde).

## Süpersede zinciri
- "üç dil build mimarisi" (07-30 → 08-02 metinleri) → **yerini aldı: 2026-08-03, K2-f — "üç REGISTER + kenar-başına biçim"**.

## Bağlantılar
[[sozluk]] · [[adversarial-hayatta-kalma]] (S-hükümlerini eleyen hakem hattı) · [[pointer-sistemi]]

**Bağlantılar:** · [[ai2ai-rapor-formati]] (karşı-link 08-22) · [[baglam-veri-ambari]] (karşı-link 08-22) · [[ajan-metodolojisi]] (karşı-link 09-03)
