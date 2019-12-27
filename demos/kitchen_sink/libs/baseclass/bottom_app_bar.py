from kivy.uix.screenmanager import Screen


class KitchenSinkBottomAppBar(Screen):
    def callback_for_bottom_app_bar(self, app, text, value):
        if value and app.data_screens["Bottom App Bar"]["object"]:
            toolbar = self.ids.bottom_toolbar
            if text == "Off":
                toolbar.remove_notch()
            elif text == "On":
                toolbar.set_notch()
            elif text == "Attached - End":
                toolbar.mode = "end"
            elif text == "Attached - Center":
                toolbar.mode = "center"
            elif text == "Free - End":
                toolbar.mode = "free-end"
            elif text == "Free - Center":
                toolbar.mode = "free-center"
