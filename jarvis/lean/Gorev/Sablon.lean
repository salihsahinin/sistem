/-
Gorev.Sablon — görev emri sözleşmesinin Lean kalıbı (Karar 114, 2026-10-16; `gorev-emri-derleme` adım 2b, `lojik-ceviri` v2).
Türkçe özet (geri-çeviri bloğu; emir md'sine kopyalanır): örnek görev "Rust taşıma partisi". Girdi: fark testi durum sayısı,
eşleşen durum sayısı, Python dosyasına dokunuldu mu, izinsiz yola yazıldı mı. Karar: izinsiz yazım varsa dur ve Salih'e sor;
yoksa tüm durumlar eşleşiyorsa teslim; eşleşmeyen varsa onar. Done: en az bir durum koştu ∧ hepsi eşleşti ∧ Python değişmedi ∧
izinsiz yazım yok. Yeni emirde bu dosya kopyalanır, alanlar görevin kendi diliyle yeniden adlandırılır.
-/
namespace Gorev.Sablon

/-- Atomik önermeler: her alan tek ölçüm. -/
structure Girdi where
  durumSayisi     : Nat  := 0      -- fark testinde koşan durum sayısı
  eslesen         : Nat  := 0      -- Python ile birebir aynı çıkan durum sayısı
  pythonDegisti   : Bool := false  -- jarvis/tools/*.py dosyalarından biri değişti mi (git diff)
  izinsizYazim    : Bool := false  -- izin listesi dışında bir yola yazıldı mı
  deriving Repr

inductive Dal
  | katman1Dur   -- DUR + Salih'e sor
  | onar         -- eşleşmeyen durum var: düzelt, yeniden koş
  | teslim
  deriving Repr, DecidableEq

/-- Tümü eşleşti := durumSayisi > 0 ∧ eslesen = durumSayisi -/
def tumuEslesti (g : Girdi) : Bool := decide (g.durumSayisi > 0) && decide (g.eslesen = g.durumSayisi)

/-- First hit-policy: izinsiz yazım → katman1Dur; aksi ∧ ¬tümüEşleşti → onar; aksi → teslim. -/
def karar (g : Girdi) : Dal :=
  if g.izinsizYazim then .katman1Dur
  else if !tumuEslesti g then .onar
  else .teslim

/-- done := tümüEşleşti ∧ ¬pythonDeğişti ∧ ¬izinsizYazım -/
def done (g : Girdi) : Bool := tumuEslesti g && !g.pythonDegisti && !g.izinsizYazim

/-- "izinsiz yazım varsa her durumda dur" -/
theorem izinsiz_dur (g : Girdi) (h : g.izinsizYazim = true) : karar g = .katman1Dur := by
  simp [karar, h]

/-- "done ise karar teslimdir" (done → teslim; tersi değil: teslim kararı Python değişikliğini görmez) -/
theorem done_teslim (g : Girdi) (h : done g = true) : karar g = .teslim := by
  simp [done] at h
  simp [karar, h]

/-- "hiç durum koşmadıysa done olamaz" -/
theorem bos_done_degil (g : Girdi) (h : g.durumSayisi = 0) : done g = false := by
  simp [done, tumuEslesti, h]

end Gorev.Sablon
