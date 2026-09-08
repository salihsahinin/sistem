# wiki/ — Jarvis'in Beyni (eski ad: Şirketin Beyni)

> **Açıklama notu:** K-012 build adım 3 çıktısı (2026-07-12). Kavram-başına LLM-wiki sayfaları (#5 ana rol, Salih teyitli; #16). Yazım standardı DENEYSEL DAMGALI (m.29) — kullanım verisiyle kalibre edilir. Kaynak desen: Karpathy LLM-wiki + v2 uzantısı (confidence/süpersede; pointer: `raporlar/2026-07-12-K013-ekosistem-arastirmasi.md`).

## Yazım standardı — sayfa şablonu (6 blok)
1. **Üst blok:** 1-2 cümle tanım · durum (GÜNCEL/BAYAT) · son-teyit tarihi · kaynaklar · kaba güven (düşük/orta/yüksek — kaç kaynak + ne kadar taze + çelişen var mı).
2. **Çekirdek:** kavram sade dille + **1 kanonik damıtılmış örnek** (Salih kuralı 07-12: ham senaryo sayfaya girmez — raporda/logda pointer'la durur; sayfaya deseni yeniden üretebilen EN KÜÇÜK hali yazılır; örnek bağlam-verimi yüksek seçilir).
3. **SOP:** "okuyucu pazartesi sabahı ne YAPAR" — adım adım prosedür (uygunsa). İleride hedef-model parametresi taşıyabilir (#17 ufku: Fable prosedür yazar, alt model uygular); İLK PARTİDE model parametresi YOK.
4. **Gotchas:** o kavramda fiilen yapılan hatalardan biriken tuzak listesi (yaşayan bölüm).
5. **Süpersede zinciri:** çelişen/güncellenen iddia silinmez — "yerini aldı: [tarih, yeni iddia]" damgasıyla işaretli durur (m.8 + çelişki kapısının wiki hali).
6. **[[wiki-link]]'ler + index kaydı** (V24 standardı; index = bu dosyanın alt bölümü, ~100 sayfaya dek yeterli).

Tempo kuralı: oturum başına 1-2 sayfa, toplu üretim yok (07-10 Salih kararı).

## Index
- [[token-x-zaman]] — iki eksenli maliyet modeli (tüzük dipnotu; farklılaşma tezinin çekirdeği)
- [[pointer-sistemi]] — m.20; özet sıcakta, detay dosyada
- [[adversarial-hayatta-kalma]] — m.40b v0.2 sağlamlık ölçütü; DARALTILDI/DÜŞTÜ kovaları (eklendi 07-22, K-019 turu)
- [[ai2ai-rapor-formati]] — ajandan-ajana rapor/emir biçim standardının derleyici sayfası (md.19-25 + m.46 + zarf disiplini; kural koymaz, adresler; eklendi 08-21, Karar 54e)
- [[sozluk]] — Carvis sözlüğü (Homebase'ten taşındı 07-15; DONDU — ekleme yalnız Salih talimatıyla, m.3)
- [[loop-engineering]] — loop kurma el kitabı (Homebase'ten taşındı 07-15)
- [[orca]] — Orca/ADE notları (Homebase'ten taşındı 07-15)
- [[kokenler-karpathy-llm-wiki]] — LLM-wiki fikrinin kökeni, Karpathy gist (taşındı 07-15)
- [[olcum-banki]] — kalıcı sayısal ölçüm defterinin kural sayfası: m.39 giriş kuralı · m.8 çürüme kuralı · uyarı-satırı sınıfı (eklendi 08-01 gece, ana-sıra)
- [[uc-register]] — üç REGISTER + kenar-başına biçim (K2-f kanon adı; eski "üç dil" süpersede; tek-IR'ın düşme gerekçesi B3; eklendi 08-03, K2 icra turu)
- [[gorsel-artefakt-dogrulama]] — SVG/HTML artefaktın okunabilirliği gözle değil bbox ölçümüyle sınanır; sessiz görsel hata sınıfı + bayat-sekme tuzağı (eklendi 08-12, staj hasadı)
- [[ingest-semasi]] — çok-sekme çıktı akışının zarf+tip+triyaj sözleşmesinin anlatımı; sözleşmenin kendisi core/ingest-semasi.md (eklendi 08-14, ingest pipeline turu; index kaydı 08-14 wiki-sayfa-yaz ilk koşumuyla tamamlandı)
- [[stokastik-dusunce]] — **EMEKLİ/RED (Salih 08-17):** stokastik entegrasyon geri alındı; sayfa artık halef ilkeyi taşır — DETERMİNİSTİK TASARIM (LLM'ler ve makineler deterministik düşünür, deterministik tasarlanır); eski içerik `kuyruk/arsiv-stokastik-dusunce-wiki-2026-08-16.md`
*(index tamlama 07-22, K-019 turu — dört sayfa taşınmış ama index'e işlenmemişti)*
- [[paralel-oturum-protokolu]] — çoklu oturumun 4 kuralı (canlı-oturum kapısı · manifest kapısı · paylaşılan kaynak/motor freni · git add -A yasağı) — Salih imzası 08-17 masa (KB-08/09/10)
- [[baglam-veri-ambari]] — bağlam VERİTABANI (operasyonel, V-1) ↔ bağlam VERİ AMBARI (analitik: aynı SQLite'ta ayrı şema/görünüm; erişim-tasarımı ayrımı; bitemporal + SCD-2 + olay↔nesne köprü) tanımı + Jarvis içerik örnekleri (olgu/boyut/mart) — 'context warehouse' dışta tanımsız, m.29 (eklendi 08-16, rapor-16-3 turu)
- [[no-mistakes]] — kod-değişikliği doğrulama pipeline'ı (review·test·lint·push·PR·CI); safe-fix ↔ insana-eskalasyon ↔ bilinçli no-op üç-sınıf ayrımı + ci-adımı/`--skip ci` ve paralel-oturum dal-değişimi gotcha'ları (eklendi 08-21, İB-04 icra turu, paralel s13)
- [[silver-saglik]] — silver temizliği = SİLME değil bayrak + güncel-görünüm (`v_guncel_*`) + tespit-damgalı kuyruk; T-Ç1..6 deterministik çelişki testleri · T-B 4 bayatlık ADAYI · T-A ön-eleme (LLM yalnız kanıt-bulucu); `tools/silver-saglik.py` + kural dosyası; ilk koşum gotcha'ları (eklendi 08-22, İB-42 icrası; Karar 58)
- [[kolon-katmani]] — SQLite yazma deposu → parquet toplu türev (gitignore) → DuckDB salt-okur; Karar 63 venv istisnası; Redshift↔Jarvis eşleme tablosu (zone map↔row group · sort key↔ORDER BY · ENCODE↔ZSTD · dist key↔yok; DEA-C01 D2-motor); k=3 ölçüm 08-29: sıcak 10,3× · byte 371× · kaybeden 0/6, soğuk ayak şerhli (eklendi 2026-08-29, İB-34 / KB-55 a)
- [[tarama-yontemleri]] — tarama yöntemi kataloğu PG ↔ SQLite EQP ↔ DuckDB/parquet ↔ rg + seçim kuralı (SEARCH-önce · dokunulan sayfa, yüzde değil · AUTOMATIC INDEX = indeks adayı · LIKE→aralık · ANALYZE hijyeni) + plan-regresyon testi (`tarama-plan.py`) (eklendi 08-22, İB-35; Karar 64)

- [[dil-secimi]] — hangi İŞ SINIFI hangi dilde (hook · CLI/veri hattı · ajan döngüsü · MCP sunucusu · dağıtılabilir ikili · konfig/şema · politika · sandbox) + üç yatay kural (nadir-dil kapısı · iki-yol parite testi · sürüm-pinli kanal) + CUE eşiği; ÖNERİ damgalı, kanon statüsü KB-64 (eklendi 08-26, seans-16 dil-seçimi atlası wf_d8cf4f3a)
- [[anakronizm-freni]] — Karar 68 (Salih 08-26): zaman-bağımlı iddia AS-OF damgasız çıkmaz; üç kanal (eski kayıt · model hafızası · konuşma) + kaynak bayatlığı; M1-M7 mekanizma seti (damga · kesim tablosu · canlı-çekim · kayıt şeması · lint · kuyruk+boşaltma · tazelik sınıfı) + Türkçe zaman-çivi listesi + SOP (eklendi 08-26, anakronizm atlası wf_9030bba4)
- [[baglam-anahtar-kaydi]] — anahtar ≠ ad: kavram/tetik/yüzey başına TEK kararlı anahtar + TEK güncel değer; emeklilik = damga+gerekçe+halef (silme yok) + sıcak katmana açık yayılım; kalıntı-referans sıcak 0 / ılık k1-k2 merdiveni; katman tek tanım (`baglam-tablo.katman_bul`); `tools/anahtar-denetim.py` SOP + izinli-kalıp gotcha'ları (eklendi 08-29, İB-04 wiki kuyruğu; kaynak core/baglam-anahtar-kaydi.md + İB-42 kalanı)
- [[ajan-metodolojisi]] — görev = tipli fonksiyon (dal-bütçesi ≤5) + hafıza = manifest (eager/lazy üç kademe) + B1-B4 lojik→kod merdiveni + lider/işçi dörtlü delegasyon sözleşmesi + model hiyerarşisi (KB-02/03) + firstmate rolü (Karar 76 E4); damıtılmış örnek `cc/gorev-2026-08-29-ib39-idempotens-atlas.md` (eklendi 08-30, İB-04 wiki kuyruğu; kaynak core/ajan-metodolojisi.md)
- [[gnhf]] — durma-koşullu (goal-loop) gece/uzun-koşum orkestratörü; Karar 84 iki-şerit kuralı (gece/sensiz→gnhf · izlenen→ayrı oturum) + Karar 76 E-1 koşullu-serbestlik (worktree ∧ yazılı bütçe ∧ push kapalı) + A3 kanıt koşumu e600a7 (eklendi 09-03, İB-04 wiki kuyruğu; kaynak cc/rapor-2026-08-03-4.md + kuyruk/senaryo-defteri.md Karar 84)
- [[lavish]] — yerel-öncelikli etkileşimli HTML artefakt editörü (lavish-axi CLI); plan/karşılaştırma/diyagram Salih'in üzerinde işaretleyip yorum bırakabildiği tarayıcı yüzeyine döner, geri bildirim ajana poll ile döner; layout-gate + Excalidraw whiteboard dönüşümü; Jarvis'te henüz kanon-koşum kanıtı yok (eklendi 09-03, İB-04 wiki kuyruğu; kaynak ~/.agents/skills/lavish/SKILL.md + cc/rapor-2026-08-03-4.md)
## Kuyruk (sonraki oturumlar)
- paralel-oturum-protokolu — vaka-1 (port çakışması 08-12) + vaka-2 (emir üstyazımı 08-15) + vaka-3 (çift-koşum 08-16) birleşik: canlı-oturum kapısı + koşum-önü manifest kapısı kural adayları (kuyruk/gelen-*-paralel-oturum-vaka-*.md); Katman-1 imza sonrası yazılır.
- veri-tablosu (V-1) — bağlam→veri tablosu v0 şeması (dosya/kayit/referans/anahtar/json_kayit + görünümler), idempotens, sorgu örnekleri; kaynak veri/README.md (08-15 kapanış hasadı).
- korelasyon-kaliciligi — dolu-satır korelasyon testi (KALICI/SEMANTİK/YAPAY): seyreklik yapaylığı ile tanımsal kopya ayrımı; kanıt `~/Desktop/repo/data-company-vehicle-scoring/analiz/feature-korelasyon-ciftler-sinif.csv` + `raporlar/seans-teslim-2026-09-04-galeri-feature-temizlik.md` (09-04 galeri hasadı; fikir V92)
- treehouse — L8 araç üçlüsünün kalan üyesi (worktree havuzu/lease; gnhf ve lavish 09-03'te wiki'ye yazıldı, treehouse kuyrukta kaldı) (08-04 L8 seans hasadı; kaynak cc/rapor-2026-08-03-4.md + teslim 08-04).
- loop-aday-yüklemi — L3 kademeli form + tekrar-birimi + loop↔skill sınırı (g23 raporu; masa kararlarından SONRA yazılır — 08-01 gece hasadı).
- indeks-aramasi — 'index seek' düzeltilmiş tanım + terim haritası (SQL Server Index Seek/Key Lookup · Postgres Index Scan/IOS/Bitmap · SQLite SEARCH↔SCAN + rowid ikinci iniş · InnoDB PK) + Jarvis erişim yolu (kök→dal→yaprak→heap: kapsül işaretçisi → silver anahtar → kayit_id → aralık; sha8 tazelik) — KB-53/54 imzası sonrası (kaynak `cc/rapor-2026-08-18-1.md` S1-S4).
- hafiza-teknik-envanteri — 'LLM hafıza yönetimi' şemsiyesi ↔ ~10 teknik × Jarvis J1-J15 eşleme matrisi — KB-43..45 sonrası (kaynak `cc/rapor-2026-08-17-2.md` S2).
- baglam-butcesi — bağlam-penceresi kategori anlamları + mutlak-token kural seti + Jarvis sondajı — KB-50..52 sonrası (kaynak `cc/rapor-2026-08-17-4.md` S1-S3).
- skill-katmanlari — proje-skill vs hesap-skill + terfi süzgeci + pointer-ilkeli skill deseni (07-23 hasadı).
- kucuk-n-eval — smoke vs sertifika ayrımı + Clopper-Pearson cebi + 3×-koşum ilacı (07-23 sayı-araştırma hasadı; kaynak cc/rapor-2026-07-23-1.md).
- rol-katmanlari (m.44) — köle ≠ üst-orkestratör ≠ domain-lider (eski ad: CEO ≠ …; emekli 08-17); aday sayfa (07-21 borcu).
- Çelişki kapısı (m.16) — sonraki oturum adayı (07-12 canlı örnekleri tazeyken); Salih notu: kontrol DAİMA dar kapsamlı, "tüm projeyi tara" yasak sınıfı.
- DONE kuralı / loop temelleri — loop verisi gelince (Salih 07-12: "beraber loop kurup düşünürken revize ederiz; bu haliyle KILAVUZ'da dursun yeter").
- İlk parti kalanı (5 kavram planı, 07-10) — tempo kuralıyla sırada.
- kesim-tablosu-ve-model-hafizasi — model-başına reliable/training kesimi, 'bilmiyorum ≠ yok', S-0 ajan vakası; kaynak veri/model-kesim.jsonl + rapor 08-26-2 A1-1/C1-2 (s16 hasadı 08-26); anakronizm-freni M2'nin ayrıntı sayfası (tempo: sonraki oturum).
- nadir-dil-kapisi — V82 kural adayı; kaynak rapor 08-26-1 S4 + B3-2 (s16 hasadı 08-26); KB-63/64 kararı sonrası yazılır.
- bakim-kk — skill bakımının kullanım-kanıtı katmanı: skill-doctor entegrasyonu + kanıt-izli öneri kuralı + kapı-uygulama zinciri; kaynak Karar 75/77 + `core/skill-uretim-semasi.md` §BAKIM + ilk çevrim raporu (s20 hasadı 08-29; tempo: sonraki oturum).
- ~~[kuyruk 09-03] `gorsellestir-skill`~~ (SKİLL SİLİNDİ, Salih 09-03 akşam; arşiv `kuyruk/arsiv/gorsellestir-skill-2026-09-03/`) — içerik sınıfı → görsel tür karar tablosu (DENEYSEL satırlar), LLM'siz kapı, CDN/offline kip; kaynak `raporlar/2026-09-03-ib77-gorsellestir-atlas.md` (İB-04 wiki 1-2/seans kuralı).
- [kuyruk 09-04] `masa-akisi` — Lavish karar masası akışı: gündem md → `tools/masa-html.py` → `.lavish/` yüzey → poll → defter Karar bloğu; kaynak `raporlar/seans-teslim-2026-09-04-karar87-damitma-cowork.md`
- [kuyruk 09-08] `hedef-sizintisi` — gün-bazlı pencerenin gün-0 sızıntısı, tek-kolon kanıt formülü P(f>0|etiket≥2)−P(f>0|etiket=0), metrik uçurumu (grupsuz AUC vs GroupAUC) ve 7 kanarya; kaynak `raporlar/seans-teslim-2026-09-08-galeri-kumeleme-dersleri-tasarim-inceleme.md` + repo `analiz/ek-bulgular-galeri-trim-tasarim-2026-09-08.md`
