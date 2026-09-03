# Görev Emri — İB-64b: K-010 A4 aşama-araştırması — denetim-çatalı Codex'siz çözüm emsalleri

*Derleyen: Carvis yan-oturum işçisi (gorev-emri-derleme skill'i, 2026-09-03). Kaynak: `veri/karar-borcu.jsonl` İB-64b satırı + `core/pano.md` K-010 kartı + `kuyruk/k010-zincir-2026-08-29.md`. Rejim: Karar 85/86 — Fable planlayıcı, Sonnet işçi; [rejim: maliyet-öncelikli].*

## Görev tanımı (tek cümle)
K-010 A4 (ajan-hazırlık: defter şeması v1 ∧ D4 tasarım kartı ∧ denetçi bütçe-çatalı çözümü) için, Karar 82(b) kısıtı altında (**Codex'siz** — dış model bağımlılığı yasak) aile-içi model ↔ kurallı/deterministik denetim çatalını nasıl çözdüğüne dair dış saha/literatür emsalleri bulunacak; D4 tasarım kartı onayının araştırma-önkoşulunu doldurur.

## Kapsam
- **Kapsamda:** LLM-tabanlı denetim (aile-içi model, örn. Sonnet↔Sonnet çapraz-denetim) ile kurallı/deterministik denetim (script, şema-doğrulama, statik kural motoru) arasındaki maliyet/güvenilirlik çatalını çözen saha örnekleri; "yapan≠ölçen" ilkesini (m.40b Karar 86 D3-i) donanımsal/aile-içi ortamda nasıl uyguladıkları; Codex-benzeri harici-model denetçiyi devre dışı bırakıp iç-model veya kural-motoruyla eşdeğer güvence sağlayan mimariler.
- **Kapsam dışı:** A2 guardrail konusu (İB-64a'nın işi); A5 ekip-lideri paketi (İB-64c'nin işi); D4 tasarım kartının kendisinin yazımı/onayı (bu araştırma D4'ün ÖNKOŞULU, D4'ü üretmez — Katman-KARAR ADIM-4'te Salih hükmüne bağlı); Codex kullanımının yeniden tartışılması (Karar 82(b) kesin kısıt, bu emir sorgulamaz).
- **Kaynak-pointer'lar:** `veri/karar-borcu.jsonl` (İB-64b satırı) · `core/pano.md` K-010 kartı (A4 tanımı: "ajan-hazırlık: defter şeması v1 ∧ D4 tasarım kartı ∧ denetçi bütçe-çatalı çözümü") · `kuyruk/k010-zincir-2026-08-29.md` ADIM 4 satırı ("A4 denetim-çatalı hükmü — Codex'siz (Karar 82(b)): aile-içi model ∨ kurallı/deterministik denetim; + D4 tasarım kartı onayı") · Karar 82(b) metni (`core/ajan-metodolojisi.md` / senaryo-defteri, "Codex'siz tasarım" kısıtı).

## KANONDA-BİLİNENLER (mükerrer araştırma freni)
Karar 82(b) kısıtı KESİN: Codex (harici model denetçi) kullanılmayacak. A4 henüz çözülmedi (pano: "A4: çatal-hükmü bekliyor; araştırması İB-64b"). Firstmate rolü (İB-07/09) ve "yapan≠ölçen" ilkesi (Karar 86 D3-i) zaten kanonda var — bu araştırma bunları YENİDEN İCAT ETMEZ, üstüne örnek arar.

## m.40b KONTRAT ŞARTLARI (Karar 86 D3, `core/ajan-metodolojisi.md` §"Ek fıkra — koşum-sözleşmesi üçlüsü")
1. **Yapan ≠ ölçen:** Tez/antitez/sentez yazan Sonnet ajanı aynı koşumda hakemlik YAPAMAZ; hakem ayrı çağrı, yalnız ham veri (iddia+kanıt) alır — emrin beklentisi verilmez. (Not: bu görevin KONUSU da "yapan≠ölçen" denetim-çatalı olduğundan, koşumun kendisi de bu ilkeyi ihlal etmeden yürütülür — özyinelemeli tutarlılık kontrolü.)
2. **V26 URL'siz-iddia kotası:** örneklem son üçlükten ≥1 kaynak iddiası + tüm sayısal iddialar + ≥1 URL'siz/model-hafızası iddia zorunlu örneklenir.
3. **Birincil-kaynak açma kotası:** işçi başına ≥2 kaynak fiilen açılır (WebFetch/curl); yalnız özetten yazılan bulgu K'da kalır.

Üç şart `atlas-kosum` skill adım 3/5/6'da gömülü; SKILL TETİKLERİ bloğunda literal çağrı + atlas ajanına açık talimat olarak iletilir.

## Beklenen çıktı formatı
D/K/X + URL etiketli rapor (`atlas-kosum` şablonu). Ek olarak: çatal kararına doğrudan girdi olacak İKİ SEÇENEKLİ karşılaştırma tablosu (aile-içi model denetim ↔ kurallı/deterministik denetim; eksen: maliyet, güvenilirlik-kanıtı, Codex'siz uyumluluk) — D4 tasarım kartına pointer olarak düşer, kartı YAZMAZ.

## SKILL TETİKLERİ
- skill: atlas-kosum
  tetik_kosulu: İB-64b koşuma alınırken (Salih ∨ sıradaki icra oturumu tetiği)
  cagri_kipi: literal
  girdi: arastirma_sorusu = "Codex'siz (Karar 82(b)) kısıtı altında, LLM-tabanlı denetim (aile-içi model) ile kurallı/deterministik denetim arasındaki bütçe/güvenilirlik çatalını çözen saha/literatür emsalleri nelerdir?"
  baglam: hedef=D4 tasarım kartı araştırma-önkoşulu · çıktı-formatı=D/K/X+URL rapor + 2-seçenekli karşılaştırma tablosu, işçi dönüşü ≈1-2k özet · araç=WebFetch/WebSearch+Read(iç envanter, Karar 82 metni) · sınırlar=Codex seçeneğini yeniden önerme yok, D4 kartını yazma yok
  yan_etki_damgasi: eklemeli × idempotent:h × dış-dünya:h
  done_yuklemi: rapor D/K/X etiketli ∧ ≥2 dik aile (aile-içi-model-denetim, kurallı/deterministik-denetim) tarandı ∧ m.40b üçlüsü uygulandı ∧ karşılaştırma tablosu üretildi
  hata_yolu: sözleşme-ihlali → çağıran (Carvis) düzeltir · yürütme hatası → telafi · retry ≤3 · FAIL-LOUD
  sira: 1/1 · handoff = `raporlar/` altına rapor dosyası + senaryo-defteri tek-satır gözlem
  kayit: execute_tool · tool.name=atlas-kosum · agent=Sonnet(işçi) · model+sürüm · tarih → skill sayacı

## ÇIKTI SÖZLEŞMESİ
- halusinasyon_derecesi: atıf/URL-yoğun rapor → H ≥ eşik kabul edilir; atlas-kosum kendi doğrulama zincirini taşır (halusinasyon-engelleyici ayrıca çağrılmaz).
- cikti_bicimi: `raporlar/2026-09-03-ib64b-denetim-catali-emsalleri.md` (D/K/X+URL + karşılaştırma tablosu) + `veri/karar-borcu.jsonl` İB-64b satırına durum güncellemesi.
- done_yuklemi: rapor dosyası yazıldı ∧ m.40b üçlüsü uygulandı ∧ karşılaştırma tablosu D4'e pointer olarak düştü ∧ Codex kararı yeniden tartışılmadı — DRFR.
- yeniden_deneme: 3

## Teslim
`raporlar/2026-09-03-ib64b-denetim-catali-emsalleri.md` + `veri/karar-borcu.jsonl` durum güncellemesi.
