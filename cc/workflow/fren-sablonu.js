// FREN ŞABLONU — Workflow script'lerine kopyalanır (İB-54 adım 2, Karar 74 M-4 (d) paket B "fan-out ÖNCESİ kestirim kapısı + aktif durdurma";
// Karar 39: uç-eşikli, kalite kısılmaz). Kök neden: fren metindeydi, taahhüt anı yerine ölçüm anındaydı, fan-out atomikti
// (raporlar/2026-08-29-ib54-delinme-kok-neden.md KN-1/2/4). Bu blok freni KODA taşır: her agent() çağrısı TAAHHÜT ANINDA sayılır,
// tavan aşımında fırlatır (Workflow'un kendi `budget` mekanizmasıyla aynı sınıf; budget yalnız "+Nk" verilince çalışır, bu her koşumda).
// Eşikler (m.29; taban silver amb_olgu_kosum @b16b1a9, 29 wf: ajan/wf p50 12 · max 23; ajan başı araç çağrısı p50 18 · p95 54):
//   AJAN_TAVAN = 36 (p50 × 3)   — aşımda agent() FIRLATIR (koşum durur, kısmi sonuç script'in elinde)
//   DALGA_TAVAN = 12 (p50)      — tek parallel()/pipeline() dalgasında ajan sayısı; aşımda log + ikinci dalga (tek-dalga kuralı: KN-4)
// REJİM ETİKETİ (m.46(d)): [rejim: manuel-tempo · kota-bol · ekonomi −%30 (Salih 08-15) · AS-OF 2026-08-29] — rejim değişince yeniden açılır.
// Kullanım: aşağıdaki bloğu meta'dan sonra yapıştır; script gövdesinde `agent(` yerine `ajan(` çağır; dalgayı `dalga([...thunk])` ile koş.

const FREN = { AJAN_TAVAN: 36, DALGA_TAVAN: 12, REJIM: 'manuel-tempo · kota-bol · ekonomi -%30 (08-15) · AS-OF 2026-08-29' }
let ajanSayaci = 0
const ajan = (prompt, opts) => {
  ajanSayaci += 1
  if (ajanSayaci > FREN.AJAN_TAVAN) {
    log(`FREN (İB-54): ${ajanSayaci}. ajan — tavan ${FREN.AJAN_TAVAN} (rejim: ${FREN.REJIM}); koşum durduruluyor, kısmi sonuç döndür`)
    throw new Error(`İB-54 ajan tavanı ${FREN.AJAN_TAVAN} aşıldı (${ajanSayaci})`)
  }
  return agent(prompt, opts)
}
// Dalga kapısı: fan-out ÖNCESİ genişlik kontrolü (taahhüt anı). Genişlik > DALGA_TAVAN ise tek seferde değil parça parça koşar (barrier).
const dalga = async (thunks) => {
  if (thunks.length <= FREN.DALGA_TAVAN) return parallel(thunks)
  log(`FREN (İB-54): dalga genişliği ${thunks.length} > ${FREN.DALGA_TAVAN} — ${Math.ceil(thunks.length / FREN.DALGA_TAVAN)} parçada koşuluyor`)
  const out = []
  for (let i = 0; i < thunks.length; i += FREN.DALGA_TAVAN) out.push(...(await parallel(thunks.slice(i, i + FREN.DALGA_TAVAN))))
  return out
}
// Kapanışta kayıt: return değerine { fren: { ajan: ajanSayaci, tavan: FREN } } ekle — ambar (amb_olgu_kosum) ile kıyas için.
