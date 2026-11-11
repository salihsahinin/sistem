# jarvis-oda

Oda modu: Jarvis (Fable, ana-sıra oturum) planı yazar, görevleri iş nodu olarak açar; her görev zorluğa göre Haiku / Sonnet / Opus işçisinde koşar. İşçi raporları, öneriler ve ortak sohbet aynı odaya düşer. Pano (Claude Code içi pane) görevleri, kalıcı dış oturumları, önerileri, sohbeti ve işçilerin canlı akışını gösterir; öneri kararı Salih'indir (Kabul/Ret).

## Mimari (v0.5+)

`hooks/register.tsx` yalnız kayıt yapar (olay → fonksiyon). Mantık `hooks/src/` altında, katman başına bir dosya:

| Dosya | Katman | Ne yapar | Ne yapmaz |
|---|---|---|---|
| `src/durum.ts` | veri | atomlar, odayı yükle/kaydet, tur ve hareket ekleme, atom okuyucuları | UI çizmez, süreç koşmaz |
| `src/metin.ts` | model metni | `oda_oku` özeti, sınıfa göre işçi emri, prompt bölümü, araç özeti | `$` almaz (saf) |
| `src/araclar.ts` | yazan taraf | araç tanımları ve işleyicileri, görev yaşam döngüsü, kütük köprüsü (`durum.exe`), kapsam ve bütçe kapısı, pano eylemleri | çizmez |
| `src/altoda.ts` | alt-oda (B9) | `oda_altoda_ac` şeması ve doğrulaması, aşama ilerletme (tur → son konum → hakem), kütük hedef + iş | ajan metnini değiştirmez |
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

## Alt-oda (B9, v0.8)

**Ne:** alt-oda üst odanın bir görev düğümüdür. İçinde 2-5 rol ajanı (`.claude/agents/<ad>.md`) turlu münazara eder ve ortak bir çıktı üretir; çıktıyı hakem ajanı done cümlesine göre tartar. Gerekçe (Karar 130 B9): sorun kötü çıktıdan çok özgünlük kaybı; Jarvis'in emri ajanın görüşünü biçimlendirmesin.

**Araç:** `oda_altoda_ac(baslik ≤120, soru ≤600, kapsam ≤400, done ≤200 tek cümle, ajanlar 2-5, tur 1-4 = 2, hakem = hakem)`. Akış:

1. Tur 1: her ajan yalnız soru + kapsam + done görür (bağımsız ilk görüş).
2. Tur 2..T: her ajan diğerlerinin önceki tur metinlerini ad etiketli görür ve yanıtlar.
3. Son konum: her ajan konuşmanın tamamını görür, tek paragraf son konum yazar.
4. Hakem: ortak çıktı (konuşmanın tamamı + son konumlar) ve done cümlesi hakeme gider; rapor `hakemRaporu` alanında ayrı durur.
5. Bitince Jarvis `[oda] alt-oda #K` ile uyanır (görev raporuyla aynı yol: `prompt.submit`). Tam döküm `oda_oku altOdaId=K`.

Kayıt üst odanın JSON'unda `altOdalar` altındadır (`ortak/oda/<odaId>.json`). Her ajan çağrısı sıradan bir `rol` görevi olarak oda kuyruğuna girer: paralel sınır ve rol bütçesi (20 çağrı, 1.5 katında kapanış) aynen işler. Durum kütüğünde alt-oda açılınca `--tur hedef` ile hedef düğümü, ajan başına `--hedef N` katkı işi açılır (oturum `oda-<odaId>`); hakem bitince işler ve hedef `oda <odaId> alt-oda #K` kanıtıyla kapanır (Karar 125: hedef alt grafın kapağı).

**Özgünlük kuralı kodda nasıl zorlanır** (`hooks/src/altoda.ts`, `hooks/src/metin.ts`):

- Şema: `additionalProperties: false`; alan listesi sabit, yöntem/üslup/serbest emir alanı yok. İşleyici de şema dışı her alanı reddeder (motorun ayrılmış alanları hariç).
- Uzunluk: soru 600, kapsam 400, done 200 karakter; done satır sonu içeremez. Emir bu alanlara gömülemez.
- Emir: ajanın gördüğü metin `metin.ts`'teki sabit şablon + bu üç alan + diğer ajanların ham metinleridir; Jarvis'in başka metni girmez.
- Çıktı: ajan cevabı `String(answer)` olarak saklanır; kısaltma, trim, özet ya da yeniden yazım adımı yoktur. Ortak çıktı bu metinleri olduğu gibi birleştirir.
- Ölçüm: çıktıyı yalnız hakem tartar; hakem katılımcı olamaz (yapan ≠ ölçen).

v0'da bilerek dışarıda: düşen (killed) ajan için alt-oda ilerletmesi (yoklama görevi `hata` yapar, alt-oda bekler), aynı tur içinde sıralı konuşma (tur içi çağrılar paralel sınıra kadar eşzamanlıdır), panoda ayrı alt-oda bölümü, alan içinde gizli emir arayan içerik denetimi.

## Araçlar, komut, ayarlar

Araçlar: `oda_ac`, `oda_plan`, `oda_gorev_ver`, `oda_altoda_ac`, `oda_ayar`, `oda_sohbet`, `oda_oku`, `oda_oneri_karar`, `oda_oneri` (işçi), `oda_rapor` (işçi), `oda_katil` ve `oda_mesaj` (dış oturum). Komut: `/oda`. Ayarlar: `otoUyandir`, `maksParalel`, `durumKaydi`, `alan`.

## Doğrulama

```bash
claude plugin validate jarvis/mods/jarvis-oda
```

```bash
claude plugin test jarvis/mods/jarvis-oda
```

Testler (`tests/`) bellek-içi motorda koşar: pano penceresi, katlama, tam metin, sınıf doğrulaması, yazma kapısı, bütçe, işçi görünümü, dış kanal gidiş-dönüşü, alt-oda (tur 1 bağımsızlık, tur 2 girdisi, metnin bayt düzeyinde korunması, şema reddi, kütük hedef + iş, paralel sınır).

## Sürümler

v0.2 paralel sınır + ortak sohbet · v0.3 işçi akışı ve izleme · v0.4 rol ajanı (`ajan`) · v0.4.1 yerel saat · v0.5 (2026-11-03) katmanlı kaynak, tanrısal bakış panosu, iş nodu sınıfı, kütük köprüsü · v0.6 (2026-11-03) dış oturum kanalı · v0.7 (2026-11-11, Karar 130 K52) kütük işi başlarken `al`, başarıda `bitir` (hata/bütçe aşımında açık kalır, neden odaya yazılır), `oda_oku gorevId=N` tam rapor, işçi önerisi Jarvis'i uyandırır (tool.call içinden prompt.submit yasak; kuyruk 3 sn'lik saatte boşalır) · v0.8 (2026-11-11, Karar 130 B9) alt-oda: `oda_altoda_ac`, turlu münazara + son konum + hakem, kütükte hedef + alt graf, `oda_oku altOdaId=K`.
