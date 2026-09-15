# Skill-Üretim Şeması v1.1 — TASLAK (2026-09-15; Salih emri: "skill oluşum şemasını ve sürecini bu bağlamda güncelle"; masa-12 M3 hükmüyle `core/skill-uretim-semasi.md`'ye işlenir)

*Kaynak: md→skill atlas koşumu (tez A1-A3 + antitez + hakem, `cc/rapor/2026-09/rapor-2026-09-15-md-skill-*.md`), V26 sondaj (birincil belgeler, çekim 2026-09-15), Kun Chen L8 transkripti (2026-06-20). Rakamlar kaynaklı; kestirim `[?]`.*

## 0. Değişen ne (v1 → v1.1) — tek bakış
| Kalem | v1 (08-15) | v1.1 (taslak) | Kanıt |
|---|---|---|---|
| Aday KAYNAĞI | aşağıdan (tekrar sayacı k_W) ∨ yukarıdan (Salih emri) | **+ S-kaynak: bağlam-uzayı madenciliği** — her seans yüklenen md'lerdeki koşullu/prosedürel bölümler sistematik aday olur | Anthropic memory belgesi: "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill or a path-scoped rule" (D) · Kun Chen L8 16:12-18:32 (koşullu bilgi → skill) |
| Üçlü yerleşim kuralı | CLAUDE.md ↔ skill ikilisi | **üç yuva:** (1) her seans gerekli olgu/kural → CLAUDE.md (≤200 satır hedefi) · (2) yalnız belli dosya/dizinle çalışırken gerekli → `.claude/rules/*.md` + `paths:` · (3) yalnız belli iş türünde gerekli prosedür → skill (description tetikli) | code.claude.com/docs/en/memory (D): rules `paths:` frontmatter; skill "task-specific instructions that don't need to be in context all the time" |
| K0 Y2 | `kural∈LAZY` | **Y2' koşullu-yük := bölüm her seans yükleniyor ∧ (koşul-dili ≥ eşik ∨ adım ≥3) ∧ okunma-oranı düşük** — `tools/baglam-skill-aday.py` skoru (deneysel, katsayı kalibresiz [?]) | Progressive disclosure: metadata ~100 token/skill, gövde <5k token yalnız tetiklenince (platform docs, D) |
| İNŞA — kaynak | eval-önce | **+ "kendinden-üretilen skill" freni:** md'den mekanik çıkarma yeterli değil; ≥3 eval + skill'siz baseline zorunlu kalır | SkillsBench abstract (D): kuratörlü skill +16,6 pp; "en fazla 3 modül"; self-generated ≈0 iddiası ikincil (K) |
| K3 biçim | F1-F5 | **+ F6 hazine-yükü:** aktif skill sayısı × ~100 token metadata her seans yüklenir; hazine tavanı 7.380 char (KB-19) korunur, her yeni skill bir emekli-adayla dengelenir (FIFO deseni, Karar 92) | platform docs (D): metadata her zaman yüklü |
| Yürütme sözleşmesi | tür-demeti | **+ determinizm katmanı:** deterministik adım = script (low freedom, "run exactly this"), plan-validate-execute deseni; skill metni model-yorumlu kalır → sorgulanabilirlik = script çıktısı + kütük | best-practices (D): "Prefer scripts for deterministic operations", "plan-validate-execute" |
| Görev icrası bağı | — | skill = kalıp-prompt; İB-84 A1-A3 görev formatı (md+lojik → json → python) skill gövdesinin "script" katmanıyla aynı eksen: A3'e ulaşan görev = script'li skill adayı | Salih 09-15 beyanı + best-practices freedom ölçeği |
| Sürüm/dağıtım | commit | **+ PR akışı (Karar 95):** skill üretimi yan oturumda yapılıyorsa branch + PR, merge ana-sıra | Karar 95 |
| Ölçüm | 10 koşum sonra kapı analizi | **+ bağlam-izleme:** `InstructionsLoaded` hook ile hangi md'nin ne zaman yüklendiği kütüklenir (session_start / nested / path_glob / compact) → S-kaynak skorunun "okunma" ayağı gerçek veriye oturur; İB-81 ön-koşulunu da karşılar | code.claude.com/docs/en/hooks (D): InstructionsLoaded matcher listesi |

## 1. S-kaynak süreci (yeni; deterministik + Salih hükmü)
1. **Madencilik (script):** `python3 tools/baglam-skill-aday.py --cikti raporlar/…` → 40 aday, skor = boyut × koşulluluk × prosedür × (1 − okunma). Tetik: seans kapanışında 5 kapanışta bir ∨ sıcak katman bayt tavanı aşımı ∨ Salih emri.
2. **Yerleşim kararı (kural, insan-okur):** aday bölüm için üç soru — her seans gerekli mi? (evet → CLAUDE.md'de kal, kısalt) · yalnız belli dosyalarla mı? (evet → `.claude/rules/` + `paths:`) · yalnız belli iş türünde mi? (evet → skill adayı, K0'a gir).
3. **K0-K3 ağacı** değişmeden koşar (kapsanmış? → EVRİM; eval-önce; topraklama; biçim). Md'den taşınan bölüm kaynakta **pointer + tek cümle** bırakır (m.8 silme yok; m.20 pointer).
4. **Hazine dengesi (F6):** yeni skill girişi = hazine char toplamı ve aktif skill sayısı yeniden sayılır; tavan aşımında BAKIM emekli-adayı seçilir.
5. **Ölçüm:** taşınan bayt × seans (bağlam tasarrufu, InstructionsLoaded kütüğünden) · tetiklenme isabeti (skill çağrıldı mı, çağrılmalıyken çağrılmadı mı — BAKIM-KK "tetiklenmeme sinyali") · 5 seans sonra karşılaştırma.

## 2. m.16 çelişki taraması
- m.43 skill-doğum (tekrarlayan-küme → aday): çelişki yok; S-kaynak ikinci giriş kapısı, sayaç kuralı aynı.
- Karar 92 FIFO / KB-19 hazine tavanı: uyumlu; F6 aynı tavanı skill sayısına bağlar.
- m.20 pointer ilkesi: uyumlu; taşınan içerik yerine pointer kalır.
- İB-81 (erteleme aynen): dokunulmuyor; yalnız ön-koşulu (bağlam-izleme) InstructionsLoaded ile ucuzlar — İB-81 tetiği yine Salih beyanı.
- Kun Chen "haftalık toplu düzenleme + sabit token bütçesi" ↔ Anthropic "aynı hata ikinci kez → hemen ekle": jarvis'te ikisi de var (kapanış ingest turu = toplu; hafıza feedback = anlık). Çelişki değil, iki ölçek.
