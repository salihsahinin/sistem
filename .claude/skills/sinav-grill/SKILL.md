---
name: sinav-grill
description: Salih'in bir plan/karar/öğrenilen konu üzerindeki anlayışını adversarial Sokratik sorgulamayla sınar (S-I); tek-tek sorular, karar-ağacı inişi, [S]/[O]/[T] derinlik haritası + bulanık-blok listesi üretir. Tetik; YALNIZ Salih beyanı — "sınav", "sınava çek", "grill", "sorguya çek". KULLANILMAZ; model kendi inisiyatifiyle ASLA tetiklemez (K3 hükmü 07-21; V55 pasif-okuma varsayılanı korunur — bu skill varsayılanı değiştirmez), ders anlatımında, karar üretiminde, ayıklık/ruh-hali sorgusunda (m.23/m.33 — sorgu İÇERİK hakkındadır, Salih'in durumu hakkında değil).
---

# Sınav/Grill (S-I, v1 — 2026-08-14; Pocock `grilling` deseni madenlendi — V25: kurulum yok, yeniden yazım)

Kaynak desen: `raporlar/2026-07-21-grill-me-skill-arastirma.md` (mattpocock/skills, MIT). Amaç: "okudum" ile "anladım" arasındaki ertelenmiş ölçüm boşluğunu İSTEĞE BAĞLI kapatmak.

## Adımlar
1. **Kapsamı al:** Salih neyi sınatmak istiyor (plan / karar / öğrenilen konu / yazdığı kod)? Kapsam DAR tutulur — "her şeyi sına" koşulmaz.
2. **Sorgulama döngüsü (çekirdek kurallar):**
   - **Tek seferde TEK soru;** cevabı bekle, sonra devam (çoklu soru sersemletir).
   - **Karar-ağacını dal dal in:** kararlar arası bağımlılıkları tek tek çöz; yüzeysel turlama yok.
   - **Her soruda kendi önerilen cevabını da ver** — Salih kıyaslasın.
   - **Olguyu sorma, kendin bak:** dosya/ortamdan bulunabilir bilgi soru konusu YAPILMAZ (kanondan oku); yalnız Salih'in KARARLARI ve ANLAYIŞI sorulur.
   - Sorular sertleşir ama içerik hakkında kalır; kişisel/psikolojik yorum yok (m.7/m.23).
3. **Anlama haritası (çıktı):** kapsamdaki her alt-konu derinlik etiketi alır — **[S]ağlam** (kendi cümleleriyle türetebildi) · **[O]rta** (tarif etti, türetemedi) · **[T]emelsiz** (ezber/boşluk). Ayrıca **bulanık-blok listesi**: cevaplanamayan/çelişen noktalar, tekrar-kuyruğu önerisiyle (çevrim adım-4: "yanlışı kuyruğa at, 2-3 gün sonra tekrar").
4. **Ortak-anlayış kapısı:** Salih "tamam, anlaştık" demeden bu skill'den EYLEME geçilmez (sınav sonucu otomatik iş doğurmaz; iş doğacaksa ayrı görev).

## Gotchas
- **Kendiliğinden tetiklenme:** en kritik yasak — "bunu sınayayım mı?" diye önermek bile V55 ihlaline kayar; Salih istemeden sınav yok.
- **Yumuşatma:** sorulan sorunun cevabını Salih'e fısıldama; önerilen-cevap SORUDAN SONRA, Salih cevapladıktan sonra kıyas için açılabilir de (Salih tercihine göre).
- **Derece-şişirmesi:** [S] etiketi "türetebildi" kanıtı ister, "doğru kelimeyi söyledi" değil.
- **Kapsam sürünmesi:** sınav ortasında yeni konu açılırsa yeni tur olarak notlanır, mevcut tur bitirilir.
- Skill kaydetme/commit yapmaz; derinlik haritası rapor olarak döner, kayıt vardiya akışının işidir (yan-etki freni).
