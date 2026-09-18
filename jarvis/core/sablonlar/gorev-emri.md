# Şablon — Görev Emri

*(Sözlük: bir ajana iş verilirken yazılan sözleşme. Hazırlayan: Jarvis (eski ad Carvis, Karar 93); Salih panodan tarar, veto edebilir.)*

- **Görev / hedef:**
- **İzinli aksiyonlar:**
- **Yasaklar:**
- **Okunacak dosyalar (wiki seti):**  <!-- #17: sınıfa optimize okuma listesi buraya -->
- **Yazılabilir yüzeyler:**  <!-- varsayılan: yalnız raporlar/ -->
- **Durma koşulu (done-yüklemi; K2-c, imza 08-03):**  <!-- ikili ya da sayılabilir tamam-koşulu ("rapor yazıldı ∧ ≥6 kaynak" formunda); yazılamıyorsa görev tanımlanmamıştır. ŞERH: bu alanın varlığı K2-d (tetik) / K2-e (kısıt-profili) alanlarının otomatik imzası DEĞİLDİR -->
- **Teslim formatı:**
- *(taslak alan, sözlük-dışı — V2)* **Zaman bütçesi / son tarih (#22):**
- *(taslak alan — V2)* **Hiyerarşi telafisi (#23):** emir ayrıntısı ∝ yetenek farkı × muğlaklık — muhakeme boşluklarını üst model doldurdu mu?
- *(taslak alan — V2)* **Koşucu sınıfı (#24):** model + effort; karar-yoğunluğuna göre boyutlandır.
- **Emir konumu + erişim doğrulaması (K2-b, imza 08-03):** kanonik adres (dal · yol) + commit SHA. ŞERH (hakem kaydı): bu alan bant-İÇİdir — m.46(a) bant-dışı doğrulamanın YERİNE GEÇMEZ, koruma sanılmamalı. *(Konum şerhi — m.46(a) cache, imza 08-20 KB-18: SHA dinamik alandır; statik-önek-önde/dinamik-son kuralı gereği bu alan şablonun SONUNDA durur; görev-fonksiyonu şablonu zaten uyumluydu.)*

## SPEC / PLAN / TASKS (KB-14, Salih 08-17 — proje-ölçekli / çok-ajan işte ZORUNLU; m.25 eşik altında atlanır)
- **SPEC (ne, neden, kabul ölçütü):** <problem · kullanıcı · done-yüklemi boolean · kapsam dışı>
- **PLAN (nasıl, hangi parçalar):** <mimari kararlar · bağımlılıklar · riskler · ölçüm (P6 dörtlüsü: token·süre·iterasyon·sonuç)>
- **TASKS (küçük tipli fonksiyonlar):** <T1..Tn: her biri görev-fonksiyonu şablonuyla; sıra/paralellik; koşum profili (kosum_profili — üst model yazar)>
*Desen kaynağı: GitHub spec-kit (kurulmadı, iskeleti alındı — 'hazırı temel al' ilkesiyle uyumlu; `raporlar/2026-08-13-spec-kit-atlas-raporu.md`).*
