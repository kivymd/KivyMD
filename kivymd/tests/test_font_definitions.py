def test_fonts_registration():
    # This should register fonts:
    from kivy.core.text import LabelBase

    import kivymd  # NOQA

    fonts = [
        "Roboto",
        "RobotoThin",
        "RobotoLight",
        "RobotoMedium",
        "RobotoBlack",
        "Icons",
    ]
    for font in fonts:
        assert font in LabelBase._fonts.keys()
