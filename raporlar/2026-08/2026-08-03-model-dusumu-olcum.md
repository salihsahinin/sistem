# Model-Düşümü Ölçüm Raporu — 2026-08-03 (temiz oturum, Carvis/Fable)

*Kapsül "Sonraki ilk iş #2"nin icrası (Salih emri 08-03 günaydın: "modeli düşüren bağlamı test edip semantik olarak onar"). Kaynak veri: 08-02→08-03 ana-sıra oturumunun audit JSONL'i (`local_2574c7d7…/audit.jsonl`, 1.068 satır; erişim: Salih-onaylı klasör mount'u). Damga: ölçüm deterministik (sayım), yorum kısmı m.29 deneysel.*

## 1. Ölçüm sonucu (sayım, tartışmasız)
- Modelli mesaj: **202** — `claude-fable-5` **179** · `claude-opus-5` **23**.
- **Tek geçiş, geri dönüş yok:** satır 975, `2026-08-02T21:40:15Z` = **03 Ağu 00:40:15 TR**.
- Satır 973 (00:40:04): `rate_limit_event` — `rateLimitType: five_hour`, `overageStatus: rejected` (`org_level_disabled`), `resetsAt` = 03 Ağu **05:30 TR**.
- Satır 975: **açık fallback kaydı** — `{"type":"fallback","from":"claude-fable-5","to":"claude-opus-5"}`. Sessiz/içerik-tetikli değil; sistem düşümü kendisi beyan etmiş.

## 2. Zaman çizgisi ↔ kanon eşlemesi (TR saati)
| An | Olay | Model |
|---|---|---|
| 22:29 | oturum açılışı | fable |
| 22:38 | `3cc20c4` B1+B3 icra | fable |
| 00:13 | `7d3bc35` **K2 masası 15/15** | fable |
| 00:35 | `e289172` iki görev emri | fable |
| 00:40:04 | rate_limit_event (five_hour) | — |
| **00:40:15** | **FALLBACK → opus** | opus |
| 00:40–00:53 | süreç-temizliği kuyruğu · tespit-protokolü cevabı · kapanış yazımları + `52ce471` | opus |

## 3. Hipotez hükmü (üçlü ayrıştırma, teslim raporu §4'ün cevabı)
- **KOTA = birincil neden (KESİN):** fallback kaydı rate-limit olayına bitişik, five_hour penceresi dolu, overage kapalı. İçerik-bağımsız.
- **BAĞLAM = tek başına neden DEĞİL, hızlandırıcı (ölçülü):** fallback anında bağlam ~237K token (172.431 cache-yazım + 64.436 cache-okuma). Kritik tanılama: `cache_miss_reason: tools_changed` — **151.647 token cache-dışı kaldı**. Fable'ın düşüm öncesi SON eylemi `ToolSearch "computer-use"` (30 araç birden yükleme) → araç seti değişti → prompt-cache kırıldı → ~172K token yeniden faturalandı → pencere doldu → fallback. Yani Salih'in sezgisi kısmen doğru: bağlam modeli doğrudan düşürmedi ama **büyük bağlam × araç-seti değişimi = ani maliyet sıçraması** düşümü tetikleyen son damla oldu.
- **SAFEGUARD/`cyber`-yem = bu vaka için YANLIŞLANDI:** düşüm içerik-tetikli değil; şerhli ingest'in 4. kalemi (yem hipotezi) bu olayın kanıtını kaybetti. KG-CC-2/md.10 hattı ayrı vakadır, bu ölçüm onu etkilemez.

## 4. Şerh kapsamı — KESİNLEŞTİ
- **ŞERHLİ (opus):** son iki cevap + bir önceki cevabın 00:40:15 sonrası kuyruğu (yalnız konuşma metni — Görev Yöneticisi/UIPI tavsiyesi; dosya yazımı yok).
- **ŞERHSİZ KESİN:** K2 masası 15/15 · B1/B3 · md.1-49 özeti · iki görev emri · defter K2 bloğu — tümü düşümden 5 dk–2 saat ÖNCE ve commit'li. **Teyit turu GEREKMEZ; K2 kararları koşulsuz yürürlükte.**
- **Semantik denetim (onarım talebi):** opus'un yazdığı 4 kapanış artefaktı (şerhli ingest · teslim raporu · kapsül · pano) + `52ce471` push'u fable-dönemi olgulara ve origin commit'lerine karşı satır satır doğrulandı — **olgu-bozulması YOK, onarım gerektiren içerik ÇIKMADI.** Kapsam beyanı ("son iki cevap") ölçümle birebir; tek eksik, kuyruk-parçasının beyan dışı kalmasıydı (etkisiz — dosya yazımı yok).

## 5. Şerhli 5 kalemin ölçüm-sonrası statüsü (kanona geçiş kararı Salih'te — Katman-1)
1. UIPI hükmü — içerik doğru görünüyor; saha-doğrulama borcu sürüyor (statü değişmedi).
2. K-018 çıkarımı — öneri, imzasız (statü değişmedi).
3. Tespit protokolü — **KOŞULDU ve DOĞRULANDI** (bu rapor protokolün ilk icrası).
4. `cyber`-yem hipotezi — **bu vaka için YANLIŞLANDI**; "ayrı teknik oturum" usul önerisi imzasız kalır, motive eden kanıtı düştü.
5. Tek-betik yakınsaması — **DOĞRULANDI:** audit.jsonl hem `model` hem `usage` (token/maliyet) taşıyor; usage-otomasyon borcu (Salih emri 08-02) ile tespit aynı betikte çözülür. Yol seçimi (parse betiği / OTLP / ccusage) m.40 gereği kısa dış araştırma sonrası — defterdeki aday statüsü sürüyor.

## 6. Ders adayı (imzasız usul — Salih kararına)
**D-0803-1:** Büyük-bağlamlı oturumun geç evresinde toplu araç-yükleme (ToolSearch ile N araç) prompt-cache'i kırar → tek turda yüz-binlerce token yeniden faturalanır → kota-fallback riski. Usul adayı: ağır araç-yüklemeleri oturum BAŞINDA yapılır ya da ayrı oturuma taşınır; oturum sonuna doğru yeni araç-ailesi açılmaz.

## 7. Tekrar üretilebilirlik
```python
import json
rows=[(i,d.get('timestamp'),d['message']['model'])
      for i,l in enumerate(open('audit.jsonl'),1)
      if (d:=json.loads(l)).get('message',{}).get('model') if isinstance(d.get('message'),dict) else None]
prev=None
for i,ts,m in rows:
    if m!=prev: print('GECIS',i,ts,prev,'->',m); prev=m
```
Ek işaretler: `"type":"rate_limit_event"` satırları · `"type":"fallback"` içerik bloğu · fallback mesajındaki `usage`/`diagnostics` alanları.
