/-
Kanon.AjanYetki — ajan-yetki kanunu (tüzük m.42 (a)-(h); Salih 2026-07-19, Karar 92 M6 2026-09-10),
Lean 4 kod tabanı. Karar 117, 2026-10-17. Model kademesi için bkz. Kanon.Delegasyon.Model (kopyalanmadı).
Türkçe özet (geri-çeviri): ajan yalnız pozitif yetki listesindekini yapar. Özgürlük ≤ hatanın toparlanabilirliği. Gevşetme ⟸ sicil ∧ geri-alınabilir hata sınıfı ∧
token-zaman baskısı; ölçek tek başına gerekçe olmaz. Yeni ajan katı sınırla doğar. Risk = hata olasılığı × hata maliyeti × geri-alma maliyeti.
Çeşitlilik bütçesi de özgürlüktür ve katı başlar. Emirde amaç ile done-yüklemi çelişirse amaçtaki her çıktı DONE'a sayılır, fark koşum başında [sapma] olur;
ajanın kendi hafıza dosyaları örtük yazma izinlidir; araç-çağrı tavanında emir şablonu yener.
-/
namespace Kanon.AjanYetki

/-- (a) Pozitif yetki: eylem yetki listesinde değilse yasak. -/
def izinli (yetkiListesinde kirmiziCizgi : Bool) : Bool := yetkiListesinde && !kirmiziCizgi

/-- (b) Özgürlük sınırı: özgürlük ≤ toparlanabilirlik. Seviyeler Nat. -/
def ozgurlukSinirinda (ozgurluk toparlanabilirlik : Nat) : Bool := decide (ozgurluk ≤ toparlanabilirlik)

/-- (c) Gevşetme koşulu. Ölçek koşulda yoktur: tek başına gerekçe değildir. -/
def gevsetilebilir (sicil geriAlinabilirHata baski : Bool) : Bool := sicil && geriAlinabilirHata && baski

/-- (d) Başlangıç: her yeni ajan/katman katı doğar. -/
inductive Sinir | kati | gevsek
  deriving Repr, DecidableEq

def baslangicSiniri : Sinir := .kati

/-- (e) Risk boyutu (m.37 4. boyut). -/
def risk (hataOlasiligi hataMaliyeti geriAlmaMaliyeti : Nat) : Nat := hataOlasiligi * hataMaliyeti * geriAlmaMaliyeti

/-- (f) Çeşitlilik-bütçesi: alternatif sayısı yetki sınırını (k) aşmaz; sınır katman ve toparlanabilirlikten gelir. -/
def cesitlilikBicesinde (alternatif sinirK : Nat) : Bool := decide (alternatif ≤ sinirK)

/-- (h) Emir iç-çelişkisi: amaç ↔ done-yüklemi çelişirse amaç kazanır; [sapma] koşum BAŞINDA beyan edilir. -/
inductive SapmaBeyani | yok | kosumBasinda
  deriving Repr, DecidableEq

def sapmaBeyani (amacDoneCelisir : Bool) : SapmaBeyani :=
  if amacDoneCelisir then .kosumBasinda else .yok

/-- Ajanın kendi hafıza dosyası türleri: yazma_izni listesinde olmasa da örtük izinli. -/
inductive Dosya | kapsul | pano | defter | kutu | geriDonusNotu | diger
  deriving Repr, DecidableEq

def yazmaIzinli (listede : Bool) : Dosya → Bool
  | .diger => listede
  | _ => true

/-- Araç-çağrı tavanı: emirdeki değer varsa o, yoksa şablon değeri (çakışmada emir kazanır). -/
def aracCagriTavani (emir : Option Nat) (sablon : Nat) : Nat := emir.getD sablon

theorem olcek_tek_basina_gevsetmez : gevsetilebilir false false true = false := rfl

theorem yeni_ajan_kati : baslangicSiniri = .kati := rfl

theorem emir_tavani_kazanir (e s : Nat) : aracCagriTavani (some e) s = e := rfl

theorem hafiza_ortuk_izinli (d : Dosya) (h : d ≠ .diger) : yazmaIzinli false d = true := by
  cases d <;> simp_all [yazmaIzinli]

end Kanon.AjanYetki
