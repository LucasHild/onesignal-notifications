import datetime
import re


class Notification:
    ANDROID_VISIBILITY_PUBLIC = 1
    ANDROID_VISIBILITY_PRIVATE = 0
    ANDROID_VISIBILITY_SECRET = -1
    IOS_BADGE_TYPE_NONE = None
    IOS_BADGE_TYPE_SET_TO = "SetTo"
    IOS_BADGE_TYPE_INCREASE = "Increase"
    DELAYED_OPTION_TIMEZONE = "timezone"
    DELAYED_OPTION_LAST_ACTIVE = "last-active"

    def __init__(self,
                 contents=None,
                 headings=None,
                 subtitle=None,
                 template_id=None,
                 content_available=None,
                 mutable_content=None,
                 email_body=None,
                 email_subject=None,
                 email_from_name=None,
                 email_from_address=None,
                 data=None,
                 url=None,
                 ios_attachments=None,
                 big_picture=None,
                 adm_big_picture=None,
                 chrome_big_picture=None,
                 buttons=None,
                 web_buttons=None,
                 ios_category=None,
                 android_channel_id=None,
                 existing_android_channel_id=None,
                 android_background_layout=None,
                 small_icon=None,
                 large_icon=None,
                 adm_small_icon=None,
                 adm_large_icon=None,
                 chrome_web_icon=None,
                 chrome_web_image=None,
                 chrome_web_badge=None,
                 firefox_icon=None,
                 chrome_icon=None,
                 ios_sound=None,
                 android_sound=None,
                 adm_sound=None,
                 wp_sound=None,
                 wp_wns_sound=None,
                 android_led_color=None,
                 android_accent_color=None,
                 android_visibility=None,
                 ios_badge_type=None,
                 ios_badge_count=None,
                 collapse_id=None,
                 apns_alert=None,
                 send_after=None,
                 delayed_option=None,
                 delivery_time_of_day=None,
                 ttl=None,
                 priority=None,
                 android_group=None,
                 android_group_message=None,
                 adm_group=None,
                 adm_group_message=None,
                 is_ios=None,
                 is_android=None,
                 is_any_web=None,
                 is_email=None,
                 is_chrome_web=None,
                 is_firefox=None,
                 is_safari=None,
                 is_wp=None,
                 is_wp_wns=None,
                 is_adm=None,
                 is_chrome=None):

        self.check_type(contents, "contents", dict)
        self.check_type(headings, "headings", dict)
        self.check_type(subtitle, "subtitle", dict)
        self.check_type(template_id, "template_id", str)
        self.check_type(content_available, "content_available", bool)
        self.check_type(mutable_content, "mutable_content", bool)

        assert contents or content_available is True or template_id, \
            "'contents' is required unless content_available=True " \
            "or template_id is set"

        self.content_data = {
            "contents": contents,
            "headings": headings,
            "subtitle": subtitle,
            "template_id": template_id,
            "content_available": content_available,
            "mutable_content": mutable_content,
        }

        self.check_type(email_body, "email_body", str)
        self.check_type(email_subject, "email_subject", str)
        self.check_type(email_from_name, "email_from_name", str)
        self.check_type(email_from_address, "email_from_address", str)

        assert not email_from_address or re.search(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
            email_from_address
        ), \
            "'email_from_address' is not a valid mail address"

        self.email_content_data = {
            "email_body": email_body,
            "email_subject": email_subject,
            "email_from_name": email_from_name,
            "email_from_address": email_from_address
        }

        self.check_type(data, "data", dict)
        self.check_type(url, "url", str)
        self.check_type(ios_attachments, "ios_attachments", dict)
        self.check_type(big_picture, "big_picture", str)
        self.check_type(adm_big_picture, "data", str)
        self.check_type(chrome_big_picture, "data", str)

        self.attachments_data = {
            "data": data,
            "url": url,
            "ios_attachments": ios_attachments,
            "big_picture": big_picture,
            "adm_big_picture": adm_big_picture,
            "chrome_big_picture": chrome_big_picture
        }

        self.check_type(buttons, "buttons", list)
        self.check_type(web_buttons, "web_buttons", list)
        self.check_type(ios_category, "ios_category", str)

        self.action_buttons_data = {
            "buttons": buttons,
            "web_buttons": web_buttons,
            "ios_category": ios_category
        }

        self.check_type(existing_android_channel_id,
                        "existing_android_channel_id", str)
        self.check_type(android_background_layout,
                        "android_background_layout", dict)
        self.check_type(small_icon, "small_icon", str)
        self.check_type(large_icon, "large_icon", str)
        self.check_type(adm_small_icon, "adm_small_icon", str)
        self.check_type(adm_large_icon, "adm_large_icon", str)
        self.check_type(firefox_icon, "firefox_icon", str)
        self.check_type(chrome_icon, "chrome_icon", str)
        self.check_type(ios_sound, "ios_sound", str)
        self.check_type(android_sound, "android_sound", str)
        self.check_type(adm_sound, "adm_sound", str)
        self.check_type(wp_sound, "wp_sound", str)
        self.check_type(wp_wns_sound, "wp_wns_sound", str)
        self.check_type(android_led_color, "android_led_color", str)
        self.check_type(android_accent_color, "android_accent_color", str)
        self.check_type(android_visibility, "android_visibility", int)
        assert android_visibility in [1, 0, -1] or not android_visibility, \
            "'android_visibility' has to 1, 0 or -1"
        self.check_type(ios_badge_type, "ios_badge_type", str)
        self.check_type(ios_badge_count, "ios_badge_count", int)
        self.check_type(collapse_id, "collapse_id", str)
        self.check_type(apns_alert, "apns_alert", dict)

        self.appearance_data = {
            "android_channel_id": android_channel_id,
            "existing_android_channel_id": existing_android_channel_id,
            "android_background_layout": android_background_layout,
            "small_icon": small_icon,
            "large_icon": large_icon,
            "adm_small_icon": adm_small_icon,
            "adm_large_icon": adm_large_icon,
            "chrome_web_icon": chrome_web_icon,
            "chrome_web_image": chrome_web_image,
            "chrome_web_badge": chrome_web_badge,
            "firefox_icon": firefox_icon,
            "chrome_icon": chrome_icon,
            "ios_sound": ios_sound,
            "android_sound": android_sound,
            "adm_sound": adm_sound,
            "wp_sound": wp_sound,
            "wp_wns_sound": wp_wns_sound,
            "android_led_color": android_led_color,
            "android_accent_color": android_accent_color,
            "android_visibility": android_visibility,
            "ios_badgeType": ios_badge_type,
            "ios_badgeCount": ios_badge_count,
            "collapse_id": collapse_id,
            "apns_alert": apns_alert
        }

        assert isinstance(send_after, datetime.datetime) or not send_after, \
            "'send_after' has to be an instance of datetime.datetime"
        if send_after:
            send_after = send_after.strftime('%Y-%m-%d %H:%M:%S %Z')
        self.check_type(delayed_option, "delayed_option", str)
        self.check_type(delivery_time_of_day, "delivery_time_of_day", str)
        self.check_type(ttl, "ttl", int)
        self.check_type(priority, "priority", int)

        self.delivery_data = {
            "send_after": send_after,
            "delayed_option": delayed_option,
            "delivery_time_of_day": delivery_time_of_day,
            "ttl": ttl,
            "priority": priority
        }

        self.check_type(android_group, "android_group", str)
        self.check_type(android_group_message, "android_group_message", dict)
        self.check_type(adm_group, "adm_group", str)
        self.check_type(adm_group_message, "adm_group_message", dict)

        self.grouping_and_collapsing_data = {
            "android_group": android_group,
            "android_group_message": android_group_message,
            "adm_group": adm_group,
            "adm_group_message": adm_group_message
        }

        self.check_type(is_ios, "is_ios", bool)
        self.check_type(is_android, "is_android", bool)
        self.check_type(is_any_web, "is_any_web", bool)
        self.check_type(is_email, "is_email", bool)
        self.check_type(is_chrome_web, "is_chrome_web", bool)
        self.check_type(is_firefox, "is_firefox", bool)
        self.check_type(is_safari, "is_safari", bool)
        self.check_type(is_wp, "is_wp", bool)
        self.check_type(is_wp_wns, "is_wp_wns", bool)
        self.check_type(is_adm, "is_adm", bool)
        self.check_type(is_chrome, "is_chrome", bool)

        self.platform_to_deliver_to_data = {
            "isIos": is_ios,
            "isAndroid": is_android,
            "isAnyWeb": is_any_web,
            "isEmail": is_email,
            "isChromeWeb": is_chrome_web,
            "isFirefox": is_firefox,
            "isWP": is_wp,
            "isWP_WNS": is_wp_wns,
            "isAdm": is_adm,
            "isChrome": is_chrome
        }

    def check_type(self, variable, variable_string, type):

        class_of_variable = str(type().__class__)[8:-2]

        if variable is not None:
            assert isinstance(variable, type), \
                "'{}' has to be a {}".format(
                    variable_string, class_of_variable)

    def get_common_data(self):
        return {
            **self.content_data,
            **self.email_content_data,
            **self.attachments_data,
            **self.action_buttons_data,
            **self.appearance_data,
            **self.delivery_data,
            **self.grouping_and_collapsing_data,
            **self.platform_to_deliver_to_data
        }
