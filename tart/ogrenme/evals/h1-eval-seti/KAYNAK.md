# Kaynak damgası (m.39, md.49)

- Veri: GSM8K (`openai/grade-school-math`), dosya `grade_school_math/data/test.jsonl`, ilk 20 satır.
- URL: https://raw.githubusercontent.com/openai/grade-school-math/master/grade_school_math/data/test.jsonl
- Lisans: MIT (repo `LICENSE`, Copyright (c) 2021 OpenAI) — canlı doğrulandı 2026-09-11.
- Çekiliş tarihi (AS-OF): 2026-09-11.
- md.49: tamamı kamu veri, şirket/staj bağlantısı yok.
- Dönüştürme: her satırın `question` alanı → `soru`; `answer` alanındaki `#### <sayı>` son satırı → `beklenen` (ara-adım muhakemesi atıldı, yalnız nihai sayısal cevap alındı).
