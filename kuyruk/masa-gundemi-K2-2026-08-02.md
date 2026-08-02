# Masa Gündemi — K2 kalemleri (rapor 08-02-1 ingest'i; Katman-1, hepsi İMZASIZ)

*Kaynak: `cc/rapor-2026-08-02-1.md` §8 (tam gerekçe + karşı-taraf orada; m.20 pointer). Rapor KOŞULLU okunur: hakem 7/7 anlaşmazlıkta hiçbir tarafa SAĞLAM vermedi, 14 tez iddiasından 8'i çürüdü. Hakemin sentez uyarısı bu gündemin okuma kuralıdır: kalemler BAĞIMSIZ karar ister — paket-kabul ve paket-red ikisi de hatadır.*

## Öne çekilenler (rapor işareti ⭐)

| # | Kalem | Rapor yönü | Karşı-taraf (özet) |
|---|---|---|---|
| K2-a ⭐ | **BANT-DIŞI kural:** koşum promptu emrin kanonik adresi + SHA'sını taşır; koşucunun ilk adımı doğrulama, başarısızlıkta DUR | YAZ — 08-02'de fiilen çalışan tek koruma; şablon-içi alan bant-içidir, kapsamı arızayı örtmez (hakem Ç6) | Kısıt sayısı arttıkça takip bozuluyor (30-19:335 emsali) |
| K2-k ⭐ | **m.40b maskeli-hakem yapısal açığı:** üretici çıktısı çalışma ağacındayken maskeleme = ∅. Üç çare: (i) hakem depo-yetkisiz · (ii) çıktı hakem bitene dek scratchpad'de · (iii) sızıntı beyanı (bu koşumun yaptığı) | MASAYA — hangisi kanon, Salih | (i) kanıt-doğrulamasını öldürür — hakem tam o yetkiyle tezin cümlelerini teze karşı kullandı |
| K2-n ⭐ | **Damga kuralı:** dış künye arama-özetinden alınmışsa `[K]` ZORUNLU; `[D-belge]` yalnız WebFetch ile birincil metne inilmişse. Ölçülü gerekçe: özet katmanı = Haiku ($1,34/32 arama, 46:1 sıkıştırma) | MASAYA | Kural sıkılaşır ⇒ geçmiş damgalar geriye dönük denetime açılır (pahalı) |

## Ad + statü kararları

| # | Kalem | Rapor yönü | Karşı-taraf |
|---|---|---|---|
| K2-f | **"Üç dil" → "üç REGISTER + kenar-başına biçim"** — terminoloji daraldı (antitez H2), mimari değil | DÜZELT | "Üç dil" Salih'in kelimesi; değişiklik yalnız Salih (Katman-1 açık kaydı) |
| K2-g | compiler-formülü §4 hibridi → **"kıyasta kazanmış ∧ KOŞULMAMIŞ hipotez"** olarak yeniden damgalanır | DÜZELT — belge kendi §6.4'ünde zaten böyle diyor | Çözülmüş sayılan kenarı yeniden maliyetli kılar |
| K2-j | `[rejim: manuel-tempo]` etiketinin kanonlaşması | MASAYA | Yeni etiket = yeni bakım kalemi |

## Şablon alanları (E1) — TEK TEK, dördü birden değil (antitez şartı)

| # | Kalem | Rapor yönü |
|---|---|---|
| K2-b | "Emir konumu + erişim doğrulaması" alanı | EKLE — ama K2-a olmadan tek başına YETMEZ (bant-içi) |
| K2-c | done-yüklemi (makine formunda) alanı | EKLE — antitez bağımsız gerekçelendirdi |
| K2-d | tetik (D8) alanı — boş bırakılamaz | EKLE — g23 Ç1 kalemiyle BİRLEŞTİRİLEREK |
| K2-e | kısıt-profili C=(R,G) · devir-arayüzü I · sınır-denetçisi V | BEKLET — kısıt yükü ölçülmeden eklenmez |

## Ölçüm/sınama kalemleri

| # | Kalem | Not |
|---|---|---|
| K2-h | Ç-YENİ hakemliği (30-13:60 ↔ 30-16:251) | = B1; ~15 dk yerel, karşı-taraf yok |
| K2-i | dil-sınırı↔loop-sınırı çakışma hipotezi | = B4; kutuda aday, çürütme gücü var/doğrulama yok |
| K2-l | m.40b hayatta-kalma serisi (4 koşum üst üste 0 tez tam-sağlam) — g20 K1-h ile birleşik | HAFİF/TAM formlar karışık, yön aynı |
| K2-m | "Ölçüm kültürü arızası" (ikiliden kademeliye genişletme, 5 anlaşmazlıkta taraf-bağımsız; kök: sürekli sayaç yok) | Sistemik kalem; sayaç kurulumu kendisi m.43 arıza sınıfına açık |

## Yapısal karar (kalem üstü — HAT ayrımı, hakem Ç7)

**HAT-A (muhafızlar) ⊥ HAT-B (mimari):** E0 bant-dışı doğrulama + E4 ölçüm çıkarımı sıfır-token, ölçülmüş arızayı kapatır, mimariden BAĞIMSIZ ilerler. Compiler SINIFI seçimi N=0 kenarlarda BEKLER (önce 3-5 çeviri elle, tek ölçüt şekil-stabilitesi). İki hat paket değil — ayrı imza ister.
