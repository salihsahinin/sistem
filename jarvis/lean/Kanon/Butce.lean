/-
Kanon.Butce — Jarvis sıcak dosya bütçeleri (seans-kapanis §6, imzalı kural 2026-07-22; kapsül §5 Karar 104 M1; jarvis AGENTS.md bütçesi
v2 08-17), Lean 4 kod tabanı. Karar 114 geçiş turu parti 3, 2026-10-16. Ölçüm: seans-kapanis §6 tek bakış, tools/kural-sayaci.py,
kod/rituel (sicak-katman-fifo).
Türkçe özet (geri-çeviri): sıcak dosya tavanları: kapsül 8 KB ve 40 satır, pano 12 KB, fikir kutusu 20 KB, senaryo defteri 48 KB,
jarvis AGENTS.md (CLAUDE.md) 7 KB ve 80 satır, KILAVUZ 16 KB, kök AGENTS.md 25 satır, hafıza indeksi 4 KB. Aşım hata değil tetiktir:
teslim raporuna "boyut-tetiği: <dosya>" satırı düşer ve damıtma turu açılır; kapsülde aşımda en eski madde arşive iner (FIFO).
-/
namespace Kanon.Butce

inductive Dosya | kapsul | pano | fikirKutusu | defter | jarvisAgents | kilavuz | kokAgents | hafizaIndeksi
  deriving Repr, DecidableEq

/-- (bayt tavanı, satır tavanı) — none = o eksende tavan yok -/
def tavan : Dosya → Option Nat × Option Nat
  | .kapsul        => (some 8192, some 40)
  | .pano          => (some 12288, none)
  | .fikirKutusu   => (some 20480, none)
  | .defter        => (some 49152, none)
  | .jarvisAgents  => (some 7168, some 80)
  | .kilavuz       => (some 16384, none)
  | .kokAgents     => (none, some 25)
  | .hafizaIndeksi => (some 4096, none)

private def asar (t : Option Nat) (v : Nat) : Bool :=
  match t with
  | some x => decide (v > x)
  | none => false

/-- Aşım := bayt > tavan ∨ satır > tavan -/
def asim (d : Dosya) (bayt satir : Nat) : Bool := asar (tavan d).1 bayt || asar (tavan d).2 satir

inductive Eylem | yok | boyutTetigiDamitma | fifoArsiv
  deriving Repr, DecidableEq

def eylem (d : Dosya) (bayt satir : Nat) : Eylem :=
  if !asim d bayt satir then .yok
  else if d == .kapsul then .fifoArsiv
  else .boyutTetigiDamitma

example : asim .defter 70000 0 = true := by decide
example : asim .kokAgents 99999 22 = false := by decide

end Kanon.Butce
