# IB-53 · ATLAS HAKEM RAPORU — Aile A (dış emsal araçları)

## Künye
- **Rol:** MASKELİ HAKEM. Üretici koşumların devamı değilim; iki raporu kimliğine değil İDDİA+KANIT içeriğine göre kıyasladım.
- **Girdi:** yalnız `hakem-a/rapor-1.md` (tez, 102 iddia) ve `hakem-a/rapor-2.md` (antitez, 19 iddia denetimi). **WEB ARAMASI YAPILMADI.**
- **AS-OF:** 2026-08-29.
- **Dış denetçi sondajı (bana bildirilen):** her iki raporun karar-taşıyan sayısal iddiaları birincil kaynağa inilerek doğrulandı ve TUTTU; tek bayrak rapor-2 tarafında — Yamlink için verilen "Marketplace lastUpdated 2026-08-18" gerçekte **2026-08-07** (hüküm değiştirmez, Ağustos 2026 canlılığı ayakta).
- **Kapsam sınırı (etiket disiplini):** rapor-2'nin kırpma beyanı gereği 102 iddianın yalnız 19'u adversarial teste girdi; kalan 83 iddia "çürütülemedi" DEĞİL, "bakılmadı" statüsündedir. SAĞLAM etiketi yalnız karşıt rapor fiilen saldırıp başaramadığı kalemlere verildi.

## Verdikt dağılımı
| Verdikt | Sayı |
|---|---|
| SAĞLAM | 8 |
| DARALDI | 9 |
| DÜŞTÜ | 4 |
| KARARSIZ | 1 |
| ÇELİŞKİLİ | 0 |

İki taraf birincil-kanıtlı olup uzlaşmayan tek bir çift bile çıkmadı; görünürdeki tek çelişki (CodeGraphy depo tarihleri) depo taşınmasıyla (V2→V4) çözüldü — çelişki değil, tezin eksik-arama hatası.

---

## Kalem-kalem verdikt tablosu

### ① Profilin tamamını karşılayan canlı araç var mı?
| # | İddia çifti | Verdikt |
|---|---|---|
| ①-1 | Tez: "①–⑤'i tek pakette veren canlı araç BULUNAMADI" (İ-83) · Antitez: agresif taramayla çürütemedi, boşluğu ölçtü | **DARALDI** |

**Daraltılmış form (AYNEN):** *Beş ölçütü birden karşılayan canlı araç yok; ama boşluk artık "hiçbir şey yok" değil, ÖLÇÜLMÜŞ bir boşluktur: en yakın canlı aday CodeGraphy'nin eksiği tek nitelik (`[[wikilink]]` yok) ve bir kullanım maliyeti (dış graf girişi dosya işaret ederek değil, npm eklentisi yazarak); profilin her parçası ayrı projelerde tek tek kanıtlıdır — file:line + belgeli-public-API emsali CBRV'de var ama proje 2023-01'den beri ölü — parçalar tek gövdede birleşmemiştir.*

Karar etkisi: tezin 1 numaralı önerisi ("kendi türevini üret") gerekçesini korur; ama "hazır araç yok, mecburen sıfırdan" gerekçesi artık kullanılamaz — CodeGraphy-eklentisi-yazma yolu gerçek bir alternatiftir.

### ② CodeGraphy / Yamlink / Cosma / Foam yetenek sınırları
| # | İddia çifti | Verdikt |
|---|---|---|
| ②-1 | Tez İ-31: "CodeGraphy dış veri girişi almaz (kendi tarayıcısı); depo `CodeGraphyV2` 2023-06-10'da durmuş, fark açıklanamadı" · Antitez: depo `CodeGraphyV4`'e taşınmış (push 2026-08-07, MIT), belgeli iki-katmanlı eklenti sistemi (`docs/PLUGINS.md`: "add Nodes and Relationships"), npm'de yayımlı sürümlenmiş API (`@codegraphy-dev/plugin-api` v8.0.0, 2026-07-30), tip düzeyinde satır/sütun aralığı | **DÜŞTÜ** (tezin nitelemesi) |
| ②-2 | Yamlink (yalnız antitezde; tezde kapsam boşluğu): MIT, v0.7.9, wikilink + blok-ID ile satır hassasiyeti + VS Code; AMA kenar-yazma API rotası YOK (yalnız düğüm CRUD) — kenarlar wikilink/frontmatter'dan türetilir → ① eksik | **DARALDI** (tarih düzeltmesiyle) |
| ②-3 | Tez §3.2: Cosma "dış kenar listesini AÇIKÇA kabul eden TEK araç" · Antitez 11a: Gephi (kenar tablosunda Source/Target zorunlu), Cytoscape, graphology/sigma da birinci-sınıf alır; Cosma'nın kendisi üç modlu (`directory|csv|online`) | **DARALDI** |
| ②-4 | Tez İ-34-36: Cosma CSV şeması (`id,source,target,label,type`), CSV↔md modlarının birlikte koşmaması, VS Code eklentisi yokluğu · Antitez 11b: birincil dokümanla birebir doğrulandı, VS Code eklentisi taramada da bulunamadı | **SAĞLAM** |
| ②-5 | Tez İ-06-11: Foam `exports.foam` enjeksiyonu mümkün ama "belgesiz iç API" · Antitez 3: enjeksiyon gerçek + Foam çok canlı; ama "belgesiz" yumuşadı VE yeni kırılganlık bulundu | **DARALDI** |

**②-1 kalan sınır (düşüş kayıtsız değil):** antitezin kendi dürüst uyarısı geçerli — CodeGraphy'nin dış veri girişi **dosya girişi değil kod girişidir** (npm paketi yaz, düğüm/kenar döndür); `[[wikilink]]` kavramı plugin API tiplerinde yok.

**②-2 daraltılmış form (AYNEN):** *Yamlink canlıdır (Marketplace lastUpdated 2026-08-07 — antitezin yazdığı 2026-08-18 değil) ve ②③④⑤'i karşılar; ① eksiktir: `src/api/router.js` yalnız düğüm CRUD sunar, kenar/link oluşturma rotası yoktur; dış kenar listesi ancak markdown'a maddîleştirilerek enjekte edilebilir; satır hassasiyeti literal `yol:satır` sözdizimiyle değil blok-ID üzerindendir.*

**②-3 daraltılmış form (AYNEN):** *Cosma, md-tabanlı bilgi-graf üreteci SINIFI İÇİNDE dış kenar listesini belgeli, birinci-sınıf giriş modu olarak alan tek araçtır; genel graf araçları (Gephi/Cytoscape/graphology) sınıf dışında bunu zaten yapar ve Cosma'nın `online` modu kenar listesini URL'den de alır — "tek araç" sıfatı yalnız sınıf-içi okumada ayakta kalır.*

**②-5 daraltılmış form (AYNEN):** *Foam enjeksiyonu fiilen mümkündür ve Foam canlıdır; ama (a) "belgesiz" sıfatı yumuşamıştır — bakımcı buna "Foam API" der (issue #308 kapanışı, 2025-09-17), "Release API v1" issue'su kapatılmıştır ve belgeli programatik yol artık MCP'dir; doküman sayfası ve npm tip paketi hâlâ yoktur; (b) enjeksiyon KALICI DEĞİLDİR — `FoamGraph.update()` sentetik kenarı siler, olay-güdümlü yeniden-enjeksiyon şarttır; (c) satır-farkındalık TEK YÖNLÜDÜR — `Connection` kenar kaynağının konumunu taşır, hedefin konumunu taşımaz (hedef çıplak URI).*

### ③ VS Code satır-adresi desteği (belgeli/belgesiz)
| # | İddia çifti | Verdikt |
|---|---|---|
| ③-1 | Tez İ-04: `vscode://file/{yol}:satır:sütun` resmî dokümanda tanımlı · Antitez 2: birebir doğrulandı, çürütecek kanıt yok | **SAĞLAM** |
| ③-2 | Tez İ-01-03: `#L123` / `#L123,45` "resmî olarak destekli" · Antitez 1: davranış doğrulandı (iddiadan bile geniş) ama "resmî" sıfatı yanlış | **DARALDI** |

**③-2 daraltılmış form (AYNEN):** *`#L123` fragmenti fiilen çalışır, iddiadan geniştir (`L` isteğe bağlı, `#L123,45` sütun, `#L12,5-L20,3` aralık) ve kasıtlıdır (bağlantı doğrulayıcı satır-linklerini açıkça muaf tutar); AMA kullanıcı dokümanında hiç geçmez — belgeli sözleşme değil, gözlemlenmiş davranıştır ve haber verilmeden değişebilir; sütun sözdizimi GitHub'ın `#L3C3` biçimiyle taşınabilir değildir. Belgeli sözleşme yalnız `vscode://` URI'sidir — iki kanal arasındaki asıl asimetri budur.*

### ④ Mermaid / D2 / Graphviz tıklanabilirlik
| # | İddia çifti | Verdikt |
|---|---|---|
| ④-1 | Tez İ-17-21: VS Code Mermaid önizlemesinde `click` çalışmaz · Antitez 6: çürütme denendi, TERSİNE mekanizma güçlendi (Mermaid `secure` anahtar listesi `securityLevel`'ı direktifle değiştirilemez kılar; yerleşik eklentinin ayar listesinde `securityLevel` yok) | **SAĞLAM** (çekirdek) |
| ④-2 | Tez İ-19'un çerçevesi: "PR #346 merge edilmeden kapandı" tezde nötr yazılmış, öneri anlatısında "reddedildi" tınısı · Antitez: PR gönderen (lilongen) tarafından kapatıldı, bakımcı kararı YOK — "denendi, olmaz dendi" değil "kimse bakmadı" | **DÜŞTÜ** ("reddedildi" okuması) |
| ④-3 | Tez İ-22-24: D2 `link:` → SVG `<a href>`, şema beyaz listesi yok, D2 canlı · Antitez 7: yerel deneyle doğrulandı (dış URL + katman + cluster linkleri gerçek `<a>` üretiyor; `href` VE `xlink:href` çift) | **SAĞLAM** (çekirdek) |
| ④-4 | Tez İ-24: "VS Code eklentisi `terrastruct/d2-vscode` 2026-08-03'te güncellendi" · Antitez: Marketplace Gallery API — `terrastruct.d2` lastUpdated **2023-09-22**, listelenen tek sürüm 0.8.8; depo canlı ama ~3 yıldır marketplace'e yayın yok | **DÜŞTÜ** (eklenti-güncel iddiası) |
| ④-5 | Tez İ-25: Graphviz `URL` özniteliği SVG'de tıklanabilir link üretir · Antitez 8: yerel deneyle doğrulandı, dokümandan bile geniş (kök graf URL'i de SVG'ye çıkıyor); ama iki pratik sınır bulundu | **DARALDI** |

**④-5 daraltılmış form (AYNEN):** *Graphviz `URL` düğüm/kenar/cluster'da SVG'ye link basar (deneyle doğrulandı, kök-graf URL'i doküman aksine SVG'de de çıkar); AMA yalnız `xlink:href` yazar, düz `href` yazmaz — SVG2 `xlink`'i emekli ettiğinden katı işleyiciler ve sanitizer'lar altında linkler sessizce ölebilir (D2 ikisini birden yazar: somut sağlamlık farkı); ve SVG `<img>` ile gömülünce linkler ölüdür — `<object>` ya da inline SVG gerekir.*

Mermaid tarafında açık kalan tek karşı-yol: Markdown Preview Enhanced'ın kullanıcı-düzenlenebilir `mermaid.initialize` yapılandırması (`securityLevel:'loose'`) — antitez de sınamadı, "sınanmamış" saydı; webview→yerel dosya engeli (vscode#112459) ayrıca duruyor.

### ⑤ Araç canlılık hükümleri
| # | İddia çifti | Verdikt |
|---|---|---|
| ⑤-1 | Tez: Dendron "ÖLÜ" · Antitez 9: upstream bakım-modu doğru; ama canlı devam çatalı `sxltd/dendron` VSIX 0.3.9 (2025-12-27) + npm paketleri dağıtıyor | **DARALDI** |
| ⑤-2 | Tez İ-58-62: SourcetrailDB arşiv, petermost forku canlı, VS Code köprüsü arşiv · Antitez 17: aynen tuttu ve keskinleşti — viewer güncelleniyor, DB-API'si (profil için kritik parça) 2021'den beri HİÇBİR yerde bakılmıyor (petermost'un kendi SDK kopyası da 2021-11-22'de donuk) | **SAĞLAM** |
| ⑤-3 | Tez İ-15-16: Marksman/Oxide/IWE sınıfında graf yok + VS Code istemcileri bayat · Antitez 5: "graf yok" 5/5 doğrulandı; istemci-bayat doğru (motorlar canlı — tez bunu zaten ayrıştırıyordu, İ-16) | **SAĞLAM** |
| ⑤-4 | Tez İ-48: zk-vscode 2024-01-04'ten beri push almadı · Antitez 14: iddiadan da kötü — marketplace yayını 2021-04-23'te donuk; zk çekirdeği çok canlı | **SAĞLAM** (ağırlaşarak) |
| ⑤-5 | Tez İ-38: Quartz v5 canlı, Releases sekmesi yanıltıcı · Antitez 12: "tamamen yanlış olabilir" diye işaretlenmişti, tersi çıktı — üç parça da doğru; Releases tuzağı antitezin kendi ilk okumasını da yanılttı | **SAĞLAM** |
| ⑤-6 | Tez İ-45: "Logseq'te SQLite'ın kanonik kaynak olduğu iddiası YALNIZ İKİNCİL kaynaklı" · Antitez 13: birincil kaynak Logseq'in kendi depolarında var (README "regular SQLite DB backups"; `db-version-changes.md`: "db.sqlite — Stores all your graph's data") | **DÜŞTÜ** (meta-iddia; alt-iddia böylece SAĞLAMLAŞTI) |
| ⑤-7 | Tez İ-55: MarkdownDB canlı (push 2026-05-21) · Antitez 18: doğru ama künye kaymış — npm `mddb` 2024-03'te donuk, yeniden yazım `@mddb/*` ailesi 2026-03'te yayında; `datopian`→`flowershow` sahiplik göçü; ~3 ay sessizlik; aynı ekipten Flowershow graf yüzeyi | **DARALDI** |
| ⑤-8 | Tez İ-57: SSG sınıfında (6 araç) "hazır bilgi-grafı bileşeni yoktur" · Antitez 16: 3/6 için ÇÜRÜDÜ — canlı hazır eklentiler var (starlight-site-graph 2026-06, docusaurus-plugin-graph-view 2026-08, MkDocs eklentileri — sonuncusunu tezin kendi §2.3'ü de belgeliyordu: iç tutarsızlık) | **DARALDI** |
| ⑤-9 | Cosma `content` kolonundaki `vscode://` linkinin üretilen HTML'e sağ salim çıkıp çıkmadığı — tez "test edilmedi, profil için kritik" diye bayraklamıştı; antitez de sınamadı | **KARARSIZ** (iki rapor da açık bıraktı; tek `cosma modelize` koşumu kapatır) |

**⑤-1 daraltılmış form (AYNEN):** *Dendron upstream'i bakım modundadır ve marketplace eklentisi 2023-08-12'den beri donuktur; ama proje "ölü" değil "upstream donuk + canlı devam çatalı var" durumundadır — `sxltd/dendron` gerçek bakım işi yapıp VSIX ve npm artefaktı dağıtmaktadır; kurucu alıntısının thread'e üçüncü kişice aktarılmış olması ayrıca zayıf halkadır.*

**⑤-7 daraltılmış form (AYNEN):** *MarkdownDB canlıdır ama tek-pakete-bakan canlılık testi yanlış negatif üretir: `mddb` npm'de 2024-03'te donuk, aktif aile `@mddb/core|cli|sdk` (2026-03); depo `flowershow/markdowndb` (datopian yönlendirmesi), son push 2026-05-21, o günden beri ~3 ay sessiz; görselleştirme kütüphanede yok, aynı ekibin Flowershow ürününde var.*

**⑤-8 daraltılmış form (AYNEN):** *SSG ÇEKİRDEKLERİNDE hazır graf bileşeni yoktur (bu form ayakta); ama sınıf genellemesi düşmüştür: Docusaurus, MkDocs ve Starlight için canlı, hazır graph-view eklentileri vardır; VitePress, Quarto ve Sphinx'te bulunamamıştır.*

---

## HAYATTA KALAN ÇEKİRDEK (karar girdisi)

1. **Tam-profil canlı araç yok — ama boşluk ölçülü.** Adversarial taramadan sonra bile beş ölçütü tek gövdede veren araç çıkmadı; en yakın canlı aday CodeGraphy'nin eksiği tek nitelik (wikilink) + bir maliyet (dış graf için npm eklentisi yazma). "Kendi türevini üret" seçeneği gerekçesini korur; "başka yol yok" gerekçesi artık kullanılamaz.
2. **VS Code satır-adres tabanı iki katmanlı.** `vscode://file/…:satır:sütun` belgeli resmî sözleşmedir (güvenle yaslanılır); markdown `#L123` fragmenti belgesiz-ama-kasıtlı davranıştır (çalışır, aralık bile destekler; yaslanılırsa "haber verilmeden değişebilir" kaydı düşülür; GitHub ile sütun sözdizimi taşınmaz).
3. **Mermaid VS Code'da tıklanamaz — mekanizma düzeyinde kesin.** `secure` anahtar listesi + yerleşik eklentinin `securityLevel` açmaması iki katmanlı kilit. Tıklanabilir graf yüzeyi = D2 (CLI canlı; VS Code marketplace eklentisi 2023'te donuk — karar CLI/SVG üzerinden verilmeli) ya da Graphviz (yalnız `xlink:href` + `<img>`-gömme tuzağı kaydıyla).
4. **Cosma CSV modu sınıfının tek belgeli dış-kenar kapısı; ama iki kayıtla.** md moduyla birlikte koşmaz (gövde CSV'ye taşınır) ve VS Code yüzü yoktur; `vscode://` linkinin çıktı HTML'ine ulaşıp ulaşmadığı hâlâ SINANMADI — karar öncesi tek `cosma modelize` deneyi zorunlu görünür.
5. **Enjeksiyonun ortak yasası (iki bağımsız ekosistemde aynı):** Foam `graph.update()` ve Obsidian çözümleme turu sentetik kenarları siler; hazır PKM'ye bindirme seçeneğinin asıl maliyeti olay-güdümlü yeniden-enjeksiyon zorunluluğudur — "bir kere yaz, dursun" yok.
6. **Canlılık tek sinyalle ölçülmez — üç doğrulanmış tuzak:** Releases-sekmesi tuzağı (Quartz), depo≠marketplace-artefaktı (D2, zk, Markdown Oxide), paket-adı/sahiplik göçü (mddb→@mddb, datopian→flowershow, CodeGraphyV2→V4). Karar "kullanıcının kuracağı artefakt" üzerinden verilmeli.

## DÜŞEN / DARALAN

**DÜŞEN (4):**
- Tez İ-31: "CodeGraphy dış veri girişi almaz; deposu 2023'te durmuş" → depo V4'e taşınmış, belgeli + npm'de sürümlenmiş eklenti API'siyle düğüm/kenar ekletiyor.
- Tez İ-24 (eklenti yarısı): "D2 VS Code eklentisi güncel" → marketplace yayını 2023-09-22'de donuk; depo canlılığı kullanıcı artefaktına yansımıyor.
- "Mermaid PR #346 reddedildi" okuması → gönderence kapatıldı; bakımcı kararı yok ("olmaz dendi" değil "kimse bakmadı" — emsal değeri farklı).
- Tez İ-45 (meta): "Logseq SQLite-kanonik iddiası yalnız ikincil kaynaklı" → birincil kaynak Logseq depolarında mevcut; düşüş alt-iddiayı güçlendirir.

**DARALAN (9):** ①-1 tam-profil boşluğu (ölçülmüş boşluğa) · ②-2 Yamlink (tarih 2026-08-07; kenar-yazma API'si yok) · ②-3 Cosma "tek araç" (sınıf-içi tek'e) · ②-5 Foam (yarı-resmî API + kalıcı-olmayan enjeksiyon + tek-yönlü Range) · ③-2 `#L123` ("resmî"den "belgesiz-kasıtlı"ya) · ④-5 Graphviz (xlink-only + img tuzağı) · ⑤-1 Dendron ("ölü"den "upstream donuk + canlı çatal"a) · ⑤-7 MarkdownDB (paket göçü + 3 ay sessizlik) · ⑤-8 SSG genellemesi (çekirdek-düzeyi forma).

**KARARSIZ (1):** ⑤-9 Cosma çıktısında `vscode://` linki — iki rapor da sınamadı; tek koşumluk deney bekliyor.

**Hakem notu:** rapor-2'nin denetlemediği 83 tez iddiası (özellikle Cosma kaynak-kodu bulguları İ-84-90, Quartz zinciri İ-91-95, MkDocs kapıları İ-96-101) adversarial testten geçmemiştir; sayısal denetçi sondajında tuttukları için karar girdisi olarak kullanılabilir ama "adversarial-hayatta-kalan" statüsü taşımazlar.

*Rapor sonu — Hakem A (maskeli, web'siz).*
