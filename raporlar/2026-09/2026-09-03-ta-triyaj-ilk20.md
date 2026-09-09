# T-A-ÖNELEME katmanlı triyaj — ilk 20

**AS-OF 2026-09-03 · üreten:** `tools/ta-triyaj.py` (deterministik, LLM YOK) · **kaynak:** `veri/baglam.sqlite::silver_karantina_aday`, kosum_id `f87c65cca4`, snapshot 2026-09-03, head `e400956` (bkz. `veri/silver-saglik.jsonl` aynı kosum_id) · **karar kaynağı:** Karar 83 B3 (a), `kuyruk/senaryo-defteri.md:195` — "T-A 500 çift → KATMANLI TRİYAJ usulü: deterministik ön-sınıflandırma + şiddet-sıralı ilk ~20 sonraki masaya".

## Girdi

T-A-ÖNELEME testi (`tools/silver-saglik.py::t_a`) bu koşumda **500/500** aday çift üretti (max_cift_kayit tavanı; testin toplam ihlal sayısı 6.985 — üretilen tüm eşleşme sayısı, 500 yalnız yazılan alt-küme). `veri/silver-saglik.jsonl`'deki `ornek` alanı yalnız ilk 10'u taşır (`Sonuclar.ekle`: `list(ornek)[:10]`); 500 çiftin tamamı için tek kaynak `silver_karantina_aday` tablosudur — bu araç oradan okudu.

Kodun kendisi (t_a()) çiftleri zaten şu şekilde eler: aynı-dosya çifti YOK (da==db atlanır), varsayılan `ayni_blok_turu=True` ile blok türü farklıysa YOK. Gruplama anahtar_terim bazlı yapıldığından ("aynı anahtar terimi taşıyan kayıtlar" grubu içinde ikili kombinasyon) **"çapraz-anahtar" sınıfı bu veri kümesinde hiç oluşmuyor** — tüm 500 çift zaten aynı-anahtar-terim ∧ çapraz-dosya ∧ aynı-blok-türü.

## Ön-sınıflandırma

Görev emrindeki "aynı-dosya/aynı-anahtar" vb. örnekler bu veri kümesinde ayırt edici değil (yukarıdaki eleme yüzünden). Bunun yerine dosya yolunun **ilk dizin bileşenine** bakan deterministik kural kullanıldı:
- `ayni-ust-klasor` — iki kayıt aynı üst dizin altında (ör. ikisi de `.claude/skills/...`)
- `capraz-ust-klasor` — farklı üst dizin (ör. `core/...` vs `.claude/skills/...`)

500 çiftin dağılımı: ayni-ust-klasor **210**, capraz-ust-klasor **290**.

## Şiddet formülü

`silver_karantina_aday` tablosu zaten `uzunluk_a`/`uzunluk_b` (kaydın karakter uzunluğu) taşıyor — yeniden hesaplanmadı, hazır alan kullanıldı (m. "hazırı temel al").

```
tekrar_sayisi(anahtar_terim) = bu 500-çiftlik kümede aynı anahtar_terimi taşıyan çift sayısı
uzunluk_toplam              = uzunluk_a + uzunluk_b
siddet                      = uzunluk_toplam × tekrar_sayisi
```

**İki alternatif denendi, SEÇİLEN ikincisi:**

| Alternatif | Formül | Neden elendi / seçildi |
|---|---|---|
| (a) uzunluk-farkı | `\|uzunluk_a−uzunluk_b\| × tekrar_sayisi` | ELENDİ — iki kaydı neredeyse eş boyuttaki (tam kopya riski en yüksek) çiftleri EN ALTA iter; istenenin tersi bir sıralama |
| (b) uzunluk-toplamı **[SEÇİLEN]** | `(uzunluk_a+uzunluk_b) × tekrar_sayisi` | "ne kadar metin taşınıyor" sorusuna cevap verir, eş-boy kopyaları cezalandırmaz |

`tekrar_sayisi` yalnız yazılan 500-çiftlik alt-küme üzerinden sayılıyor (gerçek DB-geneli grup büyüklüğü değil) — 500 sınırı kırparsa hafif eksik kalabilir, deneysel damga (m.29).

**Bu formül seçimi kesin hüküm değildir — nihai onay Fable/Salih'e bırakılır** (m.40 eki). Script'te tek yerde (`triyaj()` fonksiyonu) değiştirilebilir.

## İlk 20 (şiddet-sıralı)

| sıra | sınıf | şiddet | anahtar_terim | dosya A ↔ dosya B |
|---|---|---:|---|---|
| 1 | ayni-ust-klasor | 1.665.074 | ana-sira | core/baglam-anahtar-kaydi.md ↔ core/sablonlar/gorev-fonksiyonu.md |
| 2 | ayni-ust-klasor | 1.482.886 | ana-sira | core/baglam-anahtar-kaydi.md ↔ core/skill-tetikleme-semasi.md |
| 3 | ayni-ust-klasor | 956.544 | atlas | core/durum-kapsulu.md ↔ core/tuzuk-v0.md |
| 4 | capraz-ust-klasor | 937.365 | celiski | .claude/skills/atlas-kosum/SKILL.md ↔ core/tuzuk-v0.md |
| 5 | ayni-ust-klasor | 896.768 | atlas | core/ajan-metodolojisi.md ↔ core/tuzuk-v0.md |
| 6 | capraz-ust-klasor | 885.247 | celiski | .claude/skills/atlas-kosum/SKILL.md ↔ core/tuzuk-v0.md |
| 7 | ayni-ust-klasor | 870.784 | atlas | core/halusinasyon-paketi.md ↔ core/tuzuk-v0.md |
| 8 | capraz-ust-klasor | 867.456 | atlas | .claude/skills/karar-hatti/SKILL.md ↔ core/tuzuk-v0.md |
| 9 | capraz-ust-klasor | 867.072 | atlas | .claude/skills/pipeline-kosum/SKILL.md ↔ core/tuzuk-v0.md |
| 10 | ayni-ust-klasor | 864.000 | atlas | core/ajan-metodolojisi.md ↔ core/tuzuk-v0.md |
| 11 | capraz-ust-klasor | 863.104 | atlas | .claude/skills/seans-acilis/SKILL.md ↔ core/tuzuk-v0.md |
| 12 | capraz-ust-klasor | 861.824 | atlas | .claude/skills/karar-hatti/SKILL.md ↔ core/tuzuk-v0.md |
| 13 | capraz-ust-klasor | 855.808 | atlas | .claude/skills/karar-hatti/SKILL.md ↔ core/tuzuk-v0.md |
| 14 | capraz-ust-klasor | 854.528 | atlas | .claude/skills/seans-acilis/SKILL.md ↔ core/tuzuk-v0.md |
| 15 | ayni-ust-klasor | 851.712 | atlas | core/durum-kapsulu.md ↔ core/tuzuk-v0.md |
| 16 | capraz-ust-klasor | 847.232 | atlas | .claude/skills/karar-modeli/SKILL.md ↔ core/tuzuk-v0.md |
| 17 | capraz-ust-klasor | 844.160 | atlas | .claude/skills/karar-hatti/SKILL.md ↔ core/tuzuk-v0.md |
| 18 | capraz-ust-klasor | 839.960 | celiski | .claude/skills/celiski-kapisi/SKILL.md ↔ core/tuzuk-v0.md |
| 19 | capraz-ust-klasor | 812.636 | celiski | .claude/skills/celiski-kapisi/SKILL.md ↔ core/tuzuk-v0.md |
| 20 | capraz-ust-klasor | 774.180 | celiski | .claude/skills/celiski-kapisi/SKILL.md ↔ core/tuzuk-v0.md |

**Genel görünüm:** `core/tuzuk-v0.md` ilk-20'nin 15'inde B tarafı — beklenir, tüzük uzun ve çok anahtar-terim taşıyan bir dosya, uzunluk_toplam'ı otomatik yükseltiyor. `ana-sira`/`atlas`/`celiski` anahtar terimleri baskın (yüksek tekrar_sayisi). İlk 20 içinde ayni-ust-klasor 5, capraz-ust-klasor 15 — 500'lük genel dağılıma (210/290) göre capraz-ust-klasor ağırlıklı çıktı, çünkü çapraz-üst-klasor çiftlerinin çoğu `core/tuzuk-v0.md` gibi büyük dosyalarla eşleşiyor.

**Not:** Bu liste ÖNELEME KARARI değildir — hangi çiftlerin gerçekten anlamsal çakışma/tekrar olduğu ayrı, LLM'li bir adımdır (görev emrinde de "LLM koşumu ayrı tetik" diye belirtilmiş). Bu triyaj yalnız masaya getirilecek 20 adayı seçer.

## Kaynak
- `tools/ta-triyaj.py` (script, formül ve sınıflandırma kuralları docstring'de)
- `tools/testler/test_ta_triyaj.py` (5/5 yeşil)
- `veri/baglam.sqlite::silver_karantina_aday` (kosum_id f87c65cca4)
