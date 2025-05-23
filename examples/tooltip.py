from kivy.lang import Builder
from kivy.properties import StringProperty

from examples.common_app import CommonApp
from kivymd.app import MDApp
from kivymd.uix.navigationrail import (
    MDNavigationRailItem,
    MDNavigationRailMenuButton,
)
from kivymd.uix.tooltip import MDTooltip

KV = """
<TooltipRich>

    MDTooltipRich:
        id: tooltip
        auto_dismiss: False

        MDTooltipRichSubhead:
            text: root.tooltip_subhead

        MDTooltipRichSupportingText:
            text: root.tooltip_text

        MDTooltipRichActionButton:
            on_press: tooltip.dismiss()

            MDButtonText:
                text: root.tooltip_button_text


<TooltipPlain>

    MDTooltipPlain:
        text: root.tooltip_text


<CommonNavigationRailItem>

    MDNavigationRailItemIcon:
        icon: root.icon

    MDNavigationRailItemLabel:
        text: root.text


MDBoxLayout:

    MDNavigationRail:
        id: rail

        TooltipNavigationRailMenuButton:
            icon: "menu"
            on_release: app.open_menu(self)
            tooltip_subhead: "Add others"
            tooltip_button_text: "Learn more"
            tooltip_text:
                "Grant value is calculated using the closing stock price \\n" \
                "from the day before the grant date. Amounts do not \\n" \
                "reflect tax witholdings."

        MDNavigationRailFabButton:
            icon: "home"

        CommonNavigationRailItem:
            icon: "folder-outline"
            text: "Files"
            tooltip_text: "Files"

        CommonNavigationRailItem:
            icon: "bookmark-outline"
            text: "Bookmark"
            tooltip_text: "Bookmark"

        CommonNavigationRailItem:
            icon: "library-outline"
            text: "Library"
            tooltip_text: "Library"

    MDScreen:
        md_bg_color: self.theme_cls.secondaryContainerColor
"""


class TooltipPlain(MDTooltip):
    """Implements your plain tooltip base class."""

    tooltip_text = StringProperty()


class TooltipRich(MDTooltip):
    """Implements your rich tooltip base class."""

    tooltip_subhead = StringProperty()
    tooltip_text = StringProperty()
    tooltip_button_text = StringProperty()


class TooltipNavigationRailItem(TooltipPlain, MDNavigationRailItem):
    """Implements a item with tooltip plain behavior."""


class TooltipNavigationRailMenuButton(TooltipRich, MDNavigationRailMenuButton):
    """Implements a button with tooltip rich behavior."""


class CommonNavigationRailItem(TooltipNavigationRailItem):
    """Implements a common item for `MDNavigationRailItem`."""

    text = StringProperty()
    icon = StringProperty()


class Example(MDApp, CommonApp):
    def build(self):
        self.theme_cls.primary_palette = "Olive"
        return Builder.load_string(KV)

    def disabled_widgets(self): ...


Example().run()
