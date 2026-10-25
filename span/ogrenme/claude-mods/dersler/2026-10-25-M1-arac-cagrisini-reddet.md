# Araç çağrısını reddeden mod — ders 2 (2026-10-25; ogren v0.3) · Sektör: Hooks: PreToolUse / Decision Control · AS-OF 2026-10-25 (plugin-authoring skill, build 2.1.308)

## Ön-bağlam
M0 dersi (hook, `on`, `next`, `e`, `$`, mod klasörü). Yeni PROBE yapılmadı; iskelet Jarvis'ten gelmedi, README taslağı izlendi (`[sapma]` M0 ile aynı).

## Anlayış haritası
M0'dan devam: hook/zincir/mod klasörü seviyesi geçildi. Yeni iplikler: araç çağrısı olayı, `if` koşulu, metin arama; hepsi 0'dan başladı.

## Plan
DAG: `raporlar/gorsel-2026-10-19-claude-mods-m1-dag.html` (Artifact: https://claude.ai/artifact/MmxdSzp7pn4s1VC6ghTz5o). Kutular: 1 Hooks: PreToolUse · 2 Hooks: Decision Control · 3 JavaScript Control Flow · 4 Hook Input Schema · 5 JavaScript Strings · 6 Plugin Testing (pratik).

## Düğümler
| Kutu | Soru | Cevap | Sonuç |
|---|---|---|---|
| 1 araç çağrısı olayı | S12 | d | DOĞRU |
| 2 üç yanıt (deny, değiştir, gözle) | S13 | b | DOĞRU |
| 3 koşul `if`, `===` | S14 | d | 1. yaklaşım düştü ("Read araçtır, true" yanılgısı) |
| 3 (`===` yalnız karşılaştırır) | S15 | c | DOĞRU (2. yaklaşım) |
| 4 argüman okuma (`e.command`) | S16 | c | DOĞRU (nesne alanı); alan adı kaynakla doğrulandı (S17 öncesi) |
| 4 `deny` biçimi | S17 | a | DOĞRU (`deny: string`, Salih tip dosyasından okudu) |
| 5 `includes` | S18 | b (doğru a, `format` içinde `rm`) | 1. yaklaşım düştü |
| 5 (harf dizisi araması) | S19 | c | DOĞRU (2. yaklaşım) |
| 6 pratik (Salih'in eli) | S20 tahmin: e; canlı: `echo selam` çalıştı | | pratik `DONE` |

Pratik kaydı: Salih tip dosyasını kendisi açıp `ToolCallResult` içinde `deny: string` buldu; `BuiltinToolInputs` boş çıktı (yorum: mod yüklenince `claude-code-tools/index.d.ts` ile dolar), komut alanı `examples/tool-call.ts` içinden (`e.command`) bulundu. Mod: `on("tool.call", { tool: "Bash" }, ...)`, `e.command.includes("yasak")` ise `{ deny: "yasak kelimesi engelli" }`, değilse `next(e)`. Canlı deneme (`claude --plugin-dir`): ilk iki istekte Claude komutu kendi değiştirdi (`echo "merhaba"`), hook'a yasak kelime ulaşmadı; `echo selam` çalıştı (doğru). Toast eklenip komut tam sabitlenince Salih beyanı: hook komutu gördü ve ret geldi (ilk seçenek).

Açık düğüm: yok. Zayıf: Kutu 3 (`===` içerik karşılaştırması), Kutu 5 (`includes` alt-dize, yanlış alarm).

## ⌥ Jarvis notları
- Model komutu kendi değiştirebilir; hook yalnız gerçek çağrıyı görür. Mod testinde girdi tam sabitlenmeli ve gözlem model anlatısından bağımsız olmalı (`$.ui.toast` ile hook'un gördüğü komutu göstermek).
- Gözlenebilirlik kalıbı fikir adayı: hook kararlarını (gördüğü komut, deny) `$.ui.toast`/`$.ui.status` ile kullanıcıya göstermek; üretimde yalnız deny'da, gürültü olmasın.
- `deny` metni modele araç sonucu olarak gider; ön ek örneği `${$.plugin.name}: ...`.
- `includes('rm')` yanlış alarm üretir (`format`, `warm`); sınır için ayrı kural gerekir (M1 sonrası, regex dersi).
- `BuiltinToolInputs` boş; araç argüman adlarının kaynağı mod yüklenince oluşan `claude-code-tools/index.d.ts` ve skill'in `examples/` klasörü. Okuma kilidi Temp altını kapatıyor; Salih kendi eliyle okudu (okuma-izin-ek kararı gerekmedi).
- Build AS-OF: 2.1.308 (2026-10-25); README damgası 2.1.301'di.

## Salih notu
- "Bu komutları ben neden giriyorum, şu an neyi inceliyorum" → amaç açıklandı; sonra "dosyayı ben açayım, nasıl yapacağımı tarif et" → Salih tip dosyasını kendisi okudu.
- Canlı denemede model neden `merhaba` yazdı sorusu açık; kanıtlı neden yok (yalnız: tam sabitlenmiş komutla ret geldi).

## Kalan
M1 tamam (kavramsal `DONE`, pratik `DONE` Salih beyanıyla 2026-10-25). Sonraki ders: M2 (status line, toast, prompt üstü band). Pratik adayı: `author` uyarısı; `claude plugin test` için `*.test.ts` yazımı (örnek `pane.test.tsx` incelenmedi).
