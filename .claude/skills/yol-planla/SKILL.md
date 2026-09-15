---
name: yol-planla
description: Proje-ölçekli görevi (durum,zaman)-düğümlü senaryo-grafa döküp topoloji + maliyet-tavanı + onarım kuralını yol-planı bloğu olarak üretir (S-Ü); planı üretir, koşmaz. Tetik; "yolu planla", "yol planı çıkar", "iskele seç", pipeline/görev-emri öncesi proje-ölçekli işte plan bloğu gerektiğinde. kullanılmaz; m.25 küçük direkt işlerde, koşumda (pipeline-kosum), karar üretiminde (karar-modeli/karar-hatti), gerçek harita/navigasyon sorularında.
---

# yol-planla — senaryo-graf yol-planı üretimi (v0.1-deneysel-m29, 2026-08-16)

Kanıt tabanı: `cc/rapor/2026-08/rapor-2026-08-15-5.md` (Hat-5 m.40b; her kural YT-damgalı — sayısal dayanaklar raporda, gövdeye kopyalanmaz). Tür: T-Ü üretici — çıktı **yol-planı** bloğudur; dosya yazmaz, koşum başlatmaz, commit yapmaz.

## Adımlar (sabit sıra)
1. **Graf kur:** düğüm = (**durum**, **zaman**) çifti — "kronolojik partisyon = düğüm" **değil** [C-YT1]. Açık varsayım beyanı: bekleme-serbest (manifest/durum diskte bekleyebilir; restart-proof ön-şart). Pozitif süreli geçişlerle graf DAG'dır; zaman etiketi topolojik sırayı verir.
2. **Hedef-fonksiyonu seç ve beyan et** [C-YT3]: tek-yürütücülü seri zincir → yol-maliyeti; paralel iş-paketleri → makespan (alt-sınır: max(kritik yol, toplam-iş/eşzamanlılık)); sınırlı ajan kotası → **rcpsp** bakışı, kritik yol yalnız teşhis aracı. En-kısa-yol dili paralel işte **kullanılmaz**.
3. **Topolojiyi görev yapısından türet** [AB-YT6, C-YT7]: her partisyona `birleştirilebilir_mi` alanı yaz. Ayrıştırılıp-birleştirilebilir (map-reduce tipi) → graf/birleştirme düğümlü; bağımsız-paralel → fan; seri-bağımlı zincir → **düz zincir** (iskele kurma — dallanma kazancı yok, planlayıcı maliyeti kalır). İki iskele ancak **eşit** token bütçesinde kıyaslanır [AB-YT5].
4. **İskelet ↔ ağırlık ayrımı** [AB-YT3]: topoloji/partisyon = metrik-BAĞIMSIZ iskelet (bir kez kurulur); model/token/zaman/efor ağırlıkları = koşum-başına özelleştirme katmanı. Ağırlık değişimi iskeleti yeniden kurdurmaz.
5. **Arama/öncelik kuralı — vaat freni** [AB-YT1, C-kör]: kalibre edilmiş kalan-maliyet tahmincisi h() **yoktur** — "A*/optimal yol" **vaat edilmez**; sıralama Dijkstra/greedy/kritik-yol olarak adlandırılır. Heuristik (LLM-kestirimi dahil) kullanılıyorsa: `garanti: yok` damgası + kabul edilen sapma önceden beyan (ε-ilkesi: kötülük sınırı planla birlikte yazılır). LLM yalnız kenar-AĞIRLIĞI tahmincisidir; yol hesabı deterministik iskelette [AB-YT8].
6. **Onarım dalı** [AB-YT2/YT7, C-YT4]: yalnız **dış** doğrulanabilir sinyal açar (test çıktısı · yürütme hatası · journal/manifest durumu · kesinti kaydı) — modelin öz-yargısı onarım tetiği **değil** (üretici≠doğrulayıcı; F3 ile aynı ilke). Onarım **tavanlı**: tavan (tur/süre/token) planda sayı olarak yazılır; aşılırsa onarım **iptal** + baştan planla. Sapma yaygın ya da köke yakınsa doğrudan baştan planla.
7. **Çıktı = yol-planı bloğu** (görev-emri/manifeste gömülür): `graf (düğüm/kenar + birleştirilebilir_mi) · hedef-fonksiyon beyanı · topoloji + gerekçe · iskelet/ağırlık tablosu · maliyet-tavanı (dışarıdan verilir; plan tavansız TESLİM EDİLMEZ) · onarım kuralı (sinyal + tavan) · damgalar`. Her ampirik hücre (model, sürüm, tarih) üçlüsü taşır [C-YT8]; token×zaman×risk tek-skaler indirgeme deneysel m.29 damgalı.

## Gotchas
- **"A*" tuzağı:** ad çekici, ön-koşul yok — h()'siz A* iddiası şemadan `DÜŞTÜ` (rapor-5 en-kritik kör). Plan "A* kullanır" yazamaz.
- **Benzetme sınırı** [AB-YT4]: CH/HL-sınıfı önişlem hızlanmaları **sabit** graf ister; LLM-görev grafında kenarlar koşumda keşfedilir — aktarılabilir çekirdek yalnız ε-sınır mantığı + onarım-bütçesi desenidir.
- **Anytime ≠ dinamik** [C-YT5]: "ucuz-önce sonra iyileştir" (statik maliyet) ile "koşumda değişen maliyet" iki ayrı eksendir; plan hangisinde olduğunu beyan eder.
- **Ölçüm borcu:** onarım-tavanı ve iskele-maliyet eğrisi literatürde boş — ilk koşumlar kendi ölçümünü `kuyruk/skill-fikir-kutusu.md` ölçüm tablosuna yazar (10 koşumda kalibrasyon).
