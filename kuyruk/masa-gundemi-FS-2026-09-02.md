# Masa Gündemi — FS (Fable–Sonnet ikilisi) Karar Masası (2026-09-02)

*7. Lavish masası. Tetik: Salih Katman-1 beyanı 09-02 ("Opus saf dışı; işçi = Sonnet, planlayıcı = Fable; sistemi komple revize et; sağlık turu tavsiyelerini, icra-prompt optimumunu ve biriken kararları masaya taşı"). Yüzey: `raporlar/masa-fs-karar-yuzeyi-2026-09-02.html` (Lavish). Üretici: Carvis (Fable 5.1, ana-sıra). AS-OF 2026-09-02 · HEAD 481ddca + lokal commit'ler (push SSH-kimliksiz, m.9 borcu açık). Hükümler bu dosyaya + defter Karar 86 bloğuna işlenir.*

**Masa öncesi FİİLEN yapılan (Katman-2 icra, Salih beyanına dayanarak — veto = revert):** Karar 85 kanon şerhleri (Opus emekli; tüzük m.30/42/44, ajan-metodolojisi §37, research-agent model pin opus→sonnet + R4, gorev-emri-derleme, pipeline-kosum, 2 wiki) · test regresyonu düzeltmesi (`[ariza]`) · sağlık turu koşumu · defter Karar 85 bloğu.

## Sağlık turu özeti (Fable 5.1 ilk gözlem; kanıt satırları D6'da)
| Kapı | Sonuç |
|---|---|
| Sözdizimi (tools/*.py, hooks/*.sh) · git fsck · kural sayacı | temiz · temiz · 19/100 |
| katman-hatti (silver tazelendi) · silver-sağlık kapısı | exit 0, bilinen 2 WARN (T-C3-ılık 109 · T-C6 1) · ERROR 0, YETİM 243/351 |
| **Birim testleri** | **68 test: 5 FAIL — 08-30 `a0fc255` (parquet varsayılanı AÇIK) test fixture'ında `tarih_iso` kolonu yok → `kolon-olcum` düşüyor; üretimde belirti yok; DÜZELTİLDİ** |
| Anakronizm denetimi | 196 tekil bulgu (İHLAL 116; cc/ 224 · raporlar/ 144 satır) — önceki koşuma göre YENİ 2 (09-02 galeri teslim raporu) → birikim, sızıntı değil |
| Push'suz 3 commit (09-01/02) | kanona yalnız kapsül dokunmuş (5+/4−); bozukluk yok |
| Boyut tetikleri | defter 58,8/48 · kutu 22,3/20 · KILAVUZ 16,8/16 · pano 12,2/12 · **kapsül 7,8/8 sınırda** |
| Tel yanlış-pozitifi | `pretool-core-tel.sh` salt-okur `sed -n … \| grep -i` komutunu engelledi (satır 18 kuralı `-i`'yi sed'e ait sanıyor) |
| Push | `ssh-add -l` → "no identities" → Salih el işi |
| paralel-kapi | dalga planı bayat `tamam` birimleri listeliyor (kapı v0.2 açığı, bilinen) |

## Kalemler (hüküm Salih'te; her blokta önerilen ilk sırada)

### D1 · Lider/orkestratör katmanı — Fable-Sonnet mimarisi
Opus'un çıkışıyla m.44 "domain-lider = bir-altı model" katmanı boşaldı. Sonnet işçi (karar yetkisi sıfır) lider olamaz → orkestrasyon ya Fable'da kalır ya statik tanımlı bir orkestratör-ajan taşır. Ekip-lideri ön-araştırması (cc/rapor-2026-08-01-11/19, 08-14-2): A5 hiç KURULMADI; hafıza katmanı için "bütçe-eşitli kıyasta hafıza modülleri sade tabanı geçemedi" bulgusu; "Opus lider + Sonnet işçi %90,2" rakamı Opus-spesifik.
- **(a) ÖNERİLEN — Statik skill-orkestratör (Fable ana-sıra + tanımı dosyada duran Sonnet orkestratör-ajanı, durum taşımaz):** Fable görevi böler ve case'leri yazar; skill orkestrasyonu yük yaratıyorsa `.claude/agents/orkestrator.md` (Sonnet, salt tanım, çağrı-koşulu alanlı) açılır; her iyileştirme rol METNİNE commit'le girer. Artı: deterministik, hafıza-drift yok, İB-59 4/4 lider arızası "talimat açığı" çıktı (rol metnine kural = tam bu). Eksi: seanslar-arası öğrenme elle işlenir. Kademeli-devir çerçevesiyle birebir (başta hiyerarşi farkı maksimum).
- **(b) Hafızası gelişen ekip-lideri (A5):** kalıcı hafıza dosyalı Sonnet lider. Artı: mikro-karar devrinin taşıyıcısı. Eksi: yeni kanon yüzeyi + drift; K-010 A3/A4 açık; hafıza-modülü kanıtı negatif (arXiv:2606.15017 bütçe-eşitli); Sonnet'e kalıcı hafızayla yetki = katı-başlangıç (m.42 d) ihlali.
- **(c) Hibrit-zamanlı:** şimdi (a); A4 "ajan-defter şeması v1" kapandığında (b) ayrı masaya. (a)'nın kendisi zaten bu yolu içeriyor → (c) = (a) + tetik yazımı.

### D2 · İcra oturumu formatı — nerede · hangi model · effort · pipeline/loop/nested
Opus yan-oturumu yok. Veri: Sonnet atlas-tez n=5 / antitez n=2 / hakem n=0 (Opus 80/87/3); İB-09 V26'da Opus=Sonnet (n=1 çift); İB-65 M1 yüklem-ağacı (loop ↔ pipeline ↔ hibrit deterministik); İB-66 seviye-sayım (gerçek nesting = kendi sayacı ∧ durma yüklemi); Karar 84 gnhf iki-şerit; fren 144 (78 çağrı/4 birim ≈ 20/birim).
- **(a) ÖNERİLEN — TEK Fable ana oturumu (jarvis dizini) + Sonnet işçi pipeline'ı:** icra emirleri Fable'ın Agent aracıyla Sonnet işçilere dağıtılır (paralel-kapi + manifest, kademe N 1→2→3, işçi çağrıları SENKRON, işçi bütçesi 10-15 çağrı, effort low-medium; hakem/sentez Fable). Gece/uzun/sensiz iş → gnhf worktree (Karar 84, Sonnet ajan). Loop yalnız "sürekli-korunan değişmez" sınıfı işlerde (İB-65 M1); nested yalnız kendi sayacı+durma yüklemi olan seviyelerde (İB-66). Effort: Fable medium (planlama/hakem; high yalnız kanon kararı), Sonnet işçi low (tek-alan) / medium (atlas-tez). Artı: sıfır ikinci-Fable maliyeti, tek hareket kütüğü, hiyerarşi net. Eksi: Fable bağlamı büyür — bağlam bütçesi (KB-50) + kademe disiplini şart; ağır atlas günlerinde Fable token'ı yer.
- **(b) İkinci Fable icra yan-oturumu (Salih yapıştırmalı prompt, eski Opus rolünde):** Artı: ana oturum bağlamı temiz kalır. Eksi: 2× Fable tokeni (Salih'in kaçındığı maliyet); yan-oturum karar alamaz, aynı prompt-yazarlık sızıntısı.
- **(c) Sonnet yan-oturumu (headless `claude -p` / gnhf) olarak icra:** Artı: en ucuz. Eksi: lider yok — Sonnet karar veremez; koordinasyon her adımda Fable'a döner (fiilen (a)'nın pahalı hali).
**Kademe kuralı (tüm seçeneklerde):** fren denklemi `N_hücre + sayaç_oturum ≤ 143`, planlama tavanı 116 (İB-69 a2).

### D3 · m.40b koşum sözleşmesi — üç kural + sızıntı kuralı
Kanıt: bağımsız hakem İB-66 etiketlerini DEĞİŞTİRDİ (3 satır sertleşti, oran 55,6→44,4) · V26 "URL'li iddia" kuralı URL'siz model-hafızası iddialarını hiç örneklemiyor · işçi-başına ≥2 birincil-kaynak kotası 1→17 açılma.
- **(a) ÖNERİLEN — Üçü birlikte kanon:** (i) *yapan ≠ ölçen*: sentezi yazan ajan hakemlik yapamaz; ölçen ajana yalnız veri verilir, emrin yazarı/beklentisi verilmez (prompt-yazarlık sızıntısının da cevabı); (ii) V26 örneklemine zorunlu URL'siz-iddia kotası (son üçlükten ≥1 URL'siz iddia); (iii) işçi başına ≥2 gerçek birincil-kaynak açma kotası. Artı: üçü de ölçülmüş; sözleşme tek revizyonda. Eksi: koşum başına +1 hakem ajanı, +açılma maliyeti.
- **(b) Yalnız (i):** en güçlü kanıtlı olan. Eksi: V26 açığı ve kota açık kalır.
- **(c) Beklet:** 3 koşum daha veri.

### D4 · Ajan freni — katman-başına sayaç (seçenek A)
Bugün: tek sayaç 72/144 (Karar B 08-31). Bulgu: sayaç alt-ajan çağrılarını da sayıyor.
- **(a) ÖNERİLEN — İB olarak aç, düşük öncelik:** hook'a katman etiketi (`parent_tool_use_id` var ↔ işçi) + ayrı eşik; taban ölçümü 10 koşum sonra. Artı: fren amacı korunur. Eksi: geliştirme + yeni kalibrasyon.
- **(b) 144 sabit kalsın:** sıfır iş; tek-katmanlı kaçağı geç yakalar.

### D5 · Manifest `tur` alanı — M1 yüklem-ağacı + `matris` değeri (İB-65 + İB-69)
Envanterin %29'u iki-değerli alana sığmıyor; 17 manifest = 16 pipeline + 1 loop; göç maliyeti 0 dosya.
- **(a) ÖNERİLEN — M1 + S-A:** `tur ∈ {pipeline, loop, hibrit, matris, belirsiz→masa}`; deterministik yüklem-ağacıyla doldurulur. Eksi: `belirsiz` masaya kalem üretir.
- **(b) Beklet.**

### D6 · Sağlık turu tavsiyeleri (Fable 5.1 ilk gözlemleri)
- **(a) ÖNERİLEN — Paket:** (1) seans-kapanış ritüeline `python3 -m unittest discover -s tools/testler` kapısı (FAIL → kapanış durur; deterministik) — suite 08-30'dan beri kırıktı, kimse koşmadı; (2) `pretool-core-tel.sh` satır 18 kuralını `sed|perl` ile `-i`'nin AYNI boru segmentinde olmasına sınırla (salt-okur komutlar geçsin); (3) anakronizm birikimi: tarihli rapor/emir dosyaları (cc/, raporlar/) için "çekim tarihi = AS-OF" muafiyeti ∨ toplu damgalama İB'si (116 İHLAL'in tamamı tarihli dosya); (4) damıtma seansı: 4 dosya aşımda + kapsül 7,8/8 — ilk boş seans; (5) paralel-kapi v0.2: `durum=tamam` birimler plandan düşer; (6) SSH agent kimliği (Salih el işi) → push. Artı: 6 kalem, hepsi ölçülmüş. Eksi: (3) kural kararı gerektirir — ayrı işaretle.
- **(b) Ayıklı:** hariç kodları nota yaz.

### D7 · Devir soruları (08-31 Opus + 09-02) — toplu adresleme
④ İB-66 Model A öncesi `parent_tool_use_id` canlı doğrulaması (öneri: EVET, ucuz; D4 ile aynı sonda) · ⑦ İB-69 aile-1 raporuna 4 şerh (öneri: m.8 üstüne-not olarak aile-1'e işlenir) · ⑨ m.39 ihlalli ham rapor `cc/rapor-2026-08-31-ib68-b3-pazar-dagitim.md` (öneri: mevcut damga + başa 1 satır düzeltme notu) · ⑩ T_hucre M-1 ölçümü (öneri: transkript usage hasadı İB'si — İB-08 usage-otomasyonuyla birleşir) · ⑮ İB-66 tasarım gerekçeleri (öneri: şerhle kalır; Model A doğrulaması sonrası tazelenir) · ⑭ İB-07 bağımsız set: KARAR ALINDI 08-31 (maskeli+nötr-ad türetim, tetik ilk description değişikliği) — bilgi.
- **(a) ÖNERİLEN — Toplu kabul (önerilerle).** (b) Ayıklı. (c) Beklet.
**Masa dışı bilgi şeridi (karar istemez):** galeri devri 5 sorusu (09-02) jarvis-dışı staj şeridi — Karar "geçici hafıza" kuralı gereği masaya girmedi; Salih tetiğiyle ayrı.

### D8 · İB-70..73 sıralama + K-020
- **(a) ÖNERİLEN — Sıra 72 → 71 (baseline ölçümü) → 70 → 73; K-020 = M2 (kendi harness genellemesi, İB-69 a2 önerisi; iki ucuz ön-ölçüm koşulu).** Gerekçe: 72 (bayat-dosya karantinası) diğer üçünün tarama yükünü düşürür; 71 hedef koyabilmek için önce oranı ölçer (m.39); 73 (eğitim serisi) en büyük iş, en son bilgiyle yazılır.
- **(b) Farklı sıra (nota yaz).**

## Hükümler — MASA KAPANDI 2026-09-02 (Salih, Send&End; 8/8 hüküm = (a) önerilen; bağlayıcı kayıt defter Karar 86)
- **D1 → (a)** statik skill-orkestratör. **Salih notu:** hafızalı ekip-lideri kurulmasa da yapılan işlerden çıkan öğrenme desenleri/mimariler/şemalar/kurallar ileride kullanılmak üzere AKTARILMALI → `kuyruk/ekip-lideri-ogrenme-desenleri.md` tohum dosyası (İB-74).
- **D2 → (a)** tek Fable ana oturumu + Sonnet işçi pipeline'ı. **Salih notu:** Fable bağlamı büyüdüğünde bağlamı Sonnet işçilere devreden ekip-lideri tasarımına YAKIN tarihte geçilecek (hafıza/yetki başta sınırlı, bağlam devri esas) → İB-75.
- **D3 → (a)** üç kural kanon (tüzük m.40 ek fıkra; atlas-kosum adım 3/5/6).
- **D4 → (a)** İB-76 katman-başına fren sayacı (düşük öncelik).
- **D5 → (a)** M1 + S-A `matris` — paralel-kapi.py + 17 manifest (Sonnet işçi, commit 45ce557). **AÇIK SORU Salih'e:** yüklem-ağacı proxy alanlarla (tetik_turu/dis_tavan/iterasyon_ayak_izi) bağlandı → 17 manifestin tümü `pipeline`; İB-65'in beklediği `hibrit` ayrımı manifest alanlarından çıkmıyor — proxy kabul mü, şemaya Y1/Y2/Y3 alanları mı?
- **D6 → (a)** paket: 1 (seans-kapanis §6g) + 2 (core-tel regex) YAZILDI · **3 anakronizm tarihli-dosya muafiyeti = kural kararı, Salih imzası AYRI bekler** · 4 damıtma tetiği · 5 D5 ile · 6 Salih el işi (ssh-add).
- **D7 → (a)** toplu: ⑦ + ⑨ rapor üstüne-notları (Sonnet işçi) · ④ → İB-76 · ⑩ → İB-08 notu · ⑮ şerhle kalır.
- **D8 → (a)** sıra 72 → 71 → 70 → 73; K-020 = M2 (pano güncellendi).
- **Masa-sonrası ek hüküm (Salih, mesajla 09-02):** CLAUDE.md'de bütçe için yapılan 3 kısaltma (Salih'in-anlaması satırı · deterministik-tasarım satırı · Cowork parmak-izi satırı) Carvis önerisiyle GEÇERLİ — imzalı.
- **Arıza:** bu masanın icra yazımları (10 dosya) commit'ten önce reflog'suz bir geri-almayla kayboldu, aynı seansta yeniden uygulandı (defter Karar 86 arıza kaydı; tohum dosyasına ders).
