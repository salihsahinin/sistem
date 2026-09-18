# ajan-metodolojisi

*AS-OF 2026-08-30 (yazım: paralel icra oturumu, İB-04 wiki turu; kural kaynağı `core/ajan-metodolojisi.md` — çelişkide kanon kazanır).*

## Üst blok
Ajan-tasarım metodolojisi: görev-emri yazımı ve delegasyonun literatür-sınanmış kural seti. Dört ayak: görev = **tipli fonksiyon** (dal-bütçesi ≤5) · hafıza = **manifest** (eager/lazy) · B1→B4 lojik-kod merdiveni · lider/işçi dörtlü delegasyon + model hiyerarşisi + firstmate rolü. Durum: **güncel** · son-teyit 2026-08-30. Kaynak: `core/ajan-metodolojisi.md` v1 (`AKTİF` 2026-08-14; araştırma dayanağı `cc/rapor/2026-08/rapor-2026-08-14-2.md` — Opus lider + 4 atlas). Kaba güven: **orta** — tek araştırma turu (m.40b antitez şeridi **koşulmadı**, borç §5 madde 4'te açık), ama 2 haftalık kullanım + üç Salih revizyonuyla (KB-18 08-20, Karar 48 08-21, Karar 76 08-29) pekişmiş.

## Çekirdek
**Görev = fonksiyon (§1):** her görev-emri tipli alanlardan kurulu imza taşır — **kimlik** (`gorev_adi·rol·cagri_kosulu·rejim·model·kosum_profili`) + **girdiler** (tipli) + **bağlam-manifesti** + **sınırlar** (`kapsamda/kapsam_disi/araclar/degismezler`) + **dallar** (numaralı, m.38 bağlaçlı) + **çıktı sözleşmesi** (`done_yuklemi` boolean, derece ifadesi **yasak**). Dal-bütçesi freni: dal+koşul toplamı ≤5; aşan görev **bölünür**, zenginleştirilmez (kanıt: o1-preview 3 turda 0,877→0,707 düşüş).

**Hafıza = manifest (§2):** bağlam üç kademede açılır — S1 künye (her zaman yüklü, küçük) → S2 gövde (alaka görülünce) → S3 ek dosya (gerektiğinde). Dosya **eager** (CLAUDE.md·kapsül·pano) ya da **lazy** (wiki·raporlar·kuyruk·defter, pointer'la açılır) etiketi taşır; yeni dosya varsayılan **lazy**. Sıra kuralı: statik önek önde, dinamik ek sonda (cache breakpoint kırılırsa kazanç sıfırlanır).

**B1→B4 merdiveni (§3):** B1 serbest Türkçe → B2 kontrollü-NL/lojik (m.38, **ears**, done-yüklemi) → B3 şablon/DSL (görev-fonksiyonu, workflow-YAML, skill) → B4 deterministik kod. Varsayılan basamak **aşağıdır**; yukarı çıkış üç-soru kapısından geçer: adım sayısı tahmin edilebilir mi ∧ sabit yol kodlanabilir mi ∧ model-kararı gerekli mi — evet∧evet∧hayır ⇒ bir basamak yukarı.

**Lider/işçi dörtlüsü + model hiyerarşisi (§4):** her işçi görevi hedef · çıktı-formatı+bütçesi · araç/kaynak kılavuzu · görev-sınırları (kapsam-dışı **dahil**) taşır. Dağıtımdan önce zorunlu soru: alt-görevler **bağımsız** bilgi mi topluyor, **ortak** çıktı mı üretiyor (bağımsız→paralel serbest; ortak→tek şerit/paylaşılan manifest). Maliyet-tavanı: işçi liderden pahalı modelde koşamaz; delegasyon varsayılan `KAPALI`. Model hiyerarşisi (KB-02/03): üst model (ana-sıra, bugün Fable) = orkestratör+koşum-tahmincisi+hakem; alt modeller (Karar 89 09-09: Opus 5 lider medium · Sonnet işçi · Haiku eval; Opus/Sonnet/Haiku) [Karar 85 09-02: Opus `EMEKLİ` — işçi = Sonnet, Haiku tek-alan eval işçisi] = skill koşucuları; üst model **yalnız** kendinden düşük modeller için tahmin yazar, kendi koşumunu tahmin **etmez** (`v_skill_kosum`).

**Firstmate rolü (Karar 76 E4):** ana ajan JARVİS kalır (m.44 baki); firstmate = Jarvis'in VE Salih'in kullandığı **yardımcı** ajan, ikame değil araç. Başarılı olduğu iş sınıfı beyanla değil koşum-ölçümüyle tespit edilir (İB-59 açık borç).

**Damıtılmış örnek** (`cc/gorev/2026-08/gorev-2026-08-29-ib39-idempotens-atlas.md`, şablon `core/sablonlar/gorev-fonksiyonu.md`): `cagri_kosulu`="ledger İB-39 icra-sırada"; `kosum_profili`=işçi Sonnet 5, bütçe 10-15, effort düşük-orta, aile 3; `kapsam_disi`="kod değiştirme·kanon yazımı·LLM ile 'idempotent mi' hükmü"; `done_yuklemi`="sentez yazıldı ∧ A+B'de ≥8 birincil kaynak ∧ C'de N script sınıflandırıldı ∧ 3 seçenek (biri karşıt-temelli)" — dört koşul ayrı ayrı karşılandı/karşılanmadı işaretlenir (DRFR).

## Sop
1. `core/sablonlar/gorev-fonksiyonu.md`'yi kopyala; alan adlarını görevin dilinden seç.
2. **kimlik**+**girdiler**+**sınırlar**+**dallar**+ÇIKTI'yı doldur; dal+koşul topla — >5 ise böl.
3. Bağlam-manifestini EAGER/LAZY etiketle; büyük dosyayı **lazy** bırak, pointer ver.
4. Dağıtımdan önce **paralellik-uygunluk** sorusunu sor (bağımsız mı, ortak mı).
5. Model ata: liderden pahalı model işçiye **yasak**; tahmini yalnız üst model, yalnız alt modeller için yazar.
6. Teslimde her done-koşulunu tek tek işaretle (DRFR); tek "başarılı mı" derecesi sorma.

## Gotchas
- Sözleşme zenginleştirmek ters teper: dal-bütçesi aşımı "daha çok kural" ile değil **bölme** ile çözülür.
- N=3 değil **N=5**: m.43 skill-oluşum eşiği Salih revizyonuyla 5'e çıktı (08-20); Rule-of-Three atfı LLM alanında doğrulanmamış — şerh düşülü kalır.
- Kendini-analiz kısıtı (Karar 48): model kendi çıktısını analiz **etmez**; istisna yalnız uzun-periyot **toplu** özet ve deterministik doğrulama.
- Heredoc-python hijyeni (Karar 77): ≥15 satır python Bash heredoc'a değil scratchpad `.py` dosyasına yazılır — aksi 18 hata-benzeri çıktı üretti.
- "Firstmate Jarvis yerine geçer" `YANLIŞ` — ana ajan hep Jarvis, firstmate yardımcı araçtır.

## Süpersede zinciri
- "işçi ajan→ekip lideri→CEO→patron" hattı (07-10) → **yerini aldı 08-17:** şirket metaforu `EMEKLİ`, tek katman JARVİS+firstmate (sözlük: şirket→Jarvis·CEO→köle·patron→tek karar verici·vardiya→seans).
- m.44 çapası (RouteLLM rakamı) → **İMZALANDI 08-20 (KB-18):** rakam [X] kalır, katman kuralı ayakta.
- "firstmate = ikinci orkestratör" → **netleşti 08-29 (Karar 76 E4):** ana ajan JARVİS, firstmate yardımcı; kalıcı tanım İB-59 ölçümüyle sabitlenecek (**açık**).

## Bağlantılar
[[uc-register]] (B1-B4 register geçişinin kardeşi) · [[pointer-sistemi]] (manifest S2/S3 pointer ilkesi) · [[token-x-zaman]] (maliyet-tavanı/rejim ekseni) · [[ai2ai-rapor-formati]] (delegasyon dörtlüsünün rapor/emir karşılığı) · [[olcum-banki]] (skill eşik n≥10 ölçümü)

## Kaynaklar
- `core/ajan-metodolojisi.md` (kural kaynağı, tüm §)
- `core/sablonlar/gorev-fonksiyonu.md` (şablon)
- `cc/rapor/2026-08/rapor-2026-08-14-2.md` (araştırma dayanağı)
- `cc/gorev/2026-08/gorev-2026-08-29-ib39-idempotens-atlas.md` (örnek görev emri)
- `kuyruk/senaryo-defteri.md` (Karar 48·76, KB-18)

**Bağlantılar:** · [[gnhf]] (karşı-link 09-03)
