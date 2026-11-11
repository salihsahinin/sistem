/-
Kanon.AkisGraf — akış grafı ve seans kaydı sözleşmesi (Karar 121 + Karar 122, 2026-10-25; icra `jarvis/kod/durum`,
kütük `ortak/durum-olay.jsonl`, türevler `ortak/akis-graf.json` · `ortak/graf/akis-<alan>.d2` · `ortak/SALIH-OZET.md`).
Türkçe özet (geri-çeviri): sistemin işleri bir graftır. Düğüm = iş kaydı, hedef kaydı ya da seans (sohbet). Kenar = girdi
(bağımlılık), hizmet (iş → hedef), seansın açtığı/bitirdiği iş, seans → sonraki seans. Bir iş **sırada**dır ancak ve ancak
açıksa, iş türündeyse ve hiçbir girdisi açık/işlemde değilse. Seans açılışı konumu (graftaki yer) verir; seans kapanışı
beş soru + hedef yoklaması + Rust'ın ürettiği ölçümlerle yapılandırılmış kayıt üretir; kayıt tam değilse kapanış yoktur.
Claude JSON/graf okur; Salih tek md özetini (ASD-STE100 Türkçe) ve D2/SVG görselini okur. Kapsül/pano md artık yazılmaz.
-/
namespace Kanon.AkisGraf

inductive Durum | acik | islemde | tamam | tuketildi | bayat
  deriving Repr, DecidableEq

/-- Girdi bu durumdaysa bağımlı işi bloklamaz. -/
def Durum.blokAcar : Durum → Bool
  | .acik => false
  | .islemde => false
  | _ => true

inductive Tur | is | hedef
  deriving Repr, DecidableEq

structure Dugum where
  id     : Nat
  tur    : Tur := .is
  durum  : Durum
  girdi  : List Durum   -- girdilerin efektif durumları (katlanmış defterden)
  deriving Repr

/-- Sırada: açık ∧ iş ∧ bütün girdiler blok açar (durum crate `Defter::sirada`). -/
def sirada (d : Dugum) : Bool :=
  d.durum == .acik && d.tur == .is && d.girdi.all Durum.blokAcar

/-- Seans kapanış kaydı (Karar 121 beş soru + hedef yoklaması). Ölçümler Rust'tan gelir, burada yalnız varlığı. -/
structure SeansKaydi where
  hedef         : String
  hedefTutuldu  : Bool
  neDegisti     : List String
  kararlar      : List String
  adaylar       : List String
  sonrakiIlkIs  : List String
  yenidenAcma   : List String
  olcumVar      : Bool := false   -- durum seans-kapat ekler (git, durum sayaçları)
  deriving Repr

/-- Kayıt tam: hedef cümlesi boş değil ∧ sonraki ilk iş boş değil ∧ ölçüm eklenmiş. Beş sorunun diğerleri boş olabilir
(gerçekten değişen bir şey yoksa uydurulmaz, m.39). -/
def kayitTam (k : SeansKaydi) : Bool :=
  !k.hedef.isEmpty && !k.sonrakiIlkIs.isEmpty && k.olcumVar

/-- Seans kapanışı = kayıt tam ∧ kütüğe `seans_kapat` olayı düştü. -/
structure Kapanis where
  kayit      : SeansKaydi
  olayDustu  : Bool
  deriving Repr

def kapandi (k : Kapanis) : Bool := kayitTam k.kayit && k.olayDustu

/-- Okuyucu → biçim (Karar 121/122): Claude JSON ve graf metni okur; Salih md özet + D2/SVG. -/
inductive Okuyucu | claude | salih
  deriving Repr, DecidableEq
inductive Bicim | json | grafMetni | mdOzet | d2svg
  deriving Repr, DecidableEq

def bicimler : Okuyucu → List Bicim
  | .claude => [.json, .grafMetni]
  | .salih  => [.mdOzet, .d2svg]

theorem girdisi_acik_sirada_degil (d : Dugum) (h : Durum.acik ∈ d.girdi) : sirada d = false := by
  unfold sirada
  have : d.girdi.all Durum.blokAcar = false := by
    rw [List.all_eq_false]
    exact ⟨.acik, h, by decide⟩
  simp [this]

theorem hedef_sirada_degil (d : Dugum) (h : d.tur = .hedef) : sirada d = false := by
  simp [sirada, h]

theorem sonraki_is_bos_kapanis_yok (k : Kapanis) (h : k.kayit.sonrakiIlkIs = []) : kapandi k = false := by
  simp [kapandi, kayitTam, h]

theorem olcumsuz_kapanis_yok (k : Kapanis) (h : k.kayit.olcumVar = false) : kapandi k = false := by
  simp [kapandi, kayitTam, h]

theorem claude_md_okumaz : Bicim.mdOzet ∉ bicimler .claude := by decide
theorem salih_json_okumaz : Bicim.json ∉ bicimler .salih := by decide

end Kanon.AkisGraf
