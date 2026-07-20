# B1 — CC Yetenek Taramasının Kalanı (headless · otonomi-merdiveni · skill-verifier · worktree-paralel) — Atlas Raporu (2026-07-20)

> **Mod:** yan-oturum (m.41 · CC = yan oturum, kanon KİLİTLENMEDİ, karar ALINMADI) · şerit: çift-atlas (tez ∧ ¬tez) · aile sayısı: **5** (headless/scheduled/self-healing · auto-mode/otonomi-merdiveni · skill-verifier/eval-gate · worktree-paralel · ünlü-isimler) → 10 literatür/pratisyen şeridi + 1 CC-yetenek/otomasyon karar envanteri.
> **Kanıt kısıtı (dürüstlük):** Bu tur güçlü — `code.claude.com/docs` sayfaları (permission-modes, headless, goal, scheduled-tasks, worktrees, agent-view, routines, best-practices, hooks, ultrareview) çoğunlukla DOĞRUDAN çekildi **[D]**. Egress-403 verenler: `anthropic.com/engineering/*` (multi-agent, auto-mode, containment), `simonwillison.net`, `cognition.ai/blog`, birkaç arXiv PDF → o bulgular WebSearch-özeti **[K]**. GitHub arıza-emsalleri (#68110, #73829, #77414, #68619) doğrudan doğrulandı **[D]**.
> **Okuma sırası (Fable):** §0 Carvis sentezi + §4 dürüst bayraklar → yeterli. Detay: §1 aile bulguları · §2 kaynak/isim tablosu · §3 CC-yetenek kararlarının kategori+kontrolü · §5 V26 · §6 açık sorular.

---

## §0 — Carvis sentezi (önce oku)

**Soru (B1):** CC yetenek taramasının kalan başlıkları (headless `-p`/cron/kota-curfew/self-healing · auto-mode/otonomi-merdiveni · skill-as-verifier/`/ultrareview`/eval-gate · git-worktree paralel) JARVIS otomasyonunda kullanılmalı mı, nasıl?

**En sağlam kesişim (beş ailenin İKİ şeridinin de + envanterin ortak dediği):**

1. **Taranan HER CC yeteneği GERÇEK ve birincil-doğrulandı — hiçbiri vaporware değil.** Headless/curfew/self-heal (Aile A), otonomi-merdiveni (B), skill-verifier/eval-gate/`/ultrareview` (C), worktree-paralel (D) — hepsi `code.claude.com/docs`'ta belgeli, çoğu GA. Soru "var mı" değil, "JARVIS'e uyar mı ve hangi koşulla" sorusu. [D]

2. **Her yetenek birincil kaynaklarda AYNI ÜÇ koşulla ÇİTLENİYOR — bu tez-antitez çatışması değil, yakınsama.** Otomasyonu *mümkün* kılan kaynaklar (Anthropic best-practices, Karpathy, Willison) ile *çitleyen* kaynaklar (Cognition, Anthropic multi-agent-limit, HITL pratisyenleri) AYNI kaynaklar. Üç koşul: **(i) doğrulama-kapısı** (ayrı grader / düşman-reviewer / "verify its work"); **(ii) izin-yüzeyi kısıtı** (deterministik allowlist / minimal araç / bypass yalnız izole-internetsiz konteynerde); **(iii) izolasyon** (worktree / taze bağlam). "Etkinleştir AMA çitle" tek mesaj. [D/K]

3. **JARVIS kanonu bu üç koşulu ZATEN kodluyor — yani doktrinsel iş büyük ölçüde bitmiş.** Permission-surface = m.30 PreToolUse deterministik kilidi (KURULDU + TEST PASS 07-19); doğrulama-kapısı = m.16 çelişki-kapısı + V26 örneklem-denetimi + m.7 (işi yapan puanlamaz); izolasyon = m.41 yapısal kilit + worktree-izolasyon notu (K-015). **Eksik olan doktrin değil, OPERASYON:** frenlerin gerçek koşumda dişi tutuyor mu? [D + envanter]

4. **"Canlı ajan" sınırı doğru yerde çizilmiş (Routines) ve Anthropic'in KENDİ auto-mode tasarımı m.42'yi bağımsız doğruluyor.** Sınır = prompt + kalıcı kimlik devri (dış-tetik + kaydedilmiş-prompt + senin-kimliğinle-koşum üçlüsü ilk Routines'te birleşir); K-009 = merdivenin alt 5 basamağı (tetik-devri), K-010 = Routines. Anthropic'in auto-mode'u otonom-loop'u varsayılan bloklar, geri-alınamaz eylemi her modda kes-devreyle durdurur = m.42 "Özgürlük(a) ≤ Toparlanabilirlik(hata(a))"in birebir dış-aynası; K-010'un "2 hafta stabil" ön-koşulu = Anthropic'in hesap-ön-koşul kapısının aynısı. [D]

5. **Üç koşulu en çok AŞAN varsayılan = çift-atlas ×2 paralelliği; sırf-araştırma atlas'ları izolasyona bile ihtiyaç duymaz.** Multi-agent ~15× token, kötü-davranışta 10× katlanır (D-antitez + A2); worktree "ucuz" miti diskte patlıyor (20 dk'da 9.82 GB, 5-7 tavan) ve çakışmayı çözmez merge'e erteler. En yüksek-kaldıraçlı operasyonel sıkılaştırma yeni-yetenek eklemek değil, **paralel varsayılanı m.25 eşiğine daraltmak** (paralellik = kanıtlı istisna, sessiz varsayılan değil). [K/D]

**JARVIS'e ne demek (gözlem, KARAR DEĞİL — m.41):**

- **Dürüst manşet:** JARVIS bu yeteneklerin gerektirdiği yerin doktrinsel olarak İLERİSİNDE — üç çitleme koşulu zaten kanon. Eksik olan **operasyonel doğrulama:** (a) PreToolUse deterministik kilidi `--bare`/worktree/headless altında da tutuyor mu (bu modlarda CLAUDE.md/settings farklı yüklenebilir)? (b) İstek-yolunda kill-switch var mı — post-hoc Stop DEĞİL, ki #77414 Stop'tan SONRA 300+ ajan doğduğunu kanıtladı? (c) Herhangi bir gerçek otomasyon koşumuna sert bütçe-tavanı (`max_budget_usd`) bağlı mı, yoksa yalnız danışman `total_cost_usd` raporlaması mı var?
- **En yüksek-kaldıraçlı üç gözlem (harita, öneri değil):** (1) **m.30-uyumlu çekirdek headless yol = yerel `claude -p` + PreToolUse gate + `max_budget_usd` sert-cap;** Routines K-010-kapılı adımdır (bulut/onaysız/kimlik-devri). (2) **Savunulabilir eval-gate = deterministik/rubric/DANIŞMAN** (JARVIS'in zaten kurduğu tür), otonom LLM-judge DEĞİL — PreToolUse deterministik kilidini genişlet, LLM-judge kanon-kapısı EKLEME (C-antitez: κ≈0.51, "one token to fool" %80). (3) **Paralel/worktree varsayılanı (çift-atlas ×2) akut maliyet-maruziyeti;** sırf-araştırma atlas'ları izolasyona ihtiyaç duymaz → m.25 kanıtlı-istisnasına daralt.
- **İki eksik guardrail (antitez şeritlerinin gösterdiği):** istek-yolunda kill-switch + sert bütçe-tavanı — post-hoc Stop atomik değil (#77414), vendor "limit"leri çoğu danışman (delinebilir).

---

## §1 — Aile başına bulgular (çift-atlas)

### Aile A — Headless / zamanlanmış / self-healing
- **Tez:** `claude -p`/`--bare`/Agent SDK headless GERÇEK; Routines/`/loop`/Desktop-task/cron zamanlama; `max_turns`+`max_budget_usd`+7-gün-expiry+`CLAUDE_CODE_DISABLE_CRON` curfew primitifleri; ajan-döngüsü+`/goal`+Stop/PreToolUse hook self-healing. K-009'a doğrudan yarar. [D, code.claude.com]
- **Antitez (¬):** Gözetimsiz loop = maliyet-kaçağı (#68110: 48+ ajan/1.5M token, derinlik-limitsiz özyineleme; #68619: Max20x 5-saat limiti <5 dk'da ~4M token; gecede $6.000); durdurulamazlık (#73829: 6.5 saat yetim; #77414: Stop'tan SONRA 300+ ajan, atomik-iptal yok); self-healing/heartbeat sessiz memory-poisoning (OpenClaw #60719/#92082; arXiv 2603.23064 [X]); vendor "limit" çoğu danışman, hard-cut değil; kill-switch istek-yolunda olmalı. [D GitHub + docs, K/X blog/arXiv]
- **Kesişim:** Headless ÇEKİRDEK gerçek yarar AMA yalnız gözetim + PreToolUse gate + sert bütçe-tavanı koşulunda; gözetimsiz/self-healing/zamanlanmış = m.42/m.30/m.31 frenleri yapısal-dişli olana dek erken. Dürüst çekince: Routines (bulut/onaysız/yerel-dosya-yok) m.30 "canlı ajan" tarafı; `--bare` CLAUDE.md yüklemez.

### Aile B — Auto-mode / otonomi-merdiveni
- **Tez:** Merdiven basamak-basamak birincil-haritalı — auto-accept/`/loop`/`/goal`/headless/agent-view (K-009 tarafı: prompt+kimlik insanda) → **Routines (K-010: "canlı ajan" sınırı burada başlar)**; RC = otonomi değil yönlendirme kanalı. Merdiven K-009 içinde bile kademeli sıkılaştırma verir (her basamak öncekinin sigortasını korur). [D]
- **Antitez (¬):** Anthropic'in KENDİ auto-mode'u otonom-loop'u varsayılan bloklar; `bypassPermissions` "hiçbir koruma sağlamaz", yalnız izole-internetsiz konteyner için (JARVIS kanon-repo DEĞİL) ve `core/`+`CLAUDE.md`+`.claude/` korumasını sıfırlar; geri-alınamaz eylem her modda kes-devre (m.42 dış-aynası); auto-mode `Agent`/`Bash(*)` allow kurallarını düşürür; loop'lar devre-kesici ister (3-ardışık/20-toplam blokta duraklar); özerklik hesap-ön-koşuluna kapılı (K-010 analoğu); SWE-Marathon ultra-uzun-ufuk otonomiyi ampirik çürütüyor. [D permission-modes]
- **Kesişim:** Merdiven GERÇEK yapılandırılmış yol VE Anthropic'in kendi tasarımı tam olarak m.42/m.30'u dayatıyor (kademeli, toparlanabilirlik-kapılı, insan-döngüde); K-010'un 2-hafta ön-koşulu = Anthropic'in hesap-kapısının aynı ihtiyatı. Üst basamaklar ön-koşul karşılanana dek erken. **Aile B: iki şerit yakınsıyor.**

### Aile C — Skill-verifier / eval-gate / `/ultrareview`
- **Tez:** skill-creator 4-ajan eval motoru (Executor/Grader/Comparator/Analyzer); kanonik verifier = ayrı durumsuz **outcome-grader** + kanıt-zorlayıcı rubric + grade-and-revise loop ("işi yapan onu notlandıran değil"); Anthropic grader hiyerarşisi deterministik→LLM→insan; `/ultrareview` bulut çok-ajan doğrulama (exit 0/1, ~$5-25); `claude ultrareview` CI-subcommand; hooks PreToolUse-deny/exit-2 gate (`prompt`+`agent` handler); promptfoo `llm-rubric` threshold CI-gate. V39 3-katmana oturur (dev-zamanı skill kalitesi · koşum-zamanı çıktı-doğrulama · merge/publish kapısı); m.9 ile "geçmeden push yok" deterministik. [D ultrareview/hooks/outcome-grader, K skill-creator blog 403]
- **Antitez (¬):** LLM-judge güvenilmez (consistency-bias paradoksu +33-41 puan, pozisyon-çevirme %25-50, öz-kayırma = m.7'nin makineleşmiş ihlali, "one token to fool" %80 sahte-pozitif, güçlü-Goodhart hiç-yapmamaktan kötü); tekrar kurtarmıyor (5 koşuma dek iyileşme yok; A5'in 11-15 tekrarı); `/ultrareview` ~26× maliyet; küçük-N/altın-cevapsız = anlamlı eval-set kurulamaz (en iyi 3 model örtüşen %95 GA'da); sonsuz gerileme (verifier'ı kim doğrular). Dürüst karşı-nüans: topluluk+çoğunluk κ'yı artırır ama maliyeti geri getirir. [K arXiv]
- **Kesişim:** Verifier mekanizmaları GERÇEK ve V39/K-020'ye oturur AMA **deterministik-önce + ayrı-grader (m.7) + kanıt-zorlayıcı-rubric + DANIŞMAN** olarak (insan m.31-Katman-1'e girdi), otonom LLM-judge kanon-kapısı olarak DEĞİL. Kilit: tez'in KENDİ birincil kaynağı (Anthropic) da "deterministik-önce + ayrı grader" diyor = antitezin hafifletmesi. Güçlü yakınsama.

### Aile D — git-worktree / paralel koşum
- **Tez:** `isolation: worktree` subagent frontmatter'ı native (oto-oluştur/sil, `git worktree lock`); üç izolasyon katmanı (worktree=dosya · subagent=context · agent-teams=koordinasyon); `--worktree` paralel oturum; `.worktreeinclude` gitignore'lu dosyalar için; Anthropic'in kendi ekibi 5 paralel worktree koşuyor. 4-şerit/çift-atlas'a oturur. [D docs, K scale-pratik]
- **Antitez (¬):** Multi-agent ~15× token, kötü-davranışta 10× katlanır; Anthropic'in KENDİ sınırı (paylaşılan-bağlam/yüksek-bağımlılık uygun değil) JARVIS'i (tek-flagship/tek-kişi = yüksek bağlam-paylaşımı) birebir tarif ediyor; Cognition "kırılgan, çelişen karar, tek-şeritli"; worktree "ucuz" miti (20 dk'da 9.82 GB, 5-7 tavan); worktree çakışmayı ÇÖZMEZ merge'e erteler (iki worktree'nin aynı dosyaya dokunduğunu uyaran araç yok); eşit-bütçe seri-derin çoğu zaman paralel-genişi yakalar. [K]
- **Kesişim:** Worktree izolasyonu DOSYA-YAZAN paralel iş için gerçek & native; ama JARVIS'in tek-kişi/tek-flagship/sırf-araştırma varsayılanında paralel çoğunlukla israf → kanıtlı istisna (m.25), sessiz varsayılan değil. **Sırf-araştırma atlas'ları (dosya yazmayan) izolasyona ihtiyaç duymaz** — çift-atlas ×2 en akut maruziyet. Dürüst not: worktree'ler `.claude/settings.local.json` izin-onaylarını + `.git`'i paylaşır → m.41 kilidiyle çapraz-test gerek.

### Aile E — Ünlü isimler / pratisyen desenleri
- **Tez:** Anthropic best-practices "Automate and scale" (paralel + `claude -p` + fan-out, "yatay ölçeklenir"); Writer/Reviewer düşman-doğrulama ("işi yapan onu notlandıran değil" = m.16/V26/m.7); "verify its work"+auto = gözetimsizin ön-şartı; orkestratör-işçi +%90.2/15× token; Willison "yargıyı paralelleştir"; Karpathy "AI'ı tasmada tut, seri kaybetmek"; Ralph loop; GitHub Actions cron gecelik-ajan (**m.30 kilidiyle KRİTİK ÇATIŞMA**). [D CC-docs, K anthropic/willison 403]
- **Antitez (¬):** Aynı pratisyenler çitliyor: Cognition "don't build multi-agents"; Anthropic 15× yalnız yüksek-değerli paralelleştirilebilir araştırmaya; Willison "dark factory işlemez, darboğaz İNCELEME"; HITL "opsiyonel değil"; Anthropic containment "insan-döngüde by-design"; headless yalnız iyi-kapsamlı tekrarlanabilir tek-görev; akademik "gözetim ölçeklenmiyor". [K]
- **Kesişim:** E-tez ve E-antitez YAKINSIYOR — her otomasyon-savunusu doğrulama-kapısı + izin-yüzeyi kısıtı + izolasyon şartına bağlı. Etkinleştiren ve çitleyen AYNI kaynak. Bulgu: benimse ama daima üç koşulla.

---

## §2 — Kaynak / isim tablosu

| Kaynak/isim | Konum | Ne diyor | JARVIS bağı | Etiket |
|---|---|---|---|---|
| Anthropic best-practices | code.claude.com | "Automate and scale": paralel + `-p` + fan-out, yatay ölçeklenir; Writer/Reviewer düşman-doğrulama | m.41 çoğaltma + m.16/V26 dış-doğrulaması | [D] |
| Anthropic permission-modes | code.claude.com | Auto-mode otonom-loop'u bloklar; bypass "koruma yok"; geri-alınamaz her modda kes-devre | m.42'nin birebir dış-aynası | [D] |
| Anthropic headless / goal / scheduled-tasks | code.claude.com | `-p`/`--bare`, `/goal` Stop-hook loop, `/loop` cron, `max_turns`/`max_budget_usd` | K-009 çekirdek primitifleri | [D] |
| Anthropic worktrees | code.claude.com | `isolation: worktree`, 3 izolasyon katmanı, `.worktreeinclude` | K-015 paralel-izolasyon | [D] |
| Anthropic ultrareview / hooks | code.claude.com | Bulut çok-ajan doğrulama (exit 0/1); PreToolUse-deny/exit-2 gate (`prompt`+`agent`) | V39 eval-gate mekanizması | [D] |
| Anthropic multi-agent-research | anthropic.com [403] | Orkestratör-işçi +%90.2/15× token; paylaşılan-bağlam işine uygun değil | m.25 ölçek-eşiği + tek-flagship uyarısı | [K] |
| Cognition "Don't Build Multi-Agents" | cognition.ai [403] | Paralel kırılgan, çelişen karar; tek-şeritli tut | m.30 fan-out ihtiyatı dış-doğrulaması | [K] |
| Simon Willison | simonwillison.net [403] | "Yargıyı paralelleştir" AMA "dark factory işlemez, darboğaz inceleme" | HITL = Salih tek-karar-verici (m.1-2) | [K] |
| Karpathy | No Priors/Sequoia [K] | "AI'ı tasmada tut"; darboğaz = taste/judgment/verification | Carvis KÖPRÜ rolü (m.17) + onay eşiği | [K] |
| Geoffrey Huntley (Ralph) | ralphex.com [K] | `while true` taze-bağlam loop; hafıza=dosya-sistemi; "deterministically bad" | git-log-hafıza + taze-kapsül devri örtüşür; sigorta şart | [K] |
| GitHub #68110/#73829/#77414/#68619 | github.com | 48+ ajan/1.5M token; 6.5s yetim; Stop-sonrası 300+ ajan; $6000 gece | Gözetimsiz-loop kaçak emsalleri | [D] |
| Akademik (oversight-doesn't-scale; SWE-Marathon) | arXiv [K] | Gözetim ajan-hızında ölçeklenmiyor; ultra-uzun-ufuk otonomi başarısız | m.42 ihtiyatına akademik zemin | [K] |
| skill-creator eval motoru / promptfoo | claude.com [403] / promptfoo.dev | Executor/Grader/Comparator/Analyzer; `llm-rubric` threshold CI-gate | K-016/K-020 eval-önce | [K] |

---

## §3 — CC-yetenek kararlarımızın kategori + kontrolü (yetenek merceğiyle)

Envanter (~40 karar, A-I grupları) yetenek merceğinden kategorize+denetlendi. Özet:

| Karar/kimlik | Yetenek sınıfı | Statü | Yetenek-taraması kontrolü (bu araştırmanın verdiği) |
|---|---|---|---|
| **m.30 ek fıkrası (canlı-ajan sınırı)** | otonomi-merdiveni | imzalı kanon (07-19) | ✅ **Doğru yerde:** sınır = prompt+kimlik devri (Routines); Aile B tez birincil-doğruladı. |
| **m.30 PreToolUse deterministik kilit** | guardrail/izin-yüzeyi | KURULDU+TEST PASS 07-19 | ✅ **Savunulabilir türün ta kendisi:** C-antitez "LLM-judge değil deterministik allowlist" diyor — JARVIS zaten deterministik. Genişlet, LLM-judge ekleme. |
| **m.42 ajan-yetki kanunu** | guardrail/otonomi | imzalı kanon (07-19) | ✅ Anthropic auto-mode tasarımının birebir aynası (Özgürlük≤Toparlanabilirlik, katı-başlangıç). |
| **Otonomi merdiveni tablosu (07-17 raporu)** | otonomi-merdiveni | rapor-KABUL | ⚠️ **B1 bunu büyük ölçüde TEKRAR haritaladı** (§4 bayrak-1); B1'in net-yenisi = birincil-doğrulama + antitez stres-testi. |
| **Gece-araştırma freni (sert-bütçe+tur-tavanı)** | guardrail/kota | ŞERHLİ-KABUL, tetikli | ⚠️ Doğru yön AMA sayılar sezgisel; istek-yolunda kill-switch + `max_budget_usd` sert-cap EKSİK (A-antitez #77414). |
| **Loop guardrails (3 tur·10 dk·sıfır-ilerleme)** | guardrail | ham fikir (dış-kaynak) | ⚠️ personal-os'tan türetilmiş, JARVIS verisiyle kalibre DEĞİL (§5). |
| **V26 örneklem-denetimi** | skill-verifier | koşum-DOĞRULANDI (41→32/9/0) | ✅ Aile C/E "ayrı düşman-doğrulayıcı" ile birebir; m.7 ile korunuyor. |
| **V39 otomatik-evaluator + K-020** | eval-gate | ham fikir + bekleyen | ⚠️ Mekanizma gerçek (Aile C tez) AMA C-antitez: otonom LLM-judge kanon-kapısı olarak DEĞİL, danışman/deterministik olarak. |
| **m.43 skill-doğum (≥3 tekrar)** | skill-verifier | imzalı kanon | ✅ Eval-önce standardı; S-A/S-B eval 3/3 koşum-ölçülü. |
| **K-015 worktree-izolasyon notu** | worktree-paralel | icra notu | ✅ Native (`isolation: worktree`, Aile D tez) AMA sırf-araştırma atlas'ına gerekmez (D kesişim); settings paylaşımı m.41-çapraz-test gerek. |
| **Ekip-vs-tek karar kuralı (kazanç>vergi)** | worktree-paralel | ilke (Salih'te) | ✅ Aile D antitez + m.25 birebir: paralellik kanıtlı istisna. |
| **Kararlı-prefix koşum deseni** | scheduled | karar 07-19 | ✅ Aile A curfew + A2 caching ile uyumlu; ilk loop'ta /usage ölçülecek. |
| **Routines per-tier kota (Pro5/Max15/Ent25)** | kota | envanter notu | ❌ **DOĞRULANMADI** (§5); güncel docs tamsayı yayınlamıyor. |

**Özel vurgular (envanterden):**
- **"Canlı ajan" sınırı:** m.30 ek (07-19) + merdiven tablosu (07-17 raporu L4-L5) + K-010 kartı (2 hafta ön-koşul, BLOKE) — üç yerde tutarlı tanımlı.
- **Guardrail:** PreToolUse kilidi (KURULDU+TEST PASS) + SessionStart hook (KURULDU) imzalı & saha-doğrulanmış; kill-switch/sert-cap tarafı henüz danışman.
- **Worktree:** GA (subagent+worktree) / preview (agent-view) / OFF (agent-teams); CWD dersi (kök-dışı başlatınca .claude/agents görünmüyor, çözüm K-011) koşum-doğrulandı.

---

## §4 — Yanlış/zayıf gördüklerim (dürüst bayraklar — KARAR ALMADAN, m.41)

1. **B1, 07-17 "3-model otomasyon-vizyon" raporunu büyük ölçüde TEKRAR haritaladı.** Otonomi merdiveni (RC→/goal→/loop→agent-view→Routines→Dispatch), guardrail-tier'ları ve yetki eşlemesi orada zaten vardı. B1'in NET-YENİSİ: (a) merdivenin birincil-kaynak doğrulaması (permission-modes doc = Anthropic'in kendi tasarımı m.42'yi dayatıyor), (b) antitez stres-testi (gerçek kaçak-emsalleri #68110/#77414), (c) eval-gate/verifier ve worktree ailelerinin derinleştirilmesi. Yeni-keşif kılığına sokmuyorum — merdivenin çoğu biliniyordu.
2. **En güçlü çapraz-aile bulgusu tez-antitez çatışması DEĞİL, "benimse-ama-çitle" yakınsaması.** Beş ailenin çoğunda iki şerit AYNI sonuca varıyor (yetenek gerçek + üç koşulla çitli). JARVIS bu üç koşulu zaten kodladığından, dürüst gözlem: JARVIS doktrinsel olarak İYİ hizalı; boşluk operasyonel (frenler dişli mi), doktrinsel değil.
3. **Kill-switch/curfew sayıları dış-kaynaklı, JARVIS verisiyle kalibre değil (V23/m.39).** 3-tur/10-dk = personal-os'tan; gece-bütçe/tur-tavanı sezgisel; **Routines per-tier kotası DOĞRULANMADI**. Bunlar ölçüm bekleyen hipotez, kanıt değil.
4. **Otomatik eval-gate'i KANON-KAPISI yapmak m.9/m.4/m.16/m.41 ile çelişir.** C-antitez haklı (danışman olmalı) — AMA C-tez'in KENDİ Anthropic kaynağı da "deterministik-önce + ayrı-grader" diyor. Savunulabilir eval-gate = JARVIS'in zaten kurduğu deterministik PreToolUse kilidi türü; onu LLM-judge çıktı-puanlamasına genişletmek tuzak olur.
5. **Çift-atlas ×2 varsayılanı en büyük maliyet-maruziyeti — ve B1'in KENDİSİ bunu araştırmak için 11 ajan (10 çift-atlas + envanter) koştu.** Canlı, öz-referanslı örnek (A2'nin #68110 ve 8-saat-stall'ı gibi). Sırf-araştırma atlas'ları izolasyona bile ihtiyaç duymaz (D kesişim). Dürüstçe kayda geçiriyorum.
6. **`--bare` CLAUDE.md/hook yüklemez; worktree'ler settings.local.json izin-onaylarını paylaşır.** Yani hız/determinism için `--bare` kullanan headless JARVIS otomasyonu kapsül/tüzük/kanon bağlamını YÜKLEMEZ; ve worktree'de verilen "don't ask again" tüm worktree'lere yayılır. İkisi de m.41 Dilim-1 kilidinin otomatik/paralel koşumda tutup tutmadığının ÇAPRAZ-TEST edilmesini gerektiriyor — yapısal-kilit doğrulama boşluğu.
7. **"Gözetimsiz ≠ canlı ajan" ince ayrımı operasyonel karıştırmaya açık.** `claude --bg` background session gözetimsiz koşar ama yine K-009 tarafı (yerel, senin-promptun, senin-başlattığın). Sınır prompt+kimlik devri, gözetim değil. Envanter bunu doğru yakalıyor ama pratikte "gözetimsiz koşuyor öyleyse canlı ajan" diye karıştırılabilir — sınır tanımı gözetime değil devre bakar.

---

## §5 — V26 örneklem-denetimi

| Ajan/şerit | Denetlenen iddia | Sonuç | Etki |
|---|---|---|---|
| Envanter + A-tez | "Routines per-tier kota Pro5/Max15/Ent25" | **DOĞRULANMADI** — Nis-May2026 basınından, güncel docs tamsayı yayınlamıyor | [X]/[?]; §3'te ❌, karar dayanağı yapılmadı |
| A-antitez | "#77414 Stop'tan sonra 300+ ajan" | **Doğrulandı** — GitHub issue birincil | [D]; kill-switch istek-yolu argümanının çekirdeği |
| B-antitez | "bypassPermissions koruma sağlamaz" | **Doğrulandı** — permission-modes doc birincil alıntı | [D]; kanon-repo felaket-potansiyeli teyitli |
| C-antitez | "one token to fool %80 sahte-pozitif" | **Arama-özeti** — arXiv 2507.08794, birincil-fetch yok | [K]; eval-gate danışman-önerisi bu tek sayıya dayanmıyor |
| A/E-tez | "orkestratör-işçi +%90.2 / 15× token" | **Arama-özeti** — anthropic.com 403 | [K]; A2'de de aynı [K]; tutarlı |
| Guardrail envanter | "loop 3-tur/10-dk" | **Dış-kaynak** — personal-os, JARVIS verisiyle kalibre değil | [K]; §4 bayrak-3'e taşındı |
| Egress | anthropic.com/eng · cognition.ai · simonwillison.net · arXiv PDF'ler | **403/site-engeli** | İlgili bulgular [K]; code.claude.com doğrudan [D] |

---

## §6 — Cevaplanmamış sorular (karar biriktirilmedi — m.41)

1. **PreToolUse deterministik kilidi `--bare`/worktree/headless altında da tutuyor mu?** — bu modlarda CLAUDE.md/settings farklı yüklenir; m.41 Dilim-1 kilidi çapraz-test edilmeli (§4 bayrak-6).
2. **İstek-yolunda kill-switch + `max_budget_usd` sert-cap herhangi bir gerçek otomasyon koşumuna bağlanmalı mı?** — post-hoc Stop atomik değil (#77414); gece-freni şu an danışman.
3. **m.30-uyumlu çekirdek headless yol yerel `claude -p` + PreToolUse + sert-cap olarak sabitlensin mi, Routines K-010'a mı bırakılsın?** — Aile A tez bu ayrımı öneriyor ama karar Salih'te.
4. **V39 eval-gate deterministik/rubric/danışman olarak mı sınırlansın (LLM-judge kanon-kapısı değil)?** — C-antitez + C-tez'in kendi kaynağı bunu işaret ediyor; m.9/m.16 ile çelişki-kapısı konusu.
5. **Çift-atlas ×2 varsayılanı m.25 kanıtlı-istisnasına daraltılsın mı; sırf-araştırma atlas'ları worktree-izolasyonsuz mu koşsun?** — en akut maliyet kaldıracı, öz-referanslı (§4 bayrak-5).

---

*Bu rapor B1 kartının çıktısıdır (m.41 yan-oturum): 5 aile × 2 şerit + 1 envanter = 11 Atlas koşumu, çift-atlas (tez ∧ ¬tez). Karar ALINMADI, kanon DEĞİŞMEDİ; yalnız bulgu + kategori/kontrol + dürüst bayraklar sunuldu. Sıradaki kuyruk: B2 (superpowers desen paketi — "bu tam olarak nedir" açıklamalı).*
