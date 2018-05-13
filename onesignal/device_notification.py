from .notification import Notification


class DeviceNotification(Notification):
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
                 **kwargs):
        super().__init__(**kwargs)
        self.include_player_ids = include_player_ids
        self.include_email_tokens = include_email_tokens
        self.include_ios_tokens = include_ios_tokens
        self.include_wp_urls = include_wp_urls
        self.include_wp_wns_uris = include_wp_wns_uris
        self.include_amazon_reg_ids = include_amazon_reg_ids
        self.include_chrome_reg_ids = include_chrome_reg_ids
        self.include_chrome_web_reg_ids = include_chrome_web_reg_ids
        self.include_android_reg_ids = include_android_reg_ids

    def get_data(self):
        return {
            "include_player_ids": self.include_player_ids,
            "include_email_tokens": self.include_email_tokens,
            "include_ios_tokens": self.include_ios_tokens,
            "include_wp_urls": self.include_wp_urls,
            "include_wp_wns_uris": self.include_wp_wns_uris,
            "include_amazon_reg_ids": self.include_amazon_reg_ids,
            "include_chrome_reg_ids": self.include_chrome_reg_ids,
            "include_chrome_web_reg_ids": self.include_chrome_web_reg_ids,
            "include_android_reg_ids": self.include_android_reg_ids,
            **self.get_common_data()
        }
