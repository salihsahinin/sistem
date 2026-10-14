import Kanon

/-- `skillkapi`: stdin `anahtar=değer` satırları → stdout tek satır hüküm (RET-0 · BEKLET · ONAR-2 · ONAR-3 · ÜRET-<şekil>-<yaprak>).
Çıkış: 0 hüküm üretildi · 2 girdi hatası (stderr). -/
def main : IO UInt32 := do
  let girdi ← (← IO.getStdin).readToEnd
  match Kanon.SkillKapi.oku girdi with
  | .ok a =>
    IO.println (Kanon.SkillKapi.hukum a).kod
    return 0
  | .error e =>
    IO.eprintln s!"HATA: {e}"
    return 2
