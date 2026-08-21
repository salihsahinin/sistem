# Masa-kararı adayı (2026-08-01): koşum-tavanı yeniden-tasarımı + REJİM-ETİKETİ ilkesi

*Kaynak: Salih ↔ Carvis CC yan-oturum, 08-01 (graf-hattı sonrası maliyet hasadı). Statü: karar ADAYI — tavan/kural değişikliği masa/Salih imzası ister; bu dosya karar-malzemesidir. Kaydeden: Carvis CC.*

## Veri (13 koşumun kapanış beyanlarından hasat)

- Gerçekleşen maliyetler heterojen aygıtlardan: dedup'lı temiz ölçümler **$7,78 · $9,80 · $10,53** ↔ betik/aday rakamlar **$17,07 · $18,75 · $29,15 · ≈$120** (aygıt şerhi: `kosum-maliyeti.py` dedup'suz ≈2,6-3,3× şişik ölçebiliyor — masa EK-2① açık; web-arama sayılmıyor).
- **Tavan ($14) 4 kez İHLAL edildi** (rapor-8: 2,08× · rapor-10: 1,34× · rapor-13: 1,22× · rapor-18: ≈8×) ∧ **3 koşumda kaliteyi kırptı** (8/10/13: antitez/hakemlik düşürüldü — rapor-10 K1: m.40b tam-kontrat ≈ $30+, $14 ile sığmıyor).
- Mekanik kök-nedenler (raporların kendi ölçümleri): prompt-freni taahhüt-edilmiş-ama-bitmemiş işi göremiyor (13) · pasif fren koşan ajanı durdurmuyor (18, KL18-12) · maliyet ajan-sayısıyla değil **ajan-turu × bağlam** ile ölçekleniyor (18, KL18-2: "9-ajanlı derin koşum ≈ $100 sınıfı; $14'lük emir 1-2 ajan kaldırır") · rapor-15 hükmü: *"limit tasarruf aracı değil, kusurlu koşucuyu toparlama aracıdır."*

## Öneri A — sınıf-bazlı anomali-freni (V47 formu; sabit sayı değil kural)

tavan(sınıf) = ölçülen-medyan(sınıf) × ~3 [anomali eşiği] · sınıflar: sonnet-hafif ↔ m.40b-tam-kontrat ↔ çok-dalga-derin (sonuncusu yalnız ayrı imzayla açılır). ÖN-KOŞUL: dedup düzeltmesi + sınıf-medyan ölçümü (ölçüm-bankı bekleyen kalemi). Gerekçe: abonelik rejiminde $ bütçe-kısıtı değil; tavanın işlevi kaçak-tespiti.

## Öneri B — mekanik düzeltmeler (deterministik çağrı-kapısı borcuna girdi; artık 4 ölçülü vaka)

fan-out ÖNCESİ kestirim kapısı (taahhüt-anı, ölçüm-anı değil) ∧ aşımda AKTİF durdurma (TaskStop sınıfı) ∧ tek-dalga kuralı (ajan-başına ikinci iç-dalga yasağı) ∧ ivme-limiti (rapor-15 §8: ani-sıçrama koruması).

## Öneri C — REJİM-ETİKETİ ilkesi (Salih beyanı, 08-01 — genel karar-ilkesi adayı)

**Beyan:** "Şu anki hızımda limitim dolmuyor ama tam otomasyona geçince işler değişecek — bu tarz konularda uzun süreli karar alırken dikkat etmeliyiz."
**İlke (lojik formda):** kalibrasyon-kararı(k) ∧ rejim-bağımlı(k) → k REJİM-ETİKETİ taşır: `[rejim: manuel-tempo, kota-bol]` ∧ (rejim-geçişi[K-009/K-010 otomasyon] → k OTOMATİK yeniden-açılır, taşınmaz).
Kapsam adayları: koşum-tavanları · ε/agresiflik kadranları · damıtma tetikleri · schedule'lar. Kanon bağı: A2 kapısı ("sert-bütçe yazılı" = otomasyonun ön-koşulu — ilke bunu genelleştirir) · m.29 deneysel-damga (rejim-etiketi onun zaman-boyutlu kardeşi) · gorev-14 H26 (bayatlama) · gorev-17 H37 (rejim-geçişi = ağırlık-güncelleme fazı tetiği).

## Bağlar

`cc/rapor-2026-08-01-10.md` K1 (tavan↔m.40b çelişkisi, seçenek a-d) · `-13.md` (ölçüm-gecikmesi vakası) · `-15.md` §8 (referans mimari: kota+debi+burst+ivme+hiyerarşi) · `-18.md` KL18-2/KL18-12 · `kuyruk/olcum-banki.md` bekleyen kalemler · masa icra borcu: deterministik çağrı-kapısı TASARIMI.

---
*İNGEST EDİLDİ · 2026-08-21 damıtma turu (triyaj: NOOP — içerik karar-borcu kütüğünde izleniyor: ai2ai+ölçek-yasaları → KB-36 kutu-adayları [masada] · tavan-rejim → KB-27 Karar 39 · staj-hasadı → KB-10 H4/H6 kararı; bu dosya bronz kaynak olarak yerinde kalır, m.8).*
