from .notification import Notification, common_notification_paramenters
from .utils import merge_dicts


class DeviceNotification(Notification):
    """Notification to a specific device using their id

    Attributes:
        include_player_ids
        include_email_tokens
        include_ios_tokens
        include_wp_urls
        include_wp_wns_uris
        include_amazon_reg_ids
        include_chrome_reg_ids
        include_chrome_web_reg_ids
        include_android_reg_ids
        include_external_user_ids
        {common_notification_paramenters}
    """.format(common_notification_paramenters=common_notification_paramenters)

    def __init__(self,
                 include_player_ids=None,
                 include_email_tokens=None,
                 include_ios_tokens=None,
                 include_wp_urls=None,
                 include_wp_wns_uris=None,
                 include_amazon_reg_ids=None,
                 include_chrome_reg_ids=None,
                 include_chrome_web_reg_ids=None,
                 include_android_reg_ids=None,
                 include_external_user_ids=None,
                 **kwargs):
        Notification.__init__(self, **kwargs)
        self.include_player_ids = include_player_ids
        self.include_email_tokens = include_email_tokens
        self.include_ios_tokens = include_ios_tokens
        self.include_wp_urls = include_wp_urls
        self.include_wp_wns_uris = include_wp_wns_uris
        self.include_amazon_reg_ids = include_amazon_reg_ids
        self.include_chrome_reg_ids = include_chrome_reg_ids
        self.include_chrome_web_reg_ids = include_chrome_web_reg_ids
        self.include_android_reg_ids = include_android_reg_ids
        self.include_external_user_ids = include_external_user_ids

    def get_data(self):
        return merge_dicts(
            self.get_common_data(),
            {
                "include_player_ids": self.include_player_ids,
                "include_email_tokens": self.include_email_tokens,
                "include_ios_tokens": self.include_ios_tokens,
                "include_wp_urls": self.include_wp_urls,
                "include_wp_wns_uris": self.include_wp_wns_uris,
                "include_amazon_reg_ids": self.include_amazon_reg_ids,
                "include_chrome_reg_ids": self.include_chrome_reg_ids,
                "include_chrome_web_reg_ids": self.include_chrome_web_reg_ids,
                "include_android_reg_ids": self.include_android_reg_ids,
                "include_external_user_ids": self.include_external_user_ids
            }
        )
