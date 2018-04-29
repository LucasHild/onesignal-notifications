class Filter:
    pass


class LastSession(Filter):
    def __init__(self, relation, hours_ago):
        self.data = {
            "field": "last_session",
            "relation": relation,
            "hours_ago": hours_ago
        }


class FirstSession(Filter):
    def __init__(self, relation, hours_ago):
        self.data = {
            "field": "first_session",
            "relation": relation,
            "hours_ago": hours_ago
        }


class SessionCount(Filter):
    def __init__(self, relation, value):
        self.data = {
            "field": "session_count",
            "value": value
        }


class SessionTime(Filter):
    def __init__(self, relation, value):
        self.data = {
            "field": "session_time",
            "value": value
        }


class AmountSpent(Filter):
    def __init__(self, relation, value):
        self.data = {
            "field": "amount_spent",
            "value": value
        }


class BoughtSku(Filter):
    def __init__(self, key, relation, value):
        self.data = {
            "field": "bought_sku",
            "key": key,
            "relation": relation,
            "value": value
        }


class Tag(Filter):
    def __init__(self, key, relation, value):
        self.data = {
            "field": "tag",
            "key": key,
            "relation": relation,
            "value": value
        }


class Language(Filter):
    def __init__(self, relation, value):
        self.data = {
            "field": "language",
            "relation": relation,
            "value": value
        }


class AppVersion(Filter):
    def __init__(self, relation, value):
        self.data = {
            "field": "app_version",
            "relation": relation,
            "value": value
        }


class Location(Filter):
    def __init__(self, radius, lat, long):
        self.data = {
            "field": "location",
            "radius": radius,
            "lat": lat,
            "long": long
        }


class Email(Filter):
    def __init__(self, value):
        self.data = {
            "field": "email",
            "value": value
        }


class Country(Filter):
    def __init__(self, value):
        self.data = {
            "field": "country",
            "value": value
        }
