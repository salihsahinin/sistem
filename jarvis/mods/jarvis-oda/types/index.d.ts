export type OdaZorluk = 'kolay' | 'orta' | 'zor'
export type OdaGorevDurum = 'bekliyor' | 'kosuyor' | 'bitti' | 'hata'
export type OdaTurTuru = 'plan' | 'gorev' | 'rapor' | 'oneri' | 'karar' | 'not' | 'sohbet'

/**
 * v0.5 (A5): iş nodu sınıfı; işçinin göreceği bağlamı sınırlar (bağlam karışması freni).
 * izole = yalnız emir · planli = emir + son 3 plan turu · dosyali = emir + yazma izni listesi · rol = .claude/agents/<ad>.md
 */
export type OdaSinif = 'izole' | 'planli' | 'dosyali' | 'rol'

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
  /** v0.4: .claude/agents/<ad>.md ajan tipi; verilirse subagentType olur, plan bağlamı emre eklenmez. */
  ajan?: string
  /** v0.4: model alanı açıkça verildi mi (ajan tanımının modelini ezmek için). */
  modelAcik?: boolean
  /** v0.5: iş nodu sınıfı (eski kayıtta yok: planli sayılır). */
  sinif?: OdaSinif
  /** v0.5: dosyali sınıfında yazma izni olan dosyalar (mutlak, / ayraçlı). */
  dosyalar?: string[]
  /** v0.5: tek cümle done koşulu. */
  done?: string
  /** v0.5: araç çağrısı tavanı. */
  butce?: number
  /** v0.5: şimdiye dek araç çağrısı sayısı. */
  cagri?: number
  /** v0.5 (A4): bağlı durum kütüğü iş numarası (ortak/durum-olay.jsonl). */
  isId?: number
  /** v0.7 (K52): kütük işinin son hali; `al`/`bitir` sonucu ya da işin neden açık kaldığı. */
  kutukNot?: string
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

/**
 * C1: odaya dosya üzerinden katılan kalıcı dış oturum (fork, öğrenme sekmesi, alan ajanı).
 * Tek görevlik işçi değildir; kapanınca silinmez, durum 'ayrildi' olur.
 */
export type OdaOturum = {
  oturum: string
  rol: string
  dosyalar: string[]
  acilis: string
  durum: 'katildi' | 'ayrildi'
  son?: string
}

/** C1: dış kanal satırı (ortak/oda/<odaId>/gelen-<oturum>.jsonl ve giden.jsonl). */
export type OdaDisSatir = {
  ts: string
  kim: string
  tur: 'katil' | 'ayril' | 'sohbet' | 'rapor' | 'oneri'
  metin: string
  gerekce?: string
  gorevId?: number
  rol?: string
  dosyalar?: string[]
  /** giden.jsonl: hedef oturum adı ya da '*' (herkes). */
  hedef?: string
}

export type Oda = {
  id: string
  baslik: string
  acilis: string
  maksParalel: number
  turlar: OdaTur[]
  gorevler: OdaGorev[]
  oneriler: OdaOneri[]
  /** C1: kalıcı dış oturumlar. */
  oturumlar?: OdaOturum[]
}

export type AjanDurum = { agentId: string; status: string; gorevId: number }

/** Bir işçinin canlı akışından tek parça: araç çağrısı ya da model metni (v0.3). */
export type OdaHareket = {
  ts: string
  gorevId: number
  agentId: string
  tur: 'arac' | 'metin'
  ozet: string
}

/** v0.5: panonun bölümleri (A3, katlanır). */
export type OdaBolum = 'gorevler' | 'oturumlar' | 'oneriler' | 'sohbet' | 'akis' | 'olaylar'

/** v0.5: kaydırma penceresi olan listeler (A2). */
export type OdaListe = 'sohbet' | 'akis' | 'olaylar'

/** v0.5: panonun görünüm durumu; veri değil, yalnız ekran. */
export type OdaPano = {
  /** Açık bölümler. */
  acik: OdaBolum[]
  /** Pencere başlangıcı; null = en son (yeni satır gelince sonda kalır). */
  ofset: Record<OdaListe, number | null>
  /** Tam metni açılmış satırların anahtarı (ts + kim). */
  genis: string[]
}

declare module 'claude-code' {
  interface PluginState {
    'jarvis-oda': { oda: Oda | null; ajanlar: AjanDurum[]; hareket: OdaHareket[]; pano: OdaPano }
  }
}
