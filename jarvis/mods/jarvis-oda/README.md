# jarvis-oda

Oda modu: Jarvis (Fable, ana-sıra oturum) planı yazar, görevleri zorluğa göre Haiku / Sonnet / Opus işçi ajanlarına dağıtır, işçi raporları ve önerileri aynı odaya düşer. Pano (Claude Code içi pane) görevlerin canlı durumunu, bekleyen önerileri ve son turları gösterir; öneriyi Salih panodan Kabul/Ret ile karara bağlar. Lobi MCP'sinin oda/tur/öneri işlevinin yerel, çok-ajanlı karşılığıdır.

v0.2: anlık paralel işçi sayısı değişken (`maksParalel`; panoda −/+, araçta `oda_ayar`; sınır doluysa görev kuyruğa girer, biri bitince sıradaki başlar) ve ortak sohbet (panodaki giriş alanından Salih herkese ya da `#N` ile tek işçiye yazar; mesaj koşan işçilerin bağlamına ve Jarvis'e düşer; işçiler `oda_rapor` ile cevaplar; Jarvis `oda_sohbet` ile yazar).

Araçlar: `oda_ac`, `oda_plan`, `oda_gorev_ver`, `oda_ayar`, `oda_sohbet`, `oda_oku`, `oda_oneri_karar`, `oda_oneri` (işçi), `oda_rapor` (işçi). Komut: `/oda`. Ayarlar: `otoUyandir`, `maksParalel`.
