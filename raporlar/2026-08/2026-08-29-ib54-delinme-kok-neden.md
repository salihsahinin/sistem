# İB-54 (1) — İki fren-delinme vakasının kök-neden analizi

**AS-OF 2026-08-29 · yan icra oturumu (Fable) · Karar 74 M-4 (d) → İB-54 adım (1) · Karar 39 sırası: "önce delinmeler neden yaşanmış onu tespit etmemiz lazım… nedenini tespit ettikten sonra freni değiştiririz" (Salih, 08-20)**

*Ne bu:* 2026-08-01'de prompt-metnine yazılmış maliyet/çağrı frenlerinin delindiği iki koşumun, kayıtlı ölçümlerden çıkarılan kök-neden dökümü. Karar VERMEZ; İB-54 (2) fren tasarımının ve (3) rejim-etiketi satırının girdisidir. Her rakam kaynaklı; transkriptler bu Mac'te yok (Windows dönemi, `arsiv/claude-izler` gitignore'lu) → analiz koşumların KENDİ ölçüm beyanlarına dayanır (kosum-maliyeti.py v0, üç bilinen kusurla şerhli: dedup yok · iç-içe alt-ajan kaçağı · web-arama sayılmaz — rakamlar bilinen yönde ŞİŞİK/EKSİK, oranlar karşılaştırılabilir).

## 1. Vaka kimlikleri (Karar 39'daki "ikinci vaka kimliği analizde netleşecek" → netleşti)

| Vaka | Koşum | Fren (emirde) | Ölçülen | Aşım | Kaynak |
|---|---|---|---|---|---|
| **V-1** | [cc/rapor-2026-08-01-4.md](../cc/rapor-2026-08-01-4.md) (m.40b antitezi; sid `7c159f0c`) | "08-01-2 bandı referans: $16,34'ten KÜÇÜK olmalı" + alt-ajan başına **≤30 çağrı** | **$30,94** · 15,5 dk · Opus $21,14 (70 çağrı, ana döngü) + Sonnet $9,80 (277 çağrı, 4 alt-ajan) | **1,89×**; 4 ajandan 2'si çağrı tavanını aştı (**46** ve **~48-60** ↔ ≤30) | rapor-4 §7 ([cc/rapor-2026-08-01-4.md:205-236](../cc/rapor-2026-08-01-4.md)), emir [cc/gorev-2026-08-01-4.md:21](../cc/gorev-2026-08-01-4.md) |
| **V-2** | [cc/rapor-2026-08-01-6.md](../cc/rapor-2026-08-01-6.md) (İNSAN son-10 derlemesi) | tavan **$8**, durma çizgisi **$6,50**, alt-ajan çağrı tavanı **12** | **$19,32** (ilk ara ölçüm $12,69) · 7 alt-ajan tek turda | **2,4×** (ara ölçümde zaten 1,59×) | rapor-6 §uyum-1 ([cc/rapor-2026-08-01-6.md:27](../cc/rapor-2026-08-01-6.md)), emir [cc/gorev-2026-08-01-6.md:31](../cc/gorev-2026-08-01-6.md), okuma dosyası [raporlar/2026-08-01-INSAN-son-10-rapor.md:5](../raporlar/2026-08-01-INSAN-son-10-rapor.md) |

Bağlam: aynı hafta 07-30 serisinde $14 tavanı 4 kez ihlal edilmişti (rapor-8 2,08× · rapor-10 1,34× · rapor-13 1,22× · rapor-18 ≈8×; 3'ünde kalite kırpıldı) — [kuyruk/gelen-2026-08-01-tavan-rejim-karari.md:8](../kuyruk/gelen-2026-08-01-tavan-rejim-karari.md) [D, 13 koşumun kapanış beyanlarından hasat]. Yani delinme iki vaka değil bir SINIF; V-1/V-2 sınıfın ölçümü en ayrıntılı iki üyesi.

## 2. Vaka anatomisi

### V-1 (08-01-4): $30,94 — iki bağımsız mekanizma, ikisi de ölçülü
1. **Ana döngü $21,14 = %68.** 13,9M cache-oku / 70 çağrı ⇒ çağrı başına ~199K bağlam. Tek tetik: `claude-api` skill'i fiyat doğrulaması için çağrıldı (m.39 gereği doğru karar), skill belgesi bağlama yüklendi ve **sonraki her turda cache-oku olarak yeniden faturalandı**. Skill maliyeti = belge boyutu × KALAN TUR SAYISI (çağrı anında değil). Emirde bu sınıfa dair fren YOK (fren $ toplamı ve ajan çağrısı üstündeydi).
2. **Alt-ajanlar $9,80 (%32).** 2/4 ajan ≤30 çağrı tavanını aştı (46; 48-60). İkisi de aşımı kendiliğinden bayrakladı — istenen davranış — ama "tavan yalnız prompt metnindeydi; hiçbir mekanizma onu uygulamıyordu" (rapor-4 §7-2). Sonnet pini çalıştı (aynı hacim Opus'ta ~3×); pay %15,4→%31,7 çıkışı kademeden değil, ajan sayısının 2→4 ve tavan ihlalinden (rapor-4 §7-3 tablosu).
3. **Referans bandı kendisi eksik ölçümdü:** $16,34 rapor yazımı bitmeden alınmıştı (rapor-2 §12: "eksiktir"); $30,94 de öyle. İki eksik ölçümün oranı — 1,89× — karşılaştırılabilir ama mutlak değerler şerhli.

### V-2 (08-01-6): $19,32 — fren birimi ölçülemez, taahhüt atomik
1. **7 alt-ajan tek turda başlatıldı** → harcamanın büyük kısmı ilk ölçüm anından ÖNCE bitmişti (rapor-6 §uyum-1 (ii)).
2. **Fren $ cinsindendi; koşum içinde $ ölçümü yalnız ayrı betikle mümkün** ve emir bunu adım olarak yazmıyordu (§uyum-1 (i)). İlk ölçüm alt-ajanların çoğu bittikten sonra alındı: $12,69 (zaten tavan üstü) → o noktadan sonra yeni ajan çağrılmadı, teslim ana döngüde bitti → $19,32.
3. Alt-ajan başına 12-çağrı tavanına uyulup uyulmadığı raporda YOK [?] — ölçülmedi.
4. Emrin kendi şerhi ("bu fren henüz prompt-düzeyinde") koşumda doğrulandı; rapor-6 bunu "üçüncü kanıt" diye kaydetti.

## 3. Kök nedenler (sınıflandırma; her biri iki vakadan en az birinde ölçülü)

| # | Kök neden | V-1 | V-2 | Kanıt | Fren tasarımına çıkarım (İB-54 (2) girdisi — KARAR DEĞİL) |
|---|---|---|---|---|---|
| **KN-1** | **Fren = metin, yaptırım = yok.** Tavan prompt'ta yazılı; okuyan ajan aşımı bayraklıyor ama durmuyor. "Yazılmış ama çağrılmayan fren yok hükmündedir" (30-16 hükmü, Karar 39 "[K] fren değil etiket"). | ✓ (2 ajan) | ✓ ($8) | rapor-4 §7-2 · rapor-6 §uyum-1 | Fren KOŞUM KATMANINDA olmalı: sayaç + fiziki durdurma (Workflow `budget` gibi — `agent()` fırlatır; Agent-tool fan-out'unda PreToolUse sayaç-hook'u). |
| **KN-2** | **Ölçüm anı ≠ taahhüt anı.** Maliyet, harcandıktan sonra ölçülüyor; fan-out başlarken kestirim/kapı yok. | ✓ (rapor sonrası ölçüm) | ✓ (7 ajan paralel → ölçüm geç) | rapor-6 §uyum-1 (ii) · rapor-4 "rapor yazılmadan alındı" | Kapı taahhüt anında: fan-out genişliği × ajan-başına bütçe ≤ tavan (öneri B: "fan-out ÖNCESİ kestirim kapısı", `gelen-…tavan-rejim-karari.md:17`). |
| **KN-3** | **Ölçekleme değişkeni yanlış modellendi.** Fren $ ve ajan SAYISI üstünde; gerçek sürücü **çağrı sayısı × bağlam** (skill-belge cache-oku çarpanı: belge × kalan tur). Ana döngü %68'i tek skill yüklemesinden. | ✓ (%68) | — | rapor-4 §7-1 · rapor-18 KL18-2 ("9-ajanlı derin koşum ≈ $100 sınıfı") | Fren birimi $ değil, koşum içinde GÖZLENEBİLİR sayaç: ajan-başına araç çağrısı + bağlam/tur (bugün ambar `amb_olgu_kosum.arac_cagrisi` bunu ölçüyor). Skill yüklemesi bağlam-sayacı kapsamına girer (08-01-2 Yol-1). |
| **KN-4** | **Paralel fan-out atomik.** N ajan tek turda → ajan-başına kapı yok, toplam tek seferde taahhüt ediliyor. | ✓ (4) | ✓ (7) | rapor-4 §7-3 · rapor-6 §uyum-1 | Tek-dalga kuralı + genişlik tavanı (öneri B) · fan-out sonrası ara ölçüm zorunlu adım (emirde yazılı değildi). |
| **KN-5** | **$ birimi koşum içinde ölçülemez;** ölçüm ayrı betik + 3 kusur (dedup, iç-içe ajan, web-arama). Fren birimi olarak $ seçmek freni fiilen çalıştırılamaz kıldı. | ✓ | ✓ | [raporlar/usage/kosum-maliyeti.py](../raporlar/usage/kosum-maliyeti.py) docstring · iz-hasadı `maliyet_serh` | Fren birimi = araç çağrısı / token (deterministik, anlık); $ yalnız raporlama. |
| KN-6 (katkı) | Referans bandı ve tavan KESTİRİMDİ, ölçülmüş sınıf-medyanı değil ($16,34 eksik ölçüm; $8 keyfi; $14 keyfi). Tavan keyfi olunca "aşım" da kalite kırpmaya dönüşüyor (07-30 serisinde 3 koşum). | ✓ | ✓ | rapor-2 §12 · gelen:8 · rapor-10 K1 ("m.40b tam-kontrat ≈ $30+, $14'e sığmıyor") | Öneri A: tavan(sınıf) = ölçülen medyan(sınıf) × ~3 (anomali eşiği); uç-eşikli (Karar 39: "fren tetiklenme koşulu zor olsun"). Medyan artık ölçülü (§4). |

Ortak payda: **beş kök nedenin hiçbiri "ajan çok harcadı" değil; hepsi FRENİN KENDİ TASARIMI** (yer: metin · an: sonra · birim: $ · değişken: ajan sayısı · taahhüt: atomik). Ajanlar iki vakada da aşımı dürüstçe raporladı — davranış sorunu yok, mekanizma yok.

## 4. Bugünkü taban (AS-OF 2026-08-29, silver `amb_olgu_kosum` @ HEAD e9c0e8a; deterministik sayım)

- 401 ajan koşumu · 29 workflow · 2026-08-13 → 2026-08-29.
- **Ajan başına araç çağrısı: p50 18 · p75 27 · p90 44 · p95 54 · max 115.** >30 olan 90 (%22,4) · >60 olan 14 · >90 olan 2. (08-01'deki "≤30" tavanı bugünkü dağılımda p80 civarı — uç değil, rutin aşılır; Karar 39'un "zor tetiklensin" şartına uymaz.)
- Rol kırılımı: Atlas ANTİTEZ n=92 p50 22 p90 45 max 54 · Atlas TEZ n=80 p50 24 p90 43 max 49 · MASKELİ HAKEM n=75 p50 6 p90 10 max 14 · rolsüz (`?`) n=78 p50 32 p90 70 **max 115** · V26 örneklem-denetçisi n=22 p50 15-17 max 26.
- Workflow toplam çağrı: p50 189 · p90 376 · max 376 wf'li (ajan/wf p50 12, **max 23**; wf_id'siz 79 ajanlık grup ayrı sayılır — ilk yazımda 79/2.914 o gruptu, 08-29 P1 düzeltmesi).
- Çıktı token/ajan: p50 17.866 · p90 48.483 · max 113.621.
- Mevcut deterministik frenler: PreToolUse teli (core/ yazımı) · permissions.ask (screencapture/rec/sox, Karar 70) · Workflow `budget` (yalnız prompt'ta "+Nk" verilirse; aşımda `agent()` fırlatır — KN-1'in tam karşılığı ama OPT-IN) · işçi bütçesi 10-15 / effort düşük-orta (08-15 ekonomi rejimi; prompt-düzeyi, yaptırımsız). Ajan-başına çağrı kapısı: YOK.

## 5. (2) ve (3) için teslim (bu raporun çıktısı; karar Salih'in / ana-sıranın)

**(2) Uç-eşikli sınıf-bazlı fren — tasarım girdisi (Karar 39: A uç-eşikli + B mekanik):**
- Birim: araç çağrısı (ajan-başına) + ajan sayısı (wf-başına) + Workflow `budget` (çıktı token). $ yok.
- Uç eşik (medyan × 3, Öneri A formu, ölçülü tabandan): ajan-başına **≈ 54 çağrı** (p50 18 × 3 = 54 = p95; rol-bazlı: Atlas TEZ/ANTİTEZ ≈ 66-72, HAKEM ≈ 18-20, rolsüz ≈ 96) · wf-başına toplam **≈ 570 çağrı** (p50 189 × 3; bugüne dek yalnız 1 wf aşmış: 2.914) · ajan/wf **≈ 36** (p50 12 × 3; gözlenen max 23). Eşikler m.29 deneysel; 2 delinme vakası bu eşiklerle: V-1 ajanları (46, 48-60) rol-bazlı Atlas eşiğinin ALTINDA kalırdı (kalite kırpılmazdı), V-2 (7 ajan tek dalga) ajan/wf eşiğini geçmezdi — yani uç-eşik iki vakayı da DURDURMAZDI; durduracağı şey rolsüz 115-çağrılık ve 2.914-çağrılık koşum sınıfı (KN-4/KN-3'ün bugünkü örnekleri). Bu, Salih'in "kaliteyi kısmak istemeyiz, uç senaryolar için çalışsın" hükmüyle tutarlı.
- Yer: (a) Workflow script'lerinde `budget` + `agent()` sayacı (zaten deterministik; varsayılan bütçe yoksa `budget.total=null` → fren yok ⇒ script şablonuna varsayılan tavan satırı) · (b) Agent-tool fan-out'u için PreToolUse hook'u: oturum-başı sayaç dosyası (Agent/Task çağrısı sayısı; eşik üstünde `deny` + gerekçe) · (c) ajan-içi çağrı sayacı: Stop/SubagentStop hook'u ölçer, [veri/bronz/kosum-olay.jsonl](../veri/bronz/kosum-olay.jsonl)'e yazar (ambar zaten okuyor) — eşik aşımında durdurma değil BAYRAK (kalite korunur, kayıt düşer).
- Ölçüm-anı kuralı: fan-out ÖNCESİ "genişlik × ajan-bütçesi ≤ tavan" satırı emir şablonuna (gorev-emri-derleme) — taahhüt-anı kapısı.

**(3) Rejim-etiketi satırı (m.46(d) Karar 39'la imzalı; ilk örnek 08-15 ekonomi rejimi) — taslak, Katman-1 yazım ana-sıra/Salih:**
> `[rejim: manuel-tempo · kota-bol · ekonomi −%30 (Salih 08-15) · AS-OF 2026-08-29]` — işçi-ajan bütçesi 10-15 · effort düşük-orta · aile ≤3 · devam-script. Bu satırla kalibre edilen her tavan (İB-54 (2) eşikleri dahil) rejim değişiminde (K-009/K-010 otomasyon geçişi) OTOMATİK yeniden açılır, taşınmaz.

## 6. Ne değişti / ne değişmedi
- Değişen: İB-54 (1) KAPANDI — iki vaka kimlikli, 5+1 kök neden ölçülü, bugünkü taban sayılı, (2)/(3) girdileri yazılı.
- Değişmeyen: fren kodu YAZILMADI (adım 2, ayrı dilim); tüzük/KILAVUZ'a satır GİRMEDİ (Katman-1); eşik rakamları KARAR değil ölçüm-temelli öneri (m.29).
- Yeniden açma koşulu: transkript arşivi Mac'e taşınırsa V-1/V-2 kosum-maliyeti.py ile dedup'lu yeniden ölçülür (mutlak $ düzelir; oranlar değişmez beklentisi [?]).
