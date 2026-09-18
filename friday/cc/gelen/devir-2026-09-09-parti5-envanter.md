# Envanter — parti-5 devri için Jarvis dizin görünümü (AS-OF 2026-09-09, HEAD 33de805; lider Jarvis'i okuyamaz, bu dosya onun gözüdür)

## cc/ — dizin başına git-izlenen dosya
- cc: 5 dosya
- cc/d2-eval: 15 dosya
- cc/denetci-kalibrasyon: 13 dosya
- cc/devir: 6 dosya
- cc/gorev: 1 dosya
- cc/gorev/2026-07: 42 dosya
- cc/gorev/2026-08: 72 dosya
- cc/gorev/2026-09: 6 dosya
- cc/kanit-bulucu: 11 dosya
- cc/pipeline: 17 dosya
- cc/prompt: 5 dosya
- cc/rapor: 1 dosya
- cc/rapor/2026-07: 40 dosya
- cc/rapor/2026-08: 131 dosya
- cc/rapor/2026-09: 23 dosya
- cc/workflow: 15 dosya
- cc/ kök tekiller: 2026-08-29-erisim-soru-buyutme.py README.md defter.md karar-onerisi-2026-08-16-hat6.md oran-2026-07-30-24.py 

## raporlar/ — dizin başına git-izlenen dosya + 2 örnek ad
- raporlar: 4 dosya · örn: 2026-07-10-arastirma-1-index-mimarisi.md 2026-07-10-arastirma-2-ingest-pipeline.md 
- raporlar/2026-07: 84 dosya · örn: 2026-07-10-arastirma-1-index-mimarisi.md 2026-07-10-arastirma-2-ingest-pipeline.md 
- raporlar/2026-08: 77 dosya · örn: 2026-08-01-INSAN-rapor-23.md 2026-08-01-INSAN-son-10-rapor.md 
- raporlar/2026-09: 13 dosya · örn: 2026-09-01-son-50-prompt.md 2026-09-02-son-50-prompt.md 
- raporlar/diger: 5 dosya · örn: L8-agentic-engineering-vardiya-kaydi.html README.md 
- raporlar/gorsel: 12 dosya · örn: README.md gorsel-2026-09-03-dogum-gunu-algoritmasnn-tumevarm-kant.html 
- raporlar/hareket: 24 dosya · örn: README.md hareket-gunlugu-2026-08-12.md 
- raporlar/jarvis: 9 dosya · örn: README.md jarvis-genel-bakis-archify-2026-08-29.architecture.json 
- raporlar/masa: 10 dosya · örn: README.md masa-8-karar-yuzeyi-2026-09-03.html 
- raporlar/seans: 27 dosya · örn: README.md seans-teslim-2026-08-17-seans8-atlas-uclusu.md 
- raporlar/usage: 6 dosya · örn: README.md SENKRON-UYARI.md 
- raporlar/vardiya: 48 dosya · örn: README.md vardiya-teslim-2026-07-10-11-FINAL.md 

## Mevcut README'ler (parti 1-4 yazdı; İÇERİKLERİ giden/ çıktısı ile ÇELİŞMEMELİ — lider bunları okuyamaz, yalnız varlığını bilir)
arsiv/README.md arsiv/chat-model-degisikligi/README.md arsiv/karantina/kuyruk/arsiv/gorsellestir-skill-2026-09-03/README.md arsiv/kurulus-2026-07/README.md cc/README.md cc/devir/README.md cc/gorev/README.md cc/pipeline/README.md cc/prompt/README.md cc/rapor/README.md cc/workflow/README.md ogrenme/README.md ogrenme/kaynaklar/README.md ogrenme/mat-felsefesi/README.md ogrenme/mit-6006/README.md ogrenme/mit-6042j/README.md raporlar/README.md raporlar/diger/README.md raporlar/gorsel/README.md raporlar/hareket/README.md raporlar/jarvis/README.md raporlar/masa/README.md raporlar/seans/README.md raporlar/usage/README.md raporlar/vardiya/README.md 

## KILAVUZ.md mevcut başlıkları ('Nerede ne var' bölümü YOK — parti-5 çıktısı olarak yazılacak, KILAVUZ bütçesi 16 KB, bugün 13,5 KB → bölüm ≤1,5 KB)
5:## Oturum nasıl işler
13:## Paralel seans protokolü (Salih kararı 2026-07-12 sabah; m.36 revizyonunun operasyonel devamı — dene
18:## Arşive inenler (damıtma 08-17) — üçlü sohbet düzeni · CC kanal modeli · CC-geçiş S2 hibrit-m
20:## Emir ve soru dili
26:## Kart ve kutu kuralları
31:## Tasarım ilkeleri (sıkıştırılmış 09-04; tam gerekçeler + Salih aynen-beyanları `arsiv/kuyruk-ar
48:## ~~Skill-yazım standardı (K-013)~~ arşive indi (damıtma 08-29 → `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2
49:## Boyut-izleme — sıcak-dosya bütçesi (İMZALI kural, Salih 07-22; rakamlar deneysel m.29)
52:## Sayı-araştırma kapısı (Salih emri 07-23 — kural)
55:## Öz-usage usul kuralı (Salih beyanı 08-01 sözlü → metinleşme Salih imzası 08-01 masa)
58:## Durum görünürlüğü (m.18)
61:## Model-değişimli oturum protokolü (Salih imzası, 2026-07-13 — kural, deneysel değil)
64:## Skill Standardı (K-016 açılışı 07-19; el kitabı: `raporlar/2026-07/2026-07-17-skill-nasil-olustur
74:## Deneysel notlar — 2026-07-29 (m.29; tam gerekçeler `arsiv/kuyruk-arsiv/KILAVUZ-arsiv-2026-08-30.md`)

## Kök README.md klasör haritası (parti 1; KILAVUZ bölümü bununla çelişmemeli, tekrar etmemeli — KILAVUZ 'nasıl gezilir + hangi soruya hangi dosya' der, README 'ne var' der)
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

## Kural pointer'ları (kanon/ altında OKUNABİLİR)
- kanon/tuzuk-v0.md m.8 (silme yok) · m.20 (pointer ilkesi: özet + adres) · m.39 (rakam kaynaklı, kestirim [?])
- Tarihli dosya adı = AS-OF damgası (Karar 88 M4); README'lerde tarih damgası: 'AS-OF 2026-09-09' satırı
- Dil: Türkçe; her README 3-6 satır: ne var · nasıl gezilir · üretici script/ritüel · arşiv kuralı
