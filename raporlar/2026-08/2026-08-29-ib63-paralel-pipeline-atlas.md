# İB-63 Pipeline + Loop Paralellik-Güvenliği — Atlas Raporu + Prototip Şema (2026-08-29)

> **Mod:** ana-sıra (Fable, seans-21) · m.40b tam kontrat: tez ×3 → CoVe-Factored antitez ×2 + kaynak-koddan bağımsız iç-doğrulama ×1 → V26 ×2 → maskeli hakem ×2 · emir `cc/gorev-2026-08-29-ib63-paralel-pipeline-atlas.md` · koşum dosyaları `cc/rapor-2026-08-29-ib63-atlas-*.md` (10 işçi ajan)
> **Kanıt kısıtı:** Bernstein 1966 orijinali + Karp-Miller + Adya paywall (ders-kitabı/ikincil-birincil eşdeğerlerle kapatıldı, boşluk beyanlı) · antitez-B V26'da K-DÜŞÜŞ aldı (uydurma-atıflı bir alıntı; teyitli kalemleri normal ağırlıkta kullanıldı) · iç envanter 8/9 kaynak-koddan bağımsız doğrulandı.

## Hayatta-kalma sayımı
Hakem kalemleri 15+9 alt-iddia: **A: 1 SAĞLAM / 7 DARALDI (Kural-Taslak-1..7) / 5 mutlak-form düştü · B: 1 SAĞLAM / 5 DARALDI / 3 alt-iddia düştü.** Hakem-A antitezin de 4 aşımını kaydetti (adversarial simetri). V26: tez-tarafı 8/8 PASS, antitez-A 6/6 PASS, antitez-B K-DÜŞÜŞ.

## Sentez — Salih'in sorusuna cevap
**"Lineer bağımsızlık" sezgisinin formal adı Bernstein Koşulları'dır** (ajan adsız aramada kendisi buldu): iki birim ancak `yazar₁∩yazar₂=∅ ∧ yazar₁∩okur₂=∅ ∧ okur₁∩yazar₂=∅` ise paralel-güvenlidir. **Ama hakemlik net ayrım koydu: bu koşul GEREKLİDİR, tek başına YETERLİ DEĞİLDİR** — dört belgeli delik: ① beyan edilmemiş/görünmez ayak izleri (LLM-ajanlarda ölçülü: özdeş 1000 koşum → 80 farklı çıktı) ② granülerlik seçimi sonucu değiştirir ③ dışa-görünür yan etkiler kesişimsiz işleri de sıralatır ④ kümeler statik bilinemeyebilir. Çözüm literatürde de bizde de aynı: **beyan + zorlama + doğrulama** üçlüsü (hermetiklik varsayım değil rejimdir) ve **sıralama ↔ dışlama iki ayrı eksendir** (DAG `sira` + adlandırılmış kira).

## PROTOTİP-1 — Birim-manifest şeması (pipeline + loop ortak; ADAY, hüküm masada)
```json
{
  "birim_id": "İB-xx | loop:katman-hatti",
  "tur": "pipeline | loop",
  "pist": "K-010 | K-015 | K-022 | meta",
  "okur": ["kuyruk/senaryo-defteri.md", "veri/baglam.sqlite#kayit"],
  "yazar": ["cc/rapor-*.md"],
  "granul": "dosya | bolum | kayit",
  "sira": ["İB-yy"],
  "dislama_grubu": "silver-yazar | kanon-yazar | null",
  "silver": "okur | yazar | hayir",
  "commit_kapsami": ["yol-listesi"],
  "kanon_yuzeyi": false,
  "dis_etki": ["push", "bildirim"],
  "idempotency_anahtari": "opsiyonel",
  "zorlama_modu": "worktree | yol-kapisi | yok",
  "beyan_disi_politikasi": "hata | seri",
  "iterasyon_ayak_izi": "sabit | buyuyen",
  "tetik_turu": "zamanli | olayli | seans",
  "durma_kosulu": "loop için zorunlu",
  "kapsam_beyani": "ajan-birimse zorunlu",
  "belirlenimsiz_girdi": ["model-çıktısı", "web"],
  "dogrulama_kapisi": "test/karşılaştırma adımı"
}
```
Alan kaynakları: ilk 6 + zorlama üçlüsü + ajan-üçlüsü = hakem-A Kural-Taslak-1..7'nin birebir aktarımı; `dislama_grubu`/kira = hakem-B m.5-6; loop-üçlüsü = emir kapsamı; **`pist` = bugünkü hız-sapması dersinden** (otonomi-pisti payı ölçülebilir olsun — 26 gün/%2 vakası bir daha görünmez kalmasın).

## PROTOTİP-2 — Paralellik kural listesi (PK; ADAY, m.29 deneysel damga önerisiyle)
- **PK-1 (gereklilik/Bernstein):** çakışan çift (aynı öğe ∧ ≥1 yazma) → ya AYRIK ya `sira` kenarıyla SIRALI; ikisi de değilse koşum RED.
- **PK-2 (yeterlilik şerhi):** PK-1 geçse bile `dis_etki≠∅ ∨ belirlenimsiz_girdi≠∅` → PK-9/PK-6 devrede; paralel-izin güvenlik verir, doğruluk `dogrulama_kapisi`nındır.
- **PK-3 (granül eşitliği):** kesişim denetimi iki birimin ORTAK granülünde; belirsizlik → dosya granülüne terfi (kaba-güvenli).
- **PK-4 (beyan zorlaması):** hermetiklik varsayılmaz — `zorlama_modu` ile kısıtlanır; beyan-dışı erişim `beyan_disi_politikasi`na göre gürültülü hata ya da otomatik-seri.
- **PK-5 (silver tek-yazar):** `silver:yazar` iki birim ASLA paralel; tek uygulama-kuyruğu + `busy_timeout` (dolarsa kuyruğa iade, "dene-geç" değil); `dislama_grubu:"silver-yazar"` zorunlu.
- **PK-6 (kanon yüzeyi):** `kanon_yuzeyi:true` birim HER ŞEYLE sıralı + Salih imza hattında; hiçbir otomasyon paketine paralel giremez.
- **PK-7 (çift eksen):** `sira` (statik DAG, çevrimsiz, koşumda keşif yasak — keşif gerekirse restart) ↔ `dislama_grubu` (adlandırılmış kira: TTL + sahip + yenileme + ölü-sahip süpürgesi; **Salih'in koyduğu kilit asla süpürülmez**).
- **PK-8 (bütünlük + tazelik ayrı):** durum-dosyası yazımı write-then-swap; bayat-okuma freni ayrıca sürüm-damgalı KOŞULLU yazma ister (atomic-rename bayat-okumayı KAPSAMAZ — git lockfile.h "eski VEYA yeni" garantisi).
- **PK-9 (dış etki):** `dis_etki`li birim (push, bildirim, dış-API) ya seri-sınıf ya idempotency-anahtarlı; retry kimliği graf-dışı kalıcı kayıtta.
- **PK-10 (loop iterasyonu):** iki loop ancak ayak izleri HER iterasyonda ayrıksa paralel; `iterasyon_ayak_izi:"buyuyen"` → her N iterasyonda kapı yeniden değerlendirir.
- **PK-11 (koşum-önü kapı):** paralel paket açılmadan `tools/paralel-kapi.py` (LLM'siz, Karar 65) manifest çiftlerini tarar → çift başına PARALEL-SERBEST / SIRALI(neden) / RED(neden); kapısız fan-out yasak (İB-54 freninin küme-düzeyi tamamlayıcısı).
- **PK-12 (ana-oturum önceliği):** loop, ana-oturumun beyan edilmiş yazar-kümesine dokunuyorsa bekler — canlı-paralel H4 kuralının loop düzlemine genelleşmesi.

## 4-düzlem matrisin bugünkü somutları (iç envanter, 8/9 doğrulanmış)
| Düzlem | En riskli gerçek çift | Çözen kural |
|---|---|---|
| loop×loop | katman-hatti × katman-hatti (kilitsiz tmp→replace, son-yazan-kazanır — bugün yalnız el kararıyla önlendi) | PK-5 + PK-7 kira |
| pipeline×pipeline | İB-58 × İB-30 (ikisi de `tools/katman-hatti.py` yazar) | PK-1 → SIRALI |
| loop×pipeline | seans-kapanış (katman-hatti çağırır) × herhangi silver-yazan İB | PK-5 dışlama-grubu |
| loop×ana-oturum | hareket-kütüğü/bayat-çekim × ana-oturumun düzenlediği dosyalar | PK-12 |
Yapısal boşluklar (doğrulanmış): koşum-önü yazar∩yazar kontrolü bugün HİÇBİR yerde yok · `deny:[]` → core/ Edit/Write makine-korumasız (tel yalnız Bash) · kira/kilit mekanizması 0.

## Masa-girdisi (Salih tetiğiyle açılır — implement hükümleri)
① PK-seti + manifest-şeması imzası (m.29 deneysel, pilotla) · ② manifest doldurma turu: açık ~20 İB + 13 loop birimine ayak-izi beyanı (İB-63 devam adımı; kaynak: tez-C envanteri) · ③ `tools/paralel-kapi.py` icrası (deterministik kapı) · ④ ACİL mekanik frenler: settings.json deny'e core/ Edit/Write satırı + katman-hatti'ye kira dosyası + İB-58→İB-30 sıra kenarı · ⑤ İLK PİLOT: kapının PARALEL-SERBEST verdiği 2-3 İB ile "tek prompt çok pipeline" denemesi — **K-010 A3 kontrol-devri kapısına doğrudan kanıt üretir** · ⑥ `pist` alanının hız-ölçümüne bağlanması (otonomi-pisti pay sayacı).

## Cevaplanmamış sorular (karar biriktirilmedi)
1. Manifest'ler nerede yaşar — birim başına dosya mı (`veri/manifest/*.json`) tek JSONL mi? (kapı-script tasarımıyla birlikte)
2. `granul:"kayit"` (silver satırı) denetimi ilk sürümde mi, dosya-granülüyle mi başlanır?
3. Kira dosyalarının konumu ve ölü-sahip süpürge eşiği (TTL değeri) — ölçümsüz, pilotta seçilir.

*Hüküm Salih'te; şema+kurallar ADAY (m.31). Hayatta-kalma gözlemi deftere tek satır.*
