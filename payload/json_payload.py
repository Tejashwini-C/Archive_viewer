class Payload:
    @staticmethod
    def meta_data_params(action: str, connectionType: str, NNE_enabled: bool, LoginType: str, status: str) -> dict:
        """Returns query parameters for the metadata API."""
        return {
            "action": action,
            "connectionType": connectionType,
            "NNE_enabled": NNE_enabled,
            "LoginType": LoginType,
            "status": status
        }

    @staticmethod
    def meta_data_body(databaseType: str, host: str, port: int, username: str, psswrd: str, databaseName: str) -> dict:
        """Returns JSON body for the metadata API."""
        return {
          
                    "databaseType": databaseType,
                    "host": host,
                    "port": port,
                    "username": username,
                    "psswrd": psswrd,
                    "databaseName": databaseName

        }
    
    @staticmethod
    def Super_user_payload(loginType,name,username,psswrd,email):
        return{
            "loginType": loginType,
            "fullname": name,
            "username": username,
            "psswrd": psswrd,
            "email": email
     }
    
    @staticmethod
    def Storesuperseturl_body(superseturl):
        return{
            "superseturl": superseturl
        }
    @staticmethod
    def Storesuperseturl_params(skip):
        return{
            "skip": skip
        }
    
    @staticmethod
    def add_storage_params(storageType):
        return{
            "storageType": storageType
        }
    @staticmethod
    def add_storage_body(name, locationType, mountPath, path, UNC_path, storageProtocol, saveFlag):
        return {
            "name": name,
            "locationType": [
                locationType
                ],
            "mountPath": mountPath,
            "path": path,
            "UNC_path": UNC_path,
            "storageProtocol": storageProtocol,
            "saveFlag": saveFlag,
                }
    
    @staticmethod
    def fetch_storage_params(storageId):
        return {
            "storageId": storageId
        }
    
    @staticmethod
    def convert_server_params(platformType):
        return {
            "platformType": platformType
        }
    @staticmethod
    def convert_server_body(optimServerName, optimDirectory, psthomePath, defaultQualifier, storageId):
        return {
            "optimServerName": optimServerName,
            "optimDirectory": optimDirectory,
            "psthomePath": psthomePath,
            "defaultQualifier": defaultQualifier,
            "storageId": storageId
        }
    
    @staticmethod
    def query_server_params(catalogType:str,skip :bool,ssl):
        return {
            "catalogType": catalogType,
            "skip": skip,
            "ssl": ssl
        }
    @staticmethod
    def query_server_body(queryServerName,databaseName,host,port,username,psswrd):
        return {
            "queryServerName": queryServerName,
            "databaseName": databaseName,
            "host": host,
            "port": port,
            "username": username,
            "psswrd": psswrd
        }
