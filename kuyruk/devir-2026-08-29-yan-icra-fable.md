# Devir — 2026-08-29 yan icra oturumu (Fable; Salih: "paralel icra oturumu — kararımın gerekmediği ölçüm ve icra borçları")

*Karar 71 üç-katman düzeni: yan-oturum karar almaz, ledger'ın son-gün bloğuna yazmaz, devir dosyasıyla taşır. Ana-sıra (seans-20) 13:51'de kapandı ve push'ladı; bu oturumun ilk 10 commit'i o push'a girdi (m.9 sayıldı). Sonraki commit'ler push bekliyor. TASLAK — kapanışta güncellenir.*

## Ne yapıldı (commit sırası; hepsi `git add <yol>` pathspec'le, H4)
| # | Kalem | Commit | Kanıt |
|---|---|---|---|
| 1 | 12 karar-borcu pointer'ı onarıldı (10 kırık + 2 sessiz kayma) + `tools/pointer-kayma.py` + damitma Gotcha | 3f39b2e | karar-borcu-tablo kırık 0/320 |
| 2 | İB-52 KAPANDI: `kayit.cekim_tarihi/kaynak_tarihi` + `tools/bayat-cekim.py` + seans-kapanis 6f | 0612826 | hat exit 0; ilk N=3: kuyruk 0 |
| 3 | KB-61 (Karar 74 M-1 b) İCRA: silver `bag` (wasRevisionOf, R1/R2/R3, bitemporal) + graf kenar tipi | e9c0e8a | 20 bağ; 4 test PASS |
| 4 | İB-54 (1) KAPANDI: kök-neden raporu (V-1 08-01-4 · V-2 08-01-6; 5+1 kök neden; taban 401 ajan) | 65ee257 | `raporlar/2026-08-29-ib54-delinme-kok-neden.md` |
| 5 | İB-43 ≥100: 25→100 soru (doğrulama-terimi kapılı); eval n=100 | 27481f5 | fts5 0,617 · +gen 0,593 · +guncel 0,605 |
| 6 | İB-53 (1) KAPANDI: kapsama haritası + (2) seçenekler a-d Salih'e | 52abffb | `raporlar/2026-08-29-ib53-kapsama-haritasi.md` |
| 7 | Kolon zinciri: `.venv` duckdb; İB-31 KAPANDI; İB-33 KAPANDI (k=3, soğuk şerhli); İB-30 kısmen (venv+sıra; bayrak kararı Salih) | b08c5dd | `raporlar/2026-08-29-ib33-kolon-olcum-k3.md` §4 |
| 8 | İB-34 KAPANDI: `wiki/kolon-katmani.md` + 5 karşı-link | a6eaa5f | wiki index |
| 9 | İB-51 (1)+(2): `tools/kural-envanter.py`; 1.017 birim; seans tabanı 71 (19 değil) | ab5f5b6 | `raporlar/2026-08-29-ib51-kural-envanteri.md` |
| P1 | İB-54 (2) KAPANDI: `pretool-ajan-fren.sh` (UYARI 36 / DURDUR 72, rejim etiketli) + `cc/workflow/fren-sablonu.js` + 2 hat testi | f106319 | `tools/testler/test_fren_hook.py` 3/3 |
| P2 | İB-47 KAPANDI: `tools/erisim-vektor.py`; e5+bge gömme (53.983, MPS, ~1 sa/model); 100 soru × 8 yöntem: RRF nDCG@10 +0,057…+0,070 ANLAMLI, vektör tek başına tabanın altında; determinizm bit-eşit (e5 iki bağımsız süreç aynı sha); int8 kayıpsız 3× hızlı | aa96260 | `raporlar/2026-08-29-ib47-vektor-olcum-kolu.md` §6 masa soruları |
| P3 | İB-38 KAPANDI: `tools/tarama-plan-duckdb.py` (10 sorgu, ihlal 0; zone-map footer simülasyonu 1/14 ↔ 14/14) + hat adımı `tarama-duckdb` · İB-32 konusuz kapandı (parquet gitignore) | 1166c80 · 3af770e | `v_tarama_plan_duckdb.csv` |
| P4 | İB-49 KAPANDI: `tools/d2-eval.py` + 18 Sonnet koşumu — üretim 5/5 P=R=1,0; okuma 24/25 ↔ LLM-SQL 25/25; hakem: insan→script-D2, LLM→kenar-satırı (5,5× küçük) = Karar 67 P5 teyidi | 4d4484f | `raporlar/2026-08-29-ib49-d2-mini-eval.md` |
| P5 | İB-10 KAPANDI: `tools/denetci-kalibrasyon.py` — yakalama 12/12, yanlış alarm 0/9 (tur-1'de denetçi yazar hatasını yakaladı) · md.27 etiket tablosu ADAY (Z 5 · Z/k 12 · D 28) · A7 eşik envanteri (türetilmiş 7 / sezgisel 10) → KB-26 m.37 v2 yürürlüğü Salih'e | 6a975f5 | `raporlar/2026-08-29-ib10-denetci-kalibrasyon.md` |
| P8 | İB-43 KAPANDI: `tools/erisim-kalibrasyon.py` (LLM yok) — GEN_AGIRLIK 2→0,5 (ölçüm kuralıyla), `fts5+auto` soruya-bağlı yüzey (TÜMÜ 0,654/0,468; MRR 0,492 en iyi), çekimserlik eşikleri (e5 0,522 → 0,837), eval-sürüklenmesi gözlemi (indeks kimliği) | 593a932 | `raporlar/2026-08-29-ib43-kalibrasyon.md` |
| P6 | İB-51 KAPANDI: atlas (2 aile, tez/antitez/V26/hakem) — `.claude/rules` `paths:` canlı+deterministik ama yalnız Read-aracı tetikli; skill'lerde de `paths`; hook additionalContext aralıklı → (d) (a)'yı tamamlar, hibrit öneri; 4 açık soru | e67741b | `raporlar/2026-08-29-ib51-atlas-kural-yukleme.md` |

## Ana-sıraya taşınan kararlar / satırlar (Katman-1 ya da defter son-gün bloğu — yan oturum yazmadı)
- **Defter satırları** (Karar 74 icra kayıtları): KB-61 icra · İB-52/İB-31/İB-33/İB-34 kapanış · İB-54 (1)(2) · İB-43 ≥100 · İB-53 (1) · İB-51 (1)(2) — ledger `veri/karar-borcu.jsonl` GÜNCEL (kapanis_kaniti alanları); defter bloğu ana-sıra yazar.
- **Salih kararları bekleyen:** İB-30 bayrak (rapor ib33 §4, A önerilen) · İB-53 (2) seçenek a-d · İB-54 (3) rejim-etiketi satırı (KILAVUZ/tüzük; taslak ib54 §5) · İB-43 75 yeni soru teyidi · kural-sayaci `--skill` varsayılanı (ib51 §5) · KB-61 kalan tipler (CiTO/OpenLineage) masa kalemi · **hibrit/vektör hükmü (Karar 60 sırası): rapor ib47 §6 — RRF ikinci kol mu · model (bge/e5) · int8 varsayılan · bilgi-guncelleme'yi süpersede yüzeyinden çözmek**.
- **Ortam yan-etkileri (görünür, geri alınabilir):** `.venv` (duckdb, sentence-transformers, torch, sqlite-vec ~2,5 GB) · HF cache `~/.cache/huggingface` (e5 + bge-m3 ~4,4 GB) · `~/.duckdb/extensions` (sqlite eklentisi) · `veri/erisim-vektor.sqlite` 604 MB + 2×221 MB `.npy` (gitignore). Silmek = geri alma.
- **Ders/hasat adayları (kutu):** damıtma sonrası sessiz satır-kayması sınıfı (pointer-kayma) · çekimserlik zayıf-kontrolünün kendi-kendini-kirletmesi (üretici korpusa girince) · hook stdin↔heredoc çakışması · bayat sabit-liste testi (adım listesi türetilmeli) · kural-sayaci varsayılanın gerçek yükü 3,7× düşük göstermesi.
- **Salih el işi (opsiyonel):** `sudo purge` + tek kolon-olcum koşumu (gerçek soğuk ayak) · Obsidian'da `raporlar/2026-08-29-ib53-kapsama-haritasi.md` §6 mermaid/matematik canlı doğrulama.

## Salih masasına eklenen kararlar (P4-P6)
- KB-26 m.37 v2 yürürlüğü (kalibrasyon şartı sağlandı: ib10 §1) · md.27 etiketlerin tüzüğe yazımı (ib10 §2 ADAY tablo) · A7 temellendirme kuyruğu (ib10 §3) · kural yükleme mekanizması hibrit önerisi + 4 açık soru (ib51-atlas §"Cevaplanmamış") · Karar 67 P5 ölçülü teyit (ib49; kanon değişmez).
- Fren hook canlı: bu oturum 48 Agent çağrısı → 36'da UYARI olayı (bronz `fren-olay.jsonl`); DURDUR 72'ye ulaşılmadı.

## Açık işler — OTURUM BAĞLAM DOLDU (Salih 08-29 ~19:25: "dur, yeni seans açılacak"); kapanış ritüeli KOŞULMADI
- **P9 İB-42 kalanı YARIM (commit'li WIP):** (1) T-A kanıt-bulucu 10 koşum TAMAM — 9 YOK, 1 aday hakemce "çelişki değil" (`veri/silver-saglik-kanit.jsonl`, `cc/kanit-bulucu/`) · (2) as-of eval TAMAM (`tools/asof-eval.py`: yüzey emekli-kalıntıyı top-5'ten siliyor 4→0/6→0, güncel değer 6→8/10, bilgi-guncelleme 0,45→0,70; **auto = ham 0,45 → GUNCEL_RX'e "yerine/ne oldu/eski adı…" eklendi, ölçüm YENİLENMEDİ**) · (3) sabit kalibrasyonu TAMAM (`tools/silver-saglik-kalibrasyon.py`: 42 koşum; YETİM medyan 234 ↑247; uyarı eşiği önerisi 351 = medyan×1,5, Salih) · (4) `katman()` tek-tanım TAMAM (anahtar-denetim → baglam-tablo.katman_bul; test `tools/testler/test_katman_tek_tanim.py`; etki: kuyruk/gelen-*, kök *-KAPSULU-*, Clippings/ sınıfı ılık/soğuk değişti → anahtar-denetim ılık uyarısı 72, sıcak ihlal 0).
- **SONRAKİ İLK İŞ (yeni seans):** `python3 tools/asof-eval.py` + `python3 tools/erisim-kalibrasyon.py` yeniden (GUNCEL_RX genişletmesinin auto etkisi) → `raporlar/2026-08-29-ib42-kalan.md` yaz (4 alt kalem + sayılar) → ledger İB-42 kapandı → SCRIPTLER/README satırları (asof-eval, silver-saglik-kalibrasyon) → commit → sonra kalan liste: İB-12 doğrulama · İB-39 envanter · İB-04 wiki · İB-05 · İB-06 · İB-07/09 (LLM) · İB-08 · İB-13.
- P7 kapanış (`seans-kapanis`: teslim raporu + hasat + kapsül şeridi) yeni seansta; push Salih beyanı (origin'in ≥11 commit önünde).
