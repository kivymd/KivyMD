#ifdef GL_ES
precision mediump float;
#endif

varying vec4 frag_color;
uniform vec4 u_radius;
uniform vec4 u_glass_color;

uniform sampler2D texture0;

uniform vec2 iResolution;
uniform vec2 u_pos;
uniform vec2 u_size;
varying vec2 tex_coord0;
uniform vec2 u_touch_pos;

uniform float u_pressed;
uniform float u_blur_amount;

// ------------------------------------------------------------
// SDF for rounded rectangle.
// ------------------------------------------------------------

float sdRoundedRect(
    vec2 pos,
    vec2 halfSize,
    vec4 cornerRadius
) {
    float maxRadius = min(halfSize.x, halfSize.y);

    cornerRadius = min(
        cornerRadius,
        vec4(maxRadius)
    );

    float r = (pos.x > 0.0)
        ? ((pos.y > 0.0)
            ? cornerRadius.y
            : cornerRadius.z)
        : ((pos.y > 0.0)
            ? cornerRadius.x
            : cornerRadius.w);

    vec2 q = abs(pos) - halfSize + r;

    return min(max(q.x, q.y), 0.0)
         + length(max(q, 0.0))
         - r;
}

// ------------------------------------------------------------
// SDF normal gradient.
// ------------------------------------------------------------

vec2 getSDFGradient(
    vec2 pos,
    vec2 halfSize,
    vec4 radius
) {
    vec2 eps = vec2(0.5, 0.0);

    float dx =
        sdRoundedRect(
            pos + eps.xy,
            halfSize,
            radius
        )
        -
        sdRoundedRect(
            pos - eps.xy,
            halfSize,
            radius
        );

    float dy =
        sdRoundedRect(
            pos + eps.yx,
            halfSize,
            radius
        )
        -
        sdRoundedRect(
            pos - eps.yx,
            halfSize,
            radius
        );

    return normalize(
        vec2(dx, dy) + vec2(0.0001)
    );
}

// ------------------------------------------------------------
// Deep lens blur.
// ------------------------------------------------------------

vec3 getBlurredColor(
    vec2 uv,
    float blurAmount
) {
    vec3 col = vec3(0.0);

    vec2 radius =
        vec2(blurAmount)
        / iResolution;

    const float SAMPLES = 16.0;
    const float GOLDEN_ANGLE = 2.3999632;

    for (float i = 0.0; i < SAMPLES; i += 1.0) {

        float r =
            sqrt((i + 0.5) / SAMPLES);

        float theta =
            i * GOLDEN_ANGLE;

        vec2 offset =
            vec2(
                cos(theta),
                sin(theta)
            )
            * r
            * radius;

        col += texture2D(
            texture0,
            uv + offset
        ).rgb;
    }

    return col / SAMPLES;
}

// ------------------------------------------------------------
// Main.
// ------------------------------------------------------------

void main() {

    vec2 fragCoord =
        gl_FragCoord.xy;

    vec2 center =
        u_pos + u_size * 0.5;

    vec2 halfSize =
        u_size * 0.5;

    vec2 centeredUV =
        fragCoord - center;

    // --------------------------------------------------------
    // Rounded rectangle.
    // --------------------------------------------------------

    float sdf =
        sdRoundedRect(
            centeredUV,
            halfSize,
            u_radius
        );

    // --------------------------------------------------------
    // Rounded rectangle & Anti-Aliasing (AA).
    // --------------------------------------------------------

    if (sdf > 1.5) {
        discard;
    }

    float aa = fwidth(sdf);
    if (aa < 0.001) aa = 1.0;

    // --------------------------------------------------------
    // SDF normal.
    // --------------------------------------------------------

    vec2 grad =
        getSDFGradient(
            centeredUV,
            halfSize,
            u_radius
        );

    // --------------------------------------------------------
    // Liquid/lens distortion.
    // --------------------------------------------------------

    float heightRef =
        min(
            halfSize.x,
            halfSize.y
        );

    float normalizedInside =
        clamp(
            -sdf / heightRef,
            0.0,
            1.0
        );

    // --------------------------------------------------------
    // Rounded-corner mask.
    // --------------------------------------------------------

    float radius =
        min(
            min(u_radius.x, u_radius.y),
            min(u_radius.z, u_radius.w)
        );

    float cornerStartX =
        halfSize.x - radius;

    float cornerStartY =
        halfSize.y - radius;

    float cornerX =
        smoothstep(
            cornerStartX,
            halfSize.x,
            abs(centeredUV.x)
        );

    float cornerY =
        smoothstep(
            cornerStartY,
            halfSize.y,
            abs(centeredUV.y)
        );

    float cornerFactor =
        cornerX * cornerY;

    // --------------------------------------------------------
    // Refraction attenuation.
    // --------------------------------------------------------

    float cornerRefraction =
        mix(
            1.0,
            0.22,
            cornerFactor
        );

    // --------------------------------------------------------
    // Liquid refraction.
    // --------------------------------------------------------

    vec2 refractOffset =
        grad
        * (
            pow(normalizedInside, 2.0)
            * -0.004
            * cornerRefraction
        );

    vec2 sampleUV =
        (fragCoord / iResolution.xy)
        + refractOffset;

    // --------------------------------------------------------
    // Blurred background.
    // --------------------------------------------------------

    vec3 blurredTex =
        getBlurredColor(
            sampleUV,
            u_blur_amount
        );

    // --------------------------------------------------------
    // Liquid glass light/contrast.
    // --------------------------------------------------------

    blurredTex =
        pow(
            blurredTex,
            vec3(0.85)
        ) * 1.15;

    // --------------------------------------------------------
    // Glass tint.
    // --------------------------------------------------------

    vec3 finalColor =
        mix(
            blurredTex,
            u_glass_color.rgb,
            u_glass_color.a * 0.4
        );

    // --------------------------------------------------------
    // iOS 18 Glass Rim & Specular Highlights.
    // --------------------------------------------------------

    float rimMask =
        smoothstep(
            -2.8,
            0.0,
            sdf
        ) * smoothstep(0.5, -0.5, sdf);

    vec2 lightDir =
        normalize(
            vec2(-0.6, 0.8)
        );

    float NdotL =
        dot(
            grad,
            lightDir
        );

    float topLeftHighlight =
        pow(
            max(
                0.0,
                NdotL
            ),
            2.5
        ) * rimMask * 0.9;

    float bottomRightHighlight =
        pow(
            max(
                0.0,
                -NdotL
            ),
            3.5
        ) * rimMask * 0.75;

    float edgeStroke =
        smoothstep(
            -1.2,
            0.0,
            sdf
        ) * 0.25;

    finalColor +=
        vec3(1.0)
        * (
            topLeftHighlight
            + bottomRightHighlight
            + edgeStroke
        );

    // --------------------------------------------------------
    // Click/pressed interaction.
    // --------------------------------------------------------

    vec3 pressedGlassColor =
        mix(
            finalColor,
            vec3(
                0.2,
                0.5,
                1.0
            ),
            0.25
        );

    finalColor =
        mix(
            finalColor,
            pressedGlassColor,
            u_pressed
        );

    // --------------------------------------------------------
    // Finger/cursor glare.
    // --------------------------------------------------------

    float lightRadius =
        max(
            u_size.x,
            u_size.y
        ) * 0.85;

    float distToTouch =
        length(
            fragCoord - u_touch_pos
        );

    float spot =
        smoothstep(
            lightRadius,
            0.0,
            distToTouch
        );

    finalColor =
        mix(
            finalColor,
            vec3(1.0),
            spot
            * u_pressed
            * 0.35
        );

    // --------------------------------------------------------
    // Smooth Edge Alpha (Subpixel Anti-Aliasing).
    // --------------------------------------------------------

    float edgeAlpha = smoothstep(aa, -aa, sdf);

    gl_FragColor =
        vec4(
            finalColor,
            edgeAlpha
        )
        * frag_color.a;
}
