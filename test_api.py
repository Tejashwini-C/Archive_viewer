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
        assert response_superuser_status.status_code == 404
        log_request_response(response_superuser_status)

    def test_app_preferences(self):
        response_app_prefer = call_method.test_get_method("v1/app-preferences")
        assert response_app_prefer.status_code == 404
        log_request_response(response_app_prefer)


    def test_onboarding(self):
        response_onboarding = call_method.test_get_method("v1/onboarding")
        assert response_onboarding.status_code == 404
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
       log_request_response(metadata_response,request_body=body,params=params)
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
           log_request_response(metadata_response,request_body=body,params=params)
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

    @pytest.mark.parametrize(
        "testcasename,superseturl,skip,excepetd_statuscode",
        data_pass.Storesuperseturl,ids=[tc[0] for tc in data_pass.Storesuperseturl]  # Using test case name for readability in reports 
        )
    def test_Storesuperseturl(self, testcasename,superseturl,skip,excepetd_statuscode):
        # Generate query parameters and JSON body separately
           params = Payload.Storesuperseturl_params(skip)
           body = Payload.Storesuperseturl_body(superseturl)  
    # Send API request
           Storesuperseturl_response = call_method.test_post_method("/v1/report-url", params=params, json=body)
           log_request_response(Storesuperseturl_response,request_body=body,params=params)
           assert Storesuperseturl_response.status_code == excepetd_statuscode

    @pytest.mark.parametrize(
        "testcasename,storageType,name,locationType,mountPath,path,UNC_path,storageProtocol,saveFlag,excepetd_statuscode",
        data_pass.add_storgae,ids=[tc[0] for tc in data_pass.add_storgae]  # Using test case name for readability in reports 
        )       
    def test_add_storage(self,testcasename,storageType,name,locationType,mountPath,path,UNC_path,storageProtocol,saveFlag,excepetd_statuscode):
        params=Payload.add_storage_params(storageType)
        body=Payload.add_storage_body(name,locationType,mountPath,path,UNC_path,storageProtocol,saveFlag)
        add_storage_response=call_method.test_post_method("/v1/manage-storage",params=params,json=body)
        log_request_response(add_storage_response,request_body=body,params=params)
        assert add_storage_response.status_code==excepetd_statuscode    

    @pytest.mark.parametrize("testcasename,storageId,excepetd_statuscode",
        data_pass.fetch_storage,ids=[tc[0] for tc in data_pass.fetch_storage]
        )
    def test_fetch_storage(self,testcasename,storageId,excepetd_statuscode):
        params=Payload.fetch_storage_params(storageId)
        fetch_storage_response=call_method.test_get_method("/v1/manage-storage",params=params)
        log_request_response(fetch_storage_response,params=params)
        assert fetch_storage_response.status_code==excepetd_statuscode

    @pytest.mark.parametrize("testcasename,platformType,optimServerName, optimDirectory, psthomePath, defaultQualifier, storageId, excepetd_statuscode",
        data_pass.convert_server,ids=[tc[0] for tc in data_pass.convert_server]
        )
    def test_convert_server(self,testcasename,platformType,optimServerName, optimDirectory, psthomePath, defaultQualifier, storageId, excepetd_statuscode):
        params=Payload.convert_server_params(platformType)
        body=Payload.convert_server_body(optimServerName, optimDirectory, psthomePath, defaultQualifier, storageId)
        convert_server_response=call_method.test_post_method("/v1/convert-server",params=params,json=body)
        log_request_response(convert_server_response,request_body=body,params=params)
        assert convert_server_response.status_code==excepetd_statuscode
      
    @pytest.mark.parametrize("testcasename,catalogType,skip,ssl,queryServerName,databaseName,host,port,username,psswrd,excepetd_statuscode",
        data_pass.query_server,ids=[tc[0] for tc in data_pass.query_server]
        )
    def test_query_server(self,testcasename,catalogType,skip,ssl,queryServerName,databaseName,host,port,username,psswrd,excepetd_statuscode):
        params=Payload.query_server_params(catalogType,skip,ssl)
        body=Payload.query_server_body(queryServerName,databaseName,host,port,username,psswrd)
        query_server_response=call_method.test_post_method("/v1/query-server",params=params,json=body)
        log_request_response(query_server_response,request_body=body,params=params)
        assert query_server_response.status_code==excepetd_statuscode
