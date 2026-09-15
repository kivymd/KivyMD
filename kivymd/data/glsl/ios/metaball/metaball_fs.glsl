#ifdef GL_ES
// Enable support for standard derivatives fwidth(), dFdx(), dFdy().
// They are used below for high-quality anti-aliased SDF contours.
#extension GL_OES_standard_derivatives : enable

#ifdef GL_FRAGMENT_PRECISION_HIGH
precision highp float;
#else
precision mediump float;
#endif
#endif

// ------------------------------------------------------------
// Kivy/RenderContext
// ------------------------------------------------------------

// Vertex color passed from the vertex shader.
varying vec4 frag_color;

// Corner radii of the primary button.
// Order corresponds to the four corners of the rounded rectangle.
uniform vec4 u_radius;

// Glass layer color.
// Alpha determines the glass tint intensity.
uniform vec4 u_glass_color;

// Texture/background located beneath the glass.
// Used to simulate blurred liquid glass.
uniform sampler2D texture0;

// ------------------------------------------------------------
// Primary button position and size
// ------------------------------------------------------------

// Framebuffer/rendering area resolution in pixels.
uniform vec2 iResolution;

// Primary button position in screen coordinates.
uniform vec2 u_pos;

// Primary button size.
uniform vec2 u_size;

// Kivy texture coordinates.
varying vec2 tex_coord0;

// ------------------------------------------------------------
// Touch/interaction
// ------------------------------------------------------------

// Touch/cursor position.
// Used to create a light highlight spot when pressed.
uniform vec2 u_touch_pos;

// 0.0 — button is not pressed.
// 1.0 — button is pressed.
uniform float u_pressed;

// ------------------------------------------------------------
// Liquid Glass parameters
// ------------------------------------------------------------

// Background texture blur radius.
uniform float u_blur_amount;

// Lens distortion strength.
// Creates an optical glass lens effect.
uniform float u_lens_power;

// Displacement strength near the bevel edge.
uniform float u_bevel_power;

// ------------------------------------------------------------
// Secondary button
//
// These parameters are required to merge two independent rounded
// rectangles into a single liquid shape.
//
// Through these, the shader knows the position of the second
// button and can compute the combined SDF of both objects.
// ------------------------------------------------------------

// Secondary button position.
uniform vec2 u_pos2;

// Secondary button size.
uniform vec2 u_size2;

// Corner radii of the secondary button.
uniform vec4 u_radius2;

// ------------------------------------------------------------
// Metaball/liquid parameters
// ------------------------------------------------------------

// Smooth union strength.
//
// Higher values:
//   - cause the two shapes to meld into each other more strongly;
//   - make the connection look more fluid/liquid.
//
// Values <= 0.0001 effectively disable the secondary button.
uniform float u_k;

// Liquid boundary wobble amplitude.
uniform float u_wobble;

// Animation time.
// Used to animate the wobble movement.
uniform float u_time;

// ============================================================
// Rounded Rectangle SDF
// ============================================================
//
// Returns the signed distance to a rounded rectangle.
//
// Result:
//
//   < 0.0  — point is inside the shape
//   = 0.0  — point is exactly on the boundary
//   > 0.0  — point is outside
//
// p — coordinate relative to the rectangle center.
// b — half-extent of the rectangle.
// r — corner radii for the four corners.
//
// SDF allows defining geometry mathematically without a
// pre-rendered texture. This is especially convenient for
// liquid/metaball effects.
// ============================================================

float sdRoundedBox(vec2 p, vec2 b, vec4 r) {

    // Select left or right corner radii based on pixel position
    // relative to center.
    r.xy = (p.x > 0.0) ? r.xy : r.zw;

    // Then select top or bottom radius.
    r.x = (p.y > 0.0) ? r.x : r.y;

    // Standard rounded rectangle SDF formula.
    vec2 q = abs(p) - b + r.x;

    return min(max(q.x, q.y), 0.0)
        + length(max(q, 0.0))
        - r.x;
}

// ============================================================
// Smooth Minimum
// ============================================================
//
// Merges two SDF shapes smoothly.
//
// Standard:
//
//     min(a, b)
//
// produces a sharp intersection line.
//
// smin() instead creates a smooth blending transition.
//
// This is the core mathematical building block for
// metaball/liquid effects.
// ============================================================

float smin(float a, float b, float k) {

    float h = clamp(
        0.5 + 0.5 * (b - a) / k,
        0.0,
        1.0
    );

    return mix(b, a, h)
        - k * h * (1.0 - h);
}

// ============================================================
// Scene SDF
// ============================================================
//
// Constructs the final scene geometry.
//
// The scene can contain:
//
//     1. primary button;
//     2. secondary button;
//     3. smooth liquid connection between them;
//     4. optional wobble animation.
//
// Final result is a single unified SDF of the entire liquid shape.
// ============================================================

float sceneSDF(vec2 fragCoord) {
    // --------------------------------------------------------
    // Primary button
    // --------------------------------------------------------

    // Primary button center.
    vec2 c1 = u_pos + u_size * 0.5;

    // Primary button half-extents.
    vec2 h1 = u_size * 0.5;

    // Primary rounded rectangle SDF.
    float d1 = sdRoundedBox(
        fragCoord - c1,
        h1,
        u_radius
    );

    // --------------------------------------------------------
    // If liquid blending is disabled, return only the primary
    // button.
    // --------------------------------------------------------

    if (u_k <= 0.0001) {
        return d1;
    }

    // --------------------------------------------------------
    // Secondary button
    // --------------------------------------------------------

    // Secondary button center.
    vec2 c2 = u_pos2 + u_size2 * 0.5;

    // Secondary button half-extents.
    vec2 h2 = u_size2 * 0.5;

    // Secondary rounded rectangle SDF.
    float d2 = sdRoundedBox(
        fragCoord - c2,
        h2,
        u_radius2
    );

    // --------------------------------------------------------
    // Distance between button centers
    // --------------------------------------------------------

    float dist = distance(c1, c2);

    // --------------------------------------------------------
    // Maximum extents of objects
    //
    // Used to determine the range where liquid blending should
    // start/end.
    // --------------------------------------------------------

    float maxR1 = max(h1.x, h1.y);
    float maxR2 = max(h2.x, h2.y);

    float contactDist = maxR1 + maxR2;

    // --------------------------------------------------------
    // Smooth union scaling factor
    //
    // When buttons are far apart:
    //
    //     kFactor -> 1
    //
    // When close to each other:
    //
    //     smooth union becomes active.
    //
    // Here kFactor controls how strongly u_k is applied.
    // --------------------------------------------------------

    float kFactor = smoothstep(
        0.0,
        contactDist * 0.5,
        dist
    );

    float effectiveK = u_k * kFactor;

    // --------------------------------------------------------
    // Combine both buttons into a single liquid shape.
    // --------------------------------------------------------

    float liquidShape = smin(
        d1,
        d2,
        effectiveK
    );

    // ========================================================
    // WOBBLE
    // ========================================================
    //
    // Additional surface wave along the liquid shape edge.
    //
    // This is not object merging, but a subtle distortion of
    // the generated boundary.
    // ========================================================

    if (abs(u_wobble) > 0.001) {

        // Center point between the two buttons.
        vec2 center = (c1 + c2) * 0.5;

        // Direction vector from the primary button to the secondary button.
        vec2 dir =
            (dist > 0.0001)
            ? normalize(c2 - c1)
            : vec2(1.0, 0.0);

        // Position of the current pixel relative to the connection center.
        vec2 relP = fragCoord - center;

        // Distance from pixel to center.
        float r = length(relP);

        if (r > 0.0001) {

            // Normalized direction from center to current pixel.
            vec2 nRelP = relP / r;

            // Alignment of pixel direction relative to inter-button direction.
            float cosTheta = dot(nRelP, dir);

            // Second harmonic.
            //
            // Uses cos(2θ) to form a wave symmetric along the connection axis.
            float harmonic = cos(
                2.0 * acos(
                    clamp(cosTheta, -1.0, 1.0)
                )
            );

            // Temporal wave equation.
            //
            // 26.0 — oscillation frequency.
            // 14.0 — spatial deformation gain.
            float wave =
                sin(u_time * 26.0)
                * u_wobble
                * harmonic
                * 14.0;

            // Deformation should concentrate primarily near the boundary edge.
            //
            // Far from the edge, edgeFactor drops towards 0.
            float edgeFactor = smoothstep(
                24.0,
                0.0,
                abs(liquidShape)
            );

            // Offset the SDF value to create a subtle trembling liquid border
            // effect.
            liquidShape -= wave * edgeFactor;
        }
    }

    return liquidShape;
}

// ============================================================
// SDF Gradient
// ============================================================
//
// Computes the approximate surface normal of the SDF.
//
// The gradient is needed for:
//
//   - bevel shading;
//   - rim lighting;
//   - determining surface direction.
//
// Central difference method:
//
//     f(x + e) - f(x - e)
//
// yields an accurate approximation of the SDF gradient derivative.
// ============================================================

vec2 getSDFGradient(vec2 pos) {

    // Derivative evaluation step in pixels.
    vec2 eps = vec2(0.5, 0.0);

    // Derivative along X.
    float dx =
        sceneSDF(pos + eps.xy)
        - sceneSDF(pos - eps.xy);

    // Derivative along Y.
    float dy =
        sceneSDF(pos + eps.yx)
        - sceneSDF(pos - eps.yx);

    // Normalized surface normal vector.
    return normalize(
        vec2(dx, dy)
        + vec2(0.0001)
    );
}

// ============================================================
// Hash
// ============================================================
//
// Simple pseudo-random generator.
//
// Used for slight jitter sampling during blur passes.
//
// This gives every pixel a unique sample pattern offset sequence,
// helping eliminate visible discrete blur banding artifacts.
// ============================================================

float hash12(vec2 p) {

    vec3 p3 = fract(
        vec3(p.xyx) * 0.1031
    );

    p3 += dot(
        p3,
        p3.yzx + 33.33
    );

    return fract(
        (p3.x + p3.y) * p3.z
    );
}

// ============================================================
// Blurred texture
// ============================================================
//
// Blurs the background behind the glass pane.
//
// Uses a compact number of texture samples spread along a spiral
// pattern using the golden angle offset.
//
// More efficient than full Gaussian blur passes for real-time
// liquid glass.
// ============================================================

vec3 getBlurredColor(
    vec2 uv,
    float blurAmount,
    vec2 fragCoord
) {

    // Convert pixel blur radius into UV space coordinates.
    vec2 radius =
        vec2(blurAmount)
        / iResolution.xy;

    // Number of texture samples taken per fragment.
    //
    // Higher values = smoother quality blur, but increased fragment shader
    // cost.
    const float SAMPLES = 8.0;

    // Golden Angle constant.
    //
    // Provides uniform distribution of sample points across the spiral loop.
    const float GOLDEN_ANGLE = 2.3999632;

    vec3 col = vec3(0.0);

    // Jitter prevents overly static sample pattern artifacts.
    float jitter = hash12(fragCoord);

    // --------------------------------------------------------
    // Radial blur sampling
    // --------------------------------------------------------

    for (
        float i = 0.0;
        i < SAMPLES;
        i += 1.0
    ) {

        // Radial offset distance.
        //
        // sqrt() distributes sample points evenly across circular area space.
        float r = sqrt(
            (i + 0.5) / SAMPLES
        );

        // Angle position of current sample step.
        float theta =
            (i + jitter)
            * GOLDEN_ANGLE;

        // Offset coordinates from central base UV position.
        vec2 offset =
            vec2(
                cos(theta),
                sin(theta)
            )
            * r
            * radius;

        // Fetch sample color from background texture.
        col += texture2D(
            texture0,
            uv + offset
        ).rgb;
    }

    // Average color value across all taken samples.
    return col / SAMPLES;
}

// ============================================================
// Fragment shader
// ============================================================

void main() {
    // --------------------------------------------------------
    // Current fragment coordinate in screen pixel space.
    // --------------------------------------------------------

    vec2 fragCoord = gl_FragCoord.xy;

    // --------------------------------------------------------
    // Fetch combined scene SDF value.
    // --------------------------------------------------------

    float sdf = sceneSDF(fragCoord);

    // ========================================================
    // Anti-aliasing
    // ========================================================
    //
    // fwidth() calculates the rate of change of the SDF between
    // neighbor fragments.
    //
    // This allows producing smooth edge anti-aliasing instead of
    // jagged pixel steps.
    // ========================================================

    float aa = fwidth(sdf);

    // Protection against excessively small derivative values.
    if (aa < 0.001) {
        aa = 1.0;
    }

    // --------------------------------------------------------
    // Early discard step
    //
    // If fragment lies far outside the shape boundaries, drop
    // calculations early.
    // --------------------------------------------------------

    if (sdf > 8.0) {
        discard;
    }

    // --------------------------------------------------------
    // Surface normal vector of liquid shape.
    //
    // Used below for bevel refraction and rim lighting effects.
    // --------------------------------------------------------

    vec2 grad = getSDFGradient(fragCoord);

    // ========================================================
    // Screen UV
    // ========================================================

    // Convert pixel screen coordinates to normalized UV space.
    vec2 screenUV =
        fragCoord / iResolution.xy;

    // ========================================================
    // Lens distortion
    // ========================================================

    // Primary button center coordinates.
    vec2 center =
        u_pos + u_size * 0.5;

    // Normalized UV coordinate relative to button center point.
    //
    // Approximately maps from:
    //
    //     (-1, -1) ... (1, 1)
    //
    // across button width/height bounds.
    vec2 normButtonUV =
        (fragCoord - center)
        / (u_size * 0.5);

    // Distance offset magnitude from button center.
    float dist =
        length(normButtonUV);

    // --------------------------------------------------------
    // Lens offset computation
    //
    // Magnification displacement is strongest near center space,
    // tapering off towards edges.
    //
    // Produces realistic optical glass lens refraction behavior.
    // --------------------------------------------------------

    vec2 lensOffset =
        normButtonUV
        * (1.0 - smoothstep(
            0.0,
            1.5,
            dist
        ))
        * u_lens_power;

    // ========================================================
    // Bevel
    // ========================================================

    // Reference button size metric.
    float heightRef =
        min(u_size.x, u_size.y);

    // Maximum edge bevel stroke width.
    float bevelWidth =
        min(
            24.0,
            heightRef * 0.4
        );

    // --------------------------------------------------------
    // Bevel mask calculation
    //
    // Concentrates displacement along inner boundary region
    // boundaries.
    // --------------------------------------------------------

    float bevelMask =
        smoothstep(
            -bevelWidth,
            0.0,
            sdf
        );

    // Texture UV displacement along computed surface normal.
    vec2 bevelOffset =
        grad
        * bevelMask
        * u_bevel_power;

    // ========================================================
    // Final UV distortion composition
    // ========================================================

    // Combine lens distortion vector offset with bevel offset.
    //
    // Divide by resolution dimensions to transform pixel offsets into UV
    // coordinates.
    vec2 finalUVOffset =
        (lensOffset - bevelOffset)
        * (u_size / iResolution);

    // Final sampling coordinate vector for background texture lookup.
    vec2 sampleUV =
        screenUV - finalUVOffset;

    // ========================================================
    // Background blur
    // ========================================================

    // Fetch blurred background color passing through glass.
    vec3 blurredTex =
        getBlurredColor(
            sampleUV,
            u_blur_amount,
            fragCoord
        );

    // --------------------------------------------------------
    // Slight blur color correction tweak.
    //
    // pow(..., 0.88) slightly raises midtone brightness levels.
    // 1.15 multiplier boosts overall intensity slightly.
    // --------------------------------------------------------

    blurredTex =
        pow(
            blurredTex,
            vec3(0.88)
        ) * 1.15;

    // ========================================================
    // Glass tint
    // ========================================================

    // Apply glass color tint overlay over blurred background texture.
    //
    // u_glass_color.a * 0.4 determines tint intensity strength.
    vec3 finalColor =
        mix(
            blurredTex,
            u_glass_color.rgb,
            u_glass_color.a * 0.4
        );

    // ========================================================
    // Inner bevel shading
    // ========================================================

    // Generate subtle inner edge darkening profile near boundary walls.
    float innerBevel =
        smoothstep(
            -heightRef * 0.35,
            0.0,
            sdf
        ) * 0.2;


    // Apply slight inner ambient occlusion darkening.
    finalColor *=
        (1.0 - innerBevel);

    // ========================================================
    // Rim lighting
    // ========================================================
    //
    // Generates a sharp bright rim highlight along outer boundary
    // contour line.
    // ========================================================

    float rimMask =
        smoothstep(
            -3.0,
            -0.5,
            sdf
        )
        *
        smoothstep(
            0.5,
            -0.5,
            sdf
        );

    // Key light directional vector.
    //
    // (-0.5, 0.85) points light source primarily from top-left angle.
    vec2 lightDir =
        normalize(
            vec2(-0.5, 0.85)
        );

    // Dot product between surface normal gradient and key light direction
    // vector.
    float NdotL =
        dot(
            grad,
            lightDir
        );

    // --------------------------------------------------------
    // Top-left rim highlight specular component
    //
    // Brightens regions facing directly towards main light source
    // direction vector.
    // --------------------------------------------------------

    float topLeftHighlight =
        pow(
            max(0.0, NdotL),
            2.2
        )
        * rimMask
        * 1.1;

    // --------------------------------------------------------
    // Bottom-right rim specular highlight
    //
    // Evaluated against inverted normal vector for softer indirect
    // rim fill reflections.
    // --------------------------------------------------------

    float bottomRightHighlight =
        pow(
            max(0.0, -NdotL),
            3.0
        )
        * rimMask
        * 0.75;


    // --------------------------------------------------------
    // Subtle bright stroke line directly along boundary edge
    // zero-contour.
    // --------------------------------------------------------

    float edgeStroke =
        smoothstep(
            -1.2,
            0.0,
            sdf
        )
        * 0.25;

    // Accumulate all computed specular rim highlights.
    finalColor +=
        vec3(1.0)
        * (
            topLeftHighlight
            + bottomRightHighlight
            + edgeStroke
        );

    // ========================================================
    // Pressed state
    // ========================================================
    //
    // Applies a subtle blue hue accent transformation upon press
    // interaction.
    // ========================================================

    vec3 pressedGlassColor =
        mix(
            finalColor,
            vec3(0.25, 0.55, 1.0),
            0.25
        );

    // Smoothly blend between idle state and active press state highlights.
    //
    // u_pressed:
    //
    //     0.0 -> idle glass appearance
    //     1.0 -> pressed glass state active
    //
    finalColor =
        mix(
            finalColor,
            pressedGlassColor,
            u_pressed
        );

    // ========================================================
    // Touch highlight
    // ========================================================
    //
    // Generates a radial glow spotlight around user touch point.
    // Visible exclusively when press interaction state is active.
    // ========================================================

    float lightRadius =
        max(
            u_size.x,
            u_size.y
        ) * 0.85;

    // Radial distance calculation from fragment location to active touch
    // coordinate.
    float spot =
        smoothstep(
            lightRadius,
            0.0,
            length(
                fragCoord - u_touch_pos
            )
        );

    // Blend white touch light overlay spot.
    //
    // 0.35 — peak highlight intensity modifier ceiling.
    finalColor =
        mix(
            finalColor,
            vec3(1.0),
            spot
            * u_pressed
            * 0.35
        );

    // ========================================================
    // SDF alpha/anti-aliasing
    // ========================================================
    //
    // Evaluates final alpha opacity gradient based on signed distance
    // values.
    //
    // Inside shape interior:
    //
    //     sdf < 0
    //
    // alpha -> 1
    //
    // Outside shape exterior:
    //
    //     sdf > 0
    //
    // alpha -> 0
    //
    // Produces anti-aliased edge smoothing across boundary near
    // sdf == 0 region.
    // ========================================================

    float edgeAlpha =
        smoothstep(
            aa,
            -aa,
            sdf
        );

    // --------------------------------------------------------
    // Final fragment color output composition.
    //
    // frag_color.a incorporates incoming opacity from the Kivy
    // vertex pipeline.
    // --------------------------------------------------------

    gl_FragColor =
        vec4(
            finalColor,
            edgeAlpha
        )
        * frag_color.a;
}
