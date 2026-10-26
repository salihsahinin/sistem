# Portal Parkur

Birinci şahıs parkur + portal oyunu: Mirror's Edge tarzı beyaz çatılarda koşu, duvar koşusu, kenara tutunup çıkma ve kayma; Aperture tarzı test odalarında bilek-tipi portal cihazıyla mavi/turuncu portal, ışık köprüsü, fırlatma plakası ve itki jeli. Godot 4.7.2 ile yazıldı; tüm geometri, eller ve sesler kodla üretilir, dış varlık dosyası yoktur.

## Çalıştırma

- `oyna.bat` (Godot `C:\tools\godot\Godot_v4.7.2-stable_win64.exe` bekler; yoksa dosya içindeki adresten indirilir).
- Elle: `Godot_v4.7.2-stable_win64.exe --path <bu klasör>`.
- Otomatik mekanik testi: `test.bat` → `test_cikti\` içine ekran görüntüleri + `rapor.json`; çıkış kodu = başarısız test sayısı.

## Kontroller

| Tuş | İş |
|---|---|
| W A S D | hareket (koşu varsayılan; sürekli koşunca momentum artar) |
| Shift | sprint (momentum daha hızlı dolar) |
| Boşluk | zıpla · havada yan duvar varken otomatik duvar koşusu · duvara bakıp basınca dikey tırmanış · duvar koşusunda basınca duvardan atlama · kenar altında mantle |
| Ctrl / C | hızlıyken kayma, yavaşken çömelme; inişte basılıysa yuvarlanma (hız korunur) |
| Sol tık / Sağ tık | mavi / turuncu portal (yalnız beyaz panellere) |
| R | kontrol noktasına dön · Esc fare serbest/yakala · F3 durum satırı |

## Akış

Çatı A → 5 m boşluk atlayışı → Çatı B (1.1 m duvar vault) → kırmızı şeritli pano üzerinde duvar koşusuyla 8 m boşluk → Çatı C (kırmızı kapı) → koridor → 8 m düşüşle Oda 1 (çukur: ışık köprüsü ya da zemin pedi → uzak duvar portalı) → pencereli koridor (turuncu itki şeridi) → Oda 2 (fırlatma plakası → üst platform → cam kabin bitiş). Düşünce son kontrol noktasına dönülür, süre HUD'da.

## Dosyalar

- `betikler/oyuncu.gd` parkur durum makinesi (YERDE · HAVADA · DUVAR_KOSU · DUVAR_TIRMANIS · KAYMA · TIRMANMA) + portal geçişinde hız/yön dönüşümü.
- `betikler/portal_silahi.gd` ışınla yerleştirme, yüzeye sığdırma, çift eşleme, portal arkasındaki duvar için çarpışma istisnası, portal içinden atış.
- `betikler/eller.gd` kol/el/cihaz (primitif), duruma göre el animasyonu.
- `betikler/seviye.gd` tüm seviye geometrisi + ortam/ışık; `shaderlar/panel.gdshader` dünya-uzayı panel ızgarası.
- `betikler/hud.gd` nişangah, hız bulanıklığı (`shaderlar/hiz_bulanik.gdshader`), süre.
- `betikler/ses.gd` yordamsal WAV sentezi (adım, zıplama, iniş, portal, rüzgar).
- `betikler/test_kosum.gd` otomatik test (sanal girdi + ekran görüntüsü).
- `sahneler/portal.tscn` eklentinin Portal3D düğümü elle kurulmuş (çalışma zamanında yerleştirilir).

## Kaynaklar ve lisanslar

- Portal görüntüleme/teleport: `addons/portals` = [VojtaStruhar/godot-portals-plugin](https://github.com/VojtaStruhar/godot-portals-plugin) (MIT, Vojtěch Struhár; lisans metni klasörde). Oval maske shader'ı ve çalışma zamanı yerleştirme bu projede eklendi.
- Parkur denetleyicisi fikirleri (duvar koşusu ışınları, eğri yerçekimi, mantle ışınları): [DeiranZ/godot-parkour-fps-controller](https://github.com/DeiranZ/godot-parkour-fps-controller) (MIT) ve [Gab-ani/Godot-Parkour-And-Advanced-Movement](https://github.com/Gab-ani/Godot-Parkour-And-Advanced-Movement). Kod yeniden yazıldı.
- Portal silahı yerleştirme fikri: [xen-42/godot-portal-gun](https://github.com/xen-42/godot-portal-gun) (Godot 3).
- Dying Light / Portal 2 / Mirror's Edge ticari kodu kullanılmadı; mekanikler açık kaynak karşılıklarından ve genel bilinen tekniklerden inşa edildi.
- Referans depolar `referans/` altında klonludur (git dışı).
