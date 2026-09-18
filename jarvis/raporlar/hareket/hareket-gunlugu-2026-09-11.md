# Hareket günlüğü — 2026-09-11 (Jarvis'in araç çağrıları; kaynak transkript → `tools/hareket-tablo.py`; HEAD `c5b2d07`)

*Okunabilirlik ilkesi (Salih 08-17): Jarvis'in o gün YAPTIĞI her şey — dosya yazma/düzenleme, komut, okuma, arama, ajan/skill/workflow çağrısı — burada düz satır. Hedef gösterilir, içerik gösterilmez (içerik dosyanın kendisinde ya da git log'da). Makine-yüzü: silver `hareket` (`veri/baglam.sqlite`), gold `veri/gorunum/v_hareket_gunluk.csv` · `v_son_hareketler.csv`; bronz `veri/bronz/hareket-olay.jsonl`. Toplam bugün: 21 çağrı, 2 oturum.*

## Oturum `72eb3a58` — 09:46:32→09:51:06 · 16 çağrı · model fable-5-1 · hata 0
**Özet:** koştu 11 · düzenledi 3 · skill çağırdı 1 · yazdı 1
**Yazılan/düzenlenen dosyalar (2):** `core/durum-kapsulu.md` · `raporlar/seans/seans-teslim-2026-09-10-galeri-kumeleme-kota.md`

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 108 | 09:46:32 | skill çağırdı | seans-kapanis | tamam |
| 109 | 09:46:48 | koştu | Canlı-oturum kapısı: git durumu ve kapsülün galeri satırı ⟨cd ~/jarvis && git log -3 --format='%h %ci %s' ¦ cut -c1-140 && git status --short ¦ head -20 && echo ---KAPSUL--- && grep -n 'Güncelleme\¦GALERİ' cor…⟩ | tamam |
| 110 | 09:46:51 | koştu | Kapsülün galeri şeridi satırını tam oku ⟨cd ~/jarvis && grep -n 'GALERİ ŞERİDİ' core/durum-kapsulu.md ¦ cut -c1-900; echo; wc -c core/durum-kapsulu.md; wc -l core/durum-kapsulu.md⟩ | tamam |
| 111 | 09:46:57 | koştu | Kapanış kapıları: hareket kütüğü, bayat-çekim, katman hattı, skill eşiği, silver sağlık, kural sayacı, bağlam seyri ⟨cd ~/jarvis && { echo "== hareket-tablo"; python3 tools/hareket-tablo.py 2>&1 ¦ tail -4; echo "== bayat-cekim"; python3 tools/bayat-cekim.py --liste 2…⟩ | yok |
| 112 | 09:46:58 | koştu | Birim-test kapısı ⟨cd ~/jarvis && python3 -m unittest discover -s tools/testler -p 'test_*.py' 2>&1 ¦ tail -4⟩ | yok |
| 113 | 09:48:46 | koştu | Kapsülün tamamı ve bu oturumun bağlam seyri satırı ⟨cd ~/jarvis && cat core/durum-kapsulu.md ¦ cut -c1-700; echo ---SEYIR---; grep -i '72eb3a58' veri/gorunum/v_baglam_seyri.csv ¦ head -2; head -1 veri/g…⟩ | tamam |
| 114 | 09:48:59 | koştu | FIFO aracının kullanımı, wiki kuyruğu biçimi, son teslim raporları, arşive inen galeri satırı ⟨cd ~/jarvis && python3 tools/sicak-katman-fifo.py --help 2>&1 ¦ head -15; echo ---; grep -n -i 'kuyruk\¦as-of' wiki/README.md ¦ head -8; echo ---; ls …⟩ | tamam |
| 115 | 09:50:04 | yazdı | raporlar/seans/seans-teslim-2026-09-10-galeri-kumeleme-kota.md | tamam |
| 116 | 09:50:11 | koştu | Wiki kuyruğuna etkileşim-sinyali-testi satırı ekle ⟨cd ~/jarvis && python3 - <<'EOF' import pathlib p=pathlib.Path("wiki/README.md"); s=p.read_text() sat="- etkilesim-sinyali-testi → modelleme ÖNCESİ uc…⟩ | tamam |
| 117 | 09:50:24 | düzenledi | core/durum-kapsulu.md | tamam |
| 118 | 09:50:30 | düzenledi | core/durum-kapsulu.md | tamam |
| 119 | 09:50:33 | koştu | FIFO sayacı: kapsülde 9. madde → arşive inecek en eski madde ⟨cd ~/jarvis && python3 tools/sicak-katman-fifo.py 2>&1 ¦ grep -A6 -i 'kapsül\¦kapsul' ¦ head -14; wc -c core/durum-kapsulu.md⟩ | tamam |
| 120 | 09:50:40 | düzenledi | core/durum-kapsulu.md | tamam |
| 121 | 09:50:46 | koştu | İnen kapsül maddesini arşive yaz; FIFO'yu yeniden say ⟨cd ~/jarvis && cat > arsiv/kapsul-2026-09-11.md <<'EOF' # Kapsül arşivi — 2026-09-11 (FIFO, İB-80 / Karar 92 M1; silme yok m.8) Kapsül "Şu an" 9. madd…⟩ | tamam |
| 122 | 09:50:49 | koştu | Commit öncesi değişen dosyaların tam listesi ⟨cd ~/jarvis && git status --short ¦ cut -c1-120⟩ | tamam |
| 123 | 09:51:06 | koştu | Kapanış commit'i + türev katman commit'i (git add yol ile); push bekliyor ⟨cd ~/jarvis && git add core/durum-kapsulu.md arsiv/kapsul-2026-09-11.md wiki/README.md raporlar/seans/seans-teslim-2026-09-10-galeri-kumeleme-kota.md …⟩ | tamam |

## Oturum `14da067d` — 10:07:16→10:07:27 · 5 çağrı · model fable-5-1 · hata 0
**Özet:** koştu 4 · skill çağırdı 1

| # | saat | fiil | hedef | sonuç |
|---|---|---|---|---|
| 1 | 10:07:16 | skill çağırdı | seans-acilis | tamam |
| 2 | 10:07:19 | koştu | Tarih, son 5 commit ve durum kapsülünü oku ⟨cd ~/jarvis && date && git log -5 --format='%h %ci %s' ¦ cut -c1-140 && echo ---KAPSUL--- && cat core/durum-kapsulu.md⟩ | tamam |
| 3 | 10:07:24 | koştu | Panoyu oku ⟨cd ~/jarvis && cat core/pano.md⟩ | tamam |
| 4 | 10:07:25 | koştu | Silver bayat → katman hattını tazele (Karar 62) ⟨cd ~/jarvis && python3 tools/katman-hatti.py 2>&1 ¦ tail -15⟩ | yok |
| 5 | 10:07:27 | koştu | Son teslim raporundan devir borçlarını süz ⟨cd ~/jarvis && sed -n '1,60p' raporlar/seans/seans-teslim-2026-09-10-galeri-kumeleme-kota.md ¦ grep -inE 'devir¦borç¦salih¦sonraki' ¦ head -20⟩ | yok |

