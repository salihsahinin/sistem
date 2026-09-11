# İB-81 kuru koşum — tüzük iz taraması (2026-09-11, deneysel m.29; kanona yazılmadı)

*Kaynak `core/tuzuk-v0.md` · 47 madde · 59.0 KB · üreten `tools/tuzuk-iz-tarama.py` (deterministik). İz = SÜPERSEDE / REVİZE / EK / üstü-çizili. Çelişki adayı = iki izli madde ≥3 ortak alan-terimi (durak sözcükler dışı) — v0 GÜRÜLTÜLÜ: sözcük örtüşmesi çelişki DEĞİL, yalnız okuma sırası önerir; hüküm Salih'in.*

## İzli maddeler (tek hükme inme adayları)

| m. | başlık | satır | iz | bayt | öneri |
|---|---|---|---|---|---|
| m.36 | İlk-prototip fazı kuralı | 53 | 5 | 2306 | tek hüküm + arşiv-pointer |
| m.41 | Yan-oturum karar sınırı | 67 | 3 | 4378 | tek hüküm + arşiv-pointer |
| m.14 | JARVIS node CV-repo'su değildir | 27 | 3 | 1192 | tek hüküm + arşiv-pointer |
| m.40 | Karar-sunum protokolü | 65 | 1 | 7191 | tek hüküm + arşiv-pointer |
| m.30 | Ajan kalıcılığı + atama mimarisi + fedakarlık kararı | 46 | 1 | 5054 | tek hüküm + arşiv-pointer |
| m.42 | Ajan-yetki kanunu | 69 | 1 | 2896 | tek hüküm + arşiv-pointer |
| m.43 | Skill-doğum kuralı — tekrarlayan-küme → skill adayı | 70 | 1 | 2630 | tek hüküm + arşiv-pointer |
| m.44 | Rol katmanları — köle ≠ üst-orkestratör ≠ domain-lider | 71 | 1 | 2168 | tek hüküm + arşiv-pointer |
| m.25 | Mod sistemi yok — görev-ölçek optimizasyonu var | 41 | 1 | 861 | bekle (tek iz, küçük) |

Toplam izli madde: 9 / 47 · iz toplamı: 17

## Çelişki adayı çiftler (deterministik, ortak alan-terimi ≥4)

| çift | ortak terimler |
|---|---|
| m.14 ↔ m.40 | katman-, portrisk, tetik, varsayılan, verisi, şartı |
| m.14 ↔ m.41 | katman-, okunur, senaryo-defteri, skill, terminal, şartı |
| m.25 ↔ m.30 | optimize, sistemi, varsayılan, yetkisi |
| m.30 ↔ m.36 | gereği, görevi, görevleri, karpathy, olsun, otomasyon |
| m.30 ↔ m.40 | ajanı, bedeli, düşer, fıkra, hüküm, ingest |
| m.30 ↔ m.41 | alınır, bugün, böyle, devam, devri, durur |
| m.30 ↔ m.42 | alınır, açılış, bir-altı, dahil, deterministik, effort |
| m.30 ↔ m.43 | deterministik, düşer, hattı, hattını, kaydı, kendi |
| m.30 ↔ m.44 | bir-altı, devri, durur, effort, farklı, kapsamı |
| m.36 ↔ m.40 | dönem, kalan, koşar, koşul, koşullu, paralel |
| m.36 ↔ m.41 | artık, birlikte, commit, geçerli, kalan, kaldırıldı |
| m.36 ↔ m.42 | birlikte, kazanır, listesi, sayılır, tanımı |
| m.36 ↔ m.43 | artık, olsun, paralel, revizyonu, sayılır, tutarlı |
| m.40 ↔ m.41 | açılan, başka, denetim, devir, düzeni, düşer |
| m.40 ↔ m.42 | ajanları, alternatif, beyan, bilinçli, devir, düşük |
| m.40 ↔ m.43 | arası, beyan, deneysel, doğrudan, dürüstlük, düşer |
| m.40 ↔ m.44 | atlası, daraltildi, kanon, kapsam, kaydı, koşum |
| m.41 ↔ m.42 | alınır, birlikte, devir, hafıza, lojik, maddenin |
| m.41 ↔ m.43 | artık, düşer, lojik, olsun, oturumlar, rapor- |
| m.41 ↔ m.44 | devri, durur, güçlü, kanon, kapsam, lojik |
| m.42 ↔ m.43 | beyan, birimi, deterministik, kendi, lojik, sayılır |
| m.42 ↔ m.44 | bir-altı, effort, farklı, katman, kendi, koşum |
| m.43 ↔ m.44 | alanında, ampirik, kaydı, kendi, lojik, süpersede |

## Usul
- Uygulama: madde başına tek commit `[damıtma]`; eski metin `arsiv/tuzuk-madde-arsivi-YYYY-MM-DD.md`'ye iner (m.8).
- Şeffaflık (Salih 09-10 şartı): uygulanan maddenin son 5 seansta hangi oturumda yüklendiği `hareket` tablosundan (Read + dosya=tüzük, okuma_tipi) rapora eklenir.
