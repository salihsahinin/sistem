# Vardiya Teslim — Öğrenme Şeridi P6 (2026-07-22)

> Şerit 2 (öğrenme) → Şerit 1 (ana-sıra) devir. Öğrenme oturumu canon'a YAZMAZ; ana-sıra bu dosyadan ingest eder. Kaynak oturum: Cowork/Opus, "günaydın öğrenme — p6". Bu devir P5 devrinin (aynı gün) DEVAMI; P3→P6 reconcile setini birlikte taşır.

## 1. Sonuç
**P6 (Context eng. II: compaction, not-tutma, izolasyon) DONE (07-22).** Salih onayı: "hepsini okudum anladım." Ek: Salih **Model B→C geçişini onayladı** (madde 3).
- Ders kaydı: `ogrenme/dersler/2026-07-22-P6-context-eng-compaction.md`
- Ders (HTML): `ogrenme/dersler/2026-07-22-P6-context-eng-compaction.html` + artefakt `p6-context-eng-compaction`
- Derinlik [T], pasif-okuma v2, 6 blok + 6 gerçek SVG + Yarı-2 (K-015 taslağı).
- DONE kapısı: (a) compaction'da ne hayatta kalır/erir + not-tutmanın onu neden yendiği (b) K-015 sıcak katmanının neden iki-parçalı olması gerektiği (prefix-invalidation).

## 2. Canon'a uygulanacak (ana-sıra ingest) — P3→P6 TAM SET
> Bu mount'ta öğrenme-tracking bayat görünüyor (P3/P4/P5 "—", "Sıradaki: P2", kapsül "Şerit 2: P4"). Ana oturum origin'e yazdıysa pull sonrası aşağıdaki set zaten kısmen uygulanmış olabilir; uygulanmamış kalanları tamamla.

**A) `ogrenme/mufredat.md` — Omurga tablosu Durum sütunu:**
- P3 → **`DONE (07-19)`** · P4 → **`DONE (07-2x)`** (ana-sıra tarihi) · P5 → **`DONE (07-22)`** · P6 → **`DONE (07-22)`**

**B) `ogrenme/mufredat.md` — "Sıradaki oturum" satırı:**
- Öneri: "P1–P6 DONE (P2 devir ingest hâlâ açıksa not düş). Sıradaki: **P7 (Tool-use temelleri)** ya da doğrudan **K-015 inşası** (Salih B→C onayı sonrası öncelik olabilir) ya da Salih seçimi."

**C) `core/durum-kapsulu.md` — YALNIZ Şerit 2 satırı:**
- Öneri: "**Şerit 2 (öğrenme):** **P5+P6 DONE (07-22)** (Context eng. I+II). Yarı-2 → K-015 taslağı (Model B ✅, B→C **Salih onaylı**). Sıradaki: P7 ∨ K-015 inşası ∨ Salih seçimi. P3/P4/P5/P6'yı tekrar KOŞMA (K-019)."

## 3. Salih kararı: Model B→C geçişi ONAYLANDI (çelişki-kapısı notlu)
Salih P6 Yarı-2'de "Model B'den C'ye geçişi onaylıyorum" dedi. **Kayıt:** B (not-tutma öncelikli + iki-parçalı stabil sıcak katman) ŞİMDİ; **C (tam izolasyon: sub-agent'lı araştırma-filosu)** hedef mimari olarak ONAYLI.
**Çelişki-kapısı (m.16) notu — ana-sıra dikkatine:** C'nin aktivasyon tetiği = araştırma-filosu (D4) canlıya alınması. Ama K-009/K-010 (canlı ajan) kanonda **bloke** ve vizyon-merdiveni canlı-ajanı EN SON basamağa koyuyor. Yani onay = **B→C yol haritası + kriter onayı** (B şimdi → C, araştırma-filosu unblock olunca), "C'yi bugün inşa et" DEĞİL. Salih "hayır, şimdi inşa" derse bu K-009/K-010'u yeniden açan Katman-1 kararıdır ve merdiven-çelişkisi ayrıca raporlanır. Ana-sıra bu ayrımı Salih'le netleştirsin.

## 4. Yarı-2 → Şerit 1 aday (K-015 doğrudan tasarım girdisi; senaryo-defteri)
**Soru:** JARVIS uzun oturumda bağlamı nasıl yönetsin? **3 model, 4-tuple; deneysel/proxy (m.39).**
- A — compaction'a güven: doldurur-özetler · özet gecikmesi+cache-miss · ~0.60 (kararlar erir). ✗
- **B — not-tutma öncelikli + stabil prefix ✅:** ~2-3K sıcak sabit · hızlı, çekirdek cache tutar · ~0.85. m.20+m.34+m.9 birebir.
- C — tam izolasyon (B + sub-agent): en düşük ana-bütçe · orta (~7× işçi-token) · ~0.90, m.44 canlı gelince.
**Öneri = B (Salih onayı: B şimdi, C hedef).** B→C eşiği = düzenli-tekrar-eden yüksek-hacim iş; ilk tetik = araştırma-filosu (D4).

## 5. K-015 SOMUT İŞ KALEMLERİ (oturum-içi bulgular — Salih'in 2 uygulama sorusundan)
> **DÜZELTME KAYDI (07-22, seans sonu, ikinci-model denetimi):** Salih modeli değiştirip "son 2 cevabını tekrar kontrol et" dedi. Denetim birincil dokümana karşı koşuldu; **madde 1 kısmen YANLIŞ çıktı ve geri çekildi** (aşağıda 1-DÜZELTİLMİŞ). Madde 2/3/4 ayakta, 2'nin başlık yazımı düzeltildi. Kör onay yok kuralı kendi çıktıma da uygulandı.

**1-DÜZELTİLMİŞ — Kapsül "volatil satır tepede = anti-pattern" bulgusu GERİ ÇEKİLDİ.**
İlk cevap kapsülün en tepesindeki `**Güncelleme:** ...` satırını P6 Blok-5 anti-pattern'i saydı. Yeniden doğrulamada bu **yanlış**: prompt-cache geçersizleşmesi **blok granülerliğinde** çalışır, satır granülerliğinde değil. Doküman: prefix-hash kümülatiftir ve "cache hit, breakpoint'e kadar %100 aynı segment" ister. Kapsül tek bir `tool_result` bloğudur → bir satırı dosyanın tepesinden dibine taşımak o bloğun hash'ini aynı şekilde bozar; **cache kazancı sıfır**. Blok-5'in öğrettiği kural doğru, benim **uygulamam** yanlıştı (blok ≠ satır).
- **Doğru kural:** stabil **bloklar** önde, volatil **bloklar** arkada; sıra = tools → system → messages. Ek doğrulanmış ayrıntı: **CLAUDE.md sistem promptunun parçası değil, hemen ardından gelen bir kullanıcı mesajı olarak** enjekte ediliyor → messages'ın en başında; byte-stabilitesi asıl orada para ediyor.
- **JARVIS bu kuralı zaten sağlıyor:** kapsül CLAUDE.md'ye `@import` EDİLMİYOR (P5 kuralı). Yani yapısal kusur yok; kusur **disiplinde** olabilir (aşağıdaki gerçek riskler).
- **Satır sırası neyi GERÇEKTEN etkiler (cache'i değil):** (a) **MEMORY.md sert kesme** — 200 satır ∨ 25KB'ı aşan kısım sessizce düşer, yani en kritik içerik **TEPEDE** olmalı; (b) **SKILL.md compaction-sonrası kırpması** — "kırpma dosyanın BAŞINI korur", kritik talimat başa; (c) uyum/dikkat (yumuşak). Yani `**Güncelleme:**` satırının tepede olması savunulabilir, MEMORY.md disiplinine girerse **doğru** bile.
- **Yerine geçen gerçek riskler (K-015 denetim maddesi):** (i) **oturum ortasında CLAUDE.md'ye yazmak** — prefix'i o bloktan itibaren düşürür, kalan her tur yeniden ödenir → kanon edit'leri toplu ve vardiya sonunda; (ii) **tüzük (40KB) oturum ortasında Read** — büyük blok, thrash adayı; (iii) aynı dosyayı tekrar tekrar Read → çift kopya; (iv) **kapsül bir tool-output'tur ve compaction'ın BİRİNCİ aşamasında ilk temizlenenler arasındadır** (aşağıda).

2. **Compaction entegrasyonu (bugün yok) — AYAKTA, yazım düzeltildi:** CLAUDE.md'ye **"Compact Instructions"** başlıklı bölüm ekle (doküman birebir: *"To control what's preserved during compaction, add a 'Compact Instructions' section to CLAUDE.md or run `/compact` with a focus"*). İçerik: "aktif karar + açık borç + çelişki-kapısı KORU; ham araştırma/log AT". + `/compact focus` alışkanlığı. Asıl kural: not-tutmayla compaction'ı olay-olmaktan-çıkar. **Yeni doğrulanan mekanik:** compaction iki aşamalı — "önce eski **tool çıktıları** temizlenir, gerekirse sonra konuşma özetlenir". Bu, oturum başında okunan kapsülün **özetlenmeden önce silinen** ilk şeylerden olduğu anlamına gelir → kapsülü oturum ortasında yeniden-oku refleksi, K-015 tasarım kalemi.
3. **CLAUDE.md denetimi:** bu oturumda bridge düştüğü için YAPILAMADI (seans sonuna kadar da dönmedi). K-015'in ilk somut adımı — ama **satır-sırası değil** şunlar denetlenecek: backtick'siz `@...` satırı var mı (istemsiz eager yükleme, P5), CLAUDE.md içinde volatil/tarihli içerik var mı (oturumlar arası byte-stabilite), 200 satır hedefi, "Compact Instructions" bölümü var mı.
4. **"CC'den araştırıldı mı" tespiti:** facts Atlas'ta vardı (07-15) ama hot-layer YAPISI CC cacheable-prefix'e karşı hiç denetlenmemişti; P5/P6 ilk denetim. **Denetimin kendi çıktısı da denetlendi ve bir bulgu geri çekildi** (madde 1) — bu, yapısal denetimin gerekliliğinin kanıtı olarak deftere geçsin.
5. **Yeni (ikinci denetimde çıktı):** compaction sonrası **skill LİSTESİ yeniden enjekte edilmiyor**; yalnız fiilen çağrılmış skill gövdeleri, **5.000 token/skill · 25.000 token toplam**, en eski düşer, **kırpma dosyanın başını korur** → `atlas-kosum`/`karar-modeli` SKILL.md'lerinde kritik talimat ilk satırlara alınmalı.

## 6. Açık / taşınan
- P2 devir ingesti (varsa hâlâ) — ayrı iş.
- CLAUDE.md denetimi (madde 5.3) — K-015 ilk adım.
- Kayıtların git commit'i Salih'in makinesinde (m.9; mount'tan git YAZMA yok). NOT: bu devir yazılırken device bridge düşüktü — dosyalar chat'e teslim edildi; diske commit bridge dönünce / Salih tarafında.
