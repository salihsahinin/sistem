extends Node3D
## Birinci şahıs kollar: beyaz kol, kırmızı eldiven (Mirror's Edge), sağ ön kolda bilek-tipi portal cihazı.
## Tüm parçalar primitiflerden kurulur; her karede dirsek→el çizgisi yeniden hizalanır.

const KATMAN := 1 << 18
const BEYAZ := Color(0.93, 0.93, 0.95)
const KIRMIZI := Color(0.85, 0.08, 0.06)
const TEN := Color(0.86, 0.62, 0.48)

class Kol:
	var kok: Node3D
	var on_kol: MeshInstance3D
	var el: Node3D
	var omuz := Vector3.ZERO
	var el_poz := Vector3.ZERO
	var el_hedef := Vector3.ZERO
	var el_rot := Vector3.ZERO
	var el_rot_hedef := Vector3.ZERO

var sag := Kol.new()
var sol := Kol.new()
var cihaz_halka: MeshInstance3D
var el_disk: MeshInstance3D
var halka_mat: StandardMaterial3D
var mod := "serbest"
var mod_suresi := 0.0
var taraf := 0
var faz := 0.0
var sway := Vector2.ZERO
var tepme := 0.0
var oyuncu: CharacterBody3D

const SAG_OMUZ := Vector3(0.40, -0.46, -0.10)
const SAG_EL := Vector3(0.27, -0.25, -0.52)
const SOL_OMUZ := Vector3(-0.40, -0.46, -0.10)
const SOL_EL := Vector3(-0.27, -0.25, -0.52)


func _ready() -> void:
	oyuncu = owner as CharacterBody3D
	_kol_kur(sag, SAG_OMUZ, SAG_EL, true)
	_kol_kur(sol, SOL_OMUZ, SOL_EL, false)


func _mat(renk: Color, puruz := 0.7, emis := Color.BLACK) -> StandardMaterial3D:
	var m := StandardMaterial3D.new()
	m.albedo_color = renk
	m.roughness = puruz
	if emis != Color.BLACK:
		m.emission_enabled = true
		m.emission = emis
		m.emission_energy_multiplier = 2.5
	return m


func _mesh(m: Mesh, mat: Material, parent: Node3D, poz := Vector3.ZERO, rot := Vector3.ZERO) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	mi.mesh = m
	mi.material_override = mat
	mi.layers = KATMAN
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	mi.position = poz
	mi.rotation = rot
	parent.add_child(mi)
	return mi


func _kol_kur(k: Kol, omuz: Vector3, el: Vector3, sag_mi: bool) -> void:
	k.omuz = omuz
	k.el_poz = el
	k.el_hedef = el
	k.kok = Node3D.new()
	add_child(k.kok)
	var kap := CapsuleMesh.new()
	kap.radius = 0.042
	kap.height = 0.5
	k.on_kol = _mesh(kap, _mat(BEYAZ, 0.75), k.kok)
	k.el = Node3D.new()
	k.kok.add_child(k.el)
	var bilek := CylinderMesh.new()
	bilek.top_radius = 0.05
	bilek.bottom_radius = 0.05
	bilek.height = 0.03
	_mesh(bilek, _mat(Color(0.1, 0.1, 0.1), 0.5), k.el, Vector3(0, 0, 0.04), Vector3(PI / 2, 0, 0))
	var avuc := BoxMesh.new()
	avuc.size = Vector3(0.085, 0.028, 0.10)
	_mesh(avuc, _mat(KIRMIZI, 0.8), k.el, Vector3(0, 0, -0.05))
	for i in 4:
		var p := BoxMesh.new()
		p.size = Vector3(0.016, 0.022, 0.065)
		var x := -0.03 + i * 0.02
		var parmak := _mesh(p, _mat(KIRMIZI, 0.8), k.el, Vector3(x, 0.0, -0.13), Vector3(-0.25, 0, 0))
		var uc := BoxMesh.new()
		uc.size = Vector3(0.015, 0.02, 0.02)
		_mesh(uc, _mat(TEN, 0.9), parmak, Vector3(0, 0, -0.04))
	var bas := BoxMesh.new()
	bas.size = Vector3(0.05, 0.022, 0.02)
	var bx := -0.055 if sag_mi else 0.055
	_mesh(bas, _mat(KIRMIZI, 0.8), k.el, Vector3(bx, 0.0, -0.06), Vector3(0, 0.5 * (1.0 if sag_mi else -1.0), 0))
	if sag_mi:
		var gov := CylinderMesh.new()
		gov.top_radius = 0.06
		gov.bottom_radius = 0.065
		gov.height = 0.14
		k.on_kol.add_child(_cihaz_parcasi(gov, _mat(BEYAZ, 0.4), Vector3(0, -0.02, 0)))
		halka_mat = _mat(Color(0.2, 0.2, 0.25), 0.3, Color(0.25, 0.65, 1.0))
		var tor := TorusMesh.new()
		tor.inner_radius = 0.058
		tor.outer_radius = 0.072
		cihaz_halka = _cihaz_parcasi(tor, halka_mat, Vector3(0, -0.02, 0))
		k.on_kol.add_child(cihaz_halka)
		var disk := CylinderMesh.new()
		disk.top_radius = 0.028
		disk.bottom_radius = 0.028
		disk.height = 0.012
		el_disk = _mesh(disk, halka_mat, k.el, Vector3(0, 0.02, -0.05))


func _cihaz_parcasi(m: Mesh, mat: Material, poz: Vector3) -> MeshInstance3D:
	var mi := MeshInstance3D.new()
	mi.mesh = m
	mi.material_override = mat
	mi.layers = KATMAN
	mi.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_OFF
	mi.position = poz
	return mi


func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseMotion:
		sway += event.relative * 0.00035


func _process(delta: float) -> void:
	mod_suresi += delta
	sway = sway.lerp(Vector2.ZERO, 8.0 * delta)
	tepme = lerpf(tepme, 0.0, 10.0 * delta)
	var hiz := 0.0
	var yerde := false
	if oyuncu:
		hiz = Vector3(oyuncu.velocity.x, 0, oyuncu.velocity.z).length()
		yerde = oyuncu.is_on_floor()
	faz += delta * (hiz * 1.55 if yerde and hiz > 1.0 else 0.0)

	var sag_ofs := Vector3.ZERO
	var sol_ofs := Vector3.ZERO
	var sag_rot := Vector3.ZERO
	var sol_rot := Vector3.ZERO
	match mod:
		"serbest":
			if yerde and hiz > 1.0:
				var g: float = clampf(hiz / 9.0, 0.3, 1.4) * 0.05
				sag_ofs = Vector3(0.0, sin(faz) * g * 0.6, -cos(faz) * g * 1.4)
				sol_ofs = Vector3(0.0, -sin(faz) * g * 0.6, cos(faz) * g * 1.4)
				sag_rot = Vector3(cos(faz) * 0.25, 0, 0)
				sol_rot = Vector3(-cos(faz) * 0.25, 0, 0)
			elif not yerde:
				var t: float = clampf(oyuncu.velocity.y / 8.0, -1.0, 1.0) if oyuncu else 0.0
				sag_ofs = Vector3(0.03, 0.06 + 0.05 * t, 0.02)
				sol_ofs = Vector3(-0.03, 0.06 + 0.05 * t, 0.02)
				sag_rot = Vector3(0.3, 0, 0.2)
				sol_rot = Vector3(0.3, 0, -0.2)
		"duvar_kosu":
			if taraf < 0:
				sol_ofs = Vector3(-0.22, 0.28, 0.02)
				sol_rot = Vector3(0.2, 1.1, 0.4)
				sag_ofs = Vector3(0.0, sin(faz) * 0.03, -cos(faz) * 0.05)
			else:
				sag_ofs = Vector3(0.22, 0.28, 0.02)
				sag_rot = Vector3(0.2, -1.1, -0.4)
				sol_ofs = Vector3(0.0, -sin(faz) * 0.03, cos(faz) * 0.05)
		"tirmanis":
			var f := mod_suresi * 9.0
			sag_ofs = Vector3(0.05, 0.42 + sin(f) * 0.08, -0.05)
			sol_ofs = Vector3(-0.05, 0.42 - sin(f) * 0.08, -0.05)
			sag_rot = Vector3(-0.7, 0, 0)
			sol_rot = Vector3(-0.7, 0, 0)
		"tirman":
			var t := clampf(mod_suresi / 0.35, 0.0, 1.0)
			var y: float = lerpf(0.35, -0.25, t)
			sag_ofs = Vector3(0.06, y, -0.08)
			sol_ofs = Vector3(-0.06, y, -0.08)
			sag_rot = Vector3(-0.6 + t * 1.2, 0, 0)
			sol_rot = sag_rot
		"kayma":
			sag_ofs = Vector3(0.05, -0.08, 0.12)
			sol_ofs = Vector3(-0.08, 0.02, 0.0)
			sag_rot = Vector3(0.6, 0, 0.2)
			sol_rot = Vector3(0.2, 0.6, -0.3)
		"inis":
			var t := clampf(mod_suresi / 0.35, 0.0, 1.0)
			var d: float = (1.0 - t) * 0.22
			sag_ofs = Vector3(0.0, -d, -0.05)
			sol_ofs = Vector3(0.0, -d, -0.05)
			if t >= 1.0:
				mod = "serbest"
		"yuvarlan":
			var t := clampf(mod_suresi / 0.5, 0.0, 1.0)
			var a := sin(t * PI)
			sag_ofs = Vector3(0.1 * a, -0.3 * a, -0.1 * a)
			sol_ofs = Vector3(-0.1 * a, -0.3 * a, -0.1 * a)
			if t >= 1.0:
				mod = "serbest"
		"zipla":
			var t := clampf(mod_suresi / 0.3, 0.0, 1.0)
			var a := sin(t * PI)
			sag_ofs = Vector3(0.02, 0.10 * a, 0.03 * a)
			sol_ofs = Vector3(-0.02, 0.10 * a, 0.03 * a)
			if t >= 1.0:
				mod = "serbest"
	var sw := Vector3(-sway.x * 0.6, sway.y * 0.6, 0.0)
	sag.el_hedef = SAG_EL + sag_ofs + sw + Vector3(0.0, 0.01, 0.07) * tepme
	sol.el_hedef = SOL_EL + sol_ofs + sw
	sag.el_rot_hedef = sag_rot + Vector3(-0.5 * tepme, 0, 0)
	sol.el_rot_hedef = sol_rot
	_kol_guncelle(sag, delta)
	_kol_guncelle(sol, delta)


func _kol_guncelle(k: Kol, delta: float) -> void:
	k.el_poz = k.el_poz.lerp(k.el_hedef, 14.0 * delta)
	k.el_rot = k.el_rot.lerp(k.el_rot_hedef, 12.0 * delta)
	var yon := k.el_poz - k.omuz
	var uz := yon.length()
	if uz < 0.001:
		return
	var b := Basis.looking_at(yon.normalized(), Vector3.UP) * Basis(Vector3.RIGHT, -PI / 2)
	var kap: CapsuleMesh = k.on_kol.mesh
	kap.height = uz + 0.08
	k.on_kol.transform = Transform3D(b, k.omuz + yon * 0.5)
	var el_b := Basis.looking_at(yon.normalized(), Vector3.UP) * Basis.from_euler(k.el_rot)
	k.el.transform = Transform3D(el_b, k.el_poz)


func _mod(ad: String) -> void:
	mod = ad
	mod_suresi = 0.0

func serbest() -> void: _mod("serbest")
func zipla() -> void: _mod("zipla")
func duvar_kosu(t: int) -> void:
	taraf = t
	_mod("duvar_kosu")
func tirmanis() -> void: _mod("tirmanis")
func tirman(_sure: float) -> void: _mod("tirman")
func kayma() -> void: _mod("kayma")
func inis(_siddet: float) -> void: _mod("inis")
func yuvarlan() -> void: _mod("yuvarlan")

func ates(renk: Color) -> void:
	tepme = 1.0
	if halka_mat:
		halka_mat.emission = renk
