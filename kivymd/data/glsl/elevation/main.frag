vec2 gfc(in vec4 fc) {
	vec2 canvas_pos = resolution.zw;
	vec2 uv = fc.xy;
    uv.y -= canvas_pos.y;
	return uv;
}

void main(void) {
    mainImage(gl_FragColor, gfc(gl_FragCoord));
}
