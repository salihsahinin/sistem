# jarvis-oda

Oda modu: Jarvis (Fable, ana-sıra oturum) planı yazar, görevleri iş nodu olarak açar; her görev zorluğa göre Haiku / Sonnet / Opus işçisinde koşar. İşçi raporları, öneriler ve ortak sohbet aynı odaya düşer. Pano (Claude Code içi pane) görevleri, kalıcı dış oturumları, önerileri, sohbeti ve işçilerin canlı akışını gösterir; öneri kararı Salih'indir (Kabul/Ret).

## Mimari (v0.5+)

`hooks/register.tsx` yalnız kayıt yapar (olay → fonksiyon). Mantık `hooks/src/` altında, katman başına bir dosya:

| Dosya | Katman | Ne yapar | Ne yapmaz |
|---|---|---|---|
| `src/durum.ts` | veri | atomlar, odayı yükle/kaydet, tur ve hareket ekleme, atom okuyucuları | UI çizmez, süreç koşmaz |
| `src/metin.ts` | model metni | `oda_oku` özeti, sınıfa göre işçi emri, prompt bölümü, araç özeti | `$` almaz (saf) |
| `src/araclar.ts` | yazan taraf | araç tanımları ve işleyicileri, görev yaşam döngüsü, kütük köprüsü (`durum.exe`), kapsam ve bütçe kapısı, pano eylemleri | çizmez |
| `src/dis.ts` | dış kanal (C1) | dış oturumların dosya kanalı: `aktif.json`, `gelen-<oturum>.jsonl`, `giden.jsonl` | iç işçiye dokunmaz |
| `src/pano.tsx` | çizim | pane ağacı: görevler, oturumlar, öneriler, sohbet, canlı akış, olaylar | durumu yazmaz; her düğme `araclar.ts` eylemini çağırır |
| `src/ortak.ts` | yardımcı | saat, kısaltma, renk, pencere, yol (graf moduyla aynı kopya) | `$` almaz |

Motor kuralları bu ayrımı biçimlendirir (`claude plugin validate` denetler): `$` bir nesneye konmaz, dosyalar arası yalnız `function` bildirimine argüman olarak geçer; `read`/`update` atomun tanımlandığı modülde çağrılır; çizim sırasında yazım yapılmaz.

## İş nodu sınıfı (A5)

`oda_gorev_ver` zorunlu `sinif` ve `done` alır. Sınıf işçinin göreceği bağlamı sınırlar; amaç işçinin karışık bağlamda verim kaybetmemesidir.

| Sınıf | İşçi emri | Kapı | Varsayılan bütçe |
|---|---|---|---|
| `izole` | yalnız emir + rapor şeması | yok | 10 çağrı |
| `dosyali` | emir + yazma izni listesi (≤ 4 dosya) | liste dışı Edit/Write/NotebookEdit reddedilir | 15 |
| `planli` | emir + son 3 plan turu | yok | 20 |
| `rol` | `.claude/agents/<ad>.md` rolü, oda bağlamı yok | yok | 20 |

Bütçe dolunca işçiye uyarı düşer; 1.5 katında araçları kapanır ve görev `hata` sayılır. Panoda `[sınıf]` etiketi ve `çağrı n/bütçe` sayacı görünür.

## Pano (v0.5)

- **İşçiye tıkla:** görev başlığı, canlı akıştaki `#N` ve sohbetteki `işçi #N` düğmedir; basınca ana transkript o işçiye geçer (`$.ui.view`). İzlerken üstte "◀ ana sohbete dön" bandı çıkar.
- **Kaydırma:** sohbet, canlı akış ve olaylar pencerelidir (12 / 12 / 6); "◀ önceki · sonraki ▶ · en son". Yeni mesaj gelince pencere sondaysa sonda kalır.
- **Katlanır bölümler:** her bölüm başlığı ▾/▸ düğmesidir.
- **Etiket:** sohbet ve akış satırları `[#N · başlık · sınıf]` taşır; her görevin sabit rengi var. Uzun mesaj "▸ tam" ile Markdown olarak açılır.
- **İş nodu köprüsü (A4):** görev açılınca durum kütüğüne iş olarak yazılır (`durum.exe ac`, ayar `durumKaydi`, alan `alan`), bitince kapanır; satırdaki "iş #N ↗" akış grafında o düğümü seçer (`ortak/graf-secim.json`).
- **Dışa yazım (B8):** her kayıtta oda `ortak/oda/<odaId>.json` olarak yazılır; akış grafı HTML'i "Oda" sekmesinde okur.

## Dış oturumlar (C1, v0.6)

Kalıcı oturumlar (fork, öğrenme sekmeleri, alan ajanları) odaya dosyayla katılır; stigmerji ortak dosyadır.

- Dış oturum kendi sohbetinde `oda_katil(oturum, rol, dosyalar)` çağırır; aktif odayı `ortak/oda/aktif.json`'dan bulur. Sonra `oda_mesaj(tur: sohbet | rapor | oneri, metin)` ile yazar. Her dış oturum yalnız kendi `ortak/oda/<odaId>/gelen-<oturum>.jsonl` dosyasına yazar (tek yazar, eşzamanlı satır kaybı yok).
- Ev sahibi oda 3 sn'de bir yeni satırları okur: katılım "Oturumlar (kalıcı)" bölümüne ◆ işaretiyle düşer, sohbet ana oturuma eklenir, rapor ve öneri Jarvis'i `[oda dış]` ile uyandırır, öneri karar kapısına girer.
- Jarvis dış oturuma `oda_sohbet` hedef `@<oturum>` ile yazar: satır `giden.jsonl`'a iner, dış oturum 3 sn'de okuyup kendi sohbetine ekler; anında görmesi için Jarvis ayrıca `SendMessage` kullanır. Hedefsiz sohbet katılmış herkese (`*`) gider.
- `oda_katil ayril: true` oturumu "ayrıldı" yapar; kayıt silinmez.

## Araçlar, komut, ayarlar

Araçlar: `oda_ac`, `oda_plan`, `oda_gorev_ver`, `oda_ayar`, `oda_sohbet`, `oda_oku`, `oda_oneri_karar`, `oda_oneri` (işçi), `oda_rapor` (işçi), `oda_katil` ve `oda_mesaj` (dış oturum). Komut: `/oda`. Ayarlar: `otoUyandir`, `maksParalel`, `durumKaydi`, `alan`.

## Doğrulama

```bash
claude plugin validate jarvis/mods/jarvis-oda
```

```bash
claude plugin test jarvis/mods/jarvis-oda
```

Testler (`tests/`) bellek-içi motorda koşar: pano penceresi, katlama, tam metin, sınıf doğrulaması, yazma kapısı, bütçe, işçi görünümü, dış kanal gidiş-dönüşü.

## Sürümler

v0.2 paralel sınır + ortak sohbet · v0.3 işçi akışı ve izleme · v0.4 rol ajanı (`ajan`) · v0.4.1 yerel saat · v0.5 (2026-11-03) katmanlı kaynak, tanrısal bakış panosu, iş nodu sınıfı, kütük köprüsü · v0.6 (2026-11-03) dış oturum kanalı · v0.7 (2026-11-11, Karar 130 K52) kütük işi başlarken `al`, başarıda `bitir` (hata/bütçe aşımında açık kalır, neden odaya yazılır), `oda_oku gorevId=N` tam rapor, işçi önerisi Jarvis'i uyandırır (tool.call içinden prompt.submit yasak; kuyruk 3 sn'lik saatte boşalır).
