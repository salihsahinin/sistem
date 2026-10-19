# Mod = hook zinciri — ders 1 (2026-10-19; ogren v0.3) · Sektör: Claude Code Plugins / Hooks (middleware chain) · AS-OF 2026-10-19 (plugin-authoring skill, build 2.1.299)

## Ön-bağlam
Yok. Salih: "hook ne demek bilmiyorum", "kodu tam bilmiyorum, nasıl okunur bilmiyorum" (PROBE).

## Anlayış haritası
| İplik | Seviye | Kanıt |
|---|---|---|
| Hook ve zincir (`next`) | 0 | S1: "bilmiyorum" (soru sorulmadan beyan) |
| JS/TS fonksiyon okuma | 0 (S2 doğru ama "tahmin") | S2 |

## Plan
DAG: `raporlar/gorsel-2026-10-19-claude-mods-m0-dag.html` (Artifact: https://claude.ai/artifact/JdNAQShqSnqWDw51yNyuMZ). Kutular: 1 Hooks · 2 JavaScript Functions · 3 First-Class Functions and Callbacks · 4 Hook Registration and Matchers · 5 Middleware Chain · 6 Plugin API Surface · 7 Plugin Structure and Manifest · 8 Plugin Validation (pratik).

## Düğümler
| Kutu | Soru | Cevap | Sonuç |
|---|---|---|---|
| 1 hook nedir | S3 | c | DOĞRU |
| 2 fonksiyon okumak | S4 | a | DOĞRU |
| 3 callback | S5 | c | DOĞRU |
| 4 `on(olay, eşleştirici, hook)` | S6 | b | DOĞRU |
| 5 zincir ve `next`; formül `C = m ∘ g₂ ∘ g₁` (5→6→12→112; sıra değişince 111) | S7 | d | DOĞRU |
| 6 `e` ve `$` | S8 | e (bilmiyorum) | 1. yaklaşım düştü |
| 6 (nesne ve `...` kopya) | S9 | b | DOĞRU (2. yaklaşım) |
| 7 mod klasörü | S10 | e (bilmiyorum) | 1. yaklaşım düştü |
| 7 (kim kimi gösteriyor) | S10' | b (yanlış; doğru a) | 2. yaklaşım düştü |
| 7 (dosyayı oku) | S11 | c | DOĞRU (3. yaklaşım, zayıf) |

| 8 pratik (Salih'in eli) | `claude plugin validate ~\mod-deneme\benim-modum` | Salih beyanı: "uyarıyla beraber geçti" | pratik `DONE` |

Pratik çıktısı: `Validation passed with warnings`. Uyarı: `author` alanı yok (isteğe bağlı). `hooks: nothing` ve `calls: nothing on $` boş `register` yüzünden beklenen sonuç: mod hiçbir olayı dinlemiyor.

Açık düğüm: yok. Zayıf: Kutu 7 (`hooks.json` ile `plugin.json` ayrımı), Kutu 6 (spread sözdizimi).
Hata kaydı: S10 (ilk hali) motorun eksik dosyadaki davranışı doğrulanmadan soruldu; geri çekildi.

## ⌥ Jarvis notları
- Kutu 1: `okuma-izin.sh` bu oturumda canlı hook örneği oldu (araç çağrısı olayı, `Bash` eşleştirici, yol izin listesi); kabuk betiği hook'u ile mod hook'u aynı fikir, kurulum yolu farklı.
- Kutu 5: README'deki `f₁∘f₂∘…∘motor` yazımı ile ders yazımı `m ∘ g₂ ∘ g₁` farklı bakış (olayın aşağı akışı); README düzeltilecek.
- Kutu 6: modda dosya işi `$.fs` ile; betik hook'larının yetkisinden ayrı denetim [doğrulanmadı].
- Okuma kilidi `okuma-izin.sh` skill'in tip dosyasına (`AppData\...\plugin-authoring\types`) erişimi engelledi; `{ deny }` alanının tam tipi doğrulanamadı. Çözüm adayı: `okuma-izin-ek` ile salt-okur kök (Salih kararı).

## Salih notu
- "Mesela bu tarz tanımlamaları görsel olarak örnek bir fonksiyon üzerinde oklarla gösterebilirsin" (Kutu 2) → hafızaya yazıldı, Kutu 2-7 görselleri buna göre.
- "Türkçe başlayalım" ; sonrasında İngilizce konuşma pratiği planı (10-12 hafıza kuralı).

## Kalan
Kutu yok; M0 tamam (kavramsal `DONE`, pratik `DONE` Salih beyanıyla 2026-10-19). Sonraki ders: M1 (`tool.call` ile Bash çağrısını reddeden mod). Pratik adayı: `author` uyarısını `plugin.json`'a alan ekleyerek gidermek.
