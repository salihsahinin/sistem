---
name: atlas-kosum
description: Araştırma sorusunu dik alan-ailelerine bölüp paralel Atlas ajanları koşturur — m.40b v0.2 diyalektiği: çoklu-bağımsız tez → hedefli antitez (¬) → maskeli hakemlik; sağlamlık = adversarial-hayatta-kalma; D/K/X + URL etiketli rapor üretir. Kullan: "araştır", "atlas koştur", "dış tarama", "saha örneği bul", "dışarıda çözülmüş mü" dendiğinde ya da m.40b gereği yeni mekanizma/araç kararından önce. KULLANMA: bilinen-cevap basit soru, dosya-içi arama, terim açıklama — direkt cevapla. argument-hint: "<araştırma sorusu>"
metadata: { owner: carvis, version: "0.2.0-deneysel-m29" }
---

# atlas-kosum — m.40b v0.2 koşum talimatı

Kanon zinciri: m.40b v0.2 (multi-hop diyalektik, Salih imzası 07-21; kanıt `raporlar/2026-07-21-multihop-oneshot-literatur.md`) · V26 (örneklem-denetim) · m.39 (rakam damgası) · m.41 (yüzey yetkisi) · m.35 (ölçüm-öncelik).

## Adımlar

1. **Gerek kontrolü.** Cevap zaten biliniyor/dosyada mı? → koşturma, direkt söyle. Karar-öncesi kullanımsa sıra: TARAMA → sunum (m.40b; tersi ihlal).
2. **Alan-ailesi ayrıştırması.** Soruyu 2-5 DİK aileye böl (örtüşme israf, boşluk kör nokta). Her aileye tek cümlelik arama-hedefi yaz.
3. **Aşama 1 — TEZ koşumları.** Aile başına ≥1 tez ajanı, paralel ve BAĞIMSIZ (birbirinin çıktısını görmez; bağımsızlık şartı bu aşama İÇİNDE yaşar). Ajan promptuna yaz: URL zorunlu · rakamlar kaynaklı, kestirimse `[?]` · uydurma YASAK, "bulunamadı" meşru sonuç · erişim engeli (403/paywall) açıkça bayraklanır · **her iddia AS-OF damgalı (kaynağın tarihi ∨ çekim tarihi; Karar 68 anakronizm freni, 08-26 — damgasız iddiayı hakem DARALTIR/DÜŞÜRÜR; hazır-ürün sürümü hakem tarafından yeniden çekilir)**.
4. **Aşama 2 — hedefli ANTİTEZ (¬).** Tez raporları geldikten SONRA, tez-başına ayrı antitez ajanı kur: açık Devil's-Advocate rolü, tezin değilini (¬T) savunacak kanıt arar — "alternatif bakış" DEĞİL, lojiksel ters. **CoVe-Factored kuralı (kanon):** antitez ajanına tezin İDDİASINI ver, GEREKÇESİNİ/kanıt zincirini VERME (çıpalama freni). Aynı çıktı-disiplini (URL · `[?]` · bulunamadı meşru) burada da geçerli.
5. **V26 örneklem-denetimi (KURAL-TABANLI — Salih imzası 08-17, deterministik tasarım; eski hâli: rastgele seçim).** Hakemlikten ÖNCE, ajan başına SABİT kuralla seç: (a) çıktının SON ÜÇTE BİRİNDEN ≥1 kaynak iddiası + (b) çıktıdaki TÜM sayısal iddialar (rakam · yüzde · tarih · sayım) — rastgele yok, aynı çıktı → aynı sondaj noktaları. Kaynağa inip doğrula; tutmuyorsa o ajanın TÜM bulguları K'ya düşer ve nota geçer. Gerekçe: FActScore konum bulgusu (hata sona doğru artar; sayısal iddia en halüsinatif tür) — `core/halusinasyon-paketi.md` F7.
6. **Aşama 3 — HAKEMLİK (maskeli kıyas).** Tez↔antitez kıyası çift-başına AYRI değerlendirme; kimlik/sıra maskele (hangisi tez hangisi antitez etiketiyle değil, iddia+kanıt olarak kıyasla); hakem üretici koşumların devamı DEĞİLDİR. Aşamalar arası HAM KANIT taşınır, türetilmiş yargı taşınmaz. **Sağlamlık ölçütü = adversarial-hayatta-kalma:** bilgili antitezin çürütmeyi deneyip BAŞARAMADIĞI iddia = sağlam çekirdek; çürüyen iddia DARALTILDI/DÜŞTÜ olarak ayrı yazılır; çatışma saklanmaz, "çelişkili" diye sunulur.
7. **Etiketle + rapor üret.** Her bulgu: **D** (birincil kaynaktan doğrulandı) / **K** (arama-özeti, teyide muhtaç) / **X** (doğrulanamadı/çelişkili) + URL. Şablon: `references/rapor-sablonu.md` (sentez bölümünde "kesişim" yerine "hayatta-kalan çekirdek + düşen/daralan iddialar" yapısı). Yüzey kuralı (m.41): ana-sıradaysan rapor `raporlar/`e normal akışla; **yan-oturumdaysan** `claude/`-önekli branch'e, kanon dosyalarına DOKUNULMAZ, cevaplanmamış sorular rapora gömülür. Koşum-sonrası: hayatta-kalma oranı (kaç tez sağlam/daraldı/düştü) senaryo-defterine tek satır gözlem (m.40b v0.2 deneysel damgası).

## Opsiyon — kör-triangülasyon şeridi (Katman-1 kararları)

Katman-1 ağırlıklı kararlarda (m.31 sınıfı) isteğe bağlı EK şerit: tezleri GÖRMEYEN kör-antitez ajanı (v0.1 deseni). Bilinçli ×token bedeli (m.35); varsayılan DEĞİL, açılırsa raporda ayrı bölüm.

## Gotchas

- Antitez ajanına tez raporunun tamamını yapıştırma — yalnız İDDİA listesi geçer (CoVe-Factored; gerekçe sızarsa çıpalama freni boşalır ve koşum v0.1'den beter olur: bilgili ama çıpalı).
- Antitezi "denge olsun" diye yumuşatma — ¬T'yi gerçekten savunan açık Devil's-Advocate kur; süs-antitez 07-19 şerhine aykırı ve DARALTILDI-sinyali üretemez.
- Hakemliği tez/antitez ajanlarından birine yaptırma — üretici≠doğrulayıcı (dışsal-geribildirimsiz öz-düzeltme doğruluğu DÜŞÜRÜR; literatür kaydı raporda).
- Aile sayısını soruya göre seç; her koşuma 5 aile açmak israf (m.25). Tek-aileli küçük soruda üç aşama yine ZORUNLU (kural aile sayısından bağımsız).
- Örneklem-denetimini atlama — 07-17 serisinde WebFetch 403 vakaları "D sanılan K" üretmişti; denetimsiz hakemlik etiket enflasyonu yapar.
- Skill kaydetme/commit yapmaz; commit seans akışının işidir (yan-etki freni).
