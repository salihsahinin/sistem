# DEVİR — galeri-sıralama yaprak-doluluk oturumu → Fable

*Yazan: Carvis (Opus-5), ana-sıra Claude Code masaüstü. Oturum: 2026-08-31 15:4x → 2026-09-02 09:5x (makine yeniden başlatması oturumu böldü). Yetki: karar ALMADI (kanon), Katman-1'e dokunmadı. AS-OF: 2026-09-02.*

**Hat:** jarvis-dışı iş şeridi (m.15 / md.49 — Otonet galeri-scoring).
**Kritik:** `kuyruk/galeri-siralama/` **COMMIT'LENMEZ** (Karar 73 EK, `.gitignore:39`). Bu oturumun bütün kodu ve çıktısı orada; commit'e giren yalnız teslim raporu + kapsül + bu devir.
**Teslim raporu:** `raporlar/seans-teslim-2026-09-02-galeri-yaprak-doluluk.md`
**Ekip notu (klasör içi, kalıcı kayıt):** `kuyruk/galeri-siralama/bulgular-model-eksikleri.md` §16 (sözlük/önem) + **§17 (yaprak doluluğu — asıl bulgu)**

---

## 1. ÖZET — ne bitti, ne kaldı

| Birim | Durum | Çıktı |
|---|---|---|
| `05_agac_html.py` sürüm-bağımsızlaştırma | **TAMAM** | `--model/--veri/--lot` bayrakları; bölme 03 ile ortak |
| Sözlük sekmesi önem sıralaması | **TAMAM** | önem çubuğu + bölme sayısı + aile içi sıra |
| Yaprak doluluk teşhisi | **TAMAM** | `13_yaprak_doluluk.py`; yapısal ↔ seyrek ayrımı |
| 4× mock veri çoğaltma | **TAMAM** | `14_veri_birlestir.py` → 1.611.460 satır |
| Yoğun eğitim + derinlik araması | **TAMAM** | `15_egit_yogun.py`; d6/d5/d4/d3, %61,4 → %96,25 |
| Yeni test datasıyla HTML | **TAMAM** | `agac-semasi-model_yogun_d3-veri2u_s77.html` (açıldı) |
| **Yeni trim deneyi (Salih'in 2. emri)** | **YARIM — KOŞULMADI** | betikler hazır, koşum kesildi |

---

## 2. YARIM KALAN İŞ — Salih'in 2. emri (öncelik 1)

**Emrin kendisi (Salih, 08-31):** "yeni mock data olarak eğitim amaçlı trim listesi oluştur — hiç teklif verilmemiş, galerilerin hiç görmemiş olduğu trimler olsun. Bu yeni trim listesi için aynı galeriler nasıl sıralanıyor, model yeni trimler için galerileri sıralarken o araçla ilgili hangi feature'lar ne kadar korelasyona sahip, önem sırasını gözlemlememiz lazım. Bu korelasyona bağlı olarak örneğin hep Fiat Egea alan bir galerinin Egea dışında hiç alım datası olmasa dahi hangi trimlere hangi metriklere göre sıralandığını anlamamız lazım."

**Durum:** iki betik YAZILDI ama HİÇ KOŞULMADI (makine yeniden başladı, `/tmp/trim.log` ve çıktı JSON'u yok).

**Koşum reçetesi (tek blok):**

```bash
cd ~/jarvis/kuyruk/galeri-siralama
../ders-gbm/.venv/bin/python 16_yeni_trim.py --model model_yogun_d3.cbm --veri veri2u_s77
../ders-gbm/.venv/bin/python 17_yeni_trim_html.py
open yeni-trim.html
```

**`16_yeni_trim.py` ne yapıyor (yazıldı, doğrulanmadı):**
- Evrende HİÇ OLMAYAN trimler üretir, iki kohort: `yeni-trim` (marka/seri biliniyor, trim yeni) ve `yeni-marka` (hiçbiri bilinmiyor). Trim/seri/marka sayaçlarının hepsi 0'a çekilir.
- Aday havuz: `veri2u_s77` gerçek galerilerinin son snapshot'ı.
- İki bağımsız önem ölçüsü: **SHAP** (grup içi merkezlenmiş, modelin kendi hesabı) + **grup içi Spearman** (gözlemlenen ilişki). Ayrışma = etkileşim işareti.
- **Odak galeri analizi** = "hep Fiat Egea alan" karşılığı: aldığı araçların ≥%60'ı tek trimden ve ≥3 araç olan galeriler; yeni trimde nereye düştükleri + onları ilk-5'e taşıyan metriklerin etki büyüklüğü (σ cinsinden).
- Çıktı: `yeni-trim-sonuc.json` → `17_yeni_trim_html.py` 4 sekmeli `yeni-trim.html` üretir.

**Fable'a uyarı — betikler koşulmadığı için şu riskler AÇIK:**
1. `16_yeni_trim.py` içinde `son_satir` kurulurken `drop_duplicates("galeri_id", keep="last")` sonrası `reset_index()` ile `galeri_id` kolon olarak geri geliyor; `RNG.choice` ile seçilen alt küme `iloc` ile alınıyor — indeks/kolon çakışması ihtimali test edilmedi.
2. SHAP hesabı 180 lot × ~56 aday × 63 feature için bellek/süre ölçülmedi; patlarsa `--lot 60` ile küçült.
3. `_kohort` / `_odak` gibi alt-çizgili kolonlar Pool'a girmiyor (FEATURE listesi modelden geliyor) — ama doğrulanmadı.
4. Odak galeri kümesi boş çıkabilir (`veri2u_s77`'de tek-trim yoğunlaşma eşiği tutmayabilir); o durumda HTML "bulunamadı" kutusu basar — eşiği (%60 / 3 araç) gevşetmek gerekebilir.

---

## 3. ANA BULGU — yaprak doluluğu (Salih'in 1. emri, TAMAM)

**Emir:** "her yaprağa minimum 20 satır düşecek şekilde mock datalarla eğit."

**Ölçülen üç şey — hepsi §17'de tablolu:**

1. **Boş yaprakların %26,6'sı YAPISAL olarak imkânsız.** Simetrik ağaçta aynı kolon iki farklı eşikle sorulabiliyor (`x>5` ∧ `x>10`); "x≤5 ve x>10" satırı yoktur. Bu yapraklar mock data ile ASLA dolmaz. **Hedef "her yaprakta ≥20" değil "MÜMKÜN her yaprakta ≥20" olarak revize edildi.**
2. **`min_data_in_leaf` ölü parametre.** Doğrudan test: `min_data_in_leaf=20` ile ve onsuz eğitilen modeller aynı boş yaprak sayısını verdi — CatBoost bunu yalnız `Lossguide`/`Depthwise`'da uyguluyor, varsayılan `SymmetricTree`'de yok sayıyor.
3. **Asıl kaldıraç derinlik, veri değil.** 4× mock veri d6'da +13 puan; derinlik 6→3 aynı veriyle +22 puan. Kombinasyon sayısı 2^derinlik ile üstel büyüdüğü için veri katlamak bir seviyeyi telafi etmiyor.

| derinlik | yaprak/ağaç | ağaç | mümkün yaprak | ≥20 satır | HR@1 | HR@5 |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 64 | 1.723 | 103.055 | %74,65 | 0,711 | 0,971 |
| 5 | 32 | 1.940 | 58.676 | %82,93 | 0,709 | 0,970 |
| 4 | 16 | 1.335 | 20.293 | %91,74 | 0,707 | 0,968 |
| **3** | **8** | 1.999 | 15.600 | **%96,25** | 0,706 | 0,966 |

Başlangıç (tek evren, d6): %61,4. **Kalite bedeli 0,5 puan.**

---

## 4. DİSKTEKİ DURUM (hepsi commit dışı)

| ne | yol | not |
|---|---|---|
| seçilen model | `model_yogun_d3.cbm` | 1.999 ağaç × 8 yaprak |
| diğer modeller | `model_yogun_d{4,5,6}.cbm` | karşılaştırma için duruyor |
| eğitim verisi | `veri2u_kalabalik/` (807 MB) | 4 evren birleşik, 1.611.460 satır |
| test evreni | `veri2u_s77/` (326 MB) | eğitimde HİÇ görülmedi |
| ham tohum evrenleri | `veri2u_s4{3,4,5}/` (~965 MB) | türev, silinebilir |
| yüzey | `agac-semasi-model_yogun_d3-veri2u_s77.html` | 4,20 MB, 1.480 test lotu |
| özet | `yogun-egitim-ozet.json` | derinlik araması sayıları |
| yetim | `zaman-testi-model_v2u.json` | üreteni silindi; silme kararı Salih'te |

**Klasör toplamı 2,5 GB** — tamamı türev, tohum 42/43/44/45/77 ile bit-bit yeniden üretilir.

---

## 5. SİLİNENLER (Salih emriyle)

`zaman-testi.html` · `11_zaman_testi.py` · `12_zaman_html.py` — istenmeyen iş. Yanlış anlama: Salih "ağaç yüzeyini yeni modelle üret" derken zaman-ileri bozulma testi üretilmişti. README'den de çıkarıldı.

---

## 6. SALİH'E AÇIK SORULAR

1. **Derinlik 3 kalıcı mı?** Yüzeydeki yaprak tablosu artık 8 satır (önce 64). Okunabilirlik arttı ama model sığlaştı; d4 (%91,74, 16 yaprak) alternatif olarak duruyor.
2. **Derinlik 2 denensin mi?** %99'a çıkarabilir, model etkileşim öğrenemez.
3. `zaman-testi-model_v2u.json` silinsin mi?
4. 2,5 GB türev veri temizlensin mi (yeniden üretimi ~10 dk)?
5. Yeni trim deneyinin odak eşiği (%60 tek trim / ≥3 araç) doğru mu, gevşetilsin mi?

---

## 7. FABLE İÇİN İLK ÜÇ ADIM

1. `16_yeni_trim.py` + `17_yeni_trim_html.py` koş (§2'deki blok), hataları düzelt, `yeni-trim.html`'i aç ve Salih'e teslim et.
2. Sonucu ekip notuna §18 olarak yaz (SHAP ↔ Spearman tablosu + odak galeri okuması).
3. §6'daki 5 soruyu Salih'e sun (m.40 eki: seçenek başına ne demek · ne yaparım · artı · eksi · öneri).
