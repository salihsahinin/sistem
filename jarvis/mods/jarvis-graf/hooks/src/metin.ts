// metin.ts: grafın saf hesapları; seans satırı düzeni (B1/B2) ve düğüm detayı (B3).
// Motor ($) almaz; çizim (cizim.ts) ve pano (pano.tsx) bu çıktıları kullanır.
import type { Graf, GrafDugum, GrafEk, GrafGorunum, KutukOlay } from '../../types'
import { kisa } from './ortak'

export function zaman(n: GrafDugum): number {
  const ms = Date.parse(n.acilis_ts ?? n.ac_ts ?? '')
  return Number.isFinite(ms) ? ms : 0
}

export function acikMi(n: GrafDugum): boolean {
  return n.tur !== 'seans' && (n.durum === 'acik' || n.durum === 'islemde')
}

/** Bir graf satırı: hedef şeridi, gerçek seans ya da iş kaydındaki oturum adından türeyen sanal oturum. */
export type Satir = {
  anahtar: string
  etiket: string
  tur: 'hedef' | 'seans' | 'oturum'
  alan: string
  seans?: GrafDugum
  dugumler: GrafDugum[]
  bas: number
  son: number
}

/** Filtreye uyan düğümler. Seans düğümleri alan filtresine uyar. */
export function gorunenler(graf: Graf, gor: GrafGorunum): GrafDugum[] {
  return graf.dugumler
    .filter(n => gor.alan === 'tum' || n.alan === gor.alan)
    .filter(n => !gor.yalnizAcik || n.tur === 'seans' || acikMi(n) || n.tur === 'hedef')
}

/**
 * Satır düzeni: en üstte hedefler; sonra seanslar açılış sırasıyla (her seans satırında onun açtığı işler);
 * açan seansı olmayan işler ilk oturum adına göre sanal satıra (ör. oda-<id>), oturumu yoksa "oturumsuz".
 */
export function satirlar(graf: Graf, gor: GrafGorunum): Satir[] {
  const gor_ = gorunenler(graf, gor)
  const idler = new Set(gor_.map(n => n.id))
  const acan = new Map<string, string>()
  for (const k of graf.kenarlar) if (k.tur === 'acti' && !acan.has(k.h)) acan.set(k.h, k.k)
  const hedefler = gor_.filter(n => n.tur === 'hedef').sort((a, b) => zaman(a) - zaman(b))
  const seanslar = gor_.filter(n => n.tur === 'seans').sort((a, b) => zaman(a) - zaman(b))
  const isler = gor_.filter(n => n.tur === 'is')
  const sonuc: Satir[] = []
  if (hedefler.length) sonuc.push({ anahtar: 'hedefler', etiket: 'hedefler', tur: 'hedef', alan: '', dugumler: hedefler, bas: 0, son: 0 })
  const seansSatiri = new Map<string, Satir>()
  for (const s of seanslar) {
    const satir: Satir = { anahtar: s.id, etiket: s.etiket, tur: 'seans', alan: s.alan, seans: s, dugumler: [], bas: zaman(s), son: Date.parse(s.kapat_ts ?? '') || 0 }
    seansSatiri.set(s.id, satir)
    sonuc.push(satir)
  }
  const sanal = new Map<string, Satir>()
  for (const n of isler) {
    const a = acan.get(n.id)
    const hedefSatir = a && idler.has(a) ? seansSatiri.get(a) : undefined
    if (hedefSatir) {
      hedefSatir.dugumler.push(n)
      continue
    }
    const ad = n.oturumlar?.[0] ?? 'oturumsuz'
    const adSeansi = seanslar.find(x => x.etiket === ad)
    if (adSeansi) {
      seansSatiri.get(adSeansi.id)!.dugumler.push(n)
      continue
    }
    let s = sanal.get(ad)
    if (!s) {
      s = { anahtar: 'oturum:' + ad, etiket: ad, tur: 'oturum', alan: n.alan, dugumler: [], bas: 0, son: 0 }
      sanal.set(ad, s)
    }
    s.dugumler.push(n)
  }
  for (const s of sanal.values()) {
    s.bas = Math.min(...s.dugumler.map(zaman))
    sonuc.push(s)
  }
  for (const s of sonuc) s.dugumler.sort((a, b) => zaman(a) - zaman(b))
  // Sanal satırlar zamana göre gerçek seansların arasına yerleşir; hedef şeridi en üstte kalır.
  const ust = sonuc.filter(s => s.tur === 'hedef')
  const alt = sonuc.filter(s => s.tur !== 'hedef').sort((a, b) => a.bas - b.bas)
  return [...ust, ...alt]
}

export type DetayBag = { id: string; etiket: string; ne: string }
export type DetayOlay = { ts: string; olay: string; oturum?: string; kanit: string[]; not?: string }

export type Detay = {
  dugum: GrafDugum
  baslik: string
  satirlar: { ad: string; deger: string }[]
  baglar: DetayBag[]
  olaylar: DetayOlay[]
  defter?: { no: string; metin: string }
  kayit?: string
}

const OLAY_ADI: Record<string, string> = { ac: 'açıldı', al: 'alındı', bitir: 'bitti', bayatla: 'bayatladı', tuket: 'tüketildi', seans_ac: 'seans açıldı', seans_kapat: 'seans kapandı' }

function olayaCevir(o: KutukOlay): DetayOlay {
  return { ts: o.ts, olay: OLAY_ADI[o.olay] ?? o.olay, oturum: o.oturum, kanit: o.kanit ?? [], not: o.is ? kisa(o.is, 120) : o.hedef_cumle ? kisa(o.hedef_cumle, 160) : undefined }
}

/** B3: seçili düğümün zengin detayı (kenarlar yönlü, kütük olayları, defter paragrafı, kayıt yolu). */
export function detay(graf: Graf, ek: GrafEk, id: string): Detay | null {
  const n = graf.dugumler.find(x => x.id === id)
  if (!n) return null
  const ad = (x: string) => graf.dugumler.find(d => d.id === x)?.etiket ?? x
  const baglar: DetayBag[] = []
  for (const k of graf.kenarlar) {
    if (k.k !== id && k.h !== id) continue
    const giden = k.k === id
    const karsi = giden ? k.h : k.k
    const ne =
      k.tur === 'girdi'
        ? giden
          ? 'önünü açar'
          : 'bekler (girdi)'
        : k.tur === 'hizmet'
          ? giden
            ? 'hizmet eder (hedef)'
            : 'ona hizmet eden'
          : k.tur === 'acti'
            ? giden
              ? 'açtı'
              : 'açan seans'
            : k.tur === 'bitirdi'
              ? giden
                ? 'bitirdi'
                : 'bitiren seans'
              : k.tur === 'sonra'
                ? giden
                  ? 'sonraki seans'
                  : 'önceki seans'
                : k.tur
    baglar.push({ id: karsi, etiket: kisa(ad(karsi), 70), ne })
  }
  const satirlar: { ad: string; deger: string }[] = []
  let olaylar: DetayOlay[] = []
  if (n.tur === 'seans') {
    if (n.hedef) satirlar.push({ ad: 'hedef', deger: n.hedef })
    satirlar.push({ ad: 'hedef tutuldu', deger: n.hedef_tutuldu === true ? 'evet' : n.hedef_tutuldu === false ? 'hayır' : n.kapat_ts ? 'yoklanmadı' : 'seans açık' })
    satirlar.push({ ad: 'açılış', deger: n.ac_ts ?? '' })
    if (n.kapat_ts) satirlar.push({ ad: 'kapanış', deger: n.kapat_ts })
    if (n.dokunulan?.length) satirlar.push({ ad: 'dokunulan', deger: n.dokunulan.join(', ') })
    olaylar = ek.olaylar.filter(o => o.oturum === n.etiket).map(olayaCevir)
  } else {
    satirlar.push({ ad: 'durum', deger: `${n.durum ?? '?'}${n.sirada ? ' · sırada' : ''}` })
    if (n.sonraki_eylem) satirlar.push({ ad: 'sonraki eylem', deger: n.sonraki_eylem })
    satirlar.push({ ad: 'açılış', deger: n.acilis_ts ?? '' })
    if (n.al_ts) satirlar.push({ ad: 'alındı', deger: n.al_ts })
    if (n.bitir_ts) satirlar.push({ ad: 'bitti', deger: n.bitir_ts })
    if (n.oturumlar?.length) satirlar.push({ ad: 'oturumlar', deger: n.oturumlar.join(', ') })
    const no = Number(id.split(':')[1])
    olaylar = ek.olaylar.filter(o => o.id === no && o.olay in OLAY_ADI).map(olayaCevir)
  }
  const karar = /Karar (\d{2,3})/.exec(n.etiket)?.[1]
  let defter: Detay['defter']
  if (karar && ek.defter) {
    const i = ek.defter.search(new RegExp('\\*\\*Karar ' + karar + '\\b'))
    if (i >= 0) {
      const par = ek.defter.slice(i).split(/\n\s*\n/)[0] ?? ''
      defter = { no: karar, metin: par.length > 600 ? par.slice(0, 599) + '…' : par }
    }
  }
  return {
    dugum: n,
    baslik: n.tur === 'seans' ? `seans ${n.etiket}` : `${n.tur === 'hedef' ? 'hedef' : 'iş'} #${id.split(':')[1]}`,
    satirlar,
    baglar,
    olaylar,
    defter,
    kayit: n.kayit ?? undefined,
  }
}
