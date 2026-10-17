/-
Kanon.AjanMetodoloji — görev-fonksiyonu sözleşmesi, icra formatı, eskalasyon ve koşum hijyeni (core/ajan-metodolojisi.md §1, §6, §6b, "Koşum hijyeni ekleri";
Karar 83 C3, Karar 77, Karar 89, 92 M6, 103 M2, 104 M4, 105, 106), Lean 4 kod tabanı. Karar 117, 2026-10-17.
Çakışanlar kopyalanmadı: model kademesi, işçi ≤ lider tavanı, delegasyon varsayılan kapalı, efor cetveli → Kanon.Delegasyon; rol→model eşlemesi ve lider effort'u
(medium sabit, high yasak) → Kanon.AjanKaliciligi; orkestrasyon dalı → Kanon.RolKatman. Burada yalnız bu üçünde olmayan hükümler vardır.
Türkçe özet (geri-çeviri): §1 görev-emri alanları tiplidir ve "özetle" denmez; sözleşme üçlüsü (ön-koşul, değişmez, boolean done-yüklemi) ile yeniden-deneme tavanı (varsayılan 3) zorunludur;
dal+koşul toplamı ≤5, aşılırsa fonksiyon bölünür; Katman-1 sınıfı karar gerektiren dal DUR ve Salih'e sorar; done teslimde koşul koşul işaretlenir.
§6 işçi case'i kimlik, yazma izni, git yasağı, çağrı bütçesi (10-15), adım adım case, doğrulama komutu, çıktı şeması ve "açık soru" satırını taşır; işçinin karar yetkisi sıfırdır;
işçi çağrıları senkrondur, dönüş diske düşmeden sonraki adım yok; fren N_hücre + sayaç ≤ 143, planlama tavanı 116; aile ≤ 3 eşzamanlı; loop yalnız sürekli-korunan değişmez işinde;
iç içe yalnız kendi sayacı ∧ durma yüklemi olan seviyede; ikinci Fable yan-oturumu yalnız Salih beyanıyla. §6b eskalasyon tetikleri: Salih beyanı ∨ hakem TUTMADI ≥ 3 ∨ işçi 2 başarısız tur;
hedef Opus; her eskalasyon kaydedilir (sessiz yasak); aşağı-eskalasyonla kalite düşürme yasak; üçüncü tur yoksa görev bölünür. Emir iç-tutarlılık kapısı: amaçtaki her çıktı DONE'da sayılır, tavan emirden gelir, fark başta [sapma].
Koşum hijyeni: ≥ 15 satırlık python işi heredoc'a değil, scratchpad'de .py dosyasına yazılır.
-/
import Kanon.Delegasyon
namespace Kanon.AjanMetodoloji
open Kanon.Delegasyon

/-! ## §1 Görev = fonksiyon -/

/-- §1: emir alanı `ad: tip` yazılır; işçiye "özetle" denmez, tipli alan doldurtulur. -/
def alanGecerli (tipli ozetleDenmis : Bool) : Bool := tipli && !ozetleDenmis

/-- §1: sözleşme üçlüsü + yeniden-deneme tavanı; done-yüklemi boolean (derece ifadesi yasak). -/
structure GorevFonksiyonu where
  onKosul        : Bool
  degismez       : Bool
  doneBoolean    : Bool   -- done-yüklemi boolean değerlendirilebilir
  derece         : Bool := false  -- "iyi bir rapor" gibi derece ifadesi
  yenidenDeneme  : Nat := 3
  deriving Repr

def sozlesmeUclusuTam (g : GorevFonksiyonu) : Bool := g.onKosul && g.degismez && g.doneBoolean && !g.derece

/-- §1 dal-bütçesi: dal + koşul toplamı ≤ 5 (deneysel); aşılırsa fonksiyon bölünür. -/
def dalButcesi : Nat := 5

inductive Bolme | tek | bol
  deriving Repr, DecidableEq

def bolme (dal kosul : Nat) : Bolme := if dal + kosul ≤ dalButcesi then .tek else .bol

/-- §1: Katman-1 sınıfı karar gerektiren dal = DUR + Salih'e sor. -/
inductive DalSonuc | yurut | durSalihSor
  deriving Repr, DecidableEq

def dalSonuc (katman1Karar : Bool) : DalSonuc := if katman1Karar then .durSalihSor else .yurut

/-- §1 DRFR: teslim tek dereceyle değil koşul koşul işaretlenir; hepsi karşılandıysa done. -/
def teslimDone (kosullar : List Bool) : Bool := kosullar.all id

/-! ## §6 İcra formatı -/

/-- §6: işçi case'i; eksik alanla dağıtılmaz. -/
structure IsciCase where
  kimlik        : Bool
  yazmaIzni     : Bool   -- dosya listesi
  gitYasagi     : Bool
  cagriButcesi  : Nat    -- 10-15
  adimAdim      : Bool
  dogrulamaKomutu : Bool
  ciktiSemasi   : Bool
  acikSoruSatiri : Bool
  deriving Repr

def cagriButcesiAralikta (n : Nat) : Bool := decide (10 ≤ n ∧ n ≤ 15)

def caseTam (c : IsciCase) : Bool :=
  c.kimlik && c.yazmaIzni && c.gitYasagi && cagriButcesiAralikta c.cagriButcesi && c.adimAdim &&
  c.dogrulamaKomutu && c.ciktiSemasi && c.acikSoruSatiri

/-- §6: işçinin karar yetkisi sıfırdır. -/
def isciKararYetkisi : Nat := 0

/-- §6: işçi çağrıları senkron; işçi dönüşü diske düşmeden sonraki adım başlamaz. -/
def sonrakiAdimBaslayabilir (isciDonusuDiskte : Bool) : Bool := isciDonusuDiskte

/-- §6: fren tavanları; N_hücre + sayaç_oturum ≤ 143, planlama tavanı 116, aile ≤ 3 eşzamanlı. -/
def frenTavan : Nat := 143
def planlamaTavan : Nat := 116
def aileEszamanli : Nat := 3

def frenIcinde (nHucre sayacOturum : Nat) : Bool := decide (nHucre + sayacOturum ≤ frenTavan)
def planlamaIcinde (nHucre sayacOturum : Nat) : Bool := decide (nHucre + sayacOturum ≤ planlamaTavan)
def aileIcinde (eszamanli : Nat) : Bool := decide (eszamanli ≤ aileEszamanli)

/-- §6: loop yalnız "sürekli-korunan değişmez" sınıfı işte. -/
def loopUygun (surekliKorunanDegismez : Bool) : Bool := surekliKorunanDegismez

/-- §6: iç içe seviye yalnız kendi sayacı ∧ kendi durma yüklemi varsa. -/
def nestedUygun (kendiSayaci kendiDurmaYuklemi : Bool) : Bool := kendiSayaci && kendiDurmaYuklemi

/-- §6: ikinci Fable yan-oturumu yalnız Salih beyanıyla. -/
def ikinciFableYanOturum (salihBeyani : Bool) : Bool := salihBeyani

/-! ## §6b Eskalasyon -/

/-- Eskalasyon tetikleri (a) Salih beyanı (b) hakem TUTMADI ≥ 3 (c) işçi aynı görevde 2 başarısız tur. -/
structure EskTetik where
  salihBeyani   : Bool := false
  hakemTutmadi  : Nat  := 0
  basarisizTur  : Nat  := 0
  deriving Repr

def eskalasyonTetikli (t : EskTetik) : Bool :=
  t.salihBeyani || decide (t.hakemTutmadi ≥ 3) || decide (t.basarisizTur ≥ 2)

/-- Hedef: Opus (Karar 106); kaynak daha ucuz, hedef Opus'u aşmaz, kayıt zorunlu (sessiz eskalasyon yasak). -/
def eskalasyonGecerli (kaynak hedef : Model) (kayitli : Bool) : Bool :=
  decide (kademe kaynak < kademe hedef) && decide (kademe hedef ≤ kademe .opus) && kayitli

/-- (c) iki başarısız tur sonrası üçüncü tur yoksa görev bölünür (m.21). -/
def ucuncuTurSonrasi (ucuncuTurVar : Bool) : Bolme := if ucuncuTurVar then .tek else .bol

/-- Aşağı-eskalasyon adıyla kalite düşürme yasak: Fable işi Sonnet'e devredilmez. -/
def fableIsiDevirIzinli (hedef : Model) : Bool := decide (hedef = .fable)

def fableIsiAsagiDevir : Bool := fableIsiDevirIzinli .sonnet

/-- Varsayılan model Sonnet; Friday Opus kalıcı (Karar 104 M4 + 106). -/
inductive Rol | alanAjani | alanHakem | ortakHakem | isci | friday
  deriving Repr, DecidableEq

def varsayilanModel : Rol → Model
  | .friday => .opus
  | _ => .sonnet

/-- Emir iç-tutarlılık kapısı (Karar 92 M6 → m.42(h)): amaçtaki her çıktı DONE'da sayılmalı; tutarsızlık → koşum başında [sapma]. -/
def emirTutarli (ciktilar doneSayilan : List String) : Bool := ciktilar.all (fun c => doneSayilan.contains c)

/-! ## Koşum hijyeni -/

/-- Heredoc-python hijyeni (Karar 77): ≥ 15 satırlık python işi scratchpad'de .py dosyasına yazılır. -/
def heredocPythonUygun (satir : Nat) (dosyadan : Bool) : Bool := decide (satir < 15) || dosyadan

theorem sozlesme_derece_yasak (g : GorevFonksiyonu) (h : g.derece = true) : sozlesmeUclusuTam g = false := by
  simp [sozlesmeUclusuTam, h]
theorem alti_dal_bolunur : bolme 4 2 = .bol := by decide
theorem bes_dal_tek : bolme 3 2 = .tek := by decide
theorem katman1_dali_durur : dalSonuc true = .durSalihSor := rfl
theorem eksik_case_dagitilmaz (c : IsciCase) (h : c.gitYasagi = false) : caseTam c = false := by
  simp [caseTam, h]
theorem diske_dusmeden_adim_yok : sonrakiAdimBaslayabilir false = false := rfl
theorem sessiz_eskalasyon_yok (k h : Model) : eskalasyonGecerli k h false = false := by
  simp [eskalasyonGecerli]
theorem isci_fableye_eskale_olmaz : eskalasyonGecerli .sonnet .fable true = false := by decide
theorem sonnet_opusa_eskale : eskalasyonGecerli .sonnet .opus true = true := by decide
theorem iki_tur_tetikler : eskalasyonTetikli { basarisizTur := 2 } = true := by decide
theorem fable_isi_sonnete_gitmez : fableIsiAsagiDevir = false := by decide
theorem uzun_python_dosyaya : heredocPythonUygun 15 false = false := by decide

end Kanon.AjanMetodoloji
