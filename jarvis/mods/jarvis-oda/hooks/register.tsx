// jarvis-oda v0.6: oda modu (Salih 2026-10-27, Karar 126; v0.5 2026-11-03 tanrısal bakış + iş nodu sınıfı).
// Bu dosya yalnız kayıt yapar; mantık hooks/src/ altında: durum (veri) · araclar (yazan taraf) · metin (model metni) · pano (çizim) · ortak.
// Sürüm tarihçesi README.md'de; v0.5: işçiye tıkla → işçi transkripti, kaydırılabilir sohbet/akış, katlanır bölümler,
// [#N · başlık · sınıf] etiketleri, iş nodu sınıfı (izole/planli/dosyali/rol) + bütçe + kapsam kapısı, kütük/graf köprüsü.
import type { Register } from 'claude-code'

import { PANE, odaYukle, kosan, hareketleriOku, hareketEkle } from './src/durum'
import { PROMPT_BOLUMU, odaMetni } from './src/metin'
import { panoCiz } from './src/pano'
import {
  ARACLAR,
  type ModAyar,
  odaAc,
  planYaz,
  sinirAyarla,
  sohbetGonder,
  gorevVer,
  odaOku,
  oneriKarar,
  oneriBirak,
  raporDus,
  gorevBitti,
  ajanYokla,
  isciAracOncesi,
} from './src/araclar'
import { gelenleriIsle, gidenleriOku, odayaKatil, disMesaj, aktifIsaretle } from './src/dis'

export const register: Register = (on, options) => {
  const o = (options ?? {}) as { otoUyandir?: boolean; maksParalel?: number; durumKaydi?: boolean; alan?: string }
  const ayar: ModAyar = {
    otoUyandir: o.otoUyandir ?? true,
    varsayilanMaks: Math.max(1, Math.min(12, Number(o.maksParalel ?? 3) || 3)),
    durumKaydi: o.durumKaydi ?? true,
    alan: (o.alan ?? 'jarvis').trim() || 'jarvis',
  }

  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'oda', description: 'Oda panosunu açar (Jarvis planlar, işçiler uygular, ortak sohbet).' })
    for (const a of ARACLAR) await $.tool.register(a)
    const oda = await odaYukle($)
    if (oda) {
      $.ui.status(`oda ${oda.baslik}: ${kosan(oda)}/${oda.maksParalel} koşuyor`)
      await aktifIsaretle($, oda)
    }
    void $.ui.open({ id: PANE, title: 'Oda', rows: 40 }).catch(() => undefined)
    $.clock.every(3000, async () => {
      await ajanYokla($).catch(() => undefined)
      await gelenleriIsle($, ayar.otoUyandir).catch(() => undefined)
      await gidenleriOku($).catch(() => undefined)
    })
    return next(e)
  })

  // İşçi akışı + A5 kapısı: her araç çağrısı hareket olur, sayılır; kapsam/bütçe dışı ise reddedilir.
  on('tool.call', async ($, e, next) => {
    if (!e.agentId) return next(e)
    const ret = await isciAracOncesi($, e.agentId, e as unknown as Record<string, unknown>).catch(() => undefined)
    if (ret) {
      await hareketEkle($, e.agentId, 'arac', '✗ ' + ret).catch(() => undefined)
      return { deny: ret }
    }
    const r = await next(e)
    if ('deny' in r && r.deny) await hareketEkle($, e.agentId, 'arac', `✗ reddedildi: ${r.deny}`).catch(() => undefined)
    else if ('isError' in r && r.isError) await hareketEkle($, e.agentId, 'arac', '✗ hata').catch(() => undefined)
    return r
  })

  // İşçi akışı: model metni blok bitiminde hareket olur.
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
    return { sections: [...r.sections, { id: 'jarvis-oda', text: PROMPT_BOLUMU, scope: 'session' as const }] }
  })

  on('command.run', { command: 'oda' }, async $ => {
    await $.ui.open({ id: PANE, title: 'Oda', focus: true, rows: 40 })
    const oda = await odaYukle($)
    return { text: oda ? odaMetni(oda, 6, await hareketleriOku($)) : 'Oda yok. Jarvis oda_ac ile açar.' }
  })

  on('tool.call', { tool: 'mcp__jarvis-oda__oda_ac' }, async ($, e) => ({ result: await odaAc($, e as { baslik?: string; maksParalel?: number }, ayar) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_plan' }, async ($, e) => ({ result: await planYaz($, String((e as { metin?: string }).metin ?? '')) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_ayar' }, async ($, e) => ({ result: await sinirAyarla($, 'jarvis', Number((e as { maksParalel?: number }).maksParalel)) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_sohbet' }, async ($, e) => {
    const s = e as { metin?: string; hedef?: string }
    return { result: await sohbetGonder($, 'jarvis', String(s.metin ?? ''), s.hedef) }
  })
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_gorev_ver' }, async ($, e) => ({ result: await gorevVer($, e as Parameters<typeof gorevVer>[1], ayar) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_oku' }, async ($, e) => ({ result: await odaOku($, Number((e as { son?: number }).son ?? 12), await hareketleriOku($)) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_oneri_karar' }, async ($, e) => {
    const k = e as { oneriId?: number; karar?: string; not?: string }
    return { result: await oneriKarar($, 'jarvis', Number(k.oneriId), k.karar === 'ret' ? 'ret' : 'kabul', k.not) }
  })
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_oneri' }, async ($, e) => ({ result: await oneriBirak($, e as { metin?: string; gerekce?: string; agentId?: string }) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_katil' }, async ($, e) => ({ result: await odayaKatil($, e as Parameters<typeof odayaKatil>[1]) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_mesaj' }, async ($, e) => ({ result: await disMesaj($, e as Parameters<typeof disMesaj>[1]) }))
  on('tool.call', { tool: 'mcp__jarvis-oda__oda_rapor' }, async ($, e) => ({ result: await raporDus($, e as { metin?: string; agentId?: string }) }))

  on('turn.complete', async ($, e, next) => {
    const r = await next(e)
    if (e.agentId) await gorevBitti($, e as unknown as Parameters<typeof gorevBitti>[1], ayar).catch(err => $.ui.log('oda gorevBitti: ' + String(err)))
    return r
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => panoCiz($, e))
}
