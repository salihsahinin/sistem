# Görev Emri — İB-64a: K-010 A2 aşama-araştırması — guardrail/policy-as-code emsalleri

*Derleyen: Carvis yan-oturum işçisi (gorev-emri-derleme skill'i, 2026-09-03). Kaynak: `veri/karar-borcu.jsonl` İB-64a satırı + `core/pano.md` K-010 kartı + `kuyruk/k010-zincir-2026-08-29.md`. Rejim: Karar 85/86 — Fable planlayıcı, Sonnet işçi; [rejim: maliyet-öncelikli].*

## Görev tanımı (tek cümle)
K-010 A2 (guardrail saha-testi) aşamasında Jarvis'in fiilen kurduğu guardrail/policy-as-code mekanizmaları (PreToolUse kilit, revert tatbikatı, sert-bütçe) dış literatür/saha emsalleriyle ne ölçüde örtüşüyor, hangi boşluklar açık — atlas araştırmasıyla belirlenip G0/G4 raporuna (`raporlar/2026-07-16-jarvis-gelistirme-proje-fikirleri-zorluk-partisyonlari.md`) bağlanacak.

## Kapsam
- **Kapsamda:** guardrail/policy-as-code emsalleri (OPA/Rego, sandbox/permission sistemleri, LLM tool-call guardrail çerçeveleri, PreToolUse/interrupt desenleri); bulguların G0 (Hazır Zemin & Ölçüm Cetveli) ve G4 (Güvenlik, Bağışıklık & Gözlemlenebilirlik, `raporlar/2026-07-16-...md:67`) başlıklarına eşlenmesi; Jarvis'in mevcut A2 kanıtı (`kuyruk/k010-zincir-2026-08-29.md` ADIM-0 satırı: PreToolUse canlı PASS · M-9 revert tatbikatı · İB-54 fren kurulumu) ile dış emsal kıyası.
- **Kapsam dışı:** A2 kapısının kendisini yeniden açma/kapatma hükmü (pano zaten "A2 kapısı TAMAM" diyor — bu emir kapıyı SORGULAMAZ, yalnız kanıtı araştırma-kapısı formatına bağlar); A4 denetim-çatalı konusu (İB-64b'nin işi); A5 ekip-lideri paketi (İB-64c'nin işi); K-010 GO hükmü (Katman-1, Salih'e ait).
- **Kaynak-pointer'lar:** `veri/karar-borcu.jsonl` (İB-64a satırı) · `core/pano.md` K-010 kartı (satır 34, A2 tanımı: "guardrail saha-testi: PreToolUse kilit canlı PASS ∧ revert tatbikatı ∧ sert-bütçe yazılı") · `kuyruk/k010-zincir-2026-08-29.md` ADIM-0 ve durum-sayacı bölümleri · `raporlar/2026-07-16-jarvis-gelistirme-proje-fikirleri-zorluk-partisyonlari.md` G0/G4 başlıkları.

## KANONDA-BİLİNENLER (mükerrer araştırma freni)
A2 kapısı zaten "TAMAM" hükmünde (Karar 83 sonrası, kanıt 3/3 + İB-54(3) imzalı + tatbikat-kaydı derlendi, commit 15dcaf2) — bu araştırma kapıyı AÇMAZ, geriye-dönük "doğru mu yapılmış" denetimine (A7 ailesi) girdi sağlar ve G0/G4 raporuna pointer düşer. Verili kabul et: PreToolUse kilit + M-9 revert + İB-54 fren üçlüsü fiilen kurulu ve test edilmiş.

## m.40b KONTRAT ŞARTLARI (Karar 86 D3, `core/ajan-metodolojisi.md` §"Ek fıkra — koşum-sözleşmesi üçlüsü")
1. **Yapan ≠ ölçen:** Tez/antitez/sentez yazan Sonnet ajanı aynı koşumda hakemlik YAPAMAZ. Hakem ayrı bir Sonnet çağrısı (ya da Fable ana-sıra) olarak kurulur; hakem ajanına YALNIZ ölçülecek ham veri (iddia + kanıt) verilir — emrin yazarı, beklenen sonuç, "ne bulunmalı" gibi bilgi VERİLMEZ.
2. **V26 URL'siz-iddia kotası:** Hakemlik öncesi örneklem denetimi kural-tabanlı seçilir — (a) çıktının son üçte birinden ≥1 kaynak iddiası + (b) tüm sayısal iddialar + (c) son üçlükten ≥1 URL'siz/model-hafızası iddiası ZORUNLU örneklenir (yalnız "somut ve URL'li" iddiadan seçim YASAK — en riskli sınıfı atlar).
3. **Birincil-kaynak açma kotası:** İşçi (tez ajanı) başına ≥2 kaynak GERÇEKTEN açılır (WebFetch/curl ile); yalnız arama-özetiyle yazılan bulgu K etiketinde kalır, D'ye yükselemez.

Bu üç şart `atlas-kosum` skill'inin adım 3/5/6'sında zaten gömülü — SKILL TETİKLERİ bloğunda literal çağrı yapılır, atlas ajanına ayrıca bu üç madde açık talimat olarak iletilir.

## Beklenen çıktı formatı
D/K/X + URL etiketli rapor (`atlas-kosum` şablonu, `.claude/skills/atlas-kosum/references/rapor-sablonu.md`): **D** = birincil kaynaktan doğrulandı, **K** = arama-özeti/teyide muhtaç, **X** = doğrulanamadı/çelişkili — her bulgu URL + AS-OF tarih damgalı (Karar 68 anakronizm freni). Sentez bölümünde "hayatta-kalan çekirdek + daralan/düşen iddialar" yapısı (kör-kesişim değil). Kapanışta SAĞLAM/DARALDI/DÜŞTÜ oranı tek satır.

## SKILL TETİKLERİ
- skill: atlas-kosum
  tetik_kosulu: İB-64a koşuma alınırken (Salih ∨ sıradaki icra oturumu tetiği)
  cagri_kipi: literal
  girdi: arastirma_sorusu = "Jarvis'in guardrail/policy-as-code mekanizmaları (PreToolUse kilit, revert tatbikatı, sert-bütçe) dış saha/literatür emsalleriyle nasıl kıyaslanır; G0/G4 raporuna hangi ek/boşluk düşer?"
  baglam: hedef=A2 kanıtının araştırma-kapısı formatına bağlanması · çıktı-formatı=D/K/X+URL rapor, işçi dönüşü ≈1-2k özet · araç=WebFetch/WebSearch+Read(iç envanter) · sınırlar=A2 kapısını yeniden açma yok, yalnız kıyas+pointer
  yan_etki_damgasi: eklemeli × idempotent:h × dış-dünya:h
  done_yuklemi: rapor D/K/X etiketli ∧ ≥2 dik aile (guardrail-çerçeveleri, policy-as-code) tarandı ∧ m.40b üçlüsü (yapan≠ölçen, V26, ≥2 kaynak) uygulandı ∧ G0/G4 başlıklarına en az 1 satır pointer düşüldü
  hata_yolu: sözleşme-ihlali → çağıran (Carvis) düzeltir · yürütme hatası → telafi · retry ≤3 · FAIL-LOUD
  sira: 1/1 · handoff = `raporlar/` altına rapor dosyası + senaryo-defteri tek-satır gözlem
  kayit: execute_tool · tool.name=atlas-kosum · agent=Sonnet(işçi) · model+sürüm · tarih → skill sayacı

## ÇIKTI SÖZLEŞMESİ
- halusinasyon_derecesi: atıf/URL-yoğun rapor → H ≥ eşik kabul edilir (m.40b zaten adversarial-hayatta-kalma + V26 taşıyor; ayrıca halusinasyon-engelleyici çağrısı gerekmez — atlas-kosum kendi doğrulama zincirini taşıyor, `core/halusinasyon-paketi.md` F7 referansı adım 5'te zaten var).
- cikti_bicimi: `raporlar/2026-09-03-ib64a-guardrail-emsalleri.md` (D/K/X+URL) + `veri/karar-borcu.jsonl` İB-64a satırına durum güncellemesi.
- done_yuklemi: rapor dosyası yazıldı ∧ m.40b üçlüsü uygulandı ∧ G0/G4 pointer düşüldü ∧ A2 kapısına dokunulmadı — DRFR, her koşul tek tek işaretlenir.
- yeniden_deneme: 3

## Teslim
`raporlar/2026-09-03-ib64a-guardrail-emsalleri.md` + `veri/karar-borcu.jsonl` durum güncellemesi (icra-sırada → tamam ∨ kısmi not).
