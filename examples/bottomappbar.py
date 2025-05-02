import asynckivy
from faker import Faker  # pip install Faker
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ObjectProperty, StringProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

from kivymd.app import MDApp
from kivymd.uix.appbar import MDActionBottomAppBarButton
from kivymd.uix.boxlayout import MDBoxLayout

KV = """
#:import MDFabBottomAppBarButton kivymd.uix.appbar.MDFabBottomAppBarButton


<UserCard>
    orientation: "vertical"
    adaptive_height: True
    md_bg_color: "#373A22" if self.selected else "#1F1E15"
    radius: 16
    padding: 0, 0, 0, "16dp"

    MDListItem:
        theme_bg_color: "Custom"
        md_bg_color: root.md_bg_color
        radius: root.radius
        ripple_effect: False

        MDListItemLeadingAvatar:
            source: root.avatar
            # radius: self.height / 2

        MDListItemHeadlineText:
            text: root.name
            theme_text_color: "Custom"
            text_color: "#8A8D79"

        MDListItemSupportingText:
            text: root.time
            theme_text_color: "Custom"
            text_color: "#8A8D79"

    MDLabel:
        text: root.text
        adaptive_height: True
        theme_text_color: "Custom"
        text_color: "#8A8D79"
        padding_x: "16dp"
        shorten: True
        shorten_from: "right"

    Widget:


MDFloatLayout:
    md_bg_color: "#151511"

    RecycleView:
        id: card_list
        viewclass: "UserCard"

        SelectableRecycleGridLayout:
            orientation: 'vertical'
            spacing: "16dp"
            padding: "16dp"
            default_size: None, dp(120)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            multiselect: True
            touch_multiselect: True

    MDBottomAppBar:
        id: bottom_appbar
        scroll_cls: card_list
        allow_hidden: True
        theme_bg_color: "Custom"
        md_bg_color: "#232217"

        MDFabBottomAppBarButton:
            id: fab_button
            icon: "plus"
            theme_bg_color: "Custom"
            md_bg_color: "#373A22"
            theme_icon_color: "Custom"
            icon_color: "#ffffff"
"""


class UserCard(RecycleDataViewBehavior, MDBoxLayout):
    name = StringProperty()
    time = StringProperty()
    text = StringProperty()
    avatar = StringProperty()
    callback = ObjectProperty(lambda x: x)

    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        return super().refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            Clock.schedule_once(self.callback)
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        self.selected = is_selected
        rv.data[index]["selected"] = is_selected


class SelectableRecycleGridLayout(
    FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout
):
    pass


class BottomAppBarButton(MDActionBottomAppBarButton):
    theme_icon_color = "Custom"
    icon_color = "#8A8D79"


class Example(MDApp):
    selected_cards = False

    def build(self):
        return Builder.load_string(KV)

    def on_tap_card(self, *args):
        datas = [data["selected"] for data in self.root.ids.card_list.data]
        if True in datas and not self.selected_cards:
            self.root.ids.bottom_appbar.action_items = [
                BottomAppBarButton(icon="gmail"),
                BottomAppBarButton(icon="label-outline"),
                BottomAppBarButton(icon="bookmark"),
            ]
            self.root.ids.fab_button.icon = "pencil"
            self.selected_cards = True
        else:
            if len(list(set(datas))) == 1 and not list(set(datas))[0]:
                self.selected_cards = False
            if not self.selected_cards:
                self.root.ids.bottom_appbar.action_items = [
                    BottomAppBarButton(icon="magnify"),
                    BottomAppBarButton(icon="trash-can-outline"),
                    BottomAppBarButton(icon="download-box-outline"),
                ]
                self.root.ids.fab_button.icon = "plus"

    def on_start(self):
        async def generate_card():
            for i in range(10):
                await asynckivy.sleep(0)
                self.root.ids.card_list.data.append(
                    {
                        "name": fake.name(),
                        "time": fake.date(),
                        "avatar": fake.image_url(),
                        "text": fake.text(),
                        "selected": False,
                        "callback": self.on_tap_card,
                    }
                )

        self.on_tap_card()
        fake = Faker()
        Clock.schedule_once(lambda x: asynckivy.start(generate_card()))


Example().run()
