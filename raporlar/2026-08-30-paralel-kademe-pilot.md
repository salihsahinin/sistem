# Paralel-kapı pilotu — icra borçlarının kademeli paralel koşumu (2026-08-30)

**AS-OF 2026-08-30 09:21→10:2x · paralel icra oturumu (Fable, ana-sıra) · Salih emri (aynen): "borçları pipeline olarak icra ederken sırayla mı paralel mi yürütebileceğini oluşturduğumuz şema ile kontrol et. aynı anda çok fazla paralel pipeline koşulabilecek olsa dahi doğal bir sayı sınırı olacak ama bu sınırı biz bilmiyoruz o yüzden kademeli arttırarak dene" · şema = İB-63 PROTOTİP-1 manifest + PK-1..12 (`raporlar/2026-08-29-ib63-paralel-pipeline-atlas.md`) · kapı = `tools/paralel-kapi.py` (v0-deneysel, bugün yazıldı; PK-11'in ilk icrası — masa kalemi ③'ün imzası Salih'te, bu koşum onu KAPATMAZ) · manifestler `veri/manifest/*.json` · ham kütük scratchpad `kademe-log.jsonl` (bu tabloya aktarıldı). Rakamlar deneysel (m.29); token = Agent/Workflow aracının bildirdiği alt-ajan toplamı (girdi+çıktı).**

*Ne bu:* A kovasındaki (karar gerektirmeyen) 6 icra borcu birim-manifest'e döküldü; kapı her çifte hüküm verdi; koşum N=1 → N=2 → N=3 kademeleriyle yapıldı; her kademede çakışma (aynı dosyaya iki yazar) sıfır mı, doğrulama geçti mi, süre/token ne, ölçüldü. **Paralel oturum s22 (damıtma + kapanış) aynı anda canlıydı** — kapı onu "sahada birim" olarak matrise aldı (PK-12).

## 1. Kapı matrisi (son hâl; 8 birim, 28 çift)
| Hüküm | Çift | Neden (özet) |
|---|---|---|
| PARALEL-SERBEST 17 | argparse×İB-55 · argparse×wiki · İB-55×wiki · A2×İB-39 · A2×wiki · … | Bernstein 3/3 ∅; s22 ile çakışmayan birimler kanonu `git@946791e:` **snapshot** okudu (PK-8 sürüm-damgalı okuma) |
| SIRALI 9 | İB-55→A2 (A2, İB-55 raporunu okur) · argparse→İB-39 · argparse→erisim-fts (ikisi de `tools/SCRIPTLER.md`+`AXI-STANDARDI.md` yazar) · 6 birim→kapanış-loop | `sira` kenarı (PK-1) |
| BEKLE 2 | erisim-fts×s22 (`veri/baglam.sqlite` okur, s22 kapanışı yazar) · kapanış-loop×s22 (`veri/*`, `graf/*`, hareket günlüğü — yazar∩yazar) | PK-12 + PK-5 silver tek-yazar |
| RED 0 | (ilk koşumda 2 RED vardı: İB-39'un `AXI-STANDARDI.md`/`veri/README.md` okuması ↔ argparse/s22 yazımı → snapshot okuma + sira kenarıyla 0'a indi) | |

Kapı çıkışı 0 · dalga planı (kademe ∞): [argparse, İB-55, wiki] → [A2, İB-39] · bekleyen [erisim-fts, kapanış-loop].

## 2. Kademe sonuçları
| Kademe | N | Birim | Model | Süre (s) | Token | Araç çağrısı | Doğrulama | Çakışma | Commit |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | İB-58/2 anahtar-denetim argparse | sonnet | 445 | 116.823 | 33 | unittest 10/10 · eski/yeni insan-çıktı diff BOŞ · çıkış 0/2 | 0 | 5c8c3f9 |
| 2 | 2 | İB-55 A3 REV-2 | sonnet | 131 | 69.586 | 14 | grep REV-2 3 · uzun-loop 3 · aktif "Routine 3 OK" 0 | 0 | a5f494e |
| 2 | 2 | İB-04 wiki `ajan-metodolojisi` | sonnet | 317 | 102.908 | 17 | 5/5 link var · kırık link repo-geneli 3 (önceden) · **AS-OF damgası eksikti → sonradan eklendi** 644109d | 0 | 03dd495 |
| 3 | 3→2 | K-010 A2 tatbikat kaydı | opus | 574 | 117.700 | 60 | test_fren_hook 3/3 · hook replay EXIT 2 · pointer'lar git'te var | 0 | 15dcaf2 |
| 3 | 3→2 | İB-39 atlas (Workflow, 12 iç ajan) | sonnet+opus | 1.137 | 783.631 | 173 | 12/12 ajan, hata 0; fren sayacı 12/36; sentez done-yüklemi 5/5 | 0 | 4cdb47c |
| 3 | — | İB-58/3 erisim-fts AXI | — | — | — | — | **KOŞULMADI: PK-12 BEKLE** (s22 kapanmadı; `veri/baglam.sqlite` okuması s22'nin katman-hatti yazımıyla çakışır) | — | — |

Toplam: 5 birim tamam, 1 bekliyor · duvar saati 09:36→10:15 (39 dk) · alt-ajan token ≈ 1,19 M (bunun %66'sı İB-39 atlası) · çakışma **0/5** · doğrulama-sonrası düzeltme 1 (wiki AS-OF).

## 3. Okuma — ne öğrenildi (çıplak veri, hüküm Salih'in)
1. **Doğal sınır bu pilotta bulunmadı:** N=3 kademesi fiilen 2 ajan + 12 iç ajan (Workflow kendi tavanı min(16, CPU−2)) = ~14 eşzamanlı; makine/araç tarafında darboğaz gözlenmedi. Sınır ARAÇ değil AYAK-İZİ oldu: 3. birim (erisim-fts) sayı yüzünden değil, diğer oturumla `veri/baglam.sqlite` paylaştığı için koşamadı. **Kademe artışının sınırı = paralel-serbest çift sayısı; dalga planı bunu deterministik veriyor.**
2. **Snapshot okuma (`git@sha:yol`) 2 RED + 1 BEKLE'yi sıfıra indirdi** — kanonun (defter/pano/kapsül) başka oturumca düzenlendiği durumda paralel okuma için ucuz ve doğru; PK-8'in "sürüm-damgalı okuma" kuralının pratik biçimi. Manifest şemasına "snapshot okur" alanı adayı (masa ②).
3. **İB-39'un kendi bulgusu pilotun kararını doğruladı:** `hareket-tablo.py:145-156` kilitsiz TOCTOU (bronz 350 tekrar hareket_id, bağımsız sayımla teyit) + `baglam-tablo.py:925` sabit tmp adı → iki oturumun kapanış loop'u AYNI ANDA koşsaydı silver/bronz bozulurdu. Kapı bunu manifestten (PK-5) buldu; kod kanıtı atlas sentezinde.
4. **Kalite:** 5/5 birim doğrulama geçti; 1 eksik (AS-OF damgası) kapı değil koşum-sonrası kontrolle yakalandı → manifest `dogrulama_kapisi` alanına "AS-OF grep" standart satırı adayı. Opus'lu A2 birimi 60 araç çağrısı (Sonnet birimlerinin 2-4 katı) — kanıt derleme işi doğası gereği çok okuma; maliyet-tahmini Salih kuralı gereği yalnız alt-model için: sonnet birim ≈ 70-117k token, opus derleme ≈ 118k, atlas 12 ajan ≈ 784k.
5. **Manifest yaşam yeri (İB-63 cevaplanmamış soru 1):** bu pilotta birim başına JSON (`veri/manifest/<birim>.json`) seçildi — kapı `glob` ile okur, `durum` alanı `planli → tamam-<tarih>` ilerler, silinmez (m.8). Alternatif JSONL masada.
6. **Kapı script'inin sınırı:** çakışma denetimi dosya granülünde (glob), `#bolum` eki yalnız ikisi de bölüm-granüllüyse ayrık sayar; `kayit` (silver satırı) granülü yok (İB-63 soru 2 açık). Kira/kilit mekanizması hâlâ 0 — kapı BEYAN'a bakıyor, zorlama (`zorlama_modu`) yalnız etiket (PK-4 uyarısı üretir, engellemez).

## 4. Açık kalanlar / devir
- **erisim-fts AXI birimi** (İB-58/3): s22 kapanınca kademe-3b olarak koşulur (manifest hazır; kapı BEKLE'den çıkınca).
- **Bu oturumun kapanış loop'u** (hareket kütüğü + katman-hatti + teslim): PK-12 BEKLE — s22'nin kapanış commit'i (veri/ 28 kirli dosya) atılmadan koşulmaz; Salih hükmü: s22'yi kapat → sonra bu oturum "seans bitimi".
- Masaya: manifest şeması + PK imzası (İB-63 ①) · `paralel-kapi.py` ③ · snapshot-okur alanı · AS-OF doğrulama satırı · İB-39 masa taslağı 8 kalem (`raporlar/2026-08-29-ib39-idempotens-atlas.md`).
- K-010 sayaçları: A1 0/5 (bu koşumlar pilot sayılır mı — Salih; pilot seçimi masa kalemi) · A2 kanıt 3/3 KAYITLI (`raporlar/2026-08-30-k010-a2-tatbikat-kaydi.md`, imza boş) · A3 0/3 · ÖB-1/2 Salih'te.

*Yeniden üretim:* `python3 tools/paralel-kapi.py [--kademe N] [--json]` (manifestler repoda); kademe kütüğü satırları bu tabloda; ajan çıktıları hareket kütüğünde (kapanışta iner).
