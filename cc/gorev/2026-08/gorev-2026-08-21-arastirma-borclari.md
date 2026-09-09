# Görev Emri — Araştırma Borçları Scout Dalgası (7 işçi; pipeline: cc/pipeline-2026-08-21-arastirma-borclari.md)

*Derleyen: Carvis (Fable, ana-sıra, paralel oturum s13). Rejim: **[maliyet-öncelikli]**. Salih beyanı: "sistemdeki araştırma borçlarını pipeline kur koş" (08-21 akşam).*

## ORTAK BLOK (her rol için geçerli — statik)
- **Mekanik kapılar:** her rakam KAYNAKLI (m.39; kestirim `[?]` damgalı) · uydurma YASAK, "bulunamadı" meşru cevaptır, erişim engeli bayraklanır · her bulgu **D** (doğrulanmış: kaynağı açıldı/okundu) / **K** (kaynaklı ama tek-kaynak/okunamadı) / **X** (belirsiz/çelişkili) etiketli + URL · işçi DÖNÜŞ mesajı ≈1-2k token özet (rapor dosyaya, dönüşe özet).
- **Halüsinasyon sözleşmesi:** H=7 TETİK (v3a atıf-türü override; derece.py 08-21) → kaynak-topraklama zorunlu: her iddianın yanına kaynak; F1 yapılandırılmış kaynak listesi + F2 destek-kontrolü (rapor sonunda: hangi iddia hangi kaynağa dayanıyor) + F3/F5 atıf tekil doğrulama (URL'yi AÇMADAN künye yazma).
- **Yazım sınırı (paralel-oturum freni):** YALNIZ kendi rapor dosyana yaz; repoda başka HİÇBİR dosyaya dokunma (ledger/kutu/defter/kapsül/core kesin yasak); commit YAPMA (commit lider işidir).
- **Araçlar:** WebSearch + WebFetch (dış) · Read/Grep/Glob (iç, yalnız belirtilen dosyalar) · Bash yalnız salt-okur komut.
- **Türkçe rapor** (İngilizce alıntı üstte Türkçe özetle); şablon: başlık · bulgular (D/K/X + URL) · "Jarvis'e uygulanabilirlik" bölümü · F2 destek-tablosu · "cevaplanamayanlar" listesi.
- done_olcumu: DRFR — emrindeki her koşul tek tek · yeniden_deneme: 3 · FAIL-LOUD.

## SKILL TETİKLERİ
- skill: halusinasyon-engelleyici
  tetik_kosulu: çıktı atıf/URL/kaynakça içeriyor (v3a) — her rolde AKTİF; çıktı atıfsız iç-özet ise ÇAĞIRMA
  cagri_kipi: ortuk (F1+F2+F3/F5 disiplini ORTAK BLOK'a gömülü; skill gövdesi işçide açılmaz)
  girdi: rol emri + kaynak listesi
  baglam: ORTAK BLOK
  yan_etki_damgasi: salt-okur × idempotent:e × dış-dünya:h
  done_yuklemi: raporda F2 destek-tablosu var ∧ etiketsiz iddia 0
  hata_yolu: etiketsiz iddia → çağıran (Carvis hakemliği) DAYANAKSIZ sayar · retry ≤3 · FAIL-LOUD
  sira: her rolün içinde (7/7 paralel; handoff = rapor dosyası)
  kayit: execute_tool · tool.name=halusinasyon-engelleyici · agent=S-1a..S-5 · error.type · model+sürüm · tarih → skill sayacı + kuyruk/halusinasyon-kayit.md (Carvis düşer)

---

## S-1a — skill-bakım TEZ (AB-1)
```
gorev_adi: skill-bakim-tez · rol: scout · rejim: maliyet-öncelikli · model: sonnet
kosum_profili: sonnet × medium × ~15k bağlam × TAHMİN 4-7k çıktı · 15-30 araç · 4-8 dk (Carvis/Fable tahmini)
cagri_kosulu: skill-bakım sistemi tasarımına dış hammadde gerektiğinde
arastirma_sorusu: LLM-ajan skill/prompt varlıklarının PERİYODİK BAKIMI dışarıda nasıl çözülmüş? (eval yenileme · description/tetik isabeti ölçümü · kullanım+drift ölçümü · emeklilik/onarım kriteri · bakım aralığı/tetiği: takvim ∨ koşum-sayısı ∨ sapma-sinyali)
KANONDA-BİLİNENLER (verili kabul et, üstüne koy — TEKRAR ARAŞTIRMA):
  - İçeride VAR: skill-uretim-semasi BAKIM düğümü (Δ̂ ilk pencerede ölçülür) · İB-07 description-eval planı (20 sorgu×3×14 skill) · v_skill_kosum görünümü CANLI (skill×model: n·token·süre·sonuc/fail) · eşik kuralı Karar 51 (n≥10 → medyan band, 2× sapma raporu) · m.43 pencereli sayaç (N=5, W=90 gün) · Anthropic skill-creator'ın eval/benchmark komutları.
  - Kural: HAZIRI TEMEL AL (KB-14) — sıfırdan bakım sistemi tasarlama; bulduğun pratikleri bu parçaların ÜSTÜNE bindirilebilirlik açısından değerlendir.
kapsamda: dış tarama (Anthropic skill docs/skill-creator bakım yüzü · prompt-regression/eval-drift araçları [promptfoo, braintrust, langsmith sınıfı] · "agent skill lifecycle" pratikleri) + her bulguya "bizim hangi parçanın üstüne oturur" satırı.
kapsam_disi: bakım sisteminin TASARIMI/kararı (G-1 Carvis + Salih masası) · antitez (S-1b'nin işi) · iç repo taraması (bilinenler verildi) · skill yazımı.
cikti: cc/rapor-2026-08-21-ab1-tez.md
done_yuklemi: rapor yazıldı ∧ ≥5 D/K etiketli dış bulgu ∧ her bulguda üstüne-oturma satırı ∧ F2 tablosu var
```

## S-1b — skill-bakım ANTİTEZ (AB-1)
```
gorev_adi: skill-bakim-antitez · rol: scout · rejim: maliyet-öncelikli · model: sonnet
kosum_profili: sonnet × low × ~10k bağlam × TAHMİN 2-4k çıktı · 8-15 araç · 3-5 dk (Carvis/Fable tahmini)
cagri_kosulu: m.40b hedefli refütasyon kolu — tezden BAĞIMSIZ koşar (tez raporunu OKUMA)
refutasyon_iddiasi (İDDİA verilir, GEREKÇE verilmez — m.40b): "Periyodik/takvimli skill-bakım turu GEREKSİZDİR: kullanım-anı sinyalleri (koşum sapması, eval FAIL, tetik ıskası) yeterlidir; takvimli bakım ölü-ağırlık (bakım tiyatrosu) üretir ve bakım maliyeti kazancı yer."
kapsamda: bu iddiayı DESTEKLEYEN dış kanıt ara (scheduled maintenance vs event-driven maintenance yazılım varlıklarında · test-suite çürümesi/bakım maliyeti bulguları · alarm-yorgunluğu/işe-yaramayan periyodik denetim emsalleri); bulamazsan "iddia dış kanıt bulamadı" de — bu da meşru sonuçtur.
kapsam_disi: tez tarafı savunusu · sentez/hakemlik (Carvis) · iç repo işleri.
cikti: cc/rapor-2026-08-21-ab1-antitez.md
done_yuklemi: rapor yazıldı ∧ iddia lehine bulgular D/K/X etiketli listelendi (0 bulgu da geçerli, açıkça beyan) ∧ F2 tablosu var
```

## S-2 — idempotens sistematik entegrasyonu (AB-2, İB-39; tek-şerit + antitez-borcu kayda)
```
gorev_adi: idempotens-entegrasyon-arastirmasi · rol: scout · rejim: maliyet-öncelikli · model: sonnet
kosum_profili: sonnet × medium × ~20k bağlam × TAHMİN 5-8k çıktı · 20-35 araç · 5-10 dk (Carvis/Fable tahmini)
cagri_kosulu: İB-39 araştırma koşumu (Salih 08-20 tetiği bu emirle çekildi)
KANONDA-BİLİNENLER: kavram ayrımı KANONDA — determinizm (aynı girdi→aynı çıktı) ≠ idempotens (f(f(x))=f(x), tekrar-uygulama güvenliği); Salih yön beyanı 08-20 "deterministik ∧ idempotent sistem". İç ön-iz: 07-26 U10/L17 Temporal kaynaklı; C7: IETF Idempotency-Key o gün ARANAMADI.
kapsamda: (1) İÇ ENVANTER — yalnız şu dosyalarda idempotent desen çıkar: tools/katman-hatti.py · veri/README.md (kayit_id_kume_sha) · tools/gece-senkron* (safe-fail) · tools/ambar-parquet* (temp→rename) · tools/hareket-tablo.py (çift-kayıt riski) · .claude/skills/damitma+seans-kapanis (tekrar-koşum güvenliği var mı). (2) DIŞ — IETF Idempotency-Key draft güncel durumu · veri-pipeline idempotency desenleri (dbt/Airflow/exactly-once vs at-least-once · upsert/MERGE · idempotency-key API pratiği). (3) BOŞLUK LİSTESİ: hangi Jarvis hattı tekrar-koşumda güvensiz + hangi dış desen kapatır (eşleme tablosu).
kapsam_disi: entegrasyon TASARIM KARARI (kanon-aday → m.40b antitez borcu Carvis kaydeder) · kod değişikliği · determinizm tarafı (ayrı kavram, karıştırma).
cikti: cc/rapor-2026-08-21-ab2-idempotens.md
done_yuklemi: rapor yazıldı ∧ iç envanter ≥6 dosya işlendi ∧ dış ≥4 D/K bulgu ∧ boşluk-eşleme tablosu var ∧ F2 tablosu var
```

## S-3 — usage-otomasyon yol seçimi (AB-3, İB-08; m.40 kısa dış araştırma)
```
gorev_adi: usage-otomasyon-kisa-atlas · rol: scout · rejim: maliyet-öncelikli · model: sonnet
kosum_profili: sonnet × low × ~10k bağlam × TAHMİN 2-4k çıktı · 10-20 araç · 3-6 dk (Carvis/Fable tahmini)
cagri_kosulu: İB-08 "İCRA (m.40 araştırma-önce)" şartını kapatan kısa atlas
KANONDA-BİLİNENLER: öneri (i) JSONL-parse — emsal tools/kosum-maliyeti.py + 08-02'de elle koşuldu (8 transkript, model+zaman çıkarıldı); transkriptler ~/.claude/projects/*/*.jsonl; KB-13(5) ve KB-27 bu karara bağlı.
kapsamda: üç yolun GÜNCEL durumu: (i) transkript-JSONL parse kırılganlığı (format değişim sıklığı/garanti var mı) · (ii) Claude Code OTLP/telemetri desteği (hangi metrikler resmi export'ta) · (iii) ccusage-sınıfı hazır araçlar (aktif mi, ne veriyor, model-düşümü tespiti var mı). Çıktı: 3-satırlık kıyas tablosu (kurulum maliyeti · veri zenginliği · kırılganlık · model-düşümü yakalar mı) + ÖNERİ satırı (hazırı-temel-al süzgeciyle).
kapsam_disi: betiğin yazımı (İB-08 icra ayağı, ayrı iş) · usage-panel UI · KB-27 tavan-rejimi tasarımı.
cikti: cc/rapor-2026-08-21-ab3-usage.md
done_yuklemi: rapor yazıldı ∧ 3 yol × 4 eksen tablosu dolu ∧ öneri satırı gerekçeli ∧ F2 tablosu var
```

## S-4a — V59 token-verim okuyucu ön-katmanı TEZ (AB-4; ATLAS-V59 devralındı: cc/gorev-2026-07-22-1.md §3)
```
gorev_adi: v59-okuyucu-onkatman-tez · rol: scout · rejim: maliyet-öncelikli · model: sonnet
kosum_profili: sonnet × medium × ~15k bağlam × TAHMİN 4-7k çıktı · 15-30 araç · 5-9 dk (Carvis/Fable tahmini)
cagri_kosulu: V59 "ucuz-okuyucu→damıtık-özet→pahalı-model" deseninin dış hammaddesi
KANONDA-BİLİNENLER: m.20 pointer ilkesi (özet+adres) + m.21 bağlam-detay ölçekleme ZATEN V59'un iç akrabası · heartbeat dersi "script toplar, LLM akıl yürütür" · m.46(c) rejim etiketi kanonda (Anthropic 15×-token/%90,2-kalite ↔ FrugalGPT %98-ucuzluk zıt hedefler — bu ikisini YENİDEN anlatma, üstüne koy).
kapsamda: reader-model / kademeli-okuma desenleri (ucuz-model ön-özetleyici · prompt/bağlam sıkıştırma [LLMLingua sınıfı] · retrieval-damıtma boru hatları · model-yönlendirme [RouteLLM sınıfı]) · KALİTE KAYBI ÖLÇÜMÜ yöntemleri (özet-sadakati/downstream-görev başarısı) · her desene "m.20/m.34 pointer sistemimizle bileşme noktası" satırı.
kapsam_disi: antitez (S-4b) · Jarvis'e kurulum kararı (G-1+masa) · ATLAS-A2/A3/A5 başlıkları (07-22 emrinin diğer atlasları — bu koşumun DIŞINDA).
cikti: cc/rapor-2026-08-21-ab4-tez.md
done_yuklemi: rapor yazıldı ∧ ≥5 D/K dış bulgu ∧ her desende bileşme satırı ∧ kalite-ölçüm bölümü var ∧ F2 tablosu var
```

## S-4b — V59 ANTİTEZ (AB-4)
```
gorev_adi: v59-okuyucu-onkatman-antitez · rol: scout · rejim: maliyet-öncelikli · model: sonnet
kosum_profili: sonnet × low × ~10k bağlam × TAHMİN 2-4k çıktı · 8-15 araç · 3-5 dk (Carvis/Fable tahmini)
cagri_kosulu: m.40b hedefli refütasyon — tezden bağımsız (tez raporunu OKUMA)
refutasyon_iddiasi (gerekçesiz): "Ön-okuyucu katmanının kalite kaybı token kazancını YER: ucuz-model özeti kritik ayrıntıyı düşürür, pahalı model eksik bağlamla daha çok tur atar; uçtan-uca maliyet ve hata birlikte artar."
kapsamda: iddia lehine dış kanıt (özetleme kayıp oranları · lost-in-the-middle/bilgi-düşümü çalışmaları · kademeli sistemlerde hata-ilerlemesi (error propagation) · cascade sistemlerde toplam-maliyet ters dönmesi emsalleri); bulamazsan açıkça beyan.
kapsam_disi: tez savunusu · sentez · Jarvis iç tasarımı.
cikti: cc/rapor-2026-08-21-ab4-antitez.md
done_yuklemi: rapor yazıldı ∧ iddia lehine bulgular D/K/X listelendi (0 da geçerli, açık beyan) ∧ F2 tablosu var
```

## S-5 — cascade-failure kaynak doğrulama (AB-5; rapor-2026-08-15-3.md:538 borcu)
```
gorev_adi: cascade-failure-kaynak-dogrulama · rol: scout · rejim: maliyet-öncelikli · model: haiku
kosum_profili: haiku × low × ~6k bağlam × TAHMİN 1-2k çıktı · 4-8 araç · 1-3 dk (Carvis/Fable tahmini)
cagri_kosulu: 08-15 raporunda D-6 satırı "yalnız başlık görüldü, okunmadı" — tekil kaynak doğrulama borcu
kapsamda: https://arxiv.org/abs/2605.17288 (∨ /html/2605.17288) AÇ ve OKU: (1) başlık/yazarlar/tarih künyesi doğru mu ("When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack" beklenen) · (2) ana bulgu 2-3 cümle Türkçe özet (kademeli LLM zincirinde düşmanca girdiyle kademe çöküşü İDDİASI makalede gerçekten var mı, hangi koşullarda, hangi ölçekte) · (3) D/K/X hükmü: "kapı sayısı arttıkça saldırı yüzeyi artar" çıkarımını destekliyor mu · (4) Jarvis kapı-zincirine (çelişki-kapısı→skill-kapısı→hakem zinciri) uygulanabilirlik 2 cümle.
kapsam_disi: geniş literatür taraması (TEK kaynak işi) · bedel-defteri kaydı (Carvis devir-notuna yazar) · savunma tasarımı.
cikti: cc/rapor-2026-08-21-ab5-cascade.md
done_yuklemi: rapor yazıldı ∧ künye D/K/X hükümlü ∧ özet + uygulanabilirlik bölümleri dolu ∧ URL erişilemezse FAIL-LOUD bayrak
```

---
## DİNAMİK EK (en sonda — cache)
- Tarih: 2026-08-21 akşam · Derleyen oturum: paralel s13 (Fable, ana-sıra) · Tetikleyen: Salih "sistemdeki araştırma borçlarını pipeline kur koş"
- Emir konumu: main · cc/gorev-2026-08-21-arastirma-borclari.md · derleme-anı HEAD: 146eab1
