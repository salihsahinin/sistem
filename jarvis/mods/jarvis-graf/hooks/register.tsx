// jarvis-graf — akış grafı paneli (Salih 2026-10-27; Karar 122/124/125 grafı).
// ortak/akis-graf.json okunur; masaüstünde SVG (bantlar: hedef · iş · seans,
// x = açılış sırası, dolgu = durum), terminalde metin listesi. Düğüm seçimi
// listeden; detay panelde. HTML üretici ve D2 yenileme düğmeleri.
import { atom, read, update } from 'claude-code'
import type { Register, EngineInterface } from 'claude-code'

import type { Graf, GrafDugum, GrafGorunum } from '../types'

const PANE = 'jarvis-graf'
const grafAtom = atom({ plugin: 'jarvis-graf', key: 'graf' } as const, null as Graf | null)
const gorunumAtom = atom({ plugin: 'jarvis-graf', key: 'gorunum' } as const, {
  alan: 'jarvis',
  yalnizAcik: false,
  secili: null,
  yol: '',
  mtimeMs: 0,
  hata: null,
} as GrafGorunum)

function kisa(m: string | null | undefined, n = 80): string {
  const t = (m ?? '').replace(/\s+/g, ' ').trim()
  return t.length > n ? t.slice(0, n - 1) + '…' : t
}

function zaman(n: GrafDugum): number {
  const t = n.acilis_ts ?? n.ac_ts ?? ''
  const ms = Date.parse(t)
  return Number.isFinite(ms) ? ms : 0
}

async function yolBul($: EngineInterface): Promise<{ graf: string; jarvis: string; depo: string } | null> {
  const cwd = (await $.session.cwd()).replace(/\\/g, '/')
  const adaylar = [
    { depo: cwd, jarvis: cwd + '/jarvis' },
    { depo: cwd.replace(/\/[^/]+$/, ''), jarvis: cwd },
  ]
  for (const a of adaylar) {
    const graf = a.depo + '/ortak/akis-graf.json'
    if (await $.fs.exists(graf)) return { graf, jarvis: a.jarvis, depo: a.depo }
  }
  return null
}

async function grafYukle($: EngineInterface, zorla = false): Promise<void> {
  const yol = await yolBul($)
  if (!yol) {
    await update($, gorunumAtom, g => ({ ...g, hata: 'ortak/akis-graf.json bulunamadı (cwd depo ya da jarvis/ olmalı)' }))
    return
  }
  const st = await $.fs.stat(yol.graf)
  const g = await read($, gorunumAtom)
  if (!zorla && g.mtimeMs === st.mtimeMs && g.yol === yol.graf) return
  try {
    const graf = JSON.parse(await $.fs.read(yol.graf)) as Graf
    await update($, grafAtom, () => graf)
    await update($, gorunumAtom, x => ({ ...x, yol: yol.graf, mtimeMs: st.mtimeMs, hata: null }))
    const acik = graf.dugumler.filter(n => n.tur === 'is' && (n.durum === 'acik' || n.durum === 'islemde')).length
    $.ui.status(`graf: ${graf.dugumler.length} düğüm · ${acik} açık iş`)
  } catch (err) {
    await update($, gorunumAtom, x => ({ ...x, hata: 'JSON okunamadı: ' + String(err) }))
  }
}

function dolgu(n: GrafDugum): string {
  if (n.tur === 'seans') return n.kapat_ts ? '#8a8a8a' : '#e3b341'
  if (n.tur === 'hedef') return '#6f42c1'
  switch (n.durum) {
    case 'tamam':
      return '#2da44e'
    case 'islemde':
      return '#e3b341'
    case 'bayat':
      return '#6e6e6e'
    default:
      return '#cf222e'
  }
}

function svgCiz(graf: Graf, gor: GrafGorunum, genislikPx: number): string {
  const dugumler = graf.dugumler
    .filter(n => gor.alan === 'tum' || n.alan === gor.alan || n.tur === 'seans')
    .filter(n => !gor.yalnizAcik || n.tur !== 'is' || n.durum === 'acik' || n.durum === 'islemde')
    .sort((a, b) => zaman(a) - zaman(b))
  const bantlar: { hedef: GrafDugum[]; is: GrafDugum[]; seans: GrafDugum[] } = { hedef: [], is: [], seans: [] }
  for (const n of dugumler) bantlar[n.tur].push(n)
  const W = Math.max(320, genislikPx)
  const solBosluk = 44
  const adim = Math.max(10, Math.min(28, (W - solBosluk - 10) / Math.max(1, dugumler.length)))
  const r = Math.max(3, Math.min(7, adim / 2 - 1))
  const satirAlt = 3 // iş bandı alt-satır sayısı (çakışmayı azaltır)
  const y: { hedef: number; is: number; seans: number } = { hedef: 18, is: 48, seans: 48 + satirAlt * 16 + 20 }
  const H = y.seans + 20
  const konum = new Map<string, { x: number; y: number }>()
  dugumler.forEach((n, i) => {
    const x = solBosluk + i * adim + r
    const yy = n.tur === 'is' ? y.is + (bantlar.is.indexOf(n) % satirAlt) * 16 : y[n.tur]
    konum.set(n.id, { x, y: yy })
  })
  const kenarlar = graf.kenarlar
    .filter(e => konum.has(e.k) && konum.has(e.h))
    .map(e => {
      const a = konum.get(e.k)!
      const b = konum.get(e.h)!
      const renk = e.tur === 'hizmet' ? '#6f42c1' : e.tur === 'bitirdi' ? '#2da44e' : e.tur === 'sonra' ? '#8a8a8a' : '#9a9a9a'
      const dash = e.tur === 'girdi' ? ' stroke-dasharray="3 2"' : ''
      return `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="${renk}" stroke-width="0.8" opacity="0.55"${dash}/>`
    })
  const daireler = dugumler.map(n => {
    const p = konum.get(n.id)!
    const secili = gor.secili === n.id
    const no = n.id.split(':')[1] ?? ''
    const etiket = n.tur === 'is' ? no : n.tur === 'seans' ? kisa(n.etiket.replace(/^2026-/, ''), 11) : 'H' + no
    return (
      `<g><title>${n.id} · ${kisa(n.etiket, 90).replace(/[<>&"]/g, c => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;' })[c] ?? c)}</title>` +
      `<circle cx="${p.x}" cy="${p.y}" r="${secili ? r + 2 : r}" fill="${dolgu(n)}" stroke="${secili ? '#ffffff' : '#222'}" stroke-width="${secili ? 2 : 0.6}"/>` +
      (n.tur !== 'is' || r >= 5 ? `<text x="${p.x}" y="${p.y + r + 8}" font-size="6" text-anchor="middle" fill="#888">${etiket}</text>` : '') +
      `</g>`
    )
  })
  const bantEtiket = (ad: string, yy: number) => `<text x="2" y="${yy + 3}" font-size="8" fill="#888">${ad}</text>`
  return (
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" font-family="ui-sans-serif, system-ui">` +
    bantEtiket('hedef', y.hedef) +
    bantEtiket('iş', y.is + 16) +
    bantEtiket('seans', y.seans) +
    kenarlar.join('') +
    daireler.join('') +
    `</svg>`
  )
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'graf', description: 'Akış grafı panelini açar (ortak/akis-graf.json).' })
    await grafYukle($, true)
    void $.ui.open({ id: PANE, title: 'Akış grafı' })
    $.clock.every(10000, () => grafYukle($))
    return next(e)
  })

  on('command.run', { command: 'graf' }, async $ => {
    await grafYukle($, true)
    await $.ui.open({ id: PANE, title: 'Akış grafı', focus: true })
    const graf = await read($, grafAtom)
    if (!graf) return { text: 'Graf okunamadı.' }
    const acik = graf.dugumler.filter(n => n.tur === 'is' && (n.durum === 'acik' || n.durum === 'islemde'))
    return { text: `Akış grafı paneli açık: ${graf.dugumler.length} düğüm, ${graf.kenarlar.length} kenar, ${acik.length} açık iş.` }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const graf = await read($, grafAtom)
    const gor = await read($, gorunumAtom)
    const { Box, Text, Button } = $.ui.resolve(e)
    const sutun = (e.props as { bodyColumns?: number }).bodyColumns ?? e.viewport?.columns ?? 80

    const ayar = (fn: (g: GrafGorunum) => GrafGorunum) => () => update($, gorunumAtom, fn)
    const htmlAc = async () => {
      const yol = await yolBul($)
      if (!yol) return
      const r = await $.process.run(['python3', 'tools/akis-graf-html.py'], { cwd: yol.jarvis, timeoutMs: 60000 })
      const cikti = r.stdout.trim().split(/\r?\n/).pop() ?? ''
      if (r.exitCode === 0 && cikti) {
        await $.process.run(['cmd', '/c', 'start', '', cikti], { cwd: yol.jarvis })
        $.ui.toast('Graf HTML açıldı: ' + cikti)
      } else $.ui.toast('HTML üretilemedi: ' + kisa(r.stderr, 120))
    }
    const d2Yenile = async () => {
      const yol = await yolBul($)
      if (!yol) return
      const r = await $.process.run([yol.depo + '/target/release/durum.exe', 'graf', '--alan', gor.alan === 'tum' ? 'jarvis' : gor.alan], { cwd: yol.depo, timeoutMs: 60000 })
      $.ui.toast(r.exitCode === 0 ? 'durum graf koştu; JSON + D2 tazelendi' : 'durum graf hata: ' + kisa(r.stderr, 120))
      await grafYukle($, true)
    }

    if (!graf) {
      return (
        <Box flexDirection="column" padding={1}>
          <Text bold>Akış grafı</Text>
          <Text color="red">{gor.hata ?? 'Henüz yüklenmedi.'}</Text>
          <Button key="yenile" onPress={() => grafYukle($, true)}>
            Yenile
          </Button>
        </Box>
      )
    }

    const gorunen = graf.dugumler
      .filter(n => gor.alan === 'tum' || n.alan === gor.alan || n.tur === 'seans')
      .filter(n => !gor.yalnizAcik || n.tur !== 'is' || n.durum === 'acik' || n.durum === 'islemde')
    const isler = gorunen.filter(n => n.tur === 'is').sort((a, b) => zaman(b) - zaman(a))
    const secili = gor.secili ? graf.dugumler.find(n => n.id === gor.secili) ?? null : null
    const seciliKenarlar = secili ? graf.kenarlar.filter(k => k.k === secili.id || k.h === secili.id) : []
    const etiketi = (id: string) => kisa(graf.dugumler.find(n => n.id === id)?.etiket ?? id, 50)
    const alanlar = Array.from(new Set(graf.dugumler.map(n => n.alan).filter(Boolean)))

    const resim =
      e.surface === 'desktop' || e.surface === 'mobile' || e.surface === 'vscode'
        ? (() => {
            const { Svg } = $.ui.resolve(e)
            const px = Math.max(320, Math.min(1400, sutun * 8))
            return <Svg source={svgCiz(graf, gor, px)} alt={`Akış grafı: ${gorunen.length} düğüm; bantlar hedef, iş, seans; x = açılış sırası`} width={px} isInteractive />
          })()
        : null

    return (
      <Box flexDirection="column" padding={1} gap={1}>
        <Box flexDirection="row" justifyContent="space-between" flexWrap="wrap" gap={1}>
          <Text bold>
            Akış grafı <Text dimColor>· {String(graf.meta.tarih ?? '')} · {gorunen.length}/{graf.dugumler.length} düğüm</Text>
          </Text>
          <Box flexDirection="row" gap={1}>
            <Button key="yenile" plain onPress={() => grafYukle($, true)}>
              ⟳ yenile
            </Button>
            <Button key="html" plain onPress={htmlAc}>
              HTML aç
            </Button>
            <Button key="d2" plain onPress={d2Yenile}>
              durum graf
            </Button>
          </Box>
        </Box>
        <Box flexDirection="row" gap={1} flexWrap="wrap">
          {['tum', ...alanlar].map(a => (
            <Button key={'alan-' + a} plain dimColor={gor.alan !== a} onPress={ayar(g => ({ ...g, alan: a }))}>
              {gor.alan === a ? '[' + a + ']' : a}
            </Button>
          ))}
          <Button key="acik" plain dimColor={!gor.yalnizAcik} onPress={ayar(g => ({ ...g, yalnizAcik: !g.yalnizAcik }))}>
            {gor.yalnizAcik ? '[yalnız açık]' : 'yalnız açık'}
          </Button>
        </Box>
        {resim}
        {gor.hata && <Text color="red">{gor.hata}</Text>}
        {secili && (
          <Box flexDirection="column" borderStyle="round" paddingX={1}>
            <Text bold>
              {secili.id} <Text dimColor>· {secili.tur} · {secili.alan} · {secili.durum ?? (secili.kapat_ts ? 'kapandı' : 'açık')}</Text>
            </Text>
            <Text>{kisa(secili.etiket, 300)}</Text>
            {secili.sonraki_eylem && <Text dimColor>sonraki: {kisa(secili.sonraki_eylem, 300)}</Text>}
            {secili.hedef && <Text dimColor>hedef: {kisa(secili.hedef, 300)}</Text>}
            {seciliKenarlar.slice(0, 12).map(k => (
              <Text dimColor>
                {k.k === secili.id ? '→ ' : '← '}
                {k.tur} {etiketi(k.k === secili.id ? k.h : k.k)}
              </Text>
            ))}
            <Button key="kapat" plain onPress={ayar(g => ({ ...g, secili: null }))}>
              kapat
            </Button>
          </Box>
        )}
        <Box flexDirection="column">
          <Text bold dimColor>
            İşler ({isler.length}) · seçmek için tıkla
          </Text>
          {isler.slice(0, 40).map(n => (
            <Button key={'sec-' + n.id} plain dimColor={n.durum === 'tamam' || n.durum === 'bayat'} onPress={ayar(g => ({ ...g, secili: n.id }))}>
              {n.durum === 'tamam' ? '✓' : n.durum === 'islemde' ? '●' : n.durum === 'bayat' ? '·' : '○'} #{n.id.split(':')[1]} {kisa(n.etiket, Math.max(30, sutun - 12))}
            </Button>
          ))}
        </Box>
      </Box>
    )
  })
}
