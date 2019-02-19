# Details of Notification

You can view the details of a single notification.

```python
notification = SegmentNotification(...)
client.send(notification)
details = client.details(notification)
```

```python
{
    'adm_big_picture': None,
    'adm_group': None,
    'adm_group_message': None,
    'adm_large_icon': None,
    ...
    'contents': {
        'de': 'Hallo Welt',
        'en': 'Hello World'
    },
    'send_after': 1532629946,
    'platform_delivery_stats': {}
}
```