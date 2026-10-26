# Akış grafı: bu oturum + dünkü Portal Parkur düğümleri (AS-OF 2026-10-26 17:42; kaynak `ortak/akis-graf.json`, meta {"sema": "akis-graf v1 (Karar 122)", "uretici": "durum graf", "tarih": "2026-10-26", "alan": null, "dugum_sayisi": 48, "kenar_sayisi": 57, "not": "türetilmiş görünüm; kaynak ortak/durum-olay.jsonl; gövde deterministik"})

**Okuma anahtarı:** `seans:*` = oturum düğümü (ac_ts/kapat_ts, hedef, dokunulan iş id'leri); `is:N` = iş düğümü (durum, kanıt, girdi). Kenar türü kenar satırında.

Bu chat = `seans:2026-10-26-jarvis-2`. Dünkü oyun seansı = `seans:2026-10-26-jarvis` (gece kapandı; takvimde aynı gün).

## `seans:2026-10-26-jarvis-2`

| alan | değer |
|---|---|
| id | seans:2026-10-26-jarvis-2 |
| tur | seans |
| alan | jarvis |
| etiket | 2026-10-26-jarvis-2 |
| ac_ts | 2026-10-26T14:40:39Z |
| kapat_ts | None |
| hedef | Portal Parkur proje olarak kapatılır (Salih 2026-10-26); kayıt arşiv-pointer, kuyruk sonraki işe döner |
| hedef_tutuldu | None |
| kayit | None |
| ortuk | False |
| dokunulan | [44] |

**Kenarlar:**

- `seans:2026-10-26-jarvis` → `seans:2026-10-26-jarvis-2` (sonra)
- `seans:2026-10-26-jarvis-2` → `is:44` (bitirdi)

## `seans:2026-10-26-jarvis`

| alan | değer |
|---|---|
| id | seans:2026-10-26-jarvis |
| tur | seans |
| alan | jarvis |
| etiket | 2026-10-26-jarvis |
| ac_ts | 2026-10-25T23:11:01Z |
| kapat_ts | 2026-10-26T08:26:32Z |
| hedef | Portal x Mirror's Edge tarzı birinci şahıs parkur+portal oyununun Godot ile açık kaynak referanslardan inşası; WhatsApp videosuyla görsel/mekanik eşleşmeye kadar iterasyon |
| hedef_tutuldu | True |
| kayit | jarvis/raporlar/seans/seans-teslim-2026-10-26-portal-parkur-oyunu.json |
| ortuk | False |
| dokunulan | [42, 43, 44] |

**Kenarlar:**

- `seans:2026-10-25-jarvis` → `seans:2026-10-26-jarvis` (sonra)
- `seans:2026-10-26-jarvis` → `seans:2026-10-26-jarvis-2` (sonra)
- `seans:2026-10-26-jarvis` → `is:42` (acti)
- `seans:2026-10-26-jarvis` → `is:44` (acti)
- `seans:2026-10-26-jarvis` → `is:43` (bitirdi)

## `is:42`

| alan | değer |
|---|---|
| id | is:42 |
| tur | is |
| alan | jarvis |
| durum | tamam |
| etiket | Portal Parkur v1: Godot 4.7 birinci şahıs parkur+portal oyunu (projects/portal-parkur), 9/9 otomatik mekanik testi geçer |
| sonraki_eylem | Salih oynar, videoyla fark listesi çıkarır; sonraki iterasyon o listeyle |
| acilis_ts | 2026-10-25T23:58:36Z |
| al_ts | 2026-10-25T23:59:55Z |
| bitir_ts | 2026-10-25T23:59:55Z |
| oturumlar | ["2026-10-26-jarvis"] |
| sirada | False |

**Kenarlar:**

- `seans:2026-10-26-jarvis` → `is:42` (acti)
- `is:42` → `is:43` (girdi)

## `is:43`

| alan | değer |
|---|---|
| id | is:43 |
| tur | is |
| alan | jarvis |
| durum | tamam |
| etiket | Salih oynayıp videoyla fark listesi verir |
| sonraki_eylem | sonraki iterasyon fark listesiyle (ses, animasyon, ek bölüm) |
| acilis_ts | 2026-10-25T23:59:55Z |
| al_ts | 2026-10-26T08:25:39Z |
| bitir_ts | 2026-10-26T08:25:39Z |
| oturumlar | ["2026-10-26-jarvis"] |
| sirada | False |

**Kenarlar:**

- `seans:2026-10-26-jarvis` → `is:43` (bitirdi)
- `is:42` → `is:43` (girdi)
- `is:43` → `is:44` (girdi)

## `is:44`

| alan | değer |
|---|---|
| id | is:44 |
| tur | is |
| alan | jarvis |
| durum | tamam |
| etiket | oyun tanımı karışık (ME/Portal → DL/CS/MW → Minecraft bhop kursu katmanları üst üste) |
| sonraki_eylem | sonraki seans: Salih temiz oyun tanımını verir, Jarvis katmanları o tanıma göre ayıklar (projects/portal-parkur, F4 model/seviye anahtarları) |
| acilis_ts | 2026-10-26T08:25:39Z |
| al_ts | 2026-10-26T14:41:11Z |
| bitir_ts | 2026-10-26T14:41:11Z |
| oturumlar | ["2026-10-26-jarvis", "2026-10-26-jarvis-2"] |
| sirada | False |

**Kenarlar:**

- `seans:2026-10-26-jarvis` → `is:44` (acti)
- `seans:2026-10-26-jarvis-2` → `is:44` (bitirdi)
- `is:43` → `is:44` (girdi)

## Portal Parkur yolu (alt-graf)

```
seans:2026-10-25-jarvis --sonra--> seans:2026-10-26-jarvis --sonra--> seans:2026-10-26-jarvis-2 (BU CHAT)
                                    dokundu: is:42 -> is:43 -> is:44           bitirdi: is:44 (KAPANDI)
```
