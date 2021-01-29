import copy
import json
import time

import pytest
from tpns.common import ZONE_HK
from tpns import Push
from tpns.push import Android,AndroidMessage

from tpns.core.authenticators import BasicAuthenticator





#test zgq
#test zgq
# username = 1500001533
# password = "euwhfy3zyi3hvahkf60y0c2xx3wlpsz1"
# token = "038f7011515ffff9e8337864873cd83d271c"
# tag = "guoqing_a"
# account = "guoqing_a"
# upload_id = 36217
# token_upload_id = 35718

username = 1500001050
password = "d227909c5e33558b27e10f3c302f64b5"
token = "06f67f0857207bb9b27774e6907ce2b1e7eb"
tag = "guoqing_a"
account = "guoqing_a"
upload_id = 36217
token_upload_id = 35718

authenticator = BasicAuthenticator(username=username, password=password)
android_push = Push(authenticator=authenticator, zone=ZONE_HK)

send_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(round(time.time() + 5)))
loop_param = {"startDate":"2021-01-25",
    		                                "endDate":"2021-01-27",
    		                                "loopType":1,
                                            "loopDayIndexs":[1,2,3,4],
    		                                "dayTimes":["11:10:00", "15:25:00"]}
tag_list = {
        "op": "OR",
        "tags": [
            "guoqing_a",
            "guoqing_b"
        ]
    }
tag_rules= [
    {
        "tag_items": [
            {
                "tags": [
                    "guoqing_a","guoqing_b"
                ],
                "tags_operator": "OR",
                "items_operator": "OR",
                "is_not": False,
                "tag_type": "xg_user_define"
            }

        ]}]

android_push_data = {
    "audience_type": "tag",
    "tag_list": tag_list,
    "tag_rules":tag_rules,
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
    "loop_param": {},
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
# def test_2():
#     response = android_push.push(audience_type="tag",
#                                  message={},
#                                  tag_rules=tag_rules
#                                  )
#     print(json.dumps(response.get_result(), indent=4))
#     assert response.get_result()["ret_code"]==0

#args3 extend_params
push_data = copy.deepcopy(android_push_data)
push_data["loop_param"] = loop_param
# def test_3():
#     response = android_push.push(audience_type="None",
#                                  message={},
#                                  extend_params=push_data
#                                  )
#     print(json.dumps(response.get_result(), indent=4))
#     assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"][0]) > 0

def test_4():
    response = android_push.push(audience_type=android_push_data["audience_type"],
                                 message=android_push_data["message"],
                                 tag_rules=tag_rules

                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0


def test_5():
    response = android_push.push(audience_type=android_push_data["audience_type"],
                                 message={"title":"push_test_5","content":"push_test_5"},
                                 tag_rules=tag_rules
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0

# custom req
def test_6():
    response = android_push.push(audience_type="tag",
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
                                 tag_rules=tag_rules,
                                 push_speed=20000,
                                 collapse_id=66666,
                                 channel_rules=[{"channel": "hw","disable": False}],
                                 tpns_online_push_type=1,
                                 force_collapse=True,
                                 # extend_params=android_push_data
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0


#android args
android_args = {
"n_ch_id": "default_message",
"n_ch_name": "默认通知",
      "n_id": 0,
      "builder_id": 0,
      "ring": 1,
      "ring_raw": "ring",
"badge_type":-1,
      "vibrate": 1,
      "lights": 1,
      "clearable": 1,
      "icon_type": 0,
      "icon_res": "xg",
      "style_id": 1,
      "small_icon": "xg",
      "action": {
          "action_type": 1,
          "activity": "com.x.y.PushActivity",
          "aty_attr": {
              "if": 0,
              "pf": 0
          },
          "browser": {
              "url": "https://cloud.tencent.com ",
              "confirm": 1
          },
          "intent": "xgscheme://com.tpns.push/notify_detail"
      },
    "custom_content":"{\"key\":\"value\"}"
  }

msg = {"title": "push_test_7", "content": "push_test_7"}

msg.update(android_args)
def test_7():
    response = android_push.push(audience_type="tag",
                                 message=msg,
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
                                 tag_rules=tag_rules,
                                 push_speed=20000,
                                 collapse_id=66666,
                                 channel_rules=[{"channel": "hw","disable": False}],
                                 tpns_online_push_type=1,
                                 force_collapse=True,
                                 # extend_params=android_args
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0

#kwargs
def test_8():
    response = android_push.push(audience_type="tag",
                                 message=msg,
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
                                 tag_rules=tag_rules,
                                 push_speed=20000,
                                 collapse_id=66666,
                                 channel_rules=[{"channel": "hw","disable": False}],
                                 tpns_online_push_type=1,
                                 force_collapse=True,
                                 # extend_params=android_args
                                 a=1,
                                 b=2
                                 )
    print(json.dumps(response.get_result(), indent=4))
    assert response.get_result()['ret_code']==0 and int(response.get_result()["push_id"]) > 0




