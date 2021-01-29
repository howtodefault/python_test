import json
import time

import pytest
from tpns.common import ZONE_GZ
from tpns import Push
from tpns.push import Android,AndroidMessage

from tpns.core.authenticators import BasicAuthenticator





#test zgq
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


#args1
def test_1():
    response = android_push.push(audience_type="None",
                                 message={}
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==1008007 and response.get_result()["err_msg"]=="audience_type is not correct"

def test_2():
    response = android_push.push(audience_type="all",
                                 message=android_push_data["message"]
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0