import requests
import pytest
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class request_call():
    Base_url="https://archive208.estuate.com:3051"

    def test_get_method(self,endpoint,headers=None,params=None):
        from test_api import Testarchive
        headers = headers or {"Authorization": Testarchive.auth_token}
        url=f"{self.Base_url}/{endpoint}"
        get_response=requests.get(url=url,verify=False,headers=headers,params=params)
        return get_response
    
    def test_post_method(self,endpoint, json=None, headers=None,params=None):
        from test_api import Testarchive
        url=f"{self.Base_url}/{endpoint}"
        headers = headers or {"Authorization": Testarchive.auth_token}
        post_response=requests.post(url=url,verify=False, json=json, headers=headers,params=params)
        return post_response