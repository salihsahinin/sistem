---
name: project-graf-icinde-graf-karar-125
description: "Karar 125 (2026-10-26): akış grafı özyinelemeli; hedef = alt grafın kapağı, büyük resim yalnız üst hedefleri gösterir; kütükte hedef→hedef hizmet kenarı; HTML üretici tools/akis-graf-html.py"
metadata:
  node_type: memory
  type: project
  originSessionId: 4b1f454e-8921-45e4-bf12-ada7ec6e463d
  modified: 2026-10-26T20:06:04.457Z
---

Salih 2026-10-26: tek bağlam penceresine sığmayan projeler için graf içinde graf. Büyük resimde kaba hedef düğümleri kronolojik dizilir; iki büyük düğüm arası geçiş = bir alt grafın bitmesi (çok oturum sürebilir); alt grafın alt grafı olabilir, derinlik sınırsız. Hedef alt grafının en sağındadır, durumu alt grafından türer.

Kütük: `durum ac --tur hedef --hedef <üst>` zaten hedef→hedef hizmet kenarı üretir (Rust'ta değişiklik gerekmedi). Görsel: `jarvis/tools/akis-graf-html.py` + `akis-graf-html.sablon.html` → `raporlar/<ay>/<tarih>-akis-graf-interaktif.html`; kırıntı yolu (Büyük resim › H30 › …), katlı hedef rozeti, özyinelemeli ilerleme, bantlar (oturum · hedef · kategori satırları), tek sıra yay görünümü, geri/ileri bağ grupları, ASD-STE100 Türkçe panel + file:// ayrıntı bağlantıları.

**Why:** Salih yeni ürün/proje başlattığında Jarvis planı düz liste değil hedef hiyerarşisi olarak kütüğe açmalı; grafı sadece md olarak vermek yetmez, HTML üretilir.
**How to apply:** Proje-ölçekli işte önce üst hedef, sonra alt hedefler `--hedef` ile açılır; işler en alt hedefe bağlanır; seans kapanışında HTML yeniden üretilir. Arıza notu: `durum graf --json <yol>` 10-26'da düzeltildi (yol artık dikkate alınır). Eksik: `ac --kategori` alanı (kategori etiketten türetiliyor, kural tablosu script içinde). İlgili: [[feedback-oturum-hedefini-salih-koyar]], [[feedback-urun-ayri-repo]].
