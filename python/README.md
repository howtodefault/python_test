# TPNS Python SDK

Python client library to quickly get started with the various [TPNS APIs][tpns] services.
<details>
  <summary>Table of Contents</summary>
  
  * [Before you begin](#before-you-begin)
  * [Examples](#examples)
  * [Authentication](#authentication)
    * [UserName and Password](#username-and-password)
  * [Questions](#questions)   
  * [Changes for v1.0](#changes-for-v10)  
  * [Configuring the http client](#configuring-the-http-client)
  * [Setting the service zone](#setting-the-service-zone)
  * [Dependencies](#dependencies)
 </details>


## Before you begin
*  We now only support `python 3.5` and above


## Examples

The [examples][examples] folder has basic examples for reference


## Authentication

### UserName and Password
```python
from tpns.core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('access_id', 'secret_key')
```

## Questions
If you have issues with the APIs or have a question about the TPNS services, see [Contact US][contact]


## Changes for v1.0
Provide push-related API services

## Configuring the http client
To set client configs like timeout use the `set_http_config()` function and pass it a dictionary of configs.

## Setting the service zone
```python
from tpns import Push

# available zone
ZONE_GZ = 'gz'
ZONE_SH = 'sh'
ZONE_HK = 'hk'
ZONE_SGP = 'sgp'

## set gz as the push zone
push = Push(zone=ZONE_GZ)
```




## Dependencies
* [requests]


[tpns]: https://cloud.tencent.com/document/product/548
[examples]: ./examples
[contact]: https://cloud.tencent.com/document/product/548/47590
[requests]: http://docs.python-requests.org/en/latest/

