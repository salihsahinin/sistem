# Ders Kaydı — P6: Context Engineering II — Compaction, Not-tutma & İzolasyon (2026-07-22, KOŞTU — DONE kapısı AÇIK)

> Altıncı öğrenme oturumu. Derinlik [T], eksen L1; ön-koşullar P5 ✓ · P1 ✓. Teslim: tek dosya HTML ders (6 blok + Yarı-2 + 6 gömülü SVG) — `dersler/2026-07-22-P6-context-eng-compaction.html`. **Bu .md kaydı ingest'te yazıldı (07-23 PC açılış vardiyası, Carvis): P6 devir raporu ve ders-md diskte yoktu; html tek artefakttı (kapsül Şerit-2 borcu).** DONE kapısı Salih beyanı bekliyor (aşağıda).

## Ders özü (pointer — tam anlatım html'de)
- **Üç uzun-ufuk stratejisi, müdahale zamanıyla:** izolasyon (gürültü doğmadan, önleyici) → not-tutma (süreç boyunca, proaktif) → compaction (dolunca, son güvenlik ağı). Tamamlayıcı, rakip değil.
- **Compaction = kayıplı özet:** diskte yaşayan (CLAUDE.md · MEMORY.md · MCP) reload'da tam döner; yalnız konuşmada yaşayan özete erir. Skill gövdeleri cap'li (5K/skill, 25K toplam). Kaldıraçlar: `/compact focus` + CLAUDE.md `# Compact instructions`.
- **Not-tutma compaction'ı yener:** değeri anında diske yaz → reload'da tam döner. "Önce sadık kayıt, sonra ajan" + m.9 proof-of-work'ün mekanik ispatı; m.34 katmanlı-damıtmanın birebir karşılığı.
- **İzolasyon (sub-agent):** taze izole pencere, geçmişi görmez, yalnız özet döner — m.44 lider/işçi düzeninin mekanik zemini. Bedeli ~7× token; düzenli tekrar eden gürültüde kârlı, tek seferlikte israf. Fork istisnası: ana bağlamı miras alır.
- **Cacheable-prefix × compaction:** prefix-invalidation — tepede değişen bir bayt altını cache'ten düşürür. Kural: sıcak katman iki parçalı — değişmez çekirdek (kimlik+kural) EN ÜSTTE, volatil (tarih/sayaç/bugünün kararı) ALTTA. Timestamp tuzağından kaçın.
- **Blok 6 sentezi — K-015 şema taslağı (4 katman):** 1·stabil çekirdek (byte-sabit, cacheable) · 2·volatil sıcak (altında) · 3·disk notları (pointer+Read, compaction-dayanıklı) · 4·izole işçiler (özet döner).
- **Tek cümle P6 kuralı:** uzun oturumu compaction'la kurtarma, not-tutmayla önle; değeri anında diske, gürültüyü sub-agent'a, sıcak çekirdeği byte-sabit — compaction yalnız son ağ.

## Yarı-2 (m.37, 3 model — K-015 bağlam-yönetim stratejisi)
A compaction'a-güven (~0.60, kararlar erir, ✗ elenir) · **B not-tutma-öncelikli + stabil-prefix (✅ ÖNERİ: sıcak ~2-3K, ~0.85; m.20/m.34/m.9 birebir)** · C tam-izolasyon (~0.90 ama ~7× işçi-token; Jarvis v1 + araştırma-filosu canlıyken). Rakamlar deneysel/proxy (m.39). **B→C geçiş eşiği (P5'ten devralınan soruya cevap): düzenli tekrar eden gürültülü iş sınıfı doğunca — ilk aday araştırma-filosu (D4); C tetiği = filonun canlıya alınması.** Nihai karar + senaryo-defteri kaydı ana-sırada (bu ders kanona yazmaz — kayıt 07-23 ingest'te düşüldü).

## Kaynaklar (m.40 araştırma-önce, derste doğrulandı)
Claude Code docs: context-window (compaction hayatta-kalma tablosu) · sub-agents (izole pencere, fork, persistent memory) · costs (auto-compaction, caching, ~7×) · Anthropic Engineering "Effective context engineering for AI agents".

## DONE kapısı — AÇIK (Salih beyanı bekliyor)
Kendi cümlenle: (a) compaction'da ne hayatta kalır, ne erir — not-tutma onu neden yener? (b) K-015 sıcak katmanı neden iki parçalı — değişmez üstte, volatil altta? "Okudum anladım" ya da "şu blok bulanık: …" beyanıyla kapanır; bulanık blok v2 ile yeniden geçilir.

## Açık borç / taşınan
- DONE kapısı beyanı (Salih) — kapanınca mufredat Durum "KOŞTU" → "DONE" çevrilir.
- Model B'nin K-015 uygulaması (kapsül iki-parçalı yeniden yerleşimi dahil) — Şerit 1 işi, K-015 tasarım girdisi.
- Bağlam hijyeni: derste nötr yapısal dil kullanıldı, biyoloji-kökenli metafor yok.
