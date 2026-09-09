---
name: yol-planla
description: Proje-ölçekli görevi (durum,zaman)-düğümlü senaryo-grafa döküp topoloji + maliyet-tavanı + onarım kuralını YOL-PLANI bloğu olarak üretir (S-Ü); planı üretir, KOŞMAZ. Tetik; "yolu planla", "yol planı çıkar", "iskele seç", pipeline/görev-emri öncesi proje-ölçekli işte plan bloğu gerektiğinde. KULLANILMAZ; m.25 küçük direkt işlerde, koşumda (pipeline-kosum), karar üretiminde (karar-modeli/karar-hatti), gerçek harita/navigasyon sorularında.
---

# yol-planla — senaryo-graf yol-planı üretimi (v0.1-deneysel-m29, 2026-08-16)

Kanıt tabanı: `cc/rapor/2026-08/rapor-2026-08-15-5.md` (Hat-5 m.40b; her kural YT-damgalı — sayısal dayanaklar raporda, gövdeye kopyalanmaz). Tür: T-Ü üretici — çıktı YOL-PLANI bloğudur; dosya yazmaz, koşum başlatmaz, commit yapmaz.

## Adımlar (sabit sıra)
1. **Graf kur:** düğüm = (DURUM, ZAMAN) çifti — "kronolojik partisyon = düğüm" DEĞİL [C-YT1]. Açık varsayım beyanı: bekleme-serbest (manifest/durum diskte bekleyebilir; restart-proof ön-şart). Pozitif süreli geçişlerle graf DAG'dır; zaman etiketi topolojik sırayı verir.
2. **Hedef-fonksiyonu seç ve BEYAN et** [C-YT3]: tek-yürütücülü seri zincir → yol-maliyeti; paralel iş-paketleri → makespan (alt-sınır: max(kritik yol, toplam-iş/eşzamanlılık)); sınırlı ajan kotası → RCPSP bakışı, kritik yol yalnız teşhis aracı. En-kısa-yol dili paralel işte KULLANILMAZ.
3. **Topolojiyi görev yapısından türet** [AB-YT6, C-YT7]: her partisyona `birleştirilebilir_mi` alanı yaz. Ayrıştırılıp-birleştirilebilir (map-reduce tipi) → graf/birleştirme düğümlü; bağımsız-paralel → fan; seri-bağımlı zincir → DÜZ ZİNCİR (iskele kurma — dallanma kazancı yok, planlayıcı maliyeti kalır). İki iskele ancak EŞİT token bütçesinde kıyaslanır [AB-YT5].
4. **İskelet ↔ ağırlık ayrımı** [AB-YT3]: topoloji/partisyon = metrik-BAĞIMSIZ iskelet (bir kez kurulur); model/token/zaman/efor ağırlıkları = koşum-başına özelleştirme katmanı. Ağırlık değişimi iskeleti yeniden kurdurmaz.
5. **Arama/öncelik kuralı — VAAT FRENİ** [AB-YT1, C-kör]: kalibre edilmiş kalan-maliyet tahmincisi h() YOKTUR — "A*/optimal yol" VAAT EDİLMEZ; sıralama Dijkstra/greedy/kritik-yol olarak adlandırılır. Heuristik (LLM-kestirimi dahil) kullanılıyorsa: `garanti: yok` damgası + kabul edilen sapma önceden beyan (ε-ilkesi: kötülük sınırı planla birlikte yazılır). LLM yalnız kenar-AĞIRLIĞI tahmincisidir; yol hesabı deterministik iskelette [AB-YT8].
6. **Onarım dalı** [AB-YT2/YT7, C-YT4]: yalnız DIŞ doğrulanabilir sinyal açar (test çıktısı · yürütme hatası · journal/manifest durumu · kesinti kaydı) — modelin öz-yargısı onarım tetiği DEĞİL (üretici≠doğrulayıcı; F3 ile aynı ilke). Onarım TAVANLI: tavan (tur/süre/token) planda sayı olarak yazılır; aşılırsa onarım İPTAL + baştan planla. Sapma yaygın ya da köke yakınsa doğrudan baştan planla.
7. **Çıktı = YOL-PLANI bloğu** (görev-emri/manifeste gömülür): `graf (düğüm/kenar + birleştirilebilir_mi) · hedef-fonksiyon beyanı · topoloji + gerekçe · iskelet/ağırlık tablosu · maliyet-tavanı (dışarıdan verilir; plan tavansız TESLİM EDİLMEZ) · onarım kuralı (sinyal + tavan) · damgalar`. Her ampirik hücre (model, sürüm, tarih) üçlüsü taşır [C-YT8]; token×zaman×risk tek-skaler indirgeme deneysel m.29 damgalı.

## Gotchas
- **"A*" tuzağı:** ad çekici, ön-koşul yok — h()'siz A* iddiası şemadan DÜŞTÜ (rapor-5 en-kritik kör). Plan "A* kullanır" yazamaz.
- **Benzetme sınırı** [AB-YT4]: CH/HL-sınıfı önişlem hızlanmaları SABİT graf ister; LLM-görev grafında kenarlar koşumda keşfedilir — aktarılabilir çekirdek yalnız ε-sınır mantığı + onarım-bütçesi desenidir.
- **Anytime ≠ dinamik** [C-YT5]: "ucuz-önce sonra iyileştir" (statik maliyet) ile "koşumda değişen maliyet" iki ayrı eksendir; plan hangisinde olduğunu beyan eder.
- **Ölçüm borcu:** onarım-tavanı ve iskele-maliyet eğrisi literatürde boş — ilk koşumlar kendi ölçümünü `kuyruk/skill-fikir-kutusu.md` ölçüm tablosuna yazar (10 koşumda kalibrasyon).
