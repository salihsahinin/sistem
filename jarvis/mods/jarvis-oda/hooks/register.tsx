// jarvis-oda — lobi eşgörevi mod (Salih 2026-10-27).
// Jarvis (Fable, ana-sıra) plan ve görev yazar; görevler zorluğa göre
// Haiku / Sonnet / Opus işçi ajanlarına dağılır (video fikir 3: otomatik model
// yönlendirme); işçi raporları ve önerileri odaya düşer (fikir 1: oturumlar arası
// mesajlaşma); pano canlı durumu gösterir (fikir 2: ajan panosu). Öneri kararı
// Salih'in elindedir (human in the loop).
import { atom, read, update } from 'claude-code'
import type { Register, EngineInterface } from 'claude-code'

import type { Oda, OdaGorev, OdaOneri, OdaTur, OdaTurTuru, OdaZorluk, AjanDurum } from '../types'

const PANE = 'jarvis-oda'
const STORE_AKTIF = 'oda:aktif'
const odaAtom = atom({ plugin: 'jarvis-oda', key: 'oda' } as const, null as Oda | null)
const ajanAtom = atom({ plugin: 'jarvis-oda', key: 'ajanlar' } as const, [] as AjanDurum[])

const MODEL_HARITASI: Record<OdaZorluk, string> = { kolay: 'haiku', orta: 'sonnet', zor: 'opus' }

type Engine = EngineInterface

function simdi(): string {
  return new Date().toISOString()
}

function kisa(metin: string, n = 160): string {
  const tek = metin.replace(/\s+/g, ' ').trim()
  return tek.length > n ? tek.slice(0, n - 1) + '…' : tek
}

async function odaKaydet($: Engine, oda: Oda): Promise<void> {
  await $.store.set('oda:' + oda.id, oda)
  await $.store.set(STORE_AKTIF, oda.id)
  await update($, odaAtom, () => oda)
  const kosan = oda.gorevler.filter(g => g.durum === 'kosuyor').length
  const bekleyen = oda.oneriler.filter(o => o.durum === 'bekliyor').length
  $.ui.status(`oda ${oda.baslik}: ${kosan} koşuyor · ${bekleyen} öneri bekliyor`)
}

async function odaYukle($: Engine): Promise<Oda | null> {
  const sicak = await read($, odaAtom)
  if (sicak) return sicak
  const id = (await $.store.get(STORE_AKTIF)) as string | undefined
  if (!id) return null
  const oda = (await $.store.get('oda:' + id)) as Oda | undefined
  if (oda) await update($, odaAtom, () => oda)
  return oda ?? null
}

function turEkle(oda: Oda, kim: string, tur: OdaTurTuru, metin: string, gorevId?: number): Oda {
  const yeni: OdaTur = { ts: simdi(), kim, tur, metin, gorevId }
  return { ...oda, turlar: [...oda.turlar, yeni].slice(-300) }
}

function odaMetni(oda: Oda, son = 12): string {
  const satirlar: string[] = [`# Oda: ${oda.baslik} (${oda.id}) · açılış ${oda.acilis}`]
  satirlar.push('## Görevler')
  if (oda.gorevler.length === 0) satirlar.push('(yok)')
  for (const g of oda.gorevler) {
    satirlar.push(`- #${g.id} [${g.durum}] ${g.baslik} · ${g.zorluk}→${g.model}${g.agentId ? ' · ajan ' + g.agentId : ''}`)
    if (g.sonuc) satirlar.push('  sonuç: ' + kisa(g.sonuc, 400))
  }
  const bekleyen = oda.oneriler.filter(o => o.durum === 'bekliyor')
  satirlar.push(`## Öneriler (bekleyen ${bekleyen.length})`)
  for (const o of oda.oneriler.slice(-10)) satirlar.push(`- Ö${o.id} [${o.durum}] ${o.kim}: ${kisa(o.metin, 200)} · gerekçe: ${kisa(o.gerekce, 120)}${o.not ? ' · not: ' + o.not : ''}`)
  satirlar.push(`## Son ${son} tur`)
  for (const t of oda.turlar.slice(-son)) satirlar.push(`- ${t.ts.slice(11, 19)} ${t.kim} [${t.tur}]${t.gorevId ? ' #' + t.gorevId : ''}: ${kisa(t.metin, 300)}`)
  return satirlar.join('\n')
}

function isciEmri(oda: Oda, g: OdaGorev): string {
  const plan = oda.turlar.filter(t => t.tur === 'plan').slice(-3).map(t => '- ' + t.metin).join('\n')
  return [
    `Sen "${oda.baslik}" odasının işçi ajanısın (görev #${g.id}, model ${g.model}). Dil: Türkçe; kod tanımlayıcıları aslıyla.`,
    'Jarvis (ana-sıra) planladı, sen uygularsın. Yalnız bu görevi yap; kapsam dışına çıkma; sormadan tasarım kararı değiştirme.',
    'Bir karar gerekiyorsa işi durdurma: mcp__jarvis-oda__oda_oneri aracıyla öneri bırak (metin + gerekçe), varsayılan yolu uygulayıp raporunda belirt.',
    'Ara durum için mcp__jarvis-oda__oda_rapor aracını kullanabilirsin (kısa, çıplak veri).',
    'Son cevabın rapordur: ne yaptın · dokunulan dosyalar (tam yol) · doğrulama kanıtı (komut + çıktı özeti) · açık kalan. Övgü yok, kısa cümleler.',
    plan ? '\nOda planı (son 3):\n' + plan : '',
    '\n## Görev\n' + g.emir,
  ].join('\n')
}

export const register: Register = (on, options) => {
  const otoUyandir = (options as { otoUyandir?: boolean } | undefined)?.otoUyandir ?? true

  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'oda', description: 'Oda panosunu açar (Jarvis planlar, işçiler uygular).' })
    const ortak = { isDeferred: false as const }
    await $.tool.register({
      ...ortak,
      name: 'oda_ac',
      description: 'Yeni oda açar ya da verilen başlıkla aktif odayı değiştirir. Oda = plan + görevler + işçi raporları + öneriler. Jarvis (ana-sıra) çağırır.',
      inputSchema: { type: 'object', properties: { baslik: { type: 'string', description: 'Oda başlığı (tek satır)' } }, required: ['baslik'] },
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
        'Aktif odada görev açar ve işçi ajanı arka planda başlatır. Model zorluğa göre seçilir: kolay→haiku, orta→sonnet, zor→opus (model alanı verilirse o kazanır). Birden çok çağrı paralel koşar. Görev bitince rapor odaya düşer ve Jarvis uyandırılır.',
      inputSchema: {
        type: 'object',
        properties: {
          baslik: { type: 'string', description: 'Kısa görev adı' },
          emir: { type: 'string', description: 'İşçinin tam emri: amaç, dosyalar, done koşulu, doğrulama' },
          zorluk: { type: 'string', enum: ['kolay', 'orta', 'zor'] },
          model: { type: 'string', description: 'İsteğe bağlı: haiku | sonnet | opus' },
        },
        required: ['baslik', 'emir', 'zorluk'],
      },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_oku',
      description: 'Aktif odanın durumunu metin olarak döndürür: görevler + durumları, bekleyen öneriler, son turlar.',
      inputSchema: { type: 'object', properties: { son: { type: 'integer', description: 'Kaç tur (varsayılan 12)' } } },
    })
    await $.tool.register({
      ...ortak,
      name: 'oda_oneri_karar',
      description: 'Bekleyen bir öneriyi kabul/ret eder (Jarvis ya da Salih adına). Karar odaya tur olarak düşer.',
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
      description: 'İşçi ajan ara durum raporu düşer (kısa). Son rapor olarak ajanın final cevabı otomatik kaydedilir, bunu çağırmak gerekmez.',
      inputSchema: { type: 'object', properties: { metin: { type: 'string' } }, required: ['metin'] },
    })

    const oda = await odaYukle($)
    if (oda) $.ui.status(`oda ${oda.baslik}: ${oda.gorevler.filter(g => g.durum === 'kosuyor').length} koşuyor`)
    void $.ui.open({ id: PANE, title: 'Oda' })

    // Ajan durumlarını 3 sn'de bir panoya yansıt (yalnız koşan görev varken).
    $.clock.every(3000, async () => {
      const o = await read($, odaAtom)
      if (!o || !o.gorevler.some(g => g.durum === 'kosuyor')) return
      const liste = await $.agent.list()
      const ajanlar: AjanDurum[] = []
      for (const g of o.gorevler) {
        if (!g.agentId) continue
        const a = liste.find(x => x.id === g.agentId)
        ajanlar.push({ agentId: g.agentId, status: a?.status ?? 'bilinmiyor', gorevId: g.id })
      }
      await update($, ajanAtom, () => ajanlar)
    })

    return next(e)
  })

  on('prompt.compose', async ($, e, next) => {
    const r = await next(e)
    const text = [
      '# jarvis-oda (mod)',
      'Oda = Jarvis planlar, işçi ajanlar uygular. Araçlar: oda_ac(baslik) · oda_plan(metin) · oda_gorev_ver(baslik, emir, zorluk: kolay|orta|zor → haiku|sonnet|opus) · oda_oku · oda_oneri_karar(oneriId, kabul|ret). Çok-ajanlı iş: planı oda_plan ile yaz, görevleri paralel oda_gorev_ver ile aç, raporları oda_oku ile topla. İşçi raporu geldiğinde kuyruğa "[oda]" ile başlayan mesaj düşer; onu görev raporu olarak oku, gerekirse sonraki görevi ver. Öneri kararı Salih\'indir: bekleyen öneriyi Salih\'e tek satırda sun.',
    ].join('\n')
    return { sections: [...r.sections, { id: 'jarvis-oda', text, scope: 'session' as const }] }
  })

  on('command.run', { command: 'oda' }, async $ => {
    await $.ui.open({ id: PANE, title: 'Oda', focus: true })
    const oda = await odaYukle($)
    return { text: oda ? odaMetni(oda, 6) : 'Oda yok. Jarvis oda_ac ile açar.' }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_ac' }, async ($, e) => {
    const baslik = String((e as { baslik?: string }).baslik ?? 'oda')
    const id = new Date().toISOString().slice(0, 16).replace(/[-:T]/g, '') + '-' + baslik.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 24)
    const oda: Oda = { id, baslik, acilis: simdi(), turlar: [], gorevler: [], oneriler: [] }
    await odaKaydet($, turEkle(oda, 'jarvis', 'not', 'Oda açıldı: ' + baslik))
    void $.ui.open({ id: PANE, title: 'Oda' })
    return { result: `Oda açıldı: ${baslik} (id ${id}). Şimdi oda_plan ile planı yaz, oda_gorev_ver ile görevleri dağıt.` }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_plan' }, async ($, e) => {
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok; önce oda_ac.' }
    await odaKaydet($, turEkle(oda, 'jarvis', 'plan', String((e as { metin?: string }).metin ?? '')))
    return { result: 'Plan turu yazıldı.' }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_gorev_ver' }, async ($, e) => {
    const g0 = e as { baslik?: string; emir?: string; zorluk?: OdaZorluk; model?: string }
    let oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok; önce oda_ac.' }
    const zorluk: OdaZorluk = g0.zorluk === 'kolay' || g0.zorluk === 'zor' ? g0.zorluk : 'orta'
    const model = g0.model && g0.model.trim() ? g0.model.trim() : MODEL_HARITASI[zorluk]
    const id = oda.gorevler.length + 1
    const gorev: OdaGorev = { id, baslik: String(g0.baslik ?? 'görev ' + id), emir: String(g0.emir ?? ''), zorluk, model, durum: 'bekliyor', acilis: simdi() }
    oda = { ...oda, gorevler: [...oda.gorevler, gorev] }
    oda = turEkle(oda, 'jarvis', 'gorev', `#${id} ${gorev.baslik} → ${model}`, id)
    await odaKaydet($, oda)

    const spawn = await $.agent.spawn({
      prompt: isciEmri(oda, gorev),
      description: `oda #${id} ${kisa(gorev.baslik, 40)}`,
      subagentType: 'general-purpose',
      model,
      name: `oda-${id}`,
    })
    const taze = (await odaYukle($)) ?? oda
    if ('deny' in spawn && spawn.deny) {
      const hata = { ...taze, gorevler: taze.gorevler.map(g => (g.id === id ? { ...g, durum: 'hata' as const, sonuc: 'spawn reddi: ' + spawn.deny, kapanis: simdi() } : g)) }
      await odaKaydet($, turEkle(hata, 'oda', 'not', `#${id} başlatılamadı: ${spawn.deny}`, id))
      return { result: `Görev #${id} başlatılamadı: ${spawn.deny}` }
    }
    const agentId = (spawn as { agentId?: string }).agentId
    const kosan = { ...taze, gorevler: taze.gorevler.map(g => (g.id === id ? { ...g, durum: 'kosuyor' as const, agentId, model: (spawn as { model?: string }).model ?? model } : g)) }
    await odaKaydet($, kosan)
    return { result: `Görev #${id} "${gorev.baslik}" ${model} işçisinde koşuyor (ajan ${agentId ?? '?'}). Bitince rapor odaya düşer; beklemeden başka görev verebilirsin.` }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_oku' }, async ($, e) => {
    const oda = await odaYukle($)
    if (!oda) return { result: 'Oda yok; önce oda_ac.' }
    const son = Number((e as { son?: number }).son ?? 12)
    return { result: odaMetni(oda, Number.isFinite(son) && son > 0 ? son : 12) }
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
    await odaKaydet($, turEkle(oda, gorev ? `işçi #${gorev.id}` : 'jarvis', 'rapor', String(r.metin ?? ''), gorev?.id))
    return { result: 'Rapor düştü.' }
  })

  // İşçi ajanın final cevabı = görev raporu.
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
    if (otoUyandir) {
      const ozet = `[oda] görev #${gorev.id} "${gorev.baslik}" ${basarili ? 'bitti' : 'hata'} (${gorev.model}). Rapor:\n${kisa(sonuc, 1500)}\n\nKalan koşan: ${yeni.gorevler.filter(g => g.durum === 'kosuyor').length} · bekleyen öneri: ${yeni.oneriler.filter(o => o.durum === 'bekliyor').length}. oda_oku ile tamamını gör; sırada iş varsa oda_gorev_ver.`
      void $.prompt.submit({ text: ozet }).catch(() => undefined)
    }
    return r
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => {
    const { Box, Text, Button } = $.ui.resolve(e)
    const oda = await read($, odaAtom)
    const ajanlar = await read($, ajanAtom)
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
    return (
      <Box flexDirection="column" padding={1} gap={1}>
        <Box flexDirection="row" justifyContent="space-between">
          <Text bold>Oda · {oda.baslik}</Text>
          <Button key="yenile" plain onPress={() => $.ui.invalidate('ui.render')}>
            ⟳
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
                  <Text color={renk(g.durum)}>{g.durum === 'kosuyor' ? '●' : g.durum === 'bitti' ? '✓' : g.durum === 'hata' ? '✗' : '○'}</Text> #{g.id} {g.baslik} <Text dimColor>· {g.zorluk}→{g.model}{a ? ' · ' + a.status : ''}</Text>
                </Text>
                {g.sonuc && (
                  <Text dimColor>
                    {'   '}
                    {kisa(g.sonuc, 110)}
                  </Text>
                )}
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
            Son turlar
          </Text>
          {oda.turlar.slice(-8).map(t => (
            <Text dimColor={t.tur === 'not'}>
              <Text dimColor>{t.ts.slice(11, 16)}</Text> {t.kim} <Text dimColor>[{t.tur}]</Text> {kisa(t.metin, 90)}
            </Text>
          ))}
        </Box>
      </Box>
    )
  })
}
