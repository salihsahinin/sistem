# Alt-ajan tanımı şablonu v0 (2026-09-17, deneysel m.29) — taslak; kanon yeri Salih hükmüyle (`core/sablonlar/` ∨ skill referansı)

*Kaynak: atlas-kosum sentezi `sentez-altajan-uretim-usulu-2026-09-17.md` (43 sağlam madde) + atlas'ın 9 commit'lik dersleri. İlke: hazırı temel al (atlas'ın işleyen parçaları alınır, süsü alınmaz); üç katman Karar 89; alan ajanı = Jarvis alt-ajanı, ayrı repo yok (Karar 93 M7-1, Karar 94 EK-5).*

## Frontmatter (resmî alanlar; AS-OF 2026-09-17 sub-agents belgesi)
```yaml
---
name: <küçük-harf-tire>            # zorunlu; ':' yasak
description: <NE yapar · NE ZAMAN çağrılır (tetik kalıpları) · NE ZAMAN çağrılmaz>   # zorunlu; tüm ajanlar toplam 15.000 token
tools: <pozitif liste>              # Jarvis ilkesi: en-az-yetki (dış çerçeve yok, iç kanıt Karar 91 kilit vakaları)
disallowedTools: <varsa>            # tools'tan ÖNCE uygulanır
model: sonnet | opus | inherit      # işçi = sonnet; lider = opus (effort medium sabit, Karar 89); çağıran taraf override edebilir
effort: low | medium                # işçi düşük-orta (Salih 08-15 token kuralı)
memory: project | user | local      # yalnız durum taşıması gereken ajanda; lider durum taşımaz (m.42 d)
hooks: <ajana özel PreToolUse/PostToolUse/Stop>   # İB-83 okuma kısıdı settings'te zaten global
color: <8 sabit renkten>
---
```
Şablona **girmeyen** alanlar (gerekçe): `skills` (tam içerik enjekte eder, bağlam bütçesini patlatır; gerekirse emirde pointer) · `isolation: worktree` (Karar 95 yan-oturum usulüne çakışır) · `initialPrompt`/`background` (Agent aracı çağrısı kararıdır, tanım değil) · `omitClaudeMd` (Jarvis alt-ajanı kanon kurallarını görmeli).

## Gövde (≤ ~8 KB; bölümler XML/başlık ayrık; "minimal ama tam")
```
# <AD> — <tek cümle rol>
## Kimlik ve katman        (işçi | lider; kimden çağrılır; işçi liderden pahalı olamaz — Karar 89; MODEL KURALI BURADA, HTML yorumda değil)
## Görev sözleşmesi         (girdi tipleri · çıktı biçimi ≤N token özet + "açık soru:" satırı · done yüklemi boolean · teslim yolu `cc/rapor/YYYY-MM/…` ∨ emirdeki yol)
## Kanıt disiplini          (atlas'tan AL: kanıt hiyerarşisi birincil > ikincil > model-hafızası · D/K/X etiketi · URL + ≤15 kelime alıntı + bölüm · rakam kaynaklı, kestirim [?] · AS-OF damgası Karar 68)
## Örneklem-denetimi        (atlas'tan AL: V26 — son üçlük ≥1 kaynak + tüm sayısal iddialar + ≥1 URL'siz iddia; yapan ≠ ölçen Karar 86 D3)
## Erişim arızası kuralı    (atlas dersi: 403/paywall/bot-engeli → X + "ERİŞİLEMEDİ" sayımı; alternatif adres arama yok, soruya düş; koşumu durdurmaz)
## Sınırlar                 (kapsam_dışı zorunlu · yazma izni pozitif liste · git: pathspec-only ∨ yok · push yok · kanon/ yazımı yok · karar yetkisi yok)
## Dallar                   (≤5; "eğer … → …"; D-KATMAN1: kural değişikliği gerektiren nokta → DUR)
## Bütçe                    (araç çağrı tavanı · dönüş ≤2k token · aile ≤3)
## Ad eşitliği (sabit satır) (Karar 93: Jarvis = ana-sıra ajan; tarihli metinlerde Carvis = Jarvis; sistem = depo)
```
Atlas'tan **alınmayan**: FELSEFİ TEMELLER (kategori-kuramı, ontolojik yığın) · EPİSTEMOLOJİK ÖZ-FARKINDALIK · Aşama 5 `docs/research/…` çıktı yolu · Aşama 1 üçlemesi (FELSEFİ TEMELLER tekrarı) · akademik makale modu (yalnız atlas'a özgü, şablona değil). **Salih hükmü bekleyen:** DALGA PROTOKOLÜ (MECE sorusu) — hakem çelişkili.

## Üretim usulü (skill-kapisi ile aynı ağaç; ajan = skill'in ajan-türlü kardeşi)
1. **K0 gerek:** tekrarlanan ∧ araç-zincirli ∧ ayrı bağlam gerektiren iş mi? Mevcut ajanla (atlas, general-purpose, Explore) kapsanıyor mu? Kapsanıyorsa `RET-0`.
2. **Baseline (zorunlu, eval-önce):** aynı işin ajansız/genel-ajanlı bir koşumu ölçülür (v_skill_kosum'a benzer satır: model · token · araç çağrısı · sonuç etiketi).
3. **İnşa:** bu şablon; frontmatter + ≤8 KB gövde; `tools` pozitif liste; katman satırı.
4. **K2 topraklama:** ilk canlı koşum + İB-83 kütüğü boş ∧ araç tavanı aşılmadı ∧ done yüklemi tuttu; koşum satırı `v_skill_kosum` (ajan türüyle).
5. **K3 biçim:** büyük harf = kod (pre-commit teli `.claude/agents/*.md`'yi de saymalı — İB borcu) · Türkçe gövde · description standardı (skill-standardi.md).
6. **Kayıt:** katalog satırı (`.claude/skills/README.md` "ajanlar" bölümü ya da ayrı `.claude/agents/README.md`) · defter tek satır · her iyileştirme rol metnine commit (ajan-metodolojisi §6).

## İlk vaka: hakem/tester ajanı (Karar 98)
`name: hakem` · işçi katmanı sonnet ∨ hakem rolü opus medium (çağıran belirler) · `tools: Read, Grep, Glob, Bash(salt-okur), WebFetch` · girdi: yalnız ölçülecek veri (emrin yazarı/beklentisi verilmez — Karar 86 D3-i) · çıktı: iddia × sınıf (sağlam/daraldı/düştü/çelişkili) + sayım · baseline: bugünkü hakem koşumu (Opus 5 medium, 7 araç çağrısı, 116k token) ve İB-66 (55,6 → 44,4). Eval seti: Ö1 (promptfoo v0.123.0) üstünde.
