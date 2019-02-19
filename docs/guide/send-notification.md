# Send Notifications

There are different types of notifications:

- You can send a [`SegmentNotification`](segment-notification.html) to a specific segment of users. For example to all users.
- You can send a [`FilterNotification`](filter-notification.html) based on filters. For example only users who have a specific version of the app.
- You can send a [`DeviceNotification`](device-notification.html) to specific devices using their id.

Let's send a notification to all users. If the users clicks on the notification, GitHub opens.

```python
from onesignal import OneSignal, SegmentNotification

client = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
notification_to_all_users = SegmentNotification(
    contents={
        "en": "Hello from OneSignal-Notifications"
    },
    included_segments=SegmentNotification.ALL,
    url="https://github.com"
)
client.send(notification_to_all_users)
```

## Common parameters

### Notification Content

- contents
- headings
- subtitle
- template_id
- content_available
- mutable_content

[More details](https://documentation.onesignal.com/reference#section-content-language)

### E-Mail Content

- email_body
- email_subject
- email_from_name
- email_from_address
- email_from_address

[More details](https://documentation.onesignal.com/reference#section-email-content)

### Attachments

- data
- url
- ios_attachments
- big_picture
- adm_big_picture
- chrome_big_picture

[More details](https://documentation.onesignal.com/reference#section-attachments)

### Action Buttons

- buttons
- web_buttons
- ios_category

[More details](https://documentation.onesignal.com/reference#section-action-buttons)

### Appearance

- android_channel_id
- existing_android_channel_id
- android_background_layout
- small_icon
- large_icon
- adm_small_icon
- adm_large_icon
- chrome_web_icon
- chrome_web_image
- chrome_web_badge
- firefox_icon
- chrome_icon
- ios_sound
- android_sound
- adm_sound
- wp_sound
- wp_wns_sound
- android_led_color
- android_accent_color
- android_visibility (available values: `Notification.ANDROID_VISIBILITY_PUBLIC`, `Notification.ANDROID_VISIBILITY_PRIVATE`, `Notification.ANDROID_VISIBILITY_SECRET`)
- ios_badge_type (available values: `Notification.IOS_BADGE_TYPE_NONE`, `Notification.IOS_BADGE_TYPE_SET_TO`, `Notification.IOS_BADGE_TYPE_INCREASE`)
- ios_badge_count
- collapse_id
- apns_alert

[More details](https://documentation.onesignal.com/reference#section-appearance)

### Delivery

- send_after
- delayed_option (available values: `Notification.DELAYED_OPTION_TIMEZONE`, `Notification.DELAYED_OPTION_LAST_ACTIVE`)
- delivery_time_of_day
- ttl
- priority

[More details](https://documentation.onesignal.com/reference#section-delivery)

### Grouping & Collapsing

- android_group
- android_group_message
- adm_group
- adm_group_message

[More details](https://documentation.onesignal.com/reference#section-grouping-collapsing)

### Platform to Deliver To

- is_ios
- is_android
- is_any_web
- is_email
- is_chrome_web
- is_firefox
- is_wp
- is_wp_wns
- is_adm
- is_chrome

[More details](https://documentation.onesignal.com/reference#section-platform-to-deliver-to)
