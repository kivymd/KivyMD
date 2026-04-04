uniform vec2 in_origin;
uniform vec2 in_touch;
uniform float in_progress;
uniform float in_maxRadius;
uniform vec2 in_resolutionScale;
uniform vec2 in_noiseScale;
uniform float in_noisePhase;
uniform float in_turbulencePhase;

uniform vec2 in_tCircle1;
uniform vec2 in_tCircle2;
uniform vec2 in_tCircle3;
uniform vec2 in_tRotation1;
uniform vec2 in_tRotation2;
uniform vec2 in_tRotation3;

uniform vec4 in_color;
uniform vec4 in_sparkleColor;

float saturate(float v) {
    return clamp(v, 0.0, 1.0);
}

float triangleNoise(vec2 n) {
    n = fract(n * vec2(5.3987, 5.4421));
    n += dot(n.yx, n.xy + vec2(21.5351, 14.3137));
    float xy = n.x * n.y;
    return fract(xy * 95.4307) + fract(xy * 75.04961) - 1.0;
}

float threshold(float v, float low, float high) {
    return step(low, v) * (1.0 - step(high, v));
}

float sparkles(vec2 uv, float t) {
    float n = triangleNoise(uv);
    float s = 0.0;
    const float PI = 3.14159265359;
    for (int i = 0; i < 4; ++i) {
        float fi = float(i);
        float low = fi * 0.1;
        float high = low + 0.05;
        float offset = sin(PI * (t + 0.35 * fi));
        s += threshold(n + offset, low, high);
    }
    return saturate(s) * in_sparkleColor.a;
}

float softCircle(vec2 uv, vec2 xy, float radius, float blur) {
    float blur_half = blur * 0.5;
    float d = distance(uv, xy);
    return 1.0 - smoothstep(1.0 - blur_half, 1.0 + blur_half, d / max(radius, 0.0001));
}

float softRing(vec2 uv, vec2 xy, float radius, float progress, float blur) {
    float thickness = 0.05 * radius;
    float current_radius = radius * progress;
    float outer_circle = softCircle(uv, xy, current_radius + thickness, blur);
    float inner_circle = softCircle(uv, xy, max(current_radius - thickness, 0.0), blur);
    return saturate(outer_circle - inner_circle);
}

float subProgress(float start, float end, float progress) {
    float sub = clamp(progress, start, end);
    return (sub - start) / (end - start);
}

mat2 rotate2d(vec2 rad) {
    return mat2(rad.x, -rad.y, rad.y, rad.x);
}

float circle_grid(vec2 resolution, vec2 coord, vec2 center, vec2 rotation, float cell_diameter) {
    coord = rotate2d(rotation) * (center - coord) + center;
    coord = mod(coord, cell_diameter) / resolution;
    float normal_radius = cell_diameter / resolution.y * 0.5;
    float radius = 0.65 * normal_radius;
    return softCircle(coord, vec2(normal_radius), radius, radius * 50.0);
}

float turbulence(vec2 uv, float t_phase) {
    const vec2 scale = vec2(0.8);
    uv = uv * scale;
    float g1 = circle_grid(scale, uv, in_tCircle1, in_tRotation1, 0.17);
    float g2 = circle_grid(scale, uv, in_tCircle2, in_tRotation2, 0.2);
    float g3 = circle_grid(scale, uv, in_tCircle3, in_tRotation3, 0.275);
    float v = (g1 * g1 + g2 - g3) * 0.5;
    return saturate(0.45 + 0.8 * v);
}

void main(void) {
    vec2 p = tex_coord0 / in_resolutionScale;

    float fadeIn = subProgress(0.0, 0.13, in_progress);
    float scaleIn = subProgress(0.0, 1.0, in_progress);
    float fadeOutNoise = subProgress(0.4, 0.5, in_progress);
    float fadeOutRipple = subProgress(0.4, 1.0, in_progress);

    vec2 center = mix(in_touch, in_origin, saturate(in_progress * 2.0));
    float ring = softRing(p, center, in_maxRadius, scaleIn, 1.0);
    float alpha = min(fadeIn, 1.0 - fadeOutNoise);

    vec2 uv_for_noise = p;
    vec2 density_uv = uv_for_noise - mod(uv_for_noise, in_noiseScale);
    float turb = turbulence(uv_for_noise, in_turbulencePhase);
    float sparkleAlpha = sparkles(density_uv, in_noisePhase) * ring * alpha * turb;

    float fade = min(fadeIn, 1.0 - fadeOutRipple);
    float waveAlpha = softCircle(p, center, in_maxRadius * scaleIn, 1.0) * fade * in_color.a;
    
    vec4 waveColor = vec4(in_color.rgb * waveAlpha, waveAlpha);
    vec4 sparkleColor = vec4(in_sparkleColor.rgb * in_sparkleColor.a, in_sparkleColor.a);
    vec4 ripple_effect = mix(waveColor, sparkleColor, sparkleAlpha);

    gl_FragColor = ripple_effect;
}
