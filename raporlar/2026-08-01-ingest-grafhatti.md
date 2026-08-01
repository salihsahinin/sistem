# Rapor — raporlar/2026-08-01-ingest-grafhatti (BİRLEŞİK INGEST: F0-F1-F2 pipeline koşumu, 13 rapor)

*Emir: `cc/gorev-2026-08-01-21.md`. Tasarım girdisi: `cc/rapor-2026-08-01-20.md` §7 (✅=d) + EK-F.4 (F0 eki) + §14 (iç-müşteri) + F.3 (şema-kapsam kuralı). Koşan: Carvis alt-orkestratör (bu koşumun ORKESTRATÖRÜ, ana-sıra DEĞİL). F0(13 paralel)→F1(5 paralel lens)→F2(1 denetçi) fazları bu koşumda koşuldu; **F3 (Carvis compile + m.16 çelişki taraması + kanon-aday paketleme) bu dosyada YOKTUR — ana-sıraya kalır.** Bu dosya F0/F1/F2 çıktılarının MEKANİK DERLEMESİDİR, yeni karar/muhakeme İÇERMEZ. Format: AI-to-AI (08-01 emri) — tablo öncelikli, İNSAN-özet YOK, damga+niteleyici-taşıma sürer.*

**Karar VERİLMEDİ. Kanon yazılmadı. Katman-1 kalemleri LİSTELENDİ, imzalanmadı. Git komutu çalıştırılmadı.**

---

## §1 — H1-H51 HİPOTEZ-DURUMU TABLOSU (Lens-1 + F2 örneklem-verdikti)

*Kapsam: rapor-8..19 = H1-H47, rapor-20 (+EK-F) = H48-H51. 51/51 satır tam. F2 sütunu yalnız örneklenen satırlarda dolu (25 satırdan 10'u bu tabloya değiyor); örneklenmeyenler "—".*

| H# | kaynak-rapor(lar) | damga | hüküm-tipi | künye-sınıfı | çelişki-bayrağı | F2 verdikt |
|---|---|---|---|---|---|---|
| H1 | rapor-8 (183-186) | yapısal olarak SAĞLAM, niceliksel olarak DESTEKSİZ | aynı | — | yok | TUTTU |
| H2 | rapor-8 (188-192) | DARALTILDI ve KOŞULLANDI | aynı | — | yok | — |
| H3 | rapor-8 (194-199) | BİÇİM SAĞLAM, KORUMA EKSİK | aynı | — | yok | — |
| H4 | rapor-8 (201-205) | DÜŞTÜ — ama YERLEŞTİRİLEBİLİR (V41) | aynı | — | yok | — |
| H5 | rapor-9 (117-121) | ÇELİŞKİLİ (çekirdek AYAKTA, kuyruk DARALDI) | köprü-hipotez | — | yok | — |
| H6 | rapor-9 (122-125) | AYAKTA (adlandırma) + DARALDI (değer yargısı) | köprü-hipotez | — | yok | — |
| H7 | rapor-9 (127-130) | AYAKTA (formel); karşı-kanıt DARALDI | köprü-hipotez | — | yok | — |
| H8 | rapor-10 (155-158) | BİRİNCİ FIKRA DESTEKLENDİ(güçlü)·İKİNCİ DARALTILDI | köprü-hipotez | — | yok | TUTTU |
| H9 | rapor-10 (160-163) | DESTEKLENDİ ama İKİ YANDAN DARALTILDI | köprü-hipotez | — | yok | — |
| H10 | rapor-10 (165-168) | BİRİNCİ FIKRA DESTEKLENDİ(güçlü)·İKİNCİ NÜANSLANDI | köprü-hipotez | — | yok | — |
| H11 | rapor-10 (170-173) | (iii) DESTEKLENDİ, (ii) öngörülenden GÜÇLÜ ÇIKTI | köprü-hipotez | — | yok | — |
| H12 | rapor-11 (222-225) | AYAKTA + DARALDI | kısmi-sıralı, karma | — | yok | — |
| H13 | rapor-11 (227-230) | DARALDI (sert) | tek-atımlık çerçeve yanlış; çift-yönlü teorik meşru/ampirik desteksiz | — | yok | — |
| H14 | rapor-11 (232-234) | BİRİNCİ YARISI DÜŞTÜ(Ç11), İKİNCİ AYAKTA | temsil BİÇİMİ+TAZELEME belirleyici, salt kalıcılık kazanç vermiyor | — | yok | — |
| H15 | rapor-11 (236-239) | AYAKTA (güçlendirilmiş NEGATİF) | etiketsiz alan (V54) | [K] teyitsiz | yok | — |
| H16 | rapor-12 (284-286) | DOĞRULANDI(2.yarı güçlü), 1.yarı DARALTILDI | aynı | — | yok | — |
| H17 | rapor-12 (288-292) | 1.YARI DOĞRULANDI·2.YARI ÇÜRÜTÜLDÜ·3.YARI DARALTILDI | aynı | — | yok | — |
| H18 | rapor-12 (294-296) | 1.YARI DOĞRULANDI·2.YARI ÇÜRÜTÜLDÜ (kayıpsız düştü) | aynı | — | yok | — |
| H19 | rapor-12 (298-300) | ÇÜRÜTÜLDÜ (ölçüt-verme iddiası) | benzetme metafor düzeyinde kalıyor | — | H37(rapor-17) büyüklük-farkı gerilimi | TUTTU |
| H20 | rapor-13 (211-214) | ÇEKİRDEK AYAKTA, "tamamen" DARALTILDI | aynı | — | yok | — |
| H21 | rapor-13 (216-219) | AYAKTA (en güçlü hipotez) | aynı | — | yok | — |
| H22 | rapor-13 (221-224) | 1.YARI AYAKTA, 2.YARI DESTEKLİ AMA REJİM-DIŞI | — | — | yok | — |
| H23 | rapor-13 (226-229) | DARALDI | aynı | — | yok | — |
| H24 | rapor-14 (212-213) | İKİYE AYRILDI | 1.yarı DOĞRULANDI[D], 2.yarı DARALTILDI | [D] (kısmi) | yok | — |
| H25 | rapor-14 (215-216) | KISMEN DÜŞTÜ, YÖN DEĞİŞTİ | elle-ayar-yanlış ayakta[D]; TAKVİM-formu düştü, hayatta kalan TETİK-bağlı | [D] (kısmi) | yok | — |
| H26 | rapor-14 (218-219) | ÜÇ MEKANİZMA AYAKTA, TERS-U GENELLEMESİ DÜŞTÜ | atıf-bozulması[D]·salınım[D]·knob-overfit[D-teorik] | [D]/[D]/[D-teorik] | yok | — |
| H27 | rapor-14 (221-222) | 1.YARI AYAKTA, 2.YARI ŞARTLI, 3.YARI DÜŞTÜ | ε m.39 deneysel-damgalı zorunlu; K-020 birleşme düştü | — | yok | — |
| H28 | rapor-15 (256-258) | DARALTILDI | aynı | — | yok | — |
| H29 | rapor-15 (148-153; 260-263) | 148-153:[D-belge]/DARALTILDI(çekirdek) → 260-263:KISMEN DÜŞTÜ/DOĞRULANDI | aynı rapor içi 2 ayrı satır-aralığı, tekleştirilmedi | [D-belge] (kısmi) | YENİ (F1 tespiti): H29 rapor-15 içinde iki farklı satır-aralığında farklı hükümle geçiyor, F0'da birleştirilmemiş | — |
| H30 | rapor-15 (265-268) | KISMEN DESTEKSİZ, KISMEN DÜZELTİLDİ | künye Ç14 | — | yok | — |
| H31 | rapor-15 (270-272) | DESTEKLENDİ ve GÜÇLENDİ | MCP spec/CA DMV/FDA PCCP | — | yok | — |
| H32 | rapor-16 (214-217) | İLK YARISI AYAKTA·İKİNCİ ETİKETSİZ(V54) | aynı | — | yok | — |
| H33 | rapor-16 (219-222) | AYAKTA+GÜÇLENDİRİLDİ, bir yeri DÜZELTİLDİ | aynı | — | yok | — |
| H34 | rapor-16 (224-227) | AYAKTA+GÜÇLENDİRİLDİ | aynı | — | yok | — |
| H35 | rapor-16 (229-232) | DARALDI (iki yandan) | aynı | — | yok | — |
| H36 | rapor-17 (279-280) | DARALTILARAK DOĞRULANDI | Tek ekonomi var, adı ski-rental (amortisman değil) | — | yok | TUTTU |
| H37 | rapor-17 (282-284) | NİTEL DURUYOR, NİCEL ÖLÇÜMLE DÜŞTÜ | sıralama doğru, büyüklük farkı yok | künye: rapor-12 H19 | YENİ: H19(ÇÜRÜTÜLDÜ) ile H37 arası büyüklük-farkı gerilimi, F0'da çözülmemiş | — |
| H38 | rapor-17 (285-287) | DOĞRULANDI, beklenenden farklı maddeyle | m.31/m.42 geri-alınabilirlik eksenine oturuyor | — | yok | — |
| H39 | rapor-17 (288-290) | KOŞULLU DOĞRULANDI | ölçüt değil UYARI; bir geçiş noktası var | — | yok | — |
| H40 | rapor-18 (326-328) | DARALTILARAK DOĞRULANDI | aynı | [D] (V26 doğrulandı) | yok | — |
| H41 | rapor-18 (329-332) | KOŞULLU DOĞRULANDI | koşul BUGÜN SAĞLANMIYOR + ifade düzeltildi | [D] | yok | — |
| H42 | rapor-18 (333-334) | 1.YARI DÜZELTİLEREK DOĞRULANDI, 2.YARI DARALDI | — | [D] | yok | — |
| H43 | rapor-18 (336-337 / 297-306) | DOĞRULANDI (raporun en sağlam kalemi) | şart-zinciri (iii)⟸(ii); **rapor-20 §3.2 K2∧K3 kuralıyla AYNI YAPI (çapraz-teyit)** | [D-belge] | çapraz-teyit rapor-20 ile (bkz §4 #4) | TUTTU |
| H44 | rapor-19 (287-288) | DOĞRULANDI [D] | iki daraltmayla | [D] | yok — iç-müşteri #24 | — |
| H45 | rapor-19 (290-291) | DARALTILDI [ÇİFT 7] | aynı | — | yok | — |
| H46 | rapor-19 (293-294) | DÜŞTÜ [ÇİFT 8] [X] | aynı | [X] | yok — iç-müşteri m.37 çeşitlilik | — |
| H47 | rapor-19 (296-297) | KISMEN DOĞRULANDI [ÇİFT 12] | kritik düzeltmeyle | — | yok — iç-müşteri A5 | — |
| H48 | rapor-20 (311-315; EK-F güncelleme 617) | DARALTILARAK DOĞRULANDI (EK-F: destek güçlendi, karşı-kanıt zayıfladı, damga AYNI) | "Alakasız-bağlam zararı ölçülüdür" | — | yok | TUTTU |
| H49 | rapor-20 (316-320; EK-F 618) | DOĞRULANDI ve GÜÇLENDİRİLDİ (iki dik eksen; EK-F 3. kanal ekledi) | "Spesifiklik→başarı monoton değil" | — | yok | — |
| H50 | rapor-10 (yerel mention — **F2: rapor-10 gövdesinde doğrulanamadı**) + rapor-20 (321-326, 513; EK-F 619) | DOĞRULANDI(1.yarı,güçlü)+KOŞULLU DOĞRULANDI(2.yarı) | "Pipeline monoliti koşulsuz yenmez" | [X] (kısmi, arXiv:2503.13657 atfı için) | BİLİNEN #1: rapor-10 yerel "H50" ↔ rapor-20 H50 NUMARA ÇAKIŞMASI — **F2 bunu derinleştirdi: rapor-10'un gövdesinde H8-H11 dışında hiçbir H# yok; rapor-20 EK-C'nin rapor-10'a atfettiği "H2,H4,H50*" listesi kaynakta doğrulanamıyor (bkz §4 YENİ-2)** | KISMEN |
| H51 | rapor-20 (327-330; EK-F 620) | MEKANİZMA AYAKTA, KAZANÇ ÖLÇÜLMEMİŞ (EK-F: sertleşti) | "Ayrı okuyucu ajan kazancı doğrulayıcı≠üretici mekanizmasından gelir" | — (Anthropic iç-değ., replikasyonsuz) | BİLİNEN #2: rapor-16(153-162) ≡ rapor-20 §4.3 ÇAPRAZ-TEYİT/AYNI-KALEM | TUTTU |

---

## §2 — KATMAN-1 ADAY DEDUP TABLOSU (Lens-2 + masa-küme + F2 verdikt)

*119 ham aday satırı (rapor-içi K1-a..o kodlu + rapor-14/15/17 kodsuz satırlar + 2 kuyruk dosyasının adayları) dedup edildi. Açık mükerrer birleştirmeler (görev emrinde önceden bilinenler dahil) ve kendi-taramada bulunan ek adaylar ayrı işaretli.*

### 2.1 Açıkça BİRLEŞTİRİLEN kalemler (F0/rapor kendi beyanıyla)

| Birleşik-# | Orijinal kod(lar) | Başlık | Kaynak-rapor(lar) | F2 verdikt |
|---|---|---|---|---|
| #1 | rapor-8 K1-8 + rapor-10 K6 + rapor-13(302-306) | Deterministik çağrı-kapısı tasarımı (EK-4; rapor-13'te "4. vaka") | rapor-8, rapor-10, rapor-13 | TUTTU |
| #40 | rapor-12 K1-8 + rapor-20 §13 K1-h | m.40b v0.2 koşum-deseni (2 koşum üst üste 0/8 tam-sağlam tez) | rapor-12, rapor-20 | TUTTU |
| #92 | rapor-18 KL18-12 + rapor-20 EK-F K1-j | Bütçe/fren yazım kuralı: koşum-toplamı, ajan-başına DEĞİL | rapor-18, rapor-20 | TUTTU |
| #102+#109 | rapor-20 K1-c + rapor-20 EK-F K1-l | TAMAMLAYICI (mükerrer değil): K1-c "özetle DENMEZ" yasağı, K1-l bunu teslim-nesnesi/muhakeme-izi ayrımıyla TAMAMLIYOR | rapor-20 | — |
| #40+#111 | rapor-20 K1-h + rapor-20 EK-F K1-n | Aynı masa: m.40b koşum-deseni ailesi | rapor-20 | — |

### 2.2 Aday (dedup şüpheli, kod-tespiti/teyit bekliyor)

| Birleşik-# | Kod(lar) | Tema | Kaynak-rapor(lar) | Not |
|---|---|---|---|---|
| #8/#105 | rapor-8 K1-7 ~ rapor-20 K1-f | m.25 eşiği | rapor-8, rapor-17, rapor-20 | Üç raporda benzer tema, kesin kod-eşleşmesi kaynak dosya teyidi ister |
| #29/#73/#78 | rapor-11 KL7 ~ rapor-17 R17-1/R17-6 | K-019 iç-müşteri teması | rapor-11, rapor-17 | Aynı iç-müşteri, ayrı kod, birleşme masada teyit |
| #58/#100/#101/#113/#114/#116 | rapor-15(core/sablonlar) ~ rapor-20 K1-a/b/e ~ kuyruk-1 Q1-1/Q1-2/Q1-4 | AI2AI format/devir-arayüzü + "genel çalışma ilkeleri" masa gündemi | rapor-15, rapor-20, kuyruk-1 | En büyük tematik küme — masa tek gündem altında görebilir |
| #64 | rapor-15 8. Katman-1 kalemi | VERİ TUTARSIZLIĞI: F0 "8 adet" demiş, yalnız 7 künye listelenmiş | rapor-15 | **F2: TUTTU — doğrulandı, rapor-15'te satır 241-247 gerçekten yalnızca 7 kalem (1-7), 8. kalem YOK.** Bu F0/rapor-15 arası bir sayım-tutarsızlığıdır, ingest'e veri-bütünlüğü notu olarak taşınmalı. |

### 2.3 Masa-küme önerisi (dedup sonrası, tematik)

1. **pipeline/loop kanonu:** rapor-13(313-315,ingest-borcu), rapor-20 K1-c, rapor-20 EK-F K1-l, rapor-20 EK-F K1-o (F0 mekanik-döküm fazının ingest'e girip girmeyeceği)
2. **AI2AI format/devir-arayüzü:** rapor-15(core/sablonlar), rapor-20 K1-a/b/e, kuyruk-1 Q1-1..4 (bkz 2.2)
3. **bütçe-fren mekaniği:** #92 (birleşik), rapor-20 EK-F K1-k (mükerrer-sevk freni), kuyruk-2 Öneri-B
4. **deterministik çağrı-kapısı:** #1 (birleşik, 3 kaynaklı)
5. **ölçüm-bankı/rejim-etiketi:** rapor-8 K1-9, rapor-9 K4, rapor-11 KL10, rapor-13 KM8, rapor-15(kuyruk/olcum-banki künyeli + Ç14 künyeli), rapor-16 KL16-8, rapor-17 V47/R17-8, rapor-19 A3, kuyruk-2 Öneri-A/Öneri-C
6. **m.40b koşum-deseni:** #40 (birleşik)
7. **K-019 iç-müşteri (aday küme):** #29/#73/#78 (bkz 2.2)
8. **m.25 eşiği (aday):** #8/#105 (bkz 2.2)
9. **diğer (tekil, kümelenmemiş):** kalan ~95 satır — rapor-9 K1-K3/K5, rapor-10 K1-K5/K7-K8, rapor-11 KL1-6/9, rapor-12 K1-1..7, rapor-13 KM1-7, rapor-14 (6 kodsuz), rapor-15 (Salih-şerhi/CA-DMV/m.41), rapor-16 KL16-1/3/4/6/7, rapor-18 KL18-1/3-11/13-14, rapor-19 A2/K-b, rapor-20 K1-d/g/i, K1-m

**Toplam dedup-sonrası ayrı kalem sayısı: ~106** (119 ham − ~5 açık-birleştirme çifti kaydı − 1 tamamlayıcı-çift − veri-tutarsızlığı notu ayrımı; kesin sayım masa oturumunda teyit edilir, bu bir F1-tahminidir).

---

## §3 — İÇ-MÜŞTERİ DAĞITIM TABLOSU (Lens-3 + F2 verdikt)

### 3.1 Deterministik çağrı-kapısı (←g15)
8 kaynak-grubu: rapor-8 K1-8(256) · rapor-10 K6(234) · rapor-13(302-306,[D-ölçüm]) · rapor-15(216,[D-belge V26 doğrulandı]) · rapor-15(218-224, Beş sert tasarım kısıtı) · rapor-15(225, Anthropic API ref. mimari) · rapor-15(227, Ç13 kapı-yerleşimi) · rapor-15(229, ölçüm yüzeyi). **F2 verdikt: TUTTU** (bileşim ve içerik doğrulandı).

### 3.2 K-019/K-016 (←g17)
K-019: rapor-11 KL7(302) · rapor-17(295-299, 5 satır) · rapor-17(315, Katman-1) · rapor-17(320, Katman-1). K-016: rapor-17(305-309, 5 satır). **F2 verdikt: KISMEN** (denetim kapsamı dışında kaldı, tam liste teyit edilemedi — masa oturumunda tekrar taranmalı).

### 3.3 A5 (←g19/g20)
rapor-11 KL8(303) · rapor-19 H47(296-297) · rapor-19 K-e(247) · rapor-19 M-e(258) · rapor-19 T19(65/195-197) · rapor-20 §5 rol-tablosu ("pipeline m.44'ün yerine geçmez" şerhiyle). **F2 verdikt: —** (örneklenmedi).

### 3.4 m.37 çeşitlilik (←g19)
rapor-19 H46(293-294) · rapor-19 A1(271) · rapor-19 K-a(243). **F2 verdikt: KISMEN** (grup büyüklüğü akla yatkın ama örneklem sınırlı, rapor-19'da en az 3 ek aday nokta bulundu — tam liste teyit gerektirir).

### 3.5 #24 (←g19/g20-S4)
rapor-19 H44(287-288). **F2 verdikt: TUTMADI — EKSİK SAYIM.** rapor-19 satır 374'te ikinci bir #24 atfı var ("emir #24 satırının çift okumasında..."), Lens-3 bunu kaçırdı. Masa compile aşamasında bu ikinci satır eklenmeli.

### 3.6 Ölçüm-bankı adayları
20 ham satır (rapor-8 K1-9 · rapor-9(136-140)+K4 · rapor-11 KL10 · rapor-13(180-182,190,241-243)+KM8 · rapor-15(133,156,196,246,247) · rapor-16 KL16-8 · rapor-17(295-296,305,316,322) · rapor-19 M-c/M-d · rapor-20 §11 "sayı-sadakati≫mekanizma-sadakati"). Detaylı işleniş §5'te (Lens-5).

### 3.7 Masa / genel-çalışma-ilkeleri (diğer)
rapor-13(313-315, ingest borcu, künye rapor-12) · rapor-20 §14 K1-a/b/c/e/f (satır 407-412).

**Pointer-inişleri (Lens-3):** 0 — tüm dağıtım F0 özetinden çözüldü.

---

## §4 — ÇELİŞKİ/MÜKERRERLİK HÜKÜMLERİ (Lens-4 + F2 verdikt)

| # | Taraflar | Tip | Hüküm | Gerekçe (kaynağın kendi ifadesi) | F2 verdikt |
|---|---|---|---|---|---|
| **BİLİNEN-1** | rapor-16 §6.2(153-162, öz-DÜZELTME≠öz-DOĞRULAMA) ≡ rapor-20 §4.3(188-198) | MÜKERRER-KALEM | **BİRLEŞTİR** | rapor-20 sat.198 aynen: "Rapor-16 §6.2'nin ... hükmüyle aynı yere basıyor; ayrı kalem açılmamalı, birleştirilmeli." | TUTTU |
| **BİLİNEN-2** | rapor-10 K1(sat.229, "$16-19; tam kontrat muhtemelen $30+") ↔ m.40b v0.2 tam-kontrat tavan-rejimi | İÇERİK-ÇELİŞKİSİ | **MASAYA-İŞARETLE** (çözülmüş SAYILMAZ) | `kuyruk/gelen-2026-08-01-tavan-rejim-karari.md` bu veriyi zaten taşıyor; ingest'te AYRICA bayraklanır | TUTTU |
| 3 | rapor-10 (yerel "H50" mention, EK-C atfı) ↔ rapor-20 H50(§8, 321-325) | NUMARA-ÇAKIŞMASI | **YENİDEN-NUMARALANDIR** | rapor-20 EK-C dipnotu(513): "rapor-10'daki 'H50' numarası bu raporun H50'siyle ÇAKIŞIYOR ... V28 emsali: çakışma loglanır, silinmez." | **KISMEN** — F2: dosya-atfı ("rapor-10 EK-C sat.501") yanlış, o satır aslında rapor-20'de; ama alt-tespit önemli: rapor-10 gövdesinde H8-H11 dışında HİÇBİR H# yok |
| **YENİ-2** | rapor-20 EK-C'nin rapor-10'a atfettiği hipotez listesi ("H2, H4, H8-H11, H50*") ↔ rapor-10'un fiili gövdesi (yalnız H8-H11 doğrulanabildi) | İÇERİK-TUTARSIZLIĞI (F2-kaynaklı yeni bulgu) | **MASAYA-İŞARETLE** | F2 doğrudan-denetim: "rapor-10'da yalnız H8, H9, H10, H11 tanımlı; başka H# yok" — rapor-20'nin kendi EK-C ingest-özet tablosu (kapsam ölçümü) bu noktada rapor-10'u YANLIŞ temsil ediyor olabilir | (F2'nin kendisi bu satırı ürettiği için "verdikt" uygulanmaz — bu bir F2 tespiti, ayrıca doğrulanmalı) |
| 4 | rapor-18 §7 şart-zinciri "(iii)⟸(ii)"(301) ↔ rapor-20 §3.2 "¬(K2∧K3)→pipeline KURULMAZ"(144-147) | ÇAPRAZ-TEYİT | **TEK-KALEM-KAYDET** (mükerrer DEĞİL) | rapor-20 sat.147: "K2∧K3 şartı, rapor-18'in (iii)⟸(ii) şart-zinciriyle aynı yapıdadır ... İki bağımsız hattan aynı forma varıldı." | TUTTU |
| 5 | rapor-20 K1-j(EK-F,647) ↔ rapor-18 KL18-12(38) | MÜKERRER-KALEM | **BİRLEŞTİR** | rapor-20 K1-j aynen: "(S1 + rapor-18 KL18-12 aynı kalem, BİRLEŞTİRİLMELİ)" | TUTTU |
| 6 | rapor-20 K1-h(§13,414) ↔ rapor-12 K1-8 | MÜKERRER-KALEM | **BİRLEŞTİR** | rapor-20 K1-h aynen: "(rapor-12 K1-8 ile BİRLEŞTİRİLECEK kalem)"; rapor-20 §12(399) tekrar teyit | TUTTU |
| 7 (aday) | "deterministik çağrı-kapısı" borcu — rapor-8/rapor-10/rapor-13/rapor-15 4 bağımsız vaka | BİRİKEN-KANIT | **AYRI-TUT** (tek borç-defterinde izlenir, ayrı Katman-1 AÇILMAZ) | 4 rapor bağımsız kendi maliyet-aşım vakasını kaydediyor, birbirinin tekrarı değil | — |
| 8 (aday) | rapor-16 KL16-1 ↔ rapor-11 KL1 ("ufuk" kelimesinin iki anlamı) | MÜKERRER-KALEM (kendi-beyanlı) | **BİRLEŞTİR** | rapor-16 KL16-1 aynen: "rapor-11'in KL1'iyle (iki 'ufuk') aynı aile ... Birlikte karara bağlanmalı." | — |
| 9 (aday) | rapor-16(§7.1 madde-3) ↔ rapor-11 KL9 ↔ rapor-9 (ex-ante/ex-post sütun önerisi) | MÜKERRER-KALEM (3 raporlu zincir) | **BİRLEŞTİR** | rapor-16 aynen: "rapor-11'in KL9'u ... ile AYNI KALEM — ayrı iş açılmamalı" | — |
| 10 (aday) | rapor-16 KL16-4 ↔ rapor-11 KL5 ("ufuk = Y hedef-bandı") | MÜKERRER-KALEM (kendi-beyanlı) | **BİRLEŞTİR** | rapor-16 KL16-4 aynen: "rapor-11'in KL5'iyle ... aynı satırı hedefliyor" | — |
| 11 (aday) | rapor-16 KL16-7 ↔ rapor-11 KL4 (kenar-türü kararı) | MÜKERRER-KALEM (kendi-beyanlı) | **BİRLEŞTİR** | rapor-16 KL16-7 aynen: "rapor-11 KL4'ün ... üretim kuralı karşılığı" | — |
| 12 (aday) | rapor-18 (İlke-3/rank-sağlamlığı) ↔ rapor-17 (H38/değişmezlik) | MÜKERRER-KALEM (KISMİ) | **AYRI-TUT** (çapraz-pointer'lı) | rapor-18 kendi tablosunda: "KISMEN MÜKERRER ... Komşu ama özdeş değil" | — |
| 13 (aday) | "m.25 eşiği" — rapor-11/rapor-15/rapor-17/rapor-20 K1-f | BİRİKEN-KANIT | **AYRI-TUT** (tek gündem başlığı altında, ayrı kalemler) | Aynı tüzük maddesinin farklı alt-alanlarda bağımsız ele alınışı | — |

**TUTMADI oranı (F2 toplam, tüm lensler):** 3/34 kesin TUTMADI (~%9); KISMEN dahil 6/34 (~%18); TUTTU 28/34.

---

## §5 — ÖLÇÜM-BANKI KALEM ADAYLARI (Lens-5 + F2 verdikt)

*m.39 kuralı: yalnız GA'lı/örneklemli/doğrudan-eklenebilir somut sayısal kalemler ana tabloya girer. Lens-5 F0 özetinin ÖTESİNE geçip ham rapor dosyalarına 24 kez indi (bkz §6) — bulduğu ek veri hem doğru hem bir yerde İCAT-ETME riskini taşıdı; F2 bunu ayırt etti.*

### 5.1 Ana ölçüm-bankı aday tablosu

| Ölçüm adı | Değer/durum | GA/n | Kaynak-rapor+satır | Damga | F2 verdikt |
|---|---|---|---|---|---|
| m.40b v0.2 hayatta-kalma oranı (tek-koşum kaba sayım) — künye kaynağı doğru | rapor-8 §11'in kendi ölçüm-bankı-adayı beyanı | n belirsiz | rapor-8 §11/K1-9(257) | [D-ölçüm], aday | TUTTU (kalemin VARLIĞI doğru) |
| — aynı kalemin "(n=23 hüküm)" eki | — | — | (Lens-5'in kendi eki) | — | **TUTMADI — rapor-8'de "n=23" veya "23 hüküm" ifadesi YOK; rapor-8'de yalnız 4 HÜKÜM (H1-H4) var. Muhtemel uydurma/karıştırma — bu rakam ingest'e TAŞINMAMALI.** |
| `fikir-kutusu.md` güncel boyutu | 23,7 KB (arşiv 30,0 KB) | n=1 (anlık) | rapor-17 §9(295) | [D-ölçüm] | TUTTU — birebir doğrulandı |
| `fikir-kutusu.md` değişim sıklığı | 1,37 değişim/gün | n=19 gün | rapor-17 §9(296) | [D-ölçüm] | TUTTU — birebir doğrulandı |

**Not (F0→F1 tutarlılığı):** son iki kalem (fikir-kutusu.md ölçümleri) F0'ın rapor-17 için verdiği özette yalnızca "K-019 girdisi" olarak, ayrıntısız geçiyordu — Lens-5 bunları ham dosyaya inerek DOĞRU biçimde tamamladı. Bu, F0 özetinin bu noktada YETERSİZ, F1'in ham-rapora inişinin GEREKLİ olduğu bir vaka. "n=23 hüküm" ekiyse aynı ham-rapora-iniş davranışının YAN ÜRÜNÜ olarak icat edilmiş görünüyor — F1'in serbestçe ham metne inmesinin hem faydası hem riski aynı ajanda birlikte gözlendi.

### 5.2 Bekleyen (ön-koşullu) alt-liste
Ex-ante↔ex-post korelasyonu (rapor-9, N=15-20 koşum bekliyor) · Landmark mesafe ölçümü (rapor-13, n birikimi bekliyor) · m.43 skill-doğum eşiği N=B/r (rapor-17, B/r ölçülmedi) · Hakem karar-defteri (rapor-17, ~20 kararlık kayıt bekliyor) · Vardiya-devri turn-cost (rapor-19 A3/M-c, n≥20 vardiya) · Vardiya-saati etkisi (rapor-19 M-d, veri birikimi bekliyor).

### 5.3 Gelecek-aday (henüz ölçülmedi)
Keşif kotası/w-ε doyma eşiği (rapor-13) · w/ε+ufuk-etiketi+pdftoppm eksikliği üçlüsü — KM8 (rapor-13) · PDF-render altyapı eksikliği, 4 ardışık koşumda tekrar (rapor-11 KL10, rapor-13, rapor-16 KL16-8) · Heterojen kısıt-profili "göç" hipotezi (rapor-15 Ç14) · Yerel gaming taban-oranı (rapor-15) · ETA'nın olcum-banki'den türetilmesi (rapor-15 §5.3).

### 5.4 Nitel-gözlem adayı (m.39 dışı, ilke-adayı)
**"Alt-ajan aktarımında sayı-sadakati ≫ mekanizma-sadakati"** — rapor-20 §11(380), V26 denetiminin (12'de 10 TUTTU/2 TUTMADI) çıkardığı ilke; sayısal değil, nitel bir güvenilirlik-ilkesi olarak bank şemasına girmeli, "ölçüm" değil "uyarı" satırı olarak.

**Not:** bu koşumun kendisi (§4 ve bu bölümdeki F2 TUTMADI bulguları: Lens-3'ün #24 eksik-sayımı, Lens-5'in "n=23" icadı) yukarıdaki ilkenin **canlı ikinci örneğidir** — künyeler/rakamlar çoğunlukla doğru geldi, ama 2 noktada ajan kendi ek-veri/sayı üretti. `kuyruk/olcum-banki.md`'ye bu koşumun kendisi üçüncü örnek olarak eklenebilir (aday, karar verilmedi).

---

## §6 — PİPELİNE UYUM-GÖZLEMİ (F0→F1 gerilim ölçümü)

**Ölçülen: F1 fiilen ham rapora kaç kez indi (tool-call sayısı, lens başına)**

| Lens | Tool-call (ham dosya erişimi dahil) | Pointer-inişi beyanı | Gözlem |
|---|---|---|---|
| Lens-1 (H1-H51) | 0 | "0 pointer-inişi" | F0 özeti TEK BAŞINA yeterliydi — hiç ham rapora inmedi |
| Lens-2 (Katman-1 dedup) | 0 | "0 pointer-inişi" | F0 özeti yeterliydi; veri-tutarsızlığı tespiti (rapor-15, 8.kalem) bile F0'ın kendi çelişkisinden (7 künye ama "8 adet" ifadesi) çıkarıldı, ham dosyaya inmeden |
| Lens-3 (iç-müşteri) | 0 | "0 pointer-inişi" | F0 özeti yeterliydi — ama F2 bunun BEDELİNİ gösterdi: #24 grubunda 1 satır kaçtı (TUTMADI), K-019/K-016 ve m.37-çeşitlilik gruplarında F2 "KISMEN" verdi (F0 özeti bu iki grup için TAM değildi) |
| Lens-4 (çelişki/mükerrerlik) | 16 | beyan edilmedi (davranışsal olarak F2 tarafından doğrulandı) | Ham rapora YOĞUN indi — 4 yeni mükerrerlik adayı (§4/8-11) ve 1 dosya-atıf hatası (§4/#3, F2 TUTMADI) bu inişlerin ürünü |
| Lens-5 (ölçüm-bankı) | 24 | beyan edilmedi (davranışsal olarak F2 tarafından doğrulandı) | En yoğun ham-rapor erişimi — 2 gerçek yeni ölçüm buldu (TUTTU) + 1 icat edilmiş rakam üretti (TUTMADI) |

**F0'ın yeterlilik hükmü:** F0, 3/5 lens için (H-tablosu, Katman-1-dedup, iç-müşteri-dağıtımı) **tek başına yeterliydi** (0 pointer-inişi) — bu, rapor-20 EK-F.4'ün öngördüğü gerilimi (*"F0 iyi çalışırsa F1'in çok-lensli olması gerekmeyebilir"*) DOĞRULAR yönde bir veri noktası. Ancak 2/5 lens (çelişki-tespiti, ölçüm-bankı-çıkarımı) F0 özetini **yetersiz buldu ve yoğun** (16, 24 tool-call) ham-rapor erişimine gitti — bu da EK-F.4'ün varsaydığı "F0 sonrası F1 girdisi bütçe altına iner" iyimserliğinin **görev-tipine göre KOŞULLU** olduğunu gösteriyor: çelişki-tespiti ve serbest-sayı-çıkarımı gibi açık-uçlu/exhaustive-tarama gerektiren lensler F0'ın sabit şemasıyla YETİNEMEDİ.

**İkincil bulgu (kalite riski, gizlenmiyor):** ham-rapora yoğun inen 2 lensin ikisi de en az bir F2-TUTMADI ürettiği gözlendi (Lens-4: dosya-atıf hatası; Lens-5: icat edilmiş rakam "n=23 hüküm"). Bu koşumda örneklem küçük (n=2) ve nedensellik iddia edilmiyor, ama gözlem şudur: **F0 şemasının dışına çıkan lensler, F0'a sadık kalan lenslere göre epistemik hata riskini daha çok taşıdı.** Bu, rapor-20'nin K1-c/K1-l kalemlerinin ("özetle DENMEZ, şemayı doldur DENİR" — teslim nesnesine uygulanır) gerekçesini dolaylı olarak DESTEKLER: şema-dışı serbest-okuma arttıkça icat riski de arttı.

---

## EK — F0 HAM TABLOSU (13 rapordan muhakemesiz şema-doldurma, ham çıktı)

### rapor-8
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-8 | 183-186 | H1 | yapısal olarak SAĞLAM, niceliksel olarak DESTEKSİZ | aynı | — | hayır | hayır | hayır |
| rapor-8 | 188-192 | H2 | DARALTILDI ve KOŞULLANDI | aynı | Korf 1985; STRIPS MACROPS; SOAR chunking; Minton | hayır | hayır | hayır |
| rapor-8 | 194-199 | H3 | BİÇİM SAĞLAM, KORUMA EKSİK | aynı | A5 raporu; DECLARE; HTN metot öğrenme | hayır | hayır | hayır |
| rapor-8 | 201-205 | H4 | DÜŞTÜ — ama YERLEŞTİRİLEBİLİR (V41) | aynı | — | hayır | hayır | hayır |
| rapor-8 | 249-256 | — | — | Katman-1 aday | K1-1..K1-8 | evet | K1-8: evet (deterministik çağrı-kapısı, EK-4) | hayır |
| rapor-8 | 257 | — | — | Katman-1 aday / ölçüm-bankı adayı | K1-9 | evet | hayır | evet |

### rapor-9
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-9 | 9 | H1 | — | çapraz-kontrol borcu | cc/gorev-2026-08-01-8.md | hayır | hayır | hayır |
| rapor-9 | 117-121 | H5 | ÇELİŞKİLİ (çekirdek AYAKTA, kuyruk DARALDI) | köprü-hipotez | — | hayır | hayır | hayır |
| rapor-9 | 122-125 | H6 | AYAKTA (adlandırma) + DARALDI (değer yargısı) | köprü-hipotez | — | hayır | hayır | hayır |
| rapor-9 | 127-130 | H7 | AYAKTA (formel); karşı-kanıt DARALDI | köprü-hipotez | — | hayır | hayır | hayır |
| rapor-9 | 136-140 | — | — | ölçüm-bankı adayı | kuyruk/olcum-banki.md | hayır | hayır | evet |
| rapor-9 | 148-152 | — | — | Katman-1 aday | K1..K5 | evet | hayır | K4: evet |

### rapor-10
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-10 | 155-158 | H8 | BİRİNCİ FIKRA DESTEKLENDİ(güçlü)·İKİNCİ DARALTILDI | köprü-hipotez | Vaswani vd.; Dong vd.(Thm 2.1); Hopfield denkliği; Sparse Transformer | hayır | hayır | hayır |
| rapor-10 | 160-163 | H9 | DESTEKLENDİ ama İKİ YANDAN DARALTILDI | köprü-hipotez | Toy Models of Superposition; SAE nöron-yeme; splitting; absorption | hayır | hayır | hayır |
| rapor-10 | 165-168 | H10 | BİRİNCİ FIKRA DESTEKLENDİ(güçlü)·İKİNCİ NÜANSLANDI | köprü-hipotez | QK/OV (Elhage 2021); T3 metrik envanteri; VATP arXiv:2406.12335 | hayır | hayır | hayır |
| rapor-10 | 170-173 | H11 | (iii) DESTEKLENDİ, (ii) öngörülenden GÜÇLÜ ÇIKTI | köprü-hipotez | attribution graphs (Ameisen 2025); V39 ŞERH 3 | hayır | hayır | hayır |
| rapor-10 | 201-202 | — | [dürüst beyan] | SOMUT ÖLÇÜM: ÇIKMIYOR | — | hayır | hayır | hayır |
| rapor-10 | 229-236 | — | — | Katman-1 aday | K1..K8 | evet | K6: evet (deterministik çağrı-kapısı) | hayır |

### rapor-11
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-11 | 199-201 | — | — | A5 ekip-lideri paketi girdisi | core/pano.md (K-010 kartı) | hayır | evet (A5) | hayır |
| rapor-11 | 222-225 | H12 | AYAKTA + DARALDI | kısmi-sıralı, karma | JAIR 22 (Hoffmann/Porteous/Sebastia 2004) | hayır | hayır | hayır |
| rapor-11 | 227-230 | H13 | DARALDI (sert) | tek-atımlık çerçeve yanlış | MM; NBS; Suda 2013; Bacchus & Yang 1994 | hayır | hayır | hayır |
| rapor-11 | 232-234 | H14 | 1.YARI DÜŞTÜ(Ç11), 2.YARI AYAKTA | temsil biçimi+tazeleme belirleyici | arXiv:2606.15017; Reflexion ablasyonu | hayır | hayır | hayır |
| rapor-11 | 236-239 | H15 | AYAKTA (güçlendirilmiş NEGATİF) | etiketsiz alan (V54) | Ng ve ark.(Corollary 2)[K,teyitsiz] | hayır | hayır | hayır |
| rapor-11 | 296-305 | — | — | Katman-1 aday | KL1..KL10 | evet | KL7: evet(K-019); KL8: evet(A5) | KL10: evet |

### rapor-12
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-12 | 271-278 | — | — | Katman-1 aday | K1-1..K1-8 | evet | hayır | hayır |
| rapor-12 | 284-286 | H16 | DOĞRULANDI(2.yarı güçlü), 1.yarı DARALTILDI | aynı | — | hayır | hayır | hayır |
| rapor-12 | 288-292 | H17 | 1.YARI DOĞRULANDI·2.YARI ÇÜRÜTÜLDÜ·3.YARI DARALTILDI | aynı | — | hayır | hayır | hayır |
| rapor-12 | 294-296 | H18 | 1.YARI DOĞRULANDI·2.YARI ÇÜRÜTÜLDÜ | aynı | — | hayır | hayır | hayır |
| rapor-12 | 298-300 | H19 | ÇÜRÜTÜLDÜ | metafor düzeyinde kalıyor | — | hayır | hayır | hayır |

### rapor-13
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-13 | 211-214 | H20 | ÇEKİRDEK AYAKTA, "tamamen" DARALTILDI | aynı | — | hayır | hayır | hayır |
| rapor-13 | 216-219 | H21 | AYAKTA (en güçlü) | aynı | — | hayır | hayır | hayır |
| rapor-13 | 221-224 | H22 | 1.YARI AYAKTA, 2.YARI REJİM-DIŞI | — | — | hayır | hayır | hayır |
| rapor-13 | 226-229 | H23 | DARALDI | aynı | — | hayır | hayır | hayır |
| rapor-13 | 180-182 | — | — | ölçüm-bankı kalemi | rapor-9 C5 | hayır | hayır | evet |
| rapor-13 | 190-191 | — | — | bugün yapılabilir | kuyruk/olcum-banki.md; rapor-9 §7m3 | hayır | hayır | evet |
| rapor-13 | 196-203 | — | — | Katman-1 aday | KM1..KM8 | evet | hayır | KM8: evet |
| rapor-13 | 241-243 | — | — | ölçüm-bankı kalemi | rapor-11 KL10 | hayır | hayır | evet |
| rapor-13 | 302-306 | — | [D-ölçüm] | deterministik çağrı-kapısı 4.vakası | rapor-8; EK-4 | hayır | evet | hayır |
| rapor-13 | 313-315 | — | — | ingest borcu | rapor-12 | hayır | evet (ingest) | hayır |

### rapor-14
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-14 | 212-213 | H24 | İKİYE AYRILDI | 1.yarı DOĞRULANDI[D], 2.yarı DARALTILDI | — | hayır | hayır | hayır |
| rapor-14 | 215-216 | H25 | KISMEN DÜŞTÜ, YÖN DEĞİŞTİ | elle-ayar ayakta[D]; TAKVİM düştü | — | hayır | hayır | hayır |
| rapor-14 | 218-219 | H26 | ÜÇ MEKANİZMA AYAKTA, TERS-U DÜŞTÜ | atıf-bozulması[D], salınım[D], knob-overfit[D-teorik] | — | hayır | hayır | hayır |
| rapor-14 | 221-222 | H27 | 1.YARI AYAKTA, 2.YARI ŞARTLI, 3.YARI DÜŞTÜ | ε m.39-damgalı zorunlu | — | hayır | hayır | hayır |
| rapor-14 | 197-202 | — | — | Katman-1 aday (kod verilmemiş) | — | evet | hayır | hayır |

### rapor-15
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-15 | 148-153 | H29 | [D-belge] | DARALTILDI (çekirdek) | transkript 25:09-26:34 | hayır | hayır | hayır |
| rapor-15 | 256-258 | H28 | DARALTILDI | aynı | — | hayır | hayır | hayır |
| rapor-15 | 260-263 | H29 | KISMEN DÜŞTÜ / KISMEN DOĞRULANDI | aynı | — | hayır | hayır | hayır |
| rapor-15 | 265-268 | H30 | KISMEN DESTEKSİZ, KISMEN DÜZELTİLDİ | künye Ç14 | Ç14 | hayır | hayır | evet |
| rapor-15 | 270-272 | H31 | DESTEKLENDİ ve GÜÇLENDİ | MCP spec/CA DMV/FDA PCCP | — | hayır | hayır | hayır |
| rapor-15 | 216-229 | — | [D-belge, V26 doğrulandı] | Deterministik çağrı-kapısı 5 kalem | Claude Code izin dok.; Anthropic API; Ç13; 08-01 masa şerhi | hayır | evet (g15) | hayır |
| rapor-15 | 241-247 | — | — | Katman-1 aday (7 kalem — **F2: 8. kalem yok, F0'ın "8 adet" ifadesi hatalı**) | V46; core/sablonlar/; Salih 07-23; CA DMV/FDA PCCP; m.41/30-6; olcum-banki.md; Ç14 | evet | hayır | son 2 kalem: evet |

### rapor-16
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-16 | 214-217 | H32 | İLK YARISI AYAKTA · İKİNCİ ETİKETSİZ | aynı | — | hayır | hayır | hayır |
| rapor-16 | 219-222 | H33 | AYAKTA+GÜÇLENDİRİLDİ, düzeltmeyle | Wikipedia | — | hayır | hayır | hayır |
| rapor-16 | 224-227 | H34 | AYAKTA+GÜÇLENDİRİLDİ | Kaindl & Kainz; OSRM | — | hayır | hayır | hayır |
| rapor-16 | 229-232 | H35 | DARALDI (iki yandan) | aynı | — | hayır | hayır | hayır |
| rapor-16 | 153-162 | — | [hakem: Çift-14 DÜŞTÜ⇒ayrım kazandı] | öz-DÜZELTME≠öz-DOĞRULAMA | arXiv 2310.01798; 2402.08115 | hayır | hayır | hayır |
| rapor-16 | 296-303 | — | — | Katman-1 aday | KL16-1..KL16-8 | evet | hayır | KL16-8: evet |

### rapor-17
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-17 | 279-280 | H36 | DARALTILARAK DOĞRULANDI | ski-rental ekonomisi | — | hayır | hayır | hayır |
| rapor-17 | 282-284 | H37 | NİTEL DURUYOR, NİCEL DÜŞTÜ | büyüklük farkı yok | rapor-12 H19 | hayır | hayır | hayır |
| rapor-17 | 285-287 | H38 | DOĞRULANDI, farklı maddeyle | m.31/m.42 geri-alınabilirlik | — | hayır | hayır | hayır |
| rapor-17 | 288-290 | H39 | KOŞULLU DOĞRULANDI | ölçüt değil UYARI | — | hayır | hayır | hayır |
| rapor-17 | 295-299 | — | — | K-019 girdisi (5 satır) | — | hayır | evet (K-019) | biri evet |
| rapor-17 | 305-309 | — | — | K-016 girdisi (5 satır) | rapor-12 (biri) | hayır | evet (K-016) | biri evet |
| rapor-17 | 315-322 | — | — | Katman-1 aday (8 satır) | V47; rapor-12 H19; rapor-13 | evet | 2 satır: evet(K-019/K-016) | 2 satır: evet |

### rapor-18
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-18 | 326-328 | H40 | DARALTILARAK DOĞRULANDI | aynı | CCH Thm2,Lemma3[D]; arXiv:1002.1021 | hayır | hayır | hayır |
| rapor-18 | 329-332 | H41 | KOŞULLU DOĞRULANDI | koşul bugün sağlanmıyor | Geisberger 2008 §3.2; arXiv:2502.10519 §2.3 | hayır | hayır | hayır |
| rapor-18 | 333-334 | H42 | 1.YARI DÜZELTİLEREK DOĞRULANDI, 2.YARI DARALDI | — | CCH §1[D]; SODA'10 | hayır | hayır | hayır |
| rapor-18 | 336-337 / 297-306 | H43 | DOĞRULANDI (en sağlam kalem) | şart-zinciri (iii)⟸(ii) | §7 tablosu; M10 transkript[D-belge] | hayır | hayır | hayır |
| rapor-18 | 379-392 | — | — | Katman-1/Kanon/Kural adayları | KL18-1..KL18-14 | evet | hayır | hayır |

### rapor-19
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-19 | 287-288 | H44 | DOĞRULANDI [D] | iki daraltmayla | — | hayır | evet (#24) | hayır |
| rapor-19 | 290-291 | H45 | DARALTILDI [ÇİFT 7] | aynı | — | hayır | hayır | hayır |
| rapor-19 | 293-294 | H46 | DÜŞTÜ [ÇİFT 8] [X] | aynı | — | hayır | evet (m.37 çeşitlilik) | hayır |
| rapor-19 | 296-297 | H47 | KISMEN DOĞRULANDI [ÇİFT 12] | kritik düzeltmeyle | — | hayır | evet (A5) | hayır |
| rapor-19 | 243-275 | — | [D] | Katman-1 masası + ölçüm-bankı adayları | A1,A2,A3,K-a,K-b,K-e,M-a..M-e | evet | K-a/A1: evet(m.37); K-e/M-e: evet(A5) | M-c/M-d/A3: evet |
| rapor-19 | 65; 195-197 | — | — | A5 tasarım-paketi girdisi | T19 | hayır | evet (A5) | hayır |

### rapor-20 (+ EK-F, 671 satır tam)
| rapor_id | satır-aralığı | H# | damga | hüküm-tipi | künye | Katman-1-mi | iç-müşteri-mi | ölçüm-bankı-mı |
|---|---|---|---|---|---|---|---|---|
| rapor-20 | 311-315 | H48 | DARALTILARAK DOĞRULANDI | "gürültü-kısma öncülü sağlam" | arXiv:2410.05229; arXiv:2605.28700 | hayır | hayır | hayır |
| rapor-20 | 316-320 | H49 | DOĞRULANDI ve GÜÇLENDİRİLDİ | iki dik eksen | arXiv:2605.06445; 2602.03794; 2502.07266; 2311.10054 | hayır | hayır | hayır |
| rapor-20 | 321-326 | H50 | DOĞRULANDI(1.yarı)+KOŞULLU(2.yarı) | pipeline koşulsuz yenmez | arXiv:2604.02460; 2503.13657[X]; 2502.08788; 2607.26922; 2607.18265; 2607.14119; IWSLT2024 | hayır | hayır | hayır |
| rapor-20 | 327-330 | H51 | MEKANİZMA AYAKTA, KAZANÇ ÖLÇÜLMEMİŞ | orkestratör-bağlam-hijyeni | arXiv:2507.02778; 2310.01798; 2408.00989; Anthropic; 2406.02818 | hayır | hayır | hayır |
| rapor-20 | 407-415 | — | — | Katman-1 aday | K1-a..K1-i | evet | K1-a/b/c/e/f: evet(masa) | hayır |
| rapor-20 | 562-569 | H48,H50 | çeşitli [D-belge]/[D-ölçüm] | EK-F yeni künyeler (V26 ile doğrulanmış) | arXiv:2601.12307; 2607.03615; 2510.08623; 2510.22251; 2604.02547; 2302.00093; 2509.21051; 2406.02818/2401.14887/2604.02460 | hayır | hayır | hayır |
| rapor-20 | 617-620 | H48,H49,H50,H51 | EK-F güncellemesi (damga AYNI, dayanak eklendi) | EK-F güncelleme | EK-F güncelleme | hayır | hayır | hayır |
| rapor-20 | 647-652 | — | — | Katman-1 aday (EK-F) | K1-j..K1-o | evet | hayır | hayır |
| rapor-20 | 380 | — | — | ölçüm-bankı kalemi adayı | "sayı-sadakati≫mekanizma-sadakati" | hayır | hayır | evet |
| rapor-20 | 513 | H50 | — | numara-çakışması-bayrağı | rapor-10; V28 emsali | hayır | hayır | hayır |

---

## KAPANIŞ: model beyanları + vekil maliyet

**Orkestratör model beyanı:** bu koşumu yöneten Carvis alt-orkestratör `claude-sonnet-5` (Sonnet 5) üzerinde koştu. Fallback/model-düşüm işareti görülmedi.

**Alt-ajan model beyanı:** F0 (13), F1 (5), F2 (1) — toplam **19 alt-ajan**, tamamı `claude-sonnet-5` (emrin F0-Sonnet + F1/F2-emir-düzeyi-seçim şartına uyularak hepsi Sonnet sınıfında koşuldu; masa ③-a kararı ve #24 pini gereği). Tek dalga — hiçbir alt-ajan kendi alt-ajanını açmadı. Toplam web araması = 0 (emir gereği kapalıydı, uyuldu).

**Vekil maliyet (token toplamları, alt-ajan bazlı):**

| Faz | Ajan sayısı | Token toplamı | Tool-call toplamı |
|---|---|---|---|
| F0 (13 rapor okuyucu) | 13 | 883.979 | 25 |
| F1 (5 lens sentezcisi) | 5 | 577.679 | 40 |
| F2 (1 sınır-denetçisi) | 1 | 97.016 | 39 |
| **TOPLAM** | **19** | **1.558.674** | **104** |

**F0 içi dağılım:** rapor-8: 62.660 · rapor-9: 52.467 · rapor-10: 67.748 · rapor-11: 67.692 · rapor-12: 59.953 · rapor-13: 71.631 · rapor-14: 58.581 · rapor-15: 63.088 · rapor-16: 67.508 · rapor-17: 66.665 · rapor-18: 70.962 · rapor-19: 71.829 · rapor-20: 103.195 (en büyük — EK-F dahil 671 satır).

**F1 içi dağılım:** Lens-1(H-tablosu): 46.334 · Lens-2(Katman-1 dedup): 47.758 · Lens-3(iç-müşteri): 29.636 · Lens-4(çelişki): 170.562 · Lens-5(ölçüm-bankı): 283.389. **Lens-4 ve Lens-5'in token tüketimi diğer üç lensin toplamından (123.728) daha yüksek** — bu da §6'daki tool-call gözlemiyle (16 ve 24 ham-dosya erişimi) tutarlı: ham metne inen lensler orantısız pahalı çıktı.

**Bu dosyanın kendisi (F3-öncesi mekanik derleme) bu koşumun orkestratörü tarafından, yeni ajan çağrısı yapılmadan, F0/F1/F2 çıktılarının derlenmesiyle üretildi.**

**Kapanış beyanı:** Karar VERİLMEDİ · kanon yazılmadı (`core/`, `CLAUDE.md`, `kuyruk/`, pano/kapsül dokunulmadı) · git komutu ÇALIŞTIRILMADI · Katman-1 kalemleri yalnız LİSTELENDİ · F3 (Carvis compile + m.16 çelişki taraması + kanon-aday paketleme) bu dosyada YAPILMADI, ana-sıraya bırakıldı. Yazılan tek yüzey: `raporlar/2026-08-01-ingest-grafhatti.md`.
