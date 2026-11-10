# arsiv/gorunum-2026-11-10

**Ne var:** `veri/gorunum/` altından inen 13 gold görünüm (csv). Üreticileri 2026-11-10 depo denetiminde arşive indi (`../../arsiv/kod/python/tools/`: asof-eval, d2-eval, denetci-kalibrasyon, erisim-kalibrasyon, erisim-vektor, headless-esleme, kural-envanter, pano-akis, silver-saglik-kalibrasyon); son üretim 2026-09-22.

**Neden indi:** `katman-olcum` tazelik testi bu dosyaları her koşumda `ERROR` sayıyordu (yaş 48,9 gün) ve `katman-hatti` bu yüzden hep hata koduyla bitiyordu. Üretici koşmadığı için görünüm yenilenmez; kayıt olarak burada durur (m.8).

**Geri alma:** üretici betiği `tools/` altına, csv'yi `veri/gorunum/` altına `git mv` ile geri taşı.
