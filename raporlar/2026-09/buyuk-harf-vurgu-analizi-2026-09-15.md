# Büyük-harf vurgu sızıntısı — kök-neden analizi + düzeltme (2026-09-15, Fable ana-sıra; deneysel m.29)

*Salih yan-görevi 09-15 (aynen): "sonnet yan oturumlarımda bir konu öğrenirken bazen kontrolsüzce kelime vurgusu yapmak istediği zaman caps lock açık bir şekilde yazıyor … tahminim sistemin kendi memory/md dosyalarında caps lock ile kelime vurgusu yapılıyor ve bu durum bana yansıyabiliyor … caps lock açık bir şekilde kelime vurgusu görmek istemiyorum." Ölçüm scripti bu seans (geçici, `/tmp/caps.py`; kalıcı sürüm gerekirse `tools/`). Rakamlar bu seansın sayımı (m.39).*

## 1. Hipotez testi — Salih'in tahmini DOĞRULANDI
Ölçü: ≥4 harfli, tamamı büyük sözcük sayısı / 1000 kelime (‰); kısaltmalar (OWASP, YAML, DONE, MCP…) hariç.

| Katman | Dosya | ‰ | Örnek |
|---|---|---|---|
| Her seans yüklenen | `.claude/skills/seans-acilis/SKILL.md` | **73,1** | AKTİF, ANLATILMAZ, BAYAT, BEKLEYEN, BLOKE |
| Her seans yüklenen | `core/durum-kapsulu.md` | **45,2** | AYNEN, AÇIK, AŞIM, BEKLET, KAPANDI |
| Her seans yüklenen | `CLAUDE.md` | **38,7** | ANLAMASI, ANLATILMAZ, BAŞLAYAN, BURAYA |
| Ders oturumu yükler | `kuyruk/skill-deneme/ogren/SKILL.md` | 41,7 → **0** (düzeltildi) | ATLANIR, DOĞRU/AÇIK etiketleri, KOŞULMAZ |
| Ders oturumu yükler | `ogrenme/README.md` | 22,4 → **≈0** (düzeltildi) | BULANIK, DEĞİLDİR, DOĞRUDAN |
| Ders oturumu yükler | `ogrenme/guvenlik/README.md` · `evals/README.md` | 12,9 · 9,2 → **≈0** (düzeltildi) | ZORUNLU, SİMÜLASYON, KULLANILMAZ |
| Her seans yüklenen | hafıza `MEMORY.md` | 16,5 | SİLİNDİ, DARALTILDI |

Çıktı tarafı (transkript, yalnız asistan metni): Sonnet yan oturumları **1,4-3,2‰** (H1-H3 oturumu 30 sözcük: DOĞRU 21 — ogren skill'inin kendi etiketi; diğerleri TEMELDE, TAMAMEN, AYIRT EDEN, SONRA, İÇİNDE, AYNI = Salih'in şikâyeti). Fable ana-sıra **11,3‰** (KAPANDI, REVİZE, SÜPERSEDE = kanon sözcükleri). Yani model, yüklenen bağlamın üslubunu (20-70‰) seyreltilmiş biçimde taklit ediyor; prompt'la "yapma" demek işe yaramadı çünkü her turda aynı üslup yeniden yükleniyor.

## 2. Düzeltme (bu seans, Katman-2)
1. **Mekanik fren — Stop hook** `.claude/hooks/stop-buyuk-harf.sh` (settings.json `Stop`): her cevap bittiğinde `last_assistant_message` (yoksa transkript) taranır; kısaltma/kod/alıntı dışı ≥4 harfli tamamı-büyük sözcük varsa `decision: block` + gerekçe → model cevabı kalın-vurguyla yeniden yazar; `stop_hook_active` ile ikinci turda pas (sonsuz döngü yok). Test `stop-buyuk-harf-test.sh` 5/5. Tüm oturumlarda (ana-sıra + yan) geçerli.
2. **Kaynak temizliği — ders yolu:** ogren SKILL.md (18 sözcük), ogrenme/README (14), guvenlik README (10), evals README (5) küçük harfe indirildi; ogren'e "Üslup" bölümü, ogrenme/README adım 6'ya üslup satırı.
3. **Hafıza:** öğretim-iskeleti hafıza dosyasına kural satırı (her seans yüklenir).

## 3. Kalan kaynaklar — Katman-1 (Salih hükmü gerekir)
`CLAUDE.md` (38,7‰), `seans-acilis/SKILL.md` (73,1‰), `core/durum-kapsulu.md` (45,2‰) ve diğer core/ dosyaları büyük-harf vurgusunu **anlam taşıyıcı** olarak kullanıyor (KAPANDI, DONE, BAYAT, YASAK). Seçenekler: (a) olduğu gibi bırak, Stop hook çıktıyı tutar (öneri: ucuz, ölçülebilir; 5 seans sonra transkript ‰ yeniden ölçülür) · (b) core/ + CLAUDE.md'de vurguyu kalın harfe çevir (Katman-1; CLAUDE.md bütçesi 7168/7168 B, `**` eklemek bütçeyi aşar → aynı anda kısaltma gerekir) · (c) yalnız seans-acilis skill'ini çevir (Katman-2 sınırında, en yoğun dosya).

## 4. Ölçüm planı (m.29)
5 seans sonra: Sonnet yan-oturum transkript ‰ (hedef < 0,5), Stop hook block sayısı (hareket kütüğü / hook log), yanlış-pozitif listesi (beyaz listeye eklenecek kısaltmalar).
