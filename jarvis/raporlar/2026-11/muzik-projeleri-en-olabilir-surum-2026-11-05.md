# Müzik projeleri: en olabilir sürüm brifi (2026-11-05)

Üretici: Jarvis; 3 paralel atlas taraması. AS-OF 2026-11-05. Ölçüt yalnız yapılabilirlik (Salih 11-05): kişisel, yerel, çalışan en kısa yol; lisans not olarak durur, filtre değildir. Atlaslar çoğunlukla arama özetinden okudu; `[?]` doğrulanmadı.

Kaynak raporlar: `2026-11-05-muzik-atlas-1-erisim-kesif.md` · `2026-11-05-muzik-atlas-2-temsil-kodlama.md` · `2026-11-05-muzik-atlas-3-uretim-kalite.md` (aynı dizin).

Donanım: RTX 3060 Laptop, 6 GB ekran belleği (nvidia-smi, 11-05).

## 0. Ortak çekirdek: müzik kodlama şeması
İki eksen: kanal (davul, bas, vokal, diğer, tam miks) x nitelik (gömme vektörü, tempo, ton, enerji, etiketler). Alan adları JAMS ad alanlarına hizalı JSON. Depo: başta düz numpy, sonra sqlite-vec.

## 1. Şarkı yönlendirme (melez)
Kararlar (Salih 11-05): melez mimari; "koru" boyutları öngörülebilir, serbest boyutlarda kontrollü rastgelelik; amaç keşif; yerel dosyalar.

| halka | araç | not |
|---|---|---|
| çalma + "şu an çalan" | mpv, adlandırılmış boru üzerinden komut | kuyruğa ekleme ve bitiş olayı `[?]` |
| ayrıştırma | Demucs `htdemucs_ft` | 4 kanal; depo 2025 arşivlendi, çalışır |
| kanal gömmesi | MERT (yalnız ses) | 1024 boyut |
| metin-ses uzayı | LAION-CLAP music | hedef tarifinin aranması |
| tempo, vuruş, etiket | beat_this + Essentia modelleri | |
| ipucu çevirisi | dil modeli -> {kanal, nitelik, yön, şiddet} + hedef tarifi | şarkı adı söylemez |
| seçim | "koru" = sert kısıt (kanal uzaklığı eşiği); kalan adaylarda çeşitlilik örneklemesi | her öneride "benzer: ... / sürpriz: ..." satırı |
| sıralayıcı | CatBoost, birkaç yüz dinle/atla kaydından sonra | başta yok |
| keşif havuzu | kendi dosyaların + MTG-Jamendo (55 bin+) + Free Music Archive (106.574) | zevke uyum ölçülmedi |

Spotify çekirdek dışı: analiz uç noktaları yeni uygulamalara kapalı (2024-11-27); çalan parça ve kuyruk açık ama Premium şartlı ve daralıyor. Yalnız isteğe bağlı yüzey.

İlk çalışan çıktı: 200-500 parça, toplu analiz, mpv çalarken tek cümle ipucu, sıradaki parça + gerekçe satırı.

Riskler: (1) ayrıştırılmış kanalda gömme kalitesi literatürde ölçülmemiş, 50-100 parçalık kendi değerlendirmemiz gerekir; (2) toplu analiz süresi, işlemcide 50 bin parça yaklaşık 182 gün (atlas hesabı), ekran kartı şart, 6 GB yeterliliği `[?]`; (3) tek kullanıcıda atlama oranı zayıf ölçüt.

## 2. Müzik üretimi (yalnız davul, dört ölçü)
Kararlar (Salih 11-05): sembolik kodlama + üret-ve-ele; ses kaydına ölçülebilir kalite bariyeri.

| halka | araç | not |
|---|---|---|
| veri | Groove + genişletilmiş sürümü, yalnız nota kısmı | atıf şartlı açık lisans |
| sözlük | MidiTok | 11 yöntem |
| üretici | sürüm 1: kural/Markov; sürüm 2: küçük koşullu dizi modeli | eğitim süresi kaynağı bulunamadı |
| puanlayıcı | CatBoost; öznitelik: yoğunluk, senkop, tekrar, mikro-zamanlama | gerçek kalıp pozitif, bozulmuş negatif = gerçekçilik; beğeni için Salih ikili karşılaştırması |
| seçim | Jev karar katmanı | |
| ses | örnek çalma kendi kodumuz + pedalboard efekt zinciri | determinizm testi: iki süreçte aynı çıktı özeti |

Kalite bariyeri taslağı (atlas önerisi, kalibre değil): kayıpsız, en az 44.1 kHz / 16 bit · 16-20 kHz sert kesim + dik düşüş = ret · 3+ ardışık tam ölçek örnek = ret · doğru-tepe en çok -1 dBTP · gürültü tabanı en çok -60 dBFS · kuyruk son 50 ms içinde -50 dBFS altı · DC kayması en çok 0.001. Öğrenilmiş kalite kestirimi yalnız göreli sıralama (alt %20 elenir).

İlk çalışan çıktı: bariyerden geçmiş tek davul seti, seçenekle (tempo, yoğunluk, tür) 20 aday kalıp, puanlanmış ilk 3 ses dosyası.

Riskler: (1) eşikler kendi iyi/kötü etiketli örneklerle ayarlanmalı; (2) beğeni etiketi yokken model ortalama kalıba kayar; (3) üçlüyü birlikte yapan hazır proje bulunamadı (tek arama, zayıf kanıt).

## 3. Sıra önerisi
Şema -> proje 1 çevrim-dışı analiz hattı -> proje 1 canlı döngü -> proje 2 bariyer + üretici. Lean tarafı ayrı: Paperproof denemesi sırada, video sürümü park.
