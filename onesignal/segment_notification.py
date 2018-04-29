from .notification import Notification


class SegmentNotification(Notification):
    ALL = "All"

    def __init__(self, contents, included_segments=None, excluded_segments=None):
        self.contents = contents
        self.included_segments = included_segments
        self.excluded_segments = excluded_segments

    def _get_json(self):
        return {
            "included_segments": self.included_segments,
            "contents": self.contents,
            "excluded_segments": self.excluded_segments
        }
