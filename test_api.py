import pytest
from utils.request import request_call
import json
from payload.json_payload import Payload
from data.data import data_pass
from utils.logger import log_request_response

call_method = request_call()

class Testarchive():

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
    def test_add_metadata(self, testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode,request):
        # Generate query parameters and JSON body separately
       params = Payload.meta_data_params(action, connectionType, NNE_enabled, LoginType, status)
       body = Payload.meta_data_body(databaseType, host, port, username, psswrd, databaseName)  
    # Send API request
       metadata_response = call_method.test_post_method("v1/meta-data", params=params, json=body)
    #    print(metadata_response.json())
       log_request_response(metadata_response,request_body=body)
       assert metadata_response.status_code == excepetd_statuscode

