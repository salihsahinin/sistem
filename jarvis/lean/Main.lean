import Kanon

/-- `skillkapi`: stdin `anahtar=değer` satırları → stdout hüküm (RET-0 · BEKLET · ONAR-2 · ONAR-3 · ÜRET-<şekil>-<yaprak>).
Toplu kip: kayıtlar `---` satırıyla ayrılırsa her kayıt için bir satır (Rust uygulamasıyla fark testi için).
Çıkış: 0 hüküm üretildi · 2 girdi hatası (stderr). -/
def main : IO UInt32 := do
  let girdi ← (← IO.getStdin).readToEnd
  for kayit in girdi.splitOn "\n---\n" do
    match Kanon.SkillKapi.oku kayit with
    | .ok a => IO.println (Kanon.SkillKapi.hukum a).kod
    | .error e =>
      IO.eprintln s!"HATA: {e}"
      return 2
  return 0
