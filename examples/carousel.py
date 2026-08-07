from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.carousel import MDCarouselItem
from kivymd.uix.fitimage import FitImage
from kivymd.uix.navigationbar import MDNavigationItem


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


KV = '''
#:import MDSharedAxisTransition kivymd.uix.transition.MDSharedAxisTransition

<BaseMDNavigationItem>

    MDNavigationItemIcon:
        icon: root.icon

    MDNavigationItemLabel:
        text: root.text


MDBoxLayout:
    orientation: "vertical"
    md_bg_color: self.theme_cls.backgroundColor

    MDScreenManager:
        id: screen_manager
        transition: MDSharedAxisTransition(transition_axis="x", duration=0.75)

        MDScreen:
            name: "screen 1"
            md_bg_color: self.theme_cls.backgroundColor
            on_pre_leave: app.detach_carousel()
            on_pre_enter: app.attach_carousel()

            MDBoxLayout:
                orientation: "vertical"
                padding: 0, 0, 0, dp(20)

                MDBoxLayout:
                    id: carousel_box
                    size_hint_y: None
                    height: dp(320)

                    MDCarousel:
                        id: carousel
                        layouts: "multi-browse"

                MDBoxLayout:
                    adaptive_height: True

                    MDWidget:

                    MDButton:
                        style: "text"
                        on_release:
                            screen_manager.current = "screen 2"

                        MDButtonText:
                            text: "Show all"

                MDScrollView:
                    canvas.before:
                        ScissorPush:
                            x: int(self.x)
                            y: int(self.y)
                            width: int(self.width)
                            height: int(self.height) + dp(100)
                    canvas.after:
                        ScissorPop:

                    MDBoxLayout:
                        adaptive_height: True
                        orientation: "vertical"

                        MDBoxLayout:
                            adaptive_height: True
                            padding: dp(20), 0, 0, 0

                            MDLabel:
                                text: "Around town"
                                adaptive_height: True
                                font_style: "Headline"
                                role: "small"

                        MDListItem:

                            MDListItemLeadingAvatar:
                                source: "avatar.png"

                            MDListItemHeadlineText:
                                text: "Selen Zeynep"

                            MDListItemSupportingText:
                                text: "Local Beats • 713 people"

                        MDBoxLayout:
                            adaptive_height: True
                            padding: dp(20), 0, dp(20), 0

                            MDSmartTile:
                                size_hint_y: None
                                height: dp(240)
                                overlap: True

                                MDSmartTileImage:
                                    source: "bg.jpg"
                                    radius: [dp(24), ]

                                MDSmartTileOverlayContainer:
                                    md_bg_color: 0, 0, 0, .5
                                    orientation: "vertical"
                                    adaptive_height: True
                                    padding: "8dp"
                                    radius: [0, 0, dp(24), dp(24)]

                                    MDLabel:
                                        text: "What Buttons Are"
                                        theme_text_color: "Custom"
                                        text_color: "white"
                                        adaptive_height: True
                                        font_style: "Title"
                                        role: "large"

                                    MDLabel:
                                        text: "They Pushing"
                                        theme_text_color: "Custom"
                                        text_color: "white"
                                        adaptive_height: True
                                        font_style: "Title"
                                        role: "large"

                                    MDBoxLayout:
                                        adaptive_height: True
                                        spacing: dp(8)

                                        MDIcon:
                                            icon: "language-fortran"
                                            theme_icon_color: "Custom"
                                            icon_color: "white"

                                        MDLabel:
                                            text: "The Fortnightly"
                                            theme_text_color: "Custom"
                                            text_color: "white"
                                            adaptive_height: True
                                            font_style: "Title"
                                            role: "small"
                                            pos_hint: {"center_y": .5}

                        MDBoxLayout:
                            adaptive_height: True
                            padding: dp(20), dp(8), dp(20), 0

                            MDLabel:
                                text: "2 day ago"
                                adaptive_height: True
                                font_style: "Title"
                                role: "small"
                                pos_hint: {"center_y": .5}

                            Widget:

                            MDIconButton:
                                icon: "heart-circle"
                                style: "standard"

                            MDIconButton:
                                icon: "dots-horizontal"
                                style: "standard"

        MDScreen:
            name: "screen 2"
            md_bg_color: self.theme_cls.backgroundColor

            MDBoxLayout:
                orientation: "vertical"

                MDBoxLayout:
                    adaptive_height: True
                    padding: dp(8)

                    MDIconButton:
                        icon: "arrow-left"
                        on_release: screen_manager.current = "screen 1"
                        pos_hint: {"center_y": .5}

                    MDLabel:
                        text: "Back"
                        adaptive_height: True
                        pos_hint: {"center_y": .5}

                MDScrollView:

                    MDGridLayout:
                        id: grid_container
                        cols: 2
                        padding: dp(16)
                        spacing: dp(16)
                        adaptive_height: True


    MDNavigationBar:

        BaseMDNavigationItem
            icon: "home"
            text: "Home"
            active: True

        BaseMDNavigationItem
            icon: "star-outline"
            text: "Saved"

        BaseMDNavigationItem
            icon: "compass-outline"
            text: "Explore"

        BaseMDNavigationItem
            icon: "account-outline"
            text: "Profile"
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def detach_carousel(self):
        box = self.root.ids.carousel_box
        carousel = self.root.ids.carousel

        if carousel in box.children:
            box.remove_widget(carousel)

    def attach_carousel(self):
        box = self.root.ids.carousel_box
        carousel = self.root.ids.carousel

        if carousel not in box.children:
            box.add_widget(carousel)

    def on_start(self):
        for i in range(1, 20):
            carousel_item = MDCarouselItem()
            image = FitImage(
                source=f"https://picsum.photos/800/600?random={i}",
                radius=[dp(28)],
            )
            carousel_item.add_widget(image)
            self.root.ids.carousel.add_widget(carousel_item)

        grid = self.root.ids.grid_container
        for i in range(1, 20):
            image = FitImage(
                source=f"https://picsum.photos/800/600?random={i}",
                radius=[dp(16)],
                size_hint_y=None,
                height=dp(180),
            )
            grid.add_widget(image)


Example().run()
