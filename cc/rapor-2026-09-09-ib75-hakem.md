# IB-75 — Bağımsız hakem raporu (2026-09-09)

Hakem: bağımsız, maskeli (iddiaların kaynağı/sırası bilinmiyor). Ölçüt: kanıt gücü + kaynağa inerek doğrulama.
Araç bütçesi: 10 çağrı (WebFetch/WebSearch). AS-OF 2026-09-09.

## Bölüm 1 — Çift hükümleri

| Çift | P hükmü | Q hükmü | Gerekçe (tek cümle) |
|---|---|---|---|
| Ç1 | **P DARALDI** | **Q SAĞLAM** | Docs yalnız "statik tanım dosyası MÜMKÜNDÜR" der, "yeterlidir / öğrenene gerek yok" normatif kısmı kaynakta yok; Q'nun +%8,3 / +%4,6 sayıları kaynakta birebir DOĞRULANDI. |
| Ç2 | **P DARALDI** | **Q DARALDI** | P'nin `description` alanı belgede rota-ipucu olarak gerçekten var ama "güvenilir" nitelemesi belgede yok; Q'nun çarpımsal bozulma mantığı geçerli, ancak %95 taban oranı örnek bir varsayım — kaynağa inilmedi, `[?]`. |
| Ç3 | **P SAĞLAM** (olgu) / **DARALDI** (norm) | **Q DARALDI** | Alt-ajanın taze bağlamla başlaması belgelenmiş olgu; "bu tasarım tercih edilir" normatif ek desteksiz. Q'nun tam-iz tezi tek blog + tek vaka (Flappy Bird) — hakemli ölçüm değil, mekanizma savı. |
| Ç4 | **P DARALDI** | **Q SAĞLAM** | Context-editing belgesi mekanizmayı ve token tasarrufunu belgeler, "uzun koşumda KALİTEYİ KORUR" iddiasını ölçmez; Q'nun %39 + "kayıp esas olarak güvenilmezlik artışından" ayrımı arXiv 2505.06120 özetinde birebir var. |
| Ç5 | **P DARALDI** | **Q DARALDI** | Sayısal kısım (100.000 token tetik, keep=3) DOĞRULANDI ama bunlar VARSAYILAN değerdir, "doğru tasarım" hükmü kaynakta yok; Q'nun "en kötü anda keser" savı blog düzeyinde, ölçüm yok (arxiv 2606.23525 kontrol edilmedi, `[?]`). |
| Ç6 | **P DÜŞTÜ** | **Q SAĞLAM** | "Serbest metin özet yeterlidir" belgede hiçbir yerde iddia edilmez ve Q'nun karşı-kanıtı ölçülüdür: 824 log üzerinde dört arıza sınıfı yüzdeleriyle DOĞRULANDI; `applied_edits` yapılandırılmış dönüş alanı da doğrulandı (ama devir-özeti şeması değil, context-editing telemetrisidir → Q'nun bu ikinci dayanağı ZAYIF/yanlış-eşleşme). |
| Ç7 | **P DÜŞTÜ** | **Q SAĞLAM** | "Etkili biçimde sınırlar" iddiası, aynı korumaların pratikte atlatıldığını gösteren Trail of Bits bulgusuyla çürüdü: üç popüler ajan platformunda, allowlist'e doğrudan argüman-enjeksiyonuyla, insan onayı devreye girmeden RCE — kaynakta birebir DOĞRULANDI. |
| Ç8 | **P DARALDI** | **Q SAĞLAM** | recursion_limit/max_iterations gerçekten vardır ve döngüyü keser (olgu doğru), ama "yeterli" hükmü desteksiz; Q'nun "bütçe harcandıktan sonra devreye giren son-çare" itirazı P'nin normatif kısmını mantıken zaten yener (limit tanımı gereği post-hoc). |

Not: Ç1/Ç3/Ç4/Ç5/Ç6/Ç8'de P'lerin ORTAK arızası aynı — kaynak bir YETENEK/VARSAYILAN belgeliyor, iddia ise bundan bir YETERLİLİK NORMU çıkarıyor. Bu, kaynağın söylemediğini kaynağa yükleme (aşırı-genelleme) hatasıdır; "DÜŞTÜ" yerine "DARALDI" verdim çünkü olgusal çekirdek her birinde doğru.

## Bölüm 2 — Zorunlu doğrulama örneklemi

### (a) Sayısal

| Kalem | Durum | Kaynakta gerçekte ne yazıyor |
|---|---|---|
| %8,3 / %4,6 (ReasoningBank) | **DOĞRULANDI** | research.google blog, "Performance & emergent capabilities → Superior success rates": ölçeklemesiz ReasoningBank hafızasız ajanları WebArena'da %8,3, SWE-Bench-Verified'da %4,6 geçiyor. |
| %39 (arXiv 2505.06120) | **DOĞRULANDI** | Özet: altı üretim görevinde çok-turlu ile tek-turlu arası ortalama %39 düşüş; ayrışım "yetenekte küçük kayıp + güvenilmezlikte belirgin artış" — iddianın vurgusu birebir. |
| 100.000 token + keep=3 (context-editing) | **DOĞRULANDI (nitelemeyle)** | `clear_tool_uses_20250919` yapılandırma tablosu: `trigger` = 100.000 girdi-token, `keep` = 3 araç-kullanımı. Bunlar VARSAYILANDIR, ayarlanabilir; belge "sabit eşik doğru tasarımdır" demez. |
| %29,1 / %27,3 / %36,8 / %6,8 (arXiv 2510.07593) | **DOĞRULANDI** | Makale "AgentAsk: Multi-Agent Systems Need to Ask"; §3.5, 824 yürütme logluk etiketli derlem: Data Gap %29,1 · Referential Drift %27,3 · Signal Corruption %36,8 · Capability Gap %6,8. Özet yalnız dört sınıfı sayar, yüzdeler gövdededir. Uyarı: bu taksonomi "devir sonrası bilgi kaybı" değil, **ajanlar-arası mesaj devrindeki kenar-düzeyi hata** taksonomisidir; iddianın çerçevesi kaynağa göre hafif kaydırılmıştır. |

### (b) Son-üçlük — Trail of Bits (Ç7)

**DOĞRULANDI.** Yazı üç ayrı ajan platformunda aynı deseni bildiriyor ("three different agent platforms", eşgüdümlü açıklama sürdüğü için ürün adları verilmemiş, üçü de "popular AI agents"). İnsan onayı iddiası da yazıda: bazı komutlar verimlilik için otomatik koşuyor, diğerleri insan onayı istiyor, "bu sağlam bir koruma gibi görünebilir" — fakat argüman-enjeksiyonuyla insan-onayı koruması atlatılıyor. Allowlist hedeflemesi de açık: saldırı, onaysız koşabilen kabuk komutları allowlist'ini tespit etmekle başlıyor; sistemler argüman bayraklarını doğrulamadığı için savunmasız. Üç iddianın üçü de metinde var.

### (c) URL'siz / model-hafızası iddiaları

| Kalem | Durum | Gerçekte ne bulundu |
|---|---|---|
| U1 — "dal+koşul toplamı 5'i aşınca başarı ölçülü düşer" | **DOĞRULANAMADI** | 5 eşiği için hiçbir kaynak yok. Yön doğru ama eşiksiz: AgentIF (Tsinghua KEG), koşul-kısıtlarında modellerin düz kısıtlara göre belirgin düşük performans gösterdiğini, koşul-kısıtların gerçek dünya talimatlarının ~%42,6'sını oluşturduğunu bildiriyor; dal derinliği bir karmaşıklık ekseni olarak inceleniyor (arXiv 2608.17318). Belirli "5" sayısı UYDURMADIR — iddianın sayısal kısmı DÜŞER, niteliksel kısmı ("dal/koşul arttıkça başarı düşer") desteklidir. |
| U2 — "kendi çıktısını hakemleyen lider etiketleri yumuşatır; bağımsız hakem sertleştirir" | **KISMEN** | Kendi-kayırma (self-preference) yanlılığı literatürde yerleşik: yargıç model kendi ailesinden çıktıyı yüksek puanlar, düşük-perplexity/tanıdık metni insana kıyasla yukarı çeker (arXiv 2410.21819, 2604.22891, 2508.06709). Yani "yumuşar" yönü DESTEKLİ. Ancak "bağımsız hakem SERTLEŞTİRİR" kısmı doğrudan desteklenmiyor; literatür, bağımsız yargıcın sistematik olarak daha katı değil sadece FARKLI kalibre olduğunu, yargıçlar arası tutarlı yumuşaklık/katılık farkının ayrıca hesaba katılması gerektiğini söylüyor. Bağımsız hakem yanlılığı kaldırır ≠ sertleştirir. |
| U3 — "arXiv 2606.02875 (Handoff Debt) devir sonrası bilgi kaybını SAYISALLAŞTIRIR" | **KISMEN** | Makale gerçek: "Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks", arXiv:2606.02875, 1 Haziran 2026. 181 devir-noktası görevi; bulgu: bağlam taşıyan devirler, salt-depo devrine göre medyan ajan-olayını %20-59, kümülatif prompt-token'ı %42-63 azaltıyor. Yani sayısallaştırdığı şey **bilgi kaybı** değil, kaybın PROXY MALİYETİ (yeniden-keşif eforu/token). Referans doğru, ifade fazla iddialı → "bilgi kaybını sayısallaştırır" yerine "yeniden-keşif maliyetini sayısallaştırır" demeli. |

## Hakem özeti
- Uydurma kaynak/sayı BULUNMADI; örneklenen dört sayısal kalemin dördü de kaynakta birebir çıktı, Trail of Bits'in üç alt-iddiasının üçü de metinde var.
- Sistematik zayıflık P tarafında: belgelenmiş bir yetenek ya da varsayılan değer, belgenin savunmadığı bir "yeterlidir / doğru tasarımdır" normuna dönüştürülüyor (Ç1, Ç3, Ç4, Ç5, Ç6, Ç8).
- Q tarafındaki iki kayma: Ç6'da `applied_edits` yanlış-eşleşme (devir şeması değil, sıkıştırma telemetrisi) ve 2510.07593'ün "ajanlar-arası mesaj devri" taksonomisinin "bağlam devri sonrası kayıp" diye çerçevelenmesi.
- URL'siz üçlüde tek net arıza U1'in "5" eşiği: dayanaksız, düşürülmeli.
