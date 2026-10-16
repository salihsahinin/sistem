/-
Kanon.Commit — commit mesajı ve git işlemi izinleri (kök AGENTS md.4, 5, 6, 14; tüzük m.8, m.9, m.10), Lean 4 kod tabanı.
Karar 114 geçiş turu parti 1, 2026-10-16.
Türkçe özet (geri-çeviri): commit mesajı dört önekten biriyle başlar ([icra] [damıtma] [ariza] [revert]; ASCII yazımı [damitma] da
geçerli), em-dash içermez; dili İngilizcedir (yargı). Git işlemleri: commit serbesttir; push yalnız Salih beyanıyla (yan oturum dalı
için protokol §5 genel beyanı geçerli); `git add -A`/`.` başka canlı oturum varken yasaktır; `--force` ve yarım işi atma (discard)
yalnız Salih o işi adıyla söylediğinde. Birleştirme (merge) Jarvis ana-sıradadır ve Salih "birleştir #N" demeden yapılmaz.
-/
namespace Kanon.Commit

def onekler : List String := ["[icra]", "[damıtma]", "[damitma]", "[ariza]", "[revert]"]

/-- Önek kuralı := mesaj tanımlı öneklerden biriyle başlar -/
def onekli (m : String) : Bool := onekler.any (fun o => m.startsWith o)

/-- Em-dash yasağı (kök md.6, Kun Chen) -/
def emDashYok (m : String) : Bool := !(m.contains '—')

/-- Mesaj := önekli ∧ em-dash yok ∧ İngilizce (yargı girdisi) -/
def mesajGecerli (m : String) (ingilizce : Bool) : Bool := onekli m && emDashYok m && ingilizce

inductive Islem | commit | push | pushYanDal | addTum | force | discard | merge
  deriving Repr, DecidableEq

structure Baglam where
  salihBeyani      : Bool := false  -- Salih bu push/merge için açık beyan verdi
  salihIsAdiyla    : Bool := false  -- Salih bu force/discard işini adıyla söyledi
  canliParalel     : Bool := false  -- başka ajan/oturum canlı (acilis-kapilari K1)
  anaSira          : Bool := false  -- işlemi yapan Jarvis ana-sıra
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

theorem push_beyansiz_yok (b : Baglam) (h : b.salihBeyani = false) : izin .push b = false := by
  simp [izin, h]

theorem merge_yalniz_anasira (b : Baglam) (h : b.anaSira = false) : izin .merge b = false := by
  simp [izin, h]

theorem force_adsiz_yok (b : Baglam) (h : b.salihIsAdiyla = false) : izin .force b = false ∧ izin .discard b = false := by
  simp [izin, h]

example : mesajGecerli "[icra] Close durum #8" true = true := by native_decide
example : mesajGecerli "[icra] a — b" true = false := by native_decide
example : mesajGecerli "fix: x" true = false := by native_decide

end Kanon.Commit
