# İB-63 Aile C — Ayak-İzi Doğrulama Raporu (iç envanterin adversarial denetimi)

- **Tarih:** 2026-08-29 · **Ajan:** ayak-izi doğrulama (Fable, işçi) · **Yöntem:** envanter raporu OKUNMADI (çıpalama freni); her iddia kaynak koddan Read/Grep/Bash-okuma ile bağımsız yeniden-türetildi. Deneysel m.29; her sayı komut çıktısından.
- **Kapsam:** 9 iddia · Hüküm ölçeği: TUTTU / TUTMADI / KISMEN.

## İddia başına hüküm

**1. baglam-tablo.py tmp→replace, kilitsiz — TUTTU.**
`tools/baglam-tablo.py:922-998`: `# ---- SQLite yaz (tmp → replace) ----` bloğu; `tmp_yolu = db_yolu + ".tmp"` (925), `sqlite3.connect(tmp_yolu)` + `con.executescript(DDL)` (928-929) → DB her koşumda SIFIRDAN kurulur; `os.replace(tmp_yolu, db_yolu)` (998). Kilit taraması: `grep -n "flock|fcntl|lockf|LOCK_EX|\.lock" tools/baglam-tablo.py` → 0 eşleşme (çıkış 1). Eşzamanlı iki koşumda geç biten `os.replace` kazanır: son-yazan-kazanır doğru.

**2. Yazar∩yazar koşum-önü kontrolü hiçbir script/hook'ta yok — TUTTU.**
`grep -rn "kesişim|kesisim|yazar.*∩|YAZAR-küme|yazar_kume|intersection" tools/ .claude/hooks/ cc/workflow/` → tek eşleşme alakasız (cc/workflow/2026-08-15-skill-semasi…js:39 "MALİYET-FAYDA kesişimi" — XKCD formül notu). Mevcut hook'lar: `pretool-core-tel.sh` (Bash yazım-teli), `pretool-ajan-fren.sh` (Agent çağrı-sayacı), `session-start.sh`. `core/durum-kapsulu.md:23`'teki "koşum-önü manifest/ledger kontrolü" prosedürel metin talimatıdır, kod değil. İki işin yazar-kümesi kesişimini hesaplayan hiçbir mekanizma bulunamadı.

**3. deny listesi core/ için boş; core-teli yalnız Bash — TUTTU.**
`.claude/settings.json:3` → `"deny": []` (tamamen boş; `ask` yalnız git push/screencapture/rec/sox). `settings.local.json`'da deny anahtarı hiç yok (yalnız allow). PreToolUse matcher'ları: `"Bash"` (core-tel) + `"Agent"` (ajan-fren) — settings.json:14,23. Hook kaynağı (`pretool-core-tel.sh`) yalnız Bash komut desenlerini grep'ler (`>>`/`>`, mv/cp/rm/touch/truncate/tee/dd/install, sed/perl -i, git checkout/restore/reset/clean/rm/mv × `core/|CLAUDE.md|.claude/`). Sonuç: Edit/Write araç-yolu core/ dosyalarına makine-düzeyinde açık. Ek bulgu: hook'un kendi yorum satırı "settings-deny yalnız Edit/Write tutar" diyor — bu yorum BAYAT, bugünkü deny boş; koruma tarihte varsa da şimdi yok.

**4. İB-55..İB-61 ledger'da yok — TUTTU.**
`grep -o "İB-[0-9]*" veri/karar-borcu.jsonl | sort -u` → benzersiz küme İB-01..İB-54 (19 ve 21 boşluklu, 52 kimlik). İB-55, 56, 57, 58, 59, 60, 61'in hiçbiri geçmiyor (ASCII "IB-" varyantı da 0). Koşum-önü ledger kontrolü bu işlere kör: doğru.

**5. Hat ~16 adım · baglam.sqlite'a dokunan script ~20 — KISMEN.**
(a) Hat: `tools/katman-hatti.py:32-51` ADIMLAR = 15 kalem (baglam, karar, prompt, ambar, deneyim, hareket, seyir, tarama, saglik, bag, erisim, graf, obsidian-harita, anakronizm, olcum) + hat-içi `hijyen` fonksiyonu olcum'dan önce koşar (104-119, 138-139) = **16 adım** → "~16" TUTTU. (--parquet açıkken +3 = 19.) (b) Script sayısı: `grep -rln "baglam.sqlite" tools/` → **29 dosya** (SCRIPTLER.md dahil); .py 28; test-hariç .py **25** — ve 25'in 25'i `sqlite3.connect` içeriyor (salt-yorum değil). "~20" iddiası düşük: gerçek 25 (test-hariç) / 28 (testli), sapma +%25-40 → bu yarı TUTMADI.

**6. Kapanış ritüeli katman-hatti'yi çağırır, aynı dosyalara yazar — TUTTU.**
`.claude/skills/seans-kapanis/SKILL.md:51`: "Hat (`katman-hatti`) bu adımdan SONRA koşar ki `kayit.cekim_tarihi` taze olsun" — kapanış hattı koşturur; ayrıca hattın adımlarını tek tek de koşar: `python3 tools/hareket-tablo.py` (satır 39, hat adım 6) ve `python3 tools/silver-saglik.py --kapi` (satır 45, hat adım 9). Hat → baglam-tablo → silver DB'yi tmp→replace SIFIRDAN yazar (iddia 1). Sonuç: kapanış-loop'u sürerken paralel koşan herhangi bir silver-yazan pipeline son-yazan-kazanır çakışması üretir — iddianın mekanizma çıkarımı kaynakla tutarlı. Şerh: SKILL'de birebir `python3 tools/katman-hatti.py` komut satırı yok; koşum satır 51'in talimat cümlesiyle bağlanır (aynı seans commit'leri "pipeline 16 adım" teslimini teyit ediyor).

**7. Gece-senkron 2026-08-04'ten beri sessiz — TUTTU.**
`tail -3 raporlar/usage/senkron-log.jsonl` → son satır `"ts":"2026-08-04T05:25:02..." "status":"FAIL-ff"` (öncekiler 08-04 00:02 FAIL-ff, 08-03 20:49 OK). 08-04 sonrası tek satır yok; bugüne (08-29) 25 gün üretimsiz. Son iki kayıt FAIL-ff: sessizleşme öncesi zaten düşüyormuş.

**8. İB-58 ve İB-30 ikisi de katman-hatti.py'yi yazar-kümesinde taşır — TUTTU.**
İB-58: `core/durum-kapsulu.md:23` "İB-58 axi-standardı (ilk aday katman-hatti)" + `kuyruk/senaryo-defteri.md:233` "axi-standardı + ilk aday katman-hatti → İB-58" — işin icra hedefi katman-hatti.py'nin kendisi. İB-30: `veri/README.md:88` "--parquet bayrağı … açma eşiği Salih'te (İB-30)" — bayrağın varsayılanı `tools/katman-hatti.py:127`'de (`ap.add_argument("--parquet", action="store_true", …)`; Karar 63: varsayılan KAPALI); açma kararının icrası bu dosyayı değiştirir. `kuyruk/devir-2026-08-29-yan-icra-fable.md:14,27` İB-30'un açık/bekler durumunu teyit ediyor. Şerh: DONDUR9 dosyasında (`kuyruk/masa-gundemi-DONDUR9-2026-08-29.md`) bu iki iş için satır bulunamadı; türetme kapsül+defter+README+devir kayıtlarından.

**9. hareket-olay.jsonl'a tek yazan hareket-tablo.py — TUTTU.**
`tools/hareket-tablo.py:136` varsayılan `--proje-dizin ~/.claude/projects/-Users-HasanSalihSahin-jarvis` (transkript dizini) → :108 glob `*.jsonl`; :154-157 bronz dosyaya başlık (yoksa) + `open(byol, "a")` APPEND — yalnız yeni `hareket_id`'ler. Repo taraması (`grep -rln "hareket-olay" --include=*.py --include=*.sh --include=*.md`): katman-hatti.py yalnız hareket-tablo'yu subprocess ile çağırır (adım "hareket", :38 — ayrı yazar değil, aynı yazarın tetikleyicisi); `cc/2026-08-29-erisim-soru-buyutme.py:13` yalnız soru-verisi tuple'ı (S29, okuma yok yazma yok); kalan eşleşmeler dokümantasyon/rapor. **Doğrudan yazan: 1 script.**

## Envanter güvenilirlik hükmü

**8 TUTTU · 1 KISMEN · 0 TUTMADI.** Tek sapma iddia 5'in ikinci yarısı: baglam.sqlite'a dokunan tools/ script sayısı ~20 değil **25** (test-hariç; testlerle 28) — hat adım sayısı (~16) ise doğru. En kritik iddialar (kilitsiz tmp→replace, yazar∩yazar kontrolünün yokluğu, core/ Edit/Write açığı, İB-55..61 ledger körlüğü, İB-58∩İB-30 = katman-hatti.py çakışma potansiyeli) kaynak koddan birebir doğrulandı. Envanterin risk-iskeleti güvenilir; sayısal kalibrasyonu (script sayısı) bir kademe düşük.
