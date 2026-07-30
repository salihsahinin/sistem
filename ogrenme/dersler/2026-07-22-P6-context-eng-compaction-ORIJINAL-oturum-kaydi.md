# Ders Kaydı — P6: Context Engineering II — Compaction, Not-tutma & İzolasyon (2026-07-22, DONE)

> Altıncı paralel öğrenme oturumu (Cowork/Opus, "günaydın öğrenme — p6"). Derinlik [T]. Teslim: tek dosya HTML (6 blok + Yarı-2 + 6 gerçek SVG) — chat + artefakt (`p6-context-eng-compaction`) + `dersler/2026-07-22-P6-context-eng-compaction.html`. **Salih onayı: "hepsini okudum anladım" → P6 DONE.** Ayrıca Salih **B→C geçişini onayladı** (aşağıda, çelişki-kapısı notuyla). Canon güncellemesi ANA SIRAYA devredildi (öğrenme şeridi canon'a YAZMAZ): devir `raporlar/vardiya-teslim-2026-07-22-ogrenme-P6.md`.

## Sıra notu (çelişki kapısı, m.16)
Salih P5 sonrası "P6'dan devam" dedi. Kontrol: P6, P5'in doğal devamı (aynı eksen L1, bağlam-mühendisliği; P5 statik-yerleşim, P6 zaman-boyutu). Ön-koşul P5 (bu oturum öncesi DONE). Çelişki yok. Not: bu yerel mount'ta öğrenme-tracking satırları hâlâ bayat görünüyordu (P3/P4/P5 "—", kapsül "Şerit 2: P4") — muhtemelen ana oturum origin'e yazdı, mount pull almadı; devir tam reconcile setini taşıyor.

## Ne oldu (sıra)
1. **Açılış:** taze `core/durum-kapsulu.md` + `mufredat.md` yeniden stage edilip okundu (bayat-açılış önlemi). Salih beyanı "P4 okundu, ana oturumda düzeltme yapıldı" → P4 kapandı (ana-sıra); öğrenme şeridi P6'ya geçti.
2. **Araştırma (m.40 araştırma-önce):** 4 güncel kaynak doğrulandı — Claude Code "context window" (compaction'da ne hayatta kalır tablosu: kök CLAUDE.md/MEMORY.md/MCP diskten reload; konuşma geçmişi + path-scoped rules + nested CLAUDE.md özetlenir; çağrılmış skill 5K/skill·25K cap, en eski düşer; auto-compact; /compact focus), "sub-agents" (izole context penceresi, taze başlar geçmişi görmez, delegation mesajı, sadece özet döner, fork istisnası ana-konuşmayı miras alır, persistent memory field, isolate high-volume operations), "costs" (auto-compaction, prompt caching, agent-team ~7× token), ve Anthropic "Effective context engineering" (structured note-taking: context dışı kalıcı hafıza, geri çağırma; compaction; uzun-ufuk).
3. **Yarı-1 (6 blok, [T], hepsi gerçek SVG):**
   - Blok 1 · 3 uzun-ufuk stratejisi + müdahale noktaları (izolasyon önleyici → not-tutma proaktif → compaction reaktif/son çare), sıralı katmanlama. SVG: dolan pencere + 3 müdahale.
   - Blok 2 (çekirdek) · Compaction = konuşmayı yapısal özetle değiştir. "Ne hayatta kalır" tablosu (disk-reload vs konuşma-özeti). /compact focus + CLAUDE.md compact-instructions. 1M pencere erteler-kaldırmaz. Worked: bir karar, iki akıbet. SVG: öncesi/sonrası.
   - Blok 3 (çekirdek) · Not-tutma = context dışına yaz, geri çağır. **Diske yazılan compaction'ı YENER** (MEMORY.md/CLAUDE.md reload). JARVIS "önce sadık kayıt" + m.9 proof-of-work'ün mekanik ispatı. Worked: MEMORY.md index+topic yazma yönü. SVG: sohbet-notu erir vs disk-notu döner.
   - Blok 4 · İzolasyon = sub-agent taze izole pencere; geçmişi görmez; sadece özet döner. High-volume izolasyonu; fork istisnası; persistent memory. m.44 (lider/işçi ayrı pencere) mekaniği; ~7× token. SVG: ana pencere + sub-agent + özet oku.
   - Blok 5 (çekirdek) · Cacheable-prefix × compaction: prefix-invalidation (tepedeki değişiklik altını düşürür). Stabil çekirdek byte-sabit reload → cache tutar. Timestamp-tuzağı. İki-parçalı sıcak katman (değişmez üstte / volatil altta). Worked: timestamp örneği. SVG: doğru vs yanlış dizim.
   - Blok 6 (sentez) · K-015 dört katman (stabil çekirdek / volatil sıcak / disk notları / izole işçiler) + 4 bağlanma kuralı. Tek-cümle P6 kuralı.
4. **DONE kapısı içeriği verildi:** (a) compaction'da ne kalır/erir + not-tutmanın neden yendiği (b) K-015 sıcak katmanı neden iki-parçalı (prefix-invalidation). Salih "okudum anladım" → geçti.
5. **Yarı-2 (m.37, 3 model — K-015 taslağı):** A (compaction'a güven, ~0.60, ✗) · **B (not-tutma öncelikli + iki-parçalı stabil sıcak katman, ✅ ~0.85)** · C (tam izolasyon, ~7× token/~0.90, m.44 canlı-ajan gelince). Öneri = B. **P5'ten devralınan B→C eşiğine cevap:** eşik = "yüksek-hacim/gürültülü iş düzenli tekrar ediyor mu?" → ilk tetik = araştırma-filosu (D4) canlıya alınması. Rakamlar deneysel (m.39).

## Oturum-içi uygulama soruları (Salih, P6 okurken) → K-015 bulguları
Salih iki uygulama sorusu sordu; cevaplar sistemin gerçek dosyalarına bakılarak verildi (kör onay yok). Çıkan somut bulgular (ana-sıra K-015 iş kalemi):
- **Compaction'ı biz kullanıyor muyuz?** Pasif EVET (auto-compact her CC/Cowork oturumunda varsayılan açık — maruzuz), stratejik HAYIR (CLAUDE.md'de compact-instructions yok, /compact focus alışkanlığı yok, kapsül compaction'a göre tasarlanmamış). Entegrasyon 3 kaldıraç: (1) CLAUDE.md `# Compact instructions` bloğu (aktif karar + açık borç + çelişki-kapısı koru, ham çıktı at), (2) /compact focus alışkanlığı, (3) asıl: not-tutmayla compaction'ı olay-olmaktan-çıkar (değeri anında diske yaz).
- **İki-parçalı sıcak katman bizde var mı?** VAR (yapısal olarak) — ilk cevaptaki "kusurlu" hükmü GERİ ÇEKİLDİ, aşağıya bak.
- **CC'den araştırıldı mı?** Facts EVET (Atlas 07-15, @import/200-satır düğüm-notları), ama hot-layer YAPISI CC cacheable-prefix'e karşı HİÇ denetlenmedi. Tasarım kökeni m.20 + Anlama-Kapısı (07-09), ilk-ilkelerden yakınsama. P5/P6 = ilk CC-temelli denetim.

## DÜZELTME — ikinci-model denetimi (07-22 seans sonu, Salih emri: "son 2 cevabını tekrar kontrol et")
Salih modeli değiştirip son iki cevabın yeniden denetlenmesini istedi. Denetim birincil dokümana karşı koşuldu (prompt-caching + memory + context-window sayfaları). Sonuç:

**AYAKTA:** compaction hayatta-kalma tablosu birebir doğrulandı (kök CLAUDE.md + unscoped rules + auto memory diskten yeniden enjekte; `paths:` frontmatter'lı rules ve nested CLAUDE.md kayıp; çağrılmış skill gövdeleri 5.000 tok/skill · 25.000 tok toplam, en eski düşer). "Pasif EVET / stratejik HAYIR" hükmü ayakta. `/compact focus` ayakta. CLAUDE.md'ye compaction bölümü eklenebilirliği **doğrulandı** — resmî yazım **"Compact Instructions"**.

**GERİ ÇEKİLEN:** "kapsülün en volatil satırı en tepede = Blok 5 anti-pattern" bulgusu **yanlış**. Prompt-cache geçersizleşmesi **blok** granülerliğinde işler (kümülatif prefix-hash; hit için breakpoint'e kadar %100 aynılık). Kapsül tek bir `tool_result` bloğu → satırı tepeden dibe taşımak bloğun hash'ini aynı şekilde bozar, kazanç sıfır. **Blok 5'in öğrettiği kural doğru; benim uygulamam yanlıştı: kural blok sırasına bakar, satır sırasına değil.**

**Doğrulanan ek mekanikler (ilk cevapta yoktu):**
- **CLAUDE.md sistem promptunun parçası değil** — "sistem promptundan sonra bir kullanıcı mesajı olarak" iletiliyor; yani messages'ın en başında. Byte-stabilite asıl orada para ediyor → **oturum ortasında CLAUDE.md'ye yazmak** prefix'i o noktadan itibaren düşürür (gerçek risk; kanon edit'leri toplu/vardiya-sonu).
- **Compaction iki aşamalı:** önce eski **tool çıktıları** temizlenir, gerekirse sonra konuşma özetlenir → oturum başında okunan kapsül, özet aşamasına gelmeden temizlenen ilk şeylerden. Karşı-hamle: kapsülü oturum ortasında yeniden-oku + kritik durumu diske yaz.
- **Thrashing koruması:** tek bir dosya/çıktı çok büyükse auto-compact birkaç denemeden sonra durup hata veriyor (tüzük 40KB → aday risk).
- **Compaction sonrası skill LİSTESİ yeniden enjekte edilmiyor**; yalnız çağrılmış gövdeler, ve **kırpma dosyanın BAŞINI korur** → SKILL.md'lerde kritik talimat ilk satırlara.
- **Satır sırası neyi gerçekten etkiler:** MEMORY.md sert kesmesi (200 satır ∨ 25KB; ötesi sessizce düşer → kritik içerik TEPEDE olmalı) ve SKILL.md kırpması. Yani cache için değil, **kesilme** için önemli — ve yönü ters: tepede olmak korur.

## Format v2 notu
Pasif-okuma + [T] + 2-3 kavram/blok + self-Q&A + JARVIS senaryosu + köprü + her yapısal kavrama GERÇEK gömülü SVG + worked-örnek. 6 SVG, hepsi gömülü. Görsel-atıf/görsel-yok hatası yok.

## DONE kapısı (Salih onayı 07-22 — geçti)
- [x] compaction'da ne hayatta kalır/erir + not-tutmanın neden yendiği söylenebiliyor
- [x] K-015 sıcak katmanı neden iki-parçalı (değişmez üstte/volatil altta; prefix-invalidation) söylenebiliyor
- Ölçüm notu: gerçek anlama ölçümü K-015'i fiilen kurarken (özellikle kapsül iki-parçalı düzeltmesi + CLAUDE.md denetimi) yapılır.

## Açık borç / taşınan
- **CLAUDE.md iç satır-sırası denetimi** yapılamadı (bu oturumda device bridge düştü) → K-015'in ilk somut adımı.
- Ana-sıra ingest backlog (P3+P4+P5+P6 mufredat Durum + kapsül Şerit-2 satırı) — devirde tam set.
