extends Node
## Otomatik test koşumu (PP_TEST=1): mekanikleri sanal girdiyle sürer, ekran görüntüsü alır,
## test_cikti/rapor.json yazar, çıkış kodu = başarısız sayısı.

var ana: Node3D
var oyuncu: Oyuncu
var rapor: Array = []
var basarisiz := 0
var dizin := ""


func _ready() -> void:
	ana = get_parent()
	oyuncu = ana.oyuncu
	dizin = ProjectSettings.globalize_path("res://test_cikti/")
	DirAccess.make_dir_recursive_absolute(dizin)
	Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
	oyuncu.fare_acik = false
	kos.call_deferred()


func bekle(s: float) -> void:
	await get_tree().create_timer(s).timeout


func ekran(ad: String) -> void:
	await RenderingServer.frame_post_draw
	var img := get_viewport().get_texture().get_image()
	img.save_png(dizin + ad + ".png")


func kontrol(ad: String, ok: bool, veri: String) -> void:
	rapor.append({"test": ad, "ok": ok, "veri": veri})
	if not ok:
		basarisiz += 1
	print("[TEST] %s %s  %s" % [ad, "OK" if ok else "FAIL", veri])


func yerlestir(poz: Vector3, yaw_deg: float, pitch_deg := 0.0) -> void:
	oyuncu.sifirla()
	oyuncu.global_position = poz
	oyuncu.rotation = Vector3(0, deg_to_rad(yaw_deg), 0)
	oyuncu.kamera.rotation.x = deg_to_rad(pitch_deg)
	oyuncu.velocity = Vector3.ZERO
	oyuncu.sanal_girdi = Vector2.ZERO


func bak(hedef: Vector3) -> void:
	var d: Vector3 = (hedef - oyuncu.kamera.global_position).normalized()
	oyuncu.rotation.y = atan2(-d.x, -d.z)
	oyuncu.kamera.rotation.x = asin(clampf(d.y, -1, 1))


func kos() -> void:
	oyuncu.sanal_girdi_aktif = true
	await bekle(0.6)
	await ekran("01_baslangic")

	# T1: koşu hızı
	yerlestir(Vector3(0, 0.2, 9), 0)
	oyuncu.sanal_girdi = Vector2(0, -1)
	await bekle(1.7)
	oyuncu.iz = true
	await bekle(0.3)
	oyuncu.iz = false
	var h := oyuncu.yatay_hiz().length()
	var mc: bool = Ayarlar.al("model") > 0.5
	kontrol("kosu_hizi", h > (5.0 if mc else 8.5), "model=%s hiz=%.2f poz=%s" % ["minecraft" if mc else "parkur", h, oyuncu.global_position])
	await ekran("02_kosu")

	# T2: boşluk atlayışı A→B (kenar z=-12, B z<-17 y=-1)
	yerlestir(Vector3(0, 0.2, 2), 0)
	oyuncu.sanal_girdi = Vector2(0, -1)
	var t := 0.0
	var zipladi := false
	while t < 4.0:
		await bekle(0.02)
		t += 0.02
		if not zipladi and oyuncu.global_position.z < -11.4:
			oyuncu.sanal_zipla = true
			zipladi = true
		if zipladi and oyuncu.is_on_floor() and oyuncu.global_position.z < -16.0:
			break
	var p := oyuncu.global_position
	kontrol("bosluk_atlayisi", p.z < -16.0 and p.y > -1.5 and p.y < 0.5, "poz=%s t=%.2f" % [p, t])
	await ekran("03_atlayis")

	# T3: duvar koşusu (pano x=-4.5, sağ yüzü; oyuncu x=-3.9, z -33'ten -47'ye)
	yerlestir(Vector3(-3.85, -0.8, -30), 0)
	oyuncu.sanal_girdi = Vector2(0, -1)
	t = 0.0
	zipladi = false
	var dk_gordu := false
	var dk_ekran := false
	while t < 4.0:
		await bekle(0.02)
		t += 0.02
		if not zipladi and oyuncu.global_position.z < -34.6:
			oyuncu.sanal_zipla = true
			zipladi = true
		if int(t * 50) % 5 == 0:
			print("[IZ-T3] t=%.2f durum=%s poz=%s v=%s" % [t, Oyuncu.DURUM_AD[oyuncu.durum], oyuncu.global_position, oyuncu.velocity])
		if oyuncu.durum == Oyuncu.Durum.DUVAR_KOSU:
			dk_gordu = true
			if not dk_ekran:
				dk_ekran = true
				await ekran("04_duvar_kosu")
		if zipladi and oyuncu.is_on_floor() and oyuncu.global_position.z < -45.5:
			break
	p = oyuncu.global_position
	kontrol("duvar_kosu_gecis", dk_gordu and p.z < -45.5 and p.y > -1.5, "dk=%s poz=%s t=%.2f" % [dk_gordu, p, t])

	# T4: kenara tutunup çıkma (blok z -49..-55, üst y=2; oyuncu z=-46 → -49 duvarı)
	yerlestir(Vector3(5, -0.8, -45.5), 0)
	oyuncu.sanal_girdi = Vector2(0, -1)
	t = 0.0
	zipladi = false
	while t < 3.0:
		await bekle(0.02)
		t += 0.02
		if not zipladi and oyuncu.global_position.z < -47.6:
			oyuncu.sanal_zipla = true
			zipladi = true
		if int(t * 50) % 10 == 0:
			print("[IZ-T4] t=%.2f durum=%s poz=%s v=%s" % [t, Oyuncu.DURUM_AD[oyuncu.durum], oyuncu.global_position, oyuncu.velocity])
		if oyuncu.global_position.y > 1.9 and oyuncu.is_on_floor():
			break
	p = oyuncu.global_position
	kontrol("tirmanma", p.y > 1.9, "poz=%s durum=%s t=%.2f" % [p, Oyuncu.DURUM_AD[oyuncu.durum], t])
	await ekran("05_tirmanma")

	# T5: portal yerleştirme + geçiş (oda 1: zemin pedi (0,-8.95,-90) → uzak duvar (-5,-7.5,-116))
	yerlestir(Vector3(0, -8.9, -84), 0)
	await bekle(0.3)
	bak(Vector3(-5, -7.2, -116.0))
	oyuncu.portal_silahi.call("ates", 0)
	await bekle(0.6)
	bak(Vector3(0, -8.95, -90))
	oyuncu.portal_silahi.call("ates", 1)
	await bekle(0.6)
	var m: bool = oyuncu.portal_silahi.call("yerlesik_mi", 0)
	var tr: bool = oyuncu.portal_silahi.call("yerlesik_mi", 1)
	kontrol("portal_yerlesti", m and tr, "mavi=%s turuncu=%s %s" % [m, tr, oyuncu.portal_silahi.call("durum_metni")])
	await RenderingServer.frame_post_draw
	for i in 2:
		var vp: SubViewport = oyuncu.portal_silahi.yuvalar[i].portal.get("portal_viewport")
		if vp:
			vp.get_texture().get_image().save_png(dizin + "vp%d.png" % i)
	bak(Vector3(-2, -8.0, -100))
	await bekle(0.3)
	await ekran("06_portallar")
	bak(Vector3(0, -8.95, -90))
	await ekran("07_zemin_portali")
	# mavi portalın 2.5 m önünden bak: içinde zemin portalından yukarı bakış (tavan ışıkları) görünmeli
	yerlestir(Vector3(-5, -8.9, -113.3), 0)
	await bekle(0.2)
	bak(Vector3(-5, -7.4, -116.0))
	await bekle(0.2)
	await ekran("07b_duvar_portali_yakin")
	yerlestir(Vector3(0, -8.9, -84), 0)
	await bekle(0.2)
	# zemin portalına yürü
	oyuncu.rotation.y = 0.0
	oyuncu.kamera.rotation.x = deg_to_rad(-20)
	oyuncu.sanal_girdi = Vector2(0, -1)
	t = 0.0
	while t < 3.0 and oyuncu.teleport_sayisi == 0:
		await bekle(0.02)
		t += 0.02
	oyuncu.sanal_girdi = Vector2.ZERO
	await bekle(0.5)
	p = oyuncu.global_position
	kontrol("portal_gecis", oyuncu.teleport_sayisi >= 1 and p.z < -108, "tp=%d poz=%s t=%.2f" % [oyuncu.teleport_sayisi, p, t])
	await ekran("08_portal_sonrasi")

	# T6: ışık köprüsü (x=7.5, z -95..-105, y=-8.05)
	yerlestir(Vector3(7.5, -8.9, -92), 0)
	oyuncu.sanal_girdi = Vector2(0, -1)
	await bekle(2.2)
	p = oyuncu.global_position
	kontrol("isik_koprusu", p.z < -103 and p.y > -9.5, "poz=%s" % p)
	await ekran("09_kopru")

	# T7: fırlatma plakası → üst platform (y=-3)
	yerlestir(Vector3(0, -8.9, -137.5), 0)
	oyuncu.sanal_girdi = Vector2(0, -1)
	t = 0.0
	while t < 4.0:
		await bekle(0.02)
		t += 0.02
		if oyuncu.global_position.y > -3.2 and oyuncu.is_on_floor():
			break
	p = oyuncu.global_position
	kontrol("firlatma_plakasi", p.y > -3.2 and p.z < -150, "poz=%s t=%.2f" % [p, t])
	await ekran("10_platform")

	# T8: kayma (zemin portalı kaldırılır, yoksa kayarken portala düşer)
	oyuncu.portal_silahi.call("temizle")
	yerlestir(Vector3(0, -8.9, -81), 0)
	oyuncu.sanal_girdi = Vector2(0, -1)
	await bekle(0.9)
	t = 0.0
	while t < 2.0 and not (oyuncu.is_on_floor() and oyuncu.yatay_hiz().length() > (5.0 if mc else 8.0)):
		await bekle(0.02)
		t += 0.02
	var kay_poz := oyuncu.global_position
	oyuncu.sanal_kay = true
	await bekle(0.3)
	var kaydi := oyuncu.durum == Oyuncu.Durum.KAYMA
	await ekran("11_kayma")
	kontrol("kayma", kaydi, "durum=%s kay_poz=%s poz=%s hiz=%.1f" % [Oyuncu.DURUM_AD[oyuncu.durum], kay_poz, oyuncu.global_position, oyuncu.yatay_hiz().length()])

	var f := FileAccess.open(dizin + "rapor.json", FileAccess.WRITE)
	f.store_string(JSON.stringify({"basarisiz": basarisiz, "testler": rapor}, "  "))
	f.close()
	print("[TEST] bitti, basarisiz=%d" % basarisiz)
	get_tree().quit(basarisiz)
