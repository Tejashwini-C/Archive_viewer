class data_pass():
    metadata_test_connection = [
        # testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode
        ("incorrect_databasetype", "testConnection","Service Name", False, " ", " ", "invalid", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_host", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.1764", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_port", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 15921, "metadb", "metadb", "orcl", 422),
        ("incorrect_username", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "mestadb", "metadb", "orcl", 422),
        ("incorrect_password", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadddb", "orcl", 422),
        ("incorrect_database-name", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orrtcl", 422),
        ("invalid-action", "testCottection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("invalid-connectiontype", "testConnection","Servicevd Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("Success", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 200)
    ]

    metadata_Create_tables = [
        # testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepeted_statuscode
        ("incorrect_databasetype", "createTables","Service Name", False, " ", "drop", "invalid", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_host", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.1764", 1521, "metadb", "metadb", "orcl", 422),
        ("incorrect_port", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 15921, "metadb", "metadb", "orcl", 422),
        ("incorrect_username", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "mestadb", "metadb", "orcl", 422),
        ("incorrect_password", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadddb", "orcl", 422),
        ("incorrect_database-name", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orrtcl", 422),
        ("invalid-action", "createssTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("invalid-connectiontype", "createTables","Servicevd Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("invalid-status", "createTables","Servicevd Name", False, " ", "dop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 422),
        ("Success", "createTables","Service Name", False, " ", "drop", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 200)
    ]
    Super_user=[
        #testcasename,loginType,name,username,psswrd,email,excepetd_statuscode
        ("invalid-logintype","BASTC","Super","Super","Super@123","super@gmail.com",422),
        ("invalid-name","BASIC"," ","Super","Super@123","super@gmail.com",422),
        ("invalid-Username","BASIC","Super"," ","Super@123","super@gmail.com",422),
        ("invalid-passwrd","BASIC","Super","Super","Super**&^#$","super@gmail.com",422),
        ("invalid-email","BASIC","Super","Super","Super@123","super@gmail_com",422),
        ("valid-details","BASIC","Super","Super","Super@123","super@gmail.com",200)

    ]