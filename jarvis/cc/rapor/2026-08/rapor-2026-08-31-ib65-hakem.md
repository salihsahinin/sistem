# IB-65 — Maskeli Hakem Raporu (m.40b Aşama-3)

## Künye
- **Rol:** Maskeli hakem (kaynak-kimlikleri maskeli; yalnız iddia + URL + kanıt görüldü)
- **Model:** opus
- **AS-OF:** 2026-08-31
- **Girdi:** ŞERİT-1 (23 iddia) · ŞERİT-2 (6 hedefli çürütme sonucu) · ŞERİT-3 (bağımsız birincil-kaynak sondajı: iddia 6, 18, 20/21/22)
- **Yöntem:** Sıra bilgisi yargıda kullanılmadı; WEB çekimi yapılmadı; yargı yalnız sunulan materyalden.
- **MASKELEME SIZINTI BEYANI (K2-k şerhi):** Maskeleme TAM DEĞİLDİR. Bazı iddialarda vendor/ürün adı (Temporal 7/10/11/12/13, Airflow 8/14/15/16, Prefect 17, Dagster 18/19, Beam 3/4, Kubernetes 1/2, Claude Code 20-23) kaynak-kimliğini fiilen ele veriyor; alan-ailesi bölünmesi ürün-eksenli olduğu için hangi Atlas ailesinin ürettiği çıkarsanabilir durumda. Bu sızıntı yargıyı kaynak-güvenilirliği (resmî-dok / vendor / ikincil) ekseninde etkilemiş olabilir; ayrıca iddia 7'de "vendor sitesi" damgası maskeyi kendi başına delmektedir. Beyan açık tutulmuştur.

## Tablo — 23 iddia

| # | Etiket | Gerekçe |
|---|---|---|
| 1 | D | Resmî Kubernetes controller dokümanı non-terminating control loop tanımını birebir taşır; çürütme denenmemiş. |
| 2 | K | İçerik doğru ve çürütme başarısız, ancak tez tarafındaki kaynak ikincil bloktur; resmî doğrulama ŞERİT-2 raporu üzerinden dolaylıdır. |
| 3 | D | Beam resmî "basics" sayfası bounded/unbounded, watermark-tahmini ve trigger tanımlarını doğrudan verir. |
| 4 | K | Ortak model iddiası resmî programming guide ile örtüşür, ama "batch = unbounded'ın tamamlanmış özel hâli" formülasyonu yorumdur, kaynakta bu cümleyle yer almaz. |
| 5 | D | Alpern & Schneider 1985 akademik birincil kaynak; safety-kapalı / liveness-yoğun ve her property'nin kesişim olduğu teoremi tam olarak bu makalenin sonucudur. |
| 6 | K | ŞERİT-3 sondajı well-founded tanımını birebir doğruladı, ancak "ranking function" adıyla formal tanım sayfada yok ("measure" kullanılıyor) — iddia terim düzeyinde daraltılmalı. |
| 7 | K | Determinizm/replay/kontrol-akışı içeriği doğru fakat kaynak vendor sitesidir ve ŞERİT-2 ayrımın formal değil mühendislik-pratiği düzeyinde kaldığını gösterdi. |
| 8 | K | Airflow-tipi DAG'ın sonlu/asiklik/terminal olduğu pratikte geçerli ama kaynak ikincil bloglar; ŞERİT-2 nötr/akademik dayanak bulamadı ve iç içe geçebilme itirazını kaydetti. |
| 9 | X | ŞERİT-2 çürütmesi BAŞARILI: kaskad kontrolde iç döngü de süreklidir/terminate etmez, benzetme yapısal olarak yanlış; "yakıt enjeksiyonu" formal kanıt tekniği değil. |
| 10 | D | Resmî Temporal limits sayfası 51.200 event / 50 MB sınırını ve 10.240 / 10 MB uyarı eşiğini birebir verir. |
| 11 | D | Continue-As-New resmî design-pattern sayfasının tanımıyla birebir; tamamla-taşı-sıfırla mekanizması aynen budur. |
| 12 | D | Resmî dokümana dayalı, ayrıca hedefli çürütme denemesi BAŞARISIZ — 1000 child rakamı birebir doğrulandı. |
| 13 | D | Resmî retry-policies sayfası tüm alan varsayılanlarını (1sn, 2.0, ×100, sınırsız) ve Activity-retry / Workflow-retry-yok ayrımını verir. |
| 14 | D | Resmî deferring dokümanı (3.3.1) worker-slot bırakma + triggerer devri ile reschedule/deferrable iki modunu doğrudan tanımlar. |
| 15 | K | İçerik resmî dokümandan ama kaynak 2.4.0 sürüm dokümanıdır; 3.3.1 hattına göre sürüm-bayat, iddia AS-OF damgasıyla daraltılmalı. |
| 16 | K | Hedefli çürütme BAŞARISIZ ve 3.3.1 resmî dokümanında birebir doğrulandığı raporlandı, ancak tez tarafındaki asıl kaynak ikincildir. |
| 17 | D | Prefect v3 resmî how-to sayfası subflow'un doğrudan Python çağrısı olduğunu ve flow-seviyesi retries/retry_delay_seconds/timeout_seconds parametrelerini verir. |
| 18 | X | ŞERİT-3 sondajı: on_cron/eager/on_missing ve varsayılan sensör doğrulandı ama `use_sensors: true` ayarı kaynakta YOK — iddianın "ZORUNLUDUR" kısmı desteksiz, bileşik iddia düşer. |
| 19 | K | Task-akışı ↔ asset-odaklılık ayrımı iki ürünün resmî konumlandırmasıyla tutarlı, ancak iddiaya URL/kanıt iliştirilmemiştir; nötr kaynak yok. |
| 20 | D | ŞERİT-3 sondajı üç kip ve loop.md özelleştirmesi dahil resmî scheduled-tasks sayfasında birebir doğruladı. |
| 21 | D | ScheduleWakeup(stop:true), ~20dk fallback wakeup ve 7-gün expiry alıntı düzeyinde birebir doğrulandı. |
| 22 | D | 50 task/session, 1dk minimum interval, 7 gün expiry, 25.000 byte kesme — dördü de sondajda birebir alıntılandı. |
| 23 | X | ŞERİT-2 çürütmesi BAŞARILI: hooks zinciri, subagent zincirleme ve Dynamic Workflows adım-bağımlılığı sağlıyor; ayrıca /goal, Channels, Routines ve GitHub Actions yüzeyleri mevcut. |

## ÖZET

| Etiket | Sayı | İddia numaraları |
|---|---|---|
| **D (destekli)** | 12 | 1, 3, 5, 10, 11, 12, 13, 14, 17, 20, 21, 22 |
| **K (kısmi)** | 8 | 2, 4, 6, 7, 8, 15, 16, 19 |
| **X (çürük)** | 3 | 9, 18, 23 |

Toplam 12 + 8 + 3 = 23.

**m.40b hayatta-kalma metriği:**
- **SAĞLAM** (adversarial baskıdan tam çıkan) = **12**
- **DARALDI** (kapsam ∨ kaynak-gücü düşerek hayatta kalan) = **8**
- **DÜŞTÜ** (çürütme başarılı ∨ kaynak desteklemiyor) = **3**
- Hayatta-kalma oranı: 20/23 = %87 (tam sağlamlık %52).
- Hedefli çürütme isabet oranı: 6 denemenin 2'si tam başarılı (9, 23), 1'i kısmen başarılı (7/8 hattı), 3'ü başarısız (2, 12, 16).

## HAKEM NOTU

**Seçim-kuralı tasarımında EN GÜVENİLİR 5 iddia** (birincil resmî kaynak + bağımsız sondaj ∨ başarısız çürütme ile çift-teyitli, sayısal ve doğrudan uygulanabilir):
1. **#22** — tavanlar (50 task/session, 1dk min interval, 7 gün expiry, 25.000 byte loop.md): sondajda alıntı düzeyinde teyitli; seçim kuralının sert sınır-parametreleri buradan alınmalı.
2. **#21** — durma koşulu API'si (ScheduleWakeup stop:true, ~20dk fallback, 7 gün expire): terminasyon mekanizmasının tek birincil-teyitli tanımı.
3. **#20** — /loop üç kipi (sabit interval / self-paced / built-in prompt): yüzey seçiminin tabanı, sondajda tam doğrulandı.
4. **#5** — safety/liveness ve her property'nin kesişim olması: akademik birincil kaynak, vendor-bağımsız; "durma koşulu" ile "ilerleme koşulu"nu ayırmanın formal zemini.
5. **#10 + #11 + #13 demeti (temsilci: #11)** — Temporal history limitleri, Continue-As-New ve retry varsayılanları: üçü de resmî dokümandan sayısal, birbirini tamamlayan; ölçek/tekrar bütçesi kuralı buradan kurulabilir. (#12 de aynı güvende: hedefli çürütmeden sağ çıktı.)

**EN RİSKLİ 3 iddia** (seçim kuralına GİRMEMELİ ∨ yeniden doğrulanmadan girmemeli):
1. **#9** — kaskad-kontrol benzetmesi + "bütçe kalıtımı = yakıt enjeksiyonu": yapısal olarak yanlış (iç döngü de sürekli), formal kanıt tekniği değil. İç-içe loop tasarımı bu analojiye DAYANDIRILAMAZ; terminasyon iddiası ranking-function/measure diliyle (bkz. #6 şerhi) ayrıca kurulmalı.
2. **#18** — `use_sensors: true` zorunluluğu kaynakta yok; Dagster otomasyonuna dair operasyonel varsayım hatalı. Bileşik iddianın doğrulanan kısmı (on_cron/eager/on_missing + varsayılan sensör) ayrıştırılmadan kullanılmamalı.
3. **#23** — "Claude Code'da loop↔pipeline eşdeğeri yok" tersine döndü; adım-bağımlılığı hooks/subagent/Dynamic Workflows ile mevcut. Bu iddiaya dayanan her "kendi pipeline'ımızı yazmalıyız" gerekçesi geçersizdir; ayrıca /goal ve Channels ayrı mekanizmalar olarak dikkate alınmalı.

**İkincil risk şeridi (K bloğu içinden):** #15 (Airflow 2.4.0 sürüm-bayat kaynağı — 3.3.1'e karşı yeniden çekilmeli), #7/#8 hattı (durable-execution ↔ DAG ayrımı nötr/akademik dayanaktan YOKSUN; tasarım gerekçesi olarak kullanılırsa "vendor söylemi" damgasıyla kullanılmalı), #6 (terim "ranking function" değil "measure" — formal alıntıda ad düzeltilmeli), #19 (URL/kanıt iliştirilmemiş tek iddia).
