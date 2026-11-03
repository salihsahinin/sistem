// pano.tsx: oda panosunun çizimi; bölümler (görevler · öneriler · sohbet · canlı akış · olaylar).
// Durumu okur, yazmaz: her düğme araclar.ts eylemini çağırır.
import type { EngineInterface, RenderElement } from 'claude-code'

import type { Oda, OdaGorev, OdaHareket, OdaListe, OdaBolum, OdaPano, OdaTur, AjanDurum } from '../../types'
import { odaGoruntu, ajanlariOku, hareketleriOku, panoOku, PENCERE_BOY, kosan, kuyrukSayisi, sinifi, satirAnahtari } from './durum'
import { gorevEtiketi } from './metin'
import { kisa, saat, isciRengi, pencere } from './ortak'
import {
  sohbetGonder,
  sinirAyarla,
  oneriKarar,
  bolumAcKapa,
  pencereKaydir,
  genisAcKapa,
  isciyiIzle,
  anaSohbeteDon,
  grafdaGoster,
} from './araclar'

// Motorun eleman tablosu; masaüstü tablosu en geniş olanıdır, diğer yüzeyler alt kümesi.
type Tablo = ReturnType<EngineInterface['ui']['resolve']>
type El = { Box: (p: any) => RenderElement; Text: (p: any) => RenderElement; Button: (p: any) => RenderElement; Markdown?: (p: any) => RenderElement }

type Baglam = {
  T: El
  oda: Oda
  pano: OdaPano
  izlenen?: string
  gorev: (id?: number) => OdaGorev | undefined
}

const DURUM_IMI: Record<string, string> = { kosuyor: '●', bitti: '✓', hata: '✗', bekliyor: '○' }
const DURUM_RENGI: Record<string, string | undefined> = { kosuyor: 'yellow', bitti: 'green', hata: 'red' }
const BOLUM_ADI: Record<OdaBolum, string> = { gorevler: 'Görevler', oneriler: 'Karar bekleyen öneriler', sohbet: 'Ortak sohbet (Salih · Jarvis · işçiler)', akis: 'Canlı akış (tüm işçiler)', olaylar: 'Son olaylar' }

/** Bölüm başlığı: ▾/▸ düğmesi (A3). */
function Baslik($: EngineInterface, b: Baglam, bolum: OdaBolum, sayi: string, renk?: string): RenderElement {
  const { Button, Text } = b.T
  const acik = b.pano.acik.includes(bolum)
  return (
    <Button key={'bolum-' + bolum} plain onPress={() => void bolumAcKapa($, bolum)}>
      <Text bold color={renk} dimColor={!renk}>
        {acik ? '▾ ' : '▸ '}
        {BOLUM_ADI[bolum]} <Text dimColor>({sayi})</Text>
      </Text>
    </Button>
  )
}

/** Pencere gezinti satırı (A2): ◀ önceki · sonraki ▶ · en son, ve konum. */
function Gezinti($: EngineInterface, b: Baglam, liste: OdaListe, n: number): RenderElement | null {
  const { Box, Text, Button } = b.T
  const boy = PENCERE_BOY[liste]
  if (n <= boy) return null
  const p = pencere(n, boy, b.pano.ofset[liste])
  return (
    <Box key={'gez-' + liste} flexDirection="row" gap={1} flexWrap="wrap">
      <Button key={'gez-' + liste + '-geri'} plain dimColor={p.bas === 0} onPress={() => void pencereKaydir($, liste, n, -1)}>
        ◀ önceki {boy}
      </Button>
      <Text dimColor>
        {p.bas + 1}–{p.son} / {n}
      </Text>
      <Button key={'gez-' + liste + '-ileri'} plain dimColor={p.enSonda} onPress={() => void pencereKaydir($, liste, n, 1)}>
        sonraki {boy} ▶
      </Button>
      {!p.enSonda && (
        <Button key={'gez-' + liste + '-son'} plain onPress={() => void pencereKaydir($, liste, n, 0)}>
          en son ⇥
        </Button>
      )}
    </Box>
  )
}

/** İşçi düğmesi (A1): rengi görev numarasından; basınca ana transkript o işçiye geçer. */
function IsciDugmesi($: EngineInterface, b: Baglam, g: OdaGorev | undefined, yazi: string, anahtar: string): RenderElement {
  const { Button, Text } = b.T
  if (!g) return <Text key={anahtar} bold color="green">{yazi}</Text>
  const izleniyor = b.izlenen && b.izlenen === g.agentId
  return (
    <Button key={anahtar} plain onPress={() => void isciyiIzle($, g.agentId)}>
      <Text bold color={isciRengi(g.id)} underline={Boolean(izleniyor)}>
        {izleniyor ? '▶ ' : ''}
        {yazi}
      </Text>
    </Button>
  )
}

function GorevSatiri($: EngineInterface, b: Baglam, g: OdaGorev, a: AjanDurum | undefined, hareketler: OdaHareket[]): RenderElement {
  const { Box, Text, Button } = b.T
  const model = g.ajan && !g.modelAcik ? 'ajan tanımı' : g.model
  const durumYazi = g.durum === 'bekliyor' ? 'kuyrukta' : a ? a.status : g.durum
  const asim = g.butce && (g.cagri ?? 0) >= g.butce
  return (
    <Box key={'gorev-' + g.id} flexDirection="column">
      <Box flexDirection="row" gap={1} flexWrap="wrap" alignItems="center">
        <Text color={DURUM_RENGI[g.durum]}>{DURUM_IMI[g.durum] ?? '○'}</Text>
        {IsciDugmesi($, b, g, `#${g.id} ${kisa(g.baslik, 48)}`, 'izle-' + g.id)}
        <Text color="magenta">[{sinifi(g)}]</Text>
        {g.ajan ? <Text color="magenta">[{g.ajan}]</Text> : null}
        <Text dimColor>
          {g.zorluk}→{model} · {durumYazi}
        </Text>
        {g.butce ? <Text color={asim ? 'red' : undefined} dimColor={!asim}>çağrı {g.cagri ?? 0}/{g.butce}</Text> : null}
        {g.isId ? (
          <Button key={'is-' + g.id} plain onPress={() => void grafdaGoster($, g.isId!)}>
            <Text color="cyan">iş #{g.isId} ↗</Text>
          </Button>
        ) : null}
      </Box>
      {g.done && (
        <Text dimColor>
          {'   done: '}
          {kisa(g.done, 140)}
        </Text>
      )}
      {g.dosyalar?.length ? (
        <Text dimColor>
          {'   dosyalar: '}
          {g.dosyalar.map(d => d.split('/').pop()).join(', ')}
        </Text>
      ) : null}
      {g.sonuc && RaporGovdesi($, b, { ts: g.kapanis ?? g.acilis, kim: 'sonuc#' + g.id, metin: g.sonuc }, 110, '   ')}
      {g.durum === 'kosuyor' &&
        hareketler
          .filter(x => x.gorevId === g.id)
          .slice(-2)
          .map((hr, i) => (
            <Text key={'gh-' + g.id + '-' + i} dimColor>
              {'   '}
              <Text color={hr.tur === 'arac' ? 'blue' : undefined}>{hr.tur === 'arac' ? '⚙' : '…'}</Text> {kisa(hr.ozet, 100)}
            </Text>
          ))}
    </Box>
  )
}

/** Uzun metin: kısa hâli + ▸ tam düğmesi; açıkken Markdown ile tam metin (A7). */
function RaporGovdesi($: EngineInterface, b: Baglam, t: { ts: string; kim: string; metin: string }, n: number, girinti = ''): RenderElement {
  const { Box, Text, Button } = b.T
  const anahtar = satirAnahtari(t)
  const acik = b.pano.genis.includes(anahtar)
  const uzun = t.metin.replace(/\s+/g, ' ').trim().length > n
  if (!uzun) return <Text key={'rg-' + anahtar} dimColor>{girinti}{t.metin}</Text>
  return (
    <Box key={'rg-' + anahtar} flexDirection="column">
      <Box flexDirection="row" gap={1}>
        {girinti ? <Text>{girinti}</Text> : null}
        <Button key={'genis-' + anahtar} plain onPress={() => void genisAcKapa($, anahtar)}>
          <Text color="cyan">{acik ? '▾ kapat' : '▸ tam'}</Text>
        </Button>
        {!acik && <Text dimColor>{kisa(t.metin, n)}</Text>}
      </Box>
      {acik && (b.T.Markdown ? <b.T.Markdown key={'md-' + anahtar} text={t.metin} /> : <Text>{t.metin}</Text>)}
    </Box>
  )
}

/** Sohbet satırı (A1 + A7): saat · kim düğmesi · [#N · başlık · sınıf] · metin. */
function SohbetSatiri($: EngineInterface, b: Baglam, t: OdaTur, i: number): RenderElement {
  const { Box, Text } = b.T
  const g = b.gorev(t.gorevId)
  const kimNo = /^işçi #(\d+)$/.exec(t.kim)?.[1]
  const kimGorev = kimNo ? b.gorev(Number(kimNo)) : undefined
  const kimEl =
    t.kim === 'salih' ? (
      <Text key={'kim-' + i} bold color="cyan">salih</Text>
    ) : t.kim === 'jarvis' ? (
      <Text key={'kim-' + i} bold color="magenta">jarvis</Text>
    ) : (
      IsciDugmesi($, b, kimGorev, t.kim, 'kim-' + i)
    )
  const etiketGorev = kimGorev ?? g
  return (
    <Box key={'sohbet-' + i} flexDirection="column">
      <Box flexDirection="row" gap={1} flexWrap="wrap">
        <Text dimColor>{saat(t.ts, false)}</Text>
        {kimEl}
        {etiketGorev ? <Text color={isciRengi(etiketGorev.id)} dimColor>[{gorevEtiketi(etiketGorev)}]</Text> : null}
        {t.tur === 'rapor' ? <Text dimColor>[rapor]</Text> : null}
      </Box>
      {RaporGovdesi($, b, t, t.tur === 'rapor' ? 120 : 240, '  ')}
    </Box>
  )
}

function AkisSatiri($: EngineInterface, b: Baglam, hr: OdaHareket, i: number): RenderElement {
  const { Box, Text } = b.T
  const g = b.gorev(hr.gorevId)
  return (
    <Box key={'akis-' + i} flexDirection="row" gap={1} flexWrap="wrap">
      <Text dimColor>{saat(hr.ts)}</Text>
      {IsciDugmesi($, b, g, `#${hr.gorevId}`, 'akis-isci-' + i)}
      {g ? <Text color={isciRengi(g.id)} dimColor>[{kisa(g.baslik, 24)} · {sinifi(g)}]</Text> : null}
      <Text color={hr.tur === 'arac' ? 'blue' : undefined}>{hr.tur === 'arac' ? '⚙' : '…'}</Text>
      <Text>{kisa(hr.ozet, 140)}</Text>
    </Box>
  )
}

export async function panoCiz($: EngineInterface, e: { surface: string; props?: unknown }): Promise<RenderElement> {
  const T = $.ui.resolve(e as Parameters<EngineInterface['ui']['resolve']>[0]) as unknown as El & Tablo
  const { Box, Text, Button } = T
  const oda = await odaGoruntu($)
  if (!oda) {
    return (
      <Box flexDirection="column" padding={1}>
        <Text bold>Oda yok.</Text>
        <Text dimColor>Jarvis'e "oda aç: &lt;başlık&gt;" de; oda_ac aracı açar.</Text>
      </Box>
    )
  }
  const ajanlar = await ajanlariOku($)
  const hareketler = await hareketleriOku($)
  const pano = await panoOku($)
  const izlenen = (e.props as { view?: { agentId?: string } } | undefined)?.view?.agentId
  const harita = new Map(oda.gorevler.map(g => [g.id, g]))
  const b: Baglam = { T, oda, pano, izlenen, gorev: id => (id === undefined ? undefined : harita.get(id)) }
  const acik = (x: OdaBolum) => pano.acik.includes(x)
  const izlenenGorev = izlenen ? oda.gorevler.find(g => g.agentId === izlenen) : undefined

  const bekleyen = oda.oneriler.filter(o => o.durum === 'bekliyor')
  const sohbet = oda.turlar.filter(t => t.tur === 'sohbet' || t.tur === 'rapor')
  const olaylar = oda.turlar.filter(t => t.tur !== 'sohbet' && t.tur !== 'rapor')
  const pSohbet = pencere(sohbet.length, PENCERE_BOY.sohbet, pano.ofset.sohbet)
  const pAkis = pencere(hareketler.length, PENCERE_BOY.akis, pano.ofset.akis)
  const pOlay = pencere(olaylar.length, PENCERE_BOY.olaylar, pano.ofset.olaylar)

  const sohbetGirisi =
    e.surface === 'mobile' ? (
      <Text key="sohbet-mobil" dimColor>(mobilde giriş alanı yok; sohbet için Jarvis'e yaz)</Text>
    ) : (
      (() => {
        const { Input } = T as unknown as { Input: (p: any) => RenderElement }
        return <Input key="sohbet-giris" placeholder="herkese yaz; tek işçi için '#2 …'" submitLabel="gönder" onSubmit={(value: string) => void sohbetGonder($, 'salih', value)} />
      })()
    )

  return (
    <Box flexDirection="column" padding={1} gap={1}>
      <Box flexDirection="row" justifyContent="space-between" flexWrap="wrap">
        <Text bold>Oda · {oda.baslik}</Text>
        <Button key="yenile" plain onPress={() => $.ui.invalidate('ui.render')}>
          ⟳
        </Button>
      </Box>
      {izlenen && (
        <Box key="izleme-bandi" flexDirection="row" gap={1} flexWrap="wrap" borderStyle="round" paddingX={1}>
          <Button key="ana-sohbet" variant="primary" onPress={() => void anaSohbeteDon($)}>
            ◀ ana sohbete dön
          </Button>
          <Text>
            izlenen: <Text bold color={izlenenGorev ? isciRengi(izlenenGorev.id) : 'green'}>{izlenenGorev ? gorevEtiketi(izlenenGorev, 40) : izlenen}</Text>
          </Text>
        </Box>
      )}
      <Box flexDirection="row" gap={1} alignItems="center">
        <Text>
          koşan <Text bold color={kosan(oda) > 0 ? 'yellow' : undefined}>{kosan(oda)}</Text> / sınır <Text bold>{oda.maksParalel}</Text>
          <Text dimColor> · kuyruk {kuyrukSayisi(oda)}</Text>
        </Text>
        <Button key="sinir-az" plain onPress={() => void sinirAyarla($, 'salih', x => x - 1)}>
          −
        </Button>
        <Button key="sinir-cok" plain onPress={() => void sinirAyarla($, 'salih', x => x + 1)}>
          +
        </Button>
      </Box>

      <Box key="b-gorevler" flexDirection="column">
        {Baslik($, b, 'gorevler', String(oda.gorevler.length))}
        {acik('gorevler') && oda.gorevler.length === 0 && <Text dimColor>Henüz görev yok.</Text>}
        {acik('gorevler') && oda.gorevler.map(g => GorevSatiri($, b, g, ajanlar.find(x => x.gorevId === g.id), hareketler))}
      </Box>

      {bekleyen.length > 0 && (
        <Box key="b-oneriler" flexDirection="column">
          {Baslik($, b, 'oneriler', String(bekleyen.length), 'yellow')}
          {acik('oneriler') &&
            bekleyen.map(o => (
              <Box key={'oneri-' + o.id} flexDirection="column">
                <Text>
                  Ö{o.id} <Text dimColor>{o.kim}:</Text> {kisa(o.metin, 160)}
                </Text>
                <Text dimColor>
                  {'   gerekçe: '}
                  {kisa(o.gerekce, 140)}
                </Text>
                <Box flexDirection="row" gap={1}>
                  <Button key={'kabul-' + o.id} variant="primary" onPress={() => void oneriKarar($, 'salih', o.id, 'kabul')}>
                    Kabul
                  </Button>
                  <Button key={'ret-' + o.id} onPress={() => void oneriKarar($, 'salih', o.id, 'ret')}>
                    Ret
                  </Button>
                </Box>
              </Box>
            ))}
        </Box>
      )}

      <Box key="b-sohbet" flexDirection="column">
        {Baslik($, b, 'sohbet', String(sohbet.length))}
        {acik('sohbet') && Gezinti($, b, 'sohbet', sohbet.length)}
        {acik('sohbet') && sohbet.length === 0 && <Text dimColor>Henüz mesaj yok.</Text>}
        {acik('sohbet') && sohbet.slice(pSohbet.bas, pSohbet.son).map((t, i) => SohbetSatiri($, b, t, pSohbet.bas + i))}
        {acik('sohbet') && sohbetGirisi}
      </Box>

      <Box key="b-akis" flexDirection="column">
        {Baslik($, b, 'akis', String(hareketler.length))}
        {acik('akis') && Gezinti($, b, 'akis', hareketler.length)}
        {acik('akis') && hareketler.length === 0 && <Text dimColor>Henüz hareket yok.</Text>}
        {acik('akis') && hareketler.slice(pAkis.bas, pAkis.son).map((hr, i) => AkisSatiri($, b, hr, pAkis.bas + i))}
      </Box>

      <Box key="b-olaylar" flexDirection="column">
        {Baslik($, b, 'olaylar', String(olaylar.length))}
        {acik('olaylar') && Gezinti($, b, 'olaylar', olaylar.length)}
        {acik('olaylar') &&
          olaylar.slice(pOlay.bas, pOlay.son).map((t, i) => (
            <Text key={'olay-' + (pOlay.bas + i)} dimColor>
              {saat(t.ts, false)} {t.kim} [{t.tur}] {kisa(t.metin, 120)}
            </Text>
          ))}
      </Box>
    </Box>
  )
}
