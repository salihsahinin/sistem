class_name Oyuncu
extends CharacterBody3D
## Birinci şahıs parkur denetleyicisi: koşu-momentum, duvar koşusu, duvar tırmanışı,
## kenara tutunup çıkma (mantle), kayma, iniş; portal geçişinde hız/yön dönüşümü.

enum Durum { YERDE, HAVADA, DUVAR_KOSU, DUVAR_TIRMANIS, KAYMA, TIRMANMA }
const DURUM_AD := ["YERDE", "HAVADA", "DUVAR_KOSU", "DUVAR_TIRMANIS", "KAYMA", "TIRMANMA"]

@export var yurume_hizi := 5.5
@export var kosu_hizi := 9.0
@export var sprint_hizi := 12.5
@export var ziplama_hizi := 6.3
@export var yercekimi := 20.0
@export var fare_hassasiyet := 0.0022
@export var zemin_ivme := 16.0
@export var zemin_fren := 12.0
@export var hava_ivme := 3.5
@export var duvar_kosu_sure := 1.6
@export var duvar_kosu_hiz := 10.5
@export var duvar_tirmanis_sure := 0.8
@export var kayma_sure := 1.1
@export var temel_fov := 68.0

var durum: Durum = Durum.HAVADA
var durum_suresi := 0.0
var momentum := 0.0
var duvar_normal := Vector3.ZERO
var duvar_yon := Vector3.ZERO
var duvar_taraf := 0
var son_duvar_id := 0
var son_duvar_zaman := -10.0
var coyote := 0.0
var zipla_tampon := 0.0
var dusme_hizi := 0.0
var kafa_hedef_y := 1.6
var inis_dip := 0.0
var bob_faz := 0.0
var girdi := Vector2.ZERO
var toplam_sure := 0.0
var kilit := false
var yeniden_dogum := Vector3.ZERO
var yeniden_dogum_yaw := 0.0
var fare_acik := true
var son_teleport_zaman := -10.0
var teleport_sayisi := 0
## Test koşumu: klavye yerine bu vektör girdi sayılır (x: sağ+, y: geri+).
var sanal_girdi := Vector2.ZERO
var sanal_girdi_aktif := false
var sanal_zipla := false
var sanal_kay := false
var iz := false
var tirman_tw: Tween
var hiz_seridi := false
var cokuk := false
var son_adim_sayac := 0
var kayma_istek := 0.0
var son_shift := -10.0
var taktik_kalan := 0.0

# ---- Minecraft modeli (azalea-physics / LivingEntity.travel portu; birim blok/tick, 20 tick/sn) ----
const MC_TICK := 1.0 / 20.0
var mc_v := Vector3.ZERO
var mc_hareket := Vector3.ZERO
var mc_birikim := 0.0
var mc_senkron_gerek := true
var mc_yerde_tick := 0
var bhop_zincir := 0
var ucus_parkur := false
var firlat_kare := -10
var mc_zipla_gecikme := 0
var mc_sprint := false
var mc_son_kare := -10


func _mc_model() -> bool:
	return Ayarlar.al("model") > 0.5


func _mc_olcek() -> float:
	return 20.0 * Ayarlar.al("mc_olcek")


## blok/tick → m/s (yatay mc_olcek, dikey mc_olcek_y ile)
func _mc_ms(v: Vector3) -> Vector3:
	return Vector3(v.x * _mc_olcek(), v.y * 20.0 * Ayarlar.al("mc_olcek_y"), v.z * _mc_olcek())


func _mc_bt(v: Vector3) -> Vector3:
	return Vector3(v.x / _mc_olcek(), v.y / (20.0 * Ayarlar.al("mc_olcek_y")), v.z / _mc_olcek())


## Parkur durumlarından (duvar koşusu vb.) dönüşte Godot hızını tick durumuna aktarır.
func _mc_senkron() -> void:
	if mc_senkron_gerek or Engine.get_physics_frames() != mc_son_kare + 1:
		mc_senkron_gerek = false
		mc_v = _mc_bt(velocity)
		mc_hareket = mc_v
		mc_birikim = 0.0


## Bir Minecraft tick'i: aiStep (küçük hız sıfırlama, zıplama) + travel (girdi ivmesi, yerçekimi, atalet).
func _mc_tick(yerde: bool) -> bool:
	var zipladi := false
	if Vector2(mc_v.x, mc_v.z).length_squared() < 9.0e-6:
		mc_v.x = 0.0
		mc_v.z = 0.0
	if absf(mc_v.y) < 0.003:
		mc_v.y = 0.0
	var zipla_tut := zipla_tampon > 0.0 or (not sanal_girdi_aktif and Input.is_action_pressed("zipla"))
	var sprint_tut := Input.is_action_pressed("kos") or sanal_girdi_aktif
	var ileri_in := -girdi.y * 0.98
	var yan_in := girdi.x * 0.98
	if cokuk:
		ileri_in *= 0.3
		yan_in *= 0.3
	mc_sprint = sprint_tut and ileri_in > 0.5 and not cokuk
	var bhop := Ayarlar.al("bhop") > 0.5
	# aiStep: zıplama (vanilla: Space basılıyken 10 tick aralık; bhop: gecikmesiz, inişte hemen)
	if zipla_tut and yerde and (mc_zipla_gecikme == 0 or bhop):
		mc_v.y = maxf(0.42, mc_v.y)
		if mc_sprint:
			mc_v += ileri_yon() * 0.2
		if bhop:
			# zincir: inişten ≤2 tick sonra zıplandıysa bonus büyür, yoksa sıfırlanır
			bhop_zincir = bhop_zincir + 1 if mc_yerde_tick <= 2 else 0
			var carpan: float = 1.0 + Ayarlar.al("bhop_zincir_bonus") * minf(bhop_zincir, 15.0)
			var yatay_b := Vector2(mc_v.x, mc_v.z) * (carpan if bhop_zincir > 0 else 1.0)
			mc_v.x = yatay_b.x
			mc_v.z = yatay_b.y
		mc_zipla_gecikme = 10
		zipladi = true
	elif not zipla_tut:
		mc_zipla_gecikme = 0
	if mc_zipla_gecikme > 0:
		mc_zipla_gecikme -= 1
	mc_yerde_tick = mc_yerde_tick + 1 if yerde else 0
	# travel: moveRelative (yerde Minecraft; havada bhop açıksa Source AirAccelerate)
	var yerel := Vector3(yan_in, 0.0, -ileri_in)
	if yerel.length_squared() > 1.0e-7:
		if yerel.length_squared() > 1.0:
			yerel = yerel.normalized()
		var havada_bhop := bhop and (not yerde or zipladi)
		if havada_bhop:
			var olc := _mc_olcek()
			var wishdir: Vector3 = (global_basis * yerel)
			wishdir.y = 0.0
			if wishdir.length() > 0.01:
				wishdir = wishdir.normalized()
				var v_ms := Vector3(mc_v.x, 0.0, mc_v.z) * olc
				var wishspeed: float = (0.13 if mc_sprint else 0.1) / 0.454 * olc
				var mevcut := v_ms.dot(wishdir)
				var ekle: float = minf(wishspeed, Ayarlar.al("bhop_tavan") * Ayarlar.al("mc_olcek")) - mevcut
				if ekle > 0.0:
					v_ms += wishdir * minf(Ayarlar.al("bhop_hava_ivme") * wishspeed * MC_TICK, ekle)
				mc_v.x = v_ms.x / olc
				mc_v.z = v_ms.z / olc
		else:
			var hiz: float = (0.13 if mc_sprint else 0.1) if yerde else (0.026 if mc_sprint else 0.02)
			mc_v += (global_basis * yerel) * hiz
	# hareket bu (sürtünme öncesi) hızla yapılır; çarpışma move_and_slide ile tick'ler arasında
	mc_hareket = mc_v
	# sonra yerçekimi + atalet bir sonraki tick için (bhop: havada ve zıplama tick'inde sürtünme yok)
	mc_v.y -= 0.08
	var atalet: float = 0.546 if (yerde and not zipladi) else (1.0 if bhop else 0.91)
	mc_v.x *= atalet
	mc_v.z *= atalet
	mc_v.y *= 0.98
	return zipladi


## Tick birikimini işler, velocity'yi tick hızından kurar. Zıplama olduysa true.
func _mc_adim(delta: float, yerde: bool) -> bool:
	_mc_senkron()
	mc_birikim += delta
	var zipladi := false
	while mc_birikim >= MC_TICK:
		mc_birikim -= MC_TICK
		if _mc_tick(yerde):
			zipladi = true
			yerde = false
	velocity = _mc_ms(mc_hareket)
	return zipladi


## move_and_slide sonrası: kayan hız ve zemin/tavan teması tick durumuna geri yazılır.
func _mc_geri_oku() -> void:
	var v := _mc_bt(velocity)
	# yatay çarpışma: kayan hız hareket hızından saptıysa (duvar) o bileşen tick durumuna yazılır
	if absf(v.x - mc_hareket.x) > 1.0e-5:
		mc_v.x = v.x
		mc_hareket.x = v.x
	if absf(v.z - mc_hareket.z) > 1.0e-5:
		mc_v.z = v.z
		mc_hareket.z = v.z
	if is_on_floor() and mc_v.y < 0.0:
		mc_v.y = 0.0
		mc_hareket.y = minf(mc_hareket.y, 0.0)
	if is_on_ceiling() and mc_v.y > 0.0:
		mc_v.y = 0.0
		mc_hareket.y = 0.0
	mc_son_kare = Engine.get_physics_frames()

@onready var kafa: Node3D = $Kafa
@onready var kamera: Camera3D = $Kafa/Kamera
@onready var govde: CollisionShape3D = $Govde
@onready var govde_kisa: CollisionShape3D = $GovdeKisa
@onready var eller: Node3D = $Kafa/Kamera/Eller
@onready var portal_silahi: Node3D = $Kafa/Kamera/PortalSilahi
@onready var sol_isin: RayCast3D = $Isinlar/Sol
@onready var sag_isin: RayCast3D = $Isinlar/Sag
@onready var on_isin: RayCast3D = $Isinlar/On
@onready var diz_isin: RayCast3D = $Isinlar/Diz
@onready var ayak_isin: RayCast3D = $Isinlar/Ayak
@onready var tirmanma_ust: RayCast3D = $Isinlar/TirmanmaUst
@onready var tirmanma_orta: RayCast3D = $Isinlar/TirmanmaOrta
@onready var tirmanma_asagi: RayCast3D = $Isinlar/TirmanmaAsagi
@onready var tavan_isin: RayCast3D = $Isinlar/Tavan


func _ready() -> void:
	set_meta("teleport_root", ^".")
	if fare_acik:
		Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
	kamera.fov = temel_fov


## Fare: ham sayım birikir; _process içinde (yumuşatma 0 ise) 1:1 uygulanır.
var fare_birikim := Vector2.ZERO
var fare_hiz := Vector2.ZERO
var kamera_yaw_ofset := 0.0
var hedef_pitch := 0.0


func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseMotion and Input.mouse_mode == Input.MOUSE_MODE_CAPTURED:
		fare_birikim += event.relative
	elif event.is_action_pressed("cikis"):
		Input.mouse_mode = Input.MOUSE_MODE_VISIBLE if Input.mouse_mode == Input.MOUSE_MODE_CAPTURED else Input.MOUSE_MODE_CAPTURED
	elif event is InputEventMouseButton and event.pressed and Input.mouse_mode != Input.MOUSE_MODE_CAPTURED:
		Input.mouse_mode = Input.MOUSE_MODE_CAPTURED


func _process(delta: float) -> void:
	var d := fare_birikim
	fare_birikim = Vector2.ZERO
	var tau: float = Ayarlar.al("yumusatma")
	if tau > 0.0005:
		# üstel yumuşatma: bu karede uygulanan = birikenin bir kısmı (kare hızından bağımsız)
		fare_hiz += d
		var k: float = 1.0 - exp(-delta / tau)
		d = fare_hiz * k
		fare_hiz -= d
	var derece: float = Ayarlar.al("hassasiyet")
	var yaw_d := deg_to_rad(d.x * derece)
	var pitch_d := deg_to_rad(d.y * derece * Ayarlar.al("dikey_oran")) * (-1.0 if Ayarlar.al("ters_y") > 0.5 else 1.0)
	if yaw_d != 0.0:
		rotate_y(-yaw_d)
	kamera.rotation.x = clampf(kamera.rotation.x - pitch_d, deg_to_rad(-85), deg_to_rad(85))
	# kamera ataleti: hızlı dönüşte görüş gövdeyi kısa süre geriden izler
	var atalet: float = Ayarlar.al("kamera_atalet")
	if atalet > 0.0005:
		kamera_yaw_ofset = lerpf(kamera_yaw_ofset + yaw_d * 0.5, 0.0, clampf(delta / atalet, 0.0, 1.0))
	else:
		kamera_yaw_ofset = 0.0
	kamera.rotation.y = kamera_yaw_ofset


func yatay_hiz() -> Vector3:
	return Vector3(velocity.x, 0.0, velocity.z)


func ileri_yon() -> Vector3:
	var f := -global_basis.z
	f.y = 0.0
	return f.normalized() if f.length() > 0.001 else Vector3.FORWARD


func _kay_tiklandi() -> bool:
	if sanal_girdi_aktif:
		var k := sanal_kay
		sanal_kay = false
		return k
	return Input.is_action_just_pressed("kay")


func _zipla_basildi() -> bool:
	if sanal_girdi_aktif:
		var z := sanal_zipla
		sanal_zipla = false
		return z
	return Input.is_action_just_pressed("zipla")


func _physics_process(delta: float) -> void:
	toplam_sure += delta
	durum_suresi += delta
	if kilit:
		_kamera_guncelle(delta)
		return
	girdi = sanal_girdi if sanal_girdi_aktif else Input.get_vector("sol", "sag", "ileri", "geri")
	var yon := global_basis * Vector3(girdi.x, 0.0, girdi.y)
	yon.y = 0.0
	yon = yon.normalized() if yon.length() > 0.01 else Vector3.ZERO
	var ileri := ileri_yon()
	zipla_tampon = maxf(zipla_tampon - delta, 0.0)
	if _zipla_basildi():
		zipla_tampon = 0.15
	# auto-bhop (bunny sunucuları): Space basılı tutulunca her inişte zıpla
	if Ayarlar.al("bhop") > 0.5 and not sanal_girdi_aktif and Input.is_action_pressed("zipla"):
		zipla_tampon = maxf(zipla_tampon, 0.05)

	match durum:
		Durum.YERDE: _yerde(delta, yon, ileri)
		Durum.HAVADA: _havada(delta, yon, ileri)
		Durum.DUVAR_KOSU: _duvar_kosu(delta, yon, ileri)
		Durum.DUVAR_TIRMANIS: _duvar_tirmanis(delta, yon, ileri)
		Durum.KAYMA: _kayma(delta, yon, ileri)
		_: pass

	if not kilit:
		move_and_slide()
		if _mc_model() and (durum == Durum.YERDE or durum == Durum.HAVADA):
			_mc_geri_oku()
	_kamera_guncelle(delta)


func _durum_degistir(yeni: Durum) -> void:
	if durum == yeni:
		return
	durum = yeni
	durum_suresi = 0.0


# ---------------- YERDE ----------------
func _yerde(delta: float, yon: Vector3, ileri: Vector3) -> void:
	if not is_on_floor():
		coyote = 0.12
		_durum_degistir(Durum.HAVADA)
		return
	if _mc_model():
		_mc_yerde(delta, yon, ileri)
		return
	# MW2019 koşu modeli: W = jog · Shift = sprint (momentumla artar) · çift Shift = taktik sprint (4 sn)
	var kos := (Input.is_action_pressed("kos") or sanal_girdi_aktif) and girdi.y < -0.3
	if Input.is_action_just_pressed("kos") and not sanal_girdi_aktif:
		if toplam_sure - son_shift < 0.35:
			taktik_kalan = 4.0
		son_shift = toplam_sure
	if not kos:
		taktik_kalan = 0.0
	else:
		taktik_kalan = maxf(taktik_kalan - delta, 0.0)
	if yon == Vector3.ZERO or not kos:
		momentum = maxf(momentum - delta * 2.0, 0.0)
	else:
		momentum = clampf(momentum + delta * 0.6, 0.0, 1.0)
	var hedef_hiz: float = yurume_hizi
	if kos:
		hedef_hiz = lerpf(kosu_hizi, sprint_hizi * 0.9, momentum)
	if taktik_kalan > 0.0:
		hedef_hiz = sprint_hizi
	if girdi.y > 0.3:
		hedef_hiz = yurume_hizi * 0.8
	if hiz_seridi and yon != Vector3.ZERO:
		momentum = 1.0
		hedef_hiz = sprint_hizi * 1.5
	var yatay := yatay_hiz()
	# Ctrl tık (MW2019): hızlıyken kayma · yavaşken çömelme aç/kapa; Shift çömelmeyi bozar
	var kay_tik := _kay_tiklandi()
	if kay_tik:
		if cokuk:
			if _ayaga_kalkabilir():
				_ayaga_kalk()
		elif yatay.length() > 6.0:
			_kayma_baslat(yatay)
			return
		else:
			_cok()
	if cokuk and Input.is_action_pressed("kos") and _ayaga_kalkabilir():
		_ayaga_kalk()
	if cokuk:
		hedef_hiz = 3.5
		momentum = 0.0
	var hedef := yon * hedef_hiz
	var ivme := zemin_ivme if yon != Vector3.ZERO else zemin_fren
	if yon != Vector3.ZERO and yatay.length() > hedef_hiz:
		hedef = yon * yatay.length()
		ivme = zemin_fren * 0.5
	if Ayarlar.al("bhop") > 0.5 and yatay.length() > hedef_hiz:
		# Source Friction: control = max(hız, stopspeed); düşüş = control * sürtünme * dt
		var hiz0 := yatay.length()
		var kontrol: float = maxf(hiz0, 3.0)
		var yeni: float = maxf(hiz0 - kontrol * Ayarlar.al("bhop_surtunme") * delta, hedef_hiz)
		yatay = yatay * (yeni / hiz0)
		if yon != Vector3.ZERO:
			var mevcut := yatay.dot(yon)
			var eklenecek := hedef_hiz - mevcut
			if eklenecek > 0.0:
				yatay += yon * minf(zemin_ivme * delta, eklenecek)
	else:
		yatay = yatay.move_toward(hedef, ivme * delta)
	velocity.x = yatay.x
	velocity.z = yatay.z
	velocity.y = -2.0

	if yon.dot(ileri) > 0.5 and _basamak_dene():
		return
	if zipla_tampon > 0.0:
		zipla_tampon = 0.0
		if on_isin.is_colliding() and yon.dot(ileri) > 0.5 and _duvar_dik(on_isin.get_collision_normal()):
			_duvar_tirmanis_baslat(on_isin.get_collision_normal())
			return
		_zipla(1.0)


func _mc_yerde(delta: float, yon: Vector3, ileri: Vector3) -> void:
	var yatay := yatay_hiz()
	# Ctrl tık: sprintteyken kayma · yavaşken çömelme aç/kapa
	if _kay_tiklandi():
		if cokuk:
			if _ayaga_kalkabilir():
				_ayaga_kalk()
		elif yatay.length() > 4.5:
			_kayma_baslat(yatay)
			return
		else:
			_cok()
	if cokuk and Input.is_action_pressed("kos") and _ayaga_kalkabilir():
		_ayaga_kalk()
	# duvara bakıp zıplama → dikey tırmanış (parkur kancası)
	if zipla_tampon > 0.0 and on_isin.is_colliding() and yon.dot(ileri) > 0.5 and _duvar_dik(on_isin.get_collision_normal()):
		zipla_tampon = 0.0
		_duvar_tirmanis_baslat(on_isin.get_collision_normal())
		return
	if yon.dot(ileri) > 0.5 and _basamak_dene():
		return
	if _mc_adim(delta, true):
		zipla_tampon = 0.0
		coyote = 0.0
		kayma_istek = 0.0
		if cokuk and _ayaga_kalkabilir():
			_ayaga_kalk()
		_durum_degistir(Durum.HAVADA)
		eller.call("zipla")
		Ses.cal("zipla", -10.0, randf_range(0.9, 1.1))
	else:
		momentum = 1.0 if mc_sprint else 0.0


func _zipla(carpan: float) -> void:
	if cokuk and _ayaga_kalkabilir():
		_ayaga_kalk()
	velocity.y = ziplama_hizi * carpan
	coyote = 0.0
	kayma_istek = 0.0
	_durum_degistir(Durum.HAVADA)
	eller.call("zipla")
	Ses.cal("zipla", -10.0, randf_range(0.9, 1.1))


# ---------------- HAVADA ----------------
func _havada(delta: float, yon: Vector3, ileri: Vector3) -> void:
	if _mc_model() and not ucus_parkur:
		_mc_adim(delta, false)
	else:
		velocity.y -= yercekimi * delta
		mc_senkron_gerek = true
	dusme_hizi = minf(velocity.y, dusme_hizi)
	coyote = maxf(coyote - delta, 0.0)
	var yatay := yatay_hiz()
	if yon != Vector3.ZERO and (not _mc_model() or ucus_parkur):
		# 1) Bakış takibi (Dying Light): hız vektörü büyüklüğünü koruyarak girdi yönüne döner.
		var donus_hizi: float = deg_to_rad(Ayarlar.al("hava_donus"))
		if donus_hizi > 0.0 and yatay.length() > 0.5:
			var aci := yatay.signed_angle_to(yon, Vector3.UP)
			yatay = yatay.rotated(Vector3.UP, clampf(aci, -donus_hizi * delta, donus_hizi * delta))
		# 2) Source AirAccelerate (CS bunny hop): istenen yöndeki hız bileşeni tavanı aşamaz,
		#    eklenen ivme = min(airaccel * wishspeed * dt, tavan - v·wishdir). Yan tuş + fare
		#    dönüşüyle her karede tavan kadar yeni bileşen eklenir → hız birikir.
		var wishspeed: float = lerpf(kosu_hizi, sprint_hizi, momentum)
		var tavan: float = Ayarlar.al("bhop_tavan")
		var mevcut := yatay.dot(yon)
		var eklenecek := minf(wishspeed, tavan) - mevcut
		if eklenecek > 0.0:
			var ivme: float = minf(Ayarlar.al("bhop_hava_ivme") * wishspeed * delta, eklenecek)
			yatay += yon * ivme
	if not _mc_model() or ucus_parkur:
		velocity.x = yatay.x
		velocity.z = yatay.z

	# havada herhangi bir anda Ctrl (tık ya da basılı) → iniş anında kayma (MW2019); istek inişe kadar kalır
	if _kay_tiklandi() or (not sanal_girdi_aktif and Input.is_action_pressed("kay")):
		kayma_istek = 1.0

	if is_on_floor() and Engine.get_physics_frames() > firlat_kare + 2:
		# bunny hop: yere değilen karede zıplama basılıysa sürtünme/iniş kaybı olmadan zıpla
		if zipla_tampon > 0.0 and Ayarlar.al("bhop") > 0.5 and not _mc_model():
			zipla_tampon = 0.0
			dusme_hizi = 0.0
			son_duvar_id = 0
			Ses.cal("adim", -8.0, 1.1)
			_zipla(1.0)
			return
		_inis()
		return
	if yon.dot(ileri) > 0.3 and velocity.y < 7.0 and _tirmanma_dene():
		return
	if girdi.y < -0.3 and velocity.y < 5.0 and durum_suresi > 0.08:
		var taraf := _duvar_taraf_bul()
		if taraf != 0:
			_duvar_kosu_baslat(taraf, ileri)
			return
	if zipla_tampon > 0.0 and on_isin.is_colliding() and yon.dot(ileri) > 0.5 \
			and _duvar_dik(on_isin.get_collision_normal()) and durum_suresi > 0.1:
		zipla_tampon = 0.0
		_duvar_tirmanis_baslat(on_isin.get_collision_normal())
		return
	if zipla_tampon > 0.0 and coyote > 0.0 and not _mc_model():
		zipla_tampon = 0.0
		_zipla(1.0)


func _inis() -> void:
	ucus_parkur = false
	var siddet: float = clampf(-dusme_hizi / 22.0, 0.0, 1.0)
	Ses.cal("inis", lerpf(-18.0, 0.0, siddet), randf_range(0.9, 1.1))
	if siddet > 0.12:
		var tw := create_tween()
		inis_dip = -0.32 * siddet * Ayarlar.al("inis_dip")
		tw.tween_property(self, "inis_dip", 0.0, 0.28 + 0.2 * siddet).set_trans(Tween.TRANS_CUBIC).set_ease(Tween.EASE_OUT)
		eller.call("inis", siddet)
	if siddet > 0.55 and not _mc_model():
		if Input.is_action_pressed("kay"):
			eller.call("yuvarlan")
		else:
			velocity.x *= 0.45
			velocity.z *= 0.45
			momentum *= 0.5
	dusme_hizi = 0.0
	son_duvar_id = 0
	_durum_degistir(Durum.YERDE)
	# inişte kayma (havadayken Ctrl basıldıysa)
	if kayma_istek > 0.0:
		kayma_istek = 0.0
		if yatay_hiz().length() > 6.0:
			_kayma_baslat(yatay_hiz())


# ---------------- DUVAR KOŞUSU ----------------
func _duvar_dik(n: Vector3) -> bool:
	return absf(n.y) < 0.35


func _duvar_taraf_bul() -> int:
	if yatay_hiz().length() < 3.0:
		return 0
	for taraf in [-1, 1]:
		var isin: RayCast3D = sol_isin if taraf < 0 else sag_isin
		if not isin.is_colliding():
			continue
		if not _duvar_dik(isin.get_collision_normal()):
			continue
		var id := isin.get_collider().get_instance_id()
		if id == son_duvar_id and toplam_sure - son_duvar_zaman < 0.7:
			continue
		return taraf
	return 0


func _duvar_kosu_baslat(taraf: int, ileri: Vector3) -> void:
	var isin: RayCast3D = sol_isin if taraf < 0 else sag_isin
	duvar_normal = isin.get_collision_normal()
	duvar_normal.y = 0.0
	duvar_normal = duvar_normal.normalized()
	son_duvar_id = isin.get_collider().get_instance_id()
	duvar_taraf = taraf
	var yatay := yatay_hiz()
	duvar_yon = yatay.slide(duvar_normal)
	if duvar_yon.length() < 0.5:
		duvar_yon = ileri.slide(duvar_normal)
	duvar_yon = duvar_yon.normalized()
	var hiz := maxf(yatay.length(), duvar_kosu_hiz)
	velocity = duvar_yon * hiz
	velocity.y = 2.0
	_durum_degistir(Durum.DUVAR_KOSU)
	eller.call("duvar_kosu", taraf)
	Ses.cal("adim", -4.0, 0.8)


func _duvar_kosu(delta: float, _yon: Vector3, ileri: Vector3) -> void:
	var isin: RayCast3D = sol_isin if duvar_taraf < 0 else sag_isin
	var devam := isin.is_colliding() and durum_suresi < duvar_kosu_sure and girdi.y < -0.1 and not is_on_floor()
	if devam:
		var n := isin.get_collision_normal()
		n.y = 0.0
		if n.length() > 0.1:
			duvar_normal = n.normalized()
			duvar_yon = duvar_yon.slide(duvar_normal).normalized()
	if zipla_tampon > 0.0:
		zipla_tampon = 0.0
		_duvar_kosu_bitir(true, ileri)
		return
	if not devam:
		_duvar_kosu_bitir(false, ileri)
		return
	var t := durum_suresi / duvar_kosu_sure
	velocity.y -= yercekimi * delta * lerpf(0.12, 1.1, t * t)
	var hiz := maxf(yatay_hiz().length(), duvar_kosu_hiz * (1.0 - 0.25 * t))
	var yatay := duvar_yon * hiz - duvar_normal * 1.5
	velocity.x = yatay.x
	velocity.z = yatay.z


func _duvar_kosu_bitir(atla: bool, ileri: Vector3) -> void:
	son_duvar_zaman = toplam_sure
	if atla:
		var hiz := maxf(yatay_hiz().length(), duvar_kosu_hiz)
		var yon := duvar_yon * 0.75 + duvar_normal * 0.55
		if ileri.dot(duvar_normal) > 0.15:
			yon = ileri * 0.8 + duvar_normal * 0.4
		yon = yon.normalized()
		velocity = yon * hiz
		velocity.y = ziplama_hizi * 1.05
		eller.call("zipla")
	else:
		eller.call("serbest")
	_durum_degistir(Durum.HAVADA)


# ---------------- DUVAR TIRMANIŞI (dikey) ----------------
func _duvar_tirmanis_baslat(n: Vector3) -> void:
	duvar_normal = n
	duvar_normal.y = 0.0
	duvar_normal = duvar_normal.normalized()
	velocity = -duvar_normal * 2.0
	velocity.y = 7.2
	_durum_degistir(Durum.DUVAR_TIRMANIS)
	eller.call("tirmanis")


func _duvar_tirmanis(delta: float, _yon: Vector3, _ileri: Vector3) -> void:
	velocity.y -= yercekimi * delta * 0.55
	velocity.x = -duvar_normal.x * 2.0
	velocity.z = -duvar_normal.z * 2.0
	if _tirmanma_dene():
		return
	var bitti := durum_suresi > duvar_tirmanis_sure or velocity.y < 0.0 or not on_isin.is_colliding()
	if zipla_tampon > 0.0 and durum_suresi > 0.15:
		zipla_tampon = 0.0
		velocity = duvar_normal * 7.5
		velocity.y = ziplama_hizi
		eller.call("zipla")
		_durum_degistir(Durum.HAVADA)
		return
	if bitti:
		eller.call("serbest")
		_durum_degistir(Durum.HAVADA)


# ---------------- KENARA TUTUNUP ÇIKMA ----------------
func _tirmanma_dene() -> bool:
	if not tirmanma_orta.is_colliding() or tirmanma_ust.is_colliding():
		return false
	tirmanma_asagi.force_raycast_update()
	if not tirmanma_asagi.is_colliding():
		return false
	if tirmanma_asagi.get_collision_normal().y < 0.7:
		return false
	var ust := tirmanma_asagi.get_collision_point()
	var h := ust.y - global_position.y
	if h < 0.3 or h > 2.4:
		return false
	_tirman_baslat(ust + Vector3.UP * 0.05, clampf(h * 0.18, 0.25, 0.45))
	return true


## Küçük engel: ≤0.45 m anlık basamak, ≤1.3 m hızlı atlama (vault). Yüksek engel mantle işidir.
func _basamak_dene() -> bool:
	if not (ayak_isin.is_colliding() or diz_isin.is_colliding() or is_on_wall()):
		return false
	if tirmanma_orta.is_colliding():
		return false
	var en_iyi_h := -1.0
	var en_iyi := Vector3.ZERO
	for mesafe in [0.4, 0.55, 0.75, 0.95]:
		tirmanma_asagi.position = Vector3(0, 2.2, -mesafe)
		tirmanma_asagi.force_raycast_update()
		if tirmanma_asagi.is_colliding() and tirmanma_asagi.get_collision_normal().y > 0.7:
			var h := tirmanma_asagi.get_collision_point().y - global_position.y
			if h > 0.05 and h <= 1.3 and h > en_iyi_h:
				en_iyi_h = h
				en_iyi = tirmanma_asagi.get_collision_point()
	tirmanma_asagi.position = Vector3(0, 2.2, -0.9)
	if iz:
		print("[IZ] basamak h=%.3f poz=%s v=%s duvar=%s diz=%s ayak=%s" % [en_iyi_h, global_position, velocity, is_on_wall(), diz_isin.is_colliding(), ayak_isin.is_colliding()])
	if en_iyi_h < 0.0:
		return false
	if en_iyi_h <= 0.45:
		# anlık basamak: engelin üstüne çık, hızı koru
		var ileri := ileri_yon()
		var hiz := maxf(yatay_hiz().length(), kosu_hizi * 0.8)
		global_position = Vector3(en_iyi.x, en_iyi.y + 0.03, en_iyi.z) - ileri * 0.1
		velocity.x = ileri.x * hiz
		velocity.z = ileri.z * hiz
		velocity.y = -2.0
		return false
	_tirman_baslat(en_iyi + Vector3.UP * 0.05, clampf(en_iyi_h * 0.2, 0.14, 0.3))
	return true


func _tirman_baslat(hedef: Vector3, sure: float) -> void:
	kilit = true
	_durum_degistir(Durum.TIRMANMA)
	var hiz_koru := yatay_hiz().length()
	velocity = Vector3.ZERO
	var ara := Vector3(global_position.x, hedef.y, global_position.z)
	if tirman_tw and tirman_tw.is_valid():
		tirman_tw.kill()
	tirman_tw = create_tween()
	tirman_tw.tween_property(self, "global_position", ara, sure * 0.55).set_trans(Tween.TRANS_SINE).set_ease(Tween.EASE_OUT)
	tirman_tw.tween_property(self, "global_position", hedef, sure * 0.45).set_trans(Tween.TRANS_SINE)
	tirman_tw.tween_callback(_tirman_bitti.bind(hiz_koru))
	eller.call("tirman", sure)


func _tirman_bitti(hiz_koru: float) -> void:
	kilit = false
	var ileri := ileri_yon()
	var hiz := maxf(hiz_koru * 0.85, kosu_hizi * 0.6)
	velocity = ileri * hiz
	velocity.y = -1.0
	_durum_degistir(Durum.YERDE)
	eller.call("serbest")


# ---------------- KAYMA ----------------
func _kayma_baslat(yatay: Vector3) -> void:
	_durum_degistir(Durum.KAYMA)
	var yon := yatay.normalized()
	var hiz := yatay.length() + 3.0
	velocity.x = yon.x * hiz
	velocity.z = yon.z * hiz
	govde.set_deferred("disabled", true)
	govde_kisa.set_deferred("disabled", false)
	kafa_hedef_y = 0.75
	eller.call("kayma")
	Ses.cal("kayma", -8.0)


func _cok() -> void:
	cokuk = true
	govde.set_deferred("disabled", true)
	govde_kisa.set_deferred("disabled", false)
	kafa_hedef_y = 0.95


func _ayaga_kalkabilir() -> bool:
	tavan_isin.force_raycast_update()
	return not tavan_isin.is_colliding()


func _ayaga_kalk() -> void:
	cokuk = false
	govde.set_deferred("disabled", false)
	govde_kisa.set_deferred("disabled", true)
	kafa_hedef_y = 1.6


func _kayma(delta: float, _yon: Vector3, _ileri: Vector3) -> void:
	var yatay := yatay_hiz()
	if is_on_floor():
		var n := get_floor_normal()
		var egim := Vector3(n.x, 0.0, n.z)
		yatay += egim * yercekimi * 0.6 * delta
		yatay = yatay.move_toward(Vector3.ZERO, 5.5 * delta)
		velocity.y = -2.0
	else:
		velocity.y -= yercekimi * delta
	velocity.x = yatay.x
	velocity.z = yatay.z
	if zipla_tampon > 0.0 and _ayaga_kalkabilir():
		zipla_tampon = 0.0
		_ayaga_kalk()
		_zipla(1.0)
		return
	# slide cancel (MW2019): kayarken Ctrl tık → hız korunarak hemen ayağa
	if _kay_tiklandi() and durum_suresi > 0.12 and _ayaga_kalkabilir():
		_ayaga_kalk()
		_durum_degistir(Durum.HAVADA if not is_on_floor() else Durum.YERDE)
		eller.call("serbest")
		return
	# kayma biter → çömük kalır (Shift/Space/Ctrl tık kaldırır)
	if yatay.length() < 3.0 or durum_suresi > kayma_sure or (not is_on_floor() and durum_suresi > 0.35):
		cokuk = true
		kafa_hedef_y = 0.95
		_durum_degistir(Durum.HAVADA if not is_on_floor() else Durum.YERDE)
		eller.call("serbest")


# ---------------- KAMERA ----------------
func _kamera_guncelle(delta: float) -> void:
	var hiz := yatay_hiz().length()
	temel_fov = Ayarlar.al("fov")
	var hedef_fov: float = temel_fov + clampf((hiz - 6.0) / 6.5, 0.0, 1.0) * Ayarlar.al("sprint_fov")
	if _mc_model():
		# Minecraft: sprintte görüş açısı ×1.15 ((0.13/0.1 + 1) / 2)
		hedef_fov = temel_fov * (1.15 if mc_sprint and (durum == Durum.YERDE or durum == Durum.HAVADA) else 1.0)
	if durum == Durum.KAYMA:
		hedef_fov += 4.0
	kamera.fov = lerpf(kamera.fov, hedef_fov, 6.0 * delta)
	var hedef_roll := 0.0
	if durum == Durum.DUVAR_KOSU:
		hedef_roll = deg_to_rad(Ayarlar.al("egilme")) * duvar_taraf
	else:
		hedef_roll = -girdi.x * deg_to_rad(Ayarlar.al("yan_egilme"))
	kamera.rotation.z = lerp_angle(kamera.rotation.z, hedef_roll, 9.0 * delta)
	var bob_y := 0.0
	var bob_x := 0.0
	if durum == Durum.YERDE and hiz > 1.0:
		bob_faz += delta * hiz * 1.55
		var genlik: float = 0.028 * clampf(hiz / 9.0, 0.3, 1.5) * Ayarlar.al("bob")
		bob_y = absf(sin(bob_faz)) * genlik - genlik * 0.5
		bob_x = cos(bob_faz) * genlik * 0.55
		var adim := int(floor(bob_faz / PI))
		if adim != son_adim_sayac:
			son_adim_sayac = adim
			Ses.cal("adim", lerpf(-22.0, -8.0, clampf(hiz / 12.0, 0.0, 1.0)), randf_range(0.85, 1.15))
	Ses.ruzgar_ayarla(velocity.length())
	kafa.position.y = lerpf(kafa.position.y, kafa_hedef_y + bob_y + inis_dip, 12.0 * delta)
	kafa.position.x = lerpf(kafa.position.x, bob_x, 10.0 * delta)


# ---------------- PORTAL ----------------
## Portal3D eklentisi (ON_TELEPORT_CALLBACK): gövde dönüşümü yeni portala taşınmış durumda.
func on_teleport(portal: Node3D) -> void:
	var ileri: Vector3 = -kamera.global_basis.z
	var yatay := Vector3(ileri.x, 0.0, ileri.z)
	var yaw := rotation.y
	if yatay.length() > 0.05:
		yaw = atan2(-yatay.x, -yatay.z)
	rotation = Vector3(0.0, yaw, 0.0)
	kamera.rotation = Vector3(clampf(asin(clampf(ileri.y, -1.0, 1.0)), deg_to_rad(-85), deg_to_rad(85)), 0.0, kamera.rotation.z)
	kamera_yaw_ofset = 0.0
	velocity = portal.call("to_exit_direction", velocity)
	var cikis: Node3D = portal.get("exit_portal")
	var cikis_normal: Vector3 = cikis.global_basis.z
	var n_hiz := velocity.dot(cikis_normal)
	if n_hiz < 2.5:
		velocity += cikis_normal * (2.5 - n_hiz)
	global_position += cikis_normal * 0.05
	son_duvar_id = 0
	son_teleport_zaman = toplam_sure
	teleport_sayisi += 1
	mc_senkron_gerek = true
	Ses.cal("portal_gecis", -4.0)
	if durum != Durum.KAYMA:
		_durum_degistir(Durum.HAVADA)
	dusme_hizi = minf(velocity.y, 0.0)


## Fırlatma plakası vb. dış itki.
func firlat(v: Vector3) -> void:
	kilit = false
	_ayaga_kalk()
	# fırlatma uçuşu parkur fiziğiyle (Minecraft tick yerçekimi/ataleti plakayı bozar); inişte biter
	ucus_parkur = true
	firlat_kare = Engine.get_physics_frames()
	global_position.y += 0.06
	velocity = v
	mc_senkron_gerek = true
	dusme_hizi = 0.0
	_durum_degistir(Durum.HAVADA)
	durum_suresi = 0.0
	eller.call("zipla")


## Hareket durumunu sıfırlar (tween, kilit, hız, kapsül); konumu değiştirmez.
func sifirla() -> void:
	if tirman_tw and tirman_tw.is_valid():
		tirman_tw.kill()
	kilit = false
	velocity = Vector3.ZERO
	mc_senkron_gerek = true
	momentum = 0.0
	hiz_seridi = false
	dusme_hizi = 0.0
	son_duvar_id = 0
	_ayaga_kalk()
	_durum_degistir(Durum.HAVADA)
	eller.call("serbest")


func yeniden_dogur() -> void:
	sifirla()
	global_position = yeniden_dogum
	rotation = Vector3(0.0, yeniden_dogum_yaw, 0.0)
	kamera.rotation.x = 0.0
