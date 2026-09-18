# Paralel Yapılanma Planı v2 — 2026-07-15 (Salih emri: öğrenme şeridi + yeni öncelik sırası)

> **Açıklama notu:** v1 (`paralel-yapilanma-plani-2026-07-13.md`) arşiv-değerinde kalır (m.8); bu dosya onun revizyonudur. Tetik: Salih 07-15 günaydın emri — "cowork öğrenme oturumlarım olsun · paralel yapılanmayı güncelleyelim · portrisk 3. öncelik". m.16 çelişki raporu aynı oturumda sunuldu (P1 B-kanadı + P4 ölçüm riski); Salih kararı: "önümüzdeki birkaç gün odak sadece öğrenme + Jarvis; ölçüm bankı önemli olmaya başlayınca 3. oturum olarak tasarlanır."

## Şeritler (5 yüzey; öncelik sırasıyla)
| # | Şerit | Yüzey | Açılış | İçerik | Kanon yetkisi |
|---|---|---|---|---|---|
| 1 | JARVIS vardiyası (ana sıra) | Cowork oturum A | "günaydın" | prototip: loop-eng Faz 2+4 → K-009 → K-010; **mühendislik yarısı** | TAM (kanon sahibi) |
| 2 | Öğrenme oturumları — **YENİ** | Cowork oturum Ö | "günaydın, öğrenme" | Atlas müfredatından partisyon-partisyon: 0'dan anlatım + sistem-uygulama 3-modeli; **tersine mühendislik / bağlam inşası yarısı** (protokol: `ogrenme/README.md`) | kapsülde yalnız kendi satırı + `ogrenme/` altı TAM |
| 3 | Ölçüm-bankı (PortRisk) | Cowork oturum B | "günaydın, PortRisk" | Sprint 1+ (çift mount) — **BEKLEMEDE:** Salih "artık önemli" deyince 3. oturum olarak tasarlanıp açılır (07-15 kararı) | kapsülde yalnız kendi satırı |
| 4 | Chat şeridi | Claude chat / telefon | CHAT-KAPSULU yükle | tartışma, fikir, karar-hazırlığı | SIFIR — çıktı = fikir-kutusu-adayı |
| 5 | Jarvis-DIŞI chat'ler | Claude chat | kapsülsüz | ders/sınav, gündelik | — (Jarvis bağlamı yüklenmez) |

## Değişenler (v1 → v2)
1. **Öğrenme şeridi eklendi (öncelik 2).** İkili yapı: her partisyonun "tersine mühendislik / bağlam inşası" (konuyu 0'dan sökme) yarısı + "mühendislik" (JARVIS'e uygulama, m.37 3-model sunumuyla) yarısı.
2. **PortRisk 3. önceliğe indi ve açılışı tetiğe bağlandı** ("artık önemli" — Salih beyanı). m.36c ruhu korunur: iptal değil, sıralama. **Kabul edilen risk:** P4 (Ağustos ölçüm+deney) girdisi PortRisk hasadından gelir; gecikme P4'ü iter — kritik yolda tampon yok. Sigorta: öğrenme müfredatındaki eval/ölçüm partisyonları P4 hazırlığını kısmen taşır.
3. **P1 (ilk paralel deneme) yeniden şekillendi:** JARVIS + PortRisk çifti yerine **JARVIS + öğrenme** çiftiyle yapılır; tetik = müfredat DONE (Atlas raporu `cc/rapor-2026-07-15-1.md` + damıtılmış `ogrenme/mufredat.md`). `PARALEL-VARDIYA-ILK-DENEME.md` adımları yüzey adları değişerek geçerli.

## Senkron kuralları (v1'den aynen + ekler)
1. Kapsülde her vardiya yalnız KENDİ satırını günceller; ayrı teslim raporu; push öncesi pull.
2. Aynı dosyaya iki oturum eşzamanlı yazmaz; çakışmada Şerit 1 kazanır.
3. Chat çıktıları yalnız Salih eliyle Cowork'e girer.
4. Her Cowork oturumu açılışta kapsülü okur.
5. Şerit 5 tamamen bağımsız.
6. **YENİ:** Öğrenme oturumu ders kayıtlarını `ogrenme/dersler/`e yazar; kanona (pano/kapsül) yalnız karar/fikir ADAYI taşır — uygulama kararları ana sıraya (Şerit 1) devredilir, orada m.37 kaydıyla alınır.

## DONE tanımları
- İlk paralel gün (revize) DONE: JARVIS + öğrenme vardiyaları kendi teslim raporlarını yazdı ∧ kapsül çakışmasız ∧ push'lar temiz.
- Öğrenme şeridi denemesi DONE: ilk partisyon işlendi ∧ anlama-kapısı geçildi ∧ ≥1 uygulama-model-kararı ana sıraya aday olarak düştü.
- Revizyon tetiği: herhangi bir senkron kuralı 2 kez ihlal olursa protokol masaya gelir (v1'den aynen).
