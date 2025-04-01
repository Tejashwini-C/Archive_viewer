import requests
import pytest
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class request_call():
    Base_url="https://archive174.estuate.com:3051"

    def test_get_method(self,endpoint):
        url=f"{self.Base_url}/{endpoint}"
        get_response=requests.get(url=url,verify=False)
        return get_response
    
    def test_post_method(self,endpoint, json=None, headers=None,params=None):
        url=f"{self.Base_url}/{endpoint}"
        post_response=requests.post(url=url,verify=False, json=json, headers=headers,params=params)
        return post_response