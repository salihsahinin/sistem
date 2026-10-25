---
name: seans-kapanis
description: Friday'in seans-KAPANIŞ ritüeli. Salih "seans bitimi" / "kapat" dediğinde koşar; durum kütüğü + JSON teslim kaydı (`durum seans-kapat`; graf + Salih özeti otomatik) + defter + kütük + commit + dal push + PR üretir. md teslim raporu, kapsül ve pano yazılmaz (Karar 121/122). Kullanılmaz; açılışta ("seans başı" → seans-acilis), Jarvis oturumunda.
---

# Seans bitimi — Friday kapanışı (v0.2, 2026-10-25; Karar 121/122 graf + JSON; v0.1 09-09 Jarvis kopyası)

Hüküm `jarvis/lean/Kanon/AkisGraf.lean`: kayıt tam değilse (hedef cümlesi, sonraki ilk iş, ölçüm) kapanış yoktur. Kapanış = hafıza yazımıdır: sonraki seans yalnız kütükte ve kayıtta olanı devralır.
1. **Geri-dönüş notları:** bu seansta devralınan her devir birimi için `cc/giden/<devir_id>-geri-donus.md` var mı (şema `../sablonlar/geri-donus-v0.md`; 10+2 alan). Yoksa yaz; yazamıyorsan `durma_nedeni` ile yaz; `.aktif-devir` sil.
2. **Durum kütüğü (graf düğümleri):** bu seansta ele alınan her iş kütükte doğru durumda mı: `durum al <id> --oturum <oturum>` · `durum bitir <id> --oturum <oturum> --kanit ".."` · yarım kalan `bitir --kalan "iş|sonraki eylem"` · yeni iş `durum ac --alan friday --is ".." --sonraki ".." [--girdi a,b] [--hedef N] --oturum <oturum>`. Kütüğe yazılmayan iş sonraki seansta **yoktur**.
3. **Teslim kaydı (JSON, Karar 121):** girdi `raporlar/seans/seans-teslim-girdi-<tarih>.json` (şablon `../ortak/sablon/seans-teslim-girdi.json`; `sayaclar`: ajan çağrısı · işçi araç çağrısı · alt-ajan token `[?]`). Cümleler Türkçe, kısa, etken, tek fikirli (ASD-STE100). Sonra `durum seans-kapat --alan friday --oturum <oturum> --girdi raporlar/seans/seans-teslim-girdi-<tarih>.json --etiket <etiket> --render` → kayıt `raporlar/seans/seans-teslim-<tarih>-<etiket>.json`, graf ve `../ortak/SALIH-OZET.md` yenilenir. md teslim raporu yazılmaz; girdi dosyası silinmez (m.8).
4. **Defter:** `[oneri]` / `[sapma]` satırları `kuyruk/senaryo-defteri.md`'ye; kural adayı varsa ayrıca `cc/giden/` notuna.
5. **Kapsül/pano:** **dondu** (Karar 122): yazılmaz. Konum = kütük + kayıt.
6. **Desenler:** çekirdek adayı varsa geri-dönüş notunun `cekirdek_adayi` alanına; `core/desenler.md`'ye doğrudan yazma (Salih kabulü).
7. **Boyut kapısı:** defter ≤24 KB · kutu ≤10 KB; aşım = damıtma tetiği (kayda `adaylar` satırı).
8. **Kütük:** `veri/bronz/hareket-olay.jsonl` bu oturumun satırlarını taşıyor mu (hook); okunan yollar repo dışına çıkmış mı — tek satır denetim: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"`.
9. **Commit + push + PR (EK-5):** `git add <yol>` (asla `-A`): `raporlar/seans/*.json` · `../ortak/durum-olay.jsonl` · `../ortak/akis-graf.json` · `../ortak/graf/` · `../ortak/SALIH-OZET.md` · defter · `cc/giden/`; mesaj İngilizce `[icra] …`; `git push -u origin <dal>` + `gh-axi pr create`; birleştirme Jarvis'te Salih "birleştir #N" deyince. Son mesaj: PR linki + kayıt yolu + `../ortak/graf/akis-friday.svg`.

Bilinen sınır: `ortak/durum-olay.jsonl` worktree'de kopyadır; iki yan oturum aynı anda `ac` yaparsa id çakışır (durum #27).
