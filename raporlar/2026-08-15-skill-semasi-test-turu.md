# Skill-Şeması Test Turu — 2026-08-15 (SH-3; Salih emri: "mevcut skilleri ve adayları şemadan test olarak sok, geçecek hale getir")

*Şema: `core/skill-uretim-semasi.md` v1 · koşum: `skill-kapisi` (script `kapi-denetim.py` = K2-R + K3-F1..F4 + tür-özel; K0/K1/K2-İ/F5 Carvis) · pipeline: `cc/pipeline-2026-08-15-skill-uretim-semasi.md`. Mevcut skiller için K1 = "zaten üretilmiş" (geriye dönük: kutu m.43 sayımı ∨ Salih onayı) — bu tur asıl olarak K2/K3'ü ve şemanın kendisini sınadı.*

## 1. Sonuç tablosu (14 skill — 13 mevcut + skill-kapisi)
| skill | K0 GEREK | K1 DEĞER | K2-R (script) | K2-İ (iddia) | K3 biçim | birincil şekil (FIRST) | fasetler | HÜKÜM | uygulanan onarım |
|---|---|---|---|---|---|---|---|---|---|
| atlas-kosum | ✓ Y3 | Z1 (07-17'de 6×) | ✓ 8 ref | K (kanon-atıfları rapor-kaynaklı) | ✓ | T-O | model+kullanıcı · ana/alt-ajan · yan-etki yok · B3 · aşağıdan | GEÇTİ | — (△ paralellik-uygunluk sorusu gövdede açık değil — evrim notu) |
| celiski-kapisi | ✓ Y2 | Z1 | ✓ | K | ✓ | T-Ü | model+kullanıcı · ana · yok · B2 | GEÇTİ | — |
| damitma | ✓ Y3 | Z1 | **✗→✓** (`kuyruk/SINIFLANDIRILAMADI.md` YOKTU) | K | **✗→✓** evals yoktu | T-Ü | model+kullanıcı · ana · yok · B3 | GEÇTİ | DLQ dosyası açıldı · evals.json (3+5/5) |
| gorev-emri-derleme | ✓ Y2/Y3 | Z1 (21+2 emir) | ✓ | K | **✗→✓** | T-O | model+kullanıcı · ana · yok · B3 | GEÇTİ | evals.json |
| gunaydin-vardiya | ✓ Y2 | ritüel (Salih) | ✓ 13 ref | K | **✗→✓** neg-eval 3→5 | T-R | model(cümle) · ana · yan-etki yok · B2 · yukarıdan | GEÇTİ | +2 negatif eval (staj klasörü, "günaydın staj") · description 849→~700 char |
| karar-hatti | ✓ Y3 | Z1 | ✓ | K | ✓ | T-O | model+kullanıcı · fork · yok · B3 | GEÇTİ | — (△ paralellik sorusu) |
| karar-kaydet | ✓ Y3 | Z1 (S-G tamamlayıcı) | ✓ | K | **✗→✓** flag + evals yoktu | **T-Y** | **kullanıcı-yalnız** · ana · **yan-etki VAR** · B3/B4 | GEÇTİ | `disable-model-invocation: true` eklendi (kutu S-J tasarımı böyleydi, uygulanmamıştı) · evals.json |
| karar-modeli | ✓ Y2 | Z1 (2×) | ✓ | K | ✓ | T-Ü | model+kullanıcı · ana · yok · B2/B3 | GEÇTİ | — |
| lojik-ceviri | ✓ Y2 | Z1 (sayım belgesiz — kutu "ORTA") | ✓ | K | **✗→✓** | T-Ü | model+kullanıcı · ana · yok · B2 | GEÇTİ | evals.json · "commit yapmaz" beyanı |
| pipeline-kosum | ✓ Y3 | Z1 (3 koşum + bugün 4.) | ✓ | K | **✗→✓** | T-O | model+kullanıcı · ana · yok · B3 | GEÇTİ | evals.json |
| sinav-grill | ✓ Y2 | Salih-tetik (K3 hükmü) | ✓ | K | **✗→✓** | T-Ü | **kullanıcı-yalnız (metin; flag yok — model-tetik yasağı description'da)** · ana · yok · B2 | GEÇTİ | evals.json · "commit yapmaz" beyanı |
| vardiya-kapanis | ✓ Y2/Y3 | ritüel (Salih) | **✗→✓** (DLQ dosyası) | K | **✗→✓** neg-eval 3→5 | T-R + yan-etki faseti | model(cümle) · ana · **yan-etki VAR (commit/push, Salih-beyanı + push-ask kapılı)** · B3 | GEÇTİ | +2 negatif eval · description 872→~690 char |
| wiki-sayfa-yaz | ✓ Y2 | Z2 (Salih onayı 08-14 — zayıf-yeni) | ✓ | K | **✗→✓** | T-Ü | model+kullanıcı · ana · yok · B2 | GEÇTİ | evals.json · "commit yapmaz" beyanı |
| **skill-kapisi** (yeni) | ✓ Y2+Y3 | **Z2 (Salih emri 08-15)** | ✓ 9 ref | ✓ (τ=0,8/k=3 · %43-10/10 · 1024/1536 → rapor B2-2, C1-2, D1-4 SAĞLAM) | ✓ 12/12 | T-Ü | model+kullanıcı · ana · yok · B3+B4 (script) · yukarıdan | **ÜRET-Ü × yeni** | — (kendi kapısını geçti) |

**Toplam:** 14/14 sert kapı GEÇTİ (onarım sonrası); onarım öncesi 9/13 düşüyordu (7 evalsiz · 2 neg-eval eksik · 1 flag eksik · 2 kırık referans).

## 2. Şemanın somut yakalamaları (hallucination-freni ilk sahada)
1. **K2-R referans-varlığı:** `damitma` ve `vardiya-kapanis`, `kuyruk/SINIFLANDIRILAMADI.md`'ye işaret ediyordu; dosya HİÇ YARATILMAMIŞTI (ingest şeması v2 DLQ'su 08-14'te sözleşmede kaldı) → dosya açıldı. Bu, "var-olmayan artefakta atıf" sınıfının (paket-halüsinasyonu analoğu) kanonda yakalanmış ilk örneğidir.
2. **K3-F3 eval-önce ihlali:** 08-14'te üretilen 7 skill'in TAMAMI evalsiz doğmuştu (K-016 eval-önce kuralı fiilen atlanmış) → 7 evals.json geriye dönük yazıldı (3 test + 5/5 description-eval); tam 20×3 description-eval K-016 borcu olarak kalır.
3. **T-Y flag:** `karar-kaydet` yan-etkili (defter yazımı + commit) ama `disable-model-invocation` yoktu — 07-17 standardı ve S-J kutu tasarımı flag'i öngörmüştü; şema kapıya çevirince yakalandı → eklendi.
4. **F1e hazine-bütçesi (yeni koşul):** 14 description toplamı 7.552 char (ritüel çifti kısaltıldıktan sonra; öncesi 7.788) — %1 liste bütçesi ≈2.000 token @200k ≈ 6-8k char [? Türkçe token oranı] → **eşikte/aşımda**. Platform aşımda önce kısaltır, sonra en az çağrılan skill'in description'ını SESSİZCE düşürür = kanondaki "kaçırılan-tetik" sayacına (KG-25-3, ~3 vaka) mekanizma adayı. **Salih'e:** `/context` komutu (v2.1.196+) skill-listing bütçesini gösterir — ölçüm bir komut uzakta.
5. **Ölçüm-proxy sapması:** canlılık envanterinde `damitma` git-log sayımı 99 çıktı — "[damıtma]" commit ETİKETİ, skill koşumu değil (m.43 "ölçüm-aracı-yanıldı" sayacı n=2 → **n=3, eşik doldu**). Şema BAKIM kapısı için gerçek koşum sayacı gerekir → kutuda "kapı-ağacı koşumları" tablosu açıldı (ilk sayaç).

## 3. Kutu adayları (K0/K1 — üretilmemişler)
| aday | K0 | K1 | HÜKÜM |
|---|---|---|---|
| V25 skill-ekosistemi araştırması | ✗ (araştırma GÖREVİ, tekrarlayan prosedür değil) | — | RET-0 skill olarak; görev olarak kutuda kalır |
| V34 skill-avcısı ajan | ✓ Y3 | k_W=0, Z2 yok; K-009/K-010 bloke | BEKLET |
| V61 Record-a-Skill entegrasyonu | ✓ Y3 (dış araç akışı) | k_W=0, Z2 yok | BEKLET |
| önerme→DbC→PBT skill'i (numarasız) | ✓ Y2 (m.38 + DbC kanon-kuralı) | sayım belgesiz | BEKLET (Katman-1 numaralandırma bekliyor) |
| find-skills (kapsül erteleme) | ✓ Y3 | k_W=0 | BEKLET |
| description-eval turu | ✗ (borç/görev, skill değil) | — | RET-0; K-016 borcu olarak kalır |
| "ölçüm-aracı-yanıldı" (m.43 sayaç → n=3 bugün) | ✗ (kural/gotcha, prosedür değil) | — | RET-0 skill olarak; **kural-adayı** olarak lojik-ceviri → tüzük şerhi (pozitif karşılık: kapi-denetim.py zaten proxy-uyarısı üretiyor) |
| S-F vardiya-teslim · S-H seans-basla/bitir | ✗ kapsanmış | — | RET-0 (NOOP/SUPERSEDED teyit) |

## 4. Açık borçlar (bu tur kapatmadı)
- Description-eval tam koşumu (20 sorgu × 3 × 14 skill) — K-016; skill-creator `run_loop.py --holdout 0.4` ile.
- Hazine-bütçesi ölçümü (`/context`, Salih) → gerekirse `skillListingBudgetFraction`/`SLASH_COMMAND_TOOL_CHAR_BUDGET` ayarı ya da description kısaltma turu.
- K2-İ iddia-topraklaması eski skiller için "K" (kaynak raporlarda; bu turda bağımsız doğrulayıcı yalnız skill-kapisi'nin sayısal iddialarına koşuldu — rapor hakem hükümleriyle).
- Şema kalibrasyonu: 10 koşumda τ/W/β/n_val gözden geçirilir (`core/skill-uretim-semasi.md` §5).
