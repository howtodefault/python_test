
import json
from tpns.common import ZONE_GZ
from tpns import Push
from tpns.core.authenticators import BasicAuthenticator

username = 1500001533
password = "euwhfy3zyi3hvahkf60y0c2xx3wlpsz1"
token = "038f7011515ffff9e8337864873cd83d271c"
tag = "guoqing_a"
account = "guoqing_a"
upload_id = 36217
token_upload_id = 35718


authenticator = BasicAuthenticator(username=username, password=password)
push = Push(authenticator=authenticator, zone=ZONE_GZ)

data = {
    "planName": "TPNS_TEST123",
    "planDescribe": "plan_test"
}

response = push.add_plan_push(plan_name=data['planName'], plan_describe=data['planDescribe'])
print(json.dumps(response.get_result(), indent=2))
