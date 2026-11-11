// metin.ts: modelin okuduğu metinler; oda_oku özeti, işçi emri derleyici, araç özeti, prompt bölümü.
// Saf fonksiyonlar; motor ($) almaz, dosya yazmaz.
import type { Oda, OdaGorev, OdaHareket, OdaAltOda, OdaAltOdaMetin } from '../../types'
import { kosan, sinifi } from './durum'
import { kisa, saat } from './ortak'

/** tool.call girdisinden tek satırlık Türkçe özet. */
export function aracOzeti(e: Record<string, unknown>): string {
  const ad = String(e.tool ?? '?')
  const al = (k: string) => (typeof e[k] === 'string' ? (e[k] as string) : undefined)
  if (ad === 'Bash') return `Bash: ${al('description') ?? al('command') ?? ''}`
  if (ad === 'Read' || ad === 'Write' || ad === 'Edit' || ad === 'NotebookEdit') return `${ad}: ${al('file_path') ?? al('notebook_path') ?? ''}`
  if (ad === 'Grep' || ad === 'Glob') return `${ad}: ${al('pattern') ?? ''}${al('path') ? ' @ ' + al('path') : ''}`
  if (ad === 'WebFetch') return `WebFetch: ${al('url') ?? ''}`
  if (ad === 'WebSearch') return `WebSearch: ${al('query') ?? ''}`
  if (ad === 'Agent') return `Agent: ${al('description') ?? ''}`
  if (ad.startsWith('mcp__jarvis-oda__')) return `${ad.replace('mcp__jarvis-oda__', '')}: ${al('metin') ?? ''}`
  const ilk = Object.entries(e).find(([k, v]) => typeof v === 'string' && !['tool', 'tool_use_id', 'agentId'].includes(k))
  return ilk ? `${ad}: ${ilk[1] as string}` : ad
}

/** Görev satırının etiketi: [#N · başlık · sınıf] (A7). */
export function gorevEtiketi(g: OdaGorev | undefined, n = 24): string {
  if (!g) return ''
  return `#${g.id} · ${kisa(g.baslik, n)} · ${sinifi(g)}`
}

/** K52: tek görevin final raporu, kesilmeden (oda_oku gorevId=N). */
export function gorevRaporu(oda: Oda, gorevId: number): string {
  const g = oda.gorevler.find(x => x.id === gorevId)
  if (!g) return `Görev #${gorevId} bu odada yok (${oda.gorevler.length} görev).`
  const bas = `# Görev #${g.id} [${g.durum}] [${sinifi(g)}] ${g.baslik}${g.isId ? ' · iş #' + g.isId : ''}${g.kapanis ? ' · kapanış ' + g.kapanis : ''}`
  const kutuk = g.kutukNot ? `\nkütük: ${g.kutukNot}` : ''
  if (!g.sonuc) return `${bas}${kutuk}\n(henüz final raporu yok; ara raporlar için oda_oku)`
  return `${bas}${kutuk}\n\n${g.sonuc}`
}

export function odaMetni(oda: Oda, son = 12, hareketler: OdaHareket[] = []): string {
  const satirlar: string[] = [`# Oda: ${oda.baslik} (${oda.id}) · açılış ${oda.acilis} · paralel ${kosan(oda)}/${oda.maksParalel}`]
  satirlar.push('## Görevler')
  if (oda.gorevler.length === 0) satirlar.push('(yok)')
  for (const g of oda.gorevler) {
    const model = g.ajan && !g.modelAcik ? 'ajan tanımı' : g.model
    const ek = [g.agentId ? 'ajan ' + g.agentId : '', g.isId ? 'iş #' + g.isId : '', g.butce ? `çağrı ${g.cagri ?? 0}/${g.butce}` : ''].filter(Boolean).join(' · ')
    satirlar.push(`- #${g.id} [${g.durum}] [${sinifi(g)}] ${g.ajan ? '[' + g.ajan + '] ' : ''}${g.baslik} · ${g.zorluk}→${model}${ek ? ' · ' + ek : ''}`)
    if (g.done) satirlar.push('  done: ' + kisa(g.done, 200))
    if (g.dosyalar?.length) satirlar.push('  dosyalar: ' + g.dosyalar.join(', '))
    if (g.sonuc) satirlar.push('  sonuç: ' + kisa(g.sonuc, 400) + (g.sonuc.length > 400 ? ` (tamamı: oda_oku gorevId=${g.id})` : ''))
    if (g.kutukNot) satirlar.push('  kütük: ' + g.kutukNot)
    for (const h of hareketler.filter(x => x.gorevId === g.id).slice(-3)) satirlar.push(`  ${saat(h.ts)} [${h.tur}] ${kisa(h.ozet, 160)}`)
  }
  if (oda.oturumlar?.length) {
    satirlar.push('## Oturumlar (kalıcı)')
    for (const o of oda.oturumlar) satirlar.push(`- ◆ oturum ${o.oturum} [${o.durum === 'katildi' ? 'katıldı' : 'ayrıldı'}]${o.rol ? ' · rol: ' + o.rol : ''}${o.dosyalar.length ? ' · dosyalar: ' + o.dosyalar.join(', ') : ''}${o.son ? ' · son ' + saat(o.son) : ''}`)
  }
  if (oda.altOdalar?.length) {
    satirlar.push('## Alt-odalar')
    for (const a of oda.altOdalar) {
      const asama = a.durum === 'tur' ? `tur ${a.aktifTur}/${a.turSayisi}` : a.durum
      satirlar.push(`- alt-oda #${a.id} [${asama}] ${a.baslik} · ajanlar: ${a.ajanlar.join(', ')} · hakem: ${a.hakem}${a.kutuk ? ' · hedef #' + a.kutuk.hedefId : ''} (tam döküm: oda_oku altOdaId=${a.id})`)
      satirlar.push('  soru: ' + kisa(a.soru, 200))
      if (a.kutukNot) satirlar.push('  kütük: ' + a.kutukNot)
    }
  }
  const bekleyen = oda.oneriler.filter(o => o.durum === 'bekliyor')
  satirlar.push(`## Öneriler (bekleyen ${bekleyen.length})`)
  for (const o of oda.oneriler.slice(-10)) satirlar.push(`- Ö${o.id} [${o.durum}] ${o.kim}: ${kisa(o.metin, 200)} · gerekçe: ${kisa(o.gerekce, 120)}${o.not ? ' · not: ' + o.not : ''}`)
  satirlar.push(`## Son ${son} tur`)
  for (const t of oda.turlar.slice(-son)) satirlar.push(`- ${saat(t.ts)} ${t.kim} [${t.tur}]${t.gorevId ? ' #' + t.gorevId : ''}: ${kisa(t.metin, 300)}`)
  return satirlar.join('\n')
}

const RAPOR_SEMASI = 'Son cevabın rapordur: ne yaptın · dokunulan dosyalar (tam yol) · doğrulama kanıtı (komut + çıktı özeti) · done koşulu sağlandı mı · açık kalan. Övgü yok, kısa cümleler.'
const SOHBET_KURALI = 'Ortak sohbet: "[oda sohbet]" ile başlayan mesaj Salih ya da Jarvis\'ten gelir; kısa cevabını mcp__jarvis-oda__oda_rapor ile ver, sonra işine devam et.'
const ONERI_KURALI = 'Bir karar gerekiyorsa işi durdurma: mcp__jarvis-oda__oda_oneri aracıyla öneri bırak (metin + gerekçe), varsayılan yolu uygulayıp raporunda belirt.'

/**
 * İşçi emri; sınıfa göre bağlam (A5). izole: yalnız emir · planli: + son 3 plan turu ·
 * dosyali: + yazma izni listesi · rol: ajan tanımı, oda bağlamı yok.
 */
export function isciEmri(oda: Oda, g: OdaGorev): string {
  const sinif = sinifi(g)
  const done = g.done ? '\n## Done\n' + g.done : ''
  const butce = g.butce ? `\nAraç çağrısı bütçen ${g.butce}; aşarsan uyarı gelir, 1.5 katında araçların kapanır ve görev hata sayılır.` : ''
  if (sinif === 'rol') {
    return [
      `Bu görev "${oda.baslik}" odasında #${g.id} numarasıyla açıldı; rolün ${g.ajan ?? 'ajan'} ajan tanımındaki gibidir, ona aynen uy. Dil: Türkçe.`,
      'Oda planı, diğer işçilerin raporları ve sohbet sana verilmez (bağlam paylaşmayan rol). Ara not için mcp__jarvis-oda__oda_rapor kullanabilirsin; son cevabın rapordur.',
      '\n## Görev\n' + g.emir,
      done,
    ].join('\n')
  }
  const giris = `Sen "${oda.baslik}" odasının işçi ajanısın (görev #${g.id}, sınıf ${sinif}, model ${g.model}). Dil: Türkçe; kod tanımlayıcıları aslıyla.`
  const kapsam = 'Yalnız bu görevi yap; kapsam dışına çıkma; sormadan tasarım kararı değiştirme.'
  if (sinif === 'izole') {
    return [giris, kapsam, 'Bu görev izoledir: gereken her bilgi aşağıdaki emirdedir; oda planını ya da başka görevleri arama.', ONERI_KURALI, SOHBET_KURALI, RAPOR_SEMASI + butce, '\n## Görev\n' + g.emir, done].join('\n')
  }
  if (sinif === 'dosyali') {
    const liste = (g.dosyalar ?? []).map(d => '- ' + d).join('\n')
    return [
      giris,
      kapsam,
      'Bu görev dosyalıdır: yalnız aşağıdaki dosyaları oku ve yaz. Listede olmayan dosyaya Edit/Write/NotebookEdit oda tarafından reddedilir; Bash ile de başka dosyaya yazma.',
      '\n## Yazma izni olan dosyalar\n' + liste,
      ONERI_KURALI,
      SOHBET_KURALI,
      RAPOR_SEMASI + butce,
      '\n## Görev\n' + g.emir,
      done,
    ].join('\n')
  }
  const plan = oda.turlar.filter(t => t.tur === 'plan').slice(-3).map(t => '- ' + t.metin).join('\n')
  return [
    giris,
    'Jarvis (ana-sıra) planladı, sen uygularsın. ' + kapsam,
    ONERI_KURALI,
    SOHBET_KURALI + ' Ara durum için de oda_rapor kullanabilirsin (kısa, çıplak veri).',
    RAPOR_SEMASI + butce,
    plan ? '\nOda planı (son 3):\n' + plan : '',
    '\n## Görev\n' + g.emir,
    done,
  ].join('\n')
}

// ---------- alt-oda (B9) ----------
// Özgünlük kuralı: ajanın gördüğü metin yalnız bu dosyadaki sabit çerçeve + Jarvis'in soru/kapsam/done alanları
// + diğer ajanların ham metinleridir. Ajan metinleri olduğu gibi yapıştırılır: kısaltma, trim, özet yok.

const ALT_ODA_CERCEVE =
  'Sana soru, kapsam ve done cümlesi dışında yöntem ya da görüş verilmez; yöntemini ve görüşünü sen seçersin. Metnin değiştirilmeden kaydedilir; ortak çıktıyı yalnız hakem tartar. Dil: Türkçe. Son cevabın kaydedilen metindir.'

function altOdaBasligi(odaId: string, a: OdaAltOda, ajan: string): string {
  return [
    `Bu bir alt-oda münazarasıdır: "${a.baslik}" (üst oda ${odaId}, alt-oda #${a.id}). Rolün ${ajan} ajan tanımındaki gibidir; katılımcılar: ${a.ajanlar.join(', ')}.`,
    ALT_ODA_CERCEVE,
    '\n## Soru\n' + a.soru,
    '\n## Kapsam\n' + a.kapsam,
    '\n## Done\n' + a.done,
  ].join('\n')
}

/** Ad etiketli ham metin bloğu; metin dokunulmadan eklenir. */
function etiketliBlok(m: OdaAltOdaMetin): string {
  return `### ${m.ajan}${m.tur ? ' (tur ' + m.tur + ')' : ''}\n` + (m.hata ? `(çağrı başarısız: ${m.hata})` : m.metin)
}

/** Tur r emri: r = 1 yalnız soru/kapsam/done; r > 1 diğerlerinin r-1 metinleri ad etiketli eklenir. */
export function altOdaTurEmri(odaId: string, a: OdaAltOda, ajan: string, tur: number): string {
  const bas = altOdaBasligi(odaId, a, ajan)
  if (tur <= 1) return `${bas}\n\n## Tur 1 / ${a.turSayisi}\nBağımsız ilk görüş: diğer katılımcıların metni bu turda sana verilmez. Kendi cevabını yaz.`
  const onceki = a.turlar.filter(m => m.tur === tur - 1 && m.ajan !== ajan).map(etiketliBlok).join('\n\n')
  return `${bas}\n\n## Tur ${tur} / ${a.turSayisi}\nDiğer katılımcıların tur ${tur - 1} metinleri aşağıdadır. Onları gördükten sonra yanıtını yaz.\n\n## Tur ${tur - 1} metinleri\n${onceki}`
}

/** Son konum emri: münazaranın tamamı + tek paragraf son konum isteği. */
export function altOdaSonKonumEmri(odaId: string, a: OdaAltOda, ajan: string): string {
  return `${altOdaBasligi(odaId, a, ajan)}\n\n## Münazara (tamamı)\n${a.turlar.map(etiketliBlok).join('\n\n')}\n\n## Son konum\nMünazara bitti. Tek paragraf son konumunu yaz.`
}

/** Ortak çıktı = konuşmanın tamamı + ajan başına son konum; ajan metinleri bayt düzeyinde aynen durur. */
export function altOdaOrtakCikti(a: OdaAltOda): string {
  const turlar: string[] = []
  for (let r = 1; r <= a.turSayisi; r++) {
    const bu = a.turlar.filter(m => m.tur === r)
    if (bu.length) turlar.push(`## Tur ${r}\n\n` + bu.map(etiketliBlok).join('\n\n'))
  }
  const son = a.sonKonumlar.length ? '## Son konumlar\n\n' + a.sonKonumlar.map(etiketliBlok).join('\n\n') : ''
  return [...turlar, son].filter(Boolean).join('\n\n')
}

/** Hakem emri: done cümlesi + ortak çıktı; hakem yalnız done'a göre tartar. */
export function altOdaHakemEmri(odaId: string, a: OdaAltOda): string {
  return [
    `Alt-oda #${a.id} "${a.baslik}" (üst oda ${odaId}) münazarasının ortak çıktısını tart. Katılımcılar: ${a.ajanlar.join(', ')}. Rolün ${a.hakem} ajan tanımındaki gibidir. Dil: Türkçe.`,
    'Ölçüt yalnız aşağıdaki done cümlesidir. Ortak çıktı ajanların değiştirilmemiş metinleridir; özet ya da düzeltme yoktur.',
    '\n## Soru\n' + a.soru,
    '\n## Done\n' + a.done,
    '\n# Ortak çıktı\n' + altOdaOrtakCikti(a),
  ].join('\n')
}

/** oda_oku altOdaId=K: tam döküm, kesilmez. */
export function altOdaDokumu(a: OdaAltOda | undefined, k: number, toplam: number): string {
  if (!a) return `Alt-oda #${k} bu odada yok (${toplam} alt-oda).`
  const asama = a.durum === 'tur' ? `tur ${a.aktifTur}/${a.turSayisi}` : a.durum
  return [
    `# Alt-oda #${a.id} [${asama}] ${a.baslik}`,
    `ajanlar: ${a.ajanlar.join(', ')} · hakem: ${a.hakem} · tur sayısı: ${a.turSayisi} · açılış ${a.acilis}${a.kapanis ? ' · kapanış ' + a.kapanis : ''}`,
    a.kutukNot ? 'kütük: ' + a.kutukNot : '',
    '\n## Soru\n' + a.soru,
    '\n## Kapsam\n' + a.kapsam,
    '\n## Done\n' + a.done,
    '\n# Ortak çıktı\n' + (altOdaOrtakCikti(a) || '(henüz metin yok)'),
    '\n# Hakem raporu\n' + (a.hakemRaporu ?? '(henüz yok)'),
  ]
    .filter(s => s !== '')
    .join('\n')
}

export const PROMPT_BOLUMU = [
  '# jarvis-oda (mod)',
  'Oda = Jarvis planlar, işçi ajanlar uygular, ortak sohbet herkesi bağlar. Araçlar: oda_ac(baslik, maksParalel?) · oda_plan(metin) · oda_gorev_ver(baslik, emir, zorluk: kolay|orta|zor → haiku|sonnet|opus, sinif, done, dosyalar?, butce?, isId?, ajan?; sınır doluysa kuyruk) · oda_ayar(maksParalel) · oda_sohbet(metin, hedef "#N"?) · oda_oku · oda_oneri_karar(oneriId, kabul|ret).',
  'İş nodu sınıfı (bağlam karışması freni): görevi, işçinin sınıf dışı bağlama ihtiyaç duymayacağı kadar küçük böl. izole = emir tek başına yeter (varsayılan tercih) · dosyali = dosya listesi ≤ 4, liste dışı yazım reddedilir · planli = son 3 plan turu gerekir · rol = .claude/agents ajanı (yapan ≠ ölçen). Her görevde tek cümle done yaz.',
  'Dış oturumlar (fork, öğrenme sekmeleri, alan ajanları) kalıcıdır ve dosyayla katılır: kendi oturumlarında oda_katil(oturum, rol, dosyalar) ve oda_mesaj(tur, metin); odada "oturum <ad>" görünür, rapor/öneri "[oda dış]" ile seni uyandırır. Onlara oda_sohbet hedef "@<ad>" ile yaz ve SendMessage ile de ilet.',
  'Alt-oda (münazara): oda_altoda_ac(baslik, soru ≤600, kapsam ≤400, done ≤200, ajanlar 2-5 rol ajanı, tur 1-4?, hakem?). Rol ajanları turlu konuşur, ortak çıktıyı yalnız hakem tartar; sen yöntem ya da görüş yazmazsın, çıktıyı düzeltmezsin. Bitince "[oda] alt-oda #K" ile uyanırsın; tam döküm oda_oku altOdaId=K.',
  'Çok-ajanlı iş: planı oda_plan ile yaz, görevleri paralel oda_gorev_ver ile aç, raporları oda_oku ile topla. "[oda]" ile başlayan kuyruk mesajı = görev raporu; "[oda sohbet] salih:" = Salih\'in panodan yazdığı ortak sohbet mesajı, Jarvis ona cevap verir ve gerekirse oda_sohbet ile işçilere iletir. Öneri kararı Salih\'indir: bekleyen öneriyi tek satırda sun.',
].join('\n')
