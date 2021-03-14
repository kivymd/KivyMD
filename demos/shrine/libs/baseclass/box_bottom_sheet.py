from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import BooleanProperty, ObjectProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView

from kivymd.theming import ThemableBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import TwoLineAvatarIconListItem


class BoxBottomSheetProductList(RecycleView):
    pass


class TotalPriceForBoxBottomSheetProductList(MDBoxLayout):
    pass


class ToolbarForBoxBottomSheetProductList(MDBoxLayout):
    pass


class ItemForBoxBottomSheetProductList(TwoLineAvatarIconListItem):
    pass


class PreviousImage(CircularRippleBehavior, ButtonBehavior, Image):
    description = StringProperty()
    _root = ObjectProperty()


class BoxBottomSheet(ThemableBehavior, MDBoxLayout):
    open_sheet_box = BooleanProperty(False)

    def clear_box(self):
        while len(self.ids.previous_box.children) != 1:
            for widget in self.ids.previous_box.children:
                if widget.__class__ is not MDIconButton:
                    self.ids.previous_box.remove_widget(widget)

    def restore_opacity_bottom_sheet(self):
        Animation(opacity=1, d=0.2).start(self.ids.previous_box)
        Animation(opacity=1, d=0.2).start(self)

    def restore_width_bottom_sheet(self):
        if len(self.ids.previous_box.children) != 1:
            for widget in self.ids.previous_box.children:
                self.ids.previous_box.width += widget.width
                self.width += widget.width
        self.ids.previous_box.height = dp(48)
        if self.parent.ids.box_bottom_sheet_product_list.width == 0:
            Animation(width=self.width + dp(48), d=0.2).start(self)

    def remove_box_list(self, *args):
        self.parent.ids.box_bottom_sheet_product_list.data = []

        self.restore_width_bottom_sheet()
        self.restore_opacity_bottom_sheet()

    def hide_box_bottom_sheet(self):
        Animation(width=0, d=0.2).start(self)
        Animation(opacity=0, d=0.2).start(self)

    def do_open_bottom_sheet(self, *args):
        total_price = 0
        count_item = 0
        for widget in self.ids.previous_box.children:
            if widget.__class__ is PreviousImage:
                count_item += 1
                total_price += int(
                    float(widget.description.split("\n")[1].split("$ ")[1])
                )
                self.parent.ids.box_bottom_sheet_product_list.data.append(
                    {
                        "viewclass": "ItemForBoxBottomSheetProductList",
                        "height": dp(72),
                        "path_to_image": widget.source,
                        "description": widget.description,
                    }
                )
        self.parent.ids.box_bottom_sheet_product_list.data.insert(
            0,
            {
                "viewclass": "ToolbarForBoxBottomSheetProductList",
                "count_item": count_item,
                "callback": self.hide_bottom_sheet,
            },
        )
        self.parent.ids.box_bottom_sheet_product_list.data.append(
            {
                "viewclass": "TotalPriceForBoxBottomSheetProductList",
                "total_price": str(total_price),
            }
        )

        Animation(opacity=1, d=0.2).start(
            self.parent.ids.box_bottom_sheet_product_list
        )
        self.show_clear_button()

    def show_clear_button(self):
        self.parent.ids.clear_button.opacity = 1
        self.parent.ids.clear_button.disabled = False
        self.parent.ids.clear_button.grow()

    def hide_clear_button(self, *args):
        def hide_clear_button(interval):
            self.parent.ids.clear_button.opacity = 0
            self.parent.ids.clear_button.disabled = True

        self.parent.ids.clear_button.grow()
        Clock.schedule_once(hide_clear_button, 0.2)

    def hide_bottom_sheet(self, *args):
        Animation.stop_all(self)
        self.hide_clear_button()
        Animation(opacity=0, d=0.2).start(
            self.parent.ids.box_bottom_sheet_product_list
        )
        animation = Animation(
            height=Window.height // 3, width=Window.width // 2, d=0.1
        ) + Animation(height=dp(68), width=dp(68), d=0.2)
        animation.bind(on_complete=self.remove_box_list)
        animation.start(self)
        self.open_sheet_box = False

    def open_bottom_sheet(self):
        Animation.stop_all(self)
        anim = Animation(
            height=Window.height // 2, width=Window.width, d=0.1
        ) + Animation(height=Window.height, d=0.1)
        anim.bind(on_complete=self.do_open_bottom_sheet)
        anim.start(self)
        self.open_sheet_box = True
