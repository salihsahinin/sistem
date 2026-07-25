# Şerit 2 — "Graph Engineering" Nedir, JARVIS'e Girer mi? (Atlas Raporu, 2026-07-24)

> **Mod:** yan-oturum (m.41) — öneri üretir, kanon KİLİTLEMEZ.
> **Şerit:** çift-atlas · aile 3 · tez 3/3, antitez 2/3 (¬T2-A3 oturum limitinde öldü)
> **Kaynak:** `scratchpad/T2-A{1,2,3}-seritA.md`, `T2-A{1,2}-seritB.md`

## 0. BLUF

**Etiketi almayın, pratiği alın — ve pratiği bizde zaten var olan şeyin üstüne kurun.**

"Graph engineering" 4–18 Temmuz 2026 arasında X üzerinde doğmuş bir etiket. Kurumsal bir duyuru, makale ya da ürün değil. İşaret ettiği mühendislik pratiği ise gerçek ve etiketten yıllarca eski.

Bizim için asıl bulgu terimde değil, **kendi deponuzda yapılan ölçümde**: 146 markdown dosyanın %92,5'i graf olarak yetim ve elle tutulan wiki index'i 07-19'da 6 sayfadan 2'sini listeliyordu. Yani bizim sorunumuz "graf teknolojisi eksikliği" değil, **zaten seçtiğimiz standardın uygulanmaması**.

## 1. Kanıt kısıtı (raporun tamamını etkiler)

Bu şeritte egress politikası neredeyse tüm dış kaynakları 403'ledi: x.com, arxiv, wikipedia, medium, substack, langchain.com, turingpost, nature, research.google. **Aile 1 tek bir [D] üretemedi.**

Geçen tek yol `raw.githubusercontent.com` oldu ve iki ajan bunu ustaca kullandı: benchmark leaderboard'larının **ham CSV'lerine** ve proje README'lerine doğrudan inerek [D] üretti. Bu, bu oturumun en değerli yöntemsel keşfi.

## 2. Terim: köken ve statü

| Bulgu | Etiket |
|---|---|
| Viral fitil: 18 Temmuz 2026 tarihli tek satırlık bir X postu | [K] |
| Terimi disipline çeviren manifesto aynı gün, ~4,5 saat sonra yayımlanan bir X Article | [K] |
| Akademik makale / konferans / paket **yok** (`pypi graph-engineering` → 404) | [D] |
| **Anthropic'in tüm doküman korpusunda "graph engineering" sıfır kez geçiyor** — 6,36 MB `llms-full.txt` bugün indirilip tarandı; sözlük tamamen farklı (subagent 1176, workflow 448, agent team 113) | **[D]** |

### 2.1 ★ Antitezin tez düzeltmesi — rapora giren en önemli tekzip

Tez ajanı "LangChain terimi **reddetti**" demişti. Antitez bunu **çürüttü**:

> LangChain terimi reddetmedi, **sahiplendi**. 23 Temmuz'da Harrison Chase imzalı kurumsal blog: *"3 Years of Graph Engineering with LangGraph"* + "terimler bir sebeple ortaya çıkar, buzzword değil" savunması. Reddettiği şey terim değil, **terimin yeniliği**.

Bu, tezin "kurumsal katılım yok" iddiasını da daraltıyor: kurumsal katılım **var**, ama **gecikmeli ve tepkisel** — köken kurumsal değil. Doğru cümle: *"hiçbir kurumsal tanıtım yok"* değil, *"köken kurumsal değil"*.

### 2.2 Yaygınlık: hacim gerçek, bağımsızlık değil

Tez "~15 bağımsız ikincil kaynak" demişti. Antitez saydı: **≥18 alan adı**, ama bağımsız değil — satıcı pazarlaması (4+), **tek yayıncıda 5 SEO varyantı**, Medium yeniden-paketleyicileri. Hepsi aynı iki X postuna bağlı **korele yankı**.

### 2.3 Metodolojik uyarı (antitez ajanının kendi kaydı)

Antitez, tezi "teyit eden" arama özetinin tez cümlesiyle neredeyse birebir örtüştüğünü fark etti — yani tez ile teyit **aynı ikincil kaynağa** dayanıyor olabilir. x.com kapalı olduğu için tüm tarih/saat/görüntülenme verileri birincil doğrulanmamıştır [X]. Bu, çift-atlas protokolünün kendi kör noktasını yakaladığı nadir bir kayıt.

## 3. Teknik cevher: graf ne zaman kazanır, ne zaman kaybeder

Ham leaderboard CSV'sinden ([D], doğrudan indirildi):

| Soru tipi | Sonuç |
|---|---|
| **Çok-sıçramalı akıl yürütme** | Graf kazanıyor: 13 yöntemin 10'u düz RAG'ı geçiyor (+10 ila +20 puan) |
| **Tek-sıçramalı olgu getirme** | **Hiçbir graf yöntemi düz RAG'ı geçemiyor** (düz RAG 60.92 = alandaki en yüksek) |
| **Kötü graf tasarımı** | Düz RAG'ın yarısına düşürüyor (−33,87 puan) |

### 3.1 ★ Ölçek eşiği — bizim için belirleyici olan bulgu

Antitezin çocuğu, tezin "küçük ölçekte ölçülmemiş" iddiasını kırdı ve **geçiş noktasını** buldu [K]:

| Rejim | Korpus | Düz RAG (karmaşık akıl y.) |
|---|---|---|
| Small | ~56k token | **%58,64** (graftan iyi) |
| Medium | ~603k token | (ara) |
| Large | ~1.132k token | **%43,20** (graftan ~10 puan kötü) |

Graf yöntemi ise **tüm ölçeklerde sabit**. Yani: küçük korpusta graf kazancı **negatif**, büyük korpusta **pozitif**.

**Ve tezin örtük öncülü kırıldı:** "birkaç bin not = küçük korpus" yanlış. Eşikler token cinsinden; 56k token ≈ yalnızca ~140 kısa not.

**JARVIS'in kendi konumu [?] — kestirim, ölçüm değil:** depo ~1,3 MB metin. Türkçe için kaba çevrimle **~350–500k token**. Bu bizi **Medium rejimin içine**, geçiş noktasının yakınına koyuyor. Bugün graf yatırımı erken; ama depo iki katına çıkarsa eşiği geçiyoruz. *Bu rakam ölçülmeli — `count_tokens` ile, tahminle değil (sayı-araştırma kapısı, KILAVUZ 07-23).*

### 3.2 Orkestrasyon grafı: ölçülmüş ve **kaybediyor**

Tez "orkestrasyon grafının doğruluk kazancı ölçülmemiş" demişti. Antitez kırdı — ölçülmüş, ve sonuç graf **aleyhine** [K]:

> Prosedürel, tek-iplikli işlerde harici orkestratör (LangGraph) vs "prosedürün tamamı sistem promptunda" temel çizgisi, koşul başına 200 konuşma × 3 alan: hata oranı **%24 vs %11,5** (seyahat), **%9 vs %0,5** (destek), **%17 vs %5** (sigorta).

Karşı-rejim de var: paralelleştirilebilir / genişlik-öncelikli / yüksek-yüklü işlerde çoklu-ajan pozitif (Anthropic'in kendi araştırma sistemi +%90,2, ⚠~15× token). **JARVIS'in profili prosedürel ve tek-kullanıcılı** → bu bulgu bizde orkestrasyon grafına karşı.

### 3.3 Maliyet ve bakım riski

- GraphRAG indeksleme: 1000 sayfa PDF ≈ $120; 1M kelime ≈ $8,20; sorgu başına ≈ $0,40 [D]
- Resmî doküman kendi uyarısını basıyor: *"indeksleme pahalı olabilir, küçük başlayın"* [D]
- **Gömülü graf DB seçmek canlı bakım riski**: öne çıkan bir motor (Kuzu, 4,0k★) Ekim 2025'te sahibi tarafından arşivlendi, salt-okunur [D]

## 4. ★ Asıl bulgu: kendi deponuzun ölçümü

Dış kaynaklar kapalı olduğu için T2-A3 birinci-el ölçüme döndü. Kanıt hiyerarşisinde bu **daha yukarısı**:

| Ölçüm | Sonuç |
|---|---|
| Markdown dosya | **146** ✓ (bu oturumda bağımsız doğrulandı) |
| Çözülen `[[wiki-link]]` kenarı | **15** |
| Yetim dosya oranı | **%92,5** (135/146), 136 ayrı bileşen |
| `wiki/` alt-grafı | 8 dosya, 11 kenar, **0 yetim, tek bileşen** |
| Tam graf çıkarımı + türetilmiş index | **~45 ms**, stdlib-only, hiçbir vault dosyasına dokunmadan |
| Grafın markdown serileştirmesi | ~1,2 KB ≈ **358 token** [?] |
| Karşılaştırma: bir MCP aracının tanım maliyeti | 550–1.400 token [K] |

**Yorum:** `wiki/` standardın çalıştığını kanıtlıyor. Sorun `[[wiki-link]]` kalitesi değil, kalan 138 dosyada **uygulanmaması**.

### 4.1 ★ Elle tutulan index bayatlıyor — yaşanmış vaka, bu oturumda doğrulandı

07-19 commit'inde (`aba4f6f`) `wiki/` altında README + **6 içerik sayfası** vardı. README'nin index'i o sayfalardan **2'sini** listeliyordu → **%67 kayıp**. Hata 3 gün sonra (`e50d342`) özel bir manuel hijyen turuyla düzeltildi.

**V26 denetimi (bu oturumda, kaynağa inilerek):** ajanın sayısı ilk bakışta tutmadı (ben 3 link saydım). Farkı kapattım — üçüncü link `[[wiki-link]]`, yani standardın adı, içerik sayfası değil. **Ajan haklı, benim ölçüm aletim kabaydı.** İddia doğrulandı.

Bugün de 6 benzersiz kırık wiki-link var ve elle tutulan liste bunların yarısını içeriyor.

**Bu, "türetilmiş index" argümanının en güçlü hali:** teorik risk değil, kendi git tarihimizde iki kez gerçekleşmiş hata.

## 5. Sentez — JARVIS'e ne girer

### Girer (düşük maliyet, ölçülmüş sorun)
**Türetilmiş graf index'i, salt-okunur vault.** Alandaki olgun araçların ortak deseni bu: index kaynak dosyalardan yeniden inşa edilebilir, vault dışına yazılır, vault içeriği asla değiştirilmez.

Somut tarif (T2-A3, ~60 dk, 0 yeni bağımlılık — Python 3.11 + sqlite3 zaten var):
1. `araclar/graf.py` — salt-okunur, deterministik çıktı
2. `raporlar/graf-durum.md` — ~1,2 KB, commit'lenir (`graf.sqlite` gitignore)
3. `session-start.sh`'a 3 satır özet enjeksiyonu (~60 token; tam graf pointer'da — m.20)
4. `graf.py --check` — yalnız 07-19'da kırılan invariantı zorlayan dar kontrol
5. Geri alma: 1 dosya + 1 hook satırı + tek `git revert`

**Kanon uyumu:** m.20 (pointer) · m.35 (ölçüm-öncelik) · m.5 (sorun-güdümlü) · m.8 (silme yok, türetilmiş artefakt) · V25 (desen alınır, kurulum alınmaz).

### Girmez (bugün)
- **Etiket.** "Graph engineering" terimini kanona sokmayın; 6 haftada doğup ölen bir adlandırma döngüsü.
- **Graf veritabanı.** Bakım riski canlı, ölçek eşiği bizde henüz geçilmedi.
- **LLM entity-extraction'lı GraphRAG.** Maliyet ölçüldü, fayda bizim ölçeğimizde ölçülmedi.
- **Orkestrasyon grafı çerçevesi.** Bizim iş profilimizde ölçülen etki negatif.

### Ölçülmeli (karar değil, ölçüm borcu)
- Deponun gerçek token büyüklüğü (`count_tokens`) — graf eşiğine uzaklığımız buna bağlı.
- **Obsidian vault'a özgü kontrollü graf-vs-vektör ölçümü literatürde YOK** [X] — 8 büyük vault projesinin README'si tarandı, tek bir kontrol kollu sayı yok. Yani bu alanda ölçen ilk kişi biz olabiliriz.

## 6. Cevaplanmamış sorular (m.41)

1. Depo token büyüklüğü kaç? Medium rejimin neresindeyiz?
2. Türetilmiş index'in **kendi** arıza modları neler (prob çalışmazsa, sessizce boş üretirse)? Manuel hatayı otomatik hatayla değiştirmiş olur muyuz? — ¬T2-A3 tam bunu sınayacaktı, oturum limitinde öldü.
3. `wiki/` dışındaki 138 dosyaya link disiplini uygulanacak mı, yoksa wiki/ bilinçli olarak ayrı mı kalacak?
4. İnsan-kürasyonlu graf (bizim `[[wiki-link]]`) ile otomatik-inşa graf arasındaki getiri farkı **ölçülmemiş** [X] — tüm benchmark'lar otomatik graflar üzerinde.

---

*Yan-oturum çıktısı. Kanon kilitlenmedi. Karar ana-sırada (m.41).*
