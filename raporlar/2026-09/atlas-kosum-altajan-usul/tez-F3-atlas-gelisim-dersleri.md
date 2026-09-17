**AS-OF 2026-09-17, depo HEAD** (dal: main)

# Tez F3 — Atlas (research-agent) tanımının gelişimi ve dersler

Kaynak dosya: `.claude/agents/research-agent.md` (bugün 18.645 bayt — D, `wc -c`). Yalnız izin verilen yollar okundu (git log/show bu dosya için, atlas-kosum SKILL, ajan-metodolojisi §6, skill-uretim-semasi, `cc/rapor/**` ve `raporlar/**` içinde "atlas" grep'i); kapsül/pano/senaryo-defteri/fikir-kutusu/transkript açılmadı (İB-83 kısıtı).

## (1) Kronoloji — 9 commit, 2026-07-14 → 2026-09-10 (D, `git log`)

| # | hash | tarih | ne değişti (git show --stat) | gerekçe (commit mesajından ≤15 kelime alıntı) |
|---|------|-------|-------------------------------|----------------------------------------------|
| 1 | `9347b4e` | 07-14 | +465 satır — dosya sıfırdan kuruldu | "Install Cem's research-agent as CC subagent (V25 exception stamp)" |
| 2 | `7ffe201` | 07-14 | `tools:` alanına context7 iki aracı eklendi (1 satır) | "V52 doctrine: trigger ownership is instrumental, mission is automation" |
| 3 | `76e61bc` | 07-15 | ad `research-agent`→`atlas`, `model: sonnet`→`opus`, R1 revizyon bloğu eklendi (+6/-3) | "rename research-agent to Atlas, model sonnet->opus, default sampled verification (K-017 lesson)" |
| 4 | `f28b51c` | 08-17 | tüm gövde Türkçeye çevrildi (318 ekleme/317 silme — pratikte tam metin değişimi) | "Source files in Turkish... ATLAS agent definition translated faithfully" |
| 5 | `f4d3630` | 08-17 | R3 revizyon eklendi (örneklem-denetimi kural-tabanlı) | "V26 sample audit made rule-based... no random selection" |
| 6 | `5a10322` | 08-17 | İSTİSNA DAMGASI notuna "V25 kuralı tersine döndü" eki (1 satır) | "'build on what exists' principle replaces V25 inspiration-only rule" |
| 7 | `1ef4965` | 09-02 | `model: opus`→`sonnet`, R4 revizyon eklendi | "Opus retired - working pair is Fable (planner) + Sonnet (worker)" |
| 8 | `4ac755b` | 09-09 | R5 revizyonu eklendi (1 satır — üç katman, ajan iki rolde çağrılır) | "three tiers Fable... -> Opus 5 leader agent... -> Sonnet workers" |
| 9 | `fe3f802` | 09-10 | AD EŞİTLİĞİ yorumu eklendi (Carvis=Jarvis, 2 satır) | "name-equivalence (Carvis = Jarvis) guaranteed in every context combination" |

**Model alanı zaman çizelgesi (D):** sonnet (07-14 kuruluş) → opus (07-15, R1) → [Türkçeleştirme 08-17, model değişmedi] → sonnet (09-02, R4, Karar 85 "Opus saf dışı") → [09-09 R5: üç katman rejimi, frontmatter yine `sonnet` ama Agent aracında rol-bazlı `opus` override eklendi].

**Ders (K):** model alanı 3 kez el değiştirdi ama gövde metni (felsefi temeller, akademik mod, çıktı biçimi) 07-14'ten beri neredeyse hiç değişmedi — tek büyük gövde değişimi Türkçeleştirme çevirisiydi (satır sayısı aynı kaldı, dil değişti). Yani "evrim" ağırlıkla üstteki 20 satırlık revizyon bloğunda yaşandı, 450 satırlık gövde durağan kaldı.

## (2) Bölüm haritası — mevcut dosya (18.645 bayt)

| Bölüm | Satır aralığı | Bayt (≈) | Koşumda işe yararlılık değerlendirmesi |
|-------|---------------|----------|------------------------------------------|
| Frontmatter (`name`/`description`/`tools`/`model`) | 1-8 | 1.255 | **Yaşamsal.** Tetikleme + araç izni + model seçimi buradan okunur; description alanı örnek-temelli (2 `<example>`) — Claude'un ajanı ne zaman çağıracağını belirler. |
| Revizyon yorumları (AD EŞİTLİĞİ + İSTİSNA DAMGASI + EĞİTİM KATMANI R1-R5) | 9-19 | 2.958 | **Karma.** Karar tarihçesi için değerli (D-etiketli iz), ama koşum sırasında ajanın kendisi bunu okumaz/kullanmaz — Jarvis'in/insanın soruşturma amaçlı okuduğu meta-katman. Dosyanın ikinci en büyük bloğu (%16) salt tarihçe. |
| AMAÇ | 21-24 | 163 | Küçük, işlevsel — tek cümlelik çerçeve. |
| FELSEFİ TEMELLER (Etik/Epistemolojik/Ontolojik) | 26-96 | 2.751 | **Ölü ağırlığa yakın (K).** Kanıt hiyerarşisi (51-59) ve doğrulama protokolü (61-72) somut ve kullanılabilir; ama "Kategori-Kuramı Ontolojisi" (93-96, morfizmler/bileşim) ve "Ontolojik Yığın" şeması (81-89) hiçbir raporlarda atıfla geri gelmiyor (grep'te "morfizm"/"kategori kuramı" atlas raporlarında görülmedi) — dekoratif felsefi katman, çıktıyı değiştirdiğine dair kanıt yok. |
| AKADEMİK MAKALE ARAŞTIRMA MODU (`--paper`) | 98-157 | 2.155 | **Kullanım kanıtı yok (K).** Grep taramasında `cc/rapor` ve `raporlar` içinde `--paper`/`--slot` kullanan bir koşum kaydına rastlanmadı (arama bu oturumun kısıtları içinde sınırlı — kesin RET değil, K etiketi). Atlas-kosum SKILL'i de bu modu çağırmıyor (adım listesinde `--paper` geçmiyor). Bütçenin %11'i, kanıtlanmamış kullanım. |
| TETİKLER | 159-173 | 557 | Küçük, otomatik/elle ayrımı faydalı ama atlas-kosum SKILL'in kendi tetik cümlesiyle (üstteki listelenen skill açıklaması) örtüşüyor — çift bakım yükü (K). |
| YETENEKLER | 175-193 | 661 | Genel liste, düşük bilgi yoğunluğu; tetikleyici cümlelerin süslemesi. |
| DALGA PROTOKOLÜ (paralel araştırma, MECE ayrıştırma) | 195-236 | 2.129 | **Muhtemelen en işlevsel felsefi-olmayan blok (K, kısmi D).** ajan-metodolojisi.md §6'daki paralellik-uygunluk testiyle (satır 34) aynı fikri taşıyor; atlas-kosum'un "dik alan-ailelerine bölme" mekaniğiyle örtüşüyor — muhtemelen atlas-kosum tasarımına ilham kaynağı, ama şu an iki yerde (burada + skill'de) ayrı ayrı tarif ediliyor. |
| KISITLAR | 238-244 | 347 | Kısa, doğrudan işlevsel (uydurma yasağı vb. — halusinasyon-paketi ile uyumlu). |
| ARAŞTIRMA YÖNTEMİ Aşama 1-4 (çerçeveleme/kanıt/analiz/sentez) | 246-341 | 2.584 | Kanıt hiyerarşisi tekrarı (Aşama 2) + ödünleşim matrisi şablonu kullanılabilir kalıp; Aşama 1'deki "ontolojik/epistemolojik/etik çerçeveleme" üçlemesi FELSEFİ TEMELLER ile neredeyse birebir tekrar (K — aynı üçlü ayrım iki kez, ~900 baytlık yinelenme). |
| Aşama 5: Belgeleme (çıktı dosya şablonu `docs/research/...`) | 343-427 | 1.710 | **Şüpheli/eski (K).** Şablon `docs/research/{konu}_{tarih}.md` yoluna yazmayı öngörüyor; ama gerçek atlas koşumları `cc/rapor/` ve `raporlar/` altına yazılıyor (grep sonuçları — örn. `raporlar/2026-09/2026-09-09-problem-cozme-ai-cagi-atlas.md`). Dosyanın kendi çıktı-yolu talimatı fiilen kullanılmayan bir konvansiyonu tarif ediyor; en büyük tek ölü-ağırlık adayı (~1.7 KB). |
| ÇIKTI_BİÇİMİ (orkestratör için kısa özet şablonu) | 429-445 | 318 | Küçük ve mantıklı ama içindeki `docs/research/{konu}_{tarih}.md` referansı yine aynı tutarsızlığı taşıyor. |
| EPİSTEMOLOJİK ÖZ-FARKINDALIK | 447-465 | 651 | Süslü ama işlevsiz (K) — "Biliyorum/Bilmiyorum/Kabul ediyorum" listesi çıktıyı değiştiren bir kural içermiyor. |
| Sürüm/kapanış notu | 467-475 | 394 | Meta bilgi (sürüm 1.0, R2 tarihi) — küçük, zararsız. |

**Toplam ≈ 18.633-18.645 bayt** (bölüm bazlı toplam ile `wc -c` uyumlu, D).

## (3) Atlas'ın çağrıldığı yerler ve koşum hacmi

- **atlas-kosum SKILL** (`.claude/skills/atlas-kosum/SKILL.md:2-7`, D): "Araştırma sorusunu dik alan-ailelerine bölüp paralel Atlas ajanları koşturur — m.40b v0.2 diyalektiği: çoklu-bağımsız tez → hedefli antitez → maskeli hakemlik". Bu skill atlas'ı çağıran birincil orkestratör.
- **ajan-metodolojisi §6** (`core/ajan-metodolojisi.md:34,55`, D): satır 34 "atlas koşumları güvenli tarafta" (paralellik-uygunluk testi bağlamında); satır 55 "Sonnet low (tek-alan) / medium (atlas-tez)" — effort ataması atlas'a özel olarak anılıyor.
- **skill-uretim-semasi** (`core/skill-uretim-semasi.md:108`, D): "md→skill atlas koşumu `cc/rapor/2026-09/rapor-2026-09-15-md-skill-hakem.md`" — atlas farklı bir alanda (skill üretim hakemliği) da kullanılmış.
- **gorev-emri-derleme** (`.claude/skills/gorev-emri-derleme/SKILL.md:3`, D): "ajan/atlas/pipeline koşumu öncesi emir dosyası gerektiğinde" tetikleniyor — atlas'ı emir-üretim zincirine bağlayan nokta, ama bu skill atlas'ı çalıştırmıyor, yalnız emrini derliyor.

**Koşum sayısı için rapor dosyası taraması (D, grep -l "atlas" -i | wc -l):**
- `cc/rapor/**`: **141** dosya (tarih aralığı: dosya adlarına göre 2026-07 → 2026-09, ör. `rapor-2026-07-15-1.md` … `rapor-2026-09-15-md-skill-v26-sondaj.md`).
- `raporlar/**`: **180** dosya (2026-07-16 … devam eden tarihler; ör. `2026-07-16-...md` … `vardiya-teslim-2026-08-16-seans6-stokastik.md`).

**Önemli uyarı (K):** bu sayılar "atlas" kelimesinin geçtiği dosya sayısıdır, tekil koşum sayısı değildir — bir koşum genelde tez/antitez/hakem gibi çoklu dosya üretir (ör. `2026-09-09-problem-cozme-ai-cagi-atlas.md` tek sentez dosyası, ama ham dosyalar `cc/rapor-2026-09-09-ps-{tez,antitez}-A{1,2,3}.md` ayrı ayrı). Gerçek koşum sayısı bu 141+180'den daha azdır; kesin sayı için `v_skill_kosum` görünümü gerekir (bu görev bu dosyayı okumaya izinli değildi).

## (4) Raporlarda kayıtlı atlas dersleri/arızalar

- **403/paywall kısıtı, tekrarlayan desen (D):**
  - `raporlar/2026-08/2026-08-13-spec-kit-atlas-raporu.md:5` — "Reddit tamamen erişilemedi (403)... antitez taraması EKSİK kaldı"
  - `raporlar/2026-08/2026-08-29-ib53-atlas.md:4` — "sourcegraph.com güncel sayfaları 403... anonim github-api 403'leri kimlikli `gh api` ile aşıldı"
  - `raporlar/2026-09/2026-09-09-problem-cozme-ai-cagi-atlas.md:4` — "WEF... SSRN... pnas.org (403)... bls.gov (bot engeli)"
  - `raporlar/2026-07/2026-07-26-pasif-ogrenme-atlas.md:33,75` — "Kurumsal egress politikası... 10/10 ret"; H0 hipotezi "proxy 403'lerine takılan WebFetch/curl" — bu rapor 403 kök-neden analizine kadar gitmiş (deterministik restart sorunu, satır ~404).
- **"K'ya düştü" (V26 örneklem-denetimi kuralının fiilen çalıştığı yerler, D):**
  - `raporlar/2026-09/2026-09-09-problem-cozme-ai-cagi-atlas.md:4` — "tez-A1, tez-A3 ve antitez-A1 dosyalarının TÜM bulguları K'ya düştü"
  - `raporlar/seans/seans-teslim-2026-08-17-seans8-atlas-uclusu.md:13(b)` — "V26 kural-tabanlı örneklem işledi ama iki kusur çıktı: ÇÜRÜTÜLEMEDİ satırları... ve 'tüm bulgular K'ya düşer' kuralının ayrıntı hatalarında sertliği"
  - `raporlar/2026-08/2026-08-26-dil-secimi-ekosistem.md:54` — "V26 45 denetim: 37 TUTUYOR / 4 TUTMUYOR / 4 ERİŞİLEMEDİ (...C tez tarafı ve B antitez tarafı K'ya düştü)"
- **Kotasız/örneklem terimleri:** doğrudan "atlas + kotasız" eşleşmesi bulunamadı (yalnız `buyuk-harf-temizlik-diff` patch dosyasında V26 kuralının "URL'SİZ-İDDİA KOTASI" ifadesi geçiyor — bu atlas'ın örneklem kuralının bir parçası, `raporlar/2026-09/buyuk-harf-temizlik-diff-2026-09-15.patch:878-885`, D).
- **"D sanılan K" doğrudan ifadesi bulunamadı**; en yakın eşdeğer ders `seans-teslim-2026-08-17-seans8-atlas-uclusu.md:13` — "hakem kendi doğrulamasıyla D veriyor; kural harfiyen uygulandı, revizyon adayı kutuda" (K — hakem D etiketini bazen kuralın harfiyle değil kendi kanaatiyle veriyor olabilir riski, henüz karar değil).

## (5) Model-katman uyumu: frontmatter vs kanon (m.6 §6)

- **Kanon (D, `core/ajan-metodolojisi.md:55`):** "icra = tek Fable ana oturumu + Sonnet işçi pipeline'ı... Effort: Fable medium... Sonnet low (tek-alan) / medium (atlas-tez)." Ayrıca CLAUDE.md §6 (proje dosyası, bu oturumda zaten yüklü): "Karar 89: Fable → Opus 5 lider → Sonnet işçi."
- **Frontmatter (D, `.claude/agents/research-agent.md:7`):** `model: sonnet` — sabit, rol ayrımı yok.
- **Dosya-içi R5 notu (D, satır 18):** "Bu ajan iki rolde çağrılır: TEZ/ANTİTEZ işçisi → `model: sonnet` (frontmatter, değişmedi); SENTEZ/HAKEM lideri → Agent aracında `model: opus` + medium effort (atlas-kosum adım 5-6)."
- **Değerlendirme:** Görünüşte çelişki var (frontmatter tek değer, kanon iki katman istiyor) ama R5 notu bunu açıkça çözüyor — frontmatter kasıtlı olarak sadece "worker" varsayılanını taşıyor, lider rolü çağıran tarafın (`atlas-kosum` skill'i, Agent tool çağrısında `model` parametresi override) sorumluluğuna bırakılmış. **Sonuç: gerçek çelişki yok (D)**, ama frontmatter tek başına okunduğunda (bu R5 yorumu görülmeden) yanıltıcı — üç-katman rejimini frontmatter'dan çıkarmak mümkün değil, yalnız yorum bloğundan anlaşılıyor. Bu, ajan tanımının kendi kendini belgeleme kalitesi açısından bir zayıflık (K): kritik model-seçim mantığı HTML yorumuna gömülü, okunabilir ama keşfedilebilir değil.
- **Ölçüm şerhi (D, satır 18):** "Opus-lider n=0 yeni rejimde; ilk 3 koşum `v_skill_kosum`'da izlenir." — bu görevin izin verilen kaynaklarıyla n şu an kaç olduğu doğrulanamadı (`v_skill_kosum` erişim kısıtı dışında; bu K).

## İskelet dersleri (alt-ajan şablonu için)

1. **Al:** Kanıt hiyerarşisi + doğrulama protokolü (satır 51-72) — somut, tekrar kullanılabilir bir kural seti; yeni alt-ajan tanımlarına doğrudan taşınabilir.
2. **Al:** V26 örneklem-denetimi mantığı (son üçte birim + tüm sayısal iddialar + URL'siz-iddia kotası) — raporlarda fiilen çalıştığı D-etiketli olarak doğrulandı, en kanıtlı parça.
3. **Al:** DALGA PROTOKOLÜ'ndeki MECE ayrıştırma sorusu ("bu tek hattı araştırsam ne bulurdum, hâlâ ne eksik kalırdı") — atlas-kosum'un dik-alan-ailesi mantığının kök hücresi; ama yeni şablonda tek yerde tutulmalı (bugün hem burada hem SKILL'de ayrı ayrı yaşıyor).
4. **Alma:** FELSEFİ TEMELLER'deki "Kategori-Kuramı Ontolojisi" ve "Ontolojik Yığın" şeması (satır 81-96) — hiçbir koşum kanıtında geri gelmiyor, ~900+ bayt dekoratif yük.
5. **Alma / revize et:** Aşama 5 "Belgeleme" çıktı yolu şablonu (`docs/research/{konu}_{tarih}.md`, satır 343-427 + 429-445) — gerçek koşumlar `cc/rapor/` ve `raporlar/` altına yazıyor; şablon güncellenmediği için yeni şablonda bu yol baştan doğru yazılmalı, kopyalanmamalı.
6. **Al ama sadeleştir:** ARAŞTIRMA YÖNTEMİ Aşama 1'deki üçlü çerçeveleme (ontolojik/epistemolojik/etik) FELSEFİ TEMELLER ile örtüşüyor — yeni şablonda tek kez tanımlanmalı, iki kez değil.
7. **Al, ama görünür yap:** model-katman mantığı (worker=frontmatter sabit, lider=çağıran taraf override) çalışıyor ama HTML-yorum içine gömülü; yeni alt-ajan şablonunda bu tür kritik model-seçim kuralı gövdede (yorum değil) açık bir bölüm olmalı.
8. **Ders — dış-erişim kırılganlığı:** 403/paywall/bot-engeli çok tekrarlanan bir arıza sınıfı (en az 5 ayrı rapor, D); yeni alt-ajan şablonuna "erişilemeyen kaynak → K etiketi + 'ERİŞİLEMEDİ' sayımı, koşumu durdurma" kuralı doğrudan yazılmalı — atlas bunu ad-hoc olarak her raporda tekrar icat ediyor, kalıcı kural değil.

---
*Not: Jarvis = Salih'le konuşan ana-sıra ajan (eski ad Carvis); sistem = depo. Bu rapor İB-83 kısıtı altında yalnız izin verilen yollardan üretildi; kapsül/pano/senaryo-defteri açılmadı.*
