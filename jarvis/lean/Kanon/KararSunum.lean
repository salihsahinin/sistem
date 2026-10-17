/-
Kanon.KararSunum — karar-sunum protokolü (tüzük m.40 (a)-(c) + çift-atlas ek fıkrası + koşum-sözleşmesi üçlüsü; Salih 2026-07-13, 07-19, 07-21, Karar 86 D3),
Lean 4 kod tabanı. Karar 117, 2026-10-17.
Türkçe özet (geri-çeviri): (a) ölçek-eşiği üstü karar 3-model sunulur (eşik = m.37 eşiği; su-bardağı alt-karar muaf). (b) Dışarıda çözülmüş
olma ihtimali olan karar (yeni mekanizma/araç/desen) için sunumdan önce dış tarama yapılır; iç-önceliklendirme muaf ama geriye-dönük denetlenir.
(c) İlk-çıktı-hızlı: iş düşük geriye-dönük-maliyetliyse ∨ Jarvis v1 varsa uygulanır; yüksek maliyetli ∧ v1 yoksa tasarım-öncelikli düzen sürer.
Araştırma raporu kanon-aday olur ⟺ tez ve antitez şeritleri tamam ∨ Salih muafiyeti; token baskısı beyanında kapsam eşik-üstü araştırmaya daralır.
Koşum sözleşmesi: hakem yazar olamaz ve yalnız veri alır; örneklemde ≥1 URL'siz iddia; işçi başına ≥2 birincil kaynak açılır.
-/
namespace Kanon.KararSunum

/-- (a) sunum biçimi. -/
inductive Sunum | ucModel | tekCozum
  deriving Repr, DecidableEq

def sunum (olcekEsigiUstu suDardagi : Bool) : Sunum :=
  if olcekEsigiUstu && !suDardagi then .ucModel else .tekCozum

/-- (b) kararın türü. -/
inductive KararTuru | yeniMekanizma | icOnceliklendirme
  deriving Repr, DecidableEq

/-- Dış tarama sunumdan önce zorunlu ⟺ dışarıda çözülmüş olma ihtimali olan karar. -/
def disTaramaZorunlu : KararTuru → Bool
  | .yeniMekanizma => true
  | .icOnceliklendirme => false

/-- İç-önceliklendirme muafiyeti geriye-dönük denetime tabidir (A7). -/
def geriyeDonukDenetim : KararTuru → Bool
  | .icOnceliklendirme => true
  | .yeniMekanizma => false

/-- (c) geriye-dönük-maliyet sınıfı (ölçüt: geri-alınabilirlik, m.31 ekseni). -/
inductive Maliyet | dusuk | yuksek
  deriving Repr, DecidableEq

inductive Duzen | ilkCiktiHizli | tasarimOncelikli
  deriving Repr, DecidableEq

def duzen (m : Maliyet) (jarvisV1 : Bool) : Duzen :=
  if m == .dusuk || jarvisV1 then .ilkCiktiHizli else .tasarimOncelikli

/-- Çift-atlas: araştırma kapsamı. Token-baskısı beyanı yok → tüm araştırmalar; var → yalnız ölçek-eşiği-üstü. -/
def atlasKapsaminda (tokenBaskisi olcekEsigiUstu : Bool) : Bool :=
  !tokenBaskisi || olcekEsigiUstu

/-- Rapor kanon-aday ⟺ iki şerit tamam ∨ Salih muafiyeti. -/
def kanonAday (tezTamam antitezTamam salihMuaf : Bool) : Bool :=
  (tezTamam && antitezTamam) || salihMuaf

/-- Hayatta-kalma kaydı (K2-l): her koşumda üçlü zorunlu. -/
inductive Hayatta | saglam | daraldi | dustu
  deriving Repr, DecidableEq

/-- Koşum-sözleşmesi üçlüsü (Karar 86 D3). -/
structure Kosum where
  hakemYazarmi      : Bool  -- hakem aynı koşumda sentezi/tezi yazdı mı
  hakemGirdisiVeri  : Bool  -- hakeme yalnız ölçülecek veri verildi (emir yazarı/beklentisi verilmedi)
  urlsizOrnek       : Nat   -- örneklemdeki URL'siz/model-hafızası iddia sayısı
  acilanKaynak      : Nat   -- işçinin fiilen açtığı birincil kaynak sayısı
  deriving Repr

def kosumGecerli (k : Kosum) : Bool :=
  !k.hakemYazarmi && k.hakemGirdisiVeri && decide (k.urlsizOrnek ≥ 1) && decide (k.acilanKaynak ≥ 2)

theorem yazar_hakem_olamaz (k : Kosum) (h : k.hakemYazarmi = true) : kosumGecerli k = false := by
  simp [kosumGecerli, h]

theorem yuksek_maliyet_v1siz_tasarim : duzen .yuksek false = .tasarimOncelikli := rfl

theorem su_dardagi_muaf : sunum true true = .tekCozum := rfl

end Kanon.KararSunum
