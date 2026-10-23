/*
 * ============================================================================
 * Liquid Glass Dropdown Fragment Shader
 * ============================================================================
 *
 * Cross-platform iOS-style liquid glass rendering.
 *
 * Features:
 *   - Rounded rectangle signed distance fields.
 *   - Smooth union between button and dropdown menu.
 *   - Animated liquid deformation.
 *   - Golden-angle background blur.
 *   - Lens refraction and bevel displacement.
 *   - Directional rim lighting.
 *   - Touch tint and radial highlight.
 *   - Cross-platform-safe smoothstep transitions.
 *
 * Coordinate convention:
 *   u_pos, u_pos2, u_size, u_size2 and iResolution must use the same
 *   coordinate space as gl_FragCoord.
 *
 * ============================================================================
 */

#ifdef GL_ES
precision highp float;
#endif

varying vec4 frag_color;
varying vec2 tex_coord0;

uniform sampler2D texture0;

uniform vec2 iResolution;

uniform vec2 u_pos;
uniform vec2 u_size;
uniform vec2 u_pos2;
uniform vec2 u_size2;

uniform vec2 u_touch_pos;

uniform vec4 u_radius;
uniform vec4 u_radius2;
uniform vec4 u_glass_color;

uniform float u_pressed;
uniform float u_blur_amount;
uniform float u_menu_alpha;
uniform float u_k;
uniform float u_wobble;
uniform float u_time;

uniform float u_lens_power;
uniform float u_bevel_power;
uniform float u_border_opacity;

const float PI = 3.14159265359;
const float TWO_PI = 6.28318530718;
const float GOLDEN_ANGLE = 2.39996323;
const float EPSILON = 0.0001;
const float AA_WIDTH = 1.5;
const float BLUR_SAMPLES = 16.0;


// ============================================================================
// Rounded rectangle SDF
// ============================================================================

float sdRoundedRect(
    vec2 pos,
    vec2 halfSize,
    vec4 cornerRadius
) {
    halfSize = max(halfSize, vec2(0.0));

    float maxRadius = min(halfSize.x, halfSize.y);

    cornerRadius = clamp(
        cornerRadius,
        vec4(0.0),
        vec4(maxRadius)
    );

    float radius =
        (pos.x > 0.0)
            ? ((pos.y > 0.0)
                ? cornerRadius.y
                : cornerRadius.z)
            : ((pos.y > 0.0)
                ? cornerRadius.x
                : cornerRadius.w);

    vec2 q = abs(pos) - halfSize + radius;

    return
        min(max(q.x, q.y), 0.0)
        + length(max(q, vec2(0.0)))
        - radius;
}


// ============================================================================
// Smooth minimum
// ============================================================================

float smin(
    float a,
    float b,
    float k
) {
    if (k <= EPSILON) {
        return min(a, b);
    }

    float h = clamp(
        0.5 + 0.5 * (b - a) / k,
        0.0,
        1.0
    );

    return mix(b, a, h) - k * h * (1.0 - h);
}


// ============================================================================
// Liquid shape SDF
// ============================================================================

float mapSDF(vec2 fragCoord) {
    float menuAlpha = clamp(u_menu_alpha, 0.0, 1.0);

    vec2 center1 = u_pos + u_size * 0.5;
    vec2 halfSize1 = max(u_size * 0.5, vec2(0.0));

    float sdf1 = sdRoundedRect(
        fragCoord - center1,
        halfSize1,
        u_radius
    );

    vec2 targetCenter = u_pos2 + u_size2 * 0.5;
    vec2 targetHalfSize = max(u_size2 * 0.5, vec2(0.0));

    vec2 currentMenuCenter = mix(
        center1,
        targetCenter,
        menuAlpha
    );

    vec2 currentMenuHalfSize = mix(
        halfSize1 * 0.2,
        targetHalfSize,
        menuAlpha
    );

    vec4 currentRadius = mix(
        u_radius,
        u_radius2,
        menuAlpha
    );

    float sdf2 = sdRoundedRect(
        fragCoord - currentMenuCenter,
        currentMenuHalfSize,
        currentRadius
    );

    vec2 dir = fragCoord - currentMenuCenter;

    // Avoid unstable angle calculations at the shape center.
    if (dot(dir, dir) < EPSILON * EPSILON) {
        dir = vec2(EPSILON, 0.0);
    }

    float angle = atan(dir.y, dir.x);

    // Smoothstep edges must be strictly increasing.
    // This factor increases as the liquid blend parameter approaches zero.
    float transition =
        sin(clamp(u_menu_alpha, 0.0, 1.0) * PI);

    float transitionIntensity =
        transition * transition;

    float ripple =
        sin(angle * 5.0 + u_time * 30.0)
        * (-cos(angle * 3.0 + u_time * 20.0));

    float totalWobble =
        u_wobble
        + ripple * transitionIntensity * 0.8;

    float dropWobble =
        -totalWobble;

    sdf1 += dropWobble;
    sdf2 += dropWobble;

    if (menuAlpha >= 0.999) {
        return sdf2;
    }

    if (menuAlpha <= 0.001) {
        return sdf1;
    }

    return smin(sdf1, sdf2, max(u_k, 0.0));
}


// ============================================================================
// SDF normal
// ============================================================================

vec2 getSDFGradient(vec2 pos) {
    const float EPS = 0.5;

    float dx =
        mapSDF(pos + vec2(EPS, 0.0))
        - mapSDF(pos - vec2(EPS, 0.0));

    float dy =
        mapSDF(pos + vec2(0.0, EPS))
        - mapSDF(pos - vec2(0.0, EPS));

    vec2 gradient = vec2(dx, dy);
    float gradientLength = length(gradient);

    if (gradientLength < EPSILON) {
        return vec2(0.0, 1.0);
    }

    return gradient / gradientLength;
}


// ============================================================================
// Golden-angle disk blur
// ============================================================================

vec3 getBlurredColor(
    vec2 uv,
    float blurAmount
) {
    vec2 resolution = max(iResolution, vec2(1.0));

    vec2 radius = vec2(max(blurAmount, 0.0)) / resolution;

    vec3 color = vec3(0.0);

    for (float i = 0.0; i < BLUR_SAMPLES; i += 1.0) {
        float r = sqrt((i + 0.5) / BLUR_SAMPLES);

        float theta = i * GOLDEN_ANGLE;

        vec2 offset = vec2(
            cos(theta),
            sin(theta)
        ) * r * radius;

        vec2 sampleUV = clamp(
            uv + offset,
            vec2(0.0),
            vec2(1.0)
        );

        color += texture2D(texture0, sampleUV).rgb;
    }

    return color / BLUR_SAMPLES;
}


// ============================================================================
// Fragment shader
// ============================================================================

void main() {
    /*
     * Use one coordinate convention on every backend.
     *
     * GL_FRAGMENT_PRECISION_HIGH is not a platform identifier and must not
     * control the direction of the Y axis.
     *
     * All geometry uniforms must be supplied in this same coordinate space.
     */
    vec2 fragCoord = gl_FragCoord.xy;

    vec2 resolution = max(iResolution, vec2(1.0));

    float sdf = mapSDF(fragCoord);

    // Discard pixels outside the shape before expensive blur calculations.
    if (sdf > AA_WIDTH) {
        discard;
    }

    vec2 grad = getSDFGradient(fragCoord);

    vec2 screenUV = fragCoord / resolution;

    float menuAlpha = clamp(u_menu_alpha, 0.0, 1.0);

    vec2 center1 = u_pos + u_size * 0.5;
    vec2 center2 = u_pos2 + u_size2 * 0.5;

    vec2 activeCenter = mix(
        center1,
        center2,
        menuAlpha
    );

    vec2 activeHalfSize = max(
        mix(
            u_size * 0.5,
            u_size2 * 0.5,
            menuAlpha
        ),
        vec2(EPSILON)
    );

    // ------------------------------------------------------------------------
    // Lens refraction
    // ------------------------------------------------------------------------

    vec2 normUV = (fragCoord - activeCenter) / activeHalfSize;

    float dist = length(normUV);

    vec2 lensOffset =
        normUV
        * (1.0 - smoothstep(0.0, 1.5, dist))
        * u_lens_power;

    // ------------------------------------------------------------------------
    // Bevel refraction
    // ------------------------------------------------------------------------

    float heightRef = min(
        activeHalfSize.x,
        activeHalfSize.y
    );

    float bevelWidth = max(
        min(24.0, heightRef * 0.4),
        EPSILON
    );

    float bevelMask = smoothstep(
        -bevelWidth,
        0.0,
        sdf
    );

    vec2 bevelOffset =
        grad
        * bevelMask
        * u_bevel_power;

    vec2 activeSize = max(
        mix(u_size, u_size2, menuAlpha),
        vec2(EPSILON)
    );

    vec2 finalUVOffset =
        (lensOffset - bevelOffset)
        * (activeSize / resolution);

    vec2 sampleUV = screenUV - finalUVOffset;

    // ------------------------------------------------------------------------
    // Background blur and glass tint
    // ------------------------------------------------------------------------

    vec3 blurredTex = getBlurredColor(
        sampleUV,
        u_blur_amount
    );

    blurredTex = pow(
        max(blurredTex, vec3(0.0)),
        vec3(0.88)
    ) * 1.15;

    vec3 finalColor = mix(
        blurredTex,
        u_glass_color.rgb,
        clamp(u_glass_color.a, 0.0, 1.0)
    );

    // ------------------------------------------------------------------------
    // Inner bevel shadow
    // ------------------------------------------------------------------------

    float innerBevel = smoothstep(
        -heightRef * 0.35,
        0.0,
        sdf
    ) * 0.2;

    finalColor *= 1.0 - innerBevel;

    // ------------------------------------------------------------------------
    // Rim highlights
    // ------------------------------------------------------------------------

    float rimMask =
        smoothstep(-3.0, -0.5, sdf)
        *
        (1.0 - smoothstep(-0.5, 0.5, sdf));

    vec2 lightDir = normalize(vec2(-0.5, 0.85));

    float NdotL = dot(grad, lightDir);

    float topLeftHighlight =
        pow(max(0.0, NdotL), 2.2)
        * rimMask
        * 1.1;

    float bottomRightHighlight =
        pow(max(0.0, -NdotL), 3.0)
        * rimMask
        * 0.75;

    float edgeStroke =
        smoothstep(-1.2, 0.0, sdf)
        * 0.25;

    finalColor +=
        vec3(1.0)
        * (
            topLeftHighlight
            + bottomRightHighlight
            + edgeStroke
        )
        * u_border_opacity;

    // ------------------------------------------------------------------------
    // Touch tint and radial highlight
    // ------------------------------------------------------------------------

    float pressed = clamp(u_pressed, 0.0, 1.0);

    vec3 pressedGlassColor = mix(
        finalColor,
        vec3(0.25, 0.55, 1.0),
        0.25
    );

    finalColor = mix(
        finalColor,
        pressedGlassColor,
        pressed
    );

    float lightRadius = max(
        max(u_size.x, u_size.y) * 0.85,
        EPSILON
    );

    float touchDistance = length(
        fragCoord - u_touch_pos
    );

    // Avoid reversed smoothstep edges.
    float spot = 1.0 - smoothstep(
        0.0,
        lightRadius,
        touchDistance
    );

    finalColor = mix(
        finalColor,
        vec3(1.0),
        spot * pressed * 0.35
    );

    // ------------------------------------------------------------------------
    // Antialiased edge alpha
    // ------------------------------------------------------------------------

    float edgeAlpha = 1.0 - smoothstep(
        -AA_WIDTH,
        AA_WIDTH,
        sdf
    );

    edgeAlpha = clamp(edgeAlpha, 0.0, 1.0);

    gl_FragColor = vec4(
        finalColor,
        edgeAlpha * frag_color.a
    );
}
