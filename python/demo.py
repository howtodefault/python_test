from tpns.core.utils import (
    remove_null_values,
    merge_params
)
import json

data = {
            'audience_type': None,
            'message': None,
            'message_type': None,
            'environment': None,
            'upload_id': None,
            'expire_time': None,
            'send_time': None,
            'multi_pkg': None,
            'loop_param': None,
            'group_id': None,
            'plan_id': None,
            'tag_rules': None,
            'account_list': None,
            'account_push_type': None,
            'token_list': None,
            'push_speed': None,
            'collapse_id': None,
            'channel_rules': None,
            'tpns_online_push_type': None,
            'force_collapse': None,
        }
all_args = {
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
extend_params = {}
merge_params(data, extend_params)

data = remove_null_values(data)
print("remove_null_values:\n",data)
data = json.dumps(data,indent=4,sort_keys=True)
print("remove_null_values:\n",data)

merge_params(all_args, extend_params)
data = remove_null_values(data)
print("remove_null_values:\n",data)
data = json.dumps(data,indent=4,sort_keys=True)
print("remove_null_values:\n",data)
