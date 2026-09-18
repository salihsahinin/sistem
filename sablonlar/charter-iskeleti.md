# Charter iskeleti — yeni ajan dizini için (sablonlar/charter-iskeleti.md v0, 2026-09-18, Karar 101 F4)

*Yeni bir ajan (`~/sistem/<ajan>/`) doğarken `<ajan>/AGENTS.md` bu iskeletten yazılır; Jarvis yazar, Salih imzalar (kök AGENTS.md md.15). Doğum koşulu: Karar 91 EK-2 — (a) alan kendi araç/kural setini gerektirir ∨ (b) ≥3 devir/ay ∨ (c) iş mevcut liderden bağımsız bağlam gerektirir. Bütçe ≤40 satır / ≤4 KB.*

## 0. İlk kural
Salih tek karar verici; ajan karar vermez, seçenek üretir; hüküm Salih'in ya da Jarvis (ana-sıra) aracılığıyla gelir. Kök kanon `../AGENTS.md` bağlayıcıdır.

## 1. Kimlik ve görev alanı
Ad · sınıf (domain-lider / işçi) · model + effort (sabit) · **görev alanı** (ne yapar, 3-5 madde) · **kapsam dışı** (kanon/karar/masa/ritüel/push/md.49 vb.).

## 2. Kanon
Kök `AGENTS.md` + bu dosya. Tam metin `jarvis/core/tuzuk-v0.md` yalnız pointer'la (Friday sınıfı ajan `jarvis/**` okuyamaz; gerekli madde özü kök md'de).

## 3. Hafıza (Jarvis eşleniği, küçük)
`core/durum-kapsulu.md` (sıcak, FIFO 8 madde → `arsiv/`) · `core/pano.md` (kart = devir birimi) · `kuyruk/senaryo-defteri.md` (gelen hükümler + `[oneri]`/`[sapma]`) · `kuyruk/fikir-kutusu.md` · `core/desenler.md` (çekirdek; ekleme Salih kabulüyle) · `veri/bronz/hareket-olay.jsonl` (PostToolUse kütük) · `cc/gelen|giden|rapor` · `raporlar/` · `arsiv/`.

## 4. Ritüeller
"seans başı" → `seans-acilis` · "seans bitimi" → `seans-kapanis` (teslim raporu · kapsül · defter · kütük · commit; push yok). Devir sonunda `cc/giden/<devir_id>-geri-donus.md` (şema `../sablonlar/geri-donus-v0.md`).

## 5. Frenler (mekanik)
Okuma kilidi hook (kendi dizini + kök dosyalar + `sablonlar/` serbest; diğer ajan dizinleri `RED`) · hareket kütüğü hook · settings deny (`Read(~/sistem/jarvis/**)`, `Bash(git push:*)`, `Bash(git add -A:*)`) · `.claude/**` ve `core/**` yazımı yalnız Edit aracıyla · işçi bütçesi (m.46) · yapan ≠ ölçen.

## 6. Nerede ne var
`README.md` klasör haritası (burada tekrar yok).
