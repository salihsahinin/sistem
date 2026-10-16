/-
Kanon.DeneyselRakam — deneysel-rakam disiplini (tüzük m.39; V40a, Salih 2026-07-13; md.22 pozitif karşılık KB-28; optimal-kıyas şartı Karar 79 D3),
Lean 4 kod tabanı. Karar 117, 2026-10-17.
Türkçe özet (geri-çeviri): her deneysel rakam Jarvis'ten çıkar ya da Jarvis onayından geçer; rakam deneysel damgalı olmalı (m.29).
Rakam [?] damgası + kaynak-borcu satırıyla verilir ya da hiç verilmez. "Kaç kat" oranı yalnız optimal-kıyası ölçülmüşse
iyi-vs-optimal diye verilir; ölçülmemişse yalnız iyi-vs-kötü diye damgalanır. A7 denetimi ve Salih vetosu (m.31) her rakamda işler.
-/
namespace Kanon.DeneyselRakam

/-- Oranın kıyas türü. `yok`: rakam oran değil. -/
inductive Kiyas | yok | iyiVsKotu | iyiVsOptimal
  deriving Repr, DecidableEq

structure Rakam where
  damgali         : Bool  -- deneysel damga (m.29)
  kaynakBorcu     : Bool  -- kaynak-borcu satırı yazılı ([?] rakam için)
  jarvisOnayli    : Bool  -- Jarvis'ten çıktı ∨ Jarvis onayından geçti
  kiyas           : Kiyas
  optimalOlculdu  : Bool  -- optimal sıralama/çözüm gerçekten ölçüldü
  deriving Repr

/-- Oran türü beyanı geçerli ⟺ iyi-vs-optimal yalnız optimal ölçüldüyse. -/
def kiyasGecerli (r : Rakam) : Bool :=
  match r.kiyas with
  | .iyiVsOptimal => r.optimalOlculdu
  | _ => true

/-- Rakam verilebilir ⟺ damgalı ∧ kaynak-borçlu ∧ Jarvis onaylı ∧ kıyas geçerli; aksi halde hiç verilmez. -/
def verilebilir (r : Rakam) : Bool :=
  r.damgali && r.kaynakBorcu && r.jarvisOnayli && kiyasGecerli r

theorem optimalsiz_optimal_orani_yok (r : Rakam) (h1 : r.kiyas = .iyiVsOptimal) (h2 : r.optimalOlculdu = false) :
    verilebilir r = false := by
  simp [verilebilir, kiyasGecerli, h1, h2]

theorem onaysiz_rakam_yok (r : Rakam) (h : r.jarvisOnayli = false) : verilebilir r = false := by
  simp [verilebilir, h]

end Kanon.DeneyselRakam
