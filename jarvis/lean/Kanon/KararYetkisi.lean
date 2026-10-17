/-
Kanon.KararYetkisi — karar-yetkisi çerçevesi, ölçek eşiği ve 3-kartlı devir seti (tüzük m.31; S8 imzası, Salih 2026-07-11),
Lean 4 kod tabanı. Karar 117 parti 4, 2026-10-17. Uygulayan kod: yok (karar dalı ölçütü; Salih beyanı izinleri için Kanon.Commit).
Türkçe özet (geri-çeviri): karar iki katmanlıdır. Katman-1 sınıfları (kanon/kural, silme-birleştirme, geri-alınması zor iş,
dışarı çıkacak iş, para/portföy, rol/yetki, değer tercihi) yalnız Salih'indir; geri kalanı Katman-2: Jarvis yapar, kaydeder,
commit'ler; Salih vetosu revert'tir. Onaylı iş içindeki alt-karara soru yoktur; ancak ölçek eşiği (publish, para, kişisel veri,
pahalı geri-alma, yön değişimi) aşılırsa sorulur. Devir seti 3 karttır: K1 varsayılan (Jarvis önerisi, N=5 deneysel),
K2 token baskın, K3 zaman baskın; başlangıç her zaman K1, kart gidişata göre değişebilir.
-/
namespace Kanon.KararYetkisi

/-- Karar sınıfı: ilk yedisi Katman-1, `diger` Katman-2. -/
inductive Sinif
  | kanonKural | silmeBirlestirme | geriAlinmasiZor | disariCikacak
  | paraPortfoy | rolYetki | degerTercihi | diger
  deriving Repr, DecidableEq

inductive Katman | bir | iki
  deriving Repr, DecidableEq

def katman : Sinif → Katman
  | .diger => .iki
  | _      => .bir

inductive Karar
  | yalnizSalih          -- Katman-1
  | jarvisYapKaydetCommit -- Katman-2
  deriving Repr, DecidableEq

def karar (s : Sinif) : Karar :=
  match katman s with
  | .bir  => .yalnizSalih
  | .iki  => .jarvisYapKaydetCommit

/-- Katman-2 sonucuna Salih vetosu: revert; veto yoksa kalır. -/
inductive Sonuc | kalir | revert
  deriving Repr, DecidableEq

def veto (salihVetoEtti : Bool) : Sonuc := if salihVetoEtti then .revert else .kalir

/-- Ölçek eşiği sınıfları. -/
inductive Esik | publish | para | kisiselVeri | pahaliGeriAlma | yonDegisimi
  deriving Repr, DecidableEq

/-- Soru gerekir mi: onaylı iş içindeki alt-karar sessiz; yalnız eşik aşılırsa sorulur. -/
def soruGerekir (esik : Option Esik) : Bool := esik.isSome

/-- Devir kartı (deneysel). K1 Jarvis önerisi (Kart A, N=5), K2 token baskın, K3 zaman baskın. -/
inductive Kart | k1 | k2 | k3
  deriving Repr, DecidableEq

/-- Başlangıç her zaman K1. -/
def baslangicKart : Kart := .k1

/-- Kart yalnız gidişat/büyüklük/token gerekçesiyle değişir; gerekçe yoksa mevcut kalır. -/
def kartSec (mevcut : Kart) (degisimGerekcesi : Option Kart) : Kart :=
  degisimGerekcesi.getD mevcut

/-- Kart K1'deki varsayılan N (deneysel damga; dış-chat matematik çalışması sonrası revize edilebilir). -/
def kartANdeneysel : Nat := 5

end Kanon.KararYetkisi
