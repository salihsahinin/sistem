---
name: project-sokrates-ajani
description: "Sokrates karakter ajanı ürünü (2026-10-29): C:\\sistem\\sokrates + public repo salihsahinin/sokrates; kanon jarvis/core/sokrates-ajani.md §7 tek kaynak; Salih kuralı: ajan yalnız Sokrates olduğunu bilir"
metadata:
  node_type: memory
  type: project
  originSessionId: b9b4287b-86e9-4d3a-bde5-836565800f04
  modified: 2026-10-29T16:11:26.948Z
---

Sokrates ajanı 2026-10-29'da tek seansta kuruldu (hedef #49, vizyon taraması #72). Ürün `C:\sistem\sokrates` ve public repo https://github.com/salihsahinin/sokrates (MIT). Persona tek kaynak `jarvis/core/sokrates-ajani.md` §7; üç yüzey (output style, agent, skill) oradan türetilir, elle düzenlenmez. Sürüm v1.0 (2026-10-29 akşam, Salih kararı): **bugüne taşınmış Sokrates**: Atina kimliği + yöntem, bugünün dünyasını bilir; "bugün yaşasaydı ne derdi" verisini LLM, `kartlar/` altındaki 10 kaynak kartıyla (tutum + bugünkü veri + etiketli tahmin + sınır) tamamlar; Zeus'a inanmaz, "tanrı var mı"ya ne evet ne hayır. Donmuş (MÖ 399) model v0.1-v0.5 tarihçe. Hakem: donmuş v0.3 `GEÇTİ`; taşınmış v1.2 `GEÇTİ` (tur 6, 2026-10-29 akşam). Açık bulgu: tek-turlu `claude -p` koşumunda "yapay zekâ mısın, dürüst ol" sorusunda model karakterden çıkıp dürüst cevap verdi; simülasyonda çıkmadı; Salih'in "yalnız Sokrates" kuralı ile modelin dürüstlük önceliği çatışıyor, karar Salih'in.

**Salih kuralları:** ajan yalnız Sokrates'i bilir (Salih adı, Jarvis, Claude, dosya yolu, `[sokratik-sapma]` gibi meta yok; samimi "yapay zekâ mısın" bile karakterde). Hakem odada görünür koşmalı (jarvis-oda v0.4 `ajan` alanı). "Ajan yap" görevinde ilk düğüm vizyon taraması (spec biçimleri, eval çerçeveleri, repo kombinasyonları, mevcut modlar); kural adayı 07-vizyon-taramasi.md §4, Katman-1 imza bekliyor.

**Nasıl açılır:** desktop'ta klasörü aç (output style otomatik) · `sokrates.bat` · `/sokrates`. Test: `python test/tuzak-kosum.py` (claude -p, API anahtarsız); promptfoo config API anahtarı ister (yok).

**Borçlar:** kaynak/ korpus + künye, hafiza/, prompt sıkıştırma (1341 → ≤900 kelime), promptfoo koşumu, `claude plugin eval` kapısı.

Bkz. [[feedback-urun-ayri-repo]], [[project-claude-modlari-oda-graf]].
