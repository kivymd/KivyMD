/*
The shader code has been refactored for the KivyMD library.
You can find the original code of this shaders at the links:

https://www.shadertoy.com/view/WtdSDs
https://www.shadertoy.com/view/fsdyzB

Additional thanks to iq for optimizing conditional block for individual
corner radius:
https://iquilezles.org/articles/distfunctions
*/

// For lower opengl version

float custom_smoothstep(float a, float b, float x) {
    float t = clamp((x - a) / (b - a), 0.0, 1.0);
    return t * t * (3.0 - 2.0 * t);
}

float roundedBoxSDF(vec2 centerPosition, vec2 size, vec4 radius) {
    radius.xy = (centerPosition.x > 0.0) ? radius.xy : radius.zw;
    radius.x = (centerPosition.y > 0.0) ? radius.x : radius.y;

    vec2 q = abs(centerPosition) - (size - shadow_softness) + radius.x;
    return min(max(q.x, q.y), 0.0) + length(max(q, 0.0)) - radius.x;
}

void mainImage(out vec4 fragColor, in vec2 fragCoord) {
    // Smooth the result (free antialiasing).
    float edge0 = 0.0;
    float smoothedAlpha = 1.0 - custom_smoothstep(0.0, edge0, 1.0);
    // Get the resultant shape.
    vec4 quadColor = mix(
        vec4(
            shadow_color[0],
            shadow_color[1],
            shadow_color[2],
            0.0
        ),
        shadow_color,
        smoothedAlpha
    );
    // Apply a drop shadow effect.
    float shadowDistance = roundedBoxSDF(
        fragCoord.xy - mouse.xy - (size / 2.0), size / 2.0, shadow_radius
    );
    float shadowAlpha = 1.0 - custom_smoothstep(
        -shadow_softness, shadow_softness, shadowDistance
    );
    fragColor = mix(quadColor, shadow_color, shadowAlpha - smoothedAlpha);
}
