import pytest
from utils.request import request_call
import json
from payload.json_payload import Payload
from data.data import data_pass
from utils.logger import log_request_response

call_method = request_call()

class Testarchive():

    auth_token=None

    def test_health_check(self):
        response = call_method.test_get_method("v1/health-check")
        assert response.status_code == 200
        log_request_response(response)

    def test_meta_data(self):
        response = call_method.test_get_method("v1/metadata-status")
        assert response.status_code == 200
        log_request_response(response)

    def test_metadata_info(self):
        response_metadata_info = call_method.test_get_method("v1/metadata-info")
        assert response_metadata_info.status_code == 200
        log_request_response(response_metadata_info)
        
    def test_superuser_status(self):
        response_superuser_status = call_method.test_get_method("v1/superuser-status")
        assert response_superuser_status.status_code == 200
        log_request_response(response_superuser_status)

    def test_app_preferences(self):
        response_app_prefer = call_method.test_get_method("v1/app-preferences")
        assert response_app_prefer.status_code == 200
        log_request_response(response_app_prefer)


    def test_onboarding(self):
        response_onboarding = call_method.test_get_method("v1/onboarding")
        assert response_onboarding.status_code == 403
        log_request_response(response_onboarding)

    @pytest.mark.parametrize(
        "testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode",
        data_pass.metadata_test_connection,ids=[tc[0] for tc in data_pass.metadata_test_connection]  # Using test case name for readability in reports 
        )
    def test_add_metadata_test_connection(self, testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode):
        # Generate query parameters and JSON body separately
       params = Payload.meta_data_params(action, connectionType, NNE_enabled, LoginType, status)
       body = Payload.meta_data_body(databaseType, host, port, username, psswrd, databaseName)  
    # Send API request
       metadata_response = call_method.test_post_method("v1/meta-data", params=params, json=body)
       log_request_response(metadata_response,request_body=body)
       assert metadata_response.status_code == excepetd_statuscode

    @pytest.mark.parametrize(
        "testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode",
        data_pass.metadata_Create_tables,ids=[tc[0] for tc in data_pass.metadata_Create_tables]  # Using test case name for readability in reports 
        )
    def test_add_metadata_create_tables(self, testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode):
        # Generate query parameters and JSON body separately
           params = Payload.meta_data_params(action, connectionType, NNE_enabled, LoginType, status)
           body = Payload.meta_data_body(databaseType, host, port, username, psswrd, databaseName)  
    # Send API request
           metadata_response = call_method.test_post_method("v1/meta-data", params=params, json=body)
           log_request_response(metadata_response,request_body=body)
           assert metadata_response.status_code == excepetd_statuscode
   
    @pytest.mark.parametrize("testcasename,loginType,name,username,psswrd,email,excepetd_statuscode",
    data_pass.Super_user,ids=[tc[0] for tc in data_pass.Super_user]
    )
    def test_onboarding_authentication(self,testcasename,loginType,name,username,psswrd,email,excepetd_statuscode):
        body=Payload.Super_user_payload(loginType,name,username,psswrd,email)
        onboarding_authentication_response=call_method.test_post_method("/v1/onboarding-authentication",json=body)
        log_request_response(onboarding_authentication_response,request_body=body)
        assert onboarding_authentication_response.status_code==excepetd_statuscode
        if onboarding_authentication_response.status_code == 200:
         response_json = onboarding_authentication_response.json()
         token = response_json["detail"]["data"].get("access_token")
         if token:  # Ensure the token exists
              Testarchive.auth_token= f"Bearer {token}"
              return Testarchive.auth_token
         else:
              print("Token not found in the response.")
              return None    
    # Return None if the status code is not 200 or token is missing
        return None

    def test_onboarding_with_auth(self):
        response_onboarding = call_method.test_get_method("v1/onboarding")
        assert response_onboarding.status_code == 200
        log_request_response(response_onboarding)
    