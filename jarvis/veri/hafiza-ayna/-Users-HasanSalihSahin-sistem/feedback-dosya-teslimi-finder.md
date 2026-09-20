---
name: feedback-dosya-teslimi-finder
description: "Salih'e dosya teslim ederken göreli yol (\"raporlar/…\") yetmez — tam yol + Finder'da göster (open -R) + tarayıcıda aç; Finder aramasına klasör yolu yazmak dosyayı bulmuyor"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9fdc5615-445a-4695-a8d3-ad19f32f7c84
  modified: 2026-08-16T07:22:15.510Z
---

Salih (2026-08-16, seans-7): "dosyanın nerde olduğunu söylüyosun, Finder'a 'raporlar/' yazıyorum dosya gözükmüyor — bu sorunu bir daha yaşamak istemiyorum." Aynı gün başka oturumda "Finder'dan jarvis dosyasına erişemiyorum, dosya engelini kaldır" da denmişti. Teşhis: klasör gizli değil, Spotlight indeksliyor, izinler normal — sorun Finder aramasının yol parçasını ("raporlar/") eşlememesi.

**Why:** Salih çıktıları Finder/tarayıcıdan görür ve paylaşır (arkadaşına e-posta, sunum); göreli repo yolu onun için adres değildir. Ayrıca sunumu Lavish inceleme-yüzeyinde açmak da kafa karıştırdı ("neden böyle yaptığını anlamadım") — çerçeveli araçlar değil, düz dosya bekliyor.

**How to apply:** Bir dosya teslim ederken **her zaman**: (1) tam mutlak yol yaz (`/Users/HasanSalihSahin/jarvis/raporlar/<dosya>`), (2) `open -R <tam-yol>` ile Finder'da seçili göster (klasör için `open <klasör>`), (3) HTML/görsel ise `open <dosya>` ile tarayıcıda aç. Finder'da bulma tarifi: Cmd+Shift+G → `~/jarvis/raporlar` yapıştır. Lavish/Artifact gibi sarmalayıcı yüzeyleri Salih istemedikçe **kullanma** — sunum/tablo/rapor = düz dosya. İlgili: [[user-mac-primary]].

**Ek (2026-08-16, Salih 'son-50 yazınca çıkan ilk sonuç…' — 2 görev):** aranınca **ilk** çıkan dosya (1) doğrudan açılıp anlaşılan **türde** olmalı (HTML/PDF — tarayıcıda açılır; .md/.csv/.jsonl değil), (2) kendini açıklamalı (ilk ekran: bu ne işe yarar). Uygulama: teslim dosyasının **adı** arama anahtarıyla **başlar** ve türü büyük harfle söyler (ör. `son-50-prompt-SUNUM.html`; tarih dosyanın içinde), makine-yüzü .md/.csv tarihli-teknik adla kalır; Finder yorumu (Spotlight'ta aranır) eklenir; teslimde dosya bir kez açılır (kullanım = Spotlight sıralamasını yükseltir).

**İLK VE ilk kural (Salih 08-16 ~11:25, Katman-1 — kanon giriş dosyasına işlendi):** "ben patronum; teslimler benim anlamam için." Her çıktının birinci ölçütü patronun anlaması ve karar verebilmesi; güzel/modern değil 'anlaşıldı mı' ölçülür. Araştırma emri: `cc/gorev-2026-08-16-4.md` (patron-için-anlaşılırlık yöntemleri + metrikleri).
