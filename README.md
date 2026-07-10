# JARVIS Node — Portföy Komuta Merkezi

**Ne bu:** Salih'in JARVIS sisteminin sistem-reposu ve 6 aylık proof-of-work portföy planının komuta merkezi. Kuruluş: 2026-07-10 ("BUILD VAR" kararı, Salih). Bu repo LOKAL ve ÖZELDİR — CV artefaktı değildir; CV artefaktları ayrı public repolarda yaşar (bkz. `00_MASTER_PLAN.md`).

**Statü / onay kapısı:** Bu repo 07-10 oturumunda kuruldu. Salih'in ayık taraması = onay kapısı; veto = `git revert` ya da klasör silme (Homebase kanonuna henüz hiçbir kayıt işlenmedi — kayıt, tarama onayından sonraki ilk commit).

## Okuma sırası
1. `00_MASTER_PLAN.md` — 6 aylık proof-of-work portföy planı (hedef: bomba gibi CV).
2. `01_NODE_ARCHITECTURE.md` — node topolojisi + repo yapısı + yazma yüzeyleri + hijyen.
3. `02_KNOWLEDGE_INDEX_PLAN.md` — yerel bilgi index'i: araştırma sentezi + karar + fazlı rollout.
4. `03_DUVAR_RAPORU.md` — refutation ethos: planın gerçek sınırları (davranış, pazar, teknik, zaman).
5. `core/` — temel katman v0: durum kapsülü, pano, tüzük, şablonlar.
6. `raporlar/` — ajan görev raporları (ham kanıt; karar içermez).

## Klasör haritası
```
core/            temel katman (kapsül, pano, tüzük v0, şablonlar) — KANON: yalnız Salih kararıyla değişir
kuyruk/          iş kartları (Faz D'de aktifleşir — şimdilik placeholder)
raporlar/        ajan/araştırma raporları — serbest yazım yüzeyi
wiki/            kavram wiki'leri hedef alanı (Homebase'deki mevcut wiki'lere işaretçi)
```

**Kural mirası:** Bu node, Homebase'deki Carvis sözlüğü v1 (DONDU) terimleriyle konuşur; tüzük `core/tuzuk-v0.md`'de.
