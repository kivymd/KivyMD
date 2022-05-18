"""
Restdb.io API Wrapper
---------------------

This package is an API Wrapper for the website `restdb.io <https://restdb.io>`_,
which allows for online databases.
"""

from __future__ import annotations

import json
import os
import socket

import requests


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
    name = "RestDB"

    def __init__(self):
        database_url = "https://restdbio-5498.restdb.io"
        api_key = "7ce258d66f919d3a891d1166558765f0b4dbd"

        self.HEADERS = {"x-apikey": api_key, "Content-Type": "application/json"}
        # Address for file collections.
        self.USER_MEDIA = f"{database_url}/media"
        # Address for users collections.
        self.USER_DATA = f"{database_url}/rest/userdata"

    @get_connect
    def upload_file(self, path_to_file: str) -> dict | bool:
        """
        Uploads a file to the database.
        You can upload a file to the database only from a paid account.
        """

        HEADERS = self.HEADERS.copy()
        del HEADERS["Content-Type"]
        payload = {}
        name_file = os.path.split(path_to_file)[1]
        files = [("file", (name_file, open(path_to_file, "rb"), name_file))]
        response = requests.post(
            url=self.USER_MEDIA,
            headers=HEADERS,
            data=payload,
            files=files,
        )

        if response.status_code == 201:
            # {
            #     "msg":"OK",
            #     "uploadid": "ed1bca42334f68d873161641144e57b7",
            #     "ids": ["62614fb90f9df71600284aa7"],
            # }
            json = response.json()
            if "msg" in json and json["msg"] == "OK":
                return json
        else:
            return False

    @get_connect
    def get_data_from_collection(self, collection_address: str) -> bool | list:
        """Returns data of the selected collection from the database."""

        response = requests.get(url=collection_address, headers=self.HEADERS)
        if response.status_code != 200:
            return False
        else:
            return response.json()

    @get_connect
    def delete_doc_from_collection(self, collection_address: str) -> bool:
        """
        Delete data of the selected collection from the database.

        :param collection_address: "database_url/id_collection".
        """

        response = requests.delete(collection_address, headers=self.HEADERS)
        if response.status_code == 200:
            return True
        else:
            return False

    @get_connect
    def add_doc_to_collection(
        self, data: dict, collection_address: str
    ) -> bool:
        """Add collection to the database."""

        response = requests.post(
            url=collection_address,
            data=json.dumps(data),
            headers=self.HEADERS,
        )
        if response.status_code == 201:
            if "_id" in response.json():
                return response.json()
        else:
            return False

    @get_connect
    def edit_data(
        self, collection: dict, collection_address: str, collection_id: str
    ) -> bool:
        """Modifies data in a collection of data in a database."""

        response = requests.put(
            url=f"{collection_address}/{collection_id}",
            headers=self.HEADERS,
            json=collection,
        )
        if response.status_code == 200:
            if "_id" in response.json():
                return True
        else:
            return False
