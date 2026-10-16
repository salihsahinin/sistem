/-
Kanon.Zorlanabilirlik — zorlanabilirlik etiketi (tüzük m.45), Lean 4 kod tabanı. Karar 117 parti 2, 2026-10-16.
Uygulayan kod: yok (etiketleme turu henüz koşmadı; ilk koda taşınacak aday m.9 push-kanıtı, bkz. Kanon.Commit / push freni).
Türkçe özet (geri-çeviri): tüzüğün her maddesi ya zorlanabilir (ihlali koddan/log'dan deterministik yakalanabilir) ya zorlanamaz
(yalnız davranış kuralı) diye etiketlenir. Zorlanabilir olanlar kademeli olarak koda taşınır; ilk aday m.9. Zorlanabilir olup
henüz koda taşınmamış madde "kâğıt üzerinde" sayılır. Etiketleme turu ayrı bir damıtma seansıdır; m.45'in yazımı etiketlemenin
kendisi değildir, bu yüzden etiketsiz madde geçerli bir durumdur.
-/
namespace Kanon.Zorlanabilirlik

/-- Etiket türü: ihlal koddan/log'dan deterministik yakalanabilir mi. -/
inductive Etiket | zorlanabilir | zorlanamaz
  deriving Repr, DecidableEq

/-- Zorlanabilir maddenin koda taşınma durumu (kademeli taşıma). -/
inductive Tasima | kagitUstunde | kodda
  deriving Repr, DecidableEq

/-- Bir tüzük maddesinin kaydı. `etiket = none`: etiketleme turu henüz koşmadı. -/
structure Madde where
  no     : Nat
  etiket : Option Etiket
  tasima : Tasima
  deriving Repr

/-- Kademeli taşıma kuyruğunda ilk aday (m.45): m.9 push-kanıtı. -/
def ilkAday : Nat := 9

/-- "Kâğıt üzerinde" işareti: zorlanabilir ∧ koda taşınmamış. -/
def kagitUstunde (m : Madde) : Bool :=
  m.etiket == some .zorlanabilir && m.tasima == .kagitUstunde

/-- Koda taşınacak aday mı: yalnız zorlanabilir ∧ henüz taşınmamış; zorlanamaz ve etiketsiz madde aday değildir. -/
def tasinacakAday (m : Madde) : Bool := kagitUstunde m

/-- Etiketleme turu tamam mı: her maddenin etiketi var. -/
def etiketlemeTamam (maddeler : List Madde) : Bool := maddeler.all (·.etiket.isSome)

/-- Zorlanamaz madde hiçbir zaman "kâğıt üzerinde" işareti taşımaz (yalnız davranış kuralıdır). -/
theorem zorlanamaz_isaretsiz (n : Nat) (t : Tasima) :
    kagitUstunde ⟨n, some .zorlanamaz, t⟩ = false := by
  simp [kagitUstunde]

/-- Koda taşınan zorlanabilir madde işaret taşımaz. -/
theorem kodda_isaretsiz (n : Nat) :
    kagitUstunde ⟨n, some .zorlanabilir, .kodda⟩ = false := by
  simp [kagitUstunde]

/-- Etiketsiz madde aday olmaz: etiketleme turu önce gelir. -/
theorem etiketsiz_aday_degil (n : Nat) (t : Tasima) :
    tasinacakAday ⟨n, none, t⟩ = false := by
  simp [tasinacakAday, kagitUstunde]

theorem ilk_aday_m9 : ilkAday = 9 := rfl

end Kanon.Zorlanabilirlik
