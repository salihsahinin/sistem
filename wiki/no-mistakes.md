# no-mistakes

**Tanım:** Kod değişikliğini hedefine (push/PR) ulaşmadan önce otomatik kapılardan — kod incelemesi · test · lint · doküman · push · PR · CI — geçiren üçüncü-parti doğrulama pipeline'ı; Jarvis'te ana-sıra push hattının araç-düzeyi doğrulayıcısı. **Durum:** GÜNCEL · **Son teyit:** 2026-08-21 (PR #2 merge + PR #3 süreci bu araçla yürüdü). **Kaynaklar:** `raporlar/vardiya/vardiya-teslim-2026-08-12-l8-mac.md` §1-3 · pano K-015 L8 kaydı (`core/pano.md`) · L8 araç raporu `cc/rapor/2026-08/rapor-2026-08-03-4.md`. **Güven:** orta — iki platform kurulumu (Win v1.41.2 · Mac v1.48.0) + çok koşum gözlemi; tek-kullanıcı sahası, dış benchmark yok.

## Çekirdek

Pipeline, değişikliği hedefe götürmeden önce bulgularını ÜÇ sınıfa ayırır ve her sınıfa farklı davranır — değer bu ayrımda:

- **safe-fix:** mekanik/uygulaması tek-anlamlı düzeltmeyi kendisi yapar;
- **insana eskalasyon:** davranış/sözleşme KARARI gerektiren bulguyu düzeltmez, insana yükseltir;
- **bilinçli no-op:** önerinin uygulanmamasını kayıtla geçer.

**Kanonik örnek (08-12 L8, wf-deneme koşumu, no-mistakes v1.48.0):** tek koşumda 4 review bulgusu → pyc/test kalıntıları **auto-fix** · `carpim([])` boş-liste sözleşmesi **İNSANA ESKALE** (dönüş değeri bir davranış kararıdır; hüküm koşumda verildi: `→ None`) · `math.prod` önerisi **bilinçli no-op**. Aynı koşumda hem safe-fix hem eskalasyon sınıfının görülmesi Windows'ta iki koşum gerektirmişti — platform-bağımsız desen doğrulandı. Bu ayrım, Jarvis'in Katman-1/Katman-2 sınırının (mekanik iş Jarvis'te, davranış kararı Salih'te — m.16 ailesi) araç-düzeyi karşılığıdır.

## SOP

1. Değişikliği yap; `/no-mistakes` tetikle (ya da skill tetiği: "gate/ship/validate/push safely").
2. CI'sı olmayan depoda `--skip ci` ver (aksi hâlde ci adımı sonlanmaz — Gotcha 1).
3. Eskalasyon çıkarsa: çöp/deneme depoda Katman-2 hükmü koşumda verilebilir; gerçek projede hüküm Salih'e gider (08-12 kaydı: "gerçek projede Salih'e giderdi").
4. Push hedefine yalnız pipeline yeşilken; m.9 push şartı (Salih beyanı) aracın ÜSTÜNDE durur, araç onu kaldırmaz.

## Gotchas

1. **ci adımı CI'sız depoda sonlanmıyor** — sonsuz poll; 08-12'de fiilen yaşandı, koşum abort edildi → `--skip ci` standart önlem.
2. **Sürüm farkı izlemede:** Win v1.41.2 ↔ Mac v1.48.0 — davranış farkı gözlenmedi, ama gözlem sürüyor (08-12 aday kaydı).
3. **Kurulum usulü:** pipe-to-shell yok — betik indirilip İNCELENEREK koşulur (08-12 usul kararı).
4. **Paralel-oturum çakışması (vaka 08-21 s13):** no-mistakes koşumu working tree'de DAL DEĞİŞTİRİR ve merge yürütür (`tarama-yontemleri` vakası: UU çakışma + staged dosyalar); ikinci oturum o sırada commit atarsa merge'i yabancı adına tamamlar ya da yanlış dala yazar → ikinci oturum git-yazma işlemlerini ağaç main'e dönüp temizlenene dek BEKLETİR, commit'i pathspec'le atar ([[paralel-oturum-protokolu]] kural ailesi).

## Süpersede zinciri

— (ilk sürüm; çelişen eski iddia yok.)

## İlgili

[[paralel-oturum-protokolu]] — Gotcha 4'ün kural tabanı · [[olcum-banki]] — koşum dörtlüsünün bir kaynağı `~/.no-mistakes/` durumu (`tools/olcum-dortlu.py`) · [[gnhf]] · [[treehouse]] — L8 araç üçlüsünün diğer ikisi (sayfaları kuyrukta).

**Bağlantılar:** · [[dil-secimi]] (karşı-link 08-26)
