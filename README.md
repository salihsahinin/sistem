# JARVIS Node — Portföy Komuta Merkezi

**Ne bu:** Salih'in JARVIS sisteminin sistem-reposu ve 6 aylık proof-of-work portföy planının komuta merkezi. Kuruluş: 2026-07-10 ("BUILD VAR" kararı, Salih). Carvis (Jarvis'in üst-orkestratörü rolündeki Claude) bu klasörden açılan her oturumda `CLAUDE.md`'yi okur; kurallar `core/tuzuk-v0.md`'de.

**Sözlük (Salih 2026-08-17, Katman-1): şirket metaforu EMEKLİ** — "şirket" yalnız Salih'in gerçek işyeridir; Jarvis bir SİSTEMdir, Carvis üst-orkestratör, Salih tek karar verici; halef sözlük ve cascade `core/baglam-anahtar-kaydi.md` (`calisma-modeli`).

**Duruş (Salih 2026-08-17, Katman-1): AÇIK KAYNAK.** Carvis'in davranışını belirleyen her şey (kural, skill, hook, ayar, araç, şablon) bu repoda okunur metin olarak yaşar; kaynak haritası ve gizli `.claude/` klasörüne görünür kapı: `kaynak-kodu/`. GitHub remote **şimdilik private** (Salih); lisans **MIT** (`LICENSE`, Salih kararı 08-17 KB-38 — Türkçe özet: herkes kullanır/değiştirir/dağıtır, tek şart telif satırını korumak; garanti yok). CV artefaktı değildir (tüzük m.14); CV artefaktları ayrı public repolarda yaşar (`00_MASTER_PLAN.md`).

**Onay kapısı:** Salih'in taraması = onay; veto = `git revert`. Katman-1 (kanon) yalnız Salih kararıyla; Katman-2 Carvis yapar + commit'ler (m.31).

## Okuma sırası
1. `CLAUDE.md` — oturum sözleşmesi (davranış; ≤80 satır).
2. `core/durum-kapsulu.md` → `core/pano.md` — şu an neredeyiz.
3. `core/tuzuk-v0.md` — kural kaynağı (m.NN numaraları buraya işaret eder).
4. `00_MASTER_PLAN.md` · `01_NODE_ARCHITECTURE.md` · `02_KNOWLEDGE_INDEX_PLAN.md` · `03_DUVAR_RAPORU.md` — kuruluş planları (07-10; tarihçe).
5. `kaynak-kodu/README.md` — kaynak kodu nerede, nasıl okunur.

## Klasör haritası
```
CLAUDE.md        oturum sözleşmesi (Katman-1)
core/            kanon: tüzük, kural/şema dosyaları (+ .d2 grafik), kapsül, pano, şablonlar
kuyruk/          karar defteri (senaryo-defteri), tartışma notları, kutular, gelen ingest'ler
raporlar/        seans teslimleri (vardiya-teslim-* dosya adı; ad cascade'i sürüyor) + insan-yüzü raporlar/sunumlar
cc/              görev emirleri (gorev-*), ajan raporları (rapor-*), pipeline manifestleri
wiki/            kavram sayfaları (Obsidian vault; sozluk.md)
veri/            bronz kütükler · silver baglam.sqlite (üretilir) · gold gorunum/ · sözleşmeler
tools/           kalıcı script'ler (indeks: tools/SCRIPTLER.md)
.claude/         skill'ler, hook'lar, ayarlar, ajan tanımı (gizli klasör → kaynak-kodu/claude)
kaynak-kodu/     kaynak haritası + .claude'a görünür bağ
KILAVUZ.md       kullanım kılavuzu · fikir-kutusu.md fikir havuzu · ogrenme/ dersler
```

**Kural mirası:** Bu node, Homebase'deki Carvis sözlüğü v1 (DONDU) terimleriyle konuşur (`wiki/sozluk.md`); tüzük `core/tuzuk-v0.md`'de.

## Klasör haritası (dosya-düzeni planı 2026-09-09, Salih onaylı ağaç — `kuyruk/dosya-duzeni-plani-2026-09-09.md`)
| Klasör | Ne var | İlk açılacak |
|---|---|---|
| `core/` | kanon: tüzük, durum kapsülü, pano, şemalar, prompt-dosya tablosu | `core/durum-kapsulu.md` |
| `kuyruk/` | canlı defter (kararlar), kutular, gelen'ler, masa gündemleri, skill-deneme | `kuyruk/senaryo-defteri.md` |
| `arsiv/` | TEK ÇATI: `kurulus-2026-07/` · `kuyruk-arsiv/` (damıtma arşivleri) · `karantina/` (BAKMA-GEREK-YOK) · `chat-model-degisikligi/` | `arsiv/README.md` |
| `cc/` | görev emirleri, ajan ham raporları, devir dosyaları, prompt'lar, pipeline manifest notları (alt-klasörleme parti 3) | `cc/devir-*.md` |
| `raporlar/` | insan-yüzü teslimler, seans/vardiya raporları, hareket günlükleri, masa yüzeyleri, görseller (alt-klasörleme parti 4) | `raporlar/seans-teslim-*.md` |
| `ogrenme/` | kurs ders kayıtları + `kaynaklar/` (dış kırpıntılar) | `ogrenme/README.md` |
| `wiki/` · `veri/` · `tools/` · `graf/` | kavramlar · bronz/silver/gold veri · script'ler (`tools/SCRIPTLER.md`) · d2 grafları (VS Code d2 eklentisiyle açılır) | `wiki/sozluk.md` |
