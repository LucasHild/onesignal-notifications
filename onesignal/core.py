import requests


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
        return r.json()

    def send(self, notification):
        data = {**notification._get_json(), **{"app_id": self.app_id}}
        return self._post("notifications", json=data)
