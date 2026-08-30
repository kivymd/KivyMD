/*
 * ============================================================================
 * Liquid Glass UI Fragment Shader (iOS-Style Refraction & Blur)
 * ============================================================================
 *
 * Description:
 *   Renders an interactive glassmorphic UI element with dynamic physical
 *   effects including:
 *     1. Signed Distance Field (SDF) rounded rectangle clipping with AA.
 *     2. Golden angle multi-sample Gaussian/disk background blur.
 *     3. Dual-mode refraction:
 *        - Central magnification (lens power / bulge).
 *        - Edge/bevel normal displacement based on SDF spatial gradient.
 *     4. Procedural lighting: directional rim highlights and bevel shadows.
 *     5. Touch response: dynamic spot highlight and tinting on press.
 *
 * Uniforms:
 *   - sampler2D texture0     : Framebuffer object (FBO) background texture.
 *   - vec2 iResolution       : Screen resolution in pixels (Window.size).
 *   - vec2 u_pos             : Widget bottom-left position in screen coordinates.
 *   - vec2 u_size            : Widget dimensions (width, height).
 *   - vec4 u_radius          : Corner radii (top-left, top-right, bottom-right, bottom-left).
 *   - vec4 u_glass_color     : Base tint color and opacity (RGBA).
 *   - float u_blur_amount    : Background blur kernel radius.
 *   - float u_lens_power     : Central magnification factor (0.0 = flat).
 *   - float u_bevel_power    : Edge refraction intensity along the SDF gradient.
 *   - float u_pressed        : Touch press factor (0.0 to 1.0) for interaction.
 *   - vec2 u_touch_pos       : Current touch coordinates on screen.
 * ============================================================================
 */

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

// Dynamic uniforms for lens control
uniform float u_lens_power;
uniform float u_bevel_power;

// ------------------------------------------------------------
// Signed Distance Field (SDF) for a rounded rectangle.
// ------------------------------------------------------------

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

// ------------------------------------------------------------
// SDF normal gradient via central differences.
// ------------------------------------------------------------

vec2 getSDFGradient(
    vec2 pos,
    vec2 halfSize,
    vec4 radius
) {
    vec2 eps =
        vec2(0.5, 0.0);

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

    return
        normalize(
            vec2(dx, dy)
            + vec2(0.0001)
        );
}

// ------------------------------------------------------------
// Multi-sample golden angle disk blur.
// ------------------------------------------------------------

vec3 getBlurredColor(
    vec2 uv,
    float blurAmount
) {
    vec2 radius =
        vec2(blurAmount)
        / iResolution;

    const float SAMPLES = 16.0;
    const float GOLDEN_ANGLE = 2.3999632;

    vec3 col = vec3(0.0);

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

        col +=
            texture2D(
                texture0,
                uv + offset
            ).rgb;
    }

    return col / SAMPLES;
}

// ------------------------------------------------------------
// Main execution loop.
// ------------------------------------------------------------

void main() {
    vec2 fragCoord =
        gl_FragCoord.xy;

    vec2 center =
        u_pos
        + u_size * 0.5;

    vec2 halfSize =
        u_size * 0.5;

    vec2 centeredUV =
        fragCoord - center;

    // --------------------------------------------------------
    // Signed Distance Field & Anti-Aliasing (AA).
    // --------------------------------------------------------

    float sdf =
        sdRoundedRect(
            centeredUV,
            halfSize,
            u_radius
        );

    if (sdf > 1.5) {
        discard;
    }

    float aa =
        fwidth(sdf);

    if (aa < 0.001) {
        aa = 1.0;
    }

    vec2 grad =
        getSDFGradient(
            centeredUV,
            halfSize,
            u_radius
        );

    // --------------------------------------------------------
    // Spherical Lens Distortion & Edge Refraction.
    // --------------------------------------------------------

    vec2 screenUV =
        fragCoord / iResolution.xy;

    vec2 normButtonUV =
        centeredUV / halfSize;

    float dist =
        length(normButtonUV);

    // 1. Central magnification effect (bulge)
    vec2 lensOffset =
        normButtonUV
        * (
            1.0
            - smoothstep(0.0, 1.5, dist)
        )
        * u_lens_power;

    // 2. Bevel edge refraction
    float heightRef =
        min(
            halfSize.x,
            halfSize.y
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
        * (u_size / iResolution);

    vec2 sampleUV =
        screenUV - finalUVOffset;

    // --------------------------------------------------------
    // Background Sampling & Tone Adjustment.
    // --------------------------------------------------------

    vec3 blurredTex =
        getBlurredColor(
            sampleUV,
            u_blur_amount
        );

    blurredTex =
        pow(
            blurredTex,
            vec3(0.88)
        ) * 1.15;

    vec3 finalColor =
        mix(
            blurredTex,
            u_glass_color.rgb,
            u_glass_color.a * 0.4
        );

    // --------------------------------------------------------
    // Bevel Shadow & Specular Rim Highlights.
    // --------------------------------------------------------

    float innerBevel =
        smoothstep(
            -heightRef * 0.35,
            0.0,
            sdf
        ) * 0.2;

    finalColor *= (1.0 - innerBevel);

    float rimMask =
        smoothstep(
            -3.0,
            -0.5,
            sdf
        )
        * smoothstep(
            0.5,
            -0.5,
            sdf
        );

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
        * rimMask
        * 1.1;

    float bottomRightHighlight =
        pow(
            max(0.0, -NdotL),
            3.0
        )
        * rimMask
        * 0.75;

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
    // Touch Interaction Highlights.
    // --------------------------------------------------------

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
        ) * 0.85;

    float spot =
        smoothstep(
            lightRadius,
            0.0,
            length(fragCoord - u_touch_pos)
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
    // Alpha Compositing.
    // --------------------------------------------------------

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
        * frag_color.a;
}
