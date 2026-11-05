# Müzik keşif aracı: erişim ve keşif araştırması (atlas-1)

**AS-OF:** 2026-11-05 (tarih sistem saatinden). **Araştırmacı:** atlas. **Yöntem:** WebSearch + WebFetch; birincil sayfa okunabildiyse "okundu", yalnız arama özeti ise "özet" etiketli. Doğrulanamayan `[?]`. Sayılar kaynağındadır, kestirim yok.

## 0. Kısa hüküm

- Spotify bu tasarımın **özellik kaynağı olamaz** (audio-features, audio-analysis, recommendations, related-artists yeni uygulamalara kapalı). Yalnız çalma/kuyruk yüzeyi olarak düşünülebilir, ama Premium + 5 kullanıcı sınırı + dar uç nokta kümesi var.
- Ses analizi yerelde yapılacağı için özellik tarafı Essentia (Discogs-EffNet/MAEST) ve CLAP/MuLan-sınıfı gömmelerle kurulur; hepsi **lisansta non-commercial** (kişisel kullanım için sorun değil).
- Aday havuzu için en sağlam kaynak: MTG-Jamendo (55 bin tam parça, ses dahil) ve FMA (106 bin parça, ses dahil); ikisi de **araştırma/non-commercial** kapsamlı. Canlı önizleme için Deezer (30 sn) kullanılabilir; Apple önizleme koşulları kişisel analiz için uygun değil.
- Literatürde kapalı tipli eleştiri + kanal-ayrık gömme birleşimini tam yapan hazır araç **bulunamadı**; en yakın TalkPlay-Tools (CC-BY-NC).

## 1. Spotify Web API durumu

| Konu | Durum | Kaynak (okuma) |
|---|---|---|
| Audio Features, Audio Analysis, Recommendations, Related Artists, Featured/Category Playlists, algoritmik/editoryal çalma listeleri, çoklu-yanıtta 30 sn önizleme | 2024-11-27 ve sonrası kayıtlı yeni uygulamalar ile bekleyen uzatma talebi olmayan dev-mode uygulamalar için **erişim yok**; mevcut extended-mode uygulamalar etkilenmedi. Blog "preview_url" adını anmıyor, "multi-get yanıtlarındaki 30 sn önizleme URL'leri" diyor | https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api (okundu) |
| Dev-mode: kullanıcı sınırı | En fazla 5 kimlik doğrulanmış kullanıcı, her biri allowlist'e eklenmeli (aksi 403); uygulama sahibi Premium olmalı | https://developer.spotify.com/documentation/web-api/concepts/quota-modes (okundu) |
| Extended quota | 15 Mayıs 2025'ten beri yalnız kuruluş başvurusu; tescilli şirket, yayında servis, en az 250 bin aylık aktif kullanıcı; inceleme 6 haftaya kadar. Kişisel proje için fiilen kapalı | aynı sayfa (okundu) |
| 2026-02-06 duyuru | 11 Şubat'tan itibaren yeni dev-mode Client ID'ler: Premium şart, geliştirici başına 1 Client ID, Client ID başına 5 kullanıcı, daha küçük uç nokta kümesi. Mevcut entegrasyonlara kullanıcı/Premium/1 ID kuralları 9 Mart'ta; uç nokta kısıtı mevcutlar için ertelendi | https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security (okundu) |
| Şubat 2026 değişiklik günlüğü | Get Playback State, Get Currently Playing Track, Get User's Queue, Add Item to Queue "hâlâ mevcut" listesinde. `GET /search` limit azami 50'den 10'a, varsayılan 20'den 5'e. Çoklu-ID uçları (Get Several Tracks vb.), Artist Top Tracks, track alanlarından `popularity` ve `available_markets` kaldırıldı | https://developer.spotify.com/documentation/web-api/references/changes/february-2026 (okundu; sayfa bu uç noktaların dev-mode'a özgü olup olmadığını belirtmiyor, Migration Guide okunmadı `[?]`) |
| 2026-07-23 | Geliştirici başına Client ID sınırı 1 → 25; dev-mode kota artık geliştirici hesabı başına sayılıyor (uygulamalar arası ortak bütçe); kota aşımında 429 gövdesi `QUOTA_EXCEEDED` | https://developer.spotify.com/documentation/web-api/references/changes/july-2026 (okundu) |

Yorum: `currently-playing` ve `add-to-queue` açık görünüyor, ama Premium'lu sahip + allowlist + Spotify cihazı gerekir ve uç nokta kümesi Spotify tarafından tekrar daraltılabilir (mevcut entegrasyon kısıtı yalnız "ertelendi"). `preview_url`'ün tek-parça yanıtlarda dev-mode'da dönüp dönmediği doğrulanamadı `[?]`. Spotify'ı özellik/aday kaynağı olarak planlamak risklidir; çalma yüzeyi olarak da zorunlu değildir (bkz. §3).

## 2. Aday havuzu kaynakları

| Kaynak | Ne verir | Lisans / koşul | Canlı mı |
|---|---|---|---|
| MTG-Jamendo | 55 binin üzeri tam ses (320 kbps MP3), 195 etiket (87 tür, 40 enstrüman, 56 ruh hâli/tema); ham 30 sn ses paketi 508 GB (full), 156 GB (düşük); hazır mel-spektrogram ve Essentia özellikleri | Kod Apache 2.0, üst veri CC BY-NC-SA 4.0, her parça kendi CC lisansında (`audio_licenses.txt`); "yalnız non-commercial araştırma ve akademik kullanım" | Depo erişilebilir, okundu (https://github.com/MTG/mtg-jamendo-dataset). Güncel indirme sağlığı doğrulanmadı `[?]` |
| Jamendo API | Katalog sorgusu | Resmî koşullar: non-commercial serbest, diğerleri için lisans teklifi (licensing@jamendo.com). Aylık 35 bin istek sınırı yalnız üçüncü taraf kaynaklarda | https://devportal.jamendo.com/api_terms_of_use (özet); canlılık/güncel kota `[?]` |
| Free Music Archive (FMA veri seti) | 106.574 parça, 161 tür; small 8 bin (7,2 GiB), medium 25 bin (22 GiB), large 106 bin 30 sn klip (93 GiB), full 879 GiB; üst veri 342 MiB | Üst veri CC BY 4.0, kod MIT, ses sanatçı lisansında; "araştırma amaçlı" | Veri seti deposu okundu (https://github.com/mdeff/fma). FMA sitesinin/API'sinin 2026 durumu doğrulanamadı: yalnız 2018-2019 haberleri (satış, FMA NEXT planı) bulundu `[?]` (https://wiki.archiveteam.org/index.php/Free_Music_Archive) |
| Deezer API | Üst veri + 30 sn önizleme; "tek kısıt parçaların akışı: yalnız 30 sn önizleme" | Resmî geliştirici SSS'si; ücretli API yok; akış hakları her an değişebilir. Önizlemeyi yerelde önbellekleyip analiz etmenin ToS'a uygunluğu **doğrulanamadı** `[?]` | Canlı görünüyor (özet; https://support.deezer.com/hc/en-gb/articles/360011538897-Deezer-FAQs-For-Developers) |
| iTunes / Apple önizleme | Arama + önizleme | Apple koşulları: önizleme yalnız tanıtım amaçlı, "download on iTunes" rozeti yanında, **indirme/kaydetme/önbellekleme yok**. Yerel gömme çıkarımı için uygun değil. Sayfa arşiv belgesi (2017) | https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html (okundu); güncel durum `[?]` |
| MusicBrainz | Üst veri, ilişkiler, etiketler | Ortalama 1 istek/sn; aşımda 503; açıklayıcı User-Agent şart | https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting (özet); canlı |
| ListenBrainz | 13 API alanı (Recordings, Statistics, Popularity, Metadata, Social, Recommendations, Player vb.) | 1 çağrı/sn, 429 aşımda; User-Agent + kullanıcı jetonu | https://listenbrainz.readthedocs.io/en/latest/users/api/index.html (okundu); öneri uçlarının ayrıntısı okunmadı `[?]` |
| Last.fm API | Benzer parça/sanatçı, etiketler | Yalnız non-commercial; veri depolama üst sınırı 100 MB; atıf şart; Last.fm'den ses akışı yok | https://www.last.fm/api/tos (okundu) |
| Discogs | Üst veri | Bu turda koşulları doğrulanamadı `[?]` | `[?]` |
| AcousticBrainz | Hesaplanmış düşük/yüksek seviye ses özellikleri | Proje **sonlandırıldı** (2022-02-16 duyurusu), yalnız tek seferlik veri dökümü kaldı; üçüncü taraf yazı üst seviye tür/ruh hâli sınıflandırıcılarının güvenilmez olduğunu ve Essentia'nın bu modelleri deprecated işaretlediğini söylüyor | https://blog.metabrainz.org/?p=12333 ; https://dev.to/birrings/acousticbrainz-alternative-in-2026-the-honest-insiders-guide-28kn (özet) |

Ayrıca: Music4All-Onion (109.269 parça, 252.984.396 dinleme kaydı, CIKM 2022); lisansı doğrulanmadı `[?]` (https://zenodo.org/record/6609677). Parça ses dosyaları 30 sn önizleme kaynaklıdır (özet).

**Keşif için pratik sonuç:** yeni şarkı bulma için ana havuz MTG-Jamendo + FMA (tam yerel ses, tek seferlik indirme, kanal-ayrık gömme hesaplanabilir). Daha tanınmış müzik için yalnız Deezer 30 sn önizleme olası, hukuki yönü belirsiz. Tür çeşitliliği: Jamendo/FMA bağımsız-sanatçı ağırlıklıdır, kullanıcının zevk aralığına uyumu ölçülmedi `[?]`.

## 3. Yerel çalma

| Seçenek | Programlama yüzeyi | Windows 11 | Kaynak |
|---|---|---|---|
| mpv | JSON IPC, Windows'ta named pipe (`--input-ipc-server`); `playback-time`, `duration`, `percent-pos` özellikleri. `loadfile` append ve `end-file` olayı kılavuzun okunamayan kısmında, **doğrulanmadı** `[?]` | Evet (named pipe belgeli) | https://mpv.io/manual/stable/#json-ipc (kısmen okundu) |
| foobar2000 + foo_beefweb | REST benzeri API, Swagger tanımı, varsayılan arayüz localhost:8880; sürüm 0.10 (2025-02-28); uzak bağlantı eklenti ayarında açılmalı; now-playing yolu okunmadı `[?]` | Evet (Win 32/64) | https://www.foobar2000.org/components/view/foo_beefweb |
| mpd | Windows'ta yerel derleme, mingw-w64 çapraz derleme veya `win32/build.py` (statik EXE); resmî hazır ikili bu turda doğrulanmadı `[?]` | Derleme gerekir | https://git.pvv.ntnu.no/oysteikt/mpd/src/commit/1f5d50ccce40e138213e446e2907d1b2afe2c8b4/doc/user.rst (özet, mirror) |
| Navidrome | Subsonic API v1.16.1 (bazı istisnalarla), `getNowPlaying` destekli; macOS/Linux/Windows çalışır, MSI var | Evet | https://www.navidrome.org/docs/developers/subsonic-api (özet) |
| Jellyfin | `POST /Sessions/{id}/Playing` (`PlayNow`/`PlayNext`/`PlayLast`); 2026-01 forumda 10.11'de oturum komutlarının 204 döndüp etkisiz kaldığı bildirildi (çözüm bulunamadı) | Evet (sunucu) | https://typescript-sdk.jellyfin.org/interfaces/generated-client.SessionApiPlayRequest.html ; https://forum.jellyfin.org/t-integration-help-v10-11-session-commands-via-api-return-204-no-content-do-nothing (özet) |

**Değerlendirme (kanıta dayalı eğilim, kesin değil):** tek kullanıcı + yerel dosya için en az bileşenli yol mpv + IPC'dir: oynatma bitişi/atlama olayı aynı kanalda gelir (olay adı doğrulanmalı). Atlama ve dinleme süresi ölçümü §5 için mpv `playback-time` ile alınabilir. Navidrome/Jellyfin gerekirse çok-cihaz için sonra eklenir.

## 4. Literatür ve hazır araçlar

**Eleştiri tabanlı (critiquing) müzik önerisi**
- MusicBot (Jin vd., CIKM 2019): metin/ses sohbet, kullanıcı-başlatmalı ve sistem-önerili eleştiri. https://scholars.hkbu.edu.hk/en/publications/musicbot-evaluating-critiquing-based-music-recommenders-with-conv-2/ (özet)
- "Critiquing for Music Exploration in Conversational Recommender Systems" (Cai, Jin, Chen; IUI 2021): üç eleştiri türü, 107 katılımcılı kullanıcı çalışması. https://www.comp.hkbu.edu.hk/~lichen/download/IUI2021-Paper.pdf (özet)
- LLM tabanlı müzik eleştiri çalışmaları: aramada **bulunamadı**; 2023-2026 için ayrı arXiv taraması gerekir `[?]`.

**Metinle müzik erişimi**
- MuLan: 44 milyon kayıt (370 bin saat), iki-kule, kontrastif. https://ar5iv.labs.arxiv.org/html/2208.12415 (özet); ağırlıklar açık mı `[?]`.
- LAION-CLAP, MusCALL (kod açık, ses verisi özel), karşılaştırma çalışması (QMUL). Özet kaynak: arama sonuçları, tek tek okunmadı.
- TTMR++ (2024): LLM ile zenginleştirilmiş açıklamalar + üst veri, kod ve veri açık. https://arxiv.org/abs/2410.03264 (özet)
- TalkPlay (Doh, Choi, Nam; arXiv 2502.13713): öneriyi token üretimi sayar; parça başına 5 kip (ses, şarkı sözü, üst veri, anlamsal etiket, çalma listesi birlikte geçişi), kip başına 1024 küme. https://arxiv.org/abs/2502.13713 (özet)
- TalkPlay-Tools: SQL + BM25 + metin/ses/görsel gömme + işbirlikçi süzme + yeniden sıralama; Qwen3, CLAP, SigLIP2; lisans CC-BY-NC 4.0; resmî depo adresi doğrulanmadı (yalnız mirror) `[?]`. https://arxiv.org/pdf/2510.01698v2 (özet)

**Ses gömmeleri (yerel)**
- Essentia MTG modelleri (Discogs-EffNet, MAEST): CC BY-NC-SA 4.0, ticari için özel lisans. https://essentia.upf.edu/models.html (özet)
- 2026 karşılaştırmalı çalışmalar: https://arxiv.org/pdf/2604.23077 ; https://arxiv.org/pdf/2608.06928 (yalnız başlık/özet; sonuçlar okunmadı `[?]`).

**Kontrollü çeşitlilik**
- DPP (Chen, Zhang, Zhou; NeurIPS 2018): hızlı açgözlü MAP çıkarımı, pencereli çeşitlilik, çevrimiçi A/B testi. https://arxiv.org/pdf/1709.05135 (özet). Kanal-ayrık yapıya uyarlama: ipucunun koruduğu kanallarda çekirdek benzerliği yüksek tutulur, serbest kanallarda DPP/MMR çeşitliliği uygulanır (bu bir **tasarım önerisi**, kaynakta doğrulanmış değil).
- MMR, bandit ve sıcaklık için bu turda kaynak çekilmedi `[?]`; bilinen klasik teknikler, ama 2023-2026 müzik-özel çalışma taranmadı.

**Hazır karşılık taraması:** tam eşleşme (yerel kütüphane + CLAP + LLM eleştirisi + sonraki-şarkı yönlendirme) bulunamadı. Kısmi karşılıklar: TalkPlay-Tools (araç çağıran LLM, CC-BY-NC, GPU), Music-Recommendation-GPT (https://github.com/slxmmy999/Music-Recommendation-GPT) ve spotify-playlist-curator (https://github.com/rachel-howell/spotify-playlist-curator); ikisi Spotify/LLM metin odaklı, ses gömmesi yok (özet). Karar 119 kapısı: sıfırdan yazmadan önce TalkPlay-Tools kod tabanı incelenip kanal-ayrık gömme ve eleştiri katmanı için üstüne kurulup kurulamayacağı bakılmalı; lisansı kişisel kullanımda engel değil.

## 5. Değerlendirme (tek kullanıcı)

- **Atlama oranı** örtük geri bildirim olarak yerleşiktir: Spotify Sequential Skip Prediction Challenge (WSDM Cup 2019) skip_2 alanını kullandı; 2. yarıdaki atlama tahmininde ilk-bilinmeyen etkileşim doğruluğu ölçüt; "son eylemi tekrarla" tabanı 19. sıraya ulaştı. Veri artık indirilemez. https://www.aicrowd.com/challenges/spotify-sequential-skip-prediction-challenge (özet)
- Tek kullanıcıda örnek küçük olduğundan, aşağıdakiler **tasarım önerisidir** (kaynaklı değil, deneyle doğrulanmalı): (1) ipucu başına önce/sonra karşılaştırması: ipucundan sonraki k parçada atlama oranı, ipucu öncesi k parçaya karşı; (2) ipucu-uyum ölçütü: ipucunun korunmasını söylediği kanalda (örn. davul) gömme uzaklığının önceki parçaya göre belirli eşiğin altında kalma oranı, ve değişmesi istenen kanalda uzaklığın artma oranı; (3) kullanıcının ipucuna aykırı parçayı atlama/dinleme oranı; (4) çeşitlilik: serbest kanallarda liste içi ortalama uzaklık ve yeni-sanatçı oranı; (5) rastgele kontrol kolu: bazı turlarda eleştirisiz seçim yapıp aynı ölçüleri karşılaştırma. Kesin eşikler deneyle belirlenmeli `[?]`.
- Tek kişilik sonuçlar istatistiksel olarak zayıf olur; ölçüt ayrıntısı için yeterli güç hesabı yapılmadı `[?]`.

## 6. Güven ve sınırlar

- Yüksek güven: Spotify kısıtları (birincil sayfalar okundu), Last.fm koşulları, MTG-Jamendo/FMA lisans ve boyutları, Apple önizleme koşulları.
- Orta güven: Deezer koşulları, Essentia lisansı, Navidrome/Jellyfin/foobar2000 yüzeyleri (özet düzeyi).
- Düşük/açık: FMA ve Jamendo API'nin 2026 canlılığı, Discogs koşulları, mpv `loadfile`/olay ayrıntıları, MMR/bandit literatürü, LLM-eleştiri müzik çalışmaları, Spotify dev-mode'da tek parça `preview_url`.
- Bu rapor hukuk görüşü değildir; yasal edinilmiş dosya üzerinde yerel analiz ve Deezer önizlemesinin yerel işlenmesi için lisans metinleri ayrıca okunmalı.

## Kaynaklar

1. https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api
2. https://developer.spotify.com/documentation/web-api/concepts/quota-modes
3. https://developer.spotify.com/blog/2026-02-06-update-on-developer-access-and-platform-security
4. https://developer.spotify.com/documentation/web-api/references/changes/february-2026
5. https://developer.spotify.com/documentation/web-api/references/changes/july-2026
6. https://github.com/MTG/mtg-jamendo-dataset
7. https://github.com/mdeff/fma
8. https://devportal.jamendo.com/api_terms_of_use
9. https://www.last.fm/api/tos
10. https://support.deezer.com/hc/en-gb/articles/360011538897-Deezer-FAQs-For-Developers
11. https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html
12. https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting
13. https://listenbrainz.readthedocs.io/en/latest/users/api/index.html
14. https://blog.metabrainz.org/?p=12333
15. https://mpv.io/manual/stable/#json-ipc
16. https://www.foobar2000.org/components/view/foo_beefweb
17. https://www.navidrome.org/docs/developers/subsonic-api
18. https://typescript-sdk.jellyfin.org/interfaces/generated-client.SessionApiPlayRequest.html
19. https://arxiv.org/abs/2502.13713 ; https://arxiv.org/pdf/2510.01698v2 ; https://arxiv.org/abs/2410.03264 ; https://ar5iv.labs.arxiv.org/html/2208.12415
20. https://arxiv.org/pdf/1709.05135
21. https://essentia.upf.edu/models.html
22. https://www.aicrowd.com/challenges/spotify-sequential-skip-prediction-challenge
23. https://www.comp.hkbu.edu.hk/~lichen/download/IUI2021-Paper.pdf
