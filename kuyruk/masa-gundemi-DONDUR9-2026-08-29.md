# Masa Gündemi — ⑨ DONDUR AÇILIŞI (2026-08-29)

*Künye: EK-6 külliyatının S2 hükmüyle dondurulan ⑨ "diğer" kümesinin açılış envanteri. Kaynak kod-listesi: `raporlar/2026-08-01-ingest-grafhatti.md` §2.3 madde 9; tam metinler cc/rapor-2026-08-01-{9..20}.md. Açma tetiği: Salih beyanı bu seansta ("mevcut önemli karar borçları bitince" şartı doldu — masa kuyruğu 08-29 Karar 78 ile boşaldı; kapsül + `kuyruk/masa-gundemi-EK6-2026-08-20.md` satır 21).*

**Sayım düzeltmesi (m.39):** §2.3 "~95 satır" F1-TAHMİNİYDİ; kod-listesinin deterministik sayımı **64 kalem** (aşağıda tam döküm). Fark: ~95 ham-satır bazlıydı, kod başına birden çok satır düşüyor. Bu envanter o teyit sayımıdır.

**Külliyat şerhi (baki, EK-6 künyesinden):** F2 denetimi 3/34 TUTMADI + 1 icat-rakam — kalemler DENETİMLİ okunur; her kalem masaya gelmeden kaynağından teyit edilir.

**Durum etiketleri:** `ÇO-BEKLİYOR` = çapraz-okuma turu bekliyor (İB-14 usulü: bugünkü kanonla ABSORBE/AÇIK hükmü) · `ABSORBE-ADAY` / `SÜPERSEDE-ADAY` = güçlü emare var, kanıt pointer'lı, hüküm Salih'te · `BİRLEŞİK` = başka kalemle aynı satır.

## Envanter (64 kalem)

### rapor-9 — V39/ölçek-eşiği ailesi (4)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R9-K1 | Ex-ante tahmin sütunları V39 4-tuple'ına (kayıt-şeması; m.37 v2 yürürlük çakışma riski) | rapor-9:148 | BİRLEŞİK → R11-KL9/R16-KL16-6 ailesi; ÇO-BEKLİYOR |
| R9-K2 | "Kalite ≥ eşik" bandı: kısıt (RCSP) mi skalerleştirme ağırlığı mı | rapor-9:149 | ÇO-BEKLİYOR |
| R9-K3 | Ölçek-eşiği ölçütüne "done makine-ölçülebilir mi" ekseni | rapor-9:150 | ÇO-BEKLİYOR (m.25 V47 şerhi Karar 78'de girdi — kısmi örtüşme kontrolü) |
| R9-K5 | `kosum-maliyeti.py` dedup kusurunun kapatılması | rapor-9:152 | ÇO-BEKLİYOR (araç güncel durumu denetlenecek) |

### rapor-10 — mek-yorum/koşum-statüsü (7)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R10-K1 | Bütçe-tavanı ↔ m.40b kontratı çelişkisi (a/b/c/d seçenekleri) | rapor-10:229 | SÜPERSEDE-ADAY — KB-27 paketi + Karar 74 M-4 + İB-54 deterministik fren aynı sorunu işledi |
| R10-K2 | Bu raporun statüsü: "tam diyalektik" sayılmama hükmü | rapor-10:230 | ÇO-BEKLİYOR |
| R10-K3 | V39 tek-nokta değişimi ≡ activation patching şerh adayı | rapor-10:231 | ÇO-BEKLİYOR |
| R10-K4 | "Yüksek trafik ≠ yüksek değer" wiki eki (kritik karar-noktası) | rapor-10:232 | ÇO-BEKLİYOR (wiki kuyruğu İB-04 ile kesişim) |
| R10-K5 | "Karar-noktası kalitesi ablasyon-görelidir" tanım duruşu | rapor-10:233 | ÇO-BEKLİYOR |
| R10-K7 | Verbatim-alıntı enflasyonu: ajan promptuna bölüm-kaynağı satırı | rapor-10:235 | BİRLEŞİK → R18-KL18-14; ÇO-BEKLİYOR |
| R10-K8 | Wiki adayları: süperpozisyon · QK/OV · attribution graph · attention sink | rapor-10:236 | ÇO-BEKLİYOR (İB-04 kesişim) |

### rapor-11 — ufuk/partisyon ailesi (7)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R11-KL1 | "Ufuk" kelimesinin iki anlamı (m.22 menzili ↔ hedef/vizyon) ayrıştırma | rapor-11:296 | ÇO-BEKLİYOR |
| R11-KL2 | m.22 gerilimi: sıcak bağlam bağlam-başına mı global mi (A/B/C) | rapor-11:297 | ÇO-BEKLİYOR |
| R11-KL3 | Dört partisyon ekseninin (P/G/S/K-010) birleştirilmesi | rapor-11:298 | ÇO-BEKLİYOR |
| R11-KL4 | Kenar türü: zorunlu kenar ∧ tavsiye kenarı ayrımı şablona | rapor-11:299 | BİRLEŞİK → R16-KL16-7; ÇO-BEKLİYOR |
| R11-KL5 | "Ufuk = Y hedef-bandı" V46'ya yazımı | rapor-11:300 | BİRLEŞİK → R16-KL16-4; ÇO-BEKLİYOR |
| R11-KL6 | İlerleme göstergesi biçimi: fark (Goodhart-dışı) mı skor mu | rapor-11:301 | ÇO-BEKLİYOR |
| R11-KL9 | Tahmin-vs-gerçek satırı ≡ rapor-9 ex-ante önerisi (AYNI KALEM) | rapor-11:304 | BİRLEŞİK → R9-K1/R16-KL16-6; ÇO-BEKLİYOR |

### rapor-12 — skill doğum/emeklilik ailesi (7)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R12-K1-1 | m.43'e emeklilik fıkrası eklenmesi | rapor-12:271 | ÇO-BEKLİYOR (m.43 Karar 78'de 2. rev aldı — emeklilik fıkrası içeriyor mu denetlenecek) |
| R12-K1-2 | "Emeklilik = arşiv, silme değil" m.8 altına açık yazım | rapor-12:272 | ÇO-BEKLİYOR |
| R12-K1-3 | Doğum tetiğine "takılma" (impasse) yolu (D5) | rapor-12:273 | ÇO-BEKLİYOR |
| R12-K1-4 | Küçük-N'de otomatik emeklilik KURULMAMASI kararının kaydı (E2) | rapor-12:274 | ÇO-BEKLİYOR |
| R12-K1-5 | Ayırt-edilebilirlik ölçütünün KILAVUZ'a girmesi (D1) | rapor-12:275 | ÇO-BEKLİYOR |
| R12-K1-6 | Üç-faz şablonunun taşınmadığı bulgusunun kaydı (V41 yerleştirme) | rapor-12:276 | ÇO-BEKLİYOR |
| R12-K1-7 | Kaçırılan-tetik eşiği n≥3 (rapor-25 devri; m.43 eşiği yorumu) | rapor-12:277 | ABSORBE-ADAY — m.43 2. rev (Karar 78: birim=GÖREV, N=3) aynı eşiği hükme bağladı |

### rapor-13 — ufuk-etiketi/keşif ailesi (7)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R13-KM1 | Pano/kuyruk şemasına "hizmet ettiği ufuk(lar)" alanı | rapor-13:196 | ÇO-BEKLİYOR |
| R13-KM2 | `karar-modeli` skill'ine 5. eksen (ufuğa-katkı) | rapor-13:197 | BİRLEŞİK → R14-1 (ε ekseni); ÇO-BEKLİYOR |
| R13-KM3 | Keşif kotası açık yazımı ("vardiyanın X kadarı ufuk-bağımsız") | rapor-13:198 | ÇO-BEKLİYOR |
| R13-KM4 | Ufuk listesi kapalı mı açık mı ("hiçbir ufka hizmet etmiyor" sınıfı) | rapor-13:199 | ÇO-BEKLİYOR |
| R13-KM5 | Hedef-yönü ekseni ↔ m.36 öncelik: iki eksen mi tek sıra mı | rapor-13:200 | ÇO-BEKLİYOR |
| R13-KM6 | h-kaynağı seçimi (a-e; envanter verildi, seçim verilmedi) | rapor-13:201 | ÇO-BEKLİYOR |
| R13-KM7 | Raporun antitez+hakemlik borcu (~$4-5 sınıfı) | rapor-13:202 | ÇO-BEKLİYOR |

### rapor-14 — ε/ayar-politikası ailesi (6, kodsuz — §5.2 sıra no)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R14-1 | ε'nin varlığı ve yeri (karar-modeli 5. eksen; m.37 v2 kapısı ardında) | rapor-14 §5.2/1 | BİRLEŞİK → R13-KM2; ÇO-BEKLİYOR |
| R14-2 | Ayar-politikası biçimi: takvim mi tetik mi (koşum hükmü: tetik) | rapor-14 §5.2/2 | ÇO-BEKLİYOR |
| R14-3 | İzleme-varlığı kararı (sapma göstergesi ε'den önce) | rapor-14 §5.2/3 | ÇO-BEKLİYOR |
| R14-4 | V39 ŞERH 2 ">%5 kapısı" anlamının yazılması (anlamlılık/etki) | rapor-14 §5.2/4 | ÇO-BEKLİYOR |
| R14-5 | Ölçüm-bankı ε-satırına iki zorunlu alan (gürültü bandı + önceden-yazılı kural) | rapor-14 §5.2/5 | ÇO-BEKLİYOR (ölçüm-bankı 08-29'da DE-GOLD'a süpersede — Karar 78 F7 kesişimi) |
| R14-6 | K-020 sınır notu: ε deneyi successive-halving'e uygun ilk vaka değil | rapor-14 §5.2/6 | ÇO-BEKLİYOR |

### rapor-15 — A1-kalibrasyon/güvenlik ailesi (3)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R15-a | A1 kapısının kalibrasyonu: Salih 07-23 şerhi (N=5→>%55) = rule of three | rapor-15:243 | ÇO-BEKLİYOR |
| R15-b | A1-A4'e terfi protokolü: CA DMV faz-kilidi + FDA PCCP deseni | rapor-15:244 | ÇO-BEKLİYOR |
| R15-c | Deny-kilit gözden geçirme: "deny istisna taşıyamaz" ↔ m.41 kilit tasarımı | rapor-15:245 | ÇO-BEKLİYOR |

### rapor-16 — çift-cephe ailesi (5)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R16-KL16-1 | "Yön" kelimesinin iki anlamı (m.40b karşıt-yön ↔ zaman-yönü) | rapor-16:296 | ÇO-BEKLİYOR |
| R16-KL16-3 | Terim kararı: "üretim-cephesi ↔ gereklilik-cephesi" kanonlaşması | rapor-16:298 | ÇO-BEKLİYOR |
| R16-KL16-4 | Çift-faz loop yazım formu V46'ya (KL5 ile BİRLEŞTİRİLMELİ) | rapor-16:299 | BİRLEŞİK → R11-KL5; ÇO-BEKLİYOR |
| R16-KL16-6 | "İlk plan = bitti değil" kapanış protokolüne (KL9 ile AYNI KALEM) | rapor-16:301 | BİRLEŞİK → R11-KL9/R9-K1; ÇO-BEKLİYOR |
| R16-KL16-7 | Partisyonların çift-cephe işaretlemesi (KL4 devamı) | rapor-16:302 | BİRLEŞİK → R11-KL4; ÇO-BEKLİYOR |

### rapor-18 — koşum-disiplini ailesi (12)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R18-KL18-1 | Koşum-ortası maliyet ölçümü zorunluluğu / eşzamanlı-ajan sigortası | rapor-18:379 | ABSORBE-ADAY — İB-54 fren paketi (PreToolUse sayaç-hook warn 36/stop 72 + workflow brake, commit f106319) |
| R18-KL18-3 | H40 daraltılmış kaydı: soyutlama izni garanti ile lisanslanır | rapor-18:381 | ÇO-BEKLİYOR |
| R18-KL18-4 | rapor-16 §5.2 kalibrasyonu: "tepede buluşma" → "en yüksek rank'li düğüm" | rapor-18:382 | ÇO-BEKLİYOR |
| R18-KL18-5 | Ç3 ayrımı kaydı: stall-on-demand ≠ kısayol | rapor-18:383 | ÇO-BEKLİYOR |
| R18-KL18-6 | B1-B6 kapsama boşlukları kapatma kuyruğu (kural var, mekanizma yok sınıfı) | rapor-18:384 | ÇO-BEKLİYOR (B1=m.43 sayacı: Karar 78 + İB-60 loop-dedektör kesişimi) |
| R18-KL18-7 | Envanter ölçütü: "kaç skill" değil "tipik iş kaç kaleme bakıyor" | rapor-18:385 | ÇO-BEKLİYOR |
| R18-KL18-8 | m.39 ağırlaştırma: "kaç kat" rakamları optimal-kıyaslı değil; 1900×→2.5× kullanılmaz | rapor-18:386 | ÇO-BEKLİYOR |
| R18-KL18-9 | "Yanlış-pozitif/negatif" terim çifti yerine "hangi yönde yanılır" | rapor-18:390 | ÇO-BEKLİYOR |
| R18-KL18-10 | Bu koşumun hakemlik borcu (Aşama-3 koşulmadı; Ç1/Ç2/Ç3 doğrulaması) | rapor-18:391 | ÇO-BEKLİYOR |
| R18-KL18-11 | Emir-kapsamı dersi: sentez emirlerinde kapsam freni erken | rapor-18:392 | ÇO-BEKLİYOR |
| R18-KL18-13 | Sağlamlık mekanizması kaydı: envanter yerleşimi talepten değil yapı-darboğazından | rapor-18:389 | ÇO-BEKLİYOR |
| R18-KL18-14 | Ham-metin kuralı: özet-katmanı alıntısı ham eşleşmeden [D] alamaz (atlas-kosum gotcha adayı) | rapor-18:387 | BİRLEŞİK → R10-K7; ÇO-BEKLİYOR (halusinasyon-paketi/atlas-kosum güncel metni denetlenecek) |

### rapor-19 — m.44/ölçüm ailesi (2)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R19-A2 | m.44 RouteLLM çapasına niteleyici şerh (%14→%95 MT-Bench'e özgü; MMLU %54) | rapor-19:273 | ÇO-BEKLİYOR (tüzük metni yalnız Salih) |
| R19-K-b | **KOD BULUNAMADI** — §2.3 "rapor-19 K-b" diyor; rapor-19'da K-e/M-e var, K-b taranamadı | rapor-19 (tüm) | BAYRAK — kaynak taraması borç (F2 şerhi sınıfı: kod-listesi hatası olabilir) |

### rapor-20 — pipeline/AI2AI ailesi (4)
| Kod | Kalem | Adres | Durum |
|---|---|---|---|
| R20-K1-d | Sınır-denetçisi (Inspector) deseni loop şablonuna; V26/V8/#26 ilişkisi | rapor-20:410 | ÇO-BEKLİYOR |
| R20-K1-g | Birleşik ingest'te monolit referans dilimi (varyant c) koşulsun mu | rapor-20:413 | ÇO-BEKLİYOR (İB-61 absorbe-teyit turu kesişimi) |
| R20-K1-i | Ucuz-model alt-ajana katı şema dayatmanın işareti ölçülmedi (şerh) | rapor-20:415 | ÇO-BEKLİYOR |
| R20-K1-m | #24 pin ↔ fiiliyat: atlas opus-pini 4 koşumda Sonnet'e indi; pin mi fiiliyat mı | rapor-20:650 | AÇIK — İB-09 (Yol-C ölçümü) bu kararın girdisi, İB-09 hâlâ açık |

## Sonraki adım (bu envanterin devamı)
1. **Çapraz-okuma turu (İB-14 usulü):** 64 kalem × bugünkü kanon → ABSORBE/AÇIK/BELİRSİZ, kanıt pointer'lı; BİRLEŞİK aileler tek kalem olarak işlenir (etkin kalem sayısı ~56). Çıktı bu dosyaya işlenir.
2. **Daraltılmış masa:** ÇO sonrası CANLI kalanlar EK-6 usulüyle (kalem başına açıklama-bloklu, ayrı oturum) Salih'e.
3. R19-K-b bayrağı: rapor-19 tam taraması.

*Hükümler Salih'te; bu dosya envanter + emare, karar değil (m.31).*
