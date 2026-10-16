---
name: lojik-ceviri
description: Doğal-dil talimatı/kuralı Lean 4 koduna çevirir (S-D v2, Karar 114); atomik önermeler → `structure` alanları, dallar → `inductive` + karar fonksiyonu, done-yüklemi → `Bool` fonksiyonu, temel özellikler → `theorem`; `lake env lean` ile derlenmeden teslim edilmez. Tetik; "lojiğe çevir", "kurala dök", "formüle et", "lean'e çevir", loop/otomasyon kuralı tanımlanırken, görev emrinin done/dallar bölümü doldurulurken, `core/` kural dosyası koda taşınırken. kullanılmaz; serbest sohbet/anlatı metninde, raporun anlatı kısmında, icra kodunda (o Rust), karar üretiminde.
---

# Lojik çeviri (S-D, v2 — 2026-10-16, Karar 114: günlük dil → Lean 4 → Rust; v1 m.38 bağlaç formu arşivde git geçmişinde)

Kural kaynağı: tüzük m.38 (bağlaç seti hâlâ düşünme aracıdır) + `core/ajan-metodolojisi.md` §1/§3 + örnek modül `lean/Kanon/SkillKapi.lean`. Amaç: Türkçe niyeti kayıpsız, **derleyicinin denetlediği** forma indirmek. Lean = kural ve sözleşme (spec); icra Rust'ta, ikisi fark testiyle bağlanır; bağlama yalnız arayüz satırı + pointer girer.

## Adımlar
1. **Atomikleştir:** önermeleri tek tek ayıkla (her önerme tek iddia; saklı "ve/veya" bileşiklerini boz). Her atom bir `structure Girdi` alanı olur: `Bool` (evet/hayır ölçüm) ya da `Nat` (sayı, eşik); yanına `--` ile Türkçe tanım + ölçüm kaynağı.
2. **Bağla:** her ara formül bir `def ... : Bool`; docstring'e m.38 formu yazılır (`/-- K0 := ¬A ∧ (B ∨ C) -/`). `→` ile `↔` ayrımı burada da geçerli; niceleyiciler açık (`∀ x ∈ L, …` → `L.all`, `∃` → `L.any`), sırası korunur.
3. **Dallara dök:** sonuçlar `inductive Dal` (ya da `Hukum`); karar fonksiyonu `def karar : Girdi → Dal` if/else zinciriyle, **first hit-policy**. Dal sayısı ≤5, aşarsa modülü böl. Katman-1 gerektiren dal ayrı yapıcı: `| katman1Dur` (anlamı: DUR + Salih'e sor).
4. **Done-yüklemi:** `def done : Cikti → Bool`; derece ifadeleri ("iyi", "yeterince") ölçülebilir alana çevrilir (sayı + eşik). ears kalıbı yardımcıdır.
5. **Özellik kanıtı:** metinde kesin söylenen her cümle için bir `theorem` (ör. "tam kapsama → RET-0"). Kanıt `simp [...]` ya da `decide` ile kapanmıyorsa ya kural belirsizdir ya da çeviri yanlış: çeviriyi düzelt.
6. **Derle (zorunlu):** `cd lean && lake env lean <dosya>.lean` hatasız. Derlenmeyen çeviri teslim edilmez.
7. **Geri-çeviri kontrolü (zorunlu):** modül başındaki `/- … -/` bloğuna düz Türkçe özet yaz ve orijinal metinle yan yana sun; anlam kayması varsa kodu düzelt, orijinali değil. Nihai onay biçimin sahibinde (Salih/emri veren).

## Yer ve ad
- Kanon kuralı → `lean/Kanon/<ModulAdi>.lean` + `lean/Kanon.lean`'e `import` satırı; md dosyasında tek satır pointer kalır ("kanonik: lean/Kanon/X.lean; ayrışmada kod kazanır").
- Görev emri sözleşmesi → `lean/Gorev/<tarih>-<kisa-ad>.lean` (`gorev-emri-derleme` çağırır).
- Modül adı ASCII PascalCase; alan adları ASCII camelCase (Türkçe kök, aksansız), açıklama yorumda Türkçe.

## Gotchas
- **Lean bağlamı kendiliğinden küçültmez:** model Lean'i de metin olarak okur. Kazanç, kural Rust'ta uygulanıp bağlama yalnız arayüz satırı girdiğinde gelir; modülün tamamını bağlama yükleme.
- **Anlatı Lean'e girmez:** gerekçe, tarihçe, kaynak, rakam md/raporda kalır; Lean'e yalnız kural, dal, done ve eşik girer.
- **↔ enflasyonu:** çoğu kural tek yönlüdür; `↔` teoremi yazmadan önce tersinin de zorunlu olduğunu doğrula.
- **Niceleyicisiz mutlak ifade** ("her zaman/asla") kapsam belirsizliği doğurur; kapsamı alan olarak yaz.
- **Format-tax:** Lean talimat ve sözleşme içindir; modelin serbest çıktısını Lean'e zorlamak ayrı karardır.
- Çeviri kanon yazmaz; kural-adayının kanonlaşması G2 (Salih imzası) ister. Skill commit yapmaz (yan-etki freni).
