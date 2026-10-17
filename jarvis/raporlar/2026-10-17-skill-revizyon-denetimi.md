# Skill revizyon denetimi (AS-OF 2026-10-17, salt-okur)

Skill sayısı: 19 (`jarvis/.claude/skills/*/SKILL.md`) + `sablonlar/skills/ogren/SKILL.md` (20 dosya); bulgulu skill: 9
Toplam bulgu: 31 (grep + satır okuma ile doğrulandı)
rust-çağrı: 15 · tüzük-okuma: 2 · lean-pointer: 6
mac-yolu: 4 · model-adı: 4 · diğer: 0
Bulgu yok: karar-hatti, karar-kaydet, karar-masasi (SKILL.md), emekli-anahtar-cascade, lojik-ceviri, ogren (ikisi), sinav-grill, wiki-sayfa-yaz, yol-planla, damitma (yalnız lean-pointer)

| skill | satır | eski ifade | öneri | tür |
|---|---|---|---|---|
| seans-acilis | 19 | `python3 tools/acilis-kapilari.py` (İB-91) → K1 satırı `ŞÜPHE` ise | Birincil `target/release/acilis-kapilari.exe`; Python yedek notu | rust-çağrı |
| seans-acilis | 21 | `python3 tools/acilis-kapilari.py --is "<konu>"` → K2 koşmuş-aday | Aynı: Rust ikilisi birincil | rust-çağrı |
| seans-acilis | 27 | `tools/acilis-kapilari.py` K3 (silver tazelik) | `acilis-kapilari.exe` K3 olarak yaz | rust-çağrı |
| seans-acilis | 43 | eşzamanlı kural sayısı ≤100 (`tools/kural-sayaci.py`) | `kural-sayaci.exe` birincil | rust-çağrı |
| seans-kapanis | 43 | `python3 tools/skill-esik.py` koş | `skill-esik.exe` birincil | rust-çağrı |
| seans-kapanis | 49 | Kural-sayacı: `python3 tools/kural-sayaci.py` (CLAUDE.md + bu seansta çağrılan skill'ler) | `kural-sayaci.exe` birincil | rust-çağrı |
| seans-kapanis | 58 | `python3 tools/hafiza-ayna.py` koş (~1 sn; kaynak | `hafiza-ayna.exe` birincil | rust-çağrı |
| seans-kapanis | 58 | Sıcak-katman FIFO (Karar 104 M1): `python3 tools/sicak-katman-fifo.py` | `sicak-katman-fifo.exe` birincil | rust-çağrı |
| skill-kapisi | 17 | `python3 tools/kural-sayaci.py --skill <ad>` (kural birimi + byte) | `kural-sayaci.exe --skill <ad>` (bayrak uyumu doğrula) | rust-çağrı |
| gorev-emri-derleme | 15 | `python3 .claude/skills/halusinasyon-engelleyici/scripts/derece.py --v… [--pahali-geri-alma]` | `target/release/derece.exe`; .py yedek | rust-çağrı |
| gorev-emri-derleme | 17 | `python3 .claude/skills/gorev-emri-derleme/scripts/tetik-denetim.py <emir> --repo ~/sistem/jarvis` | `tetik-denetim.exe <emir>`; repo yolu bağıl | rust-çağrı |
| gorev-emri-derleme | 27 | koşum 2× üstündeyse kapanışta sapma satırı (`tools/skill-esik.py`) | `skill-esik.exe` yaz | rust-çağrı |
| halusinasyon-engelleyici | 3 | önce H derecesi hesaplanır (scripts/derece.py) | description'da `derece.exe` ya da yalnız "derece" | rust-çağrı |
| halusinasyon-engelleyici | 9 | derece: `scripts/derece.py` · kardeşler: skill-üretim şeması K2 | `derece.exe` birincil, `.py` yedek | rust-çağrı |
| halusinasyon-engelleyici | 12 | `python3 .claude/skills/halusinasyon-engelleyici/scripts/derece.py --v… [--pahali-geri-alma]` | `derece.exe --v…`; .py yedek | rust-çağrı |
| celiski-kapisi | 15 | Hedefli tara: `core/tuzuk-v0.md` (madde + ek fıkra + şerhler) | Tüzük 15 parça: `Read` ya da `baglam genislet core/tuzuk-v0.md`; cat/grep eksik okur | tüzük-okuma |
| seans-acilis | 8 | Kural kaynağı tüzük (`core/tuzuk-v0.md`); bu skill davranışı tetikler | Okuma yönteni ekle: `Read` ya da `baglam genislet` (Bash eksik okur) | tüzük-okuma |
| celiski-kapisi | 9 | Kanon zinciri: m.16 (çelişki kapısı — **tek** fren) · m.38 · m.31 · m.8 | `lean/Kanon/CeliskiKapisi.lean` pointer; zinciri tekrar anlatma | lean-pointer |
| halusinasyon-engelleyici | 9 | Kural kaynağı: `core/halusinasyon-paketi.md` (fren listesi F1-F10 + derece formülü | `lean/Kanon/Halusinasyon.lean` pointer ekle; F1-F10 metni md'de kalabilir | lean-pointer |
| gorev-emri-derleme | 17 | SKILL tetikleri bloğu (tetiklenme şeması v1 — `core/skill-tetikleme-semasi.md`): çağrı başına 9 alan | `lean/Kanon/SkillTetik.lean` pointer; 9 alan listesini kısalt | lean-pointer |
| skill-kapisi | 9 | Kural kaynağı: `core/skill-uretim-semasi.md` (ağaç + düğüm sözlüğü + formüller) | `lean/Kanon/SkillUretim.lean` (+ `SkillDogum.lean`) pointer ekle; yalnız SkillKapi anılıyor | lean-pointer |
| damitma | 13 | Kayıt-başına triyaj (şema §3): 4 soru → NOOP/UPDATE/GEÇERSİZ-KIL | `lean/Kanon/Ingest.lean` pointer; triyaj dalını tekrar anlatma | lean-pointer |
| pipeline-kosum | 13 | lider deseni (lider modeli: Karar 89 09-09 — Opus 5, effort **medium** sabit | `lean/Kanon/Delegasyon.lean` pointer; model adını Lean'e bağla | lean-pointer |
| seans-acilis | 16 | JARVIS kanonuna erişim var mı? (Mac: `~/sistem/jarvis` doğrudan [varsayılan yüzey] · Windows PC: `C:\JARVIS` | Varsayılan yüzey `C:\sistem\sistem\jarvis` (Windows 11); Mac ve `C:\JARVIS` satırını kaldır/arşivle | mac-yolu |
| seans-kapanis | 58 | kaynak `~/.claude/projects/-Users-HasanSalihSahin-sistem/memory/` salt-okur | Windows harness yolu `C--sistem-sistem` ile değiştir (`-Users-HasanSalihSahin` Mac ad-kodu) | mac-yolu |
| gorev-emri-derleme | 17 | `--repo ~/sistem/jarvis` | `--repo C:\sistem\sistem\jarvis` ya da bağıl yol | mac-yolu |
| skill-kapisi | 20 | skill-doctor koşumu (yerel; `~/dev/common-skills/.agents/skills/skill-doctor/`) | Yol Windows'ta var mı doğrula; yoksa güncelle | mac-yolu |
| atlas-kosum | 15 | sentez/hakem lideri Opus 5 medium (Karar 89 09-09; Karar 85 süpersede) | "Opus 5.5 medium" (Karar 89+106) | model-adı |
| gorev-emri-derleme | 23 | alt modeller (Opus 5 lider medium · Sonnet/Haiku işçi — Karar 89 09-09, Karar 85 süpersede) | "Opus 5.5 lider medium"; Karar 106 ekle | model-adı |
| gorev-emri-derleme | 27 | skill'i fiilen koşacak model **alt** modeldir (Opus 5 lider medium · Sonnet/Haiku işçi | "Opus 5.5 lider medium" | model-adı |
| pipeline-kosum | 13 | lider modeli: Karar 89 09-09 — Opus 5, effort **medium** sabit, Fable'dan Agent aracıyla | "Opus 5.5"; Fable ana-sıra ifadesi Karar 106 ile uyumlu mu bak | model-adı |

Notlar (bulgu değil, doğrulanmış güncel): seans-acilis 14 `lean/Kanon/SeansAcilis.lean`, seans-kapanis 36 `Butce.lean`, skill-kapisi 9/16 `skill-kapi` Rust ikilisi, seans-kapanis 55 `durum.exe`, gorev-emri-derleme 13 Lean sözleşme: zaten güncel. Hiçbir SKILL.md'de `open -R`, Finder, pbcopy, screencapture, `satır N` adresi yok. `Opus emekli` ifadesi yok. Scripts klasörleri: yalnız docstring/test içi `python3` çağrıları (`tetik-denetim.py`, `derece.py`, `kapi-denetim.py`, `masa-uret*.py`); karar-masasi `--repo ~/sistem/jarvis` varsayılanı docstring'te (masa-uret.py 6, masa-uret-test.py 5).

açık soru: (1) Lean eşlemesi doğrulanmadı: karar-modeli (satır 9 m.37 zinciri) için uygun modül var mı (KararSunum mu KararYetkisi mi)? (2) karar-masasi `scripts/masa-uret*.py` için Rust karşılığı planlı mı (listede yok, Python birincil kalır)? (3) `kural-sayaci.exe --skill` ve `tetik-denetim.exe --repo` bayrakları Python ile birebir mi (yalnız çağrı satırları grep'lendi, ikili çalıştırılmadı)? (4) `damitma`, `emekli-anahtar-cascade`, `wiki-sayfa-yaz` `tools/*.py` çağrılarının Rust listesinde karşılığı yok: Python birincil kalıyor, doğru mu?
