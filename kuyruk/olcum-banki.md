# Ölçüm Bankı (deneysel m.29; açılış: Salih imzası 2026-08-01, 08-01-5 ingest K3 kararı)

*Şirketin kalıcı sayısal ölçümleri. Şema: ölçüm · değer ± hata · %95 GA · n · yöntem-notu · kaynak · tarih · damga. Kural: buraya yalnız GA'lı/örneklemli ölçüm girer; kestirim ve kaba sınıf girmez (m.39). Bir ölçüm çürürse silinmez, üstü çizilir + çürüten kaynak yazılır (m.8).*

| # | Ölçüm | Değer | %95 GA | n | Not | Kaynak | Tarih | Damga |
|---|---|---|---|---|---|---|---|---|
| Ö-1 | Debi üssü γ (öz-pay bileşeni, γ_öz) | 0,7569 ± 0,0588 | [0,6366; 0,8771] | 31 | yalnız üretici açık beyanı; γ=1 reddedildi (t=−4,13); küme-duyarlılık 0,739–0,822, LOO yayılımı 0,084; "doğa kısıtı değil, yayınlanmış tasarım konvansiyonlarının özeti" şerhi | `cc/rapor-2026-08-01-5.md` §3 | 2026-08-01 | [D-ölçüm] |
| Ö-2 | Uç-birim genişliği ölçek üssü | +0,0957 ± 0,018 | [0,060; 0,132] | 76 (26 aile, 3,95 mertebe) | sıfırı içermiyor → "genişlik sabittir" hükmü geçersiz; iki komşu aile çıkarılınca da pozitif (+0,084 ± 0,015, n=56); MLA sınıfı (2 sistem) fit dışı | `cc/rapor-2026-08-01-5.md` §2 | 2026-08-01 | [D-ölçüm] |

**Uyarı satırları (nitel güvenilirlik ilkesi — m.39-dışı, "ölçüm" değil; Katman-2 eklendi 08-01 gece, veto açık):**
- U-1 · "Alt-ajan aktarımında **sayı-sadakati ≫ mekanizma-sadakati**" — künye/rakam çoğunlukla doğru taşınır, "neden böyle" katmanı ajan tarafından yeniden-üretilir. 3 bağımsız örnek: rapor-11/12 V26 serisi · rapor-20 §11 (12 denetimde 2 TUTMADI, ikisi de mekanizma-atfı) · ingest koşumu 08-01 (F2: 1 icat-rakam + 1 dosya-atıf hatası, ikisi de şema-dışı serbest-okuma lenslerinde). Kaynak: `raporlar/2026-08-01-ingest-grafhatti.md` §5.4/§6.

**Bekleyen ölçümler:** θ (kullanım ufku üssü) — K4 kararı: Seçenek B sıraya alındı (görev emri derlenecek) · γ_taşınan (debi ikinci bileşeni) — ölçülmedi, aday · **araştırma-koşumu süresi** (m.40b sınıfı; başlangıç/bitiş damgalı, n≥10 — Salih gözlemi ~26 dk/koşum, GA'sız olduğu için tabloya girmedi; 08-01 hattı 8-19 aday örneklem) · **koşum-maliyeti sınıf-medyanları** (sonnet-hafif / m.40b-tam-kontrat / çok-dalga ayrımıyla; ÖN-KOŞUL: dedup betiği EK-2① düzeltmesi — mevcut rakamlar heterojen aygıtlardan, karışık örneklem GA'sı anlamsız; ham adaylar: dedup'lı $9,80 · $7,78 · $10,53 ↔ betik/aday $29,15 · $18,75 · $17,07 · ≈$120; kaynak `cc/rapor-2026-08-01-{8..18}.md` kapanış blokları).
