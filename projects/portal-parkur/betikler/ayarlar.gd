extends Node
## Kamera/fare profili (Dying Light hissi için ayarlanabilir); user://ayarlar.cfg içinde saklanır.
## Değerler [?] kestirimdir; Dying Light ayar dosyaları (Belgeler\DyingLight\out\settings) okunursa güncellenir.

signal degisti

const YOL := "user://ayarlar.cfg"

## ad: [varsayılan, min, max, adım, açıklama]
const TANIM := {
	"hassasiyet": [0.12, 0.02, 0.60, 0.005, "derece / fare sayımı (yatay)"],
	"dikey_oran": [1.0, 0.5, 1.5, 0.05, "dikey / yatay hassasiyet oranı"],
	"yumusatma": [0.0, 0.0, 0.08, 0.005, "fare yumuşatma zaman sabiti (sn); 0 = ham 1:1"],
	"ters_y": [0.0, 0.0, 1.0, 1.0, "dikey ters (1 = açık)"],
	"fov": [68.0, 55.0, 100.0, 1.0, "görüş açısı (dikey derece)"],
	"sprint_fov": [12.0, 0.0, 30.0, 1.0, "sprintte görüş açısı artışı"],
	"kamera_atalet": [0.0, 0.0, 0.05, 0.001, "hızlı dönüşte kameranın gövdeyi geriden izlemesi (sn); 0 = yok"],
	"hava_donus": [120.0, 0.0, 720.0, 10.0, "havada hız yönünün bakışı izleme hızı (derece/sn); 0 = saf CS"],
	"bhop": [1.0, 0.0, 1.0, 1.0, "bunny hop (1): inişte zıplama basılıysa sürtünmesiz zıpla"],
	"bhop_tavan": [1.1, 0.2, 6.0, 0.1, "Source hava hız tavanı (m/s; CS 30 birim ≈ run hızının %12'si)"],
	"bhop_hava_ivme": [12.0, 1.0, 100.0, 1.0, "sv_airaccelerate (CS:GO 12, CS 1.6 10)"],
	"bhop_surtunme": [5.2, 0.0, 12.0, 0.1, "sv_friction (CS:GO 5.2, CS 1.6 4): yerde fazla hızın sönümü"],
	"bob": [1.0, 0.0, 2.0, 0.05, "baş sallanması çarpanı"],
	"egilme": [14.0, 0.0, 25.0, 1.0, "duvar koşusunda kamera eğimi (derece)"],
	"yan_egilme": [1.8, 0.0, 6.0, 0.1, "yana koşarken kamera eğimi (derece)"],
	"inis_dip": [1.0, 0.0, 2.0, 0.05, "iniş sarsıntısı çarpanı"],
}

var deger := {}


func _ready() -> void:
	for k in TANIM:
		deger[k] = TANIM[k][0]
	var cf := ConfigFile.new()
	if cf.load(YOL) == OK:
		for k in TANIM:
			deger[k] = float(cf.get_value("kamera", k, TANIM[k][0]))
	Input.use_accumulated_input = false


func al(k: String) -> float:
	return deger[k]


func ayarla(k: String, v: float) -> void:
	deger[k] = clampf(v, TANIM[k][1], TANIM[k][2])
	kaydet()
	degisti.emit()


func sifirla() -> void:
	for k in TANIM:
		deger[k] = TANIM[k][0]
	kaydet()
	degisti.emit()


func kaydet() -> void:
	var cf := ConfigFile.new()
	for k in TANIM:
		cf.set_value("kamera", k, deger[k])
	cf.save(YOL)
