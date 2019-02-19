# Cancel Notifications

You can stop a scheduled or currently outgoing notification.

```python
notification = SegmentNotification(...)
client.send(notification)
client.cancel(notification)
```

## By Id

If you want to delete a notification, that was not sent using `onesignal-notifications`, you can delete it by it's id.

```python
client.cancel("12345678-1234-1234-1234-123456789012")
```