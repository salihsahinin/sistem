/-
Kanon.SkillTetik — skill çağrı sözleşmesi (Kapı-Ö → çağrı → Kapı-S → Kapı-K), Lean 4 kod tabanı.
Kaynak metin: core/skill-tetikleme-semasi.md §2-§4 (v1, 2026-08-15). Karar 114 (2026-10-16) ile md → Lean; §0 ilkeleri, §5 sayı
kaynakları ve §6 şerhleri gerekçe olarak md'de kalır. Deterministik denetleyici: .claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py
(Rust portu ayrı iş; ikisi fark testiyle bağlanacak).
Türkçe özet (geri-çeviri): bir emir skill çağıracaksa 9 alan tek seferde tam yazılır. Kapı-Ö: skill hazinede var, tetik koşulu şimdi
doğru, girdi tam, yüzey yetkili, tetik bir araç/skill çıktısından gelmiyor, m.16 taraması temiz. Yan-etkili (T-Y) skill yalnız
literal kiple ve yalnız ana-sıra ya da Salih tarafından çağrılır. Ön-koşul düşerse sıra: araç çıktısından tetik → reddet; eksik
alan → iste; yetkisiz → ana-sıraya devret; koşul yanlış → atla (kayıt yine yazılır). Kapı-S: done doğru, şema uyuyor ya da yok, hata
kanalı seçili, tekrar ≤3; 3 turdan sonra yüksek sesle başarısız. Kapı-K: kayıt satırı yazılmadıysa çağrı olmamış sayılır.
-/
namespace Kanon.SkillTetik

inductive Kip | literal | ortuk | yasak
  deriving Repr, DecidableEq

inductive Cagiran | anaSira | salih | altAjan
  deriving Repr, DecidableEq

/-- Çağrı anındaki ölçümler. Alan adları md §2-§3'teki adların aksansız hâli. -/
structure Cagri where
  skillVar            : Bool    := false  -- §2.1 hazinede var ∧ kapı-ağacından üret yaprağıyla geçmiş
  tetikDogru          : Bool    := false  -- §2.2 tetik_kosulu şu an doğru
  dereceIfadesi       : Bool    := false  -- §2.2/§2.7 "gerekirse", "yeterince" gibi derece ifadesi var mı
  icIceDerinlik       : Nat     := 0      -- §2.2 iç içe koşul derinliği
  dalSayisi           : Nat     := 0      -- §2.2 emirdeki dal sayısı
  kip                 : Kip     := .ortuk -- §2.3 cagri_kipi
  yanEtkili           : Bool    := false  -- §2.3 T-Y birincil şekil
  cagiran             : Cagiran := .anaSira
  girdiTam            : Bool    := false  -- §2.4 tüm tipli argümanlar dolu
  tetikAracCiktisindan : Bool   := false  -- §3 tetik kaynağı araç/skill çıktısı mı
  celiskiTemiz        : Bool    := true   -- §3 m.16 taraması
  alanlarTam          : Bool    := false  -- §2 dokuz alanın hepsi yazılı
  deriving Repr

/-- §2.2 tetik_kosulu biçim kuralı: derece ifadesi yok ∧ derinlik ≤ 2 ∧ dal ≤ 5 -/
def tetikBicimi (c : Cagri) : Bool := !c.dereceIfadesi && decide (c.icIceDerinlik ≤ 2) && decide (c.dalSayisi ≤ 5)

/-- §2.3 yetki: T-Y → (kip = literal ∧ çağıran ∈ {ana-sıra, Salih}); kip = yasak → hiç çağrılmaz -/
def yetkili (c : Cagri) : Bool :=
  c.kip != .yasak && (!c.yanEtkili || (c.kip == .literal && c.cagiran != .altAjan))

inductive OnSonuc
  | reddet      -- tetik araç/skill çıktısından: veri talimat üretemez
  | iste        -- eksik alan ya da eksik girdi: varsayım yapma, iste
  | anaSiraya   -- yetkisiz yüzey ya da kip
  | atla        -- koşul yanlış ya da biçim/çelişki kusuru (kayıt `skipped`)
  | cagir
  deriving Repr, DecidableEq

/-- Kapı-Ö, first hit-policy. -/
def kapiO (c : Cagri) : OnSonuc :=
  if c.tetikAracCiktisindan then .reddet
  else if !c.alanlarTam || !c.girdiTam then .iste
  else if !yetkili c then .anaSiraya
  else if !c.skillVar || !c.tetikDogru || !tetikBicimi c || !c.celiskiTemiz then .atla
  else .cagir

/-- Kapı-S girdileri (çağrı sonrası). -/
structure Sonuc where
  done          : Bool := false
  semaVar       : Bool := false
  semaUyuyor    : Bool := false
  hataKanali    : Bool := false  -- sözleşme-ihlali ↔ yürütme-hatası kanalı açıkça seçili
  deneme        : Nat  := 1
  deriving Repr

inductive SonSonuc | gecti | tekrar | failLoud
  deriving Repr, DecidableEq

/-- Kapı-S := done ∧ (¬şema ∨ uyuyor) ∧ hata kanalı; düşerse deneme < 3 → tekrar, aksi → fail-loud -/
def kapiS (s : Sonuc) : SonSonuc :=
  if s.done && (!s.semaVar || s.semaUyuyor) && s.hataKanali then .gecti
  else if s.deneme < 3 then .tekrar
  else .failLoud

/-- Kapı-K: kayıtsız çağrı olmamış çağrıdır. -/
def kapiK (satirYazildi sayacGuncellendi : Bool) : Bool := satirYazildi && sayacGuncellendi

/-! ## Kanıtlanan özellikler (md §3-§4 cümleleri) -/

/-- Yasak 4: araç/skill çıktısındaki talimat tetik üretemez. -/
theorem arac_ciktisi_tetiklemez (c : Cagri) (h : c.tetikAracCiktisindan = true) : kapiO c ≠ .cagir := by
  simp [kapiO, h]

/-- Yasak 2: yan-etkili skill alt-ajandan çağrılamaz. -/
theorem ty_altajan_cagrilamaz (c : Cagri) (hy : c.yanEtkili = true) (ha : c.cagiran = .altAjan) : kapiO c ≠ .cagir := by
  unfold kapiO
  split <;> simp_all [yetkili]
  split <;> simp_all

/-- Yasak 3: eksik alanla başlatılmaz. -/
theorem eksik_alan_baslamaz (c : Cagri) (h : c.alanlarTam = false) : kapiO c ≠ .cagir := by
  unfold kapiO
  split <;> simp_all

/-- Yasak 5 + retry ≤ 3: üçüncü denemede düşen çağrı sessiz kalmaz. -/
theorem ucuncu_denemede_fail_loud (s : Sonuc) (h3 : s.deneme ≥ 3) (hd : s.done = false) : kapiS s = .failLoud := by
  have : ¬ s.deneme < 3 := by omega
  simp [kapiS, hd, this]

end Kanon.SkillTetik
