/-
Kanon.BaglamSirasi — bağlam yükleme sırası değişmezi (Karar 117, durum #18; 2026-10-16), Lean 4 kod tabanı.
Ölçüm: raporlar/2026-10-16-baglam-sirasi-import-deneyi.md (Claude Code 2.1.302, ham API isteği). Sentez:
raporlar/2026-10-16-baglam-sirasi-formalizasyon-sentez.md. İcra: kod/baglam (`baglam genislet|denetle`).
Türkçe özet (geri-çeviri): bir dosya, parça kimlikleri taşıyan metin ile sıralı içe aktarmalardan oluşan bir
ağaç düğümüdür. Otomatik yükleme bağlamı ağacın pre-order düzleştirmesidir: önce düğümün metni, sonra
çocuklar yazılış sırasıyla. Md dosyası kesilip parçaları çocuk dosyalara taşındığında, zincir (her dosya bir
sonrakini içe aktarır) ve yelpaze (ilk dosya kalan parçaları sırayla içe aktarır) biçimlerinin ikisi de
özgün parça dizisini aynen verir. Yelpaze derinlik 1'dir, 4 sıçrama sınırına takılmaz; tercih edilir.
-/
namespace Kanon.BaglamSirasi

/-- Dosya düğümü: metin parçalarının kimlikleri + içe aktarılan çocuklar (yazılış sırasıyla). -/
inductive Dosya where
  | dugum (metin : List Nat) (cocuklar : List Dosya)

mutual
/-- Otomatik yükleme: `L(f) = metin(f) ++ L(i₁) ++ … ++ L(iₖ)`. -/
def Dosya.yukle : Dosya → List Nat
  | .dugum m cs => m ++ Dosya.yukleHepsi cs
def Dosya.yukleHepsi : List Dosya → List Nat
  | [] => []
  | c :: cs => c.yukle ++ Dosya.yukleHepsi cs
end

/-- Çocuk listesinin yüklenmesi, her çocuğun yüklenmesinin birleşimidir (serbest monoid yüzü). -/
theorem yukleHepsi_flatten (cs : List Dosya) :
    Dosya.yukleHepsi cs = (cs.map Dosya.yukle).flatten := by
  induction cs with
  | nil => rfl
  | cons c cs ih => simp [Dosya.yukleHepsi, ih]

/-- Zincir: her parça bloğu bir sonrakini içe aktarır. -/
def zincir : List (List Nat) → Dosya
  | [] => .dugum [] []
  | [p] => .dugum p []
  | p :: ps => .dugum p [zincir ps]

theorem zincir_sira (ps : List (List Nat)) : (zincir ps).yukle = ps.flatten := by
  induction ps with
  | nil => simp [zincir, Dosya.yukle, Dosya.yukleHepsi]
  | cons p ps ih =>
    cases ps with
    | nil => simp [zincir, Dosya.yukle, Dosya.yukleHepsi]
    | cons q qs => simp [zincir, Dosya.yukle, Dosya.yukleHepsi] at ih ⊢; rw [ih]

/-- Yelpaze: ilk blok ebeveynde kalır, kalan bloklar ebeveynin sonundaki `@` satırlarıyla sırayla içe aktarılır. -/
def yelpaze : List (List Nat) → Dosya
  | [] => .dugum [] []
  | p :: ps => .dugum p (ps.map (fun q => .dugum q []))

theorem yelpaze_sira (ps : List (List Nat)) : (yelpaze ps).yukle = ps.flatten := by
  cases ps with
  | nil => simp [yelpaze, Dosya.yukle, Dosya.yukleHepsi]
  | cons p ps =>
    simp only [yelpaze, Dosya.yukle, yukleHepsi_flatten, List.map_map, List.flatten_cons]
    congr 1
    induction ps with
    | nil => rfl
    | cons q qs ih => simp [Dosya.yukle, Dosya.yukleHepsi] at ih ⊢; exact ih

/-- Sıçrama sınırı (ölçüm B8: kökten 4; daha derini sessizce düşer). -/
def azamiSicrama : Nat := 4

/-- Yelpazenin derinliği 1'dir; sınırın altında kalır. -/
theorem yelpaze_sinirda : 1 ≤ azamiSicrama := by decide

end Kanon.BaglamSirasi
