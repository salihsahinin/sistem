# Pipeline — Tahmin↔Gerçek Ambar Katmanı (Kun-Chen P-1, 2026-08-21)

**Konu:** KB-02/03 kapanış icra borcu — üst modelin alt-model koşum tahminleri (kosum_profili) ambara yapılandırılmış girer; sapma görünümle ölçülür; skill-koşum pilotu (KB-03) kendi görünümünü alır; gorev-emri-derleme'ye "skill koşucusu = alt model" alanı eklenir.
**Bindirme (İB-40, Karar 45):** aynı emir bir de MONOLİT dilim (tek ajan, bölmeden) koşulur; iki sonuç ölçüm-bankına satır (token×süre×kalite) — V1 verim tanımının ilk gerçek verisi. Bütçe ~2× bilinçli (m.35).
**Emir:** `cc/gorev-2026-08-21-1.md` · **Rejim:** maliyet-öncelikli (scout+monolit) · **Seçim gerekçesi:** kapsül "Sonraki ilk iş" 2. maddesinin Salih hükmü beklemeyen ilk kalemi; manifest kapısı tarandı (7 manifest), mükerrer koşum yok.

## Görev tablosu
| Görev | şekil | iş | intake | teslim | durum |
|---|---|---|---|---|---|
| S-1a | scout (Sonnet) | tahmin↔gerçek kayıt envanteri: künye tabloları + tahmin bantları yapılandırılmış çıkarım | emir §GİRDİLER + dilim A | `cc/rapor-2026-08-21-1a.md` | SAHADA |
| S-1b | scout (Sonnet) | ambar/hat wiring: ambar-tablo.py + katman-hatti + test kalıbı + additive ekleme noktaları | emir §GİRDİLER + dilim B | `cc/rapor-2026-08-21-1b.md` | SAHADA |
| S-1c | scout (Sonnet) | skill-koşum verisi: amb_olgu_prompt doluluk + prompt-tablo.py + KB-03 pilot gereksinimi + şablon alanı yeri | emir §GİRDİLER + dilim C | `cc/rapor-2026-08-21-1c.md` | SAHADA |
| M-1 | monolit referans (Opus, İB-40) | AYNI emir bölmeden tek ajanda: keşif + tasarım önerisi (DDL + görünüm SQL + alan metni) | emir TAMAMI | `cc/rapor-2026-08-21-M1.md` | SAHADA |
| G-1 | sentez (Carvis) | scout raporları + kanon → tasarım kararı (tahmin verisinin bronz/silver yolu, görünüm SQL'leri, alan metni) | S-1a/b/c raporları DOSYADAN | manifest olay günlüğü + SH-1 planı | BEKLİYOR |
| SH-1 | ship (Carvis) | bronz tahmin kaydı + silver yükleyici + `v_kosum_tahmin_sapma` + `v_skill_kosum` + SKILL.md alanı + test + katman-hatti koşumu | G-1 kararı | commit(ler) `[icra]` | BEKLİYOR |
| SH-2 | ship (Carvis) | ölçüm-bankı: pipeline↔monolit karşılaştırma satırları (İB-40) + bu koşumun tahmin↔gerçek 4. kaydı ambara | M-1 raporu + amb_olgu_kosum | teslim raporu §ölçüm | BEKLİYOR |
| T | teslim | teslim raporu + kapsül/pano wiring + kaptan beyanı | tüm satırlar DONE | `raporlar/seans-teslim-2026-08-21-*.md` | BEKLİYOR |

## Kosum profili (KB-02 — üst model Fable tahminleri, yalnız alt modeller; gerçekleşen koşum sonrası yanına)
| görev | model×effort | tahmin çıktı-token | tahmin araç | tahmin süre | gerçekleşen |
|---|---|---|---|---|---|
| S-1a | Sonnet × low | 2-4k | 8-15 | 2-4 dk | — |
| S-1b | Sonnet × low | 2-4k | 10-18 | 2-4 dk | — |
| S-1c | Sonnet × low | 2-4k | 10-18 | 2-4 dk | — |
| M-1 | Opus × medium | 12-20k | 30-50 | 8-15 dk | — |

## Olay günlüğü
- 12:14 Seans açılışı; borç seçimi (KB-02/03 icra + İB-40 bindirme); manifest kapısı PASS (mükerrer koşum yok); canlı-oturum eşiği tetiklenmedi (son commit 56 dk önce); çalışma ağacındaki `veri/gorunum/v_karar_borcu.csv` değişikliğine DOKUNULMUYOR (başka koşumun izi olabilir — git add yol-bazlı).
- 12:2x Emir derlendi (H=2 GEREKMEZ; SKILL TETİKLERİ: yok); tetik-denetim Kapı-Ö sonucu aşağıda.
