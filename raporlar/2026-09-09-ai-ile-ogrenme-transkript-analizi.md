# "How I Use AI to Learn Things" — transkript analizi + Jarvis'e aktarım (2026-09-09)

*Kaynak: `~/Downloads/How I Use AI to Learn Things.md` (Obsidian clipping; video Eero Alvar, yayın 2026-08-14, https://www.youtube.com/watch?v=kzcI5F4tGiU; repo https://github.com/amosblomqvist/learn — repo AÇILMADI, iddialar yalnız transkriptten). Salih yan görevi 09-09: "transkripti oku, kabaca videoyu çeken kişi nasıl kullanıyormuş anlat, artılarını sisteme implement edelim". Masa-9 M11 (İB-73 format) Salih beklet notunun ilk girdisi. AS-OF 2026-09-09; rakamlar transkriptten (m.39).*

## 1. Kişi nasıl kullanıyor (kaba özet)

**Gerekçe (iki verimsizlik → iki ilke):**
1. *Bir kaynak çok öğrenciye öğretir* → hiçbir öğrencinin "anlayış sınırı"na (edge of understanding) oturmaz; bildiğini tekrar eder, anlayamayacağını anlatır. İlke 1: **optimize öğretim** = tam anlayış sınırında çalış.
2. *Bir öğrenci çok kaynaktan öğrenir* → notasyon/üslup/arayüz değiştirme maliyeti + **güven** maliyeti (beyin tanımadığı kaynağı "hedge"ler; aynı açıklama 3Blue1Brown'dan gelince daha iyi öğrenilir). İlke 2: **zihinsel kaynağın optimize tahsisi** = zorluk malzemede kalsın, lojistik (kaynak bulma, doğrulama, sıra, plan) sisteme insin. "Maximize struggle — ama malzemede."

Bire-bir modelin itirazı ("tek öğretmen = tek bakış açısı") şöyle cevaplanıyor: öğretmen = **arayüz**, kaynak değil; tüm kaynakları toplar, tek arayüzden verir. Güven zamanla değil, **doğrulama alt-ajanlarıyla mühendislik olarak** kurulur.

**Süreç (Pi Agent harness, kendi `.pi/` klasöründe skill + quiz eklentisi + MD-log eklentisi + 2 görsel alt-ajanı; Obsidian arayüz):**
| Faz | Ne yapıyor | Neden |
|---|---|---|
| **Probe (yokla)** | Quiz aracıyla dereceli çoktan-seçmeli sorular; geniş başlar, dersin bağlı olduğu HER bağımlılık ipliğinde anlayış sınırını **ikili-arama** ile bulur; öğrenci "bilmiyorum" diyebilir; yanına "yap" notu (düşünürken yazdığı serbest alan) bağlam olarak gider | ayrıntılı anlayış haritası; ısınma; baştan bağlam verilirse probe kısalır |
| **Plan** | Yolu baştan sona akıl yürütür; doğrulama/olgu-kontrol alt-ajanlarını burada ateşler; planı **Mermaid DAG** olarak sunar | asıl neden: modeli her şeyi AKIL YÜRÜTMEYE zorlamak ("wing it" edemesin); ikinci: öğrenci neyin geleceğini görür |
| **Teach (öğret)** | DAG üzerinde **tek akıl-yürütme adımı** ilerler (acele yok — ChatGPT'nin "heyecanla hepsini anlatma" hatasına karşı); her adım sonunda küçük quiz; SVG görselleri alt-ajan üretir, **kendi ürettiği görseli açıp doğrular**; her şey MD-log ile Obsidian'a akar (LaTeX + kalıcı ders artefaktı) | (i) kendini "anladım" diye kandırmaya karşı test, (ii) sistemin kalibre kalması, (iii) uygulama = bilginin kilitlenmesi |
| **Close** | En önemli etken: öğretim ÜSLUBU — (a) öğrenme yayı (mevcut → hedef anlayış yolu), (b) yol üstündeki her adımın açıklaması | süreç değil, üslup belirleyici |

Yan notlar: model zekâsı öğretimde "gerçekten önemli" (Kimi K2 kullanmış; ölçüm yok); LLM-üslubunu düzeltmemiş ("çok talimatla boğmak istemiyorum"); demo konusu diferansiyel formlar → Maxwell.

## 2. Jarvis'te ne var, ne yok (çapraz okuma)

| Videodaki öğe | Jarvis'te karşılığı | Durum |
|---|---|---|
| Probe: dereceli MCQ + ikili-arama | hafıza kuralı "yeni konuda önce terim tabanını yokla" (08-17) — gayri-resmî, soru formatı yok | **EKSİK** (sistematik değil) |
| Plan: DAG önce, doğrulama alt-ajanı | hafıza kuralı "görsel metinden önce, metin görsele atıflı" (09-08) · `halusinasyon-engelleyici` (H ≥ eşik) | KISMİ (DAG zorunlu değil; doğrulama tetiği ders-akışına bağlı değil) |
| Teach: tek akıl-adımı + adım-quiz'i | "küçük partisyon" anlatım (SHAP/kümeleme serileri) · `sinav-grill` YALNIZ Salih tetiğiyle, ders SONUNDA | KISMİ (adım-başı soru yok; grill ders-içi değil) |
| Görsel alt-ajanı kendi çıktısını doğrular | `mcp__visualize` tek tek; görselleştir skill'i karantinada (M10) | KISMİ (doğrulama adımı yok) |
| MD-log / kalıcı ders artefaktı | `ogrenme/<kurs>/dersler/*.md` (MIT 6.006/6.042J), VS Code yüzeyi (Karar 80) | VAR |
| "yap" notu (öğrencinin düşünme alanı) | yok | EKSİK (ucuz: ders md'sinde `## Salih notu` bloğu) |
| Güven = doğrulama mühendisliği | m.39/m.40b/Karar 68 (her rakam kaynaklı, AS-OF) | VAR |
| Zorluk malzemede, lojistik sistemde | CLAUDE.md §0 "teslim Salih'in anlaması için" | İLKE VAR, ders-akışında operasyonel değil |

## 3. Artılar → uygulama (Karar 88 M5 gereği DENEME SKILL, hazineye girmez)

**`kuyruk/skill-deneme/ogren/SKILL.md`** — dört fazlı deterministik ders akışı: PROBE (≤12 soru, 4 seçenek + "bilmiyorum", iplik başına ikili-arama, Salih ön-bağlam verirse atlanır) → PLAN (DAG görseli mcp__visualize ile METİNDEN ÖNCE + düğüm listesi; olgusal/sayısal iddia varsa halusinasyon-engelleyici) → TEACH (düğüm başına: 1 akıl-adımı + görsele atıflı metin + 1 soru; doğru cevap gelmeden sonraki düğüme geçilmez) → CLOSE (ders kaydı `ogrenme/<konu>/dersler/YYYY-MM-DD-<konu>.md` şemalı; `sinav-grill` tetiği ÖNERİLİR, koşulmaz — m.33/sinav-grill kuralı). Hafıza kurallarıyla uyum: benzetme yok, doğrudan anlatım, görsel atıflı.

**Bilinçli DIŞARIDA bırakılanlar:** görsel alt-ajanının kendi çıktısını "bakarak" doğrulaması (mcp__visualize çıktısı dosya değil; ayrı araştırma) · Obsidian entegrasyonu (Karar 80: VS Code) · model seçimi iddiası (ölçümsüz).

**skill-kapisi hızlı geçiş (K0-K3, tam koşum K4 öncesi Salih tetiğiyle):** K0 GEREK: ders serileri 09-03/09-08'de 3+ kez aynı akış elle kuruldu (m.43 N=3 ↔ görev birimi) → aday · K1 DEĞER: Z2 (Salih emri "implement edelim") · K2: iddialar bu raporda kaynaklı, sayısal iddia yok · K3 TÜR: T-R ritüel (yan etki: yalnız `ogrenme/` altına md yazar, commit yapmaz). **K4 (Salih):** ≥1 canlı ders koşumu + "kabul" → hazine.

## 4. Salih'e (karar değil, bilgi)
- Bu rapor M11 "AI ile öğrenme başlıkları" araştırmasının 1. girdisi; İB-73 format hükmü Salih'te kalıyor.
- İlk canlı koşum önerisi: bir sonraki öğrenme seansında "kuyruk/skill-deneme/ogren/SKILL.md ile <konu>" de; ders kaydı `ogrenme/` altına düşer, yüzey VS Code.
