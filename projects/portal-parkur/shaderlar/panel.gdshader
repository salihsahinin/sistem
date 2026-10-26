shader_type spatial;
// Dünya-uzayı üç-düzlemli panel ızgarası (Aperture beyaz / koyu paneller, bina cepheleri).
uniform vec4 taban : source_color = vec4(0.93, 0.93, 0.91, 1.0);
uniform vec4 derz : source_color = vec4(0.62, 0.62, 0.60, 1.0);
uniform float boyut = 1.0;
uniform float derz_genislik = 0.025;
uniform float pah = 0.06;
uniform float puruz = 0.55;
uniform float metal = 0.0;
varying vec3 dunya_poz;
varying vec3 dunya_norm;

void vertex() {
	dunya_poz = (MODEL_MATRIX * vec4(VERTEX, 1.0)).xyz;
	dunya_norm = normalize((MODEL_MATRIX * vec4(NORMAL, 0.0)).xyz);
}

void fragment() {
	vec3 n = abs(dunya_norm);
	vec2 uv;
	if (n.y > 0.5) { uv = dunya_poz.xz; }
	else if (n.x > 0.5) { uv = dunya_poz.zy; }
	else { uv = dunya_poz.xy; }
	vec2 q = uv / boyut;
	vec2 e = (0.5 - abs(fract(q) - 0.5)) * boyut;
	float d = min(e.x, e.y);
	float cizgi = 1.0 - smoothstep(0.0, derz_genislik, d);
	float pah_k = 1.0 - smoothstep(derz_genislik, derz_genislik + pah, d);
	vec3 renk = mix(taban.rgb, taban.rgb * 0.88, pah_k * 0.6);
	renk = mix(renk, derz.rgb, cizgi);
	ALBEDO = renk;
	ROUGHNESS = puruz;
	METALLIC = metal;
}
