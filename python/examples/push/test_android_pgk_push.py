import json
import time

import pytest
from tpns.common import ZONE_GZ
from tpns import Push
from tpns.push import Android,AndroidMessage

from tpns.core.authenticators import BasicAuthenticator



username = 1500001533
password = "euwhfy3zyi3hvahkf60y0c2xx3wlpsz1"
token = "038f7011515ffff9e8337864873cd83d271c"
tag = "guoqing_a"
account = "guoqing_a"
upload_id = 36217
token_upload_id = 35718

authenticator = BasicAuthenticator()
android_push = Push(authenticator=authenticator, zone=ZONE_GZ)


android_push_data = {
    "audience_type": "package_account_push",
    "message_type": "notify",
    "upload_id": upload_id,
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
response = android_push.push(audience_type=android_push_data['audience_type'], message=android_push_data['message'],
                     message_type=android_push_data['message_type'],
                     upload_id=android_push_data['upload_id'])
print(json.dumps(response.get_result(), indent=2))


response = android_push.push(audience_type="package_token_push", message=android_push_data['message'],
                     message_type=android_push_data['message_type'],
                     upload_id=35718)
print(json.dumps(response.get_result(), indent=2))