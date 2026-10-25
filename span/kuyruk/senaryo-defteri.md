# Senaryo Defteri — Span (bağlam; hüküm kaydı)

*Span karar vermez. Bu defter: (a) gelen hükümler (Salih ya da Jarvis kanalıyla, aynen) · (b) `[oneri]` kayıtları (seçenekler; hüküm bekler) · (c) `[sapma]` kayıtları (emirden/iskeletten sapma + neden). Her kayıt zarf taşır: `[tip: … | kaynak: … | tarih: … | hedef: … | sema: v2 | koken: <yazar>/<model>/<asof>]` (Karar 104 M2). Bütçe ≤24 KB; aşımda damıtma → `arsiv/` (silme yok, m.8).*

## Gelen hükümler
- **Karar 105 (masa-18, 2026-09-20/21) (2026-09-21, masa-18, Salih):** `[tip: karar | kaynak: jarvis-masa-18 | tarih: 2026-09-21 | hedef: defter | sema: v2 | koken: salih/masa-18/2026-09-21]` Alan ajanı doğdu: dizin `span/` (= ad), alan bağlam, ad **Span**, model Sonnet 5, effort medium; eskalasyon (Opus/Fable) yalnız Salih beyanıyla (oturum başında 'bugün Opus'); öğrenme + ürün + sohbet bu dizinde; öğretim tasarımı Jarvis'te (Karar 103 EK 1); hakem ayrı (`.claude/agents/hakem`). Doğum belgesi charter §0b.

## Öneriler `[oneri]`
- `[tip: oneri | kaynak: claude-mods M1 | tarih: 2026-10-25 | hedef: jarvis | sema: v2 | koken: span/sonnet-5.5/2026-10-25]` Hook gözlenebilirlik kalıbı: hook kararını (gördüğü komut, deny) `$.ui.toast`/`$.ui.status` ile kullanıcıya göstermek; model komutu kendi değiştirebildiği için model anlatısı kanıt sayılmaz. Üretimde yalnız deny'da göster. Hüküm bekler.
- `[tip: oneri | kaynak: claude-mods M1 | tarih: 2026-10-25 | hedef: salih | sema: v2 | koken: span/sonnet-5.5/2026-10-25]` Salt-okur tip klasörü için `okuma-izin-ek` kalıcı çözüm değil (klasör adı her skill yüklemesinde değişir). Seçenekler: A) Salih eliyle okur (şimdiki, tarif edilebilir), B) izin eki. Hüküm bekler.

## Sapmalar `[sapma]`
- `[tip: sapma | kaynak: claude-mods M0/M1 | tarih: 2026-10-25 | hedef: defter | sema: v2 | koken: span/sonnet-5.5/2026-10-25]` Jarvis ders iskeleti yok; README taslağı izlendi, PROBE seviye 0 çıktı. Jarvis'e `cc/giden/2026-10-19-iskelet-gerekli-claude-mods-M1.md` ile bildirildi.
- `[tip: sapma | kaynak: claude-mods M1 Kutu 4 | tarih: 2026-10-25 | hedef: defter | sema: v2 | koken: span/sonnet-5.5/2026-10-25]` Ders metnindeki `e.input.command` yanlıştı; `examples/tool-call.ts` (build 2.1.308) `e.command` gösterdi. Görsel ve ders kaydı düzeltildi.
