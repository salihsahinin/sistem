# Pipeline Manifesti — ANAKRONİZM FRENİ (Salih Katman-1 yasağı, seans-16) + S-0 liderlik-tablosu güncel-model taraması — 2026-08-26

*Salih emri (01:1x, aynen): "1 yap ve bundan sonra sistemde anakronizm yapmayı yasaklıyorum bunu önleyecek şekilde nasıl yapacağını araştır atlasları koş artıları implement et."*

**Okuma (Carvis):** "1 yap" = önceki cevabın 1. seçeneği: Multi-SWE-bench/SWE-bench-Multilingual/Aider liderlik tablolarında 2026 model satırlarını çekip 2025-04 tablosuna oranlamak (tek Sonnet ajanı, ~5 dk) → S-0. "anakronizm yasak" = **Katman-1 kural, Salih beyanıyla VERİLDİ** (defter Karar 68) — araştırma kuralı sorgulamaz, "nasıl mekanikleştirilir"i arar. "artıları implement et" = Katman-2 icra (script/şema/lint/wiki/damga); kanon metni değişikliği (CLAUDE.md 7.139 B / 7 KB bütçe DOLU, tüzük, core/) → Salih kararına kalem.

## Çelişki kapısı (m.16) — hüküm: ÇELİŞKİ YOK, MEVCUT KURALLARI GÜÇLENDİRİR
Zaman-kayması freni (seans-acilis §0, 08-15) · silver tazelik kapısı (Karar 62) · halüsinasyon v2 tazelik · anahtar kaydı SCD-2/çift-zaman · ambar bitemporal · m.39 rakam damgası · hakem sürüm yeniden-çekme (08-22): hepsi aynı yönde; yeni kural bunları "zaman-bağımlı HER iddia" düzeyine genelleştirir. m.8 (silme yasağı) ile uyum: bayat kayıt silinmez, damgalanır. Tek gerilim: **CLAUDE.md bütçesi dolu** → kural satırı için "bir satır girer, bir satır çıkar" kararı Salih'in (KB kalemi).

## Koşum-önü manifest kapısı (KB-08)
`cc/pipeline-*.md` (11) + `git log -15` + `rg -i "anakroniz|tazelik|as-of"`: anakronizm konulu koşum YOK; en yakın: halüsinasyon paketi (08-15/16, v2 bayrağı), hafıza-teknik atlası (08-17, LongMemEval zaman-farkındalı sorgu), anahtar kaydı (08-15). Canlı-oturum: son commit d803e38 bu oturumun → paralel oturum YOK.

## Görev tablosu
| Rol | Şekil | İş | Intake | Teslim | Durum |
|---|---|---|---|---|---|
| S-0 | scout (tek Sonnet, atlas tipi, ≤10 erişim) | Multi-SWE-bench · SWE-bench Multilingual · Aider polyglot liderlik tablolarında GÜNCEL (2026) model satırları; Go/TS/Python(+Java/Rust) için 2025-04 Tablo-4'e oran; as-of + URL; bulunamadı meşru | prompt (manifestte özet) | `cc/rapor-2026-08-26-3.md` (ajan dönüşü + Carvis notu) | DONE 01:3x |
| S-1 | scout (m.40b 3 aile × 4 = 12 işçi) | A LLM zamansal zemin · B veri/kayıt katmanı (bitemporal/as-of/TTL) · C ajan/işletim pratiği (damga · doğrula-önce · lint · hazır araç) | `cc/gorev-2026-08-26-2.md` | `cc/rapor-2026-08-26-2.md` | DONE 01:5x |
| G-1 | sentez (Carvis) | anakronizm taksonomisi × Jarvis vakası · tazelik-sınıfı kuralı · damga kuralı (rapor + CHAT) · kayıt şeması · deterministik denetim · borç ayrımı | S-0 + S-1 | rapor §Sentez S1-S5 | DONE 02:0x |
| SH-1 | ship (Katman-2 artılar) | aday: `tools/anakronizm-denetim.py` (tarihsiz sürüm/sayı/"güncel" kalıpları lint + bayatlık testi) · damga şablonu · wiki sayfası · skill/emir şablonlarına as-of alanı · kod-envanter'e kesim-tarihi satırı · kayıtlar | G-1 | commit'ler (lint · kesim tablosu · hook satırı · wiki · SKILL satırı · kayıtlar) | DONE 02:1x |
| SH-2 | masaya | Katman-1 kalemler (CLAUDE.md satırı · tüzük maddesi · kanon metni damga zorunluluğu) ledger | G-1 | KB-66/67/68 (tablo exit 0) | DONE 02:1x |
| T | teslim | beyan + insan-yüzü rapor + `open -R` | tümü DONE | tek cümle (aşağıda) | DONE 02:1x |

## Olay günlüğü
- 01:1x Salih beyanı → defter **Karar 68** (aynen kayıt). Çelişki kapısı + manifest kapısı (yukarıda). Emir `cc/gorev-2026-08-26-2.md` derlendi (H=7 TETİK; Kapı-Ö aşağıda).
- 01:2x Kapı-Ö GEÇTİ (0 çağrı); açılış commit'i 4df7014. S-0 tek Sonnet atlas ajanı salındı (≤10 erişim). S-1 KOŞUM BAŞLADI: Workflow **wf_9030bba4-c00** (kopya `cc/workflow/2026-08-26-anakronizm-freni-m40b-wf_9030bba4.js`); 9 KB-02 tahmin satırı bronz'a (kaynak: wf_d8cf4f3a gerçekleşmeleri — önceki tahmin bandı 150-220k'nın altında kaldığı için bant DÜŞÜRÜLDÜ: tez 1-15k · antitez 2-18k · V26 0,05-1k).
- 01:3x S-0 TAMAM (10 erişim, 40k token, 2,4 dk): dil-başına güncel ölçüm BULUNAMADI (arXiv tek sürüm v1 2025-04-03 ✓; resmî leaderboard data.json 2024 SWE-bench Lite verisi — bayat/yanlış; swebench.com JS-render); Aider tepe gpt-5 high %88,0 (2025-08-23; sayfa 'last updated 2025-11-20' → leaderboard ~9 ay bayat) — Carvis V26 2/2 TUTUYOR. Anakronizm vakası #4: ajan 'Claude Mythos Preview bilinen ad değil' dedi (kendi kesimi). Rapor `cc/rapor-2026-08-26-3.md`.
- 01:5x wf_9030bba4-c00 TAMAM: 12/12, hata 0; 196 araç · 19,4 dk · alt-ajan usage 745.881; hayatta-kalma 1/29/1/0 (as-of kuralı → daralma); V26 46/4/7. `atlas-derle.py` → `cc/rapor-2026-08-26-2.md` (157 KB). Carvis V26: models/overview kesim tablosu birebir ✓ (Fable 5 Jan/Jan 2026 · Opus 5 May/May 2026 · Sonnet 5 Jan/Jan · Haiku 4.5 Feb 2025/Jul 2025).
- 02:0x G-1 sentez S1-S5 (taksonomi 4 kanal · M1-M7 · ölçülmüş etki · kanon kural metni adayı · borç ayrımı). SH-1 ARTILAR: `tools/anakronizm-denetim.py` (ilk kalıp seti 1.665 yanlış-pozitif → kalibre: İHLAL = tarihsiz sürüm/skor, UYARI = zaman-çivi; taban 201 dosya 114/319; bugünkü raporlarda 1) · `veri/model-kesim.jsonl` · SessionStart ZAMAN-ZEMİNİ satırı (1.672 B ≤ 2 KB test ✓) · `wiki/anakronizm-freni.md` + index + karşı-link · atlas-kosum SKILL as-of satırı · SCRIPTLER/veri README. SH-2: KB-66/67/68 ledger. KANON DOSYALARINA DOKUNULMADI (CLAUDE.md/tüzük/core → KB-66).
- **T BEYANI:** anakronizm freni raporu hazır ve artılar sisteme gömülü (lint · kesim tablosu · açılış satırı · wiki · SKILL disiplini); 3 KB kalemi (KB-66..68) masada; S-0 cevabı: dil-başına güncel ölçüm yok. Push Salih beyanıyla.
