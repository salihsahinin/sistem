extends "res://betikler/seviye.gd"
## Minecraft bunny hop sunucusu tarzı kurs: gökyüzünde yüzen blok platformlar; ilerleme sırası
## başlangıç → düz boşluklar → yılan (strafe) → aşağı merdiven + uzun atlayış → buz pisti → sütunlar
## → yana kayan platformlar → yukarı merdiven → final uzun atlayış → bitiş. Altın plaka = kontrol noktası.

var z := 0.0
var y := 0.0
var kn_sayac := 0
var toplam_kn := 9
var blok_beyaz: ShaderMaterial
var blok_gri: ShaderMaterial
var blok_altin: StandardMaterial3D
var blok_buz: StandardMaterial3D
var blok_slime: StandardMaterial3D
var blok_kirmizi: ShaderMaterial
var asama_renkleri: Array[ShaderMaterial] = []


func _ready() -> void:
	_malzemeler()
	_blok_malzemeleri()
	_ortam_bhop()
	_kurs()


func _blok_malzemeleri() -> void:
	blok_beyaz = _blok(Color(0.92, 0.92, 0.9))
	blok_gri = _blok(Color(0.6, 0.6, 0.62))
	blok_kirmizi = _blok(Color(0.8, 0.15, 0.12))
	for c in [Color(0.35, 0.65, 0.95), Color(0.5, 0.8, 0.25), Color(0.95, 0.55, 0.15), Color(0.75, 0.35, 0.85),
			Color(0.95, 0.85, 0.2), Color(0.2, 0.7, 0.7), Color(0.9, 0.4, 0.6), Color(0.45, 0.5, 0.95)]:
		asama_renkleri.append(_blok(c))
	blok_altin = _std(Color(1.0, 0.8, 0.15), 0.35, Color(1.0, 0.7, 0.1), 1.2)
	blok_altin.metallic = 0.6
	blok_buz = _std(Color(0.7, 0.88, 1.0, 0.85), 0.05, Color.BLACK, 1.0, true)
	blok_buz.metallic = 0.2
	blok_slime = _std(Color(0.45, 0.85, 0.35, 0.8), 0.3, Color(0.3, 0.8, 0.2), 0.6, true)


func _blok(renk: Color) -> ShaderMaterial:
	return _panel(renk, renk * 0.55, 1.0, 0.85, 0.03, 0.03)


func _ortam_bhop() -> void:
	var env := Environment.new()
	var sky := Sky.new()
	var sm := ProceduralSkyMaterial.new()
	sm.sky_top_color = Color(0.3, 0.55, 1.0)
	sm.sky_horizon_color = Color(0.75, 0.85, 1.0)
	sm.ground_bottom_color = Color(0.55, 0.65, 0.85)
	sm.ground_horizon_color = Color(0.75, 0.85, 1.0)
	sky.sky_material = sm
	env.background_mode = Environment.BG_SKY
	env.sky = sky
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = Color(0.85, 0.87, 0.92)
	env.ambient_light_energy = 0.9
	env.tonemap_mode = Environment.TONE_MAPPER_FILMIC
	env.tonemap_exposure = 1.0
	env.glow_enabled = true
	env.glow_intensity = 0.4
	env.glow_hdr_threshold = 1.2
	env.fog_enabled = true
	env.fog_light_color = Color(0.75, 0.85, 1.0)
	env.fog_density = 0.004
	env.ssao_enabled = true
	var we := WorldEnvironment.new()
	we.environment = env
	add_child(we)
	var gunes := DirectionalLight3D.new()
	gunes.rotation_degrees = Vector3(-55, 160, 0)
	gunes.light_energy = 1.4
	gunes.shadow_enabled = true
	gunes.directional_shadow_max_distance = 160.0
	add_child(gunes)


## Platform: üst yüzeyi y'de, x merkezli, z0'dan ileri (−z) d derinliğinde.
func plat(x: float, ust_y: float, z0: float, w: float, d: float, mat: Material, kayganlik := 0.6, kalin := 1.0) -> StaticBody3D:
	var sb := kutu(Vector3(x, ust_y - kalin * 0.5, z0 - d * 0.5), Vector3(w, kalin, d), mat)
	sb.set_meta("kayganlik", kayganlik)
	return sb


## Altın kontrol noktası plakası + aşama etiketi.
func kn(x: float, ust_y: float, zc: float, yaw := 0.0) -> void:
	kn_sayac += 1
	var n := kn_sayac
	gorsel(Vector3(x, ust_y + 0.03, zc), Vector3(2, 0.06, 2), blok_altin)
	var etiket := Label3D.new()
	etiket.text = "KN %d" % n
	etiket.font_size = 64
	etiket.pixel_size = 0.006
	etiket.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	etiket.modulate = Color(1.0, 0.85, 0.2)
	etiket.outline_size = 12
	etiket.position = Vector3(x, ust_y + 2.6, zc)
	add_child(etiket)
	var poz := Vector3(x, ust_y, zc)
	alan(Vector3(x, ust_y + 1.2, zc), Vector3(2.4, 2.4, 2.4), func() -> void:
		kontrol_noktasi.emit(poz, yaw)
		bilgi.emit("Kontrol noktası %d / %d" % [n, toplam_kn])
	)


func _kurs() -> void:
	olum_y = -60.0
	# 1) başlangıç platformu
	plat(0, 0, 4.5, 9, 9, blok_beyaz)
	baslangic = Vector3(0, 0.2, 2.5)
	kn(0, 0, 0)
	_etiket3d("BUNNY HOP KURSU\nShift sprint · Space basılı bhop · A/D + fare ile hız biriktir", Vector3(0, 3.5, -4.5))
	z = -4.5
	# 2) düz boşluklar: 3 → 5 blok
	var m := asama_renkleri[0]
	for g in [3.0, 3.5, 4.0, 4.5, 5.0]:
		z -= g
		plat(0, 0, z, 4, 4, m)
		z -= 4
	# 3) KN 2
	z -= 3.5
	plat(0, 0, z, 5, 5, blok_gri)
	kn(0, 0, z - 2.5)
	z -= 5
	# 4) yılan (strafe): sağ-sol dönüşümlü 3x3
	m = asama_renkleri[1]
	for i in 8:
		var x := 4.0 if i % 2 == 0 else -4.0
		z -= 3.0
		plat(x, 0, z, 3, 3, m)
		z -= 3
	# 5) KN 3
	z -= 3.5
	plat(0, 0, z, 5, 5, blok_gri)
	kn(0, 0, z - 2.5)
	z -= 5
	# 6) aşağı merdiven (hız kazan) + 9 blok uzun atlayış
	m = asama_renkleri[2]
	for i in 12:
		y -= 1.0
		plat(0, y, z, 3, 2.5, m, 0.6, 1.0)
		z -= 2.5
	plat(0, y, z, 4, 8, m)
	z -= 8
	z -= 9
	y -= 1.0
	# 7) KN 4
	plat(0, y, z, 6, 6, blok_gri)
	kn(0, y, z - 3)
	z -= 6
	# 8) buz pisti (kayganlık 0.98) + 8 blok boşluk
	z -= 2.5
	plat(0, y, z, 4, 24, blok_buz, 0.98)
	_etiket3d("BUZ: sürtünme yok, hız düşmez", Vector3(0, y + 2.5, z - 2))
	z -= 24
	z -= 8
	# 9) KN 5
	plat(0, y, z, 5, 5, blok_gri)
	kn(0, y, z - 2.5)
	z -= 5
	# 10) sütunlar 1x1, hafif yükselen
	m = asama_renkleri[3]
	for i in 8:
		z -= 3.0
		var x: float = [-1.0, 1.0, 0.0, -1.5, 1.5, 0.0, -1.0, 1.0][i]
		plat(x, y + (i % 3) * 0.5, z, 1, 1, m, 0.6, 1.0 + (i % 3) * 0.5)
		z -= 1
	# 11) KN 6
	z -= 3.0
	plat(0, y, z, 5, 5, blok_gri)
	kn(0, y, z - 2.5)
	z -= 5
	# 12) yana kayan platformlar (çapraz strafe): her biri +3 x
	m = asama_renkleri[4]
	var xk := 0.0
	for i in 6:
		xk += 3.0
		z -= 3.0
		plat(xk, y, z, 3, 3, m)
		z -= 3
	# 13) KN 7
	z -= 3.0
	plat(xk, y, z, 5, 5, blok_gri)
	kn(xk, y, z - 2.5)
	z -= 5
	# 14) yukarı merdiven: her 3 blokta 1 yukarı; slime (zıplatıcı) ile giriş
	m = asama_renkleri[5]
	z -= 3.0
	plat(xk, y, z, 3, 3, blok_slime).set_meta("ziplatici", true)
	z -= 3
	for i in 8:
		z -= 3.0
		y += 1.0
		plat(xk, y, z, 3, 3, m)
		z -= 3
	# 15) KN 8
	z -= 3.0
	plat(xk, y, z, 5, 5, blok_gri)
	kn(xk, y, z - 2.5)
	z -= 5
	# 16) final: 20 blok pist + 11 blok boşluk (zincir hızı ister)
	m = asama_renkleri[6]
	z -= 2.0
	plat(xk, y, z, 4, 20, m)
	_etiket3d("FİNAL: 11 blok, zincir hızı gerekir", Vector3(xk, y + 2.5, z - 3))
	gorsel(Vector3(xk, y + 0.03, z - 19.5), Vector3(4, 0.06, 1), blok_kirmizi)
	z -= 20
	z -= 11
	# 17) bitiş
	plat(xk, y, z, 9, 9, blok_beyaz)
	kn(xk, y, z - 2)
	gorsel(Vector3(xk, y + 0.03, z - 5.5), Vector3(3, 0.06, 3), blok_altin)
	_etiket3d("BİTİŞ", Vector3(xk, y + 3.5, z - 5.5))
	omni(Vector3(xk, y + 2, z - 5.5), 10, 2.0, Color(1.0, 0.85, 0.3))
	alan(Vector3(xk, y + 1.2, z - 5.5), Vector3(3, 2.4, 3), func() -> void: bitis.emit())
	z -= 9


func _etiket3d(metin: String, poz: Vector3) -> void:
	var l := Label3D.new()
	l.text = metin
	l.font_size = 48
	l.pixel_size = 0.006
	l.billboard = BaseMaterial3D.BILLBOARD_ENABLED
	l.outline_size = 10
	l.position = poz
	add_child(l)
