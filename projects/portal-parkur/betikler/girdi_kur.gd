extends Node
## Girdi haritasını kodla kurar (project.godot içindeki uzun nesne sözdiziminden kaçınmak için).

const TUSLAR := {
	"ileri": KEY_W, "geri": KEY_S, "sol": KEY_A, "sag": KEY_D,
	"zipla": KEY_SPACE, "kos": KEY_SHIFT, "kay": KEY_CTRL,
	"yeniden": KEY_R, "cikis": KEY_ESCAPE, "hata_ayik": KEY_F3,
}
const FARE := {"portal_mavi": MOUSE_BUTTON_LEFT, "portal_turuncu": MOUSE_BUTTON_RIGHT}

func _ready() -> void:
	for ad in TUSLAR:
		if not InputMap.has_action(ad):
			InputMap.add_action(ad)
		var e := InputEventKey.new()
		e.physical_keycode = TUSLAR[ad]
		InputMap.action_add_event(ad, e)
	var c := InputEventKey.new()
	c.physical_keycode = KEY_C
	InputMap.action_add_event("kay", c)
	for ad in FARE:
		if not InputMap.has_action(ad):
			InputMap.add_action(ad)
		var m := InputEventMouseButton.new()
		m.button_index = FARE[ad]
		InputMap.action_add_event(ad, m)
