/-
Kanon.SkillDogum — skill adayı doğumu (tüzük m.43; Karar 30 → Karar 78) ve hazineye giriş kapısı (tüzük m.47; Karar 88 M5),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 2, 2026-10-16. Kapı ağacı K0-K3 ayrı modülde: Kanon.SkillKapi.
Türkçe özet (geri-çeviri): tekrar birimi görevdir (özdeş ve varyant ayrı sayılır; skill öncesi loop tekrarı aynı sayaca girer);
son 90 günlük pencerede aynı görev ≥3 kez tekrar ederse skill adayı olur ve skill-fikir-kutusuna satır düşer. Aday üretim değildir:
inşa kararı ayrıdır (eval-önce akış ∧ Salih tetiği). Kapı ağacını geçen skill hazineye doğrudan girmez: önce deneme sürümü olarak
`kuyruk/skill-deneme/<ad>/`'da durur; hazineye giriş ⟺ K3 geçti ∧ Salih en az bir kez canlı koştu ∧ Salih kabul sözü verdi.
Ret → arşiv (m.8).
-/
namespace Kanon.SkillDogum

def esikN : Nat := 3        -- Karar 78 (2026-08-29); zincir 3 → 5 (Karar 30) → 3
def pencereGun : Nat := 90

structure Kume where
  tekrar90Gun : Nat := 0    -- son 90 günde aynı görev tekrarı
  deriving Repr

/-- m.43: aday ⟺ tekrar ≥ N -/
def aday (k : Kume) : Bool := decide (k.tekrar90Gun ≥ esikN)

/-- m.43: üretim ⟺ eval-önce akışı ∧ Salih tetiği (aday olmak yetmez) -/
def uretim (evalOnce salihTetigi : Bool) : Bool := evalOnce && salihTetigi

structure Deneme where
  k3Gecti     : Bool := false
  salihKosum  : Nat  := 0
  salihKabul  : Bool := false
  salihRet    : Bool := false
  deriving Repr

inductive Yer | deneme | hazine | arsiv
  deriving Repr, DecidableEq

/-- m.47: ret → arşiv; hazine ⟺ K3 ∧ canlı koşum ≥ 1 ∧ kabul; aksi → denemede bekler. -/
def yer (d : Deneme) : Yer :=
  if d.salihRet then .arsiv
  else if d.k3Gecti && decide (d.salihKosum ≥ 1) && d.salihKabul then .hazine
  else .deneme

theorem kosulmadan_hazine_yok (d : Deneme) (h : d.salihKosum = 0) : yer d ≠ .hazine := by
  unfold yer
  split <;> simp_all

theorem aday_uretim_degil (k : Kume) : aday k = true → uretim false true = false := by
  intro _; rfl

end Kanon.SkillDogum
