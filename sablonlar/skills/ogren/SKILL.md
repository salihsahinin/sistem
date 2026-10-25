---
name: ogren
description: Bir konuyu dört fazlı deterministik ders akışıyla öğretir ve öğrenme yan-oturumunun protokolünü taşır; açılış (kurs README + ilerleme) → `PROBE` (≤12 dereceli çoktan-seçmeli, "(e) bilmiyorum", doğru şık konumu rastgele) → `PLAN` (DAG görseli metinden önce) → `TEACH` (kutu başına akıl-adımı + örnek + 1 soru; sektör başlığı AS-OF; pratik düğümünde komutu Salih koşar) → `CLOSE` (ders kaydı + ilerleme + PR). Kullan; "seans başı, <şerit>" (evals, guvenlik, baglam, mit-6006, mit-6042j, mat-felsefesi), "ders anlat", "öğret", "kutu N'den devam", "pratiği sürdürelim" dendiğinde. Kullanma; sade "seans başı" (seans-acilis), karar üretiminde, jarvis-geliştirme icrasında, staj/galeri içeriğinde (md.49), Salih "sınav" demeden grill koşmak için, ürün turu hükmünü Salih yerine vermek için.
argument-hint: "<şerit ya da konu> [ön-bağlam: bildiklerim …]"
metadata: { owner: jarvis, version: "0.2.0-deneysel-m29", kural: "core/skill-uretim-semasi.md §4b", ib: "İB-89 P1+P2", karar: "Karar 96 M2 A2 · Karar 94 EK · Karar 88 M5/M11" }
---

# ogren — dört fazlı ders akışı + öğrenme oturum protokolü (v0.3 ALAN SÜRÜMÜ, 2026-09-21, Karar 105; v0.2 09-15 Jarvis kopyası `jarvis/.claude/skills/ogren/` öğretim-tasarımı için kalır)

**Alan-ajanı farkı (Karar 103 EK 1 · Karar 105 M4):** bu skill alan ajanının dizininde (`~/sistem/<alan>/`) koşar; şerit yolları `ogrenme/<şerit>/` **bu dizine** görelidir; ders iskeleti (`PROBE` soruları · `PLAN` DAG · kutu başlıkları) Jarvis'ten `cc/gelen/ders-<hafta>.md` ile gelir — varsa aynen kullanılır, `PROBE`/`PLAN` üretilmez; yoksa önceki dersin `## Kalan` listesiyle devam edilir, **yeni hafta açılmaz** (Jarvis'e `cc/giden/` ile "iskelet gerekli: <hafta>" notu). Oturum: worktree `C:\sistem\wt\<alan>` + kendi dalı `oturum/<tarih>-<alan>`, pathspec-only; seans sonunda dal push + PR, birleştirme Jarvis'te Salih beyanıyla (protokol §5 EK-5; EK-4 süpersede 2026-10-16). `mcp__visualize` yoksa DAG `raporlar/gorsel-*.html` olarak elle yazılır.


Tür: T-R ritüel (öğrenme yan-oturumu; yan-etki: ders dosyası + ilerleme tablosu + branch commit'i; kapsül/pano/defter'e yazmaz). Kural kaynağı: hafıza kuralları (doğrudan anlatım 08-17 · görsel önce + atıflı metin 09-08 · pratik = Salih'in eli 09-15) · m.39 (her rakam kaynaklı) · Karar 68 (AS-OF) · Karar 73 (her derste ≥1 formül) · m.33 (sorular yalnız içerik hakkında). İlke (Eero Alvar 2026-08-14 analizi, `raporlar/2026-09/2026-09-09-ai-ile-ogrenme-transkript-analizi.md`): zorluk malzemede kalır, lojistik (sıra, kaynak, doğrulama) skill'de. Canlı koşum kanıtı (K4): evals H1-H3 (09-11→14, κ=1,0) + guvenlik G1 (09-14/15). Eski protokol metni (format v2, 07-15) `arsiv/ogrenme-oturum-protokolu-v2-2026-09-15.md`.

## 0. Açılış (oturum protokolü)
1. Yüzey Salih'in adlandırdığı şerittir ("seans başı, evals"); sade "seans başı" bu skill'i tetiklemez. Açılış sözü zaman işareti değildir: tarih yalnız sistem saatinden (`date`), emekli selamlama tetiği sabah çıkarımı üretmez (zaman-kayması freni, Salih 08-15/09-09; anahtar kaydı `oturum-acilis-tetigi`). Alan ajanında worktree yok: cwd `~/sistem/<alan>`, main; ilk iş `git log -3 -- .` canlı-oturum kapısı (seans-acilis).
2. Okunur: `ogrenme/<şerit>/README.md` (müfredat tablosu + sınırlar) → `ogrenme/<şerit>/ilerleme.md` (sıradaki hafta, önceki dersin `## Kalan` ve açık düğümleri) → önceki ders dosyası yalnız `## Kalan` bölümü.
3. Sektör başlıkları: haftanın başlığı + kutu başlıkları README tablosundan alınır, ders başında canlı teyit (WebFetch/WebSearch, AS-OF damgası); değiştiyse README tablosu güncellenir (Karar 68).
4. Konu + varsa ön-bağlam ("bildiklerim: …") alınır. Ön-bağlam verildiyse `PROBE` o ipliklerde atlanır.
5. Ders dosyası açılır: `ogrenme/<şerit>/dersler/YYYY-MM-DD-<hafta>-<konu>.md` (şema §5). Yüzey VS Code (Karar 80). Commit yalnız `git add ogrenme/<şerit>/<yol>` ile, seans sonunda (§4).

## 1. Probe — anlayış sınırı
- Dersin bağımlılık iplikleri (≤5) çıkarılır (örn. "diferansiyel formlar" → çizgi integrali · gradyan/rotasyonel · Stokes · lineer fonksiyonel · çok-lineer cebir).
- İplik başına ikili-arama: en temelden başla; doğru → bir üst seviye, yanlış/"bilmiyorum" → sınır o seviyedir, iplik kapanır. Toplam ≤12 soru.
- Soru formatı sabit: tek soru · 4 seçenek (a-d) · **(e) bilmiyorum** · doğru şıkkın konumu rastgele (hafıza 09-11: hep aynı konum kalıp öğretir) · seçenek gövdeleri kısa · cevap gelmeden sonraki soru yok. Salih serbest not yazabilir: ders dosyasına `## Salih notu` altına aynen geçer.
- Çıktı: `## Anlayış haritası` tablosu (iplik · ulaşılan seviye · kanıt = soru no).

## 2. Plan — yol
- Haritadan hedefe DAG: düğüm = tek akıl-adımı (bir tanım ya da bir çıkarım), kenar = "önce bunu". Bilinen düğümler DAG'a girmez.
- **Görsel yüzeyi (Salih 2026-10-16, A + aynı gün eki: "terminalden öğrenme işini yalnızca olarak kullanmayacağım"):** iki yol da aktiftir, seçim araç listesine göre yapılır, yüzey adına göre değil. (1) **Uygulama yolu:** `mcp__visualize` araç listesinde varsa (Claude masaüstü/uygulama yüzeyi, Claude Code'un uygulama içi oturumu dahil) görsel bu araçla sohbet içinde çizilir; 2026-10-16 öncesi akış aynen. (2) **Terminal yolu:** araç yoksa (Claude Code terminali, Herdr) görsel = **Artifact** sayfası: `raporlar/gorsel-YYYY-MM-DD-<konu>-<kutu>.html` yazılır, `artifact-design` yüklenir, Artifact aracıyla yayımlanır, bağlantı cevapta verilir; ders boyunca aynı dosya güncellenerek aynı bağlantıda büyür. Ders kaydı ve ilerleme dosyası iki yolda aynıdır; bir ders yüzey değiştirerek sürebilir.
- **Görsel önce:** DAG görsel yüzeyinde çizilir (düğüm numaralı), sonra düğüm listesi metinde numaraya atıfla ("kutu 3 → kutu 5"). Her düğüm başlığı sektör başlığı taşır (`### Kutu 3 — Dolaylı injection · Sektör: Indirect Prompt Injection`).
- Derinlik etiketi (format v2 mirası, isteğe bağlı): düğüm [S] sezgisel / [O] orta / [T] tam; varsayılanı Jarvis atar (ölçüt: jarvis kararlarına uzaklık), Salih "bunu [T] yap" der.
- Olgusal/sayısal/atıf içeren düğüm varsa `halusinasyon-engelleyici` derece hesabı; H ≥ eşik → o düğüm DESTEKLİ/DAYANAKSIZ etiketiyle anlatılır.
- Salih planı görür; itiraz yoksa `TEACH`.

## 3. Teach — düğüm düğüm
Düğüm başına sabit üçlü, sıra değişmez:
1. **Akıl-adımı:** tek tanım/çıkarım, benzetme yok, terim ilk geçişte tanımlı; gerekiyorsa düğüm görseli (görsel yüzeyi §2, Salih "kutu N'i görselleştir" derse mekanizmayı adım adım simüle eden etkileşimli görsel) metinden önce, metin görselin parçalarına atıflı; metinde atıf yapılan her görsel gerçekten üretilir.
2. **Somut örnek:** sayılı/elle hesaplı tek örnek (kaynaklı ya da "türetildi" damgalı); örnek sonuna kadar işletilir (BPE "the": t·h·e → th·e → the, neyin neden birleştiği gösterilerek). Her derste ≥1 formül: tanım + sembol tablosu + elle işletilmiş sayısal örnek (Karar 73).
3. **Soru:** 1 soru (§1 formatı). Doğru → sonraki düğüm. Yanlış → aynı düğüm farklı açıdan (en fazla 2 tekrar), sonra düğüm "açik" işaretlenir, ilerlenir. "Anladın mı?" diye sorulmaz.
- Salih araya soru sorarsa cevaplanır, DAG'daki yer korunur ("kutu N'deyiz"). Tempo: tek teslimde ≤3 kavram.
- Bir seansta ≤8 düğüm; kalan düğümler ders dosyasında `## Kalan` listesi.
- **"⌥ Jarvis notu" bloğu:** düğümün depodaki karşılığı (hangi script/hook/kural) tek satır; ürün turu aday listesi bu bloklardan toplanır (§6). Ders içinde 3-model sunulmaz (format v2 Yarı-2 emekli; Karar 94 EK seri sonuna taşıdı).
- **Pratik düğümü = Salih'in eli (Salih 09-15, G1 arızası):** araç/format/komut öğreten düğümde "şimdi sen dene" adımı zorunlu (hafıza 09-11): Jarvis yalnız iskeleyi hazırlar (config, vaka şablonu, koşum komutu tek kod bloğu), komutu/koşumu Salih yapar, Jarvis yapıştırılan çıktıyı yorumlar. Jarvis'in kendi koşumu **referans koşum**dur, pratik sayılmaz. Pratik `DONE` yalnız Salih'in "yaptım/koştum" beyanıyla yazılır; ilerleme tablosuna Salih beyanı olmadan `DONE` girilmez ("kavramsal `DONE` · pratik `KALAN`" kalır).

## 4. Close
1. Ders dosyası tamamlanır (şema §5): harita · DAG görsel yolu · düğüm/soru/cevap kütüğü · açik düğümler · Kalan · "⌥ Jarvis notu" listesi.
2. İlerleme tablosu (`ogrenme/<şerit>/ilerleme.md`) satırı: hafta · durum (kavramsal `DONE` / pratik `KALAN` ya da `DONE`, yalnız Salih beyanıyla) · ders kaydı yolu · sapma notu. Anlama kapısı geçilmediyse hafta bölünür (m.21).
3. `sinav-grill` önerilir tek cümleyle; Salih "sınav" demeden koşulmaz.
4. Kapanış cümlesi: "Sonraki ders: kutu N'den." Sonra `git add ogrenme/<şerit>/…` + commit (İngilizce mesaj, m.10); dal push + PR `seans-kapanis` son adımıdır (EK-5; main'e push deny'da). Kapsül/pano/defter alan ajanının kendi `seans-kapanis` ritüelinde yazılır.

## 5. Ders dosyası şeması
```
# <konu> — ders <n> (YYYY-MM-DD; ogren v0.2) · Sektör: <güncel İngilizce başlık> · AS-OF <tarih>
## Ön-bağlam        (Salih beyanı aynen ya da "yok")
## Anlayış haritası (iplik | seviye | kanıt soru-no)
## Plan             (DAG görsel: raporlar/gorsel-YYYY-MM-DD-<konu>-dag.html; düğüm listesi 1..N, her düğümde sektör başlığı)
## Düğümler         (her düğüm: akıl-adımı · örnek · soru · cevap · sonuç DOĞRU/AÇIK · ⌥ Jarvis notu)
## Salih notu       (serbest, aynen)
## Kalan            (düğüm numaraları; pratik KALAN ise komut satırı)
```

## 6. Ürün turu (seri sonu; Karar 94 EK-1..4)
Kursun son haftasında koşar; usul `references/urun-turu.md` (a-g: aday listesi → güncel-pratik taraması → 3 model, biri "hiçbiri" → metrik önce → skill-oluşturma sorusu + icra-türü eşlemesi → Salih hükmü masada → icra ana-sırada). Yan oturum aday listesi + metrik taslağı üretir, hüküm vermez.

## Üslup
- Doğrudan tanım + mekanizma + somut örnek; uzatılmış benzetme yok; bilinmeyen terim ilk geçişte parantez içinde sade açıklama; övgü yok.
- **Büyük harf vurgusu yasak (Salih 09-15):** vurgu kalın harfle (`**sözcük**`) ya da cümle yapısıyla; tamamı büyük harfli sözcük yalnız kısaltma (OWASP, YAML, `DONE`). Kanon/skill dosyalarında görülen büyük-harf üslubu ders diline geçmez. Stop hook `.claude/hooks/stop-buyuk-harf.sh` ihlalde tek satır düzeltme ekletir (gösterilmiş çıktı geri çekilemez).

## Gotchas
- **Vekil-pratik tuzağı (G1, 09-15):** "pratiği sürdürelim" emri modelin pratiği Salih adına koşup `DONE` yazmasına dönüştü (10 vaka + promptfoo + analiz, Salih tek satır yazdı); sonraki turda model kendi yazdığı DONE'a bakıp G2'ye atladı. Pratik = Salih'in eli (§3).
- **Acele tuzağı:** düğümü atlayıp özet anlatma ("hepsini bir anda anlatır" arızası); her düğüm tek adım.
- **Probe şişmesi:** 12 soru tavanı; ön-bağlam verildiyse iplikler atlanır. Doğru şık hep aynı konumda olursa kalıp öğretir.
- **Görsel atıf/var:** metinde atıf yapılan görsel üretilmemişse hata (07-15 vakası); kalıcı kopya `raporlar/gorsel-…` HTML, ders dosyasından link.
- **Tetik çakışması:** sade "seans başı" ana-sıra ritüelidir (`seans-acilis`); bu skill yalnız şerit adıyla açılır.
- **Kapsam:** jarvis-dışı içerik (staj/galeri) bu skill'le işlense de ders kaydı jarvis'e yazılmaz (md.49); dosya o projenin klasörüne.
