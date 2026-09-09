# geri-donus v0 — devir notu şeması (Jarvis İB-75 raporu §6, 2026-09-09)

`giden/<devir_id>-geri-donus.md` bu 10 alanı bu sırayla taşır. Alan 3 ve 9 ÖNERİ kipindedir; lider hüküm cümlesi kuramaz.

| # | Alan | Tip | Zorunlu |
|---|---|---|---|
| 1 | `biten` | liste {iş, kanıt_yolu} | ✓ |
| 2 | `kalan` | liste {iş, neden_kaldı} | ✓ |
| 3 | `acik_sorular_salih` | liste str — HÜKÜM YOK | ✓ |
| 4 | `sonraki_ilk_is` | tek cümle | ✓ |
| 5 | `diskteki_dosyalar` | liste {yol, commit_dışı: bool} | ✓ |
| 6 | `sayac` | {ajan_çağrısı, araç_çağrısı, işçi_sayısı, alt_ajan_token} | ✓ |
| 7 | `sapmalar` | liste {emir_maddesi, ne_yapıldı, neden} | ✓ |
| 8 | `tohum_desen_kullanimi` | liste {desen_no, kullanıldı: bool, neden} | ✓ |
| 9 | `ledger_onerisi` | liste {ib_no, önerilen_durum} — ÖNERİ | ✓ |
| 10 | `durma_nedeni` | str \| null (fren / Katman-1 / tamamlandı) | ✓ |
| + | `hafiza_sicak_eklenen` | ≤3 madde (aynen `hafiza/sicak.md`'ye yazılan) | ✓ (bu repo eki) |
| + | `cekirdek_adayi` | liste str — Salih "kabul" derse `hafiza/cekirdek.md`'ye | isteğe bağlı (bu repo eki) |
