# CC Yüzey Okuma-Sırası / Bootstrap — Rapor (TARTIŞMA; Fable/ana-sıra ile)

> **Mod:** rapor · KARAR YOK. **COMMIT: Salih 07-18 izin verdi** (branch'e, PC'den bulunabilirlik için); **merge→main/canon = Fable Cowork süzgeci** (m.41). m.41: bu CC/Opus yan-oturum → öneri üretir, kanon KİLİTLEMEZ. Kaynak: Salih 07-17 ("CC'den de aynı Cowork'teki gibi konuşabilmem için okuma sırası mı yapsak — rapor yap, Fable Jarvis'le tartışacağım"). Araştırma: claude-code-guide (CC mekanizması) + Atlas (yüzeyler-arası tutarlılık). Repo dışı; "işle" denince `raporlar/`e iner.

---

## 1. NETLEŞTİRME (kritik): Cowork ≠ CC — ayrı ürünler, ORTAK CLAUDE.md
claude-code-guide bulgusu: **Claude Cowork ile Claude Code ayrı ürünler, ayrı config sistemleri.** İkisi de `CLAUDE.md` okur (ortak zemin), ama **Cowork, Claude Code'un `.claude/settings.json` + SessionStart hook'larını ÇALIŞTIRMAZ.** Sonuç:
- **Ortak substrat = CLAUDE.md** (git'te; her iki ürün de okur) → okuma sırası + persona buraya yazılınca ikisi de alır.
- **CC-özel garanti = SessionStart hook** (yalnız Claude Code yüzeylerinde: CLI+web+IDE; Cowork'te değil).

## 2. Yüzey haritası
| Yüzey | Model | CLAUDE.md oto-oku | Repo erişimi | Canlı-canon oku | Commit | Mevcut bootstrap | m.41 yetki |
|---|---|---|---|---|---|---|---|
| Cowork ana-sıra | **Fable** | ✓ | ✓ | ✓ (okuma sırası) | ✓ | CLAUDE.md + talimat | **TAM (kanon sahibi)** |
| **CC (bu oturum)** | Opus (≠Fable) | ✓ | ✓ | ✓ (bu oturumda yaptım) | ✓ (teknik) | **YOK — CLAUDE.md'ye yaslı** | **YAN (m.41: Fable değil)** |
| Claude chat (web/tel) | — | ✗ | ✗ | ✗ | ✗ | CHAT-KAPSULU (donuk) | YAN (snapshot) |
| Cep (mobil) | — | ✗ | ✗ | ✗ | ✗ | CEP-KAPSULU (donuk) | YAN (snapshot) |

## 3. Kilit ayrım: CC ≠ chat/mobil
- chat/mobil repo GÖRMEZ → donuk snapshot (CHAT/CEP-KAPSULU) **zorunlu**.
- **CC repo GÖRÜR** → CANLI canon okuyabilir (bu oturumda durum-kapsulu, pano, tüzük'ü okudum). CC'ye donuk snapshot **YANLIŞ** — bayatlar + tekrar + persona-kayması (Atlas Desen 5). CC, Cowork gibi CANLI okumalı.
- Fark Cowork↔CC teknik değil, iki eksende: **(a) model (Fable↔Opus) → m.41 yetki** · **(b) okuma sırasının GARANTİSİ** (Cowork alışkanlıkla yapar; CC fresh oturumda atlayabilir → dayatılmalı).

## 4. ASIL İLKE (Atlas çıpası): YETKİNLİK özdeş / YETKİ ayrı
**Senin isteğin = YETKİNLİK-tutarlılığı** (tam bağlam, doğru Carvis, doğru yöntem) — evet. **m.41 = YETKİ-tutarlılığı DEĞİL.** İkisini karıştırmak tuzak.

Atlas tek-cümle sentezi (dış-emsal): *"Yetkinlik kanona commit'lenir — her yüzeyde ÖZDEŞ; yetki ajanın DIŞINDA, yüzeye ve eylemin geri-alınabilirliğine göre daraltılır — asla ajan tarafından yükseltilemez."*
- **Yetkinlik = paylaşılan taban:** CLAUDE.md + wiki + git-hafıza = her yüzeyin okuduğu tek kanon. Model değişse de (Fable/Opus) persona sabit — **Engine/Agent ayrımı** (Atlas Desen 3). → davranış her yüzeyde AYNI.
- **Yetki = ajan-dışı, yüzeye+geri-alınabilirliğe göre daraltılmış:** **macaroon/attenuated-capability** (Atlas Desen 12) — temel kimlik "Carvis"; her yüzey onun daraltılmış kopyası; kanon-yazma yalnız ana-sıra+Fable'da AÇIK, CC/chat/mobilde KAPALI ve ajan geri açamaz. **confused-deputy** koruması (Desen 15): düşük-yetkili yüzey yüksek-yetkili ajanı kanon-yazmaya kandıramaz.
- **Akademik çıpa:** Collaborative Memory (ICML 2025, Desen 17) — aynı hafıza tabanı, yüzey/role göre filtrelenmiş okuma + farklı yazma politikası. "Repoyu-gören tam görünüm, görmeyen filtrelenmiş" tam bu.

## 5. Okuma sırası — 3 opsiyon
- **Opsiyon 1 — CLAUDE.md pointer (statüko+):** CLAUDE.md'ye CC satırı + yetki-bandı ekle. Ucuz; model-uyumuna bağlı (okumayı atlayabilir). AGENTS.md/CLAUDE.md katmanlaması (Atlas Desen 1) bu yolu destekler.
- **Opsiyon 2 — SessionStart hook (DAYATILMIŞ; ÖNERİ):** `.claude/hooks/session-start.sh` → `durum-kapsulu.md` + `pano.md` + yetki-banner'ı otomatik canon'dan okuyup her açılışa (startup/resume) enjekte eder. CLI+web+IDE'de deterministik (Cowork'te değil). "**mimari > talimat**" (JARVIS ilkesi). Canlı okur → CC her zaman Cowork'ün GÜNCEL durumuyla eşleşir (git-as-truth; otomasyon-raporu triangülasyon #1'iyle aynı taban). Bizde **`session-start-hook` skill'i** tam bunun için var. Kısıt: hook <5s tutulmalı; `disableAllHooks`/untrusted-workspace'te çalışmaz.
- **Opsiyon 3 — CC-KAPSULU snapshot:** chat/mobil tarzı donuk dosya. CC için YANLIŞ (canlı okuyabilir → bayatlar). Yalnız CC'nin neden farklı olduğunu göstermek için burada.

## 6. YETKİ katmanı (Atlas — asıl mesele; okuma sırasından AYRI tasarım)
Okuma sırası "yetkinlik"i çözer; ama senin cümlendeki gizli risk **yetki**. Emsallerin ortak reçetesi:
- **Mekanik: Claude Code izin-önceliği + PreToolUse hook** (Atlas Desen 10; claude-code-guide teyidi). `deny→ask→allow`, `managed>CLI>local>project>user`, **deny her zaman kazanır, managed override edilemez**. → `managed` seviyede CC/web yüzeyi için `core/**` + `CLAUDE.md` + `tuzuk-*.md` yazımı `deny`, `git push` `ask`/`deny`; ana-sıra yüzeyi `allow`. Bu, m.1-2 ("klavyede başkası varsa kalıcı değişiklik yok") + m.41'i **talimattan yapısal kilide** taşır — talimat unutulur, hook unutmaz.
- **Propose-only vs execute** (Desen 11): CC/chat/mobil öneri üretir (`kuyruk/`, `cc/`), commit'i yalnız yetkili yüzey atar. Mevcut `cc/` köprü kanalı zaten bu deseni prototipliyor; eksik = yapısal kilit.
- **Yetki-eşiği ↔ geri-alınabilirlik** (Desen 14): yetki(yüzey,eylem) monoton olarak geri-alınabilirlik(eylem) ile artar × yüzeyin güven-seviyesi. = m.31 eşiğinin (publish/para/pahalı-geri-alma) formel karşılığı. Bu K-009 guardrail hattıyla (PreToolUse, G4) BİRLEŞİR.
- **Authority-banner (yetki-bandı) — hook/pointer enjekte eder:**
  - `(yüzey=CC ∧ model=Opus)` → **YAN oturum:** öneri üret, kanon kilitleme, çıktı = ana-sıraya aday/devir.
  - `(yüzey=CC ∧ model=Fable ∧ Salih "ana sıra" beyanı)` → tam yetki.
  - Model yüzeye pinlenir (settings `model` / `--model`); yetki-bandının teknik dayanağı.

## 7. Persona-kayması bakımı (Atlas Desen 5)
Donuk kapsüller (CHAT/CEP-KAPSULU) bayatladıkça repoyu-gören canlı-kanon ile ayrışır. Öneri: kapsüllere **süre-caveat'ı (kısa TTL)** + kapsül-yaşı üst-verisi (eski kapsül düşük-güvenle davransın) + periyodik senkron (m.24 "hatırlatıcı Carvis'in kendisi"). CC canlı okuduğu için bu sorunu YAŞAMAZ — bu da Opsiyon 2 lehine bir argüman.

## 8. Açık sorular (Salih cevabı bekleniyor — KARAR ALINMADI; 07-17 kuralı gereği rapora eklendi)
1. CC bir gün "ana-sıra" olabilir mi (Fable + senin "ana sıra" beyanınla) yoksa **hep yan** mı? (m.41'in CC'ye uzanışı.)
2. Okuma sırası: **SessionStart hook (Opsiyon 2)** mı, CLAUDE.md pointer (Opsiyon 1) mı?
3. **Yetki katmanı yapısal kilit** ister misin (managed-deny: CC'de core/ yazma + push) yoksa şimdilik talimat-güven mi? (K-009/guardrail ile birleşir — belki oraya ertelenir.)
4. Authority-banner metni ne olsun?

## 9. Kaynaklar + doğrulanmamış bayraklar
- claude-code-guide: CC context-loading (CLAUDE.md hiyerarşisi, SessionStart hook mekanizması, model pinning, Cowork≠CC). Ajan çıktısındaki settings.json örnekleri harness'ta "talimat-şekilli" diye nötrlendi → BULGU olarak alındı, uygulanmadı.
- Atlas yüzeyler-arası: 17 desen/emsal (AGENTS.md katmanlama · macaroon · capability-security/POLA · RBAC-per-surface · OPA · PreToolUse · four-eyes/SoD · HITL-reversibility · Collaborative-Memory).
- Kısıt: WebFetch 403 (birincil doküman tam-metin yok, arama-özeti) + GitHub API kapalı. Bazı emsaller MED güven. "four-eyes ↔ geri-alınabilirlik" bağı Atlas'ın sentezi (tek kaynak yok). Uygulamadan önce code.claude.com/docs/en/permissions güncel sürümü teyit.
