# Getting started

## Sign up

For sending push notifications, you need an account for OneSignal. Head over to [OneSignal.com](https://onesignal.com) and sign up. Next you will have to choose a new name for your new application.

## Get API keys

In the top navigation bar, you will find a link to the settings. One the right, you will see the tab "Keys & IDs". Grab your app id and your rest api key. You will need it in the next step.

![](./keys_and_ids.png)

## Connect Python to OneSignal

Next you will have to install OneSignal-Notifications using pip.

```
pip install onesignal-notifications
```

In your Python script you can now import `onesignal` and create a new instance of `OneSignal` using your app id and your rest api key.

```python
from onesignal import OneSignal

client = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
```

**Remember not to put your rest api key on GitHub**! Otherwise everyone will be able to send notifications from your account to your users!

The best practise to avoid that is to create a seperat file called `config.py` or `secret.py`, that you put in `.gitignore`.

```python
# config.py

onesignal_app_id = "MY_APP_ID"
onesignal_rest_api_key = "MY_REST_API_KEY"
```

Then you can import the variable in the main file.

```python
import config
from onesignal import OneSignal

client = OneSignal(config.onesignal_app_id, config.onesignal_rest_api_key)
```