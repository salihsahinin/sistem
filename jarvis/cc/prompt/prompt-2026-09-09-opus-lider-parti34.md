# Yan-oturum promptu — Opus 5 LİDER (medium) · parti 3-4 dosya düzeni + devir-anı loglayıcı · görev tipi: PIPELINE

*Derleyen: Carvis/Fable 2026-09-09 ~12:30; Karar 89 rejimi 2. koşumu. Salih: mevcut Opus oturumuna (İB-75 devrini bırakan) ya da yeni bir Opus 5 medium oturumuna `~/jarvis`de aşağıdaki bloğu aynen yapıştır. Görev tipi: PIPELINE (tek geçiş: taşı → yolları düzelt → kapılar → commit; korunan değişmez yok → loop değil; nested yok).*

---

Sen Carvis'in LİDER-AJANISIN (Opus 5, effort medium — Karar 89). Yan-oturumsun (m.41): kanon kararı almazsın; `core/` · `CLAUDE.md` · `.claude/` DOKUNULMAZ (Bash teli de engeller) — oradaki yol değişikliklerini devir notuna "ana-sıra uygular" listesi olarak yazarsın. Önceki koşumun devir notu `cc/devir-2026-09-09-opus-ib75.md` işlendi (ledger + defter Fable'da); bu yeni bir görev.

**Önce aç (sırayla):**
1. `cc/gorev-2026-09-09-parti34-dosya-duzeni-devir-ani.md` — GÖREV EMRİ (tek kaynak; prompt yalnız varsayılan verir, çelişkide EMİR kazanır).
2. `kuyruk/dosya-duzeni-plani-2026-09-09.md` — Salih onaylı hedef ağaç + parti tablosu (parti 1-2 bitti, 289f53c).
3. `raporlar/2026-09-09-ib75-baglam-devri-ekip-lideri.md` §4 (devir-anı yüklemi; yalnız o bölüm) — U2'nin girdisi.
4. `core/ajan-metodolojisi.md` §4/§6 (lider ≠ işçi; işçi SENKRON, bütçe 10-15, tavan 20 bu emirde).

**Görev tipi: PIPELINE.** Manifest `veri/manifest/u9-parti34-dosya-duzeni.json` (`tur: pipeline`). Birimler emirdeki sırayla, her biri Sonnet işçi (low; U1c medium):
- **U1a** `cc/` taşıma (git mv, adlar değişmez) → parti-3 commit.
- **U1b** `raporlar/` taşıma → parti-4 commit. (U1a ve U1b paralel koşabilir: yazar kümeleri ayrık; U1c ikisinden sonra.)
- **U1c** sabit yollar: `tools/*.py` + ledger 138 pointer + md pointer'ları + alt-dizin README'leri; core/.claude dosyaları için yalnız LİSTE (dosya:satır, eski → yeni). Kapılar: testler yeşil · pointer-kayma KIRIK 0 · karar-borcu kırık 0 · katman-hatti exit 0 · silver-saglik --kapi exit 0 (YETİM sayısını önce/sonra yaz).
- **U2** `tools/devir-ani.py` + 3 test + katman-hatti uyarı-kanalı adımı + SCRIPTLER satırı → commit. Yüklem yalnız LOGLAR, ateşlemez; E2 = 600.000 `[?]` sabit (Q2 Salih'te).

**Sınırlar:** silme YOK (m.8) · `git add <yol>`/`git mv` (başka oturumlar açık, `-A` yasak) · commit parti başına ayrı, İngilizce `[icra] …` · push YOK (m.9) · işçi tavanı 20 çağrı · ajan freni UYARI 36 / DURDUR 72 (oturum-geneli sayaç alt-ajanları da sayar) · uydurma yok, "bulunamadı" meşru · parti-2 dersi: blanket `sed` plan cümlelerini bozdu → dosya-dosya doğrula · "artık kullanılmıyor" gördüğün dosyayı TAŞIMA, karantina adayı olarak devir notuna yaz (tescil Salih'in).

**Bitiş:** `cc/devir/devir-2026-09-09-opus-parti34.md` (İB-75 §6 geri-dönüş şeması): biten/kalan · "ana-sıra uygular" listesi · YETİM önce/sonra · karantina adayları · ajan sayacı · sapmalar · Salih'e açık sorular (hüküm verme). Son mesajın: devir dosyasının tam yolu + `open -R`.
