extends Node3D
## Portal silahı: bakış ışını → portal yerleştirme (yalnız "portal_yuzey" grubundaki yüzeyler),
## çift eşleme (Portal3D eklentisi), mermi görseli, portal arkasındaki duvar için çarpışma istisnası.

const PORTAL_SAHNE := preload("res://sahneler/portal.tscn")
const OVAL_SHADER := preload("res://shaderlar/portal_oval.gdshader")
const HALKA_SHADER := preload("res://shaderlar/portal_halka.gdshader")
const RENKLER: Array[Color] = [Color(0.25, 0.62, 1.0), Color(1.0, 0.52, 0.08)]
const PORTAL_BOYUT := Vector2(1.7, 2.5)
const ELLER_KATMAN := 1 << 18

class Yuva:
	var kok: Node3D
	var portal: Node3D
	var halka: MeshInstance3D
	var halka_mat: ShaderMaterial
	var yuzey: PhysicsBody3D
	var yerlesik := false
	var istisna := false

signal portal_yerlesti(i: int)
signal fizil(i: int)

var yuvalar: Array[Yuva] = []
var oyuncu: CharacterBody3D
var kamera: Camera3D
var istisna_sayac := {}
var hazir := false
var eller: Node3D


func _ready() -> void:
	oyuncu = owner as CharacterBody3D
	kamera = get_parent() as Camera3D
	eller = kamera.get_node_or_null("Eller")
	_kur.call_deferred()


func _kur() -> void:
	var sahne := get_tree().current_scene
	for i in 2:
		var y := Yuva.new()
		y.kok = Node3D.new()
		y.kok.name = "PortalYuva%d" % i
		y.portal = PORTAL_SAHNE.instantiate()
		y.portal.name = "Portal%d" % i
		y.kok.add_child(y.portal)
		var q := QuadMesh.new()
		q.size = PORTAL_BOYUT * 1.1
		y.halka = MeshInstance3D.new()
		y.halka.mesh = q
		y.halka_mat = ShaderMaterial.new()
		y.halka_mat.shader = HALKA_SHADER
		y.halka_mat.set_shader_parameter("renk", RENKLER[i])
		y.halka_mat.set_shader_parameter("dolu", true)
		y.halka.material_override = y.halka_mat
		y.halka.position = Vector3(0, 0, 0.012)
		y.halka.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
		y.kok.add_child(y.halka)
		y.kok.visible = false
		yuvalar.append(y)
	yuvalar[0].portal.set("exit_portal", yuvalar[1].portal)
	yuvalar[1].portal.set("exit_portal", yuvalar[0].portal)
	for i in 2:
		var y := yuvalar[i]
		sahne.add_child(y.kok)
		var pm: MeshInstance3D = y.portal.get("portal_mesh")
		var mat: ShaderMaterial = pm.material_override
		mat.shader = OVAL_SHADER
		mat.set_shader_parameter("halka_renk", RENKLER[i])
		y.portal.connect("on_teleport", _teleport_oldu.bind(i))
		var alan: Area3D = y.portal.get("teleport_area")
		alan.body_entered.connect(_alan_girdi.bind(i))
		alan.body_exited.connect(_alan_cikti.bind(i))
		alan.area_entered.connect(_alan_girdi.bind(i))
		alan.area_exited.connect(_alan_cikti.bind(i))
	hazir = true


func _oyuncu_mu(n: Node) -> bool:
	return n == oyuncu or n.get_parent() == oyuncu


func durum_metni() -> String:
	var s := ""
	for i in 2:
		var y := yuvalar[i]
		var vp: SubViewport = y.portal.get("portal_viewport")
		s += "[%d yerlesik=%s gorunur=%s/%s islem=%d viewport=%s dolu=%s istisna=%s] " % [
			i, y.yerlesik, y.kok.visible, y.portal.visible, y.portal.process_mode,
			(str(vp.size) + " mod=" + str(vp.render_target_update_mode)) if vp else "yok",
			y.halka_mat.get_shader_parameter("dolu"), y.istisna]
	return s


func _unhandled_input(event: InputEvent) -> void:
	if Input.mouse_mode != Input.MOUSE_MODE_CAPTURED:
		return
	if event.is_action_pressed("portal_mavi"):
		ates(0)
	elif event.is_action_pressed("portal_turuncu"):
		ates(1)


func _isin(from: Vector3, to: Vector3) -> Dictionary:
	var q := PhysicsRayQueryParameters3D.create(from, to, 1, [oyuncu.get_rid()])
	q.collide_with_areas = false
	return get_world_3d().direct_space_state.intersect_ray(q)


## Vuruş noktası etkin bir portalın ovali içindeyse o yuvanın indeksini döndürür, yoksa -1.
func _portal_icinde(nokta: Vector3, govde: Object) -> int:
	if not (yuvalar[0].yerlesik and yuvalar[1].yerlesik):
		return -1
	for i in 2:
		var y := yuvalar[i]
		if y.yuzey != govde:
			continue
		var lp := y.kok.global_transform.affine_inverse() * nokta
		var ex := lp.x / (PORTAL_BOYUT.x * 0.5)
		var ey := lp.y / (PORTAL_BOYUT.y * 0.5)
		if absf(lp.z) < 0.08 and ex * ex + ey * ey < 1.0:
			return i
	return -1


func ates(i: int) -> void:
	if not hazir:
		return
	var from := kamera.global_position
	var yon := -kamera.global_basis.z
	var hit := _isin(from, from + yon * 400.0)
	var ilk_hedef: Vector3 = hit.position if hit else from + yon * 400.0
	var gecis := _portal_icinde(hit.position, hit.collider) if hit else -1
	if gecis >= 0:
		var p: Node3D = yuvalar[gecis].portal
		var j := 1 - gecis
		var yeni_from: Vector3 = p.call("to_exit_position", hit.position) + yuvalar[j].kok.global_basis.z * 0.03
		var yeni_yon: Vector3 = p.call("to_exit_direction", yon)
		hit = _isin(yeni_from, yeni_from + yeni_yon * 400.0)
	if eller:
		eller.call("ates", RENKLER[i])
	Ses.cal("portal_ates", -6.0, 1.0 if i == 0 else 0.85)
	var namlu: Vector3 = kamera.global_transform * Vector3(0.24, -0.2, -0.45)
	var son := hit
	_mermi(namlu, ilk_hedef, RENKLER[i], func() -> void:
		if son:
			_yerlestir(i, son)
	)


func _mermi(from: Vector3, to: Vector3, renk: Color, bitti: Callable) -> void:
	var mi := MeshInstance3D.new()
	var s := SphereMesh.new()
	s.radius = 0.08
	s.height = 0.16
	mi.mesh = s
	var m := StandardMaterial3D.new()
	m.albedo_color = renk
	m.emission_enabled = true
	m.emission = renk
	m.emission_energy_multiplier = 4.0
	mi.material_override = m
	var isik := OmniLight3D.new()
	isik.light_color = renk
	isik.omni_range = 4.0
	isik.light_energy = 2.0
	mi.add_child(isik)
	get_tree().current_scene.add_child(mi)
	mi.global_position = from
	var sure: float = maxf(from.distance_to(to) / 90.0, 0.04)
	var tw := mi.create_tween()
	tw.tween_property(mi, "global_position", to, sure)
	tw.tween_callback(func() -> void:
		mi.queue_free()
		bitti.call()
	)


func _fizil(poz: Vector3, n: Vector3, renk: Color) -> void:
	Ses.cal("fizil", -8.0)
	var mi := MeshInstance3D.new()
	var s := SphereMesh.new()
	s.radius = 0.25
	s.height = 0.5
	mi.mesh = s
	var m := StandardMaterial3D.new()
	m.albedo_color = renk
	m.emission_enabled = true
	m.emission = renk
	m.emission_energy_multiplier = 3.0
	m.transparency = BaseMaterial3D.TRANSPARENCY_ALPHA
	mi.material_override = m
	get_tree().current_scene.add_child(mi)
	mi.global_position = poz + n * 0.1
	var tw := mi.create_tween()
	tw.tween_property(mi, "scale", Vector3.ONE * 0.05, 0.25)
	tw.tween_callback(mi.queue_free)


func _sigdir(govde: Node3D, poz: Vector3, b: Basis) -> Vector3:
	var cs: CollisionShape3D = null
	for c in govde.get_children():
		if c is CollisionShape3D and c.shape is BoxShape3D:
			cs = c
			break
	if cs == null:
		return poz
	var sh: BoxShape3D = cs.shape
	var yarim := sh.size * 0.5
	var t := cs.global_transform
	var lp := t.affine_inverse() * poz
	var binv := t.basis.inverse()
	var e: Vector3 = (binv * b.x).abs() * (PORTAL_BOYUT.x * 0.56) + (binv * b.y).abs() * (PORTAL_BOYUT.y * 0.56)
	var ln: Vector3 = (binv * b.z).abs()
	for k in 3:
		if ln[k] > 0.9:
			continue
		var lo: float = -yarim[k] + e[k]
		var hi: float = yarim[k] - e[k]
		if lo < hi:
			lp[k] = clampf(lp[k], lo, hi)
	return t * lp


func _yerlestir(i: int, hit: Dictionary) -> void:
	var govde: Object = hit.collider
	if not (govde is Node3D and govde.is_in_group("portal_yuzey")):
		_fizil(hit.position, hit.normal, RENKLER[i])
		fizil.emit(i)
		return
	var n: Vector3 = hit.normal.normalized()
	var up: Vector3
	if absf(n.y) < 0.7:
		up = Vector3.UP
	else:
		var bakis := -kamera.global_basis.z
		bakis.y = 0.0
		up = bakis.normalized() if bakis.length() > 0.05 else Vector3.FORWARD
		if n.y > 0.0:
			up = -up
	up = (up - n * up.dot(n)).normalized()
	var x := up.cross(n).normalized()
	var b := Basis(x, up, n)
	var poz := _sigdir(govde, hit.position + n * 0.012, b)
	var diger := yuvalar[1 - i]
	if diger.yerlesik and diger.kok.global_position.distance_to(poz) < 1.9:
		_fizil(hit.position, n, RENKLER[i])
		fizil.emit(i)
		return
	var y := yuvalar[i]
	_istisna_birak(y)
	y.yuzey = govde
	y.kok.global_transform = Transform3D(b, poz)
	y.kok.visible = true
	y.yerlesik = true
	_esle()
	portal_yerlesti.emit(i)


func _esle() -> void:
	var a := yuvalar[0]
	var bb := yuvalar[1]
	if a.yerlesik and bb.yerlesik:
		for y in yuvalar:
			y.portal.call("activate")
			y.halka_mat.set_shader_parameter("dolu", false)
			var pc: Camera3D = y.portal.get("portal_camera")
			if pc:
				pc.cull_mask = pc.cull_mask & ~ELLER_KATMAN
		for i in 2:
			var alan: Area3D = yuvalar[i].portal.get("teleport_area")
			for ar in alan.get_overlapping_areas():
				if _oyuncu_mu(ar):
					_istisna_al(yuvalar[i])
	else:
		for y in yuvalar:
			if y.yerlesik:
				y.portal.call("deactivate", false)
				y.halka_mat.set_shader_parameter("dolu", true)


func _istisna_al(y: Yuva) -> void:
	if y.istisna or y.yuzey == null:
		return
	y.istisna = true
	var id := y.yuzey.get_instance_id()
	istisna_sayac[id] = istisna_sayac.get(id, 0) + 1
	if istisna_sayac[id] == 1:
		oyuncu.add_collision_exception_with(y.yuzey)


func _istisna_birak(y: Yuva) -> void:
	if not y.istisna:
		return
	y.istisna = false
	if y.yuzey == null:
		return
	var id := y.yuzey.get_instance_id()
	var kalan: int = istisna_sayac.get(id, 1) - 1
	if kalan <= 0:
		istisna_sayac.erase(id)
		if is_instance_valid(y.yuzey):
			oyuncu.remove_collision_exception_with(y.yuzey)
	else:
		istisna_sayac[id] = kalan


func _alan_girdi(body: Node3D, i: int) -> void:
	if _oyuncu_mu(body) and yuvalar[0].yerlesik and yuvalar[1].yerlesik:
		_istisna_al(yuvalar[i])


func _alan_cikti(body: Node3D, i: int) -> void:
	if _oyuncu_mu(body):
		_istisna_birak(yuvalar[i])


func _teleport_oldu(node: Node3D, i: int) -> void:
	if node == oyuncu:
		_istisna_al(yuvalar[1 - i])


func yerlesik_mi(i: int) -> bool:
	return yuvalar.size() > i and yuvalar[i].yerlesik


func temizle() -> void:
	for y in yuvalar:
		_istisna_birak(y)
		y.yerlesik = false
		y.kok.visible = false
	_esle()
