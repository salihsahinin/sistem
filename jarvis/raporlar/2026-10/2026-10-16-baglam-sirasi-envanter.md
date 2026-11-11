# Bağlam sırası envanteri (kanon/hafıza md bölümleri), 2026-10-16

- Toplam bölüm: 162
- Tür sayıları: D=12 · K=61 · A=86 · ?=3
- Taşındı (md'de Lean pointer var): 23
- Oto rejimde D+K bölüm: 16
- Yöntem: başlık grep'i + örnekleme; tamamı okunmadı; satır aralıkları başlık satırlarından, yaklaşık.

| dosya | bölüm | satır aralığı | tür | hedef | rejim | not |
|---|---|---|---|---|---|---|
| AGENTS.md | 1 Depo=sistem, dizin/izolasyon, rol | 5 | K | taşındı: Kanon.AjanAdi, Kanon.Izolasyon | oto | md'de hâlâ gövde var; ad ölçütü Lean'de |
| AGENTS.md | 2 Salih tek karar verici, Katman-1/2 | 6 | K | Lean | oto | yetki dalı; Delegasyon ile ilişkili |
| AGENTS.md | 3 Öncelik: güncel talimat kuralı ezer | 7 | K | Lean | oto | öncelik sırası karar dalı |
| AGENTS.md | 4 Silme yasağı | 8 | K | Lean | oto | koşullu: kayıt silinmez, --force yalnız adla |
| AGENTS.md | 5 Push yalnız Salih beyanıyla | 9 | K | Lean | oto | hook zaten uyguluyor; kanarya gerekir |
| AGENTS.md | 6 Dil, commit öneki, em-dash | 10 | D | Rust | oto | commit öneki/dil/em-dash denetimi; Kanon.Commit var |
| AGENTS.md | 7 Pointer ilkesi | 11 | A | md | oto | ilke |
| AGENTS.md | 8 Rakam disiplini | 12 | K | Lean | oto | kestirim [?], AS-OF damgası koşulu |
| AGENTS.md | 9 Amaç ↔ done çelişkisi | 13 | K | Lean | oto | amaç kazanır dalı |
| AGENTS.md | 10 md.49 sınırı | 14 | K | Lean | oto | veri sınırı; hook kapsamı ayrı |
| AGENTS.md | 11 Üslup | 15 | A | md | oto | büyük harf denetimi D olabilir |
| AGENTS.md | 12 Teknik karar (Kun Chen) | 16 | A | md | oto | değer yargısı |
| AGENTS.md | 13 Hata düzeltme (Kun Chen) | 17 | A | md | oto | yöntem ilkesi |
| AGENTS.md | 14 Git + tek-yazar | 18 | K | taşındı: Kanon.ParalelOturum, Kanon.Commit | oto | pathspec/tek-yazar Lean'de |
| AGENTS.md | 15 Ajanlar arası iletişim | 19 | K | Lean | oto | protokol dalı, cc/gelen yolu |
| AGENTS.md | 16 Hook girişi | 20 | A | md | oto | mimari betimi |
| AGENTS.md | 17 Bakım ve sahiplik | 21 | A | md | oto | sahiplik tablosu, anlatı |
| AGENTS.md | 18 Tam metin pointer | 22 | A | md | oto | pointer |
| jarvis/AGENTS.md | 0 İlk kural (Salih anlaması) | 5-7 | A | md | oto | değer |
| jarvis/AGENTS.md | 1 Kimlik | 8-10 | A | md | oto | rol tanımı |
| jarvis/AGENTS.md | 2 Açık kaynak + okunabilirlik | 11-15 | A | md | oto | hareket kütüğü adımı D, kısmen |
| jarvis/AGENTS.md | 3 Oturum başı okuma sırası | 16-19 | K | taşındı: Kanon.SeansAcilis | oto | kapılar acilis-kapilari.py; pointer md'de yok, ? |
| jarvis/AGENTS.md | 4 Yetki | 20-24 | K | Lean | oto | Katman-1/2 dalı, frenler; Delegasyon ilişkili |
| jarvis/AGENTS.md | 5 Teslim usulü | 25-27 | K | Lean | oto | teslim biçimi kontrol listesi |
| jarvis/AGENTS.md | 6 Çalışma ilkeleri | 28-35 | A | md | oto | ilkeler; token bütçesi sayıları Sabitler |
| jarvis/AGENTS.md | 7 Nerede ne var | 36-38 | A | md | oto | dizin haritası |
| jarvis/AGENTS.md | 8 Bu dosyanın bakımı | 39-40 | K | taşındı: Kanon.Butce | oto | ≤80 satır/≤7 KB bütçe denetimi D; pointer md'de yok, ? |
| jarvis/core/tuzuk-v0.md | Giriş + devralınan m.1-2 (tek karar verici) | 1-14 | A | md | okuma | yetki beyanı |
| jarvis/core/tuzuk-v0.md | m.3-7 sözlük, soru eşiği, üslup, övgü yasağı | 15-19 | A | md | okuma | m.4 soru eşiği K adayı |
| jarvis/core/tuzuk-v0.md | m.8-10 silme, proof-of-work, commit | 20-22 | K | Lean | okuma | kök AGENTS ile çift; Kanon.Commit |
| jarvis/core/tuzuk-v0.md | m.11-15 BUILD, pist, flagship, CV, çalışma modeli | 26-30 | A | md | okuma | tarihli kararlar |
| jarvis/core/tuzuk-v0.md | m.16 denetim + çelişki kapısı | 34 | K | Lean | okuma | çelişki varsa önce rapor dalı |
| jarvis/core/tuzuk-v0.md | m.17-19 anayasa, durum bloğu, plan-spiral | 35-37 | A | md | okuma | m.18 üç yüz biçimi D adayı |
| jarvis/core/tuzuk-v0.md | m.20-22 pointer, bağlam ölçekleme, yasak yerleşimi | 38-40 | A | md | okuma | ilke |
| jarvis/core/tuzuk-v0.md | m.23-24 günlük-özüt yasağı, hatırlatıcı | 41-42 | A | md | okuma | yasak/ilke |
| jarvis/core/tuzuk-v0.md | m.25-27 mod yok, kılavuz, seans vizyonu | 43-45 | A | md | okuma | vizyon |
| jarvis/core/tuzuk-v0.md | m.28-29 denetim kapsamı, dosya-açıklama standardı | 46-47 | K | Lean | okuma | m.29 biçim denetimi D olabilir |
| jarvis/core/tuzuk-v0.md | m.30-32 ajan kalıcılığı, S8 yetki, S7 | 48-50 | K | Lean | okuma | karar-yetkisi çerçevesi |
| jarvis/core/tuzuk-v0.md | m.33 ayıklık testi yasak | 51 | K | Lean | okuma | yasak kuralı |
| jarvis/core/tuzuk-v0.md | m.34-36 ingest ilkesi, tez, prototip | 53-55 | A | md | okuma | m.34 Kanon.Ingest ilişkili |
| jarvis/core/tuzuk-v0.md | m.37-38 karar-modeli, lojik-çeviri ilkesi | 61-63 | A | md | okuma | ilke |
| jarvis/core/tuzuk-v0.md | m.39 deneysel-rakam disiplini | 65 | K | Lean | okuma | damga/[?] koşulu |
| jarvis/core/tuzuk-v0.md | m.40 karar-sunum protokolü | 67 | K | Lean | okuma | sunum alanları listesi |
| jarvis/core/tuzuk-v0.md | m.41 yan-oturum karar sınırı | 69 | K | Lean | okuma | Kanon.ParalelOturum ilişkili, pointer yok, ? |
| jarvis/core/tuzuk-v0.md | m.42 ajan-yetki kanunu | 71 | K | Lean | okuma | a-h maddeleri, done-çelişkisi |
| jarvis/core/tuzuk-v0.md | m.43 skill-doğum kuralı | 72 | K | taşındı: Kanon.SkillDogum | okuma | md'de pointer var |
| jarvis/core/tuzuk-v0.md | m.44 rol katmanları | 73 | K | Lean | okuma | Kanon.Delegasyon ilişkili, pointer yok, ? |
| jarvis/core/tuzuk-v0.md | m.45 zorlanabilirlik etiketi | 74 | K | Lean | okuma | etiket koşulu |
| jarvis/core/tuzuk-v0.md | m.46 koşum-emri bütünlük paketi | 76 | K | taşındı: Kanon.KosumButunluk | okuma | ajan_fren.rs uyguluyor |
| jarvis/core/tuzuk-v0.md | m.47 skill deneme-sürümü kapısı | 78 | K | taşındı: Kanon.SkillDogum | okuma | md'de pointer var |
| jarvis/core/ajan-metodolojisi.md | 1 Görev = fonksiyon | 5-12 | K | Lean | okuma | sözleşme dörtlüsü tamlığı Delegasyon'da, ? |
| jarvis/core/ajan-metodolojisi.md | 2 Hafıza = manifest | 13-20 | A | md | okuma | analoji/gerekçe |
| jarvis/core/ajan-metodolojisi.md | 3 Lojik→Kod merdiveni | 21-29 | K | taşındı: Kanon.Delegasyon | okuma | yukariCik pointer'lı |
| jarvis/core/ajan-metodolojisi.md | 4 Lider ≠ İşçi | 30-43 | K | taşındı: Kanon.Delegasyon | okuma | Kod notu satır 32 |
| jarvis/core/ajan-metodolojisi.md | 5 Şerh-adayları hükümleri | 44-50 | A | md | okuma | hüküm kaydı |
| jarvis/core/ajan-metodolojisi.md | Firstmate rolü | 51-53 | A | md | okuma | Salih beyanı, rol |
| jarvis/core/ajan-metodolojisi.md | 6/6b İcra formatı + eskalasyon | 54-68 | K | Lean | okuma | katman/eskalasyon dalı; Delegasyon kapsıyor mu ? |
| jarvis/core/ajan-metodolojisi.md | Koşum hijyeni ekleri | 69-70 | K | Lean | okuma | koşum kuralları |
| jarvis/core/baglam-anahtar-kaydi.md | 1 İlkeler | 5-16 | A | md | okuma | kanıt damgalı ilkeler |
| jarvis/core/baglam-anahtar-kaydi.md | 2 Anahtar kaydı (makine-okur) | 17-513 | D | Rust | okuma | tools/anahtar-denetim.py okur; veri tablosu |
| jarvis/core/baglam-anahtar-kaydi.md | 3 Emeklilik protokolü | 514-522 | K | taşındı: Kanon.AnahtarEmeklilik | okuma | Kod notu satır 515 |
| jarvis/core/baglam-anahtar-kaydi.md | 4 Metrikler ve eşik merdiveni | 523-536 | D | Rust | okuma | sayım metrikleri, eşikler; Sabitler ilişkili |
| jarvis/core/baglam-anahtar-kaydi.md | 5 Koşum ve bağlar | 537-543 | A | md | okuma | bağ listesi |
| jarvis/core/baglam-anahtar-kaydi.md | 6 Girmez + kör noktalar | 544-548 | A | md | okuma | sınır notu |
| jarvis/core/baglam-anahtar-kaydi.md | 7 Bedel defteri + ölçüm planı | 549-550 | A | md | okuma | bedel/plan |
| jarvis/core/deterministik-tasarim.md | 1 Kural | 5-7 | K | Lean | okuma | iş türüne göre vurgu dalı |
| jarvis/core/deterministik-tasarim.md | 2 Nerede uygulanır | 8-13 | K | Lean | okuma | iş türü tetik listesi |
| jarvis/core/deterministik-tasarim.md | 3 Nerede vurgulanmaz | 14-16 | K | Lean | okuma | daraltma dalı |
| jarvis/core/deterministik-tasarim.md | 4 Bağlı kayıtlar | 17-18 | A | md | okuma | pointer |
| jarvis/core/durum-kapsulu.md | Şu an | 8-12 | A | md | okuma | durum bilgisi |
| jarvis/core/durum-kapsulu.md | Açık borçlar | 13-17 | A | md | okuma | durum; boyut sayıları D üretilebilir |
| jarvis/core/durum-kapsulu.md | Sonraki ilk iş | 18-20 | A | md | okuma | durum |
| jarvis/core/halusinasyon-paketi.md | 0 Beş ilke | 5-11 | A | md | okuma | gerekçe |
| jarvis/core/halusinasyon-paketi.md | 1 Fren listesi | 12-29 | A | md | okuma | damgalı liste, gerekçe |
| jarvis/core/halusinasyon-paketi.md | 2 Derece formülü H | 30-56 | D | taşındı: Kanon.Halusinasyon | okuma | derece.py, Rust portta |
| jarvis/core/halusinasyon-paketi.md | 3 m.16 taraması + şerhler | 57-61 | A | md | okuma | tarama kaydı |
| jarvis/core/ingest-semasi.md | 1 Kayıt zarfı | 7-20 | D | taşındı: Kanon.Ingest | okuma | zarf geçerliliği |
| jarvis/core/ingest-semasi.md | 2 Tip kümesi | 21-33 | D | taşındı: Kanon.Ingest | okuma | tip→hedef yönlendirme |
| jarvis/core/ingest-semasi.md | 3 Triyaj | 34-42 | K | taşındı: Kanon.Ingest | okuma | triyaj sırası |
| jarvis/core/ingest-semasi.md | 4 Kaynak-doğruluk kuralı | 43-46 | A | md | okuma | event sourcing ilkesi |
| jarvis/core/ingest-semasi.md | 5 Tetikler ve bütçeler | 47-53 | D | taşındı: Kanon.Ingest | okuma | 140/200 satır eşikleri |
| jarvis/core/ingest-semasi.md | 6 Dlq | 54-57 | K | taşındı: Kanon.Ingest | okuma | DLQ kuralı |
| jarvis/core/ingest-semasi.md | 7 Çok-sekme protokolü | 58-63 | A | md | okuma | akış anlatısı |
| jarvis/core/ingest-semasi.md | 8 Ölçüm | 64-66 | A | md | okuma | ölçüm planı |
| jarvis/core/pano.md | Başlık + şablon notları | 1-8 | A | md | okuma | şablon açıklaması |
| jarvis/core/pano.md | AKTİF | 9-15 | A | md | okuma | durum kartları |
| jarvis/core/pano.md | BEKLEYEN | 16-28 | A | md | okuma | durum kartları |
| jarvis/core/pano.md | BLOKE | 29-35 | A | md | okuma | durum kartları |
| jarvis/core/pano.md | Son biten | 36-38 | A | md | okuma | tarihçe |
| jarvis/core/sema-sikistirma.md | 0 Beş ilke | 5-11 | A | md | okuma | gerekçe |
| jarvis/core/sema-sikistirma.md | 1 Matematik (formül) | 12-20 | D | Rust | okuma | Kanon.SemaSikistirma var, md pointer yok; ? |
| jarvis/core/sema-sikistirma.md | 2 Karar tablosu | 21-31 | K | Lean | okuma | bağlam sınıfı→yol; Kanon.SemaSikistirma ? |
| jarvis/core/sema-sikistirma.md | 3 Damıtma şema-dalı | 32-34 | A | md | okuma | uygulama notu |
| jarvis/core/sema-sikistirma.md | 4 m.16 taraması + ölçüm borcu | 35-38 | A | md | okuma | tarama kaydı |
| jarvis/core/skill-tetikleme-semasi.md | 0 Beş ilke | 7-13 | A | md | okuma | gerekçe |
| jarvis/core/skill-tetikleme-semasi.md | 1 Akış | 14-24 | A | md | okuma | akış özeti, d2 var |
| jarvis/core/skill-tetikleme-semasi.md | 2 Skill-tetiği bloğu (9 alan) | 25-39 | K | taşındı: Kanon.SkillTetik | okuma | alan kuralları |
| jarvis/core/skill-tetikleme-semasi.md | 3 Üç kapı | 40-44 | K | taşındı: Kanon.SkillTetik | okuma | kapiO/kapiS/kapiK |
| jarvis/core/skill-tetikleme-semasi.md | 4 Yedi yasak | 45-53 | K | taşındı: Kanon.SkillTetik | okuma | yasak 2-5 taşındı, 1/6/7 ? |
| jarvis/core/skill-tetikleme-semasi.md | 5 Sayısal alanlar | 54-56 | D | Rust | okuma | deneysel sayılar; Sabitler ilişkili |
| jarvis/core/skill-tetikleme-semasi.md | 6 m.16 taraması | 57-61 | A | md | okuma | tarama kaydı |
| jarvis/core/skill-uretim-semasi.md | 0 Beş tasarım ilkesi | 5-11 | A | md | okuma | gerekçe |
| jarvis/core/skill-uretim-semasi.md | 1 Ağaç (özet) | 12-27 | K | taşındı: Kanon.SkillKapi | okuma | hüküm fonksiyonu |
| jarvis/core/skill-uretim-semasi.md | 2 Düğüm sözlüğü K0-K3, yapraklar, bakım | 28-91 | K | taşındı: Kanon.SkillKapi | okuma | F3 evals eşiği D; script var |
| jarvis/core/skill-uretim-semasi.md | 3 Bedel-defteri | 92-101 | A | md | okuma | bedel tablosu |
| jarvis/core/skill-uretim-semasi.md | 4/4b Çelişki taraması + v1.1 eki | 102-121 | K | Lean | okuma | determinizm katmanı; SkillDogum ilişkili ? |
| jarvis/core/skill-uretim-semasi.md | 5 Ölçüm planı | 122-123 | A | md | okuma | plan |
| jarvis/core/varlik-felsefesi.md | 1 Özünde makine | 5-8 | A | md | okuma | değer |
| jarvis/core/varlik-felsefesi.md | 2 Matematik-temelli öğrenme | 9-14 | A | md | okuma | değer |
| jarvis/core/varlik-felsefesi.md | 3 Ansiklopedi | 15-17 | A | md | okuma | değer |
| jarvis/core/varlik-felsefesi.md | 4 Birincil kaynak sicili | 18-25 | A | md | okuma | sicil listesi |
| jarvis/core/varlik-felsefesi.md | 5 Kurs şeritleri | 26-29 | A | md | okuma | işletim anlatısı |
| jarvis/core/veri-muhendisligi-katmani.md | 1 Çekirdek kararlar | 5-11 | A | md | okuma | karar anlatısı |
| jarvis/core/veri-muhendisligi-katmani.md | 2 Katman eşlemesi (done-yüklemleri) | 12-21 | D | taşındı: Kanon.KatmanYuklem | okuma | bronz/silver/gold yüklemleri |
| jarvis/core/veri-muhendisligi-katmani.md | 3 Sözleşmeler (schema-as-code) | 22-27 | A | md | okuma | git'te şema, pointer |
| jarvis/core/veri-muhendisligi-katmani.md | 4 Araç kararı | 28-33 | A | md | okuma | stdlib-önce kararı |
| jarvis/core/veri-muhendisligi-katmani.md | 5 Yetkinlik haritası | 34-40 | A | md | okuma | öğrenme değeri |
| jarvis/core/veri-muhendisligi-katmani.md | 6 Süreç kuralı: her ship katman üretir | 41-45 | K | Lean | okuma | ship adımı done-yüklemi |
| jarvis/core/veri-muhendisligi-katmani.md | 7 m.16 çelişki taraması | 46-50 | A | md | okuma | tarama kaydı |
| jarvis/core/veri-muhendisligi-katmani.md | 8 Katman-1 sorular + icra borçları | 51-55 | A | md | okuma | borç listesi |
| jarvis/core/veri-muhendisligi-katmani.md | 8b T-A triyaj şiddet formülü | 56-58 | D | taşındı: Kanon.KatmanYuklem | okuma | Kod notu satır 13 |
| jarvis/core/veri-muhendisligi-katmani.md | 9 Kör noktalar | 59-60 | A | md | okuma | kayıt |
| jarvis/core/world-model-tasarimi.md | 1 Çekirdek kararlar | 5-10 | A | md | okuma | mimari anlatı |
| jarvis/core/world-model-tasarimi.md | 2 Grain + bus matrix | 11-28 | A | md | okuma | şema tasarımı, tablo |
| jarvis/core/world-model-tasarimi.md | 3 Learned world-model katmanı | 29-36 | A | md | okuma | tasarım anlatısı |
| jarvis/core/world-model-tasarimi.md | 4 x tanımı | 37-43 | ? | ? | okuma | birim veri↔bağlam tanımı, K mı A mı |
| jarvis/core/world-model-tasarimi.md | 5 Özütleme optimizasyonu | 44-56 | A | md | okuma | gerekçe |
| jarvis/core/world-model-tasarimi.md | 6 İlk ölçüm işleri | 57-63 | A | md | okuma | iş listesi |
| jarvis/core/world-model-tasarimi.md | 7 m.16 taraması | 64-70 | A | md | okuma | tarama kaydı |
| ~/.claude/CLAUDE.md | Tek bölüm (11 madde) | 1-11 | K | Lean | oto | dil, üslup, zaman, rakam, klasör=bağlam; kök ile çift |
| memory/MEMORY.md | İndeks (pointer satırları) | 1-21 | A | md | oto | harness biçimi; pointer indeksi |
| memory/arsiv-index.md | Arşiv indeksi | 1-3 | A | md | okuma | FIFO düşen satırlar |
| memory/feedback-anlatim-bicimi-dogrudan.md | Tek bölüm | 1-17 | A | md | okuma | üslup; kök md.11 ile örtüşür |
| memory/feedback-claude-md-kisa-tut.md | Tek bölüm | 1-17 | K | md (kural Lean adayı) | okuma | bütçe ≤80 satır; Kanon.Butce var |
| memory/feedback-ders-elle-pratik-adimi.md | Tek bölüm | 1-15 | K | md (kural Lean adayı) | okuma | ogren düğümünde pratik adımı koşulu |
| memory/feedback-dosya-teslimi-finder.md | Tek bölüm | 1-19 | K | md (kural Lean adayı) | okuma | teslim: tam yol+Finder; jarvis AGENTS §5 çift |
| memory/feedback-gorsel-anlatim-atifli.md | Tek bölüm | 1-15 | A | md | okuma | görsel üslup |
| memory/feedback-gorsel-kutu-ici-aciklama.md | Tek bölüm | 1-15 | A | md | okuma | görsel üslup |
| memory/feedback-gorsel-mekanizma-degil-metin-kutusu.md | Tek bölüm | 1-20 | A | md | okuma | görsel üslup, reddedilen yöntem |
| memory/feedback-icra-listesi-onaysiz-devam.md | Tek bölüm | 1-15 | K | md (kural Lean adayı) | okuma | liste bitene dek devam dalı |
| memory/feedback-ingilizce-konusma-pratigi.md | Tek bölüm | 1-21 | A | md | okuma | dil/üslup tercihi |
| memory/feedback-maliyet-tahmini-alt-model.md | Tek bölüm | 1-15 | K | md (kural Lean adayı) | okuma | tahmin yalnız alt-model; ~/.claude ile çift |
| memory/feedback-ogretim-iskeleti-ogren-sektor-basligi.md | Tek bölüm | 1-19 | A | md | okuma | ders iskeleti; ogren skill'inde |
| memory/feedback-oturum-acma-worktree-beyani.md | Tek bölüm | 1-20 | K | md (kural Lean adayı) | okuma | açılışta worktree beyanı koşulu |
| memory/feedback-parallel-sessions-keep-talking.md | Tek bölüm | 1-15 | K | md (kural Lean adayı) | okuma | canlı-oturum kontrolü; SeansAcilis ilişkili |
| memory/feedback-pr-ozeti-ste.md | Tek bölüm | 1-15 | K | md (kural Lean adayı) | okuma | PR öncesi özet koşulu |
| memory/feedback-pratik-salih-eli.md | Tek bölüm | 1-12 | K | md (kural Lean adayı) | okuma | DONE yalnız Salih beyanıyla |
| memory/feedback-quiz-dogru-cevap-rastgele-konum.md | Tek bölüm | 1-15 | D | md (kural Rust adayı) | okuma | şık konumu rastgele; ogren script'i |
| memory/feedback-rust-icra-kodu-test-degil.md | Tek bölüm | 1-14 | A | md | okuma | yöntem tanımı, geçiş ilkesi |
| memory/feedback-seans-basi-tetik-gunaydin-degil.md | Tek bölüm | 1-15 | K | md (kural Lean adayı) | okuma | tetik kalıbı; Kanon.SeansAcilis ilişkili |
| memory/feedback-ses-ekran-kaydi-onay.md | Tek bölüm | 1-17 | K | md (kural Lean adayı) | okuma | yakalamadan önce onay koşulu |
| memory/feedback-token-kisinti-yuzde30.md | Tek bölüm | 1-15 | A | md | okuma | bütçe emri; sayı Sabitler'de ? |
| memory/feedback-vurgusuz-anlatim-capslock-yok.md | Tek bölüm | 1-17 | A | md | okuma | üslup; büyük harf denetimi D olabilir |
| memory/feedback-yuzey-tercihi-secenekli.md | Tek bölüm | 1-15 | K | md (kural Lean adayı) | okuma | ham yol önce, seçenekli sunum |
| memory/project-ajan-adi-jarvis.md | Tek bölüm | 1-15 | A | md | okuma | ad kararı; Kanon.AjanAdi ilişkili |
| memory/project-ekip-lideri-ayri-repo.md | Tek bölüm | 1-15 | A | md | okuma | mimari karar kaydı |
| memory/user-bitirme-tezi-matematik-muhendisligi.md | Tek bölüm | 1-15 | A | md | okuma | kullanıcı olgusu |
| memory/user-mac-primary.md | Tek bölüm | 1-19 | A | md | okuma | description Mac diyor, MEMORY.md Windows diyor; bayat |
| memory/user-vscode-md-d2-viewer.md | Tek bölüm | 1-15 | A | md | okuma | kullanıcı olgusu |
| jarvis/.claude/rules/cc.md | Köprü kanalı kuralı | 1-13 | K | Lean | okuma | yol-koşullu cc/**; manifest kapısı, işçi bütçesi |
| jarvis/.claude/rules/ogrenme.md | Öğrenme kuralı | 1-14 | ? | ? | okuma | içeriği okunmadı; yol-koşullu |
| jarvis/.claude/rules/tools.md | Araç kuralı | 1-14 | ? | ? | okuma | içeriği okunmadı; yol-koşullu |

açık soru: (1) sema-sikistirma §1-2: Kanon.SemaSikistirma var, md'de pointer yok; taşındı mı? (2) tuzuk m.41 ve m.44 ile ParalelOturum/Delegasyon eşleşmesi pointer'sız. (3) skill-tetikleme §4 yasak 1/6/7 ve skill-uretim §4b kısmen taşındı mı? (4) ajan-metodolojisi §1 ve §6/6b Delegasyon kapsamında mı? (5) world-model §4 tür belirsiz. (6) rules/ogrenme.md ve tools.md içeriği okunmadı. (7) memory dosyaları yalnız description satırından sınıflandı; K işareti = kural adayı, dosya md kalır. (8) user-mac-primary.md description'ı MEMORY.md ile çelişiyor (bayat). (9) tuzuk maddeleri gruplu, kaba. (10) rules/*.md yol-koşullu yüklenir, oto sayılmadı. (11) jarvis/AGENTS §3 ve §8 'taşındı' işareti Lean modülü varlığına dayanır, md'de pointer yok.
