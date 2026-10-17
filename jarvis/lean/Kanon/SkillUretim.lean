/-
Kanon.SkillUretim — skill üretim şemasının çelişki taraması hükümleri ve v1.1 eki (core/skill-uretim-semasi.md §4, §4b; m.16, m.43, Karar 96 masa-12, Karar 43),
Lean 4 kod tabanı. Karar 117, 2026-10-17. Çakışanlar kopyalanmadı: kapı ağacı K0-K3, şekil önceliği → Kanon.SkillKapi; aday eşiği (N, W=90), deneme/hazine/arşiv yeri → Kanon.SkillDogum.
Gerekçe, rakamlı ölçüm, kaynak ve tarih md'de kalır.
Türkçe özet (geri-çeviri): yan etkili skill'de `disable-model-invocation` yalnız birincil şekli T-Y olanda zorunludur; ritüel ve orkestratörde yan-etki adımı Salih beyanı kapısıyla yeter.
Description ≤ 1024 karakter ve standart zorunludur (3. şahıs, NE, NE zaman, negatif tetik, yayın öncesi 20-sorgu eval); hazine tavanı yoktur, metadata bütçesi yalnız ölçülür (uyarı, engel değil).
S-kaynak üçüncü aday kapısıdır: tetik 5 kapanışta bir ∨ sıcak-katman tavan aşımı ∨ Salih emri. Yerleşim üç soruyla: her seans gerekli → CLAUDE.md; yalnız belli dosya/dizin → paths'li kural;
yalnız belli iş türü → skill. K0 Y2' koşullu-yük: bölüm her seans yükleniyor ∧ (koşul-dili ≥ eşik ∨ adım ≥ 3) ∧ okunma oranı düşük. Md'den mekanik çıkarma yetmez: eval-önce (≥ 3 eval ∧ skill'siz baseline).
İcra-türü satırı olmayan aday K1'e giremez. Kavram dersi: icra türü + bağlam eşlemesi varsa aday, yoksa BEKLET. Bağımsız doğrulayıcı (K2-İ) yalnız T-Y ve T-O için. Yan oturumda üretilen skill branch + PR ile gider.
-/
import Kanon.SkillKapi
namespace Kanon.SkillUretim
open Kanon.SkillKapi

/-! ## §4 Çelişki taraması hükümleri -/

/-- §4: description üst sınırı (07-17 standardı; platform sınırı 1536'dan sıkı). -/
def descriptionAzami : Nat := 1024

/-- §4: yan-etkili skill'de `disable-model-invocation` zorunluluğu: yalnız birincil şekil T-Y ise. -/
def disableModelInvocationZorunlu (s : Sekil) : Bool := decide (s = .yanEtkili)

/-- §4: ritüel/orkestratörün yan-etki adımı Salih beyanı kapısıyla yeter. -/
def yanEtkiKapisiYeter (s : Sekil) (salihBeyaniKapisi : Bool) : Bool :=
  disableModelInvocationZorunlu s || (decide (s = .rituel ∨ s = .orkestrator) && salihBeyaniKapisi)

/-! ## §4b Üç yuva, S-kaynak, description standardı -/

/-- §4b F6: description standardı. -/
structure Description where
  uzunluk       : Nat
  ucuncuSahis   : Bool
  ne            : Bool
  neZaman       : Bool
  negatifTetik  : Bool
  yirmiSorguEval : Bool   -- yayın öncesi 20-sorgu description eval
  deriving Repr

def descriptionTam (d : Description) : Bool :=
  decide (d.uzunluk ≤ descriptionAzami) && d.ucuncuSahis && d.ne && d.neZaman && d.negatifTetik && d.yirmiSorguEval

/-- §4b F6: hazine tavanı yok; metadata bütçesi aşımı yalnız uyarı üretir, üretimi engellemez. -/
def metadataAsimiEngeller (_asim : Bool) : Bool := false
def metadataAsimiUyarir (asim : Bool) : Bool := asim

/-- §4b S-kaynak: üçüncü aday kapısı tetiği := 5 kapanışta bir ∨ sıcak-katman tavan aşımı ∨ Salih emri. -/
def sKaynakTetik (kapanisSayaci : Nat) (sicakTavanAsildi salihEmri : Bool) : Bool :=
  (decide (kapanisSayaci ≥ 5)) || sicakTavanAsildi || salihEmri

/-- §4b üç yuva: yerleşim üç soruyla, bu sırayla. -/
inductive Yuva | claudeMd | yolKapsamliKural | skill
  deriving Repr, DecidableEq

def yuva (herSeansGerekli yalnizBelliDosyaDizin : Bool) : Yuva :=
  if herSeansGerekli then .claudeMd
  else if yalnizBelliDosyaDizin then .yolKapsamliKural
  else .skill

/-- §4b K0 Y2' koşullu-yük := her seans yükleniyor ∧ (koşul-dili ≥ eşik ∨ adım ≥ 3) ∧ okunma oranı düşük. Eşik kalibresiz [?], çağıran verir. -/
def y2Kosullu (herSeansYukleniyor : Bool) (kosulDili esik adim : Nat) (okunmaDusuk : Bool) : Bool :=
  herSeansYukleniyor && (decide (kosulDili ≥ esik) || decide (adim ≥ 3)) && okunmaDusuk

/-- §4b kendinden-üretilen skill freni: eval-önce := ≥ 3 eval ∧ skill'siz baseline. -/
def evalOnce (evalSayisi : Nat) (baselineVar : Bool) : Bool := decide (evalSayisi ≥ 3) && baselineVar

/-- §4b icra-türü satırı: satırsız aday K1'e giremez. -/
def k1Giris (a : Aday) (icraTuruSatiri : Bool) : Bool := k1 a && icraTuruSatiri

/-- §4b kavram dersi: icra türü + bağlam eşlemesi varsa aday; yoksa BEKLET (RET-0 değil). -/
inductive KavramHukum | aday | beklet
  deriving Repr, DecidableEq

def kavramDersi (icraTuruEslemesi : Bool) : KavramHukum := if icraTuruEslemesi then .aday else .beklet

/-- §4b hız ilkesi: pahalı bağımsız doğrulayıcı (K2-İ) yalnız T-Y ve T-O. -/
def bagimsizDogrulayiciGerekli (s : Sekil) : Bool := decide (s = .yanEtkili ∨ s = .orkestrator)

/-- §4b dağıtım: yan oturumda üretilen skill branch + PR ile gider; merge ana-sıra. -/
def yanOturumSkillPrIle (yanOturum prAcildi : Bool) : Bool := !yanOturum || prAcildi

theorem yan_etkili_disable_zorunlu : disableModelInvocationZorunlu .yanEtkili = true := by decide
theorem rituel_disable_zorunlu_degil : disableModelInvocationZorunlu .rituel = false := by decide
theorem rituel_salih_kapisiyla_yeter : yanEtkiKapisiYeter .rituel true = true := by decide
theorem uretici_kapisiz_yetmez : yanEtkiKapisiYeter .uretici true = false := by decide
theorem tavan_engellemez (b : Bool) : metadataAsimiEngeller b = false := rfl
theorem her_seans_gerekliyse_claude_md (d : Bool) : yuva true d = .claudeMd := by simp [yuva]
theorem satirsiz_aday_k1_degil (a : Aday) : k1Giris a false = false := by simp [k1Giris]
theorem eslemesiz_kavram_beklet : kavramDersi false = .beklet := rfl
theorem bes_kapanista_s_kaynak : sKaynakTetik 5 false false = true := by decide
theorem iki_eval_yetmez (b : Bool) : evalOnce 2 b = false := by simp [evalOnce]

end Kanon.SkillUretim
