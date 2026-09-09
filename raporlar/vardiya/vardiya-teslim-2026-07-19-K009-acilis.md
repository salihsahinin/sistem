# Vardiya Teslim — 2026-07-17→19 · K-009 Açılış Oturumu (Cowork ana-sıra/Fable)

**Tek satır:** K-009 açılış oturumu tamamlandı — canlı-ajan sınırı ve ajan-yetki anayasası imzalandı, 17 mobil-CC raporu süzgeçten geçip merge edildi, ilk insansız otomasyon (gecelik senkron) ve yetki kilidi kuruldu.

## Kararlar (tümü imzalı/kayıtlı; ayrıntı: senaryo-defteri 07-19 blokları)
1. **m.30 ek fıkrası:** otomasyon (K-009) = tetik devrine kadar; canlı ajan (K-010) = prompt + kalıcı kimlik devri. + PreToolUse ön-koşulu + model-hiyerarşi (JARVIS=Fable · lider=Opus/bir-altı).
2. **m.42 ajan-yetki kanunu** (7 fıkra; 07-15/07-17 formülasyonlarının tüzükleşmesi).
3. **Gecelik senkron = Model A + C aşısı** (LLM'siz ff-only script; token 0; başarısızlıkta dokunma-yok+sabah-uyarı; karşıt-temel Wald minimax).
4. **Kararlı-prefix kapsamı = koşum deseni** (TTL-içi aynı-önek tekrarı; rol farketmez).
5. **Ses sırası:** köprü protokolü → ölçümlü PoC (kapsam niyet-yakalama/triyaj).
6. **Kimi K3 ERTELENDİ** (V56); JARVIS=Fable pinli (bütçe/hesap + "final karar en zeki katmanda").
7. Süzgeç Katman-2 kararları: skill-kutusu ve POP ayrı dosya · geri-alınabilirlik alanı deneysel · supersedes notasyonu serbest · SessionStart hook Dilim-1 paketinde.

## İcra (push'lu)
17 rapor merge + `raporlar/2026-07-19-fable-suzgec-17-rapor.md` · `kuyruk/icra-sirasi-K009.md` (5 dilim; 0-1-2.1 kapalı) · `.claude/settings.json` yapısal kilit + `.claude/hooks/session-start.sh` · `tools/gece-senkron.ps1` + `raporlar/usage/` · KILAVUZ: Mobil Köprü Protokolü + bağlam-şişme kuralı · skill-kutusu (S-A..S-H) + POP (O1-O14) evleri · V56 statü. Disk dosya-düzeyi eşit (köprüyle); git HEAD Salih pull'unu bekliyor.

## Salih'e üç adım (gerekçeli)
1. **Windows terminali:** `cd C:\JARVIS` → `git pull` — .claude kilit dosyaları YALNIZ böyle iner (köprü .claude'a yazamıyor) + git tarafı kapanır; her dosya bayt-bayt eşit olduğundan çakışmasız fast-forward.
2. **Aynı terminal:** `schtasks /Create /TN "JARVIS-gece-senkron" /TR "powershell -ExecutionPolicy Bypass -File C:\JARVIS\tools\gece-senkron.ps1" /SC DAILY /ST 06:00` — ilk insansız otomasyonun tetiği; script başına da yazılı.
3. **CC saha testi:** `C:\JARVIS` kökünden YENİ CC oturumu aç → açılışta "=== JARVIS SessionStart ===" bandını görmelisin (hook testi); içine "core/tuzuk-v0.md'ye deneme satırı ekle" yaz → REDDEDİLMELİ (kilit testi); kapat. Deneysel damgaların kalkma koşulu bu test.

## Devir notu
Yeni seans "günaydın"la açılır; kapsül her şeyi taşıyor. Öğrenme P2 devri gelince ingest edilir. İmza masasında 6 kalem tüzük oturumunu bekliyor.
