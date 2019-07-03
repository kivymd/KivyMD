"""
Accordion
=========

Copyright (c) 2015 Andrés Rodríguez and KivyMD contributors -
    KivyMD library up to version 0.1.2
Copyright (c) 2019 Ivanov Yuri and KivyMD contributors -
    KivyMD library version 0.1.3 and higher

For suggestions and questions:
<kivydevelopment@gmail.com>

This file is distributed under the terms of the same license,
as the Kivy framework.
"""

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, OptionProperty, ObjectProperty
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout

from kivymd.backgroundcolorbehavior import SpecificBackgroundColorBehavior
from kivymd.font_definitions import theme_font_styles
from kivymd.list import OneLineListItem
from kivymd.theming import ThemableBehavior


class MDAccordionItemTitleLayout(ThemableBehavior, BoxLayout):
    pass


class MDAccordion(ThemableBehavior, SpecificBackgroundColorBehavior, Accordion):
    pass


class MDAccordionSubItem(OneLineListItem):
    parent_item = ObjectProperty()


class MDAccordionItem(ThemableBehavior, AccordionItem):
    title_theme_color = OptionProperty(
        None,
        allownone=True,
        options=["Primary", "Secondary", "Hint", "Error", "Custom"],
    )
    """Color theme for title text and  icon"""

    title_color = ListProperty(None, allownone=True)
    """Color for title text and icon if `title_theme_color` is Custom"""

    divider_color = ListProperty(None, allownone=True)
    """Color for dividers between different titles in rgba format 
    To remove the divider set a color with an alpha of ."""

    indicator_color = ListProperty(None, allownone=True)
    """Color for the indicator on the side of the active item in rgba format 
    To remove the indicator set a color with an alpha of . """

    font_style = OptionProperty("Subtitle1", options=theme_font_styles)
    """Font style to use for the title text"""

    title_template = StringProperty("MDAccordionItemTitle")
    """ Template to use for the title """

    icon = StringProperty("android", allownone=True)
    """Icon name to use when this item is expanded"""

    icon_expanded = StringProperty("chevron-up")
    """Icon name to use when this item is expanded"""

    icon_collapsed = StringProperty("chevron-down")
    """Icon name to use when this item is collapsed"""

    def add_widget(self, widget):
        if isinstance(widget, MDAccordionSubItem):
            widget.parent_item = self
            self.ids.ml.add_widget(widget)
        else:
            super().add_widget(widget)


Builder.load_string(
    """
#:import MDLabel kivymd.label.MDLabel
#:import md_icons kivymd.icon_definitions.md_icons


<MDAccordion>
    md_bg_color: self.theme_cls.primary_color


<MDAccordionItem>
    canvas.before:
        # PushMatrix
        # Translate:
        #     xy: (dp(2), 0) if self.orientation == 'vertical' else (0, dp(2))
    canvas.after:
        # PopMatrix
        Color:
            rgba: self.divider_color or self.theme_cls.divider_color
        Rectangle:
            size:
                (dp(1), self.height) if self.orientation == 'horizontal'\
                else (self.width, dp(1))
            pos:self.pos
        Color:
            rgba:
                [0, 0, 0, 0] if self.collapse\
                else (self.indicator_color or self.theme_cls.accent_color)
        Rectangle:
            size:
                (dp(2),self.height)\
                if self.orientation == 'vertical' else (self.width,dp(2))
            pos:self.pos

    ScrollView:
        id: sv
        MDList:
            id: ml


<MDAccordionSubItem>
    theme_text_color: 'Custom'
    text_color: self.parent_item.parent.specific_text_color


[MDAccordionItemTitle@MDAccordionItemTitleLayout]:
    padding: '12dp'
    spacing: '12dp'
    orientation:
        'horizontal' if ctx.item.orientation=='vertical' else 'vertical'

    canvas:
        PushMatrix
        Translate:
            xy:
                (-dp(2), 0) if ctx.item.orientation == 'vertical'\
                else (0, - dp(2))
    canvas.after:
        PopMatrix

    MDIcon:
        id: _icon
        icon: ctx.item.icon if ctx.item.icon else 'menu'
        theme_text_color: 'Custom'
        text_color: ctx.item.parent.specific_text_color
        size_hint:
            (None, 1) if ctx.item.orientation == 'vertical' else (1, None)
        size:
            ((self.texture_size[0],1) if ctx.item.orientation == 'vertical'\
            else (1, self.texture_size[1])) if ctx.item.icon else (0, 0)
        text_size:
            (self.width, None) if ctx.item.orientation == 'vertical'\
            else (None,self.width)

        canvas.before:
            PushMatrix
            Rotate:
                angle: 90 if ctx.item.orientation == 'horizontal' else 0
                origin: self.center
        canvas.after:
            PopMatrix

    MDLabel:
        id:_label
        theme_text_color: 'Custom'
        text_color: ctx.item.parent.specific_text_color
        text: ctx.item.title
        font_style: ctx.item.font_style
        text_size:
            (self.width, None) if ctx.item.orientation == 'vertical'\
            else (None,self.width)

        canvas.before:
            PushMatrix
            Rotate:
                angle: 90 if ctx.item.orientation == 'horizontal' else 0
                origin: self.center
        canvas.after:
            PopMatrix

    MDLabel:
        id:_expand_icon
        theme_text_color: 'Custom'
        text_color: ctx.item.parent.specific_text_color
        font_style:'Icon'
        size_hint: (None,1) if ctx.item.orientation == 'vertical' else (1,None)
        size:
            (self.texture_size[0], 1) if ctx.item.orientation == 'vertical'\
            else (1,self.texture_size[1])
        text:
            md_icons[ctx.item.icon_collapsed if ctx.item.collapse\
            else ctx.item.icon_expanded]
        halign: 'right' if ctx.item.orientation=='vertical' else 'center'
        #valign: 'middle' if ctx.item.orientation=='vertical' else 'bottom'

        canvas.before:
            PushMatrix
            Rotate:
                angle: 90 if ctx.item.orientation == 'horizontal' else 0
                origin: self.center
        canvas.after:
            PopMatrix
"""
)


if __name__ == "__main__":
    from kivy.app import App
    from kivymd.theming import ThemeManager

    class AccordionApp(App):
        theme_cls = ThemeManager()

        def build(self):
            self.theme_cls.primary_palette = "Indigo"
            return Builder.load_string(
                """
#:import MDLabel kivymd.label.MDLabel


BoxLayout:
    spacing: '64dp'

    MDAccordion:
        orientation: 'vertical'

        MDAccordionItem:
            title: 'Item 1'
            icon: 'home'
            MDAccordionSubItem:
                text: "Subitem 1"
            MDAccordionSubItem:
                text: "Subitem 2"
            MDAccordionSubItem:
                text: "Subitem 3"
        MDAccordionItem:
            title: 'Item 2'
            icon: 'earth'
            MDAccordionSubItem:
                text: "Subitem 4"
            MDAccordionSubItem:
                text: "Subitem 5"
            MDAccordionSubItem:
                text: "Subitem 6"
        MDAccordionItem:
            title: 'Item 3'
            MDAccordionSubItem:
                text: "Subitem 7"
            MDAccordionSubItem:
                text: "Subitem 8"
            MDAccordionSubItem:
                text: "Subitem 9"

    MDAccordion:
        orientation: 'horizontal'

        MDAccordionItem:
            title:'Item 1'
            icon: 'home'
            MDLabel:
                text:'Content 1'
                theme_text_color:'Primary'
        MDAccordionItem:
            title:'Item 2'
            MDLabel:
                text:'Content 2'
                theme_text_color:'Primary'
        MDAccordionItem:
            title:'Item 3'
            MDLabel:
                text:'Content 3'
                theme_text_color:'Primary'
"""
            )

    AccordionApp().run()
