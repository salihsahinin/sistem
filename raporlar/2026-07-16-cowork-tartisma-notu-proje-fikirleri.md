# Cowork Tartışma Notu — Proje Fikirleri Oturumu (2026-07-16)

*Salih emri (07-16): "bu konuşmaları Cowork'te tartışabilmem için not al, bir değişiklik yapma." → Bu dosya o nottur. KANONA DOKUNULMADI (aşağıda "Ne yapıldı / yapılmadı").*

## Oturumun özeti
Salih: internetten Atlas'la, **kronolojik zorluk partisyonlarına** ayrılmış "proje fikri" araştırması + her sınıflandırmaya "örneğin" açıklaması istedi. İki okuma yaşandı:

1. **İLK OKUMA (Carvis yanlış anladı): "JARVIS'i geliştirme"** — JARVIS sistemini V29 Iron Man ufkuna götüren proje fikirleri.
   → Rapor: `raporlar/2026-07-16-jarvis-gelistirme-proje-fikirleri-zorluk-partisyonlari.md` (**G0-G6**, Z0-Z4). 4 paralel Atlas (Beyin/Hafıza · Motor/Orkestrasyon · Ses-Proaktiflik · Öz-gelişim/Meta).
2. **SALİH DÜZELTMESİ: "JARVIS'le yapılacak projeler"** — JARVIS'i *araç* olarak kullanıp yapılacak çıktı-eserleri (PortRisk sınıfı, CV/proof-of-work).
   → Rapor: `raporlar/2026-07-16-jarvisle-yapilacak-proje-fikirleri-zorluk-partisyonlari.md` (**S0-S4**). 4 paralel Atlas (Quant/Finans · Veri/ML · Yazılım-Web-LLM-ürün · Kişisel/disiplinlerarası/fırsat). **ASIL HEDEF budur.**
   → Salih çerçevesi: "aklıma gelen HER projeyi yapabilmeliyim; başta temel yönelimler olur" (spektrum geniş, çıpa = quant/finans/veri).

İki rapor da AYRI eserdir; ikisi de HAM FİKİR (m.20), seçim turu bekler. İlk rapor emekli değil — JARVIS'i inşa yol haritası olarak ileride işe yarar.

## Cowork'te tartışılacak açık sorular (gündem)
1. **Çerçeve teyidi:** "her proje yapılabilmeli + başta temel yönelim" okuması doğru mu? S0-S4 raporu bu varsayımla kuruldu.
2. **Tek-flagship gerilimi (m.13):** Bu havuz PortRisk canlı-demoya dek yalnız FİKİR mi kalmalı, yoksa bir-iki S0/S1 "ısınma" projesi (örn. kişisel Fama-French faktör-analizi) PortRisk'e PARALEL açılmalı mı? (m.36 önceliği PortRisk hattında.)
3. **Çekirdek-örgü seçimi:** Raporun önerdiği hat — `faktör-analizi → GARCH-VaR → portföy-opt → sağlam-backtest → PortRisk v2 (flagship)` + paralel BIST/TEFAS + Türkçe-LLM-eval — Salih'in yönüne uyuyor mu? Hangi 2-3 eser "derinlemesine anlatılabilir" seçilecek (kalite>nicelik)?
4. **Katman-1 kapıları (m.31):** para akışı (Stripe/SaaS), lisanslı gerçek-zamanlı BIST verisi (VERDA), kişisel-veri dashboard'ları → publish öncesi Salih onayı; bu fikirler havuzda ama build'e ancak o kapıdan girer.
5. **Süre kalibrasyonu:** S-tier süre tahminleri Atlas kalibrasyonu ([?]); Salih'in gerçek hızıyla ayarlanmalı (senaryo-defteri deseni).
6. **İlk rapor (G0-G6) ne olsun:** JARVIS-inşa yol haritası olarak saklanıp K-009/K-010/P5 gündemine mi bağlansın, yoksa şimdilik uykuda mı kalsın?

## Ne yapıldı / ne yapılmadı (şeffaflık)
- **YAPILDI (yalnız NOT/kayıt):** 2 araştırma raporu + bu tartışma notu `raporlar/`a yazıldı; `fikir-kutusu.md`'ye 3 pointer eklendi (m.20 — kutunun kendi kuralı: kaynağa işaret, kopya değil). Commit + push (proof-of-work = kayıt kalıcı olsun, Cowork okuyabilsin).
- **YAPILMADI (Salih "değişiklik yapma" + "Cowork'te tartışacağım" emri gereği):** pano.md'ye kart açılmadı · durum-kapsulu.md / pano / tüzük / CLAUDE.md DEĞİŞTİRİLMEDİ · seçim turu koşulmadı · hiçbir build başlatılmadı · hiçbir fikir karara/kanona yükseltilmedi.
- **Konum:** her şey `claude/jarvis-project-ideas-lf6f80` branch'inde. Cowork'te bu branch'i açarak tartışabilirsin.

## Sonraki adım (Salih'te)
Cowork'te bu notu + iki raporu aç → yukarıdaki 6 gündem maddesini tart → karar verdiklerin seçim turuyla/karar formatıyla (kaynak+gerekçe+geri-açma) kanona girer, pano kartı o zaman açılır.


---

## KARAR KAYDI (2026-07-17, Cowork ana-sıra oturumu — Salih, Katman 1)

Gündemin 6 maddesi karara bağlandı (tam gerekçeler oturum kaydında; senaryo-defterine ayrıca blok düşüldü):

1. **Çerçeve:** yakın vade çapası kariyer/CV, nihai hedef "her proje yapılabilir" kapasitesi — S0-S4 kurgusu teyit.
2. **Tek-flagship (m.13): Model C** — havuz şimdilik fikir kalır, BUGÜN proje açılmaz (07-15 odak kararı korunur); "artık önemli" tetiği çekildiğinde açılacak ilk iş ŞİMDİDEN sabitlendi: **S0 kişisel-portföy faktör-analizi, PortRisk Sprint 1 ön-dilimi olarak** (K-002 kartına işlendi).
3. **Çekirdek-örgü ONAY** (PortRisk yapılış hattı olarak): faktör-analizi → GARCH-VaR → portföy-opt → sağlam-backtest → PortRisk v2 flagship. "2-3 derinlemesine eser" adayları (kilitli değil, S0-S1 koşarken revize): PortRisk v2 · sağlam-backtest çerçevesi · Türkçe-LLM-finans-eval.
4. **Katman-1 kapıları ONAY** — para akışı / lisanslı veri / kişisel-veri fikirlerine kutuda "Katman-1 kapılı" damgası.
5. **Süre kalibrasyonu ONAY (şerhli):** S-tier tahminleri deneysel damgalı; katsayı ilk 2-3 gerçek koşumdan türetilir (K-020 sahası). Salih şerhi: "yöntem yeterince içime yatmadı, sonra döneceğiz" — yöntem revizyonu açık madde.
6. **G0-G6 raporu:** uykuya YATMAZ — K-009/K-010 açılış gündemine pointer'la bağlandı (pano K-009 satırı).

Branch main'e merge edildi; HAM FİKİR statüsü değişmedi — build'e giriş hâlâ seçim turundan.
