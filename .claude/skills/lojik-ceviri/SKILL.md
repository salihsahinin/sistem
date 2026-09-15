---
name: lojik-ceviri
description: Doğal-dil talimatı/kuralı m.38 bağlaç setiyle (∧ ∨ ¬ → ↔) lojik forma çevirir (S-D); numaralı dallar, boolean done-yüklemi, niceleyici-sırası denetimi üretir. Tetik; "lojiğe çevir", "kurala dök", "formüle et", loop/otomasyon kuralı tanımlanırken, görev-fonksiyonunun dallar bölümü doldurulurken. kullanılmaz; serbest sohbet/anlatı metninde, kod (B4 basamağı) yazımında, karar üretiminde.
---

# Lojik çeviri (S-D, v1 — 2026-08-14; B1→B2 basamak geçişinin koşum skill'i)

Kural kaynağı: tüzük m.38 (bağlaç seti + ek fıkralar) + `core/ajan-metodolojisi.md` §1/§3. Amaç: Türkçe niyeti kayıpsız, denetlenebilir B2 formuna indirmek — merdivenin **orta** basamağı meşrudur, her şey koda inmez.

## Adımlar
1. **Atomikleştir:** metindeki önermeleri tek tek ayıkla (her önerme tek iddia; "ve/veya" saklı bileşikleri boz).
2. **Bağla:** ∧ ∨ ¬ → ↔ ile kur; → (ise) ile ↔ (ancak-ve-ancak) karışmasına özel dikkat. Niceleyicileri **açık** yaz ("her X" ∀ mü, "bir X" ∃ mi) ve **sırasını** koru — ∀∃ ≠ ∃∀ (niceleyici-sırası disiplini).
3. **Dallara dök:** `D1: eğer <koşul> → <eylem> · D2: aksi → <eylem>` numaralı; **dal+koşul ≤5**, aşarsa kuralı böl. Katman-1 gerektiren dal ayrı: `D-KATMAN1 → DUR + Salih'e sor`.
4. **Done-yüklemini boolean'laştır:** derece ifadesini ("iyi", "yeterince") ölçülebilir koşula çevir; **ears** kalıbı yardımcıdır: `when <koşul>, <koşum> shall <sayılabilir çıktı>`.
5. **Geri-çeviri kontrolü (zorunlu):** lojik formu düz Türkçeye **geri** oku ve orijinalle yan yana sun — anlam kayması varsa formu düzelt, orijinali değil. Nihai onay biçimin sahibinde (Salih/emri veren).

## Gotchas
- **↔ enflasyonu:** çoğu kural tek yönlüdür (→); ↔ yazmadan önce "tersi de zorunlu mu" diye sor.
- **"Her zaman/asla" tuzağı:** niceleyicisiz mutlak ifade kapsam belirsizliği doğurur — kapsamı yaz ("bu oturumda ∀ commit" gibi).
- **Format-tax uyarısı:** lojik form **talimat** içindir; modelin **çıktısını** sert şemaya zorlamak ayrı bir karardır ve doğruluk düşürebilir (kanıt kanonda) — karıştırma.
- Çeviri kanon yazmaz; kural-adayı kanonlaşması G2 (Salih imzası) ister. Skill kaydetme/commit yapmaz; commit seans akışının işidir (yan-etki freni).
