import onesignal
import os

# Put your own credentials here
client = onesignal.OneSignal(
    os.environ["ONESIGNAL_API_KEY"],
    os.environ["ONESIGNAL_REST_API_KEY"]
)


def test_initialize():
    assert isinstance(client, onesignal.OneSignal)


def test_send():
    notification = onesignal.SegmentNotification(
        contents={"en": "Hello World"},
        included_segments=[onesignal.SegmentNotification.ALL]
    )
    assert client.send(notification)


def test_cancel():
    notification = onesignal.SegmentNotification(
        contents={"en": "Hello World"},
        included_segments=[onesignal.SegmentNotification.ALL]
    )

    try:
        client.cancel(notification)
        assert False, (
            "Notification was not sent yet, "
            "but was on it's way to be canceled"
        )
    except ValueError:
        pass

    client.send(notification)
    assert client.cancel(notification)


def test_details():
    notification = onesignal.SegmentNotification(
        contents={"en": "Hello World"},
        included_segments=onesignal.SegmentNotification.ALL
    )
    client.send(notification)
    details = client.details(notification)
    assert "is_chrome_web" in details.keys()
