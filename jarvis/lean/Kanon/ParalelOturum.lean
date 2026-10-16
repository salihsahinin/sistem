/-
Kanon.ParalelOturum — oturum düzeni (wiki/paralel-oturum-protokolu.md §1 canlı-oturum kapısı + §5 EK-5; Karar 113 M4; Salih 2026-10-16 A),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 1, 2026-10-16. EK, EK-2, EK-4 ve Karar 105 satırı EK-5 ile süpersede; md'de AS-OF kalır.
Türkçe özet (geri-çeviri): Jarvis ana-sıra worktree'siz, main'e doğrudan commit atar, PR açmaz. Yalnız okuyan/soru-cevap oturumu
(gunluk) worktree'siz ve commit'siz. Diğer her yazan oturum (alan ajanı, Friday, öğrenme, omp) worktree + kendi dalı ile çalışır, seans
sonunda dalı push edip PR açar. Birleştirmeyi yalnız Jarvis ana-sıra, Salih "birleştir #N" deyince yapar. Canlı-oturum kapısı:
başka oturum şüphesi varsa tek soru sorulur, diğer oturumun dosyasına yazılmaz, commit pathspec ile atılır.
-/
namespace Kanon.ParalelOturum

inductive Tur | anaSira | yalnizOkur | yazanYan
  deriving Repr, DecidableEq

structure Duzen where
  worktree   : Bool
  kendiDali  : Bool
  prSonunda  : Bool
  mainCommit : Bool
  deriving Repr, DecidableEq

/-- EK-5 tablosu. -/
def duzen : Tur → Duzen
  | .anaSira    => { worktree := false, kendiDali := false, prSonunda := false, mainCommit := true }
  | .yalnizOkur => { worktree := false, kendiDali := false, prSonunda := false, mainCommit := false }
  | .yazanYan   => { worktree := true,  kendiDali := true,  prSonunda := true,  mainCommit := false }

/-- Birleştirme izni := yapan ana-sıra ∧ Salih "birleştir #N" dedi -/
def birlestirebilir (yapan : Tur) (salihDedi : Bool) : Bool := yapan == .anaSira && salihDedi

/-- §1 canlı-oturum kapısı (K1): şüphe → tek soru ∧ yabancı dosyaya yazma yok ∧ pathspec commit. -/
structure K1 where
  supheVar        : Bool
  deriving Repr

inductive K1Eylem | devam | tekSoruPathspec
  deriving Repr, DecidableEq

def k1 (k : K1) : K1Eylem := if k.supheVar then .tekSoruPathspec else .devam

/-- Ana-sıra dışında hiçbir oturum main'e doğrudan commit atmaz. -/
theorem yalniz_anasira_main (t : Tur) (h : (duzen t).mainCommit = true) : t = .anaSira := by
  cases t <;> simp_all [duzen]

/-- Yazan yan oturum worktree'siz çalışmaz. -/
theorem yazan_worktreede : (duzen .yazanYan).worktree = true := rfl

theorem salihsiz_birlesme_yok (t : Tur) : birlestirebilir t false = false := by
  simp [birlestirebilir]

end Kanon.ParalelOturum
