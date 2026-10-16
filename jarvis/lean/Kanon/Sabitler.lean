/-
Kanon.Sabitler — model kuşağına bağlı sabitlerin güncellik kaydı (Karar 116, 2026-10-16), Lean 4 kod tabanı.
Salih 2026-10-16 aynen: "modeller exponansiyel bir şekilde gelişiyor, gittikçe daha zeki oluyor ve gittikçe daha ucuzlaşıyor. sistemin
kuralları eskimemeli güncelliğini korumalı".
Türkçe özet (geri-çeviri): bir kuralın sayısal sabiti bir model kuşağında ölçülmüş ya da seçilmişse bu kayda girer: ad, değer, hangi
modülde kullanıldığı, ölçüldüğü tarih (AS-OF), ölçüldüğü model kuşağı, kaynak (ölçüm / Salih beyanı / kanıtsız tercih). Sabit ya
(i) yeni bir model kuşağı devreye girince (veri/model-kesim.jsonl değişimi) ya da (ii) AS-OF'tan 90 gün geçince "yeniden bak"
listesine düşer; seans açılışında listelenir. Yeniden bakmak değeri değiştirmek demek değil: ölçülür, Salih imzasıyla güncellenir
ya da AS-OF yenilenir. Yön beklentisi: modeller güçlendikçe frenler gevşer, maliyet eşikleri düşer, skill/kod eşiği aşağı iner.
-/
namespace Kanon.Sabitler

inductive Kaynak | olcum | salihBeyani | kanitsizTercih
  deriving Repr, DecidableEq

structure Sabit where
  ad      : String
  deger   : String
  modul   : String
  asOf    : String   -- YYYY-MM-DD
  kusak   : String   -- ölçüldüğü/seçildiği model kuşağı
  kaynak  : Kaynak
  deriving Repr

def gozdenGecirmeGun : Nat := 90

def kayit : List Sabit := [
  ⟨"fren.uyari",            "72",   "KosumButunluk", "2026-08-31", "Fable 5 / Opus 5 / Sonnet 5", .salihBeyani⟩,
  ⟨"fren.durdur",           "144",  "KosumButunluk", "2026-08-31", "Fable 5 / Opus 5 / Sonnet 5", .salihBeyani⟩,
  ⟨"fren.ajanBasiArac",     "54",   "KosumButunluk", "2026-08-30", "Fable 5 / Opus 5 / Sonnet 5", .olcum⟩,
  ⟨"fren.workflowBasiAjan", "36",   "KosumButunluk", "2026-08-30", "Fable 5 / Opus 5 / Sonnet 5", .olcum⟩,
  ⟨"halusinasyon.esik",     "7/4",  "Halusinasyon",  "2026-08-14", "Fable 5", .kanitsizTercih⟩,
  ⟨"halusinasyon.agirlik",  "v1..v10", "Halusinasyon", "2026-08-14", "Fable 5", .kanitsizTercih⟩,
  ⟨"skill.adayN",           "3",    "SkillDogum",    "2026-08-29", "Fable 5", .salihBeyani⟩,
  ⟨"skill.sapma",           "n≥10, 2×", "Delegasyon", "2026-08-21", "Fable 5", .salihBeyani⟩,
  ⟨"efor.cetvel",           "1 / 2-4 / 10+", "Delegasyon", "2026-08-14", "Claude 4 kuşağı (Anthropic raporu)", .olcum⟩,
  ⟨"skillTetik.retry",      "3",    "SkillTetik",    "2026-08-15", "çerçeve varsayılanı (CrewAI)", .kanitsizTercih⟩,
  ⟨"skillTetik.dal",        "≤5 dal, ≤2 derinlik", "SkillTetik", "2026-08-15", "ComplexBench / Multi-IF kohortu", .olcum⟩,
  ⟨"skillKapi.kTau",        "3",    "SkillKapi",     "2026-08-29", "Fable 5", .salihBeyani⟩
]

inductive Neden | yeniKusak | sureDoldu
  deriving Repr, DecidableEq

/-- Yeniden-bak kuralı := yeni kuşak devrede ∨ AS-OF'tan bu yana gün ≥ 90 (gün farkı çağırandan gelir). -/
def yenidenBak (yeniKusak : Bool) (gecenGun : Nat) : Option Neden :=
  if yeniKusak then some .yeniKusak
  else if gecenGun ≥ gozdenGecirmeGun then some .sureDoldu
  else none

theorem taze_sabit_listelenmez : yenidenBak false 10 = none := by decide

end Kanon.Sabitler
