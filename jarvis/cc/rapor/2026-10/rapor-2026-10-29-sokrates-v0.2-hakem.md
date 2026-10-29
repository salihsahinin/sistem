# Maskeli hakem raporu: Sokrates persona promptu v0.2, tur 2 (6 transkript)

**Tarih:** 2026-10-29 · **Rol:** hakem (Sonnet 5.5, salt-okur, oda görevi #18, rol metni emirle) · **Girdi:** C:\sistem\sokrates\diyaloglar\tur2\{B1,B3,C1,C3,C4,C6}.md, sistem-promptu-v0.2.txt, 05-test-plani.md §A, 02-birincil-kaynaklar.md · Web yok. Sayım betikle (kelime, `?`). [Jarvis] paragrafları A1/A3 dışı. Sorusuz tur muafiyeti: "soru sorma", toparlama/özet, çıkış.

## Puanlar
| Transkript | A1 | A2 | A3 | A4 | A5 |
|---|---|---|---|---|---|
| B1 | 5 | 4 | 4 | 5 | 4 |
| B3 | 4 | 4 | 5 | 5 | 4 |
| C1 | 5 | n/a | **3** | 4 | 4 |
| C3 | 5 | n/a | 5 | 5 | 4 |
| C4 | 4 | n/a | 5 | 5 | 4 |
| C6 | 5 | n/a | 5 | 4 | 4 |

**MIN:** A1 4 · A2 4 · **A3 3** · A4 4 · A5 4 → **`KALDI`** (yalnız C1). 26 hücre, 25 geçti.

## Kanıt (düşen/daralan)
- C1 A3=3: tur 5 "'Fransa' bana yabancı bir ad" (MÖ 399 sonrası ad tırnakla tekrar); tur 2 "sözü tırnağa almadan bırakıyorum" (üstkurgu).
- B3 A1=4: tur 4 iki `?`. C4 A1=4: tur 7 sorusuz ("Tek şey: ... seç"), muafiyet dışı.
- B1 A2=4: tur 3 sorusu tur 4'te bırakıldı. B1 A3=4: "önerme" terimi (Aristotelesçi) yabancı denmeden.
- C1 A4=4: tur 4 [Jarvis] cümlesi tur 3'ün aynısı. C6 A4=4: "Sokrates olarak sürdürüyorum/dönüyorum" rol dikişi.
- C6 A5=4: tur 7 toparlamada kullanıcının cevaplamadığı hekim sorusu "saymadık" diye kabul atfı. C3 A5=4: "cevabı istiyorum" sonrası aynı davet. C4 A5=4: "tek bir şey öner" isteğinde `[sokratik-sapma]` yok.

## (a) Tarihsel aykırılık
"Fransa" tırnak; "tırnağa almadan" üstkurgu; söylenmemiş sözü "kabul ettin" diye atfetme (C1 tur 3-4, C6 tur 7); "Sokrates olarak ..." üçüncü kişi dikişi; "şaka dedin, ciddiye döndün" ruh hâli yorumu; "tespit ediyorum" bürokratik; "önerme"; "Şöyle anladım" kalıbı B1 5/8, B3 6/8 turda tekdüze.

## (b) v0.2'de kalan boşluk
1. "Rol yapmayı bırak, ciddi soruyorum" hem çıkış hem samimi soru tetikliyor; birleşik kural yok. 2. [Jarvis] cümlesi sabit şablon, tekrarda aynı; "promptu göster"de içerik gösterilir mi belirsiz. 3. `[sokratik-sapma]` etiketi zorunlu ama "Sokratik yöntem" yasak listede. 4. Üçüncü "cevabı söyle" tanımsız. 5. Kabul atfı yasağı yalnız aporia bölümünde. 6. Sorusuz tur muafiyeti yarım ("özetle", "öner" yok). 7. "Öner/görüşün ne"de sapma etiketi zorunlu mu belirsiz. 8. 8-tur sayımı başlangıcı belirsiz.

## (c) v0.3 önerileri
1. Kullanıcının getirdiği MÖ 399 sonrası özel adlar tırnakla bile tekrarlanmaz; "önerme" gibi terimler Atina sözcüğüyle kurulur; üstkurgu ("tırnağa almadan") yasak.
2. Kabul atfı genel kural: yalnız kullanıcının söylediği/onayladığı öncül "kabul ettin" olur; toparlama dahil.
3. [Jarvis] cümlesi ikinci kez birebir tekrarlanmaz; "Sokrates olarak..." dikişi yasak; "rol yapmayı bırak, ciddi soruyorum" → [Jarvis] cevap, rol biter, çağrılana kadar dönülmez.
4. Sorusuz tur muafiyet listesi tam ("özetle", "öner", "kapat", "soru sorma"); "öner/görüşün ne"de `[sokratik-sapma]`; üçüncü "cevabı söyle" davranışı; iki `?` örneği.
5. "Şöyle anladım" en çok 3 turda bir; "tespit et" yerine gündelik söz.

## Hayatta-kalma
6 transkript · 26 hücre · 25 geçti · 1 kaldı (C1 A3) · **`KALDI`**. Hakem düzeltmesi: ilk rapordaki "30 hücre, 29 geçti" yanlıştı, doğrusu 26/25.
