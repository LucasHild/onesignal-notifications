# OneSignal SDK for Python

![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/onesignal-notifications.svg?style=flat-square&colorB=dfb317)](https://pypi.org/project/onesignal-notifications/)

OneSignal-Notifications is a wrapper for the OneSignal API which allows you to send notifications to Android, iOS and Web App.

## Installation

```
pip install onesignal-notifications
```

## Usage

```python
from onesignal import OneSignal, SegmentNotification

client = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
notification_to_all_users = SegmentNotification(
    contents={
        "en": "Hello from OneSignal-Notifications"
    },
    included_segments=SegmentNotification.ALL
)
client.send(notification_to_all_users)
```

<p style="text-align: right"><a href="guide/">Learn more</a> →</p>
