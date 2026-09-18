# Antitez ¬A2 — md→skill atlas koşumu (2026-09-15, Sonnet, CoVe-Factored: yalnız iddia listesi verildi)

## Antitez Raporu — Çok-proje md hiyerarşisi (A2)

**Bütçe:** 4 araç çağrısı (2 birincil WebFetch + 2 WebSearch doğrulama). AS-OF 2026-09-15.

### Genel bulgu
11 iddianın çoğu resmi belgede (code.claude.com/docs/en/memory, erişim 2026-09-15) BİREBİR doğrulandı — ¬T bulunamadı, **çürütülemedi**. Gerçek zayıf noktalar yalnız 2 yerde: "en son=en etkili" ölçüm iddiası ve "resmi belge deseni destekliyor" iddiası.

**Madde 1 — kısmen çürütüldü [?].** Belge sırayı doğruluyor ("instructions closer to where you launched Claude are read last") ama bunun DAHA ETKİLİ olduğuna dair hiçbir ölçüm/deney sunmuyor. Aksine belge şunu söylüyor: "Claude treats [CLAUDE.md/memory] as context, not enforced configuration… no guarantee of strict compliance, especially for vague or conflicting instructions" ve "if two rules contradict each other, Claude may pick one arbitrarily." Yani "en son okunan = en etkili" varsayımdır, ölçülmüş bir iddia değildir — belge çelişkide rastgele seçim olabileceğini bile kabul ediyor. Bu A2'nin en zayıf halkası.

**Madde 2 — çürütülemedi.** Belge tam olarak doğruluyor: alt-dizin CLAUDE.md'leri "instead of loading them at launch, they are included when Claude reads files in those subdirectories."

**Madde 3 — çürütülemedi.** "maximum depth of four hops" ve "imported files still load and enter the context window at launch" — iddia birebir doğru, "token tasarrufu sağlamaz" kısmı da teyitli.

**Madde 4 — çürütülemedi.** "target under 200 lines… Claude Code skips a file over 4 MiB" — birebir.

**Madde 5 — çürütülemedi.** "first 200 lines of MEMORY.md, or the first 25KB, whichever comes first."

**Madde 6 — çürütülemedi.** "Claude Code reads CLAUDE.md, not AGENTS.md… create a CLAUDE.md that imports it" ya da symlink — birebir.

**Madde 7 — çürütülemedi, güçlendi.** WebSearch (Linux Foundation basın bülteni, linuxfoundation.org) teyit ediyor: AAIF (Agentic AI Foundation) Aralık 2025'te kuruldu, AGENTS.md OpenAI öncülüğünde Ağustos 2025'te başlayıp Linux Foundation'a devredildi; 2026 ortası 60.000+ repo, 20+ araç desteği bildiriliyor [kaynak ikincil arama özeti, birincil belge açılmadı — bütçe sınırı].

**Madde 8 — çürütülemedi.** WebSearch: `claude --worktree <isim>` (kısa `-w`) v2.1.49'da (Şubat 2026) eklenmiş yerleşik komut, `.claude/worktrees/` altında yeni worktree+branch açıyor — iddiayla örtüşüyor [ikincil kaynak; code.claude.com/docs/en/worktrees birincil olarak açılmadı, bütçe sınırı].

**Madde 9 — çürütülemedi.** Belge birebir: "a gitignored CLAUDE.local.md only exists in the worktree where you created it" ve auto-memory "shared across worktrees."

**Madde 10 — çürütülemedi, gerilim teyitli.** Resmi belge olay-tetikli ekleme öneriyor ("Claude makes the same mistake a second time" → CLAUDE.md'ye ekle). Kun Chen blogu ise "haftalık toplu düzenleme" + "~5000 token sabit bütçe" savunuyor, anlık tekil düzeltmeyi değil ("evidence comes from transcripts, not from anecdotes," "batch before you update"). İki kaynak GERÇEKTEN farklı ritim öneriyor — iddia doğru, ama bu bir çelişki değil, tamamlayıcı farklı ölçek (Anthropic: ne eklenir: eşik-kuralı; Kun Chen: ne zaman eklenir: ritim-kuralı) olarak da okunabilir [?].

**Madde 11 — kısmen çürütüldü.** Resmi belgede "global md minimal, proje md = birikmiş dersler" çerçevesi DOĞRUDAN yok; belge sadece kapsam tablosu veriyor (yönetilen/kullanıcı/proje/yerel), "proje md nöral-ağ gibi kod yoluyla gelişir" metaforu YALNIZ Kun Chen'e ait, Anthropic hiç böyle bir dil kullanmıyor. Yani desen resmi belgede "karşılık bulmuyor" — Kun Chen'in kendi çerçevesi, Anthropic'in onayı değil.

### Sınanmayan nokta
"Tek global md'nin çok-proje ortamında zararı (yanlış projede yanlış kural) belgelenmiş mi" — iki birincil kaynakta da BULUNAMADI; ne Anthropic ne Kun Chen bu riski ölçüyor/örnekliyor. Bu boşluk A2'nin en savunmasız varsayımı: çok-proje riski iddia edilen ama hiçbir kaynakta ölçülmemiş bir zarar.

### Sonuç
10/11 madde çürütülemedi (resmi/ikincil kaynaklarla teyitli). Gerçek kırılma: (a) madde 1'in "en etkili" kısmı ölçümsüz varsayım, (b) madde 11'in resmi-belge-onayı iddiası abartılı, (c) çok-proje zararı hiçbir yerde belgelenmemiş — A2 tezinin kanıt-dışı en kırılgan noktaları burada.
