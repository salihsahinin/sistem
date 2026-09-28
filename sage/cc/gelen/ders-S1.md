# Ders iskeleti S1 — Meditations: metin nedir, nasıl okunur; Kitap 1 (Jarvis → Sage, 2026-09-28; Karar 105 M4 devir birimi)

`[tip: ders-iskelet | kaynak: jarvis-terminal 09-28 | tarih: 2026-09-28 | hedef: sage/ogrenme/stoa | sema: ogren v0.3 | koken: jarvis/claude-fable-5-1/2026-09-28]`

Şerit `ogrenme/stoa` · hafta **S1**. Salih kitabın ortasındaysa (`[?]`): `PROBE` aynen koşar, `PLAN` kutuları Salih'in bulunduğu kitaba göre 4-6 arasından seçilir; Kitap 1 kutusu atlanmaz (metnin anahtarı orada). Sektör başlıkları AS-OF 2026-09-28, ders başında teyit.

## PROBE — iplikler (≤5) ve sorular (≤10; doğru şık konumu rastgele; (e) bilmiyorum sabit)
İplik 1 **metnin doğası** · 2 **Stoacı üç disiplin** · 3 **kontrol ikiliği** · 4 **terim/anakronizm** · 5 **okuma pratiği**.

1. (İplik 1) *Meditations* kim için yazıldı? (a) Roma Senatosu · (b) oğlu Commodus · (c) yazarın kendisi, yayımlanmak üzere değil · (d) öğrencileri · (e) bilmiyorum. **Doğru: c.**
2. (İplik 1, üst) Kitap 1 diğer 11 kitaptan nasıl ayrılır? (a) daha uzun · (b) kişilere teşekkür/borç listesi, özdeyiş değil · (c) Latince · (d) şiir · (e) bilmiyorum. **Doğru: b.**
3. (İplik 2) Hadot'nun üç disiplini hangisidir? (a) mantık-fizik-etik · (b) algı(onay)-eylem-arzu · (c) beden-ruh-akıl · (d) geçmiş-şimdi-gelecek · (e) bilmiyorum. **Doğru: b** (mantık-fizik-etik Stoa'nın üç *bölümü*dür, disiplin değil).
4. (İplik 3) "Bize bağlı olan" (*eph' hēmin*) hangi listeye girer? (a) sağlık · (b) ün · (c) yargılarımız ve niyetlerimiz · (d) başkalarının davranışı · (e) bilmiyorum. **Doğru: c.**
5. (İplik 4) Gündelik "stoik" (duygusuz) ile Stoacı *apatheia* arasındaki fark? (a) fark yok · (b) *apatheia* yıkıcı tutkulardan (*pathē*) özgürlük; iyi duygular (*eupatheiai*) korunur · (c) *apatheia* mutluluğu reddeder · (d) yalnız çeviri farkı · (e) bilmiyorum. **Doğru: b.**
6. (İplik 5) Bir pasaja atıf yaparken ortak anahtar nedir? (a) sayfa numarası · (b) kitap.paragraf (ör. Med. 4.3) · (c) bölüm başlığı · (d) çevirmen adı · (e) bilmiyorum. **Doğru: b.**
7. (İplik 2, üst) Med. 2.1 sabah pasajı hangi disiplinin egzersizidir? (a) arzu · (b) eylem (başkalarına karşı tutum) + algı (önceden hazırlanma) · (c) yalnız fizik · (d) mantık · (e) bilmiyorum. **Doğru: b.**

Ön-bağlam Salih verirse iplik atlanır. Çıktı `## Anlayış haritası`.

## PLAN — DAG (görsel isteğe bağlı; düğüm numaralı)
```
1 Metin: hypomnemata (kendine notlar), 12 kitap, sıralı değil       
2 Kitap 1: borç listesi — 1.7 Rusticus, 1.17 tanrılara                ← 1
3 Üç disiplin (Hadot): onay · eylem · arzu                            ← 1
4 Kontrol ikiliği (Epiktetos Ench. 1 ↔ Med. 7.2)                      ← 3
5 Terimler: hēgemonikon · prosochē · apatheia (anakronizm freni)      ← 3
6 Okuma pratiği: atıf anahtarı, çeviri farkı, yorum ≠ metin etiketi   ← 1
```
Kenarlar: 1→2 · 1→3 · 3→4 · 3→5 · 1→6. Derinlik: 3,4 [T] · 2,5,6 [O] · 1 [S]. Olgusal düğüm 1-2 (tarih, düzenleme tarihçesi): `halusinasyon-engelleyici` derece; kaynak Waterfield/Hard giriş yazıları `[K]` ders içinde canlı.

## Kutu başlıkları
- Kutu 1 — Metin nedir · Sektör: *Hypomnemata / Spiritual Exercises* (Hadot 1998)
- Kutu 2 — Kitap 1 borç listesi · Sektör: *Gratitude catalogue · Med. 1.7, 1.17* — pratik: Salih'in kendi 5 satırı
- Kutu 3 — Üç disiplin · Sektör: *Three Stoic Disciplines (assent · action · desire)* — **Karar 73 karşılığı:** tanım + Yunanca + Med. 2.1'in üç disipline ayrıştırılması (elle tablo)
- Kutu 4 — Kontrol ikiliği · Sektör: *Dichotomy of Control* — Ench. 1 ↔ Med. 7.2 yan yana
- Kutu 5 — Terimler ve anakronizm · Sektör: *Stoic Terminology · "stoic" ≠ Stoic*
- Kutu 6 — Okuma pratiği · Sektör: *Citation and Translation Practice* — sözlüğe ilk 5 terim

**"⌥ Jarvis notu" adayları:** Kutu 4 → tüzük m.4 soru eşiği / kontrol dışı işlere enerji harcamama; Kutu 6 → V26 alıntı-eşleşme kuralıyla aynı (kaynak.bölüm zorunlu).

## Pratik (Salih'in eli)
README S1 `DONE`: kendi "borç listesi"nden 5 satır (kimden ne öğrendin), Med. 1 biçiminde; `urun/borc-listesi.md`.

## CLOSE
Ders kaydı `ogrenme/stoa/dersler/2026-MM-DD-S1-metin-ve-kitap-1.md` · `ilerleme.md` · `sozluk.md` ilk 5 terim · Jarvis'e dönüş `cc/giden/S1-geri-donus.md` (çeviri adı + kaldığı kitap + iskelet isteği S2).
