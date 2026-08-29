# İB-55 — K-010 A3 kapısı: "hangi araçla → hangi güvenceyle" (araç-güvence yazımı)

**AS-OF 2026-08-29 (icra devam oturumu, Fable) · kaynak: entegrasyon masası K1-7 → Karar 76 E6 (a) → İB-55 · malzeme: pano K-010 A2/A3 kapı tanımları · KILAVUZ araç-sınırı (E-1, Karar 76) · `gnhf --help` (canlı, 08-29) · `.claude/hooks/pretool-core-tel.sh` + `pretool-ajan-fren.sh` + `cc/workflow/fren-sablonu.js` (İB-54) · `cc/rapor-2026-07-29-6.md` §3.5-3.6, §4.3 (/loop, /goal, headless bayrakları — [D-belge]) · `kuyruk/build-tartisma-notlari.md:97` (gece-loop talebi + m.16 notu) · deneysel m.29. Bu bir YAZIM teslimidir; A3 kapısını GEÇMEZ — kapı kanıtla geçer (Salih 07-22: kapı = kanıt, takvim değil).**

*Ne bu:* K-010 A3 = kontrol-devri kapısı: "/goal 1 OK ∧ /loop durma-koşullu 1 OK ∧ sabit-promptlu Routine 3 OK (usage-log kanıtlı)"; bağımlılık A1∧A2→A3. Kapı "ezilmez", ama hangi araca hangi güvence bağlanacak yazılı değildi (K1-7 şerhi: "kapı-ezme değil yazım sorusu"). Aşağıdaki tablo her otonom aracı beş güvence ekseninde bağlar.

## 1. Güvence eksenleri (A2'den türetilmiş, m.38 lojik form)
G1 **Kanon kilidi** — otomat `core/ · CLAUDE.md · .claude/ · tüzük · defter`e yazamaz (PreToolUse teli + settings deny; KILAVUZ E-1 "hiçbir otomat kanon dosyalarına doğrudan yazamaz").
G2 **Sert bütçe** — yazılı token ∨ iterasyon ∨ süre ∨ $ tavanı; aşımda DURUR (fren hook UYARI 36 / DURDUR 72 ajan; gnhf `--max-iterations/--max-tokens`; headless `--max-budget-usd`).
G3 **Durma koşulu** — done-yüklemi yazılı (m.38): gnhf `--stop-when`, `/goal` koşulu, `/loop` durma-koşulu; koşulsuz loop YOK.
G4 **İzolasyon** — worktree ∨ ayrı klon; ana çalışma ağacına dokunmaz (treehouse/`--worktree`); push KAPALI (m.9 Salih beyanı).
G5 **Kanıt izi** — koşum usage-log/transkript + hareket kütüğü + `fren-olay.jsonl`; kanıt yoksa koşum SAYILMAZ (A1 sicil mantığı).
Lojik: otonom-koşum-izinli(araç) ↔ G1 ∧ G2 ∧ G3 ∧ G4 ∧ G5 ∧ (A3-kapısı-açık ∨ tek-emirlik-araştırma-görevi).

## 2. Araç × güvence tablosu
| Araç (yüzey) | G1 kanon kilidi | G2 sert bütçe | G3 durma koşulu | G4 izolasyon | G5 kanıt | A3 kapısındaki rolü | Durum 08-29 |
|---|---|---|---|---|---|---|---|
| **gnhf** ("good night, have fun"; `--agent claude`) | PreToolUse teli + deny (worktree'de de `.claude/` proje ayarı yüklenir — `--setting-sources` atlatması test edilmedi `[?]`) | `--max-iterations N` ∧ `--max-tokens N` ∧ `--max-rate-limit-wait` YAZILI zorunlu | `--stop-when "<koşul>"` zorunlu (koşulsuz gnhf YASAK) | `--worktree` zorunlu; `--push` KAPALI; `--current-branch` YASAK | gnhf kendi iterasyon günlüğü + hareket kütüğü (transkript) | "/loop durma-koşullu 1 OK" kanıtının aracı olabilir (durma-koşullu uzun koşum) | KILAVUZ E-1: KOŞULLU (worktree ∧ yazılı bütçe ∧ push kapalı) — bu satır o koşulun yazımıdır |
| **/loop** (CC yerleşik; sabit ∨ kendi-seçtiği aralık) | aynı oturum → teli + deny geçerli | oturum bağlamı = bütçe (KB-52 128K uyarısı); $ tavanı yok → **bütçe yazılı süre/aralık** | durma-koşulu prompt'ta yazılı; `Monitor` yoklamadan kaçınır | ana ağaçta koşar → yalnız SALT-OKUR/eklemeli görevler | transkript (baglam-seyir) | **A3 kanıtı #2** (/loop durma-koşullu 1 OK) | araç var [D-belge]; **sessiz arıza yolu:** `disable-model-invocation: true` skill'ler /loop'ta düz metin olarak geçer (rapor-6 §4.3) → gece-loop tasarımında ritüel skill'leri güvenilmez |
| **/goal** (koşul sağlanana dek) | aynı | aynı | koşul = done-yüklemi; `tools/verify-push.py` gibi deterministik doğrulayıcı ile (loop-eng Faz 2) | ana ağaç → salt-okur/eklemeli | transkript | **A3 kanıtı #1** (/goal 1 OK) | araç var [D-belge]; ilk kanıt koşumu YAPILMADI |
| **Routine / schedule** (bulut, sabit prompt) | bulut klonu: hook'lar/deny yüklenir mi `[?]` (Cowork-benzeri parmak-izi gerekir, KB-34 sınıfı) | routine başına sabit prompt + bütçe | tek-atış (koşum biter) | origin klonu; push? → **KAPALI** varsayılan | routine log + usage | **A3 kanıtı #3** (sabit-promptlu Routine 3 OK) | araç var; kanon-yazımı YASAK (yan-oturum karar almaz, Karar 71) |
| **claude -p** headless (`--output-format json --json-schema --max-budget-usd --permission-mode --tools`) | `--tools` + `--permission-mode` ile dar; teli/deny proje ayarından | `--max-budget-usd` YAZILI | tek koşum; done = çıktı şeması doğrulandı | worktree ∨ klon | stream-json çıktısı + hareket kütüğü | Model-3 resmî yol (İB-57 HEADLESS-ADAY sınıfları buraya iner) | bayrak seviyesinde hazır [D-ölçüm --help]; pilot A3 sonrası |
| **Workflow / Agent alt-koşum** (bugünkü fiilî headless) | işçi ajan kanon yazmaz (emir şablonu + teli) | `fren-sablonu.js` AJAN_TAVAN 36 / DALGA 12; hook UYARI 36 / DURDUR 72 | manifest + schema (done = schema dolu) | aynı ağaç, dosya-ayrık ayak izi (İB-63 atlası bunu formalize ediyor) | `amb_olgu_kosum` + `fren-olay.jsonl` | A3'ün ÖNKOŞULU değil; A2 güvencesinin canlı kanıtı (fren 36'da tetiklendi 08-29) | CANLI (İB-54) |
| **treehouse** (worktree havuzu/lease) · **no-mistakes** (kapılı ship) | worktree'de teli/deny | PR kapısı | pipeline sonu | worktree | PR #2/#3 | G4'ün aracı | KILAVUZ E-1: SERBEST |

## 3. A3 geçiş planı (kanıt sırası; kapı kanıtla açılır)
1. **A1 ∧ A2 teyidi** (önkoşul): A1 sicil (5 ardışık OK açılış-senkron) — `senkron-log` son kaydı 08-04 FAIL-ff, Mac'te gece-senkron KOŞMUYOR → A1 fiilen AÇIK DEĞİL; A2: teli PASS (08-29 hook Bash yazımını doğru engelledi, Karar 77) ∧ fren canlı ∧ sert bütçe yazılı (bu belge) ∧ revert tatbikatı (M-9 [revert] 08-29 = fiilî tatbikat, plansız).
2. **/goal 1 OK:** hedef `python3 tools/verify-push.py` PASS ya da `katman-hatti --json cikis=0` (deterministik evaluator); salt-okur görev; kanıt transkript + hareket kütüğü.
3. **/loop durma-koşullu 1 OK:** aralık ≥20 dk, durma-koşulu = "v_silver_saglik_son ERROR 0" gibi ölçülebilir yüklem; ritüel skill'i ÇAĞIRMAYAN prompt (E6 sessiz arıza).
4. **Routine 3 OK:** sabit prompt "katman-hatti --json → JSON'u dosyaya" sınıfı; push kapalı.
5. Hepsi kanıtlıysa → A3 AÇIK; ilk otonom pilot İB-57 HEADLESS-ADAY listesinden (Salih seçer).

## 4. Boşluklar / dürüstlük (m.39)
- "gece-loop m.16 raporu 08-27/29 blokları" (defter :221, :236 pointer'ı) repo taramasında BULUNAMADI (`grep gece-loop` yalnız 07-29 kayıtlarını buldu) — malzeme olarak 07-29 rapor-6 + build-tartisma-notlari:97 kullanıldı; 08-27 bloğu varsa pointer düzeltilmeli.
- `--setting-sources user,local` ile deny+hook'ların birlikte düşmesi (rapor-6 E8) test edilmedi — G1'in en zayıf halkası; K39 taraması kalemi.
- Routine/bulut yüzeyinde hook yüklenmesi ölçülmedi `[?]`.
- A1 sicili Mac'te sıfırdan başlar (schtasks Windows dönemi) — K-009 kalan.
