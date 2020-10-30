def test_icons_have_size():
    from kivy.core.text import Label

    from kivymd.icon_definitions import md_icons

    lbl = Label(font_name="Icons")
    for icon_name, icon_value in md_icons.items():
        assert len(icon_value) == 1
        lbl.refresh()
        assert lbl.get_extents(icon_value) is not None
