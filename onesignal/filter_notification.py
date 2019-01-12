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

        next_operator = None
        for index, filter in enumerate(filters):
            if isinstance(filter, Filter):
                if not next_operator:
                    self.filters.append(filter.data)

                else:
                    self.filters.append(
                        merge_dicts(
                            filter.data,
                            {"operator": next_operator}
                        )
                    )

                    next_operator = None

            elif isinstance(filter, str):
                next_operator = filter

    def get_data(self):
        return merge_dicts(
            self.get_common_data(),
            {"filters": self.filters}
        )
