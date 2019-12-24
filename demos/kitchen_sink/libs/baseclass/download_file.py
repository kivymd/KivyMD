import os

from kivy.uix.screenmanager import Screen

from kivymd.toast import toast


class KitchenSinkDownloadFile(Screen):
    def download_progress_hide(self, instance_progress, value):
        """Hides progress progress."""

        self.ids.toolbar.right_action_items = [
            [
                "download",
                lambda x: self.download_progress_show(instance_progress),
            ]
        ]

    def download_progress_show(self, instance_progress):
        self.set_chevron_back_screen()
        instance_progress.open()
        instance_progress.animation_progress_from_fade()

    def show_example_download_file(self, interval):
        from kivymd.uix.progressloader import MDProgressLoader

        def get_connect(host="8.8.8.8", port=53, timeout=3):
            import socket

            try:
                socket.setdefaulttimeout(timeout)
                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                    (host, port)
                )
                return True
            except (TimeoutError, ConnectionError, OSError):
                return False

        if get_connect():
            link = (
                "https://www.python.org/ftp/python/3.8.0/"
                "python-3.8.0-embed-win32.zip"
            )
            progress = MDProgressLoader(
                url_on_image=link,
                path_to_file=os.path.join(
                    os.environ["KITCHEN_SINK_ROOT"], "python-3.8.0.zip"
                ),
                download_complete=self.download_complete,
                download_hide=self.download_progress_hide,
            )
            progress.start(self.ids.box_flt)
        else:
            toast("Connect error!")

    def download_complete(self):
        self.set_chevron_back_screen()
        toast("Done")

    def set_chevron_back_screen(self):
        """Sets the return chevron to the previous screen in ToolBar."""

        self.ids.toolbar.right_action_items = [["dots-vertical", lambda x: x]]
