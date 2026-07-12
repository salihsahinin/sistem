# Paralel Vardiya — İlk Deneme Talimatı (Salih için)

> **Açıklama notu:** 2026-07-12 sabah kararının (m.36 revizyonu + KILAVUZ paralel vardiya protokolü) ilk saha denemesi için adım listesi. Deneme yapılıp aksaklıklar kaydedilince bu dosya arşive iner (m.8 — silinmez). Kural kaynağı: KILAVUZ "Paralel vardiya protokolü" bölümü.

## GÜNCELLEME (07-12 4. oturum): m.36 2. revizyon — ÖNCELİK PROTOTİP (K-015, ~3 ay ufku); PortRisk vardiyası artık "ölçüm-bankı vardiyası" (bloke değil, hasat verisi üretir; çatışmada prototip kazanır). Aşağıdaki adımlar aynen geçerli.

## Ne deniyoruz
İki ayrı Cowork oturumu = iki vardiya hattı: **PortRisk vardiyası** (K-002: Sprint 1) ve **JARVIS vardiyası** (K-015: loop-eng Faz 2+4). Her hat kendi işini yapar, kapanışta kendi teslim raporunu yazar, kapsülde yalnız kendi satırını günceller.

## PortRisk vardiyasını açmak için (adım adım)
1. **Yeni Cowork oturumu aç** ve klasör seçiminde İKİ klasörü birden ekle:
   - `C:\JARVIS` (bağlam buradan okunur — CLAUDE.md otomatik yüklenir)
   - `C:\Users\sasah\dev\portrisk` (kodun yaşadığı yer)
   - *Neden ikisi birden:* JARVIS olmadan oturum şirket bağlamını göremez; portrisk olmadan koda dokunamaz. İç-mutfak dosyası public portrisk reposuna asla yazılmaz.
2. **İlk mesaj:** `günaydın, PortRisk` — Carvis kapsülden K-002 şeridini alır, Sprint 1 planını önüne koyar (yfinance ile fiyat verisi çekme + getiri hesabı + pytest).
3. **Çalış:** kod portrisk reposunda yazılır; commit'ler SENİN elinden (m.9 — proof-of-work). Carvis yönlendirir, kritik satırları sen yazarsın.
4. **Kapanış:** `end of day` de — Carvis o vardiyanın teslim raporunu `raporlar/2026-MM-DD-portrisk-teslim.md` olarak yazar, kapsülde YALNIZ PortRisk satırını günceller, kendi commit'lerini push'lar.

## JARVIS vardiyası (bu hat — mevcut düzen)
1. Cowork'ü her zamanki gibi `C:\JARVIS` ile aç (Homebase da ekli olabilir).
2. **İlk mesaj:** `günaydın, JARVIS` (ya da sadece "günaydın" — Carvis hangi hat olduğunu tek soruyla netleştirir).
3. Gündem: K-015 madde 3 — loop-eng Faz 2 (/goal) + Faz 4 (Routine) + Karpathy revizyonu (senin öğrenimin).
4. Kapanış aynı: `end of day` → `raporlar/2026-MM-DD-jarvis-teslim.md` + kapsülde yalnız JARVIS satırı.

## Çakışma kuralı (iki oturum AYNI ANDA açıksa)
- Push öncesi pull zorunlu — Carvis bunu kendi yapar, senin yapman gereken yok.
- Kapsülde her vardiya yalnız kendi şeridinin satırına dokunur.

## Deneme sonrası
Aksayan ne olduysa (bağlam eksik kaldı mı, kapsül çakıştı mı, günaydın taraması şeridi doğru aldı mı) vardiya kapanışında söyle — protokol deneysel damgalı (m.29), veriyle kalibre edilecek.
