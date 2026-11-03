// graf.test.tsx: jarvis-graf v0.2 testleri (claude plugin test jarvis/mods/jarvis-graf).
// Bellek-içi motor: dosya sistemi ve süreç olayları sentetik bir depoyla alt katmandan yanıtlanır.
import { test, expect, mock } from 'claude-code/testing'
import { satirlar } from '../hooks/src/metin'
import { argumandanId } from '../hooks/src/araclar'

const DEPO = 'C:/depo'
const GRAF = {
  meta: { tarih: '2026-11-03' },
  dugumler: [
    { id: 'seans:s1', tur: 'seans', alan: 'jarvis', etiket: '2026-11-01-jarvis', ac_ts: '2026-11-01T09:00:00Z', kapat_ts: '2026-11-01T18:00:00Z', hedef: 'grafı kur', hedef_tutuldu: true, kayit: 'jarvis/raporlar/seans/s1.json' },
    { id: 'seans:s2', tur: 'seans', alan: 'jarvis', etiket: '2026-11-02-jarvis', ac_ts: '2026-11-02T09:00:00Z', kapat_ts: null },
    { id: 'is:1', tur: 'hedef', alan: 'jarvis', etiket: 'Karar 125 hedefi: graf içinde graf', durum: 'acik', acilis_ts: '2026-11-01T09:10:00Z', oturumlar: ['2026-11-01-jarvis'] },
    { id: 'is:2', tur: 'is', alan: 'jarvis', etiket: 'seans şeritli çizim', durum: 'tamam', sonraki_eylem: 'SVG yaz', acilis_ts: '2026-11-01T10:00:00Z', bitir_ts: '2026-11-02T11:00:00Z', oturumlar: ['2026-11-01-jarvis', '2026-11-02-jarvis'] },
    { id: 'is:3', tur: 'is', alan: 'jarvis', etiket: 'detay paneli', durum: 'acik', sonraki_eylem: 'kütük olayları', acilis_ts: '2026-11-02T10:00:00Z', oturumlar: ['2026-11-02-jarvis'] },
    { id: 'is:4', tur: 'is', alan: 'jarvis', etiket: 'oda #1 köprü testi', durum: 'acik', sonraki_eylem: 'test', acilis_ts: '2026-11-02T12:00:00Z', oturumlar: ['oda-202611021200-x'] },
  ],
  kenarlar: [
    { k: 'seans:s1', h: 'seans:s2', tur: 'sonra' },
    { k: 'seans:s1', h: 'is:1', tur: 'acti' },
    { k: 'seans:s1', h: 'is:2', tur: 'acti' },
    { k: 'seans:s2', h: 'is:3', tur: 'acti' },
    { k: 'seans:s2', h: 'is:2', tur: 'bitirdi' },
    { k: 'is:2', h: 'is:1', tur: 'hizmet' },
    { k: 'is:2', h: 'is:3', tur: 'girdi' },
  ],
}
const OLAYLAR = [
  { olay: 'ac', id: 2, ts: '2026-11-01T10:00:00Z', alan: 'jarvis', is: 'seans şeritli çizim', oturum: '2026-11-01-jarvis' },
  { olay: 'bitir', id: 2, ts: '2026-11-02T11:00:00Z', oturum: '2026-11-02-jarvis', kanit: ['commit abc123'] },
]
const DOSYALAR: Record<string, string> = {
  [DEPO + '/ortak/akis-graf.json']: JSON.stringify(GRAF),
  [DEPO + '/ortak/durum-olay.jsonl']: OLAYLAR.map(o => JSON.stringify(o)).join('\n'),
  [DEPO + '/jarvis/kuyruk/senaryo-defteri.md']: 'giriş\n\n**Karar 125 (Salih 2026-10-26):** graflar altında graflar.\n\n**Karar 126:** başka.',
}

/** Motor yolları ters bölüyle iletir; sentetik depo / ile anahtarlanır. */
const yol = (p: string) => p.replace(/\\/g, '/')

function sahteDepo(on: any, surec: { argv: readonly string[] }[] = [], cevap?: (argv: readonly string[]) => { exitCode: number; stdout: string; stderr: string }) {
  mock.store(on)
  mock.session(on)
  on('session.cwd', () => ({ value: DEPO + '/jarvis/mods' }))
  on('fs.exists', (_: unknown, e: { path: string }) => ({ value: yol(e.path) in DOSYALAR }))
  on('fs.stat', (_: unknown, e: { path: string }) => (yol(e.path) in DOSYALAR ? { value: { kind: 'file', size: DOSYALAR[yol(e.path)]!.length, mtimeMs: 1, isLink: false } } : { deny: 'ENOENT' }))
  on('fs.read', (_: unknown, e: { path: string }) => (yol(e.path) in DOSYALAR ? { value: DOSYALAR[yol(e.path)] } : { deny: 'ENOENT' }))
  on('ui.open', () => ({ value: {} }))
  on('ui.toast', () => ({ value: undefined }))
  on('ui.status', () => ({ value: undefined }))
  on('process.run', (_: unknown, e: { argv: readonly string[] }) => {
    surec.push({ argv: e.argv })
    return { value: cevap ? cevap(e.argv) : { exitCode: 1, stdout: '', stderr: 'yok' } }
  })
}

const PANE = { plugin: 'jarvis-graf', surface: 'desktop', component: 'Pane', requestId: 'jarvis-graf' } as const
const PROPS = { title: 'Akış grafı', isFocused: true, bodyColumns: 120, placement: 'dock', scroll: { offset: 0, bodyRows: 60 }, view: {} } as const

test('B1/B2 satır düzeni: hedef şeridi üstte, iş açan seansın satırında, seanssız iş oturum satırında', () => {
  const sat = satirlar(GRAF as any, { alan: 'tum', yalnizAcik: false } as any)
  expect(sat.map(s => s.anahtar)).toEqual(['hedefler', 'seans:s1', 'seans:s2', 'oturum:oda-202611021200-x'])
  expect(sat[1]!.dugumler.map(d => d.id)).toEqual(['is:2'])
  expect(sat[3]!.dugumler.map(d => d.id)).toEqual(['is:4'])
  expect(argumandanId('is:7')).toBe('is:7')
  expect(argumandanId('#7')).toBe('is:7')
  expect(argumandanId('seans:x')).toBe('seans:x')
  expect(argumandanId('')).toBeNull()
})

test('B5 + B3: /graf is:2 seçer; detayda olaylar, kanıt, bağlar, karar paragrafı; ızgaradan seans seçilir', async ($, on) => {
  sahteDepo(on)
  await $.command.run({ command: 'graf', args: 'is:2' } as any)
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  expect(await ui.find({ type: 'Svg' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /iş #2/ })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /Kütük olayları \(2\)/ })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /commit abc123/ })).toBeDefined()
  expect(await ui.find({ type: 'Button', text: /önünü açar: #3 detay paneli/ })).toBeDefined()
  expect(await ui.find({ type: 'Button', text: /hizmet eder \(hedef\): #1/ })).toBeDefined()
  expect(await ui.find({ type: 'Button', text: /bitiren seans: 2026-11-02-jarvis/ })).toBeDefined()
  await ui.press({ key: 'sec-seans:s1' })
  expect(await ui.find({ type: 'Text', text: 'seans 2026-11-01-jarvis' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: /seans teslim kaydı/ })).toBeDefined()
  expect(await ui.find({ type: 'Button', key: 'kayit-ac' })).toBeDefined()
  await ui.press({ key: 'sec-is:1' })
  expect(await ui.find({ type: 'Markdown', text: /graflar altında graflar/ })).toBeDefined()
  await ui.press({ key: 'sec-oturum:oda-202611021200-x' })
  expect(await ui.find({ type: 'Text', text: 'oturum oda-202611021200-x' })).toBeDefined()
  await ui.unmount()
})

test('B4: HTML aç py -3 ile üretir, otomatik açılamazsa aç · kopyala · Explorer düğmeleri ve hata metni kalır', async ($, on) => {
  const surec: { argv: readonly string[] }[] = []
  sahteDepo(on, surec, argv => (argv[0] === 'py' ? { exitCode: 0, stdout: 'uyarı\nC:\\depo\\jarvis\\raporlar\\2026-11\\graf ö.html\n', stderr: '' } : { exitCode: 1, stdout: '', stderr: 'açılamadı' }))
  await $.command.run({ command: 'graf', args: '' } as any)
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  await ui.press({ key: 'html' })
  expect(surec[0]!.argv.slice(0, 3)).toEqual(['py', '-3', 'tools/akis-graf-html.py'])
  expect(surec[1]!.argv[0]).toBe('powershell')
  expect(surec[1]!.argv.at(-1)).toContain('graf ö.html')
  expect(await ui.find({ type: 'Text', text: /HTML: graf ö.html/ })).toBeDefined()
  await ui.press({ key: 'html-dosya-explorer' })
  expect(surec.at(-1)!.argv[0]).toBe('explorer.exe')
  expect(surec.at(-1)!.argv[1]).toContain('graf ö.html')
  expect(await ui.find({ type: 'Text', text: /Otomatik açılamadı/ })).toBeDefined()
  await ui.unmount()
})

test('B4: hiçbir python yoksa üç deneme pane hata metninde görünür', async ($, on) => {
  sahteDepo(on)
  await $.command.run({ command: 'graf', args: '' } as any)
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  await ui.press({ key: 'html' })
  expect(await ui.find({ type: 'Text', text: /HTML üretilemedi.*py -3.*python.*python3/ })).toBeDefined()
  await ui.unmount()
})
