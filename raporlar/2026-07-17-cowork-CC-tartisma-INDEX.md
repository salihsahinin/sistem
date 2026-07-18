# Cowork/CC Tartışma Oturumu — INDEX (2026-07-17→18)

> **"Dün konuştuklarımı bul" giriş-noktası.** Salih'in CC (Opus yan-oturum) tarafında açtığı tartışma serisinin toplu haritası. **Mod:** hepsi TARTIŞMA/aday · KARAR YOK · **commit branch'e (Salih 07-18 izni, PC'den bulunabilirlik)** · **merge→main/canon = Fable Cowork süzgeci (m.41).** Kanon dosyalarına (core/, pano, kapsül, senaryo-defteri, fikir-kutusu) DOKUNULMADI.

## Nasıl bulunur (PC/Cowork'ten)
`git log --oneline` → bu commit · ya da `raporlar/2026-07-17-*` dosyaları. Scratchpad = uzak-oturum geçici klasörü, PC'den erişilemez (o yüzden commit'lendi).

## Raporlar
1. **`2026-07-17-otomasyon-vizyon-mimarisi-3model.md`** — Nihai hedef (sesle/telefondan geliştirme). Atlas 4-şerit dış-tarama (ses/mobil/otonomi/guardrail) + m.37 **3-model (A kaldıraç / B ölçüm-önce ✅ / C worst-case karşıt-temel)** + triangülasyon + **§9 Kararlar Kısmı** (sesli/mobil karar konsolu, m.18 üç-yüz).
2. **`2026-07-17-skill-fikri-kutusu.md`** — Tekrarlayan-küme→skill tespiti + örnek skill'ler (`karar-modeli`/`karar-hatti`/`atlas-kosum`) + değer sıralaması + Atlas rafine (eval + m.31 freni).
3. **`2026-07-17-cc-okuma-sirasi.md`** — CC'nin Cowork gibi davranması: **yetkinlik özdeş / yetki ayrı** · Cowork≠CC (ortak CLAUDE.md) · 3 opsiyon (pointer / **SessionStart hook** / snapshot) · PreToolUse yetki-kilidi.
4. **`2026-07-17-skill-nasil-olusturulur.md`** — Skill üretim metodolojisi: frontmatter (otoriter) · description zanaatı · script-vs-LLM + `disable-model-invocation` freni · **kompozisyon (`karar-hatti` = context:fork orkestratör)** · skill-creator eval · tuzaklar.

## Açık sorular — TOPLU (Salih cevabı bekleniyor; karar ALINMADI, 07-17 kuralı)
**Skill:** kutu evi (ayrı dosya/bölüm)? · ilk skill (`karar-modeli`/`karar-hatti`)? · hangileri üretim-adayı? · "tekrarlayan-küme→skill" kuralı kanona girsin mi?
**CC:** CC hep yan mı / Fable+beyanla ana-sıra olabilir mi? · hook mu pointer mı? · yetki yapısal-kilit mi talimat mı? · banner metni?
**Otomasyon:** "canlı ajan" çizgisi hangi basamak? · ses PoC'una şimdi mi? · guardrail ilk dilimle mi?
**Kararlar kısmı:** ayrı UI mı (A pano/B push/C ses) yoksa mevcut-yüzey skill/view mi? · hangi kararlar konsola? · sesli-onay doğrulama-derinliği? · `karar-modeli` skill'inin çıktı-hedefi mi?

## Standing direktif (aday — Fable kanonlar)
- Salih 07-17: "atlası her istediğin için koştur" (serbest atlas).
- Salih 07-17: cevaplanmamış soruda karar alma → rapora ekle.
- Salih 07-17: tekrarlayan-küme→skill fikri kutusu.
- Salih 07-18: bu raporlar branch'e commit'lenebilir (bulunabilirlik); merge/canon Fable'da.

## Not (açık borç)
Atlas "skill-metodolojisi" şeridi hâlâ koşuyor → rapor #4 §9 (uçtan-uca akış + ek tuzaklar) dönünce güncellenecek.
