export type OdaZorluk = 'kolay' | 'orta' | 'zor'
export type OdaGorevDurum = 'bekliyor' | 'kosuyor' | 'bitti' | 'hata'
export type OdaTurTuru = 'plan' | 'gorev' | 'rapor' | 'oneri' | 'karar' | 'not' | 'sohbet'

export type OdaTur = {
  ts: string
  kim: string
  tur: OdaTurTuru
  metin: string
  gorevId?: number
}

export type OdaGorev = {
  id: number
  baslik: string
  emir: string
  zorluk: OdaZorluk
  model: string
  durum: OdaGorevDurum
  agentId?: string
  acilis: string
  kapanis?: string
  sonuc?: string
}

export type OdaOneri = {
  id: number
  kim: string
  gorevId?: number
  metin: string
  gerekce: string
  durum: 'bekliyor' | 'kabul' | 'ret'
  not?: string
}

export type Oda = {
  id: string
  baslik: string
  acilis: string
  maksParalel: number
  turlar: OdaTur[]
  gorevler: OdaGorev[]
  oneriler: OdaOneri[]
}

export type AjanDurum = { agentId: string; status: string; gorevId: number }

declare module 'claude-code' {
  interface PluginState {
    'jarvis-oda': { oda: Oda | null; ajanlar: AjanDurum[] }
  }
}
