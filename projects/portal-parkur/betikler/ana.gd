extends Node3D
## Ana sahne: seviye + oyuncu + HUD bağlantıları, düşme/yeniden doğma, bitiş, test koşumu.

const TEST := preload("res://betikler/test_kosum.gd")

@onready var oyuncu: Oyuncu = $Oyuncu
@onready var seviye: Node3D = $Seviye
@onready var hud: CanvasLayer = $HUD

var sure := 0.0
var bitti := false


func _ready() -> void:
	oyuncu.yeniden_dogum = seviye.baslangic
	oyuncu.yeniden_dogum_yaw = 0.0
	oyuncu.global_position = seviye.baslangic
	seviye.kontrol_noktasi.connect(_kontrol_noktasi)
	seviye.bitis.connect(_bitis)
	seviye.firlat.connect(_firlat)
	hud.mesaj("Portal x Parkur", 3.0)
	if OS.has_environment("PP_TEST"):
		var t := Node.new()
		t.set_script(TEST)
		t.name = "Test"
		add_child(t)


func _kontrol_noktasi(poz: Vector3, yaw: float) -> void:
	if oyuncu.yeniden_dogum.distance_to(poz) > 0.5:
		oyuncu.yeniden_dogum = poz
		oyuncu.yeniden_dogum_yaw = yaw
		hud.mesaj("Kontrol noktası", 1.2)


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
