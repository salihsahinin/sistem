import Kanon.SkillTetik

open Kanon.SkillTetik

/-- `tetik`: stdin `anahtar=değer` satırları → stdout hüküm. Kayıtlar `---` satırıyla ayrılır (her kayıt için bir satır).
`kapi=O` (varsayılan): Kapı-Ö girdileri (`Cagri` alanları) → reddet · iste · anaSiraya · atla · cagir.
`kapi=S`: Kapı-S girdileri (`Sonuc` alanları) → gecti · tekrar · failLoud.
Bool: true/false/1/0; Nat: ondalık; `kip` ∈ literal|ortuk|yasak; `cagiran` ∈ anaSira|salih|altAjan.
Çıkış: 0 hüküm üretildi · 2 girdi hatası (stderr). Rust/Python ile fark testi: `jarvis/kod/kural/tests/lean_fark.rs`. -/
def boolOku (k v : String) : Except String Bool :=
  if v == "true" || v == "1" then .ok true
  else if v == "false" || v == "0" then .ok false
  else .error s!"{k}: Bool beklenirken '{v}'"

def natOku (k v : String) : Except String Nat :=
  match v.toNat? with
  | some x => .ok x
  | none => .error s!"{k}: Nat beklenirken '{v}'"

def kayitCoz (kayit : String) : Except String String := do
  let mut kapi := "O"
  let mut c : Cagri := {}
  let mut s : Sonuc := {}
  for ham in kayit.splitOn "\n" do
    let satir := ham.trimAscii.toString
    if satir.isEmpty || satir.startsWith "#" then continue
    match satir.splitOn "=" with
    | [k, v] =>
      let k := k.trimAscii.toString
      let v := v.trimAscii.toString
      match k with
      | "kapi" => kapi := v
      | "skillVar" => c := { c with skillVar := ← boolOku k v }
      | "tetikDogru" => c := { c with tetikDogru := ← boolOku k v }
      | "dereceIfadesi" => c := { c with dereceIfadesi := ← boolOku k v }
      | "icIceDerinlik" => c := { c with icIceDerinlik := ← natOku k v }
      | "dalSayisi" => c := { c with dalSayisi := ← natOku k v }
      | "kip" =>
        match v with
        | "literal" => c := { c with kip := .literal }
        | "ortuk" => c := { c with kip := .ortuk }
        | "yasak" => c := { c with kip := .yasak }
        | _ => throw s!"kip: literal|ortuk|yasak beklenirken '{v}'"
      | "yanEtkili" => c := { c with yanEtkili := ← boolOku k v }
      | "cagiran" =>
        match v with
        | "anaSira" => c := { c with cagiran := .anaSira }
        | "salih" => c := { c with cagiran := .salih }
        | "altAjan" => c := { c with cagiran := .altAjan }
        | _ => throw s!"cagiran: anaSira|salih|altAjan beklenirken '{v}'"
      | "girdiTam" => c := { c with girdiTam := ← boolOku k v }
      | "tetikAracCiktisindan" => c := { c with tetikAracCiktisindan := ← boolOku k v }
      | "celiskiTemiz" => c := { c with celiskiTemiz := ← boolOku k v }
      | "alanlarTam" => c := { c with alanlarTam := ← boolOku k v }
      | "done" => s := { s with done := ← boolOku k v }
      | "semaVar" => s := { s with semaVar := ← boolOku k v }
      | "semaUyuyor" => s := { s with semaUyuyor := ← boolOku k v }
      | "hataKanali" => s := { s with hataKanali := ← boolOku k v }
      | "deneme" => s := { s with deneme := ← natOku k v }
      | _ => throw s!"bilinmeyen anahtar '{k}'"
    | _ => throw s!"anahtar=değer beklenirken '{satir}'"
  match kapi with
  | "O" =>
    return match kapiO c with
      | .reddet => "reddet" | .iste => "iste" | .anaSiraya => "anaSiraya" | .atla => "atla" | .cagir => "cagir"
  | "S" =>
    return match kapiS s with
      | .gecti => "gecti" | .tekrar => "tekrar" | .failLoud => "failLoud"
  | _ => throw s!"kapi: O|S beklenirken '{kapi}'"

def main : IO UInt32 := do
  let girdi ← (← IO.getStdin).readToEnd
  for kayit in girdi.splitOn "\n---\n" do
    match kayitCoz kayit with
    | .ok h => IO.println h
    | .error e =>
      IO.eprintln s!"HATA: {e}"
      return 2
  return 0
