// araclar.ts: graf modunun yazan tarafı; HTML üretici koşumu (B4), durum graf yenileme, seçim ve filtre eylemleri.
// Pano yalnız bu fonksiyonları çağırır; süreç (process) ve dosya yazımı burada.
import type { EngineInterface } from 'claude-code'

import { PANE, yolBul, grafYukle, gorunumGuncelle, gorunumOku } from './durum'
import { kisa } from './ortak'

/** / ayraçlı yolu Windows biçimine çevirir (C:/a/b → C:\a\b). */
export function windowsYolu(dosya: string): string {
  return dosya.replace(/\//g, '\\')
}

/** B4: python3 shim'i bir bash betiğidir; kabuksuz process.run onu değil Store yönlendiricisini bulur. Sıra: py -3 → python → python3. */
const PYTHONLAR: string[][] = [['py', '-3'], ['python'], ['python3']]

export async function htmlAc($: EngineInterface): Promise<void> {
  const yol = await yolBul($)
  if (!yol) {
    await gorunumGuncelle($, g => ({ ...g, htmlHata: 'depo bulunamadı (ortak/akis-graf.json)' }))
    return
  }
  await gorunumGuncelle($, g => ({ ...g, htmlHata: 'HTML üretiliyor…' }))
  const denemeler: string[] = []
  for (const py of PYTHONLAR) {
    try {
      const r = await $.process.run([...py, 'tools/akis-graf-html.py'], { cwd: yol.jarvis, timeoutMs: 60000, env: { PYTHONUTF8: '1', PYTHONIOENCODING: 'utf-8' } })
      const cikti = r.stdout.trim().split(/\r?\n/).pop()?.trim() ?? ''
      if (r.exitCode === 0 && /\.html?$/i.test(cikti)) {
        await gorunumGuncelle($, g => ({ ...g, html: cikti, htmlHata: null }))
        await disaridaAc($, cikti)
        return
      }
      denemeler.push(`${py.join(' ')}: çıkış ${r.exitCode} ${kisa(r.stderr || r.stdout, 140)}`)
    } catch (err) {
      denemeler.push(`${py.join(' ')}: başlatılamadı (${kisa(String(err), 100)})`)
    }
  }
  await gorunumGuncelle($, g => ({ ...g, htmlHata: 'HTML üretilemedi. ' + denemeler.join(' · ') }))
}

/** Üretilen dosyayı varsayılan tarayıcıda açmayı dener; olmazsa pane'deki aç/kopyala/Explorer düğmeleri kalır. */
async function disaridaAc($: EngineInterface, dosya: string): Promise<void> {
  const r = await dosyaAc($, dosya)
  if (!r) $.ui.toast('Graf HTML açıldı')
  else await gorunumGuncelle($, g => ({ ...g, htmlHata: 'Otomatik açılamadı (' + r + '); aşağıdaki "aç" ya da "kopyala" düğmesini kullan.' }))
}

/**
 * Dosyayı ilişkili uygulamada açar (HTML → tarayıcı, JSON → düzenleyici). Masaüstü yüzeyi file:// bağlantısı
 * üretmediği için (yalnız https ve http://localhost) açma işi host sürecindedir. Dönüş: hata metni ya da null.
 */
export async function dosyaAc($: EngineInterface, dosya: string): Promise<string | null> {
  const yol = windowsYolu(dosya)
  try {
    const r = await $.process.run(['powershell', '-NoProfile', '-Command', 'Start-Process', '-FilePath', `'${yol.replace(/'/g, "''")}'`], { timeoutMs: 20000 })
    return r.exitCode === 0 ? null : `Start-Process çıkış ${r.exitCode}: ${kisa(r.stderr, 100)}`
  } catch (err) {
    return kisa(String(err), 100)
  }
}

/** Dosyayı Explorer'da seçili gösterir (explorer.exe başarıda da 1 dönebilir; sonuç beklenmez). */
export async function explorerdaGoster($: EngineInterface, dosya: string): Promise<void> {
  const yol = windowsYolu(dosya)
  await $.process.run(['explorer.exe', '/select,' + yol], { timeoutMs: 15000 }).catch(() => undefined)
}

export async function yoluKopyala($: EngineInterface, dosya: string, surface: string): Promise<void> {
  await $.ui
    .copy({ text: windowsYolu(dosya), surface: surface as 'desktop' })
    .then(() => $.ui.toast('Yol panoya kopyalandı'))
    .catch(() => $.ui.toast('Kopyalanamadı: ' + dosya))
}

export async function durumGrafYenile($: EngineInterface): Promise<void> {
  const yol = await yolBul($)
  if (!yol) return
  const gor = await gorunumOku($)
  try {
    const r = await $.process.run([yol.depo + '/target/release/durum.exe', 'graf', ...(gor.alan === 'tum' ? [] : ['--alan', gor.alan])], { cwd: yol.depo, timeoutMs: 60000 })
    $.ui.toast(r.exitCode === 0 ? 'durum graf koştu; JSON + D2 tazelendi' : 'durum graf hata: ' + kisa(r.stderr, 120))
  } catch (err) {
    $.ui.toast('durum graf başlatılamadı: ' + kisa(String(err), 120))
  }
  await grafYukle($, true)
}

export async function sec($: EngineInterface, id: string | null): Promise<void> {
  await gorunumGuncelle($, g => ({ ...g, secili: id }))
}

export async function alanSec($: EngineInterface, alan: string): Promise<void> {
  await gorunumGuncelle($, g => ({ ...g, alan }))
}

export async function yalnizAcikDegistir($: EngineInterface): Promise<void> {
  await gorunumGuncelle($, g => ({ ...g, yalnizAcik: !g.yalnizAcik }))
}

export async function htmlBildirimKapat($: EngineInterface): Promise<void> {
  await gorunumGuncelle($, g => ({ ...g, htmlHata: null }))
}

/** B5: dışarıdan gelen seçim (oda köprüsü ya da /graf is:<id>): seçer, alan filtresini açar, pane'i öne alır. */
export async function disaridanSec($: EngineInterface, id: string): Promise<void> {
  await gorunumGuncelle($, g => ({ ...g, secili: id, alan: 'tum', yalnizAcik: false }))
  await $.ui.open({ id: PANE, title: 'Akış grafı', focus: true }).catch(() => undefined)
}

/** /graf argümanı: "is:12", "#12", "12" ya da "seans:<ad>". */
export function argumandanId(arg: string): string | null {
  const a = arg.trim()
  if (!a) return null
  if (/^(is|seans):/.test(a)) return a
  const no = /^#?(\d+)$/.exec(a)?.[1]
  return no ? 'is:' + no : null
}
