# Bağlam Anahtar Kaydı v1 — tekilleştirme anahtarları · emeklilik · yayılım · metrik (2026-08-15, Salih Katman-1; sabitler deneysel m.29)

*Kanon: Jarvis bağlamı (markdown kanon + skill dosyaları + git) bir **silver katman** gibi yönetilir — her kavram/tetik/ad için **tek** kararlı anahtar, **tek** güncel değer, emekli değerlerin damgalı (silinmeden) emekliye ayrılması ve bu emekliliğin **tüm** sıcak hafızaya **yayılması**; bakım kararları metrikle. Emir: Salih 08-15 seans-3 ("tekilleştirme anahtarı = 'günaydın'→skill bağını tüm hafızadan silmek; yönetim metrikle"). Kanıt: `cc/rapor/2026-08/rapor-2026-08-15-6.md` (m.40b 4 aile, 95 iddia → 40 `SAĞLAM` / 55 `DARALDI` / 0 `DÜŞTÜ`; V26 11/12); emir `cc/gorev/2026-08/gorev-2026-08-15-6.md`; manifest `cc/pipeline/pipeline-2026-08-15-baglam-silver-katmani.md`. Veri altyapısı: `tools/baglam-tablo.py` → `veri/baglam.sqlite` (referans/anahtar tabloları). Denetim: `tools/anahtar-denetim.py`. Kanon dili Türkçe; [A-YT1] gibi köşeli atıflar rapor-6 hakem yapı-taşlarıdır.*

## 1. İlkeler (kanıt-damgalı)
1. **Anahtar = kararlı kimlik; ad/tetik = sürümlenen öznitelik.** Anahtar "akıllı" değildir, görünen addan türetilmez; "günaydın" bir anahtar değil, `oturum-acilis-tetigi` anahtarının `EMEKLİ` bir **değeridir** [A-YT1 Kimball; D-YT3 SKOS: dil başına en fazla **bir** tercih-edilen ad; V24 isim disiplini = anahtar-kararlılığı taahhüdü].
2. **Tekillik iki düzeyde ölçülür, bozulma üç tiptir:** (a) aynı anahtar özdeş kopya · (b) farklı anahtar aynı kavram (çift sayfa/eşanlam) · (c) aynı anahtar farklı kavram — **anlam kayması = tip-c'nin ölçülebilir tanımı** (kalıntı bağlantı eski anlamı yeni ada taşır) [A-YT2 **dama-nl** DDQ]. Jarvis'te anlam kayması istatistik/gömme ile **değil** deterministik ölçülür: kalıntı-referans sayımı + anahtar çakışması + kavram-sayfası tanım-diff'i [C-YT8: 10² dosyada drift detektörleri/embedding **girmez**].
3. **Sürümleme SCD-2 + çift-zaman:** her değer `gecerli_bas` / `gecerli_bitis` taşır; **tek-güncel** ⟺ `gecerli_bitis` boş; olay-zamanı (karar tarihi) ↔ işlem-zamanı (git commit) ayrı eksenlerdir [A-YT3 dbt/Kimball; B-YT1 Zep]. **Damgasız kayıt kabul edilmez** — güncel değer `max(tarih)`/serial ile **deterministik** seçilir, LLM'e sorulmaz (deterministik seçim LLM-yargısını +10,8 pp geçer; serial yoksa kazanç yok) [B-YT2].
4. **Tek-güncel-değer = açık survivorship kuralı:** kaynak-önceliği **Salih emri > tüzük > kapsül > kuyruk/kutu** → beraberlikte son commit (LUD) → tam beraberlikte commit sırası; kural yazılıdır, "en yeni = doğru" varsayılmaz [A-YT4].
5. **Emeklilik = damga + gerekçe + halef + tarih; silme değil** (m.8): `durum: emekli` · `gerekce` · `replaced_by` **TEKİL** (çoklu/insan-kapılı aday için `consider`) · `tarih`; çevrim yasağı (A→B→A) [D-YT1 OWL/OBO/Wikidata; A-YT5 dbt hard_deletes: politika ilk yazımdan **önce**]. Emeklilik ayrı `[icra]` commit'tir; **kaldırma** (kaydı arşive indirme) ayrı commit ve ≥3 vardiya sonra [D-YT4 SemVer/PEP 387 — 3 = deneysel m.29].
6. **Yayılım (cascade) = açık yeniden-yazım, kendiliğinden gelmez:** çelişkili iki sürüm yan yana bağlamda %85-87 → %10-44 doğruluk; parametrik dalga %38-66 ↔ açık yazım %82,8 [C-YT1 WikiContradict/RippleEdits]. Yayılım deterministik grep-cascade + yetim-referans raporuyla yapılır, model yargısına bırakılmaz (yazma-anı LLM geçersiz-kılma %3,3) [D-YT2 Z39.19 §11.4.3(c); B-YT4 LightMem]. Semantik **RESTRICT**: sıcak katmanda kalıntı referans varken emeklilik **tamamlanmamış** sayılır [A-YT7 PostgreSQL]. Onarım-önce: yalnız kaynağı+kronolojisi doğrulanmış geçişler yeniden yazılır (repair-only %3 gereksiz yazım vs full %80) [B-YT3 StateAuditor]. Sıra **backward**: (1) okuyucular çift-değer tanır → (2) kanon standardı yeni değere → (3) eski değer emekli-damgalı; **transıtıve**: tüm eski varyantlar tanınır [A-YT7 Schema Registry].
7. **Sıcak bağlama tek sürüm çıkar:** emekli değer sıcak katmanda "yanında not" olarak **durmaz** (model çatışmayı bildirmeden sessizce seçer; araç/dosya yüzeyinden gelen çelişkide hiyerarşi uyumu %98→%20) [B-YT7 PRIMEBench/IH-Benchmark]; damga **tek** yerde görünür (bu kayıt) — görünmeyen damga yok hükmündedir [D-YT8 PEP 565]. **Skill description = tetik yüzeyi ⇒ emekli tetik description'dan çıkarılır** [B-YT6 Anthropic]; alias yalnız exact-match türü ve soğuk katmanda pointer olarak yaşar; alias zinciri derinlik ≤1 [D-YT3, D-YT6].
8. **Emeklilik olay-tabanlıdır, "sonra güncelleriz" değildir:** tetiksiz bakımda bağlantıların <%10'u revize edilir; düzeltme olduğunda hedef değiştirme/güncelleme baskın, silme %6-13 [C-YT2]. Kanca: her ad/tetik/kural değişimi → aynı vardiyada emeklilik protokolü (§3); denetim script'i vardiya-kapanış + damıtma turlarında koşar.
9. **Otomatik çelişki/kayma alarmı = ikinci göz, kapı değil:** LLM çelişki-denetçisi FP %22-56 / FN %64'e kadar [C-YT7] ⇒ script yalnız **deterministik** sayım yapar; anlamsal aday listesi Salih triyajına gider (K2 topraklamadaki bağımsız-doğrulayıcı konumu). Cascade koşumu "diff üret → insan onayı" modelindedir; %100 otomatik değil [D-YT8 Piranha %17/%35].
10. **Kanonik ad kuralı:** kavram başına EN **fazla bir** tercih-edilen ad; tercih/alias ayrık; bir alias birden çok hedefe yalnız açık çok-anlamlılıkla gider [D-YT3 SKOS S13/S14; Z39.19 §8.2].

## 2. Anahtar kaydı (makine-okur — `tools/anahtar-denetim.py` bu bloğu okur; alan adı talimattır)
Alanlar: `anahtar_id` (slug, kalıcı) · `tur` ∈ {tetik, skill_adi, yuzey, kavram, kart, dosya} · `guncel` {deger, gecerli_bas, kaynak} · `emekli[]` {deger, varyantlar[], tarih, gerekce, replaced_by, izinli_kaliplar[] — tarihçe-damgası gibi **meşru** bağlamlar (regex, Türkçe-ASCII/büyük-küçük duyarsız), kaldirma_en_erken} · `aday[]` (Salih kararı bekleyen emeklilikler; denetimde **sayılır**, ihlal **üretmez**) · `not`. Kural: `emekli` satırı `tarih` + `replaced_by` olmadan yazılamaz; `replaced_by` tekil; çevrim yasak.

```json
{
  "sema": "anahtar-kaydi-v1",
  "guncelleme": "2026-09-15 (İB-90: ajan-adi anahtarı — Carvis→Jarvis, Karar 93, emekli-anahtar-cascade ilk canlı koşum) · önceki 2026-08-17 (seans-8: metafor emekliliği paketi — 5 anahtar EMEKLİ, halef sözlük Salih ONAYLI ~10:15; cascade koşuldu)",
  "anahtarlar": [
    {
      "anahtar_id": "oturum-acilis-tetigi",
      "tur": "tetik",
      "guncel": {
        "deger": "seans başı",
        "gecerli_bas": "2026-08-15",
        "kaynak": "Salih Katman-1 08-15 (7d349b5) + seans-3 emri (bağ tüm hafızadan)"
      },
      "emekli": [
        {
          "deger": "günaydın",
          "varyantlar": [
            "gunaydin",
            "günaydın carvis",
            "günaydın jarvis",
            "günaydın jarvis geliştirme",
            "günaydın staj",
            "günaydın, prototip",
            "günaydın, portrisk",
            "günaydın vardiya"
          ],
          "tarih": "2026-08-15",
          "gerekce": "zaman-kayması: selamlama zaman işareti sanılıyor; tetik oturum-sınırı işaretidir (Salih 08-15). Kalıntı bağ = tip-c anlam kayması riski (rapor-6 A-YT2/B-YT6).",
          "replaced_by": "seans başı",
          "izinli_kaliplar": [
            "günaydın vardiyası",
            "günaydın vardiyasi",
            "\\bgunaydin-vardiya\\b",
            "\\d\\d-\\d\\d günaydın",
            "ikinci günaydın",
            "günaydın\\)",
            "anahtar_terim",
            "emekli",
            "kelimesinin skille",
            "\\bkaç dosyada\\b",
            "günaydın 1\\d\\d dosya"
          ],
          "kaldirma_en_erken": "vardiya+3"
        }
      ],
      "aday": [],
      "not": "İlk koşum vakası. izinli_kaliplar: tüzükteki imza-damgaları ('… günaydın vardiyası') tarihçedir, yeniden yazılmaz; skill klasör adı ayrı anahtar (skill:gunaydin-vardiya)."
    },
    {
      "anahtar_id": "oturum-kapanis-tetigi",
      "tur": "tetik",
      "guncel": {
        "deger": "seans bitimi",
        "gecerli_bas": "2026-08-15",
        "kaynak": "Salih Katman-1 08-15 (7d349b5)"
      },
      "emekli": [
        {
          "deger": "uyucam",
          "varyantlar": [
            "uyuyacağım",
            "uyuyacagim",
            "günü kapat",
            "bugünlük bu kadar",
            "end of day",
            "iyi geceler"
          ],
          "tarih": "2026-08-15",
          "gerekce": "zaman-kayması simetrisi: kapanış selamı gece işareti sanılıyor (Salih Katman-1 hükmü 08-15 seans-3 soru-cevap; açılıştaki günaydın emekliliğiyle aynı sınıf).",
          "replaced_by": "seans bitimi",
          "izinli_kaliplar": [
            "\"uyucam\" tetiği",
            "uyucam tetiği",
            "emekli",
            "aday"
          ],
          "kaldirma_en_erken": "vardiya+3"
        }
      ],
      "aday": [],
      "not": "\"kapat\", \"bitiriyorum\", \"vardiyayı kapat\" zaman işareti taşımaz — tetik olarak KALDI (Salih 08-15)."
    },
    {
      "anahtar_id": "skill:gunaydin-vardiya",
      "tur": "skill_adi",
      "guncel": {
        "deger": "seans-acilis",
        "gecerli_bas": "2026-08-15",
        "kaynak": "Salih Katman-1 08-15 seans-3 soru-cevap (rename çifti; staj-acilis simetrisi)"
      },
      "emekli": [
        {
          "deger": "gunaydin-vardiya",
          "varyantlar": [],
          "tarih": "2026-08-15",
          "gerekce": "skill adı emekli tetiği taşıyordu (tip-c kalıntı: ad eski anlamı canlı tutar).",
          "replaced_by": "seans-acilis",
          "izinli_kaliplar": [
            "gunaydin-vardiya v0\\.",
            "gunaydin-vardiya → seans-acilis",
            "gunaydin-vardiya→seans-acilis",
            "emekli",
            "rename"
          ],
          "kaldirma_en_erken": "vardiya+3"
        }
      ],
      "aday": [],
      "not": "anahtar_id ad-türevi doğdu (v1 doğum hatası — \"anahtar akıllı olmamalı\" dersinin kendi üstümüzdeki örneği); id KALICI tutuldu, yalnız DEĞER değişti. Rename cascade: klasör (git mv, Salih eliyle — pretool teli) + name: + description + evals + çapraz-referanslar + bulut-kopya borcu."
    },
    {
      "anahtar_id": "skill:vardiya-kapanis",
      "tur": "skill_adi",
      "guncel": {
        "deger": "seans-kapanis",
        "gecerli_bas": "2026-08-15",
        "kaynak": "Salih Katman-1 08-15 seans-3 soru-cevap (rename çifti)"
      },
      "emekli": [
        {
          "deger": "vardiya-kapanis",
          "varyantlar": [],
          "tarih": "2026-08-15",
          "gerekce": "açılış skill'iyle ad simetrisi (Salih hükmü: ikisi birden).",
          "replaced_by": "seans-kapanis",
          "izinli_kaliplar": [
            "vardiya-kapanis v0\\.",
            "vardiya-kapanis → seans-kapanis",
            "vardiya-kapanis→seans-kapanis",
            "emekli",
            "rename"
          ],
          "kaldirma_en_erken": "vardiya+3"
        }
      ],
      "aday": [],
      "not": "id KALICI (ad-türevi doğum notu skill:gunaydin-vardiya kaydında)."
    },
    {
      "anahtar_id": "ana-sira-yuzeyi",
      "tur": "yuzey",
      "guncel": {
        "deger": "Claude Code ana-sıra (terminal ∨ masaüstü uygulaması)",
        "gecerli_bas": "2026-08-17",
        "kaynak": "Salih Katman-1 08-12; m.41 geçiş kaydı 08-14 · GK-2 08-17 (KB-34): masaüstü uygulaması Claude Code = ana-sıra (parmak izi doğrulandı); Cowork SEKMESİ koşullu (yuzey-parmak-izi.py PASS'la) — 'Cowork' emekli değeri o kapıda yeniden değerlendirilir; model şartı 'en güçlü model'"
      },
      "emekli": [
        {
          "deger": "Cowork",
          "varyantlar": [
            "cowork ana-sıra",
            "ana-sıra(cowork)",
            "cowork'ün",
            "cowork oturumu"
          ],
          "tarih": "2026-08-12",
          "gerekce": "Cowork emekli (kapsül 08-15); ana-sıra terminal",
          "replaced_by": "Claude Code ana-sıra (terminal ∨ masaüstü uygulaması)",
          "izinli_kaliplar": [
            "cowork emekli",
            "cowork-sonrası",
            "cowork homebase",
            "pc cowork",
            "mac cowork",
            "cowork,",
            "cowork\\)",
            "cowork\\s+\\d\\d-\\d\\d",
            "\\(cowork",
            "cowork/",
            "/cowork",
            "cowork ve ",
            "chat-kapsulu",
            "imzasi \\d{4}-\\d{2}-\\d{2}, cowork",
            "cowork gunaydin vardiyasi",
            "cowork sekmesi",
            "cowork modu",
            "cowork\\) a\\u00e7\\u0131lan",
            "cowork-dönemi",
            "cowork dönemi",
            "cowork-donemi"
          ],
          "kaldirma_en_erken": "vardiya+3"
        }
      ],
      "aday": [],
      "not": "İkinci koşum vakası (SH-10 sonrası ayrı tur): CLAUDE.md açıklama notu ve m.41 metni hâlâ Cowork'ü ana-sıra sayan cümleler taşıyor; tarihçe damgaları izinli. 08-16 (Jarvis/Fable, Salih \"düzelt\"): sıcak-katman kalıntısı KAPANDI — CLAUDE.md \"Yüzey yetkisi\" satırı + SessionStart hook yetki bandı geçiş kaydına yeniden yazıldı; denetim körü: `ana-sıra(Cowork)` kalıbı `\\(cowork` izinli-kalıbına takılıyordu (kalıp gevşetilmedi, kalıntı elle bulundu). | 08-17 GK-2: güncel değer 'terminal ana-sıra' → 'Claude Code ana-sıra (terminal ∨ masaüstü)'; 'terminal ana-sıra' ifadesi eş-anlamlı kalır (emekli değil). Cowork sekmesi için koşullu geri-dönüş kapısı açık (KB-34)."
    },
    {
      "anahtar_id": "calisma-modeli",
      "tur": "kavram",
      "guncel": {
        "deger": "çalışma modeli",
        "gecerli_bas": "2026-08-17",
        "kaynak": "Salih Katman-1 08-17 ~09:20 ('şirket metaforundan vazgeçelim') + halef sözlük ONAYI 08-17 ~10:15 ('halef sözlüğü onaylıyorum, cascade'i koş') · açıklama: (= Jarvis = sistem, metaforsuz; m.15 özü: CV projeleri Jarvis içinde geliştirilir, CV çıktıdır)"
      },
      "emekli": [
        {
          "deger": "şirket simülasyonu",
          "varyantlar": [
            "şirket-simülasyonu",
            "şirket simulasyonu",
            "sirket simulasyonu",
            "şirket-simulasyonu"
          ],
          "tarih": "2026-08-17",
          "gerekce": "Salih 08-17: 'jarvisin şirket ceo'su olması metaforuyla gerçekten çalıştığım bir şirket olması bağlam anlaşılmasında sorun çıkarıyor, tekilleştirmemiz lazım, şirket metaforundan vazgeçelim.'",
          "replaced_by": "çalışma modeli",
          "izinli_kaliplar": [
            "emekli",
            "metafor",
            "eski ad",
            "eski adı",
            "cascade",
            "anahtar_terim",
            "süpersede",
            "supersede",
            "staj",
            "otonet",
            "otoplus",
            "gerçek işyeri",
            "karar [3-7]\\b",
            "jarvis ile şirket simülasyonunda",
            "ben patronum",
            "sen şirket metaforundaki",
            "jarvisin şirket ceo'su",
            "şirket metaforundan vazgeçelim",
            "işbirlikçim de değilsin"
          ],
          "kaldirma_en_erken": "seans+3"
        }
      ],
      "aday": [],
      "not": "Metafor emekliliği paketi (5 anahtar: calisma-modeli · sirket-referansi · carvis-rol-adi · salih-rol-adi · oturum-birimi); tekil replaced_by kuralı için bölündü. Baseline (aday sayımı 08-17 sabah, tek anahtarda): sıcak 69 / ılık 165 / soğuk 783. 'işçi/lider' emekli DEĞİL — '-ajan' ekiyle kalır. | CASCADE 08-17 ~10:30 KOŞTU: sıcak → 0 (31 dosya: tüzük başlık+m.2/15/16/25/28/30/33/35/36/44/45, pano, kapsül, ingest/veri/world-model, şablon seans-teslim.md yeni + vardiya-teslim.md güdük, 15 SKILL.md + 6 evals.json); ılık EYLEM eşiği aşıldı → bakım kartı K-024 (KILAVUZ, wiki/sozluk, fikir-kutusu, kuyruk defterleri, veri/README, 00/01 plan dosyaları); soğuk tarihçe."
    },
    {
      "anahtar_id": "sirket-referansi",
      "tur": "kavram",
      "guncel": {
        "deger": "Jarvis (sistem)",
        "gecerli_bas": "2026-08-17",
        "kaynak": "Salih Katman-1 08-17 ~09:20 ('şirket metaforundan vazgeçelim') + halef sözlük ONAYI 08-17 ~10:15 ('halef sözlüğü onaylıyorum, cascade'i koş')"
      },
      "emekli": [
        {
          "deger": "şirket",
          "varyantlar": [
            "sirket",
            "şirketin",
            "şirketi",
            "şirkete",
            "şirketler",
            "şirketteki",
            "şirketimiz",
            "şirket-içi",
            "şirket içi"
          ],
          "tarih": "2026-08-17",
          "gerekce": "'şirket' sözcüğü Jarvis'i değil Salih'in gerçek işyerini anlatır (tekilleştirme). Jarvis = sistem.",
          "replaced_by": "Jarvis (sistem)",
          "izinli_kaliplar": [
            "emekli",
            "metafor",
            "eski ad",
            "eski adı",
            "cascade",
            "anahtar_terim",
            "süpersede",
            "supersede",
            "staj",
            "otonet",
            "otoplus",
            "gerçek işyeri",
            "karar [3-7]\\b",
            "jarvis ile şirket simülasyonunda",
            "ben patronum",
            "sen şirket metaforundaki",
            "jarvisin şirket ceo'su",
            "şirket metaforundan vazgeçelim",
            "işbirlikçim de değilsin",
            "şirket simülasyonu",
            "şirket-simülasyonu",
            "sirket simulasyonu",
            "şirket metaforu",
            "gerçek şirket",
            "gercek sirket",
            "işyeri",
            "isyeri",
            "şirket büyürken",
            "şirkete özel",
            "şirketin kalbiyim"
          ],
          "kaldirma_en_erken": "seans+3"
        }
      ],
      "aday": [],
      "not": "Tüzük başlığı 'Şirket Tüzüğü v0' → 'Jarvis Tüzüğü v0' (eski ad parantezde). Salih'in tırnaklı sözleri özgül kalıplarla izinli (genel tırnak kalıbı YOK — tetik cümlelerini gizlerdi). | CASCADE 08-17 ~10:30 KOŞTU: sıcak → 0 (31 dosya: tüzük başlık+m.2/15/16/25/28/30/33/35/36/44/45, pano, kapsül, ingest/veri/world-model, şablon seans-teslim.md yeni + vardiya-teslim.md güdük, 15 SKILL.md + 6 evals.json); ılık EYLEM eşiği aşıldı → bakım kartı K-024 (KILAVUZ, wiki/sozluk, fikir-kutusu, kuyruk defterleri, veri/README, 00/01 plan dosyaları); soğuk tarihçe. | K-024 ılık cascade 08-17 ~10:45 (Salih seçimi B: kayıtlar da yeni sözlüğe; tırnak içi Salih sözleri + 'şirkete özel' (gerçek işyeri anlamı) + tarihsel alıntılar izinli): ılık → 0."
    },
    {
      "anahtar_id": "carvis-rol-adi",
      "tur": "kavram",
      "guncel": {
        "deger": "köle",
        "gecerli_bas": "2026-08-17",
        "kaynak": "Salih Katman-1 08-17 ~09:50: 'sen şirket metaforundaki CEO değilsin artık, işbirlikçim de değilsin, sen benim kölemsin' + halef onayı 08-17 · açıklama: (Salih'in kölesi — ilişki adı; işlev adı üst-orkestratör m.44 kalır)"
      },
      "emekli": [
        {
          "deger": "CEO",
          "varyantlar": [
            "ceo'su",
            "ceo'dur"
          ],
          "tarih": "2026-08-17",
          "gerekce": "Rol adı değişti (ilişki: köle; işlev: üst-orkestratör). CEO katmanı m.44'ten düşer.",
          "replaced_by": "köle",
          "izinli_kaliplar": [
            "emekli",
            "metafor",
            "eski ad",
            "eski adı",
            "cascade",
            "anahtar_terim",
            "süpersede",
            "supersede",
            "staj",
            "otonet",
            "otoplus",
            "gerçek işyeri",
            "karar [3-7]\\b",
            "jarvis ile şirket simülasyonunda",
            "ben patronum",
            "sen şirket metaforundaki",
            "jarvisin şirket ceo'su",
            "şirket metaforundan vazgeçelim",
            "işbirlikçim de değilsin",
            "ceo değil",
            "ceo degil",
            "hem ceo hem şef",
            "ceo \\+ üst-orkestratör"
          ],
          "kaldirma_en_erken": "seans+3"
        }
      ],
      "aday": [],
      "not": "'işbirlikçi' de rol adı olarak emekli (Salih beyanı) ama sözcük başka anlamlarda geçebildiği için varyant listesine alınmadı; elle denetim. | CASCADE 08-17 ~10:30 KOŞTU: sıcak → 0 (31 dosya: tüzük başlık+m.2/15/16/25/28/30/33/35/36/44/45, pano, kapsül, ingest/veri/world-model, şablon seans-teslim.md yeni + vardiya-teslim.md güdük, 15 SKILL.md + 6 evals.json); ılık EYLEM eşiği aşıldı → bakım kartı K-024 (KILAVUZ, wiki/sozluk, fikir-kutusu, kuyruk defterleri, veri/README, 00/01 plan dosyaları); soğuk tarihçe. | K-024 ılık cascade 08-17 ~10:45 (Salih seçimi B: kayıtlar da yeni sözlüğe; tırnak içi Salih sözleri + 'şirkete özel' (gerçek işyeri anlamı) + tarihsel alıntılar izinli): ılık → 0."
    },
    {
      "anahtar_id": "salih-rol-adi",
      "tur": "kavram",
      "guncel": {
        "deger": "tek karar verici",
        "gecerli_bas": "2026-08-17",
        "kaynak": "Salih Katman-1 08-17 (metafor emekli) + halef onayı 08-17; ilk kural 08-16 'ben patronum' ÖZÜ korunur, sözcük düşer · açıklama: (m.1; ilk kural özü: durdurma hakkı + Salih'in anlaması)"
      },
      "emekli": [
        {
          "deger": "patron",
          "varyantlar": [
            "patronun",
            "patronluk",
            "patrondur",
            "patronum",
            "patrona",
            "patronu",
            "patron-yüzü",
            "patron-yuzu",
            "patron-için",
            "patron-icin",
            "patron için"
          ],
          "tarih": "2026-08-17",
          "gerekce": "Şirket metaforunun Salih tarafı; halef 'tek karar verici'.",
          "replaced_by": "tek karar verici",
          "izinli_kaliplar": [
            "emekli",
            "metafor",
            "eski ad",
            "eski adı",
            "cascade",
            "anahtar_terim",
            "süpersede",
            "supersede",
            "staj",
            "otonet",
            "otoplus",
            "gerçek işyeri",
            "karar [3-7]\\b",
            "jarvis ile şirket simülasyonunda",
            "ben patronum",
            "sen şirket metaforundaki",
            "jarvisin şirket ceo'su",
            "şirket metaforundan vazgeçelim",
            "işbirlikçim de değilsin",
            "patron-icin-teslim",
            "ilk ve ilk kural",
            "patron oluyorum"
          ],
          "kaldirma_en_erken": "seans+3"
        }
      ],
      "aday": [],
      "not": "'ben patronum' Salih beyanı (08-16) özgül kalıpla izinli; ilk kural metni CLAUDE.md §0'da metaforsuz. | CASCADE 08-17 ~10:30 KOŞTU: sıcak → 0 (31 dosya: tüzük başlık+m.2/15/16/25/28/30/33/35/36/44/45, pano, kapsül, ingest/veri/world-model, şablon seans-teslim.md yeni + vardiya-teslim.md güdük, 15 SKILL.md + 6 evals.json); ılık EYLEM eşiği aşıldı → bakım kartı K-024 (KILAVUZ, wiki/sozluk, fikir-kutusu, kuyruk defterleri, veri/README, 00/01 plan dosyaları); soğuk tarihçe. | K-024 ılık cascade 08-17 ~10:45 (Salih seçimi B: kayıtlar da yeni sözlüğe; tırnak içi Salih sözleri + 'şirkete özel' (gerçek işyeri anlamı) + tarihsel alıntılar izinli): ılık → 0."
    },
    {
      "anahtar_id": "oturum-birimi",
      "tur": "kavram",
      "guncel": {
        "deger": "seans",
        "gecerli_bas": "2026-08-17",
        "kaynak": "Salih Katman-1 08-17 halef onayı (08-15 'seans başı/bitimi' tetikleriyle aynı yön)"
      },
      "emekli": [
        {
          "deger": "vardiya",
          "varyantlar": [
            "vardiyası",
            "vardiyasi",
            "vardiyayı",
            "vardiyayi",
            "vardiyada",
            "vardiyanın",
            "vardiyanin",
            "vardiyalar",
            "vardiyaları",
            "vardiyalari",
            "vardiyalarıdır",
            "vardiyasında",
            "vardiyasinda"
          ],
          "tarih": "2026-08-17",
          "gerekce": "İş-vardiyası = şirket sözlüğü; oturum birimi 'seans' (tetikler 08-15'te zaten seans). Yeni teslim dosyaları seans-teslim-YYYY-MM-DD-*.md; şablon core/sablonlar/seans-teslim.md (eski dosya pointer-güdük).",
          "replaced_by": "seans",
          "izinli_kaliplar": [
            "emekli",
            "metafor",
            "eski ad",
            "eski adı",
            "cascade",
            "anahtar_terim",
            "süpersede",
            "supersede",
            "staj",
            "otonet",
            "otoplus",
            "gerçek işyeri",
            "karar [3-7]\\b",
            "jarvis ile şirket simülasyonunda",
            "ben patronum",
            "sen şirket metaforundaki",
            "jarvisin şirket ceo'su",
            "şirket metaforundan vazgeçelim",
            "işbirlikçim de değilsin",
            "vardiya-teslim-\\d",
            "gunaydin-vardiya",
            "vardiya-kapanis",
            "günaydın vardiyası",
            "gunaydin vardiyasi",
            "paralel-vardiya",
            "vardiya\\+3",
            "vardiya→seans",
            "vardiya->seans"
          ],
          "kaldirma_en_erken": "seans+3"
        }
      ],
      "aday": [],
      "not": "Tarihli teslim dosyaları (raporlar/vardiya/vardiya-teslim-2026-…) soğuk tarihçe, yeniden adlandırılmaz. Tüzük imza damgaları ('günaydın vardiyası') izinli. | CASCADE 08-17 ~10:30 KOŞTU: sıcak → 0 (31 dosya: tüzük başlık+m.2/15/16/25/28/30/33/35/36/44/45, pano, kapsül, ingest/veri/world-model, şablon seans-teslim.md yeni + vardiya-teslim.md güdük, 15 SKILL.md + 6 evals.json); ılık EYLEM eşiği aşıldı → bakım kartı K-024 (KILAVUZ, wiki/sozluk, fikir-kutusu, kuyruk defterleri, veri/README, 00/01 plan dosyaları); soğuk tarihçe."
    },
    {
      "anahtar_id": "ajan-adi",
      "tur": "kavram",
      "guncel": {
        "deger": "Jarvis",
        "gecerli_bas": "2026-09-10",
        "kaynak": "Salih Katman-1 09-10 Karar 93 + EK (ad-eşitliği üç katman, tools/ad-esitligi-denetim.py); kayda giriş 09-15 İB-90 canlı koşumu (emekli-anahtar-cascade kaydet)"
      },
      "emekli": [
        {
          "deger": "Carvis",
          "varyantlar": ["CARVİS", "CARVIS", "carvis"],
          "tarih": "2026-09-10",
          "gerekce": "Karar 93 (Salih 09-10): konuşan ajan JARVİS; Carvis 08-17→09-10 dönemi adı, tarihli kayıtlarda AS-OF. Ad-eşitliği (Carvis = Jarvis) her bağlam kombinasyonunda bilinir (Karar 93 EK) — bu anahtarda README bağlama ZORUNLU.",
          "replaced_by": "Jarvis",
          "izinli_kaliplar": ["emekli", "eski ad", "eski adı", "cascade", "anahtar_terim", "süpersede", "supersede", "→ jarvis", "= jarvis", "carvis\\)", "ad-esitligi", "ad-eşitliği", "karar 93", "carvis emekli", "carvis = jarvis", "carvis → jarvis", "carvis -> jarvis", "gunaydin carvis", "günaydın carvis"],
          "kaldirma_en_erken": "seans+3"
        }
      ],
      "aday": [],
      "not": "Denetim asıl aracı tools/ad-esitligi-denetim.py (K1 yüklenen katman · K2 dizin README · K3 canlı sızıntı); bu kayıt anahtar-denetim/cascade ile aynı sayım düzlemine alır."
    }
  ]
}
```

## 3. Emeklilik protokolü (her ad/tetik/kural değişiminde — zorunlu adımlar, sıra backward)
> **Kod (Karar 114, 2026-10-16):** adım sırası, `KISMİ` damgası (sıcak ihlal ≠ 0), ılık merdiven k1=1 / k2=10, bütünlük sıfırları, denetim çıkış kodu ve 3 vardiya kaldırma kuralı `lean/Kanon/AnahtarEmeklilik.lean`'de kanoniktir; §3-§4 metni uygulama tarifi ve gerekçe.
1. **Kayıt:** §2'ye `emekli` satırı (tarih + gerekçe + tekil `replaced_by` + izinli kalıplar) — Katman-1 sınıfı değişim Salih emri/imzasıyla; Katman-2 Jarvis yazar, commit'ler, veto = revert.
2. **Denetim-önce:** `python3 tools/anahtar-denetim.py` → sıcak/ılık/soğuk kırılımlı kalıntı-referans listesi (baseline sayısı kaydedilir).
3. **Yayılım (sıcak katman → 0):** CLAUDE.md · core/* · `.claude/skills/*/SKILL.md` (description **önce**) · pano · kapsül: her kalıntı ya yeni değere yeniden yazılır ya izinli tarihçe-kalıbına girer (imza damgası) — silme yok; kaldırılan cümle gerekiyorsa `kuyruk/arsiv-*` pointer'ıyla iner (m.8/m.20). Ilık katman (kuyruk/wiki/kutu/pipeline): uyarı → aynı vardiyada ya da bakım kartı. Soğuk katman (raporlar/cc rapor-emir/ogrenme/arşiv): **tarihçe** — sayılır, yeniden yazılmaz.
4. **Tetik-eval:** tetik anahtarlarında should/should-not-fire seti güncellenir (eski değer **negatif** örnek olur; skill `evals/evals.json`) — kalıntı-bağın davranışsal ölçümü literatürde yok, kendimiz ölçeriz [B kör-nokta].
5. **Denetim-sonra + commit:** script sıcak ihlal = 0 → `[icra]` commit ("retire <anahtar>: <eski>→<yeni>, cascade N dosya"); ≠0 → emeklilik **tamamlanmadı** (**restrict**), commit'e "`KISMİ`" damgası ve bakım kartı.
6. **Kaldırma (opsiyonel, ≥3 vardiya sonra):** emekli satırı `core/`den `kuyruk/arsiv-anahtar-kaydi.md`'ye iner, kayıtta tek satır pointer kalır.

## 4. Metrikler ve eşik merdiveni (sayım metrikleri — Heinrich R1-R5 uyumlu [C-YT4]; sabitler deneysel m.29, ≥10 koşumda kalibre)
| Metrik | Tanım | Kaynak | Eşik (deneysel) |
|---|---|---|---|
| kalıntı-referans (sıcak) | emekli değerin sıcak katmanda izinli-kalıp **dışı** geçiş sayısı | anahtar-denetim | **0** (sıfır tolerans; ≠0 → **fail-loud**, kanon commit'i `KISMİ`) [A-YT8 dbt `!=0`] |
| kalıntı-referans (ılık) | aynı, ılık katman | anahtar-denetim | k1=1 **uyarı** (kart) · k2=10 **eylem** (aynı vardiya cascade) [C-YT6 merdiven] |
| kalıntı-referans (soğuk) | aynı, soğuk katman — tarihçe | anahtar-denetim | eşiksiz; trend izlenir |
| halefsiz-emekli | `replaced_by` boş/çoklu/çevrimli emekli satırı | anahtar-denetim (kayıt bütünlüğü) | 0 |
| damgasız kayıt | `tarih`/`gecerli_bas` boş | anahtar-denetim | 0 (kabul edilmez) [B-YT2] |
| tekillik tip-b | farklı anahtar aynı kavram (aynı `guncel.deger` iki anahtarda) | anahtar-denetim | 0 |
| yetim referans | repo'da olmayan dosya-pointer'ı | `veri/baglam.sqlite` `v_kirik_pointer` (yol biçimli) | uyarı; sıcak katmanda 0 |
| tetik-eval geçme | should-not-fire (eski tetik) + should-fire (yeni) | skill evals | %100 (n küçük; sayı yanına n yazılır) |
| hakemlik oranı | ingest'te yeni kayıtla birlikte getirilen **eski** kaydın hükme bağlanma oranı | damıtma sayaçları (GEÇERSİZ-KIL/UPDATE) | hedef: eski kayıt hükümsüz kalmaz [B-YT4] |
Yaş/decay/TTL skorları kanon-kuralı sınıfında **girmez** (sabit raf ömrü yok — R3/R5 ihlali) [C-YT4/C4-2]; yalnız dış-URL sınıfı için deneysel (içerik-kayması %13-76: link-açılıyor-mu yetmez, kayıt-anı özü gerekir [C-YT3]).

## 5. Koşum ve bağlar
- **`tools/anahtar-denetim.py`** (stdlib): §2 JSON'u okur → git-izlenen md dosyalarını tarar (katman kuralı `tools/baglam-tablo.py` ile aynı) → anahtar × katman × ihlal/izinli tablosu + kayıt-bütünlüğü kontrolleri; çıkış 0 temiz · 1 sıcak ihlal ∨ bütünlük hatası · 2 kullanım. `--json` makine çıktısı; `--anahtar <id>` süzme; `--goster N` ilk N ihlal satırı.
- **Ne zaman:** vardiya-kapanış ritüeli (kapanış listesine kanca) · damıtma turu (**geçersiz-kıl** yayılım adımı) · her ad/tetik/kural değişimi (§3) · skill-kapisi K2 topraklama (referans-varlığı ile aynı sınıf).
- **İngest şeması v2 bağı:** **geçersiz-kıl** artık yalnız `gecerli-bitis` damgası **değil** — anahtar sınıfı çelişkide §3 yayılımı tetikler (fıkra `core/ingest-semasi.md` §3'e eklendi).
- **Veri altyapısı:** `veri/baglam.sqlite` `anahtar` tablosu `durum/replaced_by/gecerli_*` alanlarını bu kayıttan alır (İ-3, `tools/baglam-tablo.py --anahtar-kaydi`); referans sayımları `v_referans_sayim`.
- **Sınırlar (Hat-4 ile ayrım):** bu kayıt **sıkıştırma** yapmaz; tekilleştirme/geçersiz-kılma/kayma içindir. Halüsinasyon paketi (Hat-3) çıktı-doğrulama; burası hafıza-bütünlüğü.

## 6. Girmez + kör noktalar (şema tasarımcısı bilsin)
- **girmez**: parametrik düzenleme/unlearning bulguları (ağırlık düzeyi) [B-YT8] · olasılıksal varlık-çözümleme (Fellegi-Sunter/Ditto — 10⁵+ ölçek) [A kör] · istatistiksel drift detektörleri + gömme-tabanlı kayma ölçümü (n≈20-40'ta saptanabilir kayma ölçeğin %75+) [C-YT8] · "silver garantisi" otoriteye dayandırma (normatif silver tanımı yok; sözleşmeyi Jarvis yazar) [A1-2].
- **kör noktalar** (deneysel damga zorunlu): "X artık geçerli değil" cümlesi **eklemek** ↔ metni **kaldırmak** A/B ölçümü `YOK` · bayat-kayıt oranı ↔ doğruluk eğrisi yok (yalnız yön) · markdown/[[link]] kanonunda cascade etkisi ölçülmemiş · emekli tetik-kelimenin davranışsal kalıntısı ölçülmemiş (tetik-eval seti bizde) · Obsidian `aliases`/skill-registry tetik-emekliliği emsali aranmadı · WebFetch PDF-özetleyicisi 2 kez uydurma rakam üretti → doğrulama arXiv ID birebir + PDF-özet güvenilmez (K2 kuralına girdi).
- **m.16 taraması:** m.8 ✓ (silme yok, damga+arşiv) · V24 ✓ (anahtar-kararlılığı) · ingest v2 → **update** (yayılım fıkrası) · damitma → adım eklendi · gunaydin-vardiya/vardiya-kapanis skill'leri → SH-10 (tetik listesi + description) · Hat-4 → sınır çizildi · Anthropic skill best-practice ✓ (tek terim, description tetik yüzeyi). Çelişki yok; kapsam-genişletme: skill adı rename Katman-1 (Salih).

## 7. Bedel defteri + ölçüm planı
Bedel: her ad değişimi ≈ 1 script koşumu (5 sn) + sıcak katman düzenlemeleri (ilk koşum: 6 dosya) + tetik-eval; risk: aşırı-yeniden-yazım (repair-only ilkesi frenler) · tarihçe damgalarını yanlışlıkla yeniden yazma (izinli kalıplar frenler). Ölçüm: ilk 10 emeklilik koşumunda (kalıntı-önce/sonra · dosya sayısı · süre · yanlış-pozitif izinli-kalıp sayısı) → k1/k2 ve "vardiya+3" kalibrasyonu; tetik-eval sonuçları skill evals'e.
