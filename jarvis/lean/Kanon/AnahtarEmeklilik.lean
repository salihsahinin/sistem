/-
Kanon.AnahtarEmeklilik — bağlam anahtarı emeklilik protokolü ve eşik merdiveni (core/baglam-anahtar-kaydi.md §3-§4), Lean 4 kod tabanı.
Karar 114 geçiş turu parti 3, 2026-10-16. Uygulayan kod: tools/anahtar-denetim.py (çıkış 0 temiz · 1 sıcak ihlal ∨ bütünlük · 2 kullanım),
tools/anahtar-cascade.py. Anahtar kaydının kendisi (§2 JSON) veridir, md'de kalır.
Türkçe özet (geri-çeviri): bir ad/tetik/kural değişince sıra: kayıt satırı (emekli + tekil halef) → denetim-önce → sıcak katmanda
yayılım → tetik eval güncellemesi → denetim-sonra ve commit. Sıcak katmanda kalıntı 0 değilse emeklilik tamamlanmamış sayılır ve commit
`KISMİ` damgası alır. Ilık katmanda 1 kalıntı uyarı, 10 kalıntı aynı vardiyada eylem. Soğuk katman tarihçedir, eşiksiz. Halefsiz emekli,
damgasız kayıt ve aynı kavramı taşıyan iki anahtar kabul edilmez (0). Kaldırma en erken 3 vardiya sonra.
-/
namespace Kanon.AnahtarEmeklilik

inductive Adim | kayit | denetimOnce | yayilim | tetikEval | denetimSonraCommit | kaldirma
  deriving Repr, DecidableEq

def sira : List Adim := [.kayit, .denetimOnce, .yayilim, .tetikEval, .denetimSonraCommit, .kaldirma]

inductive Commit | tam | kismi
  deriving Repr, DecidableEq

def commitDamgasi (sicakIhlal : Nat) : Commit := if sicakIhlal = 0 then .tam else .kismi

inductive Ilik | temiz | uyari | eylem
  deriving Repr, DecidableEq

def k1 : Nat := 1
def k2 : Nat := 10

def ilik (kalinti : Nat) : Ilik := if kalinti ≥ k2 then .eylem else if kalinti ≥ k1 then .uyari else .temiz

structure Butunluk where
  halefsizEmekli : Nat := 0
  damgasizKayit  : Nat := 0
  tekillikB      : Nat := 0
  deriving Repr

def butunlukTemiz (b : Butunluk) : Bool := b.halefsizEmekli == 0 && b.damgasizKayit == 0 && b.tekillikB == 0

/-- anahtar-denetim.py çıkış kodu: sıcak ihlal ∨ bütünlük hatası → 1, aksi 0 -/
def cikis (sicakIhlal : Nat) (b : Butunluk) : Nat := if sicakIhlal = 0 && butunlukTemiz b then 0 else 1

def kaldirmaIzinli (gecenVardiya : Nat) : Bool := decide (gecenVardiya ≥ 3)

theorem sicak_kalinti_kismi (n : Nat) (h : n > 0) : commitDamgasi n = .kismi := by
  have : n ≠ 0 := by omega
  simp [commitDamgasi, this]

end Kanon.AnahtarEmeklilik
