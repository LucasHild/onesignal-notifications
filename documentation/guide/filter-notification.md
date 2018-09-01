# FilterNotification

You can send a `FilterNotification` based on filters. For example only users who have a specific version of the app.

Let's send a notification to all users, where `my_key` is less than 5, the version of the app is greater than 5 or their lass session is older than one hour.

```python
from onesignal import OneSignal, FilterNotification

client = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
filter_notification = FilterNotification(
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
client.send(filter_notification)
```

## Parameters

- last_session
- first_session
- session_count
- session_time
- amount_spent
- bought_sku
- tag
- language
- app_version
- location
- email
- country

[More details](https://documentation.onesignal.com/reference#section-send-to-users-based-on-filters)
