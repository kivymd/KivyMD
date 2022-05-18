from __future__ import annotations

import socket

import requests
from firebase import firebase


def get_connect(func, host="8.8.8.8", port=53, timeout=3):
    """Checks for an active Internet connection."""

    def wrapped(*args):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port)
            )
            return func(*args)
        except Exception:
            return False

    return wrapped


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    name = "Firebase"

    def __init__(self):
        self.DATABASE_URL = "https://fir-db73a-default-rtdb.firebaseio.com/"
        # Address for users collections.
        self.USER_DATA = "Userdata"
        # RealTime Database attribute.
        self.real_time_firebase = firebase.FirebaseApplication(
            self.DATABASE_URL, None
        )

    @get_connect
    def get_data_from_collection(self, name_collection: str) -> dict | bool:
        """Returns data of the selected collection from the database."""

        try:
            data = self.real_time_firebase.get(
                self.DATABASE_URL, name_collection
            )
        except requests.exceptions.ConnectionError:
            return False

        return data
