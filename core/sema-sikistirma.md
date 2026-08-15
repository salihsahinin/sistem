# Şema-Sıkıştırma v1 — şişen bağlamı şemalaştırarak compact etme · AKTİF: Salih emri 2026-08-15 (Hat-4)

*Salih sezgisi: "şemalaştırmak (graf) bağlam şişmesi için optimizasyon yöntemi — en iyi nasıl yapılır, matematiksel formülize et, hangi bağlamlar uygun." Kanıt: `cc/rapor-2026-08-15-4.md` (m.40b: 3 aile × tez→antitez→V26→hakem, 12 işçi; 15 SAĞLAM · 49 DARALDI · 2 DÜŞTÜ; V26 6/6). Uygulama: `damitma` skill'ine ŞEMA-DALI (ayrı skill AÇILMADI — kapı-ağacı K0: kapsanmış → EVRİM(damitma); kutu satırı güncel). Graf (D2): `core/sema-sikistirma.d2` → `raporlar/2026-08-15-sema-sikistirma.svg`. **Dürüstlük:** Salih'in istediği "oran × kayıp × sorgu-uyumu" ÇARPIMSAL tek-skaler biçimini literatür DESTEKLEMİYOR (iki bağımsız kör-nokta bulgusu) — matematik = MDL iki-parçalı eşitsizlik (kabul çekirdeği) + koşullu karar tablosu; Jarvis defteri (~40-50k token) literatürün ÖLÇÜLMEMİŞ bandında (26k-115k); Türkçe + karar/kural kanonu + akıl-yürütme izi sıkıştırması hiç ölçülmemiş → tüm eşikler deneysel m.29, kendi korpusumuzda kalibre.*

## 0. Beş ilke (kanıttan)
1. **Birim = atomik olgu/gözlem, serbest özet değil.** Özet-birimi en yüksek recall'la en düşük F1'i verir (recall ≠ doğruluk); olgu-satırı + kaynak-pointer; olgu HAM kaydın ÜSTÜNE ek katmandır — "olguyu tut, hamı at" varsayılamaz (değiştirme çoğu kategoride zarar; m.20/m.8 ile birebir). [A-YT1, A-YT6]
2. **Sorgu-uyumu belirleyici; oran tek başına anlamsız.** Aynı ~4× oranda soru-farkında seçim +11-17 puan, soru-bağımsız −25-45; kayıp = f(sorgu-dağılımı, konum/gürültü, oran) — KOŞULLU, çarpımsal değil. Damıtmada "neyi tutuyoruz" sorusu sorgu-dağılımıyla (kapsül/pano/defter hangi soruları cevaplıyor) cevaplanır. [A-YT2]
3. **Şemalaştırma tetiği = bağlam/pencere oranı + maliyet, doğruluk değil.** Pencereye rahat sığan bağlamda (≤~26k) şema doğruluk KAZANDIRMAZ (tam-bağlam tavan; sıkıştırma vergisi ~4-6 puan ↔ %73 token / %91 gecikme tasarrufu); ≥~115k'da tam-bağlam kendisi −%30 bozulur → şema kazanır (Zep 115k→1,6k, +%15-18). İstisna: çeliştirici/negatif sorgular (tam bağlam halüsine eder 15,7 vs 80,0). Graf katmanı ∃-kategori kararıdır (entegrasyon/temporal/çapraz-oturum +, tek-kayıt erişim ve bilgi-GÜNCELLEME −) — ∀-katman değil; olgu-listesi üstüne opsiyonel. [A-YT4, A-YT5, A2-2]
4. **Çıkar + DOĞRULA + bedel-defteri.** Şema arızasının ~%76'sı çıkarım katmanında; ham LLM üçlü-çıkarımı %65,2 özne-halüsinasyonu → hibrit doğrulama (regex + yargıç + kaynak-satıra geri-eşleme) %1,6 [K, vekil-metrik]. Niteleyici EROZYONU ölçülü: aşırı-genelleme OR 4,85, tekrarlı turda birikir (%20→%40 / 5 tur) → niteleyici/kapsam/kesinlik alanı ZORUNLU (md.20'nin ölçülmüş hâli), damıtma TUR SAYISI sınırlı (kapsül üstüne-yazılır ama kaynak = kuyruk+defter+git — tek sigorta bu). Muhasebe ÇİFT: sorgu-anı token ↔ ingest/depo token ayrı raporlanır; tek sayı yasak. [A-YT7, C-YT6, A-YT3]
5. **Ucuz-katman-önce, beyanla yüksel; ölçüm kendi korpusunda.** Önce şema/özet katmanı; "cevaplanamaz" beyanında ham/tam bağlama yüksel (token −%39-61, doğruluk ±2 bandı) = m.20 pointer-inişinin ölçülmüş biçimi. gzip-oranı proxy'si yalnız <32KB parçada meşru; sıkıştırılabilirlik ölçümü karıştırılmış kopyadan; alan-dışı kalibrasyonsuz sıkıştırma −20 puan sınıfı kayıp. [A-YT8, B-YT7, B-YT6]

## 1. Matematik (formül — beyan edilmiş biçimiyle)
**Kabul çekirdeği (MDL iki-parçalı; birim beyan edilir — token):**
`L(şema) + Σᵢ L(kayıtᵢ | şema) + L(düzeltmeler) < Σᵢ L(kayıtᵢ)` ⇒ şema kurulur.
- Düzeltme listesi ana bedel kalemidir (grafikte temsilin %70-80'i düzeltme) — ingest v2'deki DLQ + serbest-alan tam bu terim; DLQ oranı ↑ ⇒ şema-uyumu ↓ ⇒ kazanç erir.
- Kayıt-birleştirme eşiği: s = (c_u + c_v − c_birleşik)/(c_u + c_v) > 0 ise birleştir; tek adım ≤2×, büyük kazanç zincirleme; **geri-alınabilirlik bizim tercihimizle AÇIK** (m.8: silme yok — faydası düşen yapı arşive iner, pointer kalır).
**Karar tablosu (tek skaler YOK; koşullu):** `karar = f(L_bağlam/pencere, sorgu-sınıfı, düzenlilik, güncelleme-yoğunluğu)` — §2.
**Uygunluk skoru U (kayıt-sınıfı başına; deneysel m.29 — kayıt-seviyesi skor literatürde YOK, bu bizim deneyimiz):**
`U = düzenlilik(+1: sabit-alanlı/şablonlu; komşu-benzerlik yüksek) + tekrar(+1: aynı tip ≥ N kayıt) + entegrasyon-sorgusu(+1: kayıtlar-arası birleştirme soruları geliyor) + güncelleme-yoğunluğu(−1: sık GEÇERSİZ-KIL/UPDATE) + niteleyici-yoğunluğu(−1: şerh/koşul/derece taşıyan metin) + anlatı(−1: akıl-yürütme izi/tek-seferlik)` → U ≥ 2 ŞEMALA · U ∈ {0,1} OLGU-SATIRI + pointer · U < 0 HAM TUT + pointer.

## 2. Karar tablosu (bağlam-sınıfı → yol; jarvis eşlemesi)
| bağlam sınıfı | örnek | karar | gerekçe |
|---|---|---|---|
| sabit-alanlı karar/olay kayıtları | defter karar blokları · kutu satırları · koşum tabloları | **ŞEMALA** (kapalı-tip + zarf; tablo/SQL görünümü) — zaten ingest v2 bunu yapıyor; şema-dalı: FLAG'li dosyada olgu-satırlarına indir + `veri/baglam.sqlite` görünümü (seans-3 V-1 hattını KULLAN, yeniden kurma) | U≥2; log-parsing %81-91 (ama ≥5-parametreli/nadir kayıtlar ayrı kova — karar/istisna kayıtları ÖZEL doğrulama) |
| tekrarlı prosedür/ritüel | skill adımları · checklist | ŞEMALA (zaten skill/şablon) | Sequitur/AWM: tekrar → kural |
| envanter/durum | pano kartları · hazine listesi · kapsül "şu an" | OLGU-SATIRI (snapshot; tarihçe git'te) | kapsül=SNAPSHOT ilkesi |
| çapraz-kayıt ilişki soruları | "hangi karar hangi maddeyi değiştirdi" | GRAF (opsiyonel katman; olgu-listesi ÜSTÜNE; [[wiki-link]] + anahtar-kaydı `replaced_by` zaten kenar) | entegrasyon +%21 (2Wiki) ama tek-kayıt −; ∃-kategori |
| niteleyici-yoğun hüküm | tüzük maddeleri · şerhler | **HAM TUT** + pointer; şemaya yalnız İNDEKS (madde-no → başlık) | niteleyici erozyonu OR 4,85; md.20 |
| akıl-yürütme izi / anlatı | rapor gövdeleri · tartışma | HAM (arşiv) + olgu-satırlı özüt (hasat); özüt gövdeden türetilir | ölçülmemiş sınıf; en riskli; tur-sınırı 1 |
| sık-güncellenen bilgi | açık borçlar · Salih-karar listesi | OLGU-SATIRI + bi-temporal damga (gecerli-baslangic/bitis); graf DEĞİL | Zep bilgi-güncelleme −%3,4 (şemanın en zayıf kategorisi) |

## 3. Damıtma şema-dalı (uygulama — `damitma` skill'ine eklendi)
FLAG'li dosyada, triyajdan önce: (i) kayıt-sınıflarını ayır (yukarıdaki tablo); (ii) sınıf-başına U hesapla; (iii) ŞEMALA-sınıfında olgu-satırlarına indir (atomik olgu + kaynak-pointer + niteleyici alanı + bi-temporal damga), ÇIKARIMI DOĞRULA (her olgu-satırı → kaynak satırına geri-eşle; eşleşmeyen DAYANAKSIZ → kaynaklanır ya da düşer — halüsinasyon paketi F1); (iv) HAM-sınıfını arşive pointer'la; (v) ölçüm satırı: dosya · sınıf-başına kayıt sayısı · önce/sonra token (çift muhasebe) · DLQ oranı · tur numarası (≥3 turda dur — erozyon birikimi). Yükselme kuralı okuma tarafında: şema katmanı "cevaplanamaz" derse ham arşive in (m.20).

## 4. m.16 taraması + şerh-adayları + ölçüm borcu
- Çelişki YOK — m.20/m.22/ingest-v2/damitma bu şemanın önceden-var parçaları; kanıt jarvis tasarımını 3 noktada DOĞRULADI (pointer-inişi = ölçülmüş "ucuz-önce"; kapsül=SNAPSHOT + git-kaynak = compaction-sürüklenmesi sigortası; ingest kapalı-tip = MDL düzeltme-terimi yönetimi).
- **Şerh-adayı (Katman-1):** "damıtma ~%50 hedefi" orana değil sorgu-uyumuna bağlanmalı (F2 bulgusu); kapsül üstüne-yazma turlarına erozyon-sayacı.
- **Ölçüm borcu:** Jarvis bandı (26-115k) ölçülmemiş · Türkçe BPE etkisi · karar-kanonu sınıfı · U skorunun kalibrasyonu (ilk 5 damıtma koşumunda sınıf-başına önce/sonra + DRFR); Hat-6 jarvis→DB hattı `veri/baglam.sqlite` üstünde sorgu-anı/ingest çift muhasebesini ölçebilir.
