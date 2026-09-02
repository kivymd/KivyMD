void main() {
    tex_coord0 = vTexCoords0;
    frag_color = color;
    gl_Position = projection_mat * modelview_mat * vec4(vPosition, 0.0, 1.0);
}
