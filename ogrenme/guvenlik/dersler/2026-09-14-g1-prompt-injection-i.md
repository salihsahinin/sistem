# Ajan Güvenliği G1: Prompt Injection I — ders 1 (2026-09-14; ogren v0.1)

**Sektör başlığı:** *Prompt Injection* · *Indirect Prompt Injection* · OWASP Top 10 for LLM Applications **LLM01** (2026 sürümünde de #1, yayın 2026-08-04) · *Hidden Context Exposure* (2026 OWASP'ta yeniden adlandırma; eski adı *System Prompt Leakage*, LLM07) — **AS-OF 2026-09-14 canlı doğrulandı** (WebSearch, bkz. Kaynak notu altta).

## Ön-bağlam
Yok (PROBE tam koşar).

## Anlayış haritası
(PROBE ilerledikçe doldurulacak — iplik | ulaşılan seviye | kanıt soru-no)

| İplik | Seviye | Kanıt (soru no) |
|---|---|---|
| İ1: Prompt injection temel tanımı | 0 (sınır en temel seviyenin altında) | soru 1 |
| İ2: Doğrudan ↔ dolaylı ayrımı | 0 | soru 2 |
| İ3: Talimat/veri neden mekanik ayrılamaz | 0 | soru 3 |
| İ4: Sistem-prompt sızdırma / Hidden Context Exposure | 0 | soru 4 |
| İ5: Savunma katmanları (ayrım/izin/tespit) | 0 | soru 5 |

Sonuç: 5 iplik de sıfırdan başlıyor → PLAN tüm temel düğümleri içerir, hiçbir düğüm "bilinen" sayılıp atlanmaz.

## Plan
DAG görseli: `g1_prompt_injection_dag` (mcp__visualize, bu seansta gösterildi; kalıcı kopya istenirse ayrıca kaydedilir). Renk: mercan = saldırı mekanizması (1-5), deniz mavisi = savunma katmanı (6-8).

Düğüm listesi (numaralar görsele atıflı):
1. Prompt injection tanımı
2. Talimat/veri neden mekanik ayrılamaz (→1)
3. Doğrudan injection (→2)
4. Dolaylı injection (→2, 3 ile paralel)
5. Sistem-prompt sızdırma / Hidden Context Exposure (→3 ve 4'ün birleşimi)
6. Savunma: ayrım (→5)
7. Savunma: izin — en-az-yetki (→5, 6 ile paralel)
8. Savunma: tespit (→5, 6-7 ile paralel)

8 düğüm = seans tavanı (≤8); bu derste hepsi işlenecek. Salih itiraz etmedi → TEACH başlıyor.

## Düğümler

| Kutu | Konu | Soru | Cevap | Sonuç |
|---|---|---|---|---|
| 1 | Prompt injection tanımı | model, talimat ile veriyi neden aynı statüde işler | c | DOĞRU |
| 2 | Talimat/veri mekanik ayrılamaz | delimiter injection'ı neden tam çözmez | c | DOĞRU |
| 3 | Doğrudan injection | ayırt edici özellik: girdi kanalı | c | DOĞRU |
| 4 | Dolaylı injection | doğrudandan farkı: üçüncü-taraf içerik, saldırgan-kurban teması yok | c | DOĞRU |
| 5 | Sistem-prompt sızdırma / Hidden Context Exposure | saldırgana sağladığı avantaj: savunma mantığının ifşası | c | DOĞRU |
| 6 | Savunma: ayrım | riski sıfırlamaz, saldırı yüzeyini daraltır | c | DOĞRU |
| 7 | Savunma: izin (en-az-yetki) | zararı sınırlar, saldırıyı önlemez | c | DOĞRU |
| 8 | Savunma: tespit | diğer iki katmandan farkı: saldırıyı gerçekleşmeden yakalamaya çalışır | a | DOĞRU |

8/8 kutu doğru, hiçbiri "AÇIK" kalmadı.

**Formül (Karar 73 — bu derste eksik kalan, burada tamamlanıyor):** saldırı-başarı oranı ASR = başarılı deneme sayısı / toplam deneme sayısı. Elle örnek (varsayımsal, henüz gerçek koşum değil — "türetildi" damgalı): 10 injection vakasından 3'ü başarılı olsaydı ASR = 3/10 = 0,30. Gerçek Wilson %95 güven aralığı hesaplaması ve gerçek 10 vakalık promptfoo koşumu **Kalan**'a düşüyor (aşağıda).

## Salih notu
- (kutu 3'te) "cevap c, caps lock açık bir şekilde kelime vurguları yapma" — büyük harfle vurgu bu dersten itibaren yok, bold kullanılıyor.

## Kalan
Kavramsal 8 düğüm bitti; G1'in "hafta DONE"u henüz yazılı değil. README'deki G1 pratik-uygulama adımı kalan: oyuncak ajan (tek araç: web-sayfası-oku) kurup 10 injection vakasını promptfoo'da koşturmak, gerçek ASR + Wilson %95 GA hesaplamak. Bu, ya bu oturumun devamında ya da sonraki "seans başı, guvenlik" turunda yapılır.

## Kaynak notu (m.39 / Karar 68)
WebSearch 2026-09-14: OWASP Top 10 for LLM Applications 2026 sürümü (yayın 2026-08-04) — Prompt Injection hâlâ LLM01/#1; System Prompt Leakage → *Hidden Context Exposure* olarak yeniden adlandırıldı; Excessive Agency 6.'dan 3.'e yükseldi. Kaynaklar: mend.io, checkmarx.com, hackerdna.com (arama sonucu özetinden).
