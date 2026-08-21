# İngest Şeması v2 — Kayıt Katmanı (AKTİF: Salih emri 2026-08-14)

*v1'in (`kuyruk/oneri-ingest-sema-v1.md`, Salih imzalı 07-12: K3→K0 katmanları + G1/G2/G3 kapıları + V9 önem formülü) ÜZERİNE oturur, onu değiştirmez. v1 katmanları tanımlıyordu; v2 KAYDIN KENDİSİNİ tanımlar: zarf, tip, triyaj, bütçe. Kanıt tabanı: `cc/rapor-2026-08-14-1.md` (Opus lider koşumu, D-ağırlıklı). Tüm eşikler deneysel m.29; veto = revert.*

## 1. Kayıt zarfı — 5 zorunlu alan, fazlası YOK

Her ingest kaydı (devir dosyasındaki her madde) tek satır zarf taşır:

```
[tip: karar | kaynak: jarvis-terminal 08-14 | tarih: 2026-08-14 | hedef: defter | sema: v2]
```

- **Zorunlu 5:** `tip` · `kaynak` (yüzey+hat+tarih — çift-girişi yakalayan dedup anahtarı) · `tarih` · `hedef` (bilinmiyorsa `-`) · `sema`.
- **syslog kuralı:** alan başlığı hep durur, değer `-` olabilir ("doldurulmadı" ≠ "yok").
- **Opsiyonel ama yazılırsa katı:** `onem: 1-10` · `gecerli-bitis:` · `baglanti: [[wiki-adı]]` · `dogrulama:` (borçta DONE prosedürü).
- Gerekçe: en olgun standartlar 0-5 zorunlu alanla yaşıyor (ODCS/CloudEvents/Dublin Core); ağır şema = ölü şema (tek zorunlu adım kaldırınca +%45 dönüşüm — rapor D.3).

## 2. Tip kümesi — KAPALI, 8 değer

| tip | hedef (varsayılan yönlendirme) |
|---|---|
| `karar` | senaryo-defteri (LangMem formatı: durum + akıl-yürütme + sonuç + geri-açma) |
| `kural-adayı` | kuyruk → G2 kapısı (yalnız Salih imzasıyla kanonlaşır) |
| `borç` | kapsül "Açık borçlar" / pano — **`dogrulama:` alanı zorunlu; DONE = prosedür KOŞTU, "yapıldı yazıldı" değil** |
| `bulgu` | rapor / wiki-delta |
| `ders` | KILAVUZ (gotcha/tuzak) |
| `kavram` | wiki (A-MEM alan seti: içerik+etiket+bağlam-açıklaması+`[[bağlantı]]`) |
| `ham` | kuyruk/gelen-*.md (bronz; işlenmemiş) |
| `diger` | DLQ adayı — sayaç yükselirse yeni tip doğuyor demektir (additive-only genişlet, tip SİLME → deprecated) |

## 3. Triyaj — her kayıt için 4 soru (Mem0 uyarlaması)

İngest anında, aynı tip/etiketi taşıyan mevcut kanon kayıtlarına bakılır:

1. **Eşdeğeri var mı? → NOOP** (kayda "NOOP" damgası, kanona dokunma).
2. **Tamamlıyor mu? → UPDATE** (mevcut kaydı güçlendir, yeni kayıt açma).
3. **Çelişiyor mu? → GEÇERSİZ-KIL** (silme YOK — m.8/m.16: eski kayda `gecerli-bitis:` damgası = yeni kaydın tarihi; çelişki Katman-1 sınıfındaysa çelişki-kapısı raporu Salih'e). **Yayılım fıkrası (08-15, `core/baglam-anahtar-kaydi.md` §3):** çelişen kayıt bir ANAHTAR değerini (kavram/tetik/ad/yüzey) değiştiriyorsa damga tek başına yetmez — anahtar kaydına `emekli` satırı + sıcak-katman kalıntı-referanslarının aynı seansta yeniden yazımı (RESTRICT: kalıntı varken emeklilik tamamlanmamış sayılır); denetim `python3 tools/anahtar-denetim.py`.
4. **Hiçbiri → ADD** (tipin varsayılan hedefine yaz).

## 4. Kaynak-doğruluk kuralı (event sourcing)

**Kapsül SNAPSHOT'tır, gerçek kaynak DEĞİLDİR.** Gerçek kaynak: `kuyruk/` (append-only log) + `senaryo-defteri` + git log. Kapsül kaybolsa sistem bunlardan yeniden kurulabilir olmalı. Kuyruk kaydı **silinmez**; hata düzeltme = telafi kaydı ekle ("düzeltme:" önekiyle). Pano = projeksiyon.

## 5. Tetikler ve bütçeler (deneysel m.29)

- **Kapsül tavanı ≤200 satır** (Claude Code limiti emsal). ~140 satırda (%70) açılış brifinde damıtma uyarısı; tavanda zorunlu damıtma turu, ~%50 boşaltılır (MemGPT üçlüsü).
- **Kümülatif önem tetiği:** kuyruğa giren kayıtların `onem` toplamı ≥150 → damıtma turu açılır (G3'ün 40-madde eşiğine EK; 40 önemsiz not tetiklemez, 8 kritik not tetikler — Generative Agents). **λ düzeltmesi (KB-42 A, Salih imzası 2026-08-21, Karar 59 — eski metin "0.99/gün": değer VE birim kaynakla çelişiyordu, B2-2 SAĞLAM):** birincil kaynakta çürüme **0,995/sandbox-SAATİ** (Park ve ark. 2023, ar5iv 2304.03442; α_tazelik=α_önem=α_ilgililik=1 — gerekçesiz, duyarlılık analizi yok). Jarvis'e DEĞER TAŞINMAZ (sandbox-saatinin seans karşılığı tanımsız); yalnız FORM korunur: **tazelik(t) = d^t** — t = geçen SEANS sayısı (Jarvis zaman-atomu), d ∈ (0,1) çürüme tabanı **KALİBRE EDİLMEMİŞ [?]** (yerel ölçümle doğar; m.29/m.35 — ölçüm gelene dek getirme skorunda tazelik terimi kullanılmaz, tetik yalnız Σönem≥150). Genel kural (T-Ç6, silver-sağlık emsali): kanona giren her katsayı kaynaktaki DEĞER ve BİRİMLE eşleşir; eşleşmeyen "kalibre edilmemiş" damgası taşır. λ bugüne dek hiçbir script/koşumda kullanılmadı (grep doğrulaması 08-21) — geriye dönük etki yok.
- **Devir raporu bütçesi:** paralel sekmeden ana hatta dönen devir **≈1.000-2.000 token (≈4-8KB)** tavanlı. Korunacak: kararlar + çözülmemiş sorunlar + doğrulama adımları; atılacak: araç çıktıları. Sıra: önce recall, sonra precision (Anthropic).
- **Damıtma frekansı:** her oturumda değil, EŞİKTE ve TOPLU (LSM: her damıtma bir maliyettir).

## 6. DLQ — sınıflandırılamayan kayıt kanalı

`kuyruk/SINIFLANDIRILAMADI.md`: 2 seans içinde tip/hedef alamayan kayıt buraya taşınır (kaynağından telafi-notuyla). **Sessiz düşürme yasak** — silinmez, açılış taramasında yeniden denenir (redrive). Burası çöp kutusu değil bekleme/inceleme alanıdır.

## 7. Çok-sekme protokolü (şemanın ana kullanım akışı)

- **Her sekme/oturum kapanışta TEK bronz dosya bırakır:** jarvis hattı → `kuyruk/gelen-YYYY-MM-DD-<konu>.md` (zarflı kayıt listesi, §5 bütçesinde); staj hattı → kendi şeması (`~/staj başlangıç/ingest-semasi.md`; jarvis'e VERİ akmaz — md.49).
- **Triyajı ana-sıra koşar** (seans açılış/kapanış ritüelinin parçası): bronz dosyaları §3 sorularından geçirilir, hedeflerine dağıtılır, dosya "İNGEST EDİLDİ" damgası alır.
- **Şema evrimi:** additive-only — yeni zorunlu alan ASLA eklenmez; yeni alan opsiyonel+varsayılanlı; alan/tip silinmez → deprecated (Avro/Protobuf/m.8).

## 8. Ölçüm (m.35 — şemanın ilk deneği kendisi)

Seans teslimlerine sayaçlar: `giren / NOOP / UPDATE / GEÇERSİZ-KIL / ADD / DLQ`. ~10 seans sonra eşikler (150, 200 satır, 2k token) ilk kez gerçek veriyle kalibre edilir (v1 §3 sayaçlarıyla aynı havuz).
