/-
Kanon.KatmanYuklem — veri katmanı done-yüklemleri (core/veri-muhendisligi-katmani.md §2) ve T-A triyaj şiddeti (§8b; Karar 88 M13),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 3, 2026-10-16. Ölçümleri tools/silver-saglik.py, katman-hatti.py, katman-olcum.py,
ta-triyaj.py üretir; bu modül hükmü verir.
Türkçe özet (geri-çeviri): bronz kayıt git-izlenen, ekleme-esaslı, ham korunmuş ve SHA provenanslı olmalı; ham gövdeye elle temizlik
yasak. Silver tablo kaynağa 1:1 eşlenir (grain korunur), tipli, tekil anahtarlı, null politikası tanımlı, agrege değil, script ile
türetilmiş ve iki damgalı (kod SHA + girdi SHA), veri testleri ve şekil sözleşmesi geçmiş olmalı; JOIN/agregasyon yasak (tek istisna
simetrik kaynak birleşimi). Gold metrik tek yerde tanımlı, iş sorusuna hizalı, silver'a geri eşlenebilir ve şekil sözleşmeli olmalı;
elle üretilmiş sayı yasak. T-A triyajında çift şiddeti (uzunluk_a + uzunluk_b) × anahtar terim tekrarıdır, sıra azalan.
-/
namespace Kanon.KatmanYuklem

structure Bronz where
  gitIzlenen   : Bool
  eklemeEsasli : Bool
  hamKorunur   : Bool
  shaProvenans : Bool
  elleTemizlik : Bool := false
  deriving Repr

def bronzDone (b : Bronz) : Bool := b.gitIzlenen && b.eklemeEsasli && b.hamKorunur && b.shaProvenans && !b.elleTemizlik

structure Silver where
  birebir        : Bool
  tipli          : Bool
  tekil          : Bool
  nullPolitikasi : Bool
  agrege         : Bool := false
  scriptTuretim  : Bool
  ikiDamga       : Bool
  veriTesti      : Bool
  sekilSozlesme  : Bool
  joinVar        : Bool := false
  simetrikUnion  : Bool := false
  deriving Repr

def silverDone (s : Silver) : Bool :=
  s.birebir && s.tipli && s.tekil && s.nullPolitikasi && !s.agrege && s.scriptTuretim && s.ikiDamga &&
  s.veriTesti && s.sekilSozlesme && (!s.joinVar || s.simetrikUnion)

structure Gold where
  tekTanim       : Bool
  isSorusu       : Bool
  geriEslenir    : Bool
  sekilSozlesme  : Bool
  elleSayi       : Bool := false
  deriving Repr

def goldDone (g : Gold) : Bool := g.tekTanim && g.isSorusu && g.geriEslenir && g.sekilSozlesme && !g.elleSayi

/-- §8b şiddet := (uzunluk_a + uzunluk_b) × tekrar -/
def siddet (uzA uzB tekrar : Nat) : Nat := (uzA + uzB) * tekrar

theorem agrege_silver_degil (s : Silver) (h : s.agrege = true) : silverDone s = false := by
  simp [silverDone, h]

theorem elle_sayi_gold_degil (g : Gold) (h : g.elleSayi = true) : goldDone g = false := by
  simp [goldDone, h]

end Kanon.KatmanYuklem
