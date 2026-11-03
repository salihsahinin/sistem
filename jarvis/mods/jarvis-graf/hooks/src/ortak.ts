// ortak.ts: iki modda aynı içerikli küçük yardımcılar (saat, kısaltma, renk, pencere).
// Saf fonksiyonlar; motor ($) almaz. jarvis-graf/hooks/src/ortak.ts ile aynı tutulur (paket yok, kopya).

export function simdi(): string {
  return new Date().toISOString()
}

/** Kayıt UTC (ISO) kalır, görünüm yerel saat (tr-TR, 24 saat); saniye isteğe bağlı. */
export function saat(ts: string | null | undefined, saniye = true): string {
  if (!ts) return ''
  const d = new Date(ts)
  if (Number.isNaN(d.getTime())) return ts.slice(11, saniye ? 19 : 16)
  return d.toLocaleTimeString('tr-TR', { hour12: false, hour: '2-digit', minute: '2-digit', ...(saniye ? { second: '2-digit' } : {}) })
}

/** Yerel tarih + saat (gg.aa ss:dd). */
export function tarihSaat(ts: string | null | undefined): string {
  if (!ts) return ''
  const d = new Date(ts)
  if (Number.isNaN(d.getTime())) return ts
  return d.toLocaleString('tr-TR', { hour12: false, day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' })
}

/** Boşlukları tekleyip n karakterde keser. */
export function kisa(metin: string | null | undefined, n = 160): string {
  const tek = (metin ?? '').replace(/\s+/g, ' ').trim()
  return tek.length > n ? tek.slice(0, n - 1) + '…' : tek
}

/** Görev başına sabit renk (8 renk döner); salih cyan ve jarvis magenta bu listede yok. */
const ISCI_RENKLERI = ['green', 'yellow', 'blue', 'red', 'greenBright', 'yellowBright', 'blueBright', 'redBright'] as const
export function isciRengi(gorevId: number): string {
  return ISCI_RENKLERI[(Math.max(1, gorevId) - 1) % ISCI_RENKLERI.length] ?? 'green'
}

/** Kaydırma penceresi: n öğe, boy b, ofset o (null = en son). Gösterilecek [bas, son) aralığı. */
export function pencere(n: number, boy: number, ofset: number | null): { bas: number; son: number; enSonda: boolean } {
  const enGeri = Math.max(0, n - boy)
  const bas = ofset === null ? enGeri : Math.max(0, Math.min(ofset, enGeri))
  return { bas, son: Math.min(n, bas + boy), enSonda: bas >= enGeri }
}

/** Yolu karşılaştırma biçimine indirir: / ayraç, küçük harf, sondaki / yok. */
export function yolNormal(yol: string): string {
  return yol.replace(/\\/g, '/').replace(/\/+$/, '').toLowerCase()
}

/** Göreli yolu taban dizine göre mutlaklaştırır (. ve .. çözülür). */
export function yolMutlak(yol: string, taban: string): string {
  const y = yol.replace(/\\/g, '/')
  const mutlak = /^[A-Za-z]:\//.test(y) || y.startsWith('/') ? y : taban.replace(/\\/g, '/').replace(/\/+$/, '') + '/' + y
  const parca: string[] = []
  for (const p of mutlak.split('/')) {
    if (p === '.' || (p === '' && parca.length > 0)) continue
    if (p === '..') parca.pop()
    else parca.push(p)
  }
  return parca.join('/')
}
