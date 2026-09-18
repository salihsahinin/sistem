# Ölçüm Bankı

**Üst blok:** Jarvis'in kalıcı sayısal ölçüm defteri — yalnız GA'lı/örneklemli ölçümler girer, silinmez (çürürse üstü çizilir). · **Durum:** **güncel** (deneysel, m.29) · **Son teyit:** 2026-08-01 (açılış günü) · **Kaynaklar:** `kuyruk/olcum-banki.md` (defterin kendisi — kanonik kaynak, bu sayfa damıtılmış özettir) · tüzük m.29 (deneysel statü) · m.39 (giriş kuralı) · m.8 (çürüme kuralı) · `cc/rapor/2026-08/rapor-2026-08-01-5.md` §2-§3 (ilk iki ölçümün kaynağı) · **Güven:** orta (tek açılış günü, iki ölçümlük örneklem; defterin kendisi henüz genç).

## Çekirdek
Ölçüm bankı, "biliyoruz sandığımız ama aslında GA'sız kestirim olan" sayılarla gerçek örneklem sonuçlarını aynı yerde tutmamak için açıldı (Salih imzası, 2026-08-01, 08-01-5 ingest K3 kararı). Defter yalnız belirsizlik aralığı ve örneklem büyüklüğü hesaplanabilmiş ölçümleri kabul eder; sezgi, kaba sınıf ya da tek-noktalı kestirim buraya giremez (m.39) — böyle adaylar ayrı bir sınıfta ("bekleyen ölçüm") bekletilir. Bir ölçüm sonradan çürürse satır silinmez; üstü çizilir ve onu çürüten kaynak yanına eklenir (m.8) — banka böylece hem büyüyen hem de kendi hata tarihini taşıyan bir kayıt olur.

**Kanonik örnek (damıtılmış):** Ö-1 satırı — "debi üssü γ (öz-pay bileşeni)" = 0,7569 ± 0,0588, %95 GA [0,6366; 0,8771], n=31, kaynak `cc/rapor/2026-08/rapor-2026-08-01-5.md` §3, damga [D-ölçüm]. Şema tüm alanların doldurulmasını zorunlu kılar: aralık yoksa (yalnız nokta tahmini varsa) satır bankaya giremez, "bekleyen ölçüm" ya da başka bir deftere gider.

## Şema
| Alan | Anlamı |
|---|---|
| Ölçüm | ne ölçüldüğü (kısa ad) |
| Değer ± hata | nokta tahmini + standart hata/sapma |
| %95 GA | güven aralığı — GA'sız satır banka dışı (m.39) |
| n | örneklem büyüklüğü |
| Yöntem-notu | fit yöntemi, duyarlılık kontrolleri, dışlanan alt-sınıflar (kısa) |
| Kaynak | ölçümü üreten rapor dosyası + bölüm (pointer, m.20 ailesi) |
| Tarih | ölçüm tarihi |
| Damga | köken etiketi (örn. `[D-ölçüm]` = damıtılmış ölçüm) |

## Giriş kuralı (m.39)
Yalnız GA'lı/örneklemli ölçüm girer. Kestirim, kaba sınıf ya da tek-kaynaklı gözlem (örn. "Salih gözlemi ~26 dk/koşum, GA'sız") bu kurala takılıp dışarıda kalır — kendi başlarına yanlış değildir, yalnız bu defterin eşiğini geçmez; ön-koşulu tamamlanınca "bekleyen ölçüm"den bankaya terfi edebilirler.

## Çürüme kuralı (m.8)
Bir ölçüm yeni bulguyla çelişirse satır silinmez: üstü çizilir, yanına çürüten kaynağı gösteren bir not eklenir. Banka böylece "şu an doğru bildiğimiz" değil "ne bilip ne zaman öğrendiğimiz" kaydını tutar — süpersede zinciri mantığı burada da geçerli.

## Uyarı-satırı sınıfı
m.39 kapsamı dışında, ölçüm değil nitel güvenilirlik ilkesi taşıyan satırlar ayrı listelenir. Örnek — U-1: "alt-ajan aktarımında sayı-sadakati ≫ mekanizma-sadakati" (rakam/künye genelde doğru taşınır, "neden böyle" katmanı ajan tarafından yeniden üretilir); 3 bağımsız gözlemle desteklenir, kaynak `raporlar/2026-08/2026-08-01-ingest-grafhatti.md` §5.4/§6.

## Bekleyen-ölçüm sınıfı
Ön-koşulu tamamlanmamış adaylar burada beklerken bankaya girmez: θ (kullanım ufku üssü — görev emri sıraya alındı) · γ_taşınan (debi'nin ikinci bileşeni, henüz ölçülmedi) · araştırma-koşumu süresi (GA'sız gözlem, n≥10 hedefi bekliyor) · koşum-maliyeti sınıf-medyanları (ön-koşul: dedup betiği düzeltmesi — mevcut rakamlar heterojen aygıtlardan, karışık örneklem GA'sı anlamsız).

## Sop — yeni ölçüm eklerken
1. GA/n hesaplanabiliyor mu kontrol et (m.39) — hesaplanamıyorsa bekleyen-ölçüme ya da başka bir kayda yaz, bankaya girme.
2. Şemanın tüm alanlarını doldur; kaynağı dosya+bölüm düzeyinde pointer'la (m.20 ailesi — ham veri taşınmaz, adresi taşınır).
3. Eski bir ölçümü çürütüyorsa: o satırı silme, üstünü çiz + bu satırın kaynağını ekle (m.8).
4. Ölçüm değil nitel ilke ise Uyarı-satırı sınıfına, ön-koşullu adaysa Bekleyen-ölçüm sınıfına yaz — üç sınıf karıştırılmaz.
5. Değişikliği `kuyruk/olcum-banki.md`de yap; bu wiki sayfası yalnız damıtılmış özettir, bayatlarsa yeniden damıtılır.

## Gotchas
- En sık tuzak: kestirimi "ölçüm" diye bankaya sokmak (m.39 ihlali) — GA yoksa dur.
- Damga alanı süs değildir: köken etiketi olmadan satır izlenebilirliğini kaybeder (pointer-sistemi ailesi).
- Sayı doğru taşınsa da gerekçe/mekanizma katmanı alt-ajan aktarımında bozulabilir (bkz. U-1) — sayının yanına gerekçesiz güvenme.

## Mevcut içerik anlık görüntüsü
*(bayatlayabilir; güncel durum her zaman `kuyruk/olcum-banki.md`de)*
- Ö-1 — debi üssü γ (öz-pay bileşeni): 0,7569 ± 0,0588, GA [0,6366; 0,8771], n=31 — kaynak `cc/rapor/2026-08/rapor-2026-08-01-5.md` §3.
- Ö-2 — uç-birim genişliği ölçek üssü: +0,0957 ± 0,018, GA [0,060; 0,132], n=76 (26 aile) — kaynak `cc/rapor/2026-08/rapor-2026-08-01-5.md` §2.

## Süpersede zinciri
— (ilk sürüm)

## Bağlantılar
[[sozluk]] (γ_öz/γ_taşınan ve debi tanımı — ölçeklenme sözlüğü) · [[pointer-sistemi]] (m.20 ailesi — kaynak dosyada, özet burada) · [[token-x-zaman]] (bekleyen "koşum-maliyeti sınıf-medyanları" ölçümü aynı token×zaman çerçevesinde okunur) · aday (henüz wiki sayfası yok, düz metin): `kuyruk/senaryo-defteri.md` — m.37 karar kayıtlarının adresi.
- [[stokastik-dusunce]] — EMEKLİ/RED (Salih 08-17): olasılık-beyanı/Brier hattı sisteme **girmez**; sayfa halef "deterministik tasarım" ilkesini taşır (karşı-link 08-16'da açılmıştı, 08-17 güncellendi).

**Bağlantılar:** · [[baglam-veri-ambari]] (karşı-link 08-22) · [[gorsel-artefakt-dogrulama]] (karşı-link 08-22) · [[no-mistakes]] (karşı-link 08-22) · [[dil-secimi]] (karşı-link 08-26) · [[anakronizm-freni]] (karşı-link 08-26) · [[kolon-katmani]] (karşı-link 08-29) · [[ajan-metodolojisi]] (karşı-link 09-03)
