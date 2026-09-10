# gnhf

*AS-OF 2026-09-03 (yazım: İB-04 wiki kuyruğu; kural kaynağı `wiki/README.md` 6-blok standardı — çelişkide kanon kazanır).*

## Üst blok
Durma-koşullu (goal-loop) gece/uzun-koşum orkestratörü — Kun Chen'in üçlü L8 araç setinden biri (adın açılımı transkriptte "goodnight, have fun"). Salih'e bir hedef + durma koşulu + token/iterasyon tavanı verilir, ajan o koşul sağlanana dek döngüde koşar, sabah commit listesi/log ile teslim eder. Durum: GÜNCEL (mekanizma tanımı) · **kavramsal olarak GÜNCEL, araç fiilen KISMEN kurulu** — bkz. Gotchas. Son-teyit: 2026-08-31 (A3 kapı kanıtı, aşağıda). Kaynaklar: `cc/rapor/2026-08/rapor-2026-08-03-4.md` (L8 araştırması, satır 63-64, 134, 339, 353-355, 412) · `kuyruk/senaryo-defteri.md` Karar 84 / Karar 84 EK / Karar 84 EK-2 (satır 213-226) · `kuyruk/k010-zincir-2026-08-29.md` (A3 kanıt kaydı) · `core/ajan-metodolojisi.md` §6 (D2 a) · `KILAVUZ.md` "Jarvis-içi araç sınırı (E-1, Karar 76)". Kaba güven: ORTA — bir dış araştırma turu + 1 fiili koşum kanıtı (e600a7), ama Windows tarafında `[?]` işaretli doğrulanmamış kalemler var (kaynak raporunda).

## Çekirdek
gnhf = `wiki/loop-engineering.md`'nin hedef-tabanlı tipiyle birebir eşleşen bir dış koşucu: CC/Codex'teki yerleşik `/goal` ile aynı sınıfta iş yapar, ama fark **bütçe freni** — token tavanı, iterasyon tavanı ve `--stop-when` parametresi ayrı ayrı verilir (Kun Chen'in kendi gerekçesi: "`/goal` ile uyumadan önce hedef koyup uyanınca haftalık kotamın bittiğini görebilirim"). Agent-agnostic (claude/codex/copilot/pi/rovodev/opencode + genel `acp:`), `npm install -g gnhf`, temiz working-tree'li git reposu şart. Koşum kaydı `.gnhf/runs/<id>/gnhf.log` (JSONL) + paylaşılan `notes.md`; varsayılan olarak anonim telemetri gönderir (`GNHF_TELEMETRY=0` ile kapatılır — kurulumda zorunlu şart).

**Kanonik örnek (Karar 84 EK-2, e600a7 koşumu):** Salih-tetikli, ~55 dk, 3 iterasyonluk gece nöbeti (silver-health-watch dalı) — K-010'un A3 kapısındaki "Salih-tetikli uzun-loop" ayağının 1/3'ünü doldurdu; usage-log kanıtlı, rapor `raporlar/2026-08/2026-08-31-k010-a3-loop-1.md`.

## SOP (ne zaman/nasıl kullanılır)
**Karar 84 (2026-08-30, Salih beyanı aynen): "loop kurmamı istediğinde gnhf kullanmanı istiyorum — sen planlayıcısın, kendi kendine atılacak promptu yine sen hazırlaman saçma, planlayıcı olarak ajana devredersin (Kun Chen'in firstmate'i kullandığı gibi)."**
- Loop yüzeyi İKİ ŞERİT (Karar 84 EK): (1) **gece/uzun/sensiz koşum → gnhf** (`gnhf --agent claude` + İB-55 koşulları otomatik: worktree ∧ yazılı `--max-iterations`/`--max-tokens` ∧ `--stop-when` zorunlu ∧ push kapalı); (2) **izlenen/uyanıkken dönen nöbet → AYRI OTURUM** (Jarvis promptu derler, Salih yapıştırır — tetik Salih'te kalır). Orkestratör-aracılığıyla-gnhf üçüncü yolu RET edildi.
- CC-yerleşik `/loop` yalnız Salih açıkça isterse ya da iş oturum-içi gözetim gerektiriyorsa (gerekçe beyanla).
- Jarvis-içi araç sınırı (Karar 76, E-1): gnhf **KOŞULLU** — yalnız worktree ∧ yazılı token/iterasyon bütçesi ∧ push kapalı; hiçbir otomat kanon dosyalarına (core/, CLAUDE.md, tüzük, defter) doğrudan yazamaz.
- Ana-sıra icra formatı (`core/ajan-metodolojisi.md` §6, D2 a): gece/uzun/sensiz iş → gnhf worktree (Sonnet ajan); ikinci Fable yan-oturum yalnız Salih beyanıyla.

## Gotchas
- **Kurulum fiilen tamamlanmadı — kavram ≠ araç.** `cc/rapor/2026-08/rapor-2026-08-03-4.md` E02: "BİREBİR-VAR (kavram) + EKSİK-İNŞA (araç)" — gnhf'in K-009 devretme-merdiveni ile eşleşmesi doğrulandı, ama JARVIS reposuna kurulum henüz kanon-teyitli değil (ayrı deneme deposunda önce denenmesi öngörülmüştü).
- **Telemetri varsayılan AÇIK** — `GNHF_TELEMETRY=0` olmadan anonim veri gönderir; P1 done-yükleminin kapatma şartıydı.
- **gnhf ↔ firstmate arasında doküman-düzeyi karşılıklı referans YOK** (kod tabanında doğrulandı) — "tek entegre zincir" izlenimi transkriptin sunuş biçimi, kod tabanı bunu desteklemiyor.
- **Çifte-sayım çekincesi:** aynı koşumun A3'ün birden fazla ayağına sayılması Salih hükmü gerektirir (Karar 84 EK-2 örneği — hüküm verildi, otomatik varsayılmaz).
- **gnhf'teki "no-mistakes" adı bir git remote adı + CI check adıdır** (`git push no-mistakes`), Jarvis'teki [[no-mistakes]] skill'iyle karıştırılmamalı — ayrı bir isim çakışması, aynı araç değil.

## Süpersede zinciri
Yok (ilk yazım).

## [[link]]'ler
[[loop-engineering]] — hedef-tabanlı loop tipinin kural kaynağı · [[no-mistakes]] — L8 üçlüsünün diğer üyesi, isim çakışması notuyla · [[ajan-metodolojisi]] — icra formatı D2(a), gnhf'in yerleştiği katman · [[paralel-oturum-protokolu]] — worktree izolasyonu bağlamı.

## Kaynak/pointer
Karar 84 / 84-EK / 84-EK-2 (`kuyruk/senaryo-defteri.md` satır 213-226) · Karar 76 E-1 (`KILAVUZ.md`) · L8 araştırması `cc/rapor/2026-08/rapor-2026-08-03-4.md` · A3 kanıt kaydı `kuyruk/k010-zincir-2026-08-29.md` satır 55 + `raporlar/2026-08/2026-08-31-k010-a3-loop-1.md` · icra formatı `core/ajan-metodolojisi.md` §6.

**Bağlantılar:** · [[lavish]] (karşı-link 09-03)
