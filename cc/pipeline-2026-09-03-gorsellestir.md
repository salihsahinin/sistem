# Pipeline — İB-77 "görselleştir" skill'i (2026-09-03)

*Emir: `cc/gorev-2026-09-03-ib77-gorsellestir-atlas.md` · manifest `veri/manifest/ib-77-gorsellestir.json` · rejim Fable planlayıcı + Sonnet işçi (Karar 85/86). Oturum düşerse yeni oturum buradan devralır; durum yalnız bu tabloda.*

| Birim | Şekil | İş | Koşucu | Teslim | Durum |
|---|---|---|---|---|---|
| S-A | scout (tez) | kuram + öğrenme görselleştirme | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-A.md` | SAHADA 09-03 |
| S-B | scout (tez) | araç + LLM→görsel emsalleri + doğrulama kapıları | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-B.md` | SAHADA 09-03 |
| S-C | scout (iç envanter) | skill kısıtları · yeniden-kullanım parçaları · yan-oturum erişimi · description bütçesi | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-C.md` | SAHADA 09-03 |
| N-A/B | antitez (¬) | yalnız iddia listesiyle (CoVe) çürütme | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-antitez-{A,B}.md` | BEKLİYOR (S-A/B) |
| V26 | denetim | son üçlük ≥1 URL'li + ≥1 URL'siz + tüm sayısal iddialar | Sonnet | `cc/rapor-2026-09-03-ib77-gorsel-v26.md` | BEKLİYOR |
| H | hakem (maskeli) | D/K/X + hayatta-kalma; yapan≠ölçen | Fable | `cc/rapor-2026-09-03-ib77-gorsel-hakem.md` | BEKLİYOR |
| G-1 | sentez | karar tablosu + araç seçimi + skill tasarımı v0 | Fable | `raporlar/2026-09-03-ib77-gorsellestir-atlas.md` | BEKLİYOR |
| K | skill-kapisi | K0-K3 hüküm | Fable | kapı raporu (sentez içinde) | BEKLİYOR |
| SH-1 | ship | skill dosyaları + `tools/gorsellestir-*.py` (sınıflandırıcı · üretici · doğrulama kapısı) | Sonnet işçi case'leri, Fable kontrol | `.claude/skills/gorsellestir/`, `tools/` | BEKLİYOR |
| SH-2 | ship | 3 vaka testi (öğrenme partisyonu · icra çıktısı · karar masası) + symlink `~/.claude/skills/gorsellestir` | Fable + Sonnet | `raporlar/gorsel-vaka-*.html` | BEKLİYOR |
| T | teslim | SCRIPTLER.md satırı · defter kaydı · Salih'e yan-oturum canlı deneme tetiği | Fable | — | BEKLİYOR |

## Olay günlüğü
- 09-03 · pipeline açıldı; iç envanter ön-taraması (Fable): `~/.claude/skills` symlink deseni (3/4), d2 ✓ dot ✓ npx ✓ mmdc ✗, Python görsel paketi ✗ (networkx var), Lavish CDN yüzeyi ✓; S-A/S-B/S-C paralel salındı (ayak izleri ayrık: üç ayrı rapor dosyası).
- 09-03 · S-A/S-B/S-C TAMAM (A 4 açılma, Munzner/Tufte/C-M birincil erişim engelli; B 4 açılma, VisEval/ChartMimic K, D2/vl-cli açık; C: description bütçesi 7.379/7.380 → ENGEL, ölçüm aracı yok). N-A/N-B salındı (CoVe: yalnız iddia listesi). Fable ölçümü: d2 v0.8.1 + dot 15.1.1 aynı girdi→bayt-bayt aynı SVG (determinizm ✓). Ek birim: `tools/skill-butce.py` (Sonnet işçi) — bütçe ölçümü + --aday.
