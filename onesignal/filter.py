class Filter:
    pass


class LastSession(Filter):
    """Filtered by the last session of the user

    Arguments:
        relation: "<" or ">"
        hours_ago: number of hours before or after the users last session
    """

    def __init__(self, relation, hours_ago):
        self.data = {
            "field": "last_session",
            "relation": relation,
            "hours_ago": hours_ago
        }


class FirstSession(Filter):
    """Filtered by the first session of the user

    Arguments:
        relation: "<" or ">"
        hours_ago: number of hours before or after the users last session
    """

    def __init__(self, relation, hours_ago):
        self.data = {
            "field": "first_session",
            "relation": relation,
            "hours_ago": hours_ago
        }


class SessionCount(Filter):
    """Filtered by amount of sessions

    Arguments:
        relation: "<", ">", "=" or "!="
        value: time in seconds the user has been in your app
    """

    def __init__(self, relation, value):
        self.data = {
            "field": "session_count",
            "value": value
        }


class SessionTime(Filter):
    """Filtered by time the user has been in app

    Arguments:
        relation: "<" or ">"
        value: time in seconds the user has been in your app
    """

    def __init__(self, relation, value):
        self.data = {
            "field": "session_time",
            "value": value
        }


class AmountSpent(Filter):
    """Filtered by amount spent on IAP

    Arguments:
        relation: "<", ">" or "="
        value: amount in USD a user has spent on IAP (In App Purchases)
    """

    def __init__(self, relation, value):
        self.data = {
            "field": "amount_spent",
            "value": value
        }


class BoughtSku(Filter):
    """Filtered by SKU purchased

    Arguments:
        relation: "<",  ">" or "="
        key: SKU purchased in your app as an IAP (In App Purchases)
        value: value of SKU to compare to
    """

    def __init__(self, relation, key, value):
        self.data = {
            "field": "bought_sku",
            "relation": relation,
            "key": key,
            "value": value
        }


class Tag(Filter):
    """Filtered by tag

    Arguments:
        relation: "<", ">", "=", "!=", "exists" or "not_exists"
        key: tag to compare
        value: time in seconds the user has been in your app
    """

    def __init__(self, key, relation, value):
        self.data = {
            "field": "tag",
            "key": key,
            "relation": relation,
            "value": value
        }


class Language(Filter):
    """Filtered by language of user

    Arguments:
        relation: "=" or "!="
        value: 2 character language code
    """

    def __init__(self, relation, value):
        self.data = {
            "field": "language",
            "relation": relation,
            "value": value
        }


class AppVersion(Filter):
    """Filtered by version of the app

    Arguments:
        relation: "<", ">", "=" or "!="
        value: app version
    """

    def __init__(self, relation, value):
        self.data = {
            "field": "app_version",
            "relation": relation,
            "value": value
        }


class Location(Filter):
    """Filtered by location of the user

    Arguments:
        radius: in meters
        lat: latitude
        long: longitude
    """

    def __init__(self, radius, lat, long):
        self.data = {
            "field": "location",
            "radius": radius,
            "lat": lat,
            "long": long
        }


class Email(Filter):
    """Filtered by time the user has been in app

    For email targeting only, not used to send push notifications

    Arguments:
        value: email address
    """

    def __init__(self, value):
        self.data = {
            "field": "email",
            "value": value
        }


class Country(Filter):
    """Filtered by country of the user

    Arguments:
        relation: "="
        value: 2 character country code
    """

    def __init__(self, value):
        self.data = {
            "field": "country",
            "value": value
        }
