shader_type spatial;
render_mode unshaded, blend_mix, cull_disabled, depth_draw_opaque;
// Portal çevresindeki ışıklı halka; çift tamamlanmadıysa içi koyu dolu çizilir.
uniform vec4 renk : source_color = vec4(0.25, 0.65, 1.0, 1.0);
uniform bool dolu = true;

void fragment() {
	vec2 p = (UV - vec2(0.5)) * 2.0;
	float r = length(p);
	if (r > 1.0) { discard; }
	float aci = atan(p.y, p.x);
	float dalga = 0.8 + 0.2 * sin(TIME * 5.0 + aci * 5.0);
	float halka = smoothstep(0.80, 0.88, r) * (1.0 - smoothstep(0.96, 1.0, r));
	vec3 c = renk.rgb * halka * dalga;
	float a = halka;
	if (dolu) {
		vec3 ic = vec3(0.02, 0.02, 0.03) + renk.rgb * 0.10 * (1.0 - r) * (0.7 + 0.3 * sin(TIME * 2.0 + r * 8.0));
		c = mix(ic, renk.rgb * dalga, halka);
		a = 1.0;
	}
	ALBEDO = c;
	EMISSION = renk.rgb * halka * 2.5 * dalga;
	ALPHA = a;
}
