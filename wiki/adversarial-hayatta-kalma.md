# adversarial-hayatta-kalma

**Üst blok:** Bir iddianın sağlamlık ölçütü: bilgili bir karşı-tarafın (¬T savunan antitez) onu çürütmeyi **deneyip** başaramaması. "Kör kesişim = en sağlam" dilinin yerini aldı (m.40b v0.2). · Durum: **güncel** · Son teyit: 2026-07-22 (E5 dahil 5/5 eval koşumu) · Kaynaklar: tüzük m.40b v0.2 (Salih imzası 07-21) · `raporlar/2026-07/2026-07-21-multihop-oneshot-literatur.md` · `.claude/skills/atlas-kosum/SKILL.md` v0.2 · Güven: orta-yüksek (literatür + kendi eval'imiz; canlı koşum verisi henüz yok — ilk koşumda oran deftere düşer).

**Çekirdek:** Bir bulguyu "sağlam" yapan şey kaç kaynağın aynı şeyi söylemesi değil, hedefli bir çürütme girişiminden sağ çıkmasıdır. İki bağımsız tarama aynı yanlışı tekrarlayabilir (aynı ön-eğitim → korelasyonlu hata); ama iddiaya bilerek saldıran ve başarısız olan bir antitez, iddianın gerçek dayanağını test etmiş olur. Çürüyen iddia çöpe gitmez: **daraltıldı** (yalnız şu koşulda doğru) ya da `DÜŞTÜ` olarak ayrı raporlanır; çatışma saklanmaz, "çelişkili" diye sunulur. **Kanonik örnek:** "Kaynak-sayaçlı bütçe kesmesi üretimde en yaygın desendir" iddiasına antitez üç hattan saldırır — daha yaygın alternatif desen kanıtı, "en yaygın"ı ölçen verinin hiç olmadığı hattı, terk-edilme vakaları. Antitez üç hatta da güçlü kanıt bulamazsa iddia sağlam çekirdeğe girer; yalnız "ölçen veri yok" hattı tutarsa iddia "yaygın kullanılan desenlerden biri" diye **daraltılır**.

**SOP (koşumda uygulama):** (1) Tez raporlarından yalnız **iddia** listesini çıkar (gerekçe verilmez — CoVe-Factored, çıpalama freni). (2) İddia-başına açık Devil's-Advocate antitez ajanı kur: görev ¬T'yi savunmak, "dengeli bakış" değil. (3) V26 örneklem-denetimi: hakemlikten önce ajan-başına ≥1 kaynak iddiasına inip doğrula. (4) Maskeli hakemlik: kimlik/sıra etiketi olmadan iddia+kanıt kıyası; hakem üretici koşumların devamı değildir. (5) Raporu üç kovaya ayır: sağlam çekirdek / **daraltıldı** / `DÜŞTÜ` (+ çelişkili). (6) Hayatta-kalma oranını (kaç tez sağlam/daraldı/düştü) senaryo-defterine tek satır yaz.

**Gotchas:**
- Süs-antitez: "alternatif bakış" yumuşaklığında kurulan antitez DARALTILDI-sinyali üretemez — ölçüt boşalır (07-19 şerhi).
- Gerekçe sızıntısı: antiteze tezin kanıt zinciri verilirse çıpalanır — "bilgili ama çıpalı" koşum v0.1'den beter (gotcha, SKILL v0.2).
- Hakem etiketi bilirse ölçtüğün şey kanıt kalitesi değil rol önyargısı olur (E5 eval'i bu yüzden var).
- Denetimsiz hakemlik etiket enflasyonu yapar: 07-17 serisinde WebFetch 403'leri "D sanılan K" üretmişti — V26 atlanmaz.

**Süpersede zinciri:** "kör kesişim = en sağlam" (v0.1 dili, 07-17) → yerini aldı: [2026-07-21, m.40b v0.2 — sağlamlık = adversarial-hayatta-kalma; kör-şerit Katman-1 opsiyonuna indi].

**Bağlantılar:** [[token-x-zaman]] (antitez şeridinin bilinçli ×token bedeli) · [[pointer-sistemi]] (ham kanıt taşınır, türetilmiş yargı taşınmaz — m.20 ailesi) · aday: [[rol-katmanlari]] (m.44; üretici≠doğrulayıcı ayrımının örgütsel hali). · [[ai2ai-rapor-formati]] (karşı-link 08-22) · [[gorsel-artefakt-dogrulama]] (karşı-link 08-22) · [[stokastik-dusunce]] (karşı-link 08-22) · [[uc-register]] (karşı-link 08-22) · [[anakronizm-freni]] (karşı-link 08-26)
