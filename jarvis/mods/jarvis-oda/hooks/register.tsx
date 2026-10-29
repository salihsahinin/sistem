// jarvis-oda — lobi eşgörevi mod (Salih 2026-10-27, Karar 126).
// Jarvis (Fable, ana-sıra) plan ve görev yazar; görevler zorluğa göre
// Haiku / Sonnet / Opus işçi ajanlarına dağılır (video fikir 3: otomatik model
// yönlendirme); işçi raporları ve önerileri odaya düşer (fikir 1: oturumlar arası
// mesajlaşma); pano canlı durumu gösterir (fikir 2: ajan panosu). Öneri kararı
// Salih'in elindedir (human in the loop). v0.2: anlık paralel işçi sayısı
// değişken (maksParalel, kuyruk) + ortak sohbet (Salih ↔ Jarvis ↔ tüm işçiler).
// v0.3 (Salih 2026-10-29, "tanrısal bakış"): işçi akışı canlı izlenir; tool.call +
// turn.step kancaları işçi başına hareket kaydı tutar, pano her işçinin son
// hareketlerini ve ortak canlı akışı gösterir, 'izle' düğmesi transkript görünümünü
// o işçiye çevirir ($.ui.view), 'ana sohbete dön' geri alır.
// v0.4 (Salih 2026-10-29, Sokrates odası): oda_gorev_ver `ajan` alanı; değer
// .claude/agents/<ad>.md ajan tipi (hakem, sokrates…), subagentType olarak geçer,
// rol metnini/araç kısıtını/modelini Claude Code yükler; plan turları emre eklenmez
// (bağlam paylaşmayan rol, yapan ≠ ölçen); panoda [ajan] etiketi.
// v0.4.1: tur/hareket saatleri görünümde yerel saat (kayıt UTC kalır; Salih: 13:54 ≠ 16:54).
import { atom, read, update } from 'claude-code'
import type { Register, EngineInterface } from 'claude-code'

import type { Oda, OdaGorev, OdaOneri, OdaTur, OdaTurTuru, OdaZorluk, AjanDurum, OdaHareket } from '../types'

const PANE = 'jarvis-oda'
const STORE_AKTIF = 'oda:aktif'
const odaAtom = atom({ plugin: 'jarvis-oda', key: 'oda' } as const, null as Oda | null)
const ajanAtom = atom({ plugin: 'jarvis-oda', key: 'ajanlar' } as const, [] as AjanDurum[])
const hareketAtom = atom({ plugin: 'jarvis-oda', key: 'hareket' } as const, [] as OdaHareket[])
const HAREKET_TAVAN = 300

/** İşçi akışına parça ekler (yalnız oda görevine bağlı ajanlar). */
async function hareketEkle($: EngineInterface, agentId: string, tur: OdaHareket['tur'], ozet: string): Promise<void> {
  const oda = await read($, odaAtom)
  const g = oda?.gorevler.find(x => x.agentId === agentId)
  if (!g) return
  const h: OdaHareket = { ts: simdi(), gorevId: g.id, agentId, tur, ozet: kisa(ozet, 220) }
  await update($, hareketAtom, eski => [...eski, h].slice(-HAREKET_TAVAN))
}

/** tool.call girdisinden tek satırlık Türkçe özet. */
function aracOzeti(e: Record<string, unknown>): string {
  const ad = String(e.tool ?? '?')
  const al = (k: string) => (typeof e[k] === 'string' ? (e[k] as string) : undefined)
  if (ad === 'Bash') return `Bash: ${al('description') ?? al('command') ?? ''}`
  if (ad === 'Read' || ad === 'Write' || ad === 'Edit' || ad === 'NotebookEdit') return `${ad}: ${al('file_path') ?? ''}`
  if (ad === 'Grep' || ad === 'Glob') return `${ad}: ${al('pattern') ?? ''}${al('path') ? ' @ ' + al('path') : ''}`
  if (ad === 'WebFetch') return `WebFetch: ${al('url') ?? ''}`
  if (ad === 'WebSearch') return `WebSearch: ${al('query') ?? ''}`
  if (ad === 'Agent') return `Agent: ${al('description') ?? ''}`
  if (ad.startsWith('mcp__jarvis-oda__')) return `${ad.replace('mcp__jarvis-oda__', '')}: ${al('metin') ?? ''}`
  const ilk = Object.entries(e).find(([k, v]) => typeof v === 'string' && !['tool', 'tool_use_id', 'agentId'].includes(k))
  return ilk ? `${ad}: ${ilk[1] as string}` : ad
}

const MODEL_HARITASI: Record<OdaZorluk, string> = { kolay: 'haiku', orta: 'sonnet', zor: 'opus' }

function simdi(): string {
  return new Date().toISOString()
}

/** v0.4.1: kayıt UTC (ISO) kalır, görünüm yerel saat (tr-TR, 24 saat); saniye isteğe bağlı. */
function saat(ts: string, saniye = true): string {
  const d = new Date(ts)
  if (Number.isNaN(d.getTime())) return ts.slice(11, saniye ? 19 : 16)
  return d.toLocaleTimeString('tr-TR', { hour12: false, hour: '2-digit', minute: '2-digit', ...(saniye ? { second: '2-digit' } : {}) })
}

function kisa(metin: string, n = 160): string {
  const tek = metin.replace(/\s+/g, ' ').trim()
  return tek.length > n ? tek.slice(0, n - 1) + '…' : tek
}

function kosan(oda: Oda): number {
  return oda.gorevler.filter(g => g.durum === 'kosuyor').length
}

async function odaKaydet($: EngineInterface, oda: Oda): Promise<void> {
  await $.store.set('oda:' + oda.id, oda)
  await $.store.set(STORE_AKTIF, oda.id)
  await update($, odaAtom, () => oda)
  const bekleyen = oda.oneriler.filter(o => o.durum === 'bekliyor').length
  const kuyruk = oda.gorevler.filter(g => g.durum === 'bekliyor').length
  $.ui.status(`oda ${oda.baslik}: ${kosan(oda)}/${oda.maksParalel} koşuyor · ${kuyruk} kuyrukta · ${bekleyen} öneri`)
}

async function odaYukle($: EngineInterface): Promise<Oda | null> {
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

function turEkle(oda: Oda, kim: string, tur: OdaTurTuru, metin: string, gorevId?: number): Oda {
  const yeni: OdaTur = { ts: simdi(), kim, tur, metin, gorevId }
  return { ...oda, turlar: [...oda.turlar, yeni].slice(-400) }
}

function odaMetni(oda: Oda, son = 12, hareketler: OdaHareket[] = []): string {
  const satirlar: string[] = [`# Oda: ${oda.baslik} (${oda.id}) · açılış ${oda.acilis} · paralel ${kosan(oda)}/${oda.maksParalel}`]
  satirlar.push('## Görevler')
  if (oda.gorevler.length === 0) satirlar.push('(yok)')
  for (const g of oda.gorevler) {
    satirlar.push(`- #${g.id} [${g.durum}] ${g.ajan ? '[' + g.ajan + '] ' : ''}${g.baslik} · ${g.zorluk}→${g.ajan && !g.modelAcik ? 'ajan tanımı' : g.model}${g.agentId ? ' · ajan ' + g.agentId : ''}`)
    if (g.sonuc) satirlar.push('  sonuç: ' + kisa(g.sonuc, 400))
    for (const h of hareketler.filter(x => x.gorevId === g.id).slice(-3)) satirlar.push(`  ${saat(h.ts)} [${h.tur}] ${kisa(h.ozet, 160)}`)
  }
  const bekleyen = oda.oneriler.filter(o => o.durum === 'bekliyor')
  satirlar.push(`## Öneriler (bekleyen ${bekleyen.length})`)
  for (const o of oda.oneriler.slice(-10)) satirlar.push(`- Ö${o.id} [${o.durum}] ${o.kim}: ${kisa(o.metin, 200)} · gerekçe: ${kisa(o.gerekce, 120)}${o.not ? ' · not: ' + o.not : ''}`)
  satirlar.push(`## Son ${son} tur`)
  for (const t of oda.turlar.slice(-son)) satirlar.push(`- ${saat(t.ts)} ${t.kim} [${t.tur}]${t.gorevId ? ' #' + t.gorevId : ''}: ${kisa(t.metin, 300)}`)
  return satirlar.join('\n')
}

function isciEmri(oda: Oda, g: OdaGorev): string {
  if (g.ajan) {
    return [
      `Bu görev "${oda.baslik}" odasında #${g.id} numarasıyla açıldı; rolün ${g.ajan} ajan tanımındaki gibidir, ona aynen uy. Dil: Türkçe.`,
      'Oda planı, diğer işçilerin raporları ve sohbet sana verilmez (bağlam paylaşmayan rol). Ara not için mcp__jarvis-oda__oda_rapor kullanabilirsin; son cevabın rapordur.',
      '\n## Görev\n' + g.emir,
    ].join('\n')
  }
  const plan = oda.turlar.filter(t => t.tur === 'plan').slice(-3).map(t => '- ' + t.metin).join('\n')
  return [
    `Sen "${oda.baslik}" odasının işçi ajanısın (görev #${g.id}, model ${g.model}). Dil: Türkçe; kod tanımlayıcıları aslıyla.`,
    'Jarvis (ana-sıra) planladı, sen uygularsın. Yalnız bu görevi yap; kapsam dışına çıkma; sormadan tasarım kararı değiştirme.',
    'Bir karar gerekiyorsa işi durdurma: mcp__jarvis-oda__oda_oneri aracıyla öneri bırak (metin + gerekçe), varsayılan yolu uygulayıp raporunda belirt.',
    'Ortak sohbet: "[oda sohbet]" ile başlayan mesaj Salih ya da Jarvis\'ten gelir; kısa cevabını mcp__jarvis-oda__oda_rapor ile ver, sonra işine devam et. Ara durum için de oda_rapor kullanabilirsin (kısa, çıplak veri).',
    'Son cevabın rapordur: ne yaptın · dokunulan dosyalar (tam yol) · doğrulama kanıtı (komut + çıktı özeti) · açık kalan. Övgü yok, kısa cümleler.',
    plan ? '\nOda planı (son 3):\n' + plan : '',
    '\n## Görev\n' + g.emir,
  ].join('\n')
}

async function gorevBaslat($: EngineInterface, oda: Oda, id: number): Promise<Oda> {
  const gorev = oda.gorevler.find(g => g.id === id)
  if (!gorev) return oda
  const spawn = await $.agent.spawn({
    prompt: isciEmri(oda, gorev),
    description: `oda #${id} ${kisa(gorev.baslik, 40)}`,
    subagentType: gorev.ajan ?? 'general-purpose',
    ...(gorev.ajan && !gorev.modelAcik ? {} : { model: gorev.model }),
    name: `oda-${id}`,
  })
  const taze = (await odaYukle($)) ?? oda
  if ('deny' in spawn && spawn.deny) {
    const hata = { ...taze, gorevler: taze.gorevler.map(g => (g.id === id ? { ...g, durum: 'hata' as const, sonuc: 'spawn reddi: ' + spawn.deny, kapanis: simdi() } : g)) }
    const yeni = turEkle(hata, 'oda', 'not', `#${id} başlatılamadı: ${spawn.deny}`, id)
    await odaKaydet($, yeni)
    return yeni
  }
  const agentId = (spawn as { agentId?: string }).agentId
  const model = (spawn as { model?: string }).model ?? gorev.model
  const yeni = turEkle(
    { ...taze, gorevler: taze.gorevler.map(g => (g.id === id ? { ...g, durum: 'kosuyor' as const, agentId, model } : g)) },
    'oda',
    'not',
    `#${id} ${gorev.baslik} başladı (${model}${agentId ? ', ajan ' + agentId : ''})`,
    id,
  )
  await odaKaydet($, yeni)
  return yeni
}

/** Kuyruktaki görevleri maksParalel sınırına kadar başlatır. */
async function kuyrukIsle($: EngineInterface): Promise<Oda | null> {
  let oda = await odaYukle($)
  if (!oda) return null
  while (kosan(oda) < oda.maksParalel) {
    const sira = oda.gorevler.find(g => g.durum === 'bekliyor')
    if (!sira) break
    oda = await gorevBaslat($, oda, sira.id)
  }
  return oda
}

/** Ortak sohbet: mesaj odaya düşer, hedef işçilere (ya da hepsine) ve Jarvis'e iletilir. */
async function sohbetGonder($: EngineInterface, kim: string, metin: string, hedef?: string): Promise<string> {
  let oda = await odaYukle($)
  if (!oda) return 'Oda yok.'
  const m = metin.trim()
  if (!m) return 'Boş mesaj.'
  const hedefNo = /^#(\d+)/.exec(hedef ?? m)?.[1]
  oda = turEkle(oda, kim, 'sohbet', m)
  await odaKaydet($, oda)
  const alicilar = oda.gorevler.filter(g => g.durum === 'kosuyor' && g.agentId && (!hedefNo || g.id === Number(hedefNo)))
  let ulasan = 0
  for (const g of alicilar) {
    try {
      await $.session.append({ agentId: g.agentId!, message: { type: 'user', content: [{ type: 'text', text: `[oda sohbet] ${kim}: ${m}\n(Kısa cevabını oda_rapor ile ver, sonra görevine devam et.)` }] } })
      ulasan++
    } catch {
      /* ajan bitmiş olabilir */
    }
  }
  if (kim !== 'jarvis') {
    await $.session.append({ message: { type: 'user', content: [{ type: 'text', text: `[oda sohbet] ${kim}: ${m} (işçilere ulaştı: ${ulasan}/${alicilar.length})` }] } }).catch(() => undefined)
  }
  return `Sohbet düştü; işçilere ulaştı: ${ulasan}/${alicilar.length}${hedefNo ? ' (hedef #' + hedefNo + ')' : ''}.`
}

export const register: Register = (on, options) => {
  const ayar = (options ?? {}) as { otoUyandir?: boolean; maksParalel?: number }
  const otoUyandir = ayar.otoUyandir ?? true
  const varsayilanMaks = Math.max(1, Math.min(12, Number(ayar.maksParalel ?? 3) || 3))

  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'oda', description: 'Oda panosunu açar (Jarvis planlar, işçiler uygular, ortak sohbet).' })
    const ortak = { isDeferred: false as const }
    await $.tool.register({
      ...ortak,
      name: 'oda_ac',
      description: 'Yeni oda açar ya da verilen başlıkla aktif odayı değiştirir. Oda = plan + görevler + işçi raporları + öneriler + ortak sohbet. Jarvis (ana-sıra) çağırır.',
      inputSchema: { type: 'object', properties: { baslik: { type: 'string', description: 'Oda başlığı (tek satır)' }, maksParalel: { type: 'integer', description: 'Aynı anda koşan işçi üst sınırı (varsayılan 3)' } }, required: ['baslik'] },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_plan',
      description: 'Aktif odaya plan turu yazar (Jarvis). İşçilere emir vermeden önce planın özünü buraya yaz; işçi emrine son 3 plan turu eklenir.',
      inputSchema: { type: 'object', properties: { metin: { type: 'string' } }, required: ['metin'] },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_gorev_ver',
      description:
        'Aktif odada görev açar; maksParalel sınırı altındaysa işçi ajanı hemen arka planda başlatır, değilse kuyruğa alır (biri bitince sıradaki başlar). Model zorluğa göre: kolay→haiku, orta→sonnet, zor→opus (model alanı verilirse o kazanır). ajan alanı verilirse (.claude/agents/<ad>.md, ör. hakem) işçi o rolle, kendi model/araç kısıtıyla ve plan bağlamı olmadan başlar (yapan ≠ ölçen). Görev bitince rapor odaya düşer ve Jarvis uyandırılır.',
      inputSchema: {
        type: 'object',
        properties: {
          baslik: { type: 'string', description: 'Kısa görev adı' },
          emir: { type: 'string', description: 'İşçinin tam emri: amaç, dosyalar, done koşulu, doğrulama' },
          zorluk: { type: 'string', enum: ['kolay', 'orta', 'zor'] },
          model: { type: 'string', description: 'İsteğe bağlı: haiku | sonnet | opus' },
          ajan: { type: 'string', description: 'İsteğe bağlı: .claude/agents/<ad>.md ajan tipi (ör. hakem, sokrates). Verilirse işçi o rolle başlar (model/araç kısıtı tanımdan; model alanı verilmedikçe), plan turları emre eklenmez.' },
        },
        required: ['baslik', 'emir', 'zorluk'],
      },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_oku',
      description: 'Aktif odanın durumunu metin olarak döndürür: paralel sayacı, görevler + durumları + her işçinin son 3 hareketi (araç çağrısı / metin), bekleyen öneriler, son turlar (sohbet dahil).',
      inputSchema: { type: 'object', properties: { son: { type: 'integer', description: 'Kaç tur (varsayılan 12)' } } },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_ayar',
      description: 'Aktif odanın anlık paralel işçi üst sınırını değiştirir (maksParalel 1-12). Sınır düşerse koşanlar durmaz, yeni başlatma durur; yükselirse kuyruk işlenir.',
      inputSchema: { type: 'object', properties: { maksParalel: { type: 'integer' } }, required: ['maksParalel'] },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_sohbet',
      description: 'Ortak sohbete mesaj yazar: koşan tüm işçilere (ya da "#N" ile tek işçiye) iletilir; işçiler oda_rapor ile cevaplar. Jarvis\'in işçilerle anlık konuşma kanalı.',
      inputSchema: { type: 'object', properties: { metin: { type: 'string' }, hedef: { type: 'string', description: 'İsteğe bağlı "#N" (tek işçi); boşsa herkes' } }, required: ['metin'] },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_oneri_karar',
      description: 'Bekleyen bir öneriyi kabul/ret eder (Jarvis ya da Salih adına). Karar odaya tur olarak düşer ve ilgili işçiye iletilir.',
      inputSchema: {
        type: 'object',
        properties: { oneriId: { type: 'integer' }, karar: { type: 'string', enum: ['kabul', 'ret'] }, not: { type: 'string' } },
        required: ['oneriId', 'karar'],
      },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_oneri',
      description: 'İşçi ajan karar gerektiren noktada öneri bırakır (metin + gerekçe). Karar Jarvis/Salih tarafından panodan ya da oda_oneri_karar ile verilir.',
      inputSchema: { type: 'object', properties: { metin: { type: 'string' }, gerekce: { type: 'string' } }, required: ['metin', 'gerekce'] },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_rapor',
      description: 'İşçi ajan ara durum raporu ya da sohbet cevabı düşer (kısa). Final cevap otomatik kaydedilir.',
      inputSchema: { type: 'object', properties: { metin: { type: 'string' } }, required: ['metin'] },
    })

    const oda = await odaYukle($)
    if (oda) $.ui.status(`oda ${oda.baslik}: ${kosan(oda)}/${oda.maksParalel} koşuyor`)
    void $.ui.open({ id: PANE, title: 'Oda' })

    // Ajan durumlarını 3 sn'de bir panoya yansıt; biten/ölen ajanı yakala; kuyruğu işle.
    $.clock.every(3000, async () => {
      const o = await read($, odaAtom)
      if (!o || !o.gorevler.some(g => g.durum === 'kosuyor')) return
      const liste = await $.agent.list()
      const ajanlar: AjanDurum[] = []
      for (const g of o.gorevler) {
        if (!g.agentId || g.durum !== 'kosuyor') continue
        const a = liste.find(x => x.id === g.agentId)
        ajanlar.push({ agentId: g.agentId, status: a?.status ?? 'bilinmiyor', gorevId: g.id })
      }
      await update($, ajanAtom, () => ajanlar)
      // turn.complete kaçtıysa (killed/failed) görevi kapat.
      const dusen = ajanlar.filter(a => a.status === 'killed' || a.status === 'failed')
      if (dusen.length) {
        const guncel = (await odaYukle($)) ?? o
        const yeni = { ...guncel, gorevler: guncel.gorevler.map(g => (dusen.some(d => d.gorevId === g.id) ? { ...g, durum: 'hata' as const, sonuc: g.sonuc ?? 'ajan ' + (dusen.find(d => d.gorevId === g.id)?.status ?? '') , kapanis: simdi() } : g)) }
        await odaKaydet($, yeni)
        await kuyrukIsle($)
      }
    })

    return next(e)
  })

  // v0.3: işçi akışı; her araç çağrısı hareket olarak düşer (hata/ret işaretli).
  on('tool.call', async ($, e, next) => {
    if (!e.agentId) return next(e)
    const agentId = e.agentId
    const ozet = aracOzeti(e as unknown as Record<string, unknown>)
    await hareketEkle($, agentId, 'arac', ozet).catch(() => undefined)
    const r = await next(e)
    if ('deny' in r && r.deny) await hareketEkle($, agentId, 'arac', `✗ ${ozet} → reddedildi: ${r.deny}`).catch(() => undefined)
    else if ('isError' in r && r.isError) await hareketEkle($, agentId, 'arac', `✗ ${ozet} → hata`).catch(() => undefined)
    return r
  })

  // v0.3: işçi akışı; model metni blok bitiminde hareket olarak düşer.
  on('turn.step', async function* ($, e, next) {
    if (!e.agentId) return yield* next(e)
    const agentId = e.agentId
    let metin = ''
    const bosalt = async () => {
      const t = metin.trim()
      metin = ''
      if (t) await hareketEkle($, agentId, 'metin', t).catch(() => undefined)
    }
    for await (const c of next(e)) {
      if (c.kind === 'text') metin += c.text
      else if (c.kind === 'tool' || c.kind === 'stop') await bosalt()
      yield c
    }
    await bosalt()
  })

  on('prompt.compose', async ($, e, next) => {
    const r = await next(e)
    const text = [
      '# jarvis-oda (mod)',
      'Oda = Jarvis planlar, işçi ajanlar uygular, ortak sohbet herkesi bağlar. Araçlar: oda_ac(baslik, maksParalel?) · oda_plan(metin) · oda_gorev_ver(baslik, emir, zorluk: kolay|orta|zor → haiku|sonnet|opus; sınır doluysa kuyruk) · oda_ayar(maksParalel) · oda_sohbet(metin, hedef "#N"?) · oda_oku · oda_oneri_karar(oneriId, kabul|ret). Çok-ajanlı iş: planı oda_plan ile yaz, görevleri paralel oda_gorev_ver ile aç, raporları oda_oku ile topla (oda_oku her işçinin son 3 hareketini de verir; Salih panodaki izle düğmesiyle işçi transkriptini canlı görür). "[oda]" ile başlayan kuyruk mesajı = görev raporu; "[oda sohbet] salih:" = Salih\'in panodan yazdığı ortak sohbet mesajı, Jarvis ona cevap verir ve gerekirse oda_sohbet ile işçilere iletir. Öneri kararı Salih\'indir: bekleyen öneriyi tek satırda sun.',
    ].join('\n')
    return { sections: [...r.sections, { id: 'jarvis-oda', text, scope: 'session' as const }] }
  })

  on('command.run', { command: 'oda' }, async $ => {
    await $.ui.open({ id: PANE, title: 'Oda', focus: true })
    const oda = await odaYukle($)
    return { text: oda ? odaMetni(oda, 6, await read($, hareketAtom)) : 'Oda yok. Jarvis oda_ac ile açar.' }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_ac' }, async ($, e) => {
    const a = e as { baslik?: string; maksParalel?: number }
    const baslik = String(a.baslik ?? 'oda')
    const id = new Date().toISOString().slice(0, 16).replace(/[-:T]/g, '') + '-' + baslik.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 24)
    const maks = Math.max(1, Math.min(12, Number(a.maksParalel ?? varsayilanMaks) || varsayilanMaks))
    const oda: Oda = { id, baslik, acilis: simdi(), maksParalel: maks, turlar: [], gorevler: [], oneriler: [] }
    await odaKaydet($, turEkle(oda, 'jarvis', 'not', `Oda açıldı: ${baslik} (paralel sınır ${maks})`))
    void $.ui.open({ id: PANE, title: 'Oda' })
    return { result: `Oda açıldı: ${baslik} (id ${id}, paralel sınır ${maks}). Şimdi oda_plan ile planı yaz, oda_gorev_ver ile görevleri dağıt.` }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_plan' }, async ($, e) => {
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok; önce oda_ac.' }
    await odaKaydet($, turEkle(oda, 'jarvis', 'plan', String((e as { metin?: string }).metin ?? '')))
    return { result: 'Plan turu yazıldı.' }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_ayar' }, async ($, e) => {
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok; önce oda_ac.' }
    const maks = Math.max(1, Math.min(12, Number((e as { maksParalel?: number }).maksParalel) || oda.maksParalel))
    await odaKaydet($, turEkle({ ...oda, maksParalel: maks }, 'jarvis', 'not', `paralel sınır ${oda.maksParalel} → ${maks}`))
    const son = await kuyrukIsle($)
    return { result: `maksParalel = ${maks}; koşan ${son ? kosan(son) : 0}, kuyrukta ${son ? son.gorevler.filter(g => g.durum === 'bekliyor').length : 0}.` }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_sohbet' }, async ($, e) => {
    const s = e as { metin?: string; hedef?: string }
    return { result: await sohbetGonder($, 'jarvis', String(s.metin ?? ''), s.hedef) }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_gorev_ver' }, async ($, e) => {
    const g0 = e as { baslik?: string; emir?: string; zorluk?: OdaZorluk; model?: string; ajan?: string }
    let oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok; önce oda_ac.' }
    const zorluk: OdaZorluk = g0.zorluk === 'kolay' || g0.zorluk === 'zor' ? g0.zorluk : 'orta'
    const model = g0.model && g0.model.trim() ? g0.model.trim() : MODEL_HARITASI[zorluk]
    const id = oda.gorevler.length + 1
    const ajan = g0.ajan && /^[a-z0-9_-]+$/i.test(g0.ajan.trim()) ? g0.ajan.trim() : undefined
    const modelAcik = Boolean(g0.model && g0.model.trim())
    const gorev: OdaGorev = { id, baslik: String(g0.baslik ?? 'görev ' + id), emir: String(g0.emir ?? ''), zorluk, model, durum: 'bekliyor', acilis: simdi(), ...(ajan ? { ajan, modelAcik } : {}) }
    oda = turEkle({ ...oda, gorevler: [...oda.gorevler, gorev] }, 'jarvis', 'gorev', `#${id} ${ajan ? '[' + ajan + '] ' : ''}${gorev.baslik} → ${!ajan || modelAcik ? model : 'model: ajan tanımı'}`, id)
    await odaKaydet($, oda)
    const son = (await kuyrukIsle($)) ?? oda
    const g = son.gorevler.find(x => x.id === id)
    if (g?.durum === 'kosuyor') return { result: `Görev #${id} "${gorev.baslik}" ${g.model} işçisinde koşuyor (ajan ${g.agentId ?? '?'}); paralel ${kosan(son)}/${son.maksParalel}. Bitince rapor odaya düşer; beklemeden başka görev verebilirsin.` }
    if (g?.durum === 'hata') return { result: `Görev #${id} başlatılamadı: ${g.sonuc ?? ''}` }
    return { result: `Görev #${id} "${gorev.baslik}" kuyruğa alındı (paralel sınır ${son.maksParalel} dolu: ${kosan(son)} koşuyor). Biri bitince başlar; oda_ayar ile sınırı artırabilirsin.` }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_oku' }, async ($, e) => {
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok; önce oda_ac.' }
    const son = Number((e as { son?: number }).son ?? 12)
    return { result: odaMetni(oda, Number.isFinite(son) && son > 0 ? son : 12, await read($, hareketAtom)) }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_oneri_karar' }, async ($, e) => {
    const k = e as { oneriId?: number; karar?: 'kabul' | 'ret'; not?: string }
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok.' }
    const oneri = oda.oneriler.find(o => o.id === Number(k.oneriId))
    if (!oneri) return { result: `Ö${k.oneriId} bulunamadı.` }
    const karar = k.karar === 'ret' ? 'ret' : 'kabul'
    const yeni = { ...oda, oneriler: oda.oneriler.map(o => (o.id === oneri.id ? { ...o, durum: karar as 'kabul' | 'ret', not: k.not } : o)) }
    await odaKaydet($, turEkle(yeni, 'jarvis', 'karar', `Ö${oneri.id} ${karar}${k.not ? ': ' + k.not : ''}`, oneri.gorevId))
    if (oneri.gorevId) {
      const g = oda.gorevler.find(x => x.id === oneri.gorevId)
      if (g?.agentId && g.durum === 'kosuyor') {
        await $.session.append({ agentId: g.agentId, message: { type: 'user', content: [{ type: 'text', text: `[oda] Ö${oneri.id} kararı: ${karar}${k.not ? ' · ' + k.not : ''}` }] } }).catch(() => undefined)
      }
    }
    return { result: `Ö${oneri.id} ${karar}.` }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_oneri' }, async ($, e) => {
    const o = e as { metin?: string; gerekce?: string; agentId?: string }
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok.' }
    const gorev = oda.gorevler.find(g => g.agentId && g.agentId === o.agentId)
    const id = oda.oneriler.length + 1
    const oneri: OdaOneri = { id, kim: gorev ? `işçi #${gorev.id}` : 'jarvis', gorevId: gorev?.id, metin: String(o.metin ?? ''), gerekce: String(o.gerekce ?? ''), durum: 'bekliyor' }
    const yeni = turEkle({ ...oda, oneriler: [...oda.oneriler, oneri] }, oneri.kim, 'oneri', `Ö${id}: ${oneri.metin} · gerekçe: ${oneri.gerekce}`, gorev?.id)
    await odaKaydet($, yeni)
    $.ui.toast(`Oda: Ö${id} öneri bekliyor (${oneri.kim})`)
    return { result: `Ö${id} kaydedildi; karar bekleniyor. Varsayılan yolu sürdür, raporunda belirt.` }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_rapor' }, async ($, e) => {
    const r = e as { metin?: string; agentId?: string }
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok.' }
    const gorev = oda.gorevler.find(g => g.agentId && g.agentId === r.agentId)
    const kim = gorev ? `işçi #${gorev.id}` : 'jarvis'
    await odaKaydet($, turEkle(oda, kim, 'rapor', String(r.metin ?? ''), gorev?.id))
    if (gorev) $.ui.toast(`Oda ${kim}: ${kisa(String(r.metin ?? ''), 80)}`)
    return { result: 'Rapor düştü.' }
  })

  // İşçi ajanın final cevabı = görev raporu; sonra kuyruk işlenir.
  on('turn.complete', async ($, e, next) => {
    const r = await next(e)
    if (!e.agentId) return r
    const oda = await odaYukle($)
    if (!oda) return r
    const gorev = oda.gorevler.find(g => g.agentId === e.agentId && g.durum === 'kosuyor')
    if (!gorev) return r
    const basarili = e.reason === 'answer' && !e.isAborted
    const sonuc = e.reason === 'answer' ? e.answer : `(${e.reason}) ${'text' in e ? e.text : ''}`
    const yeni = turEkle(
      { ...oda, gorevler: oda.gorevler.map(g => (g.id === gorev.id ? { ...g, durum: basarili ? ('bitti' as const) : ('hata' as const), sonuc, kapanis: simdi() } : g)) },
      `işçi #${gorev.id}`,
      'rapor',
      sonuc,
      gorev.id,
    )
    await odaKaydet($, yeni)
    $.ui.toast(`Oda: görev #${gorev.id} ${basarili ? 'bitti' : 'hata'} (${gorev.model})`)
    const son = (await kuyrukIsle($)) ?? yeni
    if (otoUyandir) {
      const ozet = `[oda] görev #${gorev.id} "${gorev.baslik}" ${basarili ? 'bitti' : 'hata'} (${gorev.model}). Rapor:\n${kisa(sonuc, 1500)}\n\nKoşan: ${kosan(son)}/${son.maksParalel} · kuyrukta: ${son.gorevler.filter(g => g.durum === 'bekliyor').length} · bekleyen öneri: ${son.oneriler.filter(o => o.durum === 'bekliyor').length}. oda_oku ile tamamını gör; sırada iş varsa oda_gorev_ver.`
      void $.prompt.submit({ text: ozet }).catch(() => undefined)
    }
    return r
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text, Button } = $.ui.resolve(e)
    const oda = await read($, odaAtom)
    const ajanlar = await read($, ajanAtom)
    const hareketler = await read($, hareketAtom)
    const izlenen = (e.props as { view?: { agentId?: string } } | undefined)?.view?.agentId
    if (!oda) {
      return (
        <Box flexDirection="column" padding={1}>
          <Text bold>Oda yok.</Text>
          <Text dimColor>Jarvis'e "oda aç: &lt;başlık&gt;" de; oda_ac aracı açar.</Text>
        </Box>
      )
    }
    const renk = (d: string) => (d === 'kosuyor' ? 'yellow' : d === 'bitti' ? 'green' : d === 'hata' ? 'red' : undefined)
    const bekleyen = oda.oneriler.filter(o => o.durum === 'bekliyor')
    const kuyruk = oda.gorevler.filter(g => g.durum === 'bekliyor').length
    const karar = (o: OdaOneri, k: 'kabul' | 'ret') => async () => {
      const guncel = (await odaYukle($)) ?? oda
      const yeni = { ...guncel, oneriler: guncel.oneriler.map(x => (x.id === o.id ? { ...x, durum: k } : x)) }
      await odaKaydet($, turEkle(yeni, 'salih', 'karar', `Ö${o.id} ${k}`, o.gorevId))
      const g = guncel.gorevler.find(x => x.id === o.gorevId)
      if (g?.agentId && g.durum === 'kosuyor') {
        await $.session.append({ agentId: g.agentId, message: { type: 'user', content: [{ type: 'text', text: `[oda] Ö${o.id} kararı (Salih): ${k}` }] } }).catch(() => undefined)
      }
      await $.session.append({ message: { type: 'user', content: [{ type: 'text', text: `[oda] Salih panodan Ö${o.id} kararı verdi: ${k} (${kisa(o.metin, 120)})` }] } }).catch(() => undefined)
    }
    const sinir = (delta: number) => async () => {
      const guncel = (await odaYukle($)) ?? oda
      const maks = Math.max(1, Math.min(12, guncel.maksParalel + delta))
      if (maks === guncel.maksParalel) return
      await odaKaydet($, turEkle({ ...guncel, maksParalel: maks }, 'salih', 'not', `paralel sınır ${guncel.maksParalel} → ${maks}`))
      await kuyrukIsle($)
    }
    const sohbet = oda.turlar.filter(t => t.tur === 'sohbet' || t.tur === 'rapor').slice(-10)
    const sohbetElemani =
      e.surface === 'mobile' ? (
        <Text dimColor>(mobilde giriş alanı yok; sohbet için Jarvis'e yaz)</Text>
      ) : (
        (() => {
          const { Input } = $.ui.resolve(e as typeof e & { surface: 'terminal' | 'desktop' | 'vscode' })
          return (
            <Input
              key="sohbet-giris"
              placeholder="herkese yaz; tek işçi için '#2 …'"
              submitLabel="gönder"
              onSubmit={value => {
                void sohbetGonder($, 'salih', value)
              }}
            />
          )
        })()
      )
    return (
      <Box flexDirection="column" padding={1} gap={1}>
        <Box flexDirection="row" justifyContent="space-between">
          <Text bold>Oda · {oda.baslik}</Text>
          <Button key="yenile" plain onPress={() => $.ui.invalidate('ui.render')}>
            ⟳
          </Button>
        </Box>
        <Box flexDirection="row" gap={1} alignItems="center">
          <Text>
            koşan <Text bold color={kosan(oda) > 0 ? 'yellow' : undefined}>{kosan(oda)}</Text> / sınır <Text bold>{oda.maksParalel}</Text>
            <Text dimColor> · kuyruk {kuyruk}</Text>
          </Text>
          <Button key="sinir-az" plain onPress={sinir(-1)}>
            −
          </Button>
          <Button key="sinir-cok" plain onPress={sinir(+1)}>
            +
          </Button>
        </Box>
        <Box flexDirection="column">
          <Text bold dimColor>
            Görevler ({oda.gorevler.length})
          </Text>
          {oda.gorevler.length === 0 && <Text dimColor>Henüz görev yok.</Text>}
          {oda.gorevler.map(g => {
            const a = ajanlar.find(x => x.gorevId === g.id)
            return (
              <Box flexDirection="column">
                <Text>
                  <Text color={renk(g.durum)}>{g.durum === 'kosuyor' ? '●' : g.durum === 'bitti' ? '✓' : g.durum === 'hata' ? '✗' : '○'}</Text> #{g.id} {g.ajan ? <Text color="magenta">[{g.ajan}] </Text> : null}{g.baslik}{' '}
                  <Text dimColor>
                    · {g.zorluk}→{g.ajan && !g.modelAcik ? 'ajan tanımı' : g.model}
                    {g.durum === 'bekliyor' ? ' · kuyrukta' : a ? ' · ' + a.status : ''}
                  </Text>
                </Text>
                {g.sonuc && (
                  <Text dimColor>
                    {'   '}
                    {kisa(g.sonuc, 110)}
                  </Text>
                )}
                {g.durum === 'kosuyor' && g.agentId && (
                  <Box flexDirection="row" gap={1}>
                    <Text dimColor>{'   '}</Text>
                    <Button key={'izle-' + g.id} plain onPress={() => $.ui.view({ agentId: g.agentId! })}>
                      {izlenen === g.agentId ? '▶ izleniyor' : 'izle'}
                    </Button>
                    {izlenen === g.agentId && (
                      <Button key={'ana-' + g.id} plain onPress={() => $.ui.view({})}>
                        ana sohbete dön
                      </Button>
                    )}
                  </Box>
                )}
                {g.durum === 'kosuyor' &&
                  hareketler
                    .filter(h => h.gorevId === g.id)
                    .slice(-2)
                    .map(h => (
                      <Text dimColor>
                        {'   '}
                        <Text color={h.tur === 'arac' ? 'blue' : undefined}>{h.tur === 'arac' ? '⚙' : '…'}</Text> {kisa(h.ozet, 100)}
                      </Text>
                    ))}
              </Box>
            )
          })}
        </Box>
        {bekleyen.length > 0 && (
          <Box flexDirection="column">
            <Text bold color="yellow">
              Karar bekleyen öneriler ({bekleyen.length})
            </Text>
            {bekleyen.map(o => (
              <Box flexDirection="column">
                <Text>
                  Ö{o.id} <Text dimColor>{o.kim}:</Text> {kisa(o.metin, 120)}
                </Text>
                <Text dimColor>
                  {'   gerekçe: '}
                  {kisa(o.gerekce, 100)}
                </Text>
                <Box flexDirection="row" gap={1}>
                  <Button key={'kabul-' + o.id} variant="primary" onPress={karar(o, 'kabul')}>
                    Kabul
                  </Button>
                  <Button key={'ret-' + o.id} onPress={karar(o, 'ret')}>
                    Ret
                  </Button>
                </Box>
              </Box>
            ))}
          </Box>
        )}
        <Box flexDirection="column">
          <Text bold dimColor>
            Ortak sohbet (Salih · Jarvis · işçiler)
          </Text>
          {sohbet.length === 0 && <Text dimColor>Henüz mesaj yok.</Text>}
          {sohbet.map(t => (
            <Text>
              <Text dimColor>{saat(t.ts, false)}</Text> <Text bold color={t.kim === 'salih' ? 'cyan' : t.kim === 'jarvis' ? 'magenta' : 'green'}>{t.kim}</Text>
              {t.tur === 'rapor' ? <Text dimColor> [rapor]</Text> : null} {kisa(t.metin, 140)}
            </Text>
          ))}
          {sohbetElemani}
        </Box>
        <Box flexDirection="column">
          <Text bold dimColor>
            Canlı akış (tüm işçiler, son 12)
          </Text>
          {hareketler.length === 0 && <Text dimColor>Henüz hareket yok.</Text>}
          {hareketler.slice(-12).map(h => (
            <Text>
              <Text dimColor>{saat(h.ts)}</Text> <Text bold color="green">#{h.gorevId}</Text>{' '}
              <Text color={h.tur === 'arac' ? 'blue' : undefined}>{h.tur === 'arac' ? '⚙' : '…'}</Text> {kisa(h.ozet, 120)}
            </Text>
          ))}
        </Box>
        <Box flexDirection="column">
          <Text bold dimColor>
            Son olaylar
          </Text>
          {oda.turlar
            .filter(t => t.tur !== 'sohbet' && t.tur !== 'rapor')
            .slice(-6)
            .map(t => (
              <Text dimColor>
                <Text dimColor>{saat(t.ts, false)}</Text> {t.kim} [{t.tur}] {kisa(t.metin, 90)}
              </Text>
            ))}
        </Box>
      </Box>
    )
  })
}
