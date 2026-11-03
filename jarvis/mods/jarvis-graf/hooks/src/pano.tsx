// pano.tsx: akış grafı panosunun çizimi; üst çubuk, SVG (B1), tıklanabilir seans ızgarası (B2), detay (B3), HTML bağlantısı (B4).
// Durumu okur, yazmaz: düğmeler araclar.ts eylemlerini çağırır.
import type { EngineInterface, RenderElement } from 'claude-code'

import type { Graf, GrafDugum, GrafGorunum } from '../../types'
import { grafOku, gorunumOku, ekOku, grafYukle } from './durum'
import { satirlar, detay, gorunenler, acikMi, type Satir } from './metin'
import { svgCiz, dolgu } from './cizim'
import { kisa, tarihSaat } from './ortak'
import { htmlAc, durumGrafYenile, sec, alanSec, yalnizAcikDegistir, htmlBildirimKapat, dosyaAc, explorerdaGoster, yoluKopyala } from './araclar'

type El = { Box: (p: any) => RenderElement; Text: (p: any) => RenderElement; Button: (p: any) => RenderElement; Markdown: (p: any) => RenderElement }

const IM: Record<string, string> = { tamam: '✓', tuketildi: '✓', islemde: '●', bayat: '·', acik: '○' }
const TS_ALANI = new Set(['açılış', 'kapanış', 'alındı', 'bitti'])

/** Dosya satırı: ad + aç · kopyala · Explorer düğmeleri (masaüstü file:// bağlantısı üretmez). */
function DosyaSatiri($: EngineInterface, T: El, anahtar: string, etiket: string, dosya: string, surface: string): RenderElement {
  const { Box, Text, Button } = T
  return (
    <Box key={anahtar} flexDirection="row" flexWrap="wrap" gap={1} alignItems="center">
      <Text>{etiket}</Text>
      <Button key={anahtar + '-ac'} plain onPress={() => void dosyaAc($, dosya)}>
        <Text color="cyan">▶ aç</Text>
      </Button>
      <Button key={anahtar + '-kopyala'} plain onPress={() => void yoluKopyala($, dosya, surface)}>
        <Text color="cyan">kopyala</Text>
      </Button>
      <Button key={anahtar + '-explorer'} plain onPress={() => void explorerdaGoster($, dosya)}>
        <Text color="cyan">Explorer</Text>
      </Button>
    </Box>
  )
}

function Izgara($: EngineInterface, T: El, sat: Satir[], gor: GrafGorunum, sutun: number): RenderElement {
  const { Box, Text, Button } = T
  const n = Math.max(18, Math.min(34, Math.floor(sutun / 4)))
  return (
    <Box key="izgara" flexDirection="column" gap={0}>
      {sat.map(s => (
        <Box key={'satir-' + s.anahtar} flexDirection="row" flexWrap="wrap" gap={1} alignItems="center">
          <Button key={'sec-' + s.anahtar} plain onPress={() => void sec($, s.anahtar)}>
            <Text bold={gor.secili === s.anahtar} color={s.tur === 'hedef' ? 'magenta' : s.tur === 'oturum' ? 'cyan' : undefined}>
              {s.tur === 'hedef' ? '◆ hedefler' : (s.tur === 'oturum' ? '◇ ' : '▣ ') + kisa(s.etiket, 28)}
            </Text>
          </Button>
          {s.dugumler.length === 0 && <Text dimColor>(iş açmadı)</Text>}
          {s.dugumler.map(d => (
            <Button key={'sec-' + d.id} plain dimColor={d.durum === 'tamam' || d.durum === 'bayat' || d.durum === 'tuketildi'} onPress={() => void sec($, d.id)}>
              <Text color={dolgu(d)} bold={gor.secili === d.id} inverse={gor.secili === d.id}>
                {IM[d.durum ?? ''] ?? '○'}#{d.id.split(':')[1]}
              </Text>
              <Text dimColor> {kisa(d.etiket, n)}</Text>
            </Button>
          ))}
        </Box>
      ))}
    </Box>
  )
}

function Detay($: EngineInterface, T: El, graf: Graf, sat: Satir[], secili: string, ek: Awaited<ReturnType<typeof ekOku>>, depo: string, surface: string): RenderElement {
  const { Box, Text, Button, Markdown } = T
  const kapat = (
    <Button key="detay-kapat" plain onPress={() => void sec($, null)}>
      ✕ kapat
    </Button>
  )
  const sanal = sat.find(s => s.anahtar === secili && s.tur !== 'seans')
  if (sanal) {
    return (
      <Box key="detay" flexDirection="column" borderStyle="round" paddingX={1}>
        <Box flexDirection="row" justifyContent="space-between">
          <Text bold>{sanal.tur === 'hedef' ? 'Hedefler' : 'oturum ' + sanal.etiket}</Text>
          {kapat}
        </Box>
        <Text dimColor>{sanal.tur === 'oturum' ? 'Kütükte seans kaydı olmayan oturum (ör. oda görevleri, yan oturum).' : 'Hedef düğümleri; altlarındaki işler hizmet kenarıyla bağlı.'}</Text>
        {sanal.dugumler.map(d => (
          <Button key={'sd-' + d.id} plain onPress={() => void sec($, d.id)}>
            <Text color={dolgu(d)}>{IM[d.durum ?? ''] ?? '○'}#{d.id.split(':')[1]}</Text> {kisa(d.etiket, 90)}
          </Button>
        ))}
      </Box>
    )
  }
  const dt = detay(graf, ek, secili)
  if (!dt) return <Text key="detay-yok" color="red">{secili} grafta yok.</Text>
  const n: GrafDugum = dt.dugum
  return (
    <Box key="detay" flexDirection="column" borderStyle="round" paddingX={1} gap={1}>
      <Box flexDirection="row" justifyContent="space-between" flexWrap="wrap">
        <Text bold>
          <Text color={dolgu(n)}>{dt.baslik}</Text> <Text dimColor>· {n.alan}</Text>
        </Text>
        {kapat}
      </Box>
      <Text>{n.etiket}</Text>
      <Box flexDirection="column">
        {dt.satirlar.map((s, i) => (
          <Text key={'ds-' + i}>
            <Text dimColor>{s.ad}: </Text>
            {TS_ALANI.has(s.ad) ? tarihSaat(s.deger) : s.deger}
          </Text>
        ))}
      </Box>
      {n.oturumlar?.length ? (
        <Box flexDirection="row" flexWrap="wrap" gap={1}>
          <Text dimColor>oturumlar:</Text>
          {n.oturumlar.map(o => {
            const hedef = graf.dugumler.find(d => d.tur === 'seans' && d.etiket === o)?.id ?? 'oturum:' + o
            return (
              <Button key={'ot-' + o} plain onPress={() => void sec($, hedef)}>
                <Text color="cyan">{o}</Text>
              </Button>
            )
          })}
        </Box>
      ) : null}
      {dt.baglar.length > 0 && (
        <Box flexDirection="column">
          <Text bold dimColor>
            Bağlar ({dt.baglar.length})
          </Text>
          {dt.baglar.slice(0, 30).map((b, i) => (
            <Button key={'bag-' + i + '-' + b.id} plain onPress={() => void sec($, b.id)}>
              <Text dimColor>{b.ne}: </Text>
              {b.id.startsWith('seans:') ? <Text color="cyan">{b.etiket}</Text> : <Text color="cyan">#{b.id.split(':')[1]} <Text>{b.etiket}</Text></Text>}
            </Button>
          ))}
        </Box>
      )}
      {dt.olaylar.length > 0 && (
        <Box flexDirection="column">
          <Text bold dimColor>
            Kütük olayları ({dt.olaylar.length})
          </Text>
          {dt.olaylar.slice(-20).map((o, i) => (
            <Box key={'ol-' + i} flexDirection="column">
              <Text>
                <Text dimColor>{tarihSaat(o.ts)}</Text> {o.olay}
                {o.oturum ? <Text dimColor> · {o.oturum}</Text> : null}
                {o.not && n.tur === 'seans' ? <Text dimColor> · {o.not}</Text> : null}
              </Text>
              {o.kanit.map((k, j) => (
                <Text key={'kn-' + i + '-' + j} dimColor>
                  {'   kanıt: '}
                  {k}
                </Text>
              ))}
            </Box>
          ))}
        </Box>
      )}
      {dt.defter && (
        <Box flexDirection="column">
          <Text bold dimColor>
            Karar {dt.defter.no} (kuyruk/senaryo-defteri.md)
          </Text>
          <Markdown key="defter" text={dt.defter.metin} />
        </Box>
      )}
      {dt.kayit && depo ? DosyaSatiri($, T, 'kayit', 'seans teslim kaydı: ' + dt.kayit, depo + '/' + dt.kayit, surface) : null}
    </Box>
  )
}

export async function panoCiz($: EngineInterface, e: { surface: string; props?: unknown; viewport?: { columns?: number } }): Promise<RenderElement> {
  const T = $.ui.resolve(e as Parameters<EngineInterface['ui']['resolve']>[0]) as unknown as El
  const { Box, Text, Button } = T
  const graf = await grafOku($)
  const gor = await gorunumOku($)
  const sutun = (e.props as { bodyColumns?: number } | undefined)?.bodyColumns ?? e.viewport?.columns ?? 100

  if (!graf) {
    return (
      <Box flexDirection="column" padding={1}>
        <Text bold>Akış grafı</Text>
        <Text color="red">{gor.hata ?? 'Henüz yüklenmedi.'}</Text>
        <Button key="yenile" onPress={() => void grafYukle($, true)}>
          Yenile
        </Button>
      </Box>
    )
  }
  const ek = await ekOku($)
  const sat = satirlar(graf, gor)
  const gorunen = gorunenler(graf, gor)
  const acik = gorunen.filter(acikMi).length
  const alanlar = Array.from(new Set(graf.dugumler.map(n => n.alan).filter(Boolean)))
  const depo = gor.yol.replace(/\/ortak\/akis-graf\.json$/, '')

  const resim =
    e.surface === 'desktop' || e.surface === 'mobile' || e.surface === 'vscode'
      ? (() => {
          const { Svg } = $.ui.resolve(e as Parameters<EngineInterface['ui']['resolve']>[0]) as unknown as { Svg: (p: any) => RenderElement }
          const px = Math.max(900, sutun * 8)
          return <Svg key="svg" source={svgCiz(graf, sat, gor.secili, px)} alt={`Akış grafı: ${sat.length} satır (hedefler ve seanslar), ${gorunen.length} düğüm; x ekseni zaman, renk durum`} width={px} isInteractive />
        })()
      : null

  return (
    <Box flexDirection="column" padding={1} gap={1}>
      <Box flexDirection="row" justifyContent="space-between" flexWrap="wrap" gap={1}>
        <Text bold>
          Akış grafı{' '}
          <Text dimColor>
            · {String(graf.meta.tarih ?? '')} · {sat.length} satır · {gorunen.length}/{graf.dugumler.length} düğüm · {acik} açık
          </Text>
        </Text>
        <Box flexDirection="row" gap={1}>
          <Button key="yenile" plain onPress={() => void grafYukle($, true)}>
            ⟳ yenile
          </Button>
          <Button key="html" plain onPress={() => void htmlAc($)}>
            HTML aç
          </Button>
          <Button key="d2" plain onPress={() => void durumGrafYenile($)}>
            durum graf
          </Button>
        </Box>
      </Box>
      {(gor.html || gor.htmlHata) && (
        <Box key="html-bandi" flexDirection="row" flexWrap="wrap" gap={1}>
          {gor.htmlHata && <Text color={gor.htmlHata.startsWith('HTML üretiliyor') ? 'yellow' : 'red'}>{gor.htmlHata}</Text>}
          {gor.html ? DosyaSatiri($, T, 'html-dosya', 'HTML: ' + gor.html.replace(/\\/g, '/').split('/').pop(), gor.html, e.surface) : null}
          {gor.htmlHata && (
            <Button key="html-kapat" plain onPress={() => void htmlBildirimKapat($)}>
              ✕
            </Button>
          )}
        </Box>
      )}
      <Box flexDirection="row" gap={1} flexWrap="wrap">
        {['tum', ...alanlar].map(a => (
          <Button key={'alan-' + a} plain dimColor={gor.alan !== a} onPress={() => void alanSec($, a)}>
            {gor.alan === a ? '[' + a + ']' : a}
          </Button>
        ))}
        <Button key="acik" plain dimColor={!gor.yalnizAcik} onPress={() => void yalnizAcikDegistir($)}>
          {gor.yalnizAcik ? '[yalnız açık]' : 'yalnız açık'}
        </Button>
      </Box>
      {gor.hata && <Text color="red">{gor.hata}</Text>}
      {gor.secili && Detay($, T, graf, sat, gor.secili, ek, depo, e.surface)}
      {resim}
      <Text bold dimColor>
        Seanslar ve işleri · bir düğmeye tıkla, detay yukarıda açılır
      </Text>
      {Izgara($, T, sat, gor, sutun)}
    </Box>
  )
}
