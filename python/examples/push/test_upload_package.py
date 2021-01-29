import os.path
import json
from tpns import Push
from tpns.core.authenticators import BasicAuthenticator,NoAuthAuthenticator
from tpns.common import ZONE_GZ


username = 1500001533
password = "euwhfy3zyi3hvahkf60y0c2xx3wlpsz1"
token = "038f7011515ffff9e8337864873cd83d271c"
tag = "guoqing_a"
account = "guoqing_a"
upload_id = 36217
token_upload_id = 35718

#########################
# upload  package
#########################

authenticator = BasicAuthenticator(username=username, password=password)
# authenticator = NoAuthAuthenticator()
push = Push(authenticator=authenticator, zone=ZONE_GZ)

#upload txt
path = os.path.abspath('token_txt.txt')
with open(path, 'rb') as file:
    result = push.upload_package(file)
    print(json.dumps(result.get_result(), indent=2))
    print(result.get_status_code())
    print(result.get_headers())

#upload csv
# path = os.path.abspath('token_csv.csv')
# with open(path, 'rb') as file:
#     result = push.upload_package(file).get_result()
#     print(json.dumps(result, indent=2))
#
#
# #upload zip
# path = os.path.abspath('token_txt.zip')
# with open(path, 'rb') as file:
#     result = push.upload_package(file).get_result()
#     print(json.dumps(result, indent=2))
#
# #upload 100txt
# #upload txt
# path = os.path.abspath("Data100Mb_account.txt")
# with open(path, 'rb') as file:
#     result = push.upload_package(file).get_result()
#     print(json.dumps(result, indent=2))
#
# #upload 50mbzip
# path = os.path.abspath('only_100mb_account_txt.zip')
# with open(path, 'rb') as file:
#     result = push.upload_package(file).get_result()
#     print(json.dumps(result, indent=2))
#
# #upload 100mbzip
# path = os.path.abspath('Data100Mb_account.txt.zip')
# with open(path, 'rb') as file:
#     result = push.upload_package(file).get_result()
#     print(json.dumps(result, indent=2))