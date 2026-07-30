# Orca ADE — JARVIS'te en iyi nasıl kullanırız? — Atlas Raporu (2026-07-19)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: 3 (A: teknik gerçek · B: JARVIS-uyum · C: alternatifler) · GitHub taraması: birincil (MCP API, 2026-07-19)
> **Kanıt kısıtı (dürüstlük):** GitHub *release* API + `onorca.dev` + `dev.to` + `andrew.ooo` + App Store WebFetch'te 403 döndü → mobil-mağaza metrikleri, telemetri-metni ve RAM/DMG boyutu **birinci elden doğrulanamadı** (aşağıda [K]/[X] bayraklı). Repo *metadata* (yıldız/fork/issue/doğuş) GitHub search-API'den birincil alındı [D]. `context7` MCP yetkisiz (kullanılamadı).
> **Okuma sırası (Fable):** §0 Carvis sentezi + karar → yeterli. Detay isteyen §1 aile-bulguları · §2 V26 denetim · §3 cevaplanmamış sorular.

---

## §0 — Carvis sentezi (önce oku)

**Konu:** "Orca ade" = **Orca ADE** — `stablyai/orca`, YC-destekli Stably AI'ın MIT-lisanslı, açık kaynak *Agent Development Environment*'ı. İzole git-worktree'lerde 30+ CLI kodlama ajanını (Claude Code, Codex, OpenCode, Grok…) paralel koşturan masaüstü (macOS/Win/Linux) + mobil (iOS/Android) uygulama. Slogan: *"Fan one prompt across five agents, each in its own isolated git worktree — compare the results and merge the winner."* [D] (https://github.com/stablyai/orca)

**Üç cümlede gerçek (tez∧antitez kesişimi — en sağlam):**
1. Orca **gerçek, güçlü ve çok aktif** bir araç: 22.249 yıldız, v1.4.146 bugün (2026-07-19) yayınlandı, ~844 sürüm, günde birden çok ship, MIT + BYO-abonelik. [D]
2. Ama **erken-aşama ve kırılgan**: ~4 aylık (doğuş 2026-03-17), ağır Electron, ~750 açık issue + ~1.011 açık PR, güncel sürümde açılış çökmesi (#9441 [D]), zombie-süreç/sessiz-veri-kaybı hata sınıfları, Homebrew imza hatası (#9282). [D]
3. **Kritik:** Orca'nın başlık-değeri (worktree izolasyonu, paralel oturum, masaüstü+mobil, arka-plan) artık JARVIS'in **zaten üstünde koştuğu** yığında native var — Claude Code `isolation: worktree` (doğruladım [D]) + Cowork web/mobil/arka-plan (2026-07-07 açıldı [K]). Orca'nın **kalan biricik üstünlüğü dar**: vendor-agnostik çok-satıcı fan-out (Codex+Grok+Claude'u TEK yüzeyde yan-yana diff-merge) + Linear + Design Mode.

**Karar önerisi (m.31: benimseme Katman-1 = Salih'in kararı; ben tavsiye + gerekçe veriyorum, m.6):**

> **Orca'yı JARVIS'in orkestrasyon-katmanı olarak BENİMSEME. Onu K-013 deseniyle işle: "kurulmaz, desen madeni" — alet değil, ayna.**

Gerekçe (dört bağımsız hat aynı yöne yakınsıyor):
- **Öz-uyuşmazlığı:** Orca kodlama-*diff* IDE'si; JARVIS file-first *bilgi/köprü* OS'u. Aynı ontolojik nesneye bakmıyorlar. [D→akıl]
- **Kanon-repoda kontrendike:** Orca'nın çekirdeği "5 ajan aynı dosyayı düzenlesin, en iyi diff'i merge et". Bunu `core/` veya `wiki/` üzerine koşmak **m.8 (oto-silme yasağı) + m.31 (kanon = Salih, Katman-1)** çiğner. Orca'nın fan-out'u ASLA JARVIS kanon reposuna bakmamalı.
- **İlke çakışması:** "her şeyi kendim kurarım" (ağır dış Electron bağımlılığı + iş-akışı format lock-in), tek-flagship odağı (m.13), ve temkinli m.30 canlı-ajan kademesini (önce tetik, sonra kimlik) yüksek-fan-out otonomiye zıplayarak atlar.
- **Marjinal net fayda:** CC/Cowork zaten worktree+subagent+mobil+arka-plan veriyor; Orca'nın eklediği (çok-satıcı tek-yüzey diff + Design Mode) JARVIS'in bugünkü iş akışında koşmuyor.

**Nerede GERÇEKTEN işe yarayabilir (dar, opt-in, kanon-DIŞI):** IF/WHEN **PortRisk** (gerçek kodlama artefaktı, m.13) ağır çok-ajanlı paralel kodlama gerektirir **VE** Salih Codex/Claude/Grok'u telefondan yan-yana kıyaslamak ister → Orca aday. O zaman bile: yalnız **PortRisk kod-reposunda** (JARVIS kanon reposunda DEĞİL), telemetri kapalı (`DO_NOT_TRACK=1`), deneysel dış-araç damgasıyla. Ve **önce** native CC worktree + Cowork mobil denenir (sıfır yeni bağımlılık); yalnız "çok-satıcı-tek-yüzey" ihtiyacı gerçekse Orca'ya uzanılır.

**En yüksek-değerli JARVIS kullanımı = desen madeni (Orca kendi sezgimizi doğruluyor):**
| Orca özelliği | JARVIS'te karşılığı / çalınacak fikir |
|---|---|
| fan-out → karşılaştır → kazananı merge et | = **çeşitlilik-bütçesi / çift-atlas / koşum-deseni** (bu rapor tam da öyle üretildi). Orca, prompt-düzeyinde koştuğumuz deseni alet-düzeyinde doğruluyor. Aday skill: "N ajan → diff → seç" — ama merge yetkisi kanonda Salih'te (m.31). |
| Mobile: monitor & steer from phone + bitiş bildirimi | = **mobil-köprü** (Salih telefondan izler/yönlendirir). Cowork'te zaten kuruluyor; Orca referans. |
| Annotate AI diff → ship back to agent | = **KÖPRÜ (m.17)**: kararın işçi ajana en verimli ulaşması. Diff-satırına yorum → ajana geri. |
| Account/usage switcher + rate-limit görünürlüğü | = **token×zaman model-kombinasyonu** enstrümanı. `raporlar/usage/` için UI referansı. |
| `orca worktree/snapshot/click/fill` (agent-to-IDE CLI) | = **K-009 "otomasyon = tetik devri"** referansı: Carvis (Fable) worktree akışını headless script'ler. |

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile A — Teknik gerçek / olgunluk
- **Tez:** Olgun ve fiilen kullanılabilir güçlü araç. İzole-worktree fan-out/merge mimarisi [D]; 22.2k yıldız, günde çok sürüm (v1.4.146, ~844 release) [D]; 30+ ajan [D] (40+ [K]); Ghostty-WebGL terminal, SSH remote-worktree, Design Mode, computer-use, agent-CLI [D]; tam platform + brew/AUR/AppImage + iOS/Android [D]; MIT + BYO-abonelik [D]. (https://github.com/stablyai/orca · https://raw.githubusercontent.com/stablyai/orca/main/README.md)
- **Antitez (¬):** Erken-aşama/kırılgan. ~750 açık issue + ~1.011 açık PR [D]; güncel v1.4.146 açılışta çöküyor (#9441 [D]); computer-use ~200 kontrolsüz süreç → 40-50GB RAM [K]; zombie daemon/PTY birikimi (#9138/#9229 [D]); sessiz veri kaybı (#9158/#9073/#9155 [D]); Homebrew imza + ASAR bütünlük hatası (#9282 [D]); belgelenmiş telemetri/opt-out issue'su bulunamadı; tek-vendor bus-factor + upgrade-treadmill riski [K]. (https://github.com/stablyai/orca/issues/9441 · /9138 · /9282)
- **Kesişim:** Gerçek + çok-aktif + MIT, AMA ~4 aylık ve production-hazır değil. "Terk" riski YOK; risk = hızlı-kırılma + hızlı-değişeni-kovalama + vendor-pivot.

### Aile B — JARVIS'e uyum
- **Tez:** Çekirdek desen JARVIS ihtiyaçlarına birebir: paralel-vardiya = fan-out [D]; mobil-köprü = mobil companion ("monitor and steer your agents from your phone", doğruladım [D]); köprü = diff-annotate [D]; model-hiyerarşi = usage/account switcher [D]; Claude Code birinci-sınıf destekli → Fable/Opus yığını değişmeden sarılır [D]; K-009 tetik-devri = Orca CLI [D]. (https://raw.githubusercontent.com/stablyai/orca/main/README.md · https://www.onorca.dev/docs/mobile [403])
- **Antitez (¬):** Ontolojik/teleolojik ters. Orca kodlama-diff IDE'si, JARVIS bilgi-OS'u [D→akıl]; ~250MB Electron / 400-800MB boşta RAM → "kendim kurarım"a aykırı [K]; worktree rakip-diff'i kanon-repoda kontrendike, m.8+m.31 çiğner [D→akıl]; m.13 tek-flagship + m.30 canlı-ajan-kademesi ile çelişir; CC/Cowork zaten worktree+subagent+mobil veriyor → marjinal katkı [D]. **Dürüstlük düzeltmesi:** telemetri sandığından temiz (PostHog anonim; dosya/prompt/repo-adı GÖNDERMİYOR; `DO_NOT_TRACK=1`/`ORCA_TELEMETRY_DISABLED=1`) — ama [K] (kaynak 403, doğrulanamadı) + varsayılan AÇIK + private repo (m.14) güven-sınırını genişletir.
- **Kesişim:** Orca'nın *özellikleri* JARVIS ihtiyaç-adlarıyla eşleşiyor ama *özü* JARVIS özüne ters; eşleşen çekirdek (worktree paralellik + mobil izleme) JARVIS'te CC/Cowork ile zaten mevcut.

### Aile C — Alternatifler / fırsat-maliyeti
- **Tez:** Orca'nın savunulabilir üstünlüğü dar ama net: 40+ vendor-agnostik ajanı tek cilalı native masaüstü+mobil yüzeyde fan-out/merge + görsel diff-review + Linear + Design Mode. gastown'da native app yok, orca-orchestrator headless (UI yok), ruflo npm/web; hiçbiri native masaüstü+mobil'i birlikte vermiyor [D]. (https://github.com/gastownhall/gastown · https://github.com/gwmage/orca-orchestrator)
- **Antitez (¬):** Alternatifler baskın. **Claude Code v2.1.49 native `isolation: worktree` (doğruladım [D])** + **Cowork web/mobil/arka-plan (2026-07-07 [K])** Orca'nın başlık-özelliklerini 250MB Electron olmadan zaten veriyor; orca-orchestrator (MIT headless) çekirdeğin "sökülebilir/ince" olduğunu kanıtlıyor (ama 0★/2-commit, üretim-değil [X]); kendi ff-only script'i (A+C aşısı) felsefeye daha uygun; Orca'nın kendi incelemecisi "paralel işe ihtiyacın yoksa Orca fazla" diyor [K]. **Dürüst bayrak:** "IDE headless'e ters" iddiası zayıf — Orca'nın headless CLI + Linux server desteği VAR; gastown 17.1k★ < Orca 22.2k★, "daha olgun" iddiası yıldızla YANLIŞ.
- **Kesişim:** Orca'nın çekirdek değeri JARVIS ekosisteminde (CC+Cowork) zaten var; Orca'nın *ekstrası* (çok-satıcı tek-yüzey + Design Mode) tam da JARVIS'in bugün koşmadığı iş.

---

## §2 — V26 örneklem-denetimi

| Ajan | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| A-tez | Fan-out/merge sloganı + MIT + 30+ ajan + Claude Code ilk | **[D] doğrulandı** (raw README birebir) | Bulgular ayakta |
| A-antitez | #9441 v1.4.146 açılış çökmesi | **[D] doğrulandı** (başlık birebir; "326+ worktree'de 14-20sn'de çıkıyor" ek detay) | Bulgular ayakta |
| C-antitez | Claude Code native `isolation: worktree` | **[D] doğrulandı** (code.claude.com resmi doküman; auto-oluştur/temizle, desktop otomatik worktree) | Eksen bulgu; ayakta |
| B-antitez | Telemetri temiz (`onorca.dev/docs/telemetry`) | **[K] doğrulanamadı** (403 erişim-engeli — çürütülmedi) | Telemetri bulgusu [K] kaldı |
| B-tez | Mobil "monitor & steer from your phone" | **[D] doğrulandı** (README audit'te birebir) | Bulgular ayakta |
| Metadata | 22.249★ / 1.607 fork / doğuş 2026-03-17 | **[D]** (GitHub search-API, bugün) | Bayat 15.7k arama-önbelleği [X] elendi |

**Sonuç:** Denetlenen 4 iddiadan 3'ü birincil kaynaktan doğrulandı (biri daha zengin), 1'i erişim-engelli (çürütme değil). Hiçbir ajanın bulguları K'ya düşmedi → yüksek güven.

---

## §3 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **PortRisk kodlama-koşumu Orca-adayı mı?** (Katman-1: dış-araç benimseme + m.13 tek-flagship kapsamı = Salih kararı. Bu rapor "hayır, kanon için; belki, dar-PortRisk için" tavsiye ediyor — karar Salih'te.)
2. **Çok-satıcı yan-yana kıyas (Codex/Grok/Claude) JARVIS için gerçek ihtiyaç mı**, yoksa Claude-only native paralellik (CC worktree + Cowork) yeterli mi? (Cevap "yeterli" ise Orca'nın tek biricik üstünlüğü de düşer.)
3. **Orca desenlerini JARVIS skill'ine damıtalım mı?** (usage-switcher → `raporlar/usage/` UI · agent-CLI → K-009 tetik-devri · fan-out→diff→seç → çift-atlas resmileşmesi). K-009/skill-kutusu kapsamında aday.
4. **Telemetri [K] borcu:** benimseme gündeme gelirse `onorca.dev/docs/telemetry` (şu an 403) birinci elden teyit edilmeli; ~250MB/RAM rakamı da tek-inceleme [K], birincil ölçüm borcu.

---

*Koşum: atlas-kosum (m.40b) · 3 aile × 2 şerit = 6 bağımsız Atlas ajanı + Carvis GitHub-MCP birincil taraması + V26 denetimi. Ham şerit çıktıları bu oturumun task-transcript'lerinde (efemeral); bulgular yukarıda etiket+URL ile gömülü.*
