---
name: halusinasyon-engelleyici
description: Halüsinasyona müsait görevin ÇIKTISINI doğrulama zinciriyle üretir (kaynak-topraklama + destek-kontrolü + bağımsız doğrulayıcı + çekimserlik ekonomisi); her iddia DESTEKLİ/DAYANAKSIZ/ÇELİŞİR etiketli, önce H(görev) derecesi hesaplanır (scripts/derece.py). Tetik; görev-emrinde `halusinasyon_derecesi ≥ eşik` (7 / pahalı-geri-alma 4) ya da çıktı-türü atıf/künye/DOI/URL/kaynakça (override), "halüsinasyon freniyle üret", "doğrulama zinciriyle yaz", olgusal/sayısal/atıf-yoğun rapor üretiminde. KULLANILMAZ; H<4 rutin işlerde, sohbette, kodun test/yürütme kapısı çıktıyı zaten doğruluyorsa, skill'i/formülü değiştirmek için.
argument-hint: "<görev + kaynaklar | --derece bayrakları>"
metadata: { owner: carvis, version: "1.0.0-deneysel-m29", kural: "core/halusinasyon-paketi.md" }
---

# halusinasyon-engelleyici — doğrulama-zinciri koşum talimatı (v1, 2026-08-15)

Kural kaynağı: `core/halusinasyon-paketi.md` (fren listesi F1-F10 + derece formülü + eşik/fizibilite) · derece: `scripts/derece.py` · kardeşler: skill-üretim şeması K2 (artefakt), tetiklenme şeması (çağrı). İlke: fren = KAPI (dış sinyal), prompt değil; üretici ≠ doğrulayıcı; DAYANAKSIZ ≠ YANLIŞ; sözel güven kapı değil.

## Adımlar
1. **Derece + fizibilite:** `python3 .claude/skills/halusinasyon-engelleyici/scripts/derece.py --v… [--pahali-geri-alma]` → H, eşik, ima edilen maliyet. H < eşik ∧ atıf-türü değil → skill'i kapat, kanon frenleriyle üret (bedel freni). Görev-tipi taban riski μ ≫ hedef α ise (açık-alan nadir olgu listesi, ham uzun metinden atıf üretimi): **sertifika vaat etme** — çıktı çekimserlik-etiketli üretilir ya da insan-onayı (Salih) kovasına düşer; zorunlu çekimserlik payı ≥ (μ−α)/(1−α) beyan edilir.
2. **Adım-0 öncül/cevaplanabilirlik:** soru cevaplanabilir mi, öncül doğru mu, eksik-belirtim var mı? Şüphe → önce bunu yaz (çekimserlik izni AÇIK: "bulunamadı"/[ARANAMADI]/"öncül şüpheli" meşru); akıl-yürütme modunda bu adım atlanmaz.
3. **Kaynak toplama (F2):** yapılandırılmış + provenanslı kaynak (kanon dosyası, resmî doküman, birincil URL, veri tablosu); ham/uzun metinde alıntı-doğrulama (>32K → hedef pasajı çıkar); kaynak yoksa "KAPALI-KİTAP" damgası (v7a) ve her iddia [?]/K adayı. Sayısal → hesap yürütücüye (script/hesap), asla zihinsel; dış referans/paket/URL/DOI → tekil fetch/registry (Hat-1 F5).
4. **Üretim (F8):** çıktı şeması **gerekçe/kanıt → cevap** sırasıyla; her atomik iddia numaralı + kaynak-pointer'lı (`[k1]` = kaynak cümlesi/satırı); atıf/künye ise her biri tekil doğrulanmadan yazılmaz; uzun çıktı parçalara bölünür (m.21). Sözel güven ("eminim") yazılmaz — yalnız etiket.
5. **Bağımsız doğrulama (F1+F3+F4):** ayrı tur/alt-ajan doğrulayıcıya YALNIZ iddia listesi ver (CoVe-Factored; kaynak/gerekçe verme); her iddiaya etiket: **DESTEKLİ** (kaynak cümlesi gösterildi) / **DAYANAKSIZ** (kaynakta yok — yanlış değil) / **ÇELİŞİR** (kaynakla ya da dünyayla) / **LOJİK-tutarsız** (gerekçe↔cevap). Örneklem konum-ağırlıklı (F7): son üçlük + TÜM sayısal iddialar + tüm atıflar. Sonlu-cevaplı kritik iddialarda N=3 örnek uyuşması (F4; tutarlı-yanılgıyı yakalamaz — not düşülür). Paralellik-uygunluk: doğrulayıcı SERİ ve tek (bağımsız-keşif değil, ortak-üretim değil — yargı); handoff kontratı sabit: girdi = numaralı iddia listesi, çıktı = iddia-id → etiket + kaynak-cümlesi; yürütme-yeri: ana bağlam + 1 doğrulayıcı tur/alt-ajan (fork = geçmişsiz, istenen budur).
6. **Teslim:** DAYANAKSIZ iddialar ya kaynaklanır ya çekimser bırakılır ya "doğrulanmadı" damgasıyla geçer — sessizce doğru sayılmaz; ÇELİŞİR/LOJİK-tutarsız çıkar ya da düzeltilir (düzeltmeyi üretici değil doğrulayıcı gerekçesiyle). Çıktı sonunda **ölçüm satırı**: n iddia · DESTEKLİ/DAYANAKSIZ/ÇELİŞİR sayıları (Wilson aralığı) · H · model+sürüm · runtime-modu · kohort damgası. Puanlama beyanı: IDK=0, yanlış=−t/(1−t).
7. **Kayıt:** `kuyruk/halusinasyon-kayit.md`'ye satır (tarih · görev · v-vektörü · H · tetik · yakalanan · n) — kalibrasyon ≥50 olayda. Skill kaydetme/commit yapmaz; commit vardiya akışının işidir (yan-etki freni). Karar almaz; sonuç Salih'e etiketli teslim edilir.

## Gotchas
- **"Kaynak verdim, bitti" tuzağı:** RAG altında baskın hata dayanaksız EKLEME; destek-kontrolü olmadan kaynak = süs.
- **Tekrar ≠ doğrulama:** aynı-model tekrarların %43'ü 10/10 yeniden üretilir; N-örnek yalnız sonlu-cevapta ve tutarlı-yanılgıyı yakalamaz.
- **Atıf ≠ doğruluk:** atıf recall %73,6 ↔ doğruluk %40,4 — atıf-destek denetimi ayrı adım.
- **Öz-düzeltme prompt'u** ("çıktını gözden geçir") akıl-yürütmeyi düşürür (GSM8K 95,5→89,0); doğrulama ayrı ajan/turdur.
- **Sertifika enflasyonu:** ölçüm satırı olmadan "doğrulandı" yazma; oranlar n + aralıkla; çıplak yüzde yasak.
- **Sabitleri kanıt sanma:** ağırlıklar/eşikler kanıtsız-tercih (deneysel m.29); Claude güncel kuşak + Türkçe kör; kayıt satırı yazılmadan koşum bitmez.
