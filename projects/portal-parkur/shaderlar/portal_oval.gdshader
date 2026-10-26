shader_type spatial;
render_mode unshaded;
// Eklentinin düz portal shader'ı + oval maske: kutu mesh UV 0..1, elips dışı atılır.
uniform sampler2D albedo : hint_default_black, source_color;
uniform vec4 halka_renk : source_color = vec4(0.25, 0.65, 1.0, 1.0);

void fragment() {
	vec2 p = (UV - vec2(0.5)) * 2.0;
	float r = length(p);
	if (r > 1.0) { discard; }
	vec3 col = texture(albedo, SCREEN_UV).rgb;
	float kenar = smoothstep(0.84, 1.0, r);
	ALBEDO = mix(col, halka_renk.rgb, kenar * 0.85);
	EMISSION = halka_renk.rgb * kenar * 1.2;
}
