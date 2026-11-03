// durum.ts: graf modunun veri katmanı; atomlar, akis-graf.json + kütük + defter yükleme, oda köprüsü okuma.
// UI içermez; read/update yalnız bu dosyada (motor kuralı: atom tanımlandığı modülde okunur).
import { atom, read, update } from 'claude-code'
import type { EngineInterface } from 'claude-code'

import type { Graf, GrafEk, GrafGorunum, KutukOlay } from '../../types'

export const PANE = 'jarvis-graf'

const grafAtom = atom({ plugin: 'jarvis-graf', key: 'graf' } as const, null as Graf | null)
const gorunumAtom = atom({ plugin: 'jarvis-graf', key: 'gorunum' } as const, {
  alan: 'tum',
  yalnizAcik: false,
  secili: null,
  yol: '',
  mtimeMs: 0,
  hata: null,
  html: null,
  htmlHata: null,
  kopruTs: '',
} as GrafGorunum)
const ekAtom = atom({ plugin: 'jarvis-graf', key: 'ek' } as const, { olaylar: [], defter: '', olayMtime: 0, defterMtime: 0 } as GrafEk)

export type Yollar = { graf: string; jarvis: string; depo: string }

export function grafOku($: EngineInterface): Promise<Graf | null> {
  return read($, grafAtom)
}
export function gorunumOku($: EngineInterface): Promise<GrafGorunum> {
  return read($, gorunumAtom)
}
export async function gorunumGuncelle($: EngineInterface, fn: (g: GrafGorunum) => GrafGorunum): Promise<void> {
  await update($, gorunumAtom, fn)
}
export function ekOku($: EngineInterface): Promise<GrafEk> {
  return read($, ekAtom)
}

/** B7: cwd'den köke kadar her üst dizinde ortak/akis-graf.json arar; bulunan yol önbelleğe girer. */
export async function yolBul($: EngineInterface): Promise<Yollar | null> {
  try {
    const onceki = (await read($, gorunumAtom)).yol
    if (onceki && (await $.fs.exists(onceki))) {
      const depo = onceki.replace(/\/ortak\/akis-graf\.json$/, '')
      return { graf: onceki, jarvis: depo + '/jarvis', depo }
    }
    let dizin = (await $.session.cwd()).replace(/\\/g, '/').replace(/\/+$/, '')
    for (let i = 0; i < 32 && dizin; i++) {
      const graf = dizin + '/ortak/akis-graf.json'
      if (await $.fs.exists(graf)) return { graf, jarvis: dizin + '/jarvis', depo: dizin }
      const ust = dizin.replace(/\/[^/]*$/, '')
      if (ust === dizin || !ust.includes('/')) break
      dizin = ust
    }
  } catch {
    /* fs erişimi yok (test ortamı) */
  }
  return null
}

/** Graf JSON'unu (değiştiyse) ve yanındaki kütük + defteri yükler. */
export async function grafYukle($: EngineInterface, zorla = false): Promise<void> {
  const yol = await yolBul($)
  if (!yol) {
    // B7: graf bir kez yüklendiyse geçici arama başarısızlığı hata satırı yazmaz.
    if (!(await read($, grafAtom))) await update($, gorunumAtom, g => ({ ...g, hata: "ortak/akis-graf.json bulunamadı (cwd'den köke kadar arandı)" }))
    return
  }
  try {
    const st = await $.fs.stat(yol.graf)
    const g = await read($, gorunumAtom)
    if (zorla || g.mtimeMs !== st.mtimeMs || g.yol !== yol.graf) {
      const graf = JSON.parse(await $.fs.read(yol.graf)) as Graf
      await update($, grafAtom, () => graf)
      await update($, gorunumAtom, x => ({ ...x, yol: yol.graf, mtimeMs: st.mtimeMs, hata: null }))
      const acik = graf.dugumler.filter(n => n.tur === 'is' && (n.durum === 'acik' || n.durum === 'islemde')).length
      $.ui.status(`graf: ${graf.dugumler.length} düğüm · ${acik} açık iş`)
    }
  } catch (err) {
    await update($, gorunumAtom, x => ({ ...x, hata: 'akis-graf.json okunamadı: ' + String(err) }))
  }
  await ekYukle($, yol, zorla)
}

async function ekYukle($: EngineInterface, yol: Yollar, zorla: boolean): Promise<void> {
  const ek = await read($, ekAtom)
  const olayYolu = yol.depo + '/ortak/durum-olay.jsonl'
  const defterYolu = yol.jarvis + '/kuyruk/senaryo-defteri.md'
  let yeni: GrafEk = ek
  try {
    const st = await $.fs.stat(olayYolu)
    if (zorla || st.mtimeMs !== ek.olayMtime) {
      const olaylar: KutukOlay[] = []
      for (const satir of (await $.fs.read(olayYolu)).split(/\r?\n/)) {
        if (!satir.trim()) continue
        try {
          olaylar.push(JSON.parse(satir) as KutukOlay)
        } catch {
          /* bozuk satır atlanır */
        }
      }
      yeni = { ...yeni, olaylar, olayMtime: st.mtimeMs }
    }
  } catch {
    /* kütük yoksa detay olaysız çizilir */
  }
  try {
    const st = await $.fs.stat(defterYolu)
    if (zorla || st.mtimeMs !== ek.defterMtime) yeni = { ...yeni, defter: await $.fs.read(defterYolu), defterMtime: st.mtimeMs }
  } catch {
    /* defter yoksa karar paragrafı çıkmaz */
  }
  if (yeni !== ek) await update($, ekAtom, () => yeni)
}

/** B5: oda köprüsü; ortak/graf-secim.json yeni bir seçim taşıyorsa döndürür (ts karşılaştırması, dosya silinmez). */
export async function kopruOku($: EngineInterface, ilk = false): Promise<string | null> {
  const yol = await yolBul($)
  if (!yol) return null
  const dosya = yol.depo + '/ortak/graf-secim.json'
  try {
    if (!(await $.fs.exists(dosya))) return null
    const k = JSON.parse(await $.fs.read(dosya)) as { secili?: string; ts?: string }
    const g = await read($, gorunumAtom)
    if (!k.secili || !k.ts || k.ts <= g.kopruTs) return null
    await update($, gorunumAtom, x => ({ ...x, kopruTs: k.ts!, ...(ilk ? {} : { secili: k.secili!, yalnizAcik: false }) }))
    return ilk ? null : k.secili
  } catch {
    return null
  }
}
