import json
from tpns.common import ZONE_GZ
from tpns import Push
from tpns.core.authenticators import BasicAuthenticator

#########################
# iOS push,includes:
# 1.all push
# 2.tag push
# 3.token push
# 4.account push
# 5.package token push
# 6.package account push
#########################

authenticator = BasicAuthenticator(username='160000***', password='9f194b10*******e5b990295d1')
ios_push = Push(authenticator=authenticator, zone=ZONE_GZ)

# 1.all push

ios_push_data = {
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

# response = ios_push.push(audience_type=ios_push_data['audience_type'], message=ios_push_data['message'],
#                      message_type=ios_push_data['message_type'],
#                      environment=ios_push_data['environment'])
# print(json.dumps(response.get_result(), indent=2))


# 2.tag push
ios_push_data = {
    "audience_type": "tag",
    "environment": "product",
    "message_type": "notify",
    "message": {
        "title": "推送标题-tag",
        "content": "推送内容-tag",
        "ios": {
            "aps": {
                "alert": {
                    "subtitle": "推送副标题-tag"
                },
                "badge_type": -2,
                "sound": "Tassel.wav",
                "category": "INVITE_CATEGORY"

            },
            "custom_content": "{\"key\":\"value\"}",
            "xg": "oops"
        }
    },
    "tag_rules": [
        {
            "tag_items": [
                {
                    "tags": [
                        "uu"
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

# response = ios_push.push(audience_type=ios_push_data['audience_type'], message=ios_push_data['message'],
#                      message_type=ios_push_data['message_type'],
#                      tag_rules=ios_push_data['tag_rules'],
#                      environment=ios_push_data['environment'])
# print(json.dumps(response.get_result(), indent=2))

# 3.token push
ios_push_data = {
    "audience_type": "token",
    "environment": "product",
    "token_list": ["084b9065e91aa878537ae093aeed3e82e294"],
    "message_type": "notify",
    "message": {
        "title": "推送标题-token",
        "content": "推送内容-token",
        "ios": {
            "aps": {
                "alert": {
                    "subtitle": "推送副标题-token"
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
# response = ios_push.push(audience_type=ios_push_data['audience_type'], message=ios_push_data['message'],
#                      message_type=ios_push_data['message_type'],
#                      token_list=ios_push_data['token_list'],
#                      environment=ios_push_data['environment'])
# print(json.dumps(response.get_result(), indent=2))

# 4.account push
ios_push_data = {
    "audience_type": "account",
    "environment": "product",
    "account_list": ["123"],
    "message_type": "notify",
    "message": {
        "title": "推送标题-account",
        "content": "推送内容-account",
        "ios": {
            "aps": {
                "alert": {
                    "subtitle": "推送副标题-account"
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
# response = ios_push.push(audience_type=ios_push_data['audience_type'], message=ios_push_data['message'],
#                      message_type=ios_push_data['message_type'],
#                      account_list=ios_push_data['account_list'], environment=ios_push_data['environment'])
# print(json.dumps(response.get_result(), indent=2))


# 5.package token push
ios_push_data = {
    "audience_type": "package_token_push",
    "environment": "product",
    "upload_id": 123,
    "message_type": "notify",
    "message": {
        "title": "推送标题-token-package",
        "content": "推送内容-token-package",
        "ios": {
            "aps": {
                "alert": {
                    "subtitle": "推送副标题-token-package"
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

# response = ios_push.push(audience_type=ios_push_data['audience_type'], message=ios_push_data['message'],
#                      message_type=ios_push_data['message_type'],
#                      upload_id=ios_push_data['upload_id'], environment=ios_push_data['environment'])
# print(json.dumps(response.get_result(), indent=2))


# 6.package account push
ios_push_data = {
    "audience_type": "package_account_push",
    "environment": "product",
    "upload_id": 123,
    "message_type": "notify",
    "message": {
        "title": "推送标题-account-package",
        "content": "推送内容-account-package",
        "ios": {
            "aps": {
                "alert": {
                    "subtitle": "推送副标题-account-package"
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

# response = ios_push.push(audience_type=ios_push_data['audience_type'], message=ios_push_data['message'],
#                      message_type=ios_push_data['message_type'],
#                      upload_id=ios_push_data['upload_id'], environment=ios_push_data['environment'])
# print(json.dumps(response.get_result(), indent=2))