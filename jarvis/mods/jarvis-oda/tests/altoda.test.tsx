// altoda.test.tsx: v0.8 alt-oda (Karar 130 B9) testleri (claude plugin test jarvis/mods/jarvis-oda).
// Bellek-içi dosya sistemi + sahte agent.spawn (prompt kaydı) + işçi bitişi turn.complete ile sürülür.
// Test motoru sahte spawn'ın agentId'sini moda geçirmez (core alanı); bu yüzden bitiş testleri alt-odayı ilgili aşamada,
// koşan görevleri bilinen agentId ile store'a tohumlar (kutuk.test.tsx ile aynı yol).
// Kütük: test motoru süreç koşturmaz (yalnız "claude-code" içe aktarılır); durum.exe'nin ac/al/bitir kuralları sahte kütükte
// aynen kurulur (al yalnız acik, bitir yalnız islemde; hedef de al ister). Aynı argv dizisi gerçek durum.exe'de --kutuk ile denendi.
// Sınanan: (a) tur 1 bağımsızlık, (b) tur 2 girdisinde diğerlerinin tur 1 metni, (c) ortak çıktıda ajan metni bayt düzeyinde aynı,
// (d) şema dışı alan ve uzunluk sınırı reddi, (e) kütükte hedef + iş açılıp kanıtla kapanır, (5) paralel sınır ve rol bütçesi.
import { test, expect, mock } from 'claude-code/testing'

import { ALT_ODA_ARACI } from '../hooks/src/altoda'

const DEPO = 'C:/depo'
const yol = (p: string) => p.replace(/\\/g, '/')
type KutukKaydi = { id: number; durum: string; tur?: string; hedef?: number; oturum?: string; is?: string; kanit?: string[]; sira: string[] }
type Spawn = { prompt: string; subagentType?: string; agentId: string }
type Ortam = { dosyalar: Map<string, string>; spawnlar: Spawn[]; uyandirma: string[]; kutukCagri: string[][]; kutuk: Map<number, KutukKaydi> }

function sahteOrtam(on: any, o: Ortam, kutukAcik: boolean) {
  on('session.cwd', () => ({ value: DEPO + '/jarvis' }))
  on('fs.exists', (_: unknown, e: { path: string }) => {
    const p = yol(e.path)
    return { value: o.dosyalar.has(p) || [...o.dosyalar.keys()].some(k => k.startsWith(p + '/')) }
  })
  on('fs.read', (_: unknown, e: { path: string }) => (o.dosyalar.has(yol(e.path)) ? { value: o.dosyalar.get(yol(e.path)) } : { deny: 'ENOENT' }))
  on('fs.write', (_: unknown, e: { path: string; text: string }) => (o.dosyalar.set(yol(e.path), e.text), { value: undefined }))
  on('fs.list', () => ({ value: [] }))
  on('ui.toast', () => ({ value: undefined }))
  on('ui.status', () => ({ value: undefined }))
  on('ui.open', () => ({ value: {} }))
  on('agent.list', () => ({ value: [] }))
  let no = 100
  on('agent.spawn', (_: unknown, e: { prompt: string; subagentType?: string; subagent_type?: string }) => {
    const agentId = 'a-' + ++no
    // Test motoru spawn'ı Agent aracı girdisi olarak iletir (subagent_type).
    o.spawnlar.push({ prompt: e.prompt, subagentType: e.subagentType ?? e.subagent_type, agentId })
    return { agentId, model: 'sonnet' }
  })
  on('turn.complete', () => ({ text: '' }))
  on('prompt.submit', (_: unknown, e: { text: string }) => (o.uyandirma.push(e.text), { text: e.text }))
  // Sahte durum.exe: ac → acik (--tur, --hedef, --oturum kaydı); al yalnız acik → islemde; bitir yalnız islemde → tamam.
  on('process.run', (_: unknown, e: { argv: readonly string[] }) => {
    const argv = [...e.argv.slice(1)]
    o.kutukCagri.push(argv)
    const ok = (stdout: string) => ({ value: { exitCode: 0, stdout, stderr: '' } })
    const red = (stderr: string) => ({ value: { exitCode: 1, stdout: '', stderr } })
    if (!kutukAcik) return ok('')
    const bayrak = (b: string) => (argv.includes(b) ? argv[argv.indexOf(b) + 1] : undefined)
    const [komut, idYazi] = argv
    if (komut === 'ac') {
      const id = o.kutuk.size + 1
      const h = bayrak('--hedef')
      o.kutuk.set(id, { id, durum: 'acik', tur: bayrak('--tur'), ...(h ? { hedef: Number(h) } : {}), oturum: bayrak('--oturum'), is: bayrak('--is'), sira: ['ac'] })
      return ok(`#${id} acik jarvis`)
    }
    const k = o.kutuk.get(Number(idYazi))
    if (komut === 'al') return k?.durum === 'acik' ? ((k.durum = 'islemde'), k.sira.push('al'), ok(`#${k.id} islemde`)) : red(`durum: #${idYazi} al: acik beklenir`)
    if (komut === 'bitir') {
      if (k?.durum !== 'islemde') return red(`durum: #${idYazi} bitir: durum ${k?.durum} (islemde beklenir)`)
      k.durum = 'tamam'
      k.kanit = [bayrak('--kanit') ?? '']
      k.sira.push('bitir')
      return ok(`#${k.id} tamam`)
    }
    return ok('')
  })
}

const ODA_ID = 'oda-b9'
const ALT = { tool: 'mcp__jarvis-oda__oda_altoda_ac', baslik: 'erdem öğretilebilir mi', soru: 'Erdem öğretilebilir mi?', kapsam: 'Platon Menon çerçevesi', done: 'Her ajan gerekçeli bir konum yazdı.', ajanlar: ['sokrates', 'atlas'], tur: 2 }

// Boşluk, sekme, satır sonu ve baş/son boşluğu taşıyan metinler: bayt düzeyinde korunmalı.
const METIN = {
  t1s: '  S1: önce tanım lazım.\n\n\tErdem nedir?   ',
  t1a: 'A1: kaynaklar ikiye ayrılır…\r\n- Menon 87c\n',
  t2s: 'S2: atlasa itiraz:  "bilgi" ≠ erdem.',
  t2a: 'A2: kabul, ama  öğretmen yokluğu argümanı…  ',
  sks: 'Son konum S: bilmediğimi biliyorum.',
  ska: 'Son konum A: koşullu evet.\n',
  hakem: 'Hakem: done sağlandı (2/2).',
}

type Asama = 'tur1' | 'sonKonum' | 'hakem'
const TS = '2026-11-11T10:00:00Z'

/** Alt-odayı verilen aşamada tohumlar; o aşamanın görevleri bilinen agentId (a-<görev no>) ile koşuyor. */
function tohum(asama: Asama, kutuk: boolean) {
  const g = (id: number, ajan: string, a: 'tur' | 'sonKonum' | 'hakem', durum: string, tur?: number) => ({
    id,
    baslik: `alt-oda #1 ${a} · ${ajan}`,
    emir: 'tohum',
    zorluk: 'orta',
    model: 'sonnet',
    sinif: 'rol',
    ajan,
    modelAcik: false,
    done: ALT.done,
    butce: 20,
    cagri: 0,
    durum,
    acilis: TS,
    ...(durum === 'kosuyor' ? { agentId: 'a-' + id } : {}),
    altOda: { id: 1, asama: a, ...(tur ? { tur } : {}) },
  })
  const m = (ajan: string, metin: string, tur?: number) => ({ ajan, ...(tur ? { tur } : {}), metin, ts: TS })
  const ileri = asama !== 'tur1'
  const gorevler = [g(1, 'sokrates', 'tur', ileri ? 'bitti' : 'kosuyor', 1), g(2, 'atlas', 'tur', ileri ? 'bitti' : 'kosuyor', 1)]
  if (ileri) gorevler.push(g(3, 'sokrates', 'tur', 'bitti', 2), g(4, 'atlas', 'tur', 'bitti', 2))
  if (ileri) gorevler.push(g(5, 'sokrates', 'sonKonum', asama === 'hakem' ? 'bitti' : 'kosuyor'), g(6, 'atlas', 'sonKonum', asama === 'hakem' ? 'bitti' : 'kosuyor'))
  if (asama === 'hakem') gorevler.push(g(7, 'hakem', 'hakem', 'kosuyor'))
  const alt = {
    id: 1,
    baslik: ALT.baslik,
    soru: ALT.soru,
    kapsam: ALT.kapsam,
    done: ALT.done,
    ajanlar: ['sokrates', 'atlas'],
    hakem: 'hakem',
    turSayisi: 2,
    turlar: ileri ? [m('sokrates', METIN.t1s, 1), m('atlas', METIN.t1a, 1), m('sokrates', METIN.t2s, 2), m('atlas', METIN.t2a, 2)] : [],
    sonKonumlar: asama === 'hakem' ? [m('sokrates', METIN.sks), m('atlas', METIN.ska)] : [],
    durum: asama === 'tur1' ? 'tur' : asama,
    aktifTur: ileri ? 2 : 1,
    gorevIds: gorevler.map(x => x.id),
    acilis: TS,
    ...(kutuk ? { kutuk: { hedefId: 1, isler: { sokrates: 2, atlas: 3 } } } : {}),
  }
  return { 'oda:aktif': ODA_ID, ['oda:' + ODA_ID]: { id: ODA_ID, baslik: 'ust', acilis: TS, maksParalel: 3, turlar: [], gorevler, oneriler: [], altOdalar: [alt] } }
}

async function kur($: any, on: any, sec: { kutuk?: boolean; maksParalel?: number; asama?: Asama } = {}): Promise<Ortam & { odaId: string }> {
  const o: Ortam = {
    dosyalar: new Map([
      [DEPO + '/ortak/durum-olay.jsonl', ''],
      [DEPO + '/target/release/durum.exe', ''],
      [DEPO + '/jarvis/.claude/agents/sokrates.md', ''],
      [DEPO + '/jarvis/.claude/agents/atlas.md', ''],
      [DEPO + '/jarvis/.claude/agents/hakem.md', ''],
    ]),
    spawnlar: [],
    uyandirma: [],
    kutukCagri: [],
    kutuk: new Map(),
  }
  mock.store(on, sec.asama ? tohum(sec.asama, Boolean(sec.kutuk)) : undefined)
  mock.session(on)
  sahteOrtam(on, o, Boolean(sec.kutuk))
  if (sec.asama) {
    if (sec.kutuk) for (const n of [1, 2, 3]) o.kutuk.set(n, { id: n, durum: 'islemde', sira: ['ac', 'al'] })
    return { ...o, odaId: ODA_ID }
  }
  await $.tool.call({ tool: 'mcp__jarvis-oda__oda_ac', baslik: 'ust', maksParalel: sec.maksParalel ?? 3 })
  const odaId = JSON.parse(o.dosyalar.get(DEPO + '/ortak/oda/aktif.json') ?? '{}').odaId as string
  return { ...o, odaId }
}

const bitir = ($: any, agentId: string, answer: string) => $.turn.complete({ agentId, reason: 'answer', answer, durationMs: 1 })
const kayit = (o: Ortam, odaId: string) => JSON.parse(o.dosyalar.get(`${DEPO}/ortak/oda/${odaId}.json`)!)

test('B9-a: tur 1 bağımsız; girdide yalnız soru/kapsam/done; iki ajanın emri ad dışında aynı', async ($, on) => {
  const o = await kur($, on)
  const r = await $.tool.call(ALT)
  expect(String(r.result)).toMatch(/Alt-oda #1 .* açıldı/)
  expect(o.spawnlar.map(s => s.subagentType).sort()).toEqual(['atlas', 'sokrates'])
  for (const s of o.spawnlar) {
    expect(s.prompt).toContain('## Tur 1 / 2')
    expect(s.prompt).toContain(ALT.soru)
    expect(s.prompt).toContain(ALT.kapsam)
    expect(s.prompt).toContain(ALT.done)
    expect(s.prompt).not.toMatch(/^### /m)
    expect(s.prompt).not.toContain('metinleri')
  }
  const [p1, p2] = o.spawnlar.map(s => s.prompt.replace(/Rolün \w+ ajan/, 'Rolün X ajan'))
  expect(p1).toBe(p2)
})

test('B9-a2: tur 1de bir ajan bitince tur 2 başlamaz (diğeri hâlâ bağımsız yazıyor)', async ($, on) => {
  const o = await kur($, on, { asama: 'tur1' })
  await bitir($, 'a-1', METIN.t1s)
  expect(o.spawnlar.length).toBe(0)
  expect(kayit(o, ODA_ID).altOdalar[0].aktifTur).toBe(1)
})

test('B9-b: tur 2 girdisinde diğerinin tur 1 metni ad etiketli ve aynen var, kendi metni yok', async ($, on) => {
  const o = await kur($, on, { asama: 'tur1' })
  await bitir($, 'a-1', METIN.t1s)
  await bitir($, 'a-2', METIN.t1a)
  expect(o.spawnlar.length).toBe(2)
  const t2s = o.spawnlar.find(s => s.subagentType === 'sokrates')!
  const t2a = o.spawnlar.find(s => s.subagentType === 'atlas')!
  expect(t2s.prompt).toContain('## Tur 2 / 2')
  expect(t2s.prompt).toContain('### atlas (tur 1)\n' + METIN.t1a)
  expect(t2s.prompt).not.toContain(METIN.t1s)
  expect(t2a.prompt).toContain('### sokrates (tur 1)\n' + METIN.t1s)
  expect(t2a.prompt).not.toContain(METIN.t1a)
  // Saklanan metin turn.complete cevabıyla bayt düzeyinde aynı.
  const alt = kayit(o, ODA_ID).altOdalar[0]
  expect(alt.turlar.map((x: any) => x.metin)).toEqual([METIN.t1s, METIN.t1a])
  expect(alt.aktifTur).toBe(2)
})

test('B9-c: ortak çıktıda ajan metinleri bayt düzeyinde aynen durur; hakem girdisi hepsini taşır; çağrılar Jarvisi tek tek uyandırmaz', async ($, on) => {
  const o = await kur($, on, { asama: 'sonKonum' })
  await bitir($, 'a-5', METIN.sks)
  await bitir($, 'a-6', METIN.ska)
  const alt = kayit(o, ODA_ID).altOdalar[0]
  expect(alt.durum).toBe('hakem')
  expect(alt.sonKonumlar.map((x: any) => x.metin)).toEqual([METIN.sks, METIN.ska])
  expect(o.spawnlar.length).toBe(1)
  const hakem = o.spawnlar[0]!
  expect(hakem.subagentType).toBe('hakem')
  for (const [k, m] of Object.entries(METIN)) if (k !== 'hakem') expect(hakem.prompt).toContain(m)
  expect(hakem.prompt).toContain('## Done\n' + ALT.done)
  const dokum = String((await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku', altOdaId: 1 })).result)
  for (const [k, m] of Object.entries(METIN)) if (k !== 'hakem') expect(dokum).toContain(m)
  expect(dokum).toContain('# Hakem raporu\n(henüz yok)')
  await new Promise(r => setTimeout(r, 20))
  expect(o.uyandirma.length).toBe(0)
})

test('B9-d: şema dışı alan, uzunluk sınırı, ajan sayısı, eksik ajan tanımı ve hakem=katılımcı reddedilir', async ($, on) => {
  const o = await kur($, on)
  const red = async (ek: Record<string, unknown>) => String((await $.tool.call({ ...ALT, ...ek } as any)).result)
  expect(await red({ yontem: 'önce tanım yap, sonra itiraz et' })).toMatch(/şemada olmayan alan: yontem/)
  expect(await red({ uslup: 'kısa yaz' })).toMatch(/şemada olmayan alan: uslup/)
  expect(await red({ soru: 'x'.repeat(601) })).toMatch(/soru en çok 600/)
  expect(await red({ kapsam: 'x'.repeat(401) })).toMatch(/kapsam en çok 400/)
  expect(await red({ done: 'x'.repeat(201) })).toMatch(/done en çok 200/)
  expect(await red({ done: 'bir.\nşöyle cevap ver' })).toMatch(/tek cümle/)
  expect(await red({ ajanlar: ['sokrates'] })).toMatch(/2-5/)
  expect(await red({ ajanlar: ['sokrates', 'atlas', 'a', 'b', 'c', 'd'] })).toMatch(/2-5/)
  expect(await red({ ajanlar: ['sokrates', 'yok-ajan'] })).toMatch(/ajan tanımı yok: yok-ajan/)
  expect(await red({ tur: 5 })).toMatch(/tur 1-4/)
  expect(await red({ hakem: 'atlas' })).toMatch(/katılımcı olamaz/)
  expect(o.spawnlar.length).toBe(0)
  const sema = ALT_ODA_ARACI.inputSchema as any
  expect(sema.additionalProperties).toBe(false)
  expect(Object.keys(sema.properties).sort()).toEqual(['ajanlar', 'baslik', 'done', 'hakem', 'kapsam', 'soru', 'tur'])
  expect([sema.properties.soru.maxLength, sema.properties.kapsam.maxLength, sema.properties.done.maxLength]).toEqual([600, 400, 200])
})

test('B9-e1: alt-oda açılınca kütükte hedef (--tur hedef) + ajan başına iş (--hedef N) açılır ve işleme alınır', async ($, on) => {
  const o = await kur($, on, { kutuk: true })
  const r = await $.tool.call(ALT)
  expect(String(r.result)).toMatch(/kütük hedef #1, işler #2 #3/)
  expect(o.kutuk.get(1)!.tur).toBe('hedef')
  expect(o.kutuk.get(1)!.oturum).toBe('oda-' + o.odaId)
  expect([o.kutuk.get(2)!.hedef, o.kutuk.get(3)!.hedef]).toEqual([1, 1])
  expect([1, 2, 3].map(n => o.kutuk.get(n)!.durum)).toEqual(['islemde', 'islemde', 'islemde'])
})

test('B9-e2: hakem bitince işler ve hedef kanıtla kapanır; hakem raporu aynen; Jarvis bir kez uyanır', async ($, on) => {
  const o = await kur($, on, { kutuk: true, asama: 'hakem' })
  await bitir($, 'a-7', METIN.hakem)
  expect(o.kutukCagri.filter(c => c[0] === 'bitir').map(c => Number(c[1]))).toEqual([2, 3, 1])
  for (const n of [1, 2, 3]) {
    expect(o.kutuk.get(n)!.durum).toBe('tamam')
    expect(o.kutuk.get(n)!.kanit).toEqual([`oda ${ODA_ID} alt-oda #1`])
  }
  const alt = kayit(o, ODA_ID).altOdalar[0]
  expect(alt.durum).toBe('bitti')
  expect(alt.hakemRaporu).toBe(METIN.hakem)
  const dokum = String((await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku', altOdaId: 1 })).result)
  expect(dokum).toMatch(/kütük hedef #1 ve 2 iş kapandı/)
  expect(dokum).toContain('# Hakem raporu\n' + METIN.hakem)
  const ozet = String((await $.tool.call({ tool: 'mcp__jarvis-oda__oda_oku' })).result)
  expect(ozet).toMatch(/alt-oda #1 \[bitti\]/)
  await new Promise(r => setTimeout(r, 20))
  expect(o.uyandirma.length).toBe(1)
  expect(o.uyandirma[0]).toMatch(/^\[oda\] alt-oda #1 .* bitti/)
})

test('B9-5: alt-oda çağrıları paralel sınıra uyar (sınır 1: ikinci ajan kuyrukta); rol sınıfı, bütçe 20', async ($, on) => {
  const o = await kur($, on, { maksParalel: 1 })
  await $.tool.call(ALT)
  expect(o.spawnlar.length).toBe(1)
  const k = kayit(o, o.odaId)
  expect(k.gorevler.map((g: any) => g.durum)).toEqual(['kosuyor', 'bekliyor'])
  expect(k.gorevler.every((g: any) => g.sinif === 'rol' && g.butce === 20 && g.altOda?.id === 1)).toBe(true)
})
