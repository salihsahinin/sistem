# Pointer Sistemi

**Tanım:** Proje/karar listeleri "kısa özet + detay dosyasının adresi" formatında tutulur; detay hiçbir zaman sıcak bağlamda taşınmaz — karar anında pointer izlenir, dosya okunur, karar öyle alınır (m.20).
**Durum:** GÜNCEL · **Son teyit:** 2026-07-12 · **Kaynaklar:** tüzük m.20-22 (Salih imzalı, 07-11) + dış doğrulama: resmi skill "progressive disclosure" ilkesi birebir aynı (K-013 raporu) · **Güven:** YÜKSEK (imzalı + bağımsız dış doğrulama)

## Çekirdek
Sıcak bağlam (CLAUDE.md, kapsül, pano) sınırlı ve pahalıdır; her oturum onu baştan okur. Detayı sıcağa koymak hem token yakar hem dikkat dağıtır; detayı tamamen atmak ise bilgi kaybıdır. Pointer üçüncü yoldur: özet her zaman görünür, detay adresiyle bir adım uzakta.

**Kanonik örnek (damıtılmış):** CLAUDE.md'de tüzüğün 33 maddesi taşınmaz; tek satır taşınır — "kural kaynağı: `core/tuzuk-v0.md` (33 madde + 2 dipnot)". PAT kararı alınırken (07-12) yalnız bu pointer izlendi, dosyanın ilgili maddesi okundu, karar öyle verildi — 33 madde sıcak bağlama hiç girmedi.

## SOP — yeni bilgi yerleştirirken
1. Detayı ayrı dosyaya yaz (ya da mevcut dosyada bölüm aç).
2. Sıcak yüzeye 1 satır özet + adres koy (m.29: varsayılan 1 satır, en çok 3 cümle).
3. Özeti kısaltman gerekirse pointer'ı ASLA düşürme (m.21: dönüş yolu).
4. Karar anında: pointer izle → dosyayı oku → öyle karar ver. Özetten karar verme.
5. Bilgi bayatlarsa: silme, arşive indir; pointer'ı arşiv adresine güncelle (m.22).

## Gotchas
- **Pointer'sız kısaltma = dönüş yolu kaybı** — özet kısalırken adres düşerse detay fiilen kaybolur.
- **Bayat pointer:** dosya taşınır/ad değişirse zincir kırılır → isim disiplini sözleşmesi (V24: Salih ad değiştirmez, değiştirirse bildirir; Carvis zinciri onarır).
- **Özetten karar verme eğilimi:** pointer izlemenin maliyetinden kaçınmak yanlış karara mal olur — kural "izle, oku, karar ver"; bu adım atlanmaz.
- **Mount/senkron tuzağı (07-12 canlı vaka):** aynı dosyanın iki görünümü (Windows/sandbox) farklı olabilir — yazım sonrası doğrulama commit'ten önce yapılır.

## Süpersede zinciri
— (ilk sürüm)

## Bağlantılar
[[token-x-zaman]] (m.21 bağlam-detay ölçekleme aynı parametrelerle) · katmanlı yerleşim: tüzük m.22 · dosya-açıklama standardı: m.29

*Karşı-link (08-16):* [[baglam-veri-ambari]] — ambar sorgulanır, prompta dökülmez; brife pointer gider (aynı ilke).

**Bağlantılar:** · [[adversarial-hayatta-kalma]] (karşı-link 08-22) · [[ai2ai-rapor-formati]] (karşı-link 08-22) · [[gorsel-artefakt-dogrulama]] (karşı-link 08-22) · [[ingest-semasi]] (karşı-link 08-22) · [[kokenler-karpathy-llm-wiki]] (karşı-link 08-22) · [[olcum-banki]] (karşı-link 08-22) · [[paralel-oturum-protokolu]] (karşı-link 08-22) · [[silver-saglik]] (karşı-link 08-22) · [[uc-register]] (karşı-link 08-22) · [[tarama-yontemleri]] (karşı-link 08-22) · [[dil-secimi]] (karşı-link 08-26) · [[anakronizm-freni]] (karşı-link 08-26) · [[kolon-katmani]] (karşı-link 08-29) · [[baglam-anahtar-kaydi]] (karşı-link 08-29) · [[ajan-metodolojisi]] (karşı-link 09-03)
