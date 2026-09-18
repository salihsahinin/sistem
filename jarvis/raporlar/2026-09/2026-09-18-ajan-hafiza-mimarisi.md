# Kalıcı ajanların gelişen hafıza mimarisi — Atlas koşumu teslimi (2026-09-18, zincir 2/2, Karar 102)

*Soru: kalıcı ajanın (kendi dizini, kanonu, oturumu) hafızası nasıl gelişir; mevcut düzen (kapsül · pano · defter · kutu · çekirdek · bronz→silver→gold · harness memory · skill) literatürle nasıl eşleşir. Usul: 3 aile tez (harness/ürün · akademik · pratisyen) → 3 antitez → V26 (48 sondaj) → maskeli hakem (Opus 5 medium, 3 ek sondaj). Ham: `cc/rapor/2026-09/rapor-2026-09-18-hafiza-*.md` (8 dosya). AS-OF 2026-09-18; deneysel m.29.*

## 1. Mevcut düzenin eşlemesi (hakem §ii)
| Bileşen | Hüküm | Gerekçe | Etiket |
|---|---|---|---|
| Kapsül (FIFO 8 madde) | **değişmeli** | madde sayısı yerine ölçüm-tetikli satır/KB bütçesi; düşen her madde arşiv pointer'ı + tek satır kesilme bildirimi üretmeli (ölçülmüş arıza: indeks limitinde **sessiz** düşme; geri-çağırma bütçesinde 18 dersten 2'si görünüyor) | D |
| Karar defteri | **eklenmeli** | her kayda köken alanı: yazar kimliği + model sürümü + AS-OF (Karar 102 (3) ile aynı yönde) | D |
| Bronz→silver→gold | **eklenmeli** | sessiz-arıza sayacı: format hatası (küçük model %30, güçlü %18) ve dedup-önce-çelişki sırası arızası (%49) ölçülmüş | D |
| Harness memory (`~/.claude/projects/…/memory/`) | korunmalı + beyan | dizin depo dışında ve makine-yerel; açık-kaynak görünürlük ilkesiyle (jarvis md §2) gerilim, Salih imzası ister | D |
| Skill (koşullu bilgi) | korunmalı | Kun Chen + Claude Code belgesi | D |
| Fikir kutusu · çekirdek desenler | korunmalı | mekanizma destekli; "10 koşumda yeniden-oluşum" eşiği dışarıda yok, iç tercih | K |
| Pano | belirsiz | literatürde karşılığı yok → iç ölçüm | K |

## 2. Katmanlar ve disiplin (hakem §i, özet)
Dört-katman taksonomisi (çalışma · epizodik · semantik · prosedürel) evrensel değil; ürünler pratikte üç şey ayırıyor: **oturum bağlamı** (sıkıştırma/compaction), **kalıcı dizin** (MEMORY.md, satır/bayt tavanı; Claude Code 200 satır/25 KB, aşımda kısaltma değil hata), **dış depo** (Letta/Mem0/LangMem sınıfı, LLM'in kendi kararıyla ekle/güncelle/sil). Yazma tetiği ürünlerde otomatik; **insan onayı yalnız pratisyen tarafında** (Kun Chen: "nothing writes until I review"). Çok-ajan: ajan başına dizin izolasyonu varsayılan; paylaşılan hafıza yönetişimi tek makalede (Governed Shared Memory) ve arızaları ölçülü (yetki sızıntısı vakası; doğru yönetişimde sızıntı 0/80).

## 3. Kendini geliştiren hafıza ve frenler (hakem §iii)
- **İnsan onayının getirisi dünyada ölçülmemiş**: üç kaynakta boşluk doğrulandı; yedi üründen hiçbirinde zorunlu onay yok. Kanonun "kural yalnız Salih imzasıyla" kuralı literatürün ilerisinde, çürütülmemiş; iç ölçümün en değerli kalemi.
- **LLM-üretilen bağlam dosyaları**: Gloaguen ve ark. (arXiv 2602.11988, 2026-02): başarı düşüşü **%0,5 (SWE-bench Lite) / %2 (AGENTbench)**, maliyet **+%20**; zarar depo-özeti bölümlerine özgü. Tez raporundaki "%3" yanlış, düzeltildi.
- Hafıza sistemlerinde kazanım ölçülü ama pahalı: EvolveMem LoCoMo +%25,7 F1 (GPT-4o) / +%36,8 (GPT-5.1); inşa maliyeti 1,3M-7,04M token, MemoryOS gecikmesi kaynaklar arası çelişkili.
- AGENTS.md pratiği: 466 depoda %50'si ilk commit'ten sonra hiç güncellenmemiş; ortalama 142 satır (MSR 2026).

## 4. Hayatta kalma (36 iddia)
Sağlam 27 · daralan 7 · düşen 2 (A 6/4/2 · B 12/0/0 · C 9/3/0). Etiket: D 14 · K 20 · X 2. Düşenler: "context editing istemci taraflı" (Anthropic'in iki resmi sayfası çelişiyor) ve Mem0 "4 aşama". V26 denetimi antitez-B'nin bir hükmünü hatalı buldu (MemoryOS rakamları asıl kaynakta var), hakem geri yükseltti.

## 5. m.16 (hakem §vii)
1. "Ajan kural yazamaz" ile çelişki **görünürde**: resmi belge hafızayı bağlam, hook'u dayatma sayıyor; gerçek kural katmanı `PreToolUse` teli. Kanonla uyumlu.
2. "Silme yasağı" ile çelişki **görünürde**: literatürdeki arıza silme değil sessizlik; fren = kesilme bildirimi.
3. **Salih imzası ister:** harness oto-hafıza dizini depo dışında, makine-yerel; jarvis md §2 açık-kaynak görünürlük ilkesiyle çelişir.

## 6. Masa kalemi (hakem §viii; önerilen ilk sırada)
1. **Sessiz-düşme freni (öneri):** kapsül FIFO 8 madde → satır/KB ölçüm bütçesi; düşen madde arşiv pointer'ı + tek satır bildirim; `sicak-katman-fifo.py` revizyonu. İki ölçülmüş arıza sınıfını kapatır, silme yasağını uygulanabilir kılar.
2. Defter köken alanı (yazar · model · AS-OF).
3. Kanondan depo-özeti budaması: kazanç dar, kanon zaten ≤80 satır.

## 7. Koşum profili gerçekleşen
8 ajan (3+3+1 denetçi+1 hakem) · alt-ajan toplam ≈700k token · ≈40 dk. Tahmin 600-900k / 25-35 dk idi.
