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
  ac_ts?: string | null
  kapat_ts?: string | null
  kayit?: string | null
  oturumlar?: string[]
}

export type GrafKenar = { k: string; h: string; tur: string }

export type Graf = {
  meta: Record<string, unknown>
  dugumler: GrafDugum[]
  kenarlar: GrafKenar[]
}

export type GrafGorunum = {
  alan: string
  yalnizAcik: boolean
  secili: string | null
  yol: string
  mtimeMs: number
  hata: string | null
}

declare module 'claude-code' {
  interface PluginState {
    'jarvis-graf': { graf: Graf | null; gorunum: GrafGorunum }
  }
}
