# Ders iskeleti Q1 — Financial Markets & Instruments (Jarvis → Vega, 2026-09-22; Karar 105 M4 devir birimi)

`[tip: ders-iskelet | kaynak: jarvis-terminal 09-22 | tarih: 2026-09-22 | hedef: vega/ogrenme/quant | sema: ogren v0.3 | koken: jarvis/claude-fable-5-1/2026-09-22]`

Şerit `ogrenme/quant` · düğüm **Q1** (DAG `mufredat-dag.md`); Q2 paralel açılabilir (Salih tercihi). Bu dosya `PROBE` + `PLAN` + kutu başlıklarını taşır; `TEACH`/`CLOSE` Vega'nın. Sektör başlıkları AS-OF 2026-09-22, ders başında teyit.

## PROBE — iplikler (≤5) ve sorular (≤12; doğru şık konumu rastgele; (e) bilmiyorum sabit)
İlk ders olduğundan `PROBE` girdi düğümlerini (G1-G4) de ölçer: İplik 1 **olasılık/beklenti** · 2 **lineer cebir** · 3 **Python/pandas** · 4 **finansal enstrüman temeli** · 5 **no-arbitrage sezgisi**.

1. (İplik 1) X ∈ {−1, +2} eşit olasılıkla; E[X] ve Var[X]? (a) 0,5 · 2,25 · (b) 0,5 · 1,5 · (c) 1 · 2,25 · (d) 0,5 · 4,5 · (e) bilmiyorum. **Doğru: a** (E=0,5; E[X²]=2,5; Var=2,25).
2. (İplik 1, üst) Bağımsız iki getirinin toplamının varyansı? (a) varyansların çarpımı · (b) varyansların toplamı · (c) standart sapmaların toplamı · (d) ortalaması · (e) bilmiyorum. **Doğru: b.**
3. (İplik 2) Kovaryans matrisi Σ için portföy varyansı wᵀΣw hangi durumda 0 olabilir? (a) hiçbir zaman · (b) Σ pozitif tanımlı değilse (tekil), sıfır-olmayan bir w için · (c) w'nin toplamı 1 ise · (d) yalnız w = 0 · (e) bilmiyorum. **Doğru: b.**
4. (İplik 3) pandas'ta günlük kapanış serisinden log-getiri tek satır? (a) `p.diff()` · (b) `p.pct_change()` · (c) `np.log(p).diff()` · (d) `p.rolling(2).mean()` · (e) bilmiyorum. **Doğru: c.**
5. (İplik 4) Forward sözleşmesi opsiyondan nasıl ayrılır? (a) forward'da her iki taraf yükümlü, opsiyonda alıcının hakkı var · (b) opsiyon borsada işlem görmez · (c) forward'ın primi vardır · (d) fark yok · (e) bilmiyorum. **Doğru: a.**
6. (İplik 4, üst) K=100, vade sonu S=90 olan Avrupa put'un payoff'u? (a) 0 · (b) 10 · (c) −10 · (d) 90 · (e) bilmiyorum. **Doğru: b.**
7. (İplik 5) Hisse 100, risksiz faiz %5 (sürekli), 1 yıllık forward 108 kote ediliyor. Ne yaparsın? (a) hiçbir şey · (b) hisseyi borçla al, forward'da sat (F > S·e^{rT} ≈ 105,13) · (c) forward'da al, hisseyi açığa sat · (d) opsiyon al · (e) bilmiyorum. **Doğru: b.**
8. (İplik 5, üst) Put-call paritesi hangi varsayıma **dayanmaz**? (a) no-arbitrage · (b) Avrupa tipi opsiyon · (c) hisse fiyatının lognormal dağılımı · (d) aynı K ve T · (e) bilmiyorum. **Doğru: c** (parite modelden bağımsızdır).

Ön-bağlam Salih verirse iplik atlanır. Çıktı `## Anlayış haritası`.

## PLAN — DAG (görsel önce, `mcp__visualize`; düğüm numaralı)
```
1 Piyasa katılımcıları ve enstrüman sınıfları (hisse · tahvil · türev)
2 Forward/futures: tanım, payoff, F = S·e^{rT}                 ← 1
3 Opsiyon: call/put payoff, moneyness, Avrupa/Amerikan          ← 1
4 No-arbitrage ilkesi ve replikasyon                             ← 2
5 Put-call paritesi C − P = S − K·e^{−rT} (türetme + elle örnek) ← 3, 4
6 Fiyatı belirleyen değil sınırlayan: arbitraj sınırları        ← 5
7 Piyasa altyapısı: borsa ↔ OTC, marj, takas (Q14'e köprü)      ← 2, 3
```
Kenarlar: 1→2 · 1→3 · 2→4 · 3→5 · 4→5 · 5→6 · 2→7 · 3→7. Derinlik: 4,5 [T] · 2,3,6 [O] · 1,7 [S].

## Kutu başlıkları (TEACH sırası = topolojik; ≤8 düğüm/seans)
- Kutu 1 — Enstrüman sınıfları · Sektör: *Asset Classes & Market Participants*
- Kutu 2 — Forward ve futures · Sektör: *Forwards & Futures · Cost-of-Carry* — **Karar 73 formülü:** F = S·e^{rT}; sembol tablosu; S=100, r=0,05, T=1 → 105,13.
- Kutu 3 — Opsiyon payoff'ları · Sektör: *Call/Put Payoffs · Moneyness*
- Kutu 4 — No-arbitrage ve replikasyon · Sektör: *No-Arbitrage Principle · Replicating Portfolio*
- Kutu 5 — Put-call paritesi · Sektör: *Put-Call Parity* — türetme iki portföyle; elle S=100, K=100, r=0,05, T=1, C=10 → P = 10 − 100 + 95,12 = 5,12.
- Kutu 6 — Arbitraj sınırları · Sektör: *Arbitrage Bounds on Option Prices*
- Kutu 7 — Piyasa altyapısı · Sektör: *Exchange vs OTC · Margin · Clearing*

**"⌥ Jarvis notu" adayları:** Kutu 5 → PortRisk (K-002) hedef dilim S0'a köprü; Kutu 7 → Q14 mikroyapı.

## Pratik (Salih'in eli)
README Q1 `DONE`: 5 enstrümanın kâr/zarar diyagramı elle (kâğıt ya da matplotlib, Salih koşar) + 1 no-arbitrage örneği (soru 7 tipi) sayısal.

## CLOSE
Ders kaydı `ogrenme/quant/dersler/2026-MM-DD-Q1-piyasalar-enstrumanlar.md` · `ilerleme.md` satırı · `## Kalan` · Jarvis'e dönüş `cc/giden/Q1-geri-donus.md` (sapma + iskelet isteği Q2/Q3).
