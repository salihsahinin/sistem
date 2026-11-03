// dis.test.tsx: C1 stigmerjik dış kanal testi (claude plugin test jarvis/mods/jarvis-oda).
// Bellek-içi dosya sistemi; aynı test oturumu hem ev sahibi hem dış oturum rolündedir (kanal yalnız dosyadır).
import { test, expect, mock } from 'claude-code/testing'

const DEPO = 'C:/depo'
const yol = (p: string) => p.replace(/\\/g, '/')

function sahteFs(on: any, dosyalar: Map<string, string>) {
  on('session.cwd', () => ({ value: DEPO + '/jarvis' }))
  on('fs.exists', (_: unknown, e: { path: string }) => {
    const p = yol(e.path)
    return { value: dosyalar.has(p) || [...dosyalar.keys()].some(k => k.startsWith(p + '/')) }
  })
  on('fs.read', (_: unknown, e: { path: string }) => (dosyalar.has(yol(e.path)) ? { value: dosyalar.get(yol(e.path)) } : { deny: 'ENOENT' }))
  on('fs.write', (_: unknown, e: { path: string; text: string }) => (dosyalar.set(yol(e.path), e.text), { value: undefined }))
  on('fs.list', (_: unknown, e: { path: string }) => {
    const p = yol(e.path) + '/'
    const adlar = new Set([...dosyalar.keys()].filter(k => k.startsWith(p)).map(k => k.slice(p.length).split('/')[0]!))
    return { value: [...adlar].map(name => ({ name, kind: 'file', size: 0, mtimeMs: 0, isLink: false })) }
  })
  on('ui.toast', () => ({ value: undefined }))
  on('ui.status', () => ({ value: undefined }))
  on('ui.open', () => ({ value: {} }))
  on('agent.list', () => ({ value: [] }))
  on('command.register', () => ({ value: { command: 'oda' } }))
  on('tool.register', () => ({ value: {} }))
  on('session.start', (_: unknown, e: { cwd: string }) => ({ cwd: e.cwd }))
  on('process.run', () => ({ value: { exitCode: 1, stdout: '', stderr: 'test' } }))
}

const PANE = { plugin: 'jarvis-oda', surface: 'desktop', component: 'Pane', requestId: 'jarvis-oda' } as const
const PROPS = { title: 'Oda', isFocused: true, bodyColumns: 100, placement: 'dock', scroll: { offset: 0, bodyRows: 40 }, view: {} } as const

test('C1: dış oturum katılır, rapor dosyadan odaya düşer; @hedefli mesaj giden.jsonl ile dış oturuma iner', async ($, on) => {
  const dosyalar = new Map<string, string>([[DEPO + '/ortak/durum-olay.jsonl', '']])
  mock.store(on)
  const oturum = mock.session(on)
  const saat = mock.clock(on, { now: Date.parse('2026-11-03T12:00:00Z') })
  sahteFs(on, dosyalar)
  const uyandirma: string[] = []
  on('prompt.submit', (_: unknown, e: { text: string }) => (uyandirma.push(e.text), { text: e.text }))
  await ($ as any).session.start({ cwd: DEPO + '/jarvis', surface: 'desktop', isInteractive: true, source: 'startup' })

  await $.tool.call({ tool: 'mcp__jarvis-oda__oda_ac', baslik: 'dis kanal' })
  const aktif = JSON.parse(dosyalar.get(DEPO + '/ortak/oda/aktif.json') ?? '{}') as { odaId?: string }
  expect(aktif.odaId).toBeDefined()

  const k = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_katil', oturum: 'Claude Mods', rol: 'mod öğrenme sekmesi', dosyalar: ['span/notlar.md'] })
  expect(String(k.result)).toMatch(/oturum claude-mods/)
  const m = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_mesaj', tur: 'rapor', metin: 'Ders 3 bitti' })
  expect(String(m.result)).toMatch(/rapor düştü/)
  expect(dosyalar.get(`${DEPO}/ortak/oda/${aktif.odaId}/gelen-claude-mods.jsonl`)).toMatch(/Ders 3 bitti/)

  await saat.advance(3100)
  const oku = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku' })
  expect(String(oku.result)).toMatch(/◆ oturum claude-mods \[katıldı\]/)
  expect(String(oku.result)).toMatch(/oturum claude-mods \[rapor\]: Ders 3 bitti/)

  expect(uyandirma.join('\n')).toMatch(/\[oda dış\] oturum claude-mods \[rapor\]: Ders 3 bitti/)

  const s = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_sohbet', metin: 'teşekkürler, ders 4', hedef: '@claude-mods' })
  expect(String(s.result)).toMatch(/SendMessage/)
  expect(dosyalar.get(`${DEPO}/ortak/oda/${aktif.odaId}/giden.jsonl`)).toMatch(/"hedef":"claude-mods"/)
  await saat.advance(3100)
  expect(JSON.stringify(oturum.appended())).toMatch(/\[oda\] jarvis: teşekkürler, ders 4/)

  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  expect(await ui.find({ type: 'Text', text: 'oturum claude-mods' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /◆ oturum claude-mods/ })).toBeDefined()
  await ui.unmount()

  await $.tool.call({ tool: 'mcp__jarvis-oda__oda_katil', ayril: true })
  await saat.advance(3100)
  const son = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku' })
  expect(String(son.result)).toMatch(/oturum claude-mods \[ayrıldı\]/)
})
