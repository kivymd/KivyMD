#ifdef GL_ES
precision mediump float;
#endif

varying vec4 frag_color;
uniform vec4 u_radius;
uniform vec4 u_radius2;
uniform vec4 u_glass_color;

uniform sampler2D texture0;

uniform vec2 iResolution;
uniform vec2 u_pos;
uniform vec2 u_size;
uniform vec2 u_pos2;
uniform vec2 u_size2;
varying vec2 tex_coord0;
uniform vec2 u_touch_pos;

uniform float u_pressed;
uniform float u_blur_amount;
uniform float u_menu_alpha;
uniform float u_k;
uniform float u_wobble;
uniform float u_time;

uniform float u_lens_power;
uniform float u_bevel_power;
uniform float u_border_opacity;

float sdRoundedRect(
    vec2 pos,
    vec2 halfSize,
    vec4 cornerRadius
) {
    float maxRadius =
        min(
            halfSize.x,
            halfSize.y
        );

    cornerRadius =
        min(
            cornerRadius,
            vec4(maxRadius)
        );

    float r =
        (pos.x > 0.0)
            ? ((pos.y > 0.0)
                ? cornerRadius.y
                : cornerRadius.z)
            : ((pos.y > 0.0)
                ? cornerRadius.x
                : cornerRadius.w);

    vec2 q =
        abs(pos)
        - halfSize
        + r;

    return
        min(
            max(q.x, q.y),
            0.0
        )
        + length(max(q, 0.0))
        - r;
}

float smin(
    float a,
    float b,
    float k
) {
    if (k <= 0.0001) return min(a, b);
    float h =
        clamp(
            0.5 + 0.5 * (b - a) / max(k, 0.0001),
            0.0,
            1.0
        );
    return
        mix(b, a, h)
        - k * h * (1.0 - h);
}

float mapSDF(
    vec2 fragCoord
) {
    vec2 center1 =
        u_pos
        + u_size * 0.5;

    vec2 halfSize1 =
        u_size * 0.5;

    vec2 currentButtonHalfSize =
        mix(
            halfSize1,
            vec2(0.0),
            u_menu_alpha
        );

    float sdf1 =
        sdRoundedRect(
            fragCoord - center1,
            currentButtonHalfSize,
            u_radius
        );

    vec2 targetCenter =
        u_pos2
        + u_size2 * 0.5;

    vec2 targetHalfSize =
        u_size2 * 0.5;

    vec2 currentMenuCenter =
        mix(
            center1,
            targetCenter,
            u_menu_alpha
        );

    vec2 currentMenuHalfSize =
        mix(
            halfSize1 * 0.2,
            targetHalfSize,
            u_menu_alpha
        );

    vec4 currentRadius =
        mix(
            u_radius,
            u_radius2,
            u_menu_alpha
        );

    float sdf2 =
        sdRoundedRect(
            fragCoord - currentMenuCenter,
            currentMenuHalfSize,
            currentRadius
        );

    if (u_menu_alpha >= 0.999) return sdf2;
    if (u_menu_alpha <= 0.001) return sdf1;

    return smin(sdf1, sdf2, max(u_k, 0.001));
}

vec2 getSDFGradient(
    vec2 pos
) {
    vec2 eps =
        vec2(0.5, 0.0);

    float dx =
        mapSDF(pos + eps.xy)
        -
        mapSDF(pos - eps.xy);

    float dy =
        mapSDF(pos + eps.yx)
        -
        mapSDF(pos - eps.yx);

    return
        normalize(
            vec2(dx, dy)
            + vec2(0.0001)
        );
}

vec3 getBlurredColor(
    vec2 uv,
    float blurAmount
) {
    vec2 radius =
        vec2(blurAmount)
        / max(iResolution, vec2(1.0));

    const float SAMPLES = 16.0;
    const float GOLDEN_ANGLE = 2.3999632;

    vec3 col = vec3(0.0);

    for (float i = 0.0; i < SAMPLES; i += 1.0) {
        float r =
            sqrt((i + 0.5) / SAMPLES);

        float theta =
            mod(i * GOLDEN_ANGLE, 6.28318530718);

        vec2 offset =
            vec2(
                cos(theta),
                sin(theta)
            )
            * r
            * radius;

        col +=
            texture2D(
                texture0,
                clamp(uv + offset, 0.0, 1.0)
            ).rgb;
    }

    return col / SAMPLES;
}

void main() {
    vec2 fragCoord =
        gl_FragCoord.xy;

    float sdf =
        mapSDF(fragCoord);

    float aa = 1.5;

    if (sdf > aa) {
        discard;
    }

    vec2 grad =
        getSDFGradient(
            fragCoord
        );

    vec2 safeResolution = max(iResolution, vec2(0.001));
    vec2 screenUV =
        fragCoord / safeResolution;

    vec2 activeCenter =
        mix(
            u_pos + u_size * 0.5,
            u_pos2 + u_size2 * 0.5,
            u_menu_alpha
        );

    vec2 activeHalfSize =
        mix(
            u_size * 0.5,
            u_size2 * 0.5,
            u_menu_alpha
        );

    vec2 normUV =
        (fragCoord - activeCenter)
        / max(activeHalfSize, vec2(0.001));

    float dist =
        length(normUV);

    vec2 lensOffset =
        normUV
        * (1.0 - smoothstep(0.0, 1.5, dist))
        * u_lens_power;

    float heightRef =
        min(
            activeHalfSize.x,
            activeHalfSize.y
        );

    float bevelWidth =
        min(
            24.0,
            heightRef * 0.4
        );

    float bevelMask =
        smoothstep(
            -bevelWidth,
            0.0,
            sdf
        );

    vec2 bevelOffset =
        grad
        * bevelMask
        * u_bevel_power;

    vec2 finalUVOffset =
        (lensOffset - bevelOffset)
        * (mix(u_size, u_size2, u_menu_alpha) / safeResolution);

    vec2 sampleUV =
        screenUV - finalUVOffset;

    vec3 blurredTex =
        getBlurredColor(
            sampleUV,
            u_blur_amount
        );

    blurredTex =
        pow(
            blurredTex,
            vec3(0.88)
        )
        * 1.15;

    vec3 finalColor =
        mix(
            blurredTex,
            u_glass_color.rgb,
            u_glass_color.a
        );

    float innerBevel =
        smoothstep(
            -heightRef * 0.35,
            0.0,
            sdf
        )
        * 0.2;

    finalColor *=
        (1.0 - innerBevel);

    float rimMask =
        smoothstep(-3.0, -0.5, sdf)
        *
        smoothstep(0.5, -0.5, sdf);

    vec2 lightDir =
        normalize(
            vec2(-0.5, 0.85)
        );

    float NdotL =
        dot(
            grad,
            lightDir
        );

    float topLeftHighlight =
        pow(
            max(0.0, NdotL),
            2.2
        )
        *
        rimMask
        *
        1.1;

    float bottomRightHighlight =
        pow(
            max(0.0, -NdotL),
            3.0
        )
        *
        rimMask
        *
        0.75;

    float edgeStroke =
        smoothstep(
            -1.2,
            0.0,
            sdf
        )
        *
        0.25;

    finalColor +=
        vec3(1.0)
        *
        (
            topLeftHighlight
            + bottomRightHighlight
            + edgeStroke
        )
        *
        u_border_opacity;

    if (u_pressed > 0.001) {
        vec3 pressedGlassColor =
            mix(
                finalColor,
                vec3(0.25, 0.55, 1.0),
                0.25
            );

        finalColor =
            mix(
                finalColor,
                pressedGlassColor,
                u_pressed
            );

        float lightRadius =
            max(
                u_size.x,
                u_size.y
            )
            *
            0.85;

        float spot =
            smoothstep(
                lightRadius,
                0.0,
                length(
                    fragCoord
                    - u_touch_pos
                )
            );

        finalColor =
            mix(
                finalColor,
                vec3(1.0),
                spot
                * u_pressed
                * 0.35
            );
    }

    float edgeAlpha =
        smoothstep(
            aa,
            -aa,
            sdf
        );

    gl_FragColor =
        vec4(
            finalColor,
            edgeAlpha
        )
        *
        frag_color.a;
}