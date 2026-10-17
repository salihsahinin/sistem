/-
Kanon.AjanKaliciligi — ajan kalıcılığı, atama mimarisi, devretme merdiveni ve model hiyerarşisi (tüzük m.30 (a)-(d), ek fıkra canlı-ajan sınırı,
Karar 85/89 şerhleri, m.30b ↔ m.34 uzlaştırma dipnotu), Lean 4 kod tabanı. Karar 117 parti 4, 2026-10-17.
Uygulayan kod: PreToolUse policy-as-code kilidi (hook; m.31 Katman-1 eylemleri + m.23 yasakları, deterministik allowlist), ajan-metodolojisi §6.
Türkçe özet (geri-çeviri): atama yapılan ajan tanınmış olur; ekip lideri tek-görevlik olamaz. Kontrolün, durma-koşulunun ya da tetiğin
devri otomasyondur; promptun ya da kalıcı kimliğin devri canlı ajandır. Lojik çekirdek: özgürlük, hatanın toparlanabilirliğini aşamaz.
Gözetimsiz otomasyon açılmadan önce PreToolUse kilidi kurulu olmalıdır. Güncel hiyerarşi (Karar 89): ana-sıra, Opus lider (effort medium,
high yasak), Sonnet işçi, Haiku eval. Bir ingest varyantı kalıcılığı yalnız held-out'ta varsayılanı yenerek hak eder.
-/
namespace Kanon.AjanKaliciligi

/-- (a) kalıcılık: atanan ajan tanınmış olur; ekip lideri tek-görevlik olamaz. -/
structure Ajan where
  atandi      : Bool
  ekipLideri  : Bool
  tekGorevlik : Bool
  deriving Repr

def taninmis (a : Ajan) : Bool := a.atandi

def kaliciligaUygun (a : Ajan) : Bool := !(a.ekipLideri && a.tekGorevlik)

/-- Ek fıkra: devretme merdiveni. -/
inductive Devir | kontrol | durmaKosulu | tetik | prompt | kaliciKimlik
  deriving Repr, DecidableEq

inductive Sinif | otomasyon | canliAjan
  deriving Repr, DecidableEq

def sinif : Devir → Sinif
  | .kontrol | .durmaKosulu | .tetik => .otomasyon
  | .prompt | .kaliciKimlik => .canliAjan

/-- Lojik çekirdek (m.38): Özgürlük(a) ≤ Toparlanabilirlik(hata(a)); iki değer de sıralı Nat. -/
def sinirIcinde (ozgurluk toparlanabilirlik : Nat) : Bool := decide (ozgurluk ≤ toparlanabilirlik)

/-- Ön-koşul: gözetimsiz otomasyon dilimi, PreToolUse kilidi kurulmadan açılmaz. -/
def gozetimsizAcilabilir (pretoolKilidiKurulu : Bool) : Bool := pretoolKilidiKurulu

/-- Güncel hiyerarşi (Karar 89; Karar 85 şerhi süpersede). -/
inductive Model | haiku | sonnet | opus | fable
  deriving Repr, DecidableEq

inductive Rol | anaSira | lider | isci | eval
  deriving Repr, DecidableEq

inductive Effort | low | medium | high
  deriving Repr, DecidableEq

def rolModeli : Rol → Model
  | .anaSira => .fable
  | .lider => .opus
  | .isci => .sonnet
  | .eval => .haiku

/-- Lider effort'u medium sabittir; high yasak. -/
def effortUygun : Rol → Effort → Bool
  | .lider, e => decide (e = .medium)
  | .isci, e => decide (e = .low ∨ e = .medium)
  | _, _ => true

/-- m.30b ↔ m.34: varyant, held-out'ta varsayılanı yenerse kalıcılığı hak eder; aksi hâlde arşive iner. -/
def varyantHakEder (varyantSkor varsayilanSkor : Nat) : Bool := decide (varyantSkor > varsayilanSkor)

theorem ekip_lideri_tek_gorevlik_olamaz (a : Ajan) (h1 : a.ekipLideri = true) (h2 : a.tekGorevlik = true) :
    kaliciligaUygun a = false := by simp [kaliciligaUygun, h1, h2]

theorem prompt_devri_canli_ajan : sinif .prompt = .canliAjan := rfl
theorem tetik_devri_otomasyon : sinif .tetik = .otomasyon := rfl
theorem kilitsiz_gozetimsiz_yok : gozetimsizAcilabilir false = false := rfl
theorem lider_high_yasak : effortUygun .lider .high = false := by decide
theorem esit_skor_hak_etmez (s : Nat) : varyantHakEder s s = false := by simp [varyantHakEder]

end Kanon.AjanKaliciligi
