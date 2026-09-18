---
name: seans-bitimi
description: Çalışma seansını kapatır — seansın günlüğünü yazar, durum dosyasını tazeler, isteğe bağlı commit atar. Kullanıcı "seans bitimi", "kapatalım", "bugünlük bu kadar", "bitirdik", "günü kapat" dediğinde ya da oturumu bitirme sinyali verdiğinde çalışır. Sohbet uzayıp kullanıcı toparlanmaya başladığında bu skill'i öner. Seans açılışında ("seans başı" → seans-basi) ve ara özet istendiğinde KULLANILMAZ.
---

# Seans bitimi

Kapanış = **hafıza yazımı**. Bir sonraki seans yalnız burada yazılanı devralır; yazılmayan iş yapılmamış sayılır. Bayat/yanlış bir durum dosyası, boş olandan kötüdür.

## 1. Seansı gözden geçir

Konuşmayı baştan tara ve şunları çıkar:
- **Ne yapıldı** — hangi iş, hangi dosya (3-6 madde)
- **Ne değişti** — oluşturulan/düzenlenen dosyalar, verilen kararlar (kararın gerekçesini de yaz)
- **Açık kalan** — yarım işler, çözülmemiş sorular
- **Sonraki ilk iş** — bir sonraki seansın ilk hamlesi, 1-2 cümle

Vardiyayı devralan iş arkadaşına not yazar gibi yaz: hızlı yönlendirecek kadar, okumaktan yorulmayacak kadar. Olmayan "açık madde" uydurma; yoksa o başlığı hiç açma.

## 2. Günlüğü yaz

`gunluk/YYYY-AA-GG.md` (varsa üzerine ekle, yoksa oluştur):

```markdown
# Seans günlüğü — YYYY-AA-GG

## Ne yapıldı
- (iş — sonuç)

## Ne değişti
- (dosya ya da karar — gerekçe)

## Açık kalan
- (yarım / çözülmemiş)

## Sonraki ilk iş
(1-2 cümle)
```

## 3. `DURUM.md`'yi tazele

Üzerine yaz — arşiv değildir. Yalnız üç şey kalır: güncelleme tarihi · şu an · sonraki ilk iş (+ varsa açık işler). **Tek sayfayı geçirme**; tarihçe günlüklerde yaşar. Uzuyorsa eski satırları günlüğe taşı, durumdan çıkar.

## 4. Kaydet

Proje bir git deposuysa değişen dosyaları commit et; mesaj tek satır ve ne yapıldığını söylesin. Push'u kullanıcı istemeden atma. Git yoksa bu adımı atla — dosyaların yazılmış olması yeter.

## 5. Tek satırla teyit et

Nereye yazdığını ve "sonraki ilk iş" satırını söyle. Kullanıcı işi bitirmiş durumda; iki satırı geçme.

## Tuzaklar

- **Yazmadan "yazdım" deme:** dosyayı gerçekten oluştur/güncelle, sonra teyit et.
- **Durum dosyasını şişirme:** kapanış coşkusuyla oraya tarihçe anlatma — orası yalnız "şu an + sıradaki".
- **Sessiz hata:** commit ya da yazma başarısız olduysa gizleme, açıkça söyle.
- **Övgü kapanışı:** "harika bir gündü" gerekmez; kapanış düz veridir.

## Nasıl geliştirirsiniz

Sık yapılan eklemeler: kararları ayrı bir `kararlar.md` dosyasında biriktirmek · günlük şablonuna "ölçüm / süre" alanı koymak · kapanışta testleri ya da linter'ı bir kez koşturmak · haftalık özet çıkaran ikinci bir skill yazmak · günlük dosyasını ekip kanalına düşürmek.
