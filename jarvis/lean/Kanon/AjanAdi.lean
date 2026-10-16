/-
Kanon.AjanAdi — alan ajanı ad ölçütü (Karar 107 + 110; kök AGENTS md.1), Lean 4 kod tabanı. Karar 114 geçiş turu parti 1, 2026-10-16.
Türkçe özet (geri-çeviri): yeni ajan adı ancak dört koşulun hepsi tutarsa kabul edilir: bilinen gerçek ünlü bir kişinin adı değil
(ileride tarihi figürü ajana çevirme ihtimali, Karar 107), en çok 4 harf, İngilizce bir sözcük (Karar 110: Sayi → Calc, Odak → Span),
Türkçe bir sözcükle eş sesli değil (Gard örneği: "zar" ile karışmasın). Uzunluk dışındaki üç koşul yargıdır, girdi olarak gelir;
ilk düşen koşul ret gerekçesi olur. Mevcut adlar: jarvis, friday (kök ajanlar, ölçüt öncesi) · tart gard span calc deci vega sage.
-/
namespace Kanon.AjanAdi

structure Aday where
  ad             : String
  unluKisi       : Bool := false  -- bilinen gerçek ünlü kişinin adı mı (yargı)
  ingilizce      : Bool := false  -- İngilizce sözcük mü (yargı)
  turkceEsSesli  : Bool := false  -- Türkçe bir sözcükle eş sesli mi (yargı)
  deriving Repr

inductive Hukum | kabul | unluKisi | uzun | ingilizceDegil | esSesli
  deriving Repr, DecidableEq

/-- Uzunluk ölçütü := |ad| ≤ 4 (karakter, deterministik) -/
def kisa (a : Aday) : Bool := decide (a.ad.length ≤ 4)

/-- Ad ölçütü := ¬ünlü ∧ |ad| ≤ 4 ∧ İngilizce ∧ ¬eş-sesli; first hit-policy ret gerekçesi. -/
def hukum (a : Aday) : Hukum :=
  if a.unluKisi then .unluKisi
  else if !kisa a then .uzun
  else if !a.ingilizce then .ingilizceDegil
  else if a.turkceEsSesli then .esSesli
  else .kabul

/-- "kabul ise dört koşulun hepsi tutar" -/
theorem kabul_ise_olcut (a : Aday) (h : hukum a = .kabul) :
    a.unluKisi = false ∧ kisa a = true ∧ a.ingilizce = true ∧ a.turkceEsSesli = false := by
  unfold hukum at h
  repeat (split at h <;> simp_all)

/-- Örnek: mevcut alan ajanı adları uzunluk ölçütünü sağlar. -/
example : ["tart", "gard", "span", "calc", "deci", "vega", "sage"].all (fun s => decide (s.length ≤ 4)) = true := by decide

end Kanon.AjanAdi
