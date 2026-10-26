shader_type canvas_item;
// Hıza bağlı radyal hareket bulanıklığı + vinyet (tam ekran ColorRect).
uniform sampler2D ekran : hint_screen_texture, filter_linear_mipmap;
uniform float guc = 0.0;
uniform float vinyet = 0.0;

void fragment() {
	vec2 uv = SCREEN_UV;
	vec2 yon = uv - vec2(0.5);
	vec4 top = vec4(0.0);
	const int N = 10;
	for (int i = 0; i < N; i++) {
		float t = float(i) / float(N - 1);
		top += texture(ekran, uv - yon * t * guc);
	}
	vec4 c = top / float(N);
	float v = smoothstep(0.45, 0.95, length(yon) * 1.35);
	c.rgb *= 1.0 - v * vinyet;
	COLOR = c;
}
