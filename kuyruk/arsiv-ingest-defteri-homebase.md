> **TAŞINDI (2026-07-15, Salih icra emri):** Homebase'ten JARVIS'e — köken: `Cowork Homebase/[C] Jarvis Ingest Defteri.md`; tespit raporu: `raporlar/homebase-tasima-tespiti-2026-07-15.md`. Orijinal Homebase'te arşiv-pointer'la durur (m.8).

# [C] Jarvis Ingest Defteri

**Ne bu:** Her end-of-day'de oturumdan çıkarılan KALICI dersler/özütler (log = ne oldu; burası = ne öğrenildi). Kural (Salih, 2026-07-09 gece): "her end-of-day'de en azından temel düzeyde ingest" — v0 formatı: 3-5 özüt · tarihli · kaynaklı (hangi oturum/olay). İleride geliştirilecek (havuz #7 bilimsel ingest algoritması + #16 wiki hattı bunun üst-ufku). Statü: dosya-tabanlı bağlam zenginliği — ŞİMDİLİK BUILD YOK ile çelişmez.

**İşleme kuralı:** Özüt = tek paragraf, tekrar kullanılabilir ders (kural adayı, davranış verisi, operasyon dersi, desen). Ham olay anlatımı log'a, ders buraya. Otomatik silme yok; birleştirme Salih kararıyla.

---

## 2026-07-09 (gece oturumu — ilk ingest)

1. **[operasyon] OneDrive↔mount senkron yarışı commit bozar.** Host-tarafı edit sonrası mount kesik snapshot görebiliyor (dosya kuyruğu kayıp). Kural: mount'a yazımlar bash ile; her commit ÖNCESİ bütünlük kontrolü (`wc -c` + kuyruk satırı). Bugün bir commit bu yüzden bozuldu ve onarıldı (`d44d56b`). Sıkışan `.git/HEAD.lock` dosya-silme izniyle temizlenir.
2. **[davranış verisi] Havuz çiti ikinci kez çalıştı.** 5 fikirlik gece patlaması (→ #13-17) tamamen havuza gitti; kanona sızma, build talebi yok. 07-06 (fren Claude'da) → 07-09 gündüz (fren Salih'te) → 07-09 gece (fren gerekmedi, kanal kurumsallaştı): fikir-yakalama düzeni oturuyor.
3. **[Jarvis kuralı adayı] Karar boyutu ile bağlam boyutu eşleştirilir.** Küçük/geri-alınabilir kararlar (shell ayarı gibi) büyük vizyonla ağırlaştırılmaz; "peak misyona göre seç" talebi geri itildi, kabul gördü. Jarvis'e taşınacak: her kararda önce geri-alınabilirlik ölçülür, danışma derinliği ona göre (S8 ölçek-eşiğiyle aynı kök).
4. **[desen] "Yarına not" mekanizması çalışıyor.** Kullanıcının yarına-not istekleri CLAUDE.md Öncelikler'e tek blok düşürülür → good-morning yakalar. Bugünkü örnek: havuz #16 wiki değerlendirmesi.
5. **[desen] Besleme formatı sabitlendi.** Konuşulan fikir → numaralı madde: tarih + sade tanım (terim açıklamalı) + mevcut maddelere bağlantı + geri-açma koşulu; her besleme ayrı İngilizce commit. Sorulara boğmadan ingest; yalnız gerçek hüküm gerektiğinde soru (paket kavram 7 ile uyumlu).
6. **[kural — Salih talimatı, paralel gece oturumu] Felsefe/karakter sohbetleri profil ağırlığıyla ingest edilir.** End-of-day log'una ayrı "Felsefe/Karakter" kesiti yazılır; Prompt E + haftalık delta bu kesiti profil-B hammaddesi sayar; tür-kapsülü (#12) hammaddesi buradan birikir. İlk uygulama: 07-09 Oturum 4 (AGI felsefe haritası).
7. **[operasyon] Paralel oturumlar aynı repoya yazarken çakışma gerçek.** İki oturum aynı dosyaları commit'ledi: havuz #13 git'te geçici ezildi (amend yanlış HEAD üstüne), log Oturum 2 kırpıldı — ikisi de git tarihçesi/bağlamdan onarıldı, veri kaybı yok. Kural adayı: commit öncesi `git log -1` (HEAD beklediğin commit mi?); amend yalnız HEAD kendi commit'inken; kırpık dosya şüphesinde gerçek dosya host tarafından doğrulanır.
8. **[desen] Fikirler zincir halinde geliyor — zincir olarak ingest et.** 07-09 gece #18→#21 tek hat olarak aktı (ilke → gece ucu → sabah ucu → uç nokta); her yeni madde öncekine açık bağla yazılınca bağlam hazinesi bileşik büyüyor (izole madde listesi değil, gövde). Kural adayı: besleme sırasında Claude yeni fikrin hangi mevcut maddelerin devamı/ikizi/bağımlılığı olduğunu her seferinde açıkça işler.

## 2026-07-10 (gündüz+gece oturumu — sözlük, havuz #22-28, Faz 0-1)

9. **[operasyon] Kesilme sınıfı Cowork köprüsünün kendisi; OneDrive değil.** OneDrive makinede kurulu bile değilmiş — 07-09'daki teşhis düzeltildi. Kural netleşti: commit'lenecek dosya YALNIZ git'in gördüğü taraftan (bash) yazılır, Edit tool'u devre dışı; her commit sonrası kuyruk-satırı asserti. Bugün 3 kesilme bu kontrolle yakalandı, sıfır veri kaybı.
10. **[Jarvis kuralı — Salih] Soru eşiği = cevabın bağlam katkısı.** Salih'in girdisi sonucu değiştirmeyecekse sorulmaz, yapılır + kaydedilir (veto=revert). Aynı gün canlı test edildi: #16 planı sorulmadan üretildi, itiraz gelmedi. S8'e aday.
11. **[Jarvis kuralı — Salih] Taslak-inşa / uygulama ayrımı BUILD YOK'un gerçek sınırı.** Araştırma + 3 kart + öneri = taslak-inşa, serbest (çıktısı sözlükteki 'öneri dosyası'); yalnız seçilen şeyin sisteme kurulması kapalı. Bu ayrım günün ortasında iki kez rafine edildi — kural koyarken Salih'in ilk formülasyonu değil son formülasyonu kayda esas.
12. **[desen] Anlama-kapısı kaçışları format değişikliğiyle çözülüyor, kapıyı taşımakla değil.** Faz 0'da "basit iş" + "sen cevapla" denemeleri geri itildi; şıklı format + Salih'in bildiği göreve çeviri (CSV ağırlıkları) kapıyı İÇERİDE kapattırdı. Ders: kaçış sinyali geldiğinde soruyu kolaylaştır (tanıdık bağlam, seçenekli form), standardı düşürme.
13. **[davranış verisi] High-mod üçüncü koşu: kanal olgunlaştı.** Gece high beyanı + yüksek fikir debisi (7 madde) + sıfır karar/taahhüt; Salih build isteğini kendisi kısıtladı ("high'ım, build'e geçmek istemiyorum"). 07-06 (Claude freni) → 07-10 (öz-fren): TASLAK çiti artık dışarıdan değil içeriden çalışıyor. Yarın ayık tur yine de standart.
14. **[desen — Salih arayüzü] Puan-bütçesi kıtlığı dürüst değerlendirme üretiyor.** İlk koşuda 5 birim / 10 kategori dağıtımı, "hepsi önemli" kaçışını fiilen engelledi ve boş barlar (otomasyon, dış-çıktı) günün gerçek açığını tek bakışta gösterdi. Değerlendirme arayüzü olarak tekrar kullanılabilir — build beklemeden.

## 2026-07-11
15. **[operasyon dersi — TEKRAR] Tarih hatası ikinci kez:** Claude gün içi kayıtları "07-10" etiketledi, gerçek tarih 07-11 (07-06 dersinin aynısı; oturum başında bash tarih doğrulaması yapılmadı). Kural adayı: her kayıt-yazan oturumun İLK aksiyonu tarih doğrulama — good-morning'e gömülebilir.
16. **[desen — kapsam denetimi işliyor] Transkript iddiası ≠ disk gerçeği:** CC'nin kuruluş anlatısı diskle karşılaştırılınca gerçek boşluk çıktı (Build Yöntemleri Envanteri JARVIS'te işaretçisiz; sondevir A/K boş). Ders: kuruluş raporları "dahil" dediğinde grep ile doğrula.
17. **[davranış verisi] Vizyon-beyanları karar kapısında bekletildi:** Salih'in iki vizyon beyanı (LLM-wiki omurga; ingest 3-kart usulü) kayıt önerisiyle karşılandı, Salih karar vermeden geçti — ham fikir ↔ karar ayrımı korundu, havuza da yazılmadı (öneri Salih'te).
18. **[operasyon dersi — sarkan tur] #22-28 ayık veto taraması ikinci güne sarktı:** "yarın sabah" taahhüdü iki oturumdur açılmıyor; TASLAK çitinin değeri taramanın gerçekleşmesine bağlı — sarkma normalleşirse çit süs olur. Yarın ilk iş.
19. **[desen — mobil köprü] Cep kapsülü deseni doğdu:** tek-dosya snapshot + gömülü mobil protokol ("kalıcı karar alma, fikirleri kutu-adayı işaretle") — vault-dışı yüzeylere bağlam taşımanın ilk standart aracı; eskime riski kabul edilmiş parametre (tazeleme komutla).

## 2026-07-11 (kurulum oturumu — tüzük v1)
1. **Kural verisi:** Toptan/örtük sınıflandırma Salih'in kendi ürettiği fikir setinde KABUL GÖRMEZ — "51 maddeyi düşünerek attırdım, gerekçesini açıklayacaksın." Ders: soru-eşiği kuralı (m.4) Salih'in FİKİR MÜLKÜ söz konusuysa ters çalışır; orada gerekçeli sunum zorunlu.
2. **Desen:** Çelişki kapısı (m.16) ilk koşusunda çalıştı — aynı gün içinde iki beyan çelişti, rapor sunuldu, Salih çözümü kendi netleştirdi (2 parçalı denetçi raporu). Mekanizma değerli: high/ayık ayrımına gerek kalmadan tutarlılığı koruyor.
3. **Operasyon dersi:** C:\JARVIS mount'unda git index yazımı bozulabiliyor (0x00000000 imza) — çözüm: `GIT_INDEX_FILE=/tmp/...` ile commit, sonra index'i yeniden kur. Tekrarlarsa kalıcı çözüm K-011 taşımasıyla birlikte düşünülmeli.
4. **Karar verisi:** Kendini-analiz sistemi JARVIS'ten emekli (m.23-24) — günlük özütleri konuşmada kullanılmayacak; karakter/gidişat takibi tamamen düştü, denetçi psikolog değil.
5. **Davranış verisi:** Salih matematiksel model seçimlerini dış-chat'te çalışıp dönmeyi tercih ediyor (N kararı) — karar kalitesi için bağlamı dağıtma deseni; benzer teknik kararlarda prompt-teslimi standart araç olsun.

## 2026-07-12 (Cowork, seçim turu + yedek oturumu)
1. **Kural adayı → kanon:** Ayıklık/damga sorgusu kalıcı yasak (m.33). Ders: mobil protokoldeki tekrar-sorgu deseni kullanıcıyı yorup seriyi düşürüyordu; damga artık yalnız gönüllü beyan.
2. **Operasyon dersi:** Cowork sandbox aynası C:\JARVIS'te de bozuluyor (bayat index.lock, cache-limbo, kesik dosya görünümü) — OneDrive'a özgü değil. Çare deseni: harici GIT_INDEX_FILE + dosyayı temp'e yazıp mv + sonuç index'i .git'e kopyala.
3. **Desen:** Mobil oturum kapsül-snapshot'ı bayatlayınca numara çakışması üretiyor (mobil "V25" ≠ kutu V25). Kalıcı çözüm adayı V27 (teslim-adresi protokolü); o gelene dek ingest'te çakışma şerhi zorunlu.
4. **Yöntem:** Push devri device-flow ile çalışıyor (repo yetkisi oturumluk, token diske yazılmaz) — sürtünme: oturum başına 1 onay; kabul edilebilirliği kullanım gösterecek.
5. **Davranış verisi:** Salih seçim turunda 3 fikri (high-mod, kanka, mod-oranı) tek turda kesip attı — sadeleşme yönlü karar iştahı; build kapsamını şişirme riskine karşı doğal fren.
6. **İlke (Salih, kapanış):** Geç-keşif riski bilinçli yönetilecek — wiki-link örneği: araç baştan biliniyor olsaydı standart ilk günden kurulurdu. Kural: dışarıda hazır çözüm olabilecek her tasarım kararından ÖNCE hedefli araştırma (K-013 sınıfı) doğru SIRAYA konur; "bilmediğimizi bilmiyoruz" varsayımı default açık.

## 2026-07-12 (masaüstü build oturumu)
1. [operasyon] Git index mount'ta bozuluyor → `GIT_INDEX_FILE=/tmp/...` çözümü; oturum-başı kurulur, kapsüle teknik not yazıldı.
2. [operasyon] Mount çift-görünüm: Windows-tarafı yazım sandbox'ta gecikmeli görünür → yazım sonrası bash doğrulaması commit ön-koşulu.
3. [desen] "Araştırma-önce" doğrulandı: K-013'ü build önüne alma emri v2-gist geç-keşfini önledi — dışarıda çözülmüş problemi taramadan mekanizma yazma.
4. [davranış verisi] Salih seçenek sunulduğunda önce netleştirme sorusu soruyor (SOP nedir, neden öneriyorsun) — soru formatı cevap-yerine-soru dönüşüne açık olmalı; gerekçesiz öneri sunma (m.6 zaten emrediyor).
5. [kural adayı] Salih tezi #0: kombinasyon-başına beklenti vektörü (başarı/süre/token) + kalan-zaman politikası — kanonlaşma tartışması sonraki oturumda; ön-koşul V28 etiket verisi (1/10 başladı).

## 2026-07-12 (3. oturum — tartışma kuyruğu kapanışı)
1. [kural→kanon] Tez #0 kanonlaştı (m.35) + m.34 katmanlı ingest + m.36 ilk-prototip fazı — kuyruk 3 blok tek oturumda kapandı. Desen: öneri → Salih revizyonu → imza akışı aynı oturumda işledi (m.34'ün kendisi buna izin veriyor).
2. [desen] Çelişki kapısı ikinci canlı koşusunu yaptı (PortRisk ertelemesi): tarihsiz "bitince" kapısı, yaşayan-listeli DONE'lu karta (K-015) çevrildi — muğlak kapıyı ölçülebilir kapıya çevirme deseni tekrar kullanılabilir.
3. [operasyon] Mount git kilidi (HEAD.lock silinemedi) → commit'ler GitHub klonundan (/tmp) push'landı; yerel .git geride, dosyalar güncel. Sonraki oturum onarım: lock sil ya da fetch+reset. Bu, 07-12 sabah dersinin (çift-görünüm) üstüne üçüncü mount arızası — kalıcı çözüm K-011 taşımasıyla birlikte düşünülmeli.
4. [davranış verisi] Salih'in matematik formülizasyon iştahı yükselişte: V30 (V=ΔG/C) mobilde kendi üretti, V31 tahmin ajanı + "beklenen" bilgisi istedi — tez #0 hattı organik büyüyor; ölçüm-öncelikli stratejiyle tutarlı.
5. [davranış verisi] "Taze-oturum promote" gerekçesi Salih'e yetmedi, ingest-kalite çerçevesine kendisi çevirdi — psikolojik-bias argümanı yerine mühendislik argümanı satıyor; öneri sunarken çerçeve seçimi buna göre.

## 2026-07-12 (4. oturum — m.36 revizyonu + paralel vardiya)
1. [kural] m.36 revize: PortRisk kapısı kalktı, K-002 ile K-015 paralel şerit. Gerekçe Salih'ten: kendini projelerle geliştirecek sistemin yakıtı proje — tasarım icranın ön-koşulu değil (53:0 bulgusuyla tutarlı).
2. [desen] Dün konan kapı ertesi sabah feedback'le kalktı — çelişki kapısı 3. canlı koşusu sorunsuz: eski metin üstü çizili korunarak revizyon (m.8 uyumlu tüzük-değişim deseni oturdu).
3. [operasyon] Paralel vardiya protokolü doğdu (Salih fikri): oturum = vardiya şeridi; kapsülde satır-sahipliği + ayrı teslim raporları + push-öncesi-pull. Kritik sınır: iç-mutfak dosyası public portrisk reposuna asla yazılmaz.
4. [davranış verisi] Salih operasyonel süreç tasarımını kendisi önermeye başladı (oturum bölme + log senkronu fikri kendi cümleleriyle geldi) — sistem sahipliği pasiften aktife kayıyor.

## 2026-07-12 (4. oturum ek — gece, oyun arası)
1. [desen] "Oyun arası dikte" kullanım modu doğdu: Salih düşük-dikkat modunda fikir düşürüyor, karar almıyor ("karar almıyoruz, not al") — Carvis notu işleyip commit'liyor, kararlar açılışta hatırlatılıyor. TASLAK-çiti ailesinin hafif versiyonu; iyi işledi.
2. [kural adayı ×3, paket] Seçenekli-sunum eşiği + V36 araştırma-önce + V38 ilk-çıktı-hızlı — üçü aynı ailede (karar-sunum protokolü); birlikte imzaya gelecek.
3. [davranış verisi] Salih format ihlalini anında yakalayıp kural netleşmesi istedi — sistem-kurallarına sahiplik artıyor; Carvis'in m.31 "alt-karar" savunmasını kısmen kabul etti, sınır kalibrasyonu veriyle yapılacak.
4. [operasyon] Üçlü sohbet kanalı (cc/) kuruldu ama İLK KOŞUSU yok — V38 gereği ilk gerçek CC görev emri en yakın fırsatta (muhtemelen loop-eng Faz 2 /goal denemesi).


## 2026-07-13 (sabah oturumu — V39/m.37 çerçevesi)

*(1-5 sabah özütleri yerleşik desenle JARVIS fikir kutusuna taşındı — V47-V50; #4 V43'e birleştirildi [aynı dersin tekrarı], #2 süreç notu kapsülün 'masada kararlar' kaydıyla aynıydı, taşınmadı. 07-13 günaydın, Salih talimatı: 'her zaman ne yaptıysak onu yap')*

*(6-9 gece özütleri Salih talimatıyla JARVIS fikir kutusuna taşındı — V41-V44, 07-13)*

## 2026-07-13 (günaydın vardiyası)

*(Özütler kural gereği doğrudan JARVIS fikir kutusuna: V51 kaza-seçim dersi; oturumun tam dökümü `raporlar/vardiya-teslim-2026-07-13-gunaydin.md` + JARVIS git log d9c6926→d0737e6)*

## 2026-07-14 (JARVIS 2. oturum — ilk CC köprü koşumu)
1. **[operasyon]** İlk CC koşumunda doğrulama katmanı 70 bulgunun 12'sini düzeltti → araştırma-ajanı çıktısı doğrulamasız kutuya İŞLENMEZ; ama %100 bulgu-başına doğrulayıcı pahalı (~2,4M token) → sonraki koşumlarda V26 örneklem-denetimi + yalnız doğrudan-kullanım-adaylarına tam doğrulama.
2. **[desen]** Literatür-yokluğu simetrisi (V54, Salih): dış karşılığı olmayan tasarım ne hata ne keşif kanıtı — hipotezdir, hakem kendi koşum verisi. V48'in tamamlayıcı yarısı.
3. **[davranış verisi]** Salih sınırları iki kez netledi: takvim yetkisi ("neye ne kadar bakacağıma ben karar veririm") + V52 doktrini (tetik-sahipliği araçsal, misyon otomasyon; ama "şimdilik manuel" önerisini kabul etti — doktrin/tempo ayrımı bilinçli).
4. **[operasyon dersi]** V43 4. vaka: pano BLOKE bölümü sessizce kesikmiş, kimse fark etmemiş → push-sonrası doğrulama yalnız eklenen satırı değil dosya SONUNU/bölüm-bütünlüğünü de kontrol etmeli; git tarihçesi kurtarma kaynağı olarak çalıştı.
5. **[araç]** Skill ≠ subagent ≠ MCP ayrımı frontmatter'dan tanınır; kurulum adresleri farklı (.claude/skills / .claude/agents / .mcp.json) — "dosya türünden kaydedemedim" sınıfı sorunların kökü bu ayrım.
