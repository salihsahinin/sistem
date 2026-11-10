// oda.test.tsx: jarvis-oda v0.6 pano ve araç testleri (claude plugin test jarvis/mods/jarvis-oda).
// Bellek-içi motor: fs/process yok; kütük köprüsü sessizce atlanır, pano ve araç akışı sınanır.
import { test, expect, mock } from 'claude-code/testing'

const PANE = { plugin: 'jarvis-oda', surface: 'desktop', component: 'Pane', requestId: 'jarvis-oda' } as const
const PROPS = { title: 'Oda', isFocused: true, bodyColumns: 100, placement: 'dock', scroll: { offset: 0, bodyRows: 40 }, view: {} } as const

const ac = (t: { tool: { call: (a: any) => Promise<any> } }, baslik = 'deneme') => t.tool.call({ tool: 'mcp__jarvis-oda__oda_ac', baslik })

test('oda yokken pano yönlendirme metni gösterir', async ($, on) => {
  mock.store(on)
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  expect((await ui.find({ type: 'Text', text: /Oda yok/ }))?.text).toBeDefined()
  await ui.unmount()
})

test('A2: 20 mesajlık sohbet 12lik pencerede kayar', async ($, on) => {
  mock.store(on)
  mock.session(on)
  await ac($)
  for (let i = 1; i <= 20; i++) await $.tool.call({ tool: 'mcp__jarvis-oda__oda_sohbet', metin: `mesaj ${i}` })
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  expect((await ui.find({ type: 'Text', text: '9–20 / 20' }))).toBeDefined()
  expect(await ui.find({ type: 'Text', text: 'mesaj 20' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: 'mesaj 8' })).toBeUndefined()
  await ui.press({ key: 'gez-sohbet-geri' })
  expect(await ui.find({ type: 'Text', text: '1–12 / 20' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: 'mesaj 1' })).toBeDefined()
  await ui.press({ key: 'gez-sohbet-son' })
  expect(await ui.find({ type: 'Text', text: '9–20 / 20' })).toBeDefined()
  await ui.unmount()
})

test('A3: bölüm başlığı katlar ve açar', async ($, on) => {
  mock.store(on)
  mock.session(on)
  await ac($)
  await $.tool.call({ tool: 'mcp__jarvis-oda__oda_sohbet', metin: 'görünür mü' })
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  expect(await ui.find({ type: 'Text', text: 'görünür mü' })).toBeDefined()
  await ui.press({ key: 'bolum-sohbet' })
  expect(await ui.find({ type: 'Text', text: 'görünür mü' })).toBeUndefined()
  await ui.press({ key: 'bolum-sohbet' })
  expect(await ui.find({ type: 'Text', text: 'görünür mü' })).toBeDefined()
  await ui.unmount()
})

test('A7: uzun mesaj kısaltılır, ▸ tam ile açılır', async ($, on) => {
  mock.store(on)
  mock.session(on)
  await ac($)
  const uzun = 'uzun ' + 'kelime '.repeat(60) + 'SON'
  await $.tool.call({ tool: 'mcp__jarvis-oda__oda_sohbet', metin: uzun })
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  const dugmeler = await ui.findAll({ type: 'Button', text: /▸ tam/ })
  expect(dugmeler.length).toBeGreaterThan(0)
  await ui.press({ key: dugmeler[0]!.key! })
  expect(await ui.find({ type: 'Markdown', text: /SON/ })).toBeDefined()
  await ui.unmount()
})

test('A5: sınıfsız, done-suz ve 5 dosyalı görev reddedilir', async ($, on) => {
  mock.store(on)
  mock.session(on)
  on('session.cwd', () => ({ value: 'C:/depo' }) as any)
  await ac($)
  const r1 = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_gorev_ver', baslik: 'x', emir: 'y', zorluk: 'kolay', done: 'd' })
  expect(String(r1.result)).toMatch(/sinif gerekli/)
  const r2 = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_gorev_ver', baslik: 'x', emir: 'y', zorluk: 'kolay', sinif: 'izole' })
  expect(String(r2.result)).toMatch(/done/)
  const r3 = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_gorev_ver', baslik: 'x', emir: 'y', zorluk: 'kolay', sinif: 'dosyali', done: 'd', dosyalar: ['a', 'b', 'c', 'd', 'e'] })
  expect(String(r3.result)).toMatch(/≤ 4/)
  const r4 = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_gorev_ver', baslik: 'x', emir: 'y', zorluk: 'kolay', sinif: 'rol', done: 'd' })
  expect(String(r4.result)).toMatch(/ajan alanı/)
})

test('A5: dosyali görevde liste dışı Edit reddedilir, listedeki geçer; bütçe sayılır; oda_oku sınıfı gösterir', async ($, on) => {
  const gorev = { id: 1, baslik: 'dosya işi', emir: 'a.txt yaz', zorluk: 'kolay', model: 'haiku', sinif: 'dosyali', done: 'a.txt var', dosyalar: ['C:/depo/a.txt'], butce: 3, cagri: 0, durum: 'kosuyor', agentId: 'a-test', acilis: '2026-11-03T10:00:00Z' }
  const oda = { id: 'oda-t', baslik: 'test', acilis: '2026-11-03T10:00:00Z', maksParalel: 3, turlar: [], gorevler: [gorev], oneriler: [] }
  mock.store(on, { 'oda:aktif': 'oda-t', 'oda:oda-t': oda })
  mock.session(on)
  on('session.cwd', () => ({ value: 'C:/depo' }) as any)
  on('tool.call', () => ({ result: 'çekirdek yanıtı' }) as any)
  const gecen = await $.tool.call({ tool: 'Edit', file_path: 'C:\\depo\\A.TXT', old_string: 'a', new_string: 'b', agentId: 'a-test' })
  expect(JSON.stringify(gecen)).toMatch(/çekirdek/)
  const ret = await $.tool.call({ tool: 'Edit', file_path: 'C:/depo/b.txt', old_string: 'a', new_string: 'b', agentId: 'a-test' })
  expect(String((ret as { deny?: string }).deny ?? (ret as { text?: string }).text)).toMatch(/yazma izni listesinde yok/)
  await $.tool.call({ tool: 'Read', file_path: 'C:/depo/a.txt', agentId: 'a-test' })
  await $.tool.call({ tool: 'Read', file_path: 'C:/depo/a.txt', agentId: 'a-test' })
  const asim = await $.tool.call({ tool: 'Read', file_path: 'C:/depo/a.txt', agentId: 'a-test' })
  expect(String((asim as { deny?: string }).deny ?? (asim as { text?: string }).text)).toMatch(/bütçe aşıldı/)
  const oku = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku' })
  expect(String(oku.result)).toMatch(/\[dosyali\]/)
  expect(String(oku.result)).toMatch(/çağrı 5\/3/)
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  expect(await ui.find({ type: 'Button', key: 'izle-1' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: 'çağrı 5/3' })).toBeDefined()
  await ui.unmount()
})

test('A1: işçi düğmesi ui.view ile işçi transkriptine geçer; izlenirken ana sohbete dön bandı çıkar', async ($, on) => {
  const gorev = { id: 2, baslik: 'izlenen iş', emir: 'e', zorluk: 'orta', model: 'sonnet', sinif: 'izole', done: 'd', butce: 10, cagri: 1, durum: 'kosuyor', agentId: 'a-izle', acilis: '2026-11-03T10:00:00Z' }
  const oda = { id: 'oda-i', baslik: 'izleme', acilis: '2026-11-03T10:00:00Z', maksParalel: 3, turlar: [{ ts: '2026-11-03T10:01:00Z', kim: 'işçi #2', tur: 'rapor', metin: 'ara rapor', gorevId: 2 }], gorevler: [{ id: 1, baslik: 'boş', emir: 'e', zorluk: 'kolay', model: 'haiku', durum: 'bitti', acilis: '2026-11-03T09:00:00Z' }, gorev], oneriler: [] }
  mock.store(on, { 'oda:aktif': 'oda-i', 'oda:oda-i': oda })
  mock.session(on)
  const gorunumler: unknown[] = []
  on('ui.view', (_: unknown, e: unknown) => (gorunumler.push(e), { value: {} }) as any)
  const ui = await $.ui.mount({ ...PANE, props: PROPS })
  await ui.press({ key: 'izle-2' })
  expect(JSON.stringify(gorunumler)).toMatch(/a-izle/)
  const sohbetIsci = await ui.findAll({ type: 'Button', text: /işçi #2/ })
  expect(sohbetIsci.length).toBeGreaterThan(0)
  expect(await ui.find({ type: 'Text', text: /#2 · izlenen iş · izole/ })).toBeDefined()
  await ui.unmount()
  const ui2 = await $.ui.mount({ ...PANE, props: { ...PROPS, view: { agentId: 'a-izle' } } })
  expect(await ui2.find({ type: 'Button', key: 'ana-sohbet' })).toBeDefined()
  await ui2.press({ key: 'ana-sohbet' })
  expect(JSON.stringify(gorunumler.at(-1))).not.toMatch(/a-izle/)
  await ui2.unmount()
})
