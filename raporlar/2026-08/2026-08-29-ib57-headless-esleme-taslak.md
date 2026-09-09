# İB-57 — Headless iş-sınıfı → yüzey eşleme TASLAĞI (masaya döner)

**AS-OF 2026-08-29 (ölçüm ~20:1x) · icra devam oturumu (Fable) · K1-2 yeniden çerçeve (entegrasyon masası 08-21 → Karar 76 E7: "hangi iş sınıfı headless'a iner") · araç [tools/headless-esleme.py](../tools/headless-esleme.py) (stdlib, LLM YOK) · veri: silver `hareket` (62 oturum, 4.206 çağrı) + ambar `amb_olgu_kosum` (ajan koşumları) · deneysel m.29 — HÜKÜM DEĞİL, masa girdisi.**

*Ne bu:* "Model-3'e geçelim mi" sorusu 08-17'de düştü (ana-sıra = CC); kalan soru hangi iş sınıfının etkileşimsiz (headless: `claude -p`, `schedule`, Remote Control, Agent/Workflow alt-koşumu) koşabileceği. Bu taslak sınıfları VERİDEN türetir ve tek bir deterministik kuralla yüzey önerir; Salih masada kuralı ve eşikleri değiştirir.

## 0. Kural (deterministik, deneysel)
- `ask_oran` = skill çağrısını izleyen 12 adımda `AskUserQuestion` sayısı / çağrı. **> 0 → ANA-SIRA** (karar içeriyor).
- `ask_oran = 0 ∧ oturum ≥ 3 ∧ icra_adim ≥ 5` → **HEADLESS-ADAY** (girdi dosya, çıktı dosya, karar yok, tekrar var).
- aksi → **BELİRSİZ** (n küçük ya da icra yok). Ajan sınıfları → **ZATEN-HEADLESS** (fiilî yüzey Agent ∨ Workflow).
- Sayım: ANA-SIRA 3 · BELİRSİZ 11 · HEADLESS-ADAY 6 · ZATEN-HEADLESS 27 (toplam 47 sınıf).

## 1. Skill icra profilleri (etkileşimli ana-sıra sınıfları)
| Skill (iş sınıfı) | çağrı | oturum | Ask oranı | icra adım (Bash+Write+Edit) | alt-koşum adım | yüzey önerisi |
|---|---|---|---|---|---|---|
| seans-acilis | 25 | 25 | 0.04 | 9.5 | 0.0 | **ANA-SIRA** |
| seans-kapanis | 17 | 16 | 0.0 | 9.2 | 0.0 | **HEADLESS-ADAY** |
| atlas-kosum | 7 | 7 | 0.0 | 6.1 | 2.7 | **HEADLESS-ADAY** |
| gunaydin-vardiya | 7 | 7 | 0.14 | 8.7 | 0.1 | **ANA-SIRA** |
| gorev-emri-derleme | 6 | 6 | 0.0 | 10.0 | 0.3 | **HEADLESS-ADAY** |
| pipeline-kosum | 6 | 6 | 0.0 | 10.3 | 0.5 | **HEADLESS-ADAY** |
| wiki-sayfa-yaz | 6 | 6 | 0.0 | 11.3 | 0.0 | **HEADLESS-ADAY** |
| staj-acilis | 4 | 4 | 0.0 | 9.8 | 0.0 | **HEADLESS-ADAY** |
| damitma | 2 | 2 | 0.0 | 10.0 | 0.0 | **BELİRSİZ** |
| lavish | 2 | 2 | 0.0 | 11.0 | 0.0 | **BELİRSİZ** |
| anthropic-skills:vardiya-kapanis | 1 | 1 | 1.0 | 6.0 | 0.0 | **ANA-SIRA** |
| anthropic-skills:xlsx | 1 | 1 | 0.0 | 8.0 | 0.0 | **BELİRSİZ** |
| artifact-diagramming | 1 | 1 | 0.0 | 4.0 | 0.0 | **BELİRSİZ** |
| celiski-kapisi | 1 | 1 | 0.0 | 11.0 | 0.0 | **BELİRSİZ** |
| dataviz | 1 | 1 | 0.0 | 3.0 | 0.0 | **BELİRSİZ** |
| no-mistakes | 1 | 1 | 0.0 | 9.0 | 0.0 | **BELİRSİZ** |
| skill-kapisi | 1 | 1 | 0.0 | 11.0 | 1.0 | **BELİRSİZ** |
| staj-kapanis | 1 | 1 | 0.0 | 8.0 | 0.0 | **BELİRSİZ** |
| vardiya-kapanis | 1 | 1 | 0.0 | 7.0 | 0.0 | **BELİRSİZ** |
| yol-planla | 1 | 1 | 0.0 | 11.0 | 1.0 | **BELİRSİZ** |

## 2. Ajan koşum sınıfları (fiilen headless) — ilk 12
| Ajan sınıfı [tip] | n | süre ort (sn) | çıktı token | fiilî yüzey |
|---|---|---|---|---|
| Atlas ANTİTEZ ajanı [atlas] | 92 | 531.0 | 2839759 | ZATEN-HEADLESS: Agent alt-koşum |
| Atlas TEZ araştırmacısı [atlas] | 80 | 443.0 | 1878950 | ZATEN-HEADLESS: Agent alt-koşum |
| MASKELİ HAKEM [workflow-subagent] | 75 | 287.0 | 1685101 | ZATEN-HEADLESS: Workflow |
| - [atlas] | 56 | 805.0 | 2109611 | ZATEN-HEADLESS: Agent alt-koşum |
| - [general-purpose] | 54 | 312.0 | 815869 | ZATEN-HEADLESS: Agent alt-koşum |
| DENETÇİ [general-purpose] | 30 | 12.0 | 6636 | ZATEN-HEADLESS: Agent alt-koşum |
| V26 örneklem-denetçisi [workflow-subagent] | 11 | 151.0 | 103195 | ZATEN-HEADLESS: Workflow |
| V26 örneklem-denetçisi [workflow-subagent] | 11 | 111.0 | 70438 | ZATEN-HEADLESS: Workflow |
| V26 örneklem-denetçisi [workflow-subagent] | 11 | 88.0 | 63340 | ZATEN-HEADLESS: Workflow |
| silver-sağlık T-A KANIT-BULUCU [general-purpose] | 10 | 20.0 | 9295 | ZATEN-HEADLESS: Agent alt-koşum |
| - [Explore] | 8 | 297.0 | 201430 | ZATEN-HEADLESS: Agent alt-koşum |
| - [claude-code-guide] | 8 | 51.0 | 16752 | ZATEN-HEADLESS: Agent alt-koşum |

## 3. Okuma — taslağın söyledikleri ve söyleyemedikleri
- **Proxy zayıf:** `AskUserQuestion` Salih kararının yalnız araçlı biçimini sayar; kararların çoğu sohbet metninde akar (seans-kapanis'te push beyanı m.9, kapsül imzası). Bu yüzden `seans-kapanis` "HEADLESS-ADAY" çıkması **kuralın sınırı**, öneri değil — kapanışın headless'a inmesi K-010 A3 kontrol-devri kapısına (kanıt: /goal 1 OK ∧ /loop durma-koşullu 1 OK ∧ Routine 3 OK) bağlıdır; A3 güvence yazımı = İB-55.
- **Gerçek adaylar (karar yok + dosya-üreten + tekrarlı):** `gorev-emri-derleme` (6/6, icra 10,0) · `wiki-sayfa-yaz` (6/6, 11,3) · `pipeline-kosum` (6/6; zaten yarı-headless: manifest + Workflow) · `atlas-kosum` (7/7; Workflow'a devrediyor, ana-sıra yalnız emir + hasat). Bunlar "emir dosyası → koşum → rapor dosyası" biçimindedir; `claude -p` ile sürücü betiği yazılabilir (Model-3 resmi yolu, K-015 K-017 notu).
- **Ana-sırada kalması gerekenler:** `seans-acilis` (brif Salih'e; Ask 0,04) · `gunaydin-vardiya` (emekli ad; aynı sınıf) · Lavish masaları (Salih yüzeyi).
- **Zaten headless:** atlas tez/antitez/hakem/V26 (Workflow), DENETÇİ + kanıt-bulucu (Agent alt-koşum; 12-20 sn, ~1 araç çağrısı — en ucuz sınıf).
- **Loop-dedektörü bağı (İB-60):** kutuya düşen 4 n≥3 aday (`Write:cc → py:inline → Workflow` ailesi) = "emir yaz → hazırla → koştur" dizisi; headless-aday sınıfıyla aynı iş.

## 4. Masaya sorular (Salih)
1. Kural eşikleri: `oturum ≥ 3`, `icra_adim ≥ 5`, pencere 12 — kabul / değiştir.
2. Karar-proxy'si: `AskUserQuestion` yetmez; kapanış/açılış ritüelleri kural-dışı "ANA-SIRA zorunlu" listesine mi alınsın (m.41 GK-2 ile uyumlu)?
3. İlk headless pilotu: `gorev-emri-derleme → atlas-kosum` zinciri mi, `wiki-sayfa-yaz` mı? (A3 kapısı önce — K-010 sırası: A1∧A2→A3.)
4. Yüzey adı: `claude -p` (Model-3) ↔ `schedule` (Routine) ↔ Remote Control — sınıf başına tek yüzey mi, iş-ölçeğine göre mi (m.25)?

## 5. Yeniden üretim
`python3 tools/headless-esleme.py` → `veri/gorunum/v_headless_esleme.csv` (bu tablolar oradan; hareket kütüğü büyüdükçe sayılar değişir, kural sabit).
