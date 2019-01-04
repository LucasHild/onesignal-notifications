# DeviceNotification

You can send a DeviceNotification to specific devices using their id.

Let's send a notification to all active users. If the users clicks on the notification, GitHub opens.

```python
from onesignal import OneSignal, DeviceNotification

client = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
notification_to_users = DeviceNotification(
    contents={
        "en": "Hello from OneSignal-Notifications"
    },
    include_player_ids=["1dd608f2-c6a1-11e3-851d-000c2940e62c", "5ha618p8-c6a1-12x7-891z-000d1230ee51"]
)
client.send(notification_to_users)
```

## Parameters

- include_player_ids
- include_email_tokens
- include_ios_tokens
- include_wp_urls
- include_wp_wns_uris
- include_amazon_reg_ids
- include_chrome_reg_ids
- include_chrome_web_reg_ids
- include_android_reg_ids

[More details](https://documentation.onesignal.com/reference#section-send-to-specific-devices)
