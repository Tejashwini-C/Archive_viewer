class data_pass():
    metadata_test_connection = [
        # testcasename, action, connectionType, NNE_enabled, LoginType, status, databaseType, host, port, username, psswrd, databaseName, excepetd_statuscode
        ("incorrect_databasetype", "testConnection","Service Name", False, " ", " ", "Oracle", "192.168.0.174", 1521, "metadb", "metadb", "orcl", 200),
    ]
