from .notification import Notification
from .filter import Filter


class FilterNotification(Notification):
    def __init__(self,
                 contents,
                 filters):
        self.contents = contents
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
