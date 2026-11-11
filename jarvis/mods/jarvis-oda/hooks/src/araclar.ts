// araclar.ts: odanın yazan tarafı; araç tanımları ve işleyicileri, görev başlatma/kuyruk, sohbet,
// kütük köprüsü (durum.exe, A4), kapsam ve bütçe kapısı (A5), pano eylemleri (A1-A3, A7).
import type { EngineInterface, ToolSpec } from 'claude-code'

import type { Oda, OdaGorev, OdaOneri, OdaZorluk, OdaSinif, OdaBolum, OdaListe, OdaPano, AjanDurum } from '../../types'
import {
  odaSicak,
  ajanlariYaz,
  panoGuncelle,
  PENCERE_BOY,
  SINIF_BUTCE,
  odaKaydet,
  odaYukle,
  turEkle,
  kosan,
  kuyrukSayisi,
  bekleyenOneri,
  hareketEkle,
  sinifi,
  PANE,
} from './durum'
import { isciEmri, odaMetni, gorevRaporu, aracOzeti, altOdaDokumu } from './metin'
import { kisa, simdi, yolMutlak, yolNormal } from './ortak'
import { aktifIsaretle, gidenYaz, oturumAdi } from './dis'

const MODEL_HARITASI: Record<OdaZorluk, string> = { kolay: 'haiku', orta: 'sonnet', zor: 'opus' }
const SINIFLAR: readonly OdaSinif[] = ['izole', 'planli', 'dosyali', 'rol']
const YAZAN_ARACLAR = new Set(['Edit', 'Write', 'NotebookEdit', 'MultiEdit'])

export type ModAyar = { otoUyandir: boolean; varsayilanMaks: number; durumKaydi: boolean; alan: string }

// ---------- araç tanımları ----------

const ortak = { isDeferred: false as const }
export const ARACLAR: ToolSpec[] = [
  {
    ...ortak,
    name: 'oda_ac',
    description: 'Yeni oda açar ya da verilen başlıkla aktif odayı değiştirir. Oda = plan + görevler + işçi raporları + öneriler + ortak sohbet. Jarvis (ana-sıra) çağırır.',
    inputSchema: { type: 'object', properties: { baslik: { type: 'string', description: 'Oda başlığı (tek satır)' }, maksParalel: { type: 'integer', description: 'Aynı anda koşan işçi üst sınırı (varsayılan 3)' } }, required: ['baslik'] },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_plan',
    description: 'Aktif odaya plan turu yazar (Jarvis). planli sınıfı görevlerin emrine son 3 plan turu eklenir; izole/dosyali/rol görevlerine eklenmez.',
    inputSchema: { type: 'object', properties: { metin: { type: 'string' } }, required: ['metin'] },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_gorev_ver',
    description:
      'Aktif odada görev (iş nodu) açar; maksParalel sınırı altındaysa işçi ajanı hemen arka planda başlatır, değilse kuyruğa alır. Model zorluğa göre: kolay→haiku, orta→sonnet, zor→opus (model alanı verilirse o kazanır). sinif işçinin göreceği bağlamı belirler (bağlam karışması freni): izole = yalnız emir · planli = emir + son 3 plan turu · dosyali = emir + dosyalar listesi (≤ 4; liste dışı Edit/Write reddedilir) · rol = ajan alanındaki .claude/agents/<ad>.md rolü, oda bağlamı yok. done tek cümle zorunlu. butce araç çağrısı tavanı (varsayılan izole 10 · dosyali 15 · planli/rol 20; aşımda uyarı, 1.5 katında araçlar kapanır ve görev hata). Görev durum kütüğüne iş olarak yazılır (isId verilirse o işe bağlanır). Bitince rapor odaya düşer ve Jarvis uyandırılır.',
    inputSchema: {
      type: 'object',
      properties: {
        baslik: { type: 'string', description: 'Kısa görev adı' },
        emir: { type: 'string', description: 'İşçinin tam emri: amaç, dosyalar, adımlar, doğrulama' },
        zorluk: { type: 'string', enum: ['kolay', 'orta', 'zor'] },
        sinif: { type: 'string', enum: ['izole', 'planli', 'dosyali', 'rol'], description: 'İş nodu sınıfı; ajan verilirse rol sayılır' },
        done: { type: 'string', description: 'Tek cümle done koşulu' },
        dosyalar: { type: 'array', items: { type: 'string' }, description: 'dosyali sınıfında yazma izni olan dosyalar (≤ 4; mutlak ya da cwd-göreli)' },
        butce: { type: 'integer', description: 'İsteğe bağlı araç çağrısı tavanı' },
        isId: { type: 'integer', description: 'İsteğe bağlı: bağlanacak mevcut durum kütüğü iş numarası' },
        model: { type: 'string', description: 'İsteğe bağlı: haiku | sonnet | opus' },
        ajan: { type: 'string', description: 'İsteğe bağlı: .claude/agents/<ad>.md ajan tipi (ör. hakem, sokrates); verilirse sinif = rol.' },
      },
      required: ['baslik', 'emir', 'zorluk', 'sinif', 'done'],
    },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_oku',
    description: 'Aktif odanın durumunu metin olarak döndürür: paralel sayacı, görevler (sınıf, done, çağrı sayacı, iş numarası) + her işçinin son 3 hareketi, bekleyen öneriler, alt-odalar, son turlar (sohbet dahil). gorevId verilirse o görevin final raporunun tam metni döner.',
    inputSchema: {
      type: 'object',
      properties: {
        son: { type: 'integer', description: 'Kaç tur (varsayılan 12)' },
        gorevId: { type: 'integer', description: 'İsteğe bağlı: verilirse yalnız o görevin final raporunun tam metni döner (kesilmez)' },
        altOdaId: { type: 'integer', description: 'İsteğe bağlı: verilirse o alt-odanın tam dökümü döner (turlar, son konumlar, hakem raporu; kesilmez)' },
      },
    },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_ayar',
    description: 'Aktif odanın anlık paralel işçi üst sınırını değiştirir (maksParalel 1-12). Sınır düşerse koşanlar durmaz, yeni başlatma durur; yükselirse kuyruk işlenir.',
    inputSchema: { type: 'object', properties: { maksParalel: { type: 'integer' } }, required: ['maksParalel'] },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_sohbet',
    description: 'Ortak sohbete mesaj yazar: koşan tüm işçilere (ya da "#N" ile tek işçiye) iletilir; işçiler oda_rapor ile cevaplar. hedef "@<oturum>" dış oturuma yazar (ortak/oda/<id>/giden.jsonl); sonuç SendMessage ile de iletmeni ister.',
    inputSchema: { type: 'object', properties: { metin: { type: 'string' }, hedef: { type: 'string', description: 'İsteğe bağlı "#N" (tek işçi) ya da "@<oturum>" (dış oturum); boşsa herkes' } }, required: ['metin'] },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_oneri_karar',
    description: 'Bekleyen bir öneriyi kabul/ret eder (Jarvis ya da Salih adına). Karar odaya tur olarak düşer ve ilgili işçiye iletilir.',
    inputSchema: { type: 'object', properties: { oneriId: { type: 'integer' }, karar: { type: 'string', enum: ['kabul', 'ret'] }, not: { type: 'string' } }, required: ['oneriId', 'karar'] },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_oneri',
    description: 'İşçi ajan karar gerektiren noktada öneri bırakır (metin + gerekçe). Karar Jarvis/Salih tarafından panodan ya da oda_oneri_karar ile verilir.',
    inputSchema: { type: 'object', properties: { metin: { type: 'string' }, gerekce: { type: 'string' } }, required: ['metin', 'gerekce'] },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_rapor',
    description: 'İşçi ajan ara durum raporu ya da sohbet cevabı düşer (kısa). Final cevap otomatik kaydedilir.',
    inputSchema: { type: 'object', properties: { metin: { type: 'string' } }, required: ['metin'] },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_katil',
    description: 'Dış oturum (fork, öğrenme sekmesi, alan ajanı) kendini aktif odaya kalıcı oturum olarak kaydeder; kanal dosyadır (ortak/oda/<odaId>/gelen-<oturum>.jsonl). Odadan gelen mesajlar bu oturumun sohbetine "[oda]" ile düşer. ayril: true odadan ayrılır (kayıt silinmez).',
    inputSchema: {
      type: 'object',
      properties: {
        oturum: { type: 'string', description: 'Oturum adı (ör. claude-mods); odada "oturum <ad>" görünür' },
        rol: { type: 'string', description: 'Bu oturumun odadaki rolü (tek cümle)' },
        dosyalar: { type: 'array', items: { type: 'string' }, description: 'Bu oturumun yazdığı dosyalar' },
        ayril: { type: 'boolean', description: 'true: odadan ayrıl' },
      },
    },
  } as ToolSpec,
  {
    ...ortak,
    name: 'oda_mesaj',
    description: "Katılmış dış oturum odaya yazar: sohbet, rapor ya da öneri (öneri için gerekce). Ev sahibi oda 3 sn içinde okur; rapor ve öneri Jarvis'i uyandırır.",
    inputSchema: {
      type: 'object',
      properties: { tur: { type: 'string', enum: ['sohbet', 'rapor', 'oneri'] }, metin: { type: 'string' }, gerekce: { type: 'string' }, gorevId: { type: 'integer' } },
      required: ['tur', 'metin'],
    },
  } as ToolSpec,
]

// ---------- depo yolu ve kütük köprüsü (A4) ----------

/** cwd'den köke kadar ortak/durum-olay.jsonl olan ilk dizin (depo kökü). */
export async function depoBul($: EngineInterface): Promise<string | null> {
  try {
    return await depoAra($)
  } catch {
    return null // fs erişimi olmayan ortam (claude plugin test)
  }
}

async function depoAra($: EngineInterface): Promise<string | null> {
  const onbellek = (await $.store.get('oda:depo')) as string | undefined
  if (onbellek && (await $.fs.exists(onbellek + '/ortak/durum-olay.jsonl'))) return onbellek
  let dizin = (await $.session.cwd()).replace(/\\/g, '/').replace(/\/+$/, '')
  for (let i = 0; i < 32 && dizin; i++) {
    if (await $.fs.exists(dizin + '/ortak/durum-olay.jsonl')) {
      await $.store.set('oda:depo', dizin)
      return dizin
    }
    const ust = dizin.replace(/\/[^/]*$/, '')
    if (ust === dizin || !ust.includes('/')) break
    dizin = ust
  }
  return null
}

export async function durumKos($: EngineInterface, argv: string[]): Promise<{ ok: boolean; cikti: string }> {
  const depo = await depoBul($)
  if (!depo) return { ok: false, cikti: 'depo (ortak/durum-olay.jsonl) bulunamadı' }
  const exe = depo + '/target/release/durum.exe'
  if (!(await $.fs.exists(exe))) return { ok: false, cikti: exe + ' yok' }
  try {
    const r = await $.process.run([exe, ...argv], { cwd: depo, timeoutMs: 30000 })
    return { ok: r.exitCode === 0, cikti: (r.stdout + r.stderr).trim() }
  } catch (err) {
    return { ok: false, cikti: String(err) }
  }
}

/** Görevi kütüğe iş olarak açar; `#85 acik jarvis` çıktısından numarayı alır, grafı tazeler. */
async function kutugeAc($: EngineInterface, oda: Oda, g: OdaGorev, alan: string): Promise<{ isId?: number; not: string }> {
  const sonraki = kisa(g.done || g.emir.split(/(?<=[.!?])\s/)[0] || g.emir, 200)
  const r = await durumKos($, ['ac', '--alan', alan, '--is', `oda #${g.id} ${g.baslik}`, '--sonraki', sonraki, '--oturum', 'oda-' + oda.id])
  const no = /^#(\d+)/.exec(r.cikti)?.[1]
  if (!r.ok || !no) return { not: 'kütük açılamadı: ' + kisa(r.cikti, 160) }
  await durumKos($, ['graf'])
  return { isId: Number(no), not: `kütük iş #${no}` }
}

/** K52: işçi başlarken kütük işi işleme alınır (`al`; oturum = oda kimliği). Dönüş: odaya yazılacak not. */
async function kutukAl($: EngineInterface, oda: Oda, g: OdaGorev): Promise<string | undefined> {
  if (!g.isId) return undefined
  const r = await durumKos($, ['al', String(g.isId), '--oturum', 'oda-' + oda.id])
  return r.ok ? `kütük iş #${g.isId} işlemde` : `kütük iş #${g.isId} işleme alınamadı: ${kisa(r.cikti, 160)}`
}

/**
 * K52: başarılı işçi bitişinde kütük işi kapanır. `bitir` yalnız `islemde` işi kapatır; `al` başlangıçta koştu.
 * Kanıt oda ve görev numarasıdır; Jarvis gerçek commit kanıtını ayrıca ekler.
 */
async function kutukBitir($: EngineInterface, oda: Oda, g: OdaGorev): Promise<string | undefined> {
  if (!g.isId) return undefined
  const r = await durumKos($, ['bitir', String(g.isId), '--kanit', `oda ${oda.id} görev #${g.id}`])
  if (!r.ok) return `kütük iş #${g.isId} kapatılamadı: ${kisa(r.cikti, 160)}`
  await durumKos($, ['graf'])
  return `kütük iş #${g.isId} kapandı (kanıt: oda ${oda.id} görev #${g.id})`
}

/** K52: kütük notunu göreve ve oda turlarına yazar (taze oda üstüne). */
async function kutukNotuYaz($: EngineInterface, gorevId: number, not: string): Promise<Oda | null> {
  const oda = await odaYukle($)
  if (!oda) return null
  const yeni = turEkle({ ...oda, gorevler: oda.gorevler.map(g => (g.id === gorevId ? { ...g, kutukNot: not } : g)) }, 'oda', 'not', `#${gorevId} ${not}`, gorevId)
  await kaydet($, yeni)
  return yeni
}

/** B8: oda kaydını ortak/oda/<id>.json olarak dışa yazar (HTML "Oda" sekmesi okur). */
export async function odaDisaYaz($: EngineInterface, oda: Oda): Promise<void> {
  const depo = await depoBul($)
  if (!depo) return
  await $.fs.write(`${depo}/ortak/oda/${oda.id}.json`, JSON.stringify(oda, null, 1)).catch(() => undefined)
}

/** Tüm yazımlar buradan geçer: store + atom + dışa yazım. */
export async function kaydet($: EngineInterface, oda: Oda): Promise<void> {
  await odaKaydet($, oda)
  await odaDisaYaz($, oda)
}

// ---------- görev yaşam döngüsü ----------

async function gorevBaslat($: EngineInterface, oda: Oda, id: number): Promise<Oda> {
  const gorev = oda.gorevler.find(g => g.id === id)
  if (!gorev) return oda
  const spawn = await $.agent
    .spawn({
      // B9: alt-oda çağrısının emri mod şablonudur (metin.ts), olduğu gibi gider.
      prompt: gorev.altOda ? gorev.emir : isciEmri(oda, gorev),
      description: `oda #${id} ${kisa(gorev.baslik, 40)}`,
      subagentType: gorev.ajan ?? 'general-purpose',
      ...(gorev.ajan && !gorev.modelAcik ? {} : { model: gorev.model }),
      name: `oda-${id}`,
    })
    .catch((err: unknown) => ({ deny: String(err) }))
  const taze = (await odaYukle($)) ?? oda
  if ('deny' in spawn && spawn.deny) {
    const hata = { ...taze, gorevler: taze.gorevler.map(g => (g.id === id ? { ...g, durum: 'hata' as const, sonuc: 'spawn reddi: ' + spawn.deny, kapanis: simdi() } : g)) }
    const yeni = turEkle(hata, 'oda', 'not', `#${id} başlatılamadı: ${spawn.deny}`, id)
    await kaydet($, yeni)
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
  await kaydet($, yeni)
  // K52: kütük işi işleme alınır; sonuç göreve ve turlara not olarak düşer.
  const alNotu = await kutukAl($, yeni, gorev)
  if (alNotu) return (await kutukNotuYaz($, id, alNotu)) ?? yeni
  return yeni
}

/** Kuyruktaki görevleri maksParalel sınırına kadar başlatır. */
export async function kuyrukIsle($: EngineInterface): Promise<Oda | null> {
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
export async function sohbetGonder($: EngineInterface, kim: string, metin: string, hedef?: string): Promise<string> {
  let oda = await odaYukle($)
  if (!oda) return 'Oda yok.'
  const m = metin.trim()
  if (!m) return 'Boş mesaj.'
  const hedefNo = /^#(\d+)/.exec(hedef ?? m)?.[1]
  const disHedef = /^@([\w-]+)/.exec(hedef ?? m)?.[1]
  oda = turEkle(oda, kim, 'sohbet', m, hedefNo ? Number(hedefNo) : undefined)
  await kaydet($, oda)
  // C1: dış oturumlar dosyadan okur; @ad tek oturuma, hedefsiz mesaj katılmış herkese.
  const katilmis = (oda.oturumlar ?? []).filter(o => o.durum === 'katildi')
  let disNot = ''
  if (disHedef) {
    const ad = oturumAdi(disHedef)
    const yazildi = await gidenYaz($, oda, kim, ad, m.replace(/^@[\w-]+\s*/, ''))
    disNot = yazildi ? ` Dış oturum "${ad}": giden.jsonl'a yazıldı; anında görmesi için SendMessage ile de ilet (to: "${ad}").` : ' Dış oturum: giden.jsonl yazılamadı.'
  } else if (!hedefNo && katilmis.length) {
    if (await gidenYaz($, oda, kim, '*', m)) disNot = ` Dış oturumlara (${katilmis.map(o => o.oturum).join(', ')}) giden.jsonl ile düştü.`
  }
  const alicilar = disHedef ? [] : oda.gorevler.filter(g => g.durum === 'kosuyor' && g.agentId && (!hedefNo || g.id === Number(hedefNo)))
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
    await $.session.append({ message: { type: 'user', content: [{ type: 'text', text: `[oda sohbet] ${kim}: ${m} (işçilere ulaştı: ${ulasan}/${alicilar.length})${disNot}` }] } }).catch(() => undefined)
  }
  return `Sohbet düştü; işçilere ulaştı: ${ulasan}/${alicilar.length}${hedefNo ? ' (hedef #' + hedefNo + ')' : ''}.${disNot}`
}

// ---------- araç işleyicileri ----------

export async function odaAc($: EngineInterface, a: { baslik?: string; maksParalel?: number }, ayar: ModAyar): Promise<string> {
  const baslik = String(a.baslik ?? 'oda')
  const id = new Date().toISOString().slice(0, 16).replace(/[-:T]/g, '') + '-' + baslik.toLowerCase().replace(/[^a-z0-9]+/g, '-').slice(0, 24)
  const maks = Math.max(1, Math.min(12, Number(a.maksParalel ?? ayar.varsayilanMaks) || ayar.varsayilanMaks))
  const oda: Oda = { id, baslik, acilis: simdi(), maksParalel: maks, turlar: [], gorevler: [], oneriler: [] }
  const acilan = turEkle(oda, 'jarvis', 'not', `Oda açıldı: ${baslik} (paralel sınır ${maks})`)
  await kaydet($, acilan)
  await aktifIsaretle($, acilan)
  await panoGuncelle($, p => ({ ...p, ofset: { sohbet: null, akis: null, olaylar: null }, genis: [] }))
  void $.ui.open({ id: PANE, title: 'Oda' }).catch(() => undefined)
  return `Oda açıldı: ${baslik} (id ${id}, paralel sınır ${maks}). Şimdi oda_plan ile planı yaz, oda_gorev_ver ile görevleri sınıflı dağıt.`
}

export async function planYaz($: EngineInterface, metin: string): Promise<string> {
  const oda = await odaYukle($)
  if (!oda) return 'Oda yok; önce oda_ac.'
  await kaydet($, turEkle(oda, 'jarvis', 'plan', metin))
  return 'Plan turu yazıldı.'
}

export async function sinirAyarla($: EngineInterface, kim: string, hedef: number | ((eski: number) => number)): Promise<string> {
  const oda = await odaYukle($)
  if (!oda) return 'Oda yok; önce oda_ac.'
  const istenen = typeof hedef === 'function' ? hedef(oda.maksParalel) : hedef
  const maks = Math.max(1, Math.min(12, Number(istenen) || oda.maksParalel))
  if (maks !== oda.maksParalel) await kaydet($, turEkle({ ...oda, maksParalel: maks }, kim, 'not', `paralel sınır ${oda.maksParalel} → ${maks}`))
  const son = await kuyrukIsle($)
  return `maksParalel = ${maks}; koşan ${son ? kosan(son) : 0}, kuyrukta ${son ? kuyrukSayisi(son) : 0}.`
}

type GorevGirdi = { baslik?: string; emir?: string; zorluk?: OdaZorluk; model?: string; ajan?: string; sinif?: string; done?: string; dosyalar?: unknown; butce?: number; isId?: number }

export async function gorevVer($: EngineInterface, g0: GorevGirdi, ayar: ModAyar): Promise<string> {
  let oda = await odaYukle($)
  if (!oda) return 'Oda yok; önce oda_ac.'
  const ajan = g0.ajan && /^[a-z0-9_-]+$/i.test(g0.ajan.trim()) ? g0.ajan.trim() : undefined
  const sinif: OdaSinif | undefined = ajan ? 'rol' : SINIFLAR.find(s => s === g0.sinif)
  if (!sinif) return 'Görev açılmadı: sinif gerekli (izole | planli | dosyali | rol).'
  if (sinif === 'rol' && !ajan) return 'Görev açılmadı: rol sınıfı ajan alanı ister (.claude/agents/<ad>.md).'
  const done = String(g0.done ?? '').trim()
  if (!done) return 'Görev açılmadı: done (tek cümle) gerekli.'
  const cwd = await $.session.cwd().catch(() => '')
  const dosyalar = Array.isArray(g0.dosyalar) ? (g0.dosyalar as unknown[]).filter((d): d is string => typeof d === 'string' && d.trim() !== '').map(d => yolMutlak(d.trim(), cwd)) : []
  if (sinif === 'dosyali' && dosyalar.length === 0) return 'Görev açılmadı: dosyali sınıfı dosyalar listesi ister (≤ 4).'
  if (sinif === 'dosyali' && dosyalar.length > 4) return `Görev açılmadı: dosyali sınıfında dosya listesi ≤ 4 olmalı (${dosyalar.length} verildi); görevi böl.`
  const zorluk: OdaZorluk = g0.zorluk === 'kolay' || g0.zorluk === 'zor' ? g0.zorluk : 'orta'
  const modelAcik = Boolean(g0.model && g0.model.trim())
  const model = modelAcik ? g0.model!.trim() : MODEL_HARITASI[zorluk]
  const butce = Math.max(3, Math.min(200, Number(g0.butce) || SINIF_BUTCE[sinif]))
  const id = oda.gorevler.length + 1
  let gorev: OdaGorev = {
    id,
    baslik: String(g0.baslik ?? 'görev ' + id),
    emir: String(g0.emir ?? ''),
    zorluk,
    model,
    sinif,
    done,
    butce,
    cagri: 0,
    ...(dosyalar.length ? { dosyalar } : {}),
    durum: 'bekliyor',
    acilis: simdi(),
    ...(ajan ? { ajan, modelAcik } : {}),
  }
  let kutukNotu = ''
  if (Number.isInteger(g0.isId) && Number(g0.isId) > 0) {
    gorev = { ...gorev, isId: Number(g0.isId) }
    kutukNotu = `kütük iş #${g0.isId} bağlandı`
  } else if (ayar.durumKaydi) {
    const k = await kutugeAc($, oda, gorev, ayar.alan)
    if (k.isId) gorev = { ...gorev, isId: k.isId }
    kutukNotu = k.not
  }
  oda = (await odaYukle($)) ?? oda
  const etiket = `#${id} [${sinif}] ${ajan ? '[' + ajan + '] ' : ''}${gorev.baslik} → ${!ajan || modelAcik ? model : 'model: ajan tanımı'} · bütçe ${butce}${kutukNotu ? ' · ' + kutukNotu : ''}`
  oda = turEkle({ ...oda, gorevler: [...oda.gorevler, gorev] }, 'jarvis', 'gorev', etiket, id)
  await kaydet($, oda)
  const son = (await kuyrukIsle($)) ?? oda
  const g = son.gorevler.find(x => x.id === id)
  const ek = `${kutukNotu ? ' ' + kutukNotu + '.' : ''}`
  if (g?.durum === 'kosuyor') return `Görev #${id} "${gorev.baslik}" [${sinif}] ${g.model} işçisinde koşuyor (ajan ${g.agentId ?? '?'}); paralel ${kosan(son)}/${son.maksParalel}; bütçe ${butce} çağrı.${ek} Bitince rapor odaya düşer; beklemeden başka görev verebilirsin.`
  if (g?.durum === 'hata') return `Görev #${id} başlatılamadı: ${g.sonuc ?? ''}`
  return `Görev #${id} "${gorev.baslik}" kuyruğa alındı (paralel sınır ${son.maksParalel} dolu: ${kosan(son)} koşuyor).${ek} Biri bitince başlar; oda_ayar ile sınırı artırabilirsin.`
}

export async function odaOku($: EngineInterface, son: number, hareketler: Parameters<typeof odaMetni>[2], gorevId?: number, altOdaId?: number): Promise<string> {
  const oda = await odaYukle($)
  if (!oda) return 'Oda yok; önce oda_ac.'
  // B9: altOdaId verilirse alt-odanın tam dökümü kesilmeden döner.
  if (Number.isInteger(altOdaId) && Number(altOdaId) > 0) return altOdaDokumu(oda.altOdalar?.find(a => a.id === Number(altOdaId)), Number(altOdaId), oda.altOdalar?.length ?? 0)
  // K52: gorevId verilirse o görevin final raporu kesilmeden döner.
  if (Number.isInteger(gorevId) && Number(gorevId) > 0) return gorevRaporu(oda, Number(gorevId))
  return odaMetni(oda, Number.isFinite(son) && son > 0 ? son : 12, hareketler)
}

export async function oneriKarar($: EngineInterface, kim: 'jarvis' | 'salih', oneriId: number, karar: 'kabul' | 'ret', not?: string): Promise<string> {
  const oda = await odaYukle($)
  if (!oda) return 'Oda yok.'
  const oneri = oda.oneriler.find(o => o.id === oneriId)
  if (!oneri) return `Ö${oneriId} bulunamadı.`
  const yeni = { ...oda, oneriler: oda.oneriler.map(o => (o.id === oneri.id ? { ...o, durum: karar, not } : o)) }
  await kaydet($, turEkle(yeni, kim, 'karar', `Ö${oneri.id} ${karar}${not ? ': ' + not : ''}`, oneri.gorevId))
  const g = oneri.gorevId ? oda.gorevler.find(x => x.id === oneri.gorevId) : undefined
  if (g?.agentId && g.durum === 'kosuyor') {
    await $.session.append({ agentId: g.agentId, message: { type: 'user', content: [{ type: 'text', text: `[oda] Ö${oneri.id} kararı${kim === 'salih' ? ' (Salih)' : ''}: ${karar}${not ? ' · ' + not : ''}` }] } }).catch(() => undefined)
  }
  if (kim === 'salih') {
    await $.session.append({ message: { type: 'user', content: [{ type: 'text', text: `[oda] Salih panodan Ö${oneri.id} kararı verdi: ${karar} (${kisa(oneri.metin, 120)})` }] } }).catch(() => undefined)
  }
  return `Ö${oneri.id} ${karar}.`
}

export async function oneriBirak($: EngineInterface, o: { metin?: string; gerekce?: string; agentId?: string }, ayar?: ModAyar): Promise<string> {
  const oda = await odaYukle($)
  if (!oda) return 'Oda yok.'
  const gorev = oda.gorevler.find(g => g.agentId && g.agentId === o.agentId)
  const id = oda.oneriler.length + 1
  const oneri: OdaOneri = { id, kim: gorev ? `işçi #${gorev.id}` : 'jarvis', gorevId: gorev?.id, metin: String(o.metin ?? ''), gerekce: String(o.gerekce ?? ''), durum: 'bekliyor' }
  await kaydet($, turEkle({ ...oda, oneriler: [...oda.oneriler, oneri] }, oneri.kim, 'oneri', `Ö${id}: ${oneri.metin} · gerekçe: ${oneri.gerekce}`, gorev?.id))
  $.ui.toast(`Oda: Ö${id} öneri bekliyor (${oneri.kim})`)
  // K52: işçi önerisi Jarvis'i uyandırır (görev raporuyla aynı yol: prompt.submit, otoUyandir ayarı).
  // Motor tool.call içinden prompt.submit'i reddeder (tutulan tura bekler); uyandırma kuyruğa yazılır, 3 sn'lik saat boşaltır.
  if (gorev && (ayar?.otoUyandir ?? true)) {
    const uyar = `[oda] öneri #${id} (görev #${gorev.id}): ${oneri.metin}
gerekçe: ${oneri.gerekce}
Karar: oda_oneri_karar oneriId=${id} karar=kabul|ret.`
    const kuyruk = ((await $.store.get('oda:uyandir')) as string[] | undefined) ?? []
    await $.store.set('oda:uyandir', [...kuyruk, uyar])
  }
  return `Ö${id} kaydedildi; karar bekleniyor. Varsayılan yolu sürdür, raporunda belirt.`
}

export async function raporDus($: EngineInterface, r: { metin?: string; agentId?: string }): Promise<string> {
  const oda = await odaYukle($)
  if (!oda) return 'Oda yok.'
  const gorev = oda.gorevler.find(g => g.agentId && g.agentId === r.agentId)
  const kim = gorev ? `işçi #${gorev.id}` : 'jarvis'
  await kaydet($, turEkle(oda, kim, 'rapor', String(r.metin ?? ''), gorev?.id))
  if (gorev) $.ui.toast(`Oda ${kim}: ${kisa(String(r.metin ?? ''), 80)}`)
  return 'Rapor düştü.'
}

/** İşçinin final cevabı = görev raporu; kütük kapanır, kuyruk işlenir, Jarvis uyandırılır. */
export async function gorevBitti($: EngineInterface, e: { agentId?: string; reason: string; isAborted?: boolean; answer?: string; text?: string }, ayar: ModAyar): Promise<void> {
  if (!e.agentId) return
  const oda = await odaYukle($)
  if (!oda) return
  const gorev = oda.gorevler.find(g => g.agentId === e.agentId && g.durum === 'kosuyor')
  if (!gorev) return
  const butceAsildi = Boolean(gorev.butce && (gorev.cagri ?? 0) > Math.floor(gorev.butce * 1.5))
  const basarili = e.reason === 'answer' && !e.isAborted && !butceAsildi
  const sonuc = (butceAsildi ? `(bütçe aşıldı: ${gorev.cagri}/${gorev.butce}) ` : '') + (e.reason === 'answer' ? String(e.answer ?? '') : `(${e.reason}) ${e.text ?? ''}`)
  const kapanan = { ...gorev, durum: basarili ? ('bitti' as const) : ('hata' as const), sonuc, kapanis: simdi() }
  const yeni = turEkle({ ...oda, gorevler: oda.gorevler.map(g => (g.id === gorev.id ? kapanan : g)) }, `işçi #${gorev.id}`, 'rapor', sonuc, gorev.id)
  await kaydet($, yeni)
  // K52: başarıda kütük işi kapanır; hata ya da bütçe aşımında açık kalır, neden odaya yazılır.
  const neden = butceAsildi ? `bütçe aşıldı (${gorev.cagri}/${gorev.butce})` : e.isAborted ? 'işçi durduruldu' : `işçi hatayla bitti (${e.reason})`
  const kutukNot = basarili ? await kutukBitir($, yeni, kapanan) : gorev.isId ? `kütük iş #${gorev.isId} açık kaldı: ${neden}` : undefined
  if (kutukNot) await kutukNotuYaz($, gorev.id, kutukNot)
  $.ui.toast(`Oda: görev #${gorev.id} ${basarili ? 'bitti' : 'hata'} (${gorev.model})`)
  const son = (await kuyrukIsle($)) ?? yeni
  if (ayar.otoUyandir) {
    const ozet = `[oda] görev #${gorev.id} "${gorev.baslik}" [${sinifi(gorev)}] ${basarili ? 'bitti' : 'hata'} (${gorev.model}, çağrı ${gorev.cagri ?? 0}/${gorev.butce ?? '?'}). Rapor:\n${kisa(sonuc, 1500)}\n(tamamı: oda_oku gorevId=${gorev.id})${kutukNot ? '\n' + kutukNot : ''}\n\nKoşan: ${kosan(son)}/${son.maksParalel} · kuyrukta: ${kuyrukSayisi(son)} · bekleyen öneri: ${bekleyenOneri(son)}. Sırada iş varsa oda_gorev_ver.`
    void $.prompt.submit({ text: ozet }).catch(() => undefined)
  }
}

/** K52: kuyruktaki uyandırmaları (işçi önerileri) prompt.submit ile Jarvis'e iletir; saat olayından çağrılır. */
export async function uyandirmaBosalt($: EngineInterface): Promise<void> {
  const kuyruk = ((await $.store.get('oda:uyandir')) as string[] | undefined) ?? []
  if (!kuyruk.length) return
  await $.store.set('oda:uyandir', [])
  void $.prompt.submit({ text: kuyruk.join('\n\n') }).catch(() => undefined)
}

/** 3 sn'lik yoklama: ajan durumlarını panoya yansıtır, düşen ajanı kapatır, kuyruğu işler. */
export async function ajanYokla($: EngineInterface): Promise<void> {
  const o = await odaSicak($)
  if (!o || !o.gorevler.some(g => g.durum === 'kosuyor')) return
  const liste = await $.agent.list()
  const ajanlar: AjanDurum[] = []
  for (const g of o.gorevler) {
    if (!g.agentId || g.durum !== 'kosuyor') continue
    const a = liste.find(x => x.id === g.agentId)
    ajanlar.push({ agentId: g.agentId, status: a?.status ?? 'bilinmiyor', gorevId: g.id })
  }
  await ajanlariYaz($, ajanlar)
  const dusen = ajanlar.filter(a => a.status === 'killed' || a.status === 'failed')
  if (!dusen.length) return
  const guncel = (await odaYukle($)) ?? o
  const yeni = { ...guncel, gorevler: guncel.gorevler.map(g => (dusen.some(d => d.gorevId === g.id) ? { ...g, durum: 'hata' as const, sonuc: g.sonuc ?? 'ajan ' + (dusen.find(d => d.gorevId === g.id)?.status ?? ''), kapanis: simdi() } : g)) }
  await kaydet($, yeni)
  // K52: düşen ajanın kütük işi açık kalır; neden odaya yazılır.
  for (const d of dusen) {
    const g = guncel.gorevler.find(x => x.id === d.gorevId)
    if (g?.isId) await kutukNotuYaz($, g.id, `kütük iş #${g.isId} açık kaldı: ajan ${d.status}`)
  }
  await kuyrukIsle($)
}

// ---------- işçi akışı, kapsam ve bütçe kapısı (A5) ----------

/** İşçinin araç çağrısından önce: hareket kaydı + sayaç + kapsam/bütçe kararı. Dönüş: ret metni ya da undefined. */
export async function isciAracOncesi($: EngineInterface, agentId: string, e: Record<string, unknown>): Promise<string | undefined> {
  const ozet = aracOzeti(e)
  const gorevId = await hareketEkle($, agentId, 'arac', ozet)
  if (gorevId === undefined) return undefined
  const oda = await odaYukle($)
  const g = oda?.gorevler.find(x => x.id === gorevId)
  if (!oda || !g) return undefined
  const ad = String(e.tool ?? '')
  if (ad.startsWith('mcp__jarvis-oda__')) return undefined
  const cagri = (g.cagri ?? 0) + 1
  await kaydet($, { ...oda, gorevler: oda.gorevler.map(x => (x.id === g.id ? { ...x, cagri } : x)) })
  const butce = g.butce ?? 0
  if (butce && cagri === butce) {
    await $.session.append({ agentId, message: { type: 'user', content: [{ type: 'text', text: `[oda] Araç çağrısı bütçen doldu (${cagri}/${butce}). Kalan işi en kısa yoldan bitir ve raporunu yaz; ${Math.floor(butce * 1.5)} çağrıda araçların kapanır.` }] } }).catch(() => undefined)
  }
  if (butce && cagri > Math.floor(butce * 1.5)) return `oda: bütçe aşıldı (${cagri}/${butce}); araç kapalı. Raporunu şimdi yaz.`
  if (sinifi(g) === 'dosyali' && YAZAN_ARACLAR.has(ad)) {
    const hedef = String(e.file_path ?? e.notebook_path ?? '')
    const izin = (g.dosyalar ?? []).map(yolNormal)
    const mutlak = yolNormal(yolMutlak(hedef, await $.session.cwd().catch(() => '')))
    if (!izin.includes(mutlak)) return `oda: ${hedef} bu görevin yazma izni listesinde yok (dosyali sınıfı). İzinli: ${(g.dosyalar ?? []).join(', ')}`
  }
  return undefined
}

// ---------- pano eylemleri (pano.tsx yalnız bunları çağırır) ----------

export async function bolumAcKapa($: EngineInterface, b: OdaBolum): Promise<void> {
  await panoGuncelle($, p => ({ ...p, acik: p.acik.includes(b) ? p.acik.filter(x => x !== b) : [...p.acik, b] }))
}

/** A2: pencere kaydırma; yon -1 önceki, +1 sonraki, 0 en son. */
export async function pencereKaydir($: EngineInterface, liste: OdaListe, n: number, yon: -1 | 0 | 1): Promise<void> {
  await panoGuncelle($, p => {
    const boy = PENCERE_BOY[liste]
    const enGeri = Math.max(0, n - boy)
    const simdiki = p.ofset[liste] ?? enGeri
    let yeni: number | null = yon === 0 ? null : Math.max(0, simdiki + yon * boy)
    if (yeni !== null && yeni >= enGeri) yeni = null
    return { ...p, ofset: { ...p.ofset, [liste]: yeni } } as OdaPano
  })
}

export async function genisAcKapa($: EngineInterface, anahtar: string): Promise<void> {
  await panoGuncelle($, p => ({ ...p, genis: p.genis.includes(anahtar) ? p.genis.filter(x => x !== anahtar) : [...p.genis, anahtar].slice(-50) }))
}

/** A1: ana transkripti işçiye çevirir (yalnız kişinin basışıyla çalışır). */
export async function isciyiIzle($: EngineInterface, agentId: string | undefined): Promise<void> {
  if (!agentId) {
    $.ui.toast('Bu görevin ajanı henüz başlamadı.')
    return
  }
  await $.ui.view({ agentId }).catch(err => $.ui.toast('İşçi görünümü açılamadı: ' + kisa(String(err), 100)))
}

export async function anaSohbeteDon($: EngineInterface): Promise<void> {
  await $.ui.view({}).catch(() => undefined)
}

/** A4: graf moduna seçim köprüsü: ortak/graf-secim.json yazılır, graf modu 2 sn'de bir okur ve pane'i öne alır. */
export async function grafdaGoster($: EngineInterface, isId: number): Promise<void> {
  const depo = await depoBul($)
  if (!depo) {
    $.ui.toast('Depo bulunamadı; graf köprüsü yazılamadı.')
    return
  }
  await $.fs.write(depo + '/ortak/graf-secim.json', JSON.stringify({ secili: 'is:' + isId, ts: simdi(), kaynak: 'jarvis-oda' }))
  $.ui.toast(`Akış grafında iş #${isId} seçiliyor…`)
}
