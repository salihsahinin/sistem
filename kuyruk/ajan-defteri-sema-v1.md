# Ajan Defteri — Şema v1 (K-010/A4; deneysel m.29)

*Açılış: 2026-07-22 (Salih emri: K-010 tetiği kanıt-kapılarına çevrildi; A4 paketi). Kaynaklar: m.30 (kalıcılık + ajan-başına ingest + katmanlama) · m.42 (pozitif yetki listesi) · m.44 (rol katmanları) · taksonomi D1-D8 (07-21 kabul, deneysel) · yetki-formülasyonu 07-15 (Özgürlük(a) ≤ Toparlanabilirlik(hata(a))) · çeşitlilik-bütçesi 07-17 · defter-token boşluğu notu (build-tartisma-notlari). Format deneysel; ilk canlı koşum verisiyle kalibre edilir. Silme yok — emekli ajan ARŞİV statüsüne iner (m.8/m.30a: tanınmış ajan unutulmaz).*

## Kart şeması (ajan başına bir kart; defter = bu dosyanın altındaki kartlar, şişince `kuyruk/ajanlar/` klasörüne bölünür — pointer korunur)

**1. Kimlik:** ad · arketip · D1-D8 etiket vektörü · katman (m.44: Carvis / lider / işçi) · statü (ADAY / TANINMIŞ / ARŞİV — m.30a: atama anında TANINMIŞ, wiki sayfası `wiki/ajan-<ad>.md` o an açılır).
**2. Model + çeşitlilik:** seçili model+effort · alternatifler (karar-modeli deseni: seçilen + 2 alternatif hafızada, koşum verisiyle tartı yenilenir) · çeşitlilik-bütçesi (07-17 lojiği: alternatif-üretme yetkisi pozitif listeyle, "n≤k, şu sınırlar içinde"; icra ajanı temp≈0).
**3. Yetki (m.42):** POZİTİF yetki listesi (sadece ne YAPABİLİR) · kırmızı çizgiler · dosya-yazım kapsamı (yol listesi) · gevşetme koşulu = sicil ∧ geri-alınabilir(hata-sınıfı) ∧ token-zaman-baskısı (07-15, üçü birden; katı başlar).
**4. Durma + fren:** durma koşulu (DONE kuralı: yazılamıyorsa ajan kurulmaz) · tur limiti · süre tavanı · sert token-bütçesi · sıfır-ilerleme-durdur (saha standardı: 3 tur / 10 dk sınıfı, deneysel).
**5. İngest + önek:** ajan-başına özütleme algoritması (m.30b — pointer) · kararlı-prefix bloğu adresi (durağan-önce, oynak-sonda; TTL sınıfı).
**6. Sicil (koşum başına bir satır):** tarih · görev · süre · token (usage-log şemasıyla aynı kolonlar — `raporlar/usage/`; Routine'de /usage yok boşluğu bilinir, otomatik-usage K-020 hattı) · sonuç (OK/FAIL) · incident notu · kalite/Brier alanı (m.37 RİSK boyutunun veri kaynağı).

## Kanonik örnek kartı — araştırma-filosu işçisi (D4; ilk canlı-ajan sınıfı, 07-21 kararı: en düşük bahis)

- **Kimlik:** `arastirma-iscisi-01` · arketip: araştırmacı · D-vektör: D4 iki-yönlü (bilgi toplar-raporlar), D8 özerklik DÜŞÜK · katman: işçi (lider yok → Carvis doğrudan yönetir, m.44 istisnası) · statü: ADAY (yürürlük = K-010 tetiği).
- **Model:** önerilen aile-içi orta-katman + effort default (07-14 K-017 önerisi); alternatifler: üst-model kısa-koşum / ucuz-model çok-tur — "ucuz model ≠ ucuz iş" dersi tartıda. Çeşitlilik: 0 (icra sınıfı; çift-atlas çeşitliliği YAPIDAN gelir — tez+antitez=¬ iki ayrı koşum, m.40b).
- **Yetki:** YAPABİLİR: web/doküman okuma · rapor yazımı YALNIZ `claude/`-önekli branch'e (07-18 emsali) · cevaplanmamış soruyu rapora gömme. KIRMIZI: kanon dosyalarına yazım · commit ana dala · karar biriktirme · araç kurulumu.
- **Durma:** DONE = rapor dosyası çift-atlas kontratında yazıldı ∧ kaynak listesi D/K/X etiketli. Fren: ≤1 koşum-turu, sert bütçe kart-atamasında yazılır (token×zaman m.21).
- **İngest:** koşum-sonrası Carvis süzgeci (kör aktarım yasak, m.17); ajan kendi arşiv-özütünü taşımaz (işçi sınıfı — özüt lider katmanında başlar, m.30c).
- **Sicil:** boş — ilk satır K-010 gününde. Denetçi bağı: çıktı iddia-listesi formatında denetçiye gider (CoVe-Factored ailesi; denetçi=GPT bütçe-koşullu, defter 07-22).

## Ek — 07-22 akşam revizyonları
- **Yetki alanına zorunlu bayrak (rapor-07-22-1 #5 önerisi; Katman-2 deneysel, veto açık):** kartın Yetki bölümüne `kabuk/exec: VAR/YOK` alanı eklenir; **VAR ise dış-bant izolasyon (OS sandbox/WSL2/container/settings-deny) ZORUNLU** — gerekçe: kabuk-taşıyan ajan allowlist ne olursa olsun zaptedilemez (A5-F2 sağlam çekirdeği, [D]). Windows-native'de OS sandbox YOK → mevcut fazda varsayılan: işçi ve lider ajanlara kabuk/exec VERİLMEZ.
- **Statü terminolojisi (Salih kararı 07-22):** Atlas = CC alt-ajanı, bizim oluşturduğumuz bir ajan DEĞİL → lider sıfatı ALAMAZ; statüsü NİTELİKLİ İŞÇİ (dış-araç işçisi; defterde kartı açılmaz, koşum kaydı görev raporlarında yaşar). Kendi araştırma ajanımız ayrıca kurulacak — kanonik kart zaten bu sınıf: `arastirma-iscisi-01` (D4). Lider adayı ancak bizim tasarladığımız, defter-kartlı ajan olabilir.
- **Lider tasarım-deseni (rapor A5 sağlam çekirdeği):** lider = bağlam-SIKIŞTIRAN süpervizör (tek sürekli sahip) + kısa-ömürlü read-only özet-döndüren işçiler + YALNIZ paralelleşebilir/geniş iş (derleme · ön-süzgeç · rapor-yorumlama · tarama); bağlı/sıralı/yazma-ağırlıklı işe lider konmaz. Ölçüm: eşit-token-bütçeli ablation (m.35), "+%90 kalite" tek başına kanıt değil.
- **Sert-bütçe fren standardı (A2 kalemi, deneysel m.29; kaynak: rapor-07-22-1 A2/A3-F2 sağlam çekirdeği):** her otomasyon/ajan koşumuna kart-atamasında YAZILI sert bütçe: tur-tavanı (varsayılan ≤3) ∧ **adım-içi fan-out tavanı (varsayılan ≤5 paralel — tur-sayacı tek başına YETMEZ, vaka #4095)** ∧ sert token-tavanı ∧ süre-tavanı ∧ sıfır-ilerleme-durdur. Fren EYLEM katmanında yaşar (script/harness), hook'a GÖMÜLMEZ (fren-katmanı kaçış-vektörü olmasın); LLM'siz koşumlar (açılış-senkron) muaf — kendi ff-only/idempotent sigortası yeter. Rakamlar deneysel, ilk gerçek loop koşumunda kalibre.
