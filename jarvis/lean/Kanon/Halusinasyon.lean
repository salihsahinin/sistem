/-
Kanon.Halusinasyon — görev müsaitlik derecesi H(görev) ve tetik hükmü (core/halusinasyon-paketi.md §2, v1 deneysel m.29),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 2, 2026-10-16. Uygulayan kod: .claude/skills/halusinasyon-engelleyici/scripts/derece.py
(ağırlık tablosu ve eşikler birebir). Ağırlıklar kanıtsız tercih; ≥50 olayda yeniden kalibre (gerekçe md'de).
Türkçe özet (geri-çeviri): H, açık bayrakların tamsayı ağırlıklarının toplamıdır (v7c ve v8 eksi). Eşik normal görevde 7, pahalı
geri-alma sınıfında 4. Atıf/künye/DOI/URL çıktısı (v3a) ya da H ≥ eşik → halusinasyon-engelleyici skill tetiklenir (çıkış 10);
aksi hâlde H ≥ 4 → kaynak + destek kontrolü (F1+F2) zorunlu (çıkış 5); aksi hâlde gerekmez (çıkış 0).
-/
namespace Kanon.Halusinasyon

structure Bayrak where
  v1 : Bool := false   -- nadirlik
  v2 : Bool := false   -- tazelik
  v3a : Bool := false  -- atıf/künye/DOI/URL (override)
  v3b : Bool := false  -- yapılandırılmış veri → düzyazı
  v3c : Bool := false  -- kod API/paket/araç adı ∨ prosedür
  v3d : Bool := false  -- sayısal/tarih iddiası
  v4 : Bool := false   -- uzunluk
  v5 : Bool := false   -- bileşiklik ≥3 adım
  v6 : Bool := false   -- öncül şüphesi
  v7a : Bool := false  -- kaynak yok
  v7b : Bool := false  -- kaynak ham/uzun
  v7c : Bool := false  -- kaynak yapılandırılmış (−1)
  v8 : Bool := false   -- doğrulayıcı/yürütücü var (−2)
  v9 : Bool := false   -- runtime thinking ∧ araç
  v10 : Bool := false  -- dil Türkçe/az kaynaklı
  deriving Repr

private def a (b : Bool) (w : Int) : Int := if b then w else 0

/-- H := Σ ağırlık(açık bayrak) -/
def derece (f : Bayrak) : Int :=
  a f.v1 2 + a f.v2 3 + a f.v3a 3 + a f.v3b 2 + a f.v3c 2 + a f.v3d 1 + a f.v4 1 + a f.v5 2 + a f.v6 2 +
  a f.v7a 2 + a f.v7b 1 + a f.v7c (-1) + a f.v8 (-2) + a f.v9 1 + a f.v10 1

def esik (pahaliGeriAlma : Bool) : Int := if pahaliGeriAlma then 4 else 7

inductive Hukum | tetik | f1f2Zorunlu | gerekmez
  deriving Repr, DecidableEq

def hukum (f : Bayrak) (pahali : Bool) : Hukum :=
  if f.v3a || decide (derece f ≥ esik pahali) then .tetik
  else if decide (derece f ≥ 4) then .f1f2Zorunlu
  else .gerekmez

/-- derece.py çıkış kodu sözlüğü -/
def cikisKodu : Hukum → Nat
  | .tetik => 10 | .f1f2Zorunlu => 5 | .gerekmez => 0

/-- Atıf çıktısı her zaman skill'i tetikler (override). -/
theorem atif_override (f : Bayrak) (p : Bool) (h : f.v3a = true) : hukum f p = .tetik := by
  simp [hukum, h]

/-- Pahalı geri-almada F1+F2 bandı boştur: eşik 4 olduğundan H ≥ 4 zaten tetik. -/
theorem pahali_bant_bos (f : Bayrak) : hukum f true ≠ .f1f2Zorunlu := by
  unfold hukum esik
  split <;> simp_all
  split <;> simp_all

end Kanon.Halusinasyon
