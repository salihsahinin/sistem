# Kalıcı Script İndeksi (görünür kapı — `.claude/` gizli klasörü ve Obsidian .md-filtresi yüzünden)

*Açıklama: Carvis'in tek-seferlik OLMAYAN (kalıcı, B4 basamağı) script'leri iki yerde yaşar: (1) `tools/` (repo kökü, görünür) · (2) `.claude/skills/<skill>/scripts/` (skill'e bağlı; `.claude` GİZLİ — Finder'da ⌘⇧G ile `~/jarvis/.claude/skills` ya da terminalde `open ~/jarvis/.claude/skills`; Obsidian'da Ayarlar → Files & Links → "Detect all file extensions"). Bu indeks Salih'in "beraber okuma" isteği için açıldı (08-15): her satır yol · ne yapar · nasıl koşulur · okurken bakılacak yer. Kural: yeni kalıcı script buraya satır düşürmeden tamam sayılmaz (deneysel m.29). Tümü stdlib-only Python 3 (ps1 hariç).*

## Skill'e bağlı script'ler (08-15, Carvis — kapı/şema hattı)
| script | yol | ne yapar | koş | okurken |
|---|---|---|---|---|
| **kapi-denetim.py** | `.claude/skills/skill-kapisi/scripts/kapi-denetim.py` | Skill-üretim kapı-ağacının DETERMİNİSTİK kapıları: K2-R referans-varlığı (yol · m.NN · skill adı) + K3-F1..F4 biçim (description ≤1024/negatif-tetik/3.şahıs · <500 satır · evals ≥3+5/5 · adımlar+Gotchas) + tür-özel bayraklar (T-Y → `disable-model-invocation`) + hazine desc-bütçesi uyarısı | `python3 .claude/skills/skill-kapisi/scripts/kapi-denetim.py <skill-dizini> --repo ~/jarvis [--json]` → çıkış 0 geçti / 1 düştü | `gate()` sert/yumuşak ayrımı; K2-R regex'i (şablon yolları atlar); şekil tahmini FIRST sırası (heuristik, hüküm değil) |
| **tetik-denetim.py** | `.claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py` | Skill-tetiklenme şeması Kapı-Ö: emirdeki "SKILL TETİKLERİ" bloğunu okur; skill var mı · 9 alan dolu mu · T-Y skill örtük/alt-ajandan çağrılıyor mu (YASAK) · derece ifadesi · iç içe koşul ≤2 · retry ≤3 · FAIL-LOUD · yan-etki damgası | `python3 .claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py <emir.md> --repo ~/jarvis` → 0 geçti / 1 BLOKE / 3 blok yok | blok ayrıştırma (`- skill:` ile böler); O4 T-Y kuralı frontmatter'dan okunur |
| **derece.py** | `.claude/skills/halusinasyon-engelleyici/scripts/derece.py` | Görev-müsaitlik derece formülü H = Σ wᵢ·vᵢ (13 boolean bayrak; toplamsal, tamsayı, kanıtsız-tercih); eşik 7 / `--pahali-geri-alma` 4; v3a atıf override; ima edilen maliyet beyanı | `python3 .claude/skills/halusinasyon-engelleyici/scripts/derece.py --v2 --v3d --v4 [--pahali-geri-alma] [--json]` → çıkış 0 gerekmez / 5 F1+F2 / 10 skill TETİK | `W` sözlüğü = ağırlık + kanıt notu (tek bakışta formül); eşik mantığı 8 satır |

## Kök `tools/` script'leri
| script | ne yapar | koş | sahibi/tarih |
|---|---|---|---|
| **anahtar-denetim.py** | Bağlam Anahtar Kaydı v1 denetimi: emekli değerlerin kalıntı referanslarını katman bazında sayar (sıcak=ihlal · ılık=uyarı · soğuk=tarihçe), kayıt bütünlüğü (damgasız/halefsiz/çevrimli) | `python3 tools/anahtar-denetim.py` | Carvis paralel oturum (seans-3), 08-15 |
| **baglam-tablo.py** | JARVIS bağlamını (git-izlenen .md/.json/.jsonl) veri tablosuna çevirir → `veri/baglam.sqlite` · `veri/baglam.jsonl` · `veri/gorunum/*.csv` (şema v0; jarvis→veritabanı ilk adım) | `python3 tools/baglam-tablo.py` (sözleşme: `veri/README.md`) | Carvis paralel oturum, 08-15 (`cc/gorev-2026-08-15-7.md`) |
| **olcum-dortlu.py** | P6 enstrümantasyon: koşum-başına dörtlü (token · duvar-saati · iterasyon · sonuç) — gnhf log + no-mistakes state | `python3 tools/olcum-dortlu.py [--append]` | 08-12 (L8) |
| **verify-push.py** | Push-doğrulama: ∀ dosya origin ≡ çalışma ağacı ∧ HEAD=origin ∧ commit'lenmemiş değişiklik yok → PASS/teşhis | `python3 tools/verify-push.py` | 08-11 (loop-eng Faz 2) |
| gece-senkron.ps1 | Windows gece senkronu (origin→PC ff-only); Mac'te koşmuyor (Salih 08-11 "gerek yok") | — | 07-19 |

## Beraber okuma önerisi (Salih isteği 08-15)
Sıra: `derece.py` (en kısa; formül = tek sözlük) → `tetik-denetim.py` (blok ayrıştırma + kapı) → `kapi-denetim.py` (en uzun; regex-tabanlı kapılar) → `anahtar-denetim.py` / `baglam-tablo.py` (paralel oturumun DB hattı). Her okumada soru: "bu kapı hangi kanıta dayanıyor?" (docstring'de kural dosyası pointer'ı var) ve "hangi kısım heuristik, hangisi hüküm?" — okuma notları `ogrenme/dersler/`e; CV'ye giren gelişme noktası ayrı satır.
