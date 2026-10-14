/-
Kanon.SkillKapi — skill-üretim kapı ağacı (K0 → K1 → [inşa] → K2 → K3 → yaprak), Lean 4 kod tabanı.
Kaynak metin: core/skill-uretim-semasi.md §1-§2 (v1, 2026-08-15; m.38 lojik formu). Karar 112 sonrası md → kod pilotu
(Salih 2026-10-14: "lojik forma çevrilmiş dosyalar artık lean 4 yoluyla kod tabanlı olmalı").
Ayrım: girdiler (Aday alanları) ölçümdür; deterministik olanları `kapi-denetim.py` üretir (R, F1-F4, tür-özel bayraklar),
yargı olanları (Y1-Y3, İ, P, F5, şekil) hakem ya da Jarvis verir. Hüküm (karar ağacı) yalnız burada hesaplanır.
-/
namespace Kanon.SkillKapi

/-- Adayın kapı girdileri. Her alan tek bir ölçüm; sayısal eşik karşılaştırmaları (k_W ≥ k_τ, değer payı) burada. -/
structure Aday where
  kapsanmisTam    : Bool := false  -- ∃ s∈H: tetik(s) ⊇ tetik(a) ∧ çıktı(s) ⊇ çıktı(a)
  kapsanmisKismi  : Bool := false  -- tetik(s) ⊇ tetik(a) ∧ çıktı(s) ⊉ çıktı(a) → yaprak EVRİM
  y1              : Bool := false  -- baseline-boşluk
  y2              : Bool := false  -- kanon-kuralı LAZY
  y3              : Bool := false  -- araç-zinciri (|adım| ≥ 3 ∧ sıra sabit)
  kW              : Nat  := 0      -- son W penceredeki tekrar sayısı
  kTau            : Nat  := 3      -- beyan eşiği (Karar 78)
  deltaBilinmiyor : Bool := true   -- Δ̂ inşa öncesi bilinmiyor
  degerYeter      : Bool := false  -- k_W·Δ̂ ≥ (1+β)·C_inşa (rasyonel hesap çağıranda)
  salihEmri       : Bool := false  -- Z2: Katman-1 emir
  r               : Bool := false  -- referans-varlığı (deterministik)
  i               : Bool := false  -- iddia-topraklama (bağımsız doğrulayıcı)
  p               : Bool := false  -- kalite kontrolü yalnız prompt talimatı mı (istenen: ¬P)
  rituel          : Bool := false  -- T-R
  orkestrator     : Bool := false  -- T-O
  yanEtkili       : Bool := false  -- T-Y
  f1 : Bool := false
  f2 : Bool := false
  f3 : Bool := false
  f4 : Bool := false
  f5 : Bool := false
  turOzel : Bool := false          -- birincil şekle göre tür-özel koşullar
  deriving Repr

inductive Sekil | rituel | orkestrator | yanEtkili | uretici
  deriving Repr, DecidableEq

inductive Yaprak | yeni | evrim
  deriving Repr, DecidableEq

inductive Hukum
  | ret0
  | beklet
  | onar2
  | onar3
  | uret (s : Sekil) (y : Yaprak)
  deriving Repr, DecidableEq

/-- K0 := ¬kapsanmış(a,H) ∧ (Y1 ∨ Y2 ∨ Y3) -/
def k0 (a : Aday) : Bool := !a.kapsanmisTam && (a.y1 || a.y2 || a.y3)
/-- Z1 := k_W ≥ k_τ ∧ (Δ̂ bilinmiyor ∨ k_W·Δ̂ ≥ (1+β)·C_inşa) -/
def z1 (a : Aday) : Bool := decide (a.kW ≥ a.kTau) && (a.deltaBilinmiyor || a.degerYeter)
/-- K1 := Z1 ∨ Z2 -/
def k1 (a : Aday) : Bool := z1 a || a.salihEmri
/-- K2 := R ∧ İ ∧ ¬P -/
def k2 (a : Aday) : Bool := a.r && a.i && !a.p
/-- Şekil, first hit-policy: T-R > T-O > T-Y > T-Ü -/
def sekil (a : Aday) : Sekil :=
  if a.rituel then .rituel
  else if a.orkestrator then .orkestrator
  else if a.yanEtkili then .yanEtkili
  else .uretici
/-- K3 := F1 ∧ … ∧ F5 ∧ tür-özel -/
def k3 (a : Aday) : Bool := a.f1 && a.f2 && a.f3 && a.f4 && a.f5 && a.turOzel

/-- Kapı ağacı: ilk düşen kapı terminali verir; hepsi geçerse yaprak. -/
def hukum (a : Aday) : Hukum :=
  if !k0 a then .ret0
  else if !k1 a then .beklet
  else if !k2 a then .onar2
  else if !k3 a then .onar3
  else .uret (sekil a) (if a.kapsanmisKismi then .evrim else .yeni)

/-! ## Kanıtlanan özellikler (md metnindeki cümlelerin makine-denetimli hâli) -/

/-- "tam kapsama → RET-0" -/
theorem tam_kapsanan_ret (a : Aday) (h : a.kapsanmisTam = true) : hukum a = .ret0 := by
  simp [hukum, k0, h]

/-- Üretim hükmü ancak dört kapının hepsi geçince çıkar. -/
theorem uret_ise_kapilar (a : Aday) (s : Sekil) (y : Yaprak) (h : hukum a = .uret s y) :
    k0 a = true ∧ k1 a = true ∧ k2 a = true ∧ k3 a = true := by
  unfold hukum at h
  cases h0 : k0 a <;> cases h1 : k1 a <;> cases h2 : k2 a <;> cases h3 : k3 a <;> simp_all

/-- "Z2 (Salih emri) bütçeyi atlar; K2/K3 atlanmaz": referans yoksa emir olsa da üretim yok. -/
theorem emir_topraklamayi_atlamaz (a : Aday) (h : a.r = false) (s : Sekil) (y : Yaprak) :
    hukum a ≠ .uret s y := by
  intro hu
  have := (uret_ise_kapilar a s y hu).2.2.1
  simp [k2, h] at this

/-- "kapı prompt'la kurulmaz" (¬P): kalite kontrolü yalnız talimatsa üretim yok. -/
theorem prompt_kapisi_uretmez (a : Aday) (h : a.p = true) (s : Sekil) (y : Yaprak) :
    hukum a ≠ .uret s y := by
  intro hu
  have := (uret_ise_kapilar a s y hu).2.2.1
  simp [k2, h] at this

/-- Z2: eşik altı tekrar + Salih emri → K1 geçer. -/
theorem emir_degeri_gecirir (a : Aday) (h : a.salihEmri = true) : k1 a = true := by
  simp [k1, h]

/-- Şekil önceliği: ritüel bayrağı varsa başka bayraklar ne olursa olsun şekil ritüeldir. -/
theorem rituel_once (a : Aday) (h : a.rituel = true) : sekil a = .rituel := by
  simp [sekil, h]

/-! ## Metin kodlaması (çağıranlar için sabit sözlük) -/

def Sekil.kod : Sekil → String
  | .rituel => "R" | .orkestrator => "O" | .yanEtkili => "Y" | .uretici => "Ü"

def Hukum.kod : Hukum → String
  | .ret0 => "RET-0"
  | .beklet => "BEKLET"
  | .onar2 => "ONAR-2"
  | .onar3 => "ONAR-3"
  | .uret s .yeni => s!"ÜRET-{s.kod}-yeni"
  | .uret s .evrim => s!"ÜRET-{s.kod}-evrim"

/-- Satır biçimi `anahtar=değer` (Bool: true/false/1/0, Nat: ondalık). Bilinmeyen anahtar → hata. -/
def oku (girdi : String) : Except String Aday := do
  let mut a : Aday := {}
  for ham in girdi.splitOn "\n" do
    let satir := ham.trimAscii.toString
    if satir.isEmpty || satir.startsWith "#" then continue
    match satir.splitOn "=" with
    | [k, v] =>
      let k := k.trimAscii.toString
      let v := v.trimAscii.toString
      let b : Except String Bool :=
        if v == "true" || v == "1" then .ok true
        else if v == "false" || v == "0" then .ok false
        else .error s!"{k}: Bool beklenirken '{v}'"
      let n : Except String Nat := match v.toNat? with
        | some x => .ok x
        | none => .error s!"{k}: Nat beklenirken '{v}'"
      match k with
      | "kapsanmisTam" => a := { a with kapsanmisTam := ← b }
      | "kapsanmisKismi" => a := { a with kapsanmisKismi := ← b }
      | "y1" => a := { a with y1 := ← b }
      | "y2" => a := { a with y2 := ← b }
      | "y3" => a := { a with y3 := ← b }
      | "kW" => a := { a with kW := ← n }
      | "kTau" => a := { a with kTau := ← n }
      | "deltaBilinmiyor" => a := { a with deltaBilinmiyor := ← b }
      | "degerYeter" => a := { a with degerYeter := ← b }
      | "salihEmri" => a := { a with salihEmri := ← b }
      | "r" => a := { a with r := ← b }
      | "i" => a := { a with i := ← b }
      | "p" => a := { a with p := ← b }
      | "rituel" => a := { a with rituel := ← b }
      | "orkestrator" => a := { a with orkestrator := ← b }
      | "yanEtkili" => a := { a with yanEtkili := ← b }
      | "f1" => a := { a with f1 := ← b }
      | "f2" => a := { a with f2 := ← b }
      | "f3" => a := { a with f3 := ← b }
      | "f4" => a := { a with f4 := ← b }
      | "f5" => a := { a with f5 := ← b }
      | "turOzel" => a := { a with turOzel := ← b }
      | _ => throw s!"bilinmeyen anahtar: {k}"
    | _ => throw s!"satır 'anahtar=değer' değil: {satir}"
  return a

end Kanon.SkillKapi
