# sistem — çok-ajanlı depo (Karar 101, 2026-09-18)

**Ne bu:** Salih'in ajan sistemi. Depo = N ajan + ortak kanon. Her ajan kendi dizininde çalışır, kendi kanonunu (`AGENTS.md`, `CLAUDE.md` symlink) ve hafızasını (`core/`) taşır; ortak kural kökteki `AGENTS.md`'de (≤25 satır), tam metin `jarvis/core/tuzuk-v0.md`. Eski ad `jarvis` (tek-ajan depo, 2026-07-10 → 09-18); tarihçe git log'da, Friday tarihi `git subtree` ile korundu.

## Ajanlar
| Ajan | Dizin | Rol | Model | Oturum |
|---|---|---|---|---|
| **Jarvis** | `jarvis/` | ana-sıra ajan + kanonların bakıcısı; Salih'in tek temas noktası; işi domain-lider seviyesine kadar böler (tüzük m.44) | Fable | Claude Code, cwd `~/sistem/jarvis`, worktree **kapalı** |
| **Friday** | `friday/` | domain-lider (proje-ölçekli icra: araştırma, refactor, doküman, ölçüm; Sonnet işçi filosu) | Opus 5 medium | Claude Code, cwd `~/sistem/friday`, worktree **kapalı**; emir `cc/gelen/`, dönüş `cc/giden/` |
| **Solon** | `evals/` | alan ajanı: LLM/ajan değerlendirme mühendisliği — öğrenme + ürün + Salih'le sohbet (Karar 105) | Sonnet 5 medium + eskalasyon (Salih beyanı) | Claude Code, cwd `~/sistem/evals`, worktree **kapalı**; ders iskeleti `cc/gelen/`, dönüş `cc/giden/` |
| **Aeneas** | `guvenlik/` | alan ajanı: ajan güvenliği (Karar 105) | Sonnet 5 medium + eskalasyon | cwd `~/sistem/guvenlik`, aynı usul |
| **Simonides** | `baglam/` | alan ajanı: bağlam penceresinin matematiksel modellemesi (Karar 105) | Sonnet 5 medium + eskalasyon | cwd `~/sistem/baglam`, aynı usul |
| **Euclid** | `hesaplama/` | alan ajanı: MIT 6.006 + 6.042J + matematik felsefesi (Karar 105) | Sonnet 5 medium + eskalasyon | cwd `~/sistem/hesaplama`, aynı usul |
| hakem | `jarvis/.claude/agents/hakem` (ortak) · `<alan>/.claude/agents/hakem` (alan perspektifli) | maskeli, bağımsız, salt-okur değerlendirici; V26 zorunlu (Karar 103 M1 · 105 M1) | Sonnet 5 + eskalasyon | `Agent` aracı |
| işçiler | ajanın alt-çağrısı | tek görev, atılabilir | Sonnet | `Agent` aracı; okuma kilidi hook'la |

Yeni alan ajanı: `jarvis/tools/alan-ajani-dogur.py <spec>` (`sablonlar/ajan-iskelet/`, doğum belgesi + bakım-maliyeti satırı zorunlu, Karar 104 M5); şerit taşıma `git mv` Salih eli.

## Kök
`AGENTS.md` ortak kanon · `CLAUDE.md → AGENTS.md` · `sablonlar/` ortak şablonlar (görev-fonksiyonu · geri-dönüş v0 · devir-birimi v0 · A1 lojik blok · charter iskeleti) · `bin/hook-dispatch.sh` tek hook girişi (cwd → ajan hook'ları) · `.claude/settings.json` dispatcher kayıtları · `ogrenme/` Salih'in öğrenme şeritleri (ajanlara kapalı) · `.gitignore` kök kuralları (ajan kuralları `<ajan>/.gitignore`).

## Sahiplik (kim neyi yazar)
genel kural → kök `AGENTS.md` (Jarvis yazar, Salih imzalar) · ajan kuralı/kimliği → `<ajan>/AGENTS.md` (Jarvis yazar, Salih imzalar; ajan kural yazamaz) · ajan hafızası → `<ajan>/core/` (ajanın kendisi) · karar defteri → `jarvis/kuyruk/senaryo-defteri.md` (tek defter; diğer ajanlarda kural adayı) · proje kanonu → ileride `projects/<ad>/AGENTS.md`.

## İzolasyon (mekanik)
Friday `.claude/hooks/okuma-izin.sh`: kendi dizini + kök kanon dosyaları + `sablonlar/` serbest, `jarvis/**` ve ev dizini kapalı (test `okuma-izin-test.sh`). Jarvis `.claude/hooks/pretool-altajan-okuma.sh`: alt-ajan kapsül/pano/defter/kütük/`friday/` okuyamaz. Kanıt: her ajanın `veri/bronz/hareket-olay.jsonl` kütüğü + `talimat-yukleme-olay.jsonl` (Friday bağlamında Jarvis satırı 0 = izolasyon geçerli, Karar 101 geri-açma koşulu).

## Okuma sırası (ajan isen)
1. kök `AGENTS.md` → 2. kendi `<ajan>/AGENTS.md` → 3. kendi `core/durum-kapsulu.md` → `core/pano.md`. Jarvis için ayrıca `jarvis/README.md` + `jarvis/KILAVUZ.md`.

Lisans MIT (`jarvis/LICENSE`). Remote private (Salih).
