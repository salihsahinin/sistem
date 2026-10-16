/-
Kanon.YanOturumSinir — yan-oturum karar sınırı (tüzük m.41; Salih 2026-07-17, düzeltme 08-01, geçiş kaydı-2 08-17 KB-34, dış-proje sınırı 09-09 M6),
Lean 4 kod tabanı. Karar 117, 2026-10-17. Oturum türü için bkz. Kanon.ParalelOturum.Tur (kopyalanmadı).
Türkçe özet (geri-çeviri): kanon/inşa kararı geçerli olursa şu koşul gerekir: (yüzey = ana-sıra ∧ model = mevcut en güçlü model) ∨ Salih açık imzası.
Koşul gerekliliktir, yeterlilik değil. Yan oturum bu sınıfta karar almaz; bulguyu devir dosyasıyla ana sıraya taşır. Kapsam yalnız kanon/inşa kararlarıdır;
diğer ajanlara dair kararlar m.31 düzenindedir, model-kapısı aranmaz. Jarvis-dışı iş (staj, galeri) kararı karar masasına taşınmaz.
-/
import Kanon.ParalelOturum
namespace Kanon.YanOturumSinir
open Kanon.ParalelOturum

inductive KararSinifi | kanonInsa | digerAjan | disProje
  deriving Repr, DecidableEq

/-- Geçerliliğin GEREKLİ koşulu (yeterli değil). `enGuclu`: model = mevcut en güçlü model. -/
def gerekliKosul (yuzey : Tur) (enGuclu salihImza : Bool) : Bool :=
  (yuzey == .anaSira && enGuclu) || salihImza

/-- Sınıfa göre model-kapısı aranır mı: yalnız kanon/inşa. -/
def modelKapisiAranir : KararSinifi → Bool
  | .kanonInsa => true
  | _ => false

/-- Karar Jarvis karar masasına taşınır mı: jarvis-dışı proje taşınmaz. -/
def masayaTasinir : KararSinifi → Bool
  | .disProje => false
  | _ => true

/-- Yan oturum + Salih imzasız → kanon/inşa kararı koşulu sağlanmaz. -/
theorem yan_oturum_imzasiz_gecersiz (t : Tur) (g : Bool) (h : t ≠ .anaSira) :
    gerekliKosul t g false = false := by
  cases t <;> simp_all [gerekliKosul]

theorem ana_sira_zayif_model_gecersiz : gerekliKosul .anaSira false false = false := rfl

theorem dis_proje_masaya_tasinmaz : masayaTasinir .disProje = false := rfl

end Kanon.YanOturumSinir
