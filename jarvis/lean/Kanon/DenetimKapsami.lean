/-
Kanon.DenetimKapsami — denetim kapsamı (iş düzlemi / kişi düzlemi; tüzük m.28) ve ayıklık testi yasağı (damga "beyansız"; tüzük m.33),
Lean 4 kod tabanı. Karar 117 parti 4, 2026-10-17. Uygulayan kod: yok (Jarvis'in elle uyguladığı kurallar);
denetçi modeli ve durum kodları Kanon.CeliskiKapisi'nde, burada tekrarlanmaz.
Türkçe özet (geri-çeviri): denetçi raporu iki parçalıdır. İş düzlemi yalnız işin kendi ölçütünü taşır (commit, test, kart yaşı) ve
temiz tutulur; kişi düzlemi bir karantina bölgesidir, kişi-yorumu eğilimi oraya akıtılır, iş düzlemine sızamaz, yalnız Salih okur
(okumayabilir), düşük bütçeyle çalışır. Psikolog rolü yasaktır. Ayıklık/HI sorgusu hiçbir yüzeyde yapılmaz, damga için üsteleme
yoktur; damga yalnız gönüllü beyanla dolar, beyan yoksa "beyansız" yazılır ve kararın statüsü düşmez.
-/
namespace Kanon.DenetimKapsami

/-! ## Bölüm 1 — m.28: denetim kapsamı -/

/-- Rapor düzlemi: iş (Jarvis'in işi) ya da kişi (karantina). -/
inductive Duzlem | is | kisi
  deriving Repr, DecidableEq

/-- İş düzlemine girebilen ölçüt türleri (m.28 a: commit, test, kart yaşı). -/
inductive Olcut | commit | test | kartYasi | kisiYorumu
  deriving Repr, DecidableEq

/-- Bir ölçüt işin kendi ölçütü mü. -/
def isOlcutu : Olcut → Bool
  | .kisiYorumu => false
  | _ => true

/-- Bir içeriğin hangi düzleme yazılacağı: kişi-yorumu eğilimi kişi düzlemine akar, işin ölçütü iş düzlemine. -/
def duzlemeAkis (o : Olcut) : Duzlem :=
  if isOlcutu o then .is else .kisi

/-- İş düzlemine giriş: yalnız işin kendi ölçütü girer. -/
def isDuzlemineGirer (o : Olcut) : Bool := duzlemeAkis o == .is

/-- Denetlenenler: Salih + Jarvis + tüm Jarvis (m.28). -/
inductive Denetlenen | salih | jarvis | jarvisAltAjanlar
  deriving Repr, DecidableEq

/-- Kişi düzlemini okuyabilen: yalnız Salih. -/
def kisiDuzlemiOkuyabilir : String → Bool
  | "Salih" => true
  | _ => false

/-- Kişi düzlemi bütçe sınıfı: ucuz (düşük token×zaman). -/
inductive Butce | dusuk | normal
  deriving Repr, DecidableEq

def duzlemButcesi : Duzlem → Butce
  | .kisi => .dusuk
  | .is => .normal

/-- Kişi düzlemi bir karantina bölgesidir, meşru analiz alanı değil (psikolog-rol yasağı, m.23 geçerli). -/
def kisiDuzlemiAnalizAlani : Bool := false

/-- Rapor yapısı: iki parça; kişi parçası boş olabilir (Salih okumayabilir). -/
structure DenetimRaporu where
  isOlcutleri   : List Olcut
  kisiIcerigi   : List Olcut
  deriving Repr

/-- Rapor geçerli: iş parçasında yalnız işin ölçütü var. -/
def raporGecerli (r : DenetimRaporu) : Bool := r.isOlcutleri.all isOlcutu

/-- Kişi-yorumu iş düzlemine giremez. -/
theorem kisiYorumuIsDuzlemineGirmez : isDuzlemineGirer .kisiYorumu = false := by
  decide

/-- İş düzlemine girebilen her ölçüt işin kendi ölçütüdür. -/
theorem isDuzlemineGirenIsOlcutudur (o : Olcut) (h : isDuzlemineGirer o = true) :
    isOlcutu o = true := by
  cases o <;> simp_all [isDuzlemineGirer, duzlemeAkis, isOlcutu]

/-- Kişi düzlemini Salih'ten başkası okuyamaz. -/
theorem kisiDuzlemiYalnizSalih (k : String) (h : kisiDuzlemiOkuyabilir k = true) : k = "Salih" := by
  unfold kisiDuzlemiOkuyabilir at h
  split at h <;> simp_all

/-! ## Bölüm 2 — m.33: ayıklık testi yasağı, damga "beyansız" -/

/-- Damga alanı: yalnız gönüllü beyanla dolar; yoksa "beyansız". -/
inductive Damga | beyanli (deger : String) | beyansiz
  deriving Repr, DecidableEq

/-- Yüzeyin ayıklık/HI sorgusu yapıp yapmadığı ve damga için üsteleme olup olmadığı. -/
structure Yuzey where
  ayikliksorgusu : Bool   -- yasak: her yüzeyde (mobil dahil) false olmalı
  ustelemeVar    : Bool   -- yasak: tekrar-sorma false olmalı
  deriving Repr

/-- Yüzey kuralı ihlal etmez. -/
def yuzeyUygun (y : Yuzey) : Bool := !y.ayikliksorgusu && !y.ustelemeVar

/-- Damga: gönüllü beyan varsa o, yoksa "beyansız". -/
def damgaYaz : Option String → Damga
  | some d => .beyanli d
  | none => .beyansiz

/-- Karar statüsü (m.16: ne derse emirdir). -/
inductive Statu | emir | dusuk
  deriving Repr, DecidableEq

/-- Statü damgadan bağımsızdır: beyansız ya da beyanlı (high/ayık fark etmez) statü düşmez. -/
def statu (_ : Damga) : Statu := .emir

-- Tek fren çelişki kapısıdır (Kanon.CeliskiKapisi.dal); modül bağımsız derlendiği için burada yeniden tanımlanmaz.

/-- Beyan yoksa damga "beyansız" olur. -/
theorem beyanYoksaBeyansiz : damgaYaz none = .beyansiz := rfl

/-- Beyansız damga statüyü düşürmez. -/
theorem beyansizStatuDusurmez : statu .beyansiz = .emir := rfl

/-- Hiçbir damga değeri statüyü düşürmez. -/
theorem damgaStatuDusurmez (d : Damga) : statu d = .emir := rfl

/-- Ayıklık sorgusu yapan ya da üsteleyen yüzey uygun değildir. -/
theorem sorguYapanUygunDegil (y : Yuzey) (h : y.ayikliksorgusu = true) : yuzeyUygun y = false := by
  simp [yuzeyUygun, h]

end Kanon.DenetimKapsami
