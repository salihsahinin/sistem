# usage/ — koşum-izi asgarisi (Dilim 1.4; karar 07-19)

*(Rapor 10'un DARALTILMIŞ hali: panel yok, dosya-temelli JSONL. Her otomasyon koşumu buraya 1 satır bırakır; alanlar OTel-GenAI/Claude-Code kolonlarıyla hizalı — ileride panel gerekirse veri hazır. m.18: makine-yüzü = bu dosyalar; insan-yüzü = tek satır özet; talep-üzerine = jq projeksiyonu.)*

- `senkron-log.jsonl` — gecelik senkron scripti (ilk müşteri; token=0 satırları da yazılır: kadans-kanıtı).
- Şema: `{ts, event, status, from, to, dirty_files, dur_s, agent, class?, model, effort?, tokens, cost_usd?}` — LLM'li koşumlar tokens/cost doldurur (/usage ya da headless JSON'dan).
- `SENKRON-UYARI.md` — yalnız FAIL'de satır alır; sabah ilk oturum bakar (C-aşısı insan-anı).
