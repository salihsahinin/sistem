# Seans Teslim Raporu — 2026-08-26, oturum `1801d9ae` (kapsam-dışı görev)

*(Şablon: `core/sablonlar/seans-teslim.md`. Bu oturum JARVIS kanonuna dokunmadı — kayıt yalnız hijyen + iz için tutulur, m.8 silme-yasağı.)*

- **Bugün gerçekten ne değişti:** JARVIS reposunda **hiçbir kod/kanon/skill değişmedi**. Oturumun tamamı sahibinden.com araç ilanları (dış veri, repoya hiç girmedi) `km`/`price` kolonlarını monoton-artan-genişlikte segmentlere ayırma sorusuydu — Salih'in kendi analiz işi, JARVIS-meta değil. Kapanışta rutin hijyen koştu: `katman-hatti.py` (silver `5f6f4fc`→`ce5530a` tazelendi), `silver-saglik.py --kapi` (ERROR 0 · WARN 1, ön-bilinen T-C3-ılık kalıntı 112 · EXIT 0), `skill-esik.py` (0 sapma), `kural-sayaci.py` (18/100), `anakronizm-denetim.py` (EXIT 0, yeni ihlal yok). Bronz/silver/gold türetilmiş dosyalar (`veri/…`) bu yüzden güncellendi — içerik değil, gösterge.
- **Hangi karar verildi (kaynak + gerekçe + geri-açma):** Yok. Katman-1/2 kararı üretilmedi.
- **Hangi fikir aday kaldı (karar DEĞİL):** Yok (JARVIS fikir kutusuna eklenecek meta-fikir üretilmedi). Genellenebilir tek teknik bulgu `kuyruk/build-tartisma-notlari.md`'ye pointer olarak düşüldü (aşağıda).
- **Sonraki ilk iş:** DEĞİŞMEDİ — kapsüldeki 0/1/2/3 sırası aynen geçerli (Salih: KB-62..68 masası → E-4; Carvis: İB-50; kapanışlarda anakronizm-denetim.py).
- **Neyi yeniden açmak için hangi koşul gerekir:** Uygulanmaz (karar yok).

## Hasat

1. **Özütler:**
   - Kullanıcı bir yöntem ADI söylüyorsa (ör. "clustering") ama asıl istediği bir KISIT ise (ör. "genişlik hep artmalı"), adı verilen araç o kısıtı garanti etmeyebilir — kısıtı ayrı teşhis edip doğru aracı (burada: PAVA/izotonik regresyon, veri gerektirmez) önermek, adı geçen aracı (log-dönüşümlü KMeans/Jenks, ham veri gerektirir) da elden bırakmadan sunmak gerekti.
   - Yalnız bitmiş bin sınırları (7-9 sayı) elde olduğunda gerçek KMeans/Jenks çalıştırılamaz — bunlar bir POPÜLASYONU kümeler, sınır listesinin kendisini değil; log1p→exp uygulamak aynı sayılara özdeşlik dönüşümü olur, hiçbir şeyi değiştirmez. Bu ayrım net konuşulmadan "dönüşüm yaptım" denirse yanıltıcı olur.
   - Ham veri paylaşılmadığında yerel dosya sistemini (Downloads/Desktop/Documents + repo) taramak ucuz ve hızlı bir doğrulama adımı; sonuç negatifse kullanıcıya tekrar sormak yerine AskUserQuestion ile tıkanma noktasını somutlaştırmak denendi.
2. **Wiki-delta:** Yok — JARVIS-spesifik bir kavram değil (genel veri bilimi tekniği), sözlük/wiki kapsamı dışı.
3. **Verilebilir miydi? (V20):** Evet, dış-veri danışmanlığı bir genel-amaçlı ajana devredilebilirdi; devredilmedi çünkü doğrudan sohbet akışında geldi ve m.25 (küçük direkt iş) eşiğinin altında kaldı.
4. **Token×zaman etiketi:** az token · kısa süre (tek oturum, kod doğrulamalı teknik danışmanlık); beklenti tuttu.

## Ek not — kapanış hijyeni
- Bilinen açık hata (yeni değil, bu oturumda değişmedi): `amb_olgu_kosum_sonuc.kosum_id → amb_olgu_kosum` ihlal 5 (İB-50, grain uyuşmazlığı — sonuç workflow-düzeyi id taşıyor, koşum tablosu ajan-düzeyi).
- `acik_salih_karari` 15, `acik_icra_borcu` 24 (açılış brifindeki 23'ten +1 — doğal veri tazeleme, bu oturumun kararı değil).
