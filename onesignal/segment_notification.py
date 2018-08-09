from .notification import Notification, common_notification_paramenters


class SegmentNotification(Notification):
    f"""Notification based on specific filters

    Attributes:
        included_segment
        excluded_segments
        {common_notification_paramenters}
    """

    ALL = "All"
    ACTIVE_USERS = "Active Users"
    ENGAGED_USERS = "Engaged Users"
    INACTIVE_USERS = "Inactive Users"

    def __init__(self,
                 included_segments=None,
                 excluded_segments=None,
                 **kwargs):
        super().__init__(**kwargs)
        self.included_segments = included_segments
        self.excluded_segments = excluded_segments

    def get_data(self):
        return {
            "included_segments": self.included_segments,
            "excluded_segments": self.excluded_segments,
            **self.get_common_data()
        }
