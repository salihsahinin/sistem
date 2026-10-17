/-
Kanon.DeterministikTasarim — deterministik tasarım ilkesi ve uygulama kapsamı (core/deterministik-tasarim.md §1-§3; Salih 08-17 Katman-1, Karar 65, Salih 09-10 kapsam daraltması),
Lean 4 kod tabanı. Karar 117, 2026-10-17. Gerekçe, Salih beyanı ve bağlı kayıtlar md'de kalır.
Türkçe özet (geri-çeviri): ilke yalnız dört iş türünde uygulanır: script/araç yazımı (idempotens ∧ aynı girdi aynı çıktı), ölçüm ve katman koşumları,
ajan emri derleme ile pipeline/workflow tasarımı (dallar yazılı, tetik yüklemi boolean, "hakeme sor / dağılım çıkar" tasarım aracı değil), kanon ölçüm iddiaları
(tekrar-üretilebilir kayıt yoksa `[?]`). Sohbet, öğretim, karar sunumu, rapor anlatımı, günlük planlama ve Salih sorularına cevapta ilke sessizdir;
stokastik seçenek masaya gelirse ilke yalnız o kalemde tek cümleyle anılır. Deterministik yol varsa stokastik yol seçilmez.
-/
namespace Kanon.DeterministikTasarim

/-- §2 + §3: iş türleri; ilk dört §2 tetiği, kalan altısı §3 vurgusuz bağlamlar. -/
inductive IsTuru
  | scriptArac | olcumKatman | emirPipeline | kanonOlcumIddia
  | sohbet | ogretim | kararSunum | raporAnlati | gunlukPlan | salihCevap
  deriving Repr, DecidableEq

/-- §2: ilke yalnız bu iş türlerinde uygulanır. -/
def uygulanir : IsTuru → Bool
  | .scriptArac | .olcumKatman | .emirPipeline | .kanonOlcumIddia => true
  | _ => false

/-- §3: vurgu ⟺ uygulama; sessiz bağlamda gerekçe cümlesi de her seçeneğe süzgeç de yok. -/
def vurgulanir (t : IsTuru) : Bool := uygulanir t

/-- §3: sessiz bağlamda stokastik seçenek masaya gelirse ilke yalnız o kalemde, tek cümleyle anılır. -/
inductive Anma | yok | tekCumleKalemde | tamUygulama
  deriving Repr, DecidableEq

def anma (t : IsTuru) (stokastikSecenekVar : Bool) : Anma :=
  if uygulanir t then .tamUygulama
  else if stokastikSecenekVar then .tekCumleKalemde
  else .yok

/-- §1 (Karar 65): deterministik yol varsa stokastik yol seçilmez. -/
inductive Yol | deterministik | stokastik
  deriving Repr, DecidableEq

def yolSecimi (deterministikYolVar : Bool) : Yol :=
  if deterministikYolVar then .deterministik else .stokastik

/-- §2.1: script/araç done-yüklemi := idempotens ∧ aynı girdi aynı çıktı. -/
def scriptDone (idempotens ayniGirdiAyniCikti : Bool) : Bool := idempotens && ayniGirdiAyniCikti

/-- §2.2: ölçüm/katman koşumunda yeniden türetim el birleştirmesi olmadan yapılır (Karar 77). -/
def olcumDone (yenidenTuretimElsiz : Bool) : Bool := yenidenTuretimElsiz

/-- §2.3: emir/pipeline tasarımı := dallar yazılı ∧ tetik yüklemi boolean ∧ ¬(hakeme sor / dağılım çıkar tasarım aracı). -/
structure EmirTasarim where
  dallarYazili     : Bool
  tetikBoolean     : Bool
  hakemDagilimAraci : Bool := false
  deriving Repr

def emirTasarimDone (e : EmirTasarim) : Bool := e.dallarYazili && e.tetikBoolean && !e.hakemDagilimAraci

/-- §2.4: kanon ölçüm iddiası (m.29/m.39 rakam) tekrar-üretilebilir kayıt yoksa `[?]` taşır. -/
inductive Damga | kayitli | soru
  deriving Repr, DecidableEq

def olcumDamgasi (tekrarUretilebilirKayit : Bool) : Damga :=
  if tekrarUretilebilirKayit then .kayitli else .soru

theorem sohbet_sessiz : vurgulanir .sohbet = false := rfl
theorem salih_cevabi_sessiz : vurgulanir .salihCevap = false := rfl
theorem script_vurgulu : vurgulanir .scriptArac = true := rfl
theorem sessiz_baglam_stokastikte_tek_cumle (t : IsTuru) (h : uygulanir t = false) :
    anma t true = .tekCumleKalemde := by simp [anma, h]
theorem deterministik_varsa_stokastik_degil : yolSecimi true = .deterministik := rfl
theorem hakem_araci_emri_bozar (e : EmirTasarim) (h : e.hakemDagilimAraci = true) : emirTasarimDone e = false := by
  simp [emirTasarimDone, h]
theorem kayitsiz_rakam_soru : olcumDamgasi false = .soru := rfl

end Kanon.DeterministikTasarim
