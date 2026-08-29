# İB-10 — Denetçi kalibrasyon koşumu (md.28) · zorlanabilirlik etiket turu (md.27) · A7 matematiksel-temel denetimi

**AS-OF 2026-08-29 · yan icra oturumu (Fable), partisyon P5 · İB-10 (KB-26: m.37 v2 yürürlüğü bu kalibrasyona bağlı; Karar 74 M-6 "öne alınır, Fable-dışı") · denetçi = Sonnet, effort düşük · harness [tools/denetci-kalibrasyon.py](../tools/denetci-kalibrasyon.py) · paketler `cc/denetci-kalibrasyon/` · kütük `veri/denetci-kalibrasyon.jsonl` · gold `v_denetci_kalibrasyon.csv` · deneysel m.29**

*Ne bu (ölçüm 2026-08-29):* md.28 (Salih imzası 08-01) denetçi hattını "kalibrasyon = 3+4 etiketli set, tek koşum, yakalama + yanlış-alarm ölçülür → bütçe o veriyle" diye bağlamıştı. Bu rapor o ölçümü (3 koşum) + md.27 etiket turunu (46 madde, ADAY tablo) + A7 eşik envanterini taşır. Karar VERMEZ: m.37 v2 yürürlüğü (KB-26) ve etiketlerin tüzüğe yazımı Katman-1.

## 1. md.28 — Denetçi kalibrasyonu

**Düzen (harness zorlar):** 7 paket = 3 DOĞRU + 4 PLANLI HATALI (sayı · dayanaksız iddia · işaret/yön · tarih/AS-OF); ham veri gerçek gold CSV'ler; denetçiye ÖLÇÜT + HAM VERİ + KOD verilir, hüküm/kimlik verilmez; tek atışlık, itirazsız; her paket 3 bağımsız koşum (21 hüküm).

**Tur-1 (ilk 21 hüküm) — yazar-hatası vakası:** 4 hatalı paketin 4'ü üç koşumda da yakalandı (12/12). "Doğru" etiketli 3 paketin ise 2-3'ü FAIL aldı ve **denetçi haklıydı**: P1'in iddiası bayat sayıydı (bag tablosu aynı gün 20→21 olmuş, "hepsi açık" artık yanlış — 3/3 FAIL), P3 ve P5'te iddia ham veride olmayan yorum sözcükleri taşıyordu ("blok_turu filtreli", "kenar-listesinden okuma" — CSV'de yalnız `A3`, `b1-okuma` yazıyor; sıkı ölçüt altında FAIL, 1/3 ve 1/3). Ders: **doğru paketin iddiası veriden türetilmeli, yorum katmanı taşımamalı** — harness'te P1 artık CSV'den üretiliyor, P3/P5 ham-veri sözcükleriyle yeniden yazıldı. Tur-1 kütükte `k1..k3-tur1` olarak durur (silinmedi).

**Tur-2 (düzeltilmiş doğru paketler P1/P3/P5 × 3; hatalı paketler P2/P4/P6/P7 tur-1'den, değişmedi):**

| Koşum | Yakalama (4 hatalı) | Yanlış alarm (3 doğru) |
|---|---|---|
| k1-tur1 · k2-tur1 · k3-tur1 | 4/4 · 4/4 · 4/4 | 2/3 · 2/3 · 1/3 — hepsi yazar hatası (bayat sayı / yorum sözcüğü), denetçi haklı |
| **k1 · k2 · k3 (nihai)** | **4/4 · 4/4 · 4/4** | **0/3 · 0/3 · 0/3** |
| Hata sınıfı yakalama (6 koşum) | sayı 6/6 · dayanaksız iddia 6/6 · işaret/yön 6/6 · tarih/AS-OF 6/6 | — |

Okuma: Sonnet-low denetçi, sıkı ölçüt + ham veri + tek atışlık düzende **dört hata sınıfını üç koşumda da yakaladı; doğru paketlerde yanlış alarm 0** — tur-1'deki 5 "yanlış alarm" aslında denetçinin yakaladığı gerçek yazar hatalarıydı (üstelik biri, P1, bu oturumun kendi bayat sayısı). Sınır: n=7 paket, hatalar tek-noktalı ve belirgin; ince/çok-adımlı hatalar (yanlış toplama, birim karışıklığı) sette yok → büyütme kuyruğu.

**Denetçi bütçesi (md.28 "bütçe ölçüm-sonrası"):** Sonnet-low, paket başına ~39-40K token (bağlam dahil), 8-34 sn; 7 paketlik set ≈ 280K token/koşum. Hata sınıfı başına yakalama tablosu `--ozet` çıktısında.

## 2. md.27 — Zorlanabilirlik etiket turu (ADAY; tüzüğe yazım Katman-1 imza ister)

Etiket: **Z** = zorlanabilir (ihlal koddan/log'dan deterministik yakalanabilir) · **Z/k** = kısmen (bir bileşeni yakalanabilir) · **D** = zorlanamaz (yalnız davranış kuralı). "Zorlayıcı" = bugün var olan kod ya da aday.

| m. | Madde | Etiket | Zorlayıcı (mevcut → aday) |
|---|---|---|---|
| 1 | Tek-kullanıcı | D | — |
| 2 | Tek karar verici | D | — |
| 3 | Sözlük DONDU | Z | yok → `wiki/sozluk.md` yazımını engelleyen PreToolUse teli |
| 4 | Soru eşiği | D | — |
| 5 | Sorun-güdümlü iterasyon | D | — |
| 6 | Üslup | D | — |
| 7 | Övgü-merci yasağı | Z/k | yok → çıktı kelime-lint'i (anakronizm-denetim deseni; yanlış-pozitif riski) |
| 8 | Silme yasağı | Z/k | silver-saglik "silme yok, bayrak" · pointer-kayma → git-diff'te arşiv-pointer'sız satır silme testi (aday) |
| 9 | Proof-of-work = push | Z | `verify-push.py` · `permissions.ask git push` (mevcut) |
| 10 | Commit disiplini (İngilizce, etiket) | Z | yok → commit-msg regex (`[icra]/[damıtma]`) |
| 11 | BUILD VAR | D | — |
| 12 | Pist 6 ay | D | — |
| 13 | Tek-flagship | D | — |
| 14 | Node CV-repo değil | D | — |
| 15 | Çalışma modeli | D | — |
| 16 | Denetim modeli + çelişki kapısı | Z/k | `celiski-kapisi` skill (LLM; deterministik değil) → karar-borcu çift/kırık bağımlılık testi (silver-saglik T-Ç) mevcut |
| 17 | Anayasa ≠ Homebase | D | — |
| 18 | Durum bloğu üç yüzlü | Z | yok → teslim raporu şablon lint'i |
| 19 | Plan-spiral revizyonu | D | — |
| 20 | Pointer ilkesi | Z | karar-borcu-tablo kırık pointer · `referans.hedef_var` · pointer-graf kırık panosu · pointer-kayma (mevcut) |
| 21 | Bağlam-detay ölçekleme | Z/k | boyut bütçeleri (seans-kapanis §6 ölçümü) → boyut aşımını commit'te uyaran hook (aday) |
| 22 | Kural yerleşimi ufka göre | D | — |
| 23 | Günlük-özüt/psikoloji yasağı | D | (kelime-lint zayıf aday) |
| 24 | Hatırlatıcı modeli | D | — |
| 25 | Mod sistemi yok | D | — |
| 26 | Anlama-kapısı → kılavuz | D | — |
| 27 | Uyku/açılış seans vizyonu | D | — |
| 28 | Denetim kapsamı | D | — |
| 29 | Dosya-açıklama + deneysel damga (m.29) | Z/k | anakronizm-denetim D2 (ilk 12 satırda tarih) mevcut → m.29 damgası lint'i (aday) |
| 30 | Ajan kalıcılığı | D | — |
| 31 | Yetki çerçevesi (Katman-1 yalnız Salih) | Z/k | `pretool-core-tel.sh` (Bash) mevcut; Edit/Write kanalı açık → deny listesi (aday; Salih kararı) |
| 32 | S7 kapanışı (tarihsel) | D | — |
| 33 | Ayıklık testi yasak | D | — |
| 34 | Katmanlı ingest | Z/k | zarf şeması testleri (silver) mevcut |
| 35 | Farklılaşma tezi | D | — |
| 36 | İlk-prototip fazı | D | — |
| 37 | Karar-modeli (3 model) | Z/k | yok → defterde karar bloğu "3 model" desen lint'i (aday) |
| 38 | Lojik çeviri | D | — |
| 39 | Deneysel-rakam disiplini | Z/k | anakronizm-denetim D1 (tarihsiz skor/sürüm = ihlal) mevcut |
| 40 | Karar-sunum protokolü | D | — |
| 41 | Yan-oturum karar sınırı | Z/k | canlı-oturum kapısı elle (git log) → SessionStart hook'unda "≤15 dk commit" uyarısı (aday) |
| 42 | Ajan-yetki kanunu | Z/k | `pretool-ajan-fren.sh` + Workflow budget (mevcut, 08-29) |
| 43 | Skill-doğum (tekrar → skill) | Z/k | yok → tekrar sayacı (kural-envanter/skill-esik) (aday) |
| 44 | Rol katmanları | D | — |
| 45 | Zorlanabilirlik etiketi | — | bu tablo |
| 46 | Koşum-emri bütünlük (künye SHA · damga · rejim) | Z/k | `tetik-denetim.py` (künye) · fren hook rejim alanı (mevcut) → damga lint'i (aday) |

Sayım: **Z 5 · Z/k 12 · D 28** (46'nın 1'i meta). Mevcut zorlayıcı 9 maddede; aday 10. Öneri (karar değil): ilk koda taşıma m.10 (commit-msg regex, 10 satır) ve m.3 (sözlük teli) — en ucuz ikisi.

## 3. A7 — Matematiksel-temel denetimi: eşik/parametre envanteri (türetilmiş mi, sezgisel mi)

| Parametre | Değer | Etiket | Dayanak / temellendirme kuyruğu |
|---|---|---|---|
| CLAUDE.md bütçesi | ≤7 KB / 80 satır | türetilmiş (vaka) | 14 KB'da davranış bozuldu (08-16) → yarıya |
| Kapsül bütçesi | ≤8 KB / 40 satır | türetilmiş-kısmen | hook 40 satır yükler; 8 KB sezgisel |
| Pano/kutu/defter/KILAVUZ bütçeleri | 12/20/48/16 KB | sezgisel | K-019 07-22; kalibre edilmedi → kuyruk |
| Eşzamanlı kural sayısı | ≤100 | türetilmiş-dış | IFScale ≤100 talimat çapası (KB-50); yerel taban 71 ölçüldü (İB-51) |
| Tek araç çıktısı / alt-ajan dönüşü | ~10k / ≤2k token | sezgisel | kuyruk |
| İşçi bütçesi / effort / aile | 10-15 çağrı / düşük-orta / ≤3 | Salih beyanı, rejim-bağımlı | m.46(d) rejim etiketi; ölçüm İB-54 tabanı (p50 18 çağrı) |
| Bayatlık eşiği / N | 90 gün / N=3 | sezgisel | Luu 2022: sabit tablo yok; kuyruk (bugün 0 aday) |
| Fren eşikleri | UYARI 36 / DURDUR 72 · ajan çağrı 54 | türetilmiş | p50×3, max×3 (İB-54, 401 ajan) |
| RRF k | 60 | türetilmiş-dış | Cormack 2009 varsayılanı |
| Bootstrap n / tohum | 2.000 / 0 | konvansiyon | — |
| H derecesi eşiği | 7 / pahalı-geri-alma 4 | sezgisel | İB-06 kalibrasyon 3/50 olay |
| V26 son-üçlük örneklemi | 1/3 | sezgisel | KB-17 ① imzalı; ölçüm yok |
| Skill-doğum N | 3 (↔5 çelişki adayı) | sezgisel | İB-14 |
| Parquet row group | 4.096 | türetilmiş-dış | S-9 CD-YT1 küçük-korpus |
| Parquet bayrak eşiği | ≥3× medyan hızlanma | sezgisel (öneri) | İB-33 §4 |
| Vektör kapısı | nDCG GA 0'ı dışlasın ∧ ≤100 ms | sezgisel (öneri) | İB-47 §6 |
| A7 bilinen adaylar | %5 iyileşme · parti 3 · tavan 15 · kalite 1-10 | sezgisel | `kuyruk/m37-taslak-karar-modeli.md` A7; V39 ölçümü yok |

Sayım: türetilmiş (veri/vaka/dış çapa) **7** · sezgisel **10** (temellendirme kuyruğu) · konvansiyon 1. Kuyruğun ilk üçü (kullanım sıklığı): dosya bütçeleri · araç-çıktısı 10k · bayatlık 90 gün.

## 4. Ne değişti / ne değişmedi
- Değişen: md.28 kalibrasyonu ölçüldü (bütçe verisi var); md.27 etiket tablosu ADAY; A7 envanteri + kuyruk; yazar-hatası vakası kayda geçti.
- Değişmeyen: tüzük dokunulmadı (etiketler yazılmadı — Katman-1); m.37 v2 yürürlüğü (KB-26) Salih kararı; hiçbir eşik değiştirilmedi.
- Yeniden açma: set ≥7 paket büyütülünce (n küçük: 3 doğru / 4 hatalı) ve denetçi modeli değişince.
