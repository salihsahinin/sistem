# Vardiya Teslim — 2026-08-12 L8-MAC (Carvis/Fable, Mac Cowork, staj 1. günü paraleli)

*Açılış: "günaydın" + iki önsöz (ritüel koştu; kapsül 08-04'te bayattı, 08-05 P6-betik commit'leri + 08-11 Mac kurulumu kanona işlenmemişti — brifte şerh düşüldü). Oturum ortasında Salih beyanıyla hat NETLEŞTİ: bu oturum jarvis-geliştirme/L8. Kapanış: "seans bitimi" (staj kapısı bu oturumda beyanla aşıldı — gün boyu kanona yazan jarvis oturumuydu). Model bütünlüğü: baştan sona Fable — şerh yok.*

## 1. Bugün gerçekten ne değişti
- **Oturum yapılanması kuruldu (Salih kararı):** "günaydın jarvis geliştirme" / "günaydın staj" ayrı hatlar; staj hafızası/verisi staj klasöründe, jarvis reposu yalnız JARVIS'in işletimi. Ritüel çifti tamamlandı: staj klasöründe `staj-acilis` + `staj-kapanis` doğdu; `gunaydin-vardiya` v0.3 + `vardiya-kapanis` v0.2 STAJ KAPILI ve Mac-yollu — **hem repo hem hesap-düzeyi (claude.ai) kopyada** (bulut güncellemesi Carvis eliyle, "Edit with Claude → Update skill" akışı; Salih yalnız giriş yaptı).
- **L8 Mac geçişi Faz 0-4 DONE (envanter 10/11 diskte):** Faz 0 gemi (WezTerm + tmux 3.7b + Neovim 0.12 + OpenSuperWhisper + node + **claude CLI 2.1.228 girişli**; üç config Türkçe yorumlu). Faz 1 zemin (treehouse 2.1.1 brew'dan · gnhf 0.1.43 telemetrisiz; **iki fren Mac'te doğrulandı**: tavan 118K/100K'da kendiliğinden durdu — cache-dahil sayaç bulgusu bağımsız TEKRARLANDI; hedef-koşulu 2M tavanla `stop condition met`, 1 commit). Faz 2 doğrulama hattı (no-mistakes **v1.48.0**, wf-deneme kapılı; uçtan uca koşum → **PR #3**: 4 review bulgusu — pyc/test auto-fix + `carpim([])` sözleşmesi İNSANA ESKALE + `math.prod` bilinçli no-op; tek koşumda hem safe-fix hem eskalasyon sınıfı görüldü). Faz 3 lavish (global, `npx skills`). Faz 4 AXI'ler (gh-axi + chrome-devtools-axi, ilk kez). Faz 5 firstmate: klon hazır, ön-koşullar yeşil, **ilk koşum Salih'te (tarif verildi: tmux `kaptan` → `cd ~/dev/firstmate && claude`)**.
- Skill-tetiklenmeme arızası kapandı: 5 staj oturumu "seans bitimi"nde artık staj-kapanis'a düşer (açık oturumlar yeni skill'i oturum ortasında görüyor — bu oturumda gözlendi).
- Agile-metodoloji kalemi fikir-kutusuna İNDİ (`a8cf3f5`; araştırma emri Salih tetiğinde).
- Devralınan borçlar: 08-11 hook düzeltmesi commit'lendi (`5b62ca4`); paralel oturumun devir dosyası korundu (`27c1832`, İNGESTSİZ).

## 2. Hangi karar verildi
- **Katman-1 (Salih):** (a) günaydın-hatları oturum yapılanması (geri-açma: Salih beyanı). (b) Bu oturum = jarvis-geliştirme; L8'de **envanter-önce, entegrasyon-sonra** teyidi. (c) Bulut skill güncellemesini Carvis yapar (tarayıcı, Salih girişiyle). (d) staj-acilis/staj-kapanis kurulumu.
- **Katman-2 (Carvis, veto açık):** ci-adımı abort (CI'sız depoda sonsuz poll — iş bitmişti, PR sağlam) · rebase-kapısı onayı (çöp-depo, gnhf-dalı taban) · `carpim([])→None` sözleşme hükmü (çöp-depo; gerçek projede Salih'e giderdi) · treehouse brew-formülü tercihi (curl yerine) · kurulum betikleri indirilip incelenerek koşuldu (pipe-to-shell freni usul olarak benimsendi).

## 3. ADAY kalan (karar değil)
- **CI'sız depoda no-mistakes ci adımı sonlanmıyor** — gelecek koşumlarda `--skip ci`; wiki `no-mistakes` sayfası adayına Gotcha olarak.
- no-mistakes sürüm farkı (Win v1.41.2 → Mac v1.48.0) — davranış farkı gözlenmedi, izlenecek.
- Windows kurulumunun akıbeti (paralel mi, terk mi) — Salih'te.
- Kun'un global-memory symlink adımı (`~/.claude/CLAUDE.md` ↔ `AGENTS.md`) — entegrasyon fazının masasına (Cowork kurulumuyla çakışma riski).
- `kuyruk/gelen-2026-08-12-paralel-oturum-kaynak-cakismasi.md` — taze vardiyanın ingest'i.

## 4. Sonraki ilk iş
1. **firstmate ilk koşum** (Salih eliyle; çıktı bir sonraki jarvis oturumuna yapıştırılır → Faz 5 DONE beyanı).
2. **Faz 6 / P6 enstrümantasyon Mac uyarlaması:** `tools/olcum-dortlu.py` kaynakları artık Mac'te CANLI (`~/dev/wf-deneme/.gnhf/runs/*/gnhf.log` JSONL + `~/.no-mistakes/` durumu) — dörtlü deftere betikle.
3. Gelen devir dosyasının ingest'i + damıtma (defter FLAG sürüyor) + Salih kararları (şerhli 5 kalem, A1, stash-önce).

## 5. Yeniden-açma koşulu
- Entegrasyon fazı (kanon md'lerinin workflow'a bağlanması): "envanter 11/11 canlı" beyanıyla açılır.
- P4/çelişki kalemleri: değişmedi (Salih "workflow oturdu" beyanı).

## Hasat
- Özütler: (1) Fren bulgusu platformlar-arası tekrarlandı — gnhf sayacı cache-dahil; kalibrasyon notu artık iki bağımsız gözlemli. (2) Tek koşumda eskalasyon + safe-fix birlikte görüldü — Windows'ta iki koşum gerektirmişti. (3) Hesap-düzeyi skill'ler tarayıcıdan "Edit with Claude → Update skill" ile güncellenebiliyor — mobil yüzey senkronu artık Carvis'in elinde (yalnız giriş Salih'te). (4) Açık oturumlar yeni skill'leri oturum ortasında görüyor — "yeniden aç" tavsiyesi gereksizmiş. (5) macOS TCC Downloads'ı Cowork'ten gizliyor — dosyalar çalışma klasörüne taşınmalı.
- **Wiki-delta (kuyruğa):** `no-mistakes` sayfası (ci-adımı Gotcha'sıyla) · `firstmate` sayfası adayı (ilk koşum sonrası).
- Verilebilir miydi (V20): kurulumlar tek CC emriyle verilebilirdi; Mac ilk-koşumların Salih+Carvis eliyle gitmesi saha-teyidi üretti — P1/P2'dekiyle aynı bilinçli tercih. Tarayıcı sürüşü verilemezdi (giriş kapısı).
- Token×zaman: ~4,5 sa duvar-saati (staj günü paralelinde); ağır kalemler gnhf koşumları + no-mistakes hattı + tarayıcı sürüşü.

## Boyut-tetiği
- senaryo-defteri FLAG sürüyor (bu vardiya dokunmadı) · KILAVUZ 18,7/16KB sürüyor · kapsül bu kapanışta bütçeye göre yeniden yazıldı.

**Kapanış beyanı:** commit/push bu kapanışın parçası — sonuç aşağıda beyan edilir.
