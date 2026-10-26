extends CanvasLayer
## HUD: hız bulanıklığı (tam ekran), Portal 2 tarzı nişangah, hız/süre, durum (F3), mesaj.

const BULANIK := preload("res://shaderlar/hiz_bulanik.gdshader")

class Nisangah extends Control:
	var mavi := false
	var turuncu := false
	func _draw() -> void:
		var c := size * 0.5
		var r := 15.0
		draw_circle(c, 2.2, Color(1, 1, 1, 0.9))
		var km := Color(0.3, 0.65, 1.0, 1.0 if mavi else 0.45)
		var kt := Color(1.0, 0.55, 0.1, 1.0 if turuncu else 0.45)
		draw_arc(c, r, deg_to_rad(115), deg_to_rad(245), 24, km, 3.0 if mavi else 1.5, true)
		draw_arc(c, r, deg_to_rad(-65), deg_to_rad(65), 24, kt, 3.0 if turuncu else 1.5, true)

var bulanik: ColorRect
var bulanik_mat: ShaderMaterial
var nisangah: Nisangah
var hiz_lbl: Label
var sure_lbl: Label
var durum_lbl: Label
var mesaj_lbl: Label
var ipucu_lbl: Label
var mesaj_sure := 0.0
var hata_ayik := false
var bulanik_guc := 0.0


func _ready() -> void:
	bulanik = ColorRect.new()
	bulanik.set_anchors_preset(Control.PRESET_FULL_RECT)
	bulanik.mouse_filter = Control.MOUSE_FILTER_IGNORE
	bulanik_mat = ShaderMaterial.new()
	bulanik_mat.shader = BULANIK
	bulanik.material = bulanik_mat
	add_child(bulanik)

	nisangah = Nisangah.new()
	nisangah.set_anchors_preset(Control.PRESET_FULL_RECT)
	nisangah.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(nisangah)

	hiz_lbl = _etiket(Vector2(24, -70), 26, Control.PRESET_BOTTOM_LEFT)
	sure_lbl = _etiket(Vector2(-180, 20), 24, Control.PRESET_TOP_RIGHT)
	durum_lbl = _etiket(Vector2(24, 20), 16, Control.PRESET_TOP_LEFT)
	durum_lbl.visible = false
	mesaj_lbl = _etiket(Vector2(0, 120), 34, Control.PRESET_CENTER_TOP)
	mesaj_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	mesaj_lbl.modulate.a = 0.0
	ipucu_lbl = _etiket(Vector2(0, 0), 15, Control.PRESET_BOTTOM_WIDE)
	ipucu_lbl.text = "Sol tık mavi portal · Sağ tık turuncu · Boşluk zıpla/duvar · Shift koş · Ctrl kay · R yeniden · F3 durum"
	ipucu_lbl.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	ipucu_lbl.offset_left = 200
	ipucu_lbl.offset_right = -24
	ipucu_lbl.offset_top = -36
	ipucu_lbl.offset_bottom = -12
	ipucu_lbl.modulate.a = 0.7


func _etiket(ofs: Vector2, boyut: int, preset: int) -> Label:
	var l := Label.new()
	l.set_anchors_preset(preset)
	l.position = ofs
	l.add_theme_font_size_override("font_size", boyut)
	l.add_theme_color_override("font_outline_color", Color(0, 0, 0, 0.8))
	l.add_theme_constant_override("outline_size", 4)
	l.mouse_filter = Control.MOUSE_FILTER_IGNORE
	add_child(l)
	return l


func mesaj(m: String, sure := 2.0) -> void:
	mesaj_lbl.text = m
	mesaj_lbl.modulate.a = 1.0
	mesaj_sure = sure


func guncelle(oyuncu: Node, sure: float, delta: float) -> void:
	var v: Vector3 = oyuncu.velocity
	var hiz := Vector3(v.x, 0, v.z).length()
	hiz_lbl.text = "%4.1f m/s" % hiz
	sure_lbl.text = "%02d:%05.2f" % [int(sure / 60.0), fmod(sure, 60.0)]
	if Input.is_action_just_pressed("hata_ayik"):
		hata_ayik = not hata_ayik
		durum_lbl.visible = hata_ayik
	if hata_ayik:
		durum_lbl.text = "durum %s  momentum %.2f  v=(%.1f %.1f %.1f)  poz=(%.1f %.1f %.1f)  tp=%d  fps %d" % [
			oyuncu.DURUM_AD[oyuncu.durum], oyuncu.momentum, v.x, v.y, v.z,
			oyuncu.global_position.x, oyuncu.global_position.y, oyuncu.global_position.z,
			oyuncu.teleport_sayisi, Engine.get_frames_per_second()]
	var hedef: float = clampf((v.length() - 9.0) / 14.0, 0.0, 1.0) * 0.09
	bulanik_guc = lerpf(bulanik_guc, hedef, 6.0 * delta)
	bulanik_mat.set_shader_parameter("guc", bulanik_guc)
	bulanik_mat.set_shader_parameter("vinyet", 0.25 + bulanik_guc * 4.0)
	var ps: Node = oyuncu.portal_silahi
	var m: bool = ps.call("yerlesik_mi", 0)
	var t: bool = ps.call("yerlesik_mi", 1)
	if m != nisangah.mavi or t != nisangah.turuncu:
		nisangah.mavi = m
		nisangah.turuncu = t
		nisangah.queue_redraw()
	if mesaj_sure > 0.0:
		mesaj_sure -= delta
		if mesaj_sure <= 0.0:
			var tw := create_tween()
			tw.tween_property(mesaj_lbl, "modulate:a", 0.0, 0.6)
