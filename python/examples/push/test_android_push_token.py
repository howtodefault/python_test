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

send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(round(time.time() + 5)))
loop_param = {"startDate":"2021-01-25",
    		                                "endDate":"2021-01-27",
    		                                "loopType":3,
                                            "loopDayIndexs":[1,10,20],
    		                                "dayTimes":["11:10:00", "15:25:00"]}


android_push_data = {
    "audience_type": "token",
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
            "custom_content": "{\"key\":\"value\"}",
            "action": {
                "action_type": 1,
                "activity": "com.tencent.android.duoduo.JumpActivity",
                "aty_attr": {
                    "if": 0,
                    "pf": 0  ,
                "browser": {
                    "url": "xxxx ",
                    "confirm": 1 ,
                "intent": "xxx"
        				}
    				 }
    				}
    			 }
        },
    # "loop_param": {},
    "send_time":""

}

#args1
def test_1():
    response = android_push.push(audience_type="None",
                                 message={}
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==1008007 and response.get_result()["err_msg"]=="audience_type is not correct"

#args2
def test_2():
    response = android_push.push(audience_type="token",
                                 message={},
                                 token_list=[]
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()["ret_code"]==1008007

#args3 extend_params
def test_3():
    response = android_push.push(audience_type="None",
                                 message={},
                                 extend_params=android_push_data
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0

def test_4():
    response = android_push.push(audience_type=android_push_data["audience_type"],
                                 message=android_push_data["message"],
                                 token_list=[token]

                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0


def test_5():
    response = android_push.push(audience_type=android_push_data["audience_type"],
                                 message={"title":"push_test_5","content":"push_test_5"},
                                 token_list=[token]
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0

# custom req
def test_6():
    response = android_push.push(audience_type="token",
                                 message={"title":"push_test_6","content":"push_test_6"},
                                 message_type="notify",
                                 environment="dev",
                                 upload_id = 36217,
                                 expire_time=1600,
                                 # send_time="2021-01-25 16:15:00",
                                 multi_pkg=True,
                                 # loop_param={"startDate":"2020-04-01",
    		                     #            "endDate":"2020-05-31",
    		                     #            "loopType":3,
                                 #            "loopDayIndexs":[1,10,20],
    		                     #            "dayTimes":["11:10:00", "15:25:00"]},
                                 group_id="110",
                                 plan_id="15379",
                                 token_list=[token],
                                 push_speed=20000,
                                 collapse_id=66666,
                                 channel_rules=[{"channel": "hw","disable": False}],
                                 tpns_online_push_type=1,
                                 force_collapse=True,
                                 # extend_params=android_push_data
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0


# custom android

android = Android()
android.n_ch_id = ""
android.n_ch_name = ""
android.xm_ch_id = ""
android.hw_ch_id = ""
android.oppo_ch_id = ""
android.vivo_ch_id = ""
android.n_id = ""
android.builder_id = ""
android.badge_type = ""
android.ring = ""
android.ring_raw = ""
android.vibrate = ""
android.lights = ""
android.clearable = ""
android.icon_type = ""
android.icon_res = ""
android.style_id = ""
android.small_icon = ""
android.icon_color = ""
android.action = ""
android.custom_content = ""
android.show_type = ""
android_msg = AndroidMessage()
android_msg.title = "push_test_7"
android_msg.content= "push_test_7"
# android_msg.accept_time = ""
# android_msg.thread_id = ""
# android_msg.thread_sumtext = ""
# android_msg.xg_media_resources = ""
# android_msg.xg_media_audio_resources = ""
# android_msg.android = android

def test_7():
    response = android_push.push(audience_type="token",
                                 message=android_msg,
                                 message_type="notify",
                                 environment="dev",
                                 upload_id = 36217,
                                 expire_time=1600,
                                 # send_time="2021-01-25 16:15:00",
                                 multi_pkg=True,
                                 # loop_param={"startDate":"2020-04-01",
    		                     #            "endDate":"2020-05-31",
    		                     #            "loopType":3,
                                 #            "loopDayIndexs":[1,10,20],
    		                     #            "dayTimes":["11:10:00", "15:25:00"]},
                                 group_id="110",
                                 plan_id="15379",
                                 token_list=[token],
                                 push_speed=20000,
                                 collapse_id=66666,
                                 channel_rules=[{"channel": "hw","disable": False}],
                                 tpns_online_push_type=1,
                                 force_collapse=True,
                                 # extend_params=android_msg
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0
