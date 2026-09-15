---
name: karar-masasi
description: Salih'e sunulacak bekleyen hükümleri Lavish karar masası (DaisyUI HTML, kalem başına seçenekli açıklama bloğu, kuyrukla script'i) olarak deterministik üretir ve kalıcı kopyasını alır. Kullan; "karar masasına aç/taşı", "masa hazırla", "bende bekleyen hükümleri masaya koy", "lavish ile karar masası" dendiğinde ya da ölçek-eşiği üstü ≥2 hüküm birikince. Kullanma; tek kararlık sohbet-içi sunumda (karar-modeli yeter), masa hükümlerini deftere yazmak için (karar-kaydet), hükmü Salih yerine vermek için.
metadata: { owner: jarvis, version: "0.2.0-deneysel-m29", kural: "core/skill-uretim-semasi.md §4b", ib: "İB-88 P2", karar: "Karar 96 M2/M5" }
---

# karar-masasi — masa üretim talimatı (v0.2 P2 gövde + baseline, 2026-09-15)

Test: `python3 .claude/skills/karar-masasi/scripts/masa-uret-test.py` (E1-E3, 12/12; masa-12 eşdeğerlik). Eski masayı spec'e döken tersine araç: `scripts/masa-spec-cikar.py <masa.html>`. Baseline karşılaştırması `evals/evals.json` → `p2_sonuc`.

Tür: T-Ü üretici (yan-etki: dosya yazımı `raporlar/masa/` + `kaynak-kodu/lavish/`; kanona yazmaz). Kaynak biçim: 7.-12. masalar (elle DaisyUI, Salih 09-08 "fable 5 ile kurulan karar masaları formatı"). Tekrar sayımı 09-15: 11 masa elle (~200 satır/masa). Deterministik gövde `scripts/masa-uret.py`; şablon `sablon.html`.

## Adımlar
1. **Kalem spec'ini yaz** (`kuyruk/masa-spec-N-YYYY-MM-DD.json`; şema aşağıda). Her kalem: ad · rozet (Katman-1/2 · tür) · "ne demek" · seçenekler (etiket · value · açıklama bloğu: ne yaparım · artı · eksi · gerekçe) · `oneri` bayrağı (önerilen **ilk** sırada, m.40 eki) · `coklu` (checkbox). Kanıt tablosu satırları kaynak + etiket (D/K/X ∨ "sayım") taşır (m.39).
2. **Bayat-satır çapraz okuması (Karar 74 dersi):** her kalem için kapsül + defter son 30 satır taranır; zaten kapanmış kalem masaya girmez, "masa öncesi fiilen yapıldı" satırına iner (m.16).
3. **Üret:** `python3 .claude/skills/karar-masasi/scripts/masa-uret.py <spec.json>` → `kaynak-kodu/lavish/masa-N-YYYY-MM-DD.html` + kalıcı kopya `raporlar/masa/masa-N-karar-yuzeyi-YYYY-MM-DD.html`; çıktı yolu + kalem sayısı + doğrulama (form sayısı = kalem sayısı) basılır.
4. **Aç + bekle:** `lavish-axi <html>` → URL Salih'e; `lavish-axi poll <html>` harness-izli arka planda (Bash run_in_background); "Send & End" gelince poll çıktısı tam okunur (prompt alanları), hükümler seçenek metniyle aynen deftere `karar-kaydet` ile iner (bu skill yazmaz).
5. **Sunum cümlesi:** URL + kalıcı yol + kalem listesi (her kalemde önerilen); övgü yok, çıplak veri (m.7).

## Spec şeması (JSON)
```json
{"no": 12, "tarih": "2026-09-15", "baslik": "…", "giris": "opsiyonel giriş cümlesi", "tetik": "Salih beyanı aynen", "once_yapildi": "…", "asof": "…",
 "kanit": [{"bulgu": "…", "deger": "…", "kaynak": "…", "etiket": "D"}],
 "hakem": "opsiyonel metin",
 "kalemler": [{"id": "M1", "baslik": "…", "rozet": "Katman-1 · kural", "ne_demek": "…", "coklu": false,
   "secenekler": [{"etiket": "(a) …", "value": "hüküm metni", "oneri": true, "aciklama": "Ne yaparım: … Artı: … Eksi: … Gerekçe: …"}]}],
 "karar_no": "Karar 97"}
```

## Gotchas
- Bu skill commit yapmaz, deftere yazmaz (yan-etki freni): kayıt `karar-kaydet`, commit seans akışı.
- Önerilen seçenek ilk sırada değilse script hata verir (m.40 eki sözleşmesi).
- Seçenek `value` metni hüküm olarak deftere aynen iner; kısaltma yapma, kanon terimleriyle yaz.
- Masa numarası `raporlar/masa/` içindeki son numaradan +1; elle vermek çakışma üretir.
- Büyük harf vurgusu yok (Stop hook 09-15); vurgu `<strong>`.
- Lavish oturumunu Salih kapatırsa yeniden açma (`--reopen` yalnız istekle).
