# Halüsinasyon-Önleme Paketi v1 (hafıza) + Görev-Müsaitlik Derece Formülü · AKTİF: Salih emri 2026-08-15 (Hat-3)

*Salih emri: "AI halüsinasyonun önüne nasıl geçeriz — atlasları koş; sistemimiz için halüsinasyon-engelleyici PAKET (hafızada) + SKILL (görevlerde tetiklenebilir); görevin halüsinasyona müsaitliğini matematiksel-anlamlı DERECELENDİREN formül; derece > eşik → çıktı skill'le üretilir." Kanıt: `cc/rapor-2026-08-15-3.md` (m.40b tam şerit: 4 aile × tez→CoVe-Factored antitez→V26→maskeli hakem, 16 işçi; 30 SAĞLAM · 63 DARALDI · 0 DÜŞTÜ; V26 1 tutmuyor → antitez tarafı K). Skill: `.claude/skills/halusinasyon-engelleyici/` (+ `scripts/derece.py`). Graf (D2): `core/halusinasyon-paketi.d2` → `raporlar/2026-08-15-halusinasyon-paketi.svg`. Kardeşler: skill-üretim şeması K2 TOPRAKLAMA (artefakt kapısı) · tetiklenme şeması (çağrı kapısı) — bu paket GÖREV ÇIKTISI kapısıdır. **Dürüstlük damgası:** literatürde hazır çok-değişkenli halüsinasyon-risk formülü YOK; tüm değişkenler tek-değişkenli kanıttan; ağırlıklar küçük-veri rejiminde ÖĞRENİLMEZ, beyan edilir (kanıtsız-tercih); Claude güncel kuşak ve Türkçe sütunları BOŞ; her rakam (görev-tipi × ölçüt × kohort) damgalı, deneysel m.29.*

## 0. Beş ilke (kanıttan)
1. **Üretim hatası ≥ 2 × ayırt-etme hatası (Kalai 2025):** model "bu iddia geçerli mi"yi ayırt edemiyorsa hiçbir prompt freni işe yaramaz → fren = KAPI (dış sinyal), prompt değil; halüsinasyonun alt sınırı = tekil-geçen (singleton) olgu oranı → NADİRLİK doğrudan risk. İkili puanlama IDK'yı cezalandırır (9/10 benchmark) → model "sınav modunda"; jarvis puanlaması IDK=0, yanlış=−t/(1−t) (t=0,5/0,75/0,9 → ceza 1/2/9). [A-YT6, A2-1..4]
2. **Üç kutu, iki değil:** iddia = kaynakla ÇELİŞİR (intrinsic) · DAYANAKSIZ (extrinsic/baseless — "yanlış" DEĞİL, dışarıdan doğru olabilir) · DÜNYA-İLE-ÇELİŞİR (factuality) + talimat/lojik tutarsızlık. Doğrulama DESTEK arar (bu iddia hangi kaynak cümlesine dayanıyor?), çelişki-yokluğuyla yetinmez; RAG altında bile baskın hata dayanaksız EKLEME'dir. Jarvis eşleniği: K = dayanaksız/doğrulanamadı · X = çelişir · "bulunamadı"/[ARANAMADI] meşru. [A-YT1, A-YT2]
3. **Kaynak verildi ≠ risk sıfır:** RAG kohorta göre %9,8-52,4 yanıt-düzeyi halüsinasyon; ham/uzun metin retrieval'ı desteksiz iddiayı ARTIRABİLİR (8,7× tek çalışma [K]); >32K bağlam + örtüşmesiz hedefte geri-getirme %50 altı; zayıf getirimde soruların ~%10'unda aktif zarar → indirim sınırlı, yapılandırılmış+provenanslı kaynak şart. [B-YT1, B-YT2, C-YT7]
4. **Üretici ≠ doğrulayıcı; sözel güven kapı değil:** öz-tercih yanlılığı eşit-kaliteli çiftlerde de var (rubrik −%31,5 azaltır); atıf ≠ doğruluk (recall %73,6 ↔ doğruluk %40,4) → atıf-destek denetimi ayrı adım; sözel güven AUROC %62,7 (rastgele 50) → yalnız raporlama alanı; N-örnek uyuşma 3-5'te doyar. [B-YT4, B-YT5, D-YT7]
5. **Küçük-veri kilidi + eşik = beyan:** <100 görev / <50 olay → ağırlık VERİDEN ÖĞRENİLMEZ (10 olay/değişken); biçim TOPLAMSAL, tamsayı ağırlık, işaret beyanlı, "kanıtsız-tercih" damgalı; ∏ biçim GİRMEZ (doğrulayıcı hataları korelasyonlu); eşik seçilince ima edilen maliyet oranı t/(1−t) yazdırılır (ters yön yasak); fizibilite kapısı: görev-tipi taban riski μ > hedef α ise zorunlu çekimserlik payı ≥ (μ−α)/(1−α), sertifika vaat edilmez; oranlar n + Wilson/Jeffreys aralığıyla, çıplak yüzde yasak; eşik izleme nesnesi (karışım değişince yeniden ölçülür). [D-YT1..5, D-YT8]

## 1. Fren listesi (paket) — damga: ÖLÇÜLÜ / ÖLÇÜSÜZ / KAPSAM-DIŞI (API'de uygulanamaz)
| # | fren | ne zaman | etki (kohort-damgalı) | bedel | damga |
|---|---|---|---|---|---|
| F1 | **Destek-kontrolü** (her iddia → kaynak cümlesi; etiket: DESTEKLİ / DAYANAKSIZ / ÇELİŞİR / LOJİK-tutarsız) | kaynak/bağlam VERİLİ her görev | RAGTruth: baskın hata dayanaksız ekleme (2023 kohortu 6 model, ~18k yanıt) | 1 doğrulayıcı tur | ÖLÇÜLÜ |
| F2 | **Yapılandırılmış+provenanslı kaynak** (ham metin değil; alıntı-doğrulama) | kaynak toplarken | ham retrieval 8,7× artırabilir (tek çalışma) · zayıf getirim %10 aktif zarar | getirme maliyeti | ÖLÇÜLÜ [K] |
| F3 | **Üretici≠doğrulayıcı** (ayrı ajan/tur; CoVe-Factored: yalnız iddia) + çok-boyutlu rubrik + atıf-destek denetimi ayrı + atomik-olgu işaretleme | derece ≥ eşik | rubrik öz-tercih −%31,5 · CoVe halüsine varlık −%77 (bedel: doğru varlık −%36) | 2-5× çağrı; yanlış-negatif | ÖLÇÜLÜ |
| F4 | **N-örnek uyuşma** (3; sonlu-cevap/kısa-QA) | sonlu-cevaplı iddialar | SC +3,9..+17,9; 3-5'te doyar; tutarlı-yanılgıyı YAKALAMAZ | N çağrı | ÖLÇÜLÜ |
| F5 | **Hesap/sembolik → yürütücü**; kod → test/yürütme; dış-referans → registry (Hat-1 K2-R) | sayısal/kod/referans | PAL +15 puan; LATM 12/15 vs 3/15 | ~0 (script) | ÖLÇÜLÜ |
| F6 | **Çekimserlik ekonomisi**: IDK=0 · yanlış=−t/(1−t) · "bulunamadı"/[ARANAMADI]/DAYANAKSIZ etiketleri; öncül/cevaplanabilirlik denetimi (adım-0) | her görev; özellikle yanlış-öncül/eksik-belirtim | AbstentionBench: akıl-yürütme ince-ayarı çekimserliği −%24 → adım-0 atlanmaz | ~0 | ÖLÇÜLÜ (puanlama) / prompt-düzeyi "bilmiyorum izni" ÖLÇÜSÜZ |
| F7 | **Konum-ağırlıklı örneklem** (uzun çıktıda SON üçlük + TÜM sayısal iddialar; D2T'de ilk yarı) | uzun-form / sayısal | FActScore: hata sona doğru artar; NUM en yüksek tür (%36,2) | V26 revize 08-17 (Salih imzası A) | ÖLÇÜLÜ |
| F8 | **Çıktı şeması: gerekçe → cevap** sırası; şema istemde açık | yapısal çıktı | cevap-önce −25..−34 puan (tek çalışma, çıkar-sahibi) | ~0 | ÖLÇÜLÜ [K, deneysel] |
| F9 | **Model-damgası + runtime-modu** ayrı alan (thinking on/off · araç var/yok) | her kayıt | thinking-on araç-halüsinasyonu +1,3..+20,6 (Qwen3); Claude ölçülmemiş | ~0 | ÖLÇÜLÜ (Qwen) / Claude [?] |
| F10 | **Ölçü-disiplini**: oran = (görev-tipi × ölçüt × kohort) + n + Wilson/Jeffreys; sözel güven yalnız rapor alanı | her rapor | metrik farkı: FActScore %71,5 ↔ "%1,0 halüsinasyon" karşılaştırılamaz | ~0 | ÖLÇÜLÜ |
| — | Anthropic "reduce hallucinations" (bilmiyorum izni · alıntı-önce · CoT-doğrulama · best-of-N · bağlamla sınırla) | — | 0 rakam | — | **ÖLÇÜSÜZ** |
| — | DoLa/CAD/ITI/logit-erişimi · semantic entropy (5-10× hesap; uzun-formda bozulur; kısa-QA'da AUROC 0,79) · sıcaklık (fren değil; T=0 döngü riski) · eğitimli IDK (R-Tuning) | — | — | — | **KAPSAM-DIŞI** (API/model düzeyi) — SE kısa-QA'da opsiyonel ölçer |

**Ne-zaman-hangisi (kapı türü ↔ artefakt türü; ön-derece + post-hoc kapı birlikte):** kod → test/yürütme (post-hoc) · dış referans/paket/URL/DOI → registry/fetch (post-hoc, F5) · sayısal → hesap-devri (F5) + tümü doğrulama (F7) · olgu/liste → destek-kontrolü (F1) + F3 · sonlu-cevap → N-örnek (F4) · atıf/künye → tekil doğrulama ZORUNLU (F3+F5; oran model-damgalı %18-55 uydurma 2023) · çok-atlamalı → alt-soruya böl + her alt-cevap ayrı doğrulama · yanlış-öncül/cevaplanamaz → adım-0 çekimserlik (F6).

## 2. Görev-Müsaitlik Derece Formülü — `H(görev)` (toplamsal; tamsayı ağırlık; kanıtsız-tercih damgalı; deneysel m.29)
`H = Σ w_i · v_i` — her v_i boolean (0/1); ağırlıklar İŞARET + büyüklük beyanı (kaynak: tek-değişkenli kanıt; kalibrasyon: jarvis kaydı ≥50 olay sonrası).

| v | değişken (boolean) | w | kanıt (kohort-damgalı) |
|---|---|---|---|
| v1 | NADİRLİK: hedef varlık/konu uzun-kuyruk (arama 1-2 sonuç ≈ singleton bölgesi) | +2 | PopQA en nadir 4.000: %15-19, ölçek kurtarmaz; singleton alt-sınırı |
| v2 | TAZELİK: cevap ≤1 yılda değişir ∨ eğitim-kesimi sonrası | +3 | FreshQA: parametrik ölçekleme düz; yalnız arama düzeltir |
| v3a | ÇIKTI-TÜRÜ = atıf/künye/DOI/URL/kaynakça | +3 (**doğrudan eşik-üstü**) | 2023: %18-55 uydurma + gerçeklerin %24-43'ü hatalı |
| v3b | ÇIKTI-TÜRÜ = yapılandırılmış-veri → düzyazı (tablo/JSON/log'dan özet) | +2 | RAGTruth D2T 1,5-4,5× QA/özet; "eksik alan ≠ hayır" %17,7 |
| v3c | ÇIKTI-TÜRÜ = kod API/paket/araç adı ∨ prosedür adımları | +2 | paket-halüsinasyonu %4,6-19,7 (kohort); ToolBH |
| v3d | SAYISAL/TARİH iddiaları içerir | +1 | NUM %36,2 en yüksek tür (düşük ağırlık, ölçek küçük) |
| v4 | UZUNLUK: > ~10 atomik iddia ∨ >300 kelime | +1 | FActScore sona doğru bozulma (konum kuralı skill'de) |
| v5 | BİLEŞİKLİK: ≥3 atlamalı/adımlı akıl yürütme | +2 | ~%40 bileşiklik açığı; rejim-eşikli |
| v6 | ÖNCÜL/CEVAPLANABİLİRLİK şüphesi (yanlış-öncül, eksik-belirtim, cevaplanamaz olabilir) | +2 | AbstentionBench; ölçek yardım etmez |
| v7a | KAYNAK YOK (kapalı-kitap) | +2 | Kalai IIV; PopQA |
| v7b | kaynak var ama HAM/uzun (>32K ∨ örtüşmesiz) | +1 | NoLiMa 32K'da 11/13 model taban %50 altı |
| v7c | kaynak yapılandırılmış+provenanslı | −1 (indirim sınırlı) | RAG %9,8-52,4 kohort |
| v8 | DOĞRULAYICI/YÜRÜTÜCÜ VAR (test · yürütme · registry · hesap) | −2 | PAL +15; post-hoc kapı güçlü |
| v9 | RUNTIME: thinking-on ∧ araç-çağrısı görevi | +1 [?] | Qwen3 +1,3..+20,6; Claude ölçülmemiş |
| v10 | DİL: Türkçe/az-kaynaklı olgusal çıktı | +1 [?] | KÖR — kanıt yok, işaret pozitif varsayım (kanıtsız-tercih) |

**Eşik (beyan; ima edilen maliyet yazdırılır):**
- **τ_H = 7** normal görev → `H ≥ 7 ⇒ halusinasyon-engelleyici skill tetiklenir` (gerekçe: iki yüksek-ağırlıklı faktör (3+3) ya da üç orta (2+2+2+1); ima: skill bedeli ≈3-5× çağrı ↔ kaçırma bedeli = geri-alma; kanıtsız-tercih).
- **τ_H = 4** pahalı-geri-alma sınıfı (m.31: Katman-1 · dışarı çıkacak iş/publish · para · kişisel veri · kanon yazımı) → daha erken tetik (kaçırma yanlış-alarmdan ≥3× kötü beyanı).
- **Override:** v3a (atıf/künye) = 1 ⇒ skill zorunlu, H'den bağımsız.
- **H ≤ 3:** kanon frenleri (m.39 · D/K/X · bulunamadı) yeter; **4-6:** F1+F2 zorunlu (kaynak + destek-kontrolü), skill opsiyonel.
- **Fizibilite (sıfırıncı kapı):** görev-tipi taban riski μ (küçük-n Wilson) > hedef α ise zorunlu çekimserlik payı ≥ (μ−α)/(1−α); μ ≫ α (ör. açık-alan nadir olgu listesi) → "sertifika vaat edilmez": çıktı çekimserlik-etiketli ∨ insan-onayı kovası (Salih).
- **İzleme:** her koşum `kuyruk/halusinasyon-kayit.md`'ye satır (görev · v-vektörü · H · tetiklendi mi · yakalanan DAYANAKSIZ/ÇELİŞİR sayısı · n); ≥50 olayda ağırlık/eşik yeniden (10 olay/değişken); görev-karışımı değişince eşik yeniden ölçülür (statik eşik kayma altında %71 ihlal — tek kaynak [K]).

Deterministik hesap: `python3 .claude/skills/halusinasyon-engelleyici/scripts/derece.py --v1 --v2 ...` → H + eşik + tetik + ima edilen maliyet beyanı.

## 3. m.16 taraması + şerh-adayları
- Kanon frenleriyle ÇELİŞKİ YOK; paket onları teorik dayanağa bağlar (Kalai: IDK cezası → "bulunamadı" meşru; fren=kapı) ve 5 yeni fren ekler (F1 destek-kontrolü etiketi · F6 puanlama · F7 konum-ağırlıklı örneklem · F8 şema sırası · fizibilite kapısı).
- **V26 revizyonu — İMZALANDI (Salih Katman-1, 2026-08-17, seçenek A):** örneklem "rastgele" yerine KURAL-TABANLI: çıktının son üçte biri + tüm sayısal iddialar (FActScore konum bulgusu; deterministik tasarım ilkesi). Uygulama: `.claude/skills/atlas-kosum/SKILL.md` adım 5. Bilinen açık: işçi kuralı öğrenirse son üçlüğe özenip başı gevşetebilir — ölçüm ilerde (deneysel m.29).
- **md.21 derece-sorma yasağı şerhi:** erken çekimserlik ortalamada kazanç ama taban doğruluk yüksekken net zarar (TriviaQA) → yasak koşulsuz değil; kural: yüksek-taban görevde önce üret, sonra doğrula.
- **Kör noktalar (ölçüm borcu):** Claude güncel kuşak oranları · Türkçe · ajan/araç-çağrısı görevleri · prompt-düzeyi "bilmiyorum" etkisi · C_hata elicitation · Aile-D omurgasının tek 2026 ön-baskısına yaslanması (Kotte).
