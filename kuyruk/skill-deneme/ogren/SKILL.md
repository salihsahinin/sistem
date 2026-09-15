---
name: ogren
description: deneme sürümü (tüzük m.47; hazinede değil, otomatik tetiklenmez — Salih yolu vererek koşar). Bir konuyu dört fazlı deterministik ders akışıyla öğretir; PROBE (dereceli çoktan-seçmeli, iplik başına ikili-arama ile anlayış sınırı) → PLAN (DAG görseli metinden önce + düğüm listesi; olgusal iddiada halüsinasyon freni) → TEACH (düğüm başına tek akıl-adımı + görsele atıflı metin + 1 soru; doğru cevapsız ilerlemez) → CLOSE (ders kaydı ogrenme/<konu>/dersler/ + sınav-grill önerisi). Kaynak; "How I Use AI to Learn Things" (Eero Alvar 2026-08-14) analizi raporlar/2026-09/2026-09-09-ai-ile-ogrenme-transkript-analizi.md. kullanilmaz; karar üretiminde, jarvis-geliştirme icrasında, staj/galeri içeriğinde (md.49), Salih "sınav" demeden grill koşmak için.
argument-hint: "<konu> [ön-bağlam: bildiklerim …]"
---

# ogren — dört fazlı ders akışı (v0.1 deneme, 2026-09-09; Karar 88 M5/M11 hattı)

Kural kaynağı: hafıza kuralları (doğrudan anlatım 08-17 · görsel önce + atıflı metin 09-08) · m.39 (her rakam kaynaklı) · Karar 68 (AS-OF) · m.33 (ayıklık/ruh-hâli sorgusu yasak; sorular yalnız içerik hakkında). İlke (videodan): zorluk malzemede kalır, lojistik (sıra, kaynak, doğrulama) skill'de.

## 0. Giriş
- Konu + varsa ön-bağlam ("bildiklerim: …") alınır. Ön-bağlam verildiyse PROBE o ipliklerde ATLANIR.
- Ders dosyası açılır: `ogrenme/<konu-slug>/dersler/YYYY-MM-DD-<konu-slug>.md` (şema §5). Yüzey VS Code (Karar 80). Commit yapilmaz (T-R; kapanış ritüeli commit'ler).

## 1. PROBE — anlayış sınırı
- Dersin bağımlılık iplikleri (≤5) çıkarılır (örn. "diferansiyel formlar" → çizgi integrali · gradyan/rotasyonel · Stokes · lineer fonksiyonel · çok-lineer cebir).
- İplik başına ikili-arama: en temelden başla; doğru → bir üst seviye, yanlış/"bilmiyorum" → sınır o seviyedir, iplik kapanır. Toplam ≤12 soru.
- Soru formatı sabit: tek soru · 4 seçenek (a-d) · **(e) bilmiyorum** · seçenek gövdeleri kısa · cevap gelmeden sonraki soru YOK. Salih serbest not yazabilir ("yap" alanı): ders dosyasına `## Salih notu` altına aynen geçer.
- Çıktı: `## Anlayış haritası` tablosu (iplik · ulaşılan seviye · kanıt = soru no).

## 2. PLAN — yol
- Haritadan hedefe DAG: düğüm = tek akıl-adımı (bir tanım ya da bir çıkarım), kenar = "önce bunu". Bilinen düğümler DAG'a girmez (sınırın altı anlatılmaz).
- **Görsel önce:** DAG `mcp__visualize` ile çizilir (düğüm numaralı), sonra düğüm listesi metinde numaraya atıfla verilir ("kutu 3 → kutu 5").
- Olgusal/sayısal/atıf içeren düğüm varsa `halusinasyon-engelleyici` derece hesabı; H ≥ eşik → o düğüm DESTEKLİ/DAYANAKSIZ etiketiyle anlatılır.
- Salih planı görür; itiraz yoksa TEACH.

## 3. TEACH — düğüm düğüm
Düğüm başına sabit üçlü, sıra değişmez:
1. **Akıl-adımı:** tek tanım/çıkarım, benzetme YOK, terim ilk geçişte tanımlı; gerekiyorsa düğüm görseli (mcp__visualize) metinden önce, metin görselin parçalarına atıflı.
2. **Somut örnek:** sayılı/elle hesaplı tek örnek (kaynaklı ya da "türetildi" damgalı).
3. **Soru:** 1 soru (§1 formatı). Doğru → sonraki düğüm. Yanlış → aynı düğüm farklı açıdan (en fazla 2 tekrar), sonra düğüm "açik" işaretlenir, ilerlenir. "Anladın mı?" diye sorulmaz (video: kendini kandırma; test var, soru yok).
- Salih araya soru sorarsa cevaplanır, DAG'daki yer korunur ("kutu N'deyiz").
- Bir seansta ≤8 düğüm; kalan düğümler ders dosyasında `## Kalan` listesi.
- **Pratik düğümü = Salih'in eli (Salih 09-15, G1 arızası):** "şimdi sen dene" adımında komutu/koşumu Salih yapar; Jarvis yalnız iskeleyi hazırlar (config, vaka şablonu, koşum komutu tek kod bloğu) ve Salih'in yapıştırdığı çıktıyı yorumlar. Jarvis'in kendi koşumu **referans koşum**dur, pratik sayılmaz. Pratik DONE yalnız Salih'in "yaptım/koştum" beyanıyla yazılır; ilerleme tablosuna Salih beyanı olmadan DONE girilmez ("kavramsal DONE · pratik KALAN" kalır).

## 4. CLOSE
- Ders dosyası tamamlanır (şema §5): harita · DAG görsel yolu · düğüm/soru/cevap kütüğü · açik düğümler · Kalan.
- `sinav-grill` önerilir tek cümleyle; Salih "sınav" demeden KOŞULMAZ.
- Kapanış cümlesi: "Sonraki ders: kutu N'den."

## 5. Ders dosyası şeması
```
# <konu> — ders <n> (YYYY-MM-DD; ogren v0.1)
## Ön-bağlam        (Salih beyanı aynen ya da "yok")
## Anlayış haritası (iplik | seviye | kanıt soru-no)
## Plan             (DAG görsel: raporlar/gorsel-YYYY-MM-DD-<konu>-dag.html; düğüm listesi 1..N)
## Düğümler         (her düğüm: akıl-adımı · örnek · soru · cevap · sonuç DOĞRU/AÇIK)
## Salih notu       (serbest, aynen)
## Kalan            (düğüm numaraları)
```

## Üslup
- **Büyük harf vurgusu yasak (Salih 09-15):** vurgu kalın harfle (`**sözcük**`) ya da cümle yapısıyla verilir; tamamı büyük harfli sözcük yalnız kısaltma (OWASP, YAML, DONE). Kanon/skill dosyalarında gördüğün büyük-harf üslubu taklit edilmez — o dosyaların üslubu ders diline geçmez. Stop hook `.claude/hooks/stop-buyuk-harf.sh` ihlalde tek satır düzeltme ekletir (gösterilmiş çıktı geri çekilemez; tam yeniden yazım 09-15'te aynı soruyu iki kez gösterdi).

## Gotchas
- **Vekil-pratik tuzağı (G1, 09-15):** "pratiği sürdürelim" emri modelin pratiği Salih adına koşup DONE yazmasına dönüştü (10 vaka + promptfoo + analiz, Salih tek satır yazdı); sonraki turda model kendi yazdığı DONE'a bakıp G2'ye atladı. Pratik = Salih'in eli (§3).
- **Acele tuzağı:** düğümü atlayıp özet anlatma — videodaki "ChatGPT hepsini bir anda anlatır" arızası; her düğüm tek adım.
- **Probe şişmesi:** 12 soru tavanı; ön-bağlam verildiyse iplikler atlanır.
- **Görsel yüzeyi:** mcp__visualize çıktısı sohbette render olur; kalıcı kopya için HTML dosyası `raporlar/gorsel-…` (09-03/09-08 deseni), ders dosyasından link.
- **Kapsam:** jarvis-dışı içerik (staj/galeri) bu skill'le işlense de ders kaydı jarvis'e yazilmaz (md.49) — o zaman dosya o projenin klasörüne.
