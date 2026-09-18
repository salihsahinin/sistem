# Seans teslim — 2026-09-15 16:57 → 2026-09-18 (Fable ana-sıra, tek oturum 58141fb3, üç güne yayıldı): Karar 94 EK-5 · 98 · 99 · İB-93 · Friday tur-3/4 · atlas-kosum alt-ajan usulü · büyük-harf arızası · masa-13

*Kaynak: `core/sablonlar/seans-teslim.md` beş soru. Önceki teslim `raporlar/seans/seans-teslim-2026-09-15-karar97-buyuk-harf-ib88-92-hook-arizasi.md`. Bu çıktı bir sonraki oturumca okunacak (Salih 09-18: "seans bitimi çıktısını diğer oturum okuyacak"). Push bu kapanışta (m.9; masa-10 M8 b).*

## Devir özeti (sonraki oturum önce bunu okur)
- **Arkada koşan:** Friday tur-4 (`~/friday/cc/gelen/gorev-2026-09-18-tur4.md`, A1 v0.2, Karar 99 M2/M3/M4 uygulaması; dönüş `cc/giden/devir-2026-09-18-tur4-*` → Jarvis `cc/devir/friday-2026-09-18-tur4/`; Jarvis doğrular: test çıktısı + deny canlı deneme; sapma sayımı 2·1·0·? → 0 ise A2). **Evals H4 yan oturumu** PR açıyor (talimat: origin/main tabanlı worktree dalı, yalnız kendi dosyaları); gelince ana-sırada merge (ilerleme.md çakışması muhtemel). Güvenlik dalı merge edildi (`cffd851`), PR #5 push'la kapanır.
- **Sıradaki iş (Karar 98 + 99):** İB-108 hakem ajanı = şablon v0 ilk vakası (`raporlar/2026-09/atlas-kosum-altajan-usul/altajan-tanim-sablon-v0.md`; core'a girmez, test önce) → Ö1 eval-seti-kur (promptfoo ≥ v0.123.0, Node ≥22.22) → İB-109 atlas A/B ontoloji koşumu → İB-110..112 K0 → İB-79 → K-010 A3/A4.
- **Salih'in eli:** Sonnet güvenlik oturumunu kapat (worktree 15 commit geride, hook'ları ölü); yeni yan oturum main'den worktree açar · tüzük m.29 satırı "deneysel → kalıcı" (Edit kilidi) · galeri k=3 dokümanını gönder · mat-felsefesi ilk ders "seans başı, mat-felsefesi".

## Bugün gerçekten ne değişti
- **Karar 94 EK-5** (09-15): ürün turu icra türlerine alt-ajan; güvenlik ajanı G7 adayı.
- **İB-93** (09-16): `tools/devir-md2json.py` (A1 lojik blok → json; şema kapısı) + `gorev-emri-derleme` adım 5b + referans; ilk A1 emri Friday tur-3.
- **Friday tur-3 döndü** (09-16): S2 `D` (Read deny belgeli; tek satır symlink'i keser; 3b alt-dizin listesi), C2 `K` (okuma-izin agent_id okumuyor), sapma 0 + 3 blok-eksiği → **A1 şeması v0.2** (`OTURUM` `KAPANIŞ` `KAYNAKLAR` `AÇILIŞ_ADIMLARI`; script `.aktif-devir` yazar; test 9/9).
- **Karar 98** (09-16): çift hat (ajan-üretim ana-sırada, öğrenme yan oturumda); EK-1 zaman tetiği yok, kanıt kapıları (İB-104); EK-2 eval seti güncel araçla → promptfoo taraması (`raporlar/2026-09/2026-09-16-promptfoo-guncellik-taramasi.md`, v0.123.0 aktif).
- **Büyük-harf arızası kök neden** (09-17, `raporlar/2026-09/buyuk-harf-neden-suruyor-2026-09-17.md`): bayat worktree (Karar 97 öncesi kanon) + göreli hook yolu (Stop hook 34/36 çağrı ölü) + hook yalnız metin tarıyordu + `ogrenme/` hiç temizlenmemişti → Stop hook v0.3 (araç girdileri), `buyuk-harf-temizle.py` `ogrenme` katmanı (25 dosya, 291), pre-commit `ogrenme/**`, K1 worktree-geride sinyali.
- **İB-83 ilk canlı koşum** (09-17): `tool-results/` yanlış pozitifi → muafiyet; test bayrağı `JARVIS_HOOK_TEST`; kütükten 8 test artığı silindi.
- **atlas-kosum alt-ajan usulü** (09-17): 3 tez ∥ 3 antitez → maskeli hakem Opus 5 medium: 60 iddia → 43 sağlam / 14 daraldı / 2 düştü / 1 çelişkili; sentez + **şablon v0 taslağı**; 7 ajan ≈607k alt-ajan token.
- **Masa-13 → Karar 99** (09-18, 13/13): M1 Friday yan oturum değil · M2/M3/M4 Friday tur-4 emri · M5 dalga protokolü şablona girmez, atlas damıtılmaz · M6 şablon önce ilk vakayla test · M7 atlas dokunulmaz + A/B ontoloji koşumu · M8 galeri k=3 · M9 mat-felsefesi açık · M10 m.29 kalıcı · M11 üç skill adayı K0 · M12 Ö3-Ö6 jarvis hazinesinde (Karar 98 satırı düzeltildi, m.16) · M13 İB-79 + İB-80 sayaç.
- **İB-107** Friday tur-4 emri yazıldı (A1 v0.2 ilk kullanım).
- **Masa arızaları:** üretici onsubmit kesme-işareti hatası (`a3d6473`, test E4 13/13) · Jarvis'in kendi tarayıcı panelinde oturumu açması Salih'in yüklemesini düşürdü (ders: masayı Jarvis açmaz) · canlı oturumda yeniden üretim yükleme jetonunu bozdu (yeni dosya adıyla yeniden açıldı).
- Karar 95 EK usulü ilk kez uygulandı: güvenlik PR #5 dalı ana-sırada merge (çakışma `ilerleme.md`, dal sürümü alındı).

## Hangi karar verildi (kaynak + gerekçe + geri-açma)
- Karar 94 EK-5, 98 (+EK-1/EK-2), 99 (13 hüküm) — defter blokları; hepsi Salih Katman-1. Geri-açma: Karar 98 EK-1 kanıt sayaçları çalışmazsa · Karar 99 M6 şablon testi başarısızsa şablon revize · M7 A/B koşumu ontolojinin etkisini gösterirse atlas kararı yeniden masaya.
- Katman-2 (veto = revert): A1 şeması v0.2 · İB-83 tool-results muafiyeti · Stop hook v0.3 · `ogrenme` katmanı temizliği · masa üreticisi düzeltmesi · Karar 98 satırı düzeltmesi (M12 hükmüyle).

## Hangi fikir aday kaldı (karar değil)
- Karar 97 modal sözlük (5 seans ölçümü) · anahtar-denetim varyant×satır sayımı · K1 kapısı yanlış-pozitif ölçümü · İB-106 pre-commit `.claude/agents/*.md` · İB-105 Z1-Z3 eşleniği Jarvis testine · eski müfredat derslerinde 229 caps (tarihçe) · Friday b5 settings-reference çapa okuması · Q2/Q4/Q6/parti-34 kutuda.

## Sonraki ilk iş
İB-108 hakem ajanı (şablon v0 ilk vakası; baseline bugünkü hakem koşumu + İB-66) → Ö1 eval-seti-kur → İB-109 → İB-110..112. Friday tur-4 dönüşü geldiğinde doğrulama önce.

## Yeniden açma koşulu
Şablon testi (İB-108) başarı ölçüsü: hakem koşumunda D-oranı ve araç çağrısı bugünkü Opus koşumundan (7 çağrı, 116k token) kötü değil · A/B ontoloji koşumu (İB-109) fark gösterirse M7 · tur-4 sapma > 0 ise A1 v0.2 alanları yeniden.

## Kapılar (6b-6g)
- hareket-tablo `PASS` · skill-esik 6 çift, yeni-pencere sapması 0 · bayat-çekim kuyruk 0, çekilen 0/3 · kural-sayacı 19/100 · test-kapısı `OK` · skip 7 (128 test, 09-17 sayımı) · silver-sağlık `--kapi` çıkış 0: `WARN` YETİM aday 500/351 · T-B-KAPANDI aday 107 · T-A ön-eleme 500/9519 (Salih triyajı) · katman-hatti seyir `OK`.
- uzun-koşum: bu oturum max bağlam 491.623 (267 tur 128K üstü); statik önek >60k (KB-50 a). Araç-çıktısı aşımı: yok (atlas raporları dosyaya yazıldı, dönüşler ≤200 kelime).
- Hasat kontrol listesi: (1) karar adayları defterde (Karar 94 EK-5/98/99 + [icra] blokları) · (2) açık pipeline yok; atlas-kosum koşumu sentez raporuyla kapandı; Friday tur-4 sahada · (3) ajan koşumları: 7 atlas ajanı + promptfoo taraması + hakem — token/süre task usage satırlarında, `v_skill_kosum` (atlas-kosum bandı içinde) · (4) paralel oturumlar: güvenlik (PR #5 merge edildi) · evals (PR bekleniyor) · Friday (tur-4 çalışıyor) — çakışma: `ilerleme.md` çözüldü.
- Boyut-tetiği: kapsül 8.421/8.192 B → bu kapanışta kırpıldı · defter 48 KB üstü (devam) · MEMORY 16/16.
- Seans hedefi (Karar 99 M10, kalıcı): 09-16 hedefi "İB-93 + güvenlik dalı merge" → `TUTTU` (merge 09-18'e sarktı, dal PR'ı beklendi; sapma: takvim, kapsam değil) · 09-17 hedefi "ajan-üretim usulü + Ö1 başlangıcı + Friday tur-3 dönüşü" → usul + tur-3 `TUTTU`, Ö1 başlamadı (masa/arıza işleri araya girdi; sapma tek cümle: Ö1 sonraki oturuma).
