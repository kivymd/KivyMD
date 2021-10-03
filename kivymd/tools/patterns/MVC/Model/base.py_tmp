import datetime
import time
from typing import Union

import requests
from firebase import firebase


def get_time() -> str:
    """Returns a string with the current date and time."""

    return datetime.datetime.fromtimestamp(
        time.mktime(datetime.datetime.now().timetuple())
    ).strftime("%d-%m-%Y %H:%M:%S")


class Base:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    def __init__(self):
        # RealTime Database attribute.
        self.real_time_firebase = firebase.FirebaseApplication(
            "https://loginappmvc-5a4aa-default-rtdb.firebaseio.com/", None
        )
        self.type_base = "UserData"
        self.name_base_users = "LoginsPasswords"
        self.send_user_data_to_database({"login": "Kivy", "password": "KivyMD"})

    def get_data_from_base_users(self) -> Union[dict, None]:
        """
        Return data from the database:

        {
            '05-08-2021 20:51:22':
                {'login': 'User login', 'password': 'password'},
            ...,
        }
        """

        try:
            data = self.real_time_firebase.get(self.type_base, self.name_base_users)
        except requests.exceptions.ConnectionError:
            return None
        return data

    def send_user_data_to_database(self, data: dict) -> bool:
        """Sends data to the database."""

        try:
            self.real_time_firebase.put(
                f"{self.type_base}/{self.name_base_users}",
                get_time(),
                data,
            )
            return True
        except requests.exceptions.HTTPError:
            return False
