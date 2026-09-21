---
name: seans-kapanis
description: Alan ajanının seans-KAPANIŞ ritüeli. Salih "seans bitimi" / "kapat" dediğinde koşar; ders kaydı + ilerleme + teslim raporu + kapsül + defter + kütük + commit üretir (push yalnız Salih beyanıyla, m.9). Kullanılmaz; açılışta ("seans başı" → seans-acilis), Jarvis/Friday oturumunda.
---

# Seans bitimi — alan ajanı kapanışı (v0.1, 2026-09-21; Karar 105; Friday seans-kapanis'in alan kopyası)

Kapanış = hafıza yazımıdır: sonraki seans yalnız burada yazılanı devralır.
1. **Ders kapanışı (`ogren` §4):** açık ders dosyası tamamlandı mı (harita · DAG görsel yolu · düğüm/soru/cevap · `## Kalan`); `ogrenme/<şerit>/ilerleme.md` satırı yazıldı mı — pratik `DONE` yalnız Salih beyanıyla, aksi hâlde `KALAN`.
2. **Geri-dönüş notları:** bu seansta devralınan her ders iskeleti / devir birimi için `cc/giden/<id>-geri-donus.md` var mı (şema `../sablonlar/geri-donus-v0.md`; sapma + kural adayı + `cekirdek_adayi`). Yoksa yaz; `.aktif-devir` sil.
3. **Teslim raporu:** `raporlar/seans-teslim-YYYY-MM-DD-<etiket>.md` — beş soru: ne değişti · hangi hüküm geldi/uygulandı · hangi öneri/sapma düştü · sonraki ilk iş · yeniden-açma koşulu. Sayaçlar: kutu sayısı · soru doğru/yanlış · pratik Salih beyanı · model (Sonnet / eskalasyon).
4. **Defter:** `[oneri]` / `[sapma]` satırları `kuyruk/senaryo-defteri.md`'ye, zarf `koken:` alanıyla (Karar 104 M2).
5. **Kapsül tazeleme:** `core/durum-kapsulu.md` üzerine yaz; 4 KB/20 satır birincil, "Şu an" ≤8 madde sigorta — aşan en eski madde `arsiv/kapsul-YYYY-MM-DD.md`'ye + kapsüle `kesildi: <madde> → arsiv/…` satırı (Karar 104 M1, sessiz düşme yasak). Pano kartı güncellenir.
6. **Desenler:** çekirdek adayı yalnız geri-dönüş notunda; `core/desenler.md`'ye doğrudan yazma (Salih kabulü). Seans sayacı +1; 10'da yeniden-oluşum tetiği kapsüle.
7. **Boyut kapısı:** kapsül ≤4 KB/20 satır · defter ≤24 KB · kutu ≤10 KB · `AGENTS.md` ≤4 KB; aşım = damıtma tetiği (teslim raporuna satır).
8. **Kütük:** `veri/bronz/hareket-olay.jsonl` bu oturumun satırlarını taşıyor mu; jarvis/ ya da friday/ yolu var mı — tek satır denetim: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"`. İlk seansta bu sonuç T5 kanıtıdır, geri-dönüş notuna girer.
9. **Commit:** `git add <yol>` (asla `-A`), mesaj İngilizce `[icra] …`; push yalnız Salih "push" derse. Son mesaj: teslim raporunun tam yolu + `open -R` + "Sonraki ders: kutu N'den."
