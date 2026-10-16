/-
Kanon.Commit — commit mesajı ve git işlemi izinleri (kök AGENTS md.4, 5, 6, 14; tüzük m.8, m.9, m.10), Lean 4 kod tabanı.
Karar 114 geçiş turu parti 1, 2026-10-16.
Karar 117 parti 2 (2026-10-16): tüzük m.8-10 gövdesi bu modülde.
Türkçe özet (geri-çeviri): commit mesajı dört önekten biriyle başlar ([icra] [damıtma] [ariza] [revert]; ASCII yazımı [damitma] da
geçerli), em-dash içermez; dili İngilizcedir (yargı). Git işlemleri: commit serbesttir; push yalnız Salih beyanıyla (yan oturum dalı
için protokol §5 genel beyanı geçerli); `git add -A`/`.` başka canlı oturum varken yasaktır; `--force` ve yarım işi atma (discard)
yalnız Salih o işi adıyla söylediğinde. Birleştirme (merge) Jarvis ana-sıradadır ve Salih "birleştir #N" demeden yapılmaz.
Kayıt silme ve kayıt birleştirme (m.8) kendiliğinden yapılmaz, yalnız Salih kararıyla; arşive indirme yalnız yerinde pointer bırakılırsa
serbesttir. Gün (m.9) ancak push'lanmış commit varsa sayılır; plan, niyet ve markdown kanıt değildir. Commit (m.10) başına en çok
bir karar/mantıksal parça düşer (karar başına ayrı commit).
-/
namespace Kanon.Commit

def onekler : List String := ["[icra]", "[damıtma]", "[damitma]", "[ariza]", "[revert]"]

/-- Önek kuralı := mesaj tanımlı öneklerden biriyle başlar -/
def onekli (m : String) : Bool := onekler.any (fun o => m.startsWith o)

/-- Em-dash yasağı (kök md.6, Kun Chen) -/
def emDashYok (m : String) : Bool := !(m.contains '—')

/-- Mesaj := önekli ∧ em-dash yok ∧ İngilizce (yargı girdisi) -/
def mesajGecerli (m : String) (ingilizce : Bool) : Bool := onekli m && emDashYok m && ingilizce

inductive Islem | commit | push | pushYanDal | addTum | force | discard | merge | kayitSil | kayitBirlestir | arsivle
  deriving Repr, DecidableEq

structure Baglam where
  salihBeyani      : Bool := false  -- Salih bu push/merge için açık beyan verdi
  salihIsAdiyla    : Bool := false  -- Salih bu force/discard işini adıyla söyledi
  canliParalel     : Bool := false  -- başka ajan/oturum canlı (acilis-kapilari K1)
  anaSira          : Bool := false  -- işlemi yapan Jarvis ana-sıra
  pointerBirakildi : Bool := false  -- arşive indirilen kaydın yerinde pointer bırakıldı (m.8 pozitif karşılık)
  deriving Repr

/-- İzin tablosu (first hit yok; işlem türüne göre tek kural). -/
def izin : Islem → Baglam → Bool
  | .commit,     _ => true
  | .push,       b => b.salihBeyani
  | .pushYanDal, b => !b.anaSira          -- protokol §5 genel beyanı; ana-sıra main'i yine beyanla push eder
  | .addTum,     b => !b.canliParalel
  | .force,      b => b.salihIsAdiyla
  | .discard,    b => b.salihIsAdiyla
  | .merge,      b => b.anaSira && b.salihBeyani
  | .kayitSil,       b => b.salihBeyani   -- m.8: kendiliğinden silme yok, yalnız Salih kararı
  | .kayitBirlestir, b => b.salihBeyani   -- m.8: kendiliğinden birleştirme yok
  | .arsivle,        b => b.pointerBirakildi

theorem push_beyansiz_yok (b : Baglam) (h : b.salihBeyani = false) : izin .push b = false := by
  simp [izin, h]

theorem merge_yalniz_anasira (b : Baglam) (h : b.anaSira = false) : izin .merge b = false := by
  simp [izin, h]

theorem force_adsiz_yok (b : Baglam) (h : b.salihIsAdiyla = false) : izin .force b = false ∧ izin .discard b = false := by
  simp [izin, h]

theorem silme_kararsiz_yok (b : Baglam) (h : b.salihBeyani = false) : izin .kayitSil b = false ∧ izin .kayitBirlestir b = false := by
  simp [izin, h]

theorem arsiv_pointersiz_yok (b : Baglam) (h : b.pointerBirakildi = false) : izin .arsivle b = false := by
  simp [izin, h]

/-- Gün kanıtı türleri (m.9) -/
inductive Kanit | pushluCommit | commitPushsuz | plan | niyet | markdown
  deriving Repr, DecidableEq

/-- Done-yüklemi (m.9): gün sayılır := kanıtlardan en az biri push'lanmış commit -/
def gunSayilir (kanitlar : List Kanit) : Bool := kanitlar.any (fun k => k == Kanit.pushluCommit)

theorem plan_niyet_markdown_yetmez (k : List Kanit) (h : Kanit.pushluCommit ∉ k) : gunSayilir k = false := by
  simp only [gunSayilir, List.any_eq_false]
  intro x hx hb
  have : x = Kanit.pushluCommit := by simpa using hb
  exact h (this ▸ hx)

/-- Commit parçası kuralı (m.10): commit başına en çok bir karar/mantıksal parça -/
def tekKarar (kararSayisi : Nat) : Bool := decide (kararSayisi ≤ 1)

/-- Tam commit geçerliliği := mesaj geçerli ∧ tek karar -/
def commitGecerli (m : String) (ingilizce : Bool) (kararSayisi : Nat) : Bool :=
  mesajGecerli m ingilizce && tekKarar kararSayisi

example : gunSayilir [Kanit.plan, Kanit.markdown] = false := by decide
example : gunSayilir [Kanit.plan, Kanit.pushluCommit] = true := by decide
example : commitGecerli "[ariza] fix x" true 2 = false := by native_decide
example : commitGecerli "[revert] undo x" true 1 = true := by native_decide
example : mesajGecerli "[icra] Close durum #8" true = true := by native_decide
example : mesajGecerli "[icra] a — b" true = false := by native_decide
example : mesajGecerli "fix: x" true = false := by native_decide

end Kanon.Commit
