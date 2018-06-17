import onesignal


def test_initialize():
    client = onesignal.OneSignal("", "")
    assert isinstance(client, onesignal.OneSignal)
