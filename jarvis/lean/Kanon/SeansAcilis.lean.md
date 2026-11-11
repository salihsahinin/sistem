/-
Kanon.SeansAcilis — seans açılış kapıları (.claude/skills/seans-acilis/SKILL.md §1-§2; KB-08, İB-91, Karar 57, Karar 62, İB-89),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 1, 2026-10-16. Ölçümleri `tools/acilis-kapilari.py` üretir (K1 canlı-oturum, K2 manifest,
K3 silver); bu modül yalnız hükmü verir.
Türkçe özet (geri-çeviri): staj klasöründen ya da "staj" beyanıyla açılan oturumda ritüel koşmaz (staj akışı). Kanona erişim yoksa
SNAPSHOT kipi: kalıcı karar yok. "seans başı, <öğrenme şeridi>" ise ritüel değil `ogren`. Aksi hâlde ritüel: K1 şüphe → tek soru +
pathspec commit; K3 bayat → `katman-hatti.py` koş; koşum açmadan önce K2 koşmuş-aday → manifesti devral, yeniden koşma.
-/
namespace Kanon.SeansAcilis

structure Girdi where
  stajKlasoru     : Bool := false
  stajBeyani      : Bool := false
  kanonErisimi    : Bool := true
  ogrenmeSeridi   : Bool := false  -- "seans başı, <evals|guvenlik|...>"
  deriving Repr

inductive Yol | staj | snapshot | ogren | rituel
  deriving Repr, DecidableEq

/-- First hit-policy: staj > erişim yok > öğrenme şeridi > ritüel. -/
def yol (g : Girdi) : Yol :=
  if g.stajKlasoru || g.stajBeyani then .staj
  else if !g.kanonErisimi then .snapshot
  else if g.ogrenmeSeridi then .ogren
  else .rituel

/-- Kapı ölçümleri (acilis-kapilari.py çıktısı). -/
structure Kapilar where
  k1Suphe       : Bool := false
  k2KosmusAday  : Bool := false  -- yalnız --is "<konu>" verildiyse anlamlı
  k3Bayat       : Bool := false
  deriving Repr

structure Eylemler where
  tekSoru        : Bool
  pathspecCommit : Bool
  katmanHatti    : Bool
  kosumuDevral   : Bool
  deriving Repr, DecidableEq

def eylemler (k : Kapilar) : Eylemler :=
  { tekSoru := k.k1Suphe, pathspecCommit := k.k1Suphe, katmanHatti := k.k3Bayat, kosumuDevral := k.k2KosmusAday }

theorem staj_rituel_kosmaz (g : Girdi) (h : g.stajBeyani = true) : yol g = .staj := by
  simp [yol, h]

theorem snapshot_karar_yok (g : Girdi) (hs : g.stajKlasoru = false) (hb : g.stajBeyani = false) (he : g.kanonErisimi = false) :
    yol g = .snapshot := by
  simp [yol, hs, hb, he]

/-- Koşmuş aday varsa koşum devralınır (vaka-3: 518k mükerrer). -/
theorem kosmus_aday_devral (k : Kapilar) (h : k.k2KosmusAday = true) : (eylemler k).kosumuDevral = true := by
  simp [eylemler, h]

end Kanon.SeansAcilis
