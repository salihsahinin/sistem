---
name: atlas-kosum
description: Bir araştırma sorusunu dik alan-ailelerine bölüp paralel araştırma ajanları
  (Atlas) koşturur — çift-atlas kuralıyla (m.40b): tez şeridi savunur, antitez şeridi tezin
  lojiksel TERSİNİ (¬) savunur; V26 örneklem-denetimi + sentezle etiketli (D/K/X + URL)
  rapor üretir. Kullan: "araştır", "atlas koştur", "dış tarama", "saha örneği bul",
  "dışarıda çözülmüş mü" dendiğinde ya da m.40b gereği yeni mekanizma/araç kararından önce.
  KULLANMA: bilinen-cevap basit soru, dosya-içi arama, terim açıklama — direkt cevapla.
argument-hint: "<araştırma sorusu>"
metadata: { owner: carvis, version: "0.1.0-deneysel-m29" }
---

# atlas-kosum — m.40b koşum talimatı

Kanon zinciri: m.40b (araştırma-önce + çift-atlas + antitez=¬ şerhi 07-19) · V26 (örneklem-denetim) · m.39 (rakam damgası) · m.41 (yüzey yetkisi) · m.35 (ölçüm-öncelik).

## Adımlar

1. **Gerek kontrolü.** Cevap zaten biliniyor/dosyada mı? → koşturma, direkt söyle. Karar-öncesi kullanımsa sıra: TARAMA → sunum (m.40b; tersi ihlal).
2. **Alan-ailesi ayrıştırması.** Soruyu 2-5 DİK aileye böl (örtüşme israf, boşluk kör nokta). Her aileye tek cümlelik arama-hedefi yaz.
3. **Çift-atlas kur.** Her aile için iki şerit: **tez** (iddiayı destekleyen kanıt arar) ∧ **antitez** (iddianın DEĞİLİNİ savunacak kanıt arar — ¬T; "alternatif bakış" DEĞİL, lojiksel ters). Şeritler birbirinin çıktısını görmez (bağımsızlık şartı).
4. **Paralel koştur.** Aile×şerit başına bir ajan; ajan promptuna yaz: URL zorunlu · rakamlar kaynaklı, kestirimse `[?]` · uydurma YASAK, "bulunamadı" meşru sonuç · erişim engeli (403/paywall) açıkça bayraklanır.
5. **V26 örneklem-denetimi.** Sentezden ÖNCE: ajan başına ≥1 rastgele kaynak iddiası seç, kaynağa inip doğrula. Tutmuyorsa o ajanın TÜM bulguları K'ya düşer ve nota geçer.
6. **Etiketle + sentezle.** Her bulgu: **D** (birincil kaynaktan doğrulandı) / **K** (arama-özeti, teyide muhtaç) / **X** (doğrulanamadı/çelişkili) + URL. Sentezde tez-antitez KESİŞİMİ ayrı yazılır (en sağlam bilgi); çatışma varsa saklanmaz, "çelişkili" diye sunulur.
7. **Rapor üret.** Şablon: `references/rapor-sablonu.md`. Yüzey kuralı (m.41): ana-sıradaysan raporu `raporlar/`e Carvis normal akışla yazar; **yan-oturumdaysan** rapor `claude/`-önekli branch'e gider, kanon dosyalarına DOKUNULMAZ, cevaplanmamış sorular rapora gömülür (karar biriktirme yok).

## Gotchas

- Antitez şeridini "denge olsun" diye yumuşatma — ¬T'yi gerçekten savunan ajan kur; süs-antitez 07-19 şerhine aykırı ve DARALTILDI-sinyali üretemez.
- Aile sayısını soruya göre seç; her koşuma 5 aile açmak israf (m.25 ölçek-optimizasyonu). Tek-aileli küçük soruda çift-şerit yine ZORUNLU (kural aile sayısından bağımsız).
- Örneklem-denetimini atlama — 07-17 serisinde WebFetch 403 vakaları "D sanılan K" üretmişti; denetimsiz sentez etiket enflasyonu yapar.
- Skill kaydetme/commit yapmaz; commit vardiya akışının işidir (yan-etki freni).
