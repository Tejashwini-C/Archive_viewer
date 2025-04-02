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
