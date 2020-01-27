from .notification import Notification, common_notification_paramenters
from .filter import Filter
from .utils import merge_dicts


class FilterNotification(Notification):
    """Notification based on specific filters

    Attributes:
        filters
        {common_notification_paramenters}
    """.format(common_notification_paramenters=common_notification_paramenters)

    def __init__(self, filters, **kwargs):
        Notification.__init__(self, **kwargs)
        self.filters = []

        for filter in filters:
            if filter == "OR":
                self.filters.append({"operator": "OR"})

            elif filter == "AND":
                continue

            else:
                self.filters.append(filter.data)

    def get_data(self):
        return merge_dicts(
            self.get_common_data(),
            {"filters": self.filters}
        )
