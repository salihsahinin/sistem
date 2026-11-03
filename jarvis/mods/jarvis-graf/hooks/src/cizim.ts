// cizim.ts: graf SVG'si (B1); satır = seans, x = zaman, hedef şeridi üstte, açıklama şeridi en üstte.
// Saf fonksiyon: satır düzenini (metin.ts) alır, SVG metni döndürür; tıklama pano.tsx'teki düğme ızgarasında.
import type { Graf, GrafDugum } from '../../types'
import type { Satir } from './metin'
import { zaman } from './metin'
import { kisa } from './ortak'

const RENK = { acik: '#cf222e', islemde: '#d4a017', tamam: '#2da44e', bayat: '#6e7781', hedef: '#8250df', seans: '#57606a' }
const ALAN_TONU = ['#ddf4ff', '#fff8c5', '#dafbe1', '#ffebe9', '#fbefff', '#fff1e5']

export function dolgu(n: GrafDugum): string {
  if (n.tur === 'seans') return RENK.seans
  if (n.tur === 'hedef') return RENK.hedef
  if (n.durum === 'tamam' || n.durum === 'tuketildi') return RENK.tamam
  if (n.durum === 'islemde') return RENK.islemde
  if (n.durum === 'bayat') return RENK.bayat
  return RENK.acik
}

const kac = (m: string) => m.replace(/[<>&"]/g, c => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;' })[c] ?? c)

export const SATIR_Y = 34
const UST = 64 // açıklama şeridi + tarih ekseni
const SOL = 190 // satır etiketi sütunu
const R = 9

const ADIM = 2 * R + 4

function gunBasi(t: number): number {
  const d = new Date(t)
  d.setHours(0, 0, 0, 0)
  return d.getTime()
}

function gunlereBol(dugumler: GrafDugum[]): Map<number, GrafDugum[]> {
  const m = new Map<number, GrafDugum[]>()
  for (const n of [...dugumler].sort((a, b) => zaman(a) - zaman(b))) {
    const t = zaman(n)
    if (!t) continue
    const k = gunBasi(t)
    m.set(k, [...(m.get(k) ?? []), n])
  }
  return m
}

type Gun = { bas: number; son: number; x: number; w: number }

export type Olcek = { x: (t: number) => number; gunler: Gun[]; genislik: number; sutun: number }

/**
 * Gün-sütunlu zaman ölçeği: her günün genişliği o gün en kalabalık satırın düğüm sayısına göre (boş gün 18 px),
 * gün içi doğrusal. Gün başına sütun sayısı (sutun) 12'den 3'e iner, toplam pane genişliğine (W) sığana dek;
 * sığmayan düğümler satır içinde alt sıraya sarar. Sığarsa sütunlar orantılı açılır.
 */
export function olcek(satirlar: Satir[], W: number): Olcek {
  const zamanlar = [...satirlar.flatMap(s => s.dugumler.map(zaman)), ...satirlar.map(s => s.bas), ...satirlar.map(s => s.son)].filter(t => t > 0)
  const t0 = zamanlar.length ? Math.min(...zamanlar) : Date.now()
  const t1 = zamanlar.length ? Math.max(...zamanlar) : t0
  const kapasite = new Map<number, number>()
  for (const s of satirlar) for (const [g, grup] of gunlereBol(s.dugumler)) kapasite.set(g, Math.max(kapasite.get(g) ?? 0, grup.length))
  const gunListe: { bas: number; son: number; c: number }[] = []
  for (let d = new Date(gunBasi(t0)); d.getTime() <= t1; ) {
    const bas = d.getTime()
    d.setDate(d.getDate() + 1)
    gunListe.push({ bas, son: d.getTime(), c: kapasite.get(bas) ?? 0 })
  }
  const alan = W - SOL - 24
  const genislikler = (sutun: number) => gunListe.map(g => (g.c > 0 ? Math.min(g.c, sutun) * ADIM + 14 : 18))
  let sutun = 12
  while (sutun > 3 && genislikler(sutun).reduce((a, w) => a + w, 0) > alan) sutun--
  const ham = genislikler(sutun)
  const toplam = ham.reduce((a, w) => a + w, 0) || 1
  const k = toplam < alan ? alan / toplam : 1
  let cx = SOL + 10
  const gunler: Gun[] = gunListe.map((g, i) => {
    const r = { bas: g.bas, son: g.son, x: cx, w: ham[i]! * k }
    cx += r.w
    return r
  })
  const x = (t: number): number => {
    const g = gunler.find(v => t >= v.bas && t < v.son) ?? (t < t0 ? gunler[0] : gunler.at(-1))
    if (!g) return SOL + 10
    return g.x + Math.min(1, Math.max(0, (t - g.bas) / (g.son - g.bas))) * g.w
  }
  return { x, gunler, genislik: Math.max(W, cx + 14), sutun }
}

/** Satırın alt sıra sayısı: gün başına düğüm / sütun, en kalabalık günde. */
function altSira(s: Satir, sutun: number): number {
  let n = 1
  for (const grup of gunlereBol(s.dugumler).values()) n = Math.max(n, Math.ceil(grup.length / sutun))
  return n
}

export function svgCiz(graf: Graf, satirlar: Satir[], secili: string | null, genislik: number): string {
  const olc = olcek(satirlar, Math.max(900, genislik))
  const W = olc.genislik
  const x = olc.x
  const yukseklik = satirlar.map(s => SATIR_Y + (altSira(s, olc.sutun) - 1) * ADIM)
  const ustY: number[] = []
  yukseklik.reduce((acc, h, i) => ((ustY[i] = acc), acc + h), UST)
  const H = UST + yukseklik.reduce((a, h) => a + h, 0) + 16
  const parca: string[] = []

  // açıklama şeridi
  const aciklama: [string, string][] = [
    ['açık', RENK.acik],
    ['işlemde', RENK.islemde],
    ['tamam', RENK.tamam],
    ['bayat', RENK.bayat],
    ['hedef', RENK.hedef],
  ]
  let ax = 8
  for (const [ad, renk] of aciklama) {
    parca.push(`<circle cx="${ax + 6}" cy="14" r="6" fill="${renk}"/><text x="${ax + 16}" y="18" font-size="11" fill="currentColor">${ad}</text>`)
    ax += 24 + ad.length * 7
  }
  parca.push(`<line x1="${ax}" y1="14" x2="${ax + 22}" y2="14" stroke="${RENK.hedef}" stroke-width="1.2"/><text x="${ax + 26}" y="18" font-size="11" fill="currentColor">hizmet</text>`)
  ax += 76
  parca.push(`<line x1="${ax}" y1="14" x2="${ax + 22}" y2="14" stroke="#8c959f" stroke-width="1.2" stroke-dasharray="4 3"/><text x="${ax + 26}" y="18" font-size="11" fill="currentColor">girdi (bekler)</text>`)
  ax += 110
  parca.push(`<line x1="${ax}" y1="14" x2="${ax + 22}" y2="14" stroke="${RENK.tamam}" stroke-width="2.6"/><text x="${ax + 26}" y="18" font-size="11" fill="currentColor">bitirdi</text>`)

  // gün sütunları (yerel gece yarısı); boş günler dar, kalabalık günler geniş
  for (const g of olc.gunler) {
    const d = new Date(g.bas)
    parca.push(`<line x1="${g.x}" y1="${UST - 18}" x2="${g.x}" y2="${H - 8}" stroke="#8c959f" stroke-opacity="0.35" stroke-width="1"/>`)
    if (g.w >= 30) parca.push(`<text x="${g.x + 3}" y="${UST - 8}" font-size="10" fill="#8c959f">${String(d.getDate()).padStart(2, '0')}.${String(d.getMonth() + 1).padStart(2, '0')}</text>`)
  }

  // satırlar
  const alanlar = Array.from(new Set(satirlar.map(s => s.alan).filter(Boolean)))
  const konum = new Map<string, { x: number; y: number }>()
  satirlar.forEach((s, i) => {
    const h = yukseklik[i]!
    const y = ustY[i]! + SATIR_Y / 2
    const ton = s.tur === 'hedef' ? '#f6f0ff' : ALAN_TONU[Math.max(0, alanlar.indexOf(s.alan)) % ALAN_TONU.length]
    const seciliSatir = secili === s.anahtar
    parca.push(`<rect x="0" y="${ustY[i]! + 1}" width="${W}" height="${h - 2}" fill="${ton}" fill-opacity="${seciliSatir ? 0.55 : 0.28}"/>`)
    const isaret = s.tur === 'hedef' ? '◆ ' : s.tur === 'oturum' ? '◇ ' : '▣ '
    parca.push(`<text x="6" y="${y + 4}" font-size="11" font-weight="${seciliSatir ? 700 : 500}" fill="currentColor"><title>${kac(s.etiket)}</title>${kac(isaret + kisa(s.etiket, 26))}</text>`)
    if (s.tur === 'seans' && s.bas) {
      const bitis = s.son || (olc.gunler.at(-1)?.son ?? s.bas) - 1
      parca.push(`<rect x="${x(s.bas)}" y="${y - 2}" width="${Math.max(2, x(bitis) - x(s.bas))}" height="4" rx="2" fill="${RENK.seans}" fill-opacity="${s.son ? 0.35 : 0.7}"><title>seans ${kac(s.etiket)}${s.son ? '' : ' (açık)'}</title></rect>`)
      if (s.seans) konum.set(s.seans.id, { x: x(s.bas), y })
    }
    // gün içinde zaman sırasıyla yan yana, sütun sınırında alt sıraya sarar
    for (const [gunBas, grup] of gunlereBol(s.dugumler)) {
      const g = olc.gunler.find(k => k.bas === gunBas)
      if (!g) continue
      const sigan = Math.min(grup.length, olc.sutun)
      const bosluk = Math.max(ADIM, (g.w - 14) / Math.max(1, sigan))
      const bas = grup.length > olc.sutun ? g.x + 7 + R : Math.min(Math.max(x(zaman(grup[0]!)), g.x + R + 3), g.x + g.w - R - 3 - (sigan - 1) * ADIM)
      grup.forEach((n, j) => {
        const sira = Math.floor(j / olc.sutun)
        const kol = j % olc.sutun
        konum.set(n.id, { x: bas + kol * (grup.length > olc.sutun ? bosluk : ADIM), y: y + sira * ADIM })
      })
    }
  })

  // kenarlar: hizmet (mor ince), girdi (kesik), bitirdi (yeşil kalın, bitiren seans satırından)
  for (const k of graf.kenarlar) {
    const a = konum.get(k.k)
    const b = konum.get(k.h)
    if (!a || !b) continue
    if (k.tur === 'hizmet') parca.push(`<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="${RENK.hedef}" stroke-width="1" stroke-opacity="0.55"/>`)
    else if (k.tur === 'girdi') parca.push(`<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="#8c959f" stroke-width="1.2" stroke-dasharray="4 3" stroke-opacity="0.8"/>`)
    else if (k.tur === 'bitirdi') {
      const n = graf.dugumler.find(d => d.id === k.h)
      const bx = n?.bitir_ts ? x(Date.parse(n.bitir_ts)) : b.x
      parca.push(`<path d="M ${bx} ${a.y} Q ${(bx + b.x) / 2} ${(a.y + b.y) / 2 - 10} ${b.x} ${b.y}" fill="none" stroke="${RENK.tamam}" stroke-width="2.4" stroke-opacity="0.6"/>`)
    }
  }

  // düğümler (numara içinde)
  for (const s of satirlar) {
    for (const n of s.dugumler) {
      const p = konum.get(n.id)!
      const no = n.id.split(':')[1] ?? ''
      const sec = secili === n.id
      parca.push(
        `<g><title>${kac(`${n.tur === 'hedef' ? 'hedef' : 'iş'} #${no} · ${n.durum ?? ''} · ${kisa(n.etiket, 120)}`)}</title>` +
          (sec ? `<circle cx="${p.x}" cy="${p.y}" r="${R + 5}" fill="none" stroke="#ffffff" stroke-width="3"/><circle cx="${p.x}" cy="${p.y}" r="${R + 7}" fill="none" stroke="#0969da" stroke-width="2"/>` : '') +
          (n.tur === 'hedef'
            ? `<rect x="${p.x - R}" y="${p.y - R}" width="${2 * R}" height="${2 * R}" rx="3" fill="${dolgu(n)}" transform="rotate(45 ${p.x} ${p.y})"/>`
            : `<circle cx="${p.x}" cy="${p.y}" r="${R}" fill="${dolgu(n)}" stroke="#1f2328" stroke-width="0.6"/>`) +
          `<text x="${p.x}" y="${p.y + 3.5}" font-size="${no.length > 2 ? 7.5 : 9}" font-weight="700" text-anchor="middle" fill="#ffffff">${no}</text></g>`,
      )
    }
  }

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" font-family="ui-sans-serif, system-ui, sans-serif">${parca.join('')}</svg>`
}
