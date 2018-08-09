from .notification import Notification, common_notification_paramenters
from .filter import Filter


class FilterNotification(Notification):
    f"""Notification based on specific filters

    Attributes:
        filters
        {common_notification_paramenters}
    """

    def __init__(self, filters, **kwargs):
        super().__init__(**kwargs)
        self.filters = []

        next_operator = None
        for index, filter in enumerate(filters):
            if isinstance(filter, Filter):
                if not next_operator:
                    self.filters.append(filter.data)
                else:
                    self.filters.append({
                        **filter.data,
                        **{"operator": next_operator}
                    })
                    next_operator = None

            elif isinstance(filter, str):
                next_operator = filter

        print(self.filters)

    def get_data(self):
        return {
            **self.get_common_data,
            "filters": self.filters
        }
