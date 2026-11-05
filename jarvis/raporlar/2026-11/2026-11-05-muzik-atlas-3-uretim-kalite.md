# Müzik motoru: üretim ve kalite araştırması (atlas-3)

**AS-OF:** 2026-11-05 · **Araştırmacı:** atlas · **Yöntem:** 12 web araması (standart mod), birincil sayfa açılmadı; yalnız arama özetleri okundu. Bu yüzden "doğrulandı" demiyorum, "arama özetinde görüldü" diyorum. Kaynaksız satırlar `[?]` (model hafızası, kesim öncesi, doğrulanmadı).

## 0. Özet

Önerilen yol: davul kalıbı sembolik (MIDI benzeri) üretilir, CatBoost ile ele, sesi CC0/CC-BY örneklerle çalan deterministik motor üretir. Uçtan uca ses modelleri ilk hedef için gereksiz ve lisans açısından riskli. Sembolik kısım için hazır veri var (E-GMD, GMD: CC BY 4.0). Örnek kalitesi bariyeri için nesnel ölçüt seti aşağıda (eşikler **benim önerim**, kaynaklı kabul değil).

## 1. Ses kaydı kalite bariyeri

### 1.1 Ölçütler ve araçlar

| Ölçüt | Nasıl ölçülür | Araç | Kaynak |
|---|---|---|---|
| Örnekleme hızı, bit derinliği, kanal | Başlık okuma | `soundfile`, `ffprobe` | `[?]` |
| Sahte kayıpsız (kayıplı kodekten dönüştürülmüş) | Spektrumda sert üst kesim (tipik 16-20 kHz, kodek ve bit hızına bağlı); kesim + dik düşüş birlikte aranır | fakeflac-go (GPL-3.0, 0-100 puan, yanlış negatif üretebildiği belirtilmiş) | [pkg.go.dev/fakeflac-go](https://pkg.go.dev/github.com/drichline/fakeflac-go) |
| Sahte yüksek örnekleme (44.1 kHz içeriğin 96/192 kHz diye sunulması) | Spektrogramda üst bandın boşluğu | tarayıcı tabanlı denetçiler; kendi betiğimiz | [theaudiostuff.com](https://theaudiostuff.com/tools/hires-audio-checker.md) |
| Kırpılma | Tepe ≥ 0 dBFS olan ardışık örnek sayısı | numpy | `[?]` |
| Gürültü tabanı / SNR | Vuruş öncesi ve kuyruk sonu sessiz bölgelerin RMS'i | numpy | `[?]` |
| Dinamik aralık, tepe/RMS | Tepe ile RMS farkı | pyloudnorm, numpy | `[?]` |
| Ses yüksekliği (LUFS, EBU R128), doğru-tepe (dBTP) | ITU-R BS.1770 | pyloudnorm, ffmpeg `ebur128` | `[?]` |
| Referanssız kestirim | Audiobox Aesthetics: Production Quality, Production Complexity, Content Enjoyment, Content Usefulness; PQ netlik, aslına sadakat, dinamik, frekans dengesi gibi teknik yönleri kapsar | `audiobox-aesthetics` (kod CC-BY 4.0, kısmen MIT parçalar) | [arXiv 2502.05139](https://arxiv.org/pdf/2502.05139), [HF kartı](https://huggingface.co/facebook/audiobox-aesthetics), [özet](https://www.emergentmind.com/papers/2502.05139) |

Audiobox notu: eğitimi konuşma, müzik, genel ses karışımıdır; tek vuruş davul için kalibrasyonu **bilinmiyor**. Cyanite incelemesi (2026-05 güncel) müzik üzerinde sınırlılıkları tartışıyor: [cyanite.ai](https://cyanite.ai/blog/meta-audiobox-aesthetics-review/). Bu yüzden Audiobox PQ'yu tek başına bariyer değil, **göreli sıralama** olarak kullan; eşiği kendi örnek havuzunda kalibre et (öneri, ölçülmedi).

Fréchet Audio Distance türevleri küme-düzeyi ölçüttür (dağılım uzaklığı), tek dosya bariyeri olamaz; yalnız "seçilen havuz referans havuza ne kadar yakın" kontrolü için uygun. Bu soruda kaynak bulunmadı `[?]`.

### 1.2 Profesyonel kütüphane / veri kümesi eşikleri

Arama, profesyonel örnek kütüphanelerinin yayımlanmış kabul eşiklerini **vermedi**; E-GMD yazarları 44.1 kHz, 24 bit kayıt ve MIDI ile 2 ms hizalama kullanmış ([magenta e-gmd](https://magenta.tensorflow.org/datasets/e-gmd)). Sektör eşiği olarak sunulabilecek başka rakam doğrulanamadı. Aşağıdaki set **önerim**dir; üretici-iç tutarlılık için seçildi.

### 1.3 Önerilen eşik seti (bariyer v0, ölçülmemiş öneri)

Uygulama sırası: sert eleme (S) önce, yumuşak puan (Y) sonra. Tek vuruş davul örneği için.

| # | Ölçüt | Tür | Eşik (öneri) | Gerekçe |
|---|---|---|---|---|
| 1 | Biçim | S | WAV/FLAC; ≥ 44.1 kHz; ≥ 16 bit (tercih 24 bit) | motor ve kayıpsız zincir |
| 2 | Kodek izi | S | 16-20 kHz arasında sert kesim + dik düşüş varsa ret; yalnız kesim varsa Y-uyarı | fakeflac mantığı; yanlış negatif riski var |
| 3 | Sahte yüksek örnekleme | S | Nyquist'in altında 22 kHz üstü enerji yok ve dosya hızı > 48 kHz ise ret | gereksiz dosya, sahte bilgi |
| 4 | Kırpılma | S | Ardışık 3 ve üzeri tam ölçek örnek varsa ret | sayısal bozulma |
| 5 | Doğru-tepe | S | ≤ -1 dBTP (normalize edilmiş halde) | EBU R128 pratiği `[?]` |
| 6 | Gürültü tabanı | S | Vuruş öncesi/sonrası sessizlik RMS ≤ -60 dBFS (kick/tom), ≤ -55 dBFS (hat, zil) | yazar eşiği, kalibre edilecek |
| 7 | SNR | Y | Tepe RMS - gürültü tabanı ≥ 50 dB | öneri |
| 8 | Süre ve kesilme | S | Kuyruk, sondaki 50 ms içinde -50 dBFS altına iner (kesilmemiş) | çıtlama önleme |
| 9 | DC kayması | S | Ortalama mutlak değer ≤ 0.001 | `[?]` |
| 10 | Faz/mono uyumu | Y | Stereo ise mono toplamda ≤ 3 dB kayıp | kick/snare için |
| 11 | Audiobox PQ | Y | Havuz medyanının altına düşen alt %20 elenir (mutlak sayı yok) | kalibre edilmemiş model |
| 12 | Yinelenen/benzer | S | Parmak izi aynı ise tekilleştir | `[?]` |

Bariyer geçmeyen dosya silinmez, `karantina` listesine gider (m.8 ruhu).

## 2. Örnek kaynakları ve lisanslar

- **Meadowlark factory library**: tamamı CC0; tek vuruş kick/snare/hat, davul döngüleri, SFZ/SF2 akustik kitler; katkılar CC0 şartlı. [GitHub](https://github.com/BillyDM/meadowlark-factory-library)
- **SFZ Instruments davul koleksiyonu**: CC0-1.0 olanlar (Karoryfer: Big Rusty Drums, Frankensnare, Gogodze Phu Vol II, Swirly Drums, Unruly Drums). Aynı sayfada Salamander Drumkit CC-BY-SA-3.0, DRS Kit CC-BY-4.0. Kit başına denetle. [sfzinstruments.github.io/drums](https://sfzinstruments.github.io/drums)
- **Freesound**: her yükleyici kendi lisansını seçer; sitede CC0, CC BY, CC BY-NC filtreleri var; "CC0 veya CC BY" tek filtre olarak istenmiş, varlığı doğrulanmadı. [forum](https://freegamedev.net/d/821-freesoundorg-makes-it-easier-to-find-libre-media-now). API'de lisans filtresi var mı: **doğrulanamadı** `[?]`. Davul makinesi/ROMpler örnekleri telif riski taşır uyarısı mevcut ([Freesound forum](https://freesound.org/forum/legal-help-and-attribution-questions/40001)).
- Toplama depolar (danigb/samples, oramics/sampled, HF cueharbor): lisans klasör başına; üst kaynak denetlenmeden kullanılmaz. [danigb](https://github.com/danigb/samples), [oramics](https://github.com/oramics/sampled), [cueharbor](https://huggingface.co/datasets/cueharbor/sound-library)
- **Öneri:** ilk hedefte yalnız CC0 (atıf yükü yok), ikinci kademe CC-BY. CC-BY-SA ve NC dışarıda. Hydrogen kitleri ve Freesound Datasets lisansı bu turda **doğrulanamadı**.

Kural: her örneğe `kaynak_url, lisans, lisans_sayfa_tarihi, sha256` kaydı (depo kaydı, ürün atıf listesi için).

## 3. Sembolik veri kümeleri

| Küme | Lisans | Boyut | Davul kalıbı için | Kaynak |
|---|---|---|---|---|
| Groove MIDI Dataset (GMD) | CC BY 4.0 | 13.6 saat, 1150 MIDI, 22 binden çok ölçü | **Uygun**: insan davulcu, mikro-zamanlama ve vuruş şiddeti içerir | [magenta](https://magenta.tensorflow.org/datasets/groove) |
| E-GMD | CC BY 4.0 | ~444 saat ses, 43 kit; MIDI-only ~103 MB | **Uygun** (MIDI kısmı); ses kısmı 90 GB, gereksiz | [magenta](https://magenta.tensorflow.org/datasets/e-gmd), [arXiv 2004.00188](https://arxiv.org/pdf/2004.00188) |
| GigaMIDI | HF kartı CC BY-NC 4.0, makale CC BY 4.0 (çelişki; veri lisansı HF'e göre NC) | 1.4 milyon dosya, 5.3 milyon iz; ikincil kaynağa göre izlerin ~%57'si yalnız davul (doğrulanmadı) | **Ticari amaç varsa riskli**; ifade-zenginliği sezgileri (DNVR, DNODR, NOMML) süzme için ilginç | [arXiv 2502.17726](https://arxiv.org/html/2502.17726v1), [HF](https://huggingface.co/datasets/Metacreation/GigaMIDI) |
| Lakh MIDI, Slakh, MAESTRO | **doğrulanamadı** | | MAESTRO piyano, Slakh çok-çalgı (sentetik); davul odaklı değil | `[?]` |

Öneri: GMD + E-GMD MIDI (CC BY 4.0, atıf zorunlu). Tek tür kaynak, ~444 saat içinde tekrarlı performanslar var (E-GMD, GMD'nin yeniden kaydı); eğitimde **performans bazlı bölme** şart, aksi halde sızıntı.

## 4. Sembolik üretim modelleri

Arama özetinde görülen (hepsi davul/ritim; eğitim süresi çoğunda **yok**):
- Nuttall, Haki, Jordà (NIME 2021): Transformer-XL, GMD üzerinde ritim üretimi/devamı. [nime.org](https://nime.org/proc/nime2021_33/)
- Haki ve ark. (2022): küçük transformer kodlayıcı, gerçek zamanlı davul eşlik. [zenodo](https://zenodo.org/records/7088343/files/Haki_2022__Real-Time_Drum_Accompaniment_Using_Transformer_Architecture.pdf?download=1)
- MaskBeat (arXiv 2507.03395, 2025): döngüsel davul kalıpları, 8 katman, 8 kafa, d=512; maskeli yaklaşım; eğitim donanımı özetinde yok. [arXiv](https://arxiv.org/html/2507.03395v1)
- Rölatif konum kodlamalı transformer (2105.08399): Groove Continuation, tek GPU'da yaklaşık 3-6 saat, 9.7-14.8 GB bellek. Veri GMD değil (Groove2Groove/Band-in-a-Box); **yalnız büyüklük mertebesi** için. [arXiv](https://arxiv.org/pdf/2105.08399)
- GrooVAE (Magenta, 2019) ve MidiTok eğitim süresi/veri boyutu: bu turda **kaynak bulunamadı** `[?]`. MidiTok, `Symbotunes` gibi araç kutuları var ([arXiv 2410.20515](https://arxiv.org/abs/2410.20515v1)); davul için hazır koşullu model doğrulanmadı.

Değerlendirme: dört ölçülük davul = ~16 vuruş adımı × 4 × ~9 kanal; dizi kısa (yüzlerce jeton). Mertebe tahmini: küçük (≤ 20 milyon parametre) transformer, GMD+E-GMD MIDI üzerinde tek tüketici GPU'da saatler `[?]` (kestirim, ölçülmedi). Daha basit alternatif: kural/Markov/Euclidean üretici + CatBoost'un elemesi; model gerekmeyebilir.

## 5. Üret-ve-ele (CatBoost)

Bu turda "ağaç modelle üretilmiş müzik adaylarını puanlama" için doğrudan kaynaklı örnek **bulunamadı**. Aşağıdakiler mühendislik önerisidir (kaynaksız, `[?]`):
- Öznitelikler: vuruş yoğunluğu (adım başına), kanal başına yoğunluk, senkop oranı (zayıf vuruşta onset), kick-snare ilişkisi (backbeat varlığı), tekrar/öz-benzerlik (ölçüler arası Hamming uzaklığı), çeşitlilik (Shannon entropisi), vuruş şiddeti çeşitliliği, mikro-zamanlama sapması (GMD'den ölçülen dağılıma uzaklık), polifoni (aynı anda vuran kanal sayısı), boşluk uzunluğu, tür kutusuna uzaklık.
- Gizli etiket sorunu: kalite etiketi yok. Yol: (a) GMD gerçek kalıplar = pozitif, bozulmuş (kaydırma, rastgele ekleme/silme) = negatif; bu "gerçekçilik" öğrenir, "güzellik" değil; (b) kullanıcı seçimlerinden ikili karşılaştırma (CatBoost `YetiRank`/`PairLogit` kayıp işlevleri `[?]`); (c) az sayıda elle puan.
- Risk: tür-ayrı model olmadan puanlayıcı ortalama kalıba kayar.

## 6. Deterministik ses motoru

- **DawDreamer**: Windows tam destek, VST örnekleyici/efekt barındırır, grafik kurup çevrimdışı render eder; Windows x86-64 tekerlekleri CPython 3.11/3.12 için. [PyPI](https://pypi.org/project/dawdreamer). VST3 sessiz render hatası bildirilmiş (eklenti durumu): [GitHub #195](https://www.github.com/DBraun/DawDreamer/discussions/195).
- **Pedalboard (Spotify)**: etki işleme ve dosya G/Ç; macOS/Windows/Linux. VST3 efekt yükleme var, enstrüman barındırma doğrulanmadı. [mirror](https://sourceforge.net/projects/pedalboard.mirror/), [techfeed](https://techfeed.io/entries/613ad17f443b5f43a1505377)
- SuperCollider, Rust (cpal, fundsp, kira), Rubber Band: bu turda **aranmadı** `[?]`. Öneri: örnek çalma kendi kodumuzda basit (örnek tampondan zaman damgasına göre toplama), bu tam deterministik olur; efektler (yan-zincir sıkıştırma, filtre) için Pedalboard yeter görünüyor ama yan-zincir desteği doğrulanmadı.
- Determinizm testi: aynı grafiği taze süreçte iki kez render et, örnek karmasını (sha256) karşılaştır; farklıysa sabit çekirdek, tek iş parçacığı, eklenti yerine kendi mikser.

## 7. Uçtan uca modeller (kıyas)

| Model | Lisans (arama özetinde) | Not |
|---|---|---|
| MusicGen | Kod MIT, ağırlık CC-BY-NC 4.0 | ticari kapalı | [HF tartışma](https://huggingface.co/spaces/facebook/MusicGen/discussions/8) |
| Stable Audio Open | Stability Community License; yıllık gelir ≤ 1 milyon USD için ticari kullanım (tek ikincil kaynak) | [creativeainews](https://www.creativeainews.com/articles/best-open-source-ai-music-models-2026/), [HF](https://huggingface.co/stabilityai/stable-audio-open-1.0) |
| ACE-Step 1.5 | MIT (iki ikincil kaynak) | VRAM gereksinimi doğrulanamadı |
| YuE | v1 Apache 2.0, YuE2 CC BY-NC 4.0 (tek ikincil kaynak) | |

Lisans bilgisi tek bir 2026 karşılaştırma blogundan; birincil LICENSE dosyaları açılmadı. Yerel çalışma gereksinimleri `[?]`.

Sembolik yola göre: uçtan uca model artı = ses çeşitliliği, hızlı prototip; eksi = kontrol zayıf, ölçülebilir bariyer uygulanamaz (kaynak örnek yok), tekrarlanabilirlik zayıf, lisans karışık, davul-yalnız ve tam ölçü hizası garanti değil. Kullanıcının "yalnız kaliteli kayıt, bariyer" şartıyla **bağdaşmaz**: bariyer girdi örneklerine uygulanır, modelde örnek yok.

## 8. Hazır karşılık taraması

Aramada sembolik üretim + örnek tabanlı motor + puanlayıcı üçlüsünü birlikte yapan açık kaynak proje **bulunamadı**. Yakın araç kutuları: MusPy (MIT; veri yönetimi, G/Ç, değerlendirme, ses render) ([muspy.readthedocs.io](https://muspy.readthedocs.io/)), Symbotunes ([arXiv 2410.20515](https://arxiv.org/abs/2410.20515v1)). Tek arama yapıldı; negatif sonuç zayıf kanıt. Karar 119 kapısı: sıfırdan yazılacak parçalar yalnız bağlayıcı ve bariyer; veri, kayıt, render için hazır araç kullan.

## 9. Riskler ve sınırlar

1. **Eşikler kalibre değil**: tablo 1.3 yazar önerisi; kendi havuzunda iyi/kötü örnek etiketleyip ayarlanmadan "ölçülebilir kalite" iddiası zayıf.
2. **Etiket yokluğu**: CatBoost'a "güzel" öğretecek veri yok; gerçekçilik ile beğeni karışır.
3. **Lisans ve determinizm belirsizlikleri**: GigaMIDI lisans çelişkisi, model lisansları ikincil kaynaklı, DawDreamer VST3 durum sorunu, Windows tek-GPU varsayımı doğrulanmadı.

Sınır: birincil sayfalar açılmadı; her sayı arama özetinden. Yeniden değerlendir: Audiobox sürümü, GigaMIDI lisansı, DawDreamer sürümü değişirse.
