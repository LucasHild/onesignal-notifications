import onesignal

# Put your own credentials here
client = onesignal.OneSignal("", "")


def test_initialize():
    assert isinstance(client, onesignal.OneSignal)


def test_send():
    notification = onesignal.SegmentNotification(
        included_segments=onesignal.SegmentNotification.ALL,
        contents={"en": "Hello World"}
    )
    assert client.send(notification)


def test_cancel():
    notification = onesignal.SegmentNotification(
        included_segments=onesignal.SegmentNotification.ALL,
        contents={"en": "Hello World"}
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
