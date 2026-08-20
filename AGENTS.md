# AGENTS.md — Jarvis (STATİK KOPYA, 2026-08-21)

> **Bakım rejimi (Salih hükmü, 08-21 Karar 47):** Bu dosya STATİK bir işaret levhasıdır — SENKRON BAKIM YAPILMAZ. Claude Code bu dosyayı okumaz (tek kaynağı `CLAUDE.md`); bu dosya Claude-dışı ajan araçları (Codex vb.) sisteme girdiğinde onların ilk durağıdır ve o gün güncellenip canlı bakıma alınır. Çelişkide `CLAUDE.md` + `core/tuzuk-v0.md` kazanır.

## Bu depo nedir
Jarvis: Salih'in (tek karar verici) kişisel işletim sistemi — bağlam veri ambarı + skill hazinesi + karar süreci. Açık-kaynak okunabilirlik ilkesiyle yazılır: her hareket, kural ve kaynak bu depoda düz dosyadır; gizli klasör yoktur (nokta-dizinlerin kapısı `kaynak-kodu/`).

## Ajan isen önce bunu oku (sıra)
1. `CLAUDE.md` — davranış sözleşmesi (bütçeli, tek kaynak).
2. `core/durum-kapsulu.md` — şu an + sıradaki iş.
3. `core/pano.md` — kartlar; `core/tuzuk-v0.md` — kural kaynağı (m.NN).

## Pazarlıksız kurallar (özet; tam metin tüzükte)
- **Salih tek karar vericidir.** Katman-1 (kanon/kural değişikliği, silme, geri-alınması zor iş, dışarı çıkacak iş, para) YALNIZ Salih kararıyla. Ajan yapar + kaydeder + commit'ler; veto = revert (m.31).
- **Çelişki kapısı (m.16):** önceki kararla çelişen işte önce çelişki + artı/eksi + plan raporu, sonra icra.
- **`git push` yalnız Salih beyanıyla** (m.9). Otomatik silme yasak (m.8) — arşive indir + pointer bırak.
- **Kaynak dosyalar Türkçe** (kod tanımlayıcıları, SQL/JSON anahtarları, commit mesajları İngilizce — m.10).
- Sırlar yalnız `.secrets/` + üçüncü-şahıs verisi (md.49); içerik gizli, klasör görünür.
- Her rakam kaynaklı ve deneysel damgalı (m.29, m.39); teslim = çıktı + üreten kaynağın yolu.

## Yerleşim
`core/` kanon · `kuyruk/` karar defteri + kutular · `raporlar/` teslimler · `cc/` görev emirleri + pipeline'lar · `wiki/` kavramlar · `veri/` bronz + `baglam.sqlite` (silver) + `gorunum/` (gold) · `tools/` script'ler (`SCRIPTLER.md`) · `.claude/` skill + hook + ayar.
