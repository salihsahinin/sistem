---
name: seans-kapanis
description: Friday'in seans-KAPANIŞ ritüeli. Salih "seans bitimi" / "kapat" dediğinde koşar; teslim raporu + kapsül + defter + kütük + commit üretir (push YOK, m.9). KULLANILMAZ; açılışta ("seans başı" → seans-acilis), Jarvis oturumunda.
---

# Seans bitimi — Friday kapanışı (v0.1, 2026-09-09; Jarvis seans-kapanis'in küçük kopyası)

Kapanış = hafıza yazımıdır: sonraki seans yalnız burada yazılanı devralır.
1. **Geri-dönüş notları:** bu seansta devralınan her devir birimi için `cc/giden/<devir_id>-geri-donus.md` VAR mı (şema `core/sablonlar/geri-donus-v0.md`, 10+2 alan). Yoksa yaz; yazamıyorsan `durma_nedeni` ile yaz.
2. **Teslim raporu:** `raporlar/seans-teslim-YYYY-MM-DD-<etiket>.md` — beş soru: ne değişti · hangi hüküm geldi/uygulandı · hangi öneri/sapma kaydı düştü · sonraki ilk iş · yeniden-açma koşulu. Sayaçlar: ajan çağrısı · işçi araç çağrısı · alt-ajan token (kestirim `[?]`).
3. **Defter:** `[oneri]` / `[sapma]` satırları `kuyruk/senaryo-defteri.md`'ye; kural adayı varsa ayrıca `cc/giden/` notuna.
4. **Kapsül tazeleme:** `core/durum-kapsulu.md` üzerine yaz; "Şu an" ≤8 madde — taşan en eski madde `arsiv/kapsul-YYYY-MM-DD.md`'ye (FIFO, silme yok). Pano kartını BİTEN'e taşı.
5. **Desenler:** çekirdek adayı varsa geri-dönüş notunun `cekirdek_adayi` alanına; `core/desenler.md`'ye DOĞRUDAN YAZMA (Salih kabulü). Koşum sayacı +1; 10'da yeniden-oluşum tetiği kapsüle.
6. **Boyut kapısı:** kapsül ≤4 KB/20 satır · defter ≤24 KB · kutu ≤10 KB; aşım = damıtma tetiği (teslim raporuna satır).
7. **Kütük:** `veri/bronz/hareket-olay.jsonl` bu oturumun satırlarını taşıyor mu (hook); okunan yollar repo + `kanon/` dışına çıkmış mı — `sema` alanı olmayan satırlar (09-10 öncesi v0.1) kapsam DIŞI; tek satır denetim: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"`.
8. **Commit:** `git add <yol>` (asla `-A`), mesaj İngilizce `[icra] …`; push YOK. Son mesaj: teslim raporunun tam yolu + `open -R`.
