from .notification import Notification, common_notification_paramenters
from itertools import chain


class SegmentNotification(Notification):
    """Notification based on specific filters

    Attributes:
        included_segment
        excluded_segments
        {common_notification_paramenters}
    """.format(common_notification_paramenters=common_notification_paramenters)

    ALL = "All"
    ACTIVE_USERS = "Active Users"
    ENGAGED_USERS = "Engaged Users"
    INACTIVE_USERS = "Inactive Users"

    def __init__(self,
                 included_segments=None,
                 excluded_segments=None,
                 **kwargs):
        Notification.__init__(self, **kwargs)
        self.included_segments = included_segments
        self.excluded_segments = excluded_segments

    def get_data(self):
        return dict(chain({
            "included_segments": self.included_segments,
            "excluded_segments": self.excluded_segments
        }.items(), self.get_common_data().items()))
