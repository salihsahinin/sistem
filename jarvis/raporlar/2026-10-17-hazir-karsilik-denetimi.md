# Karar 119 geriye dönük denetim: hazır karşılık tablosu (AS-OF 2026-10-17)

1. Toplam 81 satır: 59 Python aracı + 19 skill + 3 Rust aracı (baglam, durum, jarvis-hook).
2. Hükümler: kullan 5 · üstüne kur 25 · tut 40 · ? 11.
3. En büyük 3 tasarruf (arşive inecek Python satırı, "kullan" hükmü): kod-envanter.py 269 + ambar-parquet.py 240 + kosum-maliyeti.py 180 = 689 satır.
4. Üstüne kur ağırlığı: hareket-tablo 257, baglam-seyir 166, prompt-tablo 200, erisim-fts 308, erisim-vektor 313 satırı yerel ince katmana inebilir (kısmi tasarruf, ölçülmedi).
5. Tut kümesinin çoğu kanon-özgül (Karar/tüzük kuralı kodlayan denetimler, silver/gold şeması); hazır karşılık bulunamadı.

Yöntem: araç adı ve işlevi, dosya başı docstring'inden (ilk 15 satır); skill'ler `.claude/skills/README.md` kataloğundan; Rust araçları `kod/` dizin adı + `tools/SCRIPTLER.md` satırından. Claude Code belge sayfaları bu oturumda canlı açıldı: memory, hooks, skills, statusline, costs, monitoring-usage, workflows (7 sayfa). Hüküm "kullan/üstüne kur" olan Claude Code satırları bu sayfalara dayanır. "OSS" (ripgrep, duckdb, tokei, dbt, git) ve Anthropic skill eşleşmeleri canlı doğrulanmadı, yalnız ad ve işlev eşleşmesi; hükmün yanında "(OSS-d)" yoksa Claude Code belgesine dayanır. Uyarı: hüküm işlev eşleşmesidir; fark testi yapılmadı, "kullan" hükmü arşive inmeden önce çıktı eşdeğerliği ölçülmeli.

Kısaltmalar URL sütununda: CC = https://code.claude.com/docs/en/

| ad | tür | ne yapar | hazır karşılık | URL | hüküm | not |
|---|---|---|---|---|---|---|
| kod-envanter.py | araç | repo dil envanteri + araç zinciri + başlangıç gecikmesi | tokei / scc (kod satır sayacı) | https://github.com/XAMPPRocky/tokei | kullan | (OSS-d) gecikme ölçümü tek seferlik; arşive |
| ambar-parquet.py | araç | SQLite tablolarını parquet'e yazar | DuckDB `COPY ... TO parquet` | https://duckdb.org/docs/stable/data/parquet/overview | kullan | (OSS-d) tek SQL ifadesi |
| kosum-maliyeti.py | araç | transkript usage'tan token/maliyet tablosu | `/usage`, statusline `cost`, OTel `claude_code.cost.usage` + `api_request` | CC costs, CC monitoring-usage | kullan | skill-esik'in v_skill_kosum girdisi denetlenmeli |
| verify-push.py | araç | çalışma ağacı ile origin eşitliğini doğrular | `git fetch` + `git diff origin/main` | https://git-scm.com/docs/git-diff | kullan | (OSS-d) 74 satır, git ile aynı |
| yol-tasi.py | araç | metin dosyalarında eski mutlak yolları değiştirir | sed / ripgrep -l (Karar 101 taşıması bitti) | https://github.com/BurntSushi/ripgrep | kullan | (OSS-d) tek seferlik göç aracı |
| hareket-tablo.py | araç | transkript araç çağrılarını bronz/silver/günlüğe indirir | transkript + OTel `tool_result` olayı + PostToolUse hook | CC monitoring-usage, CC hooks | üstüne kur | repoya okunur günlük kuralı yerel ince katman |
| baglam-seyir.py | araç | transkript usage'tan bağlam kompozisyonu, 128K uyarısı | `/context`, statusline context alanları, `prompt_cache` nesnesi, OTel token türleri | CC statusline, CC costs | üstüne kur | 128K uyarısı statusline'a; gold görünümler yerelde kalır |
| prompt-tablo.py | araç | Salih prompt'larını bronz-silver-gold hattından geçirir | OTel `user_prompt` olayı, UserPromptSubmit hook, `/insights` | CC monitoring-usage, CC hooks | üstüne kur | olay kaynağı hazır; tablo/gold yerel |
| masa-uret.py | araç (skill betiği) | spec'ten DaisyUI karar masası HTML üretir | Artifact aracı + `lavish` skill | https://claude.ai (Artifact tool, ortam içi) | üstüne kur | doğrulama + determinizm yerel; yüzey hazır |
| masa-uret-test.py | araç (skill betiği) | masa-uret için E1-E3 determinizm testi | masa-uret'e bağlı | — | üstüne kur | masa-uret kararını izler; "yeni birim testi yok" kuralı |
| masa-spec-cikar.py | araç (skill betiği) | eski masa HTML'inden spec JSON çıkarır | yok | — | tut | eşdeğerlik testi aracı; masa-uret ile birlikte karar |
| masa-html.py | araç | masa gündemi md'sini Lavish HTML'e çevirir | Artifact aracı + `lavish` skill | ortam içi | üstüne kur | masa-uret ile örtüşüyor; birleştirme adayı |
| sunum-son50.py | araç | son 50 prompt CSV'sinden tek dosya HTML sunum | Artifact aracı, `artifact-design` skill | ortam içi | üstüne kur | veri hazırlığı yerel, sayfa Artifact |
| sunum-proof-of-work.py | araç | git + dosyadan geliştirme kanıt sunumu HTML | Artifact aracı | ortam içi | üstüne kur | rakamlar git'ten; sayfa üretimi hazır |
| erisim-fts.py | araç | SQLite FTS5 + bm25 arama ve yerel eval | SQLite FTS5 (zaten temel); ripgrep alternatif | https://sqlite.org/fts5.html | üstüne kur | (OSS-d) zaten hazır üstünde; ince katman |
| erisim-vektor.py | araç | FTS5 eval'ine vektör + RRF kolu ekler | sentence-transformers, DuckDB vss | https://duckdb.org/docs/stable/core_extensions/vss | üstüne kur | (OSS-d) ölçüm kolu; üretim yolu değil |
| erisim-kalibrasyon.py | araç | arama genişletme ağırlığı kalibrasyonu | yok | — | tut | yerel veri kümesine özgül |
| tarama-plan.py | araç | SQLite EXPLAIN QUERY PLAN regresyon testi | SQLite `EXPLAIN QUERY PLAN` (yerleşik) | https://sqlite.org/eqp.html | üstüne kur | (OSS-d) komut hazır; regresyon sarmalı yerel |
| tarama-plan-duckdb.py | araç | DuckDB/parquet plan sınıfı denetimi | DuckDB `EXPLAIN` | https://duckdb.org/docs/stable/guides/meta/explain | üstüne kur | (OSS-d) tarama-plan'ın kardeşi |
| kolon-olcum.py | araç | SQLite ile DuckDB sorgu süre/byte ölçümü | DuckDB `EXPLAIN ANALYZE`, hyperfine | https://duckdb.org/docs/stable/dev/profiling | ? | karar araştırması bitmiş mi bilinmiyor; Salih'e sor |
| katman-hatti.py | araç | silver/gold'u bronz'dan sabit sırayla yeniden üretir | dbt (DAG + yeniden kurma) / make | https://docs.getdbt.com | ? | dbt-duckdb gerekirdi; yerel hat 220 satır, kazanç belirsiz |
| katman-olcum.py | araç | veri testi + freshness + şekil sözleşmesi | dbt tests / source freshness | https://docs.getdbt.com | ? | dbt kurulu değil; yerel kanon kurallarıyla iç içe |
| baglam-tablo.py | araç | bağlamı SQLite/jsonl/csv veri tablosuna çevirir | yok (kanon-özgül şema) | — | tut | 1019 satır; tüm hattın kökü |
| silver-saglik.py | araç | silver bayrak, güncel görünüm, tespit damgası | yok | — | tut | kanon kurallarına (Karar 58) özgül |
| silver-saglik-kalibrasyon.py | araç | silver-sağlık sabit kalibrasyonu | yok | — | tut | yerel eşiklere özgül |
| bag-tablo.py | araç | tipli bağ tablosu (süpersede ilk adım) | yok | — | tut | kanon ilişki tipleri yerel |
| deneyim-tablo.py | araç | epizodik deneyim katmanı | yok | — | tut | Karar 60 şerhine özgül |
| ta-triyaj.py | araç | T-A önelemesi aday çiftlerini katmanlı eler | yok | — | tut | silver-saglik'e bağlı yerel mantık |
| asof-eval.py | araç | silver güncel yüzeyini ham ile karşılaştırır | yok | — | tut | yerel eval; hazır karşılık yok |
| anakronizm-denetim.py | araç | AS-OF damgasız zaman-bağımlı iddiaları yakalar | yok | — | tut | Karar 68 kanon kuralı |
| bayat-cekim.py | araç | bayatlık kuyruğunu 90 gün eşiğiyle boşaltır | yok | — | tut | kanon politikası (KB-68) |
| karantina.py | araç | bayat dosyayı silmeden karantinaya taşır | yok | — | tut | silme yasağı (m.8) yerel |
| anahtar-denetim.py | araç | emekli anahtar kalıntılarını md'de tarar | ripgrep + anahtar kaydı regex'leri | https://github.com/BurntSushi/ripgrep | üstüne kur | (OSS-d) tarama rg; kayıt yerel |
| anahtar-cascade.py | araç | emekli anahtarı açık yeniden yazımla yayar | sed / rg + kayıt | ripgrep | üstüne kur | (OSS-d) kayıt ve onay kapısı yerel |
| pointer-kayma.py | araç | `dosya:satır` pointer kaymasını yakalar | lychee yalnız URL/dosya var mı bakar, satır bakmaz | https://github.com/lycheeverse/lychee | tut | (OSS-d) satır düzeyi karşılık yok |
| pointer-graf.py | araç | pointer grafını silver'dan türetir | yok | — | tut | yerel silver şemasına bağlı |
| wiki-baglanti.py | araç | `[[link]]` grafı + karşı-link geri güncelleme | Obsidian backlinks (kullanımda) | https://obsidian.md | ? | geri güncelleme (yazma) Obsidian'da var mı bilinmiyor |
| obsidian-harita.py | araç | Obsidian bağlantı haritası üretir | Obsidian graph view | https://obsidian.md | ? | çıktı biçimi neye gidiyor bilinmiyor |
| kural-envanter.py | araç | kural envanteri + deterministik kümeleme | `InstructionsLoaded` hook, `/memory` yalnız yüklenenleri listeler | CC hooks, CC memory | tut | kümeleme yok; yüklü listesi ayrı iş |
| baglam-skill-aday.py | araç | md bölümlerini skill/rules adayı olarak skorlar | yok (belge yalnız taşıma öneriyor) | CC costs | tut | skor aracı hazır değil |
| skill-butce.py | araç | skill description karakter bütçesini ölçer | `/context` skill payını gösterebilir | CC costs | ? | `/context` karakter bütçesini veriyor mu doğrulanmadı |
| kapi-denetim.py | araç (skill betiği) | skill kapı-ağacı: referans var mı, biçim | skill-creator, `/skill-doctor` | CC skills | ? | araç tanımında anıldı, belge sayfası açılmadı |
| devir-md2json.py | araç | md emirdeki lojik bloktan devir json'u türetir | yok | — | tut | A1 emir biçimi yerel |
| devir-ani.py | araç | devir anı yüklemini yalnız loglar | yok | — | tut | ölçüm aygıtı, kanon yüklemi |
| alan-ajani-dogur.py | araç | spec'ten alan ajanı dizini + doğum belgesi | plugin/subagent iskeleti yok kanon belgesi için | CC skills | tut | doğum belgesi kanon-özgül |
| buyuk-harf-temizle.py | araç | tamamı büyük harfli sözcük kuralını temizler | markdownlint böyle kural içermez (OSS-d) | https://github.com/DavidAnson/markdownlint | tut | kuru diff'li yerel kural |
| tuzuk-iz-tarama.py | araç | tüzükte SÜPERSEDE/REVİZE izlerini sayar | yok | — | tut | tüzüğe özgül |
| kod-orani-olcum.py | araç | md/kod oranı ile bağlamda okunan oranı | tokei + transkript | tokei | tut | tek seferlik baseline; sonuç bitmiş olabilir |
| yuzey-parmak-izi.py | araç | oturumun yüzey ve yetki parmak izini basar | `/status`, SessionStart hook girdisi | CC hooks | ? | yetki seti eşitliği için alan yeterli mi doğrulanmadı |
| headless-esleme.py | araç | iş sınıfı yüzey eşleme taslağı | yok | — | tut | tek seferlik taslak; kanon kararı |
| gnhf-izle.py | araç | gnhf ajan akışını canlı izler | `/workflows` ve görev paneli yalnız Claude Code işleri için | CC workflows | ? | gnhf üçüncü parti; Claude Code görünümü onu kapsamaz |
| olcum-dortlu.py | araç | gnhf log + no-mistakes state ölçümü | yok | — | tut | iki yerel aracın içine bağlı |
| denetci-kalibrasyon.py | araç | denetçi kalibrasyon harness'i | yok | — | tut | md.28 etiketli sete bağlı |
| d2-eval.py | araç | LLM d2 üretim/okuma doğruluğu eval'i | d2 derleyicisi (zaten kullanıyor) | https://d2lang.com | tut | eval harness'i yerel |
| loop-dedektor.py | araç | araç-çağrı dizilerinde döngü yakalar | yok (hook'la yazılabilir, hazır değil) | CC hooks | tut | kural-tabanlı yerel eşikler |
| pano-akis.py | araç | Kanban WIP/throughput/cycle time | yok | — | tut | pano şablonu yerel |
| karar-borcu-tablo.py | araç | açık karar borcu jsonl'ini tabloya yükler | yok | — | tut | defter şeması yerel |
| atlas-derle.py | araç | Workflow ham çıktısını mekanik rapora derler | `/workflows` görünümü + script dosyası `~/.claude/projects/` altında | CC workflows | ? | journal biçimi belgede yok; `/deep-research` raporu da var |
| ambar-tablo.py | araç | amb_ önekli bağlam veri ambarı v0 | yok | — | tut | baglam-tablo ile aynı şema ailesi |
| atlas-kosum | skill | araştırmayı alan ailelerine bölüp tez/antitez/hakem | `/deep-research` yerleşik workflow, `deep-research` skill | CC workflows | üstüne kur | diyalektik (m.40b) yerel; çok kaynaklı doğrulama hazır |
| karar-masasi | skill | bekleyen hükümleri karar masası HTML yapar | Artifact aracı + `lavish` skill | ortam içi | üstüne kur | spec/determinizm yerel, yüzey hazır |
| celiski-kapisi | skill | karar öncesi kanonda çelişki tarar (m.16) | yok | — | tut | kanon-özgül |
| damitma | skill | kuyruğu ingest triyajından geçirir, sıcak dosyayı bütçeye indirir | yok | — | tut | kanon-özgül |
| gorev-emri-derleme | skill | beyanı künyeli ajan emrine derler | yok | — | tut | emir şablonları yerel |
| halusinasyon-engelleyici | skill | H derecesi + doğrulama zinciriyle üretir | `/deep-research` doğrulama oylaması | CC workflows | tut | formül (Kanon.Halusinasyon) yerel; yöntem benzer |
| karar-hatti | skill | karar orkestratörü, çocuk skill zinciri | yok (skill'ler skill çağırabilir) | CC skills | tut | zincir kanon sırası |
| karar-kaydet | skill | kararı deftere standart blokla yazıp commit'ler | yok | — | tut | defter biçimi yerel |
| karar-modeli | skill | 3 matematik temelli karar modeli sunar | yok | — | tut | Salih'in seçenek biçimi |
| lojik-ceviri | skill | kuralı Lean 4 koduna çevirir | yok | — | tut | Lean kanon ölçütü |
| pipeline-kosum | skill | manifest + emir ile disk-durumlu pipeline yürütür | dynamic workflows (resume, `/workflows`, `meta`+`phase`) | CC workflows | üstüne kur | belge: betik tabanlı, yeniden başlatılabilir; manifest yerel |
| seans-acilis | skill | seans açılış ritüeli + kapılar | SessionStart hook (`additionalContext`, `initialUserMessage`), CLAUDE.md `@import` | CC hooks, CC memory | üstüne kur | kapı betiği yerel; yükleme hazır |
| seans-kapanis | skill | teslim raporu, hasat, ingest, kapsül, commit | SessionEnd/Stop hook, oto-hafıza | CC hooks, CC memory | üstüne kur | push kuralı (m.9) yerel; tetik hazır |
| sinav-grill | skill | Salih'i adversarial Sokratik sorguyla sınar | `grill-me` skill (Anthropic) | ortam içi | üstüne kur | [S]/[O]/[T] haritası, yalnız Salih tetiği yerel |
| skill-kapisi | skill | skill adayını kapı ağacından geçirir | `skill-creator` skill | ortam içi | üstüne kur | K0-K3 kanon kapıları yerel |
| wiki-sayfa-yaz | skill | wiki-delta'dan 6 bloklu sayfa üretir | yok | — | tut | wiki standardı yerel |
| yol-planla | skill | (durum,zaman) düğümlü yol planı bloğu üretir | plan modu (Shift+Tab), Plan alt-ajanı | CC costs | üstüne kur | maliyet tavanı + onarım kuralı yerel |
| ogren | skill | dört fazlı ders akışı PROBE-PLAN-TEACH-CLOSE | yok | — | tut | Salih öğrenme protokolü |
| emekli-anahtar-cascade | skill | anahtar kaydı + yayılım (anahtar-cascade.py) | anahtar-cascade'e bağlı | — | üstüne kur | araç kararını izler |
| baglam (Rust) | araç | `@` ağacını yükleme sırasıyla genişletir/denetler | CLAUDE.md `@import` + `InstructionsLoaded` hook | CC memory, CC hooks | üstüne kur | yükleme hazır; `denetle` doğrulaması yerel kalabilir |
| durum (Rust) | araç | ortak durum tablosu: aç/al/bitir/tüket | agent teams paylaşımlı görev listesi, TaskCreated/Completed hook | CC costs, CC hooks | ? | oturumlar arası kütük; Claude Code görev listesi kapsamı belirsiz |
| jarvis-hook (Rust) | araç | hook gövdeleri: prompt-dosya seçimi, paket yönlendirme | hooks mekanizmasının kendisi | CC hooks | üstüne kur | zaten hook üstünde; seçim mantığı yerel |

açık soru: (1) `kolon-olcum`, `katman-hatti`, `katman-olcum` için dbt/DuckDB değerlendirmesi ayrıca yapılsın mı (OSS canlı doğrulanmadı)? (2) `skill-butce`, `kapi-denetim` için `/context` ve `/skill-doctor` çıktısı bu makinede denensin mi? (3) `durum` kütüğü ile Claude Code görev listesi/oturumlar arası mesajlaşma örtüşmesi için `cross-session-messaging` ve `agent-teams` sayfaları açılsın mı?
