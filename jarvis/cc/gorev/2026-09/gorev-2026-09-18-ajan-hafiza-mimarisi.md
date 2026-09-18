# Görev emri — kalıcı ajanların gelişen hafıza mimarisi (zincir 2/2, Karar 102, 2026-09-18)

*Derleyen: Jarvis (Fable ana-sıra), S-K v1; iskelet `../../../sablonlar/gorev-fonksiyonu.md`. Zincir 1/2 = perspektif partisyonu (hakem raporu §ii: kalıcı ajan = kalıcı dizin; süreç kalıcılığı yok). Koşum `atlas-kosum` v0.2. Ham raporlar `cc/rapor/2026-09/rapor-2026-09-18-hafiza-*.md`; teslim `raporlar/2026-09/2026-09-18-ajan-hafiza-mimarisi.md`.*

```
## KİMLİK
gorev_adi:        ajan-hafiza-mimarisi-dis-tarama
rol:              lider (Opus 5 medium) → tez/antitez işçileri (Sonnet) → maskeli hakem (Opus 5 medium)
cagri_kosulu:     Salih 09-18 16:5x: "jarvis gibi ajanların kendi gelişen hafıza mimarilerinin olmasını nasıl tasarlayacağız bunu da araştırmalıyız"; Karar 102 literatür-önce
rejim:            kalite-öncelikli (kanon tasarım girdisi)
model:            işçi Sonnet 5 · lider/hakem Opus 5 medium (Karar 89); Fable koşmaz
kosum_profili:    aile 3 · tez 3 + antitez 3 + V26 denetçi 1 + hakem 1 = 8 ajan · tahmin: alt-ajan toplam 600-900k token [?], 25-35 dk [?] (zincir 1/2 gerçekleşen: 10 ajan ≈864k · ≈32 dk)

## GİRDİLER
arastirma_sorusu: metin — "Kalıcı bir ajanın (kendi dizini, kanonu, oturumu olan; ör. Jarvis, Friday) hafızası nasıl GELİŞİR? Sektör öncülleri ve 2025-2026 literatürü ajan hafızasını hangi katmanlara ayırıyor (çalışma/oturum · epizodik · semantik/çekirdek · prosedürel/skill), hangi yazma-okuma disipliniyle büyütüyor (ne zaman yazılır, kim yazar, nasıl damıtılır/sıkıştırılır, ne zaman arşive iner), 'kendini geliştiren' hafıza (yansıma, ders çıkarma, kural adayı) hangi mekanizmayla ve hangi frenle kuruluyor; çok-ajanlı sistemde ajan başına hafıza izolasyonu ile paylaşılan bilgi nasıl ayrılıyor; her bulgu model sürümü + tarih + kullanım biçimi damgalı."
mevcut_duzen:     metin (eager, ≤1 KB) — Jarvis/Friday hafıza mimarisi: kapsül (sıcak, FIFO 8 madde → arşiv) · pano (kart) · karar defteri (hüküm kaydı) · fikir kutusu · çekirdek desenler (Friday: 10 koşumda yeniden-oluşum; ekleme Salih kabulüyle) · bronz kütükler (hareket, prompt, talimat-yükleme) → silver sqlite → gold görünümler · wiki · arşiv (silme yasağı) · harness hafızası (`~/.claude/projects/<proje>/memory/`, MEMORY.md indeks) · skill'ler (koşullu bilgi). Kural: kanon yalnız Salih imzasıyla; ajan hafızaya yazar, kurala yazamaz (m.42 d).
ajan_sinifi:      dosya (lazy) — `cc/rapor/2026-09/rapor-2026-09-18-perspektif-hakem.md` §ii: alt-ajan = izole bağlam + tek dönüş; kalıcı ajan = kalıcı dizin (memory alanı, MEMORY.md ≤200 satır/25 KB sistem promptuna)

## BAĞLAM-MANİFESTİ
eager:            arastirma_sorusu · mevcut_duzen · kanonda-bilinenler
lazy:             ajan_sinifi (hakem §ii; yalnız çelişki çıkarsa)
butce:            işçi ≤40k · dönüş ≤2k · toplam ≤120k [?]

## SINIRLAR
kapsamda:         (1) hafıza katman taksonomisi (kim hangi katmanları ayırıyor; harness-düzeyi özellikler: Claude Code memory/agent-memory, OpenAI Agents SDK, Google ADK, LangGraph/LangMem, Mem0, Letta/MemGPT sınıfı) · (2) büyüme disiplini: yazma tetiği, yazar (ajan/insan/hakem), damıtma-sıkıştırma (özetleme, FIFO, çekirdek yeniden-oluşum, bütçe), arşiv/unutma, çelişki çözümü · (3) kendini-geliştiren hafıza: yansıma (Reflexion sınıfı), ders çıkarma, kural adayı → insan onayı frenleri, ölçülmüş getiri (n, benchmark, model) · (4) çok-ajanlı izolasyon vs paylaşım (ajan başına dizin, ortak bilgi, sızıntı frenleri) · (5) mevcut düzene uygulanmış "korunmalı / eklenmeli / değişmeli / belirsiz" hükmü, her hüküm ≥2 bağımsız güncel-kuşak kaynak ya da "belirsiz → iç ölçüm"
kapsam_disi:      kanon yazımı (Jarvis, masa sonrası) · vektör DB ürün kıyası (İB-47 ayrı) · RAG genel · staj/galeri (md.49) · iç kütük sayımı (Karar 102 (2), ikinci aşama)
araclar:          WebSearch · WebFetch (işçi başına ≥2 birincil kaynak açılır) · Read (yalnız eager/lazy) · Write (yalnız kendi rapor yolu)
degismezler:      URL zorunlu · rakam kaynaklı, kestirim `[?]` · uydurma yasak, "bulunamadı" meşru · 403/paywall bayrak · AS-OF damgasız iddia yok · model-sürümü damgasız bulgu hakemde düşer (eski kuşak = "o zaman böyle") · kanonda-bilinenler verili

## DALLAR (dal+koşul ≤5)
D1: eğer bir mekanizma için ≥2 bağımsız güncel-kuşak kaynak varsa → hüküm (korunmalı/eklenmeli/değişmeli) + gerekçe + AS-OF
D2: eğer kaynaklar çelişiyor ∨ yalnız eski kuşak → BELİRSİZ + iç ölçüm büyüklüğü
D3: eğer öncül bir mekanizmayı açıkça reddediyor/geri alıyorsa → RET kaydı (kim, neden, tarih, model)
D-KATMAN1: bulgu m.42 d ("ajan kural yazamaz") ya da m.8 (silme yasağı) ile çelişirse → hakem raporunda m.16 bölümü; karar Salih'te

## ÇIKTI SÖZLEŞMESİ
halusinasyon_derecesi: H = 8 (v2 +3 · v3a +3 OVERRIDE · v5 +2 · v7a +2 · v8 −2) → halusinasyon-engelleyici hakem aşamasında (her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR)
cikti_bicimi:     aile başına tez + antitez (≤2k dönüş) · V26 denetim · hakem: (i) katman × mekanizma × hüküm × kaynak × AS-OF × kuşak tablosu · (ii) mevcut düzen eşlemesi (kapsül/pano/defter/kutu/çekirdek/kütük/harness-memory/skill ↔ literatür karşılığı; korunmalı/eklenmeli/değişmeli/belirsiz) · (iii) kendini-geliştiren hafıza frenleri (insan onayı, ölçüm) · (iv) RET listesi · (v) hayatta kalma · (vi) iç ölçüme kalanlar · (vii) m.16 · (viii) masa kalemi taslağı (seçenekli, öneri ilk)
done_yuklemi:     hakem tablosunda ≥4 katman için hüküm satırı VAR ∧ mevcut düzenin 8 bileşeni eşlendi ∧ her "eklenmeli/değişmeli" satırı ≥2 URL + AS-OF + model ∧ damgasız iddia = 0 ∧ işçi başına açılan birincil kaynak ≥2
done_olcumu:      DRFR — 5 koşul tek tek
yeniden_deneme:   3

## SKILL TETİKLERİ
- skill:              atlas-kosum
  tetik_kosulu:       emir teslim edildi ∧ K2 "koşmuş-aday" DEĞİL; K2 koşmuş-aday ise ÇAĞIRMA (devral)
  cagri_kipi:         literal (Jarvis başlatır)
  girdi:              arastirma_sorusu · aileler: A) harness/ürün hafıza özellikleri ve öncül mühendislik yazıları (Anthropic memory/agent-memory belgeleri, OpenAI/Google SDK, Letta/MemGPT, Mem0, LangMem) · B) akademik hafıza taksonomileri ve kendini-geliştiren ajan literatürü 2025-2026 (agent memory survey, Reflexion/Voyager sınıfı, experience/lesson distillation, memory consolidation/forgetting) · C) pratisyen kişisel-ajan hafıza pratikleri (Kun Chen "correct → remember" deseni, CLAUDE.md/AGENTS.md büyütme disiplini, skill'e taşıma, çok-ajan izolasyonu)
  baglam:             hedef = hakem tablosu (i)-(ii); format md tablo + URL; sınır = kapsam_disi; işçi bağlamı geçmişsiz
  yan_etki_damgasi:   salt-okur × idempotent:h × dış-dünya:h
  done_yuklemi:       yukarıdaki
  hata_yolu:          işçi dönüşü şema dışı → lider düzeltir · erişim engeli → bayrak · retry ≤3 · FAIL-LOUD
  sira:               1/2
  kayit:              execute_tool · tool.name=atlas-kosum · agent · error.type · model+sürüm · tarih
- skill:              halusinasyon-engelleyici
  tetik_kosulu:       H = 8 ≥ 7 ∧ atıf/URL çıktısı; tez/antitez aşamasında ÇAĞIRMA (yalnız hakem)
  cagri_kipi:         ortuk
  girdi:              tez+antitez raporları · V26 denetim
  baglam:             her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR; damgasız → DAYANAKSIZ
  yan_etki_damgasi:   salt-okur × idempotent:e × dış-dünya:h
  done_yuklemi:       etiketsiz iddia = 0
  hata_yolu:          etiketlenemeyen → BELİRSİZ · sözleşme-ihlali → hakem düzeltir · retry ≤3 · FAIL-LOUD
  sira:               2/2
  kayit:              aynı

## KANONDA-BİLİNENLER
- Jarvis = Salih'le konuşan ana-sıra ajan; tarihli metinlerdeki "Carvis" = Jarvis; sistem/repo = depo/kanon (Karar 93 EK).
- Zincir 1/2 (09-18): kalıcı ajan = kalıcı dizin; MEMORY.md ≤200 satır/25 KB sistem promptuna; süreç kalıcılığı yok (D). Alt-ajan hafızasız, tek dönüş.
- Kun Chen (transkript 08-03): global md 27 satır minimal (her oturuma yüklenir); proje md = "yanlışı gördüğümde düzelt ve hatırla" ile büyür; koşullu bilgi md'den skill'e taşınır. Verili.
- Kanon: kapsül FIFO 8 madde (İB-80); Friday çekirdek 10 koşumda yeniden-oluşum; m.42 d ajan kural yazamaz; m.8 silme yasağı (arşiv); harness memory dizini proje anahtarına bağlı (F2'de kopyalandı).
- Geçmiş yörünge: İB-75 S6 (09-09) hafıza lehine +%8,3/+%4,6 birincil kaynak (Karar 91); yeniden taranmaz, üstüne konur.
- Karar 102: literatür-önce; model-sürümü damgası zorunlu.

## DİNAMİK EK
tarih: 2026-09-18 ~18:1x · HEAD b4773d6 · tetikleyen: Salih 16:5x beyanı (defter Karar 102 EK) · zaman-zemini Karar 68 (bugün 2026-09-18; güncel kuşak = 2025-Q3 sonrası ∧ 4.x+/5)
```
