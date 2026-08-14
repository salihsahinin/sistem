---
name: wiki-sayfa-yaz
description: Hasat wiki-delta'sından ya da wiki kuyruğundaki adaydan, yazım standardına uygun wiki sayfası üretir (W-1); 6-blok şablon + kanonik damıtılmış örnek + index kaydı + [[link]] turu. Tetik; "wiki'ye yaz", "sayfa aç", "wiki sayfası üret", vardiya hasadında wiki-delta işlenirken. KULLANILMAZ; sozluk.md eklemelerinde (sözlük DONDU — yalnız Salih talimatı), toplu üretimde (tempo kuralı; oturum başına 1-2 sayfa), ham senaryo aktarımında (ham log sayfaya girmez, pointer'la durur).
---

# Wiki sayfa yazımı (W-1, v1 — 2026-08-14, Salih onayıyla üretildi)

Kural kaynağı: `wiki/README.md` yazım standardı (deneysel m.29) + V24 isim disiplini + m.8 süpersede zinciri. Wiki = şirketin beyni (#5); sayfa = kavramın damıtılmış, yeniden-üretebilir hali.

## Adımlar
1. **Aday seç:** `wiki/README.md` Kuyruk'tan ya da verilen wiki-delta'dan; **oturum başına 1-2 sayfa** (tempo kuralı — toplu üretim yasak).
2. **6-blok şablonla yaz:**
   - *Üst blok:* 1-2 cümle tanım · durum (GÜNCEL/BAYAT) · son-teyit tarihi · kaynak pointer'ları · kaba güven (düşük/orta/yüksek — kaç kaynak + tazelik + çelişen var mı; ŞİŞİRME).
   - *Çekirdek:* sade dil + **1 kanonik damıtılmış örnek** — deseni yeniden üretebilen EN KÜÇÜK hal; ham senaryo girmez (rapor/log pointer'ı).
   - *SOP:* "okuyucu pazartesi sabahı ne YAPAR" — adım adım (uygunsa; model parametresi YOK).
   - *Gotchas:* fiilen yapılmış hatalardan tuzak listesi (yaşayan bölüm).
   - *Süpersede zinciri:* çelişen eski iddia SİLİNMEZ — "yerini aldı: [tarih, yeni iddia]" damgası.
   - *[[link]]'ler:* ilgili sayfalara bağla.
3. **Index kaydı:** `wiki/README.md` Index'e tek satır (`[[ad]] — hook (eklendi tarih, kaynak turu)`); aday kuyruktan geldiyse kuyruk satırını düşür.
4. **Bağlantı turu (A-MEM dersi — notlar statik değil):** yeni sayfanın komşuları gözden geçirilir; gerekiyorsa komşu sayfaya karşı-link ya da Gotcha güncellemesi işlenir.
5. **Teslim:** üretim, ingest-şeması zarfıyla teslim raporuna kaydedilir (`tip: kavram`).

## Gotchas
- **İsimsiz index:** sayfa yazılıp index'e işlenmemesi en sık arıza (07-22'de dört sayfa; 08-14'te ingest-semasi vakası) — adım 3 atlanamaz.
- **İsim disiplini (V24):** mevcut sayfanın adı değiştirilmez; ad değişikliği Salih bildirimi ister.
- **Güven enflasyonu:** tek kaynaklı taze bulguya "yüksek" yazma.
- **sozluk.md bu skill'in kapsamı DIŞINDA** — donmuş dosya, yalnız Salih talimatıyla ve ayrı işle.
