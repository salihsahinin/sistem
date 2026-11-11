# JARVIS Node — Portföy Komuta Merkezi

**Ne bu:** Salih'in JARVIS sisteminin sistem-reposu ve 6 aylık proof-of-work portföy planının komuta merkezi. Kuruluş: 2026-07-10 ("BUILD VAR" kararı, Salih). Jarvis (Salih'le konuşan ajan, deponun üst-orkestratörü; eski ad Carvis emekli 09-10, Karar 93) bu klasörden açılan her oturumda `CLAUDE.md`'yi okur; kurallar `core/tuzuk-v0.md`'de.

**Sözlük (Salih 2026-08-17, Katman-1): şirket metaforu EMEKLİ** — "şirket" yalnız Salih'in gerçek işyeridir; bu depo bir SİSTEMdir ("depo"/"kanon" denir), Jarvis = ajan + üst-orkestratör (Karar 93: tek ad, Carvis emekli), Salih tek karar verici; halef sözlük ve cascade `core/baglam-anahtar-kaydi.md` (`calisma-modeli`).

**Duruş (Salih 2026-08-17, Katman-1): AÇIK KAYNAK.** Jarvis'in davranışını belirleyen her şey (kural, skill, hook, ayar, araç, şablon) bu repoda okunur metin olarak yaşar; kaynak haritası ve gizli `.claude/` klasörüne görünür kapı: `kaynak-kodu/`. GitHub remote **şimdilik private** (Salih); lisans **MIT** (`LICENSE`, Salih kararı 08-17 KB-38 — Türkçe özet: herkes kullanır/değiştirir/dağıtır, tek şart telif satırını korumak; garanti yok). CV artefaktı değildir (tüzük m.14); CV artefaktları ayrı public repolarda yaşar (`00_MASTER_PLAN.md`).

**Onay kapısı:** Salih'in taraması = onay; veto = `git revert`. Katman-1 (kanon) yalnız Salih kararıyla; Katman-2 Jarvis yapar + commit'ler (m.31).

## Okuma sırası
1. `CLAUDE.md` — oturum sözleşmesi (davranış; ≤80 satır).
2. `../target/release/durum.exe oturum-basi --alan jarvis` — şu an neredeyiz (kapsül/pano dondu, Karar 122); sonra son seans kaydı `raporlar/seans/*.json`.
3. `core/tuzuk-v0.md` — kural kaynağı (m.NN numaraları buraya işaret eder).
4. `arsiv/kurulus-2026-07/` altında `00_MASTER_PLAN.md` · `01_NODE_ARCHITECTURE.md` · `02_KNOWLEDGE_INDEX_PLAN.md` · `03_DUVAR_RAPORU.md` — kuruluş planları (07-10; tarihçe).
5. `kaynak-kodu/README.md` — kaynak kodu nerede, nasıl okunur.

## Klasör haritası (2026-11-11 gerçek dizin listesine göre; ilk düzen: `kuyruk/dosya-duzeni-plani-2026-09-09.md`)
| Klasör / dosya | Ne var | İlk açılacak |
|---|---|---|
| `CLAUDE.md` · `AGENTS.md` | oturum sözleşmesi (Katman-1; CLAUDE.md = AGENTS.md symlink) | `CLAUDE.md` |
| `core/` | kanon: tüzük, kural/şema dosyaları (+ .d2 grafik), şablonlar | `core/tuzuk-v0.md` |
| `kuyruk/` | canlı defter (kararlar), kutular, gelen'ler, masa gündemleri ve spec'leri | `kuyruk/senaryo-defteri.md` |
| `arsiv/` | tek çatı: kuruluş, kuyruk arşivi, karantina, kapsül/hafıza/kanon arşivleri, worktree artıkları | `arsiv/README.md` |
| `cc/` | görev emirleri (`gorev/`), ajan ham raporları (`rapor/`), devir dosyaları, pipeline manifestleri, `workflow/` | `cc/rapor/` |
| `raporlar/` | `YYYY-MM/` ay klasörleri (konu raporları, günlük prompt özetleri) · `seans/` (teslim kayıtları, `girdi/` altında kapanış girdileri) · `hareket/` · `masa/` · `gorsel/` | `raporlar/README.md` |
| `wiki/` | kavram sayfaları (Obsidian vault) | `wiki/sozluk.md` |
| `veri/` | bronz kütükler · silver `baglam.sqlite` (üretilir) · gold `gorunum/` · sözleşmeler | `veri/gorunum/` |
| `tools/` | kalıcı script'ler | `tools/SCRIPTLER.md` |
| `kod/` · `lean/` | Rust araçları (`rituel`, `durum`, `baglam`, `arac` vb.) · Lean kanon hükümleri (`lean/Kanon/`) | `kod/` |
| `graf/` · `mods/` · `paylasim/` | d2 grafları (VS Code d2 eklentisiyle açılır) · Claude modları (oda, graf) · paylaşıma çıkan dosyalar | `graf/` |
| `.claude/` · `kaynak-kodu/` | skill, hook, ayar, ajan tanımı (nokta-dizin) · kaynak haritası + `.claude`'a görünür kapı | `kaynak-kodu/README.md` |
| `KILAVUZ.md` · `fikir-kutusu.md` · `../ogrenme/` | kullanım kılavuzu · fikir havuzu · kurs ders kayıtları (depo kökünde) | `KILAVUZ.md` |

**Kural mirası:** Bu node, Homebase'deki Jarvis sözlüğü v1 (DONDU) terimleriyle konuşur (`wiki/sozluk.md`); tüzük `core/tuzuk-v0.md`'de.
