---
name: wiki-sayfa-yaz
description: Wiki-delta'dan ya da kuyruk adayından standarda uygun wiki sayfası üretir (W-1); 6-blok şablon + index + [[link]] turu. Tetik; "wiki'ye yaz", "sayfa aç", "wiki sayfası üret", seans hasadında wiki-delta işlenirken. KULLANILMAZ; sozluk.md eklemelerinde (sözlük DONDU), toplu üretimde (oturum başına 1-2 sayfa), ham senaryo/log aktarımında (pointer'la durur).
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
4. **Bağlantı turu = NOT EVRİMİ (A-MEM dersi — notlar statik değil; KB-45 (a) Karar 60, İB-45 08-22):** (a) deterministik: `python3 tools/wiki-baglanti.py` (kuru rapor: karşı-link adayları + kırık [[link]]) → `--uygula` ile yeni sayfanın bağladığı eski sayfalara karşı-link satırı EKLENİR (silme yok; sozluk.md dokunulmaz); (b) elle: komşu sayfada süpersede/etiket/Gotcha güncellemesi gerekiyorsa işlenir. Sayaç (güncellenen sayfa · yetim→pointer) teslim raporuna — KB-45 ölçümü.
5. **Teslim:** üretim, ingest-şeması zarfıyla teslim raporuna kaydedilir (`tip: kavram`).

## Gotchas
- **İsimsiz index:** sayfa yazılıp index'e işlenmemesi en sık arıza (07-22'de dört sayfa; 08-14'te ingest-semasi vakası) — adım 3 atlanamaz.
- **İsim disiplini (V24):** mevcut sayfanın adı değiştirilmez; ad değişikliği Salih bildirimi ister.
- **Güven enflasyonu:** tek kaynaklı taze bulguya "yüksek" yazma.
- **sozluk.md bu skill'in kapsamı DIŞINDA** — donmuş dosya, yalnız Salih talimatıyla ve ayrı işle.
- Skill commit yapmaz; sayfa + index yazımı dosyaya, commit seans akışının işidir (yan-etki freni).
