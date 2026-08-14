# Pipeline Durumu — İngest Şeması Hattı (2026-08-14, firstmate-formatı)

*Kun-Chen firstmate düzeni: kaptan tek irtibatla konuşur; görevler scout/ship şekillerinde, intake sözleşmesi ve TÜM durum diskte; oturum düşerse yeni oturum bu dosyadan devralır (restart-proof). Kaptan: Salih · İrtibat: Carvis (ana-sıra terminal).*

## Görevler

| # | Şekil | İş | Intake | Teslim | Durum |
|---|---|---|---|---|---|
| S-1 | **scout** | İngest şeması literatür+sektör araştırması (4 aile: ajan-hafıza mimarileri · veri-müh. desen transferi · çok-oturum pratiği · şema tasarım ilkeleri) | `cc/gorev-2026-08-14-1.md` | `cc/rapor-2026-08-14-1.md` (D/K/X etiketli + "en güçlü 10 yapı-taşı") | **SAHADA** (Opus lider, paralel araştırmacılı; ~30-45 dk bandı) |
| G-1 | — | Şema sentezi (Carvis): S-1 raporu + jarvis kanon bilgisi → nihai ingest şeması | S-1 teslimi | şema metni | BEKLİYOR (S-1) |
| SH-1 | **ship** | Jarvis implementasyonu: `core/ingest-semasi.md` + CLAUDE.md okuma-sırası pointer'ı + kapsül notu | G-1 | commit + push (Salih 08-14: "commit push serbest") | BEKLİYOR (G-1) |
| SH-2 | **ship** | Staj implementasyonu: `~/staj başlangıç/ingest-semasi.md` (gunluk/ formatını genişletir) + staj CLAUDE.md pointer'ı | G-1 | yerel commit (remote yok — md.49) | BEKLİYOR (G-1) |
| T | teslim | Kaptan beyanı: **"şema hazır ve sisteme gömülü"** → Salih açık sekmelerini "seans bitimi" ile kapatabilir | SH-1 ∧ SH-2 | bu dosyada DONE damgası | BEKLİYOR |

## Keşif notları (implementasyona girdi)

- Jarvis'te bronz-katman FİİLEN VAR: `kuyruk/gelen-*.md` deseni (08-01 ve 08-12 devir dosyaları) — şema bunu resmileştirir, yeniden icat etmez.
- Staj tarafında `gunluk/YYYY-MM-DD.md` sabit bölümlü format zaten kuralda (Verilen task'lar · Ne yapıldı · Takıldığım yer · Sorulacaklar · Yarına devir) — şema bunu genişletir.
- md.49 yönü temiz: şema jarvis→staj YÖNTEM aktarımıdır (serbest); staj verisi jarvis'e akmaz.
- Askıda: spec-kit raporu commit'li, push Salih beyanı bekliyor (bu hattan bağımsız).

## Olay günlüğü

- 08-14 ~16:1x — Görev emri yazıldı (`cc/gorev-2026-08-14-1.md`); Opus lider sahaya çıktı (S-1 SAHADA); staj+kuyruk keşfi tamam.
- 08-14 ~16:4x — **S-1 DONE:** Opus lider teslim etti (`cc/rapor-2026-08-14-1.md`, 473 satır, ~55 D-ağırlıklı bulgu, "10 yapı-taşı" listesi; erişim-engeli şerhli: kaynak-derinliği güçlü, kaynak-keşfi eksik).
- 08-14 ~17:0x — **G-1 DONE:** şema sentezlendi (v1'in üzerine kayıt-katmanı). **SH-1 DONE:** `core/ingest-semasi.md` + jarvis CLAUDE.md pointer + kapsül notu. **SH-2 DONE:** `~/staj başlangıç/ingest-semasi.md` + staj CLAUDE.md pointer. Commit'ler: jarvis (push dahil) + staj (yerel).
- **T — TESLİM: ŞEMA HAZIR VE SİSTEME GÖMÜLÜ.** Tüm görevler DONE.
