import json
from tpns.common import ZONE_GZ
from tpns import Push
from tpns.core.authenticators import BasicAuthenticator


#test zgq
username = 1500001533
password = "euwhfy3zyi3hvahkf60y0c2xx3wlpsz1"
token = "038f7011515ffff9e8337864873cd83d271c"
tag = "guoqing_a"
accoount = "guoqing_a"
upload_id = 36217
token_upload_id = 35718


authenticator = BasicAuthenticator(username=username, password=password)
android_push = Push(authenticator=authenticator, zone=ZONE_GZ)

#########################
# android push,includes:
# 1.all push
# 2.tag push
# 3.token push
# 4.account push
# 5.package token push
# 6.package account push
#########################


# 1.all push
android_push_data = {
    "audience_type": "all",
    "environment": "product",
    "message_type": "notify",
    "message": {
        "title": "推送标题-all",
        "content": "推送内容-all",
        "ios": {
            "aps": {
                "alert": {
                    "subtitle": "推送副标题-all"
                },
                "badge_type": -2,
                "sound": "Tassel.wav",
                "category": "INVITE_CATEGORY"

            },
            "custom_content": "{\"key\":\"value\"}",
            "xg": "oops"
        }
    }
}

# response = android_push.push(audience_type=android_push_data['audience_type'], message=android_push_data['message'],
#                      message_type=android_push_data['message_type'])
# print(json.dumps(response.get_result(), indent=2))

# 2.tag push
android_push_data = {
    "audience_type": "tag",
    "message_type": "notify",
    "message": {
        "title": "推送标题-tag",
        "content": "推送内容-tag",
        "android": {
            "n_ch_id": "default_message",
            "n_ch_name": "默认通知",
            "n_id": 0,
            "builder_id": 0,
            "ring": 1,
            "ring_raw": "ring",
            "badge_type": -1,
            "vibrate": 1,
            "lights": 1,
            "clearable": 1,
            "icon_type": 0,
            "icon_res": "xg",
            "style_id": 1,
            "small_icon": "xg",
            "custom_content": "{\"key\":\"value\"}"
        }
    },
    "tag_rules": [
        {
            "tag_items": [
                {
                    "tags": [
                        "uu", "dd"
                    ],
                    "is_not": False,
                    "tags_operator": "OR",
                    "items_operator": "OR",
                    "tag_type": "xg_user_define"
                }
            ],
            "operator": "OR",
            "is_not": False
        }
    ]
}

# response = android_push.push(audience_type=android_push_data['audience_type'], message=android_push_data['message'],
#                              message_type=android_push_data['message_type'],
#                              tag_rules=android_push_data['tag_rules'])
# print(json.dumps(response.get_result(), indent=2))


# 3.token push
android_push_data = {
    "audience_type": "token_list",
    "token_list": [token],
    "message_type": "notify",
    "message": {
        "title": "推送标题-token",
        "content": "推送内容-token",
        "android": {
            "n_ch_id": "default_message",
            "n_ch_name": "默认通知",
            "n_id": 0,
            "builder_id": 0,
            "ring": 1,
            "ring_raw": "ring",
            "badge_type": -1,
            "vibrate": 1,
            "lights": 1,
            "clearable": 1,
            "icon_type": 0,
            "icon_res": "xg",
            "style_id": 1,
            "small_icon": "xg",
            "custom_content": "{\"key\":\"value\"}"
        }
    }
}
response = android_push.push(audience_type="None",
                            message="None",
                             extend_params=android_push_data )
print(json.dumps(response.get_result(), indent=4))

# 4.account push
android_push_data = {
    "audience_type": "account",
    "account_list": ["123"],
    "message_type": "notify",
    "message": {
        "title": "推送标题-account",
        "content": "推送内容-account",
        "android": {
            "n_ch_id": "default_message",
            "n_ch_name": "默认通知",
            "n_id": 0,
            "builder_id": 0,
            "ring": 1,
            "ring_raw": "ring",
            "badge_type": -1,
            "vibrate": 1,
            "lights": 1,
            "clearable": 1,
            "icon_type": 0,
            "icon_res": "xg",
            "style_id": 1,
            "small_icon": "xg",
            "custom_content": "{\"key\":\"value\"}"
        }
    }
}
# response = android_push.push(audience_type=android_push_data['audience_type'], message=android_push_data['message'],
#                      message_type=android_push_data['message_type'],
#                      account_list=android_push_data['account_list'])
# print(json.dumps(response.get_result(), indent=2))


# 5.package token push
android_push_data = {
    "audience_type": "package_token_push",
    "message_type": "notify",
    "upload_id": 123,
    "message": {
        "title": "推送标题-token-package",
        "content": "推送内容-token-package",
        "android": {
            "n_ch_id": "default_message",
            "n_ch_name": "默认通知",
            "n_id": 0,
            "builder_id": 0,
            "ring": 1,
            "ring_raw": "ring",
            "badge_type": -1,
            "vibrate": 1,
            "lights": 1,
            "clearable": 1,
            "icon_type": 0,
            "icon_res": "xg",
            "style_id": 1,
            "small_icon": "xg",
            "custom_content": "{\"key\":\"value\"}"
        }
    }
}
# response = android_push.push(audience_type=android_push_data['audience_type'], message=android_push_data['message'],
#                      message_type=android_push_data['message_type'],
#                      upload_id=android_push_data['upload_id'])
# print(json.dumps(response.get_result(), indent=2))


# 6.package account push
android_push_data = {
    "audience_type": "package_account_push",
    "message_type": "notify",
    "upload_id": 123,
    "message": {
        "title": "推送标题-account-package",
        "content": "推送内容-account-package",
        "android": {
            "n_ch_id": "default_message",
            "n_ch_name": "默认通知",
            "n_id": 0,
            "builder_id": 0,
            "ring": 1,
            "ring_raw": "ring",
            "badge_type": -1,
            "vibrate": 1,
            "lights": 1,
            "clearable": 1,
            "icon_type": 0,
            "icon_res": "xg",
            "style_id": 1,
            "small_icon": "xg",
            "custom_content": "{\"key\":\"value\"}"
        }
    }
}
# response = android_push.push(audience_type=android_push_data['audience_type'], message=android_push_data['message'],
#                      message_type=android_push_data['message_type'],
#                      upload_id=android_push_data['upload_id'])
# print(json.dumps(response.get_result(), indent=2))