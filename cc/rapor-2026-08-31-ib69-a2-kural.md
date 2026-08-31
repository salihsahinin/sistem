# İB-69 AİLE-2 (c) — Matris-koşum kurallaştırma: manifest taslağı + prompt şablonu + fren kuralları

**Künye:** rol tez-c · AS-OF 2026-08-31 · model sonnet (Sonnet-5, `[rejim: maliyet-öncelikli]`) · HEAD `c1f5c05` · **kanona dokunulmadı** (`core/`, `CLAUDE.md`, `kuyruk/`, `tools/`, `veri/manifest/` salt-okundu, yazılmadı) · yazılan tek dosya bu rapor.

**Okunan dosyalar:**
- `raporlar/2026-08-31-ib69-matris-a1-formalizasyon.md` (tam, §1-8)
- `raporlar/2026-08-31-ib65-loop-pipeline-secim-atlas.md` (satır 190-262, §4 model-3 + §5 seçim şeması)
- `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md` (satır 160-270, §5.1-5.3 + §6)
- `veri/manifest/ib-69-a1.json`, `veri/manifest/ib-65-loop-pipeline-atlas.json` (pipeline örnek) — loop örneği ayrı bulunamadı, `ib-a2-tatbikat.json` (pipeline, `sira` alanlı) ikinci referans olarak kullanıldı
- `.claude/hooks/pretool-ajan-fren.sh` (tam, satır 1-60)
- `core/pano.md` (K-010 kartı, A1 tanımı) · `core/tuzuk-v0.md` m.46(d) · `kuyruk/k010-zincir-2026-08-29.md` (A1 sayaç durumu)

---

## P1 — Manifest matris-koşum birim tipi (TASLAK, iki seçenek)

### S-A: `tur` değer kümesine `matris` eklemek

```
TUR ::= {pipeline, loop, hibrit, belirsiz, matris}          [İB-65 §5.1 dörtlüsüne 5. değer]
Y4 (yeni yüklem): eksen_carpimi_tanimli?
  Y4 = E ∧ Y1(SÜREKLİ?) = H ∧ Y3(iç-sıra-sabit) = E  →  tur = matris
```
Yüklem-ağacına Y1-Y3'ün YANINA dördüncü soru eklenir; `matris` `hibrit`ten ayrışır çünkü hibrit'in iç/dış tavanı (N,M) SAYIdır, matrisin iç/dış "tavanı" bir EKSEN listesidir (`|eksenler|≥2`, kardinalite değerlerden — İB-69/A1 §1 Ö1/Ö2). Yani matris hibritin bir alt-sınıfı değil, kardinalite kaynağı farklı KARDEŞ bir sınıf.

- **Artı:** tek alanda kalır, mevcut `tur`-okuyan her araç (`tools/loop-dedektor.py`, `katman-hatti.py` — okumadım, isim eşleşmesi) zaten enum genişlemesine dayanıklı olmalı (m.40c düşük sınıf, İB-65'in `hibrit` eklemesiyle AYNI risk sınıfı).
- **Eksi:** yüklem ağacı 3'ten 4'e çıkar → İB-65'in "belirsiz" dalına yeni bir çakışma yüzeyi açılır (SÜREKLİ ∧ iç-sıra-sabit ∧ eksen-çarpımı-var — hibrit mi matris mi belirsiz kalabilir, ayrım netleştirilmeli).
- **Göç maliyeti:** taradığım 17 manifestten (`ls veri/manifest/`) **0 tanesi** matris-koşum yapıyor — bugün hiçbir mevcut manifest `tur=matris` gerektirmiyor, göç maliyeti **0 dosya**. Yeni birimler bu değerle DOĞAR.
- **İB-65 %29 açığıyla ilişki:** doğrudan aynı boşluğun devamı — İB-65'in 24 birimlik envanterinde matris-koşum sınıfı hiç YOKTU (İB-69/A1 kendisi de "prototip koşulmadı" diyor), yani %29 açık matrisi KAPSAMIYORDU; S-A o envantere beşinci bir dal ekliyor, geriye dönük düzeltme değil ileriye dönük genişleme.

### S-B: `tur`'a dokunmadan ayrı `matris: {...}` bloğu

```
tur ∈ {pipeline, hibrit}  (değişmez)  ∧  matris = {eksenler, tekrar, erken_durdurma, hucre_tipi} | null
Zorunlu-alan yüklemi:
  matris ≠ null  →  ( |matris.eksenler| ≥ 2 ∧ (∃e: e.rol=dis) ∧ (∃e: e.rol=ic) )    [İB-69/A1 §1 Ö1]
  matris ≠ null ∧ matris.erken_durdurma = kademe_esigi  →  matris.esik ZORUNLU ∧ matris.esik SABİT
```
- **Artı:** `tur` yüklem-ağacı 3 sorudan büyümez, İB-65 şemasına SIFIR dokunuş; matris bilgisi (eksen listesi, tekrar, hücre tipi) zaten kendi iç yapısı olan bir blok, `tur` gibi tek-atomlu bir sınıflandırıcıya SIKIŞTIRILMAK zorunda değil — İB-69/A1 §1'deki `MATRIS` tipi zaten kendi başına bir obje.
- **Eksi:** iki kaynaktan okunur hâle gelir (`tur` VE `matris` birlikte okunmalı) — bir aracın yalnız `tur` okuyup matris varlığını KAÇIRMASI riski (`tur=pipeline` + `matris≠null` ise araç bunu hâlâ "düz pipeline" sanabilir); İB-66 §5.2'nin "alt-süreç başlatma yeni seviye doğurur" ilkesiyle örtüşmesi zorunlu hâle gelir çünkü `matris` bloğu görünürde `tur`'u DEĞİŞTİRMİYOR ama fiilen ikinci bir sayaç ailesi (eksen×eksen×tekrar) ekliyor.
- **Göç maliyeti:** S-A ile aynı, **0 dosya** — hiçbir mevcut manifest'te `matris` alanı yok, hepsi `null` sayılır.
- **İB-65 %29 açığıyla ilişki:** DOLAYLI — S-B, tur şemasını genişletmediği için İB-65'in kendi 5-değerli önerisiyle PARALEL akar, çakışmaz; ama matris-türü birimler `tur=hibrit` görünüp içeriden matris olacağı için envanter taramasında (İB-65 §2 tarzı elle sınıflama) gözden kaçma riski S-A'dan yüksek.

**Öneri belirtilmez (görev talimatı gereği) — HÜKÜM VERİLMEDİ, iki seçenek de eksiksiz.** [not: final mesajda kişisel değerlendirme "artı/eksi ağırlığı" olarak verilecek, bu bir HÜKÜM değil, öneri gerekçe notu.]

---

## P2 — Prompt şablonu: dış-loop → iç-matris çağrısı

İB-66 Şablon-1'in bütçe yüklemini **aynen devralıyorum** (yeniden türetmiyorum), yalnız KAPI-2 çağrı sayacını ekliyorum:

```
GİRDİ SÖZLEŞMESİ: veri/sozlesme/<is>-eksen.json  (İB-69/A1 §1 EKSEN/MATRIS şeması)

DIŞ EKSEN YİNELEMESİ (i_dis = 1..|dis.degerler|):
  ∀ i_dis: kurulum_dis(i_dis)                      [M_dis — bağlam/skill yükleme, bir kez]

  İÇ EKSEN YİNELEMESİ (i_ic = 1..|ic.degerler|, tekrar t=1..tekrar):
    ∀ (i_dis, i_ic, t): hucre_anahtari := serile(i_dis, i_ic, t)     [İB-69/A1 §2, TEKİL]
    RESUME YÜKLEMİ (İB-69/A1 §5):
      hucre_anahtari ∈ kütük_anahtarlar  →  atla (idempotency)
      hucre_anahtari ∉ kütük_anahtarlar  →  HÜCRE ÇAĞRISI

    HÜCRE ÇAĞRISI:
      cikti := cagir(sablon_id, eksen_degerleri)  ;  cikti.tip ∈ {etiket,sayi,sema}  [Ö1, §2]
      KÜTÜK APPEND: bronz jsonl satırı (İB-69/A1 §5 13 alan; append-only)

  Ö1 (ÖN-KOŞUL, İB-66 Şablon-1 — AYNEN DEVRALINDI):
    (b_iç ≥ T_hücre) ∧ (N_dış × N_iç × tekrar × b_iç ≤ 0,8 × B_oturum)  →  koşuma izin ver
    ¬(...)  →  koşma; |ic| ∨ tekrar küçült ∨ Salih'e bildir

  KAPI-2 ÇAĞRI SAYACI (İB-69/A1 §4 KAPI-2 — YENİ, Şablon-1'de YOKTU):
    N_cagri := N_dış × N_iç × tekrar   (yalnız hucre_tipi=tek_cagri ise sayaca girer;
                                          gnhf_iterasyonu hücreler .claude/hooks/pretool-ajan-fren.sh
                                          matcher'ından farklı yoldan geçebilir — [?] doğrulanmadı)
    Ö2: N_cagri + sayac_oturum ≤ DURDUR(144)  →  devam
    ¬Ö2 → matrisi oturuma BÖL (kütük append-only + hucre_anahtari ile resume — YUKARIDAKİ
          RESUME YÜKLEMİ zaten bunu karşılıyor, ek mekanizma gerekmiyor)

DURMA YÜKLEMİ:
  done ↔ ( ∀(i_dis,i_ic,t): hucre_anahtari ∈ kütük_anahtarlar )  ∨  ( B_harcanan ≥ 0,8×B_oturum )
```

**Matris seviye midir? — İB-66 §5.1'in üç şartıyla test:**
(i) kendi yineleme sayacı var mı → EVET, `hucre_anahtari` çifti (i_dis,i_ic,t) bunu taşır.
(ii) kendi durma yüklemi var mı → EVET, yukarıdaki DURMA YÜKLEMİ.
(iii) gövde alt-seviyenin TAM koşumunu içeriyor mu → **KOŞULLU**: `erken_durdurma=yok` (tam faktöriyel) ise EVET, her dış değeri için iç eksen TAM koşulur → **2 SEVİYE** (İB-69/A1 §6.3: `tam_faktoriyel ∧ ¬erken_durdurma → 2 SEVİYE [D]`). `erken_durdurma=kademe_esigi` ise (iii) KIRILIR — büzülen aday kümesi tam kapsamayı bozar → İB-66 §5.2'nin HİÇBİR sınıfına (a-e) girmiyor, yeni bir alt-tür.

**Cevap:** Matris **5. şablon DEĞİL** — tam-faktöriyel hâli Şablon-1(dış)+Şablon-2(iç)'in DOĞRUDAN İKİ-BOYUTLU örneklemesi (dış eksen = Şablon-1'in `N`, iç eksen = Şablon-1'in iç koşum listesi, tekrar Şablon-2'nin `Δdurum_dış` kontrolüyle eşleşir — her hücre kendi ölçülebilir jsonl satırını üretir, "yaptım" beyanı değil). Kademeli (erken-durdurma) hâli ise gerçekten YENİ bir alt-tür — İB-69/A1 §6.3'ün kendi hükmü ("YENİ ALT-TÜR → MASAYA") ile bu rapor aynı sonuca varıyor, çelişki yok.

---

## P3 — Fren kuralları

### hücre-tavanı

**Türetim (İB-69/A1 §4 KAPI-2'den):**
```
N_cagri + sayac_oturum ≤ DURDUR(144)     [.claude/hooks/pretool-ajan-fren.sh:9, satır-içi yorum 5-10]
→  N_hücre ≤ 144 − sayac_oturum_anlik
```
Bu ham tavan oturum-anlık sayaca bağlı, sabit değil. Planlama-zamanı SABİT bir sayı için iki emsal var:
1. **KAPI-1'in 0,8 güvenlik payı deseni** (İB-69/A1 §4, İB-66 Şablon-1 Ö1 ile aynı desen): `0,8 × DURDUR = 115,2 ≈ 115` — tek matrisin TEORİK üst sınırı (oturum başında hiç sayaç harcanmamışsa).
2. **İB-07 emsali:** eski eşik UYARI=72'de gerçek matris (60 hücre + ~5 lider çağrısı ≈ 65) kesintiye YAKLAŞMIŞTI (İB-69/A1 §4: "İB-07'nin andığı '72=DUR' ESKİ eşik"). Yani tek bir matrisin `sayac_oturum`u SIFIRDAN başlattığı bir senaryoda bile 65 hücre gerçek bir oturumun YARISINI harcamış.

**Öneri sayı:** tek bir matrisin oturum payı **≤ 72** (= DURDUR'un yarısı, 144/2), gerekçe: (a) İB-07 emsali 60-65 hücrenin ESKİ DURDUR eşiğini (72) doldurma noktasına geldiğini gösteriyor — YENİ DURDUR (144) altında aynı ORANI (yarı) korumak matrisi "oturumun tek işi" varsayımına HAPSETMİYOR, geri kalan payı diğer ajan çağrılarına (lider koordinasyonu, diğer İB'ler) bırakıyor. (b) 0,8×144=115 rakamı KAPI-1'in token bütçesi için tasarlanmış payı, çağrı-sayısı için doğrudan taşınması gerekçesiz olur (token ile çağrı-sayısı farklı kaynaklar) — bu yüzden 115 değil 72 öneriliyor. **Bu bir ÖNERİ, hüküm değil** — sayısal kalibrasyon borcu M-1'in (İB-69/A1 §8) bir yan-dalı olarak masaya girmeli.

### bütçe kalıtımı

İB-66 Şablon-1/3'ten devral, matrise uyarla: **TEK SAYAÇ**. Gerekçe — İB-65 §5.1'in `hibrit` tanımında zaten `butce_sayaci = "tek"` zorunlu kılınmış (dis_tavan × ic_tavan tek çarpım, ayrı sayaç yok); matris bunun eksen-versiyonu, aynı ilke geçerli: `N_dış × N_iç × tekrar` tek bir `N_cagri` sayısına toplanır (P2'deki KAPI-2 formülü), dış ve iç eksenler AYRI ajan-fren sayacı TUTMAZ — ikisi de aynı `.claude/hooks/state/ajan-fren-<sid>.json` dosyasındaki tek `sayac`a yazılır (hook zaten oturum-genelinde tek sayaç tutuyor, satır 27-30). Şablon-3'ün fren-kalıtımı ilkesi (her T teli ya açıkça bildirilir ya devre-dışı bırakılır) matrise AYNEN uygulanır: hücre çağrıları `.claude/hooks/pretool-ajan-fren.sh` matcher'ı `Agent`/`Task` olduğu için hücre_tipi=tek_cagri ise otomatik sayılır, ama hücre_tipi=gnhf_iterasyonu ise CLI-içi koşum bu hook'tan GEÇMEYEBİLİR — bu **doğrulanmamış** bir varsayımdır [?], P2'de aynen işaretlendi.

### A1-sicil ilişkisi

**Bulundu.** `core/pano.md:34` (K-010 kartı) + `kuyruk/k010-zincir-2026-08-29.md:55`: A1 = **"5 ardışık başarılı OTOMASYON-KOŞUMU ∧ açık incident 0 — birim KOŞUM (takvim değil)"** (Karar 81 EK-2, Salih imzası 08-30: "birim=pipeline-koşumu okuması ONAYLI"). Güncel durum: **A1 5/5 KESİN** (39-dk pencere yeterli sayıldı, c=0≠reliability şerhi kayıtlı).

**Matris koşumunun A1 sicilini etkisi:** A1 birimi "pipeline-koşumu" olarak okunuyor — matris bir `tur=matris` (S-A) ya da `tur=hibrit ∧ matris≠null` (S-B) birimidir, `tur=pipeline` DEĞİLDİR (İB-65 §5.1 yüklem-ağacında matris SÜREKLİ=H dalına girmiyor, tekrarlı-iç-sıra-sabit dalına giriyor). Yani **matris koşumu A1 sayacına doğrudan +1 KATKI VERMEZ** — A1 tanımı "pipeline-koşumu" okumasıyla ONAYLANMIŞ, matris bu okumaya sığmıyor. Bu bir ÇELİŞKİ değil bir KAPSAM-DIŞI bulgusu: A1 sicili DONDU (5/5 KESİN), yeni birim sınıfının geçmişe dönük etkisi yok; ileri dönük olarak matris-koşumları A1-benzeri ayrı bir sicil mi tutmalı sorusu masaya AÇIK BIRAKILIYOR (Katman-1, bu rapor hüküm vermiyor).

### çağrı-sayacı kapısı

`.claude/hooks/pretool-ajan-fren.sh` satır 9-10 (yorum) + kod satır 31-40: eşikler UYARI=72 / **DURDUR=144** (Salih B-hükmü 2026-08-31, devir `cc/devir-2026-08-31-opus-icra.md`, revizyon gerekçesi: "sayaç oturum-geneli ve alt-ajan çağrılarını da sayıyor → lider→işçi iki-katmanlı koşum tek-katman tabanını yapısal aşıyor"). Sayaç `matcher: Agent` olan HER PreToolUse çağrısında +1 artar (kod satır 27: `st["sayac"] += 1`), **alt-ajan çağrıları dahil** — bu satırın kendisi doğrulama: hook `tool_name in ("Agent","Task")` filtresiyle çalışıyor, alt-ajanın kendi Agent çağrısı da aynı `session_id` state dosyasına yazıyor (satır 22-24). **İB-07 emsali:** eski DURDUR=72 eşiğinde İB-07'nin 60-hücrelik matrisi + ~5 lider çağrısı (İB-69/A1 §4: "51 işçi denemesi... lider ~65 kendi çağrısı") eşiğe ÇOK YAKLAŞTI — bu YENİ DURDUR=144 altında aynı büyüklükte bir matris payının rahat sığdığını, ama 2-3 katı büyüklükte bir matrisin (örn. 20×3×3=180 hücre) YENİ eşiği de aşacağını gösteriyor. Bu yüzden hücre-tavanı önerisi (≤72) yalnız kalibrasyon rakamı değil, aynı zamanda BU eşiği aşmamak için bir GÜVENLİK PAYI.

---

## UYUM DENETİMİ

- **Aile-1 şemasına (İB-69/A1) uyum:** EKSEN/MATRIS tipleri (§1), HÜCRE tipleme kuralı (§2 Ö1), KAPI-1/KAPI-2 maliyet modeli (§4) ve KÜTÜK 13-alan standardı (§5) **AYNEN** kullanıldı, yeniden türetilmedi. AYRILMA YOK.
- **İB-65 §5'e uyum:** S-A, İB-65'in `{pipeline,loop,hibrit,belirsiz}` dörtlüsüne 5. değer olarak `matris`ı EKLİYOR, dörtlüyü BOZMUYOR; S-B dörtlüye hiç DOKUNMUYOR. AYRILMA YOK — iki seçenek de İB-65'in kendi §5.2 kapanışında bıraktığı "M3 arşive alınmaz, kuyrukta tutulur" notuyla tutarlı: matris de benzer biçimde masaya öneri olarak bırakılıyor, hüküm verilmiyor.
- **İB-66 §5'e uyum:** Şablon-1'in Ö1/Ö2/Ö3 yüklemleri **birebir** devralındı (yeniden türetilmedi — görev talimatına uyuldu). **AYRILMA:** İB-66 Şablon-1'de KAPI-2 (çağrı sayacı) YOKTU — bu rapor onu EKLEDİ, çünkü İB-69/A1 §4 KAPI-2'nin "token'dan BAĞIMSIZ, İB-07'yi kesen kapı BUDUR" tespiti Şablon-1'in token-only bütçesinde eksikti. Bu bir GENİŞLETME, çelişki değil — İB-69/A1 §6.2 zaten aynı tespiti yapmış ("Doğru fren §4 KAPI 2'dir — hiçbir tez raporu bunu maliyet modeline koymamıştı"), bu rapor o boşluğu Şablon-1'e taşıyarak kapatıyor.
- **Seviye sorusu:** İB-66 §5.1'in üç şartıyla test edildi, sonuç KOŞULLU (tam-faktöriyel → 2 seviye; kademeli → yeni alt-tür) — bu, İB-69/A1 §6.3'ün KENDİ hükmüyle (`tam_faktoriyel ∧ ¬erken_durdurma → 2 SEVİYE [D]`; `kademe_esigi → YENİ ALT-TÜR → MASAYA`) **birebir örtüşüyor**, iki bağımsız kaynaktan aynı sonuca varıldı. AYRILMA YOK.
