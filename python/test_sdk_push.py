import json
from typing import Dict, List, BinaryIO
from tpns.core.authenticators import Authenticator, BasicAuthenticator
from tpns.core import BaseService, APIResponse
from tpns.common import (
    get_sdk_headers,
    ZONE_GZ, ZONES,
    ENDPOINT_PUSH,
    ENDPOINT_ADD_PLAN_PUSH,
    ENDPOINT_UPLOAD_PACKAGE,
)
from tpns.core.utils import (
    remove_null_values,
    merge_params
)


class Push(BaseService):
    """The  Push service."""

    # audience_type
    AUDIENCE_TYPE_ALL = 'all'
    AUDIENCE_TYPE_TAG = 'tag'
    AUDIENCE_TYPE_TOKEN = 'token'
    AUDIENCE_TYPE_TOKEN_LIST = 'token_list'
    AUDIENCE_TYPE_ACCOUNT = 'account'
    AUDIENCE_TYPE_ACCOUNT_LIST = 'account_list'
    AUDIENCE_TYPE_PACKAGE_ACCOUNT_PUSH = 'package_account_push'
    AUDIENCE_TYPE_PACKAGE_TOKEN_PUSH = 'package_token_push'

    def __init__(
            self,
            zone: str = ZONE_GZ,
            authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Push service.
        :param str zone: The zone where the application is deployed. Defaults to gz.
        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
        """
        if not authenticator:
            raise ValueError('authenticator must be provided')

        if not isinstance(authenticator, BasicAuthenticator):
            raise ValueError('authenticator only support basic auth now')
        self.zone = zone
        BaseService.__init__(self, authenticator=authenticator)

    #########################
    # push
    #########################
    def push(self,
             audience_type: str = None, message: 'Message' = None, message_type: str = 'notify',
             environment: str = None, upload_id: int = None, expire_time: int = None, send_time: str = None,
             multi_pkg: bool = None, loop_param: Dict = None, group_id: str = None, plan_id: str = None,
             tag_rules: List[Dict] = None, account_list: List[str] = None, account_push_type: int = None,
             token_list: List[str] = None, push_speed: int = None, collapse_id: int = None,
             channel_rules: List[Dict] = None,
             tpns_online_push_type: int = None, force_collapse: bool = None, extend_params: Dict = None,
             **kwargs) -> APIResponse:

        if audience_type is None:
            raise ValueError('audience_type must be provided')
        if audience_type == self.AUDIENCE_TYPE_TAG and tag_rules is None:
            raise ValueError('tag_rules must be provided')
        if (audience_type == self.AUDIENCE_TYPE_TOKEN or audience_type == self.AUDIENCE_TYPE_TOKEN) \
                and token_list is None:
            raise ValueError('token_list must be provided')
        if (audience_type == self.AUDIENCE_TYPE_ACCOUNT or audience_type == self.AUDIENCE_TYPE_ACCOUNT_LIST) \
                and account_list is None:
            raise ValueError('account_list must be provided')
        if message is None:
            raise ValueError('message must be provided')
        if (audience_type == Push.AUDIENCE_TYPE_PACKAGE_ACCOUNT_PUSH or
            audience_type == Push.AUDIENCE_TYPE_PACKAGE_TOKEN_PUSH) \
                and upload_id is None:
            raise ValueError('upload_id must be provided')

        data = {
            'audience_type': audience_type,
            'message': message,
            'message_type': message_type,
            'environment': environment,
            'upload_id': upload_id,
            'expire_time': expire_time,
            'send_time': send_time,
            'multi_pkg': multi_pkg,
            'loop_param': loop_param,
            'group_id': group_id,
            'plan_id': plan_id,
            'tag_rules': tag_rules,
            'account_list': account_list,
            'account_push_type': account_push_type,
            'token_list': token_list,
            'push_speed': push_speed,
            'collapse_id': collapse_id,
            'channel_rules': channel_rules,
            'tpns_online_push_type': tpns_online_push_type,
            'force_collapse': force_collapse,
        }

        merge_params(data, extend_params)
        data = remove_null_values(data)
        data = json.dumps(data)
        print("requests:\n",data)
        headers = get_sdk_headers('push')
        headers['content-type'] = 'application/json'
        url = ZONES[self.zone][ENDPOINT_PUSH]
        # request = self.prepare_request(method='POST',
        #                                url=url,
        #                                headers=headers,
        #                                data=data)
        # response = self.send(request, **kwargs)
        # return response


username = 1500001533
password = "euwhfy3zyi3hvahkf60y0c2xx3wlpsz1"
token = "038f7011515ffff9e8337864873cd83d271c"
tag = "guoqing_a"
accoount = "guoqing_a"
upload_id = 36217
token_upload_id = 35718
authenticator = BasicAuthenticator(username=username, password=password)
android_push = Push(authenticator=authenticator, zone=ZONE_GZ)
# android_push.push(audience_type=1,message=2,extend_params=0)
data = {"audience_type": "token", "message": {"title": "push_test_5","content":"push_test_5"}, "message_type": "notify", "token_list": ["038f7011515ffff9e8337864873cd83d271c"]}
android_push.push(audience_type="1",message={},extend_params={},a=1)


# a={"a":1}
# def tt(**kwargs):
#     kwargs = dict({"timeout": 60}, **kwargs)
#     print(kwargs)
#
# tt(**a)