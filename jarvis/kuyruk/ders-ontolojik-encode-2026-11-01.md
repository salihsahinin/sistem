# Ders: ontolojik encode nasıl yapılır (düzeltme üzerinde öğretim) — hazırlık brifi, 2026-11-01

Üretici: Jarvis seansı `2026-10-31-jarvis`; 3 paralel tarama (teknik atlas · yöntem/kusur atlas · depo ontoloji envanteri). Öğretim yöntemi kanıtı `kuyruk/ders-dosya-mimarisi-2026-10-31.md` §1'den aynen taşınır (fading · subgoal label · self-explanation · contrasting cases · Salih yazar · ≤3 dosya/kutu · mini-ADR). Fork oturumu bu dosyayı okuyup `ogren` akışıyla başlar. Her sayı tarama çıktısından; `[?]` kestirim; AS-OF 2026-11-01. Damgalar: **D** canlı doğrulandı · **Ö** yalnız arama özeti · **H** model hafızası, doğrulanmadı.

## 0. Tanım, varsayım, kapsam
- **Ontolojik encode** = bir alanın kavramlarını (tipler), ilişkilerini (fonksiyon/önerme), kısıtlarını (aksiyom/teorem) ve olgularını makinenin işleyebileceği biçime dökmek; üç katman: sembolik (OWL/SHACL), tip-teorik (Lean), vektör (gömme). Kavram = tip eşlemesi kaynaklı sonuç değil, ders yazarının tasarım önerisi.
- Ders nesnesi = deponun kendi kanon ontolojisi: `lean/Kanon/` (makine-yüzü) · `wiki/sozluk.md` (insan-yüzü) · `ortak/akis-graf.json` + `kod/durum` (graf şeması) · `veri/baglam.sqlite` (silver) · `core/{world-model-tasarimi,sema-sikistirma,baglam-anahtar-kaydi}.md` (üç ayrı şema dili).
- Salih'in "müzikleri" sözü belirsiz sayıldı; Music Ontology kutu 1'in işlenmiş örneği olarak alındı. Başka anlam varsa fork düzeltir.

## 1. Teknik çerçeve (teknik atlas)
| Katman | İlke | Kaynak · damga |
|---|---|---|
| Sembolik | OWL 2 profilleri EL/QL/RL: ifade gücü ↔ PTIME akıl yürütme; SHACL şekille doğrular, `sh:closed` kapalı dünya | w3.org/TR/owl2-profiles, w3.org/TR/shacl · D; OWL açık ↔ SHACL kapalı karşılaştırması H |
| Sembolik | TBox (tanım) / ABox (olgu); SKOS gevşek kavram şeması; OBO Foundry 17 ilke (Open, URI space, Versioning, Textual Definitions, Naming); BFO continuant/occurrent | obofoundry.org · D; SKOS, BFO · H |
| Tip-teorik | Kavram = `structure`/`inductive`, ilişki = fonksiyon, kısıt = `theorem`; doğrulanmış EL akıl yürütücü VEL (Rocq, arXiv 2412.08739) | Ö; Lean ALC/SROIQ önbaskısı (2608.17741) şüpheli, açılmadan derse girmez |
| Vektör | OWL2Vec* (2021), kutu gömmeleri Box²EL/TransBox (EL++ kapalı), gömme sadakati (TKDE 2025, mOWL); kutu gömmesinin ifade sınırı (Neurosymbolic AI 2025) | Ö; TransE/hiperbolik H |
| LLM | OntoChat (ESWC 2024, Music Meta Ontology), OLLM (NeurIPS 2024), CQbyCQ ≈%91 · Ontogenia ≈%84 (Lippolis 2025); GraphRAG 5 bileşen (Han 2025); ontoloji-odaklı GraphRAG derlemesi yok | Ö |
| Ajan | MCP araç şeması: `inputSchema` JSON Schema 2020-12, `outputSchema` varsa uyum zorunlu, ad 1-128 ASCII tekil (spec 2026-07-28) | modelcontextprotocol.io · D |
| Örnek | Music Ontology (2007, `purl.org/ontology/mo/`): 3 düzey (editoryal · iş akışı · olay), `MusicalWork → Expression {Score, Sound, Signal}`, FOAF+FRBR+Event yeniden kullanımı; Schema.org `MusicRecording` V30.1 (2026-09-16) `recordingOf/recordedAs` tersi | motools.sourceforge.net, schema.org · D |
| Denetim | OntoClean rigidity/identity/unity (Kişi rigid, Öğrenci anti-rigid → Kişi ⊂ Öğrenci yanlış); OOPS! 406 ontoloji 143.436 pitfall: P08 eksik tanım ≈%97, P11 eksik domain/range, P13 eksik ters, P04 bağlantısız | Keet 2013 scitepress · D; OntoClean Ö |
| Yöntem | Noy-McGuinness 101 (7 adım, kapsam önce) · LOT (gereksinim→gerçekleştirme→yayın→bakım, CQ) · XD/SAMOD (CQ→SPARQL kırmızı/yeşil test) · dddlint (kod tanımlayıcısı ↔ sözlük, 0.1.x) | Ö |

## 2. Depodaki durum (envanter; hepsi komut çıktısı)
- Lean: 34 dosya, 51 `structure` · 96 `inductive` · 243 `def` · 130 `theorem`; namespace 34/34 `Kanon.<Dosya>`; ortak üst tip **yok**; 15 tip adı birden çok dosyada (`Durum Tur Ajan Karar Rol Sonuc ...`); yapılar kavram değil **kural-koşulu bayrak demeti** (Bool alanları). `Izolasyon.Ajan` 3 dal ↔ `kod/durum/src/lib.rs` `ALANLAR` 9 sabit.
- Sözlük: 127 satır, 19 `###` terim (9 kavram + 10 skill), `donduruldu (v1)`, başlık hâlâ `# Carvis Sözlüğü`; Lean pointer yok; 17 Lean tip adının 11'i sözlükte yok; ölçekleme sözlüğü (ölçek · debi · uç-birim) Lean'de 0.
- `core/` üç şema dili (bus matrix · MDL sınıf tablosu · SCD-2 anahtar kaydı), birbirine pointer 0, sözlüğe yalnız biri bağlı.
- Graf: 91 düğüm (`is` 73 · `seans` 9 · `hedef` 9), 133 kenar; JSON Schema dosyası yok; `tur: seans` Rust `enum Tur {Is, Hedef}` ve `AkisGraf.lean` dışında, string literal (`lib.rs:568`); `meta.not` mojibake; seans id 3 biçim.
- Silver: 18 tablo 12 görünüm; ilan edilen tek-sürüm yüzey `v_guncel_kayit` kanonik DB'de **yok** (tanım `silver_saglik.rs:579`, kopya DB'de); `blok_turu`, `anahtar.tur`, `zarf_tip` serbest metin, bir `zarf_tip='�'`; tarih 4 biçim; `anahtar.gecerli_bas` 397/397 boş.
- Çift adlar (sıcak katman): Carvis 247 / Jarvis 691 · kapsül 201 / pano 98 / durum · vardiya 182 / seans 629 · görev 279 / iş 244 / `is`. Tanımsız terimler: `Katman-1` 287 kullanım tanım 0 · `ölçek-eşiği` 36 · `devir birimi` 10.
- `ad-esitligi-denetim` exit 4: K1 eksik 3 dosya (`session-start.sh`, `friday/CLAUDE.md`, `agents/sokrates.md`), K2 `kod/README.md` yok; `SCRIPTLER.md:85` ikili yolu yanlış.

## 3. Plan DAG (8 kutu; sektör başlığı · kavram · kusur · düzeltme · soru)
1. **Knowledge Representation Fundamentals: Open vs Closed World** — ontoloji = TBox+ABox; Music Ontology 3 düzey işlenmiş örnek (contrasting: `MusicalWork` ↔ `Track`). Kusur: depoda insan-yüzü (sözlük) ile makine-yüzü (Lean) arasında pointer yok, iki ayrı ontoloji. Düzeltme (gösterim, Salih yazmaz): tek terim için `lean:` pointer satırı taslağı. Soru: "sözlükle ontolojinin farkı ne?"
2. **Encoding Is Physical Too: Identifiers, Dates, Bytes** — OBO URI space + Versioning; kimlik kararlılığı (anahtar-kaydı ilke 1). Kusur: `meta.not` mojibake, `zarf_tip='�'`, seans id 3 biçim, tarih 4 biçim. Düzeltme: UTF-8 düzelt (`kod/durum/src/lib.rs:604` çevresi), id kuralı `YYYY-MM-DD-<alan>[-N]`. Katman-2. Yanlış kavram: "encoding karakter seti değil anlam işidir" (ikisi de).
3. **Closed Types vs Free Strings** — enum ↔ serbest metin; MCP `inputSchema` zorunluluğu örnek. Kusur: `tur: seans` enum dışı; `blok_turu`/`anahtar.tur`/`zarf_tip` serbest. Düzeltme: `enum Tur` + `Seans`, literal'i enum'dan türet; `AkisGraf.lean:21` aynı (Lean kısmı Katman-1). Doğrulama: `cargo test -p durum`. Fading: Rust tarafını Salih yazar.
4. **Missing Definitions Are the Most Common Pitfall (OOPS! P08)** — P08 ≈%97. Kusur: `Katman-1` 287 kullanım tanım 0, `ölçek-eşiği`, `devir birimi`. Düzeltme: sözlüğe 3 tanım satırı (Katman-1: sözlük `donduruldu`, Salih imzası). Soru: "tanımsız terim neden en sık kusur?"
5. **One Concept, One Name: Terminology Linting** — dddlint kalıbı; emeklilik protokolü (anahtar-kaydı). Kusur: Carvis/Jarvis, vardiya/seans, kapsül/pano/durum, görev/iş; `ad-esitligi-denetim` exit 4. Düzeltme: K1 eksik 3 dosyaya tek satır, `kod/README.md`, `SCRIPTLER.md:85` yol; sözlük başlığı `# Jarvis Sözlüğü` (Katman-1). Doğrulama: `../target/release/ad-esitligi-denetim` exit 0. Salih tek başına yapar.
6. **Declared Surface Must Exist: Schema in Code vs Schema in Data** — conformed dimension (aynı ad + aynı domain). Kusur: `v_guncel_kayit` ilan edilmiş ama kanonik DB'de yok; `anahtar.tur` 6 değer ↔ `baglam-anahtar-kaydi.md §2` 6 başka değer, kesişim 2. Düzeltme: görünümü kanonik DB'ye taşı ya da `wiki/silver-saglik.md:8` iddiasını gerçeğe çek; tur kümesini tek enum. Katman-2 (md kısmı 1). Soru: "ilan edilen yüzey ile var olan yüzey ayrışırsa hangisi ontoloji?"
7. **Rigidity, Roles and Types (OntoClean)** — Kişi rigid, Öğrenci rol; Lean'de kavram ↔ kural-bayrağı. Kusur: 51 `structure` çoğu Bool bayrak demeti; `Ajan` 3 dal ↔ `ALANLAR` 9; 15 çakışan tip adı, üst tip yok. Düzeltme (Katman-1, Salih imzası): `Kanon/Tipler.lean` taslağı, `Durum/Tur/Ajan` tek kaynak. Salih yazar; Jarvis yalnız `lake env lean` koşar.
8. **Competency Questions and Red/Green Tests** — XD/SAMOD; CQ'suz terim arşive. Kapanış transferi: Salih görülmemiş bir dosyada (`core/ingest-semasi.md` zarf alanları) CQ yazar, kırmızı sorgu (`sqlite3 veri/baglam.sqlite`) → düzeltme → yeşil. Mini-ADR 4 satır.

Bağımlılık: 2 → 3 (fiziksel önce tip) · 4 → 5 (tanım önce ad birliği) · 3,6 → 7 (enum ve yüzey önce üst tip) · 8 en sona. 1 bağımsız.

## 4. Zayıf kanıt (derste "çıkarım" diye sunulur)
Kavram=tip eşlemesinin 2020+ kaynağı yok · 2607/2608 arXiv kimlikleri doğrulanmadı · SKOS, BFO, TransE, Protégé/ROBOT/pySHACL/HermiT hafızadan · OOPS! ilk-10 sıralaması kurulamadı (2013 verisi) · ontoloji-odaklı GraphRAG derlemesi yok · "ontology as prompt" kaynaksız · Music Ontology 2007 sürümü okundu, Music Meta Ontology ile fark incelenmedi.

## 5. Fork oturumuna devir
- Başlangıç: "seans başı, ontolojik-encode" → `ogren`; **probe** ≤12 soru §1 kavramlarından; DAG görseli yalnız istekle; kutu 1'den.
- Katman-1 kalemler (kutu 3 Lean, 4, 5 sözlük başlığı, 6 md, 7) fork'ta yazılmaz; Salih imzasıyla ana oturumda ya da devir dosyasıyla Jarvis'e gelir. `veri/baglam.sqlite` 348 MB: fork yalnız okur, yazım ana oturumda.
- Commit `git add <yol>`, karar başına ayrı commit, önek `[icra]`. Kaynak URL'leri tarama çıktılarında; bu dosyadaki adlarla aranır.
- Komşu ders: `kuyruk/ders-dosya-mimarisi-2026-10-31.md` (kutu 4 pointer disiplini bu dersin kutu 5'iyle aynı ilke).

## EK (Salih 2026-11-05): kutu 9 adayı, Music Feature Encoding for Steerable Recommendation
- Amaç: bir parçayı "davul iyi, vokal uymuyor" türü eleştirinin adresleyebileceği biçimde kodlamak (proje fikri: prompt ile sonraki şarkıyı yönlendirme).
- Üç katman: (1) sembolik şema, Music Ontology sınıfları (Track, Signal, Performance) + kapalı tipli nitelikler (tempo, ton, enstrümantasyon, vokal türü); (2) kanal-ayrık gömme, kaynak ayrıştırma (davul, bas, vokal, diğer) sonrası her kanal için ayrı vektör; (3) eleştiri şeması, serbest metin -> {koru: [...], değiştir: [...]} kapalı tipli yapı.
- Yetkinlik sorusu (kırmızı/yeşil): "davulu A parçasına yakın, vokali A parçasından uzak 5 parça getir" sorgusu şemadan cevaplanabiliyor mu.
- Durum: aday; derse girişi Salih beyanıyla.
