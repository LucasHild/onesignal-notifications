import requests

from .errors import OneSignalAPIError


class OneSignal:
    base_api = "https://onesignal.com/api/v1/"

    def __init__(self, app_id, rest_api_key):
        self.app_id = app_id
        self.rest_api_key = rest_api_key

    def request(self, method, endpoint, json={}):
        r = requests.request(
            method,
            self.base_api + endpoint,
            json=json,
            headers={
                "Authorization": "Basic " + self.rest_api_key
            }
        )

        if r.status_code != 200:
            raise OneSignalAPIError(r.json())

        return r.json()

    def send(self, notification):
        if isinstance(self.app_id, str):
            app_id_obj = {"app_id": self.app_id}
        elif isinstance(self.app_id, list):
            app_id_obj = {"app_ids": self.app_id}

        data = {**notification.get_data(), **app_id_obj}
        response = self.request("post", "notifications", json=data)

        notification.id = response["id"]

        return response

    def cancel(self, notification):
        if isinstance(notification, str):
            notification_id = notification
        else:
            if not notification.id:
                raise ValueError("The notification was propably not sent yet")
            notification_id = notification.id

        response = self.request(
            "delete",
            "notifications/" + notification_id + "?app_id=" + self.app_id
        )

        return response

    def details(self, notification):
        if isinstance(notification, str):
            notification_id = notification
        else:
            if not notification.id:
                raise ValueError("The notification was propably not sent yet")
            notification_id = notification.id

        response = self.request(
            "get",
            "notifications/" + notification_id + "?app_id=" + self.app_id
        )

        result = {}
        for key in response.keys():
            result[self.to_underscore(key)] = response[key]

        return result

    def to_underscore(self, var):
        result = ""
        for letter in var:
            if letter == letter.lower():
                result += letter
            else:
                result += "_" + letter.lower()
        return result
