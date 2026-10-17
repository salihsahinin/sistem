---
name: damitma
description: Kanonun damıtma/ingest turunu koşar (S-E); kuyruk/gelen dosyalarını ingest v2 triyajından geçirir, boyut-FLAG'li sıcak dosyaları bütçeye indirir (arşiv-pointer). Tetik; "damıt", "damıtma turu", "ingest et", boyut-tetiği FLAG'i, kümülatif önem ≥150 aşımı. kullanılmaz; seans kapanışının rutin ingest'inde (seans-kapanis kendi koşar), tek küçük not için (eşikte-toplu ilkesi).
---

# Damıtma turu (S-E, v1 — 2026-08-14; ingest şeması v2'nin koşum skill'i)

Kural kaynağı: `core/ingest-semasi.md` (zarf+tip+triyaj+**dlq**+bütçeler) + v1 kapıları (`kuyruk/oneri-ingest-sema-v1.md`: G1/G2/G3). Silme `YOK` (m.8); pointer her kısaltmada korunur (m.20/m.21).

## Adımlar
1. **Tetik doğrula:** eşik gerçekten aşıldı mı (G3 ≥40 madde ∨ Σönem ≥150 ∨ boyut-FLAG ∨ Salih beyanı)? Aşılmadıysa **dur** — her damıtma bir maliyettir (**lsm** write-amplification).
2. **Bronz toplama:** `kuyruk/gelen-*.md` içinde "**ingest edildi**" damgası taşımayanları listele.
3. **Kayıt-başına triyaj (şema §3; hüküm `lean/Kanon/Ingest.lean`):** zarf kontrol (eksikse tamamla, değer bilinmiyorsa `-`) → 4 soru: eşdeğer→**NOOP** · tamamlar→**UPDATE** (hedef kaydı güçlendir) · çelişir→**GEÇERSİZ-KIL** (eskiye `gecerli-bitis` damgası; Katman-1 sınıfıysa m.16 çelişki raporu Salih'e) · yeni→**ADD** (tipin varsayılan hedefine). Tip/hedef alamayan → `kuyruk/SINIFLANDIRILAMADI.md` (sessiz düşürme yasak). **GEÇERSİZ-KIL bir anahtar değerini (kavram/tetik/ad/yüzey) değiştiriyorsa** → `core/baglam-anahtar-kaydi.md` §3 emeklilik protokolü (emekli satırı + sıcak-katman yayılımı) ve tur sonunda `python3 tools/anahtar-denetim.py` (sıcak ihlal 0 olmadan tur kapanmaz).
4. **Boyut-FLAG damıtması (hedef = sorgu-uyumu, oran değil — Salih imzası 08-17 KB-17c):** önce 'damıtılmış dosya hangi sorulara cevap vermeli' listesi yazılır, o cevapları veren satırlar **kalır**; oran (~%50) sonuçtur, hedef değil. Kapsül üstüne-yazma turlarında **erozyon sayacı**: kaybolan niteleyici/pointer sayılır, teslim raporuna düşer. **korunacak**: kararlar + çözülmemiş sorunlar + doğrulama adımları + pointer'lar; **düşecek**: araç çıktıları, tarihçe-anlatısı (arşive pointer'la iner, silinmez). Sıra: önce recall, sonra precision.
5. **Kapılar:** kural-adayı kanonlaşması **yalnız** Salih imzasıyla (G2) — damıtma aday taşır, imzalamaz.
6. **Kapanış:** sayaçlar (`giren/NOOP/UPDATE/geçersiz/ADD/DLQ`) teslim raporuna; işlenen bronz dosyalara "**ingest edildi** · <tarih>" damgası; SINIFLANDIRILAMADI'daki eski kayıtlar yeniden denenir (redrive).
7. **Silver-sağlık kapısı (Karar 58, KB-39/40/41 (a); İB-42 08-22):** damıtma turu kapanmadan `python3 tools/silver-saglik.py --kapi` — T-Ç çelişki hatası (çıkış 6) varsa tur **kapanmaz**; arşive indirilen bloklar için `v_silver_kuyruk` SÜPERSEDE/YETİM adayları damıtmanın **girdisidir** (aday = öneri, silme kararı Salih'in; pointer koparma kuralı aynen).
8. **Deneyim çifti → kural adayı (KB-44 (a) Karar 60, ExpeL b-kanalı; İB-44 08-22):** `python3 tools/deneyim-tablo.py` koş → `v_deneyim_cift` (aynı wf/aile+rol altında `PASS` ∧ `FAIL` yörüngeleri). Her çift için **tek** satır kural **adayı** yazılır (`fikir-kutusu.md` ya da `kuyruk/gelen-*`; zarf `tip: kural-adayi`, kaynak = iki kosum_id, model-kuşağı damgası zorunlu — eski-kuşak yörüngesinden aday yazılmaz, yalnız not düşülür). Aday **kanonlaşmaz**: kanonlaşma yalnız **dış** geri-besleme (test/koşum sonucu/Salih imzası, G2). Çift yoksa adım "0 çift" satırıyla geçer (uydurma yok, m.39). Sayaç: aday sayısı / kabul sayısı teslim raporuna (ölçüm).
9. **Koşullu yansıma (KB-45 (a) Karar 60; İB-45 08-22):** dönem özeti ("ne öğrendik") **yalnız** bu turda dış geri-besleme varsa yazılır — (i) koşum hükmü (PASS/FAIL, `amb_olgu_kosum_sonuc`), (ii) test sonucu (katman-hatti / canary), (iii) Salih imzası/beyanı. Üçü de yoksa yansıma **yazılmaz** (kör öz-düzeltme yasak; Karar 48 kendini-analiz kısıtı). Yazılırsa ≤5 satır, her satır kaynaklı (kosum_id / test adı / Karar N) → teslim raporu "Yansıma" bloğu; wiki-delta'ya girenler için `python3 tools/wiki-baglanti.py --uygula` (not evrimi: karşı-link geri-güncellemesi; güncellenen sayfa / yetim→pointer sayacı teslim raporuna).

## Gotchas
- **Kapsül-şişirme:** damıtma çıktısını kapsüle tarihçe olarak yazma — kapsül snapshot'tır, "şu an + sıradaki"den fazlasını taşımaz.
- **Pointer koparma:** arşive inen her bloğun yerinde tek satır pointer kalır; pointer'sız arşiv = kayıp.
- **Sessiz satır-kayması (vaka 08-29, Karar 74 M-3 turu):** damıtılan dosyaya giden `dosya:satır` pointer'ları kırılmadan başka içeriğe düşebilir (kutu:29 V13→V38, defter:156 Karar 48→65); `karar-borcu-tablo.py` bunu **görmez**. Adım 4'ten sonra, commit'ten **önce**: `python3 tools/pointer-kayma.py --ref HEAD` → KAYMIŞ/KIRIK pointer'lar önerilen arşiv adresine çevrilir (m.8 arşiv-pointer), sonra `karar-borcu-tablo.py` kırık 0.
- **Çift-gelen tuzağı:** paralel sekmelerden aynı bilgi iki bronz dosyada gelebilir — `kaynak` zarf alanı dedup anahtarıdır, triyajda karşılaştır.
- Skill kendi başına commit atmaz; commit seans akışının işidir.

## Şema-dalı (v1.1, 2026-08-15 Hat-4 evrimi; kural: `core/sema-sikistirma.md` §3)
FLAG'li dosyada triyajdan **önce** kayıt-sınıflarını ayır → sınıf-başına U skoru → ŞEMALA-sınıfını olgu-satırlarına indir (atomik olgu + kaynak-pointer + niteleyici alanı + bi-temporal damga) + **çıkarımı doğrula** (kaynak satıra geri-eşle; `DAYANAKSIZ` → kaynakla ∨ düş) · HAM-sınıfı (niteleyici-yoğun hüküm, akıl-yürütme izi) arşive pointer'la, ŞEMAya girmez · ölçüm satırı çift muhasebe (sorgu-anı ↔ depo token) + **dlq** oranı + tur ≤3 (erozyon freni). Hedef "oran %50" değil **sorgu-uyumu** (kapsül/pano hangi soruları cevaplıyor).
