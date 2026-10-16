/-
Kanon.RolKatman — rol katmanları: köle ≠ üst-orkestratör ≠ domain-lider (tüzük m.44; Salih 2026-07-21; CEO katmanı emekli 08-17; Karar 89 model katmanı),
Lean 4 kod tabanı. Karar 117, 2026-10-17. Model kademesi ve işçi ≤ lider tavanı için bkz. Kanon.Delegasyon (kopyalanmadı).
Türkçe özet (geri-çeviri): görev çok-domain ise ∨ alanında lider yoksa orkestrasyon Jarvis'tedir (domain-lider seviyesine kadar böler; işçiye yalnız lider yokken iner).
Görev tek-domain ∧ alanda lider varsa orkestrasyon domain-liderdedir. Her iki dalda CEO rolü (karar hazırlama, köprü, kanon bakımı, Salih muhataplığı)
Jarvis'te sabittir, devredilemez. Domain-lider modeli Opus 5 (effort medium), işçi ondan pahalı olmaz.
-/
import Kanon.Delegasyon
namespace Kanon.RolKatman
open Kanon.Delegasyon

inductive Orkestrator | jarvis | domainLider
  deriving Repr, DecidableEq

structure Gorev where
  cokDomain  : Bool  -- kapsam çok-domain
  liderVar   : Bool  -- görevin domain'inde lider var
  deriving Repr

def orkestrasyon (g : Gorev) : Orkestrator :=
  if g.cokDomain || !g.liderVar then .jarvis else .domainLider

/-- CEO rolü her iki dalda Jarvis'tedir; devredilemez. -/
def ceo (_ : Gorev) : Orkestrator := .jarvis

/-- Üst-orkestratör işçi seviyesine yalnız o domain'de lider yokken iner. -/
def isciSeviyesineInebilir (liderVar : Bool) : Bool := !liderVar

theorem cok_domain_jarvis (l : Bool) : orkestrasyon ⟨true, l⟩ = .jarvis := by
  simp [orkestrasyon]

theorem tek_domain_lider_varsa_lider : orkestrasyon ⟨false, true⟩ = .domainLider := rfl

theorem ceo_sabit (g : Gorev) : ceo g = .jarvis := rfl

theorem sonnet_isci_opus_lider_altinda : modelUygun .opus .sonnet = true := rfl

end Kanon.RolKatman
