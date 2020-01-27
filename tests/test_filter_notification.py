import pytest

from onesignal import FilterNotification, Filter


@pytest.fixture
def example_notifications():
    notification1 = FilterNotification(
        contents={
            "en": "Hello from OneSignal-Notifications"
        },
        filters=[
            Filter.Tag("my_key", "<", "5"),
            "AND",
            Filter.AppVersion(">", "5")
        ]
    )

    notification2 = FilterNotification(
        contents={
            "en": "Hello from OneSignal-Notifications"
        },
        filters=[
            Filter.AppVersion(">", "5"),
            "OR",
            Filter.LastSession(">", "1")
        ]
    )

    return notification1, notification2


def test_get_data(example_notifications):
    notification1, notification2 = example_notifications

    data1 = notification1.get_data()
    assert data1["contents"] == {"en": "Hello from OneSignal-Notifications"}
    assert data1["filters"] == [
        {
            "field": "tag",
            "key": "my_key",
            "relation": "<",
            "value": "5"
        },
        {
            "field": "app_version",
            "relation": ">",
            "value": "5"
        }
    ]

    data2 = notification2.get_data()
    assert data2["contents"] == {"en": "Hello from OneSignal-Notifications"}
    assert data2["filters"] == [
        {
            "field": "app_version",
            "relation": ">",
            "value": "5"
        },
        {
            "operator": "OR"
        },
        {
            "field": "last_session",
            "hours_ago": "1",
            "relation": ">"
        }
    ]


def test_send_notification(client, example_notifications):
    notification1, notification2 = example_notifications

    client.send(notification1)
    client.send(notification2)
