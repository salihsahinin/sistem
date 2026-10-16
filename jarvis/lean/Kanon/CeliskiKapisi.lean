/-
Kanon.CeliskiKapisi — denetim modeli ve çelişki kapısı (tüzük m.16; Salih 2026-07-11, V7↔V8↔V14 tek sorusunun cevabı),
Lean 4 kod tabanı. Karar 117 parti 2, 2026-10-16. Uygulayan kod: yok (kapı Jarvis'in elle uyguladığı kuraldır);
koşum talimatı .claude/skills/celiski-kapisi/SKILL.md.
Türkçe özet (geri-çeviri): denetçi ajan yalnız gözlemler, çıktısı yalnız rapor dosyasıdır ve üç durum kodundan birini taşır
(bilgi, uyarı, acil). Salih'in sözü emirdir ve son karardır; tek istisna çelişki kapısıdır: yeni karar daha önce alınmış bir
kararla çelişiyorsa karar üstüne karar alınmadan önce Jarvis çelişki + değişikliğin artı/eksisi + planı içeren raporu sunar,
Salih raporu görüp karar verir, ancak sonra icra edilir. Çelişki yoksa emir doğrudan icra edilir. Kapı bugünden yürürlüktedir
(elle); denetçi ajanın kendisi K-009/K-010 ön-koşulludur.
-/
namespace Kanon.CeliskiKapisi

/-- Denetçi raporunun durum kodu (m.16: bilgi / uyarı / acil). -/
inductive DurumKodu | bilgi | uyari | acil
  deriving Repr, DecidableEq

/-- Acil kod Salih'ten raporu okumasını talep eder; diğerleri talep etmez. -/
def okumaTalebi : DurumKodu → Bool
  | .acil => true
  | _ => false

/-- Denetçi ajanın çıktı yüzeyi: yalnız rapor dosyası; geliştirme sırasında muhatap olunmaz. -/
inductive DenetciCikti | raporDosyasi | baskaYuzey
  deriving Repr, DecidableEq

def denetciCiktiGecerli : DenetciCikti → Bool
  | .raporDosyasi => true
  | .baskaYuzey => false

/-- Çelişki kapısı girdisi: yeni karar önceki kararla (ör. tüzük maddesi) çelişiyor mu; rapor sunuldu mu; Salih karar verdi mi. -/
structure Karar where
  celisiyor      : Bool
  raporSunuldu   : Bool   -- çelişki + artı/eksi + plan
  salihKararVerdi : Bool  -- raporu görüp karar verdi
  deriving Repr

/-- Kapının çıktısı. -/
inductive Dal | dogrudanIcra | raporSun | salihKarariBekle | icra
  deriving Repr, DecidableEq

/-- Karar dalı: çelişki yoksa doğrudan icra; varsa önce rapor, sonra Salih kararı, sonra icra. -/
def dal (k : Karar) : Dal :=
  if !k.celisiyor then .dogrudanIcra
  else if !k.raporSunuldu then .raporSun
  else if !k.salihKararVerdi then .salihKarariBekle
  else .icra

/-- Rapor üç parçayı da taşımalıdır (çelişki, artı/eksi, plan). -/
structure Rapor where
  celiskiVar  : Bool
  artiEksiVar : Bool
  planVar     : Bool
  deriving Repr

def raporTam (r : Rapor) : Bool := r.celiskiVar && r.artiEksiVar && r.planVar

/-- Kapı bugünden yürürlüktedir; denetçi ajan K-009/K-010 ön-koşuludur (geri-açma). -/
def denetciAcilabilir (k009 k010 : Bool) : Bool := k009 && k010

/-- Çelişki varken doğrudan icra dalı üretilmez. -/
theorem celiskiVarkenDogrudanIcraYok (k : Karar) (h : k.celisiyor = true) :
    dal k ≠ .dogrudanIcra := by
  obtain ⟨c, r, d⟩ := k
  simp at h
  subst h
  cases r <;> cases d <;> simp [dal]

/-- Çelişki yokken kapı her zaman doğrudan icradır (tören raporu yok). -/
theorem celiskiYokkenDogrudanIcra (k : Karar) (h : k.celisiyor = false) :
    dal k = .dogrudanIcra := by
  simp [dal, h]

/-- İcra dalına ulaşan çelişkili karar rapor sunulmuş ve Salih karar vermiş olmalıdır. -/
theorem icraIcinRaporVeKarar (k : Karar) (hc : k.celisiyor = true) (h : dal k = .icra) :
    k.raporSunuldu = true ∧ k.salihKararVerdi = true := by
  obtain ⟨c, r, d⟩ := k
  simp at hc
  subst hc
  cases r <;> cases d <;> simp_all [dal]

end Kanon.CeliskiKapisi
