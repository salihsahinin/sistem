# Bitirme tezi: iki eklemli kol, ders 1 (2026-11-06 → 11-08; ogren v0.2) · Sektör: Two-Link Planar Manipulator Modeling and Control · AS-OF 2026-11-08

Kaynak: Mihelj ve ark., Robotics, 2. baskı, Springer 2019, Bölüm 5 (s. 49-68), 9 (s. 123), 10 (s. 133-141). Tez başlığı: İki Eklemli Robot Kolunda Modelleme ve Yörünge Takibi: Sinir Ağları, MPC ve Pekiştirmeli Öğrenme (Taşlı, Abatay, Şahin). Oturum: fork, günlük sohbet yüzeyi.

## Ön-bağlam
Yok (müzik dersi ölçümünde 5 iplik başlangıç seviyesi; tez için ayrı ölçüm yapılmadı, Salih doğrudan anlatım istedi).

## Plan (12 kutu)
1 Joint Space and Task Space · 2 Forward Kinematics · 3 Inverse Kinematics · 4 Jacobian and Singularities · 5 Workspace · 6 Manipulator Dynamics · 7 Trajectory Planning · 8 Computed Torque Control (8a PD, 8b yerçekimi telafisi, 8c ters dinamik, 8d kazanç ve model hatası) · 9 Neural Network Dynamics Learning · 10 Model Predictive Control · 11 Reinforcement Learning for Control · 12 Benchmarking Controllers.
Bağımlılık: 1→2→3→4→5 · 2→6→8 · 7→8 · 8→9,10,11→12.

## Düğümler (soru · cevap · sonuç)
| kutu | soru özü | cevap | sonuç |
|---|---|---|---|
| 2 | θ1=90, θ2=−90 uç nokta | d (yanlış), yeniden anlatım; θ2=180 soru → b | DOĞRU (2. tur) |
| 3 | hedef (0;2) çözüm sayısı | c | DOĞRU |
| 4 | θ2=30 det J | a | DOĞRU |
| 5 | l2=0,5 hedef (0;0,3) | b | DOĞRU |
| 6 | dik ve açık kol yerçekimi momenti | b | DOĞRU |
| 7 | θ2 orta nokta hızı | e → yeniden anlatım; T=4 tepe hız → c | DOĞRU (2. tur) |
| 8a | Kp=100, e=0,1 moment | b | DOĞRU |
| 8b | telafi açıkken kalıcı hata | a | DOĞRU |
| 8c | e=0 iken moment | c | DOĞRU |
| 8d | Kp=400 kritik Kd | b | DOĞRU |

Görseller: mcp__visualize etkileşimli widget, kutu 1-8 her biri için (kol + kaydırıcı; kutu 6 fork yorumuyla kuvvet vektörleri + işaretli toplam eklendi; kutu 8 üç denetleyici simülasyonu).

## Salih notu
- 11-06: "kutu 1 ve 2'yi görsel olarak anlat, böyle anlamıyorum" → her kutuya etkileşimli görsel.
- 11-08 (fork yorumu): kuvvet vektörlerinin yönü, büyüklüğü, başlangıç noktası ve vektörel toplam görünsün.
- 11-08: kutu 8 ilk anlatımı çok sıkışık, formül tanımları yetersiz → kutu 8a-8d'ye bölündü; kural hafızaya (feedback-ders-tempo-tek-fikir).

## Kalan
Kutu 9, 10, 11, 12 (kitapta yok, tezin katkısı; her biri alt adımlara bölünerek). Pratik: kutu 2-8 formüllerinin Python/MATLAB simülasyonu Salih'in eliyle, KALAN.

## ⌥ Jarvis notu
Kutu 8 simülasyon kodu widget içinde (Euler, dt=0,002); tez simülatörünün iskeleti olarak taşınabilir. Kaynak ÇIKTI: `C:\Users\sasah\AppData\Local\Temp\rob.txt` (pdftotext).
