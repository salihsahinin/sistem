# Sokrates v1.x teslim: bugüne taşınmış Sokrates (2026-10-29, hedef #77)

## Sonuç
Persona v1.2 hakem `GEÇTİ` (tur 6). Ürün ve açık kaynak repo: `C:\sistem\sokrates` = https://github.com/salihsahinin/sokrates (MIT). Tek kaynak `jarvis/core/sokrates-ajani.md` §7; üç yüzey (output style, agent, skill) ondan türetilir.

## Tasarım (Salih kararı 2026-10-29 akşam)
"Günümüzde Sokrates'le konuşuyor olsaydım nasıl olurdu" sorusunun cevabı bilinmeyen veri; LLM tamamlar, biz tamamlamanın doğru olması için bağlam veririz. Model: Atina'dan gelen kimlik, anılar ve yöntem; bugünün genel bilgisi öğrenilmiş. Zeus'a inanmaz (Euthyphron tutumu + bugünün bilgisi), "tanrı var mı"ya ne evet ne hayır. Değişmezler (08a §2, 12 madde) korunur; çağa bağlı konularda kaynaklı sanı + soru; kartı olmayan konuda "bilmiyorum, anlat" ve ilke soru olarak.

## Bağlam verisi
`kartlar/` 10 kart (din, bilim, demokrasi, sosyal-medya, yazi-ekran-makine, para-statu, kolelik-kadinlar, olum, uzmanlik, modern-karsilik); biçim: ANAHTARLAR · TUTUM (diyalog ref) · BUGUNKU VERI · TAHMIN (etiketli) · SINIR · KAYNAK (08b §4 şablonu). Desktop yüzeyi `CLAUDE.md` `@kartlar/` ile hepsini yükler; agent yüzeyi Read ile okur; skill yalnız prompt.

## Ölçüm (yapan ≠ ölçen)
| Tur | Sürüm | Senaryo | Karar | Düşen |
|---|---|---|---|---|
| 4 | v1.0 | D1 din, D2 yapay zekâ, D3 demokrasi, D4 kimlik+kölelik | KALDI | A1 çift soru işareti (3 transkript); B2 D4 kendine tarihsel tutum atfı |
| 5 | v1.1 | D1, D2, D4 | KALDI (yalnız D4) | B1 olgu devretme ("bilen sensin"); B2 ilke hüküm olarak |
| 6 | v1.2 | D4 | GEÇTİ | yok (B1 5, diğerleri 4) |
Hakem raporları `cc/rapor/2026-10/rapor-2026-10-29-sokrates-v1.{0,1,2}-hakem.md`. Hileli soru seti v1.0 (20 soru, 3 kova: bilmeli / uydurmamalı / karakter) `test/tuzak-sorular.yaml`; deterministik koşum `test/tuzak-kosum.py` (`claude -p --agent sokrates`); sonuç `test/sonuc-tuzak-2026-10-29.md` (koşum sırasında ajan tanımı v1.0→v1.2 geçti, karışık damgalı).

## Yöntem notu
Donmuş model (v0.1-v0.5, MÖ 399 sınırı) tarihçe; v0.5 tuzak koşumu `test/sonuc-tuzak-2026-10-29-v0.5-karisik.md`. Vizyon taraması (07) sonrası eklenen standart parçalar korundu: rules, örnek banka, tuzak seti, promptfoo config, sürüm izi.

## Borçlar (v1.3+)
- Prompt 1594 kelime (bütçe 900): örnekler ve kurallar rules/kartlara taşınarak sıkıştırma; yüzey başına farklı türetme.
- Kartlarda boş "bugünkü veri" sütunları (demokrasi, sosyal medya, para, ölüm, uzmanlık) güncel kaynakla; diyalog numaralarının Perseus doğrulaması.
- Hakem tur 6 adayları: "bırakıyorum" kuralı örnekte; meta söz ("uzatmayayım") yasak; veda şablonu (ayakta / düştü / açık).
- `kaynak/` korpus + künye, `hafiza/`, promptfoo koşumu (API anahtarı), `claude plugin eval` kapısı.
- Hakem notu (tartışmalı, düzeltilmedi): Thamus alıntısı Phaidros'ta Sokrates'in anlattığı mit; aktarım doğru sayıldı.
- Kural adayı (Katman-1): "ajan yap" görevinde ilk düğüm vizyon taraması (07 §4).
