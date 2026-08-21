---
name: damitma
description: Kanonun damıtma/ingest turunu koşar (S-E); kuyruk/gelen dosyalarını ingest v2 triyajından geçirir, boyut-FLAG'li sıcak dosyaları bütçeye indirir (arşiv-pointer). Tetik; "damıt", "damıtma turu", "ingest et", boyut-tetiği FLAG'i, kümülatif önem ≥150 aşımı. KULLANILMAZ; seans kapanışının rutin ingest'inde (seans-kapanis kendi koşar), tek küçük not için (eşikte-toplu ilkesi).
---

# Damıtma turu (S-E, v1 — 2026-08-14; ingest şeması v2'nin koşum skill'i)

Kural kaynağı: `core/ingest-semasi.md` (zarf+tip+triyaj+DLQ+bütçeler) + v1 kapıları (`kuyruk/oneri-ingest-sema-v1.md`: G1/G2/G3). Silme YOK (m.8); pointer her kısaltmada korunur (m.20/m.21).

## Adımlar
1. **Tetik doğrula:** eşik gerçekten aşıldı mı (G3 ≥40 madde ∨ Σönem ≥150 ∨ boyut-FLAG ∨ Salih beyanı)? Aşılmadıysa DUR — her damıtma bir maliyettir (LSM write-amplification).
2. **Bronz toplama:** `kuyruk/gelen-*.md` içinde "İNGEST EDİLDİ" damgası taşımayanları listele.
3. **Kayıt-başına triyaj (şema §3):** zarf kontrol (eksikse tamamla, değer bilinmiyorsa `-`) → 4 soru: eşdeğer→**NOOP** · tamamlar→**UPDATE** (hedef kaydı güçlendir) · çelişir→**GEÇERSİZ-KIL** (eskiye `gecerli-bitis` damgası; Katman-1 sınıfıysa m.16 çelişki raporu Salih'e) · yeni→**ADD** (tipin varsayılan hedefine). Tip/hedef alamayan → `kuyruk/SINIFLANDIRILAMADI.md` (sessiz düşürme yasak). **GEÇERSİZ-KIL bir anahtar değerini (kavram/tetik/ad/yüzey) değiştiriyorsa** → `core/baglam-anahtar-kaydi.md` §3 emeklilik protokolü (emekli satırı + sıcak-katman yayılımı) ve tur sonunda `python3 tools/anahtar-denetim.py` (sıcak ihlal 0 olmadan tur kapanmaz).
4. **Boyut-FLAG damıtması (hedef = SORGU-UYUMU, oran değil — Salih imzası 08-17 KB-17c):** önce 'damıtılmış dosya hangi sorulara cevap vermeli' listesi yazılır, o cevapları veren satırlar KALIR; oran (~%50) sonuçtur, hedef değil. Kapsül üstüne-yazma turlarında EROZYON SAYACI: kaybolan niteleyici/pointer sayılır, teslim raporuna düşer. KORUNACAK: kararlar + çözülmemiş sorunlar + doğrulama adımları + pointer'lar; DÜŞECEK: araç çıktıları, tarihçe-anlatısı (arşive pointer'la iner, silinmez). Sıra: önce recall, sonra precision.
5. **Kapılar:** kural-adayı kanonlaşması YALNIZ Salih imzasıyla (G2) — damıtma aday taşır, imzalamaz.
6. **Kapanış:** sayaçlar (`giren/NOOP/UPDATE/geçersiz/ADD/DLQ`) teslim raporuna; işlenen bronz dosyalara "İNGEST EDİLDİ · <tarih>" damgası; SINIFLANDIRILAMADI'daki eski kayıtlar yeniden denenir (redrive).

## Gotchas
- **Kapsül-şişirme:** damıtma çıktısını kapsüle tarihçe olarak yazma — kapsül snapshot'tır, "şu an + sıradaki"den fazlasını taşımaz.
- **Pointer koparma:** arşive inen her bloğun yerinde tek satır pointer kalır; pointer'sız arşiv = kayıp.
- **Çift-gelen tuzağı:** paralel sekmelerden aynı bilgi iki bronz dosyada gelebilir — `kaynak` zarf alanı dedup anahtarıdır, triyajda karşılaştır.
- Skill kendi başına commit atmaz; commit seans akışının işidir.

## ŞEMA-DALI (v1.1, 2026-08-15 Hat-4 evrimi; kural: `core/sema-sikistirma.md` §3)
FLAG'li dosyada triyajdan ÖNCE kayıt-sınıflarını ayır → sınıf-başına U skoru → ŞEMALA-sınıfını olgu-satırlarına indir (atomik olgu + kaynak-pointer + niteleyici alanı + bi-temporal damga) + ÇIKARIMI DOĞRULA (kaynak satıra geri-eşle; DAYANAKSIZ → kaynakla ∨ düş) · HAM-sınıfı (niteleyici-yoğun hüküm, akıl-yürütme izi) arşive pointer'la, ŞEMAya girmez · ölçüm satırı çift muhasebe (sorgu-anı ↔ depo token) + DLQ oranı + tur ≤3 (erozyon freni). Hedef "oran %50" değil SORGU-UYUMU (kapsül/pano hangi soruları cevaplıyor).
