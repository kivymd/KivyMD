from kivy.metrics import dp, sp
from kivy.uix.video import Video

from kivymd.app import MDApp
from kivymd.uix.button import IOSButton, IOSIconButton
from kivymd.uix.screen import MDScreen


class VideoPlayerWithIOSButton(MDApp):
    play_button: IOSButton
    video: Video

    def build(self):
        layout = MDScreen()

        self.video = Video(
            source="sample.mp4",
            state="play",
            options={"eos": "loop"},
        )

        self.play_button = IOSButton(
            IOSIconButton(
                id="icon",
                icon="play",
                theme_font_size="Custom",
                font_size=sp(42),
                theme_icon_color="Custom",
                icon_color="white",
                pos_hint={"center_y": 0.5},
            ),
            size_hint=[None, None],
            size=[dp(100), dp(100)],
            border_radius=[dp(50)] * 4,
            target_background=self.video,
            padding=dp(29),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.play_button.bind(on_release=self.toggle_video)

        layout.add_widget(self.video)
        layout.add_widget(self.play_button)

        return layout

    def toggle_video(self, instance):
        if self.video.state == "play":
            self.video.state = "pause"
            self.root.get_ids().icon.icon = "pause"
        else:
            self.video.state = "play"
            self.root.get_ids().icon.icon = "play"


if __name__ == "__main__":
    VideoPlayerWithIOSButton().run()
