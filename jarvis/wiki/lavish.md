# lavish

*AS-OF 2026-09-03 (yazım: İB-04 wiki kuyruğu; kural kaynağı `wiki/README.md` 6-blok standardı — çelişkide kanon kazanır).*

## Üst blok
Yerel-öncelikli etkileşimli HTML artefakt editörü (`lavish-axi` CLI, Kun Chen) — Jarvis'in L8 araç üçlüsünden biri; plan/karşılaştırma/diyagram/tablo/kod-diff gibi metin-duvarı riskli çıktıları, Salih'in üzerinde işaretleyip yorum bırakabildiği ve geri bildirimi doğrudan ajana geri gönderen bir tarayıcı yüzeyine çevirir. Durum: **güncel** — bu oturumda sistem-promptu üzerinden `~/.agents/skills/lavish/SKILL.md` tam metniyle doğrulandı. Son-teyit: 2026-09-03. Kaynaklar: `~/.agents/skills/lavish/SKILL.md` (bu koşumda okundu) · `cc/rapor/2026-08/rapor-2026-08-03-4.md` (L8 araştırması, satır 57, 90, 113, 148-149, 210, 263, 342, E05) · `wiki/README.md` satır 44 (kuyruk aday kaydı). Kaba güven: **orta-yüksek** — birincil kaynak (SKILL.md tam metin) taze, ama Jarvis içinde fiili kullanım kanıtı/koşum sayacı henüz yok (araç adaydan öte kanonlaşmadı).

## Çekirdek
lavish, ajan üretilen bir HTML artefaktı `npx -y lavish-axi <html-file>` ile açar; sayfa iframe + enjekte SDK ile elemanların üstüne not almaya izin verir, `layout gate` (render doğrulama, incelemeyi bloklamaz) + Layout-issues gelen-kutusu + live-reload taşır. Salih işaretleyip prompt kuyruğa attıktan sonra ajan `npx -y lavish-axi poll <html-file>` ile o geri bildirimi bekler (long-poll, ön planda tutulur — arka-plan yalnız harness'in kendi tamamlanma-bilinçli iş takibiyle). Mermaid diyagramları otomatik olarak düzenlenebilir Excalidraw whiteboard'a döner. `end`, `export` (taşınabilir tek-dosya), `share` (üçüncü-parti ht-ml.app'te herkese-açık/parola-korumalı yayın) alt komutları var.

**Kanonik örnek — `cc/rapor/2026-08/rapor-2026-08-03-4.md` satır 57 (Kun Chen'in kendi cümlesi, Türkçe özet + orijinal alıntı):** ajan bir planı HTML sayfası olarak, o projenin kendi tasarım dilinde açıyor; Salih üstünde işaretleyip yorum bırakıyor, alttaki seçeneklere tıklayarak karar veriyor, geri bildirim terminale dönmeden doğrudan ajana gidiyor. Kun Chen'in kendi cümlesi: *"I can never go back to reading text in the terminal anymore"* (28:06).

## Sop (ne zaman/nasıl kullanılır)
Bu oturumun sistem-promptu, lavish için ayrı bir çağrı akışı tanımlıyor (özet, tam ayrıntı `~/.agents/skills/lavish/SKILL.md`'de):
1. HTML artefaktı oluştur (varsayılan konum `.lavish/<ad>.html`).
2. `npx -y lavish-axi <html-file>` ile inceleme oturumunu aç/devam ettir.
3. `npx -y lavish-axi poll <html-file>` ile Salih'in işaretleme/prompt'unu bekle (ilk poll'da `--agent-reply` ile bağlam ver).
4. Gelen prompt'u uygula, tekrar poll'la döngüyü sürdür.
5. İnceleme bittiğinde `npx -y lavish-axi end <html-file>`.
Tasarım önceliği: (1) Salih özel bir görünüm istediyse onu kullan → (2) yoksa artefaktın konusu olan projenin kendi tasarım sistemini incele ve eşle → (3) ikisi de boşsa Tailwind v4 + DaisyUI v5 **cdn** varsayılanı (`npx -y lavish-axi design`).
**Jarvis'teki durum notu:** bu görev, `Skill` aracıyla çağrılan `wiki-sayfa-yaz`in yanı sıra, sistem-promptunda ayrı bir `lavish` skill'i (aynı `lavish-axi` CLI'sini tarif eden) mevcuttu — iki kaynak (SKILL.md dosyası + sistem-prompt tanımı) **içerik olarak örtüşüyor**, çelişki yok.

## Gotchas
- **"Add to queue" ≠ gönderim (09-03 vakası):** kuyruğa alınan not tarayıcıda kalır, ajana yalnız "Send to Agent" / "Send & End" ile düşer; poll o ana dek sessizdir. Salih "kararım chat'te yazmıyor" dediğinde arıza değil, henüz gönderilmemiştir.
- **Share komutu üçüncü-parti servise (ht-ml.app) veri gönderir** — herkese-açık varsayılan; parola korumalı yayın için `--password` şart. Jarvis'in "sır yalnız `.secrets/`" ilkesiyle (CLAUDE.md §2) birlikte okunmalı — paylaşımdan önce içerik gözden geçirilmeli.
- **Poll asla arka-plana `nohup`/`&`/`disown` ile atılmaz** — SKILL.md sert kural: yalnız harness'in tamamlanma-bilinçli arka-plan mekanizması kabul edilir, yoksa ön planda tutulur.
- **Kullanıcı tarayıcıdan oturumu bitirirse** (`Send & End`), ajan `--reopen` olmadan yeniden açamaz — davetsiz yeniden-açma yasak.
- **Layout-issues gelen kutusundaki bulgular Salih kuyruğa almadan düzeltilmez** — pasif bulgu, aktif talimat değildir; sıraya alınmamış öğeye dokunma.
- **Jarvis'te henüz kanon-koşum kanıtı yok** — `cc/rapor/2026-08/rapor-2026-08-03-4.md` E05 kaydı: "Bizim tüm karar sunumumuz metin duvarı; en yüksek Salih-yükü getirisi olan kalem" (yani değer tespiti **yüksek** ama araç fiilen entegre edilmedi); CC'nin yerleşik `Artifact` aracı da aynı kategoride bir alternatif olarak raporda not edilmiş (V25: desen alınır, kurulum kopyalanmaz ilkesi).

## Süpersede zinciri
Yok (ilk yazım).

## [[link]]'ler
[[gnhf]] — L8 üçlüsünün diğer üyesi, durma-koşullu koşum tarafı · [[paralel-oturum-protokolu]] — çoklu-oturum/paylaşılan-kaynak disiplini, share-yasağı bağlamı için ilgili · [[gorsel-artefakt-dogrulama]] — SVG/HTML artefaktın okunabilirliğinin bbox-ölçümüyle sınanması ilkesi, lavish'in layout-gate mekanizmasıyla aynı sorunu (sessiz görsel hata) farklı katmanda ele alır.

## Kaynak/pointer
`~/.agents/skills/lavish/SKILL.md` (bu koşumda tam okundu) · L8 araştırması `cc/rapor/2026-08/rapor-2026-08-03-4.md` (satır 57, 90, 113, 148-149, 210, 263, 342, E05) · kuyruk aday kaydı `wiki/README.md` satır 44 (kaynak `cc/rapor/2026-08/rapor-2026-08-03-4.md` + teslim 08-04).
