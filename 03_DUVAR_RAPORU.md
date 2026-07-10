# 03 — Duvar Raporu (Refutation Ethos: Gerçek Sınırlar)

**Statü:** sentez — üç ajan raporu + yerel kayıt. Kural gereği (Salih, 07-10: "genuinely surface the wall") bu dosya planın en sert eleştirisidir; moral yönetimi yapmaz. Gözlemler çıplak veridir (övgü-merci yasağı).

## Duvar 1 — ÜRETİM TEMPOSU (ana duvar; diğer her şey bunun gölgesi)

**Veri:** Homebase (plan reposu) son 2 günde 53 commit; portrisk (CV artefaktı) son 8 günde 0. PortRisk toplam tarihçesi: 1 commit (`ee16d2d`, 07-02). 06-18'deki 8-haftalık MVP planında hafta ~3; hafta-2 işi başlamadı. Kayıtlı desen CLAUDE.md'de bizzat: "3. commit'siz oturum", "içgörü ≫ icra" (SALIH_ANALIZ P1).

**Anlamı:** Sistem kurmak, göndermeyi İKAME EDİYOR. Bu gece de aynı desenin içindeydi: JARVIS build talebi, kod değil plan üretti (bu repo dahil — bu raporun kendisi de o desenin parçası; farkı, bunu açıkça söylemesi ve kod-önceliğini plana gömmesi).

**Matematik:** Kasım penceresine ~16 hafta. PortRisk MVP planda 7 hafta; gerçekleşme katsayısı şu an 0 olduğundan iyimser 2× çarpanla 14-16 hafta → **PortRisk tek başına pisti dolduruyor. 3 repo kapanmıyor; 1 bitmiş repo + İngilizce paket + yarışma satırı kapanıyor.**

**Yapısal mitigasyon (irade değil):** tek metrik = push'lu commit · haftada ≥3 commit çapası (8 hafta) · plan-spiral limiti (bu repoya ≤30 dk/hafta, kod:plan ≥3:1) · dış çapa = başvuru takvimi (gerçek deadline'lar: banka programları Oca-Şub). Sürtünmesizlik ilkesinin dürüst sınırı kayıtlı: sürtünme azaltmak yetmez, dış çapa şart (havuz #18).

## Duvar 2 — CV-PAZAR ALGISI

- JARVIS repo olarak = gürültü; kötü sunumda AI-slop red flag'i (red-team §2.3, The Markup). Taşıyıcısı mülakat anlatısı + PortRisk README bölümü; repo değil.
- Jenerik VaR/backtest repoları şablonlaşmış (GitHub `value-at-risk` topic'i dolu; örnek: Sribaru45/quant-finance-dashboard — plandaki her şey + deploy). Ayrıştırıcı: gerçek-portföy anlatısı + savunulabilir metodoloji + canlı link + düzenli commit şekli.
- "Quant" hedefi iki ayrı pazar: elit trading firmaları (GitHub ağırlıksız; eleme = mental math/olasılık testi + okul) vs finans-domenli data/ML (GitHub gerçekten işe yarar). Plan bilinçli olarak İKİNCİYE oynuyor.
- Eleme zinciri gerçeği: banka genç-yetenek programları ilk kapıda transkript + test ister; **GPA kayıtlarda hiç geçmiyor — açık eleme değişkeni, Salih netleştirmeli.**

## Duvar 3 — TEKNİK (index/sistem tarafı; ham detay rapor 1-2)

- **Recall tavanı görünmez:** grep string bulur, anlam değil; kaçırdığını bilemezsin. Alias bilinen entity'yi kurtarır, unutulmuş kelimeyi kurtaramaz — embedding'in gerçekten çözdüğü tek şey bu (rapor 1, dürüst hata modu 1).
- **Konvansiyon disiplini bahsi:** Mimari 1, yokluğu belgelenmiş desenin ta kendisi olan editoryal disipline bahse girer; sapma hata fırlatmaz, erişim sessizce kötüleşir. Mitigasyon (git hook lint) kendisi de yaşaması gereken küçük bir rutin.
- **RAG'ın sessiz çürümesi:** bayat index kendinden emin yanlış bağlam döndürür — ilke #5'in üniformasıyla ilke #5'in kabusu. Bu yüzden M2 kalıcı elendi; hibrit ancak mekanik tripwire'la.
- **Solo-operatör kırılmaları:** yakalama-anı insan kararı 2. haftada ölür · QC katılığı sessiz backlog üretir · senkron gecelik-otomatik değilse 1 haftada ıraksama · tabansız oto-link yumak. Hepsinin yapısal supabı rapor 2'de tanımlı.
- **Token ekonomisi:** "ajan = semantik katman" her sorguda ücretli token yakar; ~15k dosya altında kazanır, üstünde sessizce pahalılaşır (tripwire'ların varlık sebebi). Genel ilke havuzda zaten var: her işi Fable-sınıfıyla yapmak sürdürülemez (#14 routing bunun için doğdu).

## Duvar 4 — TEK KOPYA RİSKİ (yeniden fiyatlama önerisi)

Makinede bulut yedek YOK (Salih'in bilinçli 07-10 kararı — o gün kapsam Homebase'di). Bu gece risk yüzeyi BÜYÜDÜ: artık aynı diskte üç kök var (Homebase + C:\JARVIS + C:\Users\sasah\dev). Tek disk arızası üçünü birden götürür. Fiili ucuz sigortalar: PortRisk zaten GitHub'da (public push = yedek); JARVIS node için de private GitHub remote'u aynı işlevi görür — bulut-yedek kurulumu gerektirmez, tek `git push`. Karar Salih'in (Katman 1: dışarı çıkan veri); öneri olarak kayıtlı.

## Duvar 5 — KARAR HİJYENİ (bu gecenin kendisi)

Çıplak kayıt: aynı gün içinde "high'ım, build'e geçmek istemiyorum" (ingest #13) → "BUILD VAR. LETS GO." Çelişki yorumsuz kaydedildi; mekanizma çalıştı: üretim karantinada (bu repo), Homebase kanonuna sıfır yazım, onay kapısı = ayık tarama, veto maliyeti = tek revert. Refutation ethos'un kendi kararına uygulanması budur; tarama onaylarsa şerh düşer, veto ederse repo gider — iki durumda da sistem kaybetmez.

## Duvar 6 — EKSİK ELEME KATMANLARI (repo-dışı gerçekler)

SQL (ilanların değişmezi — Sprint 2'ye gömüldü) · İngilizce CV/LinkedIn/profil paketi (ATS %70-keyword + 6-10 saniye taraması; repo bu katmanı geçmeden görülmez) · yarışma satırı (Prosperity: GPA-bağımsız tek hızlı ölçülebilir sinyal) · mülakat/test hazırlığı ("defend your diff": rastgele 3 satır kod + "neden bu?" — AI-destekli çalışan aday için asıl sınav bu) · başvuru lojistiği (pencereler Oca-Şub; CV'nin gerçek deadline'ı ilk açılış).

## Tek cümlelik özet

Duvar, JARVIS vizyonunda ya da araç seçiminde değil; **plan üretiminin kod üretimini ikame etmesinde** — ve bu raporu içeren gece de dahil, karşı-kanıt ancak `git log --oneline` çıktısında görünecek: `salihsahinin/portrisk`'e düşen bir sonraki commit.
