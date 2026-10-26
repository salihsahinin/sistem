extends Node3D
## Seviye: Mirror's Edge beyaz çatılar → Aperture tarzı test odaları. Tüm geometri kodla kurulur.

signal kontrol_noktasi(poz: Vector3, yaw: float)
signal bitis
signal firlat(v: Vector3)

const PANEL := preload("res://shaderlar/panel.gdshader")

var baslangic := Vector3(0, 0.3, 9)
var olum_y := -17.0

var beyaz: ShaderMaterial
var koyu: ShaderMaterial
var cephe: ShaderMaterial
var cephe_koyu: ShaderMaterial
var cati: StandardMaterial3D
var kirmizi: StandardMaterial3D
var cam: StandardMaterial3D
var isik: StandardMaterial3D
var kopru: StandardMaterial3D
var zemin_gri: StandardMaterial3D
var turuncu_mat: StandardMaterial3D


func _ready() -> void:
	_malzemeler()
	_ortam()
	_sehir()
	_catilar()
	_koridor_1()
	_oda_1()
	_koridor_2()
	_oda_2()


# ---------------- yardımcılar ----------------
func _panel(taban: Color, derz: Color, boyut: float, puruz := 0.55, derz_g := 0.025, pah := 0.06) -> ShaderMaterial:
	var m := ShaderMaterial.new()
	m.shader = PANEL
	m.set_shader_parameter("taban", taban)
	m.set_shader_parameter("derz", derz)
	m.set_shader_parameter("boyut", boyut)
	m.set_shader_parameter("puruz", puruz)
	m.set_shader_parameter("derz_genislik", derz_g)
	m.set_shader_parameter("pah", pah)
	return m


func _std(renk: Color, puruz := 0.8, emis := Color.BLACK, emis_guc := 1.0, saydam := false) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	m.albedo_color = renk
	m.roughness = puruz
	if emis != Color.BLACK:
		m.emission_enabled = true
		m.emission = emis
		m.emission_energy_multiplier = emis_guc
	if saydam:
		m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
		m.cull_mode = BaseMaterial3D.CULL_DISABLED
	return m


func _malzemeler() -> void:
	beyaz = _panel(Color(0.93, 0.93, 0.91), Color(0.58, 0.58, 0.56), 1.0, 0.5)
	koyu = _panel(Color(0.21, 0.21, 0.22), Color(0.07, 0.07, 0.08), 0.5, 0.4, 0.02, 0.04)
	cephe = _panel(Color(0.90, 0.91, 0.93), Color(0.52, 0.58, 0.68), 3.0, 0.45, 0.14, 0.35)
	cephe_koyu = _panel(Color(0.75, 0.77, 0.80), Color(0.35, 0.40, 0.48), 2.5, 0.45, 0.12, 0.3)
	cati = _std(Color(0.96, 0.96, 0.95), 0.9)
	kirmizi = _std(Color(0.86, 0.07, 0.05), 0.55)
	cam = _std(Color(0.55, 0.75, 1.0, 0.35), 0.1, Color.BLACK, 1.0, true)
	cam.metallic = 0.3
	isik = _std(Color(1, 1, 1), 0.5, Color(1.0, 0.98, 0.92), 4.0)
	kopru = _std(Color(0.35, 0.65, 1.0, 0.45), 0.2, Color(0.25, 0.55, 1.0), 2.0, true)
	zemin_gri = _std(Color(0.45, 0.47, 0.5), 0.95)
	turuncu_mat = _std(Color(1.0, 0.5, 0.1), 0.5, Color(1.0, 0.45, 0.05), 1.5)


func kutu(poz: Vector3, boyut: Vector3, mat: Material, portal := false, ad := "") -> StaticBody3D:
	var sb := StaticBody3D.new()
	if ad != "":
		sb.name = ad
	sb.collision_layer = 1
	sb.collision_mask = 0
	var cs := CollisionShape3D.new()
	var sh := BoxShape3D.new()
	sh.size = boyut
	cs.shape = sh
	sb.add_child(cs)
	var mi := MeshInstance3D.new()
	var m := BoxMesh.new()
	m.size = boyut
	mi.mesh = m
	mi.material_override = mat
	sb.add_child(mi)
	sb.position = poz
	if portal:
		sb.add_to_group("portal_yuzey")
	add_child(sb)
	return sb


## Delikli zemin: kutu (merkez, boyut) z-bantlarına bölünür; her delik Rect2(x0, z0, genişlik, derinlik) dünya xz.
func zemin_delikli(merkez: Vector3, boyut: Vector3, delikler: Array, mat: Material) -> void:
	var x0 := merkez.x - boyut.x * 0.5
	var x1 := merkez.x + boyut.x * 0.5
	var z0 := merkez.z - boyut.z * 0.5
	var z1 := merkez.z + boyut.z * 0.5
	var sirali := delikler.duplicate()
	sirali.sort_custom(func(a: Rect2, b: Rect2) -> bool: return a.position.y < b.position.y)
	var zc := z0
	for d: Rect2 in sirali:
		var dz0 := d.position.y
		var dz1 := d.position.y + d.size.y
		if dz0 > zc:
			kutu(Vector3(merkez.x, merkez.y, (zc + dz0) * 0.5), Vector3(boyut.x, boyut.y, dz0 - zc), mat)
		var dx0 := d.position.x
		var dx1 := d.position.x + d.size.x
		if dx0 > x0:
			kutu(Vector3((x0 + dx0) * 0.5, merkez.y, (dz0 + dz1) * 0.5), Vector3(dx0 - x0, boyut.y, dz1 - dz0), mat)
		if x1 > dx1:
			kutu(Vector3((dx1 + x1) * 0.5, merkez.y, (dz0 + dz1) * 0.5), Vector3(x1 - dx1, boyut.y, dz1 - dz0), mat)
		zc = dz1
	if z1 > zc:
		kutu(Vector3(merkez.x, merkez.y, (zc + z1) * 0.5), Vector3(boyut.x, boyut.y, z1 - zc), mat)


func gorsel(poz: Vector3, boyut: Vector3, mat: Material) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	var m := BoxMesh.new()
	m.size = boyut
	mi.mesh = m
	mi.material_override = mat
	mi.position = poz
	add_child(mi)
	return mi


func silindir(poz: Vector3, r: float, uzunluk: float, eksen: Vector3, mat: Material) -> StaticBody3D:
	var sb := StaticBody3D.new()
	sb.collision_layer = 1
	var cs := CollisionShape3D.new()
	var sh := CylinderShape3D.new()
	sh.radius = r
	sh.height = uzunluk
	cs.shape = sh
	sb.add_child(cs)
	var mi := MeshInstance3D.new()
	var m := CylinderMesh.new()
	m.top_radius = r
	m.bottom_radius = r
	m.height = uzunluk
	mi.mesh = m
	mi.material_override = mat
	sb.add_child(mi)
	sb.position = poz
	if eksen.is_equal_approx(Vector3.RIGHT):
		sb.rotation.z = PI / 2
	elif eksen.is_equal_approx(Vector3.FORWARD):
		sb.rotation.x = PI / 2
	add_child(sb)
	return sb


func alan(poz: Vector3, boyut: Vector3, cb: Callable) -> Area3D:
	var a := Area3D.new()
	a.collision_layer = 0
	a.collision_mask = 2
	var cs := CollisionShape3D.new()
	var sh := BoxShape3D.new()
	sh.size = boyut
	cs.shape = sh
	a.add_child(cs)
	a.position = poz
	a.body_entered.connect(func(b: Node3D) -> void:
		if b is CharacterBody3D:
			cb.call()
	)
	add_child(a)
	return a


func kontrol(poz: Vector3, yaw := 0.0) -> void:
	alan(poz + Vector3(0, 1.5, 0), Vector3(6, 3, 2), func() -> void: kontrol_noktasi.emit(poz, yaw))


func omni(poz: Vector3, menzil := 25.0, enerji := 2.5, renk := Color(1, 0.98, 0.95)) -> OmniLight3D:
	var l := OmniLight3D.new()
	l.position = poz
	l.omni_range = menzil
	l.light_energy = enerji
	l.light_color = renk
	l.shadow_enabled = false
	add_child(l)
	return l


func isik_seridi(poz: Vector3, boyut: Vector3) -> void:
	gorsel(poz, boyut, isik)


# ---------------- ortam ----------------
func _ortam() -> void:
	var env := Environment.new()
	var sky := Sky.new()
	var sm := ProceduralSkyMaterial.new()
	sm.sky_top_color = Color(0.18, 0.42, 0.92)
	sm.sky_horizon_color = Color(0.72, 0.84, 1.0)
	sm.ground_bottom_color = Color(0.35, 0.37, 0.4)
	sm.ground_horizon_color = Color(0.72, 0.8, 0.9)
	sm.sun_angle_max = 20.0
	sm.sun_curve = 0.2
	sky.sky_material = sm
	env.background_mode = Environment.BG_SKY
	env.sky = sky
	env.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	env.ambient_light_color = Color(0.8, 0.8, 0.8)
	env.ambient_light_sky_contribution = 0.1
	env.ambient_light_energy = 0.9
	env.tonemap_mode = Environment.TONE_MAPPER_FILMIC
	env.tonemap_exposure = 1.05
	env.tonemap_white = 6.0
	env.glow_enabled = true
	env.glow_intensity = 0.55
	env.glow_bloom = 0.08
	env.glow_hdr_threshold = 1.15
	env.ssao_enabled = true
	env.ssao_radius = 1.5
	env.ssao_intensity = 2.0
	env.adjustment_enabled = true
	env.adjustment_contrast = 1.08
	env.adjustment_saturation = 1.05
	var we := WorldEnvironment.new()
	we.environment = env
	add_child(we)
	var gunes := DirectionalLight3D.new()
	gunes.rotation_degrees = Vector3(-66, 150, 0)
	gunes.light_energy = 1.5
	gunes.light_color = Color(1.0, 0.97, 0.9)
	gunes.shadow_enabled = true
	gunes.directional_shadow_max_distance = 220.0
	gunes.directional_shadow_mode = DirectionalLight3D.SHADOW_PARALLEL_4_SPLITS
	add_child(gunes)


# ---------------- şehir silueti ----------------
func _sehir() -> void:
	kutu(Vector3(0, -40.5, -70), Vector3(900, 1, 900), zemin_gri)
	var rng := RandomNumberGenerator.new()
	rng.seed = 20261026
	var n := 0
	while n < 110:
		var x := rng.randf_range(-320, 320)
		var z := rng.randf_range(-360, 240)
		if absf(x) < 22 and z > -180 and z < 24:
			continue
		var w := rng.randf_range(10, 34)
		var d := rng.randf_range(10, 34)
		var uzak := Vector2(x, z).length()
		var h: float = minf(rng.randf_range(14, 50) + uzak * rng.randf_range(0.05, 0.3), 12.0 + uzak * 0.28)
		var mat := cephe if rng.randf() < 0.75 else cephe_koyu
		kutu(Vector3(x, -40 + h * 0.5, z), Vector3(w, h, d), mat)
		gorsel(Vector3(x, -40 + h + 0.05, z), Vector3(w, 0.1, d), cati)
		if rng.randf() < 0.3:
			gorsel(Vector3(x, -40 + h + 1.5, z), Vector3(w * 0.3, 3, d * 0.3), cati)
		n += 1


# ---------------- çatılar (Mirror's Edge) ----------------
func _bina(merkez_xz: Vector2, boyut_xz: Vector2, ust_y: float, yuk := 30.0) -> void:
	kutu(Vector3(merkez_xz.x, ust_y - yuk * 0.5, merkez_xz.y), Vector3(boyut_xz.x, yuk, boyut_xz.y), cephe)
	kutu(Vector3(merkez_xz.x, ust_y + 0.05, merkez_xz.y), Vector3(boyut_xz.x, 0.1, boyut_xz.y), cati)


func _parapet(merkez_xz: Vector2, boyut_xz: Vector2, ust_y: float, acik_kenar := "") -> void:
	var hx := boyut_xz.x * 0.5
	var hz := boyut_xz.y * 0.5
	var y := ust_y + 0.3
	if acik_kenar != "kuzey":
		kutu(Vector3(merkez_xz.x, y, merkez_xz.y - hz + 0.15), Vector3(boyut_xz.x, 0.6, 0.3), cati)
	if acik_kenar != "guney":
		kutu(Vector3(merkez_xz.x, y, merkez_xz.y + hz - 0.15), Vector3(boyut_xz.x, 0.6, 0.3), cati)
	if acik_kenar != "bati":
		kutu(Vector3(merkez_xz.x - hx + 0.15, y, merkez_xz.y), Vector3(0.3, 0.6, boyut_xz.y), cati)
	if acik_kenar != "dogu":
		kutu(Vector3(merkez_xz.x + hx - 0.15, y, merkez_xz.y), Vector3(0.3, 0.6, boyut_xz.y), cati)


func _catilar() -> void:
	# Çatı A (başlangıç): z -12..12, üst y=0
	_bina(Vector2(0, 0), Vector2(24, 24), 0.0)
	_parapet(Vector2(0, 0), Vector2(24, 24), 0.0, "kuzey")
	kutu(Vector3(-6, 0.65, -3), Vector3(1.6, 1.3, 1.6), cati)
	kutu(Vector3(5.5, 0.65, 2), Vector3(1.6, 1.3, 1.6), cati)
	kutu(Vector3(-3, 0.5, 6), Vector3(2.2, 1.0, 1.2), kirmizi)
	kutu(Vector3(4, 0.2, -6), Vector3(3, 0.4, 3), cam)
	silindir(Vector3(0, 0.25, -9.5), 0.14, 20.0, Vector3.RIGHT, kirmizi)
	kutu(Vector3(-9, 2.0, -11.5), Vector3(4, 4, 0.5), kirmizi)
	# Çatı B: z -37..-17, üst y=-1 (5 m boşluk)
	_bina(Vector2(0, -27), Vector2(20, 20), -1.0)
	_parapet(Vector2(0, -27), Vector2(20, 20), -1.0, "guney")
	kutu(Vector3(0, -0.45, -24), Vector3(7, 1.1, 0.4), cati)
	kutu(Vector3(6, -0.35, -30), Vector3(1.6, 1.3, 1.6), cati)
	kontrol(Vector3(0, -1, -20))
	# Duvar koşusu panosu (sol tarafta), B→C 8 m boşluğu üstünde
	kutu(Vector3(-4.5, 1.0, -41), Vector3(0.4, 4.0, 13), cati, false, "Pano")
	gorsel(Vector3(-4.28, 1.6, -41), Vector3(0.02, 1.2, 10), kirmizi)
	# Çatı C: z -65..-45, üst y=-1
	_bina(Vector2(0, -55), Vector2(20, 20), -1.0)
	_parapet(Vector2(0, -55), Vector2(20, 20), -1.0, "kuzey")
	kontrol(Vector3(-3, -1, -47))
	kutu(Vector3(5, 0.5, -52), Vector3(6, 3, 6), cati)
	kutu(Vector3(-6, -0.3, -54), Vector3(1.6, 1.4, 1.6), cati)
	silindir(Vector3(-8.5, 0.6, -55), 0.12, 20.0, Vector3.FORWARD, kirmizi)
	# Kapı yapısı (kırmızı çerçeve) → koridor
	kutu(Vector3(-3.0, 1.5, -63), Vector3(3.0, 5.0, 4.0), cati)
	kutu(Vector3(3.0, 1.5, -63), Vector3(3.0, 5.0, 4.0), cati)
	kutu(Vector3(0, 3.0, -63), Vector3(3.2, 2.0, 4.0), cati)
	kutu(Vector3(-1.65, 0.5, -61.2), Vector3(0.3, 3.0, 0.4), kirmizi)
	kutu(Vector3(1.65, 0.5, -61.2), Vector3(0.3, 3.0, 0.4), kirmizi)
	kutu(Vector3(0, 2.1, -61.2), Vector3(3.6, 0.3, 0.4), kirmizi)


# ---------------- koridor 1 (çatıdan odaya) ----------------
func _koridor_1() -> void:
	# iç: x -1.5..1.5, y -1..2, z -61..-80 ; zemin y=-1 (çatı C -65'e kadar, sonrası plaka)
	kutu(Vector3(0, -1.15, -72.5), Vector3(3.4, 0.3, 15), koyu)
	kutu(Vector3(-1.7, 0.5, -71), Vector3(0.4, 3.0, 18), koyu)
	kutu(Vector3(1.7, 0.5, -71), Vector3(0.4, 3.0, 18), koyu)
	kutu(Vector3(0, 2.15, -72), Vector3(3.8, 0.3, 20), koyu)
	for z in [-66.0, -70.0, -74.0, -78.0]:
		isik_seridi(Vector3(0, 1.95, z), Vector3(0.6, 0.05, 2.5))
	omni(Vector3(0, 1.2, -68), 10, 1.4)
	omni(Vector3(0, 1.2, -76), 10, 1.4)
	kontrol(Vector3(0, -1, -66))


# ---------------- oda 1 (Aperture) ----------------
func _oda_1() -> void:
	# iç: x -10..10, z -80..-116, zemin y=-9, tavan y=2
	# zemin: yakın (z -80..-96) ve uzak (z -104..-116); arada çukur
	zemin_delikli(Vector3(0, -9.25, -88), Vector3(20, 0.5, 16),
		[Rect2(-2.0, -83.5, 4.0, 3.0), Rect2(-1.6, -91.6, 3.2, 3.2)], koyu)
	zemin_delikli(Vector3(0, -9.25, -110), Vector3(20, 0.5, 12), [Rect2(-6.6, -111.6, 3.2, 3.2)], koyu)
	kutu(Vector3(0, -21, -100), Vector3(20, 1, 10), koyu)
	# çukur duvarları
	kutu(Vector3(0, -15.25, -96.25), Vector3(20, 12, 0.5), koyu)
	kutu(Vector3(0, -15.25, -103.75), Vector3(20, 12, 0.5), koyu)
	# yan duvarlar (beyaz, portal alır)
	kutu(Vector3(-10.25, -3.5, -98), Vector3(0.5, 11, 36), beyaz, true, "SolDuvar")
	kutu(Vector3(10.25, -3.5, -98), Vector3(0.5, 11, 36), beyaz, true, "SagDuvar")
	# uzak duvar (beyaz) kapı boşluklu
	kutu(Vector3(-5.75, -3.5, -116.25), Vector3(8.5, 11, 0.5), beyaz, true, "UzakSol")
	kutu(Vector3(5.75, -3.5, -116.25), Vector3(8.5, 11, 0.5), beyaz, true, "UzakSag")
	kutu(Vector3(0, -2, -116.25), Vector3(3, 8, 0.5), beyaz, true, "UzakUst")
	# yakın duvar (koyu), koridor ağzı y -1..2 x -1.5..1.5
	kutu(Vector3(0, -5, -79.75), Vector3(20, 8, 0.5), koyu)
	kutu(Vector3(-5.75, 0.5, -79.75), Vector3(8.5, 3, 0.5), koyu)
	kutu(Vector3(5.75, 0.5, -79.75), Vector3(8.5, 3, 0.5), koyu)
	# tavan
	kutu(Vector3(0, 2.25, -98), Vector3(20, 0.5, 36), koyu)
	for z in [-84.0, -92.0, -100.0, -108.0]:
		isik_seridi(Vector3(-4, 1.95, z), Vector3(1.0, 0.05, 5))
		isik_seridi(Vector3(4, 1.95, z), Vector3(1.0, 0.05, 5))
	omni(Vector3(0, -2, -88), 30, 3.0)
	omni(Vector3(0, -2, -110), 30, 3.0)
	# beyaz zemin pedi (portal alır) ve iniş pedi
	kutu(Vector3(0, -9.25, -90), Vector3(3.2, 0.5, 3.2), beyaz, true, "ZeminPedi")
	kutu(Vector3(0, -9.25, -82), Vector3(4, 0.5, 3), beyaz, true, "InisPedi")
	kutu(Vector3(-5, -9.25, -110), Vector3(3.2, 0.5, 3.2), beyaz, true, "UzakPed")
	# ışık köprüsü (sağ tarafta) çukur üstünde
	kutu(Vector3(7.5, -8.6, -95.4), Vector3(1.8, 0.8, 1.2), koyu)
	gorsel(Vector3(7.5, -8.1, -95.0), Vector3(1.4, 0.1, 0.1), isik)
	var k := kutu(Vector3(7.5, -8.05, -100), Vector3(1.6, 0.06, 10.4), kopru, false, "IsikKoprusu")
	k.get_child(1).cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	# gözlem penceresi (sol duvarda cam + ışık)
	gorsel(Vector3(-9.9, -3, -92), Vector3(0.1, 2.5, 6), cam)
	gorsel(Vector3(-10.0, -3, -92), Vector3(0.02, 2.4, 5.8), isik)
	kontrol(Vector3(0, -9, -86))
	kontrol(Vector3(0, -9, -108))


# ---------------- koridor 2 (pencereli) ----------------
func _koridor_2() -> void:
	# iç: x -1.5..1.5, y -9..-6, z -116..-136
	kutu(Vector3(0, -9.25, -126), Vector3(3.4, 0.5, 20), koyu)
	kutu(Vector3(-1.7, -7.5, -126), Vector3(0.4, 3.0, 20), koyu)
	kutu(Vector3(1.7, -7.5, -126), Vector3(0.4, 3.0, 20), koyu)
	kutu(Vector3(0, -5.85, -126), Vector3(3.8, 0.3, 20), koyu)
	for z in [-120.0, -126.0, -132.0]:
		gorsel(Vector3(-1.49, -7.3, z), Vector3(0.02, 1.0, 4), isik)
		gorsel(Vector3(1.49, -7.3, z), Vector3(0.02, 1.0, 4), isik)
		gorsel(Vector3(-1.45, -7.3, z), Vector3(0.02, 1.0, 4), cam)
		gorsel(Vector3(1.45, -7.3, z), Vector3(0.02, 1.0, 4), cam)
		isik_seridi(Vector3(0, -6.05, z), Vector3(0.6, 0.05, 3))
	omni(Vector3(0, -7, -122), 10, 1.5)
	omni(Vector3(0, -7, -130), 10, 1.5)
	kontrol(Vector3(0, -9, -118))
	# turuncu hız şeridi (itki jeli): üzerindeyken koşu hızı 1.5x
	gorsel(Vector3(0, -8.985, -127), Vector3(2.2, 0.03, 14), turuncu_mat)
	var serit := alan(Vector3(0, -8.4, -127), Vector3(2.6, 1.2, 14), func() -> void: pass)
	serit.body_entered.connect(func(b: Node3D) -> void:
		if b is CharacterBody3D:
			b.set("hiz_seridi", true)
	)
	serit.body_exited.connect(func(b: Node3D) -> void:
		if b is CharacterBody3D:
			b.set("hiz_seridi", false)
	)
	for z in [-121.0, -125.0, -129.0, -133.0]:
		omni(Vector3(0, -8.6, z), 4, 1.2, Color(1.0, 0.55, 0.15))


# ---------------- oda 2 (fırlatma plakası + bitiş) ----------------
func _oda_2() -> void:
	# iç: x -10..10, z -136..-166, zemin y=-9, tavan y=5
	kutu(Vector3(0, -9.25, -151), Vector3(20, 0.5, 30), koyu)
	kutu(Vector3(-10.25, -2, -151), Vector3(0.5, 14, 30), beyaz, true, "Oda2Sol")
	kutu(Vector3(10.25, -2, -151), Vector3(0.5, 14, 30), beyaz, true, "Oda2Sag")
	kutu(Vector3(0, -2, -166.25), Vector3(20, 14, 0.5), beyaz, true, "Oda2Uzak")
	kutu(Vector3(-5.75, -2, -135.75), Vector3(8.5, 14, 0.5), koyu)
	kutu(Vector3(5.75, -2, -135.75), Vector3(8.5, 14, 0.5), koyu)
	kutu(Vector3(0, 0.5, -135.75), Vector3(3, 9, 0.5), koyu)
	kutu(Vector3(0, 5.25, -151), Vector3(20, 0.5, 30), koyu)
	for z in [-140.0, -150.0, -160.0]:
		isik_seridi(Vector3(-5, 4.95, z), Vector3(1.0, 0.05, 6))
		isik_seridi(Vector3(5, 4.95, z), Vector3(1.0, 0.05, 6))
	omni(Vector3(0, 2, -143), 32, 3.0)
	omni(Vector3(0, 2, -158), 32, 3.0)
	# fırlatma plakası
	gorsel(Vector3(0, -8.985, -140), Vector3(2.2, 0.03, 2.2), koyu)
	gorsel(Vector3(0, -8.97, -140), Vector3(1.8, 0.03, 1.8), turuncu_mat)
	alan(Vector3(0, -8.3, -140), Vector3(2.0, 1.0, 2.0), func() -> void: firlat.emit(Vector3(0, 16.5, -10.0)))
	# üst platform
	kutu(Vector3(0, -3.25, -155), Vector3(9, 0.5, 9), koyu)
	kutu(Vector3(0, -3.25, -162), Vector3(5, 0.5, 5), beyaz, true, "BitisPedi")
	kontrol(Vector3(0, -3, -138))
	# bitiş: cam kabin + mavi ışık
	gorsel(Vector3(0, -1.5, -162), Vector3(3.2, 3.2, 3.2), cam)
	omni(Vector3(0, -1, -162), 8, 2.0, Color(0.3, 0.6, 1.0))
	alan(Vector3(0, -2, -162), Vector3(2.5, 2.5, 2.5), func() -> void: bitis.emit())
