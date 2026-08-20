---
name: seans-basi
description: Yeni bir çalışma seansını devralır — durum dosyasını ve son seans günlüklerini okur, kısa brif verir, sıradaki işi önerir. Kullanıcı "seans başı", "seansı devral", "başlayalım", "kaldığımız yer neresi", "bugün ne yapıyoruz" dediğinde ya da yeni oturumu selamla açtığında çalışır; selamla birlikte soru gelse bile önce bu ritüel koşulur. Oturum ortasındaki selamlaşmada ve seans kapanışında ("seans bitimi" → seans-bitimi) KULLANILMAZ.
---

# Seans başı

Selamlaşma sohbet değil **devir**dir: yeni seans, bir öncekinin bıraktığı yerden başlar. Bu skill durumu diskten okur — hafızadan, tahminden ya da sohbet geçmişinden anlatmaz.

## Kullandığı iki dosya

| Dosya | İşi |
|---|---|
| `DURUM.md` (proje kökü) | "Şu an" + "sonraki ilk iş". Tek sayfa, her kapanışta ÜZERİNE yazılır. |
| `gunluk/YYYY-AA-GG.md` | O seansın notu. Birikir, silinmez. |

Yoksa → adım 4.

## 1. Oku (ilk cevaptan ÖNCE)

1. `DURUM.md`
2. `gunluk/` içindeki son 2 dosya (yeniden eskiye)
3. Varsa `CLAUDE.md` / `README.md` — projenin kendi kuralları

Bu üçü dışında bir kaynaktan durum anlatma. Dosyalar birbiriyle çelişirse (ör. günlükte biten iş `DURUM.md`'de hâlâ açık) çelişkiyi brifte söyle, kendi kafana göre birini seçme.

## 2. Brif ver (kısa)

- Tek satır durum özeti
- Son seansta ne yapıldı (2-4 madde)
- Açık kalan / yarım işler
- Karar bekleyen şeyler (varsa)

Düz veri yaz: övgü, dolgu, "harika gidiyoruz" yok. Uzun rapor değil, oryantasyon.

## 3. Öner ve tek soru sor

Önce **net bir öneri**: "Sıradaki iş şu, çünkü …" — bir cümle, kaçamak yok. Sonra tek soru: *"Buradan mı devam edelim, başka bir şey mi?"*
Cevabı işi değiştirmeyecek soruyu sorma.

## 4. Dosya yoksa (ilk koşum)

`gunluk/` klasörünü aç ve `DURUM.md`'yi şu iskeletle oluştur, sonra kullanıcıya tek cümleyle haber ver:

```markdown
# Durum

**Güncelleme:** YYYY-AA-GG

## Şu an
- (üzerinde çalışılan iş)

## Açık işler
- (yarım kalanlar, bekleyen kararlar)

## Sonraki ilk iş
1. (bir sonraki seansın ilk hamlesi)
```

## Tuzaklar

- **Önsöz tuzağı:** Kullanıcı selamla birlikte soru sorarsa içeriğe atlama — önce ritüel, sonra soru.
- **Bayat durum:** `DURUM.md` tarihi eskiyse körü körüne güvenme; günlüklerle (ve depo git ise `git log -10` ile) çapraz kontrol et, tutarsızlığı brifte söyle.
- **Zaman:** "Günaydın" bir zaman bilgisi değildir; tarih/saat sistemden okunur.

## Nasıl geliştirirsiniz

Bu dosya skill'in kendisidir; değiştirmek için başka yere bakmanıza gerek yok. Sık yapılan eklemeler: okuma listesine issue/sprint panosu ya da `git log` eklemek · brife kendi alanınızı (deploy durumu, CI, nöbet) koymak · kişi başına ayrı `DURUM-<isim>.md` tutmak · brif sonunda otomatik bir kontrol komutu çalıştırmak.
