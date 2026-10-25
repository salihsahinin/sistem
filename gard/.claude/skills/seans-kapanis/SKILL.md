---
name: seans-kapanis
description: Alan ajanının seans-KAPANIŞ ritüeli. Salih "seans bitimi" / "kapat" dediğinde koşar; ders kaydı + ilerleme + durum kütüğü + JSON teslim kaydı (`durum seans-kapat`; graf + Salih özeti otomatik) + defter + commit + dal push + PR üretir. md teslim raporu, kapsül ve pano yazılmaz (Karar 121/122). Kullanılmaz; açılışta ("seans başı" → seans-acilis), Jarvis/Friday oturumunda.
---

# Seans bitimi — alan ajanı kapanışı (v0.2, 2026-10-25; Karar 121/122 graf + JSON; v0.1 09-21 Karar 105 Friday kopyası)

Kaynak: `sablonlar/ajan-iskelet/claude-ayar/skills/seans-kapanis/SKILL.md` (doğurucu her alan ajanına kopyalar). Hüküm `jarvis/lean/Kanon/AkisGraf.lean`: kayıt tam değilse (hedef cümlesi, sonraki ilk iş, ölçüm) kapanış yoktur.

Kapanış = hafıza yazımıdır: sonraki seans yalnız kütükte ve kayıtta olanı devralır.
1. **Ders kapanışı (`ogren` §4):** açık ders dosyası tamamlandı mı (harita · DAG görsel yolu · düğüm/soru/cevap · `## Kalan`); `ogrenme/<şerit>/ilerleme.md` satırı yazıldı mı — pratik `DONE` yalnız Salih beyanıyla, aksi hâlde `KALAN`.
2. **Geri-dönüş notları:** bu seansta devralınan her ders iskeleti / devir birimi için `cc/giden/<id>-geri-donus.md` var mı (şema `../sablonlar/geri-donus-v0.md`; sapma + kural adayı + `cekirdek_adayi`). Yoksa yaz; `.aktif-devir` sil.
3. **Durum kütüğü (graf düğümleri):** bu seansta ele alınan her iş kütükte doğru durumda mı: başlanan `durum al <id> --oturum <oturum>` · biten `durum bitir <id> --oturum <oturum> --kanit "<commit/dosya>"` · yarım kalan `bitir --kalan "iş|sonraki eylem"` (zincir kenarı otomatik) · yeni iş `durum ac --alan <alan> --is ".." --sonraki ".." [--girdi a,b] [--hedef N] --oturum <oturum>`. Oturum adı açılışta `seans-ac`'ın verdiği ad. Kütüğe yazılmayan iş sonraki seansta **yoktur**.
4. **Teslim kaydı (JSON, Karar 121):** girdi dosyasını yaz: `raporlar/seans/seans-teslim-girdi-<tarih>.json` (şablon `../ortak/sablon/seans-teslim-girdi.json`; alanlar: `hedef` · `hedef_tutuldu` · `sapma` · `ne_degisti` · `kararlar` · `adaylar` · `sonraki_ilk_is` · `yeniden_acma` · `salih_karar` · `baglar` · `sayaclar` (kutu sayısı · soru doğru/yanlış · pratik Salih beyanı · model)). Cümleler Türkçe, kısa, etken, tek fikirli (ASD-STE100): Salih özetine aynen girer. Sonra: `durum seans-kapat --alan <alan> --oturum <oturum> --girdi raporlar/seans/seans-teslim-girdi-<tarih>.json --etiket <etiket> --render` → Rust ölçümleri ekler (git, durum sayaçları, süre), kaydı `raporlar/seans/seans-teslim-<tarih>-<etiket>.json`'a yazar, `../ortak/akis-graf.json` + `../ortak/graf/akis-*.d2/.svg` + `../ortak/SALIH-OZET.md`'yi yeniden üretir. md teslim raporu yazılmaz; girdi dosyası silinmez (m.8).
5. **Defter:** `[oneri]` / `[sapma]` satırları `kuyruk/senaryo-defteri.md`'ye, zarf `koken:` alanıyla (Karar 104 M2).
6. **Kapsül/pano:** `core/durum-kapsulu.md` ve `core/pano.md` **dondu** (Karar 122): yazılmaz. Konum = kütük + kayıt.
7. **Desenler:** çekirdek adayı yalnız geri-dönüş notunda; `core/desenler.md`'ye doğrudan yazma (Salih kabulü).
8. **Boyut kapısı:** defter ≤24 KB · kutu ≤10 KB · `AGENTS.md` ≤4 KB; aşım = damıtma tetiği (kayda `adaylar` satırı).
9. **Kütük:** `veri/bronz/hareket-olay.jsonl` bu oturumun satırlarını taşıyor mu; jarvis/ ya da friday/ yolu var mı — tek satır denetim: `python3 -c "import json;print(sorted({json.loads(l)['yol'] for l in open('veri/bronz/hareket-olay.jsonl') if json.loads(l)['yol']}))"`. İlk seansta bu sonuç T5 kanıtıdır, geri-dönüş notuna girer.
10. **Commit + push + PR (EK-5):** `git add <yol>` (asla `-A`): ders dosyaları · `raporlar/seans/*.json` · `../ortak/durum-olay.jsonl` · `../ortak/akis-graf.json` · `../ortak/graf/` · `../ortak/SALIH-OZET.md` · defter; mesaj İngilizce `[icra] …`. Sonra `git push -u origin <dal>` ve `gh-axi pr create` (açıklamada "yalnız bu oturumun commit'leri"); birleştirme Jarvis'te Salih "birleştir #N" deyince. Son mesaj: PR linki + kayıt yolu + `../ortak/graf/akis-<alan>.svg` + "Sonraki ders: kutu N'den."

Bilinen sınır: `ortak/durum-olay.jsonl` worktree'de kopyadır; iki yan oturum aynı anda `ac` yaparsa id çakışır (durum #27). Yeni iş açarken PR'ı gecikmeden aç.
