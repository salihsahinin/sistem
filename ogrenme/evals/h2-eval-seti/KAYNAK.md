# Kaynak damgası (m.39, md.49)

- Soru metinleri: aynı 20 GSM8K vakası, bkz. [`../h1-eval-seti/KAYNAK.md`](../h1-eval-seti/KAYNAK.md) (pointer, m.20 — tekrar dökülmedi).
- Bu setin farkı: aynı sorulara 3 farklı deterministik assert türü (contains/regex/equals+transform) uygulanmış + 1 bilerek-kırmızı vaka eklenmiş (H2 `DONE`: "20 vakaya 3 deterministik assert türü; ilk kırmızı vakayı bilerek üret").
- Kırmızı vaka (21.) GSM8K'tan değil, sanity-check için bilerek yanlış beklenen değerle yazılmış basit bir aritmetik sorudur — açıkça etiketli.
- promptfoo assert söz dizimi (`equals`, `regex`, `transform`) canlı doğrulandı: promptfoo docs, AS-OF 2026-09-11.
