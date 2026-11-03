# jarvis-graf

Akış grafı paneli: `ortak/akis-graf.json` (Karar 122 kütük görünümü, Karar 124/125) Claude Code içinde canlı bir pane olarak çizilir. Dosya değişince (10 sn) pane kendiliğinden yenilenir. Komut: `/graf` (argüman `is:<id>`, `#<id>` ya da `seans:<ad>` o düğümü seçer).

## Mimari (v0.2)

`hooks/register.tsx` yalnız kayıt yapar. Mantık `hooks/src/` altında:

| Dosya | Katman | Ne yapar |
|---|---|---|
| `src/durum.ts` | veri | atomlar; graf JSON, kütük (`ortak/durum-olay.jsonl`) ve karar defteri yükleme; yol bulma (cwd'den köke); oda köprüsü okuma |
| `src/metin.ts` | saf hesap | satır düzeni (hedef şeridi, seans satırları, sanal oturum satırları), düğüm detayı |
| `src/cizim.ts` | saf çizim | SVG: gün sütunlu ölçek, satır = seans, numaralı düğümler, kenarlar, açıklama şeridi |
| `src/araclar.ts` | yazan taraf | HTML üretici koşumu, dosya açma/kopyalama/Explorer, `durum graf`, seçim ve filtre eylemleri |
| `src/pano.tsx` | çizim | üst çubuk, SVG, tıklanabilir ızgara, detay kutusu |
| `src/ortak.ts` | yardımcı | oda moduyla aynı kopya |

## Görünüm

- **Graf (B1):** her satır bir seans (sohbet); en üstte hedef şeridi; kütükte seans kaydı olmayan işler (ör. oda görevleri `oda-<id>`) kendi oturum adlarıyla sanal satıra düşer. x ekseni gün sütunlarıdır: boş gün dar, kalabalık gün geniş; yoğun günde düğümler satır içinde alt sıraya sarar, SVG pane'e sığar. Düğümün içinde iş numarası, rengi durumu verir (açık kırmızı, işlemde sarı, tamam yeşil, bayat gri, hedef mor elmas). Kenarlar: hizmet mor ince, girdi kesik, bitirdi yeşil kalın.
- **Izgara (B2):** SVG'nin altında aynı satırlar düğme olarak durur: seans adı ve o seansın işleri. Basınca seçilir; SVG seçili düğümü halkayla gösterir. (Motor SVG içindeki tıklamayı iletmez; tıklama bu ızgaradadır.)
- **Detay (B3):** tam etiket, sonraki eylem, durum, yerel saatler, oturumlar (düğme), yönlü bağlar (bekler · önünü açar · hizmet eder · açan/bitiren seans; düğme), kütük olayları ve kanıtları, etikette "Karar NNN" varsa defter paragrafı, seans kaydı için aç · kopyala · Explorer.
- **HTML aç (B4):** `tools/akis-graf-html.py` `py -3` → `python` → `python3` sırasıyla denenir (`python3` bu makinede bash shim'idir, kabuksuz süreçte açılmaz), çıktı `Start-Process` ile tarayıcıda açılır. Açılamazsa pane'de dosya satırı (aç · kopyala · Explorer) ve hata metni kalır. Masaüstü yüzeyi `file://` bağlantısı çizmez; bu yüzden bağlantı yerine düğme kullanılır.
- **Oda köprüsü (B5):** oda panosundaki "iş #N ↗" `ortak/graf-secim.json` yazar; bu mod 2 sn'de bir okur (zaman damgası karşılaştırması, dosya silinmez), düğümü seçer ve pane'i öne alır.

## Doğrulama

```bash
claude plugin validate jarvis/mods/jarvis-graf
```

```bash
claude plugin test jarvis/mods/jarvis-graf
```

## Sürümler

v0.1 (2026-10-27) ilk pane · v0.2 (2026-11-03) seans şeritli graf, ızgara, zengin detay, HTML aç onarımı, oda köprüsü.
