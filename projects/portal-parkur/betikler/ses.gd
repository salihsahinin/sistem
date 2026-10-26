extends Node
## Yordamsal sesler: başlangıçta kısa WAV tamponları sentezlenir, dış ses varlığı yoktur.
## Kullanım: Ses.cal("adim"), Ses.ruzgar_ayarla(hiz)

const MIX := 22050
var sesler := {}
var havuz: Array[AudioStreamPlayer] = []
var ruzgar: AudioStreamPlayer
var ruzgar_hedef_db := -60.0
var rng := RandomNumberGenerator.new()


func _ready() -> void:
	rng.seed = 7
	sesler["adim"] = _wav(_adim())
	sesler["zipla"] = _wav(_zipla())
	sesler["inis"] = _wav(_inis())
	sesler["portal_ates"] = _wav(_portal_ates())
	sesler["portal_gecis"] = _wav(_portal_gecis())
	sesler["kayma"] = _wav(_kayma())
	sesler["fizil"] = _wav(_fizil())
	var r := _wav(_ruzgar())
	r.loop_mode = AudioStreamWAV.LOOP_FORWARD
	r.loop_end = r.data.size() / 2
	for i in 8:
		var p := AudioStreamPlayer.new()
		add_child(p)
		havuz.append(p)
	ruzgar = AudioStreamPlayer.new()
	ruzgar.stream = r
	ruzgar.volume_db = -60.0
	add_child(ruzgar)
	ruzgar.play()


func _process(delta: float) -> void:
	ruzgar.volume_db = lerpf(ruzgar.volume_db, ruzgar_hedef_db, 4.0 * delta)


func cal(ad: String, db := 0.0, pitch := 1.0) -> void:
	if not sesler.has(ad):
		return
	for p in havuz:
		if not p.playing:
			p.stream = sesler[ad]
			p.volume_db = db
			p.pitch_scale = pitch
			p.play()
			return


func ruzgar_ayarla(hiz: float) -> void:
	var t: float = clampf((hiz - 7.0) / 14.0, 0.0, 1.0)
	ruzgar_hedef_db = lerpf(-40.0, -8.0, t) if t > 0.0 else -60.0


# ---------------- sentez ----------------
func _wav(ornekler: PackedFloat32Array) -> AudioStreamWAV:
	var n := ornekler.size()
	var bytes := PackedByteArray()
	bytes.resize(n * 2)
	for i in n:
		bytes.encode_s16(i * 2, int(clampf(ornekler[i], -1.0, 1.0) * 32000.0))
	var w := AudioStreamWAV.new()
	w.format = AudioStreamWAV.FORMAT_16_BITS
	w.mix_rate = MIX
	w.stereo = false
	w.data = bytes
	return w


func _gurultu_lp(sure: float, kesim: float) -> PackedFloat32Array:
	var n := int(sure * MIX)
	var a := PackedFloat32Array()
	a.resize(n)
	var y := 0.0
	var k: float = clampf(kesim / MIX * 6.28, 0.0, 1.0)
	for i in n:
		y += k * (rng.randf_range(-1.0, 1.0) - y)
		a[i] = y
	return a


func _zarf(a: PackedFloat32Array, atak: float, sonum: float) -> PackedFloat32Array:
	var n := a.size()
	for i in n:
		var t := float(i) / MIX
		var e: float = minf(t / maxf(atak, 0.0005), 1.0) * exp(-t * sonum)
		a[i] *= e
	return a


func _adim() -> PackedFloat32Array:
	return _zarf(_gurultu_lp(0.09, 900.0), 0.003, 45.0)


func _zipla() -> PackedFloat32Array:
	var a := _gurultu_lp(0.18, 2500.0)
	return _zarf(a, 0.02, 18.0)


func _inis() -> PackedFloat32Array:
	var n := int(0.2 * MIX)
	var a := _gurultu_lp(0.2, 600.0)
	for i in n:
		var t := float(i) / MIX
		a[i] = a[i] * 0.7 + sin(t * 6.28 * 70.0) * 0.8 * exp(-t * 25.0)
	return _zarf(a, 0.002, 14.0)


func _portal_ates() -> PackedFloat32Array:
	var n := int(0.28 * MIX)
	var a := PackedFloat32Array()
	a.resize(n)
	var faz := 0.0
	for i in n:
		var t := float(i) / MIX
		var f: float = lerpf(300.0, 1400.0, t / 0.28)
		faz += f / MIX * 6.28
		a[i] = (sin(faz) * 0.6 + sin(faz * 2.01) * 0.25) * exp(-t * 9.0) + rng.randf_range(-0.1, 0.1) * exp(-t * 30.0)
	return a


func _portal_gecis() -> PackedFloat32Array:
	var n := int(0.45 * MIX)
	var a := _gurultu_lp(0.45, 1800.0)
	var faz := 0.0
	for i in n:
		var t := float(i) / MIX
		var e := sin(clampf(t / 0.45, 0.0, 1.0) * PI)
		var f: float = lerpf(900.0, 200.0, t / 0.45)
		faz += f / MIX * 6.28
		a[i] = a[i] * 0.9 * e + sin(faz) * 0.25 * e
	return a


func _kayma() -> PackedFloat32Array:
	return _zarf(_gurultu_lp(0.6, 1200.0), 0.03, 4.0)


func _fizil() -> PackedFloat32Array:
	var n := int(0.25 * MIX)
	var a := _gurultu_lp(0.25, 3000.0)
	for i in n:
		var t := float(i) / MIX
		a[i] = a[i] * (1.0 - t / 0.25) * (0.5 + 0.5 * sin(t * 6.28 * 40.0))
	return a


func _ruzgar() -> PackedFloat32Array:
	var a := _gurultu_lp(1.0, 500.0)
	var n := a.size()
	for i in 400:
		var k := float(i) / 400.0
		a[i] *= k
		a[n - 1 - i] *= k
	return a
