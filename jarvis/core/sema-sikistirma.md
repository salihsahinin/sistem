# Şema-Sıkıştırma v1 — şişen bağlamı şemalaştırarak compact etme · aktif: Salih emri 2026-08-15 (Hat-4)

*Salih sezgisi: "şemalaştırmak (graf) bağlam şişmesi için optimizasyon yöntemi — en iyi nasıl yapılır, matematiksel formülize et, hangi bağlamlar uygun." Kanıt: `cc/rapor/2026-08/rapor-2026-08-15-4.md` (m.40b: 3 aile × tez→antitez→V26→hakem, 12 işçi; 15 `SAĞLAM` · 49 `DARALDI` · 2 `DÜŞTÜ`; V26 6/6). Uygulama: `damitma` skill'ine **şema-dalı** (ayrı skill **açılmadı** — kapı-ağacı K0: kapsanmış → **evrim**(damitma); kutu satırı güncel). Graf (D2): `core/sema-sikistirma.d2` → `raporlar/2026-08/2026-08-15-sema-sikistirma.svg`. **Dürüstlük:** Salih'in istediği "oran × kayıp × sorgu-uyumu" **çarpımsal** tek-skaler biçimini literatür **desteklemiyor** (iki bağımsız kör-nokta bulgusu) — matematik = **mdl** iki-parçalı eşitsizlik (kabul çekirdeği) + koşullu karar tablosu; Jarvis defteri (~40-50k token) literatürün **ölçülmemiş** bandında (26k-115k); Türkçe + karar/kural kanonu + akıl-yürütme izi sıkıştırması hiç ölçülmemiş → tüm eşikler deneysel m.29, kendi korpusumuzda kalibre.*

## 0. Beş ilke (kanıttan)
1. **Birim = atomik olgu/gözlem, serbest özet değil.** Özet-birimi en yüksek recall'la en düşük F1'i verir (recall ≠ doğruluk); olgu-satırı + kaynak-pointer; olgu **ham** kaydın **üstüne** ek katmandır — "olguyu tut, hamı at" varsayılamaz (değiştirme çoğu kategoride zarar; m.20/m.8 ile birebir). [A-YT1, A-YT6]
2. **Sorgu-uyumu belirleyici; oran tek başına anlamsız.** Aynı ~4× oranda soru-farkında seçim +11-17 puan, soru-bağımsız −25-45; kayıp = f(sorgu-dağılımı, konum/gürültü, oran) — **koşullu**, çarpımsal değil. Damıtmada "neyi tutuyoruz" sorusu sorgu-dağılımıyla (kapsül/pano/defter hangi soruları cevaplıyor) cevaplanır. [A-YT2]
3. **Şemalaştırma tetiği = bağlam/pencere oranı + maliyet, doğruluk değil.** Pencereye rahat sığan bağlamda (≤~26k) şema doğruluk **kazandırmaz** (tam-bağlam tavan; sıkıştırma vergisi ~4-6 puan ↔ %73 token / %91 gecikme tasarrufu); ≥~115k'da tam-bağlam kendisi −%30 bozulur → şema kazanır (Zep 115k→1,6k, +%15-18). İstisna: çeliştirici/negatif sorgular (tam bağlam halüsine eder 15,7 vs 80,0). Graf katmanı ∃-kategori kararıdır (entegrasyon/temporal/çapraz-oturum +, tek-kayıt erişim ve bilgi-GÜNCELLEME −) — ∀-katman değil; olgu-listesi üstüne opsiyonel. [A-YT4, A-YT5, A2-2]
4. **Çıkar + doğrula + bedel-defteri.** Şema arızasının ~%76'sı çıkarım katmanında; ham LLM üçlü-çıkarımı %65,2 özne-halüsinasyonu → hibrit doğrulama (regex + yargıç + kaynak-satıra geri-eşleme) %1,6 [K, vekil-metrik]. Niteleyici **erozyonu** ölçülü: aşırı-genelleme OR 4,85, tekrarlı turda birikir (%20→%40 / 5 tur) → niteleyici/kapsam/kesinlik alanı **zorunlu** (md.20'nin ölçülmüş hâli), damıtma **tur sayısı** sınırlı (kapsül üstüne-yazılır ama kaynak = kuyruk+defter+git — tek sigorta bu). Muhasebe **çift**: sorgu-anı token ↔ ingest/depo token ayrı raporlanır; tek sayı yasak. [A-YT7, C-YT6, A-YT3]
5. **Ucuz-katman-önce, beyanla yüksel; ölçüm kendi korpusunda.** Önce şema/özet katmanı; "cevaplanamaz" beyanında ham/tam bağlama yüksel (token −%39-61, doğruluk ±2 bandı) = m.20 pointer-inişinin ölçülmüş biçimi. gzip-oranı proxy'si yalnız <32KB parçada meşru; sıkıştırılabilirlik ölçümü karıştırılmış kopyadan; alan-dışı kalibrasyonsuz sıkıştırma −20 puan sınıfı kayıp. [A-YT8, B-YT7, B-YT6]

## 1. Matematik (formül — beyan edilmiş biçimiyle)
**Kabul çekirdeği (mdl iki-parçalı; birim beyan edilir — token):**
`L(şema) + Σᵢ L(kayıtᵢ | şema) + L(düzeltmeler) < Σᵢ L(kayıtᵢ)` ⇒ şema kurulur.
- Düzeltme listesi ana bedel kalemidir (grafikte temsilin %70-80'i düzeltme) — ingest v2'deki **dlq** + serbest-alan tam bu terim; **dlq** oranı ↑ ⇒ şema-uyumu ↓ ⇒ kazanç erir.
- Kayıt-birleştirme eşiği: s = (c_u + c_v − c_birleşik)/(c_u + c_v) > 0 ise birleştir; tek adım ≤2×, büyük kazanç zincirleme; **geri-alınabilirlik bizim tercihimizle açık** (m.8: silme yok — faydası düşen yapı arşive iner, pointer kalır).
**Karar tablosu (tek skaler `YOK`; koşullu):** `karar = f(L_bağlam/pencere, sorgu-sınıfı, düzenlilik, güncelleme-yoğunluğu)` — §2.
**Uygunluk skoru U (kayıt-sınıfı başına; deneysel m.29 — kayıt-seviyesi skor literatürde `YOK`, bu bizim deneyimiz):**
Bileşenler: düzenlilik (sabit-alanlı/şablonlu) · tekrar (aynı tip ≥ N kayıt) · entegrasyon-sorgusu (kayıtlar-arası sorular) · güncelleme-yoğunluğu (sık GEÇERSİZ-KIL/UPDATE) · niteleyici-yoğunluğu (şerh/koşul/derece) · anlatı (akıl-yürütme izi). **Skor, MDL kabulü, birleştirme eşiği, yol eşikleri (≥2 / 0-1 / <0) ve 3 tur sınırı kanonik olarak `lean/Kanon/SemaSikistirma.lean`** (Karar 114, 2026-10-16; özgün formül git `2cfa2da`).

## 2. Karar tablosu (bağlam-sınıfı → yol; jarvis eşlemesi)
| bağlam sınıfı | örnek | karar | gerekçe |
|---|---|---|---|
| sabit-alanlı karar/olay kayıtları | defter karar blokları · kutu satırları · koşum tabloları | **ŞEMALA** (kapalı-tip + zarf; tablo/SQL görünümü) — zaten ingest v2 bunu yapıyor; şema-dalı: FLAG'li dosyada olgu-satırlarına indir + `veri/baglam.sqlite` görünümü (seans-3 V-1 hattını **kullan**, yeniden kurma) | U≥2; log-parsing %81-91 (ama ≥5-parametreli/nadir kayıtlar ayrı kova — karar/istisna kayıtları **özel** doğrulama) |
| tekrarlı prosedür/ritüel | skill adımları · checklist | **şemala** (zaten skill/şablon) | Sequitur/AWM: tekrar → kural |
| envanter/durum | pano kartları · hazine listesi · kapsül "şu an" | **olgu-satırı** (snapshot; tarihçe git'te) | kapsül=`SNAPSHOT` ilkesi |
| çapraz-kayıt ilişki soruları | "hangi karar hangi maddeyi değiştirdi" | **graf** (opsiyonel katman; olgu-listesi **üstüne**; [[wiki-link]] + anahtar-kaydı `replaced_by` zaten kenar) | entegrasyon +%21 (2Wiki) ama tek-kayıt −; ∃-kategori |
| niteleyici-yoğun hüküm | tüzük maddeleri · şerhler | **HAM tut** + pointer; şemaya yalnız **indeks** (madde-no → başlık) | niteleyici erozyonu OR 4,85; md.20 |
| akıl-yürütme izi / anlatı | rapor gövdeleri · tartışma | **ham** (arşiv) + olgu-satırlı özüt (hasat); özüt gövdeden türetilir | ölçülmemiş sınıf; en riskli; tur-sınırı 1 |
| sık-güncellenen bilgi | açık borçlar · Salih-karar listesi | **olgu-satırı** + bi-temporal damga (gecerli-baslangic/bitis); graf **değil** | Zep bilgi-güncelleme −%3,4 (şemanın en zayıf kategorisi) |

## 3. Damıtma şema-dalı (uygulama — `damitma` skill'ine eklendi)
FLAG'li dosyada, triyajdan önce: (i) kayıt-sınıflarını ayır (yukarıdaki tablo); (ii) sınıf-başına U hesapla; (iii) ŞEMALA-sınıfında olgu-satırlarına indir (atomik olgu + kaynak-pointer + niteleyici alanı + bi-temporal damga), **çıkarımı doğrula** (her olgu-satırı → kaynak satırına geri-eşle; eşleşmeyen `DAYANAKSIZ` → kaynaklanır ya da düşer — halüsinasyon paketi F1); (iv) HAM-sınıfını arşive pointer'la; (v) ölçüm satırı: dosya · sınıf-başına kayıt sayısı · önce/sonra token (çift muhasebe) · **dlq** oranı · tur numarası (≥3 turda dur — erozyon birikimi). Yükselme kuralı okuma tarafında: şema katmanı "cevaplanamaz" derse ham arşive in (m.20).

## 4. m.16 taraması + şerh-adayları + ölçüm borcu
- Çelişki `YOK` — m.20/m.22/ingest-v2/damitma bu şemanın önceden-var parçaları; kanıt jarvis tasarımını 3 noktada **doğruladı** (pointer-inişi = ölçülmüş "ucuz-önce"; kapsül=`SNAPSHOT` + git-kaynak = compaction-sürüklenmesi sigortası; ingest kapalı-tip = **mdl** düzeltme-terimi yönetimi).
- **Şerh — `İMZALANDI` (Salih 08-17 masa KB-17c):** "damıtma ~%50 hedefi" orana değil **sorgu-uyumuna** bağlı (F2 bulgusu; damitma skill'i adım 4); kapsül üstüne-yazma turlarına erozyon-sayacı (teslim raporuna). İlk uygulama: 08-17 defter damıtması (kararlar+pointer korundu; oran 180,9→42,7 KB sonuçtu).
- **Ölçüm borcu:** Jarvis bandı (26-115k) ölçülmemiş · Türkçe BPE etkisi · karar-kanonu sınıfı · U skorunun kalibrasyonu (ilk 5 damıtma koşumunda sınıf-başına önce/sonra + DRFR); Hat-6 jarvis→DB hattı `veri/baglam.sqlite` üstünde sorgu-anı/ingest çift muhasebesini ölçebilir.

**Lean eki (Karar 117, 2026-10-17):** §1 formül, §2 karar tablosu ve §3 damıtma dalının kodu aşağıda yüklenir (`Kanon.SemaSikistirma`); md metni yerinde kalır, ayrışırsa kod kazanır.

@../lean/Kanon/SemaSikistirma.lean.md
