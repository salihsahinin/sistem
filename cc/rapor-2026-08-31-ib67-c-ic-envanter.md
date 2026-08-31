# İB-67 C1 ailesi — İç envanter (paper-adayı ayağı): 5 aday çalışan-kanıt çıkarımı

**AS-OF 2026-08-31 · aile C1 · model sonnet · dizin: /Users/HasanSalihSahin/jarvis · yalnız repo-içi okuma (Read/Grep/Bash), web YOK · tarama YAPILMADI, yalnız var olan rapor/kod pointer'ları okundu**

Bu rapor tarama/hüküm üretmez; her aday için (a) mekanizma, (b) repo-pointer, (c) rapordan birebir alıntılanmış ölçüm, (d) yenilik-iddiası formülasyonu verir.

---

## ① İB-53 — dosya:satır + layout birleşik IR şeması

**(a) Mekanizma:** Kod referansları (`dosya:satır`) ile diyagram/layout bilgisini TEK bir ara-temsil (IR) şemasında birleştirmek; md-yerli satır-adresli IR (mdast/unist `Point` + Pandoc `sourcepos` tabanlı, layout alanı eklenmiş).

**(b) Repo-pointer:** `raporlar/2026-08-29-ib53-atlas.md` (Aile C bölümü), `raporlar/2026-08-29-ib53-kapsama-haritasi.md` §1-§4.

**(c) Ölçüm (birebir alıntı):**
> "dosya:satır + layout" BİRLEŞİK şeması emsalsiz alan — hakemlikten SAĞLAM çıkan tek negatif" (Aile C hakem dağılımı: 1S/6D/0Dü)
> "en yakın tabanlar SourcetrailDB/SARIF (satır+graf, layout'suz) + Sprotty `trace` deseni (görsel öğe → kaynak geri-bağı)"
> Kapsama haritası sayıları: dosya_pointer referansı **9.793** (çözümlü 8.487 · kırık **1.306**) · backtick yol pointer'ı satırsız **4.999**, satırlı (`yol:123`) **380**.

**(d) Yenilik-iddiası (formülasyon, tarama yapılmadı):** "Kod-satırı referansı ile diyagram layout geometrisini aynı IR şemasında (tek kayıt = hem kaynak konumu hem görsel konum) taşıyan, md-yerli ve araç-bağımsız bir temsil önerilmemiştir; mevcut emsaller (SourcetrailDB, SARIF, Sprotty) ikisinden yalnız birini taşır."

---

## ② İB-49 — D2-dili LLM üretim/okuma mini-eval

**(a) Mekanizma:** LLM'in graf verisini D2 diline (insan-okunur, görsel) üretme/okuma başarımı ile SQL-motoruna devretme (kenar listesi → SQL sorgusu) başarımının A/B ölçümü; harness `tools/d2-eval.py` (LLM çağırmaz, stdlib + d2 CLI).

**(b) Repo-pointer:** `raporlar/2026-08-29-ib49-d2-mini-eval.md` §1; harness `tools/d2-eval.py`; kütük `veri/d2-eval.jsonl`; gold `veri/gorunum/v_d2_eval.csv`.

**(c) Ölçüm (birebir alıntı):**
> "(a) üretim | kenar kümesi (kaynak, hedef, tip) ↔ model | 5/5 birebir: 58/58, eksik 0, fazla 0, P = R = 1,0"
> "(b1) okuma, kenar listesi | 5 yapısal soru × 5 işçi | 24/25 = 0,96 — tek hata: o5, "tablo:kayit'e giren kenar" 3 ↔ 4 (sayım hatası)"
> "(b2) LLM SQL yazar / motor yürütür | 5 soru × 5 işçi | 25/25 = 1,0"
> "(c) hakem A/B | LLM girdi verimliliği (h3) | LLM kenar-satırı D2 (2,4 KB ↔ 13,0 KB = 5,5×; yapısal soruları aynı bilgiyle taşıyor)"

**(d) Yenilik-iddiası (formülasyon):** "Diyagram-dili (D2) üretiminde LLM'in kural-tabanlı dönüşümle deterministik-doğru (P=R=1,0, 5/5 byte-özdeş) çıktı ürettiği, ama yapısal-sorgu OKUMA görevinde metin-üzerinden-sayma (%96) yerine SQL-motoruna devretmenin (%100) hatasız olduğu; ayrıca insan-okunurluk ile LLM-girdi-verimliliği arasında ölçülü bir 5,5× biçim-ayrımı (script-D2 ↔ ince kenar listesi) gösterilmiştir — literatürde D2 için benchmark yok, bu Jarvis'e özgü ilk ölçümdür."

---

## ⑤ İB-57 — ask_oran proxy'siyle iş-sınıfı → yüzey türetme

**(a) Mekanizma:** Seans hareket kütüğünden (`hareket` silver) deterministik bir proxy metrik (`ask_oran` = skill çağrısını izleyen 12 adımda `AskUserQuestion` sayısı / çağrı) türetip, iş sınıflarını üç sınıfa (ANA-SIRA / HEADLESS-ADAY / BELİRSİZ) otomatik etiketleyen kural + araç.

**(b) Repo-pointer:** `raporlar/2026-08-29-ib57-headless-esleme-taslak.md` §0-§3; araç `tools/headless-esleme.py`; veri kaynağı silver `hareket` (62 oturum, 4.206 çağrı) + `amb_olgu_kosum`.

**(c) Ölçüm (birebir alıntı):**
> "Sayım: ANA-SIRA 3 · BELİRSİZ 11 · HEADLESS-ADAY 6 · ZATEN-HEADLESS 27 (toplam 47 sınıf)."
> Örnek satır: "gorev-emri-derleme | 6 | 6 | 0.0 | 10.0 | 0.3 | HEADLESS-ADAY"
> Ajan sınıfı örneği: "Atlas ANTİTEZ ajanı [atlas] | 92 | 531.0 | 2839759 | ZATEN-HEADLESS: Agent alt-koşum"

**(d) Yenilik-iddiası (formülasyon):** "Bir çok-ajanlı geliştirme ortamında hangi iş sınıfının etkileşimsiz (headless) koşabileceğini, ajan çağrılarının içerdiği kullanıcı-soru oranından (ask_oran) türeten tamamen deterministik, LLM'siz bir sınıflandırma kuralı — insan kararı gerekliliğini dolaylı gözlemden (AskUserQuestion sıklığı) çıkarsayan bir proxy metrik önerisi."

---

## ⑦ İB-51 — kural-birimi envanteri + IFScale ≤100 çapası

**(a) Mekanizma:** Sistemdeki tüm yazılı kuralları (CLAUDE.md, skill, kanon, wiki) "taşıyıcı sınıfı" (ne zaman bağlama girer: T0 her-oturum / T1 ritüel / T2 çağrı-skill / T3 kanon-pointer / T4 wiki) ve "görev sınıfı" (anahtar-kelime kümeleme) eksenlerinde deterministik script ile sayıp, dış literatürdeki IFScale talimat-uyum eğrisiyle (500 talimatta %68 uyum) yerel bir ≤100-birim eşiğini çapalamak.

**(b) Repo-pointer:** `raporlar/2026-08-29-ib51-kural-envanteri.md` §1-§3; atlas doğrulama `raporlar/2026-08-29-ib51-atlas-kural-yukleme.md` (Aile B, IFScale satırı); üretici `tools/kural-envanter.py`; gold `veri/gorunum/v_kural_envanter.csv`.

**(c) Ölçüm (birebir alıntı):**
> "T0+T1 = 71 birim / 21,8 KB (kural-sayaci bugün yalnız CLAUDE.md'yi sayıyor: 19 → ritüel skill'ler eklenince 71). KB-50 (a) eşiği ≤100: ortalama 2 çağrı-skill tetiklenince (71 + 2×14,5 = 100) eşik doludur"
> "Toplam | 49 (dosya) | 1.017 (kural birimi) | 339.142 (byte)"
> Atlas-B: "IFScale: en iyi model 500 talimatta %68 [D]; kural dosyalarının token maliyetine ampirik benchmark YOK"

**(d) Yenilik-iddiası (formülasyon):** "Bir ajan sisteminde yazılı kural bütçesini (kaç 'kural birimi' bir oturumda fiilen bağlama girer) deterministik olarak ölçüp, dış talimat-uyum literatüründeki (IFScale) genel eğriye karşı yerel bir eşik (≤100 birim) kalibre eden ilk ölçüm; kuralın NEREDE (taşıyıcı) ve HANGİ GÖREV SINIFINDA yaşadığının çapraz-tablosu."

---

## ⑧ İB-66 — Gözlemlenebilir nested-loop boşluğu

**(a) Mekanizma:** 12 gözlemlenebilirlik/ajan-orkestrasyon aracını (LangGraph Studio, AgentOps, AutoGen Studio, CrewAI, OpenAI Agents SDK, Temporal, Claude Agent SDK, Devin, Manus, Langfuse, Arize Phoenix, Braintrust) taramadan-önce-sabitlenmiş 5 kriterle (K1 canlılık, K2 konuşma-granülü, K3 iç-içe seviye ayrımı, K4 müdahale, K5 ürün-olgunluğu) çarpraz matrise oturtup, hiçbirinin dört kriteri (K1∧K2∧K3∧K4) birlikte karşılamadığını göstermek.

**(b) Repo-pointer:** `raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md` §0-§2 (matris ve sütun sayımı).

**(c) Ölçüm (birebir alıntı — matris özeti + 0/12 hükmü):**
> Sütun sayımı: "K1 | 4 EVET | 2 KISMİ | 2 HAYIR | 4 [?] · K2 | 6 EVET | 2 KISMİ | 1 HAYIR | 3 [?] · K3 | 1 EVET | 6 KISMİ | 2 HAYIR | 3 [?] · K4 | 4 EVET | 0 KISMİ | 6 HAYIR | 2 [?] · K5 | 8 EVET | 2 KISMİ | 1 HAYIR | 1 [?]"
> "**K1∧K2∧K3∧K4 hepsi EVET olan araç: 0 / 12.**"
> Hüküm: "KISMİ. Beş kriteri BİRLİKTE karşılayan ürün YOK (0/12); kriterler ayrı ayrı VAR." — darboğaz K3: "12 araçta yalnız 1 net EVET (Devin: koordinatör + N managed Devin, her biri ayrı izole oturum)."
> Denetim şeffaflığı: "V26 örneklem sondajı 9 iddiadan 5'ini tam doğruladı (%55,6)... 6 ihlal listelendi"; hakem dağılımı "D 27 · K 11 · X 8."

**(d) Yenilik-iddiası (formülasyon):** "Çok-ajanlı LLM sistemlerinde iç-içe (nested) döngü yürütmesinin CANLI, konuşma-granülü, seviye-ayrımlı ve müdahale-edilebilir tek bir gözlem yüzeyinde birleşmediğini — pazardaki 12 aracın hiçbirinin dört kriteri birlikte karşılamadığını (0/12) — taramadan-önce-sabitlenmiş kriter matrisi + antitez/örneklem-denetimiyle gösteren ilk sistematik boşluk tespiti; ardından bu boşluğu kapatan sıfır-ek-token maliyetli, mevcut araç (`gnhf-izle.py`) üstüne inşa tasarım modeli."

---

## Özet tablo

| aday | mekanizma | repo-pointer | ölçüm | yenilik-iddiası |
|---|---|---|---|---|
| ① İB-53 | dosya:satır+layout birleşik IR şeması | raporlar/2026-08-29-ib53-atlas.md; -kapsama-haritasi.md | "emsalsiz alan — hakemden SAĞLAM tek negatif"; kırık pointer 1.306/9.793; satırlı pointer 380 | md-yerli, araç-bağımsız, kod-satırı+layout-geometri birleşik IR şeması yok |
| ② İB-49 | D2 üretim/okuma mini-eval, tools/d2-eval.py | raporlar/2026-08-29-ib49-d2-mini-eval.md | üretim 58/58 P=R=1,0; okuma kenar-listesi %96, SQL %100; token 5,5× (2,4KB↔13,0KB) | D2 için ilk benchmark; üretim-deterministik + okuma-SQL-devri + biçim-ayrımı ölçümü |
| ⑤ İB-57 | ask_oran proxy → yüzey sınıflama, tools/headless-esleme.py | raporlar/2026-08-29-ib57-headless-esleme-taslak.md | ANA-SIRA 3 · BELİRSİZ 11 · HEADLESS-ADAY 6 · ZATEN-HEADLESS 27 (47 sınıf) | AskUserQuestion sıklığından deterministik headless-uygunluk proxy'si |
| ⑦ İB-51 | kural-birimi envanteri + IFScale çapası, tools/kural-envanter.py | raporlar/2026-08-29-ib51-kural-envanteri.md; -atlas-kural-yukleme.md | T0+T1=71 birim/21,8KB; toplam 1.017 birim/339.142 B; IFScale %68@500 dış-referans | kural-bütçesi deterministik ölçüm + dış talimat-uyum eğrisine yerel eşik kalibrasyonu |
| ⑧ İB-66 | 12 araç × 5 kriter matris, nested-loop gözlemlenebilirlik | raporlar/2026-08-31-ib66-gozlemlenebilir-nested-loop-atlas.md | K1∧K2∧K3∧K4 hepsi EVET: 0/12; darboğaz K3 (1/12 net EVET); V26 doğrulama %55,6 | tarama-öncesi-sabit kriterli sistematik 0/12 boşluk tespiti + sıfır-ek-token tasarım modeli |
