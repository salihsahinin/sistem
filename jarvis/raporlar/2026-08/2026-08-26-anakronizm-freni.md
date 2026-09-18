# Anakronizm Freni — "sistemde anakronizm YASAK" (Karar 68) nasıl mekanikleşir + S-0 liderlik taraması — İNSAN-YÜZÜ TESLİM, 2026-08-26 (seans-16)

*Salih emri (01:1x, aynen): "1 yap ve bundan sonra sistemde anakronizm yapmayı yasaklıyorum bunu önleyecek şekilde nasıl yapacağını araştır atlasları koş artıları implement et."*
*Kaynak: `cc/rapor-2026-08-26-2.md` (m.40b, 3 aile × 12 işçi, wf_9030bba4; §Sentez S1-S5) · S-0 `cc/rapor-2026-08-26-3.md` · manifest `cc/pipeline-2026-08-26-anakronizm.md` · kural sayfası `wiki/anakronizm-freni.md`. Her rakam AS-OF damgalı; D = birincil, K = teyide muhtaç. Yazan: Carvis (Fable 5, reliable kesim 2026-01 — satıcı tablosu çekimi 2026-08-26).*

## 1. Tek cümle
**Anakronizm dört kanaldan geliyor (eski kayıt · model hafızası · konuşma · bayat kaynak) ve dördü de tek kuralla kapanıyor: zaman-bağımlı her iddia AS-OF damgası taşır, damgası eskiyse kullanılmadan önce canlı çekilir — bu kural bugün kod olarak gömüldü** (lint + kesim tablosu + açılış satırı); kanon metnine yazılması ve kapı sertliği Salih kararında (KB-66..68).

## 2. Bugünkü vakalar (neden yasak geldi)
| # | Kanal | Ne oldu | Doğrusu (AS-OF) |
|---|---|---|---|
| 1 | eski kayıt | 07-30 "Rust SDK yok" → 08-26'da "Rust hiçbir sınıfta" | 2026-07-31'de doğru; 2026-08-26'da API'de hâlâ yok, MCP'de Tier-1 (rmcp v3.1.4, 2026-08-20) |
| 2 | konuşma | "Go'da LLM doğruluğu düşük" (tarihsiz) | Multi-SWE-bench Tablo 4, **2025-04**, Claude 3.7: Go %7,5 |
| 3 | model hafızası | SWE-bench toplam skorlarını "biliyorum" | Fable 5 reliable kesim **2026-01**; bugün 2026-08-26 → 7-8 ay boşluk; doğrulanmadı |
| 4 | model hafızası (ajan) | S-0 ajanı "Claude Mythos Preview bilinen ad değil" | ajanın kesimi; "bilmiyorum" ≠ "yok" |
| 5 | bayat kaynak | "güncel leaderboard" | Aider sayfası "last updated **2025-11-20**"; Multi-SWE resmî data.json 2024 verisi |

## 3. Mekanizma seti (araştırma sonucu; hepsi kural/kod, "modele dikkat et" değil — Karar 65)
| M | Ne | Emsal (AS-OF) | Durum |
|---|---|---|---|
| M1 damga | iddia + AS-OF (çekim) + kaynak tarihi; chat dahil | Wikipedia `{{As of}}` (~93k sayfa, gizli bakım kategorisi) · Microsoft Learn zorunlu `ms.date` (çekim 2026-08-26) | kural wiki'de; kanon yerleşimi **KB-66** |
| M2 kesim tablosu | model-başına reliable/training kesimi; hafıza iddiası "AS-OF ≤ kesim, doğrulanmadı" | Anthropic sistem promptu `{{currentDateTime}}` + `<knowledge_cutoff>` (2026-07-24); models/overview tablosu V26 ✓: Fable 5 Jan/Jan 2026 · Opus 5 May/May 2026 · Sonnet 5 Jan/Jan 2026 · Haiku 4.5 Feb 2025/Jul 2025 | **GÖMÜLÜ:** `veri/model-kesim.jsonl` + SessionStart brifinde ZAMAN-ZEMİNİ satırı (bugün = sistem saati) |
| M3 canlı-çekim | zaman-bağımlı sınıf → cevaptan önce çek; bayat kayıt yeniden doğrulanmadan kullanılamaz | FreshPrompt: GPT-4 hızlı-değişen %28,6 → %75,6 (+47,0; ölçüm 2023-04) · RFC 9111 must-revalidate (2022-06) | kural wiki'de; hakem "sürümü yeniden çek" kuralı (08-22) genelleşti |
| M4 kayıt şeması | `gecerli_bas/bitis` + `cekim_tarihi` + `kaynak_tarihi`; as-of yüklemi | Wikidata P580/P582/P585/P813 · PROV (2013) · SQL Server `AS OF` yüklemi · SQLite pencere (3.25+) | SCD-2/bitemporal VAR; `cekim_tarihi` kolonu **KB-68** |
| M5 lint | tarihsiz sürüm/skor = İHLAL · zaman-çivi sözcüğü = UYARI · damgasız dosya = İHLAL · bayat damga = kuyruk | Vale `conditional` v3.18.0 (2026-08-20) · Google timeless-doc listesi (2024-10-15) · actions/stale (v11.0.0, 2026-07-28) | **GÖMÜLÜ:** `tools/anakronizm-denetim.py` — taban 201 dosya → 114 İHLAL / 319 UYARI; rejim **KB-67** |
| M6 kuyruk+boşaltma | `v_bayat_aday`; kapanışta N yeniden-çekim; silme yok (m.8) | Wikipedia 2010 kategorisinde hâlâ 3.126 açık sayfa (çekim 2026-08-26) → boşaltmasız damga = borç | gold görünüm gömülü; politika **KB-68** |
| M7 tazelik sınıfı | {zaman-bağımsız \| zaman-bağımlı}; sabit gün tablosu yok | FreshQA never/slow/fast (2023-11) · Luu 2022: bayatlama görevler arası ~30× | eşik 90 gün varsayılan; sınıf eşiği **KB-68** |

**Türkçe zaman-çivi sözcükleri (deneysel, kaynaksız):** şu an(da) · şimdilik · hâlâ · artık · henüz · yakında · son zamanlarda · en güncel · en güçlü · en son sürüm · en yeni · bugün itibarıyla · yeni/eski sürüm · desteklenmiyor · "resmî SDK'sı yok" · henüz yok → yanına tarih/sürüm konur.

## 4. KARAR MASASINA (Katman-1, ÖNERİ damgalı; ledger KB-66..68)
**KB-66 · Kural metninin kanon yerleşimi** (CLAUDE.md 7.139 B / 7 KB DOLU): **(a) CLAUDE.md §6'ya 1 satır pointer (bir satır girer, çıkacak satırı Salih seçer) + gövde wiki** — artı: kural her seans bağlama girer; eksi: satır takası · (b) tüzüğe madde — artı: tam metin; eksi: olgunlaşmamış kural · (c) yalnız wiki + KILAVUZ pointer — artı: dokunma yok; eksi: seans başında görünmez. Öneri **(a)**.
**KB-67 · Lint rejimi:** **(a) stdlib lint + katman-hatti'ye UYARI-kanallı adım (İHLAL hattı düşürmez, sayılır; pre-commit yok)** — artı: yanlış-pozitif ölçülmeden engel yok; eksi: ihlal commit'lenebilir · (b) pre-commit engel — artı: sert; eksi: yanlış-pozitif iş durdurur · (c) Vale'e geçiş — artı: hazır ürün; eksi: +1 Go zinciri, Türkçe kalıp yine elle. Öneri **(a)**.
**KB-68 · Bayatlık kuyruğu politikası:** **(a) tek eşik 90 gün + kapanışta N=3 yeniden-çekim + silver'a additive `cekim_tarihi`/`kaynak_tarihi` kolonu** — artı: ölçüm başlar; eksi: eşik kestirim · (b) sınıf-başına eşik (sürüm 30 · skor 90 · kavram 365 [?]) + N=5 — artı: ince; eksi: kaynaksız tablo · (c) yalnız rapor, boşaltma Salih tetiğinde — eksi: Wikipedia borç emsali. Öneri **(a)**.

## 5. Bu seansta GÖMÜLEN artılar (Katman-2)
- `tools/anakronizm-denetim.py` — D1/D2/D3; `--json`; bronz `veri/anakronizm-denetim.jsonl` + gold `veri/gorunum/v_bayat_aday.csv`; ilk kalıp seti 1.665 vuruş → kalibre (İHLAL/UYARI ayrımı).
- `veri/model-kesim.jsonl` — 4 model × 2 kesim türü, satıcı tablosu V26 ✓ (çekim 2026-08-26).
- `.claude/hooks/session-start.sh` — ZAMAN-ZEMİNİ satırı: "BUGÜN <sistem saati> · kesim(reliable) Fable 5 2026-01 · Opus 5 2026-05 · … · zaman-bağımlı iddia AS-OF damgasız ÇIKMAZ" (brif 1.672 B ≤ 2 KB).
- `wiki/anakronizm-freni.md` (M1-M7 + Türkçe liste + SOP + gotcha) + index + karşı-link turu; `atlas-kosum` SKILL disiplinine "her iddia AS-OF" satırı; SCRIPTLER/veri README kayıtları; defter Karar 68 + gözlem; kosum-sonuc PASS ×2; tahmin/halüsinasyon satırları; kapsül pointer.
- **Dokunulmayan:** CLAUDE.md · tüzük · core/ (KB-66) · katman-hatti adım listesi (KB-67) · silver şeması (KB-68).

## 6. S-0 cevabı ("1 yap")
Dil-başına GÜNCEL LLM doğruluk ölçümü **bulunamadı** (Multi-SWE-bench arXiv tek sürüm 2025-04-03 ✓; resmî leaderboard data.json 2024 SWE-bench Lite verisi; swebench.com Multilingual JS-render). Dil-kırılımsız: Aider polyglot gpt-5 high %88,0 (2025-08-23; sayfa 2025-11-20 ✓). Üçüncü-taraf agregatör sayıları K/güvenilmez. Kalan yol: yerel ölçüm (`cc/rapor-2026-08-26-3.md` §4; Salih tetiğinde).

## 7. Koşum künyesi + kör noktalar
wf_9030bba4-c00: 12 işçi · 196 araç · 19,4 dk · hayatta-kalma 1/29/1/0 (as-of kuralı → daralma baskın; DÜŞTÜ 1: LongMemEval bileşen rakamı doğrulanamadı) · V26 57 denetim 46/4/7. S-0: 1 Sonnet, 10 erişim, 2,4 dk, Carvis V26 2/2.
Kör: Türkçe zaman-ifadesi lint'i (liste kaynaksız; yanlış-pozitif oranı ölçülmedi) · chat damgasının makine denetimi · modelin kesim öz-bilgisi ölçümü · kişisel-ölçek emsali · "hangi mekanizma ne kadar azaltır" karşılaştırmalı ölçüm (Jarvis'te lint sayısı seans-başına izlenecek) · Datalog/tüzük-lojiği ekseni.
