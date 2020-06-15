def test_fonts_registration():
    # This should register fonts:
    import kivymd  # NOQA
    from kivy.core.text import LabelBase

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
