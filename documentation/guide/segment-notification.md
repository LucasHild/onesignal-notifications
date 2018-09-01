# SegmentNotification

You can send a `SegmentNotification` to a specific segment of users. For example to all users.

Let's send a notification to all active users. If the users clicks on the notification, GitHub opens.

```python
from onesignal import OneSignal, SegmentNotification

client = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
notification_to_all_active_users = SegmentNotification(
    contents={
        "en": "Hello from OneSignal-Notifications"
    },
    included_segments=SegmentNotification.ACTIVE_USERS,
    web_buttons=[
        {
            "id": "like-button",
            "text": "Like",
            "icon": "http://i.imgur.com/N8SN8ZS.png",
            "url": "https://github.com"
        },
        {
            "id": "read-more-button",
            "text": "Read more",
            "icon": "http://i.imgur.com/MIxJp1L.png",
            "url": "https://github.com"
        }
    ]
)
client.send(notification_to_all_active_users)
```

## Parameters

- included_segments (available values: `SegmentNotification.ALL`, `SegmentNotification.ACTIVE_USERS`, `SegmentNotification.ENGAGED_USERS` `SegmentNotification.INACTIVE_USERS`, your own segment)
- excluded_segments (available values: `SegmentNotification.ALL`, `SegmentNotification.ACTIVE_USERS`, `SegmentNotification.ENGAGED_USERS` `SegmentNotification.INACTIVE_USERS`, your own segment)

[More details](https://documentation.onesignal.com/reference#section-send-to-segments)
