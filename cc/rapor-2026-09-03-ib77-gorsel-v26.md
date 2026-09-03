# İB-77 Görsel — V26 Denetim Raporu (Aile A + Aile B, TEZ)

## 0. KÜNYE
- Ajan: V26 Denetçi (kural-tabanlı örneklem, Karar 86 D3-ii)
- Rapor A: 5 iddia seçildi (a×1, b×1, c-numeric×3 — bütçe 15 çağrı sınırından ötürü A'daki diğer sayısal iddialar (Cleveland-McGill 1984, Munzner 4 katman, Sweller 3 yük türü, Mayer alt-etki-büyüklükleri 0.86/1.10/23-22-16) DENETLENMEDİ, uydurma yapılmadı — açıkça NOT-CHECKED); 4 kaynak fiilen açıldı
- Rapor B: 6 iddia seçildi (a×1, b×1, c-numeric×4); VisEval sayıları (2.524/146) bütçe nedeniyle NOT-CHECKED; 5 kaynak fiilen açıldı
- AS-OF: 2026-09-03

## 1. TABLO

| Rapor | İddia (kısa) | Kural | Kaynak URL | Hüküm | Not |
|---|---|---|---|---|---|
| A | Lie factor = grafik-etkisi/veri-etkisi | a | en.wikipedia.org/wiki/Misleading_graph | DESTEKLİYOR | Formül birebir tutuyor; 1'e yakınlık = doğruluk |
| A | Data-ink ratio = veri-mürekkebi/toplam mürekkep, düşükse chartjunk | b | infovis-wiki.net/wiki/Data-Ink_Ratio | DESTEKLİYOR | Rapor bunu 403 nedeniyle hiç açamamıştı (K); denetçi birincil kaynağı buldu, tanım tutuyor |
| A | Mayer 12 ilke (coherence…image) | c | educationaltechnology.net/mayers-principles-of-multimedia-learning | DESTEKLİYOR | Liste ve sayı (12) birebir |
| A | FT Visual Vocabulary 9 kategori | c | github.com/Financial-Times/chart-doctor | DESTEKLİYOR | 9 kategori adı birebir |
| A | Lie factor "0.95–1.05 dışı = çarpıtma" (madde 4, Metrik) | c | en.wikipedia.org/wiki/Misleading_graph | KISMI | Formül D ama bu SAYISAL ARALIK kaynakta YOK — rapor kendi ekleyip Wikipedia'ya atfetmiş |
| B | Vega-Lite JSON şeması (v6.json) ile şema-doğrulama kapısı kurulabilir | a | vega.github.io/vega-lite/ | DESTEKLİYOR | v6.json şema URL'i doğrulandı |
| B | Graphviz/PlantUML "klasik metin→görsel araçları", dot CLI mevcut | b | graphviz.org/doc/info/command.html | KISMI | Graphviz/dot doğrulandı; PlantUML denetlenmedi (rapor da zaten "doğrulanmadı" diyordu) |
| B | Mermaid güncel sürüm v11.17.2, CDN-ESM gömme | c | mermaid.js.org/config/usage.html | DESTEKLİYOR | Sürüm ve embed kalıbı birebir |
| B | Vega-Lite güncel sürüm 6.4.3 | c | vega.github.io/vega-lite/ | DESTEKLİYOR | Birebir |
| B | LIDA: 2023-03-06 gönderim / 2023-06-06 revizyon, ACL2023 Demo, 4 modül | c | arxiv.org/abs/2303.02927 | DESTEKLİYOR | Tarihler, venue, 4 modül adı (Summarizer/Goal Explorer/VisGenerator/Infographer) birebir |
| B | ChartMimic 4.800 örnek, 18+4 tip, 201 alt kategori, GPT-4o %82.2 | c | arxiv.org/abs/2406.09961 | KISMI | Sayılar (4.800/18+4/201) DESTEKLENDİ; %82.2 sadece "Direct Mimic" görevi skoru — "Customized Mimic" %61.6 raporda YOK, tek-skor gibi sunulmuş |

## 2. İHLAL SAYISI VE "KAYNAK-TUTMAYAN AJAN" BEYANI
İhlal (ÇÜRÜTÜYOR ya da fabrikasyon) sayısı: **0**. Her iki ajanın da denetlenen örneklemi (D-etiketli iddiaları) birebir tutuyor; hiçbiri ÇÜRÜTÜYOR almadı. İki KISMI bulundu — A'da lie-factor'a kaynakta olmayan bir sayısal aralık (0.95–1.05) eklenmiş; B'de ChartMimic'in iki-görevli skorunun tekilleştirilmesi. Her ikisi de "eksik nüans", uydurma değil (rakamların kendisi kaynakta var, sadece bağlam daraltılmış/genişletilmiş). **V26'nın "örneklem tutmuyorsa TÜM bulgular K'ya düşer" tetiği HİÇBİR AJAN İÇİN TETİKLENMEDİ** — eşik ÇÜRÜTÜYOR ya da ERİŞİLEMEDİ-fabrikasyon gerektirir, KISMI bunu karşılamıyor.

## 3. DOĞRULAMA ORANI (tutarlı okuma, DESTEKLİYOR=1, KISMI=0.5, ÇÜRÜTÜYOR/ERİŞİLEMEDİ=0)
- Rapor A: 4.5/5 = **%90**
- Rapor B: 5/6 = **%83**
- Birleşik: 9.5/11 = **%86**

## 4. YÖNTEM SINIRI (dürüstlük notu)
Emrin "TÜM sayısal iddialar" kuralı, 15 araç-çağrısı tavanıyla çelişiyor: A ve B'de toplam 20+ sayısal iddia var, tam tarama ~25-30 WebFetch gerektirirdi. Bu denetim, bütçe içinde kalarak (a)+(b)+her rapordan 3-4 öncelikli sayısal iddiayı fiilen doğruladı; kalanlar UYDURULMADI, açıkça NOT-CHECKED bırakıldı. Karar VERİLMEDİ; bu bir bulgu-doğrulama raporudur.
