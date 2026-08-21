# EK-6 Triyaj + Süpersede Çapraz-Okuma (KB-23/24 icrası)

*Künye: 2026-08-20 seans-11 · emir: masa Karar 36 (KB-23 → A ön-triyaj · KB-24 → A teyit-önce) · koşucu: 1 Explore işçi (Sonnet, düşük-orta effort; 125,4k token · 21 araç · 6,8 dk) · derleme + doğrulama: Carvis/Fable. Nokta kontrol: 4 kanıt pointer'ı doğrulandı 4/4 PASS (`skill-tetikleme-semasi.md:27` tetik_kosulu · `ajan-metodolojisi.md:35` rejim-etiketi · `masa-gundemi-2026-07-30.md:549/553/558` · `2026-08-01-ingest-grafhatti.md:167` n=23 icat-rakam kaydı). Etiketler ÖNERİDİR — hüküm Salih'te. Deneysel m.29.*

**Külliyat şerhi (hakem kaydı, taşındı):** EK-6 F2 denetiminde 34 iddianın 3'ü TUTMADI (~%9) + 1 icat-rakam ("n=23 hüküm") yakalandı — kalemler denetimli okunur, kör imza yok.

## 1. Süpersede çapraz-okuması (KB-24: 08-15 tetikleme şeması ↔ 4 eski kalem)

| Kalem | Kaynak | Hüküm önerisi | Kanıt |
|---|---|---|---|
| **K2-d** tetik (D8) alanı | `kuyruk/masa-gundemi-K2-2026-08-02.md:27` | **SÜPERSEDE — kapat** | `core/skill-tetikleme-semasi.md:27` alan #2 `tetik_kosulu` (K2, m.38 boolean, boş bırakılamaz, Kapı-Ö bloke eder) talebi birebir karşılıyor; K2-d'nin "g23 Ç1 ile birleştir" hükmü fiilen bu alanda gerçekleşmiş |
| **g23** loop-desen K1-a..l | `kuyruk/masa-gundemi-2026-07-30.md:553-557` | **KISMEN** | Kapsanan: iç-içe derinlik tavanı (≤2) + zincir-uzunluk kaydı (`skill-tetikleme-semasi.md:10,34,53` alan #9 `sira`). Açık kalan: tekrar-BİRİMİ tanımı · m.43'e TETİK ayağı · m.40b-loop kaydı (loop-TESPİT mekanizması) — şema çağrı sözleşmesi, loop dedektörü değil |
| **g22** bellek/RAM B1-B5 | `kuyruk/masa-gundemi-2026-07-30.md:549-552` | **KAPSAMIYOR — canlı** | Hiçbir 08-15 şeması sistem-kaynağı/RAM izlemeye değinmiyor; konu donanım işletimi (bellek kapısı, GB ekseni, izleme rutini, donanım eşiği, kalibrasyon) |
| **g24** rejim-etiketi tetiği (K1-24) | `kuyruk/masa-gundemi-2026-07-30.md:558-564` | **KAPSAMIYOR — canlı; KB-27 kesişimi** | Rejim-etiketi TANIMI `core/ajan-metodolojisi.md:35`'te var ama K1-24'ün asıl konusu (CC-oran matrisi/hedef-metni seçimi + K1-24-l "K-009'dan önce oku") hiçbir şemada yok. **Dikkat:** rejim-etiketi parçası masadaki KB-27 C seçeneğiyle kesişiyor — KB-27 imzalanırsa bu parça oraya bağlanır |

## 2. EK-6 külliyatı triyajı (KB-23: 9 küme; kaynak `raporlar/2026-08-01-ingest-grafhatti.md` §2.3)

| # | Küme | ~Kalem | Etiket önerisi | Gerekçe/halef |
|---|---|---|---|---|
| ④ | deterministik çağrı-kapısı | 1 birleşik / 8 kaynak | **SÜPERSEDE — kapat (en net)** | `core/skill-tetikleme-semasi.md` bütünüyle (Kapı-Ö/S/K) bu talebin formalize hali |
| ③ | bütçe-fren mekaniği | ~3 | **SÜPERSEDE — kapat** | `core/ajan-metodolojisi.md:19,35` (bütçe alanı · maliyet-tavanı · rejim etiketi); kalıntısı varsa KB-27 paketine akar |
| ⑥ | m.40b koşum-deseni | ~2 | **SÜPERSEDE — kapat** | Eski "0/8 tam-sağlam" bulgusu 08-15/08-18 serisince (12 koşum) çok daha büyük örneklemle güncellendi; hüküm zemini artık KB-25 K2-l |
| ⑦ | K-019 damıtma/sabit-önek | ~3 | **SÜPERSEDE — kapat** | `core/world-model-tasarimi.md:51,68` (kararlı-önek+delta) + ingest v2 massetmiş |
| ② | AI2AI/devir-arayüzü | ~8 | **KISMEN — kalıntı listesi** | md.38 rapor-dili paketi (08-01) fiilen kanonlaştırdı; skill-çağrı alt-kümesi şemada; kalıntı: format şablonlaşmasının şablon-dosyası düzeyi |
| ⑤ | ölçüm-bankı/rejim-etiketi | ~20 ham satır | **KISMEN — kalıntı listesi** | Rejim-etiketi süpersede; ölçüm-bankı yarısı DE-katmanı GOLD ile kısmen örtüşüyor ama `kuyruk/olcum-banki.md` ayrı canlı — birleştirme kararı gerekir |
| ⑧ | m.25 eşiği (V47 formu) | ~2 | **CANLI — masaya** | "m.25 eşiğinin pipeline sınıfı için V47 formunda yazılması" hiçbir halefte yok; K0-Y3 yakın ama aynı değil |
| ① | pipeline/loop kanonu | ~4 | **[?] belirsiz** | ajan-metodolojisi + ingest-şeması kısmen absorbe etmiş görünüyor; tam eşleşme teyitsiz — kapanış ancak kalem-kalem bakışla |
| ⑨ | diğer (tekil) | ~95 | **heterojen — tek hüküm verilemez** | 11 rapordan dağınık; küme-içi CANLI/BAYAT karışık; ya kendi tekil triyaj turu (ayrı koşum) ya tarih-damgalı DONDUR |

## 3. Salih'e hüküm soruları (masa kalemi; açıklama blokları seans kaydında)

1. **S1 — Süpersede kapanışları:** K2-d + kümeler ③④⑥⑦ kapansın mı? (Kanıt tablodaki halef dosyalar; kapanış = arşiv damgası, silme yok.)
2. **S2 — ⑨ "diğer" (~95 kalem):** (a) tekil triyaj koşumu (1-2 işçi, kalem-kalem CANLI/BAYAT listesi) · (b) tarih-damgalı DONDUR (tetik yazılı) · (c) EK-6 masasında ham açılır.
3. **S3 — Canlı kalanların adresi:** g22 (bellek/RAM) + g24 (CC-oran; rejim parçası KB-27'ye) + ⑧ (m.25/V47) + g23 açık parçaları + ②⑤ kalıntıları → daraltılmış EK-6 masa-hazırlık dosyasına mı, mevcut kalemlere mi dağıtılır (g24→KB-27, ⑤→ölçüm-bankı kartı)?

*Üretim izi: işçi dönüşü bu dosyaya Carvis derlemesiyle indi; ham dönüş oturum kaydında. KB-23/24 jsonl güncel.*

## 4. HÜKÜMLER (Salih, 2026-08-20 seans-11 — defter Karar 41)

- **S1 → A:** K2-d + kümeler ③④⑥⑦ KAPANDI (arşiv damgası, halef kanıtları §1-2 tablolarında; silme yok). **Ek şart (Salih):** düşük-öncelikli borç — ilerde "yanlışlıkla kapanmış kalem var mı" kontrolü yapılacak (külliyat %9 hata şerhi gerekçesiyle).
- **S2 → DONDUR-tetikli:** ⑨ "diğer" (~95 tekil kalem) tarih-damgalı DONDUR; **tetik (Salih, aynen): "Kalemleri açacağız ama mevcut önemli karar borçları bitince."** Yan emir: karar-borçlarının optimize sıralanması ihtiyacı → fikir-kutusu adayı.
- **S3 → A (optimize dağıt):** g24-rejim parçası → KB-27 m.46(d) imzasıyla kapandı · ⑤ ölçüm-bankı kalıntısı → ölçüm-bankı hattı (birleştirme sorusu daraltılmış masada) · kalan canlılar → `kuyruk/masa-gundemi-EK6-2026-08-20.md` (~106 kalemden ~9 kaleme indi).
