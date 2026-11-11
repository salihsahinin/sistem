// kutuk.test.tsx: v0.7 (Karar 130 K52) testleri (claude plugin test jarvis/mods/jarvis-oda).
// Bellek-içi dosya sistemi + sahte durum.exe (ac/al/bitir durum makinesi); gerçek kütüğe dokunmaz.
// Sınanan: işçi başlarken `al`, başarıda `bitir --kanit "oda <id> görev #N"`, hatada iş açık kalır ve neden odaya yazılır;
// oda_oku gorevId=N tam rapor; işçi önerisi anında prompt.submit ile Jarvis'i uyandırır.
import { test, expect, mock } from 'claude-code/testing'

const DEPO = 'C:/depo'
const yol = (p: string) => p.replace(/\\/g, '/')

type Kutuk = { durum: Map<number, string>; cagrilar: string[][] }

function sahteOrtam(on: any, dosyalar: Map<string, string>, kutuk: Kutuk, uyandirma: string[]) {
  on('session.cwd', () => ({ value: DEPO + '/jarvis' }))
  on('fs.exists', (_: unknown, e: { path: string }) => {
    const p = yol(e.path)
    return { value: dosyalar.has(p) || [...dosyalar.keys()].some(k => k.startsWith(p + '/')) }
  })
  on('fs.read', (_: unknown, e: { path: string }) => (dosyalar.has(yol(e.path)) ? { value: dosyalar.get(yol(e.path)) } : { deny: 'ENOENT' }))
  on('fs.write', (_: unknown, e: { path: string; text: string }) => (dosyalar.set(yol(e.path), e.text), { value: undefined }))
  on('fs.list', () => ({ value: [] }))
  on('ui.toast', (_: unknown, e: any) => ({ value: undefined }))
  on('ui.status', () => ({ value: undefined }))
  on('ui.open', () => ({ value: {} }))
  on('agent.list', () => ({ value: [] }))
  on('command.register', () => ({ value: { command: 'oda' } }))
  on('tool.register', () => ({ value: {} }))
  on('session.start', (_: unknown, e: { cwd: string }) => ({ cwd: e.cwd }))
  let ajanNo = 0
  on('agent.spawn', () => ({ agentId: 'a-' + ++ajanNo, model: 'opus' }))
  on('turn.complete', () => ({ text: '' }))
  on('prompt.submit', (_: unknown, e: { text: string }) => (uyandirma.push(e.text), { text: e.text }))
  // Sahte durum.exe: ac → acik, al yalnız acik işi islemde yapar, bitir yalnız islemde işi tamam yapar.
  on('process.run', (_: unknown, e: { argv: readonly string[] }) => {
    const [, komut, idYazi] = e.argv
    kutuk.cagrilar.push([...e.argv.slice(1)])
    const ok = (stdout: string) => ({ value: { exitCode: 0, stdout, stderr: '' } })
    const red = (stderr: string) => ({ value: { exitCode: 1, stdout: '', stderr } })
    if (komut === 'ac') {
      const id = kutuk.durum.size + 1
      kutuk.durum.set(id, 'acik')
      return ok(`#${id} acik jarvis`)
    }
    const id = Number(idYazi)
    if (komut === 'al') return kutuk.durum.get(id) === 'acik' ? (kutuk.durum.set(id, 'islemde'), ok(`#${id} islemde`)) : red(`durum: #${id} al: acik beklenir`)
    if (komut === 'bitir') return kutuk.durum.get(id) === 'islemde' ? (kutuk.durum.set(id, 'tamam'), ok(`#${id} tamam`)) : red(`durum: #${id} bitir: islemde beklenir`)
    return ok('')
  })
}

// Motor agentId'yi hook'a bıraktırmaz; bitiş ve öneri testleri için koşan görev store'a tohumlanır.
const ODA_ID = 'oda-k'
const kosanGorev = { id: 1, baslik: 'koşan iş', emir: 'e', zorluk: 'zor', model: 'opus', sinif: 'izole', done: 'd', butce: 10, cagri: 0, durum: 'kosuyor', agentId: 'a-1', isId: 1, acilis: '2026-11-11T10:00:00Z' }
const tohum = { 'oda:aktif': ODA_ID, ['oda:' + ODA_ID]: { id: ODA_ID, baslik: 'kutuk', acilis: '2026-11-11T10:00:00Z', maksParalel: 3, turlar: [], gorevler: [kosanGorev], oneriler: [] } }
const bekle = () => new Promise(r => setTimeout(r, 20))

async function kur($: any, on: any, tohumla = false) {
  const dosyalar = new Map<string, string>([
    [DEPO + '/ortak/durum-olay.jsonl', ''],
    [DEPO + '/target/release/durum.exe', ''],
  ])
  const kutuk: Kutuk = { durum: new Map(), cagrilar: [] }
  const uyandirma: string[] = []
  mock.store(on, tohumla ? tohum : undefined)
  mock.session(on)
  sahteOrtam(on, dosyalar, kutuk, uyandirma)
  if (tohumla) {
    kutuk.durum.set(1, 'islemde')
    return { kutuk, uyandirma, odaId: ODA_ID }
  }
  await $.tool.call({ tool: 'mcp__jarvis-oda__oda_ac', baslik: 'kutuk' })
  const odaId = JSON.parse(dosyalar.get(DEPO + '/ortak/oda/aktif.json') ?? '{}').odaId as string
  return { kutuk, uyandirma, odaId }
}

const gorev = (baslik: string) => ({ tool: 'mcp__jarvis-oda__oda_gorev_ver', baslik, emir: 'e', zorluk: 'zor', sinif: 'izole', done: 'd' })

test('K52-1: işçi başlarken kütük işi al ile işleme alınır (oturum = oda kimliği)', async ($, on) => {
  const { kutuk, uyandirma, odaId } = await kur($, on)
  const r = await $.tool.call(gorev('başarılı iş'))
  expect(String(r.result)).toMatch(/kütük iş #1/)
  expect(kutuk.cagrilar.some(c => c[0] === 'al' && c[1] === '1' && c.includes('oda-' + odaId))).toBe(true)
  expect(kutuk.durum.get(1)).toBe('islemde')
})

test('K52-1: başarıda bitir; kanıt oda ve görev numarası; bildirimde tamamı ipucu; K52-2 oda_oku gorevId tam rapor', async ($, on) => {
  const { kutuk, uyandirma, odaId } = await kur($, on, true)
  const uzun = 'rapor ' + 'x'.repeat(3000) + ' SON'
  await ($ as any).turn.complete({ agentId: 'a-1', reason: 'answer', answer: uzun, durationMs: 1 })
  expect(kutuk.durum.get(1)).toBe('tamam')
  const bitir = kutuk.cagrilar.find(c => c[0] === 'bitir')!
  expect(bitir[bitir.indexOf('--kanit') + 1]).toBe(`oda ${odaId} görev #1`)
  await bekle()
  expect(uyandirma.join('\n')).toMatch(/tamamı: oda_oku gorevId=1/)
  expect(uyandirma.join('\n')).toMatch(/kütük iş #1 kapandı/)
  // K52-2: gorevId verilince rapor kesilmez.
  const tam = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku', gorevId: 1 })
  expect(String(tam.result)).toContain(uzun)
  const ozet = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku' })
  expect(String(ozet.result)).not.toContain(' SON')
  expect(String(ozet.result)).toMatch(/tamamı: oda_oku gorevId=1/)
  expect(String(ozet.result)).toMatch(/kütük: kütük iş #1 kapandı/)
})

test('K52-1: hata ve bütçe aşımında kütük işi açık kalır, neden odaya yazılır', async ($, on) => {
  const { kutuk } = await kur($, on, true)
  await ($ as any).turn.complete({ agentId: 'a-1', reason: 'error', answer: '', text: 'API hatası', durationMs: 1 })
  expect(kutuk.cagrilar.some(c => c[0] === 'bitir')).toBe(false)
  expect(kutuk.durum.get(1)).toBe('islemde')
  const oku = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku', gorevId: 1 })
  expect(String(oku.result)).toMatch(/kütük iş #1 açık kaldı: işçi hatayla bitti \(error\)/)
  const yok = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku', gorevId: 9 })
  expect(String(yok.result)).toMatch(/#9 bu odada yok/)
})

test('K52-3: işçi önerisi geldiği anda Jarvis uyanır', async ($, on) => {
  const saat = mock.clock(on, { now: Date.parse('2026-11-11T12:00:00Z') })
  const { uyandirma } = await kur($, on, true)
  await ($ as any).session.start({ cwd: DEPO + '/jarvis', surface: 'desktop', isInteractive: true, source: 'startup' })
  const once = uyandirma.length
  const r = await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oneri', metin: 'B yolunu seç', gerekce: 'daha ucuz', agentId: 'a-1' })
  expect(String(r.result)).toMatch(/Ö1 kaydedildi/)
  await saat.advance(3100)
  await bekle()
  expect(uyandirma.length).toBe(once + 1)
  expect(uyandirma.at(-1)).toMatch(/^\[oda\] öneri #1 \(görev #1\): B yolunu seç/)
})
