# Görev Emri — İB-75 + İB-64c birleşik: bağlam-devri ekip-lideri v0 (Opus 5 medium lider) — çift-atlas ön-koşul + tasarım paketi

*Derleyen: Carvis/Fable (ana-sıra), gorev-emri-derleme skill'i, 2026-09-09. Kaynak: Karar 89 (Fable → Opus 5 lider medium → Sonnet işçi; Karar 85 süpersede) · Karar 88 M8 (a) · ledger İB-75 + İB-64c · Karar 86 D2 Salih notu aynen ("fable bağlamı çok büyüdüğü noktada bağlamı sonnet işçilere devredecek şekilde ekip lideri tasarımına geçeceğiz … başta hafıza gelişimi ve yetkileri sınırlı olur ama bağlamı devredip azaltmak önemli") · tohum `kuyruk/ekip-lideri-ogrenme-desenleri.md` (20 satır, 10 desen). Rejim: kalite-öncelikli (Katman-1 tasarım girdisi). Koşum: ilk boş seansta `pipeline-kosum`; hüküm masa-10.*

## KİMLİK
gorev_adi:        baglam-devri-ekip-lideri-v0
rol:              lider (Opus 5, effort MEDIUM sabit — Karar 89; high YASAK) + işçi (Sonnet) + hakem (ayrı Opus medium çağrısı, maskeli)
cagri_kosulu:     Karar 89 sonrası ilk boş seans; Fable "İB-75 koşumu" tetiği; İB-64c koşulmadıysa bu emrin 1. aşaması olarak koşulur (birleşik)
rejim:            kalite-öncelikli
model:            lider Opus 5 (medium) · işçi Sonnet (low: envanter · medium: tez/antitez) · hakem Opus 5 (medium, maskeli, sentezden AYRI çağrı — Karar 86 D3-i)
kosum_profili:    Fable yazdı (KB-02; kendi koşumu için tahmin yok). Lider Opus medium: 1 çağrı, bağlam ≈40k, tahmini çıktı 6-10k token `[?]`. İşçi Sonnet: 6 ajan (tez A/B/C · antitez A/B · iç-envanter) × 10-15 araç çağrısı, işçi dönüşü ≤2k token, toplam ≈60-90k out `[?]`. Hakem Opus medium: 1 çağrı ≈8k `[?]`. Bant bronz `veri/bronz/tahmin-olay.jsonl`'e koşum öncesi düşer. Fren: ajan ≤36/wf, çağrı ≤54/ajan (m.46); N_hücre + sayaç ≤143.

## GİRDİLER
arastirma_sorusu:     "Fable ana-oturumunun bağlamı büyüdüğünde (ölçüm: 09-04 tepe 427.877 token, 172 tur 128k üstü — `v_baglam_seyri`) bağlamı bir lider-ajana (Opus 5 medium) ve işçilere (Sonnet) devreden ekip-lideri katmanı NASIL tasarlanır: devir birimi (ne devredilir: görev-case · manifest · karar-özeti · dosya-pointer) · devir anı (eşik: token ∨ tur ∨ görev sınırı) · lider hafızası (durum taşımaz — m.42 d katı başlangıç; öğrenme desenleri tohum dosyasından NASIL okunur) · yetki sınırı (lider karar ALAMAZ, Katman-2 icra + kayıt) · geri-dönüş (liderden Fable'a devir notu formatı)?"
saha_sorusu_ib64c:    İB-64c emri `cc/gorev-2026-09-03-ib64c-ekip-lideri-paketi.md`'deki soru AYNEN (statik vs hafızası-gelişen lider · lider↔işçi bağlam-devri emsalleri); Karar 89 ile kıyas satırı artık "Fable→Opus→Sonnet üç katman"a göre yazılır (emirdeki "Fable-Sonnet ikilisi" ifadesi bu emirle SÜPERSEDE).
ic_envanter:          `core/ajan-metodolojisi.md` §4/§6 · `core/tuzuk-v0.md` m.30/42/44 · `kuyruk/ekip-lideri-ogrenme-desenleri.md` · `cc/devir-2026-08-31-opus-icra.md` §3 (İB-59 lider-arıza ölçümü: 4/4 talimat açığı) · `cc/rapor-2026-08-01-11.md` · `cc/rapor-2026-08-01-19.md` · `cc/rapor-2026-08-14-2.md` · `veri/gorunum/v_baglam_seyri.csv` · `.claude/agents/research-agent.md` R1-R5
tohum_dosyasi:        `kuyruk/ekip-lideri-ogrenme-desenleri.md` (append-only; her desen tasarımda "kullanıldı / kullanılmadı: neden" satırı alır)

## BAĞLAM-MANİFESTİ
eager:            bu emir · Karar 89 satırı (defter) · ajan-metodolojisi §6 · tohum dosyası (≈4 KB)
lazy:             İB-64c emri (aşama 1 başında) · 08-01/08-14 raporlar (KANONDA-BİLİNENLER doğrulaması gerekince) · v_baglam_seyri (eşik tasarımı dalında) · research-agent.md (rol metni şablonu için)
butce:            lider ≤40k bağlam · işçi ≤15k girdi · toplam çıktı ≤110k `[?]`

## SINIRLAR
kapsamda:         (1) İB-64c çift-atlas (tez A/B/C → antitez A/B → maskeli hakem) — saha/literatür emsalleri D/K/X+URL · (2) iç-envanter işçisi: Jarvis'teki mevcut devir mekanizmalarının sayımı (devir dosyaları `cc/devir-*`, manifest şeması, kapsül, paralel-kapi) · (3) lider sentezi: **tasarım paketi v0** = (a) devir birimi şeması (tipli alanlar) · (b) devir-anı yüklemi (m.38 boolean, ölçülebilir eşik + kaynak) · (c) lider rol-metni taslağı `.claude/agents/ekip-lideri.md` (ADAY — hazineye Salih imzasıyla) · (d) geri-dönüş devir-notu şeması · (e) 3 karar modeli (m.37: token×zaman×kalite×risk sayısal, biri karşıt-temelli) masa-10 için · (f) tohum dosyası kullanım satırları.
kapsam_disi:      ekip-liderinin fiilen KURULMASI/koşulması (masa-10 hükmü sonrası ayrı İB) · K-010 GO hükmü · A1-A4 aşamaları · hafızası-gelişen lider (m.42 d: katı başlangıç; yalnız "sonraki adım" notu) · model seçimi tartışması (Karar 89 sabit: Opus 5 medium) · Fable'ın kendi bağlam bütçesini değiştirme (KB-50 kanon).
araclar:          WebSearch/WebFetch (işçi başına ≥2 birincil kaynak fiilen açılır — m.40b kota) · Read/Grep (iç envanter) · sqlite3 `veri/baglam.sqlite` (v_baglam_seyri, deneyim_fts) · Write yalnız `cc/rapor-2026-09-09-ib75-*.md` + `raporlar/2026-09-09-ib75-baglam-devri-ekip-lideri.md` + tohum dosyasına append · git YOK (commit ana-sıranın)
degismezler:      yapan ≠ hakem (D3-i) · V26 URL'siz kotası (D3-ii) · rakam kaynaklı, kestirim `[?]` (m.39) · AS-OF damgası (Karar 68) · lider effort MEDIUM (Karar 89) · lider karar üretmez, SEÇENEK üretir (Katman-1 hüküm Salih) · tohum dosyasına SİLME yok (append-only) · işçi Fable'dan pahalı model kullanamaz.

## DALLAR
D1: eğer İB-64c raporu (`raporlar/2026-09-03-ib64c-*` ∨ `raporlar/*ib64c*`) MEVCUT ∧ D/K/X etiketli → aşama 1 ATLANIR, sentez o rapora oturur; aksi → aşama 1 (çift-atlas) koşulur.
D2: eğer iç-envanter işçisi ≥1 mevcut devir mekanizması bulur (devir dosyası şeması, manifest) → tasarım o şemayı GENİŞLETİR ("hazırı temel al"); aksi → sıfırdan şema ADAY, "emsalsiz" damgalı.
D3: eğer devir-anı için ölçülebilir eşik verisi (`v_baglam_seyri` ≥3 seans) varsa → eşik sayısal önerilir + kaynak; aksi → eşik `[?]` + ölçüm borcu satırı.
D4: eğer hakem sentezdeki ≥1 SAĞLAM iddiayı X'e düşürürse → o iddiaya dayanan tasarım maddesi "DÜŞTÜ" damgalı kalır, paket yine teslim edilir (silme yok).
D-KATMAN1: tasarım paketi bir kanon satırı (tüzük/ajan-metodolojisi) DEĞİŞTİRMEYİ gerektiriyorsa → DUR, masa-10 kalemi olarak yaz; lider kanona yazmaz.

## ÇIKTI SÖZLEŞMESİ
halusinasyon_derecesi: **H = 11 ≥ eşik 7 → TETİK** (`derece.py --v1 --v2 --v3a --v5 --v7a --v7b --v8`: nadirlik +2 · tazelik · atıf-çıktısı OVERRIDE · bileşik · kaynak yok/ham · doğrulayıcı −2; deneysel m.29). Aşama 1 (atlas) kendi maskeli-hakem zincirini taşır; aşama 2 lider SENTEZİ `halusinasyon-engelleyici` ile üretilir (her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR, kaynak-topraklama + bağımsız doğrulayıcı = hakem Opus çağrısı); sayısal eşik iddiaları F1+F2.
cikti_bicimi:     (1) `cc/rapor-2026-09-09-ib75-tez-*.md` / `-antitez-*.md` / `-envanter.md` / `-hakem.md` (işçi ham raporları, ≤2k dönüş) · (2) `raporlar/2026-09-09-ib75-baglam-devri-ekip-lideri.md` (lider sentezi: D/K/X tablosu + tasarım paketi v0 (a)-(f) + masa-10 karar bloğu taslağı) · (3) tohum dosyasına ≤10 append satırı · (4) ledger İB-75/İB-64c durum satırı ÖNERİSİ (ana-sıra yazar).
done_yuklemi:     sentez dosyası VAR ∧ (a)-(f) altı bölüm dolu ∧ hakem raporu sentezden ayrı çağrıda üretildi ∧ her işçi ≥2 birincil kaynak açtı ∧ V26 URL'siz kotası uygulandı ∧ tohum dosyasına ≥1 satır eklendi ∧ kanon dosyasına yazım = 0.
done_olcumu:      DRFR — yukarıdaki 7 koşul tek tek.
yeniden_deneme:   3

## KANONDA-BİLİNENLER (verili kabul et, üstüne koy)
- Karar 86 D1 (09-02): hafızası-gelişen A5 KURULMAZ; öğrenme desenleri tohum dosyasına. Karar 89 (09-09) lider modelini Opus 5 medium yaptı, hafıza kuralı DEĞİŞMEDİ.
- İB-59 (08-31): lider-ajan arızalarının 4/4'ü talimat açığı; rol METNİNE kural yazınca düzeldi → tasarım rol-metni odaklı.
- Tohum dosyası 10 desen (08-31/09-02): işçi çağrıları SENKRON · fan-out×fren çakışması emirde öngörülür · sayaç oturum-geneli · yapan≠ölçen · … (dosyada tam liste).
- 08-01/08-14 raporlar: "Opus lider + Sonnet işçi %90,2" rakamı Opus-spesifik (yeniden geçerli olabilir — Karar 89), bütçe-eşitli kıyasta hafıza modülleri sade tabanı geçemedi.
- Bağlam ölçümü: 09-04 Fable tepe 427.877 / 172 tur >128k; 09-02 Cowork Sonnet 741.072 (`v_baglam_seyri`).
- GEÇMİŞ YÖRÜNGELER (`deneyim-tablo.py --benzer`, 5 sonuç, kuşak 5 = eski Opus-lider koşumları 08-14/08-16: agent ad5b8c31 · a8e8bf9e "ARAŞTIRMA EKİP LİDERİSİN (Opus)"; wf_89527235 tez/antitez/hakem üçlüsü) — "o zaman böyle koştu" notu; profil tahminine taşınmadı (Salih şerhi).

## SKILL TETİKLERİ
- skill:              atlas-kosum
  tetik_kosulu:       D1 aksi dalı (İB-64c raporu YOK) ∧ pipeline aşama-1 başladı; İB-64c raporu VARSA ÇAĞIRMA
  cagri_kipi:         literal
  girdi:              arastirma_sorusu = saha_sorusu_ib64c (yukarıda) · aile = {A: statik/tanımlı lider desenleri, B: bağlam-devri mekanizmaları (handoff/summary/checkpoint), C: yetki-sınırlı lider (permission/guardrail)} · işçi Sonnet medium · sentez+hakem Opus medium (R5)
  baglam:             hedef = tasarım paketinin dış kanıt tabanı · çıktı = D/K/X+URL rapor, işçi dönüşü ≤2k · araç = WebFetch/WebSearch + Read(iç envanter) · sınır = tasarım üretme, yalnız kanıt
  yan_etki_damgasi:   eklemeli × idempotent:h × dış-dünya:h
  done_yuklemi:       rapor D/K/X etiketli ∧ tez→antitez→maskeli hakem üç aşama koşuldu ∧ m.40b üçlüsü uygulandı
  hata_yolu:          sözleşme-ihlali → Fable düzeltir · yürütme → telafi · retry ≤3 · FAIL-LOUD
  sira:               1/3 · handoff = `cc/rapor-2026-09-09-ib75-*.md` → aşama 2 lider sentezi
  kayit:              execute_tool · tool.name=atlas-kosum · agent=Sonnet(işçi)/Opus(lider) · model+sürüm · tarih → skill sayacı
- skill:              halusinasyon-engelleyici
  tetik_kosulu:       aşama 2 lider sentezi yazılırken (H = 11 ≥ 7) ∧ işçi ham raporları diskte; ham raporlar eksikse ÇAĞIRMA (önce aşama 1)
  cagri_kipi:         literal
  girdi:              gorev = sentez (a)-(d) metni · kaynaklar = `cc/rapor-2026-09-09-ib75-*.md` + KANONDA-BİLİNENLER pointer'ları · derece = 11
  baglam:             hedef = her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR etiketli sentez · çıktı = `raporlar/2026-09-09-ib75-baglam-devri-ekip-lideri.md` §D/K/X · araç = Read (ham raporlar) + WebFetch (yeniden açma) · sınır = yeni araştırma yok, yalnız topraklama; doğrulayıcı = ayrı Opus medium hakem çağrısı (yapan ≠ ölçen)
  yan_etki_damgasi:   eklemeli × idempotent:e × dış-dünya:h
  done_yuklemi:       sentezdeki iddia sayısı = etiketli iddia sayısı ∧ DAYANAKSIZ iddialar tasarım maddesine dayanak YAPILMADI
  hata_yolu:          sözleşme-ihlali → Fable düzeltir · yürütme → telafi · retry ≤3 · FAIL-LOUD
  sira:               2/3 · handoff = etiketli sentez → karar-modeli
  kayit:              execute_tool · tool.name=halusinasyon-engelleyici · agent=Opus(lider) · model+sürüm · tarih → skill sayacı
- skill:              karar-modeli
  tetik_kosulu:       aşama 2 sentez bitti ∧ etiketli ∧ (a)-(d) dolu; aksi ÇAĞIRMA
  cagri_kipi:         literal
  girdi:              karar_sorusu = "Bağlam-devri ekip-lideri v0 hangi devir-birimi + devir-anı + yetki modeliyle kurulsun?" · girdi = sentez (a)-(d)
  baglam:             hedef = masa-10 kalemi (3 model, biri karşıt-temelli, sayısal token×zaman×kalite×risk) · çıktı = defter bloğu taslağı · sınır = hüküm Salih'in
  yan_etki_damgasi:   salt-okur × idempotent:e × dış-dünya:h
  done_yuklemi:       3 model ∧ ≥1 karşıt-temelli ∧ 4 eksen sayısal ∧ önerilen işaretli
  hata_yolu:          sözleşme-ihlali → Fable düzeltir · retry ≤3 · FAIL-LOUD
  sira:               3/3 · handoff = sentez dosyası §(e)
  kayit:              execute_tool · tool.name=karar-modeli · agent=Opus(lider) · model+sürüm · tarih → skill sayacı

## Teslim
`raporlar/2026-09-09-ib75-baglam-devri-ekip-lideri.md` (insan-yüzü, emir yolu KAZANIR — Karar 88 M7 ⑤) + `cc/rapor-2026-09-09-ib75-*.md` (ham) + tohum append + ledger öneri satırı. Manifest: `veri/manifest/u8-ib75-baglam-devri-ekip-lideri.json` (koşum öncesi pipeline-kosum yazar; `tur: pipeline`).

## DİNAMİK EK
tarih: 2026-09-09 · HEAD: 4ac755b (Karar 89 paketi) · tetikleyen: Salih "plan evet" (m.16 raporu sonrası) + Karar 88 M8 (a) · halusinasyon_derecesi: H = 11 (derece.py 09-09, exit 10 TETİK) · kanıt AS-OF: v_baglam_seyri 2026-09-08 çekimi.
