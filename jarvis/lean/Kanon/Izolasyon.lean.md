/-
Kanon.Izolasyon — ajan okuma/yazma yetki matrisi (kök AGENTS md.1, 14, 15; Karar 91/101/103 M3/105 M6; alt-ajan kilidi İB-83),
Lean 4 kod tabanı. Karar 114 geçiş turu parti 1, 2026-10-16. Uygulayan kod: alan ajanlarında `.claude/hooks/okuma-izin.sh`
(tek kaynak friday kopyası), Jarvis'te `kod/hook/src/altajan_okuma.rs` + `core_tel.rs`; kök giriş `bin/hook-dispatch.sh`.
Türkçe özet (geri-çeviri): okuma: ajan kendi dizinini, depo kökünün doğrudan altındaki kanon dosyalarını (AGENTS.md, CLAUDE.md,
README.md), kök `sablonlar/`, geçici dizinleri ve `.claude/okuma-izin-ek`'te listelenen ortak kaynakları okur; başka ajanın dizini
okunmaz. Jarvis kanon bakıcısı olarak her yeri okur. `ogrenme/` Salih'indir, okuma-izin-ek'te açılmadıkça ajanlara kapalı. Alt-ajan
(işçi) ayrıca başka oturum transkriptini, Jarvis sıcak hafızasını, olay kütüklerini ve `cc/gelen/` emirlerini okuyamaz. Yazma: her
dosyanın yazarı dizin sahibi ajandır (tek-yazar); istisna: Jarvis kök kanonu ve `<ajan>/AGENTS.md`'yi Salih imzasıyla yazar; başka
ajana iş `cc/gelen/` devir dosyasıyla gider. `ogrenme/` ve `sablonlar/` ajan yazımına kapalı (Jarvis şablonu Salih imzasıyla).
-/
namespace Kanon.Izolasyon

inductive Ajan | jarvis | friday | alan (ad : String)
  deriving Repr, DecidableEq

/-- Hedef yolun sınıfı (yol → sınıf eşlemesi hook'ta; burada hüküm). -/
inductive Yer
  | kendiDizini
  | baskaAjanDizini
  | kokKanonDosyasi      -- depo kökünün doğrudan altındaki dosya (AGENTS.md, CLAUDE.md, README.md)
  | sablonlar
  | ogrenme
  | ekIzinli             -- .claude/okuma-izin-ek'te listeli ortak kaynak
  | gecici               -- /tmp, harness araç çıktısı
  | baskaAjanAgentsMd    -- <başka ajan>/AGENTS.md (kanon dosyası)
  deriving Repr, DecidableEq

/-- Alt-ajanın ek yasakları (agent_id varken). -/
inductive AltajanYasak | transkript | sicakHafiza | olayKutugu | gelenEmir | yok
  deriving Repr, DecidableEq

def okuyabilir (a : Ajan) (y : Yer) : Bool :=
  match a, y with
  | .jarvis, _                 => true
  | _, .kendiDizini            => true
  | _, .kokKanonDosyasi        => true
  | _, .sablonlar              => true
  | _, .ekIzinli               => true
  | _, .gecici                 => true
  | _, _                       => false

/-- Alt-ajan: ana kural ∧ ek yasak yok. -/
def altajanOkuyabilir (a : Ajan) (y : Yer) (ek : AltajanYasak) : Bool := okuyabilir a y && ek == .yok

def yazabilir (a : Ajan) (y : Yer) (salihImzasi : Bool) : Bool :=
  match a, y with
  | _, .kendiDizini              => true
  | _, .gecici                   => true
  | .jarvis, .kokKanonDosyasi    => salihImzasi
  | .jarvis, .baskaAjanAgentsMd  => salihImzasi
  | .jarvis, .sablonlar          => salihImzasi
  | _, _                         => false

theorem baska_ajan_okunmaz (ad : String) : okuyabilir (.alan ad) .baskaAjanDizini = false := rfl
theorem ogrenme_ajana_kapali (ad : String) : okuyabilir (.alan ad) .ogrenme = false := rfl
theorem friday_jarvisi_okumaz : okuyabilir .friday .baskaAjanDizini = false := rfl

/-- Tek-yazar: Jarvis dışında hiçbir ajan kendi dizini ve geçici dışına yazamaz. -/
theorem tek_yazar (a : Ajan) (y : Yer) (s : Bool) (ha : a ≠ .jarvis) (h : yazabilir a y s = true) :
    y = .kendiDizini ∨ y = .gecici := by
  cases a <;> cases y <;> simp_all [yazabilir]

/-- Jarvis'in kanon yazımı Salih imzasına bağlı. -/
theorem jarvis_kanon_imzali : yazabilir .jarvis .kokKanonDosyasi false = false := rfl

end Kanon.Izolasyon
