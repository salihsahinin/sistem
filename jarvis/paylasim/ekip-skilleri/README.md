# Ekip için iki skill: `seans-basi` · `seans-bitimi`

Claude Code ile çalışırken her oturum sıfırdan başlar: model bir önceki seansta ne yaptığınızı hatırlamaz. Bu iki skill o boşluğu **iki düz metin dosyasıyla** kapatır.

| Skill | Ne yapar |
|---|---|
| `seans-basi` | Durum dosyasını + son günlükleri okur, kısa brif verir, sıradaki işi önerir. |
| `seans-bitimi` | Seansın günlüğünü yazar, durum dosyasını tazeler, (git varsa) commit atar. |

Tuttukları tek sözleşme:

```
DURUM.md             → "şu an" + "sonraki ilk iş"   (tek sayfa, üzerine yazılır)
gunluk/YYYY-AA-GG.md → o seansın notu               (birikir)
```

Başka altyapı, veritabanı, script yok. Bilerek böyle: bu bir **iskelet**, kendi işinize göre büyütesiniz diye.

## Kurulum

Bu klasördeki `seans-basi` ve `seans-bitimi` dizinlerini skill klasörünüze kopyalayın:

```bash
mkdir -p .claude/skills && cp -r seans-basi seans-bitimi .claude/skills/
```

- **Proje içine** (`<proje>/.claude/skills/`) koyarsanız: yalnız o projede çalışır, depoya commit edilir, ekipteki herkese gider.
- **Kişisel** (`~/.claude/skills/`) koyarsanız: bütün projelerinizde çalışır, ekibe gitmez.

## Kullanım

Oturumun başında `seans başı`, sonunda `seans bitimi` yazmanız yeterli — skill kendi tetiklenir. `/seans-basi` diye açıkça da çağırabilirsiniz.

İlk koşumda `DURUM.md` ve `gunluk/` yoksa `seans-basi` bunları kendisi oluşturur; ilk gerçek içerik ilk `seans bitimi`nde yazılır.

## Neden işe yarıyor

- **Durum diskte, sohbette değil.** Model "hatırladığını" anlatmaz; dosyadan okur, çelişki görürse söyler.
- **Kapanış zorunlu adım.** Yazılmayan iş bir sonraki seans için yok hükmündedir.
- **Durum dosyası kısa tutulur.** Tarihçe günlüklerde yaşar; `DURUM.md` yalnız "şu an + sıradaki" kalır — böylece her açılışta okunması ucuzdur.

## Nasıl geliştirilir

`SKILL.md` dosyaları skill'in kendisidir; başka yerde saklı mantık yok. Değiştirmek = o dosyayı düzenlemek. Sık eklenenler:

- Açılışta ek kaynak okutmak (issue listesi, sprint panosu, `git log -10`, CI durumu)
- Brif ve günlük şablonlarına kendi alanlarınızı koymak (deploy, nöbet, müşteri)
- Kararları ayrı bir `kararlar.md`'de biriktirmek (gerekçe + geri alma koşuluyla)
- Kapanışta testleri/linter'ı bir kez koşturmak
- Kişi başına `DURUM-<isim>.md` ya da haftalık özet çıkaran üçüncü bir skill

Bir şeyi ilk koşumdan önce eklemek zorunda değilsiniz; iki hafta kullanıp neyin eksik kaldığını görün, ondan sonra ekleyin.

## Sınırlar

- Skill sohbeti özetler; ürettiği not **sizin yazdıklarınız kadar** doğrudur.
- Aynı anda iki oturum açıksa ikisi de `DURUM.md`'yi yazmak ister — o durumda kişi başına ayrı durum dosyası kullanın.
- Push'u kullanıcı istemeden atmaz; bu kasıtlıdır.
