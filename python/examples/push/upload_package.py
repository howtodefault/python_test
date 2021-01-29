import os.path
import json
from tpns import Push
from tpns.core.authenticators import BasicAuthenticator
from tpns.common import ZONE_GZ


#########################
# upload  package
#########################

authenticator = BasicAuthenticator(username='15000**', password='c87f******e001140bd')
push = Push(authenticator=authenticator, zone=ZONE_GZ)

path = os.path.abspath('package.txt')
with open(path, 'rb') as file:
    result = push.upload_package(file).get_result()
    print(json.dumps(result, indent=2))
