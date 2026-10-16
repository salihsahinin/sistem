/-
Kanon.AlanAjani — alan ajanı ortak şablonunun sayısal ve yetki kuralları (8 alan ajanı AGENTS.md §3-§5; üretici
jarvis/tools/alan-ajani-dogur.py, şablon sablonlar/ajan-iskelet/AGENTS.md.tmpl; Karar 104 M1, 105, 113 M4, protokol §5 EK-5),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 3, 2026-10-16. Model tavanı Kanon.Delegasyon, okuma/yazma Kanon.Izolasyon, oturum
düzeni Kanon.ParalelOturum modülündedir.
Türkçe özet (geri-çeviri): alan ajanının kapsülü 4 KB ve 20 satırı aşamaz, sigorta olarak en çok 8 madde; aşımda en eski madde arşive
iner. Defter 24 KB, fikir kutusu 10 KB tavanlı. Bir koşumda en çok 36 işçi, işçi başına en çok 54 araç çağrısı, en çok 3 aile.
Ölçen (hakem) yapandan ayrıdır. Pratik ve `DONE` hükmü yalnız Salih beyanıyla. `.claude/**` ve `core/**` yalnız Edit aracıyla
yazılır. Oturum: worktree + kendi dalı + seans sonunda PR (EK-5).
-/
namespace Kanon.AlanAjani

def kapsulBayt : Nat := 4096
def kapsulSatir : Nat := 20
def kapsulMadde : Nat := 8
def defterBayt : Nat := 24576
def fikirBayt : Nat := 10240
def isciKosum : Nat := 36
def aracIsci : Nat := 54
def aile : Nat := 3

structure Kapsul where
  bayt : Nat
  satir : Nat
  madde : Nat
  deriving Repr

/-- Kapsül bütçesi := bayt ≤ 4 KB ∧ satır ≤ 20 ∧ madde ≤ 8; aşım → FIFO arşiv -/
def kapsulIcinde (k : Kapsul) : Bool :=
  decide (k.bayt ≤ kapsulBayt) && decide (k.satir ≤ kapsulSatir) && decide (k.madde ≤ kapsulMadde)

structure Kosum where
  isci : Nat
  enCokArac : Nat
  aileSayisi : Nat
  deriving Repr

def kosumIcinde (k : Kosum) : Bool :=
  decide (k.isci ≤ isciKosum) && decide (k.enCokArac ≤ aracIsci) && decide (k.aileSayisi ≤ aile)

/-- Yapan ≠ ölçen -/
def olcumGecerli (yapan olcen : String) : Bool := yapan != olcen

/-- `DONE` yalnız Salih beyanıyla -/
def doneGecerli (salihBeyani : Bool) : Bool := salihBeyani

inductive Arac | edit | bash | write
  deriving Repr, DecidableEq

/-- `.claude/**` ve `core/**` yazımı yalnız Edit/Write aracıyla (Bash teli). -/
def kanonYazimIzinli : Arac → Bool
  | .bash => false
  | _ => true

theorem kendi_olcumu_gecersiz (a : String) : olcumGecerli a a = false := by
  simp [olcumGecerli]

theorem bash_kanon_yazamaz : kanonYazimIzinli .bash = false := rfl

end Kanon.AlanAjani
