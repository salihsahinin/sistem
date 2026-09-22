# Quant öğrenme müfredatı — Atlas sentez raporu (2026-09-22; m.40b v0.2 diyalektik: tez 4 → antitez 4 → V26 → maskeli hakem)

`[tip: rapor | kaynak: jarvis-terminal 09-22 | tarih: 2026-09-22 | hedef: raporlar | sema: v2 | koken: jarvis/claude-fable-5-1/2026-09-22]`

**Soru (Salih 09-22):** sıfırdan quant öğrenmek isteyen matematik mühendisliği son sınıf öğrencisi için sektörde kabul gören öğrenme sırası ve konu-bağımlılık DAG'ı. **Ürün:** `vega/ogrenme/quant/mufredat-dag.md` (17 düğüm, 28 kenar) + `README.md` Q-tablosu + `vega/cc/gelen/ders-Q1.md`. Emir: `cc/gorev/2026-09/gorev-2026-09-22-quant-mufredat-atlas.md`.

## Koşum
| Aşama | Ajan | Model | Çıktı |
|---|---|---|---|
| Tez A-D | 4 atlas | Sonnet 5 | `cc/rapor/2026-09/…-tez-{A..D}.md` (11,4 · 9,8 · 10,1 · 10,9 KB) |
| İddia çıkarımı (CoVe-Factored) | 1 işçi | Sonnet 5 | `…-iddia-{A..D}.md` (20 · 18 · 17 · 20 iddia) |
| Antitez A-D | 4 atlas (Devil's Advocate) | Sonnet 5 | `…-antitez-{A..D}.md` |
| V26 sondaj | 1 işçi | Sonnet 5 | `…-v26.md`: 40 sondaj · `TUTTU` 25 · `TUTMADI` 7-8 · `ERİŞİLEMEDİ` 8; K tavanı tez-A/B/D + antitez-A |
| Hakem | `hakem` ajanı | **Opus 5.5** (eskalasyon b: tez-D `TUTMADI` 3/5 ≥ 3) | `…-hakem.md` |
Gerçekleşen: 14 ajan · ≈0,89 M alt-ajan token (tez 255k · iddia 108k · antitez 279k · V26 148k · hakem 98k) · ≈25 dk duvar saati. Emirdeki kestirim 0,8-1,2 M `[?]` → tuttu.

## Hayatta-kalma (hakem)
51 iddia: **sağlam 24 / daraldı 20 / düştü 5 · çelişkili 2**. Aile: A 7/5/2 · B 3/5/2 · C 6/3/0 · D 8/7/1. DAG 30 kenar: **D 1 / K 24 (11 daraldı) / X 5**. Yalnız 8 iddia birincil kaynakla D (Oxford yapısı ×2, ETH kredi, Stevens FE630 önkoşulu, Campbell-Lo-MacKinlay, Tsay, LLM meta-analizi, Jane Street ilanı). Erişim engeli: QuantNet 403 (tüm thread'ler), Baruch ECONNRESET, Columbia 403/şifre, Springer/OUP duvarı.

## Hayatta-kalan çekirdek (sıra kararını taşıyan bulgular)
1. **Program iskeleti:** hazırlık bloğu (2-3 hafta) → çekirdek-1 (stokastik hesap + piyasalar + istatistik + programlama) → çekirdek-2 (risk + sabit getiri + ileri stokastik) → seçmeli → tez; CMU/NYU/Oxford'da var (Oxford D), Princeton belirtmiyor, ETH-UZH sessiz (A14 K↓).
2. **Binom model stokastik hesaptan önce** (Shreve I → II; hakem ters yönü X'ledi). Ölçü teorisi **önkoşul değil, tavsiye** (UZH "exposure önerilir"; Rutgers/Baruch/Stony Brook ölçü teorisiz işliyor).
3. **Portföy/risk stokastik hesapla paralel**: Grinold-Kahn stokastik hesap istemez; NYU'da Risk & Portfolio Core L1'de stokastik hesapla aynı dönem. Fixed income → türev yönü şüpheli (CMU'da FI türevin önkoşulu).
4. **Veri hattı:** Campbell-Lo-MacKinlay'ın önkoşulu "temel istatistik" (D); Tsay şart değil. López de Prado modül sırası (ekonometri tuzakları → ML → backtest → portföy kurulumu) yazarın kendi sitesinde (kenar D).
5. **Araçlar alternatif, zincir değil:** vectorbt (açık kaynak bakım modunda) ∥ zipline-reloaded ∥ QuantConnect; backtrader yavaşlamış, durmamış (PR 2026-03). Veri: yfinance prototip (ToS riski) → WRDS/CRSP (Morningstar satın aldı 2026-02, K) → Polygon/massive (ücretsiz Basic + $29/ay Starter var; "pahalı" yalnız üst katman).
6. **Kariyer:** rol ayrımı researcher/trader/dev bulanık; Python asgari; mülakat üçlüsü Green Book + Heard on the Street + Joshi, 150 MFAQ **3. baskı (2024)**; Jane Street NY taban $300k (D); Türkiye'de tek somut ilan (Algocor), ikinci örnek teyitsiz.

## Düşen / daralan (müfredata girmeyen ya da şerhli)
- **Düştü:** "Shreve omurga" iddiasının gösterilen kaynağı Shreve'i anmıyor (kitap sırası yine Shreve I→II ile kuruldu, dayanak Joshi/Stevens K) · CMU prep 4 hafta (3) · Oxford tez %30/25-40 sayfa · Jorion→Meucci sırası (model hafızası) · CRSP CIZ 2026 (aslında 2022).
- **Daraldı:** Björk içindekiler · QuantStart listesi 2013 tarihli (Hull 8e) · Grinold-Kahn 3 kısım (4) · Baruch/Columbia yapıları (erişilemedi) · ETH-UZH "hazırlık yok" (sessiz) · mikroyapı "resmî sırası" yok.
- **Çelişkili:** Björk↔Shreve kıyası kaynaklı mı (QuantNet 403) · LLM hız çarpanı (satıcı 2-4×) ↔ meta-analiz g=0,33 (birim farklı).

## Öneriler (Salih hükmü; sonucu değiştirmeyen alt-kararlar Vega'da)
- **Ö1 (öneri): DAG v1 aynen** (`mufredat-dag.md`), 17 düğüm; ilk ders Q1 ∥ Q2 (Temel blok = hazırlık bloğu karşılığı). Artı: hakem X kenarları dışarıda, paralel dallar açık; PortRisk (K-002) Q5/Q17'ye bağlanır. Eksi: Q9/Q14 kenarları K↓, 3 ders sonra Vega `ilerleme.md` sapma notuyla revize.
- **Ö2:** ölçü teorisi düğümünü zorunlu yap (ETH/NYU titiz yolu). Artı: MFE başvurusu düşünülüyorsa avantaj. Eksi: 4-6 hafta gecikme, hakem "tavsiye" dedi.
- **Ö3:** veri hattını (Q11-Q13) çekirdek-1'e çek (ML-önce). Artı: PortRisk'e hızlı ürün. Eksi: türev fiyatlama gecikir, program iskeletine aykırı.
- **Açık borç:** QuantNet/Baruch/Columbia birincil erişimi (tarayıcıyla Salih eli) · Türkiye ilan taraması (Kariyer.net/LinkedIn 403) · Sonnet-hakem ölçüm borcu bu koşumda sayılmadı (Opus eskalasyonu).
