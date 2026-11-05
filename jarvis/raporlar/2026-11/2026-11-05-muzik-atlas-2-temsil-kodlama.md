# Müzik atlas 2: temsil ve kodlama şeması (kaynak ayrıştırma, gömme, nitelik, sembolik şema, vektör deposu)

**AS-OF:** 2026-11-05 | **Araştırmacı:** atlas | **Yöntem:** canlı WebFetch/WebSearch; her iddia URL'li; sayfadan doğrulanamayan `[?]`. Model hafızası "kesim öncesi, doğrulanmadı" sayıldı ve rapora girmedi.
**Bağlam:** Proje A (kanal-ayrık keşif aracı, metin ipucuyla yönlendirme) + Proje B (aynı şemayla sembolik üretim). Kullanıcı: matematik mühendisliği son sınıf, CatBoost bilir, Windows 11.

## Özet karar tablosu

| Halka | Öneri | Gerekçe (tek satır) |
|---|---|---|
| Ayrıştırma | htdemucs_ft (4 stem: vocals, drums, bass, other) | MIT, Windows pip kurulumu belgeli; RoFormer ailesi SDR'de önde ama ağırlık/lisans belirsiz |
| Gömme (ses) | MERT-v1-330M ya da MuQ, stem başına | Yalnız ses; ama lisans CC-BY-NC (araştırma/yerel kullanım için uygun) |
| Gömme (metin-ses ortak uzay) | MuQ-MuLan (en yeni) ya da LAION-CLAP music (Apache-2.0) | Metin ipucunu aynı uzaya düşürür |
| Ölçülebilir nitelikler | beat_this (vuruş) + Essentia modelleri (tempo, ses cinsiyeti, enstrüman, ruh hali) + librosa | MIT / AGPL-CC BY-NC-SA lisans farkına dikkat |
| Şema | Kendi JSON şeması, JAMS ad alanlarına hizalı; sembolik tarafta MidiTok | JAMS doğrulanabilir JSON; MidiTok 11 token yöntemi |
| LLM yapılandırması | İpucu metni, sabit alanlı JSON'a (stem, nitelik, yön, şiddet) | Müzik alanında hazır örnek yok; Loop Copilot en yakın |
| Depo | sqlite-vec (ya da düz numpy matris) | 50 bin parça için brute-force yeter; hesap altta |

## 1. Kaynak ayrıştırma

**Demucs (htdemucs).**
- Sürümler: `htdemucs` (varsayılan, MusDB + 800 şarkı), `htdemucs_ft` (ince ayarlı, yaklaşık 4 kat yavaş, biraz daha iyi), `htdemucs_6s` (piyano ve gitar ekler; piyano "şu an iyi çalışmıyor"), `hdemucs_mmi`. Kaynak: https://github.com/facebookresearch/demucs
- SDR (MUSDB HQ test): HT Demucs f.t. 9.00 dB, Hybrid Demucs v3 7.7 dB (aynı kaynak).
- Lisans MIT. **Depo 1 Ocak 2025'te arşivlendi**, bakımcı Meta'dan ayrıldı; yalnız önemli hata düzeltmeleri adefossez/demucs çatalında. Yeni özellik kabul edilmiyor (aynı kaynak).
- Donanım: en az 3 GB GPU belleği, varsayılan ayarlarla yaklaşık 7 GB; 3 GB için `--segment 8`; `-d cpu` ile işlemcide çalışır. README işlemci süresini "parça süresinin yaklaşık 1,5 katı" diye verir, donanım belirtmez. GPU saniye değeri sayfada yok `[?]`.
- Windows: `python.exe -m pip install -U demucs`; torchaudio Windows desteği sınırlı, ffmpeg gerekir (aynı kaynak).
- Hesap (benim aritmetiğim, 1,5 kat varsayımıyla; donanım bağımlı): 50 bin parça x 3,5 dk = 175.000 dk ses; x1,5 = 262.500 dk, yaklaşık 4.375 saat, yaklaşık 182 gün tek işlemci hattı. `htdemucs_ft` ile 4 kat. Yani 50 bin parça için GPU fiilen şart; 5 bin parça için işlemci yaklaşık 18 gün (aynı aritmetik).

**BS-RoFormer ve Mel-Band RoFormer.**
- BS-RoFormer: eğitim verisi yalnız MUSDB18HQ olan küçük model ortalama 9,80 dB SDR, MUSDB18HQ + 500 ek şarkı ile SDX23 müzik ayrıştırma pistinde birinci. Kaynak: https://arxiv.org/abs/2309.02612
- Mel-RoFormer makalesi (ek veri yok, L=6): vokal SDR 11,21 dB (BS-RoFormer 10,78), bas ise 9,64 dB (BS-RoFormer 11,43); HDemucs vokal 8,04, ortalama 7,72. Ek veriyle BS-RoFormer ortalama 11,99 dB. Kaynak: https://arxiv.org/html/2310.01809v1 (WebSearch özeti üzerinden; tabloyu doğrudan okumadım). Not: karşılaştırılan HDemucs, htdemucs değil; doğrudan kıyas değil.
- Pratik çatı: ZFTurbo/Music-Source-Separation-Training (MIT), bs_roformer ve mel_band_roformer eğitim modelleri; eğitim yapılandırmaları A6000 48 GB için boyutlanmış, çıkarım için asgari VRAM sayfada yok `[?]`; hazır ağırlıklar ayrı belgede (`docs/pretrained_models.md`), ağırlık lisansları okunmadı `[?]`. Kaynak: https://github.com/ZFTurbo/Music-Source-Separation-Training
- Bu rapor MVSep sıralaması, 2025-26 topluluk ağırlıkları ve topluluk ağırlık lisansı için kaynak bulamadı `[?]`.

**Spleeter.** MIT kod; 2, 4, 5 stem; GPU'da "100 kat gerçek zamandan hızlı" (donanım belirtilmemiş, SDR sayfada yok); ağırlık lisansı sayfada yok `[?]`. Bakım durumu kesin değil. Kaynak: https://github.com/deezer/spleeter. Mimari olarak eski (SDR yönünden Demucs'un altında olması beklenir, bu raporda ölçüm kaynağı yok `[?]`).

**Karar.** Başlangıç htdemucs_ft: 4 kanal tam olarak kullanıcının istediği (davul, bas, vokal, diğer), Windows yolu belgeli, lisans temiz. RoFormer, vokal kalitesi kritikse ikinci aşamada denenir (ağırlık lisansı doğrulandıktan sonra).

## 2. Müzik gömme modelleri

| Model | Metin-ses ortak uzay | Boyut | Lisans | Kaynak |
|---|---|---|---|---|
| LAION-CLAP music (`music_audioset_epoch_15_esc_90.14`, HTSAT-base) | Evet | parametre sayısı sayfada yok `[?]`; gömme boyutu sayfada yok `[?]` | Depo CC0-1.0; `larger_clap_music` HF kartı Apache-2.0; checkpoint "geçici sürüm, kendi riskinle" | https://github.com/LAION-AI/CLAP , https://huggingface.co/laion/larger_clap_music |
| MS-CLAP (2022, 2023, clapcap) | Evet (ses-metin) | boyut yok `[?]`; müzik desteği sayfada doğrulanmadı `[?]` | MIT | https://github.com/microsoft/CLAP |
| MuQ-MuLan-large | Evet (İngilizce ve Çince metin) | yaklaşık 700M parametre; gömme boyutu sayfada yok `[?]` | Kod MIT, **ağırlık CC-BY-NC 4.0** | https://github.com/tencent-ailab/MuQ , https://huggingface.co/OpenMuQ/MuQ-MuLan-large |
| MuQ (yalnız ses) | Hayır | yaklaşık 300M; 24 kHz; açık sürüm MSD üzerinde eğitildi, makale sonuçlarının altında kalabilir | Kod MIT, ağırlık CC-BY-NC 4.0 | https://github.com/tencent-ailab/MuQ |
| MERT-v1-330M | Hayır (yalnız ses) | 330M, 24 katman, katman başına 1024 özellik, 24 kHz | CC-BY-NC 4.0 | https://huggingface.co/m-a-p/MERT-v1-330M |
| MusicFM (FMA ya da MSD) | Hayır (yalnız ses; vuruş, akor, yapı, ton, etiket için) | boyut yok `[?]`; 25 Hz kare hızı | MIT ve Apache-2.0 rozetleri çelişik, belirsiz `[?]` | https://github.com/minzwon/musicfm |
| Essentia Discogs-EffNet, MAEST | Hayır (yalnız ses; Discogs stil ile eğitilmiş) | boyut sayfada yok `[?]`; 16 kHz | MTG modelleri CC BY-NC-SA 4.0 (ticari için özel lisans talebi) | https://essentia.upf.edu/models.html |

- MuQ makalesi: MuQ yalnızca 0,9 bin saatlik açık veriyle önceki öz-denetimli modelleri geçer; MuQ-MuLan MagnaTagATune sıfır-atış etiketlemede SOTA (yazarlar). Kaynak: https://arxiv.org/abs/2501.01108
- **Stem düzeyinde gömme çalışmaları.** Per-stem CLAP ile geri getirme yapan bir makale bulunamadı `[?]` (arama sonucu açıkça belirtti). En yakın işler: Stem-JEPA (stem geri getirme, MUSDB18 ve MoisesDB; tek stemi hedef, diğer stemleri bağlam yapar) https://arxiv.org/pdf/2411.19806 ; COCOLA (stem-karışım uyumunu ölçen karşıt öğrenme) https://www.arxiv.org/pdf/2404.16969v4 ; PHALAR https://gladia.di.uniroma1.it/publication/2026-marincione-phalar/ (başlık ve özet düzeyi, doğrulanmadı). Çıkarım: stem başına gömme fikri literatürde yeni bir teknik değil, ama hazır "kanal-eleştirisi" aracı yok; bu boşluk şemanın kendi tasarımıdır.
- Önemli uyarı (benim çıkarımım, kaynaklı değil): ayrıştırılmış stem, karışımla eğitilmiş bir modelin dağılımı dışındadır; ayrıştırma artefaktları gömmeyi kaydırabilir. Ölçülmeli `[?]`.

**Karar.** Metin ipucu için MuQ-MuLan (ağırlık CC-BY-NC: kişisel yerel araç için sorun yok, ürünleşirse sorun) ya da ticari esneklik için LAION-CLAP music (Apache-2.0 kart). Stem başına ses gömmesi için MERT/MuQ. Hangisinin eleştiri cümlesini tek stemde daha iyi adreslediği ölçülmeden seçilemez; küçük bir iç değerlendirme (kullanıcının 50-100 parçası) önerilir.

## 3. Ölçülebilir nitelikler

- **Vuruş:** beat_this (ISMIR 2024, DBN gerektirmez), MIT kod ve ağırlık, ana modeller yaklaşık 78 MB, küçük yaklaşık 8,1 MB; `--dbn` isteğe bağlı madmom. F1 sayıları depo sayfasında yok, makale Tablo 1-3'te `[?]`. Kaynak: https://github.com/CPJKU/beat_this
- **madmom:** kod BSD, **model ve veri dosyaları CC BY-NC-SA 4.0**; README "Python 2.7 ya da 3.5+" der (eski görünüm), son sürüm tarihi sayfada yok, Windows talimatı yok. Bakım belirsiz `[?]`. Kaynak: https://github.com/CPJKU/madmom
- **Essentia:** AGPL-3.0; Windows dahil çok platformlu. Kaynak: https://github.com/MTG/essentia . Modeller: TempoCNN 256 sınıf 30-286 BPM (doğruluk sayfada yok `[?]`); ses cinsiyeti ikili (kadın/erkek), 5 gömme üstünde; enstrüman 40 sınıf MTG-Jamendo; ruh hali ikili sınıflayıcılar (agresif, mutlu, parti, rahat, üzgün); dans edilebilirlik; uyarılma/değerlik; tür 400/519 Discogs stili. Doğruluk değerleri sayfada verilmemiş `[?]`. Kaynak: https://essentia.upf.edu/models.html
- **librosa:** bu rapor için sayfa okunmadı `[?]`; tempo/enerji (RMS) gibi basit niteliklerde çıkarım olarak yeterli, ama kaynaklı doğruluk verisi yok.
- Vokal tını/tür etiketleri (örn. kırgın, kısık) için hazır etiketleyici bulunamadı `[?]`; MTG-Jamendo "mood/theme" 56 sınıf ve Essentia ses cinsiyeti en yakın seçenekler. Kanal-ayrık yaklaşım burada kazanç sağlar: vokal stemine uygulanan sınıflayıcı karışımdakinden daha az gürültülü olabilir (hipotez, ölçülmedi).
- **Lisans uyarısı:** Essentia (AGPL) + MTG modelleri (CC BY-NC-SA) + madmom modelleri (CC BY-NC-SA) + MERT/MuQ ağırlıkları (CC-BY-NC): tüm zincir yalnız ticari olmayan kullanım için güvenli; ürünleşme için lisans temizliği şart.

## 4. Sembolik ve ontolojik şemalar

- **Music Ontology:** 2006'da Giasson tarafından MusicBrainz yapısını RDF ile anlatmak için başlatıldı; DCMI sayfası 54 sınıf, 153 özellik der; Event ve Timeline ontolojileri üstüne kurulu; ikincil kaynak, resmî sayfa okunmadı `[?]`. Kaynaklar: https://msi.dublincore.org/standards/music-ontology , https://groups.google.com/g/music-ontology-specification-group/c/9GSmjW05QFE/m/INslIAJy4-8J . Music Meta (2023) Wikidata ve Music Ontology hizalamaları verir: https://ar5iv.labs.arxiv.org/html/2311.03942
- **MusicBrainz ve Wikidata müzik özellikleri:** bu rapor kendi şema belgelerini okumadı `[?]`. Değerlendirme: bunlar katalog üst verisi (sanatçı, albüm, kayıt) içindir; "davul iyi, vokal uymuyor" gibi ses-içi nitelikleri taşımazlar. Şemada yalnız kimlik bağlama alanı olarak kalmalı (çıkarım).
- **JAMS:** "A JSON Annotated Music Specification"; vuruş, akor, bölüm, etiket tipleri; resmî JSON şema, doğrulama, mir_eval çevirisi; ISC lisans. Tempo ve ton ad alanları sayfadan doğrulanamadı `[?]`. Kaynak: https://github.com/marl/jams . Öneri: şema alanlarını JAMS ad alanlarıyla eşle, stem bilgisini kendi ek alanı olarak taşı (JAMS'te stem başına zorunlu yapı olduğu doğrulanmadı `[?]`).
- **MIDI token sözlükleri (MidiTok):** 11 yöntem: REMI, REMI+, MIDI-Like, TSD, BEAT, Structured, CPWord, Octuple, MuMIDI, MMM, PerTok. Lisans türü sayfada okunamadı `[?]`. Kaynak: https://github.com/Natooz/MidiTok . Çok kanallı için MMM ve REMI+ (çok enstrümanlı) adayları; hangisinin kanal-ayrık şemaya en uygun olduğu bu raporda doğrulanmadı `[?]`.
- **Ayrık (disentangled) temsil:** EC2-VAE perde ve ritmi ayırır (https://arxiv.org/abs/1906.03626) ; akor-doku VAE (ISMIR 2020, https://alphaxiv.org/abs/2008.07122) ; Long-EC2-VAE uzun dönem (https://arxiv.org/pdf/2202.06180v1.pdf) ; Polyffusion dışarıdan akor/doku koşulu veren difüzyon, kendisi ayrık temsil değil (https://archives.ismir.net/ismir2023/paper/000026.pdf) ; ses tarafında tını/perde ayrımı (https://arxiv.org/pdf/1811.03271). Hiçbiri kanal (enstrüman) ayrımı yapmaz; ayrım faktör bazlıdır (perde/ritim/akor/doku). Bu iki eksen (kanal x faktör) şemada çarpım olarak tasarlanabilir; literatürde hazır karşılık bulunamadı `[?]`.

**Karar.** Şema iki eksenli: kanal (davul, bas, vokal, diğer) x nitelik (ölçülebilir etiketler + gömme vektörü + serbest not). Sembolik taraf (Proje B) aynı kanal listesini MIDI program/track eşlemesine bağlar.

## 5. Metin ipucunu yapılandırılmış eleştiriye çevirme

- **MusicCaps:** 5.521 klip x 10 sn (AudioSet), müzisyen yazımı serbest metin başlıklar + `aspect_list`; cc-by-sa-4.0; yalnız YouTube kimlik ve zaman damgası, sesi kendin indirirsin. Kaynak: https://huggingface.co/datasets/google/MusicCaps
- **Song Describer:** 706 kayıt, 1,1 bin insan yazımı betimleme, Creative Commons; betimleme, metinden müziğe üretim, müzik-dil geri getirme için ölçüt. Kaynak: https://arxiv.org/abs/2311.10057
- **LP-MusicCaps:** etiket listesine görev talimatı ekleyip LLM'e başlık yazdırır; MC alt kümesi 5.521 ses, 22.084 başlık. Kaynak: https://arxiv.org/pdf/2307.16372 ; https://huggingface.co/datasets/seungheondoh/LP-MusicCaps-MC
- **Düzenleme tarafı:** Loop Copilot (LLM kullanıcı girdisini yapılandırılmış veriye çevirir, Küresel Nitelik Tablosu tutar), MusicMagus (tek stem içi düzenleme), InstructME (ekle, çıkar, çıkar-ayıkla, değiştir, karıştır), Instruct-MusicGen. Kaynak: https://www.bohrium.com/paper-details/loop-copilot-conducting-ai-ensembles-for-music-generation-and-iterative-editing/922190942436327479-108628 , https://arxiv.org/html/2402.06178v3 , https://arxiv.org/pdf/2405.18386
- **Boşluk:** LLM'in serbest metin eleştiriyi (stem, nitelik, yön) JSON'a çevirmesine dair müzik alanında yayımlanmış ölçüt/veri kümesi bulunamadı `[?]` (arama sonucu açıkça bunu söyledi). Bu, Proje A için ölçülecek iç bileşendir: kullanıcının kendi ipuçlarından küçük bir etiketli küme.
- Öneri şema (benim tasarımım, kaynaklı değil): `{stem: drums|bass|vocals|other|mix, nitelik: serbest|etiket, yön: +|-|=, şiddet: 0..1, hedef_nitelik_değeri: opsiyonel}`.

## 6. Vektör deposu ve hesap

**Boyut aritmetiği** (benim hesabım; float32 = 4 bayt; stem sayısı 5 = 4 stem + karışım; parça başına zaman-ortalama tek vektör varsayımı):
- 512 boyut: 5k parça = 51 MB; 50k = 512 MB.
- 1024 boyut (MERT/MuQ tipi): 5k = 102 MB; 50k = 1,02 GB.
- Çoklu katman ya da çoklu model tutulursa doğrusal çarpılır. int8 niceleme /4 (sqlite-vec int8 ve binary vektör saklıyor: https://github.com/asg017/sqlite-vec).
- Kare düzeyinde (zaman serisi) gömme saklanırsa bu hesabın kat kat üstüne çıkar; ilk sürümde gerekmez (öneri).
- Gömme boyutları (CLAP, MuQ-MuLan) sayfalardan doğrulanamadı `[?]`; 512 yalnız örnek.

**Arama araçları:**
- sqlite-vec: pre-v1 ("kırıcı değişiklik beklenir"), Apache-2.0 ve MIT, Windows dahil; ANN belgelenmemiş (dosya listesinde IVF, DiskANN, benchmarks-ann klasörleri var, durumu doğrulanmadı `[?]`). Kaynak: https://github.com/asg017/sqlite-vec . SQLite avantajı: nitelik etiketleriyle (tempo aralığı, BPM filtresi) aynı dosyada SQL birleşimi.
- FAISS: MIT; HNSW ve niceleme; belleğe sığmayan boyuta kadar; Windows desteği sayfada yok `[?]`, conda paketleri var. Kaynak: https://github.com/facebookresearch/faiss
- LanceDB: Apache-2.0, gömülü; Windows sayfada yok `[?]`; milyar ölçeği iddiası bu kütüphane için aşırı. Kaynak: https://github.com/lancedb/lancedb
- Çıkarım: 50k x 5 = 250k vektör, 512-1024 boyutta, brute-force kosinüs aramasıyla milisaniyeler değil ama saniye altı beklenir (ölçülmedi `[?]`); ANN şart değil. Önerilen: SQLite + sqlite-vec (ya da başlangıçta düz numpy), nitelik tablosu aynı veritabanında.

## Matematik/CatBoost bağlantısı (çıkarım)

CatBoost, ölçülebilir niteliklerle (BPM, enerji, etiket olasılıkları, gömme boyut indirgemesi) kullanıcının beğeni/tepki verisi üzerinde tablo-türü model olarak kurulabilir; bu çalışma CatBoost'u müzikte kullanan kaynak aramadı `[?]`. Metin-ses kosinüs benzerliği ile CatBoost skoru birleştirilebilir; gömme ham 512-1024 boyutta CatBoost için ağır, PCA ile küçültmek makul (öneri).

## Epistemolojik not

Okunan: Demucs, ZFTurbo, MuQ, MERT, beat_this, MidiTok, Essentia, LAION-CLAP, MS-CLAP, sqlite-vec, FAISS, LanceDB, JAMS, MusicCaps, Song Describer sayfaları (WebFetch özetleri; ham sayfa değil, bir ara model özetledi). Arama özetinden gelenler (MuQ makalesi tablosu, Mel-RoFormer rakamları, Stem-JEPA, COCOLA, PHALAR, Music Ontology) ikincil. Doğrulanamayan çok sayıda boyut, doğruluk ve lisans `[?]` ile işaretli. Anlık görüntü; bir yıl içinde eskimesi beklenir.
