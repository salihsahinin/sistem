extends Node3D
## Ana sahne: seviye + oyuncu + HUD bağlantıları, düşme/yeniden doğma, bitiş, test koşumu.

const TEST := preload("res://betikler/test_kosum.gd")
const SEVIYE_ME := preload("res://betikler/seviye.gd")
const SEVIYE_BHOP := preload("res://betikler/seviye_bhop.gd")

@onready var oyuncu: Oyuncu = $Oyuncu
@onready var hud: CanvasLayer = $HUD
var seviye: Node3D

var sure := 0.0
var bitti := false


func _ready() -> void:
	# seviye seçimi: F4 `seviye` 0 = bhop kursu, 1 = çatı + portal odaları; test koşumu eski haritayı kullanır
	var bhop_kursu: bool = Ayarlar.al("seviye") < 0.5 and not OS.has_environment("PP_TEST")
	seviye = Node3D.new()
	seviye.name = "Seviye"
	seviye.set_script(SEVIYE_BHOP if bhop_kursu else SEVIYE_ME)
	add_child(seviye)
	move_child(seviye, 0)
	oyuncu.yeniden_dogum = seviye.baslangic
	oyuncu.yeniden_dogum_yaw = 0.0
	oyuncu.global_position = seviye.baslangic
	seviye.kontrol_noktasi.connect(_kontrol_noktasi)
	seviye.bitis.connect(_bitis)
	seviye.firlat.connect(_firlat)
	seviye.bilgi.connect(func(m: String) -> void: hud.mesaj(m, 1.5))
	hud.mesaj("Bunny Hop Kursu" if bhop_kursu else "Portal x Parkur", 3.0)
	if OS.has_environment("PP_EKRAN"):
		_ekran_al.call_deferred()
	if OS.has_environment("PP_TEST"):
		var t := Node.new()
		t.set_script(TEST)
		t.name = "Test"
		add_child(t)


## PP_EKRAN=1: başlangıçtan ve kuş bakışı iki ekran görüntüsü alıp çıkar (görsel kontrol).
func _ekran_al() -> void:
	Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
	oyuncu.fare_acik = false
	var dizin := ProjectSettings.globalize_path("res://test_cikti/")
	await get_tree().create_timer(1.0).timeout
	oyuncu.kamera.rotation.x = deg_to_rad(-8)
	await RenderingServer.frame_post_draw
	get_viewport().get_texture().get_image().save_png(dizin + "bhop_01_baslangic.png")
	oyuncu.sifirla()
	oyuncu.global_position = Vector3(-10, 24, 20)
	oyuncu.rotation.y = deg_to_rad(-25)
	oyuncu.kamera.rotation.x = deg_to_rad(-28)
	oyuncu.set_physics_process(false)
	await get_tree().create_timer(0.5).timeout
	await RenderingServer.frame_post_draw
	get_viewport().get_texture().get_image().save_png(dizin + "bhop_02_kusbakisi.png")
	oyuncu.global_position = Vector3(6, 2, -150)
	oyuncu.rotation.y = deg_to_rad(10)
	oyuncu.kamera.rotation.x = deg_to_rad(-15)
	await get_tree().create_timer(0.5).timeout
	await RenderingServer.frame_post_draw
	get_viewport().get_texture().get_image().save_png(dizin + "bhop_03_orta.png")
	get_tree().quit()


func _kontrol_noktasi(poz: Vector3, yaw: float) -> void:
	if oyuncu.yeniden_dogum.distance_to(poz) > 0.5:
		oyuncu.yeniden_dogum = poz
		oyuncu.yeniden_dogum_yaw = yaw


func _firlat(v: Vector3) -> void:
	oyuncu.firlat(v)
	hud.mesaj("", 0.1)


func _bitis() -> void:
	if bitti:
		return
	bitti = true
	hud.mesaj("BİTİŞ  %02d:%05.2f" % [int(sure / 60.0), fmod(sure, 60.0)], 8.0)


func _process(delta: float) -> void:
	if not bitti:
		sure += delta
	if oyuncu.global_position.y < seviye.olum_y:
		oyuncu.yeniden_dogur()
		hud.mesaj("Düştün", 1.0)
	if Input.is_action_just_pressed("yeniden"):
		oyuncu.yeniden_dogur()
	hud.guncelle(oyuncu, sure, delta)
