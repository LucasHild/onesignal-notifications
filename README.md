# OneSignal-Notifications

![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/onesignal-notifications.svg?style=flat-square&colorB=dfb317)](https://pypi.org/project/onesignal-notifications/)

OneSignal-Notifications is a wrapper for the OneSignal API which allows you to send notifications for Android, iOS and Web App.

## Installation

```
pip install onesignal-notifications
```

## Usage

```python
from onesignal import OneSignal, SegmentNotification

client = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
notification_to_all_users = SegmentNotification(
    {
        "en": "Hello from OneSignal-Notifications"
    },
    included_segments=SegmentNotification.ALL
)
```

## Meta

Lucas Hild - [https://lucas-hild.de](https://lucas.hild.de)  
This project is licensed under the MIT License - see the LICENSE file for details
