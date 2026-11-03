// jarvis-graf v0.2: akış grafı paneli (Salih 2026-10-27; Karar 122/124/125; v0.2 2026-11-03).
// Bu dosya yalnız kayıt yapar; mantık hooks/src/ altında: durum (veri) · metin (satır düzeni, detay) · cizim (SVG) · araclar (süreç, eylem) · pano (çizim) · ortak.
// v0.2: seans şeritli SVG, tıklanabilir seans ızgarası, zengin detay (kütük olayları, defter paragrafı, kayıt linki),
// HTML aç onarımı (py -3, kalıcı bağlantı), oda köprüsü (ortak/graf-secim.json) ve /graf is:<id>.
import type { Register } from 'claude-code'

import { PANE, grafYukle, kopruOku, grafOku } from './src/durum'
import { panoCiz } from './src/pano'
import { disaridanSec, argumandanId } from './src/araclar'

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'graf', description: 'Akış grafı panelini açar; argüman is:<id>, #<id> ya da seans:<ad> o düğümü seçer.', argumentHint: '[is:<id>]', immediate: true })
    await grafYukle($, true)
    await kopruOku($, true) // açılıştaki eski köprü seçimini işlenmiş say
    void $.ui.open({ id: PANE, title: 'Akış grafı' }).catch(() => undefined)
    $.clock.every(10000, () => grafYukle($))
    $.clock.every(2000, async () => {
      const id = await kopruOku($)
      if (id) {
        await grafYukle($, true)
        await disaridanSec($, id)
      }
    })
    return next(e)
  })

  on('command.run', { command: 'graf' }, async ($, e) => {
    await grafYukle($, true)
    const id = argumandanId(e.args ?? '')
    if (id) await disaridanSec($, id)
    else await $.ui.open({ id: PANE, title: 'Akış grafı', focus: true }).catch(() => undefined)
    const graf = await grafOku($)
    if (!graf) return { text: 'Graf okunamadı.' }
    const acik = graf.dugumler.filter(n => n.tur === 'is' && (n.durum === 'acik' || n.durum === 'islemde'))
    return { text: `Akış grafı paneli açık: ${graf.dugumler.length} düğüm, ${graf.kenarlar.length} kenar, ${acik.length} açık iş${id ? `; seçili ${id}` : ''}.` }
  })

  on('ui.render', { component: 'Pane', requestId: PANE }, async ($, e) => panoCiz($, e))
}
