uniform vec2 u_mouse;
uniform float u_glare_opacity;
uniform float u_glare_radius;
uniform float u_max_opacity;
uniform vec3 u_glare_color;
uniform vec2 u_parallax_offset;
uniform vec2 u_card_size;
uniform float u_corner_radius;

float sdRoundedBox(
    vec2 p,
    vec2 b,
    float r
) {
    vec2 q =
        abs(p) - b + r;

    return
        min(
            max(q.x, q.y),
            0.0
        )
        +
        length(
            max(q, 0.0)
        )
        -
        r;
}

void main() {
    vec2 uv_shape = tex_coord0;

    vec2 uv_texture = tex_coord0 + u_parallax_offset;

    vec2 p =
        (uv_shape - 0.5)
        *
        u_card_size;

    float d =
        sdRoundedBox(
            p,
            u_card_size * 0.5,
            u_corner_radius
        );

    if (d > 0.0) {
        discard;
    }

    vec4 tex_color =
        texture2D(
            texture0,
            uv_texture
        )
        *
        frag_color;

    float dist =
        distance(
            uv_shape,
            u_mouse
        );

    float glare =
        smoothstep(
            u_glare_radius,
            0.0,
            dist
        )
        *
        u_glare_opacity;

    vec3 final_glare =
        u_glare_color
        *
        glare
        *
        u_max_opacity;

    gl_FragColor =
        vec4(
            tex_color.rgb + final_glare,
            tex_color.a
        );
}
