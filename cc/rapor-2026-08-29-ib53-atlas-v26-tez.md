# V26 ÖRNEKLEM-DENETİMİ — IB-53 ATLAS tez raporları (A · B · C)

**Denetçi:** V26 örneklem-denetçisi (kural-tabanlı, deterministik — Salih imzası 08-17)
**AS-OF:** 2026-08-29 (tüm sondajlar bu tarihte canlı kaynaktan çekildi)
**Rol sınırı:** Üretici değil. Yorum, karar, öneri YOK — yalnız sondaj sonuçları.

## Kırpma beyanı (zorunlu)

Bu **tam doğrulama değildir**. Denetlenen iddia sayısı: 3 raporda toplam **257 iddia** (tez-A 102 · tez-B 28 · tez-C 55 + gövde tabloları). Sondaja alınan: **16 kalem**.

Seçim kuralı (rastgelelik yok, R3):
1. Her rapor için **son üçte birindeki İLK kaynak-URL'li iddia** (deterministik konum kuralı).
2. Görev emrinde adı geçen **karar-taşıyan sayısal iddialar** — yani sonraki antitez/karar aşamasının üstüne basacağı rakamlar.
Denetlenmeyenler: canlılık/tarih satırlarının çoğu, lisans envanteri, paywall'lı akademik kalemler (tez-B'nin kendi bayrakladığı Ware&Mitchell 2008 · Greffard 2011 · Ghoniem 2005), kaynak-kodu satır-numarası iddiaları.

**Yöntem:** `gh api` (kimlik doğrulamalı GitHub REST), VS Code Marketplace Gallery API (`extensionquery`, flags=914), `curl` + `raw.githubusercontent.com`, PDF indirip `pdftotext` ile ham metin (özet modeline güvenilmedi), MDN canlı sayfa.

---

## RAPOR A — `cc/rapor-2026-08-29-ib53-atlas-tez-a.md`

Son üçte bir sınırı: 371 satırın 248. satırı → ilk kaynak-URL'li iddia **İ-63**.

| # | İddia (aynen) | Kaynak | Sonuç | Bulunan gerçek değer |
|---|---|---|---|---|
| A1 | *(son üçte bir kuralı)* "`sourcegraph/sourcegraph` deposu bugün GitHub API'de **404** döndürür; `sourcegraph/sourcegraph-public-snapshot` arşivlidir (son push 2024-09-02) ve README'si *'Sourcegraph transitioned to a private monorepo'* der" | `gh api repos/sourcegraph/sourcegraph` · `…/sourcegraph-public-snapshot` · README ham | **TUTTU** | `sourcegraph/sourcegraph` → `{"message":"Not Found","status":"404"}`. Snapshot: `archived:true`, `pushed_at:2024-09-02T11:52:13Z`. README satır 2 birebir: *"Sourcegraph transitioned to a private monorepo. This repository, `sourcegraph/sourcegraph-public-snapshot` is a publicly available copy…"* — üç bileşen de birebir. |
| A2 | "Foam … 272.027 kuruluma sahiptir (Gallery API çekimi)" (İ-13) | Marketplace Gallery API, flags=914 | **TUTTU** (canlı sayaç kayması) | `install: 272029.0`. Fark **+2**, aynı gün içinde, monoton artan canlı sayaç. Yöntem birebir tekrar-üretildi; olgusal hata değil. |
| A3 | "Foam marketplace'te **0.44.5** sürümüyle **2026-07-26**'da güncellendi" (İ-13) | Marketplace Gallery API | **TUTTU** | `version: 0.44.5`, `lastUpdated: 2026-07-26T09:28:14.18Z` — birebir. |
| A4 | "Cosma'nın lisans dosyası `GPL-3.0 OR CeCILL-2.1` ifadesini taşır; son sürüm **2.6.1**, **2026-03-17**" (İ-37) | `gh api repos/graphlab-fr/cosma/releases` · `LICENSE.txt` (develop) · `package.json` | **TUTTU** (bir imla farkı) | Release: `tag 2.6.1`, `published_at 2026-03-17T10:57:55Z` — birebir. `LICENSE.txt` gerçek metni: **`GPL-3.0 OR CeCILL.2.1`** (ayraç **nokta**, tire değil). `package.json` → `GPL-3.0-or-later`. Rapor bu ikili-kaynak tutarsızlığını İ-102'de zaten kayda geçirmiş; tek fark tek karakterlik imla. Yan doğrulama: `stars: 190` (raporla aynı). |
| A5 | "VS Code markdown'da `[b](./b.md#L3)` biçimi dosyayı 3. satırda açar; talep **2017-12-13**'te 'completed' olarak kapatıldı" (İ-1) | `gh api repos/microsoft/vscode/issues/40140` | **TUTTU** | `state: closed`, `state_reason: **completed**`, `closed_at: 2017-12-13T02:13:49Z`, başlık *"Support link with line numbers in the markdown editor"* — birebir. Yan doğrulama: #125320 `closed 2021-10-08`, `completed`; vscode-markdown-languageservice#29 `closed 2022-09-16` — ikisi de raporla birebir. |

**SONUÇ SATIRI — RAPOR A: PASS.** 5/5 sondaj tuttu. TUTMADI yok → K-damgası tetiklenmedi. İki mikro-not: (a) Foam kurulum sayacı +2 kaydı (canlı sayaç, olgusal sapma değil); (b) Cosma LICENSE.txt'te ayraç `CeCILL.2.1` (nokta), raporda `CeCILL-2.1` (tire) — anlam aynı, imla farklı.

---

## RAPOR B — `cc/rapor-2026-08-29-ib53-atlas-tez-b.md`

Son üçte bir sınırı: 213 satırın 142. satırı → bu bölgedeki ilk kaynak-URL'li iddia **İddia 1** (satır 162).

| # | İddia (aynen) | Kaynak | Sonuç | Bulunan gerçek değer |
|---|---|---|---|---|
| B1 | *(son üçte bir kuralı)* "Ware & Franck'in 1996 deneyinde … aynı deneyde **statik perspektif 2B'den anlamlı ölçüde farklılaşmamıştır**" | `ware96.pdf` → `pdftotext`, gövde | **TUTTU** | Gövde birebir: *"The two 2D conditions gave significantly higher error rates than all other conditions although they did not differ significantly from each other."* Koşul listesi de doğrulandı: **(1) 2D** (ortografik, "removing Z axis information") ve **(2) Static perspective** — yani "iki 2B koşulu" okuması doğru. Sonuç bölümü ayrıca: *"A static perspective image may add little in comparison with a 2D diagram."* |
| B2 | "aynı hata oranında anlaşılabilir graf yalnız stereo ile **1,6×**, yalnız kafa-izleme ile **2,2×**, ikisi birlikte **3,0×** büyür" (İddia 2) | `ware96.pdf` gövde s.133 + abstract | **TUTTU** | Gövde birebir: *"…head-coupled stereo is about 3.0 times as large as the 2D graph for any given error rate… stereo alone… by approximately a factor of 1.6, and adding head coupling alone… by a factor of 2.2."* Abstract'ta da aynı üç rakam. |
| B3 | "(hata=C·N katsayıları **0,369 / 0,232 / 0,167 / 0,123**)" (İddia 2) | `ware96.pdf` gövde, tek-parametreli uyum tablosu | **TUTTU** | Tablo birebir: 2D **0.369** · Stereo perspective **0.232** · Head-coupled perspective **0.167** · Stereo, head-coupled perspective **0.123**. Model birebir: *"a one–parameter fit, of the form `Errors = C * N` where N is the number of nodes accounted for 95% of the variance"* → raporun "varyansın %95'i" ifadesi de tuttu. Ayrıca "ikili ANOVA'ların hepsi p<0,01": gövde *"each of the four conditions was significantly different from the others with p < 0.01"*. |
| B4 | "ölçülmüş kırılma noktası: **yoğunluk 6'da ≥50 düğüm**, **yoğunluk 2'de >100 düğüm**; bu noktalarda katılımcılar denemelerin yarısından fazlasında YANLIŞ cevap vermiştir" (İddia 12) | arXiv 2008.07944 PDF → `pdftotext`, gövde + abstract | **TUTTU** | Gövde birebir: *"For small-world graphs with 50 or more nodes and a density (ratio of edges to nodes) of 6, participants were unable to correctly answer in more than half of the trials. This was also the case for graphs with a density of 2 and more than 100 nodes."* İki eşik de birebir. |
| B5 | "tarama … graf boyutu medyanı **49,5 düğüm** … %80'i (**121/152**) ≤100 düğüm" (İddia 15) | arXiv 1809.00270 PDF → `pdftotext`, Tablo II + Bölüm "Findings" | **TUTTU** | Tablo II medyan satırı: **49.5** düğüm / **73** kenar. Gövde birebir: *"80% of studies (121 / 152 studies) use graphs with 100 nodes or less, while only 37% (56 / 152 studies)…"* Yan doğrulama (bedava çıktı): alt çeyrek **18.5**, üst çeyrek **116.5** ✓; *"(20 / 24 studies, 83%)"* ✓ — raporun 16. iddiası da birebir. |
| B6 | "odak-getirme … **27,2s → 8,5s** (~3,2× hız) ve yoğun grafta hata **%25 → %10**" (İddia 20) | aviz.fr Moscovich CHI 2009 PDF → `pdftotext`, Results | **TUTTU** | Gövde birebir: *"Mean times were: PZ 27.2 sec (SD=0.8), BEV 21 sec (SD=0.7), LS 24 sec (SD=0.8) and B&G 8.5 sec (SD=0.2)"*, `F3,33 = 69.811, p < .0001`. Hata birebir: *"BEV (42% error rate) and LS (33%)… than B&G (10%), while PZ showed a 25% error rate."* → PZ %25 → B&G %10 tuttu; 27,2/8,5 = 3,2× oranı da doğru. |

**SONUÇ SATIRI — RAPOR B: PASS.** 6/6 sondaj tuttu. TUTMADI yok → K-damgası tetiklenmedi. Kapsam notu: raporun kendi bayrakladığı paywall'lı üç kalem (Ware&Mitchell 2008 · Greffard 2011 · Ghoniem 2005) bu sondaj listesinde YOKTU, dolayısıyla denetlenmedi — raporun o kalemleri "yalnız abstract" diye işaretlemesi olduğu gibi durmaktadır.

---

## RAPOR C — `cc/rapor-2026-08-29-ib53-atlas-tez-c.md`

Son üçte bir sınırı: 199 satırın 133. satırı → ilk kaynak-URL'li iddia **İddia 16**.

| # | İddia (aynen) | Kaynak | Sonuç | Bulunan gerçek değer |
|---|---|---|---|---|
| C1 | *(son üçte bir kuralı)* "TypeDoc JSON çıktısı her sembol için `sources: [{ fileName, line, character }]` üretir." (İddia 16) | `typedoc.org/api/modules/JSONOutput.html` (HTTP 200) + `TypeStrong/typedoc` ham kaynak | **TUTTU** | `src/lib/serialization/schema.ts:421` birebir: `export interface SourceReference extends S<M.SourceReference, "fileName" \| "line" \| "character" \| "url"> {}`. `sources` alanı `DeclarationReflection` ve `SignatureReflection` serileştirmelerinde mevcut (satır 142, 167). Model tarafı `SourceReference.ts` `toObject()` → `{fileName, line, character}` basıyor. Tek fark: şema `url` alanını da taşıyor (rapor bunu saymamış — eksiltme, hata değil). |
| C2 | "SCIP'in `Occurrence.range` alanı … tam olarak **üç** (`[startLine, startCharacter, endCharacter]`) ya da **dört** (`[startLine, startCharacter, endLine, endCharacter]`) elemanlı olmak zorundadır." (İddia 1) | `raw.githubusercontent.com/sourcegraph/scip/main/scip.proto` (HTTP 200, `scip-code/scip`'e yönleniyor) | **TUTTU** (+ atlanmış nitelik) | `scip.proto:695-697` birebir: *"Half-open [start, end) range. Must be exactly three or four elements: - Three elements: `[startLine, startCharacter, endCharacter]` (single-line) - Four elements: `[startLine, startCharacter, endLine, endCharacter]`"*. **Not:** aynı dosyanın 709. satırında alan `repeated int32 range = 1 [deprecated = true]` olarak işaretli; raporun İddia 1'i bu "deprecated" durumunu ANMIYOR (gövde tablosu C1 satırı tipli `single_line_range`/`multi_line_range` alternatiflerini anıyor, "deprecated" demiyor). İddianın söylediği yanlış değil, eksik. |
| C3 | "SCIP verisi için belgelenmiş tek somut oran sıkıştırma oranıdır (**'compression ratio around in the range of 10%-20%'**)" (İddia 5) | `raw…/scip/main/docs/DESIGN.md` (HTTP 200) | **TUTTU** | `DESIGN.md` dipnot [^3] birebir: *"In practice, SCIP data tends to be have a compression ratio around in the range of 10%-20%, as modern compressors are very good at de-duplicating away the repetitive textual symbols."* Rapordaki tırnak içi ifade karakter karakter aynı (kaynaktaki dilbilgisi hatası "tends to be have" dâhil). Raporun "8x küçük / 3x hızlı rakamları doğrulanamadı [?]" bayrağı da yerinde: DESIGN.md'de o rakamlar geçmiyor. |
| C4 | "SourcetrailDB API'si `recordSymbolLocation()` ile `fileId, startLine, startColumn, endLine, endColumn` kaydeder ve satır/sütun **1-tabanlıdır**." (İddia 10) | `raw…/CoatiSoftware/SourcetrailDB/master/README.md` (HTTP 200) | **TUTTU** | README satır 289-297 birebir: `sourcetrail::SourceRange location;` → `location.fileId` · `location.startLine = 8; // lines start at 1, not 0` · `location.startColumn = 7; // columns start at 1, not 0` · `location.endLine` · `location.endColumn` → `writer.recordSymbolLocation(symbolId, location);`. Beş alan da, 1-tabanlılık da birebir. Yan doğrulama: "arbitrary … or other kind of data" ifadesi de README satır 13'te birebir (tez-A İ-58 ile aynı kaynak). |
| C5 | "Modern tarayıcılar (Firefox ve Chrome dâhil) tüm yerel dosyaları varsayılan olarak **opak origin** sayar… MDN'in çözümü yerel bir sunucu kurmaktır." (İddia 29 + 30) | MDN `CORS/Errors/CORSRequestNotHttp` canlı sayfa | **TUTTU** | Birebir: *"Many browsers, including Firefox and Chrome, now treat all local files as having opaque origins (by default)."* ve *"Developers who need to perform local testing should now set up a local server."* CVE-2019-11730 atfı da sayfada mevcut — raporun C24 satırındaki gerekçelendirme doğru. |

**SONUÇ SATIRI — RAPOR C: PASS.** 5/5 sondaj tuttu. TUTMADI yok → K-damgası tetiklenmedi. Bir eksiltme kaydı: İddia 1, `Occurrence.range` alanının `scip.proto`'da `[deprecated = true]` işaretli olduğunu belirtmiyor (iddia doğru, nitelik eksik).

---

## TOPLAM

| Rapor | Sondaj | TUTTU | TUTMADI | ERİŞİLEMEDİ | Sonuç |
|---|---|---|---|---|---|
| tez-A | 5 | 5 | 0 | 0 | **PASS** |
| tez-B | 6 | 6 | 0 | 0 | **PASS** |
| tez-C | 5 | 5 | 0 | 0 | **PASS** |

**K-damgası tetiklenmedi** (hiçbir raporda TUTMADI yok). Üç rapor da denetlenen kalemler bakımından kaynağa iniyor ve rakamları birebir taşıyor.

**Erişim kaydı:** Bu denetimde hiçbir sondaj 403/paywall'a takılmadı. Denetlenen 16 kalemin tamamı birincil kaynaktan (ham repo dosyası · resmî spec · yayıncı/kurum PDF'i · resmî API) çekildi. `api.github.com` anonim kotası doldu → kimlik doğrulamalı `gh api` ile koşuldu.

**Bulunan sapmalar (üçü de olgusal-olmayan, kayıt amaçlı):**
1. tez-A / Foam kurulum sayacı: rapor 272.027, denetim 272.029 (+2, aynı gün, monoton canlı sayaç).
2. tez-A / Cosma LICENSE.txt: gerçek metin `GPL-3.0 OR CeCILL.2.1` (nokta), raporda `CeCILL-2.1` (tire).
3. tez-C / İddia 1: `Occurrence.range` alanının `[deprecated = true]` niteliği anılmamış.

---

**Denetim sonu — V26 örneklem-denetçisi, AS-OF 2026-08-29.**
