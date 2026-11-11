// altoda.ts: alt-oda (Karar 130 B9); üst odanın görev düğümü içinde rol ajanlarının turlu münazarası.
// Akış: tur 1 (bağımsız ilk görüş) → tur 2..T (diğerlerinin önceki tur metinleri) → son konum → hakem.
// Özgünlük kuralı kodda: (1) araç şeması yalnız baslik/soru/kapsam/done/ajanlar/tur/hakem kabul eder, başka alan reddedilir;
// (2) soru/kapsam/done uzunluk sınırlı; (3) ajan emri metin.ts'teki sabit şablondur, Jarvis metni yalnız bu üç alandan girer;
// (4) ajan cevabı String(answer) olarak saklanır, hiçbir adım onu kısaltmaz, düzeltmez, özetlemez; (5) çıktıyı yalnız hakem tartar.
// Her ajan çağrısı sıradan bir rol görevi olarak oda kuyruğuna girer: paralel sınır ve bütçe kapısı aynen işler.
import type { EngineInterface, ToolSpec } from 'claude-code'

import type { Oda, OdaAltOda, OdaAltOdaAsama, OdaAltOdaMetin, OdaGorev } from '../../types'
import { SINIF_BUTCE, odaYukle, turEkle, kosan } from './durum'
import { altOdaTurEmri, altOdaSonKonumEmri, altOdaHakemEmri } from './metin'
import { kisa, simdi } from './ortak'
import { depoBul, durumKos, kaydet, kuyrukIsle, type ModAyar } from './araclar'

/** Uzunluk sınırları: emir bu alanlara gömülemesin (özgünlük kuralı). */
export const ALT_ODA_SINIR = { baslik: 120, soru: 600, kapsam: 400, done: 200 } as const
const IZINLI_ALANLAR = new Set(['baslik', 'soru', 'kapsam', 'done', 'ajanlar', 'tur', 'hakem'])
/** Motorun araç girdisine kendisi eklediği alanlar; şema dışı sayılmaz. */
const MOTOR_ALANLARI = new Set(['tool', 'tool_use_id', 'agentId', 'consent', 'requestMeta'])
const AJAN_ADI = /^[a-z0-9_-]+$/i

export const ALT_ODA_ARACI: ToolSpec = {
  isDeferred: false,
  name: 'oda_altoda_ac',
  description:
    'Aktif odada alt-oda (münazara düğümü) açar: 2-5 rol ajanı (.claude/agents/<ad>.md) tur tur konuşur. Tur 1 bağımsız ilk görüş; sonraki turlarda her ajan diğerlerinin önceki tur metnini görür; son turdan sonra her ajan tek paragraf son konum yazar. Ortak çıktı (konuşmanın tamamı + son konumlar) değiştirilmeden saklanır, hakem ajanı done cümlesine göre tartar. Özgünlük kuralı: yalnız soru, kapsam ve done verilir; yöntem, üslup ya da görüş alanı yoktur, verilirse reddedilir. Durum kütüğünde hedef düğümü + ajan başına iş açılır. Bitince Jarvis "[oda] alt-oda #K" ile uyandırılır.',
  inputSchema: {
    type: 'object',
    additionalProperties: false,
    properties: {
      baslik: { type: 'string', maxLength: ALT_ODA_SINIR.baslik, description: 'Kısa alt-oda adı' },
      soru: { type: 'string', maxLength: ALT_ODA_SINIR.soru, description: 'Münazara sorusu (≤ 600 karakter)' },
      kapsam: { type: 'string', maxLength: ALT_ODA_SINIR.kapsam, description: 'Kapsam sınırı (≤ 400 karakter)' },
      done: { type: 'string', maxLength: ALT_ODA_SINIR.done, description: 'Tek cümle done (≤ 200 karakter); hakemin tek ölçütü' },
      ajanlar: { type: 'array', items: { type: 'string' }, minItems: 2, maxItems: 5, description: '2-5 rol ajanı adı (.claude/agents/<ad>.md)' },
      tur: { type: 'integer', minimum: 1, maximum: 4, description: 'Münazara tur sayısı (varsayılan 2, en çok 4)' },
      hakem: { type: 'string', description: 'İsteğe bağlı hakem ajanı (varsayılan hakem); katılımcı olamaz' },
    },
    required: ['baslik', 'soru', 'kapsam', 'done', 'ajanlar'],
  },
} as ToolSpec

/** Ajan tanımı var mı: cwd/.claude/agents, depo/jarvis/.claude/agents, depo/.claude/agents. */
async function ajanVarMi($: EngineInterface, ad: string): Promise<boolean> {
  const cwd = (await $.session.cwd().catch(() => '')).replace(/\\/g, '/').replace(/\/+$/, '')
  const depo = await depoBul($)
  const adaylar = [cwd && `${cwd}/.claude/agents/${ad}.md`, depo && `${depo}/jarvis/.claude/agents/${ad}.md`, depo && `${depo}/.claude/agents/${ad}.md`].filter(Boolean) as string[]
  for (const y of adaylar) {
    try {
      if (await $.fs.exists(y)) return true
    } catch {
      /* fs yok */
    }
  }
  return false
}

type AltOdaGirdi = Record<string, unknown>

/** Girdi doğrulama: şema dışı alan, uzunluk, ajan sayısı/adı/varlığı, tur aralığı, hakem ≠ katılımcı. */
async function dogrula($: EngineInterface, g: AltOdaGirdi): Promise<{ hata: string } | { baslik: string; soru: string; kapsam: string; done: string; ajanlar: string[]; tur: number; hakem: string }> {
  const fazla = Object.keys(g).filter(k => !IZINLI_ALANLAR.has(k) && !MOTOR_ALANLARI.has(k))
  if (fazla.length) return { hata: `şemada olmayan alan: ${fazla.join(', ')}. Özgünlük kuralı: alt-odaya yalnız baslik, soru, kapsam, done, ajanlar, tur, hakem verilir; yöntem ya da görüş emri yazılmaz.` }
  const metin: Record<string, string> = {}
  for (const k of ['baslik', 'soru', 'kapsam', 'done'] as const) {
    const v = g[k]
    if (typeof v !== 'string' || !v.trim()) return { hata: `${k} gerekli.` }
    if (v.length > ALT_ODA_SINIR[k]) return { hata: `${k} en çok ${ALT_ODA_SINIR[k]} karakter (${v.length} verildi); emir bu alana gömülemez.` }
    metin[k] = v
  }
  if (/[\r\n]/.test(metin.done!)) return { hata: 'done tek cümle olmalı (satır sonu yok).' }
  const ham = Array.isArray(g.ajanlar) ? (g.ajanlar as unknown[]) : []
  const ajanlar = ham.map(a => (typeof a === 'string' ? a.trim() : ''))
  if (ajanlar.length < 2 || ajanlar.length > 5) return { hata: `ajanlar 2-5 rol ajanı olmalı (${ajanlar.length} verildi).` }
  if (ajanlar.some(a => !AJAN_ADI.test(a))) return { hata: 'ajan adı yalnız harf, rakam, - ve _ içerir.' }
  if (new Set(ajanlar).size !== ajanlar.length) return { hata: 'ajanlar tekrarsız olmalı.' }
  const turHam = g.tur === undefined ? 2 : Number(g.tur)
  if (!Number.isInteger(turHam) || turHam < 1 || turHam > 4) return { hata: `tur 1-4 arası tam sayı olmalı (${String(g.tur)} verildi).` }
  const hakem = typeof g.hakem === 'string' && g.hakem.trim() ? g.hakem.trim() : 'hakem'
  if (!AJAN_ADI.test(hakem)) return { hata: 'hakem adı yalnız harf, rakam, - ve _ içerir.' }
  if (ajanlar.includes(hakem)) return { hata: `hakem (${hakem}) katılımcı olamaz: yapan ≠ ölçen.` }
  const yok: string[] = []
  for (const a of [...ajanlar, hakem]) if (!(await ajanVarMi($, a))) yok.push(a)
  if (yok.length) return { hata: `ajan tanımı yok: ${yok.join(', ')} (.claude/agents/<ad>.md).` }
  return { baslik: metin.baslik!, soru: metin.soru!, kapsam: metin.kapsam!, done: metin.done!, ajanlar, tur: turHam, hakem }
}

/** Alt-oda aşaması için rol görevlerini kuyruğa ekler (bekliyor); emir metin.ts şablonundan gelir. */
function asamaGorevleri(oda: Oda, a: OdaAltOda, asama: OdaAltOdaAsama, tur?: number): { oda: Oda; alt: OdaAltOda } {
  const kisiler = asama === 'hakem' ? [a.hakem] : a.ajanlar
  const yeniGorevler: OdaGorev[] = []
  let id = oda.gorevler.length
  for (const ajan of kisiler) {
    id++
    const emir = asama === 'tur' ? altOdaTurEmri(oda.id, a, ajan, tur ?? 1) : asama === 'sonKonum' ? altOdaSonKonumEmri(oda.id, a, ajan) : altOdaHakemEmri(oda.id, a)
    const etiket = asama === 'tur' ? `tur ${tur}/${a.turSayisi}` : asama === 'sonKonum' ? 'son konum' : 'hakem'
    yeniGorevler.push({
      id,
      baslik: `alt-oda #${a.id} ${etiket} · ${ajan}`,
      emir,
      zorluk: 'orta',
      model: 'sonnet',
      sinif: 'rol',
      ajan,
      modelAcik: false,
      done: a.done,
      butce: SINIF_BUTCE.rol,
      cagri: 0,
      durum: 'bekliyor',
      acilis: simdi(),
      altOda: { id: a.id, asama, ...(tur ? { tur } : {}) },
    })
  }
  const alt: OdaAltOda = { ...a, gorevIds: [...a.gorevIds, ...yeniGorevler.map(g => g.id)] }
  const yeni = { ...oda, gorevler: [...oda.gorevler, ...yeniGorevler], altOdalar: (oda.altOdalar ?? []).map(x => (x.id === a.id ? alt : x)) }
  return { oda: turEkle(yeni, 'oda', 'not', `alt-oda #${a.id} ${asama === 'tur' ? 'tur ' + tur : asama === 'sonKonum' ? 'son konum' : 'hakem'} aşaması: ${kisiler.join(', ')} kuyrukta`), alt }
}

/** Kütük: hedef düğümü (--tur hedef) + ajan başına katkı işi (--hedef N); hepsi işleme alınır (oturum oda-<id>). */
async function kutukAc($: EngineInterface, oda: Oda, a: OdaAltOda, alan: string): Promise<{ kutuk?: OdaAltOda['kutuk']; not: string }> {
  const oturum = 'oda-' + oda.id
  const h = await durumKos($, ['ac', '--alan', alan, '--is', `oda alt-oda #${a.id} ${a.baslik}`, '--sonraki', kisa(a.done, 200), '--oturum', oturum, '--tur', 'hedef'])
  const hedefNo = /^#(\d+)/.exec(h.cikti)?.[1]
  if (!h.ok || !hedefNo) return { not: 'kütük hedefi açılamadı: ' + kisa(h.cikti, 160) }
  const hedefId = Number(hedefNo)
  await durumKos($, ['al', String(hedefId), '--oturum', oturum])
  const isler: Record<string, number> = {}
  for (const ajan of a.ajanlar) {
    const r = await durumKos($, ['ac', '--alan', alan, '--is', `alt-oda #${a.id} ${ajan} katkısı`, '--sonraki', kisa(a.soru, 200), '--oturum', oturum, '--hedef', String(hedefId)])
    const no = /^#(\d+)/.exec(r.cikti)?.[1]
    if (!r.ok || !no) continue
    isler[ajan] = Number(no)
    await durumKos($, ['al', no, '--oturum', oturum])
  }
  await durumKos($, ['graf'])
  return { kutuk: { hedefId, isler }, not: `kütük hedef #${hedefId}, işler ${Object.values(isler).map(n => '#' + n).join(' ')}` }
}

/** Kütük kapanışı: önce katkı işleri, sonra hedef; kanıt "oda <odaId> alt-oda #K". */
async function kutukKapat($: EngineInterface, oda: Oda, a: OdaAltOda): Promise<string | undefined> {
  if (!a.kutuk) return undefined
  const kanit = `oda ${oda.id} alt-oda #${a.id}`
  const hatalar: string[] = []
  for (const no of Object.values(a.kutuk.isler)) {
    const r = await durumKos($, ['bitir', String(no), '--kanit', kanit])
    if (!r.ok) hatalar.push(`#${no}: ${kisa(r.cikti, 80)}`)
  }
  const h = await durumKos($, ['bitir', String(a.kutuk.hedefId), '--kanit', kanit])
  if (!h.ok) hatalar.push(`hedef #${a.kutuk.hedefId}: ${kisa(h.cikti, 80)}`)
  await durumKos($, ['graf'])
  return hatalar.length ? `kütük kapanışında hata: ${hatalar.join('; ')}` : `kütük hedef #${a.kutuk.hedefId} ve ${Object.keys(a.kutuk.isler).length} iş kapandı (kanıt: ${kanit})`
}

export async function altOdaAc($: EngineInterface, girdi: AltOdaGirdi, ayar: ModAyar): Promise<string> {
  let oda = await odaYukle($)
  if (!oda) return 'Oda yok; önce oda_ac.'
  const d = await dogrula($, girdi ?? {})
  if ('hata' in d) return 'Alt-oda açılmadı: ' + d.hata
  const id = (oda.altOdalar?.length ?? 0) + 1
  let alt: OdaAltOda = {
    id,
    baslik: d.baslik,
    soru: d.soru,
    kapsam: d.kapsam,
    done: d.done,
    ajanlar: d.ajanlar,
    hakem: d.hakem,
    turSayisi: d.tur,
    turlar: [],
    sonKonumlar: [],
    durum: 'tur',
    aktifTur: 1,
    gorevIds: [],
    acilis: simdi(),
  }
  if (ayar.durumKaydi) {
    const k = await kutukAc($, oda, alt, ayar.alan)
    alt = { ...alt, ...(k.kutuk ? { kutuk: k.kutuk } : {}), kutukNot: k.not }
  }
  oda = (await odaYukle($)) ?? oda
  oda = turEkle({ ...oda, altOdalar: [...(oda.altOdalar ?? []), alt] }, 'jarvis', 'gorev', `alt-oda #${id} açıldı: ${alt.baslik} · ajanlar ${alt.ajanlar.join(', ')} · ${alt.turSayisi} tur · hakem ${alt.hakem}${alt.kutukNot ? ' · ' + alt.kutukNot : ''}`)
  oda = asamaGorevleri(oda, alt, 'tur', 1).oda
  await kaydet($, oda)
  const son = (await kuyrukIsle($)) ?? oda
  return `Alt-oda #${id} "${alt.baslik}" açıldı: ${alt.ajanlar.length} ajan × ${alt.turSayisi} tur + son konum + hakem (${alt.hakem}). Tur 1 başladı; paralel ${kosan(son)}/${son.maksParalel}.${alt.kutukNot ? ' ' + alt.kutukNot + '.' : ''} Bitince "[oda] alt-oda #${id}" ile uyanırsın; tam döküm oda_oku altOdaId=${id}.`
}

/** Aşamanın tüm görevleri kapandı mı. */
function asamaBitti(oda: Oda, a: OdaAltOda, asama: OdaAltOdaAsama, tur?: number): boolean {
  const ilgili = oda.gorevler.filter(g => a.gorevIds.includes(g.id) && g.altOda?.asama === asama && (asama !== 'tur' || g.altOda?.tur === tur))
  return ilgili.length > 0 && ilgili.every(g => g.durum === 'bitti' || g.durum === 'hata')
}

/**
 * Alt-oda görevinin bitişi (turn.complete). Alt-oda görevi değilse false döner, sıradan gorevBitti koşar.
 * Ajan metni String(answer) olarak aynen saklanır; sonraki aşama kuyruğa girer; hakemden sonra kütük kapanır, Jarvis uyanır.
 */
export async function altOdaGorevBitti($: EngineInterface, e: { agentId?: string; reason: string; isAborted?: boolean; answer?: string; text?: string }, ayar: ModAyar): Promise<boolean> {
  if (!e.agentId) return false
  let oda = await odaYukle($)
  if (!oda) return false
  const gorev = oda.gorevler.find(g => g.agentId === e.agentId && g.durum === 'kosuyor' && g.altOda)
  if (!gorev || !gorev.altOda) return false
  const a0 = oda.altOdalar?.find(x => x.id === gorev.altOda!.id)
  if (!a0) return false
  const butceAsildi = Boolean(gorev.butce && (gorev.cagri ?? 0) > Math.floor(gorev.butce * 1.5))
  const basarili = e.reason === 'answer' && !e.isAborted && !butceAsildi
  const neden = butceAsildi ? `bütçe aşıldı (${gorev.cagri}/${gorev.butce})` : e.isAborted ? 'ajan durduruldu' : `ajan hatayla bitti (${e.reason})`
  // Ajan metni: dönüştürme yok (trim, kısaltma, özet yok).
  const metin = basarili ? String(e.answer ?? '') : ''
  const kayit: OdaAltOdaMetin = { ajan: gorev.ajan ?? '?', ...(gorev.altOda.tur ? { tur: gorev.altOda.tur } : {}), metin, ts: simdi(), ...(basarili ? {} : { hata: neden }) }
  let a: OdaAltOda = a0
  if (gorev.altOda.asama === 'tur') a = { ...a, turlar: [...a.turlar, kayit] }
  else if (gorev.altOda.asama === 'sonKonum') a = { ...a, sonKonumlar: [...a.sonKonumlar, kayit] }
  else a = { ...a, hakemRaporu: basarili ? metin : `(hakem çağrısı başarısız: ${neden})` }
  const kapanan: OdaGorev = { ...gorev, durum: basarili ? 'bitti' : 'hata', sonuc: basarili ? metin : neden, kapanis: simdi() }
  oda = {
    ...oda,
    gorevler: oda.gorevler.map(g => (g.id === gorev.id ? kapanan : g)),
    altOdalar: (oda.altOdalar ?? []).map(x => (x.id === a.id ? a : x)),
  }
  oda = turEkle(oda, `işçi #${gorev.id}`, 'rapor', `${gorev.baslik}: ${basarili ? `metin kaydedildi (${metin.length} karakter)` : neden}`, gorev.id)
  // Aşama ilerletme.
  let bitti = false
  if (a.durum === 'tur' && asamaBitti(oda, a, 'tur', a.aktifTur)) {
    if (a.aktifTur < a.turSayisi) {
      a = { ...a, aktifTur: a.aktifTur + 1 }
      oda = { ...oda, altOdalar: oda.altOdalar!.map(x => (x.id === a.id ? a : x)) }
      ;({ oda, alt: a } = asamaGorevleri(oda, a, 'tur', a.aktifTur))
    } else {
      a = { ...a, durum: 'sonKonum' }
      oda = { ...oda, altOdalar: oda.altOdalar!.map(x => (x.id === a.id ? a : x)) }
      ;({ oda, alt: a } = asamaGorevleri(oda, a, 'sonKonum'))
    }
  } else if (a.durum === 'sonKonum' && asamaBitti(oda, a, 'sonKonum')) {
    a = { ...a, durum: 'hakem' }
    oda = { ...oda, altOdalar: oda.altOdalar!.map(x => (x.id === a.id ? a : x)) }
    ;({ oda, alt: a } = asamaGorevleri(oda, a, 'hakem'))
  } else if (a.durum === 'hakem' && asamaBitti(oda, a, 'hakem')) {
    a = { ...a, durum: basarili ? 'bitti' : 'hata', kapanis: simdi() }
    oda = { ...oda, altOdalar: oda.altOdalar!.map(x => (x.id === a.id ? a : x)) }
    bitti = true
  }
  await kaydet($, oda)
  if (bitti) {
    // Hakem başarılıysa kütük kanıtla kapanır; değilse açık kalır, neden yazılır.
    const kutukNot = a.durum === 'bitti' ? await kutukKapat($, oda, a) : a.kutuk ? `kütük hedef #${a.kutuk.hedefId} açık kaldı: hakem ${neden}` : undefined
    const taze = (await odaYukle($)) ?? oda
    const guncel = turEkle({ ...taze, altOdalar: (taze.altOdalar ?? []).map(x => (x.id === a.id ? { ...x, ...(kutukNot ? { kutukNot } : {}) } : x)) }, 'oda', 'not', `alt-oda #${a.id} ${a.durum}${kutukNot ? ' · ' + kutukNot : ''}`)
    await kaydet($, guncel)
    $.ui.toast(`Oda: alt-oda #${a.id} ${a.durum}`)
    if (ayar.otoUyandir) {
      const ozet = `[oda] alt-oda #${a.id} "${a.baslik}" ${a.durum} (ajanlar ${a.ajanlar.join(', ')}, ${a.turSayisi} tur, hakem ${a.hakem}). Hakem raporu:\n${kisa(a.hakemRaporu ?? '', 1500)}\n(tam döküm: oda_oku altOdaId=${a.id})${kutukNot ? '\n' + kutukNot : ''}`
      void $.prompt.submit({ text: ozet }).catch(() => undefined)
    }
  }
  await kuyrukIsle($)
  return true
}
