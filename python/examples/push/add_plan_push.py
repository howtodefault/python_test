import json
from tpns.common import ZONE_GZ
from tpns import Push
from tpns.core.authenticators import BasicAuthenticator

#########################
# add plan push
#########################

authenticator = BasicAuthenticator(username='15000***', password='c87f41********11e001140bd')
push = Push(authenticator=authenticator, zone=ZONE_GZ)

data = {
    "planName": "TPNS_TEST123",
    "planDescribe": "plan_test"
}

response = push.add_plan_push(plan_name=data['planName'], plan_describe=data['planDescribe'])
print(json.dumps(response.get_result(), indent=2))
