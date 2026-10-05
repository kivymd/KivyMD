/*
 * ============================================================================
 * Liquid Dropdown Glass UI Fragment Shader
 * ============================================================================
 *
 * Description:
 *   Fragment shader for an iOS-style liquid glass Dropdown component.
 *
 * Main effects:
 *
 *   1. Rounded Rectangle SDF
 *      Describes the button and menu geometry mathematically.
 *   2. Smooth Minimum (smin)
 *      Smoothly blends the button and menu into a single liquid shape.
 *   3. Procedural Wobble / Ripple
 *      Adds dynamic deformation to the liquid boundary during expansion.
 *   4. Background Blur
 *      Samples and blurs the framebuffer behind the glass surface.
 *   5. Lens Refraction
 *      Creates a central magnification effect through the glass.
 *   6. Bevel Refraction
 *      Displaces the background along the SDF surface normal,
 *      simulating refraction around the glass edges.
 *   7. Procedural Lighting
 *      Adds directional highlights, edge lighting, and bevel shading.
 *   8. Touch Response
 *      Adds a pressed-state tint and a dynamic highlight around
 *      the current touch position.
 *
 * ============================================================================
 *
 * Uniforms:
 *   - sampler2D texture0     : Framebuffer object (FBO) background texture.
 *   - vec2 iResolution       : Screen/framebuffer resolution in pixels.
 *   - vec2 u_pos             : Trigger button bottom-left position in screen coordinates.
 *   - vec2 u_size            : Trigger button dimensions (width, height).
 *   - vec4 u_radius          : Trigger button corner radii.
 *   - vec2 u_pos2            : Dropdown menu bottom-left position in screen coordinates.
 *   - vec2 u_size2           : Dropdown menu dimensions (width, height).
 *   - vec4 u_radius2         : Dropdown menu corner radii.
 *   - float u_k              : Smooth-minimum blending radius for liquid connection.
 *   - float u_menu_alpha     : Dropdown expansion progress (0.0 = closed, 1.0 = fully expanded).
 *   - float u_wobble         : External liquid deformation impulse.
 *   - float u_time           : Global animation time.
 *   - vec4 u_glass_color     : Base glass tint color and opacity (RGBA).
 *   - float u_blur_amount    : Background blur kernel radius.
 *   - float u_lens_power     : Central magnification/refraction intensity (0.0 = flat).
 *   - float u_bevel_power    : Edge refraction intensity along the SDF gradient.
 *   - float u_border_opacity : Opacity of the procedural border lighting (0.0 to 1.0).
 *   - float u_pressed        : Touch press factor (0.0 to 1.0) for interaction.
 *   - vec2 u_touch_pos       : Current touch coordinates in screen space.
 *
 * ============================================================================
 */

#ifdef GL_ES

/*
 * fwidth() is used for analytical SDF anti-aliasing.
 *
 * Some OpenGL ES implementations require the standard derivatives
 * extension to be explicitly enabled.
 */
#extension GL_OES_standard_derivatives : enable

/*
 * Medium precision is used for OpenGL ES compatibility.
 */
precision mediump float;

#endif

/*
 * Vertex color passed through the rendering pipeline.
 *
 * The final alpha value is multiplied by frag_color.a.
 */
varying vec4 frag_color;

/* ============================================================================
 * BACKGROUND / SCREEN
 * ========================================================================== */

/*
 * Framebuffer texture containing the content behind the glass.
 */
uniform sampler2D texture0;

/*
 * Screen / framebuffer resolution in pixels:
 *
 *     x = width
 *     y = height
 */
uniform vec2 iResolution;

/* ============================================================================
 * SOURCE BUTTON
 * ========================================================================== */

/*
 * Bottom-left position of the original trigger button.
 */
uniform vec2 u_pos;

/*
 * Size of the original trigger button:
 *
 *     x = width
 *     y = height
 */
uniform vec2 u_size;

/*
 * Corner radii of the original trigger button.
 */
uniform vec4 u_radius;

/* ============================================================================
 * DROPDOWN MENU
 * ========================================================================== */

/*
 * Bottom-left position of the expanded dropdown menu.
 */
uniform vec2 u_pos2;

/*
 * Size of the expanded dropdown menu.
 */
uniform vec2 u_size2;

/*
 * Corner radii of the expanded dropdown menu.
 */
uniform vec4 u_radius2;

/* ============================================================================
 * LIQUID / ANIMATION
 * ========================================================================== */

/*
 * Smooth-minimum blending radius.
 *
 * Larger values create a wider liquid connection between the
 * button and the dropdown menu.
 */
uniform float u_k;

/*
 * Dropdown expansion progress:
 *
 *     0.0 = closed
 *     1.0 = fully expanded
 */
uniform float u_menu_alpha;

/*
 * External liquid deformation impulse.
 */
uniform float u_wobble;

/*
 * Global animation timer.
 */
uniform float u_time;

/* ============================================================================
 * GLASS PROPERTIES
 * ========================================================================== */

/*
 * Glass tint:
 *
 *     rgb = tint color
 *     a   = tint strength
 */
uniform vec4 u_glass_color;

/*
 * Background blur radius in pixels.
 */
uniform float u_blur_amount;

/*
 * Central lens / magnification strength.
 */
uniform float u_lens_power;

/*
 * Edge / bevel refraction strength.
 */
uniform float u_bevel_power;

/*
 * Procedural border lighting opacity.
 */
uniform float u_border_opacity;


/* ============================================================================
 * TOUCH RESPONSE
 * ========================================================================== */

/*
 * Pressed-state interpolation:
 *
 *     0.0 = released
 *     1.0 = fully pressed
 */
uniform float u_pressed;

/*
 * Current touch position in screen coordinates.
 */
uniform vec2 u_touch_pos;

/* ============================================================================
 * SIGNED DISTANCE FIELD
 * ============================================================================
 *
 * Returns the signed distance from a point to a rounded rectangle.
 *
 * Result:
 *
 *     sdf < 0.0  -> inside the shape
 *     sdf = 0.0  -> exactly on the boundary
 *     sdf > 0.0  -> outside the shape
 *
 * SDF allows the entire dropdown geometry to be generated
 * procedurally inside the fragment shader.
 * ========================================================================== */

float sdRoundedRect(
    vec2 pos,
    vec2 halfSize,
    vec4 cornerRadius
) {
    /*
     * The maximum possible corner radius is limited by
     * the smallest half-dimension of the rectangle.
     *
     * This prevents the radius from exceeding the shape itself.
     */
    float maxRadius =
        min(
            halfSize.x,
            halfSize.y
        );

    /*
     * Clamp all four corner radii to the maximum valid radius.
     */
    cornerRadius =
        min(
            cornerRadius,
            vec4(maxRadius)
        );

    /*
     * Select the corner radius according to the quadrant
     * containing the current point.
     *
     *     x > 0, y > 0 -> top-right
     *     x < 0, y > 0 -> top-left
     *     x > 0, y < 0 -> bottom-right
     *     x < 0, y < 0 -> bottom-left
     */
    float r =
        (pos.x > 0.0)
            ? ((pos.y > 0.0)
                ? cornerRadius.y
                : cornerRadius.z)
            : ((pos.y > 0.0)
                ? cornerRadius.x
                : cornerRadius.w);

    /*
     * Standard rounded-rectangle SDF construction.
     */
    vec2 q =
        abs(pos)
        - halfSize
        + r;

    /*
     * The first term describes the inner rectangular region.
     *
     * The second term describes the rounded outer region.
     */
    return
        min(
            max(q.x, q.y),
            0.0
        )
        + length(max(q, 0.0))
        - r;
}

/* ============================================================================
 * SMOOTH MINIMUM
 * ============================================================================
 *
 * A regular min(a, b) produces a hard intersection between two SDFs.
 *
 * smin() replaces that hard intersection with a smooth transition,
 * creating the liquid connection between the button and menu.
 * ========================================================================== */

float smin(
    float a,
    float b,
    float k
) {
    /*
     * When k is almost zero, the regular minimum is sufficient.
     */
    if (k <= 0.0001) return min(a, b);

    /*
     * Interpolation factor controlling the smooth transition
     * between the two SDF values.
     */
    float h =
        clamp(
            0.5 + 0.5 * (b - a) / k,
            0.0,
            1.0
        );

    /*
     * Polynomial smooth-minimum operation.
     */
    return
        mix(b, a, h)
        - k * h * (1.0 - h);
}

/* ============================================================================
 * GLOBAL SDF
 * ============================================================================
 *
 * Builds the complete dropdown geometry.
 *
 * The function:
 *
 *     1. Builds the trigger button SDF.
 *     2. Builds the dropdown menu SDF.
 *     3. Interpolates their positions and sizes.
 *     4. Applies procedural liquid deformation.
 *     5. Blends both shapes using smooth-minimum.
 * ========================================================================== */

float mapSDF(
    vec2 fragCoord
) {
    /* ------------------------------------------------------------------------
     * SOURCE BUTTON GEOMETRY
     * ---------------------------------------------------------------------- */

    /*
     * Calculate the center of the original button.
     */
    vec2 center1 =
        u_pos
        + u_size * 0.5;

    /*
     * Convert the button size to half-size.
     */
    vec2 halfSize1 =
        u_size * 0.5;

    /*
     * During expansion, the original button gradually shrinks.
     *
     *     alpha = 0.0 -> original size
     *     alpha = 1.0 -> zero size
     */
    vec2 currentButtonHalfSize =
        mix(
            halfSize1,
            vec2(0.0),
            u_menu_alpha
        );

    /*
     * Calculate the SDF of the trigger button.
     */
    float sdf1 =
        sdRoundedRect(
            fragCoord - center1,
            currentButtonHalfSize,
            u_radius
        );

    /* ------------------------------------------------------------------------
     * DROPDOWN MENU GEOMETRY
     * ---------------------------------------------------------------------- */

    /*
     * Calculate the final center of the dropdown menu.
     */
    vec2 targetCenter =
        u_pos2
        + u_size2 * 0.5;

    /*
     * Calculate the final half-size of the dropdown menu.
     */
    vec2 targetHalfSize =
        u_size2 * 0.5;

    /*
     * Interpolate the menu center from the trigger button
     * to the final dropdown position.
     */
    vec2 currentMenuCenter =
        mix(
            center1,
            targetCenter,
            u_menu_alpha
        );

    /*
     * The menu starts as a small shape and grows
     * toward its final dimensions.
     */
    vec2 currentMenuHalfSize =
        mix(
            halfSize1 * 0.2,
            targetHalfSize,
            u_menu_alpha
        );

    /*
     * Interpolate the corner radii from the button
     * to the final menu geometry.
     */
    vec4 currentRadius =
        mix(
            u_radius,
            u_radius2,
            u_menu_alpha
        );

    /*
     * Calculate the SDF of the interpolated menu shape.
     */
    float sdf2 =
        sdRoundedRect(
            fragCoord - currentMenuCenter,
            currentMenuHalfSize,
            currentRadius
        );

    /* ------------------------------------------------------------------------
     * ACTIVE CENTER
     * ---------------------------------------------------------------------- */

    /*
     * Current center of the moving liquid shape.
     */
    vec2 activeCenter =
        mix(
            center1,
            targetCenter,
            u_menu_alpha
        );

    /*
     * Vector from the active center to the current fragment.
     */
    vec2 dir =
        fragCoord - activeCenter;

    /*
     * Polar angle of the current fragment.
     *
     * Used to generate the procedural radial ripple.
     */
    float angle =
        atan(dir.y, dir.x);

    /* ------------------------------------------------------------------------
     * SNAP INTENSITY
     * ---------------------------------------------------------------------- */

    /*
     * The sine curve reaches its maximum around the middle
     * of the expansion animation.
     *
     *     alpha = 0.0 -> 0
     *     alpha = 0.5 -> maximum
     *     alpha = 1.0 -> 0
     */
    float snapIntensity =
        smoothstep(
            0.0,
            1.0,
            sin(u_menu_alpha * 3.14159265)
        )
        *
        /*
         * Additional dependency on the smooth-minimum factor.
         *
         * This increases the snap effect while the liquid
         * connection is being released.
         */
        smoothstep(
            u_k,
            0.0,
            u_k * 0.5
        );

    /* ------------------------------------------------------------------------
     * PROCEDURAL RIPPLE
     * ---------------------------------------------------------------------- */

    /*
     * Combine two angular waves with different frequencies
     * and animation speeds.
     *
     * Their product produces a non-uniform liquid deformation.
     */
    float ripple =
        sin(angle * 5.0 + u_time * 30.0)
        *
        cos(angle * 3.0 - u_time * 20.0);

    /*
     * Combine the externally supplied wobble impulse
     * with the automatically generated snap impulse.
     */
    float totalWobble =
        u_wobble
        + snapIntensity * 0.8;

    /*
     * Convert the normalized ripple into an SDF displacement.
     */
    float dropWobble =
        ripple
        * totalWobble
        * 8.0;

    /*
     * Apply the same deformation to both shapes
     * so their boundaries move consistently.
     */
    sdf1 += dropWobble;
    sdf2 += dropWobble;

    /* ------------------------------------------------------------------------
     * FINAL SHAPE
     * ---------------------------------------------------------------------- */

    /*
     * Once fully expanded, use only the menu SDF.
     */
    if (u_menu_alpha >= 0.999) return sdf2;

    /*
     * Once fully closed, use only the button SDF.
     */
    if (u_menu_alpha <= 0.001) return sdf1;

    /*
     * During the transition, smoothly merge both shapes.
     */
    return smin(sdf1, sdf2, u_k);
}

/* ============================================================================
 * SDF GRADIENT
 * ============================================================================
 *
 * Approximates the SDF gradient using central differences.
 *
 * The gradient points approximately in the direction of the
 * surface normal and is used for:
 *
 *     - bevel refraction
 *     - procedural lighting
 *     - rim highlights
 * ========================================================================== */

vec2 getSDFGradient(
    vec2 pos
) {
    /*
     * Numerical differentiation step.
     */
    vec2 eps =
        vec2(0.5, 0.0);

    /*
     * Derivative along the X axis.
     */
    float dx =
        mapSDF(pos + eps.xy)
        - mapSDF(pos - eps.xy);

    /*
     * Derivative along the Y axis.
     */
    float dy =
        mapSDF(pos + eps.yx)
        - mapSDF(pos - eps.yx);

    /*
     * Normalize the resulting gradient to obtain
     * an approximate surface normal.
     *
     * The small offset prevents a zero-length vector.
     */
    return
        normalize(
            vec2(dx, dy)
            + vec2(0.0001)
        );
}

/* ============================================================================
 * GOLDEN ANGLE DISK BLUR
 * ============================================================================
 *
 * Samples the background texture around the current UV coordinate.
 *
 * Samples are distributed using the golden angle to obtain
 * relatively uniform disk coverage with a small number of texture reads.
 *
 * This provides an efficient approximation of background glass blur.
 * ========================================================================== */

vec3 getBlurredColor(
    vec2 uv,
    float blurAmount
) {
    /*
     * Convert the blur radius from pixels to normalized UV coordinates.
     */
    vec2 radius =
        vec2(blurAmount)
        / iResolution;

    /*
     * Number of texture samples.
     *
     * Increasing this value improves blur quality
     * at the cost of shader performance.
     */
    const float SAMPLES = 16.0;

    /*
     * Golden angle in radians.
     *
     * This distributes samples evenly around the disk.
     */
    const float GOLDEN_ANGLE = 2.3999632;

    /*
     * Accumulated RGB color.
     */
    vec3 col = vec3(0.0);

    /*
     * Generate the individual blur samples.
     */
    for (float i = 0.0; i < SAMPLES; i += 1.0) {

        /*
         * sqrt() produces an approximately uniform distribution
         * across the disk area instead of concentrating samples
         * near the center.
         */
        float r =
            sqrt((i + 0.5) / SAMPLES);

        /*
         * Current angular position.
         */
        float theta =
            i * GOLDEN_ANGLE;

        /*
         * Calculate the current sample offset.
         */
        vec2 offset =
            vec2(
                cos(theta),
                sin(theta)
            )
            * r
            * radius;

        /*
         * Sample the framebuffer at the offset position.
         */
        col +=
            texture2D(
                texture0,
                uv + offset
            ).rgb;
    }

    /*
     * Average all samples.
     */
    return col / SAMPLES;
}

/* ============================================================================
 * MAIN
 * ========================================================================== */

void main() {

    /*
     * Current fragment position in screen pixels.
     */
    vec2 fragCoord =
        gl_FragCoord.xy;

    /* ------------------------------------------------------------------------
     * SDF
     * ---------------------------------------------------------------------- */

    /*
     * Calculate the signed distance to the complete liquid shape.
     */
    float sdf =
        mapSDF(fragCoord);

    /*
     * Discard fragments that are sufficiently far outside
     * the SDF boundary.
     *
     * The small 1.5-pixel margin preserves the anti-aliased edge.
     */
    if (sdf > 1.5) {
        discard;
    }


    /* ------------------------------------------------------------------------
     * ANTI-ALIASING
     * ---------------------------------------------------------------------- */

    /*
     * Estimate how quickly the SDF changes across neighboring fragments.
     *
     * This is used to create a smooth SDF edge.
     */
    float aa =
        fwidth(sdf);

    /*
     * Protect against extremely small derivative values.
     */
    if (aa < 0.001) aa = 1.0;

    /* ------------------------------------------------------------------------
     * SURFACE NORMAL
     * ---------------------------------------------------------------------- */

    /*
     * Calculate the approximate surface normal from the SDF gradient.
     */
    vec2 grad =
        getSDFGradient(fragCoord);

    /* ------------------------------------------------------------------------
     * SCREEN UV
     * ---------------------------------------------------------------------- */

    /*
     * Convert pixel coordinates to normalized texture coordinates.
     *
     *     (0, 0) -> bottom-left
     *     (1, 1) -> top-right
     */
    vec2 screenUV =
        fragCoord / iResolution.xy;

    /* ------------------------------------------------------------------------
     * ACTIVE GEOMETRY
     * ---------------------------------------------------------------------- */

    /*
     * Interpolate the active shape center between the
     * trigger button and the final dropdown menu.
     */
    vec2 activeCenter =
        mix(
            u_pos + u_size * 0.5,
            u_pos2 + u_size2 * 0.5,
            u_menu_alpha
        );

    /*
     * Interpolate the active half-size between the
     * trigger button and the final dropdown menu.
     */
    vec2 activeHalfSize =
        mix(
            u_size * 0.5,
            u_size2 * 0.5,
            u_menu_alpha
        );

    /* ------------------------------------------------------------------------
     * NORMALIZED POSITION
     * ---------------------------------------------------------------------- */

    /*
     * Calculate the fragment position relative to the active center.
     *
     * The result is normalized by the current shape dimensions
     * and is used for the central lens effect.
     */
    vec2 normUV =
        (fragCoord - activeCenter)
        / max(activeHalfSize, vec2(1.0));

    /* ------------------------------------------------------------------------
     * CENTRAL LENS REFRACTION
     * ---------------------------------------------------------------------- */

    /*
     * Create a lens-shaped displacement.
     *
     * The effect is strongest near the center and gradually
     * disappears toward the outer region.
     */
    vec2 lensOffset =
        normUV
        *
        (1.0 - smoothstep(
            0.0,
            1.5,
            length(normUV)
        ))
        *
        u_lens_power;

    /* ------------------------------------------------------------------------
     * BEVEL REFRACTION
     * ---------------------------------------------------------------------- */

    /*
     * Use the smaller dimension as a reference for bevel thickness.
     */
    float heightRef =
        min(
            activeHalfSize.x,
            activeHalfSize.y
        );

    /*
     * Limit the bevel width to prevent excessive edge distortion.
     */
    float bevelWidth =
        min(
            24.0,
            heightRef * 0.4
        );

    /*
     * Create a mask that is strongest near the SDF boundary.
     *
     *     sdf < 0 -> inside the shape
     *     sdf = 0 -> boundary
     */
    float bevelMask =
        smoothstep(
            -bevelWidth,
            0.0,
            sdf
        );

    /*
     * Displace the background along the surface normal.
     *
     * This simulates light refraction through the rounded glass edge.
     */
    vec2 bevelOffset =
        grad
        * bevelMask
        * u_bevel_power;

    /* ------------------------------------------------------------------------
     * FINAL REFRACTION OFFSET
     * ---------------------------------------------------------------------- */

    /*
     * Combine central lens displacement with bevel displacement.
     *
     * The resulting pixel displacement is converted from
     * screen pixels into normalized texture coordinates.
     */
    vec2 finalUVOffset =
        (lensOffset - bevelOffset)
        *
        (mix(u_size, u_size2, u_menu_alpha) / iResolution);

    /*
     * Apply the refraction offset to the framebuffer sample position.
     */
    vec2 sampleUV =
        screenUV - finalUVOffset;

    /* ------------------------------------------------------------------------
     * BACKGROUND BLUR
     * ---------------------------------------------------------------------- */

    /*
     * Sample the framebuffer using the golden-angle blur kernel.
     */
    vec3 blurredTex =
        getBlurredColor(
            sampleUV,
            u_blur_amount
        );

    /*
     * Apply a mild gamma / brightness adjustment
     * to compensate for the blurred background.
     */
    blurredTex =
        pow(
            blurredTex,
            vec3(0.88)
        )
        * 1.15;

    /* ------------------------------------------------------------------------
     * GLASS TINT
     * ---------------------------------------------------------------------- */

    /*
     * Blend the blurred background with the glass tint.
     *
     * u_glass_color.a controls how strongly the glass tint
     * replaces the background.
     */
    vec3 finalColor =
        mix(
            blurredTex,
            u_glass_color.rgb,
            u_glass_color.a
        );

    /* ------------------------------------------------------------------------
     * INNER BEVEL SHADOW
     * ---------------------------------------------------------------------- */

    /*
     * Generate a soft darkening effect near the inner edge.
     *
     * This gives the glass surface a sense of thickness.
     */
    float innerBevel =
        smoothstep(
            -heightRef * 0.35,
            0.0,
            sdf
        )
        * 0.2;

    /*
     * Apply the inner bevel shading.
     */
    finalColor *=
        (1.0 - innerBevel);

    /* ------------------------------------------------------------------------
     * RIM LIGHT
     * ---------------------------------------------------------------------- */

    /*
     * Generate a narrow mask around the SDF boundary.
     *
     * This mask is used by the procedural edge lighting.
     */
    float rimMask =
        smoothstep(-3.0, -0.5, sdf)
        *
        smoothstep(0.5, -0.5, sdf);

    /* ------------------------------------------------------------------------
     * LIGHT DIRECTION
     * ---------------------------------------------------------------------- */

    /*
     * Direction of the virtual light source.
     *
     * The light comes primarily from the upper-left direction.
     */
    vec2 lightDir =
        normalize(
            vec2(-0.5, 0.85)
        );

    /*
     * Calculate the alignment between the surface normal
     * and the light direction.
     */
    float NdotL =
        dot(
            grad,
            lightDir
        );

    /* ------------------------------------------------------------------------
     * TOP-LEFT HIGHLIGHT
     * ---------------------------------------------------------------------- */

    /*
     * Highlight the side of the glass facing the light.
     *
     * The power function controls the sharpness of the highlight.
     */
    float topLeftHighlight =
        pow(
            max(0.0, NdotL),
            2.2
        )
        *
        rimMask
        *
        1.1;

    /* ------------------------------------------------------------------------
     * BOTTOM-RIGHT HIGHLIGHT
     * ---------------------------------------------------------------------- */

    /*
     * Add a weaker highlight on the opposite side
     * to simulate secondary reflected light.
     */
    float bottomRightHighlight =
        pow(
            max(0.0, -NdotL),
            3.0
        )
        *
        rimMask
        *
        0.75;

    /* ------------------------------------------------------------------------
     * EDGE STROKE
     * ---------------------------------------------------------------------- */

    /*
     * Add a thin procedural light stroke directly around
     * the SDF boundary.
     */
    float edgeStroke =
        smoothstep(
            -1.2,
            0.0,
            sdf
        )
        *
        0.25;

    /*
     * Combine the procedural lighting components.
     *
     * u_border_opacity controls the overall intensity
     * of the generated border lighting.
     */
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

    /* =========================================================================
     * TOUCH / PRESSED EFFECT
     * ========================================================================= */

    /*
     * Apply the touch effect only while the component is pressed.
     */
    if (u_pressed > 0.001) {

        /*
         * Generate the pressed-state glass color.
         *
         * The current glass color is mixed with a blue tint.
         */
        vec3 pressedGlassColor =
            mix(
                finalColor,
                vec3(0.25, 0.55, 1.0),
                0.25
            );

        /*
         * Interpolate toward the pressed-state color
         * according to the current press amount.
         */
        finalColor =
            mix(
                finalColor,
                pressedGlassColor,
                u_pressed
            );

        /*
         * Radius of the touch highlight.
         *
         * It is based on the largest dimension of the trigger button.
         */
        float lightRadius =
            max(
                u_size.x,
                u_size.y
            )
            *
            0.85;

        /*
         * Calculate the distance between the current fragment
         * and the touch position.
         */
        float spot =
            smoothstep(
                lightRadius,
                0.0,
                length(
                    fragCoord
                    - u_touch_pos
                )
            );

        /*
         * Add a soft white highlight around the touch position.
         */
        finalColor =
            mix(
                finalColor,
                vec3(1.0),
                spot
                * u_pressed
                * 0.35
            );
    }

    /* =========================================================================
     * FINAL ALPHA / ANTI-ALIASING
     * ========================================================================= */

    /*
     * Convert the signed distance into a smooth alpha mask.
     *
     * The SDF boundary is anti-aliased using the derivative
     * calculated earlier.
     */
    float edgeAlpha =
        smoothstep(
            aa,
            -aa,
            sdf
        );

    /* ------------------------------------------------------------------------
     * FINAL FRAGMENT
     * ---------------------------------------------------------------------- */

    /*
     * Output the final glass color and calculated alpha.
     *
     * frag_color.a provides an additional global alpha multiplier
     * from the Kivy rendering pipeline.
     */
    gl_FragColor =
        vec4(
            finalColor,
            edgeAlpha
        )
        *
        frag_color.a;
}
