> **İNGEST EDİLDİ · 2026-08-17** (masa KB-08/09/10, Salih imzası → `wiki/paralel-oturum-protokolu.md` + seans-acilis §1.4-1.5 + KILAVUZ; kural adayları KURAL oldu). Bu dosya tarihçe.

# GELEN — Paralel-oturum kaynak çakışması, VAKA 2 (2026-08-15 20:22-20:30, terminal ana-sıra)

> **HAM / ingest edilecek** (ingest şeması v2 zarfı aşağıda). Kanon değildir. Bağ: `kuyruk/gelen-2026-08-12-paralel-oturum-kaynak-cakismasi.md` (vaka 1; kural taslağı "paylaşılan kaynak freni") — bu dosya o taslağın 2. saha verisidir, o dosya düzenlenmedi (yan-oturum yeni dosya açar kuralı).

**Zarf:** kaynak = Carvis/Fable seans-3 (oturum `1620e67b`) · tarih 2026-08-15 · tip = ARIZA-KAYDI + KURAL-ADAYI · hedef = KILAVUZ paralel-vardiya protokolü + `gunaydin-vardiya` skill'i · triyaj önerisi = ADD (yeni vaka) + UPDATE (ritüele adım).

## Olay (çıplak veri)
- 20:22:22 — seans-2 (oturum `d0e63fae`) Hat-2 commit'i `7e90a30` attı; kapanış ritüeli KOŞMADI (kapsül "seans-2 açık" hâlinde).
- 20:22:55 — Salih yeni terminal oturumunda "seans başı" dedi → seans-3 açıldı; gunaydin-vardiya ritüeli koştu. Brifte "önceki oturum 33 sn önce commit attı; kapalı varsayıyorum" dendi — **varsayım yanlıştı.**
- 20:25:22 — seans-2, Hat-3 emrini (`cc/gorev/2026-08/gorev-2026-08-15-3.md`) + manifest güncellemesini commit'ledi (`9f30f20`) ve S-3 workflow'unu sahaya çıkardı (`wf_e9c7f897-923`, 16 işçi, ~1M token sınıfı).
- 20:26-20:28 — seans-3, aynı standing emirden Hat-3'ü "açtı": gorev-emri-derleme ile `cc/gorev/2026-08/gorev-2026-08-15-3.md` YAZDI (seans-2'nin dosyasının ÜSTÜNE — Write aracı diğer oturumun dosyasını görmedi), manifest güncellemesi denedi (assert ile fark edildi: manifest zaten "S-3 SAHADA" diyordu).
- 20:29 — çakışma teşhis edildi: `git log` 20:25:22 commit'i + `subagents/workflows/wf_e9c7f897` dizini. **Workflow BAŞLATILMADI** (çift-harcama 0). Seans-3'ün dosya taslağı scratchpad'e alındı, dosya `git checkout` ile seans-2'nin HEAD sürümüne döndürüldü. Net hasar: 0 (yalnız ~10 dk + emir-derleme tokeni).

## Bulgu
1. **Vaka-1 kuralı doğru yönde ama tetiği eksik:** "yan oturum mevcut dosyayı düzenlemez, yeni dosya açar" kuralı ancak oturum kendini YAN oturum bildiğinde çalışır. Burada seans-3 kendini ANA-SIRA sanıyordu; kural devreye girmedi. Eksik olan: **canlı-oturum tespiti** (kim ana, kim yan — ritüelde adım yok).
2. **Yeni paylaşılan kaynak sınıfı:** Workflow/ajan koşumu (token bütçesi + aynı hedef dosyalar). Vaka-1 tablosuna satır: `Workflow (16 işçi) | aynı S-görevi iki kez koşar, ~1M token | git yakalamaz`.
3. **Yakalayan sinyal ucuzdu:** `git log -1 --format=%ci` (son commit ≤ N dk) ∧ kapsülde kapanış kaydı yok ⇒ paralel-oturum şüphesi. Ritüel bu iki veriyi zaten okuyor, yalnız BAĞLAMIYOR. Ek sinyal: `~/.claude/projects/<repo>/*.jsonl` mtime'ları (başka transcript son ~10 dk'da yazılmış mı).
4. Yazma aracı diğer oturumun yeni dosyasını "yok" sayıp üstüne yazdı — commit'li olduğu için `git checkout` kurtardı; **commit'siz olsaydı seans-2'nin emri kaybolurdu** (m.8 otomatik-silme sınıfı hasar). Vaka-1'in gerekçesi ("son yazan ezer, git yakalamaz") birebir doğrulandı.

## Kural adayı (taslak — Salih imzası; deneysel m.29)
> **Canlı-oturum kapısı (gunaydin-vardiya adım 1.4):** ritüel, `git log -1` zamanı ile oturum açılış zamanı arasındaki fark ≤ 15 dk ∧ kapsülde o vardiyanın KAPANIŞ kaydı yok ise → "paralel-oturum şüphesi" beyan eder ve **Salih'e tek soru sorar** (hangi oturum ana-sıra?); cevap gelene dek oturum SALT-OKUR (kanon/cc/manifest yazımı yok, workflow/ajan koşumu yok). Sayısal eşik (15 dk) deneysel; pozitif karşılık: şüphe yoksa normal akış.
> **Aynı-iş freni (vaka-1 "paylaşılan kaynak freni"nin genişlemesi):** ajan/workflow koşumu da paylaşılan kaynaktır — koşum öncesi manifestteki görev satırı okunur; "SAHADA" ise İKİNCİ KEZ KOŞULMAZ, bildirilir.

## Ders (ogrenme-hattı adayı)
Ritüel "kapsül taze, V4 sorunu yok" dedi — doğruydu; taze kapsül paralel oturumu DIŞLAMAZ, tersine "çok taze commit" paralel oturumun işaretidir. Tazelik testi tek yönlü okunmuş.
