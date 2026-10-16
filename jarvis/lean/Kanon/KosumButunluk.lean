/-
Kanon.KosumButunluk — koşum emri bütünlüğü ve koşum tavanı freni (tüzük m.46 (a)-(d); K2 masası, Karar 39, Karar 83 A4, 08-31 B hükmü),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 2, 2026-10-16. Uygulayan kod: kod/hook/src/ajan_fren.rs (PreToolUse Agent sayacı;
env JARVIS_FREN_UYARI/DURDUR/KAPALI), cc/workflow/fren-sablonu.js (Workflow).
Türkçe özet (geri-çeviri): koşucu ilk adımda emri okur, künyesini (yol, ilk başlık, SHA) rapora yazar; emir bulunamaz ya da SHA tutmazsa
durur. Künye yalnız arama özetinden geldiyse [K] damgası zorunlu, [D-belge] yalnız birincil metne inildiyse. Koşum tavanı/bütçesi
rejime bağlıdır, her koşum rejim etiketi taşır, etiketsiz tavan beyanı geçersizdir; rejimi yalnız Salih değiştirir. Fren uç eşiklidir
(yalnız aşırı uçta çalışır): oturum başına Agent çağrısı 72'de uyarı, 144'te durdur (Salih 2026-08-31 B hükmü: iki katmanlı koşum
için 2× çarpan; Salih 2026-10-16: "72/144'den devam"); ajan başına 54 araç çağrısı, workflow başına 570, workflow başına 36 ajan uyarı
eşiğidir. Eşikler model kuşağına bağlı sabitlerdir; güncellik Kanon.Sabitler kaydında izlenir.
-/
namespace Kanon.KosumButunluk

/-- (a) bant-dışı erişim doğrulama -/
structure Kunye where
  emirBulundu : Bool
  shaEsit     : Bool
  deriving Repr

inductive Baslangic | devam | durArizaBildir
  deriving Repr, DecidableEq

def baslangic (k : Kunye) : Baslangic := if k.emirBulundu && k.shaEsit then .devam else .durArizaBildir

/-- (b) damga: yalnız arama özetinden geldiyse [K]; birincil metne inildiyse [D-belge] izinli. -/
inductive Damga | k | dBelge
  deriving Repr, DecidableEq

def damgaIzinli (birincilOkundu : Bool) : Damga → Bool
  | .k => true
  | .dBelge => birincilOkundu

/-- (d) uç eşikler (oturum başı Agent sayacı; 08-31 B hükmü, 10-16 teyit). -/
def uyariEsik : Nat := 72
def durdurEsik : Nat := 144
def ajanBasiAracCagrisi : Nat := 54
def workflowBasiCagri : Nat := 570
def workflowBasiAjan : Nat := 36

inductive Fren | gec | uyar | durdur
  deriving Repr, DecidableEq

/-- Sayaç hükmü; kapalı (Salih beyanı, JARVIS_FREN_KAPALI=1) → geç. -/
def fren (sayac : Nat) (kapali : Bool) : Fren :=
  if kapali then .gec
  else if sayac ≥ durdurEsik then .durdur
  else if sayac ≥ uyariEsik then .uyar
  else .gec

/-- (d) etiketsiz tavan beyanı geçersiz. -/
def tavanGecerli (rejimEtiketi : Bool) : Bool := rejimEtiketi

theorem sha_tutmazsa_dur (b : Bool) : baslangic ⟨b, false⟩ = .durArizaBildir := by
  simp [baslangic]

theorem ozetten_dbelge_yok : damgaIzinli false .dBelge = false := rfl

theorem esik_altinda_gecer (s : Nat) (h : s < 72) : fren s false = .gec := by
  have h1 : ¬ s ≥ 144 := by omega
  have h2 : ¬ s ≥ 72 := by omega
  simp [fren, durdurEsik, uyariEsik, h1, h2]

theorem uc_esikte_durur (s : Nat) (h : s ≥ 144) : fren s false = .durdur := by
  simp [fren, durdurEsik, h]

end Kanon.KosumButunluk
