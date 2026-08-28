# Hareket günlüğü — 2026-08-27 (Carvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `6f617f9`)

*Okunabilirlik ilkesi (Salih 08-17): Carvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 37 çağrı, 3 oturum.*

## Oturum `563ea60e` — 00:24:35→12:24:15 · 4 çağrı · model sonnet-5 · hata 0
**Özet:** düzenledi 4
**Yazılan/düzenlenen dosyalar (1):** `kuyruk/ders-gbm-ilerleme.md`

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 26 | 00:24:35 | düzenledi | kuyruk/ders-gbm-ilerleme.md | tamam |
| 27 | 10:55:16 | düzenledi | kuyruk/ders-gbm-ilerleme.md | tamam |
| 28 | 12:13:28 | düzenledi | kuyruk/ders-gbm-ilerleme.md | tamam |
| 29 | 12:24:15 | düzenledi | kuyruk/ders-gbm-ilerleme.md | tamam |

## Oturum `405e80db` — 00:30:51→00:51:40 · 29 çağrı · model fable-5 · hata 0
**Özet:** koştu 23 · düzenledi 4 · yazdı 1 · skill çağırdı 1
**Yazılan/düzenlenen dosyalar (3):** `KILAVUZ.md` · `tools/katman-hatti.py` · `tools/obsidian-harita.py`

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 27 | 00:30:51 | koştu | Silver tazele + katman-hatti adım yapısını bul ⟨python3 tools/katman-hatti.py 2>&1 ¦ tail -3 && echo '=== adım listesi ===' && grep -n 'ADIMLAR\¦def adim\¦("adim\¦adimlar =\¦steps =\¦\["' tools/katm…⟩ | yok |
| 28 | 00:30:52 | koştu | baglam-tablo.py hangi dizinleri tarıyor ⟨grep -n 'KAPSAM\¦TARANAN\¦dizin\¦glob\¦rglob\¦scan\¦klasor' tools/baglam-tablo.py ¦ head -20⟩ | yok |
| 29 | 00:31:25 | koştu | Silver şeması: referans tablosu var mı, türleri neler ⟨sqlite3 veri/baglam.sqlite ".tables" && echo '---' && sqlite3 veri/baglam.sqlite "SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%re…⟩ | tamam |
| 30 | 00:31:46 | koştu | kayit şeması + dosya dizin dağılımı + tarama kapsamı ⟨sqlite3 veri/baglam.sqlite "PRAGMA table_info(kayit)" ¦ head -8 && echo '--- dosya dizin dağılımı ---' && sqlite3 veri/baglam.sqlite "SELECT dizin, CO…⟩ | tamam |
| 31 | 00:31:50 | koştu | baglam-tablo dosya seçim mantığını oku ⟨sed -n '760,800p' tools/baglam-tablo.py⟩ | tamam |
| 32 | 00:32:37 | koştu | referanslar() ayıklama desenlerini oku ⟨sed -n '505,560p' tools/baglam-tablo.py⟩ | tamam |
| 33 | 00:32:42 | koştu | RE_YOL regex tanımını gör ⟨grep -n 'RE_YOL\s*=' tools/baglam-tablo.py && grep -n 'RE_YOL' tools/baglam-tablo.py ¦ head -3 && sed -n "$(grep -n 'RE_YOL\s*=' tools/baglam-tablo.py…⟩ | tamam |
| 34 | 00:32:59 | koştu | RE_YOL md-link içindeki yolu yakalıyor mu testi ⟨python3 - <<'EOF' import importlib.util spec = importlib.util.spec_from_file_location("bt", "tools/baglam-tablo.py") bt = importlib.util.module_from_s…⟩ | tamam |
| 35 | 00:33:31 | koştu | uretim şeması + katman-hatti graf adımı satırları ⟨sqlite3 veri/baglam.sqlite "PRAGMA table_info(uretim)" && sqlite3 veri/baglam.sqlite "SELECT * FROM uretim" ¦ head -3 && sed -n '43,49p' tools/katman-…⟩ | tamam |
| 36 | 00:34:08 | yazdı | tools/obsidian-harita.py | tamam |
| 37 | 00:34:14 | koştu | Gitignore ekle + harita script'ini ilk kez koş, çıktıyı gör ⟨printf '# Obsidian harita türevleri (Karar 72 EK): silverdan her koşumda yeniden üretilir\ngraf/obsidian-harita*.md\n' >> .gitignore && python3 tools/…⟩ | tamam |
| 38 | 00:34:34 | düzenledi | tools/obsidian-harita.py | tamam |
| 39 | 00:34:35 | düzenledi | tools/obsidian-harita.py | tamam |
| 40 | 00:34:42 | koştu | Nokta-dizin düzeltmesiyle yeniden koş + link hedeflerini örneklemle doğrula ⟨python3 tools/obsidian-harita.py && echo '--- örnek: core haritası ilk 14 satır ---' && head -14 graf/obsidian-harita-core.md && echo '--- link hedefl…⟩ | tamam |
| 41 | 00:34:52 | düzenledi | tools/katman-hatti.py | tamam |
| 42 | 00:34:58 | düzenledi | KILAVUZ.md | tamam |
| 43 | 00:35:01 | koştu | SCRIPTLER.md ve graf/README biçimlerine bak ⟨tail -6 tools/SCRIPTLER.md && echo '=== graf/README son 10 ===' && tail -10 graf/README.md⟩ | tamam |
| 44 | 00:35:21 | koştu | SCRIPTLER.md satırı + graf/README bölümü ekle ⟨cat >> tools/SCRIPTLER.md <<'EOF' ¦ **obsidian-harita.py** ¦ OBSIDIAN BAĞLANTI HARİTASI (Karar 72 EK, Salih seçimi A, 08-27): silver'daki hazır pointe…⟩ | tamam |
| 45 | 00:35:38 | koştu | Defter Karar 72 EK kaydı + tam hat koşumu (yeni adım dahil) ⟨cat >> kuyruk/senaryo-defteri.md <<'EOF' **Karar 72 EK (2026-08-27 seans-18, Salih seçimi aynen: "2. başlık:a diyeceğim ve icraya başla") · GRAF-BAĞLA…⟩ | yok |
| 46 | 00:36:06 | koştu | Commit öncesi değişiklik envanteri ⟨git status --short ¦ head -20 && git status --short ¦ wc -l⟩ | tamam |
| 47 | 00:36:16 | koştu | Karar 72 EK icrasını pathspec ile commit'le ⟨git add .gitignore KILAVUZ.md graf tools/SCRIPTLER.md tools/katman-hatti.py tools/obsidian-harita.py kuyruk/senaryo-defteri.md veri raporlar && git st…⟩ | tamam |
| 48 | 00:43:30 | koştu | İcra borcu tablosunu listele ⟨python3 tools/karar-borcu-tablo.py 2>/dev/null ¦ head -60⟩ | tamam |
| 49 | 00:43:36 | koştu | Açık borçları katman/durum ile listele ⟨sqlite3 veri/baglam.sqlite "PRAGMA table_info(karar_borcu)" && sqlite3 veri/baglam.sqlite "SELECT durum, COUNT(*) FROM karar_borcu GROUP BY durum" && …⟩ | tamam |
| 50 | 00:43:56 | koştu | İcra-sırada ve kısmen-kapandı borçların İB eşlemesi ⟨sqlite3 -separator ' ¦¦ ' veri/baglam.sqlite "SELECT borc_id, substr(baslik,1,70), COALESCE(icra_borcu,'-'), COALESCE(substr(not_,1,60),'-') FROM kara…⟩ | tamam |
| 51 | 00:49:22 | koştu | gnhf CLI yardımını oku ⟨which gnhf && gnhf --help 2>&1 ¦ head -40⟩ | tamam |
| 52 | 00:50:16 | skill çağırdı | celiski-kapisi Gece, Salih kararı gerektirmeyen icra/ölçüm borçlarını (İB havuzu) kapatan otonom loop kurulsun; koşucu gnhf (claude CLI ajanı), model Fable DEĞİL (daha ucuz model), commit var push yok | tamam |
| 53 | 00:51:34 | koştu | Tüzük m.30/m.41/m.42 maddelerini birebir alıntıla ⟨grep -n 'm\.42\¦^## m\.4[12]\¦^## m\.30\¦^## m\.9\b\¦^### ' core/tuzuk-v0.md ¦ head -20; echo '=== m.41 / m.42 / m.30 gövde ==='; awk '/^## m\.(30¦41¦…⟩ | tamam |
| 54 | 00:51:38 | koştu | Tüzük 9/30/41/42 maddelerinin ilk 400 karakteri ⟨grep -n '^9\.\¦^30\.\¦^41\.\¦^42\.' core/tuzuk-v0.md ¦ cut -c1-400⟩ | tamam |
| 55 | 00:51:40 | koştu | m.42 ajan-yetki kanununu tam oku ⟨sed -n '69p' core/tuzuk-v0.md ¦ fold -s -w 160 ¦ head -30⟩ | tamam |

## Oturum `6108b705` — 18:04:42→18:04:55 · 4 çağrı · model opus-5 · hata 0
**Özet:** koştu 3 · skill çağırdı 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 1 | 18:04:42 | skill çağırdı | seans-acilis | tamam |
| 2 | 18:04:45 | koştu | Tarih, son commitler ve git durumu ⟨date "+%Y-%m-%d %H:%M" && echo "--- git log -5 ---" && git log -5 --format='%h %ad %s' --date=format:'%m-%d %H:%M' ¦ cut -c1-160 && echo "--- status -…⟩ | tamam |
| 3 | 18:04:49 | koştu | Durum kapsülü ve panoyu oku ⟨cat core/durum-kapsulu.md && echo "=== PANO ===" && cat core/pano.md⟩ | tamam |
| 4 | 18:04:55 | koştu | Senkron logu oku ve katman hattını koştur ⟨tail -1 raporlar/usage/senkron-log.jsonl; echo "=== hat ==="; python3 tools/katman-hatti.py 2>&1 ¦ tail -25⟩ | yok |

