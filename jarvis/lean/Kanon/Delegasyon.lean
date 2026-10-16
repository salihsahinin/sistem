/-
Kanon.Delegasyon — basamak geçişi, lider/işçi delegasyon kuralları (core/ajan-metodolojisi.md §3-§4; Karar 48, 51, 89, 106),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 2, 2026-10-16. Uygulayan kod: tools/skill-esik.py (eşik), tools/paralel-kapi.py,
kod/hook/src/ajan_fren.rs (sayaç). Gerekçe ve kaynaklar (Anthropic, Cognition, CrewAI, awm) md'de.
Türkçe özet (geri-çeviri): bir adım ancak adım sayısı önceden tahmin edilebiliyor, sabit yol kodlanabiliyor ve model kararı
gerekmiyorsa bir basamak yukarı (koda) çıkar. İşçi görevi dört alanı (hedef, çıktı biçimi + bütçe, araç/kaynak kılavuzu, görev
sınırları) eksiksiz taşımadan dağıtılmaz. Alt görevler bağımsız bilgi topluyorsa paralel, ortak çıktı üretiyorsa tek şerit ya da
paylaşılan karar manifesti. İşçi liderden pahalı modelde koşamaz. Delegasyon varsayılan kapalıdır; işçi işçi doğuramaz, lider açıkça
yetki verir. Model kendi çıktısını analiz etmez (deterministik doğrulama ve dönemlik toplu özet hariç). Skill×model çifti n ≥ 10
olunca medyan bandı hesaplanır, koşum bandın 2 katını aşarsa kapanışta sapma satırı yazılır; kural otomatik değişmez.
Efor cetveli: basit iş 1 ajan, kıyas 2-4, karmaşık 10+.
-/
namespace Kanon.Delegasyon

/-- §3 basamak-geçiş kapısı := adım tahmin edilebilir ∧ sabit yol kodlanabilir ∧ ¬model kararı gerekir -/
def yukariCik (adimTahmin sabitYol modelKarari : Bool) : Bool := adimTahmin && sabitYol && !modelKarari

structure Sozlesme where
  hedef       : Bool := false
  ciktiBicimi : Bool := false   -- biçim + bütçe
  aracKilavuz : Bool := false
  sinirlar    : Bool := false   -- "sana ait olmayan" dahil
  deriving Repr

def sozlesmeTam (s : Sozlesme) : Bool := s.hedef && s.ciktiBicimi && s.aracKilavuz && s.sinirlar

inductive Dagitim | paralel | tekSerit
  deriving Repr, DecidableEq

/-- Paralellik-uygunluk: bağımsız keşif → paralel; ortak üretim → tek şerit (paylaşılan manifest yoksa). -/
def dagitim (ortakCikti paylasilanManifest : Bool) : Dagitim :=
  if ortakCikti && !paylasilanManifest then .tekSerit else .paralel

/-- Model kademesi (Karar 89 + 106): büyük sayı = pahalı. -/
inductive Model | haiku | sonnet | opus | fable
  deriving Repr, DecidableEq

def kademe : Model → Nat
  | .haiku => 0 | .sonnet => 1 | .opus => 2 | .fable => 3

/-- Maliyet tavanı: işçi ≤ lider. -/
def modelUygun (lider isci : Model) : Bool := decide (kademe isci ≤ kademe lider)

/-- Delegasyon varsayılan kapalı: işçi alt-ajan doğurabilir ⟺ lider açık yetki verdi. -/
def isciDogurabilir (liderYetkisi : Bool) : Bool := liderYetkisi

/-- Kendini analiz kısıtı (Karar 48): kendi çıktısı ise yalnız deterministik doğrulama ya da dönemlik toplu özet serbest. -/
def analizSerbest (kendiCiktisi deterministik donemlikToplu : Bool) : Bool := !kendiCiktisi || deterministik || donemlikToplu

/-- Skill eşik kuralı (Karar 51): n ≥ 10 ∧ koşum > 2 × medyan → sapma satırı. -/
def sapma (n medyan kosum : Nat) : Bool := decide (n ≥ 10) && decide (kosum > 2 * medyan)

inductive Is | basit | kiyas | karmasik
  deriving Repr, DecidableEq

/-- Efor cetveli: (en az, en çok) ajan; karmaşıkta üst sınır yok (none). -/
def efor : Is → Nat × Option Nat
  | .basit => (1, some 1) | .kiyas => (2, some 4) | .karmasik => (10, none)

theorem isci_liderden_pahali_degil : modelUygun .sonnet .opus = false := rfl
theorem eksik_sinir_dagitilmaz (s : Sozlesme) (h : s.sinirlar = false) : sozlesmeTam s = false := by
  simp [sozlesmeTam, h]
theorem varsayilan_kapali : isciDogurabilir false = false := rfl
theorem az_ornekte_sapma_yok (m k : Nat) : sapma 9 m k = false := by simp [sapma]

end Kanon.Delegasyon
