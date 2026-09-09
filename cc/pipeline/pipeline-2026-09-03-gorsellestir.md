# Pipeline — İB-77 "görselleştir" skill'i (2026-09-03)

*Emir: `cc/gorev-2026-09-03-ib77-gorsellestir-atlas.md` · manifest `veri/manifest/ib-77-gorsellestir.json` · rejim Fable planlayıcı + Sonnet işçi (Karar 85/86). Oturum düşerse yeni oturum buradan devralır; durum yalnız bu tabloda.*

| Birim | Şekil | İş | Koşucu | Teslim | Durum |
|---|---|---|---|---|---|
| S-A | scout (tez) | kuram + öğrenme görselleştirme | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-A.md` | TAMAM 09-03 |
| S-B | scout (tez) | araç + LLM→görsel emsalleri + doğrulama kapıları | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-B.md` | TAMAM 09-03 |
| S-C | scout (iç envanter) | skill kısıtları · yeniden-kullanım parçaları · yan-oturum erişimi · description bütçesi | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-C.md` | TAMAM 09-03 |
| N-A/B | antitez (¬) | yalnız iddia listesiyle (CoVe) çürütme | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-antitez-{A,B}.md` | TAMAM 09-03 |
| V26 | denetim | son üçlük ≥1 URL'li + ≥1 URL'siz + tüm sayısal iddialar | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-v26.md` | TAMAM 09-03 |
| H | hakem (maskeli) | D/K/X + hayatta-kalma; yapan≠ölçen | Fable | `cc/rapor-2026-09-03-ib77-gorsel-hakem.md` | TAMAM 09-03 |
| G-1 | sentez | karar tablosu + araç seçimi + skill tasarımı v0 | Fable | `raporlar/2026-09-03-ib77-gorsellestir-atlas.md` | TAMAM 09-03 |
| K | skill-kapisi | K0-K3 hüküm | Fable | kapı raporu (sentez içinde) | TAMAM 09-03 |
| SH-1 | ship | skill dosyaları + `tools/gorsellestir-*.py` (sınıflandırıcı · üretici · doğrulama kapısı) | Sonnet işçi case'leri, Fable kontrol | `.claude/skills/gorsellestir/`, `tools/` | TAMAM 09-03 |
| SH-2 | ship | 3 vaka testi (öğrenme partisyonu · icra çıktısı · karar masası) + symlink `~/.claude/skills/gorsellestir` | Fable + Sonnet | `raporlar/gorsel-vaka-*.html` | TAMAM 09-03 |
| T | teslim | SCRIPTLER.md satırı · defter kaydı · Salih'e yan-oturum canlı deneme tetiği | Fable | — | TAMAM 09-03 |

## Olay günlüğü
- 09-03 · pipeline açıldı; iç envanter ön-taraması (Fable): `~/.claude/skills` symlink deseni (3/4), d2 ✓ dot ✓ npx ✓ mmdc ✗, Python görsel paketi ✗ (networkx var), Lavish CDN yüzeyi ✓; S-A/S-B/S-C paralel salındı (ayak izleri ayrık: üç ayrı rapor dosyası).
- 09-03 · S-A/S-B/S-C TAMAM (A 4 açılma, Munzner/Tufte/C-M birincil erişim engelli; B 4 açılma, VisEval/ChartMimic K, D2/vl-cli açık; C: description bütçesi 7.379/7.380 → ENGEL, ölçüm aracı yok). N-A/N-B salındı (CoVe: yalnız iddia listesi). Fable ölçümü: d2 v0.8.1 + dot 15.1.1 aynı girdi→bayt-bayt aynı SVG (determinizm ✓). Ek birim: `tools/skill-butce.py` (Sonnet işçi) — bütçe ölçümü + --aday.
- 09-03 · N-A/N-B/V26/H TAMAM (hakem ayrı Sonnet: D14/K7/X4; SAĞLAM 6 · DARALDI 15 · DÜŞTÜ 4; T1 X → metin satırları DENEYSEL; T4 X → data-ink kural değil). G-1 sentez `raporlar/2026-09-03-ib77-gorsellestir-atlas.md`. K skill-kapisi: kapi-denetim GEÇTİ (T-Ü, F3b evals 8/7, R 3/3), F1e hazine bütçesi AŞIM (9.201/7.380 — Salih kalemi). SH-1: `tools/gorsellestir.py` (534 satır, 7 test) + SKILL.md + references/karar-tablosu.md + evals. SH-2: 3 vaka 13/13 PASS + tarayıcı render doğrulaması (d2 concept map · Vega-Lite bar · tablo) + symlink `~/.claude/skills/gorsellestir` kuruldu. T: SCRIPTLER.md 2 satır. Açık Salih kalemleri: description bütçesi kalibrasyonu/kısaltma · vl-convert pip · CDN bağımlılığı kabulü · DENEYSEL satırlar için beyan. Sınır: Mermaid/Vega-Lite tarayıcısız render doğrulanmaz (yapısal kapı) — vaka-2 tarayıcıda elle doğrulandı.
