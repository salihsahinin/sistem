// durum.ts: oda veri modeli; atomlar, yükle/kaydet, tur ve hareket ekleme.
// UI içermez; pano bu dosyadaki okuyucuları, araclar.ts yazıcıları kullanır.
import { atom, read, update } from 'claude-code'
import type { EngineInterface } from 'claude-code'

import type { Oda, OdaHareket, OdaPano, OdaTur, OdaTurTuru, AjanDurum, OdaSinif } from '../../types'
import { simdi, kisa } from './ortak'

export const PANE = 'jarvis-oda'
const STORE_AKTIF = 'oda:aktif'
const HAREKET_TAVAN = 400
const TUR_TAVAN = 600

export const odaAtom = atom({ plugin: 'jarvis-oda', key: 'oda' } as const, null as Oda | null)
export const ajanAtom = atom({ plugin: 'jarvis-oda', key: 'ajanlar' } as const, [] as AjanDurum[])
export const hareketAtom = atom({ plugin: 'jarvis-oda', key: 'hareket' } as const, [] as OdaHareket[])
export const panoAtom = atom({ plugin: 'jarvis-oda', key: 'pano' } as const, {
  acik: ['gorevler', 'oturumlar', 'sohbet'],
  ofset: { sohbet: null, akis: null, olaylar: null },
  genis: [],
} as OdaPano)

/** Pencere boyları (A2): sohbet 12, canlı akış 12, olaylar 6. */
export const PENCERE_BOY = { sohbet: 12, akis: 12, olaylar: 6 } as const

/** Sınıf başına varsayılan araç çağrısı tavanı (A5). */
export const SINIF_BUTCE: Record<OdaSinif, number> = { izole: 10, dosyali: 15, planli: 20, rol: 20 }

export function kosan(oda: Oda): number {
  return oda.gorevler.filter(g => g.durum === 'kosuyor').length
}

export function kuyrukSayisi(oda: Oda): number {
  return oda.gorevler.filter(g => g.durum === 'bekliyor').length
}

export function bekleyenOneri(oda: Oda): number {
  return oda.oneriler.filter(o => o.durum === 'bekliyor').length
}

/** Eski kayıtta sinif yok: ajan varsa rol, yoksa planli. */
export function sinifi(g: { sinif?: OdaSinif; ajan?: string }): OdaSinif {
  return g.sinif ?? (g.ajan ? 'rol' : 'planli')
}

export async function odaKaydet($: EngineInterface, oda: Oda): Promise<void> {
  await $.store.set('oda:' + oda.id, oda)
  await $.store.set(STORE_AKTIF, oda.id)
  await update($, odaAtom, () => oda)
  $.ui.status(`oda ${oda.baslik}: ${kosan(oda)}/${oda.maksParalel} koşuyor · ${kuyrukSayisi(oda)} kuyrukta · ${bekleyenOneri(oda)} öneri`)
}

export async function odaYukle($: EngineInterface): Promise<Oda | null> {
  const sicak = await read($, odaAtom)
  if (sicak) return sicak.maksParalel ? sicak : { ...sicak, maksParalel: 3 }
  const id = (await $.store.get(STORE_AKTIF)) as string | undefined
  if (!id) return null
  const ham = (await $.store.get('oda:' + id)) as Oda | undefined
  if (!ham) return null
  const oda: Oda = { ...ham, maksParalel: ham.maksParalel ?? 3 }
  await update($, odaAtom, () => oda)
  return oda
}

export function turEkle(oda: Oda, kim: string, tur: OdaTurTuru, metin: string, gorevId?: number): Oda {
  const yeni: OdaTur = { ts: simdi(), kim, tur, metin, gorevId }
  return { ...oda, turlar: [...oda.turlar, yeni].slice(-TUR_TAVAN) }
}

/** İşçi akışına parça ekler (yalnız oda görevine bağlı ajanlar); görev numarasını döndürür. */
export async function hareketEkle($: EngineInterface, agentId: string, tur: OdaHareket['tur'], ozet: string): Promise<number | undefined> {
  const oda = await odaYukle($)
  const g = oda?.gorevler.find(x => x.agentId === agentId)
  if (!g) return undefined
  const h: OdaHareket = { ts: simdi(), gorevId: g.id, agentId, tur, ozet: kisa(ozet, 400) }
  await update($, hareketAtom, eski => [...eski, h].slice(-HAREKET_TAVAN))
  return g.id
}

/** Satırın genişletme anahtarı (A7). */
export function satirAnahtari(t: { ts: string; kim?: string; gorevId?: number }): string {
  return t.ts + '|' + (t.kim ?? '#' + (t.gorevId ?? ''))
}

// ---------- atom erişimi (motor kuralı: read/update atomun tanımlandığı modülde çağrılır) ----------

export function odaSicak($: EngineInterface): Promise<Oda | null> {
  return read($, odaAtom)
}
/** Çizim için: atom boşsa store'dan okur, yazmaz (ui.render sırasında yazım reddedilir). */
export async function odaGoruntu($: EngineInterface): Promise<Oda | null> {
  const sicak = await read($, odaAtom)
  if (sicak) return sicak
  const id = (await $.store.get(STORE_AKTIF)) as string | undefined
  const ham = id ? ((await $.store.get('oda:' + id)) as Oda | undefined) : undefined
  return ham ? { ...ham, maksParalel: ham.maksParalel ?? 3 } : null
}
export function ajanlariOku($: EngineInterface): Promise<AjanDurum[]> {
  return read($, ajanAtom)
}
export async function ajanlariYaz($: EngineInterface, liste: AjanDurum[]): Promise<void> {
  await update($, ajanAtom, () => liste)
}
export function hareketleriOku($: EngineInterface): Promise<OdaHareket[]> {
  return read($, hareketAtom)
}
export function panoOku($: EngineInterface): Promise<OdaPano> {
  return read($, panoAtom)
}
export async function panoGuncelle($: EngineInterface, fn: (p: OdaPano) => OdaPano): Promise<void> {
  await update($, panoAtom, fn)
}
