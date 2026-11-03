// dis.ts: stigmerjik dış kanal (C1); kalıcı dış oturumlar odaya dosya üzerinden katılır ve yazar.
// Ev sahibi oda gelen-<oturum>.jsonl dosyalarını okur, giden.jsonl'a yazar; dış oturum tersini yapar. Her dosyanın tek yazarı var.
import type { EngineInterface } from 'claude-code'

import type { Oda, OdaDisSatir, OdaOneri, OdaOturum } from '../../types'
import { odaYukle, turEkle } from './durum'
import { depoBul, kaydet } from './araclar'
import { kisa, simdi } from './ortak'

const KATILIM = 'dis:katilim'

type Katilim = { odaId: string; oturum: string; gidenSatir: number }

/** Oturum adı dosya adında kullanılır: küçük harf, rakam, - ve _. */
export function oturumAdi(ad: string): string {
  return ad
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9_-]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 40)
}

function odaDizini(depo: string, odaId: string): string {
  return `${depo}/ortak/oda/${odaId}`
}

async function satirlariOku($: EngineInterface, dosya: string): Promise<OdaDisSatir[]> {
  if (!(await $.fs.exists(dosya).catch(() => false))) return []
  const metin = await $.fs.read(dosya).catch(() => '')
  const sonuc: OdaDisSatir[] = []
  for (const s of metin.split(/\r?\n/)) {
    if (!s.trim()) continue
    try {
      sonuc.push(JSON.parse(s) as OdaDisSatir)
    } catch {
      /* bozuk satır atlanır */
    }
  }
  return sonuc
}

/** Tek yazarlı dosyaya satır ekler (oku + yaz; dosyanın başka yazarı yok). */
async function satirEkle($: EngineInterface, dosya: string, satir: OdaDisSatir): Promise<void> {
  const eski = (await $.fs.exists(dosya).catch(() => false)) ? await $.fs.read(dosya).catch(() => '') : ''
  await $.fs.write(dosya, eski + (eski && !eski.endsWith('\n') ? '\n' : '') + JSON.stringify(satir) + '\n')
}

// ---------- ev sahibi (odayı tutan oturum) ----------

/** Aktif oda işaretçisi: dış oturumlar hangi odaya katılacağını buradan okur. */
export async function aktifIsaretle($: EngineInterface, oda: Oda): Promise<void> {
  const depo = await depoBul($)
  if (!depo) return
  await $.fs.write(`${depo}/ortak/oda/aktif.json`, JSON.stringify({ odaId: oda.id, baslik: oda.baslik, ts: simdi() })).catch(() => undefined)
}

/** 3 sn yoklaması: gelen-*.jsonl dosyalarındaki yeni satırları odaya işler. */
export async function gelenleriIsle($: EngineInterface, otoUyandir: boolean): Promise<void> {
  let oda = await odaYukle($)
  if (!oda) return
  const depo = await depoBul($)
  if (!depo) return
  const dizin = odaDizini(depo, oda.id)
  if (!(await $.fs.exists(dizin).catch(() => false))) return
  const dosyalar = (await $.fs.list(dizin).catch(() => [])).filter(d => /^gelen-.*\.jsonl$/.test(d.name))
  const uyandir: string[] = []
  let degisti = false
  for (const d of dosyalar) {
    const anahtar = `oda:gelen:${oda.id}:${d.name}`
    const islenen = Number((await $.store.get(anahtar)) ?? 0)
    const satirlar = await satirlariOku($, `${dizin}/${d.name}`)
    if (satirlar.length <= islenen) continue
    for (const s of satirlar.slice(islenen)) {
      oda = disSatirIsle(oda, s)
      degisti = true
      if (s.tur === 'rapor' || s.tur === 'oneri') uyandir.push(`oturum ${s.kim} [${s.tur}]: ${kisa(s.metin, 600)}`)
      else if (s.tur === 'sohbet') {
        await $.session.append({ message: { type: 'user', content: [{ type: 'text', text: `[oda dış] oturum ${s.kim}: ${s.metin}` }] } }).catch(() => undefined)
      }
      $.ui.toast(`Oda: oturum ${s.kim} ${s.tur === 'katil' ? 'katıldı' : s.tur === 'ayril' ? 'ayrıldı' : s.tur}`)
    }
    await $.store.set(anahtar, satirlar.length)
  }
  if (degisti) await kaydet($, oda)
  if (uyandir.length && otoUyandir) {
    void $.prompt.submit({ text: `[oda dış] ${uyandir.join('\n')}\n\noda_oku ile tamamını gör; dış oturuma cevap için oda_sohbet hedef "@<oturum>".` }).catch(() => undefined)
  }
}

/** Bir dış satırı odaya uygular (saf). */
export function disSatirIsle(oda: Oda, s: OdaDisSatir): Oda {
  const ad = oturumAdi(s.kim)
  const oturumlar = [...(oda.oturumlar ?? [])]
  const i = oturumlar.findIndex(o => o.oturum === ad)
  const eski: OdaOturum | undefined = oturumlar[i]
  if (s.tur === 'katil') {
    const yeni: OdaOturum = { oturum: ad, rol: s.rol ?? eski?.rol ?? '', dosyalar: s.dosyalar ?? eski?.dosyalar ?? [], acilis: eski?.acilis ?? s.ts, durum: 'katildi', son: s.ts }
    if (i >= 0) oturumlar[i] = yeni
    else oturumlar.push(yeni)
    return turEkle({ ...oda, oturumlar }, 'oturum ' + ad, 'not', `oturum ${ad} katıldı${yeni.rol ? ' · rol: ' + yeni.rol : ''}${yeni.dosyalar.length ? ' · dosyalar: ' + yeni.dosyalar.join(', ') : ''}`)
  }
  if (i >= 0) oturumlar[i] = { ...eski!, son: s.ts, ...(s.tur === 'ayril' ? { durum: 'ayrildi' as const } : {}) }
  else oturumlar.push({ oturum: ad, rol: '', dosyalar: [], acilis: s.ts, durum: s.tur === 'ayril' ? 'ayrildi' : 'katildi', son: s.ts })
  const taban = { ...oda, oturumlar }
  if (s.tur === 'ayril') return turEkle(taban, 'oturum ' + ad, 'not', `oturum ${ad} ayrıldı${s.metin ? ': ' + s.metin : ''}`)
  if (s.tur === 'oneri') {
    const oneri: OdaOneri = { id: oda.oneriler.length + 1, kim: 'oturum ' + ad, gorevId: s.gorevId, metin: s.metin, gerekce: s.gerekce ?? '', durum: 'bekliyor' }
    return turEkle({ ...taban, oneriler: [...oda.oneriler, oneri] }, oneri.kim, 'oneri', `Ö${oneri.id}: ${oneri.metin} · gerekçe: ${oneri.gerekce}`, s.gorevId)
  }
  return turEkle(taban, 'oturum ' + ad, s.tur === 'rapor' ? 'rapor' : 'sohbet', s.metin, s.gorevId)
}

/** Ev sahibinden dışarı mesaj: giden.jsonl'a satır (hedef oturum ya da '*'). */
export async function gidenYaz($: EngineInterface, oda: Oda, kim: string, hedef: string, metin: string): Promise<boolean> {
  const depo = await depoBul($)
  if (!depo) return false
  try {
    await satirEkle($, `${odaDizini(depo, oda.id)}/giden.jsonl`, { ts: simdi(), kim, tur: 'sohbet', metin, hedef })
    return true
  } catch {
    return false
  }
}

// ---------- dış oturum (odaya katılan oturum) ----------

export async function odayaKatil($: EngineInterface, a: { oturum?: string; rol?: string; dosyalar?: unknown; ayril?: boolean }): Promise<string> {
  const depo = await depoBul($)
  if (!depo) return 'Depo bulunamadı (ortak/durum-olay.jsonl); katılım dosyası yazılamadı.'
  const katilim = (await $.store.get(KATILIM)) as Katilim | undefined
  if (a.ayril) {
    if (!katilim) return 'Bu oturum bir odaya katılmamış.'
    await satirEkle($, `${odaDizini(depo, katilim.odaId)}/gelen-${katilim.oturum}.jsonl`, { ts: simdi(), kim: katilim.oturum, tur: 'ayril', metin: '' })
    await $.store.delete(KATILIM)
    return `Odadan ayrıldın (${katilim.odaId}); kayıt silinmez, panoda "ayrıldı" görünür.`
  }
  const ad = oturumAdi(String(a.oturum ?? ''))
  if (!ad) return 'oturum adı gerekli (ör. claude-mods).'
  const aktif = await $.fs
    .read(`${depo}/ortak/oda/aktif.json`)
    .then(m => JSON.parse(m) as { odaId?: string; baslik?: string })
    .catch(() => null)
  if (!aktif?.odaId) return 'Aktif oda yok (ortak/oda/aktif.json); Jarvis önce oda_ac ile oda açmalı.'
  const dosyalar = Array.isArray(a.dosyalar) ? (a.dosyalar as unknown[]).filter((d): d is string => typeof d === 'string') : []
  await satirEkle($, `${odaDizini(depo, aktif.odaId)}/gelen-${ad}.jsonl`, { ts: simdi(), kim: ad, tur: 'katil', metin: '', rol: String(a.rol ?? ''), dosyalar })
  const gidenler = await satirlariOku($, `${odaDizini(depo, aktif.odaId)}/giden.jsonl`)
  await $.store.set(KATILIM, { odaId: aktif.odaId, oturum: ad, gidenSatir: gidenler.length } as Katilim)
  return `"${aktif.baslik ?? aktif.odaId}" odasına "oturum ${ad}" olarak katıldın. Yazmak için oda_mesaj (tur: sohbet | rapor | oneri). Odadan sana gelen mesajlar bu sohbete "[oda]" ile düşer. Ayrılmak için oda_katil ayril: true.`
}

export async function disMesaj($: EngineInterface, a: { tur?: string; metin?: string; gerekce?: string; gorevId?: number }): Promise<string> {
  const katilim = (await $.store.get(KATILIM)) as Katilim | undefined
  if (!katilim) return 'Önce oda_katil ile odaya katıl.'
  const depo = await depoBul($)
  if (!depo) return 'Depo bulunamadı.'
  const tur = a.tur === 'rapor' || a.tur === 'oneri' ? a.tur : 'sohbet'
  const metin = String(a.metin ?? '').trim()
  if (!metin) return 'Boş mesaj.'
  await satirEkle($, `${odaDizini(depo, katilim.odaId)}/gelen-${katilim.oturum}.jsonl`, {
    ts: simdi(),
    kim: katilim.oturum,
    tur,
    metin,
    ...(a.gerekce ? { gerekce: String(a.gerekce) } : {}),
    ...(Number.isInteger(a.gorevId) ? { gorevId: Number(a.gorevId) } : {}),
  })
  return `Odaya ${tur} düştü (oturum ${katilim.oturum}); ev sahibi 3 sn içinde okur.`
}

/** Dış oturumun 3 sn yoklaması: giden.jsonl'da bu oturuma ya da herkese yazılan yeni satırları sohbete düşürür. */
export async function gidenleriOku($: EngineInterface): Promise<void> {
  const katilim = (await $.store.get(KATILIM)) as Katilim | undefined
  if (!katilim) return
  const depo = await depoBul($)
  if (!depo) return
  const satirlar = await satirlariOku($, `${odaDizini(depo, katilim.odaId)}/giden.jsonl`)
  if (satirlar.length <= katilim.gidenSatir) return
  for (const s of satirlar.slice(katilim.gidenSatir)) {
    if (s.hedef !== '*' && oturumAdi(s.hedef ?? '') !== katilim.oturum) continue
    await $.session.append({ message: { type: 'user', content: [{ type: 'text', text: `[oda] ${s.kim}${s.hedef === '*' ? ' (herkese)' : ''}: ${s.metin}\n(Cevap için oda_mesaj.)` }] } }).catch(() => undefined)
    $.ui.toast(`Oda: ${s.kim} → ${kisa(s.metin, 60)}`)
  }
  await $.store.set(KATILIM, { ...katilim, gidenSatir: satirlar.length })
}
