import pytest

from onesignal import FilterNotification, Filter


@pytest.fixture
def notification():
    return FilterNotification(
        contents={
            "en": "Hello from OneSignal-Notifications"
        },
        filters=[
            Filter.Tag("my_key", "<", "5"),
            "AND",
            Filter.AppVersion(">", "5"),
            "OR",
            Filter.LastSession(">", "1"),
        ]
    )


def test_get_data(notification):
    data = notification.get_data()
    assert data["contents"] == {"en": "Hello from OneSignal-Notifications"}
    assert data["filters"] == [
        {
            "field": "tag",
            "key": "my_key",
            "relation": "<",
            "value": "5"
        },
        {
            "field": "app_version",
            "operator": "AND",
            "relation": ">",
            "value": "5"
        },
        {
            "field": "last_session",
            "hours_ago": "1",
            "operator": "OR",
            "relation": ">"
        }
    ]


def test_send_notification(client, notification):
    client.send(notification)
