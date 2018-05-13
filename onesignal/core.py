import requests

from .errors import OneSignalAPIError


class OneSignal:
    base_api = "https://onesignal.com/api/v1/"

    def __init__(self, app_id, rest_api_key):
        self.app_id = app_id
        self.rest_api_key = rest_api_key

    def _post(self, endpoint, json):
        r = requests.post(self.base_api + endpoint,
                          json=json,
                          headers={
                              "Authorization": "Basic " + self.rest_api_key
                          })

        if r.status_code != 200:
            raise OneSignalAPIError(r.json())

        return r.json()

    def send(self, notification):
        if isinstance(self.app_id, str):
            app_id_obj = {"app_id": self.app_id}
        elif isinstance(self.app_id, list):
            app_id_obj = {"app_ids": self.app_id}

        data = {**notification.get_data(), **app_id_obj}
        return self._post("notifications", json=data)
