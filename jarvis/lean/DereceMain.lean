import Kanon.Halusinasyon

open Kanon.Halusinasyon

/-- `derece`: stdin `anahtar=değer` satırları → stdout `cikisKodu` (0 gerekmez · 5 F1+F2 zorunlu · 10 skill tetiklenir).
Anahtarlar: v1 v2 v3a v3b v3c v3d v4 v5 v6 v7a v7b v7c v8 v9 v10 ve `pahali` (pahalı geri-alma sınıfı); Bool: true/false/1/0.
Kayıtlar `---` satırıyla ayrılır (her kayıt için bir satır). Çıkış: 0 hüküm üretildi · 2 girdi hatası (stderr).
Rust/Python ile fark testi: `jarvis/kod/kural/tests/lean_fark.rs`. -/
def boolOku (k v : String) : Except String Bool :=
  if v == "true" || v == "1" then .ok true
  else if v == "false" || v == "0" then .ok false
  else .error s!"{k}: Bool beklenirken '{v}'"

def kayitCoz (kayit : String) : Except String Nat := do
  let mut f : Bayrak := {}
  let mut pahali := false
  for ham in kayit.splitOn "\n" do
    let satir := ham.trimAscii.toString
    if satir.isEmpty || satir.startsWith "#" then continue
    match satir.splitOn "=" with
    | [k, v] =>
      let k := k.trimAscii.toString
      let v := v.trimAscii.toString
      match k with
      | "v1" => f := { f with v1 := ← boolOku k v }
      | "v2" => f := { f with v2 := ← boolOku k v }
      | "v3a" => f := { f with v3a := ← boolOku k v }
      | "v3b" => f := { f with v3b := ← boolOku k v }
      | "v3c" => f := { f with v3c := ← boolOku k v }
      | "v3d" => f := { f with v3d := ← boolOku k v }
      | "v4" => f := { f with v4 := ← boolOku k v }
      | "v5" => f := { f with v5 := ← boolOku k v }
      | "v6" => f := { f with v6 := ← boolOku k v }
      | "v7a" => f := { f with v7a := ← boolOku k v }
      | "v7b" => f := { f with v7b := ← boolOku k v }
      | "v7c" => f := { f with v7c := ← boolOku k v }
      | "v8" => f := { f with v8 := ← boolOku k v }
      | "v9" => f := { f with v9 := ← boolOku k v }
      | "v10" => f := { f with v10 := ← boolOku k v }
      | "pahali" => pahali ← boolOku k v
      | _ => throw s!"bilinmeyen anahtar '{k}'"
    | _ => throw s!"anahtar=değer beklenirken '{satir}'"
  return cikisKodu (hukum f pahali)

def main : IO UInt32 := do
  let girdi ← (← IO.getStdin).readToEnd
  for kayit in girdi.splitOn "\n---\n" do
    match kayitCoz kayit with
    | .ok k => IO.println k
    | .error e =>
      IO.eprintln s!"HATA: {e}"
      return 2
  return 0
