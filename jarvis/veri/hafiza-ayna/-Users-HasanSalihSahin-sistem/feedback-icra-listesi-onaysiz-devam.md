---
name: feedback-icra-listesi-onaysiz-devam
description: "Salih 08-30 — icra oturumunda planlanmış yapılacaklar listesi bitene kadar durma, devam onayı bekleme; kademeli paralel pipeline denemesi istenir"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7223e5b2-58f1-4b61-ad7b-e196424b26b2
  modified: 2026-08-30T07:17:52.811Z
---

Salih (2026-08-30, icra oturumu, aynen): "planlamış olduğun yapılacaklar listesi bitene kadar durma devam onayımı bekleme" ve aynı emirde: borçları pipeline olarak icra ederken sıralı/paralel kararını İB-63 şemasıyla (manifest + PK kuralları, `tools/paralel-kapi.py`) kontrol et; paralel sayısını kademeli artır (doğal sınır bilinmiyor).

**Why:** Salih otonom icra oturumunda ara onay sorularını iş kaybı sayıyor; karar gerektirmeyen (A kovası) borçlar için brif sonrası tek "başla" yeter. Paralellik deneyi = K-010 A1/A3 kanıt hattı.

**How to apply:** "seans başı, icra oturumu" açılışında A kovasını listele → Salih "önerinden git" derse listeyi sonuna kadar koş (ara onay yok; yalnız Katman-1/çelişki kapısı durdurur). Birimleri `veri/manifest/*.json` ile beyan et, kapıyı koş, N'i 1→2→3 artır, sonuçları `raporlar/…-paralel-kademe-pilot.md` biçiminde kaydet. Paralel oturum varsa kanonu `git@sha:` snapshot'tan oku, `git add <yol>` ile commit. İlgili: [[feedback-parallel-sessions-keep-talking]], [[feedback-token-kisinti-yuzde30]].
