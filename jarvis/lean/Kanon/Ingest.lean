/-
Kanon.Ingest — ingest kayıt katmanı (core/ingest-semasi.md v2 §1-§3, §5-§6; Karar 59, Karar 104 M2), Lean 4 kod tabanı.
Karar 114 geçiş turu parti 3, 2026-10-16. Gerekçe ve kaynaklar (ODCS, CloudEvents, Mem0, Generative Agents, MemGPT) md'de.
Türkçe özet (geri-çeviri): her kayıt beş zorunlu alanlı zarf taşır (tip, kaynak, tarih, hedef, sema); değer "-" olabilir ama alan
başlığı durur; 2026-09-20 sonrası defter kaydında köken alanı da zorunlu. Tip kümesi kapalıdır (8 değer) ve her tipin varsayılan
hedefi vardır; borç tipinde doğrulama alanı zorunludur. Triyaj sırası: eşdeğeri varsa NOOP, tamamlıyorsa güncelle, çelişiyorsa eski
kaydı geçersiz kıl (silme yok; anahtar değişiyorsa emeklilik yayılımı da gerekir), hiçbiri değilse ekle. Damıtma tetiği: kapsül
~140 satırda uyarı, 200'de zorunlu tur; kuyruktaki önem toplamı ≥150 ise tur açılır. Devir raporu ≈1.000-2.000 token tavanlı.
2 seans içinde tip/hedef alamayan kayıt sınıflandırılamadı kanalına taşınır; sessiz düşürme yok.
-/
namespace Kanon.Ingest

inductive Tip | karar | kuralAdayi | borc | bulgu | ders | kavram | ham | diger
  deriving Repr, DecidableEq

inductive Hedef | defter | g2Kuyruk | kapsulPano | raporWiki | kilavuz | wiki | gelenBronz | dlqAday
  deriving Repr, DecidableEq

/-- §2 varsayılan yönlendirme -/
def hedef : Tip → Hedef
  | .karar => .defter | .kuralAdayi => .g2Kuyruk | .borc => .kapsulPano | .bulgu => .raporWiki
  | .ders => .kilavuz | .kavram => .wiki | .ham => .gelenBronz | .diger => .dlqAday

structure Zarf where
  tip        : Option Tip
  kaynakVar  : Bool
  tarihVar   : Bool
  hedefVar   : Bool      -- değer "-" olabilir; başlık durmalı
  semaVar    : Bool
  kokenVar   : Bool := false
  dogrulama  : Bool := false
  defterKaydi : Bool := false
  tarih20Eylul20Sonrasi : Bool := false
  deriving Repr

/-- §1 zarf geçerliliği := 5 alan ∧ (borç → doğrulama) ∧ (defter ∧ 09-20 sonrası → köken) -/
def zarfGecerli (z : Zarf) : Bool :=
  z.tip.isSome && z.kaynakVar && z.tarihVar && z.hedefVar && z.semaVar &&
  (z.tip != some .borc || z.dogrulama) &&
  (!(z.defterKaydi && z.tarih20Eylul20Sonrasi) || z.kokenVar)

/-- §3 triyaj (first hit) -/
inductive Triyaj | noop | guncelle | gecersizKil | ekle
  deriving Repr, DecidableEq

def triyaj (esdeger tamamliyor celisiyor : Bool) : Triyaj :=
  if esdeger then .noop else if tamamliyor then .guncelle else if celisiyor then .gecersizKil else .ekle

/-- Geçersiz kılmada anahtar değişiyorsa emeklilik yayılımı zorunlu (restrict: kalıntı varken tamamlanmış sayılmaz). -/
def gecersizKilmaTamam (anahtarDegisti emekliSatiri kalintiVar : Bool) : Bool :=
  !anahtarDegisti || (emekliSatiri && !kalintiVar)

/-- §5 damıtma tetikleri -/
inductive Damitma | yok | uyari | zorunluTur
  deriving Repr, DecidableEq

def damitma (kapsulSatir onemToplam : Nat) : Damitma :=
  if kapsulSatir ≥ 200 || onemToplam ≥ 150 then .zorunluTur
  else if kapsulSatir ≥ 140 then .uyari
  else .yok

def devirTavanToken : Nat := 2000

/-- §6 DLQ: 2 seans içinde tip/hedef alamayan kayıt taşınır. -/
def dlqTasi (seansSayisi : Nat) (tipHedefVar : Bool) : Bool := !tipHedefVar && decide (seansSayisi ≥ 2)

theorem borc_dogrulamasiz_gecersiz (z : Zarf) (h : z.tip = some .borc) (hd : z.dogrulama = false) : zarfGecerli z = false := by
  simp [zarfGecerli, h, hd]

theorem esdeger_noop (t c : Bool) : triyaj true t c = .noop := rfl

theorem onem_tetigi (s : Nat) : damitma s 150 = .zorunluTur := by
  simp [damitma]

end Kanon.Ingest
