export type GrafDugum = {
  id: string
  tur: 'seans' | 'hedef' | 'is'
  alan: string
  etiket: string
  durum?: string | null
  sonraki_eylem?: string | null
  hedef?: string | null
  hedef_tutuldu?: boolean | null
  acilis_ts?: string | null
  al_ts?: string | null
  bitir_ts?: string | null
  ac_ts?: string | null
  kapat_ts?: string | null
  kayit?: string | null
  oturumlar?: string[]
  sirada?: boolean
  ortuk?: boolean
  dokunulan?: string[]
}

export type GrafKenar = { k: string; h: string; tur: string }

export type Graf = {
  meta: Record<string, unknown>
  dugumler: GrafDugum[]
  kenarlar: GrafKenar[]
}

/** ortak/durum-olay.jsonl satırı (yalnız okunan alanlar). */
export type KutukOlay = {
  olay: string
  ts: string
  id?: number
  alan?: string
  is?: string
  sonraki_eylem?: string
  oturum?: string
  kanit?: string[]
  hedef_cumle?: string
  hedef_tutuldu?: boolean
  kayit?: string
  etiket?: string
}

/** Graf yanında okunan kaynaklar: kütük olayları ve karar defteri (B3). */
export type GrafEk = {
  olaylar: KutukOlay[]
  defter: string
  olayMtime: number
  defterMtime: number
}

export type GrafGorunum = {
  alan: string
  yalnizAcik: boolean
  secili: string | null
  yol: string
  mtimeMs: number
  hata: string | null
  /** B4: son üretilen HTML'in yolu ve hata metni (kalıcı, toast değil). */
  html: string | null
  htmlHata: string | null
  /** B5: oda köprüsünden en son işlenen seçim zamanı. */
  kopruTs: string
}

declare module 'claude-code' {
  interface PluginState {
    'jarvis-graf': { graf: Graf | null; gorunum: GrafGorunum; ek: GrafEk }
  }
}
