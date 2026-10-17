/-
Kanon.DosyaAciklama — dosya-açıklama standardı ve deneysel-veri meta kuralı (tüzük m.29; S5 cevabı, Salih 2026-07-11),
Lean 4 kod tabanı. Karar 117 parti 4, 2026-10-17. Uygulayan kod: yok (kural-ölçüt düzeyi; liste üreten script'ler bu yüklemi çağırabilir).
Türkçe özet (geri-çeviri): klasör/dosya listesinde açıklama varsayılan olarak 1 satırdır; yanlış-anlaşılma maliyeti yüksek
dosyada en çok 3 cümle ve işlev satırı yazılır; pointer her durumda zorunludur. Her biçim kararı deneysel damgalı başlar,
yalnız kullanım verisiyle kalibre edildikten sonra damga kalkar. Fitting algoritması kurulana dek eşikler sabit sayılmaz.
-/
namespace Kanon.DosyaAciklama

/-- Açıklama düzeyi: varsayılan 1 satır; geniş yalnız yanlış-anlaşılma maliyeti yüksekse. -/
inductive Duzey | varsayilan | genis
  deriving Repr, DecidableEq

/-- Açıklamanın ölçülen alanları. -/
structure Aciklama where
  satirSayisi  : Nat
  cumleSayisi  : Nat
  islevVar     : Bool
  pointerVar   : Bool
  deriving Repr

/-- Düzey seçimi: maliyet yüksekse geniş izinli, değilse varsayılan. -/
def duzey (yanlisAnlasilmaMaliyetiYuksek : Bool) : Duzey :=
  if yanlisAnlasilmaMaliyetiYuksek then .genis else .varsayilan

/-- Açıklama geçerli mi: pointer her durumda zorunlu; varsayılan 1 satır; geniş en çok 3 cümle + işlev. -/
def gecerli (d : Duzey) (a : Aciklama) : Bool :=
  a.pointerVar &&
    match d with
    | .varsayilan => decide (a.satirSayisi = 1)
    | .genis      => decide (a.cumleSayisi ≤ 3) && a.islevVar

/-- Biçim kararının damgası: yeni karar `deneysel` başlar, kullanım verisiyle `kalibre` olur. -/
inductive Damga | deneysel | kalibre
  deriving Repr, DecidableEq

structure BicimKarari where
  damga           : Damga
  kullanimVerisiVar : Bool
  deriving Repr

/-- Meta kural: yeni biçim kararı deneysel damgalı başlar; kalibre damga yalnız kullanım verisiyle. -/
def damgaGecerli (k : BicimKarari) : Bool :=
  match k.damga with
  | .deneysel => true
  | .kalibre  => k.kullanimVerisiVar

def baslangicDamgasi : Damga := .deneysel

end Kanon.DosyaAciklama
